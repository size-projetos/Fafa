"""Canal web: serve o painel (../src) e expoe a API local que liga o painel ao agente.

Rotas:
  GET  /api/saude         estado do nucleo (nome, voz, ouvido, ferramentas)
  POST /api/chat          {"texto": ..., "usuario": ...} -> {"texto", "ferramentas", "rodadas"}
  POST /api/falar         {"texto": ...} -> audio/wav (204 se o motor de voz e local/mudo)
  POST /api/ouvir         multipart "audio" (webm/ogg/wav) -> {"texto": ...}
  GET  /                  o painel estatico da v1 (src/)

Tudo fica em 127.0.0.1: e um aplicativo local, nao um servico publico.
"""

from __future__ import annotations

import logging
from pathlib import Path

from fafa import __version__
from fafa.channels.base import Canal
from fafa.config import RAIZ
from fafa.core.agent import Agente
from fafa.voz.audio import TAXA_REPRODUCAO, _pcm_para_wav
from fafa.voz.stt import OuvidoOpenAI, criar_ouvido
from fafa.voz.tts import VozComReserva, VozMuda, VozWindows, criar_voz, limpar_para_fala

try:
    from fastapi import FastAPI, File, HTTPException, UploadFile
    from fastapi.middleware.cors import CORSMiddleware
    from fastapi.responses import Response
    from fastapi.staticfiles import StaticFiles
    from pydantic import BaseModel
except ImportError:  # pragma: no cover
    FastAPI = None  # type: ignore[assignment]
    BaseModel = object  # type: ignore[assignment,misc]

log = logging.getLogger("fafa.web")


# Modelos no nivel do modulo: com "from __future__ import annotations" o FastAPI so
# resolve os tipos das rotas se eles forem visiveis no escopo global.
class Pergunta(BaseModel):
    texto: str
    usuario: str = "local"


class Fala(BaseModel):
    texto: str

PASTA_PAINEL = RAIZ.parent / "src"


class CanalWeb(Canal):
    nome = "web"

    def enviar(self, usuario: str, texto: str) -> None:  # a resposta volta pelo HTTP
        return None


def _motor_final(voz) -> str:
    """Nome do motor que de fato vai gerar audio agora (segue a cadeia de reservas)."""
    while isinstance(voz, VozComReserva):
        voz = voz.reserva if voz._usando_reserva else voz.principal
    return voz.nome


def criar_app(agente: Agente | None = None):
    if FastAPI is None:
        raise RuntimeError('FastAPI nao instalado. Rode: pip install "fafa[web]"')

    agente = agente or Agente()
    canal = CanalWeb(agente)
    cfg = agente.config
    voz = criar_voz(cfg)
    ouvido = criar_ouvido(cfg)

    app = FastAPI(title="Fafa · nucleo local", version=__version__)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://127.0.0.1", "http://localhost", "http://127.0.0.1:4173",
                       "http://localhost:4173", "null"],
        allow_origin_regex=r"https?://(127\.0\.0\.1|localhost)(:\d+)?",
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/api/saude")
    def saude() -> dict:
        return {
            "status": "ok",
            "nome": cfg.fafa_nome,
            "versao": __version__,
            "voz": _motor_final(voz),
            "ouvido": ouvido.nome if ouvido else None,
            "ferramentas": [f.nome for f in agente.registro.listar()],
        }

    @app.post("/api/chat")
    def chat(p: Pergunta) -> dict:
        texto = p.texto.strip()
        if not texto:
            raise HTTPException(400, "texto vazio")
        r = canal.processar(p.usuario, texto)
        return {"texto": r.texto, "ferramentas": r.ferramentas_usadas, "rodadas": r.rodadas}

    @app.post("/api/falar")
    def falar(f: Fala):
        texto = limpar_para_fala(f.texto)
        if not texto:
            return Response(status_code=204)
        # Motores locais (Windows) falam pelo proprio PC e nao devolvem PCM; o navegador
        # entao usa a sintese dele. Mudo: nada.
        alvo = voz
        while isinstance(alvo, VozComReserva):
            alvo = alvo.reserva if alvo._usando_reserva else alvo.principal
        if isinstance(alvo, (VozWindows, VozMuda)):
            return Response(status_code=204)
        try:
            pcm = voz.sintetizar(texto)
        except Exception as exc:  # noqa: BLE001
            log.warning("falar: %s", exc)
            return Response(status_code=204)
        if not pcm:
            return Response(status_code=204)
        return Response(content=_pcm_para_wav(pcm, TAXA_REPRODUCAO), media_type="audio/wav")

    @app.post("/api/ouvir")
    async def ouvir(audio: UploadFile = File(...)) -> dict:
        if not isinstance(ouvido, OuvidoOpenAI):
            raise HTTPException(503, "reconhecimento de voz nao configurado (OPENAI_API_KEY)")
        dados = await audio.read()
        if len(dados) < 2000:
            return {"texto": ""}
        nome = audio.filename or "fala.webm"
        mime = audio.content_type or "audio/webm"
        return {"texto": ouvido.transcrever_arquivo(dados, nome, mime)}

    if PASTA_PAINEL.is_dir():
        app.mount("/", StaticFiles(directory=str(PASTA_PAINEL), html=True), name="painel")
    else:  # pragma: no cover
        log.warning("painel nao encontrado em %s; servindo so a API", PASTA_PAINEL)

    return app


def abrir_como_app(url: str) -> None:
    """Abre a URL numa janela de aplicativo (Edge/Chrome --app) ou no navegador padrao."""
    import shutil
    import subprocess
    import webbrowser

    for nome in ("msedge", "chrome"):
        exe = shutil.which(nome)
        if exe:
            subprocess.Popen([exe, f"--app={url}", "--window-size=1440,900"])
            return
    # Windows: Edge fica fora do PATH
    for candidato in (
        Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
        Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
        Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
    ):
        if candidato.exists():
            subprocess.Popen([str(candidato), f"--app={url}", "--window-size=1440,900"])
            return
    webbrowser.open(url)
