# Roadmap do backend

Ordem definida por Daniel em 15/09/2026: geoprocessamento primeiro, WhatsApp na
sequência; documentos e organização de arquivos ficam em segundo plano.

## Fase 1 — Geoprocessamento no terminal · *em andamento*

- [x] Núcleo do agente, registro de ferramentas, memória SQLite
- [x] Conversão de coordenadas (pyproj + motor interno validado)
- [x] Azimute e distância
- [x] Tabela de vértices com lat/lon, confrontantes, perímetro, área
- [x] Leitura de CSV de coordenadas
- [x] CLI `fafa` no desktop SIZE-LIDAR
- [ ] Testar ponta a ponta com a chave da API (primeira conversa real)
- [ ] Ler vértices direto de DXF (polilinhas fechadas) — `ezdxf`
- [ ] Exportar a tabela em `.xlsx` no modelo SIZE
- [ ] Integrar com os scripts existentes do `C:\geo312` (nuvem de pontos, LiDAR)
- [ ] Memorial descritivo em texto (parágrafo por segmento) a partir da tabela

## Fase 1b — Voz e atalho no desktop · *entregue em 15/09/2026*

- [x] `fafa voz`: Enter → fala → transcrição (OpenAI) → resposta falada (ElevenLabs / OpenAI / Windows)
- [x] Detector de fim de fala por silêncio; texto digitado como alternativa
- [x] `Fafa.bat` + `criar_atalho.ps1` + ícone: Fafa abre como aplicativo pelo ícone na área de trabalho
- [ ] Palavra de ativação ("Fafa, …") e tecla de atalho global
- [ ] Interromper a fala ao começar a falar
- [ ] Voz do Fafa escolhida (ElevenLabs) e chaves configuradas no SIZE-LIDAR

## Fase 1c — Visão · *entregue em 15/09/2026*

- [x] `ver_tela`, `ver_arquivo` (imagem, PDF, texto), `ver_camera`
- [x] Imagem enviada só no turno da captura; histórico guarda marcador
- [ ] Ler DXF como desenho (renderizar polilinhas) além de extrair vértices
- [ ] Receber foto pelo WhatsApp e responder (entra com a fase 2)

## Fase 2 — WhatsApp · *próxima*

- [x] Envio de texto e template (Meta Cloud API)
- [x] Webhook FastAPI com verificação e lista de números autorizados
- [x] `fafa notificar` para avisos "terminei"
- [ ] Conta Meta Business + número dedicado do Fafa (ver `docs/whatsapp.md`)
- [ ] Túnel público para o webhook no desktop (cloudflared) ou relay pequeno na nuvem
- [ ] Template aprovado para avisos fora da janela de 24 h
- [ ] Receber arquivos (CSV/DXF) pelo WhatsApp e processar
- [ ] Tarefas longas em segundo plano com aviso ao concluir

## Fase 3 — Documentos SIZE · *segundo plano*

- [ ] Memorial descritivo em `.docx` no padrão `SIZE_MODELO-MEMORIAL-TECNICO`
- [ ] Laudos e relatórios a partir de dados estruturados
- [ ] Base de conhecimento normativo (CFT 089/159, CORSAN, SIGEF, INCRA)

## Fase 4 — Arquivos e e-mail · *segundo plano*

- [ ] Organização dos Drives (SIZE Projetos, Obras em Execução)
- [ ] Triagem de e-mail e avisos de prazo
- [ ] Arquivamento automático de documentos de obra

## Integração com o painel web (v1)

- [x] `fafa web`: serve o painel + `/api/chat`, `/api/falar`, `/api/ouvir`, `/api/saude` (16/09)
- [x] `fafa-nucleo.js`: Conversa com Fafa ligada ao núcleo, com voz e microfone; reserva local
- [x] `Fafa.bat` abre o painel como aplicativo
- [ ] Painel mostra tabelas de vértices e imagens (ver_tela) formatadas, não só texto
- [ ] Projetos/tarefas do painel deixam o `localStorage` e passam para o SQLite do backend
- [ ] Encaminhar ao GPT certo a partir da conversa (o Fafa sugere o agente do catálogo)

## Ideias sem fase

- Canal Telegram (trivial com a interface `Canal`; polling, sem URL pública)
- Painel web local para ver histórico, tabelas e mapas
- Modo "voz" no desktop
