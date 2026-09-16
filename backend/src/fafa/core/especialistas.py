"""Especialistas: conhecimento sob demanda, no formato de skills (SKILL.md + referencias).

A pasta backend/especialistas/<nome>/ tem um SKILL.md com frontmatter YAML
(name, description) e o corpo com as instrucoes. O prompt de sistema lista so
nome e descricao; o corpo entra na conversa quando o agente chama a ferramenta
`consultar_especialista` — igual ao mecanismo de skills do Claude, para nao
inflar cada mensagem com 40 mil palavras de instrucoes.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

from fafa.config import RAIZ

PASTA = RAIZ / "especialistas"
_FRONT = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
MAX_CHARS_CORPO = 60_000
MAX_CHARS_REFERENCIA = 40_000
_EXT_TEXTO = {".md", ".txt", ".csv", ".json", ".yaml", ".yml", ".html"}


@dataclass(slots=True)
class Especialista:
    nome: str
    descricao: str
    pasta: Path
    grupo: str = "geral"
    referencias: list[str] = field(default_factory=list)

    @property
    def corpo(self) -> str:
        texto = (self.pasta / "SKILL.md").read_text(encoding="utf-8")
        m = _FRONT.match(texto)
        corpo = texto[m.end():] if m else texto
        if len(corpo) > MAX_CHARS_CORPO:
            corpo = corpo[:MAX_CHARS_CORPO] + "\n\n[... instrucoes cortadas por tamanho ...]"
        return corpo.strip()

    def descricao_curta(self, limite: int = 220) -> str:
        d = " ".join(self.descricao.split())
        return d if len(d) <= limite else d[: limite - 1].rsplit(" ", 1)[0] + "…"

    def ler_referencia(self, caminho: str) -> str:
        alvo = (self.pasta / caminho).resolve()
        if self.pasta.resolve() not in alvo.parents:
            raise ValueError("caminho fora da pasta do especialista")
        if not alvo.is_file():
            raise FileNotFoundError(f"referencia nao encontrada: {caminho}")
        if alvo.suffix.lower() not in _EXT_TEXTO:
            raise ValueError(
                f"'{caminho}' nao e texto; para imagens use ver_arquivo com o caminho {alvo}"
            )
        texto = alvo.read_text(encoding="utf-8", errors="replace")
        if len(texto) > MAX_CHARS_REFERENCIA:
            texto = texto[:MAX_CHARS_REFERENCIA] + "\n\n[... cortado por tamanho ...]"
        return texto


def _frontmatter(texto: str) -> dict[str, str]:
    m = _FRONT.match(texto)
    if not m:
        return {}
    dados: dict[str, str] = {}
    for linha in m.group(1).splitlines():
        if ":" not in linha:
            continue
        chave, _, valor = linha.partition(":")
        valor = valor.strip()
        if len(valor) >= 2 and valor[0] == valor[-1] and valor[0] in "\"'":
            valor = valor[1:-1]
        dados[chave.strip()] = valor
    return dados


def _grupo(nome: str) -> str:
    if nome.startswith("budo-seedance"):
        return "video"
    if nome in ("auxiliar-escritorio", "site-topografia"):
        return "engenharia"
    if nome == "due360":
        return "governanca"
    return "geral"


@lru_cache(maxsize=1)
def carregar_todos(pasta: Path | None = None) -> dict[str, Especialista]:
    pasta = pasta or PASTA
    itens: dict[str, Especialista] = {}
    if not pasta.is_dir():
        return itens
    for skill in sorted(pasta.glob("*/SKILL.md")):
        try:
            fm = _frontmatter(skill.read_text(encoding="utf-8"))
        except OSError:
            continue
        nome = fm.get("name") or skill.parent.name
        refs = sorted(
            str(p.relative_to(skill.parent)).replace("\\", "/")
            for p in skill.parent.rglob("*")
            if p.is_file() and p.name != "SKILL.md"
        )
        itens[nome] = Especialista(
            nome=nome,
            descricao=fm.get("description", ""),
            pasta=skill.parent,
            grupo=_grupo(nome),
            referencias=refs,
        )
    return itens


def obter(nome: str) -> Especialista | None:
    return carregar_todos().get(nome.strip().lower())


def catalogo_para_prompt() -> str:
    """Lista compacta para o prompt de sistema: os budo agrupados numa linha so."""
    todos = carregar_todos()
    if not todos:
        return ""
    linhas = []
    budo = [n for n in todos if n.startswith("budo-seedance")]
    for nome, e in todos.items():
        if nome in budo:
            continue
        linhas.append(f"- {nome}: {e.descricao_curta()}")
    if budo:
        categorias = ", ".join(n.replace("budo-seedance-", "") for n in budo if n != "budo-seedance-base")
        linhas.append(
            "- budo-seedance-*: prompts de video para Seedance 2.0 (Higgsfield). Consulte primeiro "
            f"budo-seedance-base e depois a categoria: {categorias}."
        )
    return "\n".join(linhas)
