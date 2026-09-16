"""Ferramentas para o agente consultar os especialistas (skills) e o catalogo de GPTs."""

from __future__ import annotations

import json
import re
import unicodedata
from functools import lru_cache
from typing import Any

from fafa.config import RAIZ
from fafa.core import especialistas as esp
from fafa.core.registry import ferramenta

CATALOGO_GPT = RAIZ.parent / "src" / "agents.js"


@ferramenta(
    dominio="especialistas",
    descricoes={"nome": "Nome do especialista, ex.: 'auxiliar-escritorio', 'due360', 'budo-seedance-base'"},
)
def consultar_especialista(nome: str) -> dict[str, Any]:
    """Carrega as instrucoes completas de um especialista (skill) para seguir neste pedido. Use quando o pedido casar com a descricao do especialista listada no prompt."""
    e = esp.obter(nome)
    if e is None:
        return {"erro": f"especialista '{nome}' nao existe", "disponiveis": sorted(esp.carregar_todos())}
    return {
        "especialista": e.nome,
        "grupo": e.grupo,
        "instrucoes": e.corpo,
        "referencias": e.referencias,
        "como_usar_referencias": "ler_referencia_especialista(nome, caminho) para textos; ver_arquivo para imagens",
    }


@ferramenta(
    dominio="especialistas",
    descricoes={
        "nome": "Nome do especialista",
        "caminho": "Caminho relativo listado em 'referencias', ex.: 'references/01-topografia/crib-sheet.md'",
    },
)
def ler_referencia_especialista(nome: str, caminho: str) -> dict[str, Any]:
    """Le um arquivo de referencia (texto) de um especialista ja consultado."""
    e = esp.obter(nome)
    if e is None:
        raise ValueError(f"especialista '{nome}' nao existe")
    return {"especialista": e.nome, "arquivo": caminho, "conteudo": e.ler_referencia(caminho)}


@ferramenta(dominio="especialistas")
def listar_especialistas() -> list[dict[str, str]]:
    """Lista os especialistas (skills) disponiveis com nome, grupo e descricao."""
    return [
        {"nome": e.nome, "grupo": e.grupo, "descricao": e.descricao_curta(300)}
        for e in esp.carregar_todos().values()
    ]


# --- catalogo de GPTs (src/agents.js) -----------------------------------------


def _normalizar(t: str) -> str:
    t = unicodedata.normalize("NFKD", t.lower())
    return "".join(c for c in t if not unicodedata.combining(c))


@lru_cache(maxsize=1)
def _agentes() -> list[dict[str, Any]]:
    if not CATALOGO_GPT.is_file():
        return []
    texto = CATALOGO_GPT.read_text(encoding="utf-8")
    ini, fim = texto.find("["), texto.rfind("]")
    if ini < 0 or fim < 0:
        return []
    return json.loads(texto[ini : fim + 1])


@ferramenta(
    dominio="especialistas",
    descricoes={
        "objetivo": "O que o usuario quer produzir, em uma frase (ex.: 'render realista de fachada a partir de print')",
        "colecao": "Opcional: Montani (criacao visual), Mastplan (urbanismo) ou Engenharia",
    },
)
def sugerir_agente_gpt(objetivo: str, colecao: str = "") -> dict[str, Any]:
    """Sugere os agentes GPT do catalogo da SIZE (29 no ChatGPT) mais adequados a um objetivo, com link para abrir. Use para pedidos de criacao visual, render, video, planta humanizada, masterplan e apresentacoes."""
    agentes = _agentes()
    if not agentes:
        return {"erro": "catalogo src/agents.js nao encontrado"}
    termos = {t for t in re.findall(r"[a-z0-9]+", _normalizar(objetivo)) if len(t) > 2}
    pontuados = []
    for a in agentes:
        if colecao and _normalizar(colecao) not in [_normalizar(c) for c in a.get("collections", [])]:
            continue
        texto = _normalizar(" ".join(str(a.get(k, "")) for k in ("name", "fullName", "description", "detail", "group", "input")))
        pontos = sum(3 if t in _normalizar(a.get("name", "")) else 1 for t in termos if t in texto)
        if pontos:
            pontuados.append((pontos, a))
    pontuados.sort(key=lambda x: -x[0])
    melhores = [
        {
            "nome": a["name"],
            "titulo": a.get("fullName", a["name"]),
            "faz": a.get("description", ""),
            "grupo": a.get("group", ""),
            "colecao": ", ".join(a.get("collections", [])),
            "o_que_enviar": a.get("input", ""),
            "url": a["url"],
        }
        for _, a in pontuados[:4]
    ]
    coordenador = next((a for a in agentes if a.get("coordinator")), None)
    return {
        "objetivo": objetivo,
        "sugestoes": melhores,
        "coordenadora_montani": {"nome": coordenador["name"], "url": coordenador["url"]} if coordenador else None,
        "observacao": "Os GPTs abrem no ChatGPT, fora do Fafa; o usuario envia os arquivos la.",
    }


@ferramenta(dominio="especialistas", descricoes={"colecao": "Montani, Mastplan, Engenharia ou vazio para todos"})
def listar_agentes_gpt(colecao: str = "") -> list[dict[str, str]]:
    """Lista os agentes GPT do catalogo da SIZE, opcionalmente por colecao."""
    saida = []
    for a in _agentes():
        if colecao and _normalizar(colecao) not in [_normalizar(c) for c in a.get("collections", [])]:
            continue
        saida.append({"nome": a["name"], "faz": a.get("description", ""), "grupo": a.get("group", ""),
                      "colecao": ", ".join(a.get("collections", [])), "url": a["url"]})
    return saida
