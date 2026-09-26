# Week 13 — Determinants (including the 2×2 and 3×3 Formulas)

**Session length:** 3 hours
**Source:** Siefken, *MAT223 Workbook*, Module 14 (Determinants) and Appendix 4 (Formulas for 2×2 and 3×3 Determinants)

---

## Page 1 — Introduction, Key Facts & Definitions

### Why this matters

Linear transformations move vectors around, but they also change *sets* — stretching, flattening, or flipping them. This week gives that change a single number: the **determinant**. It tells you, all at once, how much a transformation scales volume, whether it flips orientation, and — critically — whether the transformation (or its matrix) is invertible at all. You already know an invertible matrix is one with zero nullity; the determinant gives you a single number to check instead of doing a full row reduction. The 2×2 and 3×3 formulas at the end of the week are the fast, special-case shortcuts you'll use constantly from here on, including next week when you compute characteristic polynomials for eigenvalues.

### Definition: Unit $n$-cube

*(Source subsection: Volumes)*

The **unit $n$-cube** is the $n$-dimensional cube with sides given by the standard basis vectors and lower-left corner at the origin:
$$C_n=\left\{\vec x\in\mathbb{R}^n : \vec x=\sum_{i=1}^n\alpha_i\vec e_i \text{ for some } \alpha_1,\ldots,\alpha_n\in[0,1]\right\}=[0,1]^n.$$
$C_n$ always has volume $1$ — this is true by definition, and it is the yardstick every other volume in this module is measured against.

### Fact: Volume Change of a Linear Transformation

*(Source subsection: Volumes)*

For $S:\mathbb{R}^n\to\mathbb{R}^n$, define $\operatorname{VolChange}(S)=\dfrac{\operatorname{Vol}(S(C_n))}{\operatorname{Vol}(C_n)}=\operatorname{Vol}(S(C_n))$. Although this is defined using only the unit cube, because $S$ is linear, $\operatorname{VolChange}(S)$ describes how $S$ changes the volume of **any** figure: if $X\subseteq\mathbb{R}^n$ has volume $\alpha$, then $T(X)$ has volume $\alpha\cdot\operatorname{VolChange}(T)$.

### Definition: Orientation Preserving / Reversing

*(Source subsection: The Determinant)*

Let $T:\mathbb{R}^n\to\mathbb{R}^n$ be linear. $T$ is **orientation preserving** if $\{T(\vec e_1),\ldots,T(\vec e_n)\}$ is a positively oriented basis, and **orientation reversing** if that set is a negatively oriented basis. (If $\{T(\vec e_1),\ldots,T(\vec e_n)\}$ isn't a basis at all, $T$ is neither.)

### Definition: Determinant

*(Source subsection: The Determinant)*

The **determinant** of a linear transformation $T:\mathbb{R}^n\to\mathbb{R}^n$, written $\det(T)$ or $|T|$, is the *oriented* volume of the image of the unit $n$-cube: $+\operatorname{Vol}(T(C_n))$ if $T$ is orientation preserving, $-\operatorname{Vol}(T(C_n))$ if orientation reversing. **The determinant of a square matrix is the determinant of its induced transformation.**

### Theorem: Determinants are Multiplicative

*(Source subsection: Determinants of Composition / Determinants of Matrices)*

For linear transformations $S,T:\mathbb{R}^n\to\mathbb{R}^n$: $\det(S\circ T)=\det(S)\det(T)$. Since a matrix's determinant is the determinant of its induced transformation, this immediately gives, for $n\times n$ matrices $A,B$:
$$\det(AB)=\det(A)\det(B).$$

### Theorem: Volume Theorem I

*(Source subsection: Determinants of Matrices)*

For a square matrix $M$, $\det(M)$ is the oriented volume of the **parallelepiped given by the columns of $M$** — because the columns of $M$ are exactly $\{T_M(\vec e_1),\ldots,T_M(\vec e_n)\}$, the images of the standard basis vectors.

### Fact: Determinants of Elementary Matrices

*(Source subsection: Determinants of Matrices)*

- **Multiply a row by a nonzero constant $\alpha$:** $\det(E_m)=\alpha$.
- **Swap two rows:** $\det(E_s)=-1$ (a swap reverses orientation).
- **Add a multiple of one row to another:** $\det(E_a)=1$ (this only *shears* the cube, which never changes its volume).

Since any matrix can be decomposed into a product of elementary matrices via row reduction, this lets you compute *any* determinant by tracking these three easy numbers through a row reduction.

### Theorem: Determinants and Invertibility

*(Source subsection: Determinants and Invertibility)*

Let $A$ be $n\times n$. **$A$ is invertible if and only if $\det(A)\neq 0$.** If $A$ is not invertible, $\operatorname{rank}(A)<n$, so the parallelepiped given by its columns is "flattened" and has zero volume. If $A$ is invertible, $A=E_1\cdots E_k$ for elementary matrices with nonzero determinants, so $\det(A)=\det(E_1)\cdots\det(E_k)\neq 0$. Also, since $AA^{-1}=I$ gives $\det(A)\det(A^{-1})=\det(I)=1$:
$$\det(A^{-1})=\frac{1}{\det(A)}.$$

### Theorem: Volume Theorem II — Determinant and Transpose

*(Source subsection: Determinants and Transposes)*

For a square matrix $A$: $\det(A)=\det(A^T)$. (Equivalently, $\det(A)$ is also the oriented volume of the parallelepiped given by the **rows** of $A$.) This joins $\operatorname{rank}(A)=\operatorname{rank}(A^T)$ as another fact that is true of a matrix and its transpose together, even though the two matrices can look completely different.

### Fact: The $2\times2$ Determinant Formula

*(Source subsection: Computing $2\times2$ Determinants, Appendix 4)*

For $M=\begin{bmatrix}a&b\\c&d\end{bmatrix}$:
$$\det(M)=ad-bc.$$
Because $2\times2$ and $3\times3$ matrices come up so often, it's worth memorizing this shortcut rather than row-reducing every time — though row reduction (via elementary matrices) always agrees with it.

### Fact: The $3\times3$ Determinant Formula — Rule of Sarrus

*(Source subsection: Computing $3\times3$ Determinants, Appendix 4)*

For $M=\begin{bmatrix}a&b&c\\d&e&f\\g&h&i\end{bmatrix}$:
$$\det(M)=aei+bfg+cdh-gec-hfa-idb.$$
**Mnemonic (diagonal trick):** augment $M$ with copies of its first two columns, then sum the three "downward" diagonal products ($aei+bfg+cdh$) and subtract the three "upward" anti-diagonal products ($gec+hfa+idb$). **This trick only works for $3\times3$ matrices** — do not try to extend it to $4\times4$ or larger; those need row reduction or a genuinely different (and far more complex) formula.

### Fact: Determinant Sign and Orientation of a Basis

*(Source subsection: Determinant Formulas and Orientation, Appendix 4)*

For an ordered basis $B=\{\vec b_1,\vec b_2\}$ of $\mathbb{R}^2$, let $M=[\vec b_1\mid\vec b_2]$. Since $B$ is linearly independent, $\det(M)\neq0$, and:
$$\det(M)>0 \iff B \text{ is right-handed}, \qquad \det(M)<0\iff B\text{ is left-handed}.$$

---

## Pages 2–3 — Solved Examples

**Example 1 (Volume of the image of the unit square).** Let $T:\mathbb{R}^2\to\mathbb{R}^2$ be defined by $T\begin{bmatrix}x\\y\end{bmatrix}=\begin{bmatrix}3x-y\\x-\frac14y\end{bmatrix}$. Find the volume of $T(C_2)$.

The matrix of $T$ is $M_T=\begin{bmatrix}3&-1\\1&-1/4\end{bmatrix}$. By Volume Theorem I, $\operatorname{Vol}(T(C_2))=|\det(M_T)|$:
$$\det(M_T)=(3)\left(-\tfrac14\right)-(-1)(1)=-\tfrac34+1=\tfrac14.$$
So $\operatorname{Vol}(T(C_2))=\dfrac14$. (Since $\det(M_T)>0$ here, $T$ is also orientation preserving, so the *oriented* volume — i.e. $\det(T)$ itself — is also $\frac14$.) $\blacksquare$

**Example 2 (Orientation and determinant together).** Let $T\begin{bmatrix}x\\y\end{bmatrix}=\begin{bmatrix}x+2y\\-x-y\end{bmatrix}$. Determine whether $T$ is orientation preserving or reversing, and find $\det(T)$.

$T(\vec e_1)=\begin{bmatrix}1\\-1\end{bmatrix}$, $T(\vec e_2)=\begin{bmatrix}2\\-1\end{bmatrix}$. Check the orientation using the $2\times2$ formula on $[T(\vec e_1)\mid T(\vec e_2)]$:
$$\det\begin{bmatrix}1&2\\-1&-1\end{bmatrix}=(1)(-1)-(2)(-1)=-1+2=1>0,$$
so $\{T(\vec e_1),T(\vec e_2)\}$ is positively oriented and $T$ is **orientation preserving**. Therefore $\det(T)=+1$ (the oriented volume equals the ordinary determinant value, with no sign flip needed). $\blacksquare$

**Example 3 (Determinants of easy geometric transformations).** Find $\det(S)$ for $S:\mathbb{R}^2\to\mathbb{R}^2$, which shortens every vector by a factor of $\frac23$; and $\det(F)$ for $F:\mathbb{R}^2\to\mathbb{R}^2$, reflection across the line $y=-x$.

$S=\frac23I$, so its matrix is $\begin{bmatrix}2/3&0\\0&2/3\end{bmatrix}$, giving $\det(S)=\left(\frac23\right)^2=\frac49$. A reflection always reverses orientation while preserving all lengths and areas, so $|\det(F)|=1$ with a negative sign: $\det(F)=-1$. (Every reflection has determinant exactly $-1$; every rotation has determinant exactly $+1$ — worth remembering as a shortcut.) $\blacksquare$

**Example 4 (A $3\times3$ determinant by cofactor-style expansion).** Let $T\begin{bmatrix}x\\y\\z\end{bmatrix}=\begin{bmatrix}x-y+z\\x-\frac13y+z\\z\end{bmatrix}$. Find $\det(T)$.

The matrix is $M=\begin{bmatrix}1&-1&1\\1&-1/3&1\\0&0&1\end{bmatrix}$. Since row 3 has only one nonzero entry, expand along it: $\det(M)=1\cdot\det\begin{bmatrix}1&-1\\1&-1/3\end{bmatrix}=1\cdot\left((1)\left(-\tfrac13\right)-(-1)(1)\right)=1\cdot\left(-\tfrac13+1\right)=\tfrac23$. $\blacksquare$

**Example 5 (Determinant via elementary matrices, checked against the $2\times2$ formula).** Let $A=\begin{bmatrix}2&3\\1&5\end{bmatrix}$. Find $\det(A)$ using elementary matrices, and confirm with the $2\times2$ formula.

Row reduce: swap $R_1,R_2$ ($\det=-1$) $\to\begin{bmatrix}1&5\\2&3\end{bmatrix}$; then $R_2-2R_1$ ($\det=1$) $\to\begin{bmatrix}1&5\\0&-7\end{bmatrix}$; then $R_2\div(-7)$ ($\det=-\frac17$) $\to\begin{bmatrix}1&5\\0&1\end{bmatrix}$; then $R_1-5R_2$ ($\det=1$) $\to I$. So $(-1)\left(1\right)\left(-\tfrac17\right)(1)\det(A)=\det(I)=1$, giving $\tfrac17\det(A)=1$, so $\det(A)=7$. Checking with the formula: $\det(A)=(2)(5)-(3)(1)=10-3=7$. ✓ $\blacksquare$

**Example 6 (A $3\times3$ determinant via cofactor expansion, then checking invertibility).** Let $A=\begin{bmatrix}1&2&0\\0&2&1\\1&2&3\end{bmatrix}$. Find $\det(A)$, $\det(A^{-1})$, and $\det(A^T)$.

Expanding along the first row: $\det(A)=1\cdot\det\begin{bmatrix}2&1\\2&3\end{bmatrix}-2\cdot\det\begin{bmatrix}0&1\\1&3\end{bmatrix}+0=1(6-2)-2(0-1)=4+2=6$. Since $\det(A)=6\neq0$, $A$ **is invertible**, and $\det(A^{-1})=\dfrac{1}{\det(A)}=\dfrac16$. By Volume Theorem II, $\det(A^T)=\det(A)=6$ — no extra computation needed. $\blacksquare$

**Example 7 (Rule of Sarrus).** Use the Rule of Sarrus to compute $\det(N)$ for $N=\begin{bmatrix}2&0&1\\3&1&-1\\0&2&4\end{bmatrix}$.

With $a=2,b=0,c=1,d=3,e=1,f=-1,g=0,h=2,i=4$:
$$\det(N)=\underbrace{(2)(1)(4)+(0)(-1)(0)+(1)(3)(2)}_{8+0+6}-\underbrace{\big[(0)(1)(1)+(2)(-1)(2)+(4)(3)(0)\big]}_{0+(-4)+0}=14-(-4)=18.$$
(Double-check with cofactor expansion along row 1: $2(4-(-2))-0+1(6-0)=2(6)+6=18$. ✓) $\blacksquare$

**Example 8 (Determinant as an orientation test).** Determine whether the ordered basis $\left\{\begin{bmatrix}2\\-1\end{bmatrix},\begin{bmatrix}3\\4\end{bmatrix}\right\}$ is left- or right-handed.

Let $M=\begin{bmatrix}2&3\\-1&4\end{bmatrix}$. $\det(M)=(2)(4)-(3)(-1)=8+3=11>0$, so the basis is **right-handed**. $\blacksquare$

---

## Pages 4–5 — Practice Problems (unsolved)

**Volume, Determinant & Orientation of a Linear Transformation**

1. Let $T\begin{bmatrix}x\\y\end{bmatrix}=\begin{bmatrix}2x+y\\x-\frac12y\end{bmatrix}$. Find the volume of $T(C_2)$.
2. Let $T\begin{bmatrix}x\\y\end{bmatrix}=\begin{bmatrix}x+2y\\-x-y\end{bmatrix}$ (from Example 2). Draw $E=\{\vec e_1,\vec e_2\}$ and $T(E)$, and use your picture to explain, geometrically, why $T$ came out orientation preserving.
3. For each transformation, find its determinant. (a) $S:\mathbb{R}^2\to\mathbb{R}^2$, where $S$ shortens every vector by a factor of $\frac23$ (Example 3's $S$). (b) $R:\mathbb{R}^2\to\mathbb{R}^2$, rotation counter-clockwise by $90°$. (c) $F:\mathbb{R}^2\to\mathbb{R}^2$, reflection across the line $y=x$.

**The $2\times2$ and $3\times3$ Determinant Formulas**

4. Let $A=\begin{bmatrix}4&2\\3&5\end{bmatrix}$. (a) Find $\det(A)$ using elementary matrices, tracking each row operation's determinant multiplier. (b) Confirm your answer using the $2\times2$ formula.
5. Let $A=\begin{bmatrix}1&2&0\\0&2&1\\1&2&3\end{bmatrix}$ (from Example 6). Recompute $\det(A)$ using the Rule of Sarrus instead of cofactor expansion, and confirm you get the same value.
6. Use the Rule of Sarrus to compute $\det\begin{bmatrix}1&4&0\\-2&3&1\\0&2&1\end{bmatrix}$.

**Determinants, Invertibility & Orientation**

7. Determine whether $P=\begin{bmatrix}1&2&3\\2&4&6\\1&1&2\end{bmatrix}$ is invertible, using its determinant to justify your answer.
8. Determine whether the ordered basis $\left\{\begin{bmatrix}-1\\2\end{bmatrix},\begin{bmatrix}3\\1\end{bmatrix}\right\}$ is left- or right-handed.

**Determinants and Elementary Matrices — Conceptual**

9. Let $A$ be an $n\times n$ matrix that can be decomposed into a product of elementary matrices. (a) What is $\operatorname{rank}(A)$? Justify your answer. (b) What is $\operatorname{nullity}(A^{-1})$? Justify your answer.
10. Anna and Ella are studying $S:\mathbb{R}^3\to\mathbb{R}^3$ defined by $S\begin{bmatrix}x\\y\\z\end{bmatrix}=\begin{bmatrix}4x\\2z\\0\end{bmatrix}$. Anna says: "Since the image of $C_3$ under $S$ is the parallelogram generated by $\begin{bmatrix}4\\0\\0\end{bmatrix}$ and $\begin{bmatrix}0\\2\\0\end{bmatrix}$, which has area $8$, we get $\det(S)=8$." Ella says: "$\det(S)$ is undefined, because $S$ is not invertible." Evaluate each argument as correct, mostly correct, or incorrect, and give the correct value of $\det(S)$ (or explain why it doesn't exist).
11. True or false, with justification: "If $\det(A)=0$ for a $4\times4$ matrix $A$, then $A$ must have an entire row of zeros."

---

## Answer Key & Misconception Notes (for tutor use — do not show student until after attempt)

| # | Answer | Common misconception |
|---|---|---|
| 1 | Matrix $\begin{bmatrix}2&1\\1&-1/2\end{bmatrix}$, $\det=2(-1/2)-1(1)=-1-1=-2$, so $\operatorname{Vol}(T(C_2))=\lvert -2\rvert=2$. | Forgetting the volume asked for is the *unsigned* value $\lvert\det\rvert$, and reporting $-2$ as "the volume." |
| 2 | $T(E)$ is $T(\vec e_1)=(1,-1)$ and $T(\vec e_2)=(2,-1)$; sketching shows rotating from $\vec e_1$ to $\vec e_2$ (counter-clockwise, the short way) matches the sense of rotating from $T(\vec e_1)$ to $T(\vec e_2)$ — same rotational sense as the standard basis, hence orientation preserving. | Trying to answer this purely algebraically (recomputing the determinant) instead of actually drawing the two pairs of vectors and comparing their rotational sense, which is what "orientation" geometrically means. |
| 3 | (a) $\det(S)=(2/3)^2=4/9$. (b) $\det(R)=1$ (every rotation has determinant $+1$). (c) $\det(F)=-1$ (every reflection has determinant $-1$). | Forgetting that a *reflection* always has determinant exactly $-1$ regardless of the line, and instead trying to recompute it from scratch each time; or mixing up which of rotation/reflection gets the $+1$ and which gets $-1$. |
| 4 | $\det(A)=(4)(5)-(2)(3)=20-6=14$; the elementary-matrix product of row-operation determinants should also multiply out to $14$. | Losing track of the sign or reciprocal when a row is scaled (e.g. writing the scale factor's determinant as its reciprocal, or forgetting a row swap contributes $-1$). |
| 5 | $\det(A)=6$, matching Example 6. | Misplacing which diagonal is "added" and which is "subtracted" in the Rule of Sarrus — always augment with the *first two* columns and read the three down-right diagonals as positive, the three down-left as negative. |
| 6 | $\det=1(3)(1)+4(1)(0)+0(-2)(2)-\big[0(3)(0)+2(1)(1)+1(-2)(4)\big]=3-\big[0+2-8\big]=3-(-6)=9$. | Forgetting to re-copy the first two columns before reading off the diagonals, which scrambles which entries multiply together. |
| 7 | Not invertible: expanding along row 1, $\det(P)=1(4\cdot2-6\cdot1)-2(2\cdot2-6\cdot1)+3(2\cdot1-4\cdot1)=1(2)-2(-2)+3(-2)=2+4-6=0$, and $\det(P)=0\Rightarrow P$ is not invertible. | Not noticing row 2 is exactly $2\times$ row 1 (which would let you conclude $\det(P)=0$ instantly, with no arithmetic at all) and grinding through the full expansion unnecessarily — not wrong, just slower than reading the dependency directly. |
| 8 | $\det=(-1)(1)-(3)(2)=-1-6=-7<0$, so the basis is **left-handed**. | Computing the columns of the matrix in the wrong order (putting the second vector's entries in column 1), which can flip the sign of the determinant and give the wrong handedness. |
| 9 | (a) $\operatorname{rank}(A)=n$: a product of elementary matrices is always invertible (each elementary matrix is invertible, and a product of invertible matrices is invertible), so $A$ is invertible, hence full rank. (b) $\operatorname{nullity}(A^{-1})=0$: $A^{-1}$ is itself invertible (the inverse of an invertible matrix), so it has trivial null space. | Trying to compute $A^{-1}$ explicitly, or reasoning about specific numbers, instead of using the general fact that a product of invertible matrices — and the inverse of an invertible matrix — is always invertible. |
| 10 | $S$'s matrix is $\begin{bmatrix}4&0&0\\0&0&2\\0&0&0\end{bmatrix}$, and expanding along row 3 (all zero) gives $\det(S)=0$. Ella is right that $S$ is not invertible, but wrong that $\det(S)$ is undefined — the determinant is defined for **every** square matrix, invertible or not; when the matrix isn't invertible, the determinant is simply $0$. Anna's value ($8$) and reasoning are incorrect: the $2$-dimensional area of a flattened image sitting inside $\mathbb{R}^3$ is not the same thing as the $3$-dimensional oriented volume that the determinant measures — a flattened image in $3$-space always has $3$-dimensional volume $0$, however large its own $2$-dimensional area is. | Believing "not invertible" and "determinant doesn't exist" are the same statement — they are not: every square matrix has a determinant, and $\det=0$ is precisely the *test* for non-invertibility, not a sign that the number can't be computed. |
| 11 | False. A matrix can have $\det=0$ purely because its rows (or columns) are *linearly dependent*, with no row equal to all zeros — e.g. a $4\times4$ matrix whose row 2 equals row 1 exactly (but neither is zero) still has $\det=0$. | Confusing "the parallelepiped is flattened (zero volume)" with "one of the generating vectors must itself be the zero vector" — dependence, not a zero row, is the general condition; a zero row is only one special way to get dependence. |
