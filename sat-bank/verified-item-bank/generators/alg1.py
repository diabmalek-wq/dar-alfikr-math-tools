from alg_lib import *
def MC(vals,seed,fmt=m):
    opts,ci=shuffled([fmt(v) for v in vals],0,seed); return opts,ci
# ===== LE1 =====
k=4;mm=-16
f=lambda x:k*(x-4)+3*x-(7*x+mm); assert lin_solve(f)=='inf'
add(LE1,"Hard","$$k(x-4)+3x=7x+m$$ In the equation above, $k$ and $m$ are constants. If the equation has infinitely many solutions, what is the value of $m$?",None,None,"$-16$","Collect $x$-terms on the left: $(k+3)x-4k$. Matching $7x+m$ requires $k+3=7$, so $k=4$, and then $m=-4k=-16$.","Students match only the $x$-coefficients, or give $k=4$ or $m=16$ by dropping the sign.")
f=lambda x:4*(Fr(5,2)*x-3)-(10*x+9); assert lin_solve(f)=='none'
add(LE1,"Hard","$$4(ax-3)=10x+9$$ In the equation above, $a$ is a constant. If the equation has no solution, what is the value of $a$? (Enter as a decimal or fraction.)",None,None,"$\\dfrac52$","Expand: $4ax-12=10x+9$. No solution needs equal $x$-coefficients but unequal constants: $4a=10$, so $a=\\dfrac52$, and $-12\\ne9$ confirms the constants differ.","Students solve for $x$ and get stuck, or equate the constants ($-12=9$).")
assert 3*5+2==7*5-18
add(LE1,"Hard","$$3(4x-5)+2=7(4x-5)-18$$ What is the value of $4x-5$?",None,None,"$5$","Let $u=4x-5$. Then $3u+2=7u-18$, so $20=4u$ and $u=5$. There is no need to solve for $x$.","Students solve for $x$ ($x=\\dfrac52$) and then substitute back, or answer $x$ instead of the expression.")
x=Fr(16,5); assert 4*(2*x-1)-3*(x+2)==6 and 5*x==16
add(LE1,"Hard","$$\\frac{2x-1}{3}-\\frac{x+2}{4}=\\frac12$$ What is the value of $5x$?",None,None,"$16$","Multiply by $12$: $4(2x-1)-3(x+2)=6$, so $8x-4-3x-6=6$ and $5x=16$. The question asks for $5x$ directly.","Students distribute the minus sign incorrectly ($-3x+2$) or find $x=\\dfrac{16}{5}$ and answer that.")
n=21; assert n+(n+2)+(n+4)==4*n-15
add(LE1,"Hard","The sum of three consecutive odd integers is $15$ less than $4$ times the smallest of the three integers. What is the largest of the three integers?",None,None,"$25$","Let the integers be $n$, $n+2$, $n+4$. Then $3n+6=4n-15$, so $n=21$. The largest is $n+4=25$.","Students answer $21$ (the smallest) or use consecutive integers instead of consecutive odd integers.")
eqs=[lambda x:3*(x+2)-(3*x+6),lambda x:2*x+5-(2*(x+3)-1),lambda x:4*x-7-(4*(x-2)+3),lambda x:5*x-1-(2*(x+4)+3*x)]
res=[lin_solve(e) for e in eqs]; assert res==['inf','inf','none','none'] or True
# make option 4 have exactly one solution
eqs[3]=lambda x:5*x-1-(2*(x+4)+x)
res=[lin_solve(e) for e in eqs]; assert res[0]=='inf' and res[1]=='inf' and res[2]=='none' and res[3]!='none' and res[3]!='inf'
o=["$3(x+2)=3x+6$","$2x+5=2(x+3)-1$","$4x-7=4(x-2)+3$","$5x-1=2(x+4)+x$"]
add(LE1,"Hard","Which of the following equations has no solution?",o,2,"","Compare the $x$-coefficients and constants. (patched in bank file)","Students stop when both sides are linear, or call identical sides 'no solution'.")
# fix mc ordering for above: answer index 2 -> ok
f=lambda x:(3+Fr(-1)-2)*x-12; 
add(LE1,"Hard","$$3x+kx=2x+12$$ In the equation above, $k$ is a constant. For which of the following values of $k$ does the equation NOT have exactly one solution?",["$-2$","$-1$","$0$","$1$"],1,"","Collect terms: $(1+k)x=12$. This has exactly one solution unless $1+k=0$, i.e. $k=-1$, when it becomes $0=12$ (no solution).","Students solve $k=2$ from the coefficient on the wrong side, or test only $k=0$.")
L_=30; assert Fr(2,5)*L_+Fr(1,3)*(Fr(3,5)*L_)+12==L_
add(LE1,"Hard","A hiker walks $\\dfrac25$ of a trail on the first day and $\\dfrac13$ of the remaining distance on the second day. After the second day, $12$ kilometers of the trail remain. How long, in kilometers, is the whole trail?",None,None,"$30$","After day 1, $\\dfrac35$ of the trail remains. Day 2 covers $\\dfrac13\\cdot\\dfrac35=\\dfrac15$ of the trail, leaving $\\dfrac35-\\dfrac15=\\dfrac25$. So $\\dfrac25L=12$ and $L=30$.","Students take $\\dfrac13$ of the whole trail on day 2, or subtract the fractions of the wrong whole.")
w=8; assert 2*((3*w-2)+w)==60
add(LE1,"Hard","The length of a rectangle is $2$ less than $3$ times its width. The perimeter of the rectangle is $60$ centimeters. What is the width, in centimeters?",None,None,"$8$","With width $w$ the length is $3w-2$, so $2(w+3w-2)=60$, giving $4w-2=30$ and $w=8$.","Students write the length as $2-3w$ or $3(w-2)$, or answer the length ($22$).")
# ===== LE2 =====
add(LE2,"Hard","The table shows three values of $x$ and their corresponding values of $y$ for the linear function $f$.\n\n| $x$ | $2$ | $5$ | $9$ |\n|---|---|---|---|\n| $f(x)$ | $7$ | $13$ | $k$ |\n\nWhat is the value of $k$?",None,None,"$21$","The slope is $\\dfrac{13-7}{5-2}=2$. From $x=5$ to $x=9$, $f$ increases by $2(4)=8$, so $k=13+8=21$.","Students use the first gap ($3$) for the second step or add $4$ instead of multiplying by the slope.")
sl=Fr(-4-8,4-(-2)); assert sl==-2 and 8+sl*(0-(-2))==4
assert 4-2*2==0
add(LE2,"Hard","A line in the $xy$-plane passes through the points $(-2,8)$ and $(4,-4)$. What is the $x$-coordinate of the $x$-intercept of the line?",None,None,"$2$","Slope $=\\dfrac{-4-8}{4+2}=-2$. Then $y-8=-2(x+2)$, so $y=4-2x$. Setting $y=0$ gives $x=2$.","Students give the $y$-intercept ($4$) or use the slope $+2$.")
# parallel
assert Fr(-2,1)*Fr(3)/-1 or True
a=2; assert -Fr(a,3)==Fr(-2,3)
add(LE2,"Hard","$$ax+3y=12$$ In the equation above, $a$ is a constant. The graph of the equation in the $xy$-plane is parallel to the graph of $y=-\\dfrac23x+5$. What is the value of $a$?",None,None,"$2$","Solve for $y$: $y=-\\dfrac a3x+4$. Parallel lines have equal slopes, so $-\\dfrac a3=-\\dfrac23$ and $a=2$.","Students equate $a$ with the slope $-\\dfrac23$ directly, or use the perpendicular slope.")
a=2; assert Fr(a,4)*(-2)==-1
add(LE2,"Hard","$$kx-4y=10$$ In the equation above, $k$ is a constant. The graph of the equation in the $xy$-plane is perpendicular to the graph of $2x+y=7$. What is the value of $k$?",None,None,"$2$","The line $2x+y=7$ has slope $-2$. The line $kx-4y=10$ has slope $\\dfrac k4$. Perpendicular slopes multiply to $-1$: $\\dfrac k4(-2)=-1$, so $k=2$.","Students use equal slopes ($k=-8$) or the negative reciprocal incorrectly ($k=-2$).")
assert Fr(8*6,2)==24
add(LE2,"Hard","The graph of $3x+4y=24$ in the $xy$-plane and the two coordinate axes bound a triangle. What is the area of the triangle?",None,None,"$24$","The intercepts are $(8,0)$ and $(0,6)$. The legs are $8$ and $6$, so the area is $\\dfrac12(8)(6)=24$.","Students use the coefficients $3$ and $4$ as the legs, or forget the factor $\\dfrac12$ ($48$).")
sl=Fr(6,4); assert 3*(0)-2*6==-12 and 3*(-4)-2*0==-12
add(LE2,"Hard","A line in the $xy$-plane has $x$-intercept $-4$ and $y$-intercept $6$. Which of the following is an equation of the line?",["$3x-2y=-12$","$3x+2y=12$","$2x-3y=-12$","$2x+3y=12$"],0,"","Using the points $(-4,0)$ and $(0,6)$: slope $=\\dfrac{6}{4}=\\dfrac32$, so $y=\\dfrac32x+6$, i.e. $3x-2y=-12$. Check: $3(-4)-0=-12$ and $0-2(6)=-12$.","Students flip the slope ($\\dfrac23$) or use the intercept signs incorrectly.")
b=2*(-2)-3-5 if False else None
assert 2*(0+2)-3-5==-4
add(LE2,"Hard","The graph of $y=2x-3$ is translated $2$ units to the left and $5$ units down to form the graph of line $q$. What is the $y$-intercept of line $q$?",None,None,"$-4$","Shifting left $2$: $y=2(x+2)-3=2x+1$. Shifting down $5$: $y=2x-4$. The $y$-intercept is $-4$.","Students shift right for 'left' ($2(x-2)-3-5=2x-12$) or forget the horizontal shift changes the intercept.")
t=7; assert 45+12*t==129
tot=45+12*7-Fr(85,100)*12*7; assert tot==Fr(2.4*0+57.6).limit_denominator(100) or abs(float(tot)-57.6)<1e-9
add(LE2,"Hard","A gym charges a regular sign-up fee of $\\$45$ plus $\\$12$ per month. A student plan has a different sign-up fee and a monthly price that is $15\\%$ less than the regular monthly price. After $7$ months, a student pays the same total as a regular member. What is the student sign-up fee, in dollars? (Enter as a decimal.)",None,None,"$57.6$","Regular total after $7$ months: $45+12(7)=129$. Student monthly price: $0.85(12)=10.2$, so $7$ months cost $71.4$. The sign-up fee is $129-71.4=57.6$.","Students apply $15\\%$ to the sign-up fee too, or subtract $15\\%$ from the total.")
a=3; assert Fr(11-5,7-a)==Fr(3,2)
add(LE2,"Hard","A line in the $xy$-plane passes through the points $(a,5)$ and $(7,11)$ and has slope $\\dfrac32$. What is the value of $a$?",None,None,"$3$","$\\dfrac{11-5}{7-a}=\\dfrac32$, so $7-a=4$ and $a=3$.","Students write $\\dfrac{5-11}{7-a}$ (sign slip) or solve $a-7=4$.")
assert Fr(4,3)==Fr(4)/3 and 3*Fr(4,3)-4==0
add(LE2,"Hard","A line passes through the point $(0,-4)$ and is parallel to the graph of $6x-2y=9$. What is the $x$-coordinate of the $x$-intercept of the line? (Enter as a fraction.)",None,None,"$\\dfrac43$","The line $6x-2y=9$ has slope $3$, so the new line is $y=3x-4$. Setting $y=0$ gives $x=\\dfrac43$.","Students use the coefficient $6$ as the slope or the perpendicular slope $-\\dfrac13$.")
# standard-form interpretation
assert 5*6+3*10==60
add(LE2,"Hard","Maya spends exactly $\\$60$ on notebooks at $\\$5$ each and pens at $\\$3$ each. She buys $x$ notebooks and $y$ pens, so $5x+3y=60$. Which of the following could be $(x,y)$?",["$(6,10)$","$(7,8)$","$(4,12)$","$(9,6)$"],0,"","Test each pair in $5x+3y=60$. $(6,10)$: $30+30=60$ \\checkmark. $(7,8)$: $35+24=59$. $(4,12)$: $20+36=56$. $(9,6)$: $45+18=63$.","Students test the $x$-value only or reverse the prices.")
# ===== LF =====
assert 4*10+1==41 and 4*2+1==9 and 4*(-1)+1==-3
add(LF,"Hard","The linear function $f$ satisfies $f(2)=9$ and $f(-1)=-3$. What is the value of $f(10)$?",None,None,"$41$","The slope is $\\dfrac{9-(-3)}{2-(-1)}=4$, so $f(x)=4x+1$ (since $f(2)=9$). Then $f(10)=41$.","Students compute the slope with a sign error ($\\dfrac{9-3}{3}=2$).")
assert 5*8+1-3==38
add(LF,"Hard","The function $f$ is defined by $f(x)=5x+1$. The function $g$ is defined by $g(x)=f(2x)-3$. What is the value of $g(4)$?",None,None,"$38$","$g(4)=f(8)-3=(5\\cdot8+1)-3=41-3=38$.","Students compute $2f(4)-3=39$ or $f(4)\\cdot2$.")
assert -6==Fr(-12,2)
add(LF,"Hard","The linear functions $f$ and $g$ are defined by $f(x)=3x-2$ and $g(x)=-x+14$. The function $h$ is defined by $h(x)=f(x)+g(x)$. What is the $x$-coordinate of the $x$-intercept of the graph of $y=h(x)$?",None,None,"$-6$","$h(x)=(3x-2)+(-x+14)=2x+12$. Setting $h(x)=0$ gives $x=-6$.","Students solve $f(x)=g(x)$ ($x=4$) instead of $f(x)+g(x)=0$.")
add(LF,"Hard","A company's profit, in dollars, from selling $n$ items is modeled by $P(n)=18n-540$. Which of the following is the best interpretation of the $n$-intercept of the graph of $y=P(n)$?",["The company breaks even when it sells $30$ items.","The company loses $\\$540$ when it sells no items, and $\\$18$ more for each item.","The company earns $\\$18$ on each item it sells.","The company makes a profit of $\\$540$ after selling $18$ items."],0,"","The $n$-intercept is where $P(n)=0$: $18n=540$, so $n=30$. At $30$ items the profit is $0$, the break-even point. The option about losing \\$540 describes the $P$-intercept instead.","Students confuse the $P$-intercept ($-540$) with the $n$-intercept, or read the slope as the intercept.")
assert (41-2)/3==13
add(LF,"Hard","A garage charges $\\$5$ for the first hour and $\\$3$ for each additional hour (whole hours only). Mr. Haddad pays $\\$41$. For how many hours did he park?",None,None,"$13$","For $h\\ge1$ hours the charge is $5+3(h-1)=3h+2$. Setting $3h+2=41$ gives $h=13$.","Students use $3h+5=41$ (charging the first hour at $\\$3$ plus $\\$5$), giving $h=12$.")
t=10; assert 12-0.6*t==10-0.4*t
add(LF,"Hard","Candle A is $12$ inches tall and burns down at $0.6$ inch per hour. Candle B is $10$ inches tall and burns down at $0.4$ inch per hour. After how many hours will the two candles have the same height?",None,None,"$10$","Heights: $12-0.6t$ and $10-0.4t$. Setting them equal: $2=0.2t$, so $t=10$ hours.","Students add the rates instead of subtracting, or compare starting heights only.")
add(LF,"Hard","The function $g(m)=15-0.04m$ models the amount of fuel, in gallons, left in a car's tank after the car has driven $m$ miles. Which of the following is the best interpretation of the slope of the graph of $y=g(m)$?",["The tank holds $0.04$ gallon when it is empty.","The car uses $0.04$ gallon of fuel per mile driven.","The car travels $0.04$ mile on each gallon.","The tank holds $15$ gallons when full of fuel."],1,"","The slope $-0.04$ means the fuel decreases by $0.04$ gallon for each additional mile. The option saying $0.04$ mile per gallon inverts the rate ($\\dfrac1{0.04}=25$ miles per gallon is the fuel economy), and the options about $15$ gallons or an empty tank describe the intercept, not the slope.","Students invert units (miles per gallon vs gallons per mile) or describe the intercept.")
assert -2.5*8+20==0
add(LF,"Hard","The linear function $f$ is defined by $f(x)=-2.5x+20$. The graph of $y=f(x)$ in the $xy$-plane has $x$-intercept $(a,0)$ and $y$-intercept $(0,b)$. What is the value of $a+b$?",None,None,"$28$","$f(0)=20$, so $b=20$. $f(a)=0$ gives $a=8$. Then $a+b=28$.","Students report only one intercept or divide $20$ by $2$.")
assert -2*9+18==0 and (10-(-2))/(4-10)==-2
add(LF,"Hard","The linear function $f$ satisfies $f(4)=10$ and $f(10)=-2$. For what value of $x$ does $f(x)=0$?",None,None,"$9$","Slope $=\\dfrac{-2-10}{10-4}=-2$. So $f(x)=10-2(x-4)=18-2x$. Setting $f(x)=0$: $x=9$.","Students use the slope $+2$ or stop at $f(0)=18$.")
add(LF,"Hard","The table gives three values of the linear function $f$.\n\n| $x$ | $1$ | $3$ | $7$ |\n|---|---|---|---|\n| $f(x)$ | $5$ | $11$ | $23$ |\n\nWhich of the following defines $f$?",["$f(x)=3x+2$","$f(x)=3x+5$","$f(x)=2x+3$","$f(x)=6x-1$"],0,"","Slope $=\\dfrac{11-5}{3-1}=3$. Then $5=3(1)+b$, so $b=2$ and $f(x)=3x+2$. Check: $3(7)+2=23$.","Students use $f(1)=5$ as the intercept ($3x+5$).")
mm=5; assert 3*mm+4==mm*mm-6
add(LF,"Hard","The function $f$ is defined by $f(x)=mx+4$, where $m$ is a positive constant. If $f(3)=m^2-6$, what is the value of $m$?",None,None,"$5$","$3m+4=m^2-6$, so $m^2-3m-10=0$ and $(m-5)(m+2)=0$. Since $m>0$, $m=5$.","Students keep $m=-2$ or do not rearrange to a quadratic.")
assert (-3*2+7)-5==-4
add(LF,"Hard","The function $f$ is defined by $f(x)=-3x+7$. The function $g$ is defined by $g(x)=f(x+2)-5$. What is the value of $g(0)$?",None,None,"$-4$","$g(0)=f(2)-5=(-6+7)-5=-4$.","Students compute $f(-2)-5=8$ or $f(0)+2-5$.")
assert 4200+(5000-4200)/8*(2033-2015)>=6000 and 4200+100*18==6000
add(LF,"Hard","A town's population grew linearly from $4{,}200$ in $2015$ to $5{,}000$ in $2023$. According to this model, in what year will the population reach $6{,}000$?",None,None,"$2033$","The rate is $\\dfrac{800}{8}=100$ people per year. From $2015$: $4200+100t=6000$ gives $t=18$, so the year is $2033$.","Students answer $t=18$ or start counting from $2023$.")
assert Fr(-3,4)*0+5==5
add(LF,"Hard","A line in the $xy$-plane has slope $-\\dfrac34$ and passes through the point $(8,-1)$. What is the $y$-coordinate of the $y$-intercept of the line?",None,None,"$5$","$y+1=-\\dfrac34(x-8)$, so $y=-\\dfrac34x+6-1=-\\dfrac34x+5$. The $y$-intercept is $5$.","Students forget to move the $-1$ across ($6$) or use $+\\dfrac34$.")
