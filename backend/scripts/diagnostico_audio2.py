"""Compara a captacao de dois microfones ao mesmo tempo (USB x Headset Baseus), 4 s."""

import math
import struct
import threading

import sounddevice as sd

ALVOS = {"USB [1]": 1, "Baseus [2]": 2}
resultados = {}


def captar(nome, idx):
    niveis = []
    try:
        with sd.RawInputStream(device=idx, samplerate=16000, channels=1, dtype="int16", blocksize=16000) as s:
            for _ in range(4):
                b = bytes(s.read(16000)[0])
                n = len(b) // 2
                a = struct.unpack(f"<{n}h", b)
                niveis.append(math.sqrt(sum(x * x for x in a) / n) / 32768)
    except Exception as exc:  # noqa: BLE001
        resultados[nome] = f"erro: {exc}"
        return
    resultados[nome] = niveis


threads = [threading.Thread(target=captar, args=(n, i)) for n, i in ALVOS.items()]
for t in threads:
    t.start()
for t in threads:
    t.join()
for nome, r in resultados.items():
    if isinstance(r, str):
        print(nome, r)
    else:
        print(nome, " ".join(f"{v:.4f}" for v in r), "-> pico", f"{max(r):.4f}", "(som)" if max(r) > 0.012 else "(silencio)")
