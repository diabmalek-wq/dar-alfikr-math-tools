# Week 15 — Full-Course Review & Timed Mock Exam

**Session length:** 3 hours
**Source:** All (Kielstra *MAT A22 Course Notes*, Weeks 0–2; Siefken *MAT223 Workbook*, Modules 1–16 and Appendices 1–4)

---

## Page 1 — Introduction, Key Facts & Definitions

### Why this matters

This is the last session before the exam. Rather than introducing anything new, today collects the whole course into one map, then puts it to the test under timed conditions — exactly like the real exam. The recap below is organized into five blocks, matching the order the course was built in: foundations, spanning sets, geometry of subspaces, linear transformations, and the determinant/eigenvalue toolkit. Read it as a checklist — if any line doesn't immediately make sense, that is the topic to revisit before the exam, not during it.

### Key Fact: Foundations — Fields, Vector Spaces, $n$-tuples (Weeks 1–2)

*(Source subsection: Kielstra Wk 0–1; Siefken App. 3)*

A **field** is a number system (like $\mathbb{R}$ or $\mathbb{C}$) with addition and multiplication satisfying the usual arithmetic laws (commutativity, associativity, distributivity, identities, inverses). A **vector space** over a field is a set closed under addition and scalar multiplication satisfying ten axioms (associativity/commutativity of addition, an additive identity $\vec 0$, additive inverses, and four scalar-multiplication laws). $\mathbb{R}^n$, matrices $M_{m\times n}(\mathbb{R})$, and even function spaces are all vector spaces under this definition. Matrix operations (addition, scalar multiplication, matrix multiplication, transpose) obey specific algebraic rules — notably $AB\neq BA$ in general, and $(AB)^T=B^TA^T$.

### Key Fact: Systems & Spanning Sets (Weeks 3–6)

*(Source subsection: Siefken App. 1–2, Modules 1–3)*

A system of linear equations is solved by row reduction to **reduced row echelon form (RREF)**; the system has no solution, one solution, or infinitely many, according to whether the RREF has an inconsistent row, a pivot in every column, or a free variable. A **span** $\operatorname{span}\{\vec v_1,\ldots,\vec v_k\}$ is the set of all linear combinations of those vectors; geometrically, this is a point, line, plane, or higher-dimensional flat through the origin (or, for a **translated span**, through a given point). A set of vectors is **linearly independent** if the only linear combination equalling $\vec 0$ is the trivial one — equivalently, if none of the vectors can be written as a combination of the others.

### Key Fact: Dot Products, Subspaces & Bases (Weeks 7–9)

*(Source subsection: Siefken Modules 4–8)*

The **dot product** $\vec u\cdot\vec v$ gives length ($\|\vec v\|=\sqrt{\vec v\cdot\vec v}$) and angle ($\cos\theta=\frac{\vec u\cdot\vec v}{\|\vec u\|\|\vec v\|}$); the **projection** of $\vec u$ onto $\vec v$ is $\operatorname{proj}_{\vec v}\vec u=\frac{\vec u\cdot\vec v}{\vec v\cdot\vec v}\vec v$. A **subspace** is a span (equivalently: contains $\vec 0$, closed under addition and scalar multiplication). A **basis** is a linearly independent spanning set; its size is the **dimension** of the subspace. **Coordinates** $[\vec v]_B$ express a vector in terms of a chosen basis $B$, and the **change-of-basis matrix** converts coordinates between two bases.

### Key Fact: Linear Transformations (Weeks 10–12)

*(Source subsection: Siefken Modules 9–13)*

A function $T$ is a **linear transformation** exactly when $T(\vec u+\vec v)=T(\vec u)+T(\vec v)$ and $T(c\vec u)=cT(\vec u)$ for all vectors and scalars — equivalently, when $T(\vec x)=A\vec x$ for a unique **standard matrix** $A=[T]$. **Composition** of linear transformations corresponds to matrix multiplication: $[S\circ T]=[S][T]$. The **range** (column space) and **nullspace** (kernel) of $T$ satisfy $\dim(\operatorname{range})+\dim(\operatorname{null})=n$ (the Rank–Nullity Theorem). $T$ is **invertible** exactly when $[T]$ is invertible, i.e. $\operatorname{null}(T)=\{\vec 0\}$ and $\operatorname{range}(T)=\mathbb{R}^n$; then $[T^{-1}]=[T]^{-1}$. Changing basis transforms a matrix representation via $[T]_{B}=P^{-1}[T]_{\text{std}}P$, where $P$'s columns are $B$'s vectors.

### Key Fact: Determinants, Eigenvalues & Diagonalization (Weeks 13–14)

*(Source subsection: Siefken Module 14–16, App. 4)*

The **determinant** measures the signed volume-scaling factor of a linear transformation; $\det(A)\neq0\iff A$ is invertible, and $\det(AB)=\det(A)\det(B)$. For $2\times2$: $\det\begin{bmatrix}a&b\\c&d\end{bmatrix}=ad-bc$; for $3\times3$, use the Rule of Sarrus or cofactor expansion. An **eigenvector** $\vec v\neq\vec 0$ of $A$ satisfies $A\vec v=\lambda\vec v$; eigenvalues are the roots of $\operatorname{char}(A)=\det(A-\lambda I)$. $A$ is **diagonalizable** ($A=PDP^{-1}$) exactly when the geometric multiplicities of all its eigenvalues sum to $n$ — equivalently, when geometric multiplicity equals algebraic multiplicity for every eigenvalue.

### Fact: How the Pieces Connect

*(Source subsection: cumulative)*

For an $n\times n$ matrix $A$, the following are all **equivalent**: $A$ is invertible $\iff\det(A)\neq0\iff0$ is not an eigenvalue of $A\iff\operatorname{null}(A)=\{\vec 0\}\iff$ the columns of $A$ are linearly independent $\iff$ the columns of $A$ form a basis of $\mathbb{R}^n\iff\operatorname{rank}(A)=n$. This single chain of equivalences ties together nearly every major topic in the course, and exam questions frequently test it by giving one fact in the chain and asking you to conclude another.

---

## Pages 2–3 — Solved Examples

**Example 1 (Spans, independence, and dimension together).** Let $\vec v_1=\begin{bmatrix}1\\2\\1\end{bmatrix}$, $\vec v_2=\begin{bmatrix}0\\1\\1\end{bmatrix}$, $\vec v_3=\begin{bmatrix}1\\4\\3\end{bmatrix}$. Determine $\dim(\operatorname{span}\{\vec v_1,\vec v_2,\vec v_3\})$, and find a basis for it.

Row-reduce $[\vec v_1\mid\vec v_2\mid\vec v_3]^T$ (as rows, to find dependencies): $\begin{bmatrix}1&2&1\\0&1&1\\1&4&3\end{bmatrix}\xrightarrow{R_3-R_1}\begin{bmatrix}1&2&1\\0&1&1\\0&2&2\end{bmatrix}\xrightarrow{R_3-2R_2}\begin{bmatrix}1&2&1\\0&1&1\\0&0&0\end{bmatrix}$. Only two pivots, so $\vec v_3=\vec v_1+2\vec v_2$ (check: $\begin{bmatrix}1\\2\\1\end{bmatrix}+2\begin{bmatrix}0\\1\\1\end{bmatrix}=\begin{bmatrix}1\\4\\3\end{bmatrix}$ ✓) and the span has dimension $2$, with basis $\{\vec v_1,\vec v_2\}$. $\blacksquare$

**Example 2 (Linear transformation: matrix, range, nullspace, rank–nullity).** Let $T:\mathbb{R}^3\to\mathbb{R}^2$, $T\begin{bmatrix}x\\y\\z\end{bmatrix}=\begin{bmatrix}x+y+z\\2x+2y+2z\end{bmatrix}$. Find $[T]$, $\operatorname{range}(T)$, $\operatorname{null}(T)$, and verify Rank–Nullity.

$[T]=\begin{bmatrix}1&1&1\\2&2&2\end{bmatrix}$. Row $2$ is $2\times$ Row $1$, so $\operatorname{rank}([T])=1$ and $\operatorname{range}(T)=\operatorname{span}\left\{\begin{bmatrix}1\\2\end{bmatrix}\right\}$ (a line, not all of $\mathbb{R}^2$ — $T$ is not onto). $\operatorname{null}(T)$: solve $x+y+z=0$, a plane through the origin with $\dim=2$, basis $\left\{\begin{bmatrix}1\\-1\\0\end{bmatrix},\begin{bmatrix}1\\0\\-1\end{bmatrix}\right\}$. Rank–Nullity: $\dim(\operatorname{range})+\dim(\operatorname{null})=1+2=3=n$. ✓ $\blacksquare$

**Example 3 (Change of basis, full circuit).** Let $B=\left\{\begin{bmatrix}1\\1\end{bmatrix},\begin{bmatrix}1\\-1\end{bmatrix}\right\}$ and $\vec v=\begin{bmatrix}5\\1\end{bmatrix}$. Find $[\vec v]_B$, then use it to reconstruct $\vec v$.

Solve $c_1\begin{bmatrix}1\\1\end{bmatrix}+c_2\begin{bmatrix}1\\-1\end{bmatrix}=\begin{bmatrix}5\\1\end{bmatrix}$: adding the two scalar equations $c_1+c_2=5$, $c_1-c_2=1$ gives $c_1=3,c_2=2$. So $[\vec v]_B=\begin{bmatrix}3\\2\end{bmatrix}$. Reconstructing: $3\begin{bmatrix}1\\1\end{bmatrix}+2\begin{bmatrix}1\\-1\end{bmatrix}=\begin{bmatrix}5\\1\end{bmatrix}=\vec v$ ✓. $\blacksquare$

**Example 4 (Determinant, invertibility, and eigenvalues in one problem).** Let $A=\begin{bmatrix}3&1\\2&2\end{bmatrix}$. Is $A$ invertible? Find its eigenvalues, and state whether $A$ is diagonalizable.

$\det(A)=(3)(2)-(1)(2)=4\neq0$, so $A$ is **invertible** (and by the equivalence chain, $0$ is not an eigenvalue). $\operatorname{char}(A)=\det\begin{bmatrix}3-\lambda&1\\2&2-\lambda\end{bmatrix}=(3-\lambda)(2-\lambda)-2=\lambda^2-5\lambda+4=(\lambda-1)(\lambda-4)$. Eigenvalues $1,4$ — two *distinct* eigenvalues for a $2\times2$ matrix guarantees each has geometric multiplicity $1=$ its algebraic multiplicity, so **$A$ is diagonalizable**. $\blacksquare$

**Example 5 (A multi-topic "if-then" reasoning problem, exam-style).** Suppose $A$ is a $3\times3$ matrix with $\det(A)=0$. What can you conclude about $\operatorname{null}(A)$, the columns of $A$, and whether $0$ is an eigenvalue of $A$?

By the equivalence chain: $\det(A)=0\Rightarrow A$ is **not invertible** $\Rightarrow\operatorname{null}(A)\neq\{\vec 0\}$ (there is a non-trivial null space) $\Rightarrow$ the columns of $A$ are **linearly dependent** (they do not form a basis of $\mathbb{R}^3$) $\Rightarrow$ **$0$ is an eigenvalue of $A$** (since $\operatorname{char}(A)$ at $\lambda=0$ equals $\det(A)=0$). Note what we *cannot* conclude: the exact dimension of $\operatorname{null}(A)$ (it could be $1$ or $2$, not $3$, unless $A=0$) — $\det(A)=0$ only guarantees the null space is non-trivial, not its size. $\blacksquare$

---

## Pages 4–5 — Practice Problems (unsolved)

**Suggested time budget:** treat this as a $90$-minute timed mock exam (roughly $8$–$9$ minutes per problem); work straight through without checking the answer key, then review afterward.

**Foundations & Spanning Sets**

1. Is the set of all $2\times2$ matrices with determinant equal to $1$ a vector space (under the usual matrix addition and scalar multiplication)? Justify your answer using the vector space axioms.
2. Let $\vec v_1=\begin{bmatrix}1\\0\\-1\end{bmatrix}$, $\vec v_2=\begin{bmatrix}2\\1\\0\end{bmatrix}$, $\vec v_3=\begin{bmatrix}0\\1\\2\end{bmatrix}$. (a) Are $\vec v_1,\vec v_2,\vec v_3$ linearly independent? (b) Find $\dim(\operatorname{span}\{\vec v_1,\vec v_2,\vec v_3\})$.
3. Solve the system $\begin{cases}x+2y-z=3\\2x+3y+z=5\\-x-y+2z=-2\end{cases}$ by row reduction, and state whether the solution is unique.

**Subspaces, Bases & Geometry**

4. Let $W=\operatorname{span}\left\{\begin{bmatrix}1\\1\\0\end{bmatrix},\begin{bmatrix}0\\1\\1\end{bmatrix}\right\}$. (a) Find a normal vector to the plane $W$. (b) Find the projection of $\vec u=\begin{bmatrix}1\\2\\3\end{bmatrix}$ onto $\begin{bmatrix}1\\1\\0\end{bmatrix}$.
5. Let $B=\left\{\begin{bmatrix}2\\1\end{bmatrix},\begin{bmatrix}1\\1\end{bmatrix}\right\}$. Find $[\vec v]_B$ for $\vec v=\begin{bmatrix}4\\3\end{bmatrix}$.

**Linear Transformations**

6. Let $T:\mathbb{R}^2\to\mathbb{R}^2$ be the linear transformation with $T\begin{bmatrix}1\\0\end{bmatrix}=\begin{bmatrix}2\\1\end{bmatrix}$ and $T\begin{bmatrix}0\\1\end{bmatrix}=\begin{bmatrix}-1\\3\end{bmatrix}$. (a) Find $[T]$. (b) Is $T$ invertible? If so, find $[T^{-1}]$.
7. Let $S,T:\mathbb{R}^2\to\mathbb{R}^2$ with $[S]=\begin{bmatrix}0&-1\\1&0\end{bmatrix}$ and $[T]=\begin{bmatrix}2&0\\0&2\end{bmatrix}$. Find $[S\circ T]$ and $[T\circ S]$. Are they equal?
8. Let $A=\begin{bmatrix}1&2&1\\2&4&2\\1&2&1\end{bmatrix}$ be the standard matrix of a linear transformation $T:\mathbb{R}^3\to\mathbb{R}^3$. Find $\operatorname{rank}(A)$ and $\dim(\operatorname{null}(T))$ without fully solving for the null space, then verify Rank–Nullity by finding the null space directly.

**Determinants, Eigenvalues & Diagonalization**

9. Let $A=\begin{bmatrix}2&0&1\\1&1&0\\0&2&1\end{bmatrix}$. Compute $\det(A)$, and state whether $A$ is invertible.
10. Find the eigenvalues and eigenvectors of $B=\begin{bmatrix}4&2\\1&3\end{bmatrix}$, and determine whether $B$ is diagonalizable.

**Mixed / Cumulative Reasoning**

11. True or false, with justification for each. (a) If $A$ is a $4\times4$ matrix with $\operatorname{rank}(A)=4$, then $A$ is invertible. (b) A set of $4$ vectors in $\mathbb{R}^3$ can be linearly independent. (c) If $0$ is an eigenvalue of $A$, then $A$ is not invertible. (d) Every basis of a given subspace has the same number of vectors. (e) If $A$ and $B$ are both diagonalizable, then $AB$ is always diagonalizable.
12. A $3\times3$ matrix $A$ has characteristic polynomial $\operatorname{char}(A)=-(\lambda-2)^2(\lambda-5)$. (a) What are the eigenvalues of $A$, and their algebraic multiplicities? (b) If $\operatorname{rank}(A-2I)=1$, is $A$ diagonalizable? (c) What is $\det(A)$?

---

## Answer Key & Misconception Notes (for tutor use — do not show student until after attempt)

| # | Answer | Common misconception |
|---|---|---|
| 1 | **No.** The zero matrix (all entries $0$) has determinant $0\neq1$, so it is not in the set — but every vector space must contain the additive identity $\vec 0$. The set fails the very first axiom needed. | Trying to check closure under addition/scalar multiplication first (which also fails, e.g. two determinant-$1$ matrices need not sum to a determinant-$1$ matrix) instead of using the fast, decisive test: does the set contain $\vec 0$ at all? |
| 2 | (a) Row-reducing $[\vec v_1\mid\vec v_2\mid\vec v_3]$ gives $3$ pivots — **linearly independent**. (b) Since they're independent, $\dim(\operatorname{span})=3$ (they form a basis of $\mathbb{R}^3$). | Forgetting that $3$ independent vectors in $\mathbb{R}^3$ automatically span all of $\mathbb{R}^3$ — re-deriving the span "from scratch" instead of using the independence result already found in part (a). |
| 3 | Row-reducing the augmented matrix yields a unique solution $x=1,\,y=1,\,z=0$ (RREF has a pivot in every variable column and no inconsistent row). | Arithmetic slips while combining three equations at once — always re-substitute the found values back into all three original equations to check, not just one. |
| 4 | (a) A normal vector is $\begin{bmatrix}1\\1\\0\end{bmatrix}\times\begin{bmatrix}0\\1\\1\end{bmatrix}=\begin{bmatrix}1\\-1\\1\end{bmatrix}$ (or any non-zero scalar multiple). (b) $\operatorname{proj}_{(1,1,0)}\vec u=\frac{\vec u\cdot(1,1,0)}{(1,1,0)\cdot(1,1,0)}(1,1,0)=\frac{3}{2}\begin{bmatrix}1\\1\\0\end{bmatrix}=\begin{bmatrix}3/2\\3/2\\0\end{bmatrix}$. | For (a), forgetting that a normal vector to a plane spanned by two vectors is found via the *cross product* of those two vectors, not by inspection or by solving a random linear system. |
| 5 | Solve $c_1\begin{bmatrix}2\\1\end{bmatrix}+c_2\begin{bmatrix}1\\1\end{bmatrix}=\begin{bmatrix}4\\3\end{bmatrix}$: $c_1=1,c_2=2$, so $[\vec v]_B=\begin{bmatrix}1\\2\end{bmatrix}$. | Writing the coordinate vector in the same order as $\vec v$'s standard entries rather than matching each coefficient to its corresponding basis vector — always double check by reconstructing $\vec v$ from $[\vec v]_B$ and $B$. |
| 6 | (a) $[T]=\begin{bmatrix}2&-1\\1&3\end{bmatrix}$ (columns are the images of $\vec e_1,\vec e_2$). (b) $\det([T])=6-(-1)=7\neq0$, so $T$ **is invertible**; $[T^{-1}]=\frac{1}{7}\begin{bmatrix}3&1\\-1&2\end{bmatrix}$. | Forgetting that the columns of $[T]$ are $T(\vec e_1)$ and $T(\vec e_2)$ **in that order** — swapping them gives the transpose of the correct matrix, not $[T]$ itself. |
| 7 | $[S\circ T]=[S][T]=\begin{bmatrix}0&-2\\2&0\end{bmatrix}$; $[T\circ S]=[T][S]=\begin{bmatrix}0&-2\\2&0\end{bmatrix}$. They **are equal** here (because $[T]=2I$ is a scalar multiple of the identity, which commutes with everything) — but this is a special case, not a general rule. | Concluding from this one example that composition of linear transformations is always commutative — matrix multiplication is non-commutative in general; this pair happens to commute only because one of the matrices is a scalar multiple of $I$. |
| 8 | Rows $2$ and $3$ of $A$ are multiples of Row $1$ ($R_2=2R_1$, $R_3=R_1$), so $\operatorname{rank}(A)=1$; by Rank–Nullity, $\dim(\operatorname{null}(T))=3-1=2$. Direct check: $\operatorname{null}(A)$ solves $x+2y+z=0$, a plane with basis $\left\{\begin{bmatrix}-2\\1\\0\end{bmatrix},\begin{bmatrix}-1\\0\\1\end{bmatrix}\right\}$, dimension $2$. ✓ | Computing the full null space first "just to be safe" instead of reading the rank directly off the row-dependency pattern — recognizing repeated/proportional rows is a fast rank shortcut worth using on exam problems. |
| 9 | Expanding along the first row: $\det(A)=2(1\cdot1-0\cdot2)-0(1\cdot1-0\cdot0)+1(1\cdot2-1\cdot0)=2(1)-0+1(2)=4$. Since $\det(A)=4\neq0$, $A$ **is invertible**. | Picking a row or column with no zeros to expand along, creating unnecessary extra terms — expanding along the row or column with the most zeros (here, row $1$ has one zero, or column $2$ also works well) minimizes arithmetic. |
| 10 | $\operatorname{char}(B)=(4-\lambda)(3-\lambda)-2=\lambda^2-7\lambda+10=(\lambda-2)(\lambda-5)$. Eigenvalues $2,5$. For $\lambda=2$: $\operatorname{null}(B-2I)=\operatorname{null}\begin{bmatrix}2&2\\1&1\end{bmatrix}=\operatorname{span}\left\{\begin{bmatrix}1\\-1\end{bmatrix}\right\}$. For $\lambda=5$: $\operatorname{null}(B-5I)=\operatorname{null}\begin{bmatrix}-1&2\\1&-2\end{bmatrix}=\operatorname{span}\left\{\begin{bmatrix}2\\1\end{bmatrix}\right\}$. Two distinct eigenvalues in a $2\times2$ matrix $\Rightarrow$ **diagonalizable**. | Forgetting that once two eigenvalues come out *distinct* for a $2\times2$ (or more generally, all $n$ eigenvalues of an $n\times n$ matrix are distinct), diagonalizability is automatic — no need to double-check geometric multiplicities in that case, though computing the eigenvectors is still required to actually build $P$. |
| 11 | (a) **True** — for a square matrix, full rank $\iff$ invertible. (b) **False** — at most $3$ vectors in $\mathbb{R}^3$ can be linearly independent (any $4$ vectors in a $3$-dimensional space must be dependent). (c) **True** — this is the equivalence chain directly: $0$ an eigenvalue $\iff\det(A)=0\iff A$ not invertible. (d) **True** — this is the definition of dimension being well-defined. (e) **False** in general — diagonalizability of $A$ and $B$ individually does not guarantee $AB$ is diagonalizable, especially if $A$ and $B$ don't share the same eigenvectors (a common exam trap). | For (e), assuming diagonalizability is preserved under matrix multiplication the way it's preserved under, say, taking powers of a single diagonalizable matrix — the key requirement (a shared eigenbasis) generally fails for two unrelated diagonalizable matrices. |
| 12 | (a) Eigenvalues $2$ (algebraic multiplicity $2$) and $5$ (algebraic multiplicity $1$). (b) $\operatorname{rank}(A-2I)=1\Rightarrow\operatorname{nullity}(A-2I)=3-1=2=$ geometric multiplicity of $2$, which matches its algebraic multiplicity $2$; the eigenvalue $5$ (multiplicity $1$) automatically matches too — so **$A$ is diagonalizable**. (c) $\det(A)=\operatorname{char}(A)$ at $\lambda=0$: $-(0-2)^2(0-5)=-(4)(-5)=20$. | For (c), forgetting the leading minus sign in the given characteristic polynomial when substituting $\lambda=0$ — a sign slip here flips the final determinant's sign entirely. |
