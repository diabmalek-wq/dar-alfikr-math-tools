# Week 12: Diagonalizability

## Big idea
A linear operator is diagonalizable exactly when $V$ has a basis of eigenvectors. Distinct eigenvalues guarantee this, and in general algebraic and geometric multiplicities decide it.

## Definitions
- **Diagonalizable operator**: $T\in\mathcal{L}(V)$ for which some basis $\alpha$ makes $[T]_\alpha$ diagonal, equivalently $V$ has a basis of eigenvectors.
- **Diagonalizable matrix**: a matrix similar to a diagonal matrix, i.e. $A=PDP^{-1}$.
- **Algebraic multiplicity** $\mathrm{Alg}(\lambda)$: the number of factors $(x-\lambda)$ in the linear factorization of the characteristic polynomial.
- **Geometric multiplicity** $\mathrm{Geo}(\lambda)=\dim E_\lambda$.
- **Dependence relation**: a polynomial $p$ with $p(T)=Z$, where $Z$ is the zero map.

## Theorems and results
- **Eigenbasis.** $T$ is diagonalizable iff $V$ has a basis of eigenvectors; the diagonal entries are then the eigenvalues. *Idea:* a diagonal matrix has columns $T(\vec v_i)=\lambda_i\vec v_i$, and conversely.
- **Matrix form.** $A$ is diagonalizable iff $A$ has $n$ linearly independent eigenvectors. *Idea:* $AP=PD$ forces the columns of $P$ to be eigenvectors.
- **Distinct eigenvalues.** Eigenvectors for distinct eigenvalues are linearly independent. *Idea:* take a shortest dependence, apply $T$, subtract a multiple of the original, and get a shorter dependence. Corollary: $n$ distinct real eigenvalues on an $n$-dimensional real space give a diagonalizable operator.
- **Geometric $\le$ algebraic.** For a real eigenvalue, $\mathrm{Geo}(\lambda)\le\mathrm{Alg}(\lambda)$. *Idea:* extend a basis of $E_\lambda$ to a basis of $V$; the characteristic polynomial then has a factor $(t-\lambda)^{\mathrm{Geo}(\lambda)}$.
- **Eigenspaces.** For $\lambda_1\neq\lambda_2$, $E_{\lambda_1}\cap E_{\lambda_2}=\{\vec 0\}$. Independent sets from distinct eigenspaces combine into an independent set.
- **Criterion.** With distinct real eigenvalues $\lambda_j$ of multiplicities $m_j$, $T$ is diagonalizable iff $\dim V=\sum_j m_j$ and $\dim E_{\lambda_j}=m_j$ for each $j$. Equivalently, the eigenspaces sum to $V$.
- **Dependence relation.** If $p(T)=Z$ and $\lambda$ is an eigenvalue of $T$, then $p(\lambda)=0$. The roots of $p$ are the only possible eigenvalues; not every root need be one.
- **Idempotent case.** If $T^2=T$, then $V=E_0+E_1$ with $E_0\cap E_1=\{\vec 0\}$, so $T$ is diagonalizable. *Idea:* $\vec v=(\vec v-T\vec v)+T\vec v$.
- **Matrix functions.** If $A=PDP^{-1}$, then $f(A)=Pf(D)P^{-1}$, with $f(D)$ computed entrywise. Likewise $e^A=Pe^DP^{-1}$, $\sin A=P\sin(D)P^{-1}$, $\cos A=P\cos(D)P^{-1}$.

## Techniques / procedures
1. **Diagonalize $A$:** (a) find eigenvalues from $\chi_A$; (b) solve $(A-\lambda I)\vec x=\vec 0$ for each $\lambda$; (c) if $n$ independent eigenvectors exist, set $P=[\vec v_1\cdots\vec v_n]$ and $D=\mathrm{diag}(\lambda_i)$.
2. **Test via multiplicities:** factor $\chi_A$ for $\mathrm{Alg}$; row reduce $A-\lambda I$ and count free variables for $\mathrm{Geo}$. Check $\mathrm{Alg}=\mathrm{Geo}$ only when $\mathrm{Alg}>1$.
3. **Compute $f(A)$:** evaluate $f$ on each diagonal entry of $D$, then return $Pf(D)P^{-1}$.
4. **Compute $f(T)$:** choose a basis $\alpha$, form $A=[T]_\alpha$, diagonalize, compute $f(A)$, and convert back with $[f(T)]_\alpha=f(A)$.
5. **Eigenvector from a dependence relation:** apply the factors $(T-\lambda_iI)$ successively to a nonzero $\vec v$ until the result is $\vec 0$; the last nonzero vector is an eigenvector for the last factor used.

## Worked examples in the notes
- $T(x,y)=(x+4y,2x+3y)$ $\to$ eigenvalues $5,-1$, eigenvectors $(1,1)$ and $(-2,1)$, which are independent $\to$ diagonalizable.
- $A=\begin{pmatrix}0&3&0\\1&0&-1\\0&2&0\end{pmatrix}$ $\to$ $\chi=-\lambda(\lambda-1)(\lambda+1)$ $\to$ eigenvectors $(1,0,1)$, $(3,1,2)$, $(3,-1,2)$ for $0,1,-1$ $\to$ diagonalizable.
- $\begin{pmatrix}1&1&0&0\\0&1&0&0\\0&0&2&0\\0&0&0&3\end{pmatrix}$ $\to$ $\mathrm{Alg}(1)=2$ but $\mathrm{Geo}(1)=1$ $\to$ the criterion fails.
- $\begin{pmatrix}7&-4&0\\8&-5&0\\6&-6&3\end{pmatrix}$ $\to$ $\chi=-(\lambda-3)^2(\lambda+1)$; $E_3=\mathrm{span}\{(1,1,0),(0,0,1)\}$, so $\mathrm{Geo}(3)=\mathrm{Alg}(3)=2$ $\to$ diagonalizable.
- $A=\begin{pmatrix}1&1\\1&0\end{pmatrix}$ $\to$ dependence $A^2-A-I=0$ $\to$ possible eigenvalues are the roots of $x^2-x-1$.
- $A=\begin{pmatrix}1&4\\2&3\end{pmatrix}$ $\to$ dependence $(A-5I)(A+I)=0$ $\to$ possible eigenvalues $5,-1$; the vector $(2,3)$ is an eigenvector for neither.

## Common pitfalls
- The zero vector is never an eigenvector.
- The roots of a dependence relation are only candidate eigenvalues; not all of them need be eigenvalues.
- $\mathrm{Alg}=\mathrm{Geo}$ must be verified only for eigenvalues with $\mathrm{Alg}>1$.
