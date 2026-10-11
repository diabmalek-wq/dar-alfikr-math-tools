# Week 5: Sums and Direct Sums

## Big idea
For subspaces $U,V\subseteq W$, the sum $U+V$ need not have unique decompositions $w=u+v$. A direct sum is the case where every vector of $U+V$ has exactly one such decomposition, which the notes show is equivalent to $U\cap V=\{0\}$.

## Definitions
- **Sum**: $U+V=\{u+v : u\in U,\ v\in V\}$.
- **Direct sum** ($U\oplus V$): $U$ and $V$ form a direct sum if $0=u+v$ with $u\in U$, $v\in V$ forces $u=0$ and $v=0$.
- **Direct sum of $U_1,\dots,U_k$**: $0=u_1+\cdots+u_k$ with $u_i\in U_i$ forces $u_1=\cdots=u_k=0$.
- **Linearly independent family of subspaces**: the same condition as the direct sum of $U_1,\dots,U_k$.

## Theorems and results
- **Two subspaces.** TFAE: (1) $U+V$ is direct; (2) every $w\in U+V$ is uniquely $w=u+v$; (3) $U\cap V=\{0\}$. *Idea:* (1)$\Rightarrow$(2) subtract two representations to get a zero representation; (2)$\Rightarrow$(3) write $0=x+(-x)$ for $x\in U\cap V$; (3)$\Rightarrow$(1) if $u=-v$ then $u\in U\cap V$.
- **Finitely many subspaces** ($W$ finite-dimensional, $\mathcal B_i$ a basis of $U_i$). TFAE: (1) the zero vector has a unique representation; (2) every vector of $U_1+\cdots+U_k$ is uniquely represented; (3) $\mathcal B_1\cup\cdots\cup\mathcal B_k$ is linearly independent. (Proof of (1)$\Leftrightarrow$(2) left as exercise.)
- **Dimension criterion.** TFAE: (1) direct sum; (2) $\mathcal B_1\cup\cdots\cup\mathcal B_k$ is a basis of $W_1\oplus\cdots\oplus W_k$; (3) $\dim(W_1+\cdots+W_k)=\dim W_1+\cdots+\dim W_k$. *Idea:* (1)$\Rightarrow$(2) spanning by grouping, independence from uniqueness of zero; (2)$\Rightarrow$(3) count elements; (3)$\Rightarrow$(1) the union spans, equal dimension makes it a basis, so the zero representation is unique.
- **Pairwise is not enough.** Pairwise direct sums do not imply a direct sum of all the subspaces.

## Techniques / procedures
1. To show $U+V$ is direct: take $x\in U\cap V$, write $0=x+(-x)$, conclude $x=0$, so $U\cap V=\{0\}$.
2. To show $W=U+V$: take arbitrary $w\in W$ and exhibit $u\in U$, $v\in V$ with $w=u+v$.
3. Even/odd split: $f_e(x)=\dfrac{f(x)+f(-x)}{2}$, $f_o(x)=\dfrac{f(x)-f(-x)}{2}$; check $f_e$ is even, $f_o$ is odd, and $f=f_e+f_o$.
4. For three or more subspaces, test the zero vector against all of them simultaneously; pairwise checks are not sufficient.
5. In finite dimension, compare $\dim(W_1+\cdots+W_k)$ with $\sum\dim W_i$.

## Worked examples in the notes
- $U=V=\operatorname{span}\{(1,0)\}\subseteq\mathbb R^2$ $\to$ $(1,0)=1(1,0)+0(1,0)$ and a second split with $u=[\text{unclear in scan}]\,(1,0)$, $v=3(1,0)$ $\to$ two representations, so not direct.
- $W_1=\operatorname{span}\{e_1,e_2\}$ (scan reads "$e_s,e_p$") and $W_2=\operatorname{span}\{e_3\}$ in $\mathbb R^3$ $\to$ $e_3\notin W_1$ $\to$ $\mathbb R^3=W_1\oplus W_2$.
- $\operatorname{span}\{(1,0)\},\ \operatorname{span}\{(0,1)\},\ \operatorname{span}\{(1,1)\}$ in $\mathbb R^2$ $\to$ $0=1(1,0)+1(0,1)+(-1)(1,1)$ with nonzero coefficients $\to$ pairwise direct, but not a direct sum.
- Even and odd functions on $\mathbb R$ $\to$ $f=f_e+f_o$ by the formulas above; if $g\in E\cap O$ then $2g(x)=0$ $\to$ $\mathbb R^{\mathbb R}=E\oplus O$.
- $M_n(\mathbb R)=S\oplus K$ (symmetric and skew-symmetric) $\to$ suggested exercise only; hint $\tfrac12(A+A^T)$ and $\tfrac12(A-A^T)$.

## Common pitfalls
- $U\cap V=\{0\}$ does not mean vectors chosen from $U$ and $V$ are automatically linearly independent; independence is a property of a set of vectors.
- Representations $w=u+v$ in $U+V$ need not be unique in general.
- Pairwise directness does not guarantee global directness; the zero vector must have a unique representation using all subspaces at once.
