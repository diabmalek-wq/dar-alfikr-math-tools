# Week 10 — Linear Transformations

**Session length:** 3 hours
**Source:** Siefken, *MAT223 Workbook*, Module 9 (Linear Transformations)

---

## Page 1 — Introduction, Key Facts & Definitions

### Why this matters

A **transformation** (or **map**) is just another word for a function. Transformations show up any time you need to describe vectors *changing* — stretching, rotating, translating, and so on. Last week we represented systems of equations with matrices; this week we flip that around and use matrices to represent **functions between vector spaces**. Linear algebra's main focus is a special category of transformations, the **linear transformations**, because (i) we have a complete theory of them, and (ii) many non-linear transformations can be approximated by linear ones.

### Definition: Transformation and Image of a Set

*(Source subsection: Images of Sets)*

Let $L : \mathbb{R}^n \to \mathbb{R}^m$ be a transformation and let $X \subseteq \mathbb{R}^n$ be a set. The **image of the set $X$ under $L$**, denoted $L(X)$, is the set
$$L(X) = \{\vec y \in \mathbb{R}^m : \vec y = L(\vec x) \text{ for some } \vec x \in X\}.$$

In plain language, the image of a set $X$ under a transformation $L$ is the set of all outputs of $L$ when the inputs come from $X$. Images let us describe complicated geometric figures in terms of an original figure and a transformation — for example, if $R$ is rotation counter-clockwise by $30^\circ$ and $X$ is the filled-in unit square, then $R(X)$ is that same square rotated to meet the $x$-axis at a $30^\circ$ angle.

### Definition: Linear Transformation

*(Source subsection: Linear Transformations)*

Let $V$ and $W$ be subspaces. A function $T : V \to W$ is called a **linear transformation** if
$$T(\vec u + \vec v) = T(\vec u) + T(\vec v) \qquad \text{and} \qquad T(\alpha \vec v) = \alpha T(\vec v)$$
for all vectors $\vec u, \vec v \in V$ and all scalars $\alpha$.

In plain language, $T$ is linear if it distributes over addition and scalar multiplication — equivalently, $T$ distributes over linear combinations. Linear transformations include rotations, dilations (stretches), shears, and projections.

**Function notation reminder:** for transformations we use capital letters ($T$, not $t$), and parentheses around the input are optional — $T(\vec x)$ and $T\vec x$ mean the same thing. Also remember the distinction between a function and its output: "the transformation $T$" is valid; "the transformation $T(\vec x)$" is not — $T(\vec x)$ is a *vector* (the output), not a function.

### Key Fact: $T(\vec 0) = \vec 0$

*(Source subsection: Linear Transformations)*

If $T : \mathbb{R}^n \to \mathbb{R}^m$ is a linear transformation, then $T(\vec 0) = \vec 0$.

*Proof.* Let $\vec v \in \mathbb{R}^n$. Since $0\vec v = \vec 0$, linearity gives
$$T(\vec 0) = T(0\vec v) = 0\,T(\vec v) = \vec 0. \qquad \blacksquare$$

This is a one-way test: if $T(\vec 0) \neq \vec 0$, then $T$ is **automatically not linear** — no further work needed. (But $T(\vec 0) = \vec 0$ alone does *not* guarantee $T$ is linear.)

### Key Fact: Linear Transformations Preserve Lines, Parallel Lines, and Subspaces

*(Source subsection: Linear Transformations)*

If $T : \mathbb{R}^n \to \mathbb{R}^m$ is a linear transformation, then:

- $T$ takes **lines to lines (or points).** If $\ell$ is the line $\vec x = t\vec d + \vec p$, then $T(\ell) = \{t\,T(\vec d) + T(\vec p)\}$, which is a line if $T(\vec d) \neq \vec 0$, or a single point if $T(\vec d) = \vec 0$.
- $T$ takes **parallel lines to parallel lines (or points)**, since two parallel lines share the same direction vector $\vec d$, and so do their images.
- $T$ takes **subspaces to subspaces.** If $V \subseteq \mathbb{R}^n$ is a subspace, $T(V)$ is closed under addition and scalar multiplication because $T(\vec u) + T(\vec v) = T(\vec u + \vec v) \in T(V)$ and $\alpha T(\vec u) = T(\alpha \vec u) \in T(V)$.

### Method: Proving Linearity (or Non-Linearity)

*(Source subsection: Linear Transformations and Proofs)*

**To prove $T$ IS linear**, you must show both properties hold for *every* possible input and scalar at once. The standard template is:

> *Proof.* Let $\vec x, \vec y \in \mathbb{R}^n$ and let $\alpha$ be a scalar. By applying the definition of $T$, we see
> $$T(\vec x + \vec y) = \text{application(s) of the definition} = T(\vec x) + T(\vec y).$$
> Similarly, $T(\alpha \vec x) = \text{application(s) of the definition} = \alpha T(\vec x)$.
> Since $T$ satisfies the two properties of a linear transformation, $T$ is a linear transformation. $\blacksquare$

Starting with "let $\vec x, \vec y \in \mathbb{R}^n$ and let $\alpha$ be a scalar" lets you argue about *all* vectors and scalars simultaneously, while still having named objects to compute with.

**To prove $T$ is NOT linear**, you only need **one** counterexample — a single pair of vectors, or a single vector and scalar, for which one of the two properties fails. (Be careful: showing a property fails for *one* input does not mean it fails for *all* inputs.)

### Definition: Matrix Transformation

*(Source subsection: Matrix Transformations)*

For an $m \times n$ matrix $M$, define $T : \mathbb{R}^n \to \mathbb{R}^m$ by $T(\vec x) = M\vec x$. Because $T$ is defined by a matrix, $T$ is called a **matrix transformation**. All matrix transformations are linear transformations, and most linear transformations are matrix transformations.

**A matrix and a linear transformation are not the same thing.** A matrix is a box of numbers with no meaning until we give it one; a linear transformation is a function that inputs and outputs vectors. Correct ways to describe $T$ using $M$: "the transformation defined by $T(\vec x) = M\vec x$," "the transformation given by multiplication by $M$," "the matrix transformation given by $M$," or "the linear transformation whose matrix is $M$." You would never say "$T$ *is* $M$," just like you would never say the function $f(x) = 2x$ *is* the number $2$.

### Fact: Finding the Standard Matrix of a Linear Transformation

*(Source subsection: Finding a Matrix for a Linear Transformation — Siefken calls the object below simply "a matrix for $T$"; this course also uses the common name **the standard matrix of $T$** for the same object.)*

Let $T : \mathbb{R}^n \to \mathbb{R}^m$ be a linear transformation. Since $T$ inputs vectors with $n$ coordinates and outputs vectors with $m$ coordinates, any matrix for $T$ must be $m \times n$. In general:

1. Create an $m \times n$ matrix of unknown entries.
2. Use known input-output pairs of $T$ to set up a system of equations in the unknowns.
3. Solve the system.

**Shortcut using the standard basis vectors.** If you know where $T$ sends each standard basis vector $\vec e_1, \dots, \vec e_n$, you get the standard matrix immediately with no system to solve. This is because if $M$ is the standard matrix, $M\vec e_i$ equals the $i$-th column of $M$ (a fact from matrix-vector multiplication). Since $T(\vec e_i) = M \vec e_i$, it follows that
$$\text{column } i \text{ of the standard matrix} = T(\vec e_i).$$
So the standard matrix of $T$ is simply
$$M = \begin{bmatrix} T(\vec e_1) & T(\vec e_2) & \cdots & T(\vec e_n) \end{bmatrix}.$$
Once you have $M$, computing $T(\vec x)$ for any specific $\vec x$ is just the matrix-vector product $M\vec x$.

### Key Fact: The "Look" of a Linear Transformation and Named Examples

*(Source subsections: Linear Transformations; "The 'look' of a Linear Transformation")*

Images of a grid under a linear transformation still look like a grid of parallel lines (straight, evenly spaced) — never curved or bent. Named linear transformations you will work with include **rotations**, **dilations (stretches)**, **shears**, **projections**, and **reflections**. A **translation** (sliding every vector by a fixed nonzero vector, e.g. $T(\vec x) = \vec x + 3\vec e_1$) is a common example of a transformation that is **not** linear, since $T(\vec 0) \neq \vec 0$.

---

## Pages 2–3 — Solved Examples

**Example 1 (Verify a transformation IS linear).** Let $S : \mathbb{R}^2 \to \mathbb{R}^2$ be defined by $S\begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 2x \\ y \end{bmatrix}$. Determine whether $S$ is a linear transformation.

Let $\vec u = \begin{bmatrix} u_1 \\ u_2 \end{bmatrix}$, $\vec v = \begin{bmatrix} v_1 \\ v_2 \end{bmatrix}$ be vectors, and let $\alpha$ be a scalar. We check both properties.

**Additivity:**
$$S(\vec u + \vec v) = S\begin{bmatrix} u_1+v_1 \\ u_2+v_2 \end{bmatrix} = \begin{bmatrix} 2u_1+2v_1 \\ u_2+v_2 \end{bmatrix} = \begin{bmatrix} 2u_1 \\ u_2 \end{bmatrix} + \begin{bmatrix} 2v_1 \\ v_2 \end{bmatrix} = S(\vec u) + S(\vec v).$$

**Scalar multiplication:**
$$S(\alpha \vec u) = \begin{bmatrix} 2\alpha u_1 \\ \alpha u_2 \end{bmatrix} = \alpha \begin{bmatrix} 2u_1 \\ u_2 \end{bmatrix} = \alpha S(\vec u).$$

Since $S$ satisfies both properties for arbitrary $\vec u, \vec v, \alpha$, $S$ is a linear transformation. $\blacksquare$

**Example 2 (Show a transformation is NOT linear — additivity fails).** Let $T : \mathbb{R}^2 \to \mathbb{R}^2$ be defined by $T\begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} x \\ y+4 \end{bmatrix}$. Show $T$ is not linear.

Notice $T(\vec u + \vec v) = \begin{bmatrix} u_1+v_1 \\ u_2+v_2+4 \end{bmatrix}$ doesn't look like $T(\vec u) + T(\vec v) = \begin{bmatrix} u_1+v_1 \\ u_2+v_2+8 \end{bmatrix}$, so we look for a counterexample. Using $\vec e_1 = \begin{bmatrix}1\\0\end{bmatrix}$ and $\vec e_2 = \begin{bmatrix}0\\1\end{bmatrix}$:
$$T(\vec e_1 + \vec e_2) = T\begin{bmatrix}1\\1\end{bmatrix} = \begin{bmatrix}1\\5\end{bmatrix} \neq \begin{bmatrix}1\\4\end{bmatrix}+\begin{bmatrix}0\\5\end{bmatrix} = T(\vec e_1) + T(\vec e_2).$$
Since a required property of linearity is violated, $T$ is not a linear transformation. $\blacksquare$

**Example 3 (Show a transformation is NOT linear — scalar multiplication fails).** Let $T : \mathbb{R}^n \to \mathbb{R}^n$ be defined by $T(\vec x) = \vec x + \vec e_1$. Show $T$ is not linear.

We show $T$ does not distribute over scalar multiplication. Observe
$$T(2\vec 0) = T(\vec 0) = \vec e_1 \neq 2\vec e_1 = 2T(\vec 0).$$
Therefore $T$ cannot be a linear transformation. $\blacksquare$

(Note: this also follows instantly from the Key Fact on Page 1, since $T(\vec 0) = \vec e_1 \neq \vec 0$.)

**Example 4 (General proof that a transformation IS linear).** Let $T : \mathbb{R}^n \to \mathbb{R}^n$ be defined by $T(\vec v) = 2\vec v$. Show $T$ is linear.

*Proof.* Let $\vec x, \vec y \in \mathbb{R}^n$ and let $\alpha$ be a scalar. By the definition of $T$,
$$T(\vec x + \vec y) = 2(\vec x + \vec y) = 2\vec x + 2\vec y = T(\vec x) + T(\vec y).$$
Similarly,
$$T(\alpha \vec x) = 2(\alpha \vec x) = \alpha(2\vec x) = \alpha T(\vec x).$$
Since $T$ satisfies both properties of a linear transformation, $T$ is linear. $\blacksquare$

**Example 5 (Find the standard matrix from a formula, using input-output pairs).** Let $T : \mathbb{R}^2 \to \mathbb{R}^2$ be defined by $T\begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 2x+y \\ x \end{bmatrix}$. Find a matrix $M$ for $T$.

Since $T : \mathbb{R}^2 \to \mathbb{R}^2$, $M$ is $2 \times 2$. Let $M = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$. We know $T\begin{bmatrix}1\\1\end{bmatrix} = \begin{bmatrix}3\\1\end{bmatrix}$ and $T\begin{bmatrix}0\\1\end{bmatrix} = \begin{bmatrix}1\\0\end{bmatrix}$. Since $M\vec x = T(\vec x)$ for all $\vec x$:
$$M\begin{bmatrix}1\\1\end{bmatrix} = \begin{bmatrix}a+b\\c+d\end{bmatrix} = \begin{bmatrix}3\\1\end{bmatrix}, \qquad M\begin{bmatrix}0\\1\end{bmatrix} = \begin{bmatrix}b\\d\end{bmatrix} = \begin{bmatrix}1\\0\end{bmatrix}.$$
This gives the system $a+b=3,\ c+d=1,\ b=1,\ d=0$, which solves to $a=2,\ b=1,\ c=1,\ d=0$. So
$$M = \begin{bmatrix} 2 & 1 \\ 1 & 0 \end{bmatrix}.$$

**Example 6 (Find the standard matrix from standard basis images, then compute $T(\vec x)$).** Suppose $T : \mathbb{R}^2 \to \mathbb{R}^2$ is linear with $T(\vec e_1) = \begin{bmatrix}2\\1\end{bmatrix}$ and $T(\vec e_2) = \begin{bmatrix}0\\-3\end{bmatrix}$. Find the standard matrix of $T$, then compute $T\begin{bmatrix}4\\-2\end{bmatrix}$.

By the shortcut on Page 1, the columns of the standard matrix are exactly the images of the standard basis vectors:
$$M = \begin{bmatrix} T(\vec e_1) & T(\vec e_2) \end{bmatrix} = \begin{bmatrix} 2 & 0 \\ 1 & -3 \end{bmatrix}.$$
Now compute $T(\vec x) = M\vec x$ for $\vec x = \begin{bmatrix}4\\-2\end{bmatrix}$:
$$T\begin{bmatrix}4\\-2\end{bmatrix} = \begin{bmatrix} 2 & 0 \\ 1 & -3 \end{bmatrix}\begin{bmatrix}4\\-2\end{bmatrix} = \begin{bmatrix} 2(4)+0(-2) \\ 1(4)+(-3)(-2) \end{bmatrix} = \begin{bmatrix} 8 \\ 10 \end{bmatrix}.$$

**Example 7 (Standard matrix of a geometric transformation — rotation).** Let $R : \mathbb{R}^2 \to \mathbb{R}^2$ be rotation counter-clockwise by $90^\circ$. Find the standard matrix of $R$.

We find $R(\vec e_1)$ and $R(\vec e_2)$ directly by picturing the rotation. $\vec e_1 = \begin{bmatrix}1\\0\end{bmatrix}$ points along the positive $x$-axis (angle $0^\circ$); rotating it $90^\circ$ counter-clockwise sends it to the positive $y$-axis: $R(\vec e_1) = \begin{bmatrix}0\\1\end{bmatrix}$. $\vec e_2 = \begin{bmatrix}0\\1\end{bmatrix}$ points along the positive $y$-axis ($90^\circ$); rotating it another $90^\circ$ sends it to $180^\circ$, i.e. the negative $x$-axis: $R(\vec e_2) = \begin{bmatrix}-1\\0\end{bmatrix}$. By the standard-basis shortcut,
$$R = \begin{bmatrix} R(\vec e_1) & R(\vec e_2) \end{bmatrix} = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}.$$
Check: $R\begin{bmatrix}1\\1\end{bmatrix} = \begin{bmatrix}-1\\1\end{bmatrix}$, which is indeed $\begin{bmatrix}1\\1\end{bmatrix}$ rotated $90^\circ$ counter-clockwise.

**Example 8 (Standard matrix of a geometric transformation — reflection).** Let $F : \mathbb{R}^2 \to \mathbb{R}^2$ be reflection over the line $y = x$. Find the standard matrix of $F$.

Reflecting a point over the line $y=x$ swaps its coordinates: $F\begin{bmatrix}x\\y\end{bmatrix} = \begin{bmatrix}y\\x\end{bmatrix}$. So $F(\vec e_1) = F\begin{bmatrix}1\\0\end{bmatrix} = \begin{bmatrix}0\\1\end{bmatrix}$ and $F(\vec e_2) = F\begin{bmatrix}0\\1\end{bmatrix} = \begin{bmatrix}1\\0\end{bmatrix}$. By the shortcut,
$$F = \begin{bmatrix} F(\vec e_1) & F(\vec e_2) \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}.$$

---

## Pages 4–5 — Practice Problems (unsolved)

**Verifying Linearity**

1. For each transformation below, prove whether or not it is a linear transformation.
   (a) $A : \mathbb{R}^2 \to \mathbb{R}^2$ defined by $A\begin{bmatrix}x\\y\end{bmatrix} = \begin{bmatrix}-x\\y\end{bmatrix}$.
   (b) $B : \mathbb{R}^2 \to \mathbb{R}^2$ defined by $B\begin{bmatrix}x\\y\end{bmatrix} = \begin{bmatrix}-x-1\\y\end{bmatrix}$.
2. Let $C : \mathbb{R}^2 \to \mathbb{R}^2$ send all vectors strictly above the $x$-axis to $\vec 0$, and all vectors on or below the $x$-axis to $-\vec e_2$. Prove whether or not $C$ is linear.
3. Let $S : \mathbb{R}^n \to \mathbb{R}^m$ and $T : \mathbb{R}^n \to \mathbb{R}^m$ be linear transformations, and define $R : \mathbb{R}^n \to \mathbb{R}^m$ by $R(\vec x) = S(\vec x) + T(\vec x)$. Prove that $R$ is also linear.

**Finding the Standard Matrix from a Formula**

4. Find the standard matrix of $T : \mathbb{R}^2 \to \mathbb{R}^2$ defined by $T\begin{bmatrix}x\\y\end{bmatrix} = \begin{bmatrix}3x-y\\2y\end{bmatrix}$.
5. Find the standard matrix of $T : \mathbb{R}^3 \to \mathbb{R}^2$ defined by $T\begin{bmatrix}x\\y\\z\end{bmatrix} = \begin{bmatrix}x+2y-z\\3y+z\end{bmatrix}$.

**Standard Matrix from Standard Basis Images, and Computing $T(\vec x)$**

6. Let $M = \begin{bmatrix} 1 & -2 & 3 \\ -4 & 5 & -6 \end{bmatrix}$ and let $T_M$ be the corresponding matrix transformation.
   (a) Determine the domain and codomain of $T_M$.
   (b) Calculate $T_M\begin{bmatrix}2\\-1\\1\end{bmatrix}$.
   (c) Find the images of the standard basis vectors of the domain under $T_M$.
7. A linear transformation $T : \mathbb{R}^2 \to \mathbb{R}^2$ satisfies $T(\vec e_1) = \begin{bmatrix}2\\1\end{bmatrix}$ and $T(\vec e_2) = \begin{bmatrix}0\\-3\end{bmatrix}$. Find the standard matrix of $T$, then compute $T\begin{bmatrix}4\\-2\end{bmatrix}$.
8. A linear transformation $T : \mathbb{R}^3 \to \mathbb{R}^3$ satisfies $T(\vec e_1) = \begin{bmatrix}1\\0\\-1\end{bmatrix}$, $T(\vec e_2) = \begin{bmatrix}2\\1\\0\end{bmatrix}$, $T(\vec e_3) = \begin{bmatrix}0\\-1\\3\end{bmatrix}$. Find the standard matrix of $T$, then compute $T\begin{bmatrix}1\\2\\-1\end{bmatrix}$.

**Geometric Linear Transformations**

9. Find the standard matrix for $S : \mathbb{R}^2 \to \mathbb{R}^2$, the transformation that doubles every vector.
10. Find the standard matrix for $R : \mathbb{R}^2 \to \mathbb{R}^2$, rotation clockwise by $135^\circ$.
11. Let $T : \mathbb{R}^2 \to \mathbb{R}^2$ translate every vector by $3\vec e_1$. Does $T$ have a standard matrix? Justify your answer.
12. Find the standard matrix for (a) $P : \mathbb{R}^2 \to \mathbb{R}^2$, projection onto the $y$-axis, and (b) $F : \mathbb{R}^2 \to \mathbb{R}^2$, reflection over the line $y=x$.

**Concept Checks**

13. Let $T : \mathbb{R}^2 \to \mathbb{R}^2$ be the transformation that doubles the length of its input, $T(\vec v) = 2\vec v$. The following statements about $T$ are each incorrect or incomplete. Fix each one so it is correct and complete.
    (a) "$T = \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix}$."
    (b) "Since $T\vec x = 2\vec x$ for every $\vec x$, we can say $T = 2$."
    (c) "$T$ is a linear transformation because $2(\vec x+\vec y) = 2\vec x+2\vec y$."
14. Determine whether each statement is true or false. Justify your answer using a Page 1 fact or a counterexample.
    (a) Every transformation from $\mathbb{R}^n$ to $\mathbb{R}^m$ can be represented by a matrix.
    (b) The image of a subspace under a linear transformation is not a subspace.
    (c) A transformation that takes every vector in the domain to $\vec 0$ is not linear.
    (d) Every matrix is a linear transformation.
    (e) Parallel lines stay parallel under a linear transformation.

---

## Answer Key & Misconception Notes (for tutor use — do not show student until after attempt)

| # | Answer | Common misconception |
|---|---|---|
| 1 | (a) $A$ is linear: $A(\vec u+\vec v)=A(\vec u)+A(\vec v)$ and $A(\alpha\vec u)=\alpha A(\vec u)$ check out directly (standard matrix $\begin{bmatrix}-1&0\\0&1\end{bmatrix}$). (b) $B$ is **not** linear: $B(\vec 0) = \begin{bmatrix}-1\\0\end{bmatrix} \neq \vec 0$, so it fails immediately. | Students try to verify $B$ with the full additivity/scalar-multiplication computation instead of noticing the fast $T(\vec 0)\neq \vec 0$ shortcut; they also sometimes think "linear" means "looks like a line/has a $+$ or $-$ sign," confusing it with linear *equations*. |
| 2 | Not linear. E.g. $C(\vec 0,1) = \vec 0$ (above axis) but $C\big((-1)(0,1)\big) = C(0,-1) = -\vec e_2 \neq (-1)\vec 0 = \vec 0$, so scalar multiplication fails. | Students test only additivity and forget to also check scalar multiplication (or vice versa) — one property holding is not enough; a transformation must satisfy **both**. |
| 3 | $R(\vec x+\vec y) = S(\vec x+\vec y)+T(\vec x+\vec y) = S(\vec x)+S(\vec y)+T(\vec x)+T(\vec y) = R(\vec x)+R(\vec y)$; $R(\alpha\vec x)=S(\alpha\vec x)+T(\alpha\vec x)=\alpha S(\vec x)+\alpha T(\vec x)=\alpha R(\vec x)$. So $R$ is linear. | Students assume the result "obviously" follows because $S$ and $T$ are each linear, without actually writing out the algebra that combines the two linearity assumptions — this proof requires *using* the hypothesis that $S,T$ are linear, not just asserting it. |
| 4 | $M = \begin{bmatrix} 3 & -1 \\ 0 & 2 \end{bmatrix}$ | Reading off coefficients from the formula in the wrong order/sign — e.g. writing the $y$-coefficient of the first row as $+1$ instead of $-1$, or transposing rows and columns. |
| 5 | $M = \begin{bmatrix} 1 & 2 & -1 \\ 0 & 3 & 1 \end{bmatrix}$ | Forgetting that the codomain is $\mathbb{R}^2$ (not $\mathbb{R}^3$) so the matrix must be $2\times 3$, not $3\times 3$ or $3\times 2$; mixing up which dimension is rows vs. columns. |
| 6 | (a) domain $\mathbb{R}^3$, codomain $\mathbb{R}^2$. (b) $T_M\begin{bmatrix}2\\-1\\1\end{bmatrix} = \begin{bmatrix}7\\-19\end{bmatrix}$. (c) $T_M(\vec e_1)=\begin{bmatrix}1\\-4\end{bmatrix}$, $T_M(\vec e_2)=\begin{bmatrix}-2\\5\end{bmatrix}$, $T_M(\vec e_3)=\begin{bmatrix}3\\-6\end{bmatrix}$. | Swapping domain/codomain (thinking a $2\times 3$ matrix maps $\mathbb{R}^2\to\mathbb{R}^3$ instead of $\mathbb{R}^3\to\mathbb{R}^2$); in (b), sign errors multiplying negative entries. |
| 7 | $M=\begin{bmatrix}2&0\\1&-3\end{bmatrix}$; $T\begin{bmatrix}4\\-2\end{bmatrix}=\begin{bmatrix}8\\10\end{bmatrix}$. | Placing $T(\vec e_1)$ and $T(\vec e_2)$ as *rows* of $M$ instead of *columns*. |
| 8 | $M=\begin{bmatrix}1&2&0\\0&1&-1\\-1&0&3\end{bmatrix}$; $T\begin{bmatrix}1\\2\\-1\end{bmatrix}=\begin{bmatrix}5\\3\\-4\end{bmatrix}$. | Same row/column mix-up as #7, compounded by arithmetic slips when there are 3 columns to track; forgetting a negative sign from $T(\vec e_1)$'s third entry. |
| 9 | $S=\begin{bmatrix}2&0\\0&2\end{bmatrix}$ | Writing $2I$ correctly but then second-guessing it and adding off-diagonal terms because "doubling" sounds like it should mix $x$ and $y$. |
| 10 | $R=\begin{bmatrix}-\frac{\sqrt2}{2}&\frac{\sqrt2}{2}\\-\frac{\sqrt2}{2}&-\frac{\sqrt2}{2}\end{bmatrix}$ | Using the counter-clockwise rotation matrix formula with a positive angle instead of accounting for the clockwise direction (sign errors on the off-diagonal entries), or forgetting $135^\circ$ is in the second quadrant so both coordinates of $R(\vec e_1)$ are negative. |
| 11 | No standard matrix exists, because $T(\vec 0)=3\vec e_1\neq \vec 0$, so $T$ is not linear, and every matrix transformation sends $\vec 0\mapsto\vec 0$. | Trying to force a matrix anyway (e.g. by writing translation as $\vec x+3\vec e_1$ in matrix form), not recognizing that translations are the classic example of a non-linear transformation. |
| 12 | (a) $P=\begin{bmatrix}0&0\\0&1\end{bmatrix}$. (b) $F=\begin{bmatrix}0&1\\1&0\end{bmatrix}$. | For (a), projecting onto the $y$-axis but keeping the $x$-coordinate (writing $\begin{bmatrix}1&0\\0&1\end{bmatrix}$ or $\begin{bmatrix}1&0\\0&0\end{bmatrix}$ instead of zeroing out $x$); for (b), confusing reflection over $y=x$ (swap coordinates) with reflection over the $x$-axis or $y$-axis. |
| 13 | (a) Correct statement: "The standard matrix of $T$ is $\begin{bmatrix}2&0\\0&2\end{bmatrix}$," not "$T$ equals" the matrix. (b) Correct: $T$ is the transformation $T(\vec x)=2\vec x$; it cannot be set equal to the scalar $2$, since $T$ is a function and $2$ is a number. (c) A complete proof needs both properties, stated for arbitrary $\vec x,\vec y,\alpha$: $T(\vec x+\vec y)=2(\vec x+\vec y)=2\vec x+2\vec y=T(\vec x)+T(\vec y)$ and $T(\alpha\vec x)=2(\alpha\vec x)=\alpha(2\vec x)=\alpha T(\vec x)$. | This is exactly the matrix-vs-transformation confusion the module warns about — students conflate "$T$" (the function), "$T(\vec x)$" (a vector, the output), and "the matrix of $T$" (a box of numbers) as if they were interchangeable; in (c) students also often stop after checking additivity alone and forget scalar multiplication is a separate, required property. |
| 14 | (a) False — only linear transformations have a matrix (e.g. translation from #11 has none). (b) False — it **is** always a subspace (Page 1 Key Fact). (c) False — the zero transformation $T(\vec x)=\vec 0$ is linear (check both properties: they hold trivially). (d) False — a matrix is a box of numbers; it *induces* a linear transformation via $\vec x \mapsto M\vec x$, but is not itself a function. (e) True (or the images degenerate to points). | For (b) and (c) students often answer by gut feeling ("that sounds wrong/right") instead of checking against the specific Page 1 theorem or definition that settles it; for (d) students blur the matrix/transformation distinction again. |
