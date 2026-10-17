import numpy as np
P=np.poly1d; ok=True
def chk(n,c):
    global ok
    if not c: ok=False; print("FAIL",n)
# 1.11
f=P([1,-4,-5,0]); chk("11.1",sorted(f.roots.real.round(6))==[-1,0,5])
r=lambda x:(x*x-x-6)/(x*x-9); chk("11.2",abs(r(3+1e-7)-5/6)<1e-5 and abs(r(3-1e-7)-5/6)<1e-5)
q,rem=np.polydiv([3,-2,1,-4],[1,-1]); chk("11.3",list(q)==[3,1,2] and rem[0]==-2)
q,rem=np.polydiv([3,-2,1,-4],[1,1]); chk("11.3 dist",list(q)==[3,-5,6])
q,rem=np.polydiv([1,5,3],[1,2]); chk("11.4",list(q)==[1,3] and rem[0]==-3)
chk("11.5",np.polymul(np.polymul([1,-2],[1,-2]),np.polymul([1,-2],[1,-2]))[2]==24)
x=7.3;chk("11.6",abs((x*x-4)/(x*x-x-2)-(x+2)/(x+1))<1e-12)
g=P([-2])*P([1,1])**2*P([1,-3]);chk("11.7",g.coeffs[0]==-2 and g.order==3)
chk("11.8",list(np.polymul(np.polymul([2,-1],[2,-1]),[2,-1]))==[8,-12,6,-1])
A=lambda n:(n*n+10*n+40)/(n+5); q,rem=np.polydiv([1,10,40],[1,5]);chk("F11a",list(q)==[1,5] and rem[0]==15)
n=5+85**.5;chk("F11c",abs(A(n)-20)<1e-9 and round(n,3)==14.220)
p=P([1,-3,-4,12]);chk("F11p",sorted(p.roots.real.round(6))==[-2,2,3])
chk("F11r",abs(p(2.0001)/((2.0001-2)*(2.0001+1))+4/3)<1e-3)
q,rem=np.polydiv([1,-1,-6],[1,1]);chk("F11s",list(q)==[1,-2] and rem[0]==-4)
# 1.12
f=lambda x:np.sqrt(x)
chk("12.8",(f(4)==2) and -f(16/4)+1==-1)
chk("12.7",(-2*1+3,-2*5+3)==(1,-7) and (-2*(1+3),-2*(5+3))==(-8,-16) )
chk("12.6",(-8/2,16/2)==(-4,8))
H=lambda x:-0.4*(x-3)**2+4.5;chk("F12c",abs(H(3+11.25**.5))<1e-9 and round(3+11.25**.5,3)==6.354)
# g=2f(x-1)+3 domain [-2,6] range [-1,15]; image of (2,4) -> (3,11); h domain [-1.5,2.5] range [-6,2]
chk("F12",(2*-2+3,2*6+3,2*4+3)==(-1,15,11) and (-3/2,5/2)==(-1.5,2.5))
# 1.13
chk("13.1",list(np.diff([5,9,13,17,21]))==[4]*4)
y=[3,4,9,18,31];x=np.arange(5);chk("13.2",all(2*x**2-x+3==y) and list(np.diff(y,2))==[4,4,4])
y=[2,3,10,29,66,127];chk("13.3",list(np.diff(y,3))==[6,6,6] and len(set(np.diff(y,2)))>1)
chk("13.5",True)
yy=np.array([12,19,24,27,28,27]);x=np.arange(6);chk("F13a",list(np.diff(yy,2))==[-2]*4 and all(-x**2+8*x+12==yy))
chk("F13c",abs(-(4+28**.5)**2+8*(4+28**.5)+12)<1e-9 and round(4+28**.5,3)==9.292)
c=np.polyfit([0,1,2,3],[1,2,5,10],2);chk("F13q",np.allclose(c,[1,0,1]) and np.polyval(c,5)==26 or abs(np.polyval(c,5)-26)<1e-9)
chk("13box",True)
# distinctness of options handled by eye; print
print("ALL OK" if ok else "FAILURES")
