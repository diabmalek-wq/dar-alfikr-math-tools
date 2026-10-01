# Week 3 — Integration Techniques I: Substitution & Integration by Parts

**Session length:** 3 hours
**Source:** OpenStax, *Calculus Volume 2*, §3.1 (Integration by Parts); paired with MAT137 (Calculus with Proofs) Unit 9 lecture-slide prompts on substitution and parts, and Evan Dummit's *Calculus II (Part 1): Techniques of Integration* lecture notes (tabular/repeated integration by parts) — MAT137 is the University of Toronto's official exclusion-equivalent of MATA37H3

---

## Page 1 — Introduction, Key Facts & Definitions

### Recap and orientation

FTC (Week 2) reduced every definite integral to "find an antiderivative, then subtract endpoint values." This unit is the first of two building a toolkit for actually *finding* antiderivatives when the integrand isn't already a basic form. Here we cover the two most fundamental techniques: **substitution** (undoing the chain rule) and **integration by parts** (undoing the product rule). Next week's session adds trigonometric-integral identities and partial fractions to the toolkit.

### Why this matters

Nearly every integral on a MATA37/MAT137-style exam is designed to test whether you can correctly *identify* the technique, not just execute it. Substitution and integration by parts are the two techniques you will reach for constantly — inside trig integrals, inside partial-fraction results, inside improper-integral evaluations, and throughout the series unit when checking that a power series' antiderivative was computed correctly.

### Key Fact: Integration by Substitution (Undoing the Chain Rule) (MAT137 Unit 9)

If $F$ is an antiderivative of $f$, then $\dfrac{d}{dx}\big[F(g(x))\big] = f(g(x))g'(x)$ by the chain rule, so
$$\int f(g(x))\,g'(x)\,dx = F(g(x)) + C.$$
In practice: pick $u = g(x)$ (the "inside function"), compute $du = g'(x)\,dx$, and rewrite the whole integral in terms of $u$ only — if any leftover $x$'s remain after substituting, the wrong $u$ was chosen (or the integral needs a different technique entirely).

### Key Fact: Substitution in a Definite Integral (MAT137 Unit 9)

When evaluating $\int_a^b f(g(x))g'(x)\,dx$ by substitution $u=g(x)$, the **limits of integration must also change**, to $u=g(a)$ and $u=g(b)$:
$$\int_a^b f(g(x))\,g'(x)\,dx = \int_{g(a)}^{g(b)} f(u)\,du.$$
A common but invalid shortcut is to substitute $u=g(x)$ throughout the integrand while leaving the limits as the original $x$-values — this produces a numeric answer that is often coincidentally close but is not justified by the change-of-variables theorem, and the *evaluation* step (plugging in numbers) must use whichever variable's limits you are currently using.

### Theorem: Integration by Parts (OpenStax §3.1, Theorem 3.1)

If $u=f(x)$ and $v=g(x)$ have continuous derivatives, then
$$\int u\,dv = uv - \int v\,du.$$
This comes directly from integrating the product rule $\big(f(x)g(x)\big)' = f'(x)g(x)+f(x)g'(x)$. Use it when the integrand is a **product** of two functions where one part becomes simpler when differentiated (choose that part as $u$) and the other part is easy to integrate (that part is $dv$). A common mnemonic for choosing $u$ is **LIATE** (Logarithmic, Inverse trig, Algebraic, Trigonometric, Exponential — earlier in the list is generally the better choice of $u$).

### Key Fact: Repeated / Tabular Integration by Parts (MAT137 Unit 9; Dummit)

When the "algebraic" factor is a polynomial of degree $n\geq 2$ (e.g. $\int x^3 e^{x}dx$), integration by parts must be applied **repeatedly**, each time differentiating the polynomial part further, until it reaches degree $0$. The **tabular method** organizes this bookkeeping: make a column of successive derivatives of the polynomial factor (down to $0$) alongside a column of successive antiderivatives of the other factor, then combine diagonally with alternating signs. When the pattern instead **cycles back to the original integral** (as with $\int e^{ax}\sin(bx)\,dx$, where two rounds of parts return a multiple of the same integral), solve for the original integral algebraically rather than trying to apply parts a third time.

---

## Pages 2–3 — Solved Examples

**Example 1 (Basic substitution).** Evaluate $\displaystyle\int \frac{\sin\sqrt x}{\sqrt x}\,dx$.

Let $u=\sqrt x = x^{1/2}$, so $du = \dfrac{1}{2\sqrt x}dx$, i.e. $\dfrac{dx}{\sqrt x} = 2\,du$. Then
$$\int \frac{\sin\sqrt x}{\sqrt x}\,dx = \int \sin u \cdot 2\,du = -2\cos u + C = -2\cos\sqrt x + C. \qquad \blacksquare$$

---

**Example 2 (Substitution in a definite integral — done correctly).** Evaluate $\displaystyle I=\int_0^2 \sqrt{x^3+1}\,x^2\,dx$.

Let $u = x^3+1$, so $du = 3x^2\,dx$, i.e. $x^2dx = \frac13 du$. **Changing the limits**: when $x=0$, $u=1$; when $x=2$, $u=9$. So
$$I = \int_1^9 \sqrt u \cdot\frac13\,du = \frac13\cdot\frac23 u^{3/2}\Big|_1^9 = \frac29\left(9^{3/2}-1^{3/2}\right) = \frac29(27-1) = \frac{52}{9}.$$
Note that the limits were changed to $u$-values ($1$ and $9$), not left as $0$ and $2$ — mixing the new integrand with the old limits would be evaluating the wrong quantity. $\blacksquare$

---

**Example 3 (Integration by parts, single application).** Evaluate $\displaystyle\int x\,e^{-2x}\,dx$.

Choose $u=x$ (gets simpler when differentiated), $dv = e^{-2x}dx$. Then $du = dx$, $v = -\frac12 e^{-2x}$.
$$\int x e^{-2x}dx = uv - \int v\,du = -\frac{x}{2}e^{-2x} - \int\left(-\frac12 e^{-2x}\right)dx = -\frac x2 e^{-2x} + \frac12\int e^{-2x}dx = -\frac x2 e^{-2x} - \frac14 e^{-2x} + C. \qquad \blacksquare$$

---

**Example 4 (Repeated integration by parts).** Evaluate $\displaystyle\int x^2 \sin x\,dx$.

First round: $u=x^2$, $dv=\sin x\,dx \Rightarrow du=2x\,dx$, $v=-\cos x$:
$$\int x^2\sin x\,dx = -x^2\cos x + \int 2x\cos x\,dx.$$
Second round on $\int 2x\cos x\,dx$: $u=2x$, $dv=\cos x\,dx \Rightarrow du=2\,dx$, $v=\sin x$:
$$\int 2x\cos x\,dx = 2x\sin x - \int 2\sin x\,dx = 2x\sin x + 2\cos x + C.$$
Combining, $\displaystyle\int x^2\sin x\,dx = -x^2\cos x + 2x\sin x + 2\cos x + C$. $\blacksquare$

---

**Example 5 (Tabular integration by parts — three rounds in one table).** Evaluate $\displaystyle\int x^3 e^{x}\,dx$ using the tabular method.

Differentiate $x^3$ down to $0$ in one column, and antidifferentiate $e^x$ (which reproduces itself) in a parallel column, alternating signs $+,-,+,-$ down the diagonal products:
$$\begin{array}{c|c|c}
\text{Sign} & D\text{-column (derivatives of }x^3) & I\text{-column (antiderivatives of }e^x)\\\hline
+ & x^3 & e^x\\
- & 3x^2 & e^x\\
+ & 6x & e^x\\
- & 6 & e^x\\
 & 0 & e^x
\end{array}$$

Multiply each $D$-entry by the *next* $I$-entry down, with the listed sign, and stop once the $D$-column reaches $0$:
$$\int x^3e^x\,dx = x^3e^x - 3x^2e^x + 6xe^x - 6e^x + C.$$
This is exactly three applications of integration by parts done in one pass — the tabular method is a bookkeeping shortcut, not a new theorem, and it only works cleanly when one column terminates at $0$ (a polynomial) while the other column is easy to keep antidifferentiating (as $e^x$, $\sin x$, $\cos x$ all are). $\blacksquare$

---

**Example 6 (The "solve for the integral" trick — a column that never terminates).** Evaluate $\displaystyle I=\int e^{x}\sin x\,dx$.

Round 1: $u=e^x$, $dv=\sin x\,dx \Rightarrow du=e^x dx$, $v=-\cos x$:
$$I = -e^x\cos x + \int e^x\cos x\,dx.$$
Round 2, on $\int e^x\cos x\,dx$: $u=e^x$, $dv=\cos x\,dx \Rightarrow du=e^xdx$, $v=\sin x$:
$$\int e^x\cos x\,dx = e^x\sin x - \int e^x\sin x\,dx = e^x\sin x - I.$$
Substituting back: $I = -e^x\cos x + e^x\sin x - I$, so $2I = e^x(\sin x - \cos x)$, giving
$$I = \int e^x\sin x\,dx = \frac{e^x(\sin x-\cos x)}{2} + C.$$
Here neither column of a tabular setup would ever reach $0$ (differentiating/antidifferentiating $e^x$ and $\sin x$/$\cos x$ cycles forever) — this is the signal to stop applying parts and instead solve the resulting algebraic equation for $I$. $\blacksquare$

---

**Example 7 (Logarithm as the $u$ — nothing else to differentiate).** Evaluate $\displaystyle\int \ln x\,dx$.

Treat this as $\int 1\cdot\ln x\,dx$: choose $u=\ln x$ (it must be $u$, since there is no antiderivative shortcut for $dv=\ln x\,dx$), $dv=dx$. Then $du=\frac1x dx$, $v=x$:
$$\int \ln x\,dx = x\ln x - \int x\cdot\frac1x\,dx = x\ln x - \int 1\,dx = x\ln x - x + C. \qquad \blacksquare$$

---

**Example 8 (LIATE with two genuinely different factors).** Evaluate $\displaystyle\int x\arctan x\,dx$.

By LIATE, Inverse-trig outranks Algebraic, so $u=\arctan x$, $dv=x\,dx \Rightarrow du=\dfrac{1}{1+x^2}dx$, $v=\dfrac{x^2}{2}$:
$$\int x\arctan x\,dx = \frac{x^2}{2}\arctan x - \int\frac{x^2}{2(1+x^2)}\,dx.$$
Simplify the leftover integral by dividing out **before** reaching for partial fractions: $\dfrac{x^2}{1+x^2} = 1-\dfrac{1}{1+x^2}$, so
$$\int x\arctan x\,dx = \frac{x^2}{2}\arctan x - \frac12\int\left(1-\frac{1}{1+x^2}\right)dx = \frac{x^2}{2}\arctan x - \frac{x}{2}+\frac12\arctan x+C. \qquad \blacksquare$$

---

**Example 9 (Level: Foundational — a trig antiderivative building on Practice Problem 2's cousin).** Evaluate $\displaystyle\int \tan x\,dx$.

Rewrite $\tan x = \dfrac{\sin x}{\cos x}$ and let $u=\cos x$, so $du=-\sin x\,dx$, i.e. $\sin x\,dx=-du$. Then
$$\int\tan x\,dx = \int\frac{\sin x}{\cos x}dx = \int\frac{-du}{u} = -\ln|u|+C = -\ln|\cos x|+C = \ln|\sec x|+C.$$
This is the "twin" of Practice Problem 2 ($\cot x$) — same substitution idea, opposite trig ratio — and the two answers are easy to mix up if the sign or the inside function gets copied on autopilot. $\blacksquare$

---

**Example 10 (Level: Intermediate — substitution with algebraic rewriting first).** Evaluate $\displaystyle\int x^3\sqrt{x^2+1}\,dx$.

The obvious substitution $u=x^2+1$ gives $du=2x\,dx$, which only accounts for **one** factor of $x$ — but the integrand has $x^3=x^2\cdot x$. Solve for the leftover $x^2$ in terms of $u$: since $u=x^2+1$, $x^2=u-1$. Then
$$x^3\sqrt{x^2+1}\,dx = x^2\sqrt{x^2+1}\cdot x\,dx = (u-1)\sqrt u\cdot\frac{du}{2}.$$
$$\int x^3\sqrt{x^2+1}\,dx = \frac12\int\big(u^{3/2}-u^{1/2}\big)du = \frac12\left(\frac25u^{5/2}-\frac23u^{3/2}\right)+C = \frac15(x^2+1)^{5/2}-\frac13(x^2+1)^{3/2}+C.$$
The key move is substituting for the *leftover* power of $x$ in terms of $u$, rather than declaring the integral "un-doable by substitution" the moment more than one factor of $x$ remains after forming $du$. $\blacksquare$

---

**Example 11 (Level: Advanced — integration by parts on a definite integral).** Evaluate $\displaystyle\int_0^{\pi/2} x\cos x\,dx$.

Choose $u=x$, $dv=\cos x\,dx \Rightarrow du=dx$, $v=\sin x$:
$$\int_0^{\pi/2}x\cos x\,dx = \Big[x\sin x\Big]_0^{\pi/2}-\int_0^{\pi/2}\sin x\,dx = \left(\frac{\pi}{2}\cdot1-0\right)-\Big[-\cos x\Big]_0^{\pi/2}.$$
$$=\frac{\pi}{2}-\big(-\cos(\pi/2)+\cos 0\big) = \frac{\pi}{2}-(0+1) = \frac{\pi}{2}-1.$$
When integration by parts meets a definite integral, the boundary term $[uv]_a^b$ is evaluated at the endpoints **immediately**, and only the remaining integral $\int v\,du$ carries limits forward — there is no need to find a general antiderivative first and evaluate everything at the very end. $\blacksquare$

---

**Example 12 (Level: Challenge — substitution feeds into tabular parts).** Evaluate $\displaystyle\int x^5e^{x^2}\,dx$.

Neither technique works alone: substitution's obvious candidate $u=x^2$ leaves a leftover $x^4$ that doesn't match any single $du$, and parts with $x^5$ as the polynomial factor would need five rounds against $e^{x^2}$ — whose antiderivative isn't even elementary, so parts cannot get started at all. Instead substitute on **part** of the integrand: let $u=x^2$, $du=2x\,dx$, so $x^4=u^2$ and $x\,dx=\frac12du$:
$$\int x^5e^{x^2}\,dx = \int x^4e^{x^2}\cdot x\,dx = \int u^2e^u\cdot\frac{du}{2} = \frac12\int u^2e^u\,du.$$
Now $\int u^2e^u\,du$ is a textbook tabular-parts integral (compare Example 5): $D$-column $u^2,2u,2,0$; $I$-column $e^u,e^u,e^u,e^u$; signs $+,-,+$:
$$\int u^2e^u\,du = u^2e^u-2ue^u+2e^u+C.$$
$$\int x^5e^{x^2}\,dx = \frac12\left(x^4e^{x^2}-2x^2e^{x^2}+2e^{x^2}\right)+C = \frac12e^{x^2}\big(x^4-2x^2+2\big)+C.$$
The diagnostic skill here is recognizing that a *partial* substitution — one that simplifies the exponent while deliberately leaving a polynomial factor behind — can turn an integral that resists both techniques individually into one that yields cleanly to parts. $\blacksquare$

---

## Pages 4–5 — Practice Problems (unsolved)

**Substitution**

1. Evaluate $\displaystyle\int e^x\cos(e^x)\,dx$.
2. Evaluate $\displaystyle\int \cot x\,dx$. (Hint: rewrite as $\dfrac{\cos x}{\sin x}$.)
3. Evaluate $\displaystyle\int_0^1 x e^{-x^2}\,dx$, carefully converting the limits of integration.
4. The following write-up contains an error even though its final numeric answer happens to be wrong: "$\displaystyle\int_0^2\sqrt{x^3+1}\,x^2\,dx$: let $u=x^3+1$, $du=3x^2dx$; $=\frac13\int_0^2\sqrt u\,du = \frac29 u^{3/2}\Big|_0^2$." Identify the specific error and compute the correct value.
5. Evaluate $\displaystyle\int \frac{x}{\sqrt{4-x^2}}\,dx$.

**Integration by Parts — single and repeated**

6. Evaluate $\displaystyle\int x\,e^{3x}\,dx$.
7. Evaluate $\displaystyle\int x^2\,\ln x\,dx$.
8. Evaluate $\displaystyle\int x^4 e^{-x}\,dx$ using the tabular method from Example 5.
9. Evaluate $\displaystyle\int e^{ax}\cos(bx)\,dx$ (constants $a,b\neq0$), using the "solve for the integral" trick from Worked Example 6.

**Mixed / Applications**

10. Estimate $\displaystyle\int_0^1 f'(x)\,dx$ and $\displaystyle\int_0^3 xf'(x)\,dx$ from a graph where $f$ is a smooth increasing convex function with $f(0)=2$, $f(1)=3$, $f(3)\approx 4.7$ (using $\int_0^1 f'(x)dx = f(1)-f(0)$ via FTC Part 2, and integration by parts on the second one).
11. Evaluate $\displaystyle\int \sin(\ln x)\,dx$. (Hint: this needs the "solve for the integral" trick — two rounds of parts, with $u=$ the trig-of-log factor each time.)
12. A student claims that $\int \dfrac{1}{x}\ln x\,dx$ "obviously needs integration by parts since it's a product of $\frac1x$ and $\ln x$." Show that a substitution is actually faster, and evaluate the integral both ways to confirm they agree.

**More Practice, Graded by Level and Idea**

13. *(Level: Foundational — recognition)* Evaluate $\displaystyle\int\sec^2(3x)\,dx$.
14. *(Level: Foundational — inverse trig via parts)* Evaluate $\displaystyle\int\arcsin x\,dx$.
15. *(Level: Intermediate)* Evaluate $\displaystyle\int_1^e\ln x\,dx$ — the definite-integral version of Worked Example 7.
16. *(Level: Intermediate — algebra before technique)* Evaluate $\displaystyle\int\frac{x^3}{x^2+1}\,dx$. (Hint: this integrand isn't ready for substitution or parts yet — one algebraic step comes first.)
17. *(Level: Advanced)* Evaluate $\displaystyle\int x\cos(2x)\,dx$ by parts, then verify your answer by differentiating it.
18. *(Level: Advanced — diagnose the error)* A student evaluating $\displaystyle\int xe^{x^2}\,dx$ writes: "Let $u=x,\,dv=e^{x^2}dx$; then $v=e^{x^2}$, so $\int xe^{x^2}dx = xe^{x^2}-\int e^{x^2}dx$." Explain precisely what is wrong with this approach — there are two separate problems with it — and give the correct evaluation.
19. *(Level: Challenge — combined technique)* Evaluate $\displaystyle\int e^{\sqrt x}\,dx$. (Hint: substitute to remove the radical from the exponent first; a second technique is needed after that.)
20. *(Level: Challenge — application, Vision 2030 context)* A pipe supplying a new desalination facility on the Red Sea coast, part of a NEOM-area water infrastructure project, has flow rate $r(t)=5te^{-t/2}$ cubic meters per minute during a valve-opening test, for $t\geq0$. Find the total volume, in cubic meters, that flows through the pipe during the first $4$ minutes, i.e. compute $\displaystyle\int_0^4 5te^{-t/2}\,dt$.

---

## Answer Key & Misconception Notes (for tutor use — do not show student until after attempt)

**Problem 1 — Answer.**

**Step 1.** Let $u=e^x$, so $du=e^x\,dx$ — this is exactly the leftover factor in the integrand.
**Step 2.** Rewrite: $\displaystyle\int e^x\cos(e^x)\,dx = \int\cos u\,du$.
**Step 3.** Antidifferentiate and substitute back: $\int\cos u\,du = \sin u + C = \sin(e^x)+C$.

\textbf{\textcolor{cautionInk}{Common misconception:}} Forgetting that $d(e^x)=e^x\,dx$ exactly matches the leftover factor — trying an unnecessary second substitution instead of recognizing the integral is already complete after $u=e^x$.

---

**Problem 2 — Answer.**

**Step 1.** Rewrite $\cot x = \dfrac{\cos x}{\sin x}$.
**Step 2.** Let $u=\sin x$, so $du=\cos x\,dx$ — again exactly the leftover factor.
**Step 3.** Rewrite and integrate: $\displaystyle\int\frac{\cos x}{\sin x}dx = \int\frac{du}{u} = \ln|u|+C = \ln|\sin x|+C$.

\textbf{\textcolor{cautionInk}{Common misconception:}} Confusing $\cot x$'s antiderivative with $\tan x$'s ($-\ln|\cos x|+C$) — these are mirror images and easy to swap.

---

**Problem 3 — Answer.**

**Step 1.** Let $u=x^2$, so $du=2x\,dx$, i.e. $x\,dx=\frac12du$.
**Step 2.** Convert the limits: $x=0\Rightarrow u=0$; $x=1\Rightarrow u=1$.
**Step 3.** Rewrite entirely in $u$: $\displaystyle\int_0^1 xe^{-x^2}dx = \frac12\int_0^1 e^{-u}\,du$.
**Step 4.** Antidifferentiate and evaluate: $\frac12\left[-e^{-u}\right]_0^1 = \frac12\big(-e^{-1}-(-1)\big) = \frac12(1-e^{-1})$.

\textbf{\textcolor{cautionInk}{Common misconception:}} Forgetting to convert the limits from $x$-values to $u$-values, and instead plugging the original $x=0,1$ bounds into the antiderivative written in terms of $u$.

---

**Problem 4 — Answer.**

**Step 1.** Locate the flaw: the write-up substitutes $u=x^3+1$ inside the integrand but never converts the limits $x=0,2$ into $u$-values.
**Step 2.** Compute the correct limits: $x=0\Rightarrow u=1$ (not $u=0$); $x=2\Rightarrow u=9$.
**Step 3.** Redo the evaluation with the correct limits (matching Worked Example 2): $\displaystyle\int_1^9\sqrt u\cdot\frac13\,du = \frac29\left(9^{3/2}-1^{3/2}\right) = \frac29(27-1) = \frac{52}{9}$.
**Step 4.** Compare: the flawed write-up's $\frac29\big(2^{3/2}-0\big)=\frac{2^{5/2}}{9}\approx0.63$ is not even close to the correct $\frac{52}{9}\approx5.78$ — despite the problem statement's framing, the flawed method does *not* land on the right number by luck here, which is itself worth pointing out to a student who assumes a "close enough" answer signals a minor slip.

\textbf{\textcolor{cautionInk}{Common misconception:}} Assuming that because a substitution technically "worked" once in a similar-looking example, skipping the limit-conversion step is a safe shortcut — it is not, and can silently change the answer.

---

**Problem 5 — Answer.**

**Step 1.** Let $u=4-x^2$, so $du=-2x\,dx$, i.e. $x\,dx=-\frac12du$.
**Step 2.** Rewrite: $\displaystyle\int\frac{x}{\sqrt{4-x^2}}dx = -\frac12\int u^{-1/2}\,du$.
**Step 3.** Antidifferentiate: $-\frac12\cdot2u^{1/2}+C = -\sqrt u + C = -\sqrt{4-x^2}+C$.

\textbf{\textcolor{cautionInk}{Common misconception:}} Reaching for trig substitution ($x=2\sin\theta$) when a much simpler direct substitution $u=4-x^2$ already matches the leftover $x\,dx$ factor exactly.

---

**Problem 6 — Answer.**

**Step 1.** Choose $u=x$, $dv=e^{3x}dx$, so $du=dx$, $v=\frac13e^{3x}$.
**Step 2.** Apply parts: $\displaystyle\int xe^{3x}dx = \frac{x}{3}e^{3x}-\int\frac13e^{3x}\,dx$.
**Step 3.** Finish the remaining integral: $\frac{x}{3}e^{3x}-\frac19e^{3x}+C$.

\textbf{\textcolor{cautionInk}{Common misconception:}} Forgetting the $\frac13$ that comes from antidifferentiating $e^{3x}$ (writing $v=e^{3x}$ instead of $\frac13e^{3x}$).

---

**Problem 7 — Answer.**

**Step 1.** By LIATE, choose $u=\ln x$ (Logarithmic outranks Algebraic), $dv=x^2dx$, so $du=\frac1x dx$, $v=\frac{x^3}{3}$.
**Step 2.** Apply parts: $\displaystyle\int x^2\ln x\,dx = \frac{x^3}{3}\ln x-\int\frac{x^3}{3}\cdot\frac1x\,dx$.
**Step 3.** Simplify and finish the remaining integral: $\frac{x^3}{3}\ln x-\int\frac{x^2}{3}dx = \frac{x^3}{3}\ln x-\frac{x^3}{9}+C$.

\textbf{\textcolor{cautionInk}{Common misconception:}} Choosing $u=x^2$ instead of $u=\ln x$ (violating LIATE) — on this particular integral the leftover terms still simplify, but on harder log-times-polynomial integrals the wrong choice causes the degree of the polynomial factor to increase instead of decrease, and the process never terminates.

---

**Problem 8 — Answer.**

**Step 1.** Set up the tabular method as in Worked Example 5: differentiate $x^4$ down to $0$ across five rows: $x^4,4x^3,12x^2,24x,24,0$.
**Step 2.** Antidifferentiate $e^{-x}$ repeatedly, tracking the extra sign flip each round (since $\int e^{-x}dx=-e^{-x}$): the $I$-column is $-e^{-x},e^{-x},-e^{-x},e^{-x},-e^{-x}$.
**Step 3.** Combine diagonally with the tabular method's own alternating signs $+,-,+,-,+$: the five products are $-x^4e^{-x}$, $-4x^3e^{-x}$, $-12x^2e^{-x}$, $-24xe^{-x}$, $-24e^{-x}$.
**Step 4.** Sum: $\displaystyle\int x^4e^{-x}dx = -x^4e^{-x}-4x^3e^{-x}-12x^2e^{-x}-24xe^{-x}-24e^{-x}+C$.

\textbf{\textcolor{cautionInk}{Common misconception:}} Forgetting that antidifferentiating $e^{-x}$ repeatedly alternates an *extra* sign on top of the tabular method's own alternating signs — losing track of this compounding sign is the single most common tabular-method arithmetic error.

---

**Problem 9 — Answer.**

**Step 1.** Round 1: $u=e^{ax}$, $dv=\cos(bx)dx\Rightarrow du=ae^{ax}dx$, $v=\frac1b\sin(bx)$: $\displaystyle I=\frac{e^{ax}\sin(bx)}{b}-\frac ab\int e^{ax}\sin(bx)\,dx$.
**Step 2.** Round 2 on the remaining integral: $u=e^{ax}$, $dv=\sin(bx)dx\Rightarrow du=ae^{ax}dx$, $v=-\frac1b\cos(bx)$: $\displaystyle\int e^{ax}\sin(bx)dx = -\frac{e^{ax}\cos(bx)}{b}+\frac ab\int e^{ax}\cos(bx)dx = -\frac{e^{ax}\cos(bx)}{b}+\frac ab I$.
**Step 3.** Substitute back into Step 1: $\displaystyle I = \frac{e^{ax}\sin(bx)}{b}-\frac ab\left(-\frac{e^{ax}\cos(bx)}{b}+\frac ab I\right) = \frac{e^{ax}\sin(bx)}{b}+\frac{ae^{ax}\cos(bx)}{b^2}-\frac{a^2}{b^2}I$.
**Step 4.** Solve for $I$: $\displaystyle I\left(1+\frac{a^2}{b^2}\right) = \frac{be^{ax}\sin(bx)+ae^{ax}\cos(bx)}{b^2}$, so $\displaystyle I\cdot\frac{a^2+b^2}{b^2} = \frac{e^{ax}(a\cos(bx)+b\sin(bx))}{b^2}$, giving $\displaystyle I=\frac{e^{ax}(a\cos(bx)+b\sin(bx))}{a^2+b^2}+C$.

\textbf{\textcolor{cautionInk}{Common misconception:}} Applying integration by parts correctly for two rounds but then trying a third round instead of recognizing the original integral has reappeared and can be solved for algebraically.

---

**Problem 10 — Answer.**

**Step 1.** For the first integral, apply FTC Part 2 directly: $\displaystyle\int_0^1 f'(x)dx = f(1)-f(0) = 3-2 = 1$.
**Step 2.** For the second integral, apply parts with $u=x$, $dv=f'(x)dx\Rightarrow du=dx$, $v=f(x)$: $\displaystyle\int_0^3 xf'(x)dx = \big[xf(x)\big]_0^3-\int_0^3f(x)\,dx$.
**Step 3.** Evaluate the boundary term: $\big[xf(x)\big]_0^3 = 3f(3)-0\cdot f(0) \approx 3(4.7) = 14.1$.
**Step 4.** So $\displaystyle\int_0^3 xf'(x)dx \approx 14.1-\int_0^3f(x)\,dx$, where $\int_0^3f(x)dx$ must be read off as the area under the graph of $f$ itself (not $f'$) — this is an estimation problem, so the final numeric value depends on that area reading, but the *setup* above is the exact, non-negotiable target.

\textbf{\textcolor{cautionInk}{Common misconception:}} Trying to estimate $\int_0^3 xf'(x)\,dx$ directly from the graph of $f$ (not $f'$) without recognizing integration by parts converts it into terms involving $f$ itself, which the graph of $f$ can estimate.

---

**Problem 11 — Answer.**

**Step 1.** Round 1: $u=\sin(\ln x)$, $dv=dx\Rightarrow du=\cos(\ln x)\cdot\frac1x\,dx$, $v=x$: $\displaystyle I = x\sin(\ln x)-\int x\cdot\cos(\ln x)\cdot\frac1x\,dx = x\sin(\ln x)-\int\cos(\ln x)\,dx$.
**Step 2.** Round 2 on $\int\cos(\ln x)dx$: $u=\cos(\ln x)$, $dv=dx\Rightarrow du=-\sin(\ln x)\cdot\frac1x\,dx$, $v=x$: $\displaystyle\int\cos(\ln x)dx = x\cos(\ln x)+\int\sin(\ln x)\,dx = x\cos(\ln x)+I$.
**Step 3.** Substitute back into Step 1: $I = x\sin(\ln x)-\big(x\cos(\ln x)+I\big) = x\sin(\ln x)-x\cos(\ln x)-I$.
**Step 4.** Solve for $I$: $2I = x\sin(\ln x)-x\cos(\ln x)$, so $\displaystyle I=\frac{x\big(\sin(\ln x)-\cos(\ln x)\big)}{2}+C$.

\textbf{\textcolor{cautionInk}{Common misconception:}} Trying a substitution $u=\ln x$ first — which does simplify the *argument* but leaves an extra $x=e^u$ factor from $dv=dx$ that must still be integrated by parts — instead of going directly to integration by parts on the original variable.

---

**Problem 12 — Answer.**

**Step 1.** \textit{Substitution route:} let $u=\ln x$, $du=\frac1x dx$: $\displaystyle\int\frac{\ln x}{x}dx = \int u\,du = \frac{u^2}{2}+C = \frac{(\ln x)^2}{2}+C$.
**Step 2.** \textit{Parts route, for comparison:} let $u=\ln x$, $dv=\frac1x dx\Rightarrow du=\frac1x dx$, $v=\ln x$: $\displaystyle\int\frac{\ln x}{x}dx = (\ln x)^2-\int\frac{\ln x}{x}dx$.
**Step 3.** Solve the parts equation for the integral: $2\int\frac{\ln x}{x}dx = (\ln x)^2$, so $\displaystyle\int\frac{\ln x}{x}dx = \frac{(\ln x)^2}{2}+C$ — the same answer as Step 1, but only after the extra algebra of solving for the integral.
**Step 4.** Conclusion: both methods agree, but substitution reaches the answer in one line while parts requires recognizing and resolving a self-referential equation — substitution is the faster route here.

\textbf{\textcolor{cautionInk}{Common misconception:}} Assuming integration by parts is always necessary for any integrand that "looks like a product" — $\frac1x\ln x$ is really $f(g(x))g'(x)$ in disguise (with $g(x)=\ln x$), which substitution handles in one line.

---

**Problem 13 — Answer.**

**Step 1.** Let $u=3x$, so $du=3\,dx$, i.e. $dx=\frac13du$.
**Step 2.** Rewrite and integrate: $\displaystyle\int\sec^2(3x)\,dx = \frac13\int\sec^2u\,du = \frac13\tan u+C$.
**Step 3.** Substitute back: $\frac13\tan(3x)+C$.

\textbf{\textcolor{cautionInk}{Common misconception:}} Writing $\tan(3x)+C$ with no compensating $\frac13$ — forgetting that scaling the *inside* of a function by $3$ requires dividing the antiderivative by that same $3$.

---

**Problem 14 — Answer.**

**Step 1.** Treat this as $\int1\cdot\arcsin x\,dx$: choose $u=\arcsin x$, $dv=dx$, so $du=\frac{1}{\sqrt{1-x^2}}dx$, $v=x$.
**Step 2.** Apply parts: $\displaystyle\int\arcsin x\,dx = x\arcsin x-\int\frac{x}{\sqrt{1-x^2}}\,dx$.
**Step 3.** Evaluate the remaining integral by substitution: let $w=1-x^2$, $dw=-2x\,dx$: $\displaystyle\int\frac{x}{\sqrt{1-x^2}}dx = -\frac12\int w^{-1/2}dw = -\sqrt w+C = -\sqrt{1-x^2}+C$.
**Step 4.** Combine: $\displaystyle\int\arcsin x\,dx = x\arcsin x-\big(-\sqrt{1-x^2}\big)+C = x\arcsin x+\sqrt{1-x^2}+C$.

\textbf{\textcolor{cautionInk}{Common misconception:}} Trying $dv=\arcsin x\,dx$ instead of $u=\arcsin x$ — there is no elementary antiderivative to use as $v$ that way, so $\arcsin x$ (and any inverse trig function with no easy antiderivative) must always be chosen as $u$, per LIATE.

---

**Problem 15 — Answer.**

**Step 1.** From Worked Example 7, the general antiderivative is $\int\ln x\,dx = x\ln x-x+C$.
**Step 2.** Evaluate at the upper limit: $e\ln e-e = e(1)-e = 0$.
**Step 3.** Evaluate at the lower limit: $1\ln 1-1 = 1(0)-1=-1$.
**Step 4.** Subtract: $\displaystyle\int_1^e\ln x\,dx = 0-(-1) = 1$.

\textbf{\textcolor{cautionInk}{Common misconception:}} Forgetting that $\ln 1=0$ (not undefined or $1$), which causes the lower-limit evaluation to be miscomputed as $0-1=-1$ read incorrectly, or dropped entirely.

---

**Problem 16 — Answer.**

**Step 1.** Recognize this is not yet in substitution or parts form: the numerator's degree ($3$) is higher than the denominator's ($2$), so divide first. Polynomial long division gives $\dfrac{x^3}{x^2+1} = x-\dfrac{x}{x^2+1}$.
**Step 2.** Split the integral: $\displaystyle\int\frac{x^3}{x^2+1}dx = \int x\,dx-\int\frac{x}{x^2+1}dx$.
**Step 3.** The first piece is immediate: $\int x\,dx = \frac{x^2}{2}$. The second is a direct substitution, $u=x^2+1$, $du=2x\,dx$: $\int\frac{x}{x^2+1}dx = \frac12\ln(x^2+1)$.
**Step 4.** Combine: $\displaystyle\int\frac{x^3}{x^2+1}dx = \frac{x^2}{2}-\frac12\ln(x^2+1)+C$.

\textbf{\textcolor{cautionInk}{Common misconception:}} Trying to force a substitution $u=x^2+1$ on the *whole* fraction right away — it only cleanly matches after the algebraic division step separates out the piece substitution can actually handle.

---

**Problem 17 — Answer.**

**Step 1.** Choose $u=x$, $dv=\cos(2x)dx$, so $du=dx$, $v=\frac12\sin(2x)$.
**Step 2.** Apply parts: $\displaystyle\int x\cos(2x)\,dx = \frac{x}{2}\sin(2x)-\int\frac12\sin(2x)\,dx$.
**Step 3.** Finish the remaining integral: $\frac{x}{2}\sin(2x)-\frac12\left(-\frac12\cos(2x)\right)+C = \frac{x}{2}\sin(2x)+\frac14\cos(2x)+C$.
**Step 4.** Verify by differentiating: $\frac{d}{dx}\left[\frac{x}{2}\sin(2x)\right] = \frac12\sin(2x)+x\cos(2x)$, and $\frac{d}{dx}\left[\frac14\cos(2x)\right]=-\frac12\sin(2x)$; summing gives $x\cos(2x)$, matching the original integrand exactly.

\textbf{\textcolor{cautionInk}{Common misconception:}} Forgetting the extra $\frac12$ that appears when antidifferentiating $\int\sin(2x)dx$, and writing $-\cos(2x)$ instead of $-\frac12\cos(2x)$.

---

**Problem 18 — Answer.**

**Step 1.** First problem with the student's approach: $dv=e^{x^2}dx$ has no elementary antiderivative at all, so "$v=e^{x^2}$" is simply false — $v$ must be an antiderivative of $dv$, and $\frac{d}{dx}\big[e^{x^2}\big]=2xe^{x^2}\neq e^{x^2}$.
**Step 2.** Second, deeper problem: integration by parts is the wrong tool here regardless — the integrand $xe^{x^2}$ is already in the exact form $f(g(x))g'(x)$ (with $g(x)=x^2$, $g'(x)=2x$ up to a constant), which is a direct substitution, not a product needing parts.
**Step 3.** Correct evaluation: let $u=x^2$, $du=2x\,dx$, i.e. $x\,dx=\frac12du$: $\displaystyle\int xe^{x^2}dx = \frac12\int e^u\,du = \frac12e^u+C = \frac12e^{x^2}+C$.

\textbf{\textcolor{cautionInk}{Common misconception:}} Reaching for integration by parts on *any* integrand that superficially looks like a product of two functions, without first checking whether it's actually a disguised chain-rule substitution — and without checking that the proposed $v$ is a genuine antiderivative of $dv$.

---

**Problem 19 — Answer.**

**Step 1.** Substitute to remove the radical from the exponent: let $t=\sqrt x$, so $x=t^2$, $dx=2t\,dt$: $\displaystyle\int e^{\sqrt x}\,dx = \int e^t\cdot2t\,dt = 2\int te^t\,dt$.
**Step 2.** The remaining integral needs a second technique, integration by parts: $u=t$, $dv=e^t dt\Rightarrow du=dt$, $v=e^t$: $\displaystyle\int te^t\,dt = te^t-\int e^t\,dt = te^t-e^t+C$.
**Step 3.** Combine and substitute back $t=\sqrt x$: $\displaystyle\int e^{\sqrt x}\,dx = 2\big(te^t-e^t\big)+C = 2e^t(t-1)+C = 2e^{\sqrt x}\big(\sqrt x-1\big)+C$.
**Step 4.** Verify by differentiating: $\frac{d}{dx}\left[2e^{\sqrt x}(\sqrt x-1)\right] = 2\left[e^{\sqrt x}\cdot\frac{1}{2\sqrt x}\cdot(\sqrt x-1)+e^{\sqrt x}\cdot\frac{1}{2\sqrt x}\right] = \frac{e^{\sqrt x}}{\sqrt x}\big[(\sqrt x-1)+1\big] = \frac{e^{\sqrt x}}{\sqrt x}\cdot\sqrt x = e^{\sqrt x}$, matching the original integrand.

\textbf{\textcolor{cautionInk}{Common misconception:}} Trying integration by parts directly on $e^{\sqrt x}$ without first substituting away the radical in the exponent — parts alone cannot make progress while $\sqrt x$ sits inside the exponential.

---

**Problem 20 — Answer.**

**Step 1.** Choose $u=5t$, $dv=e^{-t/2}dt$, so $du=5\,dt$, $v=-2e^{-t/2}$.
**Step 2.** Apply parts: $\displaystyle\int5te^{-t/2}\,dt = -10te^{-t/2}-\int\big(-2e^{-t/2}\big)(5)\,dt = -10te^{-t/2}+10\int e^{-t/2}\,dt$.
**Step 3.** Finish the remaining integral: $-10te^{-t/2}+10\big(-2e^{-t/2}\big)+C = -10te^{-t/2}-20e^{-t/2}+C = -10e^{-t/2}(t+2)+C$.
**Step 4.** Evaluate from $t=0$ to $t=4$: at $t=4$, $-10e^{-2}(6)=-60e^{-2}$; at $t=0$, $-10e^0(2)=-20$. So $\displaystyle\int_0^4 5te^{-t/2}\,dt = -60e^{-2}-(-20) = 20-60e^{-2}\approx20-8.12\approx11.88$ cubic meters.

\textbf{\textcolor{cautionInk}{Common misconception:}} Forgetting to evaluate the antiderivative at the *lower* limit $t=0$ as well — since it isn't zero here ($-10e^0(0+2)=-20$, not $0$), skipping it silently drops $20$ cubic meters from the answer.
