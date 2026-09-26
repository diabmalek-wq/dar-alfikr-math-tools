# Week 2 — The Fundamental Theorem of Calculus

**Session length:** 3 hours
**Source:** OpenStax, *Calculus Volume 2*, §1.3 (The Fundamental Theorem of Calculus); paired with MAT137 (Calculus with Proofs) Unit 8 lecture-slide prompts on antiderivatives, functions defined by integrals, and FTC Parts 1 & 2 — MAT137 is the University of Toronto's official exclusion-equivalent of MATA37H3

---

## Page 1 — Introduction, Key Facts & Definitions

### Recap and orientation

Unit 7 defined $\int_a^b f(x)\,dx$ as a limit of Riemann sums — a definition that is rigorous but nearly impossible to compute directly for anything but the simplest functions. This unit introduces the **Fundamental Theorem of Calculus (FTC)**, which converts definite-integral computation into an *antiderivative-lookup* problem: no more limits of sums needed. FTC has two parts — Part 1 says differentiating an integral gets you back the original function; Part 2 says you can evaluate a definite integral by plugging endpoints into any antiderivative. Together they say, informally, "integration and differentiation undo each other."

### Why this matters

Every integral you compute from Unit 9 onward — by substitution, by parts, with partial fractions — is really just "find an antiderivative, then invoke FTC Part 2." Misunderstanding FTC is also one of the most common sources of subtle errors on rigorous exams: confusing "an antiderivative" with "the antiderivative $\int_0^x f$", forgetting the chain rule when the upper limit is itself a function of $x$, and misapplying FTC to functions that are only piecewise continuous.

### Definition: Antiderivative and Indefinite Integral (MAT137 Unit 8)

A function $F$ is an **antiderivative** of $f$ on an interval $I$ if $F'(x) = f(x)$ for every $x \in I$. If $F$ is one antiderivative of $f$ on $I$, then *every* antiderivative of $f$ on $I$ has the form $F(x) + C$ for some constant $C$ — this is why we write $\int f(x)\,dx = F(x) + C$ (the **indefinite integral**), with the understanding that $C$ ranges over all real numbers.

**Watch for:** the "$+C$" fact requires $I$ to be a *single interval*. On a domain with a gap (like $\mathbb{R}\setminus\{0\}$), two antiderivatives can differ by a *different* constant on each piece — this is exactly the trap in Worked Example 1 below.

### Key Fact: Functions Defined by an Integral (MAT137 Unit 8)

An expression like $F(x) = \int_a^x f(t)\,dt$ (with $x$ as the *upper limit*, and a dummy variable $t$ inside) defines a genuine function of $x$: for each fixed $x$, the integral is a single number. This is a completely valid way to define a function, **even when $f$ has no elementary antiderivative** (e.g. $F(x) = \int_0^x e^{-t^2}\,dt$). It is *not* valid to have the same free variable appear both as the bound of integration and as the integration variable, e.g. $\int_0^x \frac{x}{1+t^8}\,dt$ mixes them; the variable of integration must be a dummy (like $t$), never the same letter as the limit.

### Theorem: Fundamental Theorem of Calculus, Part 1 (OpenStax §1.3, Theorem 1.4)

If $f$ is continuous on $[a,b]$, and $F(x) = \int_a^x f(t)\,dt$, then
$$F'(x) = f(x) \qquad \text{for every } x \text{ in } [a,b].$$
In words: the derivative of "the integral of $f$ from a fixed point to a variable point $x$" is just $f(x)$ itself. This is the precise sense in which integration and differentiation are inverse operations.

### Key Fact: FTC Part 1 with a Function in the Limit (Chain Rule Extension)

If $F(x) = \int_a^{g(x)} f(t)\,dt$ for a differentiable function $g$, then by FTC Part 1 combined with the chain rule,
$$F'(x) = f(g(x))\cdot g'(x).$$
If the **lower** limit is the variable instead, $\int_{g(x)}^{b} f(t)\,dt = -\int_b^{g(x)} f(t)\,dt$, so differentiating picks up an extra minus sign: $\dfrac{d}{dx}\displaystyle\int_{g(x)}^b f(t)\,dt = -f(g(x))\,g'(x)$. If **both** limits depend on $x$, split the integral at any convenient constant point and differentiate each piece separately.

### Theorem: Fundamental Theorem of Calculus, Part 2 — the Evaluation Theorem (OpenStax §1.3, Theorem 1.5)

If $f$ is continuous on $[a,b]$ and $F$ is **any** antiderivative of $f$ on $[a,b]$, then
$$\int_a^b f(x)\,dx = F(b) - F(a),$$
often written $F(x)\Big|_a^b$. This is what makes definite integrals computable: find *any one* antiderivative, evaluate it at the two endpoints, subtract. It does not matter which antiderivative you pick — the arbitrary constant $C$ always cancels in the subtraction.

### Key Fact: General Solution to $G'(x) = f(x)$, $G(x_0) = y_0$ (MAT137 Unit 8)

If $f$ is continuous on $\mathbb{R}$ and we want the *unique* function $G$ with $G'(x)=f(x)$ **and** a prescribed value $G(x_0) = y_0$, the answer is
$$G(x) = y_0 + \int_{x_0}^{x} f(t)\,dt.$$
This single formula answers "which antiderivative?" — a bare antiderivative of $f$ is only ever determined up to $+C$; pinning down one specific value $G(x_0)=y_0$ removes that ambiguity and produces exactly this formula, not $\displaystyle\int_0^x f(t)\,dt$ unless $x_0=0$ and $y_0=0$.

### Definition: Mean Value Theorem for Integrals & Average Value (OpenStax §1.3, Theorem 1.3)

If $f$ is continuous on $[a,b]$, there exists at least one point $c \in [a,b]$ such that
$$f(c) = \frac{1}{b-a}\int_a^b f(x)\,dx.$$
The right-hand side, $\dfrac{1}{b-a}\displaystyle\int_a^b f(x)\,dx$, is called the **average value** of $f$ on $[a,b]$ — this theorem says a continuous function always *attains* its own average value somewhere on the interval.

---

## Pages 2–3 — Solved Examples

**Example 1 (The most misunderstood antiderivative).** Find $\displaystyle\int \frac{1}{x}\,dx$, and explain why $F_1(x)=\ln x$ alone is not a correct general answer.

$F_1(x) = \ln x$ has domain $(0,\infty)$ only, so it cannot be the antiderivative on all of $\mathbb{R}\setminus\{0\}$. Instead consider $F_3(x) = \ln\lvert x\rvert$: for $x>0$, $F_3(x)=\ln x$ so $F_3'(x)=\frac1x$; for $x<0$, $F_3(x)=\ln(-x)$ so by the chain rule $F_3'(x) = \dfrac{1}{-x}\cdot(-1) = \dfrac1x$. So $F_3'(x)=\dfrac1x$ on **both** pieces of the domain, giving
$$\int \frac1x\,dx = \ln|x| + C.$$
But since the domain $\mathbb{R}\setminus\{0\}$ is *not* a single interval, the constant is allowed to be **different on each side of $0$**: the most general antiderivative is actually
$$G(x) = \begin{cases} \ln|x| + C_1 & x>0 \\ \ln|x| + C_2 & x<0\end{cases}$$
for independently chosen $C_1, C_2$. This is why $F_4(x) = \ln|2x| = \ln|x|+\ln 2$ is *also* a valid antiderivative on $x>0$ — it just corresponds to $C_1 = \ln 2$ — and does not contradict the "$+C$" rule, because that rule only guarantees a single shared constant on a connected interval. $\blacksquare$

---

**Example 2 (FTC Part 1, straightforward and with the chain rule).** Find $F'(x)$ for (a) $F(x) = \displaystyle\int_2^x \sin(t^3)\,dt$, and (b) $G(x) = \displaystyle\int_1^{x^2} \dfrac{\sin t}{t^2}\,dt$.

(a) By FTC Part 1 directly (the upper limit is bare $x$), $F'(x) = \sin(x^3)$.

(b) Here the upper limit is $g(x)=x^2$, not $x$ itself, so we need the chain-rule extension: with $f(t) = \dfrac{\sin t}{t^2}$,
$$G'(x) = f(g(x))\cdot g'(x) = \frac{\sin(x^2)}{(x^2)^2}\cdot 2x = \frac{2x\sin(x^2)}{x^4} = \frac{2\sin(x^2)}{x^3}. \qquad \blacksquare$$

---

**Example 3 (FTC Part 1 with the variable in the lower limit and both limits).** Find $F'(x)$ for $F(x) = \displaystyle\int_{2x}^{x^2} \dfrac{1}{1+t^3}\,dt$.

Split at a convenient constant, say $t=0$:
$$F(x) = \int_{2x}^{0}\frac{dt}{1+t^3} + \int_0^{x^2}\frac{dt}{1+t^3} = -\int_0^{2x}\frac{dt}{1+t^3} + \int_0^{x^2}\frac{dt}{1+t^3}.$$
Differentiate each piece with the chain rule (using $f(t)=\dfrac{1}{1+t^3}$):
$$F'(x) = -f(2x)\cdot 2 + f(x^2)\cdot 2x = \frac{-2}{1+8x^3} + \frac{2x}{1+x^6}. \qquad \blacksquare$$

---

**Example 4 (Reading FTC Part 1 off a piecewise-linear graph).** Let $f$ be the piecewise-linear function with $f(0)=0$, rising with slope $1$ to $f(1)=1$, constant at $1$ on $[1,2]$, falling with slope $-1$ to $f(3)=0$ and continuing to $f(4)=-1$, then constant at $-1$ on $[4,5]$. Let $F(x) = \int_0^x f(t)\,dt$. Sketch $F$ and describe $F'$.

Since $F$ is an antiderivative of $f$ by FTC Part 1, $F' = f$ — so wherever $f$ is *positive*, $F$ is increasing; wherever $f$ is *negative*, $F$ is decreasing; and $F$ has a local max/min exactly where $f$ crosses zero. Computing $F$ by accumulating signed area under $f$: $F(0)=0$; on $[0,1]$, area of a triangle $=\frac12$, so $F(1)=\frac12$; on $[1,2]$, add a $1\times1$ rectangle, so $F(2)=\frac32$; on $[2,3]$, $f$ falls linearly from $1$ to $0$, adding another triangle of area $\frac12$, so $F(3)=2$ (this is $F$'s **maximum**, since $f$ changes from $+$ to $-$ there); on $[3,4]$, $f$ is negative (a triangle from $0$ down to $-1$), subtracting $\frac12$, so $F(4)=\frac32$; on $[4,5]$, $f\equiv-1$, subtracting $1$ more, so $F(5)=\frac12$. So $F$ rises from $0$ to a peak of $2$ at $x=3$, then falls to $\frac12$ at $x=5$ — and $F'(x)=f(x)$ throughout, confirming FTC Part 1 graphically. $\blacksquare$

---

**Example 5 (FTC Part 2 — basic evaluation).** Evaluate $\displaystyle\int_1^3 (2x^2 - 4)\,dx$.

An antiderivative of $2x^2-4$ is $F(x) = \dfrac{2x^3}{3} - 4x$ (any choice of $C$ works; take $C=0$). By FTC Part 2,
$$\int_1^3(2x^2-4)\,dx = F(3)-F(1) = \left(\frac{2(27)}{3}-12\right) - \left(\frac23 - 4\right) = (18-12)-\left(\frac23-4\right) = 6+\frac{10}{3} = \frac{28}{3}. \qquad \blacksquare$$

---

**Example 6 (Area between a function and the $x$-axis, watching for sign changes).** Find the area of the region bounded by $y=\sin x$ and the $x$-axis on $[0,2\pi]$.

$\sin x \geq 0$ on $[0,\pi]$ and $\sin x \leq 0$ on $[\pi,2\pi]$, so **naively** computing $\int_0^{2\pi}\sin x\,dx$ would let the negative part cancel the positive part — giving the *net signed area*, not the true geometric area. Instead, split and take absolute values:
$$\text{Area} = \int_0^\pi \sin x\,dx + \left|\int_\pi^{2\pi}\sin x\,dx\right| = \big[-\cos x\big]_0^\pi + \left|\big[-\cos x\big]_\pi^{2\pi}\right| = (1-(-1)) + |{-1-1}| = 2+2=4. \qquad \blacksquare$$
(Direct check: $\int_0^{2\pi}\sin x\,dx = -\cos(2\pi)+\cos 0 = -1+1=0$ — the signed total, which is *not* the area — confirming why the split was necessary.)

---

**Example 7 (Uniqueness of the solution to an IVP-style antiderivative problem).** Find the unique function $H$ with $H'(x) = e^{\sin x}$ for all $x\in\mathbb{R}$ and $H(1) = -2$.

By the Key Fact on Page 1, with $x_0=1$, $y_0=-2$, $f(t)=e^{\sin t}$:
$$H(x) = -2 + \int_1^x e^{\sin t}\,dt.$$
This is the *only* function satisfying both conditions: any other antiderivative of $e^{\sin x}$ differs from $\int_1^x e^{\sin t}\,dt$ by a constant $C$, and demanding $H(1)=-2$ forces $C=-2$ exactly (since $\int_1^1 e^{\sin t}dt = 0$). Writing $H(x) = \int_0^x e^{\sin t}\,dt - 2$ instead would be **wrong** unless the extra constant happens to work out — check: at $x=1$ that expression gives $\int_0^1 e^{\sin t}dt - 2 \neq -2$ in general, so that guess fails the initial condition. $\blacksquare$

---

## Pages 4–5 — Practice Problems (unsolved)

**Antiderivatives & Indefinite Integrals**

1. Compute $\displaystyle\int \left(3x^8 - 18x^5+1\right)dx$ and $\displaystyle\int \sqrt[3]{x}\,dx$ by "guess and check."
2. Compute $\displaystyle\int \sec x\tan x\,dx$ and $\displaystyle\int \frac{1}{x+5}\,dx$.
3. Find the domain and derivative of $F(x) = \ln|3x|$, and confirm it is a valid antiderivative of $\dfrac1x$ on $x>0$ by identifying the corresponding constant $C$ in $\ln|x|+C$.

**Functions Defined by Integrals & FTC Part 1**

4. Which of these are *valid* ways to define a function $F(x)$ (i.e. the dummy variable and the free variable are used correctly)? (a) $F(x)=\displaystyle\int_0^x \dfrac{t}{1+t^8}\,dt$; (b) $F(x) = \displaystyle\int_0^x \dfrac{x}{1+t^8}\,dt$; (c) $F(x) = \displaystyle\int_3^0 \dfrac{t}{1+x^2+t^8}\,dt$.
5. Find $F'(x)$ for $F(x) = \displaystyle\int_5^x \cos(t^2)\,dt$.
6. Find $F'(x)$ for $F(x) = \displaystyle\int_x^{7} \sin^3(\sqrt t)\,dt$. (Careful with the variable in the *lower* limit.)
7. Find $F'(x)$ for $F(x) = \displaystyle\int_{\sin x}^{e^x} \dfrac{t}{1+t^8}\,dt$.
8. Let $G$ be an antiderivative of a continuous function $f$ with domain $\mathbb{R}$. Decide true or false, with a brief justification: (a) $G(x) = \int_0^x f(t)\,dt$ must hold. (b) There exists $C\in\mathbb{R}$ such that $G(x) = C + \int_0^x f(t)\,dt$.

**FTC Part 2 & Applications**

9. Evaluate $\displaystyle\int_0^1 \left(e^x+e^{-x}-\cos(2x)\right)dx$.
10. Evaluate $\displaystyle\int_{\pi/4}^{\pi/3}\sec^2x\,dx$.
11. Find the area of the bounded region enclosed between $y=x^2+3$ and $y=3x+1$.
12. Find the average value of $f(x) = 9-x^2$ on $[0,3]$, and find a value $c\in[0,3]$ where $f(c)$ equals that average value (Mean Value Theorem for Integrals).

---

## Answer Key & Misconception Notes (for tutor use — do not show student until after attempt)

| # | Answer | Common misconception |
|---|---|---|
| 1 | $\frac{3x^9}{9}-\frac{18x^6}{6}+x+C = \frac{x^9}{3}-3x^6+x+C$; $\int\sqrt[3]{x}\,dx=\int x^{1/3}dx=\frac{3}{4}x^{4/3}+C$ | Using the power rule on $x^{1/3}$ but writing the new exponent as $1/3-1=-2/3$ without flipping the sign correctly, or forgetting to invert-and-multiply by the reciprocal of the new exponent ($\frac{3}{4}$, not $\frac43$ inverted incorrectly). |
| 2 | $\int\sec x\tan x\,dx=\sec x+C$; $\int\frac{1}{x+5}dx=\ln\lvert x+5\rvert+C$ | Confusing $\sec x\tan x$'s antiderivative with $\tan x$'s (writing $\tan x + C$ instead of $\sec x+C$) — these are two different "guess and check" facts that get mixed up. |
| 3 | Domain $x>0$ (since $3x>0 \iff x>0$); $F'(x)=\frac{1}{3x}\cdot 3=\frac1x$; matches $\ln x+C$ with $C=\ln 3$, since $\ln(3x)=\ln 3+\ln x$ | Computing $\frac{d}{dx}\ln(3x)$ as $\frac13$ (forgetting the chain rule multiplies by the derivative of the *inside*, which is $3$, and the $3$s cancel to leave exactly $1/x$, not $1/(3x)$ or $1/3$). |
| 4 | (a) valid; (b) **not** valid — the free variable $x$ appears both as the upper limit and inside the integrand, which is not allowed; (c) **not** valid for two separate reasons: the limits are backwards-oriented as written to look like an antiderivative in $x$, and more importantly $x$ appears in the integrand while the integral is not with respect to $x$ — this is fine on its own (that's what makes it a function of $x$), so actually flag (c) as valid **only if** read as $F(x)=\int_3^0(\cdots)dt$, a legitimate (if unusually oriented) function of $x$ | Assuming that *any* appearance of the outer variable $x$ inside the integrand invalidates the definition — it doesn't, as long as $x$ is not *also* claiming to be the dummy variable of integration (that's specifically case (b)'s problem). |
| 5 | $F'(x)=\cos(x^2)$ | Adding an extra chain-rule factor when the upper limit is literally $x$ (not a function of $x$) — no extra multiplication is needed here, unlike Problems 6–7. |
| 6 | $F'(x) = -\sin^3(\sqrt x)\cdot\frac{1}{1}$, i.e. $F'(x)=-\sin^3(\sqrt x)$, using $F(x)=-\int_7^x\sin^3(\sqrt t)dt$ first to flip the limits, then differentiating (the "inside function" here is just $x$ itself, so no extra chain-rule factor beyond the sign flip) | Forgetting to flip the sign when the variable is in the *lower* limit, and reporting $F'(x)=\sin^3(\sqrt x)$ without the minus sign. |
| 7 | $F'(x) = \dfrac{e^x}{1+e^{8x}}\cdot e^x - \dfrac{\sin x}{1+\sin^8 x}\cdot\cos x$ | Only differentiating with respect to the upper limit and forgetting the lower limit is *also* a function of $x$ here — both limits need their own chain-rule term, with a minus sign on the lower-limit term. |
| 8 | (a) False — $G$ could be $\int_0^x f(t)dt + 5$ for instance, which is also an antiderivative but isn't equal to the bare integral unless $G(0)=0$; (b) True — this is exactly the "$+C$" fact, since both $G(x)$ and $\int_0^x f(t)dt$ are antiderivatives of $f$ on the single interval $\mathbb{R}$ | Believing that *every* antiderivative must be expressible with lower limit exactly $0$ — the constant $C$ can be realized using $\int_0^x f\,dt$ with any added constant, or equally well using $\int_{x_0}^x f\,dt$ for any other base point $x_0$; there's no canonical choice. |
| 9 | $\left[e^x-e^{-x}-\frac12\sin(2x)\right]_0^1 = \left(e-e^{-1}-\frac12\sin 2\right)-(1-1-0) = e-e^{-1}-\frac12\sin 2$ | Mis-antidifferentiating $e^{-x}$ as $e^{-x}$ instead of $-e^{-x}$ (sign error from the chain rule on the exponent $-x$), which flips the sign of that whole term in the final answer. |
| 10 | $[\tan x]_{\pi/4}^{\pi/3} = \tan(\pi/3)-\tan(\pi/4) = \sqrt3 - 1$ | Writing the antiderivative of $\sec^2x$ as $\sec x\tan x$ (confusing it with the derivative *of* $\sec x$) instead of $\tan x$. |
| 11 | Curves meet where $x^2+3=3x+1 \Rightarrow x^2-3x+2=0 \Rightarrow x=1,2$; on $[1,2]$ the line is on top, so Area $=\int_1^2\left[(3x+1)-(x^2+3)\right]dx = \int_1^2(-x^2+3x-2)dx = \left[-\frac{x^3}3+\frac{3x^2}2-2x\right]_1^2 = \frac16$ | Integrating $(x^2+3)-(3x+1)$ (top minus bottom reversed) without first checking which curve is actually larger on $[1,2]$, producing a negative "area." |
| 12 | Average $=\frac{1}{3-0}\int_0^3(9-x^2)dx = \frac13\left[9x-\frac{x^3}3\right]_0^3 = \frac13(27-9)=6$; solve $9-c^2=6 \Rightarrow c^2=3 \Rightarrow c=\sqrt3$ (taking the root in $[0,3]$) | Forgetting to divide by $b-a$ when computing the average value — reporting the bare integral $18$ as if it were the average, instead of $18/3=6$. |
