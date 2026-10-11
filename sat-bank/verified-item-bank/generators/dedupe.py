import re,sys
sys.path.insert(0,'/home/claude/cb')
def load(path='/home/claude/sat_bank_all.md'):
    t=open(path).read()
    parts=re.split(r'^### (?=[A-Z]{1,3}-\d+\s*$)',t,flags=re.M)[1:]
    out=[]
    for p in parts:
        i=p.split('\n',1)[0].strip()
        m=re.search(r'\*\*Question:\*\* (.*?)\n\n(?:\(A\)|\*\*Correct)',p,re.S)
        if m: out.append((i,m.group(1)))
    return out
def tok(s): return set(re.findall(r'[a-z]{3,}',re.sub(r'\$[^$]*\$',' ',s.lower())))
def nums(s): return set(re.findall(r'\d+(?:\.\d+)?',s))
def sim(q1,q2):
    a,b=tok(q1),tok(q2);x,y=nums(q1),nums(q2)
    return len(a&b)/max(1,len(a|b))*0.6+len(x&y)/max(1,len(x|y))*0.4
def check(items,thr=0.4,path='/home/claude/sat_bank_all.md'):
    bank=load(path);res=[]
    for n,it in enumerate(items,1):
        s,i=max((sim(it['q'],q),i) for i,q in bank)
        res.append((n,s,i))
    return res,bank
if __name__=='__main__':
    exec(open(sys.argv[1]).read())
    res,bank=check(I);d=dict(bank)
    for n,s,i in res:
        if s>0.4: print(n,round(s,2),i,'|',I[n-1]['q'][:70],'|',d[i][:70])
    print(len(bank))
