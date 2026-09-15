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

A versão 1 é uma aplicação web estática, sem compilação e sem dependências obrigatórias.

- `src/index.html`: estrutura da interface.
- `src/style.css`: identidade visual e responsividade.
- `src/agents.js`: catálogo e roteamento dos agentes.
- `src/app.js`: navegação, busca, filtros e interações.
- `src/operations.js`: projetos, tarefas, riscos, decisões, lembretes e relatórios.
- `AGENTS.md`: regras para outras IAs que trabalharem no projeto.
- `docs/ARCHITECTURE.md`: arquitetura e limitações.
- `docs/ROADMAP.md`: próximas fases.

## 6. Decisões confirmadas

1. O nome do produto é **Fafa**.
2. A identidade visual deve seguir a marca SIZE.
3. Os agentes devem permanecer separados entre Montani, Mastplan e Engenharia.
4. Todos os agentes com nomes de heróis pertencem à Montani.
5. A NOVA funciona como coordenadora do ecossistema Montani.
6. A integração com drives deve permanecer aberta no planejamento, porém desativada até a organização dos drives da empresa.
7. O código deve permanecer privado enquanto a empresa avalia sua evolução.
8. Outras IAs podem trabalhar no projeto desde que sigam o `AGENTS.md` e não inventem integrações ou acessos.

## 7. Limitações conhecidas

- Os GPTs externos abrem por link; o painel ainda não os executa internamente.
- Os dados locais não sincronizam entre computadores ou usuários.
- Não existe banco de dados central nem autenticação corporativa própria.
- O registro de arquivos guarda metadados, não o conteúdo.
- A pesquisa em Google Drive e outras nuvens está desativada.
- Indicadores de CPU, RAM, rede e atividade exibidos por um navegador não devem ser tratados como telemetria real sem uma integração própria.

## 8. Próxima fase recomendada

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
- Repositório privado principal: https://github.com/size-projetos/Fafa
- Site institucional: https://www.sizeengenhariaambiental.com.br/

## 10. Instrução para a próxima IA

Antes de alterar o produto, leia `AGENTS.md`, este documento, `docs/ARCHITECTURE.md` e `docs/ROADMAP.md`. Preserve as decisões confirmadas, não conecte os drives sem autorização expressa e mantenha segredos fora do código-fonte.

