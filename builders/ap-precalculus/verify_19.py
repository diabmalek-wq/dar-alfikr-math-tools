import numpy as np, sys, re, json, collections
sys.path.insert(0,"/home/claude/w8ap")
from ws_19 import M19,F19
ok=True
def chk(n,c):
    global ok
    if not c: ok=False; print("FAIL",n)
big=1e7; e=1e-7
def lim(f,a,side):  # sign of f near a from side; returns +inf/-inf/value
    v=f(a+side*e); w=f(a+side*e/10)
    if abs(w)>abs(v)*5 and abs(w)>1e5: return np.sign(w)*np.inf
    return round(float(w),4)
INF=np.inf
# Q1  (x+4)/(x^2-x-12): VA 4,-3 ; num zero -4
den=np.poly1d([1,-1,-12]); num=np.poly1d([1,4])
chk("1",sorted(den.roots)==[-3,4] and all(abs(num(r))>0 for r in den.roots))
# Q2 (x^2-9)/(x^2-x-6): hole at 3, VA -2
n=np.poly1d([1,0,-9]); d=np.poly1d([1,-1,-6]); f=lambda x:n(x)/d(x)
chk("2 roots",sorted(d.roots)==[-2,3] and n(3)==0 and n(-2)!=0)
chk("2 hole finite",abs(f(3+1e-6)-6/5)<1e-4 and lim(f,-2,1)==INF and lim(f,-2,-1)==-INF)
# Q3 graph function, same as in mkfigs_19.py
src=open("/home/claude/w8ap/mkfigs_19.py").read()
chk("3 fig fn","f=lambda x:-3/((x+1)*(x-2)**2)" in src and "axvline(-1" in src and "axvline(2" in src)
f=lambda x:-3/((x+1)*(x-2)**2)
chk("3",lim(f,-1,1)==-INF and lim(f,2,1)==-INF and lim(f,-1,-1)==INF and lim(f,2,-1)==-INF and abs(f(-1000))<1e-6)
# Q4
f=lambda x:(x+1)/(x-3); chk("4",lim(f,3,-1)==-INF and lim(f,3,1)==INF)
# Q5
f=lambda x:5/((x+2)**2*(x-1)); chk("5",lim(f,-2,-1)==-INF and lim(f,-2,1)==-INF)
# Q6
r=lambda x:(x-1)/((x+2)*(x-5)); chk("6",abs(r(1))<1e-12 and lim(r,-2,1)!=0 and abs(r(-2+1e-9))>1e6 and abs(r(5+1e-9))>1e6 and abs(r(1.5))>0 and abs(r(3))>0)
# Q7
C=lambda p:50*p/(100-p); chk("7",lim(C,100,-1)==INF and C(99)==4950 and C(0)==0)
# Q8
n=np.polymul(np.polymul([1,-2],[1,-2]),[1,1]); d=np.polymul(np.polymul(np.polymul([1,-2],[1,-2]),[1,-2]),[1,4])
f=lambda x:np.polyval(n,x)/np.polyval(d,x)
chk("8",abs(f(2+1e-6))>1e5 and abs(f(-4+1e-6))>1e5 and abs(f(-1))<1e-12 and abs(f(-1+1e-6))<1e-3)
# FRQ1
v=lambda u:10*u/(u-10); chk("F1a",lim(v,10,1)==INF); u=50/3; chk("F1c",abs(v(u)-25)<1e-9 and round(u,3)==16.667)
# FRQ2
r=lambda x:(x*x-2*x-3)/(x*x-2*x)
chk("F2a",list(np.round(sorted(np.roots([1,-2,-3])),9))==[-1,3] and list(np.round(sorted(np.roots([1,-2,0])),9))==[0,2])
chk("F2b",lim(r,2,-1)==INF and lim(r,2,1)==-INF)
q=lambda x:1/(x**2*(x-2)); chk("F2c",lim(q,0,-1)==-INF and lim(q,0,1)==-INF and lim(q,2,1)==INF and lim(q,2,-1)==-INF)
# structure
pos=[]
for i,(s,c,d,p,why) in enumerate(M19,1):
    o=list(d); o.insert(p,c); chk(f"distinct{i}",len(set(o))==4); chk(f"why{i}",all("{d%d}"%j in why for j in range(3))); pos.append("ABCD"[p])
cnt=collections.Counter(pos); chk("balanced",sorted(cnt.values())==[2,2,2,2]); print("answers",''.join(pos),dict(cnt)); chk("8mcq",len(M19)==8)
chk("2frq",len(F19)==2 and all(len(f["parts"])==3 for f in F19))
# deck checks
T=lambda v:36/(v-4)+36/(v+4)
chk("T single",all(abs(T(v)-72*v/(v*v-16))<1e-12 for v in (5,12,30)) and abs(T(12)-6.75)<1e-12 and abs(T(12)-864/128)<1e-12)
chk("T lim",T(4+1e-7)>1e6)
r=lambda x:(x-4)/((x+2)*(x-1)); chk("deck r",lim(r,-2,-1)==-INF and lim(r,-2,1)==INF and lim(r,1,-1)==INF and lim(r,1,1)==-INF and r(4)==0)
chk("fig deck","r=lambda x:(x-4)/((x+2)*(x-1))" in src)
h=lambda x:-1/(x+1)**3; chk("h",lim(h,-1,-1)==INF and lim(h,-1,1)==-INF)
g=lambda x:3/(x-2)**2; chk("g",lim(g,2,-1)==INF and lim(g,2,1)==INF)
rr=lambda x:(x+2)**2/((x+2)**3*(x-1)); chk("deck C",abs(rr(-2+1e-6))>1e5 and abs(rr(1+1e-6))>1e5 and abs(rr(0.5)-1/((2.5)*(-0.5)))<1e-9)
chk("practice",abs(((lambda x:(x-3)/(x*x-9))(3+1e-6))-1/6)<1e-6 and abs((lambda x:(x-3)/(x*x-9))(-3+1e-7))>1e6)
C2=lambda p:80*p/(100-p); chk("apply",C2(50)==80 and abs(C2(99)-7920)<1e-9 and lim(C2,100,-1)==INF)
chk("gate1",abs((lambda x:(x+5)/(x*x-25))(5+1e-7))>1e6 and abs((lambda x:(x+5)/(x*x-25))(-5+1e-6)+0.1)<1e-4)
chk("gate2",lim(lambda x:x/(x-2),2,1)==INF)
chk("gate3",abs((lambda x:(x-1)/((x-1)**2*(x+3)))(1+1e-6))>1e5 and abs((lambda x:(x-1)/((x-1)**2*(x+3)))(-3+1e-6))>1e5)
chk("exit",lim(lambda x:(x+1)/(x+3),-3,-1)==INF)
chk("smart",lim(lambda x:(x-1)/((x+2)*(x-5)),5,1)==INF)
# plain-text math scan of deck prose and worksheet
cfg=json.load(open("/home/claude/fikr_pptx/prezi/cfg/AP1-9.json"))
chk("no PLACEHOLDER",b"PLACEHOLDER" not in open("/home/claude/fikr_pptx/prezi/cfg/AP1-9.json","rb").read())
for s,c,d,p,why in M19:
    for t in [s,c]+d: chk("dollar balance "+t[:20],t.count("$")%2==0)
print("ALL OK" if ok else "FAILURES")
