# Orçamento e Quantificação (BIM 5D) — Crib Sheet

> Fontes: EBPOS-URB-VOL10 (Quantificação e Orçamentação — BIM5D) e
> EBPOS-URB-VOL9 (BDI). Material conceitual, com uma fórmula numérica central (BDI).

## 1. Fórmula do BDI (Benefícios e Despesas Indiretas)

```
BDI = (Custos Diretos + Custos Indiretos) / Custos Diretos
```

- **Custos diretos**: materiais, mão de obra, equipamentos — diretamente
  associáveis à execução da obra.
- **Custos indiretos**: aluguel, energia, seguros, despesas administrativas — não
  alocáveis a uma obra específica, mas necessários para viabilizá-la.
- O BDI varia conforme tipo de obra, localização, complexidade e prazo — não existe
  valor fixo universal; calcular caso a caso.

> Nota: esta é a formulação simplificada apresentada no material. Em licitações
> públicas brasileiras, o cálculo de BDI segue acórdãos do TCU (ex.: Acórdão
> 2622/2013) com fórmula detalhada por parcela (AC, S, R, G, DF, L, I) — usar essa
> versão completa quando o orçamento for para órgão público.

## 2. Identificação de custos diretos e indiretos (Capítulo 4)

Fluxo conceitual:
1. Levantar todos os itens de serviço da obra (quantitativos).
2. Separar custo direto de cada item (material + mão de obra + equipamento).
3. Consolidar custos indiretos da empresa (rateio proporcional ao porte da obra).
4. Aplicar o BDI sobre os custos diretos para chegar ao preço de venda.
5. Em ambiente BIM, os passos 1-2 são semi-automatizados pela extração de
   quantitativos do modelo (ver seção 3).

## 3. Quantificação BIM 5D — fluxo de trabalho

1. Modelo 3D com elementos parametrizados (cada objeto carrega atributos de
   material, dimensão, especificação).
2. Extração automática de quantitativos (Capítulo 3) — elimina medição manual em
   planta 2D, reduz erro humano.
3. Vinculação dos quantitativos a uma base de composições de custo (unitárias).
4. Simulação de cenários (alteração de especificação → recálculo automático de
   custo).
5. Integração com cronograma (BIM 4D) para curva de desembolso físico-financeiro.

## 4. Benefícios do BIM na orçamentação (citados no material)

- Maior transparência e rastreabilidade dos quantitativos.
- Redução de divergências entre projeto e orçamento (planilha sempre atualizada
  com o modelo).
- Simulação de cenários de custo antes da execução.
- Integração de todas as disciplinas em uma base única de quantitativos.

## 5. Ponto de atenção prático

Ao extrair quantitativos de um modelo BIM para orçamento, conferir se os atributos
de material/dimensão foram preenchidos corretamente em **todos** os elementos —
erro de atributo não aparece como erro geométrico, mas gera quantitativo errado
silenciosamente. Fazer verificação cruzada por amostragem contra medição manual em
pelo menos uma disciplina antes de fechar o orçamento.
