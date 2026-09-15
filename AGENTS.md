# Orientações para agentes de IA

## Objetivo

Evoluir o Fafa como central operacional da SIZE Engenharia, preservando a identidade visual, a clareza do roteamento e a segurança dos dados.

## Regras de trabalho

1. Leia `README.md`, `docs/ARCHITECTURE.md` e `docs/ROADMAP.md` antes de alterar o código.
2. Preserve a paleta SIZE: verde geomático, verde profissional, turquesa, grafite e cinzas técnicos.
3. Mantenha a tipografia Montserrat e o nome **Fafa**.
4. Trate o catálogo em `src/agents.js` como fonte única dos agentes.
5. Não invente integrações, credenciais, métricas ou estados operacionais.
6. Não conecte nem indexe drives até autorização expressa do responsável pelo projeto.
7. Nunca grave segredos, tokens ou dados pessoais no repositório ou no navegador.
8. Preserve compatibilidade com navegadores atuais e funcionamento responsivo.
9. Teste busca, filtros, roteamento, persistência e exportação após mudanças funcionais.
10. Documente mudanças de arquitetura e limites conhecidos.

## Critérios de conclusão

- Interface sem erros no console.
- Fluxos principais utilizáveis com teclado e mouse.
- Dados locais preservados após recarregar a página.
- Nenhuma credencial ou dado privado versionado.
- Documentação atualizada quando o comportamento mudar.
