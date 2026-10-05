"""Auto-wrap over-wide LaTeX items into 2-3 line arrays (split at depth-0 colon or 'and'). usage: prep_cfg.py cfg.json  (needs m_<id> rendered)"""
import json,sys,re
from collect import key
cfg_path=sys.argv[1]; c=json.load(open(cfg_path)); idx=json.load(open(f"m_{c['id']}/_index.json"))
def width(t,col="222E2D"): m=idx.get(key(t,col)); return m["win"] if m else 0
def splits(t):
    out=[];d=0;i=0
    while i<len(t):
        ch=t[i]
        if ch=='{': d+=1
        elif ch=='}': d-=1
        elif d==0 and ch==':' : 
            j=i+1
            while t[j:j+2] in('\\ ','\\,') : j+=2
            out.append((i+1,j))
        elif d==0 and t.startswith('\\text{ and }',i): out.append((i,i+len('\\text{ and }')) ) ; 
        i+=1
    return out
def wrap(t,thr,depth=0):
    if width(t)<=thr or depth>=2: return None
    sp=splits(t)
    mid=len(t)/2
    ts=[]
    for m in re.finditer(r'\\text\{[^{}]*\}',t):
        for j in range(m.start()+6,m.end()-1):
            if t[j]==' ' and 3<j-m.start() : ts.append(j)
    cand=[(a,b,0) for a,b in sp]+[(j,j+1,1) for j in ts]
    if not cand: return None
    a,b,kind=min(cand,key=lambda s:abs(s[0]-mid))
    if kind: 
        l=[t[:a]+'}','\\text{'+t[b:]]
        return l
    l1=t[:a]; l2=t[b:]
    if t.startswith('\\text{ and }',a): l2='\\text{and }'+t[b:]
    if not l1.strip() or not l2.strip(): return None
    return [l1,l2]
n=0
def fix(t,thr):
    global n
    if '\\begin{array}' in t: return t
    r=wrap(t,thr)
    if not r: return t
    n+=1; return '\\begin{array}{c}'+r[0]+'\\\\ '+r[1]+'\\end{array}'
def lst(a,thr):
    for i,t in enumerate(a): a[i]=fix(t,thr)
lst(c['diagnose']['items'],3.0); lst(c['gate']['items'],3.0); lst(c['smart']['exit'],3.3)
for k in('practice','apply','investigate'): lst(c['practice'][k]['items'],3.3)
for k in('sat','gat','saat'): lst(c['exam'][k]['q'],2.5)
for b in c['blocks']:
    for e in b['examples']:
        w=2.2 if not b['fig'] and len(b['examples'])==3 else 2.5
        e['q']=fix(e['q'],w)
json.dump(c,open(cfg_path,'w'),indent=1,ensure_ascii=False); print(c['id'],'wrapped',n)
