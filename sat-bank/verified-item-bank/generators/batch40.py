import math
from fractions import Fraction as Fr
SRC="House-authored from a trick archetype found in the October 2026 web sweep (Bluebook PT4–PT10 walkthroughs, 2025–2026 real-test reports, prep guides). Archetype only; no source item, wording or numbers reproduced."
LF="Algebra — Linear functions"; L2="Algebra — Linear equations in two variables"; L1="Algebra — Linear equations in one variable"
LI="Algebra — Linear inequalities in one or two variables"; SY="Algebra — Systems of two linear equations in two variables"
NF="Advanced Math — Nonlinear functions"; NE="Advanced Math — Nonlinear equations in one variable and systems of equations in two variables"; EE="Advanced Math — Equivalent expressions"
AV="Geometry and Trigonometry — Area and volume"; LAT="Geometry and Trigonometry — Lines, angles, and triangles"
RT="Geometry and Trigonometry — Right triangles and trigonometry"; CI="Geometry and Trigonometry — Circles"
OV="Problem-Solving and Data Analysis — One-variable data: Distributions and measures of center and spread"
PC="Problem-Solving and Data Analysis — Percentages"; RR="Problem-Solving and Data Analysis — Ratios, rates, proportional relationships, and units"
PR="Problem-Solving and Data Analysis — Probability and conditional probability"; TV="Problem-Solving and Data Analysis — Two-variable data: Models and scatterplots"
NC="No calculator needed"; CA="Calculator"; DE="Desmos"
I=[]
def add(id,skill,diff,tool,q,rat,mis,opts=None,correct=None,ans=None):
    d=dict(id=id,skill=skill,diff=diff,tool=tool,q=q,rat=rat,mis=mis,opts=opts,correct=correct,ans=ans)
    if opts: assert len(set(opts))==4 and 0<=correct<4
    else: assert ans
    I.append(d)

# ======================= ALGEBRA (A-316 to A-335) =======================
add("A-316",LF,"Hard",NC,
 r"The function $f$ is linear, $f(3)=k$ and $f(k)=3$, where $k$ is a constant and $k\neq 3$. If $f(10)=-1$, what is the value of $k$?",
 r"The two points are $(3,k)$ and $(k,3)$. Slope $=\dfrac{3-k}{k-3}=-1$ for every $k\neq3$. So $f(x)=-x+b$. From $f(10)=-1$: $b=9$, so $f(x)=-x+9$ and $k=f(3)=6$. Check: $f(6)=3$ ✓.",
 r"Students think two unknowns ($k$ and the slope) cannot be found, or assume the slope is $+1$ because the inputs and outputs are swapped.",ans=r"$6$")
f=lambda x:-x+9; assert f(3)==6 and f(6)==3 and f(10)==-1
add("A-317",LF,"Hard",NC,
 r"The function $f$ is linear, $f(5)+f(-5)=14$, and $f(2)=13$. What is the value of $f(-2)$?",
 r"For $f(x)=mx+b$: $f(c)+f(-c)=2b$ for every $c$. So $2b=14$ and $f(2)+f(-2)=14$, giving $f(-2)=14-13=1$. ($m=3$, $b=7$.)",
 r"Students treat $f$ as odd and answer $-13$, or try to find $m$ and $b$ from one point.",
 opts=[r"$-13$",r"$1$",r"$-1$",r"$7$"],correct=1)
m,b=3,7; assert (5*m+b)+(-5*m+b)==14 and 2*m+b==13 and -2*m+b==1
add("A-318",LF,"Hard",NC,
 r"The function $f$ is linear, $f(2)+f(8)=30$, and $f(11)=33$. What is the value of $f(0)$?",
 r"For a linear function the average of two outputs is the output at the average input: $f(5)=\dfrac{30}{2}=15$. Slope $=\dfrac{33-15}{11-5}=3$, so $f(0)=15-5\cdot3=0$.",
 r"Students think a sum of two outputs gives no usable point and stop, or use $(2,30)$ as a point.",ans=r"$0$")
g=lambda x:3*x; assert g(2)+g(8)==30 and g(11)==33 and g(0)==0
add("A-319",L2,"Medium",NC,
 r"In the $xy$-plane, what is the $y$-intercept of the graph of $x=4y-12$?",
 r"Set $x=0$: $4y=12$, so $y=3$. The $y$-intercept is $(0,3)$. (Solving for $y$: $y=\tfrac14x+3$, so the slope is $\tfrac14$, not $4$.)",
 r"Students read the equation as if it were solved for $y$ and take $-12$ as the $y$-intercept or $4$ as the slope.",
 opts=[r"$(0,-12)$",r"$(-12,0)$",r"$(0,3)$",r"$(0,-3)$"],correct=2)
add("A-320",L2,"Hard",NC,
 r"In the equation $ax+by=c$, $a$, $b$ and $c$ are constants with $a>0$, $b<0$ and $c>0$. The graph of the equation in the $xy$-plane does NOT pass through which quadrant?",
 r"Solve for $y$: $y=-\dfrac ab x+\dfrac cb$. Since $b<0$: slope $-\dfrac ab>0$ and $y$-intercept $\dfrac cb<0$. A line with positive slope and negative $y$-intercept passes through Quadrants I, III and IV and misses Quadrant II. Test: $a=1,b=-1,c=1$ gives $y=x-1$.",
 r"Students forget that dividing by the negative $b$ flips both signs, and read the slope as $-\dfrac ab<0$.",
 opts=[r"Quadrant I",r"Quadrant II",r"Quadrant III",r"Quadrant IV"],correct=1)
add("A-321",LI,"Hard",NC,
 r"The system $2y-x>4$ and $y<5$ is graphed in the $xy$-plane. Which inequality describes all possible $x$-coordinates of points in the solution region?",
 r"From the first inequality, $x<2y-4$. Since $y<5$, $2y-4<6$, so every solution has $x<6$. Every $x<6$ is reached: for $x<6$ choose $y$ with $\dfrac{x+4}{2}<y<5$.",
 r"Students solve each inequality on its own (for example $x<-4$ from $y=0$) instead of combining them through $y$.",
 opts=[r"$x<6$",r"$x<14$",r"$x>6$",r"$x<-4$"],correct=0)
add("A-322",LI,"Hard",NC,
 r"For real numbers $x$ and $y$, $x+y<12$ and $x-y>4$. Which of the following must be true?",
 r"Rewrite the second inequality so both point the same way: $y-x<-4$. Adding $x+y<12$ and $y-x<-4$ gives $2y<8$, so $y<4$. The value of $x$ is not bounded: $(100,-90)$ satisfies both.",
 r"Students subtract the inequalities directly ($x+y-(x-y)<12-4$) or add them as written to get a false bound on $x$.",
 opts=[r"$x<8$",r"$x>8$",r"$y<4$",r"$y>4$"],correct=2)
assert 100-90<12 and 100+90>4
add("A-323",LI,"Hard",NC,
 r"If $-3\le x\le 2$ and $-5\le y\le 1$, what is the greatest possible value of $xy$?",
 r"Check the corner products: $(-3)(-5)=15$, $(-3)(1)=-3$, $2(-5)=-10$, $2(1)=2$. The greatest is $15$, from two negatives.",
 r"Students multiply the two upper bounds and answer $2$.",ans=r"$15$")
assert max(a*b for a in(-3,2) for b in(-5,1))==15
add("A-324",L2,"Medium",NC,
 r"A farm has $40$ hectares of date palms and $25$ hectares of olive trees. The equation $40x+25y=3{,}600$ represents the farm's total harvest, in tonnes, last season. What does $x$ represent?",
 r"$40$ is the number of date-palm hectares, so $40x$ is the date harvest in tonnes; $x$ is the date harvest per hectare, in tonnes.",
 r"Because $x$ is usually a count, students choose ``the number of hectares'', missing that the coefficients are the counts here.",
 opts=[r"The number of hectares of date palms",r"The average date harvest per hectare, in tonnes",r"The total date harvest, in tonnes",r"The number of tonnes harvested per date palm tree"],correct=1)
add("A-325",L2,"Medium",NC,
 r"A line in the $xy$-plane has slope $3$ and passes through the points $(2,k)$ and $(k,14)$. What is the value of $k$?",
 r"$\dfrac{14-k}{k-2}=3\Rightarrow14-k=3k-6\Rightarrow k=5$. Check: points $(2,5)$ and $(5,14)$, slope $\dfrac93=3$ ✓.",
 r"Students write the slope as $\dfrac{k-2}{14-k}$ (run over rise) and get a wrong value such as $11$.",
 opts=[r"$4$",r"$5$",r"$8$",r"$11$"],correct=1)
assert (14-5)/(5-2)==3
add("A-326",L2,"Hard",NC,
 r"In the $xy$-plane, the region with $x\ge0$, $y\ge0$ and $2x+y\le12$ is a triangle. The line $y=mx$ divides this triangle into two regions of equal area. What is the value of $m$?",
 r"The vertices are $(0,0)$, $(6,0)$ and $(0,12)$. A line through the vertex $(0,0)$ halves the area exactly when it passes through the midpoint of the opposite side, $(3,6)$. So $m=\dfrac63=2$. Check: the piece below the line, with vertices $(0,0)$, $(6,0)$ and $(3,6)$, has area $\tfrac12\cdot6\cdot6=18$, half of $36$ ✓.",
 r"Students halve a leg (for example the line through $(3,0)$ or $(0,6)$) instead of using the midpoint of the side opposite the origin.",ans=r"$2$")
add("A-327",LF,"Medium",NC,
 r"The function $V(t)=1{,}200-0.75t$ gives the volume, in liters, of water in a tank $t$ minutes after it starts draining. Which function gives the volume, in liters, $h$ hours after the tank starts draining?",
 r"$t=60h$, so $V=1{,}200-0.75(60h)=1{,}200-45h$.",
 r"Students divide the rate by $60$ instead of multiplying, or shift the input.",
 opts=[r"$1{,}200-0.0125h$",r"$1{,}200-45h$",r"$20-0.75h$",r"$1{,}200-0.75(h+60)$"],correct=1)
add("A-328",SY,"Hard",NC,
 r"In the system $y=2x+k$ and $y=-x+10$, $k$ is a constant. For how many integer values of $k$ is the solution $(x,y)$ in Quadrant I (that is, $x>0$ and $y>0$)?",
 r"$2x+k=-x+10\Rightarrow x=\dfrac{10-k}{3}$ and $y=\dfrac{20+k}{3}$. $x>0\Rightarrow k<10$; $y>0\Rightarrow k>-20$. Integers from $-19$ to $9$: $29$ values.",
 r"Students include an endpoint ($k=10$ or $k=-20$) or count $9-(-19)=28$.",ans=r"$29$")
assert sum(1 for k in range(-100,100) if (10-k)/3>0 and (20+k)/3>0)==29
add("A-329",LI,"Medium",NC,
 r"In the inequality $kx+4<10$, $k$ is a constant and $k<0$. Which describes the solution set?",
 r"$kx<6$. Dividing by the negative $k$ reverses the inequality: $x>\dfrac6k$. Test $k=-2$: $-2x<6\Rightarrow x>-3=\dfrac{6}{-2}$ ✓.",
 r"Students divide by $k$ without reversing the sign because the letter $k$ looks positive.",
 opts=[r"$x<\dfrac6k$",r"$x>\dfrac6k$",r"$x>-\dfrac6k$",r"$x<-\dfrac6k$"],correct=1)
add("A-330",L2,"Medium",NC,
 r"A shopper spends exactly $600$ dollars on $x$ kilograms of oranges at $4$ dollars per kilogram and $y$ kilograms of apples at $5$ dollars per kilogram, so $4x+5y=600$. If the shopper buys $10$ more kilograms of oranges and still spends $600$ dollars, by how many kilograms does $y$ decrease?",
 r"$4\Delta x+5\Delta y=0\Rightarrow 4(10)+5\Delta y=0\Rightarrow\Delta y=-8$: $y$ decreases by $8$ kg.",
 r"Students answer $-10$ (one-for-one trade) or $-12.5$ (dividing by $4$ and multiplying by $5$).",ans=r"$8$")
add("A-331",L2,"Hard",NC,
 r"If $7x-2y=3x+6y$ and $x$ and $y$ are nonzero, what is the value of $\dfrac{x+y}{x-y}$?",
 r"$4x=8y$, so $x=2y$. Then $\dfrac{x+y}{x-y}=\dfrac{3y}{y}=3$.",
 r"Students believe one equation in two unknowns cannot fix a value, and choose ``cannot be determined''.",
 opts=[r"$2$",r"$3$",r"$\dfrac13$",r"The value cannot be determined from the information given."],correct=1)
add("A-332",SY,"Hard",NC,
 r"Consider the system $3x-4y=10$ and $-6x+8y=-20$. Which point lies on the graphs of both equations for every real number $t$?",
 r"The second equation is $-2$ times the first, so the graphs are the same line and every point of $3x-4y=10$ works. Let $x=t$: $4y=3t-10$, so the point is $\left(t,\dfrac{3t-10}{4}\right)$. (With $y=t$, $x=\dfrac{4t+10}{3}$, not $\dfrac{4t-10}{3}$.)",
 r"Students make a sign error isolating $y$, or give up because the system has ``no single solution''.",
 opts=[r"$\left(t,\dfrac{3t-10}{4}\right)$",r"$\left(t,\dfrac{10-3t}{4}\right)$",r"$\left(\dfrac{4t-10}{3},t\right)$",r"$\left(t,\dfrac{3t+10}{4}\right)$"],correct=0)
for t in(-3,0,2.5,7): assert abs(3*t-4*(3*t-10)/4-10)<1e-12
add("A-333",L1,"Hard",NC,
 r"A wall is $9x$ meters long, where $x$ is a positive integer. Lamps are placed at both ends of the wall and every $\dfrac97$ meters along it. Which expression gives the number of lamps?",
 r"Number of gaps $=\dfrac{9x}{9/7}=7x$. With a lamp at both ends, lamps $=$ gaps $+1=7x+1$. Check $x=7$: $63$ m, $49$ gaps, $50$ lamps.",
 r"Students count gaps instead of lamps ($7x$), or divide the wrong way ($\dfrac{81x}{7}+1$).",
 opts=[r"$7x$",r"$7x+1$",r"$9x+1$",r"$\dfrac{81x}{7}+1$"],correct=1)
add("A-334",SY,"Medium",NC,
 r"How many solutions does the system $2x+y=11$, $x-y=1$, $x+3y=-13$ have?",
 r"The first two equations give $3x=12$, so $(4,3)$. Test it in the third: $4+3(3)=13\neq-13$. No point lies on all three lines: $0$ solutions.",
 r"Students count the pairwise intersections ($3$) or stop after the first two equations ($1$).",
 opts=[r"Zero",r"Exactly one",r"Exactly two",r"Exactly three"],correct=0)
add("A-335",LF,"Hard",NC,
 r"An oven's temperature is $70^\circ\text{F}$ when it is switched on at $t=0$. For $3\le t\le12$, where $t$ is the time in minutes, the temperature is modeled by $T=a+bt$, where $a$ and $b$ are constants. The model gives $T=200$ at $t=3$ and $T=380$ at $t=7$. What is the value of $a$?",
 r"$b=\dfrac{380-200}{7-3}=45$. $a=200-45(3)=65$. The model is valid only for $t\ge3$, so its intercept $65$ need not equal the real starting temperature $70$.",
 r"Students assume the intercept must be the given starting value $70$.",ans=r"$65$")

# ======================= ADVANCED MATH (AM-303 to AM-321) =======================
add("AM-303",NE,"Hard",NC,
 r"In the equation $(k-2)x^2+4x+1=0$, $k$ is a constant. The equation has exactly one real solution for exactly two values of $k$. What is the sum of these two values of $k$?",
 r"Case 1: $k=2$ makes the equation linear, $4x+1=0$, one solution. Case 2: $k\neq2$ and $\Delta=16-4(k-2)=0$, so $k=6$. Sum $=2+6=8$.",
 r"Students use only the discriminant and miss that a zero leading coefficient makes the equation linear.",
 opts=[r"$6$",r"$8$",r"$2$",r"$4$"],correct=1)
assert 16-4*(6-2)==0
add("AM-304",NF,"Hard",NC,
 r"The function $g$ is defined by $g(x)=\dfrac{x^2-kx-18}{x+3}$, where $k$ is a constant. The graph of $y=g(x)$ in the $xy$-plane is a line with exactly one point removed. What is the $y$-coordinate of the removed point?",
 r"The graph is a line only if $x+3$ cancels, so $x=-3$ is a zero of the numerator: $9+3k-18=0$, $k=3$. Then $x^2-3x-18=(x+3)(x-6)$ and $g(x)=x-6$ for $x\neq-3$. The removed point is $(-3,-9)$.",
 r"Students give the $x$-coordinate $-3$, or answer $0$ because the function is undefined there.",ans=r"$-9$")
assert 9+3*3-18==0
add("AM-305",NF,"Hard",NC,
 r"The function $h$ is defined by $h(x)=\dfrac{x^2-4x-12}{x^2-36}$. What is the sum of all values of $x$ for which $h(x)=0$?",
 r"The numerator is $(x-6)(x+2)$, but $x=6$ also makes the denominator $0$, so $h(6)$ is undefined. The only zero is $x=-2$; the sum is $-2$.",
 r"Students set the numerator equal to $0$ and use the sum of its roots, $4$.",
 opts=[r"$4$",r"$-2$",r"$6$",r"$-8$"],correct=1)
add("AM-306",NF,"Hard",NC,
 r"The function $h$ is defined by $h(x)=x^2-9$ for $x<2$ and $h(x)=-2x+10$ for $x\ge2$. What is the sum of all values of $m$ for which $h(m)=0$?",
 r"For $x<2$: $x^2=9$ gives $x=\pm3$, but $3$ is not less than $2$, so only $-3$. For $x\ge2$: $x=5$ ✓. Sum $=-3+5=2$.",
 r"Students keep $x=3$ although it is outside its piece, giving $5$ or $8$.",
 opts=[r"$2$",r"$5$",r"$8$",r"$0$"],correct=0)
add("AM-307",NE,"Hard",NC,
 r"In the equation $\dfrac{x^2}{x-a}=\dfrac{9}{x-a}$, $a$ is a constant. For how many real values of $a$ does the equation have exactly one real solution?",
 r"Multiplying gives $x^2=9$, so $x=\pm3$, with the restriction $x\neq a$. The equation has exactly one solution when $a$ equals one of these roots: $a=3$ or $a=-3$. Two values.",
 r"Students treat the two roots as fixed and answer $0$, or think every $a$ works.",
 opts=[r"Zero",r"Exactly one",r"Exactly two",r"Infinitely many"],correct=2)
add("AM-308",NF,"Hard",NC,
 r"The function $f$ is defined by $f(x)=x^2-1$. How many distinct real solutions does the equation $f(f(x))=0$ have?",
 r"$f(u)=0$ when $u=\pm1$. $f(x)=1\Rightarrow x^2=2\Rightarrow x=\pm\sqrt2$. $f(x)=-1\Rightarrow x^2=0\Rightarrow x=0$ (one solution only). Total: $3$.",
 r"Students expect $2\times2=4$ solutions, or stop at the zeros of $f$ and answer $2$.",
 opts=[r"$2$",r"$3$",r"$4$",r"$1$"],correct=1)
add("AM-309",NE,"Hard",DE,
 r"How many solutions $(x,y)$ does the system $x^2+y^2=25$ and $y=x^2-5$ have?",
 r"Substitute $x^2=y+5$: $y+5+y^2=25\Rightarrow y^2+y-20=0\Rightarrow y=4$ or $y=-5$. $y=4$: $x=\pm3$ (two points). $y=-5$: $x^2=0$, $x=0$ (one point). Total $3$. Desmos: graph both and count the intersection points.",
 r"Students give every $y$-value two $x$-values ($4$) or count $y$-values only ($2$).",
 opts=[r"$2$",r"$3$",r"$4$",r"$1$"],correct=1)
add("AM-310",NE,"Hard",DE,
 r"How many real solutions does the equation $x^2=2^x$ have?",
 r"$x=2$ and $x=4$ work by inspection. For $x<0$, $x^2$ grows to $\infty$ as $x\to-\infty$ while $2^x\to0$, and at $x=0$, $x^2=0<1=2^0$, so the graphs also cross once for $x<0$ (near $x\approx-0.77$). Total $3$. Desmos: graph $y=x^2$ and $y=2^x$ and zoom out.",
 r"Students find $2$ and $4$ by testing integers and miss the negative root.",
 opts=[r"$1$",r"$2$",r"$3$",r"$4$"],correct=2)
lo,hi=-1.0,-0.5
for _ in range(60):
    mid=(lo+hi)/2
    if (lo**2-2**lo)*(mid**2-2**mid)<=0: hi=mid
    else: lo=mid
assert abs(lo+0.7667)<1e-3
add("AM-311",NE,"Medium",NC,
 r"What is the sum of all solutions to the equation $(x-3)^2=(2x+1)^2$?",
 r"$x-3=\pm(2x+1)$. With $+$: $x=-4$. With $-$: $x-3=-2x-1\Rightarrow x=\tfrac23$. Sum $=-4+\tfrac23=-\tfrac{10}{3}$.",
 r"Students take square roots without $\pm$ and find only $x=-4$.",ans=r"$-\dfrac{10}{3}$ (or $-3.333$)")
for x in(-4,Fr(2,3)): assert (x-3)**2==(2*x+1)**2
add("AM-312",EE,"Hard",NC,
 r"How many real solutions does the equation $\sqrt{x^2-10x+25}=5-x$ have?",
 r"$\sqrt{x^2-10x+25}=\sqrt{(x-5)^2}=|x-5|$. And $|x-5|=5-x$ exactly when $x-5\le0$, that is, for every $x\le5$. Infinitely many solutions.",
 r"Students write $\sqrt{(x-5)^2}=x-5$ and get only $x=5$, or square both sides, reach $0=0$ and panic.",
 opts=[r"Zero",r"Exactly one",r"Exactly two",r"Infinitely many"],correct=3)
for x in(-7,0,3,5): assert math.isclose(math.sqrt(x*x-10*x+25),5-x)
add("AM-313",NF,"Hard",NC,
 r"A kiosk's daily profit, in hundreds of dollars, is modeled by $P(x)=-2x^2+12x+5$, where $x$ is the price of an item in dollars. The model is used only for $4\le x\le7$. What is the greatest daily profit, in hundreds of dollars, predicted by the model on this interval?",
 r"The vertex is at $x=-\dfrac{12}{2(-2)}=3$, outside the interval. On $4\le x\le7$ the parabola is decreasing, so the maximum is $P(4)=-32+48+5=21$.",
 r"Students use the vertex value $P(3)=23$ without checking the interval.",
 opts=[r"$23$",r"$21$",r"$-9$",r"$5$"],correct=1)
P=lambda x:-2*x*x+12*x+5; assert P(3)==23 and P(4)==21 and P(7)==-9
add("AM-314",EE,"Hard",NC,
 r"The expression $\dfrac{6x^2+7x-5}{2x+3}$ is equivalent to $Ax+B+\dfrac{C}{2x+3}$, where $A$, $B$ and $C$ are constants. What is the value of $A+B+C$?",
 r"$(2x+3)(3x-1)=6x^2+7x-3$, so $6x^2+7x-5=(2x+3)(3x-1)-2$. $A=3$, $B=-1$, $C=-2$; sum $=0$.",
 r"Students use synthetic division with $-\tfrac32$ and forget to divide the quotient by $2$, getting $A=6$, $B=-2$.",
 opts=[r"$2$",r"$0$",r"$-4$",r"$4$"],correct=1)
for x in(0,1,5): assert 6*x*x+7*x-5==(2*x+3)*(3*x-1)-2
add("AM-315",NF,"Hard",NC,
 r"When the polynomial $p(x)$ is divided by $x-5$, the remainder is $8$. What is the remainder when $p(2x-1)$ is divided by $x-3$?",
 r"By the remainder theorem, the remainder is the value of $p(2x-1)$ at $x=3$, which is $p(5)=8$.",
 r"Students transform the remainder ($2\cdot8-1=15$) or answer the input $5$.",
 opts=[r"$15$",r"$5$",r"$8$",r"$3$"],correct=2)
add("AM-316",NF,"Hard",NC,
 r"For all real numbers $x$, $f(2x-1)=4x^2+3$. Which of the following defines $f(x)$?",
 r"Let $u=2x-1$, so $x=\dfrac{u+1}{2}$ and $4x^2=(u+1)^2$. Then $f(u)=(u+1)^2+3=u^2+2u+4$. Check: $x=3$ gives $f(5)=39$ and $25+10+4=39$ ✓.",
 r"Students copy the right side unchanged, or substitute $2x-1$ into it instead of inverting.",
 opts=[r"$f(x)=4x^2+3$",r"$f(x)=4x^2-4x+4$",r"$f(x)=x^2+2x+4$",r"$f(x)=x^2+4$"],correct=2)
for x in(-2,0,3): u=2*x-1; assert u*u+2*u+4==4*x*x+3
add("AM-317",NE,"Hard",DE,
 r"In the $xy$-plane, the graphs of $y=|x-2|$ and $y=mx+1$, where $m$ is a constant, intersect at exactly two points. Which of the following could be the value of $m$?",
 r"Right branch ($x\ge2$): $x=\dfrac{3}{1-m}\ge2$ needs $-\tfrac12\le m<1$. Left branch ($x<2$): $x=\dfrac1{1+m}<2$ needs $m>-\tfrac12$ (or $m<-1$). Both branches meet the line when $-\tfrac12<m<1$, so $m=\tfrac12$. Desmos: add a slider for $m$ and count intersections.",
 r"Students think any line through $(0,1)$ with a slope between $-1$ and $1$ works, or check only one branch.",
 opts=[r"$-\dfrac34$",r"$2$",r"$-2$",r"$\dfrac12$"],correct=3)
def cnt(m):
    c=0
    if m!=1:
        x=3/(1-m)
        if x>=2: c+=1
    if m!=-1:
        x=1/(1+m)
        if x<2: c+=1
    return c
assert cnt(0.5)==2 and cnt(-0.75)==0 and cnt(2)==1 and cnt(-2)==1
add("AM-318",NE,"Medium",NC,
 r"How many integers $x$ satisfy the inequality $x(x-4)<2x$?",
 r"$x^2-6x<0\Rightarrow x(x-6)<0\Rightarrow0<x<6$. Integers: $1,2,3,4,5$, so $5$.",
 r"Students divide both sides by $x$ (not allowed when $x$ may be negative or zero) and get $x<6$, which has infinitely many integers.",ans=r"$5$")
assert sum(1 for x in range(-50,50) if x*(x-4)<2*x)==5
add("AM-319",NF,"Hard",NC,
 r"The function $f$ is defined by $f(x)=a\big((x-3)^2-b\big)\big((x-3)^2-c\big)$, where $a$, $b$ and $c$ are constants. If $f(1)=40$ and $f(6)=-14$, what is the value of $f(5)+f(0)$?",
 r"$x$ appears only in $(x-3)^2$, so the graph is symmetric about $x=3$. $f(5)$ uses $(5-3)^2=4$, the same as $f(1)$, so $f(5)=40$. $f(0)$ uses $9$, the same as $f(6)$, so $f(0)=-14$. Sum $=26$.",
 r"Students try to solve for $a$, $b$ and $c$ (three unknowns, two equations) and decide it cannot be done.",ans=r"$26$")
add("AM-320",NE,"Hard",NC,
 r"In the equation $\dfrac{x+a}{x^2-a^2}=-\dfrac{3}{20x}$, $a$ is a constant. If $x=6$ is a solution, what is the value of $a$?",
 r"For $x\neq\pm a$, $\dfrac{x+a}{(x+a)(x-a)}=\dfrac1{x-a}$. So $\dfrac1{x-a}=-\dfrac3{20x}\Rightarrow20x=-3x+3a\Rightarrow a=\dfrac{23x}{3}=46$. Check: $\dfrac{52}{36-2116}=-\dfrac1{40}=-\dfrac{3}{120}$ ✓.",
 r"Students cross-multiply the full quadratic and lose signs, or stop at a value of $x$.",ans=r"$46$")
assert Fr(52,36-46*46)==Fr(-3,120)
add("AM-321",NE,"Hard",NC,
 r"In the equation $\dfrac{x^2}{\sqrt{x^2-k^2}}=\dfrac{k^2}{\sqrt{x^2-k^2}}+24$, $k$ is a positive constant. Which of the following is a solution?",
 r"$\dfrac{x^2-k^2}{\sqrt{x^2-k^2}}=24\Rightarrow\sqrt{x^2-k^2}=24\Rightarrow x^2=k^2+576\Rightarrow x=\pm\sqrt{k^2+576}$. Only the negative root is offered. Check $k=7$: $x=-25$.",
 r"Students forget to square $24$ (choosing $\sqrt{k^2+24}$) or reject a negative answer.",
 opts=[r"$k+24$",r"$\sqrt{k^2+24}$",r"$-\sqrt{k^2+576}$",r"$\sqrt{576-k^2}$"],correct=2)
k=7;x=-25;assert math.isclose(x*x/math.sqrt(x*x-k*k),k*k/math.sqrt(x*x-k*k)+24)

# ======================= GEOMETRY AND TRIGONOMETRY (GT-232 to GT-257) =======================
add("GT-232",CI,"Hard",NC,
 r"In the $xy$-plane, a circle has equation $(x-4)^2+(y+2)^2=50$. Which point lies in the interior of the circle?",
 r"Compare $(x-4)^2+(y+2)^2$ with $50$: $(-3,0)\to53$; $(9,3)\to50$ (on the circle); $(10,2)\to52$; $(-1,-6)\to25+16=41<50$, inside.",
 r"Students check each coordinate separately ($|x-4|<\sqrt{50}$ and $|y+2|<\sqrt{50}$), choose a point that is on the circle, or flip the centre's signs.",
 opts=[r"$(-3,0)$",r"$(9,3)$",r"$(10,2)$",r"$(-1,-6)$"],correct=3)
assert [(x-4)**2+(y+2)**2 for x,y in[(-3,0),(9,3),(10,2),(-1,-6)]]==[53,50,52,41]
add("GT-233",CI,"Hard",NC,
 r"The graph of $x^2+y^2+10x-8y+k=0$ in the $xy$-plane is a circle, where $k$ is a constant. What is the greatest possible integer value of $k$?",
 r"Complete the squares: $(x+5)^2+(y-4)^2=41-k$. A circle needs $r^2>0$, so $k<41$. Greatest integer: $40$. ($k=41$ gives a single point.)",
 r"Students allow $r^2=0$ and answer $41$, or reverse the inequality.",ans=r"$40$")
add("GT-234",RT,"Hard",NC,
 r"For $0<t<\dfrac{\pi}{2}$, $\sin t=0.6$. What is the value of $\cos(\pi+t)+\sin(\pi-t)$?",
 r"$\cos t=0.8$. On the unit circle, $\pi+t$ is in Quadrant III, so $\cos(\pi+t)=-\cos t=-0.8$; $\pi-t$ is in Quadrant II, so $\sin(\pi-t)=\sin t=0.6$. Sum $=-0.2$.",
 r"Students make both terms negative ($-1.4$) or both positive ($1.4$).",
 opts=[r"$-1.4$",r"$-0.2$",r"$0.2$",r"$1.4$"],correct=1)
t=math.asin(0.6); assert math.isclose(math.cos(math.pi+t)+math.sin(math.pi-t),-0.2)
add("GT-235",CI,"Hard",NC,
 r"Points $A$, $B$ and $C$ lie on a circle with radius $12$, and $C$ lies on the major arc $AB$. The measure of angle $ACB$ is $\dfrac{2\pi}{9}$ radians. What is the length of minor arc $AB$?",
 r"The central angle is twice the inscribed angle: $\dfrac{4\pi}{9}$. Arc length $=12\cdot\dfrac{4\pi}{9}=\dfrac{16\pi}{3}$.",
 r"Students use the inscribed angle as the central angle and get $\dfrac{8\pi}{3}$.",
 opts=[r"$\dfrac{8\pi}{3}$",r"$\dfrac{16\pi}{3}$",r"$\dfrac{56\pi}{3}$",r"$\dfrac{64\pi}{3}$"],correct=1)
add("GT-236",LAT,"Hard",NC,
 r"In triangle $ABC$, point $D$ lies on $\overline{AB}$ and point $E$ lies on $\overline{AC}$ so that the measure of angle $AED$ equals the measure of angle $ABC$. If $AD=4$, $DB=11$ and $AE=6$, what is the length of $\overline{EC}$?",
 r"Triangles $AED$ and $ABC$ share angle $A$ and have $\angle AED=\angle ABC$, so $A\leftrightarrow A$, $E\leftrightarrow B$, $D\leftrightarrow C$. Then $\dfrac{AE}{AB}=\dfrac{AD}{AC}$: $\dfrac6{15}=\dfrac4{AC}$, $AC=10$, $EC=10-6=4$. $\overline{DE}$ is NOT parallel to $\overline{BC}$.",
 r"Students assume $\overline{DE}\parallel\overline{BC}$ and use $\dfrac{AD}{DB}=\dfrac{AE}{EC}$, getting $16.5$.",
 opts=[r"$4$",r"$10$",r"$16.5$",r"$22.5$"],correct=0)
assert Fr(6,15)==Fr(4,10)
add("GT-237",RT,"Hard",NC,
 r"In right triangle $ABC$, angle $C$ is the right angle, $AC=16$ and $BC=12$. Point $E$ lies on $\overline{AC}$ with $AE=10$, and point $F$ lies on $\overline{AB}$ so that $\overline{EF}\perp\overline{AB}$. What is the length of $\overline{EF}$?",
 r"$AB=20$. Triangles $AFE$ and $ACB$ are similar (shared angle $A$, right angles at $F$ and $C$), with hypotenuses $AE$ and $AB$. So $\dfrac{EF}{BC}=\dfrac{AE}{AB}$: $EF=12\cdot\dfrac{10}{20}=6$.",
 r"Students match $AE$ with the leg $AC$ ($EF=12\cdot\tfrac{10}{16}=7.5$) or give $AF=8$.",
 opts=[r"$6$",r"$7.5$",r"$8$",r"$12.5$"],correct=0)
add("GT-238",AV,"Medium",NC,
 r"A triangle has two sides of lengths $10$ and $12$, and the angle between them measures $150^\circ$. What is the area of the triangle?",
 r"The height to the side of length $10$ is $12\sin150^\circ=12\cdot\tfrac12=6$ (it falls outside the triangle). Area $=\tfrac12\cdot10\cdot6=30$.",
 r"Students use $\sin60^\circ$ or treat the triangle as right ($\tfrac12\cdot10\cdot12=60$).",
 opts=[r"$15$",r"$30$",r"$30\sqrt3$",r"$60$"],correct=1)
add("GT-239",AV,"Hard",NC,
 r"A rhombus has side length $13$ and area $120$. What is the sum of the lengths of its diagonals?",
 r"Area $=\tfrac12d_1d_2=120\Rightarrow d_1d_2=240$. Half-diagonals and a side form a right triangle: $d_1^2+d_2^2=4(13^2)=676$. $(d_1+d_2)^2=676+480=1156$, so $d_1+d_2=34$ (diagonals $24$ and $10$).",
 r"Students forget the $\tfrac12$ in the area formula or answer $2\cdot13=26$.",ans=r"$34$")
add("GT-240",AV,"Hard",NC,
 r"A right circular cone stands with its vertex pointing up. Its base radius is $6$ and its height is $12$. Water fills the cone to a depth of $6$, measured from the base. What is the volume of the water?",
 r"The empty top part is a cone similar to the whole with scale $\tfrac12$, so its volume is $\tfrac18$ of the cone. Cone volume $=\tfrac13\pi(36)(12)=144\pi$. Water $=\tfrac78\cdot144\pi=126\pi$.",
 r"Students take the water as the small cone ($18\pi$) or halve the volume ($72\pi$).",
 opts=[r"$18\pi$",r"$72\pi$",r"$108\pi$",r"$126\pi$"],correct=3)
add("GT-241",AV,"Hard",NC,
 r"A sector of a circle has radius $10$ and central angle $216^\circ$. The sector is rolled into a right circular cone so that its two straight edges meet. The volume of the cone is $k\pi$. What is the value of $k$?",
 r"Arc length $=10\cdot\dfrac{216}{360}\cdot2\pi=12\pi$, which is the base circumference, so $r=6$. The sector radius is the slant height: $h=\sqrt{10^2-6^2}=8$. $V=\tfrac13\pi(36)(8)=96\pi$.",
 r"Students use $10$ as the cone's radius or height.",ans=r"$96$")
add("GT-242",RT,"Hard",NC,
 r"Line $\ell$ passes through $(0,0)$ and $(a,12)$, where $a>0$. The acute angle between $\ell$ and the positive $y$-axis measures $60^\circ$. What is the value of $a$?",
 r"The angle with the positive $x$-axis is $90^\circ-60^\circ=30^\circ$, so $\tan30^\circ=\dfrac{12}{a}$ and $a=\dfrac{12}{1/\sqrt3}=12\sqrt3$.",
 r"Students use $60^\circ$ as the angle with the $x$-axis and get $a=4\sqrt3$.",
 opts=[r"$4\sqrt3$",r"$12\sqrt3$",r"$6$",r"$24$"],correct=1)
add("GT-243",LAT,"Hard",NC,
 r"In triangles $PQR$ and $XYZ$, $PQ=XY=9$ and $m\angle R=m\angle Z=35^\circ$, where $\overline{PQ}$ is opposite angle $R$ and $\overline{XY}$ is opposite angle $Z$. Which additional fact is enough to prove that triangle $PQR$ is congruent to triangle $XYZ$?",
 r"With $\angle Q=\angle Y$, the triangles have two angles and a non-included side equal (AAS). Choices with one more side give SSA, which can fit two different triangles (for $QR=14$ there are two triangles, with $PR\approx15.5$ or $PR\approx7.4$). $PR=QR$ is about one triangle only.",
 r"Students accept side-side-angle as a congruence test.",
 opts=[r"$QR=YZ=14$",r"$PR=XZ$",r"$m\angle Q=m\angle Y$",r"$PR=QR$"],correct=2)
add("GT-244",AV,"Hard",NC,
 r"A square has one side on the diameter of a semicircle of radius $10$, and its other two vertices lie on the arc. What is the area of the square?",
 r"Let the side be $s$. A top vertex is $\tfrac s2$ from the centre horizontally and $s$ up, so $s^2+\left(\tfrac s2\right)^2=100$, $\tfrac54s^2=100$, $s^2=80$.",
 r"Students use the full-circle result (area $2r^2=200$) or half of it.",
 opts=[r"$50$",r"$80$",r"$100$",r"$200$"],correct=1)
add("GT-245",CI,"Medium",NC,
 r"In the $xy$-plane, the endpoints of a diameter of a circle are $(-2,3)$ and $(6,-1)$. Which equation represents the circle?",
 r"Centre $(2,1)$, $r^2=(6-2)^2+(-1-1)^2=20$. $(x-2)^2+(y-1)^2=20\Rightarrow x^2+y^2-4x-2y+5=20\Rightarrow x^2+y^2-4x-2y-15=0$.",
 r"Students use the diameter squared ($80$) as $r^2$ or drop the constants $4+1$ when expanding.",
 opts=[r"$x^2+y^2-4x-2y-15=0$",r"$x^2+y^2+4x+2y-15=0$",r"$x^2+y^2-4x-2y-75=0$",r"$x^2+y^2-4x-2y-20=0$"],correct=0)
add("GT-246",LAT,"Hard",NC,
 r"Triangle $ABC$ has area $60$. Point $D$ lies on $\overline{BC}$ with $BD:DC=2:3$, and point $E$ lies on $\overline{AD}$ with $AE:ED=3:1$. What is the area of triangle $BED$?",
 r"Triangles $ABD$ and $ABC$ share the height from $A$: area $ABD=\tfrac25\cdot60=24$. Triangles $BED$ and $BAD$ share the height from $B$: area $BED=\tfrac14\cdot24=6$.",
 r"Students use the wrong part of a ratio ($\tfrac34$ instead of $\tfrac14$, or $\tfrac23$ instead of $\tfrac25$).",
 opts=[r"$6$",r"$10$",r"$15$",r"$18$"],correct=0)
add("GT-247",CI,"Hard",NC,
 r"In a circle of radius $13$, two parallel chords have lengths $24$ and $10$. Which of the following could be the distance between the two chords?",
 r"Distances from the centre: $\sqrt{169-144}=5$ and $\sqrt{169-25}=12$. Same side of the centre: $12-5=7$; opposite sides: $12+5=17$. Only $17$ is offered.",
 r"Students picture only one case, or add the half-chord lengths.",
 opts=[r"$5$",r"$12$",r"$17$",r"$26$"],correct=2)
add("GT-248",AV,"Medium",CA,
 r"The radius of a right circular cylinder is increased by $20\%$ and its height is decreased by $25\%$. What is the effect on the volume of the cylinder?",
 r"$V$ scales by $(1.2)^2(0.75)=1.08$: an increase of $8\%$.",
 r"Students add percents ($20-25=-5$) or forget to square the radius factor.",
 opts=[r"It decreases by $5\%$.",r"It does not change.",r"It increases by $8\%$.",r"It increases by $19\%$."],correct=2)
assert math.isclose(1.2**2*0.75,1.08)
add("GT-249",AV,"Hard",NC,
 r"Sphere $Q$ has volume $36\pi$. Sphere $P$ has a radius $7$ times the radius of sphere $Q$. The spheres are externally tangent at point $T$. Segment $\overline{MT}$ is a diameter of sphere $P$ and segment $\overline{TN}$ is a diameter of sphere $Q$, with $M$, $T$ and $N$ on one line. What is the length of $\overline{MN}$?",
 r"$\tfrac43\pi r^3=36\pi\Rightarrow r^3=27$, $r=3$. Sphere $P$ has radius $21$. $MN=2(21)+2(3)=48$.",
 r"Students add the radii ($24$) or solve $r^2=27$.",
 opts=[r"$24$",r"$45$",r"$48$",r"$66$"],correct=2)
add("GT-250",RT,"Hard",DE,
 r"In the equation $\sin\left(\dfrac{39\pi}{p}\right)=\dfrac{\sqrt3}{2}$, $p$ is a constant and $p>60$. What is the value of $p$?",
 r"$p>60$ means $0<\dfrac{39\pi}{p}<\dfrac{39\pi}{60}=0.65\pi$. The only angle in this interval with sine $\dfrac{\sqrt3}2$ is $\dfrac\pi3$ (the next, $\dfrac{2\pi}3$, gives $p=58.5$). So $\dfrac{39}{p}=\dfrac13$, $p=117$.",
 r"Students take $\dfrac{2\pi}{3}$ and get $58.5$, ignoring the condition, or work in degrees.",ans=r"$117$")
assert math.isclose(math.sin(39*math.pi/117),math.sqrt(3)/2)
add("GT-251",CI,"Hard",NC,
 r"A rectangle is inscribed in a circle with area $676\pi$. The length of the rectangle's diagonal is twice the length of its shorter side. What is the perimeter of the rectangle?",
 r"$r=26$, so the diagonal (a diameter) is $52$ and the short side is $26$. The diagonal is twice the short side, so the triangle is $30^\circ$–$60^\circ$–$90^\circ$ and the long side is $26\sqrt3$. Perimeter $=52+52\sqrt3$.",
 r"Students assume a square, or use the radius as the diagonal.",
 opts=[r"$26+26\sqrt3$",r"$52+52\sqrt3$",r"$104$",r"$104+52\sqrt3$"],correct=1)
add("GT-252",AV,"Hard",NC,
 r"Two identical right rectangular prisms each have a square base with side length $s$ and a height of $35$. Each prism has surface area $K$. The prisms are glued together base to base, and the new solid has surface area $\dfrac{15}{8}K$. What is the value of $s$?",
 r"$K=2s^2+140s$. Gluing hides one base on each prism: new area $=2K-2s^2$. So $2K-2s^2=\tfrac{15}8K\Rightarrow\tfrac18K=2s^2\Rightarrow K=16s^2$. Then $2s^2+140s=16s^2\Rightarrow s=10$.",
 r"Students subtract the glued face once, or set the new area to $2K$.",ans=r"$10$")
s=10;K=2*s*s+140*s;assert 2*K-2*s*s==Fr(15,8)*K
add("GT-253",AV,"Hard",CA,
 r"Square pyramids $X$ and $Y$ have the same base, a square with side length $10$. Pyramid $X$ has height $12$ and pyramid $Y$ has height $24$. The total surface area of $Y$ is approximately what percent greater than the total surface area of $X$?",
 r"Slant heights: $X$: $\sqrt{12^2+5^2}=13$; $Y$: $\sqrt{24^2+5^2}=\sqrt{601}\approx24.52$. Areas: $X=100+20(13)=360$; $Y=100+20(24.52)\approx590.3$. $\dfrac{590.3}{360}\approx1.64$: about $64\%$ greater.",
 r"Students expect doubling ($100\%$), use the height as the slant height, or compare lateral areas only ($89\%$).",
 opts=[r"$50\%$",r"$64\%$",r"$89\%$",r"$100\%$"],correct=1)
assert round((100+20*math.sqrt(601))/360-1,2)==0.64
add("GT-254",LAT,"Hard",NC,
 r"In triangle $ABC$, the measure of angle $A$ is $18^\circ$. Which additional fact is NOT sufficient to determine the measure of angle $B$?",
 r"If the triangle is isosceles, angle $A$ could be a base angle or the vertex angle, so $B$ could be $18^\circ$, $81^\circ$ or $144^\circ$. Each other fact fixes $B$: $B+3B=162\Rightarrow B=40.5^\circ$; $B=C\Rightarrow B=81^\circ$; $C=90^\circ\Rightarrow B=72^\circ$.",
 r"Students think ``isosceles'' fixes the angles and stop at the first case.",
 opts=[r"$m\angle C=3\,m\angle B$",r"Triangle $ABC$ is isosceles.",r"$m\angle B=m\angle C$",r"$m\angle C=90^\circ$"],correct=1)
add("GT-255",CI,"Hard",CA,
 r"Model Earth as a sphere with radius $6{,}371$ kilometers. An observer's eye is $1$ kilometer above the surface. The line of sight from the eye to the horizon is tangent to Earth. Which is closest to the distance, in kilometers, from the eye to the point where the line of sight touches Earth?",
 r"The radius to the point of tangency is perpendicular to the line of sight: $d=\sqrt{6{,}372^2-6{,}371^2}=\sqrt{12{,}743}\approx112.9$.",
 r"Students compute $\sqrt{Rh}\approx79.8$ (dropping the factor $2$ in $2Rh$) or do not see the right triangle.",
 opts=[r"$1.0$",r"$79.8$",r"$112.9$",r"$6{,}371.0$"],correct=2)
assert round(math.sqrt(6372**2-6371**2),1)==112.9
add("GT-256",LAT,"Hard",NC,
 r"Parallel lines $m$ and $n$ are cut by a transversal. Angles $b$ and $c$ are same-side interior angles, and angle $a$ is one of the other angles formed. If $200<a+b+c<236$, where all measures are in degrees, which of the following could be the measure of angle $a$, in degrees?",
 r"Same-side interior angles are supplementary: $b+c=180$. So $200<a+180<236$, giving $20<a<56$. Only $40$ works ($56$ is excluded by the strict inequality; $18$ and $64$ are outside).",
 r"Students include an endpoint or do not use $b+c=180$.",
 opts=[r"$18$",r"$40$",r"$56$",r"$64$"],correct=1)
add("GT-257",RT,"Hard",NC,
 r"In triangle $JKL$, the measure of angle $J$ is $(ab)^\circ$ and the measure of angle $K$ is $(cd)^\circ$, where $ab+cd=90$. If $\sin J=0.6$, what is the value of $\tan K$?",
 r"$J+K=90^\circ$, so angle $L=90^\circ$ and $J$, $K$ are complementary: $\cos K=\sin J=0.6$, $\sin K=0.8$, $\tan K=\dfrac{0.8}{0.6}=\dfrac43$.",
 r"Students decide there is not enough information because $a,b,c,d$ are unknown.",
 opts=[r"$\dfrac34$",r"$\dfrac43$",r"$\dfrac45$",r"The value cannot be determined from the information given."],correct=1)

# ======================= PSDA (PS-157 to PS-175) =======================
add("PS-157",OV,"Hard",NC,
 r"Data sets $A$ and $B$ each contain $20$ values, all from the list $10,20,30,40,50$. The frequencies in $A$ are $2,3,10,3,2$ and the frequencies in $B$ are $5,3,4,3,5$, in that order. Which statement is true?",
 r"Both sets have mean $30$ and range $40$. $B$ has more values at the extremes ($10$ and $50$) and fewer at the mean, so its values are farther from the mean on average: SD of $B$ ($\approx15.2$) is greater than SD of $A$ ($\approx10.5$).",
 r"Students think equal means and ranges force equal standard deviations.",
 opts=[r"The standard deviation of $A$ is greater.",r"The standard deviation of $B$ is greater.",r"The standard deviations are equal because the means and ranges are equal.",r"The standard deviations cannot be compared without calculating them."],correct=1)
def sd(v,f):
    n=sum(f);mu=sum(a*b for a,b in zip(v,f))/n
    return math.sqrt(sum(b*(a-mu)**2 for a,b in zip(v,f))/n)
assert sd([10,20,30,40,50],[5,3,4,3,5])>sd([10,20,30,40,50],[2,3,10,3,2])
add("PS-158",OV,"Medium",NC,
 r"The daily high temperatures in a city for one week have a mean of $34^\circ\text{C}$ and a standard deviation of $4^\circ\text{C}$. Each temperature is converted to degrees Fahrenheit using $F=1.8C+32$. What is the standard deviation of the converted temperatures, in degrees Fahrenheit?",
 r"Multiplying every value by $1.8$ multiplies the SD by $1.8$; adding $32$ shifts the values but does not change the spread. SD $=1.8\cdot4=7.2$.",
 r"Students apply the full conversion ($1.8\cdot4+32=39.2$) or think the SD does not change.",ans=r"$7.2$")
add("PS-159",OV,"Hard",NC,
 r"The data set $12,15,19,24,30$ has a range of $18$. A sixth value, $x$, is added, and the range of the new data set is $1.5$ times the original range. What is the sum of all possible values of $x$?",
 r"New range $=27$. Either $x$ is the new maximum: $x-12=27$, $x=39$; or the new minimum: $30-x=27$, $x=3$. Sum $=42$.",
 r"Students assume the new value is the maximum and answer $39$.",ans=r"$42$")
add("PS-160",OV,"Hard",NC,
 r"The data set $2,6,9,15,x$ has a mean equal to its median, where $x$ is a real number. What is the sum of all possible values of $x$?",
 r"Mean $=\dfrac{32+x}5$. If $x\le6$, median $6$: $x=-2$ ✓. If $6\le x\le9$, median $x$: $32+x=5x$, $x=8$ ✓. If $x\ge9$, median $9$: $x=13$ ✓. Sum $=-2+8+13=19$.",
 r"Students assume $x$ is the median, or reject the negative value.",ans=r"$19$")
import statistics as st
for x in(-2,8,13): assert st.mean([2,6,9,15,x])==st.median([2,6,9,15,x])
add("PS-161",OV,"Hard",NC,
 r"A data set contains the values $1,2,3,4,5$ with frequencies $4,k,6,3,5$, respectively, where $k$ is a positive integer. The median of the data set is $3$. What is the greatest possible value of $k$?",
 r"There are $18+k$ values, and $4+k$ of them are at most $2$. For $k=9$: $27$ values, the $14$th is $3$ ✓. For $k=10$: $28$ values, the $14$th is $2$ and the $15$th is $3$, so the median is $2.5$. Greatest $k=9$.",
 r"Students ignore that the total changes with $k$, or forget that an even count averages the two middle values.",ans=r"$9$")
def med(k):
    d=[1]*4+[2]*k+[3]*6+[4]*3+[5]*5;return st.median(d)
assert med(9)==3 and med(10)==2.5 and max(k for k in range(1,40) if med(k)==3)==9
add("PS-162",OV,"Hard",NC,
 r"The commute times, in whole minutes, of $20$ students are grouped: $10$ students took $0$ to $9$ minutes, $7$ took $10$ to $19$ minutes, and $3$ took $20$ to $29$ minutes. Which of the following could NOT be the median commute time?",
 r"The median is the mean of the $10$th and $11$th values. The $10$th is in $0$–$9$ and the $11$th is in $10$–$19$, so the median is between $\tfrac{0+10}2=5$ and $\tfrac{9+19}2=14$. $4$ is impossible; $7.5$, $10$ and $14$ are possible.",
 r"Students think the median must lie inside one bin, or that it cannot be bounded at all.",
 opts=[r"$4$",r"$7.5$",r"$10$",r"$14$"],correct=0)
add("PS-163",OV,"Hard",NC,
 r"Data set $A$ has $11$ values with median $40$. Data set $B$ has $11$ values with median $52$. The two data sets are combined. Which of the following could be the median of the combined $22$ values?",
 r"At most $5$ values of $A$ and at most $5$ values of $B$ are less than $40$, so at most $10$ combined values are below $40$ and the $11$th value is at least $40$. Likewise at most $10$ combined values are greater than $52$, so the $12$th value is at most $52$. The median lies between $40$ and $52$; only $46$ is in this range.",
 r"Students think nothing can be said, or believe the median must equal the average of the two medians.",
 opts=[r"$38$",r"$46$",r"$54$",r"$60$"],correct=1)
add("PS-164",PC,"Hard",CA,
 r"Electric vehicles made up $4\%$ of a country's new-car sales in one year and $6\%$ the next year. Total new-car sales increased by $10\%$ from the first year to the second. By what percent did the number of electric vehicles sold increase?",
 r"Let first-year sales be $100$: EVs $=4$. Second year: $110$ cars, EVs $=0.06(110)=6.6$. Increase $=\dfrac{2.6}{4}=65\%$.",
 r"Students answer $2$ (percentage points) or $50$ (ignoring the change in total sales).",
 opts=[r"$2\%$",r"$50\%$",r"$60\%$",r"$65\%$"],correct=3)
assert math.isclose(0.06*110/4,1.65)
add("PS-165",PC,"Hard",NC,
 r"The number $a$ is $150\%$ more than the number $b$, and $b$ is $60\%$ less than the positive number $c$. The number $a$ is what percent of $c$?",
 r"$a=2.5b$ and $b=0.4c$, so $a=c$: $100\%$.",
 r"Students read ``$150\%$ more than'' as $1.5b$, giving $60\%$.",ans=r"$100$")
add("PS-166",RR,"Hard",CA,
 r"District $A$ has $120{,}000$ residents and a population density of $4{,}000$ residents per square kilometer. District $B$ has $60{,}000$ residents and a population density of $1{,}500$ residents per square kilometer. Which is closest to the population density, in residents per square kilometer, of the two districts combined?",
 r"Areas: $\tfrac{120{,}000}{4{,}000}=30$ and $\tfrac{60{,}000}{1{,}500}=40$ km². Combined density $=\tfrac{180{,}000}{70}\approx2{,}571$.",
 r"Students average the densities ($2{,}750$) or weight them by population ($\approx3{,}167$).",
 opts=[r"$2{,}571$",r"$2{,}750$",r"$3{,}167$",r"$5{,}500$"],correct=0)
add("PS-167",PC,"Hard",CA,
 r"Bottle $B$ holds $20\%$ more juice than bottle $A$ and costs $15\%$ more. To the nearest tenth of a percent, by what percent is the price per liter of bottle $B$ less than the price per liter of bottle $A$?",
 r"Price per liter of $B$ relative to $A$: $\dfrac{1.15}{1.20}\approx0.9583$. It is about $4.2\%$ less.",
 r"Students subtract the percents and answer $5$.",ans=r"$4.2$")
assert round((1-1.15/1.2)*100,1)==4.2
add("PS-168",PR,"Hard",NC,
 r"In a school, a student is chosen at random. The probability that the student is in grade $10$, given that the student is in the robotics club, is $\dfrac38$. The probability that the student is in the robotics club, given that the student is in grade $10$, is $\dfrac14$. There are $96$ grade $10$ students. How many robotics club members are NOT in grade $10$?",
 r"Grade $10$ robotics members $=\tfrac14\cdot96=24$. These are $\tfrac38$ of the club, so the club has $\tfrac{24}{3/8}=64$ members. Not in grade $10$: $64-24=40$.",
 r"Students use the same denominator for both conditional probabilities.",ans=r"$40$")
add("PS-169",PR,"Hard",NC,
 r"In grade $10$, $12$ students are in a club and $28$ are not. In grade $11$, $k$ students are in the club and $42$ are not. Being in the club is independent of grade. What is the value of $k$?",
 r"Independence means the proportion in the club is the same in each grade: $\dfrac{12}{40}=\dfrac{k}{k+42}$. $0.3k+12.6=k\Rightarrow k=18$.",
 r"Students set $k=12$ (equal counts) or compare with the wrong total.",ans=r"$18$")
assert Fr(12,40)==Fr(18,60)
add("PS-170",PR,"Hard",NC,
 r"In grade $10$, $18$ students are in the robotics club and $42$ are not. In grade $11$, $30$ students are in the robotics club and $60$ are not. A student is chosen at random from the students who are in grade $10$ OR in the robotics club. What is the probability that the student is in grade $11$?",
 r"The group is all $60$ grade $10$ students plus the $30$ grade $11$ robotics members: $90$ students. Grade $11$ students in it: $30$. Probability $=\dfrac{30}{90}=\dfrac13$.",
 r"Students use only the robotics club ($\tfrac{30}{48}$) or all students ($\tfrac{30}{150}$) as the denominator.",
 opts=[r"$\dfrac{5}{8}$",r"$\dfrac15$",r"$\dfrac13$",r"$\dfrac12$"],correct=2)
add("PS-171",TV,"Hard",NC,
 r"A line of best fit for a data set is $\hat y=2.5x+40$. For the data point with $x=24$, the predicted value of $y$ is $20\%$ less than the actual value. What is the residual for this data point?",
 r"Predicted $=2.5(24)+40=100$. $100=0.8\cdot$actual, so actual $=125$. Residual $=$ actual $-$ predicted $=25$.",
 r"Students take $20\%$ of the predicted value ($20$) or get the sign of the residual wrong.",ans=r"$25$")
add("PS-172",TV,"Hard",NC,
 r"The model $\hat y=4.8x+62$ estimates a town's population $y$, in thousands, where $x$ is the number of decades since $1980$. According to the model, what is the estimated increase in the population, in people, per year?",
 r"$4.8$ thousand per decade $=4{,}800$ people per $10$ years $=480$ people per year.",
 r"Students report $4.8$, $48$ or $4{,}800$ by converting only one of the units.",ans=r"$480$")
add("PS-173",RR,"Medium",NC,
 r"The ratio of grade $9$ students to grade $10$ students in a club is $3:5$, and the ratio of grade $10$ students to grade $11$ students is $4:7$. The club has $201$ students in grades $9$, $10$ and $11$. How many more grade $11$ students than grade $9$ students are in the club?",
 r"Make the grade $10$ terms equal: $12:20$ and $20:35$, so $12:20:35$ (sum $67$). $201\div67=3$: $36$, $60$ and $105$. Difference $=105-36=69$.",
 r"Students write $3:5:7$ (sum $15$) and divide $201$ by $15$.",ans=r"$69$")
add("PS-174",TV,"Hard",NC,
 r"A line of best fit for a data set is $\hat y=2.4x+15$. A new data set is formed by adding $5$ to every $x$-value and keeping each $y$-value. What is the $y$-intercept of the line of best fit for the new data set?",
 r"Shifting every $x$ right by $5$ shifts the line right by $5$: $\hat y=2.4(x-5)+15=2.4x+3$. Same slope, new intercept $3$.",
 r"Students add $5$ to the intercept ($20$) or change the slope.",ans=r"$3$")
import random
R=random.Random(1);xs=[R.uniform(0,10) for _ in range(30)];ys=[2.4*x+15+R.gauss(0,1) for x in xs]
def fit(X,Y):
    n=len(X);mx=sum(X)/n;my=sum(Y)/n;s=sum((a-mx)*(b-my) for a,b in zip(X,Y))/sum((a-mx)**2 for a in X);return s,my-s*mx
s1,b1=fit(xs,ys);s2,b2=fit([x+5 for x in xs],ys);assert math.isclose(s1,s2) and math.isclose(b2,b1-5*s1)
add("PS-175",OV,"Hard",NC,
 r"Data set $A$ has $10$ integers: $4$ are from $10$ to $19$ and $6$ are from $20$ to $29$. Data set $B$ has $10$ integers: $3$ are from $30$ to $39$ and $7$ are from $40$ to $49$. What is the smallest possible value of (mean of $B$) $-$ (mean of $A$)?",
 r"Make $A$ as large as possible and $B$ as small as possible. Greatest mean of $A=\dfrac{4(19)+6(29)}{10}=25$. Least mean of $B=\dfrac{3(30)+7(40)}{10}=37$. Smallest difference $=12$.",
 r"Students use bin midpoints (difference $21$) or think the means cannot be compared.",ans=r"$12$")
print(len(I),"items OK")
