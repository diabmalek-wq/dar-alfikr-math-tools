# Week 6 — Spans, Translated Spans, and Linear (In)dependence

**Session length:** 3 hours
**Source:** Siefken, *MAT223 Workbook*, Module 3 (Spans, Translated Spans, and Linear Independence/Dependence)

---

## Page 1 — Introduction, Key Facts & Definitions

### Recap from Week 5 (Module 2)

Last week you learned to write lines and planes in **vector form**, $\vec x = t\vec d + \vec p$ or $\vec x = t\vec d_1 + s\vec d_2 + \vec p$, and you already know what a **linear combination** is from Weeks 4–5. This week reuses both ideas: the set of *all* linear combinations of some vectors is called their **span**, and vector form is really just a span (when $\vec p = \vec 0$) or a span shifted by a point (when $\vec p \neq \vec 0$). We also formalize when a set of direction vectors is "genuinely necessary" — this is **linear independence**.

### Why this matters

Vector form is not unique, and not every list of direction vectors is a valid one — a redundant direction vector can silently turn a "plane" into a line. Spans give us the language to describe *every* line, plane, and point through the origin in one unified way, and linear independence tells us exactly when a list of direction vectors is not carrying dead weight.

### Definition: Span

*(Source subsection: Span)*

The **span** of a set of vectors $V$ is the set of all linear combinations of vectors in $V$. That is,
$$\operatorname{span} V = \{\vec v : \vec v = \alpha_1 \vec v_1 + \alpha_2 \vec v_2 + \cdots + \alpha_n \vec v_n \text{ for some } \vec v_1, \vec v_2, \ldots, \vec v_n \in V \text{ and scalars } \alpha_1,\alpha_2,\ldots,\alpha_n\}.$$
Additionally, we define $\operatorname{span}\{\} = \{\vec 0\}$. We may also use *span* as a verb: if $\operatorname{span}\{\vec u,\vec v\} = \mathbb{R}^2$, we say $\{\vec u,\vec v\}$ **spans** $\mathbb{R}^2$.

### Fact: Every Span Passes Through the Origin

*(Source subsection: Representing Lines & Planes as Spans)*

If $X = \operatorname{span}\{\vec v_1,\ldots,\vec v_n\}$, then $\vec 0 = 0\vec v_1 + \cdots + 0\vec v_n \in X$, so every span contains the origin. Conversely, every line/plane/volume *through the origin* can be written as a span: if $\ell$ has vector form $\vec x = t\vec d + \vec 0$, then $\ell = \operatorname{span}\{\vec d\}$; if $P$ has vector form $\vec x = t\vec d_1+s\vec d_2+\vec 0$, then $P = \operatorname{span}\{\vec d_1,\vec d_2\}$.

**Takeaway.** Lines and planes through the origin, and *only* lines and planes through the origin, can be expressed as spans.

### Definition: Set Addition

*(Source subsection: Set Addition)*

If $A$ and $B$ are sets of vectors, the **set sum** of $A$ and $B$, denoted $A+B$, is
$$A + B = \{\vec x : \vec x = \vec a + \vec b \text{ for some } \vec a \in A \text{ and } \vec b \in B\}.$$
Set sums behave differently from ordinary sums (e.g. $A + \{\} = \{\}$). Note: if $A$ is a set and $\vec p$ is a single vector, "$A + \vec p$" does not make mathematical sense — it must be written $A + \{\vec p\}$.

### Definition: Translated Span

*(Source subsection: Translated Spans)*

If a line/plane/volume $Q$ has vector form $\vec x = t\vec d_1 + s\vec d_2 + \vec p$ (with $\vec p \neq \vec 0$ possibly), then using set addition,
$$Q = \operatorname{span}\{\vec d_1,\vec d_2\} + \{\vec p\}.$$
This is called $Q$ expressed as a **translated span**. It is exactly $\operatorname{span}\{\vec d_1,\vec d_2\}$ shifted (translated) by the fixed vector $\vec p$.

### Key Fact: Translated Spans Describe All Lines and Planes

*(Source subsection: Translated Spans)*

Unlike a plain span (which always passes through the origin), a translated span can describe a line/plane anywhere. **All lines and planes, whether through the origin or not, can be expressed as translated spans.** This is why translated-span notation is an alternative to vector form: they describe exactly the same sets.

### Definition: Linearly Dependent & Independent (Geometric)

*(Source subsection: Linear Independence & Linear Dependence)*

We say the vectors $\vec v_1, \vec v_2, \ldots, \vec v_n$ are **linearly dependent** if for at least one $i$,
$$\vec v_i \in \operatorname{span}\{\vec v_1,\ldots,\vec v_{i-1},\vec v_{i+1},\ldots,\vec v_n\}.$$
Otherwise, they are called **linearly independent**. In words: the vectors are linearly dependent exactly when at least one of them is *redundant* — removing it does not shrink the span.

### Definition: Trivial Linear Combination

*(Source subsection: Linear Independence & Linear Dependence)*

The linear combination $\alpha_1\vec v_1 + \cdots + \alpha_n \vec v_n$ is called **trivial** if $\alpha_1 = \cdots = \alpha_n = 0$. If at least one $\alpha_i \neq 0$, the linear combination is called **non-trivial**.

### Definition: Linearly Dependent & Independent (Algebraic)

*(Source subsection: Linear Independence & Linear Dependence)*

The vectors $\vec v_1,\vec v_2,\ldots,\vec v_n$ are **linearly dependent** if there is a non-trivial linear combination of $\vec v_1,\ldots,\vec v_n$ that equals the zero vector. Otherwise they are **linearly independent**.

The geometric definition is easy to visualize but hard to use directly (you'd have to check every vector against the span of all the others). The algebraic definition only requires analyzing solutions to *one* vector equation, so it is the one used for actual computation.

### Theorem: The Geometric and Algebraic Definitions Are Equivalent

*(Source subsection: Linear Independence & Linear Dependence)*

The geometric definition of linear (in)dependence and the algebraic definition of linear (in)dependence describe exactly the same sets of vectors. (Geometrically dependent $\iff$ algebraically dependent.)

### Definition: Homogeneous System

*(Source subsection: Linear Independence and Unique Solutions)*

A system of linear equations or a vector equation in the variables $\alpha_1,\ldots,\alpha_n$ is called **homogeneous** if it takes the form
$$\alpha_1\vec v_1 + \alpha_2\vec v_2 + \cdots + \alpha_n\vec v_n = \vec 0,$$
i.e. the right side of the equation is $\vec 0$. A homogeneous system always has at least the **trivial solution** $\alpha_1 = \cdots = \alpha_n = 0$.

### Theorem: Linear Independence and Unique Solutions

*(Source subsection: Linear Independence and Unique Solutions)*

The vectors $\vec v_1,\ldots,\vec v_n$ are linearly independent **if and only if** the homogeneous equation $\alpha_1\vec v_1 + \cdots + \alpha_n\vec v_n = \vec 0$ has a **unique solution** (namely, only the trivial one). If a non-trivial solution exists, it is one of *infinitely many* non-trivial solutions (any scalar multiple of a non-trivial solution is again a solution).

**Practical use:** to decide whether $\vec a, \vec b, \vec c$ are linearly dependent, you may either (i) find a non-trivial solution to $x\vec a+y\vec b+z\vec c=\vec 0$, or (ii) merely show that this equation has *more than one* solution — whichever is easier.

### Key Fact: Linear Independence and Vector Form

*(Source subsection: Linear Independence and Vector Form)*

The equation $\vec x = t_1\vec d_1 + t_2\vec d_2$ represents a genuine **plane** in vector form exactly when $\{\vec d_1,\vec d_2\}$ is linearly independent (equivalently, $\vec d_1,\vec d_2$ are non-zero and non-parallel). Likewise $\vec x = t\vec d$ represents a **line** exactly when $\{\vec d\}$ is linearly independent (i.e. $\vec d \neq \vec 0$), and $\vec x = t_1\vec d_1+t_2\vec d_2+t_3\vec d_3$ represents a genuine **volume** exactly when $\{\vec d_1,\vec d_2,\vec d_3\}$ is linearly independent. If the direction vectors are linearly *dependent*, one or more of them is redundant, and the equation collapses to describe a lower-dimensional object (or just a point) instead.

**Takeaway.** When writing an object in vector form, the direction vectors must always be linearly independent — otherwise the vector form is misleading about the object's dimension.

---

## Pages 2–3 — Solved Examples

**Example 1 (Describing the span of two vectors that turn out to be parallel).** Let $\vec u = \begin{bmatrix}-1\\2\end{bmatrix}$ and $\vec v = \begin{bmatrix}1\\-2\end{bmatrix}$. Find $\operatorname{span}\{\vec u,\vec v\}$.

By definition, $\operatorname{span}\{\vec u,\vec v\} = \{\vec x : \vec x = \alpha\vec u+\beta\vec v \text{ for some } \alpha,\beta \in \mathbb{R}\}$. We need to determine for which $x,y$ the vector equation $\begin{bmatrix}x\\y\end{bmatrix} = \alpha\begin{bmatrix}-1\\2\end{bmatrix}+\beta\begin{bmatrix}1\\-2\end{bmatrix}$ is consistent. Reading off coordinates:
$$x = -\alpha+\beta, \qquad y = 2\alpha-2\beta.$$
Adding $2$ times the first equation to the second: $2x+y = 0$, so $y=-2x$. Therefore, whenever $\begin{bmatrix}x\\y\end{bmatrix}$ makes the system consistent, $\begin{bmatrix}x\\y\end{bmatrix} = \begin{bmatrix}t\\-2t\end{bmatrix} = t\vec v$ for some $t$. Thus
$$\operatorname{span}\{\vec u,\vec v\} = \{\vec x : \vec x = t\vec v \text{ for some } t\} = \operatorname{span}\{\vec v\},$$
which is a line through the origin with direction $\vec v$ (equation $y=-2x$). $\vec u$ was redundant — notice $\vec u = -\vec v$. $\blacksquare$

---

**Example 2 (Describing the span of three vectors in $\mathbb{R}^3$).** Let $\vec a = \begin{bmatrix}1\\2\\1\end{bmatrix}$, $\vec b = \begin{bmatrix}0\\1\\0\end{bmatrix}$, $\vec c = \begin{bmatrix}1\\1\\2\end{bmatrix}$. Show that $\mathbb{R}^3 = \operatorname{span}\{\vec a,\vec b,\vec c\}$.

If the equation $\vec x = \begin{bmatrix}x\\y\\z\end{bmatrix} = \alpha_1\vec a+\alpha_2\vec b+\alpha_3\vec c$ is *always* consistent (no matter the values of $x,y,z$), then every vector in $\mathbb{R}^3$ is a linear combination of $\vec a,\vec b,\vec c$. Reading off coordinates gives the system
$$x = \alpha_1+\alpha_3, \qquad y = 2\alpha_1+\alpha_2+\alpha_3, \qquad z = \alpha_1+2\alpha_3.$$
Solving, we find
$$\alpha_1 = 2x-z, \qquad \alpha_2 = -3x+y+z, \qquad \alpha_3 = -x+z$$
is always a solution, regardless of $x,y,z$ (check: $\alpha_1+\alpha_3 = (2x-z)+(-x+z)=x$ ✓, and similarly for the other two coordinates). Since the system is consistent for *every* $(x,y,z)$, we conclude $\operatorname{span}\{\vec a,\vec b,\vec c\} = \mathbb{R}^3$. $\blacksquare$

---

**Example 3 (Is a given vector in the span of two others?).** Let $\vec u = \begin{bmatrix}1\\2\end{bmatrix}$, $\vec v = \begin{bmatrix}2\\-1\end{bmatrix}$, $\vec w = \begin{bmatrix}5\\5\end{bmatrix}$. Is $\vec w \in \operatorname{span}\{\vec u,\vec v\}$?

*Reasoning.* $\vec w$ is in the span of $\vec u,\vec v$ if and only if the vector equation $\alpha\vec u+\beta\vec v = \vec w$ is consistent — exactly the same technique we used in Weeks 3–5 to solve a linear system.
$$\alpha\begin{bmatrix}1\\2\end{bmatrix}+\beta\begin{bmatrix}2\\-1\end{bmatrix}=\begin{bmatrix}5\\5\end{bmatrix} \;\Longrightarrow\; \begin{cases}\alpha+2\beta=5\\2\alpha-\beta=5\end{cases}.$$
From the second equation, $\beta = 2\alpha-5$. Substituting into the first: $\alpha+2(2\alpha-5)=5 \Rightarrow 5\alpha-10=5 \Rightarrow \alpha=3$, so $\beta=2(3)-5=1$. **Check:** $3\begin{bmatrix}1\\2\end{bmatrix}+1\begin{bmatrix}2\\-1\end{bmatrix} = \begin{bmatrix}3\\6\end{bmatrix}+\begin{bmatrix}2\\-1\end{bmatrix}=\begin{bmatrix}5\\5\end{bmatrix}$ ✓. Since a solution exists, $\vec w \in \operatorname{span}\{\vec u,\vec v\}$. $\blacksquare$

*(Bonus remark, following the same method as Example 1: since $\vec u,\vec v$ are not parallel, one can check that the system $\alpha\vec u+\beta\vec v = \begin{bmatrix}x\\y\end{bmatrix}$ is consistent for every $x,y$, so in fact $\operatorname{span}\{\vec u,\vec v\} = \mathbb{R}^2$ — every vector, not just $\vec w$, lies in this span.)*

---

**Example 4 (A translated span for a line not through the origin).** Recall $\ell \subseteq \mathbb{R}^2$ is the line described by $3x+y=6$. Describe $\ell$ as a translated span.

*Reasoning.* $(0,6)$ does not make $3x+y=0$, so $\ell$ is not a span by itself — we need a translated span. First find vector form: by guess-and-check, $P=(0,6)$ and $Q=(1,3)$ both satisfy $3x+y=6$, so $\vec d = Q-P = \begin{bmatrix}1\\-3\end{bmatrix}$, giving
$$\vec x = t\begin{bmatrix}1\\-3\end{bmatrix}+\begin{bmatrix}0\\6\end{bmatrix}.$$
Reading this off as a translated span,
$$\ell = \operatorname{span}\left\{\begin{bmatrix}1\\-3\end{bmatrix}\right\} + \left\{\begin{bmatrix}0\\6\end{bmatrix}\right\}.$$
It would be incorrect to write "$\ell = \operatorname{span}\{(1,-3)\} + (0,6)$" — the second term must be a *set* $\{(0,6)\}$, not a bare vector, since set addition needs two sets. $\blacksquare$

---

**Example 5 (Testing linear independence of two vectors, algebraically).** Let $\vec p = \begin{bmatrix}3\\1\end{bmatrix}$, $\vec q = \begin{bmatrix}-1\\2\end{bmatrix}$. Determine whether $\{\vec p,\vec q\}$ is linearly independent.

*Reasoning.* By the algebraic definition, we need to determine whether $\alpha\vec p+\beta\vec q=\vec 0$ has *only* the trivial solution.
$$\alpha\begin{bmatrix}3\\1\end{bmatrix}+\beta\begin{bmatrix}-1\\2\end{bmatrix}=\begin{bmatrix}0\\0\end{bmatrix} \;\Longrightarrow\; \begin{cases}3\alpha-\beta=0\\\alpha+2\beta=0\end{cases}.$$
From the first equation, $\beta=3\alpha$. Substituting into the second: $\alpha+2(3\alpha)=0 \Rightarrow 7\alpha=0 \Rightarrow \alpha=0$, and then $\beta=3(0)=0$. The **only** solution is $\alpha=\beta=0$ — the trivial one. By the Linear Independence and Unique Solutions theorem, $\{\vec p,\vec q\}$ is **linearly independent**. $\blacksquare$

---

**Example 6 (Spotting linear dependence by inspection — geometric definition).** Let $\vec a = \begin{bmatrix}1\\2\end{bmatrix}$, $\vec b = \begin{bmatrix}2\\3\end{bmatrix}$, $\vec c = \begin{bmatrix}4\\6\end{bmatrix}$, $\vec d = \begin{bmatrix}4\\5\end{bmatrix}$. Determine whether $\{\vec a,\vec b,\vec c,\vec d\}$ is linearly independent or dependent.

By inspection, $\vec c = 2\vec b$. Therefore $\vec c \in \operatorname{span}\{\vec a,\vec b,\vec d\}$ (in fact just $\operatorname{span}\{\vec b\}$ alone), so by the geometric definition $\{\vec a,\vec b,\vec c,\vec d\}$ is **linearly dependent** — $\vec c$ is redundant, and $\operatorname{span}\{\vec a,\vec b,\vec c,\vec d\} = \operatorname{span}\{\vec a,\vec b,\vec d\}$. $\blacksquare$

---

**Example 7 (Testing linear independence of three vectors, and finding the actual dependency relation).** Let $\vec u = \begin{bmatrix}1\\2\end{bmatrix}$, $\vec v = \begin{bmatrix}2\\3\end{bmatrix}$, $\vec w = \begin{bmatrix}4\\5\end{bmatrix}$. Use the algebraic definition to determine whether $\{\vec u,\vec v,\vec w\}$ is linearly independent or dependent. If dependent, exhibit an explicit non-trivial relation.

We need to determine whether there is a non-trivial solution to $x\vec u+y\vec v+z\vec w=\vec 0$. This vector equation is equivalent to the system
$$\begin{cases}x+2y+4z=0\\2x+3y+5z=0.\end{cases}$$
Row-reducing (two equations, three unknowns — a free variable is guaranteed), the complete solution set can be expressed as
$$\begin{bmatrix}x\\y\\z\end{bmatrix} = t\begin{bmatrix}2\\-3\\1\end{bmatrix}.$$
In particular, $(x,y,z)=(2,-3,1)$ is a non-trivial solution, so $\{\vec u,\vec v,\vec w\}$ is **linearly dependent**. The explicit relation is
$$2\vec u - 3\vec v + \vec w = \vec 0,$$
which we can verify directly: $2\begin{bmatrix}1\\2\end{bmatrix}-3\begin{bmatrix}2\\3\end{bmatrix}+\begin{bmatrix}4\\5\end{bmatrix} = \begin{bmatrix}2\\4\end{bmatrix}-\begin{bmatrix}6\\9\end{bmatrix}+\begin{bmatrix}4\\5\end{bmatrix}=\begin{bmatrix}0\\0\end{bmatrix}$ ✓. Equivalently, solving for $\vec w$: $\vec w = -2\vec u+3\vec v$, showing $\vec w$ is the redundant vector. $\blacksquare$

---

**Example 8 (Harder application: are two planes, given in vector form, actually the same plane?).** The planes $P$ and $Q$ are given in vector form by
$$P: \vec x = t\begin{bmatrix}1\\2\\1\end{bmatrix}+s\begin{bmatrix}2\\2\\1\end{bmatrix}, \qquad Q: \vec x = t\begin{bmatrix}3\\4\\2\end{bmatrix}+s\begin{bmatrix}2\\2\\1\end{bmatrix}.$$
Determine if $P$ and $Q$ are the same plane, using spans and linear dependence instead of the Module 2 method.

*Reasoning.* Let $\vec a_1 = \begin{bmatrix}1\\2\\1\end{bmatrix}$, $\vec a_2 = \begin{bmatrix}2\\2\\1\end{bmatrix}$ be direction vectors for $P$, and $\vec b_1 = \begin{bmatrix}3\\4\\2\end{bmatrix}$, $\vec b_2 = \begin{bmatrix}2\\2\\1\end{bmatrix}$ be direction vectors for $Q$, so $P=\operatorname{span}\{\vec a_1,\vec a_2\}$ and $Q=\operatorname{span}\{\vec b_1,\vec b_2\}$. Note $\vec a_2 = \vec b_2$ already. By definition $P=Q$ requires (i) every point of $P$ is a point of $Q$, and (ii) every point of $Q$ is a point of $P$.

For (i): observe $\vec a_1 = \vec b_1 - \vec b_2$ (check: $\begin{bmatrix}3\\4\\2\end{bmatrix}-\begin{bmatrix}2\\2\\1\end{bmatrix}=\begin{bmatrix}1\\2\\1\end{bmatrix}=\vec a_1$ ✓), so $\vec a_1 \in \operatorname{span}\{\vec b_1,\vec b_2\}=Q$. Also $\vec a_2 = \vec b_2 \in Q$ trivially. Since $Q$ is itself a span, every linear combination of $\vec a_1,\vec a_2$ (i.e. every point of $P$) is a linear combination of $\vec b_1,\vec b_2$, hence lies in $Q$. So $P \subseteq Q$.

For (ii): $\vec b_2 = \vec a_2 \in P$, and $\vec b_1 = \vec a_1+\vec a_2 \in \operatorname{span}\{\vec a_1,\vec a_2\}=P$. By the same reasoning, $Q \subseteq P$.

Since $P\subseteq Q$ and $Q\subseteq P$, we conclude $P=Q$: they are the **same plane**. $\blacksquare$

---

## Pages 4–5 — Practice Problems (unsolved)

**Spans — Describing Spans and Testing Membership**

1. Let $\vec v = \begin{bmatrix}2\\4\end{bmatrix}$. Describe $\operatorname{span}\{\vec v\}$ geometrically, and write it in set-builder notation.
2. Let $\vec p = \begin{bmatrix}1\\2\end{bmatrix}$ and $\vec q = \begin{bmatrix}-2\\-4\end{bmatrix}$. Are $\vec p$ and $\vec q$ parallel? Describe $\operatorname{span}\{\vec p,\vec q\}$.
3. Let $\vec u = \begin{bmatrix}2\\1\end{bmatrix}$ and $\vec v = \begin{bmatrix}-1\\3\end{bmatrix}$. Is $\vec w = \begin{bmatrix}7\\4\end{bmatrix}$ in $\operatorname{span}\{\vec u,\vec v\}$?
4. Let $\vec a = \begin{bmatrix}1\\0\\1\end{bmatrix}$, $\vec b = \begin{bmatrix}0\\1\\1\end{bmatrix}$, $\vec c = \begin{bmatrix}1\\1\\0\end{bmatrix}$. Determine whether $\operatorname{span}\{\vec a,\vec b,\vec c\} = \mathbb{R}^3$.

**Translated Spans**

5. Express the line $\ell: 3x+y=6$ (in $\mathbb{R}^2$) as a translated span.
6. Express the plane $x-2y+z=5$ (in $\mathbb{R}^3$) as a translated span.
7. Let $X = \operatorname{span}\left\{\begin{bmatrix}1\\0\\-2\end{bmatrix}\right\} + \left\{\begin{bmatrix}3\\1\\0\end{bmatrix}\right\}$. Is $\begin{bmatrix}4\\1\\-2\end{bmatrix}$ in $X$?

**Linear Independence & Dependence**

8. Determine whether $\left\{\begin{bmatrix}2\\-1\end{bmatrix},\begin{bmatrix}-6\\3\end{bmatrix}\right\}$ is linearly independent or dependent, using the algebraic definition.
9. Let $\vec v_1 = \begin{bmatrix}1\\1\\1\end{bmatrix}$, $\vec v_2 = \begin{bmatrix}2\\0\\1\end{bmatrix}$, $\vec v_3 = \begin{bmatrix}0\\2\\1\end{bmatrix}$. Determine whether $\{\vec v_1,\vec v_2,\vec v_3\}$ is linearly independent or dependent. If dependent, exhibit an explicit non-trivial linear combination equal to $\vec 0$.
10. Let $\vec a = \begin{bmatrix}1\\-1\\2\end{bmatrix}$, $\vec b = \begin{bmatrix}3\\0\\1\end{bmatrix}$, $\vec c = \begin{bmatrix}-1\\-2\\3\end{bmatrix}$. Using the geometric definition (look for a pattern before doing algebra), determine whether $\{\vec a,\vec b,\vec c\}$ is linearly independent or dependent, and if dependent, state the relation.

**Independence, Vector Form & Conceptual Reasoning**

11. For each statement, say whether it is true or false, and justify your answer.
    (a) If $\vec v_1$ can be written as a linear combination of $\vec v_2$ and $\vec v_3$, then $\{\vec v_1,\vec v_2,\vec v_3\}$ is linearly dependent.
    (b) If $\{\vec v_1,\vec v_2,\vec v_3\}$ is linearly independent, then none of $\vec v_1,\vec v_2,\vec v_3$ can be $\vec 0$.
    (c) If $\vec v_1$ is not a scalar multiple of $\vec v_2$, then $\{\vec v_1,\vec v_2\}$ is linearly independent.
    (d) Every set of vectors containing $\vec 0$ is linearly independent.
12. Let $\vec d_1 = \begin{bmatrix}1\\2\\-1\end{bmatrix}$ and $\vec d_2 = \begin{bmatrix}-2\\-4\\2\end{bmatrix}$. Does $\vec x = t\vec d_1+s\vec d_2$ represent a plane? If not, what object does it actually represent, and how would you write that object correctly (as a span)?
13. Can a set of $4$ vectors in $\mathbb{R}^3$ ever be linearly independent? Explain your reasoning by relating the number of vectors to the number of equations and unknowns in the corresponding homogeneous system (recall Weeks 3–5: what does having more unknowns than equations guarantee about a homogeneous system's solution set?).

---

## Answer Key & Misconception Notes (for tutor use — do not show student until after attempt)

| # | Answer | Common misconception |
|---|---|---|
| 1 | $\operatorname{span}\{\vec v\}$ is the line $y=2x$ through the origin; $\{\vec x : \vec x = t\begin{bmatrix}2\\4\end{bmatrix} \text{ for some } t \in \mathbb{R}\}$ | Writing "$y=2x$" as the final answer without the set-builder/span description, or forgetting the "for some $t$" — treating span as a single vector instead of an infinite set. |
| 2 | $\vec q = -2\vec p$, so they are parallel; $\operatorname{span}\{\vec p,\vec q\} = \operatorname{span}\{\vec p\}$, the line $y=2x$ through the origin | Assuming two (nonzero) vectors always span all of $\mathbb{R}^2$ without first checking whether one is a scalar multiple of the other. |
| 3 | Yes; $\alpha=3,\ \beta=1$ gives $3\vec u+1\vec v=\vec w$ | Setting up the linear system correctly but only checking that one coordinate equation is satisfied, instead of verifying the found $\alpha,\beta$ against *both* coordinates. |
| 4 | Yes, $\operatorname{span}\{\vec a,\vec b,\vec c\}=\mathbb{R}^3$; e.g. $\alpha_1=\tfrac{x-y+z}{2},\ \alpha_2=\tfrac{-x+y+z}{2},\ \alpha_3=\tfrac{x+y-z}{2}$ solves the system for every $x,y,z$ | Assuming any 3 vectors in $\mathbb{R}^3$ automatically span all of $\mathbb{R}^3$ just because "3 vectors, 3 dimensions" — without actually checking the system is consistent (the vectors could be dependent). |
| 5 | $\ell = \operatorname{span}\left\{\begin{bmatrix}1\\-3\end{bmatrix}\right\}+\left\{\begin{bmatrix}0\\6\end{bmatrix}\right\}$ | Writing everything inside one span, e.g. "$\operatorname{span}\{\vec d,\vec p\}$", instead of using set addition — this is wrong because $\ell$ does not pass through the origin, so it cannot be a plain span at all. |
| 6 | $\operatorname{span}\left\{\begin{bmatrix}1\\0\\-1\end{bmatrix},\begin{bmatrix}0\\1\\2\end{bmatrix}\right\}+\left\{\begin{bmatrix}0\\0\\5\end{bmatrix}\right\}$ (using points $(0,0,5),(1,0,4),(0,1,7)$) | Forgetting to check that the two chosen direction vectors are non-parallel (linearly independent) before writing the translated span — picking 3 points that are secretly collinear collapses the "plane" into a line. |
| 7 | Yes; $t=1$ gives $\begin{bmatrix}1+3\\0+1\\-2+0\end{bmatrix}=\begin{bmatrix}4\\1\\-2\end{bmatrix}$ | Solving for $t$ using only the first coordinate and declaring membership without checking that the *same* $t$ also satisfies the second and third coordinates. |
| 8 | Linearly dependent: $\begin{bmatrix}-6\\3\end{bmatrix}=-3\begin{bmatrix}2\\-1\end{bmatrix}$, so $\alpha\vec p+\beta\vec q=\vec 0$ has non-trivial solutions (e.g. $\alpha=3,\beta=1$) | Since neither vector is $\vec 0$, assuming they must be independent — missing that a nonzero scalar-multiple relationship between two vectors is exactly what forces dependence. |
| 9 | Linearly dependent; $2\vec v_1 - \vec v_2 - \vec v_3 = \vec 0$ | After row-reducing and finding a free variable, concluding "dependent" without going back and writing the actual non-trivial linear combination that equals $\vec 0$ — the problem specifically asks for that relation. |
| 10 | Linearly dependent; $\vec c = 2\vec a-\vec b$, i.e. $2\vec a-\vec b-\vec c=\vec 0$ | Checking only whether any two of the three vectors are scalar multiples of each other, seeing none are, and wrongly concluding independence — with 3 or more vectors, dependence can come from a combination of *all* of them, not just a pairwise relationship. |
| 11 | (a) True (b) True (c) True (d) False — e.g. $\{\vec 0\}$ is linearly dependent, since $1\cdot\vec 0=\vec 0$ is a non-trivial combination equal to $\vec 0$ | For (c): over-generalizing "not a scalar multiple" to sets of 3 or more vectors — that pairwise check only guarantees independence for a set of exactly *two* vectors. For (d): assuming $\vec 0$ is "harmless" in a set rather than recognizing it always creates a non-trivial relation ($1\cdot\vec 0=\vec 0$). |
| 12 | No — $\vec d_2=-2\vec d_1$, so $\{\vec d_1,\vec d_2\}$ is dependent; the equation only represents the line $\operatorname{span}\{\vec d_1\}$, i.e. $\operatorname{span}\left\{\begin{bmatrix}1\\2\\-1\end{bmatrix}\right\}$ | Assuming two direction vectors that "look different" (different numbers) must automatically give a plane, without checking whether one is a scalar multiple of the other first. |
| 13 | No — the homogeneous system $x_1\vec v_1+x_2\vec v_2+x_3\vec v_3+x_4\vec v_4=\vec 0$ has 4 unknowns but only 3 equations (one per coordinate in $\mathbb{R}^3$), so it always has a free variable and hence infinitely many solutions, including a non-trivial one — forcing dependence | Thinking linear independence is about the vectors "looking sufficiently different" from each other rather than about counting equations versus unknowns in the corresponding homogeneous system; also forgetting this argument works for *any* set of more vectors than the dimension of the space. |
