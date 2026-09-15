# Arquitetura do backend

Relação com o restante do repositório: o painel web em `../src` (v1) é a
camada de organização — catálogo de agentes GPT, projetos, tarefas — e roda
sozinho no navegador. Este backend é a camada de execução: um agente próprio
que calcula, lembra e conversa. Hoje são independentes; a integração
(painel chamando o backend por HTTP) está no roadmap.

## Ideia central

Um único **Agente** serve todos os canais. O canal só traduz o meio (terminal,
WhatsApp) para texto + identidade do usuário; tudo o mais — chamar o modelo,
executar ferramentas, guardar histórico — é do núcleo. Isso é o que permite
ligar o WhatsApp depois sem mexer em nada do geoprocessamento.

```
 ┌────────────┐   ┌──────────────┐
 │  CLI       │   │  WhatsApp    │      canais: recebem texto, devolvem texto
 └─────┬──────┘   └──────┬───────┘
       │ sessao_id = "canal:usuario"
       ▼                 ▼
 ┌─────────────────────────────────┐
 │            Agente               │  loop: modelo → tool_use → executa → tool_result → ...
 │  prompt de sistema + memórias   │
 └──────┬──────────────┬───────────┘
        │              │
        ▼              ▼
 ┌────────────┐  ┌────────────────┐
 │  Registro  │  │    Memória     │  SQLite: mensagens por sessão + fatos duráveis
 │ @ferramenta│  └────────────────┘
 └─────┬──────┘
       ▼
 geo · memoria · (docs · files · email — roadmap)
```

## Componentes

**`config.py`** — `pydantic-settings`. Tudo vem do `.env`; nada de segredo no código.
Expõe os padrões técnicos da SIZE (EPSG 31982 / 4674) para as ferramentas.

**`core/registry.py`** — o decorator `@ferramenta` lê a assinatura da função
(`get_type_hints`) e a docstring e produz o `input_schema` que a API espera.
Parâmetros com `_` na frente (ex.: `_ctx`) ficam fora do schema e são injetados
pelo agente. Uma única fonte de verdade: a função Python.

**`core/agent.py`** — `Agente.responder()` faz o loop clássico de uso de
ferramentas, com limite de 12 rodadas. Cada mensagem (inclusive `tool_use` e
`tool_result`) é persistida na hora, então uma queda no meio não perde contexto.
Erros de ferramenta voltam ao modelo como `tool_result` com `is_error`, para ele
corrigir ou explicar, em vez de derrubar a conversa.

**`core/memory.py`** — SQLite puro, sem ORM. `historico()` apara o início da
janela para nunca começar em um `tool_result` órfão (a API rejeita). As
"memórias" são pares chave/valor que entram no prompt de sistema de todas as
conversas — é assim que o Fafa lembra de clientes e projetos entre sessões.

**`tools/_projecao.py`** — usa `pyproj` quando disponível. Sem ele, implementa
a Transversa de Mercator pela série de Krüger (ordem 6) sobre o GRS80. Os
testes comparam com o pyproj em pontos reais do RS/SC e exigem erro < 1 mm.

**`channels/base.py`** — contrato `Canal`: `processar()` (entrada → agente →
resposta), `enviar()` (saída) e `notificar()` (aviso espontâneo). O
`sessao_id` é `"<canal>:<usuario>"`, então a mesma pessoa tem históricos
separados no terminal e no WhatsApp — de propósito: o contexto de trabalho no
desktop é longo e técnico; o do WhatsApp é curto.

## Fluxo "saí do computador"

1. Daniel pede uma tarefa longa pelo terminal.
2. A ferramenta (ou um script) termina e chama
   `fafa notificar <numero> "..."` — ou `CanalWhatsApp.notificar()`.
3. Daniel responde pelo WhatsApp; o webhook entrega ao mesmo Agente, com a
   sessão `whatsapp:<numero>`.

Restrição da Meta: mensagem livre só dentro de 24 h após a última mensagem
**dele**. Fora disso, só template aprovado (`enviar_template`). Solução
prática: cadastrar um template curto tipo *"Fafa: {{1}}"* para os avisos.

## Decisões

- **Python** — conversa com o ambiente `geo312`, GDAL, EPANET e os scripts que
  já existem na SIZE.
- **API direta em vez de framework de agentes** — o loop tem 80 linhas e não
  esconde nada; frameworks trazem abstrações que atrapalham quando o problema
  é de domínio (topografia), não de orquestração.
- **SQLite** — um arquivo, zero infraestrutura, backup é copiar `data/fafa.db`.
- **Sem Telegram/Web por enquanto** — a interface `Canal` já está pronta para
  eles; entram quando houver necessidade real.
