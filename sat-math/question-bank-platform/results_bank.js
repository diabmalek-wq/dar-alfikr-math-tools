const PTS=[[0,200],[2,240],[4,280],[6,320],[8,350],[10,380],[12,410],[14,440],[16,470],[18,500],[20,530],[22,560],[24,590],[26,610],[28,640],[30,660],[32,680],[34,700],[36,720],[38,740],[40,770],[42,790],[44,800]];
function estScore(raw){
  for(let k=1;k<PTS.length;k++){if(raw<=PTS[k][0]){const [x0,y0]=PTS[k-1],[x1,y1]=PTS[k];return y0+(y1-y0)*(raw-x0)/(x1-x0)}}
  return 800;
}
function scoreRange(raw){
  const c=estScore(raw);let lo=Math.round(c/10)*10-20;lo=Math.max(200,Math.min(760,lo));
  return [lo,lo+40,Math.round(c)];
}
function pct(a,b){return b?Math.round(100*a/b):0}
function results(){
  const TARGET=EXAM.secs.reduce((a,b)=>a+b,0)/EXAM.mods.flat().length;
  const all=[];EXAM.mods.forEach((ml,m)=>ml.forEach((it,k)=>all.push({it,m,k,a:S.ans[m][k],ok:correct(it,S.ans[m][k]),t:S.time[m][k]||0,fl:!!S.flag[m][k]})));
  all.forEach(x=>{x.sk=(x.a==null||x.a==='')});
  const N=all.length,tot=all.filter(x=>x.ok).length,skipped=all.filter(x=>x.sk).length;
  const showBand=N>=20,[lo,hi]=scoreRange(tot/N*44);
  const grp=f=>{const g=all.filter(f);return {n:g.length,c:g.filter(x=>x.ok).length}};
  const bars=(rows)=>rows.map(r=>`<div class="brow"><span>${r[0]}</span><span class="t"><i style="width:${pct(r[1],r[2])}%"></i></span><span class="v">${r[1]}/${r[2]}</span></div>`).join('');
  const byDom={},bySk={};all.forEach(x=>{const d=byDom[x.it.domain]=byDom[x.it.domain]||{n:0,c:0};d.n++;if(x.ok)d.c++;const k=x.it.domain+'|'+x.it.skill;const s=bySk[k]=bySk[k]||{n:0,c:0,name:x.it.skill,dom:x.it.domain};s.n++;if(x.ok)s.c++});
  const mc=grp(x=>x.it.mc),spr=grp(x=>!x.it.mc),med=grp(x=>x.it.lv==='M'),hard=grp(x=>x.it.lv==='H');
  const used=all.reduce((a,x)=>a+x.t,0),avg=used/N;
  const fastWrong=all.filter(x=>!x.ok&&!x.sk&&x.t<TARGET*0.5),slowWrong=all.filter(x=>!x.ok&&!x.sk&&x.t>TARGET*1.5),slowRight=all.filter(x=>x.ok&&x.t>TARGET*1.5);
  const flagged=grp(x=>x.fl);
  const maxT=Math.max(TARGET*2,...all.map(x=>x.t));
  const Hh=120,gx=Math.max(3,Math.min(8,Math.floor(900/N)));const svgW=N*gx+60;
  const bar=all.map((x,j)=>{const h=Math.max(2,Math.round(Hh*Math.min(x.t,maxT)/maxT));const col=x.sk?'var(--muted)':x.ok?'var(--good)':'var(--bad)';
    return `<rect x="${40+j*gx}" y="${Hh+10-h}" width="${gx-1}" height="${h}" rx="1" fill="${col}"><title>M${x.m+1} Q${x.k+1}: ${Math.round(x.t)} s</title></rect>`}).join('');
  const ty=Hh+10-Math.round(Hh*TARGET/maxT);
  let off=0;const marks=EXAM.mods.map((ml,m)=>{const x=40+off*gx;off+=ml.length;return `<text x="${x}" y="${Hh+24}" font-size="8" fill="var(--muted)">Module ${m+1}</text>`+(m?`<line x1="${x-2}" x2="${x-2}" y1="4" y2="${Hh+10}" stroke="var(--line)"/>`:'')}).join('');
  const chart=`<svg viewBox="0 0 ${svgW} ${Hh+34}" width="100%" role="img" aria-label="Seconds spent on each question, green correct, red incorrect, grey skipped" style="max-width:${svgW*3}px">${bar}
   <line x1="38" x2="${40+N*gx}" y1="${ty}" y2="${ty}" stroke="var(--muted)" stroke-dasharray="3 3"/><text x="2" y="${ty+3}" font-size="8" fill="var(--muted)">${Math.round(TARGET)} s</text>
   <line x1="38" x2="${40+N*gx}" y1="${Hh+10}" y2="${Hh+10}" stroke="var(--line)"/>${marks}</svg>`;
  const skills=Object.values(bySk).map(s=>({...s,acc:s.c/s.n}));
  const weak=skills.filter(x=>x.acc<0.7&&x.n>=2).sort((a,b)=>a.acc-b.acc),strong=skills.filter(x=>x.acc>=0.7&&x.n>=2);
  const advice=[];
  if(weak.length)advice.push(`<b>Redo first:</b> ${weak.slice(0,6).map(x=>`${x.name} (${x.c}/${x.n})`).join(', ')}${weak.length>6?` and ${weak.length-6} more`:''}. Work the missed questions below with the Desmos steps, then build a topic drill on these skills.`);
  else advice.push('<b>Strong across the topics in this exam.</b> Build a harder or longer exam, and watch your timing.');
  if(strong.length&&weak.length)advice.push(`<b>Keep warm:</b> ${strong.slice(0,5).map(x=>x.name).join(', ')} are at 70% or better.`);
  if(hard.n>=3&&med.n>=3&&pct(med.c,med.n)-pct(hard.c,hard.n)>=25)advice.push(`<b>Hard-question gap:</b> ${pct(med.c,med.n)}% on Medium vs ${pct(hard.c,hard.n)}% on Hard. The score is capped by the second module, so drill Hard questions by topic.`);
  if(spr.n>=3&&mc.n>=3&&pct(spr.c,spr.n)+20<pct(mc.c,mc.n))advice.push(`<b>Grid-in answers:</b> ${pct(spr.c,spr.n)}% vs ${pct(mc.c,mc.n)}% on multiple choice. Check the answer format (fractions, decimals, sign) and plug the result back in.`);
  if(fastWrong.length>=3)advice.push(`<b>Rushed misses:</b> ${fastWrong.length} wrong answers came in under ${Math.round(TARGET*0.5)} seconds. Slow down on the first read and re-read what the question asks for.`);
  if(slowWrong.length>=3)advice.push(`<b>Stuck misses:</b> ${slowWrong.length} wrong answers took over ${Math.round(TARGET*1.5)} seconds. Flag and move on, then return with spare time.`);
  if(skipped>=3)advice.push(`<b>Unanswered:</b> ${skipped} questions had no answer. There is no penalty for guessing, so answer every question before time runs out.`);
  if(flagged.n>=3&&flagged.c/flagged.n<0.4)advice.push(`<b>Marked questions:</b> only ${flagged.c} of ${flagged.n} you marked for review were correct. Marking works when you actually return to them.`);
  const show=all.filter(x=>filter==='all'||(filter==='wrong'&&!x.ok)||(filter==='skip'&&x.sk));
  const items=show.map(x=>{
    const it=x.it,sk=x.sk;
    const opts=it.mc?it.opts.map((o,j)=>`<span class="optr ${j===it.key?'key':''} ${j===x.a&&!x.ok?'mine':''}"><b>${'ABCD'[j]}.</b> ${o}${j===it.key?' ✓':''}${j===x.a&&!x.ok?' (your answer)':''}</span>`).join(''):`<p>Correct answer: <b>$${it.disp}$</b>${sk?'':` · you entered <b>${esc(String(x.a))}</b>`}</p>`;
    const tag=!x.ok&&!sk?(x.t<TARGET*0.5?' · answered fast':x.t>TARGET*1.5?' · took long':''):'';
    return `<details class="item"><summary><b>M${x.m+1} · Q${x.k+1}</b><span class="pill ${x.ok?'ok':sk?'sk':'no'}">${x.ok?'Correct':sk?'Skipped':'Incorrect'}</span><span class="meta">${it.skill} · ${it.lv==='H'?'Hard':'Medium'} · ${Math.round(x.t)} s${tag}${x.fl?' · marked':''} · ${it.id}</span></summary><div class="body">${fmt(it.q)}${opts}<h4 style="margin:12px 0 2px">Desmos solution</h4><ol class="steps">${it.steps.map(s=>'<li>'+s+'</li>').join('')}</ol></div></details>`}).join('');
  const modBoxes=EXAM.mods.map((ml,m)=>{const g=all.filter(x=>x.m===m);return `<div class="fact"><b>${g.filter(x=>x.ok).length}/${g.length}</b><span>Module ${m+1}</span></div>`}).join('');
  const full=BANK.length>N+60;
  $('#app').innerHTML=`<div class="page" style="overflow:auto"><div class="eyebrow">Score report · ${EXAM.title}</div>
  <div class="hero"><div class="eyebrow">${showBand?'Expected Math score':'Result'}</div><div class="big">${showBand?lo+'–'+hi:pct(tot,N)+'%'}</div><div class="sub">${showBand?'out of 800 · ':''}${tot} of ${N} correct (${pct(tot,N)}%)</div></div>
  <p class="meta" style="color:var(--muted);font-size:.86rem;max-width:66ch;margin:0 0 6px">${showBand?`An estimate, not an official score.${N===44?'':` Your accuracy on these ${N} questions is projected onto a full 44-question test.`} It maps to a 40-point band using a hard-module conversion. The exam is not adaptive and questions are Medium or Hard, so expect a different band on a real Bluebook test.`:'Too few questions for a score band. Take 20 or more questions to see an expected score range.'}</p>
  <div class="score">${modBoxes}<div class="fact"><b>${skipped}</b><span>unanswered</span></div><div class="fact"><b>${Math.round(used/60)} min</b><span>of ${Math.round(EXAM.secs.reduce((a,b)=>a+b,0)/60)} used · ${Math.round(avg)} s per question</span></div></div>
  <h2>What to do next</h2><ul class="rules adv">${advice.map(a=>'<li>'+a+'</li>').join('')}</ul>
  <h2>By domain</h2><div class="bars">${bars(DOMS.filter(d=>byDom[d]).map(d=>[DOMSHORT[d],byDom[d].c,byDom[d].n]))}</div>
  <h2>By skill</h2><div class="bars">${bars(skills.sort((a,b)=>DOMS.indexOf(a.dom)-DOMS.indexOf(b.dom)||a.name.localeCompare(b.name)).map(x=>[x.name,x.c,x.n]))}</div>
  <h2>By question type</h2><div class="bars">${bars([['Multiple choice',mc.c,mc.n],['Grid-in',spr.c,spr.n],['Medium',med.c,med.n],['Hard',hard.c,hard.n]].filter(r=>r[2]))}</div>
  <h2>Pacing</h2><p class="meta" style="color:var(--muted);font-size:.88rem;margin:0 0 6px">Seconds on each question. Dashed line is the ${Math.round(TARGET)} s average this exam allows. ${slowRight.length?`${slowRight.length} correct answers took over ${Math.round(TARGET*1.5)} s. `:''}${fastWrong.length?`${fastWrong.length} wrong answers took under ${Math.round(TARGET*0.5)} s.`:''}</p>
  <div class="chart">${chart}</div><div class="legend" style="justify-content:flex-start"><span style="color:var(--good)">■ correct</span><span style="color:var(--bad)">■ incorrect</span><span>■ skipped</span></div>
  <h2>Review every question</h2><div class="filters" role="group" aria-label="Filter questions"><button class="chip" data-f="all" aria-pressed="${filter==='all'}">All ${N}</button><button class="chip" data-f="wrong" aria-pressed="${filter==='wrong'}">Incorrect or skipped ${all.filter(x=>!x.ok).length}</button><button class="chip" data-f="skip" aria-pressed="${filter==='skip'}">Skipped ${skipped}</button></div>
  ${items||'<p class="lede">Nothing to show for this filter.</p>'}
  <div class="row" style="margin-top:22px"><button class="btn" id="again">Retake this exam</button>${full?'<button class="btn primary" id="newex">Build another exam</button>':''}</div></div>`;
  typeset($('#app'));
  document.querySelectorAll('.chip').forEach(b=>b.onclick=()=>{filter=b.dataset.f;results()});
  $('#again').onclick=()=>{const keep=EXAM;resetState();EXAM=keep;S.phase='intro';render()};
  const nb=$('#newex');if(nb)nb.onclick=()=>{EXAM=null;S.phase='intro';render()};
}
