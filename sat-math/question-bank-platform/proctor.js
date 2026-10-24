/* ===== PROCTOR: integrity layer (fullscreen, leave detection, copy block, report, SEB check) ===== */
const PROC=(function(){
  const UA=navigator.userAgent,SEB=/\bSEB\b/i.test(UA),R=document.documentElement;
  const reqFS=R.requestFullscreen||R.webkitRequestFullscreen,exitFS=document.exitFullscreen||document.webkitExitFullscreen;
  const fsOn=()=>!!(document.fullscreenElement||document.webkitFullscreenElement);
  const L={was:false,on:false,max:3,log:[],blocked:0,away:null,t0:0,fs:false,fsFail:false,auto:null,name:'',total:0,seb:SEB};
  const cfg=()=>(EXAM&&EXAM.pr)||{on:false};
  const mm=s=>{s=Math.round(s);return Math.floor(s/60)+':'+String(s%60).padStart(2,'0')};
  const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  const editable=e=>e.target&&e.target.closest&&e.target.closest('.dcg-container,#desmos,.sprbox,input,textarea');
  function ov(){let o=document.getElementById('procov');if(!o){o=document.createElement('div');o.id='procov';o.setAttribute('role','alertdialog');o.setAttribute('aria-modal','true');document.body.appendChild(o)}return o}
  function showOv(){
    const e=L.log[L.log.length-1];if(!e)return;const o=ov(),left=L.max?L.max-e.n:0;
    const warn=!L.max?'Leaves are recorded and appear in your integrity report.':left===1?'<b>Your next leave will submit the exam automatically.</b>':`${left} more leaves before the exam is submitted automatically.`;
    o.innerHTML=`<div class="pbox"><div class="eyebrow">Exam integrity</div><h2>You left the exam</h2><p>${esc(e.why)}. This is <b>leave ${e.n}${L.max?' of '+L.max:''}</b> and it has been recorded.</p><p>${warn}</p><p class="small">The clock kept running while you were away.</p><button class="btn primary" id="procback">Return to exam</button></div>`;
    o.style.display='flex';document.getElementById('procback').onclick=back;document.getElementById('procback').focus();
  }
  function back(){
    const e=L.log[L.log.length-1];if(L.away&&e&&e.dur==null){e.dur=(Date.now()-L.away.t)/1000;L.total+=e.dur}
    L.away=null;
    if(L.fs&&!fsOn()&&reqFS)try{const p=reqFS.call(R);if(p&&p.catch)p.catch(()=>{})}catch(x){}
    const o=document.getElementById('procov');if(o)o.style.display='none';S.last=Date.now();
  }
  function leave(why){
    if(!L.on||L.away||S.phase==='results')return;
    const n=L.log.length+1;L.away={t:Date.now()};
    const e={n,at:(Date.now()-L.t0)/1000,dur:null,why,mod:S.mod+1,q:S.i+1};L.log.push(e);
    if(L.max&&n>=L.max){e.dur=0;L.auto={n,mod:S.mod+1,q:S.i+1};clearInterval(S.tick);S.modal=null;S.phase='results';end();render();return}
    showOv();
  }
  function ret(){ // student is physically back; stop the away clock
    const e=L.log[L.log.length-1];if(L.away&&e&&e.dur==null&&!document.hidden&&document.hasFocus()){e.dur=(Date.now()-L.away.t)/1000;L.total+=e.dur}
  }
  const onVis=()=>document.hidden?leave('Switched tab or minimised the window'):ret();
  const onBlur=()=>setTimeout(()=>{if(L.on&&!document.hidden&&!document.hasFocus())leave('Clicked outside the exam window')},700);
  const onFS=()=>{if(!fsOn()){if(L.fs&&L.on)leave('Left fullscreen')}else ret()};
  const stop=e=>{if(!L.on||editable(e))return;e.preventDefault();L.blocked++};
  const onKey=e=>{if(!L.on)return;const k=e.key.toLowerCase(),c=e.ctrlKey||e.metaKey;
    if(k==='f12'||(c&&['p','s','u'].includes(k))||(c&&e.shiftKey&&['i','j','c'].includes(k))||(e.metaKey&&e.altKey&&['i','j','c','u'].includes(k))){e.preventDefault();L.blocked++}};
  const H=[['visibilitychange',onVis,document],['blur',onBlur,window],['focus',ret,window],['fullscreenchange',onFS,document],['webkitfullscreenchange',onFS,document],
    ['copy',stop,document],['cut',stop,document],['paste',stop,document],['contextmenu',stop,document],['dragstart',stop,document],['keydown',onKey,document]];
  function begin(){
    end(true);Object.assign(L,{was:false,on:false,log:[],blocked:0,away:null,auto:null,total:0,fsFail:false,fs:false});
    const c=cfg();if(!c.on)return;L.was=L.on=true;L.max=+c.max||0;L.t0=Date.now();
    L.fs=!!reqFS&&!SEB;
    if(L.fs){try{const p=reqFS.call(R);if(p&&p.catch)p.catch(()=>{L.fs=false;L.fsFail=true})}catch(x){L.fs=false;L.fsFail=true}}
    H.forEach(([n,f,o])=>o.addEventListener(n,f));document.body.classList.add('procon');
  }
  function end(quiet){
    if(L.on||quiet){H.forEach(([n,f,o])=>o.removeEventListener(n,f))}
    L.on=false;document.body.classList.remove('procon');
    const o=document.getElementById('procov');if(o)o.style.display='none';
    if(!quiet&&fsOn()&&exitFS)try{exitFS.call(document)}catch(x){}
  }
  function gate(){ // returns true if the exam may start
    const c=cfg();if(c.on&&c.seb&&!SEB){S.sebBlocked=true;startPage();return false}
    const nm=document.getElementById('stuname');if(nm)L.name=nm.value.trim();
    S.sebBlocked=false;return true;
  }
  function startHTML(){
    const c=cfg();if(!c.on)return '';
    const sebLine=c.seb?(SEB?'<li class="ok">Safe Exam Browser detected.</li>':'<li class="bad">This exam requires <b>Safe Exam Browser</b>. Open it from the teacher\'s exam file or link in SEB to start.</li>'):'';
    return `<h2>Exam integrity</h2><ul class="rules"><li>The exam runs in <b>fullscreen</b>. Leaving the window, switching tabs or exiting fullscreen is recorded.</li>
    <li>${c.max?`The <b>${c.max}${['th','st','nd','rd'][c.max]&&c.max<4?['th','st','nd','rd'][c.max]:'th'} leave submits the exam automatically</b>.`:'Leaves are recorded and shown in your integrity report.'} The clock keeps running while you are away.</li>
    <li>Copy, paste, right-click and printing are turned off. Desmos still works normally.</li>${sebLine}</ul>
    <p style="margin:6px 0"><label style="font-weight:600;font-size:.9rem">Your name <small style="font-weight:400;color:var(--muted)">(printed on your integrity report)</small><br><input id="stuname" class="nameIn" maxlength="60" value="${esc(L.name)}" autocomplete="off"></label></p>`
      +(S.sebBlocked?'<p class="sebmsg" role="alert">This exam can only be started inside Safe Exam Browser.</p>':'');
  }
  function card(){
    if(!L.was)return '';
    const n=L.log.length,flag=L.auto||n>=3?'flag':n?'review':'clean',lab={clean:'Clean',review:'Review',flag:'Flagged'}[flag];
    const rows=L.log.map(e=>`<tr><td>${e.n}</td><td>${mm(e.at)}</td><td>${e.dur==null?'n/a':e.dur<1?'under 1 s':mm(e.dur)}</td><td>${esc(e.why)}</td><td>M${e.mod} Q${e.q}</td></tr>`).join('');
    return `<h2>Exam integrity</h2><div class="pcard ${flag}"><div class="pstat"><span class="pchip ${flag}">${lab}</span><span><b>${n}</b> leave${n===1?'':'s'}</span><span><b>${mm(L.total)}</b> away</span><span><b>${L.blocked}</b> blocked actions</span><span>${SEB?'Safe Exam Browser':L.fs?'Fullscreen':L.fsFail?'Fullscreen refused':'No fullscreen support'}</span></div>
    ${L.auto?`<p class="pauto"><b>Auto-submitted</b> at leave ${L.auto.n} (Module ${L.auto.mod}, question ${L.auto.q}). Unanswered questions count as incorrect.</p>`:''}
    ${n?`<div class="ptw"><table class="ptab"><thead><tr><th>#</th><th>At</th><th>Away</th><th>What happened</th><th>Where</th></tr></thead><tbody>${rows}</tbody></table></div>`:'<p class="small">No leaves recorded.</p>'}
    <p class="small">This report is created in the student's browser. It shows what the page could detect, so it is not proof on its own. Use it with in-person supervision.</p>
    <button class="btn ghost" id="procopy">Copy report</button> <span id="procmsg" class="small"></span></div>`;
  }
  function report(){
    const d=new Date().toLocaleString();let s=`SAT Aceit integrity report\nExam: ${EXAM.title}\nStudent: ${L.name||'(no name)'}\nDate: ${d}\nLeaves: ${L.log.length} · away ${mm(L.total)} · blocked actions ${L.blocked}\nMode: ${SEB?'Safe Exam Browser':L.fs?'Fullscreen':'No fullscreen'}${L.auto?'\nAUTO-SUBMITTED at leave '+L.auto.n+' (Module '+L.auto.mod+', Q'+L.auto.q+')':''}\n`;
    L.log.forEach(e=>{s+=`  #${e.n} at ${mm(e.at)}, away ${e.dur==null?'n/a':mm(e.dur)}, ${e.why}, M${e.mod} Q${e.q}\n`});return s}
  function bind(){const b=document.getElementById('procopy');if(!b)return;b.onclick=()=>{const m=document.getElementById('procmsg'),t=report();
    (navigator.clipboard&&navigator.clipboard.writeText?navigator.clipboard.writeText(t):Promise.reject()).then(()=>{m.textContent='Copied.'},()=>{m.textContent='Select and copy: '+t.replace(/\n/g,' | ')})}}
  return {begin,end,gate,startHTML,card,bind,L,SEB,cfg};
})();
window.__sat={PROC,S,presetFrom,makeExam}; /* test handle */
