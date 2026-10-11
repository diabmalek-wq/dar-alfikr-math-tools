import sys,re,collections,random; sys.path.insert(0,'/home/claude/cb')
exec(open('/home/claude/cb/gt1.py').read())
HARD=["altitude from $Q$","\\sin\\theta=0.6","length of $\\overline{QS}$","sine of one acute angle is","legs of a right triangle have lengths $x$","x^2+y^2+10x-24y","center on the $x$-axis and passes","slope of the line tangent","$\\overline{PA}$ and $\\overline{PB}$ are tangent","inscribed in the circle so that","radius of a sphere is increased","hemisphere","volumes in the ratio","space diagonal is $26$","water level rise","lateral surface area of the pyramid","bisector of angle $A$","How many different integer lengths","angle $ABD$","Hard-keep"]
for it in I:
    it['diff']="Hard" if any(k in it['q'] for k in HARD) else "Medium"
t=open('/home/claude/sat_bank_all.md').read()
last=max(int(x.split('-')[1]) for x in re.findall(r'^### (GT-\d+)\s*$',t,re.M)); print('last GT',last)
out=[];rows=[];mcn=0;TG=[2,0,3,1,2,0,1,3]
for n,it in enumerate(I,1):
    iid=f"GT-{last+n}"
    if it['opts']:
        tgt=TG[mcn%len(TG)];mcn+=1
        others=[o for j,o in enumerate(it['opts']) if j!=it['correct']]
        random.Random(2000+n).shuffle(others)
        opts=others[:tgt]+[it['opts'][it['correct']]]+others[tgt:];ci=tgt
        ans=f"({L[ci]}) {opts[ci]}"
    else: opts=None;ans=it['ans']
    assert not re.search(r'Choice [A-D]\b|\([A-D]\)',it['rat']),iid
    s=f"### {iid}\n\n**Skill:** {it['skill']}\n**Difficulty:** {it['diff']}\n**Format:** {'Multiple Choice' if opts else 'SPR'}\n\n{SRC}\n\n**Question:** {it['q']}\n"
    if opts: s+="\n"+"\n".join(f"({L[i]}) {o}" for i,o in enumerate(opts))+"\n"
    s+=f"\n**Correct Answer:** {ans}\n\n**Rationale:** {it['rat']}\n\n**Misconception addressed:** {it['mis']}\n\n---\n"
    out.append(s)
    d,sk=it['skill'].split(' — ');rows.append(f"| {iid} | {d} | {sk} | {it['diff']} | {'Multiple Choice' if opts else 'SPR'} |")
head=f"### 2.34 Gap-Closing Batch 4 — Geometry and Trigonometry (Right Triangles, Circles, Area and Volume, Lines, Angles and Triangles) ({len(I)} items — GT-{last+1} to GT-{last+len(I)})\n\nFigure-free items: every diagram is described in words or coordinates so each item prints without a drawing.\n\n"
assert '### 2.34' not in t
t=t.replace("\n## 3. Bank Index (for worksheet sourcing)","\n"+head+"\n".join(out)+"\n## 3. Bank Index (for worksheet sourcing)",1)
k=t.index("\n---\n\n## 4. Next Step")
t=t[:k].rstrip('\n')+"\n"+"\n".join(rows)+"\n"+t[k:]
tot=811+len(I)
t=t.replace("**Item count:** 811 items",f"**Item count:** {tot} items",1)
t=t.replace(" + 61 gap-closing Algebra §2.33;",f" + 61 gap-closing Algebra §2.33 + {len(I)} gap-closing Geometry and Trigonometry §2.34;",1)
t=t.replace("**Status:** Complete — §2.33",f"**Status:** Complete — §2.34 adds {len(I)} Geometry and Trigonometry items (right triangles, circles, area and volume, lines/angles/triangles); §2.33",1)
h=re.findall(r'^### ([A-Z]{1,3}-\d+)\s*$',t,re.M);ix=re.findall(r'^\| ([A-Z]{1,3}-\d+) \|',t,re.M)
print(len(h),len(set(h)),len(ix),set(h)==set(ix))
a=t.index("### Bank summary");b=t.index("### Full index")
rws=re.findall(r'^\| ([A-Z]{1,3}-\d+) \| ([^|]+) \| ([^|]+) \| (Easy|Medium|Hard) \| ([^|]+) \|',t,re.M)
N={'Nonlinear equations in one variable':'Nonlinear equations in one variable and systems of equations in two variables','One-variable data: distributions and measures of center and spread':'One-variable data: Distributions and measures of center and spread','One-variable data: mean, median, range, standard deviation':'One-variable data: Distributions and measures of center and spread'}
sk=collections.defaultdict(lambda:[0,0]);dom={}
for r in rws:
    s_=N.get(r[2].strip(),r[2].strip());sk[s_][0 if r[3]=='Medium' else 1]+=1;dom[s_]=r[1].strip()
Ls=[f"### Bank summary (all {len(rws)} items)","","| Domain | Skill | Medium | Hard | Total |","|---|---|---:|---:|---:|"]
for s_,(m_,h_) in sorted(sk.items(),key=lambda x:(dom[x[0]],x[0])): Ls.append(f"| {dom[s_]} | {s_} | {m_} | {h_} | {m_+h_} |")
Ls.append(f"| **Total** | | **{sum(v[0] for v in sk.values())}** | **{sum(v[1] for v in sk.values())}** | **{len(rws)}** |")
t=t[:a]+"\n".join(Ls)+"\n\n"+t[b:]
open('/home/claude/sat_bank_all.md','w').write(t)
dm=collections.Counter()
for s_,(m_,h_) in sk.items(): dm[dom[s_]]+=m_+h_
print(len(rws),{k:(v,round(v/len(rws)*100,1)) for k,v in dm.items()})
print(collections.Counter(it['diff'] for it in I),collections.Counter(re.findall(r'Correct Answer:\*\* \(([A-D])\)',"\n".join(out))))
