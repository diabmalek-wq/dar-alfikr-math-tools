# Week 12 — Inverse Functions & Inverse Matrices; Change of Basis II

**Session length:** 3 hours
**Source:** Siefken, *MAT223 Workbook*, Module 12 (Inverse Functions & Inverse Matrices) and Module 13 (Change of Basis II)

---

## Page 1 — Introduction, Key Facts & Definitions

### Why this matters

Recently you learned to compute the rank and nullity of a matrix and connect them with the rank-nullity theorem. This week asks a natural question: when can a linear transformation — or the matrix that represents it — be *undone*? The answer turns out to be exactly the rank/nullity conditions you already know how to check. Once we know how to invert a matrix, we get a second way to solve $A\vec x=\vec b$ (multiply both sides by $A^{-1}$) and a systematic row-reduction method that inverts any invertible square matrix. The second half of this week extends Week 9's Change of Basis I: there you converted coordinates to and from the *standard* basis $E$; now you'll convert directly between two **non-standard** bases, and see that change-of-basis matrices are always invertible — in fact, "invertible" and "is a change-of-basis matrix" turn out to describe exactly the same set of matrices.

### Definition: Identity Function

*(Source subsection: Invertible Functions)*

Let $X$ be a set. The **identity function** with domain and codomain $X$, notated $\operatorname{id}:X\to X$, is the function satisfying
$$\operatorname{id}(x)=x \quad \text{for all } x\in X.$$
The identity function does nothing to its input; in the world of matrices, the identity matrix $I$ plays this role.

### Definition: Inverse Function

*(Source subsection: Invertible Functions)*

Let $f:X\to Y$ be a function. We say $f$ is **invertible** if there exists a function $g:Y\to X$ so that
$$f\circ g=\operatorname{id} \quad \text{and} \quad g\circ f=\operatorname{id}.$$
In this case $g$ is called an inverse of $f$, and we write $f^{-1}=g$.

### Definition: One-to-One and Onto

*(Source subsection: Invertible Functions)*

Let $f:X\to Y$ be a function.

- $f$ is **one-to-one** (or *injective*) if distinct inputs produce distinct outputs: $f(x)=f(y)$ implies $x=y$.
- $f$ is **onto** (or *surjective*) if every point of the codomain gets mapped to: $\operatorname{range}(f)=Y$.

**Every invertible function is both one-to-one and onto, and every one-to-one and onto function is invertible.**

### Fact: Invertibility of a Linear Transformation via Rank and Nullity

*(Source subsection: Invertibility and Linear Transformations)*

A linear transformation $T:\mathbb{R}^n\to\mathbb{R}^m$ is invertible if and only if it is one-to-one and onto. Combined with the rank-nullity theorem ($\operatorname{rank}(T)+\operatorname{nullity}(T)=n$), this is equivalent to any one of:

- $\operatorname{nullity}(T)=0$ and $\operatorname{rank}(T)=m$;
- $m=n$ and $\operatorname{nullity}(T)=0$;
- $m=n$ and $\operatorname{rank}(T)=m$.

If $T$ is invertible, its inverse $T^{-1}$ is also a linear transformation.

### Definition: Identity Matrix and Matrix Inverse

*(Source subsection: Invertibility and Matrices)*

An **identity matrix** is a square matrix with ones on the diagonal and zeros everywhere else, denoted $I_{n\times n}$ or just $I$.

The **inverse of a matrix $A$** is a matrix $B$ such that
$$AB=I \qquad \text{and} \qquad BA=I.$$
In this case $B$ is called the inverse of $A$ and is notated $A^{-1}$.

### Fact: Invertibility of a Matrix via Rank and Nullity

*(Source subsection: Invertibility and Matrices)*

Since every matrix induces a linear transformation, the facts above translate directly to matrices:

- An $n\times m$ matrix $A$ is invertible if and only if $\operatorname{nullity}(A)=0$ and $\operatorname{rank}(A)=n$.
- An $n\times n$ matrix $A$ is invertible if and only if $\operatorname{nullity}(A)=0$.
- An $n\times n$ matrix $A$ is invertible if and only if $\operatorname{rank}(A)=n$.

In particular, **a non-square matrix can never be invertible.**

### Fact: Using the Inverse to Solve $A\vec x=\vec b$

*(Source subsection: Matrix Algebra)*

If $A$ is invertible, then
$$A\vec x=\vec b \implies A^{-1}A\vec x=A^{-1}\vec b \implies \vec x=A^{-1}\vec b.$$
**Order matters.** Unlike scalar algebra, you cannot rearrange freely: $A\vec x=\vec b$ does **not** imply $\vec x=\vec b A^{-1}$ (if $\vec b$ is a column vector, $\vec bA^{-1}$ is almost always undefined). $A^{-1}$ must multiply on the correct side, consistently, on both sides of the equation.

### Fact: Finding a Matrix Inverse by Row Reduction

*(Source subsection: Finding a Matrix Inverse / Elementary Matrices and Inverses)*

Because $\vec x=A^{-1}\vec b$ is always the unique solution to $A\vec x=\vec b$, plugging in $\vec b=\vec e_1,\ldots,\vec e_n$ one at a time and solving for $\vec x$ builds up the columns of $A^{-1}$ one by one. Doing this for every $\vec e_i$ simultaneously is exactly the same as row-reducing the augmented matrix
$$[A\mid I] \;\longrightarrow\; [I\mid A^{-1}],$$
applying the *same* row operations to both blocks at once. If, partway through, a row of the **left**-hand block becomes entirely zero, $A$ cannot row-reduce to $I$, so $\operatorname{rank}(A)<n$ and $A$ is **not invertible** — you can stop immediately, no further work needed.

*(Recall from Week 9: for a $2\times2$ matrix $\begin{bmatrix}a&b\\c&d\end{bmatrix}$ with $ad-bc\neq 0$, the shortcut $A^{-1}=\dfrac{1}{ad-bc}\begin{bmatrix}d&-b\\-c&a\end{bmatrix}$ agrees with row reduction — but the row-reduction method below is the one that generalizes to any size matrix.)*

### Definition: Elementary Matrix

*(Source subsection: Elementary Matrices)*

A matrix is called an **elementary matrix** if it is an identity matrix with a single elementary row operation applied (multiply a row by a non-zero constant; add a multiple of one row to another; or swap two rows). Multiplying by an elementary matrix *performs* the corresponding row operation.

### Theorem: Invertibility, Elementary Matrices, and $AB=I$

*(Source subsection: Elementary Matrices and Inverses / Decomposition into Elementary Matrices)*

- A matrix $M$ is invertible if and only if there exist elementary matrices $E_1,\ldots,E_k$ with $E_k\cdots E_2E_1M=I$; in that case $M^{-1}=E_k\cdots E_2E_1$.
- A matrix $M$ is invertible if and only if it can be written as a product of elementary matrices.
- **If $A$ is a square matrix and $AB=I$ for some matrix $B$, then $BA=I$ as well.** So for *square* matrices, checking $AB=I$ alone is enough to conclude $B=A^{-1}$. This is exactly what row-reducing $[A\mid I]$ to $[I\mid A^{-1}]$ is doing behind the scenes: the sequence of row operations *is* the sequence of elementary matrices $E_k\cdots E_1$ applied to $A$ on the left, and applying that same sequence to $I$ produces $A^{-1}$.

### Fact: Coordinates Convert Between Any Two Bases

*(Source subsection: Change of Basis II — Introduction)*

Week 9 (Change of Basis I) converted coordinates to and from the *standard* basis $E$ only. In general, given **any** two bases $A$ and $B$ for $\mathbb{R}^n$, a vector $\vec x$ has two equally valid coordinate representations, $[\vec x]_A$ and $[\vec x]_B$, and there is always a function converting between them: plug the numbers in $[\vec x]_A$ in as coefficients of the $A$-basis vectors to recover the true vector $\vec x$, then re-express that same $\vec x$ in the $B$ basis. Neither basis has to be the standard basis.

### Definition: Change of Basis Matrix (General Case)

*(Source subsection: Change of Basis Matrix)*

Let $A$ and $B$ be bases for $\mathbb{R}^n$. The matrix $M$ is called the **change of basis matrix** converting from $A$ to $B$ if
$$M[\vec x]_A=[\vec x]_B \quad \text{for all } \vec x\in\mathbb{R}^n.$$
We notate this matrix $[B\leftarrow A]$, so $M=[B\leftarrow A]$. If $A=\{\vec a_1,\ldots,\vec a_n\}$, the columns of $[B\leftarrow A]$ are $[\vec a_1]_B,\ldots,[\vec a_n]_B$.

### Fact: Change-of-Basis Matrices Compose

*(Source subsection: Change of Basis Matrix)*

For bases $A,B,C$ of $\mathbb{R}^n$,
$$[C\leftarrow A]=[C\leftarrow B][B\leftarrow A].$$
The notation is built so the "inner" basis label ($B$) cancels, just like the arrows chain: $[\vec x]_C=[C\leftarrow B][B\leftarrow A][\vec x]_A$.

### Fact: Change-of-Basis Matrices Are Always Invertible

*(Source subsection: Change of Basis Matrix in Detail)*

If $M=[B\leftarrow A]$, then $M^{-1}=[A\leftarrow B]$, since
$$M^{-1}M=[A\leftarrow B][B\leftarrow A]=[A\leftarrow A]=I, \qquad MM^{-1}=[B\leftarrow A][A\leftarrow B]=[B\leftarrow B]=I.$$
($[A\leftarrow A]$ and $[B\leftarrow B]$ do nothing to a vector's coordinates — converting a basis to itself changes nothing.)

### Theorem: Invertible $\iff$ Change of Basis Matrix

*(Source subsection: Change of Basis Matrix in Detail)*

**An $n\times n$ matrix is invertible if and only if it is a change of basis matrix.** If $M=[B\leftarrow A]$, then $M^{-1}=[A\leftarrow B]$ exists, so $M$ is invertible. Conversely, if $M=[\,\vec C_1\mid\cdots\mid\vec C_n\,]$ is invertible, reading its columns as standard-coordinate vectors $\vec c_i$ gives a basis $C=\{\vec c_1,\ldots,\vec c_n\}$ of $\mathbb{R}^n$, and $M=[E\leftarrow C]$.

This links directly back to Module 12: invertibility of a square matrix, having zero nullity (full rank), and being *some* change-of-basis matrix are all the very same condition.

---

## Pages 2–3 — Solved Examples

**Example 1 (Verify two matrices are inverses of each other).** Let $A=\begin{bmatrix}2&5\\-3&-7\end{bmatrix}$ and $B=\begin{bmatrix}-7&-5\\3&2\end{bmatrix}$. Determine whether $A$ and $B$ are inverses of each other.

We must check **both** products.
$$AB=\begin{bmatrix}2&5\\-3&-7\end{bmatrix}\begin{bmatrix}-7&-5\\3&2\end{bmatrix}=\begin{bmatrix}2(-7)+5(3)&2(-5)+5(2)\\-3(-7)+(-7)(3)&-3(-5)+(-7)(2)\end{bmatrix}=\begin{bmatrix}1&0\\0&1\end{bmatrix}=I.$$
$$BA=\begin{bmatrix}-7&-5\\3&2\end{bmatrix}\begin{bmatrix}2&5\\-3&-7\end{bmatrix}=\begin{bmatrix}-7(2)+(-5)(-3)&-7(5)+(-5)(-7)\\3(2)+2(-3)&3(5)+2(-7)\end{bmatrix}=\begin{bmatrix}1&0\\0&1\end{bmatrix}=I.$$
Since $AB=I$ **and** $BA=I$, $A$ and $B$ are inverses of each other: $B=A^{-1}$. $\blacksquare$

**Example 2 ($AB=I$ is not, by itself, enough — squareness matters).** Let $A=\begin{bmatrix}2&5&0\\-3&-7&0\end{bmatrix}$ (a $2\times3$ matrix) and $B=\begin{bmatrix}-7&-5\\3&2\\1&1\end{bmatrix}$ (a $3\times2$ matrix). Determine whether $A$ and $B$ are inverses of each other.

$$AB=\begin{bmatrix}2&5&0\\-3&-7&0\end{bmatrix}\begin{bmatrix}-7&-5\\3&2\\1&1\end{bmatrix}=\begin{bmatrix}1&0\\0&1\end{bmatrix}=I.$$
So far so good — but the *other* order gives something different:
$$BA=\begin{bmatrix}-7&-5\\3&2\\1&1\end{bmatrix}\begin{bmatrix}2&5&0\\-3&-7&0\end{bmatrix}=\begin{bmatrix}1&0&0\\0&1&0\\-1&-2&0\end{bmatrix}\neq I.$$
(For instance, entry $(3,1)$ of $BA$ is $1(2)+1(-3)=-1$.) So $A$ and $B$ are **not** inverses of each other, even though $AB=I$. This does not contradict "$A$ square and $AB=I$ implies $BA=I$" — that theorem requires $A$ to be square, and here $A$ is $2\times3$, so it never applies. Neither $A$ nor $B$ is even square, so neither can be invertible in the first place. $\blacksquare$

**Example 3 (Compute a $2\times2$ inverse by row-reducing $[A\mid I]$).** Let $A=\begin{bmatrix}3&1\\5&2\end{bmatrix}$. Find $A^{-1}$.

$$\left[\begin{array}{cc|cc}3&1&1&0\\5&2&0&1\end{array}\right]\xrightarrow{R_1\div3}\left[\begin{array}{cc|cc}1&1/3&1/3&0\\5&2&0&1\end{array}\right]\xrightarrow{R_2-5R_1}\left[\begin{array}{cc|cc}1&1/3&1/3&0\\0&1/3&-5/3&1\end{array}\right]$$
$$\xrightarrow{R_2\times3}\left[\begin{array}{cc|cc}1&1/3&1/3&0\\0&1&-5&3\end{array}\right]\xrightarrow{R_1-\frac13R_2}\left[\begin{array}{cc|cc}1&0&2&-1\\0&1&-5&3\end{array}\right].$$
So $A^{-1}=\begin{bmatrix}2&-1\\-5&3\end{bmatrix}$. Check: $AA^{-1}=\begin{bmatrix}3&1\\5&2\end{bmatrix}\begin{bmatrix}2&-1\\-5&3\end{bmatrix}=\begin{bmatrix}6-5&-3+3\\10-10&-5+6\end{bmatrix}=\begin{bmatrix}1&0\\0&1\end{bmatrix}=I.$ $\blacksquare$

**Example 4 (Compute a $3\times3$ inverse by row-reducing $[A\mid I]$).** Let $A=\begin{bmatrix}1&2&0\\0&4&0\\0&-1&1\end{bmatrix}$. Find $A^{-1}$.

$$\left[\begin{array}{ccc|ccc}1&2&0&1&0&0\\0&4&0&0&1&0\\0&-1&1&0&0&1\end{array}\right]\xrightarrow{R_2\div4}\left[\begin{array}{ccc|ccc}1&2&0&1&0&0\\0&1&0&0&1/4&0\\0&-1&1&0&0&1\end{array}\right]$$
$$\xrightarrow{R_3+R_2}\left[\begin{array}{ccc|ccc}1&2&0&1&0&0\\0&1&0&0&1/4&0\\0&0&1&0&1/4&1\end{array}\right]\xrightarrow{R_1-2R_2}\left[\begin{array}{ccc|ccc}1&0&0&1&-1/2&0\\0&1&0&0&1/4&0\\0&0&1&0&1/4&1\end{array}\right].$$
So
$$A^{-1}=\begin{bmatrix}1&-\dfrac12&0\\[4pt]0&\dfrac14&0\\[4pt]0&\dfrac14&1\end{bmatrix}.$$
(This same $A^{-1}$ can also be assembled as a product of elementary matrices $E_3E_2E_1$, one per row operation above — row-reducing $[A\mid I]$ performs exactly that computation all at once.) $\blacksquare$

**Example 5 (Recognize a non-invertible matrix).** Let $A=\begin{bmatrix}1&2&3\\2&4&6\\1&1&1\end{bmatrix}$. Determine whether $A$ is invertible.

Begin row-reducing $[A\mid I]$:
$$\left[\begin{array}{ccc|ccc}1&2&3&1&0&0\\2&4&6&0&1&0\\1&1&1&0&0&1\end{array}\right]\xrightarrow{R_2-2R_1}\left[\begin{array}{ccc|ccc}1&2&3&1&0&0\\0&0&0&-2&1&0\\1&1&1&0&0&1\end{array}\right].$$
Row 2 of the **left**-hand block is already entirely zero (because row 2 of $A$ is exactly twice row 1), so $A$ cannot row-reduce to $I$. There is no need to continue: $A$ is **not invertible**. (Equivalently: the rows of $A$ are linearly dependent, so $\operatorname{rank}(A)<3$ and $\operatorname{nullity}(A)>0$.) $\blacksquare$

**Example 6 (Convert coordinates between two non-standard bases).** Let $A=\{\vec a_1,\vec a_2\}$ with $\vec a_1=\begin{bmatrix}1\\1\end{bmatrix}_E$, $\vec a_2=\begin{bmatrix}1\\-1\end{bmatrix}_E$, and $B=\{\vec b_1,\vec b_2\}$ with $\vec b_1=\begin{bmatrix}2\\1\end{bmatrix}_E$, $\vec b_2=\begin{bmatrix}5\\3\end{bmatrix}_E$, both bases for $\mathbb{R}^2$. Given $[\vec x]_A=\begin{bmatrix}2\\-3\end{bmatrix}$, find $[\vec x]_B$.

Neither basis is standard, so we pass through the true vector $\vec x$. By definition of $[\vec x]_A$:
$$\vec x=2\vec a_1-3\vec a_2=2(\vec e_1+\vec e_2)-3(\vec e_1-\vec e_2)=-\vec e_1+5\vec e_2.$$
Now write this same $\vec x$ as a combination of $\vec b_1,\vec b_2$: we need $\alpha,\beta$ with
$$-\vec e_1+5\vec e_2=\alpha(2\vec e_1+\vec e_2)+\beta(5\vec e_1+3\vec e_2)=(2\alpha+5\beta)\vec e_1+(\alpha+3\beta)\vec e_2.$$
Matching coefficients of $\vec e_1,\vec e_2$ (they are linearly independent, so coefficients must match exactly):
$$2\alpha+5\beta=-1, \qquad \alpha+3\beta=5.$$
From the second equation, $\alpha=5-3\beta$. Substituting: $2(5-3\beta)+5\beta=-1 \Rightarrow 10-\beta=-1 \Rightarrow \beta=11$, so $\alpha=5-3(11)=-28$. Therefore
$$[\vec x]_B=\begin{bmatrix}-28\\11\end{bmatrix}. \qquad \blacksquare$$

**Example 7 (Build a change-of-basis matrix directly).** Using the same $A,B$ as Example 6, find $[B\leftarrow A]$.

$[B\leftarrow A]$'s columns are $[\vec a_1]_B$ and $[\vec a_2]_B$. For $\vec a_1=(1,1)$: solve $\alpha(2,1)+\beta(5,3)=(1,1)$, i.e. $2\alpha+5\beta=1,\ \alpha+3\beta=1$. Then $\alpha=1-3\beta$, so $2(1-3\beta)+5\beta=1 \Rightarrow 2-\beta=1 \Rightarrow \beta=1$, $\alpha=-2$. So $[\vec a_1]_B=\begin{bmatrix}-2\\1\end{bmatrix}$.

For $\vec a_2=(1,-1)$: solve $2\alpha+5\beta=1,\ \alpha+3\beta=-1$. Then $\alpha=-1-3\beta$, so $2(-1-3\beta)+5\beta=1 \Rightarrow -2-\beta=1 \Rightarrow \beta=-3$, $\alpha=8$. So $[\vec a_2]_B=\begin{bmatrix}8\\-3\end{bmatrix}$.

Therefore
$$[B\leftarrow A]=\begin{bmatrix}-2&8\\1&-3\end{bmatrix}.$$
Check against Example 6: $[B\leftarrow A][\vec x]_A=\begin{bmatrix}-2&8\\1&-3\end{bmatrix}\begin{bmatrix}2\\-3\end{bmatrix}=\begin{bmatrix}-4-24\\2+9\end{bmatrix}=\begin{bmatrix}-28\\11\end{bmatrix}=[\vec x]_B$ ✓. $\blacksquare$

**Example 8 (Compose two change-of-basis matrices).** Keep $A,B$ from Examples 6–7, and let $C=\{\vec c_1,\vec c_2\}$ with $\vec c_1=\begin{bmatrix}1\\0\end{bmatrix}_E$, $\vec c_2=\begin{bmatrix}1\\1\end{bmatrix}_E$. Find $[C\leftarrow B]$, use composition to find $[C\leftarrow A]$, and verify directly.

*Step 1 — find $[C\leftarrow B]$.* Its columns are $[\vec b_1]_C,[\vec b_2]_C$. For $\vec b_1=(2,1)$: solve $x(1,0)+y(1,1)=(2,1)$, i.e. $x+y=2,\ y=1$, so $y=1,x=1$: $[\vec b_1]_C=\begin{bmatrix}1\\1\end{bmatrix}$. For $\vec b_2=(5,3)$: $x+y=5,\ y=3$, so $y=3,x=2$: $[\vec b_2]_C=\begin{bmatrix}2\\3\end{bmatrix}$. Thus
$$[C\leftarrow B]=\begin{bmatrix}1&2\\1&3\end{bmatrix}.$$

*Step 2 — compose.* Using $[B\leftarrow A]=\begin{bmatrix}-2&8\\1&-3\end{bmatrix}$ from Example 7:
$$[C\leftarrow A]=[C\leftarrow B][B\leftarrow A]=\begin{bmatrix}1&2\\1&3\end{bmatrix}\begin{bmatrix}-2&8\\1&-3\end{bmatrix}=\begin{bmatrix}1(-2)+2(1)&1(8)+2(-3)\\1(-2)+3(1)&1(8)+3(-3)\end{bmatrix}=\begin{bmatrix}0&2\\1&-1\end{bmatrix}.$$

*Step 3 — verify directly.* $[C\leftarrow A]$'s columns should be $[\vec a_1]_C,[\vec a_2]_C$. For $\vec a_1=(1,1)$: $x+y=1,\ y=1 \Rightarrow x=0$: $[\vec a_1]_C=\begin{bmatrix}0\\1\end{bmatrix}$. For $\vec a_2=(1,-1)$: $x+y=1,\ y=-1 \Rightarrow x=2$: $[\vec a_2]_C=\begin{bmatrix}2\\-1\end{bmatrix}$. Directly, $[C\leftarrow A]=\begin{bmatrix}0&2\\1&-1\end{bmatrix}$ — exactly matching Step 2. $\blacksquare$

---

## Pages 4–5 — Practice Problems (unsolved)

**Invertible Functions & Linear Transformations**

1. Classify each transformation below as one-to-one, onto, both, or neither, and state whether it is invertible. Justify each answer.
    - (a) $R:\mathbb{R}^2\to\mathbb{R}^2$, rotation clockwise by $72°$.
    - (b) $P:\mathbb{R}^2\to\mathbb{R}^2$, projection onto the $y$-axis.
    - (c) $F:\mathbb{R}^2\to\mathbb{R}^2$, reflection over the line $y=x$.
    - (d) $U:\mathbb{R}^3\to\mathbb{R}^2$, induced by the matrix $M_U=\begin{bmatrix}1&2&3\\3&4&5\end{bmatrix}$.
2. Let $T:\mathbb{R}^3\to\mathbb{R}^3$ be induced by $M_T=\begin{bmatrix}1&2&3\\4&5&6\\7&8&9\end{bmatrix}$. Determine whether $T$ is invertible, using rank and nullity to justify your answer.

**Verifying and Computing Matrix Inverses ($2\times2$)**

3. Determine whether $M_1=\begin{bmatrix}2&3\\1&-1\end{bmatrix}$ is invertible; if so, find $M_1^{-1}$ by row-reducing $[M_1\mid I]$.
4. Determine whether $M_2=\begin{bmatrix}1&0\\1&0\end{bmatrix}$ is invertible. Justify your answer *without* doing a full row reduction.
5. Verify by direct multiplication whether $\begin{bmatrix}1&2\\3&5\end{bmatrix}$ and $\begin{bmatrix}-5&2\\3&-1\end{bmatrix}$ are inverses of each other.

**Matrix Inverses via Row Reduction of $[A\mid I]$ (Including Non-Invertible Cases)**

6. Find $M_3^{-1}$ for $M_3=\begin{bmatrix}0&2&1\\1&0&1\\-2&3&0\end{bmatrix}$ by row-reducing $[M_3\mid I]$, or show it does not exist.
7. Explain, without row reducing, why $M_4=\begin{bmatrix}2&0&1&8\\1&-5&2&2\\3&-1&0&7\end{bmatrix}$ cannot possibly be invertible.
8. Let $A=\begin{bmatrix}1&1&2\\2&2&4\\1&0&1\end{bmatrix}$. Attempt to find $A^{-1}$ by row-reducing $[A\mid I]$. What happens, and what does it tell you about $A$?

**Using Inverses to Solve Systems**

9. Solve the system $\begin{cases}2x+y=5\\3x+7y=3\end{cases}$ two ways: (i) by row reduction, and (ii) by finding the coefficient matrix's inverse and computing $\vec x=A^{-1}\vec b$.
10. A classmate says: "Since $A\vec x=\vec b$ gives $\vec x=A^{-1}\vec b$, it must also be true that $\vec b=\vec xA^{-1}$ works the same way, just rearranged." Explain what is wrong with this reasoning.

**Change of Basis Between Two Non-Standard Bases**

11. Let $A=\left\{\begin{bmatrix}2\\1\end{bmatrix}_E,\begin{bmatrix}1\\-2\end{bmatrix}_E\right\}$ and $B=\left\{\begin{bmatrix}3\\-1\end{bmatrix}_E,\begin{bmatrix}-2\\3\end{bmatrix}_E\right\}$ be bases for $\mathbb{R}^2$, and let $\vec x$ satisfy $[\vec x]_A=\begin{bmatrix}1\\-1\end{bmatrix}$.
    - (a) Find $[\vec x]_E$.
    - (b) Find $[\vec x]_B$ (first find $\vec x$ in standard coordinates, then re-express it in the $B$ basis).
12. Using the bases $A$ and $B$ from Problem 11, find the change-of-basis matrices $[E\leftarrow A]$, $[A\leftarrow E]$, and $[B\leftarrow A]$.

**Composing Change-of-Basis Matrices & Conceptual Checks**

13. Let $E$ be the standard basis for $\mathbb{R}^3$, let $A=\left\{\begin{bmatrix}2\\1\\0\end{bmatrix}_E,\begin{bmatrix}1\\-2\\0\end{bmatrix}_E,\begin{bmatrix}0\\0\\1\end{bmatrix}_E\right\}$, and let $B=\{\vec b_1,\vec b_2,\vec b_3\}$ where $[\vec b_1]_A=\begin{bmatrix}1\\0\\0\end{bmatrix}$, $[\vec b_2]_A=\begin{bmatrix}1\\1\\0\end{bmatrix}$, $[\vec b_3]_A=\begin{bmatrix}1\\1\\1\end{bmatrix}$.
    - (a) Find $\vec b_1,\vec b_2,\vec b_3$ in standard coordinates.
    - (b) Find the change-of-basis matrices $[A\leftarrow E]$ and $[E\leftarrow B]$.
    - (c) Use your answers to (b) to compute $[A\leftarrow B]$.
14. True or false, with justification: "Every invertible $n\times n$ matrix can be viewed as a change-of-basis matrix (converting from some basis to the standard basis)."

---

## Answer Key & Misconception Notes (for tutor use — do not show student until after attempt)

| # | Answer | Common misconception |
|---|---|---|
| 1 | (a) $R$: one-to-one and onto (rotations are always bijective), invertible — inverse is rotation counter-clockwise by $72°$. (b) $P$: neither one-to-one nor onto (e.g. $P(0,0)=P(0,2)$; range is only the $y$-axis, not all of $\mathbb{R}^2$), not invertible. (c) $F$: one-to-one and onto (reflections are their own inverse), invertible. (d) $U$: onto ($\operatorname{rank}=2=m$) but not one-to-one ($\operatorname{nullity}=3-2=1>0$), so not invertible. | For (a)/(c), assuming a transformation must have an "obvious formula" in mind before calling it invertible, instead of reasoning from one-to-one/onto directly. For (d), assuming onto alone (or "it maps everywhere") is enough for invertibility, forgetting one-to-one is also required — which forces $m=n$. |
| 2 | Row reducing $M_T$ gives a zero row (row 3 $-$ row 1 $=$ (6,6,6), and row 2 $-$ 4(row1) then combining shows dependency), so $\operatorname{rank}(M_T)=2<3$, $\operatorname{nullity}(M_T)=1\neq0$. Since $M_T$ is square but nullity $\neq0$, $T$ is **not invertible**. | Assuming a square matrix filled with "ordinary-looking" consecutive integers must be invertible without actually checking rank; skipping the row reduction because the matrix "looks generic." |
| 3 | $M_1^{-1}=\dfrac{1}{5}\begin{bmatrix}1&3\\1&-2\end{bmatrix}=\begin{bmatrix}1/5&3/5\\1/5&-2/5\end{bmatrix}$ | Sign or arithmetic slip when subtracting a multiple of one row from another, or forgetting to divide *both* sides (left and right blocks) of a row by the same pivot value. |
| 4 | Not invertible: the second column of $M_2$ is $\begin{bmatrix}0\\0\end{bmatrix}$, so $M_2\begin{bmatrix}0\\1\end{bmatrix}=\vec 0$ with $\begin{bmatrix}0\\1\end{bmatrix}\neq\vec0$, meaning $\operatorname{nullity}(M_2)\neq0$. | Starting a full row reduction of $[M_2\mid I]$ instead of noticing immediately that a zero column (or any pair of dependent columns) rules out invertibility on the spot. |
| 5 | Yes, they are inverses: $\begin{bmatrix}1&2\\3&5\end{bmatrix}\begin{bmatrix}-5&2\\3&-1\end{bmatrix}=\begin{bmatrix}1&0\\0&1\end{bmatrix}$ and $\begin{bmatrix}-5&2\\3&-1\end{bmatrix}\begin{bmatrix}1&2\\3&5\end{bmatrix}=\begin{bmatrix}1&0\\0&1\end{bmatrix}$. | Computing only one of the two products (usually just $AB$) and declaring them inverses without citing the theorem that, for *square* matrices, $AB=I$ alone forces $BA=I$ — the check works here, but only because both matrices are square. |
| 6 | $M_3^{-1}=\begin{bmatrix}3&-3&-2\\2&-2&-1\\-3&4&2\end{bmatrix}$ | Getting stuck (or dividing by zero) at the first pivot because the $(1,1)$ entry of $M_3$ is $0$, instead of swapping rows first to bring a non-zero entry into the pivot position. |
| 7 | $M_4$ is $3\times4$, not square. A matrix must be square before $AB=I=BA$ can even be asked as a same-size equation, so a non-square matrix can never have a two-sided inverse — this rules out invertibility instantly, with no row reduction needed. | Trying to row-reduce the rectangular matrix or compute a "one-sided" inverse, not realizing squareness is a prerequisite check that should happen *before* any arithmetic. |
| 8 | Row 2 of $A$ equals $2\times$row 1, so $R_2-2R_1$ immediately produces a zero row on the left of $[A\mid I]$ (specifically $[0,0,0\mid{-2},1,0]$). This means $A$ cannot reduce to $I$, so $A$ is **not invertible**; there is no need to continue row reducing. | Continuing to grind through further row operations after a zero row already appears on the left, instead of stopping immediately and reporting non-invertibility — or misreading the zero row as "the inverse has a zero row" rather than "no inverse exists." |
| 9 | $x=\dfrac{32}{11}$, $y=-\dfrac{9}{11}$ by both methods. Row reduction gives the same pair directly; via the inverse, $A^{-1}=\dfrac{1}{11}\begin{bmatrix}7&-1\\-3&2\end{bmatrix}$ and $A^{-1}\vec b=\dfrac{1}{11}\begin{bmatrix}32\\-9\end{bmatrix}$. | Sign error in the $2\times2$ inverse shortcut (swapping which entries get negated), or multiplying $\vec bA^{-1}$ instead of $A^{-1}\vec b$ (wrong side/order). |
| 10 | False. Matrix multiplication is not commutative, and $\vec xA^{-1}$ (a column vector times a matrix, in that order) is typically not even defined — and even where some product is defined, it will not in general equal $\vec b$. The only valid manipulation is multiplying $A^{-1}$ on the **left** of both sides of $A\vec x=\vec b$, consistently. | This *is* the misconception being tested: carrying over scalar-algebra intuition ("just move it to the other side") into matrix algebra, without respecting that the side and order of multiplication matter. |
| 11 | (a) $[\vec x]_E=1\begin{bmatrix}2\\1\end{bmatrix}-1\begin{bmatrix}1\\-2\end{bmatrix}=\begin{bmatrix}1\\3\end{bmatrix}$. (b) Solving $\alpha\begin{bmatrix}3\\-1\end{bmatrix}+\beta\begin{bmatrix}-2\\3\end{bmatrix}=\begin{bmatrix}1\\3\end{bmatrix}$ gives $\alpha=\dfrac{9}{7}$, $\beta=\dfrac{10}{7}$, so $[\vec x]_B=\begin{bmatrix}9/7\\10/7\end{bmatrix}$. | Trying to convert $[\vec x]_A$ directly into $[\vec x]_B$ with some imagined shortcut formula, instead of first passing through the true vector $\vec x$ (or building $[B\leftarrow A]$ first). |
| 12 | $[E\leftarrow A]=\begin{bmatrix}2&1\\1&-2\end{bmatrix}$; $[A\leftarrow E]=[E\leftarrow A]^{-1}=\begin{bmatrix}2/5&1/5\\1/5&-2/5\end{bmatrix}$; $[B\leftarrow A]=\begin{bmatrix}8/7&-1/7\\5/7&-5/7\end{bmatrix}$. | Building $[B\leftarrow A]$ by computing $[\vec b_1]_A,[\vec b_2]_A$ (columns for the wrong direction) instead of $[\vec a_1]_B,[\vec a_2]_B$ — reversing the arrow in the $[B\leftarrow A]$ notation. |
| 13 | (a) $\vec b_1=(2,1,0)$, $\vec b_2=(3,-1,0)$, $\vec b_3=(3,-1,1)$. (b) $[A\leftarrow E]=\begin{bmatrix}2/5&1/5&0\\1/5&-2/5&0\\0&0&1\end{bmatrix}$, $[E\leftarrow B]=\begin{bmatrix}2&3&3\\1&-1&-1\\0&0&1\end{bmatrix}$. (c) $[A\leftarrow B]=[A\leftarrow E][E\leftarrow B]=\begin{bmatrix}1&1&1\\0&1&1\\0&0&1\end{bmatrix}$ — which also matches the given $[\vec b_i]_A$ columns directly, as a check. | Multiplying the two change-of-basis matrices in the wrong order ($[E\leftarrow B][A\leftarrow E]$ instead of $[A\leftarrow E][E\leftarrow B]$), or not noticing that the given $[\vec b_i]_A$ values are already, by definition, the columns of $[A\leftarrow B]$ — a useful check on the final answer. |
| 14 | True. By the Invertible $\iff$ Change of Basis Matrix theorem, if $M$ is invertible, its columns (read in standard coordinates) form a basis $C$, and $M=[E\leftarrow C]$. | Believing this only works for "nice" or orthogonal-looking matrices, and that some extra condition beyond invertibility is required — invertibility alone is exactly equivalent to being some change-of-basis matrix. |
