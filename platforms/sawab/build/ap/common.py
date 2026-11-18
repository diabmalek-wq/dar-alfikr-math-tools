import random, math
from fractions import Fraction as Fr
import sympy as sp
L='ABCD'
def fx(v):
    """Fraction/int -> latex"""
    v=Fr(v)
    if v.denominator==1: return str(v.numerator)
    s='-' if v<0 else ''
    return '%s\\dfrac{%d}{%d}'%(s,abs(v.numerator),v.denominator)
def sx(e):
    """sympy expr -> latex"""
    return sp.latex(sp.nsimplify(e)).replace('\\frac','\\dfrac')
def term(c,p,v='x',first=False):
    c=Fr(c)
    if c==0: return ''
    sg='-' if c<0 else ('' if first else '+')
    a=abs(c)
    cs='' if (a==1 and p!=0) else fx(a)
    vs='' if p==0 else (v if p==1 else '%s^{%d}'%(v,p))
    return sg+cs+vs
def poly(terms,v='x'):
    out='';first=True
    for c,p in terms:
        t=term(c,p,v,first)
        if t: out+=t;first=False
    return out or '0'
def lin(a,b,v='x'):  # a v + b
    return poly([(a,1),(b,0)],v)
def fac(r,v='x'):   # (x - r)
    r=Fr(r)
    if r==0: return v
    return '(%s%s%s)'%(v,'-' if r>0 else '+',fx(abs(r)))
def num(v,d=3):
    s=('%.'+str(d)+'f')%v
    return s
def pick(r,a): return a[r.randrange(len(a))]

class Bad(Exception): pass
import re as _re
def clean(s):
    s=_re.sub(r'(\d?)\\left\((\d+)\\right\)\^',lambda m:(m.group(1)+'\\cdot ' if m.group(1) else '')+m.group(2)+'^',s)
    s=s.replace('^{\\dfrac','^{\\frac').replace('_{\\dfrac','_{\\frac')
    return s

def build(t,gid,tpl,seed,lvl='Medium',calc=None):
    """returns item dict; tpl(r)->dict(q,c,tr=[(v,why)*3],st=[steps], lvl?, calc?)"""
    for k in range(200):
        r=random.Random(seed*1000+k)
        try: d=tpl(r)
        except Bad: continue
        vals=[d['c']]+[v for v,_ in d['tr']]
        if len(set(vals))<4: continue
        order=list(range(4)); r.shuffle(order)
        o=[vals[i] for i in order]; a=order.index(0)
        traps={L[order.index(i+1)]:d['tr'][i][1] for i in range(3)}
        st=[clean(x) for x in d['st']]; o=[clean(x) for x in o]; traps={k:clean(v) for k,v in traps.items()}; d['q']=clean(d['q'])
        return {'id':gid,'t':t,'src':'ws','q':d['q'],'o':o,'a':a,'sol':' '.join(st),'steps':st,'traps':traps,'fig':None,
                'calc':d.get('calc',calc),'lvl':d.get('lvl',lvl)}
    raise RuntimeError('template failed '+gid)

REG={}
def reg(t,lvl='Medium',calc=None):
    def deco(f):
        REG.setdefault(t,[]).append((f,lvl,calc)); return f
    return deco
def make_all(topics=None):
    out=[]
    for t,tpls in REG.items():
        if topics and t not in topics: continue
        for k,(f,lvl,calc) in enumerate(tpls):
            base=hash((t,k))%997+17
            s1=int(t.replace('.',''))*37+k*101+3
            a=build(t,'%s-g%d'%(t,k+1),f,s1,lvl,calc)
            for j in range(1,50):
                b=build(t,'%s-g%d~t'%(t,k+1),f,s1+7919*j,lvl,calc)
                if b['q']!=a['q']: break
            qs={a['q'],b['q']}
            for j in range(50,120):
                c=build(t,'%s-g%dc'%(t,k+1),f,s1+7919*j,lvl,calc)
                if c['q'] not in qs: break
            out.append(a); out.append(b); out.append(c)
    return out
