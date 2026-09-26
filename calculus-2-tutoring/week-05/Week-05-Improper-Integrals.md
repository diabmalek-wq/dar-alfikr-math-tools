# Week 5 — Improper Integrals

**Session length:** 60 minutes (Pages 1–5, self-paced)
**Source:** OpenStax *Calculus Volume 2*, §3.7 (Improper Integrals) — Definitions 3.16–3.21, Theorem 3.7 (A Comparison Theorem); adapted with the Limit Comparison Test structure from Theorem 5.12 (§5.4, stated there for series and carried over here for integrals, as MAT137 does). MAT137 Unit 12 slides (12.1–12.3: Type-1/Type-2 definitions and the $p$-integrals; Basic Comparison Test with four True/False variants; Limit Comparison Test).

## Page 1 — Definitions and Key Facts

### Definition: Type-1 Improper Integral (Infinite Interval)

Let $f$ be continuous on $[a, +\infty)$. Then
$$\int_{a}^{+\infty} f(x)\,dx = \lim_{t \to +\infty} \int_{a}^{t} f(x)\,dx,$$
provided the limit exists. Similarly, if $f$ is continuous on $(-\infty, b]$,
$$\int_{-\infty}^{b} f(x)\,dx = \lim_{t \to -\infty} \int_{t}^{b} f(x)\,dx.$$
If $f$ is continuous on $(-\infty, +\infty)$, then for any real number $a$,
$$\int_{-\infty}^{+\infty} f(x)\,dx = \int_{-\infty}^{a} f(x)\,dx + \int_{a}^{+\infty} f(x)\,dx,$$
provided **both** pieces converge. If either piece diverges, the whole integral diverges — you may not swap in a different splitting point to "rescue" a divergent integral.

In every case: if the limit exists (and is finite), the improper integral **converges**; if the limit does not exist or is infinite, it **diverges**.

### Definition: Type-2 Improper Integral (Discontinuous Integrand)

Let $f$ be continuous on $[a, b)$ with a discontinuity at $b$ (e.g.\ a vertical asymptote). Then
$$\int_{a}^{b} f(x)\,dx = \lim_{t \to b^{-}} \int_{a}^{t} f(x)\,dx.$$
Similarly, if $f$ is continuous on $(a, b]$ with a discontinuity at $a$,
$$\int_{a}^{b} f(x)\,dx = \lim_{t \to a^{+}} \int_{t}^{b} f(x)\,dx.$$
If $f$ is continuous on $[a, b]$ except at some interior point $c$, then
$$\int_{a}^{b} f(x)\,dx = \int_{a}^{c} f(x)\,dx + \int_{c}^{b} f(x)\,dx,$$
provided **both** pieces converge; if either diverges, the whole integral diverges.

### Key Fact: The $p$-Integrals

These are the benchmark integrals every comparison is built from — memorize the convergence conditions, not just the computation.

$$\int_{1}^{+\infty} \frac{1}{x^{p}}\,dx \text{ converges} \iff p > 1, \qquad
\int_{0}^{1} \frac{1}{x^{p}}\,dx \text{ converges} \iff p < 1.$$

Consequently $\displaystyle\int_{0}^{+\infty} \frac{1}{x^{p}}\,dx$ **diverges for every** $p$, since it splits as $\int_0^1 \frac{1}{x^p}\,dx + \int_1^{+\infty} \frac{1}{x^p}\,dx$, and no single value of $p$ makes both pieces converge at once (one needs $p<1$, the other needs $p>1$).

### Theorem: A Comparison Theorem (Basic Comparison Test, BCT)

Let $f(x)$ and $g(x)$ be continuous on $[a, +\infty)$ with $0 \le f(x) \le g(x)$ for all $x \ge a$.

**(i)** If $\displaystyle\int_{a}^{+\infty} f(x)\,dx = +\infty$, then $\displaystyle\int_{a}^{+\infty} g(x)\,dx = +\infty$.

**(ii)** If $\displaystyle\int_{a}^{+\infty} g(x)\,dx = L$ for a real number $L$, then $\displaystyle\int_{a}^{+\infty} f(x)\,dx$ converges to some real number $M \le L$.

In words: **"small diverges $\Rightarrow$ big diverges"** and **"big converges $\Rightarrow$ small converges."** The two other implications (big diverges $\Rightarrow$ small diverges; small converges $\Rightarrow$ big converges) are **false** in general — a smaller positive function can still diverge, and a larger one can still converge to a finite value. The hypothesis only needs to hold eventually: if $\exists\, M \ge a$ such that $0 \le f(x) \le g(x)$ for all $x \ge M$, the same conclusions hold, since $\int_a^M f$ and $\int_a^M g$ are ordinary (finite) integrals that never affect convergence at infinity.

### Key Fact: Limit Comparison Test (LCT) for Improper Integrals

Let $f(x), g(x) \ge 0$ be continuous on $[a, +\infty)$, and suppose $\displaystyle\lim_{x \to +\infty} \frac{f(x)}{g(x)} = L$.

* If $L$ is a **finite, nonzero** real number, then $\displaystyle\int_a^{+\infty} f(x)\,dx$ and $\displaystyle\int_a^{+\infty} g(x)\,dx$ **either both converge or both diverge**.
* If $L = 0$ and $\displaystyle\int_a^{+\infty} g(x)\,dx$ converges, then $\displaystyle\int_a^{+\infty} f(x)\,dx$ converges.
* If $L = +\infty$ and $\displaystyle\int_a^{+\infty} g(x)\,dx$ diverges, then $\displaystyle\int_a^{+\infty} f(x)\,dx$ diverges.

(This is the direct integral analogue of the Limit Comparison Test for series, Theorem 5.12 — same three cases, same logic, just with $\int_a^{+\infty}$ in place of $\sum_{n=1}^{\infty}$.) LCT is the tool of choice when BCT's inequality $f(x) \le g(x)$ is awkward or false pointwise, but $f$ and $g$ still behave the same way as $x \to \infty$ — e.g. comparing $\dfrac{1+\cos^2 x}{x^{2/3}}$ to $\dfrac{1}{x^{2/3}}$ is easy with BCT (since $1 \le 1+\cos^2 x \le 2$ pointwise); comparing $\dfrac{x+2}{\sqrt{x^4+x+1}}$ to $\dfrac{1}{x}$ is much cleaner with LCT.

## Pages 2–3 — Solved Examples

**Example 1 (basic Type-1, computed from the definition).** Evaluate $\displaystyle\int_1^{+\infty} \frac{1}{x^2+x}\,dx$.

*Solution.* Partial fractions: $\dfrac{1}{x^2+x} = \dfrac{1}{x} - \dfrac{1}{x+1}$ (check: $\frac{(x+1)-x}{x(x+1)} = \frac{1}{x(x+1)}$ ✓). Then
$$\int_1^{t} \left(\frac{1}{x}-\frac{1}{x+1}\right)dx = \Big[\ln|x| - \ln|x+1|\Big]_1^{t} = \ln\frac{t}{t+1} - \ln\frac{1}{2}.$$
As $t \to +\infty$, $\dfrac{t}{t+1} \to 1$, so $\ln\dfrac{t}{t+1} \to \ln 1 = 0$. Hence the limit is $0 - \ln\frac12 = \ln 2$. The integral **converges to $\ln 2$**.

**Example 2 ($p$-integral, derived from the definition — do not just quote the rule).** Show $\displaystyle\int_1^{+\infty}\frac{1}{x^p}\,dx$ converges iff $p>1$.

*Solution.* Case $p \ne 1$: $\displaystyle\int_1^{t} x^{-p}\,dx = \left[\frac{x^{1-p}}{1-p}\right]_1^{t} = \frac{t^{1-p}-1}{1-p}$. If $p>1$, then $1-p<0$, so $t^{1-p} = \dfrac{1}{t^{p-1}} \to 0$ as $t\to+\infty$, giving limit $\dfrac{0-1}{1-p} = \dfrac{1}{p-1}$ — **converges**. If $p<1$, then $1-p>0$, so $t^{1-p}\to+\infty$ — **diverges**. Case $p=1$: $\displaystyle\int_1^t \frac1x\,dx = \ln t \to +\infty$ — **diverges**. Combining: converges exactly when $p>1$.

**Example 3 (Type-1 on $(-\infty,+\infty)$, splitting required).** Determine whether $\displaystyle\int_{-\infty}^{+\infty} xe^{-x^2}\,dx$ converges.

*Solution.* Split at $0$: $\displaystyle\int_{-\infty}^{0} xe^{-x^2}\,dx + \int_{0}^{+\infty} xe^{-x^2}\,dx$. For the second piece, with $u=-x^2,\,du=-2x\,dx$: $\displaystyle\int_0^t xe^{-x^2}\,dx = \left[-\tfrac12 e^{-x^2}\right]_0^t = -\tfrac12 e^{-t^2}+\tfrac12 \to \tfrac12$ as $t\to+\infty$ — converges to $\tfrac12$. By the symmetry $x e^{-x^2}$ is odd, so $\displaystyle\int_{-\infty}^0 xe^{-x^2}\,dx = \lim_{t\to-\infty}\left[-\tfrac12 e^{-x^2}\right]_t^0 = -\tfrac12 - \left(-\lim_{t\to-\infty}\tfrac12 e^{-t^2}\right) = -\tfrac12$. Both pieces converge, so the full integral converges to $-\tfrac12 + \tfrac12 = 0$.
*Misconception flag:* you may **not** shortcut this by declaring "odd function on a symmetric interval $\Rightarrow$ integral is $0$" — that trick is only valid for **finite** intervals with no discontinuity. Here it happens to give the right numerical answer, but only because we first verified **both halves individually converge**. If even one half diverged, the whole improper integral would diverge, regardless of "symmetry."

**Example 4 (Type-2, discontinuity at an endpoint).** Evaluate $\displaystyle\int_0^4 \frac{1}{\sqrt{4-x}}\,dx$.

*Solution.* $f(x)=\frac{1}{\sqrt{4-x}}$ is continuous on $[0,4)$ with a vertical asymptote at $x=4$. So
$$\int_0^t \frac{1}{\sqrt{4-x}}\,dx = \Big[-2\sqrt{4-x}\Big]_0^t = -2\sqrt{4-t}+4.$$
As $t\to 4^-$, $\sqrt{4-t}\to 0$, so the limit is $4$. **Converges to $4$.**

**Example 5 (Type-2, discontinuity at an interior point — a classic trap).** Evaluate $\displaystyle\int_{-1}^{1} \frac{1}{x^3}\,dx$.

*Solution.* $f(x)=1/x^3$ is discontinuous at $x=0 \in (-1,1)$, so this **must** be split there: $\displaystyle\int_{-1}^1 \frac{1}{x^3}\,dx = \int_{-1}^0 \frac{1}{x^3}\,dx + \int_0^1 \frac{1}{x^3}\,dx$. Check the first piece: $\displaystyle\int_{-1}^{t}\frac{1}{x^3}\,dx = \left[-\frac{1}{2x^2}\right]_{-1}^{t} = -\frac{1}{2t^2}+\frac12 \to -\infty$ as $t\to 0^-$. This piece **diverges**, so the whole integral diverges — you never even need to check the second piece.
*Misconception flag:* it is **wrong** to write $\int_{-1}^1 x^{-3}\,dx = \left[-\frac{1}{2x^2}\right]_{-1}^1 = -\frac12+\frac12 = 0$ by treating this as an ordinary (proper) integral with the Fundamental Theorem of Calculus. FTC requires the antiderivative to be continuous on the **whole** interval of integration; $-\frac{1}{2x^2}$ blows up at $x=0$, which is inside $[-1,1]$, so this application of FTC is invalid and produces a wrong, finite-looking answer for a divergent integral.

**Example 6 (BCT, "small diverges $\Rightarrow$ big diverges").** Determine convergence of $\displaystyle\int_{1}^{+\infty} \frac{1+\cos^2 x}{x^{2/3}}\,dx$.

*Solution.* For all $x\ge 1$: $\dfrac{1+\cos^2 x}{x^{2/3}} \ge \dfrac{1}{x^{2/3}} \ge 0$ (since $1+\cos^2 x \ge 1$). By the $p$-integral with $p=\frac23 < 1$, $\displaystyle\int_1^{+\infty}\frac{1}{x^{2/3}}\,dx$ diverges. Since our function is $\ge$ a divergent nonnegative function, by BCT part (i), $\displaystyle\int_1^{+\infty}\frac{1+\cos^2 x}{x^{2/3}}\,dx$ **diverges**.

**Example 7 (BCT, "big converges $\Rightarrow$ small converges").** Determine convergence of $\displaystyle\int_{2}^{+\infty} \frac{(\ln x)^{10}}{x^2}\,dx$.

*Solution.* This needs a two-step comparison, since $(\ln x)^{10}$ grows (slower than any power of $x$, but the direct comparison to $1/x^2$ isn't obviously true pointwise). Use the growth-rate fact $\ln x \ll x^{1/20}$ (from Unit 11's Big Theorem): for $x$ large enough, $(\ln x)^{10} \le x^{1/2}$, so $\dfrac{(\ln x)^{10}}{x^2} \le \dfrac{x^{1/2}}{x^2} = \dfrac{1}{x^{3/2}}$ eventually. Since $\displaystyle\int_2^{+\infty}\frac{1}{x^{3/2}}\,dx$ converges ($p=\frac32>1$), and our function is eventually $\le$ this convergent nonnegative function, BCT part (ii) gives that $\displaystyle\int_2^{+\infty}\frac{(\ln x)^{10}}{x^2}\,dx$ **converges**. (In practice, most instructors accept declaring this "clear from growth rates" without the explicit intermediate bound — but you must be able to produce it if asked.)

**Example 8 (LCT, when BCT's inequality is inconvenient).** Determine convergence of $\displaystyle\int_{1}^{+\infty} \frac{x+2}{\sqrt{x^4+x+1}}\,dx$.

*Solution.* For large $x$, $\dfrac{x+2}{\sqrt{x^4+x+1}} \approx \dfrac{x}{\sqrt{x^4}} = \dfrac{1}{x}$, so compare to $g(x)=\dfrac1x$:
$$L = \lim_{x\to+\infty} \frac{\left(\dfrac{x+2}{\sqrt{x^4+x+1}}\right)}{\left(\dfrac1x\right)} = \lim_{x\to+\infty} \frac{x(x+2)}{\sqrt{x^4+x+1}} = \lim_{x\to+\infty} \frac{x^2+2x}{x^2\sqrt{1+\frac{1}{x^3}+\frac{1}{x^4}}} = 1.$$
$L=1$ is finite and nonzero, so by LCT, $\displaystyle\int_1^{+\infty}\frac{x+2}{\sqrt{x^4+x+1}}\,dx$ and $\displaystyle\int_1^{+\infty}\frac1x\,dx$ behave the same way. The latter diverges ($p=1$), so the original integral **diverges**.

## Pages 4–5 — Practice Problems (unsolved)

**Computing from the definition**

1. Evaluate $\displaystyle\int_2^{+\infty} \frac{1}{(x-1)^2}\,dx$, or show it diverges.
2. Evaluate $\displaystyle\int_0^{+\infty} xe^{-2x}\,dx$, or show it diverges.
3. Evaluate $\displaystyle\int_{-\infty}^{0} \frac{1}{x^2+4}\,dx$, or show it diverges.

**Type-2 and split integrals**

4. Evaluate $\displaystyle\int_0^{1} \frac{1}{\sqrt{x}}\,dx$, or show it diverges.
5. Determine whether $\displaystyle\int_{-8}^{8} \frac{1}{x^{2/3}}\,dx$ converges or diverges. (Careful — identify **every** discontinuity in $[-8,8]$ before you decide how to split it.)
6. **Spot the error.** A student evaluates $\displaystyle\int_0^{2} \frac{1}{(x-1)^2}\,dx$ as follows: "$\displaystyle\int_0^2 (x-1)^{-2}\,dx = \left[-\dfrac{1}{x-1}\right]_0^2 = -1-1=-2$." Explain precisely what is wrong with this computation, and determine the correct answer (convergent value, or divergent).

**Rapid $p$-integral & comparison judgment (state convergent/divergent with one line of justification — no full computation required)**

7. $\displaystyle\int_1^{+\infty} \frac{1}{x^{5}}\,dx$
8. $\displaystyle\int_0^{1} \frac{1}{x^{5}}\,dx$
9. $\displaystyle\int_1^{+\infty} \frac{2+\sin x}{x^{3/4}}\,dx$ (use BCT)

**BCT / LCT applications**

10. Use BCT to determine whether $\displaystyle\int_1^{+\infty} \frac{\arctan(x^2)}{1+x^3}\,dx$ converges or diverges.
11. Use LCT to determine whether $\displaystyle\int_1^{+\infty} \frac{x^3+2x+7}{x^5+11x^4+1}\,dx$ converges or diverges.
12. Use LCT to determine whether $\displaystyle\int_0^{1} \frac{\sin x}{x^{3/2}}\,dx$ converges or diverges. (Recall $\displaystyle\lim_{x\to 0}\dfrac{\sin x}{x}=1$, and note the discontinuity here is at $x=0$, not $x=+\infty$ — LCT works the same way as $x\to 0^+$.)

## Answer Key & Misconception Notes (for tutor use — do not show student until after attempt)

| # | Answer | Common misconception |
|---|--------|----------------------|
| 1 | Converges to $1$. $\int_2^t (x-1)^{-2}dx = \left[-\frac{1}{x-1}\right]_2^t = -\frac1{t-1}+1 \to 1$. | Forgetting the substitution shift ($u=x-1$) and integrating as if the singularity/power rule applied directly to $x^2$ instead of $(x-1)^2$, giving a wrong antiderivative. |
| 2 | Converges to $\frac14$. Integration by parts ($u=x,\,dv=e^{-2x}dx$) gives $\int_0^t xe^{-2x}dx = \left[-\frac{x}{2}e^{-2x}-\frac14 e^{-2x}\right]_0^t \to \frac14$ (using $\lim_{t\to\infty} t e^{-2t}=0$). | Dropping the limit $\lim_{t\to\infty} te^{-2t}=0$ as "obviously infinity times zero is undefined" instead of resolving it (L'Hôpital or exponential-dominates-polynomial). |
| 3 | Converges to $\frac{\pi}{4}$. $\int_t^0 \frac{1}{x^2+4}dx = \left[\frac12\arctan\frac{x}{2}\right]_t^0 = 0-\frac12\arctan\frac{t}{2} \to \frac12\cdot\frac{\pi}{4}\cdot(-1)\cdot(-1)$; carefully: as $t\to-\infty$, $\arctan(t/2)\to-\pi/2$, so the limit is $0-\frac12(-\frac{\pi}{2})=\frac{\pi}{4}$. | Sign error on the arctan limit as $t\to-\infty$ (using $+\pi/2$ instead of $-\pi/2$), or forgetting the $\frac12$ factor from the chain rule on $\arctan(x/2)$. |
| 4 | Converges to $2$ ($p=\frac12<1$ on $(0,1]$; direct computation: $\int_t^1 x^{-1/2}dx=[2\sqrt x]_t^1=2-2\sqrt t\to 2$). | Treating this as a Type-1 integral or not noticing the discontinuity is at $x=0$ (the lower limit), so setting up the limit at the wrong endpoint. |
| 5 | There are **two** trouble points: $x=0$ is an interior discontinuity (vertical asymptote of $x^{-2/3}$), so the integral must split as $\int_{-8}^0+\int_0^8$. Each piece is itself a $p$-integral with $p=\frac23<1$ on a finite interval touching the singularity, so by the $p<1$ rule each piece **converges** individually. Computing: $\int_0^8 x^{-2/3}\,dx = \left[3x^{1/3}\right]_0^8 = 6$, and by symmetry $\int_{-8}^0 x^{-2/3}\,dx = 6$ as well, so the series **converges** to $12$. | The core misconception being tested is students **not noticing the interior discontinuity at all** and integrating straight through as if $x^{-2/3}$ were continuous on $[-8,8]$ (it is NOT defined/continuous at $x=0$), OR, once noticed, assuming any singularity automatically means divergence without checking the actual power of $p$ against $1$. |
| 6 | The computation is invalid: $(x-1)^{-2}$ has a discontinuity at $x=1$, which lies **inside** $[0,2]$, so FTC cannot be applied directly across the interval. Correctly split at $x=1$: both $\int_0^1(x-1)^{-2}dx$ and $\int_1^2(x-1)^{-2}dx$ diverge to $+\infty$ (each is a $p=2$ power blowing up at the shared endpoint), so the true answer is **diverges**. | Exactly the Example 5 trap: applying FTC through a point where the antiderivative (and the integrand) is undefined, producing a finite but meaningless numeric answer instead of recognizing divergence. |
| 7 | Converges ($p=5>1$). | None of the "$p$" rule variants confused (see #8) — but watch for automatically writing "converges" without checking that the interval is $[1,\infty)$ and not $[0,1]$, where the rule flips. |
| 8 | Diverges ($p=5>1$, but this is the $[0,1]$ case, which needs $p<1$ to converge). | The single most common error in this whole unit: applying the $[1,\infty)$ rule ("$p>1$ converges") to a $[0,1]$-type integral without checking which endpoint has the singularity. The two rules are opposite. |
| 9 | Converges. Since $1 \le 2+\sin x \le 3$, we get $\frac{2+\sin x}{x^{3/4}} \le \frac{3}{x^{3/4}}$ for $x\ge1$... but $p=\frac34<1$ makes $\int \frac{3}{x^{3/4}}dx$ **diverge**, which gives no information via the "small" side. Instead use the **lower** bound: $\frac{2+\sin x}{x^{3/4}} \ge \frac{1}{x^{3/4}}$, which also diverges ($p<1$) — and since our function is $\ge$ a divergent function, by BCT it **diverges**, not converges. | Grabbing whichever bound is algebraically easiest ($\le$ vs $\ge$) without checking that it actually points the comparison in a conclusion-yielding direction; a $\le$-bound to a *divergent* comparison function proves nothing (case not covered by BCT), so students must switch to the $\ge$-bound here. |
| 10 | Converges. $0 \le \frac{\arctan(x^2)}{1+x^3} \le \frac{\pi/2}{x^3}$ for $x\ge1$ (since $\arctan$ is bounded above by $\pi/2$, and $1+x^3 \ge x^3$). $\int_1^{\infty}\frac{\pi/2}{x^3}dx$ converges ($p=3>1$), so by BCT the original integral converges. | Trying to bound $\arctan(x^2)$ by something growing (like $x^2$ itself) instead of noticing arctan is **always** bounded by $\pi/2$ — missing the single easiest and most useful bound in the whole toolkit. |
| 11 | Diverges. Compare to $g(x)=\frac{1}{x^2}$ (matching leading degree $3-5=-2$): $L=\lim \frac{x^3+2x+7}{x^5+11x^4+1}\cdot x^2 = \lim\frac{x^5+2x^3+7x^2}{x^5+11x^4+1}=1$, finite and nonzero. **Correction**: $\int_1^\infty \frac1{x^2}dx$ actually **converges** ($p=2>1$), so LCT says the original integral **converges**, not diverges. | Miscounting the degree gap (using $x^{5-3}=x^2$ in the denominator instead of correctly forming the ratio $\frac{\deg\text{ num}}{\deg\text{ denom}} = 3-5=-2$, i.e., comparing to $x^{-2}$), or after correctly finding $p=2$, misremembering the $p>1$ convergence rule as divergence. |
| 12 | Converges. Compare to $g(x)=\frac{1}{x^{1/2}}$ near $x=0$: $L=\lim_{x\to0^+}\frac{\sin x/x^{3/2}}{1/x^{1/2}} = \lim_{x\to0^+}\frac{\sin x}{x} = 1$, finite and nonzero. $\int_0^1 x^{-1/2}dx$ converges ($p=\frac12<1$ on $[0,1]$), so by LCT the original converges. | Applying the LCT limit as $x\to\infty$ out of habit instead of $x\to0^+$ (the actual location of the singularity in this problem), which produces a meaningless or wrong limit value. |
