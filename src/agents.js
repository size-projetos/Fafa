const agents = [
  {
    "id": "ferro",
    "name": "Homem de Ferro",
    "fullName": "Homem de Ferro | Print to Render INTERIORES",
    "description": "Render de interiores",
    "detail": "print de ambiente interno para render.",
    "url": "https://chatgpt.com/g/g-69639775e9448191b9eded93f8d33ce1-homem-de-ferro-print-to-render",
    "group": "Arquitetura",
    "input": "Um print do ambiente interno e o estilo desejado.",
    "initials": "HF",
    "collections": [
      "Montani"
    ]
  },
  {
    "id": "cavaleiro",
    "name": "Cavaleiro Negro",
    "fullName": "Cavaleiro Negro | Print to Render Exteriores",
    "description": "Render de exteriores",
    "detail": "print de exterior para render.",
    "url": "https://chatgpt.com/g/g-6966926850b081918a0f7a7ecb97960e-cavaleiro-negro-print-to-render-exterior",
    "group": "Arquitetura",
    "input": "Um print da fachada ou cena externa e referências.",
    "initials": "CN",
    "collections": [
      "Montani"
    ]
  },
  {
    "id": "visao",
    "name": "VISÃO",
    "fullName": "VISÃO | Planta Humanizada",
    "description": "Planta humanizada",
    "detail": "humanização de plantas.",
    "url": "https://chatgpt.com/g/g-6967f776ef8881919a05f1a7c8a4d078-visao-i-planta-humanizada",
    "group": "Arquitetura",
    "input": "A planta legível, com escala ou medidas quando disponíveis.",
    "initials": "V",
    "collections": [
      "Montani"
    ]
  },
  {
    "id": "stan",
    "name": "Stan Lee",
    "fullName": "Stan Lee | Detalhamento por Imagem",
    "description": "Detalhamento por imagem",
    "detail": "detalhamento a partir de imagens; confirmar o tipo de entrega.",
    "url": "https://chatgpt.com/g/g-695fe5829d14819193fc0f0570a7ff03-stan-lee-detalhamento-por-imagem",
    "group": "Arquitetura",
    "input": "A imagem e o tipo de detalhamento que você precisa.",
    "initials": "SL",
    "collections": [
      "Montani"
    ]
  },
  {
    "id": "feiticeiro",
    "name": "Feiticeiro Escarlate",
    "fullName": "Feiticeiro Escarlate | Estações do ano exteriores",
    "description": "Estações do ano",
    "detail": "variações sazonais em cenas externas.",
    "url": "https://chatgpt.com/g/g-68bf73cdb01c81919fda8f3cea9481d7-feiticeiro-escarlate-estacoes-do-ano-exteriores",
    "group": "Arquitetura",
    "input": "A imagem externa e as estações desejadas.",
    "initials": "FE",
    "collections": [
      "Montani"
    ]
  },
  {
    "id": "capitao",
    "name": "Capitão América",
    "fullName": "Capitão América | Cria Prompt para gerar imagens",
    "description": "Prompts para imagens",
    "detail": "transformar ideias em prompts de imagem.",
    "url": "https://chatgpt.com/g/g-68c03b4d93d88191ba7c5b0053717c0e-capitao-america-cria-prompt-para-gerar-imagens",
    "group": "Imagem",
    "input": "Sua ideia, o uso da imagem e o estilo visual.",
    "initials": "CA",
    "collections": [
      "Montani"
    ]
  },
  {
    "id": "aranha",
    "name": "Homem Aranha",
    "fullName": "Homem Aranha | Assistente de Imagem IA",
    "description": "Assistente de imagem IA",
    "detail": "assistência geral com imagens IA; confirmar escopo quando necessário.",
    "url": "https://chatgpt.com/g/g-68c03b5a69588191aa7bb4a489450114-homem-aranha-assistente-de-imagem-ia",
    "group": "Imagem",
    "input": "Sua dúvida, objetivo e imagem de referência, se houver.",
    "initials": "HA",
    "collections": [
      "Montani"
    ]
  },
  {
    "id": "gaviao",
    "name": "Gavião Arqueiro",
    "fullName": "Gavião Arqueiro | Editor de Imagem IA (FLUX/NANO)",
    "description": "Edição de imagem",
    "detail": "edição orientada de imagens.",
    "url": "https://chatgpt.com/g/g-68c03b54e2d88191ad4cf26943349615-gaviao-arqueiro-editor-de-imagem-ia-flux-nano",
    "group": "Imagem",
    "input": "A imagem original e a lista do que deve mudar.",
    "initials": "GA",
    "collections": [
      "Montani"
    ]
  },
  {
    "id": "pantera",
    "name": "Pantera",
    "fullName": "Pantera | Agente de Ensaios Fotográficos",
    "description": "Ensaios fotográficos",
    "detail": "ensaios fotográficos.",
    "url": "https://chatgpt.com/g/g-68c41f25c7708191b673b39cffbce853-pantera-i-agente-de-ensaios-fotograficos",
    "group": "Imagem",
    "input": "O tema, as referências e o objetivo do ensaio.",
    "initials": "P",
    "collections": [
      "Montani"
    ]
  },
  {
    "id": "loki",
    "name": "LOKI",
    "fullName": "LOKI | Consistência de imagens",
    "description": "Consistência de imagens",
    "detail": "consistência entre imagens.",
    "url": "https://chatgpt.com/g/g-69bdd084dd788191abb7e6eacfc07c4f-loki-consistencia-de-imagens",
    "group": "Imagem",
    "input": "As imagens de referência e o que deve permanecer igual.",
    "initials": "L",
    "collections": [
      "Montani"
    ]
  },
  {
    "id": "flash",
    "name": "Flash",
    "fullName": "Flash | Timelapse de Construção",
    "description": "Timelapse de construção",
    "detail": "timelapse de construção.",
    "url": "https://chatgpt.com/g/g-69162ef7b6b88191a6c87be4ede5f5b0-flash-timelapse-de-construcao",
    "group": "Cinema",
    "input": "As imagens ou descrição da obra e a sequência de construção.",
    "initials": "F",
    "collections": [
      "Montani"
    ]
  },
  {
    "id": "thor",
    "name": "Thor",
    "fullName": "Thor | Assistente VEO 3",
    "description": "Vídeo com VEO 3",
    "detail": "assistência para trabalhar com VEO 3.",
    "url": "https://chatgpt.com/g/g-68c03b50e1448191a1cbaaeef552a740-thor-assistente-veo-3",
    "group": "Cinema",
    "input": "A descrição da cena, duração e formato desejados.",
    "initials": "T",
    "collections": [
      "Montani"
    ]
  },
  {
    "id": "estranho",
    "name": "Doutor Estranho",
    "fullName": "Doutor Estranho | Assistente JSON to VEO 3",
    "description": "JSON para VEO 3",
    "detail": "pedidos estruturados em JSON para VEO 3.",
    "url": "https://chatgpt.com/g/g-68c03b4ac59881919c30efc36d0db29a-doutor-estranho-assistente-json-to-veo-3",
    "group": "Cinema",
    "input": "A descrição da cena e a estrutura JSON exigida, se houver.",
    "initials": "DE",
    "collections": [
      "Montani"
    ]
  },
  {
    "id": "formiga",
    "name": "Homem Formiga",
    "fullName": "Homem Formiga | Expansão de cenas cinematográficas",
    "description": "Expansão de cenas",
    "detail": "desenvolvimento ou expansão de cenas; confirmar o sentido de expansão desejado.",
    "url": "https://chatgpt.com/g/g-69162e73c6a48191a8ec69fa5327ff0a-homem-formiga-expansao-de-cenas-cinematograficas",
    "group": "Cinema",
    "input": "A cena inicial e como você quer desenvolvê-la.",
    "initials": "HF",
    "collections": [
      "Montani"
    ]
  },
  {
    "id": "starlord",
    "name": "Starlord",
    "fullName": "Starlord | Diretor de filmes IA",
    "description": "Direção de filmes IA",
    "detail": "direção de filmes com IA.",
    "url": "https://chatgpt.com/g/g-69162ed1c7e081919ae2ef2562d6e80b-starlord-diretor-de-filmes-ia",
    "group": "Cinema",
    "input": "O tema do filme, público e duração pretendida.",
    "initials": "S",
    "collections": [
      "Montani"
    ]
  },
  {
    "id": "thanos",
    "name": "Thanos",
    "fullName": "Thanos | Storyboard com Storytelling",
    "description": "Storyboard e narrativa",
    "detail": "narrativa e storyboard.",
    "url": "https://chatgpt.com/g/g-68caf8db4f888191a9fc26064a15be8b-thanos-i-storyboard-com-storytellingh",
    "group": "Cinema",
    "input": "A história ou ideia e o número de cenas desejado.",
    "initials": "T",
    "collections": [
      "Montani"
    ]
  },
  {
    "id": "nick",
    "name": "Nick Fury",
    "fullName": "Nick Fury | Diretor Cinematográfico",
    "description": "Direção cinematográfica",
    "detail": "direção cinematográfica.",
    "url": "https://chatgpt.com/g/g-69a86bd2060c8191b23e6c83d0b059e2-nick-fury-i-diretor-cinematografico",
    "group": "Cinema",
    "input": "O roteiro ou cena e o tipo de direção desejado.",
    "initials": "NF",
    "collections": [
      "Montani"
    ]
  },
  {
    "id": "saneargpt",
    "name": "SanearGPT",
    "fullName": "SanearGPT",
    "description": "Assistência em saneamento",
    "detail": "orientação geral sobre saneamento.",
    "url": "https://chatgpt.com/g/g-67d92d6f6e5c8191b69dbed7b1533f29-saneargpt",
    "group": "Arquitetura",
    "input": "O contexto do sistema de saneamento, dados disponíveis e resultado técnico esperado.",
    "initials": "SG",
    "collections": [
      "Engenharia"
    ]
  },
  {
    "id": "enghydro",
    "name": "EngHydro",
    "fullName": "EngHydro",
    "description": "Engenharia hidráulica",
    "detail": "assistência em temas de hidráulica.",
    "url": "https://chatgpt.com/g/g-67d06e1c49008191a5947d1d0352e44c-enghydro",
    "group": "Arquitetura",
    "input": "Os dados hidráulicos, plantas, premissas e objetivo do estudo.",
    "initials": "EH",
    "collections": [
      "Engenharia"
    ]
  },
  {
    "id": "eng-saneamento",
    "name": "Eng. de Saneamento",
    "fullName": "Eng. de Saneamento",
    "description": "Engenharia de saneamento",
    "detail": "apoio técnico em engenharia de saneamento.",
    "url": "https://chatgpt.com/g/g-68f6a87e42288191a9ae0aa2d9a1c24c-eng-de-saneamento",
    "group": "Arquitetura",
    "input": "O problema de saneamento, dados de campo, normas aplicáveis e entrega esperada.",
    "initials": "ES",
    "collections": [
      "Engenharia"
    ]
  },
  {
    "id": "infra-vision",
    "name": "Infra Vision Studio",
    "fullName": "Infra Vision Studio",
    "description": "Visualização de infraestrutura",
    "detail": "produção visual voltada à infraestrutura.",
    "url": "https://chatgpt.com/g/g-69fdc2f75d688191bcc545f3519a9d60-infra-vision-studio",
    "group": "Imagem",
    "input": "A planta, modelo, imagem ou projeto de infraestrutura e o resultado visual desejado.",
    "initials": "IV",
    "collections": [
      "Engenharia"
    ]
  },
  {
    "id": "docs-graficos-eng",
    "name": "Documentos Gráficos",
    "fullName": "Especialista em Documentos Gráficos de Engenharia",
    "description": "Documentos gráficos de engenharia",
    "detail": "organização e apresentação gráfica de documentos técnicos.",
    "url": "https://chatgpt.com/g/g-69eb580d06848191a7ac23115ec68585-especialista-em-documentos-graficos-de-engenharia",
    "group": "Imagem",
    "input": "O documento técnico, dados e padrão gráfico esperado.",
    "initials": "DG",
    "collections": [
      "Engenharia"
    ]
  },
  {
    "id": "apresentacao-eng",
    "name": "Apresentação Técnica",
    "fullName": "Especialista em Apresentação Técnica de Engenharia",
    "description": "Apresentações técnicas de engenharia",
    "detail": "estruturação visual de apresentações técnicas.",
    "url": "https://chatgpt.com/g/g-69f32f7ef02c8191b108ec55725a43e4-especialista-em-apresentacao-tecnica-de-engenharia",
    "group": "Imagem",
    "input": "O conteúdo técnico, público, objetivo e formato da apresentação.",
    "initials": "AT",
    "collections": [
      "Engenharia"
    ]
  },
  {
    "id": "diretor-criativo",
    "name": "Diretor Criativo",
    "fullName": "Diretor Criativo",
    "description": "Direção criativa",
    "detail": "direção visual e conceitual.",
    "url": "https://chatgpt.com/g/g-69f39e21ed0c81918f5344d866f07fee-diretor-criativo",
    "group": "Imagem",
    "input": "O objetivo, público, materiais e referências visuais do projeto.",
    "initials": "DC",
    "collections": [
      "Mastplan"
    ]
  },
  {
    "id": "fotografo-ia",
    "name": "Fotógrafo IA",
    "fullName": "Fotógrafo IA by @azev300",
    "description": "Fotografia e direção de imagem",
    "detail": "produção e orientação fotográfica com IA.",
    "url": "https://chatgpt.com/g/g-687e901644a48191a9827ad670dce45a-fotografo-ia-by-azev300",
    "group": "Imagem",
    "input": "O tema, local, referências, enquadramento e finalidade das imagens.",
    "initials": "FI",
    "collections": [
      "Mastplan"
    ]
  },
  {
    "id": "urban-planning",
    "name": "Urban Planning",
    "fullName": "Urban Planning",
    "description": "Planejamento urbano",
    "detail": "apoio a estudos e propostas de planejamento urbano.",
    "url": "https://chatgpt.com/g/g-ajx0lMi3v-urban-planning/c/6a452af3-0108-83e9-8eed-442c8f0271b8",
    "group": "Arquitetura",
    "input": "A área de estudo, condicionantes, programa e objetivo urbanístico.",
    "initials": "UP",
    "collections": [
      "Mastplan"
    ]
  },
  {
    "id": "master-plan",
    "name": "Master Plan",
    "fullName": "Master Plan",
    "description": "Desenvolvimento de masterplans",
    "detail": "estruturação e análise de masterplans.",
    "url": "https://chatgpt.com/g/g-jNPkEn8HM-master-plan",
    "group": "Arquitetura",
    "input": "A área, levantamento, programa, premissas e resultado esperado para o masterplan.",
    "initials": "MP",
    "collections": [
      "Mastplan"
    ]
  },
  {
    "id": "infra-vision-2",
    "name": "Infra Vision Studio 2.0",
    "fullName": "Infra Vision Studio 2.0",
    "description": "Visualização de masterplan e infraestrutura",
    "detail": "visualização avançada de projetos territoriais e de infraestrutura.",
    "url": "https://chatgpt.com/g/g-6a4559ab5a3c819180db02ffff8b4222-infra-vision-studio-2-0",
    "group": "Imagem",
    "input": "O masterplan, planta ou imagem-base e o resultado visual esperado.",
    "initials": "IV2",
    "collections": [
      "Mastplan"
    ]
  },
  {
    "id": "nova-montani",
    "name": "NOVA",
    "fullName": "NOVA | Agente de Agentes Montani",
    "description": "Coordena os 17 agentes Montani",
    "detail": "escolha e encadeamento dos agentes Montani.",
    "url": "https://chatgpt.com/g/g-6a3ac7cdc8688191942e9a09a507cebc-nova-agente-de-agentes-montani",
    "group": "Coordenação",
    "input": "Seu objetivo, os materiais disponíveis e o resultado final desejado. A NOVA indicará quais agentes Montani usar e em que ordem.",
    "initials": "NV",
    "collections": [
      "Montani"
    ],
    "coordinator": true
  }
];
