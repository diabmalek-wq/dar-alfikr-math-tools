// PART K of the SAAT booklet — the Tahsili revision compilation.
//
// Same rule as every other source: read for the SKILL and the TRICK only. No
// stem, number set, option list or figure is reproduced. Every stem is newly
// worded, every number set is new, every answer re-derived in verify_saat_k.py,
// and the four figures are drawn from scratch in make_figs_saat_k.py.
//
// The source holds about 216 items and skews heavily to the routine band the
// bank already covers — its geometry in particular is repetitive midsegment and
// angle-chase drill. Only about a tenth of it was worth anything, which is why
// this part is twenty-five items rather than a hundred. What it did carry:
//
//   · THE FLOOR FUNCTION, which the bank had nowhere — and the floor of a
//     NEGATIVE number, which goes down, away from zero.
//   · TRAPS THE ALGEBRA SETS AND THE DOMAIN THEN KILLS — a trig equation whose
//     only root is where the functions are undefined; a composite domain whose
//     exclusion has to be traced back through the inner function; a division
//     whose restrictions come from the divisor's NUMERATOR once it is flipped.
//   · WORK THAT DISAPPEARS IF YOU LOOK FIRST — a radical that collapses to a
//     quadratic before differentiating, an average rate that is zero by
//     symmetry, a limit that is not indeterminate at all, and a composition
//     whose outer function is constant.
//   · TWO SAUDI HOOKS — a Hijri-year span, where counting the years rather than
//     reading the year numbers is the whole item, and a big wheel on the
//     coordinate axes giving a polar circle.
//
// The source's printed answer strip is NOT reliable: at least six of its keys
// contradict the mathematics, two items are broken outright, and one item is
// keyed two different ways in two places. Nothing here trusts it.

module.exports = [
  // ==================================================== THE FLOOR FUNCTION
  {
    sig: "floor-of-a-negative-value",
    code: "SAAT-M-ALG.176", ses: 21, lvl: 4,
    stem: "For the function below, what is f(−7)?",
    stemEq: "kx_floor",
    opts: [
      "−1",
      "0",
      "1",
      "−3"
    ],
    ans: 0,
    trick: "the floor of a NEGATIVE number goes DOWN, away from zero — ⌊−2.8⌋ is −3 and not −2, and simply chopping the decimal off is the commonest error on the page",
    why: "0.4(−7) = −2.8, and ⌊−2.8⌋ = −3, so f(−7) = −3 + 2 = −1.",
    traps: [
      "B: the decimal chopped off instead of floored, giving −2.",
      "C: the value rounded to the nearest whole number.",
      "D: the floor reported with the +2 never added.",
    ],
  },
  {
    sig: "range-of-a-floor-function",
    code: "SAAT-M-ALG.177", ses: 20, lvl: 4,
    stem: "What is the range of g(x) = ⌊|x|⌋ + 5?",
    opts: [
      "All real numbers",
      "All integers greater than or equal to 5",
      "All real numbers greater than or equal to 5",
      "All integers greater than or equal to 0"
    ],
    ans: 1,
    trick: "the floor of anything is an INTEGER, so the range is a set of whole numbers and not an interval — the +5 lifts the set but does not change what kind of numbers are in it",
    why: "⌊|x|⌋ takes every value in {0, 1, 2, …}, so the sum takes every integer from 5 upwards.",
    traps: [
      "A: neither restriction applied.",
      "C: the integer condition dropped, leaving an interval.",
      "D: the +5 never applied.",
    ],
  },

  // ============================================ VECTORS, ANGLES AND MODELLING
  {
    sig: "components-recombine-to-the-force",
    code: "SAAT-M-ALG.178", ses: 79, lvl: 4,
    stem: "A force F is resolved into a horizontal and a vertical component, as shown. Which statement is true for EVERY angle θ?",
    fig: "kx_force_res", figW: 2.0,
    opts: [
      "Each component is less than half of F",
      "The horizontal component is always the larger",
      "The two components combine by Pythagoras to give F",
      "The two components add to F"
    ],
    ans: 2,
    trick: "the two components are at RIGHT ANGLES, so they recombine by Pythagoras and never by ordinary addition — their arithmetic sum is always larger than F, which is exactly why the adding option cannot be right",
    why: "(F cos θ)² + (F sin θ)² = F², so the components always rebuild F.",
    traps: [
      "A: at a small angle the horizontal component is nearly all of F.",
      "B: past 45° the vertical component is the larger.",
      "D: adding them ignores that they are perpendicular.",
    ],
  },
  {
    sig: "angular-displacement-over-time",
    code: "SAAT-M-TRI.63", ses: 67, lvl: 4,
    stem: "A wheel turns steadily and completes one full revolution every 9 hours. Through what angle, in radians, does it turn in 6 hours?",
    opts: [
      { eq: "kx_ad2" },
      { eq: "kx_ad3" },
      { eq: "kx_ad4" },
      { eq: "kx_ad1" }
    ],
    ans: 3,
    trick: "a full turn is 2π, so the angle is the FRACTION of the period times 2π — the fraction is time over period, and turning it upside down is what two of the options are built on",
    why: "(6/9)(2π) = (2/3)(2π) = 4π/3.",
    traps: [
      "A: the fraction taken as one third.",
      "B: the fraction inverted, 9 over 6.",
      "C: the period ignored and the hours multiplied by a full turn.",
    ],
  },
  {
    sig: "displacement-is-not-distance",
    code: "SAAT-M-ALG.181", ses: 79, lvl: 3,
    stem: "A runner goes 8 km north and then 6 km east, as shown. How far is she from her starting point?",
    fig: "kx_walk", figW: 1.7,
    opts: [
      "10 km",
      "14 km",
      "8 km",
      "2 km"
    ],
    ans: 0,
    trick: "how FAR from the start is the straight-line displacement, not the distance run — adding the two legs answers a different question, and that sum is the option placed beside the answer",
    why: "√(8² + 6²) = √100 = 10.",
    traps: [
      "B: the two legs added, which is the distance run.",
      "C: the longer leg alone.",
      "D: the two legs subtracted.",
    ],
  },
  {
    sig: "polar-equation-from-a-worded-circle",
    code: "SAAT-M-TRI.64", ses: 80, lvl: 4,
    stem: "A big wheel touches the ground at the origin and its highest point is (0, 30), as shown. What is its polar equation?",
    fig: "kx_wheel", figW: 1.6,
    opts: [
      { eq: "kx_w4" },
      { eq: "kx_w1" },
      { eq: "kx_w2" },
      { eq: "kx_w3" }
    ],
    ans: 1,
    trick: "for a circle through the pole the coefficient is the DIAMETER, and a circle sitting ABOVE the axis takes the sine — the two decisions are independent, and the four options cover all four combinations",
    why: "The centre is (0, 15) and the radius 15, so the diameter is 30 and r = 30 sin θ.",
    traps: [
      "A: both decisions taken the wrong way.",
      "C: the radius used where the diameter belongs.",
      "D: the cosine used, which puts the circle beside the pole.",
    ],
  },
  {
    sig: "hijri-year-span-in-compound-growth",
    code: "SAAT-M-ALG.180", ses: 53, lvl: 4,
    stem: "A school had 256 students in 1442 AH and its roll grows by 25% each year. How many students does it have in 1445 AH?",
    opts: [
      "320",
      "512",
      "500",
      "400"
    ],
    ans: 2,
    trick: "count the YEARS, not the year numbers — 1445 minus 1442 is three steps of growth, and taking it as two is the error the second option is built on",
    why: "256(1.25)³ = 256 × 125/64 = 500.",
    traps: [
      "A: only one year applied.",
      "B: the growth taken as a doubling across the whole span.",
      "D: only two years of growth applied.",
    ],
  },

  // ==================================================== PLANE GEOMETRY
  {
    sig: "two-reflections-in-parallel-lines",
    code: "SAAT-M-GEO.108", ses: 40, lvl: 4,
    stem: "A figure is reflected in a line, and its image is then reflected in a second line parallel to the first. What single transformation has the same effect?",
    opts: [
      "A rotation",
      "A reflection",
      "A dilation",
      "A translation"
    ],
    ans: 3,
    trick: "two reflections in PARALLEL lines slide the figure without turning it, through twice the gap between the lines — it is two reflections in INTERSECTING lines that give a rotation",
    why: "Reflecting twice in parallel lines translates the figure by twice the distance between them.",
    traps: [
      "A: that is what two INTERSECTING lines give.",
      "B: one reflection reverses orientation; two restore it.",
      "C: no reflection changes size.",
    ],
  },
  {
    sig: "which-value-cannot-be-an-exterior-angle",
    code: "SAAT-M-GEO.109", ses: 29, lvl: 4,
    stem: "A triangle has two angles of 55° and 65°. Which of these can NOT be one of its exterior angles?",
    opts: [
      "130°",
      "125°",
      "115°",
      "120°"
    ],
    ans: 0,
    trick: "find the THIRD angle first, then the three exterior angles are simply its three supplements — the question is negative, so three of the four values will be on that list",
    why: "The third angle is 60°, so the exterior angles are 125°, 115° and 120°.",
    traps: [
      "B: 125° is the supplement of 55°.",
      "C: 115° is the supplement of 65°.",
      "D: 120° is the supplement of the third angle.",
    ],
  },
  {
    sig: "counterexample-from-a-figure",
    code: "SAAT-M-GEO.110", ses: 28, lvl: 4,
    stem: "Which diagram below is a counterexample to the claim \"adjacent angles are always complementary\"?",
    fig: "kx_adj_cases", figW: 3.1,
    opts: [
      "B",
      "C",
      "D",
      "A"
    ],
    ans: 1,
    trick: "a counterexample has to show adjacent angles that do NOT add to 90° — three of these four add to exactly 90°, so they support the claim rather than refuting it",
    why: "In C the two angles are 65° and 70°, which add to 135°, not 90°.",
    traps: [
      "A: 55° and 35° add to 90°.",
      "C: 25° and 65° add to 90°.",
      "D: 40° and 50° add to 90°, which supports the claim.",
    ],
  },
  {
    sig: "smallest-integer-third-side",
    code: "SAAT-M-GEO.112", ses: 29, lvl: 3,
    stem: "Two sides of a triangle measure 11 cm and 4 cm. What is the smallest WHOLE-NUMBER length the third side can have?",
    opts: [
      "15 cm",
      "6 cm",
      "8 cm",
      "7 cm"
    ],
    ans: 2,
    trick: "the third side must be strictly GREATER than the difference, so the difference itself is not allowed — the smallest whole number that works is one more than it",
    why: "The third side satisfies 7 < n < 15, so the smallest whole number is 8.",
    traps: [
      "A: the sum used, which is the upper bound.",
      "B: a value below the difference.",
      "D: the difference itself taken, which gives a flat triangle.",
    ],
  },
  {
    sig: "dilation-with-a-negative-factor",
    code: "SAAT-M-GEO.113", ses: 40, lvl: 3,
    stem: "The point (−6, 4) is dilated about the origin by a scale factor of −1/2. What is its image?",
    opts: [
      { eq: "kx_dl2" },
      { eq: "kx_dl3" },
      { eq: "kx_dl4" },
      { eq: "kx_dl1" }
    ],
    ans: 3,
    trick: "a NEGATIVE scale factor halves the distance AND sends the point through the origin to the opposite side, so both coordinates change sign as well as size",
    why: "(−6, 4) × (−1/2) = (3, −2).",
    traps: [
      "A: the sign of the factor ignored.",
      "B: the sign applied to the x coordinate only.",
      "C: the sign applied to the y coordinate only.",
    ],
  },

  // ================================== WHAT THE ALGEBRA SETS AND THE DOMAIN KILLS
  {
    sig: "restrictions-from-the-divisor-when-dividing",
    code: "SAAT-M-ALG.182", ses: 7, lvl: 4,
    stem: "For which values of x is the quotient below undefined?",
    stemEq: "kx_div",
    opts: [
      "2, 3 and −3",
      "2 and −3",
      "3 and −3",
      "2 only"
    ],
    ans: 0,
    trick: "dividing means multiplying by the RECIPROCAL, so the second fraction's NUMERATOR moves to the bottom — its zeros are excluded too, and those are the ones everybody misses",
    why: "x − 2 ≠ 0 gives x ≠ 2; flipping the divisor puts x² − 9 underneath, so x ≠ 3 and x ≠ −3.",
    traps: [
      "B: the flipped numerator's zeros not excluded.",
      "C: the first denominator's zero forgotten.",
      "D: only the first denominator checked at all.",
    ],
  },
  {
    sig: "composite-domain-with-a-hidden-exclusion",
    code: "SAAT-M-ALG.183", ses: 25, lvl: 4,
    stem: "For f(x) = 1 ÷ (x − 4) and g(x) = √(x + 5), what is the domain of f∘g?",
    opts: [
      "All real numbers except 4",
      "x ≥ −5 and x ≠ 11",
      "x ≥ −5",
      "x ≥ −5 and x ≠ 4"
    ],
    ans: 1,
    trick: "the inner function's own restriction comes first, and THEN the value that makes the outer denominator vanish has to be traced back through the inner function — it is not 4, it is the x whose square root IS 4",
    why: "x + 5 ≥ 0 gives x ≥ −5, and √(x + 5) = 4 at x = 11, which must be excluded.",
    traps: [
      "A: the inner restriction overlooked entirely.",
      "C: the outer function's exclusion never traced back.",
      "D: the outer exclusion applied to x directly.",
    ],
  },
  {
    sig: "trig-equation-with-no-solution",
    code: "SAAT-M-TRI.65", ses: 76, lvl: 4,
    stem: "Solve sec θ − tan θ = 0 for 0 ≤ θ < 2π.",
    opts: [
      "θ = 0",
      "θ = π/2 and θ = 3π/2",
      "No solution",
      "θ = π/2"
    ],
    ans: 2,
    trick: "the algebra produces θ = π/2, but the secant and the tangent are both UNDEFINED there — a root the domain kills is not a solution, and it is sitting in the option right below the answer",
    why: "(1 − sin θ)/cos θ = 0 needs sin θ = 1, so θ = π/2; but cos(π/2) = 0, where neither function exists.",
    traps: [
      "A: cos θ = 1 solved instead.",
      "B: both roots of sin θ = ±1 kept.",
      "D: the root kept without checking where the functions live.",
    ],
  },

  // ======================================= WORK THAT DISAPPEARS IF YOU LOOK FIRST
  {
    sig: "average-rate-zero-by-symmetry",
    code: "SAAT-M-CAL.63", ses: 94, lvl: 4,
    stem: "What is the average rate of change of f(x) = x² − 6x + 5 between x = 1 and x = 5?",
    opts: [
      "1",
      "−1",
      "4",
      "0"
    ],
    ans: 3,
    trick: "the interval is symmetric about the vertex at x = 3, so the two end values are EQUAL and the rate is zero — spotting the axis of symmetry answers this without evaluating anything at all",
    why: "f(1) = 0 and f(5) = 0, so the rate is 0/4 = 0.",
    traps: [
      "A: the difference of the inputs used.",
      "B: that difference with the sign reversed.",
      "C: the width of the interval given.",
    ],
  },
  {
    sig: "composition-with-a-constant-outer-function",
    code: "SAAT-M-ALG.179", ses: 25, lvl: 3,
    stem: "For f(x) = 4x² − 3x and g(x) = 7, what is (g∘f)(x)?",
    opts: [
      { eq: "kx_cp1" },
      { eq: "kx_cp2" },
      { eq: "kx_cp3" },
      { eq: "kx_cp4" }
    ],
    ans: 0,
    trick: "g sends EVERY input to 7, so whatever f produces, g flattens it — the outer function never looks at its input, and three of the options are what you get by forgetting that",
    why: "g(anything) = 7, so (g∘f)(x) = 7.",
    traps: [
      "B: the inner function returned instead.",
      "C: the constant multiplied through rather than substituted.",
      "D: the composition done the other way round, at x = 7.",
    ],
  },
  {
    sig: "simplify-the-radical-before-differentiating",
    code: "SAAT-M-CAL.67", ses: 95, lvl: 4,
    stem: "Differentiate the function below.",
    stemEq: "kx_rad",
    opts: [
      { eq: "kx_rd4" },
      { eq: "kx_rd1" },
      { eq: "kx_rd2" },
      { eq: "kx_rd3" }
    ],
    ans: 1,
    trick: "simplify the radical FIRST — a fourth root of x to the minus eight is x to the minus two, so the whole function is a plain quadratic and the power rule finishes it in one line",
    why: "⁴√(x⁻⁸) = x⁻², so f(x) = x²/3 and f′(x) = 2x/3.",
    traps: [
      "A: the simplified function returned, not its derivative.",
      "C: differentiated without simplifying first.",
      "D: the unsimplified function returned.",
    ],
  },
  {
    sig: "substitution-works-not-indeterminate",
    code: "SAAT-M-CAL.65", ses: 91, lvl: 4,
    stem: "Find the limit below.",
    stemEq: "kx_lim",
    opts: [
      { eq: "kx_lm3" },
      { eq: "kx_lm4" },
      { eq: "kx_lm1" },
      { eq: "kx_lm2" }
    ],
    ans: 2,
    trick: "check for 0/0 BEFORE reaching for any technique — the denominator here is −1, not 0, so plain substitution finishes it, and treating a limit that is not indeterminate as though it were gives a wrong answer",
    why: "At x = 0 the value is π ÷ cos π = π ÷ (−1) = −π.",
    traps: [
      "A: the numerator read as x alone.",
      "B: only the denominator evaluated.",
      "D: the sign of cos π lost.",
    ],
  },
  {
    sig: "limit-versus-the-function-value",
    code: "SAAT-M-CAL.66", ses: 91, lvl: 4,
    stem: "For a function f the limit from the left at x = 2 is 5, the limit from the right at x = 2 is −5, and f(2) = 9. What is the limit of f as x approaches 2?",
    opts: [
      "9",
      "0",
      "5",
      "It does not exist"
    ],
    ans: 3,
    trick: "a two-sided limit exists only when the two one-sided limits AGREE, and the value of f at the point has nothing whatever to do with it — the 9 is in the question purely to be picked",
    why: "The one-sided limits are 5 and −5, which differ, so the limit does not exist.",
    traps: [
      "A: the function's value at the point given.",
      "B: the two one-sided limits averaged.",
      "C: the left-hand limit given.",
    ],
  },
  {
    sig: "name-the-type-of-discontinuity",
    code: "SAAT-M-CAL.64", ses: 92, lvl: 4,
    stem: "The function below is discontinuous at x = 3. What kind of discontinuity is it?",
    stemEq: "kx_disc",
    opts: [
      "Jump",
      "Removable",
      "Infinite",
      "None — the function is continuous there"
    ],
    ans: 0,
    trick: "both one-sided limits are FINITE but they disagree, which is a jump — a removable one needs them to be equal, and an infinite one needs at least one of them to run away",
    why: "The left limit is 9 − 5 = 4 and the right limit is 6; both finite, and unequal.",
    traps: [
      "B: a removable discontinuity needs the two one-sided limits to agree.",
      "C: an infinite one needs a one-sided limit to be unbounded.",
      "D: the two branches do not meet at 3.",
    ],
  },
  {
    sig: "coefficient-from-an-absolute-value-integral",
    code: "SAAT-M-CAL.62", ses: 114, lvl: 4,
    stem: "For which value of k does the integral below equal 36?",
    stemEq: "kx_abs",
    opts: [
      "36",
      "4",
      "8",
      "9"
    ],
    ans: 1,
    trick: "the graph of an absolute value over this interval is TWO triangles, so the integral is an area you can read straight off — antidifferentiating through the corner is where the sign errors come from",
    why: "The two triangles have area 4.5 each, so ∫|x − 1| dx = 9 and 9k = 36 gives k = 4.",
    traps: [
      "A: the value of the integral copied out.",
      "C: only one of the two triangles counted.",
      "D: the area itself reported as k.",
    ],
  },

  // ==================================================== ALGEBRA, SEEN PROPERLY
  {
    sig: "difference-of-squares-in-a-radical",
    code: "SAAT-M-ALG.184", ses: 3, lvl: 4,
    stem: "Simplify the expression below.",
    stemEq: "kx_dos",
    opts: [
      { eq: "kx_ds3" },
      { eq: "kx_ds4" },
      { eq: "kx_ds1" },
      { eq: "kx_ds2" }
    ],
    ans: 2,
    trick: "read x as the SQUARE of √x and the numerator becomes a difference of squares in √x — the factor then cancels outright, and nothing has to be rationalised at all",
    why: "x − 9 = (√x − 3)(√x + 3), so the quotient is √x + 3.",
    traps: [
      "A: the root dropped after cancelling.",
      "B: the reciprocal taken.",
      "D: the wrong factor cancelled.",
    ],
  },
  {
    sig: "exponential-with-an-added-constant",
    code: "SAAT-M-ALG.185", ses: 47, lvl: 4,
    stem: "Solve the equation below.",
    stemEq: "kx_exp",
    opts: [
      "3",
      "2",
      "64",
      "4"
    ],
    ans: 3,
    trick: "isolate the POWER before touching the exponent, then write both sides to the same base — 64 is 4³, so the exponent is 3 and x is one MORE than that",
    why: "4^(x−1) = 70 − 6 = 64 = 4³, so x − 1 = 3 and x = 4.",
    traps: [
      "A: the exponent x − 1 given instead of x.",
      "B: the shift applied the wrong way round.",
      "C: the power itself reported.",
    ],
  },
  {
    sig: "values-for-which-a-series-converges",
    code: "SAAT-M-ALG.186", ses: 58, lvl: 4,
    stem: "For which values of x does the infinite series below converge?",
    stemEq: "kx_ser",
    opts: [
      { eq: "kx_sr1" },
      { eq: "kx_sr2" },
      { eq: "kx_sr3" },
      { eq: "kx_sr4" }
    ],
    ans: 0,
    trick: "find the RATIO of consecutive terms, which is 2x and not x — an infinite geometric series converges when the SIZE of the ratio is under 1, so the bound on x is halved",
    why: "The ratio is 2x, and |2x| < 1 gives |x| < 1/2.",
    traps: [
      "B: the ratio taken as x alone.",
      "C: the bound inverted.",
      "D: the first term used as the ratio.",
    ],
  },
];
