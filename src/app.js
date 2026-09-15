'use strict';
const byId = id => agents.find(a=>a.id===id);
const normalize = str => str.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
const state = {collection:'Montani',filter:'Todos',search:'',selected:null,route:[],brief:''};
const el = id => document.getElementById(id);
const escapeHTML = str => String(str).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));

function showView(view){
  for(const name of ['inicio','agentes','operacoes','projetos','conhecimento','biblioteca']) el(name).hidden=name!==view;
  document.querySelectorAll('.nav').forEach(b=>{b.classList.toggle('active',b.dataset.view===view);if(b.dataset.view===view)b.setAttribute('aria-current','page');else b.removeAttribute('aria-current');});
}
function renderDirectory(){
  const inCollection=agents.filter(a=>state.collection==='Todos'||a.collections.includes(state.collection));
  document.querySelector('.directory .count').textContent=inCollection.length;
  document.querySelector('.directory-footer').textContent=`${inCollection.length} agentes · ${state.collection==='Todos'?'Todas as especialidades':state.collection}`;
  el('collection-summary').textContent=`${state.collection==='Todos'?'Todas as especialidades':state.collection} · ${inCollection.length} agentes`;
  document.querySelectorAll('.catalog-card').forEach(card=>card.hidden=!inCollection.some(a=>a.id===card.dataset.agent));
  el('catalog-empty').hidden=inCollection.length>0;
  const visible=inCollection.filter(a=>(state.filter==='Todos'||a.group===state.filter)&&normalize(a.fullName+' '+a.description+' '+a.group+' '+a.collections.join(' ')).includes(normalize(state.search)));
  el('agent-list').replaceChildren();
  if(!visible.length){const p=document.createElement('p');p.className='no-results';p.textContent=inCollection.length?'Nenhum agente encontrado. Tente “render”, “vídeo” ou outro nome.':'Ainda não há agentes cadastrados em '+state.collection+'.';el('agent-list').append(p);return;}
  for(const group of ['Coordenação','Arquitetura','Imagem','Cinema']){
    const items=visible.filter(a=>a.group===group);if(!items.length)continue;
    const h=document.createElement('div');h.className='group-title';h.textContent=group;el('agent-list').append(h);
    for(const a of items){const b=document.createElement('button');b.type='button';b.className='agent-item'+(state.selected===a.id?' selected':'');b.setAttribute('aria-pressed',String(state.selected===a.id));b.setAttribute('aria-label',a.name+' — '+a.description);b.innerHTML=`<span class="agent-monogram">${escapeHTML(a.initials)}</span><span class="agent-info"><strong>${escapeHTML(a.name)}</strong><small>${escapeHTML(a.description)}</small></span><span class="agent-arrow" aria-hidden="true">↗</span>`;b.addEventListener('click',()=>selectAgent(a.id));el('agent-list').append(b);}
  }
}
function selectAgent(id,keepRoute=false){
  if(!byId(id))throw Error('Agente não encontrado.');
  if(state.collection!=='Todos'&&!byId(id).collections.includes(state.collection)){state.collection=byId(id).collections[0];el('collection').value=state.collection;}
  state.selected=id;if(!keepRoute){state.route=[id];state.brief=el('brief').value.trim();}
  showView('inicio');renderDirectory();renderRoute();
  if(matchMedia('(max-width:740px)').matches)el('route-title').scrollIntoView({behavior:'smooth',block:'start'});
  return {agent:id,name:byId(id).name,url:byId(id).url};
}
function recommend(text){
  const specialty=state.collection;
  if(state.collection!=='Todos'&&!agents.some(a=>a.collections.includes(state.collection)))return {ids:[],question:'Ainda não há agentes cadastrados em '+state.collection+'. Selecione Montani ou Todas as especialidades para buscar nos agentes disponíveis.'};
  const t=normalize(text);const ids=[];const add=id=>{if(!ids.includes(id))ids.push(id);};
  const has=re=>re.test(t);
  if(specialty==='Engenharia'){
    if(has(/hidraul|drenagem|vazao|tubul/))add('enghydro');
    else if(has(/apresenta/))add('apresentacao-eng');
    else if(has(/documento|prancha|grafico/))add('docs-graficos-eng');
    else if(has(/visual|render|imagem|infra/))add('infra-vision');
    else if(has(/saneamento|agua|esgoto/))add('eng-saneamento');
    else add('saneargpt');
    return {ids};
  }
  if(specialty==='Mastplan'){
    if(has(/foto|fotograf/))add('fotografo-ia');
    else if(has(/direcao|criativ|apresenta/))add('diretor-criativo');
    else if(has(/visual|render|imagem|infra/))add('infra-vision-2');
    else if(has(/urbano|urbanismo|planejamento urbano/))add('urban-planning');
    else add('master-plan');
    return {ids};
  }
  if(specialty==='Montani'&&has(/organizar|qual agente|agente de agentes|fluxo/)){add('nova-montani');return {ids};}
  if(has(/manual|template|hdri|corona|3ds ?max/)&&!has(/render|video|filme/))return {library:true,ids:[]};
  if(has(/timelapse|time.lapse|evolucao da obra/))add('flash');
  else {
    if(has(/filme|curta.metragem|curta metragem/))add('starlord');
    if(has(/storyboard|storytelling|roteiro|narrativa/))add('thanos');
    if(has(/direcao cinematografica|enquadramento cinematografico/))add('nick');
    if(has(/expan.{0,20}cena|desenvolver.{0,20}cena/))add('formiga');
    if(has(/planta/)&&has(/humaniz/))add('visao');
    if(has(/detalha/)&&has(/imagem|foto/))add('stan');
    if(has(/estac.{0,10}ano|inverno|verao|outono|primavera/))add('feiticeiro');
    if(has(/render|print/)){
      if(has(/exterior|extern|fachada|predio|edificio/))add('cavaleiro');
      else if(has(/interior|intern|sala|cozinha|quarto|banheiro/))add('ferro');
    }
    if(has(/ensaio|fotografico/))add('pantera');
    if(has(/edit|alter|mudar|trocar|remover|substituir/)&&has(/imagem|foto|ceu|fundo/))add('gaviao');
    if(has(/consisten|mesm.{0,20}personagem|manter.{0,20}identidade/))add('loki');
    if(has(/prompt/)&&has(/imagem/)&&!ids.length)add('capitao');
    if(has(/json/))add('estranho');else if(has(/veo|video|filme/))add('thor');
    if(!ids.length&&has(/criar.{0,30}imagem|gerar.{0,30}imagem/))add('capitao');
    if(!ids.length&&has(/imagem|fotografia|foto/))add('aranha');
  }
  if(!ids.length&&has(/render|print/))return {ids:[],question:'O render é de um ambiente interno ou de uma cena externa?',choices:[['Interior','Tenho um print de um ambiente interno e quero um render.'],['Exterior','Tenho um print de uma fachada e quero um render externo.']]};
  return ids.length?{ids}:{ids:[],question:'Você quer trabalhar com arquitetura, imagens ou cinema? Escolha um agente na lista ou detalhe o resultado que deseja.'};
}
function preparePrompt(a){
  const index=state.route.indexOf(a.id);
  let goal=state.brief||`Preciso de ajuda com ${a.description.toLowerCase()}.`;
  return `Olá! Trabalho com a Size Engenharia Ambiental Ltda.\n\nOBJETIVO DO PROJETO\n${goal}\n\nSUA ETAPA\n${a.description}.${state.route.length>1?` Etapa ${index+1} de ${state.route.length}. Foque nesta etapa; outras especialidades serão trabalhadas separadamente.`:''}\n\nMATERIAL DE ENTRADA\n${a.input}${index>0?'\nVou fornecer também o resultado aprovado da etapa anterior.':''}\n\nDIRETRIZES\nPreserve os elementos do projeto ou da imagem que não foram autorizados a mudar. Não invente medidas ou detalhes técnicos ausentes.\nQuando houver aplicação de marca, utilize o logotipo oficial fornecido, sem redesenhá-lo, e a tipografia Montserrat. Paleta SIZE: verde #00AB78, verde profissional #0F7D5A, turquesa #00B3B8, grafite #2E2E2E e cinza claro #E9ECEF. A paleta se aplica à apresentação gráfica; não recolora o projeto arquitetônico sem solicitação.\n\nENTREGA\nOriente a preparação do resultado desta etapa conforme seus recursos. Antes de começar, confirme os arquivos e informações indispensáveis que faltarem. Não presuma que anexos mencionados já foram enviados.`;
}
function renderRoute(){
  const a=byId(state.selected);if(!a)return;
  const c=el('route-content');c.innerHTML=`<h3 class="route-agent">${escapeHTML(a.name)}</h3><p class="route-reason">${escapeHTML(a.description)}. ${state.route.length>1?'Siga a sequência e leve o resultado de uma etapa à próxima.':'Prepare o material abaixo e abra este especialista.'}</p>`;
  if(state.route.length>1){const seq=document.createElement('div');seq.className='route-sequence';seq.setAttribute('aria-label','Etapas recomendadas');state.route.forEach((id,i)=>{const item=byId(id);const b=document.createElement('button');b.type='button';b.className=id===a.id?'current':'';b.setAttribute('aria-pressed',String(id===a.id));b.innerHTML=`<small>${String(i+1).padStart(2,'0')}</small> ${escapeHTML(item.name)} <span class="agent-arrow">↗</span>`;b.addEventListener('click',()=>selectAgent(id,true));seq.append(b);});c.append(seq);}
  const label=document.createElement('span');label.className='route-label';label.textContent='O QUE LEVAR';c.append(label);
  const input=document.createElement('p');input.className='route-reason';input.textContent=a.input;c.append(input);
  const requestLabel=document.createElement('label');requestLabel.className='route-label';requestLabel.htmlFor='request';requestLabel.textContent='PEDIDO PRONTO · PODE EDITAR';c.append(requestLabel);
  const request=document.createElement('textarea');request.id='request';request.className='request-text';request.value=preparePrompt(a);c.append(request);
  const actions=document.createElement('div');actions.className='route-buttons';const copy=document.createElement('button');copy.type='button';copy.className='secondary';copy.textContent='Copiar pedido';copy.addEventListener('click',async()=>{try{await navigator.clipboard.writeText(request.value);toast('Pedido copiado. Cole na conversa com o agente.');}catch{request.focus();request.select();toast('Selecione e copie o texto do pedido.');}});actions.append(copy);
  const link=document.createElement('a');link.className='primary';link.href=a.url;link.target='_blank';link.rel='noopener noreferrer';link.textContent='Abrir agente ↗';actions.append(link);c.append(actions);
  const note=document.createElement('p');note.className='route-note';note.textContent=a.coordinator?'A NOVA organiza o uso dos outros 17 agentes Montani. Cole o pedido nela para receber o fluxo recomendado.':'Cole o pedido e anexe o material no GPT. As especialidades foram organizadas pelos nomes fornecidos; confirme os recursos com o agente.';c.append(note);
}
function submitBrief(text){
  if(typeof text!=='string'||text.trim().length<3||text.length>3000)throw Error('Descreva seu objetivo com 3 a 3.000 caracteres.');
  state.brief=text.trim();el('brief').value=state.brief;const result=recommend(state.brief);
  if(result.library){showView('biblioteca');return {view:'biblioteca'};}
  showView('inicio');
  if(!result.ids.length){state.route=[];state.selected=null;renderDirectory();el('route-content').replaceChildren();const h=document.createElement('h3');h.textContent='Vamos definir o objetivo';const p=document.createElement('p');p.className='muted';p.textContent=result.question;el('route-content').append(h,p);for(const [label,value]of result.choices||[]){const b=document.createElement('button');b.type='button';b.className='secondary';b.style.marginRight='8px';b.textContent=label;b.addEventListener('click',()=>submitBrief(state.brief+'\n'+value));el('route-content').append(b);}return {question:result.question};}
  state.route=result.ids;selectAgent(result.ids[0],true);return {agents:result.ids.map(id=>({name:byId(id).name,url:byId(id).url}))};
}
let toastTimer;
function toast(message){el('toast').textContent=message;el('toast').hidden=false;clearTimeout(toastTimer);toastTimer=setTimeout(()=>el('toast').hidden=true,4500);}
el('collection').addEventListener('change',e=>{state.collection=e.target.value;state.selected=null;state.route=[];renderDirectory();el('route-content').innerHTML='<h3>Escolha seu próximo agente</h3><p class="muted">Selecione um especialista deste grupo ou descreva seu objetivo.</p>';});
document.querySelectorAll('.nav').forEach(b=>b.addEventListener('click',()=>showView(b.dataset.view)));
document.querySelector('.brand').addEventListener('click',()=>showView('inicio'));
el('search').addEventListener('input',e=>{state.search=e.target.value;renderDirectory();});
document.querySelectorAll('[data-filter]').forEach(b=>b.addEventListener('click',()=>{state.filter=b.dataset.filter;document.querySelectorAll('[data-filter]').forEach(x=>{x.classList.toggle('active',x===b);x.setAttribute('aria-pressed',String(x===b));});renderDirectory();}));
el('brief-form').addEventListener('submit',e=>{e.preventDefault();try{submitBrief(el('brief').value);}catch(error){toast(error.message);}});
document.querySelectorAll('[data-example]').forEach(b=>b.addEventListener('click',()=>submitBrief(b.dataset.example)));
for(const a of agents){const b=document.createElement('button');b.type='button';b.className='catalog-card';b.dataset.agent=a.id;b.innerHTML=`<span class="agent-monogram">${escapeHTML(a.initials)}</span><strong>${escapeHTML(a.name)}</strong><p class="muted">${escapeHTML(a.description)}</p><span>${escapeHTML(a.collections.join(' / '))} · ${escapeHTML(a.group)} · Preparar pedido ↗</span>`;b.addEventListener('click',()=>selectAgent(a.id));el('catalog').append(b);}
renderDirectory();
if(document.modelContext?.registerTool){const lifecycle=new AbortController();try{Promise.resolve(document.modelContext.registerTool({name:'prepare_agent_route',title:'Preparar caminho de agentes',description:'Seleciona agentes pelo objetivo e prepara o pedido na tela. Não executa GPTs externos nem envia mensagens.',inputSchema:{type:'object',properties:{objective:{type:'string',minLength:3,maxLength:3000}},required:['objective'],additionalProperties:false},annotations:{readOnlyHint:false},execute(input){if(!input||typeof input!=='object'||Object.keys(input).some(k=>k!=='objective'))throw Error('Informe apenas objective.');return submitBrief(input.objective);}},{signal:lifecycle.signal})).catch(()=>{});}catch{}window.addEventListener('pagehide',()=>lifecycle.abort(),{once:true});}
