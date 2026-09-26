# Week 3 — Integration Methods

**Session length:** 3 hours
**Source:** OpenStax, *Calculus Volume 2*, §3.1 (Integration by Parts), §3.2 (Trigonometric Integrals), §3.4 (Partial Fractions); paired with MAT137 (Calculus with Proofs) Unit 9 lecture-slide prompts on substitution, parts, trig-function products, and rational functions — MAT137 is the University of Toronto's official exclusion-equivalent of MATA37H3

---

## Page 1 — Introduction, Key Facts & Definitions

### Recap and orientation

FTC (Unit 8) reduced every definite integral to "find an antiderivative, then subtract endpoint values." This unit builds a toolkit of four techniques for actually *finding* antiderivatives when the integrand isn't already a basic form: **substitution** (undoing the chain rule), **integration by parts** (undoing the product rule), **trigonometric-integral identities** (for products/powers of $\sin,\cos,\sec,\tan$), and **partial fractions** (for rational functions). Recognizing *which* technique a given integral calls for is itself a skill this unit builds.

### Why this matters

Nearly every integral on a MATA37/MAT137-style exam is designed to test whether you can correctly *identify* the technique, not just execute it — a $\sec^n x\tan^m x$ integral with the wrong parity choice, or a partial-fraction integral where you forget to long-divide first when the numerator's degree isn't smaller, are the classic traps. Units 12 (improper integrals) and 13–14 (series/power series) all assume fluency with these techniques.

### Key Fact: Integration by Substitution (Undoing the Chain Rule) (MAT137 Unit 9)

If $F$ is an antiderivative of $f$, then $\dfrac{d}{dx}\big[F(g(x))\big] = f(g(x))g'(x)$ by the chain rule, so
$$\int f(g(x))\,g'(x)\,dx = F(g(x)) + C.$$
In practice: pick $u = g(x)$ (the "inside function"), compute $du = g'(x)\,dx$, and rewrite the whole integral in terms of $u$ only — if any leftover $x$'s remain after substituting, the wrong $u$ was chosen (or the integral needs a different technique entirely).

### Key Fact: Substitution in a Definite Integral (MAT137 Unit 9)

When evaluating $\int_a^b f(g(x))g'(x)\,dx$ by substitution $u=g(x)$, the **limits of integration must also change**, to $u=g(a)$ and $u=g(b)$:
$$\int_a^b f(g(x))\,g'(x)\,dx = \int_{g(a)}^{g(b)} f(u)\,du.$$
A common but invalid shortcut is to substitute $u=g(x)$ throughout the integrand while leaving the limits as the original $x$-values — this produces a numeric answer that is often coincidentally close but is not justified by the change-of-variables theorem, and the *evaluation* step (plugging in numbers) must use whichever variable's limits you are currently using.

### Theorem: Integration by Parts (OpenStax §3.1, Theorem 3.1)

If $u=f(x)$ and $v=g(x)$ have continuous derivatives, then
$$\int u\,dv = uv - \int v\,du.$$
This comes directly from integrating the product rule $\big(f(x)g(x)\big)' = f'(x)g(x)+f(x)g'(x)$. Use it when the integrand is a **product** of two functions where one part becomes simpler when differentiated (choose that part as $u$) and the other part is easy to integrate (that part is $dv$). A common mnemonic for choosing $u$ is **LIATE** (Logarithmic, Inverse trig, Algebraic, Trigonometric, Exponential — earlier in the list is generally the better choice of $u$).

### Key Fact: Repeated / Tabular Integration by Parts (MAT137 Unit 9)

When the "algebraic" factor is a polynomial of degree $n\geq 2$ (e.g. $\int x^2 e^{-x}dx$), integration by parts must be applied **repeatedly**, each time differentiating the polynomial part further, until it reaches degree $0$. When the pattern instead **cycles back to the original integral** (as with $\int e^{ax}\sin(bx)\,dx$, where two rounds of parts return a multiple of the same integral), solve for the original integral algebraically rather than trying to apply parts a third time.

### Key Fact: Powers of $\sin x$ and $\cos x$ (OpenStax §3.2)

To integrate $\int \sin^n x\cos^m x\,dx$:
- If **either** exponent is **odd**, peel off one copy of that function, convert the remaining even power using $\sin^2x+\cos^2x=1$, and substitute $u=$ (the other function). E.g. for odd $m$: write $\cos^m x = \cos^{m-1}x\cos x$, convert $\cos^{m-1}x$ (even power) via $\cos^2x = 1-\sin^2x$, then let $u=\sin x$.
- If **both** exponents are **even**, use the half-angle identities $\sin^2x = \dfrac{1-\cos(2x)}{2}$ and $\cos^2x=\dfrac{1+\cos(2x)}{2}$ to reduce the powers before integrating (possibly needing to repeat).

### Key Fact: Powers of $\sec x$ and $\tan x$ (OpenStax §3.2; MAT137 Unit 9)

To integrate $\int \sec^n x\tan^m x\,dx$, use $\dfrac{d}{dx}[\tan x]=\sec^2x$, $\dfrac{d}{dx}[\sec x]=\sec x\tan x$, and the identity $\tan^2x+1=\sec^2x$:
- If $n$ (the power of secant) is **even**, peel off $\sec^2x$, convert the rest of the secant power to tangents via $\sec^2x=1+\tan^2x$, and substitute $u=\tan x$.
- If $m$ (the power of tangent) is **odd**, peel off one $\sec x\tan x$, convert the remaining even tangent power to secants via $\tan^2x=\sec^2x-1$, and substitute $u=\sec x$.
- The lone integrals $\int\sec x\,dx = \ln|\sec x+\tan x|+C$ and $\int\csc x\,dx = -\ln|\csc x+\cot x|+C$ don't fit either pattern above and must be memorized (or re-derived via the "multiply by $\frac{\sec x+\tan x}{\sec x+\tan x}$" trick).

### Definition: Partial Fraction Decomposition (OpenStax §3.4)

A rational function $\dfrac{P(x)}{Q(x)}$ can be decomposed into a sum of simpler fractions **only when** $\deg P < \deg Q$. If $\deg P \geq \deg Q$, **long divide first**: $\dfrac{P(x)}{Q(x)} = A(x) + \dfrac{R(x)}{Q(x)}$ with $\deg R < \deg Q$, and only then decompose $\dfrac{R(x)}{Q(x)}$. The decomposition's *shape* is determined by factoring $Q(x)$:
- A **distinct linear factor** $(x-a)$ contributes a term $\dfrac{A}{x-a}$.
- A **repeated linear factor** $(x-a)^k$ contributes $\dfrac{A_1}{x-a}+\dfrac{A_2}{(x-a)^2}+\cdots+\dfrac{A_k}{(x-a)^k}$ — one term for *every* power from $1$ to $k$, not just the highest.
- An **irreducible quadratic factor** contributes a term of the form $\dfrac{Ax+B}{x^2+px+q}$ (linear numerator, not just a constant).

Once decomposed, each piece integrates using $\int\frac{du}{u}=\ln|u|+C$ (linear factors), the power rule (repeated factors), or $\int\frac{du}{u^2+a^2}=\frac1a\arctan\left(\frac ua\right)+C$ (irreducible quadratics).

---

## Pages 2–3 — Solved Examples

**Example 1 (Basic substitution).** Evaluate $\displaystyle\int \frac{\sin\sqrt x}{\sqrt x}\,dx$.

Let $u=\sqrt x = x^{1/2}$, so $du = \dfrac{1}{2\sqrt x}dx$, i.e. $\dfrac{dx}{\sqrt x} = 2\,du$. Then
$$\int \frac{\sin\sqrt x}{\sqrt x}\,dx = \int \sin u \cdot 2\,du = -2\cos u + C = -2\cos\sqrt x + C. \qquad \blacksquare$$

---

**Example 2 (Substitution in a definite integral — done correctly).** Evaluate $\displaystyle I=\int_0^2 \sqrt{x^3+1}\,x^2\,dx$.

Let $u = x^3+1$, so $du = 3x^2\,dx$, i.e. $x^2dx = \frac13 du$. **Changing the limits**: when $x=0$, $u=1$; when $x=2$, $u=9$. So
$$I = \int_1^9 \sqrt u \cdot\frac13\,du = \frac13\cdot\frac23 u^{3/2}\Big|_1^9 = \frac29\left(9^{3/2}-1^{3/2}\right) = \frac29(27-1) = \frac{52}{9}.$$
Note that the limits were changed to $u$-values ($1$ and $9$), not left as $0$ and $2$ — mixing the new integrand with the old limits would be evaluating the wrong quantity, even though (as this example shows) converting back to $x$ before plugging in numbers gives the same correct final answer either way, as long as it's done consistently. $\blacksquare$

---

**Example 3 (Integration by parts, single application).** Evaluate $\displaystyle\int x\,e^{-2x}\,dx$.

Choose $u=x$ (gets simpler when differentiated), $dv = e^{-2x}dx$. Then $du = dx$, $v = -\frac12 e^{-2x}$.
$$\int x e^{-2x}dx = uv - \int v\,du = -\frac{x}{2}e^{-2x} - \int\left(-\frac12 e^{-2x}\right)dx = -\frac x2 e^{-2x} + \frac12\int e^{-2x}dx = -\frac x2 e^{-2x} - \frac14 e^{-2x} + C. \qquad \blacksquare$$

---

**Example 4 (Repeated integration by parts).** Evaluate $\displaystyle\int x^2 \sin x\,dx$.

First round: $u=x^2$, $dv=\sin x\,dx \Rightarrow du=2x\,dx$, $v=-\cos x$:
$$\int x^2\sin x\,dx = -x^2\cos x + \int 2x\cos x\,dx.$$
Second round on $\int 2x\cos x\,dx$: $u=2x$, $dv=\cos x\,dx \Rightarrow du=2\,dx$, $v=\sin x$:
$$\int 2x\cos x\,dx = 2x\sin x - \int 2\sin x\,dx = 2x\sin x + 2\cos x + C.$$
Combining, $\displaystyle\int x^2\sin x\,dx = -x^2\cos x + 2x\sin x + 2\cos x + C$. $\blacksquare$

---

**Example 5 (The "solve for the integral" trick).** Evaluate $\displaystyle I=\int e^{x}\sin x\,dx$.

Round 1: $u=e^x$, $dv=\sin x\,dx \Rightarrow du=e^x dx$, $v=-\cos x$:
$$I = -e^x\cos x + \int e^x\cos x\,dx.$$
Round 2, on $\int e^x\cos x\,dx$: $u=e^x$, $dv=\cos x\,dx \Rightarrow du=e^xdx$, $v=\sin x$:
$$\int e^x\cos x\,dx = e^x\sin x - \int e^x\sin x\,dx = e^x\sin x - I.$$
Substituting back: $I = -e^x\cos x + e^x\sin x - I$, so $2I = e^x(\sin x - \cos x)$, giving
$$I = \int e^x\sin x\,dx = \frac{e^x(\sin x-\cos x)}{2} + C.$$
This is the key move: when the second round of parts reproduces the *original* integral $I$ (rather than something new), solve the resulting equation for $I$ algebraically instead of continuing to integrate by parts forever. $\blacksquare$

---

**Example 6 (Odd power of sine — trig integral).** Evaluate $\displaystyle\int \sin^3 x\cos^2 x\,dx$.

The power of $\sin x$ is odd, so peel off one factor: $\sin^3x = \sin^2x\cdot\sin x = (1-\cos^2x)\sin x$. Substituting $u=\cos x$, $du=-\sin x\,dx$:
$$\int(1-\cos^2x)\cos^2x\sin x\,dx = -\int(1-u^2)u^2\,du = -\int(u^2-u^4)\,du = -\frac{u^3}{3}+\frac{u^5}{5}+C = -\frac{\cos^3x}{3}+\frac{\cos^5x}{5}+C. \qquad\blacksquare$$

---

**Example 7 (Both powers even — half-angle identities).** Evaluate $\displaystyle\int \cos^2 x\,dx$.

Both the "powers" here are even ($\cos^2x\sin^0x$), so use $\cos^2x = \dfrac{1+\cos(2x)}{2}$:
$$\int\cos^2x\,dx = \int\frac{1+\cos(2x)}{2}\,dx = \frac{x}{2} + \frac{\sin(2x)}{4} + C. \qquad \blacksquare$$

---

**Example 8 (Odd power of tangent — sec/tan integral).** Evaluate $\displaystyle\int \sec^4x\tan^3x\,dx$.

The power of tangent ($3$) is odd, so peel off one $\sec x\tan x$ and convert the rest of the tangent power using $\tan^2x=\sec^2x-1$: $\tan^3x = \tan^2x\cdot\tan x = (\sec^2x-1)\tan x$, so the integral is $\int\sec^3x(\sec^2x-1)\cdot(\sec x\tan x)\,dx$. Substituting $u=\sec x$, $du=\sec x\tan x\,dx$:
$$\int u^3(u^2-1)\,du = \int(u^5-u^3)\,du = \frac{u^6}{6}-\frac{u^4}{4}+C = \frac{\sec^6x}{6}-\frac{\sec^4x}{4}+C. \qquad \blacksquare$$

---

**Example 9 (Partial fractions — distinct linear factors, with long division).** Evaluate $\displaystyle\int \frac{x^2+3x+5}{x+1}\,dx$.

Since $\deg(\text{numerator}) = 2 \geq 1 = \deg(\text{denominator})$, long-divide first: $x^2+3x+5 = (x+1)(x+2) + 3$, so
$$\frac{x^2+3x+5}{x+1} = x+2+\frac{3}{x+1}.$$
Now integrate term by term:
$$\int\left(x+2+\frac{3}{x+1}\right)dx = \frac{x^2}{2}+2x+3\ln|x+1|+C. \qquad \blacksquare$$

---

**Example 10 (Partial fractions — repeated linear factor).** Evaluate $\displaystyle\int \frac{2x+6}{(x+1)^2}\,dx$.

Set up $\dfrac{2x+6}{(x+1)^2} = \dfrac{A}{x+1}+\dfrac{B}{(x+1)^2}$ — **two** terms since the factor is repeated. Clearing denominators: $2x+6 = A(x+1)+B$. Matching coefficients: $A=2$ (coefficient of $x$), and $A+B=6 \Rightarrow B=4$. So
$$\int\left(\frac{2}{x+1}+\frac{4}{(x+1)^2}\right)dx = 2\ln|x+1| - \frac{4}{x+1}+C. \qquad \blacksquare$$

---

## Pages 4–5 — Practice Problems (unsolved)

**Substitution**

1. Evaluate $\displaystyle\int e^x\cos(e^x)\,dx$.
2. Evaluate $\displaystyle\int \cot x\,dx$. (Hint: rewrite as $\dfrac{\cos x}{\sin x}$.)
3. Evaluate $\displaystyle\int_0^1 x e^{-x^2}\,dx$, carefully converting the limits of integration.
4. The following write-up contains an error even though its final numeric answer happens to be correct: "$\displaystyle\int_0^2\sqrt{x^3+1}\,x^2\,dx$: let $u=x^3+1$, $du=3x^2dx$; $=\frac13\int_0^2\sqrt u\,du = \frac29 u^{3/2}\Big|_0^2$." Identify the specific error.

**Integration by Parts**

5. Evaluate $\displaystyle\int \ln x\,dx$. (Hint: treat this as $\int 1\cdot\ln x\,dx$ and choose $u=\ln x$.)
6. Evaluate $\displaystyle\int x\arctan x\,dx$.
7. Evaluate $\displaystyle\int e^{ax}\cos(bx)\,dx$ (constants $a,b\neq0$), using the "solve for the integral" trick from Worked Example 5.
8. Estimate $\displaystyle\int_0^1 f'(x)\,dx$ and $\displaystyle\int_0^3 xf'(x)\,dx$ from a graph where $f$ is a smooth increasing convex function with $f(0)=2$, $f(1)=3$, $f(3)\approx 4.7$ (using $\int_0^1 f'(x)dx = f(1)-f(0)$ via FTC Part 2, and integration by parts on the second one).

**Trigonometric Integrals**

9. Evaluate $\displaystyle\int \sin^{10}x\cos x\,dx$ and $\displaystyle\int\sin^{10}x\cos^7x\,dx$ (identify which technique each needs).
10. Evaluate $\displaystyle\int \cos^4x\,dx$ (both powers are even — this will need the half-angle identity applied *twice*).
11. State which substitution ($u=\tan x$ or $u=\sec x$) is appropriate for $\displaystyle\int\sec^5x\tan^3x\,dx$, and explain why using the Key Fact on Page 1, then evaluate it.

**Partial Fractions**

12. Evaluate $\displaystyle\int \frac{1}{x^2+3x}\,dx$ and $\displaystyle\int\frac{1}{x^3-x}\,dx$, first factoring each denominator completely.

---

## Answer Key & Misconception Notes (for tutor use — do not show student until after attempt)

| # | Answer | Common misconception |
|---|---|---|
| 1 | $\sin(e^x)+C$ | Forgetting that $d(e^x)=e^x dx$ exactly matches the leftover factor — trying an unnecessary second substitution instead of recognizing the integral is already complete after $u=e^x$. |
| 2 | $u=\sin x$, $du=\cos x\,dx$: $\int\cot x\,dx = \int\frac{\cos x}{\sin x}dx = \ln\lvert\sin x\rvert+C$ | Confusing $\cot x$'s antiderivative with $\tan x$'s ($-\ln\lvert\cos x\rvert+C$) — these are mirror images and easy to swap. |
| 3 | $u=-x^2$ style: with $u=x^2$, $du=2x\,dx$; limits $x=0\to u=0$, $x=1\to u=1$: $\int_0^1 e^{-x^2}x\,dx = \frac12\int_0^1 e^{-u}du \cdot(-1)$... careful: $du=2xdx \Rightarrow x\,dx=\frac12 du$ and the exponent becomes $e^{-u}$: $=\frac12\left[-e^{-u}\right]_0^1 = \frac12(1-e^{-1})$ | Forgetting to convert the limits from $x$-values to $u$-values, and instead plugging the original $x=0,1$ bounds into the antiderivative written in terms of $u$. |
| 4 | The error: the limits $0,2$ were never converted to $u$-values (should be $u=1$ to $u=9$, since $x=0\Rightarrow u=1$, not $u=0$); it "worked out" only because a matching second error (leaving the antiderivative in terms of $u$ but evaluating at the wrong bounds) is not actually present in a way that cancels — in fact this write-up is simply wrong and would give $\frac29(2^{3/2}-0)=\frac{2^{5/2}}{9}$, a **different, incorrect** value from Worked Example 2's true answer $\frac{52}{9}$ | Assuming that because a substitution technically "worked" once in a similar-looking example, skipping the limit-conversion step is a safe shortcut — it is not, and only coincidentally avoids trouble in some (not all) cases. |
| 5 | $u=\ln x$, $dv=dx \Rightarrow du=\frac1x dx$, $v=x$: $\int\ln x\,dx = x\ln x - \int x\cdot\frac1x dx = x\ln x - x + C$ | Trying to pick $dv=\ln x\,dx$ (which cannot be directly integrated) instead of recognizing $\ln x$ itself must be the $u$ here, since there is no other factor to differentiate. |
| 6 | $u=\arctan x$, $dv=x\,dx \Rightarrow du=\frac{1}{1+x^2}dx$, $v=\frac{x^2}{2}$: $\int x\arctan x\,dx = \frac{x^2}{2}\arctan x - \int\frac{x^2}{2(1+x^2)}dx = \frac{x^2}2\arctan x - \frac12\int\left(1-\frac{1}{1+x^2}\right)dx = \frac{x^2}2\arctan x - \frac x2+\frac12\arctan x+C$ | Leaving $\int\frac{x^2}{1+x^2}dx$ unsimplified instead of rewriting $\frac{x^2}{1+x^2}=1-\frac{1}{1+x^2}$ (dividing out), getting stuck on an integral that looks like it needs partial fractions but is actually a simple rewrite. |
| 7 | $\dfrac{e^{ax}(a\cos(bx)+b\sin(bx))}{a^2+b^2}+C$ (via the same "solve for $I$" method as Worked Example 5, generalized with constants $a,b$) | Applying integration by parts correctly for two rounds but then trying a third round instead of recognizing the original integral has reappeared and can be solved for algebraically. |
| 8 | $\int_0^1 f'(x)dx = f(1)-f(0)=1$ by FTC Part 2; $\int_0^3 xf'(x)dx$ needs parts with $u=x, dv=f'(x)dx \Rightarrow v=f(x)$: $=\big[xf(x)\big]_0^3-\int_0^3 f(x)dx = 3f(3)-0-\int_0^3f(x)dx \approx 3(4.7)-\int_0^3f(x)dx$, requiring an area estimate under $f$ from the graph | Trying to estimate $\int_0^3 xf'(x)\,dx$ directly from the graph of $f$ (not $f'$) without recognizing integration by parts converts it into a combination of an endpoint evaluation and $\int f(x)dx$, which the graph of $f$ itself can estimate. |
| 9 | $\int\sin^{10}x\cos x\,dx$: substitution $u=\sin x$ works directly since $\cos x\,dx=du$: $=\frac{\sin^{11}x}{11}+C$; $\int\sin^{10}x\cos^7x\,dx$: cosine's power (7) is odd, so peel one off and convert the rest via $\cos^6x=(1-\sin^2x)^3$, then $u=\sin x$ | Trying to use $u=\sin x$ directly on the second integral without first peeling off a $\cos x$ factor to match — $\cos^7x\,dx$ does not equal $du$ for $u=\sin x$ on its own, only $\cos x\,dx$ does. |
| 10 | $\cos^4x=(\cos^2x)^2=\left(\frac{1+\cos2x}{2}\right)^2=\frac{1+2\cos2x+\cos^22x}{4}$, then apply the half-angle identity again to $\cos^22x=\frac{1+\cos4x}{2}$: integrating gives $\frac{3x}{8}+\frac{\sin2x}{4}+\frac{\sin4x}{32}+C$ | Applying the half-angle identity once and stopping, leaving a $\cos^22x$ term unintegrated (forgetting that squaring the half-angle substitution reintroduces another even power that itself needs the identity). |
| 11 | Neither exponent alone fits the "even secant" or "odd tangent" pattern cleanly at first glance since $n=5$ is odd and $m=3$ is odd — but $m=3$ (tangent) is odd, so the **odd-tangent** rule applies: peel off $\sec x\tan x$, convert $\tan^2x=\sec^2x-1$, substitute $u=\sec x$: $\int\sec^4x(\sec^2x-1)\sec x\tan x\,dx = \int u^4(u^2-1)du = \frac{u^7}{7}-\frac{u^5}{5}+C=\frac{\sec^7x}{7}-\frac{\sec^5x}{5}+C$ | Checking only whether $n$ (secant's power) is even and concluding neither rule applies when $n$ is odd — but the odd-tangent rule only needs $m$ (tangent's power) to be odd, independent of whether $n$ is even or odd. |
| 12 | $\frac{1}{x^2+3x}=\frac{1}{x(x+3)}=\frac{A}{x}+\frac{B}{x+3}$ with $A=\frac13,B=-\frac13$: integral $=\frac13\ln\lvert x\rvert-\frac13\ln\lvert x+3\rvert+C$; $\frac{1}{x^3-x}=\frac{1}{x(x-1)(x+1)}=\frac{A}{x}+\frac{B}{x-1}+\frac{C}{x+1}$ with $A=-1,B=\frac12,C=\frac12$: integral $=-\ln\lvert x\rvert+\frac12\ln\lvert x-1\rvert+\frac12\ln\lvert x+1\rvert+C$ | Factoring $x^3-x$ as $x(x^2-1)$ and stopping there, setting up only two partial-fraction terms ($\frac{A}{x}+\frac{Bx+C}{x^2-1}$) instead of recognizing $x^2-1=(x-1)(x+1)$ factors further into two distinct linear factors, each needing its own term. |
