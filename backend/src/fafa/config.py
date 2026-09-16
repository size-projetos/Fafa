"""Configuracao central do Fafa, carregada de variaveis de ambiente / .env."""

from __future__ import annotations

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

RAIZ = Path(__file__).resolve().parents[2]


class Config(BaseSettings):
    """Todas as configuracoes do Fafa em um lugar so.

    Le de variaveis de ambiente e do arquivo .env na raiz do projeto.
    """

    model_config = SettingsConfigDict(
        env_file=RAIZ / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    # --- Cerebro ------------------------------------------------------------
    anthropic_api_key: str = ""
    fafa_model: str = "claude-sonnet-4-5"
    fafa_max_tokens: int = 4096

    # --- Identidade ---------------------------------------------------------
    fafa_nome: str = "Fafa"
    fafa_dono: str = "Daniel Broleis"
    fafa_empresa: str = "SIZE Engenharia Ambiental"

    # --- Persistencia -------------------------------------------------------
    fafa_db_path: str = "data/fafa.db"

    # --- Padroes tecnicos ---------------------------------------------------
    # SIRGAS 2000 / UTM 22S por padrao, conforme a convencao da SIZE.
    fafa_epsg_projetado: int = 31982
    fafa_epsg_geografico: int = 4674

    # --- Canais -------------------------------------------------------------
    telegram_bot_token: str = ""
    telegram_allowed_ids: str = ""

    whatsapp_token: str = ""
    whatsapp_phone_number_id: str = ""
    whatsapp_verify_token: str = ""
    whatsapp_allowed_numbers: str = ""

    fafa_web_host: str = "127.0.0.1"
    fafa_web_port: int = 8000          # painel web + API local
    fafa_whatsapp_port: int = 8001     # webhook do WhatsApp
    fafa_web_token: str = ""

    # --- Voz --------------------------------------------------------------
    # TTS: auto | elevenlabs | openai | windows | mudo
    fafa_tts: str = "auto"
    # STT: auto | openai | texto
    fafa_stt: str = "auto"
    fafa_voz_limiar: float = 0.012      # RMS (0-1) acima do qual ha fala
    fafa_voz_silencio_s: float = 1.2    # segundos de silencio que encerram a fala
    fafa_voz_max_s: float = 60.0        # duracao maxima de uma gravacao
    fafa_voz_espera_s: float = 8.0      # tempo esperando a fala comecar

    elevenlabs_api_key: str = ""
    elevenlabs_voice_id: str = ""
    elevenlabs_model: str = "eleven_flash_v2_5"

    openai_api_key: str = ""
    openai_tts_model: str = "gpt-4o-mini-tts"
    openai_tts_voice: str = "marin"
    openai_stt_model: str = "gpt-4o-mini-transcribe"

    # --- Derivados ----------------------------------------------------------
    @property
    def tts_efetivo(self) -> str:
        """Resolve 'auto' para o melhor motor de voz disponivel."""
        if self.fafa_tts != "auto":
            return self.fafa_tts
        if self.elevenlabs_api_key and self.elevenlabs_voice_id:
            return "elevenlabs"
        if self.openai_api_key:
            return "openai"
        return "windows"

    @property
    def stt_efetivo(self) -> str:
        if self.fafa_stt != "auto":
            return self.fafa_stt
        return "openai" if self.openai_api_key else "texto"

    @property
    def caminho_banco(self) -> Path:
        """Caminho absoluto do banco SQLite, com o diretorio ja criado."""
        p = Path(self.fafa_db_path)
        if not p.is_absolute():
            p = RAIZ / p
        p.parent.mkdir(parents=True, exist_ok=True)
        return p

    @property
    def telegram_ids_liberados(self) -> set[int]:
        """IDs de usuario do Telegram autorizados. Vazio = ninguem autorizado."""
        return {int(x) for x in _lista(self.telegram_allowed_ids) if x.isdigit()}

    @property
    def whatsapp_numeros_liberados(self) -> set[str]:
        """Numeros de WhatsApp autorizados, so digitos. Vazio = ninguem."""
        return {"".join(c for c in x if c.isdigit()) for x in _lista(self.whatsapp_allowed_numbers)}


def _lista(bruto: str) -> list[str]:
    """Quebra uma string separada por virgulas em itens limpos."""
    return [item.strip() for item in bruto.split(",") if item.strip()]


config = Config()
