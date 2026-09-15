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

- [ ] Endpoint HTTP `/chat` no backend para o painel conversar com o Fafa
- [ ] Painel mostra tabelas de vértices e resultados geo gerados pelo backend
- [ ] Projetos/tarefas do painel deixam o `localStorage` e passam para o SQLite do backend

## Ideias sem fase

- Canal Telegram (trivial com a interface `Canal`; polling, sem URL pública)
- Painel web local para ver histórico, tabelas e mapas
- Modo "voz" no desktop
