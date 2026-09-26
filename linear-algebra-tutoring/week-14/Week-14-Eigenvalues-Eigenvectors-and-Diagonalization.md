# Week 14 — Eigenvalues, Eigenvectors & Diagonalization

**Session length:** 3 hours
**Source:** Siefken, *MAT223 Workbook*, Module 15 (Eigenvalues and Eigenvectors) and Module 16 (Diagonalization)

---

## Page 1 — Introduction, Key Facts & Definitions

### Why this matters

Every linear transformation you've studied — stretch, shear, rotation, projection — can be described by how it treats *every* vector. But some vectors are special: a transformation might stretch a particular vector without changing its direction at all. Finding those special "eigen" directions turns out to be one of the most useful things you can do with a matrix, because in the right basis — a basis made of these special vectors — the matrix becomes *diagonal*, and multiplying by a diagonal matrix is as easy as matrix arithmetic ever gets. Last week's determinant is the tool that makes finding these vectors possible.

### Definition: Eigenvector and Eigenvalue

*(Source subsection: Eigenvectors)*

Let $X$ be a linear transformation or a matrix. An **eigenvector** for $X$ is a non-zero vector that doesn't change direction when $X$ is applied — that is, $\vec v\neq\vec 0$ is an eigenvector for $X$ if
$$X\vec v=\lambda\vec v$$
for some scalar $\lambda$. We call $\lambda$ the **eigenvalue** of $X$ corresponding to the eigenvector $\vec v$. ("Eigen" is German for *characteristic* or *intrinsic*.)

### Fact: Finding Eigenvectors via a Null Space

*(Source subsection: Finding Eigenvectors)*

For a square matrix $M$, $\vec v\neq\vec 0$ is an eigenvector with eigenvalue $\lambda$ exactly when $(M-\lambda I)\vec v=\vec 0$ — that is, when $\vec v\in\operatorname{null}(M-\lambda I)$. Writing $E_\lambda=M-\lambda I$, this reduces "find the eigenvectors" to "find the null space of $E_\lambda$" for the right choice of $\lambda$.

### Definition: Characteristic Polynomial

*(Source subsection: Characteristic Polynomial)*

For a matrix $A$, the **characteristic polynomial** of $A$ is
$$\operatorname{char}(A)=\det(A-\lambda I).$$
Since $E_\lambda=A-\lambda I$ is $n\times n$, it has a non-trivial null space exactly when it is *not invertible*, i.e. when $\det(E_\lambda)=0$ — so **the roots of $\operatorname{char}(A)$ are precisely the eigenvalues of $A$.**

### Fact: Properties of the Characteristic Polynomial

*(Source subsection: Characteristic Polynomial)*

For an $n\times n$ matrix $A$: $\operatorname{char}(A)$ is a polynomial of degree $n$; the coefficient of its $\lambda^n$ term is $\pm1$ ($+1$ if $n$ is even, $-1$ if $n$ is odd); and $\operatorname{char}(A)$ evaluated at $\lambda=0$ equals $\det(A)$ — so **$0$ is an eigenvalue of $A$ if and only if $\det(A)=0$**, tying this week directly to last week's invertibility test.

### Theorem: Every Matrix Has an Eigenvalue (Allowing Complex Numbers)

*(Source subsection: Transformations without Eigenvectors)*

A real matrix does not always have a *real* eigenvalue — e.g. rotation by $90°$ has characteristic polynomial $\lambda^2+1$, whose roots $\pm i$ are not real, so the rotation has no real eigenvectors. However, **if complex eigenvalues are permitted, every square matrix has at least one eigenvalue** (a direct consequence of the Fundamental Theorem of Algebra).

### Definition: Eigenspace, Geometric Multiplicity, Algebraic Multiplicity

*(Source subsection: Geometric and Algebraic Multiplicities)*

Let $A$ be $n\times n$ with eigenvalues $\lambda_1,\ldots,\lambda_m$. The **eigenspace** of $A$ for $\lambda_i$ is $\operatorname{null}(A-\lambda_iI)$ — the space of all eigenvectors for $\lambda_i$, together with $\vec0$. The **geometric multiplicity** of $\lambda_i$ is the dimension of that eigenspace. The **algebraic multiplicity** of $\lambda_i$ is the number of times $\lambda_i$ occurs as a root of $\operatorname{char}(A)$ (i.e. the power of $(\lambda_i-\lambda)$ in the factored polynomial).

### Theorem: Geometric Multiplicity Never Exceeds Algebraic Multiplicity

*(Source subsection: Geometric and Algebraic Multiplicities)*

For any eigenvalue $\lambda$ of a matrix $A$: $\operatorname{geomult}(\lambda)\leq\operatorname{algmult}(\lambda)$. Combined with the Fundamental Theorem of Algebra (the algebraic multiplicities of an $n\times n$ matrix's eigenvalues always sum to $n$, once complex roots are allowed), this is the key inequality behind whether a matrix can be diagonalized.

### Definition: Similar Matrices and Diagonalizable

*(Source subsection: Diagonalization)*

Two matrices are **similar** if they represent the same linear transformation in (possibly) different bases: $A$ and $B$ are similar exactly when $A=PBP^{-1}$ for some invertible change-of-basis matrix $P$. A matrix is **diagonalizable** if it is similar to a diagonal matrix.

### Theorem: Diagonal Representation $\iff$ Basis of Eigenvectors

*(Source subsection: Diagonalization)*

A linear transformation $T:\mathbb{R}^n\to\mathbb{R}^n$ can be represented by a diagonal matrix $[T]_B=\operatorname{diag}(\alpha_1,\ldots,\alpha_n)$ **if and only if** $B=\{\vec b_1,\ldots,\vec b_n\}$ is a basis of eigenvectors for $T$, with $T(\vec b_i)=\alpha_i\vec b_i$ for each $i$. In other words: writing $T$ in the "eigenbasis" turns it into the simplest possible matrix — one that just scales each coordinate.

### Fact: Diagonalizing a Matrix — $A=PDP^{-1}$

*(Source subsection: Diagonalization)*

If $A$ is $n\times n$ with a basis of eigenvectors $\vec v_1,\ldots,\vec v_n$ and corresponding eigenvalues $\lambda_1,\ldots,\lambda_n$, let $P=[\vec v_1\mid\cdots\mid\vec v_n]$ (the change-of-basis matrix from the eigenbasis to the standard basis) and $D=\operatorname{diag}(\lambda_1,\ldots,\lambda_n)$ (the eigenvalues, in the *same order* as their eigenvectors appear in $P$). Then
$$A=PDP^{-1}.$$

### Theorem: A Matrix is Diagonalizable $\iff$ Geometric Multiplicities Sum to $n$

*(Source subsection: Geometric and Algebraic Multiplicities)*

An $n\times n$ matrix $A$ is diagonalizable if and only if the sum of the geometric multiplicities of all its eigenvalues equals $n$. Equivalently (allowing complex eigenvalues), $A$ is diagonalizable if and only if **every eigenvalue's geometric multiplicity equals its algebraic multiplicity**. This is the practical test: find every eigenvalue, find each eigenspace's dimension, and check whether those dimensions add up to $n$.

---

## Pages 2–3 — Solved Examples

**Example 1 (Recognizing eigenvectors geometrically).** Let $P:\mathbb{R}^2\to\mathbb{R}^2$ be projection onto the line $\ell$ given by $y=x$. Find the eigenvectors and eigenvalues of $P$ without computing a characteristic polynomial.

Since $P(\ell)=\ell$, every vector already on $\ell$ is left unchanged: for $\vec v\in\ell$, $P(\vec v)=1\cdot\vec v$. So every non-zero multiple of $\begin{bmatrix}1\\1\end{bmatrix}$ is an eigenvector with eigenvalue $1$. A vector perpendicular to $\ell$, like $\begin{bmatrix}1\\-1\end{bmatrix}$, gets projected entirely to $\vec 0$: $P\begin{bmatrix}1\\-1\end{bmatrix}=\begin{bmatrix}0\\0\end{bmatrix}=0\begin{bmatrix}1\\-1\end{bmatrix}$. So every non-zero multiple of $\begin{bmatrix}1\\-1\end{bmatrix}$ is an eigenvector with eigenvalue $0$. $\blacksquare$

**Example 2 (Finding eigenvalues/eigenvectors via the characteristic polynomial).** Find the eigenvectors and eigenvalues of $A=\begin{bmatrix}1&2\\3&2\end{bmatrix}$.

$$\operatorname{char}(A)=\det\begin{bmatrix}1-\lambda&2\\3&2-\lambda\end{bmatrix}=(1-\lambda)(2-\lambda)-6=\lambda^2-3\lambda-4=(4-\lambda)(-1-\lambda).$$
Roots: $\lambda_1=-1$, $\lambda_2=4$. For $\lambda_1=-1$: $\operatorname{null}(A+I)=\operatorname{null}\begin{bmatrix}2&2\\3&3\end{bmatrix}=\operatorname{span}\left\{\begin{bmatrix}1\\-1\end{bmatrix}\right\}$. For $\lambda_2=4$: $\operatorname{null}(A-4I)=\operatorname{null}\begin{bmatrix}-3&2\\3&-2\end{bmatrix}=\operatorname{span}\left\{\begin{bmatrix}2\\3\end{bmatrix}\right\}$. So the eigenvectors are the non-zero multiples of $\begin{bmatrix}1\\-1\end{bmatrix}$ (eigenvalue $-1$) and of $\begin{bmatrix}2\\3\end{bmatrix}$ (eigenvalue $4$). $\blacksquare$

**Example 3 (A transformation with no real eigenvalues).** Let $R:\mathbb{R}^2\to\mathbb{R}^2$ be rotation counter-clockwise by $90°$, with matrix $M_R=\begin{bmatrix}0&-1\\1&0\end{bmatrix}$. Find the real eigenvalues of $R$, if any.

$$\operatorname{char}(M_R)=\det\begin{bmatrix}-\lambda&-1\\1&-\lambda\end{bmatrix}=\lambda^2+1.$$
$\lambda^2+1=0$ has no real solutions (only $\lambda=\pm i$). So $R$ has **no real eigenvalues** — which makes geometric sense: a $90°$ rotation changes the direction of *every* non-zero vector, so no real vector can be an eigenvector. $\blacksquare$

**Example 4 (A matrix that is NOT diagonalizable — repeated eigenvalue, deficient eigenspace).** Is $J=\begin{bmatrix}5&1\\0&5\end{bmatrix}$ diagonalizable?

$\operatorname{char}(J)=(5-\lambda)^2$, so $\lambda=5$ is the only eigenvalue, with algebraic multiplicity $2$. Its eigenspace is $\operatorname{null}(J-5I)=\operatorname{null}\begin{bmatrix}0&1\\0&0\end{bmatrix}=\operatorname{span}\left\{\begin{bmatrix}1\\0\end{bmatrix}\right\}$, which has dimension $1$ — the geometric multiplicity of $5$ is $1$, not $2$. Since $1\neq2$ (equivalently, the geometric multiplicities sum to $1\neq2=n$), there is no basis of $\mathbb{R}^2$ consisting of eigenvectors of $J$. **$J$ is not diagonalizable.** $\blacksquare$

**Example 5 (A matrix that IS diagonalizable — two distinct eigenvalues).** Is $K=\begin{bmatrix}5&1\\0&2\end{bmatrix}$ diagonalizable? If so, diagonalize it.

$\operatorname{char}(K)=(5-\lambda)(2-\lambda)$, roots $\lambda=5,2$, each with algebraic multiplicity $1$. Eigenspace for $5$: $\operatorname{null}(K-5I)=\operatorname{null}\begin{bmatrix}0&1\\0&-3\end{bmatrix}=\operatorname{span}\left\{\begin{bmatrix}1\\0\end{bmatrix}\right\}$. Eigenspace for $2$: $\operatorname{null}(K-2I)=\operatorname{null}\begin{bmatrix}3&1\\0&0\end{bmatrix}=\operatorname{span}\left\{\begin{bmatrix}-1\\3\end{bmatrix}\right\}$. Both geometric multiplicities are $1$, matching their algebraic multiplicities, and $1+1=2=n$. **$K$ is diagonalizable**, with $P=\begin{bmatrix}1&-1\\0&3\end{bmatrix}$, $D=\begin{bmatrix}5&0\\0&2\end{bmatrix}$, so $K=PDP^{-1}$. $\blacksquare$

**Example 6 (Non-diagonalizability in $3\times3$).** Is $M=\begin{bmatrix}2&1&0\\0&2&0\\0&0&3\end{bmatrix}$ diagonalizable?

$M$ is upper triangular, so its eigenvalues are its diagonal entries: $\operatorname{char}(M)=(2-\lambda)^2(3-\lambda)$, giving $\lambda=2$ (algebraic multiplicity $2$) and $\lambda=3$ (algebraic multiplicity $1$). Eigenspace for $\lambda=2$: $\operatorname{null}(M-2I)=\operatorname{null}\begin{bmatrix}0&1&0\\0&0&0\\0&0&1\end{bmatrix}$ — this forces $y=0$ and $z=0$ with $x$ free, so the eigenspace is $\operatorname{span}\left\{\begin{bmatrix}1\\0\\0\end{bmatrix}\right\}$, dimension $1$. Since $\operatorname{geomult}(2)=1<2=\operatorname{algmult}(2)$, the geometric multiplicities can sum to at most $1+1=2\neq3=n$. **$M$ is not diagonalizable**, even though it's $3\times3$ and one eigenvalue is "clean" (multiplicity $1$) — one deficient eigenvalue is enough to block diagonalization entirely. $\blacksquare$

**Example 7 (Diagonalizing a $3\times3$ matrix from given eigenvectors).** Let $A=\begin{bmatrix}1&2&5\\-11&14&5\\-3&2&9\end{bmatrix}$, and suppose you're told $\vec v_1=\begin{bmatrix}5\\5\\1\end{bmatrix}$, $\vec v_2=\begin{bmatrix}1\\1\\1\end{bmatrix}$, $\vec v_3=\begin{bmatrix}1\\3\\1\end{bmatrix}$ are eigenvectors of $A$. Diagonalize $A$.

First find each eigenvalue by direct multiplication: $A\vec v_1=\begin{bmatrix}20\\20\\4\end{bmatrix}=4\vec v_1$, $A\vec v_2=\begin{bmatrix}8\\8\\8\end{bmatrix}=8\vec v_2$, $A\vec v_3=\begin{bmatrix}12\\36\\12\end{bmatrix}=12\vec v_3$. So the eigenvalues are $4,8,12$ respectively. Setting $P=[\vec v_1\mid\vec v_2\mid\vec v_3]=\begin{bmatrix}5&1&1\\5&1&3\\1&1&1\end{bmatrix}$ and $D=\begin{bmatrix}4&0&0\\0&8&0\\0&0&12\end{bmatrix}$ (eigenvalues in the same column order as their eigenvectors in $P$), we get
$$A=PDP^{-1}.$$
(You never needed to compute a characteristic polynomial here — once you're *given* a full set of eigenvectors, diagonalizing is just bookkeeping: verify each $A\vec v_i=\lambda_i\vec v_i$, then assemble $P$ and $D$.) $\blacksquare$

---

## Pages 4–5 — Practice Problems (unsolved)

**Finding Eigenvectors and Eigenvalues Geometrically**

1. For each linear transformation, find its eigenvectors and eigenvalues, or explain why none exist (without computing a characteristic polynomial). (a) $S:\mathbb{R}^2\to\mathbb{R}^2$, which stretches every vector by a factor of $3$. (b) $R:\mathbb{R}^2\to\mathbb{R}^2$, rotation clockwise by $\frac{\pi}{4}$. (c) $P:\mathbb{R}^2\to\mathbb{R}^2$, projection onto the line $\ell$ given by $y=-x$. (d) $F:\mathbb{R}^2\to\mathbb{R}^2$, reflection over the line $\ell$ given by $y=-x$.

**The Characteristic Polynomial**

2. Let $A=\begin{bmatrix}1&2\\3&0\end{bmatrix}$. (a) Find $\operatorname{char}(A)$. (b) Find the eigenvalues of $A$.
3. Let $B=\begin{bmatrix}1&2\\0&4\end{bmatrix}$. (a) Find the eigenvalues of $B$. (b) Find the eigenvalues of $B^T$. What do you notice, and why does this happen for *any* square matrix (not just this one)?
4. Find the eigenvectors and eigenvalues of $C=\begin{bmatrix}2&1\\1&2\end{bmatrix}$ using its characteristic polynomial.

**Geometric & Algebraic Multiplicity**

5. For each matrix, find the geometric and algebraic multiplicity of each eigenvalue. (a) $A=\begin{bmatrix}2&0\\-2&1\end{bmatrix}$. (b) $B=\begin{bmatrix}3&0\\0&3\end{bmatrix}$. (c) $C=\begin{bmatrix}3&0\\3&0\end{bmatrix}$.
6. Diagonalize each matrix from Problem 5, or explain why it cannot be diagonalized.

**Diagonalization**

7. Give an example of a $4\times4$ matrix whose only eigenvalues are $2$ and $7$. State the algebraic multiplicity you chose for each.
8. Diagonalize $M_2=\begin{bmatrix}4&1&0\\0&4&0\\0&0&-1\end{bmatrix}$, or explain precisely why it cannot be diagonalized.

**Conceptual — True/False and Reasoning**

9. True or false, with justification. (a) Zero cannot be an eigenvalue of any matrix. (b) The zero vector can be an eigenvector of some matrix. (c) A $2\times2$ real matrix always has a real eigenvalue. (d) A $3\times3$ real matrix always has a real eigenvalue. (e) An invertible square matrix can never have zero as an eigenvalue. (f) A non-invertible square matrix always has zero as an eigenvalue.
10. Suppose $\operatorname{char}(E)=-\lambda(2-\lambda)(-3-\lambda)$ for some unknown $3\times3$ matrix $E$. (a) What are the eigenvalues of $E$? (b) Is $E$ invertible? (c) What can you say about $\operatorname{nullity}(E)$, $\operatorname{nullity}(E-3I)$, and $\operatorname{nullity}(E+3I)$?
11. Can the geometric multiplicity of an eigenvalue ever be $0$? Explain your reasoning from the definitions.

---

## Answer Key & Misconception Notes (for tutor use — do not show student until after attempt)

| # | Answer | Common misconception |
|---|---|---|
| 1 | (a) Every non-zero vector is an eigenvector of $S$, eigenvalue $3$. (b) $R$ has no real eigenvectors (a non-trivial rotation changes every vector's direction). (c) Non-zero multiples of $\begin{bmatrix}1\\-1\end{bmatrix}$ are eigenvectors with eigenvalue $1$ (on the line); non-zero multiples of $\begin{bmatrix}1\\1\end{bmatrix}$ (perpendicular to the line) are eigenvectors with eigenvalue $0$. (d) Non-zero multiples of $\begin{bmatrix}1\\-1\end{bmatrix}$ have eigenvalue $1$ (fixed, on the line); non-zero multiples of $\begin{bmatrix}1\\1\end{bmatrix}$ have eigenvalue $-1$ (flipped). | For (c)/(d), mixing up which direction (along the line, or perpendicular to it) gets which eigenvalue — always check by applying the transformation to a specific vector in that direction and comparing, rather than guessing. |
| 2 | (a) $\operatorname{char}(A)=(1-\lambda)(-\lambda)-6=\lambda^2-\lambda-6=(\lambda-3)(\lambda+2)$. (b) Eigenvalues: $3,-2$. | Sign error expanding $(1-\lambda)(-\lambda)$ — it's $-\lambda+\lambda^2$, not $\lambda-\lambda^2$ or $-\lambda-\lambda^2$. |
| 3 | (a) Eigenvalues of $B$: $1,4$. (b) Eigenvalues of $B^T$: $1,4$ — the **same** eigenvalues. This is always true: $\det(A-\lambda I)=\det\big((A-\lambda I)^T\big)=\det(A^T-\lambda I)$, so $A$ and $A^T$ always have the identical characteristic polynomial, hence identical eigenvalues (though generally *different* eigenvectors). | Assuming $A$ and $A^T$ must have different eigenvalues just because the matrices themselves look different, instead of recognizing that determinant-and-transpose (Week 13) forces their characteristic polynomials to match exactly. |
| 4 | $\operatorname{char}(C)=(2-\lambda)^2-1=\lambda^2-4\lambda+3=(\lambda-1)(\lambda-3)$. For $\lambda=1$: eigenvectors are multiples of $\begin{bmatrix}1\\-1\end{bmatrix}$. For $\lambda=3$: eigenvectors are multiples of $\begin{bmatrix}1\\1\end{bmatrix}$. | Forgetting to expand $(2-\lambda)^2$ fully (it's $4-4\lambda+\lambda^2$, not $4-\lambda^2$), which corrupts the whole characteristic polynomial. |
| 5 | (a) $A$: eigenvalues $2,1$, each algebraic mult. $1$, geometric mult. $1$ — diagonalizable. (b) $B=3I$: eigenvalue $3$, algebraic mult. $2$, geometric mult. $2$ (eigenspace is all of $\mathbb{R}^2$). (c) $C$: eigenvalues $0,3$, each algebraic mult. $1$, geometric mult. $1$. | For (b), assuming a repeated eigenvalue must automatically have geometric multiplicity less than its algebraic multiplicity — a scalar multiple of $I$ is the extreme counterexample where every vector is an eigenvector. |
| 6 | (a) $P=\begin{bmatrix}1&0\\-2&1\end{bmatrix}$, $D=\begin{bmatrix}2&0\\0&1\end{bmatrix}$. (b) Already diagonal; e.g. $P=I$, $D=B$. (c) $P=\begin{bmatrix}0&1\\1&1\end{bmatrix}$, $D=\begin{bmatrix}0&0\\0&3\end{bmatrix}$. | Putting the eigenvalues into $D$ in a different order than their corresponding eigenvectors appear as columns of $P$ — the $i$th column of $P$ and the $i$th diagonal entry of $D$ must be a matched pair. |
| 7 | Any diagonal (or diagonalizable) matrix with only $2$'s and $7$'s on the diagonal works, e.g. $\operatorname{diag}(2,2,7,7)$ (algebraic mult. $2$ each) or $\operatorname{diag}(2,2,2,7)$ (mult. $3$ and $1$). | Trying to build a non-diagonal matrix with off-diagonal entries "to make it more interesting" — that risks accidentally changing the eigenvalues or making the matrix non-diagonalizable; a diagonal matrix is the simplest correct answer. |
| 8 | $M_2$ is upper triangular with eigenvalues $4$ (algebraic mult. $2$) and $-1$ (algebraic mult. $1$). $\operatorname{null}(M_2-4I)=\operatorname{null}\begin{bmatrix}0&1&0\\0&0&0\\0&0&-5\end{bmatrix}=\operatorname{span}\{(1,0,0)\}$, geometric mult. $1<2$. Since the geometric multiplicities can sum to at most $1+1=2\neq3$, **$M_2$ is not diagonalizable**. | Stopping after finding the eigenvalues and assuming diagonalizability follows automatically — algebraic multiplicity alone never guarantees diagonalizability; the eigenspace dimension (geometric multiplicity) must always be checked separately. |
| 9 | (a) **False** — $0$ is an eigenvalue exactly when the matrix is non-invertible (e.g. any singular matrix). (b) **False** — eigenvectors are non-zero by definition, always. (c) **False** — e.g. a $90°$ rotation has characteristic polynomial $\lambda^2+1$, no real roots. (d) **True** — an odd-degree real polynomial always has at least one real root. (e) **True** — invertible $\iff\det\neq0\iff0$ is not a root of $\operatorname{char}(A)$. (f) **True** — non-invertible $\iff\det=0=\operatorname{char}(A)$ at $\lambda=0\iff0$ is an eigenvalue. | For (c)/(d), assuming "real matrix" forces "real eigenvalues" in every dimension — parity of the dimension matters: odd-size real matrices are guaranteed a real eigenvalue, even-size ones are not. |
| 10 | (a) Eigenvalues: $0,\,2,\,-3$ (the roots of $\operatorname{char}(E)$). (b) $\det(E)=\operatorname{char}(E)$ at $\lambda=0$, which is $0$ — so $E$ is **not invertible**. (c) $\operatorname{nullity}(E)=1$ (eigenvalue $0$ has algebraic mult. $1$, so its geometric mult. is exactly $1$). $\operatorname{nullity}(E-3I)=0$, since $+3$ is **not** one of the eigenvalues $\{0,2,-3\}$ — $E-3I$ is invertible. $\operatorname{nullity}(E+3I)=1$, since $E+3I=E-(-3)I$ and $-3$ **is** an eigenvalue, with algebraic mult. $1$. | Confusing $E-3I$ with $E+3I$ — $\operatorname{nullity}(E-cI)$ tests whether $+c$ is an eigenvalue, and $\operatorname{nullity}(E+cI)=\operatorname{nullity}(E-(-c)I)$ tests whether $-c$ is one; mixing up the sign here is the single most common error in this kind of problem. |
| 11 | No. By definition, if $\lambda$ is an eigenvalue of $A$, there exists *at least one* non-zero eigenvector for $\lambda$ — so its eigenspace, $\operatorname{null}(A-\lambda I)$, contains a non-zero vector and therefore has dimension $\geq1$. A geometric multiplicity of $0$ would mean "no eigenvectors exist for $\lambda$," which directly contradicts $\lambda$ being an eigenvalue in the first place. | Confusing "geometric multiplicity is small" (which can be $1$) with "geometric multiplicity can be $0$" — the smallest possible value for an *actual* eigenvalue's geometric multiplicity is always $1$, never $0$. |
