"""API local do painel: saude, chat, falar, ouvir e o painel estatico."""

from types import SimpleNamespace

import pytest

from fafa.channels import web
from fafa.config import Config
from fafa.core.agent import Agente, Resposta
from fafa.core.memory import Memoria

pytest.importorskip("fastapi")
from fastapi.testclient import TestClient  # noqa: E402


class AgenteEco(Agente):
    def __init__(self, cfg):
        super().__init__(config=cfg, memoria=Memoria(cfg.caminho_banco), cliente=object())
        self.recebidas = []

    def responder(self, texto, **kw):
        self.recebidas.append((kw["sessao_id"], texto))
        return Resposta(texto=f"eco: {texto}", ferramentas_usadas=["azimute_distancia"], rodadas=2)


@pytest.fixture
def cliente(tmp_path, monkeypatch):
    cfg = Config(anthropic_api_key="x", fafa_db_path=str(tmp_path / "t.db"), fafa_tts="mudo")
    agente = AgenteEco(cfg)
    return TestClient(web.criar_app(agente)), agente


def test_saude_e_painel(cliente):
    c, _ = cliente
    j = c.get("/api/saude").json()
    assert j["status"] == "ok" and j["voz"] == "mudo" and j["ouvido"] is None
    assert "tabela_vertices" in j["ferramentas"]
    r = c.get("/")  # painel estatico da v1
    assert r.status_code == 200 and "fafa-nucleo.js" in r.text
    assert c.get("/fafa-nucleo.js").status_code == 200


def test_chat(cliente):
    c, agente = cliente
    r = c.post("/api/chat", json={"texto": "oi", "usuario": "painel"})
    assert r.status_code == 200
    assert r.json() == {"texto": "eco: oi", "ferramentas": ["azimute_distancia"], "rodadas": 2}
    assert agente.recebidas == [("web:painel", "oi")]
    assert c.post("/api/chat", json={"texto": "   "}).status_code == 400


def test_falar_mudo_devolve_204(cliente):
    c, _ = cliente
    assert c.post("/api/falar", json={"texto": "olá"}).status_code == 204


def test_falar_devolve_wav(tmp_path, monkeypatch):
    cfg = Config(anthropic_api_key="x", fafa_db_path=str(tmp_path / "t.db"),
                 openai_api_key="k", fafa_tts="openai")
    monkeypatch.setattr(web, "criar_voz", lambda c: SimpleNamespace(
        nome="openai", sintetizar=lambda t: b"\x00\x01" * 2400))
    c = TestClient(web.criar_app(AgenteEco(cfg)))
    r = c.post("/api/falar", json={"texto": "**olá**"})
    assert r.status_code == 200 and r.headers["content-type"].startswith("audio/wav")
    assert r.content[:4] == b"RIFF"


def test_ouvir(tmp_path, monkeypatch):
    cfg = Config(anthropic_api_key="x", fafa_db_path=str(tmp_path / "t.db"),
                 openai_api_key="k", fafa_tts="mudo")
    c = TestClient(web.criar_app(AgenteEco(cfg)))
    monkeypatch.setattr(web.OuvidoOpenAI, "transcrever_arquivo",
                        lambda self, dados, nome, mime: f"{nome}|{mime}|{len(dados)}")
    r = c.post("/api/ouvir", files={"audio": ("fala.webm", b"x" * 5000, "audio/webm")})
    assert r.json()["texto"] == "fala.webm|audio/webm|5000"
    r = c.post("/api/ouvir", files={"audio": ("fala.webm", b"x" * 10, "audio/webm")})
    assert r.json()["texto"] == ""  # curto demais: nada


def test_ouvir_sem_chave_503(cliente):
    c, _ = cliente
    r = c.post("/api/ouvir", files={"audio": ("f.webm", b"x" * 5000, "audio/webm")})
    assert r.status_code == 503
