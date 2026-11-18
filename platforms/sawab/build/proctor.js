/* Sawab exam integrity layer — same rules as SAT Aceit: fullscreen, leave detection, the 3rd leave submits
   automatically, copy/paste/right-click/print off, integrity report at the end. Page supplies window.__PX hooks. */
(function(){
const X=()=>window.__PX||{};
const R=document.documentElement,reqFS=R.requestFullscreen||R.webkitRequestFullscreen,exitFS=document.exitFullscreen||document.webkitExitFullscreen;
const fsOn=()=>!!(document.fullscreenElement||document.webkitFullscreenElement);
const SEB=/\bSEB\b/i.test(navigator.userAgent),MAX=3;
const L={was:false,on:false,log:[],blocked:0,away:null,t0:0,fs:false,fsFail:false,auto:null,total:0};
const mm=s=>{s=Math.round(s);return Math.floor(s/60)+':'+String(s%60).padStart(2,'0')};
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const css=document.createElement('style');css.textContent=`
#procov{position:fixed;inset:0;z-index:99999;display:none;align-items:center;justify-content:center;background:rgba(10,16,24,.92);padding:20px;font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
#procov .pbox{background:#fff;color:#1c2736;max-width:460px;width:100%;border-radius:14px;padding:26px 28px;box-shadow:0 10px 40px rgba(0,0,0,.4)}
#procov .ey{font:600 .72rem ui-monospace,Menlo,monospace;letter-spacing:.14em;text-transform:uppercase;color:#b42318}
#procov h2{margin:4px 0 10px;font-size:1.4rem;color:#1f3a5f}#procov p{margin:8px 0;line-height:1.5}#procov .sm{font-size:.85rem;color:#5d6b7e}
#procov button,#procard button,#procban button{background:#1f3a5f;color:#fff;border:0;border-radius:999px;padding:10px 22px;font:600 .9rem system-ui,sans-serif;cursor:pointer;margin-top:8px}
#procban{position:fixed;left:50%;top:14px;transform:translateX(-50%);z-index:9999;background:#1f3a5f;color:#fff;border-radius:14px;padding:14px 18px;max-width:560px;width:calc(100% - 28px);box-shadow:0 10px 30px rgba(0,0,0,.3);font:400 .9rem/1.5 system-ui,sans-serif}
#procban b{color:#ffd88a}#procban ul{margin:6px 0 4px;padding-left:18px}#procban button{background:#fff;color:#1f3a5f;padding:7px 16px;margin-top:4px}
#procard{background:#fff;color:#1c2736;border:1px solid #d5dbe4;border-radius:14px;padding:16px 18px;margin:16px 0;font:400 .92rem/1.5 system-ui,sans-serif;text-align:left}
#procard h3{margin:0 0 8px;font-size:1.05rem;color:#1f3a5f}#procard .st{display:flex;gap:14px;flex-wrap:wrap;align-items:center;margin-bottom:8px}
#procard .chip{border-radius:999px;padding:3px 10px;font-weight:700;font-size:.78rem}#procard .clean{background:#e3f4e9;color:#17803d}#procard .review{background:#fdf0d9;color:#a15c07}#procard .flag{background:#fbe7e4;color:#b42318}
#procard table{border-collapse:collapse;width:100%;font-size:.85rem;margin:6px 0}#procard th,#procard td{border-bottom:1px solid #e5e9f0;padding:5px 8px;text-align:left}
#procard .sm{font-size:.8rem;color:#5d6b7e}#procard .auto{background:#fbe7e4;border-radius:10px;padding:8px 12px;color:#b42318}
body.procon .stem,body.procon .opt,body.procon .q,body.procon .qbox,body.procon .opts{-webkit-user-select:none;user-select:none}`;
document.head.appendChild(css);
function ov(){let o=document.getElementById('procov');if(!o){o=document.createElement('div');o.id='procov';o.setAttribute('role','alertdialog');o.setAttribute('aria-modal','true');document.body.appendChild(o)}return o}
function showOv(){
  const e=L.log[L.log.length-1];if(!e)return;const o=ov(),left=MAX-e.n;
  const warn=left===1?'<b>Your next leave will submit the exam automatically.</b>':`${left} more leaves before the exam is submitted automatically.`;
  o.innerHTML=`<div class="pbox"><div class="ey">Exam integrity</div><h2>You left the exam</h2><p>${esc(e.why)}. This is <b>leave ${e.n} of ${MAX}</b> and it has been recorded.</p><p>${warn}</p><p class="sm">The clock kept running while you were away.</p><button id="procback">Return to exam</button></div>`;
  o.style.display='flex';const b=document.getElementById('procback');b.onclick=back;b.focus();
}
function back(){
  const e=L.log[L.log.length-1];if(L.away&&e&&e.dur==null){e.dur=(Date.now()-L.away.t)/1000;L.total+=e.dur}
  L.away=null;if(L.fs&&!fsOn()&&reqFS)try{const p=reqFS.call(R);if(p&&p.catch)p.catch(()=>{})}catch(x){}
  const o=document.getElementById('procov');if(o)o.style.display='none';
}
function where(){try{return X().where?X().where():''}catch(e){return ''}}
function leave(why){
  if(!L.on||L.away)return;
  const n=L.log.length+1;L.away={t:Date.now()};const e={n,at:(Date.now()-L.t0)/1000,dur:null,why,q:where()};L.log.push(e);
  if(n>=MAX){e.dur=0;L.auto={n,q:e.q};end();try{X().submit&&X().submit()}catch(x){}return}
  showOv();
}
function ret(){const e=L.log[L.log.length-1];if(L.away&&e&&e.dur==null&&!document.hidden&&document.hasFocus()){e.dur=(Date.now()-L.away.t)/1000;L.total+=e.dur}}
const onVis=()=>document.hidden?leave('Switched tab or minimised the window'):ret();
const onBlur=()=>setTimeout(()=>{if(L.on&&!document.hidden&&!document.hasFocus())leave('Clicked outside the exam window')},700);
const onFS=()=>{if(!fsOn()){if(L.fs&&L.on)leave('Left fullscreen')}else ret()};
const editable=e=>e.target&&e.target.closest&&e.target.closest('input,textarea,canvas');
const stop=e=>{if(!L.on||editable(e))return;e.preventDefault();L.blocked++};
const onKey=e=>{if(!L.on)return;const k=(e.key||'').toLowerCase(),c=e.ctrlKey||e.metaKey;
  if(k==='f12'||(c&&['p','s','u'].includes(k))||(c&&e.shiftKey&&['i','j','c'].includes(k))||(e.metaKey&&e.altKey&&['i','j','c','u'].includes(k))){e.preventDefault();L.blocked++}};
const H=[['visibilitychange',onVis,document],['blur',onBlur,window],['focus',ret,window],['fullscreenchange',onFS,document],['webkitfullscreenchange',onFS,document],
  ['copy',stop,document],['cut',stop,document],['paste',stop,document],['contextmenu',stop,document],['dragstart',stop,document],['keydown',onKey,document]];
function begin(){
  Object.assign(L,{was:true,on:true,log:[],blocked:0,away:null,auto:null,total:0,fsFail:false,fs:false,t0:Date.now()});
  const c=document.getElementById('procard');if(c)c.remove();
  L.fs=!!reqFS&&!SEB;
  if(L.fs){try{const p=reqFS.call(R);if(p&&p.catch)p.catch(()=>{L.fs=false;L.fsFail=true})}catch(x){L.fs=false;L.fsFail=true}}
  H.forEach(([n,f,o])=>o.addEventListener(n,f));document.body.classList.add('procon');banner();
}
function end(){
  H.forEach(([n,f,o])=>o.removeEventListener(n,f));L.on=false;document.body.classList.remove('procon');
  const o=document.getElementById('procov');if(o)o.style.display='none';const b=document.getElementById('procban');if(b)b.remove();
  if(fsOn()&&exitFS)try{exitFS.call(document)}catch(x){}
}
function banner(){
  const b=document.createElement('div');b.id='procban';b.setAttribute('role','status');
  b.innerHTML=`<b>Exam integrity is on.</b><ul><li>The exam runs in fullscreen. Leaving the window, switching tabs or exiting fullscreen is recorded.</li><li>The <b>${MAX}rd leave submits the exam automatically</b>. The clock keeps running while you are away.</li><li>Copy, paste, right-click and printing are turned off.</li></ul><button id="procok">I understand</button>`;
  document.body.appendChild(b);document.getElementById('procok').onclick=()=>b.remove();setTimeout(()=>{if(b.isConnected)b.remove()},15000);
}
function cardHTML(){
  const n=L.log.length,flag=L.auto||n>=3?'flag':n?'review':'clean',lab={clean:'Clean',review:'Review',flag:'Flagged'}[flag];
  const rows=L.log.map(e=>`<tr><td>${e.n}</td><td>${mm(e.at)}</td><td>${e.dur==null?'n/a':e.dur<1?'under 1 s':mm(e.dur)}</td><td>${esc(e.why)}</td><td>${esc(e.q||'')}</td></tr>`).join('');
  return `<h3>Exam integrity</h3><div class="st"><span class="chip ${flag}">${lab}</span><span><b>${n}</b> leave${n===1?'':'s'}</span><span><b>${mm(L.total)}</b> away</span><span><b>${L.blocked}</b> blocked actions</span><span>${SEB?'Safe Exam Browser':L.fs?'Fullscreen':L.fsFail?'Fullscreen refused':'No fullscreen support'}</span></div>
  ${L.auto?`<p class="auto"><b>Auto-submitted</b> at leave ${L.auto.n}${L.auto.q?' ('+esc(L.auto.q)+')':''}. Unanswered questions count as incorrect.</p>`:''}
  ${n?`<table><thead><tr><th>#</th><th>At</th><th>Away</th><th>What happened</th><th>Where</th></tr></thead><tbody>${rows}</tbody></table>`:'<p class="sm">No leaves recorded.</p>'}
  <p class="sm">This report is created in the student's browser. It shows what the page could detect, so it is not proof on its own. Use it with in-person supervision.</p><button id="procopy">Copy report</button> <span id="procmsg" class="sm"></span>`;
}
function text(){let s=`${(X().title||'Sawab mock exam')} integrity report\nDate: ${new Date().toLocaleString()}\nLeaves: ${L.log.length} · away ${mm(L.total)} · blocked actions ${L.blocked}\nMode: ${SEB?'Safe Exam Browser':L.fs?'Fullscreen':'No fullscreen'}${L.auto?'\nAUTO-SUBMITTED at leave '+L.auto.n:''}\n`;L.log.forEach(e=>{s+=`  #${e.n} at ${mm(e.at)}, away ${e.dur==null?'n/a':mm(e.dur)}, ${e.why}${e.q?', '+e.q:''}\n`});return s}
function placeCard(){
  if(!L.was||L.on)return;let rep=false;try{rep=!!(X().isReport&&X().isReport())}catch(e){}
  const ex=document.getElementById('procard');
  if(!rep){if(ex)ex.remove();return}
  if(ex)return;
  const host=document.getElementById('app')||document.body;const c=document.createElement('div');c.id='procard';c.innerHTML=cardHTML();
  const anchor=host.querySelector('header,.top,.head');if(anchor&&anchor.parentElement)anchor.parentElement.insertBefore(c,anchor.nextSibling);else host.prepend(c);
  document.getElementById('procopy').onclick=()=>{const m=document.getElementById('procmsg'),t=text();(navigator.clipboard&&navigator.clipboard.writeText?navigator.clipboard.writeText(t):Promise.reject()).then(()=>{m.textContent='Copied.'},()=>{m.textContent='Select and copy: '+t.replace(/\n/g,' | ')})};
}
function active(){try{return !!(X().active&&X().active())}catch(e){return false}}
document.addEventListener('click',()=>setTimeout(()=>{if(!L.on&&active())begin()},0),true);
setInterval(()=>{const a=active();if(L.on&&!a)end();else if(!L.on&&a)begin();placeCard()},400);
window.__proctor={L,begin,end};
})();
