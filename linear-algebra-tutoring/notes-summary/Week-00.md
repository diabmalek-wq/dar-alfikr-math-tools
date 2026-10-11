# Week 0: A Review of Matrices and Functions: Notations and Proof Techniques

## Big idea
Three standard vector spaces, $\mathbb{F}^n$, $M_{n\times k}(\mathbb{F})$ and $\mathcal{F}(\mathbb{F})$, are each defined by coordinatewise, entrywise or pointwise addition, scalar multiplication and equality. Proofs about them fix one generic coordinate, entry or input, so the argument covers every index at once.

## Definitions
- $\mathbb{F}^n$: $\{(x_1,\dots,x_n): x_i\in\mathbb{F}\}$; $x+y:=(x_1+y_1,\dots,x_n+y_n)$; $cx:=(cx_1,\dots,cx_n)$; $x=y$ iff $x_i=y_i$ for all $i$.
- $M_{n\times k}(\mathbb{F})$: $n\times k$ matrices with entries in $\mathbb{F}$; $(A+B)_{ij}:=A_{ij}+B_{ij}$; $(cA)_{ij}:=cA_{ij}$; $A=B$ iff the dimensions agree and $A_{ij}=B_{ij}$ for all $i,j$.
- Transpose: for $A\in M_{n\times k}(\mathbb{F})$, $A^T\in M_{k\times n}(\mathbb{F})$ with $(A^T)_{ij}:=A_{ji}$.
- $\mathcal{F}(\mathbb{F})=\{f:\mathbb{F}\to\mathbb{F}\}$; $(f+g)(x):=f(x)+g(x)$; $(cf)(x):=c\,f(x)$; $f=g$ iff $f(x)=g(x)$ for all $x\in\mathbb{F}$.
- Composition: $(f\circ g)(x):=f(g(x))$.

## Theorems and results
- For $x,y\in\mathbb{F}^n$ and $c,d\in\mathbb{F}$: $c(x+y)=cx+cy$ and $(c+d)x=cx+dx$. Proof idea: compare the $i$th entries and reduce to distributivity in $\mathbb{F}$.
- The same two identities hold in $M_{n\times k}(\mathbb{F})$ (compare entries $(i,j)$) and in $\mathcal{F}(\mathbb{F})$ (compare values at $x$).
- $(A+B)^T=A^T+B^T$ for $A,B\in M_{n\times k}(\mathbb{F})$. Proof idea: $(A+B)^T_{ij}=A_{ji}+B_{ji}$, which is the $(i,j)$ entry of $A^T+B^T$.
- $(f+g)\circ h=f\circ h+g\circ h$. Proof idea: evaluate both sides at an arbitrary $x$.

## Techniques / procedures
1. Vector or matrix equality: check that dimensions match, then compare every coordinate or entry.
2. Function equality: fix an arbitrary input $x$ and show the outputs agree.
3. Generic element: fix an arbitrary index $i$ (or $i,j$, or $x$), prove the identity for that one entry, and conclude for all.
4. Transpose: swap row and column indices.

## Worked examples in the notes
- $x=(1,0,-2)$, $c=3$, $y=\left(\tfrac13,0,-\tfrac23\right)$ $\to$ check $(cy)_i=c\,y_i=x_i$ for each $i$ $\to$ $x=cy$.
- $x=(1,2,3)$, $z=(1,2)$ $\to$ dimensions differ $\to$ $x+z$ is not defined.
- $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$, $B=\begin{pmatrix}5&6\\7&8\end{pmatrix}$ $\to$ add entrywise $\to$ $A+B=\begin{pmatrix}6&8\\10&12\end{pmatrix}$.
- $A=\begin{pmatrix}1&-2&0\\3&4&5\end{pmatrix}$ $\to$ $(A^T)_{ij}=A_{ji}$ $\to$ $A^T=\begin{pmatrix}1&3\\-2&4\\0&5\end{pmatrix}$.
- $A=\begin{pmatrix}1&2&3\\4&5&6\end{pmatrix}$, $B=\begin{pmatrix}1&0\\-1&2\\3&1\end{pmatrix}$ $\to$ $A^T+B$ is $3\times2$ and defined $\to$ $(A^T+B)^T=\begin{pmatrix}2&1&6\\4&7&7\end{pmatrix}$.
- $f(x)=2x$, $g(x)=x$, $c=2$ $\to$ $(cg)(x)=2x=f(x)$ for all $x$ $\to$ $f=cg$.

## Common pitfalls
- Addition is defined only for objects of the same dimension: $x+z$ with $x\in\mathbb{F}^3$, $z\in\mathbb{F}^2$, and $A+C$ with $A$ of size $2\times2$ and $C$ of size $2\times3$, are undefined.
- $A^T+B^T$ is undefined when $A^T$ is $3\times2$ and $B^T$ is $2\times3$ (notes' example), even though $A+B^T$ is defined.
- Agreeing at one input does not make two functions equal; equality requires $f(x)=g(x)$ for all $x$.
