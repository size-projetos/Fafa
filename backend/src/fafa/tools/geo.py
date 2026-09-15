"""Ferramentas de geoprocessamento e topografia.

Todas trabalham por padrao em SIRGAS 2000 / UTM 22S (EPSG:31982), o padrao da
SIZE, e devolvem dados estruturados que o agente transforma em texto, tabela
ou memorial.
"""

from __future__ import annotations

import csv
import math
from pathlib import Path
from typing import Any

from fafa.config import config
from fafa.core.registry import ferramenta
from fafa.tools._projecao import descrever_epsg, tem_pyproj, transformar

# --- Formatacao -----------------------------------------------------------------


def graus_para_gms(graus: float, casas_segundos: int = 0) -> str:
    """Graus decimais -> string em graus, minutos e segundos (ex.: 123°45'06")."""
    graus = graus % 360
    g = int(graus)
    resto = (graus - g) * 60
    m = int(resto)
    s = (resto - m) * 60
    s = round(s, casas_segundos)
    if s >= 60:
        s -= 60
        m += 1
    if m >= 60:
        m -= 60
        g += 1
    if g >= 360:
        g -= 360
    if casas_segundos == 0:
        return f"{g:d}°{m:02d}'{int(s):02d}\""
    return f"{g:d}°{m:02d}'{s:0{3 + casas_segundos}.{casas_segundos}f}\""


def azimute(x1: float, y1: float, x2: float, y2: float) -> float:
    """Azimute plano de 1 para 2, em graus decimais [0, 360), a partir do Norte."""
    return math.degrees(math.atan2(x2 - x1, y2 - y1)) % 360


def distancia(x1: float, y1: float, x2: float, y2: float) -> float:
    return math.hypot(x2 - x1, y2 - y1)


# --- Ferramentas ----------------------------------------------------------------


@ferramenta(
    dominio="geo",
    descricoes={
        "x": "Este (m) ou longitude (graus decimais), conforme o EPSG de origem",
        "y": "Norte (m) ou latitude (graus decimais), conforme o EPSG de origem",
        "epsg_origem": "EPSG de origem. Padrao: 31982 (SIRGAS 2000 / UTM 22S)",
        "epsg_destino": "EPSG de destino. Padrao: 4674 (SIRGAS 2000 geografico)",
    },
)
def converter_coordenadas(
    x: float,
    y: float,
    epsg_origem: int = config.fafa_epsg_projetado,
    epsg_destino: int = config.fafa_epsg_geografico,
) -> dict[str, Any]:
    """Converte um par de coordenadas entre sistemas (UTM <-> geografico, SIRGAS/WGS)."""
    xd, yd = transformar(x, y, epsg_origem, epsg_destino)
    geografico = epsg_destino in (4674, 4326)
    return {
        "origem": {"epsg": epsg_origem, "sistema": descrever_epsg(epsg_origem), "x": x, "y": y},
        "destino": {
            "epsg": epsg_destino,
            "sistema": descrever_epsg(epsg_destino),
            **(
                {"longitude": round(xd, 8), "latitude": round(yd, 8)}
                if geografico
                else {"este": round(xd, 3), "norte": round(yd, 3)}
            ),
        },
        "motor": "pyproj" if tem_pyproj() else "interno (Krueger)",
    }


@ferramenta(
    dominio="geo",
    descricoes={
        "x1": "Este do ponto inicial (m)",
        "y1": "Norte do ponto inicial (m)",
        "x2": "Este do ponto final (m)",
        "y2": "Norte do ponto final (m)",
    },
)
def azimute_distancia(x1: float, y1: float, x2: float, y2: float) -> dict[str, Any]:
    """Calcula azimute plano (GMS e decimal) e distancia horizontal entre dois pontos UTM."""
    az = azimute(x1, y1, x2, y2)
    return {
        "azimute_decimal": round(az, 6),
        "azimute_gms": graus_para_gms(az),
        "distancia_m": round(distancia(x1, y1, x2, y2), 3),
        "delta_x": round(x2 - x1, 3),
        "delta_y": round(y2 - y1, 3),
    }


@ferramenta(
    dominio="geo",
    descricoes={
        "vertices": (
            "Lista de vertices em ordem de caminhamento. Cada item: "
            "{'nome': 'V1', 'x': 512345.678, 'y': 6712345.678, 'confrontante': 'opcional'}"
        ),
        "epsg": "EPSG das coordenadas informadas. Padrao: 31982 (SIRGAS 2000 / UTM 22S)",
        "fechar": "Se True (padrao), inclui o segmento do ultimo vertice de volta ao primeiro",
    },
)
def tabela_vertices(
    vertices: list[dict[str, Any]],
    epsg: int = config.fafa_epsg_projetado,
    fechar: bool = True,
) -> dict[str, Any]:
    """Monta a tabela completa de vertices de um poligono: coordenadas UTM, lat/lon, azimutes, distancias, perimetro e area."""
    if len(vertices) < 2:
        raise ValueError("informe pelo menos 2 vertices")

    pontos = []
    for i, v in enumerate(vertices, start=1):
        try:
            x = float(v["x"])
            y = float(v["y"])
        except (KeyError, TypeError, ValueError) as exc:
            raise ValueError(f"vertice {i} sem x/y numericos: {v}") from exc
        pontos.append(
            {
                "nome": str(v.get("nome") or f"V{i}"),
                "x": x,
                "y": y,
                "confrontante": v.get("confrontante") or "",
            }
        )

    linhas = []
    perimetro = 0.0
    n = len(pontos)
    ultimo = n if fechar else n - 1
    for i in range(ultimo):
        p = pontos[i]
        q = pontos[(i + 1) % n]
        lon, lat = transformar(p["x"], p["y"], epsg, config.fafa_epsg_geografico)
        az = azimute(p["x"], p["y"], q["x"], q["y"])
        d = distancia(p["x"], p["y"], q["x"], q["y"])
        perimetro += d
        linhas.append(
            {
                "vertice": p["nome"],
                "este": round(p["x"], 3),
                "norte": round(p["y"], 3),
                "latitude": round(lat, 6),
                "longitude": round(lon, 6),
                "para": q["nome"],
                "azimute": graus_para_gms(az),
                "azimute_decimal": round(az, 6),
                "distancia_m": round(d, 2),
                "confrontante": p["confrontante"],
            }
        )
    if not fechar:
        p = pontos[-1]
        lon, lat = transformar(p["x"], p["y"], epsg, config.fafa_epsg_geografico)
        linhas.append(
            {
                "vertice": p["nome"],
                "este": round(p["x"], 3),
                "norte": round(p["y"], 3),
                "latitude": round(lat, 6),
                "longitude": round(lon, 6),
                "para": "",
                "azimute": "",
                "azimute_decimal": None,
                "distancia_m": None,
                "confrontante": p["confrontante"],
            }
        )

    resultado: dict[str, Any] = {
        "sistema": descrever_epsg(epsg),
        "epsg": epsg,
        "quantidade_vertices": n,
        "perimetro_m": round(perimetro, 2),
        "linhas": linhas,
    }
    if fechar and n >= 3:
        a = area_shoelace([(p["x"], p["y"]) for p in pontos])
        resultado["area_m2"] = round(a, 2)
        resultado["area_ha"] = round(a / 10_000, 4)
        resultado["sentido"] = "horario" if _sentido_horario(pontos) else "anti-horario"
    return resultado


@ferramenta(
    dominio="geo",
    descricoes={
        "caminho": "Caminho do arquivo CSV no computador",
        "epsg": "EPSG das coordenadas do arquivo. Padrao: 31982",
    },
)
def ler_csv_coordenadas(caminho: str, epsg: int = config.fafa_epsg_projetado) -> dict[str, Any]:
    """Le um CSV de coordenadas (colunas nome/x/y ou vertice/este/norte) e devolve a lista de vertices pronta para tabela_vertices."""
    arquivo = Path(caminho).expanduser()
    if not arquivo.exists():
        raise FileNotFoundError(f"arquivo nao encontrado: {arquivo}")

    texto = arquivo.read_text(encoding="utf-8-sig")
    dialeto = csv.Sniffer().sniff(texto[:2048], delimiters=";,\t")
    leitor = csv.DictReader(texto.splitlines(), dialect=dialeto)
    if not leitor.fieldnames:
        raise ValueError("CSV sem cabecalho")

    col = {c.strip().lower(): c for c in leitor.fieldnames}
    c_nome = _achar(col, ("nome", "vertice", "vértice", "ponto", "id", "marco"))
    c_x = _achar(col, ("x", "este", "e", "leste", "easting", "longitude", "lon"))
    c_y = _achar(col, ("y", "norte", "n", "northing", "latitude", "lat"))
    c_conf = _achar(col, ("confrontante", "confrontação", "confrontacao", "limite"))
    if not (c_x and c_y):
        raise ValueError(f"nao achei colunas de coordenadas. Colunas: {leitor.fieldnames}")

    vertices = []
    for i, linha in enumerate(leitor, start=1):
        x = _numero(linha[c_x])
        y = _numero(linha[c_y])
        if x is None or y is None:
            continue
        vertices.append(
            {
                "nome": (linha.get(c_nome) or f"V{i}").strip() if c_nome else f"V{i}",
                "x": x,
                "y": y,
                "confrontante": (linha.get(c_conf) or "").strip() if c_conf else "",
            }
        )
    return {"arquivo": str(arquivo), "epsg": epsg, "quantidade": len(vertices), "vertices": vertices}


# --- Geometria ------------------------------------------------------------------


def area_shoelace(pontos: list[tuple[float, float]]) -> float:
    """Area plana de um poligono fechado (formula de Gauss), sempre positiva."""
    s = 0.0
    n = len(pontos)
    for i in range(n):
        x1, y1 = pontos[i]
        x2, y2 = pontos[(i + 1) % n]
        s += x1 * y2 - x2 * y1
    return abs(s) / 2


def _sentido_horario(pontos: list[dict[str, Any]]) -> bool:
    s = 0.0
    n = len(pontos)
    for i in range(n):
        p, q = pontos[i], pontos[(i + 1) % n]
        s += (q["x"] - p["x"]) * (q["y"] + p["y"])
    return s > 0


def _achar(colunas: dict[str, str], candidatos: tuple[str, ...]) -> str | None:
    for c in candidatos:
        if c in colunas:
            return colunas[c]
    return None


def _numero(valor: str | None) -> float | None:
    if valor is None:
        return None
    v = valor.strip().replace(" ", "")
    if not v:
        return None
    # aceita 6.712.345,678 e 6712345.678
    if "," in v and "." in v:
        v = v.replace(".", "").replace(",", ".")
    elif "," in v:
        v = v.replace(",", ".")
    try:
        return float(v)
    except ValueError:
        return None
