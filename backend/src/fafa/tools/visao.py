"""Os olhos do Fafa: tela, arquivos e camera.

Cada ferramenta devolve `Imagem`/`ResultadoVisual`; o agente transforma em blocos
`image` para o modelo enxergar. Dependencias (Pillow, OpenCV, PyMuPDF) sao
importadas sob demanda: `pip install -e ".[visao]"`.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from fafa.core.imagem import Imagem, ResultadoVisual
from fafa.core.registry import ferramenta

_EXT_IMAGEM = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp", ".tif", ".tiff"}
_EXT_TEXTO = {".txt", ".csv", ".md", ".json", ".xml", ".log", ".ini", ".yaml", ".yml", ".py"}
_MAX_TEXTO = 40_000


@ferramenta(
    dominio="visao",
    descricoes={
        "monitor": "Qual monitor capturar: 0 = todos juntos (padrao), 1 = primeiro, 2 = segundo...",
    },
)
def ver_tela(monitor: int = 0) -> Imagem:
    """Captura a tela do computador agora e devolve a imagem para analise (o que o usuario esta vendo)."""
    from PIL import ImageGrab

    if monitor <= 0:
        im = ImageGrab.grab(all_screens=True)
        legenda = "tela completa"
    else:
        try:
            import mss  # opcional; permite escolher o monitor

            with mss.mss() as sct:
                mon = sct.monitors[monitor]
                raw = sct.grab(mon)
                from PIL import Image

                im = Image.frombytes("RGB", raw.size, raw.bgra, "raw", "BGRX")
        except ImportError:
            im = ImageGrab.grab()
        legenda = f"monitor {monitor}"
    return Imagem.de_pil(im, legenda)


@ferramenta(
    dominio="visao",
    descricoes={
        "caminho": "Caminho do arquivo no computador (imagem, PDF ou texto)",
        "paginas": "So para PDF: paginas a mostrar, ex.: '1' ou '1-3' (maximo 4 por chamada). Padrao: '1'",
    },
)
def ver_arquivo(caminho: str, paginas: str = "1") -> Any:
    """Abre um arquivo para o Fafa ver: imagens (foto, croqui, planta), PDF (paginas renderizadas) ou texto."""
    arquivo = Path(caminho).expanduser()
    if not arquivo.exists():
        raise FileNotFoundError(f"arquivo nao encontrado: {arquivo}")
    ext = arquivo.suffix.lower()

    if ext in _EXT_IMAGEM:
        from PIL import Image

        with Image.open(arquivo) as im:
            im.load()
            return Imagem.de_pil(im, f"arquivo {arquivo.name} ({im.size[0]}x{im.size[1]} original)")

    if ext == ".pdf":
        return _ver_pdf(arquivo, paginas)

    if ext in _EXT_TEXTO or _parece_texto(arquivo):
        texto = arquivo.read_text(encoding="utf-8", errors="replace")
        cortado = len(texto) > _MAX_TEXTO
        return {
            "arquivo": str(arquivo),
            "tamanho_chars": len(texto),
            "cortado": cortado,
            "conteudo": texto[:_MAX_TEXTO],
        }

    raise ValueError(f"nao sei abrir '{ext}'. Aceito imagens, PDF e texto (CSV, TXT, MD, JSON...).")


def _ver_pdf(arquivo: Path, paginas: str) -> ResultadoVisual:
    import fitz  # PyMuPDF

    ini, fim = _intervalo(paginas)
    doc = fitz.open(arquivo)
    total = doc.page_count
    fim = min(fim, total, ini + 3)
    imagens = []
    for n in range(ini, fim + 1):
        pagina = doc[n - 1]
        pix = pagina.get_pixmap(dpi=110)
        from PIL import Image

        im = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        imagens.append(Imagem.de_pil(im, f"{arquivo.name} pagina {n}/{total}"))
    doc.close()
    return ResultadoVisual(imagens, texto=f"PDF com {total} pagina(s); mostrando {ini}-{fim}.")


@ferramenta(
    dominio="visao",
    descricoes={"indice": "Indice da camera (0 = padrao do Windows)"},
)
def ver_camera(indice: int = 0) -> Imagem:
    """Tira uma foto agora com a webcam do computador e devolve a imagem."""
    import cv2

    # Windows: Media Foundation e o padrao moderno; DirectShow e o legado; ANY deixa o OpenCV escolher.
    backends = [getattr(cv2, n) for n in ("CAP_MSMF", "CAP_DSHOW", "CAP_ANY") if hasattr(cv2, n)]
    cap = None
    for backend in backends:
        tentativa = cv2.VideoCapture(indice, backend)
        if tentativa.isOpened():
            cap = tentativa
            break
        tentativa.release()
    if cap is None:
        raise RuntimeError(
            f"camera {indice} nao encontrada ou em uso por outro programa (Meet, Teams, OBS...)"
        )
    try:
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        quadro = None
        for _ in range(8):  # descarta os primeiros quadros (exposicao/foco)
            ok, quadro = cap.read()
            if not ok:
                quadro = None
        if quadro is None:
            raise RuntimeError("a camera abriu mas nao entregou imagem")
    finally:
        cap.release()

    from PIL import Image

    im = Image.fromarray(cv2.cvtColor(quadro, cv2.COLOR_BGR2RGB))
    return Imagem.de_pil(im, f"webcam {indice}")


# --- utilitarios ---------------------------------------------------------------


def _intervalo(texto: str) -> tuple[int, int]:
    t = (texto or "1").strip()
    if "-" in t:
        a, b = t.split("-", 1)
        ini, fim = int(a), int(b)
    else:
        ini = fim = int(t)
    if ini < 1 or fim < ini:
        raise ValueError(f"intervalo de paginas invalido: {texto}")
    return ini, fim


def _parece_texto(arquivo: Path) -> bool:
    try:
        amostra = arquivo.read_bytes()[:2048]
    except OSError:
        return False
    return b"\x00" not in amostra
