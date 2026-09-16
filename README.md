# Fafa | SIZE Engenharia

Central operacional de IA da SIZE Engenharia, em duas camadas:

- **Painel web** (`src/`): organiza agentes especializados, recomenda o agente adequado para cada solicitação e mantém projetos, tarefas, riscos, decisões e registros de arquivos no navegador.
- **Backend** (`backend/`): o núcleo de inteligência do Fafa — um agente em Python sobre a API da Anthropic, com ferramentas de topografia e geoprocessamento, memória persistente e canais de conversa (terminal e WhatsApp). Documentação própria em [`backend/README.md`](backend/README.md).

## Executar localmente

Sirva a pasta `src` com qualquer servidor HTTP estático. Exemplo:

```bash
python -m http.server 4173 --directory src
```

Abra `http://127.0.0.1:4173`.

## Executar o backend

```powershell
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -e ".[all,dev]"
copy .env.example .env      # preencher ANTHROPIC_API_KEY
fafa                        # conversa no terminal
fafa voz                    # conversa por voz (ver backend/docs/voz.md)
pytest                      # testes
```

Para abrir o Fafa como aplicativo, pelo ícone na área de trabalho:

```powershell
powershell -ExecutionPolicy Bypass -File backend\scripts\criar_atalho.ps1
```

## Estrutura

- `src/index.html`: interface principal.
- `src/style.css`: identidade visual e responsividade.
- `src/agents.js`: catálogo e roteamento dos agentes.
- `src/app.js`: navegação e interações principais.
- `src/operations.js`: projetos, tarefas, riscos, decisões e persistência local.
- `src/fafa-nucleo.js`: liga a Conversa com Fafa ao backend quando ele está no ar (chat, voz, microfone).
- `backend/src/fafa/`: agente, registro de ferramentas, memória, ferramentas geo e canais.
- `backend/docs/`: arquitetura, roadmap, WhatsApp e voz do backend.
- `Fafa.bat`: lançador do desktop — sobe o núcleo e abre o painel como aplicativo (`fafa web`).
- `Fafa-Voz.bat`: alternativa no terminal, por voz (`fafa voz`).
- `src/fafa.ico`: ícone do atalho.
- `docs/ARCHITECTURE.md`: arquitetura e limites atuais.
- `docs/ROADMAP.md`: próximas integrações.
- `AGENTS.md`: orientação para agentes de IA que alterarem o projeto.

## Estado atual

O painel (versão 1) continua funcionando sozinho como aplicação estática, com dados no `localStorage`. Quando o backend está rodando (`fafa web`, ou o ícone **Fafa** no desktop), ele serve o painel em `http://127.0.0.1:8000` e a seção **Conversa com Fafa** passa a falar com o núcleo Python — cálculo, visão, memória, voz e microfone — via `src/fafa-nucleo.js`; sem o backend, a conversa volta ao comportamento local. Projetos, tarefas e riscos seguem no `localStorage` (próxima etapa: migrar para o SQLite do backend). O canal WhatsApp está implementado e aguarda a configuração da conta Meta. A integração com drives está deliberadamente pausada até a organização das fontes de arquivos.

## Privacidade e propriedade

Projeto privado da SIZE Engenharia. Marcas, logotipos e materiais visuais pertencem aos respectivos titulares. Não publique nem redistribua sem autorização.
