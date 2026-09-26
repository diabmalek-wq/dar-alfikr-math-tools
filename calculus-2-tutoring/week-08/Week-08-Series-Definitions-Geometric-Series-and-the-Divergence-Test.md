# Week 8 — Series: Definitions, Geometric Series & the Divergence Test

**Session length:** 60 minutes (Pages 1–5, self-paced)
**Source:** OpenStax *Calculus Volume 2*, §5.2 (Infinite Series — partial sums, geometric series, telescoping, Theorem 5.7) and §5.3 (Divergence Test, Theorem 5.8). MAT137 Unit 13 slides (13.1–13.9: definition of series via partial sums, telescoping series, tail-of-a-series properties, geometric series, the $0.999\ldots=1$ problem, necessary-condition/divergence-test True-or-False).

## Page 1 — Definitions and Key Facts

### Definition: Infinite Series and Partial Sums

An infinite series is a sum of infinitely many terms, written $\displaystyle\sum_{n=1}^{\infty} a_n = a_1+a_2+a_3+\cdots$. The **$k$-th partial sum** is the finite sum $\displaystyle S_k = \sum_{n=1}^{k} a_n = a_1+a_2+\cdots+a_k$. The series is defined as the limit of its partial-sum sequence:
$$\sum_{n=1}^{\infty} a_n = \lim_{k\to\infty} S_k.$$
If this limit exists (is a finite number), the series **converges** to that value; if the limit fails to exist or is $\pm\infty$, the series **diverges**. A series can diverge in three distinct ways: to $+\infty$, to $-\infty$, or by **oscillating** (the partial sums never settle, e.g. $\sum(-1)^n$).

### Key Fact: The Tail of a Series

Convergence is a "long-run" (tail) property: for any fixed integer $N$, $\displaystyle\sum_{n=0}^{\infty} a_n$ converges **if and only if** $\displaystyle\sum_{n=N}^{\infty} a_n$ converges — changing, adding, or removing finitely many leading terms never changes whether a series converges, though it **does** change the value it converges to. (Do not confuse "convergent" with "converges to a specific relative size" — dropping the first $N$ terms only ever subtracts a *finite* amount, so it cannot turn a divergent series convergent or vice versa, but it does shift the sum.)

### Theorem: Algebraic Properties of Convergent Series

If $\displaystyle\sum a_n$ and $\displaystyle\sum b_n$ both converge, then: (i) $\displaystyle\sum(a_n+b_n) = \sum a_n + \sum b_n$ (Sum Rule); (ii) $\displaystyle\sum(a_n-b_n) = \sum a_n - \sum b_n$ (Difference Rule); (iii) for any constant $c$, $\displaystyle\sum ca_n = c\sum a_n$ (Constant Multiple Rule). **These rules require both series to already be known convergent** — you may not split a series into two pieces and sum each separately unless you first establish that both pieces converge (see Example 3's misconception flag).

### Definition: Geometric Series

A geometric series has the form $\displaystyle\sum_{n=1}^{\infty} ar^{n-1} = a+ar+ar^2+ar^3+\cdots$, where $a$ is the initial term and $r$ is the common ratio. Its $k$-th partial sum is $S_k = \dfrac{a(1-r^k)}{1-r}$ for $r\ne 1$. Consequently:
$$\sum_{n=1}^{\infty} ar^{n-1} = \frac{a}{1-r} \quad \text{if } |r|<1, \qquad\qquad \sum_{n=1}^{\infty} ar^{n-1} \text{ diverges if } |r|\ge 1.$$
The starting index matters for the formula: if a geometric series starts at $n=k$ instead of $n=1$, write out the first term explicitly and re-apply $\dfrac{\text{first term}}{1-r}$ rather than reusing the $n=1$ formula blindly.

### Key Fact: Telescoping Series

A telescoping series is one whose partial sum collapses because consecutive terms cancel: if $a_n = b_n - b_{n+1}$, then $S_k = b_1 - b_{k+1}$, so $\displaystyle\sum_{n=1}^{\infty} a_n = b_1 - \lim_{k\to\infty} b_{k+1}$ (provided that limit exists). Partial fractions is the standard way to reveal this telescoping structure in a rational-function series.

### Theorem: The Divergence Test (Necessary Condition)

If $\displaystyle\lim_{n\to\infty} a_n \ne 0$ or the limit does not exist, then $\displaystyle\sum_{n=1}^{\infty} a_n$ **diverges**. Equivalently: convergence of $\sum a_n$ **requires** $a_n \to 0$. This is a **one-directional** test — it can only prove divergence, never convergence. If $a_n \to 0$, the Divergence Test gives **no information at all** (the series might converge or might diverge — the harmonic series $\sum 1/n$ is the standard counterexample: $1/n \to 0$ but the series diverges).

## Pages 2–3 — Solved Examples

**Example 1 (partial sums built directly, geometric — a "real-world" setup).** Oil seeps into a lake: $1000$ gal week 1, then half as much each subsequent week ($500, 250, 125,\ldots$). In thousands of gallons, express the total amount after $k$ weeks as a partial sum, then find the long-run total.

*Solution.* Week $n$ contributes $(1/2)^{n-1}$ (thousand gallons), so $\displaystyle S_k = \sum_{n=1}^{k}\left(\frac12\right)^{n-1}$, a geometric partial sum with $a=1,\,r=\frac12$. As $k\to\infty$: $\displaystyle\sum_{n=1}^{\infty}\left(\frac12\right)^{n-1} = \frac{1}{1-\frac12} = 2$. The total amount of oil approaches (but never reaches) $2000$ gallons.

**Example 2 (telescoping series via partial fractions).** Evaluate $\displaystyle\sum_{n=1}^{\infty} \frac{1}{n^2+2n}$.

*Solution.* Partial fractions: $\dfrac{1}{n^2+2n} = \dfrac{1}{n(n+2)} = \dfrac{1}{2}\left(\dfrac1n - \dfrac{1}{n+2}\right)$ (check: $\frac{1}{2}\cdot\frac{(n+2)-n}{n(n+2)} = \frac{1}{2}\cdot\frac{2}{n(n+2)}=\frac{1}{n(n+2)}$ ✓). This telescopes with a **gap of 2**, so consecutive terms don't fully cancel — write out several terms:
$$S_k = \frac12\left[\left(1-\frac13\right)+\left(\frac12-\frac14\right)+\left(\frac13-\frac15\right)+\cdots+\left(\frac1k-\frac{1}{k+2}\right)\right] = \frac12\left[1+\frac12-\frac{1}{k+1}-\frac{1}{k+2}\right].$$
As $k\to\infty$, the last two terms vanish, giving $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2+2n} = \frac12\left(1+\frac12\right) = \frac34$.

**Example 3 (spot the error — splitting a divergent series illegally).** A "proof" claims $\displaystyle\sum_{n=2}^{\infty}\ln\frac{n}{n+1} = \ln 2$ by writing $\sum[\ln n - \ln(n+1)] = \sum\ln n - \sum\ln(n+1) = (\ln2+\ln3+\cdots)-(\ln3+\ln4+\cdots) = \ln2$. Find the error and fix it.

*Solution.* The error is applying the **Difference Rule** (Theorem 5.7ii) to split $\sum[\ln n - \ln(n+1)]$ into $\sum\ln n - \sum\ln(n+1)$ — but $\displaystyle\sum_{n=2}^{\infty}\ln n$ and $\displaystyle\sum_{n=2}^{\infty}\ln(n+1)$ **each diverge individually** (to $+\infty$), and "$\infty - \infty$" is not a valid algebraic manipulation. The Difference Rule requires **both series to already converge** before you're allowed to split them; it was never checked here. The correct approach is to work with partial sums directly (proper telescoping): $S_k = \displaystyle\sum_{n=2}^{k}[\ln n - \ln(n+1)] = \ln 2 - \ln(k+1)$ (everything else cancels). As $k\to\infty$, $\ln(k+1)\to\infty$, so $S_k \to -\infty$. The series actually **diverges to $-\infty$** — the claimed answer of $\ln 2$ is wrong, and the true behavior is the opposite of "converges to a finite number."

**Example 4 (geometric series with a shifted/altered index).** Evaluate $\displaystyle\sum_{n=1}^{\infty}(-1)^n\frac{3^n}{2^{2n+1}}$.

*Solution.* Rewrite the general term as a single ratio to a power of $n$: $(-1)^n\dfrac{3^n}{2^{2n+1}} = \dfrac{1}{2}\cdot\left(\dfrac{-3}{4}\right)^n$ (since $2^{2n+1}=2\cdot4^n$ and $(-1)^n 3^n = (-3)^n$). This is geometric with ratio $r=-\frac34$ (so $|r|<1$, convergent) but the sum starts at $n=1$, giving first term $\frac12\cdot(-\frac34) = -\frac38$. Using $\dfrac{\text{first term}}{1-r}$: $\dfrac{-3/8}{1-(-3/4)} = \dfrac{-3/8}{7/4} = -\dfrac{3}{14}$.

**Example 5 ($0.\overline{9} = 1$, geometric series application).** Write $0.999\ldots$ as a series and evaluate it.

*Solution.* $0.999\ldots = \displaystyle\sum_{n=1}^{\infty} \frac{9}{10^n} = \frac{9}{10}+\frac{9}{100}+\frac{9}{1000}+\cdots$, geometric with $a=\frac{9}{10},\,r=\frac{1}{10}$. Sum $= \dfrac{9/10}{1-1/10} = \dfrac{9/10}{9/10} = 1$. So $0.\overline{9}=1$ **exactly** — this is not an approximation or a rounding convention; it is a genuine equality proven by the geometric series formula.

**Example 6 (Divergence Test, correctly applied vs. correctly declared inconclusive).** For each series, either conclude divergence via the Divergence Test or state that the test is inconclusive: (a) $\displaystyle\sum_{n=1}^{\infty}\frac{n}{3n-1}$; (b) $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^3}$.

*Solution.* (a) $\dfrac{n}{3n-1} \to \dfrac13 \ne 0$, so by the Divergence Test, the series **diverges**. (b) $\dfrac{1}{n^3}\to 0$, so the Divergence Test is **inconclusive** — this tells us nothing about whether $\sum 1/n^3$ converges or diverges (it happens to converge, but not by this test; that requires the Integral Test or $p$-series rule from the next worksheet).

**Example 7 (properties of the partial-sum sequence — True/False reasoning).** True or False: "If $\forall n>0,\ a_n>0$, then the partial-sum sequence $\{S_n\}$ is increasing," and its converse, "If $\{S_n\}$ is increasing, then $\forall n>0,\ a_n>0$."

*Solution.* **Forward direction is TRUE**: if every term added is strictly positive, each partial sum is strictly larger than the last, i.e. $S_{n+1}=S_n+a_{n+1}>S_n$, so $\{S_n\}$ is (strictly) increasing. **Converse is FALSE**: $\{S_n\}$ increasing only requires $S_{n+1}>S_n$ for the specific indices actually compared, but a subtle trap is that the definition of "increasing" quantifies over *all* $n$, and there is no way to break it with a single counterexample of a **non-monotonic** $a_n$ sequence that still keeps every partial sum increasing — actually here, $S_{n+1}>S_n \iff a_{n+1}>0$ for every $n$, so the converse **is also TRUE** by definition. (This item is a reminder to check "if and only if" claims by working from definitions rather than assuming asymmetry — sometimes the converse of a true statement is also true, and that must be verified, not assumed false.)

## Pages 4–5 — Practice Problems (unsolved)

**Geometric series**

1. Evaluate $\displaystyle 1+\frac13+\frac19+\frac{1}{27}+\cdots$
2. Evaluate $\displaystyle\frac32-\frac94+\frac{27}{8}-\frac{81}{16}+\cdots$, or show it diverges.
3. Evaluate $\displaystyle\sum_{n=5}^{\infty}\frac{3^n}{2^{2n+1}}$.
4. Evaluate $\displaystyle\sum_{n=3}^{\infty}\frac{3^n}{1000\cdot 2^{n+2}}$, or show it diverges.
5. For which values of $x$ does $\displaystyle\sum_{n=k}^{\infty} x^n$ converge, and what does it converge to (in terms of $x$ and $k$)?

**Telescoping series**

6. Evaluate $\displaystyle\sum_{n=1}^{\infty}\frac{1}{(n+1)(n+2)}$.
7. **Spot the error, and fix it.** A student claims $\displaystyle\sum_{n=1}^{\infty}\left(\frac{1}{n}-\frac{1}{n+1}\right) = \left(\sum_{n=1}^{\infty}\frac1n\right)-\left(\sum_{n=1}^{\infty}\frac{1}{n+1}\right) = \infty - \infty$, and concludes the series diverges. Determine the actual value (or confirm divergence) using partial sums directly, and explain precisely where the student's method breaks down.

**Divergence Test**

8. Apply the Divergence Test to $\displaystyle\sum_{n=1}^{\infty}\frac{2n^2+1}{5n^2-3}$. State the conclusion.
9. Apply the Divergence Test to $\displaystyle\sum_{n=1}^{\infty}\left(1+\frac1n\right)^n$. (Recall $\displaystyle\lim_{n\to\infty}\left(1+\frac1n\right)^n=e$.)
10. Explain why the Divergence Test gives no information about $\displaystyle\sum_{n=1}^{\infty}\frac{1}{\sqrt n}$, and — using only what you currently know (not yet the Integral Test) — determine whether it converges or diverges by comparing its partial sums to an integral you can estimate geometrically, OR by relating it to the (already-known-divergent) harmonic series via a direct term-by-term inequality.

**Tail of a series / properties**

11. True or False, with justification: "If $\displaystyle\sum_{n=0}^{\infty}a_n$ converges, then $\displaystyle\sum_{n=7}^{\infty}a_n$ converges to a *smaller* number than $\displaystyle\sum_{n=0}^\infty a_n$."
12. Suppose $\displaystyle\sum_{n=1}^{\infty} a_n$ converges and $\displaystyle\sum_{n=1}^{\infty} b_n$ diverges. What can you conclude about $\displaystyle\sum_{n=1}^{\infty}(a_n+b_n)$? Prove your claim (do not just assert it).

## Answer Key & Misconception Notes (for tutor use — do not show student until after attempt)

| # | Answer | Common misconception |
|---|--------|----------------------|
| 1 | Converges to $\frac32$. $a=1,\,r=\frac13$: $\frac{1}{1-1/3}=\frac32$. | Misidentifying $a$ as the second term or misreading the ratio (e.g., using $r=3$ instead of $r=\frac13$ from writing the series "backwards"). |
| 2 | Diverges. Ratio is $r=-\frac32$ (check: $\frac{-9/4}{3/2}=-\frac32$), and $|r|=\frac32>1$, so it diverges (oscillating in sign with growing magnitude). | Only checking the ratio's sign pattern (alternating) and assuming alternating automatically implies convergence — magnitude ($|r|\ge1$) is what actually decides convergence for a geometric series, not the alternating sign alone. |
| 3 | Diverges — wait, recompute: general term is $\frac12(-\frac34)^n$ type structure only when alternating sign is present; here there's no $(-1)^n$, so this is $\frac{3^n}{2^{2n+1}}=\frac12\left(\frac34\right)^n$, ratio $r=\frac34$, $|r|<1$, **converges**. Starting at $n=5$: first term $=\frac12(\frac34)^5=\frac{243}{2048}$. Sum $=\dfrac{243/2048}{1-3/4}=\dfrac{243}{512}$. | Forgetting to recompute the "first term" when the series starts at $n=5$ instead of $n=1$ or $n=0$, and instead plugging into $\frac{a}{1-r}$ using the $n=1$ term. |
| 4 | Simplify first: $\dfrac{3^n}{1000\cdot2^{n+2}} = \dfrac{1}{4000}\left(\dfrac32\right)^n$, so the ratio is $r=\dfrac32$. Since $|r|=\dfrac32>1$, the series **diverges**. | Not simplifying the constant/exponential parts fully before reading off $r$, and mistaking a large constant coefficient ($1000$) for evidence of convergence — the coefficient is irrelevant to convergence; only $|r|$ matters. |
| 5 | Converges iff $|x|<1$; sum $=\dfrac{x^k}{1-x}$ (first term is $x^k$). | Using the $n=0$-indexed formula $\frac{1}{1-x}$ regardless of the starting index $k$, ignoring that the "first term" of the sum is $x^k$, not $1$. |
| 6 | $1$ (telescoping: $\frac{1}{(n+1)(n+2)}=\frac{1}{n+1}-\frac{1}{n+2}$, gap of 1, $S_k=\frac12-\frac{1}{k+2}\to\frac12$; wait recompute from $n=1$: $S_k = \frac{1}{2}-\frac{1}{k+2} \to \frac12$). Correct value: $\frac12$. | Off-by-one error in identifying the first surviving term of the telescoping sum (using $\frac{1}{1}$ instead of $\frac{1}{n+1}$ evaluated at the correct starting index $n=1$, i.e. $\frac{1}{2}$). |
| 7 | The series converges (it telescopes to $S_k = 1-\frac{1}{k+1}\to 1$), so the true value is $1$, not divergent. The student's error is identical to Example 3: splitting $\sum(a_n-b_n)$ into $\sum a_n - \sum b_n$ before confirming each piece converges — since $\sum \frac1n$ and $\sum\frac{1}{n+1}$ both individually diverge, "$\infty-\infty$" is undefined and the split is invalid, even though the *combined* telescoping series does converge. | Believing that because the "shortcut" split produces a divergent-looking answer, the original series must diverge — the correct method (direct partial sums) can give a completely different, finite answer. |
| 8 | Diverges. $\frac{2n^2+1}{5n^2-3}\to\frac25\ne0$, so by the Divergence Test it diverges. | Computing the limit correctly but then concluding "the terms approach a finite number, so the series converges" — confusing $a_n\to L$ (finite, nonzero) with $a_n\to 0$; only the latter is even a candidate for convergence. |
| 9 | Diverges. $\left(1+\frac1n\right)^n \to e \ne 0$, so by the Divergence Test it diverges. | Assuming any limit that "settles down" to a specific numerical value (rather than blowing up) implies series convergence, regardless of whether that value is $0$. |
| 10 | The Divergence Test is inconclusive since $\frac{1}{\sqrt n}\to0$. Direct comparison: $\frac{1}{\sqrt n} \ge \frac1n$ for all $n\ge1$, and since $\sum\frac1n$ (harmonic) diverges, by direct term-by-term reasoning on partial sums ($S_k(\frac{1}{\sqrt n}) \ge S_k(\frac1n)\to\infty$), $\sum\frac{1}{\sqrt n}$ also diverges. | Assuming a series "smaller-looking" than a divergent one (since $\sqrt n$ grows faster than $n$... no, actually $\frac{1}{\sqrt n}>\frac1n$) must converge just because individual terms shrink to $0$ — term-by-term size relative to a known divergent series is what should be checked, not the shrink-to-zero behavior alone. |
| 11 | False. Removing finitely many terms changes the *value* the tail converges to, but there is no guarantee of direction (smaller or larger) — if some of the removed terms $a_0,\ldots,a_6$ are negative, the tail sum could easily be *larger* than the full sum. Convergence of the tail is guaranteed; the direction of the inequality is not. | Assuming "removing early terms" always shrinks the total, by implicitly picturing only series with positive terms — the claim is false in general once negative terms are allowed. |
| 12 | $\sum(a_n+b_n)$ **diverges**. Proof: suppose for contradiction it converges. Since $\sum a_n$ converges, by the Difference Rule (Theorem 5.7), $\sum[(a_n+b_n)-a_n] = \sum b_n$ would also have to converge — contradicting the given fact that $\sum b_n$ diverges. Hence $\sum(a_n+b_n)$ cannot converge. | Assuming "convergent + divergent = divergent" is simply true by pattern-matching without proof, or (worse) trying to apply the Sum Rule directly to a convergent and a divergent series (which is not a valid application of Theorem 5.7, since that rule requires BOTH series to already be convergent) — the correct proof is by contradiction, using the rule in the other direction. |
