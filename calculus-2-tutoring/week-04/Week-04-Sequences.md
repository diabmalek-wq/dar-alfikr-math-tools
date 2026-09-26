# Week 4 — Sequences

**Session length:** 3 hours
**Source:** OpenStax, *Calculus Volume 2*, §5.1 (Sequences); paired with MAT137 (Calculus with Proofs) Unit 11 lecture-slide prompts on the formal $\varepsilon$–$N$ definition of limit, monotonicity/boundedness, and proof-writing about sequences — MAT137 is the University of Toronto's official exclusion-equivalent of MATA37H3

---

## Page 1 — Introduction, Key Facts & Definitions

### Recap and orientation

Units 7–9 built up integral calculus; Units 11–14 pivot to **sequences and series** — the other major topic of MATA37H3. A sequence is just an infinite, ordered list of numbers, and the central question is always: does it settle down to a single number (**converge**), or not (**diverge**)? This unit gives the rigorous, $\varepsilon$–$N$ definition of convergence (parallel to the $\varepsilon$–$\delta$ definition of a function limit), the key structural properties (monotonic, bounded), and the two big convergence theorems: Squeeze and Monotone Convergence.

### Why this matters

Series (Units 13–14) are literally defined as limits of sequences of partial sums, so every series-convergence question secretly reduces to a sequence-convergence question. The formal $\varepsilon$–$N$ definition is also a favourite proof-writing topic on rigorous exams — recognizing which of several superficially similar quantifier statements is actually equivalent to "$a_n\to L$" is a core skill (see the Key Fact below and Worked Example 3).

### Definition: Sequence, Explicit Formula, Recurrence Relation (OpenStax §5.1)

An infinite **sequence** $\{a_n\}_{n=1}^\infty$ is an ordered list $a_1, a_2, a_3, \ldots$. The subscript $n$ is the **index**, and each $a_n$ is a **term**. A sequence can be given by an **explicit formula** $a_n = f(n)$, or by a **recurrence relation**, where one or more terms are given explicitly and later terms are defined in terms of earlier ones (e.g. $a_1=3$, $a_n = a_{n-1}+4$ for $n\geq2$). The index need not start at $1$ — it can start at $0$ or any other integer. Equivalently, a sequence **is** a function whose domain is a set of consecutive integers, which is exactly what lets us compare sequences to ordinary functions (as in the next Key Fact).

### Key Fact: Sequences vs. Functions (MAT137 Unit 11)

If $f$ has domain $[0,\infty)$ and we define $a_n = f(n)$, several natural-looking implications between "$f$-behaviour" and "$a_n$-behaviour" are **true only in one direction**:
- $\displaystyle\lim_{x\to\infty}f(x)=L \implies \lim_{n\to\infty}a_n=L$ — **true**: if $f(x)$ settles to $L$ along the whole continuum, it certainly does so along the integers.
- $\displaystyle\lim_{n\to\infty}a_n=L \implies \lim_{x\to\infty}f(x)=L$ — **false in general**: $a_n$ only samples $f$ at integers, so $f$ could oscillate wildly *between* integers without the sequence ever noticing (e.g. $f(x)=\sin(\pi x)$ gives $a_n=0$ for all $n$, yet $\lim_{x\to\infty}\sin(\pi x)$ does not exist).
- Similarly, $f$ increasing $\implies \{a_n\}$ increasing (true), but $\{a_n\}$ increasing $\nRightarrow f$ increasing (false — same oscillation idea).
- $f$ bounded $\implies\{a_n\}$ bounded (true), but $\{a_n\}$ bounded $\nRightarrow f$ bounded (false).

### Definition: Convergence of a Sequence — the Formal $\varepsilon$–$N$ Definition (OpenStax §5.1)

A sequence $\{a_n\}$ **converges** to $L\in\mathbb{R}$, written $\displaystyle\lim_{n\to\infty}a_n=L$, if
$$\forall \varepsilon>0,\ \exists n_0\in\mathbb{N},\ \forall n\in\mathbb{N},\quad n\geq n_0 \implies |a_n-L|<\varepsilon.$$
If no such $L$ exists, $\{a_n\}$ **diverges**. Every quantifier and every symbol here is load-bearing: $\varepsilon$ ranges over all positive reals (not just small ones, and not just integers), $n_0$ must be a natural number (an index, not an arbitrary real), and the inequality $n\geq n_0$ (not strict) must hold for *every* $n$ from $n_0$ onward, not just one. See Worked Example 3 for exactly which small changes to this statement still give an equivalent definition and which do not.

### Definition: Divergence to $\infty$ (MAT137 Unit 11)

A sequence $\{a_n\}$ **diverges to $\infty$**, written $a_n\to\infty$, if
$$\forall M\in\mathbb{R},\ \exists n_0\in\mathbb{N},\ \forall n\in\mathbb{N},\quad n\geq n_0\implies a_n>M.$$
(Divergence to $-\infty$ is the mirror statement with $a_n<M$.) Note "diverges to $\infty$" is a *specific kind* of divergence — a sequence can diverge without diverging to $\infty$ or $-\infty$ at all, e.g. $\{(-1)^n\}$, which merely oscillates.

### Definition: Bounded, Increasing, Decreasing, Monotonic (OpenStax §5.1)

$\{a_n\}$ is **bounded above** if $\exists M\in\mathbb{R}$ with $a_n\leq M$ for all $n$; **bounded below** similarly with $a_n\geq M$; **bounded** if both. $\{a_n\}$ is **increasing** (from some point $n_0$ on) if $a_n\leq a_{n+1}$ for all $n\geq n_0$; **decreasing** if $a_n\geq a_{n+1}$; **monotonic** (eventually) if it is eventually increasing or eventually decreasing. "Eventually" matters: a sequence can fail to be monotonic on its first several terms and still be eventually monotonic, which is all the theorems below require.

### Theorem: Convergent Sequences Are Bounded (OpenStax §5.1, Theorem 5.5)

If $\{a_n\}$ converges, then it is bounded. **The converse is false**: $\{(-1)^n\}$ is bounded but does not converge (it oscillates between $-1$ and $1$ forever without settling).

### Theorem: Monotone Convergence Theorem (OpenStax §5.1, Theorem 5.6)

If $\{a_n\}$ is bounded, and eventually monotonic, then $\{a_n\}$ **converges**. This is a genuinely useful *sufficient* condition: it lets you prove a sequence converges without first finding its limit — bounded + eventually monotonic is enough. It is not necessary, however: plenty of convergent sequences are not monotonic (e.g. $a_n = \frac{(-1)^n}{n}$, which oscillates in sign while still $\to 0$).

### Theorem: Squeeze Theorem for Sequences (OpenStax §5.1, Theorem 5.4)

If $a_n \leq b_n \leq c_n$ for all $n$ past some point, and $\displaystyle\lim_{n\to\infty}a_n = L = \lim_{n\to\infty}c_n$, then $\displaystyle\lim_{n\to\infty}b_n = L$ too. This is the standard tool for sequences whose formula involves a bounded "wobble" term like $\sin n$ or $\cos n$ multiplied by something going to $0$.

### Key Fact: Geometric Sequence Behaviour (OpenStax §5.1)

For the geometric sequence $\{r^n\}$: $r^n\to 0$ if $|r|<1$; $r^n\to 1$ if $r=1$; $r^n\to\infty$ if $r>1$; and $\{r^n\}$ diverges (oscillating, unbounded) if $r\leq -1$. This single fact, memorized, resolves an enormous number of limit and (later) series-convergence questions instantly.

### Key Fact: "The Big Theorem" — Comparing Growth Rates (MAT137 Unit 11)

Write $a_n \ll b_n$ ("$a_n$ is dominated by $b_n$," for **positive** sequences) to mean $\displaystyle\lim_{n\to\infty}\frac{a_n}{b_n}=0$. The formal (equivalent) definition is
$$\forall \varepsilon>0,\ \exists n_0\in\mathbb{N},\ \forall n\in\mathbb{N},\quad n\geq n_0 \implies a_n < \varepsilon\, b_n.$$
The Big Theorem ranks the standard growth-rate families from slowest to fastest:
$$\ln n \ \ll\ n^a\ (a>0) \ \ll\ r^n\ (r>1) \ \ll\ n! \ \ll\ n^n.$$
This is the tool of choice for evaluating limits of ratios that mix factorials, exponentials, and polynomials (see Worked Examples 5–6), and later becomes essential for the Ratio and Root Tests (Unit 13/14).

---

## Pages 2–3 — Solved Examples

**Example 1 (Finding an explicit formula from a pattern).** Find an explicit formula for the general term of $\left\{-\dfrac12, \dfrac23, -\dfrac34, \dfrac45, -\dfrac56,\ldots\right\}$.

The signs alternate, starting negative at $n=1$, so include a factor $(-1)^n$. The numerators are $1,2,3,4,5,\ldots$, i.e. $n$. The denominators are $2,3,4,5,6,\ldots$, i.e. $n+1$. So
$$a_n = \frac{(-1)^n\,n}{n+1}. \qquad \blacksquare$$

---

**Example 2 (Recurrence relation to explicit formula).** Find an explicit formula for $a_1=2$, $a_n = -3a_{n-1}$ for $n\geq2$.

Write out terms: $a_1=2$, $a_2=-3(2)$, $a_3=(-3)^2(2)$, $a_4=(-3)^3(2)$. The pattern is $a_n = 2(-3)^{n-1}$. (Check: $n=1$ gives $2(-3)^0=2$. ✓) $\blacksquare$

---

**Example 3 (Dissecting the formal definition of a limit — which variants are equivalent?).** Let $\{a_n\}_{n=0}^\infty$ be a sequence and $L\in\mathbb{R}$. Decide whether each variant below is **equivalent** to the standard definition $\forall\varepsilon>0,\exists n_0\in\mathbb{N},\forall n\in\mathbb{N},\,n\geq n_0\implies|a_n-L|<\varepsilon$:

(a) Same statement but with $n>n_0$ instead of $n\geq n_0$.
(b) Same statement but with $n_0\in\mathbb{R}$ instead of $n_0\in\mathbb{N}$.
(c) Same statement but with $|a_n-L|\leq\varepsilon$ instead of $<\varepsilon$.
(d) $\forall k\in\mathbb{Z}^+,\exists n_0\in\mathbb{N},\forall n\in\mathbb{N}, n\geq n_0\implies |a_n-L|<\frac1k$.

(a) **Equivalent.** If the $\geq n_0$ version holds, the $>n_0$ version holds using $n_0' = n_0+1$ (shifting the threshold by one index doesn't change which tail of the sequence is being controlled); conversely $>n_0$ implies $\geq n_0$ using the same $n_0$ shifted down — either way, both express "eventually within $\varepsilon$."

(b) **Equivalent.** Since $\mathbb{N}\subset\mathbb{R}$, allowing $n_0$ to be any real number seems weaker, but any real threshold can be replaced by $\lceil n_0\rceil\in\mathbb{N}$ without changing which $n\in\mathbb{N}$ satisfy $n\geq n_0$.

(c) **Equivalent**, though this takes more care: $<\varepsilon$ trivially implies $\leq\varepsilon$; conversely, if the $\leq\varepsilon$ version holds for all $\varepsilon>0$, then given any $\varepsilon>0$, apply it with $\varepsilon/2$ to get $|a_n-L|\leq\varepsilon/2<\varepsilon$, recovering the strict version.

(d) **Equivalent.** This restricts $\varepsilon$ to only the special values $\frac1k$ for positive integers $k$, but since every $\varepsilon>0$ has some $\frac1k<\varepsilon$, controlling all the $\frac1k$ automatically controls every $\varepsilon$ (using the same $n_0$ that works for that $\frac1k$). $\blacksquare$

---

**Example 4 (Squeeze Theorem).** Find $\displaystyle\lim_{n\to\infty} \frac{\cos n}{n^2}$.

Since $-1\leq\cos n\leq 1$ for every integer $n$, dividing through by $n^2>0$ gives $-\dfrac{1}{n^2}\leq\dfrac{\cos n}{n^2}\leq\dfrac{1}{n^2}$. Since $-\dfrac{1}{n^2}\to0$ and $\dfrac1{n^2}\to0$, the Squeeze Theorem gives $\dfrac{\cos n}{n^2}\to 0$. $\blacksquare$

---

**Example 5 (Using the Big Theorem to evaluate a limit).** Find $\displaystyle\lim_{n\to\infty}\frac{n!+2e^n}{3n!+4e^n}$.

By the Big Theorem, $e^n \ll n!$ (exponential is dominated by factorial), so as $n\to\infty$, both the numerator and denominator are eventually dominated by their $n!$ terms — the $e^n$ terms become negligible in comparison. Formally, divide every term by $n!$:
$$\frac{n!+2e^n}{3n!+4e^n} = \frac{1+2\frac{e^n}{n!}}{3+4\frac{e^n}{n!}} \xrightarrow[n\to\infty]{} \frac{1+2(0)}{3+4(0)} = \frac13,$$
using $\dfrac{e^n}{n!}\to0$, which is exactly the statement $e^n\ll n!$. $\blacksquare$

---

**Example 6 (Big Theorem with three competing terms).** Find $\displaystyle\lim_{n\to\infty}\frac{5n^5+5^n+5\cdot n!}{n^n}$.

By the Big Theorem's chain $n^a \ll r^n \ll n! \ll n^n$, the term $n!$ dominates $5^n$ and $n^5$, but $n^n$ dominates $n!$ itself (since $n^n = n\cdot n^{n-1} \gg (n-1)!\cdot n \approx n!$ for large $n$). So every term in the numerator is dominated by the denominator $n^n$, and dividing through, each fraction $\to 0$:
$$\frac{5n^5+5^n+5n!}{n^n} = \frac{5n^5}{n^n}+\frac{5^n}{n^n}+\frac{5\cdot n!}{n^n} \xrightarrow[n\to\infty]{} 0+0+0 = 0. \qquad \blacksquare$$

---

**Example 7 (Proving convergence via Monotone Convergence, without finding the limit first).** Let $a_1 = \sqrt2$ and $a_n = \sqrt{2+a_{n-1}}$ for $n\geq2$. Prove $\{a_n\}$ converges (you are not asked to find the limit).

*Bounded:* Claim $a_n<2$ for all $n$. Base case: $a_1=\sqrt2<2$. Inductive step: if $a_{n-1}<2$, then $a_n = \sqrt{2+a_{n-1}} < \sqrt{2+2}=2$. So by induction $a_n<2$ for all $n$, i.e. $\{a_n\}$ is bounded above by $2$ (and bounded below by $0$ since it's a sequence of square roots).

*Monotonic:* Claim $a_n$ is increasing. Since $0<a_{n-1}<2$, we have $2+a_{n-1} > a_{n-1}$ would need $2>0$ ✓, more directly: $a_n^2 - a_{n-1}^2$... a cleaner route: since $a_{n-1}<2$, $a_{n-1}^2 < 2a_{n-1}$ would need $a_{n-1}<2$ ✓ (as $a_{n-1}>0$), so $a_{n-1}^2 < 2a_{n-1} < 2+a_{n-1} = a_n^2$, and since both sides are positive, $a_{n-1}<a_n$. So $\{a_n\}$ is increasing.

By the Monotone Convergence Theorem, a bounded, monotonic (here, increasing) sequence converges. $\blacksquare$ (Bonus, not required: the limit satisfies $L=\sqrt{2+L}\Rightarrow L^2-L-2=0\Rightarrow L=2$.)

---

## Pages 4–5 — Practice Problems (unsolved)

**Formulas & Recurrence Relations**

1. Find an explicit formula for the general term of $\left\{\dfrac15,-\dfrac17,\dfrac19,-\dfrac{1}{11},\ldots\right\}$.
2. Find an explicit formula for the recursively defined sequence $a_1=\dfrac12$, $a_n = a_{n-1}+\left(\dfrac12\right)^n$ for $n\geq2$ (write out the first 3–4 terms first).

**The Formal Definition of Limit**

3. For each pair, decide whether $f$'s behaviour forces the corresponding statement about $a_n=f(n)$, and give a counterexample if not: (a) $f$ is bounded $\implies \{a_n\}$ is bounded; (b) $\{a_n\}$ is bounded $\implies f$ is bounded.
4. Write out, in full formal quantifier notation, the definition of "$\{a_n\}_{n=0}^\infty$ is divergent" (i.e., the **negation** of the convergence definition — be careful with how $\forall$/$\exists$ flip).
5. Decide whether $\forall\varepsilon\in(0,1),\exists n_0\in\mathbb{N},\forall n\in\mathbb{N}, n\geq n_0\implies|a_n-L|<\varepsilon$ (restricting $\varepsilon$ to $(0,1)$ instead of all positive reals) is equivalent to the standard definition. Justify.

**Monotonicity, Boundedness & Convergence**

6. Decide true or false, with a one-line justification or counterexample for each: (a) convergent $\implies$ bounded; (b) bounded $\implies$ convergent; (c) bounded + eventually monotonic $\implies$ convergent; (d) divergent $\implies$ unbounded.
7. Construct one example of a sequence that is monotonic, bounded, but divergent — or explain, citing a theorem, why no such example can exist.
8. Construct one example of a sequence that is bounded, not monotonic, and convergent.
9. Write a formal proof of: if $\{a_n\}$ is increasing and unbounded above, then $a_n\to\infty$. (Structure: state what you must show using the formal definition of $\to\infty$, then use "unbounded above" to produce the required $n_0$.)

**Growth Rates & the Big Theorem**

10. Evaluate $\displaystyle\lim_{n\to\infty}\frac{2^n+(2n)^2}{2^{n+1}+n^2}$.
11. Using the Big Theorem, construct a sequence $\{u_n\}$ such that $n^a \ll u_n$ for every $a\leq 2$, and $u_n \ll n^a$ for every $a>2$. (I.e., $u_n$ sits exactly "between" $n^2$ and $n^{2+\text{anything}}$ in growth rate.)
12. Evaluate $\displaystyle\lim_{n\to\infty}\frac{n^5+3^n}{n!}$.

---

## Answer Key & Misconception Notes (for tutor use — do not show student until after attempt)

| # | Answer | Common misconception |
|---|---|---|
| 1 | $a_n = \dfrac{(-1)^{n-1}}{2n+3}$ (denominators $5,7,9,11,\ldots = 2n+3$; signs start positive at $n=1$) | Getting the denominator pattern right but using $(-1)^n$ instead of $(-1)^{n-1}$, which flips every sign since the sequence starts *positive*, not negative. |
| 2 | $a_2=\frac12+\frac14=\frac34$, $a_3=\frac34+\frac18=\frac78$, pattern: $a_n = 1-\left(\frac12\right)^n$ | Guessing the pattern from only the first two terms instead of computing a third to confirm — $\frac34, \frac78$ alone could suggest several different formulas. |
| 3 | (a) True (given, no counterexample needed); (b) False — e.g. $f(x)=\sin(\pi x)\cdot x$ is unbounded on $[0,\infty)$, but $a_n=f(n)=\sin(\pi n)\cdot n = 0$ for every integer $n$, so $\{a_n\}$ is bounded (identically $0$) | Assuming boundedness must transfer symmetrically in both directions between $f$ and its sampled sequence, when only the function-to-sequence direction is guaranteed. |
| 4 | $\exists\varepsilon>0,\ \forall n_0\in\mathbb{N},\ \exists n\in\mathbb{N}$ with $n\geq n_0$ and $\lvert a_n-L\rvert\geq\varepsilon$ — and this negation must actually hold for **every** $L\in\mathbb{R}$ for the sequence to be divergent (not just one candidate $L$) | Only negating the inner quantifiers correctly but forgetting that "divergent" means this negated statement holds for *every* real $L$, not just failing to converge to one specific guessed value. |
| 5 | Equivalent — the same argument as Worked Example 3(d): restricting $\varepsilon$ to a smaller-but-still-arbitrarily-small range $(0,1)$ doesn't weaken the definition, since every $\varepsilon\geq1$ is automatically satisfied once smaller $\varepsilon$'s are controlled (a bound working for tiny $\varepsilon$ works even better for a larger one) | Assuming that shrinking the domain of $\varepsilon$ always changes the meaning of a $\forall\varepsilon$ statement — it only changes the meaning if it removes small $\varepsilon$'s (which are the ones that actually matter for a "closeness" definition), not large ones. |
| 6 | (a) True (Theorem 5.5); (b) False, e.g. $(-1)^n$; (c) True (Monotone Convergence Theorem); (d) False, e.g. $(-1)^n$ is divergent but bounded | Treating (a) "convergent $\Rightarrow$ bounded" and (b) "bounded $\Rightarrow$ convergent" as if one being true makes the other true — they are converses of each other and need separate justification. |
| 7 | No such example exists, by the Monotone Convergence Theorem: monotonic + bounded together are a **sufficient** condition for convergence, so any sequence satisfying both must converge — it cannot be divergent | Trying to construct a counterexample to a theorem instead of recognizing the question is really asking "why is this impossible," which should trigger citing the relevant theorem directly. |
| 8 | E.g. $a_n = \dfrac{(-1)^n}{n}$: bounded (between $-1$ and $1$), not monotonic (alternates sign), but $a_n\to0$ | Reaching for $(-1)^n$ alone (bounded, not monotonic, but divergent, not convergent) without the extra factor that forces it to shrink to a limit. |
| 9 | WTS: $\forall M\in\mathbb{R}, \exists n_0\in\mathbb{N}, \forall n\in\mathbb{N}, n\geq n_0\implies a_n>M$. Proof: Let $M\in\mathbb{R}$. Since $\{a_n\}$ is unbounded above, $M$ is not an upper bound, so $\exists n_0\in\mathbb{N}$ with $a_{n_0}>M$. Now let $n\geq n_0$. Since $\{a_n\}$ is increasing, $a_n\geq a_{n_0}>M$. Hence $a_n>M$, as required. $\blacksquare$ | Starting the proof by assuming $a_n\to\infty$ is what needs to be shown and working backwards without ever fixing an arbitrary $M$ first — the proof must begin "Let $M\in\mathbb{R}$" (matching the $\forall M$ in the statement) before anything else can be derived. |
| 10 | Divide by $2^n$: $\dfrac{1+4n^2/2^n}{2+n^2/2^n} \to \dfrac{1+0}{2+0}=\dfrac12$, using $n^2\ll 2^n$ (polynomial dominated by exponential) | Dividing by $n^2$ instead of $2^n$, which doesn't clear the exponential terms and leaves an indeterminate form instead of resolving the limit. |
| 11 | $u_n = n^2\ln n$ works: for $a<2$, $n^a \ll n^2 \ll n^2\ln n$ (since $\ln n\to\infty$, however slowly); for $a=2$, need $n^2\ll n^2\ln n$, true since $\ln n\to\infty$; for $a>2$, $n^2\ln n \ll n^a$ since $\ln n \ll n^{a-2}$ for any $a-2>0$ by the Big Theorem's $\ln n\ll n^a$ rule | Guessing $u_n=n^2$ itself, which fails the boundary requirement — the problem needs $u_n$ to sit strictly *between* $n^a$ for $a\leq2$ and $a>2$, which $n^2$ itself cannot do (it IS the $a=2$ case, not strictly between). |
| 12 | By the Big Theorem, $3^n \ll n!$ and $n^5 \ll n!$, so both numerator terms are dominated by the denominator: $\dfrac{n^5+3^n}{n!}\to 0$ | Trying to apply the Ratio Test or another series-convergence tool to what is really just a growth-rate comparison problem — at this stage (before series are introduced) the Big Theorem alone answers it directly. |
