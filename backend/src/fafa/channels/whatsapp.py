"""Canal WhatsApp via Meta Cloud API (API oficial).

Duas partes independentes:

1. `enviar_texto` / `CanalWhatsApp.notificar`: envio de mensagens. So precisa
   de token e Phone Number ID. E o que o Fafa usa para avisar "terminei" quando
   o Daniel saiu da frente do computador.

2. `criar_app`: servidor de webhook (FastAPI) que recebe mensagens do Daniel e
   responde pelo agente. A Meta precisa alcancar o servidor por uma URL
   publica HTTPS; num desktop isso se resolve com um tunel (cloudflared/ngrok).

Regra importante da Meta: fora da janela de 24 h apos a ultima mensagem do
usuario, so e possivel enviar mensagens de *template* aprovado. Para o aviso
"tarefa concluida" vale cadastrar um template simples ou manter a conversa
ativa mandando qualquer mensagem ao Fafa antes de sair.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

import httpx

try:  # o servidor de webhook e opcional: pip install "fafa[web]"
    from fastapi import BackgroundTasks, FastAPI, HTTPException, Request
    from fastapi.responses import PlainTextResponse
except ImportError:  # pragma: no cover
    FastAPI = None  # type: ignore[assignment]

from fafa.channels.base import Canal
from fafa.config import Config, config as config_padrao
from fafa.core.agent import Agente

log = logging.getLogger("fafa.whatsapp")

API_VERSAO = "v21.0"


def _url(cfg: Config) -> str:
    return f"https://graph.facebook.com/{API_VERSAO}/{cfg.whatsapp_phone_number_id}/messages"


def _so_digitos(numero: str) -> str:
    return "".join(c for c in numero if c.isdigit())


def enviar_texto(para: str, texto: str, cfg: Config | None = None) -> dict[str, Any]:
    """Envia uma mensagem de texto livre (dentro da janela de 24 h)."""
    cfg = cfg or config_padrao
    if not (cfg.whatsapp_token and cfg.whatsapp_phone_number_id):
        raise RuntimeError("WHATSAPP_TOKEN e WHATSAPP_PHONE_NUMBER_ID nao configurados")
    payload = {
        "messaging_product": "whatsapp",
        "to": _so_digitos(para),
        "type": "text",
        "text": {"preview_url": False, "body": texto[:4096]},
    }
    r = httpx.post(
        _url(cfg),
        headers={"Authorization": f"Bearer {cfg.whatsapp_token}"},
        json=payload,
        timeout=30,
    )
    r.raise_for_status()
    return r.json()


def enviar_template(
    para: str, nome_template: str, parametros: list[str], idioma: str = "pt_BR", cfg: Config | None = None
) -> dict[str, Any]:
    """Envia um template aprovado (funciona fora da janela de 24 h)."""
    cfg = cfg or config_padrao
    payload = {
        "messaging_product": "whatsapp",
        "to": _so_digitos(para),
        "type": "template",
        "template": {
            "name": nome_template,
            "language": {"code": idioma},
            "components": [
                {"type": "body", "parameters": [{"type": "text", "text": p} for p in parametros]}
            ]
            if parametros
            else [],
        },
    }
    r = httpx.post(
        _url(cfg),
        headers={"Authorization": f"Bearer {cfg.whatsapp_token}"},
        json=payload,
        timeout=30,
    )
    r.raise_for_status()
    return r.json()


class CanalWhatsApp(Canal):
    nome = "whatsapp"

    def enviar(self, usuario: str, texto: str) -> None:
        enviar_texto(usuario, texto, self.agente.config)

    def autorizado(self, numero: str) -> bool:
        liberados = self.agente.config.whatsapp_numeros_liberados
        return _so_digitos(numero) in liberados

    def tratar_evento(self, corpo: dict[str, Any]) -> int:
        """Processa um payload de webhook. Devolve quantas mensagens respondeu."""
        respondidas = 0
        for entrada in corpo.get("entry", []):
            for mudanca in entrada.get("changes", []):
                valor = mudanca.get("value", {})
                for msg in valor.get("messages", []):
                    if msg.get("type") != "text":
                        continue
                    numero = msg.get("from", "")
                    texto = (msg.get("text") or {}).get("body", "").strip()
                    if not texto:
                        continue
                    if not self.autorizado(numero):
                        log.warning("mensagem de numero nao autorizado: %s", numero)
                        continue
                    try:
                        resposta = self.processar(numero, texto)
                        self.enviar(numero, resposta.texto or "(sem resposta)")
                        respondidas += 1
                    except Exception as exc:  # noqa: BLE001
                        log.exception("erro ao responder %s", numero)
                        try:
                            self.enviar(numero, f"Deu erro aqui: {type(exc).__name__}: {exc}")
                        except Exception:  # noqa: BLE001
                            pass
        return respondidas


def abrir_tunel(porta: int, ao_url=None):
    """Sobe um tunel publico (cloudflared quick tunnel) para a porta local.

    Devolve o processo, e chama `ao_url(url)` quando a URL https://...trycloudflare.com
    aparecer no log. Se o cloudflared nao estiver instalado, devolve None.
    """
    import re
    import shutil
    import subprocess
    import threading

    exe = shutil.which("cloudflared")
    if not exe:
        for candidato in (
            r"C:\Program Files (x86)\cloudflared\cloudflared.exe",
            r"C:\Program Files\cloudflared\cloudflared.exe",
        ):
            if Path(candidato).exists():
                exe = candidato
                break
    if not exe:
        return None

    proc = subprocess.Popen(
        [exe, "tunnel", "--url", f"http://127.0.0.1:{porta}", "--no-autoupdate"],
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding="utf-8", errors="replace",
    )
    padrao = re.compile(r"https://[a-z0-9-]+\.trycloudflare\.com")

    estado = {"avisado": False}

    def ler2():
        assert proc.stdout is not None
        for linha in proc.stdout:
            m = padrao.search(linha)
            if m and not estado["avisado"] and ao_url:
                estado["avisado"] = True
                ao_url(m.group(0))

    threading.Thread(target=ler2, daemon=True).start()
    return proc


def criar_app(agente: Agente | None = None):
    """Cria a aplicacao FastAPI do webhook. Rode com `fafa whatsapp`."""
    if FastAPI is None:
        raise RuntimeError('FastAPI nao instalado. Rode: pip install "fafa[web]"')

    agente = agente or Agente()
    canal = CanalWhatsApp(agente)
    cfg = agente.config
    app = FastAPI(title="Fafa · webhook WhatsApp")

    @app.get("/saude")
    def saude() -> dict[str, str]:
        return {"status": "ok", "nome": cfg.fafa_nome}

    @app.get("/webhook")
    def verificar(request: Request):
        q = request.query_params
        if q.get("hub.mode") == "subscribe" and q.get("hub.verify_token") == cfg.whatsapp_verify_token:
            return PlainTextResponse(q.get("hub.challenge", ""))
        raise HTTPException(status_code=403, detail="verify token invalido")

    @app.post("/webhook")
    async def receber(request: Request, tarefas: BackgroundTasks) -> dict[str, str]:
        corpo = await request.json()
        # Responde 200 imediatamente; a Meta reenvia se demorar. O agente roda em segundo plano.
        tarefas.add_task(canal.tratar_evento, corpo)
        return {"status": "recebido"}

    return app
