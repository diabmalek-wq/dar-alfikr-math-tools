// PART J of the SAAT booklet — the three recalled summer papers.
//
// Same rule as every other source in this bank, and it matters most here: the
// papers were read for the SKILL and the TRICK only. No stem, number set,
// option list or figure is reproduced. Every stem is newly worded in English,
// every number set is new, every answer re-derived in verify_saat_j.py, and the
// seven figures are drawn from scratch in make_figs_saat_j.py.
//
// Between them the three papers carried over 300 items. The great majority
// tested skills the bank already held and were dropped. The twenty-six below
// are what was genuinely new, and they cluster in places a normal Algebra II
// course never goes:
//
//   · PHYSICS-FLAVOURED VECTORS — resolving a force into components, and
//     quadrant-bearing notation (S 20° W), which is navigation language.
//   · STRUCTURAL GEOMETRY — three items answerable WITHOUT finding any single
//     angle or length: interior plus exterior is a straight angle; the three
//     marked angles of a square's diagonal are one triangle's; two perpendicular
//     medians give a side by Pythagoras on the centroid pieces.
//   · COUNTING-BASED PROBABILITY — hypergeometric selection, divisibility by
//     five decided by the units digit, and a circular arrangement as 1/(n−1)!.
//   · STRUCTURAL ALGEBRA AND CALCULUS — a cancelled factor that is still
//     excluded, a factor that is the NEGATIVE of another, limit laws with no
//     function given at all, a derivative that does not exist because the
//     function does not, and a definite integral read off as a semicircle.
//
// One of the recalled papers printed an answer key that disagrees with its own
// mathematics on several items — including the eccentricity item this part
// reworks, where the key gives the semi-axis and the question asks for the
// axis. Every answer below was derived here and trusts nothing on those pages.

module.exports = [
  // ============================================ VECTORS AND POLAR, IN PHYSICS
  {
    sig: "resolve-a-force-into-components",
    code: "SAAT-M-ALG.171", ses: 79, lvl: 4,
    stem: "A rope pulls a crate with a force of 120 N at 30° above the horizontal, as shown. What is the horizontal component of the force?",
    fig: "jx_force", figW: 2.2,
    opts: [
      { eq: "jx_f1" },
      { eq: "jx_f2" },
      { eq: "jx_f3" },
      { eq: "jx_f4" }
    ],
    ans: 0,
    trick: "the HORIZONTAL component uses the COSINE of the angle made with the horizontal — the sine gives the vertical one, and neither component can ever be as large as the force itself",
    why: "120 cos 30° = 120(√3/2) = 60√3.",
    traps: [
      "B: the sine used, which gives the vertical component.",
      "C: the force copied down unresolved.",
      "D: the 45° ratio used instead of the 30° one.",
    ],
  },
  {
    sig: "quadrant-bearing-for-a-vector",
    code: "SAAT-M-ALG.172", ses: 79, lvl: 4,
    stem: "A ship sails in a direction 20° west of due south. How is that direction written as a quadrant bearing?",
    opts: [
      "N 20° E",
      "S 20° W",
      "W 20° S",
      "S 70° W"
    ],
    ans: 1,
    trick: "a quadrant bearing names the NORTH–SOUTH axis first, then the angle turned from it towards east or west — swapping the two letters names a completely different direction",
    why: "The direction starts from due south and turns 20° towards the west, which is written S 20° W.",
    traps: [
      "A: the opposite direction.",
      "C: the two axis letters reversed, which measures from west instead.",
      "D: the complement used, 70° instead of 20°.",
    ],
  },
  {
    sig: "equivalent-polar-representations",
    code: "SAAT-M-TRI.59", ses: 80, lvl: 4,
    stem: "Which pair of polar coordinates names the SAME point as (−5, 40°)?",
    opts: [
      "(−5, 220°)",
      "(5, 140°)",
      "(5, 220°)",
      "(5, 40°)"
    ],
    ans: 2,
    trick: "a negative radius puts the point on the OPPOSITE ray, so the minus sign is removed by turning the angle through 180° — changing only the sign, or only the angle, moves the point somewhere else entirely",
    why: "(−5, 40°) lies on the ray at 40° + 180° = 220°, at distance 5, so it is (5, 220°).",
    traps: [
      "A: the angle turned but the minus sign kept, undoing the turn.",
      "B: the angle reflected in the vertical axis instead of turned through 180°.",
      "D: the minus sign simply dropped.",
    ],
  },
  {
    sig: "polar-two-term-to-a-circle",
    code: "SAAT-M-TRI.60", ses: 80, lvl: 4,
    stem: "Write the polar equation below in rectangular form.",
    stemEq: "jx_pol",
    opts: [
      { eq: "jx_pc2" },
      { eq: "jx_pc3" },
      { eq: "jx_pc4" },
      { eq: "jx_pc1" }
    ],
    ans: 3,
    trick: "multiply through by r FIRST so that BOTH terms convert, then complete the square twice — the centre is half of each coefficient, and the radius squared is the sum of those two halves squared",
    why: "r² = 4r cos θ + 6r sin θ gives x² + y² = 4x + 6y, so (x − 2)² + (y − 3)² = 13.",
    traps: [
      "A: the two coefficients attached to the wrong variables.",
      "B: the signs in the centre not reversed.",
      "C: the radius written where the radius SQUARED belongs.",
    ],
  },

  // ==================================================== REASONING AND LOGIC
  {
    sig: "causal-versus-correlational-statement",
    code: "SAAT-M-STA.35", unit: 0, topic: "Statements, truth values & reasoning", lvl: 4,
    stem: "Which statement below describes a CAUSAL relationship rather than a correlation?",
    opts: [
      "Heating water to 100 °C at sea level makes it boil",
      "Students who own more books tend to score higher in tests",
      "Ice-cream sales and sunburn cases rise in the same months",
      "Cities with more schools also have more hospitals"
    ],
    ans: 0,
    trick: "a correlation says two things move TOGETHER; a cause says one MAKES the other happen — the giveaway in the wrong options is a third factor, the season or the size of the city, that is driving both",
    why: "Heating water past its boiling point is what makes it boil; the others are pairs driven by something else.",
    traps: [
      "B: a shared cause — households that buy books also support study.",
      "C: both are driven by the weather.",
      "D: both are driven by population.",
    ],
  },
  {
    sig: "average-rate-zero-what-follows",
    code: "SAAT-M-CAL.57", ses: 94, lvl: 4,
    stem: "The average rate of change of f between x = m and x = n is zero. Which statement MUST be true?",
    opts: [
      "f is constant between m and n",
      "f(m) = f(n)",
      "m = n",
      "f(m) = 0 and f(n) = 0"
    ],
    ans: 1,
    trick: "a zero average rate forces the two OUTPUTS to be equal and nothing else — the inputs must actually differ for the rate to exist at all, and what the function does in between is completely unconstrained",
    why: "(f(n) − f(m))/(n − m) = 0 with n ≠ m gives f(n) = f(m).",
    traps: [
      "A: the function may rise and fall in between and still return.",
      "C: equal inputs would make the rate undefined, not zero.",
      "D: equal values need not be zero values.",
    ],
  },
  {
    sig: "lines-in-a-square-grid",
    code: "SAAT-M-STA.36", ses: 43, lvl: 4,
    stem: "A square is ruled into a 5 by 5 array of small squares. How many straight grid lines, including the four outer edges, does the drawing contain?",
    opts: [
      "25",
      "6",
      "12",
      "10"
    ],
    ans: 2,
    trick: "count the LINES, not the squares — an array n squares across needs n + 1 lines to make it, one more than the number of squares along a side, and that extra one is the whole question",
    why: "6 horizontal lines and 6 vertical lines make 12.",
    traps: [
      "A: the small squares counted.",
      "B: only one direction counted.",
      "D: five lines counted in each direction instead of six.",
    ],
  },

  // ======================================================== PLANE GEOMETRY
  {
    sig: "interior-plus-exterior-angle-is-a-straight-angle",
    code: "SAAT-M-GEO.101", ses: 32, lvl: 4,
    stem: "One side of the regular pentagon below is produced. What is x + y?",
    fig: "jx_pent_ext", figW: 1.8,
    opts: [
      "108°",
      "72°",
      "360°",
      "180°"
    ],
    ans: 3,
    trick: "the interior angle and the exterior angle at the SAME vertex lie on a straight line, so they add to 180° whatever the polygon is — neither of them ever has to be worked out",
    why: "x and y form a linear pair along the produced side, so x + y = 180°.",
    traps: [
      "A: only the interior angle given.",
      "B: only the exterior angle given.",
      "C: the full turn given.",
    ],
  },
  {
    sig: "angle-sum-without-finding-any-angle",
    code: "SAAT-M-GEO.102", ses: 32, lvl: 4,
    stem: "A diagonal is drawn in the square below. What is x + y + z?",
    fig: "jx_square_diag", figW: 1.6,
    opts: [
      "180°",
      "135°",
      "90°",
      "360°"
    ],
    ans: 0,
    trick: "the three marked angles are the three angles of ONE triangle, so they add to 180° — no individual angle ever has to be found, and the 45° the eye reaches for is a distraction",
    why: "x, y and z are the angles of the triangle the diagonal cuts off.",
    traps: [
      "B: all three taken as 45°.",
      "C: only the right angle counted.",
      "D: the square's full turn given.",
    ],
  },
  {
    sig: "pythagoras-across-stacked-squares",
    code: "SAAT-M-GEO.103", ses: 31, lvl: 4,
    stem: "In the figure below two squares of side 7 and 5 stand side by side on the same line. How long is the marked segment?",
    fig: "jx_stacked_sq", figW: 2.2,
    opts: [
      { eq: "jx_sq4" },
      { eq: "jx_sq1" },
      { eq: "jx_sq2" },
      { eq: "jx_sq3" }
    ],
    ans: 1,
    trick: "the segment is the hypotenuse of ONE right triangle whose legs are the TOTAL base and the height of the second square — adding the side lengths is the near-miss the figure is built to invite",
    why: "The legs are 7 + 5 = 12 and 5, so the segment is √(144 + 25) = 13.",
    traps: [
      "A: only the second square used.",
      "C: only the total base counted.",
      "D: the three marked lengths added.",
    ],
  },
  {
    sig: "count-lines-of-symmetry",
    code: "SAAT-M-GEO.104", ses: 40, lvl: 3,
    stem: "How many lines of symmetry does the figure below have?",
    fig: "jx_symmetry", figW: 1.5,
    opts: [
      "8",
      "1",
      "4",
      "2"
    ],
    ans: 2,
    trick: "a line of symmetry is a WHOLE line, not a half — counting each one as two rays going opposite ways doubles the answer, and that doubled figure is on the page",
    why: "The vertical, the horizontal and the two diagonals are all axes of symmetry.",
    traps: [
      "A: each axis counted twice, as two rays.",
      "B: only the vertical axis found.",
      "D: only the two through the arms found.",
    ],
  },
  {
    sig: "name-the-quadrilateral-from-its-sides",
    code: "SAAT-M-GEO.105", ses: 32, lvl: 3,
    stem: "A quadrilateral has two pairs of congruent ADJACENT sides, and its opposite sides are not congruent. What is it?",
    opts: [
      "A rhombus",
      "A parallelogram",
      "A trapezoid",
      "A kite"
    ],
    ans: 3,
    trick: "a kite pairs its congruent sides NEXT to each other; a rhombus and a parallelogram pair theirs OPPOSITE each other, which the second half of the question rules out",
    why: "Two pairs of congruent adjacent sides with unequal opposite sides is the definition of a kite.",
    traps: [
      "A: a rhombus has all four sides congruent.",
      "B: a parallelogram pairs its opposite sides.",
      "C: a trapezoid is defined by parallel sides, not congruent ones.",
    ],
  },
  {
    sig: "perpendicular-medians-and-the-centroid",
    code: "SAAT-M-GEO.106", ses: 29, lvl: 4,
    stem: "In the triangle below the medians drawn from A and from B meet at right angles, and they measure 12 and 9. How long is AB?",
    fig: "jx_perp_medians", figW: 1.9,
    opts: [
      "10",
      "15",
      "5",
      "21"
    ],
    ans: 0,
    trick: "the pieces meeting at the centroid are TWO-THIRDS of each median, measured from the vertex — Pythagoras then runs on those two pieces, not on the whole medians and not on the short thirds",
    why: "The pieces are (2/3)(12) = 8 and (2/3)(9) = 6, so AB = √(64 + 36) = 10.",
    traps: [
      "B: the whole medians used as the legs.",
      "C: the one-third pieces used.",
      "D: the two medians simply added.",
    ],
  },

  // ================================================ COUNTING AND PROBABILITY
  {
    sig: "hypergeometric-selection-probability",
    code: "SAAT-M-STA.37", ses: 44, lvl: 4,
    stem: "A box holds 5 blue pens and 3 red pens. Three pens are taken out together at random. What is the probability that exactly two of them are blue?",
    opts: [
      { eq: "jx_hg4" },
      { eq: "jx_hg1" },
      { eq: "jx_hg2" },
      { eq: "jx_hg3" }
    ],
    ans: 1,
    trick: "choose from EACH colour separately and MULTIPLY, then divide by the ways of choosing the whole handful — the third pen has to come from the other colour, and forgetting that is what the second option is built on",
    why: "C(5,2)·C(3,1)/C(8,3) = 10 × 3 / 56 = 30/56 = 15/28.",
    traps: [
      "A: the raw share of blue pens used.",
      "C: the red pen's three choices left out.",
      "D: the two counts added instead of multiplied.",
    ],
  },
  {
    sig: "probability-of-a-number-divisible-by-five",
    code: "SAAT-M-STA.38", ses: 44, lvl: 4,
    stem: "The digits 2, 4, 5 and 7 are arranged at random into a four-digit number, using each digit once. What is the probability that the number is divisible by 5?",
    opts: [
      { eq: "jx_d53" },
      { eq: "jx_d54" },
      { eq: "jx_d51" },
      { eq: "jx_d52" }
    ],
    ans: 2,
    trick: "divisibility by 5 is settled by the UNITS digit alone, so the whole question is the chance that the 5 lands last — one place out of four, whatever the other three digits do",
    why: "3! = 6 of the 4! = 24 arrangements end in 5, and 6/24 = 1/4.",
    traps: [
      "A: a single arrangement counted.",
      "B: the arrangements of the other three digits used as the probability.",
      "D: one fifth taken because the divisor is 5.",
    ],
  },
  {
    sig: "probability-of-one-circular-arrangement",
    code: "SAAT-M-STA.39", ses: 44, lvl: 4,
    stem: "Seven people sit at random around a round table. What is the probability of one particular seating, counting only who sits next to whom?",
    opts: [
      { eq: "jx_cir2" },
      { eq: "jx_cir3" },
      { eq: "jx_cir4" },
      { eq: "jx_cir1" }
    ],
    ans: 3,
    trick: "round a table there is no first chair, so one person is FIXED and the rest are arranged around them — that gives (n − 1)! seatings, not n!, and the larger figure is the option beside the answer",
    why: "There are 6! = 720 distinct circular seatings, so one of them has probability 1/720.",
    traps: [
      "A: 7! used, as though the seats were in a row.",
      "B: one over the number of people.",
      "C: one over the square of the number of people.",
    ],
  },

  // ============================================ STRUCTURAL ALGEBRA
  {
    sig: "cancelled-factor-is-still-excluded",
    code: "SAAT-M-ALG.173", ses: 7, lvl: 4,
    stem: "For which values of x is the expression below undefined?",
    stemEq: "jx_hole",
    opts: [
      "3 and −5",
      "−5 only",
      "3, −3 and −5",
      "−3 and −5"
    ],
    ans: 0,
    trick: "a factor that cancels leaves a HOLE, and the expression is still undefined there — cancelling first and then reading off the denominator loses that value every single time",
    why: "The denominator is zero at x = 3 and x = −5; the (x − 3) cancels but 3 stays excluded.",
    traps: [
      "B: the cancelled factor's zero dropped.",
      "C: the numerator's other zero included as well.",
      "D: the sign of the surviving exclusion reversed.",
    ],
  },
  {
    sig: "cancel-a-factor-that-is-the-negative-of-another",
    code: "SAAT-M-ALG.174", ses: 7, lvl: 4,
    stem: "Simplify the product below.",
    stemEq: "jx_neg",
    opts: [
      { eq: "jx_ng4" },
      { eq: "jx_ng1" },
      { eq: "jx_ng2" },
      { eq: "jx_ng3" }
    ],
    ans: 1,
    trick: "one numerator is the NEGATIVE of the other denominator, so that pair cancels to −1 — the whole question is the minus sign, and multiplying out instead of cancelling buries it",
    why: "(3 − x)/(x − 3) = −1, so the product is −a/6.",
    traps: [
      "A: the 6 and the 3 cancelled as though they were factors.",
      "C: the sign of the cancellation missed.",
      "D: left unsimplified.",
    ],
  },
  {
    sig: "number-of-terms-from-the-sum",
    code: "SAAT-M-ALG.175", ses: 60, lvl: 4,
    stem: "An arithmetic series has first term 4, last term 40 and sum 220. How many terms has it?",
    opts: [
      "11",
      "5",
      "10",
      "9"
    ],
    ans: 2,
    trick: "with the first term, the last term AND the sum all given, n drops straight out of S = n(a₁ + aₙ)/2 — the common difference is never needed, and hunting for it first is where the time goes",
    why: "220 = n(4 + 40)/2 = 22n, so n = 10.",
    traps: [
      "A: one added.",
      "B: the halving left out, giving 220 = 44n.",
      "D: one subtracted, as though counting the gaps.",
    ],
  },

  // ==================================================== STRUCTURAL CALCULUS
  {
    sig: "constant-that-makes-a-piecewise-function-continuous",
    code: "SAAT-M-CAL.58", ses: 92, lvl: 4,
    stem: "For which value of a is the function below continuous at x = 2?",
    stemEq: "jx_cont",
    opts: [
      "−1",
      "5",
      "9",
      "1"
    ],
    ans: 3,
    trick: "continuity at the join means the two branches must AGREE there, so set one equal to the other at the joining value — substituting into only one branch answers nothing at all",
    why: "4 + a = 5 gives a = 1.",
    traps: [
      "A: the sign of a lost in solving.",
      "B: the second branch's value given instead of a.",
      "C: the two branch values added.",
    ],
  },
  {
    sig: "definite-integral-as-a-semicircle-area",
    code: "SAAT-M-CAL.59", ses: 114, lvl: 4,
    stem: "Use the area of the shaded region to evaluate the integral below.",
    stemEq: "jx_semi",
    fig: "jx_semicircle", figW: 2.0,
    opts: [
      { eq: "jx_si1" },
      { eq: "jx_si2" },
      { eq: "jx_si3" },
      { eq: "jx_si4" }
    ],
    ans: 0,
    trick: "the integrand is the UPPER HALF of a circle of radius 3, so the integral is half that circle's area — hunting for an antiderivative is slow and is not what the question is asking for",
    why: "Half of π(3)² is 9π/2.",
    traps: [
      "B: the whole circle's area given.",
      "C: the radius used where the radius squared belongs.",
      "D: the diameter used as the radius.",
    ],
  },
  {
    sig: "derivative-does-not-exist-at-a-domain-gap",
    code: "SAAT-M-CAL.60", ses: 94, lvl: 4,
    stem: "For f(x) = (x + 1) ÷ (x − 5), what is f′(5)?",
    opts: [
      "1",
      "It does not exist",
      "0",
      "−6"
    ],
    ans: 1,
    trick: "a function has no DERIVATIVE where it has no VALUE — the quotient rule happily produces a formula, but that formula is undefined at 5 as well, so no number can be read off it",
    why: "f is undefined at x = 5, so f′(5) cannot exist; the quotient rule gives −6/(x − 5)², which is also undefined there.",
    traps: [
      "A: the ratio of the leading coefficients given.",
      "C: a constant numerator mistaken for a constant function.",
      "D: the numerator of the derivative reported.",
    ],
  },
  {
    sig: "limit-laws-with-symbolic-values",
    code: "SAAT-M-CAL.61", ses: 91, lvl: 4,
    stem: "As x approaches c, the limit of f is A and the limit of g is −A. What is the limit of f(x) − g(x)?",
    opts: [
      "−2A",
      "A",
      "2A",
      "0"
    ],
    ans: 2,
    trick: "the limit of a difference is the DIFFERENCE of the limits, and subtracting a negative adds — no function is ever given, so the whole item is the double negative",
    why: "A − (−A) = 2A.",
    traps: [
      "A: the difference taken the wrong way round.",
      "B: one of the two terms dropped.",
      "D: the two limits read as cancelling.",
    ],
  },

  // ================================================ TRIGONOMETRY AND CONICS
  {
    sig: "exact-sine-by-decomposing-a-non-special-angle",
    code: "SAAT-M-TRI.61", ses: 74, lvl: 4,
    stem: "What is the exact value of sin 75°?",
    opts: [
      { eq: "jx_s752" },
      { eq: "jx_s753" },
      { eq: "jx_s754" },
      { eq: "jx_s751" }
    ],
    ans: 3,
    trick: "75° is 45° + 30°, so the SUM formula applies, and the two products each pick up a quarter — using the difference formula, or forgetting that two halves multiply to a quarter, are the two errors offered",
    why: "sin 45° cos 30° + cos 45° sin 30° = (√6 + √2)/4.",
    traps: [
      "A: the difference formula used.",
      "B: the surds combined arithmetically.",
      "C: the two halves not multiplied, leaving a denominator of 2.",
    ],
  },
  {
    sig: "collapse-a-cosine-sum-to-a-quadrantal-angle",
    code: "SAAT-M-TRI.62", ses: 74, lvl: 4,
    stem: "Evaluate the expression below.",
    stemEq: "jx_coll",
    opts: [
      { eq: "jx_cl1" },
      { eq: "jx_cl2" },
      { eq: "jx_cl3" },
      { eq: "jx_cl4" }
    ],
    ans: 0,
    trick: "this is exactly cos A cos B − sin A sin B, which collapses to cos(A + B) — and the two angles add to 90°, so the value falls out with no arithmetic at all",
    why: "cos 70° cos 20° − sin 70° sin 20° = cos 90° = 0.",
    traps: [
      "B: read as the Pythagorean identity.",
      "C: cos 60° given.",
      "D: cos 30° given.",
    ],
  },
  {
    sig: "minor-axis-from-eccentricity",
    code: "SAAT-M-GEO.107", ses: 84, lvl: 4,
    stem: "An ellipse has a major axis of length 20 and eccentricity 3/5. How long is its MINOR AXIS?",
    opts: [
      "12",
      "16",
      "8",
      "64"
    ],
    ans: 1,
    trick: "an AXIS is twice the semi-axis, and b is only the semi-minor — the value 8 is the half the question does not ask for, and it is exactly where most students stop",
    why: "a = 10, c = (3/5)(10) = 6, b² = 100 − 36 = 64, b = 8, so the minor axis is 16.",
    traps: [
      "A: 2c given.",
      "C: the semi-minor axis given instead of the axis.",
      "D: b² given.",
    ],
  },
];
