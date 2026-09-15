from fafa.tools import geo


def test_gms():
    assert geo.graus_para_gms(0) == "0°00'00\""
    assert geo.graus_para_gms(123.7683333) == "123°46'06\""
    assert geo.graus_para_gms(359.99999) == "0°00'00\""  # arredonda e da a volta
    assert geo.graus_para_gms(-90) == "270°00'00\""


def test_azimute_quadrantes():
    assert geo.azimute(0, 0, 0, 10) == 0
    assert geo.azimute(0, 0, 10, 0) == 90
    assert geo.azimute(0, 0, 0, -10) == 180
    assert geo.azimute(0, 0, -10, 0) == 270


def test_azimute_distancia():
    r = geo.azimute_distancia(1000, 1000, 1100, 1100)
    assert r["azimute_gms"] == "45°00'00\""
    assert r["distancia_m"] == 141.421


def test_tabela_vertices_quadrado():
    q = [
        {"nome": "M1", "x": 596000, "y": 6709000, "confrontante": "Rua A"},
        {"nome": "M2", "x": 596100, "y": 6709000},
        {"nome": "M3", "x": 596100, "y": 6709100},
        {"nome": "M4", "x": 596000, "y": 6709100},
    ]
    t = geo.tabela_vertices(q)
    assert t["quantidade_vertices"] == 4
    assert t["perimetro_m"] == 400.0
    assert t["area_m2"] == 10000.0
    assert t["area_ha"] == 1.0
    assert t["sentido"] == "anti-horario"
    l0 = t["linhas"][0]
    assert l0["vertice"] == "M1" and l0["para"] == "M2"
    assert l0["azimute"] == "90°00'00\""
    assert l0["confrontante"] == "Rua A"
    assert -30 < l0["latitude"] < -29
    assert -51 < l0["longitude"] < -49
    assert t["linhas"][-1]["para"] == "M1"


def test_tabela_aberta():
    t = geo.tabela_vertices([{"x": 0, "y": 0}, {"x": 0, "y": 100}], fechar=False)
    assert len(t["linhas"]) == 2
    assert "area_m2" not in t
    assert t["linhas"][1]["para"] == ""


def test_ler_csv(tmp_path):
    csv = tmp_path / "v.csv"
    csv.write_text(
        "Vértice;Este;Norte;Confrontante\nM1;596.000,000;6.709.000,000;Rua A\nM2;596100,5;6709000;\n",
        encoding="utf-8",
    )
    r = geo.ler_csv_coordenadas(str(csv))
    assert r["quantidade"] == 2
    assert r["vertices"][0] == {"nome": "M1", "x": 596000.0, "y": 6709000.0, "confrontante": "Rua A"}
    assert r["vertices"][1]["x"] == 596100.5
