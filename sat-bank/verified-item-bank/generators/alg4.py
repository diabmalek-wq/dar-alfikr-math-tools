import sys; sys.path.insert(0,'/home/claude/cb')
from alg_lib import *
H,M_="Hard","Medium"
def S(skill,d,q,ans,rat,mis): add(skill,d,q,None,None,ans,rat,mis)
def C(skill,d,q,opts,rat,mis): add(skill,d,q,opts,0,"",rat,mis)
# ===== LE1 =====
v=Fr(14,5); assert (2*v+1)/3-(v-2)/4==2
S(LE1,H,"What value of $x$ satisfies the equation $\\dfrac{2x+1}{3}-\\dfrac{x-2}{4}=2$? (Enter as a decimal.)","$2.8$ (or $\\dfrac{14}{5}$)","Multiply both sides by $12$: $4(2x+1)-3(x-2)=24$. Then $8x+4-3x+6=24$, so $5x=14$ and $x=2.8$.","Students distribute the minus sign only to $x$ in $-3(x-2)$, writing $-3x-6$, and get a different value.")
assert 3*6-7==2*3+5
S(LE1,M_,"In the equation $kx-7=2x+5$, $k$ is a constant. If $x=3$ is the solution, what is the value of $k$?","$6$","Substitute $x=3$: $3k-7=11$, so $3k=18$ and $k=6$.","Students solve for $x$ in terms of $k$ first, or forget to evaluate the right side at $x=3$ ($2\\cdot3+5=11$).")
for x in (-5,0,3): assert 3*(x+4)-5==3*x+7
S(LE1,M_,"$$a(x+4)-5=3x+b$$ In the equation above, $a$ and $b$ are constants. The equation has infinitely many solutions. What is the value of $b-a$?","$4$","Infinitely many solutions require identical sides. Matching the $x$-coefficients gives $a=3$. The left side is then $3x+12-5=3x+7$, so $b=7$. Therefore $b-a=4$.","Students match coefficients but forget the constant $-5$ that comes with the parentheses, giving $b=12$.")
s=5;o=15; assert o==3*s and o+5==2*(s+5)
S(LE1,M_,"Omar is now $3$ times as old as his sister. In $5$ years, Omar will be twice as old as his sister will be then. How old is Omar now?","$15$","Let his sister be $s$ years old now, so Omar is $3s$. Then $3s+5=2(s+5)$, which gives $s=5$. Omar is $3s=15$.","Students answer with the sister's age ($5$) or write $2s$ instead of $2(s+5)$.")
n=24; assert n+(n+2)+(n+4)+(n+6)==108
S(LE1,M_,"The sum of four consecutive even integers is $108$. What is the largest of the four integers?","$30$","Let the integers be $n,\\ n+2,\\ n+4,\\ n+6$. Their sum is $4n+12=108$, so $n=24$. The largest is $n+6=30$.","Students find the smallest integer ($24$) or treat consecutive even integers as differing by $1$.")
t=2; assert 12*(t+1)==18*t
S(LE1,H,"Cyclist A leaves a town riding at a constant $12$ kilometers per hour. One hour later, cyclist B leaves the same town on the same road at a constant $18$ kilometers per hour. How many hours after cyclist B starts does B catch up with A?","$2$","At time $t$ hours after B starts, A has ridden for $t+1$ hours. They meet when $12(t+1)=18t$, so $12=6t$ and $t=2$.","Students measure time from A's start ($t=3$) or forget A's one-hour head start.")
# ===== LE2 =====
assert Fr(-3-5,6-2)==-2 and 5-(-2)*2==9
S(LE2,M_,"A line in the $xy$-plane passes through the points $(2,5)$ and $(6,-3)$. What is the $y$-coordinate of the $y$-intercept of the line?","$9$","The slope is $\\dfrac{-3-5}{6-2}=-2$. Using $(2,5)$: $y-5=-2(x-2)$, so $y=-2x+9$. The $y$-intercept is $9$.","Students use the slope as the intercept ($-2$) or mis-signed $5-(-2)(2)$ as $1$.")
assert 3*5+4*3==27
S(LE2,H,"Line $m$ is parallel to the line $3x+4y=12$ and passes through the point $(5,3)$. What is the $x$-coordinate of the $x$-intercept of line $m$?","$9$","Parallel lines share the same left side, so $m$ is $3x+4y=c$. The point $(5,3)$ gives $c=15+12=27$. Setting $y=0$ gives $3x=27$, so $x=9$.","Students keep $c=12$ (the intercept of the original line, $x=4$) or use the slope in place of the intercept.")
k=3; assert Fr(1,2)*Fr(24,k)*6==24
S(LE2,H,"$$kx+4y=24$$ In the $xy$-plane, the graph of the equation above, where $k$ is a positive constant, forms a right triangle together with the $x$-axis and the $y$-axis. The area of the triangle is $24$ square units. What is the value of $k$?","$3$","The intercepts are $\\left(\\dfrac{24}{k},0\\right)$ and $(0,6)$. The area is $\\dfrac12\\cdot\\dfrac{24}{k}\\cdot6=\\dfrac{72}{k}$. Setting $\\dfrac{72}{k}=24$ gives $k=3$.","Students forget the factor $\\dfrac12$ in the area and get $k=6$ from $\\dfrac{144}{k}=24$.")
assert Fr(-11-1,7-(-2))*(1-(-2))+1==-3 and Fr(-3-1,1+2)==Fr(-4,3)
S(LE2,M_,"The points $(-2,1)$, $(1,k)$ and $(7,-11)$ lie on the same line in the $xy$-plane. What is the value of $k$?","$-3$","The slope between the outer points is $\\dfrac{-11-1}{7-(-2)}=-\\dfrac43$. Moving from $x=-2$ to $x=1$ is $3$ units, so $k=1+3\\left(-\\dfrac43\\right)=-3$.","Students use the midpoint idea ($k$ halfway between $1$ and $-11$) even though $x=1$ is not halfway between $-2$ and $7$.")
assert Fr(4-0,2-(-6))==Fr(1,2) and 4-Fr(1,2)*2==3
S(LE2,M_,"A line has an $x$-intercept at $(-6,0)$ and passes through the point $(2,4)$. What is the $y$-intercept of the line? (Enter the $y$-coordinate.)","$3$","The slope is $\\dfrac{4-0}{2-(-6)}=\\dfrac12$. Then $y=\\dfrac12(x+6)$, and at $x=0$ we get $y=3$.","Students compute the run as $2-6=-4$ instead of $2-(-6)=8$.")
import math
assert math.hypot(12,5)==13 and 5*12+12*0==60
C(LE2,M_,"The graph of $5x+12y=60$ in the $xy$-plane crosses the $x$-axis at point $P$ and the $y$-axis at point $Q$. What is the distance between $P$ and $Q$?",["$13$","$17$","$\\sqrt{119}$","$60$"],"Setting $y=0$ gives $P=(12,0)$ and setting $x=0$ gives $Q=(0,5)$. Then $PQ=\\sqrt{12^2+5^2}=13$.","Students add the intercepts ($12+5=17$) instead of applying the distance formula.")
assert -1+Fr(-3,2)*(0-4)==5
S(LE2,M_,"Line $\\ell$ has slope $-\\dfrac32$ and passes through the point $(4,-1)$. The point $(k,5)$ also lies on $\\ell$. What is the value of $k$?","$0$","Using point-slope form, $5-(-1)=-\\dfrac32(k-4)$, so $6=-\\dfrac32(k-4)$ and $k-4=-4$. Therefore $k=0$.","Students lose the sign: $6=\\dfrac32(k-4)$ gives $k=8$.")
# ===== LF =====
assert -3*(-1)+4==7 and -3*3+4==-5
C(LF,M_,"The linear function $f$ satisfies $f(-1)=7$ and $f(3)=-5$. What is the value of $f(0)$?",["$4$","$-3$","$1$","$10$"],"The slope is $\\dfrac{-5-7}{3-(-1)}=-3$. Then $f(0)=f(-1)+(-3)(1)=4$.","Students report the slope $-3$ or step in the wrong direction ($7+(-3)(-1)=10$).")
assert 3+2*4.5==12
S(LF,M_,"A ride-share charges a base fare of $\\$3$ plus $\\$0.40$ for every $\\dfrac15$ of a mile traveled. What is the fare, in dollars, for a trip of $4.5$ miles? (Ignore the dollar sign when entering your answer.)","$12$","There are $5$ fifths in each mile, so the charge is $\\$0.40\\cdot5=\\$2$ per mile. The fare is $3+2(4.5)=12$ dollars.","Students apply $\\$0.40$ per mile and get $3+0.4(4.5)=4.80$.")
assert 480-12*30==120
S(LF,M_,"A full tank holds $480$ liters of water. When a valve is opened, water drains at a constant rate, and $10$ minutes after the valve opens the tank contains $360$ liters. How many minutes after the valve opens will the tank contain $120$ liters?","$30$","The drain rate is $\\dfrac{480-360}{10}=12$ liters per minute. Solving $480-12t=120$ gives $t=30$.","Students count from $10$ minutes ($t=20$) or divide $120$ by the rate instead of the amount drained.")
C(LF,M_,"A school bus company charges $C(n)=350+12n$ dollars for a field trip, where $n$ is the number of students attending. Which of the following is the best interpretation of the number $12$ in this context?",["Each additional student increases the cost by $\\$12$","The cost for $0$ students is $\\$12$","The trip is limited to $12$ students","Twelve students ride for free"],"In a linear model $C(n)=b+mn$, the coefficient $m$ is the change in cost per additional student, so each added student adds $\\$12$. The constant $350$ is the cost with no students.","Students swap the roles of the constant term and the coefficient.")
assert 3*3+2==-3+14==11
S(LF,M_,"The functions $f(x)=3x+2$ and $g(x)=-x+14$ are graphed in the $xy$-plane and intersect at the point $(a,b)$. What is the value of $a+b$?","$14$","Setting $3x+2=-x+14$ gives $4x=12$, so $a=3$. Then $b=3(3)+2=11$, so $a+b=14$.","Students stop after finding $a=3$ or take $b$ from only one function incorrectly.")
a=3;b=2; assert a*a==9 and a*b+b==8 and a*2+b==8
S(LF,H,"The linear function $f$ is defined by $f(x)=ax+b$, where $a$ and $b$ are constants and $a>0$. For all $x$, $f(f(x))=9x+8$. What is the value of $f(2)$?","$8$","$f(f(x))=a(ax+b)+b=a^2x+ab+b$. So $a^2=9$, giving $a=3$ since $a>0$. Then $3b+b=8$, so $b=2$. Therefore $f(2)=3(2)+2=8$.","Students write $f(f(x))=(ax+b)^2$ or reject the condition $a>0$ and choose $a=-3$.")
assert 5+3*9==32
S(LF,H,"The function $f$ is linear. For every real number $x$, $f(x+2)-f(x)=6$, and $f(1)=5$. What is the value of $f(10)$?","$32$","Each increase of $2$ in $x$ adds $6$ to $f$, so the slope is $3$. From $x=1$ to $x=10$ is $9$ units, so $f(10)=5+3(9)=32$.","Students treat $6$ as the slope and compute $5+6(9)=59$.")
a_=Fr(2,3); b_=3-a_*2; assert b_==Fr(5,3)
S(LF,H,"The linear function $g(x)=ax+b$ has a slope equal to $\\dfrac13$ of the slope of the line through the points $(0,0)$ and $(3,6)$. The graph of $g$ passes through $(2,3)$. What is the value of $g(0)$? (Enter as a fraction or a decimal rounded to the nearest hundredth.)","$\\dfrac53$ (or $1.67$)","The line through $(0,0)$ and $(3,6)$ has slope $2$, so $a=\\dfrac23$. Using $(2,3)$: $3=\\dfrac23(2)+b$, so $b=\\dfrac53$. Thus $g(0)=\\dfrac53$.","Students use the slope $2$ unchanged or take $\\dfrac13$ of the point's coordinates.")
assert 8+3*11==41 and Fr(26-14,6-2)==3
S(LF,M_,"A plant's height is recorded each week. The height was $14$ cm at the end of week $2$ and $26$ cm at the end of week $6$. If the height grows at a constant rate, in which week will the height first reach $41$ cm?","$11$","The growth rate is $\\dfrac{26-14}{6-2}=3$ cm per week, so $h=14+3(w-2)$. Setting $h=41$ gives $w-2=9$, so $w=11$.","Students divide $41$ by $3$ or count $9$ weeks from the start instead of from week $2$.")
# ===== LI =====
assert 7*12+8*14<=200<7*12+8*15
S(LI,M_,"Concert tickets cost $\\$12$ for section A and $\\$8$ for section B. Mia has at most $\\$200$ to spend and buys exactly $7$ tickets in section A. What is the greatest number of section B tickets she can buy?","$14$","After $7$ section A tickets she has spent $84$. Then $84+8y\\le200$ gives $y\\le14.5$. Since $y$ must be a whole number, the greatest value is $14$.","Students round $14.5$ up to $15$ and overspend.")
k=3; assert 3*k-5==4
S(LI,H,"$$2x-5>3(x-k)$$ In the inequality above, $k$ is a constant. The solution set of the inequality is all real numbers $x$ such that $x<4$. What is the value of $k$?","$3$","$2x-5>3x-3k$ gives $-x>5-3k$, so $x<3k-5$ after dividing by $-1$ and reversing the inequality. Setting $3k-5=4$ gives $k=3$.","Students forget to reverse the inequality when dividing by $-1$ and get $x>3k-5$.")
cnt=[x for x in range(-50,50) if -3<(2*x-1)/5<=3]; assert cnt==list(range(-6,9)) and len(cnt)==15
S(LI,M_,"How many integers $x$ satisfy the compound inequality $-3<\\dfrac{2x-1}{5}\\le3$?","$15$","Multiply by $5$: $-15<2x-1\\le15$. Add $1$: $-14<2x\\le16$. Divide by $2$: $-7<x\\le8$. The integers are $-6$ through $8$, which is $15$ integers.","Students include $-7$ (treating $<$ as $\\le$) and count $16$ integers, or exclude $8$ and count $14$.")
pts=[(1,2),(3,2),(4,1),(0,7)]; ok=[p for p in pts if p[1]>2*p[0]-3 and p[1]<=-p[0]+6]; assert ok==[(1,2)]
C(LI,M_,"$$y>2x-3$$ $$y\\le-x+6$$ Which of the following ordered pairs $(x,y)$ is a solution to the system of inequalities above?",["$(1,2)$","$(3,2)$","$(4,1)$","$(0,7)$"],"For $(1,2)$: $2>-1$ is true and $2\\le5$ is true. The pair $(3,2)$ fails $2>3$, $(4,1)$ fails $1>5$, and $(0,7)$ fails $7\\le6$.","Students check only one of the two inequalities.")
assert [n for n in range(0,50) if 20+5*n<9*n][0]==6
S(LI,M_,"Gym A charges a $\\$20$ joining fee plus $\\$5$ per visit. Gym B has no joining fee and charges $\\$9$ per visit. What is the least whole number of visits for which Gym A costs less than Gym B in total?","$6$","Gym A is cheaper when $20+5n<9n$, so $n>5$. The least whole number greater than $5$ is $6$ (at $n=5$ the costs are equal).","Students answer $5$, where the two gyms cost the same.")
assert [x for x in range(0,100) if Fr(3,4)*x-2>=Fr(1,3)*x+4][0]==15
S(LI,M_,"What is the least integer $x$ that satisfies $\\dfrac34x-2\\ge\\dfrac13x+4$?","$15$","Multiply by $12$: $9x-24\\ge4x+48$, so $5x\\ge72$ and $x\\ge14.4$. The least integer is $15$.","Students round $14.4$ down to $14$, which does not satisfy the inequality.")
cnt=sum(1 for x in range(1,10) for y in range(1,10) if 3*x+2*y<=12); assert cnt==8
C(LI,M_,"How many ordered pairs $(x,y)$ of positive integers satisfy $3x+2y\\le12$?",["$8$","$6$","$9$","$10$"],"For $x=1$: $y\\le4.5$, so $y=1,2,3,4$ ($4$ pairs). For $x=2$: $y\\le3$ ($3$ pairs). For $x=3$: $y\\le1.5$, so $y=1$ ($1$ pair). For $x=4$: $y\\le0$, so none. The total is $4+3+1=8$.","Students count $y=0$ or non-integer values, or stop at $x=2$.")
assert 338+87>=5*85 and 338+86<5*85
S(LI,M_,"Dana's scores on her first four tests are $78$, $90$, $82$ and $88$. To get an average of at least $85$ on all five tests, what is the least score she can earn on the fifth test?","$87$","The four scores total $338$. She needs a total of at least $5\\cdot85=425$, so the fifth score is at least $425-338=87$.","Students average the first four scores ($84.5$) or divide by $4$ instead of $5$.")
# ===== SYS =====
C(SYS,M_,"$$2x+3y=12$$ $$4x+ay=20$$ In the system of equations above, $a$ is a constant. If the system has no solution, what is the value of $a$?",["$6$","$10$","$3$","$-6$"],"No solution means the lines are parallel and distinct. Doubling the first equation gives $4x+6y=24$, so the $y$-coefficients must match: $a=6$. Since $24\\ne20$, the lines are distinct and have no common point.","Students match the right-hand sides ($a=10$) rather than the coefficients of $y$.")
a_=21; assert a_+19==40 and 12*a_+7*19==385
S(SYS,M_,"A theater sold $40$ tickets for a total of $\\$385$. Adult tickets cost $\\$12$ each and child tickets cost $\\$7$ each. How many adult tickets were sold?","$21$","Let $a$ be adult tickets. Then $12a+7(40-a)=385$, so $5a=105$ and $a=21$.","Students report the child count ($19$) or write the total as $12a+7a$.")
bb=Fr(15,2);cc=Fr(3,2); assert bb+cc==9 and bb-cc==6
S(SYS,M_,"A boat travels $18$ miles downstream in $2$ hours and returns the same $18$ miles upstream in $3$ hours. Assuming the boat's own speed and the river's current are constant, what is the speed of the current, in miles per hour?","$1.5$","Downstream speed is $\\dfrac{18}{2}=9$ and upstream speed is $\\dfrac{18}{3}=6$. If $b$ is boat speed and $c$ is current speed, $b+c=9$ and $b-c=6$. Subtracting gives $2c=3$, so $c=1.5$.","Students report the boat's speed ($7.5$) or average the two speeds without subtracting.")
k=2; x=4; assert 3*x+2*x==20 and 5*x-k*x==12
S(SYS,H,"$$3x+2y=20$$ $$5x-ky=12$$ In the system above, $k$ is a constant. The solution $(x,y)$ to the system has $x=y$. What is the value of $k$?","$2$","With $x=y$, the first equation gives $5x=20$, so $x=y=4$. The second equation becomes $20-4k=12$, so $k=2$.","Students find $x$ but substitute it into the wrong equation or forget that $y=x$ also appears in $-ky$.")
x,y=2,3; assert 5*x+3*y==19 and 2*x+y==7 and x+2*y==8
S(SYS,M_,"If $5x+3y=19$ and $2x+y=7$, what is the value of $x+2y$?","$8$","From $2x+y=7$, $y=7-2x$. Then $5x+3(7-2x)=19$ gives $-x=-2$, so $x=2$ and $y=3$. Therefore $x+2y=8$.","Students find only $x$, or substitute into the wrong equation and make a sign error.")
y_=4; assert Fr(3,10)*(12-y_)+Fr(6,10)*y_==Fr(4,10)*12
S(SYS,M_,"A chemist mixes a $30\\%$ acid solution with a $60\\%$ acid solution to make $12$ liters of a $40\\%$ acid solution. How many liters of the $60\\%$ solution are used?","$4$","Let $y$ be liters of the $60\\%$ solution, so $12-y$ liters of the $30\\%$ solution are used. The acid amounts give $0.3(12-y)+0.6y=0.4(12)$, so $3.6+0.3y=4.8$ and $y=4$.","Students report the $30\\%$ amount ($8$) or average $30\\%$ and $60\\%$ to $45\\%$.")
b,n=Fr(1,2),Fr(1,5); assert 3*b+2*n==Fr(19,10) and 2*b+3*n==Fr(8,5) and b+n==Fr(7,10)
S(SYS,M_,"Three books and two notebooks weigh $1.9$ kilograms. Two books and three notebooks weigh $1.6$ kilograms. What is the combined weight, in kilograms, of one book and one notebook?","$0.7$","Adding the two equations $3b+2n=1.9$ and $2b+3n=1.6$ gives $5b+5n=3.5$. Dividing by $5$ gives $b+n=0.7$. No need to solve for each weight.","Students solve for $b$ and $n$ separately and make an arithmetic slip, or answer $b$ alone ($0.5$).")
k=4; assert 3*k+2*k*2==28 and 3*k==12
S(SYS,M_,"The ratio of $x$ to $y$ is $3$ to $2$, and $x+2y=28$. What is the value of $x$?","$12$","Write $x=3k$ and $y=2k$. Then $3k+4k=28$, so $k=4$ and $x=12$.","Students use $x=2k$ and $y=3k$ (reversing the ratio) or answer $y=8$.")
assert 30+Fr(1,5)*80==18+Fr(7,20)*80==46
S(SYS,M_,"Car rental company A charges a $\\$30$ fee plus $\\$0.20$ per mile. Company B charges an $\\$18$ fee plus $\\$0.35$ per mile. For how many miles driven do the two companies charge the same total?","$80$","Set $30+0.20m=18+0.35m$. Then $12=0.15m$, so $m=80$. (Both charge $\\$46$.)","Students report the common cost ($46$) or subtract the fees in the wrong direction.")
w=8;l=19; assert l==2*w+3 and 2*(w+l)==54 and w*l==152
S(SYS,M_,"The length of a rectangle is $3$ more than twice its width. The perimeter of the rectangle is $54$. What is the area of the rectangle?","$152$","With width $w$ and length $2w+3$, the perimeter gives $2(w+2w+3)=54$, so $w=8$ and the length is $19$. The area is $8\\cdot19=152$.","Students answer with the width or length, or use perimeter formula $w+l=54$.")
x=10; assert x+(3*x+6)==46 and 3*x+6==36
S(SYS,M_,"The sum of two numbers is $46$. One of the numbers is $6$ more than $3$ times the other number. What is the larger number?","$36$","Let the smaller number be $x$. Then $x+(3x+6)=46$, so $x=10$ and the larger number is $3(10)+6=36$.","Students give the smaller number ($10$) or write the larger as $3x-6$.")
assert len(I)>=38,len(I)
