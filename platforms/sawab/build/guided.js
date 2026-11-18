/* Sawab guided practice engine. Rules: worked example -> hinted "Your turn" (same idea) -> unhinted independent block;
   mixed item types; feedback on every option; proper LaTeX; first guided block carries hints, the last block none. */
(()=>{
const CFG=JSON.parse(document.getElementById('cfg').textContent);
const ITEMS=JSON.parse(document.getElementById('items').textContent);
const BY=Object.fromEntries(ITEMS.map(i=>[i.id,i]));
const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
const LSK='sawab_gp_'+CFG.key;
const LS={get(k,d){try{return JSON.parse(localStorage.getItem(k))??d}catch(e){return d}},set(k,v){try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}}};
let H=LS.get(LSK,{});
let F=CFG.filters?LS.get(LSK+'_f','all'):'all';
const FNAME={all:'All questions',common:'Most common',hard:'Challenging'};
const fok=it=>F==='common'?!!it.cm:F==='hard'?it.l===3:true;
const hk=g=>F==='all'?g:g+'@'+F;
const L='ABCDEFGH';
const rnd=a=>{a=a.slice();for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a};
const app=$('#app');
function mj(el){if(CFG.math&&window.renderMathInElement){try{renderMathInElement(el||app,{delimiters:[{left:'$$',right:'$$',display:true},{left:'$',right:'$',display:false},{left:'\\(',right:'\\)',display:false}],throwOnError:false})}catch(e){}}}
const cap=h=>h?String(h).replace(/^(\s*(?:<[^>]+>)*)([a-z])/,(m,a,b)=>a+b.toUpperCase()):h;
const E=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));

/* ---------- numbers ---------- */
function parseNum(s){
  if(s==null)return null;
  s=String(s).replace(/<[^>]+>/g,'').replace(/\\dfrac|\\tfrac/g,'\\frac').replace(/\\left|\\right|\\,|\\!|\\ |\$/g,'').replace(/[−–]/g,'-').replace(/\s+/g,'').replace(/,(?=\d{3}\b)/g,'');
  s=s.replace(/\\frac\{(-?\d+(?:\.\d+)?)\}\{(-?\d+(?:\.\d+)?)\}/g,'($1)/($2)');
  s=s.replace(/%$/,'');
  let m=s.match(/^(-?)\((-?\d+(?:\.\d+)?)\)\/\((-?\d+(?:\.\d+)?)\)$/);
  if(m){const d=+m[3];if(!d)return null;return (m[1]?-1:1)*(+m[2])/d}
  m=s.match(/^(-?\d+(?:\.\d+)?)\/(-?\d+(?:\.\d+)?)$/);
  if(m){const d=+m[2];if(!d)return null;return (+m[1])/d}
  if(/^-?\d+(?:\.\d+)?$/.test(s))return +s;
  return null;
}
const near=(x,k)=>x!=null&&Math.abs(x-k)<=Math.max(1e-9,Math.abs(k)*5e-4);
const numOpt=it=>{if(!it.o)return null;const v=it.o.map(parseNum);if(v.some(x=>x==null))return null;if(new Set(v.map(x=>x.toFixed(6))).size<v.length)return null;return v};
const BAD_FILL=/which of the following|could be|possible value|must be|which statement|which quantity|which expression|which equation|which graph|which of these/i;

/* ---------- types ---------- */
function typesFor(it){
  const t=[];
  if(!it.o){t.push('fill');return t}
  t.push('mc','tf');
  if(numOpt(it)&&!BAD_FILL.test(it.q.replace(/<[^>]+>/g,'')))t.push('fill');
  if(it.ord)t.push('order');
  if(it.c&&it.c.filter(Boolean).length>=3&&it.o.length===4)t.push('match');
  return t;
}
const ROT_T=['mc','fill','tf','order','match','mc'];
const ROT_I=['fill','mc','tf','match','order','mc'];
function pickType(it,k,rot,prev){
  const av=typesFor(it);const want=rot[k%rot.length];
  const order=[want,...['mc','fill','tf','order','match'].filter(x=>x!==want)];
  const ok=order.filter(x=>av.includes(x));
  const alt=ok.find(x=>x!==prev);
  return alt||ok[0];
}

/* ---------- session ---------- */
function groupItems(g){const G=CFG.groups.find(x=>x.id===g);if(!G)return[];return (G.ids==='*'?ITEMS:G.ids.map(i=>BY[i]).filter(Boolean)).filter(fok)}
function build(gid){
  const G=CFG.groups.find(x=>x.id===gid);let pool=groupItems(gid);
  const rec=H[hk(gid)]||{};let seen=new Set(rec.seen||[]);
  let fresh=pool.filter(i=>!seen.has(i.id));
  if(fresh.length<Math.min(pool.length,12)){fresh=pool;seen=new Set()}
  const N=fresh.length;let p=Math.min(6,Math.floor(N/3)),q=Math.min(6,N-2*p);
  if(p<1&&N>=2){p=1;q=Math.max(0,N-2)}
  /* twins first: the worked example and "Your turn" share the same idea and trick */
  const G0=CFG.groups.find(x=>x.id===gid),allG=(G0.ids==='*'?ITEMS:G0.ids.map(i=>BY[i]).filter(Boolean));
  const twinC=rnd(allG.filter(i=>i.wk&&i.tw&&BY[i.tw]&&fok(BY[i.tw])&&!seen.has(i.tw)));
  const twinAll=rnd(allG.filter(i=>i.wk&&i.tw&&BY[i.tw]&&fok(BY[i.tw])));
  const tp=[];const tu=new Set();
  for(const w of [...twinC,...twinAll]){if(tp.length>=6)break;if(tu.has(w.id))continue;tu.add(w.id);tu.add(w.tw);tp.push([w,BY[w.tw]])}
  if(tp.length){
    const p2=tp.length,rest0=rnd(fresh.filter(i=>!tu.has(i.id)&&!(i.tw&&tu.has(i.tw)))),q2=Math.min(6,rest0.length);
    tp.sort((a,b)=>a[1].l-b[1].l);
    const steps=[];let prev=null,k=0;
    tp.forEach(([w,t])=>{steps.push({kind:'w',it:w,ri:0});const ty=pickType(t,k++,ROT_T,prev);prev=ty;steps.push({kind:'t',it:t,type:ty,tries:0,hint:0,done:false,ok:null,pts:0})});
    k=0;prev=null;rest0.slice(0,q2).forEach(it=>{const ty=pickType(it,k++,ROT_I,prev);prev=ty;steps.push({kind:'i',it,type:ty,tries:0,hint:0,done:false,ok:null,pts:0})});
    steps.forEach(x=>prep(x));
    return {gid,G,steps,i:0,t0:Date.now(),nPairs:p2,nInd:q2};
  }
  const bySub={};fresh.forEach(i=>(bySub[i.u||'']=bySub[i.u||'']||[]).push(i));
  Object.values(bySub).forEach(a=>a.sort((x,y)=>(x.l-y.l)||Math.random()-.5));
  const subs=Object.keys(bySub).sort((a,b)=>bySub[b].length-bySub[a].length||Math.random()-.5);
  const used=new Set(),pairs=[];
  for(const s of rnd(subs)){const a=bySub[s];while(a.length>=2&&pairs.length<p){pairs.push([a.shift(),a.shift()])}}
  let rest=rnd(Object.values(bySub).flat()).filter(i=>!pairs.some(pr=>pr.includes(i)));
  rest.sort((a,b)=>a.l-b.l);
  while(pairs.length<p&&rest.length>=2){pairs.push([rest.shift(),rest.shift()])}
  if(CFG.desmos)pairs.forEach(pr=>{if(!codes(pr[0]).length&&codes(pr[1]).length)pr.reverse()});
  pairs.sort((a,b)=>a[0].l-b[0].l);
  const subsUsed=new Set(pairs.map(pr=>pr[0].u));
  rest=rnd(rest);rest.sort((a,b)=>(subsUsed.has(b.u)?1:0)-(subsUsed.has(a.u)?1:0)||Math.random()-.5);
  const ind=rest.slice(0,q);
  const steps=[];let prev=null,k=0;
  pairs.forEach(([w,t])=>{steps.push({kind:'w',it:w,ri:0});const ty=pickType(t,k++,ROT_T,prev);prev=ty;steps.push({kind:'t',it:t,type:ty,tries:0,hint:0,done:false,ok:null,pts:0})});
  k=0;prev=null;rnd(ind).forEach(it=>{const ty=pickType(it,k++,ROT_I,prev);prev=ty;steps.push({kind:'i',it,type:ty,tries:0,hint:0,done:false,ok:null,pts:0})});
  steps.forEach(s=>prep(s));
  return {gid,G,steps,i:0,t0:Date.now(),nPairs:pairs.length,nInd:ind.length};
}
function prep(s){
  if(s.kind==='w')return;const it=s.it;
  if(s.type==='tf'){
    const wrong=it.o.map((_,i)=>i).filter(i=>i!==it.a&&it.a!=null);
    const useTrue=Math.random()<.45||!wrong.length||(it.a==null);
    if(it.a==null){s.type='fill'}
    else{s.claim=useTrue?it.a:wrong.sort((a,b)=>(it.c&&it.c[b]?1:0)-(it.c&&it.c[a]?1:0)||Math.random()-.5)[0]}
  }
  if(s.type==='order'){s.seq=[];s.pool=rnd(it.ord.map((_,i)=>i));}
  if(s.type==='match'){
    const wi=it.o.map((_,i)=>i).filter(i=>i!==it.a&&it.c[i]);
    s.rows=wi.slice(0,3);s.ans=rnd(s.rows);s.sel={};
  }
  if(s.type==='mc'){s.sel=null}
  if(s.type==='fill'){s.val=''}
}


/* ---------- Desmos (SAT) ---------- */
const DK=CFG.desmos||null;
const dec=s=>s.replace(/&lt;/g,'<').replace(/&gt;/g,'>').replace(/&quot;/g,'"').replace(/&amp;/g,'&');
const codesOld=it=>{const o=[];(it.s||[]).forEach((st,i)=>{const re=/<code>([\s\S]*?)<\/code>/g;let m;while((m=re.exec(st)))o.push({step:i+1,code:dec(m[1].trim())})});return o};
const codes=it=>{if(it.dz){const o=[];it.dz.forEach(st=>(st.c||[]).forEach(c=>o.push({code:c.s,tex:c.x})));return o}return codesOld(it)};
const toLatex=c=>c.replace(/\*/g,'\\cdot ').replace(/\bsqrt\(([^()]*)\)/g,'\\sqrt{$1}').replace(/\bpi\b/g,'\\pi ').replace(/<=/g,'\\le ').replace(/>=/g,'\\ge ').replace(/\babs\(([^()]*)\)/g,'\\left|$1\\right|').replace(/\b(ln|log|sin|cos|tan|arcsin|arccos|arctan)\(/g,'\\$1(').replace(/\b(floor|ceil|round|mod|min|max|mean|median|stdev|stdevp|total|sign|nCr|nPr|lcm|gcd|random)\(/g,'\\operatorname{$1}(');
let dock=null,dcalc=null,dstate='idle',dqueue=null;
function ensureDock(){
  if(dock)return;
  dock=document.createElement('div');dock.id='dock';dock.innerHTML='<div class="dh"><b>Desmos graphing calculator</b><span><button id="dclr" class="link">Clear</button><button id="dx" class="link">Close</button></span></div><div id="dbody"></div>';
  document.body.appendChild(dock);
  $('#dx').onclick=()=>dockShow(false);$('#dclr').onclick=()=>{if(dcalc)dcalc.setBlank()};
}
function loadDesmos(cb){
  if(window.Desmos){cb();return}
  if(dstate==='loading'){dqueue=cb;return}
  dstate='loading';dqueue=cb;
  const sc=document.createElement('script');sc.src='https://www.desmos.com/api/v1.12/calculator.js?apiKey='+encodeURIComponent(DK.key);
  sc.onload=()=>{dstate='ready';const f=dqueue;dqueue=null;f&&f()};
  sc.onerror=()=>{dstate='failed';$('#dbody').innerHTML='<div class="dfail">Desmos could not load. Check your connection, or open <a href="https://www.desmos.com/calculator" target="_blank" rel="noopener">desmos.com/calculator</a> in another tab and type the lines shown.</div>'};
  document.head.appendChild(sc);
}
function dockShow(on){
  ensureDock();dock.classList.toggle('on',on);document.body.classList.toggle('dk-open',on);
  const fb=$('#dfab');if(fb)fb.style.display=on?'none':'';
  if(on&&!dcalc){loadDesmos(()=>{if(dcalc||!window.Desmos)return;dcalc=Desmos.GraphingCalculator($('#dbody'),{keypad:true,expressions:true,settingsMenu:true,zoomButtons:true,expressionsTopbar:true});if(dqueue2){const q=dqueue2;dqueue2=null;put(q)}})}
}
let dqueue2=null;
function put(list){
  if(!dcalc){dqueue2=list;return}
  dcalc.setBlank();
  list.forEach((c,i)=>dcalc.setExpression({id:'g'+i,latex:c.tex||toLatex(c.code)}));
}
function dockLoad(it){const list=codes(it);if(list.length)dqueue2=list;dockShow(true);if(dcalc&&dqueue2){const q=dqueue2;dqueue2=null;put(q)}}
function fab(){
  if(!DK)return;ensureDock();
  const b=document.createElement('button');b.id='dfab';b.textContent='Open Desmos';b.onclick=()=>dockShow(true);document.body.appendChild(b);
  document.addEventListener('click',e=>{const t=e.target.closest('[data-dl]');if(t){dockLoad(BY[t.dataset.dl])}});
}
const TOOLKIT=[['Calculate','Click an empty expression line and type an arithmetic expression such as <code>(26-17)/(7-4)</code>. The value appears at the right of the line.'],['Solve an equation','Type the equation, for example <code>8x-2=5x+34</code>. Desmos draws a vertical line at the solution; click it to read the x-value. Or graph each side as its own line and click where they cross.'],['Find intersections, zeros, vertex','Graph the functions and click a curve: grey dots appear at x-intercepts, the vertex and intersections. Click a dot to read its coordinates.'],['Unknown value or parameter','Type a letter such as <code>a</code> inside an expression, then click "add slider". Drag it until the condition in the question holds.'],['Data and best-fit line','Add a table (the + button), enter the data, then type <code>y_1~mx_1+b</code> to get the regression line and its r value.'],['Test an answer choice','Type the answer choice as an expression, or substitute it into the equation, and see whether both sides match.']];
function walk(it){
  if(!it.dz)return '';
  return `<ol class="dwalk">${it.dz.map((st,i)=>`<li class="${st.fin?'dfin':''}"><span class="dn">${st.fin?'✓':i+1}</span><div><div>${st.t}</div>${st.c&&st.c.length?`<div class="dchips">${st.c.map(c=>`<code>${E(c.s)}</code>`).join('')}</div>`:''}${st.r?`<div class="dread">${st.r}</div>`:''}</div></li>`).join('')}</ol>`;
}
function desmosPanel(it,closed){
  if(!DK)return '';
  const cs=codes(it);
  const body=`<p class="dtip">Click an empty line in Desmos and type exactly what is shown. After <code>/</code> or <code>^</code>, press the right-arrow key to leave the fraction or exponent.</p>${walk(it)}<div class="act"><button class="btn sm" data-dl="${it.id}">${cs.length?'Open these lines in Desmos':'Open Desmos'}</button></div><details class="tk"><summary>Desmos toolkit: the six moves used on the SAT</summary><ul>${TOOLKIT.map(t=>`<li><b>${t[0]}.</b> ${t[1]}</li>`).join('')}</ul></details>`;
  return closed?`<details class="call dsm dd"><summary><b>Solve it with Desmos</b></summary>${body}</details>`:`<div class="call dsm"><b>Solve it with Desmos</b>${body}</div>`;
}

/* ---------- home ---------- */
function ring(p){const r=18,c=2*Math.PI*r;return `<svg class="ring" viewBox="0 0 44 44"><circle cx="22" cy="22" r="${r}" class="rb"/><circle cx="22" cy="22" r="${r}" class="rf" stroke-dasharray="${(c*p/100).toFixed(1)} ${c.toFixed(1)}" transform="rotate(-90 22 22)"/><text x="22" y="26" text-anchor="middle">${p>0?Math.round(p):'–'}</text></svg>`}
function home(){
  S=null;const cats=[...new Set(CFG.groups.map(g=>g.cat))];
  const done=CFG.groups.filter(g=>(H[hk(g.id)]||{}).best>=80).length;
  app.innerHTML=`<div class="wrap">${head()}
  <section class="hero"><div class="eyebrow">${E(CFG.eyebrow)}</div><h1>${CFG.title}</h1><p class="lede">${CFG.lede}</p></section>
  <section class="how"><div class="how-i"><b>1</b><div><h3>Watch a worked example</h3><p>Reveal the solution one step at a time and read the idea behind it.</p></div></div><div class="how-i"><b>2</b><div><h3>Your turn, with hints</h3><p>The same idea, a new question. Hints are free; every wrong option tells you the mistake it hides.</p></div></div><div class="how-i"><b>3</b><div><h3>Now alone</h3><p>No hints. Done when you score 80% or more in the independent block.</p></div></div></section>
  ${CFG.filters?`<div class="filt"><span>Questions</span><div class="seg">${['all','common','hard'].map(k=>`<button data-f="${k}" class="${F===k?'on':''}">${FNAME[k]}</button>`).join('')}</div><small>${F==='common'?'Only the question types that come up most often in each skill.':F==='hard'?'Only hard-level questions.':'Every question type and level.'}</small></div>`:''}<div class="mini"><span>${done} of ${CFG.groups.length} topics passed</span><span>Each session: up to 6 worked examples + 6 hinted turns + 6 independent questions</span></div>
  ${cats.map(c=>`<h2 class="cat">${E(c)}</h2><div class="gr">${CFG.groups.filter(g=>g.cat===c).map(g=>{const n=groupItems(g.id).length,r=H[hk(g.id)]||{};const dis=n<3;return `<button class="gcard" data-g="${g.id}" ${dis?'disabled':''}><div class="gtop">${ring(r.best||0)}<div><h3>${E(g.label)}</h3><small>${r.n?`${r.n} session${r.n>1?'s':''} · best ${r.best}%`:'Not started'}</small></div></div><p>${E(g.blurb||'')}</p><span class="go">${r.n?'Practise again':'Start'} →</span></button>`}).join('')}</div>`).join('')}
  <footer>Sawab · Original practice questions · progress is saved on this device</footer></div>`;
  $$('.filt [data-f]').forEach(b=>b.onclick=()=>{F=b.dataset.f;LS.set(LSK+'_f',F);home()});
  $$('.gcard').forEach(b=>b.onclick=()=>{S=build(b.dataset.g);if(S.steps.length<2)return;go()});
  mj();window.scrollTo(0,0);
}
function head(){return `<header class="top"><a class="brand" href="../"><span class="logo">${CFG.logo}</span><span><b>${E(CFG.name)}</b><small>${E(CFG.sub)} · Guided practice</small></span></a><nav><a class="pill" href="../mock/">Mock exam</a><a class="pill" href="../">⟵ Hub</a></nav></header>`}

/* ---------- session shell ---------- */
let S=null;
function go(){render();window.scrollTo(0,0)}
function dots(){
  return `<div class="dots">${S.steps.map((s,i)=>{const c=['d',s.kind,i===S.i?'cur':'',(s.kind!=='w'&&s.done)?(s.ok?'ok':'no'):(s.kind==='w'&&i<S.i?'ok':'')].join(' ');return `<i class="${c}" title="${s.kind==='w'?'Worked example':s.kind==='t'?'Your turn':'Independent'}"></i>`}).join('')}</div>`;
}
function phase(s){
  if(s.kind==='w'){const n=S.steps.slice(0,S.steps.indexOf(s)+1).filter(x=>x.kind==='w').length;return `<span class="tag w">Worked example ${n} of ${S.nPairs}</span>`}
  if(s.kind==='t'){const n=S.steps.slice(0,S.steps.indexOf(s)+1).filter(x=>x.kind==='t').length;return `<span class="tag t">Your turn ${n} of ${S.nPairs} · hints on</span>`}
  const n=S.steps.slice(0,S.steps.indexOf(s)+1).filter(x=>x.kind==='i').length;return `<span class="tag i">Independent ${n} of ${S.nInd} · no hints</span>`;
}
function render(){
  const s=S.steps[S.i];
  app.innerHTML=`<div class="wrap">${head()}<div class="sess"><div class="sbar"><button class="link" id="quit">← Topics</button><b>${E(S.G.label)}${F!=='all'?` <span class="fchip">${FNAME[F]}</span>`:''}</b><span class="cnt">${S.i+1} / ${S.steps.length}</span></div>${dots()}<div id="stage"></div></div></div>`;
  $('#quit').onclick=()=>{if(confirm('Leave this session? Your answers so far will not be saved.'))home()};
  stage();
}
function qHtml(it){return `<div class="qbox">${it.q}${it.f||''}</div>`}
function optsStatic(it,mark){return `<div class="opts static">${it.o.map((o,i)=>`<div class="opt ${mark&&i===it.a?'good':''}"><span class="ltr">${L[i]}</span><span class="ot">${o}</span></div>`).join('')}</div>`}
function stage(){
  const s=S.steps[S.i],st=$('#stage');
  if(s.kind==='w')return worked(s,st);
  practice(s,st);
}
function worked(s,st){
  const it=s.it,n=it.s.length;
  st.innerHTML=`<div class="card">${phase(s)}<h2 class="ct">Watch how it is solved</h2>${qHtml(it)}${it.o?optsStatic(it,s.ri>=n):''}
  <ol class="steps">${it.s.slice(0,s.ri).map((x,i)=>`<li class="in"><span class="sn">${i+1}</span><div>${x}</div></li>`).join('')}</ol>
  ${s.ri<n?`<div class="act"><button class="btn" id="next">Show step ${s.ri+1} of ${n}</button><button class="link" id="all">show all steps</button></div>`:`<div class="ans">Answer: <b>${it.o?`${L[it.a]}. ${it.o[it.a]}`:it.d}</b></div>${it.t?`<div class="call idea"><b>The idea</b>${it.t}</div>`:''}${watch(it)}${desmosPanel(it)}<div class="act"><button class="btn" id="go">Your turn →</button></div>`}</div>`;
  const nx=$('#next',st);if(nx)nx.onclick=()=>{s.ri++;stage();mj($('#stage'))};
  const al=$('#all',st);if(al)al.onclick=()=>{s.ri=n;stage();mj($('#stage'))};
  const g=$('#go',st);if(g)g.onclick=()=>{S.i++;go()};
  mj(st);
}
function watch(it){
  if(!it.o||!it.c)return it.k?`<div class="call watch"><b>Watch out</b>${it.k}</div>`:'';
  const w=it.c.map((c,i)=>c&&i!==it.a?`<li><b>${L[i]}.</b> ${cap(c)}</li>`:'').join('');
  return w?`<div class="call watch"><b>Watch out — the wrong options are traps</b><ul>${w}</ul></div>`:(it.k?`<div class="call watch"><b>Watch out</b>${it.k}</div>`:'');
}

/* ---------- practice ---------- */
function hints(s){
  const it=s.it,h=[];
  if(it.h)h.push(it.h);
  if(s.type==='mc'&&it.o){const w=it.o.map((_,i)=>i).filter(i=>i!==it.a);const e=w[(it.id.length)%w.length];h.push(`Eliminate <b>${L[e]}</b>: ${it.c&&it.c[e]?it.c[e]:'it does not survive a quick check of the question.'}`)}
  else if(it.s&&it.s.length>1)h.push(`The first step: ${it.s[0]}`);
  return h;
}
function widget(s){
  const it=s.it,dis=s.done?'disabled':'';
  if(s.type==='mc')return `<div class="opts">${it.o.map((o,i)=>`<button class="opt ${s.sel===i?'sel':''} ${s.done?(i===it.a?'good':(s.sel===i?'bad':'')):''}" data-i="${i}" ${dis}><span class="ltr">${L[i]}</span><span class="ot">${o}</span></button>`).join('')}</div>`;
  if(s.type==='tf'){const mark=s.done?(b=>(b===(s.claim===it.a))?'good':(s.sel===b?'bad':'')):()=>'';return `<div class="claim"><small>Claim</small><div>The correct answer is <b>${it.o[s.claim]}</b>.</div></div><div class="tf"><button class="opt ${s.sel===true?'sel':''} ${mark(true)}" data-b="1" ${dis}>True</button><button class="opt ${s.sel===false?'sel':''} ${mark(false)}" data-b="0" ${dis}>False</button></div>`}
  if(s.type==='fill')return `<div class="fillrow"><input class="fin" id="fin" inputmode="decimal" autocomplete="off" placeholder="Type your answer" value="${E(s.val||'')}" ${dis}><small>Whole number, decimal or fraction such as 3/4</small></div>`;
  if(s.type==='order')return `<div class="ordhelp">Click the steps in the order you would do them.</div><ol class="ordsel">${s.seq.map((i,k)=>`<li><button class="chip pl" data-rm="${k}" ${dis}><span class="sn">${k+1}</span>${it.ord[i]}</button></li>`).join('')}</ol><div class="ordpool">${s.pool.filter(i=>!s.seq.includes(i)).map(i=>`<button class="chip" data-add="${i}" ${dis}>${it.ord[i]}</button>`).join('')}</div>`;
  if(s.type==='match'){
    const ms=s.ans.map((r,k)=>`<li><b>${String.fromCharCode(65+k)}.</b> ${cap(it.c[r])}</li>`).join('');
    return `<div class="ordhelp">Each wrong option comes from one mistake. Match them.</div><div class="mtab">${s.rows.map(r=>`<div class="mrow"><div class="mo"><span class="ltr">${L[r]}</span><span class="ot">${it.o[r]}</span></div><select data-r="${r}" ${dis}><option value="">Choose the mistake…</option>${s.ans.map((x,k)=>`<option value="${x}" ${s.sel[r]==x?'selected':''}>${String.fromCharCode(65+k)}</option>`).join('')}</select></div>`).join('')}</div><ol class="mist">${ms}</ol>`;
  }
  return '';
}
function canCheck(s){
  if(s.type==='mc')return s.sel!=null;if(s.type==='tf')return s.sel!=null;
  if(s.type==='fill')return (s.val||'').trim()!=='';
  if(s.type==='order')return s.seq.length===s.it.ord.length;
  if(s.type==='match')return s.rows.every(r=>s.sel[r]!=null&&s.sel[r]!=='');
  return false;
}
function practice(s,st){
  const it=s.it,guided=s.kind==='t',hs=guided?hints(s):[];
  const typeName={mc:'Multiple choice',tf:'True or false',fill:'Type the answer',order:'Put the steps in order',match:'Match the mistake'}[s.type];
  const left=guided?Math.max(0,2-s.tries):1;
  st.innerHTML=`<div class="card">${phase(s)}<span class="ty">${typeName}</span>${guided?`<h2 class="ct">Same idea, new question</h2>`:`<h2 class="ct">Work it out</h2>`}
  ${s.type==='order'?`<div class="qbox">${it.q}${it.f||''}</div>`:qHtml(it)}
  ${widget(s)}
  ${guided&&!s.done&&hs.length?`<div class="hints">${hs.slice(0,s.hint).map((h,i)=>`<div class="call hint"><b>Hint ${i+1}</b>${h}</div>`).join('')}</div>`:''}
  <div id="fb"></div>
  <div class="act" id="acts"></div></div>`;
  bind(s);acts(s);if(s.fb)showFb(s);mj(st);
}
function acts(s){
  const a=$('#acts');const guided=s.kind==='t',hs=guided?hints(s):[];
  if(s.done){a.innerHTML=`<button class="btn" id="cont">${S.i===S.steps.length-1?'See my results':'Continue →'}</button>`;$('#cont').onclick=()=>{if(S.i===S.steps.length-1)summary();else{S.i++;go()}};return}
  a.innerHTML=`<button class="btn" id="chk" ${canCheck(s)?'':'disabled'}>Check</button>${guided&&s.hint<hs.length?`<button class="ghost" id="hint">Hint (${s.hint}/${hs.length})</button>`:''}`;
  $('#chk').onclick=()=>check(s);
  const h=$('#hint');if(h)h.onclick=()=>{s.hint++;keep(s)};
}
function keep(s){practice(s,$('#stage'))}
function bind(s){
  const st=$('#stage');
  $$('.opt[data-i]',st).forEach(b=>b.onclick=()=>{if(s.done)return;s.sel=+b.dataset.i;s.fb=null;keep(s)});
  $$('.opt[data-b]',st).forEach(b=>b.onclick=()=>{if(s.done)return;s.sel=b.dataset.b==='1';s.fb=null;keep(s)});
  const f=$('#fin',st);if(f){f.oninput=()=>{s.val=f.value;const c=$('#chk');if(c)c.disabled=!canCheck(s)};f.onkeydown=e=>{if(e.key==='Enter'&&canCheck(s)&&!s.done)check(s)};if(!s.done&&!s.fb)setTimeout(()=>f.focus(),30)}
  $$('[data-add]',st).forEach(b=>b.onclick=()=>{s.seq.push(+b.dataset.add);s.fb=null;keep(s)});
  $$('[data-rm]',st).forEach(b=>b.onclick=()=>{s.seq.splice(+b.dataset.rm,1);s.fb=null;keep(s)});
  $$('select[data-r]',st).forEach(x=>x.onchange=()=>{s.sel[x.dataset.r]=x.value===''?'':+x.value;s.fb=null;const c=$('#chk');if(c)c.disabled=!canCheck(s)});
}
function check(s){
  const it=s.it;let ok=false,fb='',bad=null;
  if(s.type==='mc'){ok=s.sel===it.a;if(!ok)fb=cap(it.c&&it.c[s.sel]?it.c[s.sel]:(it.k||'That option does not match the question.'))}
  else if(s.type==='tf'){const truth=s.claim===it.a;ok=s.sel===truth;if(!ok){fb=truth?`The claim is actually true: the answer is ${it.o[it.a]}.`:cap(it.c&&it.c[s.claim]?it.c[s.claim]:(it.k||'That value comes from a common mistake.'))}}
  else if(s.type==='fill'){
    const v=parseNum(s.val);
    if(v==null){s.fb={kind:'warn',html:'Type a number, such as 12, 3/4 or 0.75.'};showFb(s);return}
    const key=it.a!=null?numOpt(it)[it.a]:it.n;ok=near(v,key);
    if(!ok){const ov=it.o?numOpt(it):null;const hit=ov?ov.findIndex(x=>near(v,x)):-1;fb=cap(hit>=0&&it.c&&it.c[hit]?it.c[hit]:(it.k||'Not quite. Check each step again.'))}
  }
  else if(s.type==='order'){ok=s.seq.every((x,k)=>x===k);if(!ok){const right=s.seq.filter((x,k)=>x===k).length;fb=`${right} of ${s.seq.length} steps are in the right place. Think about what each step needs from the one before it.`}}
  else if(s.type==='match'){bad=s.rows.filter(r=>+s.sel[r]!==r);ok=!bad.length;if(!ok)fb=`${s.rows.length-bad.length} of ${s.rows.length} matches are right. Re-read the mistake that would give each option.`}
  s.tries++;
  const guided=s.kind==='t';
  if(ok){s.done=true;s.ok=true;s.pts=guided?(s.tries===1&&!s.hint?1:s.tries===1?.75:.5):1;if(!guided)s.pts=1;s.fb={kind:'good',html:'Correct.'}}
  else if(guided&&s.tries<2){s.hint=Math.max(s.hint,1);s.fb={kind:'bad',html:fb,retry:true}}
  else{s.done=true;s.ok=false;s.pts=0;s.fb={kind:'bad',html:fb,final:true}}
  keep(s);
}
function solutionHtml(s){
  const it=s.it;
  const o=it.o&&(s.type==='mc'||s.type==='tf'||s.type==='fill'||s.type==='match')?`<div class="every"><b>Every option</b>${it.o.map((x,i)=>`<div class="eo ${i===it.a?'g':'b'}"><span class="ltr">${L[i]}</span><span class="ot">${x}</span><span class="why">${i===it.a?'<b>Correct.</b> '+(it.t||''):cap(it.c&&it.c[i]?it.c[i]:(it.k||''))}</span></div>`).join('')}</div>`:'';
  return `<details class="sol" open><summary>Full solution</summary><ol class="steps">${it.s.map((x,i)=>`<li class="in"><span class="sn">${i+1}</span><div>${x}</div></li>`).join('')}</ol><div class="ans">Answer: <b>${it.o?`${L[it.a]}. ${it.o[it.a]}`:it.d}</b></div>${DK?desmosPanel(it,true):''}${o}</details>`;
}
function showFb(s){
  const f=s.fb,b=$('#fb');if(!f||!b)return;
  if(f.kind==='warn'){b.innerHTML=`<div class="fb warn">${f.html}</div>`;return}
  if(s.done){
    b.innerHTML=`<div class="fb ${f.kind}"><b>${s.ok?(s.tries>1?'Got it on the second try.':'Correct.'):'Not this time.'}</b>${f.kind==='bad'&&f.html?` <span>${f.html}</span>`:''}</div>${solutionHtml(s)}`;
  }else b.innerHTML=`<div class="fb bad"><b>Not yet.</b> <span>${f.html}</span> ${hints(s).length?'<em>Hint 1 is now open — try again.</em>':'<em>Try again.</em>'}</div>`;
  mj(b);
}

/* ---------- summary ---------- */
function summary(){
  const T=S.steps.filter(x=>x.kind==='t'),I=S.steps.filter(x=>x.kind==='i');
  const gp=T.reduce((a,x)=>a+x.pts,0),ip=I.reduce((a,x)=>a+x.pts,0);
  const gpct=T.length?Math.round(gp/T.length*100):0,ipct=I.length?Math.round(ip/I.length*100):gpct;
  const pass=ipct>=80;
  const rec=H[hk(S.gid)]||{best:0,n:0,seen:[]};
  rec.best=Math.max(rec.best||0,ipct);rec.last=ipct;rec.n=(rec.n||0)+1;rec.date=new Date().toISOString().slice(0,10);
  rec.seen=[...new Set([...(rec.seen||[]),...S.steps.filter(x=>x.kind!=='w').map(x=>x.it.id),...S.steps.filter(x=>x.kind==='w').map(x=>x.it.id)])].slice(-400);
  H[hk(S.gid)]=rec;LS.set(LSK,H);
  const miss=S.steps.filter(x=>x.kind!=='w'&&!x.ok);
  app.innerHTML=`<div class="wrap">${head()}<section class="sum"><div class="eyebrow">${E(S.G.label)}${F!=='all'?' · '+FNAME[F]:''}</div><h1>${pass?'Mastery gate passed.':'Nearly there.'}</h1>
  <p class="lede">${pass?'You solved the independent block without hints. That is the signal that the idea has stuck.':'The independent block is the real test. Review the questions below, then try a fresh session.'}</p>
  <div class="scores"><div class="sc"><small>Guided block</small><b>${gpct}%</b><span>${+gp.toFixed(2)} of ${T.length} points, hints counted</span></div><div class="sc ${pass?'pass':''}"><small>Independent block</small><b>${ipct}%</b><span>${ip} of ${I.length} correct, no hints</span></div><div class="sc"><small>Best on this topic</small><b>${rec.best}%</b><span>${rec.n} session${rec.n>1?'s':''} saved</span></div></div>
  <p class="done"><b>Done when</b> you score at least 80% in the independent block.</p>
  <div class="act"><button class="btn" id="again">New session, fresh questions</button><button class="ghost" id="back">All topics</button></div>
  ${miss.length?`<h2 class="cat">Review what you missed</h2>${miss.map((s,i)=>`<div class="card rv"><span class="tag ${s.kind}">${s.kind==='t'?'Your turn':'Independent'}</span>${qHtml(s.it)}${solutionHtml({...s,type:'mc'}).replace('<details class="sol" open>','<details class="sol">')}</div>`).join('')}`:`<div class="card"><b>Clean sheet.</b> Every question was right. Try another topic or come back for a fresh session.</div>`}
  </section></div>`;
  $('#again').onclick=()=>{S=build(S.gid);go()};$('#back').onclick=home;mj();window.scrollTo(0,0);
}
fab();
window.__GP={CFG,ITEMS,get S(){return S},build:g=>{S=build(g);go()},parseNum,typesFor,home};
home();
})();
