# Week 8: Injectivity, Surjectivity and Composition

## Big idea
For linear maps, injectivity is equivalent to a trivial kernel, and dimension counting (rank-nullity) strongly constrains injectivity and surjectivity. Composition of linear maps is linear, and its matrix is the product of the matrices.

## Definitions
- **Injective**: $f(v_1)=f(v_2)$ implies $v_1=v_2$.
- **Surjective**: for every $w\in W$ there is $v\in V$ with $f(v)=w$.
- **Sum and scaling of maps**: $(S+T)(v)=S(v)+T(v)$ and $(aS)(v)=a\,S(v)$.
- **Composition**: $(S\circ T)(x)=S(T(x))$, defined when $\operatorname{image}(T)\subseteq\operatorname{domain}(S)$.
- **Matrix product**: $p_{ij}=\sum_{N} t_{iN}\,s_{Nj}$ for $[T]\,[S]$.

## Theorems and results
- **Finite sets.** For $f:D\to R$ with $D,R$ finite: (1) $|D|<|R|$ implies $f$ is not surjective; (2) $|D|>|R|$ implies $f$ is not injective; (3) if $|D|=|R|$, $f$ is injective iff surjective.
- **Injectivity.** For linear $T$, TFAE: $T$ injective; $\ker T=\{0\}$; $\dim\ker T=0$. *Idea:* $T(u)=T(v)$ gives $T(u-v)=0$; conversely $T(v)=0=T(0)$ forces $v=0$.
- **Surjectivity** ($W$ finite-dimensional). For linear $T$, TFAE: $T$ surjective; $\operatorname{image}(T)=W$; $\dim\operatorname{image}(T)=\dim W$. *Idea:* a subspace of $W$ with dimension $\dim W$ equals $W$.
- If $\dim W<\dim V$ (finite), then $T$ is not injective. *Idea:* rank-nullity gives $\dim\ker T\ge \dim V-\dim W>0$.
- If $\dim V<\dim W$ (finite), then $T$ is not surjective. *Idea:* $\dim\operatorname{image}T\le\dim V<\dim W$.
- If $\dim V=\dim W=n<\infty$, then $T$ is injective iff surjective. *Idea:* rank-nullity gives $\dim\operatorname{image}T=n-\dim\ker T$.
- For linear $S:U\to V$ and $T:V\to W$: $\ker S\subseteq\ker(TS)$ and $\operatorname{image}(TS)\subseteq\operatorname{image}(T)$.
- Composition of linear maps is linear; composition is associative; composition and addition distribute (partly proved in notes, rest left as exercise).
- **Matrix of a composition**: $[TS]^\gamma_\alpha=[T]^\gamma_\beta\,[S]^\beta_\alpha$. *Idea:* compare the $(i,j)$ entries using uniqueness of coordinates and rearranging sums.
- Matrix multiplication is associative and distributive (proved entrywise).

## Techniques / procedures
1. Injectivity: row-reduce $[T]\,v=0$; if the only solution is trivial (a pivot in every column), $T$ is injective.
2. Surjectivity: find pivot columns of $[T]$ to get $\operatorname{image}(T)$, or compare $\dim\operatorname{image}(T)$ with $\dim W$.
3. Before computing, use dimensions: $\dim V>\dim W$ rules out injectivity; $\dim V<\dim W$ rules out surjectivity.
4. Matrix of $T\circ S$: multiply $[T]^\gamma_\beta$ by $[S]^\beta_\alpha$, row by column.
5. Entrywise proofs: compare $(i,j)$ entries using the definition of matrix product.

## Worked examples in the notes
- $T(u_1,u_2)=(u_1,\ 2u_1+u_2,\ -u_1+3u_2)$ $\to$ columns $(1,2,-1)^T$ and $(0,1,3)^T$ $\to$ $[T]v=0$ reduces to $u_1=u_2=0$ $\to$ injective.
- $D:P_3(\mathbb R)\to P_2(\mathbb R)$, $D(p)=p'$ $\to$ $[D]$ has pivot columns 2, 3, 4 $\to$ image basis $\{1,2x,3x^2\}$, dimension $3=\dim P_2(\mathbb R)$ $\to$ surjective (kernel dimension 1 by rank-nullity).
- No injective linear map $\mathbb R^{10}\to\mathbb R^2$ $\to$ $\dim V>\dim W$; no surjective linear map $\mathbb R^2\to\mathbb R^{10}$ $\to$ $\dim V<\dim W$.
- $\begin{pmatrix}1&-1\\0&1\end{pmatrix}\begin{pmatrix}3&0\\1&4\end{pmatrix}=\begin{pmatrix}2&-4\\1&4\end{pmatrix}$ $\to$ row-by-column $\to$ used to argue non-commutativity (the reverse product is a suggested exercise; scan partly unclear).

## Common pitfalls
- For a composition $TS$ to be defined, the codomain of the inner map must match the domain of the outer map.
- The "injective iff surjective" equivalence needs $\dim V=\dim W$; the notes stress this.
- Finiteness matters: in infinite dimensions a space can have a proper subspace of the same dimension, so the dimension test for surjectivity fails.
- Matrix multiplication is not commutative (suggested exercise using the example above).
