# Voz — o Fafa ouvindo e falando

`fafa voz` abre o Fafa em modo conversa: **Enter** para falar, ele transcreve,
responde no agente e **fala a resposta** (o texto também aparece na tela).
Digitar em vez de apertar Enter envia o texto direto. O atalho **Fafa** na área
de trabalho abre exatamente isso.

## Motores

| Papel | Motor | Qualidade pt-BR | Custo | Variáveis |
|---|---|---|---|---|
| Falar (TTS) | **ElevenLabs** `eleven_flash_v2_5` | a melhor, voz natural | pago — faixa grátis ~10 min/mês; Starter US$ 5/mês ≈ 30 min | `ELEVENLABS_API_KEY`, `ELEVENLABS_VOICE_ID` |
| Falar (TTS) | **OpenAI** `gpt-4o-mini-tts` | boa; vozes `marin`/`cedar` recomendadas | ≈ US$ 0,015/min | `OPENAI_API_KEY` |
| Falar (TTS) | **Windows** (SAPI, pyttsx3) | robótica | grátis, offline | — |
| Ouvir (STT) | **OpenAI** `gpt-4o-mini-transcribe` | excelente em pt-BR | ≈ US$ 0,003/min | `OPENAI_API_KEY` |

`FAFA_TTS=auto` (padrão) escolhe ElevenLabs → OpenAI → Windows conforme as
chaves preenchidas no `.env`. `FAFA_STT=auto` usa OpenAI se houver chave;
senão o Fafa só aceita texto digitado (mas ainda fala).

**Recomendação para começar:** só a `OPENAI_API_KEY` já dá ouvido + voz decente
com uma conta. Se a voz do Fafa importar (e para um "Jarvis" importa), adicione
o ElevenLabs para falar e deixe a OpenAI só ouvindo — é a combinação com melhor
custo-benefício.

## Configurar

1. Instale o extra de voz (já vem no `[all]`): `pip install -e ".[voz]"`.
2. Preencha no `backend\.env`:
   ```
   OPENAI_API_KEY=sk-...
   ELEVENLABS_API_KEY=...        # opcional
   ELEVENLABS_VOICE_ID=...       # opcional; em elevenlabs.io → Voices, escolha uma voz pt-BR e copie o ID
   ```
3. Confira os dispositivos: `fafa audio` (lista microfones e saídas; o padrão do
   Windows é o usado).
4. Rode `fafa voz`. Fale depois do Enter; ele para de gravar após 1,2 s de
   silêncio. Se cortar cedo ou tarde, ajuste `FAFA_VOZ_SILENCIO_S`; se não
   detectar a fala (barra não sobe), abaixe `FAFA_VOZ_LIMIAR` (0,012 padrão).

## Atalho na área de trabalho

```powershell
powershell -ExecutionPolicy Bypass -File backend\scripts\criar_atalho.ps1
```

Cria **Fafa.lnk** na área de trabalho apontando para `Fafa.bat` (raiz do repo),
que ativa o venv, corrige a codificação do console e abre `fafa voz`. Sem
`.env` ele avisa e para.

## Como funciona

- Gravação a 16 kHz, mono, em blocos de 50 ms. Um detector por RMS decide
  quando a fala começou e quando acabou (`fafa.voz.audio.DetectorDeFala`).
- A transcrição vai por HTTP como WAV. O prompt da transcrição carrega o
  vocabulário técnico (UTM, SIRGAS, azimute…) para reduzir erros.
- A resposta volta como PCM 24 kHz e toca direto; nenhum decodificador MP3.
- No canal `voz`, o prompt de sistema pede respostas de 1–3 frases sem
  markdown; `limpar_para_fala` remove o que sobrar antes de sintetizar.
- Falha no áudio nunca derruba a conversa: o texto sempre aparece na tela.

## Limites atuais

- Push-to-talk por Enter, sem palavra de ativação ("Fafa, …") e sem tecla de
  atalho global — próximos passos naturais.
- Sem interrupção: enquanto fala, não ouve.
- Janela é o console do Windows; a interface gráfica é a integração com o
  painel web, no roadmap.
