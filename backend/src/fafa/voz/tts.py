"""Sintese de voz (o Fafa falando).

Tres motores atras da mesma interface:
- ElevenLabs: melhor naturalidade em pt-BR. Pago (tem faixa gratis pequena).
- OpenAI (gpt-4o-mini-tts): boa qualidade, mesma chave usada para transcrever.
- Windows (SAPI via pyttsx3): gratis e offline, qualidade de leitor de tela.
"""

from __future__ import annotations

import logging
import re
from abc import ABC, abstractmethod

import httpx

from fafa.config import Config, config as config_padrao
from fafa.voz.audio import TAXA_REPRODUCAO, reproduzir_pcm

log = logging.getLogger("fafa.voz.tts")


def limpar_para_fala(texto: str) -> str:
    """Remove marcacao que nao faz sentido falada (markdown, tabelas, codigo)."""
    t = re.sub(r"```.*?```", " (trecho de código omitido) ", texto, flags=re.S)
    t = re.sub(r"`([^`]*)`", r"\1", t)
    t = re.sub(r"^\s*\|.*\|\s*$", " ", t, flags=re.M)          # linhas de tabela
    t = re.sub(r"^\s{0,3}#{1,6}\s*", "", t, flags=re.M)         # cabecalhos
    t = re.sub(r"[*_]{1,3}([^*_]+)[*_]{1,3}", r"\1", t)         # negrito/italico
    t = re.sub(r"^\s*[-*•]\s+", "", t, flags=re.M)              # marcadores
    t = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", t)               # links
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n{2,}", ". ", t)
    t = t.replace("\n", " ")
    return t.strip()


class Voz(ABC):
    nome: str = "voz"

    @abstractmethod
    def sintetizar(self, texto: str) -> bytes:
        """Devolve PCM int16 mono a TAXA_REPRODUCAO. Vazio se o motor fala sozinho."""

    def falar(self, texto: str) -> None:
        texto = limpar_para_fala(texto)
        if not texto:
            return
        pcm = self.sintetizar(texto)
        if pcm:
            reproduzir_pcm(pcm, TAXA_REPRODUCAO)


class VozMuda(Voz):
    nome = "mudo"

    def sintetizar(self, texto: str) -> bytes:
        return b""


class VozElevenLabs(Voz):
    nome = "elevenlabs"

    def __init__(self, cfg: Config) -> None:
        if not (cfg.elevenlabs_api_key and cfg.elevenlabs_voice_id):
            raise RuntimeError("ELEVENLABS_API_KEY e ELEVENLABS_VOICE_ID sao obrigatorios")
        self.cfg = cfg

    def sintetizar(self, texto: str) -> bytes:
        r = httpx.post(
            f"https://api.elevenlabs.io/v1/text-to-speech/{self.cfg.elevenlabs_voice_id}",
            params={"output_format": "pcm_24000"},
            headers={"xi-api-key": self.cfg.elevenlabs_api_key, "accept": "audio/pcm"},
            json={
                "text": texto[:5000],
                "model_id": self.cfg.elevenlabs_model,
                "language_code": "pt",
                "voice_settings": {"stability": 0.5, "similarity_boost": 0.75, "speed": 1.0},
            },
            timeout=60,
        )
        r.raise_for_status()
        return r.content


class VozOpenAI(Voz):
    nome = "openai"

    def __init__(self, cfg: Config) -> None:
        if not cfg.openai_api_key:
            raise RuntimeError("OPENAI_API_KEY e obrigatoria")
        self.cfg = cfg

    def sintetizar(self, texto: str) -> bytes:
        r = httpx.post(
            "https://api.openai.com/v1/audio/speech",
            headers={"Authorization": f"Bearer {self.cfg.openai_api_key}"},
            json={
                "model": self.cfg.openai_tts_model,
                "voice": self.cfg.openai_tts_voice,
                "input": texto[:4096],
                "response_format": "pcm",  # 24 kHz, int16, mono
                "instructions": (
                    "Fale em português do Brasil, com sotaque neutro, tom profissional e "
                    "cordial, ritmo natural. Você é o Fafa, assistente técnico de engenharia."
                ),
            },
            timeout=60,
        )
        r.raise_for_status()
        return r.content


class VozWindows(Voz):
    """SAPI do Windows. Fala direto pelo pyttsx3, sem passar por PCM."""

    nome = "windows"

    def __init__(self, cfg: Config) -> None:
        import pyttsx3  # opcional

        self.motor = pyttsx3.init()
        self.motor.setProperty("rate", 185)
        for v in self.motor.getProperty("voices"):
            ident = f"{v.id} {v.name} {' '.join(v.languages or [])}".lower()
            if "pt-br" in ident or "brazil" in ident or "portug" in ident or "maria" in ident:
                self.motor.setProperty("voice", v.id)
                break

    def sintetizar(self, texto: str) -> bytes:
        self.motor.say(texto)
        self.motor.runAndWait()
        return b""


def criar_voz(cfg: Config | None = None) -> Voz:
    """Instancia o motor escolhido em FAFA_TTS (ou o melhor disponivel em 'auto')."""
    cfg = cfg or config_padrao
    motor = cfg.tts_efetivo
    if motor == "mudo":
        return VozMuda()
    if motor == "elevenlabs":
        return VozElevenLabs(cfg)
    if motor == "openai":
        return VozOpenAI(cfg)
    if motor == "windows":
        try:
            return VozWindows(cfg)
        except Exception as exc:  # noqa: BLE001
            log.warning("voz do Windows indisponivel (%s); ficando mudo", exc)
            return VozMuda()
    raise ValueError(f"FAFA_TTS invalido: {motor}")
