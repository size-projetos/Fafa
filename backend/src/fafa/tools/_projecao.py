"""Transformacao de coordenadas.

Usa pyproj quando instalado (qualquer EPSG). Sem pyproj, cai em uma
implementacao propria de Transversa de Mercator (serie de Krueger, precisao
milimetrica dentro do fuso) que cobre os casos do dia a dia da SIZE:
SIRGAS 2000 e WGS 84, geografico e UTM.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

try:  # pragma: no cover - depende do ambiente
    from pyproj import Transformer

    _TEM_PYPROJ = True
except ImportError:  # pragma: no cover
    _TEM_PYPROJ = False


@dataclass(frozen=True, slots=True)
class Utm:
    fuso: int
    sul: bool

    @property
    def meridiano_central(self) -> float:
        return (self.fuso - 1) * 6 - 180 + 3

    @property
    def falso_norte(self) -> float:
        return 10_000_000.0 if self.sul else 0.0


# Elipsoide GRS80 (SIRGAS 2000). WGS84 difere no achatamento em ~1e-10: irrelevante.
_A = 6_378_137.0
_F = 1 / 298.257_222_101
_K0 = 0.9996
_FALSO_ESTE = 500_000.0

_GEOGRAFICOS = {4674, 4326, 4989, 4979}


def epsg_para_utm(epsg: int) -> Utm | None:
    """Decodifica um EPSG de UTM em (fuso, hemisferio). None se nao for UTM conhecido."""
    if 31965 <= epsg <= 31976:  # SIRGAS 2000 / UTM 11N..22N
        return Utm(epsg - 31954, sul=False)
    if 31977 <= epsg <= 31985:  # SIRGAS 2000 / UTM 17S..25S
        return Utm(epsg - 31960, sul=True)
    if 32601 <= epsg <= 32660:  # WGS 84 / UTM N
        return Utm(epsg - 32600, sul=False)
    if 32701 <= epsg <= 32760:  # WGS 84 / UTM S
        return Utm(epsg - 32700, sul=True)
    return None


def descrever_epsg(epsg: int) -> str:
    if epsg == 4674:
        return "SIRGAS 2000 (geografico)"
    if epsg == 4326:
        return "WGS 84 (geografico)"
    utm = epsg_para_utm(epsg)
    if utm:
        datum = "SIRGAS 2000" if 31965 <= epsg <= 31985 else "WGS 84"
        return f"{datum} / UTM {utm.fuso}{'S' if utm.sul else 'N'}"
    return f"EPSG:{epsg}"


def transformar(x: float, y: float, epsg_origem: int, epsg_destino: int) -> tuple[float, float]:
    """Transforma (x, y) de um EPSG para outro.

    Para sistemas geograficos, x = longitude e y = latitude (graus decimais).
    Para UTM, x = Este e y = Norte (metros).
    """
    if epsg_origem == epsg_destino:
        return x, y
    if _TEM_PYPROJ:
        t = Transformer.from_crs(f"EPSG:{epsg_origem}", f"EPSG:{epsg_destino}", always_xy=True)
        return t.transform(x, y)
    return _transformar_local(x, y, epsg_origem, epsg_destino)


def _transformar_local(x: float, y: float, origem: int, destino: int) -> tuple[float, float]:
    # Passo 1: origem -> geografico
    if origem in _GEOGRAFICOS:
        lon, lat = x, y
    else:
        utm = epsg_para_utm(origem)
        if utm is None:
            raise ValueError(
                f"EPSG:{origem} nao suportado sem pyproj. Instale com: pip install pyproj"
            )
        lat, lon = utm_para_geo(x, y, utm)

    # Passo 2: geografico -> destino
    if destino in _GEOGRAFICOS:
        return lon, lat
    utm = epsg_para_utm(destino)
    if utm is None:
        raise ValueError(f"EPSG:{destino} nao suportado sem pyproj. Instale com: pip install pyproj")
    return geo_para_utm(lat, lon, utm)


# --- Transversa de Mercator (serie de Krueger, ordem 6) -------------------------

_N = _F / (2 - _F)
_N2, _N3, _N4, _N5, _N6 = _N**2, _N**3, _N**4, _N**5, _N**6
_AA = _A / (1 + _N) * (1 + _N2 / 4 + _N4 / 64 + _N6 / 256)

_ALFA = (
    _N / 2 - 2 * _N2 / 3 + 5 * _N3 / 16 + 41 * _N4 / 180 - 127 * _N5 / 288 + 7891 * _N6 / 37800,
    13 * _N2 / 48 - 3 * _N3 / 5 + 557 * _N4 / 1440 + 281 * _N5 / 630 - 1983433 * _N6 / 1935360,
    61 * _N3 / 240 - 103 * _N4 / 140 + 15061 * _N5 / 26880 + 167603 * _N6 / 181440,
    49561 * _N4 / 161280 - 179 * _N5 / 168 + 6601661 * _N6 / 7257600,
    34729 * _N5 / 80640 - 3418889 * _N6 / 1995840,
    212378941 * _N6 / 319334400,
)
_BETA = (
    _N / 2 - 2 * _N2 / 3 + 37 * _N3 / 96 - _N4 / 360 - 81 * _N5 / 512 + 96199 * _N6 / 604800,
    _N2 / 48 + _N3 / 15 - 437 * _N4 / 1440 + 46 * _N5 / 105 - 1118711 * _N6 / 3870720,
    17 * _N3 / 480 - 37 * _N4 / 840 - 209 * _N5 / 4480 + 5569 * _N6 / 90720,
    4397 * _N4 / 161280 - 11 * _N5 / 504 - 830251 * _N6 / 7257600,
    4583 * _N5 / 161280 - 108847 * _N6 / 3991680,
    20648693 * _N6 / 638668800,
)
_DELTA = (
    2 * _N - 2 * _N2 / 3 - 2 * _N3 + 116 * _N4 / 45 + 26 * _N5 / 45 - 2854 * _N6 / 675,
    7 * _N2 / 3 - 8 * _N3 / 5 - 227 * _N4 / 45 + 2704 * _N5 / 315 + 2323 * _N6 / 945,
    56 * _N3 / 15 - 136 * _N4 / 35 - 1262 * _N5 / 105 + 73814 * _N6 / 2835,
    4279 * _N4 / 630 - 332 * _N5 / 35 - 399572 * _N6 / 14175,
    4174 * _N5 / 315 - 144838 * _N6 / 6237,
    601676 * _N6 / 22275,
)


def geo_para_utm(lat: float, lon: float, utm: Utm) -> tuple[float, float]:
    """Latitude/longitude (graus) -> Este/Norte (m) no fuso indicado."""
    phi = math.radians(lat)
    lam = math.radians(lon - utm.meridiano_central)

    t = math.sinh(math.atanh(math.sin(phi)) - 2 * math.sqrt(_N) / (1 + _N) * math.atanh(
        2 * math.sqrt(_N) / (1 + _N) * math.sin(phi)
    ))
    xi_ = math.atan2(t, math.cos(lam))
    eta_ = math.atanh(math.sin(lam) / math.sqrt(1 + t * t))

    xi = xi_
    eta = eta_
    for j, a in enumerate(_ALFA, start=1):
        xi += a * math.sin(2 * j * xi_) * math.cosh(2 * j * eta_)
        eta += a * math.cos(2 * j * xi_) * math.sinh(2 * j * eta_)

    este = _FALSO_ESTE + _K0 * _AA * eta
    norte = utm.falso_norte + _K0 * _AA * xi
    return este, norte


def utm_para_geo(este: float, norte: float, utm: Utm) -> tuple[float, float]:
    """Este/Norte (m) -> latitude/longitude (graus)."""
    xi = (norte - utm.falso_norte) / (_K0 * _AA)
    eta = (este - _FALSO_ESTE) / (_K0 * _AA)

    xi_ = xi
    eta_ = eta
    for j, b in enumerate(_BETA, start=1):
        xi_ -= b * math.sin(2 * j * xi) * math.cosh(2 * j * eta)
        eta_ -= b * math.cos(2 * j * xi) * math.sinh(2 * j * eta)

    chi = math.asin(math.sin(xi_) / math.cosh(eta_))
    phi = chi
    for j, d in enumerate(_DELTA, start=1):
        phi += d * math.sin(2 * j * chi)

    lam = math.atan2(math.sinh(eta_), math.cos(xi_))
    return math.degrees(phi), utm.meridiano_central + math.degrees(lam)


def tem_pyproj() -> bool:
    return _TEM_PYPROJ
