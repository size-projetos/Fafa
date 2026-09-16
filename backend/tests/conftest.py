import pytest

import fafa.tools  # noqa: F401  (registra as ferramentas)
from fafa.config import Config
from fafa.core.memory import Memoria

_CHAVES = ("ANTHROPIC_API_KEY", "OPENAI_API_KEY", "ELEVENLABS_API_KEY", "ELEVENLABS_VOICE_ID",
           "FAFA_TTS", "FAFA_STT", "WHATSAPP_TOKEN", "WHATSAPP_ALLOWED_NUMBERS", "FAFA_DB_PATH")


@pytest.fixture(autouse=True)
def _sem_env_real(monkeypatch):
    """Os testes nao podem ler o backend/.env da maquina (chaves reais mudam o comportamento)."""
    monkeypatch.setitem(Config.model_config, "env_file", None)
    for chave in _CHAVES:
        monkeypatch.delenv(chave, raising=False)


@pytest.fixture
def cfg(tmp_path):
    return Config(anthropic_api_key="teste", fafa_db_path=str(tmp_path / "t.db"))


@pytest.fixture
def memoria(cfg):
    return Memoria(cfg.caminho_banco)
