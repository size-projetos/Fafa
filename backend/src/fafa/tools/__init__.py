"""Ferramentas que o Fafa pode chamar, agrupadas por dominio.

Importar este pacote registra todas as ferramentas no registro global.
Fase 1: geoprocessamento + memoria. Os demais dominios entram conforme o roadmap.
"""

from fafa.tools import geo, memoria  # noqa: F401  (registra as ferramentas)

__all__ = ["geo", "memoria"]
