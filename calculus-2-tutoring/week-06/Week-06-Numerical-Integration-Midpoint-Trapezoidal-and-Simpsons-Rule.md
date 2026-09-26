# Week 6 — Numerical Integration: Midpoint, Trapezoidal & Simpson's Rule

**Session length:** 60 minutes (Pages 1–5, self-paced)
**Source:** OpenStax *Calculus Volume 2*, §3.6 (Numerical Integration — Midpoint Rule, Trapezoidal Rule Theorem 3.4, error bounds Theorem 3.5, Simpson's Rule Theorem 3.6 and its error bound). Closes the one topic in the official MATA37H3 calendar not covered by Weeks 1–5: approximating a definite integral when no elementary antiderivative exists.

## Page 1 — Definitions and Key Facts

### Why this topic exists

Many important integrands (e.g. $e^{-x^2}$, $\sin(x^2)$, $\dfrac{\sin x}{x}$) have **no elementary antiderivative** — FTC Part 2 cannot be applied directly. Numerical integration approximates $\displaystyle\int_a^b f(x)\,dx$ to any desired accuracy using only values of $f$, by partitioning $[a,b]$ into $n$ equal subintervals of width $\Delta x = \dfrac{b-a}{n}$ with grid points $x_0=a<x_1<\cdots<x_n=b$.

### Key Fact: The Midpoint Rule

$$M_n = \Delta x\Big[f(\bar x_1)+f(\bar x_2)+\cdots+f(\bar x_n)\Big], \qquad \bar x_i = \frac{x_{i-1}+x_i}{2}\ \text{(midpoint of the $i$-th subinterval).}$$
Geometrically, $M_n$ sums the areas of rectangles whose height is the function value at each subinterval's midpoint.

### Theorem: The Trapezoidal Rule

$$T_n = \frac{\Delta x}{2}\Big[f(x_0)+2f(x_1)+2f(x_2)+\cdots+2f(x_{n-1})+f(x_n)\Big].$$
Geometrically, $T_n$ sums the areas of trapezoids formed by connecting consecutive points $(x_{i-1},f(x_{i-1}))$ and $(x_i,f(x_i))$ with a straight line. **Coefficient pattern:** first and last endpoint get weight $1$; every interior grid point gets weight $2$ — a classic place to drop a factor of $2$ by mistake.

### Theorem: Error Bounds for $M_n$ and $T_n$

If $|f''(x)|\le K$ for all $x\in[a,b]$, then the errors $E_M = \left|\displaystyle\int_a^b f\,dx - M_n\right|$ and $E_T = \left|\displaystyle\int_a^b f\,dx - T_n\right|$ satisfy
$$E_M \le \frac{K(b-a)^3}{24n^2}, \qquad E_T \le \frac{K(b-a)^3}{12n^2}.$$
**Key relationship:** the Trapezoidal bound is **exactly twice** the Midpoint bound — for a concave function, $M_n$ and $T_n$ err in *opposite directions* (one underestimates, the other overestimates), which is why weighting $2M_n$ and $T_n$ together (see Simpson's Rule below) cancels much of the error.

### Theorem: Simpson's Rule

For **even** $n$,
$$S_n = \frac{\Delta x}{3}\Big[f(x_0)+4f(x_1)+2f(x_2)+4f(x_3)+2f(x_4)+\cdots+4f(x_{n-1})+f(x_n)\Big].$$
**Coefficient pattern:** endpoints get weight $1$; interior grid points alternate weight $4,2,4,2,\ldots,4$ (always **starting and ending the interior run with $4$**, since $n$ is even). Simpson's Rule fits a parabola through each consecutive triple of points, so it integrates any polynomial of degree $\le3$ **exactly** (zero error).

### Theorem: Error Bound for $S_n$

If $\left|f^{(4)}(x)\right|\le M$ for all $x\in[a,b]$, then
$$E_S = \left|\int_a^b f\,dx - S_n\right| \le \frac{M(b-a)^5}{180n^4}.$$
The $n^4$ in the denominator (versus $n^2$ for $M_n,T_n$) is why Simpson's Rule converges **dramatically faster** as $n$ increases — doubling $n$ shrinks the Trapezoidal error by a factor of $4$, but shrinks the Simpson error by a factor of $16$.

## Pages 2–3 — Solved Examples

**Example 1 (Trapezoidal Rule, basic computation).** Approximate $\displaystyle\int_0^2 x^2\,dx$ using $T_4$.

*Solution.* $\Delta x = \dfrac{2-0}{4}=0.5$; grid points $x_0,\ldots,x_4 = 0,0.5,1,1.5,2$; $f$-values $0,\,0.25,\,1,\,2.25,\,4$.
$$T_4 = \frac{0.5}{2}\big[0+2(0.25)+2(1)+2(2.25)+4\big] = 0.25\big[0+0.5+2+4.5+4\big]=0.25(11)=2.75.$$
The exact value is $\displaystyle\int_0^2x^2dx=\left[\frac{x^3}{3}\right]_0^2=\frac83\approx2.667$. $T_4$ **overestimates** because $f(x)=x^2$ is concave up ($f''=2>0$) — trapezoids drawn above a concave-up curve always lie above it. $\blacksquare$

**Example 2 (Midpoint Rule, same integral — contrast the sign of the error).** Approximate $\displaystyle\int_0^2 x^2\,dx$ using $M_4$.

*Solution.* Same $\Delta x=0.5$; midpoints $0.25,\,0.75,\,1.25,\,1.75$; $f$-values $0.0625,\,0.5625,\,1.5625,\,3.0625$.
$$M_4 = 0.5\big[0.0625+0.5625+1.5625+3.0625\big] = 0.5(5.25) = 2.625.$$
Here $M_4$ **underestimates** the exact value $8/3\approx2.667$ — for a concave-up function, the Midpoint Rule always underestimates (the tangent-line rectangle at the midpoint sits *below* the curve on average). Note the errors: $|E_T|=|2.75-2.667|\approx0.083$, $|E_M|=|2.667-2.625|\approx0.042$ — matching the theorem's prediction that $E_T\approx 2E_M$ for the same $n$. $\blacksquare$

**Example 3 (Simpson's Rule, same integral — exactness for low-degree polynomials).** Approximate $\displaystyle\int_0^2 x^2\,dx$ using $S_4$.

*Solution.* Using the same grid as Example 1:
$$S_4 = \frac{0.5}{3}\big[0+4(0.25)+2(1)+4(2.25)+4\big] = \frac16\big[0+1+2+9+4\big] = \frac{16}{6}=\frac83.$$
$S_4$ gives the **exact** value $8/3$ with zero error, because Simpson's Rule integrates any polynomial of degree $\le3$ exactly, and $f(x)=x^2$ has degree $2\le3$. $\blacksquare$

**Example 4 (Error-bound computation, Trapezoidal Rule).** Find a bound on the error when approximating $\displaystyle\int_1^2\frac{1}{x}\,dx$ using $T_{10}$.

*Solution.* $f(x)=1/x$, $f''(x)=2/x^3$. On $[1,2]$, $|f''(x)|$ is largest at $x=1$ (since $x^3$ is smallest there): $K=|f''(1)|=2$. Then
$$E_T \le \frac{K(b-a)^3}{12n^2} = \frac{2\cdot1^3}{12\cdot100} = \frac{2}{1200}=\frac{1}{600}\approx0.00167.$$
So $T_{10}$ is guaranteed accurate to within about $0.00167$ of the true value $\ln 2\approx0.6931$. $\blacksquare$

**Example 5 (Choosing $n$ in advance to guarantee a target accuracy, Simpson's Rule).** How large must (even) $n$ be so that $S_n$ approximates $\displaystyle\int_0^1 \sin x\,dx$ with error less than $0.0001$?

*Solution.* $f^{(4)}(x)=\sin x$, and $|\sin x|\le1$ for all $x$, so take $M=1$. We need
$$\frac{M(b-a)^5}{180n^4} < 0.0001 \;\Longrightarrow\; \frac{1}{180n^4} < 0.0001 \;\Longrightarrow\; n^4 > \frac{1}{180(0.0001)} = \frac{1}{0.018}\approx55.6 \;\Longrightarrow\; n > 55.6^{1/4}\approx2.73.$$
Since $n$ must be an even integer, the smallest valid choice is $n=4$. $\blacksquare$

## Pages 4–5 — Practice Problems (unsolved)

**Midpoint & Trapezoidal Computation**

1. Approximate $\displaystyle\int_0^4 \sqrt{x}\,dx$ using $T_4$ (grid points at $0,1,2,3,4$; use $\sqrt0=0,\sqrt1=1,\sqrt2\approx1.414,\sqrt3\approx1.732,\sqrt4=2$).
2. Approximate the same integral, $\displaystyle\int_0^4\sqrt{x}\,dx$, using $M_4$ (midpoints $0.5,1.5,2.5,3.5$; use $\sqrt{0.5}\approx0.707,\sqrt{1.5}\approx1.225,\sqrt{2.5}\approx1.581,\sqrt{3.5}\approx1.871$).

**Simpson's Rule Computation**

3. Approximate $\displaystyle\int_0^2 (x^3+1)\,dx$ using $S_4$ (grid points $0,0.5,1,1.5,2$), and compare to the exact value. Explain why the two must match exactly.
4. Approximate $\displaystyle\int_0^{\pi} \sin x\,dx$ using $S_4$ (grid points $0,\pi/4,\pi/2,3\pi/4,\pi$; use $\sin0=0,\sin(\pi/4)\approx0.707,\sin(\pi/2)=1,\sin(3\pi/4)\approx0.707,\sin\pi=0$), and compare to the exact value $2$.

**Error Bounds**

5. Find a bound on the error in approximating $\displaystyle\int_0^1 e^{x}\,dx$ using $T_8$. (Use $f''(x)=e^x$, and since $e^x$ is increasing, its maximum on $[0,1]$ is $e\approx2.718$.)
6. Find a bound on the error in approximating $\displaystyle\int_1^3 \ln x\,dx$ using $M_6$. (Use $f''(x)=-1/x^2$, so $|f''(x)|$ is largest at $x=1$.)
7. How large must $n$ be so that $T_n$ approximates $\displaystyle\int_0^1 e^{x}\,dx$ with error less than $0.001$?
8. How large must (even) $n$ be so that $S_n$ approximates $\displaystyle\int_0^2 x^4\,dx$ with error less than $0.01$? (Use $f^{(4)}(x)=24$, a constant, so $M=24$.)

**Mixed reasoning**

9. A student computes $T_4$ and $M_4$ for the same integral and gets $T_4=5.20$ and $M_4=5.05$. Without further calculation, give the best available estimate for $S_4$ using the identity $S_{2n}=\dfrac{2M_n+T_n}{3}$ (the exact relationship Simpson's Rule is built from), and briefly explain why this weighted average reduces error compared to either $T_4$ or $M_4$ alone.
10. Explain, using the error-bound formulas on Page 1, why doubling $n$ reduces the Trapezoidal error bound by a factor of $4$ but reduces the Simpson error bound by a factor of $16$.

## Answer Key & Misconception Notes (for tutor use — do not show student until after attempt)

| # | Answer | Common misconception |
|---|--------|----------------------|
| 1 | $T_4 = \frac{1}{2}\big[0+2(1)+2(1.414)+2(1.732)+2\big] = \frac12\big[0+2+2.828+3.464+2\big]=\frac12(10.292)=5.146$. | Forgetting to double the interior grid-point values (weight $2$) while leaving the two endpoints at weight $1$ — a dropped factor of $2$ on an interior term is the single most common Trapezoidal Rule slip. |
| 2 | $M_4 = 1\big[0.707+1.225+1.581+1.871\big] = 5.384$. | Using the *endpoints* of each subinterval instead of the *midpoint* — the Midpoint Rule requires evaluating $f$ only at the center of each subinterval, never at $x_{i-1}$ or $x_i$ directly. |
| 3 | $S_4 = \frac{0.5}{3}\big[1+4(1.125)+2(2)+4(4.375)+9\big] = \frac16\big[1+4.5+4+17.5+9\big]=\frac{36}{6}=6$. Exact: $\int_0^2(x^3+1)dx = \left[\frac{x^4}{4}+x\right]_0^2 = 4+2=6$. They match exactly because Simpson's Rule integrates any polynomial of degree $\le3$ exactly, and $x^3+1$ has degree $3$. | Assuming Simpson's Rule is only "very accurate" rather than *exact* for cubics — the exactness is a hard theorem (zero error), not an approximation that happens to be close. |
| 4 | $S_4 = \frac{\pi/4}{3}\big[0+4(0.707)+2(1)+4(0.707)+0\big] = \frac{\pi}{12}\big[0+2.828+2+2.828+0\big]=\frac{\pi}{12}(7.656)\approx2.005$, very close to the exact value $2$ (small residual error since $\sin x$ is not a polynomial of degree $\le3$). | Expecting Simpson's Rule to be exact here — $\sin x$ is not a polynomial, so Simpson's Rule is highly accurate but not exact; only degree-$\le3$ polynomials get *zero* error. |
| 5 | $E_T \le \frac{K(b-a)^3}{12n^2} = \frac{e\cdot1^3}{12\cdot64}=\frac{2.718}{768}\approx0.00354$. | Using $f'(x)=e^x$ (first derivative) instead of $f''(x)=e^x$ in the error-bound formula — the Trapezoidal and Midpoint error bounds require the *second* derivative's bound $K$, not the first. |
| 6 | $E_M \le \frac{K(b-a)^3}{24n^2} = \frac{1\cdot2^3}{24\cdot36}=\frac{8}{864}\approx0.00926$ (using $K=|f''(1)|=1$, and $b-a=3-1=2$). | Forgetting that the Midpoint bound's denominator has a $24$, not a $12$ (that's the Trapezoidal bound) — mixing up the two formulas' constants is the most common error-bound mistake. |
| 7 | Need $\frac{e\cdot1^3}{12n^2}<0.001 \Rightarrow n^2 > \frac{2.718}{0.012}\approx226.5 \Rightarrow n>15.05$, so $n=16$ (smallest integer satisfying the bound; Trapezoidal Rule has no parity requirement, unlike Simpson's). | Rounding $n$ down instead of up — since the inequality must be satisfied (not approximately satisfied), always round up to the next integer to *guarantee* the target accuracy, even if that pushes just barely past a whole number. |
| 8 | Need $\frac{24\cdot2^5}{180n^4}<0.01 \Rightarrow \frac{768}{180n^4}<0.01 \Rightarrow n^4 > \frac{768}{1.8}\approx426.7 \Rightarrow n>4.54$, so the smallest even integer satisfying this is $n=6$. | Rounding to the nearest even integer ($n=4$) instead of the smallest even integer *at or above* the computed threshold ($n>4.54$ requires $n=6$, since $n=4$ does not satisfy the strict inequality). |
| 9 | $S_4 = \dfrac{2(5.05)+5.20}{3} = \dfrac{10.10+5.20}{3}=\dfrac{15.30}{3}=5.10$. This weighted average is more accurate because $T_n$ and $M_n$ typically err in *opposite* directions for a function of consistent concavity (Example 2's pattern), so combining them with weights $2:1$ (matching how Simpson's Rule is actually derived from fitting parabolas) cancels much of the leading-order error term that $T_n$ and $M_n$ each carry individually. | Averaging $T_4$ and $M_4$ with equal weights ($\frac{T_4+M_4}{2}$) instead of the correct $2:1$ weighting toward $M_n$ — the factor of $2$ on $M_n$ is not arbitrary, it comes directly from the ratio of the Trapezoidal and Midpoint error-bound constants ($12$ vs. $24$). |
| 10 | The Trapezoidal/Midpoint error bounds have $n^2$ in the denominator, so replacing $n$ with $2n$ gives $(2n)^2=4n^2$ — a factor-of-$4$ reduction. The Simpson bound has $n^4$ in the denominator, so replacing $n$ with $2n$ gives $(2n)^4=16n^4$ — a factor-of-$16$ reduction. This is exactly why Simpson's Rule reaches high accuracy with far fewer function evaluations than the Trapezoidal or Midpoint Rules. | Assuming all numerical integration methods improve at the same rate as $n$ increases — the *rate* of convergence (the power of $n$ in the error bound's denominator) is a structural property of each method, not something that can be inferred from one example alone. |
