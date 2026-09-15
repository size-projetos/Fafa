"""Memoria persistente do Fafa em SQLite.

Guarda duas coisas:
- o historico de mensagens de cada sessao (para o agente ter contexto entre
  mensagens no WhatsApp, por exemplo);
- fatos duraveis ("memorias") que o agente decide guardar sobre projetos,
  clientes e preferencias.
"""

from __future__ import annotations

import json
import sqlite3
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator

_SCHEMA = """
CREATE TABLE IF NOT EXISTS sessoes (
    id          TEXT PRIMARY KEY,
    canal       TEXT NOT NULL,
    usuario     TEXT NOT NULL,
    criada_em   TEXT NOT NULL,
    atualizada  TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS mensagens (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    sessao_id   TEXT NOT NULL REFERENCES sessoes(id) ON DELETE CASCADE,
    papel       TEXT NOT NULL,          -- 'user' | 'assistant'
    conteudo    TEXT NOT NULL,          -- JSON (blocos de conteudo da API)
    criada_em   TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_mensagens_sessao ON mensagens(sessao_id, id);

CREATE TABLE IF NOT EXISTS memorias (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    chave       TEXT NOT NULL UNIQUE,
    valor       TEXT NOT NULL,
    origem      TEXT,
    criada_em   TEXT NOT NULL,
    atualizada  TEXT NOT NULL
);
"""


def _agora() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


@dataclass(slots=True)
class Mensagem:
    papel: str
    conteudo: Any  # str ou lista de blocos de conteudo

    def para_api(self) -> dict[str, Any]:
        return {"role": self.papel, "content": self.conteudo}


class Memoria:
    """Acesso ao banco SQLite. Uma instancia por processo basta."""

    def __init__(self, caminho: Path | str) -> None:
        self.caminho = Path(caminho)
        self.caminho.parent.mkdir(parents=True, exist_ok=True)
        with self._conexao() as con:
            con.executescript(_SCHEMA)

    @contextmanager
    def _conexao(self) -> Iterator[sqlite3.Connection]:
        con = sqlite3.connect(self.caminho)
        con.row_factory = sqlite3.Row
        con.execute("PRAGMA foreign_keys = ON")
        try:
            yield con
            con.commit()
        finally:
            con.close()

    # --- Sessoes --------------------------------------------------------------

    def garantir_sessao(self, sessao_id: str, canal: str, usuario: str) -> None:
        agora = _agora()
        with self._conexao() as con:
            con.execute(
                """
                INSERT INTO sessoes (id, canal, usuario, criada_em, atualizada)
                VALUES (?, ?, ?, ?, ?)
                ON CONFLICT(id) DO UPDATE SET atualizada = excluded.atualizada
                """,
                (sessao_id, canal, usuario, agora, agora),
            )

    def limpar_sessao(self, sessao_id: str) -> None:
        with self._conexao() as con:
            con.execute("DELETE FROM mensagens WHERE sessao_id = ?", (sessao_id,))

    # --- Mensagens ------------------------------------------------------------

    def adicionar_mensagem(self, sessao_id: str, msg: Mensagem) -> None:
        with self._conexao() as con:
            con.execute(
                "INSERT INTO mensagens (sessao_id, papel, conteudo, criada_em) VALUES (?, ?, ?, ?)",
                (sessao_id, msg.papel, json.dumps(msg.conteudo, ensure_ascii=False), _agora()),
            )
            con.execute("UPDATE sessoes SET atualizada = ? WHERE id = ?", (_agora(), sessao_id))

    def historico(self, sessao_id: str, limite: int = 40) -> list[Mensagem]:
        """Ultimas `limite` mensagens da sessao, em ordem cronologica."""
        with self._conexao() as con:
            linhas = con.execute(
                """
                SELECT papel, conteudo FROM mensagens
                WHERE sessao_id = ?
                ORDER BY id DESC LIMIT ?
                """,
                (sessao_id, limite),
            ).fetchall()
        msgs = [Mensagem(linha["papel"], json.loads(linha["conteudo"])) for linha in reversed(linhas)]
        return _aparar_inicio(msgs)

    # --- Memorias duraveis ----------------------------------------------------

    def lembrar(self, chave: str, valor: str, origem: str | None = None) -> None:
        agora = _agora()
        with self._conexao() as con:
            con.execute(
                """
                INSERT INTO memorias (chave, valor, origem, criada_em, atualizada)
                VALUES (?, ?, ?, ?, ?)
                ON CONFLICT(chave) DO UPDATE SET
                    valor = excluded.valor,
                    origem = excluded.origem,
                    atualizada = excluded.atualizada
                """,
                (chave.strip().lower(), valor.strip(), origem, agora, agora),
            )

    def esquecer(self, chave: str) -> bool:
        with self._conexao() as con:
            cur = con.execute("DELETE FROM memorias WHERE chave = ?", (chave.strip().lower(),))
            return cur.rowcount > 0

    def memorias(self) -> dict[str, str]:
        with self._conexao() as con:
            linhas = con.execute("SELECT chave, valor FROM memorias ORDER BY chave").fetchall()
        return {linha["chave"]: linha["valor"] for linha in linhas}


def _aparar_inicio(msgs: list[Mensagem]) -> list[Mensagem]:
    """Garante que o historico comece em uma mensagem 'user' de texto.

    Se o corte do LIMIT cair no meio de um ciclo tool_use/tool_result, a API
    rejeita a conversa. Descarta do inicio ate encontrar um ponto seguro.
    """
    while msgs:
        primeira = msgs[0]
        if primeira.papel == "user" and not _contem_bloco(primeira.conteudo, "tool_result"):
            break
        msgs.pop(0)
    return msgs


def _contem_bloco(conteudo: Any, tipo: str) -> bool:
    if isinstance(conteudo, list):
        return any(isinstance(b, dict) and b.get("type") == tipo for b in conteudo)
    return False
