[Math Department Logo] | Mr. Malek Thiab | [Dar Alfikr School Logo]

# SAT Bank — Student-Recalled 2026 Reports + Hard Module 2 Archetypes (Nov 2026)

**Added:** 17 Nov 2026. 14 new items: A-346 to A-348, AM-344 to AM-350, GT-278 to GT-279, PS-214 to PS-215.
**Sources:** (1) "2026 Digital SAT Math: Student-Recalled Questions" (Aug–Nov 2026 reconstructions); (2) "Digital SAT Math Hard Module 2 Archetypes".
**Method:** archetype only. Numbers changed from the recalled versions, wording original, no Saudi context (SAT rule). Every answer checked by script. Each candidate was screened against the existing bank (about 1,210 items in the Verified Item Bank) by keyword search and by reading the closest hits.
**Merge note:** these items follow the bank's ID sequence (last IDs were A-345, AM-343, GT-277, PS-213). Append them to the Verified Item Bank file when it is next rebuilt.

## Screening result

| Candidate | Source | Decision | Reason |
|---|---|---|---|
| Shifted-table quadratic regression | Recalled 1.1 | **Added** AM-350 | no shifted-table item |
| Chained % concentration (DI water and sodium) | Recalled 1.2 | **Added** PS-214 | sub-volume chain not in bank |
| "A is p% of C, C is q% of B" chain | Recalled 1.3 | **Added** PS-215 | no percent-of-percent with "less/greater than" |
| Stars M and K graph, scale reading | Recalled 1.3 | Skipped | needs the original graph; scale-reading is covered |
| Circle A to circle B translation | Recalled 1.3 | Skipped | repeat of the existing circle translation and dilation item |
| tan X from leg and hypotenuse | Recalled 2.1 | **Added** GT-278 | existing tan items give two legs or a ratio |
| Parameterized integer clones, evaluate at 0 | Recalled 2.2 | Skipped | covered by existing $f(0)$ items |
| Higher-degree difference of squares | Recalled 3.1 | **Added** AM-346 | existing factor items are cubic grouping only |
| Target-shift with sign reversal | Recalled 3.2 | **Added** A-346 | not in bank |
| Triangle angles, inconsistent system | Recalled 3.3 | **Added** A-347 | not in bank |
| Symmetric output cancellation | Recalled 3.4 | **Added** AM-344 | not in bank |
| Exponent base rewriting, solve for p | Recalled 3.5 | **Added** AM-345 | not in bank |
| Quartic in $(x+4)^2$, symmetry | Recalled 4.1 | **Added** AM-347 | closest existing is a quadratic symmetry item |
| Isosceles altitude, scaled triple | Recalled 4.2 | **Added** GT-279 | not in bank |
| Tangent spheres, outer endpoints | Recalled 4.3 | **Skipped, repeat** | GT item with spheres $Q$, $P$ tangent at $T$ and $MN=2R+2r$ already in bank |
| Integer-constrained polynomial identity | Archetype A | **Skipped, repeat** | existing $6x^4+kx^2+24=(2x^2+a)(3x^2+b)$, greatest $k$ |
| Infinitely many solutions, ratio $r/s$ | Archetype B | **Skipped, repeat** | 36 existing items on the condition |
| Tangency, parabola and line, find $c$ | Archetype C | **Skipped, repeat** | existing line–parabola tangency item (find $m$) |
| Non-unit exponential period | Archetype D | **Added** AM-348 | not in bank |
| Chained percent, work back to $p$ | Archetype E | **Added** AM-349 | existing items solve for the starting value, not $p$ |
| Circle with radius parameter, find $k$ | Archetype F | **Skipped, repeat** | existing $x^2+y^2+4x-10y+k=0$ with radius 4 |
| Constant cancellation, $(p,r)$ and $(2p,5r)$ | Meta-trick | **Added** A-348 | not in bank |
| Cofunction $\sin A-\cos B$ | Meta-trick | Skipped | cofunction items already present |

**Totals:** 24 candidates screened, 14 added, 10 skipped (4 exact-pattern repeats from the Archetypes PDF, 1 repeat from the recalled list, 5 covered or not reproducible without the original figure).

**Correction to the recalled PDF:** item 3.2 prints the answer as an unreadable "$-31$". The correct reading is $15u+1=18u\Rightarrow u=\tfrac13$, so $x^2-11=-\tfrac13$ (see A-346).

---

### A-346

**Skill:** Algebra — Linear equations in one variable
**Difficulty:** Hard
**Format:** SPR
**Tool:** No calculator needed

**Source:** House variant of a student-recalled September 2026 Module 2 item (target-shift with sign reversal); numbers changed.

**Question:** If $12(7-x^2)+2=15(7-x^2)$, what is the value of $x^2-7$?

**Correct Answer:** $-\dfrac{2}{3}$

**Rationale:** Let $u=7-x^2$. Then $12u+2=15u$, so $3u=2$ and $u=\dfrac23$. The question asks for $x^2-7=-u=-\dfrac23$.

**Misconception addressed:** Students find $7-x^2=\dfrac23$ and enter it without noticing the target reverses the subtraction order.

---

### A-347

**Skill:** Algebra — Systems of two linear equations in two variables
**Difficulty:** Hard
**Format:** Multiple Choice
**Tool:** No calculator needed

**Source:** House variant of a student-recalled September 2026 Module 2 item (inconsistent system with the triangle angle sum); numbers changed.

**Question:** A triangle has angles measuring $x^\circ$, $y^\circ$ and $22^\circ$, where $x>y>22$. Which of the following equations, together with the angle sum of the triangle, would NOT be enough to determine the values of $x$ and $y$?

(A) $x-y=30$
(B) $3x+3y=474$
(C) $x=2y$
(D) $2x-y=200$

**Correct Answer:** (B)

**Rationale:** The angle sum gives $x+y=158$. Equation (B) divides to $x+y=158$, the same line, so infinitely many pairs satisfy both. The others have different $x$ and $y$ coefficient ratios and give a unique pair: (A) $x=94,\ y=64$; (C) $x=\dfrac{316}{3},\ y=\dfrac{158}{3}$; (D) $x=\dfrac{358}{3},\ y=\dfrac{116}{3}$.

**Misconception addressed:** Students solve each option fully instead of comparing coefficient ratios with $x+y=158$; some choose (C) because it "looks" proportional.

---

### A-348

**Skill:** Algebra — Linear functions
**Difficulty:** Hard
**Format:** SPR
**Tool:** No calculator needed

**Source:** House variant of the "deliberate constant cancellation" meta-trick in the Hard Module 2 Archetypes report.

**Question:** In the $xy$-plane, the point $(p,r)$ lies on the line $y=x+b$ and the point $(2p,\,5r)$ lies on the line $y=2x+b$, where $b$ is a constant and $p\ne0$. What is the value of $\dfrac{r}{p}$?

**Correct Answer:** $\dfrac{3}{4}$ (0.75)

**Rationale:** $r=p+b$ and $5r=4p+b$. Subtracting the first from the second eliminates $b$: $4r=3p$, so $\dfrac rp=\dfrac34$.

**Misconception addressed:** Students try to solve for $b$, $p$ and $r$ separately (three unknowns, two equations) instead of subtracting to cancel $b$.

---

### AM-344

**Skill:** Advanced Math — Nonlinear functions
**Difficulty:** Hard
**Format:** SPR
**Tool:** No calculator needed

**Source:** House variant of a student-recalled September 2026 Module 2 item (symmetric output cancellation); numbers changed.

**Question:** The function $f$ is defined by $f(x)=-2(x+6)+k$, where $k$ is a constant. The graph of $y=f(x)$ in the $xy$-plane passes through $(-2,t)$ and $(5,-t)$. What is the value of $k$?

**Correct Answer:** $15$

**Rationale:** $f(-2)=-8+k=t$ and $f(5)=-22+k=-t$. Adding the equations cancels $t$: $2k-30=0$, so $k=15$. (Then $t=7$.)

**Misconception addressed:** Students substitute and solve for $t$ first, which is longer; others expand $-2(x+6)$ as $-2x+6$.

---

### AM-345

**Skill:** Advanced Math — Equivalent expressions
**Difficulty:** Hard
**Format:** Multiple Choice
**Tool:** No calculator needed

**Source:** House variant of a student-recalled September 2026 Module 2 item (exponent base rewriting with a variable exponent); numbers changed.

**Question:** For all positive $m$, $q^{m/6}=\left(1+\dfrac{p}{100}\right)^{m/2}$. Which of the following expresses $p$ in terms of $q$?

(A) $100\left(q^{1/3}-1\right)$
(B) $100\left(q^{3}-1\right)$
(C) $100q^{1/3}-1$
(D) $100\left(q^{1/3}+1\right)$

**Correct Answer:** (A)

**Rationale:** Raise both sides to the power $\dfrac2m$: $q^{1/3}=1+\dfrac{p}{100}$, so $p=100\left(q^{1/3}-1\right)$.

**Misconception addressed:** Students invert the exponent ratio ($q^3$, choice B), forget to multiply the "$-1$" by $100$ (C), or add instead of subtract (D).

---

### AM-346

**Skill:** Advanced Math — Equivalent expressions
**Difficulty:** Hard
**Format:** Multiple Choice
**Tool:** No calculator needed

**Source:** House variant of a student-recalled September 2026 Module 2 item (higher-degree difference of squares); the recalled report lists the variant $(x-3)$ with $16$, used here with different structure.

**Question:** Which of the following is a factor of $y^2(x-3)-16(x-3)^3$?

(A) $y-4x+12$
(B) $y-4x+3$
(C) $y+16x-48$
(D) $y-16x+48$

**Correct Answer:** (A)

**Rationale:** Factor out $(x-3)$: $(x-3)\left[y^2-16(x-3)^2\right]$. Apply $A^2-B^2=(A-B)(A+B)$ with $A=y$ and $B=4(x-3)$: $(x-3)(y-4x+12)(y+4x-12)$. Choice (A) is the first bracket.

**Misconception addressed:** Students take $\sqrt{16}=4$ but forget to distribute it over $(x-3)$ (choice B), or leave $16$ unrooted (C and D).

---

### AM-347

**Skill:** Advanced Math — Nonlinear functions
**Difficulty:** Hard
**Format:** SPR
**Tool:** No calculator needed

**Source:** House variant of a student-recalled August 2026 Module 2 item (axis-of-symmetry quartic); numbers changed.

**Question:** For the function $f(x)=a\left[(x+4)^2-b\right]\left[(x+4)^2-c\right]$, where $a$, $b$ and $c$ are constants, $f(-6)=20$ and $f(1)=45$. What is the value of $f(-2)+f(-9)$?

**Correct Answer:** $65$

**Rationale:** $x$ appears only inside $(x+4)^2$, so the graph is symmetric about $x=-4$. $-6$ and $-2$ are each $2$ units from $-4$, so $f(-2)=f(-6)=20$. $1$ and $-9$ are each $5$ units from $-4$, so $f(-9)=f(1)=45$. The sum is $65$, with no need to find $a$, $b$ or $c$.

**Misconception addressed:** Students try to solve for $a$, $b$ and $c$ from two equations (impossible) instead of recognising the symmetry about $x=-4$.

---

### AM-348

**Skill:** Advanced Math — Nonlinear functions
**Difficulty:** Hard
**Format:** Multiple Choice
**Tool:** Calculator

**Source:** House item from the "non-unit exponential period" archetype in the Hard Module 2 Archetypes report.

**Question:** The population $N(t)$ of a bacterial culture, in thousands, is modeled by $N(t)=600(1.21)^{t/2}$, where $t$ is the number of hours since the culture was started. By what percent does the population increase each hour?

(A) $5$
(B) $10$
(C) $10.5$
(D) $21$

**Correct Answer:** (B)

**Rationale:** $(1.21)^{t/2}=\left(1.21^{1/2}\right)^t=(1.1)^t$. The hourly growth factor is $1.1$, an increase of $10\%$.

**Misconception addressed:** Students halve the two-hour growth rate ($21\%\div2=10.5\%$, choice C) instead of taking the square root of the factor; (D) reads the base directly.

---

### AM-349

**Skill:** Advanced Math — Nonlinear functions (exponential growth and decay)
**Difficulty:** Hard
**Format:** SPR
**Tool:** No calculator needed

**Source:** House item from the "working backward through chained percentages" archetype in the Hard Module 2 Archetypes report; numbers kept in the archetype's form.

**Question:** The value of an asset increased by $p\%$ from 2023 to 2024, and then decreased by $20\%$ from 2024 to 2025. If the value in 2025 was $16\%$ greater than the value in 2023, what is the value of $p$?

**Correct Answer:** $45$

**Rationale:** Take the 2023 value as $100$: $100\left(1+\dfrac{p}{100}\right)(0.80)=116$. Then $1+\dfrac{p}{100}=1.45$, so $p=45$.

**Misconception addressed:** Students add and subtract the percents ($p-20=16$, so $p=36$), ignoring that the $20\%$ decrease applies to the larger 2024 value.

---

### AM-350

**Skill:** Advanced Math — Nonlinear functions
**Difficulty:** Hard
**Format:** Multiple Choice
**Tool:** Calculator

**Source:** House item from the "shifted-table quadratic regression" pattern in the student-recalled November 2026 report.

**Question:** The table gives values of $h(x)=f(x)-5$, where $f$ is a quadratic function.

| $x$ | $1$ | $2$ | $3$ |
|---|---|---|---|
| $h(x)$ | $-5$ | $-2$ | $5$ |

What is the $y$-coordinate of the $y$-intercept of the graph of $y=f(x)$?

(A) $-5$
(B) $-4$
(C) $1$
(D) $5$

**Correct Answer:** (C)

**Rationale:** The quadratic through the table is $h(x)=2x^2-3x-4$, so $h(0)=-4$. Since $h=f-5$, $f(0)=h(0)+5=1$.

**Misconception addressed:** Students run the regression on the table and report the constant term of $h$ ($-4$, choice B) instead of adding back the vertical shift.

---

### GT-278

**Skill:** Geometry and Trigonometry — Right triangles and trigonometry
**Difficulty:** Hard
**Format:** Multiple Choice
**Tool:** No calculator needed

**Source:** House variant of a student-recalled October 2026 Module 2 item (Pythagorean setup for $\tan X$); numbers changed.

**Question:** In right triangle $XYZ$, the right angle is at $Y$, $XY=20$ and $XZ=29$. What is the value of $\tan X$?

(A) $\dfrac{20}{29}$
(B) $\dfrac{20}{21}$
(C) $\dfrac{21}{29}$
(D) $\dfrac{21}{20}$

**Correct Answer:** (D)

**Rationale:** $YZ=\sqrt{29^2-20^2}=\sqrt{441}=21$. Angle $X$ has opposite side $YZ=21$ and adjacent side $XY=20$, so $\tan X=\dfrac{21}{20}$.

**Misconception addressed:** Students compute $\cos X$ (A) or $\sin X$ (C) from the given sides, or invert the ratio (B).

---

### GT-279

**Skill:** Geometry and Trigonometry — Lines, angles, and triangles
**Difficulty:** Hard
**Format:** SPR
**Tool:** No calculator needed

**Source:** House variant of a student-recalled August 2026 Module 2 item (isosceles altitude, scaled Pythagorean triple); numbers changed.

**Question:** An isosceles triangle has a height of $15\sqrt2$ and a base of $16\sqrt2$. Its two congruent sides each have length $a\sqrt2$. What is the value of $a$?

**Correct Answer:** $17$

**Rationale:** The altitude to the base bisects it, giving a right triangle with legs $8\sqrt2$ and $15\sqrt2$. This is an $8$–$15$–$17$ triangle scaled by $\sqrt2$, so the hypotenuse is $17\sqrt2$ and $a=17$.

**Misconception addressed:** Students use the full base $16\sqrt2$ as a leg, giving $\sqrt{15^2+16^2}$, or forget to divide the $\sqrt2$ out.

---

### PS-214

**Skill:** Problem-Solving and Data Analysis — Percentages
**Difficulty:** Medium
**Format:** SPR
**Tool:** Calculator

**Source:** House variant of a student-recalled November 2026 Module 2 item (chained percentage concentration); numbers changed.

**Question:** A $250$ mL solution is $60\%$ distilled water by volume. Of the distilled-water portion, $0.35\%$ is dissolved salt by volume. How many milliliters of salt are in the solution? (Enter the answer rounded to the nearest hundredth.)

**Correct Answer:** $0.53$ (exactly $0.525$)

**Rationale:** Chain the decimals: $250\times0.60\times0.0035=0.525$ mL, which rounds to $0.53$.

**Misconception addressed:** Students convert $0.35\%$ to $0.35$ or $0.035$, or apply $0.35\%$ to the whole $250$ mL ($0.875$).

---

### PS-215

**Skill:** Problem-Solving and Data Analysis — Percentages
**Difficulty:** Hard
**Format:** SPR
**Tool:** No calculator needed

**Source:** House variant of the three-variable percent chain recalled for the International November 2026 form.

**Question:** The quantity $A$ is $20\%$ less than the quantity $C$, and $C$ is $50\%$ greater than the quantity $B$, where $B>0$. $A$ is what percent of $B$?

**Correct Answer:** $120$

**Rationale:** $A=0.80\,C$ and $C=1.50\,B$, so $A=0.80(1.50)B=1.20\,B$, which is $120\%$ of $B$.

**Misconception addressed:** Students combine the changes additively ($+50-20=+30$, giving $130$) or take $50\%$ of $B$.
