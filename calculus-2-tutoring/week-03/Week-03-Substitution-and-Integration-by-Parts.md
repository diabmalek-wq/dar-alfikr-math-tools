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

---

## Answer Key & Misconception Notes (for tutor use — do not show student until after attempt)

| # | Answer | Common misconception |
|---|---|---|
| 1 | $\sin(e^x)+C$ | Forgetting that $d(e^x)=e^x dx$ exactly matches the leftover factor — trying an unnecessary second substitution instead of recognizing the integral is already complete after $u=e^x$. |
| 2 | $u=\sin x$, $du=\cos x\,dx$: $\int\cot x\,dx = \int\frac{\cos x}{\sin x}dx = \ln\lvert\sin x\rvert+C$ | Confusing $\cot x$'s antiderivative with $\tan x$'s ($-\ln\lvert\cos x\rvert+C$) — these are mirror images and easy to swap. |
| 3 | $u=x^2$, $du=2x\,dx \Rightarrow x\,dx=\frac12du$; limits $x=0\to u=0$, $x=1\to u=1$: $\int_0^1 xe^{-x^2}dx = \frac12\int_0^1 e^{-u}du = \frac12\left[-e^{-u}\right]_0^1 = \frac12(1-e^{-1})$ | Forgetting to convert the limits from $x$-values to $u$-values, and instead plugging the original $x=0,1$ bounds into the antiderivative written in terms of $u$. |
| 4 | The error: the limits $0,2$ were never converted to $u$-values (should be $u=1$ to $u=9$, since $x=0\Rightarrow u=1$, not $u=0$); the correct value (matching Worked Example 2) is $\frac{52}{9}$, not $\frac29(2^{3/2}-0)=\frac{2^{5/2}}{9}$ as the flawed write-up would give | Assuming that because a substitution technically "worked" once in a similar-looking example, skipping the limit-conversion step is a safe shortcut — it is not, and can silently change the answer. |
| 5 | $u=4-x^2$, $du=-2x\,dx$: $\int\frac{x}{\sqrt{4-x^2}}dx = -\frac12\int u^{-1/2}du = -\sqrt{4-x^2}+C$ | Trying trig substitution ($x=2\sin\theta$) when a much simpler direct substitution $u=4-x^2$ already matches the leftover $x\,dx$ factor exactly. |
| 6 | $u=x,\,dv=e^{3x}dx \Rightarrow du=dx,\,v=\frac13e^{3x}$: $\int xe^{3x}dx=\frac{x}{3}e^{3x}-\frac19e^{3x}+C$ | Forgetting the $\frac13$ that comes from antidifferentiating $e^{3x}$ (writing $v=e^{3x}$ instead of $\frac13e^{3x}$). |
| 7 | $u=\ln x,\,dv=x^2dx \Rightarrow du=\frac1xdx,\,v=\frac{x^3}{3}$: $\int x^2\ln x\,dx = \frac{x^3}{3}\ln x-\int\frac{x^2}{3}dx = \frac{x^3}{3}\ln x-\frac{x^3}{9}+C$ | Choosing $u=x^2$ instead of $u=\ln x$ (violating LIATE) — this leaves $\int \frac{x^3}{3}\cdot\frac{1}{x}dx$-style terms that are actually fine here, but on harder log-times-polynomial integrals the wrong choice causes the degree of the polynomial factor to increase instead of decrease. |
| 8 | $\int x^4e^{-x}dx = -x^4e^{-x}-4x^3e^{-x}-12x^2e^{-x}-24xe^{-x}-24e^{-x}+C$ (five rows: $D$-column $x^4,4x^3,12x^2,24x,24,0$; $I$-column all $-e^{-x}$ after the first, since antiderivatives of $e^{-x}$ pick up a sign each time) | Forgetting that antidifferentiating $e^{-x}$ repeatedly alternates an *extra* sign on top of the tabular method's own alternating signs — losing track of this compounding sign is the single most common tabular-method arithmetic error. |
| 9 | $\dfrac{e^{ax}(a\cos(bx)+b\sin(bx))}{a^2+b^2}+C$ (via the same "solve for $I$" method as Worked Example 6, generalized with constants $a,b$) | Applying integration by parts correctly for two rounds but then trying a third round instead of recognizing the original integral has reappeared and can be solved for algebraically. |
| 10 | $\int_0^1 f'(x)dx = f(1)-f(0)=1$ by FTC Part 2; $\int_0^3 xf'(x)dx$ needs parts with $u=x, dv=f'(x)dx \Rightarrow v=f(x)$: $=\big[xf(x)\big]_0^3-\int_0^3 f(x)dx = 3f(3)-0-\int_0^3f(x)dx \approx 3(4.7)-\int_0^3f(x)dx$, requiring an area estimate under $f$ from the graph | Trying to estimate $\int_0^3 xf'(x)\,dx$ directly from the graph of $f$ (not $f'$) without recognizing integration by parts converts it into terms involving $f$ itself, which the graph of $f$ can estimate. |
| 11 | $u=\sin(\ln x),\,dv=dx\Rightarrow du=\cos(\ln x)\cdot\frac1x dx,\,v=x$, giving $I=x\sin(\ln x)-\int\cos(\ln x)dx$; a second round on $\int\cos(\ln x)dx$ (with $u=\cos(\ln x)$) produces $x\cos(\ln x)+\int\sin(\ln x)dx = x\cos(\ln x)+I$; solving, $2I = x\sin(\ln x)-x\cos(\ln x)$, so $I=\dfrac{x\big(\sin(\ln x)-\cos(\ln x)\big)}{2}+C$ | Trying a substitution $u=\ln x$ first (which does simplify the *argument* but leaves an extra $x=e^u$ factor from $dv=dx$ that must still be integrated by parts) instead of going directly to integration by parts on the original variable. |
| 12 | Substitution: $u=\ln x,\,du=\frac1x dx$, so $\int\frac{\ln x}{x}dx = \int u\,du = \frac{u^2}{2}+C = \frac{(\ln x)^2}{2}+C$; by parts: $u=\ln x,\,dv=\frac1x dx\Rightarrow du=\frac1xdx,\,v=\ln x$, giving $\int\frac{\ln x}{x}dx = (\ln x)^2 - \int\frac{\ln x}{x}dx$, so $2\int\frac{\ln x}{x}dx=(\ln x)^2$, i.e. the same answer $\frac{(\ln x)^2}{2}+C$ — by parts works too, but requires the "solve for the integral" trick, making substitution the faster route | Assuming integration by parts is always necessary for any integrand that "looks like a product" — $\frac1x\ln x$ is really $f(g(x))g'(x)$ in disguise (with $g(x)=\ln x$), which substitution handles in one line. |
