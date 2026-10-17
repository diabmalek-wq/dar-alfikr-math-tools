import numpy as np, sys, json
sys.path.insert(0,"/home/claude/w8ap")
import ws_110 as W
ok=True
def chk(n,c):
    global ok
    if not c: ok=False; print("FAIL",n)
P=np.poly1d
def lim(f,c,h=1e-6): a,b=f(c-h),f(c+h); chk("two-sided "+str(f.__code__.co_firstlineno)+" "+str((a,b)),abs(a-b)<1e-3); return (a+b)/2
def prod(*roots,k=1): return k*np.poly(roots) if roots else np.array([k])
# M1
f=lambda x:(x*x+2*x-8)/(x*x-3*x+2); chk("M1",abs(lim(f,2)-6)<1e-4); chk("M1 fac",np.allclose(np.polymul([1,4],[1,-2]),[1,2,-8]) and np.allclose(np.polymul([1,-1],[1,-2]),[1,-3,2]))
# M2: numerator mult 1, den mult 2 at 3; outputs blow up
f=lambda x:(x*x-9)/(x*x-6*x+9); chk("M2",abs(f(3+1e-4))>1e3 and abs(f(3-1e-4))>1e3 and np.allclose(np.polymul([1,-3],[1,-3]),[1,-6,9]))
# M3
f=lambda x:(x*x+2*x-3)/(x+3); chk("M3",abs(lim(f,-3)+4)<1e-4)
# M4 table
f=lambda x:(x*x+x-6)/(x-2); xs=[1.9,1.99,1.999,2.001,2.01,2.1]; chk("M4",np.allclose([f(x) for x in xs],[4.9,4.99,4.999,5.001,5.01,5.1],atol=1e-6))
# M5: correct option structure
chk("M5",np.allclose(np.polymul([1,-1],[1,3]),[1,2,-3]) )
# M6
f=lambda x:(x-2)**3*(x+1)/((x-2)**2*(x-5)); chk("M6",abs(lim(f,2,1e-4))<1e-3 and abs((2-2)*(2+1)/(2-5))<1e-12)
chk("M6 d0",(2+1)==3)
# M7: roots
num=[-1,2,4];den=[2,4,-5];holes=set(num)&set(den);chk("M7",len(holes)==2 and len(set(den)-set(num))==1)
# M8
f=lambda x:(2*x*x-8)/(x*x-x-2); chk("M8",abs(lim(f,2)-8/3)<1e-4)
# FRQ9
v=lambda t:((t*t+3*t)-(1+3))/(t-1); chk("F9a",np.allclose(np.polymul([1,4],[1,-1]),[1,3,-4]))
chk("F9b",abs(lim(v,1)-5)<1e-4); chk("F9c",abs(v(3.5)-7.5)<1e-9 and all(abs(v(t)-5)>1e-3 for t in np.linspace(0.1,5,500) if abs(t-1)>1e-3))
# FRQ10
r=lambda x:(x-3)**2*(x+1)*(x-2)/((x-3)*(x-2)**2*(x+4))
chk("F10a",abs(lim(r,3,1e-5))<1e-3 and abs(r(2+1e-5))>1e3 and abs(r(-4+1e-5))>1e3)
chk("F10c",abs(r(-1))<1e-12 and all(abs(r(x))>1e-4 for x in (3+1e-3,3-1e-3)) )
# distinct options & balance & letters
import re
pos=[]
for i,(s,c,d,p,why) in enumerate(W.M10,1):
    o=list(d);o.insert(p,c); chk(f"distinct {i}",len(set(o))==4); chk(f"why refs {i}","{d0}" in why and "{d1}" in why and "{d2}" in why); pos.append(p)
chk("balance",sorted(pos)==[0,0,1,1,2,2,3,3]); chk("8 MCQ 2 FRQ",len(W.M10)==8 and len(W.F10)==2)
# figure numbers: r(x)=(x+2)/(x-3) hole (1,-3/2), VA 3, HA 1, zero -2
g=lambda x:(x*x+x-2)/(x*x-4*x+3); chk("fig hole",abs(lim(g,1)+1.5)<1e-4); chk("fig xyz",abs(g(-2))<1e-12 and abs(g(1e6)-1)<1e-4 and abs(g(3+1e-5))>1e3)
# deck checks
c=json.load(open("/home/claude/fikr_pptx/prezi/cfg/AP1-10.json"))
chk("deck B1A",abs(lim(lambda x:(x*x-4)/(x*x-2*x),2)-2)<1e-4)
chk("deck B1B",abs(lim(lambda x:(x*x-2*x-3)/(x*x-x-6),3)-0.8)<1e-4)
chk("deck B2A",abs(lim(lambda x:(x-1)**2*(x+2)/((x-1)*(x+3)),1,1e-4))<1e-3)
chk("deck B3B",abs((2.99**2-9)/(2.99-3)-5.99)<1e-9 and abs((3.01**2-9)/(3.01-3)-6.01)<1e-9)
chk("practice",abs(lim(lambda x:(x*x-x-12)/(x*x-16),4)-7/8)<1e-4)
chk("apply",abs(lim(lambda x:(x*x-25)/(x-5),5)-10)<1e-4)
chk("investigate",abs(lim(lambda x:15*(x-2)/((x-2)*(x+1)),2)-5)<1e-4)
A=lambda t:(t*t+2*t-8)/(t-2); chk("prod",abs(lim(A,2)-6)<1e-4 and np.allclose([A(1.9),A(1.99),A(2.01),A(2.1)],[5.9,5.99,6.01,6.1]) and (2**2+2*2)==8)
chk("gate1",abs(lim(lambda x:(x*x-1)/(x*x+3*x+2),-1)+2)<1e-4); chk("gate2",abs(((x:=2+1e-4)-2)**2/((x-2)**3*(x+1)))>1e3)
chk("gate3",abs(lim(lambda x:(x*x-16)/(x-4),4)-8)<1e-4)
chk("smart",abs(lim(lambda x:(x*x+x-2)/(x+2),-2)+3)<1e-4)
chk("diag3",abs((1+2)/(1-3)+1.5)<1e-12)
print("ALL OK" if ok else "FAILURES")
