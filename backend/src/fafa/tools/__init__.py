"""Ferramentas que o Fafa pode chamar, agrupadas por dominio.

Importar este pacote registra todas as ferramentas no registro global.
Fase 1: geoprocessamento + memoria + visao. Os demais dominios entram conforme o roadmap.
"""

from fafa.tools import especialistas, geo, memoria, visao  # noqa: F401  (registra as ferramentas)

__all__ = ["especialistas", "geo", "memoria", "visao"]
