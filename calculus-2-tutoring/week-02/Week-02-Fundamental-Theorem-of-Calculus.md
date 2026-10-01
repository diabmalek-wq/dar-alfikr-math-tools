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

**Example 8 (Level: Foundational — FTC Part 2 with a polynomial).** Evaluate $\displaystyle\int_0^2 (3x^2-2x+1)\,dx$.

**Step 1.** Find an antiderivative term by term: $\displaystyle\int 3x^2\,dx = x^3$, $\displaystyle\int -2x\,dx = -x^2$, $\displaystyle\int 1\,dx = x$, giving $F(x)=x^3-x^2+x$ (check: $F'(x)=3x^2-2x+1$, matches the integrand $\checkmark$).

**Step 2.** By FTC Part 2, $\displaystyle\int_0^2(3x^2-2x+1)\,dx = F(2)-F(0)$.

**Step 3.** Compute the two endpoint values: $F(2) = 2^3-2^2+2 = 8-4+2=6$; $F(0)=0-0+0=0$.

**Step 4.** Subtract: $6-0=6$. $\blacksquare$

---

**Example 9 (Level: Intermediate — FTC Part 1, both limits are functions of $x$).** Find $F'(x)$ for $F(x)=\displaystyle\int_x^{x^3}\cos(t^2)\,dt$.

**Step 1.** Split the integral at a convenient constant, $t=0$, so each piece has one variable limit and one fixed limit:
$$F(x) = \int_x^0 \cos(t^2)\,dt + \int_0^{x^3}\cos(t^2)\,dt = -\int_0^x\cos(t^2)\,dt+\int_0^{x^3}\cos(t^2)\,dt.$$

**Step 2.** Differentiate the first piece using FTC Part 1 directly (upper limit is bare $x$), with $f(t)=\cos(t^2)$:
$$\frac{d}{dx}\left[-\int_0^x f(t)\,dt\right] = -f(x) = -\cos(x^2).$$

**Step 3.** Differentiate the second piece using the chain-rule extension, with $g(x)=x^3$, $g'(x)=3x^2$:
$$\frac{d}{dx}\left[\int_0^{x^3} f(t)\,dt\right] = f(g(x))\cdot g'(x) = \cos\!\big((x^3)^2\big)\cdot 3x^2 = 3x^2\cos(x^6).$$

**Step 4.** Add the two pieces: $F'(x) = 3x^2\cos(x^6) - \cos(x^2)$. $\blacksquare$

---

**Example 10 (Level: Challenge — FTC with a non-elementary integrand, both limits variable).** Find $F'(x)$ for $F(x) = \displaystyle\int_{\sin x}^{x^2} e^{t^2}\,dt$. (Note: $e^{t^2}$ has no elementary antiderivative — FTC Part 1 does not need one.)

**Step 1.** Split at $t=0$: $F(x) = -\displaystyle\int_0^{\sin x} e^{t^2}\,dt + \int_0^{x^2} e^{t^2}\,dt$, with $f(t)=e^{t^2}$.

**Step 2.** Differentiate the upper-limit piece, $g(x)=x^2$, $g'(x)=2x$:
$$\frac{d}{dx}\left[\int_0^{x^2} f(t)\,dt\right] = f(x^2)\cdot 2x = 2x\,e^{(x^2)^2} = 2x\,e^{x^4}.$$

**Step 3.** Differentiate the lower-limit piece, $h(x)=\sin x$, $h'(x)=\cos x$:
$$\frac{d}{dx}\left[-\int_0^{\sin x} f(t)\,dt\right] = -f(\sin x)\cdot\cos x = -\cos x\,e^{\sin^2 x}.$$

**Step 4.** Combine: $F'(x) = 2x\,e^{x^4} - \cos x\,e^{\sin^2 x}$. $\blacksquare$

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

**More Practice, Graded by Level**

13. *(Level: Foundational)* Evaluate $\displaystyle\int_{-1}^{1}(4x^3-3x^2)\,dx$.
14. *(Level: Intermediate)* Find $F'(x)$ for $F(x)=\displaystyle\int_1^{\ln x} t^2\,dt$ (for $x>0$).
15. *(Level: Challenge)* Find the average value of $f(x)=\sec^2x$ on $\left[0,\dfrac{\pi}{4}\right]$, and find the exact value $c$ in that interval where $f(c)$ equals the average (Mean Value Theorem for Integrals).

---

## Answer Key & Misconception Notes (for tutor use — do not show student until after attempt)

**Problem 1 — Answer.**

**Step 1.** Antidifferentiate $3x^8-18x^5+1$ term by term using the power rule $\int x^n dx=\frac{x^{n+1}}{n+1}$: $\int 3x^8dx=\frac{3x^9}{9}=\frac{x^9}{3}$; $\int -18x^5dx=-\frac{18x^6}{6}=-3x^6$; $\int 1\,dx=x$.

**Step 2.** Combine with a single constant: $\displaystyle\int(3x^8-18x^5+1)dx=\frac{x^9}{3}-3x^6+x+C$.

**Step 3.** For $\int\sqrt[3]{x}\,dx$, rewrite as $\int x^{1/3}dx$; add $1$ to the exponent: $\frac13+1=\frac43$.

**Step 4.** Divide by the new exponent, i.e. multiply by its reciprocal $\frac34$: $\int x^{1/3}dx=\frac34x^{4/3}+C$.

\textbf{\textcolor{cautionInk}{Common misconception:}} Using the power rule on $x^{1/3}$ but writing the new exponent as $1/3-1=-2/3$ without flipping the sign correctly, or forgetting to invert-and-multiply by the reciprocal of the new exponent ($\frac34$, not $\frac43$ inverted incorrectly).

**Problem 2 — Answer.**

**Step 1.** Recall from the derivative table that $\dfrac{d}{dx}[\sec x]=\sec x\tan x$; reversing this gives $\int\sec x\tan x\,dx=\sec x+C$.

**Step 2.** Recall $\dfrac{d}{dx}[\ln|x+5|]=\dfrac{1}{x+5}\cdot 1=\dfrac1{x+5}$ (chain rule, derivative of the inside $x+5$ is $1$); reversing gives $\int\dfrac{dx}{x+5}=\ln|x+5|+C$.

\textbf{\textcolor{cautionInk}{Common misconception:}} Confusing $\sec x\tan x$'s antiderivative with $\tan x$'s (writing $\tan x+C$ instead of $\sec x+C$) — these are two different "guess and check" facts that get mixed up.

**Problem 3 — Answer.**

**Step 1.** Domain: $F(x)=\ln|3x|$ requires $3x\neq 0$; restricting to $x>0$ (as the problem asks), $3x>0$ so $|3x|=3x$ and $F(x)=\ln(3x)$.

**Step 2.** Differentiate with the chain rule: $F'(x)=\dfrac{1}{3x}\cdot\dfrac{d}{dx}[3x]=\dfrac{1}{3x}\cdot 3=\dfrac1x$ — the factor of $3$ from the inside function cancels the $3$ in the denominator.

**Step 3.** Since $F'(x)=\dfrac1x$ on $x>0$, $F$ is indeed a valid antiderivative of $\dfrac1x$ there.

**Step 4.** Identify $C$: by the log law $\ln(3x)=\ln3+\ln x$, so $F(x)=\ln x+\ln3$ — matching the general form $\ln x+C$ with $C=\ln3$.

\textbf{\textcolor{cautionInk}{Common misconception:}} Computing $\frac{d}{dx}\ln(3x)$ as $\frac13$ (forgetting the chain rule multiplies by the derivative of the \textit{inside}, which is $3$, and the $3$s cancel to leave exactly $1/x$, not $1/(3x)$ or $1/3$).

**Problem 4 — Answer.**

**Step 1.** The rule to check in each case: the dummy (integration) variable — the one attached to the differential, e.g. $dt$ — must never be the same letter as the free/outer variable $x$; but $x$ is completely allowed to appear elsewhere (as the upper/lower limit, or as a plain parameter inside the integrand), since none of that conflicts with $t$ being the variable of integration.

**Step 2.** (a) $F(x)=\int_0^x\frac{t}{1+t^8}dt$: dummy variable is $t$, $x$ only appears as the upper limit. \textbf{Valid.}

**Step 3.** (b) $F(x)=\int_0^x\frac{x}{1+t^8}dt$: the differential is still $dt$, so $t$ is the dummy variable; $x$ appears as the upper limit \emph{and} as a constant-with-respect-to-$t$ factor in the integrand, which is perfectly fine — it simply means $F(x)=x\displaystyle\int_0^x\frac{dt}{1+t^8}$, a well-defined function of $x$. \textbf{Valid} (this corrects an earlier, over-cautious version of this key, which is why the misconception below is worth reading carefully).

**Step 4.** (c) $F(x)=\int_3^0\frac{t}{1+x^2+t^8}dt$: the differential is $dt$, so $t$ is again the dummy variable; the limits are fixed numbers ($3$ and $0$, not functions of $x$), and $x$ appears only as a parameter ($x^2$) inside the integrand. A "backwards" pair of constant limits is not a problem — it only contributes an overall minus sign, $\int_3^0(\cdots)dt=-\int_0^3(\cdots)dt$. \textbf{Valid.}

\textbf{\textcolor{cautionInk}{Common misconception:}} Assuming that \textit{any} appearance of the outer variable $x$ inside the integrand invalidates the definition. It doesn't — the only actual violation would be $x$ itself acting as the dummy variable, e.g. something like $\int_0^x\frac{x}{1+x^8}dx$, where the differential $dx$ collides with $x$ also being the limit. None of (a), (b), (c) do that, so all three are valid.

**Problem 5 — Answer.**

**Step 1.** The upper limit is bare $x$ (not a function of $x$), so FTC Part 1 applies directly with $f(t)=\cos(t^2)$: $F'(x)=f(x)=\cos(x^2)$.

\textbf{\textcolor{cautionInk}{Common misconception:}} Adding an extra chain-rule factor when the upper limit is literally $x$ — no extra multiplication is needed here, unlike Problems 6–7 where the limit is a genuine function of $x$.

**Problem 6 — Answer.**

**Step 1.** The variable is in the \textit{lower} limit, so first flip the integral to put it on top: $F(x)=\int_x^7\sin^3(\sqrt t)\,dt=-\int_7^x\sin^3(\sqrt t)\,dt$.

**Step 2.** Now the upper limit is bare $x$, so FTC Part 1 applies with $f(t)=\sin^3(\sqrt t)$: $\dfrac{d}{dx}\left[-\int_7^x f(t)dt\right]=-f(x)=-\sin^3(\sqrt x)$.

\textbf{\textcolor{cautionInk}{Common misconception:}} Forgetting to flip the sign when the variable is in the \textit{lower} limit, and reporting $F'(x)=\sin^3(\sqrt x)$ without the minus sign.

**Problem 7 — Answer.**

**Step 1.** Both limits depend on $x$, so split at a convenient constant, $t=0$, with $f(t)=\dfrac{t}{1+t^8}$: $F(x)=-\displaystyle\int_0^{\sin x}f(t)\,dt+\int_0^{e^x}f(t)\,dt$.

**Step 2.** Differentiate the upper-limit piece with $g(x)=e^x$, $g'(x)=e^x$: $\dfrac{d}{dx}\left[\int_0^{e^x}f\,dt\right]=f(e^x)\cdot e^x=\dfrac{e^x}{1+e^{8x}}\cdot e^x$.

**Step 3.** Differentiate the lower-limit piece with $h(x)=\sin x$, $h'(x)=\cos x$: $\dfrac{d}{dx}\left[-\int_0^{\sin x}f\,dt\right]=-f(\sin x)\cdot\cos x=-\dfrac{\sin x}{1+\sin^8x}\cdot\cos x$.

**Step 4.** Combine: $F'(x) = \dfrac{e^x}{1+e^{8x}}\cdot e^x - \dfrac{\sin x}{1+\sin^8 x}\cdot\cos x$.

\textbf{\textcolor{cautionInk}{Common misconception:}} Only differentiating with respect to the upper limit and forgetting the lower limit is \textit{also} a function of $x$ here — both limits need their own chain-rule term, with a minus sign on the lower-limit term.

**Problem 8 — Answer.**

**Step 1.** (a) Test with a counterexample: let $G(x)=\int_0^x f(t)dt+5$. Then $G'(x)=f(x)$ (so $G$ genuinely is an antiderivative of $f$), but $G(x)\neq\int_0^xf(t)dt$ unless the extra $5$ happens to be $0$. So the claim "$G(x)=\int_0^xf(t)dt$ must hold" is \textbf{False}.

**Step 2.** (b) This is exactly the "$+C$" fact from Page 1: both $G(x)$ and $\int_0^xf(t)dt$ are antiderivatives of $f$ on the single interval $\mathbb{R}$, so they differ by a constant. \textbf{True.}

\textbf{\textcolor{cautionInk}{Common misconception:}} Believing that \textit{every} antiderivative must be expressible with lower limit exactly $0$ — the constant $C$ can equally well be realized using $\int_{x_0}^xf\,dt$ for any other base point $x_0$; there is no canonical choice.

**Problem 9 — Answer.**

**Step 1.** Find an antiderivative term by term: $\int e^x dx=e^x$; $\int e^{-x}dx=-e^{-x}$ (chain rule on the exponent $-x$); $\int-\cos(2x)dx=-\frac12\sin(2x)$ (check: $\frac{d}{dx}[-\frac12\sin2x]=-\cos2x$ $\checkmark$). So $F(x)=e^x-e^{-x}-\frac12\sin(2x)$.

**Step 2.** Apply FTC Part 2: $\displaystyle\int_0^1(e^x+e^{-x}-\cos2x)dx=F(1)-F(0)$.

**Step 3.** $F(1)=e-e^{-1}-\frac12\sin2$; $F(0)=1-1-\frac12\sin0=0$.

**Step 4.** Subtract: $F(1)-F(0)=e-e^{-1}-\frac12\sin2$.

\textbf{\textcolor{cautionInk}{Common misconception:}} Mis-antidifferentiating $e^{-x}$ as $e^{-x}$ instead of $-e^{-x}$ (a sign error from the chain rule on the exponent $-x$), which flips the sign of that whole term in the final answer.

**Problem 10 — Answer.**

**Step 1.** Use the row $\sec^2x\to\tan x$ from the derivative table (never $\sec x\tan x$, which is the derivative \textit{of} $\sec x$, not its antiderivative): $\int\sec^2x\,dx=\tan x+C$.

**Step 2.** Evaluate: $[\tan x]_{\pi/4}^{\pi/3}=\tan(\pi/3)-\tan(\pi/4)=\sqrt3-1$.

\textbf{\textcolor{cautionInk}{Common misconception:}} Writing the antiderivative of $\sec^2x$ as $\sec x\tan x$ (confusing it with the derivative \textit{of} $\sec x$) instead of $\tan x$.

**Problem 11 — Answer.**

**Step 1.** Find where the curves meet: $x^2+3=3x+1\Rightarrow x^2-3x+2=0\Rightarrow(x-1)(x-2)=0\Rightarrow x=1,2$.

**Step 2.** Decide which curve is on top on $[1,2]$ by testing $x=1.5$: line gives $3(1.5)+1=5.5$; parabola gives $1.5^2+3=5.25$. The line is larger, so the line is on top.

**Step 3.** Set up the area integral, top minus bottom: $\text{Area}=\displaystyle\int_1^2\left[(3x+1)-(x^2+3)\right]dx=\int_1^2(-x^2+3x-2)dx$.

**Step 4.** Antidifferentiate and evaluate: $\left[-\frac{x^3}3+\frac{3x^2}2-2x\right]_1^2$. At $x=2$: $-\frac83+6-4=-\frac23$. At $x=1$: $-\frac13+\frac32-2=-\frac56$.

**Step 5.** Subtract: $-\frac23-\left(-\frac56\right)=-\frac46+\frac56=\frac16$.

\textbf{\textcolor{cautionInk}{Common misconception:}} Integrating $(x^2+3)-(3x+1)$ (top minus bottom reversed) without first checking which curve is actually larger on $[1,2]$, producing a negative "area."

**Problem 12 — Answer.**

**Step 1.** Average value formula: $\text{avg}=\dfrac{1}{b-a}\displaystyle\int_a^bf(x)dx=\dfrac{1}{3-0}\int_0^3(9-x^2)dx$.

**Step 2.** Antidifferentiate and evaluate: $\dfrac13\left[9x-\dfrac{x^3}3\right]_0^3=\dfrac13\big[(27-9)-0\big]=\dfrac13(18)=6$.

**Step 3.** Solve $f(c)=6$: $9-c^2=6\Rightarrow c^2=3\Rightarrow c=\pm\sqrt3$; only $c=\sqrt3$ lies in $[0,3]$.

\textbf{\textcolor{cautionInk}{Common misconception:}} Forgetting to divide by $b-a$ when computing the average value — reporting the bare integral $18$ as if it were the average, instead of $18/3=6$.

**Problem 13 — Answer.**

**Step 1.** Antidifferentiate term by term: $\int4x^3dx=x^4$; $\int-3x^2dx=-x^3$, giving $F(x)=x^4-x^3$.

**Step 2.** Evaluate at the endpoints: $F(1)=1^4-1^3=1-1=0$; $F(-1)=(-1)^4-(-1)^3=1-(-1)=2$.

**Step 3.** Apply FTC Part 2: $\displaystyle\int_{-1}^1(4x^3-3x^2)dx=F(1)-F(-1)=0-2=-2$.

\textbf{\textcolor{cautionInk}{Common misconception:}} Treating $(-1)^3$ as $+1$ instead of $-1$ when evaluating $F(-1)$ — an odd-power sign error that silently turns a subtraction into an addition.

**Problem 14 — Answer.**

**Step 1.** The upper limit is $g(x)=\ln x$, a genuine function of $x$ (not bare $x$), so use the chain-rule extension of FTC Part 1 with $f(t)=t^2$: $F'(x)=f(g(x))\cdot g'(x)$.

**Step 2.** Compute the two pieces: $f(g(x))=f(\ln x)=(\ln x)^2$; $g'(x)=\dfrac{d}{dx}[\ln x]=\dfrac1x$.

**Step 3.** Multiply: $F'(x)=(\ln x)^2\cdot\dfrac1x=\dfrac{(\ln x)^2}{x}$.

\textbf{\textcolor{cautionInk}{Common misconception:}} Treating $\ln x$ in the upper limit like the "bare $x$" case (Problem 5) and skipping the extra factor of $g'(x)=1/x$ that the chain rule requires whenever the limit is a function of $x$ rather than $x$ itself.

**Problem 15 — Answer.**

**Step 1.** Average value: $\text{avg}=\dfrac{1}{\pi/4-0}\displaystyle\int_0^{\pi/4}\sec^2x\,dx=\dfrac4\pi\big[\tan x\big]_0^{\pi/4}=\dfrac4\pi(1-0)=\dfrac4\pi$.

**Step 2.** Set up the MVT equation: solve $\sec^2c=\dfrac4\pi$ for $c\in\left[0,\dfrac\pi4\right]$.

**Step 3.** Rewrite in cosine: $\sec^2c=\dfrac4\pi\iff\cos^2c=\dfrac\pi4\iff\cos c=\dfrac{\sqrt\pi}2$ (taking the positive root, since $c\in\left[0,\frac\pi4\right]$ means $\cos c>0$).

**Step 4.** So $c=\arccos\!\left(\dfrac{\sqrt\pi}2\right)\approx\arccos(0.886)\approx0.482$ radians — and this does lie inside $\left[0,\frac\pi4\right]\approx[0,0.785]$, confirming the Mean Value Theorem for Integrals.

\textbf{\textcolor{cautionInk}{Common misconception:}} Solving $\sec^2c=4/\pi$ by taking $c=\text{arcsec}(\sqrt{4/\pi})$ directly without first converting to $\cos c$, which is much easier to invert exactly here — or forgetting to check that the resulting $c$ actually lies inside the given interval.
