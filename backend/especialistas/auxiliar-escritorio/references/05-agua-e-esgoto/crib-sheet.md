# Água Potável e Esgotamento Sanitário — Crib Sheet

> Fonte: EBPOS-URB-VOL7 (Rede de Água Potável e Esgotamento Sanitário,
> Compatibilização com a Metodologia BIM). Material conceitual/processual (fluxo
> BIM em Civil 3D), sem tabelas de dimensionamento hidráulico numérico. Combinar
> com Hazen-Williams e o Manual Técnico CORSAN 2025 já fixados como referência
> permanente no SKILL.md principal.

## 1. Traçado de redes de abastecimento — etapas conceituais

1. Análise de demanda (população, consumo per capita, uso industrial/comercial,
   variação horária).
2. Definição de zonas de pressão da rede.
3. Seleção de materiais e diâmetros de tubulação conforme solo, topografia e
   qualidade da água exigida.
4. Minimização de perdas (vazamentos, rupturas) como objetivo permanente de
   traçado.

## 2. Pressure Network (Civil 3D) — rede de água sob pressão

- Composta por tubulações (PVC, ferro fundido, aço, materiais compostos) e conexões
  que transportam água potável sob pressão.
- Estações de bombeamento: necessárias quando a pressão natural não é suficiente
  para atingir áreas elevadas/distantes.
- Válvulas de controle: regulam fluxo e pressão em pontos específicos da rede.
- No Civil 3D, a modelagem de rede pressurizada usa layout de tubulações + acessórios
  (compass rotation, ajuste de conexões) — ferramenta específica citada: *Pressure
  Network*.

## 3. Dimensionamento hidráulico (usar normas complementares)

O material não traz fórmulas numéricas de dimensionamento. Usar como referência
fixa (já no SKILL.md principal):
- **Hazen-Williams** para perda de carga em redes de distribuição de água.
- **Blocos de ancoragem** — metodologia PAM Saint-Gobain: `F = P × S × K`.
- **Manual Técnico CORSAN 2025** para parâmetros de projeto de redes municipais no
  RS (per capita, K1/K2, diâmetros mínimos, profundidades de assentamento) — este é
  o documento de referência primária para dimensionamento real, não o material
  EBPOS.

## 4. Esgotamento sanitário — pontos conceituais do material

- Cálculo de vazão de esgoto mencionado apenas como etapa de projeto (sem fórmula
  explícita no PDF) — normalmente proporcional ao consumo de água (coeficiente de
  retorno, tipicamente 0,8 no Brasil — valor de mercado, **confirmar contra a norma
  CORSAN/ABNT antes de aplicar**, não extraído literalmente deste material).
- Compatibilização entre redes de água e esgoto com drenagem pluvial e demais
  disciplinas é tratada no Capítulo 5 — ver `references/09-compatibilizacao/`.

## 5. Boas práticas de projeto (BIM)

- Verificar cruzamento de rede de água/esgoto com drenagem pluvial e rede elétrica
  no modelo 3D antes da emissão (evita interferências físicas em campo).
- Manter profundidade mínima de assentamento compatível com a carga de tráfego da
  via e o congelamento/movimentação do solo (parâmetro local, confirmar CORSAN).
- Documentar diâmetros e materiais de tubulação diretamente nos atributos do
  modelo BIM para facilitar extração de quantitativos (ver
  `references/10-orcamento/`).

## Lacunas a complementar

Fórmulas de dimensionamento de rede (Hazen-Williams aplicado, per capita, K1/K2,
diâmetro mínimo, declividade mínima de coletor de esgoto) devem vir do Manual
Técnico CORSAN 2025 ou da NBR 9649 (redes coletoras de esgoto) — não estão neste
PDF.
