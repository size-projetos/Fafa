# Geotecnia — Crib Sheet

> Fonte: EBPOS-URB-VOL3 (Análises Geotécnicas em Áreas Urbanas e Loteamentos,
> Compatibilização com a Metodologia BIM). Material conceitual/processual — sem
> tabelas normativas de classificação numérica (ex.: faixas SUCS/HRB completas).
> Usar em conjunto com as NBRs de sondagem, fundações e concreto já referenciadas
> no SKILL.md principal.

## 1. Investigação geotécnica — métodos

- **Investigação de superfície**: mapeamento geológico, geofísica (eletrorresistividade,
  GPR), fotointerpretação.
- **Sondagem** (Capítulo 1): SPT (Standard Penetration Test) é o ensaio de campo mais
  citado como base para fundações e taludes.
- **Ensaio de campo** (Capítulo 3): complementa a sondagem para parâmetros in situ.

## 2. Ensaios de laboratório (Capítulo 2)

Sequência típica de caracterização de solo:
1. **Amostragem do solo** — coleta representativa, cuidado com alteração de umidade/
   estrutura.
2. **Análise granulométrica por peneiramento** — série de peneiras de aberturas
   graduadas; resultado expresso em % retida acumulada por peneira → curva
   granulométrica.
3. **Limites de Atterberg**:
   - **Limite de Liquidez (LL)**: teor de umidade na transição do estado plástico
     para o líquido.
   - **Limite de Plástico (LP)**: teor de umidade na transição do estado semissólido
     para o plástico.
   - **Índice de Plasticidade (IP) = LL − LP** (não explicitado no material, mas é a
     definição padrão de geotecnia — confirmar contra NBR 7180/6459 antes de uso
     formal).
4. **Ensaio de ISC/CBR (California Bearing Ratio)**:
   - Amostra compactada em cilindro padronizado, submetida a carga vertical.
   - CBR = razão percentual entre a carga necessária para penetrar o solo-amostra e
     a carga necessária para a mesma penetração em amostra padrão de rocha britada.
   - Usado para dimensionamento de pavimentos e avaliação de capacidade de suporte.
5. **Resistência mecânica e durabilidade de agregados** — ensaios de forma dos grãos,
   resistência à compressão simples, contaminação por finos plásticos.
6. **Adensamento e Triaxial Rápido** — parâmetros de compressibilidade e resistência
   ao cisalhamento, usados em fundações e aterros sobre solos compressíveis.

## 3. Aterros sobre solos compressíveis (Capítulo 4)

- Foco em geometria do aterro: inclinação de taludes, forma da base (base larga
  distribui melhor as cargas, reduz recalque diferencial).
- Taxa de carregamento: aplicação rápida de carga pode gerar liquefação em solos
  granulares saturados ou resposta não-drenada crítica em solos coesivos — atenção
  em aterros de grande altura e cronogramas de construção acelerados.

## 4. Taludes, contenções e geossintéticos (Capítulo 5)

- Estabilidade de taludes em corte e aterro é tratada de forma conceitual no
  material; para verificação quantitativa (fator de segurança), usar o **método da
  encosta infinita** já adotado como padrão no SKILL.md principal, ou métodos de
  equilíbrio limite (Bishop, Fellenius) conforme a complexidade do caso.
- Geossintéticos mencionados como solução de reforço/contenção — sem
  dimensionamento numérico detalhado no material-fonte.

## 5. Aplicações citadas para investigação geotécnica

Fundações, barragens, taludes de corte/aterro, pavimentação, contenções — sempre
como insumo de entrada para compatibilização com os demais projetos (ver
`references/09-compatibilizacao/`).

## Lacunas a complementar

Este material não traz:
- Tabelas de classificação SUCS/HRB com faixas numéricas.
- Fórmulas de fator de segurança de taludes.
- Parâmetros de dimensionamento de fundações (capacidade de carga, recalque).

Para esses itens, recomenda-se consultar diretamente as NBRs aplicáveis (6502, 6484,
6489, 6502, 9603, 6122) ou complementar com um manual técnico de mecânica dos solos.
