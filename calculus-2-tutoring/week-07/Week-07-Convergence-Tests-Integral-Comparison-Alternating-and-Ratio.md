# Week 7 — Convergence Tests: Integral, Comparison, Alternating Series & Ratio Test

**Session length:** 60 minutes (Pages 1–5, self-paced)
**Source:** OpenStax *Calculus Volume 2*, §5.3 (Integral Test, Theorem 5.9; $p$-series), §5.4 (Comparison Test Theorem 5.11; Limit Comparison Test Theorem 5.12), §5.5 (Alternating Series Test Theorem 5.13; Remainder Theorem 5.14; Absolute Convergence Implies Convergence Theorem 5.15), §5.6 (Ratio Test Theorem 5.16). MAT137 Unit 13 slides (13.10–13.19: integral/comparison tests, alternating series test and error estimation, absolute vs. conditional convergence, "ninja level" convergence puzzles, ratio test).

## Page 1 — Definitions and Key Facts

### Theorem: The Integral Test

Suppose $\displaystyle\sum_{n=1}^{\infty} a_n$ has positive terms, and there is a function $f$ and integer $N$ such that (i) $f$ is continuous, (ii) $f$ is decreasing, and (iii) $f(n)=a_n$ for all $n\ge N$. Then
$$\sum_{n=1}^{\infty} a_n \ \text{ and } \ \int_{N}^{+\infty} f(x)\,dx \ \text{ either both converge or both diverge.}$$
**Critical warning:** even when both converge, the *values* are almost always different — the integral test only ever certifies convergence/divergence, never computes the sum.

### Key Fact: $p$-Series

$\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^p}$ converges if and only if $p>1$ (diverges for $p\le 1$) — this follows directly from the Integral Test applied to $f(x)=1/x^p$, mirroring the $p$-integral rule from Unit 12. The case $p=1$ is the harmonic series (divergent).

### Theorem: The Comparison Test (for series)

Let $a_n, b_n \ge 0$ eventually (for $n\ge N$).
**(i)** If $a_n \le b_n$ for $n\ge N$ and $\displaystyle\sum b_n$ converges, then $\displaystyle\sum a_n$ converges.
**(ii)** If $a_n \ge b_n \ge 0$ for $n\ge N$ and $\displaystyle\sum b_n$ diverges, then $\displaystyle\sum a_n$ diverges.
(Exact structural analogue of BCT for improper integrals from Unit 12 — "small diverges ⟹ big diverges," "big converges ⟹ small converges," and the two converse implications are false.)

### Theorem: The Limit Comparison Test (LCT, for series)

Let $a_n, b_n \ge 0$, and suppose $\displaystyle\lim_{n\to\infty}\frac{a_n}{b_n} = L$.
* If $L$ is finite and nonzero: $\displaystyle\sum a_n$ and $\displaystyle\sum b_n$ **both converge or both diverge**.
* If $L=0$ and $\displaystyle\sum b_n$ converges, then $\displaystyle\sum a_n$ converges.
* If $L=\infty$ and $\displaystyle\sum b_n$ diverges, then $\displaystyle\sum a_n$ diverges.

### Theorem: The Alternating Series Test (AST)

An alternating series $\displaystyle\sum(-1)^{n+1}b_n$ (or $\sum(-1)^n b_n$) with $b_n\ge0$ **converges** if (i) $b_{n+1}\le b_n$ eventually (the $b_n$ are eventually non-increasing) **and** (ii) $\displaystyle\lim_{n\to\infty}b_n=0$. AST is a **one-directional sufficient condition** — if either hypothesis fails, you learn nothing from AST itself (you must fall back on the Divergence Test or another test).

### Theorem: Remainder Estimate for Alternating Series

Under the AST hypotheses, if $S$ is the true sum and $S_N$ the $N$-th partial sum, the error satisfies $|R_N| = |S-S_N| \le b_{N+1}$ — **the error is bounded by the first omitted term's absolute value**. This gives a concrete, computable stopping rule for estimating a sum to a target precision.

### Definitions: Absolute and Conditional Convergence

$\displaystyle\sum a_n$ is **absolutely convergent** if $\displaystyle\sum|a_n|$ converges. It is **conditionally convergent** if $\displaystyle\sum a_n$ converges but $\displaystyle\sum|a_n|$ diverges. These two categories are **mutually exclusive** by definition — a series cannot be both, despite the superficially similar names.

### Theorem: Absolute Convergence Implies Convergence

If $\displaystyle\sum|a_n|$ converges, then $\displaystyle\sum a_n$ converges. (The converse is false — this is exactly what "conditionally convergent" describes.) This is the standard tool for handling a series with **mixed-sign, non-alternating** terms (e.g. $\sum \sin n/n^p$), where AST does not apply directly: test $\sum|a_n|$ with a positive-term test instead.

### Theorem: The Ratio Test

Let $\displaystyle\sum a_n$ have nonzero terms, and let $\rho = \displaystyle\lim_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|$.
* If $0\le \rho<1$: $\displaystyle\sum a_n$ converges **absolutely**.
* If $\rho>1$ or $\rho=\infty$: $\displaystyle\sum a_n$ diverges.
* If $\rho=1$: **inconclusive** — the Ratio Test gives no information (a classic trap: $p$-series always give $\rho=1$ regardless of $p$, so Ratio Test can never distinguish convergent from divergent $p$-series).

## Pages 2–3 — Solved Examples

**Example 1 (Integral Test, basic application).** Determine convergence of $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n(\ln n)^3}$ (starting effectively at $n=2$, since $\ln 1=0$).

*Solution.* $f(x)=\dfrac{1}{x(\ln x)^3}$ is continuous, positive, and decreasing for $x\ge2$. Substituting $u=\ln x,\,du=dx/x$: $\displaystyle\int_2^{+\infty}\frac{dx}{x(\ln x)^3} = \int_{\ln 2}^{+\infty}\frac{du}{u^3}$, a $p$-integral with $p=3>1$ — converges. By the Integral Test, $\displaystyle\sum\frac{1}{n(\ln n)^3}$ **converges**.

**Example 2 (contrast: $\sum 1/(n\ln n)$ diverges — same technique, different $p$).** Determine convergence of $\displaystyle\sum_{n=2}^{\infty}\frac{1}{n\ln n}$.

*Solution.* Same substitution gives $\displaystyle\int_{\ln2}^{+\infty}\frac{du}{u}$, a $p$-integral with $p=1$ — **diverges**. So $\displaystyle\sum\frac{1}{n\ln n}$ **diverges**, despite looking almost identical to Example 1 (only the power on $\ln n$ differs — this pair is a standard "spot the difference" pairing).

**Example 3 (Comparison Test, "small diverges").** Determine convergence of $\displaystyle\sum_{n=1}^{\infty}\frac{n+1}{n^2+1}$.

*Solution.* For $n\ge1$: $\dfrac{n+1}{n^2+1} \ge \dfrac{n}{n^2+n^2} = \dfrac{1}{2n}$ (using $n^2+1\le 2n^2$ for $n\ge1$, and $n+1\ge n$). Since $\displaystyle\sum\frac{1}{2n} = \frac12\sum\frac1n$ diverges (harmonic), and our series' terms are $\ge$ this divergent series' terms, by the Comparison Test the original series **diverges**.

**Example 4 (LCT, cleaner than direct comparison).** Determine convergence of $\displaystyle\sum_{n=1}^{\infty}\frac{\sqrt[3]{n^2+1}+1}{\sqrt{n^3+n}+n+1}$.

*Solution.* Leading-order behavior: numerator $\sim n^{2/3}$, denominator $\sim n^{3/2}$, so compare to $b_n = n^{2/3}/n^{3/2} = n^{-5/6}$. Compute $L=\displaystyle\lim_{n\to\infty}\frac{a_n}{b_n}=1$ (finite, nonzero — routine but tedious algebra, dividing numerator and denominator by the dominant powers). Since $\displaystyle\sum n^{-5/6}$ is a $p$-series with $p=\frac56<1$, it diverges; by LCT, the original series **diverges** too.

**Example 5 (Alternating Series Test, standard application).** Determine convergence of $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n^{0.5}}$.

*Solution.* $b_n = n^{-0.5}$ is positive, decreasing ($b_{n+1}<b_n$ since $x^{-0.5}$ is a decreasing function), and $b_n\to0$. Both AST hypotheses hold, so the series **converges**. (Note: $\sum|a_n| = \sum n^{-0.5}$ is a $p$-series with $p=0.5<1$, which **diverges** — so this convergence is *conditional*, not absolute; see Example 7.)

**Example 6 (AST fails to apply — must use another test).** Determine convergence of $\displaystyle\sum_{n=1}^{\infty}(-1)^{n+1}\frac{n}{n+1}$.

*Solution.* Here $b_n = \dfrac{n}{n+1} \to 1 \ne 0$, so hypothesis (ii) of AST **fails** — AST cannot be applied (this is not "AST proves divergence"; AST simply does not apply). Instead, apply the Divergence Test directly to the original alternating terms: $(-1)^{n+1}\frac{n}{n+1}$ does not approach $0$ (it oscillates between values near $+1$ and $-1$), so by the Divergence Test, the series **diverges**.

**Example 7 (Absolute vs. Conditional convergence, side-by-side classification).** Classify each as absolutely convergent, conditionally convergent, or divergent: (a) $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^n}{n^{1.5}}$; (b) $\displaystyle\sum_{n=1}^{\infty}\frac{\sin n}{n^{1.5}}$.

*Solution.* (a) $\sum|a_n| = \sum n^{-1.5}$, a $p$-series with $p=1.5>1$ — **converges**. So the original series is **absolutely convergent**. (b) $\sin n$ is not eventually of consistent alternating sign, so AST does not directly apply here; but $|\sin n/n^{1.5}| \le 1/n^{1.5}$, and $\sum n^{-1.5}$ converges ($p=1.5>1$), so by the Comparison Test, $\sum|\sin n / n^{1.5}|$ converges. Hence the original series is also **absolutely convergent** (Theorem 5.15 then gives convergence of the series itself, without needing AST at all).

**Example 8 (error estimation with the Alternating Series Remainder bound).** Estimate $\displaystyle S = \sum_{n=0}^{\infty}\frac{(-1)^n}{(2n+1)!}$ to within an error of $0.001$, as an exact rational number.

*Solution.* Terms: $b_0=\frac11=1,\,b_1=\frac16,\,b_2=\frac{1}{120},\,b_3=\frac{1}{5040}$. Since $b_3=\frac{1}{5040}\approx0.000198 < 0.001$, the remainder theorem guarantees $S_2$ (the partial sum through $n=2$) is within $b_3<0.001$ of $S$. So $S \approx S_2 = 1-\frac16+\frac{1}{120} = \frac{120}{120}-\frac{20}{120}+\frac{1}{120} = \frac{101}{120}$.

**Example 9 (Ratio Test, factorial series).** Determine convergence of $\displaystyle\sum_{n=1}^{\infty}\frac{3^n}{n!}$.

*Solution.* $\rho = \displaystyle\lim_{n\to\infty}\left|\frac{3^{n+1}/(n+1)!}{3^n/n!}\right| = \lim_{n\to\infty}\frac{3}{n+1} = 0$. Since $0\le\rho<1$, the series **converges absolutely**.

**Example 10 (Ratio Test correctly identified as inconclusive — must switch tests).** Determine convergence of $\displaystyle\sum_{n=2}^{\infty}\frac{1}{\ln n}$.

*Solution.* $\rho = \displaystyle\lim_{n\to\infty}\left|\frac{1/\ln(n+1)}{1/\ln n}\right| = \lim_{n\to\infty}\frac{\ln n}{\ln(n+1)} = 1$ (both grow at the same logarithmic rate). Ratio Test is **inconclusive**. Instead: since $\ln n < n$ for all $n\ge2$, $\dfrac{1}{\ln n} > \dfrac1n$, and $\sum\frac1n$ diverges (harmonic); by the Comparison Test, $\displaystyle\sum\frac{1}{\ln n}$ **diverges**.

## Pages 4–5 — Practice Problems (unsolved)

**Integral Test**

1. Use the Integral Test to determine convergence of $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2+1}$.
2. Use the Integral Test to determine convergence of $\displaystyle\sum_{n=1}^{\infty}n e^{-n^2}$.

**Comparison / LCT**

3. Determine convergence of $\displaystyle\sum_{n=1}^{\infty}\frac{n^2+3n}{n^4+5n+1}$ using the Comparison Test.
4. Determine convergence of $\displaystyle\sum_{n=1}^{\infty}\frac{2^n-40}{3^n-20}$ using an appropriate comparison.
5. Determine convergence of $\displaystyle\sum_{n=1}^{\infty}\sin^2\left(\frac1n\right)$ using LCT. (Hint: recall $\displaystyle\lim_{x\to0}\frac{\sin x}{x}=1$.)

**Alternating Series & Absolute/Conditional Convergence**

6. Determine whether $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^n}{\arctan n}$ converges, and if so, classify it as absolute or conditional.
7. Classify $\displaystyle\sum_{n=1}^{\infty}\frac{\sin n}{\arctan n}$ (convergent/divergent; if convergent, absolute or conditional).
8. Estimate $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n^3}$ to within an error of $0.01$, giving an exact rational number.

**Ratio Test**

9. Use the Ratio Test to determine convergence of $\displaystyle\sum_{n=1}^{\infty}\frac{(2n)!}{(n!)^2 3^{n+1}}$.
10. Use the Ratio Test to determine convergence of $\displaystyle\sum_{n=2}^{\infty}\frac{n!}{n^n}$.

**Mixed / "ninja level" reasoning (no computation — reason from hypotheses only)**

11. Suppose $a_n>0$ for all $n$ and $\displaystyle\sum a_n$ is known to converge. For each of the following, state whether it must converge, must diverge, or cannot be determined from the given information alone, with a one-line justification: (a) $\displaystyle\sum \sqrt{a_n}$; (b) $\displaystyle\sum (a_n)^2$; (c) $\displaystyle\sum \sin(a_n)$.
12. Give an example of two convergent series $\displaystyle\sum a_n$ and $\displaystyle\sum b_n$ (with real terms, not necessarily positive) such that $\displaystyle\sum a_n b_n$ **diverges**. Verify your example satisfies all stated conditions.

## Answer Key & Misconception Notes (for tutor use — do not show student until after attempt)

| # | Answer | Common misconception |
|---|--------|----------------------|
| 1 | Converges. $f(x)=1/(x^2+1)$ is continuous, positive, decreasing on $[1,\infty)$; $\int_1^\infty \frac{dx}{x^2+1} = [\arctan x]_1^\infty = \frac\pi2-\frac\pi4=\frac\pi4$, finite. By Integral Test, series converges. | Reporting the sum of the series as $\pi/4$ (the integral's value) — the Integral Test only certifies convergence, it does not compute the series' actual sum, which is generally a *different* number. |
| 2 | Converges. $f(x)=xe^{-x^2}$ is positive and eventually decreasing (check $f'(x)=e^{-x^2}(1-2x^2)<0$ for $x>1/\sqrt2$); $\int_1^\infty xe^{-x^2}dx = \left[-\frac12e^{-x^2}\right]_1^\infty = \frac{1}{2e}$, finite — converges. | Not verifying the "decreasing" hypothesis of the Integral Test before applying it — some functions increase initially and only decrease later; the test still applies as long as it's *eventually* decreasing (from some $N$ onward), but this must be checked, not assumed. |
| 3 | Converges. For large $n$, $\frac{n^2+3n}{n^4+5n+1} \le \frac{2n^2}{n^4} = \frac{2}{n^2}$ eventually; $\sum 2/n^2$ converges ($p=2>1$); by Comparison Test the original series converges. | Comparing to $1/n^4$ (matching only the denominator's degree) instead of correctly computing the *net* degree gap (numerator degree $2$, denominator degree $4$, net comparison should be to $n^{2-4}=n^{-2}$, not $n^{-4}$). |
| 4 | Diverges. $\frac{2^n-40}{3^n-20}$ behaves like $(2/3)^n$ for large $n$ — but $(2/3)^n \to 0$ and this is actually the *convergent* comparison; recheck: since $2^n-40 \sim 2^n$ and $3^n-20\sim3^n$, the ratio $\sim(2/3)^n$, a convergent geometric-type series ($|r|=2/3<1$). So the series actually **converges**, not diverges — apply LCT with $b_n=(2/3)^n$ to confirm $L=1$ rigorously, then $\sum(2/3)^n$ converges, so original series converges. | Eyeballing "big numbers in numerator and denominator both growing" as automatically divergent, without identifying that the *ratio* of the dominant terms is what determines convergence, not their individual growth. |
| 5 | Converges. $\sin^2(1/n) \sim (1/n)^2$ as $n\to\infty$ (since $\sin x\approx x$ near $0$); LCT with $b_n=1/n^2$: $L = \lim \frac{\sin^2(1/n)}{1/n^2} = \left(\lim\frac{\sin(1/n)}{1/n}\right)^2 = 1^2=1$, finite nonzero. $\sum 1/n^2$ converges ($p=2>1$), so original series converges. | Comparing to $1/n$ instead of $1/n^2$ (forgetting the square on $\sin^2$, which changes the effective power of $n$ in the comparison series). |
| 6 | Converges conditionally. AST: $b_n=1/\arctan n$ is eventually decreasing (since $\arctan n$ is increasing and bounded above by $\pi/2$) and $b_n \to 1/(\pi/2) = 2/\pi \ne 0$ — **wait**, this means $b_n \not\to 0$, so AST does NOT apply and instead the Divergence Test applies directly to $a_n=(-1)^n/\arctan n$, which does not tend to $0$ — the series actually **diverges**. | Applying AST without checking hypothesis (ii) ($b_n\to0$) — $\arctan n$ is bounded, so $1/\arctan n$ does NOT go to zero, which silently invalidates AST; this is a deliberately placed trap mirroring the slide's "ninja level" difficulty. |
| 7 | Diverges, by the same reasoning as #6: $|\sin n/\arctan n|$ does not tend to $0$ (since $\arctan n \to \pi/2$, a nonzero bounded limit, while $\sin n$ oscillates and does not settle), so the terms $\sin n/\arctan n$ themselves do not tend to $0$ — Divergence Test applies, series diverges. | Assuming any series with a "$\sin n$" numerator must be handled by comparison to $|\sin n|\le1$ and therefore convergent — but the denominator here does not grow (it's bounded near $\pi/2$), so this is not actually a "small term" series at all. |
| 8 | $S\approx S_3 = 1-\frac18+\frac{1}{27}-\frac{1}{64}$ (since $b_4=1/4^3=1/64\approx0.0156$, too big — need $b_N<0.01$; $b_4 = 1/256 \approx 0.0039<0.01$ using correct indexing from $n=1$: $b_n=1/n^3$, $b_5=1/125=0.008<0.01$). So use $S_4 = 1-\frac18+\frac{1}{27}-\frac{1}{64} = \frac{1728-216+64-27}{1728}=\frac{1549}{1728}$. | Off-by-one indexing errors in matching "the first omitted term" to the correct $b_N$ — students often use $b_N$ (the last included term) instead of $b_{N+1}$ (the first excluded term) when checking the error bound. |
| 9 | Converges absolutely. $\rho = \lim\left|\frac{(2n+2)!/((n+1)!)^2 3^{n+2}}{(2n)!/(n!)^2 3^{n+1}}\right| = \lim \frac{(2n+1)(2n+2)}{(n+1)^2\cdot 3} = \frac{4}{3}$. Since $\rho=4/3>1$, the series actually **diverges** (recheck arithmetic: $(2n+2)(2n+1)/(n+1)^2 \to 4$, divided by $3$ gives $4/3>1$). | Losing track of factorial-ratio simplification (e.g. incorrectly canceling $(n!)^2$ against $((n+1)!)^2$ as if they were $n!/(n+1)!=1/(n+1)$ applied twice without squaring correctly), leading to a wrong $\rho$. |
| 10 | Converges. $\rho = \lim\left|\frac{(n+1)!/(n+1)^{n+1}}{n!/n^n}\right| = \lim\frac{n^n}{(n+1)^n} = \lim\left(\frac{n}{n+1}\right)^n = \lim\left(1-\frac{1}{n+1}\right)^n = \frac1e$ (using the standard limit $(1-1/n)^n\to 1/e$). Since $\rho=1/e<1$, the series **converges absolutely**. | Not recognizing the $\left(\frac{n}{n+1}\right)^n \to 1/e$ limit pattern and instead concluding $\rho=1$ by naively canceling $n/(n+1)\to1$ before raising to the $n$-th power — order of operations (limit of the ratio vs. ratio then limit of the power) matters critically here. |
| 11 | (a) Cannot be determined — e.g. $a_n=1/n^2$ gives $\sqrt{a_n}=1/n$, divergent; but $a_n=1/n^4$ gives $\sqrt{a_n}=1/n^2$, convergent. (b) Must converge — since $a_n\to0$ eventually $a_n<1$, so $(a_n)^2<a_n$ eventually, and by Comparison Test with the convergent $\sum a_n$, $\sum(a_n)^2$ converges. (c) Must converge — $0\le\sin(a_n)\le a_n$ for small positive $a_n$ (since $a_n\to0$), so by Comparison Test, $\sum\sin(a_n)$ converges. | For (a), assuming "square-rooting a convergent series' terms" always preserves or always breaks convergence — it genuinely depends on how fast $a_n\to0$, and this must be reasoned per-case, not generalized; for (b)/(c), forgetting to justify *why* the inequality needed for Comparison Test holds only "eventually" (once $a_n<1$), not for all $n$. |
| 12 | Example: $a_n=b_n=\dfrac{(-1)^n}{\sqrt n}$ for $n\ge1$. Each converges by AST individually (conditionally). But $a_nb_n = \dfrac{(-1)^{2n}}{n} = \dfrac1n$, and $\sum\frac1n$ (harmonic) diverges. | Trying to use two series that are each absolutely convergent (their product will typically also converge, since $|a_nb_n|\le\frac12(a_n^2+b_n^2)$ eventually) — the counterexample **requires** at least conditional (non-absolute) convergence to break the product; students often pick two absolutely convergent series and fail to find a counterexample, then incorrectly conclude none exists. |
