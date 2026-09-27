# Week 15 — Final Exam Review: Comprehensive

## Page 1 — Key Facts

**Roadmap: The Full MATA37H3 Topic List**

This review week cycles through every topic from Weeks 1–14: Riemann sums and the definite integral, the Fundamental Theorem of Calculus, integration techniques (substitution, by parts, trig integrals, partial fractions, Weierstrass substitution), improper integrals, numerical integration, sequences, series and the divergence test, convergence tests (Integral, Comparison, LCT, Alternating Series, Ratio), absolute vs. conditional convergence, power series, Taylor polynomials, and Taylor/Maclaurin series with the Binomial Series. No new theorems are introduced this week — this is consolidation and exam practice.

**Key Fact: True/False Is a High-Stakes Section**

On real MATA37H3-style final exams, a True/False section is often the *first* section and carries significant weight. These questions test precise recall of hypotheses (e.g., "the Ratio Test is inconclusive when the limit equals $1$" is true; "the Ratio Test proves divergence when the limit equals $1$" is false). A single missing hypothesis (boundedness, continuity, positivity of terms) turns a true statement false. Read every word before answering.

**Key Fact: The Convergence-Test Decision Tree**

Given a series $\sum a_n$, ask in order: (1) Does $a_n\to0$? If not, **Divergence Test** applies immediately. (2) Are all terms positive (or eventually positive)? If the terms resemble $\dfrac{1}{n^p}$ or fit an integral, try the **Integral Test** or **$p$-Series** benchmark. If they resemble a known series by comparison, try **Comparison** or **Limit Comparison**. (3) Do the terms alternate in sign? Try the **Alternating Series Test**, and separately ask whether $\sum|a_n|$ converges (**absolute** convergence) or only $\sum a_n$ converges (**conditional**). (4) Does the series involve factorials, $n$-th powers, or $n!$-type growth? Try the **Ratio Test**.

**Key Fact: The Taylor Series Toolkit**

To find a Taylor/Maclaurin series: (a) compute derivatives directly from the coefficient formula $\dfrac{f^{(k)}(a)}{k!}$; (b) substitute into one of the six core Maclaurin series ($e^x$, $\sin x$, $\cos x$, $\dfrac{1}{1-x}$, $\ln(1+x)$, the Binomial Series); or (c) manipulate a known series termwise (differentiate, integrate, multiply by $x^k$, add/subtract series). To bound the error of a truncated series, use the **Alternating Series Remainder** ($|R_n|\le b_{n+1}$) when the series alternates and its terms decrease, or the **Lagrange Remainder** ($|R_n(x)|\le\dfrac{M}{(n+1)!}|x-a|^{n+1}$) otherwise.

## Pages 2–3 — Solved Examples

**Example 1 (Riemann Sums / FTC).** Evaluate $\displaystyle\int_1^4\left(3x^2-\dfrac{2}{x}\right)dx$ using the Fundamental Theorem of Calculus.

*Solution.* An antiderivative is $F(x)=x^3-2\ln x$. Then
$$\int_1^4\left(3x^2-\dfrac{2}{x}\right)dx=F(4)-F(1)=\left(64-2\ln4\right)-\left(1-2\ln1\right)=63-2\ln4.$$
Since $\ln1=0$, the final answer is $63-2\ln4=63-4\ln2$. $\blacksquare$

**Example 2 (Integration by Parts).** Evaluate $\displaystyle\int x\ln x\,dx$.

*Solution.* Let $u=\ln x$, $dv=x\,dx$, so $du=\dfrac{1}{x}dx$ and $v=\dfrac{x^2}{2}$. Then
$$\int x\ln x\,dx=\dfrac{x^2}{2}\ln x-\int\dfrac{x^2}{2}\cdot\dfrac{1}{x}\,dx=\dfrac{x^2}{2}\ln x-\int\dfrac{x}{2}\,dx=\dfrac{x^2}{2}\ln x-\dfrac{x^2}{4}+C.\ \blacksquare$$

**Example 3 (Partial Fractions).** Evaluate $\displaystyle\int\dfrac{5x-1}{(x-1)(x+2)}\,dx$.

*Solution.* Write $\dfrac{5x-1}{(x-1)(x+2)}=\dfrac{A}{x-1}+\dfrac{B}{x+2}$. Clearing denominators: $5x-1=A(x+2)+B(x-1)$. At $x=1$: $4=3A\Rightarrow A=\dfrac{4}{3}$. At $x=-2$: $-11=-3B\Rightarrow B=\dfrac{11}{3}$. Thus
$$\int\dfrac{5x-1}{(x-1)(x+2)}\,dx=\dfrac{4}{3}\ln|x-1|+\dfrac{11}{3}\ln|x+2|+C.\ \blacksquare$$

**Example 4 (Improper Integral).** Determine whether $\displaystyle\int_1^\infty\dfrac{1}{x^{3/2}}\,dx$ converges, and if so, find its value.

*Solution.* This is a $p$-integral with $p=\dfrac32>1$, so it converges. Compute directly:
$$\int_1^\infty x^{-3/2}\,dx=\lim_{b\to\infty}\left[-2x^{-1/2}\right]_1^b=\lim_{b\to\infty}\left(-\dfrac{2}{\sqrt b}+2\right)=2.\ \blacksquare$$

**Example 5 (Numerical Integration).** Use Simpson's Rule with $n=4$ to approximate $\displaystyle\int_0^2 x^3\,dx$, and compare to the exact value.

*Solution.* Here $\Delta x=\dfrac{2-0}{4}=\dfrac12$, nodes $x_0,\dots,x_4=0,0.5,1,1.5,2$, with $f(x)=x^3$: $f(x_0)=0$, $f(x_1)=0.125$, $f(x_2)=1$, $f(x_3)=3.375$, $f(x_4)=8$.
$$S_4=\dfrac{\Delta x}{3}\left[f(x_0)+4f(x_1)+2f(x_2)+4f(x_3)+f(x_4)\right]=\dfrac{0.5}{3}\left[0+0.5+2+13.5+8\right]=\dfrac{0.5}{3}(24)=4.$$
The exact value is $\displaystyle\int_0^2x^3\,dx=\left[\dfrac{x^4}{4}\right]_0^2=4$. Simpson's Rule is exact here because it integrates cubics exactly. $\blacksquare$

**Example 6 (Sequence Convergence).** Determine whether $a_n=\dfrac{3n^2+1}{n^2-2n}$ converges, and find its limit if so.

*Solution.* Divide numerator and denominator by $n^2$:
$$a_n=\dfrac{3+\dfrac{1}{n^2}}{1-\dfrac{2}{n}}\longrightarrow\dfrac{3+0}{1-0}=3\quad\text{as }n\to\infty.$$
The sequence converges to $3$. $\blacksquare$

**Example 7 (Convergence Test Selection).** Determine whether $\displaystyle\sum_{n=1}^\infty\dfrac{n+5}{n^3-2}$ converges.

*Solution.* For large $n$, $a_n=\dfrac{n+5}{n^3-2}$ behaves like $\dfrac{n}{n^3}=\dfrac{1}{n^2}$. Apply the Limit Comparison Test with $b_n=\dfrac{1}{n^2}$:
$$\lim_{n\to\infty}\dfrac{a_n}{b_n}=\lim_{n\to\infty}\dfrac{n^2(n+5)}{n^3-2}=\lim_{n\to\infty}\dfrac{n^3+5n^2}{n^3-2}=1.$$
Since the limit is a finite positive number and $\displaystyle\sum\dfrac{1}{n^2}$ is a convergent $p$-series ($p=2>1$), the given series also converges. $\blacksquare$

**Example 8 (Absolute vs. Conditional Convergence).** Determine whether $\displaystyle\sum_{n=1}^\infty\dfrac{(-1)^{n-1}}{\sqrt n}$ converges absolutely, converges conditionally, or diverges.

*Solution.* The series alternates, with $b_n=\dfrac{1}{\sqrt n}$ decreasing to $0$, so by the Alternating Series Test the series converges. Checking absolute convergence: $\displaystyle\sum\left|\dfrac{(-1)^{n-1}}{\sqrt n}\right|=\sum\dfrac{1}{\sqrt n}$ is a $p$-series with $p=\dfrac12\le1$, which diverges. Therefore the series converges **conditionally**. $\blacksquare$

**Example 9 (Power Series Interval of Convergence).** Find the radius and interval of convergence of $\displaystyle\sum_{n=1}^\infty\dfrac{(x-3)^n}{n\cdot4^n}$.

*Solution.* By the Ratio Test:
$$\lim_{n\to\infty}\left|\dfrac{(x-3)^{n+1}}{(n+1)4^{n+1}}\cdot\dfrac{n\cdot4^n}{(x-3)^n}\right|=\dfrac{|x-3|}{4}\lim_{n\to\infty}\dfrac{n}{n+1}=\dfrac{|x-3|}{4}.$$
Convergence requires $\dfrac{|x-3|}{4}<1$, i.e. $|x-3|<4$, so $R=4$. Checking endpoints: at $x=7$, the series is $\displaystyle\sum\dfrac{1}{n}$, which diverges; at $x=-1$, the series is $\displaystyle\sum\dfrac{(-1)^n}{n}$, which converges (Alternating Series Test). The interval of convergence is $[-1,7)$. $\blacksquare$

**Example 10 (Taylor Series with Error Bound).** Estimate $\cos(0.5)$ using the Maclaurin polynomial of degree $4$, and bound the error using the Lagrange Remainder.

*Solution.* The degree-$4$ Maclaurin polynomial for $\cos x$ is $p_4(x)=1-\dfrac{x^2}{2}+\dfrac{x^4}{24}$. At $x=0.5$:
$$p_4(0.5)=1-\dfrac{0.25}{2}+\dfrac{0.0625}{24}=1-0.125+0.0026=0.8776.$$
For the Lagrange bound, $f^{(5)}(t)=-\sin t$, so $|f^{(5)}(t)|\le1$ for all $t$. Thus
$$|R_4(0.5)|\le\dfrac{1}{5!}(0.5)^5=\dfrac{0.03125}{120}\approx0.00026.$$
So $\cos(0.5)\approx0.8776$ with error under $0.0003$. $\blacksquare$

## Pages 4–5 — Practice Problems

**Part A — True/False.** State whether each is True or False, and justify briefly.

1. If $\displaystyle\lim_{n\to\infty}a_n=0$, then $\displaystyle\sum_{n=1}^\infty a_n$ converges.

2. If the Ratio Test gives $\displaystyle\lim_{n\to\infty}\left|\dfrac{a_{n+1}}{a_n}\right|=1$, then $\sum a_n$ diverges.

3. Every absolutely convergent series is also conditionally convergent.

4. If $f$ is continuous on $[a,b]$, then $\displaystyle\int_a^b f(x)\,dx$ exists.

5. The interval of convergence of a power series is always a closed interval $[a-R,\,a+R]$.

**Part B — Mixed Computation.**

6. Evaluate $\displaystyle\int \dfrac{x}{\sqrt{4-x^2}}\,dx$ using an appropriate substitution.

7. Determine whether $\displaystyle\int_0^\infty e^{-2x}\,dx$ converges, and if so, find its value.

8. Use the Trapezoidal Rule with $n=4$ to approximate $\displaystyle\int_0^4\sqrt{x}\,dx$.

9. Determine whether $\displaystyle\sum_{n=2}^\infty \dfrac{1}{n(\ln n)^2}$ converges, using the Integral Test.

10. Determine whether $\displaystyle\sum_{n=1}^\infty \dfrac{(-1)^n n}{n^2+1}$ converges absolutely, converges conditionally, or diverges.

11. Find the Taylor series for $f(x)=\dfrac{1}{x}$ centered at $a=2$, and state its radius of convergence.

12. Use the Binomial Series to find the first four terms of the Maclaurin series for $\sqrt[3]{1+x}$.

13. A series $\sum a_n$ has partial sums $S_n=\dfrac{2n}{n+1}$. Find $\displaystyle\sum_{n=1}^\infty a_n$ (i.e., find $\displaystyle\lim_{n\to\infty}S_n$), and state what this tells you about convergence.

## Answer Key & Misconception Notes

| # | Answer | Misconception Note |
|---|--------|---------------------|
| 1 | **False.** | $a_n\to0$ is *necessary* but not *sufficient* for convergence — the classic counterexample is the harmonic series $\sum\frac1n$, where $a_n\to0$ but the series diverges. |
| 2 | **False.** | A Ratio Test limit of $1$ is **inconclusive** — it proves neither convergence nor divergence. A common exam trap treats $L=1$ as automatic divergence. |
| 3 | **False.** | It's the reverse: absolute convergence *implies* ordinary convergence, but "conditionally convergent" specifically means the series converges while $\sum|a_n|$ diverges — an absolutely convergent series is never called conditionally convergent. |
| 4 | **True.** | Continuity on a closed interval guarantees Riemann integrability — this is a standard existence theorem, distinct from asking whether the integral has an elementary antiderivative. |
| 5 | **False.** | The interval of convergence can be open, closed, or half-open depending on endpoint behavior — only the *radius* $R$ is guaranteed; each endpoint $x=a\pm R$ must be checked separately by direct substitution. |
| 6 | $-\sqrt{4-x^2}+C$ | Using $u=4-x^2$, $du=-2x\,dx$, gives $\int x(4-x^2)^{-1/2}dx=-\frac12\int u^{-1/2}du=-\sqrt u+C$. A common error is mishandling the $-\frac12$ factor from $du$. |
| 7 | Converges to $\dfrac12$ | $\int_0^\infty e^{-2x}dx=\lim_{b\to\infty}\left[-\frac12e^{-2x}\right]_0^b=0-(-\frac12)=\frac12$. Forgetting the $\frac12$ from the chain rule on $e^{-2x}$ is the usual slip. |
| 8 | $\approx5.146$ | $\Delta x=1$; nodes $0,1,2,3,4$ give $f$-values $0,1,\sqrt2\approx1.414,\sqrt3\approx1.732,2$; $T_4=\frac{1}{2}[0+2(1)+2(1.414)+2(1.732)+2]\approx5.146$ — forgetting to double the interior nodes (only the endpoints stay single-weighted) is the most common Trapezoidal error. |
| 9 | Converges | With $u=\ln x$, $\int_2^\infty\frac{dx}{x(\ln x)^2}=\int_{\ln2}^\infty u^{-2}du$, a convergent $p$-integral ($p=2>1$). Forgetting to substitute the bounds ($x=2\Rightarrow u=\ln2$, not $u=2$) is a common slip. |
| 10 | Diverges | The Divergence Test applies directly: $a_n=\frac{(-1)^n n}{n^2+1}$ does not tend to $0$ in absolute value — $|a_n|=\frac{n}{n^2+1}\to0$ actually, so re-examine: $|a_n|\to0$, so the Divergence Test does NOT immediately apply; instead compare $|a_n|=\frac{n}{n^2+1}$ to $\frac1n$ via LCT ($\lim\frac{n^2}{n^2+1}=1$), and since $\sum\frac1n$ diverges, the series does not converge absolutely; the Alternating Series Test then shows the alternating series itself **converges conditionally**. The trap is stopping after checking $|a_n|\to0$ and wrongly concluding absolute convergence without a comparison test. |
| 11 | $\displaystyle\sum_{n=0}^\infty\dfrac{(-1)^n(x-2)^n}{2^{n+1}}$, $R=2$ | Write $\frac1x=\frac{1}{2+(x-2)}=\frac12\cdot\frac{1}{1+\frac{x-2}{2}}$, then apply the geometric series with ratio $-\frac{x-2}{2}$. Forgetting the overall $\frac12$ factor is the common error. |
| 12 | $1+\dfrac{x}{3}-\dfrac{x^2}{9}+\dfrac{5x^3}{81}-\cdots$ | Using $r=\frac13$: $\binom{1/3}{1}=\frac13$, $\binom{1/3}{2}=\frac{\frac13\cdot(-\frac23)}{2}=-\frac19$, $\binom{1/3}{3}=\frac{\frac13\cdot(-\frac23)\cdot(-\frac53)}{6}=\frac{5}{81}$. A common error is reusing the $\sqrt{1+x}$ ($r=\frac12$) coefficients instead of recomputing for $r=\frac13$. |
| 13 | $\displaystyle\lim_{n\to\infty}S_n=2$, so $\sum a_n$ converges to $2$ | By definition, a series converges exactly when its sequence of partial sums converges, and the sum equals that limit — a frequent misconception is trying to reconstruct $a_n$ first rather than recognizing that the limit of $S_n$ IS the answer directly. |
