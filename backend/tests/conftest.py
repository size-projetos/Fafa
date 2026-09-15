import pytest

import fafa.tools  # noqa: F401  (registra as ferramentas)
from fafa.config import Config
from fafa.core.memory import Memoria


@pytest.fixture
def cfg(tmp_path):
    return Config(anthropic_api_key="teste", fafa_db_path=str(tmp_path / "t.db"))


@pytest.fixture
def memoria(cfg):
    return Memoria(cfg.caminho_banco)
