"""Reconhecimento de fala (o Fafa ouvindo)."""

from __future__ import annotations

import re
import unicodedata
from abc import ABC, abstractmethod

import httpx

from fafa.config import Config, config as config_padrao
from fafa.voz.audio import Gravacao, gravar


class Ouvido(ABC):
    nome: str = "ouvido"

    def __init__(self, cfg: Config) -> None:
        self.cfg = cfg

    def gravar(self, ao_nivel=None) -> Gravacao:
        return gravar(
            limiar=self.cfg.fafa_voz_limiar,
            silencio_s=self.cfg.fafa_voz_silencio_s,
            max_s=self.cfg.fafa_voz_max_s,
            espera_s=self.cfg.fafa_voz_espera_s,
            ao_nivel=ao_nivel,
        )

    @abstractmethod
    def transcrever(self, gravacao: Gravacao) -> str:
        """Texto reconhecido (vazio se nada foi entendido)."""

    def ouvir(self, ao_nivel=None) -> str:
        g = self.gravar(ao_nivel)
        if not g.teve_fala or g.duracao_s < 0.3:
            return ""
        return self.transcrever(g)


VOCABULARIO = (
    "Conversa técnica de topografia e engenharia: coordenadas UTM, SIRGAS 2000, "
    "vértices, azimute, memorial descritivo, loteamento, CORSAN, SIZE Engenharia."
)


def _normalizar(t: str) -> str:
    t = unicodedata.normalize("NFKD", t.lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9 ]+", " ", t).strip()


def eco_do_vocabulario(transcricao: str) -> bool:
    """True se o modelo devolveu o proprio prompt de vocabulario (alucinacao em silencio/ruido)."""
    a, b = _normalizar(transcricao), _normalizar(VOCABULARIO)
    if not a:
        return True
    if a in b or b in a:
        return True
    pa, pb = set(a.split()), set(b.split())
    return len(pa & pb) / max(1, len(pa)) > 0.7


class OuvidoOpenAI(Ouvido):
    nome = "openai"

    def __init__(self, cfg: Config) -> None:
        if not cfg.openai_api_key:
            raise RuntimeError("OPENAI_API_KEY e obrigatoria para transcrever")
        super().__init__(cfg)

    def transcrever(self, gravacao: Gravacao) -> str:
        r = httpx.post(
            "https://api.openai.com/v1/audio/transcriptions",
            headers={"Authorization": f"Bearer {self.cfg.openai_api_key}"},
            files={"file": ("fala.wav", gravacao.como_wav(), "audio/wav")},
            data={
                "model": self.cfg.openai_stt_model,
                "language": "pt",
                "response_format": "json",
                "prompt": VOCABULARIO,
            },
            timeout=60,
        )
        r.raise_for_status()
        texto = (r.json().get("text") or "").strip()
        return "" if eco_do_vocabulario(texto) else texto


def criar_ouvido(cfg: Config | None = None) -> Ouvido | None:
    """Instancia o reconhecedor escolhido; None significa 'so texto digitado'."""
    cfg = cfg or config_padrao
    motor = cfg.stt_efetivo
    if motor == "texto":
        return None
    if motor == "openai":
        return OuvidoOpenAI(cfg)
    raise ValueError(f"FAFA_STT invalido: {motor}")
