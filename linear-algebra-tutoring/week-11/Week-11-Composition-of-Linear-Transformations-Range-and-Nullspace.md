# Week 11 — Composition of Linear Transformations; Range & Nullspace

**Session length:** 3 hours
**Source:** Siefken, *MAT223 Workbook*, Module 10 (The Composition of Linear Transformations) and Module 11 (Range & Nullspace of a Linear Transformation)

---

## Page 1 — Introduction, Key Facts & Definitions

### Why this matters

Last week we learned that every linear transformation $T : \mathbb{R}^n \to \mathbb{R}^m$ has a **standard matrix**, and that $T(\vec x) = M\vec x$. This week we ask two new questions. First: what happens when we do one linear transformation *after* another — and how does that relate to the standard matrices we already know how to find? Second: every linear transformation has two special subspaces attached to it, its **range** and its **null space**, which measure everything the transformation can output and everything it destroys (sends to $\vec 0$). Understanding these two subspaces — and the single number, the **rank**, that ties them together — is one of the central goals of the rest of this course.

### Definition: Composition of Functions

*(Source subsection: Module 10 introduction)*

Let $f : A \to B$ and $g : B \to C$. The **composition of $g$ and $f$**, notated $g \circ f$, is the function $h : A \to C$ defined by
$$h(x) = g \circ f(x) = g\big(f(x)\big).$$

In plain language: to compute $g \circ f(x)$, you apply $f$ **first**, then apply $g$ to the result. (Siefken's own example: if $X$ = putting on socks and $S$ = putting on shoes, then "getting dressed" is $D = S \circ X$ — you must do $X$ before $S$.) We can build a complicated transformation out of simple pieces by composing them, and, conversely, we can sometimes understand a complicated transformation by breaking it into a composition of simple ones.

### Key Fact: The Composition of Linear Transformations Is Linear

*(Source subsection: Compositions and Matrix Products — used implicitly whenever the module treats $T = A \circ B$ as a linear transformation with its own standard matrix)*

If $S : \mathbb{R}^n \to \mathbb{R}^m$ and $T : \mathbb{R}^m \to \mathbb{R}^p$ are linear transformations, then $T \circ S : \mathbb{R}^n \to \mathbb{R}^p$ is also a linear transformation.

*Proof.* Let $\vec x, \vec y \in \mathbb{R}^n$ and let $\alpha$ be a scalar. Since $S$ is linear,
$$(T \circ S)(\vec x + \vec y) = T\big(S(\vec x + \vec y)\big) = T\big(S(\vec x) + S(\vec y)\big) = T(S(\vec x)) + T(S(\vec y)) = (T \circ S)(\vec x) + (T \circ S)(\vec y),$$
where the middle step uses that $T$ is linear. Similarly,
$$(T \circ S)(\alpha \vec x) = T\big(S(\alpha \vec x)\big) = T\big(\alpha S(\vec x)\big) = \alpha\, T(S(\vec x)) = \alpha (T \circ S)(\vec x).$$
Since $T \circ S$ satisfies both properties, it is a linear transformation. $\blacksquare$

This is why $T \circ S$ always has its own standard matrix, exactly like any other linear transformation.

### Theorem: The Standard Matrix of a Composition Is a Matrix Product

*(Source subsection: Compositions and Matrix Products)*

If $P : \mathbb{R}^a \to \mathbb{R}^b$ and $Q : \mathbb{R}^c \to \mathbb{R}^a$ are matrix transformations with standard matrices $M_P$ and $M_Q$, then $P \circ Q$ is a matrix transformation whose standard matrix is the matrix product $M_P M_Q$.

**Why:** Since $P\vec x = M_P \vec x$ and $Q \vec x = M_Q \vec x$, we have $(P \circ Q)(\vec x) = P(Q(\vec x)) = M_P(M_Q \vec x)$. Matrix multiplication is associative, so $M_P(M_Q\vec x) = (M_P M_Q)\vec x$. Thus $M_P M_Q$ is a matrix for $P \circ Q$.

**Order matters.** $Q$ is applied first (its output must be a valid input for $P$, so $Q : \mathbb{R}^c \to \mathbb{R}^a$ and $P : \mathbb{R}^a \to \mathbb{R}^b$), and its matrix $M_Q$ sits on the **right** of the product, exactly mirroring the order of the $\circ$ symbol in $P \circ Q$. Since function composition is not commutative in general ("you must put on your socks before your shoes"), matrix multiplication is not commutative either — $M_P M_Q$ and $M_Q M_P$ are generally different matrices (and may not even both be defined).

### Definition: Range (Image) of a Linear Transformation

*(Source subsection: Range)*

The **range** (or **image**) of a linear transformation $T : V \to W$ is the set of vectors that $T$ can output:
$$\operatorname{range}(T) = \{\vec y \in W : \vec y = T\vec x \text{ for some } \vec x \in V\}.$$

This is exactly the image of the **entire domain** under $T$. Unlike the range of an arbitrary function, the range of a linear transformation is always a subspace.

### Theorem: The Range of a Linear Transformation Is a Subspace; the Rank of a Linear Transformation

*(Source subsection: Range)*

Let $T : \mathbb{R}^n \to \mathbb{R}^m$ be a linear transformation. Then $\operatorname{range}(T) \subseteq \mathbb{R}^m$ is a subspace.

*Proof.* Since $\operatorname{range}(T) = T(\mathbb{R}^n)$ and $\mathbb{R}^n$ is non-empty, $\operatorname{range}(T)$ is non-empty. It remains to show closure under addition and scalar multiplication.

(i) Let $\vec x, \vec y \in \operatorname{range}(T)$. Then $\vec x = T(\vec u)$ and $\vec y = T(\vec v)$ for some $\vec u, \vec v \in \mathbb{R}^n$. Since $T$ is linear, $\vec x + \vec y = T(\vec u) + T(\vec v) = T(\vec u + \vec v)$, so $\vec x + \vec y \in \operatorname{range}(T)$.

(ii) Let $\vec x \in \operatorname{range}(T)$ and let $\alpha$ be a scalar. Then $\vec x = T(\vec u)$ for some $\vec u$, and by linearity, $\alpha \vec x = \alpha T(\vec u) = T(\alpha \vec u)$, so $\alpha \vec x \in \operatorname{range}(T)$. $\blacksquare$

**Rank of a linear transformation.** For $T : \mathbb{R}^n \to \mathbb{R}^m$, the **rank of $T$**, denoted $\operatorname{rank}(T)$, is $\dim(\operatorname{range}(T))$. A rank-$0$ transformation sends every vector to $\vec 0$; a rank-$1$ transformation sends every vector into a single line; and so on — the rank measures how "big" the set of outputs is.

### Definition: Null Space (Kernel) of a Linear Transformation

*(Source subsection: Null Space)*

The **null space** (or **kernel**) of a linear transformation $T : V \to W$ is the set of vectors sent to the zero vector by $T$:
$$\operatorname{null}(T) = \{\vec x \in V : T\vec x = \vec 0\}.$$

### Theorem: The Null Space of a Linear Transformation Is a Subspace; the Nullity of a Linear Transformation

*(Source subsection: Null Space)*

Let $T : \mathbb{R}^n \to \mathbb{R}^m$ be a linear transformation. Then $\operatorname{null}(T) \subseteq \mathbb{R}^n$ is a subspace.

*Proof.* Since $T$ is linear, $T(\vec 0) = \vec 0$, so $\vec 0 \in \operatorname{null}(T)$, and $\operatorname{null}(T)$ is non-empty.

(i) Let $\vec x, \vec y \in \operatorname{null}(T)$, so $T(\vec x) = T(\vec y) = \vec 0$. By linearity, $T(\vec x + \vec y) = T(\vec x) + T(\vec y) = \vec 0 + \vec 0 = \vec 0$, so $\vec x + \vec y \in \operatorname{null}(T)$.

(ii) Let $\vec x \in \operatorname{null}(T)$ and let $\alpha$ be a scalar. Then $T(\alpha \vec x) = \alpha T(\vec x) = \alpha \vec 0 = \vec 0$, so $\alpha \vec x \in \operatorname{null}(T)$. $\blacksquare$

**Nullity of a linear transformation.** For $T : \mathbb{R}^n \to \mathbb{R}^m$, the **nullity of $T$**, denoted $\operatorname{nullity}(T)$, is $\dim(\operatorname{null}(T))$.

### Definition: Fundamental Subspaces of a Matrix

*(Source subsection: Fundamental Subspaces of a Matrix)*

Associated with any matrix $M$ are three **fundamental subspaces**:

- the **row space** of $M$, $\operatorname{row}(M)$, is the span of the rows of $M$;
- the **column space** of $M$, $\operatorname{col}(M)$, is the span of the columns of $M$;
- the **null space** of $M$, $\operatorname{null}(M)$, is the set of solutions to $M\vec x = \vec 0$.

Computationally, it is much easier to find the fundamental subspaces of a matrix than the range/null space of an abstract transformation, because matrix questions turn into systems of linear equations.

### Method: Finding Bases for the Null Space, Column Space, and Row Space of a Matrix

*(Source subsection: Fundamental Subspaces of a Matrix)*

- **$\operatorname{null}(M)$:** row-reduce $M$, solve $M\vec x = \vec 0$, and write the complete solution in vector form using the free variables. The resulting direction vector(s) form a basis for $\operatorname{null}(M)$.
- **$\operatorname{col}(M)$:** row-reduce $M$ to find the pivot columns of $\operatorname{rref}(M)$. The **original** columns of $M$ in those same positions form a basis for $\operatorname{col}(M)$.
- **$\operatorname{row}(M)$:** the non-zero rows of $\operatorname{rref}(M)$ form a basis for $\operatorname{row}(M)$ (row operations don't change the row space).

**Theorem (Row-Col Dimension).** For a matrix $A$, $\dim(\operatorname{row}(A)) = \dim(\operatorname{col}(A))$ — every pivot of $\operatorname{rref}(A)$ lies in exactly one row and one column, so the number of basis vectors is the same for both.

### Key Fact: $\operatorname{range}(T) = \operatorname{col}(M)$ and $\operatorname{null}(T) = \operatorname{null}(M)$

*(Source subsection: Range vs. Column Space & Null Space vs. Null Space)*

If $T$ is a linear transformation with standard matrix $M$, then
$$\operatorname{range}(T) = \operatorname{col}(M) \qquad \text{and} \qquad \operatorname{null}(T) = \operatorname{null}(M).$$

Consequently:

- $\operatorname{rank}(M) := \operatorname{rank}(T) = \dim(\operatorname{col}(M))$ = the number of pivots in $\operatorname{rref}(M)$.
- $\operatorname{nullity}(M) := \operatorname{nullity}(T) = \dim(\operatorname{null}(M))$ = the number of free-variable columns in $\operatorname{rref}(M)$.

This means any question about the range or null space of a linear transformation can be answered by row-reducing its standard matrix instead.

### Theorem: The Rank-Nullity Theorem

*(Source subsection: The Rank-Nullity Theorem)*

For a matrix $A$:
$$\operatorname{rank}(A) + \operatorname{nullity}(A) = \#\text{ of columns in } A.$$

For a linear transformation $T$:
$$\operatorname{rank}(T) + \operatorname{nullity}(T) = \dim(\text{domain of } T).$$

This single equation lets you find one of $\operatorname{rank}$/$\operatorname{nullity}$/domain-dimension immediately from the other two, without any extra row reduction.

---

## Pages 2–3 — Solved Examples

**Example 1 (Standard matrix of a composition, via matrix multiplication).** Let $A : \mathbb{R}^2 \to \mathbb{R}^2$ and $B : \mathbb{R}^2 \to \mathbb{R}^2$ be matrix transformations with matrices
$$M_A = \begin{bmatrix} 1 & 2 \\ 0 & 2 \end{bmatrix}, \qquad M_B = \begin{bmatrix} -1 & -1 \\ -2 & 0 \end{bmatrix}.$$
Define $T = A \circ B$. Find the standard matrix $M_T$.

*Method 1 (input-output pairs).* Compute $T(\vec e_1)$ and $T(\vec e_2)$ directly:
$$T(\vec e_1) = A\big(B(\vec e_1)\big) = A\begin{bmatrix} -1 \\ -2 \end{bmatrix} = \begin{bmatrix} 1(-1)+2(-2) \\ 0(-1)+2(-2) \end{bmatrix} = \begin{bmatrix} -5 \\ -4 \end{bmatrix}, \qquad T(\vec e_2) = A\big(B(\vec e_2)\big) = A\begin{bmatrix} -1 \\ 0 \end{bmatrix} = \begin{bmatrix} -1 \\ 0 \end{bmatrix}.$$
So $M_T = \begin{bmatrix} -5 & -1 \\ -4 & 0 \end{bmatrix}$.

*Method 2 (matrix product).* By the Theorem on Page 1, $M_T = M_A M_B$:
$$M_A M_B = \begin{bmatrix} 1 & 2 \\ 0 & 2 \end{bmatrix}\begin{bmatrix} -1 & -1 \\ -2 & 0 \end{bmatrix} = \begin{bmatrix} 1(-1)+2(-2) & 1(-1)+2(0) \\ 0(-1)+2(-2) & 0(-1)+2(0) \end{bmatrix} = \begin{bmatrix} -5 & -1 \\ -4 & 0 \end{bmatrix} = M_T.$$
Both methods agree, as the theorem guarantees they must.

**Example 2 (Verify $T \circ S$ two ways: compose first, then multiply matrices first).** Using $A$ and $B$ from Example 1 (so $M_T = M_A M_B = \begin{bmatrix} -5 & -1 \\ -4 & 0 \end{bmatrix}$), let $\vec v = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$. Compute $T(\vec v)$ two ways and check they agree.

*Way 1 (compose first — apply $B$, then $A$, to the vector).*
$$B(\vec v) = M_B \vec v = \begin{bmatrix} -1 & -1 \\ -2 & 0 \end{bmatrix}\begin{bmatrix} 1 \\ -1 \end{bmatrix} = \begin{bmatrix} -1(1)+(-1)(-1) \\ -2(1)+0(-1) \end{bmatrix} = \begin{bmatrix} 0 \\ -2 \end{bmatrix}.$$
$$A\big(B(\vec v)\big) = M_A \begin{bmatrix} 0 \\ -2 \end{bmatrix} = \begin{bmatrix} 1(0)+2(-2) \\ 0(0)+2(-2) \end{bmatrix} = \begin{bmatrix} -4 \\ -4 \end{bmatrix}.$$

*Way 2 (multiply the matrices first, then apply once).*
$$M_T \vec v = \begin{bmatrix} -5 & -1 \\ -4 & 0 \end{bmatrix}\begin{bmatrix} 1 \\ -1 \end{bmatrix} = \begin{bmatrix} -5(1)+(-1)(-1) \\ -4(1)+0(-1) \end{bmatrix} = \begin{bmatrix} -4 \\ -4 \end{bmatrix}.$$

Both ways give $\begin{bmatrix} -4 \\ -4 \end{bmatrix}$, confirming $T(\vec v) = (A \circ B)(\vec v) = M_T \vec v$, exactly as the Theorem on Page 1 guarantees for *every* vector, not just this one.

**Example 3 (Decomposing a transformation as a composition, in the correct order).** Let $U : \mathbb{R}^2 \to \mathbb{R}^2$ be given by the matrix $M_U = \begin{bmatrix} \dfrac{\sqrt2}{2} & -\dfrac{\sqrt2}{2} \\[4pt] 0 & 0 \end{bmatrix}$, let $R$ be rotation counter-clockwise by $45^\circ$, and let $P$ be projection onto the $x$-axis. Write $U$ as the composition (in some order) of $R$ and $P$.

We test both orders on $\vec e_1, \vec e_2$. First, $U(\vec e_1) = \begin{bmatrix} \sqrt2/2 \\ 0 \end{bmatrix}$ and $U(\vec e_2) = \begin{bmatrix} -\sqrt2/2 \\ 0 \end{bmatrix}$.

*Testing $R \circ P$:* $\;R\circ P(\vec e_1) = R\big(P(\vec e_1)\big) = R\begin{bmatrix} 1\\0 \end{bmatrix} = \begin{bmatrix} \sqrt2/2 \\ \sqrt2/2 \end{bmatrix} \neq U(\vec e_1)$. So $R \circ P \neq U$.

*Testing $P \circ R$:* $\;P \circ R(\vec e_1) = P\big(R(\vec e_1)\big) = P\begin{bmatrix} \sqrt2/2 \\ \sqrt2/2 \end{bmatrix} = \begin{bmatrix} \sqrt2/2 \\ 0 \end{bmatrix} = U(\vec e_1)$. Also, $P \circ R(\vec e_2) = P\big(R(\vec e_2)\big) = P\begin{bmatrix} -\sqrt2/2 \\ \sqrt2/2 \end{bmatrix} = \begin{bmatrix} -\sqrt2/2 \\ 0 \end{bmatrix} = U(\vec e_2)$.

Since $P \circ R$ agrees with $U$ on the standard basis, $P \circ R$ and $U$ agree everywhere. Therefore $U = P \circ R$ (rotate first, then project) — **not** $R \circ P$.

**Example 4 (Finding a basis for a null space).** Find the null space of $M = \begin{bmatrix} 1 & 2 & 5 \\ 2 & -2 & -2 \end{bmatrix}$.

We solve $M\vec x = \vec 0$ by row reduction:
$$\operatorname{rref}(M) = \begin{bmatrix} 1 & 0 & 1 \\ 0 & 1 & 2 \end{bmatrix}.$$
The third column has no pivot, so $z$ is a free variable. From the rows, $x = -z$ and $y = -2z$. Letting $z = t$, the complete solution in vector form is
$$\begin{bmatrix} x \\ y \\ z \end{bmatrix} = t\begin{bmatrix} -1 \\ -2 \\ 1 \end{bmatrix}, \qquad \text{so} \qquad \operatorname{null}(M) = \operatorname{span}\left\{ \begin{bmatrix} -1 \\ -2 \\ 1 \end{bmatrix} \right\}.$$
A basis for $\operatorname{null}(M)$ is $\left\{\begin{bmatrix} -1 \\ -2 \\ 1 \end{bmatrix}\right\}$, so $\operatorname{nullity}(M) = 1$.

**Example 5 (Finding a basis for the column space and row space of the same matrix).** Using $M = \begin{bmatrix} 1 & 2 & 5 \\ 2 & -2 & -2 \end{bmatrix}$ from Example 4, find a basis for $\operatorname{col}(M)$ and for $\operatorname{row}(M)$.

From $\operatorname{rref}(M) = \begin{bmatrix} 1 & 0 & 1 \\ 0 & 1 & 2 \end{bmatrix}$, columns 1 and 2 are the pivot columns. So a basis for $\operatorname{col}(M)$ consists of the **original** columns 1 and 2 of $M$:
$$\operatorname{col}(M) = \operatorname{span}\left\{\begin{bmatrix} 1 \\ 2 \end{bmatrix}, \begin{bmatrix} 2 \\ -2 \end{bmatrix}\right\} = \mathbb{R}^2.$$
For the row space, the two rows of $M$, $\begin{bmatrix} 1 & 2 & 5\end{bmatrix}$ and $\begin{bmatrix}2 & -2 & -2\end{bmatrix}$, are linearly independent (neither is a scalar multiple of the other), so
$$\operatorname{row}(M) = \operatorname{span}\left\{\begin{bmatrix} 1\\2\\5 \end{bmatrix}, \begin{bmatrix} 2\\-2\\-2 \end{bmatrix}\right\}.$$
Both subspaces have dimension $2$, consistent with the Row-Col Dimension Theorem.

**Example 6 (Finding the range and rank of a transformation given by a formula).** Let $T : \mathbb{R}^3 \to \mathbb{R}^2$ be defined by $T\begin{bmatrix} x\\y\\z \end{bmatrix} = \begin{bmatrix} 2x - z \\ 4x - 2z \end{bmatrix}$. Find $\operatorname{range}(T)$ and $\operatorname{rank}(T)$.

The standard matrix of $T$ is $M = \begin{bmatrix} 2 & 0 & -1 \\ 4 & 0 & -2 \end{bmatrix}$, and $\operatorname{range}(T) = \operatorname{col}(M)$. By inspection, column 2 is $\vec 0$ and column 3 is $-\tfrac12$ times column 1, so column 1 alone is a maximal linearly independent set:
$$\operatorname{range}(T) = \operatorname{col}(M) = \operatorname{span}\left\{ \begin{bmatrix} 2\\4 \end{bmatrix} \right\}, \qquad \operatorname{rank}(T) = 1.$$

**Example 7 (Range, null space, rank, and nullity of a projection onto a plane).** Let $P$ be the plane $x+y+z=0$ in $\mathbb{R}^3$, and let $T : \mathbb{R}^3 \to \mathbb{R}^3$ be projection onto $P$. Find $\operatorname{range}(T)$, $\operatorname{rank}(T)$, $\operatorname{null}(T)$, and $\operatorname{nullity}(T)$.

*Range.* Since $T$ projects onto $P$, every output lies in $P$, so $\operatorname{range}(T) \subseteq P$. Also, $T(\vec p) = \vec p$ for every $\vec p \in P$ (a vector already in $P$ is unaffected by projecting onto $P$), so $P \subseteq \operatorname{range}(T)$. Hence $\operatorname{range}(T) = P$, and since $P$ is a plane, $\operatorname{rank}(T) = \dim(P) = 2$.

*Null space.* A vector is sent to $\vec 0$ by projection onto $P$ exactly when it is perpendicular to $P$ — i.e., a normal vector for $P$ (together with $\vec 0$ itself). Since $\begin{bmatrix}1\\1\\1\end{bmatrix}$ is a normal vector for $P$,
$$\operatorname{null}(T) = \operatorname{span}\left\{ \begin{bmatrix}1\\1\\1\end{bmatrix} \right\}, \qquad \operatorname{nullity}(T) = 1.$$

*Check via Rank-Nullity:* $\operatorname{rank}(T) + \operatorname{nullity}(T) = 2 + 1 = 3 = \dim(\mathbb{R}^3)$, the dimension of the domain. $\checkmark$

**Example 8 (Using the Rank-Nullity Theorem as a shortcut to relate dimensions).** Let $M = \begin{bmatrix} 1 & 2 & 2 \end{bmatrix}$, and let $P = \operatorname{null}(M)$, the plane $x+2y+2z=0$ in $\mathbb{R}^3$. Use the Rank-Nullity Theorem to find $\operatorname{rank}(M)$, and use this to describe the set of normal vectors to $P$.

Since $P$ is a plane, $\dim(P) = 2$, so $\operatorname{nullity}(M) = 2$. $M$ has $3$ columns, so by the Rank-Nullity Theorem,
$$\operatorname{rank}(M) = 3 - \operatorname{nullity}(M) = 3 - 2 = 1.$$
By the Row-Col Dimension Theorem, $\dim(\operatorname{row}(M)) = \dim(\operatorname{col}(M)) = \operatorname{rank}(M) = 1$. Since non-zero vectors in $\operatorname{row}(M)$ are exactly the normal vectors to $P = \operatorname{null}(M)$, and $\operatorname{row}(M)$ is one-dimensional, the set of normal vectors to $P$ forms a **line** (through the origin) — found entirely from the Rank-Nullity Theorem, without ever needing to describe $P$ itself.

---

## Pages 4–5 — Practice Problems (unsolved)

**Composition of Linear Transformations**

1. Let $A : \mathbb{R}^2 \to \mathbb{R}^2$ and $B : \mathbb{R}^2 \to \mathbb{R}^2$ be matrix transformations with matrices $M_A = \begin{bmatrix} 2 & 2 \\ 1 & 3 \end{bmatrix}$ and $M_B = \begin{bmatrix} 3 & 2 \\ 0 & 4 \end{bmatrix}$. Let $T = A \circ B$. Find $M_T$ by computing input-output pairs for $T$, then check your answer using matrix multiplication.
2. Let $A : \mathbb{R}^3 \to \mathbb{R}^2$ and $B : \mathbb{R}^2 \to \mathbb{R}^1$ be matrix transformations with matrices $M_A = \begin{bmatrix} 2 & 1 & 0 \\ 2 & 3 & 0 \end{bmatrix}$ and $M_B = \begin{bmatrix} 3 & 2 \end{bmatrix}$. Let $T = B \circ A$. Find $M_T$ two ways (input-output pairs, and matrix multiplication).
3. Let $S : \mathbb{R}^2 \to \mathbb{R}^2$ double every vector, and let $F : \mathbb{R}^2 \to \mathbb{R}^2$ reflect over the line $y=x$. Find the standard matrices for $F \circ S$ and $S \circ F$. Are the two resulting matrices equal? If so, is this a coincidence, or does it always happen when you compose two arbitrary linear transformations?
4. Let $V : \mathbb{R}^2 \to \mathbb{R}^2$ be given by the matrix $\begin{bmatrix} 0 & 2 \\ 2 & 0 \end{bmatrix}$. Using $S$ and $F$ from Problem 3, write $V$ as the composition (in some order) of $S$ and $F$, justifying your order choice using $\vec e_1$ and $\vec e_2$.

**Null Space (Kernel)**

5. Find the null space of $M_1 = \begin{bmatrix} 1 & 2 & 1 \\ 3 & 1 & -2 \\ 8 & 6 & -2 \end{bmatrix}$.
6. Find the null space of $M_2 = \begin{bmatrix} 0 & 2 & 1 \\ 3 & 2 & 5 \end{bmatrix}$.
7. Let $T : \mathbb{R}^2 \to \mathbb{R}^2$ be projection onto the line $y = x$. Find $\operatorname{null}(T)$ and $\operatorname{nullity}(T)$.
8. Let $Q : \mathbb{R}^3 \to \mathbb{R}^1$ be defined by $Q\begin{bmatrix} x\\y\\z \end{bmatrix} = x+z$. Find $\operatorname{null}(Q)$.

**Range (Column Space)**

9. Using $M_1$ from Problem 5, find a basis for $\operatorname{col}(M_1)$ and a basis for $\operatorname{row}(M_1)$. What are their dimensions?
10. Let $M : \mathbb{R}^3 \to \mathbb{R}^3$ be the matrix transformation given by $\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix}$. Find $\operatorname{range}(M)$ and $\operatorname{rank}(M)$.
11. Let $P : \mathbb{R}^3 \to \mathbb{R}^3$ be projection onto the $xy$-plane. Find a matrix for $P$, then find $\operatorname{range}(P)$ and $\operatorname{null}(P)$.

**Rank-Nullity and Concept Checks**

12. Let $P$ be the plane $3x+4y+5z=0$ in $\mathbb{R}^3$, and let $T : \mathbb{R}^3 \to \mathbb{R}^3$ be projection onto $P$. Find $\operatorname{range}(T)$, $\operatorname{rank}(T)$, $\operatorname{null}(T)$, and $\operatorname{nullity}(T)$.
13. The rank of a $3 \times 4$ matrix $A$ is $3$. Are the column vectors of $A$ linearly independent? Justify your answer using the Rank-Nullity Theorem.
14. True or false, with justification: "Let $T : \mathbb{R}^m \to \mathbb{R}^n$ be a linear transformation induced by a matrix $M$. If $\operatorname{rank}(T) = n$, then $\operatorname{nullity}(M) = 0$."

---

## Answer Key & Misconception Notes (for tutor use — do not show student until after attempt)

| # | Answer | Common misconception |
|---|---|---|
| 1 | $M_T = M_A M_B = \begin{bmatrix} 6 & 12 \\ 3 & 14 \end{bmatrix}$ | Multiplying in the wrong order ($M_B M_A$ instead of $M_A M_B$) — students forget that in $T = A \circ B$, $B$'s matrix goes on the **right**, matching the order the composition symbol is written. |
| 2 | $M_T = M_B M_A = \begin{bmatrix} 10 & 9 & 0 \end{bmatrix}$ (a $1\times 3$ matrix) | Trying to compute $M_A M_B$ instead of $M_B M_A$ — students default to "matrix that was defined first" rather than checking which matrix multiplication is actually defined given the dimensions ($M_B$ is $1\times2$, $M_A$ is $2\times3$, so only $M_B M_A$, a $1\times 3$ product, makes sense). |
| 3 | $F \circ S$ and $S \circ F$ both equal $\begin{bmatrix} 0 & 2 \\ 2 & 0 \end{bmatrix}$. This is **not** a general phenomenon — it happens here only because $S = 2I$ is a scalar multiple of the identity matrix, and scalar multiples of $I$ commute with every matrix. In general $M_P M_Q \neq M_Q M_P$. | Concluding from this one example that "composition order doesn't matter" — students need to see that this is a special case (caused by $S$ being $2I$), not evidence against the general non-commutativity rule stated on Page 1. |
| 4 | $V = F \circ S = S \circ F$ (both compositions equal $V$ here, since they're equal to each other from Problem 3). Checking $\vec e_1$: $F\circ S(\vec e_1) = F\begin{bmatrix}2\\0\end{bmatrix} = \begin{bmatrix}0\\2\end{bmatrix} = V(\vec e_1)$. $\checkmark$ | Assuming there's only "one correct answer" for the order and getting stuck when both orders check out — students should recognize that when the two composition matrices coincide (as flagged in Problem 3), either order is a valid decomposition. |
| 5 | $\operatorname{null}(M_1) = \operatorname{span}\left\{\begin{bmatrix}1\\-1\\1\end{bmatrix}\right\}$ | Forgetting to fully reduce to rref before reading off the free variable, or making a row-reduction arithmetic slip on the $8$ or $6$ in row 3 and getting an extra (incorrect) free variable. |
| 6 | $\operatorname{null}(M_2) = \operatorname{span}\left\{\begin{bmatrix}8\\3\\-6\end{bmatrix}\right\}$ | Leaving the answer in fraction form (e.g. $\begin{bmatrix}-4/3\\-1/2\\1\end{bmatrix}$) without checking whether a cleaner integer scalar multiple exists — the span is the same, but it's easy to mis-copy a fraction on a later problem that reuses this null space. |
| 7 | $\operatorname{null}(T) = \operatorname{span}\left\{\begin{bmatrix}1\\-1\end{bmatrix}\right\}$; $\operatorname{nullity}(T) = 1$ | Confusing the line the projection projects **onto** ($y=x$, which is $\operatorname{range}(T)$) with the line that gets sent to $\vec 0$ ($y=-x$, the orthogonal line, which is $\operatorname{null}(T)$). |
| 8 | $\operatorname{null}(Q) = \operatorname{span}\left\{\begin{bmatrix}0\\1\\0\end{bmatrix}, \begin{bmatrix}-1\\0\\1\end{bmatrix}\right\}$, a plane (2-dimensional) | Treating $Q$'s matrix $\begin{bmatrix}1 & 0 & 1\end{bmatrix}$ as if it had only one free variable, forgetting that $y$ never appears in the equation $x+z=0$ and so is *also* free, giving nullity $2$, not $1$. |
| 9 | Basis for $\operatorname{col}(M_1)$: $\left\{\begin{bmatrix}1\\3\\8\end{bmatrix}, \begin{bmatrix}2\\1\\6\end{bmatrix}\right\}$; basis for $\operatorname{row}(M_1)$: $\left\{\begin{bmatrix}1\\0\\-1\end{bmatrix}, \begin{bmatrix}0\\1\\1\end{bmatrix}\right\}$ (the non-zero rows of $\operatorname{rref}(M_1)$); both have dimension $2$ | Reading the column-space basis off of $\operatorname{rref}(M_1)$ itself instead of going back to the **original** matrix $M_1$ — the pivot *positions* come from rref, but the basis vectors for $\operatorname{col}(M)$ must be the original columns. |
| 10 | $\operatorname{range}(M) = \operatorname{span}\left\{\begin{bmatrix}1\\4\\7\end{bmatrix}, \begin{bmatrix}2\\5\\8\end{bmatrix}\right\}$; $\operatorname{rank}(M) = 2$ | Assuming a $3\times 3$ matrix automatically has rank $3$ (i.e. full range $\mathbb{R}^3$) without actually row-reducing — this matrix's third row is a linear combination of the first two, so the rank is only $2$. |
| 11 | Matrix: $\begin{bmatrix} 1&0&0\\0&1&0\\0&0&0 \end{bmatrix}$; $\operatorname{range}(P) = \operatorname{span}\{\vec e_1, \vec e_2\}$ (the $xy$-plane); $\operatorname{null}(P) = \operatorname{span}\{\vec e_3\}$ (the $z$-axis) | Writing the projection matrix with a $1$ instead of $0$ in the $(3,3)$ entry (forgetting to zero out the $z$-coordinate), which would incorrectly make $P$ the identity. |
| 12 | $\operatorname{range}(T) = P$, $\operatorname{rank}(T)=2$; $\operatorname{null}(T) = \operatorname{span}\left\{\begin{bmatrix}3\\4\\5\end{bmatrix}\right\}$, $\operatorname{nullity}(T)=1$ | Using the normal vector $\begin{bmatrix}3\\4\\5\end{bmatrix}$ correctly for the null space but then also listing it (or a multiple of it) as part of the range — students sometimes forget the range and null space of a projection are orthogonal complements, not overlapping sets. |
| 13 | No — by Rank-Nullity, $\operatorname{nullity}(A) = 4 - \operatorname{rank}(A) = 4-3 = 1 \neq 0$, so there is a non-trivial solution to $A\vec x = \vec 0$, meaning the four columns satisfy a non-trivial linear combination equal to $\vec 0$ — i.e. they are linearly **dependent**. | Reasoning "rank is high (3 out of a possible 3 rows), so the columns must be independent" — students conflate rank (row-space/column-space dimension) with the number of *columns*; with $4$ columns in $\mathbb{R}^3$, dependence is unavoidable regardless of rank. |
| 14 | False in general — only true when $m=n$. By Rank-Nullity, $\operatorname{rank}(T)+\operatorname{nullity}(T) = m$ (the domain dimension), so if $\operatorname{rank}(T)=n$, then $\operatorname{nullity}(M) = \operatorname{nullity}(T) = m-n$, which is $0$ only if $m=n$. Counterexample: $M = \begin{bmatrix}1&0&0\\0&1&0\end{bmatrix}$ has $\operatorname{rank}(T)=2=n$ but $\operatorname{nullity}(M) = 3-2=1 \neq 0$. | Assuming "rank is as large as possible" (full row rank, i.e. $T$ is onto) automatically implies "nullity is zero" (i.e. $T$ is one-to-one) — these are two *different* extremes of Rank-Nullity that only coincide when the domain and codomain have the same dimension. |
