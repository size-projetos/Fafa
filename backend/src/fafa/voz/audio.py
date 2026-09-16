"""Captura e reproducao de audio.

Tudo em PCM 16 bits mono. Microfone a 16 kHz (o que os servicos de
transcricao esperam); reproducao a 24 kHz (o que ElevenLabs e OpenAI devolvem).
`sounddevice` e `numpy` sao importados sob demanda para o resto do Fafa
funcionar em maquinas sem placa de som.
"""

from __future__ import annotations

import io
import math
import struct
import sys
import time
import wave
from dataclasses import dataclass

TAXA_MIC = 16_000
TAXA_REPRODUCAO = 24_000


@dataclass(slots=True)
class Gravacao:
    pcm: bytes           # int16 mono
    taxa: int
    duracao_s: float
    teve_fala: bool

    def como_wav(self) -> bytes:
        return _pcm_para_wav(self.pcm, self.taxa)


def rms(bloco: bytes) -> float:
    """RMS normalizado (0-1) de um bloco PCM int16."""
    n = len(bloco) // 2
    if n == 0:
        return 0.0
    amostras = struct.unpack(f"<{n}h", bloco[: n * 2])
    return math.sqrt(sum(a * a for a in amostras) / n) / 32768.0


class DetectorDeFala:
    """Maquina de estados: espera fala -> gravando -> encerra apos silencio.

    Puro (sem audio), para ser testavel. Alimente com blocos e leia `terminou`.
    """

    def __init__(
        self,
        limiar: float,
        silencio_s: float,
        max_s: float,
        espera_s: float,
        bloco_s: float,
    ) -> None:
        self.limiar = limiar
        self.blocos_silencio_fim = max(1, int(silencio_s / bloco_s))
        self.blocos_max = max(1, int(max_s / bloco_s))
        self.blocos_espera = max(1, int(espera_s / bloco_s))
        self.teve_fala = False
        self.terminou = False
        self._silencio = 0
        self._total = 0

    def alimentar(self, nivel: float) -> None:
        if self.terminou:
            return
        self._total += 1
        if nivel >= self.limiar:
            self.teve_fala = True
            self._silencio = 0
        else:
            self._silencio += 1

        if self.teve_fala and self._silencio >= self.blocos_silencio_fim:
            self.terminou = True
        elif not self.teve_fala and self._total >= self.blocos_espera:
            self.terminou = True
        elif self._total >= self.blocos_max:
            self.terminou = True


def gravar(
    limiar: float,
    silencio_s: float,
    max_s: float,
    espera_s: float,
    ao_nivel=None,
) -> Gravacao:
    """Grava do microfone padrao ate detectar o fim da fala."""
    import sounddevice as sd  # importado aqui: opcional

    bloco_s = 0.05
    tamanho_bloco = int(TAXA_MIC * bloco_s)
    detector = DetectorDeFala(limiar, silencio_s, max_s, espera_s, bloco_s)
    partes: list[bytes] = []
    inicio = time.monotonic()

    with sd.RawInputStream(
        samplerate=TAXA_MIC, channels=1, dtype="int16", blocksize=tamanho_bloco
    ) as stream:
        while not detector.terminou:
            dados, _ = stream.read(tamanho_bloco)
            bloco = bytes(dados)
            nivel = rms(bloco)
            detector.alimentar(nivel)
            if ao_nivel:
                ao_nivel(nivel, detector.teve_fala)
            if detector.teve_fala:
                partes.append(bloco)

    pcm = b"".join(partes)
    return Gravacao(
        pcm=pcm,
        taxa=TAXA_MIC,
        duracao_s=len(pcm) / 2 / TAXA_MIC,
        teve_fala=detector.teve_fala,
    ) if detector.teve_fala else Gravacao(b"", TAXA_MIC, time.monotonic() - inicio, False)


def _pcm_para_wav(pcm: bytes, taxa: int) -> bytes:
    buf = io.BytesIO()
    with wave.open(buf, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(taxa)
        w.writeframes(pcm)
    return buf.getvalue()


def reproduzir_pcm(pcm: bytes, taxa: int = TAXA_REPRODUCAO) -> None:
    """Toca PCM int16 mono e espera terminar.

    No Windows usa o caminho nativo (winsound, o mesmo da voz do sistema), que
    respeita o dispositivo padrao inclusive com fones Bluetooth. Nos demais
    sistemas, ou se o winsound falhar, usa sounddevice.
    """
    if not pcm:
        return
    pcm = pcm[: len(pcm) - len(pcm) % 2]
    if sys.platform == "win32":
        try:
            import winsound

            winsound.PlaySound(_pcm_para_wav(pcm, taxa), winsound.SND_MEMORY)
            return
        except Exception:  # noqa: BLE001 - cai para o sounddevice
            pass
    import numpy as np
    import sounddevice as sd

    dados = np.frombuffer(pcm, dtype=np.int16)
    sd.play(dados, samplerate=taxa)
    sd.wait()


def dispositivos() -> str:
    """Lista os dispositivos de audio, para diagnostico."""
    import sounddevice as sd

    return str(sd.query_devices())
