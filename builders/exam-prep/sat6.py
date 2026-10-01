"""SAT Math Week 6 (Grade 11, 11C) — paper + key. All answers re-derived in code before the TeX is written."""
import math, statistics as st, itertools, sys
from fractions import Fraction as F

# ------------------------------------------------------------------ verification
def chk(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond: sys.exit(1)

# A1 (a/2)(4x-6)=10x+b  -> 2a x - 3a = 10x + b
a = F(10, 2); b = -3 * a
chk("A1 a=5,b=-15,a+b=-10", a == 5 and b == -15 and a + b == -10 and all((a/2)*(4*x-6) == 10*x+b for x in range(-4, 5)))
# A2 5x-2y=9, kx+6y=10 no solution -> k=-15
k = -15
chk("A2 k=-15 parallel, consts differ", F(5, k) == F(-2, 6) and F(9, 10) != F(5, k))
chk("A2 distractors differ", len({-30, -15, 15, 30}) == 4)
# A3 3.5*12 + 1.25 p <= 90
pmax = max(p for p in range(0, 100) if 3.5*12 + 1.25*p <= 90)
chk("A3 38 pens", pmax == 38 and 3.5*12 + 1.25*39 > 90 and 90 - 42 == 48 and 90/1.25 == 72)
# B1 g(x) = -f(x+3) = -sqrt(x+8)
f = lambda x: math.sqrt(x + 5)
g = lambda x: -f(x + 3)
chk("B1 g=-sqrt(x+8)", all(abs(g(x) + math.sqrt(x + 8)) < 1e-12 for x in [-3, 0, 4, 10]))
# B2 tangent: y=2x+c to y=x^2-4x+7
c = -2
disc = lambda c: 36 - 4*(7 - c)
chk("B2 c=-2 disc 0", disc(c) == 0 and disc(-1) != 0)
# B3 1.05^(t/3), 6 years
chk("B3 10.25%", abs(1.05**2 - 1.1025) < 1e-12 and round((1.05**3 - 1)*100, 2) == 15.76)
# C1 headphones
p = 241.5 / (0.7 * 1.15)
chk("C1 300", abs(p - 300) < 1e-9 and round(241.5/0.85, 2) == 284.12 and round(241.5*1.3, 2) == 313.95 and round(241.5/0.7, 2) == 345.0)
# C2
chk("C2 20", abs(1 - 1/1.25 - 0.2) < 1e-12)
# C3 table
T = {"U": (48, 30, 22), "O": (32, 45, 65)}
tot = [T["U"][i] + T["O"][i] for i in range(3)]
allN = sum(tot)
bc_over = (T["O"][1] + T["O"][2]) / (tot[1] + tot[2])
chk("C3 totals", tot == [80, 75, 87] and allN == 242 and sum(T["U"]) == 100 and sum(T["O"]) == 142)
chk("C3 68%", round(bc_over*100) == 68 and round((T["O"][1]+T["O"][2])/allN*100) == 45 and round(sum(T["O"])/allN*100) == 59
    and round((T["O"][1]+T["O"][2])/sum(T["O"])*100) == 77)
# C4 acid
w = 300*0.12/0.08 - 300
chk("C4 150", abs(w - 150) < 1e-9)
# C5
vals = [2, 3, 5, 8]; fr = [4, 6, 7, 3]
data = sum(([v]*n for v, n in zip(vals, fr)), [])
mean = st.mean(data); med = st.median(data)
chk("C5 mean-median=.25", len(data) == 20 and mean == 4.25 and med == 4 and mean - med == 0.25
    and abs(st.mean(vals) - med - 0.5) < 1e-12 and mean - data[9] == 1.25 and st.median(fr) == 5 and abs(5 - mean) == 0.75)
# C6
A = [12, 14, 15, 16, 18]; B = [12, 14, 15, 16, 38]
chk("C6", st.median(A) == st.median(B) == 15 and st.mean(B) > st.mean(A) and st.pstdev(B) > st.pstdev(A)
    and max(A)-min(A) == 6 and max(B)-min(B) == 26)
# C7 histogram
bins = [(0, 10), (10, 20), (20, 30), (30, 40), (40, 50)]; fq = [2, 5, 9, 3, 1]
n = sum(fq)
lo = sum(l*q for (l, h), q in zip(bins, fq))/n
hi = sum(h*q for (l, h), q in zip(bins, fq))/n
mid = sum((l+h)/2*q for (l, h), q in zip(bins, fq))/n
chk("C7 least mean 18", n == 20 and lo == 18 and hi == 28 and mid == 23)
# C8 boxplots
X = (40, 55, 68, 80, 96); Y = (50, 60, 64, 72, 90)
iqrX = X[3]-X[1]; iqrY = Y[3]-Y[1]
chk("C8 statements", (Y[4]-Y[0] > X[4]-X[0]) is False and (iqrX > 2*iqrY) is True and (X[2] < Y[2]) is False and iqrX == 25 and iqrY == 12)
# C9 transform
mu, sd = 40, 6
chk("C9 55, 9", (1.5*mu - 5, 1.5*sd) == (55, 9))
# C10 area
chk("C10", round(35*3.28**2, 1) == 376.5 and round(35*3.28, 1) == 114.8 and round(35/3.28, 1) == 10.7 and round(35/3.28**2, 1) == 3.3)
# C11
yhat = 3.2*6 + 15
chk("C11 5.2", abs(abs(29 - yhat) - 5.2) < 1e-9)
# C12
same = F(math.comb(5, 2)+math.comb(4, 2)+math.comb(3, 2), math.comb(12, 2))
repl = F(25+16+9, 144)
chk("C12 19/66", same == F(19, 66) and repl == F(25, 72) and F(19, 132) < same < repl < F(5, 12) and F(5, 12) == F(5, 12))
# C13 text only
# D1
k_ = F(39, 13)
chk("D1 90", 5*k_ + 12*k_ + 39 == 90 and 5**2+12**2 == 13**2)
# D2 circle
chk("D2 k=23", 36 - 13 == 23)
# D3 sphere
r = round((288*3/4) ** (1/3))
chk("D3 144pi", r == 6 and 4*r*r == 144 and r*r == 36 and 2*r*r == 72 and 3*r*r == 108 and F(4, 3)*r**3 == 288)

# ------------------------------------------------------------------ item data
N, C, D = "N", "C", "D"
ITEMS = []
def item(**kw): ITEMS.append(kw)

# keys: for MCQ 'opts' = 4 option TeX strings, 'key' = index; mode 'grid' (2x2) or 'list'
item(id="A1", dom="Algebra", sk="Linear equations in one variable", lv="H", tool=N, wk="Spiral · Week 1", spr=True, ans="-10",
 q=r"In the equation $\dfrac{a}{2}(4x-6)=10x+b$, $a$ and $b$ are constants. If the equation has infinitely many solutions, what is the value of $a+b$?",
 trick="Match coefficients, then constants",
 sol=r"Expand the left side: $2ax-3a=10x+b$. For every $x$, the coefficients of $x$ must match, so $2a=10$ and $a=5$. The constants must then match: $b=-3a=-15$. Therefore $a+b=5+(-15)=-10$.",
 why=r"Students who match only the constants (or only the $x$-terms) find one of $a,b$ and stop; $a+b$ needs both. Dropping the $-3$ from $-3a$ when distributing gives $b=-5$ and $0$.")
item(id="A2", dom="Algebra", sk="Systems of two linear equations", lv="M", tool=N, wk="Spiral · Week 2", opts=[r"$-30$", r"$-15$", r"$15$", r"$30$"], key=1, mode="grid",
 q=r"\[\begin{aligned}5x-2y&=9\\ kx+6y&=10\end{aligned}\]In the system of equations above, $k$ is a constant. If the system has no solution, what is the value of $k$?",
 trick="No solution means same slope, different intercept",
 sol=r"No solution means parallel lines: equal slopes and different intercepts. Multiply the first equation by $3$: $15x-6y=27$. Adding it to the second equation gives $(15+k)x=37$. This has no solution only if $15+k=0$, so $k=-15$. The lines are parallel, not identical, because the constants are not in the same ratio: $\frac{5}{-15}=\frac{-2}{6}=-\frac13$ but $\frac{9}{10}\ne-\frac13$.",
 why=r"(A) $-30$: doubled the multiplier. (C) $15$: sign slip when matching $-2y$ with $6y$. (D) $30$: both slips. Check the sign of the $y$-terms before cross-multiplying.")
item(id="A3", dom="Algebra", sk="Linear inequalities / modeling", lv="M", tool=C, wk="Spiral · Week 2", opts=[r"$38$", r"$39$", r"$48$", r"$72$"], key=0, mode="grid",
 q=r"A school club has a budget of at most \$90. Notebooks cost \$3.50 each and pens cost \$1.25 each. The club buys $12$ notebooks. What is the greatest number of pens it can buy?",
 trick="Solve, then round DOWN for an ``at most'' count",
 sol=r"$3.50(12)+1.25p\le 90\Rightarrow 42+1.25p\le90\Rightarrow p\le\dfrac{48}{1.25}=38.4$. A count must be a whole number and the budget cannot be exceeded, so round down: $p=38$.",
 why=r"(B) $39$ rounds $38.4$ up and breaks the budget ($42+48.75=90.75$). (C) $48$ is the money left over, not the number of pens. (D) $72$ is $90\div1.25$, ignoring the notebooks.")
item(id="B1", dom="Advanced Math", sk="Nonlinear functions: transformations", lv="M", tool=N, wk="Spiral · Week 3",
 opts=[r"$g(x)=-\sqrt{x+2}$", r"$g(x)=\sqrt{x+8}$", r"$g(x)=-\sqrt{x+8}$", r"$g(x)=-\sqrt{x+5}-3$"], key=2, mode="grid",
 q=r"The function $f$ is defined by $f(x)=\sqrt{x+5}$. The graph of $y=g(x)$ is the graph of $y=f(x)$ shifted $3$ units to the left and then reflected across the $x$-axis. Which equation defines $g$?",
 trick="Inside moves opposite, outside moves with",
 sol=r"Shifting $3$ units left replaces $x$ by $x+3$ inside: $f(x+3)=\sqrt{(x+3)+5}=\sqrt{x+8}$. Reflecting across the $x$-axis negates the whole output: $g(x)=-\sqrt{x+8}$.",
 why=r"(A) shifted right instead of left. (B) forgot the reflection. (D) treated ``left $3$'' as ``down $3$'' (an outside change).")
item(id="B2", dom="Advanced Math", sk="Nonlinear equations and systems", lv="H", tool=D, wk="Spiral · Week 4", spr=True, ans="-2",
 q=r"The line $y=2x+c$ is tangent to the parabola $y=x^{2}-4x+7$ in the $xy$-plane, where $c$ is a constant. What is the value of $c$?",
 trick="Tangent means discriminant zero",
 sol=r"Set the expressions equal: $x^2-4x+7=2x+c\Rightarrow x^2-6x+(7-c)=0$. A tangent line meets the parabola at exactly one point, so the discriminant is $0$: $(-6)^2-4(1)(7-c)=0\Rightarrow 36-28+4c=0\Rightarrow c=-2$. (Desmos check: graph $y=x^2-4x+7$ and $y=2x+c$ with a slider; they touch once at $c=-2$, at $(3,4)$.)",
 why=r"Students who set $c=7$ (matching the $y$-intercept) or who forget the $-4x$ moves to the other side (using $-2x$ instead of $-6x$) get $c=6$.")
item(id="B3", dom="Advanced Math", sk="Exponential models", lv="M", tool=C, wk="Spiral · Week 5", opts=[r"$5\%$", r"$10\%$", r"$10.25\%$", r"$15.76\%$"], key=2, mode="grid",
 q=r"The value $V$, in dollars, of an investment $t$ years after it was made is modeled by $V(t)=2000(1.05)^{t/3}$. By what percent does the value increase every $6$ years?",
 trick="The period in the exponent sets the multiplier",
 sol=r"Every $3$ years the value is multiplied by $1.05$. In $6$ years that happens twice: $(1.05)^2=1.1025$, an increase of $10.25\%$.",
 why=r"(A) read $5\%$ as the rate per $6$ years. (B) added $5\%+5\%$ and ignored compounding. (D) $(1.05)^3$: used the exponent $6/2$ instead of $6/3$.")
item(id="C1", dom="Problem-Solving and Data Analysis", sk="Percentages", lv="M", tool=C, wk="Anchor · 6A Percents", opts=[r"\$284.12", r"\$300.00", r"\$313.95", r"\$345.00"], key=1, mode="grid",
 q=r"A pair of headphones is discounted by $30\%$. A $15\%$ sales tax is then applied to the discounted price, and the total paid is \$241.50. What was the original price of the headphones, before the discount?",
 trick="Undo a chain with the product of the multipliers",
 sol=r"The chain of changes is one multiplier: $0.70\times1.15=0.805$. So $0.805p=241.50$ and $p=\dfrac{241.50}{0.805}=300$.",
 why=r"(A) $241.50\div0.85$ treats the two changes as a net $-15\%$. (C) $241.50\times1.30$ adds the $30\%$ back to the total. (D) $241.50\div0.70$ undoes only the discount.")
item(id="C2", dom="Problem-Solving and Data Analysis", sk="Percentages", lv="M", tool=N, wk="Anchor · 6A Percents", spr=True, ans="20",
 q=r"A town's population increased by $25\%$ from 2020 to 2023. By what percent must the population decrease from 2023 to 2026 for it to return to its 2020 value?",
 trick="The percent back is not the percent forward",
 sol=r"Let the 2020 population be $P$. In 2023 it is $1.25P$. We need $1.25P(1-r)=P$, so $1-r=\dfrac{1}{1.25}=0.8$ and $r=0.20$. The answer is $20$.",
 why=r"The common wrong answer is $25$: the decrease is taken from the larger 2023 base, so a smaller percent undoes the increase.")
item(id="C3", dom="Problem-Solving and Data Analysis", sk="Percentages / two-way tables", lv="M", tool=C, wk="Anchor · 6A Percents", opts=[r"$45\%$", r"$59\%$", r"$68\%$", r"$77\%$"], key=2, mode="grid",
 q=r"A survey asked $242$ people their age group and preferred way to travel to work.\par\medskip\centerline{\begin{tabular}{@{}l|ccc|c@{}}&Train&Bus&Car&Total\\\hline Under 30&48&30&22&100\\ 30 or over&32&45&65&142\\\hline Total&80&75&87&242\end{tabular}}\par\medskip Of the people who prefer the bus or the car, approximately what percent are $30$ or over?",
 trick="Name the denominator: the subset the question names",
 sol=r"The subset is ``bus or car'': $75+87=162$ people. Of those, $45+65=110$ are $30$ or over. $\dfrac{110}{162}\approx0.679\approx68\%$.",
 why=r"(A) $110/242$: whole-survey denominator. (B) $142/242$: all $30$-or-over people, ignoring the subset. (D) $110/142$: used the age group as the denominator.")
item(id="C4", dom="Problem-Solving and Data Analysis", sk="Percentages / mixtures", lv="M", tool=N, wk="Anchor · 6A Percents", spr=True, ans="150",
 q=r"A $300$-milliliter solution is $12\%$ acid by volume. How many milliliters of water must be added to the solution so that it becomes $8\%$ acid by volume?",
 trick="Hold the solute fixed, change the total",
 sol=r"The acid does not change: $0.12(300)=36$ mL. Let $w$ be the water added: $\dfrac{36}{300+w}=0.08\Rightarrow 300+w=450\Rightarrow w=150$.",
 why=r"Subtracting $12-8=4\%$ of $300$ gives $12$. The total volume, not the acid, changes: set up acid $\div$ new total.")
item(id="C5", dom="Problem-Solving and Data Analysis", sk="One-variable data: center", lv="H", tool=C, wk="Anchor · 6B Center and Spread", opts=[r"$0.25$", r"$0.50$", r"$0.75$", r"$1.25$"], key=0, mode="grid",
 q=r"The frequency table summarizes $20$ scores.\par\medskip\centerline{\begin{tabular}{@{}l|cccc@{}}Score&2&3&5&8\\\hline Frequency&4&6&7&3\end{tabular}}\par\medskip What is the mean of the scores minus the median of the scores?",
 trick="Unpack the table: count positions, not rows",
 sol=r"Mean $=\dfrac{2(4)+3(6)+5(7)+8(3)}{20}=\dfrac{85}{20}=4.25$. The $20$ ordered scores place the $10$th at $3$ (positions $5$--$10$) and the $11$th at $5$ (positions $11$--$17$), so the median is $\dfrac{3+5}{2}=4$. Mean $-$ median $=0.25$.",
 why=r"(B) averaged the four listed scores ($4.5$). (C) used the frequency column as if it were the data (median $5$). (D) took the $10$th score alone ($3$) as the median.")
item(id="C6", dom="Problem-Solving and Data Analysis", sk="One-variable data: spread", lv="M", tool=N, wk="Anchor · 6B Center and Spread",
 opts=[r"Set $B$ has a greater median and a greater mean than set $A$.", r"Sets $A$ and $B$ have the same mean, but set $B$ has the greater standard deviation.",
       r"Sets $A$ and $B$ have the same median and the same range.", r"Sets $A$ and $B$ have the same median, but set $B$ has the greater mean and the greater standard deviation."], key=3, mode="list",
 q=r"Set $A$: $12,\ 14,\ 15,\ 16,\ 18$. \quad Set $B$: $12,\ 14,\ 15,\ 16,\ 38$.\par\smallskip Set $B$ is set $A$ with the greatest value changed. Which statement is true?",
 trick="Resistant versus non-resistant measures",
 sol=r"Both sets have median $15$ (the middle value is untouched). The mean of $A$ is $15$; the mean of $B$ is $19$. The range grows from $6$ to $26$ and the data are more spread out, so the standard deviation of $B$ is greater. Only (D) is entirely true.",
 why=r"(A) the median does not move. (B) the mean does move. (C) the range goes from $6$ to $26$. One outlier shifts the mean, the range and the standard deviation but not the median.")
item(id="C7", dom="Problem-Solving and Data Analysis", sk="One-variable data: distributions", lv="H", tool=C, wk="Anchor · 6B Center and Spread", opts=[r"$18$", r"$20$", r"$23$", r"$28$"], key=0, mode="grid",
 q=r"The histogram shows the distribution of $20$ values. Each interval includes its left endpoint but not its right endpoint, so a value of $10$ is counted in the $10$--$20$ interval.\HIST\par\smallskip What is the least possible value of the mean of the $20$ values?",
 trick="Bounds from grouped data: use the left endpoints",
 sol=r"The mean is smallest when every value sits at the left end of its interval: $\dfrac{0(2)+10(5)+20(9)+30(3)+40(1)}{20}=\dfrac{360}{20}=18$.",
 why=r"(B) lower bound of the median interval. (C) used midpoints ($23$), an estimate and not the least possible value. (D) used the right endpoints ($28$), which gives the greatest possible mean.")
item(id="C8", dom="Problem-Solving and Data Analysis", sk="One-variable data: box plots", lv="H", tool=N, wk="Anchor · 6B Center and Spread",
 opts=[r"The range of the scores in class $Y$ is greater than the range of the scores in class $X$.", r"The interquartile range of class $X$ is more than twice the interquartile range of class $Y$.",
       r"The median score of class $X$ is less than the median score of class $Y$.", r"At least half of the scores in class $Y$ are greater than $72$."], key=1, mode="list",
 q=r"The box plots show the scores of two classes on the same test.\BOX\par\smallskip Which of the following statements is supported by the box plots?",
 trick="IQR from the box edges, never the whiskers",
 sol=r"Class $X$: IQR $=80-55=25$. Class $Y$: IQR $=72-60=12$, and $2(12)=24<25$, so (B) is true. (A) is false: the ranges are $96-40=56$ and $90-50=40$. (C) is false: $68>64$. (D) is false: $72$ is the third quartile, so only about $25\%$ of the scores are above it.",
 why=r"(A) compared the ends of the whiskers the wrong way round. (C) misread which median is higher. (D) used the third quartile as if it were the median.")
item(id="C9", dom="Problem-Solving and Data Analysis", sk="One-variable data: spread", lv="M", tool=C, wk="Anchor · 6B Center and Spread",
 opts=[r"mean $55$, standard deviation $9$", r"mean $55$, standard deviation $4$", r"mean $60$, standard deviation $9$", r"mean $55$, standard deviation $14$"], key=0, mode="list",
 q=r"A data set has mean $40$ and standard deviation $6$. Each value in the data set is multiplied by $1.5$, and then $5$ is subtracted from the result. What are the mean and the standard deviation of the new data set?",
 trick="A shift moves the center only; a scale moves both",
 sol=r"Mean: $1.5(40)-5=55$. Standard deviation: multiplying scales the spread by $1.5$ but subtracting a constant does not change it: $1.5(6)=9$.",
 why=r"(B) subtracted $5$ from the standard deviation. (C) forgot to subtract $5$ from the mean. (D) added $5$ to the standard deviation.")
item(id="C10", dom="Problem-Solving and Data Analysis", sk="Units and conversion", lv="M", tool=C, wk="Spiral · Week 5", opts=[r"$3.3$", r"$10.7$", r"$114.8$", r"$376.5$"], key=3, mode="grid",
 q=r"A rectangular floor measures $7$ meters by $5$ meters. If $1$ meter is approximately $3.28$ feet, which of the following is closest to the area of the floor, in square feet?",
 trick="Square the conversion factor for area",
 sol=r"The area is $35$ m$^2$. One square meter is $(3.28)^2\approx10.76$ square feet, so the area is $35\times10.76\approx376.5$ ft$^2$.",
 why=r"(C) multiplied by $3.28$ once. (B) divided by $3.28$. (A) divided by $3.28^2$. Only the squared factor converts an area.")
item(id="C11", dom="Problem-Solving and Data Analysis", sk="Two-variable data: models", lv="M", tool=C, wk="Seed · Week 7 Scatterplots", spr=True, ans="5.2",
 q=r"A line of best fit for a scatterplot of hours studied, $x$, and exam score, $y$, is $\hat y=3.2x+15$. A student who studied $6$ hours scored $29$. What is the absolute difference between the student's actual score and the score predicted by the line?",
 trick="Residual = actual $-$ predicted",
 sol=r"Predicted: $3.2(6)+15=34.2$. Actual: $29$. The residual is $29-34.2=-5.2$, so the absolute difference is $5.2$.",
 why=r"Students who answer $-5.2$ report a signed residual; the question asks for the absolute difference.")
item(id="C12", dom="Problem-Solving and Data Analysis", sk="Probability", lv="M", tool=C, wk="Seed · Week 7 Probability", opts=[r"$\dfrac{19}{132}$", r"$\dfrac{19}{66}$", r"$\dfrac{25}{72}$", r"$\dfrac{5}{12}$"], key=1, mode="grid",
 q=r"A bag contains $5$ red, $4$ blue and $3$ green marbles. Two marbles are drawn at random, one after the other, without replacement. What is the probability that both marbles are the same color?",
 trick="Without replacement shrinks the denominator",
 sol=r"Same-color pairs: $\dbinom52+\dbinom42+\dbinom32=10+6+3=19$. All pairs: $\dbinom{12}{2}=66$. The probability is $\dfrac{19}{66}$. Equivalent: $\dfrac{5}{12}\cdot\dfrac{4}{11}+\dfrac{4}{12}\cdot\dfrac{3}{11}+\dfrac{3}{12}\cdot\dfrac{2}{11}=\dfrac{38}{132}$.",
 why=r"(A) $19/132$ counts pairs but divides by ordered pairs. (C) $25/72$ is the answer with replacement. (D) $5/12$ is just $P(\text{red})$.")
item(id="C13", dom="Problem-Solving and Data Analysis", sk="Inference and margin of error", lv="M", tool=N, wk="Seed · Week 7 Inference",
 opts=[r"Exactly $54\%$ of all registered voters in the city support the new bike lane.", r"Between $50\%$ and $58\%$ of the $600$ voters in the sample support the new bike lane.",
       r"It is plausible that between $50\%$ and $58\%$ of all registered voters in the city support the new bike lane.", r"It is certain that between $50\%$ and $58\%$ of all registered voters in the city support the new bike lane."], key=2, mode="list",
 q=r"A random sample of $600$ registered voters in a city was asked whether they support a new bike lane. $54\%$ of the sample said yes. The margin of error for this estimate was $4$ percentage points at a $95\%$ confidence level. Which of the following is the most appropriate conclusion?",
 trick="Sample statistic versus population claim",
 sol=r"The sample result is $54\%$ exactly. The margin of error builds an interval for the \emph{population}: $54\pm4$, i.e.\ $50\%$ to $58\%$. At $95\%$ confidence the interval is plausible, not certain. (C) is the only claim that is about the population and is worded as plausible.",
 why=r"(A) treats a sample percent as the population value. (B) puts the interval on the sample, whose result is exactly $54\%$. (D) turns ``plausible'' into ``certain''.")
item(id="D1", dom="Geometry and Trigonometry", sk="Right triangles and trigonometry", lv="M", tool=N, wk="Seed · Week 8 Trigonometry", spr=True, ans="90",
 q=r"In right triangle $PQR$, angle $Q$ is the right angle, $\tan P=\dfrac{5}{12}$, and $PR=39$. What is the perimeter of triangle $PQR$?",
 trick="Scale the Pythagorean triple",
 sol=r"$\tan P=\dfrac{QR}{PQ}=\dfrac{5}{12}$, so the legs are $5k$ and $12k$ and the hypotenuse is $13k$ (the $5$-$12$-$13$ triple). $13k=39\Rightarrow k=3$. The legs are $15$ and $36$. Perimeter $=15+36+39=90$.",
 why=r"Taking $39$ as a leg, or reading $\tan P$ as opposite over hypotenuse, breaks the scaling. $PR$ is the hypotenuse because it lies opposite the right angle at $Q$.")
item(id="D2", dom="Geometry and Trigonometry", sk="Circles", lv="H", tool=N, wk="Seed · Week 8 Circles", spr=True, ans="23",
 q=r"The equation $x^{2}+y^{2}-6x+4y=k$ represents a circle in the $xy$-plane with radius $6$. What is the value of $k$?",
 trick="Complete the square on both variables",
 sol=r"Add $\left(\frac{-6}{2}\right)^2=9$ and $\left(\frac{4}{2}\right)^2=4$ to both sides: $(x-3)^2+(y+2)^2=k+13$. The radius is $6$, so $k+13=36$ and $k=23$.",
 why=r"Setting $k=36$ forgets the $9+4$ added to complete the squares; $k=49$ adds $13$ instead of subtracting it.")
item(id="D3", dom="Geometry and Trigonometry", sk="Area and volume", lv="M", tool=C, wk="Seed · Week 9 Solids", opts=[r"$36\pi$", r"$72\pi$", r"$108\pi$", r"$144\pi$"], key=3, mode="grid",
 q=r"A sphere has a volume of $288\pi$ cubic centimeters. What is the surface area of the sphere, in square centimeters?",
 trick="Volume to radius to surface area",
 sol=r"$\dfrac43\pi r^3=288\pi\Rightarrow r^3=216\Rightarrow r=6$. Surface area $=4\pi r^2=4\pi(36)=144\pi$.",
 why=r"(A) $\pi r^2$: the area of a great circle. (B) $2\pi r^2$. (C) $3\pi r^2$: the closed hemisphere. The sphere needs $4\pi r^2$.")

assert len(ITEMS) == 22
assert [i["id"] for i in ITEMS] == ["A1","A2","A3","B1","B2","B3","C1","C2","C3","C4","C5","C6","C7","C8","C9","C10","C11","C12","C13","D1","D2","D3"]

# ------------------------------------------------------------------ structural checks
from collections import Counter
mc = [i for i in ITEMS if "opts" in i]
spr = [i for i in ITEMS if i.get("spr")]
chk("15 MCQ + 7 SPR", len(mc) == 15 and len(spr) == 7)
for i in ITEMS:
    assert i["trick"] and i["sol"] and i["why"], i["id"]
    if "opts" in i:
        assert len(i["opts"]) == 4 and len(set(i["opts"])) == 4 and 0 <= i["key"] < 4
cnt = Counter("ABCD"[i["key"]] for i in mc)
print("answer letters", dict(sorted(cnt.items())))
chk("letter balance 4/4/4/3", sorted(cnt.values()) == [3, 4, 4, 4])
seq = [("ABCD"[i["key"]]) for i in mc]
chk("no three identical letters in a row", not any(seq[j] == seq[j+1] == seq[j+2] for j in range(len(seq)-2)))
print("SPR answers", [(i["id"], i["ans"]) for i in spr])
print("tools", Counter(i["tool"] for i in ITEMS), "levels", Counter(i["lv"] for i in ITEMS))
print("origin", Counter(i["wk"].split(" · ")[0] for i in ITEMS))
