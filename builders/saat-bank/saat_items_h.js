// PART H of the SAAT booklet — the skills taken from the circulated Tahsili
// recall album ("اختبر نفسك — تحصيلي رياضيات").
//
// The album is a recall deck: candidates leave the hall and reconstruct what
// they saw. It was read here for TWO things only — which skill each card tests
// and which misconception its distractors are built to catch. No stem, number
// set, option list or figure is reproduced. Every stem is newly worded in
// English, every number set is new, every answer re-derived, and the three
// figures are drawn from scratch in make_figs_saat_h.py.
//
// Only the skills the bank did NOT already hold were written up. Twenty-one of
// the forty-one cards read were already covered by parts A–G and were dropped
// rather than repeated — the sig guard would have stopped them anyway.
//
// Every answer is re-derived independently in verify_saat_h.py.

module.exports = [
  // ============================================ VECTORS, POLYNOMIALS, GRAPHS
  {
    sig: "parallelogram-area-from-a-cross-product",
    code: "SAAT-M-ALG.158", ses: 79, lvl: 4,
    stem: "What is the area of the parallelogram with adjacent sides u = ⟨2, −1, 3⟩ and v = ⟨1, 4, −2⟩?",
    opts: [
      { eq: "h_cp1" },
      { eq: "h_cp2" },
      { eq: "h_cp3" },
      { eq: "h_cp4" }
    ],
    ans: 0,
    trick: "the area of the parallelogram is the MAGNITUDE OF THE CROSS PRODUCT, and it is not halved — halving gives the triangle on the same two sides, and the dot product gives no area at all",
    why: "u × v = ⟨−10, 7, 9⟩, whose magnitude is √(100 + 49 + 81) = √230.",
    traps: [
      "B: halved, as though the figure were the triangle.",
      "C: the dot product taken instead of the cross product.",
      "D: the two magnitudes multiplied.",
    ],
  },
  {
    sig: "box-base-area-model-from-a-sheet",
    code: "SAAT-M-ALG.159", ses: 16, lvl: 4,
    stem: "Squares of side x are cut from the four corners of a 24 cm by 18 cm sheet and the sides are folded up. Which expression gives the area of the base?",
    opts: [
      { eq: "h_bx4" },
      { eq: "h_bx1" },
      { eq: "h_bx2" },
      { eq: "h_bx3" }
    ],
    ans: 1,
    trick: "each dimension loses a square at BOTH ends, so 2x comes off it — not 4x, and not x — and the base is the product of what is left, not the sheet with four squares subtracted",
    why: "The base measures (24 − 2x) by (18 − 2x).",
    traps: [
      "A: the four corner squares subtracted from the whole sheet.",
      "C: 4x taken off each dimension, counting each corner twice.",
      "D: only one corner removed from each dimension.",
    ],
  },
  {
    sig: "domain-of-a-piecewise-graph-with-an-open-end",
    code: "SAAT-M-ALG.160", ses: 20, lvl: 4,
    stem: "What is the domain of the function graphed below?",
    fig: "h_piecewise", figW: 2.0,
    opts: [
      { eq: "h_dm3" },
      { eq: "h_dm4" },
      { eq: "h_dm1" },
      { eq: "h_dm2" }
    ],
    ans: 2,
    trick: "the domain is read ALONG the x-axis, and a hollow endpoint is excluded while a filled one is not — the gap between the two pieces belongs to neither",
    why: "The ray covers x < 1 with 1 excluded, and the segment covers 3 ≤ x ≤ 6.",
    traps: [
      "A: the gap between the two pieces filled in.",
      "B: the range given instead of the domain.",
      "D: the hollow endpoint treated as included.",
    ],
  },
  {
    sig: "range-of-a-piecewise-graph-with-an-isolated-value",
    code: "SAAT-M-ALG.161", ses: 20, lvl: 4,
    stem: "What is the range of the function graphed below?",
    fig: "h_piecewise", figW: 2.0,
    opts: [
      { eq: "h_rg2" },
      { eq: "h_rg3" },
      { eq: "h_rg4" },
      { eq: "h_rg1" }
    ],
    ans: 3,
    trick: "a HORIZONTAL piece contributes a single y value however long it is, so the range is an interval together with one isolated number — writing it as one interval swallows the gap",
    why: "The ray gives every y below −1, with −1 itself excluded; the segment gives y = 2 only.",
    traps: [
      "A: the excluded endpoint treated as included.",
      "B: the isolated value merged into the interval.",
      "C: the domain given instead of the range.",
    ],
  },

  // ============================================================ TRIGONOMETRY
  {
    sig: "sum-angle-with-a-forty-five-degree-shift",
    code: "SAAT-M-TRI.49", ses: 74, lvl: 4,
    stem: "Write the expression below without brackets.",
    stemEq: "h_sa",
    opts: [
      { eq: "h_sa1" },
      { eq: "h_sa2" },
      { eq: "h_sa3" },
      { eq: "h_sa4" }
    ],
    ans: 0,
    trick: "expand with the sum formula and notice that BOTH terms pick up the same √2/2 — the √2 outside cancels it exactly, so the surd disappears from the answer",
    why: "√2(sin x cos 45° + cos x sin 45°) = √2 · (√2/2)(sin x + cos x) = sin x + cos x.",
    traps: [
      "B: the outside √2 never cancelled.",
      "C: the sum formula applied with the difference's sign.",
      "D: the expansion applied to the first term only.",
    ],
  },
  {
    sig: "radians-to-degrees-multiple-of-pi",
    code: "SAAT-M-TRI.50", ses: 67, lvl: 3,
    stem: "An angle measures 7π/3 radians. What is its measure in degrees?",
    opts: [
      "60°",
      "420°",
      "210°",
      "840°"
    ],
    ans: 1,
    trick: "multiply by 180 over π, not by 360 over π — and the question asks for the MEASURE, so an angle past a full turn is not reduced",
    why: "7π/3 × 180/π = 7 × 60 = 420.",
    traps: [
      "A: a full revolution taken off, giving the coterminal angle.",
      "C: the fraction halved before converting.",
      "D: multiplied by 360/π instead of 180/π.",
    ],
  },
  {
    sig: "exact-sine-in-the-third-quadrant",
    code: "SAAT-M-TRI.51", ses: 69, lvl: 4,
    stem: "What is the exact value of sin 240°?",
    opts: [
      { eq: "h_q33" },
      { eq: "h_q34" },
      { eq: "h_q31" },
      { eq: "h_q32" }
    ],
    ans: 2,
    trick: "take the reference angle first — 240 − 180 = 60 — and then let the QUADRANT fix the sign; below the axis the sine is negative whatever the reference angle says",
    why: "The reference angle is 60°, and sine is negative in the third quadrant, so the value is −√3/2.",
    traps: [
      "A: the reference angle taken as 30°.",
      "B: the reference angle taken as 45°.",
      "D: the quadrant's sign ignored.",
    ],
  },
  {
    sig: "exact-sine-of-a-coterminal-angle",
    code: "SAAT-M-TRI.52", ses: 69, lvl: 4,
    stem: "What is the exact value of sin 780°?",
    opts: [
      { eq: "h_ct2" },
      { eq: "h_ct3" },
      { eq: "h_ct4" },
      { eq: "h_ct1" }
    ],
    ans: 3,
    trick: "keep subtracting 360° until the angle lands between 0° and 360° — 780 needs TWO full turns, and stopping after one leaves 420°, which is still off the circle",
    why: "780 − 720 = 60, and sin 60° = √3/2.",
    traps: [
      "A: only one revolution removed, and the sign read from the wrong quadrant.",
      "B: the reference angle taken as 30°.",
      "C: the reference angle taken as 45°.",
    ],
  },
  {
    sig: "radius-of-a-polar-circle-is-half-the-coefficient",
    code: "SAAT-M-TRI.53", ses: 80, lvl: 4,
    stem: "What is the radius of the circle r = 10 sin θ?",
    opts: [
      "5",
      "10",
      "25",
      "2.5"
    ],
    ans: 0,
    trick: "in r = a sin θ the coefficient is the DIAMETER, because the curve runs from the pole out to its far point and back — the radius is half of it",
    why: "r = 10 sin θ is the circle of centre (0, 5) and radius 5.",
    traps: [
      "B: the coefficient read as the radius.",
      "C: the coefficient squared.",
      "D: the coefficient quartered.",
    ],
  },
  {
    sig: "cosecant-from-a-sine-value-rationalised",
    code: "SAAT-M-TRI.54", ses: 73, lvl: 4,
    stem: "Given the value below, what is csc θ?",
    stemEq: "j_cscval",
    opts: [
      { eq: "h_cs4" },
      { eq: "h_cs1" },
      { eq: "h_cs2" },
      { eq: "h_cs3" }
    ],
    ans: 1,
    trick: "the cosecant is the RECIPROCAL of the sine, so turn the fraction over — and then clear the surd from the denominator, which changes how the answer looks but not what it is worth",
    why: "csc θ = 4/√6 = 4√6/6 = 2√6/3.",
    traps: [
      "A: the surd dropped while rationalising.",
      "C: the given sine returned unchanged.",
      "D: the rationalised fraction turned over.",
    ],
  },

  // =========================================== FUNCTIONS, LOGS AND GEOMETRY
  {
    sig: "graph-of-the-inverse-of-an-exponential",
    code: "SAAT-M-ALG.162", ses: 52, lvl: 4,
    stem: "The graph of y = 4ˣ is reflected in the line y = x. Which statement describes the image?",
    opts: [
      "It has a vertical asymptote at x = 0 and passes through (0, 1)",
      "It passes through the origin and has no asymptote",
      "It has a vertical asymptote at x = 0 and passes through (1, 0)",
      "It has a horizontal asymptote at y = 0 and passes through (0, 1)"
    ],
    ans: 2,
    trick: "reflecting in y = x swaps x with y EVERYWHERE, so the horizontal asymptote becomes a vertical one and the point (0, 1) becomes (1, 0) — the curve is the logarithm",
    why: "The inverse of y = 4ˣ is y = log₄ x, which has the y-axis as an asymptote and cuts the x-axis at 1.",
    traps: [
      "A: the asymptote swapped but the point left where it was.",
      "B: a curve through the origin, which a logarithm never is.",
      "D: the original exponential described, not its reflection.",
    ],
  },
  {
    sig: "inverse-of-a-linear-rational-function",
    code: "SAAT-M-ALG.163", ses: 24, lvl: 4,
    stem: "For f(x) = (2x + 1) ÷ (x − 3), what is the inverse function?",
    opts: [
      { eq: "h_iv2" },
      { eq: "h_iv3" },
      { eq: "h_iv4" },
      { eq: "h_iv1" }
    ],
    ans: 3,
    trick: "swap x and y and then SOLVE for y — that means clearing the fraction and collecting every y term on one side; the reciprocal is not the inverse and never was",
    why: "x(y − 3) = 2y + 1 gives y(x − 2) = 3x + 1, so the inverse is (3x + 1)/(x − 2).",
    traps: [
      "A: the reciprocal taken instead of the inverse.",
      "B: the signs mishandled when collecting the y terms.",
      "C: the sign of the constant in the denominator not carried through.",
    ],
  },
  {
    sig: "logarithm-of-a-decimal-that-is-a-negative-power",
    code: "SAAT-M-ALG.164", ses: 50, lvl: 4,
    stem: "What is the value of log₂ 0.125?",
    opts: [
      "−3",
      "3",
      "−4",
      "0.125"
    ],
    ans: 0,
    trick: "write the decimal as a fraction first: 0.125 is one eighth, and a RECIPROCAL power carries a negative exponent — the sign is the whole question",
    why: "0.125 = 1/8 = 2⁻³, so the logarithm is −3.",
    traps: [
      "B: the sign of the exponent dropped.",
      "C: the decimal places counted as the exponent.",
      "D: the argument returned unchanged.",
    ],
  },
  {
    sig: "slope-from-two-points-with-negatives",
    code: "SAAT-M-GEO.98", ses: 38, lvl: 3,
    stem: "What is the slope of the line through (−4, 7) and (2, −11)?",
    opts: [
      { eq: "h_sl4" },
      { eq: "h_sl1" },
      { eq: "h_sl2" },
      { eq: "h_sl3" }
    ],
    ans: 1,
    trick: "slope is rise over run, and subtracting a NEGATIVE x adds — the run here is 6, not 2, and getting that wrong is what every wrong option is built on",
    why: "(−11 − 7) ÷ (2 − (−4)) = −18 ÷ 6 = −3.",
    traps: [
      "A: the run taken as 2, the negative x ignored.",
      "C: the sign of the rise lost.",
      "D: run divided by rise.",
    ],
  },
  {
    sig: "base-of-an-isosceles-triangle-from-its-altitude",
    code: "SAAT-M-GEO.99", ses: 29, lvl: 4,
    stem: "In the isosceles triangle below the two equal sides measure 13 and the altitude to the base measures 12. How long is the base?",
    fig: "h_iso_alt", figW: 1.6,
    opts: [
      "25",
      "24",
      "10",
      "5"
    ],
    ans: 2,
    trick: "the altitude from the apex of an isosceles triangle BISECTS the base, so Pythagoras gives only half of it — the answer has to be doubled, and the half is always offered",
    why: "√(169 − 144) = 5 is half the base, so the base is 10.",
    traps: [
      "A: the half-base squared.",
      "B: the altitude doubled instead.",
      "D: the half-base given as the answer.",
    ],
  },
  {
    sig: "parallelogram-angle-split-by-a-diagonal",
    code: "SAAT-M-GEO.100", ses: 32, lvl: 4,
    stem: "In the parallelogram below the diagonal AC splits the angle at A. What is x?",
    fig: "h_pgram_diag", figW: 2.45,
    opts: [
      "70°",
      "150°",
      "40°",
      "30°"
    ],
    ans: 3,
    trick: "consecutive angles of a parallelogram are SUPPLEMENTARY, not equal, so find the whole angle at A first — and only then take off the part the diagonal cuts away",
    why: "Angle A = 180 − 110 = 70, and x = 70 − 40 = 30.",
    traps: [
      "A: the whole angle at A given, the diagonal's part not removed.",
      "B: the two given angles simply added.",
      "C: the marked part copied out as the answer.",
    ],
  },

  // =========================================== CALCULUS AND PROBABILITY
  {
    sig: "limit-at-infinity-with-an-absolute-value",
    code: "SAAT-M-CAL.55", ses: 93, lvl: 4,
    stem: "Find the limit below.",
    stemEq: "h_li",
    opts: [
      "3",
      "−3",
      "0",
      "6"
    ],
    ans: 0,
    trick: "for x running to PLUS infinity the modulus is just x, so x|x| behaves like x² — the limit is then the ratio of the leading coefficients, and the sign only flips if x runs the other way",
    why: "For large positive x, (3x|x| + 5)/(x² − 4x) → 3x²/x² = 3.",
    traps: [
      "B: the modulus handled as though x ran to minus infinity.",
      "C: the numerator read as first degree.",
      "D: the modulus counted a second time.",
    ],
  },
  {
    sig: "solve-for-the-upper-limit-of-an-integral",
    code: "SAAT-M-CAL.56", ses: 112, lvl: 4,
    stem: "Find the value of n for which the integral below equals 26.",
    stemEq: "h_ul",
    opts: [
      "1",
      "3",
      "27",
      "26"
    ],
    ans: 1,
    trick: "evaluate the antiderivative at BOTH limits before solving — dropping the lower one leaves an equation with no whole-number answer, and the cube itself is offered in place of the number",
    why: "[x³] from 1 to n is n³ − 1 = 26, so n³ = 27 and n = 3.",
    traps: [
      "A: the lower limit returned.",
      "C: n³ reported instead of n.",
      "D: the value of the integral copied out as the answer.",
    ],
  },
  {
    sig: "normal-asymmetric-band-percentage",
    code: "SAAT-M-STA.28", ses: 42, lvl: 4,
    stem: "A test has a normal distribution with mean 500 and standard deviation 40. What percentage of scores lie between 460 and 580?",
    opts: [
      "68%",
      "47.5%",
      "81.5%",
      "95%"
    ],
    ans: 2,
    trick: "the band is NOT symmetric — one standard deviation below the mean but two above — so add the two halves separately instead of reaching for 68 or 95",
    why: "34% lies from 460 to 500 and 47.5% from 500 to 580, giving 81.5%.",
    traps: [
      "A: the symmetric one-deviation band used.",
      "B: only the upper half counted.",
      "D: the symmetric two-deviation band used.",
    ],
  },
  {
    sig: "independence-and-the-gambler-fallacy",
    code: "SAAT-M-STA.29", ses: 43, lvl: 3,
    stem: "A fair coin has landed heads five times in a row. What is the probability that the next toss is heads?",
    opts: [
      "1.6%",
      "0%",
      "98.4%",
      "50%"
    ],
    ans: 3,
    trick: "the tosses are INDEPENDENT and the coin has no memory, so the run before it changes nothing — the chance of six heads in a row is a different question from the chance of the sixth",
    why: "Each toss of a fair coin is independent, so the probability stays 1/2.",
    traps: [
      "A: the probability of the whole run of six given instead.",
      "B: the run treated as making another head impossible.",
      "C: the complement of the run's probability.",
    ],
  },
];
