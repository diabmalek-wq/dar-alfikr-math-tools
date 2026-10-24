t=open('tpl_src.html').read()
def rep(old,new,count=1):
    global t
    assert old in t, old[:60]
    t=t.replace(old,new,count)

# ---- data block
a=t.index('/* ===== DATA ===== */'); b=t.index("const CFG=")
t=t[:a]+'''/* ===== DATA ===== */
const RAW=JSON.parse(document.getElementById('bankdata').textContent);
const BANK=JSON.parse(document.getElementById('bankdata').textContent);
const PRESET=null;/*P*/
/* escape < > & inside $...$ so innerHTML cannot read "$AD<DB$" as a tag */
(function(){const f=s=>typeof s!=='string'?s:s.replace(/\\$\\$[^$]+\\$\\$|\\$[^$]+\\$/g,m=>m.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'));
 BANK.forEach(it=>{it.q=f(it.q);if(it.opts)it.opts=it.opts.map(f);it.steps=it.steps.map(f);if(it.disp)it.disp=it.disp})})();
const FIGS={};
'''+t[b:]
rep("<div id=\"app\"></div>\n<script>","<div id=\"app\"></div>\n<script type=\"application/json\" id=\"bankdata\">/*BANK*/[]</script>\n<script>")
rep("moduleSeconds:35*60,desmosTest","desmosTest")
# ---- state
rep("const S={phase:'intro',mod:0,i:0,ans:[[],[]],flag:[[],[]],elim:[[],[]],time:[[],[]],left:[CFG.moduleSeconds,CFG.moduleSeconds],\n  hideTimer:false,calc:false,mapOpen:false,modal:null,last:Date.now(),tick:null};\nconst mods=()=>[DATA.m1,DATA.m2];",
"const SRC='<!doctype html>'+document.documentElement.outerHTML;\nlet EXAM=null;\nconst S={phase:'intro',mod:0,i:0,ans:[],flag:[],elim:[],time:[],left:[],hideTimer:false,calc:false,mapOpen:false,modal:null,last:Date.now(),tick:null};\nconst mods=()=>EXAM.mods;\nfunction resetState(){Object.assign(S,{phase:'intro',mod:0,i:0,ans:EXAM.mods.map(()=>[]),flag:EXAM.mods.map(()=>[]),elim:EXAM.mods.map(()=>[]),time:EXAM.mods.map(()=>[]),left:EXAM.secs.slice(),mapOpen:false,modal:null,calc:S.calc});filter='all'}")
# ---- intro -> builder/start (replace intro() through startModule start)
a=t.index("function intro(){"); b=t.index("function startModule(m){")
builder=r'''
const DOMW={'Algebra':.35,'Advanced Math':.35,'Problem-Solving and Data Analysis':.15,'Geometry and Trigonometry':.15};
const DOMS=Object.keys(DOMW);
const DOMSHORT={'Algebra':'Algebra','Advanced Math':'Advanced Math','Problem-Solving and Data Analysis':'Problem-Solving & Data Analysis','Geometry and Trigonometry':'Geometry & Trigonometry'};
const SKEY=it=>it.domain+'|'+it.skill+'|'+(it.sub||'General');
const ALLKEYS=[...new Set(BANK.map(SKEY))].sort((a,b)=>DOMS.indexOf(a.split('|')[0])-DOMS.indexOf(b.split('|')[0])||a.localeCompare(b));
let B={sk:new Set(ALLKEYS),lv:'MH',fmt:'all',n:44,modules:2,mins:'',balance:true,seed:(Date.now()%1e9)|0,title:'Custom SAT Math exam',preset:'full'};
function rng(seed){let a=seed>>>0;return()=>{a=(a+0x6D2B79F5)>>>0;let t=a;t=Math.imul(t^t>>>15,t|1);t^=t+Math.imul(t^t>>>7,t|61);return((t^t>>>14)>>>0)/4294967296}}
function shuf(a,r){a=a.slice();for(let i=a.length-1;i>0;i--){const j=Math.floor(r()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a}
function pool(extra){return BANK.filter(it=>B.sk.has(SKEY(it))&&(B.lv==='MH'||it.lv===B.lv)&&(B.fmt==='all'||(B.fmt==='mc')===it.mc)&&(!extra||extra(it)))}
function allocate(list,count,r){ // pick `count` items from list, domain-weighted when B.balance
  count=Math.min(count,list.length); if(count<=0)return [];
  if(!B.balance)return shuf(list,r).slice(0,count);
  const by={};list.forEach(it=>(by[it.domain]=by[it.domain]||[]).push(it));
  const doms=Object.keys(by); const sw=doms.reduce((a,d)=>a+DOMW[d],0);
  const al={};let used=0;doms.forEach(d=>{al[d]=Math.min(by[d].length,Math.floor(count*DOMW[d]/sw));used+=al[d]});
  let guard=0;while(used<count&&guard++<1000){ // hand out the rest by largest unmet share
    const d=doms.filter(d=>al[d]<by[d].length).sort((a,b)=>(count*DOMW[b]/sw-al[b])-(count*DOMW[a]/sw-al[a]))[0]; if(!d)break; al[d]++;used++}
  let out=[];doms.forEach(d=>{out=out.concat(shuf(by[d],r).slice(0,al[d]))});
  return shuf(out,r)}
function draw(list,count,r){
  if(B.fmt!=='all')return allocate(list,count,r);
  const ns=Math.round(count*.27);let S=allocate(list.filter(i=>!i.mc),ns,r);let Mc=allocate(list.filter(i=>i.mc),count-S.length,r);
  const miss=count-S.length-Mc.length;if(miss>0){const used=new Set(S.concat(Mc).map(i=>i.id));Mc=Mc.concat(allocate(list.filter(i=>!used.has(i.id)),miss,r))}
  return shuf(Mc.filter(i=>i.mc),r).concat(shuf(S.concat(Mc.filter(i=>!i.mc)),r))}
function makeExam(){
  const r=rng(B.seed),n=B.n;let m;
  if(B.lv==='MH'){const nm=Math.floor(n/2);let M=draw(pool(i=>i.lv==='M'),nm,r),H=draw(pool(i=>i.lv==='H'),n-nm,r);
    {const u=new Set(M.concat(H).map(i=>i.id));const need=n-M.length-H.length;if(need>0){const ex=draw(pool(i=>!u.has(i.id)),need,r);M=M.concat(ex.filter(i=>i.lv==='M'));H=H.concat(ex.filter(i=>i.lv!=='M'))}}
    m=B.modules===2?[M,H]:[M.concat(H)]}
  else{if(B.modules===2){const P0=pool(),a1=draw(P0,Math.ceil(n/2),r),u=new Set(a1.map(i=>i.id));m=[a1,draw(P0.filter(i=>!u.has(i.id)),Math.floor(n/2),r)]}else m=[draw(pool(),n,r)]}
  m=m.filter(x=>x.length);
  const secs=m.map(x=>{const mi=parseFloat(B.mins);return mi>0?Math.round(mi*60):Math.round(x.length*95.45)});
  return {mods:m,secs,title:B.title||'Custom SAT Math exam'}}
const b64=s=>btoa(unescape(encodeURIComponent(s))).replace(/\+/g,'-').replace(/\//g,'_').replace(/=+$/,'');
const unb64=s=>decodeURIComponent(escape(atob(s.replace(/-/g,'+').replace(/_/g,'/'))));
function presetFrom(ex){return {m:ex.mods.map(x=>x.map(i=>i.id)),s:ex.secs,t:ex.title}}
function examFromPreset(p){const byId={};BANK.forEach(i=>byId[i.id]=i);const m=p.m.map(l=>l.map(id=>byId[id]).filter(Boolean)).filter(l=>l.length);return {mods:m,secs:p.s.slice(0,m.length),title:p.t||'SAT Math exam'}}
function counts(ex){const c={},lv={M:0,H:0};ex.mods.flat().forEach(i=>{c[i.domain]=(c[i.domain]||0)+1;lv[i.lv]++});return {c,lv,n:ex.mods.flat().length}}
const PRESETS={
 full:{label:'Full mock',sub:'44 Q · 2 modules · Medium then Hard · SAT weights',set:()=>{B.sk=new Set(ALLKEYS);B.lv='MH';B.fmt='all';B.n=44;B.modules=2;B.mins='';B.balance=true;B.title='SAT Math full mock exam'}},
 module:{label:'One module',sub:'22 Q · 35 min · mixed topics',set:()=>{B.sk=new Set(ALLKEYS);B.lv='MH';B.fmt='all';B.n=22;B.modules=1;B.mins='';B.balance=true;B.title='SAT Math module'}},
 hard:{label:'Hard only',sub:'22 Q · Hard · mixed topics',set:()=>{B.sk=new Set(ALLKEYS);B.lv='H';B.fmt='all';B.n=22;B.modules=1;B.mins='';B.balance=true;B.title='SAT Math hard module'}},
 topic:{label:'Topic drill',sub:'pick topics below · 15 Q',set:()=>{B.lv='MH';B.fmt='all';B.n=15;B.modules=1;B.mins='';B.balance=false;B.title='SAT Math topic drill'}}
};
function builder(){
  const P=pool(),ex=makeExam(),cn=counts(ex);
  const byDom={};ALLKEYS.forEach(k=>{const [d,sk,sb]=k.split('|');((byDom[d]=byDom[d]||{})[sk]=byDom[d][sk]||[]).push(sb)});
  const avail=k=>BANK.filter(it=>SKEY(it)===k&&(B.lv==='MH'||it.lv===B.lv)&&(B.fmt==='all'||(B.fmt==='mc')===it.mc)).length;
  const cnt=ks=>ks.reduce((a,k)=>a+avail(k),0);
  const domHTML=DOMS.map(d=>{const sks=byDom[d]||{};const dk=ALLKEYS.filter(k=>k.startsWith(d+'|'));const on=dk.filter(k=>B.sk.has(k)).length;
    const skHTML=Object.keys(sks).map(sk=>{const kk=sks[sk].map(sb=>d+'|'+sk+'|'+sb);const o2=kk.filter(k=>B.sk.has(k)).length;
      return `<details class="skg" ${o2&&o2<kk.length?'open':''}><summary><label><input type="checkbox" data-skill="${d}|${sk}" ${o2===kk.length?'checked':''} ${o2&&o2<kk.length?'data-part="1"':''}> <b>${sk}</b></label><span class="cnt">${cnt(kk)}</span></summary><div class="subs">${sks[sk].map(sb=>`<label class="sk"><input type="checkbox" data-sk="${d}|${sk}|${sb}" ${B.sk.has(d+'|'+sk+'|'+sb)?'checked':''}> ${sb} <span class="cnt">${avail(d+'|'+sk+'|'+sb)}</span></label>`).join('')}</div></details>`}).join('');
    return `<details class="dom" ${on&&on<dk.length?'open':''}><summary><label><input type="checkbox" data-dom="${d}" ${on===dk.length?'checked':''} ${on&&on<dk.length?'data-part="1"':''}> <b>${DOMSHORT[d]}</b></label><span class="cnt">${cnt(dk)} questions</span></summary>
      <div class="sks">${skHTML}</div></details>`}).join('');
  const short=P.length<B.n;
  $('#app').innerHTML=`<div class="page bld" style="overflow:auto"><div class="eyebrow">Mr Malek Thiab · SAT Math Mastery</div><h1>SAT Aceit Exam Builder</h1>
  <p class="lede">${BANK.length.toLocaleString()} rephrased, answer-verified questions. Pick the topics, difficulty and length, and the builder draws a fresh exam each time. It runs like Bluebook with the Desmos calculator, the reference sheet and a 40-point expected score band.</p>
  <h2>Start from</h2><div class="presets">${Object.entries(PRESETS).map(([k,p])=>`<button class="preset ${B.preset===k?'on':''}" data-p="${k}"><b>${p.label}</b><span>${p.sub}</span></button>`).join('')}</div>
  <h2>Topics</h2><p class="hint">Tick a domain for everything in it, or click the arrow on its row to open the skills and subtopics (for example Circles &rarr; Tangent lines) and tick only the ones you want.</p><div class="row" style="margin:0 0 8px"><button class="chip" id="allT">Select all</button><button class="chip" id="noT">Clear</button><button class="chip" id="openT">Open all</button><button class="chip" id="closeT">Close all</button></div>${domHTML}
  <h2>Settings</h2><div class="set">
   <div><label>Difficulty</label><div class="seg" data-g="lv">${[['M','Medium'],['H','Hard'],['MH','Both']].map(([v,l])=>`<button data-v="${v}" aria-pressed="${B.lv===v}">${l}</button>`).join('')}</div></div>
   <div><label>Format</label><div class="seg" data-g="fmt">${[['all','All'],['mc','Multiple choice'],['spr','Grid-in']].map(([v,l])=>`<button data-v="${v}" aria-pressed="${B.fmt===v}">${l}</button>`).join('')}</div></div>
   <div><label>Modules</label><div class="seg" data-g="modules">${[[1,'1'],[2,'2 (Medium then Hard)']].map(([v,l])=>`<button data-v="${v}" aria-pressed="${B.modules===v}">${l}</button>`).join('')}</div></div>
   <div><label for="nq">Number of questions</label><input id="nq" type="number" min="4" max="100" value="${B.n}"></div>
   <div><label for="mn">Minutes per module <small>(blank = about 1 min 35 s per question)</small></label><input id="mn" type="number" min="1" max="120" value="${B.mins}" placeholder="auto"></div>
   <div><label class="chk"><input type="checkbox" id="bal" ${B.balance?'checked':''}> Balance topics like the real SAT (Algebra 35%, Advanced Math 35%, Problem-Solving 15%, Geometry 15%)</label></div>
  </div>
  <div class="sum ${short?'warn':''}"><b>${cn.n} questions</b> · ${cn.lv.M} Medium + ${cn.lv.H} Hard · ${ex.mods.length} module${ex.mods.length>1?'s':''}, ${ex.secs.map(s=>Math.round(s/60)+' min').join(' + ')}<br><span>${DOMS.filter(d=>cn.c[d]).map(d=>DOMSHORT[d]+' '+cn.c[d]).join(' · ')||'no questions match'}</span>${short?`<br><span>Only ${P.length} questions match these filters, so the exam is shorter than ${B.n}.</span>`:''}</div>
  <div class="row" style="margin-top:16px"><button class="btn primary" id="startB" style="font-size:1.05rem;padding:11px 34px" ${cn.n?'':'disabled'}>Start exam</button>
   <button class="btn ghost" id="reshuf">New draw</button><button class="btn ghost" id="shareB" ${cn.n?'':'disabled'}>Copy exam link</button><button class="btn ghost" id="dlB" ${cn.n?'':'disabled'}>Download exam file</button><button class="btn ghost" id="refB">Reference sheet</button></div>
  <p class="meta" id="msg" style="color:var(--muted);font-size:.86rem;min-height:1.4em"></p>
  <div class="note">The draw is random but repeatable: the same link or file always opens the same questions. Every question keeps the answer verified in the bank. Scores here are estimates, not official scores.</div></div>`;
  bindBuilder();
}
function bindBuilder(){
  document.querySelectorAll('.preset').forEach(b=>b.onclick=()=>{PRESETS[b.dataset.p].set();B.preset=b.dataset.p;B.seed=(Date.now()%1e9)|0;builder()});
  document.querySelectorAll('[data-dom]').forEach(c=>{if(c.dataset.part)c.indeterminate=true;c.onchange=()=>{const d=c.dataset.dom;ALLKEYS.filter(k=>k.startsWith(d+'|')).forEach(k=>c.checked?B.sk.add(k):B.sk.delete(k));B.preset='';builder()}});
  document.querySelectorAll('[data-skill]').forEach(c=>{if(c.dataset.part)c.indeterminate=true;c.onchange=()=>{const p=c.dataset.skill+'|';ALLKEYS.filter(k=>k.startsWith(p)).forEach(k=>c.checked?B.sk.add(k):B.sk.delete(k));B.preset='';builder()}});
  document.querySelectorAll('[data-sk]').forEach(c=>c.onchange=()=>{c.checked?B.sk.add(c.dataset.sk):B.sk.delete(c.dataset.sk);B.preset='';builder()});
  $('#allT').onclick=()=>{B.sk=new Set(ALLKEYS);builder()};$('#openT').onclick=()=>document.querySelectorAll('details.dom,details.skg').forEach(d=>d.open=true);$('#closeT').onclick=()=>document.querySelectorAll('details.dom,details.skg').forEach(d=>d.open=false);$('#noT').onclick=()=>{B.sk=new Set();builder()};
  document.querySelectorAll('.seg').forEach(g=>g.querySelectorAll('button').forEach(b=>b.onclick=()=>{const v=b.dataset.v;B[g.dataset.g]=g.dataset.g==='modules'?+v:v;B.preset='';builder()}));
  $('#nq').onchange=e=>{B.n=Math.max(4,Math.min(100,parseInt(e.target.value)||44));B.preset='';builder()};
  $('#mn').onchange=e=>{B.mins=e.target.value;builder()};
  $('#bal').onchange=e=>{B.balance=e.target.checked;builder()};
  $('#reshuf').onclick=()=>{B.seed=(Date.now()%1e9)|0;builder()};
  $('#refB').onclick=()=>{S.modal='ref';modal()};
  $('#startB').onclick=()=>{EXAM=makeExam();resetState();startExam()};
  $('#shareB').onclick=()=>{const ex=makeExam();const url=location.href.split('#')[0]+'#x='+b64(JSON.stringify(presetFrom(ex)));
    const done=()=>{$('#msg').textContent='Link copied. Anyone with the same file opens these '+counts(ex).n+' questions.'};
    (navigator.clipboard&&navigator.clipboard.writeText?navigator.clipboard.writeText(url).then(done,()=>{$('#msg').innerHTML='Copy this link: <input style="width:60%" readonly value="'+url+'">'}):Promise.reject()).catch(()=>{$('#msg').innerHTML='Copy this link: <input style="width:60%" readonly value="'+url+'">'})};
  $('#dlB').onclick=()=>{const ex=makeExam(),ids=new Set(ex.mods.flat().map(i=>i.id));const sub=BANK.filter(i=>ids.has(i.id));
    const safe=s=>s.replace(/<\//g,'<\\/').replace(/<\x21--/g,'<\\u0021--');
    let h=SRC.replace(/(<script type="application\/json" id="bankdata">)[\s\S]*?(<\/script>)/,(m,a,b)=>a+safe(JSON.stringify(sub0(sub)))+b);
    h=h.replace('const PRESET=null;/*P*/','const PRESET='+JSON.stringify(presetFrom(ex))+';/*P*/');
    const blob=new Blob([h],{type:'text/html'});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='SAT_Aceit_'+counts(ex).n+'Q_exam.html';document.body.appendChild(a);a.click();setTimeout(()=>{URL.revokeObjectURL(a.href);a.remove()},500);
    $('#msg').textContent='Exam file downloaded: '+counts(ex).n+' questions.'};
}
function sub0(arr){return RAW.filter(i=>arr.some(a=>a.id===i.id))} // original (unescaped) items for export
function startPage(){
  const cn=counts(EXAM);
  $('#app').innerHTML=`<div class="page" style="overflow:auto"><div class="eyebrow">Mr Malek Thiab · SAT Math Mastery</div><h1>${EXAM.title}</h1>
  <p class="lede">${cn.n} questions across ${EXAM.mods.length} module${EXAM.mods.length>1?'s':''}. It runs like Bluebook: timed modules, the Desmos calculator, a reference sheet, flagging and answer elimination.</p>
  <div class="facts"><div class="fact"><b>${cn.n}</b><span>questions · ${cn.lv.M} Medium + ${cn.lv.H} Hard</span></div><div class="fact"><b>${EXAM.secs.map(s=>mmss(s)).join(' + ')}</b><span>time per module</span></div><div class="fact"><b>Desmos</b><span>open on every question</span></div><div class="fact"><b>${DOMS.filter(d=>cn.c[d]).length}</b><span>domains covered</span></div></div>
  <h2>Rules</h2><ul class="rules"><li>A module locks when you submit it or when time runs out. You cannot go back to it.</li>
   <li>Multiple-choice questions have one correct answer. For grid-in questions, type a whole number, a decimal or a fraction such as <b>7/4</b>. Up to 5 characters for positive and 6 for negative answers.</li>
   <li>Use <b>Mark for Review</b> to flag a question and the question map to jump around. Keys: <b>←</b> <b>→</b> move, <b>A–D</b> pick an answer.</li></ul>
  <div class="note">Scores here are estimates, not official scores. Questions are Medium and Hard, so they run harder than a typical test.</div>
  <div class="row" style="margin-top:20px"><button class="btn primary" id="go" style="font-size:1.05rem;padding:11px 34px">Start</button><button class="btn ghost" id="refB">Reference sheet</button>${BANK.length>cn.n+60?'<button class="btn ghost" id="bk">Build another exam</button>':''}</div></div>`;
  $('#go').onclick=()=>startExam();$('#refB').onclick=()=>{S.modal='ref';modal()};const bk=$('#bk');if(bk)bk.onclick=()=>{S.phase='intro';EXAM=null;render()};
}
function startExam(){S.phase='exam';S.mod=0;S.i=0;S.last=Date.now();clearInterval(S.tick);S.tick=setInterval(tick,500);render()}
'''
t=t[:a]+builder+t[b:]
rep("function startModule(m){\n  S.phase='exam';","function startModule(m){\n  S.phase='exam';")
# render(): intro handling + header label
rep("  if(S.phase==='intro')return intro();","  if(S.phase==='intro'){if(!EXAM)return builder();return startPage()}")
rep("Section 2, Module ${m+1}: Math</div>","${mods().length>1?'Section 2, Module '+(m+1)+': Math':EXAM.title}</div>")
# between/finish
a=t.index("function finishModule(timeout){"); b=t.index("let filter='all';")
t=t[:a]+r'''function finishModule(timeout){
  clearInterval(S.tick);
  if(S.mod<mods().length-1){S.phase='between';S.timeout=timeout;render()} else {S.phase='results';render()}
}
function between(){
  const nx=S.mod+1,n=mods()[nx].length;
  $('#app').innerHTML=`<div class="page" style="overflow:auto"><div class="rv"><div class="eyebrow">Module ${S.mod+1} submitted</div><h1>${S.timeout?'Time is up for Module '+(S.mod+1):'Take a short break'}</h1>
  <p class="lede">Module ${nx+1} has ${n} questions and ${Math.round(S.left[nx]/60)} minutes on the clock. Once it starts you cannot return to Module ${S.mod+1}.</p>
  <div class="row"><button class="btn primary" id="m2" style="padding:11px 34px">Start Module ${nx+1}</button></div></div></div>`;
  $('#m2').onclick=()=>startModule(nx);
}
'''+t[b:]
# results: rewrite
a=t.index("const PTS=[[0,200]"); b=t.index("document.addEventListener('keydown'")
res=open('results_bank.js').read()
t=t[:a]+res+t[b:]

# ---- PROCTOR layer
proc=open('proctor.js').read()
rep("preset:'full'};","preset:'full',proc:true,maxLeave:3,seb:false};")
rep("return {mods:m,secs,title:B.title||'Custom SAT Math exam'}}","return {mods:m,secs,title:B.title||'Custom SAT Math exam',pr:{on:!!B.proc,max:+B.maxLeave||0,seb:!!B.seb}}}")
rep("function presetFrom(ex){return {m:ex.mods.map(x=>x.map(i=>i.id)),s:ex.secs,t:ex.title}}","function presetFrom(ex){return {m:ex.mods.map(x=>x.map(i=>i.id)),s:ex.secs,t:ex.title,pr:ex.pr}}")
rep("title:p.t||'SAT Math exam'}}","title:p.t||'SAT Math exam',pr:p.pr||{on:false,max:3,seb:false}}}")
for k in ("full","module","hard"):
    rep("B.title='SAT Math "+{"full":"full mock exam","module":"module","hard":"hard module"}[k]+"'}","B.title='SAT Math "+{"full":"full mock exam","module":"module","hard":"hard module"}[k]+"';B.proc=true}")
rep("B.title='SAT Math topic drill'}","B.title='SAT Math topic drill';B.proc=false}")
rep("  <div class=\"sum ${short?'warn':''}\">",r"""  <h2>Exam integrity</h2><div class="set">
   <div><label class="chk"><input type="checkbox" id="proc" ${B.proc?'checked':''}> Proctor mode: fullscreen, tab-switch detection, copy and right-click off, integrity report</label></div>
   <div><label for="mxl">Auto-submit on leave number</label><select id="mxl" ${B.proc?'':'disabled'}>${[[0,'Never (warn and report only)'],[2,'2nd leave'],[3,'3rd leave (recommended)'],[5,'5th leave']].map(([v,l])=>`<option value="${v}" ${+B.maxLeave===v?'selected':''}>${l}</option>`).join('')}</select></div>
   <div><label class="chk"><input type="checkbox" id="seb" ${B.seb?'checked':''} ${B.proc?'':'disabled'}> Require Safe Exam Browser <small>(a normal browser cannot start the exam)</small></label></div></div>
  <p class="hint">A web page cannot block other apps or websites. Proctor mode detects and records leaving the exam. For a true lock, run the exam inside Safe Exam Browser or a Chromebook kiosk (see HOW_TO_PUBLISH.md).</p>
  <div class="sum ${short?'warn':''}">""")
rep("  $('#reshuf').onclick=","  $('#proc').onchange=e=>{B.proc=e.target.checked;builder()};$('#mxl').onchange=e=>{B.maxLeave=+e.target.value};$('#seb').onchange=e=>{B.seb=e.target.checked};\n  $('#reshuf').onclick=")
rep("<div class=\"note\">Scores here are estimates, not official scores. Questions are Medium and Hard, so they run harder than a typical test.</div>","${PROC.startHTML()}<div class=\"note\">Scores here are estimates, not official scores. Questions are Medium and Hard, so they run harder than a typical test.</div>")
rep("function startExam(){S.phase='exam';","function startExam(){if(!PROC.gate())return;PROC.begin();S.phase='exam';")
rep("else {S.phase='results';render()}\n}\nfunction between","else {S.phase='results';PROC.end();render()}\n}\nfunction between")
rep("  <h2>What to do next</h2>","  ${PROC.card()}\n  <h2>What to do next</h2>")
rep("  typeset($('#app'));\n  document.querySelectorAll('.chip')","  typeset($('#app'));PROC.bind();\n  document.querySelectorAll('.chip')")
# define PROC before startExam (inside builder block) 
rep("function startExam(){",proc+"\nfunction startExam(){")


# ---- PLAN layer (no repeats, current topic + cumulative review)
plan=open('plan.js').read()
a=t.index("function makeExam(){"); b=t.index("const b64=s=>")
t=t[:a]+plan+t[b:]
rep("proc:true,maxLeave:3,seb:false};","proc:true,maxLeave:3,seb:false,avoid:true,layout:'std',cov:new Set(ALLKEYS.map(k=>k.split('|').slice(0,2).join('|')))};")
rep("t:ex.title,pr:ex.pr}","t:ex.title,pr:ex.pr,nt:ex.note}")
rep("pr:p.pr||{on:false,max:3,seb:false}}}","pr:p.pr||{on:false,max:3,seb:false},note:p.nt||''}}")
rep("PRESETS[b.dataset.p].set();","B.layout='std';PRESETS[b.dataset.p].set();")
rep(" topic:{label:'Topic drill'"," plan:{label:'Current topic + review',sub:'Module 1: topics you tick · Module 2: everything covered',set:()=>{B.sk=new Set();B.lv='MH';B.fmt='all';B.n=44;B.modules=2;B.mins='';B.balance=true;B.title='Current topic + cumulative review';B.proc=true;B.layout='plan'}},\n topic:{label:'Topic drill'")
rep("B[g.dataset.g]=g.dataset.g==='modules'?+v:v;","B[g.dataset.g]=g.dataset.g==='modules'?+v:v;if(B.layout==='plan')B.modules=2;")
rep("  <h2>Exam integrity</h2><div class=\"set\">",r"""  <h2>Exam layout</h2><div class="set">
   <div><label>Layout</label><div class="seg" data-g="layout">${[['std','One set'],['plan','Module 1 current topic, Module 2 review']].map(([v,l])=>`<button data-v="${v}" aria-pressed="${B.layout===v}">${l}</button>`).join('')}</div></div>
   <div><label class="chk"><input type="checkbox" id="avoid" ${B.avoid?'checked':''}> Avoid questions I have already seen <small>(including their rephrased twins; remembered on this device)</small></label><div class="small">Seen so far: <b>${SEEN.size}</b> of ${FAMN} <button class="chip" id="rstSeen">Reset history</button></div></div></div>
  ${B.layout==='plan'?`<p class="hint"><b>Module 1</b> uses the topics ticked above (what you are studying now). <b>Module 2</b> is a comprehensive review drawn from the skills ticked here, plus the current topics.</p><div class="row" style="margin:0 0 8px"><button class="chip" id="covAll">All covered</button><button class="chip" id="covNone">Clear</button></div>${DOMS.map(d=>`<div class="covd"><b>${DOMSHORT[d]}</b><div class="covs">${Object.keys(byDom[d]||{}).map(sk=>`<label class="sk"><input type="checkbox" data-cov="${d}|${sk}" ${B.cov.has(d+'|'+sk)?'checked':''}> ${sk}</label>`).join('')}</div></div>`).join('')}`:''}
  <h2>Exam integrity</h2><div class="set">""")
rep("${short?`<br><span>Only ${P.length}","${B.layout==='plan'?'<br><span>Module 1: '+(ex.mods[0]||[]).length+' questions on the current topics · Module 2: '+(ex.mods[1]||[]).length+' questions of cumulative review</span>':''}${B.avoid?'<br><span>Unseen matching questions: '+new Set(P.filter(i=>!SEEN.has(FAM(i.id))).map(i=>FAM(i.id))).size+' of '+new Set(P.map(i=>FAM(i.id))).size+'</span>':''}${short?`<br><span>Only ${P.length}")
rep("id=\"startB\" style=\"font-size:1.05rem;padding:11px 34px\" ${cn.n?'':'disabled'}>","id=\"startB\" style=\"font-size:1.05rem;padding:11px 34px\" ${cn.n&&!(B.layout==='plan'&&!P.length)?'':'disabled'}>")
rep("  <div class=\"row\" style=\"margin-top:16px\"><button class=\"btn primary\" id=\"startB\"","  ${B.layout==='plan'&&!P.length?'<p class=\"hint\" style=\"color:#a4262c\">Tick the topic(s) you are studying now in the Topics list above to build Module 1.</p>':''}\n  <div class=\"row\" style=\"margin-top:16px\"><button class=\"btn primary\" id=\"startB\"")
rep("  $('#proc').onchange=","  document.querySelectorAll('[data-cov]').forEach(c=>c.onchange=()=>{c.checked?B.cov.add(c.dataset.cov):B.cov.delete(c.dataset.cov);builder()});\n  const ca=$('#covAll');if(ca){ca.onclick=()=>{B.cov=new Set(ALLKEYS.map(k=>k.split('|').slice(0,2).join('|')));builder()};$('#covNone').onclick=()=>{B.cov=new Set();builder()}}\n  $('#avoid').onchange=e=>{B.avoid=e.target.checked;builder()};$('#rstSeen').onclick=()=>{SEEN=new Set();saveSeen();builder()};\n  $('#proc').onchange=")
rep("${PROC.startHTML()}<div class=\"note\">Scores here","${EXAM.note?'<p class=\"lede\"><b>'+EXAM.note+'</b></p>':''}${PROC.startHTML()}<div class=\"note\">Scores here")
rep("function finishModule(timeout){\n  clearInterval(S.tick);","function finishModule(timeout){\n  clearInterval(S.tick);markSeen(mods()[S.mod]);")
rep("function results(){\n","function results(){\n  EXAM.mods.slice(0,S.mod+1).forEach(markSeen);\n")

open('bank_template.html','w').write(t)
print('ok',len(t))

