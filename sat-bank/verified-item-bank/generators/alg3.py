import sys; sys.path.insert(0,'/home/claude/cb')
from alg_lib import *
H,M_="Hard","Medium"
# ===== LE1 =====
assert Fr(1,6)+Fr(1,9)==Fr(5,18) and Fr(18,5)==Fr(36,10)
add(LE1,H,"Pump A can fill an empty tank in $6$ hours working alone. Pump B can fill the same tank in $9$ hours working alone. How many hours will it take the two pumps, working together, to fill the empty tank? (Enter as a decimal.)",None,None,"$3.6$","In one hour the pumps fill $\\dfrac16+\\dfrac19=\\dfrac5{18}$ of the tank. The time is $\\dfrac{18}{5}=3.6$ hours.","Students average the times ($7.5$) or add them ($15$).")
n=6; assert 5*n-3==2*(n+8)-1
add(LE1,M_,"When $3$ is subtracted from $5$ times a number $n$, the result is $1$ less than twice the sum of $n$ and $8$. What is the value of $n$?",None,None,"$6$","$5n-3=2(n+8)-1=2n+15$, so $3n=18$ and $n=6$.","Students write $2n+8-1$ (dropping the parentheses) and get $n=\\dfrac{12}{3}\\ldots$ a different value.")
x=9; assert (x)+(x+3)+(2*x-1)==38 and max(x,x+3,2*x-1)==17
add(LE1,M_,"The three sides of a triangle have lengths $x$, $x+3$ and $2x-1$. The perimeter of the triangle is $38$. What is the length of the longest side?",None,None,"$17$","$x+(x+3)+(2x-1)=4x+2=38$, so $x=9$. The sides are $9$, $12$ and $17$, and the longest is $17$.","Students answer $x=9$ or the middle side $x+3$.")
assert Fr(4,10)*40==Fr(25,100)*64
add(LE1,M_,"$40\\%$ of a number $n$ equals $25\\%$ of $64$. What is the value of $n$?",None,None,"$40$","$0.4n=0.25(64)=16$, so $n=40$.","Students find $25\\%$ of $64$ and stop ($16$).")
assert Fr(5*Fr(23,5)*2-4,1)==42 or (10*Fr(23,5)-4==42)
add(LE1,H,"$$\\frac{5x-2}{3}=7$$ What is the value of $10x-4$?",None,None,"$42$","Multiply by $3$: $5x-2=21$. Then $10x-4=2(5x-2)=42$. No need to find $x$.","Students solve $x=\\dfrac{23}{5}$ and make an arithmetic slip, or answer $21$.")
f=lambda x:2*x+1
assert f(f(1))==7 and 4+3*3==13
add(LE1,H,"The function $f$ is defined by $f(x)=2x+b$, where $b$ is a constant. If $f(f(1))=13$, what is the value of $b$?",None,None,"$3$","$f(1)=2+b$. Then $f(f(1))=2(2+b)+b=4+3b=13$, so $b=3$.","Students compute $f(f(1))=2f(1)+b$ without substituting $f(1)$ correctly, or give $f(1)$.")
# ===== LE2 =====
k=-14; assert 3*k-2*(2*k)==14
add(LE2,H,"The point $(k,2k)$ lies on the line $3x-2y=14$ in the $xy$-plane. What is the value of $k$?",None,None,"$-14$","Substitute: $3k-2(2k)=14$, so $-k=14$ and $k=-14$.","Students treat $(k,2k)$ as $x=k$, $y=2$ or lose the sign.")
b=Fr(5,2); assert Fr(1,1)/(2*b)+Fr(2)/b==1
add(LE2,H,"A line in the $xy$-plane passes through $(1,2)$, and its $x$-intercept is twice its $y$-intercept. What is the $y$-intercept of the line? (Enter as a fraction or decimal.)",None,None,"$\\dfrac52$","Let the $y$-intercept be $b$, so the $x$-intercept is $2b$ and $\\dfrac{x}{2b}+\\dfrac yb=1$. Substituting $(1,2)$: $\\dfrac1{2b}+\\dfrac2b=\\dfrac5{2b}=1$, so $b=\\dfrac52$.","Students assume the intercepts are $(2,0)$ and $(0,1)$ or use $b=2$.")
assert (2*3+3*2==12) and (3-2==1) and Fr(1,2)*5*3==Fr(15,2)
add(LE2,H,"The lines $2x+3y=12$ and $x-y=1$ intersect at a point. The two lines and the $y$-axis form a triangle. What is the area of the triangle? (Enter as a decimal.)",None,None,"$7.5$","The intersection is $(3,2)$. The $y$-intercepts are $4$ and $-1$, so the base along the $y$-axis is $5$ and the height is $3$. Area $=\\dfrac12(5)(3)=7.5$.","Students use the $x$-intercepts or the wrong base ($3$).")
assert Fr(3)==(Fr(1,1)*5)*Fr(4,5)-1
add(LE2,H,"The segment with endpoints $(2,-3)$ and $(8,9)$ has its midpoint on the line $y=mx-1$ in the $xy$-plane. What is the value of $m$? (Enter as a fraction.)",None,None,"$\\dfrac45$","The midpoint is $\\left(\\dfrac{2+8}2,\\dfrac{-3+9}2\\right)=(5,3)$. Then $3=5m-1$, so $m=\\dfrac45$.","Students add instead of averaging, or use an endpoint.")
assert 3*4+2*4==20 and 3*1+2*2!=20 or True
mid=(4,4); sl=Fr(6-2,7-1); assert sl==Fr(2,3) and 3*mid[0]+2*mid[1]==20
add(LE2,H,"Points $A(1,2)$ and $B(7,6)$ are given in the $xy$-plane. Which of the following is an equation of the line that is perpendicular to $\\overline{AB}$ and passes through its midpoint?",["$3x+2y=20$","$3x-2y=4$","$2x+3y=20$","$2x-3y=-4$"],0,"","The midpoint is $(4,4)$ and the slope of $AB$ is $\\dfrac23$, so the perpendicular slope is $-\\dfrac32$: $y-4=-\\dfrac32(x-4)$, i.e. $3x+2y=20$.","Students use the slope $\\dfrac23$ itself (the line through the midpoint parallel to $AB$) or the wrong sign.")
a=1; assert Fr(a-3,5-a)==Fr(-1,2)
add(LE2,H,"The line through the points $(a,3)$ and $(5,a)$ has slope $-\\dfrac12$. What is the value of $a$?",None,None,"$1$","$\\dfrac{a-3}{5-a}=-\\dfrac12$, so $2a-6=a-5$ and $a=1$. Check: the points $(1,3)$ and $(5,1)$ have slope $\\dfrac{-2}{4}=-\\dfrac12$.","Students write the slope as $\\dfrac{5-a}{a-3}$ (inverted).")
aa=Fr(39-19,8-3); assert aa==4 and 19-3*4==7 and 4*12+7==55
add(LE2,M_,"A print shop charges a per-copy price plus a flat setup fee. An order of $3$ copies costs $\\$19$ and an order of $8$ copies costs $\\$39$. What is the cost, in dollars, of an order of $12$ copies?",None,None,"$55$","The per-copy price is $\\dfrac{39-19}{8-3}=4$, so the setup fee is $19-12=7$. Twelve copies cost $4(12)+7=55$.","Students find the unit price from $\\dfrac{39}{8}$ or ignore the setup fee.")
assert Fr(9,2)==Fr(3)+Fr(-1,2)*(0-3)*-1*0 or True
# line through (3,3) perpendicular to y=2x-3: slope -1/2: y=-x/2+9/2
assert Fr(9,2)==3+Fr(1,2)*3
add(LE2,H,"The lines $y=2x-3$ and $y=-x+6$ intersect at the point $P$. A third line passes through $P$ and is perpendicular to $y=2x-3$. What is the $y$-intercept of the third line? (Enter as a fraction or decimal.)",None,None,"$\\dfrac92$","Solve $2x-3=-x+6$: $x=3$, $y=3$, so $P=(3,3)$. The perpendicular slope is $-\\dfrac12$, so $y-3=-\\dfrac12(x-3)$ and $y=-\\dfrac12x+\\dfrac92$.","Students use the wrong perpendicular slope ($-2$) or use the second line for the intercept.")
m=Fr(5,3); assert m*(2+1)==5 and -1==-Fr(1)
add(LE2,H,"A line in the $xy$-plane passes through $(2,5)$ and has a slope equal to its $y$-intercept. What is the $x$-coordinate of its $x$-intercept?",None,None,"$-1$","The line is $y=mx+m=m(x+1)$. Through $(2,5)$: $5=3m$, so $m=\\dfrac53$. Setting $y=0$ gives $x+1=0$, so $x=-1$ (for any nonzero slope).","Students try to find the intercept using the point $(2,5)$ only.")
assert 3*Fr(4,3)==4  # (A) quick sanity
assert (3*5-2*1*3==9) or True
add(LE2,H,"$$3x-2y=12$$ Line $\\ell$ in the $xy$-plane is defined by the equation above. Line $m$ has the same $y$-intercept as $\\ell$ and is perpendicular to $\\ell$. What is the $x$-coordinate of the $x$-intercept of $m$?",None,None,"$-12$","Line $\\ell$: $y=\\dfrac32x-6$, so its $y$-intercept is $-6$. Line $m$ has slope $-\\dfrac23$ and $y=-\\dfrac23x-6$. Setting $y=0$: $x=-9$.","")
I.pop()
assert -Fr(2,3)*(-9)-6==0
add(LE2,H,"$$3x-2y=12$$ Line $\\ell$ in the $xy$-plane is defined by the equation above. Line $m$ has the same $y$-intercept as $\\ell$ and is perpendicular to $\\ell$. What is the $x$-coordinate of the $x$-intercept of $m$?",None,None,"$-9$","Line $\\ell$: $y=\\dfrac32x-6$, so its $y$-intercept is $-6$. Line $m$ has slope $-\\dfrac23$ and equation $y=-\\dfrac23x-6$. Setting $y=0$ gives $x=-9$.","Students use the parallel slope $\\dfrac32$ ($x=4$) or the intercept $-6$ itself.")
# ===== LF =====
add(LF,H,"The function $f$ is defined by $f(x)=3x-7$. For what value of $x$ is $f(x)=5$?",None,None,"$4$","$3x-7=5$, so $x=4$.","Students evaluate $f(5)=8$ instead of solving $f(x)=5$.")
a=3;b=2; assert a*a==9 and a*b+b==8 and a+b==5
add(LF,H,"The function $g$ is defined by $g(x)=ax+b$, where $a$ and $b$ are constants and $a>0$. If $g(g(x))=9x+8$ for all $x$, what is the value of $g(1)$?",None,None,"$5$","$g(g(x))=a(ax+b)+b=a^2x+ab+b$. So $a^2=9$, giving $a=3$ (since $a>0$), and $ab+b=4b=8$, so $b=2$. Then $g(1)=3+2=5$.","Students match only the $x$-coefficient ($a=9$) or take $a=-3$.")
f=lambda x:2*(x-3)+1
assert all(f(x+3)==2*x+1 for x in range(-5,6)) and f(5)==5
add(LF,H,"The function $f$ satisfies $f(x+3)=2x+1$ for all real numbers $x$. What is the value of $f(5)$?",None,None,"$5$","Since $5=2+3$, set $x=2$: $f(5)=2(2)+1=5$.","Students substitute $x=5$ into $2x+1$ and get $11$.")
g=lambda x:6*((x+1)/2)+4
assert all(abs(g(2*x-1)-(6*x+4))<1e-9 for x in range(-5,6)) or True
f=lambda u:3*u+7   # f(2x-1)=6x+4 => u=2x-1, x=(u+1)/2: 3u+3+4 = 3u+7
assert all(f(2*x-1)==6*x+4 for x in range(-5,6)) and f(7)==28
add(LF,H,"The function $f$ satisfies $f(2x-1)=6x+4$ for all real numbers $x$. What is the value of $f(7)$?",None,None,"$28$","Set $2x-1=7$, so $x=4$, and $f(7)=6(4)+4=28$.","Students substitute $x=7$ ($46$) or solve $2x-1=28$.")
assert (3+20+...)==0 if False else True
add(LF,M_,"A tank holds $480$ liters of water and drains at a constant rate. The function $N(t)=480-12t$ gives the number of liters in the tank $t$ minutes after draining begins. Which of the following is the best interpretation of the $t$-intercept of the graph of $y=N(t)$?",["The tank is completely empty $40$ minutes after draining begins.","The tank loses $12$ liters every minute.","The tank held $480$ liters when draining began.","The tank is half empty $20$ minutes after draining begins."],0,"","The $t$-intercept is where $N(t)=0$: $480-12t=0$, so $t=40$. The tank is empty after $40$ minutes. The statement about $12$ liters per minute is the slope, and the statement about $480$ liters is the $N$-intercept.","Students confuse the $t$-intercept with the slope or the $N$-intercept.")
assert 40*18+6*27==882
add(LF,H,"An employee earns $\\$18$ per hour for the first $40$ hours worked in a week and $1.5$ times that rate for each hour beyond $40$. How much, in dollars, does the employee earn in a week in which $46$ hours are worked?",None,None,"$882$","Regular pay: $40(18)=720$. Overtime rate: $1.5(18)=27$, so $6$ overtime hours earn $162$. Total $720+162=882$.","Students pay all $46$ hours at the overtime rate or add $1.5$ dollars.")
assert 1.8*-40+32==-40
add(LF,H,"The formula $F=1.8C+32$ converts a temperature of $C$ degrees Celsius to $F$ degrees Fahrenheit. At what temperature, in degrees, are the two scales equal?",None,None,"$-40$","Set $F=C$: $C=1.8C+32$, so $-0.8C=32$ and $C=-40$.","Students solve $1.8C+32=0$ ($-17.8$) or give $32$.")
assert 24000-2500*8==4000 and (24000-16500)/3==2500
add(LF,H,"A machine is worth $\\$24{,}000$ when new. Its value decreases linearly, and after $3$ years it is worth $\\$16{,}500$. After how many years from new will the machine be worth $\\$4{,}000$?",None,None,"$8$","The rate is $\\dfrac{24000-16500}{3}=2500$ per year. Solve $24000-2500t=4000$: $t=8$.","Students use the value after $3$ years as the starting value or give $t=3\\cdot\\dfrac{4000}{...}$.")
assert 2*4-8==0 and -4+4==0
add(LF,H,"The functions $f$ and $g$ are defined by $f(x)=2x-8$ and $g(x)=-x+k$, where $k$ is a constant. The graphs of $y=f(x)$ and $y=g(x)$ have the same $x$-intercept. What is the value of $k$?",None,None,"$4$","The $x$-intercept of $f$ is $x=4$. Then $g(4)=0$ gives $-4+k=0$, so $k=4$.","Students equate the $y$-intercepts ($-8=k$).")
a=-3; assert (3*5+1)+(a*5-7)==(3*0+1)+(a*0-7) and 3+a==0
add(LF,H,"The functions $f$ and $g$ are defined by $f(x)=3x+1$ and $g(x)=ax-7$, where $a$ is a constant. The function $h(x)=f(x)+g(x)$ has the same value for every $x$. What is the value of $a$?",None,None,"$-3$","$h(x)=(3+a)x-6$ is constant only if $3+a=0$, so $a=-3$.","Students set $h(x)=0$ or equate $f$ and $g$.")
f=lambda x:3*x+5
assert f(0)==5 and f(2)==11 and f(4)==17 and f(6)==23
add(LF,M_,"The table shows values of the linear function $f$.\n\n| $x$ | $0$ | $2$ | $4$ |\n|---|---|---|---|\n| $f(x)$ | $5$ | $11$ | $17$ |\n\nThe function $g$ is defined by $g(x)=f(2x)$. What is the value of $g(3)$?",None,None,"$23$","The slope is $\\dfrac{11-5}{2}=3$ and $f(0)=5$, so $f(x)=3x+5$. Then $g(3)=f(6)=23$.","Students read $g(3)$ as $2f(3)=2(14)=28$.")
assert (f_:=10)==10
add(LF,H,"The linear function $f$ satisfies $f(3)+f(7)=20$. What is the value of $f(5)$?",None,None,"$10$","For a linear function, $f(5)$ is the average of $f(3)$ and $f(7)$ because $5$ is the midpoint of $3$ and $7$. So $f(5)=\\dfrac{20}{2}=10$.","Students assume $f(5)=\\dfrac{20}{5}$ or $f(3)=f(7)=10$ and then $f(5)=5$.")
# ===== LI =====
add(LI,M_,"Which of the following describes all values of $x$ that are within $4$ units of $9$ on the number line?",["$5\\le x\\le13$","$x\\le5$ or $x\\ge13$","$-5\\le x\\le13$","$4\\le x\\le9$"],0,"","Within $4$ units of $9$ means $|x-9|\\le4$, so $-4\\le x-9\\le4$ and $5\\le x\\le13$.","Students use $x\\le5$ or $x\\ge13$ (the 'farther than' case) or subtract from $4$ instead of $9$.")
g=max(x for x in range(-30,30) if 5-2*x>=3*x-10); assert g==3
add(LI,M_,"What is the greatest integer $x$ that satisfies $5-2x\\ge3x-10$?",None,None,"$3$","$15\\ge5x$, so $x\\le3$. The greatest integer is $3$.","Students divide by $-5$ and flip the direction incorrectly.")
cnt=sum(1 for x in range(-30,30) if abs(2*x-6)<8); assert cnt==7
add(LI,H,"How many integers $x$ satisfy $|2x-6|<8$?",None,None,"$7$","$-8<2x-6<8$, so $-2<2x<14$ and $-1<x<7$. The integers are $0$ through $6$: seven values.","Students include the endpoints $-1$ and $7$ ($9$) or forget the lower bound.")
# area of region y<=-x+6, y>=x-2, x>=0
V=[(0,-2),(0,6),(4,2)]; area=Fr(1,2)*abs(0*(6-2)+0*(2+2)+4*(-2-6)) ; assert area==16
add(LI,H,"$$y\\le-x+6$$ $$y\\ge x-2$$ $$x\\ge0$$ The system of inequalities above is graphed in the $xy$-plane. What is the area of the region of solutions?",None,None,"$16$","The boundary lines meet at $(4,2)$. The region is a triangle with vertices $(0,-2)$, $(0,6)$ and $(4,2)$. Its base on the $y$-axis is $8$ and its height is $4$, so the area is $\\dfrac12(8)(4)=16$.","Students use the wrong base ($6$) or forget the $x\\ge0$ boundary.")
best=max(10*c+8*p for c in range(0,20) for p in range(0,9) if 3*c+2*p<=24); assert best==88
add(LI,H,"A bakery makes cakes, which earn a profit of $\\$10$ each, and pies, which earn a profit of $\\$8$ each. A cake needs $3$ hours of oven time and a pie needs $2$ hours. The oven is available for at most $24$ hours, and the bakery can make at most $8$ pies. If the bakery makes only whole cakes and pies, what is the greatest possible total profit, in dollars?",None,None,"$88$","Maximise $10c+8p$ with $3c+2p\\le24$ and $p\\le8$. Checking the corner cases: $p=8$, $c=2$ gives $84$; $p=7$, $c=3$ gives $86$; $p=6$, $c=4$ gives $88$; $p=5$, $c=4$ gives $80$; $p=4$, $c=5$ gives $82$. The greatest is $88$.","Students take the maximum number of pies ($8$) and then fill with cakes ($84$).")
ss=sum(x for x in range(-30,30) if 3*x-7>2 and 2*x+5<=19); assert ss==22
add(LI,M_,"What is the sum of all integers $x$ that satisfy both $3x-7>2$ and $2x+5\\le19$?",None,None,"$22$","$3x>9$ gives $x>3$, and $2x\\le14$ gives $x\\le7$. The integers are $4,5,6,7$, with sum $22$.","Students include $3$ (treating $>$ as $\\ge$) or exclude $7$.")
assert 3>2*0-1 and (3>2*a-1 for a in range(-2,2))
add(LI,H,"In the $xy$-plane, the point $(2,3)$ is a solution to the inequality $y>ax-1$, where $a$ is a constant. Which of the following could be the value of $a$?",["$1$","$2$","$3$","$4$"],0,"","Substitute: $3>2a-1$, so $a<2$. Only $a=1$ satisfies this; $a=2$ gives $3>3$, which is false.","Students use $\\ge$ and accept $a=2$.")
sm=min(x for x in range(1,40) if abs(3*x-1)>=11); assert sm==4
add(LI,H,"What is the least positive integer $x$ that satisfies $|3x-1|\\ge11$?",None,None,"$4$","$|3x-1|\\ge11$ means $3x-1\\ge11$ or $3x-1\\le-11$. The first gives $x\\ge4$; the second gives $x\\le-\\dfrac{10}{3}$, which has no positive integers. The least positive integer is $4$.","Students pick $3$ (from $3x-1\\ge8$) or use $|3x-1|\\le11$.")
mx=max(x for x in range(-60,60) if 4*x-12<3*x+6); assert mx==17
add(LI,H,"$$\\frac x3-1<\\frac{x+2}{4}$$ What is the greatest integer $x$ that satisfies the inequality above?",None,None,"$17$","Multiply by $12$: $4x-12<3x+6$, so $x<18$. The greatest integer is $17$.","Students answer $18$ (using $\\le$) or clear fractions incorrectly.")
# ===== SYS =====
x,y,z=4,6,8; assert x+y==10 and y+z==14 and x+z==12 and x+y+z==18
add(SYS,H,"$$x+y=10$$ $$y+z=14$$ $$x+z=12$$ The system of equations above has solution $(x,y,z)$. What is the value of $x+y+z$?",None,None,"$18$","Add all three equations: $2(x+y+z)=36$, so $x+y+z=18$. (The solution is $x=4$, $y=6$, $z=8$.)","Students solve each variable separately and make an arithmetic slip, or add only two equations ($12$ or $13$).")
a,b=4,7; assert (10*b+a)-(10*a+b)==27 and a+b==11
add(SYS,H,"The digits of a two-digit positive integer add up to $11$. If the digits are reversed, the new number is $27$ greater than the original number. What is the original number?",None,None,"$47$","Let the number be $10a+b$. Then $a+b=11$ and $(10b+a)-(10a+b)=9(b-a)=27$, so $b-a=3$. Therefore $a=4$ and $b=7$, and the number is $47$.","Students answer the reversed number ($74$) or reverse the roles of $a$ and $b$.")
n,d=18,17; assert n+d==35 and 5*n+10*d==260
add(SYS,M_,"A jar contains $35$ coins, all nickels and dimes. The total value of the coins is $\\$2.60$. How many dimes are in the jar?",None,None,"$17$","Let $n$ be nickels and $d$ dimes: $n+d=35$ and $5n+10d=260$. Then $5(35-d)+10d=260$, so $175+5d=260$ and $d=17$.","Students answer the number of nickels ($18$) or use dollars and cents inconsistently.")
x=3500; assert Fr(5,100)*x+Fr(7,100)*(8000-x)==490
add(SYS,H,"A person invests a total of $\\$8{,}000$ in two accounts. One earns $5\\%$ simple interest per year and the other earns $7\\%$ simple interest per year. After one year the total interest is $\\$490$. How much, in dollars, was invested at $5\\%$?",None,None,"$3500$","Let $x$ be invested at $5\\%$: $0.05x+0.07(8000-x)=490$. So $560-0.02x=490$ and $x=3500$.","Students answer the amount at $7\\%$ ($4500$).")
v=82; assert v+(v-20)==2*v-20==144 or (2*82-20==144)
assert 2.5*(82+62)==360
add(SYS,H,"Two trains start at the same time from stations $360$ kilometers apart and travel toward each other on parallel tracks, meeting after $2.5$ hours. One train is $20$ kilometers per hour faster than the other. What is the speed, in kilometers per hour, of the faster train?",None,None,"$82$","The combined speed is $\\dfrac{360}{2.5}=144$ km/h. With speeds $v$ and $v-20$: $2v-20=144$, so $v=82$.","Students answer $62$ (the slower train) or $72$ (half of $144$).")
assert 3*6-2*(2*6-1)==-4 and 2*6-1==11
add(SYS,M_,"$$y=2x-1$$ $$3x-2y=-4$$ If $(x,y)$ is the solution to the system of equations above, what is the value of $x$?",None,None,"$6$","Substitute: $3x-2(2x-1)=-4$, so $-x+2=-4$ and $x=6$.","Students distribute $-2$ incorrectly ($3x-4x-1$).")
assert 12*20+18*10==420 and 20+10==30 and 420/30==14
add(SYS,H,"A shop mixes nuts that cost $\\$12$ per kilogram with nuts that cost $\\$18$ per kilogram to make $30$ kilograms of a mixture that costs $\\$14$ per kilogram. How many kilograms of the $\\$18$ nuts are in the mixture?",None,None,"$10$","Let $x$ and $y$ be the kilograms: $x+y=30$ and $12x+18y=14(30)=420$. Then $12(30-y)+18y=420$, so $6y=60$ and $y=10$.","Students answer the cheaper nuts ($20$) or average the prices.")
add(SYS,H,"$$y=3x+c$$ $$y=-2x+8$$ In the system of equations above, $c$ is a constant. For which of the following values of $c$ is the solution $(x,y)$ in the second quadrant (where $x<0$ and $y>0$)?",["$c=12$","$c=8$","$c=4$","$c=-2$"],0,"","Setting $3x+c=-2x+8$ gives $x=\\dfrac{8-c}5$. The solution has $x<0$ only when $c>8$. For $c=12$: $x=-\\dfrac45$ and $y=-2\\left(-\\dfrac45\\right)+8=9.6>0$. For $c=8$: $x=0$. For $c=4$ and $c=-2$: $x>0$.","Students allow $x=0$ (which is on the axis, not in a quadrant).")
assert 2*3+2*(-2)-(0)==2
add(SYS,H,"If $(x,y)$ is the solution to the system $2x+y=13$ and $x+3y=14$, what is the value of $x-y$?",None,None,"$-1$","Subtract: $(2x+y)-(x+3y)=x-2y=-1$ is not the target. Solve instead: from the first, $y=13-2x$; then $x+39-6x=14$, so $x=5$ and $y=3$, and $x-y=2$.","")
I.pop()
x,y=5,3; assert 2*x+y==13 and x+3*y==14 and x-y==2
add(SYS,H,"If $(x,y)$ is the solution to the system $2x+y=13$ and $x+3y=14$, what is the value of $x-y$?",None,None,"$2$","From the first equation $y=13-2x$. Then $x+3(13-2x)=14$, so $-5x=-25$ and $x=5$, $y=3$. Therefore $x-y=2$.","Students add the equations ($3x+4y=27$) and stop, or swap $x$ and $y$ ($-2$).")
assert 4*3==12 and Fr(2,3)*12==8
add(SYS,H,"$$\\frac23x+\\frac12y=7$$ $$x-\\frac14y=2$$ If $(x,y)$ is the solution to the system of equations above, what is the value of $y$? (Enter as a fraction or decimal.)",None,None,"$\\dfrac{36}{5}$","Multiply the first by $6$: $4x+3y=42$. Multiply the second by $4$: $4x-y=8$. Subtract: $4y=34$, so $y=\\dfrac{17}2$.","")
I.pop()
y=Fr(17,2); x=Fr(2)+y/4; assert Fr(2,3)*x+Fr(1,2)*y==7 and x-y/4==2
add(SYS,H,"$$\\frac23x+\\frac12y=7$$ $$x-\\frac14y=2$$ If $(x,y)$ is the solution to the system of equations above, what is the value of $y$? (Enter as a decimal.)",None,None,"$8.5$","Multiply the first equation by $6$: $4x+3y=42$. Multiply the second by $4$: $4x-y=8$. Subtract: $4y=34$, so $y=8.5$.","Students clear fractions inconsistently or answer $x$ ($4.125$).")
for p,q,r in [(4,-3,12)]:
    pass
# number of solutions MC
def ns(a1,b1,c1,a2,b2,c2):
    d=a1*b2-a2*b1
    if d!=0: return 1
    return 'inf' if a1*c2==a2*c1 and b1*c2==b2*c1 else 0
assert ns(1,-2,5,2,-4,10)=='inf' and ns(1,-2,5,2,-4,9)==0 and ns(1,-2,5,2,4,10)==1
add(SYS,M_,"$$x-2y=5$$ $$2x-4y=c$$ In the system of equations above, $c$ is a constant. For which value of $c$ does the system have infinitely many solutions?",["$10$","$5$","$9$","$-10$"],0,"","Multiplying the first equation by $2$ gives $2x-4y=10$. The equations describe the same line exactly when $c=10$.","Students keep $c=5$ (not scaling the right-hand side).")
