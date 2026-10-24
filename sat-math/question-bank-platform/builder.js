/* ===== BUILDER: two modules, each with its own topics ===== */
const DOMW={'Algebra':.35,'Advanced Math':.35,'Problem-Solving and Data Analysis':.15,'Geometry and Trigonometry':.15};
const DOMS=Object.keys(DOMW);
const DOMSHORT={'Algebra':'Algebra','Advanced Math':'Advanced Math','Problem-Solving and Data Analysis':'Problem-Solving & Data Analysis','Geometry and Trigonometry':'Geometry & Trigonometry'};
const SKEY=it=>it.domain+'|'+it.skill+'|'+(it.sub||'General');
const ALLKEYS=[...new Set(BANK.map(SKEY))].sort((a,b)=>DOMS.indexOf(a.split('|')[0])-DOMS.indexOf(b.split('|')[0])||a.localeCompare(b));
let B={sk:[new Set(ALLKEYS),new Set(ALLKEYS)],tab:0,lv:['M','H'],fmt:'all',n:25,mins:'',balance:true,seed:(Date.now()%1e9)|0,title:'SAT Math full mock exam',preset:'full',proc:true,maxLeave:3,seb:false,avoid:true};
function rng(seed){let a=seed>>>0;return()=>{a=(a+0x6D2B79F5)>>>0;let t=a;t=Math.imul(t^t>>>15,t|1);t^=t+Math.imul(t^t>>>7,t|61);return((t^t>>>14)>>>0)/4294967296}}
function shuf(a,r){a=a.slice();for(let i=a.length-1;i>0;i--){const j=Math.floor(r()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a}
function allocate(list,count,r){
  count=Math.min(count,list.length); if(count<=0)return [];
  if(!B.balance)return shuf(list,r).slice(0,count);
  const by={};list.forEach(it=>(by[it.domain]=by[it.domain]||[]).push(it));
  const doms=Object.keys(by),sw=doms.reduce((a,d)=>a+DOMW[d],0),al={};let used=0;
  doms.forEach(d=>{al[d]=Math.min(by[d].length,Math.floor(count*DOMW[d]/sw));used+=al[d]});
  let guard=0;while(used<count&&guard++<1000){
    const d=doms.filter(d=>al[d]<by[d].length).sort((a,b)=>(count*DOMW[b]/sw-al[b])-(count*DOMW[a]/sw-al[a]))[0];if(!d)break;al[d]++;used++}
  let out=[];doms.forEach(d=>{out=out.concat(shuf(by[d],r).slice(0,al[d]))});
  return shuf(out,r)}
function draw(list,count,r){
  if(B.fmt!=='all')return allocate(list,count,r);
  const ns=Math.round(count*.27);let S=allocate(list.filter(i=>!i.mc),ns,r);let Mc=allocate(list.filter(i=>i.mc),count-S.length,r);
  const miss=count-S.length-Mc.length;if(miss>0){const used=new Set(S.concat(Mc).map(i=>i.id));Mc=Mc.concat(allocate(list.filter(i=>!used.has(i.id)),miss,r))}
  return shuf(Mc.filter(i=>i.mc),r).concat(shuf(S.concat(Mc.filter(i=>!i.mc)),r))}
/* questions already seen on this device (by family, so a rephrased twin counts as seen) */
const FAM=id=>id.replace(/-2$/,'');
let SEEN=new Set();try{SEEN=new Set(JSON.parse(localStorage.getItem('aceit_seen')||'[]'))}catch(e){}
function saveSeen(){try{localStorage.setItem('aceit_seen',JSON.stringify([...SEEN]))}catch(e){}}
function markSeen(items){(items||[]).forEach(i=>SEEN.add(FAM(i.id)));saveSeen()}
const FAMN=new Set(BANK.map(i=>FAM(i.id))).size;
function pickN(base,count,r,used){
  if(count<=0)return [];
  const sf=new Set(),L=shuf(base,r).filter(i=>{const f=FAM(i.id);if(used.has(f)||sf.has(f))return false;sf.add(f);return true});
  const fresh=B.avoid?L.filter(i=>!SEEN.has(FAM(i.id))):L;
  let out=draw(fresh,Math.min(count,fresh.length),r);
  if(out.length<count&&B.avoid){const ids=new Set(out.map(i=>i.id));out=out.concat(draw(L.filter(i=>!ids.has(i.id)),count-out.length,r))}
  out.forEach(i=>used.add(FAM(i.id)));
  return out.filter(i=>i.mc).concat(out.filter(i=>!i.mc));
}
function pool(m){return BANK.filter(it=>B.sk[m].has(SKEY(it))&&(B.lv[m]==='MH'||it.lv===B.lv[m])&&(B.fmt==='all'||(B.fmt==='mc')===it.mc))}
function makeExam(){
  const r=rng(B.seed),used=new Set();
  const m=[0,1].map(i=>pickN(pool(i),B.n,r,used)).map(x=>x.filter(i=>i.mc).concat(x.filter(i=>!i.mc)));
  const mi=parseFloat(B.mins),secs=m.map(x=>mi>0?Math.round(mi*60):Math.round(x.length*95.45));
  return {mods:m,secs,title:B.title||'SAT Math exam',pr:{on:!!B.proc,max:+B.maxLeave||0,seb:!!B.seb}}}
const b64=s=>btoa(unescape(encodeURIComponent(s))).replace(/\+/g,'-').replace(/\//g,'_').replace(/=+$/,'');
const unb64=s=>decodeURIComponent(escape(atob(s.replace(/-/g,'+').replace(/_/g,'/'))));
function presetFrom(ex){return {m:ex.mods.map(x=>x.map(i=>i.id)),s:ex.secs,t:ex.title,pr:ex.pr}}
function examFromPreset(p){const byId={};BANK.forEach(i=>byId[i.id]=i);const m=p.m.map(l=>l.map(id=>byId[id]).filter(Boolean)).filter(l=>l.length);return {mods:m,secs:p.s.slice(0,m.length),title:p.t||'SAT Math exam',pr:p.pr||{on:false,max:3,seb:false}}}
function counts(ex){const c={},lv={M:0,H:0};ex.mods.flat().forEach(i=>{c[i.domain]=(c[i.domain]||0)+1;lv[i.lv]++});return {c,lv,n:ex.mods.flat().length}}
const PRESETS={
 full:{label:'Full mock',sub:'2 modules · Medium then Hard · all topics',set:()=>{B.sk=[new Set(ALLKEYS),new Set(ALLKEYS)];B.lv=['M','H'];B.fmt='all';B.n=25;B.mins='';B.balance=true;B.title='SAT Math full mock exam';B.proc=true}},
 hard:{label:'Hard only',sub:'2 modules · Hard · all topics',set:()=>{B.sk=[new Set(ALLKEYS),new Set(ALLKEYS)];B.lv=['H','H'];B.fmt='all';B.n=25;B.mins='';B.balance=true;B.title='SAT Math hard exam';B.proc=true}},
 plan:{label:'Current topic + review',sub:'Module 1: topics you pick · Module 2: all topics',set:()=>{B.sk=[new Set(),new Set(ALLKEYS)];B.tab=0;B.lv=['MH','MH'];B.fmt='all';B.n=25;B.mins='';B.balance=true;B.title='Current topic + cumulative review';B.proc=true}}
};
function builder(){
  const ex=makeExam(),cn=counts(ex),m=B.tab,SK=B.sk[m];
  const byDom={};ALLKEYS.forEach(k=>{const [d,sk,sb]=k.split('|');((byDom[d]=byDom[d]||{})[sk]=byDom[d][sk]||[]).push(sb)});
  const domHTML=DOMS.map(d=>{const sks=byDom[d]||{};const dk=ALLKEYS.filter(k=>k.startsWith(d+'|'));const on=dk.filter(k=>SK.has(k)).length;
    const skHTML=Object.keys(sks).map(sk=>{const kk=sks[sk].map(sb=>d+'|'+sk+'|'+sb);const o2=kk.filter(k=>SK.has(k)).length;
      return `<details class="skg" ${o2&&o2<kk.length?'open':''}><summary><label><input type="checkbox" data-skill="${d}|${sk}" ${o2===kk.length?'checked':''} ${o2&&o2<kk.length?'data-part="1"':''}> <b>${sk}</b></label></summary><div class="subs">${sks[sk].map(sb=>`<label class="sk"><input type="checkbox" data-sk="${d}|${sk}|${sb}" ${SK.has(d+'|'+sk+'|'+sb)?'checked':''}> ${sb}</label>`).join('')}</div></details>`}).join('');
    return `<details class="dom" ${on&&on<dk.length?'open':''}><summary><label><input type="checkbox" data-dom="${d}" ${on===dk.length?'checked':''} ${on&&on<dk.length?'data-part="1"':''}> <b>${DOMSHORT[d]}</b></label></summary><div class="sks">${skHTML}</div></details>`}).join('');
  const ok=[0,1].every(i=>ex.mods[i]&&ex.mods[i].length);
  const warns=[0,1].map(i=>{const P=pool(i);return !B.sk[i].size?`Module ${i+1}: no topics selected.`:!P.length?`Module ${i+1}: no questions match these topics.`:P.length<B.n?`Module ${i+1}: only ${P.length} questions match, so it is shorter than ${B.n}.`:''}).filter(Boolean);
  const dsum=l=>DOMS.map(d=>[d,l.filter(i=>i.domain===d).length]).filter(x=>x[1]).map(x=>DOMSHORT[x[0]]+' '+x[1]).join(' · ');
  const lvLab={M:'Medium',H:'Hard',MH:'Mixed'};
  const segLv=i=>`<div><label>Module ${i+1} difficulty</label><div class="seg" data-g="lv${i}">${[['M','Medium'],['H','Hard'],['MH','Mixed']].map(([v,l])=>`<button data-v="${v}" aria-pressed="${B.lv[i]===v}">${l}</button>`).join('')}</div></div>`;
  $('#app').innerHTML=`<div class="page bld" style="overflow:auto"><div class="eyebrow">Mr Malek Thiab · SAT Math Mastery</div><h1>SAT Aceit Exam Builder</h1>
  <p class="lede">Practice the digital SAT Math section the way you will meet it on test day. The exam is made of two timed modules that mix multiple-choice and student-produced (grid-in) questions from four domains: Algebra, Advanced Math, Problem-Solving and Data Analysis, and Geometry and Trigonometry. On every question you can use the built-in Desmos calculator and the reference sheet, mark a question for review, and cross out answer choices. Choose the topics for each module, then set the difficulty and length. The builder draws a fresh exam each time, and the score report gives an estimated Math score band and shows what to practise next.</p>
  <h2>Start from</h2><div class="presets">${Object.entries(PRESETS).map(([k,p])=>`<button class="preset ${B.preset===k?'on':''}" data-p="${k}"><b>${p.label}</b><span>${p.sub}</span></button>`).join('')}</div>
  <h2>Topics</h2>
  <div class="segt" role="tablist">${[0,1].map(i=>`<button data-tab="${i}" role="tab" aria-pressed="${m===i}">Module ${i+1} <small>${B.sk[i].size} of ${ALLKEYS.length} subtopics</small></button>`).join('')}</div>
  <div class="row" style="margin:10px 0 8px"><button class="chip" id="allT">Select all</button><button class="chip" id="noT">Clear</button><button class="chip" id="openT">Open all</button><button class="chip" id="closeT">Close all</button><button class="chip" id="copyT">Copy to Module ${m?1:2}</button></div>${domHTML}
  <h2>Settings</h2><div class="set">
   ${segLv(0)}${segLv(1)}
   <div><label>Format</label><div class="seg" data-g="fmt">${[['all','All'],['mc','Multiple choice'],['spr','Grid-in']].map(([v,l])=>`<button data-v="${v}" aria-pressed="${B.fmt===v}">${l}</button>`).join('')}</div></div>
   <div><label for="nq">Questions per module</label><input id="nq" type="number" min="4" max="50" value="${B.n}"></div>
   <div><label for="mn">Minutes per module <small>(blank = about 1 min 35 s per question)</small></label><input id="mn" type="number" min="1" max="120" value="${B.mins}" placeholder="auto"></div>
   <div><label class="chk"><input type="checkbox" id="bal" ${B.balance?'checked':''}> Balance topics like the real SAT (Algebra 35%, Advanced Math 35%, Problem-Solving 15%, Geometry 15%)</label></div>
   <div><label class="chk"><input type="checkbox" id="avoid" ${B.avoid?'checked':''}> Avoid questions I have already seen</label><div class="small">Seen so far: <b>${SEEN.size}</b> of ${FAMN} <button class="chip" id="rstSeen">Reset history</button></div></div>
  </div>
  <h2>Exam integrity</h2><div class="set">
   <div><label class="chk"><input type="checkbox" id="proc" ${B.proc?'checked':''}> Proctor mode: fullscreen, tab-switch detection, copy and right-click off, integrity report</label></div>
   <div><label for="mxl">Auto-submit on leave number</label><select id="mxl" ${B.proc?'':'disabled'}>${[[0,'Never (warn and report only)'],[2,'2nd leave'],[3,'3rd leave (recommended)'],[5,'5th leave']].map(([v,l])=>`<option value="${v}" ${+B.maxLeave===v?'selected':''}>${l}</option>`).join('')}</select></div>
   <div><label class="chk"><input type="checkbox" id="seb" ${B.seb?'checked':''} ${B.proc?'':'disabled'}> Require Safe Exam Browser</label></div></div>
  <div class="sum ${warns.length?'warn':''}"><b>${cn.n} questions</b> · 2 modules, ${ex.secs.map(s=>Math.round(s/60)+' min').join(' + ')}${[0,1].map(i=>`<br><span>Module ${i+1} (${lvLab[B.lv[i]]}): ${(ex.mods[i]||[]).length} questions · ${dsum(ex.mods[i]||[])||'no questions'}</span>`).join('')}${warns.map(w=>`<br><span>${w}</span>`).join('')}</div>
  <div class="row" style="margin-top:16px"><button class="btn primary" id="startB" style="font-size:1.05rem;padding:11px 34px" ${ok?'':'disabled'}>Start exam</button>
   <button class="btn ghost" id="reshuf">New draw</button><button class="btn ghost" id="shareB" ${ok?'':'disabled'}>Copy exam link</button><button class="btn ghost" id="dlB" ${ok?'':'disabled'}>Download exam file</button><button class="btn ghost" id="refB">Reference sheet</button></div>
  <p class="meta" id="msg" style="color:var(--muted);font-size:.86rem;min-height:1.4em"></p></div>`;
  bindBuilder();
}
function bindBuilder(){
  const SK=()=>B.sk[B.tab];
  document.querySelectorAll('.preset').forEach(b=>b.onclick=()=>{PRESETS[b.dataset.p].set();B.preset=b.dataset.p;B.seed=(Date.now()%1e9)|0;builder()});
  document.querySelectorAll('[data-tab]').forEach(b=>b.onclick=()=>{B.tab=+b.dataset.tab;builder()});
  document.querySelectorAll('[data-dom]').forEach(c=>{if(c.dataset.part)c.indeterminate=true;c.onchange=()=>{const d=c.dataset.dom;ALLKEYS.filter(k=>k.startsWith(d+'|')).forEach(k=>c.checked?SK().add(k):SK().delete(k));B.preset='';builder()}});
  document.querySelectorAll('[data-skill]').forEach(c=>{if(c.dataset.part)c.indeterminate=true;c.onchange=()=>{const p=c.dataset.skill+'|';ALLKEYS.filter(k=>k.startsWith(p)).forEach(k=>c.checked?SK().add(k):SK().delete(k));B.preset='';builder()}});
  document.querySelectorAll('[data-sk]').forEach(c=>c.onchange=()=>{c.checked?SK().add(c.dataset.sk):SK().delete(c.dataset.sk);B.preset='';builder()});
  $('#allT').onclick=()=>{B.sk[B.tab]=new Set(ALLKEYS);B.preset='';builder()};$('#noT').onclick=()=>{B.sk[B.tab]=new Set();B.preset='';builder()};
  $('#openT').onclick=()=>document.querySelectorAll('details.dom,details.skg').forEach(d=>d.open=true);$('#closeT').onclick=()=>document.querySelectorAll('details.dom,details.skg').forEach(d=>d.open=false);
  $('#copyT').onclick=()=>{B.sk[B.tab?0:1]=new Set(B.sk[B.tab]);B.preset='';builder()};
  document.querySelectorAll('.seg').forEach(g=>g.querySelectorAll('button').forEach(b=>b.onclick=()=>{const v=b.dataset.v,k=g.dataset.g;if(k==='lv0'||k==='lv1')B.lv[+k[2]]=v;else B[k]=v;B.preset='';builder()}));
  $('#nq').onchange=e=>{B.n=Math.max(4,Math.min(50,parseInt(e.target.value)||25));B.preset='';builder()};
  $('#mn').onchange=e=>{B.mins=e.target.value;builder()};
  $('#bal').onchange=e=>{B.balance=e.target.checked;builder()};
  $('#avoid').onchange=e=>{B.avoid=e.target.checked;builder()};$('#rstSeen').onclick=()=>{SEEN=new Set();saveSeen();builder()};
  $('#proc').onchange=e=>{B.proc=e.target.checked;builder()};$('#mxl').onchange=e=>{B.maxLeave=+e.target.value};$('#seb').onchange=e=>{B.seb=e.target.checked};
  $('#reshuf').onclick=()=>{B.seed=(Date.now()%1e9)|0;builder()};
  $('#refB').onclick=()=>{S.modal='ref';modal()};
  $('#startB').onclick=()=>{EXAM=makeExam();resetState();startExam()};
  $('#shareB').onclick=()=>{const ex=makeExam();const url=location.href.split('#')[0]+'#x='+b64(JSON.stringify(presetFrom(ex)));
    const show=()=>{$('#msg').innerHTML='Copy this link: <input style="width:60%" readonly value="'+url+'">'};
    (navigator.clipboard&&navigator.clipboard.writeText?navigator.clipboard.writeText(url).then(()=>{$('#msg').textContent='Link copied.'},show):Promise.reject()).catch(show)};
  $('#dlB').onclick=()=>{const ex=makeExam(),ids=new Set(ex.mods.flat().map(i=>i.id));const sub=BANK.filter(i=>ids.has(i.id));
    const safe=s=>s.replace(/<\//g,'<\\/').replace(/<\x21--/g,'<\\u0021--');
    let h=SRC.replace(/(<script type="application\/json" id="bankdata">)[\s\S]*?(<\/script>)/,(m,a,b)=>a+safe(JSON.stringify(sub0(sub)))+b);
    h=h.replace('const PRESET=null;/*P*/','const PRESET='+JSON.stringify(presetFrom(ex))+';/*P*/');
    const blob=new Blob([h],{type:'text/html'});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='SAT_Aceit_'+counts(ex).n+'Q_exam.html';document.body.appendChild(a);a.click();setTimeout(()=>{URL.revokeObjectURL(a.href);a.remove()},500);
    $('#msg').textContent='Exam file downloaded.'};
}
window.__sat2={get B(){return B},get SEEN(){return SEEN},markSeen,FAM,makeExam}; /* test handle */
