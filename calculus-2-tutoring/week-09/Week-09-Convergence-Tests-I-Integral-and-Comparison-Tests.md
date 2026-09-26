# Week 9 — Convergence Tests I: The Integral Test & Comparison Tests

**Session length:** 60 minutes (Pages 1–5, self-paced)
**Source:** OpenStax *Calculus Volume 2*, §5.3 (Integral Test, Theorem 5.9; $p$-series), §5.4 (Comparison Test Theorem 5.11; Limit Comparison Test Theorem 5.12). MAT137 Unit 13 slides (13.10–13.14: integral and comparison tests) — MAT137 is the University of Toronto's official exclusion-equivalent of MATA37H3.

## Page 1 — Definitions and Key Facts

### Theorem: The Integral Test

Suppose $\displaystyle\sum_{n=1}^{\infty} a_n$ has positive terms, and there is a function $f$ and integer $N$ such that (i) $f$ is continuous, (ii) $f$ is decreasing, and (iii) $f(n)=a_n$ for all $n\ge N$. Then
$$\sum_{n=1}^{\infty} a_n \ \text{ and } \ \int_{N}^{+\infty} f(x)\,dx \ \text{ either both converge or both diverge.}$$
**Critical warning:** even when both converge, the *values* are almost always different — the integral test only ever certifies convergence/divergence, never computes the sum.

### Key Fact: $p$-Series

$\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^p}$ converges if and only if $p>1$ (diverges for $p\le 1$) — this follows directly from the Integral Test applied to $f(x)=1/x^p$, mirroring the $p$-integral rule from Week 5. The case $p=1$ is the harmonic series (divergent).

### Theorem: The Comparison Test (for series)

Let $a_n, b_n \ge 0$ eventually (for $n\ge N$).
**(i)** If $a_n \le b_n$ for $n\ge N$ and $\displaystyle\sum b_n$ converges, then $\displaystyle\sum a_n$ converges.
**(ii)** If $a_n \ge b_n \ge 0$ for $n\ge N$ and $\displaystyle\sum b_n$ diverges, then $\displaystyle\sum a_n$ diverges.
(Exact structural analogue of the Comparison Theorem for improper integrals from Week 5 — "small diverges $\Rightarrow$ big diverges," "big converges $\Rightarrow$ small converges," and the two converse implications are false.)

### Theorem: The Limit Comparison Test (LCT, for series)

Let $a_n, b_n \ge 0$, and suppose $\displaystyle\lim_{n\to\infty}\frac{a_n}{b_n} = L$.
* If $L$ is finite and nonzero: $\displaystyle\sum a_n$ and $\displaystyle\sum b_n$ **both converge or both diverge**.
* If $L=0$ and $\displaystyle\sum b_n$ converges, then $\displaystyle\sum a_n$ converges.
* If $L=\infty$ and $\displaystyle\sum b_n$ diverges, then $\displaystyle\sum a_n$ diverges.

## Pages 2–3 — Solved Examples

**Example 1 (Integral Test, basic application).** Determine convergence of $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n(\ln n)^3}$ (starting effectively at $n=2$, since $\ln 1=0$).

*Solution.* $f(x)=\dfrac{1}{x(\ln x)^3}$ is continuous, positive, and decreasing for $x\ge2$. Substituting $u=\ln x,\,du=dx/x$: $\displaystyle\int_2^{+\infty}\frac{dx}{x(\ln x)^3} = \int_{\ln 2}^{+\infty}\frac{du}{u^3}$, a $p$-integral with $p=3>1$ — converges. By the Integral Test, $\displaystyle\sum\frac{1}{n(\ln n)^3}$ **converges**. $\blacksquare$

**Example 2 (contrast: $\sum 1/(n\ln n)$ diverges — same technique, different $p$).** Determine convergence of $\displaystyle\sum_{n=2}^{\infty}\frac{1}{n\ln n}$.

*Solution.* Same substitution gives $\displaystyle\int_{\ln2}^{+\infty}\frac{du}{u}$, a $p$-integral with $p=1$ — **diverges**. So $\displaystyle\sum\frac{1}{n\ln n}$ **diverges**, despite looking almost identical to Example 1 (only the power on $\ln n$ differs — this pair is a standard "spot the difference" pairing). $\blacksquare$

**Example 3 (Comparison Test, "small diverges").** Determine convergence of $\displaystyle\sum_{n=1}^{\infty}\frac{n+1}{n^2+1}$.

*Solution.* For $n\ge1$: $\dfrac{n+1}{n^2+1} \ge \dfrac{n}{n^2+n^2} = \dfrac{1}{2n}$ (using $n^2+1\le 2n^2$ for $n\ge1$, and $n+1\ge n$). Since $\displaystyle\sum\frac{1}{2n} = \frac12\sum\frac1n$ diverges (harmonic), and our series' terms are $\ge$ this divergent series' terms, by the Comparison Test the original series **diverges**. $\blacksquare$

**Example 4 (LCT, cleaner than direct comparison).** Determine convergence of $\displaystyle\sum_{n=1}^{\infty}\frac{\sqrt[3]{n^2+1}+1}{\sqrt{n^3+n}+n+1}$.

*Solution.* Leading-order behavior: numerator $\sim n^{2/3}$, denominator $\sim n^{3/2}$, so compare to $b_n = n^{2/3}/n^{3/2} = n^{-5/6}$. Compute $L=\displaystyle\lim_{n\to\infty}\frac{a_n}{b_n}=1$ (finite, nonzero — routine but tedious algebra, dividing numerator and denominator by the dominant powers). Since $\displaystyle\sum n^{-5/6}$ is a $p$-series with $p=\frac56<1$, it diverges; by LCT, the original series **diverges** too. $\blacksquare$

**Example 5 (choosing between Comparison and LCT).** Determine convergence of $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2-n+1}$.

*Solution.* Direct comparison is awkward here (the $-n$ makes a clean term-by-term inequality fiddly), so use LCT with $b_n=1/n^2$: $L=\displaystyle\lim_{n\to\infty}\frac{n^2}{n^2-n+1}=1$, finite and nonzero. Since $\sum 1/n^2$ converges ($p=2>1$), by LCT the original series **converges**. This illustrates the general rule of thumb: use direct Comparison when a clean term-by-term inequality is easy to produce; reach for LCT when the algebra of a direct inequality would be messy but the leading-order behavior is clear. $\blacksquare$

## Pages 4–5 — Practice Problems (unsolved)

**Integral Test**

1. Use the Integral Test to determine convergence of $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2+1}$.
2. Use the Integral Test to determine convergence of $\displaystyle\sum_{n=1}^{\infty}n e^{-n^2}$.
3. Use the Integral Test to determine convergence of $\displaystyle\sum_{n=2}^{\infty}\frac{1}{n(\ln n)}\cdot\frac{1}{\ln(\ln n)}$ for $n\ge3$ (i.e. starting the sum where $\ln(\ln n)$ is defined and positive). (Hint: substitute $u=\ln x$, then $v=\ln u$.)

**Comparison Test**

4. Determine convergence of $\displaystyle\sum_{n=1}^{\infty}\frac{n^2+3n}{n^4+5n+1}$ using the Comparison Test.
5. Determine convergence of $\displaystyle\sum_{n=1}^{\infty}\frac{1}{2^n+n}$ using the Comparison Test.

**Limit Comparison Test**

6. Determine convergence of $\displaystyle\sum_{n=1}^{\infty}\frac{2^n-40}{3^n-20}$ using LCT.
7. Determine convergence of $\displaystyle\sum_{n=1}^{\infty}\sin^2\left(\frac1n\right)$ using LCT. (Hint: recall $\displaystyle\lim_{x\to0}\frac{\sin x}{x}=1$.)
8. Determine convergence of $\displaystyle\sum_{n=1}^{\infty}\frac{5n^3-2n+1}{n^5+n^2-3}$ using LCT.

**Mixed reasoning**

9. Explain, in one or two sentences, why a $p$-series can never be used as the comparison series $b_n$ to establish convergence via the Comparison Test's part (i) when $p\le1$ — and give the smallest $p$ that *would* work as a valid comparison series for $\displaystyle\sum \frac{1}{n^2+\sqrt n}$.
10. A student claims: "Since $\dfrac{1}{n!}<\dfrac{1}{n^2}$ for all $n\ge4$, and $\sum 1/n^2$ converges, the Comparison Test proves $\sum 1/n!$ converges." Is the *logic* of this argument valid (regardless of whether the conclusion happens to be true)? Justify your answer using the exact statement of the Comparison Test on Page 1.

## Answer Key & Misconception Notes (for tutor use — do not show student until after attempt)

| # | Answer | Common misconception |
|---|--------|----------------------|
| 1 | Converges. $f(x)=1/(x^2+1)$ is continuous, positive, decreasing on $[1,\infty)$; $\int_1^\infty \frac{dx}{x^2+1} = [\arctan x]_1^\infty = \frac\pi2-\frac\pi4=\frac\pi4$, finite. By Integral Test, series converges. | Reporting the sum of the series as $\pi/4$ (the integral's value) — the Integral Test only certifies convergence, it does not compute the series' actual sum, which is generally a *different* number. |
| 2 | Converges. $f(x)=xe^{-x^2}$ is positive and eventually decreasing (check $f'(x)=e^{-x^2}(1-2x^2)<0$ for $x>1/\sqrt2$); $\int_1^\infty xe^{-x^2}dx = \left[-\frac12e^{-x^2}\right]_1^\infty = \frac{1}{2e}$, finite — converges. | Not verifying the "decreasing" hypothesis of the Integral Test before applying it — some functions increase initially and only decrease later; the test still applies as long as it's *eventually* decreasing (from some $N$ onward), but this must be checked, not assumed. |
| 3 | Diverges. With $u=\ln x$, $v=\ln u$: $\int \frac{dx}{x\ln x \ln(\ln x)} = \int \frac{dv}{v}$, a $p$-integral with $p=1$ — diverges. By the Integral Test, the series diverges. | Assuming every "nested log" integral automatically converges because it "decays fast" — the substitution must actually be carried out; nested-log $p$-integrals with $p=1$ still diverge, just very slowly. |
| 4 | Converges. For large $n$, $\frac{n^2+3n}{n^4+5n+1} \le \frac{2n^2}{n^4} = \frac{2}{n^2}$ eventually; $\sum 2/n^2$ converges ($p=2>1$); by Comparison Test the original series converges. | Comparing to $1/n^4$ (matching only the denominator's degree) instead of correctly computing the *net* degree gap (numerator degree $2$, denominator degree $4$, net comparison should be to $n^{2-4}=n^{-2}$, not $n^{-4}$). |
| 5 | Converges. $\frac{1}{2^n+n} \le \frac{1}{2^n}$ for all $n\ge1$; $\sum 1/2^n$ is a convergent geometric series ($r=1/2$); by the Comparison Test the original series converges. | Trying to compare to $1/n$ instead of the geometric term $1/2^n$ — since the geometric term dominates the denominator's growth, the tighter (and correct) comparison series is geometric, not a $p$-series. |
| 6 | Converges. $\frac{2^n-40}{3^n-20}$ behaves like $(2/3)^n$ for large $n$; using LCT with $b_n=(2/3)^n$: $L=\lim\frac{2^n-40}{3^n-20}\cdot\left(\frac32\right)^n = \lim\frac{1-40\cdot2^{-n}}{1-20\cdot3^{-n}}=1$, finite nonzero. Since $\sum(2/3)^n$ converges (geometric, $|r|<1$), the original series converges. | Eyeballing "big numbers in numerator and denominator both growing" as automatically divergent, without identifying that the *ratio* of the dominant terms is what determines convergence, not their individual growth. |
| 7 | Converges. $\sin^2(1/n) \sim (1/n)^2$ as $n\to\infty$ (since $\sin x\approx x$ near $0$); LCT with $b_n=1/n^2$: $L = \lim \frac{\sin^2(1/n)}{1/n^2} = \left(\lim\frac{\sin(1/n)}{1/n}\right)^2 = 1^2=1$, finite nonzero. $\sum 1/n^2$ converges ($p=2>1$), so original series converges. | Comparing to $1/n$ instead of $1/n^2$ (forgetting the square on $\sin^2$, which changes the effective power of $n$ in the comparison series). |
| 8 | Diverges. Leading behavior: numerator $\sim 5n^3$, denominator $\sim n^5$, so compare to $b_n=1/n^2$: $L=\lim\frac{5n^3-2n+1}{n^5+n^2-3}\cdot n^2 = 5$, finite nonzero. $\sum 1/n^2$ actually **converges** ($p=2>1$) — recheck degree gap: numerator degree $3$, denominator degree $5$, net power $3-5=-2$, so $b_n=n^{-2}$ is correct and $\sum n^{-2}$ converges, so the original series **converges**, not diverges. | Miscounting the degree gap between numerator and denominator — always subtract (numerator degree) $-$ (denominator degree) to get the comparison series' exponent, and double-check whether that resulting $p$-series converges or diverges before stating the final answer. |
| 9 | A $p$-series with $p\le1$ diverges, so it can never serve as a convergent $b_n$ in part (i) of the Comparison Test (which requires $\sum b_n$ to converge). For $\sum \frac{1}{n^2+\sqrt n}$, since $\frac{1}{n^2+\sqrt n}<\frac{1}{n^2}$ and $p=2>1$ works (any $p$ with $1<p\le2$ also works, but $p=2$ is the natural/tightest choice matching the dominant term). | Thinking any $p$-series can be used as a comparison series regardless of whether it itself converges — the comparison series' own convergence behavior (determined by its own $p$) is what does the logical work, so it must be checked first. |
| 10 | No, the logic is invalid as stated (even though the conclusion is true). The Comparison Test's part (i) requires $a_n\le b_n$ where $b_n$ is the *known convergent* series — here the student has it backwards: $1/n!$ is the *smaller* term and $1/n^2$ is being used correctly as the larger convergent bound, so actually re-reading it, $a_n=1/n!\le b_n=1/n^2$ with $\sum b_n$ convergent **does** correctly match part (i) and the conclusion is valid. The trap is checking that the inequality direction and the roles of $a_n,b_n$ are matched to the *correct* part of the theorem, not assuming a plausible-sounding argument is automatically flawed or automatically correct — restate the theorem's hypotheses explicitly and verify each one before accepting or rejecting an argument. | Either accepting a plausible-sounding comparison argument without explicitly checking which part (i)/(ii) applies and whether the inequality direction matches, or over-correcting by assuming any Comparison Test argument stated by a "student claim" prompt must contain an error — always verify against the theorem's exact hypotheses on Page 1 rather than pattern-matching from memory. |
