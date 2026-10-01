"""SAAT (Tahsili) Math Week 6 — Grade 11 (11C). 24 items; every answer re-derived by an independent route."""
import math, cmath, itertools, sys
from fractions import Fraction as F

def chk(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond: sys.exit(1)

# ---------------------------------------------------------------- independent verification
# 1 logs by direct evaluation
chk("1 =12", round(math.log2(32)) + round(math.log(81, 3)) - round(math.log10(0.001)) == 12 and 5 + 4 - 2 == 7)
# 2 log2(12) = a + 2
a = math.log2(3); chk("2 a+2", abs(math.log2(12) - (a + 2)) < 1e-12 and abs(math.log2(12) - 2*a) > 0.1)
# 3 solve by scan, with domain
sols = [x for x in [i/1000 for i in range(-20000, 20000)] if x + 2 > 0 and x - 4 > 0 and abs(math.log(x+2, 3) + math.log(x-4, 3) - 3) < 1e-9]
chk("3 x=7 only", sols == [7.0] and (-5+2)*(-5-4) == 27 and (F(5, 2)+2)+(F(5, 2)-4) == 3)
# 4 halving tank
h = 0; v = 2048
while v > 16: v /= 2; h += 6
chk("4 42 h", h == 42 and 2048/2**6 == 32 and 2048/2**8 == 8 and 2048 == 2**11)
# 5 vertex
f = lambda x: 2*x*x - 12*x + 7
xs = [F(i, 100) for i in range(-1000, 1000)]
xm = min(xs, key=f); chk("5 (3,-11)", xm == 3 and f(xm) == -11 and 2*(3-3)**2-2 == -2 and f(F(6)) == 7)
# 6 arch
hh = lambda x: -(x-1)*(x-9)
mx = max(hh(F(i, 100)) for i in range(0, 1100)); chk("6 16", mx == 16 and 9-1 == 8 and 8//2 == 4)
# 7 Vieta
k = [k for k in range(-50, 100) if (lambda d: d >= 0 and abs(math.sqrt(d) - 3) < 1e-12)(49 - 4*k)]
chk("7 k=10", k == [10] and 1*6 == 6 and 3*4 == 12 and 7*3 == 21)
# 8 discriminant
good = lambda k: k != 0 and 36 - 12*k > 0
ks = [F(i, 4) for i in range(-40, 40)]
chk("8 k<3,k!=0", all(good(k) == (k < 3 and k != 0) for k in ks) and (36-12*3 == 0))
# 9 exponents
chk("9 =8", abs(8**(2/3) * (1/4)**(-1/2) - 8) < 1e-9 and abs(8**(2/3)*4 - 16) < 1e-9 and abs(8**(2/3)*0.5 - 2) < 1e-9 and 64*2 == 128)
# 10 taxi
rate = F(40-25, 14-8); base = 25 - rate*8
chk("10 55", rate == F(5, 2) and base == 5 and base + rate*20 == 55 and rate*20 == 50 and F(40)+5*rate == F(105, 2) and F(25, 8)*20 == F(125, 2))
# 11 composite domain
inner = lambda x: x*x - 5*x + 5
ok = lambda x: inner(x) >= 1
pts = [F(i, 8) for i in range(-80, 120)]
dom = {x for x in pts if ok(x)}
chk("11 domain", all((x <= 1 or x >= 4) == (x in dom) for x in pts))
# 12 similar plots
chk("12 60", F(40)*F(3, 2) == 60 and F(40)*F(9, 4) == 90 and F(40)*2 == 80 and F(40)*3 == 120)
# 13 circle: place points, measure
th = math.radians(76)  # central angle AOB = 2*38
A = (math.cos(-th/2), math.sin(-th/2)); B = (math.cos(th/2), math.sin(th/2)); O = (0, 0)
C = (math.cos(math.pi), math.sin(math.pi))           # major arc
def ang(P, Q, R):
    v1 = (P[0]-Q[0], P[1]-Q[1]); v2 = (R[0]-Q[0], R[1]-Q[1])
    return math.degrees(math.acos((v1[0]*v2[0]+v1[1]*v2[1])/(math.hypot(*v1)*math.hypot(*v2))))
# inscribed angle ACB should equal half the central angle
chk("13 angle ACB=38", abs(ang(A, C, B) - 38) < 1e-9)
chk("13 OAB=52", abs(ang(O, A, B) - 52) < 1e-9 and 180-76 == 104)
# 14 perpendicular bisector
Ap, Bp = (1, 2), (5, 8)
eq = lambda P: (P[0]-Ap[0])**2 + (P[1]-Ap[1])**2 == (P[0]-Bp[0])**2 + (P[1]-Bp[1])**2
cand = [(5, 2), (6, 3), (6, 7), (7, 11)]
chk("14 only (6,3)", [p for p in cand if eq(p)] == [(6, 3)])
# 15 cube
s = F(6); chk("15 216", 3*s*s == 108 and math.isclose(math.sqrt(3)*6, 6*math.sqrt(3)) and s**3 == 216 and s*s == 36)
d = 6*math.sqrt(3); chk("15 traps", abs(d**3 - 648*math.sqrt(3)) < 1e-6 and abs((d/2)**3 - 81*math.sqrt(3)) < 1e-6)
# 16 club
g11 = F(40, 100)*F(30, 100); oth = F(60, 100)*F(20, 100)
chk("16 50%", g11 == F(12, 100) and g11/(g11+oth) == F(1, 2) and (F(30)+F(20))/2 == 25)
# 17 normal band via erf
Phi = lambda z: 0.5*(1 + math.erf(z/math.sqrt(2)))
exact = Phi(2) - Phi(-1)
rule = 0.34 + 0.34 + 0.135
chk("17 81.5", abs(rule - 0.815) < 1e-12 and abs(exact - 0.8186) < 1e-3)
# 18 arrangements
perms = set(itertools.permutations("MAKKAH"))
chk("18 180", len(perms) == 180 and math.factorial(6)//(2*2*2) == 90 and math.factorial(5) == 120 and math.factorial(6)//2 == 360)
# 19 double angle
sx = 3/5; cx = -math.sqrt(1 - sx**2)
x = math.atan2(sx, cx)
chk("19 7/25", abs(math.cos(2*x) - 7/25) < 1e-12 and abs(math.sin(2*x) + 24/25) < 1e-12 and math.pi/2 < x < math.pi)
# 20 vectors
dot = lambda u, v: sum(a*b for a, b in zip(u, v))
chk("20 k=2", dot((2, 2, -1), (3, -4, -2)) == 0 and dot((F(8, 3), 2, -1), (3, -4, -2)) == 2 and dot((F(10, 3), 2, -1), (3, -4, -2)) == 4)
# parallel check -3/2
chk("20 parallel", F(-3, 2)/3 == F(2, -4) == F(-1, 2) * 1 and F(-1)/F(-2) != F(2, -4))
# 21 complex
z = (1 - 1j)**6
chk("21 8i", abs(z - 8j) < 1e-9 and abs((-2j)**3 - 8j) < 1e-9)
# 22 limit
vals = [(t*t - 4)/(t*t - t - 2) for t in (2 + 1e-7, 2 - 1e-7)]
chk("22 4/3", all(abs(v - 4/3) < 1e-6 for v in vals))
# 23 derivative min
fx = lambda x: x**3 - 6*x**2 + 5
dfx = lambda x: (fx(x+1e-6) - fx(x-1e-6))/2e-6
crit = [0, 4]
chk("23 min at 4", all(abs(dfx(c)) < 1e-4 for c in crit) and fx(4+0.1) > fx(4) < fx(4-0.1) and fx(0.1) < fx(0) > fx(-0.1) and fx(2) == -11)
# 24 integral exact via antiderivative and Riemann check
n = 200000; riem = sum((3*((i+0.5)*2/n)**2 + 2*((i+0.5)*2/n))*(2/n) for i in range(n))
chk("24 12", abs(riem - 12) < 1e-6 and 4 == 2**2 and 8 == 2**3 and 16 == 2*2**3)

# ---------------------------------------------------------------- item data
# option = (tex, note|None, numeric value|None). note None = correct.  Numeric options print ascending.
def O(tex, note=None, val=None, ok=False): return dict(tex=tex, note=note, val=val, ok=ok)
ITEMS = []
def item(**kw): ITEMS.append(kw)

item(strand="ALG", wk="Anchor · Logarithms", trick="A logarithm is an exponent: ask ``which power?''",
 q=r"What is the value of $\log_2 32+\log_3 81-\log_{10}0.001$?",
 opts=[O("$6$", r"$5+4-3$: treated $\log_{10}0.001$ as $+3$ and then subtracted it the wrong way round.", 6), O("$9$", r"ignored the last term altogether.", 9),
       O("$11$", r"counted two zeros: $0.001=10^{-2}$ instead of $10^{-3}$.", 11), O("$12$", ok=True, val=12)],
 sol=r"$\log_2 32=5$, $\log_3 81=4$ and $\log_{10}0.001=\log_{10}10^{-3}=-3$. So the value is $5+4-(-3)=12$.")
item(strand="ALG", wk="Anchor · Logarithms", trick="Split the product, then evaluate what is known",
 q=r"If $\log_2 3=a$, which expression is equal to $\log_2 12$?",
 opts=[O(r"$2a$", r"multiplied instead of adding: $\log_2 3\cdot\log_2 4$."), O(r"$a+4$", r"took $\log_2 4=4$ instead of $2$."),
       O(r"$a+2$", ok=True), O(r"$4a$", r"treated $12=3\cdot4$ as $3^4$-style scaling.")], key=2,
 sol=r"$\log_2 12=\log_2(3\cdot4)=\log_2 3+\log_2 4=a+2$.")
item(strand="ALG", wk="Anchor · Logarithms", trick="Check the domain: reject the root that makes an argument negative",
 q=r"What is the solution of $\log_3(x+2)+\log_3(x-4)=3$?",
 opts=[O(r"$x=-5$", r"a root of the quadratic, but it makes both arguments negative."), O(r"$x=\dfrac52$", r"added the arguments instead of multiplying them."),
       O(r"$x=7$", ok=True), O(r"$x=-5$ or $x=7$", r"kept the extraneous root.")], key=2,
 sol=r"Combine: $\log_3\big[(x+2)(x-4)\big]=3\Rightarrow(x+2)(x-4)=27\Rightarrow x^2-2x-35=0\Rightarrow(x-7)(x+5)=0$. The arguments must be positive, so $x>4$: reject $x=-5$. The solution is $x=7$ (check: $\log_39+\log_33=2+1=3$).")
item(strand="ALG", wk="Anchor · Exponential models", trick="Count the halvings, then multiply by the period",
 q=r"The water in a storage tank at the Jubail desalination plant halves every $6$ hours. The tank starts with $2048$ cubic metres. After how many hours will it hold $16$ cubic metres?",
 opts=[O("$36$ hours", r"$6$ halvings: that leaves $32$ m$^3$, not $16$.", 36), O("$42$ hours", ok=True, val=42), O("$48$ hours", r"$8$ halvings: that leaves $8$ m$^3$.", 48),
       O("$66$ hours", r"used $2048=2^{11}$ and ignored the target (that is $11$ halvings).", 66)],
 sol=r"$\dfrac{2048}{16}=128=2^7$, so $7$ halvings are needed: $7\times6=42$ hours.")
item(strand="ALG", wk="Anchor · Vertex form", trick=r"Vertex at $x=-\frac{b}{2a}$; the factor outside the bracket multiplies the correction",
 q=r"What are the coordinates of the vertex of the graph of $f(x)=2x^{2}-12x+7$?",
 opts=[O(r"$(3,-11)$", ok=True), O(r"$(3,-2)$", r"completed the square but forgot to multiply the correction by $2$: $2(x-3)^2-9+7$."),
       O(r"$(-3,-11)$", r"read $2(x-3)^2$ as $2(x+3)^2$: sign of $h$."), O(r"$(6,7)$", r"used $x=-b/a$ instead of $-b/2a$.")], key=0,
 sol=r"$x=-\dfrac{-12}{2(2)}=3$ and $f(3)=18-36+7=-11$. Equivalent: $2(x^2-6x)+7=2(x-3)^2-18+7=2(x-3)^2-11$. The vertex is $(3,-11)$.")
item(strand="ALG", wk="Anchor · Factored form", trick="The axis sits halfway between the two intercepts",
 q=r"The height, in metres, of a decorative arch over a walkway on the Jeddah Corniche is modelled by $h(x)=-(x-1)(x-9)$, where $x$ is the distance in metres along the walkway. What is the greatest height of the arch?",
 opts=[O("$4$ m", r"half the span: a horizontal length, not a height.", 4), O("$5$ m", r"the $x$-coordinate of the vertex.", 5), O("$8$ m", r"the span between the intercepts.", 8), O("$16$ m", ok=True, val=16)],
 sol=r"The zeros are $x=1$ and $x=9$, so the axis is $x=\dfrac{1+9}{2}=5$. Then $h(5)=-(5-1)(5-9)=-(4)(-4)=16$ metres.")
item(strand="ALG", wk="Anchor · Standard form", trick="Sum and difference of the roots give the roots",
 q=r"The two roots of $x^{2}-7x+k=0$ differ by $3$. What is the value of $k$?",
 opts=[O("$6$", r"roots $1$ and $6$: the sum is right but the difference is $5$.", 6), O("$10$", ok=True, val=10), O("$12$", r"roots $3$ and $4$: the sum is right but the difference is $1$.", 12), O("$21$", r"multiplied the sum $7$ by the difference $3$.", 21)],
 sol=r"The roots $r_1,r_2$ satisfy $r_1+r_2=7$ and $r_1-r_2=3$, so $r_1=5$ and $r_2=2$. Then $k=r_1r_2=10$. (Check: $x^2-7x+10=(x-5)(x-2)$.)")
item(strand="ALG", wk="Anchor · Quadratics", trick="Discriminant, and keep the leading-coefficient condition",
 q=r"For which values of $k$ does the equation $kx^{2}-6x+3=0$ have two distinct real solutions?",
 opts=[O(r"$k<3$", r"forgot that $k=0$ makes the equation linear (one solution)."), O(r"$k<3$ and $k\neq0$", ok=True),
       O(r"$k>3$", r"reversed the inequality $36-12k>0$."), O(r"$k\le3$ and $k\neq0$", r"$k=3$ gives a repeated root, not two distinct roots.")], key=1,
 sol=r"Two distinct real roots need $b^2-4ac=36-12k>0$, so $k<3$. The equation is quadratic only when $k\ne0$ (at $k=0$ it is $-6x+3=0$, one solution). So $k<3$ and $k\ne0$.")
item(strand="ALG", wk="Spiral · Exponents and radicals", trick="Root first, then power; a negative exponent flips",
 q=r"Which of the following is equal to $8^{2/3}\cdot\left(\dfrac14\right)^{-1/2}$?",
 opts=[O("$2$", r"read $(1/4)^{-1/2}$ as $\tfrac12$: the negative exponent was ignored.", 2), O("$8$", ok=True, val=8), O("$16$", r"dropped the square root: $(1/4)^{-1}=4$.", 16), O("$128$", r"computed $8^{2/3}$ as $8^2=64$.", 128)],
 sol=r"$8^{2/3}=(\sqrt[3]{8})^2=4$. $\left(\frac14\right)^{-1/2}=4^{1/2}=2$. The product is $4\cdot2=8$.")
item(strand="ALG", wk="Spiral · Systems and modelling", trick="Rate from the difference of two points, then the fixed fee",
 q=r"A taxi in Jeddah charges a fixed starting fee plus a fixed price per kilometre. An $8$ km trip costs $25$ SAR and a $14$ km trip costs $40$ SAR. How much does a $20$ km trip cost?",
 opts=[O("$50$ SAR", r"$2.5\times20$: left out the starting fee.", 50), O("$52.5$ SAR", r"added only $5$ km to the $14$ km fare instead of $6$.", 52.5), O("$55$ SAR", ok=True, val=55), O("$62.5$ SAR", r"treated the fare as proportional to distance ($25/8$ per km).", 62.5)],
 sol=r"Rate: $\dfrac{40-25}{14-8}=2.5$ SAR per km. Fee: $25-2.5(8)=5$ SAR. For $20$ km: $5+2.5(20)=55$ SAR.")
item(strand="ALG", wk="Spiral · Functions", trick="The inner output must land in the outer function's domain",
 q=r"Let $f(x)=\sqrt{x-1}$ and $g(x)=x^{2}-5x+5$. What is the domain of $f(g(x))$?",
 opts=[O(r"$[1,4]$", r"kept the interval between the roots, but $x^2-5x+4\ge0$ is true outside them."), O(r"$(-\infty,1]\cup[4,\infty)$", ok=True),
       O(r"$(1,4)$", r"both the wrong region and the wrong ends."), O(r"$(-\infty,1)\cup(4,\infty)$", r"made the ends open, but $\sqrt{0}$ is allowed.")], key=1,
 sol=r"$f(g(x))=\sqrt{g(x)-1}=\sqrt{x^2-5x+4}$, which needs $x^2-5x+4\ge0$. Factor: $(x-1)(x-4)\ge0$, true for $x\le1$ or $x\ge4$ (the ends are included).")
item(strand="GEO", wk="Spiral · Similarity", trick="Lengths scale by the square root of the area ratio",
 q=r"Two similar rectangular plots in Makkah have areas in the ratio $4:9$. The perimeter of the smaller plot is $40$ m. What is the perimeter of the larger plot?",
 opts=[O("$60$ m", ok=True, val=60), O("$80$ m", r"scaled by $2$ (took only the root of the smaller part).", 80), O("$90$ m", r"applied the area ratio $9/4$ to a length.", 90), O("$120$ m", r"scaled by $3$ and dropped the $2$ of the length ratio $2:3$.", 120)],
 sol=r"Areas $4:9$ means lengths $2:3$. Perimeters are lengths, so they scale by $\dfrac32$: $40\times\dfrac32=60$ m.")
item(strand="GEO", wk="Spiral · Circles", trick="Central angle is twice the inscribed angle, then use the equal radii",
 q=r"In a circle with centre $O$, points $A$, $B$ and $C$ lie on the circle with $C$ on the major arc $AB$. If $\angle ACB=38^\circ$, what is the measure of $\angle OAB$?",
 opts=[O(r"$38^\circ$", r"copied the inscribed angle.", 38), O(r"$52^\circ$", ok=True, val=52), O(r"$76^\circ$", r"stopped at the central angle $\angle AOB$.", 76), O(r"$104^\circ$", r"$180^\circ-76^\circ$: the sum of the two base angles.", 104)],
 sol=r"The central angle is $\angle AOB=2(38^\circ)=76^\circ$. Triangle $OAB$ is isosceles ($OA=OB$ are radii), so $\angle OAB=\dfrac{180^\circ-76^\circ}{2}=52^\circ$.")
item(strand="GEO", wk="Spiral · Coordinate geometry", trick="Midpoint plus the negative reciprocal slope",
 q=r"Which of the following points lies on the perpendicular bisector of the segment with endpoints $A(1,2)$ and $B(5,8)$?",
 opts=[O(r"$(5,2)$", r"used the negated slope $-\tfrac32$ instead of the negative reciprocal."), O(r"$(6,3)$", ok=True),
       O(r"$(6,7)$", r"used the slope $+\tfrac23$: reciprocal without the sign change."), O(r"$(7,11)$", r"drew the parallel to $AB$ through the midpoint.")], key=1,
 sol=r"Midpoint: $(3,5)$. Slope of $AB$: $\dfrac{8-2}{5-1}=\dfrac32$, so the bisector has slope $-\dfrac23$: $y-5=-\dfrac23(x-3)$, i.e. $2x+3y=21$. Only $(6,3)$ fits: $12+9=21$.")
item(strand="GEO", wk="Seed · Solids", trick="Space diagonal of a cube is $s\sqrt3$",
 q=r"The space diagonal of a cube is $6\sqrt3$ cm. What is the volume of the cube?",
 opts=[O(r"$36$ cm$^3$", r"found the edge but squared it (a face area).", 36), O(r"$81\sqrt3$ cm$^3$", r"took the diagonal as twice the edge.", 81*math.sqrt(3)), O(r"$216$ cm$^3$", ok=True, val=216), O(r"$648\sqrt3$ cm$^3$", r"cubed the diagonal itself.", 648*math.sqrt(3))],
 sol=r"For a cube of edge $s$ the space diagonal is $s\sqrt3$. So $s\sqrt3=6\sqrt3\Rightarrow s=6$ and $V=s^3=216$ cm$^3$.")
item(strand="STA", wk="Spiral · Percentages", trick="Weight each group, then take the share of the total",
 q=r"In a Jeddah school, $40\%$ of the students are in Grade 11. In the robotics club, $30\%$ of the Grade 11 students and $20\%$ of all the other students are members. What percent of the club's members are in Grade 11?",
 opts=[O("$12\%$", r"that is Grade 11 members as a share of the whole school.", 12), O("$25\%$", r"averaged the two membership rates $30\%$ and $20\%$.", 25), O("$30\%$", r"the Grade 11 membership rate, not their share of the club.", 30), O("$50\%$", ok=True, val=50)],
 sol=r"Take $100$ students. Grade 11: $40$ students, $30\%$ join $=12$. Others: $60$ students, $20\%$ join $=12$. The club has $24$ members, of whom $12$ are in Grade 11: $\dfrac{12}{24}=50\%$.")
item(strand="STA", wk="Spiral · Normal distribution", trick="Asymmetric band: add the pieces of the 68--95--99.7 rule",
 q=r"Scores on a Tahsili practice test follow a normal distribution with mean $70$ and standard deviation $8$. Using the $68$--$95$--$99.7$ rule, approximately what percent of the scores lie between $62$ and $86$?",
 opts=[O("$68\%$", r"used only $\pm1$ standard deviation.", 68), O("$81.5\%$", ok=True, val=81.5), O("$95\%$", r"used $\pm2$ standard deviations.", 95), O("$97.5\%$", r"counted everything below $+2\sigma$.", 97.5)],
 sol=r"$62=70-1\sigma$ and $86=70+2\sigma$. From $-1\sigma$ to the mean is $34\%$; from the mean to $+2\sigma$ is $34\%+13.5\%=47.5\%$. Total $=34+47.5=81.5\%$.")
item(strand="STA", wk="Spiral · Counting", trick="Divide by the factorial of each repeated letter",
 q=r"How many different arrangements are there of all the letters of the word MAKKAH?",
 opts=[O("$90$", r"divided by three repeats, but only two letters repeat.", 90), O("$120$", r"computed $5!$.", 120), O("$180$", ok=True, val=180), O("$360$", r"divided for only one repeated letter.", 360)],
 sol=r"Six letters, with K twice and A twice: $\dfrac{6!}{2!\,2!}=\dfrac{720}{4}=180$.")
item(strand="TRI", wk="Seed · Trigonometry", trick="Pick the double-angle form that needs only the given ratio",
 q=r"If $\sin x=\dfrac35$ and $x$ lies in the second quadrant, what is the value of $\cos 2x$?",
 opts=[O(r"$-\dfrac{24}{25}$", r"found $\sin 2x$ instead of $\cos 2x$.", -24/25), O(r"$-\dfrac{7}{25}$", r"subtracted in the wrong order: $\sin^2x-\cos^2x$.", -7/25), O(r"$\dfrac{7}{25}$", ok=True, val=7/25), O(r"$\dfrac{24}{25}$", r"$|\sin 2x|$: wrong function and the sign dropped.", 24/25)],
 sol=r"$\cos2x=1-2\sin^2x=1-2\cdot\dfrac{9}{25}=\dfrac{7}{25}$. (Check: $\cos x=-\dfrac45$, so $\cos^2x-\sin^2x=\dfrac{16}{25}-\dfrac{9}{25}=\dfrac7{25}$.)")
item(strand="TRI", wk="Seed · Vectors", trick="Perpendicular means the dot product is zero",
 q=r"For which value of $k$ are the vectors $\mathbf u=(k,\,2,\,-1)$ and $\mathbf v=(3,\,-4,\,-2)$ perpendicular?",
 opts=[O(r"$-\dfrac32$", r"tested for parallel vectors (equal ratios) instead of perpendicular.", -1.5), O(r"$2$", ok=True, val=2), O(r"$\dfrac83$", r"left out the third component.", 8/3), O(r"$\dfrac{10}{3}$", r"sign slip on the third term: $(-1)(-2)=-2$.", 10/3)],
 sol=r"$\mathbf u\cdot\mathbf v=3k+(2)(-4)+(-1)(-2)=3k-8+2=3k-6=0\Rightarrow k=2$.")
item(strand="TRI", wk="Seed · Complex numbers", trick="Square first: $(1-i)^2=-2i$",
 q=r"What is the value of $(1-i)^{6}$?",
 opts=[O(r"$-8i$", r"used $i^3=i$ (it is $-i$)."), O(r"$8i$", ok=True), O(r"$-8$", r"treated $(1-i)^2$ as $-2$."), O(r"$8$", r"treated $(1-i)^2$ as $2$ and cubed it.")], key=1,
 sol=r"$(1-i)^2=1-2i+i^2=-2i$. Then $(1-i)^6=(-2i)^3=-8i^3=-8(-i)=8i$.")
item(strand="CAL", wk="Seed · Limits", trick="Factor out the zero factor before substituting",
 q=r"What is the value of $\displaystyle\lim_{x\to2}\dfrac{x^{2}-4}{x^{2}-x-2}$?",
 opts=[O(r"$0$", r"the numerator is $0$, so the whole fraction was taken as $0$."), O(r"$1$", r"compared the leading coefficients."), O(r"$\dfrac43$", ok=True), O(r"does not exist", r"stopped at $\frac00$ and called it undefined.")], key=2,
 sol=r"Direct substitution gives $\frac00$, so factor: $\dfrac{(x-2)(x+2)}{(x-2)(x+1)}=\dfrac{x+2}{x+1}$ for $x\ne2$. The limit is $\dfrac{2+2}{2+1}=\dfrac43$.")
item(strand="CAL", wk="Seed · Derivatives", trick="$f'=0$ gives candidates; the sign change names the minimum",
 q=r"At what value of $x$ does the function $f(x)=x^{3}-6x^{2}+5$ have a local minimum?",
 opts=[O(r"$x=0$", r"a critical point, but it is the local maximum.", 0), O(r"$x=2$", r"the inflection point ($f''=0$), not a critical point.", 2), O(r"$x=4$", ok=True, val=4), O(r"$x=6$", r"a zero of $x^3-6x^2$, not of $f'$.", 6)],
 sol=r"$f'(x)=3x^2-12x=3x(x-4)=0$ gives $x=0$ or $x=4$. The sign of $f'$ goes $+,-,+$ across $0$ and $4$, so $x=0$ is a maximum and $x=4$ a minimum. (Also $f''(4)=12>0$.)")
item(strand="CAL", wk="Seed · Integration", trick="Antiderivative, then upper minus lower",
 q=r"What is the value of $\displaystyle\int_{0}^{2}\left(3x^{2}+2x\right)dx$?",
 opts=[O("$4$", r"integrated only the $2x$ term.", 4), O("$8$", r"integrated only the $3x^2$ term.", 8), O("$12$", ok=True, val=12), O("$16$", r"wrote $\int2x\,dx$ as $2x^2$.", 16)],
 sol=r"$\displaystyle\int_0^2(3x^2+2x)\,dx=\Big[x^3+x^2\Big]_0^2=(8+4)-0=12$.")

assert len(ITEMS) == 24

# ---------------------------------------------------------------- finish: ascending numerics, balanced letters
TARGET = {1: "D", 2: "A", 3: "A", 4: "B", 5: "A", 6: "D", 7: "B", 8: "D", 9: "B", 10: "C", 11: "D", 12: "A", 13: "B", 14: "A",
          15: "C", 16: "D", 17: "B", 18: "C", 19: "C", 20: "B", 21: "A", 22: "D", 23: "C", 24: "C"}
for n, it in enumerate(ITEMS, 1):
    o = it["opts"]
    if all(x["val"] is not None for x in o):
        o.sort(key=lambda x: x["val"]); it["fixed"] = True
        it["key"] = [i for i, x in enumerate(o) if x["ok"]][0] if any(x["ok"] for x in o) else None
    else:
        it["fixed"] = False
        # ok flag is set on the right option
        k0 = [i for i, x in enumerate(o) if x["ok"]][0]
        want = "ABCD".index(TARGET[n]); r = (want - k0) % 4
        it["opts"] = o[-r:] + o[:-r] if r else o
    it["key"] = [i for i, x in enumerate(it["opts"]) if x["ok"]][0]
    it["n"] = n

from collections import Counter
letters = ["ABCD"[i["key"]] for i in ITEMS]
cnt = Counter(letters)
print("keys:", "".join(letters), dict(sorted(cnt.items())))
chk("24 items, 6/6/6/6", sorted(cnt.values()) == [6, 6, 6, 6])
chk("no triple repeats", not any(letters[i] == letters[i+1] == letters[i+2] for i in range(22)))
for it in ITEMS:
    assert len(it["opts"]) == 4 and len({o["tex"] for o in it["opts"]}) == 4
    assert sum(o["ok"] for o in it["opts"]) == 1
    assert all(o["note"] for o in it["opts"] if not o["ok"]), it["n"]
    assert it["trick"] and it["sol"]
# numeric-option check: key position matches the independently verified value
VERIFIED = {1: "12", 4: "42", 6: "16", 7: "10", 9: "8", 10: "55", 12: "60", 13: "52", 15: "216", 16: "50", 17: "81.5", 18: "180", 23: "4", 24: "12"}
import re
for n, v in VERIFIED.items():
    t = ITEMS[n-1]["opts"][ITEMS[n-1]["key"]]["tex"]
    assert re.search(r"(?<![\d.])" + re.escape(v) + r"(?![\d.])", t), (n, t)
chk("numeric keys match verified values", True)
print("strands", Counter(i["strand"] for i in ITEMS), "origin", Counter(i["wk"].split(" · ")[0] for i in ITEMS))
