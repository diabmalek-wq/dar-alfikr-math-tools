import sys,re,collections,random; sys.path.insert(0,'/home/claude/cb')
exec(open('/home/claude/cb/alg3.py').read())
t=open('/home/claude/sat_bank_all.md').read()
last=max(int(x.split('-')[1]) for x in re.findall(r'^### (A-\d+)\s*$',t,re.M)); print('last A',last)
out=[];rows=[];mcn=0;TG=[2,0,3,1,2,0,1,3]
for n,it in enumerate(I,1):
    iid=f"A-{last+n}"
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
head=f"### 2.35 Gap-Closing Batch 5 — Algebra Top-Up (Linear Equations, Lines, Linear Functions, Inequalities, Systems) ({len(I)} items — A-{last+1} to A-{last+len(I)})\n\nFigure-free items; all answers verified programmatically.\n\n"
assert '### 2.35' not in t
t=t.replace("\n## 3. Bank Index (for worksheet sourcing)","\n"+head+"\n".join(out)+"\n## 3. Bank Index (for worksheet sourcing)",1)
k=t.index("\n---\n\n## 4. Next Step")
t=t[:k].rstrip('\n')+"\n"+"\n".join(rows)+"\n"+t[k:]
tot=861+len(I)
t=t.replace("**Item count:** 861 items",f"**Item count:** {tot} items",1)
t=t.replace(" + 30 gap-closing §2.32 the earlier"," + 30 gap-closing §2.32 + 61 gap-closing Algebra §2.33 + 50 gap-closing Geometry and Trigonometry §2.34 + %d gap-closing Algebra top-up §2.35; the earlier"%len(I),1)
t=t.replace("**Status:** Complete — §2.34",f"**Status:** Complete — §2.35 adds {len(I)} Algebra top-up items (linear equations, lines, linear functions, inequalities, systems); §2.34",1)
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
