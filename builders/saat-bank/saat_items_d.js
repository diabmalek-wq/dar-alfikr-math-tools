// PART D of the simulated SAAT bank — written from the skill inventory of the
// Arabic teaching book in the project files (204 worked examples, no question
// sets of its own).
//
// WHAT CROSSED OVER AND WHAT DID NOT. The book supplied the SKILL and, where it
// had one, the TRICK the examiner uses on that skill. Nothing else. Every stem
// below is newly worded, every number set is new, every option list is built
// from the traps a student of ours actually falls into, and every answer is
// re-derived in verify_saat_d.py by a route that never reads the item's own
// reasoning. An example that only restates a definition produced no item; an
// example whose skill is already in parts A, B or C produced no item either.
//
// PLACEMENT. Each item names the session of the 45-week course it belongs to.
// The driver refuses a session that does not exist or that is not a teaching
// session, so nothing here can drift outside the plan.
//
// The book opens with a chapter on logic — truth tables, negation, the
// conditional and its converse, inverse and contrapositive, the biconditional
// and the syllogism. The 45-week plan has no session for it, so it has no items
// here. Counterexamples and always/sometimes/never DO have a home (session 89)
// and are written below.

module.exports = [
  // ============================================================ UNIT 1
  // ---------------------------------------------- session 3 · exponents & radicals
  {
    sig: "how-many-real-fourth-roots",
    code: "SAAT-M-ALG.33", ses: 3, lvl: 2,
    stem: "How many real fourth roots does 81 have, and what are they?",
    opts: [
      "Two: 3 and −3",
      "Four: 3, −3, 3i and −3i",
      "None, because the index is even",
      "One: 3"
    ],
    ans: 0,
    trick: "an EVEN index over a POSITIVE number gives two real roots, one positive and one negative — the radical sign alone names only the positive one, but the question asks for the roots, not for the sign",
    why: "3⁴ = 81 and (−3)⁴ = 81, and no other real number has fourth power 81.",
    traps: [
      "B: the two complex fourth roots exist, but they are not real.",
      "C: an even index refuses a NEGATIVE radicand; 81 is positive.",
      "D: only the principal root, which is what the symbol ⁴√81 means — but not what was asked.",
    ],
  },
  {
    sig: "principal-root-of-an-even-power",
    code: "SAAT-M-ALG.34", ses: 3, lvl: 3,
    stem: "Simplify the expression below, given that y may be any real number.",
    stemEq: "d_prin",
    opts: [
      { eq: "d_prin4" },
      { eq: "d_prin1" },
      { eq: "d_prin2" },
      { eq: "d_prin3" }
    ],
    ans: 1,
    trick: "the square root sign returns the NON-NEGATIVE root, and y² is already non-negative, so no absolute-value bars are needed here — they are needed only when the surviving power is odd",
    why: "√(16y⁴) = √((4y²)²) = 4y², and y² ≥ 0 for every real y.",
    traps: [
      "A: the index halved but the coefficient left alone.",
      "C: the ± belongs to the equation x² = 16y⁴, not to the radical.",
      "D: bars added out of habit; y² cannot be negative.",
    ],
  },
  {
    sig: "rationalise-a-single-term-denominator",
    code: "SAAT-M-ALG.35", ses: 3, lvl: 2,
    stem: "Write the expression below with no radical in the denominator.",
    stemEq: "d_rat1",
    opts: [
      { eq: "d_rat1c" },
      { eq: "d_rat1d" },
      { eq: "d_rat1a" },
      { eq: "d_rat1b" }
    ],
    ans: 2,
    trick: "multiply TOP AND BOTTOM by the same radical — the denominator becomes the number under it, here 5, and the 5 does not cancel with the numerator's 3",
    why: "3/√5 × √5/√5 = 3√5 ÷ 5.",
    traps: [
      "A: the 3 and the 5 cancelled, which they cannot — one is inside a product, the other a denominator.",
      "B: multiplied by √5 on the top only.",
      "D: the radical moved up but the denominator left as √5.",
    ],
  },
  {
    sig: "simplify-a-radical-with-a-square-factor",
    code: "SAAT-M-ALG.36", ses: 3, lvl: 3,
    stem: "Write the expression below in its simplest radical form, where x ≥ 0.",
    stemEq: "d_srad",
    opts: [
      { eq: "d_srad4" },
      { eq: "d_srad1" },
      { eq: "d_srad2" },
      { eq: "d_srad3" }
    ],
    ans: 3,
    trick: "split 50 into 25 × 2, not into 5 × 10 — you want the LARGEST perfect square inside, and x⁶ is a perfect square already because 6 is even",
    why: "√(50x⁶) = √25 · √2 · √(x⁶) = 5x³√2.",
    traps: [
      "A: x⁶ read as x² rather than x³.",
      "B: 50 left whole under the radical.",
      "C: the exponent halved but the 25 not taken out.",
    ],
  },

  // ---------------------------------------------- session 5 · expressions & operations
  {
    sig: "subtract-two-polynomials",
    code: "SAAT-M-ALG.37", ses: 5, lvl: 2,
    stem: "Simplify the expression below.",
    stemEq: "d_subp",
    opts: [
      { eq: "d_subp2" },
      { eq: "d_subp3" },
      { eq: "d_subp4" },
      { eq: "d_subp1" }
    ],
    ans: 0,
    trick: "the minus sign in front of the bracket changes EVERY sign inside it, the last term included — most of the marks lost here are lost on the constant",
    why: "(5x² − 3x + 4) − (2x² + 6x − 1) = 3x² − 9x + 5.",
    traps: [
      "B: the constant left as 4 − 1 = 3 with the sign of −1 missed.",
      "C: the x terms added instead of subtracted.",
      "D: only the first term inside the bracket had its sign changed.",
    ],
  },
  {
    sig: "degree-of-a-polynomial-in-two-variables",
    code: "SAAT-M-ALG.38", ses: 5, lvl: 2,
    stem: "What is the degree of the polynomial below?",
    stemEq: "d_deg",
    opts: [
      "5",
      "7",
      "9",
      "4"
    ],
    ans: 1,
    trick: "the degree of a TERM in two variables is the SUM of its exponents, and the degree of the polynomial is the largest of those sums — not the largest single exponent anywhere in it",
    why: "The terms have degrees 4 + 3 = 7, 5 and 2, so the degree is 7.",
    traps: [
      "A: the largest exponent on a single variable taken as the degree.",
      "C: the exponent of x from one term added to the exponent of y from another.",
      "D: only the exponent of x in the leading term read.",
    ],
  },
  {
    sig: "is-the-expression-a-polynomial",
    code: "SAAT-M-ALG.39", ses: 5, lvl: 2,
    stem: "Which of the expressions below is NOT a polynomial?",
    opts: [
      { eq: "d_poly1" },
      { eq: "d_poly2" },
      { eq: "d_poly3" },
      { eq: "d_poly4" }
    ],
    ans: 2,
    trick: "a polynomial allows only WHOLE-NUMBER exponents on the variable — a variable under a radical, or in a denominator, disqualifies the expression however tidy it looks",
    why: "√x is x^(1/2); an exponent of one half is not a whole number.",
    traps: [
      "A: a constant term is a perfectly good monomial of degree 0.",
      "B: a negative COEFFICIENT is allowed; a negative exponent is not.",
      "D: three terms and a large exponent, but every exponent is a whole number.",
    ],
  },
  {
    sig: "divide-a-polynomial-by-a-monomial",
    code: "SAAT-M-ALG.40", ses: 5, lvl: 3,
    stem: "Simplify the quotient below.",
    stemEq: "d_divm",
    opts: [
      { eq: "d_divm2" },
      { eq: "d_divm3" },
      { eq: "d_divm4" },
      { eq: "d_divm1" }
    ],
    ans: 3,
    trick: "EVERY term of the numerator is divided by the monomial, not just the first — and dividing powers subtracts exponents, so a term can lose its variable entirely",
    why: "(12x⁴y³ + 8x³y² − 4x²y) ÷ (4x²y) = 3x²y² + 2xy − 1.",
    traps: [
      "A: the last term divided into 0 instead of 1.",
      "B: only the first term divided.",
      "C: the exponents added instead of subtracted.",
    ],
  },

  // ---------------------------------------------- session 6 · factoring
  {
    sig: "product-that-gives-a-difference-of-cubes",
    code: "SAAT-M-ALG.41", ses: 6, lvl: 3,
    stem: "Expand and simplify the product below.",
    stemEq: "d_cube",
    opts: [
      { eq: "d_cube4" },
      { eq: "d_cube1" },
      { eq: "d_cube2" },
      { eq: "d_cube3" }
    ],
    ans: 0,
    trick: "this is the difference-of-cubes pattern run backwards — every middle term cancels, so the answer has exactly TWO terms, and a four-term answer is a sign that the cancelling was not done",
    why: "(x − 5)(x² + 5x + 25) = x³ − 125.",
    traps: [
      "B: the sign of the cube taken from the second bracket.",
      "C: the middle terms not cancelled.",
      "D: 5³ read as 5 × 3.",
    ],
  },
  {
    sig: "factor-a-difference-of-cubes",
    code: "SAAT-M-ALG.42", ses: 6, lvl: 3,
    stem: "Factor the expression below completely.",
    stemEq: "d_fcub",
    opts: [
      { eq: "d_fcub1" },
      { eq: "d_fcub2" },
      { eq: "d_fcub3" },
      { eq: "d_fcub4" }
    ],
    ans: 1,
    trick: "in the cubic pattern the middle term of the quadratic factor is PLUS ab, with no 2 in front of it — writing (a − b)² there is the single most common error on this skill",
    why: "8x³ − 27 = (2x)³ − 3³ = (2x − 3)(4x² + 6x + 9).",
    traps: [
      "A: the quadratic factor written as a perfect square.",
      "C: the sign inside the linear factor taken as plus.",
      "D: treated as a difference of squares.",
    ],
  },

  // ---------------------------------------------- session 7 · algebraic fractions
  {
    sig: "multiply-two-rational-expressions",
    code: "SAAT-M-ALG.43", ses: 7, lvl: 3,
    stem: "Simplify the product below.",
    stemEq: "d_mulr",
    opts: [
      { eq: "d_mulr3" },
      { eq: "d_mulr4" },
      { eq: "d_mulr1" },
      { eq: "d_mulr2" }
    ],
    ans: 2,
    trick: "factor BOTH fractions before anything is cancelled — cancelling a term that is part of a sum, rather than a whole factor, is what produces every wrong option here",
    why: "[(x² − 9)/(x + 2)] × [(x + 2)/(x − 3)] = [(x−3)(x+3)/(x+2)] × [(x+2)/(x−3)] = x + 3.",
    traps: [
      "A: x² − 9 read as (x − 3)².",
      "B: the two denominators cancelled but the numerators multiplied out.",
      "D: the (x − 3) cancelled and the (x + 3) dropped with it.",
    ],
  },
  {
    sig: "divide-two-rational-expressions",
    code: "SAAT-M-ALG.44", ses: 7, lvl: 3,
    stem: "Simplify the quotient below.",
    stemEq: "d_divr",
    opts: [
      { eq: "d_divr4" },
      { eq: "d_divr1" },
      { eq: "d_divr2" },
      { eq: "d_divr3" }
    ],
    ans: 3,
    trick: "invert the SECOND fraction and multiply — inverting the first instead gives the reciprocal of the right answer, which is always one of the options",
    why: "(3x/8) ÷ (9x²/4) = (3x/8) × (4/9x²) = 1/(6x).",
    traps: [
      "A: the powers of x not divided.",
      "B: the first fraction inverted instead of the second.",
      "C: the two fractions simply multiplied.",
    ],
  },

  // ============================================================ UNIT 2
  // ---------------------------------------------- session 10 · matrices
  {
    sig: "order-of-a-matrix-and-an-element",
    code: "SAAT-M-ALG.45", ses: 10, lvl: 2,
    stem: "For the matrix below, state its order and the value of the element a₃₂.",
    stemEq: "d_mord",
    opts: [
      "3 × 2, and a₃₂ = −1",
      "2 × 3, and a₃₂ = −1",
      "3 × 2, and a₃₂ = 6",
      "2 × 3, and a₃₂ = 6"
    ],
    ans: 0,
    trick: "order is ROWS × COLUMNS and the subscripts of an element are read the same way round — a₃₂ is row three, column two, not column three, row two",
    why: "The matrix has three rows and two columns; row 3 is (6  −1), whose second entry is −1.",
    traps: [
      "B: order written columns first.",
      "C: a₃₂ read as row 3, and then the first entry taken.",
      "D: both errors together.",
    ],
  },
  {
    sig: "scalar-multiple-of-a-matrix",
    code: "SAAT-M-ALG.46", ses: 10, lvl: 2,
    stem: "Find the matrix below.",
    stemEq: "d_msc",
    opts: [
      { eq: "d_msc1" },
      { eq: "d_msc2" },
      { eq: "d_msc3" },
      { eq: "d_msc4" }
    ],
    ans: 1,
    trick: "the scalar multiplies EVERY entry, and a negative scalar reverses the sign of an already negative entry — the entry that started negative is the one that decides the question",
    why: "−3 × [[4, 1], [7, −2]] = [[−12, −3], [−21, 6]].",
    traps: [
      "A: only the first row multiplied.",
      "C: the sign of the entry that was already negative left unchanged.",
      "D: −3 added to each entry rather than multiplied.",
    ],
  },
  {
    sig: "product-of-two-2x2-matrices",
    code: "SAAT-M-ALG.47", ses: 10, lvl: 4,
    stem: "Find the product below.",
    stemEq: "d_mpr",
    opts: [
      { eq: "d_mpr2" },
      { eq: "d_mpr3" },
      { eq: "d_mpr4" },
      { eq: "d_mpr1" }
    ],
    ans: 2,
    trick: "each entry is a ROW of the first against a COLUMN of the second — multiplying entry by entry in place is the error the paper is looking for, and it always produces a tidy-looking wrong matrix",
    why: "[[2,3],[1,4]] × [[5,6],[7,8]] = [[10+21, 12+24], [5+28, 6+32]] = [[31, 36], [33, 38]].",
    traps: [
      "A: rows taken against rows instead of columns.",
      "B: the two matrices multiplied in the other order.",
      "D: the matrices multiplied entry by entry in place.",
    ],
  },
  {
    sig: "determinant-of-a-3x3",
    code: "SAAT-M-ALG.48", ses: 10, lvl: 4,
    stem: "Find the value of the determinant below.",
    stemEq: "d_det3",
    opts: [
      "31",
      "48",
      "−41",
      "41"
    ],
    ans: 3,
    trick: "the middle term of the expansion carries a MINUS sign before it, whatever the sign of the entry itself — the checkerboard of signs is the whole difficulty of a 3 × 3",
    why: "2(4·6 − 5·0) − 1(0·6 − 5·1) + 3(0·0 − 4·1) = 48 + 5 − 12 = 41.",
    traps: [
      "A: the minus sign in front of the middle term dropped.",
      "B: the determinant taken as the product of the main diagonal, 2 × 4 × 6.",
      "C: the sign of the whole expansion reversed.",
    ],
  },

  // ---------------------------------------------- session 13 · completing the square & the formula
  {
    sig: "square-root-property",
    code: "SAAT-M-ALG.49", ses: 13, lvl: 2,
    stem: "Solve the equation below.",
    stemEq: "d_sqp",
    opts: [
      { eq: "d_sqp3" },
      { eq: "d_sqp4" },
      { eq: "d_sqp1" },
      { eq: "d_sqp2" }
    ],
    ans: 0,
    trick: "taking the root of both sides gives PLUS OR MINUS — keeping only the positive root loses one solution, and the lost one is the one the options are built around",
    why: "(x − 5)² = 9 gives x − 5 = ±3, so x = 8 or x = 2.",
    traps: [
      "B: the square root of 9 taken as 4.5.",
      "C: only the positive root taken.",
      "D: the 5 subtracted instead of added.",
    ],
  },
  {
    sig: "complete-the-square-with-surd-roots",
    code: "SAAT-M-ALG.50", ses: 13, lvl: 4,
    stem: "Solve the equation below by completing the square.",
    stemEq: "d_cts2",
    opts: [
      { eq: "d_cts2a" },
      { eq: "d_cts2b" },
      { eq: "d_cts2c" },
      { eq: "d_cts2d" }
    ],
    ans: 1,
    trick: "half of the x coefficient is squared and then SUBTRACTED again so the equation is unchanged — adding 9 without taking it back off is the classic slip, and it shifts the constant by exactly 9",
    why: "x² + 6x − 14 = (x + 3)² − 9 − 14 = 0, so (x + 3)² = 23 and x = −3 ± √23.",
    traps: [
      "A: the 9 added but never subtracted, leaving 5 under the root.",
      "C: the sign of the 3 outside the bracket kept as plus.",
      "D: the root taken only positively.",
    ],
  },
  {
    sig: "sum-and-product-of-roots",
    code: "SAAT-M-ALG.51", ses: 13, lvl: 3,
    stem: "Without solving it, find the sum and the product of the roots of the equation below.",
    stemEq: "d_sump",
    opts: [
      "Sum −4, product 5",
      "Sum 4, product −5",
      "Sum −4, product −5",
      "Sum 4, product 5"
    ],
    ans: 2,
    trick: "the sum is MINUS b over a and the product is c over a — the minus sign belongs to the sum only, and forgetting it flips the answer to the option beside it",
    why: "For 2x² + 8x − 10 = 0: sum = −8/2 = −4, product = −10/2 = −5.",
    traps: [
      "A: the sign of c/a reversed as well.",
      "B: the minus sign in −b/a dropped.",
      "D: both signs taken from the coefficients as written.",
    ],
  },

  // ---------------------------------------------- session 16 · polynomial equations
  {
    sig: "quadratic-in-disguise",
    code: "SAAT-M-ALG.52", ses: 16, lvl: 4,
    stem: "Solve the equation below.",
    stemEq: "d_dis",
    opts: [
      { eq: "d_dis2" },
      { eq: "d_dis3" },
      { eq: "d_dis4" },
      { eq: "d_dis1" }
    ],
    ans: 3,
    trick: "put u = x² and the equation becomes an ordinary quadratic — but the answer wanted is x, not u, so every value of u still has to be un-squared, and a NEGATIVE u gives no real x at all",
    why: "With u = x²: u² − 13u + 36 = 0, so u = 4 or 9, and x = ±2 or ±3.",
    traps: [
      "A: the values of u reported as the values of x.",
      "B: only the positive square roots kept.",
      "C: the quadratic in u factored with the wrong pair.",
    ],
  },
  {
    sig: "number-of-roots-from-the-degree",
    code: "SAAT-M-ALG.53", ses: 16, lvl: 2,
    stem: "How many roots does the equation below have in the set of complex numbers, counted with repeats?",
    stemEq: "d_nrt",
    opts: [
      "5",
      "2",
      "4",
      "3"
    ],
    ans: 0,
    trick: "count the DEGREE, not the number of terms and not the number of real roots you can see — the fundamental theorem gives exactly as many complex roots as the degree",
    why: "The polynomial has degree 5, so it has five complex roots counted with multiplicity.",
    traps: [
      "B: only the real roots counted.",
      "C: the degree of the second term taken.",
      "D: the number of terms counted.",
    ],
  },

  // ---------------------------------------------- session 17 · rational equations
  {
    sig: "rational-inequality-boundary-values",
    code: "SAAT-M-ALG.54", ses: 17, lvl: 4,
    stem: "Which values must be marked on the number line before the inequality below can be solved?",
    stemEq: "d_rin",
    opts: [
      "Only x = 5",
      "x = 5 and x = 2",
      "x = 2 only",
      "x = 5, x = 2 and x = 0"
    ],
    ans: 1,
    trick: "a rational inequality has TWO kinds of boundary — where the expression is zero and where it is undefined — and the undefined one is never part of the solution however the inequality sign points",
    why: "(x − 2)/(x − 5) is zero at x = 2 and undefined at x = 5.",
    traps: [
      "A: only the excluded value found.",
      "C: only the zero of the numerator found.",
      "D: x = 0 added, which is neither a zero nor an exclusion here.",
    ],
  },

  // ============================================================ UNIT 3
  // ---------------------------------------------- session 19 · relations & functions
  {
    sig: "is-the-relation-a-function",
    code: "SAAT-M-ALG.55", ses: 19, lvl: 2,
    stem: "Which set of ordered pairs below does NOT represent a function?",
    opts: [
      "{(−2, 3), (−1, 3), (0, 5)}",
      "{(1, 4), (2, 4), (3, 4)}",
      "{(1, 4), (1, 5), (2, 6)}",
      "{(0, 0), (1, 1), (2, 8)}"
    ],
    ans: 2,
    trick: "a function forbids a repeated FIRST coordinate, never a repeated second — three pairs all sharing the same y is a perfectly good function, and it is the option most students strike out first",
    why: "In {(1, 4), (1, 5), (2, 6)} the input 1 has two different outputs.",
    traps: [
      "A: two inputs share the output 3, which is again allowed.",
      "B: one output shared by three inputs, which a function allows.",
      "D: every input used once.",
    ],
  },
  {
    sig: "vertical-line-test",
    code: "SAAT-M-ALG.56", ses: 19, lvl: 2,
    stem: "Which of the curves below fails the vertical line test?",
    opts: [
      "A straight line of slope 2",
      "The graph of the absolute-value function",
      "A parabola opening upwards",
      "A circle of radius 4 centred at the origin"
    ],
    ans: 3,
    trick: "the test is about a VERTICAL line meeting the curve twice — a parabola is met twice by a HORIZONTAL line, which is a different test and a different question",
    why: "The line x = 0 meets the circle at (0, 4) and (0, −4).",
    traps: [
      "A: a non-vertical line is met once by every vertical line.",
      "B: the V shape is met once by every vertical line.",
      "C: a parabola fails the horizontal line test, not the vertical one.",
    ],
  },
  {
    sig: "one-to-one-by-the-horizontal-line-test",
    code: "SAAT-M-ALG.57", ses: 19, lvl: 3,
    stem: "Which function below is one-to-one on the whole set of real numbers?",
    opts: [
      { eq: "d_o2o3" },
      { eq: "d_o2o4" },
      { eq: "d_o2o1" },
      { eq: "d_o2o2" }
    ],
    ans: 0,
    trick: "one-to-one means no HORIZONTAL line meets the graph twice — every even power and every absolute value fails it immediately, because f(−x) equals f(x)",
    why: "A cubic of positive leading coefficient with no turning points is strictly increasing, so it is one-to-one.",
    traps: [
      "B: a quadratic is met twice by every horizontal line above its vertex.",
      "C: an even power takes the same value at x and at −x.",
      "D: the absolute value is symmetric about the y-axis.",
    ],
  },

  // ---------------------------------------------- session 20 · domain & range
  {
    sig: "domain-of-a-radical-function",
    code: "SAAT-M-ALG.58", ses: 20, lvl: 2,
    stem: "What is the domain of the function below?",
    stemEq: "d_dmr",
    opts: [
      { eq: "d_dmr3" },
      { eq: "d_dmr4" },
      { eq: "d_dmr1" },
      { eq: "d_dmr2" }
    ],
    ans: 1,
    trick: "the expression under an EVEN root must be greater than or equal to zero — the inequality is solved for x, and the sign of the answer is the opposite of the sign inside the bracket",
    why: "x + 4 ≥ 0 gives x ≥ −4.",
    traps: [
      "A: the inequality reversed.",
      "C: the sign of the 4 carried straight through.",
      "D: the endpoint excluded, though the root of zero is defined.",
    ],
  },
  {
    sig: "domain-of-a-rational-function-two-exclusions",
    code: "SAAT-M-ALG.59", ses: 20, lvl: 3,
    stem: "What is the domain of the function below?",
    stemEq: "d_dmq",
    opts: [
      { eq: "d_dmq3" },
      { eq: "d_dmq4" },
      { eq: "d_dmq1" },
      { eq: "d_dmq2" }
    ],
    ans: 2,
    trick: "factor the denominator FIRST — a quadratic denominator normally excludes two values, and stopping at the one that is easy to see costs the mark",
    why: "x² − 7x = x(x − 7) is zero at x = 0 and x = 7, so both are excluded.",
    traps: [
      "A: only x = 0 excluded.",
      "B: the zeros of the numerator excluded instead.",
      "D: only x = 7 excluded.",
    ],
  },
  {
    sig: "range-of-an-absolute-value-function",
    code: "SAAT-M-ALG.60", ses: 20, lvl: 3,
    stem: "What is the range of the function below?",
    stemEq: "d_rga",
    opts: [
      { eq: "d_rga3" },
      { eq: "d_rga4" },
      { eq: "d_rga1" },
      { eq: "d_rga2" }
    ],
    ans: 3,
    trick: "the absolute value itself is never negative, so the smallest value the whole expression can take is the constant on the end — the coefficient inside the bars changes the width of the V, never the height of its point",
    why: "|2x| ≥ 0, so f(x) = |2x| − 4 ≥ −4.",
    traps: [
      "A: the domain given instead of the range.",
      "B: the 2 inside the bars taken to lift the vertex.",
      "C: the sign of the constant read as positive.",
    ],
  },
  {
    sig: "domain-and-range-of-the-greatest-integer-function",
    code: "SAAT-M-ALG.61", ses: 20, lvl: 3,
    stem: "For the greatest-integer function f(x) = ⌊x⌋, which statement below is correct?",
    opts: [
      "The domain is the real numbers and the range is the integers",
      "The domain and the range are both the real numbers",
      "The domain and the range are both the integers",
      "The domain is the integers and the range is the real numbers"
    ],
    ans: 0,
    trick: "every real number has a floor, so the DOMAIN is unrestricted — it is the OUTPUT that is trapped on the integers, and the two are easy to swap under time pressure",
    why: "⌊x⌋ is defined for every real x and always returns an integer.",
    traps: [
      "B: the range taken to be continuous because the input is.",
      "C: the domain restricted to the values where the output changes.",
      "D: domain and range interchanged.",
    ],
  },

  // ---------------------------------------------- session 21 · function notation
  {
    sig: "evaluate-a-function-at-two-values",
    code: "SAAT-M-ALG.62", ses: 21, lvl: 2,
    stem: "For the function below, find f(3) − f(0).",
    stemEq: "d_ev2",
    opts: [
      "24",
      "18",
      "36",
      "12"
    ],
    ans: 1,
    trick: "substitute the whole value, brackets included, before squaring — and f(0) is not zero here, because a constant term survives every substitution",
    why: "f(3) = 2(9) − 8 = 10 and f(0) = −8, so f(3) − f(0) = 18.",
    traps: [
      "A: 2x² read as (2x)².",
      "C: f(0) taken as 0 and f(3) doubled.",
      "D: the two values added rather than subtracted, after an arithmetic slip.",
    ],
  },
  {
    sig: "evaluate-a-piecewise-function",
    code: "SAAT-M-ALG.63", ses: 21, lvl: 3,
    stem: "For the piecewise function below, find f(−2) + f(4).",
    stemEq: "d_pw",
    opts: [
      "7",
      "13",
      "11",
      "17"
    ],
    ans: 2,
    trick: "check which branch each input belongs to BEFORE substituting — an input on the boundary belongs to the branch whose inequality is not strict, and using one rule for both inputs is the error the options are built on",
    why: "−2 < 1 so f(−2) = 3(−2) + 2 = −4; 4 ≥ 1 so f(4) = 4² − 1 = 15; the sum is 11.",
    traps: [
      "A: the first rule used for both inputs.",
      "B: the branches swapped.",
      "D: the second rule used for both inputs.",
    ],
  },
  {
    sig: "solve-f-of-x-equals-k",
    code: "SAAT-M-ALG.64", ses: 21, lvl: 3,
    stem: "For the function below, find every value of x for which f(x) = 12.",
    stemEq: "d_fk",
    opts: [
      { eq: "d_fk4" },
      { eq: "d_fk1" },
      { eq: "d_fk2" },
      { eq: "d_fk3" }
    ],
    ans: 3,
    trick: "set the rule equal to the value and bring EVERYTHING to one side — solving f(x) = 12 is a quadratic equation, so it has two answers, and stopping at one is what the short option is there to catch",
    why: "x² + x = 12 gives x² + x − 12 = 0, so (x + 4)(x − 3) = 0 and x = −4 or x = 3.",
    traps: [
      "A: 12 factored as 2 × 6 and the signs guessed.",
      "B: the equation solved as if 12 were on the left.",
      "C: only the positive root kept.",
    ],
  },

  // ---------------------------------------------- session 22 · graphs of functions
  {
    sig: "zeros-and-the-y-intercept",
    code: "SAAT-M-ALG.65", ses: 22, lvl: 3,
    stem: "Find the zeros and the y-intercept of the function below.",
    stemEq: "d_zyi",
    opts: [
      "Zeros −3 and 2.5, y-intercept −15",
      "Zeros 3 and −2.5, y-intercept −15",
      "Zeros −3 and 2.5, y-intercept 15",
      "Zeros −3 and 2.5, y-intercept 0"
    ],
    ans: 0,
    trick: "the zeros come from f(x) = 0 and the y-intercept from f(0) — two different substitutions, and the y-intercept of a polynomial is simply its constant term, sign and all",
    why: "2x² + x − 15 = (2x − 5)(x + 3) gives x = 2.5 and x = −3; f(0) = −15.",
    traps: [
      "B: the signs of both zeros reversed.",
      "C: the sign of the constant term dropped.",
      "D: the y-intercept taken as zero because the zeros were found first.",
    ],
  },

  // ---------------------------------------------- session 23 · transformations of functions
  {
    sig: "name-the-parent-function",
    code: "SAAT-M-ALG.66", ses: 23, lvl: 2,
    stem: "What is the parent function of the rule below?",
    stemEq: "d_par",
    opts: [
      { eq: "d_par1" },
      { eq: "d_par2" },
      { eq: "d_par3" },
      { eq: "d_par4" }
    ],
    ans: 1,
    trick: "strip away every shift, stretch and reflection and read what is LEFT — the parent keeps the operation, never the numbers attached to it",
    why: "y = −3(x + 2)² + 7 is built from y = x².",
    traps: [
      "A: the minus sign read as part of the parent.",
      "C: the linear inside the bracket taken as the parent.",
      "D: the constant read as a cubic term.",
    ],
  },
  {
    sig: "horizontal-compression-and-reflection",
    code: "SAAT-M-ALG.67", ses: 23, lvl: 4,
    stem: "Describe the graph of the function below in terms of the graph of y = x².",
    stemEq: "d_hcr",
    opts: [
      "A vertical stretch by a factor of 2, then a reflection in the y-axis",
      "A horizontal compression by a factor of one half only",
      "A horizontal compression by a factor of one half, then a reflection in the x-axis",
      "A horizontal stretch by a factor of 2, then a reflection in the x-axis"
    ],
    ans: 2,
    trick: "a number multiplying x INSIDE the function squeezes the graph by its reciprocal — a 2 inside compresses, it does not stretch, and the minus in front reflects in the x-axis, not the y-axis",
    why: "g(x) = −(2x)² compresses horizontally by 1/2 and then reflects in the x-axis.",
    traps: [
      "A: the 2 read as a vertical stretch and the reflection put on the wrong axis.",
      "B: the leading minus sign ignored.",
      "D: the inside factor read as a stretch.",
    ],
  },
  {
    sig: "translate-a-parent-graph",
    code: "SAAT-M-ALG.68", ses: 23, lvl: 3,
    stem: "The graph of the function below is moved 3 units to the right and 5 units down. What is the rule of the new graph?",
    stemEq: "j_shiftroot",
    opts: [
      { eq: "d_tpg4" },
      { eq: "d_tpg1" },
      { eq: "d_tpg2" },
      { eq: "d_tpg3" }
    ],
    ans: 3,
    trick: "a move to the RIGHT appears as a MINUS inside the function — the horizontal sign is always the opposite of the direction, while the vertical sign is not",
    why: "Right 3 and down 5 give y = √(x − 3) − 5.",
    traps: [
      "A: the 5 put inside the root with the 3.",
      "B: the horizontal sign taken as it reads.",
      "C: both signs reversed.",
    ],
  },

  // ---------------------------------------------- session 24 · inverse functions
  {
    sig: "inverse-from-a-set-of-ordered-pairs",
    code: "SAAT-M-ALG.69", ses: 24, lvl: 2,
    stem: "If A = {(1, 5), (2, 6), (3, 7)}, which set below is its inverse?",
    opts: [
      "{(5, 1), (6, 2), (7, 3)}",
      "{(−1, −5), (−2, −6), (−3, −7)}",
      "{(1, 1/5), (2, 1/6), (3, 1/7)}",
      "{(1, 5), (2, 6), (3, 7)}"
    ],
    ans: 0,
    trick: "the inverse of a relation SWAPS the coordinates of every pair — it is not a reciprocal and it is not a change of sign, whatever the word inverse suggests elsewhere in the syllabus",
    why: "Exchanging the two coordinates of each pair gives {(5, 1), (6, 2), (7, 3)}.",
    traps: [
      "B: inverse read as negative.",
      "C: inverse read as reciprocal.",
      "D: the original set unchanged.",
    ],
  },
  {
    sig: "inverse-of-a-radical-function",
    code: "SAAT-M-ALG.70", ses: 24, lvl: 4,
    stem: "Find the inverse of the function below, together with the domain of that inverse.",
    stemEq: "d_invr",
    opts: [
      { eq: "d_invr3" },
      { eq: "d_invr4" },
      { eq: "d_invr1" },
      { eq: "d_invr2" }
    ],
    ans: 1,
    trick: "square both sides only AFTER x and y have been exchanged, and then remember that the domain of the inverse is the RANGE of the original — a square root is never negative, so the inverse is restricted",
    why: "y = √(x − 4) gives x = √(y − 4), so y = x² + 4 with x ≥ 0.",
    traps: [
      "A: the square root kept instead of being undone.",
      "C: the 4 moved to the wrong side.",
      "D: no restriction stated, so the rule is not a function's inverse.",
    ],
  },
  {
    sig: "verify-a-pair-of-inverses",
    code: "SAAT-M-ALG.71", ses: 24, lvl: 3,
    stem: "Which composition must be checked, and what must it equal, to prove that two functions are inverses of each other?",
    opts: [
      "Both f(g(x)) and g(f(x)), and each must equal 1",
      "f(g(x)) only, and it must equal 1",
      "Both f(g(x)) and g(f(x)), and each must equal x",
      "f(x) · g(x), and it must equal 1"
    ],
    ans: 2,
    trick: "inverse under COMPOSITION returns x, not 1 — the answer 1 belongs to multiplicative inverses, and checking one order only is not a proof",
    why: "f and g are inverses exactly when f(g(x)) = g(f(x)) = x.",
    traps: [
      "A: the right compositions, the wrong target.",
      "B: only one order checked, and the wrong target.",
      "D: the multiplicative inverse tested instead.",
    ],
  },

  // ---------------------------------------------- session 25 · composite functions
  {
    sig: "sum-and-product-of-two-functions",
    code: "SAAT-M-ALG.72", ses: 25, lvl: 3,
    stem: "For f(x) = x² + 4x and h(x) = 3x − 5, find (f − h)(x).",
    opts: [
      { eq: "d_sfp2" },
      { eq: "d_sfp3" },
      { eq: "d_sfp4" },
      { eq: "d_sfp1" }
    ],
    ans: 3,
    trick: "subtracting a function subtracts ALL of it — the −5 becomes +5, and that single sign is what separates the right answer from the option beside it",
    why: "(x² + 4x) − (3x − 5) = x² + x + 5.",
    traps: [
      "A: the constant left as −5.",
      "B: the functions added instead of subtracted.",
      "C: the x terms subtracted the wrong way round.",
    ],
  },
  {
    sig: "domain-of-a-sum-of-functions",
    code: "SAAT-M-ALG.73", ses: 25, lvl: 4,
    stem: "For the two functions below, what is the domain of (f + g)(x)?",
    stemEq: "j_sumdom",
    opts: [
      { eq: "d_dsf3" },
      { eq: "d_dsf4" },
      { eq: "d_dsf1" },
      { eq: "d_dsf2" }
    ],
    ans: 0,
    trick: "the domain of a sum is the INTERSECTION of the two domains — the polynomial allows everything, so the radical alone decides, and the answer is the narrower of the two, never the wider",
    why: "f is defined everywhere and g needs x ≥ −2, so the intersection is x ≥ −2.",
    traps: [
      "B: the endpoint excluded.",
      "C: the union taken instead of the intersection.",
      "D: the sign of the 2 carried through unchanged.",
    ],
  },

  // ---------------------------------------------- session 26 · variation & modelling
  {
    sig: "direct-variation-find-a-value",
    code: "SAAT-M-ALG.74", ses: 26, lvl: 2,
    stem: "y varies directly as x, and y = 15 when x = 5. What is y when x = 7?",
    opts: [
      "10.5",
      "21",
      "17",
      "35"
    ],
    ans: 1,
    trick: "in DIRECT variation the RATIO stays fixed — set y₁/x₁ = y₂/x₂ and cross-multiply; adding the change to y instead of scaling it is the error the second option is built from",
    why: "15/5 = y/7, so y = 21.",
    traps: [
      "A: the relation treated as inverse.",
      "C: the increase of 2 in x simply added to y.",
      "D: the two known values multiplied.",
    ],
  },
  {
    sig: "inverse-variation-find-a-value",
    code: "SAAT-M-ALG.75", ses: 26, lvl: 3,
    stem: "a varies inversely as b, and a = 28 when b = 2. What is a when b = 10?",
    opts: [
      "36",
      "140",
      "5.6",
      "20"
    ],
    ans: 2,
    trick: "in INVERSE variation the PRODUCT stays fixed, so a₁b₁ = a₂b₂ — using the ratio rule here gives a number five times too big, which is exactly the first option",
    why: "28 × 2 = 56, so a = 56 ÷ 10 = 5.6.",
    traps: [
      "A: the constant taken as a + b.",
      "B: the direct-variation rule used.",
      "D: 28 reduced by the change in b.",
    ],
  },
  {
    sig: "combined-variation-find-a-value",
    code: "SAAT-M-ALG.76", ses: 26, lvl: 4,
    stem: "f varies directly as g and inversely as h. When g = 24 and h = 2, f = 6. Find g when f = 18 and h = −3.",
    opts: [
      "108",
      "−12",
      "12",
      "−108"
    ],
    ans: 3,
    trick: "build the constant first, k = f h ÷ g, and keep the SIGN of h all the way through — a negative h with a positive f forces g negative, and every positive option is a dropped sign",
    why: "k = 6 × 2 ÷ 24 = 1/2, so g = f h ÷ k = 18 × (−3) ÷ (1/2) = −108.",
    traps: [
      "A: the sign of h dropped.",
      "B: h multiplied where it should divide.",
      "C: both errors together.",
    ],
  },

  // ============================================================ UNIT 4
  // ---------------------------------------------- session 28 · points, lines & angles
  {
    sig: "name-the-angle-pair-at-a-transversal",
    code: "SAAT-M-GEO.5", ses: 28, lvl: 2,
    stem: "Two parallel lines are cut by a transversal. One angle lies above the first parallel and to the left of the transversal; another lies below the second parallel and to the right. What is this pair called, and what is true of them?",
    opts: [
      "Alternate exterior angles, and they are equal",
      "Co-interior angles, and they are supplementary",
      "Corresponding angles, and they are equal",
      "Alternate interior angles, and they are supplementary"
    ],
    ans: 0,
    trick: "OUTSIDE the pair of parallels and on OPPOSITE sides of the transversal makes them alternate EXTERIOR, and alternate pairs are equal — it is the co-interior pair, the one on the same side and inside, that adds to 180°",
    why: "Both angles are outside the parallels and on opposite sides of the transversal, so they are alternate exterior and therefore equal.",
    traps: [
      "B: the right relationship attached to the wrong pair.",
      "C: corresponding angles sit on the SAME side of the transversal.",
      "D: alternate pairs are equal, not supplementary.",
    ],
  },
  {
    sig: "co-interior-angles-find-the-angle",
    code: "SAAT-M-GEO.6", ses: 28, lvl: 3,
    stem: "Two parallel lines are cut by a transversal. One co-interior angle measures 3x + 10 degrees and the other measures 2x degrees. What is the larger of the two angles?",
    opts: [
      "102°",
      "112°",
      "68°",
      "34°"
    ],
    ans: 1,
    trick: "co-interior angles ADD to 180°, they are not equal — setting the two expressions equal to each other is the mistake, and it produces an answer that looks perfectly reasonable",
    why: "3x + 10 + 2x = 180 gives x = 34, so the angles are 112° and 68°.",
    traps: [
      "A: the two expressions set equal to each other.",
      "C: the smaller angle given.",
      "D: the value of x reported instead of an angle.",
    ],
  },
  {
    sig: "perpendicular-to-one-of-two-parallels",
    code: "SAAT-M-GEO.7", ses: 28, lvl: 2,
    stem: "In one plane, line a is parallel to line b, and line t is perpendicular to line a. What follows about t and b?",
    opts: [
      "Nothing can be decided without a diagram",
      "t is parallel to b",
      "t is perpendicular to b",
      "t meets b at 45°"
    ],
    ans: 2,
    trick: "a transversal perpendicular to one of two parallels is perpendicular to the OTHER as well — the right angle is carried across by the corresponding-angle relation, so no diagram is needed",
    why: "Corresponding angles at parallel lines are equal, so the 90° at a is repeated at b.",
    traps: [
      "A: the theorem is general; a diagram adds nothing.",
      "B: perpendicular confused with parallel.",
      "D: an angle invented from nothing in the statement.",
    ],
  },
  {
    sig: "segment-addition-betweenness",
    code: "SAAT-M-GEO.8", ses: 28, lvl: 2,
    stem: "Points A, B and C are collinear with B between A and C. If AB = 3x − 4, BC = x + 6 and AC = 26, what is x?",
    opts: [
      "8",
      "5",
      "7",
      "6"
    ],
    ans: 3,
    trick: "betweenness means the two short pieces ADD to the whole — AB + BC = AC, not AC − AB = BC solved as an equation in two unknowns",
    why: "(3x − 4) + (x + 6) = 26 gives 4x + 2 = 26, so x = 6.",
    traps: [
      "A: the constant 2 added instead of subtracted.",
      "B: the two expressions set equal to each other.",
      "C: AC divided by the number of pieces.",
    ],
  },

  // ---------------------------------------------- session 29 · properties of triangles
  {
    sig: "exterior-angle-of-a-triangle",
    code: "SAAT-M-GEO.9", ses: 29, lvl: 2,
    stem: "In a triangle the two remote interior angles measure 48° and 65°. What is the exterior angle at the third vertex?",
    opts: [
      "113°",
      "67°",
      "247°",
      "133°"
    ],
    ans: 0,
    trick: "an exterior angle equals the SUM of the two remote interior angles — going the long way round through the third angle and 180° gives the same number, but subtracting instead of adding gives the option beside it",
    why: "48 + 65 = 113.",
    traps: [
      "B: the third interior angle given instead of the exterior one.",
      "C: 360° used instead of 180°.",
      "D: 180 − 48 given.",
    ],
  },
  {
    sig: "equiangular-triangle-angle",
    code: "SAAT-M-GEO.10", ses: 29, lvl: 2,
    stem: "A triangle has three congruent sides. What is the measure of each of its angles, and why?",
    opts: [
      "It cannot be found without one angle being given",
      "60°, because a triangle is equilateral if and only if it is equiangular",
      "45°, because the three angles share 135°",
      "90°, because congruent sides force right angles"
    ],
    ans: 1,
    trick: "equilateral and equiangular are the SAME condition for a triangle, so three equal sides fix all three angles at once — no measurement is needed and none can be given",
    why: "Three equal sides give three equal angles, and 180 ÷ 3 = 60.",
    traps: [
      "A: the theorem overlooked.",
      "C: 180° divided by four.",
      "D: congruent sides confused with perpendicular sides.",
    ],
  },
  {
    sig: "perpendicular-bisector-equidistant",
    code: "SAAT-M-GEO.11", ses: 29, lvl: 3,
    stem: "Point P lies on the perpendicular bisector of segment AB. If PA = 4y − 7 and PB = y + 8, what is PA?",
    opts: [
      "20",
      "8",
      "13",
      "5"
    ],
    ans: 2,
    trick: "a point on the perpendicular bisector is EQUIDISTANT from the two endpoints, so the two expressions are equal — the answer wanted is the length, not the value of the variable, and both are among the options",
    why: "4y − 7 = y + 8 gives y = 5, so PA = 4(5) − 7 = 13.",
    traps: [
      "A: the two lengths added.",
      "B: the constants subtracted without solving.",
      "D: the value of y reported as the length.",
    ],
  },
  {
    sig: "circumcentre-of-an-obtuse-triangle",
    code: "SAAT-M-GEO.12", ses: 29, lvl: 3,
    stem: "Where does the point of concurrency of the perpendicular bisectors of an obtuse triangle lie?",
    opts: [
      "Inside the triangle",
      "At the midpoint of the longest side",
      "At the vertex of the obtuse angle",
      "Outside the triangle"
    ],
    ans: 3,
    trick: "the circumcentre sits INSIDE an acute triangle, ON the hypotenuse of a right triangle and OUTSIDE an obtuse one — the type of triangle is the whole question, and 'inside' is only true for the acute case",
    why: "For an obtuse triangle the circumcentre falls outside, on the far side of the longest side.",
    traps: [
      "A: true for an acute triangle only.",
      "B: true for a right triangle only.",
      "C: the incentre and circumcentre confused with a vertex.",
    ],
  },
  {
    sig: "incentre-equidistant-from-the-sides",
    code: "SAAT-M-GEO.13", ses: 29, lvl: 2,
    stem: "The angle bisectors of a triangle meet at a point P. What is true of P?",
    opts: [
      "It is the same distance from all three sides, and always lies inside the triangle",
      "It is the same distance from all three vertices, and always lies inside the triangle",
      "It divides each bisector in the ratio 2 : 1",
      "It is the same distance from all three sides, but may lie outside the triangle"
    ],
    ans: 0,
    trick: "angle bisectors give equal distances to the SIDES; perpendicular bisectors give equal distances to the VERTICES — and the incentre never leaves the triangle, whatever the shape",
    why: "Every point on an angle bisector is equidistant from the two arms, so the meeting point is equidistant from all three sides.",
    traps: [
      "B: the circumcentre's property attached to the incentre.",
      "C: the centroid's ratio attached to the incentre.",
      "D: the right distances, but the incentre is always interior.",
    ],
  },
  {
    sig: "centroid-divides-a-median",
    code: "SAAT-M-GEO.14", ses: 29, lvl: 3,
    stem: "P is the centroid of triangle ABC and the median from A has length 18. What is AP?",
    opts: [
      "36",
      "12",
      "6",
      "9"
    ],
    ans: 1,
    trick: "the centroid cuts each median so that the piece nearest the VERTEX is two thirds of the whole — one third is the piece nearest the midpoint, and it is the answer next door",
    why: "AP = (2/3) × 18 = 12.",
    traps: [
      "A: the median doubled.",
      "C: the third nearest the opposite side taken.",
      "D: the median halved.",
    ],
  },
  {
    sig: "at-most-one-right-or-obtuse-angle",
    code: "SAAT-M-GEO.15", ses: 29, lvl: 2,
    stem: "Which statement about the angles of a triangle is true?",
    opts: [
      "A triangle may have two obtuse angles if both are small",
      "Every triangle has at least one obtuse angle",
      "A triangle has at most one angle that is right or obtuse",
      "A triangle may have two right angles if the third is zero"
    ],
    ans: 2,
    trick: "two angles of 90° or more already reach 180° on their own, leaving nothing for the third — so the acute angles in any triangle are at least two, always",
    why: "The three angles sum to 180°, so at most one of them can be 90° or more.",
    traps: [
      "A: two obtuse angles exceed 180° between them.",
      "B: an acute-angled triangle has none.",
      "D: a zero angle does not close a triangle.",
    ],
  },

  // ---------------------------------------------- session 30 · congruence & similarity
  {
    sig: "which-congruence-rule-applies",
    code: "SAAT-M-GEO.16", ses: 30, lvl: 3,
    stem: "In two triangles, two sides of one are congruent to two sides of the other, and the angles between those pairs of sides are congruent. Which rule proves the triangles congruent?",
    opts: [
      "SSA",
      "AAA",
      "SSS",
      "SAS"
    ],
    ans: 3,
    trick: "the angle must be the one ENCLOSED by the two sides — an angle anywhere else gives SSA, which proves nothing, and that is the option placed directly beside the right one",
    why: "Two sides and the included angle is exactly the SAS condition.",
    traps: [
      "A: the angle not between the two sides proves nothing.",
      "B: three angles give similarity, not congruence.",
      "C: only two pairs of sides are known.",
    ],
  },
  {
    sig: "triangle-proportionality-find-a-length",
    code: "SAAT-M-GEO.17", ses: 30, lvl: 3,
    stem: "In triangle ABC a line parallel to BC meets AB at D and AC at E. If AD = 6, DB = 4 and AE = 9, what is EC?",
    opts: [
      "6",
      "13.5",
      "15",
      "5"
    ],
    ans: 0,
    trick: "the proportion pairs the pieces of one side with the pieces of the OTHER, top with top and bottom with bottom — pairing a piece with the whole side instead is what produces the large wrong answer",
    why: "AD/DB = AE/EC gives 6/4 = 9/EC, so EC = 6.",
    traps: [
      "B: the proportion inverted.",
      "C: AE paired with the whole of AB rather than with AD.",
      "D: DB copied across as EC.",
    ],
  },
  {
    sig: "midsegment-of-a-triangle",
    code: "SAAT-M-GEO.18", ses: 30, lvl: 2,
    stem: "J and K are the midpoints of two sides of a triangle, and the third side measures 17 cm. What is JK, and how is it related to that side?",
    opts: [
      "17 cm, and it is parallel to it",
      "8.5 cm, and it is parallel to it",
      "34 cm, and it is parallel to it",
      "8.5 cm, and it is perpendicular to it"
    ],
    ans: 1,
    trick: "a midsegment is HALF the third side and PARALLEL to it — both halves of that statement are examined, and the option that gets the length right and the direction wrong is always present",
    why: "The midsegment is parallel to the third side and half its length: 17 ÷ 2 = 8.5.",
    traps: [
      "A: the midsegment taken as equal to the side.",
      "C: the side doubled instead of halved.",
      "D: the right length, the wrong relationship.",
    ],
  },
  {
    sig: "three-parallels-cut-by-transversals",
    code: "SAAT-M-GEO.19", ses: 30, lvl: 3,
    stem: "Three parallel lines are cut by two transversals. On the first transversal they cut off pieces of 8 and 12. On the second, the piece matching the 8 measures 10. What is the other piece on the second transversal?",
    opts: [
      "12",
      "20",
      "15",
      "14"
    ],
    ans: 2,
    trick: "parallel lines cut PROPORTIONAL pieces on every transversal, not equal ones — carrying the difference across instead of the ratio gives the second option",
    why: "8/12 = 10/x gives x = 15.",
    traps: [
      "A: the pieces of the first transversal simply copied to the second.",
      "B: 10 doubled, on the assumption that 8 : 12 is 1 : 2.",
      "D: the difference of 4 added to 10 instead of the ratio applied.",
    ],
  },
  {
    sig: "ratio-of-corresponding-altitudes",
    code: "SAAT-M-GEO.20", ses: 30, lvl: 3,
    stem: "Two similar triangles have corresponding sides in the ratio 3 : 5. What is the ratio of their corresponding altitudes, and of their areas?",
    opts: [
      "Altitudes 9 : 25, areas 3 : 5",
      "Altitudes 3 : 5, areas 3 : 5",
      "Altitudes 9 : 25, areas 27 : 125",
      "Altitudes 3 : 5, areas 9 : 25"
    ],
    ans: 3,
    trick: "every LENGTH in similar figures — altitude, median, bisector, perimeter — carries the plain ratio, while AREA carries its square; the squaring belongs to the area alone",
    why: "Altitudes are lengths, so 3 : 5; areas scale as the square, so 9 : 25.",
    traps: [
      "A: the two ratios interchanged.",
      "B: the area left unsquared.",
      "C: the cube used, which belongs to volume.",
    ],
  },
  {
    sig: "angle-bisector-divides-the-opposite-side",
    code: "SAAT-M-GEO.21", ses: 30, lvl: 4,
    stem: "In triangle JKL the bisector from J meets KL at M. If JK = 12, JL = 18 and KM = 8, what is ML?",
    opts: [
      "12",
      "5.33",
      "14",
      "8"
    ],
    ans: 0,
    trick: "the bisector splits the opposite side in the ratio of the two sides that FORM the angle — pairing KM with JL instead of with JK inverts the ratio and gives a number that is too small",
    why: "KM/ML = JK/JL gives 8/ML = 12/18, so ML = 12.",
    traps: [
      "B: the ratio inverted.",
      "C: the difference of the two sides added to KM.",
      "D: the bisector assumed to bisect the opposite side as well.",
    ],
  },

  // ---------------------------------------------- session 31 · Pythagoras
  {
    sig: "pythagoras-inside-a-kite",
    code: "SAAT-M-GEO.22", ses: 31, lvl: 3,
    stem: "The diagonals of a kite are perpendicular. In one of the four right triangles the hypotenuse is 6 cm and one leg is 4 cm. What is the other leg?",
    opts: [
      { eq: "d_kite4" },
      { eq: "d_kite1" },
      { eq: "d_kite2" },
      { eq: "d_kite3" }
    ],
    ans: 1,
    trick: "the 6 is the HYPOTENUSE, so the legs are found by SUBTRACTING the squares — adding them instead gives √52, which is the option built to catch exactly that",
    why: "√(36 − 16) = √20 = 2√5.",
    traps: [
      "A: the root not simplified past 20.",
      "C: the squares added instead of subtracted.",
      "D: the lengths subtracted before squaring.",
    ],
  },
  {
    sig: "recognise-a-pythagorean-triple",
    code: "SAAT-M-GEO.23", ses: 31, lvl: 2,
    stem: "Which set of three lengths below can NOT be the sides of a right triangle?",
    opts: [
      "8, 15, 17",
      "7, 24, 25",
      "6, 8, 11",
      "9, 12, 15"
    ],
    ans: 2,
    trick: "test the LONGEST length as the hypotenuse and nothing else — a set that is a multiple of a known triple always works, and the one that fails usually looks closest to working",
    why: "6² + 8² = 100 but 11² = 121, so the triangle is not right-angled.",
    traps: [
      "A: a standard triple.",
      "B: a standard triple.",
      "D: three times the 3-4-5 triple.",
    ],
  },

  // ---------------------------------------------- session 32 · quadrilaterals & polygons
  {
    sig: "interior-angle-sum-of-a-polygon",
    code: "SAAT-M-GEO.24", ses: 32, lvl: 2,
    stem: "What is the sum of the interior angles of a regular heptagon?",
    opts: [
      "1260°",
      "720°",
      "540°",
      "900°"
    ],
    ans: 3,
    trick: "the rule is (n − 2) × 180° — using n instead of n − 2 overshoots by exactly 360°, and that overshoot is one of the options",
    why: "(7 − 2) × 180 = 900.",
    traps: [
      "A: n used instead of n − 2.",
      "B: a hexagon's sum.",
      "C: a pentagon's sum.",
    ],
  },
  {
    sig: "exterior-angle-sum-is-360",
    code: "SAAT-M-GEO.25", ses: 32, lvl: 3,
    stem: "The exterior angles of a convex polygon measure 3x + 10, 6x − 5, 2x − 5, 5x and 2x degrees. What is x?",
    opts: [
      "20",
      "40",
      "30",
      "72"
    ],
    ans: 0,
    trick: "the exterior angles of ANY convex polygon add to 360°, whatever the number of sides — reaching for (n − 2) × 180° here is the trap, and with five angles it gives 540 and a wrong x",
    why: "18x = 360, so x = 20.",
    traps: [
      "B: 720° used.",
      "C: 540°, the interior sum of a pentagon, used.",
      "D: the five angles assumed equal, 360 ÷ 5.",
    ],
  },
  {
    sig: "regular-polygon-one-interior-angle",
    code: "SAAT-M-GEO.26", ses: 32, lvl: 3,
    stem: "Each interior angle of a regular polygon measures 150°. How many sides has it?",
    opts: [
      "30",
      "12",
      "10",
      "24"
    ],
    ans: 1,
    trick: "go through the EXTERIOR angle: 180 − 150 = 30, and 360 ÷ 30 = 12 — dividing the interior angle into 360 directly is quicker and wrong",
    why: "Each exterior angle is 30°, and 360 ÷ 30 = 12.",
    traps: [
      "A: the exterior angle, 30°, reported as the number of sides.",
      "C: 1500 ÷ 150 taken as the count.",
      "D: 360 divided by half the interior angle.",
    ],
  },
  {
    sig: "consecutive-angles-of-a-parallelogram",
    code: "SAAT-M-GEO.27", ses: 32, lvl: 2,
    stem: "In a parallelogram one angle measures 55°. What are the measures of the other three?",
    opts: [
      "35°, 145°, 35°",
      "125°, 125°, 55°",
      "125°, 55°, 125°",
      "55°, 55°, 55°"
    ],
    ans: 2,
    trick: "opposite angles are EQUAL and consecutive angles are SUPPLEMENTARY — the two rules must be used in turn, and the angles round the shape alternate rather than repeat in pairs",
    why: "The opposite angle is 55° and the two consecutive ones are 180 − 55 = 125°.",
    traps: [
      "A: complementary used instead of supplementary.",
      "B: the equal pair placed adjacent instead of opposite.",
      "D: all angles taken as equal.",
    ],
  },
  {
    sig: "rectangle-diagonals-are-equal",
    code: "SAAT-M-GEO.28", ses: 32, lvl: 3,
    stem: "In rectangle FGHK the diagonals meet at P. If FP = 2x + 3 and PH = 5x − 9, what is the length of the diagonal FH?",
    opts: [
      "11",
      "4",
      "44",
      "22"
    ],
    ans: 3,
    trick: "the diagonals of a rectangle are equal AND bisect each other, so FP and PH are both HALF of FH — solving for the half and stopping there is what the small option rewards",
    why: "2x + 3 = 5x − 9 gives x = 4, so FP = 11 and FH = 22.",
    traps: [
      "A: the half-diagonal given instead of the whole.",
      "B: the value of x reported as a length.",
      "C: the whole diagonal doubled a second time.",
    ],
  },
  {
    sig: "rhombus-diagonal-bisects-the-angle",
    code: "SAAT-M-GEO.29", ses: 32, lvl: 3,
    stem: "In a rhombus the diagonals meet at P, and one vertex angle measures 82°. What is the acute angle between that diagonal and a side at the neighbouring vertex?",
    opts: [
      "49°",
      "41°",
      "82°",
      "45°"
    ],
    ans: 0,
    trick: "the diagonal bisects the vertex angle, giving 41°, and the diagonals are PERPENDICULAR — so the angle wanted is the third angle of a right triangle, 90 − 41, not the 41 itself",
    why: "Half of 82° is 41°, and 90 − 41 = 49.",
    traps: [
      "B: the bisected angle given, one step short.",
      "C: the vertex angle repeated.",
      "D: the diagonals assumed to bisect the right angle at P.",
    ],
  },
  {
    sig: "isosceles-trapezoid-base-angles",
    code: "SAAT-M-GEO.30", ses: 32, lvl: 2,
    stem: "In an isosceles trapezoid one base angle measures 85°. What are the measures of the angle beside it on the same leg, and of the other base angle?",
    opts: [
      "5° and 85°",
      "95° and 85°",
      "85° and 95°",
      "95° and 95°"
    ],
    ans: 1,
    trick: "the two angles on the SAME leg are co-interior and add to 180°, while the two angles on the SAME base are equal — mixing the two relations is the whole difficulty",
    why: "180 − 85 = 95 along the leg; the other base angle equals 85°.",
    traps: [
      "A: complementary used instead of supplementary.",
      "C: the two answers interchanged.",
      "D: both taken as supplementary.",
    ],
  },
  {
    sig: "diagonals-of-a-kite",
    code: "SAAT-M-GEO.31", ses: 32, lvl: 2,
    stem: "What is always true of the diagonals of a kite?",
    opts: [
      "They are equal in length",
      "They are parallel",
      "They are perpendicular",
      "They bisect each other"
    ],
    ans: 2,
    trick: "a kite guarantees only PERPENDICULAR diagonals — one of them bisects the other, but they do not bisect each other, and that half-truth is the option beside the answer",
    why: "The axis of symmetry of a kite is perpendicular to the other diagonal.",
    traps: [
      "A: equal diagonals belong to a rectangle.",
      "B: diagonals of any quadrilateral meet.",
      "D: only one diagonal is bisected, not both.",
    ],
  },

  // ---------------------------------------------- session 33 · circles
  {
    sig: "circumference-from-the-diameter",
    code: "SAAT-M-GEO.32", ses: 33, lvl: 2,
    stem: "A circular fountain in a Jeddah park has a diameter of 16 m. Taking π ≈ 3.14, what is its circumference?",
    opts: [
      "100.48 m",
      "200.96 m",
      "25.12 m",
      "50.24 m"
    ],
    ans: 3,
    trick: "C = πd OR C = 2πr, never both at once — using 2πd doubles the answer, and that doubled value is always offered",
    why: "3.14 × 16 = 50.24.",
    traps: [
      "A: 2πd used.",
      "B: the area formula used with r = 8.",
      "C: the radius used in πd.",
    ],
  },
  {
    sig: "inscribed-angle-half-the-arc",
    code: "SAAT-M-GEO.33", ses: 33, lvl: 2,
    stem: "An inscribed angle of a circle subtends an arc of 126°. What is the measure of the angle?",
    opts: [
      "63°",
      "126°",
      "252°",
      "117°"
    ],
    ans: 0,
    trick: "an INSCRIBED angle is half its arc; a CENTRAL angle equals its arc — the two are told apart by where the vertex sits, and the arc itself is always offered as an option",
    why: "126 ÷ 2 = 63.",
    traps: [
      "B: the central angle given instead.",
      "C: the arc doubled.",
      "D: 180 − 63 taken.",
    ],
  },
  {
    sig: "angle-in-a-semicircle",
    code: "SAAT-M-GEO.34", ses: 33, lvl: 3,
    stem: "In a circle, RS is a diameter and T is a point on the circle. If angle TRS = 3x + 1 and angle TSR = 7x − 1, what is x?",
    opts: [
      "45",
      "9",
      "18",
      "0.5"
    ],
    ans: 1,
    trick: "the angle at T is 90° because it stands on a diameter, so the other two angles are COMPLEMENTARY, adding to 90 and not to 180 — using 180 doubles the answer",
    why: "3x + 1 + 7x − 1 = 90 gives 10x = 90, so x = 9.",
    traps: [
      "A: the right angle at T reported instead of x.",
      "C: 180 used instead of 90.",
      "D: the two expressions set equal to each other.",
    ],
  },
  {
    sig: "cyclic-quadrilateral-opposite-angles",
    code: "SAAT-M-GEO.35", ses: 33, lvl: 2,
    stem: "A quadrilateral WXYZ is inscribed in a circle. If angle Z = 60° and angle W = 95°, what are angles X and Y?",
    opts: [
      "X = 30°, Y = 5°",
      "X = 85°, Y = 120°",
      "X = 120°, Y = 85°",
      "X = 60°, Y = 95°"
    ],
    ans: 2,
    trick: "OPPOSITE angles of a cyclic quadrilateral are supplementary, adjacent ones are not — so X pairs with Z and Y pairs with W, and pairing them the other way round swaps the two answers",
    why: "X = 180 − 60 = 120 and Y = 180 − 95 = 85.",
    traps: [
      "A: complementary used instead of supplementary.",
      "B: the pairing reversed.",
      "D: opposite angles taken as equal.",
    ],
  },
  {
    sig: "two-tangents-from-an-external-point",
    code: "SAAT-M-GEO.36", ses: 33, lvl: 2,
    stem: "From a point outside a circle two tangent segments are drawn to the circle. What is true of them?",
    opts: [
      "They are perpendicular to each other",
      "They are congruent to the radius",
      "One is twice the other",
      "They are congruent"
    ],
    ans: 3,
    trick: "two tangents from the same external point are EQUAL — the right angle in the figure is between a tangent and the RADIUS at the point of contact, not between the two tangents",
    why: "The two right triangles formed share a hypotenuse and have equal legs, so the tangents are congruent.",
    traps: [
      "A: the right angle is at the point of contact, not at the external point.",
      "B: the tangent length depends on how far away the point is.",
      "C: no such relation exists.",
    ],
  },
  {
    sig: "tangent-chord-angle",
    code: "SAAT-M-GEO.37", ses: 33, lvl: 3,
    stem: "A tangent and a chord meet at a point on a circle, and the intercepted arc measures 148°. What is the angle between them?",
    opts: [
      "74°",
      "148°",
      "106°",
      "37°"
    ],
    ans: 0,
    trick: "a tangent-chord angle is HALF its intercepted arc, exactly like an inscribed angle — the vertex being on the circle is what matters, not that one arm is a tangent",
    why: "148 ÷ 2 = 74.",
    traps: [
      "B: the arc given as the angle.",
      "C: 180 − 74 taken.",
      "D: the arc quartered.",
    ],
  },
  {
    sig: "angle-between-two-chords",
    code: "SAAT-M-GEO.38", ses: 33, lvl: 3,
    stem: "Two chords of a circle cross inside it. The two arcs they intercept measure 60° and 125°. What is the angle between the chords?",
    opts: [
      "65°",
      "92.5°",
      "32.5°",
      "185°"
    ],
    ans: 1,
    trick: "the vertex INSIDE the circle takes HALF the SUM of the two arcs; a vertex outside takes half the DIFFERENCE — one word decides which, and both answers are on the page",
    why: "(60 + 125) ÷ 2 = 92.5.",
    traps: [
      "A: the difference of the arcs taken.",
      "C: half the difference taken, which belongs to an external vertex.",
      "D: the arcs added and not halved.",
    ],
  },
  {
    sig: "angle-between-two-secants",
    code: "SAAT-M-GEO.39", ses: 33, lvl: 4,
    stem: "Two secants are drawn from a point outside a circle. The angle between them measures 56° and the nearer arc measures 95°. What is the far arc?",
    opts: [
      "39°",
      "112°",
      "207°",
      "151°"
    ],
    ans: 2,
    trick: "outside the circle the angle is half the DIFFERENCE of the arcs — so the far arc is twice the angle PLUS the near arc, and simply adding the angle to the arc gives the option beside it",
    why: "56 = (far − 95) ÷ 2 gives far = 112 + 95 = 207.",
    traps: [
      "A: the angle subtracted from the near arc.",
      "B: only twice the angle given.",
      "D: the angle added once to the near arc.",
    ],
  },
  {
    sig: "intersecting-chords-product",
    code: "SAAT-M-GEO.40", ses: 33, lvl: 3,
    stem: "Two chords of a circle cross. One is cut into pieces of 5 and 12; the other is cut into pieces of 10 and x. What is x?",
    opts: [
      "7",
      "24",
      "8.5",
      "6"
    ],
    ans: 3,
    trick: "the two PRODUCTS are equal, not the two sums — adding the pieces instead of multiplying them is what makes the second option look right",
    why: "10x = 5 × 12 = 60, so x = 6.",
    traps: [
      "A: the pieces added instead of multiplied.",
      "B: 60 taken as the answer without dividing.",
      "C: the halves of the chords averaged.",
    ],
  },
  {
    sig: "two-secants-from-an-external-point",
    code: "SAAT-M-GEO.41", ses: 33, lvl: 4,
    stem: "From an external point two secants are drawn. On the first the external piece is 8 and the whole secant is 8 + x. On the second the external piece is 6 and the whole secant is 16. What is x?",
    opts: [
      "4",
      "12",
      "6",
      "8"
    ],
    ans: 0,
    trick: "each side of the equation is EXTERNAL piece × WHOLE secant — using the far piece instead of the whole secant is the standard error, and it makes every number in the problem look usable",
    why: "8(8 + x) = 6(16) gives 64 + 8x = 96, so x = 4.",
    traps: [
      "B: 96 ÷ 8 taken as x directly, without subtracting the external piece.",
      "C: the external piece of the second secant copied across.",
      "D: the two whole secants assumed equal.",
    ],
  },
  {
    sig: "tangent-secant-square",
    code: "SAAT-M-GEO.42", ses: 33, lvl: 4,
    stem: "A tangent of length 6 and a secant are drawn to a circle from the same external point. The external piece of the secant measures 4. What is the far piece?",
    opts: [
      "32",
      "5",
      "9",
      "4"
    ],
    ans: 1,
    trick: "the tangent is SQUARED and set equal to external × whole — the whole secant is 4 + far, so the answer is not 36 ÷ 4 but that quotient minus the external piece",
    why: "36 = 4(4 + far) gives 4 + far = 9, so the far piece is 5.",
    traps: [
      "A: the external piece subtracted from the square of the tangent.",
      "C: the WHOLE secant given rather than the far piece.",
      "D: the external piece copied as the answer.",
    ],
  },

  // ---------------------------------------------- session 34 · perimeter & area
  {
    sig: "area-of-a-sector",
    code: "SAAT-M-GEO.43", ses: 34, lvl: 3,
    stem: "A sector of a circle of radius 12 cm has a central angle of 60°. Taking π ≈ 3.14, what is its area?",
    opts: [
      "150.72 cm²",
      "37.68 cm²",
      "75.36 cm²",
      "12.56 cm²"
    ],
    ans: 2,
    trick: "a sector is the FRACTION of the circle that its angle is of 360°, applied to the AREA — applying it to the circumference instead gives the arc length, which is the small option",
    why: "(60/360) × 3.14 × 144 = 75.36.",
    traps: [
      "A: the fraction taken as one third instead of one sixth.",
      "B: the sector area halved once more.",
      "D: the arc length found instead of the area.",
    ],
  },
  {
    sig: "arc-length-from-a-central-angle",
    code: "SAAT-M-GEO.44", ses: 34, lvl: 3,
    stem: "An arc of a circle of radius 10 cm is cut off by a central angle of 72°. Taking π ≈ 3.14, what is the arc length?",
    opts: [
      "62.8 cm",
      "6.28 cm",
      "31.4 cm",
      "12.56 cm"
    ],
    ans: 3,
    trick: "arc length uses the CIRCUMFERENCE, 2πr, not the area — the fraction is the same in both, so the whole question is which of the two whole-circle measures you scale",
    why: "(72/360) × 2 × 3.14 × 10 = 12.56.",
    traps: [
      "A: the sector area found instead.",
      "B: πr used instead of 2πr.",
      "C: the circumference of a semicircle given.",
    ],
  },

  // ---------------------------------------------- session 36 · three-dimensional geometry
  {
    sig: "midpoint-in-three-dimensions",
    code: "SAAT-M-GEO.45", ses: 36, lvl: 3,
    stem: "What is the midpoint of the segment joining A(−3, −4, 2) and B(3, 2, −3)?",
    opts: [
      { eq: "d_mid31" },
      { eq: "d_mid32" },
      { eq: "d_mid33" },
      { eq: "d_mid34" }
    ],
    ans: 0,
    trick: "average each coordinate SEPARATELY — subtracting instead of adding gives the components of the vector AB, which is a different object and is always offered",
    why: "((−3+3)/2, (−4+2)/2, (2−3)/2) = (0, −1, −0.5).",
    traps: [
      "B: the coordinates subtracted, giving the direction vector halved.",
      "C: the sum taken without dividing by two.",
      "D: the z-coordinate averaged with the wrong sign.",
    ],
  },

  // ============================================================ UNIT 5
  // ---------------------------------------------- session 37 · slope
  {
    sig: "slope-of-a-vertical-line",
    code: "SAAT-M-GEO.46", ses: 37, lvl: 2,
    stem: "What is the slope of the line through (4, −1) and (4, 7)?",
    opts: [
      "2",
      "Undefined",
      "0",
      "8"
    ],
    ans: 1,
    trick: "a repeated x makes the DENOMINATOR zero, and a zero denominator means the slope does not exist — a slope of zero is the horizontal case, where the y values repeat instead",
    why: "The run is 4 − 4 = 0, so the quotient is undefined.",
    traps: [
      "A: the two x values divided into the rise.",
      "C: the horizontal case, where the y values would repeat.",
      "D: the rise given without dividing.",
    ],
  },

  // ---------------------------------------------- session 38 · parallel & perpendicular
  {
    sig: "slope-of-a-perpendicular-line",
    code: "SAAT-M-GEO.47", ses: 38, lvl: 2,
    stem: "A line has slope −2/5. What is the slope of any line perpendicular to it?",
    opts: [
      { eq: "d_perp3" },
      { eq: "d_perp4" },
      { eq: "d_perp1" },
      { eq: "d_perp2" }
    ],
    ans: 2,
    trick: "the perpendicular slope is the NEGATIVE RECIPROCAL — flipping the fraction without changing the sign, or changing the sign without flipping, each gives an option on this page",
    why: "The negative reciprocal of −2/5 is 5/2.",
    traps: [
      "A: only the sign changed.",
      "B: the same slope repeated, which gives a parallel line.",
      "D: the fraction inverted with the sign kept.",
    ],
  },
  {
    sig: "equation-of-a-perpendicular-bisector",
    code: "SAAT-M-GEO.48", ses: 38, lvl: 4,
    stem: "What is the equation of the perpendicular bisector of the segment joining P(5, 2) and Q(7, 4)?",
    opts: [
      { eq: "d_pb4" },
      { eq: "d_pb1" },
      { eq: "d_pb2" },
      { eq: "d_pb3" }
    ],
    ans: 3,
    trick: "two things are needed and both are easy to half-do — the MIDPOINT to pass through, and the NEGATIVE RECIPROCAL of the segment's slope; using the segment's own slope gives a line through the midpoint that bisects nothing",
    why: "Midpoint (6, 3); slope of PQ is 1, so the bisector has slope −1: y = −x + 9.",
    traps: [
      "A: the midpoint coordinates added rather than averaged.",
      "B: the slope of PQ used instead of its negative reciprocal.",
      "C: the correct slope through P rather than the midpoint.",
    ],
  },

  // ---------------------------------------------- session 39 · distance & midpoint
  {
    sig: "midpoint-given-one-endpoint",
    code: "SAAT-M-GEO.49", ses: 39, lvl: 3,
    stem: "M(6, 3) is the midpoint of segment AB, and A is (2, −1). What are the coordinates of B?",
    opts: [
      { eq: "d_mep1" },
      { eq: "d_mep2" },
      { eq: "d_mep3" },
      { eq: "d_mep4" }
    ],
    ans: 0,
    trick: "work the midpoint formula BACKWARDS: B = 2M − A, coordinate by coordinate — averaging M with A instead gives the quarter point, which is the option next to the answer",
    why: "B = (2·6 − 2, 2·3 − (−1)) = (10, 7).",
    traps: [
      "B: M and A averaged instead.",
      "C: A subtracted from M without doubling.",
      "D: the sign of the −1 lost.",
    ],
  },
  {
    sig: "distance-between-two-points",
    code: "SAAT-M-GEO.50", ses: 39, lvl: 2,
    stem: "What is the distance between R(−2, −1) and S(1, −4)?",
    opts: [
      { eq: "d_dst4" },
      { eq: "d_dst1" },
      { eq: "d_dst2" },
      { eq: "d_dst3" }
    ],
    ans: 1,
    trick: "subtract first and square afterwards — squaring the coordinates before subtracting is the error, and with two negative coordinates it looks convincing",
    why: "√((1+2)² + (−4+1)²) = √(9 + 9) = 3√2.",
    traps: [
      "A: the root not simplified past 18.",
      "C: the coordinates squared before being subtracted.",
      "D: the differences added without squaring.",
    ],
  },

  // ---------------------------------------------- session 40 · transformations in the plane
  {
    sig: "translate-then-reflect",
    code: "SAAT-M-GEO.51", ses: 40, lvl: 4,
    stem: "The point J(6, −1) is moved 4 units up and then reflected in the y-axis. What is its final image?",
    opts: [
      { eq: "d_trf3" },
      { eq: "d_trf4" },
      { eq: "d_trf1" },
      { eq: "d_trf2" }
    ],
    ans: 2,
    trick: "do the two steps IN ORDER — a reflection in the y-axis changes the sign of x only, so the translation done afterwards would land somewhere else entirely",
    why: "(6, −1) → (6, 3) → (−6, 3).",
    traps: [
      "A: reflected in the x-axis instead.",
      "B: the translation applied to x rather than to y.",
      "D: the two steps done in the other order.",
    ],
  },
  {
    sig: "dilation-scale-factor",
    code: "SAAT-M-GEO.52", ses: 40, lvl: 3,
    stem: "A triangle with vertices at (2, 4), (−6, 2) and (0, −8) is dilated about the origin with scale factor 1/2. What is the image of the second vertex?",
    opts: [
      { eq: "d_dil2" },
      { eq: "d_dil3" },
      { eq: "d_dil4" },
      { eq: "d_dil1" }
    ],
    ans: 3,
    trick: "a dilation MULTIPLIES both coordinates by the factor — subtracting the factor, or applying it to one coordinate only, are the two errors the options are built from",
    why: "(−6, 2) × 1/2 = (−3, 1).",
    traps: [
      "A: the factor applied to the x-coordinate only.",
      "B: the factor 1/2 subtracted from each coordinate.",
      "C: the factor taken as 2 rather than one half.",
    ],
  },

  // ---------------------------------------------- session 41 · measures of centre
  {
    sig: "which-measure-of-centre-to-use",
    code: "SAAT-M-STA.3", ses: 41, lvl: 2,
    stem: "A set of monthly salaries contains one figure many times larger than all the others. Which measure of centre best describes the set, and why?",
    opts: [
      "The median, because it is not dragged by an extreme value",
      "The mean, because it uses every value in the set",
      "The mode, because it is the value that occurs most often",
      "The mean, because the extreme value should be represented"
    ],
    ans: 0,
    trick: "an OUTLIER moves the mean and leaves the median where it is — 'uses every value' sounds like a strength and is exactly the weakness in this case",
    why: "The median depends only on position, so a single extreme value cannot shift it.",
    traps: [
      "B: using every value is what makes the mean vulnerable here.",
      "C: the mode may not exist, and need not sit near the centre.",
      "D: one salary should not decide the summary of many.",
    ],
  },
  {
    sig: "expected-value-of-a-die",
    code: "SAAT-M-STA.4", ses: 41, lvl: 3,
    stem: "A fair six-sided die numbered 1 to 6 is rolled once. What is the expected value of the number shown?",
    opts: [
      "6",
      "3.5",
      "3",
      "21"
    ],
    ans: 1,
    trick: "expected value is the SUM of value × probability, and it need not be a value the die can actually show — an answer that must be a whole number is the giveaway that the division was skipped",
    why: "(1 + 2 + 3 + 4 + 5 + 6) ÷ 6 = 3.5.",
    traps: [
      "A: the largest outcome taken.",
      "C: the answer rounded to a face that exists.",
      "D: the sum given without dividing.",
    ],
  },

  // ---------------------------------------------- session 42 · dispersion & sampling
  {
    sig: "margin-of-sampling-error",
    code: "SAAT-M-STA.5", ses: 42, lvl: 3,
    stem: "A random survey of 2500 people reports that 58% name football as their favourite sport. What is the margin of sampling error, to the nearest tenth of a percent?",
    opts: [
      "0.04%",
      "5.8%",
      "2.0%",
      "4.0%"
    ],
    ans: 2,
    trick: "the margin is one over the ROOT of the sample size, not one over the sample size — and the reported percentage plays no part in it at all",
    why: "1/√2500 = 1/50 = 0.02 = 2.0%.",
    traps: [
      "A: 1/2500 used without the root.",
      "B: the reported percentage divided by ten.",
      "D: the margin doubled to give the whole interval width.",
    ],
  },
  {
    sig: "interval-from-a-margin-of-error",
    code: "SAAT-M-STA.6", ses: 42, lvl: 3,
    stem: "A poll reports 46% support with a margin of sampling error of 2.5%. Which interval is likely to contain the true proportion?",
    opts: [
      "46% to 48.5%",
      "43.5% to 46%",
      "41% to 51%",
      "43.5% to 48.5%"
    ],
    ans: 3,
    trick: "the margin is applied in BOTH directions, so the interval is symmetric about the reported figure — a one-sided interval and a doubled margin are both offered",
    why: "46 − 2.5 = 43.5 and 46 + 2.5 = 48.5.",
    traps: [
      "A: the margin applied upwards only.",
      "B: the margin applied downwards only.",
      "C: the margin doubled before being applied.",
    ],
  },

  // ---------------------------------------------- session 43 · probability & counting
  {
    sig: "size-of-a-sample-space",
    code: "SAAT-M-STA.7", ses: 43, lvl: 2,
    stem: "A coin is tossed twice. How many outcomes are in the sample space, and are they equally likely?",
    opts: [
      "4, and they are equally likely",
      "3, and they are equally likely",
      "4, and they are not equally likely",
      "2, and they are equally likely"
    ],
    ans: 0,
    trick: "count ORDERED outcomes — head-then-tail and tail-then-head are two different outcomes, and counting 'one of each' as a single case is what reduces the four to three",
    why: "HH, HT, TH, TT are four outcomes, each of probability 1/4.",
    traps: [
      "B: HT and TH counted as one outcome.",
      "C: the count is right but a fair coin gives equal outcomes.",
      "D: the outcomes of a single toss counted.",
    ],
  },
  {
    sig: "fundamental-counting-principle",
    code: "SAAT-M-STA.8", ses: 43, lvl: 2,
    stem: "A tailor in Jeddah offers 5 fabrics, 6 colours, 3 sleeve styles and 2 collar styles. How many different thobes can be ordered?",
    opts: [
      "360",
      "180",
      "16",
      "90"
    ],
    ans: 1,
    trick: "independent choices MULTIPLY, they do not add — the sum of the four numbers is always offered and is always wrong",
    why: "5 × 6 × 3 × 2 = 180.",
    traps: [
      "A: the product doubled.",
      "C: the four numbers added.",
      "D: the collar choice left out.",
    ],
  },
  {
    sig: "geometric-probability-by-length",
    code: "SAAT-M-STA.9", ses: 43, lvl: 3,
    stem: "A point is chosen at random on a segment JL of length 14 cm. A sub-segment KL measures 7 cm. What is the probability that the point lies on KL?",
    opts: [
      "0.07",
      "0.14",
      "0.5",
      "7"
    ],
    ans: 2,
    trick: "geometric probability is a RATIO of two lengths, so it is a number between 0 and 1 and carries no units — an answer in centimetres has skipped the division",
    why: "7 ÷ 14 = 0.5.",
    traps: [
      "A: the length read as a percentage of 100.",
      "B: the whole length read as a decimal.",
      "D: the favourable length given as the probability.",
    ],
  },
  {
    sig: "geometric-probability-by-area",
    code: "SAAT-M-STA.10", ses: 43, lvl: 3,
    stem: "A square target of side 8 cm has a shaded square of side 3 cm inside it. A dart lands at random on the target. What is the probability that it lands on the shaded square?",
    opts: [
      "3/8",
      "64/9",
      "1/9",
      "9/64"
    ],
    ans: 3,
    trick: "with areas the ratio uses the SQUARES of the sides, not the sides — the ratio of the sides is the option that looks simplest and is offered first",
    why: "9 ÷ 64.",
    traps: [
      "A: the ratio of the sides given.",
      "B: the ratio inverted.",
      "C: the reciprocal of the shaded area taken.",
    ],
  },
  {
    sig: "mutually-exclusive-union",
    code: "SAAT-M-STA.11", ses: 43, lvl: 3,
    stem: "A library holds 10 religious books, 12 physics books and 13 chemistry books. One book is chosen at random. What is the probability that it is religious or physics?",
    opts: [
      "22/35",
      "35/22",
      "10/35",
      "120/35"
    ],
    ans: 0,
    trick: "the two categories cannot overlap, so the probabilities simply ADD — the denominator is the TOTAL number of books, and using only the two categories mentioned is the standard slip",
    why: "(10 + 12) ÷ 35 = 22/35.",
    traps: [
      "B: the fraction inverted.",
      "C: only the religious books counted.",
      "D: the two counts multiplied.",
    ],
  },
  {
    sig: "union-not-mutually-exclusive",
    code: "SAAT-M-STA.12", ses: 43, lvl: 4,
    stem: "A fair die is rolled once. What is the probability of getting a number greater than 2 or an even number?",
    opts: [
      "1/2",
      "5/6",
      "7/6",
      "4/6"
    ],
    ans: 1,
    trick: "the two events OVERLAP — 4 and 6 are in both — so the overlap must be subtracted once, otherwise the answer exceeds 1 and that impossible value is on the page",
    why: "4/6 + 3/6 − 2/6 = 5/6.",
    traps: [
      "A: only the second event counted.",
      "C: the overlap not subtracted, giving a probability above 1.",
      "D: only the first event counted.",
    ],
  },
  {
    sig: "complement-of-an-event",
    code: "SAAT-M-STA.13", ses: 43, lvl: 2,
    stem: "A box holds 300 tickets, of which 20 win a prize. One ticket is drawn at random. What is the probability that it does NOT win?",
    opts: [
      "20/300",
      "15/14",
      "14/15",
      "1/15"
    ],
    ans: 2,
    trick: "subtract from ONE, not from the number of tickets — the complement is a probability, so the answer is 1 − 20/300 and never a count",
    why: "1 − 20/300 = 280/300 = 14/15.",
    traps: [
      "A: the winning probability unsimplified.",
      "B: the answer inverted.",
      "D: the winning probability given instead.",
    ],
  },

  // ---------------------------------------------- session 44 · permutations, combinations & conditional
  {
    sig: "permutations-nPr",
    code: "SAAT-M-STA.14", ses: 44, lvl: 2,
    stem: "In how many ways can 2 of 7 different books be placed in order on a shelf?",
    opts: [
      "21",
      "49",
      "14",
      "42"
    ],
    ans: 3,
    trick: "ORDER matters on a shelf, so this is a permutation, not a combination — the combination answer is exactly half of it and is always offered",
    why: "7 × 6 = 42.",
    traps: [
      "A: the combination counted instead of the permutation.",
      "B: 7² taken, allowing the same book twice.",
      "C: the two numbers multiplied.",
    ],
  },
  {
    sig: "combinations-nCr",
    code: "SAAT-M-STA.15", ses: 44, lvl: 3,
    stem: "A committee of 3 is to be chosen from 8 people. In how many ways can this be done?",
    opts: [
      "56",
      "336",
      "24",
      "112"
    ],
    ans: 0,
    trick: "a committee has no ORDER, so divide the permutation count by 3! — leaving that division out multiplies the answer by six, and that value is on the page",
    why: "8!/(3!·5!) = 56.",
    traps: [
      "B: the permutation count given.",
      "C: 8 × 3 taken.",
      "D: the answer doubled.",
    ],
  },
  {
    sig: "permutations-with-repeated-letters",
    code: "SAAT-M-STA.16", ses: 44, lvl: 4,
    stem: "How many distinct arrangements are there of the letters of the word LEVEL?",
    opts: [
      "20",
      "30",
      "120",
      "60"
    ],
    ans: 1,
    trick: "divide by the factorial of EACH repeated letter's count — LEVEL repeats both L and E, so the division is by 2! twice, not once",
    why: "5!/(2!·2!) = 120 ÷ 4 = 30.",
    traps: [
      "A: divided by 3! by miscounting the repeats.",
      "C: no division for the repeats.",
      "D: divided by 2! once only.",
    ],
  },
  {
    sig: "circular-permutations",
    code: "SAAT-M-STA.17", ses: 44, lvl: 3,
    stem: "In how many ways can 6 people be seated around a round table, if only their positions relative to one another matter?",
    opts: [
      "36",
      "60",
      "120",
      "720"
    ],
    ans: 2,
    trick: "a circle has no first seat, so one person is FIXED and the rest are arranged — the count is (n − 1)!, not n!, and the straight-line answer is offered beside it",
    why: "(6 − 1)! = 120.",
    traps: [
      "A: 6² taken.",
      "B: 720 divided by 12 rather than by 6.",
      "D: the straight-line arrangement counted.",
    ],
  },
  {
    sig: "independent-events-product",
    code: "SAAT-M-STA.18", ses: 44, lvl: 2,
    stem: "A coin is tossed and a fair six-sided die is rolled. What is the probability of a head and a six?",
    opts: [
      "2/3",
      "7/12",
      "1/8",
      "1/12"
    ],
    ans: 3,
    trick: "independent events MULTIPLY for 'and' — adding them is what 'or' does for exclusive events, and that sum is on the page",
    why: "1/2 × 1/6 = 1/12.",
    traps: [
      "A: the two probabilities added and mishandled.",
      "B: the two probabilities added.",
      "C: the die treated as having eight faces.",
    ],
  },
  {
    sig: "dependent-events-without-replacement",
    code: "SAAT-M-STA.19", ses: 44, lvl: 4,
    stem: "A bag holds 5 yellow slips and 3 blue slips. Two slips are drawn one after the other and the first is not replaced. What is the probability that both are yellow?",
    opts: [
      "5/14",
      "25/64",
      "25/56",
      "15/56"
    ],
    ans: 0,
    trick: "without replacement BOTH the favourable count and the total drop by one for the second draw — treating the second draw as if the bag were untouched gives the square, which is offered",
    why: "5/8 × 4/7 = 20/56 = 5/14.",
    traps: [
      "B: the first probability squared, as if the slip were replaced.",
      "C: only the total reduced, not the favourable count.",
      "D: the second slip taken as blue.",
    ],
  },

  // ============================================================ UNIT 6
  {
    sig: "growth-or-decay-from-the-base",
    code: "SAAT-M-ALG.77", ses: 47, lvl: 2,
    stem: "Which of the functions below is an exponential DECAY function?",
    opts: [
      { eq: "d_gd2" },
      { eq: "d_gd3" },
      { eq: "d_gd4" },
      { eq: "d_gd1" }
    ],
    ans: 1,
    trick: "decay is decided by the BASE lying strictly between 0 and 1 — a negative coefficient in front makes the graph point downwards but does not make it decay, and that is the option beside the answer",
    why: "y = 5(1/3)^x has base 1/3, which lies between 0 and 1.",
    traps: [
      "A: a negative coefficient reflects the graph; the base still grows.",
      "C: the exponent is negative but the base is written as 3, and the reader must convert first.",
      "D: base greater than 1, so this grows.",
    ],
  },
  {
    sig: "y-intercept-and-asymptote-of-an-exponential",
    code: "SAAT-M-ALG.78", ses: 47, lvl: 3,
    stem: "For the parent function y = b^x with b > 1, what are the y-intercept and the asymptote?",
    opts: [
      "y-intercept 1, asymptote the y-axis",
      "y-intercept b, asymptote the x-axis",
      "y-intercept 1, asymptote the x-axis",
      "y-intercept 0, asymptote the x-axis"
    ],
    ans: 2,
    trick: "b⁰ = 1 whatever the base, so every exponential parent passes through (0, 1) — an intercept of 0 would mean the curve touches the axis it is asymptotic to, which it never does",
    why: "b⁰ = 1, and b^x approaches 0 as x → −∞ without reaching it.",
    traps: [
      "A: the asymptote of the exponential is horizontal, not vertical.",
      "B: b¹ read instead of b⁰.",
      "D: the curve never meets the x-axis, so 0 is impossible.",
    ],
  },
  {
    sig: "solve-by-equating-exponents",
    code: "SAAT-M-ALG.79", ses: 48, lvl: 3,
    stem: "Solve the equation below.",
    stemEq: "d_eeq",
    opts: [
      "3",
      "27",
      "6",
      "9"
    ],
    ans: 3,
    trick: "write BOTH sides to the same base first — 8 is 2³, so the right side becomes 2⁹, and comparing 2^x with 8 directly is what produces the answer 3",
    why: "2^x = 8³ = 2⁹, so x = 9.",
    traps: [
      "A: the exponent of the base read as the answer.",
      "B: 8³ evaluated but the base not matched.",
      "C: 8 read as 2 × 3.",
    ],
  },
  {
    sig: "exponential-inequality",
    code: "SAAT-M-ALG.80", ses: 48, lvl: 4,
    stem: "Solve the inequality below.",
    stemEq: "d_eineq",
    opts: [
      { eq: "d_ein2" },
      { eq: "d_ein3" },
      { eq: "d_ein4" },
      { eq: "d_ein1" }
    ],
    ans: 0,
    trick: "with a base GREATER than 1 the inequality between the exponents keeps its direction — the sign only reverses for a base between 0 and 1, and reversing it here is the trap",
    why: "4 · 2^(8x−12) > 2⁴ gives 2^(8x−10) > 2⁴, so 8x − 10 > 4 and x > 7/4.",
    traps: [
      "B: the coefficient 4 left out of the left side.",
      "C: 16 not written as a power of 2.",
      "D: the inequality reversed.",
    ],
  },
  {
    sig: "logarithmic-to-exponential-form",
    code: "SAAT-M-ALG.81", ses: 49, lvl: 2,
    stem: "Which exponential statement is equivalent to log₃ 27 = y?",
    opts: [
      { eq: "d_lef4" },
      { eq: "d_lef1" },
      { eq: "d_lef2" },
      { eq: "d_lef3" }
    ],
    ans: 1,
    trick: "the BASE stays the base and the logarithm is the EXPONENT — swapping the base with the number inside is the standard error, and it gives a statement that is also true-looking",
    why: "log₃ 27 = y means 3^y = 27.",
    traps: [
      "A: y and 27 interchanged.",
      "C: the base and the argument interchanged.",
      "D: the logarithm read as a product.",
    ],
  },
  {
    sig: "domain-of-a-logarithm",
    code: "SAAT-M-ALG.82", ses: 49, lvl: 3,
    stem: "Why is log₁₀(−5) undefined over the real numbers?",
    opts: [
      "Because logarithms are defined only for integers",
      "Because the base 10 is too small",
      "Because no real power of 10 gives a negative number",
      "Because the base must also be negative"
    ],
    ans: 2,
    trick: "a positive base raised to ANY real power stays positive, so the argument of a logarithm must be strictly positive — the restriction sits on the argument, never on the base's size",
    why: "10^y > 0 for every real y, so 10^y = −5 has no real solution.",
    traps: [
      "A: log₁₀ 2.5 is perfectly well defined.",
      "B: the size of the base is irrelevant.",
      "D: a negative base is not allowed either, but that is not the reason here.",
    ],
  },
  {
    sig: "logarithmic-inequality",
    code: "SAAT-M-ALG.83", ses: 51, lvl: 4,
    stem: "Solve the inequality below.",
    stemEq: "d_lineq",
    opts: [
      { eq: "d_li2" },
      { eq: "d_li3" },
      { eq: "d_li4" },
      { eq: "d_li1" }
    ],
    ans: 3,
    trick: "raise the base to both sides, and remember the DOMAIN — the argument must stay positive, so the solution can never include zero or a negative number however the algebra comes out",
    why: "log₃ x > 4 gives x > 3⁴ = 81.",
    traps: [
      "A: the 4 multiplied by the base instead of used as an exponent.",
      "B: the inequality reversed.",
      "C: the base and the exponent interchanged.",
    ],
  },
  {
    sig: "solve-an-exponential-with-common-logs",
    code: "SAAT-M-ALG.84", ses: 51, lvl: 4,
    stem: "Solve 4^x = 19, giving the answer as a quotient of logarithms.",
    opts: [
      { eq: "d_scl1" },
      { eq: "d_scl2" },
      { eq: "d_scl3" },
      { eq: "d_scl4" }
    ],
    ans: 0,
    trick: "take logs of both sides and bring the exponent down — the answer is log 19 DIVIDED by log 4, never the log of the quotient, and the two are close enough on the page to be confused",
    why: "x log 4 = log 19, so x = log 19 ÷ log 4.",
    traps: [
      "B: the logarithm of the quotient taken.",
      "C: the quotient inverted.",
      "D: the logs subtracted instead of divided.",
    ],
  },

  // ============================================================ UNIT 7
  {
    sig: "arithmetic-geometric-or-neither",
    code: "SAAT-M-ALG.85", ses: 55, lvl: 2,
    stem: "Which of the sequences below is geometric?",
    opts: [
      "5, −6, −17, −28, …",
      "−2, 6, −18, 54, …",
      "8, 16, 24, 32, …",
      "4, 12, 28, 42, …"
    ],
    ans: 1,
    trick: "test the RATIO of consecutive terms, not the difference — a sequence whose signs alternate is very often geometric with a negative ratio, and it is the one that looks least regular",
    why: "6 ÷ (−2) = −3, −18 ÷ 6 = −3 and 54 ÷ (−18) = −3.",
    traps: [
      "A: a constant difference of −11, so arithmetic.",
      "C: a constant difference of 8, so arithmetic.",
      "D: neither the differences nor the ratios are constant.",
    ],
  },
  {
    sig: "nth-term-of-an-arithmetic-sequence",
    code: "SAAT-M-ALG.86", ses: 56, lvl: 2,
    stem: "Find the twelfth term of the arithmetic sequence 9, 16, 23, 30 and so on.",
    opts: [
      "79",
      "84",
      "86",
      "93"
    ],
    ans: 2,
    trick: "the formula uses n − 1, not n — multiplying the difference by 12 instead of by 11 overshoots by exactly one common difference, and that value is offered",
    why: "9 + (12 − 1)(7) = 9 + 77 = 86.",
    traps: [
      "A: n − 2 used.",
      "B: the first term left out of the sum.",
      "D: n used in place of n − 1.",
    ],
  },
  {
    sig: "arithmetic-means-between-two-terms",
    code: "SAAT-M-ALG.87", ses: 56, lvl: 4,
    stem: "Insert four arithmetic means between −8 and 22. What is the common difference?",
    opts: [
      "7.5",
      "5",
      "30",
      "6"
    ],
    ans: 3,
    trick: "inserting FOUR means makes SIX terms in all, so the difference is spread over five steps — dividing by four is the error, and it gives the option beside the answer",
    why: "22 = −8 + 5d gives 5d = 30, so d = 6.",
    traps: [
      "A: the range divided by four.",
      "B: the range divided by six.",
      "C: the range given as the difference.",
    ],
  },
  {
    sig: "sum-of-an-arithmetic-series",
    code: "SAAT-M-ALG.88", ses: 56, lvl: 3,
    stem: "Find the sum 2 + 4 + 6 + ⋯ + 100.",
    opts: [
      "2550",
      "5100",
      "2500",
      "1275"
    ],
    ans: 0,
    trick: "find HOW MANY terms first — there are 50, not 100, and using the last term as the count doubles the answer",
    why: "n = 50 and S = (50/2)(2 + 100) = 25 × 102 = 2550.",
    traps: [
      "B: 100 used as the number of terms.",
      "C: the sum of the first 50 whole numbers squared, taken as a shortcut.",
      "D: the sum halved.",
    ],
  },
  {
    sig: "nth-term-of-a-geometric-sequence",
    code: "SAAT-M-ALG.89", ses: 57, lvl: 3,
    stem: "In a geometric sequence the fourth term is 5 and the common ratio is 6. What is the sixth term?",
    opts: [
      "150",
      "180",
      "30",
      "1080"
    ],
    ans: 1,
    trick: "from the fourth term to the sixth is TWO steps, so multiply by the ratio squared — one step gives 30 and three gives 1080, and both are on the page",
    why: "5 × 6² = 180.",
    traps: [
      "A: the ratio added twice rather than multiplied.",
      "C: one step taken instead of two.",
      "D: three steps taken.",
    ],
  },
  {
    sig: "geometric-means-between-two-terms",
    code: "SAAT-M-ALG.90", ses: 57, lvl: 4,
    stem: "Three geometric means are inserted between 2 and 1250. What are the possible values of the common ratio?",
    opts: [
      "±25",
      "±625",
      "±5",
      "5"
    ],
    ans: 2,
    trick: "three means make FIVE terms, so r⁴ = 625 — and an EVEN power leaves two possible ratios, one positive and one negative, so answering with the positive one alone is only half the answer",
    why: "1250 = 2r⁴ gives r⁴ = 625, so r = ±5.",
    traps: [
      "A: the square root taken once instead of twice.",
      "B: r to the fourth reported instead of r.",
      "D: the negative ratio overlooked.",
    ],
  },
  {
    sig: "sum-of-a-geometric-series",
    code: "SAAT-M-ALG.91", ses: 57, lvl: 4,
    stem: "Find the sum of the first seven terms of a geometric series whose first term is 12 and whose ratio is 3.",
    opts: [
      "26244",
      "4372",
      "8748",
      "13116"
    ],
    ans: 3,
    trick: "the formula needs r to the power n, and n is the NUMBER of terms, not the index of the last one — using r⁶ here loses two thirds of the sum",
    why: "12(1 − 3⁷)/(1 − 3) = 12(1 − 2187)/(−2) = 13116.",
    traps: [
      "A: the sum doubled by dividing by 1 rather than by r − 1.",
      "B: 3⁶ used instead of 3⁷.",
      "C: the seventh term given instead of the sum.",
    ],
  },
  {
    sig: "convergent-or-divergent-series",
    code: "SAAT-M-ALG.92", ses: 58, lvl: 3,
    stem: "Which infinite geometric series below converges?",
    opts: [
      "54 + 36 + 24 + ⋯",
      "8 + 12 + 18 + ⋯",
      "3 + 6 + 12 + ⋯",
      "1 + 1 + 1 + ⋯"
    ],
    ans: 0,
    trick: "convergence needs the absolute value of the ratio to be strictly LESS than 1 — a ratio of exactly 1 does not converge either, and that boundary case is on the page",
    why: "36 ÷ 54 = 2/3, and |2/3| < 1.",
    traps: [
      "B: ratio 3/2, which is greater than 1.",
      "C: ratio 2.",
      "D: ratio exactly 1, so the partial sums grow without bound.",
    ],
  },
  {
    sig: "sum-of-an-infinite-geometric-series",
    code: "SAAT-M-ALG.93", ses: 58, lvl: 4,
    stem: "Find the sum of the infinite geometric series whose first term is 10 and whose ratio is 4/5.",
    opts: [
      "40",
      "50",
      "12.5",
      "2"
    ],
    ans: 1,
    trick: "the denominator is 1 − r, not r − 1 and not 1 + r — a ratio close to 1 makes the sum large, so an answer smaller than the first term is a sign the subtraction went the wrong way",
    why: "10 ÷ (1 − 4/5) = 10 ÷ (1/5) = 50.",
    traps: [
      "A: the first term multiplied by the ratio and by 5.",
      "C: 1 + r used in the denominator.",
      "D: the first term divided by the ratio.",
    ],
  },
  {
    sig: "number-of-terms-in-an-expansion",
    code: "SAAT-M-ALG.94", ses: 59, lvl: 2,
    stem: "How many terms are there in the expansion of (x + 3)⁵, and what is the coefficient of x⁴?",
    opts: [
      "6 terms, coefficient 5",
      "5 terms, coefficient 3",
      "6 terms, coefficient 15",
      "5 terms, coefficient 15"
    ],
    ans: 2,
    trick: "an expansion of power n has n + 1 terms, one more than the power — and the coefficient of the second term is n times the constant, here 5 × 3",
    why: "(x + 3)⁵ has six terms, and the x⁴ term is 5C1 · x⁴ · 3 = 15x⁴.",
    traps: [
      "A: the binomial coefficient given without the 3.",
      "B: both counts wrong.",
      "D: the number of terms taken as the power.",
    ],
  },
  {
    sig: "induction-what-to-prove-next",
    code: "SAAT-M-ALG.95", ses: 60, lvl: 4,
    stem: "In a proof by mathematical induction, after assuming the statement true for n = k, what must be proved?",
    opts: [
      "That the statement is true for every n",
      "That the statement is true for n = k − 1",
      "That the assumption for n = k was correct",
      "That the statement is true for n = k + 1"
    ],
    ans: 3,
    trick: "the induction step is a SINGLE step forward from the assumption — proving the general case directly is what induction is designed to avoid, and re-proving the assumption is circular",
    why: "The inductive step carries the truth from k to k + 1.",
    traps: [
      "A: that is the conclusion, not the step.",
      "B: induction moves forward, not backward.",
      "C: the assumption is granted, not proved.",
    ],
  },
  {
    sig: "equality-of-two-complex-numbers",
    code: "SAAT-M-ALG.96", ses: 61, lvl: 3,
    stem: "Find the real numbers x and y for which 5x + 1 + (3 + 2y)i = 2x − 2 + (y − 6)i.",
    opts: [
      "x = −1, y = −9",
      "x = 1, y = 9",
      "x = −1, y = 9",
      "x = −3, y = −3"
    ],
    ans: 0,
    trick: "two complex numbers are equal only when the real parts match AND the imaginary parts match — that gives TWO separate equations, and mixing a real term into the imaginary equation is the error",
    why: "5x + 1 = 2x − 2 gives x = −1; 3 + 2y = y − 6 gives y = −9.",
    traps: [
      "B: both signs reversed.",
      "C: the sign of y lost.",
      "D: the real and imaginary parts added together into one equation.",
    ],
  },
  {
    sig: "add-and-subtract-complex-numbers",
    code: "SAAT-M-ALG.97", ses: 61, lvl: 2,
    stem: "If z = 3 + 6i and w = 2i, find w − z.",
    opts: [
      { eq: "d_cws4" },
      { eq: "d_cws1" },
      { eq: "d_cws2" },
      { eq: "d_cws3" }
    ],
    ans: 1,
    trick: "subtracting a complex number subtracts BOTH parts — the real part of w is 0, so the answer's real part is −3, and reading w as having no real part at all is what leaves the 3 positive",
    why: "2i − (3 + 6i) = −3 − 4i.",
    traps: [
      "A: the imaginary parts added.",
      "C: the order of the subtraction reversed.",
      "D: the real part left positive.",
    ],
  },

  // ============================================================ UNIT 8
  {
    sig: "find-a-side-with-a-trig-ratio",
    code: "SAAT-M-TRI.7", ses: 64, lvl: 2,
    stem: "In a right triangle the hypotenuse measures 14 and one acute angle is 30°. What is the length of the side opposite that angle?",
    opts: [
      "28",
      "14√3",
      "7",
      "7√3"
    ],
    ans: 2,
    trick: "sin 30° = 1/2 exactly, so the opposite side is HALF the hypotenuse — reaching for cos 30° gives the other leg, which is the option beside it",
    why: "sin 30° = x/14 gives x = 7.",
    traps: [
      "A: the ratio inverted.",
      "B: the hypotenuse scaled by √3.",
      "D: the adjacent side found instead.",
    ],
  },
  {
    sig: "which-ratio-to-use",
    code: "SAAT-M-TRI.8", ses: 65, lvl: 2,
    stem: "In a right triangle you know the side adjacent to an acute angle and the hypotenuse, and you want the angle. Which ratio do you use?",
    opts: [
      "Sine",
      "Tangent",
      "Cotangent",
      "Cosine"
    ],
    ans: 3,
    trick: "match the ratio to the two sides you HAVE, not to the one you want — adjacent over hypotenuse is cosine, and tangent is the choice only when the hypotenuse is not involved at all",
    why: "cos θ = adjacent ÷ hypotenuse.",
    traps: [
      "A: sine uses the opposite side.",
      "B: tangent uses no hypotenuse.",
      "C: cotangent uses no hypotenuse either.",
    ],
  },
  {
    sig: "degrees-to-radians",
    code: "SAAT-M-TRI.9", ses: 67, lvl: 2,
    stem: "Convert 135° to radians.",
    opts: [
      { eq: "d_d2r1" },
      { eq: "d_d2r2" },
      { eq: "d_d2r3" },
      { eq: "d_d2r4" }
    ],
    ans: 0,
    trick: "multiply by π/180 to go INTO radians and by 180/π to come out — using the wrong one of the two leaves a π in the denominator, which is the visible sign of the error",
    why: "135 × π/180 = 3π/4.",
    traps: [
      "B: multiplied by 180/π instead.",
      "C: 135 divided by 180 without the π.",
      "D: the fraction not reduced.",
    ],
  },
  {
    sig: "r-from-a-point-on-the-terminal-side",
    code: "SAAT-M-TRI.10", ses: 69, lvl: 3,
    stem: "The point P(−8, 6) lies on the terminal side of an angle in standard position. What is sin θ?",
    opts: [
      { eq: "d_rts4" },
      { eq: "d_rts1" },
      { eq: "d_rts2" },
      { eq: "d_rts3" }
    ],
    ans: 1,
    trick: "r is a DISTANCE and is never negative, however negative the coordinates are — the sign of the ratio comes from the coordinate on top, not from r",
    why: "r = √(64 + 36) = 10, so sin θ = 6/10 = 3/5.",
    traps: [
      "A: the coordinates used without finding r.",
      "C: r taken as negative because x is.",
      "D: cos θ given instead.",
    ],
  },
  {
    sig: "cosine-from-sine-in-a-quadrant",
    code: "SAAT-M-TRI.11", ses: 69, lvl: 3,
    stem: "If sin θ = 2/3 and θ lies in the first quadrant, what is cos θ?",
    opts: [
      { eq: "d_csq3" },
      { eq: "d_csq4" },
      { eq: "d_csq1" },
      { eq: "d_csq2" }
    ],
    ans: 2,
    trick: "square, subtract from 1 and take the root — then let the QUADRANT choose the sign, which in the first quadrant is positive; taking 1 − 2/3 instead of 1 − (2/3)² is the standard slip",
    why: "cos²θ = 1 − 4/9 = 5/9, so cos θ = √5 ÷ 3.",
    traps: [
      "A: the sine subtracted from 1 without squaring.",
      "B: the sine and cosine assumed to add to 1.",
      "D: the negative root taken.",
    ],
  },

  // ============================================================ UNIT 9
  {
    sig: "sine-of-a-negative-angle",
    code: "SAAT-M-TRI.12", ses: 73, lvl: 2,
    stem: "Which statement below is an identity?",
    opts: [
      { eq: "d_neg2" },
      { eq: "d_neg3" },
      { eq: "d_neg4" },
      { eq: "d_neg1" }
    ],
    ans: 3,
    trick: "sine is ODD and cosine is EVEN — sin(−θ) reverses sign while cos(−θ) does not, and the option that reverses the cosine instead is always offered",
    why: "sin(−θ) = −sin θ for every θ.",
    traps: [
      "A: cosine is even, so the sign does not change.",
      "B: the sign kept on the sine.",
      "C: tangent is odd, so this sign is wrong too.",
    ],
  },
  {
    sig: "cofunction-identity",
    code: "SAAT-M-TRI.13", ses: 73, lvl: 3,
    stem: "Which expression equals sin θ for every θ?",
    opts: [
      { eq: "d_cof1" },
      { eq: "d_cof2" },
      { eq: "d_cof3" },
      { eq: "d_cof4" }
    ],
    ans: 0,
    trick: "the cofunction relation subtracts the angle from a RIGHT angle, not from a straight angle — using π instead of π/2 gives an identity that is true only for the sine's own reflection",
    why: "cos(π/2 − θ) = sin θ.",
    traps: [
      "B: π used instead of π/2.",
      "C: the sine and cosine interchanged in the wrong direction.",
      "D: the angle added rather than subtracted.",
    ],
  },
  {
    sig: "cos-double-angle-from-cosine",
    code: "SAAT-M-TRI.14", ses: 74, lvl: 3,
    stem: "If cos θ = 3/5, what is cos 2θ?",
    opts: [
      { eq: "d_cd4" },
      { eq: "d_cd1" },
      { eq: "d_cd2" },
      { eq: "d_cd3" }
    ],
    ans: 1,
    trick: "use the form 2cos²θ − 1, which needs the cosine ALONE — doubling the cosine itself is not a double angle, and 6/5 is outside the range of a cosine, which is the check that catches it",
    why: "2(9/25) − 1 = 18/25 − 1 = −7/25.",
    traps: [
      "A: the sine's double-angle formula used.",
      "C: the cosine simply doubled.",
      "D: the sign of the 1 mishandled.",
    ],
  },
  {
    sig: "solve-a-trig-equation-in-a-range",
    code: "SAAT-M-TRI.15", ses: 76, lvl: 4,
    stem: "Solve sin θ cos θ − ½ cos θ = 0 for 0° ≤ θ ≤ 180°.",
    opts: [
      "90° only",
      "30°, 90°, 150° and 270°",
      "30°, 90° and 150°",
      "30° and 150° only"
    ],
    ans: 2,
    trick: "factor the common cos θ out and set EACH factor to zero — dividing by cos θ instead throws away the solution θ = 90°, and that lost root is what the second option represents",
    why: "cos θ(sin θ − ½) = 0 gives θ = 90°, or sin θ = ½ giving θ = 30° or 150°.",
    traps: [
      "A: only the cosine factor solved.",
      "B: 270° included, which lies outside the stated range.",
      "D: the equation divided through by cos θ.",
    ],
  },
  {
    sig: "general-solution-of-a-trig-equation",
    code: "SAAT-M-TRI.16", ses: 76, lvl: 4,
    stem: "What is the general solution of cos θ + 1 = 0, with θ in radians?",
    opts: [
      { eq: "d_gen2" },
      { eq: "d_gen3" },
      { eq: "d_gen4" },
      { eq: "d_gen1" }
    ],
    ans: 3,
    trick: "cos θ = −1 happens once per FULL turn, so the period added is 2πk, not πk — halving the period doubles the solution set and brings in angles where the cosine is +1",
    why: "cos θ = −1 at θ = π, and the cosine has period 2π.",
    traps: [
      "A: a period of π used.",
      "B: the solution of cos θ = 1 given.",
      "C: the sine's solution given.",
    ],
  },
  {
    sig: "component-form-from-two-points",
    code: "SAAT-M-TRI.17", ses: 79, lvl: 2,
    stem: "A vector has initial point A(−4, 2) and terminal point B(3, −5). What is its component form?",
    opts: [
      { eq: "d_cmp1" },
      { eq: "d_cmp2" },
      { eq: "d_cmp3" },
      { eq: "d_cmp4" }
    ],
    ans: 0,
    trick: "TERMINAL minus INITIAL, in that order — reversing it gives the vector BA, which points the other way and is always among the options",
    why: "⟨3 − (−4), −5 − 2⟩ = ⟨7, −7⟩.",
    traps: [
      "B: initial minus terminal, giving BA.",
      "C: the coordinates added.",
      "D: the sign of the first subtraction lost.",
    ],
  },
  {
    sig: "unit-vector-in-the-same-direction",
    code: "SAAT-M-TRI.18", ses: 79, lvl: 3,
    stem: "Find the unit vector in the same direction as v = ⟨−2, 3⟩.",
    opts: [
      { eq: "d_uv4" },
      { eq: "d_uv1" },
      { eq: "d_uv2" },
      { eq: "d_uv3" }
    ],
    ans: 1,
    trick: "divide the vector by its own MAGNITUDE — dividing by the number of components, or by the larger component, gives a vector of the right direction and the wrong length",
    why: "|v| = √13, so the unit vector is ⟨−2/√13, 3/√13⟩.",
    traps: [
      "A: the components halved.",
      "C: divided by 13 rather than by its root.",
      "D: divided by the larger component.",
    ],
  },
  {
    sig: "components-from-magnitude-and-direction",
    code: "SAAT-M-TRI.19", ses: 79, lvl: 3,
    stem: "A vector of magnitude 10 makes an angle of 45° with the positive x-axis. What is its component form?",
    opts: [
      { eq: "d_md3" },
      { eq: "d_md4" },
      { eq: "d_md1" },
      { eq: "d_md2" }
    ],
    ans: 2,
    trick: "the x component uses COSINE and the y component uses SINE — at 45° they happen to be equal, so the real test is whether the magnitude was multiplied in at all",
    why: "⟨10 cos 45°, 10 sin 45°⟩ = ⟨5√2, 5√2⟩.",
    traps: [
      "A: the components given as 10 and 45.",
      "B: the magnitude divided rather than multiplied.",
      "D: the magnitude left out.",
    ],
  },
  {
    sig: "angle-between-two-vectors",
    code: "SAAT-M-TRI.20", ses: 79, lvl: 4,
    stem: "Find the angle between u = ⟨3, 1⟩ and v = ⟨3, −3⟩, to the nearest degree.",
    opts: [
      "27°",
      "45°",
      "117°",
      "63°"
    ],
    ans: 3,
    trick: "the dot product goes over the PRODUCT of the two magnitudes, and the answer is the inverse cosine of that — taking the inverse sine instead gives the complement, which is on the page",
    why: "cos θ = 6 ÷ (√10 · √18) ≈ 0.4472, so θ ≈ 63°.",
    traps: [
      "A: the inverse sine taken instead of the inverse cosine.",
      "B: the vectors assumed to be at 45° from their look.",
      "C: the supplement given.",
    ],
  },
  {
    sig: "cross-product-in-space",
    code: "SAAT-M-TRI.21", ses: 79, lvl: 4,
    stem: "Find u × v for u = ⟨3, −2, 1⟩ and v = ⟨−3, 3, 1⟩.",
    opts: [
      { eq: "d_cr1" },
      { eq: "d_cr2" },
      { eq: "d_cr3" },
      { eq: "d_cr4" }
    ],
    ans: 0,
    trick: "the middle component of a cross product carries a MINUS sign in front of its determinant — dropping it is the single error that produces every wrong option here",
    why: "⟨(−2)(1) − (1)(3), −[(3)(1) − (1)(−3)], (3)(3) − (−2)(−3)⟩ = ⟨−5, −6, 3⟩.",
    traps: [
      "B: the sign of the middle component dropped.",
      "C: the two vectors crossed in the other order.",
      "D: the dot product's components computed instead.",
    ],
  },
  {
    sig: "distance-between-two-polar-points",
    code: "SAAT-M-TRI.22", ses: 80, lvl: 4,
    stem: "Find the distance between the polar points M(2, 330°) and N(5, 60°).",
    opts: [
      { eq: "d_pol4" },
      { eq: "d_pol1" },
      { eq: "d_pol2" },
      { eq: "d_pol3" }
    ],
    ans: 1,
    trick: "use the law of cosines on the two radii with the DIFFERENCE of the angles between them — here that difference is 90°, so the cosine term vanishes and the answer is simply √(4 + 25)",
    why: "√(4 + 25 − 2·2·5·cos 90°) = √29.",
    traps: [
      "A: the cosine term kept as if the angle were 60°.",
      "C: the angles added rather than subtracted.",
      "D: the two radii simply subtracted.",
    ],
  },
  {
    sig: "modulus-of-a-complex-number",
    code: "SAAT-M-TRI.23", ses: 80, lvl: 2,
    stem: "What is the absolute value of the complex number z = −6 + 8i?",
    opts: [
      "14",
      "√2",
      "10",
      "2"
    ],
    ans: 2,
    trick: "the modulus is the ROOT of the sum of the squares, so the sign of the real part never survives — adding or subtracting the parts is what produces the two small options",
    why: "√(36 + 64) = 10.",
    traps: [
      "A: the two parts added without signs.",
      "B: the difference of the parts rooted.",
      "D: the two parts added with their signs.",
    ],
  },

  // ============================================================ UNIT 10
  {
    sig: "centre-and-radius-from-the-equation",
    code: "SAAT-M-GEO.53", ses: 82, lvl: 2,
    stem: "Find the centre and the radius of the circle whose equation is (x − 4)² + (y + 1)² = 9.",
    opts: [
      "Centre (−4, 1), radius 3",
      "Centre (4, −1), radius 9",
      "Centre (4, 1), radius 3",
      "Centre (4, −1), radius 3"
    ],
    ans: 3,
    trick: "the coordinates of the centre are the OPPOSITE of the signs inside the brackets, and the right side is r SQUARED — taking 9 as the radius is the other half of the same carelessness",
    why: "(x − 4)² + (y − (−1))² = 3² gives centre (4, −1) and radius 3.",
    traps: [
      "A: both signs read as they stand.",
      "B: r² taken as r.",
      "C: the sign of the y coordinate not reversed.",
    ],
  },
  {
    sig: "circle-from-the-ends-of-a-diameter",
    code: "SAAT-M-GEO.54", ses: 82, lvl: 4,
    stem: "Write the equation of the circle whose diameter has endpoints (7, 6) and (−1, −8).",
    opts: [
      { eq: "d_cd1e" },
      { eq: "d_cd2e" },
      { eq: "d_cd3e" },
      { eq: "d_cd4e" }
    ],
    ans: 0,
    trick: "the centre is the MIDPOINT and the radius is HALF the diameter — using the full distance between the two points as the radius quadruples the right-hand side",
    why: "Centre (3, −1); radius² = (3−7)² + (−1−6)² = 16 + 49 = 65.",
    traps: [
      "B: the whole diameter used as the radius.",
      "C: the signs of the centre not reversed in the brackets.",
      "D: the radius left unsquared.",
    ],
  },
  {
    sig: "direction-a-parabola-opens",
    code: "SAAT-M-GEO.55", ses: 83, lvl: 3,
    stem: "The equation of a parabola is (x − 6)² = −4(y − 15). Which way does it open, and where is its vertex?",
    opts: [
      "Downwards, vertex (−6, −15)",
      "Downwards, vertex (6, 15)",
      "Upwards, vertex (6, 15)",
      "To the left, vertex (6, 15)"
    ],
    ans: 1,
    trick: "the SQUARED variable tells you the axis — x squared means a vertical axis — and the sign of the coefficient on the other side tells you the direction",
    why: "x is squared, so the axis is vertical, and −4 < 0 opens it downwards; the vertex is (6, 15).",
    traps: [
      "A: the signs of the vertex not reversed.",
      "C: the minus sign overlooked.",
      "D: the squared variable read as y.",
    ],
  },
  {
    sig: "equation-from-focus-and-vertex",
    code: "SAAT-M-GEO.56", ses: 83, lvl: 4,
    stem: "A parabola has focus (3, −4) and vertex (1, −4). What is its equation?",
    opts: [
      { eq: "d_pf3" },
      { eq: "d_pf4" },
      { eq: "d_pf1" },
      { eq: "d_pf2" }
    ],
    ans: 2,
    trick: "the focus and vertex share a y coordinate, so the axis is HORIZONTAL and y is the squared variable — c is the distance from vertex to focus, here 2, and it is 4c that appears in the equation",
    why: "c = 3 − 1 = 2, so (y + 4)² = 8(x − 1).",
    traps: [
      "A: c used in place of 4c.",
      "B: the signs inside the brackets not reversed.",
      "D: x taken as the squared variable.",
    ],
  },
  {
    sig: "centre-axes-and-foci-of-an-ellipse",
    code: "SAAT-M-GEO.57", ses: 84, lvl: 4,
    stem: "For the ellipse (x − 3)²/36 + (y + 1)²/9 = 1, what are the centre, the length of the major axis and the value of c?",
    opts: [
      "Centre (3, −1), major axis 6, c = 3√3",
      "Centre (−3, 1), major axis 12, c = 3√5",
      "Centre (3, −1), major axis 12, c = 3√5",
      "Centre (3, −1), major axis 12, c = 3√3"
    ],
    ans: 3,
    trick: "a is the ROOT of the larger denominator and the major axis is 2a, not a — and for an ellipse c² = a² − b², a subtraction, while the hyperbola uses a sum",
    why: "a = 6, so the major axis is 12; c = √(36 − 9) = 3√3.",
    traps: [
      "A: the semi-axis given as the axis.",
      "B: the centre signs not reversed and the hyperbola's c used.",
      "C: c² taken as a² + b².",
    ],
  },
  {
    sig: "eccentricity-of-an-ellipse",
    code: "SAAT-M-GEO.58", ses: 84, lvl: 3,
    stem: "An ellipse has a = 5 and b = 4. What is its eccentricity?",
    opts: [
      "0.6",
      "1.25",
      "0.8",
      "1.67"
    ],
    ans: 0,
    trick: "eccentricity is c ÷ a and for an ellipse it always lies strictly between 0 and 1 — any answer above 1 belongs to a hyperbola and can be rejected on sight",
    why: "c = √(25 − 16) = 3, so e = 3/5 = 0.6.",
    traps: [
      "B: a divided by c.",
      "C: b divided by a.",
      "D: a divided by b.",
    ],
  },
  {
    sig: "centre-and-vertices-of-a-hyperbola",
    code: "SAAT-M-GEO.59", ses: 85, lvl: 4,
    stem: "For the hyperbola (x + 1)²/9 − (y + 2)²/16 = 1, what are the centre and the vertices?",
    opts: [
      "Centre (−1, −2), vertices (4, −2) and (−6, −2)",
      "Centre (−1, −2), vertices (2, −2) and (−4, −2)",
      "Centre (1, 2), vertices (4, 2) and (−2, 2)",
      "Centre (−1, −2), vertices (−1, 2) and (−1, −6)"
    ],
    ans: 1,
    trick: "the vertices lie along the axis of the POSITIVE term, at a distance a from the centre — with x positive here they move horizontally, and a is 3, not 4 and not 5",
    why: "Centre (−1, −2), a = 3, so the vertices are (−1 ± 3, −2).",
    traps: [
      "A: c used in place of a.",
      "C: the signs of the centre not reversed.",
      "D: the vertices moved along the y direction.",
    ],
  },
  {
    sig: "asymptotes-of-a-hyperbola",
    code: "SAAT-M-GEO.60", ses: 85, lvl: 4,
    stem: "What are the slopes of the asymptotes of the hyperbola (x + 1)²/9 − (y + 2)²/16 = 1?",
    opts: [
      { eq: "d_as3" },
      { eq: "d_as4" },
      { eq: "d_as1" },
      { eq: "d_as2" }
    ],
    ans: 2,
    trick: "for a hyperbola opening left and right the slopes are ± b over a, with a under the POSITIVE term — inverting the fraction is the error, and the inverted pair is on the page",
    why: "a = 3 and b = 4, so the slopes are ±4/3.",
    traps: [
      "A: the denominators used without their roots.",
      "B: only the positive slope given.",
      "D: the fraction inverted.",
    ],
  },
  {
    sig: "counterexample-to-a-claim",
    code: "SAAT-M-GEO.61", ses: 89, lvl: 3,
    stem: "A student claims that 2ⁿ + 2n² is divisible by 4 for every natural number n. Which value of n disproves the claim?",
    opts: [
      "1",
      "2",
      "4",
      "3"
    ],
    ans: 3,
    trick: "one counterexample is enough to kill a general claim, and the smallest cases are usually the ones that WORK — testing only n = 1 and n = 2 is what leaves the claim standing",
    why: "At n = 3: 8 + 18 = 26, and 26 is not divisible by 4.",
    traps: [
      "A: 2 + 2 = 4, which is divisible by 4.",
      "B: 4 + 8 = 12, which is divisible by 4.",
      "C: 16 + 32 = 48, which is divisible by 4.",
    ],
  },
  {
    sig: "always-sometimes-or-never",
    code: "SAAT-M-GEO.62", ses: 89, lvl: 3,
    stem: "Three points J, K and L satisfy JK = KL. Which description of the statement 'K is the midpoint of JL' is correct?",
    opts: [
      "Sometimes true — it fails whenever the three points are not collinear",
      "Always true, because the two distances are equal",
      "Never true, because equal distances do not define a midpoint",
      "Always true, provided the three points are distinct"
    ],
    ans: 0,
    trick: "a midpoint needs the point to be BETWEEN the other two, and equal distances alone do not force that — the apex of an isosceles triangle is the counterexample that decides the question",
    why: "If J, K and L form an isosceles triangle then JK = KL but K is not on JL.",
    traps: [
      "B: equal distances do not imply collinearity.",
      "C: when the points are collinear the statement is true.",
      "D: distinctness does not make the points collinear.",
    ],
  },

  // ============================================================ UNITS 11–13
  {
    sig: "one-sided-limits-agree",
    code: "SAAT-M-CAL.10", ses: 91, lvl: 3,
    stem: "A function g is 4 everywhere except at x = −3, where g(−3) = −2. What is the limit of g(x) as x approaches −3?",
    opts: [
      "The limit does not exist",
      "4",
      "−2",
      "1"
    ],
    ans: 1,
    trick: "a limit describes the values NEAR the point, never the value AT it — a function may be defined at a point by something entirely different and the limit is untouched",
    why: "Both one-sided limits equal 4, so the limit is 4.",
    traps: [
      "A: the limit exists whenever the one-sided limits agree, whatever happens at the point.",
      "C: the value of the function at the point given.",
      "D: the two numbers averaged.",
    ],
  },
  {
    sig: "limit-by-factoring",
    code: "SAAT-M-CAL.11", ses: 91, lvl: 3,
    stem: "Evaluate the limit below.",
    stemEq: "d_lf",
    opts: [
      "1",
      "The limit does not exist",
      "2",
      "0"
    ],
    ans: 2,
    trick: "the 0/0 form is an instruction to FACTOR, not a verdict — cancelling the common factor leaves an expression that is perfectly well behaved at the point",
    why: "(x² − 1)/(x − 1) = x + 1 for x ≠ 1, and 1 + 1 = 2.",
    traps: [
      "A: the numerator and denominator each evaluated and then divided as 0/0 → 1.",
      "B: the indeterminate form taken as a verdict.",
      "D: the numerator's value at 1 given.",
    ],
  },
  {
    sig: "three-conditions-for-continuity",
    code: "SAAT-M-CAL.12", ses: 92, lvl: 3,
    stem: "Which three conditions must hold for f to be continuous at x = c?",
    opts: [
      "f(c) exists and the limit at c exists",
      "The limit at c exists and f is differentiable at c",
      "f(c) exists and f is increasing at c",
      "f(c) exists, the limit at c exists, and the two are equal"
    ],
    ans: 3,
    trick: "the third condition is the one that is dropped — a function can be defined at c AND have a limit there while the two disagree, which is exactly a removable discontinuity",
    why: "Continuity at c requires f(c) defined, the limit to exist, and the limit to equal f(c).",
    traps: [
      "A: the two may exist and differ, giving a hole.",
      "B: differentiability is a stronger condition, not one of the three.",
      "C: monotonicity has nothing to do with continuity.",
    ],
  },
  {
    sig: "limit-at-infinity-by-degree",
    code: "SAAT-M-CAL.13", ses: 93, lvl: 3,
    stem: "For a rational function whose numerator has degree 2 and whose denominator has degree 3, what is the limit as x tends to infinity?",
    opts: [
      "0",
      "Infinity",
      "The ratio of the leading coefficients",
      "It cannot be decided from the degrees alone"
    ],
    ans: 0,
    trick: "compare the DEGREES: bottom-heavy gives 0, equal degrees give the ratio of the leading coefficients, top-heavy gives infinity — three cases, and the middle one is the one usually applied by mistake",
    why: "The denominator grows faster, so the quotient tends to 0.",
    traps: [
      "B: the top-heavy case.",
      "C: the equal-degree case.",
      "D: the degrees decide it completely.",
    ],
  },
  {
    sig: "asymptotes-of-a-shifted-reciprocal",
    code: "SAAT-M-CAL.14", ses: 93, lvl: 3,
    stem: "For the function y = 1/(x − 2) + 1, what are the vertical and horizontal asymptotes?",
    opts: [
      "x = 1 and y = 2",
      "x = 2 and y = 1",
      "x = −2 and y = 1",
      "x = 2 and y = 0"
    ],
    ans: 1,
    trick: "the vertical asymptote is where the DENOMINATOR is zero, so its sign is the opposite of the one written; the horizontal one is the constant added on the outside, not zero",
    why: "x − 2 = 0 gives x = 2, and the +1 lifts the horizontal asymptote to y = 1.",
    traps: [
      "A: the two constants interchanged.",
      "C: the sign of the shift not reversed.",
      "D: the outside constant ignored.",
    ],
  },
  {
    sig: "a-hole-not-an-asymptote",
    code: "SAAT-M-CAL.15", ses: 93, lvl: 4,
    stem: "The function f(x) = (x² − 16)/(x − 4) has what feature at x = 4?",
    opts: [
      "A horizontal asymptote at y = 8",
      "Nothing unusual; the function is defined there",
      "A hole, because the factor cancels",
      "A vertical asymptote, because the denominator is zero"
    ],
    ans: 2,
    trick: "a zero denominator is not automatically an asymptote — if the same factor cancels from the numerator the graph is a straight line with a single point missing",
    why: "(x − 4)(x + 4)/(x − 4) = x + 4 for x ≠ 4, so the graph is the line y = x + 4 with a hole at (4, 8).",
    traps: [
      "A: the y value at the hole read as a horizontal asymptote.",
      "B: the function is still undefined at x = 4.",
      "D: true only when the factor does not cancel.",
    ],
  },
  {
    sig: "derivative-from-first-principles",
    code: "SAAT-M-CAL.16", ses: 94, lvl: 4,
    stem: "Using the limit definition, find f′(x) for f(x) = 4x² − 5x + 8, and then f′(1.5).",
    opts: [
      "f′(x) = 8x − 5, and f′(1.5) = 12",
      "f′(x) = 8x + 5, and f′(1.5) = 17",
      "f′(x) = 4x − 5, and f′(1.5) = 1",
      "f′(x) = 8x − 5, and f′(1.5) = 7"
    ],
    ans: 3,
    trick: "the constant vanishes and the linear term keeps its own sign — the difference quotient leaves 8x + 4h − 5, and it is the 4h that goes to zero, not the 5",
    why: "f′(x) = 8x − 5, so f′(1.5) = 12 − 5 = 7.",
    traps: [
      "A: the derivative right but the constant not subtracted.",
      "B: the sign of the linear term reversed.",
      "C: the 2 in the exponent not brought down.",
    ],
  },
  {
    sig: "average-rate-over-an-interval-in-context",
    code: "SAAT-M-CAL.17", ses: 100, lvl: 3,
    stem: "A runner's distance in kilometres after t hours is f(t) = −1.3t² + 12t. What is the average speed between t = 2 and t = 3?",
    opts: [
      "5.5 km/h",
      "18.8 km/h",
      "24.3 km/h",
      "11 km/h"
    ],
    ans: 0,
    trick: "average rate is the CHANGE in distance over the CHANGE in time — reporting one of the two distances instead is what the two large options are for",
    why: "f(2) = 18.8 and f(3) = 24.3, so the average speed is (24.3 − 18.8)/(3 − 2) = 5.5.",
    traps: [
      "B: the distance at t = 2 given.",
      "C: the distance at t = 3 given.",
      "D: the difference doubled.",
    ],
  },
  {
    sig: "area-under-a-curve-on-an-interval",
    code: "SAAT-M-CAL.18", ses: 115, lvl: 4,
    stem: "Find the area of the region bounded by y = 4x³, the x-axis and the lines x = 1 and x = 3.",
    opts: [
      "40",
      "80",
      "26",
      "108"
    ],
    ans: 1,
    trick: "integrate and then subtract the value at the LOWER limit — forgetting that subtraction leaves the value at the upper limit alone, which is the largest option",
    why: "∫₁³ 4x³ dx = [x⁴]₁³ = 81 − 1 = 80.",
    traps: [
      "A: the antiderivative taken as x⁴/4 with the 4 divided twice.",
      "C: the integrand evaluated rather than integrated.",
      "D: only the upper limit substituted.",
    ],
  },
];
