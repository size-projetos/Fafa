'use strict';
/* Liga a "Conversa com Fafa" ao núcleo Python (backend/), quando ele está rodando.
   Sem núcleo, nada muda: o painel continua com as respostas locais de operations.js. */
(()=>{
const $=id=>document.getElementById(id);
const KEY='fafa_nucleo_chat';
const candidatos=[location.origin, 'http://127.0.0.1:8000'];
let base=null, info=null, gravador=null, pedacos=[], falando=null;

const estado=texto=>{const el=$('voice-status');if(el)el.textContent=texto||'';};
const historico=()=>{try{return JSON.parse(localStorage.getItem(KEY)||'[]');}catch{return [];}};
const guardar=msgs=>{try{localStorage.setItem(KEY,JSON.stringify(msgs.slice(-40)));}catch{}};

function preencher(el,texto){
  // texto puro + URLs como links (nunca innerHTML com texto do modelo)
  el.replaceChildren();
  const partes=String(texto).split(/(https?:\/\/[^\s<>()"']+)/g);
  partes.forEach((parte,i)=>{
    if(i%2===1){const a=document.createElement('a');a.href=parte;a.target='_blank';a.rel='noopener noreferrer';a.textContent=parte.replace(/^https?:\/\//,'').slice(0,60)+(parte.length>68?'…':'');a.className='link-nucleo';el.append(a);}
    else if(parte)el.append(document.createTextNode(parte));
  });
}
function bolha(role,texto,extra){
  const box=$('chat-messages');const d=document.createElement('div');
  d.className='message nucleo '+role+(extra?' '+extra:'');preencher(d,texto);box.append(d);
  box.scrollTop=box.scrollHeight;return d;
}
function renderHistorico(){
  const box=$('chat-messages');box.querySelectorAll('.nucleo').forEach(n=>n.remove());
  historico().slice(-20).forEach(m=>bolha(m.role,m.text));
}
function badge(){
  const heading=document.querySelector('.chat-dock .panel-heading .eyebrow');
  if(!heading)return;
  heading.textContent='NÚCLEO CONECTADO · '+(info.voz||'sem voz')+(info.ouvido?' · ouvido':'');
  heading.classList.add('nucleo-on');
  const h2=document.querySelector('.chat-dock .panel-heading h2');
  if(h2)h2.textContent='Conversa com '+(info.nome||'Fafa');
}

async function detectar(){
  for(const url of candidatos){
    try{
      const r=await fetch(url+'/api/saude',{cache:'no-store'});
      if(r.ok){const j=await r.json();if(j.status==='ok'){base=url;info=j;return true;}}
    }catch{}
  }
  return false;
}

async function falar(texto){
  try{
    const r=await fetch(base+'/api/falar',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({texto})});
    if(r.status===200){
      const blob=await r.blob();const url=URL.createObjectURL(blob);
      if(falando){falando.pause();}
      falando=new Audio(url);falando.onended=()=>URL.revokeObjectURL(url);await falando.play();return;
    }
  }catch{}
  if('speechSynthesis'in window){
    const u=new SpeechSynthesisUtterance(texto.replace(/[*#_`|]/g,''));u.lang='pt-BR';
    const v=speechSynthesis.getVoices().find(v=>/pt[-_]BR/i.test(v.lang));if(v)u.voice=v;
    speechSynthesis.cancel();speechSynthesis.speak(u);
  }
}

async function perguntar(texto){
  const msgs=historico();msgs.push({role:'user',text:texto});guardar(msgs);
  bolha('user',texto);
  const pend=bolha('assistant','…','pending');
  try{
    const r=await fetch(base+'/api/chat',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({texto,usuario:'painel'})});
    if(!r.ok)throw Error('HTTP '+r.status);
    const j=await r.json();
    pend.classList.remove('pending');preencher(pend,j.texto||'(sem resposta)');
    if(j.ferramentas?.length){const s=document.createElement('small');s.className='ferramentas';s.textContent='ferramentas: '+j.ferramentas.join(', ');pend.append(s);}
    msgs.push({role:'assistant',text:j.texto||''});guardar(msgs);
    falar(j.texto||'');
  }catch(err){
    pend.classList.remove('pending');pend.textContent='Não consegui falar com o núcleo ('+err.message+'). Verifique se o Fafa está aberto.';
  }
}

function interceptarEnvio(){
  const form=$('chat-form');const input=$('chat-input');
  form.addEventListener('submit',e=>{
    e.preventDefault();e.stopImmediatePropagation();
    const texto=String(input.value).trim();if(!texto)return;
    input.value='';perguntar(texto);
  },true); // captura: roda antes do handler local de operations.js
}

async function alternarGravacao(){
  const btn=$('voice-chat');
  if(gravador&&gravador.state==='recording'){gravador.stop();return;}
  if(!info.ouvido){estado('O núcleo está sem reconhecimento de voz (OPENAI_API_KEY).');return;}
  try{
    const stream=await navigator.mediaDevices.getUserMedia({audio:true});
    pedacos=[];gravador=new MediaRecorder(stream,{mimeType:MediaRecorder.isTypeSupported('audio/webm;codecs=opus')?'audio/webm;codecs=opus':'audio/webm'});
    gravador.ondataavailable=e=>{if(e.data.size)pedacos.push(e.data);};
    gravador.onstop=async()=>{
      stream.getTracks().forEach(t=>t.stop());
      btn.textContent='◉ Voz';btn.classList.remove('gravando');estado('Transcrevendo…');
      const blob=new Blob(pedacos,{type:'audio/webm'});const fd=new FormData();fd.append('audio',blob,'fala.webm');
      try{
        const r=await fetch(base+'/api/ouvir',{method:'POST',body:fd});const j=await r.json();
        if(j.texto){estado('');perguntar(j.texto);}else estado('Não entendi. Tente de novo.');
      }catch{estado('Falha ao transcrever.');}
    };
    gravador.start();btn.textContent='■ Parar';btn.classList.add('gravando');estado('Gravando… clique em Parar quando terminar.');
  }catch{estado('Não foi possível usar o microfone.');}
}

function interceptarVoz(){
  const btn=$('voice-chat');if(!btn)return;
  const novo=btn.cloneNode(true);btn.replaceWith(novo); // descarta o handler local (SpeechRecognition)
  novo.addEventListener('click',alternarGravacao);
}

async function iniciar(){
  if(!(await detectar()))return;
  badge();renderHistorico();interceptarEnvio();interceptarVoz();
  if(!historico().length)bolha('assistant','Núcleo conectado. Posso calcular, converter coordenadas, montar tabelas de vértices, ver sua tela e lembrar do que importa. O que vamos fazer?');
  const sys=$('system-online');if(sys)sys.textContent='Núcleo local · '+(info.voz||'texto');
}
document.addEventListener('DOMContentLoaded',iniciar);
if(document.readyState!=='loading')iniciar();
})();
