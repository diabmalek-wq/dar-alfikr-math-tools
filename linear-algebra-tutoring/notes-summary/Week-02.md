# Week 2: Subspaces and Linear Combinations

## Big idea
A subspace is a subset of a vector space that is itself a vector space under the same operations, and closure under $cx+y$ tests this. Spans, linear combinations and linear independence describe subspaces and detect redundant vectors.

## Definitions
- Subspace: $W\subseteq V$ that is a vector space with the same $0$ and operations as $V$.
- Linear combination of $S\subseteq V$: $a_1v_1+\cdots+a_kv_k$ with $v_i\in S$, $a_i\in\mathbb{F}$.
- $\operatorname{span}(S)$: all linear combinations of elements of $S$; $\operatorname{span}(\varnothing)=\{0\}$.
- Sum of subsets: $A+B=\{a+b: a\in A,\ b\in B\}$.
- Linearly dependent (L.D.): some constants $a_1,\dots,a_k$, not all zero, satisfy $\sum a_iv_i=0$. Linearly independent (L.I.): not dependent.
- Redundant: $w\in S$ with $w\in\operatorname{span}(S\setminus\{w\})$.
- $\operatorname{col}(A)$, $\operatorname{row}(A)$: spans of the columns and rows of $A$.

## Theorems and results
- Closure characterization: a nonempty $W\subseteq V$ is a subspace iff $cx+y\in W$ for all $c\in\mathbb{F}$, $x,y\in W$. Proof idea: $0\in W$ follows from $(-1)x+x$, and $(-1)x\in W$ gives inverses.
- $\operatorname{span}(S)$ is a subspace of $V$ (case split on $S=\varnothing$).
- If $W_1,W_2$ are subspaces, so are $W_1\cap W_2$ and $W_1+W_2$.
- If $W_i=\operatorname{span}(S_i)$, then $W_1+W_2=\operatorname{span}(S_1\cup S_2)$.
- $S$ is linearly dependent iff $S$ contains a redundant vector. Proof idea: a relation with $a_n\neq0$ solves for $v_n$; conversely $w=\sum a_iw_i$ gives $(-1)w+\sum a_iw_i=0$.
- For $S=\{v_1,\dots,v_n\}$ the following are equivalent: (1) $S$ is L.I.; (2) $0\in\operatorname{span}(S)$ is represented uniquely; (3) every vector of $\operatorname{span}(S)$ is represented uniquely. Proof: $1\Rightarrow2\Rightarrow3\Rightarrow1$.

## Techniques / procedures
1. Subspace test: show $W\neq\varnothing$ (e.g., $0\in W$), then show $cx+y\in W$.
2. To show $W=\operatorname{span}(S)$: solve the constraints, write a generic element as free parameters times fixed vectors, and prove both inclusions.
3. Independence test: set $\sum a_iv_i=0$ and show only $a_i=0$ works.
4. Remove redundant vectors to shrink a spanning set without changing its span.
5. Case-by-case proof: split into cases covering all possibilities and prove each.

## Worked examples in the notes
- $\{(a,0):a\in\mathbb{R}\}$ $\to$ $c(a,0)+(b,0)=(ca+b,0)$ $\to$ subspace.
- Continuous functions in $\mathcal{F}(\mathbb{R})$ $\to$ $cf+g$ is continuous $\to$ subspace.
- $\{(x,y,z): x+y+z=0\}$ $\to$ substitute $x=-y-z$ $\to$ $y(-1,1,0)+z(-1,0,1)$ $\to$ span of $\{(-1,1,0),(-1,0,1)\}$.
- $\{(x,0)\}+\{(y,y)\}=\mathbb{R}^2$ $\to$ $(a,b)=(a-b,0)+(b,b)$ $\to$ both inclusions.
- $\{(1,2),(1,0),(0,1)\}$ $\to$ $(1,2)=(1,0)+2(0,1)$ $\to$ $(1,2)$ is redundant.
- $\{(1,2,3),(1,0,1),(2,2,4)\}$ $\to$ $(1,2,3)+(1,0,1)=(2,2,4)$ $\to$ dependent.
- $\{\sin^2x,\cos^2x,1\}$ $\to$ $\sin^2x+\cos^2x-1=0$ $\to$ dependent.
- $\{\sin x,\cos x\}$ $\to$ $x=0$ gives $b=0$; $x=\dfrac{\pi}{2}$ gives $a=0$ $\to$ independent.

## Common pitfalls
- A proof by cases must cover every case; examples where the statement holds are not a proof.
- Equality of sets needs both $A\subseteq B$ and $B\subseteq A$.
- The empty sum is $0$, so $\operatorname{span}(\varnothing)=\{0\}$, not $\varnothing$.
- A set is dependent if any finite subset of it is dependent.
