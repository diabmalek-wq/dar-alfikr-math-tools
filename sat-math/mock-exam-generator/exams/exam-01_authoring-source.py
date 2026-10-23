# Reference only: this is the script that produced exam-01 (items + traps + steps + numeric checks).
# It read the earlier exam (for sess/domain/skill tags) from ../exam.json and wrote exam2.json.
# For a new exam, copy the pattern: one MC()/SPR() call per item, with the key verified in code.
import json, math
from fractions import Fraction as Fr
e=json.load(open('../exam.json'))
orig={x['id']:x for x in e['m1']+e['m2']}
OUT={'m1':[],'m2':[]}
def MC(m,oid,q,key,wrong,pos,steps,newid=None):
    o=orig[oid]; opts=list(wrong); opts.insert(pos,key)
    OUT[m].append(dict(id=(newid or oid)+'T',sess=o['sess'],lv=o['lv'],mc=True,q=q,opts=opts,key=pos,steps=steps,domain=o['domain'],skill=o['skill']))
def SPR(m,oid,q,key,steps,disp=None):
    o=orig[oid]
    d=dict(id=oid+'T',sess=o['sess'],lv=o['lv'],mc=False,q=q,key=float(key),steps=steps,domain=o['domain'],skill=o['skill'])
    if disp: d['disp']=disp
    OUT[m].append(d)
# ---------------- MODULE 1 ----------------
# 1
assert abs(((64**2*math.sqrt(64))**(1/3))/64 - 64**(-1/6))<1e-9
SPR('m1','AM-082',r"If $x>0$ and $\dfrac{\sqrt[3]{x^{2}\sqrt{x}}}{x}=x^{a}$, what is the value of $a$?",-1/6,
 [r"Pick an $x$ that makes every root clean, $x=64$: type <code>(64^2*sqrt(64))^(1/3)/64</code>. It returns $0.5$.",
  r"Type <code>y=64^x</code> and <code>y=0.5</code> ($x$ stands for $a$). Tap the intersection: $x\approx-0.1667$.",
  r"Exact: <code>ln(0.5)/ln(64)</code> returns $-0.1667=-\dfrac16$.",
  r"By exponents: $\dfrac{x^{2/3}\cdot x^{1/6}}{x}=x^{5/6-1}=x^{-1/6}$. Trap: stopping at $\dfrac56$ and forgetting to divide by $x$."],disp=r"-\dfrac{1}{6}")
# 2
MC('m1','AM-142',"$$\\dfrac{9}{x^2-6x+9}=4$$\nWhat is the sum of the squares of all solutions to the equation above?",r"$\dfrac{45}{2}$",[r"$6$",r"$9$",r"$36$"],2,
 [r"Type <code>y=9/(x^2-6x+9)</code> and <code>y=4</code>. Tap both intersections: $x=1.5$ and $x=4.5$.",
  r"Type <code>1.5^2+4.5^2</code>: it returns $22.5=\dfrac{45}{2}$.",
  r"Traps: $6$ is the sum of the solutions, and $36$ is the sum squared, $(1.5+4.5)^2$."])
# 3
SPR('m1','AM-114',"Twice the square of a positive number is $4$ more than $7$ times the number. What is the number?",4,
 [r"Write it: $2x^{2}=7x+4$. Type <code>y=2x^2</code> and <code>y=7x+4</code>.",r"Intersections: $x=-0.5$ and $x=4$. The number must be positive, so $x=4$.",r"Check: $2(16)=32$ and $7(4)+4=32$."])
# 4
assert 6*16==96 and 96/24==4
SPR('m1','AM-092',"The variable $x$ is inversely proportional to $y^{2}$. If $x=6$ when $y=4$, what is the positive value of $y$ when $x=24$?",2,
 [r"Inverse to $y^{2}$ means $xy^{2}=k$. Type <code>6*4^2</code>: $k=96$.",r"Solve $24y^{2}=96$: $y^{2}=4$, so $y=2$ (positive).",r"Trap: using $y$ instead of $y^{2}$ gives $y=1$."])
# 5
h=lambda t:3*t**2-24*t+10; assert h(4)==-38 and h(-4)==154
MC('m1','AM-047',"The function $h$ is defined by $h(x)=3x^{2}-24x+10$. What is the minimum value of $h$?",r"$-38$",[r"$4$",r"$10$",r"$154$"],3,
 [r"Type <code>y=3x^2-24x+10</code>. Tap the lowest point: $(4,\,-38)$.",r"The question asks for the minimum <b>value</b>, the $y$-coordinate: $-38$.",r"Traps: $4$ is the $x$-coordinate of the vertex; $10$ is the $y$-intercept."])
# 6
assert abs(15*5/(2*math.pi)-75/(2*math.pi))<1e-12
MC('m1','GT-054',"Points $X$, $Y$, and $Z$ lie on a circular fountain. The measure of major arc $XZY$ is $4$ times the measure of minor arc $XY$, and minor arc $XY$ has a length of $15$ meters. What is the radius, in meters, of the fountain?",r"$\dfrac{75}{2\pi}$",[r"$75$",r"$\dfrac{75}{\pi}$",r"$\dfrac{15}{2\pi}$"],0,
 [r"The two arcs fill $360^\circ$: $x+4x=360^\circ$, so the minor arc is $72^\circ=\dfrac15$ of the circle.",r"Circumference $=5\cdot15=75$ m.",r"$2\pi r=75$, so $r=\dfrac{75}{2\pi}\approx11.94$. Type <code>75/(2*pi)</code> to confirm.",r"Trap: $75$ is the circumference, not the radius."])
# 7
MC('m1','GT-074',"A sector of a circle with radius $9$ cm has an area of $27\\pi$ cm$^{2}$. What is the length, in cm, of the arc of the sector?",r"$6\pi$",[r"$3\pi$",r"$12\pi$",r"$18\pi$"],0,
 [r"Fraction of the circle: $\dfrac{27\pi}{81\pi}=\dfrac13$.",r"Circumference $=2\pi(9)=18\pi$, so the arc is $\dfrac13\cdot18\pi=6\pi$.",r"Trap: $18\pi$ is the full circumference."])
# 8
MC('m1','AM-025',"If $a$ and $b$ are positive numbers such that $a^{5}=b^{2}$, which of the following is equivalent to $\\dfrac{a^{3}}{b}$?",r"$\sqrt{a}$",[r"$a^{\frac{11}{2}}$",r"$a^{-\frac{1}{2}}$",r"$a^{\frac{5}{2}}$"],2,
 [r"Since $b>0$, $b=a^{5/2}$.",r"$\dfrac{a^{3}}{a^{5/2}}=a^{3-5/2}=a^{1/2}=\sqrt a$.",r"Check with $a=4$: $b=\sqrt{4^{5}}=32$ and $\dfrac{64}{32}=2=\sqrt4$.",r"Trap: adding exponents ($3+\tfrac52=\tfrac{11}{2}$) instead of subtracting."])
# 9
MC('m1','AM-068',"What is the sum of the $y$-coordinates of the solutions to the system below?\n$$y=x^2-2x-3$$\n$$y=x+3$$",r"$9$",[r"$3$",r"$6$",r"$12$"],0,
 [r"Type both equations. The intersections are $(-1.37,\,1.63)$ and $(4.37,\,7.37)$.",r"Add the $y$-values: $1.63+7.37=9$.",r"Algebra: $x^2-3x-6=0$ gives $x_1+x_2=3$, then $y_1+y_2=(x_1+3)+(x_2+3)=3+6=9$.",r"Trap: $3$ is the sum of the $x$-coordinates."])
# 10
MC('m1','AM-042',"For $g(x)=\\dfrac{x+3}{x^{2}-x-12}$, at which value of $x$ does the graph of $g$ have a vertical asymptote?",r"$4$",[r"$-3$",r"$3$",r"$12$"],2,
 [r"Factor: $x^{2}-x-12=(x-4)(x+3)$, so $g(x)=\dfrac{x+3}{(x-4)(x+3)}$.",r"The factor $(x+3)$ cancels: a <b>hole</b> at $x=-3$, not an asymptote.",r"Type <code>y=(x+3)/(x^2-x-12)</code>: the curve shoots up and down only at $x=4$."])
# 11
F=lambda t:t**2+1; G=lambda t:t+3
MC('m1','AM-036',"If $f(x)=x^{2}+1$ and $g(x)=x+3$, for what value of $x$ does $f\\left(g(x)\\right)=g\\left(f(x)\\right)$?",r"$-1$",[r"$1$",r"$-3$",r"$3$"],0,
 [r"Type <code>y=(x+3)^2+1</code> and <code>y=x^2+1+3</code>.",r"They meet at one point: $(-1,\,5)$. So $x=-1$.",r"Algebra: $x^{2}+6x+10=x^{2}+4\Rightarrow 6x=-6$."])
# 12
SPR('m1','AM-122',"$$xy=75$$\n$$y-3x=0$$\nIf $(x,\\,y)$ is a solution to the system above and $x>0$, what is the value of $x+y$?",20,
 [r"Substitute $y=3x$: $3x^{2}=75$, so $x=5$ (positive), $y=15$.",r"Type <code>y=75/x</code> and <code>y=3x</code>: intersection $(5,15)$.",r"Answer $x+y=20$. Trap: reporting $y=15$ or $x=5$ alone."])
# 13
vals={nn**3-nn for nn in range(-50,51)}; assert 30 not in vals and {0,6,24}<=vals
MC('m1','AM-029',"An integer $n$ is subtracted from its cube. Which of the following could NOT be the result?",r"$30$",[r"$0$",r"$6$",r"$24$"],3,
 [r"$n^{3}-n=(n-1)\,n\,(n+1)$, a product of three consecutive integers, so it is always divisible by $6$.",r"$0$ ($n=0$), $6$ ($n=2$) and $24$ ($n=3$) all occur.",r"$30$ looks plausible because $6\mid30$, but $n=3$ gives $24$ and $n=4$ gives $60$. Type <code>y=x^3-x</code> and <code>y=30</code>: no integer $x$ at the intersection."])
# 14
assert 15*36==540 and 540/100==5.4
MC('m1','AM-032',"The variable $y$ varies inversely with the square of $x$. When $x=6$, $y=15$. What is the value of $y$ when $x=10$?",r"$\dfrac{27}{5}$",[r"$9$",r"$25$",r"$\dfrac{125}{3}$"],1,
 [r"$yx^{2}=k$: type <code>15*6^2</code> to get $k=540$.",r"Then $y=\dfrac{540}{10^{2}}=5.4=\dfrac{27}{5}$.",r"Traps: $9=\dfrac{90}{10}$ (plain inverse), $\dfrac{125}{3}=15\left(\dfrac{10}{6}\right)^{2}$ (direct square)."])
# 15
MC('m1','GT-109',"Segment $AC$ is a diameter of a circle, and point $B$ lies on the circle. If $AB=10$ and $BC=24$, what is the area of the circle?",r"$169\pi$",[r"$676\pi$",r"$26\pi$",r"$13\pi$"],2,
 [r"$\angle ABC=90^\circ$ (inscribed in a semicircle), so $AC=\sqrt{10^{2}+24^{2}}=26$. Type <code>sqrt(10^2+24^2)</code>.",r"Radius $=13$, area $=\pi(13)^{2}=169\pi$.",r"Trap: $676\pi$ uses the diameter as the radius."])
# 16
MC('m1','AM-055',"Which expression is equivalent to $3(2x-5)-2(4x-7)$?",r"$-2x-1$",[r"$-2x-29$",r"$14x-29$",r"$-2x+1$"],0,
 [r"Type <code>3(2x-5)-2(4x-7)</code> in one line and <code>y=-2x-1</code> in another; the graphs coincide.",r"Algebra: $6x-15-8x+14=-2x-1$.",r"Trap: $-2x-29$ comes from $-2(-7)=-14$ (sign error)."])
# 17
MC('m1','AM-056',r"Which expression is equivalent to $\left(4x^{2}-3x+8\right)-\left(x^{2}-5x-6\right)-\left(x-2\right)$?".replace('$',''),r"$3x^{2}+x+16$",[r"$3x^{2}-9x$",r"$3x^{2}+x+12$",r"$3x^{2}+x-4$"],1,
 [r"Distribute each minus: $4x^{2}-3x+8-x^{2}+5x+6-x+2$.",r"Combine: $3x^{2}+(-3+5-1)x+(8+6+2)=3x^{2}+x+16$.",r"Trap: not distributing the last minus gives $3x^{2}-9x$."])
OUT['m1'][-1]['q']=r"Which expression is equivalent to $\left(4x^{2}-3x+8\right)-\left(x^{2}-5x-6\right)-\left(x-2\right)$?"
# 18
MC('m1','AM-107',"What is the sum of the squares of the solutions to $2x^{2}-2x-24=0$?",r"$25$",[r"$1$",r"$49$",r"$7$"],3,
 [r"Type <code>y=2x^2-2x-24</code>. It crosses the $x$-axis at $x=-3$ and $x=4$.",r"Squares: $9+16=25$.",r"Traps: $1=-3+4$ (sum of solutions), $49=(3+4)^{2}$, $7=3+4$."])
# 19
MC('m1','GT-073',"A circle in the $xy$-plane is given by $x^{2}+y^{2}+4x-10y-20=0$. What is the radius of the circle?",r"$7$",[r"$49$",r"$2\sqrt5$",r"$\sqrt{29}$"],0,
 [r"Complete the square: $(x^{2}+4x+4)+(y^{2}-10y+25)=20+4+25$.",r"$(x+2)^{2}+(y-5)^{2}=49$, so $r=7$.",r"Traps: $49$ is $r^{2}$; $\sqrt{29}=\sqrt{4+25}$ forgets the $20$."])
# 20
rem=2*(-2)**3+3*(-2)**2-7*(-2)-8; assert rem==2
MC('m1','AM-038',"What is the remainder when $2x^{3}+3x^{2}-7x-8$ is divided by $x+2$?",r"$2$",[r"$6$",r"$-2$",r"$-8$"],0,
 [r"Remainder Theorem: evaluate at $x=-2$ (root of $x+2$). Type <code>2(-2)^3+3(-2)^2-7(-2)-8</code>.",r"It returns $2$.",r"Trap: $6$ is the value at $x=+2$; $-8$ is just the constant term."])
# 21
assert 1.8*-40+32==-40
MC('m1','AM-040',"The function $F$ converts a Celsius temperature $c$ to Fahrenheit: $F(c)=1.8c+32$. For what value of $c$ is $F(c)=c$?",r"$-40$",[r"$-32$",r"$0$",r"$40$"],0,
 [r"Type <code>y=1.8x+32</code> and <code>y=x</code>.",r"Tap the intersection: $(-40,-40)$.",r"Algebra: $1.8c+32=c\Rightarrow0.8c=-32\Rightarrow c=-40$."])
# 22
assert (4-1)**2+16==25
SPR('m1','GT-196',"In the $xy$-plane, the line $x=4$ intersects the circle $(x-1)^2+y^2=25$ at two points. What is the area of the triangle formed by these two points and the center of the circle?",12,
 [r"Substitute $x=4$: $9+y^{2}=25$, so $y=\pm4$. The points are $(4,4)$ and $(4,-4)$.",r"Base $=8$ (distance between them). Height $=$ distance from center $(1,0)$ to the line $x=4$, which is $3$.",r"Area $=\dfrac12\cdot8\cdot3=12$. Trap: answering $8$, the chord length."])
# ---------------- MODULE 2 ----------------
# 1
assert Fr(384)/400==Fr(24,25)
MC('m2','GT-155',"Triangle $ABC$ is inscribed in a circle with circumference $40\\pi$. Side $AC$ has length $40$ and side $AB$ has length $24$. What is the ratio of the area of triangle $ABC$ to the area of the circle?",r"$\dfrac{24}{25\pi}$",[r"$\dfrac{24}{25}$",r"$\dfrac{48}{25\pi}$",r"$\dfrac{12}{25\pi}$"],3,
 [r"$2\pi r=40\pi\Rightarrow r=20$, so $AC=40$ is a diameter and $\angle B=90^\circ$.",r"$BC=\sqrt{40^{2}-24^{2}}=32$. Triangle area $=\dfrac12\cdot24\cdot32=384$.",r"Circle area $=400\pi$. Ratio $=\dfrac{384}{400\pi}=\dfrac{24}{25\pi}$.",r"Trap: dropping the $\pi$ gives $\dfrac{24}{25}$."])
# 2
SPR('m2','AM-118',"If $a>0$ and $a^{-\\frac{3}{4}}=\\dfrac{1}{8}$, what is the value of $a^{\\frac{3}{2}}$?",64,
 [r"Take the reciprocal: $a^{3/4}=8$.",r"Square both sides: $a^{3/2}=8^{2}=64$.",r"Check with Desmos: $a=8^{4/3}=16$; type <code>16^(3/2)</code> returns $64$."])
assert 16**(-0.75)==1/8 and 16**1.5==64
# 3
SPR('m2','AM-102',"If $(x+1)^2=16$ and $(x-5)^2=100$, what is the value of $x$?",-5,
 [r"First equation: $x+1=\pm4$, so $x=3$ or $x=-5$.",r"Second equation: $x-5=\pm10$, so $x=15$ or $x=-5$.",r"The only value in both lists is $x=-5$."])
# 4
g=lambda t:2**t-5*t
from scipy.optimize import minimize_scalar
mn=minimize_scalar(g,bounds=(0,6),method='bounded'); assert -7.1<mn.fun<-7.0
MC('m2','AM-196',"$$2^{x}=5x+k$$\nIn the equation above, $k$ is a constant. What is the smallest integer value of $k$ for which the equation has two distinct real solutions?",r"$-7$",[r"$-8$",r"$-6$",r"$-5$"],1,
 [r"Rewrite as $2^{x}-5x=k$. Type <code>y=2^x-5x</code> and a slider line <code>y=k</code>.",r"The graph has a minimum of about $-7.04$ near $x=2.85$. Two intersections occur only when $k>-7.04$.",r"The smallest integer above $-7.04$ is $-7$. Trap: $-8$ is below the minimum (no solutions)."])
# 5
import numpy as np
r8=8; chord=8*np.sqrt(3); ang=2*np.arcsin(chord/(2*r8)); assert abs(ang-2*np.pi/3)<1e-12
assert abs(0.5*r8**2*(ang-np.sin(ang))-(64*np.pi/3-16*np.sqrt(3)))<1e-9
MC('m2','GT-159',"In a circle with center $O$ and radius $8$, chord $\\overline{AB}$ has length $8\\sqrt3$. What is the area of the region bounded by chord $\\overline{AB}$ and the minor arc $AB$?",r"$\dfrac{64\pi}{3}-16\sqrt3$",[r"$\dfrac{64\pi}{3}-32\sqrt3$",r"$\dfrac{64\pi}{3}+16\sqrt3$",r"$\dfrac{32\pi}{3}-16\sqrt3$"],2,
 [r"Triangle $OAB$ has sides $8,8,8\sqrt3$: by the law of cosines $\cos\angle O=-\tfrac12$, so $\angle AOB=120^\circ$.",r"Sector $=\dfrac13\pi(8)^{2}=\dfrac{64\pi}{3}$. Triangle $=\dfrac12(8)(8)\sin120^\circ=16\sqrt3$.",r"Segment $=$ sector $-$ triangle $=\dfrac{64\pi}{3}-16\sqrt3\approx 28.7$. Type <code>64pi/3-16sqrt(3)</code> to confirm.",r"Trap: using $60^\circ$ gives $\dfrac{32\pi}{3}-16\sqrt3$."])
# 6
MC('m2','AM-054',"A taxi company uses the formula $10p=q+25r$, where $p$ is the fare per passenger, in dollars; $q$ is a fixed service charge, in dollars; and $r$ is the distance traveled, in kilometers. If $q$ is increased by $40$ and $r$ is decreased by $2$, how does $p$ change?",r"It decreases by $1$",[r"It increases by $1$",r"It decreases by $10$",r"It increases by $10$"],0,
 [r"Change in the right side: $+40+25(-2)=-10$.",r"So $10\,\Delta p=-10$, giving $\Delta p=-1$: the fare decreases by $\$1$.",r"Trap: forgetting to divide by $10$ gives a change of $10$."])
# 7
r_=13; AD=13-5; assert AD*26==208 and math.isclose(math.sqrt(208),4*math.sqrt(13))
MC('m2','GT-166',"Segment $\\overline{AB}$ is a diameter of a circle and has length $26$. Point $C$ lies on the circle, and point $D$ lies on $\\overline{AB}$ with $\\overline{CD}\\perp\\overline{AB}$ and $CD=12$. If $AD<DB$, what is the length of $\\overline{AC}$?",r"$4\sqrt{13}$",[r"$6\sqrt{13}$",r"$2\sqrt{39}$",r"$13$"],1,
 [r"Let $O$ be the center. $OC=13$, $CD=12$, so $OD=\sqrt{13^{2}-12^{2}}=5$.",r"$AD<DB$ means $D$ is on $A$'s side: $AD=13-5=8$.",r"$AC=\sqrt{AD^{2}+CD^{2}}=\sqrt{64+144}=\sqrt{208}=4\sqrt{13}$.",r"Trap: $6\sqrt{13}=\sqrt{468}$ is $BC$ (the other leg, $DB=18$)."])
# 8
MC('m2','AM-174',"In the $xy$-plane, the line $y=mx+3$ intersects the parabola $y=x^{2}+2x+7$ at exactly one point, where $m$ is a positive constant. What is the $y$-coordinate of that point?",r"$15$",[r"$2$",r"$6$",r"$11$"],0,
 [r"Set equal: $x^{2}+(2-m)x+4=0$. One solution means the discriminant is $0$: $(2-m)^{2}-16=0$, so $m=6$ (positive) or $m=-2$.",r"With $m=6$: $x^{2}-4x+4=0$, $x=2$.",r"$y=6(2)+3=15$. Check in the parabola: $4+4+7=15$.",r"Traps: $2$ is the $x$-coordinate; $6$ is $m$."])
# 9
assert math.isclose(8*8*math.sqrt(3),64*math.sqrt(3))
MC('m2','GT-170',"In a circle with center $O$, chord $\\overline{AB}$ has $\\angle AOB=120^\\circ$ and lies at a perpendicular distance of $4$ from $O$. The lines tangent to the circle at $A$ and at $B$ intersect at point $P$. What is the area of quadrilateral $OAPB$?",r"$64\sqrt3$",[r"$32\sqrt3$",r"$128\sqrt3$",r"$64$"],0,
 [r"The distance to the chord is $r\cos60^\circ=4$, so $r=8$.",r"Tangent length $PA=r\tan60^\circ=8\sqrt3$. Type <code>8tan(60)</code> in degree mode.",r"$OAPB$ is two right triangles: area $=2\cdot\dfrac12\cdot8\cdot8\sqrt3=64\sqrt3$.",r"Trap: $32\sqrt3$ is only one triangle."])
# 10
MC('m2','AM-066',"The function $g$ is defined by $g(x)=x^{2}+8x+3$. The graph of $g$ is the same as the graph of $y=x^{2}$ after which of the following transformations?",r"Shifted left $4$ and down $13$",[r"Shifted right $4$ and down $13$",r"Shifted left $4$ and down $3$",r"Shifted left $8$ and up $3$"],0,
 [r"Complete the square: $x^{2}+8x+3=(x+4)^{2}-16+3=(x+4)^{2}-13$.",r"$(x+4)$ moves the graph <b>left</b> $4$; $-13$ moves it down $13$.",r"Type <code>y=x^2+8x+3</code>: the vertex is at $(-4,-13)$."])
# 11
assert 26+(-17)==9
SPR('m2','GT-115',"Circle $A$ in the $xy$-plane has equation $x^2+y^2+10x-2y-n=0$, where $n$ is a constant. Circle $B$ has the same center as circle $A$, has three times the diameter of circle $A$, and passes through $(-5,10)$. What is the value of $n$?",-17,
 [r"Complete the square: $(x+5)^{2}+(y-1)^{2}=n+26$. Center $(-5,1)$.",r"Radius of $B$ = distance from $(-5,1)$ to $(-5,10)$ $=9$. Radius of $A=9\div3=3$.",r"$n+26=3^{2}=9$, so $n=-17$."])
# 12
assert 4**(-1.5)==1/8
SPR('m2','AM-028',"The function $N$ is defined by $N(t)=k\\cdot4^{-at}$ for positive constants $k$ and $a$. The table shows values of $N$ for select values of $t$.\n\n<table class=\"dt\"><tr><th>$t$</th><th>$0$</th><th>$1$</th><th>$2$</th></tr><tr><td>$N(t)$</td><td>$640$</td><td>$80$</td><td>$10$</td></tr></table>\n\nWhat is the value of $a$?",1.5,
 [r"$N(0)=k=640$. Each step in $t$ multiplies $N$ by $\dfrac{80}{640}=\dfrac18$.",r"So $4^{-a}=\dfrac18$. Type <code>y=4^(-x)</code> and <code>y=1/8</code>: intersection at $x=1.5$.",r"Exact: $2^{-2a}=2^{-3}\Rightarrow a=\dfrac32$. Trap: reading the base as $2$ gives $a=3$."],disp=r"\dfrac{3}{2}")
# 13
MC('m2','AM-169',"For a real number $x$, $9^{x}-2\\cdot3^{x+1}-27=0$. What is the value of $3^{x+1}$?",r"$27$",[r"$-9$",r"$9$",r"$3$"],2,
 [r"Let $u=3^{x}$. Then $u^{2}-6u-27=0$, so $(u-9)(u+3)=0$.",r"$3^{x}>0$, so $u=9$ (reject $-3$).",r"$3^{x+1}=3u=27$. Traps: $9$ is $3^{x}$; $-9$ comes from the rejected root."])
# 14
MC('m2','AM-266',"The equation $x^2-5x+6=0$ has solutions $p$ and $q$. Which of the following equations has solutions $p^{2}$ and $q^{2}$?",r"$x^2-13x+36=0$",[r"$x^2-25x+36=0$",r"$x^2-5x+36=0$",r"$x^2-13x+6=0$"],0,
 [r"Solutions of the first equation: $p=2$, $q=3$, so the new solutions are $4$ and $9$.",r"Sum $=13$, product $=36$: $x^2-13x+36=0$. Type <code>y=x^2-13x+36</code>: zeros at $4$ and $9$.",r"Trap: $25=(p+q)^2$ is not $p^2+q^2$."])
# 15
assert Fr(2,3)+Fr(1,4)-Fr(1,2)==Fr(5,12)
MC('m2','AM-172',r"For a positive real number $x$, $\dfrac{\sqrt[3]{x^{2}}\cdot\sqrt[4]{x}}{\sqrt{x}}=\sqrt[6]{k}$, where $k=2^{15}$. Which of the following is equal to $x$?".replace("Which of the following is equal to $x$?","Which of the following is equal to $x$?"),r"$2^{6}$",[r"$2^{\frac{75}{2}}$",r"$2^{\frac{25}{2}}$",r"$2^{5}$"],0,
 [r"Left side: $x^{\frac23+\frac14-\frac12}=x^{\frac{5}{12}}$.",r"Right side: $k^{\frac16}=2^{\frac{15}{6}}=2^{\frac52}$.",r"$x^{\frac5{12}}=2^{\frac52}\Rightarrow x=2^{\frac52\cdot\frac{12}{5}}=2^{6}$.",r"Check: $64^{5/12}=2^{2.5}$; type <code>64^(5/12)</code> returns $5.657=2^{2.5}$."])
OUT['m2'][-1]['q']=r"For a positive real number $x$, $\dfrac{\sqrt[3]{x^{2}}\cdot\sqrt[4]{x}}{\sqrt{x}}=\sqrt[6]{k}$, where $k=2^{15}$. Which of the following is equal to $x$?"
# 16
MC('m2','AM-084',"The function $f$ is defined by $f(x)=\\dfrac{(2x-1)(3x+4)}{(x+5)(1-x)}$, where $x\\neq-5$ and $x\\neq1$. As the value of $x$ increases without bound, the value of $f(x)$ approaches which of the following?",r"$-6$",[r"$6$",r"$-2$",r"$0$"],1,
 [r"Type the function and zoom out: the curve levels off at $y=-6$.",r"Leading terms: numerator $6x^{2}$, denominator $-x^{2}$ (since $(x)(-x)=-x^{2}$).",r"Ratio $\to\dfrac{6}{-1}=-6$. Trap: $6$ forgets the sign from $(1-x)$."])
# 17
MC('m2','AM-269',"$$\\frac{x^{2}}{x-2}=\\frac{4}{x-2}$$\nHow many solutions does the equation above have?",r"Exactly one",[r"Zero",r"Exactly two",r"Infinitely many"],1,
 [r"Multiply by $x-2$ ($x\neq2$): $x^{2}=4$, so $x=2$ or $x=-2$.",r"$x=2$ makes the denominators $0$: extraneous. Only $x=-2$ works.",r"Type <code>y=x^2/(x-2)</code> and <code>y=4/(x-2)</code>: one intersection, at $x=-2$."])
# 18
MC('m2','AM-058',"Which expression is equivalent to $x^{4}-5x^{2}-36$?",r"$(x-3)(x+3)(x^{2}+4)$",[r"$(x^{2}-4)(x^{2}+9)$",r"$(x^{2}-9)(x^{2}-4)$",r"$(x^{2}+4)(x^{2}+9)$"],2,
 [r"Let $u=x^{2}$: $u^{2}-5u-36=(u-9)(u+4)$.",r"So $x^{4}-5x^{2}-36=(x^{2}-9)(x^{2}+4)=(x-3)(x+3)(x^{2}+4)$.",r"Check: graph the original and the option; $x^2+4$ never factors over the reals. Trap: swapping the signs gives $x^4+5x^2-36$."])
# 19
assert 10*2**(10/2)==320 and 40/2**(4/2)==10
MC('m2','AM-005',"The function $f$ is defined by $f(x)=a\\cdot2^{x/2}$, where $a$ is a constant. If $f(4)=40$, what is the value of $f(10)$?",r"$320$",[r"$2560$",r"$160$",r"$640$"],3,
 [r"$f(4)=a\cdot2^{2}=4a=40$, so $a=10$.",r"$f(10)=10\cdot2^{5}=320$. Type <code>10*2^(10/2)</code>.",r"Trap: ignoring the $\tfrac{x}{2}$ gives $a=2.5$ and $f(10)=2560$."])
# 20
SPR('m2','AM-170',"For constants $p$, $q$ and $c$, the equation $$(2x+3)(x^2+px+q)=2x^3+x^2+cx-15$$ is true for all real values of $x$. What is the value of $c$?",-13,
 [r"Constant terms: $3q=-15$, so $q=-5$.",r"$x^{2}$ terms: $2p+3=1$, so $p=-1$.",r"$x$ terms: $2q+3p=-10-3=-13$, so $c=-13$.",r"Check: type <code>y=(2x+3)(x^2-x-5)</code> and <code>y=2x^3+x^2-13x-15</code>: identical graphs."])
# 21
assert 5*(32-8)+12*(0-10)==0 and (8-3)**2+(10+2)**2==169
MC('m2','GT-191',"In the $xy$-plane, the circle $(x-3)^2+(y+2)^2=169$ passes through the point $(8,10)$. The line tangent to the circle at $(8,10)$ crosses the $x$-axis at the point $(a,0)$. What is the value of $a$?",r"$32$",[r"$\dfrac{23}{6}$",r"$\dfrac{16}{3}$",r"$\dfrac{64}{3}$"],0,
 [r"Center $(3,-2)$; radius vector to $(8,10)$ is $\langle5,12\rangle$. The tangent is perpendicular to it.",r"Tangent line: $5(x-8)+12(y-10)=0$. Set $y=0$: $5x-40-120=0$, so $x=32$.",r"Check: type <code>5(x-8)+12(y-10)=0</code> with the circle: it touches at one point and meets $y=0$ at $x=32$.",r"Trap: using the radius slope $\tfrac{12}{5}$ as the tangent slope gives $\tfrac{23}{6}$."])
# 22
assert 2*4+(-2)*(-2)-12==0
SPR('m2','AM-067',"If $x=-2$ is one solution to the equation $2x^2+kx-12=0$, what is the product of $k$ and the other solution?",-6,
 [r"Substitute $x=-2$: $8-2k-12=0$, so $k=-2$.",r"Equation: $2x^{2}-2x-12=0\Rightarrow x^{2}-x-6=0$, roots $-2$ and $3$. Other solution $=3$.",r"Product: $(-2)(3)=-6$. Check with product of roots: $\dfrac{-12}{2}=-6=(-2)(3)$."])
assert len(OUT['m1'])==22 and len(OUT['m2'])==22,(len(OUT['m1']),len(OUT['m2']))
json.dump(OUT,open('exam2.json','w'))
# duplicate-check keys & options
for m in OUT:
    for it in OUT[m]:
        if it['mc']: assert len(set(it['opts']))==4, it['id']
print('OK',len(OUT['m1']),len(OUT['m2']))
