# Iluminação Pública e Redes Elétricas — Crib Sheet

> Fonte: EBPOS-URB-VOL8 (Projetos de Iluminação Urbana e Rede Elétrica com BIM).
> O material cobre eletrotécnica básica, NBR 5101 (descritiva, sem tabelas de lux)
> e fluxo BIM para redes aérea/subterrânea. Para os níveis de iluminância exigidos
> por classe de via, consultar a NBR 5101 na íntegra (tabelas não reproduzidas
> neste PDF-fonte).

## 1. Fórmulas elétricas básicas (Capítulo 2)

- **Lei de Ohm**: `I = V / R` (corrente = tensão / resistência)
- **Resistência**: `R = V / I`
- **Potência (Lei de Joule)**: `P = V × I`
- **Potência dissipada em resistência**: `P = I² × R`
- **Tensão de linha vs. fase (trifásico)**: `VL = √3 × Vf`
- **Fator de potência**: `FP = P / S` (potência ativa / potência aparente)
- Potência **ativa**: trabalho útil (calor/mecânico). Potência **aparente** (VA):
  ativa + reativa, base para dimensionamento de rede de distribuição.

## 2. Rede de distribuição aérea x subterrânea (Capítulos 3-4)

- **Rede aérea**: menor custo de implantação, manutenção mais simples, maior
  impacto visual e vulnerabilidade a intempéries.
- **Rede subterrânea**: maior custo inicial, exige projeto de dutos/caixas de
  passagem, preferida em áreas urbanas centrais/loteamentos de padrão elevado.
- Compatibilizar sempre com drenagem e saneamento (interferência de valas) — ver
  `references/09-compatibilizacao/`.

## 3. NBR 5101 — Iluminação Pública (descritivo, sem tabelas numéricas no material)

Aspectos normativos cobertos pela NBR 5101 (conforme descrito no material — os
valores numéricos de cada item devem ser consultados na norma original):
1. Distribuição uniforme da iluminação ao longo da via.
2. Características técnicas das luminárias (potência, eficiência luminosa,
   resistência a intempéries/vandalismo).
3. Critérios de seleção de lâmpadas (eficiência energética, IRC, vida útil).
4. Controle de ofuscamento.
5. Eficiência energética.
6. Procedimentos de manutenção e inspeção.

**NBR 5101 — Iluminação Pública para Pedestres**: mesmos critérios acima,
adaptados para calçadas, praças, parques e passagens subterrâneas, com foco em
segurança e conforto do pedestre.

## 4. Conceitos fotométricos (Capítulo 5)

- **Índice de Reprodução de Cor (IRC)**: escala 0-100; quanto mais próximo de 100,
  mais fiel a reprodução de cores em relação à luz natural.
- **Temperatura de cor**: medida em Kelvin; lâmpadas incandescentes tradicionais
  ~2700K (luz "quente"); LEDs variam amplamente conforme fabricação.
- **Índice de Desconforto Unificado (UGR)**: mede o ofuscamento causado por uma
  fonte de luz — quanto maior, mais desconfortável.

## 5. Ferramenta de simulação

**DIALux**: software de simulação luminotécnica citado no material para
verificação de níveis de iluminância e uniformidade antes da execução do projeto.

## Lacunas a complementar

- Tabelas de iluminância mínima (lux) por classe de via — consultar NBR 5101
  diretamente.
- Espaçamento entre postes e altura de montagem por tipo de luminária — não
  constam no material, consultar catálogo do fabricante + norma.
