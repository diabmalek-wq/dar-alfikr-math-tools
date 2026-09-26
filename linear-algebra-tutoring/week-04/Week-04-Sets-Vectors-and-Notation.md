# Week 4 — Sets, Vectors & Notation

**Session length:** 3 hours
**Source:** Siefken, *MAT223 Workbook*, Module 1 (Sets, Vectors & Notation)

---

## Page 1 — Introduction, Key Facts & Definitions

### Why this matters

Sets are the language every later definition in this course is written in — "the set of vectors satisfying this equation," "the set of solutions," "the set spanned by these vectors." Vectors, meanwhile, are the objects the whole course studies. This week builds the vocabulary (sets, set-builder notation, vector notation, linear combinations) that Module 2 (lines, planes, and *sets* of vectors — Week 5) leans on immediately, so get comfortable translating between English, pictures, and symbols.

### Definition: Set
*(Source subsection: Sets)*

A **set** is an unordered collection of distinct objects. We write a set with curly braces $\{$ and $\}$ and list the objects inside, e.g. $\{1, 2, 3\}$, read aloud as "the set containing the elements $1$, $2$, and $3$." Objects in a set are called **elements** (or, traditionally, **points**, even when they are not point-like). Sets may contain mixtures of objects, including other sets, e.g. $\{1, 2, a, \{-70, \infty\}, x\}$ is a perfectly valid set.

- $\in$ means "is an element of": $3 \in \{1,2,3\}$.
- $\notin$ means "is not an element of": $4 \notin \{1,2,3\}$.

The **empty set** is the set containing no elements, written $\varnothing$ or $\{\}$. Note that $\{\varnothing\}$ is **not** the empty set — it is the set containing the empty set as its one element.

### Definition: Subset, Superset & Set Equality
*(Source subsection: Operations on Sets)*

The set $B$ is a **subset** of the set $A$, written $B \subseteq A$, if for all $b \in B$ we also have $b \in A$. In this case $A$ is called a **superset** of $B$.

The sets $A$ and $B$ are **equal**, written $A = B$, if $A \subseteq B$ and $B \subseteq A$.

This double-inclusion definition of equality is the standard tool for proving two sets described differently are actually the same set: show each is a subset of the other.

### Definition: Set-builder Notation
*(Source subsection: Set-builder Notation)*

Listing every element of a set is a hassle, and impossible for infinite sets. If $X$ is a set, we define a subset
$$Y = \{a \in X : \text{some rule involving } a\},$$
read "$Y$ is the set of $a$ in $X$ such that some rule involving $a$ is true." If $X$ is understood from context, it may be omitted: $Y = \{a : \text{some rule involving } a\}$. The vertical bar "$\mid$" may be used in place of the colon: $Y = \{a \mid \text{some rule involving } a\}$.

### Definition: Unions & Intersections
*(Source subsection: Set-builder Notation)*

Let $X$ and $Y$ be sets.
$$\text{(union)} \quad X \cup Y = \{a : a \in X \text{ or } a \in Y\}, \qquad \text{(intersection)} \quad X \cap Y = \{a : a \in X \text{ and } a \in Y\}.$$

For example, if $A = \{1,2,3\}$ and $B = \{-1,0,1,2\}$, then $A \cap B = \{1,2\}$ and $A \cup B = \{-1,0,1,2,3\}$. Unions are associative among themselves, and intersections are associative among themselves, so $A \cup B \cup C$ and $A \cap B \cap C$ are unambiguous. **But** $(A \cup B) \cap C$ is generally **not** the same set as $A \cup (B \cap C)$ — parentheses matter once you mix $\cup$ and $\cap$.

### Fact: Common Named Sets
*(Source subsection: Set-builder Notation)*

$$\varnothing = \{\}, \qquad \mathbb{N} = \{0, 1, 2, 3, \dots\}, \qquad \mathbb{Z} = \{\dots, -2, -1, 0, 1, 2, \dots\}, \qquad \mathbb{Q} = \{\text{rational numbers}\}, \qquad \mathbb{R} = \{\text{real numbers}\}, \qquad \mathbb{R}^n = \{\text{vectors in } n\text{-dimensional Euclidean space}\}.$$

### Definition: Vectors & Scalars
*(Source subsection: Vectors & Scalars)*

A **scalar** (an ordinary number) models a relationship between quantities — a recipe might call for six times as much flour as sugar. A **vector**, in contrast, models a relationship between *points* — the store might be $2\text{km}$ East and $4\text{km}$ North of your house. A vector may be thought of as a **displacement**, with a magnitude and a direction. Given points $P = (1,1)$ and $Q = (3,2)$, the displacement from $P$ to $Q$ is written $\overrightarrow{PQ}$, with magnitude $\sqrt{5}$ (Pythagorean theorem) and direction given by the directed segment from $P$ to $Q$.

### Definition: Vector Notation
*(Source subsection: Vector Notation)*

Common ways to write a vector: $\overrightarrow{PQ}$ (between two named points), a bold letter $\mathbf{a}$, or an arrow over a letter $\vec{a}$. **This workbook (and this course) uses $\vec{a}$.** The notation $\lVert \vec{a} \rVert$ is the **magnitude** (also called the **norm** or **length**) of $\vec{a}$.

Graphically we draw vectors as directed line segments, but a vector itself has **no origin** — it is the displacement, not the picture. For points $A=(1,1)$, $B=(3,2)$, $X=(1,0)$, $Y=(3,1)$, define $\vec{a} = \overrightarrow{AB}$ and $\vec{x} = \overrightarrow{XY}$. As directed segments they sit in different places, but they have the same magnitude and direction, so $\vec{a} = \vec{x}$ even though $A \neq X$.

**Takeaway.** A vector is not the same as a line segment, and a vector by itself has no "origin."

### Fact: Vectors and Points Are Interchangeable
*(Source subsection: Vectors and Points)*

A point specifies an absolute position; a vector specifies a displacement. Given a point $P$, we associate it with the vector $\vec{p} = \overrightarrow{OP}$, where $O$ is the origin. Conversely, given a vector $\vec{v}$, we associate it with the point $V$ such that $\overrightarrow{OV} = \vec{v}$. This lets us move back and forth unambiguously between vectors and points, and from here on we treat them interchangeably.

### Definition: Zero Vector, Scalar Multiplication & Vector Addition
*(Source subsection: Vector Arithmetic)*

The **zero vector**, written $\vec{0}$, is the vector with no magnitude. It does not have a well-defined direction — never speak of "the direction of the zero vector."

**Scalar multiplication (intuitive definition).** For a vector $\vec{v}$ and a scalar $\alpha > 0$, the vector $\vec{w} = \alpha\vec{v}$ points in the same direction as $\vec{v}$ but with length scaled by $\alpha$, i.e. $\lVert \vec{w} \rVert = \alpha \lVert \vec{v} \rVert$. The vector $-\vec{v}$ has the same length as $\vec{v}$ but points in the exact opposite direction.

**Vector addition.** For vectors $\vec{u}$ and $\vec{v}$, the sum $\vec{w} = \vec{u} + \vec{v}$ is the displacement obtained by first displacing along $\vec{u}$, then along $\vec{v}$ (add **tip to tail**).

**Takeaway.** You add vectors tip to tail, and you scale vectors by changing their length.

### Fact: Laws of Vector Arithmetic
*(Source subsection: Vector Arithmetic)*

For vectors $\vec{u}, \vec{v}, \vec{w}$ and scalars $\alpha, \beta$:
$$(\vec{u}+\vec{v})+\vec{w} = \vec{u}+(\vec{v}+\vec{w}) \quad \text{(Associativity)} \qquad \vec{u}+\vec{v} = \vec{v}+\vec{u} \quad \text{(Commutativity)} \qquad \alpha(\vec{u}+\vec{v}) = \alpha\vec{u}+\alpha\vec{v} \quad \text{(Distributivity)}$$
$$(\alpha\beta)\vec{v} = \alpha(\beta\vec{v}) \quad \text{(Associativity II)} \qquad (\alpha+\beta)\vec{v} = \alpha\vec{v}+\beta\vec{v} \quad \text{(Distributivity II)}$$

These laws hold for vectors in flat (Euclidean) space, and from now on we treat them as the axioms of vector arithmetic.

### Definition: Linear Combination
*(Source subsection: Vector Arithmetic)*

A **linear combination** of vectors $\vec{v}_1, \vec{v}_2, \dots, \vec{v}_n$ is a vector
$$\vec{w} = \alpha_1 \vec{v}_1 + \alpha_2 \vec{v}_2 + \cdots + \alpha_n \vec{v}_n.$$
The scalars $\alpha_1, \alpha_2, \dots, \alpha_n$ are called the **coefficients** of the linear combination.

### Definition: Coordinates and the Standard Basis
*(Source subsection: Coordinates and the Standard Basis)*

In the standard $xy$-coordinate system for $\mathbb{R}^2$, the **standard basis vectors** $\vec{e}_1$ and $\vec{e}_2$ point one unit along the positive $x$-axis and positive $y$-axis, respectively. Every point/vector in $\mathbb{R}^2$ can be written **uniquely** as a linear combination of $\vec{e}_1, \vec{e}_2$: if $P$ has coordinates $(\alpha, \beta)$, then $\overrightarrow{OP} = \alpha\vec{e}_1 + \beta\vec{e}_2$.

**Takeaway.** Every vector in $\mathbb{R}^2$ can be written uniquely as a linear combination of the standard basis vectors.

For $\vec{w} = \alpha\vec{e}_1 + \beta\vec{e}_2$, the pair $(\alpha,\beta)$ is called the **standard coordinates** of $\vec{w}$. Equivalent notations for a vector's coordinates:

| Notation | Name |
|---|---|
| $(\alpha, \beta)$ | parentheses |
| $\langle \alpha, \beta \rangle$ | angle brackets |
| $\begin{bmatrix} \alpha & \beta \end{bmatrix}$ | row vector |
| $\begin{bmatrix} \alpha \\ \beta \end{bmatrix}$ | column vector |

We will often write $\vec{v} = \begin{bmatrix} \alpha \\ \beta \end{bmatrix}$ as shorthand for "$\vec{v} = \alpha\vec{e}_1 + \beta\vec{e}_2$."

### Fact: Vector Arithmetic in Coordinates
*(Source subsection: Solving Problems with Coordinates)*

Let $\vec{u} = \begin{bmatrix} a \\ b \end{bmatrix}$ and $\vec{v} = \begin{bmatrix} x \\ y \end{bmatrix}$. Then
$$\vec{u} = \vec{v} \iff a = x \text{ and } b = y, \qquad \vec{u}+\vec{v} = \begin{bmatrix} a+x \\ b+y \end{bmatrix}, \qquad t\vec{u} = \begin{bmatrix} ta \\ tb \end{bmatrix} \text{ for any scalar } t.$$
Coordinates turn questions about vectors into ordinary algebra questions — in particular, deciding whether $\vec{r}$ is a linear combination of $\vec{x}, \vec{y}$ reduces to solving a system of linear equations for the coefficients.

### Definition: Higher Dimensions
*(Source subsection: Higher Dimensions)*

We coordinatize three-dimensional space $\mathbb{R}^3$ with $x$, $y$, $z$ axes and standard basis $\vec{e}_1, \vec{e}_2, \vec{e}_3$ (one unit along each axis). In general, $\mathbb{R}^n$ denotes $n$-dimensional Euclidean space, with standard basis $\vec{e}_1, \vec{e}_2, \dots, \vec{e}_n$. Every vector in $\mathbb{R}^n$ can be written uniquely as a linear combination of the standard basis, and a coordinate representation of a vector in $\mathbb{R}^n$ is a list of $n$ scalars.

---

## Pages 2–3 — Solved Examples

**Example 1 (Set membership and subset notation).** For the set $S = \{1, 2, 3\}$, determine whether each statement is true: (a) $3 \in S$, (b) $4 \in S$, (c) $\{1,2\} \subseteq S$, (d) $1 \subseteq S$.

(a) True — $3$ is listed as an element of $S$.

(b) False — $4$ is not one of the listed elements, so $4 \notin S$.

(c) True — every element of $\{1,2\}$ (namely $1$ and $2$) is also an element of $S$, which is exactly the definition of $\subseteq$.

(d) False, as **stated**. The symbol $\subseteq$ relates two *sets*, but $1$ is an element, not a set. The correct comparison would be $1 \in S$ (true) or $\{1\} \subseteq S$ (true) — but "$1 \subseteq S$" is not a well-formed true statement about the number $1$ itself. $\blacksquare$

**Example 2 (Proving set equality by double inclusion).** Let $A$ be the set of numbers expressible as $2n$ for some whole number $n$, and let $B$ be the set of numbers expressible as $m+1$ where $m$ is an odd whole number. Show $A = B$.

*Proof.* We use the definition of set equality: show $A \subseteq B$ and $B \subseteq A$.

$(A \subseteq B)$: Let $x \in A$. Then $x = 2n$ for some whole number $n$. Rewrite:
$$x = 2n = 2(n-1) + 1 + 1 = m + 1, \qquad \text{where } m = 2(n-1)+1.$$
Since $m = 2(n-1)+1$ is, by definition, odd, we have $x = m+1$ with $m$ odd, so $x \in B$. This proves $A \subseteq B$.

$(B \subseteq A)$: Let $x \in B$. Then $x = m+1$ for some odd $m$. By the definition of oddness, $m = 2k+1$ for some whole number $k$. So
$$x = m+1 = (2k+1)+1 = 2k+2 = 2(k+1) = 2n, \qquad \text{where } n = k+1,$$
so $x \in A$. This proves $B \subseteq A$.

Since $A \subseteq B$ and $B \subseteq A$, by definition $A = B$. $\blacksquare$

**Example 3 (Writing set-builder notation).** Write, in set-builder notation, the subset $A \subseteq \mathbb{R}$ of real numbers larger than $\sqrt{2}$.

We need "the set of $x$ in $\mathbb{R}$ such that $x$ is larger than $\sqrt{2}$." Translating directly into the definition $Y = \{a \in X : \text{rule}\}$ with $X = \mathbb{R}$ and rule "$x > \sqrt{2}$":
$$A = \{x \in \mathbb{R} : x > \sqrt{2}\}. \qquad \blacksquare$$

**Example 4 (Unions and intersections).** Let $X = \{1,3,5,7\}$ and $Y = \{3,5,9\}$. Compute $X \cup Y$ and $X \cap Y$.

By definition, $X \cup Y$ collects every element that is in $X$ **or** $Y$ (each element listed once, even if it's in both):
$$X \cup Y = \{1,3,5,7,9\}.$$
By definition, $X \cap Y$ collects only the elements that are in $X$ **and** $Y$:
$$X \cap Y = \{3,5\}. \qquad \blacksquare$$

**Example 5 (Vector notation: combining and simplifying).** Write $\vec{v} = 5\vec{e}_1 - 2\vec{e}_2 - 3\vec{e}_1 + \vec{e}_2$ as a column vector.

First combine like terms in the linear combination — collect all $\vec{e}_1$ coefficients and all $\vec{e}_2$ coefficients separately, exactly as you would with $x$'s and $y$'s in ordinary algebra:
$$\vec{v} = (5-3)\vec{e}_1 + (-2+1)\vec{e}_2 = 2\vec{e}_1 - \vec{e}_2.$$
Now read off the coefficients of $\vec{e}_1$ and $\vec{e}_2$ as the top and bottom entries of the column vector:
$$\vec{v} = \begin{bmatrix} 2 \\ -1 \end{bmatrix}. \qquad \blacksquare$$

**Example 6 (Vector arithmetic in $\mathbb{R}^2$).** Let $\vec{u} = \begin{bmatrix} 2 \\ -1 \end{bmatrix}$ and $\vec{v} = \begin{bmatrix} 3 \\ 4 \end{bmatrix}$. Compute $2\vec{u} - \vec{v}$.

Scalar multiplication scales each coordinate; here $2\vec{u} = \begin{bmatrix} 2\cdot 2 \\ 2\cdot(-1) \end{bmatrix} = \begin{bmatrix} 4 \\ -2 \end{bmatrix}$. Subtracting $\vec{v}$ means adding $(-1)\vec{v} = \begin{bmatrix} -3 \\ -4 \end{bmatrix}$, and vector addition is done entrywise:
$$2\vec{u} - \vec{v} = \begin{bmatrix} 4 \\ -2 \end{bmatrix} + \begin{bmatrix} -3 \\ -4 \end{bmatrix} = \begin{bmatrix} 4 + (-3) \\ -2 + (-4) \end{bmatrix} = \begin{bmatrix} 1 \\ -6 \end{bmatrix}. \qquad \blacksquare$$

**Example 7 (Vector arithmetic in $\mathbb{R}^3$).** Let $\vec{x}, \vec{y} \in \mathbb{R}^3$ be given by $\vec{x} = 2\vec{e}_1 - \vec{e}_3$ and $\vec{y} = 6\vec{e}_2 + 3\vec{e}_3$. Compute $\vec{z} = \vec{x} + 2\vec{y}$.

First write $\vec{x}$ and $\vec{y}$ as column vectors, filling in a $0$ for any missing basis direction — $\vec{x}$ has no $\vec{e}_2$ term, and $\vec{y}$ has no $\vec{e}_1$ term:
$$\vec{x} = \begin{bmatrix} 2 \\ 0 \\ -1 \end{bmatrix}, \qquad \vec{y} = \begin{bmatrix} 0 \\ 6 \\ 3 \end{bmatrix}.$$
Now scale $\vec{y}$ by $2$ (multiply every entry by $2$), then add entrywise to $\vec{x}$:
$$\vec{z} = \vec{x} + 2\vec{y} = \begin{bmatrix} 2 \\ 0 \\ -1 \end{bmatrix} + \begin{bmatrix} 0 \\ 12 \\ 6 \end{bmatrix} = \begin{bmatrix} 2 \\ 12 \\ 5 \end{bmatrix} = 2\vec{e}_1 + 12\vec{e}_2 + 5\vec{e}_3. \qquad \blacksquare$$

**Example 8 (Deciding if a vector is a linear combination, via a system of equations).** Let $\vec{x} = \vec{e}_1 - \vec{e}_2$, $\vec{y} = 3\vec{e}_1 - \vec{e}_2$, and $\vec{r} = 2\vec{e}_1 + 2\vec{e}_2$. Is $\vec{r}$ a linear combination of $\vec{x}$ and $\vec{y}$?

By definition, $\vec{r}$ is a linear combination of $\vec{x}$ and $\vec{y}$ if there exist scalars $a$ and $b$ such that $\vec{r} = a\vec{x} + b\vec{y}$. Rewrite everything in coordinates:
$$\begin{bmatrix} 2 \\ 2 \end{bmatrix} = a\begin{bmatrix} 1 \\ -1 \end{bmatrix} + b\begin{bmatrix} 3 \\ -1 \end{bmatrix} = \begin{bmatrix} a + 3b \\ -a - b \end{bmatrix}.$$
This vector equation is only true if **both** coordinates match, giving a system of linear equations in the unknown coefficients $a, b$:
$$\begin{cases} a + 3b = 2 \\ -a - b = 2 \end{cases}$$
Add the two equations to eliminate $a$: $2b = 4$, so $b = 2$. Substitute back into the first equation: $a + 3(2) = 2 \Rightarrow a = -4$. Check in the second equation: $-(-4) - 2 = 4 - 2 = 2$. ✓. Since a solution exists ($a=-4$, $b=2$), $\vec{r}$ **is** a linear combination of $\vec{x}$ and $\vec{y}$:
$$\vec{r} = -4\vec{x} + 2\vec{y}. \qquad \blacksquare$$

This last technique — translating "is $\vec{r}$ a linear combination of these vectors?" into a system of linear equations and solving for the coefficients — is exactly what Module 2 (Week 5) builds on to describe lines, planes, and spans.

---

## Pages 4–5 — Practice Problems (unsolved)

**Sets & Set Notation**

1. Let $S = \{2, 4, 6, 8\}$. Determine whether each statement is true or false: (a) $6 \in S$, (b) $5 \in S$, (c) $\{2,4\} \subseteq S$, (d) $8 \subseteq S$.
2. Let $A$ be the set of numbers expressible as $3n$ for some whole number $n$, and let $B$ be the set of numbers expressible as $3m+3$ for some whole number $m$. Prove $A = B$ using the double-inclusion definition of set equality.
3. List the elements of $\{x \in \mathbb{Z} : -2 \leq x < 3\}$.

**Set-Builder Notation**

4. Write, in set-builder notation, the subset $B \subseteq \mathbb{R}$ of real numbers less than $-5$.
5. Write, in set-builder notation, the subset $C \subseteq \mathbb{R}^2$ of vectors whose second coordinate is three times the first coordinate.

**Unions & Intersections**

6. Let $X = \{1,2,3,4\}$, $Y = \{3,4,5,6\}$, $Z = \{5,6,7\}$. Compute (a) $X \cup Y$, (b) $X \cap Y$, (c) $X \cup Y \cup Z$, (d) $X \cap Y \cap Z$.
7. Is the following statement true for all sets $A, B$? "If $A \subseteq B$, then $A \cap B = A$." Prove it, or give a counterexample.
8. Is the following statement true for all sets $A, B, C$? "If $C \subseteq A \cup B$, then $C \subseteq A$." Prove it, or give a counterexample.

**Vector Notation**

9. Write $\vec{v} = 5\vec{e}_1 - 3\vec{e}_3 + 2\vec{e}_2 - 4\vec{e}_1 + \vec{e}_3 \in \mathbb{R}^3$ as a column vector.
10. Write $\begin{bmatrix} -3 \\ 4 \\ 2 \end{bmatrix}$ as a linear combination of $\vec{e}_1, \vec{e}_2, \vec{e}_3$.

**Vector Arithmetic**

11. Let $\vec{u} = \begin{bmatrix} 3 \\ -2 \end{bmatrix}$ and $\vec{v} = \begin{bmatrix} -1 \\ 5 \end{bmatrix}$. Compute $\vec{u} + \vec{v}$, $\vec{u} - \vec{v}$, and $3\vec{u} - 2\vec{v}$.
12. Let $\vec{x} = 3\vec{e}_1 - 2\vec{e}_2 + \vec{e}_3$ and $\vec{y} = -\vec{e}_1 + 4\vec{e}_2 + 2\vec{e}_3$ in $\mathbb{R}^3$. Compute $\vec{z} = 2\vec{x} - \vec{y}$.

**Linear Combinations & Set-Builder Descriptions of Vectors**

13. (a) Is $\begin{bmatrix} 6 \\ -9 \end{bmatrix}$ in the set $\left\{ \vec{v} \in \mathbb{R}^2 : \vec{v} = k\begin{bmatrix} 2 \\ -3 \end{bmatrix} \text{ for some } k \in \mathbb{R} \right\}$? If so, find $k$.
    (b) Let $\vec{v}_1 = \begin{bmatrix} 2 \\ 1 \end{bmatrix}$ and $\vec{v}_2 = \begin{bmatrix} 1 \\ 3 \end{bmatrix}$. Is $\begin{bmatrix} 7 \\ 5 \end{bmatrix}$ a linear combination of $\vec{v}_1$ and $\vec{v}_2$? If so, find the coefficients by setting up and solving a system of linear equations.

---

## Answer Key & Misconception Notes (for tutor use — do not show student until after attempt)

| # | Answer | Common misconception |
|---|---|---|
| 1 | (a) True; (b) False; (c) True; (d) False (as stated — $8$ is an element, not a set, so "$8 \subseteq S$" is not well-formed; the true statement is $8 \in S$ or $\{8\} \subseteq S$) | Confusing $\in$ (element-of) with $\subseteq$ (subset-of), especially treating a single number as automatically "a subset" of the set it belongs to without wrapping it in braces. |
| 2 | $A = B$; proof mirrors the module's own $A \subseteq B$ / $B \subseteq A$ structure (for $A \subseteq B$: $x=3n=3(n-1)+3=3m+3$ with $m=n-1$; for $B \subseteq A$: $x=3m+3=3(m+1)=3n$ with $n=m+1$) | Trying to prove $A=B$ by testing a few numeric examples instead of proving both inclusions in general; or proving only one direction ($A \subseteq B$) and stopping, forgetting equality requires *both* inclusions. |
| 3 | $\{-2, -1, 0, 1, 2\}$ | Including $3$ because the inequality "looks like" it should be inclusive on both ends — missing that $<$ (strict) excludes $3$ while $\leq$ (non-strict) includes $-2$. |
| 4 | $B = \{x \in \mathbb{R} : x < -5\}$ | Writing $x > -5$ (flipping the inequality direction) or using $\leq$ instead of $<$ when the problem says "less than," not "less than or equal to." |
| 5 | $C = \{\vec{v} \in \mathbb{R}^2 : \vec{v} = \begin{bmatrix} x \\ y \end{bmatrix}, \ y = 3x\}$ (equivalently $\{\vec{v} \in \mathbb{R}^2 : \vec{v} = t\begin{bmatrix}1\\3\end{bmatrix} \text{ for some } t \in \mathbb{R}\}$) | Writing the relation backwards as "first coordinate is three times the second" ($x = 3y$), swapping which coordinate is being described. |
| 6 | (a) $\{1,2,3,4,5,6\}$; (b) $\{3,4\}$; (c) $\{1,2,3,4,5,6,7\}$; (d) $\varnothing$ (no element is in all three) | Assuming $X \cap Y \cap Z$ must be nonempty just because $X\cap Y$ and $Y \cap Z$ are each nonempty; forgetting the empty set is a valid, correct answer. |
| 7 | True. If $A \subseteq B$, every element of $A$ is in $B$, so every element of $A$ is in both $A$ and $B$, meaning $A \subseteq A \cap B$; also $A \cap B \subseteq A$ always. So $A \cap B = A$. | Trying to "verify" the claim with one specific example instead of proving it holds for *all* sets $A, B$ with $A \subseteq B$; or confusing this with the (false) claim that $A \cap B = B$ when $A \subseteq B$. |
| 8 | False. Counterexample: $A = \{1\}$, $B = \{2\}$, $C = \{2\} = B$. Then $C \subseteq A \cup B = \{1,2\}$, but $C \not\subseteq A$. | Assuming any subset of a union must be a subset of "the first" set listed; not realizing a single counterexample is enough to disprove a for-all statement. |
| 9 | $\begin{bmatrix} 1 \\ 2 \\ -2 \end{bmatrix}$ | Forgetting to combine the two $\vec{e}_1$ terms ($5\vec{e}_1$ and $-4\vec{e}_1$) before reading off coordinates, e.g. writing $5$ instead of $1$ in the top entry. |
| 10 | $-3\vec{e}_1 + 4\vec{e}_2 + 2\vec{e}_3$ | Mismatching which entry goes with which basis vector, e.g. writing $-3\vec{e}_2$ instead of $-3\vec{e}_1$ (reversing the order of $\vec{e}_1, \vec{e}_2, \vec{e}_3$). |
| 11 | $\vec{u}+\vec{v} = \begin{bmatrix}2\\3\end{bmatrix}$; $\vec{u}-\vec{v} = \begin{bmatrix}4\\-7\end{bmatrix}$; $3\vec{u}-2\vec{v} = \begin{bmatrix}11\\-16\end{bmatrix}$ | Scaling only one entry of the vector when computing $3\vec{u}$ or $2\vec{v}$ (e.g. multiplying the top entry by $3$ but leaving the bottom entry unscaled). |
| 12 | $\vec{z} = \begin{bmatrix}7\\-8\\0\end{bmatrix} = 7\vec{e}_1 - 8\vec{e}_2$ | Sign error distributing the $-1$ across $\vec{y}$'s entries when computing $2\vec{x}-\vec{y}$, e.g. computing $2(1)$ or forgetting to flip the sign of one of $\vec{y}$'s coordinates. |
| 13 | (a) Yes, $k=3$ (since $3\begin{bmatrix}2\\-3\end{bmatrix} = \begin{bmatrix}6\\-9\end{bmatrix}$); (b) Yes: solving $\begin{cases}2a+b=7\\a+3b=5\end{cases}$ gives $a=\dfrac{16}{5}$, $b=\dfrac{3}{5}$ | (a) Guessing $k$ by eyeballing one coordinate only, then not checking it against the second coordinate. (b) Setting up the system with rows and columns swapped (mixing up which equation comes from the first vs. second coordinate), or stopping after finding $a$ without substituting back to check both original equations. |
