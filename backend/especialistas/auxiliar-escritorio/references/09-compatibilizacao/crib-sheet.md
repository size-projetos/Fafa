# Compatibilização de Projetos (BIM) — Crib Sheet

> Fonte: EBPOS-URB-VOL9 (Compatibilização e Planejamento de Projetos de
> Infraestrutura Urbana — BIM4D).

## 1. Objetivo da compatibilização

Identificar e resolver conflitos entre disciplinas (topografia, terraplenagem,
drenagem, geotecnia, geométrico, água/esgoto, elétrica) **antes** da execução em
campo, via modelo 3D federado.

## 2. Fluxo de compatibilização por disciplina (Capítulo 2)

Ordem sugerida de verificação cruzada (conforme estrutura do material):
1. **Terraplenagem** — conflitos entre plataforma projetada e relevo natural.
2. **Topografia** — consistência entre superfície levantada e modelo de projeto.
3. **Drenagem** — cruzamento de redes de drenagem com demais disciplinas.
4. **Ensaio de campo** — validar premissas geotécnicas assumidas no modelo.
5. **Geotecnia** — compatibilizar cortes/aterros com capacidade de suporte real do
   solo.

## 3. Clash detection (detecção de conflitos)

- Identifica interferências físicas entre elementos de disciplinas diferentes
  (ex.: tubulação de água cruzando galeria de drenagem sem afastamento mínimo).
- Detecta também conflitos entre projeto e relevo natural do terreno (corte/aterro
  incompatível com a superfície real).
- Deve ser rodada em pontos de controle do projeto (anteprojeto, projeto básico,
  projeto executivo), não apenas ao final.

## 4. Projeto geométrico em BIM — raios mínimos e máximos (Capítulo 3)

O material trata **conceitualmente** a importância dos raios mínimos/máximos de
curvas (segurança, fluidez de tráfego), mas não traz as tabelas numéricas — usar
os valores normativos já consolidados em `references/03-geometrico-e-trp/`
(Quadro 5.4.3.2 do IPR-706) para os raios mínimos reais por velocidade diretriz e
superelevação.

## 5. Animação programática da construção (BIM 4D) — Capítulo 4

- Uso de simulação de cronograma vinculada ao modelo 3D para:
  - Visualização realista da sequência construtiva.
  - Comunicação com stakeholders (cliente, financiador, comunidade).
  - Identificação antecipada de problemas de sequenciamento.
  - Demonstração de progresso físico da obra (medição/acompanhamento).
  - Uso como ferramenta de marketing e vendas em loteamentos.

## 6. Checklist prático de compatibilização (extraído do fluxo do material)

- [ ] Superfície de terraplenagem compatível com relevo natural (sem cortes/aterros
      inconsistentes com a sondagem real).
- [ ] Traçado geométrico compatível com greide de drenagem (sem pontos baixos sem
      escoamento).
- [ ] Redes de água/esgoto/drenagem sem interferência física entre si e com a
      rede elétrica.
- [ ] Raios de curva conferidos contra o Quadro 5.4.3.2 (IPR-706) para a
      velocidade diretriz do trecho.
- [ ] Clash detection rodado em pelo menos 3 marcos do projeto (básico, executivo,
      pré-obra).
