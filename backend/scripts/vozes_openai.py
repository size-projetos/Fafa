"""Toca a frase de teste com as vozes masculinas da OpenAI para escolher a reserva do Fafa.

Uso:
  python scripts/vozes_openai.py                 # onyx, ash, cedar, echo
  python scripts/vozes_openai.py marin verse     # vozes especificas
  python scripts/vozes_openai.py --usar onyx     # grava OPENAI_TTS_VOICE no .env
"""

from __future__ import annotations

import re
import sys
import time
from pathlib import Path

from dotenv import load_dotenv

RAIZ = Path(__file__).resolve().parents[1]
load_dotenv(RAIZ / ".env")
from fafa.config import Config  # noqa: E402
from fafa.voz.audio import reproduzir_pcm  # noqa: E402
from fafa.voz.tts import VozOpenAI  # noqa: E402

FRASE = (
    "Daniel, terminei a tabela do Parque Germânico. São vinte e dois vértices e área de dois "
    "vírgula três hectares, em SIRGAS dois mil, fuso vinte e dois sul. Achei uma divergência de "
    "quatro centímetros no marco M-doze. Quer que eu mostre na tela?"
)
PADRAO = ["onyx", "ash", "cedar", "echo"]


def main() -> None:
    args = sys.argv[1:]
    if args[:1] == ["--usar"]:
        voz = args[1]
        env = RAIZ / ".env"
        c = env.read_text(encoding="utf-8")
        c = re.sub(r"(?m)^OPENAI_TTS_VOICE=.*$", f"OPENAI_TTS_VOICE={voz}", c)
        env.write_text(c, encoding="utf-8")
        print(f"voz de reserva do Fafa: {voz}")
        return
    for nome in args or PADRAO:
        cfg = Config(openai_tts_voice=nome)
        print(f"▶ {nome}")
        try:
            pcm = VozOpenAI(cfg).sintetizar(FRASE)
        except Exception as exc:  # noqa: BLE001
            print(f"  erro: {exc}")
            continue
        (RAIZ / "data" / "vozes").mkdir(parents=True, exist_ok=True)
        (RAIZ / "data" / "vozes" / f"openai_{nome}.pcm").write_bytes(pcm)
        reproduzir_pcm(pcm, 24_000)
        time.sleep(1)


if __name__ == "__main__":
    main()
