# Week 10 — Convergence Tests II: Alternating Series, Absolute/Conditional Convergence & the Ratio Test

**Session length:** 60 minutes (Pages 1–5, self-paced)
**Source:** OpenStax *Calculus Volume 2*, §5.5 (Alternating Series Test Theorem 5.13; Remainder Theorem 5.14; Absolute Convergence Implies Convergence Theorem 5.15), §5.6 (Ratio Test Theorem 5.16). MAT137 Unit 13 slides (13.15–13.19: alternating series test and error estimation, absolute vs. conditional convergence, "ninja level" convergence puzzles, ratio test) — MAT137 is the University of Toronto's official exclusion-equivalent of MATA37H3.

## Page 1 — Definitions and Key Facts

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

**Example 1 (Alternating Series Test, standard application).** Determine convergence of $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n^{0.5}}$.

*Solution.* $b_n = n^{-0.5}$ is positive, decreasing ($b_{n+1}<b_n$ since $x^{-0.5}$ is a decreasing function), and $b_n\to0$. Both AST hypotheses hold, so the series **converges**. (Note: $\sum|a_n| = \sum n^{-0.5}$ is a $p$-series with $p=0.5<1$, which **diverges** — so this convergence is *conditional*, not absolute; see Example 3.) $\blacksquare$

**Example 2 (AST fails to apply — must use another test).** Determine convergence of $\displaystyle\sum_{n=1}^{\infty}(-1)^{n+1}\frac{n}{n+1}$.

*Solution.* Here $b_n = \dfrac{n}{n+1} \to 1 \ne 0$, so hypothesis (ii) of AST **fails** — AST cannot be applied (this is not "AST proves divergence"; AST simply does not apply). Instead, apply the Divergence Test directly to the original alternating terms: $(-1)^{n+1}\frac{n}{n+1}$ does not approach $0$ (it oscillates between values near $+1$ and $-1$), so by the Divergence Test, the series **diverges**. $\blacksquare$

**Example 3 (Absolute vs. Conditional convergence, side-by-side classification).** Classify each as absolutely convergent, conditionally convergent, or divergent: (a) $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^n}{n^{1.5}}$; (b) $\displaystyle\sum_{n=1}^{\infty}\frac{\sin n}{n^{1.5}}$.

*Solution.* (a) $\sum|a_n| = \sum n^{-1.5}$, a $p$-series with $p=1.5>1$ — **converges**. So the original series is **absolutely convergent**. (b) $\sin n$ is not eventually of consistent alternating sign, so AST does not directly apply here; but $|\sin n/n^{1.5}| \le 1/n^{1.5}$, and $\sum n^{-1.5}$ converges ($p=1.5>1$), so by the Comparison Test, $\sum|\sin n / n^{1.5}|$ converges. Hence the original series is also **absolutely convergent** (Theorem 5.15 then gives convergence of the series itself, without needing AST at all). $\blacksquare$

**Example 4 (error estimation with the Alternating Series Remainder bound).** Estimate $\displaystyle S = \sum_{n=0}^{\infty}\frac{(-1)^n}{(2n+1)!}$ to within an error of $0.001$, as an exact rational number.

*Solution.* Terms: $b_0=\frac11=1,\,b_1=\frac16,\,b_2=\frac{1}{120},\,b_3=\frac{1}{5040}$. Since $b_3=\frac{1}{5040}\approx0.000198 < 0.001$, the remainder theorem guarantees $S_2$ (the partial sum through $n=2$) is within $b_3<0.001$ of $S$. So $S \approx S_2 = 1-\frac16+\frac{1}{120} = \frac{120}{120}-\frac{20}{120}+\frac{1}{120} = \frac{101}{120}$. $\blacksquare$

**Example 5 (Ratio Test, factorial series).** Determine convergence of $\displaystyle\sum_{n=1}^{\infty}\frac{3^n}{n!}$.

*Solution.* $\rho = \displaystyle\lim_{n\to\infty}\left|\frac{3^{n+1}/(n+1)!}{3^n/n!}\right| = \lim_{n\to\infty}\frac{3}{n+1} = 0$. Since $0\le\rho<1$, the series **converges absolutely**. $\blacksquare$

**Example 6 (Ratio Test correctly identified as inconclusive — must switch tests).** Determine convergence of $\displaystyle\sum_{n=2}^{\infty}\frac{1}{\ln n}$.

*Solution.* $\rho = \displaystyle\lim_{n\to\infty}\left|\frac{1/\ln(n+1)}{1/\ln n}\right| = \lim_{n\to\infty}\frac{\ln n}{\ln(n+1)} = 1$ (both grow at the same logarithmic rate). Ratio Test is **inconclusive**. Instead: since $\ln n < n$ for all $n\ge2$, $\dfrac{1}{\ln n} > \dfrac1n$, and $\sum\frac1n$ diverges (harmonic); by the Comparison Test, $\displaystyle\sum\frac{1}{\ln n}$ **diverges**. $\blacksquare$

## Pages 4–5 — Practice Problems (unsolved)

**Alternating Series & Absolute/Conditional Convergence**

1. Determine whether $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^n}{\arctan n}$ converges, and if so, classify it as absolute or conditional.
2. Classify $\displaystyle\sum_{n=1}^{\infty}\frac{\sin n}{\arctan n}$ (convergent/divergent; if convergent, absolute or conditional).
3. Estimate $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n^3}$ to within an error of $0.01$, giving an exact rational number.
4. Classify $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^n\sqrt n}{n+3}$ (convergent/divergent; if convergent, absolute or conditional).

**Ratio Test**

5. Use the Ratio Test to determine convergence of $\displaystyle\sum_{n=1}^{\infty}\frac{(2n)!}{(n!)^2 3^{n+1}}$.
6. Use the Ratio Test to determine convergence of $\displaystyle\sum_{n=2}^{\infty}\frac{n!}{n^n}$.
7. Use the Ratio Test to determine convergence of $\displaystyle\sum_{n=1}^{\infty}\frac{n^2}{2^n}$.

**Mixed / "ninja level" reasoning (no computation — reason from hypotheses only)**

8. Suppose $a_n>0$ for all $n$ and $\displaystyle\sum a_n$ is known to converge. For each of the following, state whether it must converge, must diverge, or cannot be determined from the given information alone, with a one-line justification: (a) $\displaystyle\sum \sqrt{a_n}$; (b) $\displaystyle\sum (a_n)^2$; (c) $\displaystyle\sum \sin(a_n)$.
9. Give an example of two convergent series $\displaystyle\sum a_n$ and $\displaystyle\sum b_n$ (with real terms, not necessarily positive) such that $\displaystyle\sum a_n b_n$ **diverges**. Verify your example satisfies all stated conditions.
10. A series $\sum a_n$ satisfies $\rho=\lim|a_{n+1}/a_n|=1$ exactly. Explain why the Ratio Test alone can never distinguish between $\sum 1/n$ (divergent) and $\sum 1/n^2$ (convergent), even though both give $\rho=1$, and state which test(s) from this week and last week correctly handle both cases.

## Answer Key & Misconception Notes (for tutor use — do not show student until after attempt)

| # | Answer | Common misconception |
|---|--------|----------------------|
| 1 | Diverges. $b_n=1/\arctan n$ is eventually decreasing (since $\arctan n$ is increasing and bounded above by $\pi/2$), but $b_n \to 1/(\pi/2) = 2/\pi \ne 0$ — hypothesis (ii) of AST fails, so AST does NOT apply. Instead the Divergence Test applies directly to $a_n=(-1)^n/\arctan n$, which does not tend to $0$ — the series diverges. | Applying AST without checking hypothesis (ii) ($b_n\to0$) — $\arctan n$ is bounded, so $1/\arctan n$ does NOT go to zero, which silently invalidates AST; this is a deliberately placed trap mirroring the "ninja level" difficulty from the source slides. |
| 2 | Diverges, by the same reasoning as #1: $|\sin n/\arctan n|$ does not tend to $0$ (since $\arctan n \to \pi/2$, a nonzero bounded limit, while $\sin n$ oscillates and does not settle), so the terms $\sin n/\arctan n$ themselves do not tend to $0$ — Divergence Test applies, series diverges. | Assuming any series with a "$\sin n$" numerator must be handled by comparison to $|\sin n|\le1$ and therefore convergent — but the denominator here does not grow (it's bounded near $\pi/2$), so this is not actually a "small term" series at all. |
| 3 | $S\approx S_4 = 1-\frac18+\frac{1}{27}-\frac{1}{64}=\frac{1728-216+64-27}{1728}=\frac{1549}{1728}$, since $b_5=1/125=0.008<0.01$ certifies the error after 4 terms is within the target. | Off-by-one indexing errors in matching "the first omitted term" to the correct $b_N$ — students often use $b_N$ (the last included term) instead of $b_{N+1}$ (the first excluded term) when checking the error bound. |
| 4 | Conditionally convergent. AST: $b_n=\sqrt n/(n+3)$ is eventually decreasing and $b_n\to0$ (since $\sqrt n/(n+3)\sim n^{-1/2}\to0$), so the series converges. But $\sum|a_n| = \sum \sqrt n/(n+3) \sim \sum n^{-1/2}$, a divergent $p$-series ($p=1/2\le1$) — so the convergence is conditional, not absolute. | Concluding "absolutely convergent" just because the series converges by AST — AST convergence says nothing about whether $\sum|a_n|$ converges; that must be checked separately, and here it does not. |
| 5 | Diverges. $\rho = \lim\left|\frac{(2n+2)!/((n+1)!)^2 3^{n+2}}{(2n)!/(n!)^2 3^{n+1}}\right| = \lim \frac{(2n+1)(2n+2)}{(n+1)^2\cdot 3} = \frac{4}{3}>1$, so the series diverges. | Losing track of factorial-ratio simplification (e.g. incorrectly canceling $(n!)^2$ against $((n+1)!)^2$ as if they were $n!/(n+1)!=1/(n+1)$ applied twice without squaring correctly), leading to a wrong $\rho$. |
| 6 | Converges. $\rho = \lim\left|\frac{(n+1)!/(n+1)^{n+1}}{n!/n^n}\right| = \lim\frac{n^n}{(n+1)^n} = \lim\left(\frac{n}{n+1}\right)^n = \lim\left(1-\frac{1}{n+1}\right)^n = \frac1e$ (using the standard limit $(1-1/n)^n\to 1/e$). Since $\rho=1/e<1$, the series **converges absolutely**. | Not recognizing the $\left(\frac{n}{n+1}\right)^n \to 1/e$ limit pattern and instead concluding $\rho=1$ by naively canceling $n/(n+1)\to1$ before raising to the $n$-th power — order of operations (limit of the ratio vs. ratio then limit of the power) matters critically here. |
| 7 | Converges. $\rho=\lim\left|\frac{(n+1)^2/2^{n+1}}{n^2/2^n}\right| = \lim\frac{(n+1)^2}{2n^2}=\frac12$. Since $\rho=1/2<1$, the series converges absolutely. | Forgetting to take the limit as $n\to\infty$ after forming the ratio — the ratio $(n+1)^2/(2n^2)$ is not itself $1/2$ for small $n$, only in the limit, and some students stop at the unsimplified ratio and misjudge $\rho$. |
| 8 | (a) Cannot be determined — e.g. $a_n=1/n^2$ gives $\sqrt{a_n}=1/n$, divergent; but $a_n=1/n^4$ gives $\sqrt{a_n}=1/n^2$, convergent. (b) Must converge — since $a_n\to0$ eventually $a_n<1$, so $(a_n)^2<a_n$ eventually, and by Comparison Test with the convergent $\sum a_n$, $\sum(a_n)^2$ converges. (c) Must converge — $0\le\sin(a_n)\le a_n$ for small positive $a_n$ (since $a_n\to0$), so by Comparison Test, $\sum\sin(a_n)$ converges. | For (a), assuming "square-rooting a convergent series' terms" always preserves or always breaks convergence — it genuinely depends on how fast $a_n\to0$, and this must be reasoned per-case, not generalized; for (b)/(c), forgetting to justify *why* the inequality needed for Comparison Test holds only "eventually" (once $a_n<1$), not for all $n$. |
| 9 | Example: $a_n=b_n=\dfrac{(-1)^n}{\sqrt n}$ for $n\ge1$. Each converges by AST individually (conditionally). But $a_nb_n = \dfrac{(-1)^{2n}}{n} = \dfrac1n$, and $\sum\frac1n$ (harmonic) diverges. | Trying to use two series that are each absolutely convergent (their product will typically also converge, since $|a_nb_n|\le\frac12(a_n^2+b_n^2)$ eventually) — the counterexample **requires** at least conditional (non-absolute) convergence to break the product; students often pick two absolutely convergent series and fail to find a counterexample, then incorrectly conclude none exists. |
| 10 | The Ratio Test compares consecutive-term ratios, which converge to $1$ for *every* $p$-series regardless of $p$ — the test simply cannot see the difference in growth rate that distinguishes $p=1$ (divergent) from $p=2$ (convergent). The Integral Test or the (Limit) Comparison Test from Week 9, which directly examine the $p$-series' own convergence behavior, correctly resolve both cases. | Assuming $\rho=1$ means "the series is borderline convergent" or trying to force a conclusion from the Ratio Test anyway — $\rho=1$ means strictly "try a different test," never a weak or partial answer from the Ratio Test itself. |
