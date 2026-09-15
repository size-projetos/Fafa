# Fafa · backend

O núcleo de inteligência do Fafa: um agente sobre a API da Anthropic com
ferramentas de topografia e geoprocessamento, acessível pelo terminal do desktop
SIZE-LIDAR e pelo WhatsApp. É a camada que o [painel web](../src) da v1 ainda
não tinha — o "backend" pedido no roadmap original.

**Fase atual:** geoprocessamento + terminal. WhatsApp em preparação.
Veja o [roadmap](docs/roadmap.md).

## O que já faz

| Ferramenta | O que entrega |
|---|---|
| `converter_coordenadas` | UTM ↔ geográfico, SIRGAS 2000 / WGS 84, qualquer fuso |
| `azimute_distancia` | Azimute (GMS e decimal) e distância entre dois pontos |
| `tabela_vertices` | Tabela completa do polígono: E/N, lat/lon, azimutes, distâncias, confrontantes, perímetro, área, sentido |
| `ler_csv_coordenadas` | Lê CSV de vértices (`;` ou `,`, números no formato brasileiro) |
| `lembrar` / `esquecer` / `listar_memorias` | Memória de longo prazo entre conversas |

Padrão de trabalho: **SIRGAS 2000 / UTM 22S (EPSG:31982)**, geográfico EPSG:4674,
vértices em sequência crescente, tabelas com LATITUDE, LONGITUDE e CONFRONTANTE.

## Instalação (Windows, desktop SIZE-LIDAR)

```powershell
git clone https://github.com/size-projetos/Fafa.git
cd Fafa\backend
python -m venv .venv
.venv\Scripts\activate
pip install -e ".[all,dev]"
copy .env.example .env
notepad .env          # preencher ANTHROPIC_API_KEY (o .env fica só nesta máquina)
```

Sem `pyproj` o Fafa ainda converte coordenadas SIRGAS 2000 / WGS 84 com um motor
interno (precisão milimétrica). Para outros datums (SAD69, Córrego Alegre),
instale `pyproj`, que já vem no extra `[all]`.

## Uso

```powershell
fafa                     # conversa no terminal
fafa tools               # lista as ferramentas e seus parâmetros
fafa whatsapp            # sobe o webhook do WhatsApp (ver docs/whatsapp.md)
fafa notificar 5551982835944 "Terminei a tabela do Parque Germânico."
```

No terminal: `/tools`, `/memorias`, `/limpar`, `/sair`.

Exemplo de conversa:

> **você:** monta a tabela do lote com M1 596000/6709000, M2 596100/6709000,
> M3 596100/6709100, M4 596000/6709100. M1 confronta com a Rua A.
>
> **Fafa:** *(executa `tabela_vertices`)* Tabela em SIRGAS 2000 / UTM 22S,
> 4 vértices, perímetro 400,00 m, área 10.000,00 m² (1,0000 ha), sentido
> anti-horário. M1 → M2: az 90°00'00", 100,00 m, confrontante Rua A ...

## Estrutura

```
src/fafa/
  config.py          configurações (.env)
  core/
    agent.py         loop modelo ↔ ferramentas ↔ memória
    registry.py      @ferramenta: schema JSON gerado da assinatura Python
    memory.py        SQLite: histórico por sessão + fatos duráveis
  tools/
    geo.py           ferramentas de topografia
    _projecao.py     transformação de coordenadas (pyproj ou motor interno)
    memoria.py       lembrar / esquecer
  channels/
    base.py          contrato Canal (processar, enviar, notificar)
    cli.py           terminal
    whatsapp.py      Meta Cloud API: envio, template e webhook
  __main__.py        comando `fafa`
tests/               27 testes; a projeção interna é validada contra o pyproj
docs/                arquitetura, roadmap, configuração do WhatsApp
```

## Desenvolvimento

```powershell
pytest              # testes
ruff check src tests
```

Para adicionar uma ferramenta, escreva uma função com anotações de tipo e
docstring e decore com `@ferramenta`. O schema para a API é gerado sozinho:

```python
from fafa.core.registry import ferramenta

@ferramenta(dominio="geo", descricoes={"cota": "Cota em metros"})
def exemplo(cota: float, referencia: str = "IBGE") -> dict:
    """Uma linha explicando o que a ferramenta faz (o modelo lê isto)."""
    ...
```
