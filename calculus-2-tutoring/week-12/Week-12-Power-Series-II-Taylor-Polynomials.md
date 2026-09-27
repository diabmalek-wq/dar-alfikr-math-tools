# Week 12 — Power Series II: Taylor Polynomials

**Session length:** 60 minutes (Pages 1–5, self-paced)
**Source:** OpenStax *Calculus Volume 2*, §6.3 (Taylor and Maclaurin Series) — Definition of the $n$th Taylor polynomial, Theorem 6.5 (Uniqueness of Power Series). MAT137 Unit 14 slides (14.4–14.6: Taylor polynomials of a polynomial from two equivalent definitions; reconstructing a polynomial from its derivative values; the "Competition" task showing Taylor coefficients are basis-independent) — MAT137 is the University of Toronto's official exclusion-equivalent of MATA37H3.

## Page 1 — Definitions and Key Facts

### Definition: The $n$th Taylor Polynomial

If $f$ has $n$ derivatives at $x=a$, the **$n$th Taylor polynomial for $f$ at $a$** is
$$p_n(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f'''(a)}{3!}(x-a)^3 + \cdots + \frac{f^{(n)}(a)}{n!}(x-a)^n = \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(x-a)^k.$$
When $a=0$, $p_n$ is called the $n$th **Maclaurin polynomial**.

### Theorem 6.5: Uniqueness of Power Series

If $f$ can be written as **any** polynomial (or power series) in $(x-a)$, its Taylor polynomial coefficients are exactly the coefficients of that expansion — you don't have to differentiate to find them. Equivalently: at most one degree-$\le n$ polynomial can match $f(a), f'(a), \ldots, f^{(n)}(a)$ simultaneously, so any correct method for finding $p_n$ (differentiating and plugging in, or recognizing $f$'s expansion directly) must produce the **same** answer.

### Key Fact: Taylor Polynomials of a Polynomial (No Differentiation Needed)

If $f$ is already a polynomial of degree $d$ and $n\ge d$, then $p_n(x) = f(x)$ **exactly** — the Taylor polynomial reproduces $f$ with zero remainder, regardless of the center $a$ (only the *packaging* into powers of $(x-a)$ changes). If $n<d$, $p_n$ keeps exactly the terms of degree $\le n$ from $f$'s expansion in powers of $(x-a)$ and drops the rest — including any terms that happen to be zero, which must still be accounted for when reasoning through the pattern.

### Key Fact: Reconstructing a Polynomial from Derivative Data

Given $f(a), f'(a), f''(a), \ldots, f^{(n)}(a)$, the coefficient formula is **forced**, not a choice: there is exactly one degree-$\le n$ polynomial with those derivative values at $a$ (Theorem 6.5, applied to the finite case), so simply plugging the given values into the coefficient formula produces the unique correct answer.

## Pages 2–3 — Solved Examples

**Example 1 (Taylor polynomials of a polynomial from the coefficient formula, matched against direct algebra).** For $f(x)=x^3$, find $p_3(x)$ and $p_2(x)$ at $a=0$, two ways.

*Solution.* **Coefficient formula:** $f(0)=0,\,f'(x)=3x^2\Rightarrow f'(0)=0,\,f''(x)=6x\Rightarrow f''(0)=0,\,f'''(x)=6\Rightarrow f'''(0)=6$. So $p_3(x) = 0+0\cdot x+\dfrac{0}{2!}x^2+\dfrac{6}{3!}x^3 = x^3$. **Direct check (Uniqueness of Power Series):** $f(x)=x^3$ is *already* a polynomial in $x$ of degree $3$, so its own Taylor polynomial of degree $\ge 3$ must just be itself — matches. For $p_2$: truncate the degree-$3$ expansion at degree $2$, i.e. drop the $x^3$ term: $p_2(x) = 0$ (the zero polynomial), since $x^3$ contributes nothing to degrees $0,1,2$. *(Misconception flag: $p_2(x)$ is $0$, not "undefined" or "$x^3$ with the $x^3$ erased differently" — the $n$th Taylor polynomial keeps exactly the terms of degree $\le n$ from the true expansion and nothing else.)* $\blacksquare$

**Example 2 (same $f$, centered at $a=1$).** For $f(x)=x^3$, find $p_3(x)$ centered at $a=1$ (write it in powers of $(x-1)$).

*Solution.* $f(1)=1,\,f'(1)=3,\,f''(1)=6,\,f'''(1)=6$. So
$$p_3(x) = 1 + 3(x-1) + \frac{6}{2!}(x-1)^2 + \frac{6}{3!}(x-1)^3 = 1+3(x-1)+3(x-1)^2+(x-1)^3.$$
*Check by substitution:* let $u=x-1$, so $x=u+1$ and $x^3=(u+1)^3 = u^3+3u^2+3u+1$ — matches term-for-term with $u=(x-1)$. Since $f$ is a cubic, $p_3=f$ **exactly** (no approximation, no remainder) regardless of the center — only the *packaging* into powers of $(x-a)$ changes. $\blacksquare$

**Example 3 (reconstructing a polynomial from derivative data — building toward the coefficient formula).** A polynomial $P$ of degree $\le 3$ satisfies $P(0)=5,\,P'(0)=-2,\,P''(0)=0,\,P'''(0)=12$. Find $P(x)$, and explain why it is the *only* such polynomial of degree $\le 3$.

*Solution.* By the coefficient formula (which is forced, not a choice, once we require $P=p_3$ for itself): $P(x) = 5 + (-2)x + \dfrac{0}{2!}x^2+\dfrac{12}{3!}x^3 = 5-2x+2x^3$. **Uniqueness:** any degree-$\le3$ polynomial is completely determined by its value and first three derivatives at a single point, because matching $Q(0)=P(0),\,Q'(0)=P'(0),\,Q''(0)=P''(0),\,Q'''(0)=P'''(0)$ for two degree-$\le 3$ polynomials forces $Q-P$ to be a degree-$\le3$ polynomial with a quadruple root at $0$ in the derivative sense — i.e. $Q-P\equiv 0$ (Theorem 6.5, Uniqueness of Power Series, applied to the finite case). $\blacksquare$

## Pages 4–5 — Practice Problems (unsolved)

**Taylor polynomials of a polynomial (no differentiation needed — use uniqueness)**

1. For $f(x) = 2x^3 - x^2+5$, write down $p_3(x)$, $p_2(x)$, and $p_1(x)$ at $a=0$ directly from the given expansion, with no derivative computations.
2. For $f(x)=x^3$, find $p_3(x)$ centered at $a=-1$ (powers of $(x+1)$), and verify it by substituting $u=x+1$ as in Example 2.
3. A polynomial $Q$ of degree $\le 4$ satisfies $Q(2)=1,\,Q'(2)=0,\,Q''(2)=-6,\,Q'''(2)=0,\,Q^{(4)}(2)=24$. Find $Q(x)$ in powers of $(x-2)$.

**Taylor polynomials of a non-polynomial function (differentiation required)**

4. Find $p_3(x)$ (the 3rd Maclaurin polynomial) for $f(x)=e^x$, using $f(0)=f'(0)=f''(0)=f'''(0)=1$.
5. Find $p_2(x)$ for $f(x)=\cos x$ centered at $a=0$, using $f(0)=1,\,f'(0)=0,\,f''(0)=-1$.

**Reasoning / "why does this work"**

6. Two students each write $f(x)=x^4$ as a Taylor expansion at $a=0$ using totally different-looking methods (one differentiates four times and plugs into the coefficient formula; the other multiplies out $f(x)=x\cdot x\cdot x\cdot x$ directly). Explain, citing Theorem 6.5, why they are guaranteed to get the same $p_4(x)$ — and give it.
7. True or false, with justification: "If $f$ is a polynomial of degree $7$, then its Taylor polynomial $p_{10}(x)$ at any center $a$ equals $f(x)$ exactly." (Careful with the direction of the inequality $10$ vs. $7$.)
8. Explain why, for a polynomial $f$ of degree $d$, the Taylor polynomial $p_n(x)$ for $n<d$ is generally **not** the same as simply setting $x^{n+1}, x^{n+2},\ldots$ to zero in $f$'s expansion **around a nonzero center** $a$ — i.e., why the truncation must happen in powers of $(x-a)$, not in powers of $x$.

## Answer Key & Misconception Notes (for tutor use — do not show student until after attempt)

| # | Answer | Common misconception |
|---|--------|----------------------|
| 1 | $p_3(x)=2x^3-x^2+5$ (equals $f$ itself, since $f$ has degree $3$). $p_2(x) = -x^2+5$ (drop the $x^3$ term). $p_1(x)=5$ (drop $x^3$ and $x^2$ terms — **not** $5+0\cdot x$ written differently, just the constant). | Trying to differentiate $f$ from scratch instead of reading the coefficients off directly — wastes time and invites arithmetic slips; uniqueness makes this a zero-computation problem. |
| 2 | With $u=x+1$ (so $x=u-1$): $x^3=(u-1)^3=u^3-3u^2+3u-1$, so $p_3(x) = -1+3(x+1)-3(x+1)^2+(x+1)^3$. Check via coefficient formula: $f(-1)=-1,\,f'(-1)=3,\,f''(-1)=-6\Rightarrow\frac{-6}{2!}=-3,\,f'''(-1)=6\Rightarrow\frac6{3!}=1$ — matches. | Sign errors expanding $(u-1)^3$ — dropping the alternating signs on the odd-power terms. |
| 3 | $Q(x) = 1+0(x-2)+\dfrac{-6}{2!}(x-2)^2+0(x-2)^3+\dfrac{24}{4!}(x-2)^4 = 1-3(x-2)^2+(x-2)^4$. | Forgetting to include the *zero* coefficients explicitly when reasoning through the pattern — students sometimes skip straight to only the nonzero terms and lose track of which power goes with which given derivative. |
| 4 | $p_3(x) = 1+x+\dfrac{1}{2!}x^2+\dfrac{1}{3!}x^3 = 1+x+\dfrac{x^2}{2}+\dfrac{x^3}{6}$. | Forgetting to divide by $k!$ at each step — writing $1+x+x^2+x^3$ (using the derivative values directly as coefficients) instead of dividing each by the correct factorial. |
| 5 | $p_2(x) = 1+0\cdot x+\dfrac{-1}{2!}x^2 = 1-\dfrac{x^2}{2}$. | Forgetting the negative sign on $f''(0)=-1$, giving $1+\frac{x^2}{2}$ instead of $1-\frac{x^2}{2}$ — a sign slip that silently produces the wrong concavity in the approximation. |
| 6 | Both methods compute the **same** degree-$\le4$ polynomial matching $f$ and its derivatives up to order $4$ at $a=0$; Theorem 6.5 (Uniqueness of Power Series) guarantees only one such polynomial exists, so any correct method must land on it: $p_4(x)=x^4$ (trivially, since $f$ already has degree $4$). | Treating "two different methods might give two different but both '''correct''' answers" as plausible — uniqueness rules this out completely; if two computations of a Taylor polynomial disagree, at least one has an arithmetic error. |
| 7 | **True.** If $\deg f = 7 \le 10$, then $f$'s own expansion already has zero coefficients for every power above $7$, so $p_{10}$ just reproduces $f$ exactly (Taylor polynomials of degree $\ge \deg f$ always equal $f$ exactly, with no remainder). It's $p_n$ for $n < \deg f$ that would truncate real information. | Reflexively assuming "higher-degree Taylor polynomial = better approximation, never exact" — for a polynomial $f$, any $p_n$ with $n\ge\deg f$ is not an approximation at all, it's $f$ itself. |
| 8 | Truncating in powers of $x$ only agrees with truncating in powers of $(x-a)$ when $a=0$ — for a nonzero center, expanding $f$ in powers of $(x-a)$ redistributes coefficients across all powers (via the binomial expansion of each $x^k=((x-a)+a)^k$), so "zeroing out high powers of $x$" and "zeroing out high powers of $(x-a)$" generally keep or discard **different** information about $f$ near $a$. | Assuming truncation is basis-independent — which power's coefficients you zero out depends entirely on which variable ($x$ or $x-a$) the expansion is written in; the Taylor polynomial construction always uses $(x-a)$, centered at the point of interest. |
