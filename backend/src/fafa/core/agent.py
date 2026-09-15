"""O agente: loop de conversa com a API da Anthropic e execucao de ferramentas.

Um unico Agente serve todos os canais. Cada canal identifica a conversa por um
`sessao_id` (ex.: "cli:daniel", "whatsapp:5551982835944") e o agente cuida de
recuperar o historico, chamar o modelo, executar ferramentas e persistir tudo.
"""

from __future__ import annotations

import inspect
import json
import logging
import traceback
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any

from fafa.config import Config, config as config_padrao
from fafa.core.imagem import Imagem, ResultadoVisual
from fafa.core.memory import Memoria, Mensagem
from fafa.core.registry import Registro, registro as registro_padrao

log = logging.getLogger("fafa.agente")

MAX_RODADAS_FERRAMENTA = 12

_NOTAS_CANAL = {
    "voz": (
        "Canal atual: VOZ. O usuario esta falando com voce e vai OUVIR a resposta. "
        "Responda como em uma conversa: 1 a 3 frases, sem listas, tabelas, markdown ou "
        "simbolos. Coordenadas e numeros longos: diga so o essencial e ofereca mostrar a "
        "tabela completa na tela. Se precisar de varias etapas, avise em uma frase e faca."
    ),
    "whatsapp": "Canal atual: WhatsApp. Respostas curtas, sem markdown.",
}


@dataclass(slots=True)
class Contexto:
    """O que uma ferramenta recebe alem dos seus proprios argumentos.

    Ferramentas que declaram um parametro `_ctx` recebem esta instancia.
    """

    config: Config
    memoria: Memoria
    sessao_id: str
    canal: str
    usuario: str


@dataclass(slots=True)
class Resposta:
    """Resultado de uma rodada de conversa."""

    texto: str
    ferramentas_usadas: list[str] = field(default_factory=list)
    rodadas: int = 0
    tokens_entrada: int = 0
    tokens_saida: int = 0


class Agente:
    """Orquestra uma conversa: modelo <-> ferramentas <-> memoria."""

    def __init__(
        self,
        config: Config | None = None,
        memoria: Memoria | None = None,
        registro: Registro | None = None,
        cliente: Any | None = None,
    ) -> None:
        self.config = config or config_padrao
        self.memoria = memoria or Memoria(self.config.caminho_banco)
        self.registro = registro or registro_padrao
        self._cliente = cliente  # injetavel para testes; criado sob demanda

    # --- Cliente da API -------------------------------------------------------

    @property
    def cliente(self) -> Any:
        if self._cliente is None:
            if not self.config.anthropic_api_key:
                raise RuntimeError(
                    "ANTHROPIC_API_KEY nao configurada. Copie .env.example para .env e preencha."
                )
            from anthropic import Anthropic

            self._cliente = Anthropic(api_key=self.config.anthropic_api_key)
        return self._cliente

    # --- Prompt de sistema ----------------------------------------------------

    def prompt_sistema(self, canal: str = "cli") -> str:
        c = self.config
        memorias = self.memoria.memorias()
        bloco_memorias = (
            "\n".join(f"- {k}: {v}" for k, v in memorias.items()) if memorias else "- (nenhuma ainda)"
        )
        return f"""Voce e {c.fafa_nome}, assistente tecnico pessoal de {c.fafa_dono}, da {c.fafa_empresa}.

Sua especialidade e topografia, georreferenciamento e geoprocessamento. Voce e
direto, preciso e fala portugues do Brasil. Nao inventa numeros: quando um
calculo e necessario, usa as ferramentas disponiveis.

Padroes tecnicos da empresa (adote sempre que o usuario nao disser o contrario):
- Sistema de coordenadas: SIRGAS 2000 / UTM fuso 22S (EPSG:{c.fafa_epsg_projetado});
  geografico SIRGAS 2000 (EPSG:{c.fafa_epsg_geografico}).
- Numeracao de vertices: sequencial e crescente.
- Tabelas de coordenadas: incluir LATITUDE e LONGITUDE em graus decimais
  (6 casas) e a coluna CONFRONTANTE.
- Precisao: coordenadas UTM com 3 casas decimais; distancias em metros com
  2 casas; azimutes em graus, minutos e segundos.

Memorias duraveis (fatos que voce guardou em conversas anteriores):
{bloco_memorias}

Voce enxerga: `ver_tela` captura a tela do computador, `ver_arquivo` abre
imagens, PDFs e textos, `ver_camera` tira uma foto pela webcam. Quando o
usuario disser "olha isso", "ve aqui", "o que e isso na tela", use `ver_tela`
sem pedir confirmacao. Descreva o que ve com precisao tecnica e admita quando
algo estiver ilegivel.

Quando o usuario disser algo que vale lembrar para sempre (nome de projeto,
cliente, decisao, preferencia), use a ferramenta `lembrar`. Nao guarde dados
sensiveis ou passageiros.

Responda de forma objetiva. Em canais de mensagem (WhatsApp) prefira respostas
curtas e sem markdown pesado.
{_NOTAS_CANAL.get(canal, "")}"""

    # --- Conversa -------------------------------------------------------------

    def responder(
        self,
        texto: str,
        *,
        sessao_id: str,
        canal: str,
        usuario: str,
        ao_progresso: Callable[[str], None] | None = None,
    ) -> Resposta:
        """Processa uma mensagem do usuario e devolve a resposta final.

        `ao_progresso` e chamado com um texto curto sempre que uma ferramenta e
        executada, util para o canal mostrar "calculando..." ao usuario.
        """
        self.memoria.garantir_sessao(sessao_id, canal, usuario)
        ctx = Contexto(self.config, self.memoria, sessao_id, canal, usuario)

        mensagens = [m.para_api() for m in self.memoria.historico(sessao_id)]
        nova = Mensagem("user", texto)
        mensagens.append(nova.para_api())
        self.memoria.adicionar_mensagem(sessao_id, nova)

        resposta = Resposta(texto="")
        ferramentas = self.registro.schemas()
        textos: list[str] = []  # texto de todas as rodadas, nao so da ultima

        for rodada in range(1, MAX_RODADAS_FERRAMENTA + 1):
            resposta.rodadas = rodada
            saida = self.cliente.messages.create(
                model=self.config.fafa_model,
                max_tokens=self.config.fafa_max_tokens,
                system=self.prompt_sistema(canal),
                messages=mensagens,
                tools=ferramentas or None,
            )
            uso = getattr(saida, "usage", None)
            if uso is not None:
                resposta.tokens_entrada += getattr(uso, "input_tokens", 0) or 0
                resposta.tokens_saida += getattr(uso, "output_tokens", 0) or 0

            blocos = [_bloco_para_dict(b) for b in saida.content]
            msg_assistente = Mensagem("assistant", blocos)
            mensagens.append(msg_assistente.para_api())
            self.memoria.adicionar_mensagem(sessao_id, msg_assistente)

            parcial = _texto_dos_blocos(blocos)
            if parcial:
                textos.append(parcial)

            chamadas = [b for b in blocos if b.get("type") == "tool_use"]
            if saida.stop_reason != "tool_use" or not chamadas:
                resposta.texto = "\n\n".join(textos)
                return resposta

            resultados_api = []
            resultados_memoria = []
            for chamada in chamadas:
                nome = chamada["name"]
                resposta.ferramentas_usadas.append(nome)
                if ao_progresso:
                    ao_progresso(f"executando {nome}...")
                para_api, para_memoria, erro = self._executar(nome, chamada.get("input") or {}, ctx)
                base = {"type": "tool_result", "tool_use_id": chamada["id"]}
                if erro:
                    base["is_error"] = True
                resultados_api.append({**base, "content": para_api})
                resultados_memoria.append({**base, "content": para_memoria})

            mensagens.append({"role": "user", "content": resultados_api})
            self.memoria.adicionar_mensagem(sessao_id, Mensagem("user", resultados_memoria))

        resposta.texto = (
            "Atingi o limite de etapas para esta tarefa sem concluir. "
            "Pode dividir o pedido em partes menores?"
        )
        return resposta

    # --- Execucao de ferramentas ----------------------------------------------

    def _executar(
        self, nome: str, entrada: dict[str, Any], ctx: Contexto
    ) -> tuple[Any, Any, bool]:
        """Executa uma ferramenta.

        Devolve (conteudo_para_api, conteudo_para_memoria, houve_erro). Os dois sao
        iguais para texto; para imagens, a API recebe os blocos `image` e a memoria
        recebe so um marcador textual.
        """
        f = self.registro.obter(nome)
        if f is None:
            msg = f"Ferramenta desconhecida: {nome}"
            return msg, msg, True
        try:
            kwargs = dict(entrada)
            if "_ctx" in inspect.signature(f.funcao).parameters:
                kwargs["_ctx"] = ctx
            resultado = f.executar(**kwargs)
        except Exception as exc:  # noqa: BLE001 - o modelo precisa ver o erro
            log.warning("erro na ferramenta %s: %s\n%s", nome, exc, traceback.format_exc())
            msg = f"Erro ao executar {nome}: {type(exc).__name__}: {exc}"
            return msg, msg, True

        if isinstance(resultado, Imagem):
            resultado = ResultadoVisual([resultado])
        if isinstance(resultado, ResultadoVisual):
            blocos: list[dict[str, Any]] = [im.bloco_api() for im in resultado.imagens]
            marcadores = " ".join(im.marcador() for im in resultado.imagens)
            texto = (resultado.texto + " " if resultado.texto else "") + marcadores
            blocos.append({"type": "text", "text": texto.strip()})
            return blocos, texto.strip(), False

        texto = _serializar(resultado)
        return texto, texto, False


# --- Utilitarios --------------------------------------------------------------


def _bloco_para_dict(bloco: Any) -> dict[str, Any]:
    """Converte um bloco de conteudo do SDK em dict serializavel."""
    if isinstance(bloco, dict):
        return bloco
    if hasattr(bloco, "model_dump"):
        d = bloco.model_dump()
        # Remove campos nulos que a API nao aceita de volta.
        return {k: v for k, v in d.items() if v is not None}
    tipo = getattr(bloco, "type", "text")
    if tipo == "text":
        return {"type": "text", "text": getattr(bloco, "text", "")}
    if tipo == "tool_use":
        return {
            "type": "tool_use",
            "id": getattr(bloco, "id"),
            "name": getattr(bloco, "name"),
            "input": getattr(bloco, "input", {}),
        }
    return {"type": tipo}


def _texto_dos_blocos(blocos: list[dict[str, Any]]) -> str:
    return "\n".join(b.get("text", "") for b in blocos if b.get("type") == "text").strip()


def _serializar(valor: Any) -> str:
    if valor is None:
        return "ok"
    if isinstance(valor, str):
        return valor
    try:
        return json.dumps(valor, ensure_ascii=False, indent=2, default=str)
    except TypeError:
        return str(valor)
