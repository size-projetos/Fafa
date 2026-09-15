"""Escolher a voz do Fafa no catalogo publico da ElevenLabs (funciona no plano gratis).

Uso:
  python scripts/catalogo_vozes.py                    # lista vozes masculinas em portugues, baixa as previas
  python scripts/catalogo_vozes.py --genero female    # femininas
  python scripts/catalogo_vozes.py --tocar 1 2 3      # toca as previas dos numeros indicados
  python scripts/catalogo_vozes.py --adicionar 2      # adiciona a voz 2 a "My Voices" como "Fafa" e grava o ID no .env
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

import httpx
from dotenv import load_dotenv

RAIZ = Path(__file__).resolve().parents[1]
load_dotenv(RAIZ / ".env")
from fafa.config import config  # noqa: E402

API = "https://api.elevenlabs.io/v1"
PASTA = RAIZ / "data" / "vozes" / "catalogo"
LISTA = PASTA / "lista.json"


def _h() -> dict[str, str]:
    if not config.elevenlabs_api_key:
        sys.exit("ELEVENLABS_API_KEY nao configurada no .env")
    return {"xi-api-key": config.elevenlabs_api_key}


def listar(genero: str, idade: str | None, quantidade: int) -> list[dict]:
    PASTA.mkdir(parents=True, exist_ok=True)
    params = {"language": "pt", "gender": genero, "page_size": 100, "sort": "cloned_by_count"}
    if idade:
        params["age"] = idade
    r = httpx.get(f"{API}/shared-voices", headers=_h(), params=params, timeout=60)
    if r.status_code >= 400:
        sys.exit(f"erro {r.status_code}: {r.text[:300]}")
    vozes = r.json().get("voices", [])
    # prioriza sotaque brasileiro e uso conversacional/informativo
    def nota(v):
        acc = (v.get("accent") or "").lower()
        uso = (v.get("use_case") or "").lower()
        n = v.get("cloned_by_count") or 0
        bonus = 0
        if "brazil" in acc or "brasil" in acc:
            bonus += 1_000_000
        if any(k in uso for k in ("conversational", "informative", "narrative", "educational")):
            bonus += 100_000
        return -(bonus + n)
    vozes.sort(key=nota)
    vozes = vozes[:quantidade]
    LISTA.write_text(json.dumps(vozes, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{'#':>2}  {'nome':<22} {'sotaque':<16} {'idade':<12} {'estilo':<14} {'uso':<16} {'usos':>6}")
    for i, v in enumerate(vozes, start=1):
        print(f"{i:>2}  {v['name'][:22]:<22} {str(v.get('accent',''))[:16]:<16} "
              f"{str(v.get('age',''))[:12]:<12} {str(v.get('descriptive',''))[:14]:<14} "
              f"{str(v.get('use_case',''))[:16]:<16} {v.get('cloned_by_count') or 0:>6}")
        if v.get("description"):
            print(f"     {v['description'][:110]}")
    print(f"\nprévias em {PASTA}. Para ouvir: --tocar 1 2 3   Para escolher: --adicionar N")
    return vozes


def _baixar(i: int, v: dict) -> Path:
    destino = PASTA / f"{i:02d}_{re.sub(r'[^A-Za-z0-9]+', '_', v['name'])[:30]}.mp3"
    if not destino.exists():
        r = httpx.get(v["preview_url"], timeout=60, follow_redirects=True)
        r.raise_for_status()
        destino.write_bytes(r.content)
    return destino


def tocar(numeros: list[int]) -> None:
    vozes = json.loads(LISTA.read_text(encoding="utf-8"))
    for n in numeros:
        v = vozes[n - 1]
        arq = _baixar(n, v)
        print(f"▶ {n}: {v['name']} — {v.get('accent','')} / {v.get('descriptive','')}")
        ps = (
            "Add-Type -AssemblyName PresentationCore; "
            "$p = New-Object System.Windows.Media.MediaPlayer; "
            f"$p.Open([uri]'{arq}'); Start-Sleep -Milliseconds 400; $p.Play(); "
            "while (-not $p.NaturalDuration.HasTimeSpan) { Start-Sleep -Milliseconds 100 }; "
            "Start-Sleep -Seconds ([math]::Ceiling($p.NaturalDuration.TimeSpan.TotalSeconds) + 1); $p.Close()"
        )
        subprocess.run(["powershell", "-NoProfile", "-Command", ps], check=False)


def adicionar(n: int, nome: str) -> None:
    vozes = json.loads(LISTA.read_text(encoding="utf-8"))
    v = vozes[n - 1]
    r = httpx.post(
        f"{API}/voices/add/{v['public_owner_id']}/{v['voice_id']}",
        headers=_h(),
        json={"new_name": nome},
        timeout=60,
    )
    if r.status_code >= 400:
        sys.exit(f"erro {r.status_code}: {r.text[:300]}")
    voice_id = r.json()["voice_id"]
    env = RAIZ / ".env"
    c = env.read_text(encoding="utf-8")
    if re.search(r"(?m)^ELEVENLABS_VOICE_ID=", c):
        c = re.sub(r"(?m)^ELEVENLABS_VOICE_ID=.*$", f"ELEVENLABS_VOICE_ID={voice_id}", c)
    else:
        c += f"\nELEVENLABS_VOICE_ID={voice_id}\n"
    env.write_text(c, encoding="utf-8")
    print(f"voz '{v['name']}' adicionada como '{nome}': {voice_id} → gravado no .env")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--genero", default="male", choices=["male", "female", "neutral"])
    ap.add_argument("--idade", default=None, choices=[None, "young", "middle_aged", "old"])
    ap.add_argument("--quantidade", type=int, default=12)
    ap.add_argument("--tocar", type=int, nargs="+", metavar="N")
    ap.add_argument("--adicionar", type=int, metavar="N")
    ap.add_argument("--nome", default="Fafa")
    a = ap.parse_args()
    if a.adicionar:
        adicionar(a.adicionar, a.nome)
    elif a.tocar:
        tocar(a.tocar)
    else:
        listar(a.genero, a.idade, a.quantidade)


if __name__ == "__main__":
    main()
