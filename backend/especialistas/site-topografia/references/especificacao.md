# Especificação Completa — Landing Page Geotech Premium

## Índice
1. Contexto e objetivo
2. Identidade visual
3. Layout — 10 seções
4. Simulador de orçamento (detalhado)
5. UX e microinterações
6. Acessibilidade
7. SEO e performance
8. Stack tecnológica

---

## 1. Contexto e objetivo

**Persona do designer**: UX Designer Senior, Product Designer, especialista em Conversão (CRO), SaaS B2B, Apple Human Interface, Material Design 3, Stripe Design System, Linear.app, Vercel, Framer e Awwwards.

**Missão**: landing page premium focada em gerar solicitações de orçamento para empresa especializada em:

- Levantamento Topográfico com LiDAR
- Mapeamento Aéreo
- Fotogrametria
- Digital Twin
- BIM As Built
- Modelagem 3D
- Cálculo de Volumes
- Monitoramento de Obras
- Inspeções Técnicas
- Drone DJI Matrice 350 RTK + Zenmuse L2

**Público-alvo**: Engenheiros Civis, Construtoras, Mineradoras, Prefeituras, Concessionárias, Arquitetos, Empresas de Energia, Empresas Ferroviárias, Condomínios, Loteamentos.

**Tom**: tecnologia, precisão, engenharia e confiança. Nunca aparência de site barato. Objetivo: parecer uma empresa milionária, líder em geotecnologia e captura de realidade. Padrão visual digno de Awwwards.

---

## 2. Identidade visual

**Estilo**: minimalista, luxuoso, futurista, corporativo.

**Inspirações**: Apple, Stripe, Linear, Notion, DroneDeploy, Pix4D, Leica Geosystems, Hexagon, Tesla.

**Paleta**:
- Preto
- Cinza grafite
- Branco
- Azul elétrico `#2563EB`
- Verde neon **apenas** para status positivos

**Regras visuais**:
- Muito espaço em branco
- Sombras suaves
- Bordas de 20px (`border-radius: 20px`)
- Glassmorphism discreto
- Ícones minimalistas

**Tipografia**: Inter, SF Pro Display. Fonte grande. Hierarquia impecável.

---

## 3. Layout — 10 seções

### Seção 1 — Hero fullscreen
- Imagem de fundo: Matrice 350 RTK voando sobre uma obra gigantesca (em artifact: usar gradiente escuro sofisticado + SVG/ilustração de drone se não houver imagem real)
- Overlay escuro
- **Headline**: "Dados Precisos para Decisões Inteligentes."
- **Subheadline**: "Levantamentos LiDAR, Topografia, Digital Twin e Monitoramento de Obras com precisão centimétrica."
- Botões: **Solicitar Orçamento** (primário, azul) e **Ver Projetos** (secundário)
- Indicadores animados (count-up ao entrar na viewport):
  - +150 Projetos
  - 99% Precisão
  - 48h Entrega
  - 500 km² Mapeados

### Seção 2 — Por que escolher
Cards animados, cada um com ilustração (3D/isométrica ou ícone premium):
- ✓ Precisão RTK
- ✓ LiDAR
- ✓ Modelos 3D
- ✓ Economia de tempo
- ✓ Segurança
- ✓ Relatórios completos

### Seção 3 — Serviços
Grid elegante. Cada card: imagem, título, descrição, botão "Saiba Mais".

Serviços (12): Topografia LiDAR · Digital Twin · Fotogrametria · Volume de Estoque · As Built BIM · Monitoramento de Obras · Inspeções · Agrimensura · Energia · Mineração · Ferrovias · Condomínios

### Seção 4 — Como funciona
Timeline horizontal com micro animações:
1. Contato → 2. Planejamento → 3. Voo → 4. Processamento → 5. Relatórios → 6. Entrega

### Seção 5 — Simulador de orçamento
Ver seção 4 deste documento. É a peça central da página.

### Seção 6 — Portfólio
- Grid Masonry, fotos gigantes
- Comparador Antes/Depois (slider arrastável)
- Viewer 3D / Point Cloud (em artifact: pode ser canvas com nuvem de pontos animada simples)
- Mapa Interativo

### Seção 7 — Clientes
Logos em escala de cinza; ficam coloridos no hover.

### Seção 8 — Depoimentos
Cards estilo Apple: foto, nome, empresa, ★★★★★.

### Seção 9 — FAQ
Accordion elegante e acessível.

### Seção 10 — CTA final
- Headline: "Pronto para conhecer seu projeto em detalhes?"
- Botão azul grande: **Solicitar Orçamento**

### Footer
Contato, mapa, WhatsApp, Instagram, LinkedIn, email, endereço, LGPD.

---

## 4. Simulador de orçamento (wizard multi-etapas)

A melhor parte da página. Wizard com barra de progresso, transições suaves entre etapas, botões Voltar/Avançar.

**Etapa 1 — Tipo de serviço** (radio):
○ Topografia · ○ Digital Twin · ○ Volume · ○ Inspeção · ○ Fotogrametria

**Etapa 2 — Área** (slider): 100 m² até 10.000 hectares (escala logarítmica recomendada; exibir valor formatado)

**Etapa 3 — Localização**: Google Maps com autocomplete (em artifact sem API key: input de texto com sugestões simuladas de cidades brasileiras ou campo simples)

**Etapa 4 — Prazo** (radio): Urgente · 15 dias · 30 dias · Sem prazo

**Etapa 5 — Produtos desejados** (checkbox):
Ortomosaico · Curvas · MDT · DSM · LAS · DWG · Civil 3D · Revit · IFC · Relatórios

**Etapa 6 — Uploads**: Projeto (PDF, DWG, KML, KMZ) e Fotos. Drag-and-drop com lista dos arquivos selecionados (em artifact: apenas UI, arquivos em memória).

**Etapa 7 — Contato**: Nome · Empresa · Telefone · WhatsApp · Email · Cidade (validação básica de email/telefone)

**Tela final (sucesso)**:
- "Recebemos sua solicitação."
- "Nossa equipe retornará em até 2 horas."
- Botão: **Conversar no WhatsApp** (link `https://wa.me/<numero>` com mensagem pré-preenchida resumindo a solicitação)

---

## 5. UX e microinterações

- Animações suaves, scroll reveal, parallax leve
- Hover premium, loader elegante
- Dark mode, 100% responsivo
- Botões expandem no hover; cards levantam; ícones animam
- Contadores crescem (count-up on scroll)
- Scroll extremamente fluido

---

## 6. Acessibilidade

- WCAG AA, contraste excelente
- Navegação por teclado completa (foco visível)
- Labels em todos os inputs
- ARIA: `aria-expanded` no accordion, `role`/`aria-label` nos controles do wizard, `aria-live` na tela de sucesso

---

## 7. SEO e performance

- Schema.org (LocalBusiness/Service), Open Graph, meta tags
- URLs amigáveis
- Performance 95+ (Lighthouse), lazy loading de imagens

---

## 8. Stack tecnológica

**Projeto de produção**: Next.js · React · Tailwind · Framer Motion · TypeScript · Three.js apenas onde necessário · GSAP apenas para o hero.

**Artifact no chat**: arquivo HTML único auto-contido, CSS custom com variáveis, JS vanilla (ou React via CDN se justificado), Intersection Observer para scroll reveal e contadores, sem dependências de build.
