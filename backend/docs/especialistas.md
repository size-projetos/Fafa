# Especialistas — as skills dentro do Fafa

O Fafa carrega conhecimento **sob demanda**, no mesmo formato das skills do
Claude: uma pasta por especialista em `backend/especialistas/<nome>/` com um
`SKILL.md` (frontmatter `name` + `description`, depois as instruções) e, se
houver, `references/` e `assets/`.

O prompt de sistema lista só **nome e descrição** de cada um (≈ 1 linha).
Quando o pedido casa com a descrição, o agente chama `consultar_especialista`
e recebe as instruções completas como resultado de ferramenta — elas ficam no
histórico da sessão e valem para o resto da conversa. Assim 40 mil palavras de
instruções não entram em toda mensagem; entram só quando são úteis.

## Instalados (19)

| Grupo | Especialista | Quando o Fafa chama |
|---|---|---|
| engenharia | `auxiliar-escritorio` | topografia, memorial, vértices, DXF, loteamento, drenagem, saneamento, laudos, orçamento… (10 crib-sheets em `references/`) |
| engenharia | `site-topografia` | landing page para empresa de geotecnologia |
| governança | `due360` | menção a DUE360, decisões, ADR, governança da SIZE — **pede confirmação antes de aplicar**, conforme a própria skill |
| vídeo | `budo-seedance-base` + 15 categorias | prompts de vídeo para Seedance 2.0 (Higgsfield): cinematic, real-estate, product-ad, social-hook… O Fafa consulta a base e depois a categoria |

Ferramentas: `consultar_especialista(nome)`, `ler_referencia_especialista(nome, caminho)`,
`listar_especialistas()`.

**Gatilhos deterministas.** Modelos às vezes "esquecem" de chamar a ferramenta e
respondem de memória (aconteceu no primeiro teste: inventou a Lei Magna dos
vértices). Por isso `fafa.core.especialistas.GATILHOS` mapeia termos → especialista;
se um termo aparece em qualquer mensagem do usuário na sessão, as instruções
entram direto no prompt de sistema (`=== ESPECIALISTAS ATIVOS ===`). Custo: o
`auxiliar-escritorio` soma ≈ 2.500 tokens ao prompt enquanto o assunto for técnico.

## Catálogo de GPTs (src/agents.js)

Os 29 agentes GPT do painel (Montani / Mastplan / Engenharia) **não rodam dentro
do Fafa** — são GPTs do ChatGPT, abertos por link. O que o Fafa faz é encaminhar:
`sugerir_agente_gpt(objetivo)` lê `src/agents.js` (fonte única do catálogo,
regra do `AGENTS.md`) e devolve os mais adequados com o link e o que enviar.
No painel, os links das respostas ficam clicáveis.

Divisão de trabalho, em resumo:

- **Cálculo, topografia, documentos técnicos, governança** → o Fafa resolve, com os especialistas.
- **Render, planta humanizada, vídeo, storyboard, masterplan visual** → o Fafa indica o GPT (e, se for vídeo, já entrega o prompt pronto via `budo-seedance-*`).

## Manter atualizado

As skills originais vivem na conta Claude do Daniel. Quando uma mudar, copie a
pasta de novo para `backend/especialistas/` e rode `pytest` — o teste
`test_especialistas.py` confere que as 19 carregam. Para adicionar um
especialista novo, basta criar a pasta com um `SKILL.md`; ele entra no prompt
sozinho.
