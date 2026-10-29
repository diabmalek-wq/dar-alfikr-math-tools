import math,re
from fractions import Fraction
import numpy as np
from scipy.optimize import brentq
d2r=math.radians
def sind(x): return math.sin(d2r(x))
def cosd(x): return math.cos(d2r(x))
def tand(x): return math.tan(d2r(x))
def dist(p,q): return math.hypot(p[0]-q[0],p[1]-q[1])
def foot(P,A,B):
    A=np.array(A,float);B=np.array(B,float);P=np.array(P,float)
    t=np.dot(P-A,B-A)/np.dot(B-A,B-A); return A+t*(B-A)
def ang(V,P,Q):
    """angle at V between rays to P and Q in degrees"""
    a=np.array(P,float)-np.array(V,float); b=np.array(Q,float)-np.array(V,float)
    return math.degrees(math.acos(np.dot(a,b)/np.linalg.norm(a)/np.linalg.norm(b)))
def area(A,B,C): return abs((B[0]-A[0])*(C[1]-A[1])-(C[0]-A[0])*(B[1]-A[1]))/2
def roots_in(f,lo,hi,n=200001):
    xs=np.linspace(lo,hi,n); ys=np.array([f(x) for x in xs]); r=[]
    for i in range(n-1):
        if ys[i]==0: r.append(xs[i])
        elif ys[i]*ys[i+1]<0: r.append(brentq(f,xs[i],xs[i+1],xtol=1e-13))
    return r
# ---- latex option -> float ----
def lx(s):
    t=s.strip().strip('$')
    t=t.replace('\\dfrac','\\frac').replace('\\left','').replace('\\right','').replace('{,}','').replace('\\,','').replace('\\%','')
    t=re.sub(r'\\sqrt(\d)',r'\\sqrt{\1}',t)
    t=re.sub(r'\\frac(\d)(\d)',r'\\frac{\1}{\2}',t)
    t=t.replace('\\pi','PI')
    def conv(s):
        while True:
            m=re.search(r'\\frac\{([^{}]*)\}\{([^{}]*)\}',s)
            if m: s=s[:m.start()]+'(('+m.group(1)+')/('+m.group(2)+'))'+s[m.end():]; continue
            m=re.search(r'\\sqrt\{([^{}]*)\}',s)
            if m: s=s[:m.start()]+'SQ('+m.group(1)+')'+s[m.end():]; continue
            return s
    t=conv(t)
    t=t.replace('{','(').replace('}',')')
    t=re.sub(r'(\d|\)|PI)\s*(SQ|PI|\()',r'\1*\2',t)
    return eval(t,{'__builtins__':{}},{'SQ':math.sqrt,'PI':math.pi})
# ---- float -> latex ----
def sqfree(n):
    k=1;m=n
    for p in range(2,int(math.isqrt(n))+1):
        while m%(p*p)==0: m//=p*p;k*=p
    return k,m
def tex(v,tol=1e-9):
    """exact latex for an integer, fraction, k*sqrt(n)/q, a+b sqrt(n), or multiple of pi"""
    if abs(v-round(v))<tol: return str(int(round(v)))
    for q in range(2,400):
        p=v*q
        if abs(p-round(p))<tol*q:
            p=int(round(p)); g=math.gcd(abs(p),q); p//=g; qq=q//g
            return ('-' if p<0 else '')+'\\dfrac{%d}{%d}'%(abs(p),qq)
    for q in range(1,60):
        for n in range(2,200):
            k,m=sqfree(n)
            if m==1: continue
            if n!=m: continue
            p=v*q/math.sqrt(n)
            if abs(p-round(p))<tol*q and round(p)!=0:
                p=int(round(p)); g=math.gcd(abs(p),q); p//=g; qq=q//g
                sgn='-' if p<0 else ''; p=abs(p)
                num=('' if p==1 else str(p))+'\\sqrt{%d}'%n
                return sgn+(num if qq==1 else '\\dfrac{%s}{%d}'%(num,qq))
    for n in range(2,200):
        k,m=sqfree(n)
        if m==1 or n!=m: continue
        for b in range(-30,31):
            if b==0: continue
            a=v-b*math.sqrt(n)
            if abs(a-round(a))<tol:
                a=int(round(a)); bs=('' if abs(b)==1 else str(abs(b)))+'\\sqrt{%d}'%n
                return ('%d'%a if a else '')+('-' if b<0 else ('+' if a else ''))+bs
    for q in range(1,100):
        p=v/math.pi*q
        if abs(p-round(p))<tol*q:
            p=int(round(p)); g=math.gcd(abs(p),q); p//=g; qq=q//g
            num=('' if abs(p)==1 else str(abs(p)))+'\\pi'
            return ('-' if p<0 else '')+(num if qq==1 else '\\dfrac{%s}{%d}'%(num,qq))
    raise ValueError(v)
def dec(v,d=1):
    s='%.*f'%(d,v); return s
