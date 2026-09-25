// PART I of the SAAT booklet — the eleventh ETEC sample paper.
//
// Same rule as every other part: the paper was read for the SKILL and the
// TRICK only. No stem, number set, option list or figure is reproduced. Every
// stem is newly worded in English, every number set is new, every answer
// re-derived, and the four figures are drawn from scratch in
// make_figs_saat_i.py.
//
// Twenty-seven distinct items were read. Twelve tested skills the bank already
// held — the vertical line test, amplitude and period, the area rule, a
// counterexample to a false identity, conditional probability without
// replacement, a permutation equation, a complex fraction, a quotient by a
// conjugate, the gambler's fallacy and so on — and were dropped rather than
// repeated. The fifteen below are what was genuinely new.
//
// The paper's own shape is worth recording: trigonometry took nine of its
// first fourteen items, and counting-based probability six of the last
// thirteen. Those are the two places a Tahsili candidate loses marks fastest.
//
// Every answer is re-derived independently in verify_saat_i.py.

module.exports = [
  // =============================================== FUNCTIONS AND EXPRESSIONS
  {
    sig: "expand-a-horizontally-shifted-quadratic",
    code: "SAAT-M-ALG.165", ses: 23, lvl: 3,
    stem: "For f(x) = x², write f(x − 4) in expanded form.",
    opts: [
      { eq: "i_sh1" },
      { eq: "i_sh2" },
      { eq: "i_sh3" },
      { eq: "i_sh4" }
    ],
    ans: 0,
    trick: "replacing x by x − 4 moves the graph RIGHT, and squaring the bracket keeps a middle term — losing that middle term is the commonest slip, and two of the options are built on it",
    why: "(x − 4)² = x² − 8x + 16.",
    traps: [
      "B: the shift taken in the wrong direction.",
      "C: the bracket squared term by term, keeping the minus.",
      "D: the bracket squared term by term.",
    ],
  },
  {
    sig: "which-expression-is-not-rational",
    code: "SAAT-M-ALG.166", ses: 7, lvl: 4,
    stem: "Which of these is NOT a rational expression?",
    opts: [
      { eq: "i_nr4" },
      { eq: "i_nr1" },
      { eq: "i_nr2" },
      { eq: "i_nr3" }
    ],
    ans: 1,
    trick: "a rational expression is one polynomial over another, and a polynomial may carry ANY real coefficients — a surd multiplying x is perfectly legal; a surd OF x is not, because its exponent is a half",
    why: "√x has exponent 1/2, so the numerator is not a polynomial.",
    traps: [
      "A: a constant numerator, which is a polynomial of degree zero.",
      "C: a surd COEFFICIENT, which a polynomial is allowed to have.",
      "D: a high degree, which changes nothing.",
    ],
  },
  {
    sig: "radical-inequality-from-a-shaded-graph",
    code: "SAAT-M-ALG.167", ses: 23, lvl: 4,
    stem: "Which inequality describes the shaded region below?",
    fig: "i_rad_ineq", figW: 2.0,
    opts: [
      { eq: "i_ri3" },
      { eq: "i_ri4" },
      { eq: "i_ri1" },
      { eq: "i_ri2" }
    ],
    ans: 2,
    trick: "two decisions, and the options cover all four combinations — the ENDPOINT gives the shift with its sign reversed, and the SHADED SIDE gives the direction of the inequality",
    why: "The endpoint at x = −2 gives √(x + 2), and the region below the curve is y ≤ √(x + 2).",
    traps: [
      "A: the shift's sign not reversed.",
      "B: both decisions taken the wrong way.",
      "D: the shading read on the wrong side of the curve.",
    ],
  },
  {
    sig: "add-radicals-after-simplifying",
    code: "SAAT-M-ALG.168", ses: 3, lvl: 3,
    stem: "Simplify the expression below.",
    stemEq: "j_addrad",
    opts: [
      { eq: "i_ar2" },
      { eq: "i_ar3" },
      { eq: "i_ar4" },
      { eq: "i_ar1" }
    ],
    ans: 3,
    trick: "pull the square factor out of each surd FIRST so that all three carry the same radicand, then add and subtract the coefficients — the numbers under the roots are never added",
    why: "5√3 + 4√3 − 2√3 = 7√3.",
    traps: [
      "A: the subtraction treated as an addition.",
      "B: the radicands added.",
      "C: √48 simplified as 6√3.",
    ],
  },

  // ================================================== COMPLEX NUMBERS
  {
    sig: "product-of-two-complex-binomials",
    code: "SAAT-M-ALG.169", ses: 61, lvl: 3,
    stem: "Work out (3 + 2i)(2 − i).",
    opts: [
      { eq: "i_cb1" },
      { eq: "i_cb2" },
      { eq: "i_cb3" },
      { eq: "i_cb4" }
    ],
    ans: 0,
    trick: "multiply out all four products and remember i² is MINUS one — that turns the last term into a real number which ADDS to the real part rather than subtracting from it",
    why: "6 − 3i + 4i − 2i² = 6 + i + 2 = 8 + i.",
    traps: [
      "B: i² left as +1.",
      "C: the two middle terms added without their signs.",
      "D: only the first and last terms multiplied.",
    ],
  },
  {
    sig: "power-of-one-plus-i-by-squaring",
    code: "SAAT-M-ALG.170", ses: 61, lvl: 4,
    stem: "Work out (1 + i)⁶.",
    opts: [
      { eq: "i_pw4" },
      { eq: "i_pw1" },
      { eq: "i_pw2" },
      { eq: "i_pw3" }
    ],
    ans: 1,
    trick: "square ONCE and the work collapses — (1 + i)² is exactly 2i — then cube that; i³ is −i, and losing that sign is the whole question",
    why: "(1 + i)² = 2i, so (1 + i)⁶ = (2i)³ = 8i³ = −8i.",
    traps: [
      "A: both the sign and the i lost.",
      "C: i³ taken as +i.",
      "D: the i dropped from i³.",
    ],
  },

  // ======================================================== TRIGONOMETRY
  {
    sig: "principal-value-of-an-inverse-cosine",
    code: "SAAT-M-TRI.55", ses: 76, lvl: 4,
    stem: "What is the principal value below, in degrees?",
    stemEq: "j_acos",
    opts: [
      "225°",
      "315°",
      "135°",
      "45°"
    ],
    ans: 2,
    trick: "the inverse cosine only ever returns an angle between 0° and 180°, so a negative input lands in the SECOND quadrant — every other solution on the circle is outside the range and cannot be the answer",
    why: "cos 135° = −√2/2, and 135° lies in the range of the inverse cosine.",
    traps: [
      "A: the third-quadrant solution, outside the range.",
      "B: the fourth-quadrant solution, outside the range.",
      "D: the reference angle given.",
    ],
  },
  {
    sig: "cosine-of-a-negative-angle-is-even",
    code: "SAAT-M-TRI.56", ses: 73, lvl: 4,
    stem: "What is the exact value of cos(−150°)?",
    opts: [
      { eq: "i_ce2" },
      { eq: "i_ce3" },
      { eq: "i_ce4" },
      { eq: "i_ce1" }
    ],
    ans: 3,
    trick: "the cosine is EVEN, so the minus sign on the angle does nothing at all — the sign of the answer comes from the quadrant 150° sits in, not from the negative in front of it",
    why: "cos(−150°) = cos 150° = −√3/2.",
    traps: [
      "A: the negative angle treated as flipping the sign, as the sine's would.",
      "B: the sine of the angle given instead.",
      "C: the sine used and its sign flipped as well.",
    ],
  },
  {
    sig: "law-of-sines-find-a-side",
    code: "SAAT-M-TRI.57", ses: 77, lvl: 4,
    stem: "In the triangle below, how long is x?",
    fig: "i_sine_rule", figW: 2.1,
    opts: [
      { eq: "i_ls1" },
      { eq: "i_ls2" },
      { eq: "i_ls3" },
      { eq: "i_ls4" }
    ],
    ans: 0,
    trick: "two angles and one side is the law of SINES, and each side pairs with the angle OPPOSITE it — the wrong options are the same two ratios the other way up, and they always shorten the side that should be longer",
    why: "x/sin 60° = 14/sin 45°, so x = 14(√3/2)/(√2/2) = 7√6.",
    traps: [
      "B: the ratio inverted.",
      "C: the two sides assumed equal.",
      "D: sin 60° read as 1/2.",
    ],
  },
  {
    sig: "inverse-sine-of-a-cosine-does-not-cancel",
    code: "SAAT-M-TRI.58", ses: 73, lvl: 4,
    stem: "Evaluate sin⁻¹(cos 30°), in radians.",
    opts: [
      { eq: "i_ic4" },
      { eq: "i_ic1" },
      { eq: "i_ic2" },
      { eq: "i_ic3" }
    ],
    ans: 1,
    trick: "the inverse SINE and the COSINE are not inverses of each other, so nothing cancels — work the cosine out first, then ask which angle has that value as its sine; the cofunction rule gets there in one step",
    why: "cos 30° = √3/2, and sin⁻¹(√3/2) = π/3.",
    traps: [
      "A: the value read from the 45° row.",
      "C: the two functions cancelled as though they undid each other.",
      "D: the cofunction subtraction started but the angle never taken off.",
    ],
  },

  // =============================================== COUNTING AND PROBABILITY
  {
    sig: "probability-of-one-specific-arrangement",
    code: "SAAT-M-STA.30", ses: 43, lvl: 3,
    stem: "Five different books are put on a shelf in a random order. What is the probability that they end up in one particular order?",
    opts: [
      { eq: "i_sa3" },
      { eq: "i_sa4" },
      { eq: "i_sa1" },
      { eq: "i_sa2" }
    ],
    ans: 2,
    trick: "every one of the 5! orders is equally likely, so one named order has probability 1 over 5! — one over the NUMBER OF BOOKS is what the eye reaches for and it is far too large",
    why: "There are 5! = 120 equally likely orders, so the probability is 1/120.",
    traps: [
      "A: one over the square of the number of books.",
      "B: one over 5 × 4.",
      "D: one over the number of books.",
    ],
  },
  {
    sig: "midpoint-square-is-half-the-area",
    code: "SAAT-M-STA.31", ses: 43, lvl: 4,
    stem: "A point is chosen at random inside the large square below. What is the probability that it lands inside the shaded square?",
    fig: "i_mid_square", figW: 1.6,
    opts: [
      { eq: "i_ms2" },
      { eq: "i_ms3" },
      { eq: "i_ms4" },
      { eq: "i_ms1" }
    ],
    ans: 3,
    trick: "joining the midpoints of a square always halves its AREA, whatever the side is — the measurement printed on the figure is decoration and never has to be used at all",
    why: "The four corner triangles make up exactly half the square, so the shaded square is the other half.",
    traps: [
      "A: the side halved and the area quartered with it.",
      "B: one of the four corner triangles given.",
      "C: the ratio of the SIDES given instead of the ratio of the areas.",
    ],
  },
  {
    sig: "probability-of-an-arrangement-with-end-constraints",
    code: "SAAT-M-STA.32", ses: 44, lvl: 4,
    stem: "Three boys and two girls stand in a row in a random order. What is the probability that a girl stands at each end?",
    opts: [
      { eq: "i_ec1" },
      { eq: "i_ec2" },
      { eq: "i_ec3" },
      { eq: "i_ec4" }
    ],
    ans: 0,
    trick: "count favourable ARRANGEMENTS, not favourable people — the two ends can be filled in 2! ways and the middle three in 3!, so 12 of the 120 orders qualify",
    why: "2! × 3! = 12 of the 5! = 120 orders put a girl at each end, and 12/120 = 1/10.",
    traps: [
      "B: the girls fixed at the ends in one order only.",
      "C: the ratio of girls to people given.",
      "D: one single arrangement counted.",
    ],
  },
  {
    sig: "lines-determined-by-points",
    code: "SAAT-M-STA.33", ses: 44, lvl: 3,
    stem: "Twelve points lie on a circle. How many straight lines are determined by pairs of them?",
    opts: [
      "24",
      "66",
      "132",
      "220"
    ],
    ans: 1,
    trick: "a line needs TWO points and the order does not matter, so this is a combination — counting ordered pairs doubles the answer, and choosing three points counts triangles instead",
    why: "C(12, 2) = 66.",
    traps: [
      "A: twice the number of points.",
      "C: ordered pairs counted, doubling the answer.",
      "D: groups of three counted, which gives triangles.",
    ],
  },
  {
    sig: "probability-that-three-points-are-collinear",
    code: "SAAT-M-STA.34", ses: 43, lvl: 4,
    stem: "Three of the nine points below are chosen at random. What is the probability that they lie on one straight line?",
    fig: "i_grid_points", figW: 1.35,
    opts: [
      { eq: "i_co3" },
      { eq: "i_co4" },
      { eq: "i_co1" },
      { eq: "i_co2" }
    ],
    ans: 2,
    trick: "count the collinear TRIPLES and divide by every triple — three rows and three columns are easy to see, and the two DIAGONALS are what the paper is waiting for you to forget",
    why: "8 collinear triples (3 rows, 3 columns, 2 diagonals) out of C(9, 3) = 84, which is 2/21.",
    traps: [
      "A: the number of lines divided by the number of points.",
      "B: ordered triples used in the denominator.",
      "D: the two diagonals missed.",
    ],
  },
];
