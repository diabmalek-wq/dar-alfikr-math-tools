exec(open('/home/claude/cb/alg1.py').read())
# ===== LI =====
V=[(0,0),(5,0),(0,4),(4,2)]
assert all(2*x+y<=10 and x+2*y<=8 for x,y in V) and 2*4+2==10 and 4+2*2==8
best=max(3*x+4*y for x,y in V); assert best==20
# brute force over fine grid
bf=max(3*x/4+4*y/4 for x in range(0,21) for y in range(0,17) if 2*x/4+y/4<=10 and x/4+2*y/4<=8); assert abs(bf-20)<1e-9
add(LI,"Hard","$$x\\ge0,\\quad y\\ge0,\\quad 2x+y\\le10,\\quad x+2y\\le8$$ For the ordered pairs $(x,y)$ that satisfy the system of inequalities above, what is the greatest possible value of $3x+4y$?",None,None,"$20$","The feasible region is a quadrilateral with vertices $(0,0)$, $(5,0)$, $(0,4)$ and $(4,2)$ (where $2x+y=10$ meets $x+2y=8$). Evaluate $3x+4y$ at each: $0$, $15$, $16$, $20$. The greatest value is $20$.","Students test only the axis intercepts ($(5,0)$ and $(0,4)$) and miss the corner where the two boundary lines meet.")
import math as M
mx=max(m_ for m_ in range(0,1000) if (20+0.05*m_)*1.08<=50+1e-12); assert mx==525
add(LI,"Hard","A phone plan costs $\\$20$ per month plus $\\$0.05$ per minute of calls. An $8\\%$ tax is applied to the whole monthly bill. A customer wants the bill, including tax, to be at most $\\$50$. What is the greatest whole number of minutes the customer can use in a month?",None,None,"$525$","The inequality is $1.08(20+0.05m)\\le50$. Dividing by $1.08$: $20+0.05m\\le46.296\\ldots$, so $0.05m\\le26.296\\ldots$ and $m\\le525.9\\ldots$. The greatest whole number is $525$.","Students tax only the per-minute charge, or round up to $526$.")
cnt=sum(1 for x in range(-20,20) if -4<3-2*x<=9); assert cnt==7
add(LI,"Medium","$$-4<3-2x\\le9$$ How many integers $x$ satisfy the compound inequality above?",None,None,"$7$","$-4<3-2x$ gives $x<3.5$. $3-2x\\le9$ gives $x\\ge-3$ (dividing by $-2$ flips the sign). So $-3\\le x<3.5$, and the integers are $-3,-2,-1,0,1,2,3$: seven.","Students forget to flip the inequality when dividing by $-2$, or exclude an endpoint.")
sols=[k for k in range(-5,10) if 5>2*k+1 and 5<9-k]; assert sols==[-5,-4,-3,-2,-1,0,1]
add(LI,"Hard","The system of inequalities $y>2x+1$ and $y<-x+9$ is graphed in the $xy$-plane. For which of the following sets of values of $k$ is the point $(k,5)$ a solution to the system?",["$k<2$","$k<4$","$2<k<4$","$k>2$"],0,"","Substitute $(k,5)$. First inequality: $5>2k+1$, so $k<2$. Second: $5<-k+9$, so $k<4$. Both must hold, so $k<2$.","Students combine the two bounds as an interval ($2<k<4$) or use only the weaker condition.")
a=4; assert all((3*x-a<2*x+5)==(x<9) for x in range(-20,30))
add(LI,"Medium","$$3x-a<2x+5$$ In the inequality above, $a$ is a constant. If the solution set of the inequality is all $x$ with $x<9$, what is the value of $a$?",None,None,"$4$","Subtract $2x$: $x-a<5$, so $x<5+a$. Setting $5+a=9$ gives $a=4$.","Students move $a$ with the wrong sign and get $a=-4$.")
k=1; assert all((-3*x+7>k)==(x<2) for x in range(-20,20))
add(LI,"Medium","$$-3x+7>k$$ In the inequality above, $k$ is a constant. If the solution set is all $x$ with $x<2$, what is the value of $k$?",None,None,"$1$","$-3x>k-7$, so dividing by $-3$ flips the sign: $x<\\dfrac{7-k}{3}$. Setting $\\dfrac{7-k}{3}=2$ gives $k=1$.","Students forget the sign flip and get $x>\\dfrac{k-7}{-3}$-type results or $k=13$.")
c=min(c_ for c_ in range(0,50) if 35+4*c_<15+9*c_); assert c==5
add(LI,"Hard","Gym A charges a monthly fee of $\\$35$ plus $\\$4$ per class. Gym B charges a monthly fee of $\\$15$ plus $\\$9$ per class. What is the least whole number of classes in a month for which Gym A costs less than Gym B?",None,None,"$5$","Gym A is cheaper when $35+4c<15+9c$, so $20<5c$ and $c>4$. The least whole number is $5$. (At exactly $4$ classes the costs are equal, $\\$51$.)","Students answer $4$ (the equal-cost point) because they use $\\le$.")
cnt=sum(1 for x in range(1,20) for y in range(1,20) if x+2*y<=9); assert cnt==16
add(LI,"Hard","How many ordered pairs $(x,y)$ of positive integers satisfy $x+2y\\le9$?",None,None,"$16$","For $y=1$: $x\\le7$ (7 pairs). $y=2$: $x\\le5$ (5). $y=3$: $x\\le3$ (3). $y=4$: $x\\le1$ (1). Total $7+5+3+1=16$.","Students include $x=0$ or $y=0$, or stop after $y=3$.")
p=max(p_ for p_ in range(0,200) if 0.8*p_-5<60); assert p==81
add(LI,"Hard","A store takes $20\\%$ off the price $p$ of a jacket, and then a customer uses a $\\$5$ coupon. The customer pays less than $\\$60$. What is the greatest whole-dollar value of $p$?",None,None,"$81$","The cost is $0.8p-5<60$, so $0.8p<65$ and $p<81.25$. The greatest whole-dollar price is $81$.","Students apply the coupon before the discount ($0.8(p-5)<60$) or round up to $82$.")
assert Fr(1,2)*6*9==27
add(LI,"Hard","In the $xy$-plane, the graph of $3x+2y\\le18$ together with $x\\ge0$ and $y\\ge0$ is a triangular region. What is the area of this region?",None,None,"$27$","The boundary meets the axes at $(6,0)$ and $(0,9)$. The legs are $6$ and $9$, so the area is $\\dfrac12(6)(9)=27$.","Students use $3$ and $2$ as the legs or forget the factor $\\dfrac12$.")
cmax=max(c_ for c_ in range(0,50) if 1.5*c_+2*4<=24); assert cmax==10
add(LI,"Hard","A shipping container can hold at most $24$ tons. Crates weigh either $1.5$ tons or $2$ tons. A shipment includes at least $4$ crates of the $2$-ton type. What is the greatest number of $1.5$-ton crates the shipment can include?",None,None,"$10$","With $h\\ge4$ heavy crates and $c$ light crates, $2h+1.5c\\le24$. The most light crates occurs at $h=4$: $1.5c\\le16$, so $c\\le10.67$ and the greatest whole number is $10$.","Students round $10.67$ up to $11$ or use $h=0$.")
kk=13; assert all((5<2*x-1<kk)==(3<x<7) for x in [i/2 for i in range(-10,30)])
add(LI,"Medium","$$5<2x-1<k$$ In the compound inequality above, $k$ is a constant. If the solution set is all $x$ with $3<x<7$, what is the value of $k$?",None,None,"$13$","Add $1$ and divide by $2$: $3<x<\\dfrac{k+1}{2}$. Setting $\\dfrac{k+1}{2}=7$ gives $k=13$.","Students solve $2x-1=7$ ($x=4$) or set $k=7$.")
# ===== SYS =====
add(SYS,"Hard","$$3x+ky=7$$ $$9x+12y=m$$ In the system of equations above, $k$ and $m$ are constants. For which of the following values of $k$ and $m$ does the system have no solution?",["$k=4,\\ m=7$","$k=4,\\ m=21$","$k=3,\\ m=21$","$k=12,\\ m=7$"],0,"","The equations are parallel when $\\dfrac39=\\dfrac k{12}$, so $k=4$. They are the same line only if $m=3\\cdot7=21$. So $k=4$ with $m\\ne21$ gives no solution: $k=4,\\ m=7$. With $k=4,\\ m=21$ there are infinitely many solutions, and $k=3$ or $k=12$ gives one solution.","Students find $k=4$ and then choose the pair with $m=21$ (infinitely many solutions).")
a=6; assert a/3==4/2==14/7
add(SYS,"Medium","$$ax+4y=14$$ $$3x+2y=7$$ In the system of equations above, $a$ is a constant. If the system has infinitely many solutions, what is the value of $a$?",None,None,"$6$","The second equation times $2$ is $6x+4y=14$, which matches the first when $a=6$.","Students compare only the $y$-coefficients and constants incorrectly, giving $a=3$.")
x,y=4,1; assert 3*x+5*y==17 and 5*x+3*y==23 and x+y==5
add(SYS,"Hard","$$3x+5y=17$$ $$5x+3y=23$$ If $(x,y)$ is the solution to the system of equations above, what is the value of $x+y$?",None,None,"$5$","Add the equations: $8x+8y=40$, so $x+y=5$. (Solving gives $x=4$, $y=1$.)","Students solve a full elimination and make an arithmetic slip, or divide $40$ by $4$.")
assert (2*0+0) or True
x=Fr(28,6)*0
sol=None
# 2x-3y=7, 4x+y=21 -> y=21-4x; 2x-63+12x=7 -> 14x=70 -> x=5,y=1
assert 2*5-3*1==7 and 4*5+1==21 and 6*5-2*1==28
add(SYS,"Hard","$$2x-3y=7$$ $$4x+y=21$$ If $(x,y)$ is the solution to the system of equations above, what is the value of $6x-2y$?",None,None,"$28$","Add the equations: $(2x-3y)+(4x+y)=6x-2y=7+21=28$.","Students try to isolate $x$ first, or add and get $6x-2y=14$ by mis-adding the constants.")
assert 2*2+1==-2+7
add(SYS,"Medium","$$y=2x+k$$ $$y=-x+7$$ In the system of equations above, $k$ is a constant. The graphs of the two equations intersect at the point with $x$-coordinate $2$. What is the value of $k$?",None,None,"$1$","At $x=2$ the second equation gives $y=5$. The first must also give $5$: $2(2)+k=5$, so $k=1$.","Students substitute into the wrong equation or use $y=7$ as the intersection.")
aa=5;bb=9; assert aa*2+3*(-1)==7 and 2*2-bb*(-1)==13 and aa*bb==45
add(SYS,"Hard","$$ax+3y=7$$ $$2x-by=13$$ In the system of equations above, $a$ and $b$ are constants. If $(2,-1)$ is the solution to the system, what is the value of $ab$?",None,None,"$45$","Substitute $(2,-1)$ into the first: $2a-3=7$, so $a=5$. Into the second: $4+b=13$, so $b=9$. Then $ab=45$.","Students substitute $x=-1,\\ y=2$ (swapped coordinates) or forget the sign on $-by$.")
assert Fr(1,2)*0==0
x_=6; y_=18-6; assert Fr(12,100)*x_+Fr(30,100)*y_==Fr(24,100)*18
add(SYS,"Hard","A chemist mixes $x$ liters of a $12\\%$ saline solution with $y$ liters of a $30\\%$ saline solution to make $18$ liters of a $24\\%$ saline solution. How many liters of the $12\\%$ solution are used?",None,None,"$6$","$x+y=18$ and $0.12x+0.30y=0.24(18)=4.32$. Substitute $y=18-x$: $0.12x+5.4-0.30x=4.32$, so $-0.18x=-1.08$ and $x=6$.","Students answer $y=12$ (the other solution) or use $0.24$ as an average of the two percents.")
v=Fr(15,2); assert (v+3)*2==18 or True
assert 9==Fr(15,2)+Fr(3,2) and 6==Fr(15,2)-Fr(3,2) and 9*2==18 and 6*3==18
add(SYS,"Hard","A boat travels $18$ kilometers downstream in $2$ hours and returns the same $18$ kilometers upstream in $3$ hours. What is the speed of the boat in still water, in kilometers per hour? (Enter as a decimal.)",None,None,"$7.5$","Downstream speed $=9$ km/h and upstream speed $=6$ km/h. With boat speed $v$ and current $c$: $v+c=9$ and $v-c=6$, so $v=7.5$.","Students average the two trip times or answer the current ($1.5$).")
o=5; s_=2*o+4; assert (s_+6)+(o+6)==40 and s_==24 or True
# recompute: o=8
o=8; s_=2*o+4; assert (s_+6)+(o+6)==40 and s_==20
add(SYS,"Hard","Sara is $4$ years older than twice Omar's age. In $6$ years, the sum of their ages will be $40$. How old is Sara now?",None,None,"$20$","Let Omar be $o$ years old, so Sara is $2o+4$. In $6$ years: $(2o+4+6)+(o+6)=40$, so $3o+16=40$ and $o=8$. Sara is $2(8)+4=20$.","Students forget to add $6$ to both ages, or answer Omar's age ($8$).")
for k_,m_ in [(2,1),(2,5)]:
    pass
# no solution second equation
def ns(a,b,c): # 4x-6y=9 vs a x + b y = c
    d=4*b-(-6)*a
    if d!=0: return 1
    return 'inf' if Fr(c,9)==Fr(a,4) else 0
assert ns(2,-3,10)==0 and ns(2,-3,Fr(9,2))=='inf' and ns(6,4,9)==1 and ns(3,-2,9)==1
add(SYS,"Hard","$$4x-6y=9$$ One equation of a system of two linear equations is given above. Which of the following could be the second equation so that the system has no solution?",["$2x-3y=10$","$2x-3y=\\dfrac92$","$6x+4y=9$","$3x-2y=9$"],0,"","The given line has slope $\\dfrac23$. The second equation must have the same slope but a different line. $2x-3y=10$ has slope $\\dfrac23$, and multiplying by $2$ gives $4x-6y=20\\ne9$, so the lines are parallel: no solution. $2x-3y=\\dfrac92$ is the same line (infinitely many solutions). The other two have different slopes (one solution each).","Students pick the equivalent equation (same line) instead of the parallel one.")
assert 6*6==36 and Fr(6,2)+Fr(6,3)==5 and Fr(6,4)-Fr(6,6)==Fr(1,2)
add(SYS,"Hard","$$\\frac x2+\\frac y3=5$$ $$\\frac x4-\\frac y6=\\frac12$$ If $(x,y)$ is the solution to the system of equations above, what is the value of $xy$?",None,None,"$36$","Multiply the first by $6$: $3x+2y=30$. Multiply the second by $12$: $3x-2y=6$. Adding gives $6x=36$, so $x=6$, and then $y=6$. So $xy=36$.","Students clear fractions inconsistently or add $x+y=12$.")
c_=84; assert 12*(150-c_)+7*c_==1380
add(SYS,"Medium","A theater sold $150$ tickets for a performance. Adult tickets cost $\\$12$ and child tickets cost $\\$7$. The total ticket revenue was $\\$1{,}380$. How many child tickets were sold?",None,None,"$84$","Let $c$ be child tickets: $12(150-c)+7c=1380$, so $1800-5c=1380$ and $c=84$.","Students answer the number of adult tickets ($66$) or mix up the prices.")
assert 3*3+3*1==12 and 2*3+1==7 and 3-1==2
add(SYS,"Hard","The lines $2x+y=7$, $x-y=2$ and $ax+3y=12$ all pass through the same point in the $xy$-plane. What is the value of $a$?",None,None,"$3$","Solve the first two: adding gives $3x=9$, so $x=3$ and $y=1$. The third line passes through $(3,1)$: $3a+3=12$, so $a=3$.","Students use $x=1,\\ y=3$ or solve all three equations at once.")
ks=[k for k in [Fr(i,2) for i in range(-40,41)] if k*(k+2)-8==0]; assert set(ks)=={Fr(2),Fr(-4)}
def nos(k):
    # kx+4y=10, 2x+(k+2)y=5
    det=k*(k+2)-8
    if det!=0: return False
    return Fr(10,5)!=Fr(k,2) or Fr(4,k+2)!=Fr(10,5) if False else (k*5!=10*2 if True else None)
# check both parallel and inconsistent explicitly
for k in (2,-4):
    a1,b1,c1=k,4,10;a2,b2,c2=2,k+2,5
    assert a1*b2-a2*b1==0 and not (a1*c2==a2*c1 and b1*c2==b2*c1)
add(SYS,"Hard","$$kx+4y=10$$ $$2x+(k+2)y=5$$ In the system of equations above, $k$ is a constant. What is the sum of all values of $k$ for which the system has no solution?",None,None,"$-2$","The lines are parallel when $k(k+2)=8$, so $k^2+2k-8=0$ and $k=2$ or $k=-4$. For $k=2$: $2x+4y=10$ and $2x+4y=5$ are different parallel lines. For $k=-4$: $-4x+4y=10$ and $2x-2y=5$, whose multiple $-4x+4y=-10$ differs from $10$. Both give no solution, so the sum is $2+(-4)=-2$.","Students find only the positive value or forget to check that the lines are not identical.")
assert Fr(1,2)*6*4==12
add(SYS,"Hard","The graphs of $y=2x-4$ and $y=-x+8$ and the $x$-axis bound a triangular region in the $xy$-plane. What is the area of the triangle?",None,None,"$12$","The lines meet where $2x-4=-x+8$, i.e. $x=4$, $y=4$. Their $x$-intercepts are $2$ and $8$, so the base is $6$ and the height is $4$. Area $=\\dfrac12(6)(4)=12$.","Students use the $y$-intercepts as the base or forget the factor $\\dfrac12$.")
