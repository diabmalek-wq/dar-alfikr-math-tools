# Week 2 — Vector Spaces of n-tuples, Matrices & Functions; Matrix Operations

**Session length:** 3 hours
**Source:** Kielstra, *MAT A22 Course Notes*, Week 0 (0A: n-tuples; 0B: $n \times k$ Matrices; 0C: $F$-Valued Functions); Siefken, *MAT223 Workbook*, Appendix 3 (Matrices & Matrix Operations)

---

## Page 1 — Introduction, Key Facts & Definitions

### Why this matters

Last week we studied fields and the abstract axioms of a vector space. This week we meet the **three vector spaces used constantly throughout the course**: $n$-tuples, matrices, and functions. For each one, we need to pin down exactly what its elements are, how to add them, how to scalar-multiply them, and — the question students most often underestimate — **when two of them count as equal.** Matrices, in particular, are more than notation for keeping numbers organized: they are objects you can do arithmetic with (Siefken, Appendix 3).

### Definition: The Vector Space $F^n$

The vector space of $F$ $n$-tuples is
$$F^n = \{(x_1, x_2, \ldots, x_n) : x_i \in F\}.$$
Addition and scalar multiplication are defined coordinatewise:
$$x + y = (x_1, \ldots, x_n) + (y_1, \ldots, y_n) := (x_1+y_1, \ldots, x_n+y_n), \qquad cx := (cx_1, \ldots, cx_n).$$
Let $x, y \in F^n$. Then $x = y$ if and only if $x_i = y_i$ for all $i$.
*(Kielstra, 0A: n-tuples)*

**Key computational fact:** $x + z$ is only defined when $x$ and $z$ live in the *same* $F^n$ — i.e. have the same number of coordinates. Addition between $F^n$ and $F^m$ with $n \neq m$ is simply not defined; there is no "padding" or "truncating." *(Kielstra, 0A: n-tuples)*

### Definition: The Vector Space of $n \times k$ Matrices $M_{n\times k}(F)$

The vector space of $n \times k$ matrices is the set of all rectangular arrays with entries $A_{ij} \in F$, $1 \le i \le n$, $1 \le j \le k$. For $A, B \in M_{n\times k}(F)$:
$$(A+B)_{ij} := A_{ij} + B_{ij}, \qquad (cA)_{ij} := cA_{ij}.$$
$A = B$ if and only if (1) $A$ and $B$ have the same dimensions, **and** (2) $A_{ij} = B_{ij}$ for all $i,j$. *(Kielstra, 0B: n×k Matrices)*

Matrix addition only makes sense for matrices of the same shape; any matrix can be scalar-multiplied by any scalar, regardless of shape. *(Siefken, Appendix 3)*

### Definition: Matrix Notation, Shape, and Special Matrices

A matrix is described by its **shape** (rows $\times$ columns) and its **entries**. An $m \times n$ matrix $A = [a_{ij}]$ has $a_{ij}$ in row $i$, column $j$. The **diagonal** of $A$ consists of entries $a_{ij}$ with $i=j$; the **upper triangle** consists of entries with $j \ge i$; the **lower triangle** consists of entries with $j \le i$. *(Siefken, Appendix 3)*

- A matrix is **triangular** (upper or lower) if all its non-zero entries lie in the corresponding triangle.
- A matrix is **square** if it has the same number of rows as columns.
- A square matrix is **diagonal** if its only non-zero entries lie on the diagonal.
- A square matrix $A=[a_{ij}]$ is **symmetric** if $a_{ij}=a_{ji}$ for all $i,j$ (and **skew-symmetric** if $a_{ij} = -a_{ji}$).
- A **zero matrix** has every entry equal to $0$.
- An **identity matrix** $I_{n\times n}$ (or just $I$) is a square matrix with $1$'s on the diagonal and $0$'s everywhere else.

*(Siefken, Appendix 3)*

### Definition: Transpose of a Matrix

Let $A \in M_{n\times k}(F)$ with entries $A_{ij}$. The **transpose** of $A$, denoted $A^T$, is the $k \times n$ matrix defined by
$$(A^T)_{ij} := A_{ji}.$$
That is, the transpose is obtained by interchanging the rows and columns of $A$. *(Kielstra, 0B: n×k Matrices)*

**Key computational fact:** because transposing changes the shape of a matrix (an $n\times k$ matrix becomes $k \times n$), you must re-check dimension compatibility *after* transposing before adding two matrices — the original shapes being compatible (or not) tells you nothing about the transposed shapes.

### Definition: Matrix–Vector Multiplication

Let $A$ be an $m \times n$ matrix with columns $\vec c_1, \ldots, \vec c_n$ and rows $\vec r_1, \ldots, \vec r_m$ (written as column vectors), and let $\vec x \in F^n$.

- **Column picture:** $A\vec x$ is the linear combination of the columns of $A$ with coefficients $x_1, \ldots, x_n$:
$$A\vec x = x_1\vec c_1 + x_2 \vec c_2 + \cdots + x_n \vec c_n.$$
- **Row picture:** $A\vec x$ is the vector whose $i$th coordinate is the dot product of row $i$ of $A$ with $\vec x$:
$$A\vec x = \begin{bmatrix} \vec r_1 \cdot \vec x \\ \vec r_2 \cdot \vec x \\ \vdots \\ \vec r_m \cdot \vec x \end{bmatrix}.$$

The two pictures always give the same answer. $A\vec x$ is only defined if $\vec x$ has $n$ coordinates (matching the number of *columns* of $A$); the result has $m$ coordinates (the number of *rows* of $A$). *(Siefken, Appendix 3)*

### Definition: Matrix–Matrix Multiplication

Let $C$ be an $m \times n$ matrix and $A$ an $n \times k$ matrix with columns $\vec a_1, \ldots, \vec a_k$. Then $CA$ is the $m \times k$ matrix whose columns are $C\vec a_1, \ldots, C\vec a_k$ — i.e. matrix–matrix multiplication is built out of repeated matrix–vector multiplication. Equivalently, if $C$ has rows $\vec r_1, \ldots, \vec r_m$, the $(i,j)$ entry of $CA$ is $\vec r_i \cdot \vec a_j$ (row $i$ of $C$ dotted with column $j$ of $A$).

For $CA$ to be defined, the number of columns of $C$ must equal the number of rows of $A$; the resulting matrix has (rows of $C$) $\times$ (columns of $A$). *(Siefken, Appendix 3)*

### Fact: Properties of Matrix Algebra

For $A, B, C \in M_{n\times n}(F)$ and $\alpha \in F$:
$$(AB)C = A(BC), \qquad A(B+C) = AB+AC, \qquad (A+B)C = AC+BC,$$
$$IA = AI = A, \qquad 0A = A0 = 0.$$
**Matrix multiplication is, in general, *not* commutative:** $AB \neq BA$ in general, even for square matrices of the same size. We write matrix–vector and matrix–matrix products by adjacency ($A\vec v$, $AB$) — never with $\cdot$ or $\times$, which are reserved for the dot product and cross product. *(Siefken, Appendix 3)*

### Definition: The Vector Space of $F$-Valued Functions $\mathcal F(F)$

$$\mathcal F(F) = \{f : F \to F\}.$$
For $f, g \in \mathcal F(F)$ and $c \in F$:
$$(f+g)(x) := f(x)+g(x), \qquad (cf)(x) := cf(x).$$
Two functions $f,g$ are equal if and only if $f(x)=g(x)$ **for all** $x \in F$ — function equality is checked *pointwise*, not by "looking similar" or agreeing on part of the domain. *(Kielstra, 0C: F-Valued Functions)*

**Definition: Composition.** $(f \circ g)(x) := f(g(x))$. *(Kielstra, 0C: F-Valued Functions)*

### Note: Generic Elements Simplify Proofs

Proving an identity about $F^n$, matrices, or functions by expanding every coordinate/entry/input leads to long, repetitive expressions. Instead, fix an arbitrary index $i$ (for $F^n$), an arbitrary pair $(i,j)$ (for matrices), or an arbitrary input $x$ (for functions), and prove the identity holds for that single generic piece. Since the choice was arbitrary, the identity then holds everywhere at once. This is the standard proof strategy used throughout this unit. *(Kielstra, 0A/0B/0C)*

---

## Pages 2–3 — Solved Examples

**Example 1 (Equality of $n$-tuples).** Let $x = (2,-1,5)$, $y=(2,-1,5)$. Verify $x=y$ using the definition of equality in $F^3$.

By definition, $x=y$ if and only if $x_i=y_i$ for $i=1,2,3$. Here $x_1=2=y_1$, $x_2=-1=y_2$, $x_3=5=y_3$. Since $x_i = y_i$ for all $i$, we conclude $x=y$. $\blacksquare$

**Example 2 (Can these $n$-tuple operations be computed?).** Let $x=(1,2,3)$, $y=(4,5,6)$, $z=(1,2)$. Determine whether $x+y$ and $x+z$ can be computed.

$x$ and $y$ are both in $F^3$, so their sum is defined:
$$x+y = (1+4,\ 2+5,\ 3+6) = (5,7,9).$$
$x$ is in $F^3$ while $z$ is in $F^2$. Since vector addition on $F^n$ is only defined between two elements of the *same* $F^n$, and $3 \neq 2$, the sum $x+z$ is **not defined**. $\blacksquare$

**Example 3 (Distributivity in $F^n$, generic-coordinate proof).** Let $x,y \in F^n$ and $c \in F$. Prove $c(x+y) = cx+cy$.

Rather than expand all $n$ coordinates at once, fix an arbitrary index $i$ with $1 \le i \le n$ and compare the $i$th entries of both sides:
$$
(c(x+y))_i = c(x+y)_i \quad (\text{def. of scalar mult. in } F^n)
$$
$$
= c(x_i+y_i) \quad (\text{def. of vector addition in } F^n)
$$
$$
= cx_i+cy_i \quad (\text{distributivity in the field } F)
$$
$$
= (cx)_i + (cy)_i \quad (\text{def. of scalar mult. in } F^n)
$$
$$
= (cx+cy)_i \quad (\text{def. of vector addition in } F^n).
$$
Since $(c(x+y))_i = (cx+cy)_i$ for every $i=1,\ldots,n$, the two $n$-tuples agree in every coordinate, so $c(x+y)=cx+cy$. $\blacksquare$

**Example 4 (Matrix addition and scalar multiplication).** Let $A = \begin{bmatrix}1&2&3\\4&5&6\end{bmatrix}$, $B=\begin{bmatrix}1&1\\2&2\end{bmatrix}$, $C=\begin{bmatrix}-1&0&-1\\2&1&2\end{bmatrix}$. Compute $2A+B$ and $A+3C$, if possible.

First check shapes. $A$ is $2\times3$, so it can only be added to another $2\times3$ matrix. $B$ is $2\times2$, so $2A+B$ is **not defined** — the shapes don't match, no matter what scalar multiple of $A$ we take. $C$, however, is $2\times3$, so $A+3C$ is defined. We first scalar-multiply $C$ entrywise, then add entrywise:
$$
3C = \begin{bmatrix}-3&0&-3\\6&3&6\end{bmatrix}, \qquad
A+3C = \begin{bmatrix}1&2&3\\4&5&6\end{bmatrix}+\begin{bmatrix}-3&0&-3\\6&3&6\end{bmatrix} = \begin{bmatrix}1-3&2+0&3-3\\4+6&5+3&6+6\end{bmatrix} = \begin{bmatrix}-2&2&0\\10&8&12\end{bmatrix}. \qquad \blacksquare
$$
*(Siefken, Appendix 3)*

**Example 5 (Matrix transpose and a combined expression).** Let $A=\begin{bmatrix}1&2&3\\4&5&6\end{bmatrix}$ ($2\times3$) and $B=\begin{bmatrix}1&0\\-1&2\\3&1\end{bmatrix}$ ($3\times2$). Compute $A^T$, and determine whether $A^T+B$ is defined; if so, compute it.

Transposing $A$ swaps its rows and columns, turning the $2\times3$ matrix into a $3\times2$ matrix:
$$A^T = \begin{bmatrix}1&4\\2&5\\3&6\end{bmatrix}.$$
Now $A^T$ is $3\times2$ and $B$ is $3\times2$ — the shapes match, so $A^T+B$ **is** defined:
$$
A^T+B = \begin{bmatrix}1&4\\2&5\\3&6\end{bmatrix}+\begin{bmatrix}1&0\\-1&2\\3&1\end{bmatrix} = \begin{bmatrix}1+1&4+0\\2-1&5+2\\3+3&6+1\end{bmatrix} = \begin{bmatrix}2&4\\1&7\\6&7\end{bmatrix}. \qquad \blacksquare
$$
*(Kielstra, 0B: n×k Matrices)*

**Example 6 (Matrix–vector multiplication: column and row pictures).** Let $B = \begin{bmatrix}1&2\\-2&3\end{bmatrix}$ and $\vec v = \begin{bmatrix}4\\3\end{bmatrix}$. Compute $B\vec v$ using the column picture, then verify with the row picture.

*Column picture.* The columns of $B$ are $\vec c_1 = \begin{bmatrix}1\\-2\end{bmatrix}$ and $\vec c_2=\begin{bmatrix}2\\3\end{bmatrix}$. We take the linear combination with coefficients from $\vec v$:
$$
B\vec v = 4\begin{bmatrix}1\\-2\end{bmatrix} + 3\begin{bmatrix}2\\3\end{bmatrix} = \begin{bmatrix}4\\-8\end{bmatrix}+\begin{bmatrix}6\\9\end{bmatrix} = \begin{bmatrix}10\\1\end{bmatrix}.
$$
*Row picture.* The rows of $B$ (written as column vectors) are $\vec r_1=\begin{bmatrix}1\\2\end{bmatrix}$ and $\vec r_2 = \begin{bmatrix}-2\\3\end{bmatrix}$. Each output coordinate is a dot product with $\vec v$:
$$
B\vec v = \begin{bmatrix}\vec r_1 \cdot \vec v \\ \vec r_2 \cdot \vec v\end{bmatrix} = \begin{bmatrix}(1)(4)+(2)(3) \\ (-2)(4)+(3)(3)\end{bmatrix} = \begin{bmatrix}10\\1\end{bmatrix}.
$$
Both pictures agree: $B\vec v = \begin{bmatrix}10\\1\end{bmatrix}$. $\blacksquare$ *(Siefken, Appendix 3)*

**Example 7 (Matrix–matrix multiplication and non-commutativity).** Let $X=\begin{bmatrix}1&2&3\\0&-1&0\end{bmatrix}$ and $Y=\begin{bmatrix}2&3\\1&1\\1&0\end{bmatrix}$. Compute $XY$ and $YX$.

First check compatibility: $X$ is $2\times3$ and $Y$ is $3\times2$. For $XY$: columns of $X$ (3) match rows of $Y$ (3), so $XY$ is defined and will be $2\times2$. Using the row-dot-column rule, the $(1,1)$ entry of $XY$ is row 1 of $X$ dotted with column 1 of $Y$:
$$
\begin{bmatrix}1\\2\\3\end{bmatrix}\cdot\begin{bmatrix}2\\1\\1\end{bmatrix} = 2+2+3 = 7.
$$
Computing every entry the same way gives
$$
XY = \begin{bmatrix}1&2&3\\0&-1&0\end{bmatrix}\begin{bmatrix}2&3\\1&1\\1&0\end{bmatrix} = \begin{bmatrix}7&5\\-1&-1\end{bmatrix}.
$$
Now for $YX$: columns of $Y$ (2) match rows of $X$ (2), so $YX$ is defined and will be $3\times3$. Computing entry by entry (e.g. the $(1,1)$ entry is $\begin{bmatrix}2\\3\end{bmatrix}\cdot\begin{bmatrix}1\\0\end{bmatrix}=2$):
$$
YX = \begin{bmatrix}2&3\\1&1\\1&0\end{bmatrix}\begin{bmatrix}1&2&3\\0&-1&0\end{bmatrix} = \begin{bmatrix}2&1&6\\1&1&3\\1&2&3\end{bmatrix}.
$$
Notice $XY$ is $2\times2$ while $YX$ is $3\times3$ — they aren't even the same shape, so certainly $XY \neq YX$. This illustrates that matrix multiplication is **not commutative**, and in fact $AB$ and $BA$ need not even have the same shape. $\blacksquare$ *(Siefken, Appendix 3)*

**Example 8 ($F$-valued functions form a vector space; composition distributes over addition).** Let $f,g,h \in \mathcal F(F)$. Prove $(f+g)\circ h = f\circ h + g \circ h$.

Fix an arbitrary $x \in F$ and compare the values of both sides at $x$:
$$
((f+g)\circ h)(x) = (f+g)(h(x)) \quad (\text{def. of composition})
$$
$$
= f(h(x)) + g(h(x)) \quad (\text{def. of function addition, applied at the input } h(x))
$$
$$
= (f\circ h)(x) + (g \circ h)(x) \quad (\text{def. of composition, applied to each term})
$$
$$
= (f\circ h + g\circ h)(x) \quad (\text{def. of function addition}).
$$
Since this holds for every $x \in F$, and function equality is exactly agreement at every input, we conclude $(f+g)\circ h = f\circ h + g\circ h$. $\blacksquare$ *(Kielstra, 0C: F-Valued Functions)*

---

## Pages 4–5 — Practice Problems (unsolved)

**$n$-tuples**

1. Let $x=(1,-1,2)$ and $y=(0,3,4)$. Compute $x+y$ and $2x$.
2. Let $x=(1,2,3)$ and $z=(1,2)$. Explain why $x+z$ is not defined.
3. Let $x \in F^n$ and $c,d \in F$. Use a generic coordinate to prove $(c+d)x = cx+dx$.

**Matrices — addition, scalar multiplication & equality**

4. Let $A=\begin{bmatrix}1&2\\3&4\end{bmatrix}$ and $B=\begin{bmatrix}0&-1\\2&5\end{bmatrix}$. Compute $A+B$ and $3A$. Then let $C=\begin{bmatrix}1&2&3\\4&5&6\end{bmatrix}$; explain why $A+C$ is not defined.
5. Let $c=4$, $A=\begin{bmatrix}2&-4\\6&0\end{bmatrix}$, $B=\begin{bmatrix}\tfrac12&-1\\\tfrac32&0\end{bmatrix}$. Verify that $A=cB$ using the definition of matrix equality (i.e. check every entry of $cB$ against the corresponding entry of $A$).
6. Let $A,B \in M_{n\times k}(F)$ and $c \in F$. Prove $c(A+B)=cA+cB$ using generic entries $A_{ij}$, $B_{ij}$.

**Matrix transpose**

7. Let $A=\begin{bmatrix}1&0\\2&-1\\0&3\end{bmatrix}$ and $B=\begin{bmatrix}1&2&1\\0&-1&2\end{bmatrix}$. Compute $A^T$, and determine whether $A^T+B$ is defined; if so, compute it.
8. Let $A,B \in M_{n\times k}(F)$. Prove $(A+B)^T = A^T+B^T$ using generic entries.

**Matrix–vector and matrix–matrix multiplication**

9. Let $M=\begin{bmatrix}2&1\\0&3\end{bmatrix}$ and $\vec v = \begin{bmatrix}5\\-2\end{bmatrix}$. Compute $M\vec v$ using the column picture, then verify your answer using the row picture.
10. Let $A$ be a $3\times2$ matrix, $B$ a $2\times4$ matrix, and $C$ a $1\times2$ matrix. Determine which of the products $AB$, $BA$, $CB$, $BC$, $CA$, $AC$ are defined, and give the shape of each defined product.
11. Let $X=\begin{bmatrix}1&2\\0&1\end{bmatrix}$ and $Y=\begin{bmatrix}3&0\\1&2\end{bmatrix}$. Compute $XY$ and $YX$. What does the result tell you about matrix multiplication in general?

**$F$-valued functions as vectors**

12. Let $f(x)=x^2+1$ and $g(x)=2x$. Compute $(f+g)(x)$ and $(3f)(x)$.
13. Let $f(x)=x$ and $g(x)=|x|$. Are $f$ and $g$ equal as elements of $\mathcal F(F)$? Justify your answer using the definition of function equality.
14. Let $f,g \in \mathcal F(F)$ and $c \in F$. Prove $c(f+g)=cf+cg$ using a generic input $x \in F$.

---

## Answer Key & Misconception Notes (for tutor use — do not show student until after attempt)

| # | Answer | Common misconception |
|---|---|---|
| 1 | $x+y=(1,2,6)$; $2x=(2,-2,4)$ | Forgetting to scale **every** coordinate by $2$ (e.g. only doubling the first entry), or adding $x$ and $y$ by mismatching which coordinate pairs with which. |
| 2 | Not defined: $x \in F^3$, $z \in F^2$; vector addition on $F^n$ is only defined between two elements of the *same* $F^n$ | Believing you can "pad" the shorter tuple with a $0$ or truncate the longer one to make the addition work — the definition simply doesn't allow it, there's no fallback rule. |
| 3 | $((c+d)x)_i = (c+d)x_i = cx_i+dx_i = (cx)_i+(dx)_i = (cx+dx)_i$ for all $i$ | Writing out the proof for a specific numeric $n$ (e.g. $n=3$) instead of a generic index $i$, or skipping the explicit citation of distributivity *in the field $F$* as its own step. |
| 4 | $A+B=\begin{bmatrix}1&1\\5&9\end{bmatrix}$; $3A=\begin{bmatrix}3&6\\9&12\end{bmatrix}$; $A+C$ undefined since $A$ is $2\times2$ and $C$ is $2\times3$ | Adding the matching $2\times2$ block of $C$ to $A$ and dropping the extra column, instead of declaring the whole sum undefined. |
| 5 | $(cB)_{11}=2$, $(cB)_{12}=-4$, $(cB)_{21}=6$, $(cB)_{22}=0$, all matching $A$, so $A=cB$ | Judging the matrices "proportional overall" (e.g. by eyeballing that $A$ "looks like" $4$ times $B$) rather than verifying $A_{ij}=(cB)_{ij}$ entry by entry as the definition requires. |
| 6 | $(c(A+B))_{ij}=c(A+B)_{ij}=c(A_{ij}+B_{ij})=cA_{ij}+cB_{ij}=(cA)_{ij}+(cB)_{ij}=(cA+cB)_{ij}$ for all $i,j$ | Thinking a generic pair $(i,j)$ only covers "one row and one column" and that rows and columns need to be argued separately, rather than realizing a single arbitrary entry covers the whole matrix at once. |
| 7 | $A^T=\begin{bmatrix}1&2&0\\0&-1&3\end{bmatrix}$ ($2\times3$); since $B$ is also $2\times3$, $A^T+B$ is defined and equals $\begin{bmatrix}2&4&1\\0&-2&5\end{bmatrix}$ | Checking compatibility using $A$'s original shape ($3\times2$) instead of $A^T$'s new shape ($2\times3$) — forgetting that transposing changes which matrices it can be added to. |
| 8 | $((A+B)^T)_{ij}=(A+B)_{ji}=A_{ji}+B_{ji}=(A^T)_{ij}+(B^T)_{ij}=(A^T+B^T)_{ij}$ for all $i,j$ | Swapping only one index when applying the transpose definition (e.g. writing $(A+B)_{ji}$ as $A_{ij}+B_{ji}$) instead of consistently swapping **both** the row and column index on every term. |
| 9 | $M\vec v = \begin{bmatrix}8\\-6\end{bmatrix}$ by both pictures (column: $5\begin{bmatrix}2\\0\end{bmatrix}-2\begin{bmatrix}1\\3\end{bmatrix}$; row: $(2\cdot5+1\cdot(-2),\ 0\cdot5+3\cdot(-2))$) | In the column picture, adding the raw columns without scaling them by the corresponding entries of $\vec v$ first; in the row picture, pairing row and vector entries in the wrong order when taking the dot product. |
| 10 | Defined: $AB$ ($3\times4$), $CB$ ($1\times4$). Undefined: $BA$, $BC$, $CA$, $AC$ (inner dimensions don't match) | Assuming a product is defined just because a "$2$" appears in both matrices' shapes, rather than checking that the number of *columns of the first* matches the number of *rows of the second*, in that specific order. |
| 11 | $XY=\begin{bmatrix}5&4\\1&2\end{bmatrix}$, $YX=\begin{bmatrix}3&6\\1&4\end{bmatrix}$; $XY \neq YX$, confirming matrix multiplication is not commutative | Multiplying entrywise (Hadamard-style: matching entries in the same position) instead of using the row-dot-column rule — tempting here because $X$ and $Y$ are the same shape. |
| 12 | $(f+g)(x)=x^2+2x+1$; $(3f)(x)=3x^2+3$ | Forgetting to distribute the scalar to **every** term of $f(x)$, e.g. writing $(3f)(x)=3x^2+1$ instead of $3(x^2+1)$. |
| 13 | Not equal: e.g. $f(-1)=-1$ but $g(-1)=1$, so $f(x)\neq g(x)$ for all negative $x$ | Concluding $f=g$ because the two functions agree for all $x \ge 0$ — forgetting that function equality (pointwise) requires agreement at **every** input in $F$, not just most of them. |
| 14 | $(c(f+g))(x)=c(f+g)(x)=c(f(x)+g(x))=cf(x)+cg(x)=(cf)(x)+(cg)(x)=(cf+cg)(x)$ for all $x$ | Treating $c(f+g)$ as an algebra shortcut and skipping the definitional chain (function addition, then scalar multiplication, then distributivity in $F$) instead of justifying each equality as its own step. |
