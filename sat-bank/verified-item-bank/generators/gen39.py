import re,collections,random
exec(open('/home/claude/cb/batch39.py').read())
L="ABCD"
t=open('/home/claude/cb/bank_new2.md').read()
assert '### 2.39' not in t
out=[];rows=[];TG=[1,3,0,2,1,2,0,3];mc=0
for n,it in enumerate(I,1):
    q=it['q'].replace('\\n','\n')
    if it['opts']:
        tgt=TG[mc%len(TG)];mc+=1
        others=[o for j,o in enumerate(it['opts']) if j!=it['correct']]
        random.Random(3900+n).shuffle(others)
        opts=others[:tgt]+[it['opts'][it['correct']]]+others[tgt:]
        ans=f"({L[tgt]}) {opts[tgt]}"
    else: opts=None;ans=it['ans']
    assert not (opts and re.search(r'Choice [A-D]\b|option \([A-D]\)',it['rat'])),it['id']
    s=f"### {it['id']}\n\n**Skill:** {it['skill']}\n**Difficulty:** {it['diff']}\n**Format:** {'Multiple Choice' if opts else 'SPR'}\n\n**Source:** {SRC}\n\n**Question:** {q}\n"
    if opts: s+="\n"+"\n".join(f"({L[i]}) {o}" for i,o in enumerate(opts))+"\n"
    s+=f"\n**Correct Answer:** {ans}\n\n**Rationale:** {it['rat']}\n\n**Misconception addressed:** {it['mis']}\n\n---\n"
    out.append(s)
    d,sk=it['skill'].split(' — ');rows.append(f"| {it['id']} | {d} | {sk} | {it['diff']} | {'Multiple Choice' if opts else 'SPR'} |")
ids=[it['id'] for it in I]; pre=sorted({i.split('-')[0]+'-'+str(int(i.split('-')[1])) for i in ids})
head=f"### 2.39 Gap-Closing Batch 7 — Thin Skills and Open Archetypes ({len(I)} items — PS-133 to PS-156, AM-288 to AM-302, GT-226 to GT-231)\n\nBuilt after a gap review of the 11-session plan. Targets: evaluating statistical claims (4), inference and margin of error (6), probability and conditional probability (7), two-variable data (7), function composition and transformations (7), sum and product of solutions (4), and similar triangles with area ratios (6). A web sweep of public prep pages supplied archetypes only; every item is original, every answer was computed by script, and each item was screened against the whole bank (candidates that repeated an existing archetype were replaced).\n\n"
t=t.replace("\n## 3. Bank Index (for worksheet sourcing)","\n"+head+"\n".join(out)+"\n## 3. Bank Index (for worksheet sourcing)",1)
k=t.index("\n---\n\n## 4. Next Step")
t=t[:k].rstrip('\n')+"\n"+"\n".join(rows)+"\n"+t[k:]
t=t.replace("**Item count:** 949 items",f"**Item count:** {949+len(I)} items",1)
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
open('/home/claude/cb/bank_new3.md','w').write(t)
print("\n".join(Ls))
print(collections.Counter(re.findall(r'Correct Answer:\*\* \(([A-D])\)',"\n".join(out))))
