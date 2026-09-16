# Seguranca DUE360

## Classificacao

DUE360 e proprietario e deve ser tratado como material confidencial por padrao.

## Regras

- Nao publicar segredos, chaves, tokens, credenciais ou dados sensiveis.
- Nao expor conteudo proprietario fora de ambientes autorizados.
- Nao conectar agentes, skills ou plugins a ferramentas externas sem revisao previa.
- Nao conceder permissoes de escrita a terceiros sem aprovacao do titular.
- Toda integracao com IA deve declarar dados lidos, escritos, transmitidos ou armazenados.

## Bloqueios Obrigatorios

Bloqueie ou alerte quando:

- Houver risco de vazamento proprietario.
- Houver permissao indefinida.
- Houver conflito com a Constituicao.
- Houver impacto estrutural sem registro de decisao.
- Houver tentativa de alterar Kernel, Plugins ou Governanca sem autorizacao.

## Checklist Rapido

Antes de aprovar uma acao:

- O repositorio ou contexto e privado?
- A Regra de Ouro foi aplicada?
- A Regra Diamante foi aplicada?
- A acao transmite dados para terceiros?
- A acao altera Kernel, Plugins, Skill, Agente ou Governanca?
- Existe necessidade de ADR ou Decision Log?

## Resposta a Incidentes

1. Identificar escopo.
2. Conter acessos, tokens ou integracoes afetadas.
3. Registrar evidencias.
4. Corrigir causa raiz.
5. Revisar governanca, plugins ou adaptadores relacionados.
