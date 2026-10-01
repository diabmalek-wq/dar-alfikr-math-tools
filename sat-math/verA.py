from fractions import Fraction as F
import itertools
ok=True
def chk(name,cond):
    global ok
    print(('PASS' if cond else 'FAIL'),name); ok&=cond
# brute solver for linear eq f(x)=0 via two evaluations
def solve(f):
    a=f(F(0)); b=f(F(1)); m=b-a
    return None if m==0 else -a/m
chk('1', solve(lambda x:4*x+3-27)==6 and 8*6+6==54)
chk('2', solve(lambda x:-2*(3*x-5)-(4*x-10))==2)
chk('3', solve(lambda x:(2*x+1)/3-(x-4)/2)==-14)
c=F(7); Fv=F(9,5)*c+32; chk('4',F(5,9)*(Fv-32)==c and (F(5,9)*Fv-32)!=c)
chk('5', solve(lambda n:2*n-3-(n+5))==8)
xs=[x for x in range(-30,30) if -3*x+7<=22]; chk('6',min(xs)==-5)
chk('7', all(F(1,2)*(6*x+14)-(3*x+7)==0 for x in [F(0),F(3),F(-5)]))
# 8: (a-2)x+3=5x+7 no solution at a=7, others one
chk('8a', (7-2)==5 and 3!=7); chk('8b', all(solve(lambda x,a=a:(a-2)*x+3-5*x-7) is not None for a in [2,3,5]))
chk('9', all(3*(2*x+7)-(6*x+21)==0 for x in range(-3,4)))
t=F(96,8); chk('10', 5*t-3*t==24)
A,h,b2=F(50),F(4),F(3); b1=2*A/h-b2; chk('11', A==h*(b1+b2)/2)
chk('12', 150+45*12==690)
import math; chk('13', max(t for t in range(0,40) if 60-4.5*t>=5)==12)
chk('14', len([x for x in range(-20,20) if -7<3-2*x<=9])==8)
chk('15', solve(lambda x:F(4,10)*(x+10)-(F(25,100)*x+F(76,10)))==24)
w=solve(lambda w:2*(w+2*w-3)-54); chk('16', w==10 and w*(2*w-3)==170)
# 17
import fractions
cnt=0
for a in [F(n,2) for n in range(-12,13)]:
    c=a*a-9; n=a+3
    if c==0: cnt+=1
chk('17', cnt==2)
chk('18', all(((a+b)/(a-b)==3) for a,b in [(F(2),F(1)),(F(-6),F(-3))]) and F(2)==2)
chk('19', sum(range(9,17,2))==48 and 2*15+18==48 and 11*13==143)
x=solve(lambda x:(2*x-1)/3-(x+2)/4-(x/6-F(1,2))); chk('20', x==F(4,3))
# 21 sets
import numpy as np
def sol(opt,x):
    A=lambda x:3*x+1
    return opt(x)
xs=[F(n,2) for n in range(-12,12)]
opts={'A':lambda x:(3*x+1>=-5) or (x-4<-3),'B':lambda x:(3*x+1<=-5) and (x-4>-3),'C':lambda x:(3*x+1<-5) or (x-4>=-3),'D':lambda x:(3*x+1<=-5) or (x-4>-3)}
target=lambda x: x<=-2 or x>1
chk('21', [k for k,f in opts.items() if all(f(x)==target(x) for x in xs)]==['D'])
chk('22', [k for k in range(-20,20) if 12-k==2*k]==[4])
tot=0
for k in range(-200,201):
    if k==1: continue
    x=F(k-3,k-1)
    assert (k+1)*x+3==2*x+k
    if x.denominator==1: tot+=k
chk('23', tot==4)
per=0
for x in [F(2),F(9,2),F(7)]:
    s=sorted([x+2,3*x-2,5*x-16])
    if s[0]<=0: continue
    if not(s[0]+s[1]>s[2]): continue
    if len(set(s))==2: per+=sum(s)
chk('24', per==F(143,2))
print('ALL OK' if ok else 'PROBLEM')
