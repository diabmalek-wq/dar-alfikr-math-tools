import re,collections,random,json
exec(open('/home/claude/cb/batch40.py').read())
L="ABCD"
t=open('/home/claude/tp2/bank.md').read()
assert '### 2.40' not in t
out=[];rows=[];TG=[1,3,0,2,2,0,3,1];mc=0;final=[]
for n,it in enumerate(I,1):
    q=it['q']
    if it['opts']:
        tgt=TG[mc%len(TG)];mc+=1
        others=[o for j,o in enumerate(it['opts']) if j!=it['correct']]
        random.Random(4000+n).shuffle(others)
        opts=others[:tgt]+[it['opts'][it['correct']]]+others[tgt:]
        ans=f"({L[tgt]}) {opts[tgt]}";key=L[tgt]
    else: opts=None;ans=it['ans'];key=None
    final.append(dict(it,opts_final=opts,ans_final=ans,key=key))
    s=f"### {it['id']}\n\n**Skill:** {it['skill']}\n**Difficulty:** {it['diff']}\n**Format:** {'Multiple Choice' if opts else 'SPR'}\n**Tool:** {it['tool']}\n\n**Source:** {SRC}\n\n**Question:** {q}\n"
    if opts: s+="\n"+"\n".join(f"({L[i]}) {o}" for i,o in enumerate(opts))+"\n"
    s+=f"\n**Correct Answer:** {ans}\n\n**Rationale:** {it['rat']}\n\n**Misconception addressed:** {it['mis']}\n\n---\n"
    out.append(s)
    d,sk=it['skill'].split(' — ');rows.append(f"| {it['id']} | {d} | {sk} | {it['diff']} | {'Multiple Choice' if opts else 'SPR'} |")
json.dump(final,open('/home/claude/cb/tp2_final.json','w'))
head=f"### 2.40 Web Research Batch 3 — Trick Pack 2 ({len(I)} items — A-316 to A-335, AM-303 to AM-321, GT-232 to GT-257, PS-157 to PS-175)\n\nBuilt 21 Oct 2026 from a five-agent web sweep of sources not used before: Bluebook Practice Tests 4–10 Module 2 walkthroughs (schoolofmath.us), real-test recaps for 2025–2026 administrations (test-ninjas.com exam-feedback pages, thetestadvantage.com August 2026 recap), and prep guides (outlierlearning, fiveable, targettestprep, magoosh, apguru, open-exam-prep, varsitytutors, quadeducationgroup, tigerway). About 87 candidate archetypes were screened against the 994-item bank by keyword search; 84 new tricks were kept. Archetype only: no source item, wording or numbers reproduced. Every answer was checked by script, and the batch was screened again with dedupe.py (no item shares a trick with an existing bank item). Each item states its tool.\n\n"
t=t.replace("\n## 3. Bank Index (for worksheet sourcing)","\n"+head+"\n".join(out)+"\n## 3. Bank Index (for worksheet sourcing)",1)
k=t.index("\n---\n\n## 4. Next Step")
t=t[:k].rstrip('\n')+"\n"+"\n".join(rows)+"\n"+t[k:]
t=t.replace("**Item count:** 994 items (",f"**Item count:** {994+len(I)} items (",1)
t=t.replace("(second sweep) §2.38;","(second sweep) §2.38 + 45 gap-closing §2.39 + 84 Trick Pack 2 web-research items §2.40;",1)
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
open('/home/claude/cb/bank_new4.md','w').write(t)
print("\n".join(Ls[-6:]))
print(collections.Counter(f['key'] for f in final if f['key']))
