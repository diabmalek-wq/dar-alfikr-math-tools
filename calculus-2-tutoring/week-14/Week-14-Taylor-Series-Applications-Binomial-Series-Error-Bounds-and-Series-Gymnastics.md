# Week 14 — Taylor Series Applications: Binomial Series, Error Bounds & Series Gymnastics

**Session length:** 60 minutes (Pages 1–5, self-paced)
**Source:** OpenStax *Calculus Volume 2*, §6.3–§6.4 (Binomial Series; error estimation with Taylor's Theorem; evaluating limits and nonelementary quantities with series). MAT137 Unit 14 slides (14.12–14.14: limits via series substitution; error-bounded numerical estimation) — MAT137 is the University of Toronto's official exclusion-equivalent of MATA37H3.

## Page 1 — Definitions and Key Facts

### Theorem: The Binomial Series

For any real number $r$ (not necessarily a positive integer) and $|x|<1$,
$$(1+x)^r = \sum_{n=0}^{\infty}\binom{r}{n}x^n, \qquad \binom{r}{n} = \frac{r(r-1)(r-2)\cdots(r-n+1)}{n!}, \quad \binom{r}{0}=1.$$
When $r$ is a nonnegative integer, $\binom{r}{n}=0$ for $n>r$ and the series terminates — this recovers the familiar Binomial **Theorem** for finite expansions as a special case. For any other $r$ (negative, or non-integer), the series is genuinely infinite and converges only for $|x|<1$ (radius of convergence $R=1$, regardless of $r$). The binomial series joins the six core Maclaurin series from Week 13 as a seventh standard building block.

### Key Fact: Choosing the Right Error-Bound Tool

Two different tools bound the error of a truncated series, and picking the wrong one wastes effort:
* **Alternating Series Remainder** (Week 10): use when the *numerical series itself* is alternating with terms decreasing to $0$ — the bound is simply the first omitted term, $|R_N|\le b_{N+1}$, no calculus needed beyond identifying the terms.
* **Lagrange Remainder bound** (Theorem 6.7, Week 13): use when the series is **not** alternating, or when you need a bound on a whole *interval* of $x$-values at once — requires bounding $\left|f^{(n+1)}(t)\right|$ by a constant $M$ on the interval in question.

### Key Fact: Series Gymnastics for Limits and Estimation (recap)

Substituting a function's Maclaurin series into a limit or an integral converts an indeterminate form or a nonelementary integral into ordinary term-by-term algebra. The recurring trap: truncating a series too early. Always carry the expansion **at least one order past** the terms that are explicitly being cancelled or subtracted, or the term that actually determines the answer gets thrown away by accident.

## Pages 2–3 — Solved Examples

**Example 1 (Binomial Series, deriving $\frac{1}{\sqrt{1-x}}$).** Find the first four terms of the Maclaurin series for $f(x)=\dfrac{1}{\sqrt{1-x}} = (1-x)^{-1/2}$.

*Solution.* Apply the Binomial Series with $r=-\frac12$ and $x\to -x$: $\binom{-1/2}{0}=1$; $\binom{-1/2}{1}=-\frac12$; $\binom{-1/2}{2}=\dfrac{(-\frac12)(-\frac32)}{2!}=\dfrac{3/4}{2}=\dfrac38$; $\binom{-1/2}{3}=\dfrac{(-\frac12)(-\frac32)(-\frac52)}{3!}=\dfrac{-15/8}{6}=-\dfrac{5}{16}$. So
$$(1-x)^{-1/2} = 1+\left(-\tfrac12\right)(-x)+\tfrac38(-x)^2+\left(-\tfrac{5}{16}\right)(-x)^3+\cdots = 1+\frac x2+\frac{3x^2}{8}+\frac{5x^3}{16}+\cdots,$$
valid for $|x|<1$. Note every sign came out **positive** here because each $(-1)$ from $\binom{r}{n}$'s alternating factors paired with each $(-1)$ from $(-x)^n$. $\blacksquare$

**Example 2 (limit via Maclaurin substitution, higher-order terms matter).** Evaluate $\displaystyle\lim_{x\to0}\frac{\sin x - x+\frac{x^3}{6}}{x^5}$.

*Solution.* Substitute the full Maclaurin series: $\sin x = x-\dfrac{x^3}{6}+\dfrac{x^5}{120}-\dfrac{x^7}{5040}+\cdots$. Then
$$\sin x - x + \frac{x^3}{6} = \frac{x^5}{120}-\frac{x^7}{5040}+\cdots = x^5\left(\frac{1}{120}-\frac{x^2}{5040}+\cdots\right).$$
Divide by $x^5$ and let $x\to0$: every remaining term has a positive power of $x$ except the first, so the limit is $\dfrac{1}{120}$. *Misconception flag:* stopping the $\sin x$ expansion at $x^3$ (matching only the terms that are being explicitly subtracted) throws away the $x^5$ term that **is** the answer — always carry the series at least one order past the cancellation you expect. $\blacksquare$

**Example 3 (comparing growth via series, a two-function contrast).** Determine which is larger for small $x>0$: $\cos(2x)$ or $e^{-2x^2}$, by comparing their Maclaurin series through the $x^4$ term.

*Solution.* $\cos(2x) = 1-\dfrac{(2x)^2}{2}+\dfrac{(2x)^4}{24}-\cdots = 1-2x^2+\dfrac{2}{3}x^4-\cdots$. Also $e^{-2x^2} = \displaystyle\sum_{n=0}^\infty\dfrac{(-2x^2)^n}{n!} = 1-2x^2+2x^4-\cdots$. Both start $1-2x^2+\cdots$, agreeing through the $x^2$ term, but the $x^4$ coefficients differ: $\dfrac23$ for $\cos(2x)$ versus $2$ for $e^{-2x^2}$. Since $\dfrac23<2$, for small $x>0$, $\cos(2x) < e^{-2x^2}$ (concretely, $\cos(2x)-e^{-2x^2}\approx\left(\dfrac23-2\right)x^4 = -\dfrac43x^4<0$ for small $x\ne0$). $\blacksquare$

**Example 4 (numerical estimation with a guaranteed error bound — Alternating Series Remainder).** Estimate $B=\ln(0.9)$ to error less than $0.001$.

*Solution.* $\ln(1+x) = \displaystyle\sum_{n=1}^\infty(-1)^{n+1}\dfrac{x^n}{n}$ at $x=-0.1$: $\ln(0.9) = -\displaystyle\sum_{n=1}^\infty \dfrac{(0.1)^n}{n}$ (every term comes out negative — check directly: $n=1$ term is $-0.1$; $n=2$ term is $-0.01$; and so on). Treating $b_n=\dfrac{(0.1)^n}{n}$ as the magnitude sequence: $b_1=0.1,\,b_2=0.005,\,b_3=0.000333\ldots<0.001$. So keeping terms through $n=2$ (partial sum $-0.1-0.005=-0.105$) guarantees error $<b_3<0.001$. **$\ln(0.9)\approx -0.105$** to the required accuracy. $\blacksquare$

**Example 5 (a nonelementary-looking integral, estimated via series).** Estimate $\displaystyle\int_0^1 \frac{\sin x}{x}\,dx$ to three decimal places (this integrand has no elementary antiderivative).

*Solution.* $\dfrac{\sin x}{x} = \displaystyle\sum_{n=0}^\infty(-1)^n\dfrac{x^{2n}}{(2n+1)!} = 1-\dfrac{x^2}{6}+\dfrac{x^4}{120}-\dfrac{x^6}{5040}+\cdots$ (valid for all $x$, including the removable point $x=0$). Integrate term-by-term from $0$ to $1$: $\displaystyle\int_0^1\dfrac{\sin x}x\,dx = 1-\dfrac{1}{18}+\dfrac{1}{600}-\dfrac{1}{35280}+\cdots$. This is alternating with rapidly shrinking terms; the fourth term $\frac1{35280}\approx0.0000283$ is already below the needed precision, so summing the first three terms: $1-0.05556+0.001667 \approx 0.94611$. **$\displaystyle\int_0^1\frac{\sin x}x\,dx \approx 0.946$.** $\blacksquare$

**Example 6 (error bound with the Lagrange Remainder — non-alternating case).** Estimate $e^{0.2}$ using $p_3(x)$ for $e^x$ at $a=0$, and give a guaranteed bound on the error using the Lagrange Remainder (Theorem 6.7).

*Solution.* $p_3(0.2) = 1+0.2+\dfrac{0.2^2}{2}+\dfrac{0.2^3}{6} = 1+0.2+0.02+0.001\overline3 = 1.221\overline3$. Since $e^x$'s series has **all positive terms** at $x=0.2>0$, the Alternating Series Remainder does not apply — use the Lagrange bound instead: $f^{(4)}(t)=e^t$, and on $[0,0.2]$, $e^t\le e^{0.2}<e^{0.3}\approx1.35$ (a safe, easy-to-justify overestimate for $M$ without needing the answer itself). So
$$|R_3(0.2)| \le \frac{M}{4!}(0.2)^4 \le \frac{1.35}{24}(0.0016) \approx 0.00009.$$
So $e^{0.2}\approx1.2213$ with guaranteed error under $0.0001$ (matches the true value $e^{0.2}\approx1.22140$). $\blacksquare$

## Pages 4–5 — Practice Problems (unsolved)

**Binomial Series**

1. Find the first four terms of the Maclaurin series for $f(x)=(1+x)^{-2}$ using the Binomial Series with $r=-2$, and check your answer against Week 11's result $\dfrac{1}{(1-x)^2}=\sum(n+1)x^n$ (substitute $x\to-x$ to compare).
2. Find the first three nonzero terms of the Maclaurin series for $f(x)=\sqrt{1+x}=(1+x)^{1/2}$.

**Limits and Growth Comparisons**

3. Evaluate $\displaystyle\lim_{x\to0}\dfrac{\cos x - 1+\frac{x^2}2}{x^4}$ using Maclaurin series.

**Numerical Estimation**

4. Estimate $\sin(1)$ using the first three nonzero terms of its Maclaurin series, and use the Alternating Series Remainder to state a guaranteed error bound on your estimate.
5. Estimate $\displaystyle\int_0^1 e^{-x^2}\,dx$ to two decimal places using the Maclaurin series for $e^{-x^2}$, integrated term-by-term (state how many terms you needed and why you can stop there).
6. Estimate $\cos(0.3)$ using $p_2(x)$ for $\cos x$ at $a=0$, and use the Lagrange Remainder to give a guaranteed error bound (use $M=1$, since every derivative of $\cos x$ is bounded by $1$).

**Reasoning**

7. A student claims: "Since the Taylor series of $f$ at $a$ converges for all $x\in\mathbb R$, we know $f$ equals its Taylor series everywhere." Explain precisely why this claim is **false** in general, citing the distinction between "the series converges" and "the series converges to $f$" (Theorem 6.8, Week 13), and what extra ingredient (the Lagrange remainder bound) is needed to upgrade convergence to equality.

## Answer Key & Misconception Notes (for tutor use — do not show student until after attempt)

| # | Answer | Common misconception |
|---|--------|----------------------|
| 1 | $\binom{-2}{0}=1,\ \binom{-2}{1}=-2,\ \binom{-2}{2}=\dfrac{(-2)(-3)}{2}=3,\ \binom{-2}{3}=\dfrac{(-2)(-3)(-4)}{6}=-4$. So $(1+x)^{-2} = 1-2x+3x^2-4x^3+\cdots = \sum(-1)^n(n+1)x^n$. Substituting $x\to-x$ gives $(1-x)^{-2}=\sum(n+1)x^n$ — matches Week 11 Problem 6 exactly. | Forgetting to alternate signs when $r$ is a negative integer — the pattern $1,-2,3,-4,\ldots$ is easy to mis-copy as all-positive since the *magnitudes* $1,2,3,4$ look like the familiar $(n+1)$ pattern on their own. |
| 2 | $\binom{1/2}{0}=1,\ \binom{1/2}{1}=\dfrac12,\ \binom{1/2}{2}=\dfrac{(\frac12)(-\frac12)}{2}=-\dfrac18$. So $\sqrt{1+x} \approx 1+\dfrac{x}{2}-\dfrac{x^2}{8}+\cdots$. | Assuming all binomial coefficients for $r=\frac12$ stay positive (since $r>0$) — the factors $(r-1),(r-2),\ldots$ go negative as soon as $n\ge2$, since $r-1=-\frac12<0$ here. |
| 3 | $\cos x = 1-\dfrac{x^2}2+\dfrac{x^4}{24}-\cdots$, so $\cos x-1+\dfrac{x^2}2 = \dfrac{x^4}{24}-\dfrac{x^6}{720}+\cdots = x^4\left(\dfrac1{24}-\dfrac{x^2}{720}+\cdots\right)$. Dividing by $x^4$ and letting $x\to0$: limit is $\dfrac{1}{24}$. | Stopping the $\cos x$ expansion at the $x^2$ term (matching only what's explicitly subtracted) and missing the $x^4$ term that produces the actual limit — same trap as Example 2. |
| 4 | $\sin1 \approx 1-\dfrac16+\dfrac1{120} = 1-0.16\overline6+0.008\overline3 \approx 0.84167$. Alternating Series Remainder: error $\le$ next omitted term $= \dfrac{1}{5040}\approx0.000198$, so $\sin(1) = 0.84167\pm0.0002$ (matches the true value $\sin1\approx0.84147$). | Reporting the estimate without stating an error bound — the whole point of using the *Alternating Series* Remainder (rather than a vague "should be close") is that it gives a **guaranteed, computable** bound on how far off the truncated sum can be. |
| 5 | $e^{-x^2} = \displaystyle\sum_{n=0}^\infty\dfrac{(-x^2)^n}{n!} = 1-x^2+\dfrac{x^4}2-\dfrac{x^6}6+\dfrac{x^8}{24}-\cdots$. Integrate term-by-term from $0$ to $1$: $1-\dfrac13+\dfrac1{10}-\dfrac1{42}+\dfrac1{216}-\cdots \approx 1-0.3333+0.1-0.0238+0.00463-\cdots \approx 0.7475$. The 5th term ($\approx0.0046$) already affects only the third decimal, so stopping after 5 terms gives **$\approx 0.75$** to two decimal places (matches the known value $\approx0.7468$ closely at this precision). | Integrating only the first two or three terms and declaring victory without checking that the omitted terms are actually small enough for the *requested* precision — always state which term you stopped at and why it's safely below the needed error. |
| 6 | $p_2(0.3) = 1-\dfrac{0.3^2}{2} = 1-0.045 = 0.955$. Since the series alternates in *sign* but the terms here are not simply "the next term in a numerical alternating series" in the same clean sense once truncated at a fixed order, use the Lagrange bound directly: $|R_2(0.3)|\le\dfrac{M}{3!}(0.3)^3 = \dfrac{1}{6}(0.027)=0.0045$. So $\cos(0.3)\approx0.955\pm0.0045$ (matches the true value $\cos(0.3)\approx0.9553$). | Trying to apply the Alternating Series Remainder here since $\cos x$'s *full* series alternates — but once truncated at a specific $p_n$, the correct tool for a guaranteed bound on the *function's* error (not a numerical series' error) is the Lagrange Remainder, which uses the next derivative's bound, not "the next term." |
| 7 | Convergence of the Taylor series (as a series, for whichever $x$ make it converge) says nothing by itself about what it converges *to* — Theorem 6.8 says the series equals $f(x)$ **only when** $R_n(x)\to0$ for that $x$. A series can converge everywhere yet its sum disagree with $f$ off an isolated point (the standard example, not required here, is $f(x)=e^{-1/x^2}$ for $x\ne0$, $f(0)=0$: every derivative at $0$ is $0$, so its Maclaurin series is identically $0$, which trivially "converges everywhere" — to $0$, not to $f(x)$, for any $x\ne0$). The extra ingredient is exactly the Lagrange remainder bound: you need $R_n(x)\to0$, not just that the series of $\frac{f^{(n)}(a)}{n!}(x-a)^n$ happens to converge as a numerical series. | Treating "the Taylor series converges" and "the function is analytic" as synonyms — this is precisely the gap Theorem 6.8 exists to close, and it is a favorite trap on both problem sets and exams. |

---

**Enrichment closer (not a problem — read together as a capstone).** MAT137's final slide deck presents, without proof,
$$\cot x = \frac1x - \frac{2}{6}x - \frac{2}{90}x^3 - \frac{2}{945}x^5 - \cdots,$$
whose coefficients are secretly built from the values $\zeta(2)=\displaystyle\sum\frac1{n^2}=\dfrac{\pi^2}{6}$, $\zeta(4)=\dfrac{\pi^4}{90}$, $\zeta(6)=\dfrac{\pi^6}{945}$ (the **Basel problem** and its higher-power cousins). This is a nice place to point out to a strong student that power series don't just approximate known functions — sometimes the *coefficients themselves* encode deep number-theoretic facts, discovered by Euler roughly 300 years ago.
