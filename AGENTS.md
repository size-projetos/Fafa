# Orientações para agentes de IA

## Objetivo

Evoluir o Fafa como central operacional da SIZE Engenharia, preservando a identidade visual, a clareza do roteamento e a segurança dos dados.

## Regras de trabalho

1. Leia `README.md`, `CONTEXT.md`, `docs/ARCHITECTURE.md` e `docs/ROADMAP.md` antes de alterar o código. Para o backend, leia também `backend/README.md` e `backend/docs/arquitetura.md`.
2. Preserve a paleta SIZE: verde geomático, verde profissional, turquesa, grafite e cinzas técnicos.
3. Mantenha a tipografia Montserrat e o nome **Fafa**.
4. Trate o catálogo em `src/agents.js` como fonte única dos agentes.
5. Não invente integrações, credenciais, métricas ou estados operacionais.
6. Não conecte nem indexe drives até autorização expressa do responsável pelo projeto.
7. Nunca grave segredos, tokens ou dados pessoais no repositório ou no navegador.
8. Preserve compatibilidade com navegadores atuais e funcionamento responsivo.
9. Teste busca, filtros, roteamento, persistência e exportação após mudanças funcionais.
10. Documente mudanças de arquitetura e limites conhecidos.

## Regras específicas do backend (`backend/`)

11. Toda ferramenta nova é uma função Python tipada, com docstring, decorada com `@ferramenta` — o schema é gerado dela; não escreva schemas à mão.
12. Padrão de coordenadas: SIRGAS 2000 / UTM 22S (EPSG:31982), geográfico EPSG:4674. Só mude quando o usuário pedir.
13. Rode `pytest` e `ruff check src tests` antes de considerar uma mudança pronta. A projeção interna deve continuar batendo com o pyproj (< 1 mm).
14. Segredos ficam apenas no `backend/.env` local. `.env.example` lista as variáveis, sempre vazias.
15. Não adicione canais (Telegram, web) nem integrações (Drive, e-mail) sem pedido expresso de Daniel; a interface `Canal` já existe para quando for a hora.
16. Português do Brasil no código, nas docstrings e nas mensagens ao usuário.
17. `backend/especialistas/` espelha as skills do Daniel; não edite o conteúdo delas aqui (edite a skill de origem e copie de novo). O Fafa indica GPTs a partir de `src/agents.js`; nunca duplique o catálogo em outro lugar.

## Critérios de conclusão

- Interface sem erros no console.
- Fluxos principais utilizáveis com teclado e mouse.
- Dados locais preservados após recarregar a página.
- Nenhuma credencial ou dado privado versionado.
- Documentação atualizada quando o comportamento mudar.
- Backend: testes passando e `fafa tools` listando as ferramentas sem erro.
