# Week 8 — Subspaces & Bases

**Session length:** 3 hours
**Source:** Siefken, *MAT223 Workbook*, Module 6 (Subspaces & Bases)

---

## Page 1 — Introduction, Key Facts & Definitions

### Why this matters

Last time, we worked with **spans** and learned to test a set of vectors for **linear independence**. This week we ask a sharper question: what makes a set "closed" under linear combinations in the first place, and what is the *simplest possible* description of such a set? A line or plane through the origin can be written as the span of its direction vector(s), but a line or plane that does **not** pass through the origin cannot be written as a span — it can only be written as a *translated* span. Sets that behave like spans (closed under linear combinations) are called **subspaces**. Bases, built using linear independence, give us the simplest possible spanning set for a subspace.

### Definition: Subspace

A non-empty subset $V \subseteq \mathbb{R}^n$ is called a **subspace** if for all $\vec u, \vec v \in V$ and all scalars $k$ we have

- (i) $\vec u + \vec v \in V$; and
- (ii) $k\vec u \in V$.

Property (i) is called being **closed with respect to vector addition**, and property (ii) is called being **closed with respect to scalar multiplication**. Subspaces generalize the idea of flat spaces through the origin — lines, planes, volumes, and more. *(Module 6, "Subspaces & Bases" — Subspace definition.)*

### Fact: A Span Is Always a Subspace, and a Subspace Is Always a Span (Subspace-Span Theorem)

**Theorem (Subspace-Span).** Every subspace is a span and every span is a subspace. More precisely, $V \subseteq \mathbb{R}^n$ is a subspace if and only if $V = \operatorname{span} X$ for some set $X$.

The intuition: a linear combination of linear combinations is still a linear combination, so a span can never "escape itself" under addition or scalar multiplication — this is exactly what closure means. Spans give a **constructive** description of a subspace ("every point is built from these vectors"); subspaces give a **categorical** description of the same object ("these properties are satisfied"). *(Module 6, Subspace-Span Theorem.)*

### Fact: Special Subspaces of $\mathbb{R}^n$

There are two subspaces that are always available inside $\mathbb{R}^n$:

- $\mathbb{R}^n$ **itself** — it is non-empty, and linear combinations of vectors in $\mathbb{R}^n$ remain in $\mathbb{R}^n$.
- The **trivial subspace** $\{\vec 0\}$ — non-empty since $\vec 0 \in \{\vec 0\}$, and $\vec 0 + \vec 0 = \vec 0 \in \{\vec 0\}$, $\alpha \vec 0 = \vec 0 \in \{\vec 0\}$ for every scalar $\alpha$, so both closure conditions hold trivially. *(Module 6, "Special Subspaces.")*

### Definition: Basis

A **basis** for a subspace $V$ is a linearly independent set of vectors, $B$, so that $\operatorname{span} B = V$. In short: a basis for a subspace is a linearly independent set that spans that subspace. A basis is the simplest possible description of a subspace — not too big (no redundant vectors, since it's independent), not too small (it still spans everything). *(Module 6, "Bases.")*

### Key Fact: Properties of Bases

- **Bases are not unique.** Every subspace (except the trivial subspace) has more than one basis. (If $B = \{\vec b_1, \vec b_2, \ldots\}$ is a basis with at least one element, then $\{2\vec b_1, 2\vec b_2, \ldots\}$ is a different basis for the same subspace. The empty set is a basis for the trivial subspace.)
- **Coordinates are unique.** Given a basis for a subspace, every vector in the subspace can be written as a **unique** linear combination of the basis vectors. (This follows from linear independence.)
- **All bases for the same subspace have the same number of elements.** This fact is less obvious and takes more work to prove, so we accept it as given. *(Module 6, "Bases," Facts 1–3.)*

### Definition: Dimension

The **dimension** of a subspace $V$ is the number of elements in a basis for $V$. (By the fact above, this number does not depend on which basis you choose.) The dimension tells you the maximum number of linearly independent vectors that can simultaneously exist in $V$. This matches intuition: a line through $\vec 0$ is $1$-dimensional, a plane through $\vec 0$ is $2$-dimensional, and $\{\vec 0\}$ itself is $0$-dimensional (its basis is the empty set). *(Module 6, "Dimension.")*

### Definition: Standard Basis

The **standard basis** for $\mathbb{R}^n$ is the set $\{\vec e_1, \ldots, \vec e_n\}$, where $\vec e_i$ is the vector with a $1$ in its $i$-th coordinate and zeros elsewhere. The notation $\vec e_i$ is context-specific: if $\vec e_i \in \mathbb{R}^2$, it has exactly two coordinates; if $\vec e_i \in \mathbb{R}^{45}$, it has $45$ coordinates. *(Module 6, "Standard Basis.")*

---

## Pages 2–3 — Solved Examples

**Example 1 (Use the subspace test to show a set IS a subspace).** Let $V \subseteq \mathbb{R}^2$ be the complete solution to $x + 2y = 0$. Show $V$ is a subspace.

Let $\vec u = \begin{bmatrix} u_1 \\ u_2 \end{bmatrix}$ and $\vec v = \begin{bmatrix} v_1 \\ v_2 \end{bmatrix}$ be in $V$, and let $k$ be a scalar. By definition, $u_1 + 2u_2 = 0$ and $v_1 + 2v_2 = 0$.

*Non-empty:* $\vec 0 = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$ satisfies $x+2y=0$, so $\vec 0 \in V$ and $V$ is non-empty.

*(i) Closed under addition:* $\vec u + \vec v = \begin{bmatrix} u_1+v_1 \\ u_2+v_2 \end{bmatrix}$, and $(u_1+v_1)+2(u_2+v_2) = (u_1+2u_2)+(v_1+2v_2) = 0+0=0$. So $\vec u + \vec v \in V$.

*(ii) Closed under scalar multiplication:* $k\vec u = \begin{bmatrix} ku_1 \\ ku_2 \end{bmatrix}$, and $(ku_1)+2(ku_2) = k(u_1+2u_2)=k\cdot 0 = 0$. So $k\vec u \in V$.

Since $V$ is non-empty and satisfies (i) and (ii), $V$ is a subspace. $\blacksquare$

**Example 2 (Use the subspace test to show a set is NOT a subspace).** Let $W \subseteq \mathbb{R}^2$ be the line $\vec x = t\begin{bmatrix} 1 \\ 2 \end{bmatrix} + \begin{bmatrix} 1 \\ 1 \end{bmatrix}$. Determine whether $W$ is a subspace.

$W$ is **not** a subspace. Take $\vec v = \begin{bmatrix} 1 \\ 1 \end{bmatrix} \in W$ (using $t=0$). Then $0\vec v = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$. Is $\vec 0 \in W$? We'd need $t$ with $t+1=0$ and $2t+1=0$ simultaneously. The first equation gives $t=-1$; substituting into the second gives $2(-1)+1=-1 \neq 0$. No such $t$ exists, so $\vec 0 \notin W$. Since $\vec v \in W$ but $0\vec v \notin W$, $W$ is not closed under scalar multiplication, so $W$ is **not a subspace**. (Notice $W$ never contains $\vec 0$ at all, which already rules it out.) $\blacksquare$

**Example 3 (Prove a span is a subspace directly from the definition).** Let $S = \operatorname{span}\left\{ \begin{bmatrix} 2 \\ -1 \\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\ 1 \\ 3 \end{bmatrix} \right\} \subseteq \mathbb{R}^3$. Prove $S$ is a subspace using the definition.

Write $\vec v_1 = \begin{bmatrix} 2 \\ -1 \\ 0 \end{bmatrix}$, $\vec v_2 = \begin{bmatrix} 0 \\ 1 \\ 3 \end{bmatrix}$. Let $\vec u = a_1\vec v_1 + a_2\vec v_2$ and $\vec w = b_1 \vec v_1 + b_2 \vec v_2$ be arbitrary elements of $S$, and let $k$ be a scalar.

*Non-empty:* $\vec 0 = 0\vec v_1 + 0 \vec v_2 \in S$.

*(i)* $\vec u + \vec w = (a_1+b_1)\vec v_1 + (a_2+b_2)\vec v_2$ — this is again a linear combination of $\vec v_1, \vec v_2$, so $\vec u + \vec w \in S$.

*(ii)* $k\vec u = (ka_1)\vec v_1 + (ka_2)\vec v_2$ — again a linear combination of $\vec v_1, \vec v_2$, so $k\vec u \in S$.

Since $S$ is non-empty and satisfies (i) and (ii), $S$ is a subspace. (This is just the Subspace-Span Theorem's argument specialized to these two vectors — the same reasoning works for *any* span.) $\blacksquare$

**Example 4 (Find two different bases for a span with redundant vectors).** Let $\ell = \operatorname{span}\left\{ \begin{bmatrix} 1 \\ 2 \end{bmatrix}, \begin{bmatrix} -2 \\ -4 \end{bmatrix}, \begin{bmatrix} 1/2 \\ 1 \end{bmatrix} \right\}$. Find two different bases for $\ell$.

Notice
$$\begin{bmatrix} 1 \\ 2 \end{bmatrix} = -\frac{1}{2}\begin{bmatrix} -2 \\ -4 \end{bmatrix} = 2\begin{bmatrix} 1/2 \\ 1 \end{bmatrix},$$
so all three vectors are scalar multiples of each other. Therefore
$$\operatorname{span}\left\{\begin{bmatrix} 1 \\ 2 \end{bmatrix}\right\} = \operatorname{span}\left\{\begin{bmatrix} -2 \\ -4 \end{bmatrix}\right\} = \operatorname{span}\left\{\begin{bmatrix} 1/2 \\ 1 \end{bmatrix}\right\} = \operatorname{span}\left\{\begin{bmatrix} 1 \\ 2 \end{bmatrix}, \begin{bmatrix} -2 \\ -4 \end{bmatrix}, \begin{bmatrix} 1/2 \\ 1 \end{bmatrix}\right\} = \ell.$$
Since $\left\{\begin{bmatrix} 1 \\ 2 \end{bmatrix}\right\}$ is linearly independent (a single non-zero vector always is) and spans $\ell$, it is a basis for $\ell$. Similarly, $\left\{\begin{bmatrix} 1/2 \\ 1 \end{bmatrix}\right\}$ is another basis for $\ell$. $\blacksquare$

**Example 5 (Find a basis for and the dimension of a solution set).** Let $A = \{(x_1,x_2,x_3,x_4) : x_1+2x_2-x_3=0 \text{ and } x_1+6x_4=0\}$. Find a basis for and the dimension of $A$.

$A$ is the complete solution to the system $\begin{cases} x_1+2x_2-x_3=0 \\ x_1+6x_4=0 \end{cases}$, which in vector form is
$$\begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{bmatrix} = t\begin{bmatrix} 0 \\ 1/2 \\ 1 \\ 0 \end{bmatrix} + s\begin{bmatrix} -6 \\ 3 \\ 0 \\ 1 \end{bmatrix}.$$
So $A = \operatorname{span}\left\{\begin{bmatrix} 0 \\ 1/2 \\ 1 \\ 0 \end{bmatrix}, \begin{bmatrix} -6 \\ 3 \\ 0 \\ 1 \end{bmatrix}\right\}$. These two vectors are not scalar multiples of each other (check any coordinate ratio), so they are linearly independent. A linearly independent spanning set with two elements is a basis, so
$$B = \left\{\begin{bmatrix} 0 \\ 1/2 \\ 1 \\ 0 \end{bmatrix}, \begin{bmatrix} -6 \\ 3 \\ 0 \\ 1 \end{bmatrix}\right\}$$
is a basis for $A$, and $A$ is **two-dimensional**. $\blacksquare$

**Example 6 (Verify a given set IS a basis — check spanning AND independence).** Let $B = \left\{\begin{bmatrix} 1 \\ 0 \end{bmatrix}, \begin{bmatrix} 1 \\ 1 \end{bmatrix}\right\}$. Is $B$ a basis for $\mathbb{R}^2$?

*Spanning:* given an arbitrary $\begin{bmatrix} x \\ y \end{bmatrix} \in \mathbb{R}^2$, we need scalars $a,b$ with $a\begin{bmatrix} 1 \\ 0 \end{bmatrix} + b\begin{bmatrix} 1 \\ 1 \end{bmatrix} = \begin{bmatrix} x \\ y \end{bmatrix}$, i.e. $a+b=x$ and $b=y$. This gives $b=y$, $a=x-y$ — a solution always exists, so $B$ spans $\mathbb{R}^2$.

*Independence:* suppose $a\begin{bmatrix} 1 \\ 0 \end{bmatrix} + b\begin{bmatrix} 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$. Then $a+b=0$ and $b=0$, forcing $a=0$ too. Only the trivial solution exists, so $B$ is linearly independent.

Since $B$ spans $\mathbb{R}^2$ and is linearly independent, $B$ **is** a basis for $\mathbb{R}^2$. (This matches dimension: $\mathbb{R}^2$ is $2$-dimensional, and $B$ has exactly $2$ elements.) $\blacksquare$

**Example 7 (A spanning set that is NOT a basis, because it's dependent).** Let $\vec u = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}$, $\vec v = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}$, $\vec w = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}$, and $V = \operatorname{span}\{\vec u, \vec v, \vec w\}$. Is $\{\vec u, \vec v, \vec w\}$ a basis for $V$? If not, find one, and give $\dim V$.

Notice $\vec w = \vec u + \vec v$, i.e. $\vec u + \vec v - \vec w = \vec 0$ is a **non-trivial** linear combination equal to $\vec 0$ (coefficients $1,1,-1$, not all zero). So $\{\vec u, \vec v, \vec w\}$ is linearly **dependent**. Even though it spans $V$, a dependent set can never be a basis — so $\{\vec u, \vec v, \vec w\}$ is **not** a basis for $V$.

However, $\vec w$ is redundant (it's already a combination of $\vec u, \vec v$), so $\operatorname{span}\{\vec u,\vec v\} = \operatorname{span}\{\vec u,\vec v,\vec w\} = V$. Since $\vec u, \vec v$ are not scalar multiples of each other, $\{\vec u, \vec v\}$ is independent, and it spans $V$ — so $\{\vec u, \vec v\}$ **is** a basis for $V$, and $\dim V = 2$. (Geometrically, $V$ is the $xy$-plane inside $\mathbb{R}^3$.) $\blacksquare$

**Example 8 (Find the dimension of a span by uncovering a hidden dependency).** Let $\vec v_1 = \begin{bmatrix} 1 \\ 2 \\ 1 \end{bmatrix}$, $\vec v_2 = \begin{bmatrix} 2 \\ 1 \\ 3 \end{bmatrix}$, $\vec v_3 = \begin{bmatrix} 4 \\ 5 \\ 5 \end{bmatrix}$, and $T = \operatorname{span}\{\vec v_1, \vec v_2, \vec v_3\}$. Find a basis for and the dimension of $T$.

Unlike Example 4, it isn't obvious by inspection whether these vectors are dependent. Test whether $\vec v_3$ is a linear combination of $\vec v_1, \vec v_2$: we want $c_1, c_2$ with $c_1\vec v_1 + c_2 \vec v_2 = \vec v_3$, i.e.
$$c_1 + 2c_2 = 4, \qquad 2c_1+c_2=5, \qquad c_1+3c_2=5.$$
From the first equation, $c_1 = 4-2c_2$. Substituting into the second: $2(4-2c_2)+c_2=5 \Rightarrow 8-3c_2=5 \Rightarrow c_2=1$, so $c_1=2$. Check the third equation: $c_1+3c_2 = 2+3=5$ ✓ — consistent. So $\vec v_3 = 2\vec v_1 + \vec v_2$, meaning $\vec v_3$ is redundant and
$$T = \operatorname{span}\{\vec v_1, \vec v_2, \vec v_3\} = \operatorname{span}\{\vec v_1, \vec v_2\}.$$
Since $\vec v_1, \vec v_2$ are not scalar multiples of each other, $\{\vec v_1, \vec v_2\}$ is linearly independent, hence a basis for $T$. Therefore $\dim T = 2$. $\blacksquare$

---

## Pages 4–5 — Practice Problems (unsolved)

**The Subspace Test**

1. Let $T \subseteq \mathbb{R}^2$ be the complete solution to $3x - y = 0$. Prove or disprove that $T$ is a subspace.
2. Let $V \subseteq \mathbb{R}^2$ be the complete solution to $x - 5y - 1 = 0$. Prove or disprove that $V$ is a subspace.
3. Let $B \subseteq \mathbb{R}^2$ be given in vector form by $\vec x = t\begin{bmatrix} -3 \\ 4 \end{bmatrix}$. Prove or disprove that $B$ is a subspace.
4. Let $A \subseteq \mathbb{R}^2$ be given in vector form by $\vec x = t\begin{bmatrix} 5 \\ -7 \end{bmatrix} + \begin{bmatrix} 1 \\ 2 \end{bmatrix}$. Prove or disprove that $A$ is a subspace.
5. Let $Q = \{(x_1,x_2) : x_1 \geq 0\} \subseteq \mathbb{R}^2$. Determine whether $Q$ is a subspace. If not, say precisely which property fails and justify it with a specific counterexample.
6. Is the empty set $\{\}$ a subspace of $\mathbb{R}^2$? Justify your answer using the definition.

**Spans Are Always Subspaces**

7. Use the definition of subspace directly (not the Subspace-Span Theorem by name) to prove that $\operatorname{span}\left\{\begin{bmatrix} 0 \\ 1 \end{bmatrix}, \begin{bmatrix} 1 \\ 2 \end{bmatrix}\right\}$ is a subspace of $\mathbb{R}^2$.
8. Use the definition of subspace directly to prove that $\operatorname{span}\left\{\begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}, \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}, \begin{bmatrix} 2 \\ 0 \\ 0 \end{bmatrix}\right\}$ is a subspace of $\mathbb{R}^3$.

**Finding a Basis and Dimension**

9. Find a basis for and the dimension of $\operatorname{span}\left\{\begin{bmatrix} 2 \\ 3 \end{bmatrix}, \begin{bmatrix} -4 \\ -6 \end{bmatrix}, \begin{bmatrix} 1 \\ 3/2 \end{bmatrix}\right\}$.
10. Find a basis for and the dimension of $\operatorname{span}\left\{\begin{bmatrix} 1 \\ 0 \\ -2 \end{bmatrix}, \begin{bmatrix} 0 \\ 2 \\ 5 \end{bmatrix}, \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}\right\}$.
11. Find a basis for and the dimension of the complete solution to $x+3y+3z+7w=0$ in $\mathbb{R}^4$.
12. Give two examples of subspaces of $\mathbb{R}^4$ that are (i) $1$-dimensional and (ii) $3$-dimensional. Can you give an example of a subspace that is $0$-dimensional?

**Verifying a Basis**

13. Is $\left\{\begin{bmatrix} 2 \\ 6 \\ 1 \end{bmatrix}, \begin{bmatrix} 4 \\ 2 \\ 1 \end{bmatrix}, \begin{bmatrix} 6 \\ 8 \\ 2 \end{bmatrix}\right\}$ a basis for $\mathbb{R}^3$? Justify your answer.
14. Is $\left\{\begin{bmatrix} 2 \\ 3 \\ 5 \end{bmatrix}, \begin{bmatrix} 5 \\ -4 \\ 2 \end{bmatrix}\right\}$ a basis for $\mathbb{R}^3$? Justify your answer.

---

## Answer Key & Misconception Notes (for tutor use — do not show student until after attempt)

| # | Answer | Common misconception |
|---|---|---|
| 1 | $T$ **is** a subspace (homogeneous equation $y=3x$, a line through the origin; passes the subspace test). | Forgetting to explicitly verify non-emptiness / that $\vec 0$ satisfies the equation, and assuming "it's a line" is automatically enough without running the closure checks. |
| 2 | $V$ is **not** a subspace. It's not homogeneous: $\vec 0=(0,0)$ gives $0-0-1=-1\neq 0$, so $\vec 0 \notin V$; equivalently, scaling a point in $V$ by $k=0$ leaves $V$. | Seeing "it's a line" and assuming that's sufficient, without noticing the constant term $-1$ means it doesn't pass through the origin. |
| 3 | $B$ **is** a subspace — it is $\operatorname{span}\left\{\begin{bmatrix}-3\\4\end{bmatrix}\right\}$, a line through the origin. | Treating every "vector form" description as needing a full from-scratch subspace-test proof, instead of recognizing it's already a span (hence automatically a subspace). |
| 4 | $A$ is **not** a subspace. Taking $\vec v=(1,2)$ ($t=0$) $\in A$, $0\vec v=(0,0)$ requires $5t+1=0$ and $-7t+2=0$ simultaneously; $t=-\tfrac15$ solves the first but gives $\tfrac{17}{5}\neq 0$ in the second, so $\vec 0 \notin A$. | Thinking a "direction vector plus a shift" is still fine since it "looks like a span," missing that the added constant vector moves the whole line off the origin. |
| 5 | $Q$ is **not** a subspace — closed under addition (sum of nonnegatives is nonnegative) but fails scalar multiplication: $(1,0)\in Q$ but $(-1)(1,0)=(-1,0)\notin Q$. | Checking only closure under addition (which happens to hold here) and stopping, without testing a negative scalar. |
| 6 | The empty set is **not** a subspace — the definition explicitly requires non-emptiness. | Believing the empty set "vacuously" satisfies the closure conditions (no elements to violate them) and is therefore automatically a subspace. |
| 7 | Writing $\vec u = a_1(0,1)+a_2(1,2)$, $\vec v=b_1(0,1)+b_2(1,2)$: $\vec u+\vec v$ and $k\vec u$ are again combinations of the same two vectors, and $\vec 0$ is in the span, so it's a subspace. | Asserting closure without actually combining the coefficients (e.g. writing $(a_1+b_1)$, $(a_2+b_2)$) — skipping the algebra that makes the argument rigorous. |
| 8 | Same argument as #7 with three spanning vectors: sums and scalar multiples of combinations are still combinations of $\{(1,1,1),(1,0,0),(2,0,0)\}$, so it's a subspace. | Worrying that $(2,0,0)=2(1,0,0)$ being redundant somehow breaks the proof — redundancy among spanning vectors never affects whether the span is a subspace. |
| 9 | Basis $\left\{\begin{bmatrix}2\\3\end{bmatrix}\right\}$ (or any one nonzero vector from the set); $\dim = 1$, since all three vectors are scalar multiples of $(2,3)$. | Assuming the dimension automatically equals the number of vectors listed (here 3) instead of first checking for redundancy. |
| 10 | Basis $\left\{\begin{bmatrix}1\\0\\-2\end{bmatrix},\begin{bmatrix}0\\2\\5\end{bmatrix}\right\}$; $\dim=2$, since $\begin{bmatrix}1\\0\\-2\end{bmatrix}+\begin{bmatrix}0\\2\\5\end{bmatrix}=\begin{bmatrix}1\\2\\3\end{bmatrix}$ (the third vector is redundant). | Assuming three vectors in $\mathbb{R}^3$ must automatically form a basis for $\mathbb{R}^3$ (or at least be independent), without checking for a dependency. |
| 11 | The equation removes one degree of freedom from $\mathbb{R}^4$: parametrizing $y=s,z=t,w=r$, $x=-3s-3t-7r$ gives basis $\left\{\begin{bmatrix}-3\\1\\0\\0\end{bmatrix},\begin{bmatrix}-3\\0\\1\\0\end{bmatrix},\begin{bmatrix}-7\\0\\0\\1\end{bmatrix}\right\}$; $\dim = 3$. | Miscounting free variables when parametrizing, or forgetting that one homogeneous equation in $\mathbb{R}^4$ generically cuts the dimension down by exactly $1$ (from $4$ to $3$). |
| 12 | E.g. $1$-dim: $\operatorname{span}\{(1,0,0,0)\}$, $\operatorname{span}\{(1,1,0,0)\}$. $3$-dim: $\operatorname{span}\{e_1,e_2,e_3\}$, or the solution set to $x+y+z+w=0$. Yes: $\{\vec 0\}$ is $0$-dimensional (basis is the empty set). | Thinking the trivial subspace $\{\vec 0\}$ "doesn't count" as a subspace or has no well-defined dimension, instead of recognizing dimension $0$ with an empty basis. |
| 13 | **Not** a basis — dependent, since $(2,6,1)+(4,2,1)=(6,8,2)$, the third vector. | Assuming any $3$ vectors in $\mathbb{R}^3$ automatically form a basis just because the count matches the dimension, without checking independence. |
| 14 | **Not** a basis — only $2$ vectors, but every basis for $\mathbb{R}^3$ must have exactly $3$ elements (all bases have the same size, and the standard basis has $3$). | Checking that the two given vectors are independent (they are) and concluding that's enough, forgetting a basis for $\mathbb{R}^3$ specifically needs $3$ independent vectors, not just "some." |
