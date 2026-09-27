# Week 13 — Taylor & Maclaurin Series: Analytic Functions

**Session length:** 60 minutes (Pages 1–5, self-paced)
**Source:** OpenStax *Calculus Volume 2*, §6.3 (Taylor and Maclaurin Series) — Theorem 6.6 (Uniqueness of Taylor Series), Theorem 6.7 (Taylor's Theorem with Remainder), Theorem 6.8 (Convergence of Taylor Series), Table 6.1 (Maclaurin Series for Common Functions); §6.4 (Working with Taylor Series) — constructing new series by substitution/differentiation/integration. MAT137 Unit 14 slides (14.7–14.11: Lagrange's Remainder Theorem and proving $\sin x$ is analytic; the general analyticity criterion; deriving $\arctan x$ as a power series and extracting a single high-order derivative value; "Taylor series gymnastics" — building new series from known ones) — MAT137 is the University of Toronto's official exclusion-equivalent of MATA37H3.

## Page 1 — Definitions and Key Facts

### Definition: Taylor Series, Maclaurin Series, Analytic Function

If $f$ has derivatives of every order at $x=a$, the **Taylor series for $f$ at $a$** is
$$\sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^n.$$
At $a=0$ this is the **Maclaurin series**. A function $f$ is **analytic at $a$** if there is an open interval containing $a$ on which $f$ equals its own Taylor series at $a$ — i.e. the Taylor series doesn't just converge, it converges *to $f$ itself*. (A Taylor series can converge everywhere and still fail to equal $f$ off a single point — this definition is exactly the guard against that.)

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
These six are the toolbox for building new series — you are expected to *recognize* a disguised version of one of these rather than differentiate from scratch. (The binomial series joins this toolbox in Week 14.)

### Key Fact: Constructing New Series from Known Ones

Three legal moves, all justified by uniqueness (Theorem 6.6) and Theorem 6.4 (Week 11): **(1) substitute** a function of $x$ into a known series in place of the variable; **(2) differentiate or integrate** a known series term-by-term; **(3) combine algebraically** — add, subtract, or multiply two known series by a common factor of $x^k$. Whichever moves you use, the interval of validity is inherited from the original series (intersected, if you combine two series with different intervals) — always state it.

## Pages 2–3 — Solved Examples

**Example 1 (proving $\sin x$ is analytic on all of $\mathbb R$, using the Lagrange bound).** Show $\displaystyle\lim_{n\to\infty}R_n(x)=0$ for every real $x$, where $R_n(x)$ is the remainder for the Maclaurin series of $\sin x$.

*Solution.* Every derivative of $\sin x$ is $\pm\sin x$ or $\pm\cos x$, so $\left|f^{(n+1)}(t)\right|\le 1$ for **every** $t\in\mathbb R$ and **every** $n$ — a single bound $M=1$ works on the whole real line, independent of $n$. By the Lagrange bound, $|R_n(x)| \le \dfrac{1}{(n+1)!}|x|^{n+1}$. Fix any $x$; then $\dfrac{|x|^{n+1}}{(n+1)!}\to 0$ as $n\to\infty$ (factorial growth eventually dominates any fixed power). By Squeeze, $R_n(x)\to 0$ for every $x$. By Theorem 6.8, $\sin x$ equals its Maclaurin series for all $x\in\mathbb R$ — **$\sin x$ is analytic everywhere.** $\blacksquare$

**Example 2 (the general analyticity criterion).** State a hypothesis on $f$ guaranteeing $f$ is analytic on all of an interval $I$.

*Solution.* It suffices that there exist a **single constant $M$** (not depending on $n$) such that $\left|f^{(n+1)}(t)\right| \le M$ for **every** $n$ and **every** $t\in I$. Then exactly the argument of Example 1 applies verbatim: the Lagrange bound gives $|R_n(x)|\le \frac{M}{(n+1)!}|x-a|^{n+1}\to0$ for every $x\in I$, so $f=$ its Taylor series on all of $I$. *Misconception flag:* it is **not** enough for each individual derivative to merely be bounded (i.e. a possibly-different bound $M_n$ for each $n$) — if $M_n$ grows too fast with $n$, the ratio $M_n/(n+1)!$ need not $\to 0$. The bound must be **uniform in $n$**. $\blacksquare$

**Example 3 (deriving $\arctan x$ as a power series, then extracting one derivative value).** Given $G(x)=\arctan x$, derive its Maclaurin series and find $G^{(137)}(0)$.

*Solution.* $G'(x) = \dfrac{1}{1+x^2} = \dfrac{1}{1-(-x^2)} = \displaystyle\sum_{n=0}^\infty(-x^2)^n = \sum_{n=0}^\infty(-1)^nx^{2n}$ for $|x|<1$. Integrate term-by-term: $G(x) = C+\displaystyle\sum_{n=0}^\infty(-1)^n\dfrac{x^{2n+1}}{2n+1}$; since $G(0)=\arctan0=0$, $C=0$. So $\arctan x = \displaystyle\sum_{n=0}^\infty (-1)^n\dfrac{x^{2n+1}}{2n+1}$. **To find $G^{(137)}(0)$,** don't differentiate $137$ times — match coefficients with the *definition* of the Maclaurin series: the coefficient of $x^{137}$ in $\sum \frac{G^{(n)}(0)}{n!}x^n$ is $\dfrac{G^{(137)}(0)}{137!}$. Since $137=2n+1\Rightarrow n=68$ (and $137$ is odd, matching the series' odd powers, with sign $(-1)^{68}=1$), the coefficient of $x^{137}$ is $\dfrac{1}{137}$. Setting equal: $\dfrac{G^{(137)}(0)}{137!}=\dfrac1{137} \Rightarrow G^{(137)}(0) = \dfrac{137!}{137} = 136!$. $\blacksquare$

**Example 4 (exact evaluation of a numerical series, recognizing it as a known series value).** Evaluate $A = \displaystyle\sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)3^n\sqrt3}$ exactly.

*Solution.* Recall $\arctan x = \sum_{n=0}^\infty (-1)^n \dfrac{x^{2n+1}}{2n+1}$. We want the sum to look like this with $x^{2n+1}$ producing a $3^{-n}$ factor: try $x=\dfrac{1}{\sqrt3}$, so $x^{2n+1} = \dfrac{1}{3^n\sqrt3}$ — matches exactly. So $A = \arctan\dfrac{1}{\sqrt3} = \dfrac{\pi}{6}$ (a standard reference angle). *Misconception flag:* the temptation is to try to "compute" an infinite sum numerically — the entire point of this technique is to recognize the numerical series as a **known function's Maclaurin series evaluated at a specific point**, giving an exact closed form. $\blacksquare$

**Example 5 (series gymnastics — building new series from known ones, several moves at once).** Find the Maclaurin series for $f(x) = x^2\cos x$ and state its interval of validity.

*Solution.* Start from $\cos x = \displaystyle\sum_{n=0}^\infty(-1)^n\dfrac{x^{2n}}{(2n)!}$ (all $x$). Multiply through by $x^2$ (a legal algebraic combination — pure substitution of the extra factor):
$$x^2\cos x = \sum_{n=0}^{\infty}(-1)^n\frac{x^{2n+2}}{(2n)!},$$
valid for all $x$ (multiplying by a polynomial doesn't change the radius of convergence). $\blacksquare$

**Example 6 (series gymnastics — a rational function via geometric-series substitution and scaling).** Find the Maclaurin series for $f(x) = \dfrac{x}{3+2x}$.

*Solution.* $\dfrac{x}{3+2x} = \dfrac{x}{3}\cdot\dfrac{1}{1+\frac{2x}{3}} = \dfrac x3\displaystyle\sum_{n=0}^\infty\left(-\dfrac{2x}3\right)^n = \sum_{n=0}^\infty \dfrac{(-1)^n2^n}{3^{n+1}}x^{n+1}$, valid for $\left|\dfrac{2x}3\right|<1\iff |x|<\dfrac32$. $\blacksquare$

## Pages 4–5 — Practice Problems (unsolved)

**Proving analyticity**

1. Show that $e^x$ is analytic on every interval $[-R,R]$ (i.e. $R_n(x)\to0$ for every fixed $x$), using the Lagrange bound with $M=e^R$ (justify why this $M$ works for every $t\in[-R,R]$).
2. Explain, in a sentence, why the argument in Problem 1 does **not** immediately give "analytic on all of $\mathbb R$ with a single bound $M$" the way $\sin x$'s argument did — and why it doesn't need to (what do you do instead to conclude $e^x$ is analytic everywhere)?

**Deriving series and extracting a single derivative value**

3. Given $f(x) = \dfrac{1}{1-x^3}$, write its Maclaurin series (substitution into the geometric series) and find $f^{(15)}(0)$.
4. Find $A = \displaystyle\sum_{n=0}^\infty \dfrac{1}{n!}$ exactly, by recognizing it as a known Maclaurin series evaluated at a specific point.
5. Evaluate $B=\displaystyle\sum_{n=0}^\infty\frac{(-1)^n\pi^{2n+1}}{4^{2n+1}(2n+1)!}$ exactly, by recognizing it as a known Maclaurin series value. (Hint: which of the six core series has odd powers over $(2n+1)!$ with alternating sign?)

**Series gymnastics**

6. Find the Maclaurin series for $f(x) = e^{-x}$ and state its interval of validity.
7. Find the Maclaurin series for $f(x) = \dfrac{e^x+e^{-x}}{2}$ (hyperbolic cosine) by adding two known series and dividing by $2$. What happens to the odd-power terms, and why does that make sense given $f$ is an even function?
8. Find the Maclaurin series for $f(x) = \ln\dfrac{1+x}{1-x}$ using $\ln(1+x)-\ln(1-x)$ and two applications of the known $\ln(1+x)$ series (careful with the substitution in the second one).

## Answer Key & Misconception Notes (for tutor use — do not show student until after attempt)

| # | Answer | Common misconception |
|---|--------|----------------------|
| 1 | Every derivative of $e^x$ is $e^x$ itself, and on $[-R,R]$, $e^t \le e^R$ for all $t$ in that interval — so $M=e^R$ bounds $\left|f^{(n+1)}(t)\right|$ uniformly in both $t\in[-R,R]$ and $n$. Then $|R_n(x)|\le \dfrac{e^R}{(n+1)!}|x|^{n+1}\to0$ as $n\to\infty$ for any fixed $x\in[-R,R]$ (factorial beats any fixed base). | Trying to use $M=e^x$ itself as the bound (a variable, not a constant) — the bound **must** be a single number that works for the whole interval, not a function of $t$. |
| 2 | The bound $M=e^R$ depends on $R$ — it isn't a single constant working for *all* of $\mathbb R$ simultaneously. Instead: fix any $x\in\mathbb R$, choose $R=\lvert x\rvert$ (or larger), apply Problem 1's argument on $[-R,R]$, and conclude $R_n(x)\to0$ for *that* $x$ — repeating this for every $x$ shows $e^x$ is analytic on all of $\mathbb R$, just interval-by-interval rather than with one universal $M$. | Assuming "analytic on every bounded interval" is somehow weaker than "analytic on $\mathbb R$" — together, "analytic on $[-R,R]$ for every $R$" **is** exactly what "analytic on $\mathbb R$" means, since every real number lies in some $[-R,R]$. |
| 3 | $\dfrac{1}{1-x^3} = \displaystyle\sum_{n=0}^\infty x^{3n} = 1+x^3+x^6+x^9+\cdots$ (substitute $x^3$ into the geometric series, valid $|x|<1$). Coefficient of $x^{15}$: since $15=3n\Rightarrow n=5$, the coefficient is $1$. Matching with $\dfrac{f^{(15)}(0)}{15!}=1\Rightarrow f^{(15)}(0)=15!$. | Forgetting that most coefficients in this series are $0$ (only multiples of $3$ appear) — if asked for, say, $f^{(16)}(0)$ instead, the answer would be $0$, not "undefined." |
| 4 | $e^x = \displaystyle\sum_{n=0}^\infty\dfrac{x^n}{n!}$; at $x=1$: $e^1 = \displaystyle\sum_{n=0}^\infty\dfrac1{n!} = A$. **$A=e$.** | Trying to compute this as an unfamiliar numerical series rather than instantly recognizing the pattern $\frac{1}{n!}$ as the $e^x$ series evaluated at $x=1$ — this recognition should be immediate once the six core series are memorized. |
| 5 | $\sin x = \displaystyle\sum_{n=0}^\infty(-1)^n\dfrac{x^{2n+1}}{(2n+1)!}$; at $x=\dfrac{\pi}{4}$: $\sin\dfrac{\pi}{4} = \displaystyle\sum_{n=0}^\infty(-1)^n\dfrac{(\pi/4)^{2n+1}}{(2n+1)!} = \sum_{n=0}^\infty\dfrac{(-1)^n\pi^{2n+1}}{4^{2n+1}(2n+1)!} = B$. So $B = \sin\dfrac{\pi}{4} = \dfrac{\sqrt2}{2}$. | Confusing the $\sin x$ series (odd powers over $(2n+1)!$) with the $\arctan x$ series (odd powers over $2n+1$, no factorial) — the presence of $(2n+1)!$ in the denominator is the signature of $\sin x$, not $\arctan x$. |
| 6 | $e^{-x} = \displaystyle\sum_{n=0}^\infty\dfrac{(-x)^n}{n!} = \sum_{n=0}^\infty\dfrac{(-1)^nx^n}{n!}$, valid for all $x$ (substitution never shrinks an infinite radius). | Writing $e^{-x}=-e^x$ or otherwise trying to relate it algebraically to $e^x$ as a whole, instead of substituting directly into the series (they are **not** negatives of each other). |
| 7 | $\dfrac{e^x+e^{-x}}2 = \dfrac12\left[\displaystyle\sum_{n=0}^\infty\dfrac{x^n}{n!}+\sum_{n=0}^\infty\dfrac{(-1)^nx^n}{n!}\right] = \displaystyle\sum_{n=0}^\infty \dfrac{1+(-1)^n}{2}\cdot\dfrac{x^n}{n!} = \sum_{k=0}^\infty \dfrac{x^{2k}}{(2k)!}$ (all odd-$n$ terms cancel since $1+(-1)^n=0$ there; even-$n$ terms double then get halved back). This makes sense because $f$ is even ($f(-x)=f(x)$), and an even function's Maclaurin series can only contain even powers of $x$ — odd-power coefficients must vanish identically. | Not connecting the algebraic cancellation to the general fact about even/odd functions — this is a reusable shortcut: even $f\Rightarrow$ series has only even powers; odd $f\Rightarrow$ only odd powers; check this *before* grinding through the addition. |
| 8 | $\ln(1+x) = \displaystyle\sum_{n=1}^\infty(-1)^{n+1}\dfrac{x^n}n$; and $\ln(1-x) = \displaystyle\sum_{n=1}^\infty(-1)^{n+1}\dfrac{(-x)^n}{n} = \sum_{n=1}^\infty(-1)^{n+1}(-1)^n\dfrac{x^n}n = -\sum_{n=1}^\infty\dfrac{x^n}n$. So $\ln\dfrac{1+x}{1-x} = \ln(1+x)-\ln(1-x) = \displaystyle\sum_{n=1}^\infty\left[(-1)^{n+1}+1\right]\dfrac{x^n}{n} = \sum_{k=0}^\infty \dfrac{2}{2k+1}x^{2k+1}$ (only odd $n$ survive), valid for $|x|<1$. | Substituting $-x$ for $x$ in the $\ln(1+x)$ series but forgetting that $(-1)^{n+1}(-x)^n$ simplifies to a **constant sign** ($-1$, not alternating) once you track $(-1)^n$ separately. |
