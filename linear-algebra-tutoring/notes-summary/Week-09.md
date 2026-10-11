# Week 9: Inverses of Linear Transformations

## Big idea
A function has an inverse exactly when it is bijective, and the inverse of a linear transformation is again linear. For linear maps between finite-dimensional spaces, the inverse is computed by row reducing the matrix of the map against the identity.

## Definitions
- **Inverse of $S:V\to W$**: a function $T:W\to V$ with $T(S(\vec v))=\vec v$ for all $\vec v\in V$ and $S(T(\vec w))=\vec w$ for all $\vec w\in W$.
- **Isomorphism**: an invertible linear transformation $T:V\to W$.
- **Endomorphism**: a linear transformation $T:V\to V$ (linear operator); $\mathcal{L}(V)$ is the set of all of them.
- **Automorphism**: an invertible endomorphism; $\mathrm{Aut}(V)\subseteq\mathcal{L}(V)$ is the set of these.
- **Isomorphic**: $V$ and $W$ are isomorphic if an isomorphism $T:V\to W$ exists.
- **Group**: $\mathrm{Aut}(V)$ under composition is a group (associative, identity $I$, inverses).
- **Elementary row operations**: (i) add $\lambda$ times row $i$ to row $j$, with $i\neq j$; (ii) multiply a row by $\lambda\neq 0$; (iii) interchange two rows.

## Theorems and results
- **Inverse exists iff bijective.** $S$ has an inverse iff $S$ is injective and surjective. *Idea:* an inverse gives surjectivity via $\vec v=T(\vec w)$ and injectivity by applying $T$ to $S(\vec v_1)=S(\vec v_2)$. Conversely, define $T(\vec w)=\vec v$ where $S(\vec v)=\vec w$.
- **Uniqueness.** An inverse, if it exists, is unique. *Idea:* every $\vec w$ equals $S(\vec v)$ for some $\vec v$, so two inverses agree on $\vec w$.
- **Inverse of a linear map is linear.** If linear $S$ has inverse $T$, then $T$ is linear. *Idea:* write vectors as $S(\cdot)$ and use linearity of $S$.
- **Row operations are invertible.** Scaling by $\lambda$ is undone by scaling by $\dfrac{1}{\lambda}$; $R_j+\lambda R_i$ is undone by $R_j-\lambda R_i$; a swap is its own inverse. Each operation is left-multiplication by an invertible elementary matrix $E$.
- **Inverse algorithm.** If $[M\mid I]$ reduces to $[A\mid M']$ in RREF with $A=I$, then $M^{-1}=M'$; otherwise $M$ is not invertible. *Idea:* $E_k\cdots E_1M=I$, so the product is a left inverse, hence the inverse.
- **Matrix of an inverse.** For invertible $T$ and bases, the matrix of $T^{-1}$ is the inverse of the matrix of $T$ (exact index placement [unclear in scan]; proof left as exercise).
- **Isomorphism test.** $T:V\to W$ is an isomorphism iff it is injective and surjective. If $\dim V=\dim W$ is finite, either one suffices.
- **Dimension criterion.** Finite-dimensional real spaces $V,W$ are isomorphic iff $\dim V=\dim W$. Any $n$-dimensional space over $F$ is isomorphic to $F^n$.

## Techniques / procedures
1. **Invert $M$:** form $[M\mid I]$, row reduce to RREF, and read $M^{-1}$ from the right block if the left block is $I$.
2. **Invert $T:V\to W$:** pick bases $\alpha,\beta$; compute $[T]$; invert the matrix; define $T^{-1}$ from the inverse matrix.
3. **Prove an isomorphism:** check linearity; show $\ker T=\{\vec 0\}$ (injective); show surjectivity, or use dimension equality to need only one.
4. **Show $V\cong F^n$:** choose a basis, map $\sum a_i\vec v_i\mapsto(a_1,\dots,a_n)$, check linearity, injectivity and surjectivity.

## Worked examples in the notes
- $T(a+bx)=(a+b,a)$, $P_1(\mathbb R)\to\mathbb R^2$, standard bases $\to [T]=\begin{pmatrix}1&1\\1&0\end{pmatrix}$, inverse matrix $\begin{pmatrix}0&1\\1&-1\end{pmatrix}$, so $T^{-1}(a,b)=b+(a-b)x$.
- $\begin{pmatrix}1&2&3\\0&4&5\\0&0&6\end{pmatrix}$ $\to$ row reduces to $I$ $\to$ invertible (inverse entries [unclear in scan]).
- $\begin{pmatrix}1&2&3\\2&5&7\\3&7&10\end{pmatrix}$ $\to$ reduction yields a zero row $\to$ not invertible.
- $M_{2\times2}(\mathbb R)\cong\mathbb R^4$ via $\begin{pmatrix}a&b\\c&d\end{pmatrix}\mapsto(a,b,c,d)$ $\to$ linear, $\ker=\{\vec 0\}$, surjective.
- $P_3(\mathbb R)\cong\mathbb R^4$ via $a_0+a_1x+a_2x^2+a_3x^3\mapsto(a_0,a_1,a_2,a_3)$ $\to$ proof left as exercise.

## Common pitfalls
- The scalar in $R_i\to\lambda R_i$ must be nonzero, or the operation cannot be undone.
- $R_j+\lambda R_i$ requires $i\neq j$.
- The inverse algorithm always works in theory, but it is numerically unstable and costly.
