# Urbanismo Viário e Segurança Viária — Crib Sheet

> Fontes: PROJGEO0002 Mód. 01 (Segurança Viária Aplicada ao Projeto Geométrico) e
> material complementar: Guia de Redução de Acidentes com Base em Medidas de
> Engenharia de Baixo Custo (DNIT/IPR-703), Manual de Segurança Viária (DER-SP),
> Handbook of Road Safety Measures (Elvik), Global Street Design Guide (NACTO,
> "guia global de desenho de ruas"), Guia de Áreas de Trânsito Calmo (WRI 2022),
> "O Desenho de Cidades Seguras", Livro Segurança no Trânsito (Coca Ferraz).
> Corpus muito extenso (>3.000 páginas somadas); este crib sheet cobre a
> metodologia estrutural — para casos específicos, consultar o PDF de origem
> indicado em cada item (todos disponíveis em `/mnt/skills/...` via referência
> cruzada, ou no material original do usuário).

## 1. Metodologia de identificação de pontos críticos (IPR-703)

Fluxo do "Guia de Redução de Acidentes" (DNER/DNIT), adaptável a qualquer rede
viária ou área urbana:

1. **Identificação dos segmentos concentradores de acidentes** — a partir de
   listagens de acidentes por trecho (quilometragem, VMD, índice de acidentes e
   índice crítico calculado por trecho).
2. **Coleta e análise de dados de acidentes** — boletins de ocorrência, tipo,
   gravidade, causas prováveis.
3. **Inspeção de campo** do segmento selecionado — checklist, croqui, cadastro
   fotográfico, entrevistas.
4. **Diagnóstico** — associar padrões de acidente a causas prováveis (geometria,
   sinalização, pavimento, comportamento).
5. **Proposição de melhorias** — priorizar soluções de baixo custo antes de obras
   de grande porte.
6. **Avaliação econômica** — comparar custo da intervenção com benefício estimado
   (redução de acidentes × custo médio por acidente/vítima).
7. **Implantação, monitoramento e avaliação de efetividade** (antes x depois, com
   ajuste estatístico quando possível).

**Taxa de acidentes por exposição** (prática consolidada internacional, útil para
comparar segmentos de volumes de tráfego diferentes):

```
Taxa (acid./106 veíc.km) = (Nº de acidentes × 10^6) / (VDM × 365 × extensão do trecho em km × nº de anos)
```

> Fórmula de uso corrente na engenharia de tráfego (não citada literalmente no
> trecho revisado do IPR-703) — confirmar contra a versão exata do guia antes de
> uso formal em relatório técnico/pericial.

## 2. Hierarquia de intervenção — Safe System / Visão Zero

Princípio adotado pelos guias internacionais (Elvik, NACTO, WRI):
1. **Eliminar** o risco na origem (ex.: eliminar cruzamento em nível).
2. **Separar** usuários vulneráveis de tráfego motorizado (ciclovia física,
   calçada segregada).
3. **Reduzir a velocidade de conflito** para um nível sobrevivível (traffic
   calming, redução de velocidade em áreas de conflito com pedestre: referência
   internacional usual é 30 km/h em áreas de convivência intensa).
4. **Mitigar a consequência** do impacto quando não é possível evitá-lo
   (dispositivos de contenção, zonas de amortecimento).

## 3. Trânsito calmo (traffic calming) — dispositivos típicos (Guia WRI 2022)

- Lombadas e almofadas redutoras de velocidade.
- Estreitamentos de pista (chicanes, extensões de calçada/orelhas).
- Mudança de textura/cor de pavimento em travessias.
- Minirrotatórias em interseções locais.
- Fechamento parcial de vias (diagonal diverters) em áreas residenciais.

## 4. Auditoria de segurança viária — fases

1. Viabilidade / concepção.
2. Projeto básico.
3. Projeto executivo.
4. Pré-abertura ao tráfego.
5. Via em operação (auditoria de via existente).

Cada fase deve ser conduzida por equipe **independente** da equipe de projeto.

## 5. Desenho de ruas seguras — princípios do Global Street Design Guide (NACTO)

- Rua como espaço público multifuncional, não apenas corredor de tráfego motorizado.
- Priorização hierárquica de modos: pedestre > ciclista > transporte público >
  veículo particular, em áreas urbanas centrais.
- Redução da largura de faixa de rolamento como ferramenta de moderação de
  velocidade (faixas mais largas induzem maior velocidade praticada).
- Interseções compactas reduzem tempo de exposição do pedestre na travessia.

## 6. Relação com o projeto geométrico

Os raios mínimos, distâncias de visibilidade e rampas máximas ficam em
`references/03-geometrico-e-trp/` — este arquivo trata do **enquadramento de
segurança e urbanístico** que orienta a escolha de parâmetros dentro da faixa
normativa (ex.: preferir valores acima do mínimo em trechos com alto fluxo de
pedestres, mesmo que o mínimo normativo permita menos).

## Observação sobre profundidade de cobertura

Os manuais complementares de segurança viária somam mais de 3.000 páginas (Elvik,
DER-SP, guia global de desenho de ruas, entre outros). Este crib sheet cobre a
estrutura metodológica e os princípios mais citados; para uma consulta pontual e
aprofundada (ex.: efetividade específica de uma contramedida, valores de projeto de
uma interseção-tipo), peça para eu reabrir o PDF de origem e extrair o trecho exato.
