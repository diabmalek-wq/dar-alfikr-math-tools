import numpy as np, re, sys, json
sys.argv=[sys.argv[0]]
ok=True
def chk(n,c):
    global ok
    if not c: ok=False; print("FAIL",n)
def isz(f,a,eps=1e-9):  # a is a zero in the domain: f finite and ~0
    try: return abs(f(a))<1e-9
    except ZeroDivisionError: return False
def defined(f,a):
    try: f(a); return True
    except ZeroDivisionError: return False
def sg(f,x): return np.sign(f(x))
# MCQ1
r=lambda x:(x-3)*(x+4)/((x+1)*(x-2)); chk("1",isz(r,3) and isz(r,-4) and not defined(r,-1) and not defined(r,2))
# MCQ2
f=lambda x:(x*x-9)/(x*x-x-6); chk("2",isz(f,-3) and not defined(f,3))
chk("2b",abs(f(3.0000001)-6/5)<1e-5)  # hole value 6/5, not 0 -> 3 is not a zero even as limit
# MCQ3 figure: s=(x+1)(x-3)/(x-1) with hole at -3
s=lambda x:(x+1)*(x-3)/(x-1)
chk("3 hole",abs(s(-3)+3)<1e-12); chk("3 zeros",isz(s,-1) and isz(s,3)); chk("3 va",not defined(s,1))
xs=np.concatenate([np.linspace(-20,0.999,5000),np.linspace(1.001,20,5000)])
mask=np.array([(abs(x+3)>1e-3) for x in xs])
neg=xs[(s(xs)<=1e-12)&mask]
# solution set (-inf,-3)U(-3,-1]U(1,3]
inA=lambda x:((x<-3)|((x>-3)&(x<=-1))|((x>1)&(x<=3)))
chk("3 set",all(inA(x) for x in neg) and all((s(x)<=1e-12) or not inA(x) or False for x in xs[mask]) and all(inA(x)==(s(x)<=1e-12) for x in xs[mask]))
# MCQ4
g=lambda x:(x**3-x)/(x*x+4); chk("4",all(isz(g,a) for a in(-1,0,1)) and np.all(np.array([x*x+4 for x in np.linspace(-9,9,99)])>0) and len(np.roots([1,0,-1,0]))==3)
# MCQ5
h=lambda x:1/(x-2)-3/(x+4); chk("5",isz(h,5) and not isz(h,-7) and not isz(h,-5) and np.allclose(np.polyadd([1,4],[-3,6]),[-2,10]))
# MCQ6 (x+2)/(x-3)<=0
q=lambda x:(x+2)/(x-3); xs=np.linspace(-20,20,40001); xs=xs[np.abs(xs-3)>1e-9]
chk("6",all((q(x)<=1e-12)==(-2<=x<3) for x in xs))
# MCQ7: count real zeros
cands={"A":lambda x:(x*x-4)/(x-2),"B":lambda x:(x*x-4)/(x*x+1),"C":lambda x:(x-2)*(x+1)/(x+3),"D":lambda x:(x*x+4)/(x-1)}
nz={"A":[a for a in(-2,2) if isz(cands["A"],a)],"B":[a for a in(-2,2) if isz(cands["B"],a)],"C":[a for a in(2,-1) if isz(cands["C"],a)],"D":[]}
chk("7",[len(v) for v in nz.values()]==[1,2,2,0] and np.all(np.roots([1,0,4]).imag!=0))
# MCQ8
f8=lambda x:(x-4)**2*(x+1)/((x-4)*(x+2)); chk("8",isz(f8,-1) and not defined(f8,4) and abs(f8(4+1e-7))<1e-5 and not isz(f8,-2))
# FRQ1
R=lambda t:2*(t-6)*(t+1)/(t+3); chk("F1a",isz(R,6) and R(0)==-4); ts=np.linspace(0,60,6001); chk("F1b",all((R(t)>=-1e-12)==(t>=6) for t in ts))
t=(7+97**.5)/2; chk("F1c",abs(R(t)-4)<1e-9 and round(t,3)==8.424 and (7-97**.5)/2<0)
# FRQ2
r2=lambda x:(x**3-4*x*x-5*x)/(x*x-2*x-15)
chk("F2a",np.allclose(sorted(np.roots([1,-4,-5,0])),[-1,0,5]) and np.allclose(sorted(np.roots([1,-2,-15])),[-3,5]) and isz(r2,0) and isz(r2,-1) and not defined(r2,5))
chk("F2b",abs(r2(5+1e-6)-15/4)<1e-4 and abs(r2(5-1e-6)-15/4)<1e-4)
xs=np.linspace(-20,20,40001); xs=xs[(np.abs(xs+3)>1e-9)&(np.abs(xs-5)>1e-9)]
sol=lambda x:((x>-3)&(x<=-1))|((x>=0)&(x<5))|(x>5)
chk("F2c",all((r2(x)>=-1e-12)==bool(sol(x)) for x in xs))
# distinct options + balance + figure/stem agreement
sys.path.insert(0,"/home/claude/w8ap")
src=open("/home/claude/w8ap/ws_18.py").read()
ns={}
exec(src.split("exec(_src)")[0].split("# ---- figure")[0],ns) if False else None
import ast
m=src[src.index("M18=["):src.index("F18=[")]
M=eval(m.replace("M18=",""))
pos=[x[3] for x in M]
for i,(st,c,d,p,why) in enumerate(M,1):
    o=list(d);o.insert(p,c); chk(f"distinct{i}",len(set(o))==4)
chk("balance",sorted(pos)==[0,0,1,1,2,2,3,3]); print("answers","".join("ABCD"[p] for p in pos))
# no plain-text math: every item string should have math in $...$ ; check there is no ^ or / outside $
def outside(s): return re.sub(r"\$[^$]*\$","",s)
bad=[x for it in M for x in [it[0],it[1]]+it[2] if re.search(r"[\^/]|\d\s*[+*=]",outside(x))]
chk("plaintext",not bad); print(bad)
print("ALL OK" if ok else "FAILURES")
