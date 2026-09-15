"""Imagens que uma ferramenta devolve para o modelo enxergar."""

from __future__ import annotations

import base64
import io
from dataclasses import dataclass, field
from typing import Any

LADO_MAXIMO = 1568  # limite recomendado pela API; acima disso e redimensionado de qualquer jeito


@dataclass(slots=True)
class Imagem:
    """Uma imagem JPEG/PNG pronta para virar bloco `image` da API.

    `legenda` e o que fica gravado no historico no lugar da imagem — a imagem em si
    so e enviada no turno em que foi capturada, para nao custar tokens para sempre.
    """

    dados: bytes
    media_type: str = "image/jpeg"
    legenda: str = "imagem"
    extras: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def de_pil(cls, im, legenda: str, qualidade: int = 82) -> "Imagem":
        """Converte uma imagem PIL, reduzindo para caber em LADO_MAXIMO."""
        if im.mode not in ("RGB", "L"):
            im = im.convert("RGB")
        w, h = im.size
        maior = max(w, h)
        if maior > LADO_MAXIMO:
            fator = LADO_MAXIMO / maior
            im = im.resize((max(1, int(w * fator)), max(1, int(h * fator))))
        buf = io.BytesIO()
        im.save(buf, format="JPEG", quality=qualidade, optimize=True)
        return cls(buf.getvalue(), "image/jpeg", legenda, {"largura": im.size[0], "altura": im.size[1]})

    def bloco_api(self) -> dict[str, Any]:
        return {
            "type": "image",
            "source": {
                "type": "base64",
                "media_type": self.media_type,
                "data": base64.b64encode(self.dados).decode("ascii"),
            },
        }

    def marcador(self) -> str:
        dims = ""
        if "largura" in self.extras:
            dims = f", {self.extras['largura']}x{self.extras['altura']}"
        return f"[imagem: {self.legenda}{dims}, {len(self.dados) // 1024} KB]"


@dataclass(slots=True)
class ResultadoVisual:
    """Resultado de ferramenta com uma ou mais imagens e um texto de apoio."""

    imagens: list[Imagem]
    texto: str = ""
