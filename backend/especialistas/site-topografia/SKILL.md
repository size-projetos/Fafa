---
name: site-topografia
description: "Cria landing pages premium de alta conversão para empresas de geotecnologia e captura de realidade: topografia LiDAR, mapeamento aéreo com drone, fotogrametria, Digital Twin, BIM As Built, cálculo de volumes, monitoramento de obras e inspeções técnicas. Use SEMPRE que o usuário pedir landing page, site, página de vendas, página de orçamento ou presença web para serviços de drone, LiDAR, topografia, agrimensura, mapeamento, Digital Twin, BIM ou captura de realidade — mesmo que ele não diga 'landing page' explicitamente (ex: 'faz um site pra minha empresa de drone'). Também use para revisar ou melhorar landing pages existentes desse nicho. Padrão visual: Apple/Stripe/Linear, minimalista, luxuoso, dark, azul elétrico #2563EB, digno de Awwwards. Inclui simulador de orçamento em wizard multi-etapas."
---

# Landing Page Geotech Premium

Skill para criar landing pages de padrão Awwwards para empresas de geotecnologia (LiDAR, drone, topografia, Digital Twin, BIM). Objetivo: máxima conversão em solicitações de orçamento, transmitindo tecnologia, precisão, engenharia e confiança — aparência de "empresa milionária", nunca de site barato.

## Workflow

1. **Leia `references/especificacao.md`** — contém a especificação completa e obrigatória: identidade visual, as 10 seções da página, o simulador de orçamento (wizard de 7 etapas), microinterações, acessibilidade, SEO e stack.
2. **Identifique o formato de entrega** antes de codar:
   - **Artifact no chat (padrão)**: arquivo HTML único auto-contido (HTML + CSS + JS vanilla ou React via CDN). Adapte a spec: sem Next.js/build step; Google Maps vira campo de texto com autocomplete simulado ou input simples; Three.js/GSAP via cdnjs apenas se agregarem valor real; uploads viram UI de drag-and-drop sem backend (armazenar em memória).
   - **Projeto completo (se o usuário pedir código de produção/repositório)**: Next.js + React + TypeScript + Tailwind + Framer Motion, estrutura de componentes, conforme a stack da spec.
3. **Personalize com dados reais do cliente** quando fornecidos (nome da empresa, WhatsApp, cidade, projetos, logos). Se não houver, use placeholders claros e coerentes com o nicho (ex: SIZE Engenharia) e avise o usuário do que precisa ser substituído.
4. **Consulte a skill `frontend-design`** (`/mnt/skills/public/frontend-design/SKILL.md`) para decisões estéticas finas antes de escrever o código.
5. **Implemente as 10 seções na ordem da spec.** Nenhuma seção pode ser omitida sem o usuário pedir. O simulador de orçamento é a peça central — capriche nele.
6. **Valide o checklist de qualidade** abaixo antes de entregar.

## Regras de design inegociáveis

- Paleta: preto, cinza grafite, branco, azul elétrico `#2563EB`; verde neon somente para status positivos.
- Tipografia Inter/SF Pro Display, fonte grande, hierarquia impecável, muito espaço em branco.
- Bordas 20px, sombras suaves, glassmorphism discreto, ícones minimalistas (SVG line icons).
- Dark mode como estética principal (hero escuro com overlay).
- Animações suaves: scroll reveal, contadores animados, hover que levanta cards, botões que expandem. Nada exagerado ou "piscante".
- Contraste WCAG AA, navegação por teclado, labels e ARIA em todos os controles interativos.

## Checklist de qualidade (validar antes de entregar)

- [ ] Hero fullscreen com headline "Dados Precisos para Decisões Inteligentes." e CTAs duplos
- [ ] Contadores animados (+150 Projetos, 99% Precisão, 48h Entrega, 500 km² Mapeados)
- [ ] Grid de 12 serviços com cards clicáveis
- [ ] Timeline "Como Funciona" com 6 etapas
- [ ] Simulador de orçamento wizard com 7 etapas + tela de sucesso + botão WhatsApp
- [ ] Portfólio com comparador antes/depois funcional
- [ ] FAQ em accordion acessível (botões reais, aria-expanded)
- [ ] CTA final + footer completo com LGPD
- [ ] 100% responsivo (testar mentalmente mobile 380px)
- [ ] Zero aparência de template genérico/barato
