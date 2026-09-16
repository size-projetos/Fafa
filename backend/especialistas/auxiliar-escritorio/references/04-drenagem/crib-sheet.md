# Drenagem Urbana — Crib Sheet

> Fonte: EBPOS-URB-VOL6 (Drenagem Urbana Utilizando a Metodologia BIM). Material
> focado em fluxo de trabalho BIM/Civil 3D, não traz fórmulas hidrológicas
> (método racional, IDF, Manning) com valores numéricos. Para dimensionamento
> hidráulico completo, o próprio material referencia os manuais DNIT abaixo — não
> incluídos neste pacote de PDFs, recomenda-se buscá-los separadamente.

## 1. Bibliografia normativa citada (não incluída no PDF, buscar separadamente)

- **DNIT — Manual de Hidrologia Básica para Estruturas de Drenagem (IPR-715)**
- **DNIT — Manual de Drenagem de Rodovias (IPR-724)**
- **DNIT — Álbum de Projetos-Tipo de Dispositivos de Drenagem (IPR-736)**
- SUDECAP — Caderno de Encargos, Capítulo 19: Drenagem (referência municipal, BH)

## 2. Fluxo de projeto executivo de drenagem em BIM (Civil 3D)

1. **Catchment Analysis (Análise de Bacias de Contribuição)** — delimitação das
   sub-bacias de drenagem a partir do MDT/superfície TIN.
2. **Pipe Network Design (Projeto de Rede de Tubulação)** — layout de tubulações de
   drenagem pluvial e esgoto sanitário, gestão de conexões entre tubos, geração de
   perfis longitudinais e verificação de cruzamentos com outras redes.
3. **Grading Tools (Ferramentas de Terraplenagem)** — não são exclusivas de
   drenagem, mas modelam a superfície (taludes, rampas, canaletas) para garantir o
   escoamento correto das águas pluviais.
4. Extração de quantitativos e informações do modelo (Capítulo 4) para memorial e
   orçamento.
5. Uso de biblioteca BIM de componentes de drenagem (poços de visita, bocas de
   lobo, tubulações padronizadas) — Capítulo 5.

## 3. Sistema de drenagem pluvial: hierarquia

- **Microdrenagem**: rede local (bocas de lobo, galerias secundárias) que capta o
  escoamento superficial de lotes e vias locais.
- **Macrodrenagem**: sistema regional/estrutural (canais, galerias principais,
  bacias de detenção) que recebe as contribuições da microdrenagem.
- **Controles regionais**: dispositivos de amortecimento de cheias (bacias de
  detenção/retenção) — mencionados como parte do capítulo, sem dimensionamento
  numérico no material.

## 4. Pontos de atenção para compatibilização (uso prático)

- Verificar cruzamento de redes de drenagem com outras infraestruturas (água,
  esgoto, elétrica) diretamente no modelo BIM antes da emissão do projeto — ver
  `references/09-compatibilizacao/`.
- A superfície de terraplenagem (grading) deve ser compatível com o greide viário
  do projeto geométrico (`references/03-geometrico-e-trp/`) para não gerar pontos
  baixos sem escoamento.

## Lacunas a complementar

Para dimensionamento hidráulico real (vazão de projeto, tempo de concentração,
diâmetro de tubulação, período de retorno), buscar os manuais IPR-715 e IPR-724
citados acima, ou a norma municipal aplicável ao município do projeto (ex.: plano
diretor de drenagem urbana local).
