# Week 11: Change of Basis and Eigenvalue and Eigenvectors

## Big idea
Eigenvectors are nonzero vectors that a linear map only rescales, and a matrix similar to a diagonal matrix makes its powers and polynomials easy to compute. Change-of-basis matrices relate coordinates across bases, which is what lets eigenvectors produce a diagonalizing basis.

## Definitions
- **Polynomial of a matrix**: for $p(x)=\sum_i a_ix^i$, $p(A)=\sum_i a_iA^i$ with $A^0=I$.
- **Similar matrices**: $A,B\in M_{n\times n}(F)$ are similar if $B=M^{-1}AM$ for some invertible $M$.
- **Diagonalizable matrix**: a matrix similar to a diagonal matrix.
- **Eigenvector and eigenvalue**: for $M\in M_{n\times n}(F)$, a nonzero $\vec x$ with $M\vec x=\lambda\vec x$ for some $\lambda\in F$. For $T\in\mathcal{L}(V)$, a nonzero $\vec v$ with $T(\vec v)=\lambda\vec v$.
- **Eigenspace**: $E_\lambda=\{\vec v: T(\vec v)=\lambda\vec v\}=\ker(T-\lambda I)$, a subspace.
- **Characteristic polynomial**: $\chi_A(x)=\det(A-xI)$.
- **Change-of-basis matrix**: the matrix that converts coordinates from one basis to another, $[\vec v]_\beta=[I]\,[\vec v]_\alpha$ (index placement [unclear in scan]).

## Theorems and results
- **Diagonal powers.** For diagonal $D$, $(D^k)_{ii}=d_{ii}^k$. Hence $p(D)$ is diagonal with entries $p(d_{ii})$ (induction, left as exercise).
- **Similarity and powers.** If $B=M^{-1}AM$, then $A^k=MB^kM^{-1}$ and $p(A)=Mp(B)M^{-1}$. *Idea:* the inner $M^{-1}M$ factors cancel.
- **Eigenvectors in coordinates.** $\vec v$ is an eigenvector of $T$ with eigenvalue $\lambda$ iff $[\vec v]_\alpha$ is an eigenvector of $[T]_\alpha$ with eigenvalue $\lambda$.
- **Kernel form.** $M\vec x=\lambda\vec x$ iff $\vec x\in\mathrm{null}(M-\lambda I)$.
- **Eigenvalues are roots.** $\lambda$ is an eigenvalue iff $\chi(\lambda)=0$. *Idea:* $\det(A-\lambda I)=0$ iff $A-\lambda I$ has a nonzero kernel vector.
- **Count.** An $n\times n$ matrix has at most $n$ complex eigenvalues, and at most $n$ real ones. *Idea:* $\chi$ has degree $n$, and the fundamental theorem of algebra factors it.
- **Basis independence.** The eigenvalues of $T$ do not depend on the basis used to compute them.
- **Change of basis.** Change-of-basis matrices are inverse to each other. Matrix representations of $T$ in two bases are related by change-of-basis matrices (exact placement [unclear in scan]).

## Techniques / procedures
1. **Eigenpairs of a matrix:** (a) compute $\det(A-xI)$; (b) factor to find the roots $\lambda_j$; (c) row reduce $A-\lambda_jI$ and take nonzero solutions as eigenvectors.
2. **Eigenpairs of $T$:** pick a basis $\alpha$, compute $[T]_\alpha$, apply the steps above, then convert eigenvectors back using $\alpha$.
3. **Compute $p(A)$ for diagonalizable $A$:** find $M,D$ with $A=MDM^{-1}$; compute $p(D)$ entrywise; return $p(A)=Mp(D)M^{-1}$.
4. **Change-of-basis matrix:** write the coordinates of each basis vector in the other basis as columns; invert by Gauss–Jordan when needed.

## Worked examples in the notes
- $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$ $\to$ direct multiplication $\to$ $A^2=\begin{pmatrix}7&10\\15&22\end{pmatrix}$.
- $p(x)=3x^2+2x+5$ applied to $\begin{pmatrix}1&2\\3&4\end{pmatrix}$ $\to$ $3A^2+2A+5I$ $\to$ $\begin{pmatrix}28&34\\51&79\end{pmatrix}$.
- Diagonal matrix with transcendental entries $\to$ powers computed entrywise.
- $T(x,y)=(2x+y,x+2y)$ $\to$ $T(1,1)=(3,3)$ $\to$ $(1,1)$ is an eigenvector with eigenvalue $3$.
- $[T]=\begin{pmatrix}1&2\\4&3\end{pmatrix}$ $\to$ $\chi=(\lambda-5)(\lambda+1)$ $\to$ $E_5=\mathrm{span}\{(1,2)\}$, $E_{-1}=\mathrm{span}\{(-1,1)\}$. (The printed formula $(x+4y,2x+3y)$ does not match this matrix [unclear in scan].)
- $A=\begin{pmatrix}1&0&0\\0&2&0\\0&0&2\end{pmatrix}$ $\to$ $\chi=(1-x)(2-x)^2$ $\to$ eigenvalues $1$ and $2$.
- $A=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ $\to$ $\chi=x^2+1$ $\to$ no real eigenvalues; eigenvalues $\pm i$ over $\mathbb C$.
- Fibonacci $A=\begin{pmatrix}1&1\\1&0\end{pmatrix}$ $\to$ $\chi=x^2-x-1$ $\to$ eigenvalues $\dfrac{1\pm\sqrt5}{2}$, eigenvectors $t(\lambda,1)$.

## Common pitfalls
- The zero vector is never accepted as an eigenvector.
- Not every matrix has eigenvalues: they must lie in the field used, as the $\mathbb R$-rotation example shows.
- Only real roots count when working over $\mathbb R$.
- Finding eigenvalues and eigenvectors by hand is laborious, so follow the fixed sequence of steps.
