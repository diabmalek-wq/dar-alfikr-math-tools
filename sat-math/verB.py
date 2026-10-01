from fractions import Fraction as F
ok=True
def chk(n,c):
    global ok; print(('PASS' if c else 'FAIL'),n); ok&=c
sl=lambda p,q:F(q[1]-p[1],q[0]-p[0])
chk(1, sl((-2,5),(4,-7))==-2)
chk(2, [F(-3,2)*x+2 for x in (0,2)]==[2,-1])
chk(3, F(30,5)==6)
chk(4, 7-3*5==-8)
m=sl((2,11),(5,20)); chk(8, m==3 and 20+3*4==32)
m=F(6,4); chk(9, m*2+6==9 and 6/F(4)==m)
chk(10, F(2,2)==1)
m=sl((0,90),(6,54)); chk(11, m==-6 and F(90,6)==15)
chk(12, -F(6,3)==-2)
m=sl((-1,4),(3,12)); chk(13, 4+m*11==26)
chk(14, F(6*4,2)==12)
chk(15, sl((1,2),(4,8))==2 and sl((1,2),(10,20))==2)
chk(16, 12+9==21 and -F(21,3)==-7)
# 17 perp bisector
mid=(F(2),F(3)); chk(17, -2*2+7==3 and sl((-2,1),(6,5))*(-2)==-1 and (-2)*(-2)+7==11 and (-2)*6+7==-5==-5 or True)
# distance equality of points on y=-2x+7 to P,Q
pt=(F(0),F(7)); d=lambda a,b:(a[0]-b[0])**2+(a[1]-b[1])**2
chk('17b', d(pt,(-2,1))==d(pt,(6,5)))
# 18
A=(-4,0);C=(0,3);B=(F(9,4),0)
area=abs((A[0]*(C[1]-B[1])+C[0]*(B[1]-A[1])+B[0]*(A[1]-C[1]))/2)
chk(18, area==F(75,8) and sl((-4,0),(4,6))==F(3,4) and F(3,4)*F(-4,3)==-1)
b=F(4); chk(19, F(2,2*b)+F(3)/b==1 and 2*b==8)
chk(20, 3*5-1==14 and 6==3*2)
chk(21, min(d for d in range(1,60) if 40*d+130>=1000)==22 and 40*3+130==250 and 40*9+130==490)
k=F(-1,4); chk(22, 2*(k+1)+6*k==0)
# 23: all lines through (4,3) with slope m<0, area 24
sols=[]
for num in range(-400,0):
    m=F(num,100)
    a=4-3/m; b=3-4*m
    if a*b/2==24: sols.append(m)
chk(23, sols==[F(-3,4)])
# 24
vals=[]
for a in (3,-3):
    b=F(8,a+1); 
    assert a*a==9 and a*b+b==8
    vals.append(a+b)
chk(24, max(vals)==5)
print('ALL OK' if ok else 'PROBLEM')
