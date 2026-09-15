"""Voice Design da ElevenLabs: gera variacoes de voz para o Fafa, toca no fone e salva a escolhida.

Uso:
  python scripts/desenhar_voz.py                 # gera 3 previas, toca e guarda em data/vozes/
  python scripts/desenhar_voz.py --tocar          # so toca de novo as previas ja geradas
  python scripts/desenhar_voz.py --salvar 2       # salva a previa 2 como voz "Fafa" e grava o ID no .env
  python scripts/desenhar_voz.py --mais-rouca     # variante da descricao com mais textura
  python scripts/desenhar_voz.py --menos-rouca    # variante sem rouquidao
"""

from __future__ import annotations

import argparse
import base64
import json
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

PASTA = RAIZ / "data" / "vozes"
API = "https://api.elevenlabs.io/v1"

DESCRICAO = (
    "Male voice, mid-40s, Brazilian Portuguese with a neutral southern accent. Warm, slightly "
    "raspy and textured timbre - like a rock singer speaking, not singing. Medium-low pitch, never "
    "boomy. Calm, unhurried rhythm; confident and direct, as if speaking to a colleague across the "
    "table. Understated charisma: sounds engaged, never theatrical or salesy. Clear articulation of "
    "technical terms. Studio-quality, close-mic, no reverb."
)
MAIS_ROUCA = DESCRICAO.replace(
    "Warm, slightly raspy and textured timbre",
    "Warm, distinctly raspy, gravelly and textured timbre",
)
MENOS_ROUCA = DESCRICAO.replace(
    "Warm, slightly raspy and textured timbre - like a rock singer speaking, not singing.",
    "Warm, smooth and textured timbre with a calm, grounded presence.",
)

TEXTO = (
    "Daniel, terminei a tabela do Parque Germânico. São vinte e dois vértices, perímetro de "
    "oitocentos e quarenta metros e área de dois vírgula três hectares, tudo em SIRGAS dois mil, "
    "fuso vinte e dois sul. Encontrei uma divergência de quatro centímetros no marco M-doze. "
    "Quer que eu mostre na tela?"
)


def _cabecalho() -> dict[str, str]:
    if not config.elevenlabs_api_key:
        sys.exit("ELEVENLABS_API_KEY nao configurada no .env")
    return {"xi-api-key": config.elevenlabs_api_key}


def gerar(descricao: str) -> list[dict]:
    PASTA.mkdir(parents=True, exist_ok=True)
    print("gerando variações no Voice Design (leva ~20 s)...")
    r = httpx.post(
        f"{API}/text-to-voice/design",
        headers=_cabecalho(),
        json={
            "voice_description": descricao,
            "text": TEXTO,
            "model_id": "eleven_multilingual_ttv_v2",
            "output_format": "pcm_24000",
            "guidance_scale": 5,
        },
        timeout=120,
    )
    if r.status_code >= 400:
        sys.exit(f"erro {r.status_code}: {r.text[:400]}")
    previas = r.json()["previews"]
    for i, p in enumerate(previas, start=1):
        (PASTA / f"previa_{i}.pcm").write_bytes(base64.b64decode(p["audio_base_64"]))
    (PASTA / "previas.json").write_text(
        json.dumps(
            {
                "descricao": descricao,
                "texto": TEXTO,
                "previas": [
                    {k: v for k, v in p.items() if k != "audio_base_64"} for p in previas
                ],
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"{len(previas)} variações salvas em {PASTA}")
    return previas


def tocar() -> None:
    meta = json.loads((PASTA / "previas.json").read_text(encoding="utf-8"))
    for i, p in enumerate(meta["previas"], start=1):
        pcm = (PASTA / f"previa_{i}.pcm").read_bytes()
        print(f"\n▶ variação {i}  ({p.get('duration_secs', 0):.1f} s)")
        reproduzir_pcm(pcm, 24_000)
        time.sleep(1.2)
    print("\nPara escolher: python scripts/desenhar_voz.py --salvar N")


def salvar(n: int, nome: str) -> None:
    meta = json.loads((PASTA / "previas.json").read_text(encoding="utf-8"))
    previa = meta["previas"][n - 1]
    r = httpx.post(
        f"{API}/text-to-voice/create",
        headers=_cabecalho(),
        json={
            "voice_name": nome,
            "voice_description": meta["descricao"][:500],
            "generated_voice_id": previa["generated_voice_id"],
            "labels": {"language": "pt-BR", "use_case": "assistant", "accent": "brazilian"},
        },
        timeout=60,
    )
    if r.status_code >= 400:
        sys.exit(f"erro {r.status_code}: {r.text[:400]}")
    voice_id = r.json()["voice_id"]
    env = RAIZ / ".env"
    conteudo = env.read_text(encoding="utf-8")
    if re.search(r"(?m)^ELEVENLABS_VOICE_ID=", conteudo):
        conteudo = re.sub(r"(?m)^ELEVENLABS_VOICE_ID=.*$", f"ELEVENLABS_VOICE_ID={voice_id}", conteudo)
    else:
        conteudo += f"\nELEVENLABS_VOICE_ID={voice_id}\n"
    env.write_text(conteudo, encoding="utf-8")
    print(f"voz '{nome}' salva: {voice_id}  → gravado em .env (ELEVENLABS_VOICE_ID)")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tocar", action="store_true")
    ap.add_argument("--salvar", type=int, metavar="N")
    ap.add_argument("--nome", default="Fafa")
    ap.add_argument("--mais-rouca", action="store_true")
    ap.add_argument("--menos-rouca", action="store_true")
    ap.add_argument("--sem-audio", action="store_true", help="gera sem tocar")
    a = ap.parse_args()

    if a.salvar:
        salvar(a.salvar, a.nome)
        return
    if a.tocar:
        tocar()
        return
    descricao = MAIS_ROUCA if a.mais_rouca else MENOS_ROUCA if a.menos_rouca else DESCRICAO
    gerar(descricao)
    if not a.sem_audio:
        tocar()


if __name__ == "__main__":
    main()
