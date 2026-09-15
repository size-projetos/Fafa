"""Canal de voz no desktop: aperte Enter, fale, o Fafa responde falando.

Tambem aceita texto digitado (para quando o microfone nao ajuda) e os mesmos
comandos do terminal. Se nao houver reconhecedor configurado, vira um terminal
que fala as respostas.
"""

from __future__ import annotations

import sys

from fafa.channels.base import Canal
from fafa.channels.cli import AJUDA
from fafa.core.agent import Agente
from fafa.voz import criar_ouvido, criar_voz

AJUDA_VOZ = AJUDA + """  /mudo       liga/desliga a fala do Fafa
  /voz        mostra os motores de voz em uso
  Enter vazio grava do microfone; texto digitado e enviado direto
"""


class CanalVoz(Canal):
    nome = "voz"

    def __init__(self, agente: Agente, usuario: str = "local", mudo: bool = False) -> None:
        super().__init__(agente)
        self.usuario = usuario
        self.voz = criar_voz(agente.config)
        self.ouvido = criar_ouvido(agente.config)
        self.mudo = mudo

    # --- saida ---------------------------------------------------------------

    def enviar(self, usuario: str, texto: str) -> None:
        print(f"\n{self.agente.config.fafa_nome}: {texto}\n")
        if not self.mudo:
            try:
                self.voz.falar(texto)
            except Exception as exc:  # noqa: BLE001 - voz nunca derruba a conversa
                print(f"  (sem áudio: {type(exc).__name__}: {exc})", file=sys.stderr)

    def _progresso(self, texto: str) -> None:
        print(f"  · {texto}", file=sys.stderr)

    # --- entrada -------------------------------------------------------------

    def _mostrar_nivel(self, nivel: float, falando: bool) -> None:
        barras = "█" * min(30, int(nivel * 400))
        estado = "gravando" if falando else "aguardando fala"
        print(f"\r  {estado:<16} {barras:<30}", end="", file=sys.stderr, flush=True)

    def ouvir(self) -> str:
        if self.ouvido is None:
            print("  (sem reconhecimento de voz configurado; digite o texto)", file=sys.stderr)
            return ""
        try:
            texto = self.ouvido.ouvir(ao_nivel=self._mostrar_nivel)
        except Exception as exc:  # noqa: BLE001
            print(f"\n  erro no microfone: {type(exc).__name__}: {exc}", file=sys.stderr)
            return ""
        print("\r" + " " * 60 + "\r", end="", file=sys.stderr)
        return texto

    # --- loop ----------------------------------------------------------------

    def loop(self) -> None:
        nome = self.agente.config.fafa_nome
        ouvido = self.ouvido.nome if self.ouvido else "só texto"
        print(f"{nome} pronto · voz: {self.voz.nome} · ouvido: {ouvido}")
        print("Enter para falar, ou digite. /ajuda para os comandos.\n")

        while True:
            try:
                digitado = input("você: ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                break

            if digitado in ("/sair", "/exit", "/quit"):
                break
            if digitado == "/ajuda":
                print(AJUDA_VOZ)
                continue
            if digitado == "/mudo":
                self.mudo = not self.mudo
                print("fala desligada.\n" if self.mudo else "fala ligada.\n")
                continue
            if digitado == "/voz":
                print(f"  TTS: {self.voz.nome}   STT: {ouvido}\n")
                continue
            if digitado == "/limpar":
                self.agente.memoria.limpar_sessao(self.sessao_id(self.usuario))
                print("histórico apagado.\n")
                continue
            if digitado == "/memorias":
                for k, v in self.agente.memoria.memorias().items():
                    print(f"  {k}: {v}")
                print()
                continue
            if digitado == "/tools":
                for f in self.agente.registro.listar():
                    print(f"  [{f.dominio}] {f.nome}")
                print()
                continue

            texto = digitado or self.ouvir()
            if not texto:
                if not digitado:
                    print("  não entendi nada; tente de novo ou digite.\n")
                continue
            if not digitado:
                print(f"você (voz): {texto}")

            try:
                resposta = self.processar(self.usuario, texto, ao_progresso=self._progresso)
            except Exception as exc:  # noqa: BLE001
                print(f"\nerro: {exc}\n", file=sys.stderr)
                continue
            self.enviar(self.usuario, resposta.texto)
