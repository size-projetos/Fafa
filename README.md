# Fafa | SIZE Engenharia

Central operacional de IA da SIZE Engenharia. A aplicação organiza agentes especializados, recomenda o agente adequado para cada solicitação e mantém projetos, tarefas, riscos, decisões e registros de arquivos no navegador.

## Executar localmente

Sirva a pasta `src` com qualquer servidor HTTP estático. Exemplo:

```bash
python -m http.server 4173 --directory src
```

Abra `http://127.0.0.1:4173`.

## Estrutura

- `src/index.html`: interface principal.
- `src/style.css`: identidade visual e responsividade.
- `src/agents.js`: catálogo e roteamento dos agentes.
- `src/app.js`: navegação e interações principais.
- `src/operations.js`: projetos, tarefas, riscos, decisões e persistência local.
- `docs/ARCHITECTURE.md`: arquitetura e limites atuais.
- `docs/ROADMAP.md`: próximas integrações.
- `AGENTS.md`: orientação para agentes de IA que alterarem o projeto.

## Estado atual

A versão 1 funciona como aplicação estática e armazena os dados no `localStorage` do navegador. A integração com drives está deliberadamente pausada até a organização das fontes de arquivos.

## Privacidade e propriedade

Projeto privado da SIZE Engenharia. Marcas, logotipos e materiais visuais pertencem aos respectivos titulares. Não publique nem redistribua sem autorização.
