# Week 9 — Matrix Representations of Systems; Coordinates & Change of Basis I

**Session length:** 3 hours
**Source:** Siefken, *MAT223 Workbook*, Module 7 (Matrix Representations of Systems of Linear Equations) and Module 8 (Coordinates & Change of Basis I)

---

## Page 1 — Introduction, Key Facts & Definitions

### Why this matters

Last week you learned that a subspace is completely pinned down once you have a basis for it, and that every basis for the same subspace has the same number of elements (its dimension). This week combines that idea with matrix-vector multiplication (Week 2) in two directions. First, we compress an entire system of linear equations into a single matrix equation $A\vec x = \vec b$, which gives three complementary ways to think about what a "solution" means — and connects directly back to linear independence and normal vectors. Second, we take seriously the fact that a basis does not have to be the standard basis $\{\vec e_1, \ldots, \vec e_n\}$: once you fix *any* basis $B$, every vector has a unique set of coordinates relative to $B$, and you need careful notation, $[\vec v]_B$, to keep track of which basis a list of numbers refers to. By the end of this week you can convert a vector's coordinates from one basis to another using a **change-of-basis matrix**.

### Definition: Coefficient Matrix and the Matrix Equation $A\vec x = \vec b$

*(Source subsection: Matrix Representations of Systems of Linear Equations)*

Every system of linear equations can be rewritten as a single matrix equation
$$A\vec x = \vec b,$$
where $A$ is the **coefficient matrix** (built from the coefficients of the system, one row per equation), $\vec x$ is the column vector of unknowns, and $\vec b$ is the column vector of constants on the right-hand side. For example, the system
$$\begin{cases} x+2y-2z=-15\\ 2x+y-5z=-21\\ x-4y+z=18\end{cases}$$
is exactly the matrix equation
$$\underbrace{\begin{bmatrix}1&2&-2\\2&1&-5\\1&-4&1\end{bmatrix}}_{A}\begin{bmatrix}x\\y\\z\end{bmatrix}=\begin{bmatrix}-15\\-21\\18\end{bmatrix}.$$
Multiplying out the left-hand side with matrix-vector multiplication (Week 2) reproduces the original three equations, row by row.

### Fact: Three Interpretations of a Matrix Equation

*(Source subsection: Interpretations of Matrix Equations)*

A matrix equation $A\vec x = \vec b$ can be read three complementary ways:

- **Hyperplane-intersection picture.** Each row of $A$ (together with the matching entry of $\vec b$) gives one equation — one hyperplane (a line in $\mathbb{R}^2$, a plane in $\mathbb{R}^3$, and so on) — and the solution set is the intersection of all of these hyperplanes.
- **Column picture.** Writing $A = \begin{bmatrix}\vec a_1 & \cdots & \vec a_n\end{bmatrix}$ in terms of its columns, $A\vec x = x_1\vec a_1 + \cdots + x_n\vec a_n$. So "solve $A\vec x = \vec b$" is the same question as "what coefficients let the columns of $A$ combine (as a linear combination) to form $\vec b$?"
- **Row picture (dot products).** If $\vec r_1, \ldots, \vec r_m$ are the rows of $A$, then $A\vec x = \begin{bmatrix}\vec r_1\cdot \vec x \\ \vdots \\ \vec r_m \cdot \vec x\end{bmatrix}$. So a solution $\vec x$ is exactly a vector whose dot product with $\vec r_i$ equals the $i$-th entry of $\vec b$, for every $i$.

### Fact: Homogeneous Systems Link Solutions to Independence and Orthogonality

*(Source subsection: Interpreting Homogeneous Systems)*

For a homogeneous system $A\vec x = \vec 0$, the column picture asks: what linear combinations of the columns of $A$ give $\vec 0$? This is exactly the question you ask to test whether the columns of $A$ are linearly independent (Week 6). The row picture asks: what vectors are simultaneously orthogonal to every row of $A$? This second question is the reasoning behind finding normal vectors, below — and it is especially useful because when $\vec b = \vec 0$, the row picture becomes a purely geometric question about orthogonality.

### Fact: Using the Row Picture to Find Normal Vectors

*(Source subsection: Interpreting Homogeneous Systems — worked examples)*

To find every vector orthogonal to a list of given vectors $\vec d_1, \ldots, \vec d_k$, stack the $\vec d_i$ as the **rows** of a matrix $A$ and solve the homogeneous system $A\vec x = \vec 0$ by row reduction. In particular, if a hyperplane $P$ is given in vector form with direction vectors $\vec d_1, \ldots, \vec d_k$, the non-zero solutions of $A\vec x = \vec 0$ (with the $\vec d_i$ as rows of $A$) are exactly the normal vectors of $P$ — this is how you convert a hyperplane from vector form to normal form (Week 7).

### Definition: Representation of a Vector in a Basis

*(Source subsection: Representation in a Basis)*

Let $B = \{\vec b_1, \ldots, \vec b_n\}$ be a basis for a subspace $V$, and let $\vec v \in V$. Since $B$ is a basis, there is a *unique* choice of scalars $\alpha_1, \ldots, \alpha_n$ with $\vec v = \alpha_1\vec b_1 + \cdots + \alpha_n\vec b_n$ (uniqueness is exactly the "coordinates are unique" fact from Week 8). The **representation of $\vec v$ in the $B$ basis**, notated $[\vec v]_B$, is the column matrix
$$[\vec v]_B = \begin{bmatrix}\alpha_1\\ \vdots \\ \alpha_n\end{bmatrix}.$$
Conversely, $\begin{bmatrix}\alpha_1\\ \vdots \\ \alpha_n\end{bmatrix}_B$ is notation for the linear combination $\alpha_1\vec b_1 + \cdots + \alpha_n \vec b_n$ itself — the true vector you get by plugging the numbers back into the basis $B$.

### Fact: Notation Conventions for Coordinate Vectors

*(Source subsection: Notation Conventions)*

Writing $\vec x = \begin{bmatrix}2\\3\end{bmatrix}$ has always secretly meant $\vec x = 2\vec e_1+3\vec e_2$, i.e. $\vec x = \begin{bmatrix}2\\3\end{bmatrix}_E$ where $E$ is the standard basis. The convention going forward:

- If a problem involves only **one** basis, you may drop the subscript and write $\begin{bmatrix}x\\y\end{bmatrix}$ to mean $\begin{bmatrix}x\\y\end{bmatrix}_E$.
- If a problem involves **more than one** basis, you must always write the subscript, e.g. $\begin{bmatrix}x\\y\end{bmatrix}_X$, to specify which basis $X$ the coordinates are relative to.

### Fact: True Vectors vs. Representations

*(Source subsection: True Vectors vs. Representations)*

A vector $\vec v$ itself (a "true vector") is *not* the same object as its coordinate list $[\vec v]_X$ (a list of numbers) — a list of numbers has no meaning until you attach a basis to it. For any basis $X$:
$$[\text{true vector}]_X = \text{list of numbers}, \qquad [\text{list of numbers}]_X = \text{true vector}.$$
In particular $\vec v \neq [\vec v]_E$ in general, even though, by the notation convention above, we usually abbreviate $[\vec v]_E$ as $\vec v$ when only the standard basis is in play.

### Fact: Change-of-Basis Matrices Convert Between Coordinate Systems

*(Source subsection: Change of Basis & Coordinates)*

If $C = \{\vec c_1, \vec c_2\}$ is a basis for $\mathbb{R}^2$ given in standard coordinates, then the matrix $X = \begin{bmatrix}\vec c_1 & \vec c_2\end{bmatrix}$ (whose columns are $\vec c_1,\vec c_2$) satisfies
$$X[\vec w]_C = [\vec w]_E \quad \text{for every } \vec w,$$
since plugging $[\vec w]_C = \begin{bmatrix}1\\0\end{bmatrix}$ or $\begin{bmatrix}0\\1\end{bmatrix}$ into $X[\vec w]_C$ (the column picture) reproduces $\vec c_1$ or $\vec c_2$ in standard coordinates — exactly the columns of $X$. Because $X$ converts $C$-coordinates to $E$-coordinates, its inverse $Y = X^{-1}$ converts the other way:
$$Y[\vec w]_E = [\vec w]_C \quad \text{for every } \vec w.$$
Consequently $YX = X^{-1}X = I$, the identity matrix — converting to standard coordinates and back changes nothing.

---

## Pages 2–3 — Solved Examples

**Example 1 (Rewrite systems of equations as matrix equations).** Rewrite the one-equation system $x-4y+z=5$ and the two-equation system $\begin{cases}x-4y+z=5\\y-z=9\end{cases}$ as matrix equations.

For a single equation, the coefficient matrix has just one row:
$$\begin{bmatrix}1&-4&1\end{bmatrix}\begin{bmatrix}x\\y\\z\end{bmatrix}=\begin{bmatrix}5\end{bmatrix}.$$
Multiplying out the left side, $\begin{bmatrix}1&-4&1\end{bmatrix}\begin{bmatrix}x\\y\\z\end{bmatrix} = \begin{bmatrix}x-4y+z\end{bmatrix} = \begin{bmatrix}5\end{bmatrix}$, exactly the original equation.

For the two-equation system, each equation becomes a row:
$$\begin{bmatrix}1&-4&1\\0&1&-1\end{bmatrix}\begin{bmatrix}x\\y\\z\end{bmatrix}=\begin{bmatrix}5\\9\end{bmatrix}.$$
Checking: row 1 gives $x-4y+z=5$; row 2 gives $0x+y-z=9$, i.e. $y-z=9$ — both match the original system. $\blacksquare$

**Example 2 (The three interpretations of one matrix equation).** Consider $\begin{cases}x+2y-2z=-15\\2x+y-5z=-21\\x-4y+z=18\end{cases}$, i.e. $A\vec x=\vec b$ with $A=\begin{bmatrix}1&2&-2\\2&1&-5\\1&-4&1\end{bmatrix}$ and $\vec b=\begin{bmatrix}-15\\-21\\18\end{bmatrix}$. Describe the solution set all three ways.

*Hyperplane intersection:* each row gives a plane in $\mathbb{R}^3$; the solution set is the intersection of $x+2y-2z=-15$, $2x+y-5z=-21$, and $x-4y+z=18$.

*Column picture:* writing $A$'s columns as $\vec a_1=\begin{bmatrix}1\\2\\1\end{bmatrix}$, $\vec a_2=\begin{bmatrix}2\\1\\-4\end{bmatrix}$, $\vec a_3=\begin{bmatrix}-2\\-5\\1\end{bmatrix}$, the equation reads $x\vec a_1+y\vec a_2+z\vec a_3=\vec b$ — a solution is a choice of coefficients that combines $\vec a_1,\vec a_2,\vec a_3$ into $\vec b$.

*Row (dot-product) picture:* with rows $\vec r_1=(1,2,-2)$, $\vec r_2=(2,1,-5)$, $\vec r_3=(1,-4,1)$, a solution $\vec x=(x,y,z)$ is exactly a vector satisfying $\vec r_1\cdot\vec x=-15$, $\vec r_2\cdot\vec x=-21$, and $\vec r_3\cdot\vec x=18$ simultaneously. $\blacksquare$

**Example 3 (Solve $A\vec x=\vec b$ by row reduction and interpret the solution).** Let $A=\begin{bmatrix}1&2\\3&3\end{bmatrix}$, $\vec x=\begin{bmatrix}x\\y\end{bmatrix}$, $\vec b=\begin{bmatrix}-2\\-1\end{bmatrix}$. Solve $A\vec x=\vec b$, then explain the solution (a) as an intersection of lines and (b) as a linear combination of columns.

Row reduce the augmented matrix:
$$\left[\begin{array}{cc|c}1&2&-2\\3&3&-1\end{array}\right] \xrightarrow{R_2-3R_1} \left[\begin{array}{cc|c}1&2&-2\\0&-3&5\end{array}\right] \xrightarrow{R_2\div(-3)} \left[\begin{array}{cc|c}1&2&-2\\0&1&-5/3\end{array}\right] \xrightarrow{R_1-2R_2} \left[\begin{array}{cc|c}1&0&4/3\\0&1&-5/3\end{array}\right].$$
So $x=\dfrac{4}{3}$, $y=-\dfrac{5}{3}$.

(a) The rows $x+2y=-2$ and $3x+3y=-1$ are each lines in the $xy$-plane; $\left(\dfrac{4}{3},-\dfrac{5}{3}\right)$ is the single point where these two lines cross.

(b) The columns of $A$ are $\vec a_1=\begin{bmatrix}1\\3\end{bmatrix}$ and $\vec a_2=\begin{bmatrix}2\\3\end{bmatrix}$; the solution says $\dfrac43\vec a_1-\dfrac53\vec a_2=\vec b$. Checking: $\dfrac43\begin{bmatrix}1\\3\end{bmatrix}-\dfrac53\begin{bmatrix}2\\3\end{bmatrix}=\begin{bmatrix}4/3-10/3\\4-5\end{bmatrix}=\begin{bmatrix}-2\\-1\end{bmatrix}$. $\blacksquare$

**Example 4 (Homogeneous system: find all vectors orthogonal to two given vectors).** Find all vectors orthogonal to $\vec a=\begin{bmatrix}1\\1\\1\end{bmatrix}$ and $\vec b=\begin{bmatrix}1\\2\\1\end{bmatrix}$.

We need $\vec x$ with $\vec a\cdot\vec x=0$ and $\vec b\cdot\vec x=0$ simultaneously — by the row picture, this is exactly the homogeneous system $A\vec x=\vec 0$ where $A$ has $\vec a,\vec b$ as its rows:
$$A=\begin{bmatrix}1&1&1\\1&2&1\end{bmatrix}.$$
Row reduce: $R_2-R_1$ gives $\begin{bmatrix}1&1&1\\0&1&0\end{bmatrix}$; then $R_1-R_2$ gives $\operatorname{rref}(A)=\begin{bmatrix}1&0&1\\0&1&0\end{bmatrix}$. So $x=-z$, $y=0$, with $z$ free. Setting $z=t$, the complete solution is
$$\vec x=t\begin{bmatrix}-1\\0\\1\end{bmatrix}.$$
Every non-zero multiple of $\begin{bmatrix}-1\\0\\1\end{bmatrix}$ is orthogonal to both $\vec a$ and $\vec b$: $\begin{bmatrix}-1\\0\\1\end{bmatrix}\cdot\vec a=-1+0+1=0$ and $\begin{bmatrix}-1\\0\\1\end{bmatrix}\cdot\vec b=-1+0+1=0$. $\blacksquare$

**Example 5 (Find a normal vector and normal form for a hyperplane given in vector form).** Let $Q$ be the hyperplane $\vec x=t\vec d_1+s\vec d_2+r\vec d_3+\vec p$ with $\vec d_1=\begin{bmatrix}1\\1\\-1\\1\end{bmatrix}$, $\vec d_2=\begin{bmatrix}0\\1\\0\\1\end{bmatrix}$, $\vec d_3=\begin{bmatrix}2\\0\\0\\0\end{bmatrix}$, $\vec p=\begin{bmatrix}1\\2\\3\\4\end{bmatrix}$. Find a normal vector for $Q$ and write $Q$ in normal form.

A normal vector must be orthogonal to $\vec d_1,\vec d_2,\vec d_3$ simultaneously — by the row picture, we need the non-zero solutions of $A\vec x=\vec 0$ where $A$ has $\vec d_1,\vec d_2,\vec d_3$ as rows:
$$A=\begin{bmatrix}1&1&-1&1\\0&1&0&1\\2&0&0&0\end{bmatrix}.$$
Row reducing gives $\operatorname{rref}(A)=\begin{bmatrix}1&0&0&0\\0&1&0&1\\0&0&1&0\end{bmatrix}$, so with free variable $w=t$: $x=0$, $y=-t$, $z=0$, $w=t$, i.e.
$$\vec x=t\begin{bmatrix}0\\-1\\0\\1\end{bmatrix}.$$
So $\vec n=\begin{bmatrix}0\\-1\\0\\1\end{bmatrix}$ is a normal vector for $Q$, and $Q$'s normal form is
$$\begin{bmatrix}0\\-1\\0\\1\end{bmatrix}\cdot\left(\begin{bmatrix}x\\y\\z\\w\end{bmatrix}-\begin{bmatrix}1\\2\\3\\4\end{bmatrix}\right)=0. \qquad \blacksquare$$

**Example 6 (Find the coordinates of a vector relative to a non-standard basis).** Let $E=\{\vec e_1,\vec e_2\}$ be the standard basis for $\mathbb{R}^2$, and let $C=\{\vec c_1,\vec c_2\}$ where $\vec c_1=\vec e_1+\vec e_2$ and $\vec c_2=3\vec e_2$. Let $\vec v=2\vec e_1-\vec e_2$. Find $[\vec v]_E$ and $[\vec v]_C$.

Since $\vec v=2\vec e_1-\vec e_2$ is already written in terms of $\vec e_1,\vec e_2$, we read off
$$[\vec v]_E=\begin{bmatrix}2\\-1\end{bmatrix}.$$
To find $[\vec v]_C$ we need scalars $x,y$ with $\vec v=x\vec c_1+y\vec c_2$. Substituting $\vec c_1=\vec e_1+\vec e_2$ and $\vec c_2=3\vec e_2$:
$$x\vec c_1+y\vec c_2=x(\vec e_1+\vec e_2)+3y\vec e_2=x\vec e_1+(x+3y)\vec e_2.$$
Setting this equal to $\vec v=2\vec e_1-\vec e_2$ and matching coefficients of $\vec e_1,\vec e_2$ (which are linearly independent, so coefficients must match exactly) gives the system
$$x=2, \qquad x+3y=-1.$$
Substituting $x=2$: $2+3y=-1 \Rightarrow y=-1$. So $\vec v=2\vec c_1-\vec c_2$, and
$$[\vec v]_C=\begin{bmatrix}2\\-1\end{bmatrix}. \qquad \blacksquare$$

(The numbers happen to match $[\vec v]_E$ here — that is a coincidence of this particular vector and basis, not a general rule.)

**Example 7 (Convert a coordinate vector back into a true vector in standard coordinates).** Let $E$ be the standard basis for $\mathbb{R}^2$, and let $B=\{\vec b_1,\vec b_2\}$ with $\vec b_1=\begin{bmatrix}2\\1\end{bmatrix}$, $\vec b_2=\begin{bmatrix}0\\1\end{bmatrix}$. Given $\begin{bmatrix}1\\2\end{bmatrix}_B$, find the corresponding true vector's standard coordinates.

By the converse notation, $\begin{bmatrix}1\\2\end{bmatrix}_B$ means the linear combination $1\cdot\vec b_1+2\cdot\vec b_2$:
$$1\begin{bmatrix}2\\1\end{bmatrix}+2\begin{bmatrix}0\\1\end{bmatrix}=\begin{bmatrix}2\\1\end{bmatrix}+\begin{bmatrix}0\\2\end{bmatrix}=\begin{bmatrix}2\\3\end{bmatrix}.$$
So the true vector is $\vec x=2\vec e_1+3\vec e_2$, i.e. $[\vec x]_E=\begin{bmatrix}2\\3\end{bmatrix}$. (This is the same $\vec x$ from the very first example of the module: it has $E$-coordinates $(2,3)$ and $B$-coordinates $(1,2)$.) $\blacksquare$

**Example 8 (Build and use a change-of-basis matrix).** Let $E$ be the standard basis for $\mathbb{R}^2$ and $C=\{\vec c_1,\vec c_2\}$ with $[\vec c_1]_E=\begin{bmatrix}2\\1\end{bmatrix}$, $[\vec c_2]_E=\begin{bmatrix}5\\3\end{bmatrix}$. Find a matrix $X$ with $X[\vec w]_C=[\vec w]_E$ for every $\vec w$, and a matrix $Y$ with $Y[\vec w]_E=[\vec w]_C$ for every $\vec w$. Use $Y$ to find $[\vec v]_C$ for $\vec v=2\vec e_1+2\vec e_2$.

$X$'s columns are just $\vec c_1,\vec c_2$ in standard coordinates:
$$X=\begin{bmatrix}2&5\\1&3\end{bmatrix},$$
since plugging $[\vec w]_C=\begin{bmatrix}1\\0\end{bmatrix}$ into $X[\vec w]_C$ must return $[\vec c_1]_E$, and plugging in $\begin{bmatrix}0\\1\end{bmatrix}$ must return $[\vec c_2]_E$ — exactly the two columns of $X$.

To convert the other way, $Y=X^{-1}$. Since $\det X=2(3)-5(1)=1$,
$$Y=X^{-1}=\dfrac{1}{1}\begin{bmatrix}3&-5\\-1&2\end{bmatrix}=\begin{bmatrix}3&-5\\-1&2\end{bmatrix}.$$
Now $[\vec v]_E=\begin{bmatrix}2\\2\end{bmatrix}$, so
$$[\vec v]_C=Y[\vec v]_E=\begin{bmatrix}3&-5\\-1&2\end{bmatrix}\begin{bmatrix}2\\2\end{bmatrix}=\begin{bmatrix}6-10\\-2+4\end{bmatrix}=\begin{bmatrix}-4\\2\end{bmatrix}.$$
Check with $X$: $X[\vec v]_C=\begin{bmatrix}2&5\\1&3\end{bmatrix}\begin{bmatrix}-4\\2\end{bmatrix}=\begin{bmatrix}-8+10\\-4+6\end{bmatrix}=\begin{bmatrix}2\\2\end{bmatrix}=[\vec v]_E$ ✓, confirming $YX=I$. $\blacksquare$

---

## Pages 4–5 — Practice Problems (unsolved)

**Writing Systems as Matrix Equations**

1. Rewrite the system $\begin{cases}x-y+z=1\\2x-y+z=2\\3x+y-z=3\end{cases}$ as a single matrix equation $A\vec x=\vec b$.
2. Let $A=\begin{bmatrix}2&1\\1&4\end{bmatrix}$, $\vec x=\begin{bmatrix}x\\y\end{bmatrix}$, $\vec b=\begin{bmatrix}7\\8\end{bmatrix}$. Write out the system of equations that the matrix equation $A\vec x=\vec b$ represents.

**Solving Matrix Equations & Interpreting Solutions**

3. Let $A=\begin{bmatrix}1&2\\3&3\end{bmatrix}$ and $\vec b=\begin{bmatrix}1\\7\end{bmatrix}$. Solve $A\vec x=\vec b$ by row reduction, then explain what your solution means (a) in terms of intersecting lines and (b) in terms of a linear combination of the columns of $A$.
4. Let $\vec u=\begin{bmatrix}1\\2\\3\end{bmatrix}$, $\vec v=\begin{bmatrix}4\\5\\6\end{bmatrix}$, $\vec w=\begin{bmatrix}7\\8\\9\end{bmatrix}$. Rephrase the question "is $\{\vec u,\vec v,\vec w\}$ linearly independent?" as a matrix equation, then row reduce to answer it.

**Homogeneous Systems, Orthogonality & Normal Vectors**

5. Find all vectors orthogonal to $\begin{bmatrix}0\\5\\6\end{bmatrix}$ and $\begin{bmatrix}1\\10\\2\end{bmatrix}$.
6. Express the plane $\vec x=t\begin{bmatrix}1\\6\\8\end{bmatrix}+s\begin{bmatrix}2\\0\\2\end{bmatrix}+\begin{bmatrix}0\\0\\9\end{bmatrix}$ in normal form.
7. Consider the system represented by $\operatorname{rref}(A)=\begin{bmatrix}1&-3&0\\0&0&1\\0&0&0\end{bmatrix}$, i.e. $\operatorname{rref}(A)\begin{bmatrix}x\\y\\z\end{bmatrix}=\vec b$. If $\vec b=\begin{bmatrix}1\\1\\0\end{bmatrix}$, is the solution set a point, line, plane, or other? What if $\vec b=\begin{bmatrix}1\\2\\3\end{bmatrix}$?

**Coordinates Relative to a Basis**

8. Let $\vec u=\vec e_1+8\vec e_2$ and $\vec v=-\vec e_1+3\vec e_2$ in $\mathbb{R}^2$. Find $[\vec u]_E$ and $[\vec v]_E$. Then let $A=\{3\vec e_1+2\vec e_2,\ 4\vec e_1-\vec e_2\}$; find $[\vec u]_A$ and $[\vec v]_A$.
9. Let $[\vec a]_E=\begin{bmatrix}5\\-12\end{bmatrix}$ where $E$ is the standard basis for $\mathbb{R}^2$. Find a basis $M$ for $\mathbb{R}^2$ such that $[\vec a]_M=\begin{bmatrix}1\\0\end{bmatrix}$.

**Change-of-Basis Matrices**

10. Let $E$ be the standard basis for $\mathbb{R}^2$ and $C=\{\vec c_1,\vec c_2\}$ with $[\vec c_1]_E=\begin{bmatrix}3\\1\end{bmatrix}$ and $[\vec c_2]_E=\begin{bmatrix}1\\1\end{bmatrix}$.
    - (a) Express $\vec e_1,\vec e_2$ as linear combinations of $\vec c_1,\vec c_2$.
    - (b) Find the matrix $X$ so that $X[\vec w]_C=[\vec w]_E$ for every $\vec w$.
    - (c) Find the matrix $Y$ so that $Y[\vec w]_E=[\vec w]_C$ for every $\vec w$.
    - (d) Compute $YX$ and explain, in words, why you got that answer.
11. Using the basis $C$ and matrices $X,Y$ from Problem 10: (a) find $[\vec w]_E$ given $[\vec w]_C=\begin{bmatrix}2\\-3\end{bmatrix}_C$; (b) find $[\vec w]_C$ given $[\vec w]_E=\begin{bmatrix}4\\1\end{bmatrix}_E$.
12. A student writes "$[\vec v]_B=\vec v$" for the basis $B=\left\{\begin{bmatrix}1\\1\end{bmatrix},\begin{bmatrix}1\\-1\end{bmatrix}\right\}$ and the vector $\vec v=\begin{bmatrix}4\\2\end{bmatrix}$. Explain what is wrong with this equation, then correctly compute $[\vec v]_B$.

---

## Answer Key & Misconception Notes (for tutor use — do not show student until after attempt)

| # | Answer | Common misconception |
|---|---|---|
| 1 | $\begin{bmatrix}1&-1&1\\2&-1&1\\3&1&-1\end{bmatrix}\begin{bmatrix}x\\y\\z\end{bmatrix}=\begin{bmatrix}1\\2\\3\end{bmatrix}$ | Putting the constants from the right-hand side into the coefficient matrix $A$ instead of into $\vec b$, or transposing rows and columns when copying coefficients into $A$. |
| 2 | $2x+y=7$ and $x+4y=8$ | Reading the matrix row-by-row but multiplying entries in the wrong order (e.g. writing $1x+2y=7$ by reading down a column of $A$ instead of across a row). |
| 3 | $x=\dfrac{11}{3}$, $y=-\dfrac{4}{3}$. (a) The lines $x+2y=1$ and $3x+3y=7$ cross at $\left(\dfrac{11}{3},-\dfrac{4}{3}\right)$. (b) $\dfrac{11}{3}\begin{bmatrix}1\\3\end{bmatrix}-\dfrac{4}{3}\begin{bmatrix}2\\3\end{bmatrix}=\begin{bmatrix}1\\7\end{bmatrix}$. | Forgetting that $x$ and $y$ play *two* roles simultaneously (the intersection point **and** the combination coefficients) and trying to compute a totally separate "combination answer" instead of reusing the row-reduction solution. |
| 4 | Dependent: solving $c_1\vec u+c_2\vec v+c_3\vec w=\vec 0$ (columns of $\begin{bmatrix}1&4&7\\2&5&8\\3&6&9\end{bmatrix}$) gives a free variable, e.g. $\vec u-2\vec v+\vec w=\vec 0$. | Assuming three vectors in $\mathbb{R}^3$ must automatically be independent, without actually row reducing to check for a free variable (a zero row appears after elimination here). |
| 5 | $\vec x=t\begin{bmatrix}10\\-6/5\\1\end{bmatrix}$ (or any scalar multiple, e.g. $t\begin{bmatrix}50\\-6\\5\end{bmatrix}$) | Setting up the matrix with the given vectors as **columns** instead of **rows** — the row picture requires the vectors you want orthogonality to be the rows of $A$. |
| 6 | Normal vector $\vec n=\begin{bmatrix}6\\7\\-6\end{bmatrix}$; normal form $\begin{bmatrix}6\\7\\-6\end{bmatrix}\cdot\left(\vec x-\begin{bmatrix}0\\0\\9\end{bmatrix}\right)=0$ | Using the given point vector $\begin{bmatrix}0\\0\\9\end{bmatrix}$ as if it were a direction vector when building the matrix $A$ to row reduce, instead of only using $\vec d_1,\vec d_2$. |
| 7 | $\vec b=(1,1,0)$: a line (one free variable, $y$). $\vec b=(1,2,3)$: no solution at all ("other") because the last row demands $0=3$. | Seeing a zero row in $\operatorname{rref}(A)$ and assuming it always contributes a free variable / infinite solutions, without checking whether the corresponding entry of $\vec b$ makes that row's equation $0=(\text{nonzero})$, i.e. inconsistent. |
| 8 | $[\vec u]_E=\begin{bmatrix}1\\8\end{bmatrix}$, $[\vec v]_E=\begin{bmatrix}-1\\3\end{bmatrix}$; $[\vec u]_A=\begin{bmatrix}3\\-2\end{bmatrix}$, $[\vec v]_A=\begin{bmatrix}1\\-1\end{bmatrix}$ | Trying to read $[\vec u]_A$ off "by inspection" the way you can for the standard basis, instead of setting up and solving $x(3\vec e_1+2\vec e_2)+y(4\vec e_1-\vec e_2)=\vec u$ as a system. |
| 9 | E.g. $M=\left\{\begin{bmatrix}5\\-12\end{bmatrix},\begin{bmatrix}0\\1\end{bmatrix}\right\}$ (any second vector not parallel to $(5,-12)$ works) | Not realizing that $[\vec a]_M=\begin{bmatrix}1\\0\end{bmatrix}$ literally means $\vec a$ **is** the first basis vector of $M$ — instead trying to solve for $M$ using row reduction as if it were a coordinate-finding problem. |
| 10 | (a) $\vec e_1=\dfrac12\vec c_1-\dfrac12\vec c_2$, $\vec e_2=-\dfrac12\vec c_1+\dfrac32\vec c_2$. (b) $X=\begin{bmatrix}3&1\\1&1\end{bmatrix}$. (c) $Y=X^{-1}=\begin{bmatrix}1/2&-1/2\\-1/2&3/2\end{bmatrix}$. (d) $YX=I$, since converting $C$-coordinates to $E$-coordinates and back to $C$-coordinates returns the original coordinates unchanged. | Building $X$ from the equations in part (a) instead of directly from $\vec c_1,\vec c_2$ (the columns of $X$ are simply $[\vec c_1]_E$ and $[\vec c_2]_E$ — no system-solving needed for $X$ itself, only for $Y$). |
| 11 | (a) $[\vec w]_E=X\begin{bmatrix}2\\-3\end{bmatrix}=\begin{bmatrix}3\\-1\end{bmatrix}$. (b) $[\vec w]_C=Y\begin{bmatrix}4\\1\end{bmatrix}=\begin{bmatrix}3/2\\-1/2\end{bmatrix}$ | Using $X$ when $Y$ is needed (or vice versa) — i.e. multiplying by the change-of-basis matrix that converts the wrong direction. |
| 12 | $[\vec v]_B=\begin{bmatrix}3\\1\end{bmatrix} \neq \vec v=\begin{bmatrix}4\\2\end{bmatrix}$: a representation is a list of numbers, only meaningful once tied to a basis, while $\vec v$ is a true (geometric) vector — they are different kinds of objects, so the equation as literally written is a category error, even though it happens that $[\vec v]_E=\vec v$'s numerical coordinates. | Believing $[\vec v]_B$ and $\vec v$ "are the same thing, just written differently," rather than recognizing they answer different questions (one names the vector's coordinates in $B$, the other names the vector itself) — the exact confusion the True-Vectors-vs-Representations fact is meant to prevent. |
