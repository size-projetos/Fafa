# Projeto Geométrico, Terraplenagem e Segurança Viária — Crib Sheet

> Fontes: Manual de Projeto Geométrico de Rodovias Rurais (DNIT/IPR-706), Manual de
> Projeto de Interseções (DNIT/IPR-718), Instruções de Serviço para Projetos
> Rodoviários (DNIT/IPR-726), Manual de Projeto de Acessos a Áreas Lindeiras a
> Rodovias Federais (DNIT/IPR-728), Manual de Projeto Geométrico de Travessias
> Urbanas (DNIT/IPR-740); EBPOS-URB-VOL4 (Projeto Geométrico e Terraplenagem BIM),
> EBPOS-URB-VOL9 (Compatibilização); Curso PROJGEO0002 Mód. 01 (Segurança Viária) e
> Mód. 02 (Normas Técnicas de Projeto Geométrico e Interseções).
> Ver `assets/03-geometrico-e-trp/` para figuras extraídas dos manuais.

## 1. Distância de visibilidade para tomada de decisão em acessos (IPR-728)

Tabela 2 (veículos comuns) — valores mínimos, segundo a velocidade diretriz da via:

| V diretriz (km/h) | 50 | 60 | 70 | 80 | 90 | 100 | 110 | 120 |
|---|---|---|---|---|---|---|---|---|
| Dv mínima (m) | 145 | 170 | 200 | 230 | 270 | 315 | 330 | 360 |

Tabela 3 (veículos especiais / cargas indivisíveis):

| V diretriz (km/h) | 50 | 60 | 70 | 80 | 90 | 100 | 110 | 120 |
|---|---|---|---|---|---|---|---|---|
| Dv mínima (m) | 195 | 235 | 275 | 315 | 355 | 390 | 430 | 470 |

Fonte primária citada pelo DNIT: AASHTO, *A Policy on Geometric Design of Highways
and Streets* (2018). Os três pontos de verificação (Dv1 divergência, Dv2 cruzamento,
Dv3 convergência) devem atender ao mínimo tabelado — ver Figura 1 do manual (extraída
em `assets/`). Ajustar pela Tabela 4 do manual em função do greide da via.

## 2. Distância de visibilidade de parada — ciclovias (IPR-740)

Fórmula geral (mesma lógica da rodovia, adaptada ao ciclista):

```
D = V² / [254·(f ± G)] + V/1,4
```
- D = distância mínima de visibilidade de parada (m)
- V = velocidade de projeto (km/h)
- f = coeficiente de atrito = 0,25 (ciclovias)
- G = greide (m/m); sinal + subida, − descida
- Premissas: tempo de percepção-reação 2,5 s; altura do olho do ciclista 1,4 m; altura do objeto = 0

Tabela 16 — distância mínima de visibilidade de parada em declive (m):

| V projeto (km/h) | 0% | 5% | 10% | 15% | 20% |
|---|---|---|---|---|---|
| 10 | 9 | 9 | 10 | 11 | 15 |
| 20 | 21 | 22 | 25 | 30 | 46 |
| 30 | 36 | 39 | 45 | 57 | 92 |
| 40 | 54 | 60 | 71 | 92 | 155 |
| 50 | 75 | 85 | 101 | 134 | 233 |

## 3. Raios mínimos para ciclovias (IPR-740, e = 2%)

Superelevação: mínimo técnico 2% (drenagem), máximo recomendado ~5%.

| V projeto (km/h) | Coef. atrito f | Raio mínimo (m) |
|---|---|---|
| 20 | 0,31 | 10 |
| 30 | 0,28 | 24 |
| 40 | 0,25 | 47 |
| 50 | 0,21 | 86 |

Greides: evitar > 5%; aceitável acima de 5% só em trechos < 240 m com velocidade de
projeto elevada.

## 4. Hierarquia funcional de vias (IPR-740, base DNER 1974)

| Áreas urbanas | Áreas rurais |
|---|---|
| Sistema Arterial Principal / Secundário | Sistema Arterial Principal / Primário / Secundário |
| Sistema Coletor | Sistema Coletor Primário / Secundário |
| Sistema Local | Sistema Local |

Espaçamento típico de vias arteriais principais em áreas urbanas: 1,6 km (centros
comerciais densos) a 8 km+ (áreas periféricas pouco desenvolvidas).

## 5. Interseções (IPR-718)

- Parâmetros de projeto tabelados separadamente para interseções de **3 ramos**
  (Tabela 7) e **4 ramos** (Tabela 8) — consultar o manual/`assets/` para os valores
  completos, pois variam por tipo de solução (canalizada, rotatória, etc.).
- Velocidades de projeto de rótulas (rotatórias) convencionais: Tabela 14 do manual;
  rótulas de baixa velocidade operam em torno de **20 km/h**.
- Redução de acidentes ao evoluir de interseção tipo A → tipo B/C e ao deslocar
  interseção de 4 ramos: ver Tabelas 9 e 10 (percentuais de redução — consultar fonte
  para o caso específico, variam por configuração).
- Capacidade de ramos, áreas de convergência/divergência: Tabelas 11-13.
- Fatores de equivalência em Unidades de Carro de Passeio (UCP): Tabela 18.

## 6. Meios-fios e travessias (IPR-740)

- V < 80 km/h: preferir meio-fio transponível (chanfrado) de **15 cm** de altura.
- V ≥ 80 km/h: preferir meio-fio transponível de **10 cm** de altura.
- Travessia em desnível (passarela/subsolo) recomendada para vias com V até 60 km/h
  em condições específicas de fluxo — avaliar caso a caso conforme o manual.

## 7a. Distância de visibilidade de parada em rodovias rurais (IPR-706, Quadro 5.3.1.3)

Fórmula geral:
```
d = 0,7·V + V² / [255·(f + i)]
```
- d = distância de visibilidade de parada (m)
- V = velocidade diretriz ou velocidade média (km/h)
- f = coeficiente de atrito longitudinal (pavimento molhado)
- i = greide (m/m; + ascendente, − descendente)
- 0,7·V representa o percurso no tempo de percepção-reação (2,5 s)

Coeficientes de atrito longitudinal por velocidade diretriz — Quadro 5.3.1.2:

| Vdir (km/h) | 30 | 40 | 50 | 60 | 70 | 80 | 90 | 100 | 110 | 120 |
|---|---|---|---|---|---|---|---|---|---|---|
| f | 0,40 | 0,37 | 0,35 | 0,33 | 0,31 | 0,30 | 0,29 | 0,28 | 0,28 | 0,27 |

Distância de visibilidade de parada mínima, greide nulo (m), calculada pela fórmula
acima e arredondada para múltiplos de 5:

| V (km/h) | 30 | 40 | 50 | 60 | 70 | 80 | 90 | 100 | 110 | 120 |
|---|---|---|---|---|---|---|---|---|---|---|
| d mín. (m) | 30 | 45 | 65 | 85 | 110 | 140 | 175 | 210 | 245 | 295 |

> Só é obrigatório atender à distância mínima para greide nulo (o manual permite
> desprezar o efeito do greide na maioria dos casos, ver Quadro 5.3.1.3 do original
> para valores específicos por greide de -6% a +6%). A Distância de Visibilidade
> Desejada (Quadro 5.3.1.4, baseada na velocidade média — maior que a diretriz em
> pistas simples) é a meta de projeto quando as condições permitirem.



Fórmula (equilíbrio da força centrífuga, Figura 5.4.3.1 do manual):

```
Rmin = V² / [127 × (emax + fmax)]
```
- R = raio mínimo da curva (m)
- V = velocidade diretriz (km/h)
- emax = taxa máxima de superelevação adotada (m/m)
- fmax = coeficiente de atrito transversal máximo admissível (adimensional)

Coeficientes de atrito transversal máximo admissível — Quadro 5.4.3.1:

| V diretriz (km/h) | 30 | 40 | 50 | 60 | 70 | 80 | 90 | 100 | 110 | 120 |
|---|---|---|---|---|---|---|---|---|---|---|
| fmax | 0,19 | 0,18 | 0,16 | 0,15 | 0,15 | 0,14 | 0,14 | 0,13 | 0,12 | 0,11 |

Raios mínimos (m) resultantes — Quadro 5.4.3.2, por taxa máxima de superelevação:

| emax \\ V (km/h) | 30 | 40 | 50 | 60 | 70 | 80 | 90 | 100 | 110 | 120 |
|---|---|---|---|---|---|---|---|---|---|---|
| 4% | 30 | 55 | 100 | 150 | 205 | 280 | 355 | 465 | 595 | 755 |
| 6% | 30 | 50 | 90 | 135 | 185 | 250 | 320 | 415 | 530 | 665 |
| 8% | 25 | 50 | 80 | 125 | 170 | 230 | 290 | 375 | 475 | 595 |
| 10% | 25 | 45 | 75 | 115 | 155 | 210 | 265 | 340 | 435 | 540 |
| 12% | 25 | 40 | 70 | 105 | 145 | 195 | 245 | 315 | 395 | 495 |

> Valores recalculados pela fórmula e coeficientes acima e conferidos linha a linha
> contra o OCR do manual original (Quadro 5.4.3.2) — convergência exata ou por
> arredondamento de ≤2 m em todas as células cruzadas. Superelevação máxima usual de
> projeto no Brasil: 8% em rodovias rurais (12% em casos excepcionais, condições
> especiais de clima/relevo); em travessias urbanas com meio-fio, é comum limitar a
> 4% (ver IPR-740).

Sempre objetivar raios superiores ao mínimo — os valores do quadro são limites, não
recomendações de projeto.

## 7b. Classes de projeto e rampas máximas (IPR-706)

Classificação técnica por classe de projeto — Quadro 5.8.1 (critério simplificado):

| Classe | Característica | Critério de tráfego |
|---|---|---|
| Via Expressa | Controle total de acesso | Decisão administrativa |
| I-A | Pista dupla, controle parcial de acesso | Nível de serviço da pista simples insuficiente |
| I-B | Pista simples | VHP > 200 e VMD > 1.400 |
| II | Pista simples | VMD 700–1.400 |
| III | Pista simples | VMD 300–700 |
| IV-A | Pista simples | VMD (abertura) 50–200 |
| IV-B | Pista simples | VMD (abertura) < 50 |

VHP = volume horário de projeto; VMD = volume médio diário.

Rampas máximas (%) por classe de projeto e tipo de relevo — Quadro 5.5.2.1:

| Classe | Plano | Ondulado | Montanhoso |
|---|---|---|---|
| 0 | 3% | 4% | 5% |
| I | 3% | 4,5% | 6% |
| II | 3% | 5% | 7% |
| III | 4% | 6% | 8% |
| IV-A | 4% | 6% | 8% |
| IV-B | 6% | 8% | 10%* |

\* Rampas acima de 8% devem ser limitadas, quando possível, a trechos contínuos de
até 300 m.

Curvas verticais de concordância: parábola do 2º grau, parâmetro K (m por 1% de
variação de rampa); comprimento `L = K × A` (A = diferença algébrica das rampas, %);
arredondar L para múltiplos de 20 m. Pode-se usar curva circular equivalente com
`R = 100·K`.

## 8. Segurança viária — conceitos-chave (PROJGEO0002 Mód. 01, manuais complementares)

- **Hierarquia de intervenção** (visão sistêmica, "Safe System"): eliminar risco na
  origem > separar usuários vulneráveis > reduzir velocidade de conflito > mitigar
  consequência do impacto.
- **Zonas de trânsito calmo (traffic calming)**: uso de lombadas, estreitamentos,
  chicanes e mudanças de pavimento para reduzir velocidade em áreas residenciais e
  centros urbanos (referência: guia WRI 2022 "Áreas de Trânsito Calmo").
- **Auditoria de segurança viária**: revisão sistemática de projeto/via existente
  por equipe independente, em fases distintas do projeto (viabilidade, projeto
  básico, projeto executivo, pré-abertura, via em operação).
- Referências de literatura técnica disponíveis no material complementar: manual de
  intervenções de segurança viária (iRAP/consolidado internacional), manual DER-SP,
  Elvik *Handbook of Road Safety Measures*, guia global de desenho de ruas (NACTO/
  Global Street Design Guide), "O Desenho de Cidades Seguras".

## 9. BIM aplicado a projeto geométrico e terraplenagem (EBPOS-URB-VOL4)

Fluxo de trabalho típico (Civil 3D / metodologia BIM):
1. Importar levantamento topográfico (superfície TIN).
2. Definir traçado horizontal (alinhamentos, curvas de concordância).
3. Definir perfil longitudinal e greide.
4. Gerar seções transversais.
5. Calcular volumes de corte/aterro (projeto de terraplenagem).
6. Extrair quantitativos para orçamento.

Elementos do projeto geométrico: traçado horizontal, curvas de concordância
(horizontais e verticais), perfil longitudinal, greide, seções transversais.

## Domínios ainda sem cobertura direta

- **Pavimentação**: nenhum PDF do material fornecido trata especificamente de
  dimensionamento de pavimentos (apenas menções pontuais a CBR/ISC no volume de
  geotecnia — ver `references/02-geotecnica/`). Recomenda-se complementar com o
  Manual de Pavimentação DNIT (IPR-719) se necessário.
