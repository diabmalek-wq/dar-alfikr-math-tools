// Prezi-style FIKR deck engine. usage: node engine.js cfg/<id>.json  -> raw_<id>.pptx
const pptxgen=require('pptxgenjs'),fs=require('fs'),crypto=require('crypto');
const cfg=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
const MD='m_'+cfg.id; const IDX=JSON.parse(fs.readFileSync(MD+'/_index.json','utf8'));
const L='../';
const C={NAVY:'1F3864',INK:'222E2D',TEAL:'17A199',DEEP:'0E4F4C',OR:'E8762C',GOLD:'F0B323',BG:'F4F8F7',WHITE:'FFFFFF'};
const key=(t,c='222E2D')=>'k'+crypto.createHash('md5').update(c+'|'+t,'utf8').digest('hex').slice(0,10);
const K=(t,w)=>key(t,w?'FFFFFF':'222E2D');
const pres=new pptxgen(); pres.layout='LAYOUT_WIDE'; pres.title=cfg.outName; pres.author='Mr Malek Thiab';
const ST=[['Diagnose','6 min'],['Targeted Instruction','18 min'],['Practice','12 min'],['Production','12 min'],['Mastery Gate','6 min'],['Smart Production','6 min']];
const FONT='Calibri',HEAD='Cambria',CODES=cfg.codes;
const sh=()=>({type:'outer',color:'000000',opacity:0.15,blur:8,offset:2,angle:90});
function M(s,k,x,y,sc=1.6,maxW=99){const m=IDX[k]; if(!m) throw new Error('no math '+k); sc=Math.min(sc,maxW/m.win); const w=m.win*sc,h=m.hin*sc; s.addImage({path:MD+'/'+k+'.png',x,y,w,h}); return {w,h};}
function Mc(s,k,cx,y,sc,maxW){const m=IDX[k]; if(!m) throw new Error('no math '+k); sc=Math.min(sc,maxW/m.win); return M(s,k,cx-m.win*sc/2,y,sc,maxW);}
// stack math images vertically centred horizontally in box; auto-shrink to fit height
function stack(s,items,cx,y0,maxH,maxW,sc=1.8,gap=0.2){ // items: [{k,gapBefore?}]
  const dim=it=>{const m=IDX[it.k]; if(!m) throw new Error('no math '+it.k); const f=Math.min(sc*(it.sc||1),maxW/m.win); return {w:m.win*f,h:m.hin*f};};
  let tot=items.reduce((a,it,i)=>a+dim(it).h+(i?gap:0),0), f=Math.min(1,maxH/tot); let y=y0;
  items.forEach((it,i)=>{const m=IDX[it.k]; const ff=Math.min(sc*(it.sc||1),maxW/m.win)*f; const w=m.win*ff,h=m.hin*ff; s.addImage({path:MD+'/'+it.k+'.png',x:cx-w/2,y,w,h}); y+=h+gap*f;});
  return y;}
function card(s,x,y,w,h,fill=C.WHITE,line){s.addShape('roundRect',{x,y,w,h,rectRadius:0.12,fill:{color:fill},line:line?{color:line,width:1.25}:{color:'DDE6E4',width:0.75},shadow:sh()});}
function txt(s,t,o){s.addText(t,Object.assign({fontFace:FONT,color:C.INK,fontSize:16,margin:0,isTextBox:true,valign:'top'},o));}
let N=0;
function circles(s){s.addShape('ellipse',{x:-1.2,y:5.2,w:3.4,h:3.4,fill:{color:C.TEAL,transparency:88},line:{color:C.TEAL,transparency:100}}); s.addShape('ellipse',{x:11.2,y:-1.3,w:3.2,h:3.2,fill:{color:C.GOLD,transparency:86},line:{color:C.GOLD,transparency:100}});}
function footer(s,dark){const fs=CODES.length>70?7:CODES.length>45?8:8.5;
  txt(s,CODES,{x:0.4,y:7.06,w:5.2,h:0.34,fontSize:fs,color:dark?'BFD8D5':'5A6B69'});
  txt(s,'FAITH, RIGHTEOUSNESS AND WISDOM',{x:5.75,y:7.1,w:3.6,h:0.25,fontSize:9.5,bold:true,color:dark?'FFFFFF':C.NAVY,align:'center',charSpacing:2});
  txt(s,'Mr Malek Thiab  ·  '+N,{x:9.7,y:7.1,w:3.25,h:0.25,fontSize:10,color:dark?'BFD8D5':'5A6B69',align:'right'});}
function chrome(s,dark){s.addImage({path:L+(dark?'dept_logo_white.png':'dept_logo.png'),x:0.4,y:0.22,w:1.62,h:0.5}); s.addImage({path:L+(dark?'school_logo_white.png':'school_logo.png'),x:12.35,y:0.18,w:0.62,h:0.62}); footer(s,dark);}
function crumb(s,active){for(let i=0;i<6;i++){const on=i===active,d=on?0.5:0.3,cx=4.55+i*0.78,cy=0.5;
  s.addShape('ellipse',{objectName:'stn'+(i+1),x:cx-d/2,y:cy-d/2,w:d,h:d,fill:{color:on?C.OR:C.TEAL},line:{color:C.WHITE,width:1.5}});
  txt(s,String(i+1),{x:cx-0.2,y:cy-0.12,w:0.4,h:0.24,fontSize:on?12:9,bold:true,color:C.WHITE,align:'center',valign:'middle'});
  if(i<5) s.addShape('line',{objectName:'path'+(i+1),x:cx+d/2+0.02,y:cy,w:0.78-d/2-(i+1===active?0.25:0.15)-0.02,h:0,line:{color:C.TEAL,width:2,dashType:'dash'}});}}
const STD=(cfg.standardsSlide=cfg.standards.length>4||cfg.standards.reduce((a,s)=>a+s.text.length,0)>700);
const shiftNotes=t=>STD?t.replace(/\b([Ss]lide )(\d+)/g,(m,a,n)=>+n>=4?a+(+n+1):m):t;
function slide(title,st,notes,opts={}){N++; const s=pres.addSlide(); s.background={color:opts.dark?C.DEEP:C.BG}; circles(s); chrome(s,opts.dark); if(st!=null)crumb(s,st);
  if(title){ if(st!=null) txt(s,('STATION '+(st+1)+'  ·  '+ST[st][0]+'  ·  '+ST[st][1]).toUpperCase(),{x:0.5,y:0.98,w:9,h:0.3,fontSize:12,bold:true,color:C.OR,charSpacing:2});
    txt(s,title,{x:0.5,y:st==null?0.9:1.25,w:12.3,h:st==null?0.5:0.6,fontSize:title.length>48?26:30,bold:true,fontFace:HEAD,color:C.NAVY,valign:'middle'});}
  s.addNotes(shiftNotes(notes)); return s;}
const nb=(s,x,y,i,col=C.TEAL)=>{s.addShape('ellipse',{x,y,w:0.55,h:0.55,fill:{color:col},line:{color:C.WHITE}}); txt(s,String(i),{x,y,w:0.55,h:0.55,fontSize:18,bold:true,color:C.WHITE,align:'center',valign:'middle'});};
const lab=(s,t,x,y,w=4)=>txt(s,t,{x,y,w,h:0.25,fontSize:11,bold:true,color:C.OR,charSpacing:2});
const bullets=(arr,o={})=>arr.map((t,i)=>({text:t,options:{bullet:o.num?{type:'number'}:true,breakLine:i<arr.length-1,paraSpaceAfter:o.sp||8}}));
let b_title='';function rule(s,rules,y=1.95,h=1.2){card(s,0.5,y,12.3,h,C.DEEP); const ms=rules.map(r=>IDX[K(r,1)]); const gap=0.7, avail=12.3-0.6-gap*(rules.length-1);
  const sc=Math.min(2.0,(h-0.3)/Math.max(...ms.map(m=>m.hin)),avail/ms.reduce((a,m)=>a+m.win,0)); const tot=ms.reduce((a,m)=>a+m.win*sc,0)+gap*(rules.length-1); let x=0.5+(12.3-tot)/2; console.log('rule sc',sc.toFixed(2),b_title||'');
  rules.forEach((r,i)=>{const m=ms[i]; M(s,K(r,1),x,y+(h-m.hin*sc)/2,sc,99); x+=m.win*sc+gap;});}
// ---- station circle layout
const cx=[1.5,3.65,5.8,7.95,10.1,12.0],cy=[4.7,3.5,4.7,3.5,4.7,3.5],D=1.45;
function journey(recap){N++; const s=pres.addSlide(); s.background={color:C.DEEP};
  s.addShape('ellipse',{x:-1.2,y:5.0,w:3.8,h:3.8,fill:{color:C.TEAL,transparency:80},line:{color:C.TEAL,transparency:100}}); s.addShape('ellipse',{x:10.8,y:-1.2,w:3.6,h:3.6,fill:{color:C.GOLD,transparency:82},line:{color:C.GOLD,transparency:100}});
  s.addImage({path:L+'dept_logo_white.png',x:0.4,y:0.22,w:1.62,h:0.5}); s.addImage({path:L+'school_logo_white.png',x:12.35,y:0.18,w:0.62,h:0.62});
  txt(s,recap?'Journey complete':"Today's journey",{x:0.6,y:0.95,w:12,h:0.8,fontSize:40,bold:true,fontFace:HEAD,color:C.WHITE});
  if(!recap) txt(s,'Six stations. Each one zooms in as we arrive.',{x:0.6,y:1.7,w:12,h:0.4,fontSize:18,color:'BFD8D5'});
  for(let i=0;i<5;i++){const x1=cx[i],y1=cy[i],x2=cx[i+1],y2=cy[i+1]; s.addShape('line',{objectName:'path'+(i+1),x:x1,y:Math.min(y1,y2),w:x2-x1,h:Math.abs(y2-y1),flipV:y2<y1,line:{color:C.GOLD,width:3,dashType:'dash'}});}
  for(let i=0;i<6;i++){s.addShape('ellipse',{objectName:'stn'+(i+1),x:cx[i]-D/2,y:cy[i]-D/2,w:D,h:D,fill:{color:recap?C.GOLD:(i===0?C.OR:C.TEAL)},line:{color:C.WHITE,width:3}});
    txt(s,recap?'✓':String(i+1),{x:cx[i]-0.4,y:cy[i]-0.3,w:0.8,h:0.6,fontSize:recap?32:30,bold:true,fontFace:HEAD,color:recap?C.DEEP:C.WHITE,align:'center',valign:'middle'});
    const above=cy[i]<4; txt(s,recap?ST[i][0]:ST[i][0]+'\n'+ST[i][1],{x:cx[i]-1.05,y:above?cy[i]-D/2-(recap?0.7:0.95):cy[i]+D/2+0.12,w:2.1,h:recap?0.6:0.8,fontSize:recap?16:17,bold:true,color:C.WHITE,align:'center',valign:above?'bottom':'top'});}
  if(recap) txt(s,cfg.recap,{x:0.6,y:6.2,w:12.1,h:0.7,fontSize:cfg.recap.length>95?17:19,color:C.GOLD,align:'center',bold:true,valign:'middle'});
  txt(s,'FAITH, RIGHTEOUSNESS AND WISDOM',{x:4.4,y:7.1,w:4.5,h:0.25,fontSize:10,bold:true,color:C.WHITE,align:'center',charSpacing:3});
  return s;}
const nxt=cfg.smart.next;
// ---------- 1 TITLE
{N++; const s=pres.addSlide(); s.background={color:C.BG};
 s.addShape('ellipse',{x:7.2,y:1.6,w:8.6,h:8.6,fill:{color:C.DEEP},line:{color:C.DEEP}}); s.addShape('ellipse',{x:9.4,y:-1.6,w:3.6,h:3.6,fill:{color:C.GOLD,transparency:70},line:{color:C.GOLD,transparency:100}}); s.addShape('ellipse',{x:-1.4,y:4.4,w:3.6,h:3.6,fill:{color:C.TEAL,transparency:85},line:{color:C.TEAL,transparency:100}});
 s.addImage({path:L+'dept_logo.png',x:0.4,y:0.22,w:1.62,h:0.5}); s.addImage({path:L+'cognia_badge.png',x:5.1,y:0.1,w:1.3,h:0.975}); s.addImage({path:L+'school_logo.png',x:12.35,y:0.18,w:0.62,h:0.62});
 txt(s,[cfg.grade,cfg.course,cfg.topicNo].join('  ·  '),{x:0.7,y:2.0,w:7,h:0.3,fontSize:14,bold:true,color:C.OR,charSpacing:3});
 txt(s,cfg.lessonNo,{x:0.7,y:2.4,w:6.5,h:0.6,fontSize:26,fontFace:HEAD,color:C.TEAL,bold:true});
 const mx=Math.max(...cfg.titleLines.map(l=>l.length)); const fsz=mx<=14?50:mx<=17?44:mx<=20?38:34;
 txt(s,cfg.titleLines.join('\n'),{x:0.7,y:3.0,w:6.6,h:1.9,fontSize:fsz,bold:true,fontFace:HEAD,color:C.NAVY});
 txt(s,cfg.topicTitle,{x:0.7,y:5.0,w:6.6,h:0.4,fontSize:18}); txt(s,'Mr Malek Thiab',{x:0.7,y:5.55,w:5,h:0.4,fontSize:18,bold:true});
 Mc(s,K(cfg.titleMath,1),11.0,3.3,2.6,3.6); txt(s,'Journey of 6 stations, 60 minutes',{x:8.9,y:4.55,w:4.2,h:0.4,fontSize:16,color:C.WHITE,align:'center'});
 txt(s,'FAITH, RIGHTEOUSNESS AND WISDOM',{x:0.4,y:7.1,w:6.5,h:0.25,fontSize:10,bold:true,color:C.NAVY,charSpacing:3});
 s.addNotes(cfg.titleNotes||('Speaker notes: Welcome to '+cfg.lessonNo+': '+cfg.titleLines.join(' ')+'.\nTiming: 60 minutes (Diagnose 6, Targeted Instruction 18, Practice 12, Production 12, Mastery Gate 6, Smart Production 6). For a 40-minute class scale every station by two thirds.\nThe journey map on the next slide shows the six stations; in slideshow mode the Morph transition zooms the station circles into the breadcrumb at the top of every later slide.'));
}
// ---------- 2 JOURNEY
{const s=journey(false); s.addNotes('Speaker notes: This is the whole map. Walk it left to right: Diagnose (what we already know), Targeted Instruction ('+cfg.blocks.map(b=>b.title).join('; ')+'), Practice (Practice, Apply, Investigate), Production ('+cfg.production.title+'), Mastery Gate (three questions to pass), Smart Production (create, then Time to Check).\nIn slideshow mode the Morph transition animates these circles shrinking into the breadcrumb on later slides; without Morph the slides fade.\nAsk the class which station they think will be hardest.');}
// ---------- 3 OBJECTIVES
{const hasEQ=!!(cfg.eq||cfg.mps); const s=slide('What we are learning',null,'Speaker notes: Read the objectives aloud one at a time and have students say which one they feel least sure about.\nVocabulary used today: '+cfg.vocab.join(', ')+'.\nStandards '+(STD?'are on the next slide.':'are listed on this slide.')+(hasEQ?'':'\nThe essential question and mathematical practices are not shown because they are not in the project documents; add them from the curriculum map if you want them displayed.'));
 const ol=cfg.objectives.reduce((a,t)=>a+t.length,0); const ofs=ol>420?14:ol>300?16:17;
 const oh=hasEQ?4.0:5.5; card(s,0.5,1.4,6.3,oh); lab(s,'OBJECTIVES',0.8,1.5);
 txt(s,cfg.objectives.map((t,i,a)=>({text:t,options:{bullet:{type:'number'},breakLine:i<a.length-1,paraSpaceAfter:9}})),{x:0.8,y:1.85,w:5.8,h:oh-0.6,fontSize:ofs});
 if(hasEQ){card(s,0.5,5.55,6.3,1.35,C.DEEP); if(cfg.eq){lab(s,'ESSENTIAL QUESTION',0.8,5.65,4); txt(s,cfg.eq,{x:0.8,y:5.92,w:5.7,h:0.5,fontSize:cfg.eq.length>70?12.5:14,color:C.WHITE,bold:true});}
   if(cfg.mps){txt(s,'MATHEMATICAL PRACTICES   '+cfg.mps.join('  ·  '),{x:0.8,y:6.5,w:5.7,h:0.3,fontSize:12,bold:true,color:C.GOLD});}}
 const vr=Math.ceil(cfg.vocab.length/2), vh=Math.min(5.5,0.6+vr*0.33+0.1); card(s,7.0,1.4,5.8,vh); lab(s,'VOCABULARY',7.3,1.5);
 cfg.vocab.forEach((t,i)=>{const col=i%2,row=Math.floor(i/2); s.addShape('roundRect',{x:7.25+col*2.8,y:1.85+row*0.33,w:2.7,h:0.29,rectRadius:0.14,fill:{color:[C.TEAL,C.NAVY,C.OR][row%3]},line:{color:C.WHITE}}); txt(s,t,{x:7.25+col*2.8,y:1.85+row*0.33,w:2.7,h:0.29,fontSize:t.length>26?9.5:11,bold:true,color:C.WHITE,align:'center',valign:'middle'});});
 if(!STD){const y=1.4+vh+0.15; card(s,7.0,y,5.8,6.9-y); lab(s,'STANDARDS',7.3,y+0.08);
  txt(s,cfg.standards.flatMap((st,i,a)=>[{text:st.code+'  ',options:{bold:true}},{text:st.text,options:{breakLine:i<a.length-1,paraSpaceAfter:4}}]),{x:7.3,y:y+0.4,w:5.3,h:6.9-y-0.5,fontSize:10.5});}
}
// ---------- 3b STANDARDS
if(STD){const tot=cfg.standards.reduce((a,s)=>a+s.text.length+s.code.length,0); const fz=tot>1500?14:tot>1100?15:16;
 const s=slide('Standards',null,'Speaker notes: Standards are quoted verbatim from the curriculum map. Students do not need to read them aloud; point to the ones that match today\'s objectives.');
 const half=[[],[]]; let acc=0; cfg.standards.forEach(st=>{(acc<tot/2?half[0]:half[1]).push(st); acc+=st.text.length+st.code.length;});
 half.forEach((h,i)=>{const x=0.5+i*6.25; card(s,x,1.5,6.05,5.4); txt(s,h.flatMap((st,j,a)=>[{text:st.code+'  ',options:{bold:true,color:C.TEAL}},{text:st.text,options:{breakLine:j<a.length-1,paraSpaceAfter:9}}]),{x:x+0.3,y:1.75,w:5.45,h:4.95,fontSize:fz});});
}
// ---------- DIAGNOSE
{const d=cfg.diagnose; const s=slide('Start here: three quick checks',0,'Speaker notes (Diagnose, 6 min, no calculator):\n'+d.notes);
 d.items.forEach((t,i)=>{const x=0.5+i*4.1; card(s,x,2.1,3.95,2.4); nb(s,x+0.2,2.25,i+1); stack(s,[{k:K(t)}],x+2.0,2.95,1.45,3.7,2.0);});
 card(s,0.5,4.85,12.3,1.6,C.DEEP); txt(s,'Done when',{x:0.85,y:5.0,w:4,h:0.35,fontSize:14,bold:true,color:C.GOLD}); txt(s,d.doneWhen,{x:0.85,y:5.4,w:11.6,h:0.9,fontSize:d.doneWhen.length>140?16:18,color:C.WHITE});
}
// ---------- BLOCKS
cfg.blocks.forEach((b,bi)=>{b_title=b.title;const s=slide(b.title,1,'Speaker notes (Targeted Instruction, block '+(bi+1)+' of '+cfg.blocks.length+'):\n'+b.notes);
 rule(s,b.rules,1.95,1.2); const ex=b.examples, n=ex.length;
 let boxes; if(b.fig){boxes=[[4.8,3.8],[8.75,4.05]];} else if(n===2) boxes=[[0.5,6.05],[6.75,6.05]]; else boxes=[[0.5,4.0],[4.65,4.0],[8.8,4.0]];
 if(b.fig){boxes=[[4.95,3.85],[8.95,3.85]]; card(s,0.5,3.4,4.3,3.45); const f=b.fig,ar=f.w/f.h; let w=4.0,h=w/ar; if(h>3.15){h=3.15;w=h*ar;} s.addImage({path:b.fig.file,x:0.5+(4.3-w)/2,y:3.4+(3.45-h)/2,w,h});}
 ex.forEach((e,i)=>{const [x,w]=boxes[i]; card(s,x,3.4,w,3.45); lab(s,'EXAMPLE '+'ABC'[i],x+0.25,3.5,3);
   stack(s,[{k:K(e.q),sc:1.05},...e.steps.map(t=>({k:K(t)}))],x+w/2,3.9,2.85,w-0.4,1.8,0.17);});
});
// ---------- PRACTICE
{const p=cfg.practice; const s=slide('Give it a go: Practice, Apply, Investigate',2,'Speaker notes (Practice, 12 min; tierless differentiation: students choose the starting column and may move across):\n'+p.notes);
 [['practice','PRACTICE','Secure the method',C.TEAL],['apply','APPLY','Use it in context',C.OR],['investigate','INVESTIGATE','Find out why',C.NAVY]].forEach(([k,h,sub,col],i)=>{const x=0.5+i*4.15; s.addShape('roundRect',{x,y:2.0,w:3.95,h:0.85,rectRadius:0.12,fill:{color:col},line:{color:C.WHITE}}); txt(s,h,{x:x+0.25,y:2.07,w:3.5,h:0.4,fontSize:20,bold:true,color:C.WHITE}); txt(s,sub,{x:x+0.25,y:2.45,w:3.5,h:0.3,fontSize:13,color:C.WHITE});
   card(s,x,2.95,3.95,3.95); stack(s,p[k].items.map(t=>({k:K(t)})),x+1.975,3.2,2.35,3.7,2.0,0.3); txt(s,p[k].done,{x:x+0.25,y:5.7,w:3.5,h:1.1,fontSize:p[k].done.length>90?11.5:12.5,color:'3F4B49',valign:'bottom'});});
}
// ---------- PRODUCTION
{const p=cfg.production; const s=slide('Production: '+p.title,3,'Speaker notes (Production, 12 min):\n'+p.notes);
 card(s,0.5,2.0,6.4,4.85); lab(s,'THE MODEL',0.8,2.1);
 const cl=p.context.length; const cf=cl>330?13:cl>260?14:15; const ch=cl>330?1.6:cl>260?1.4:1.25;
 txt(s,p.context,{x:0.8,y:2.4,w:5.8,h:ch,fontSize:cf});
 const gy=2.4+ch+0.1; const ey=stack(s,p.given.map(t=>({k:K(t)})),3.7,gy,1.15,5.6,1.6,0.12);
 txt(s,p.tasks.map((t,i,a)=>({text:t,options:{bullet:{type:'number'},breakLine:i<a.length-1,paraSpaceAfter:4}})),{x:0.8,y:ey+0.15,w:5.8,h:6.8-ey-0.15,fontSize:p.tasks.some(t=>t.length>70)?13:14});
 card(s,7.1,2.0,5.7,4.85,C.DEEP); lab(s,'DONE WHEN',7.4,2.1);
 txt(s,p.doneWhen.map((t,i,a)=>({text:t,options:{bullet:true,breakLine:i<a.length-1,paraSpaceAfter:9}})),{x:7.4,y:2.5,w:5.1,h:3.2,fontSize:p.doneWhen.some(t=>t.length>70)?14:15.5,color:C.WHITE});
 txt(s,p.hint,{x:7.4,y:5.8,w:5.1,h:0.9,fontSize:12.5,italic:true,color:C.GOLD});
}
// ---------- GATE
{const g=cfg.gate; const s=slide('Mastery Gate: three questions to pass',4,'Speaker notes (Mastery Gate, 6 min, no calculator):\n'+g.notes);
 g.items.forEach((t,i)=>{const x=0.5+i*4.1; card(s,x,2.1,3.95,2.5,C.WHITE,C.OR); nb(s,x+0.2,2.25,i+1,C.OR); stack(s,[{k:K(t)}],x+2.0,3.0,1.4,3.5,1.9);});
 card(s,0.5,4.9,12.3,1.7,C.DEEP); txt(s,'Pass mark',{x:0.85,y:5.05,w:4,h:0.35,fontSize:14,bold:true,color:C.GOLD}); txt(s,'3 of 3 correct unlocks Station 6. Fewer than that: return to the slide for the question you missed, redo it, then re-take the gate.',{x:0.85,y:5.45,w:11.6,h:1.0,fontSize:18,color:C.WHITE});
}
// ---------- SMART
{const m=cfg.smart; const s=slide('Smart Production: make one, then check it',5,'Speaker notes (Smart Production, 6 min):\n'+m.notes);
 card(s,0.5,2.0,6.1,4.85); s.addShape('roundRect',{x:0.8,y:2.2,w:2.6,h:0.5,rectRadius:0.25,fill:{color:C.TEAL},line:{color:C.WHITE}}); txt(s,'CREATE',{x:0.8,y:2.2,w:2.6,h:0.5,fontSize:16,bold:true,color:C.WHITE,align:'center',valign:'middle'});
 txt(s,m.create.map((t,i,a)=>({text:t,options:{bullet:{type:'number'},breakLine:i<a.length-1,paraSpaceAfter:8}})),{x:0.8,y:2.95,w:5.5,h:2.7,fontSize:m.create.some(t=>t.length>80)?15:17});
 txt(s,m.createDone,{x:0.8,y:5.7,w:5.5,h:1.0,fontSize:14,color:'3F4B49'});
 card(s,6.8,2.0,6.0,4.85,C.DEEP); s.addShape('roundRect',{x:7.1,y:2.2,w:2.9,h:0.5,rectRadius:0.25,fill:{color:C.GOLD},line:{color:C.WHITE}}); txt(s,'TIME TO CHECK',{x:7.1,y:2.2,w:2.9,h:0.5,fontSize:16,bold:true,color:C.INK,align:'center',valign:'middle'});
 txt(s,m.exitIntro,{x:7.1,y:2.95,w:5.4,h:0.9,fontSize:16,color:C.WHITE});
 s.addShape('roundRect',{x:7.1,y:3.95,w:5.4,h:1.35,rectRadius:0.1,fill:{color:C.WHITE},line:{color:C.WHITE}}); stack(s,m.exit.map(t=>({k:K(t)})),9.8,4.05,1.15,5.0,1.6,0.1);
 txt(s,nxt,{x:7.1,y:5.55,w:5.4,h:0.9,fontSize:15,color:'BFD8D5'});
}
// ---------- EXAM
{const e=cfg.exam; const s=slide('Exam connections',null,'Speaker notes: each exam item is worked in numbered steps.\n'+e.notes);
 [['SAT','sat',C.TEAL],['GAT','gat',C.OR],['SAAT','saat',C.NAVY]].forEach(([t,k,col],i)=>{const x=0.5+i*4.15; s.addShape('roundRect',{x,y:1.4,w:3.95,h:0.6,rectRadius:0.12,fill:{color:col},line:{color:C.WHITE}}); txt(s,t,{x:x+0.25,y:1.4,w:3.4,h:0.6,fontSize:20,bold:true,color:C.WHITE,valign:'middle'});
   card(s,x,2.1,3.95,4.8); const yq=stack(s,e[k].q.map(q=>({k:K(q)})),x+1.975,2.35,1.3,3.65,1.5,0.1); lab(s,'STEPS',x+0.25,Math.max(yq+0.1,3.55),2);
   let y=Math.max(yq+0.4,3.9); const room=6.7-y; const sg=Math.min(0.95,room/e[k].steps.length);
   e[k].steps.forEach((st,j)=>{const m=IDX[K(st)]; const f=Math.min(1.6,3.1/m.win,(sg-0.12)/m.hin); txt(s,String(j+1),{x:x+0.25,y:y+j*sg,w:0.4,h:0.4,fontSize:16,bold:true,color:col}); M(s,K(st),x+0.7,y+j*sg,f,99);});});
}
// ---------- RECAP
{const s=journey(true); s.addNotes(shiftNotes('Speaker notes: Every station is checked off. Recap in one sentence: '+cfg.recap+' Collect the Time to Check responses. '+nxt));}
pres.writeFile({fileName:'raw_'+cfg.id+'.pptx'}).then(()=>console.log('ok',cfg.id,N,'slides',STD?'(standards slide)':''));
