/* ===== PLAN: no repeats + current-topic / cumulative-review layout ===== */
const FAM=id=>id.replace(/-2$/,'');
let SEEN=new Set();try{SEEN=new Set(JSON.parse(localStorage.getItem('aceit_seen')||'[]'))}catch(e){}
function saveSeen(){try{localStorage.setItem('aceit_seen',JSON.stringify([...SEEN]))}catch(e){}}
function markSeen(items){(items||[]).forEach(i=>SEEN.add(FAM(i.id)));saveSeen()}
const FAMN=new Set(BANK.map(i=>FAM(i.id))).size;
function pickN(base,count,r,used){ // one question per family, unseen first, never twice in one exam
  if(count<=0)return [];
  const sf=new Set(),L=shuf(base,r).filter(i=>{const f=FAM(i.id);if(used.has(f)||sf.has(f))return false;sf.add(f);return true});
  const fresh=B.avoid?L.filter(i=>!SEEN.has(FAM(i.id))):L;
  let out=draw(fresh,Math.min(count,fresh.length),r);
  if(out.length<count&&B.avoid){const ids=new Set(out.map(i=>i.id));out=out.concat(draw(L.filter(i=>!ids.has(i.id)),count-out.length,r))}
  out.forEach(i=>used.add(FAM(i.id)));
  return out.filter(i=>i.mc).concat(out.filter(i=>!i.mc));
}
function makeExam(){
  const r=rng(B.seed),n=B.n,used=new Set(),flt=(it,x)=>(B.lv==='MH'||it.lv===B.lv)&&(B.fmt==='all'||(B.fmt==='mc')===it.mc)&&(!x||x(it));
  let m,note='';
  if(B.layout==='plan'){
    const n1=Math.ceil(n/2),cur=BANK.filter(it=>B.sk.has(SKEY(it))&&flt(it)),cov=BANK.filter(it=>(B.cov.has(it.domain+'|'+it.skill)||B.sk.has(SKEY(it)))&&flt(it));
    m=[pickN(cur,n1,r,used),pickN(cov,n-n1,r,used)];
    note='Module 1 covers the topics you are studying now. Module 2 is a comprehensive review of everything covered so far.';
  }else if(B.lv==='MH'){
    const nm=Math.floor(n/2);let M=pickN(pool(i=>i.lv==='M'),nm,r,used),H=pickN(pool(i=>i.lv==='H'),n-nm,r,used);
    const need=n-M.length-H.length;if(need>0){const ex=pickN(pool(),need,r,used);M=M.concat(ex.filter(i=>i.lv==='M'));H=H.concat(ex.filter(i=>i.lv!=='M'))}
    m=B.modules===2?[M,H]:[M.concat(H)];
  }else{if(B.modules===2){const P0=pool(),a1=pickN(P0,Math.ceil(n/2),r,used);m=[a1,pickN(P0,Math.floor(n/2),r,used)]}else m=[pickN(pool(),n,r,used)]}
  m=m.filter(x=>x.length).map(x=>x.filter(i=>i.mc).concat(x.filter(i=>!i.mc)));
  const secs=m.map(x=>{const mi=parseFloat(B.mins);return mi>0?Math.round(mi*60):Math.round(x.length*95.45)});
  return {mods:m,secs,title:B.title||'Custom SAT Math exam',note,pr:{on:!!B.proc,max:+B.maxLeave||0,seb:!!B.seb}}}
window.__sat2={get B(){return B},get SEEN(){return SEEN},markSeen,FAM,makeExam}; /* test handle */
