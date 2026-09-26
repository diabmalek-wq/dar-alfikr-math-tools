# Week 4 — Integration Techniques II: Trigonometric Integrals, Partial Fractions & the Weierstrass Substitution

**Session length:** 3 hours
**Source:** OpenStax, *Calculus Volume 2*, §3.2 (Trigonometric Integrals), §3.4 (Partial Fractions); paired with MAT137 (Calculus with Proofs) Unit 9 lecture-slide prompts on trig-function products and rational functions, and Evan Dummit's *Calculus II (Part 1): Techniques of Integration* lecture notes (the Weierstrass substitution) — MAT137 is the University of Toronto's official exclusion-equivalent of MATA37H3

---

## Page 1 — Introduction, Key Facts & Definitions

### Recap and orientation

Last week covered substitution and integration by parts. This week finishes the integration-techniques toolkit with **trigonometric-integral identities** (for products/powers of $\sin,\cos,\sec,\tan$), **partial fractions** (for rational functions), and one powerful "universal" technique — the **Weierstrass substitution** — that converts *any* rational function of $\sin x$ and $\cos x$ into an ordinary rational function of $t$, solvable by partial fractions.

### Why this matters

A $\sec^n x\tan^m x$ integral with the wrong parity choice, or a partial-fraction integral where you forget to long-divide first when the numerator's degree isn't smaller, are classic exam traps. The Weierstrass substitution is the technique to reach for when no other pattern applies — it always works, though it isn't always the fastest. Units on improper integrals and series (Weeks 5–14) all assume fluency with this full toolkit.

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

### Key Fact: The Weierstrass Substitution — a "Universal" Rational-Trig Technique (Dummit)

For an integral whose integrand is a rational function of $\sin x$ and $\cos x$ (i.e. built only from $\sin x$, $\cos x$, and arithmetic — no other functions), the substitution
$$t = \tan\!\left(\frac{x}{2}\right)$$
converts the *entire* integrand into an ordinary rational function of $t$, via
$$\sin x = \frac{2t}{1+t^2}, \qquad \cos x = \frac{1-t^2}{1+t^2}, \qquad dx = \frac{2\,dt}{1+t^2}.$$
The resulting integral in $t$ is always solvable by partial fractions. This technique is a **fallback**: it always works on rational-trig integrands, but it is not always the fastest route (Worked Example 6 below solves the same integral both ways for comparison). Reach for it when no other pattern — odd power, even power, sec/tan parity — applies cleanly.

---

## Pages 2–3 — Solved Examples

**Example 1 (Odd power of sine — trig integral).** Evaluate $\displaystyle\int \sin^3 x\cos^2 x\,dx$.

The power of $\sin x$ is odd, so peel off one factor: $\sin^3x = \sin^2x\cdot\sin x = (1-\cos^2x)\sin x$. Substituting $u=\cos x$, $du=-\sin x\,dx$:
$$\int(1-\cos^2x)\cos^2x\sin x\,dx = -\int(1-u^2)u^2\,du = -\int(u^2-u^4)\,du = -\frac{u^3}{3}+\frac{u^5}{5}+C = -\frac{\cos^3x}{3}+\frac{\cos^5x}{5}+C. \qquad\blacksquare$$

---

**Example 2 (Both powers even — half-angle identities).** Evaluate $\displaystyle\int \cos^2 x\,dx$.

Both the "powers" here are even ($\cos^2x\sin^0x$), so use $\cos^2x = \dfrac{1+\cos(2x)}{2}$:
$$\int\cos^2x\,dx = \int\frac{1+\cos(2x)}{2}\,dx = \frac{x}{2} + \frac{\sin(2x)}{4} + C. \qquad \blacksquare$$

---

**Example 3 (Both powers even, needing the identity twice).** Evaluate $\displaystyle\int \cos^4 x\,dx$.

$$\cos^4x=(\cos^2x)^2=\left(\frac{1+\cos2x}{2}\right)^2=\frac{1+2\cos2x+\cos^22x}{4}.$$
The $\cos^22x$ term is itself an even power and needs the identity a **second** time: $\cos^22x=\dfrac{1+\cos4x}{2}$. Substituting and integrating term by term:
$$\int\cos^4x\,dx = \int\left(\frac14+\frac{\cos2x}{2}+\frac18+\frac{\cos4x}{8}\right)dx = \frac{3x}{8}+\frac{\sin2x}{4}+\frac{\sin4x}{32}+C. \qquad\blacksquare$$

---

**Example 4 (Odd power of tangent — sec/tan integral).** Evaluate $\displaystyle\int \sec^4x\tan^3x\,dx$.

The power of tangent ($3$) is odd, so peel off one $\sec x\tan x$ and convert the rest of the tangent power using $\tan^2x=\sec^2x-1$: $\tan^3x = \tan^2x\cdot\tan x = (\sec^2x-1)\tan x$, so the integral is $\int\sec^3x(\sec^2x-1)\cdot(\sec x\tan x)\,dx$. Substituting $u=\sec x$, $du=\sec x\tan x\,dx$:
$$\int u^3(u^2-1)\,du = \int(u^5-u^3)\,du = \frac{u^6}{6}-\frac{u^4}{4}+C = \frac{\sec^6x}{6}-\frac{\sec^4x}{4}+C. \qquad \blacksquare$$

---

**Example 5 (Partial fractions — repeated linear factor, with long division).** Evaluate $\displaystyle\int \frac{x^2+3x+5}{x+1}\,dx$ and $\displaystyle\int \frac{2x+6}{(x+1)^2}\,dx$.

*First integral:* since $\deg(\text{numerator})=2\geq1=\deg(\text{denominator})$, long-divide first: $x^2+3x+5=(x+1)(x+2)+3$, so
$$\int\left(x+2+\frac{3}{x+1}\right)dx = \frac{x^2}{2}+2x+3\ln|x+1|+C.$$
*Second integral:* set up $\dfrac{2x+6}{(x+1)^2} = \dfrac{A}{x+1}+\dfrac{B}{(x+1)^2}$ — **two** terms since the factor is repeated. Clearing denominators: $2x+6=A(x+1)+B$, giving $A=2$, $B=4$:
$$\int\left(\frac{2}{x+1}+\frac{4}{(x+1)^2}\right)dx = 2\ln|x+1|-\frac{4}{x+1}+C. \qquad\blacksquare$$

---

**Example 6 (The Weierstrass substitution — and a comparison with a direct method).** Evaluate $\displaystyle\int \frac{1}{2+\cos x}\,dx$.

No odd/even power pattern applies here (there is no power of sine or cosine to peel off), so use $t=\tan(x/2)$: $\cos x = \dfrac{1-t^2}{1+t^2}$, $dx=\dfrac{2\,dt}{1+t^2}$, so
$$\int\frac{1}{2+\frac{1-t^2}{1+t^2}}\cdot\frac{2\,dt}{1+t^2} = \int \frac{2\,dt}{2(1+t^2)+(1-t^2)} = \int\frac{2\,dt}{t^2+3}.$$
This is now a standard arctangent form: $\displaystyle\int\frac{2\,dt}{t^2+3} = \frac{2}{\sqrt3}\arctan\!\left(\frac{t}{\sqrt3}\right)+C = \frac{2}{\sqrt3}\arctan\!\left(\frac{\tan(x/2)}{\sqrt3}\right)+C$.

**Why this matters as a fallback:** nothing in the Page 1 "odd/even power" toolkit applies directly to $\frac{1}{2+\cos x}$ — there is no $\sin x$ or $\tan x$ factor to substitute with. The Weierstrass substitution turned an integral with no obvious technique into a routine arctangent integral, at the cost of a messier-looking intermediate rational function in $t$. $\blacksquare$

---

## Pages 4–5 — Practice Problems (unsolved)

**Trigonometric Integrals**

1. Evaluate $\displaystyle\int \sin^{10}x\cos x\,dx$ and $\displaystyle\int\sin^{10}x\cos^7x\,dx$ (identify which technique each needs).
2. Evaluate $\displaystyle\int \sin^4x\,dx$ (both powers even — apply the half-angle identity twice, as in Worked Example 3).
3. State which substitution ($u=\tan x$ or $u=\sec x$) is appropriate for $\displaystyle\int\sec^5x\tan^3x\,dx$, and explain why using the Key Fact on Page 1, then evaluate it.
4. Evaluate $\displaystyle\int \tan^3x\,dx$. (Hint: $\tan^3x = \tan x\cdot\tan^2x = \tan x(\sec^2x-1)$, then split into two integrals.)

**Partial Fractions**

5. Evaluate $\displaystyle\int \frac{1}{x^2+3x}\,dx$ and $\displaystyle\int\frac{1}{x^3-x}\,dx$, first factoring each denominator completely.
6. Evaluate $\displaystyle\int \frac{3x^2+2}{x^2+1}\,dx$. (Watch the degree of the numerator before deciding whether to long-divide.)
7. Evaluate $\displaystyle\int \frac{x+1}{x^2(x-2)}\,dx$, setting up the correct three-term decomposition for a distinct linear factor plus a repeated linear factor.
8. Evaluate $\displaystyle\int \frac{2x}{(x^2+1)(x-1)}\,dx$, using an irreducible-quadratic term $\dfrac{Ax+B}{x^2+1}$ together with $\dfrac{C}{x-1}$.

**The Weierstrass Substitution**

9. Use $t=\tan(x/2)$ to evaluate $\displaystyle\int \frac{1}{1+\sin x}\,dx$.
10. Use $t=\tan(x/2)$ to evaluate $\displaystyle\int \frac{1}{3+5\cos x}\,dx$, and simplify the resulting arctangent (or logarithm, depending on the sign of the discriminant) expression fully.
11. Show that $\displaystyle\int \sec x\,dx$ can be evaluated with the Weierstrass substitution and confirm it agrees with the memorized formula $\ln|\sec x+\tan x|+C$. (This is a good consistency check on the substitution itself.)

**Mixed / Technique Identification**

12. For each integral, state which single technique from Weeks 3–4 (substitution, integration by parts, trig-power identities, partial fractions, or the Weierstrass substitution) is the most efficient, without fully evaluating: (a) $\displaystyle\int \frac{x}{x^2-9}dx$; (b) $\displaystyle\int x^2\cos(x^3)\,dx$; (c) $\displaystyle\int \frac{1}{\sin x-\cos x}\,dx$; (d) $\displaystyle\int \sec^6x\,dx$.

---

## Answer Key & Misconception Notes (for tutor use — do not show student until after attempt)

| # | Answer | Common misconception |
|---|---|---|
| 1 | $\int\sin^{10}x\cos x\,dx$: substitution $u=\sin x$ works directly since $\cos x\,dx=du$: $=\frac{\sin^{11}x}{11}+C$; $\int\sin^{10}x\cos^7x\,dx$: cosine's power (7) is odd, so peel one off and convert the rest via $\cos^6x=(1-\sin^2x)^3$, then $u=\sin x$ | Trying to use $u=\sin x$ directly on the second integral without first peeling off a $\cos x$ factor to match — $\cos^7x\,dx$ does not equal $du$ for $u=\sin x$ on its own, only $\cos x\,dx$ does. |
| 2 | $\sin^4x=\left(\frac{1-\cos2x}{2}\right)^2=\frac{1-2\cos2x+\cos^22x}{4}$, and $\cos^22x=\frac{1+\cos4x}{2}$: integrating gives $\frac{3x}{8}-\frac{\sin2x}{4}+\frac{\sin4x}{32}+C$ | Applying the half-angle identity once and stopping, leaving a $\cos^22x$ term unintegrated — squaring the half-angle substitution always reintroduces another even power that itself needs the identity. |
| 3 | Neither exponent alone fits the "even secant" pattern since $n=5$ is odd — but $m=3$ (tangent) is odd, so the **odd-tangent** rule applies: peel off $\sec x\tan x$, convert $\tan^2x=\sec^2x-1$, substitute $u=\sec x$: $\int\sec^4x(\sec^2x-1)\sec x\tan x\,dx = \int u^4(u^2-1)du = \frac{u^7}{7}-\frac{u^5}{5}+C=\frac{\sec^7x}{7}-\frac{\sec^5x}{5}+C$ | Checking only whether $n$ (secant's power) is even and concluding neither rule applies when $n$ is odd — but the odd-tangent rule only needs $m$ (tangent's power) to be odd, independent of whether $n$ is even or odd. |
| 4 | $\int\tan^3x\,dx = \int\tan x\sec^2x\,dx - \int\tan x\,dx = \frac{\tan^2x}{2}-\ln\lvert\sec x\rvert+C$ | Trying to apply the sec/tan parity rule from Page 1 directly, forgetting it's stated for $\sec^n x\tan^m x$ with $n\geq1$ actually present — here $n=0$ (no secant factor), so the integral is split using $\tan^2x=\sec^2x-1$ first instead. |
| 5 | $\frac{1}{x^2+3x}=\frac{1}{x(x+3)}=\frac{A}{x}+\frac{B}{x+3}$ with $A=\frac13,B=-\frac13$: integral $=\frac13\ln\lvert x\rvert-\frac13\ln\lvert x+3\rvert+C$; $\frac{1}{x^3-x}=\frac{1}{x(x-1)(x+1)}=\frac{A}{x}+\frac{B}{x-1}+\frac{C}{x+1}$ with $A=-1,B=\frac12,C=\frac12$: integral $=-\ln\lvert x\rvert+\frac12\ln\lvert x-1\rvert+\frac12\ln\lvert x+1\rvert+C$ | Factoring $x^3-x$ as $x(x^2-1)$ and stopping there, setting up only two partial-fraction terms instead of recognizing $x^2-1=(x-1)(x+1)$ factors further into two distinct linear factors, each needing its own term. |
| 6 | $\deg(\text{num})=\deg(\text{denom})=2$, so long-divide first: $\frac{3x^2+2}{x^2+1}=3+\frac{-1}{x^2+1}$: integral $=3x-\arctan x+C$ | Trying to decompose $\frac{3x^2+2}{x^2+1}$ directly into $\frac{Ax+B}{x^2+1}$ without long dividing first — partial fractions only applies once $\deg(\text{numerator})<\deg(\text{denominator})$. |
| 7 | $\frac{x+1}{x^2(x-2)}=\frac{A}{x}+\frac{B}{x^2}+\frac{C}{x-2}$; clearing denominators and matching coefficients gives $A=-\frac34,\,B=-\frac12,\,C=\frac34$: integral $=-\frac34\ln\lvert x\rvert+\frac{1}{2x}+\frac34\ln\lvert x-2\rvert+C$ | Setting up only $\frac{A}{x^2}+\frac{B}{x-2}$ (one term for the repeated factor instead of two) — a repeated linear factor $x^2=(x-0)^2$ needs both a $\frac{A}{x}$ term and a $\frac{B}{x^2}$ term. |
| 8 | $\frac{2x}{(x^2+1)(x-1)}=\frac{Ax+B}{x^2+1}+\frac{C}{x-1}$; clearing denominators and matching coefficients gives $A=-1,\,B=-1,\,C=1$: integral $=-\frac12\ln(x^2+1)-\arctan x+\ln\lvert x-1\rvert+C$ | Using a constant numerator $\frac{A}{x^2+1}$ instead of a linear numerator $\frac{Ax+B}{x^2+1}$ for the irreducible quadratic factor — this under-determines the system and cannot match all the coefficients. |
| 9 | $t=\tan(x/2)$: $\sin x=\frac{2t}{1+t^2}$, $dx=\frac{2dt}{1+t^2}$: $\int\frac{1}{1+\frac{2t}{1+t^2}}\cdot\frac{2dt}{1+t^2}=\int\frac{2dt}{(1+t)^2}=\frac{-2}{1+t}+C=\frac{-2}{1+\tan(x/2)}+C$ | Forgetting that $1+\sin x$ becomes $\frac{(1+t)^2}{1+t^2}$ (a perfect square) after combining over a common denominator — missing this simplification leads to an unnecessarily complicated partial-fraction setup instead of a direct power-rule integral. |
| 10 | $t=\tan(x/2)$: $\cos x=\frac{1-t^2}{1+t^2}$: $\int\frac{1}{3+5\cdot\frac{1-t^2}{1+t^2}}\cdot\frac{2dt}{1+t^2}=\int\frac{2dt}{3(1+t^2)+5(1-t^2)}=\int\frac{2dt}{8-2t^2}=\int\frac{dt}{4-t^2}$, a standard log-form partial-fraction integral (since the denominator factors over the reals): $=\frac14\ln\left\lvert\frac{2+t}{2-t}\right\rvert+C=\frac14\ln\left\lvert\frac{2+\tan(x/2)}{2-\tan(x/2)}\right\rvert+C$ | Assuming the Weierstrass substitution always produces an arctangent — it produces whatever standard rational-integral form the resulting denominator calls for (arctangent if the denominator is irreducible, a log/partial-fraction form if it factors, as it does here). |
| 11 | $t=\tan(x/2)$: $\int\sec x\,dx=\int\frac{1+t^2}{1-t^2}\cdot\frac{2dt}{1+t^2}=\int\frac{2\,dt}{1-t^2}=\ln\left\lvert\frac{1+t}{1-t}\right\rvert+C$; using the half-angle identities $1+t=1+\tan(x/2)$ and half-angle algebra, this simplifies to $\ln\lvert\sec x+\tan x\rvert+C$, matching the memorized formula | Treating the Weierstrass-substitution answer $\ln\left\lvert\frac{1+\tan(x/2)}{1-\tan(x/2)}\right\rvert+C$ as a *different* correct answer from $\ln\lvert\sec x+\tan x\rvert+C$ rather than checking (via half-angle identities) that the two expressions are actually algebraically equal up to a constant. |
| 12 | (a) substitution ($u=x^2-9$, direct match); (b) substitution ($u=x^3$, direct match); (c) Weierstrass substitution (no odd/even trig-power pattern applies to a sum of sine and cosine in the denominator); (d) sec/tan even-secant rule (peel off $\sec^2x$, substitute $u=\tan x$) | Reaching for the Weierstrass substitution on (a), (b), or (d) "just to be safe" — it always works on rational-trig integrands, but using it where a direct substitution or the sec/tan rule already applies produces far messier intermediate algebra for no benefit. |
