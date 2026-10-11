# Week 1: A Quick Tour of Number Systems, Fields and Vector Spaces

## Big idea
Algebraic structures are built from axioms; this week fixes the fields $\mathbb{R}$ and $\mathbb{C}$ and the eight axioms of a vector space over a field. Most later verifications reduce to the fact that the scalars form a field.

## Definitions
- Binary operation: a function $\boxplus: X\times X\to X$. Commutative: $x\boxplus y=y\boxplus x$. Associative: $x\boxplus(y\boxplus z)=(x\boxplus y)\boxplus z$.
- Field: a set $\mathbb{F}$ with addition $\boxplus$ and multiplication $\boxdot$ satisfying A1–A8: both operations associative and commutative; identities $\hat 0$ and $1$; additive inverses; multiplicative inverses for $x\neq\hat 0$; and $a\boxdot(b\boxplus c)=a\boxdot b\boxplus a\boxdot c$.
- Complex number: $z=a+bi$ with $a,b\in\mathbb{R}$, $i=\sqrt{-1}$; $\operatorname{Re}(z)=a$, $\operatorname{Im}(z)=b$.
- Conjugate: $\bar z:=a-bi$. Modulus: $|z|:=\sqrt{\operatorname{Re}(z)^2+\operatorname{Im}(z)^2}$.
- Complex operations: $(a+bi)+(c+di):=(a+c)+(b+d)i$; $(a+bi)(c+di):=(ac-bd)+(ad+bc)i$; $z_1-z_2:=(a-c)+(b-d)i$.
- Division: $\dfrac{z_1}{z_2}:=\dfrac{z_1\bar z_2}{|z_2|^2}$.
- Vector space: a set $V$ over a field $\mathbb{F}$, with $\boxplus:V\times V\to V$ and $\boxdot:\mathbb{F}\times V\to V$, satisfying A1–A8: $\boxplus$ associative and commutative; a zero vector $0$; additive inverses; $c\boxdot(x\boxplus y)=(c\boxdot x)\boxplus(c\boxdot y)$; $(c+d)\boxdot x=(c\boxdot x)\boxplus(d\boxdot x)$; $(cd)\boxdot x=c\boxdot(d\boxdot x)$; $1\boxdot x=x$.
- Examples: $\mathbb{R}^n$; $\mathcal{F}(\mathbb{R})=\{f:\mathbb{R}\to\mathbb{R}\}$; $M_{m\times n}(\mathbb{R})$; over a general field, $\mathcal{F}(\mathbb{F})$ and $M_{m\times n}(\mathbb{F})$.

## Theorems and results
- The zero vector is unique. Proof idea: $0'=0\boxplus0'=0'\boxplus0=0$.
- $0\vec z=\vec 0$ in every vector space. Proof idea: $0\vec z=(0+0)\vec z$, apply A6, then cancel.
- $(-1)\vec x$ is an additive inverse of $\vec x$. Proof: $\vec x\boxplus(-1)\vec x=(1+(-1))\vec x=0\vec x=\vec 0$.
- A nonzero $z=a+bi$ has $z^{-1}=\dfrac{a}{a^2+b^2}-\dfrac{b}{a^2+b^2}i$.
- $\mathbb{C}$ is a field (stated as an exercise).

## Techniques / procedures
1. Multiply complex numbers by expanding and using $i^2=-1$.
2. Divide $z_1$ by $z_2$: multiply top and bottom by $\bar z_2$, then divide by $|z_2|^2$.
3. To write $v$ as a linear combination, equate components to a linear system in the scalars and solve.
4. Verify a vector-space axiom coordinatewise, reducing each step to a field axiom.
5. Uniqueness proof: assume two objects have the property, then show they are equal.

## Worked examples in the notes
- $(a+bi)(c+di)$ $\to$ expand $\to$ $(ac-bd)+(ad+bc)i$.
- $z\times z^{-1}$ $\to$ multiply out $\to$ $1+0i$.
- $x=(1,2,3)+2\big((1,1,1)-(3,2,1)\big)$ $\to$ compute inside, scale, add $\to$ $(-3,0,3)$.
- Is $(-1,1)=a(1,2)+b(1,1)$? $\to$ $-1=a+b$, $1=2a+b$ $\to$ $(a,b)=(2,-3)$. (The printed check "$2(1,2)-2(1,1)$" equals $(0,2)$, not $(-1,1)$; the solved values do check.)
- $c\boxdot(f\boxplus g)=c\boxdot f\boxplus c\boxdot g$ in $\mathcal{F}(\mathbb{R})$ $\to$ compare at arbitrary $x$ $\to$ distributivity in $\mathbb{R}$ $\to$ equal.

## Common pitfalls
- Subtraction is neither commutative ($2-3\neq3-2$) nor associative ($(1-2)-3\neq1-(2-3)$).
- Division is not commutative ($\tfrac32\neq\tfrac23$); complex numbers are divided via $\bar z_2/|z_2|^2$.
- Exponents: $2^3\neq3^2$, and $(2^3)^4\neq2^{(3^4)}$ [bracketing unclear in scan].
