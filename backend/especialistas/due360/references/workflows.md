# Workflows DUE360

## Consulta Simples

Use quando o usuario pedir explicacao, resumo ou orientacao.

1. Identifique o topico.
2. Consulte o recurso correspondente.
3. Responda de forma direta.
4. Aponte riscos se existirem.

## Decisao Estrutural

Use quando o pedido afetar Constituicao, Regras, Motor de Decisao, Kernel, Plugins, Governanca, Skill ou Agente.

Formato:

```text
Classificacao:
Decisao:
Aplicacao da Regra de Ouro:
Aplicacao da Regra Diamante:
Impacto:
Riscos:
Registro recomendado:
Proximo passo:
```

## Mudanca Documental

1. Identificar documento afetado.
2. Verificar se a mudanca altera sentido ou apenas forma.
3. Se alterar sentido, recomendar ADR ou Decision Log.
4. Preservar linguagem proprietaria e governanca.

## Plugin

1. Definir finalidade.
2. Declarar escopo.
3. Declarar dependencias.
4. Avaliar impacto no Kernel.
5. Classificar estado: Proposto, Experimental, Ativo, Suspenso ou Obsoleto.
6. Registrar decisao.

## Skill

1. Confirmar que a skill e adaptador, nao nucleo.
2. Definir quando a skill deve ser usada.
3. Definir recursos de referencia.
4. Definir bloqueios obrigatorios.
5. Testar com exemplos controlados.

## Agente

1. Definir objetivo.
2. Definir permissoes.
3. Declarar ferramentas.
4. Aplicar Motor de Decisao antes da execucao.
5. Registrar resultados.
6. Bloquear quando houver conflito.
