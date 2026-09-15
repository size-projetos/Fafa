"""A implementacao interna precisa bater com o pyproj em nivel de milimetro."""

import math

import pytest

from fafa.tools import _projecao as pj

pyproj = pytest.importorskip("pyproj")

# Pontos reais na area de atuacao da SIZE (litoral norte / vale do Sinos, RS)
PONTOS = [
    (-29.7450, -50.0100),  # Capao da Canoa
    (-29.7600, -51.1470),  # Sao Leopoldo
    (-29.5190, -49.9820),  # Terra de Areia
    (-26.7400, -49.1770),  # Pomerode/SC (fuso 22, borda)
]


@pytest.mark.parametrize("lat,lon", PONTOS)
def test_geo_para_utm_bate_com_pyproj(lat, lon):
    t = pyproj.Transformer.from_crs("EPSG:4674", "EPSG:31982", always_xy=True)
    e_ref, n_ref = t.transform(lon, lat)
    e, n = pj.geo_para_utm(lat, lon, pj.Utm(22, sul=True))
    assert abs(e - e_ref) < 0.001
    assert abs(n - n_ref) < 0.001


@pytest.mark.parametrize("lat,lon", PONTOS)
def test_ida_e_volta(lat, lon):
    utm = pj.Utm(22, sul=True)
    e, n = pj.geo_para_utm(lat, lon, utm)
    lat2, lon2 = pj.utm_para_geo(e, n, utm)
    assert math.isclose(lat, lat2, abs_tol=1e-9)
    assert math.isclose(lon, lon2, abs_tol=1e-9)


def test_transformar_local_sem_pyproj(monkeypatch):
    monkeypatch.setattr(pj, "_TEM_PYPROJ", False)
    lon, lat = pj._transformar_local(596_000.0, 6_709_000.0, 31982, 4674)
    t = pyproj.Transformer.from_crs("EPSG:31982", "EPSG:4674", always_xy=True)
    lon_ref, lat_ref = t.transform(596_000.0, 6_709_000.0)
    assert abs(lon - lon_ref) < 1e-8
    assert abs(lat - lat_ref) < 1e-8


def test_epsg_para_utm():
    assert pj.epsg_para_utm(31982) == pj.Utm(22, sul=True)
    assert pj.epsg_para_utm(31981) == pj.Utm(21, sul=True)
    assert pj.epsg_para_utm(32722) == pj.Utm(22, sul=True)
    assert pj.epsg_para_utm(31976) == pj.Utm(22, sul=False)
    assert pj.epsg_para_utm(4674) is None
    assert pj.Utm(22, sul=True).meridiano_central == -51
