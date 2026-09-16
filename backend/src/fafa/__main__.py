"""Ponto de entrada: `fafa <comando>` ou `python -m fafa <comando>`."""

from __future__ import annotations

import argparse
import logging
import sys

from fafa import __version__


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="fafa", description="Fafa · assistente tecnico da SIZE")
    parser.add_argument("--version", action="version", version=f"fafa {__version__}")
    parser.add_argument("-v", "--verbose", action="store_true", help="logs detalhados")
    sub = parser.add_subparsers(dest="comando")

    p_chat = sub.add_parser("chat", help="conversa no terminal (padrao)")
    p_chat.add_argument("--usuario", default="local")

    p_web = sub.add_parser("web", help="abre o painel do Fafa ligado ao nucleo (aplicativo)")
    p_web.add_argument("--porta", type=int, default=None)
    p_web.add_argument("--sem-janela", action="store_true", help="so sobe o servidor")

    p_voz = sub.add_parser("voz", help="conversa por voz no desktop (Enter para falar)")
    p_voz.add_argument("--usuario", default="local")
    p_voz.add_argument("--mudo", action="store_true", help="nao fala as respostas")

    sub.add_parser("audio", help="lista os dispositivos de audio (diagnostico)")

    sub.add_parser("tools", help="lista as ferramentas registradas")

    p_wa = sub.add_parser("whatsapp", help="sobe o servidor de webhook do WhatsApp")
    p_wa.add_argument("--host", default=None)
    p_wa.add_argument("--porta", type=int, default=None)

    p_not = sub.add_parser("notificar", help="envia um aviso por WhatsApp")
    p_not.add_argument("numero", help="numero com DDI, ex.: 5551982835944")
    p_not.add_argument("texto")

    args = parser.parse_args(argv)
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(name)s %(levelname)s %(message)s",
    )

    from fafa.core.agent import Agente
    import fafa.tools  # noqa: F401  (registra as ferramentas)

    comando = args.comando or "chat"

    if comando == "chat":
        from fafa.channels.cli import CanalCli

        CanalCli(Agente(), usuario=args.usuario).loop()
        return 0

    if comando == "web":
        import threading

        import uvicorn

        from fafa.channels.web import abrir_como_app, criar_app
        from fafa.config import config

        porta = args.porta or config.fafa_web_port
        url = f"http://{config.fafa_web_host}:{porta}/"
        app = criar_app(Agente())
        if not args.sem_janela:
            threading.Timer(1.2, abrir_como_app, args=(url,)).start()
        print(f"{config.fafa_nome} · painel em {url}  (Ctrl+C para encerrar)")
        uvicorn.run(app, host=config.fafa_web_host, port=porta, log_level="warning")
        return 0

    if comando == "voz":
        from fafa.channels.voz import CanalVoz

        CanalVoz(Agente(), usuario=args.usuario, mudo=args.mudo).loop()
        return 0

    if comando == "audio":
        from fafa.config import config
        from fafa.voz.audio import dispositivos

        print(f"TTS: {config.tts_efetivo}   STT: {config.stt_efetivo}\n")
        print(dispositivos())
        return 0

    if comando == "tools":
        from fafa.core.registry import registro

        for f in registro.listar():
            print(f"[{f.dominio}] {f.nome}")
            print(f"    {f.descricao.splitlines()[0]}")
            for p, s in f.schema["properties"].items():
                obrig = "*" if p in f.schema["required"] else " "
                print(f"    {obrig} {p}: {s.get('type')} — {s.get('description', '')}")
        return 0

    if comando == "whatsapp":
        import uvicorn

        from fafa.channels.whatsapp import criar_app
        from fafa.config import config

        uvicorn.run(
            criar_app(Agente()),
            host=args.host or config.fafa_web_host,
            port=args.porta or config.fafa_whatsapp_port,
        )
        return 0

    if comando == "notificar":
        from fafa.channels.whatsapp import enviar_texto

        print(enviar_texto(args.numero, args.texto))
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
