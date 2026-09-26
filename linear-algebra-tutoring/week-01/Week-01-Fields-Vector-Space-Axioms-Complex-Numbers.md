# Week 1 — Fields, Vector Space Axioms & Complex Numbers

**Session length:** 3 hours
**Source:** Kielstra, *MAT A22 Course Notes*, Week 1 (1A: Scalars and Fields; 1B: Vectors and Vector Spaces)

---

## Page 1 — Introduction, Key Facts & Definitions

### Why this matters

Algebra is about **definitions, theorems, proofs, and structure**. Every structure we study is built from a small list of **axioms** — basic rules used to describe how mathematical objects behave.

### Definition: Binary Operation

A **binary operation** is a function $\boxplus : X \times X \to X$ with two inputs and one output.

- Real addition $+ : \mathbb{R} \times \mathbb{R} \to \mathbb{R}$ is a binary operation.
- Real multiplication $\cdot : \mathbb{R} \times \mathbb{R} \to \mathbb{R}$ is a binary operation.

### Definition: Commutative and Associative

An operation $\boxplus : X \times X \to X$ is **commutative** if, for all $x, y \in X$:
$$x \boxplus y = y \boxplus x.$$

An operation $\boxplus : X \times X \to X$ is **associative** if, for all $x, y, z \in X$:
$$x \boxplus (y \boxplus z) = (x \boxplus y) \boxplus z.$$

**Non-commutative operators:** division $\left(\dfrac{2}{3} \neq \dfrac{3}{2}\right)$, subtraction $(2-3 \neq 3-2)$, exponents $(2^3 \neq 3^2)$.

**Non-associative operators:** subtraction $\big((1-2)-3 \neq 1-(2-3)\big)$, exponents $\big((2^3)^4 \neq 2^{(3^4)}\big)$.

### Definition: The Axioms of a Field

A **field** is a set $F$ together with two binary operations
$$\boxplus : F \times F \to F, \qquad \boxdot : F \times F \to F$$
called *addition* and *multiplication*, such that:

- **A1.** $\boxplus$ is associative.
- **A2.** $\boxplus$ is commutative.
- **A3.** There exists an additive identity $\hat{0} \in F$ and a multiplicative identity $1 \in F$ such that $\hat{0} \boxplus x = x$ and $1 \boxdot x = x$ for all $x \in F$.
- **A4.** For each $x \in F$ there is an additive inverse $x' \in F$ such that $x \boxplus x' = \hat{0}$.
- **A5.** $\boxdot$ is associative.
- **A6.** $\boxdot$ is commutative.
- **A7.** For each $x \in F$ except $\hat{0}$ there is a multiplicative inverse $x' \in F$ such that $x \boxdot x' = 1$.
- **A8.** Multiplication is distributive over addition: for all $a, b, c \in F$,
$$a \boxdot (b \boxplus c) = a \boxdot b \boxplus a \boxdot c.$$

*Their order, numbering, and names are important.* This course uses two fields: the **real numbers** $\mathbb{R}$ and the **complex numbers** $\mathbb{C}$.

### Definition: The Imaginary Number $i$

$$i = \sqrt{-1}.$$

$i$ is not a real number, but it plays a central role in mathematics.

### Definition: Complex Numbers

A complex number has the form
$$z = a + bi, \qquad a, b \in \mathbb{R},$$
where $a = \operatorname{Re}(z)$ is the *real part* and $b = \operatorname{Im}(z)$ is the *imaginary part*.

### Definition: Complex Addition and Multiplication

Let $z_1 = a+bi$ and $z_2 = c+di$. Then
$$z_1 + z_2 := (a+c) + (b+d)i, \qquad z_1 \times z_2 := (ac-bd) + (ad+bc)i,$$
where the operations inside the brackets are the standard real-number operations.

### Definition: Additive Inverse, Subtraction, Conjugate, Modulus, Division

- Additive inverse: $-z := (-a) + (-b)i$.
- Subtraction: $z_1 - z_2 := (a-c) + (b-d)i$.
- Multiplicative inverse ($a, b$ not both $0$):
$$z_1^{-1} := \left(\dfrac{a}{a^2+b^2}\right) + \left(\dfrac{-b}{a^2+b^2}\right)i.$$
- Complex conjugate: $\bar z := a - bi$.
- Modulus: $|z| = \sqrt{\operatorname{Re}(z)^2 + \operatorname{Im}(z)^2}$.
- Division: $\dfrac{z_1}{z_2} := z_1 \times (z_2)^{-1} = \dfrac{z_1 \bar z_2}{|z_2|^2}$.

### Definition: The Axioms of a Vector Space

A **vector space** is a set $V$ together with a field $F$ and two binary operations
$$\boxplus : V \times V \to V, \qquad \boxdot : F \times V \to V$$
called *vector addition* and *scalar multiplication*, such that:

- **A1.** $\boxplus$ is associative.
- **A2.** $\boxplus$ is commutative.
- **A3.** There exists $\vec 0 \in V$ (the **zero vector**) such that $\vec 0 \boxplus x = x$ for all $x \in V$.
- **A4.** For each $x \in V$ there is an additive inverse $x' \in V$ such that $x \boxplus x' = \vec 0$.
- **A5.** For all $x, y \in V$ and $c \in F$: $c \boxdot (x \boxplus y) = (c \boxdot x) \boxplus (c \boxdot y)$.
- **A6.** For all $x \in V$ and $c, d \in F$: $(c+d) \boxdot x = (c \boxdot x) \boxplus (d \boxdot x)$.
- **A7.** For all $x \in V$ and $c, d \in F$: $(cd) \boxdot x = c \boxdot (d \boxdot x)$.
- **A8.** For all $x \in V$: $1 \boxdot x = x$.

*(Axioms adapted from Little and Damiano, p. 7.)*

A **complex vector space** ($\mathbb{C}$-vector space) is a vector space over the field $\mathbb{C}$. A **real vector space** ($\mathbb{R}$-vector space) is a vector space over the field $\mathbb{R}$.

### Proof Techniques Introduced This Week

- **Direct proof:** prove a statement true or false using only established definitions, axioms, lemmas, or theorems — no extra assumptions.
- **Uniqueness proof:** assume two objects both have the desired property, then show they must be equal to each other.

---

## Pages 2–3 — Solved Examples

**Example 1 (Verify the additive inverse of a complex number).** Let $z = a+bi$. Show $z + (-z) = 0$ for all $z \in \mathbb{C}$.

$$z + (-z) = (a+bi) + (-a + (-b)i) = \big(a+(-a)\big) + \big(b+(-b)\big)i = 0 + 0i = 0. \qquad \blacksquare$$

**Example 2 (Verify the multiplicative inverse of a complex number).** Let $z_1 = a+bi$, with $a,b$ not both $0$. Show $z_1 \times z_1^{-1} = 1$.

$$
(a+bi)\left(\left(\frac{a}{a^2+b^2}\right)+\left(\frac{-b}{a^2+b^2}\right)i\right)
= \left(\frac{a^2+b^2}{a^2+b^2}\right) + \left(\frac{-ab+ab}{a^2+b^2}\right)i = 1 + 0i. \qquad \blacksquare
$$

**Example 3 (Uniqueness of the zero vector).** Show the zero vector $\vec 0 \in V$ (Axiom A3) is unique.

*Proof.* Suppose $\vec 0$ and $\vec 0\,'$ both satisfy A3. Then
$$
\vec 0\,' = \vec 0 \boxplus \vec 0\,' \quad (\text{A3 for } \vec 0, \text{ with } x = \vec 0\,')
= \vec 0\,' \boxplus \vec 0 \quad (\text{A2, commutativity})
= \vec 0 \quad (\text{A3 for } \vec 0\,', \text{ with } x = \vec 0).
$$
So $\vec 0 = \vec 0\,'$. $\blacksquare$

**Example 4 (A fact that seems obvious but needs proof).** If $\vec z \in V$, then $0\vec z = \vec 0$.

*Proof.*
$$
0\vec z = (0+0)\vec z = 0\vec z \boxplus 0\vec z \quad (\text{A6}).
$$
Add the additive inverse $(0\vec z)'$ to both sides:
$$
0\vec z \boxplus (0\vec z)' = \big(0\vec z \boxplus 0\vec z\big) \boxplus (0\vec z)'
\;\Rightarrow\; \vec 0 = 0\vec z \boxplus \big(0\vec z \boxplus (0\vec z)'\big) \quad (\text{A1, associativity})
$$
$$
= 0\vec z \boxplus \vec 0 = \vec 0 \boxplus 0\vec z \quad (\text{A2}) = 0\vec z \quad (\text{A3}).
$$
Hence $0\vec z = \vec 0$ in **any** vector space. $\blacksquare$

**Example 5 ($(-1)x$ is the additive inverse of $x$).** Let $x \in V$. Prove $(-1)x$ is an additive inverse of $x$.

$$
x \boxplus (-1)x = 1x \boxplus (-1)x \quad (\text{A8}) = \big(1+(-1)\big)x \quad (\text{A6}) = 0x = \vec 0 \quad (\text{Example 4}). \qquad \blacksquare
$$

---

## Pages 4–5 — Practice Problems (unsolved)

**Complex numbers**

1. Let $z_1 = 3 - 2i$ and $z_2 = -1 + 4i$. Compute $z_1 + z_2$, $z_1 - z_2$, and $z_1 \times z_2$.
2. Compute the modulus $|z|$ for $z = 5 - 12i$.
3. Find $z^{-1}$ for $z = 2 + 3i$, then verify $z \times z^{-1} = 1$.
4. Compute $\dfrac{2+i}{1-i}$ by rationalizing with the conjugate.
5. Find the complex conjugate of $z = -4 + 7i$ and confirm $z + \bar z$ is a real number.

**Fields**

6. State axioms A1–A8 for a field in your own words (without looking back at Page 1), then check your answer against the definition.
7. Explain, using an example, why subtraction is **not** a binary operation that makes $\mathbb{R}$ satisfy Axiom A2 (commutativity) on its own — i.e. why subtraction is not the "addition" operation of a field.
8. Is $(\mathbb{Z}, +, \times)$ (the integers with standard addition and multiplication) a field? Identify which axiom fails and explain why.

**Vector space axioms**

9. Let $x, y \in V$ and suppose $x \boxplus y = x$. Prove that $y = \vec 0$. (Hint: add the additive inverse of $x$ to both sides.)
10. Prove that the additive inverse of any $x \in V$ is unique. (Model your proof on the zero-vector uniqueness proof on Page 3.)
11. Let $x \in V$. Using the axioms only, prove that $-(-x) = x$.
12. A student claims: "Since $1 \boxdot x = x$ for all $x$ (A8), it must also be true that $2 \boxdot x = x \boxplus x$ for all $x$." Prove this claim using the axioms (do not just assert it).

---

## Answer Key & Misconception Notes (for tutor use — do not show student until after attempt)

| # | Answer | Common misconception |
|---|---|---|
| 1 | $z_1+z_2 = 2+2i$; $z_1-z_2 = 4-6i$; $z_1 \times z_2 = 5+14i$ | Students often forget $i^2 = -1$ when expanding the product, leaving a $bd i^2$ term uncombined. |
| 2 | $|z| = 13$ | Confusing modulus with $\lvert \operatorname{Re}(z) \rvert$ alone (i.e. forgetting the imaginary part). |
| 3 | $z^{-1} = \dfrac{2}{13} - \dfrac{3}{13}i$ | Sign error: using $+\dfrac{b}{a^2+b^2}$ instead of $-\dfrac{b}{a^2+b^2}$ in the inverse formula. |
| 4 | $\dfrac{2+i}{1-i} = \dfrac{(2+i)(1+i)}{(1-i)(1+i)} = \dfrac{1+3i}{2}= \dfrac12+\dfrac32 i$ | Forgetting to multiply *both* numerator and denominator by the conjugate. |
| 5 | $\bar z = -4-7i$; $z+\bar z = -8$ (real) | Thinking the conjugate flips the sign of $a$ as well as $b$. |
| 6 | — | Mixing up A3 (identity) with A4 (inverse), or forgetting A3 requires *both* an additive **and** multiplicative identity. |
| 7 | — | Believing "subtraction is fine because $2-3$ makes sense" — misses that the axiom requires commutativity for *all* pairs, not that the operation is merely defined. |
| 8 | Not a field — A7 fails (no multiplicative inverse for most integers, e.g. $2$) | Assuming closure alone is enough to be a field; forgetting inverses must also lie in the set. |
| 9 | $y = \vec 0$ | Trying to "cancel" $x$ from both sides informally instead of adding the inverse and citing A1/A2/A3/A4 explicitly. |
| 10 | Uniqueness proof mirrors zero-vector proof, swapping roles | Forgetting to use commutativity (A2) as the pivot step. |
| 11 | $-(-x) = x$ | Treating $-x$ as a new independent object rather than $(-1)x$ from Example 5, missing the axiomatic route entirely. |
| 12 | $2 \boxdot x = (1+1)\boxdot x = 1\boxdot x \boxplus 1 \boxdot x = x \boxplus x$ (uses A6, then A8) | Assuming $2x$ "obviously" means $x+x$ without justifying it from the axioms — the whole point of this unit is that nothing is obvious until proven. |
