# Visão — o Fafa enxergando

O cérebro do Fafa (Claude) lê imagens nativamente. As ferramentas abaixo são
os "olhos": capturam e entregam a imagem ao modelo no mesmo turno.

| Ferramenta | O que faz | Como pedir |
|---|---|---|
| `ver_tela` | Captura a tela (todos os monitores, ou um específico) | "olha minha tela", "o que é isso aqui?" |
| `ver_arquivo` | Abre imagem (foto, croqui, planta), PDF (até 4 páginas por vez, renderizadas) ou texto (CSV, TXT, JSON…) | "abre C:\...\planta.pdf página 2", "lê esse CSV" |
| `ver_camera` | Foto pela webcam (índice 0 = padrão) | "tira uma foto", "olha pela câmera" |

Instalação: `pip install -e ".[visao]"` (já vem no `[all]`): Pillow, OpenCV
(headless), PyMuPDF e mss.

## Custo e memória

- Imagens são reduzidas para no máximo 1568 px no maior lado e comprimidas em
  JPEG (~100–300 KB). Uma tela cheia custa ≈ 1.500 tokens de entrada — centavos.
- **A imagem só é enviada no turno em que foi capturada.** No histórico da
  sessão fica um marcador (`[imagem: tela completa, 1568x882, 210 KB]`), então
  os turnos seguintes não pagam de novo por ela. Se o usuário perguntar algo
  novo sobre a mesma tela, o Fafa captura de novo.

## Limites

- `ver_tela` no Windows captura o que está visível; janelas minimizadas não.
- PDF: 110 dpi por página, suficiente para texto e plantas em A3; para detalhe
  fino peça a página específica.
- `ver_camera` usa DirectShow; se outra aplicação estiver com a câmera, falha
  com mensagem clara.
- DXF/DWG ainda não são lidos como desenho — abra no CAD e peça `ver_tela`, ou
  aguarde a fase de leitura de DXF do roadmap.
