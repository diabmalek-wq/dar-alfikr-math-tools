# Week 9 — Taylor Series, Analytic Functions & Applications

**Session length:** 60 minutes (Pages 1–5, self-paced)
**Source:** OpenStax *Calculus Volume 2*, §6.3 (Taylor and Maclaurin Series) — Theorem 6.6 (Uniqueness of Taylor Series), Theorem 6.7 (Taylor's Theorem with Remainder), Theorem 6.8 (Convergence of Taylor Series), Table 6.1 (Maclaurin Series for Common Functions); §6.4 (Working with Taylor Series) — constructing new series by substitution/differentiation/integration, evaluating limits and nonelementary quantities with series. MAT137 Unit 14 slides (14.7–14.14: Lagrange's Remainder Theorem and proving $\sin x$ is analytic; the general analyticity criterion; deriving $\arctan x$ and $\arcsin x$ as power series and extracting a single high-order derivative value from them; "Taylor series gymnastics" — building new series from known ones; limits via series substitution; error-bounded numerical estimation; the closing $\cot x$/Basel-problem enrichment).

## Page 1 — Definitions and Key Facts

### Definition: Taylor Series, Maclaurin Series, Analytic Function

If $f$ has derivatives of every order at $x=a$, the **Taylor series for $f$ at $a$** is
$$\sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^n.$$
At $a=0$ this is the **Maclaurin series**. A function $f$ is **analytic at $a$** if there is an open interval containing $a$ on which $f$ equals its own Taylor series at $a$ — i.e.\ the Taylor series doesn't just converge, it converges *to $f$ itself*. (A Taylor series can converge everywhere and still fail to equal $f$ off a single point — this definition is exactly the guard against that.)

### Theorem 6.7: Taylor's Theorem with Remainder

Let $f$ be $(n+1)$-times differentiable on an interval $I$ containing $a$. For $x\in I$, define the remainder $R_n(x) = f(x)-p_n(x)$. Then there exists $c$ strictly between $a$ and $x$ such that
$$R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}.$$
**Corollary (Lagrange bound).** If there is a single constant $M$ with $\left|f^{(n+1)}(t)\right|\le M$ for *every* $t$ in $I$ (not just at $c$ — that's the whole point, since $c$ is unknown), then
$$|R_n(x)| \le \frac{M}{(n+1)!}|x-a|^{n+1} \quad\text{for all } x\in I.$$

### Theorem 6.8: Convergence of Taylor Series $\Longleftrightarrow$ $R_n(x)\to 0$

$f(x)$ equals its Taylor series at $a$, for a given $x$, **if and only if** $\displaystyle\lim_{n\to\infty} R_n(x) = 0$. Strategy to prove a function is analytic on all of $I$: find a bound $M$ (possibly depending on the interval, but *not* on $n$) for $\left|f^{(n+1)}\right|$ on $I$, plug into the Lagrange bound, and show the resulting bound $\to 0$ as $n\to\infty$ — usually because it contains a factorial in the denominator, which beats any fixed power or exponential in the numerator.

### Key Fact: Maclaurin Series for Common Functions (Table 6.1)

$$\frac{1}{1-x}=\sum_{n=0}^{\infty}x^n\ (|x|<1), \qquad e^x=\sum_{n=0}^{\infty}\frac{x^n}{n!}\ (\text{all }x), \qquad \sin x=\sum_{n=0}^{\infty}(-1)^n\frac{x^{2n+1}}{(2n+1)!}\ (\text{all }x),$$
$$\cos x=\sum_{n=0}^{\infty}(-1)^n\frac{x^{2n}}{(2n)!}\ (\text{all }x), \qquad \ln(1+x)=\sum_{n=1}^{\infty}(-1)^{n+1}\frac{x^n}{n}\ (-1<x\le1), \qquad \arctan x=\sum_{n=0}^{\infty}(-1)^n\frac{x^{2n+1}}{2n+1}\ (-1\le x\le 1).$$
These six (plus the binomial series $(1+x)^r=\sum\binom{r}{n}x^n$, $|x|<1$) are the toolbox for §6.4 — you are expected to *recognize* a disguised version of one of these rather than differentiate from scratch.

### Key Fact: Constructing New Series from Known Ones

Three legal moves, all justified by uniqueness (Theorem 6.6) and Theorem 6.4: **(1) substitute** a function of $x$ into a known series in place of the variable; **(2) differentiate or integrate** a known series term-by-term; **(3) combine algebraically** — add, subtract, or multiply two known series by a common factor of $x^k$. Whichever moves you use, the interval of validity is inherited from the original series (intersected, if you combine two series with different intervals) — always state it.

## Pages 2–3 — Solved Examples

**Example 1 (proving $\sin x$ is analytic on all of $\mathbb R$, using the Lagrange bound).** Show $\displaystyle\lim_{n\to\infty}R_n(x)=0$ for every real $x$, where $R_n(x)$ is the remainder for the Maclaurin series of $\sin x$.

*Solution.* Every derivative of $\sin x$ is $\pm\sin x$ or $\pm\cos x$, so $\left|f^{(n+1)}(t)\right|\le 1$ for **every** $t\in\mathbb R$ and **every** $n$ — a single bound $M=1$ works on the whole real line, independent of $n$. By the Lagrange bound, $|R_n(x)| \le \dfrac{1}{(n+1)!}|x|^{n+1}$. Fix any $x$; then $\dfrac{|x|^{n+1}}{(n+1)!}\to 0$ as $n\to\infty$ (factorial growth eventually dominates any fixed power — this is a standard limit fact, provable by the Ratio Test applied to the series $\sum \frac{|x|^{n+1}}{(n+1)!}$, which must converge, forcing its terms to $\to0$). By Squeeze, $R_n(x)\to 0$ for every $x$. By Theorem 6.8, $\sin x$ equals its Maclaurin series for all $x\in\mathbb R$ — **$\sin x$ is analytic everywhere.**

**Example 2 (the general analyticity criterion, fill-in-the-blank reconstructed).** State a hypothesis on $f$ guaranteeing $f$ is analytic on all of an interval $I$.

*Solution.* It suffices that there exist a **single constant $M$** (not depending on $n$) such that $\left|f^{(n+1)}(t)\right| \le M$ for **every** $n$ and **every** $t\in I$. Then exactly the argument of Example 1 applies verbatim: the Lagrange bound gives $|R_n(x)|\le \frac{M}{(n+1)!}|x-a|^{n+1}\to0$ for every $x\in I$, so $f=$ its Taylor series on all of $I$. *Misconception flag:* it is **not** enough for each individual derivative to merely be bounded (i.e.\ a possibly-different bound $M_n$ for each $n$) — if $M_n$ grows too fast with $n$, the ratio $M_n/(n+1)!$ need not $\to 0$. The bound must be **uniform in $n$**.

**Example 3 (deriving $\arctan x$ as a power series, then extracting one derivative value).** Given $G(x)=\arctan x$, derive its Maclaurin series and find $G^{(137)}(0)$.

*Solution.* $G'(x) = \dfrac{1}{1+x^2} = \dfrac{1}{1-(-x^2)} = \displaystyle\sum_{n=0}^\infty(-x^2)^n = \sum_{n=0}^\infty(-1)^nx^{2n}$ for $|x|<1$. Integrate term-by-term: $G(x) = C+\displaystyle\sum_{n=0}^\infty(-1)^n\dfrac{x^{2n+1}}{2n+1}$; since $G(0)=\arctan0=0$, $C=0$. So $\arctan x = \displaystyle\sum_{n=0}^\infty (-1)^n\dfrac{x^{2n+1}}{2n+1}$. **To find $G^{(137)}(0)$,** don't differentiate $137$ times — match coefficients with the *definition* of the Maclaurin series: the coefficient of $x^{137}$ in $\sum \frac{G^{(n)}(0)}{n!}x^n$ is $\dfrac{G^{(137)}(0)}{137!}$. Since $137=2n+1\Rightarrow n=68$ (and $137$ is odd, matching the series' odd powers, with sign $(-1)^{68}=1$), the coefficient of $x^{137}$ is $\dfrac{1}{137}$. Setting equal: $\dfrac{G^{(137)}(0)}{137!}=\dfrac1{137} \Rightarrow G^{(137)}(0) = \dfrac{137!}{137} = 136!$.

**Example 4 (exact evaluation of a numerical series, recognizing it as a known series value).** Evaluate $A = \displaystyle\sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)3^n\sqrt3}$ exactly.

*Solution.* Recall $\arctan x = \sum_{n=0}^\infty (-1)^n \dfrac{x^{2n+1}}{2n+1}$. We want the sum to look like this with $x^{2n+1}$ producing a $3^{-n}$ factor: try $x=\dfrac{1}{\sqrt3}$, so $x^{2n+1} = \dfrac{1}{3^n\sqrt3}$ — matches exactly. So $A = \arctan\dfrac{1}{\sqrt3} = \dfrac{\pi}{6}$ (a standard reference angle). *Misconception flag:* the temptation is to try to "compute" an infinite sum numerically — the entire point of this technique is to recognize the numerical series as a **known function's Maclaurin series evaluated at a specific point**, giving an exact closed form.

**Example 5 (series gymnastics — building new series from known ones, several moves at once).** Find the Maclaurin series for $f(x) = x^2\cos x$ and state its interval of validity.

*Solution.* Start from $\cos x = \displaystyle\sum_{n=0}^\infty(-1)^n\dfrac{x^{2n}}{(2n)!}$ (all $x$). Multiply through by $x^2$ (a legal algebraic combination — pure substitution of the extra factor):
$$x^2\cos x = \sum_{n=0}^{\infty}(-1)^n\frac{x^{2n+2}}{(2n)!},$$
valid for all $x$ (multiplying by a polynomial doesn't change the radius of convergence).

**Example 6 (series gymnastics — a rational function via geometric-series substitution and scaling).** Find the Maclaurin series for $f(x) = \dfrac{x}{3+2x}$.

*Solution.* $\dfrac{x}{3+2x} = \dfrac{x}{3}\cdot\dfrac{1}{1+\frac{2x}{3}} = \dfrac x3\displaystyle\sum_{n=0}^\infty\left(-\dfrac{2x}3\right)^n = \sum_{n=0}^\infty \dfrac{(-1)^n2^n}{3^{n+1}}x^{n+1}$, valid for $\left|\dfrac{2x}3\right|<1\iff |x|<\dfrac32$.

**Example 7 (limit via Maclaurin substitution, higher-order terms matter).** Evaluate $\displaystyle\lim_{x\to0}\frac{\sin x - x+\frac{x^3}{6}}{x^5}$.

*Solution.* Substitute the full Maclaurin series: $\sin x = x-\dfrac{x^3}{6}+\dfrac{x^5}{120}-\dfrac{x^7}{5040}+\cdots$. Then
$$\sin x - x + \frac{x^3}{6} = \frac{x^5}{120}-\frac{x^7}{5040}+\cdots = x^5\left(\frac{1}{120}-\frac{x^2}{5040}+\cdots\right).$$
Divide by $x^5$ and let $x\to0$: every remaining term has a positive power of $x$ except the first, so the limit is $\dfrac{1}{120}$. *Misconception flag:* stopping the $\sin x$ expansion at $x^3$ (matching only the terms that are being explicitly subtracted) throws away the $x^5$ term that **is** the answer — always carry the series at least one order past the cancellation you expect.

**Example 8 (comparing growth via series, a two-limit contrast).** Determine which is larger for small $x>0$: $\cos(2x)$ or $e^{-2x^2}$, by comparing their Maclaurin series through the $x^4$ term.

*Solution.* $\cos(2x) = 1-\dfrac{(2x)^2}{2}+\dfrac{(2x)^4}{24}-\cdots = 1-2x^2+\dfrac{2}{3}x^4-\cdots$. Also $e^{-2x^2} = \displaystyle\sum_{n=0}^\infty\dfrac{(-2x^2)^n}{n!} = 1-2x^2+2x^4-\cdots$. Both start $1-2x^2+\cdots$, agreeing through the $x^2$ term, but the $x^4$ coefficients differ: $\dfrac23$ for $\cos(2x)$ versus $2$ for $e^{-2x^2}$. Since $\dfrac23<2$, for small $x>0$, $\cos(2x) < e^{-2x^2}$ (the smaller coefficient pulls the value down less than the larger one, but with a **negative** leading correction already applied at $x^2$ — concretely, $\cos(2x)-e^{-2x^2}\approx\left(\dfrac23-2\right)x^4 = -\dfrac43x^4<0$ for small $x\ne0$).

**Example 9 (numerical estimation with a guaranteed error bound — Alternating Series Remainder).** Estimate $B=\ln(0.9)$ to error less than $0.001$.

*Solution.* $\ln(1+x) = \displaystyle\sum_{n=1}^\infty(-1)^{n+1}\dfrac{x^n}{n}$ at $x=-0.1$: $\ln(0.9) = \displaystyle\sum_{n=1}^\infty(-1)^{n+1}\dfrac{(-0.1)^n}{n} = -\sum_{n=1}^\infty \dfrac{(0.1)^n}{n}$ (every term is negative, since $(-1)^{n+1}(-0.1)^n = -(-1)^n(-1)^n(0.1)^n\cdot(-1)= -(0.1)^n$ — check directly: $n=1$ term is $(+1)\cdot(-0.1)=-0.1$; $n=2$ term is $(-1)\cdot0.01=-0.01$; all terms come out negative). This is an alternating-in-form series in the underlying $\sum(0.1)^n/n$ once factored, so use the Alternating Series Remainder bound on the terms $b_n = \dfrac{(0.1)^n}{n}$: we need the first *omitted* term to satisfy $b_{n+1}<0.001$. $b_1=0.1,\,b_2=0.005,\,b_3=0.000333\ldots<0.001$. So keeping terms through $n=2$ (partial sum $-0.1-0.005=-0.105$) guarantees error $<b_3<0.001$. **$\ln(0.9)\approx -0.105$** to the required accuracy.

**Example 10 (a nonelementary-looking integral, estimated via series).** Estimate $\displaystyle\int_0^1 \frac{\sin x}{x}\,dx$ to three decimal places (this integrand has no elementary antiderivative).

*Solution.* $\dfrac{\sin x}{x} = \displaystyle\sum_{n=0}^\infty(-1)^n\dfrac{x^{2n}}{(2n+1)!} = 1-\dfrac{x^2}{6}+\dfrac{x^4}{120}-\dfrac{x^6}{5040}+\cdots$ (valid for all $x$, including the removable point $x=0$). Integrate term-by-term from $0$ to $1$: $\displaystyle\int_0^1\dfrac{\sin x}x\,dx = 1-\dfrac{1}{18}+\dfrac{1}{600}-\dfrac{1}{35280}+\cdots$. This is alternating with rapidly shrinking terms; the fourth term $\frac1{35280}\approx0.0000283$ is already below the needed precision, so summing the first three terms: $1-0.05556+0.001667 \approx 0.94611$. **$\displaystyle\int_0^1\frac{\sin x}x\,dx \approx 0.946$.**

## Pages 4–5 — Practice Problems (unsolved)

**Proving analyticity**

1. Show that $e^x$ is analytic on every interval $[-R,R]$ (i.e.\ $R_n(x)\to0$ for every fixed $x$), using the Lagrange bound with $M=e^R$ (justify why this $M$ works for every $t\in[-R,R]$).
2. Explain, in a sentence, why the argument in Problem 1 does **not** immediately give "analytic on all of $\mathbb R$ with a single bound $M$" the way $\sin x$'s argument did — and why it doesn't need to (what do you do instead to conclude $e^x$ is analytic everywhere)?

**Deriving series and extracting a single derivative value**

3. Given $f(x) = \dfrac{1}{1-x^3}$, write its Maclaurin series (substitution into the geometric series) and find $f^{(15)}(0)$.
4. Using the arcsin power series (given: $\dfrac{1}{\sqrt{1+x}} = 1-\dfrac12x+\dfrac{1\cdot3}{2\cdot4}x^2-\dfrac{1\cdot3\cdot5}{2\cdot4\cdot6}x^3+\cdots$ derived from the binomial series with $r=-\frac12$), set up $h(x)=\arcsin x$ as $h'(x) = (1-x^2)^{-1/2}$ and integrate term-by-term to find the first three nonzero terms of $\arcsin x$ centered at $0$.
5. Find $A = \displaystyle\sum_{n=0}^\infty \dfrac{1}{n!}$ exactly, by recognizing it as a known Maclaurin series evaluated at a specific point.

**Series gymnastics**

6. Find the Maclaurin series for $f(x) = e^{-x}$ and state its interval of validity.
7. Find the Maclaurin series for $f(x) = \dfrac{e^x+e^{-x}}{2}$ (hyperbolic cosine) by adding two known series and dividing by $2$. What happens to the odd-power terms, and why does that make sense given $f$ is an even function?
8. Find the Maclaurin series for $f(x) = \ln\dfrac{1+x}{1-x}$ using $\ln(1+x)-\ln(1-x)$ and two applications of the known $\ln(1+x)$ series (careful with the substitution in the second one).

**Limits and estimation**

9. Evaluate $\displaystyle\lim_{x\to0}\dfrac{\cos x - 1+\frac{x^2}2}{x^4}$ using Maclaurin series.
10. Estimate $\sin(1)$ using the first three nonzero terms of its Maclaurin series, and use the Alternating Series Remainder to state a guaranteed error bound on your estimate.
11. Estimate $\displaystyle\int_0^1 e^{-x^2}\,dx$ to two decimal places using the Maclaurin series for $e^{-x^2}$, integrated term-by-term (state how many terms you needed and why you can stop there).

**Reasoning**

12. A student claims: "Since the Taylor series of $f$ at $a$ converges for all $x\in\mathbb R$, we know $f$ equals its Taylor series everywhere." Explain precisely why this claim is **false** in general, citing the distinction between "the series converges" and "the series converges to $f$" (Theorem 6.8), and what extra ingredient (the Lagrange remainder bound) is needed to upgrade convergence to equality.

## Answer Key & Misconception Notes (for tutor use — do not show student until after attempt)

| # | Answer | Common misconception |
|---|--------|----------------------|
| 1 | Every derivative of $e^x$ is $e^x$ itself, and on $[-R,R]$, $e^t \le e^R$ for all $t$ in that interval — so $M=e^R$ bounds $\left|f^{(n+1)}(t)\right|$ uniformly in both $t\in[-R,R]$ and $n$. Then $|R_n(x)|\le \dfrac{e^R}{(n+1)!}|x|^{n+1}\to0$ as $n\to\infty$ for any fixed $x\in[-R,R]$ (factorial beats any fixed base). | Trying to use $M=e^x$ itself as the bound (a variable, not a constant) — the bound **must** be a single number that works for the whole interval, not a function of $t$. |
| 2 | The bound $M=e^R$ depends on $R$ — it isn't a single constant working for *all* of $\mathbb R$ simultaneously (as $R\to\infty$, $M\to\infty$ too, and the Lagrange bound argument would need $\lim_n \frac{e^R}{(n+1)!}|x|^{n+1}$, which is fine for each *fixed* $R$, but $R$ itself was tied to $x$). Instead: fix any $x\in\mathbb R$, choose $R=\lvert x\rvert$ (or larger), apply Problem 1's argument on $[-R,R]$, and conclude $R_n(x)\to0$ for *that* $x$ — repeating this for every $x$ shows $e^x$ is analytic on all of $\mathbb R$, just interval-by-interval rather than with one universal $M$. | Assuming "analytic on every bounded interval" is somehow weaker than "analytic on $\mathbb R$" — together, "analytic on $[-R,R]$ for every $R$" **is** exactly what "analytic on $\mathbb R$" means, since every real number lies in some $[-R,R]$. |
| 3 | $\dfrac{1}{1-x^3} = \displaystyle\sum_{n=0}^\infty x^{3n} = 1+x^3+x^6+x^9+\cdots$ (substitute $x^3$ into the geometric series, valid $|x|<1$). Coefficient of $x^{15}$: since $15=3n\Rightarrow n=5$, the coefficient is $1$. Matching with $\dfrac{f^{(15)}(0)}{15!}=1\Rightarrow f^{(15)}(0)=15!$. | Forgetting that most coefficients in this series are $0$ (only multiples of $3$ appear) — if asked for, say, $f^{(16)}(0)$ instead, the answer would be $0$, not "undefined." |
| 4 | $h'(x)=(1-x^2)^{-1/2}$: substitute $-x^2$ for $x$ in the given series for $(1+x)^{-1/2}$: $h'(x) = 1-\dfrac12(-x^2)+\dfrac{1\cdot3}{2\cdot4}(-x^2)^2-\cdots = 1+\dfrac12x^2+\dfrac{3}{8}x^4+\cdots$ (signs flip to all-positive because $(-x^2)^n$ alternates sign in a way that cancels the series' own alternating sign). Integrating: $h(x) = x+\dfrac16x^3+\dfrac{3}{40}x^5+\cdots$ (using $\int x^2\,dx=\frac{x^3}3$ so $\frac12\cdot\frac13=\frac16$, and $\int x^4\,dx=\frac{x^5}5$ so $\frac38\cdot\frac15=\frac{3}{40}$); constant of integration is $0$ since $\arcsin(0)=0$. | Substituting $-x^2$ for $x$ but forgetting to also square/cube the coefficient signs correctly — a very common sign-tracking error; safest is to substitute one term at a time and simplify before moving to the next. |
| 5 | $e^x = \displaystyle\sum_{n=0}^\infty\dfrac{x^n}{n!}$; at $x=1$: $e^1 = \displaystyle\sum_{n=0}^\infty\dfrac1{n!} = A$. **$A=e$.** | Trying to compute this as an unfamiliar numerical series rather than instantly recognizing the pattern $\frac{1}{n!}$ as the $e^x$ series evaluated at $x=1$ — this recognition should be immediate once the six core series are memorized. |
| 6 | $e^{-x} = \displaystyle\sum_{n=0}^\infty\dfrac{(-x)^n}{n!} = \sum_{n=0}^\infty\dfrac{(-1)^nx^n}{n!}$, valid for all $x$ (substitution never shrinks an infinite radius). | Writing $e^{-x}=-e^x$ or otherwise trying to relate it algebraically to $e^x$ as a whole, instead of substituting directly into the series (they are **not** negatives of each other). |
| 7 | $\dfrac{e^x+e^{-x}}2 = \dfrac12\left[\displaystyle\sum_{n=0}^\infty\dfrac{x^n}{n!}+\sum_{n=0}^\infty\dfrac{(-1)^nx^n}{n!}\right] = \displaystyle\sum_{n=0}^\infty \dfrac{1+(-1)^n}{2}\cdot\dfrac{x^n}{n!} = \sum_{k=0}^\infty \dfrac{x^{2k}}{(2k)!}$ (all odd-$n$ terms cancel since $1+(-1)^n=0$ there; even-$n$ terms double then get halved back). This makes sense because $f$ is even ($f(-x)=f(x)$), and an even function's Maclaurin series can only contain even powers of $x$ — odd-power coefficients must vanish identically. | Not connecting the algebraic cancellation to the general fact about even/odd functions — this is a reusable shortcut: even $f\Rightarrow$ series has only even powers; odd $f\Rightarrow$ only odd powers; check this *before* grinding through the addition. |
| 8 | $\ln(1+x) = \displaystyle\sum_{n=1}^\infty(-1)^{n+1}\dfrac{x^n}n$; and $\ln(1-x) = \displaystyle\sum_{n=1}^\infty(-1)^{n+1}\dfrac{(-x)^n}{n} = \sum_{n=1}^\infty(-1)^{n+1}(-1)^n\dfrac{x^n}n = -\sum_{n=1}^\infty\dfrac{x^n}n$. So $\ln\dfrac{1+x}{1-x} = \ln(1+x)-\ln(1-x) = \displaystyle\sum_{n=1}^\infty\left[(-1)^{n+1}+1\right]\dfrac{x^n}{n} = \sum_{k=0}^\infty \dfrac{2}{2k+1}x^{2k+1}$ (only odd $n$ survive), valid for $|x|<1$. | Substituting $-x$ for $x$ in the $\ln(1+x)$ series but forgetting that $(-1)^{n+1}(-x)^n$ simplifies to a **constant sign** ($-1$, not alternating) once you track $(-1)^n$ separately — this is the same sign-tracking trap as Problem 4. |
| 9 | $\cos x = 1-\dfrac{x^2}2+\dfrac{x^4}{24}-\cdots$, so $\cos x-1+\dfrac{x^2}2 = \dfrac{x^4}{24}-\dfrac{x^6}{720}+\cdots = x^4\left(\dfrac1{24}-\dfrac{x^2}{720}+\cdots\right)$. Dividing by $x^4$ and letting $x\to0$: limit is $\dfrac{1}{24}$. | Stopping the $\cos x$ expansion at the $x^2$ term (matching only what's explicitly subtracted) and missing the $x^4$ term that produces the actual limit — same trap as Example 7. |
| 10 | $\sin1 \approx 1-\dfrac16+\dfrac1{120} = 1-0.16\overline6+0.008\overline3 \approx 0.84167$. Alternating Series Remainder: error $\le$ next omitted term $= \dfrac{1}{5040}\approx0.000198$, so $\sin(1) = 0.84167\pm0.0002$ (matches the true value $\sin1\approx0.84147$). | Reporting the estimate without stating an error bound — the whole point of using the *Alternating Series* Remainder (rather than a vague "should be close") is that it gives a **guaranteed, computable** bound on how far off the truncated sum can be. |
| 11 | $e^{-x^2} = \displaystyle\sum_{n=0}^\infty\dfrac{(-x^2)^n}{n!} = 1-x^2+\dfrac{x^4}2-\dfrac{x^6}6+\dfrac{x^8}{24}-\cdots$. Integrate term-by-term from $0$ to $1$: $1-\dfrac13+\dfrac1{10}-\dfrac1{42}+\dfrac1{216}-\cdots \approx 1-0.3333+0.1-0.0238+0.00463-\cdots \approx 0.7475$. The 5th term ($\approx0.0046$) already affects only the third decimal, and the 6th term is smaller still, so stopping after 5 terms gives **$\approx 0.75$** to two decimal places (matches the known value $\approx0.7468$ closely enough at this precision; a careful bound would keep one more term to be fully rigorous about the *second* decimal — worth flagging to a strong student). | Integrating only the first two or three terms and declaring victory without checking that the omitted terms are actually small enough for the *requested* precision — always state which term you stopped at and why it's safely below the needed error. |
| 12 | Convergence of the Taylor series (as a series, for whichever $x$ make it converge) says nothing by itself about what it converges *to* — Theorem 6.8 says the series equals $f(x)$ **only when** $R_n(x)\to0$ for that $x$. A series can converge everywhere yet its sum disagree with $f$ off an isolated point (the standard example, not required here, is $f(x)=e^{-1/x^2}$ for $x\ne0$, $f(0)=0$: every derivative at $0$ is $0$, so its Maclaurin series is identically $0$, which trivially "converges everywhere" — to $0$, not to $f(x)$, for any $x\ne0$). The extra ingredient is exactly the Lagrange remainder bound: you need $R_n(x)\to0$, not just that the series of $\frac{f^{(n)}(a)}{n!}(x-a)^n$ happens to converge as a numerical series. | Treating "the Taylor series converges" and "the function is analytic" as synonyms — this is precisely the gap Theorem 6.8 exists to close, and it is a favorite trap on both problem sets and exams (including a T/F-style question worth flagging as exam-relevant). |

---

**Enrichment closer (not a problem — read together as a capstone).** MAT137's final slide deck presents, without proof,
$$\cot x = \frac1x - \frac{2}{6}x - \frac{2}{90}x^3 - \frac{2}{945}x^5 - \cdots,$$
whose coefficients are secretly built from the values $\zeta(2)=\displaystyle\sum\frac1{n^2}=\dfrac{\pi^2}{6}$, $\zeta(4)=\dfrac{\pi^4}{90}$, $\zeta(6)=\dfrac{\pi^6}{945}$ (the **Basel problem** and its higher-power cousins). This is a nice place to point out to a strong student that power series don't just approximate known functions — sometimes the *coefficients themselves* encode deep number-theoretic facts, discovered by Euler roughly 300 years ago.
