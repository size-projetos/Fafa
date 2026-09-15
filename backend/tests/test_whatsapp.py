from fafa.channels import whatsapp as wa
from fafa.config import Config
from fafa.core.agent import Agente


class AgenteFalso(Agente):
    def __init__(self, config, memoria):
        super().__init__(config=config, memoria=memoria, cliente=object())
        self.recebidas = []

    def responder(self, texto, **kw):
        self.recebidas.append((kw["sessao_id"], texto))
        from fafa.core.agent import Resposta

        return Resposta(texto=f"eco: {texto}")


def payload(numero, texto, tipo="text"):
    return {
        "entry": [{"changes": [{"value": {"messages": [
            {"from": numero, "type": tipo, "text": {"body": texto}}
        ]}}]}]
    }


def test_webhook_responde_numero_autorizado(tmp_path, monkeypatch):
    cfg = Config(anthropic_api_key="x", fafa_db_path=str(tmp_path / "t.db"),
                 whatsapp_allowed_numbers="+55 51 98283-5944")
    from fafa.core.memory import Memoria

    agente = AgenteFalso(cfg, Memoria(cfg.caminho_banco))
    canal = wa.CanalWhatsApp(agente)
    enviados = []
    monkeypatch.setattr(wa, "enviar_texto", lambda para, texto, cfg=None: enviados.append((para, texto)))

    assert canal.tratar_evento(payload("5551982835944", "oi fafa")) == 1
    assert agente.recebidas == [("whatsapp:5551982835944", "oi fafa")]
    assert enviados == [("5551982835944", "eco: oi fafa")]

    # numero desconhecido e ignorado
    assert canal.tratar_evento(payload("5599999999999", "invasor")) == 0
    # midia sem texto e ignorada
    assert canal.tratar_evento(payload("5551982835944", "", tipo="image")) == 0
    assert len(enviados) == 1


def test_verificacao_do_webhook(tmp_path):
    from fastapi.testclient import TestClient
    from fafa.core.memory import Memoria

    cfg = Config(anthropic_api_key="x", fafa_db_path=str(tmp_path / "t.db"), whatsapp_verify_token="segredo")
    app = wa.criar_app(AgenteFalso(cfg, Memoria(cfg.caminho_banco)))
    c = TestClient(app)
    r = c.get("/webhook", params={"hub.mode": "subscribe", "hub.verify_token": "segredo", "hub.challenge": "123"})
    assert r.status_code == 200 and r.text == "123"
    assert c.get("/webhook", params={"hub.mode": "subscribe", "hub.verify_token": "errado"}).status_code == 403
    assert c.get("/saude").json()["status"] == "ok"
