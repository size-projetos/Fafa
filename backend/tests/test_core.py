"""Registro, memoria e loop do agente com um cliente falso da API."""

from types import SimpleNamespace

from fafa.core.agent import Agente
from fafa.core.memory import Mensagem
from fafa.core.registry import Registro, ferramenta, registro


def test_schema_derivado_da_assinatura():
    f = registro.obter("converter_coordenadas")
    assert f is not None
    s = f.schema
    assert s["required"] == ["x", "y"]
    assert s["properties"]["x"]["type"] == "number"
    assert s["properties"]["epsg_origem"]["type"] == "integer"
    assert s["properties"]["epsg_origem"]["default"] == 31982
    assert "SIRGAS" in s["properties"]["epsg_origem"]["description"]


def test_parametro_ctx_fica_fora_do_schema():
    f = registro.obter("lembrar")
    assert "_ctx" not in f.schema["properties"]
    assert f.schema["required"] == ["chave", "valor"]


def test_lista_vira_array():
    f = registro.obter("tabela_vertices")
    assert f.schema["properties"]["vertices"]["type"] == "array"
    assert f.schema["properties"]["vertices"]["items"]["type"] == "object"


def test_memoria_sessao_e_fatos(memoria):
    memoria.garantir_sessao("cli:x", "cli", "x")
    memoria.adicionar_mensagem("cli:x", Mensagem("user", "oi"))
    memoria.adicionar_mensagem("cli:x", Mensagem("assistant", [{"type": "text", "text": "ola"}]))
    h = memoria.historico("cli:x")
    assert [m.papel for m in h] == ["user", "assistant"]

    memoria.lembrar("Cliente.X", "  contato Joao ")
    assert memoria.memorias() == {"cliente.x": "contato Joao"}
    assert memoria.esquecer("cliente.x") is True
    assert memoria.esquecer("cliente.x") is False


def test_historico_nao_comeca_em_tool_result(memoria):
    memoria.garantir_sessao("s", "cli", "x")
    memoria.adicionar_mensagem("s", Mensagem("user", "a"))
    memoria.adicionar_mensagem("s", Mensagem("assistant", [{"type": "tool_use", "id": "1", "name": "n", "input": {}}]))
    memoria.adicionar_mensagem("s", Mensagem("user", [{"type": "tool_result", "tool_use_id": "1", "content": "r"}]))
    memoria.adicionar_mensagem("s", Mensagem("assistant", [{"type": "text", "text": "fim"}]))
    memoria.adicionar_mensagem("s", Mensagem("user", "b"))
    h = memoria.historico("s", limite=3)  # corta no meio do ciclo de ferramenta
    assert h[0].papel == "user" and h[0].conteudo == "b"


class ClienteFalso:
    """Simula a API: primeira chamada pede uma ferramenta, segunda responde."""

    def __init__(self):
        self.chamadas = []
        self.messages = SimpleNamespace(create=self._create)

    def _create(self, **kw):
        self.chamadas.append(kw)
        if len(self.chamadas) == 1:
            return SimpleNamespace(
                stop_reason="tool_use",
                usage=SimpleNamespace(input_tokens=10, output_tokens=5),
                content=[
                    SimpleNamespace(type="text", text="vou calcular"),
                    SimpleNamespace(
                        type="tool_use",
                        id="t1",
                        name="azimute_distancia",
                        input={"x1": 0, "y1": 0, "x2": 100, "y2": 0},
                    ),
                ],
            )
        # A segunda chamada deve conter o tool_result da primeira
        ultima = kw["messages"][-1]
        assert ultima["role"] == "user"
        assert ultima["content"][0]["type"] == "tool_result"
        assert '"azimute_gms": "90' in ultima["content"][0]["content"]
        return SimpleNamespace(
            stop_reason="end_turn",
            usage=SimpleNamespace(input_tokens=20, output_tokens=8),
            content=[SimpleNamespace(type="text", text="Azimute 90°, 100 m.")],
        )


def test_loop_do_agente_com_ferramenta(cfg, memoria):
    cliente = ClienteFalso()
    agente = Agente(config=cfg, memoria=memoria, cliente=cliente)
    progresso = []
    r = agente.responder(
        "azimute de (0,0) para (100,0)?",
        sessao_id="cli:t",
        canal="cli",
        usuario="t",
        ao_progresso=progresso.append,
    )
    assert r.texto == "vou calcular\n\nAzimute 90°, 100 m."
    assert r.ferramentas_usadas == ["azimute_distancia"]
    assert r.rodadas == 2
    assert r.tokens_entrada == 30 and r.tokens_saida == 13
    assert progresso == ["executando azimute_distancia..."]
    assert "SIRGAS 2000" in cliente.chamadas[0]["system"]
    assert any(t["name"] == "tabela_vertices" for t in cliente.chamadas[0]["tools"])
    # historico persistido: user, assistant(tool_use), user(tool_result), assistant(texto)
    assert [m.papel for m in memoria.historico("cli:t")] == ["user", "assistant", "user", "assistant"]


def test_ferramenta_com_ctx_grava_memoria(cfg, memoria):
    class Cliente:
        n = 0
        messages = None

        def __init__(self):
            self.messages = SimpleNamespace(create=self.create)

        def create(self, **kw):
            self.n += 1
            if self.n == 1:
                return SimpleNamespace(
                    stop_reason="tool_use",
                    usage=None,
                    content=[SimpleNamespace(type="tool_use", id="1", name="lembrar",
                                             input={"chave": "obra.prime", "valor": "booster em Curumim"})],
                )
            return SimpleNamespace(stop_reason="end_turn", usage=None,
                                   content=[SimpleNamespace(type="text", text="anotado")])

    agente = Agente(config=cfg, memoria=memoria, cliente=Cliente())
    r = agente.responder("lembra que...", sessao_id="s", canal="cli", usuario="u")
    assert r.texto == "anotado"
    assert memoria.memorias() == {"obra.prime": "booster em Curumim"}
    assert "obra.prime" in agente.prompt_sistema()


def test_erro_de_ferramenta_vira_tool_result_com_is_error(cfg, memoria):
    class Cliente:
        def __init__(self):
            self.n = 0
            self.messages = SimpleNamespace(create=self.create)

        def create(self, **kw):
            self.n += 1
            if self.n == 1:
                return SimpleNamespace(stop_reason="tool_use", usage=None,
                                       content=[SimpleNamespace(type="tool_use", id="1", name="tabela_vertices",
                                                                input={"vertices": []})])
            assert kw["messages"][-1]["content"][0]["is_error"] is True
            return SimpleNamespace(stop_reason="end_turn", usage=None,
                                   content=[SimpleNamespace(type="text", text="faltam vertices")])

    agente = Agente(config=cfg, memoria=memoria, cliente=Cliente())
    assert agente.responder("tabela", sessao_id="s", canal="cli", usuario="u").texto == "faltam vertices"


def test_registro_isolado_rejeita_duplicata():
    reg = Registro()

    @ferramenta(dominio="t")
    def _unica_para_teste(a: int) -> int:
        """x"""
        return a

    assert registro.obter("_unica_para_teste") is not None
    reg.adicionar(registro.obter("_unica_para_teste"))
    try:
        reg.adicionar(registro.obter("_unica_para_teste"))
        raise AssertionError("devia falhar")
    except ValueError:
        pass
