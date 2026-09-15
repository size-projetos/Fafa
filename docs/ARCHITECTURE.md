# Arquitetura

## Aplicação atual

O Fafa é uma aplicação web estática, sem etapa de compilação e sem dependências externas obrigatórias.

- A interface é construída em HTML e CSS.
- `agents.js` contém o catálogo, categorias, especialidades e links dos agentes.
- `app.js` controla navegação, busca, filtros e recomendação.
- `operations.js` controla projetos, tarefas, riscos, decisões, lembretes e relatórios.
- O navegador mantém o estado por meio de `localStorage`.

## Categorias

- **Montani:** agentes com nomes de heróis e a coordenadora NOVA.
- **Mastplan:** planejamento urbano, masterplans e visualização territorial.
- **Engenharia:** saneamento, hidráulica, infraestrutura e documentos técnicos.

## Limites da versão 1

- Os GPTs externos abrem por link e não são executados dentro do painel.
- Os dados não sincronizam entre dispositivos.
- Não existe banco de dados central nem autenticação corporativa própria.
- O registro de arquivos armazena metadados, não o conteúdo dos arquivos.
- A busca em Google Drive e outras nuvens permanece desativada.

## Segurança

Nenhuma credencial deve entrar no código-fonte. Integrações futuras devem usar autenticação OAuth e serviços de backend com controle de acesso e auditoria.
