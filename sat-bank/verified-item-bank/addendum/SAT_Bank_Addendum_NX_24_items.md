[Math Department Logo] | Mr. Malek Thiab | [Dar Alfikr School Logo]

# SAT Math Bank — Addendum NX (24 items, Oct 2026)

**Teacher of Record:** Mr. Malek Thiab  
**Scope:** SAT Math, Grades 10–11  
**Items:** 24 (all answers script-verified in `build_nx.py`)  
**Origin:** original rewrites of skills seen in SATQuestionBank.org, Schoolhouse.world, College Board SAT Practice Test 1 (2016) and the erikthered.com Hard Quiz; none of the source stems, numbers or options are reproduced.  
**Note:** NX-08 corrects the source answer (asks for $x$, not the constant).

---

### NX-01
**Skill:** Rational exponents / radicals | **Difficulty:** Hard | **Format:** Multiple Choice
**Source:** House-authored rewrite — SATQuestionBank skill pattern

**Question:** For all positive values of $n$, $\sqrt[4]{90n}\,\left(\sqrt[6]{90n}\right)^{3}=(90n)^{20x}$. What is the value of $x$?

A) $\dfrac{1}{160}$
B) $\dfrac{1}{48}$
C) $\dfrac{3}{80}$
D) $\dfrac{13}{80}$

**Correct Answer:** C

**Rationale:** Rewrite each radical as a power: $\sqrt[4]{90n}=(90n)^{1/4}$ and $\left(\sqrt[6]{90n}\right)^3=(90n)^{3/6}=(90n)^{1/2}$. Same base, so add exponents: $\dfrac14+\dfrac12=\dfrac34$. Then $20x=\dfrac34$, so $x=\dfrac{3}{80}$. **Desmos:** type `1/4+1/2` to confirm $0.75$, then `0.75/20` gives $0.0375=\frac{3}{80}$.

**Misconception addressed:** Students multiply the exponents ($\frac14\cdot\frac12$) instead of adding, or drop the cube on the sixth root.

---

### NX-02
**Skill:** Equivalent expressions: matching coefficients | **Difficulty:** Hard | **Format:** Multiple Choice
**Source:** House-authored rewrite — SATQuestionBank skill pattern

**Question:** $(ax+2)(2x^2-bx+5)=6x^3-8x^2+7x+10$ for all values of $x$, where $a$ and $b$ are constants. What is the value of $ab$?

A) $3$
B) $4$
C) $7$
D) $12$

**Correct Answer:** D

**Rationale:** Match the $x^3$ terms: $2a=6$, so $a=3$. Match the $x^2$ terms: $-ab+4=-8$, so $ab=12$ (and $b=4$). Check the $x$ terms: $5a-2b=15-8=7$ ✓. The question asks for the product, so the answer is $12$. **Desmos:** type `(3x+2)(2x^2-4x+5)` and `6x^3-8x^2+7x+10` and confirm the graphs coincide.

**Misconception addressed:** Students stop after finding $a=3$ or $b=4$, or answer with $a+b=7$ instead of $ab$.

---

### NX-03
**Skill:** Solids: cone volume and slant height | **Difficulty:** Hard | **Format:** Multiple Choice
**Source:** House-authored rewrite — SATQuestionBank skill pattern

**Question:** A right circular cone has volume $6{,}144\pi$ cubic centimeters and a base with area $576\pi$ square centimeters. What is the slant height, in centimeters, of the cone?

A) $24$
B) $32$
C) $40$
D) $56$

**Correct Answer:** C

**Rationale:** Base area: $\pi r^2=576\pi$, so $r=24$. Volume: $\dfrac13\pi r^2h=6144\pi$ gives $\dfrac13(576)h=6144$, so $h=32$. Slant height: $\sqrt{24^2+32^2}=\sqrt{1600}=40$. **Desmos:** type `sqrt(24^2+32^2)` to get $40$.

**Misconception addressed:** Students answer with the height $32$, or add $r+h=56$, instead of using the Pythagorean theorem.

---

### NX-04
**Skill:** Density and units: cube root | **Difficulty:** Hard | **Format:** Student-Produced Response
**Source:** House-authored rewrite — SATQuestionBank skill pattern

**Question:** A solid cube of metal has density $2.7$ grams per cubic centimeter and mass $2{,}500$ grams. What is the length, in centimeters, of one edge of the cube? (Round your answer to the nearest hundredth.)

**Correct Answer:** 9.75

**Rationale:** Density $=\dfrac{\text{mass}}{\text{volume}}$, so $V=\dfrac{2500}{2.7}\approx925.93$ cm$^3$. For a cube $V=s^3$, so $s=\sqrt[3]{925.93}\approx9.75$. **Desmos:** type `(2500/2.7)^(1/3)`.

**Misconception addressed:** Students take the square root of the volume, or stop at the volume $925.93$.

---

### NX-05
**Skill:** Exponential decay: percent change | **Difficulty:** Medium | **Format:** Multiple Choice
**Source:** House-authored rewrite — SATQuestionBank skill pattern

**Question:** A delivery van was bought for $\$18{,}000$ and loses $15\%$ of its value each year. Which of the following is closest to its value, in dollars, after $3$ years?

A) $9{,}900$
B) $11{,}054$
C) $15{,}300$
D) $7{,}650$

**Correct Answer:** B

**Rationale:** Each year the value is multiplied by $0.85$, so $V=18000(0.85)^3\approx11{,}054$. **Desmos:** type `18000*0.85^3`.

**Misconception addressed:** Students subtract $15\%$ of the original three times (linear decay, giving $9{,}900$) or multiply by $0.85$ only once.

---

### NX-06
**Skill:** Exponential functions: base to percent rate | **Difficulty:** Hard | **Format:** Multiple Choice
**Source:** House-authored rewrite — Schoolhouse.world skill pattern

**Question:** The function $f(x)=(2.25)^{x/3}$ can be rewritten as $f(x)=\left(1+\dfrac{p}{100}\right)^{x}$. Which of the following is closest to the value of $p$?

A) $31$
B) $42$
C) $75$
D) $125$

**Correct Answer:** A

**Rationale:** $(2.25)^{x/3}=\left(2.25^{1/3}\right)^x$, so $1+\dfrac{p}{100}=2.25^{1/3}\approx1.3104$ and $p\approx31$. **Desmos:** type `(2.25^(1/3)-1)*100`.

**Misconception addressed:** Students divide $125\%$ by $3$ to get about $42$, or read the exponent's $\frac13$ as a percent change.

---

### NX-07
**Skill:** Exponential models: interpreting the rate period | **Difficulty:** Hard | **Format:** Multiple Choice
**Source:** House-authored rewrite — Schoolhouse.world skill pattern

**Question:** The population of a bacteria colony is modeled by $P(t)=480(1.05)^{\frac{3}{4}t}$, where $P$ is the population and $t$ is the time in years since the colony was started. The population increases by $5\%$ every $n$ months. What is the value of $n$?

A) $9$
B) $12$
C) $16$
D) $48$

**Correct Answer:** C

**Rationale:** The population is multiplied by $1.05$ when the exponent $\dfrac34t$ increases by $1$, i.e. when $t=\dfrac43$ years $=\dfrac43\times12=16$ months. **Desmos:** graph `480*1.05^(0.75x)`; the population at $x=\frac43$ is $1.05$ times the starting value.

**Misconception addressed:** Students convert $\frac34$ year to $9$ months instead of inverting it, or answer $12$ because the model is in years.

---

### NX-08
**Skill:** Quadratic-linear systems: tangency | **Difficulty:** Hard | **Format:** Multiple Choice
**Source:** House-authored rewrite — Schoolhouse.world skill pattern (answer corrected)

**Question:** The graphs of $y=2x^2-18x+60$ and $y=2x+k$ intersect at exactly one point $(x,y)$ in the $xy$-plane, where $k$ is a constant. What is the value of $x$?

A) $2$
B) $5$
C) $10$
D) $20$

**Correct Answer:** B

**Rationale:** Set equal: $2x^2-20x+(60-k)=0$. One intersection means discriminant $=0$: $400-8(60-k)=0$, so $k=10$. The repeated root is $x=\dfrac{20}{2(2)}=5$. The constant $k=10$ is **not** what is asked. **Desmos:** graph the parabola and `y=2x+k` with a slider for $k$; at $k=10$ the line touches the parabola at $x=5$.

**Misconception addressed:** Students stop at $k=10$ and answer with the constant instead of the $x$-coordinate of the intersection.

---

### NX-09
**Skill:** Systems of linear equations: no solution | **Difficulty:** Hard | **Format:** Multiple Choice
**Source:** House-authored rewrite — Schoolhouse.world skill pattern

**Question:** $30x-45y=20y+15$ and $ry=\dfrac13-6x$. In the system above, $r$ is a constant. For what value of $r$ does the system have no solution?

A) $-13$
B) $13$
C) $-5$
D) $-65$

**Correct Answer:** A

**Rationale:** Write both in the form $Ax+By=C$: $30x-65y=15$ and $6x+ry=\dfrac13$. Multiply the second by $5$: $30x+5ry=\dfrac53$. For no solution the $x$-coefficients match and the $y$-coefficients match: $5r=-65$, so $r=-13$. The constants $15$ and $\dfrac53$ differ, so the lines are parallel, not identical. **Desmos:** graph both lines with `r` as a slider; they are parallel at $r=-13$.

**Misconception addressed:** Students forget to multiply the second equation (matching $r=-65$) or forget to move $20y$ to the left side.

---

### NX-10
**Skill:** Equivalent expressions: adding rational expressions | **Difficulty:** Hard | **Format:** Multiple Choice
**Source:** House-authored rewrite — Schoolhouse.world skill pattern

**Question:** Which of the following expressions is equivalent to $\dfrac{y+9}{x-5}+\dfrac{y(x-5)}{x^2y-5xy}$?

A) $\dfrac{xy+y+9}{x^2y-5xy+x-5}$
B) $\dfrac{xy+9+y(x-5)}{x^2y-4xy-5}$
C) $\dfrac{xy^2+9xy-5y}{x^2y-5xy}$
D) $\dfrac{xy^2+10xy-5y}{x^2y-5xy}$

**Correct Answer:** D

**Rationale:** Factor the second denominator: $x^2y-5xy=xy(x-5)$, so the second term is $\dfrac{y(x-5)}{xy(x-5)}=\dfrac1x$. Now $\dfrac{y+9}{x-5}+\dfrac1x=\dfrac{x(y+9)+(x-5)}{x(x-5)}=\dfrac{xy+10x-5}{x^2-5x}$. Multiply top and bottom by $y$: $\dfrac{xy^2+10xy-5y}{x^2y-5xy}$. **Desmos:** graph the original and each option (use `x` for the variable and set `y=3`); only option D overlaps.

**Misconception addressed:** Students add numerators and denominators separately, or forget that cancelling $(x-5)$ leaves a factor of $x$ in the new denominator.

---

### NX-11
**Skill:** Circles: right angle at the center | **Difficulty:** Hard | **Format:** Multiple Choice
**Source:** House-authored rewrite — Schoolhouse.world skill pattern

**Question:** A circle in the $xy$-plane has center $C(h,k)$. Point $A$ has coordinates $\left(h+1,\,k+\sqrt{74}\right)$ and lies on the circle. Point $B$ is also on the circle, and $\angle ACB=90^\circ$. What is the length of $\overline{AB}$?

A) $5\sqrt{3}$
B) $5\sqrt{6}$
C) $10\sqrt{3}$
D) $75$

**Correct Answer:** B

**Rationale:** The radius is $CA=\sqrt{1^2+(\sqrt{74})^2}=\sqrt{75}=5\sqrt3$. Triangle $ACB$ is an isosceles right triangle with legs $5\sqrt3$, so $AB=5\sqrt3\cdot\sqrt2=5\sqrt6$. **Desmos:** type `sqrt(2*75)` to get $12.247$ and compare with `5*sqrt(6)`.

**Misconception addressed:** Students give the radius $5\sqrt3$ as the chord, or square the radius to get $75$.

---

### NX-12
**Skill:** Equivalent expressions: matching coefficients, two cases | **Difficulty:** Hard | **Format:** Multiple Choice
**Source:** House-authored rewrite — SAT Practice Test 1 (2016) skill pattern

**Question:** $(ax+3)(bx+4)=24x^2+cx+12$ for all values of $x$. If $a+b=11$, what are the two possible values of $c$?

A) $24$ and $11$
B) $33$ and $44$
C) $36$ and $41$
D) $12$ and $24$

**Correct Answer:** C

**Rationale:** Expanding gives $ab=24$ and $c=4a+3b$. With $a+b=11$ and $ab=24$, $\{a,b\}=\{3,8\}$. If $(a,b)=(3,8)$, $c=12+24=36$. If $(a,b)=(8,3)$, $c=32+9=41$. **Desmos:** graph `y=x^2-11x+24` to see the roots $3$ and $8$, then evaluate `4a+3b` for each order.

**Misconception addressed:** Students find only one assignment of $a$ and $b$; the order matters because the two factors have different constants.

---

### NX-13
**Skill:** Equivalent expressions: complex fractions | **Difficulty:** Hard | **Format:** Multiple Choice
**Source:** House-authored rewrite — SAT Practice Test 1 (2016) skill pattern

**Question:** If $x>0$, which of the following is equivalent to $\dfrac{1}{\dfrac{1}{x+4}+\dfrac{1}{x+6}}$?

A) $\dfrac{2x+10}{x^2+10x+24}$
B) $2x+10$
C) $\dfrac{x^2+10x+24}{2x+10}$
D) $x^2+10x+24$

**Correct Answer:** C

**Rationale:** $\dfrac{1}{x+4}+\dfrac{1}{x+6}=\dfrac{2x+10}{(x+4)(x+6)}$. The reciprocal is $\dfrac{(x+4)(x+6)}{2x+10}=\dfrac{x^2+10x+24}{2x+10}$. **Desmos:** graph the original and option C; they coincide. Option A is the reciprocal and does not.

**Misconception addressed:** Students stop after combining the fractions and forget to take the reciprocal (choosing A).

---

### NX-14
**Skill:** Exponent rules: common base | **Difficulty:** Hard | **Format:** Multiple Choice
**Source:** House-authored rewrite — SAT Practice Test 1 (2016) skill pattern

**Question:** If $3x-2y=8$, what is the value of $\dfrac{27^{x}}{9^{y}}$?

A) $3^{8}$
B) $3^{11}$
C) $3^{5}$
D) $3^{16}$

**Correct Answer:** A

**Rationale:** $27^x=3^{3x}$ and $9^y=3^{2y}$, so $\dfrac{27^x}{9^y}=3^{3x-2y}=3^{8}=6561$. **Desmos:** pick $x=4,\ y=2$ (which satisfies $12-4=8$): `27^4/9^2` gives $6561$.

**Misconception addressed:** Students multiply or add the exponents ($3x+2y$), or try to solve for $x$ and $y$ separately.

---

### NX-15
**Skill:** Percentages: successive discount and tax | **Difficulty:** Medium | **Format:** Multiple Choice
**Source:** House-authored rewrite — SAT Practice Test 1 (2016) skill pattern

**Question:** A student bought a tablet at a store that gave a $25\%$ discount off the original price. The total amount paid, including a $6\%$ sales tax on the discounted price, was $p$ dollars. Which of the following represents the original price of the tablet, in terms of $p$?

A) $0.81p$
B) $\dfrac{p}{0.81}$
C) $(0.75)(1.06)p$
D) $\dfrac{p}{(0.75)(1.06)}$

**Correct Answer:** D

**Rationale:** Paid $=\text{original}\times0.75\times1.06$, so original $=\dfrac{p}{(0.75)(1.06)}$. **Desmos:** test with an original price of $100$: `100*0.75*1.06 = 79.5`; then `79.5/(0.75*1.06)` returns $100$.

**Misconception addressed:** Students combine the rates as $-25\%+6\%$ (giving $0.81$) and multiply instead of divide.

---

### NX-16
**Skill:** Data: average rate of change from a table, units | **Difficulty:** Medium | **Format:** Multiple Choice
**Source:** House-authored rewrite — SAT Practice Test 1 (2016) skill pattern

**Question:** The table shows the annual public-transit budget of a city, in thousands of dollars.

| Year | 2019 | 2020 | 2021 |
|---|---|---|---|
| Budget (thousands of dollars) | $412{,}300$ | $466{,}100$ | $518{,}900$ |

Which of the following best approximates the average rate of change of the budget from 2019 to 2021?

A) $\$53{,}300$ per year
B) $\$53{,}300{,}000$ per year
C) $\$106{,}600{,}000$ per year
D) $\$53{,}300{,}000{,}000$ per year

**Correct Answer:** B

**Rationale:** Change in budget $=518{,}900-412{,}300=106{,}600$ thousand dollars over $2$ years $=53{,}300$ thousand dollars per year $=\$53{,}300{,}000$ per year. **Desmos:** type `(518900-412300)/2*1000`.

**Misconception addressed:** Students forget the table is in thousands (choosing A), or divide by $1$ instead of $2$ years (choosing C).

---

### NX-17
**Skill:** Inference: sample to population | **Difficulty:** Medium | **Format:** Multiple Choice
**Source:** House-authored rewrite — SAT Practice Test 1 (2016) skill pattern

**Question:** A rectangular field measures $20$ meters by $20$ meters. Eight students each mark off a different randomly selected, non-overlapping square region of the field, $1$ meter on each side, and count the snails in it. The counts were $21, 25, 18, 24, 22, 27, 19,$ and $24$. Which of the following is a reasonable estimate of the number of snails in the entire field?

A) $900$
B) $9{,}000$
C) $90{,}000$
D) $900{,}000$

**Correct Answer:** B

**Rationale:** Mean per square meter $=\dfrac{180}{8}=22.5$. The field has area $400$ m$^2$, so the estimate is $22.5\times400=9{,}000$. **Desmos:** type `mean(21,25,18,24,22,27,19,24)*400`.

**Misconception addressed:** Students multiply by the $8$ sampled regions instead of the field area, or misplace a power of ten.

---

### NX-18
**Skill:** Polynomials: remainder theorem | **Difficulty:** Medium | **Format:** Multiple Choice
**Source:** House-authored rewrite — SAT Practice Test 1 (2016) skill pattern

**Question:** For a polynomial $p(x)$, the value of $p(-2)$ is $7$. Which of the following must be true about $p(x)$?

A) $x-7$ is a factor of $p(x)$.
B) $x+7$ is a factor of $p(x)$.
C) $x-2$ is a factor of $p(x)$.
D) The remainder when $p(x)$ is divided by $x+2$ is $7$.

**Correct Answer:** D

**Rationale:** By the remainder theorem, the remainder when $p(x)$ is divided by $x-c$ is $p(c)$. With $c=-2$, dividing by $x+2$ leaves remainder $p(-2)=7$. A factor would require $p=0$ at that point, which none of the options give. **Desmos:** try $p(x)=x^2+3$: `p(-2)=7`; $x+2$ is not a factor since the remainder is not $0$.

**Misconception addressed:** Students confuse the value $p(c)$ with a factor, or use the wrong sign of $c$ (choosing $x-2$).

---

### NX-19
**Skill:** Systems of linear inequalities | **Difficulty:** Medium | **Format:** Multiple Choice
**Source:** House-authored rewrite — SAT Practice Test 1 (2016) skill pattern

**Question:** If the system of inequalities $y\ge3x+2$ and $y>\dfrac13x-2$ is graphed in the $xy$-plane, which quadrant contains no solutions to the system?

A) Quadrant I
B) Quadrant II
C) Quadrant III
D) Quadrant IV

**Correct Answer:** D

**Rationale:** In Quadrant IV, $x>0$ and $y<0$. But $y\ge3x+2>2$ whenever $x>0$, which contradicts $y<0$. So there are no solutions in Quadrant IV; the other three quadrants each contain solutions (for example $(1,6)$, $(-1,1)$ and $(-3,-1)$). **Desmos:** graph both inequalities; the shaded region never enters the lower right.

**Misconception addressed:** Students test only the origin, or sketch the lines without noting that the steeper line forces $y>2$ for every $x>0$.

---

### NX-20
**Skill:** Statistics: mean with constraints | **Difficulty:** Hard | **Format:** Multiple Choice
**Source:** House-authored rewrite — Hard-practice-quiz skill pattern

**Question:** Three positive integers have a mean of $80$. Which of the following CANNOT be one of the three integers?

A) $1$
B) $237$
C) $238$
D) $239$

**Correct Answer:** D

**Rationale:** The sum is $3\times80=240$. The other two integers are each at least $1$, so the largest possible integer is $240-1-1=238$. Therefore $239$ is impossible. **Desmos:** type `240-2` to get $238$.

**Misconception addressed:** Students think the maximum equals the total ($240$) or forget the other two integers must be positive.

---

### NX-21
**Skill:** Statistics: effect of replacing a value on the mean | **Difficulty:** Medium | **Format:** Multiple Choice
**Source:** House-authored rewrite — Hard-practice-quiz skill pattern

**Question:** The mean of a set of $6$ numbers is $20$. When one of the numbers is replaced by $8$, the mean of the set becomes $23$. What number was replaced?

A) $-10$
B) $-2$
C) $8$
D) $28$

**Correct Answer:** A

**Rationale:** Original sum $=6\times20=120$; new sum $=6\times23=138$. The sum rose by $18$ even though the replacement is $8$, so the removed number was $8-18=-10$. **Desmos:** type `8-(23*6-20*6)`.

**Misconception addressed:** Students think a higher mean means a smaller replacement, or forget to multiply the mean change by the number of values.

---

### NX-22
**Skill:** Integers: perfect squares and prime factorization | **Difficulty:** Hard | **Format:** Multiple Choice
**Source:** House-authored rewrite — Hard-practice-quiz skill pattern

**Question:** The positive integers $m$ and $n$ satisfy $mn>12$. If $12mn$ is a perfect square, what is the least possible value of $mn$?

A) $12$
B) $24$
C) $27$
D) $36$

**Correct Answer:** C

**Rationale:** $12=2^2\cdot3$, so $12mn$ is a perfect square exactly when $mn$ supplies another factor of $3$: $mn=3k^2$. The values $3, 12, 27,\dots$ occur for $k=1,2,3$. Since $mn>12$, the least value is $27$ (and $12\cdot27=324=18^2$). **Desmos:** type `12*27` to get $324$ and `sqrt(324)` to get $18$.

**Misconception addressed:** Students pick $12$ (not allowed since $mn>12$) or choose $24$, which gives $288$, not a square.

---

### NX-23
**Skill:** Triangles: equilateral, area and perimeter | **Difficulty:** Hard | **Format:** Multiple Choice
**Source:** House-authored rewrite — Hard-practice-quiz skill pattern

**Question:** The perimeter of an equilateral triangle, in inches, is numerically equal to its area, in square inches. What is the side length of the triangle, in inches?

A) $4$
B) $4\sqrt{3}$
C) $12$
D) $12\sqrt{3}$

**Correct Answer:** B

**Rationale:** For side $s$: perimeter $=3s$ and area $=\dfrac{\sqrt3}{4}s^2$. Setting $3s=\dfrac{\sqrt3}{4}s^2$ gives $s=\dfrac{12}{\sqrt3}=4\sqrt3$. **Desmos:** graph `y=3x` and `y=(sqrt(3)/4)x^2`; they meet at $x\approx6.93=4\sqrt3$.

**Misconception addressed:** Students give the perimeter $12\sqrt3$ (the wrong quantity) or forget the area formula contains $\sqrt3$.

---

### NX-24
**Skill:** Triangles: third-side rule with ranges | **Difficulty:** Hard | **Format:** Multiple Choice
**Source:** House-authored rewrite — Hard-practice-quiz skill pattern

**Question:** Two sides of a triangle have lengths $x$ and $y$, where $2<x<6$ and $10<y<14$. Which of the following represents all possible values of the third side $z$?

A) $4<z<20$
B) $4<z<16$
C) $8<z<20$
D) $0<z<20$

**Correct Answer:** A

**Rationale:** The third side satisfies $y-x<z<x+y$. The largest possible $x+y$ is just under $6+14=20$, so $z<20$. The smallest possible $y-x$ is just over $10-6=4$, so $z>4$. Therefore $4<z<20$. **Desmos:** type `10-6` and `6+14`.

**Misconception addressed:** Students use $|x-y|$ with the wrong endpoints (e.g. $14-6=8$), or use $0$ as the lower bound.

---
