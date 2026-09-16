# Topografia, RPAS/Drones e LiDAR — Crib Sheet

> Fonte: EBPOS-URB-VOL2 (Topografia, utilização de RPAS/Drones e Laser Scanner/LIDAR
> para Levantamento da Realidade). Este material é predominantemente conceitual
> (não traz tabelas normativas de precisão/classe); use em conjunto com a NBR 13133
> e as especificações do fabricante do equipamento (DJI Matrice 350 RTK + Zenmuse L2)
> já referenciadas no SKILL.md principal.

## 1. Sensoriamento remoto — tipos de sensores

- **Sensores passivos**: captam radiação refletida/emitida naturalmente (câmeras
  RGB, multiespectrais, hiperespectrais, térmicas).
- **Sensores ativos**: emitem seu próprio sinal e medem o retorno (LiDAR, RADAR).
- Aplicações citadas: agricultura de precisão, planejamento urbano, arqueologia,
  geologia.

## 2. Fotogrametria — fluxo conceitual

1. Aquisição de imagens sobrepostas (aerofotogrametria com RPAS).
2. Processamento (aerotriangulação, geração de nuvem de pontos densa).
3. Geração de ortomosaico, MDS/MDT e modelo 3D.
4. Exportação para uso em BIM/CAD.

## 3. Códigos EPSG mais citados

| Código EPSG | Sistema |
|---|---|
| 4326 | WGS84 geográfico (lat/long) |
| 3857 | Web Mercator (uso em visualização web, não para medições de precisão) |
| 32633 | UTM zona 33N (exemplo de projeção UTM — para o litoral norte do RS, usar a zona 22S / SIRGAS 2000, conforme padrão já fixado no SKILL.md principal) |

Usar sempre o EPSG correspondente a SIRGAS 2000 / UTM 22S para os projetos da SIZE
(não usar os códigos de exemplo acima, que são ilustrativos do material-fonte).

## 4. GNSS e Laser Scanner (LiDAR)

- Levantamento GNSS RTK depende de correções diferenciais (base local ou rede
  RTK/NTRIP) para atingir precisão centimétrica em tempo real.
- Laser Scanner terrestre e LiDAR aerotransportado geram nuvens de pontos
  tridimensionais densas, usadas para modelagem de superfícies (MDT) e elementos
  urbanos (fiação, postes, edificações).
- O material não especifica classes formais de precisão GNSS (estático/RTK/PPK) —
  seguir a NBR 13133 e o memorial de especificação de cada equipamento para essa
  definição.

## 5. Regularização de voo (drones)

O material trata do tema de forma genérica (regulamentação aeronáutica, papel do
piloto, planejamento de rota). Para os requisitos brasileiros específicos
(ANAC/DECEA — SARPAS, RBAC-E nº 94, classes de aeronave não tripulada por peso),
consultar diretamente a legislação vigente, pois não constam números normativos
neste material.

## 6. Formatos de entrega mencionados

Nuvem de pontos, ortomosaico, modelo digital de superfície/terreno, integração com
softwares BIM (Civil 3D) para geração de superfície TIN a partir do levantamento.

## 7. Boas práticas de fluxo de trabalho

- Validar a qualidade dos pontos de controle em campo antes de aceitar o
  processamento fotogramétrico.
- Verificar consistência do sistema de referência (datum/projeção) em todas as
  etapas, do voo à entrega final em CAD/BIM.
- Documentar o EPSG/datum usado em todo entregável para evitar erros de
  interoperabilidade entre softwares.
