"""Voz: deteccao de fala, limpeza de texto, escolha de motor e chamadas HTTP (simuladas)."""

import struct

import httpx
import pytest

from fafa.config import Config
from fafa.voz import audio, stt, tts


# --- audio -------------------------------------------------------------------

def _pcm(amplitude: int, n: int = 800) -> bytes:
    return struct.pack(f"<{n}h", *([amplitude, -amplitude] * (n // 2)))


def test_rms():
    assert audio.rms(b"") == 0.0
    assert audio.rms(_pcm(0)) == 0.0
    assert abs(audio.rms(_pcm(16384)) - 0.5) < 1e-6


def test_detector_encerra_apos_silencio():
    d = audio.DetectorDeFala(limiar=0.1, silencio_s=0.2, max_s=10, espera_s=5, bloco_s=0.05)
    for _ in range(3):
        d.alimentar(0.0)          # silencio inicial nao conta como fim
    assert not d.terminou
    for _ in range(4):
        d.alimentar(0.5)          # fala
    assert d.teve_fala and not d.terminou
    for _ in range(3):
        d.alimentar(0.0)
    assert not d.terminou         # 0.15 s de silencio ainda nao chega a 0.2
    d.alimentar(0.0)
    assert d.terminou


def test_detector_desiste_sem_fala():
    d = audio.DetectorDeFala(limiar=0.1, silencio_s=1, max_s=10, espera_s=0.5, bloco_s=0.1)
    for _ in range(5):
        d.alimentar(0.01)
    assert d.terminou and not d.teve_fala


def test_detector_respeita_maximo():
    d = audio.DetectorDeFala(limiar=0.1, silencio_s=5, max_s=0.3, espera_s=5, bloco_s=0.1)
    for _ in range(3):
        d.alimentar(0.9)
    assert d.terminou and d.teve_fala


def test_gravacao_vira_wav_valido():
    g = audio.Gravacao(pcm=_pcm(1000), taxa=16000, duracao_s=0.05, teve_fala=True)
    wav = g.como_wav()
    assert wav[:4] == b"RIFF" and wav[8:12] == b"WAVE"
    assert struct.unpack("<I", wav[24:28])[0] == 16000


# --- texto para fala ---------------------------------------------------------

def test_limpar_para_fala():
    t = "## Resultado\n\n- **Área:** 1,0 ha\n- Perímetro: `400 m`\n\n| a | b |\n|---|---|\n\n```py\nx=1\n```\nFim [link](http://x)."
    limpo = tts.limpar_para_fala(t)
    assert "#" not in limpo and "*" not in limpo and "|" not in limpo and "`" not in limpo
    assert "Área: 1,0 ha" in limpo and "Perímetro: 400 m" in limpo
    assert "trecho de código omitido" in limpo
    assert "Fim link." in limpo


# --- escolha de motor --------------------------------------------------------

def test_auto_escolhe_pela_chave_disponivel(tmp_path):
    base = dict(anthropic_api_key="x", fafa_db_path=str(tmp_path / "t.db"))
    assert Config(**base).tts_efetivo == "windows"
    assert Config(**base).stt_efetivo == "texto"
    assert Config(**base, openai_api_key="k").tts_efetivo == "openai"
    assert Config(**base, openai_api_key="k").stt_efetivo == "openai"
    assert Config(**base, openai_api_key="k", elevenlabs_api_key="e",
                  elevenlabs_voice_id="v").tts_efetivo == "elevenlabs"
    assert Config(**base, fafa_tts="mudo", openai_api_key="k").tts_efetivo == "mudo"


def test_criar_voz_muda_e_erros(tmp_path):
    cfg = Config(anthropic_api_key="x", fafa_db_path=str(tmp_path / "t.db"), fafa_tts="mudo")
    assert isinstance(tts.criar_voz(cfg), tts.VozMuda)
    with pytest.raises(RuntimeError):
        tts.VozElevenLabs(Config(anthropic_api_key="x", fafa_db_path=str(tmp_path / "t.db")))
    assert stt.criar_ouvido(Config(anthropic_api_key="x", fafa_db_path=str(tmp_path / "t.db"))) is None


# --- chamadas HTTP simuladas -------------------------------------------------

class _Resp:
    def __init__(self, content=b"", json=None, status=200):
        self.content = content
        self._json = json or {}
        self.status_code = status

    def raise_for_status(self):
        if self.status_code >= 400:
            raise httpx.HTTPStatusError("erro", request=None, response=None)

    def json(self):
        return self._json


def test_elevenlabs_monta_requisicao(monkeypatch, tmp_path):
    chamadas = {}

    def post(url, **kw):
        chamadas.update(url=url, **kw)
        return _Resp(content=b"\x00\x01" * 100)

    monkeypatch.setattr(tts.httpx, "post", post)
    cfg = Config(anthropic_api_key="x", fafa_db_path=str(tmp_path / "t.db"),
                 elevenlabs_api_key="ek", elevenlabs_voice_id="VOZ1")
    pcm = tts.VozElevenLabs(cfg).sintetizar("olá")
    assert pcm == b"\x00\x01" * 100
    assert chamadas["url"].endswith("/text-to-speech/VOZ1")
    assert chamadas["params"] == {"output_format": "pcm_24000"}
    assert chamadas["headers"]["xi-api-key"] == "ek"
    assert chamadas["json"]["model_id"] == "eleven_flash_v2_5"
    assert chamadas["json"]["text"] == "olá"


def test_openai_tts_e_stt(monkeypatch, tmp_path):
    chamadas = []

    def post(url, **kw):
        chamadas.append((url, kw))
        if url.endswith("/audio/speech"):
            return _Resp(content=b"\x02\x03" * 10)
        return _Resp(json={"text": " azimute de noventa graus "})

    monkeypatch.setattr(tts.httpx, "post", post)
    monkeypatch.setattr(stt.httpx, "post", post)
    cfg = Config(anthropic_api_key="x", fafa_db_path=str(tmp_path / "t.db"), openai_api_key="ok")

    assert tts.VozOpenAI(cfg).sintetizar("oi") == b"\x02\x03" * 10
    corpo = chamadas[0][1]["json"]
    assert corpo["response_format"] == "pcm" and corpo["voice"] == "marin"

    g = audio.Gravacao(pcm=_pcm(500), taxa=16000, duracao_s=1.0, teve_fala=True)
    assert stt.OuvidoOpenAI(cfg).transcrever(g) == "azimute de noventa graus"
    dados = chamadas[1][1]["data"]
    assert dados["model"] == "gpt-4o-mini-transcribe" and dados["language"] == "pt"
    assert chamadas[1][1]["files"]["file"][0] == "fala.wav"


def test_ouvir_ignora_gravacao_sem_fala(monkeypatch, tmp_path):
    cfg = Config(anthropic_api_key="x", fafa_db_path=str(tmp_path / "t.db"), openai_api_key="ok")
    o = stt.OuvidoOpenAI(cfg)
    monkeypatch.setattr(o, "gravar", lambda ao_nivel=None: audio.Gravacao(b"", 16000, 8.0, False))
    monkeypatch.setattr(o, "transcrever", lambda g: pytest.fail("nao devia transcrever"))
    assert o.ouvir() == ""


def test_prompt_do_canal_voz(tmp_path):
    from fafa.core.agent import Agente
    from fafa.core.memory import Memoria

    cfg = Config(anthropic_api_key="x", fafa_db_path=str(tmp_path / "t.db"))
    a = Agente(config=cfg, memoria=Memoria(cfg.caminho_banco), cliente=object())
    assert "Canal atual: VOZ" in a.prompt_sistema("voz")
    assert "Canal atual" not in a.prompt_sistema("cli")
