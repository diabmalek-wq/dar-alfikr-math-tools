# Week 4: Bases and Dimension

## Big idea
A basis is a linearly independent spanning set, and all finite bases of a space have the same size, so $\dim(V)$ is well defined. Spanning sets can therefore be shrunk to bases, and independent sets can be extended to bases.

## Definitions
- Spanning set: $S\subseteq V$ with $V=\operatorname{span}(S)$.
- Basis: $S\subseteq V$ that is linearly independent and spans $V$.
- Finite-dimensional: $V$ admits a finite basis; $\dim(V)$ is the number of elements in any basis.
- Proper subspace: a subspace $S$ with $S\neq V$.
- Standard basis of $\mathbb{R}^n$ or $\mathbb{C}^n$: $\{e_1,\dots,e_n\}$, where $e_i$ has $1$ in position $i$ and $0$ elsewhere.

## Theorems and results
- $S$ is a basis of $V$ iff every vector of $V$ has a unique representation in $\operatorname{span}(S)$. Proof: spanning gives existence and independence gives uniqueness, and conversely.
- Extension lemma: for $S$ linearly independent and $x\notin S$, $S\cup\{x\}$ is linearly independent iff $x\notin\operatorname{span}(S)$. Forward direction by contradiction; backward direction by solving for $x$.
- If $V$ has a finite spanning set $T$ and $S$ is a finite independent subset, a finite basis $S'\supseteq S$ exists. Proof idea: add each $y\in T$ that is not in the span of the current set.
- Replacement result: if $T=\{y_1,\dots,y_n\}$ spans $V$ and $S=\{x_1,\dots,x_k\}$ is independent, the notes print "$n<k$" [unclear in scan]. The proof (writing each $x_i$ in terms of $T$, then a homogeneous system with more unknowns than equations) supports $k\leq n$.
- Any two finite bases of $V$ have the same number of elements.
- If $\dim(V)=n$ and $S$ is independent with $|S|=n$, then $S$ is a basis. Proof by contradiction via the extension lemma.
- Suggested exercise: for finite-dimensional $V$ and a proper subspace $S$, $\dim(S)<\dim(V)$.

## Techniques / procedures
1. To show $S$ is a basis: (i) solve $\sum c_iv_i=0$ and find only the trivial solution; (ii) solve $v=\sum a_iv_i$ for arbitrary $v$.
2. For $\mathbb{R}^n$, write $v=\sum v_ie_i$ to show the standard basis spans.
3. To extend an independent set, go through a finite spanning set $T$, adding each $y_j\notin\operatorname{span}$ of the current set.
4. If an independent set has $\dim(V)$ elements, it is a basis.

## Worked examples in the notes
- Standard basis of $\mathbb{R}^n$ $\to$ check independence and $v=\sum v_ie_i$ $\to$ basis.
- $\{(1,1),(1,-1)\}$ spans $\mathbb{R}^2$ $\to$ solve $a+b=x$, $a-b=y$ $\to$ $(a,b)=\left(\tfrac{x+y}{2},\tfrac{x-y}{2}\right)$ [final expression garbled in scan; this is the solution of the system as written].
- $\{(1,1),(1,-1)\}$ is independent $\to$ $a+b=0$, $a-b=0$ $\to$ $a=b=0$ $\to$ basis of $\mathbb{R}^2$.
- $\{1,a,\dots,a^n\}$ $\to$ basis of $P_n(\mathbb{R})$ $\to$ $n+1$ elements, so $\dim=n+1$.
- $\{a^k: k\in\mathbb{N}\}$ $\to$ basis of $P(\mathbb{R})$ $\to$ infinite.
- $\mathcal{F}(\mathbb{R})$ $\to$ a basis exists only via the Axiom of Choice $\to$ no explicit basis.

## Common pitfalls
- The notes single out recalling and applying previously proved theorems as the step students most often struggle with.
- $\dim(V)$ is defined only for finite-dimensional spaces; $P(\mathbb{R})$ needs an infinite basis.
- The backward direction of the extension lemma needs a different argument from the forward direction.
