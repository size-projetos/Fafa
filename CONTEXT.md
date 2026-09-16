# Contexto do Projeto — Fafa | SIZE Engenharia

Atualizado em 15 de setembro de 2026.

## 1. Visão do produto

O **Fafa** é o agente central da SIZE Engenharia, inspirado no conceito de um assistente operacional como o Jarvis. Seu nome é uma alusão a Fabiano, idealizador e fundador da empresa.

O produto foi concebido para receber uma solicitação, entender a especialidade necessária, recomendar o agente mais adequado e concentrar informações operacionais da empresa em um único painel.

## 2. Identidade visual

- Marca: **Fafa — seu agente pessoal de IA**.
- Empresa: **SIZE Engenharia Ambiental Ltda.**
- Linguagem visual: tecnológica, precisa e corporativa.
- Paleta principal: Verde Geomático `#00AB78`, Verde Profissional `#0F7D5A`, Turquesa `#00B3B8`, Grafite `#2E2E2E`, Cinza Técnico `#6B6B6B` e Cinza Claro `#E9ECEF`.
- Tipografia: Montserrat.
- O símbolo do Fafa deriva da geometria modular da marca SIZE e incorpora a letra F.

## 3. Organização dos agentes

O catálogo atual possui **29 links únicos**, separados por origem e especialidade.

### Montani

Todos os agentes com nomes de heróis pertencem à categoria Montani. Atuam principalmente em criação de imagens, vídeo, direção cinematográfica, renderização, storyboard e consistência visual.

A **NOVA** é a coordenadora dos agentes Montani e pode orientar fluxos que envolvam vários agentes dessa categoria.

### Mastplan

Reúne agentes de planejamento urbano, masterplan, urbanismo, visualização territorial e apresentação de empreendimentos.

### Engenharia

Reúne agentes de saneamento, hidráulica, infraestrutura, documentos gráficos e apresentações técnicas de engenharia.

O catálogo completo, com nomes, descrições, links, palavras-chave e regras de roteamento, está em `src/agents.js`.

## 4. Funcionalidades entregues na versão 1

- Painel responsivo com identidade SIZE.
- Catálogo pesquisável de agentes.
- Filtros por empresa, grupo e especialidade.
- Recomendação local do agente conforme a solicitação.
- Geração de prompt para encaminhamento ao agente escolhido.
- Abertura dos GPTs pelos respectivos links.
- Cadastro local de projetos.
- Gestão local de tarefas, riscos e decisões.
- Registro de metadados de arquivos.
- Lembretes enquanto a página está aberta.
- Histórico e perfil armazenados no navegador.
- Exportação de relatórios em JSON.
- Grafo visual da rede de conhecimento.
- Comando por voz quando o navegador oferece `SpeechRecognition`.
- Persistência por `localStorage`.

## 5. Arquitetura atual

O repositório tem duas camadas independentes.

### 5.1 Painel web (versão 1)

Aplicação web estática, sem compilação e sem dependências obrigatórias.

- `src/index.html`: estrutura da interface.
- `src/style.css`: identidade visual e responsividade.
- `src/agents.js`: catálogo e roteamento dos agentes.
- `src/app.js`: navegação, busca, filtros e interações.
- `src/operations.js`: projetos, tarefas, riscos, decisões, lembretes e relatórios.
- `AGENTS.md`: regras para outras IAs que trabalharem no projeto.
- `docs/ARCHITECTURE.md`: arquitetura e limitações.
- `docs/ROADMAP.md`: próximas fases.

### 5.2 Backend (fase 1 — adicionado em 15/09/2026)

Núcleo de inteligência do Fafa em Python (`backend/`), construído com Claude a partir das decisões de Daniel Broleis:

- Um único agente sobre a API da Anthropic serve todos os canais. Loop modelo → ferramenta → resultado, com limite de rodadas e persistência de cada passo.
- Ferramentas registradas por decorator (`@ferramenta`); o schema da API é gerado da assinatura Python.
- Memória em SQLite: histórico por sessão (`canal:usuário`) e fatos duráveis que entram no prompt de sistema.
- Ferramentas de geoprocessamento: conversão de coordenadas (SIRGAS 2000 / UTM 22S por padrão, EPSG:31982), azimute e distância, tabela completa de vértices (E/N, lat/lon, azimute GMS, confrontantes, perímetro, área), leitura de CSV. Sem `pyproj`, um motor interno (série de Krüger) cobre SIRGAS 2000 e WGS 84 com erro < 1 mm, validado por testes contra o pyproj.
- Canais: terminal (`fafa chat`), voz no desktop (`fafa voz`: Enter, fala, resposta falada) e WhatsApp via Meta Cloud API (envio, template, webhook, lista de números autorizados). Telegram e painel web ficam como possibilidades, não implementadas.
- Voz: transcrição pela OpenAI (`gpt-4o-mini-transcribe`); fala por ElevenLabs (preferido, pago), OpenAI (`gpt-4o-mini-tts`) ou SAPI do Windows (grátis), escolhidos pelas chaves no `.env`. Detalhes em `backend/docs/voz.md`.
- Especialistas (16/09/2026): as skills do Daniel no Claude (`auxiliar-escritorio`, `due360`, `site-topografia`, `budo-seedance-*` ×16) foram copiadas para `backend/especialistas/` e o Fafa as consulta sob demanda (`consultar_especialista`). O catálogo `src/agents.js` continua a fonte única dos GPTs; o Fafa só **indica** o GPT (`sugerir_agente_gpt`), não o executa. Detalhes em `backend/docs/especialistas.md`.
- Visão: `ver_tela` (captura de tela), `ver_arquivo` (imagem, PDF renderizado, texto) e `ver_camera` (webcam). A imagem vai ao modelo só no turno da captura; o histórico guarda um marcador textual. Detalhes em `backend/docs/visao.md`.
- Aplicativo: `Fafa.bat` na raiz e `backend/scripts/criar_atalho.ps1` criam o ícone **Fafa** na área de trabalho, que abre o modo voz. Ícone em `src/fafa.ico` (original, paleta SIZE) — o `src/fafa-logo.png` do repositório está corrompido (só as primeiras linhas decodificam) e precisa ser reenviado.
- Prioridade definida por Daniel: geoprocessamento primeiro, WhatsApp na sequência; geração de documentos SIZE e organização de arquivos/e-mail em segundo plano.
- Detalhes em `backend/README.md`, `backend/docs/arquitetura.md`, `backend/docs/roadmap.md` e `backend/docs/whatsapp.md`.

Integração painel ↔ backend (16/09/2026): `fafa web` serve o painel e expõe `/api/saude`, `/api/chat`, `/api/falar` (áudio WAV) e `/api/ouvir` (transcrição). `src/fafa-nucleo.js` detecta o núcleo e assume a **Conversa com Fafa** (texto, voz do Fafa e microfone via MediaRecorder), mantendo o comportamento local quando o backend não está rodando. `Fafa.bat` abre o painel em janela de aplicativo (Edge/Chrome `--app`). Projetos/tarefas continuam no `localStorage`; a migração para o SQLite é a próxima etapa.

## 6. Decisões confirmadas

1. O nome do produto é **Fafa**.
2. A identidade visual deve seguir a marca SIZE.
3. Os agentes devem permanecer separados entre Montani, Mastplan e Engenharia.
4. Todos os agentes com nomes de heróis pertencem à Montani.
5. A NOVA funciona como coordenadora do ecossistema Montani.
6. A integração com drives deve permanecer aberta no planejamento, porém desativada até a organização dos drives da empresa.
7. O código deve permanecer privado enquanto a empresa avalia sua evolução.
8. Outras IAs podem trabalhar no projeto desde que sigam o `AGENTS.md` e não inventem integrações ou acessos.
9. O backend é em Python, usa a API da Anthropic diretamente (sem framework de agentes) e adota SIRGAS 2000 / UTM 22S como sistema de coordenadas padrão.
10. O backend roda primeiro no desktop SIZE-LIDAR (terminal); o WhatsApp é o canal para avisos e comandos quando Daniel está fora do computador.
11. Este repositório (`size-projetos/Fafa`) é o principal e o único que outras IAs devem usar. O `size-projetos/size-fafa` foi criado por engano e está vazio.

## 7. Limitações conhecidas

- Os GPTs externos abrem por link; o painel ainda não os executa internamente.
- Os dados locais não sincronizam entre computadores ou usuários.
- Não existe banco de dados central nem autenticação corporativa própria.
- O registro de arquivos guarda metadados, não o conteúdo.
- A pesquisa em Google Drive e outras nuvens está desativada.
- Indicadores de CPU, RAM, rede e atividade exibidos por um navegador não devem ser tratados como telemetria real sem uma integração própria.
- Primeira conversa real com a API da Anthropic feita em 15/09/2026 (chave `fafa-size-lidar`, gravada só em `backend/.env` do SIZE-LIDAR). Os testes automatizados continuam usando um cliente simulado.
- O canal WhatsApp depende de conta Meta Business, número dedicado e URL pública para o webhook; fora da janela de 24 h só mensagens de template aprovado podem ser enviadas.
- O backend não lê DXF nem gera `.docx`; isso está no roadmap.
- A voz é push-to-talk (Enter); não há palavra de ativação nem interrupção da fala.
- `src/fafa-logo.png` está corrompido no repositório.

## 8. Próxima fase recomendada

Para o backend (ordem de Daniel): primeira conversa real com a chave da API; leitura de DXF; exportação `.xlsx`; conta Meta e túnel para o WhatsApp. Detalhes em `backend/docs/roadmap.md`.

Para o painel e a integração das camadas:

1. Organizar os drives e definir fontes autorizadas.
2. Definir usuários, papéis e permissões.
3. Implementar autenticação corporativa.
4. Criar backend e banco de dados central.
5. Integrar a busca segura em nuvem usando OAuth.
6. Integrar agentes e modelos por APIs compatíveis.
7. Adicionar auditoria, monitoramento e recuperação de dados.
8. Criar testes automatizados para roteamento e fluxos críticos.

## 9. Links de referência

- Produto publicado: https://fafa-size-engenharia.projetos334718.chatgpt.site
- Repositório principal: https://github.com/size-projetos/Fafa (tornado público por Daniel em 15/09/2026)
- Site institucional: https://www.sizeengenhariaambiental.com.br/

## 10. Instrução para a próxima IA

Antes de alterar o produto, leia `AGENTS.md`, este documento, `docs/ARCHITECTURE.md` e `docs/ROADMAP.md`. Para mexer no backend, leia também `backend/README.md` e `backend/docs/arquitetura.md` e rode `pytest` antes e depois. Preserve as decisões confirmadas, não conecte os drives sem autorização expressa e mantenha segredos fora do código-fonte.

