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
- `backend/src/fafa/`: agente, registro de ferramentas, memória, ferramentas geo e canais.
- `backend/docs/`: arquitetura, roadmap, WhatsApp e voz do backend.
- `Fafa.bat`: lançador do desktop (ativa o venv e abre `fafa voz`).
- `src/fafa.ico`: ícone do atalho.
- `docs/ARCHITECTURE.md`: arquitetura e limites atuais.
- `docs/ROADMAP.md`: próximas integrações.
- `AGENTS.md`: orientação para agentes de IA que alterarem o projeto.

## Estado atual

O painel (versão 1) funciona como aplicação estática e armazena os dados no `localStorage` do navegador. O backend (fase 1) roda no terminal do desktop SIZE-LIDAR com as ferramentas de geoprocessamento; o canal WhatsApp está implementado e aguarda a configuração da conta Meta. Painel e backend ainda não se comunicam — essa integração está no roadmap. A integração com drives está deliberadamente pausada até a organização das fontes de arquivos.

## Privacidade e propriedade

Projeto privado da SIZE Engenharia. Marcas, logotipos e materiais visuais pertencem aos respectivos titulares. Não publique nem redistribua sem autorização.
