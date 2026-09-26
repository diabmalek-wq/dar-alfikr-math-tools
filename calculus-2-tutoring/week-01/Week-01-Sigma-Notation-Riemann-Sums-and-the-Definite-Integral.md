# Week 1 — Sigma Notation, Riemann Sums & the Definite Integral

**Session length:** 3 hours
**Source:** OpenStax, *Calculus Volume 2*, §1.1 (Approximating Areas) & §1.2 (The Definite Integral); paired with MAT137 (Calculus with Proofs) Unit 7 lecture-slide prompts on partitions, suprema/infima, and upper/lower sums — MAT137 is the University of Toronto's official exclusion-equivalent of MATA37H3

---

## Page 1 — Introduction, Key Facts & Definitions

### Recap and orientation

This unit builds the machinery needed to give a rigorous meaning to "the area under a curve," which is exactly what the definite integral will turn out to be. We start with **sigma notation**, a compact way to write long sums, then use sums of rectangle areas (**Riemann sums**) to approximate area, and finally take a limit as the number of rectangles goes to infinity to *define* the definite integral. Along the way we introduce **partitions**, **upper and lower sums**, and the supremum/infimum ideas that make the definition precise. Everything in Units 8 onward (the Fundamental Theorem of Calculus, integration techniques) builds directly on the definitions in this unit.

### Why this matters

Every integral you will ever compute is, underneath the antiderivative shortcuts you'll learn in Unit 8, defined as a limit of sums of rectangle areas. Understanding *why* that limit exists and *what it means* for a function to be integrable is what separates knowing the mechanics of integration from actually understanding calculus — and it is a favourite source of "trap" questions on rigorous exams (is a given set a partition? does a given expression equal $L_P(f)$ or $U_P(f)$? does the limit exist here?).

### Definition: Sigma (Summation) Notation (OpenStax §1.1)

The Greek capital letter $\Sigma$ is used to write a long sum compactly. In the form
$$\sum_{i=1}^{n} a_i,$$
$a_i$ describes the terms being added and $i$ is called the **index**. We evaluate the term at $i=1$, then $i=2$, and so on up through $i=n$, and add all the resulting values. The index is a **dummy variable**: it exists only to keep track of which terms to add, and does not affect the value of the sum. We may use any letter we like for the index ($i$, $j$, $k$, $n$, ...), and starting the sum at a different lower limit (e.g. $\sum_{i=2}^{4}$) simply changes which terms are included.

### Key Fact: Properties of Sigma Notation (OpenStax §1.1)

Let $a_1,\dots,a_n$ and $b_1,\dots,b_n$ be two sequences of terms and let $c$ be a constant. For all positive integers $n$ and integers $m$ with $1 \leq m \leq n$:
$$\sum_{i=1}^{n} c = nc, \qquad \sum_{i=1}^{n} ca_i = c\sum_{i=1}^{n} a_i,$$
$$\sum_{i=1}^{n}(a_i+b_i) = \sum_{i=1}^{n}a_i + \sum_{i=1}^{n}b_i, \qquad \sum_{i=1}^{n}(a_i-b_i) = \sum_{i=1}^{n}a_i - \sum_{i=1}^{n}b_i,$$
$$\sum_{i=1}^{n} a_i = \sum_{i=1}^{m} a_i + \sum_{i=m+1}^{n} a_i.$$
The last property lets you split a sum at any point and is exactly what makes **telescoping sums** collapse.

### Key Fact: Sums and Powers of Integers (OpenStax §1.1)

$$\sum_{i=1}^{n} i = \frac{n(n+1)}{2}, \qquad \sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6}, \qquad \sum_{i=1}^{n} i^3 = \frac{n^2(n+1)^2}{4}.$$
These closed-form formulas are what let you evaluate a Riemann sum *exactly*, in closed form, before taking the limit as $n\to\infty$ (rather than only estimating it numerically).

### Definition: Partition (OpenStax §1.1)

A set of points $P = \{x_0, x_1,\dots,x_n\}$ with $a = x_0 < x_1 < x_2 < \cdots < x_n = b$, dividing $[a,b]$ into the subintervals $[x_0,x_1],[x_1,x_2],\dots,[x_{n-1},x_n]$, is called a **partition** of $[a,b]$. If every subinterval has the same width, $P$ is a **regular partition**, and that common width is denoted $\Delta x = \dfrac{b-a}{n}$. For an arbitrary (possibly irregular) partition, the width of the $i$-th subinterval is written $\Delta x_i = x_i - x_{i-1}$.

**Watch for:** a partition of $[a,b]$ must *always* include both endpoints $a$ and $b$ — a finite set of points strictly inside $(a,b)$ is not a partition of $[a,b]$ on its own.

### Key Fact: Left- and Right-Endpoint Approximation (OpenStax §1.1)

On each subinterval $[x_{i-1},x_i]$ of a regular partition, build a rectangle of width $\Delta x$. Using the **left** endpoint's function value for the height gives the left-endpoint approximation; using the **right** endpoint's value gives the right-endpoint approximation:
$$L_n = \sum_{i=1}^{n} f(x_{i-1})\Delta x, \qquad R_n = \sum_{i=1}^{n} f(x_i)\Delta x.$$
Both are estimates of the area under $y=f(x)$ on $[a,b]$; neither is exact for finite $n$, but both improve as $n$ grows.

### Definition: Riemann Sum (OpenStax §1.1)

Let $f$ be defined on $[a,b]$ and let $P$ be a partition with subintervals of width $\Delta x_i$. For each $i$, choose **any** point $x_i^*$ in $[x_{i-1},x_i]$ (a "sample point" — not necessarily an endpoint). The corresponding **Riemann sum** for $f$ is
$$\sum_{i=1}^{n} f(x_i^*)\,\Delta x_i.$$
Left- and right-endpoint approximations are the special cases $x_i^* = x_{i-1}$ and $x_i^* = x_i$.

### Definition: Area via a Limit of Riemann Sums (OpenStax §1.1)

If $f$ is continuous and nonnegative on $[a,b]$, the (exact) area under $y=f(x)$ on $[a,b]$ is
$$A = \lim_{n\to\infty} \sum_{i=1}^{n} f(x_i^*)\Delta x.$$
This limit can be shown to exist and to be the same regardless of how the sample points $x_i^*$ are chosen, whenever $f$ is continuous — this independence-of-choice is what makes "the area under the curve" a well-defined number rather than something that depends on an arbitrary choice.

### Key Fact: Upper Sums, Lower Sums, and $L_P(f)$, $U_P(f)$ (OpenStax §1.1; MAT137 notation)

If, on each subinterval, $x_i^*$ is chosen so that $f(x_i^*)$ is the **supremum** (least upper bound) of $f$ on $[x_{i-1},x_i]$, the resulting Riemann sum is called the **upper sum**, written $U_P(f)$. If $f(x_i^*)$ is instead the **infimum** (greatest lower bound) of $f$ on that subinterval, the resulting sum is the **lower sum**, $L_P(f)$. For *any* partition $P$ and any bounded function $f$,
$$L_P(f) \leq U_P(f),$$
because every lower estimate on a subinterval is $\leq$ every upper estimate on that same subinterval. If $f$ is monotonic (increasing or decreasing throughout $[a,b]$), the maximum/minimum on each subinterval automatically occurs at an endpoint, so $L_P(f)$ and $U_P(f)$ coincide with whichever of $L_n, R_n$ is the underestimate/overestimate.

**Refining a partition:** if $Q \supseteq P$ (i.e. $Q$ is obtained from $P$ by adding more partition points — a **finer** partition), then
$$L_P(f) \leq L_Q(f) \leq U_Q(f) \leq U_P(f).$$
Lower sums only ever increase and upper sums only ever decrease as you add more points — they "squeeze" toward each other.

### Definition: The Definite Integral (OpenStax §1.2)

If $f$ is a function defined on $[a,b]$, the **definite integral** of $f$ from $a$ to $b$ is
$$\int_a^b f(x)\,dx = \lim_{n\to\infty} \sum_{i=1}^{n} f(x_i^*)\Delta x,$$
**provided this limit exists** (and is the same for every choice of sample points $x_i^*$). If it exists, $f$ is called **integrable** on $[a,b]$. Here $a,b$ are the **limits of integration** ($a$ lower, $b$ upper), $f(x)$ is the **integrand**, and $x$ (in $dx$) is the **variable of integration** — itself a dummy variable, so $\int_a^b f(x)\,dx = \int_a^b f(t)\,dt$.

### Theorem: Continuous Functions Are Integrable (OpenStax §1.2, Theorem 1.1)

If $f$ is continuous on $[a,b]$, then $f$ is integrable on $[a,b]$. (Integrability can still hold for some discontinuous functions too — e.g. a function with finitely many jump discontinuities — but continuity is the simplest sufficient condition, and the one used most often in this course.)

### Key Fact: Equivalent Characterizations of the Supremum (MAT137 Unit 7, Videos 7.3–7.4)

Let $S$ be an upper bound of a set $A \subseteq \mathbb{R}$. The following statements are **all equivalent** to "$S = \sup A$":
$$\text{(i) if } R \text{ is an upper bound of } A \text{, then } S \leq R;$$
$$\text{(ii) } \forall R < S,\ R \text{ is not an upper bound of } A; \qquad \text{(iii) } \forall R < S,\ \exists\, x\in A \text{ such that } R < x;$$
$$\text{(iv) } \forall \varepsilon>0,\ \exists\, x\in A \text{ such that } S-\varepsilon < x.$$
Forms (ii)–(iv) are the ones actually used to *prove* a specific number is the supremum: they say that **no number smaller than $S$ can also be an upper bound**, so $S$ is the *smallest* one. Swapping a strict inequality for a non-strict one (e.g. "$R \leq x$" instead of "$R < x$" in (iii)) generally changes the meaning and breaks the equivalence — see Practice Problem 11.

---

## Pages 2–3 — Solved Examples

**Example 1 (Evaluate a sum using sigma-notation properties).** Evaluate $\displaystyle\sum_{i=1}^{50}(i^2 - 4i + 7)$.

Split the sum using the sigma-notation properties, then apply the closed-form formulas:
$$\sum_{i=1}^{50}(i^2-4i+7) = \sum_{i=1}^{50} i^2 - 4\sum_{i=1}^{50} i + \sum_{i=1}^{50} 7.$$
Using $\sum i^2 = \dfrac{n(n+1)(2n+1)}{6}$ and $\sum i = \dfrac{n(n+1)}{2}$ with $n=50$:
$$\sum_{i=1}^{50} i^2 = \frac{50(51)(101)}{6} = 42{,}925, \qquad \sum_{i=1}^{50} i = \frac{50(51)}{2} = 1275, \qquad \sum_{i=1}^{50} 7 = 50(7) = 350.$$
So the sum equals $42{,}925 - 4(1275) + 350 = 42{,}925 - 5100 + 350 = 38{,}175$. $\blacksquare$

---

**Example 2 (Telescoping sum).** Evaluate $\displaystyle\sum_{i=1}^{99}\left(\frac{1}{i}-\frac{1}{i+1}\right)$ exactly.

Writing out the first few and last few terms,
$$\left(\frac{1}{1}-\frac{1}{2}\right)+\left(\frac{1}{2}-\frac{1}{3}\right)+\left(\frac{1}{3}-\frac{1}{4}\right)+\cdots+\left(\frac{1}{98}-\frac{1}{99}\right)+\left(\frac{1}{99}-\frac{1}{100}\right).$$
Every term of the form $-\dfrac1k$ is exactly cancelled by the $+\dfrac1k$ in the next bracket, except the very first $+\dfrac11$ and the very last $-\dfrac{1}{100}$. So the whole sum **collapses** to
$$1 - \frac{1}{100} = \frac{99}{100}. \qquad \blacksquare$$
This is the "telescoping" trick: whenever a sum's general term is a *difference* of consecutive values of some expression, splitting it via the sigma-notation properties and writing out a few terms reveals the cancellation pattern.

---

**Example 3 (Left- and right-endpoint approximation).** Approximate the area under $f(x) = x^2 + 1$ on $[0,2]$ using $n=4$ subintervals, with both the left- and right-endpoint approximations.

With $n=4$, $\Delta x = \dfrac{2-0}{4} = 0.5$, so the partition points are $x_0=0,\ x_1=0.5,\ x_2=1,\ x_3=1.5,\ x_4=2$, and $f(x_0)=1,\ f(x_1)=1.25,\ f(x_2)=2,\ f(x_3)=3.25,\ f(x_4)=5$.

*Left endpoints* $x_0,x_1,x_2,x_3$:
$$L_4 = (1+1.25+2+3.25)(0.5) = (7.5)(0.5) = 3.75.$$
*Right endpoints* $x_1,x_2,x_3,x_4$:
$$R_4 = (1.25+2+3.25+5)(0.5) = (11.5)(0.5) = 5.75.$$
Since $f$ is increasing on $[0,2]$, $L_4$ underestimates and $R_4$ overestimates the true area, and $L_4 = L_P(f) \leq U_P(f) = R_4$ for this partition, as the theory predicts. $\blacksquare$

---

**Example 4 (Upper and lower sums on a given partition).** Let $f(x) = 9 - x^2$ on $[0,2]$, and let $P = \{0, 1, 2\}$. Compute $L_P(f)$ and $U_P(f)$.

$f$ is **decreasing** on $[0,2]$ (since $f'(x)=-2x<0$ for $x>0$), so on each subinterval the maximum of $f$ occurs at the *left* endpoint and the minimum at the *right* endpoint.

Subinterval $[0,1]$: $f(0)=9$ (max), $f(1)=8$ (min), width $\Delta x_1 = 1$.
Subinterval $[1,2]$: $f(1)=8$ (max), $f(2)=5$ (min), width $\Delta x_2 = 1$.

$$U_P(f) = f(0)(1) + f(1)(1) = 9+8 = 17, \qquad L_P(f) = f(1)(1) + f(2)(1) = 8+5 = 13.$$
Indeed $L_P(f)=13 \leq 17 = U_P(f)$. $\blacksquare$

---

**Example 5 (Refining a partition).** Using $f$ from Example 4, refine $P=\{0,1,2\}$ to $Q = \{0, 0.5, 1, 2\}$ and recompute $L_Q(f)$, $U_Q(f)$. Confirm $L_P(f)\leq L_Q(f) \leq U_Q(f) \leq U_P(f)$.

$f$ is still decreasing, so on each subinterval of $Q$ the left endpoint gives the max and the right endpoint the min.

Subintervals: $[0,0.5]$ ($\Delta x=0.5$): $f(0)=9$, $f(0.5)=8.75$. $\ [0.5,1]$ ($\Delta x = 0.5$): $f(0.5)=8.75$, $f(1)=8$. $\ [1,2]$ ($\Delta x=1$): $f(1)=8$, $f(2)=5$.

$$U_Q(f) = 9(0.5)+8.75(0.5)+8(1) = 4.5+4.375+8 = 16.875,$$
$$L_Q(f) = 8.75(0.5)+8(0.5)+5(1) = 4.375+4+5=13.375.$$
Comparing to Example 4 ($L_P=13$, $U_P=17$): $13 \leq 13.375 \leq 16.875 \leq 17$. ✓ The lower sum increased and the upper sum decreased when we refined the partition, exactly as the Key Fact predicts. $\blacksquare$

---

**Example 6 (Evaluate a definite integral from the limit definition).** Use the definition of the definite integral (with right-endpoint sample points) to evaluate $\displaystyle\int_0^1 x^2\,dx$.

Here $a=0$, $b=1$, so $\Delta x = \dfrac{1-0}{n} = \dfrac1n$, and the right endpoint of the $i$-th subinterval is $x_i = 0 + i\Delta x = \dfrac{i}{n}$. Then
$$f(x_i) = x_i^2 = \frac{i^2}{n^2}, \qquad \sum_{i=1}^{n} f(x_i)\Delta x = \sum_{i=1}^{n} \frac{i^2}{n^2}\cdot\frac1n = \frac{1}{n^3}\sum_{i=1}^{n} i^2 = \frac{1}{n^3}\cdot\frac{n(n+1)(2n+1)}{6}.$$
Expanding and simplifying,
$$\frac{n(n+1)(2n+1)}{6n^3} = \frac{2n^3+3n^2+n}{6n^3} = \frac13 + \frac{1}{2n} + \frac{1}{6n^2}.$$
Taking the limit as $n\to\infty$, the last two terms vanish:
$$\int_0^1 x^2\,dx = \lim_{n\to\infty}\left(\frac13+\frac{1}{2n}+\frac{1}{6n^2}\right) = \frac13. \qquad \blacksquare$$

---

**Example 7 (Deciding whether a set is a partition).** Which of the following are valid partitions of $[0,3]$: (a) $\{0,3\}$; (b) $\{0, 1, 1, 2, 3\}$; (c) $\{1, 3\}$; (d) $\{0, \sqrt2, 3\}$?

A partition of $[0,3]$ must be a set of points that includes **both endpoints**, listed in strictly increasing order (repeats are meaningless in a set, and the points don't need to be evenly spaced).
(a) $\{0,3\}$ — valid; it's the trivial partition with a single subinterval $[0,3]$.
(b) As a *set*, $\{0,1,1,2,3\} = \{0,1,2,3\}$ — valid (the repeated $1$ doesn't create a second point).
(c) $\{1,3\}$ — **not** valid: it does not include the left endpoint $0$, so it isn't a partition of $[0,3]$ (it would be a valid partition of $[1,3]$).
(d) $\{0,\sqrt2,3\}$ — valid; a partition's points don't need to be rational or evenly spaced, only strictly increasing and equal to $a,b$ at the ends. $\blacksquare$

---

## Pages 4–5 — Practice Problems (unsolved)

**Sigma Notation & Sums**

1. Evaluate $\displaystyle\sum_{i=1}^{6}(2i-3)$ two ways: (a) by expanding term by term, and (b) by first splitting the sum using the sigma-notation properties. Confirm the two methods agree.
2. Write $1^3 + 2^3 + 3^3 + \cdots + 40^3$ in sigma notation, then evaluate it using the closed-form formula for $\sum i^3$.
3. Evaluate $\displaystyle\sum_{i=1}^{250}\left(\frac{1}{i+1}-\frac{1}{i+2}\right)$ exactly, using the telescoping-sum idea.
4. Compute $\displaystyle\sum_{i=1}^{N}\sum_{k=1}^{i} 1$ and $\displaystyle\sum_{i=1}^{N}\sum_{k=1}^{i} k$ in terms of $N$. (Evaluate the inner sum first for each fixed $i$, then sum the result over $i$.)

**Partitions & Riemann Sums**

5. Which of the following are partitions of $[-1,4]$? (a) $[-1,4]$ itself (the whole interval, not a finite set of points); (b) $\{-1, 0, 2, 4\}$; (c) $\{-1, 4\}$; (d) $\{0, 2, 4\}$; (e) $\left\{-1 + \dfrac{5n}{n+1} : n \in \mathbb{N}\right\} \cup \{4\}$.
6. Approximate the area under $f(x) = \sqrt{x}+1$ on $[0,4]$ using $n=4$ subintervals, with both the left- and right-endpoint approximations. Which one is the overestimate here, and why?
7. Let $f(x) = 8-2x$ on $[0,3]$ and let $P=\{0,1,3\}$ (an *irregular* partition — the two subintervals do not have equal width). Compute $L_P(f)$ and $U_P(f)$, being careful to use the correct $\Delta x_i$ for each subinterval.
8. Let $f$ be an **increasing**, bounded function on $[a,b]$, and let $P=\{x_0,x_1,\dots,x_N\}$ be a partition. Write the correct summation formula for $L_P(f)$ and for $U_P(f)$ in terms of $f(x_{i-1})$, $f(x_i)$, and $\Delta x_i$ — and explain why the formulas are the *opposite* way around from the decreasing-function case in the Key Fact box on Page 1.

**The Definite Integral**

9. Use the limit definition of the definite integral (with right-endpoint sample points) to evaluate $\displaystyle\int_0^2 x^2\,dx$.
10. Suppose $L_P(f)=4$, $U_P(f)=10$ for a partition $P$, and $L_Q(f)=6$, $U_Q(f)=9$ for a partition $Q$. (a) Is it possible that $P \subseteq Q$? Justify using the Key Fact about refining partitions. (b) What can you conclude about the relationship between $L_{P\cup Q}(f)$ and both pairs of values above?
11. Let $S$ be an upper bound of a set $A \subseteq \mathbb{R}$. Consider the two statements (C) $\forall R<S,\ \exists x\in A$ such that $R<x$, and (D) $\forall R<S,\ \exists x \in A$ such that $R\leq x$. Does (C) imply (D)? Does (D) imply (C)? Which one (if either) is a correct restatement of "$S=\sup A$"?
12. Let $f$ be a bounded (but not necessarily continuous) function on $[a,b]$, and define $\underline{I}_a^b(f)$ as the *supremum over all partitions $P$* of $L_P(f)$, and $\overline{I}_a^b(f)$ as the *infimum over all partitions $P$* of $U_P(f)$. Explain why $\underline{I}_a^b(f) \leq \overline{I}_a^b(f)$ always holds, and state (in your own words) the extra condition on $f$ that is needed for $\int_a^b f(x)\,dx$ to actually exist.

---

## Answer Key & Misconception Notes (for tutor use — do not show student until after attempt)

| # | Answer | Common misconception |
|---|---|---|
| 1 | Both methods give $\sum_{i=1}^6(2i-3) = 2(21)-3(6) = 42-18=24$ | Treating $\sum(2i-3)$ as $2\sum i - 3$ (forgetting the $-3$ must also be summed $n$ times, i.e. it's $-3n$, not just $-3$). |
| 2 | $\sum_{i=1}^{40} i^3 = \dfrac{40^2(41)^2}{4} = 672{,}400$ | Using the formula for $\sum i^2$ instead of $\sum i^3$, or forgetting to square the numerator $n(n+1)$ before dividing by 4. |
| 3 | Telescopes to $\dfrac12 - \dfrac{1}{252} = \dfrac{125}{252}$ | Cancelling terms incorrectly — writing out only the first two terms instead of enough terms to see which boundary terms survive (here it's the very first $+\frac12$ and very last $-\frac{1}{252}$, not $\frac11$ and $\frac{1}{251}$, since the sum starts at $\frac{1}{i+1}$ with $i=1$). |
| 4 | $\sum_{i=1}^N\sum_{k=1}^i 1 = \sum_{i=1}^N i = \dfrac{N(N+1)}2$; $\sum_{i=1}^N\sum_{k=1}^i k = \sum_{i=1}^N \dfrac{i(i+1)}2 = \dfrac12\left(\dfrac{N(N+1)(2N+1)}6+\dfrac{N(N+1)}2\right)$ | Treating the inner sum's upper limit $i$ as if it were the constant $N$, e.g. writing $\sum_{k=1}^i 1 = N$ instead of $i$ — the inner limit depends on the outer index and changes from one outer term to the next. |
| 5 | (a) not a partition (it's an interval, not a finite point set); (b) valid; (c) not valid (missing $-1$); (d) not valid (missing $-1$); (e) valid (as $n\to\infty$ the points approach but never reach $4$ from below, and $4$ is included separately, so together with the implicit... actually this set alone is infinite and has no largest element below 4 built in as a finite list — flag as **not a valid partition** since a partition must be a *finite* set of points) | Assuming "contains the two endpoints" is sufficient on its own without also checking that the set is finite and strictly increasing — an infinite set of points is not a partition even if it's bounded by $a$ and $b$. |
| 6 | $L_4 = 4.146$ (approx), $R_4=5.146$ (approx), using $\Delta x=1$ and $f(0)=1,f(1)\approx2,f(2)\approx2.414,f(3)\approx2.732,f(4)=3$; $R_4$ overestimates since $f$ is increasing | Assuming the *right*-endpoint sum is always the overestimate regardless of whether $f$ is increasing or decreasing — it's only the overestimate here because $f$ is increasing; for a decreasing function the left sum overestimates. |
| 7 | $\Delta x_1=1$ on $[0,1]$, $\Delta x_2=2$ on $[1,3]$; since $f$ is decreasing, $U_P(f)=f(0)(1)+f(1)(2)=8+12=20$, $L_P(f)=f(1)(1)+f(3)(2)=6+4=10$ | Using the same $\Delta x$ for both subintervals (treating the partition as if it were regular) instead of computing $\Delta x_i = x_i-x_{i-1}$ separately for each piece. |
| 8 | For increasing $f$: $L_P(f)=\sum_{i=1}^N f(x_{i-1})\Delta x_i$ (left endpoint gives the min), $U_P(f)=\sum_{i=1}^N f(x_i)\Delta x_i$ (right endpoint gives the max) — swapped from the decreasing case because for an increasing function the smallest value on each subinterval is at the *left* end, not the right | Copying the decreasing-function formulas from Page 1 without re-deriving which endpoint gives the max vs. min for an increasing function — the roles of left/right literally reverse. |
| 9 | $\int_0^2 x^2\,dx = \lim_{n\to\infty}\dfrac{8}{3}\cdot\text{(ratio}\to1) = \dfrac83$ (using $\Delta x=2/n$, $x_i=2i/n$, and $\sum f(x_i)\Delta x = \dfrac{8}{n^3}\sum i^2 \to \dfrac83$) | Reusing the exact algebra from the worked $\int_0^1x^2dx$ example without redoing $\Delta x = (b-a)/n$ and $x_i$ for the new limits $a=0,b=2$ — the constant out front changes from $\frac13$ to $\frac83$, it does not stay the same. |
| 10 | (a) No: if $P\subseteq Q$ we'd need $L_P(f)\leq L_Q(f)$ **and** $U_Q(f)\leq U_P(f)$ simultaneously; here $L_P=4\leq L_Q=6$ ✓ but $U_Q=9\leq U_P=10$ ✓ as well — so actually this data is *consistent* with $P\subseteq Q$, though it doesn't prove it (other configurations of $P,Q$ could produce the same numbers without one containing the other). (b) $L_{P\cup Q}(f) \geq \max(L_P,L_Q)=6$ and $U_{P\cup Q}(f)\leq\min(U_P,U_Q)=9$, since $P\cup Q$ refines both $P$ and $Q$ | Concluding "$P\subseteq Q$" or "$Q\subseteq P$" is *forced* by the numbers, when refining relationships only give one-directional inequalities — consistency with a containment is not proof of it. |
| 11 | (C) does **not** imply (D) is false — actually (C) $\Rightarrow$ (D) trivially since $R<x \Rightarrow R\leq x$; (D) does **not** imply (C) in general (e.g. if the only element of $A$ satisfying $R\leq x$ has $x=R$ exactly, (D) holds but (C) fails); (C) is the correct restatement of $S=\sup A$, not (D) | Assuming that swapping $<$ for $\leq$ in a supremum-style statement never changes its truth value or logical strength — here it strictly weakens the implication in one direction. |
| 12 | $\underline{I}_a^b(f)\leq\overline{I}_a^b(f)$ because for *any two* partitions $P,Q$ (not just $P=Q$), $L_P(f)\leq L_{P\cup Q}(f)\leq U_{P\cup Q}(f)\leq U_Q(f)$, so every lower sum is $\leq$ every upper sum, hence the sup of all lower sums is $\leq$ the inf of all upper sums; $f$ is (Riemann) integrable exactly when $\underline{I}_a^b(f)=\overline{I}_a^b(f)$ | Trying to prove $L_P(f)\leq U_P(f)$ for the *same* partition $P$ (true, but not what's needed) instead of comparing $L_P(f)$ and $U_Q(f)$ for two *different* partitions via their common refinement $P\cup Q$ — the general inequality needs the refinement step. |
