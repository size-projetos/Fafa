"""Ferramentas para o agente guardar e apagar fatos duraveis."""

from __future__ import annotations

from fafa.core.agent import Contexto
from fafa.core.registry import ferramenta


@ferramenta(
    dominio="geral",
    descricoes={
        "chave": "Identificador curto do fato, ex.: 'cliente.prime_beach.contato'",
        "valor": "O fato em si, em uma frase",
    },
)
def lembrar(chave: str, valor: str, _ctx: Contexto) -> str:
    """Guarda um fato duravel na memoria de longo prazo do Fafa."""
    _ctx.memoria.lembrar(chave, valor, origem=_ctx.canal)
    return f"guardado: {chave}"


@ferramenta(dominio="geral", descricoes={"chave": "Chave do fato a apagar"})
def esquecer(chave: str, _ctx: Contexto) -> str:
    """Apaga um fato da memoria de longo prazo."""
    return "apagado" if _ctx.memoria.esquecer(chave) else "chave nao encontrada"


@ferramenta(dominio="geral")
def listar_memorias(_ctx: Contexto) -> dict[str, str]:
    """Lista todos os fatos guardados na memoria de longo prazo."""
    return _ctx.memoria.memorias()
