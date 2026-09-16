"""Exemplo de uso direto das ferramentas, sem o modelo (util para scripts)."""

from fafa.tools.geo import tabela_vertices

lote = [
    {"nome": "M1", "x": 596000.000, "y": 6709000.000, "confrontante": "Rua A"},
    {"nome": "M2", "x": 596100.000, "y": 6709000.000, "confrontante": "Lote 02"},
    {"nome": "M3", "x": 596100.000, "y": 6709100.000, "confrontante": "Lote 15"},
    {"nome": "M4", "x": 596000.000, "y": 6709100.000, "confrontante": "Rua B"},
]

t = tabela_vertices(lote)
print(f"{t['sistema']} · {t['quantidade_vertices']} vertices · "
      f"perimetro {t['perimetro_m']:.2f} m · area {t['area_m2']:.2f} m2 ({t['area_ha']:.4f} ha)")
print()
print(f"{'VERT':<5} {'ESTE':>12} {'NORTE':>13} {'LATITUDE':>11} {'LONGITUDE':>11} "
      f"{'PARA':<5} {'AZIMUTE':>12} {'DIST (m)':>9}  CONFRONTANTE")
for ln in t["linhas"]:
    print(f"{ln['vertice']:<5} {ln['este']:>12.3f} {ln['norte']:>13.3f} {ln['latitude']:>11.6f} "
          f"{ln['longitude']:>11.6f} {ln['para']:<5} {ln['azimute']:>12} {ln['distancia_m']:>9.2f}  "
          f"{ln['confrontante']}")
