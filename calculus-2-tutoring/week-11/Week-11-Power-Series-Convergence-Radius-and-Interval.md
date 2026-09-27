# Week 11 — Power Series I: Radius/Interval of Convergence & Function Representations

**Session length:** 60 minutes (Pages 1–5, self-paced)
**Source:** OpenStax *Calculus Volume 2*, §6.1 (Power Series and Functions) — Theorem 6.1 (Convergence of a Power Series), radius/interval of convergence; §6.2 (Properties of Power Series) — Theorem 6.2 (Combining Power Series), Theorem 6.4 (Term-by-Term Differentiation and Integration). MAT137 Unit 14 slides (14.1–14.3: interval of convergence including a "hard" factorial-ratio series; writing functions as power series via geometric-series manipulation) — MAT137 is the University of Toronto's official exclusion-equivalent of MATA37H3.

## Page 1 — Definitions and Key Facts

### Definition: Power Series, Radius & Interval of Convergence

A **power series centered at $a$** is a series of the form
$$\sum_{n=0}^{\infty} c_n (x-a)^n = c_0 + c_1(x-a) + c_2(x-a)^2 + \cdots.$$
By Theorem 6.1, exactly one of the following holds: (i) the series converges only at $x=a$ (**radius of convergence $R=0$**); (ii) the series converges for **all** real $x$ ($R=\infty$); or (iii) there is a real number $R>0$ such that the series converges for $|x-a|<R$ and diverges for $|x-a|>R$ — the **interval of convergence** is then $(a-R,\,a+R)$, possibly with one or both endpoints included, and each endpoint $x=a\pm R$ **must be checked separately** (the Ratio Test is inconclusive there).

### Key Fact: Finding the Interval of Convergence (Ratio Test Method)

Apply the Ratio Test to $a_n = c_n(x-a)^n$: compute $L(x) = \displaystyle\lim_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|$. Solve $L(x)<1$ for $x$ — this gives the open interval and $R$. Then plug each endpoint back into the **original series** (not the ratio) and test it on its own merits (Divergence Test, $p$-series, Alternating Series Test, etc. — see Weeks 9–10).

### Theorem 6.4: Term-by-Term Differentiation and Integration for Power Series

If $f(x) = \displaystyle\sum_{n=0}^{\infty} c_n(x-a)^n$ has radius of convergence $R>0$, then for $|x-a|<R$,
$$f'(x) = \sum_{n=1}^{\infty} n\,c_n(x-a)^{n-1}, \qquad \int f(x)\,dx = C + \sum_{n=0}^{\infty} \frac{c_n}{n+1}(x-a)^{n+1},$$
and **both** the differentiated and integrated series have the **same radius of convergence $R$** as the original (endpoint behavior can change, even though $R$ does not).

### Key Fact: Building New Power Series from $\dfrac{1}{1-x} = \displaystyle\sum_{n=0}^{\infty} x^n$, $|x|<1$

The geometric series is the master template. To represent a new function as a power series, manipulate it algebraically (substitute for $x$, factor out constants, split into partial fractions) until it looks like $\dfrac{1}{1-(\text{something})}$, then substitute term-by-term. Combined with Theorem 6.4, this also lets you build series for functions whose derivative or antiderivative is a disguised geometric series (e.g. $\ln(1+x)$, whose derivative $\frac{1}{1+x}$ is geometric).

## Pages 2–3 — Solved Examples

**Example 1 (interval of convergence, standard case).** Find the radius and interval of convergence of $\displaystyle\sum_{n=1}^{\infty} \frac{(x-3)^n}{n\cdot 4^n}$.

*Solution.* $\left|\dfrac{a_{n+1}}{a_n}\right| = \dfrac{|x-3|^{n+1}}{(n+1)4^{n+1}}\cdot\dfrac{n\cdot 4^n}{|x-3|^n} = \dfrac{n}{n+1}\cdot\dfrac{|x-3|}{4} \to \dfrac{|x-3|}{4}$. Need $\dfrac{|x-3|}{4}<1 \iff |x-3|<4$, so $R=4$, open interval $(-1,7)$. **Endpoint $x=7$:** series becomes $\sum \frac{4^n}{n\cdot4^n} = \sum\frac1n$ — diverges ($p$-series, $p=1$). **Endpoint $x=-1$:** series becomes $\sum \frac{(-4)^n}{n\cdot4^n} = \sum\frac{(-1)^n}{n}$ — converges (Alternating Series Test: terms $\to 0$, decreasing). Interval of convergence: $[-1,7)$. $\blacksquare$

**Example 2 (the "hard" factorial-ratio case).** Find the radius of convergence of $\displaystyle\sum_{n=1}^{\infty}\frac{(3n)!}{n!\,(2n)!}x^n$.

*Solution.* $\left|\dfrac{a_{n+1}}{a_n}\right| = \dfrac{(3n+3)!}{(n+1)!(2n+2)!}\cdot\dfrac{n!(2n)!}{(3n)!}|x| = \dfrac{(3n+1)(3n+2)(3n+3)}{(n+1)(2n+1)(2n+2)}|x|$. Both numerator and denominator are cubic in $n$ with leading coefficients $27$ and $4$, so the ratio $\to \dfrac{27}{4}|x|$. Need $\dfrac{27}{4}|x|<1 \iff |x|<\dfrac{4}{27}$. **Radius of convergence $R=\dfrac{4}{27}$.** *(Misconception flag: don't stop at "it's a ratio of factorials so $R=0$" — factorial growth can cancel almost completely when it appears on both top and bottom; always simplify the ratio algebraically before taking the limit.)* $\blacksquare$

**Example 3 (representing a function as a power series, factor first).** Represent $f(x) = \dfrac{1}{2-x}$ as a power series centered at $0$, and find its interval of convergence.

*Solution.* Factor a $2$ out of the denominator: $\dfrac{1}{2-x} = \dfrac{1}{2}\cdot\dfrac{1}{1-\frac{x}{2}} = \dfrac12\sum_{n=0}^{\infty}\left(\dfrac{x}{2}\right)^n = \sum_{n=0}^{\infty}\dfrac{x^n}{2^{n+1}}$, valid when $\left|\dfrac x2\right|<1$, i.e. interval of convergence $(-2,2)$. $\blacksquare$

**Example 4 (representing $\frac{1}{1-x^2}$, substitution).** Represent $f(x)=\dfrac{1}{1-x^2}$ as a power series and find its interval of convergence.

*Solution.* Substitute $x^2$ for $x$ in $\frac{1}{1-x}=\sum x^n$: $\dfrac{1}{1-x^2} = \displaystyle\sum_{n=0}^{\infty}(x^2)^n = \sum_{n=0}^{\infty}x^{2n}$, valid for $|x^2|<1 \iff |x|<1$. Interval of convergence: $(-1,1)$. $\blacksquare$

**Example 5 ($\ln(1+x)$, integrate a known series — the "compute the derivative first" hint).** Represent $f(x)=\ln(1+x)$ as a power series centered at $0$.

*Solution.* $f'(x) = \dfrac{1}{1+x} = \dfrac{1}{1-(-x)} = \displaystyle\sum_{n=0}^{\infty}(-x)^n = \sum_{n=0}^{\infty}(-1)^n x^n$ for $|x|<1$. Integrating term-by-term (Theorem 6.4):
$$f(x) = \int f'(x)\,dx = C + \sum_{n=0}^{\infty} (-1)^n \frac{x^{n+1}}{n+1}.$$
Set $x=0$: $f(0)=\ln 1 = 0 = C$, so $C=0$. Reindex with $m=n+1$: $f(x) = \displaystyle\sum_{m=1}^{\infty}(-1)^{m-1}\dfrac{x^m}{m}$, valid (at least) for $|x|<1$ — the radius doesn't change under integration, though the endpoint $x=1$ needs a separate check (it turns out to converge there too, by AST, giving $\ln 2 = 1-\frac12+\frac13-\cdots$, a classical fact you may quote but not prove here). $\blacksquare$

## Pages 4–5 — Practice Problems (unsolved)

**Interval and radius of convergence**

1. Find the radius and interval of convergence of $\displaystyle\sum_{n=1}^{\infty} \frac{(-1)^n (x+2)^n}{n^2}$.
2. Find the radius and interval of convergence of $\displaystyle\sum_{n=0}^{\infty} \frac{x^n}{n!}$. (No endpoint work needed — explain why, in one sentence, from the value of $R$.)
3. Find the radius of convergence of $\displaystyle\sum_{n=1}^{\infty} \frac{n!\,x^n}{n^n}$.

**Representing functions as power series**

4. Represent $f(x) = \dfrac{1}{1+3x}$ as a power series centered at $0$ and give its interval of convergence.
5. Represent $f(x) = \dfrac{x}{4+x^2}$ as a power series centered at $0$ and give its interval of convergence. (Hint: factor a $4$ out first, as in Example 3, then multiply by $x$.)
6. Use the geometric series and Theorem 6.4 to represent $f(x) = \dfrac{1}{(1-x)^2}$ as a power series. (Hint: $\dfrac{1}{(1-x)^2}$ is the derivative of $\dfrac{1}{1-x}$.)

## Answer Key & Misconception Notes (for tutor use — do not show student until after attempt)

| # | Answer | Common misconception |
|---|--------|----------------------|
| 1 | $\left|\dfrac{a_{n+1}}{a_n}\right| = \dfrac{n^2}{(n+1)^2}|x+2| \to |x+2|$; need $|x+2|<1$, so $R=1$, open interval $(-3,-1)$. At $x=-1$: $\sum\frac{(-1)^n}{n^2}$ converges absolutely. At $x=-3$: $\sum\frac{(-1)^n(-1)^n}{n^2}=\sum\frac1{n^2}$ converges. **Interval: $[-3,-1]$.** | Forgetting that **both** endpoints can converge — students often assume alternating series behavior at one endpoint means the other must diverge; here $p=2$ makes both converge absolutely regardless of sign. |
| 2 | Ratio $\to \dfrac{|x|}{n+1}\to 0<1$ for every $x$, so $R=\infty$, interval $(-\infty,\infty)$. No endpoints to check because there are none when $R=\infty$. | Some students still "check $x=\pm\infty$" — endpoints only exist (and only need checking) when $R$ is a finite positive number. |
| 3 | $\left|\dfrac{a_{n+1}}{a_n}\right| = \dfrac{(n+1)!}{(n+1)^{n+1}}\cdot\dfrac{n^n}{n!}|x| = \dfrac{n^n}{(n+1)^n}|x| = \left(\dfrac{n}{n+1}\right)^n|x| \to \dfrac1e|x|$ (standard limit). Need $\frac1e|x|<1\iff|x|<e$. **$R=e$.** | Treating $\left(\frac{n}{n+1}\right)^n$ as $\to 1$ instead of $\to 1/e$ — this is the same limit that defines $e$ in disguise ($\left(1+\frac1n\right)^{-n}\to e^{-1}$) and is easy to rush past. |
| 4 | $\dfrac{1}{1+3x} = \dfrac{1}{1-(-3x)} = \displaystyle\sum_{n=0}^\infty(-3x)^n = \sum_{n=0}^\infty(-3)^n x^n$, valid for $|3x|<1$, i.e. $\left(-\dfrac13,\dfrac13\right)$. | Substituting $-3x$ but forgetting to raise the $-3$ to the $n$th power along with $x$ — writing $(-3)x^n$ instead of $(-3)^nx^n$. |
| 5 | $\dfrac{x}{4+x^2} = x\cdot\dfrac14\cdot\dfrac{1}{1-\left(-\frac{x^2}{4}\right)} = \dfrac{x}4\sum_{n=0}^\infty\left(-\dfrac{x^2}{4}\right)^n = \displaystyle\sum_{n=0}^\infty \dfrac{(-1)^n x^{2n+1}}{4^{n+1}}$, valid for $\left|\dfrac{x^2}{4}\right|<1\iff |x|<2$. Interval: $(-2,2)$. | Forgetting to multiply the whole series by the leftover factor of $x$ at the end, or dropping the $\frac14$ pulled out front. |
| 6 | $\dfrac{d}{dx}\left[\dfrac{1}{1-x}\right] = \dfrac{1}{(1-x)^2}$, and $\dfrac{d}{dx}\left[\sum_{n=0}^\infty x^n\right] = \sum_{n=1}^\infty nx^{n-1}$, so $\dfrac{1}{(1-x)^2} = \displaystyle\sum_{n=1}^\infty n x^{n-1} = \sum_{n=0}^\infty (n+1)x^n$, valid for $|x|<1$ (same $R$ by Theorem 6.4). | Differentiating the *closed form* correctly but forgetting to reindex the series (leaving it as $\sum n x^{n-1}$ starting from $n=1$ is fine, but writing $\sum n x^{n-1}$ starting from $n=0$ silently includes a nonsense term). |
