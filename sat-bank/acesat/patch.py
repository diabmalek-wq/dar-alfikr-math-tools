import json,re
src=open('/mnt/user-data/uploads/Downloads/acesat_live_backup.html',encoding='utf8').read()
bank=json.load(open('live_bank.json')); new=json.load(open('new_live_items.json'))
RM=set('PS-093 PS-101 PS-117 PS-094 MR-174 PS-015 PS-208 PS-209 PS-013 PS-096 PS-139'.split())
bank=[b for b in bank if (b['id'][:-2] if b['id'].endswith('-2') else b['id']) not in RM]
print('after removal',len(bank))
have={b['id'] for b in bank}; assert not any(n['id'] in have for n in new)
bank2=bank+new
s0=src.index('<script type="application/json" id="bankdata">')+len('<script type="application/json" id="bankdata">'); e0=src.index('</script>',s0)
js=json.dumps(bank2,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')
h=src[:s0]+js+src[e0:]
# --- planFor with explicit domain split
old_plan=h[h.index('function planFor(n,tf){'):h.index('function realExam(){')]
new_plan=old_plan.replace('function planFor(n,tf){','function planFor(n,tf,domv){').replace("dom=lrAlloc(n,[.35,.35,.15,.15])","dom=domv||lrAlloc(n,[.35,.35,.15,.15])")
assert new_plan!=old_plan
h=h.replace(old_plan,new_plan)
# --- realExam replacement
a=h.index('function realExam(){'); b=h.index('function makeExam(){')
REAL=r'''/* ===== Coverage-aware real exam: every skill appears, most-repeated skills and subtopics weighted higher, adaptive Module 2 ===== */
const SKW={'Linear equations in one variable':1,'Linear equations in two variables':1.2,'Linear functions':1.1,'Systems of linear equations':1.1,'Linear inequalities':.9,
 'Equivalent expressions':1.3,'Nonlinear equations and systems':1.4,'Nonlinear functions':1.5,
 'Ratios, rates and units':1.3,'Percentages':1.2,'One-variable data':1.1,'Two-variable data and scatterplots':1.1,'Probability':.9,'Inference and margin of error':.8,'Statistical claims and studies':.7,
 'Area and volume':1.2,'Lines, angles, and triangles':1.3,'Right triangles and trigonometry':1.3,'Circles':1.1};
const SKBY={};['Algebra','Advanced Math','Problem-Solving and Data Analysis','Geometry and Trigonometry'].forEach(d=>SKBY[d]=[...new Set(BANK.filter(i=>i.domain===d).map(i=>i.skill))]);
const NSKILL=Object.values(SKBY).reduce((a,l)=>a+l.length,0);
function wpick(arr,w,r){const t=w.reduce((a,b)=>a+b,0);let x=r()*t;for(let i=0;i<arr.length;i++){x-=w[i];if(x<=0)return arr[i]}return arr[arr.length-1]}
function skillSlots(d,k,cov,usk,r){ /* uncovered skills first (heaviest first by chance), then the most-repeated skills again */
  const S=SKBY[d],out=[];
  for(let t=0;t<k;t++){const unc=S.filter(s=>!cov.has(s)),P=unc.length?unc:S;
    const pk=wpick(P,P.map(s=>(SKW[s]||1)/(unc.length?1:Math.pow(1+(usk[s]||0),2))),r);
    out.push(pk);cov.add(pk);usk[pk]=(usk[pk]||0)+1}
  return out}
const NEAR={E:['E','M','H'],M:['M','E','H'],H:['H','M','E']};
function pickSlot(s,r,used,usub){
  const ok=(it,lv,sk,mc,fresh)=>it.domain===s.d&&(!sk||it.skill===s.sk)&&it.lv===lv&&(mc===null||it.mc===mc)&&!used.has(FAM(it.id))&&(!fresh||!B.avoid||!SEEN.has(FAM(it.id)));
  const want=!s.sp,att=[];
  [true,false].forEach(fr=>{att.push([s.lv,true,want,fr]);att.push([s.lv,true,!want,fr])});
  NEAR[s.lv].slice(1).forEach(lv=>{att.push([lv,true,want,true]);att.push([lv,true,null,false])});
  NEAR[s.lv].forEach(lv=>att.push([lv,false,null,false]));
  for(const [lv,sk,mc,fr] of att){
    const C=BANK.filter(it=>ok(it,lv,sk,mc,fr));if(!C.length)continue;
    const by={};C.forEach(it=>(by[it.skill+'|'+it.sub]=by[it.skill+'|'+it.sub]||[]).push(it));
    const ks=Object.keys(by),kk=wpick(ks,ks.map(k=>by[k].length/(1+2*(usub[k]||0))),r),L=by[kk],it=L[Math.floor(r()*L.length)];
    usub[kk]=(usub[kk]||0)+1;used.add(FAM(it.id));return it}
  return null}
function realExam(){ /* real digital-SAT structure scaled to B.n questions per module: Module 1 mixed Easy/Medium/Hard; Module 2 harder or easier by Module 1 score */
  const n=Math.max(8,Math.min(22,B.n|0||22)),sp=Math.round(n*.27),r=rng(B.seed),used=new Set(),D=DOMS;
  /* domain split over the whole exam like the real test (Algebra 15, Advanced Math 15, Problem-Solving 7, Geometry 7 of 44), halved between the modules */
  const tot=lrAlloc(2*n,[15,15,7,7]),d1=tot.map(x=>Math.floor(x/2));let rem=n-d1.reduce((a,b)=>a+b,0);
  tot.forEach((x,j)=>{if(rem>0&&x%2){d1[j]++;rem--}});for(let j=0;rem>0;j=(j+1)%4){if(d1[j]<tot[j]){d1[j]++;rem--}}
  const d2=tot.map((x,j)=>x-d1[j]);
  const mod=(plan,cov,usk,usub)=>{const slots=[];
    D.forEach((d,j)=>{const lvs=[];['E','M','H'].forEach(lv=>{for(let q=0;q<(plan[j][lv]||0);q++)lvs.push(lv)});
      const sk=skillSlots(d,lvs.length,cov,usk,r);shuf(lvs,r).forEach((lv,q)=>slots.push({d,lv,sk:sk[q]}))});
    shuf(slots.map((_,i)=>i),r).slice(0,sp).forEach(i=>{slots[i].sp=true});
    const out=slots.map(s=>pickSlot(s,r,used,usub)).filter(Boolean);
    return out.filter(i=>i.mc).concat(out.filter(i=>!i.mc))};
  const cov=new Set(),usk={},usub={};
  const m1=mod(planFor(n,{E:7/22,M:9/22,H:6/22},d1),cov,usk,usub);
  const route=tf=>mod(planFor(n,tf,d2),new Set(cov),Object.assign({},usk),Object.assign({},usub));
  const hard=route({M:8/22,H:14/22}),easy=route({E:12/22,M:10/22});
  const secs=Math.round(n*95.45),skills=l=>new Set(l.map(i=>i.skill));
  const cv=[...skills(m1.concat(hard))].length,cve=[...skills(m1.concat(easy))].length;
  return {mods:[m1,hard],alt:{hard,easy,cut:Math.round(n*15/22)},real:true,secs:[secs,secs],cov:{hard:cv,easy:cve,of:NSKILL},title:B.title||'SAT Math adaptive mock exam',pr:{on:!!B.proc,max:+B.maxLeave||0,seb:!!B.seb}}}
'''
h=h[:a]+REAL+h[b:]
# --- start-page text
h=h.replace("<span>Algebra, Advanced Math, Problem-Solving and Data Analysis, Geometry and Trigonometry, weighted like the real test.</span>","<span>Weighted like the real test: Algebra and Advanced Math about 34% each, Problem-Solving and Data Analysis and Geometry and Trigonometry about 16% each. Every skill is drawn at least once, as far as the length allows, and the most repeated skills and subtopics are drawn most often. At full length (22 + 22) all ${NSKILL} skills appear.</span>")
open('/home/claude/acesat_new.html','w',encoding='utf8').write(h)
print(len(h),len(bank2))
