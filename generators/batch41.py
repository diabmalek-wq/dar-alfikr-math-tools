import math, statistics as st
from fractions import Fraction as Fr
exec(open('/home/claude/cb/batch40.py').read().split("I=[]")[0])  # skill constants
SRC="House-authored from a trick archetype found in the fourth web sweep (21 Oct 2026; admitstudio, themathdoctors, media4math, edisonos, quiz-tree, 1600.io topic lists, satsphere, prepedu, kaptest, nrich, uniontestprep, AP Statistics conventions). Archetype only; no source item, wording or numbers reproduced."
CL="Problem-Solving and Data Analysis — Evaluating statistical claims: Observational studies and experiments"
I=[]
def add(id,skill,diff,tool,q,rat,mis,opts=None,correct=None,ans=None):
    d=dict(id=id,skill=skill,diff=diff,tool=tool,q=q,rat=rat,mis=mis,opts=opts,correct=correct,ans=ans)
    if opts: assert len(set(opts))==4 and 0<=correct<4
    else: assert ans
    I.append(d)

# ======================= ALGEBRA A-336..A-342 =======================
add("A-337",SY,"Hard",NC,
 r"The solution to the system $ax+by=31$ and $bx+ay=19$, where $a$ and $b$ are constants, is $(4,1)$. What is the value of $a^2-b^2$?",
 r"$4a+b=31$ and $a+4b=19$. Adding: $5a+5b=50$, so $a+b=10$. Subtracting: $3a-3b=12$, so $a-b=4$. $a^2-b^2=(a+b)(a-b)=40$ ($a=7$, $b=3$).",
 r"Students report $a+b=10$, $(a-b)^2=16$ or $a^2+b^2=58$.",
 opts=[r"$10$",r"$16$",r"$40$",r"$58$"],correct=2)
assert 4*7+3==31 and 7+12==19
add("A-338",L2,"Hard",NC,
 r"In the $xy$-plane, the graph of $3x-ky=12$, where $k$ is a nonzero constant, has an $x$-intercept equal to its $y$-intercept. What is the value of $k$?",
 r"$x$-intercept: $3x=12$, $x=4$. $y$-intercept: $-ky=12$, $y=-\dfrac{12}{k}$. Set $-\dfrac{12}{k}=4$: $k=-3$.",
 r"Students drop the negative sign in $-ky$ and get $k=3$.",
 opts=[r"$-3$",r"$3$",r"$-4$",r"$4$"],correct=0)
add("A-339",L2,"Hard",NC,
 r"For every real number $m$, the graph of $y=mx+3m-2$ in the $xy$-plane passes through the point $P$. What are the coordinates of $P$?",
 r"Rewrite: $y+2=m(x+3)$. This holds for every $m$ only when $x+3=0$ and $y+2=0$, so $P=(-3,-2)$.",
 r"Students test only $m=0$ and pick $(0,-2)$, or make a sign error.",
 opts=[r"$(-3,-2)$",r"$(3,-2)$",r"$(-2,3)$",r"$(0,-2)$"],correct=0)
for m in(-2,0,5): assert m*(-3)+3*m-2==-2
add("A-340",L2,"Hard",NC,
 r"A cafe sells juice for $4$ dollars each and sandwiches for $7$ dollars each. A customer spends exactly $112$ dollars and buys at least one juice and at least one sandwich. How many different combinations of juices and sandwiches are possible?",
 r"$4x+7y=112$ with $x,y\ge1$ integers. $4x=112-7y$ needs $y$ to be a multiple of $4$: $y=4,x=21$; $y=8,x=14$; $y=12,x=7$ ($y=16$ gives $x=0$, not allowed). $3$ combinations.",
 r"Students include $(28,0)$ or $(0,16)$ (answers $4$ or $5$) or divide $112$ by $4$.",
 opts=[r"$3$",r"$4$",r"$5$",r"$28$"],correct=0)
assert sum(1 for x in range(1,29) for y in range(1,17) if 4*x+7*y==112)==3
add("A-341",LI,"Medium",NC,
 r"Which inequality has the solution set $x\le-3$ or $x\ge11$?",
 r"The centre of $-3$ and $11$ is $4$ and the distance to each is $7$; the solutions lie outside: $|x-4|\ge7$.",
 r"Students reverse the inequality, flip the sign of the centre, or swap centre and distance.",
 opts=[r"$|x-4|\ge7$",r"$|x-4|\le7$",r"$|x+4|\ge7$",r"$|x-7|\ge4$"],correct=0)
assert all((abs(x-4)>=7)==(x<=-3 or x>=11) for x in range(-20,30))
add("A-342",LI,"Hard",NC,
 r"For how many integer values of $k$ does the point $(k,k)$ satisfy both $y\ge2x-5$ and $y>-x+1$?",
 r"$k\ge2k-5\Rightarrow k\le5$. $k>-k+1\Rightarrow k>\tfrac12$. Integers $1,2,3,4,5$: $5$ values.",
 r"Students treat $\ge$ as $>$ (getting $4$) or use only one inequality.",
 opts=[r"$4$",r"$5$",r"$6$",r"Infinitely many"],correct=1)
assert sum(1 for k in range(-50,50) if k>=2*k-5 and k>-k+1)==5

# ======================= ADVANCED MATH AM-322..AM-331 =======================
add("AM-322",NE,"Hard",NC,
 r"In the equation $\dfrac{ax}{x-2}=3+\dfrac{4}{x-2}$, $a$ is a constant. For which values of $a$ does the equation have no solution?",
 r"Multiply by $x-2$: $ax=3(x-2)+4$, so $(a-3)x=-2$. If $a=3$: $0=-2$, no solution. Otherwise $x=\dfrac{-2}{a-3}$, which is extraneous when it equals $2$: $a-3=-1$, $a=2$. So $a=2$ and $a=3$.",
 r"Students find only the coefficient case ($a=3$) and forget the extraneous-root case.",
 opts=[r"$3$ only",r"$2$ only",r"$2$ and $3$ only",r"$3$ and $4$ only"],correct=2)
add("AM-323",NF,"Hard",NC,
 r"The function $f$ is defined by $f(x)=3x^2-5x+2$. Which expression is equivalent to $f(a+1)-f(a)$?",
 r"$f(a+1)=3(a+1)^2-5(a+1)+2=3a^2+a$. $f(a)=3a^2-5a+2$. Difference: $6a-2$.",
 r"Students assume $f(a+1)=f(a)+f(1)$, giving $0$ because $f(1)=0$, or drop the linear term.",
 opts=[r"$0$",r"$6a-2$",r"$6a+3$",r"$6a+8$"],correct=1)
F=lambda x:3*x*x-5*x+2; assert all(F(a+1)-F(a)==6*a-2 for a in range(-5,6))
add("AM-324",NE,"Hard",NC,
 r"For how many integer values of $b$ does the equation $x^2+bx+36=0$ have two distinct integer solutions?",
 r"The roots $p,q$ satisfy $pq=36$ and $b=-(p+q)$. Distinct factor pairs: $(1,36),(2,18),(3,12),(4,9)$ and their negatives, giving $b=\pm37,\pm20,\pm15,\pm13$: $8$ values. $(6,6)$ is a repeated root.",
 r"Students count positive $b$ only ($4$) or include $b=\pm12$ ($10$).",ans=r"$8$")
bs=set()
for p in range(-36,37):
    if p and 36%p==0:
        q=36//p
        if p!=q: bs.add(-(p+q))
assert len(bs)==8
add("AM-325",NE,"Hard",NC,
 r"The equations $x^2-x-12=0$ and $x^2+kx+8=0$ have a common solution, where $k$ is a positive constant. What is the value of $k$?",
 r"$x^2-x-12=(x-4)(x+3)$. Common root $4$: $16+4k+8=0$, $k=-6$ (not positive). Common root $-3$: $9-3k+8=0$, $k=\tfrac{17}{3}$.",
 r"Students test only the first root and answer $-6$, or ignore the condition $k>0$.",
 opts=[r"$-6$",r"$\dfrac{17}{3}$",r"$6$",r"$-\dfrac{17}{3}$"],correct=1)
assert 9-3*Fr(17,3)+8==0
add("AM-326",NE,"Hard",DE,
 r"What is the sum of all distinct real solutions of $x^3-2x^2-15x+36=0$?",
 r"$x^3-2x^2-15x+36=(x-3)^2(x+4)$. The distinct solutions are $3$ and $-4$; sum $=-1$. (Vieta's sum, $2$, counts the double root twice.) Desmos: the graph touches the $x$-axis at $3$ and crosses at $-4$.",
 r"Students use the sum of roots from the coefficients ($2$) without checking for a repeated root.",
 opts=[r"$-1$",r"$2$",r"$7$",r"$-2$"],correct=0)
assert all((x-3)**2*(x+4)==x**3-2*x*x-15*x+36 for x in range(-6,7))
add("AM-327",NE,"Hard",NC,
 r"What is the solution set of the equation $2x^{2/3}-3=15$?",
 r"$x^{2/3}=9\Rightarrow\left(x^{1/3}\right)^2=9\Rightarrow x^{1/3}=\pm3\Rightarrow x=\pm27$. Check: $(-27)^{2/3}=\left((-27)^{1/3}\right)^2=9$.",
 r"Students keep only the positive root, or invert the exponent the wrong way.",
 opts=[r"$\{27\}$",r"$\{-27,27\}$",r"$\{-9^{2/3},9^{2/3}\}$",r"$\{-6,6\}$"],correct=1)
add("AM-328",NF,"Hard",NC,
 r"The functions $f$ and $g$ are defined by $f(x)=7\cdot4^x$ and $g(x)=f(x-1.5)$. For all values of $x$, $g(x)=k\cdot f(x)$, where $k$ is a constant. What is the value of $k$?",
 r"$g(x)=7\cdot4^{x-1.5}=7\cdot4^x\cdot4^{-1.5}=f(x)\cdot\dfrac18$. So $k=\dfrac18$.",
 r"Students shift in the wrong direction ($k=8$) or subtract $1.5$ from the base.",
 opts=[r"$\dfrac18$",r"$8$",r"$\dfrac78$",r"$-6$"],correct=0)
assert math.isclose(4**-1.5,1/8)
add("AM-329",NF,"Hard",NC,
 r"The function $f$ is defined by $f(x)=2(x-1)(x-7)$. For what value of $k$ does the graph of $y=f(x)+k$ have exactly one $x$-intercept?",
 r"The vertex is midway between the zeros, at $x=4$: $f(4)=2(3)(-3)=-18$. Shifting up by $18$ makes the vertex touch the $x$-axis: $k=18$.",
 r"Students answer the minimum value $-18$, or forget the leading coefficient ($9$).",
 opts=[r"$-18$",r"$18$",r"$9$",r"$14$"],correct=1)
assert 16**2-4*2*32==0
add("AM-330",NF,"Hard",NC,
 r"The function $g$ is defined by $g(x)=3^x$. If $g(a)=4$, what is the value of $g(2a-1)$?",
 r"$g(2a-1)=3^{2a-1}=\dfrac{(3^a)^2}{3}=\dfrac{16}{3}$.",
 r"Students apply the input operations to the output ($2\cdot4-1=7$) or compute $4^2-1$.",
 opts=[r"$\dfrac{16}{3}$",r"$7$",r"$15$",r"$\dfrac83$"],correct=0)
a=math.log(4,3); assert math.isclose(3**(2*a-1),16/3)
add("AM-331",EE,"Medium",NC,
 r"If $2a-3b=7$, what is the value of $\dfrac{4^a}{8^b}$?",
 r"$\dfrac{4^a}{8^b}=\dfrac{2^{2a}}{2^{3b}}=2^{2a-3b}=2^7=128$.",
 r"Students answer $7$, or subtract the exponents in the wrong order.",
 opts=[r"$7$",r"$\dfrac{1}{128}$",r"$128$",r"$2^{14}$"],correct=2)

# ======================= GEOMETRY & TRIG GT-258..GT-274 =======================
add("GT-258",RT,"Hard",NC,
 r"Right triangles $PQR$ and $XYZ$ are similar, with $P$, $Q$ and $R$ corresponding to $X$, $Y$ and $Z$, and right angles at $Q$ and $Y$. If $\tan P=\dfrac{8}{15}$ and $XZ=51$, what is the length of $\overline{XY}$?",
 r"$\tan X=\tan P=\dfrac{8}{15}=\dfrac{YZ}{XY}$, so the sides are $8k$, $15k$ and hypotenuse $17k$. $17k=51$, $k=3$, $XY=15k=45$.",
 r"Students give the opposite side ($24$) or multiply the hypotenuse by the tangent ($27.2$) or divide by it ($95.625$).",
 opts=[r"$24$",r"$27.2$",r"$45$",r"$95.625$"],correct=2)
add("GT-259",RT,"Hard",NC,
 r"In triangle $ABC$, $AB=AC=17$ and $BC=16$. What is the value of $\tan B$?",
 r"The altitude from $A$ bisects $\overline{BC}$: half-base $8$, altitude $\sqrt{17^2-8^2}=15$. $\tan B=\dfrac{15}{8}$.",
 r"Students use the whole base, flip the ratio, or give $\sin B$.",
 opts=[r"$\dfrac{8}{15}$",r"$\dfrac{15}{17}$",r"$\dfrac{15}{8}$",r"$\dfrac{16}{17}$"],correct=2)
add("GT-260",RT,"Hard",NC,
 r"A rectangular box has a base that measures $9$ by $12$ and a height of $20$. Let $\theta$ be the angle between a diagonal of the box (from a bottom corner to the opposite top corner) and the base. What is the value of $\tan\theta$?",
 r"The diagonal's projection on the base is the base diagonal, $\sqrt{9^2+12^2}=15$. $\tan\theta=\dfrac{20}{15}=\dfrac43$.",
 r"Students use one base edge ($9$ or $12$) instead of the base diagonal, or flip the ratio.",
 opts=[r"$\dfrac34$",r"$\dfrac43$",r"$\dfrac53$",r"$\dfrac{20}{9}$"],correct=1)
add("GT-261",RT,"Hard",NC,
 r"In right triangle $ABC$, angle $C$ is the right angle and $\cos A=k$. Which expression is equal to $\sin^2A+\sin^2B$?",
 r"$A$ and $B$ are complementary, so $\sin B=\cos A$. $\sin^2A+\sin^2B=\sin^2A+\cos^2A=1$.",
 r"Students think the value depends on $k$ or cannot be found.",
 opts=[r"$2k^2$",r"$1$",r"$2-2k^2$",r"The value cannot be determined from the information given."],correct=1)
add("GT-262",RT,"Hard",NC,
 r"Right triangle $ABC$ has its right angle at $C$, $AC=9$ and $BC=12$. Each leg is lengthened by $3$ and the angle at $C$ stays a right angle. What is $\tan A$ in the new triangle?",
 r"New legs: $AC=12$, $BC=15$. $\tan A=\dfrac{BC}{AC}=\dfrac{15}{12}=\dfrac54$. Adding the same amount to each leg does not keep the triangle similar, so the ratio changes from $\dfrac43$.",
 r"Students assume the trig ratio is unchanged ($\tfrac43$).",
 opts=[r"$\dfrac43$",r"$\dfrac54$",r"$\dfrac45$",r"$\dfrac53$"],correct=1)
add("GT-263",RT,"Hard",NC,
 r"A straight railway track up a hill has a constant grade of $75\%$, meaning it rises $75$ meters for every $100$ meters of horizontal distance. The track is $300$ meters long, measured along the slope. What is the vertical rise of the track, in meters?",
 r"Grade is $\tan\theta=\dfrac34$, so the sides are in ratio $3:4:5$ and $\sin\theta=\dfrac35$. Rise $=300\cdot\dfrac35=180$.",
 r"Students treat the grade as the sine ($300\cdot0.75=225$) or give the horizontal run ($240$).",
 opts=[r"$180$",r"$225$",r"$240$",r"$400$"],correct=0)
add("GT-264",RT,"Hard",NC,
 r"A drone flies $12$ kilometers in a direction $60^\circ$ north of east, then flies $12$ kilometers due west. How far, in kilometers, is the drone from its starting point?",
 r"First leg ends at $(12\cos60^\circ,12\sin60^\circ)=(6,6\sqrt3)$. After moving $12$ west: $(-6,6\sqrt3)$. Distance $=\sqrt{36+108}=12$.",
 r"Students assume the legs are perpendicular ($12\sqrt2$) or add them ($24$).",
 opts=[r"$6\sqrt3$",r"$12$",r"$12\sqrt2$",r"$24$"],correct=1)
assert math.isclose(math.hypot(-6,6*math.sqrt(3)),12)
add("GT-265",RT,"Hard",NC,
 r"In triangle $ABC$, the measure of angle $B$ is $45^\circ$ and the measure of angle $C$ is $30^\circ$. The altitude from $A$ to $\overline{BC}$ has length $6$. What is the length of $\overline{BC}$?",
 r"The altitude meets $\overline{BC}$ at $D$. In the $45^\circ$ triangle, $BD=6$. In the $30^\circ$ triangle, $DC=\dfrac{6}{\tan30^\circ}=6\sqrt3$. $BC=6+6\sqrt3$.",
 r"Students multiply by $\tan30^\circ$ instead of dividing ($6+2\sqrt3$).",
 opts=[r"$6+2\sqrt3$",r"$12$",r"$6+6\sqrt3$",r"$12+6\sqrt2$"],correct=2)
add("GT-266",RT,"Hard",NC,
 r"In the $xy$-plane, the points $A(0,0)$, $B(6,3)$ and $C(4,7)$ are the vertices of a triangle. What is the value of $\tan(\angle CAB)$?",
 r"Slopes: $AB=\tfrac12$, $BC=\dfrac{7-3}{4-6}=-2$; their product is $-1$, so the right angle is at $B$. $AB=\sqrt{45}$, $BC=\sqrt{20}$, $\tan A=\dfrac{BC}{AB}=\sqrt{\dfrac{20}{45}}=\dfrac23$.",
 r"Students give the slope of $\overline{AC}$ ($\tfrac74$) or of $\overline{AB}$ ($\tfrac12$) instead of a ratio of sides.",
 opts=[r"$\dfrac74$",r"$\dfrac12$",r"$\dfrac23$",r"$\dfrac32$"],correct=2)
assert math.isclose(math.tan(math.atan2(7,4)-math.atan2(3,6)),2/3)
add("GT-267",AV,"Medium",NC,
 r"A parallelogram has sides of lengths $12$ and $20$. The cosine of one of its acute angles is $0.8$. What is the area of the parallelogram?",
 r"$\sin\theta=\sqrt{1-0.8^2}=0.6$. Height to the side of length $20$ is $12\cdot0.6=7.2$. Area $=20\cdot7.2=144$.",
 r"Students use the cosine as the height ratio ($192$) or ignore the angle ($240$).",
 opts=[r"$72$",r"$144$",r"$192$",r"$240$"],correct=1)
add("GT-268",RT,"Hard",NC,
 r"From the top of a cliff $45$ meters high, the angles of depression to two boats on opposite sides of the cliff are $30^\circ$ and $45^\circ$. The boats and the base of the cliff are on a straight line. What is the distance, in meters, between the boats?",
 r"Horizontal distances: $\dfrac{45}{\tan30^\circ}=45\sqrt3$ and $\dfrac{45}{\tan45^\circ}=45$. Opposite sides, so add: $45+45\sqrt3$.",
 r"Students subtract the distances (the same-side case) or multiply by $\tan30^\circ$.",
 opts=[r"$45\sqrt3-45$",r"$45+15\sqrt3$",r"$45+45\sqrt3$",r"$45\sqrt3$"],correct=2)
add("GT-269",RT,"Hard",NC,
 r"In a right triangle, the measure of acute angle $A$ is between $45^\circ$ and $90^\circ$. Which of the following is true?",
 r"Above $45^\circ$ the opposite leg is longer than the adjacent leg, so $\cos A<\sin A$, and $\tan A=\dfrac{\sin A}{\cos A}>1>\sin A$. Check $60^\circ$: $0.5<0.866<1.732$.",
 r"Students use the ordering that holds below $45^\circ$ ($\sin A<\cos A$).",
 opts=[r"$\sin A<\cos A<\tan A$",r"$\cos A<\sin A<\tan A$",r"$\tan A<\sin A<\cos A$",r"$\cos A<\tan A<\sin A$"],correct=1)
add("GT-270",LAT,"Hard",NC,
 r"A rectangle has side lengths $6$ and $6\sqrt3$. What is the measure, in degrees, of the acute angle formed by its diagonals?",
 r"Each diagonal makes an angle with the longer side whose tangent is $\dfrac{6}{6\sqrt3}=\dfrac1{\sqrt3}$, so $30^\circ$. The triangle formed by the longer side and the two half-diagonals has base angles $30^\circ$ and apex angle $120^\circ$. The adjacent angle at the centre, facing the shorter side, is $180^\circ-120^\circ=60^\circ$.",
 r"Students give the diagonal-to-side angle ($30^\circ$) or the obtuse angle ($120^\circ$).",ans=r"$60$")
add("GT-271",RT,"Hard",NC,
 r"In the $xy$-plane, line $\ell$ has slope $\dfrac34$ and line $k$ is perpendicular to line $\ell$. Line $k$ makes an angle $\theta$ with the positive $x$-axis, measured counterclockwise, where $0^\circ<\theta<180^\circ$. What is the value of $\cos\theta$?",
 r"Slope of $k$: $-\dfrac43$, so $\theta$ is obtuse with direction $(-3,4)$ (length $5$). $\cos\theta=-\dfrac35$.",
 r"Students drop the negative sign or use the sine ($\tfrac45$).",
 opts=[r"$\dfrac35$",r"$-\dfrac35$",r"$-\dfrac45$",r"$\dfrac45$"],correct=1)
assert math.isclose(math.cos(math.pi-math.atan(4/3)),-0.6)
add("GT-272",LAT,"Hard",NC,
 r"Parallel lines $\ell$ and $m$ are horizontal, with $\ell$ above $m$. Point $P$ lies between the lines. Point $A$ on $\ell$ and point $B$ on $m$ are both to the right of $P$. Segment $\overline{PA}$ makes a $38^\circ$ angle with line $\ell$, and segment $\overline{PB}$ makes a $47^\circ$ angle with line $m$, both angles opening toward $P$. What is the measure, in degrees, of angle $APB$?",
 r"Draw a line through $P$ parallel to $\ell$ and $m$. Alternate interior angles give $38^\circ$ above it and $47^\circ$ below it, so $\angle APB=38^\circ+47^\circ=85^\circ$.",
 r"Students compute $180-(38+47)=95$ or the difference $9$.",
 opts=[r"$9$",r"$42.5$",r"$85$",r"$95$"],correct=2)
add("GT-273",LAT,"Hard",NC,
 r"In triangle $ABC$, the measure of angle $A$ is $52^\circ$. The bisectors of angles $B$ and $C$ intersect at point $I$. What is the measure, in degrees, of angle $BIC$?",
 r"$B+C=128^\circ$, so $\tfrac B2+\tfrac C2=64^\circ$ and $\angle BIC=180^\circ-64^\circ=116^\circ$.",
 r"Students compute $180-52=128$, or $2\cdot52=104$, or stop at $64$.",
 opts=[r"$64$",r"$104$",r"$116$",r"$128$"],correct=2)
add("GT-274",LAT,"Medium",NC,
 r"In triangle $ABC$, $AB=2x+1$, $BC=x+6$ and $CA=3x-4$. The perimeter of the triangle is $45$. Which angle of the triangle has the greatest measure?",
 r"$6x+3=45\Rightarrow x=7$: $AB=15$, $BC=13$, $CA=17$. The greatest angle is opposite the longest side $\overline{CA}$, which is angle $B$.",
 r"Students name a vertex of the longest side ($A$ or $C$) instead of the opposite angle.",
 opts=[r"Angle $A$",r"Angle $B$",r"Angle $C$",r"It cannot be determined from the information given."],correct=1)

# ======================= PSDA PS-176..PS-210 =======================
add("PS-176",PC,"Hard",NC,
 r"If $18\%$ of $a$ is $24$, what is $a\%$ of $18$?",
 r"$a\%$ of $18=\dfrac{a\cdot18}{100}=18\%$ of $a=24$. No need to find $a$.",
 r"Students solve for $a$ ($133\tfrac13$) and stop, or multiply $0.18\cdot24$.",
 opts=[r"$4.32$",r"$24$",r"$133\tfrac13$",r"$2{,}400$"],correct=1)
add("PS-177",PC,"Medium",CA,
 r"The monthly rent of an apartment increased by $60\%$. By what percent must the new rent decrease to return to the original rent?",
 r"New rent $=1.6R$. Decrease needed: $\dfrac{0.6R}{1.6R}=0.375=37.5\%$.",
 r"Students reuse $60\%$ or compute $100-60=40$.",
 opts=[r"$60\%$",r"$40\%$",r"$37.5\%$",r"$62.5\%$"],correct=2)
add("PS-178",PC,"Hard",CA,
 r"A store's profit on each jacket is $37.5\%$ of the selling price. The profit is what percent of the cost of the jacket to the store?",
 r"Let the price be $100$: profit $37.5$, cost $62.5$. $\dfrac{37.5}{62.5}=0.6=60\%$.",
 r"Students keep the selling price as the base ($37.5\%$) or compute cost as a percent of price ($62.5\%$).",
 opts=[r"$27.3\%$",r"$37.5\%$",r"$60\%$",r"$62.5\%$"],correct=2)
add("PS-179",PC,"Hard",CA,
 r"A restaurant adds a $15\%$ tax and a $10\%$ service charge to a bill. Both are calculated on the original subtotal. The total paid is $250$ dollars. What was the subtotal, in dollars?",
 r"Both percents use the same base, so they add: total $=1.25\cdot$subtotal. Subtotal $=\dfrac{250}{1.25}=200$.",
 r"Students chain the percents ($\tfrac{250}{1.15\cdot1.10}\approx197.63$) or ignore one charge.",
 opts=[r"$187.50$",r"$197.63$",r"$200.00$",r"$217.39$"],correct=2)
add("PS-180",PC,"Hard",NC,
 r"A club has $40$ members, and $30\%$ of the members are girls. How many girls must join the club, with no one leaving, so that girls make up $60\%$ of the members?",
 r"Girls now: $12$. $12+g=0.6(40+g)\Rightarrow0.4g=12\Rightarrow g=30$.",
 r"Students take $60\%$ of the old total ($24-12=12$) and forget the total grows.",
 opts=[r"$12$",r"$20$",r"$28$",r"$30$"],correct=3)
add("PS-181",PC,"Hard",CA,
 r"A worker spends $30\%$ of her monthly salary on rent, then $25\%$ of the remaining amount on food, then $40\%$ of what is left after that on savings. She has $3{,}780$ dollars left. What is her monthly salary, in dollars?",
 r"Remaining fraction: $0.7\cdot0.75\cdot0.6=0.315$. Salary $=\dfrac{3{,}780}{0.315}=12{,}000$.",
 r"Students add the percents ($95\%$ spent) or skip a step.",
 opts=[r"$6{,}300$",r"$7{,}200$",r"$12{,}000$",r"$75{,}600$"],correct=2)
assert math.isclose(3780/(0.7*0.75*0.6),12000)
add("PS-182",PC,"Hard",CA,
 r"Two positive numbers $a$ and $b$ are in the ratio $a:b=9:5$. The number $b$ is what percent less than $a$, to the nearest tenth of a percent?",
 r"$\dfrac{a-b}{a}=\dfrac49\approx44.4\%$.",
 r"Students use $b$ as the base ($80\%$, which is how much greater $a$ is) or use the total parts.",
 opts=[r"$28.6\%$",r"$44.4\%$",r"$55.6\%$",r"$80.0\%$"],correct=1)
add("PS-183",PC,"Hard",NC,
 r"The number $y$ is $p\%$ less than the positive number $x$, where $0<p<100$. Which expression is equal to $x$?",
 r"$y=x\left(1-\dfrac{p}{100}\right)=x\cdot\dfrac{100-p}{100}$, so $x=\dfrac{100y}{100-p}$. Check $p=20$, $y=80$: $x=100$.",
 r"Students add $p\%$ back to $y$ (using the wrong base).",
 opts=[r"$y\left(1+\dfrac{p}{100}\right)$",r"$\dfrac{100y}{100-p}$",r"$\dfrac{(100-p)y}{100}$",r"$\dfrac{100y}{100+p}$"],correct=1)
add("PS-184",PC,"Hard",NC,
 r"Fresh dates are $80\%$ water by mass. After drying, the dates are $50\%$ water by mass. How many kilograms of dried dates are produced from $60$ kilograms of fresh dates?",
 r"The non-water part does not change: $0.2\cdot60=12$ kg. After drying it is $50\%$ of the mass: $\dfrac{12}{0.5}=24$ kg.",
 r"Students subtract $30$ percentage points of the mass ($60\cdot0.7=42$) or halve the mass.",
 opts=[r"$12$",r"$24$",r"$30$",r"$42$"],correct=1)
add("PS-185",PC,"Hard",NC,
 r"In a survey, exactly $37.5\%$ of the people answered ``yes,'' exactly $20\%$ answered ``no,'' and the rest were undecided. What is the least possible number of people surveyed?",
 r"$37.5\%=\dfrac38$ and $20\%=\dfrac15$, so the number surveyed must be a multiple of $8$ and of $5$: least is $40$ ($15$ yes, $8$ no, $17$ undecided).",
 r"Students satisfy only one percent ($8$ or $5$).",
 opts=[r"$5$",r"$8$",r"$40$",r"$1{,}000$"],correct=2)
add("PS-186",PC,"Hard",NC,
 r"At a school, $85\%$ of the boys and $60\%$ of the girls passed an exam, and $70\%$ of all the students passed. What percent of the students at the school are boys?",
 r"Let $b$ be the fraction of boys: $0.85b+0.6(1-b)=0.7\Rightarrow0.25b=0.1\Rightarrow b=0.4=40\%$.",
 r"Students assume equal groups ($50\%$) or swap the groups ($60\%$).",
 opts=[r"$25\%$",r"$40\%$",r"$50\%$",r"$60\%$"],correct=1)
add("PS-187",RR,"Medium",CA,
 r"A runner's pace is $6$ minutes $15$ seconds per kilometer. What is the runner's speed, in kilometers per hour?",
 r"$6$ min $15$ s $=6.25$ min. Speed $=\dfrac{60}{6.25}=9.6$ km/h.",
 r"Students read $6$ min $15$ s as $6.15$ min ($\approx9.76$).",
 opts=[r"$0.16$",r"$6.25$",r"$9.6$",r"$9.76$"],correct=2)
add("PS-188",RR,"Hard",NC,
 r"A pipe can fill an empty tank in $6$ hours, and a drain can empty the full tank in $9$ hours. Starting with the tank empty, the pipe and the drain are both open for $4$ hours, and then the drain is closed. How many more hours does it take the pipe to fill the tank?",
 r"Net rate $\dfrac16-\dfrac19=\dfrac1{18}$ tank per hour; after $4$ hours: $\dfrac29$ full. Remaining $\dfrac79$ at $\dfrac16$ per hour: $\dfrac{7/9}{1/6}=\dfrac{14}{3}$ hours ($4$ h $40$ min).",
 r"Students give the total time ($8\tfrac23$ h) or leave the drain open.",
 opts=[r"$2$",r"$\dfrac{14}{3}$",r"$\dfrac{26}{3}$",r"$14$"],correct=1)
assert Fr(7,9)/Fr(1,6)==Fr(14,3)
add("PS-189",RR,"Hard",NC,
 r"A crew of $12$ workers can finish a job in $20$ days. After the crew has worked for $5$ days, $3$ more workers join, all working at the same rate. How many days in total does the job take?",
 r"Total work $=12\cdot20=240$ worker-days. Done in $5$ days: $60$. Remaining $180$ with $15$ workers: $12$ days. Total $5+12=17$.",
 r"Students give only the remaining days ($12$) or assume $15$ workers from the start ($16$).",
 opts=[r"$12$",r"$16$",r"$17$",r"$25$"],correct=2)
add("PS-190",RR,"Hard",NC,
 r"A driver travels from one city to another at an average speed of $60$ kilometers per hour. At what average speed, in kilometers per hour, must the driver return along the same road so that the average speed for the whole round trip is $80$ kilometers per hour?",
 r"Let the distance be $d$. $\dfrac{2d}{d/60+d/v}=80\Rightarrow\dfrac2{80}=\dfrac1{60}+\dfrac1v\Rightarrow\dfrac1v=\dfrac1{120}$, $v=120$.",
 r"Students average the speeds ($100$).",
 opts=[r"$100$",r"$106.7$",r"$120$",r"$160$"],correct=2)
add("PS-191",RR,"Hard",NC,
 r"A printer prints $p$ pages every $m$ seconds. Which expression gives the number of minutes the printer takes to print $n$ pages?",
 r"Seconds per page $=\dfrac mp$; $n$ pages take $\dfrac{mn}{p}$ seconds $=\dfrac{mn}{60p}$ minutes. Check $p=10$, $m=5$, $n=120$: $60$ s $=1$ min.",
 r"Students multiply by $60$ instead of dividing, or invert the rate.",
 opts=[r"$\dfrac{60mn}{p}$",r"$\dfrac{mn}{60p}$",r"$\dfrac{pn}{60m}$",r"$\dfrac{60m}{pn}$"],correct=1)
add("PS-192",RR,"Hard",CA,
 r"A bank sells US dollars at $3.77$ riyals per dollar. It first deducts a $1\%$ commission from the riyals a customer pays. How many US dollars does a customer receive for $5{,}655$ riyals?",
 r"Riyals exchanged: $0.99\cdot5{,}655=5{,}598.45$. Dollars $=\dfrac{5{,}598.45}{3.77}=1{,}485$.",
 r"Students ignore the commission ($1{,}500$), add it, or multiply by the rate.",
 opts=[r"$1{,}485$",r"$1{,}500$",r"$1{,}515$",r"$21{,}319$"],correct=0)
assert round(5655*0.99/3.77,6)==1485
add("PS-193",OV,"Hard",NC,
 r"The data set $3,5,6,8,9,11,12,46$ has one outlier, $46$, which is removed. Which statement about the effect of removing $46$ is true?",
 r"Mean: $12.5\to\dfrac{54}{7}\approx7.71$. Median: $\dfrac{8+9}2=8.5\to8$ (the count changes from $8$ to $7$). Both decrease, and the mean decreases more.",
 r"Students think the median cannot change when an outlier is removed.",
 opts=[r"Only the mean changes.",r"Both the mean and the median decrease, and the mean decreases more.",r"The mean decreases and the median increases.",r"The mean decreases and the median stays the same."],correct=1)
d=[3,5,6,8,9,11,12,46]; assert st.median(d)==8.5 and st.median(d[:-1])==8
add("PS-194",OV,"Hard",NC,
 r"A data set consists of $12,15,18,21,24,27,30,33,36,40$. The value $40$ is mistakenly recorded as $400$. How do the median, the interquartile range (IQR) and the standard deviation of the recorded data compare with those of the correct data?",
 r"Only the maximum changed. The median ($25.5$) and the quartiles ($18$ and $33$) do not involve the maximum, so the median and IQR are unchanged. The standard deviation measures distance from the mean and grows greatly (about $8.8$ to about $113$).",
 r"Students think every statistic changes with an outlier, or that the IQR is affected.",
 opts=[r"The median, IQR and standard deviation are all unchanged.",r"The median and IQR are unchanged, but the standard deviation is greater.",r"Only the median is unchanged.",r"The median is unchanged, but the IQR and standard deviation are greater."],correct=1)
add("PS-195",OV,"Hard",NC,
 r"Section $P$ has $60$ students and section $Q$ has $24$ students. Test-score summaries: Section $P$: minimum $55$, first quartile $68$, median $76$, third quartile $84$, maximum $97$. Section $Q$: minimum $62$, first quartile $77$, median $83$, third quartile $88$, maximum $95$. Which statement must be true?",
 r"In $Q$, at least $75\%$ of the scores are at or above its first quartile, $77$, which is above $P$'s median, $76$. the statement about more students above $84$ cannot be decided (different section sizes; only percents are known); the range of $Q$ ($33$) is less than that of $P$ ($42$); the IQR of $Q$ ($11$) is less than that of $P$ ($16$).",
 r"Students compare counts when only percents are known, or compare ranges by eye.",
 opts=[r"More students in $Q$ than in $P$ scored above $84$.",r"The range of $Q$ is greater than the range of $P$.",r"At least $75\%$ of the students in $Q$ scored above the median of $P$.",r"The IQR of $Q$ is greater than the IQR of $P$."],correct=2)
add("PS-196",OV,"Hard",NC,
 r"At a company, the median monthly salary is $9{,}000$ dollars and the mean monthly salary is $14{,}500$ dollars. Which statement must be true?",
 r"Any employee earning more than $14{,}500$ also earns more than the median $9{,}000$, and at most half of the employees earn more than the median. So no more than half earn more than $14{,}500$.",
 r"Students read the mean as the typical salary, or treat mean minus median as the standard deviation.",
 opts=[r"More than half of the employees earn more than $14{,}500$ dollars.",r"No more than half of the employees earn more than $14{,}500$ dollars.",r"The standard deviation of the salaries is $5{,}500$ dollars.",r"The most common salary is $9{,}000$ dollars."],correct=1)
add("PS-197",OV,"Hard",NC,
 r"In a data set, the values $1$, $2$, $3$, $4$ and $5$ occur with relative frequencies $10\%$, $15\%$, $20\%$, $30\%$ and $25\%$, respectively. What is the median of the data set minus the mean of the data set?",
 r"Cumulative: $10\%,25\%,45\%,75\%$, so the $50\%$ point is at the value $4$: median $=4$. Mean $=0.1+0.3+0.6+1.2+1.25=3.45$. Difference $=0.55$.",
 r"Students think the total count is needed, or take the median of the percents.",ans=r"$0.55$ (or $\tfrac{11}{20}$)")
add("PS-198",OV,"Hard",NC,
 r"A data set has six values. Their deviations from $40$ (value minus $40$) are $-7$, $3$, $12$, $-5$, $x$ and $2$. The mean of the data set is $42$. What is the value whose deviation from $40$ is $x$?",
 r"The deviations from $40$ sum to $6(42-40)=12$, not $0$ (they sum to $0$ only around the mean). $5+x=12$, $x=7$; the value is $47$.",
 r"Students set the deviations' sum to $0$ ($x=-5$, value $35$) or stop at $x=7$.",
 opts=[r"$35$",r"$47$",r"$7$",r"$52$"],correct=1)
add("PS-199",OV,"Hard",NC,
 r"A data set of $30$ values has a mean of $50$ and a standard deviation of $10$. The values $38$ and $62$ are added to the data set. Which statement is true?",
 r"The pair is symmetric about $50$, so the mean stays $50$. Each new value is $12$ from the mean, farther than the typical distance $10$, so the standard deviation increases (to about $10.1$).",
 r"Students assume values inside the range lower the SD, or that a symmetric pair leaves it unchanged.",
 opts=[r"The mean and the standard deviation are both unchanged.",r"The mean is unchanged and the standard deviation decreases.",r"The mean is unchanged and the standard deviation increases.",r"The mean and the standard deviation both increase."],correct=2)
assert math.sqrt((30*100+2*144)/32)>10
add("PS-200",OV,"Medium",NC,
 r"In a data set, a value is called a low outlier if it is less than $Q_1-1.5\cdot\text{IQR}$, where $Q_1$ is the first quartile and IQR is the interquartile range. For a data set, $Q_1=28$ and the third quartile is $40$. What is the greatest integer value that would be a low outlier?",
 r"IQR $=12$; fence $=28-18=10$. A low outlier is strictly less than $10$, so the greatest integer is $9$.",
 r"Students include the boundary ($10$) or forget the factor $1.5$ ($16$).",ans=r"$9$")
add("PS-201",OV,"Hard",NC,
 r"The recorded values of a data set are $18,22,27,30,33,36,41,47,52$. The value $52$ should have been $25$. After the correction, how do the mean and the median change?",
 r"Mean: $34\to31$ (the sum drops by $27$ over $9$ values). Median: $33\to30$, because $25$ moves below the middle and the middle value shifts. Both decrease by $3$.",
 r"Students assume the median is unchanged when one value is corrected.",
 opts=[r"The mean decreases by $3$ and the median is unchanged.",r"The mean and the median both decrease by $3$.",r"The mean decreases by $27$ and the median decreases by $3$.",r"The median decreases and the mean is unchanged."],correct=1)
d=[18,22,27,30,33,36,41,47,52];e=d[:-1]+[25];assert st.mean(d)-st.mean(e)==3 and st.median(d)-st.median(e)==3
add("PS-202",CL,"Hard",NC,
 r"A company randomly selected $200$ of its employees and gave them new office chairs. Their average productivity rose $8\%$ during the next $3$ months. Which conclusion is best supported?",
 r"There was no comparison group without new chairs, so the rise could come from other changes over the same months. Random selection allows generalization, not a causal claim.",
 r"Students think a random sample alone supports cause and effect.",
 opts=[r"The new chairs caused the rise for all employees.",r"The new chairs caused the rise for the $200$ employees only.",r"The rise cannot be attributed to the chairs, because there was no comparison group.",r"The new chairs had no effect on productivity."],correct=2)
add("PS-203",CL,"Hard",NC,
 r"In an experiment, garden plots were randomly assigned to receive $0$, $20$ or $40$ grams of a fertilizer. The plots given $40$ grams had the highest mean yield. Which conclusion is best supported?",
 r"Random assignment supports a causal conclusion, but only within the tested doses and for plots like these.",
 r"Students extrapolate a valid causal result beyond the tested doses.",
 opts=[r"Using $80$ grams would give an even higher yield.",r"For plots like these, increasing the fertilizer from $0$ to $40$ grams caused higher yields.",r"No causal conclusion is possible.",r"Doubling the fertilizer doubles the yield."],correct=1)
add("PS-204",CL,"Hard",NC,
 r"A survey was mailed to $1{,}200$ randomly selected households, and $180$ surveys were returned. Of these, $72\%$ supported a new fee. What is the main reason the $72\%$ may not represent all households?",
 r"Only $15\%$ responded. People who choose to return a survey may differ from those who do not (non-response bias), even though the original selection was random.",
 r"Students think random selection guarantees a representative result.",
 opts=[r"The sample of $1{,}200$ is too small.",r"Many selected households did not respond, and those who responded may differ from those who did not.",r"There was no random assignment to treatments.",r"The households were selected at random."],correct=1)
add("PS-205",CL,"Medium",NC,
 r"An observational study found that children from homes with more books tend to have higher reading scores. Which of the following is the most plausible confounding variable?",
 r"A confounder is related to both variables: parents' education level can affect both the number of books at home and the children's reading scores.",
 r"Students choose a variable linked to only one of the two variables, or a feature of the study design.",
 opts=[r"Parents' education level",r"The number of pages per book",r"The scale used for the reading test",r"The number of children in the study"],correct=0)
add("PS-206",CL,"Medium",NC,
 r"To estimate the average weekly exercise time of adults in a city, a researcher randomly selected $400$ people from the membership lists of the city's gyms. Why is the estimate likely to be biased?",
 r"The sampling frame (gym members) leaves out adults who are not gym members, who probably exercise less. Random selection from a biased list is still biased.",
 r"Students accept random selection without checking the list it came from.",
 opts=[r"The sample size is too small.",r"The list leaves out adults who are not gym members.",r"There was no random assignment.",r"The selection was random, so the estimate is not biased."],correct=1)
add("PS-207",CL,"Medium",NC,
 r"A teacher randomly selected $50$ students and asked each one, face to face, ``Have you ever copied homework?'' Of the students, $6\%$ answered yes. Which is the most likely problem with this result?",
 r"The question is sensitive and asked in person by a teacher, so students may under-report (response bias), even though the sample was random.",
 r"Students check only how the sample was chosen and miss the measurement problem.",
 opts=[r"Students may give untrue answers because the question is sensitive and asked in person.",r"The sample was not selected at random.",r"There was no control group.",r"A sample of $50$ students is too large."],correct=0)
add("PS-208",TV,"Medium",NC,
 r"For a data set, the correlation coefficient between height in centimeters and mass in kilograms is $r=0.72$. The heights are converted to inches, the masses to pounds, and the two variables are swapped between the axes. What is the correlation coefficient for the converted data?",
 r"Correlation has no units and is symmetric: changing units (positive scale factors) and swapping the axes leave $r$ unchanged, $0.72$.",
 r"Students scale $r$ by the conversion factors or take its reciprocal.",
 opts=[r"$0.72$",r"$-0.72$",r"$\dfrac{1}{0.72}$",r"$0.72\cdot\dfrac{2.2}{2.54}$"],correct=0)
add("PS-209",TV,"Hard",NC,
 r"For data set $P$, the line of best fit is $\hat y=4.2x+3$ and the correlation coefficient is $0.41$. For data set $Q$, the line of best fit is $\hat y=0.6x+10$ and the correlation coefficient is $0.93$. Which statement is true?",
 r"The strength of a linear association is measured by $r$, not by the slope. $Q$ has $r$ closer to $1$, so its points fit a line more closely, relative to the spread of the data.",
 r"Students think a steeper slope means a stronger association.",
 opts=[r"$P$ has the stronger linear association because its slope is greater.",r"$Q$ has the stronger linear association.",r"$Q$ has a weaker association because its slope is less than $1$.",r"The associations cannot be compared because the slopes are different."],correct=1)
add("PS-210",TV,"Hard",NC,
 r"A model for a data set is $\hat y=2.5x+10$. The data points are $(2,17)$, $(4,19.5)$, $(6,24)$, $(8,31)$ and $(10,34.5)$. For how many of the data points does the model underestimate the actual value of $y$?",
 r"Residuals (actual $-$ predicted): $17-15=2$, $19.5-20=-0.5$, $24-25=-1$, $31-30=1$, $34.5-35=-0.5$. The model underestimates when the residual is positive: $2$ points.",
 r"Students reverse ``underestimate'' and count the negative residuals ($3$).",
 opts=[r"$1$",r"$2$",r"$3$",r"$5$"],correct=1)
assert sum(1 for x,y in[(2,17),(4,19.5),(6,24),(8,31),(10,34.5)] if y>2.5*x+10)==2
print(len(I),"items OK")
