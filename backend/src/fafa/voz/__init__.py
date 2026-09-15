"""Voz do Fafa: sintese (falar), reconhecimento (ouvir) e audio do microfone."""

from fafa.voz.stt import Ouvido, criar_ouvido
from fafa.voz.tts import Voz, criar_voz

__all__ = ["Voz", "Ouvido", "criar_voz", "criar_ouvido"]
