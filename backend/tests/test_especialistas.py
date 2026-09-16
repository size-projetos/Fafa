"""Especialistas (skills) e catalogo de GPTs."""

from fafa.core import especialistas as esp
from fafa.core.agent import Agente
from fafa.core.memory import Memoria
from fafa.tools import especialistas as tools


def test_carrega_skills_reais():
    todos = esp.carregar_todos()
    assert {"auxiliar-escritorio", "due360", "budo-seedance-base", "site-topografia"} <= set(todos)
    assert sum(n.startswith("budo-seedance") for n in todos) == 16
    aux = todos["auxiliar-escritorio"]
    assert aux.grupo == "engenharia"
    assert "Lei Magna dos vértices" in aux.corpo
    assert "name:" not in aux.corpo[:200]          # frontmatter removido
    assert "references/01-topografia/crib-sheet.md" in aux.referencias


def test_descricao_curta_e_catalogo():
    e = esp.obter("auxiliar-escritorio")
    assert len(e.descricao_curta()) <= 220
    cat = esp.catalogo_para_prompt()
    assert "- auxiliar-escritorio:" in cat and "- due360:" in cat
    assert "budo-seedance-*" in cat and "budo-seedance-cinematic" not in cat  # agrupado


def test_ler_referencia_segura():
    e = esp.obter("auxiliar-escritorio")
    texto = e.ler_referencia("references/01-topografia/crib-sheet.md")
    assert len(texto) > 100
    import pytest

    with pytest.raises(ValueError):
        e.ler_referencia("../../src/agents.js")
    with pytest.raises(FileNotFoundError):
        e.ler_referencia("references/nao-existe.md")


def test_ferramentas_especialista():
    r = tools.consultar_especialista("due360")
    assert r["especialista"] == "due360" and "Confirmacao de Ativacao" in r["instrucoes"]
    assert "references/framework.md" in r["referencias"]
    r = tools.consultar_especialista("nao-existe")
    assert "erro" in r and "auxiliar-escritorio" in r["disponiveis"]
    assert any(x["nome"] == "budo-seedance-base" for x in tools.listar_especialistas())


def test_catalogo_gpt():
    todos = tools.listar_agentes_gpt()
    assert len(todos) == 29
    assert len(tools.listar_agentes_gpt("Mastplan")) == 5
    r = tools.sugerir_agente_gpt("render realista de fachada a partir de um print")
    nomes = [s["nome"] for s in r["sugestoes"]]
    assert nomes[0] == "Cavaleiro Negro"           # print to render exteriores
    assert all(s["url"].startswith("https://chatgpt.com/") for s in r["sugestoes"])
    assert r["coordenadora_montani"]["nome"] == "NOVA"
    r = tools.sugerir_agente_gpt("planta humanizada", colecao="Montani")
    assert r["sugestoes"][0]["nome"] == "VISÃO"


def test_prompt_lista_especialistas_e_gpts(cfg, memoria):
    a = Agente(config=cfg, memoria=Memoria(cfg.caminho_banco), cliente=object())
    p = a.prompt_sistema()
    assert "consultar_especialista" in p and "auxiliar-escritorio" in p
    assert "sugerir_agente_gpt" in p and "29 GPTs" in p


def test_rotear_por_gatilho():
    nomes = lambda ts: [e.nome for e in esp.rotear(ts)]  # noqa: E731
    assert nomes(["qual é a Lei Magna dos vértices?"]) == ["auxiliar-escritorio"]
    assert nomes(["me ajuda com a governança DUE360 desse projeto"]) == ["auxiliar-escritorio", "due360"] or \
           "due360" in nomes(["me ajuda com a governança DUE360 desse projeto"])
    assert nomes(["quero um prompt de vídeo para o Higgsfield"]) == ["budo-seedance-base"]
    assert nomes(["oi, tudo bem?"]) == []
    assert nomes(["oi", "monta a tabela de coordenadas do loteamento"]) == ["auxiliar-escritorio"]  # gatilho em mensagem anterior


def test_agente_injeta_especialista_no_prompt(cfg, memoria):
    from types import SimpleNamespace

    vistos = []

    class Cliente:
        def __init__(self):
            self.messages = SimpleNamespace(create=self.create)

        def create(self, **kw):
            vistos.append(kw["system"])
            return SimpleNamespace(stop_reason="end_turn", usage=None,
                                   content=[SimpleNamespace(type="text", text="ok")])

    a = Agente(config=cfg, memoria=memoria, cliente=Cliente())
    a.responder("oi", sessao_id="s", canal="cli", usuario="u")
    assert "ESPECIALISTAS ATIVOS" not in vistos[-1]
    a.responder("qual a Lei Magna dos vértices?", sessao_id="s", canal="cli", usuario="u")
    assert "ESPECIALISTAS ATIVOS" in vistos[-1] and "Lei Magna dos vértices" in vistos[-1]
    a.responder("e o perímetro?", sessao_id="s", canal="cli", usuario="u")   # continua ativo pelo historico
    assert "--- auxiliar-escritorio ---" in vistos[-1]
