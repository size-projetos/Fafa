"""Diagnostico de captacao: qual microfone o Python ve, se ele capta som e se /api/ouvir transcreve."""

import math
import struct
import sys

import httpx
import sounddevice as sd

print("entrada padrao :", sd.query_devices(kind="input")["name"])
print("saida padrao   :", sd.query_devices(kind="output")["name"])
print("--- entradas disponiveis ---")
for i, d in enumerate(sd.query_devices()):
    api = sd.query_hostapis(d["hostapi"])["name"]
    if d["max_input_channels"] > 0 and ("MME" in api or "WASAPI" in api):
        print(f"  [{i}] {d['name']}  ({api})")

print("--- 4 s captando no mic padrao (fale algo!) ---")
partes = []
with sd.RawInputStream(samplerate=16000, channels=1, dtype="int16", blocksize=16000) as s:
    for k in range(4):
        b, _ = s.read(16000)
        b = bytes(b)
        partes.append(b)
        n = len(b) // 2
        a = struct.unpack(f"<{n}h", b)
        rms = math.sqrt(sum(x * x for x in a) / n) / 32768
        print(f"  s{k+1}: rms={rms:.4f}", "(som)" if rms > 0.012 else "(silencio)")

if "--transcrever" in sys.argv:
    from fafa.voz.audio import Gravacao

    g = Gravacao(b"".join(partes), 16000, 4.0, True)
    r = httpx.post("http://127.0.0.1:8000/api/ouvir",
                   files={"audio": ("fala.wav", g.como_wav(), "audio/wav")}, timeout=60)
    print("/api/ouvir ->", r.status_code, r.text[:200])
