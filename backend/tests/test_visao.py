"""Visao: imagens viram blocos `image` para a API e marcadores de texto na memoria."""

import base64
import json
from types import SimpleNamespace

import pytest

from fafa.core.agent import Agente
from fafa.core.imagem import LADO_MAXIMO, Imagem, ResultadoVisual
from fafa.tools import visao

PIL = pytest.importorskip("PIL")
from PIL import Image  # noqa: E402


def _png(tmp_path, nome="foto.png", tamanho=(64, 48), cor=(0, 171, 120)):
    p = tmp_path / nome
    Image.new("RGB", tamanho, cor).save(p)
    return p


def test_imagem_de_pil_reduz_e_marca():
    im = Image.new("RGB", (4000, 2000), (10, 20, 30))
    img = Imagem.de_pil(im, "tela")
    assert img.media_type == "image/jpeg"
    assert img.extras["largura"] == LADO_MAXIMO and img.extras["altura"] == LADO_MAXIMO // 2
    bloco = img.bloco_api()
    assert bloco["type"] == "image" and bloco["source"]["media_type"] == "image/jpeg"
    assert base64.b64decode(bloco["source"]["data"])[:3] == b"\xff\xd8\xff"  # JPEG
    assert img.marcador().startswith("[imagem: tela, 1568x784,")


def test_ver_arquivo_imagem_pdf_texto(tmp_path):
    png = _png(tmp_path)
    r = visao.ver_arquivo(str(png))
    assert isinstance(r, Imagem) and "foto.png" in r.legenda

    csv = tmp_path / "v.csv"
    csv.write_text("nome;x;y\nM1;1;2\n", encoding="utf-8")
    r = visao.ver_arquivo(str(csv))
    assert r["conteudo"].startswith("nome;x;y") and r["cortado"] is False

    with pytest.raises(FileNotFoundError):
        visao.ver_arquivo(str(tmp_path / "nao_existe.png"))
    (tmp_path / "x.bin").write_bytes(b"\x00\x01\x02")
    with pytest.raises(ValueError):
        visao.ver_arquivo(str(tmp_path / "x.bin"))


def test_ver_pdf(tmp_path):
    fitz = pytest.importorskip("fitz")
    pdf = tmp_path / "planta.pdf"
    doc = fitz.open()
    for i in range(6):
        pg = doc.new_page()
        pg.insert_text((72, 72), f"Pagina {i + 1}")
    doc.save(pdf)
    doc.close()

    r = visao.ver_arquivo(str(pdf), paginas="2-5")
    assert isinstance(r, ResultadoVisual)
    assert len(r.imagens) == 4                      # limite de 4 por chamada
    assert r.imagens[0].legenda == "planta.pdf pagina 2/6"
    assert "mostrando 2-5" in r.texto
    with pytest.raises(ValueError):
        visao._intervalo("5-2")


def test_agente_envia_imagem_para_api_e_marcador_para_memoria(cfg, memoria, tmp_path):
    png = _png(tmp_path)
    chamadas = []

    class Cliente:
        def __init__(self):
            self.n = 0
            self.messages = SimpleNamespace(create=self.create)

        def create(self, **kw):
            self.n += 1
            chamadas.append({**kw, "messages": list(kw["messages"])})  # copia: a lista muda depois
            if self.n == 1:
                return SimpleNamespace(stop_reason="tool_use", usage=None, content=[
                    SimpleNamespace(type="tool_use", id="v1", name="ver_arquivo",
                                    input={"caminho": str(png)})])
            return SimpleNamespace(stop_reason="end_turn", usage=None,
                                   content=[SimpleNamespace(type="text", text="É um retângulo verde.")])

    a = Agente(config=cfg, memoria=memoria, cliente=Cliente())
    r = a.responder("olha essa foto", sessao_id="s", canal="cli", usuario="u")
    assert r.texto == "É um retângulo verde."

    # 2a chamada: tool_result com bloco image + texto
    conteudo = chamadas[1]["messages"][-1]["content"][0]["content"]
    assert conteudo[0]["type"] == "image" and conteudo[1]["type"] == "text"
    assert "[imagem: arquivo foto.png" in conteudo[1]["text"]

    # memoria: so o marcador, nada de base64
    hist = memoria.historico("s")
    tool_result = hist[2].conteudo[0]
    assert tool_result["type"] == "tool_result"
    assert isinstance(tool_result["content"], str) and "[imagem:" in tool_result["content"]
    assert "base64" not in json.dumps([m.conteudo for m in hist])


def test_prompt_menciona_visao(cfg, memoria):
    a = Agente(config=cfg, memoria=memoria, cliente=object())
    assert "ver_tela" in a.prompt_sistema()


def test_registro_visao():
    from fafa.core.registry import registro

    nomes = {f.nome for f in registro.listar("visao")}
    assert nomes == {"ver_tela", "ver_arquivo", "ver_camera"}
    assert registro.obter("ver_arquivo").schema["required"] == ["caminho"]
