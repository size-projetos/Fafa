"""Registro de ferramentas.

Uma ferramenta e uma funcao Python comum decorada com @ferramenta. O schema
JSON enviado para a API da Anthropic e derivado automaticamente da assinatura
e das anotacoes de tipo, para nao existirem duas fontes de verdade.
"""

from __future__ import annotations

import inspect
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any, Union, get_args, get_origin, get_type_hints

# Mapeamento de tipos Python para tipos JSON Schema.
_TIPOS_JSON: dict[Any, str] = {
    str: "string",
    int: "integer",
    float: "number",
    bool: "boolean",
    list: "array",
    dict: "object",
}


@dataclass(slots=True)
class Ferramenta:
    """Uma ferramenta registrada, pronta para ser oferecida ao modelo."""

    nome: str
    descricao: str
    funcao: Callable[..., Any]
    schema: dict[str, Any]
    dominio: str = "geral"
    perigosa: bool = False

    def para_api(self) -> dict[str, Any]:
        """Formato esperado pelo parametro `tools` da API da Anthropic."""
        return {
            "name": self.nome,
            "description": self.descricao,
            "input_schema": self.schema,
        }

    def executar(self, **kwargs: Any) -> Any:
        return self.funcao(**kwargs)


@dataclass(slots=True)
class Registro:
    """Coleção de ferramentas disponiveis para o agente."""

    ferramentas: dict[str, Ferramenta] = field(default_factory=dict)

    def adicionar(self, f: Ferramenta) -> None:
        if f.nome in self.ferramentas:
            raise ValueError(f"ferramenta duplicada: {f.nome}")
        self.ferramentas[f.nome] = f

    def obter(self, nome: str) -> Ferramenta | None:
        return self.ferramentas.get(nome)

    def listar(self, dominio: str | None = None) -> list[Ferramenta]:
        itens = list(self.ferramentas.values())
        if dominio:
            itens = [f for f in itens if f.dominio == dominio]
        return sorted(itens, key=lambda f: f.nome)

    def schemas(self, dominio: str | None = None) -> list[dict[str, Any]]:
        return [f.para_api() for f in self.listar(dominio)]

    def __len__(self) -> int:
        return len(self.ferramentas)


# Registro global, populado pelo decorator na importacao dos modulos de tools.
registro = Registro()


def _tipo_json(anotacao: Any) -> dict[str, Any]:
    """Converte uma anotacao de tipo Python em um fragmento de JSON Schema."""
    if anotacao is inspect.Parameter.empty or anotacao is Any:
        return {"type": "string"}

    origem = get_origin(anotacao)

    # Optional[X] / X | None -> usa o primeiro tipo nao-nulo.
    if origem is Union:
        args = [a for a in get_args(anotacao) if a is not type(None)]
        return _tipo_json(args[0]) if args else {"type": "string"}

    if origem in (list, set, tuple):
        args = get_args(anotacao)
        itens = _tipo_json(args[0]) if args else {"type": "string"}
        return {"type": "array", "items": itens}

    if origem is dict:
        return {"type": "object"}

    return {"type": _TIPOS_JSON.get(anotacao, "string")}


def ferramenta(
    *,
    nome: str | None = None,
    dominio: str = "geral",
    descricoes: dict[str, str] | None = None,
    perigosa: bool = False,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Registra uma funcao como ferramenta do Fafa.

    A descricao da ferramenta vem da primeira linha da docstring; a descricao de
    cada parametro vem do dicionario `descricoes`. Parametros sem valor padrao
    viram obrigatorios no schema.

    Exemplo:
        @ferramenta(dominio="geo", descricoes={"epsg": "Codigo EPSG de destino"})
        def converter(epsg: int) -> str:
            '''Converte coordenadas para outro sistema.'''
    """
    descricoes = descricoes or {}

    def decorator(fn: Callable[..., Any]) -> Callable[..., Any]:
        assinatura = inspect.signature(fn)
        # Resolve anotacoes adiadas ("from __future__ import annotations").
        try:
            dicas = get_type_hints(fn)
        except Exception:  # noqa: BLE001 - tipo nao resolvivel vira string no schema
            dicas = {}
        propriedades: dict[str, Any] = {}
        obrigatorios: list[str] = []

        for nome_param, param in assinatura.parameters.items():
            if nome_param.startswith("_"):
                continue
            esquema = _tipo_json(dicas.get(nome_param, param.annotation))
            if nome_param in descricoes:
                esquema["description"] = descricoes[nome_param]
            if param.default is not inspect.Parameter.empty:
                esquema["default"] = param.default
            else:
                obrigatorios.append(nome_param)
            propriedades[nome_param] = esquema

        doc = inspect.getdoc(fn) or ""
        descricao = doc.strip() or f"Ferramenta {fn.__name__}"

        registro.adicionar(
            Ferramenta(
                nome=nome or fn.__name__,
                descricao=descricao,
                funcao=fn,
                dominio=dominio,
                perigosa=perigosa,
                schema={
                    "type": "object",
                    "properties": propriedades,
                    "required": obrigatorios,
                },
            )
        )
        return fn

    return decorator
