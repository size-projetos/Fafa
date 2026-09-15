"""Canal de terminal: conversa com o Fafa direto no PowerShell / shell."""

from __future__ import annotations

import sys

from fafa.channels.base import Canal
from fafa.core.agent import Agente

AJUDA = """comandos:
  /limpar     apaga o historico desta sessao
  /memorias   lista as memorias de longo prazo
  /tools      lista as ferramentas disponiveis
  /sair       encerra
"""


class CanalCli(Canal):
    nome = "cli"

    def __init__(self, agente: Agente, usuario: str = "local") -> None:
        super().__init__(agente)
        self.usuario = usuario

    def enviar(self, usuario: str, texto: str) -> None:
        print(f"\n{self.agente.config.fafa_nome}: {texto}\n")

    def _progresso(self, texto: str) -> None:
        print(f"  · {texto}", file=sys.stderr)

    def loop(self) -> None:
        nome = self.agente.config.fafa_nome
        print(f"{nome} pronto. Digite /ajuda para os comandos.\n")
        while True:
            try:
                texto = input("você: ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                break
            if not texto:
                continue
            if texto in ("/sair", "/exit", "/quit"):
                break
            if texto == "/ajuda":
                print(AJUDA)
                continue
            if texto == "/limpar":
                self.agente.memoria.limpar_sessao(self.sessao_id(self.usuario))
                print("historico apagado.\n")
                continue
            if texto == "/memorias":
                for k, v in self.agente.memoria.memorias().items():
                    print(f"  {k}: {v}")
                print()
                continue
            if texto == "/tools":
                for f in self.agente.registro.listar():
                    print(f"  [{f.dominio}] {f.nome} — {f.descricao.splitlines()[0]}")
                print()
                continue

            try:
                resposta = self.processar(self.usuario, texto, ao_progresso=self._progresso)
            except Exception as exc:  # noqa: BLE001
                print(f"\nerro: {exc}\n", file=sys.stderr)
                continue
            self.enviar(self.usuario, resposta.texto)
