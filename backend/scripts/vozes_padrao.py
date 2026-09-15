"""Vozes padrao da ElevenLabs (as unicas que o plano gratis usa pela API).

Uso:
  python scripts/vozes_padrao.py                   # lista
  python scripts/vozes_padrao.py --tocar Callum Daniel Brian   # fala a frase de teste em pt-BR com cada uma
  python scripts/vozes_padrao.py --usar Callum     # grava o voice_id no .env
"""

from __future__ import annotations

import argparse
import re
import sys
import time
from pathlib import Path

import httpx
from dotenv import load_dotenv

RAIZ = Path(__file__).resolve().parents[1]
load_dotenv(RAIZ / ".env")
from fafa.config import config  # noqa: E402
from fafa.voz.audio import reproduzir_pcm  # noqa: E402

API = "https://api.elevenlabs.io/v1"
FRASE = (
    "Daniel, terminei a tabela do Parque Germânico. São vinte e dois vértices e área de dois "
    "vírgula três hectares, em SIRGAS dois mil, fuso vinte e dois sul. Achei uma divergência de "
    "quatro centímetros no marco M-doze. Quer que eu mostre na tela?"
)


def _h():
    return {"xi-api-key": config.elevenlabs_api_key}


def vozes() -> list[dict]:
    r = httpx.get(f"{API}/voices", headers=_h(), timeout=60)
    r.raise_for_status()
    return [v for v in r.json()["voices"] if v.get("category") == "premade"]


def listar() -> None:
    for v in vozes():
        lab = v.get("labels") or {}
        print(f"{v['name']:<9} {lab.get('gender',''):<7} {lab.get('age',''):<12} "
              f"{lab.get('accent',''):<14} {lab.get('description',''):<16} {lab.get('use_case','')}")


def tocar(nomes: list[str]) -> None:
    por_nome = {v["name"].lower(): v for v in vozes()}
    for nome in nomes:
        v = por_nome.get(nome.lower())
        if not v:
            print(f"voz '{nome}' nao encontrada")
            continue
        print(f"▶ {v['name']}")
        r = httpx.post(
            f"{API}/text-to-speech/{v['voice_id']}",
            params={"output_format": "pcm_24000"},
            headers=_h(),
            json={"text": FRASE, "model_id": "eleven_multilingual_v2", "language_code": "pt",
                  "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}},
            timeout=90,
        )
        if r.status_code >= 400:
            print(f"  erro {r.status_code}: {r.text[:200]}")
            continue
        (RAIZ / "data" / "vozes").mkdir(parents=True, exist_ok=True)
        (RAIZ / "data" / "vozes" / f"padrao_{v['name']}.pcm").write_bytes(r.content)
        reproduzir_pcm(r.content, 24_000)
        time.sleep(1)


def usar(nome: str) -> None:
    por_nome = {v["name"].lower(): v for v in vozes()}
    v = por_nome.get(nome.lower())
    if not v:
        sys.exit(f"voz '{nome}' nao encontrada")
    env = RAIZ / ".env"
    c = env.read_text(encoding="utf-8")
    c = re.sub(r"(?m)^ELEVENLABS_VOICE_ID=.*$", f"ELEVENLABS_VOICE_ID={v['voice_id']}", c)
    env.write_text(c, encoding="utf-8")
    print(f"voz do Fafa agora: {v['name']} ({v['voice_id']})")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--tocar", nargs="+")
    ap.add_argument("--usar")
    a = ap.parse_args()
    if a.usar:
        usar(a.usar)
    elif a.tocar:
        tocar(a.tocar)
    else:
        listar()
