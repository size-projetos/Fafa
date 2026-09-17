# WhatsApp — configuração

O Fafa usa a **Meta Cloud API** (API oficial do WhatsApp Business). Sem risco
de bloqueio do número, mas com burocracia inicial. Bibliotecas não oficiais
(Baileys, whatsapp-web.js) funcionam sem nada disso, porém podem derrubar o
número — não vale para um número da empresa.

## 1. Conta e número

1. Criar app em <https://developers.facebook.com> do tipo *Business* e
   adicionar o produto **WhatsApp**.
2. A Meta fornece um **número de teste** gratuito que só manda mensagem para
   até 5 números cadastrados — suficiente para começar. Para produção, usar um
   número que **não** esteja em nenhum WhatsApp comum (um chip novo para o Fafa).
3. Anotar no `.env`:
   - `WHATSAPP_TOKEN` — token de acesso (gerar um permanente via *System User*)
   - `WHATSAPP_PHONE_NUMBER_ID` — ID do número (não é o número em si)
   - `WHATSAPP_VERIFY_TOKEN` — qualquer string secreta sua
   - `WHATSAPP_ALLOWED_NUMBERS` — `5551982835944` (só o Fafa responde a estes)

## 2. Só avisos (sem webhook)

Não precisa de servidor. Basta o token e:

```powershell
fafa notificar 5551982835944 "Terminei a tabela do Parque Germânico."
```

Funciona dentro de 24 h após a última mensagem que **você** mandou ao número
do Fafa. Fora disso, use um template aprovado:

```python
from fafa.channels.whatsapp import enviar_template
enviar_template("5551982835944", "fafa_aviso", ["Tabela do Parque Germânico pronta."])
```

Template sugerido para aprovar no painel da Meta (categoria *Utility*):
`Fafa: {{1}}`

## 3. Conversa (com webhook)

A Meta precisa alcançar seu servidor por HTTPS público. No desktop SIZE-LIDAR
basta o **Fafa-WhatsApp.bat** (ou `fafa whatsapp`): ele sobe o webhook na porta
8001 **e** abre o túnel do cloudflared, imprimindo a URL pública pronta:

```
  URL publica do webhook:  https://xxxx.trycloudflare.com/webhook
  Verify token:            <o seu WHATSAPP_VERIFY_TOKEN>
```

Pré-requisito único: `winget install Cloudflare.cloudflared`. No painel da
Meta → WhatsApp → Configuration → Webhook:

- Callback URL: a URL impressa (`https://xxxx.trycloudflare.com/webhook`)
- Verify token: o mesmo `WHATSAPP_VERIFY_TOKEN` do `.env`
- Assinar o campo `messages`

Limitação: a URL do túnel gratuito muda a cada reinício. Para algo estável, ou
um túnel nomeado do Cloudflare (gratuito, exige domínio) ou um relay mínimo na
nuvem que só repassa para o desktop.

## 4. Verificar

```powershell
curl http://127.0.0.1:8000/saude
```

Mande "oi" ao número do Fafa. O terminal onde roda `fafa whatsapp` mostra o
processamento; a resposta chega no WhatsApp.
