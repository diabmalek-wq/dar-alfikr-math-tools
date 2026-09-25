// ---------------------------------------------------------------------------
// SIMULATED GAT BANK — part K: skills from the computerised-section inventory.
//
// WHAT THIS PART IS, AND WHAT IT IS NOT. The source was a circulated Arabic
// recall booklet for the computerised sitting. Its questions are candidate
// recollections, which ETEC retires once they circulate — what carries over to
// the next form is the IDEA, not the item. So what was taken here is the idea:
// a one-line skill and the trap it turns on, nothing else. No stem, number set,
// option list or figure crossed over. The twenty-one items below were written
// from the skill names, with new numbers, new Saudi contexts and figures drawn
// from scratch to the house spec, and every answer re-derived in verify_sim.py.
//
// Roughly two thirds of the booklet's quantitative skills were already in the
// bank — inverse proportion, two-digit digit conditions, combined work rate,
// day-of-week cycles, comparing powers by a common exponent, percent complement.
// Those were left alone rather than duplicated, which is the same rule every
// other part of this bank is built under.
//
// Three of these are worth the teaching time on their own:
//   · the reflex angle in an arrowhead quadrilateral (item 14),
//   · the cylinder comparison whose answer is genuinely "not enough
//     information" (item 15) — the bank is short of honest (D) answers,
//   · the circle-versus-triangle comparison (item 16), where the picture
//     suggests one answer and the arithmetic gives the other.
// ---------------------------------------------------------------------------
module.exports = [

// ============================================================== ARITHMETIC
{ sig: "half-of-a-power", code: "GAT-Q-ARI.4", lvl: 2,
  stem: "Find half of the number below.", stemEq: "k_pow50",
  opts: [{ eq: "k_h1" }, { eq: "k_h2" }, { eq: "k_h3" }, { eq: "k_h4" }], ans: 1,
  trick: "halving means dividing by 2, and 2 is 2¹ — so the exponent drops by ONE. Halving the exponent is the mistake the question is built around",
  why: "2⁵⁰ ÷ 2 = 2⁵⁰⁻¹ = 2⁴⁹.",
  traps: ["A: the exponent halved instead of reduced by one — the trap this item exists for.",
          "C: 2 subtracted from the number rather than divided out.",
          "D: the base halved instead of the value."] },

{ sig: "digit-sum-of-square", code: "GAT-Q-ARI.3", lvl: 2,
  stem: "Find the sum of the digits of the number below.", stemEq: "k_sq999",
  opts: ["18", "27", "36", "81"], ans: 1,
  trick: "999 is 1000 − 1, so the square is 1 000 000 − 2000 + 1 = 998 001 — square it that way and you never do a long multiplication",
  why: "999² = 998 001, and 9 + 9 + 8 + 0 + 0 + 1 = 27.",
  traps: ["A: only the first three digits added.",
          "C: the digit sum of 999 squared, 27, then confused with 9 × 4.",
          "D: the digit sum of 999 multiplied by itself."] },

{ sig: "extreme-numbers-by-digit-count", code: "GAT-Q-ARI.1", lvl: 2,
  stem: "Find the difference between the smallest three-digit odd number and the largest two-digit even number.",
  opts: ["1", "2", "3", "4"], ans: 2,
  trick: "build each number to its own two conditions — smallest three-digit is 100, but it must be ODD, so it is 101; largest two-digit is 99, but it must be EVEN, so it is 98",
  why: "101 − 98 = 3.",
  traps: ["A: 100 − 99 taken, both conditions ignored.",
          "B: only one of the two conditions applied.",
          "D: 102 − 98 taken."] },

{ sig: "difference-of-powers-of-ten", code: "GAT-Q-ARI.4", lvl: 2,
  stem: "Find the value below.", stemEq: "k_powdiff",
  opts: [{ eq: "k_d2" }, { eq: "k_d1" }, { eq: "k_d3" }, { eq: "k_d4" }], ans: 1,
  trick: "powers SUBTRACT as numbers, not as exponents — factor out the smaller power: 10⁶(10 − 1)",
  why: "10⁷ − 10⁶ = 10⁶(10 − 1) = 9 × 10⁶.",
  traps: ["A: the exponents subtracted, giving 10¹.",
          "C: only one power counted.",
          "D: the 9 attached to the larger power."] },

{ sig: "product-of-decimals-standard-form", code: "GAT-Q-ARI.4", lvl: 2,
  stem: "Write the value below in scientific notation.", stemEq: "k_decprod",
  opts: [{ eq: "k_p2" }, { eq: "k_p1" }, { eq: "k_p4" }, { eq: "k_p3" }], ans: 1,
  trick: "multiply the digits and count the decimal places SEPARATELY — 3 × 3 × 3 = 27 and the places are 1 + 2 + 3 = 6, which puts 27 six places down",
  why: "0.3 × 0.03 × 0.003 = 0.000 027 = 2.7 × 10⁻⁵.",
  traps: ["A: one decimal place too many.",
          "C: the digits multiplied as 3 × 3 = 9.",
          "D: correct in value but not written with a number between 1 and 10."] },

{ sig: "ratio-as-fraction-direction", code: "GAT-Q-ARI.3", lvl: 2,
  stem: "A household's water use compared with its electricity use is given below. If the water use is 20 units, what is the electricity use, in the same units?",
  stemEq: "k_ratio",
  opts: ["1", "20", "40", "400"], ans: 3,
  trick: "read which quantity is on TOP — water is the numerator, so electricity is twenty times the water, not a twentieth of it",
  why: "water ÷ electricity = 1/20, so electricity = 20 × water = 20 × 20 = 400 units.",
  traps: ["A: the fraction read as the answer itself.",
          "B: the water figure repeated.",
          "C: 20 doubled, the ratio applied once and halved."] },

{ sig: "percent-part-to-complement-count", code: "GAT-Q-ARI.3", lvl: 2,
  stem: "A student answered 60% of the questions on a test, and that 60% came to 30 questions. How many questions did he leave unanswered?",
  opts: ["12", "18", "20", "50"], ans: 2,
  trick: "the 30 is the PART, not the whole — find the whole first, then take the part off. Working out 40% of 30 is the fast wrong answer",
  why: "30 is 60% of the test, so the test has 30 ÷ 0.6 = 50 questions and 50 − 30 = 20 were left.",
  traps: ["A: 40% of 30 taken.",
          "B: 60% of 30 taken.",
          "D: the total given rather than the number left."] },

// ================================================================= ALGEBRA
{ sig: "even-powers-never-negative", code: "GAT-Q-ALG.4", lvl: 2,
  stem: "Given the condition below, which of the following can never be negative?",
  stemEq: "k_xy",
  opts: [{ eq: "k_s2" }, { eq: "k_s3" }, { eq: "k_s1" }, { eq: "k_s4" }], ans: 2,
  trick: "count the powers: a term where EVERY letter carries an even power is a square, and a square is never negative whatever the signs underneath",
  why: "xy < 0 means x and y have opposite signs, so xy is negative. But x²y² = (xy)², and a square is never negative.",
  traps: ["A: x²y keeps the sign of y, so it can be negative.",
          "B: xy² keeps the sign of x.",
          "D: x³y³ = (xy)³, an odd power, so it stays negative."] },

{ sig: "mean-of-algebraic-terms", code: "GAT-Q-ALG.5", lvl: 2,
  stem: "Find the mean of the three expressions below.", stemEq: "k_terms",
  opts: [{ eq: "k_m2" }, { eq: "k_m1" }, { eq: "k_m3" }, { eq: "k_m4" }], ans: 1,
  trick: "the mean of expressions works exactly like the mean of numbers — add and divide by three. Both the n terms and the numbers get divided",
  why: "The sum is 3n + 12, and (3n + 12) ÷ 3 = n + 4.",
  traps: ["A: the middle expression given instead of the mean.",
          "C: the sum given, the division forgotten — the trap this item exists for.",
          "D: only the numbers averaged and n left alone."] },

{ sig: "equal-after-opposite-percent-changes", code: "GAT-Q-ALG.5", lvl: 3,
  stem: "A quantity x is increased by 20% and a quantity y is decreased by 20%, after which the two are equal. Find the ratio x : y.",
  opts: ["1 : 1", "2 : 3", "3 : 2", "4 : 1"], ans: 1,
  trick: "turn each change into a MULTIPLIER — 1.2x and 0.8y — set them equal, and the ratio falls straight out. The two 20% changes do not cancel",
  why: "1.2x = 0.8y gives x/y = 0.8/1.2 = 2/3, so x : y = 2 : 3.",
  traps: ["A: the equal percentages assumed to leave the quantities equal — the trap this item exists for.",
          "C: the ratio written the wrong way round.",
          "D: 120 and 80 subtracted rather than divided."] },

// ================================================================ GEOMETRY
{ sig: "square-minus-corner-triangle", code: "GAT-Q-GEO.4", lvl: 3,
  stem: "A corner has been cut off the square below by a straight line, and the lengths shown are in centimetres. Find the shaded area, in square centimetres.",
  fig: "k_corner_cut", figW: 1.95,
  opts: ["52", "54", "58", "64"], ans: 2,
  trick: "the labels give what is LEFT of each side, not the cut piece — subtract each from 8 to get the triangle's legs before taking its area off the square",
  why: "The triangle's legs are 8 − 4 = 4 cm and 8 − 5 = 3 cm, so its area is 6 cm². The square is 64 cm², leaving 64 − 6 = 58 cm².",
  traps: ["A: the triangle taken as 4 by 3 without halving.",
          "B: the legs read straight off the figure as 4 and 5, giving a triangle of 10.",
          "D: the whole square given, the cut ignored."] },

{ sig: "angles-round-point-expression", code: "GAT-Q-GEO.1", lvl: 3,
  stem: "Three rays leave a single point as shown. Find the value of 180 − x − y.",
  fig: "k_rays_expr", figW: 1.9,
  opts: [{ eq: "k_a1" }, { eq: "k_a2" }, { eq: "k_a3" }, { eq: "k_a4" }], ans: 0,
  trick: "write the turn first: 2x + 2y + a = 360. Divide the whole line by 2 and x + y + a/2 = 180 appears, which is the expression asked for",
  why: "2x + 2y + a = 360, so x + y + a/2 = 180 and 180 − x − y = a/2.",
  traps: ["B: the halving of the whole equation forgotten.",
          "C: the equation multiplied by 2 instead of divided.",
          "D: a straight line used, 180 − a, instead of the full turn."] },

{ sig: "count-rectangles-in-strip", code: "GAT-Q-GEO.4", lvl: 2,
  stem: "How many rectangles of any size appear in the figure below?",
  fig: "k_strip_rects", figW: 2.5,
  opts: ["6", "12", "21", "36"], ans: 2,
  trick: "a rectangle is fixed by choosing TWO of the seven vertical lines, so the count is 1 + 2 + … + 6, not the number of cells",
  why: "With 6 cells there are 7 vertical lines and any two of them bound a rectangle: 7 × 6 ÷ 2 = 21.",
  traps: ["A: only the single cells counted.",
          "B: the cells counted twice over.",
          "D: 6² given."] },

{ sig: "concave-quadrilateral-reflex-angle", code: "GAT-Q-GEO.1", lvl: 3,
  stem: "Find the value of x in the four-sided figure below, in degrees.",
  fig: "k_dart", figW: 3.4,
  opts: ["110", "140", "180", "250"], ans: 3,
  trick: "the angles of ANY quadrilateral add to 360, concave or not — and the angle at a dent is the REFLEX one, the one that opens inside the shape",
  why: "60 + 30 + 20 = 110, so x = 360 − 110 = 250°.",
  traps: ["A: the three given angles added and offered as the answer.",
          "B: 250 confused with the outside angle 360 − 250 = 110, then doubled.",
          "C: the three angles subtracted from 180 as if this were a triangle."] },

{ sig: "cylinder-compare-insufficient-data", code: "GAT-Q-GEO.5", lvl: 3,
  stem: "In a cylinder, the height is equal to the square of the radius of the base. Which quantity is greater: (A) the circumference of the base, or (B) the height?",
  opts: ["A is greater", "B is greater", "they are equal", "not enough information"], ans: 3,
  trick: "write both in terms of r — 2πr against r² — and try TWO sizes. At r = 2 the circumference wins; at r = 10 the height does. A comparison that changes with the size has no single answer",
  why: "The circumference is 2πr ≈ 6.28r and the height is r². For r = 2 the circumference is larger (12.6 against 4); for r = 10 the height is larger (100 against 62.8). Since r is not given, neither can be named.",
  traps: ["A: only a small radius tried.",
          "B: only a large radius tried.",
          "C: 6.28r and r² read as the same expression."] },

{ sig: "compare-circumference-with-triangle-area", code: "GAT-Q-GEO.3", lvl: 3,
  stem: "The circle below has circumference 20π, and the triangle stands on a diameter with its apex on the circle. Which is greater as a NUMBER: (A) the circumference of the circle, or (B) the area of the triangle? (Take π = 3.14.)",
  fig: "k_circ_tri", figW: 1.9,
  opts: ["A is greater", "B is greater", "they are equal", "not enough information"], ans: 1,
  trick: "the triangle's base is the DIAMETER and its height is the radius, so its area is r² — then compare the two as plain numbers and ignore that one is a length and the other an area",
  why: "2πr = 20π gives r = 10, so the circumference is 62.8 and the triangle's area is ½ × 20 × 10 = 100. The area is the greater number.",
  traps: ["A: the circle read as the bigger figure because it encloses the triangle.",
          "C: 20π assumed to make both quantities the same.",
          "D: r is fully determined by the circumference, so the comparison can be made."] },

{ sig: "three-quarter-sector-diameter", code: "GAT-Q-GEO.3", lvl: 2,
  stem: "In the figure below, three quarters of a circle of diameter 8 cm are shaded. Find the shaded area, in square centimetres.",
  fig: "k_three_quarter", figW: 1.55,
  opts: [{ eq: "k_q1" }, { eq: "k_q2" }, { eq: "k_q3" }, { eq: "k_q4" }], ans: 2,
  trick: "the 8 is the DIAMETER — halve it before it goes anywhere near the area formula. Every wrong option here comes from a radius of 8",
  why: "The radius is 4 cm, so the whole circle is 16π cm² and three quarters of it is 12π cm².",
  traps: ["A: a quarter of the circle given instead of three quarters.",
          "B: the diameter used as the radius and then quartered.",
          "D: the whole circle given, the three quarters ignored."] },

// ===================================================================== DATA
{ sig: "probability-prime-in-range", code: "GAT-Q-DAT.3", lvl: 2,
  stem: "One card is drawn at random from cards numbered 1 to 10. What is the probability that the number on it is prime?",
  opts: [{ eq: "k_pr3" }, { eq: "k_pr4" }, { eq: "k_pr1" }, { eq: "k_pr2" }], ans: 2,
  trick: "1 is NOT prime and 2 IS — those two facts decide this question, and both of them are the ones students get wrong",
  why: "The primes up to 10 are 2, 3, 5 and 7: four of ten cards, so the probability is 4/10 = 2/5.",
  traps: ["A: only 2, 3 counted as prime.",
          "B: 1 counted as prime and 2 left out.",
          "D: the odd numbers counted instead of the primes."] },

{ sig: "bar-share-per-person", code: "GAT-Q-DAT.1", lvl: 2,
  stem: "The chart below shows how many employees each branch has. A bonus of 60 000 SAR is shared equally among the employees of branch 1. How many riyals does each of them receive?",
  fig: "k_bar_branches", figW: 2.77,
  opts: ["400", "500", "600", "1 000"], ans: 0,
  trick: "read the ONE bar the question names before doing any arithmetic — the other four bars are there to be added by mistake",
  why: "Branch 1 has 150 employees, and 60 000 ÷ 150 = 400 SAR each.",
  traps: ["B: 120 employees read off, the wrong bar.",
          "C: 100 used as a round guess for the bar height.",
          "D: 60 employees read off the axis instead of the bar."] },

{ sig: "table-score-with-penalty", code: "GAT-Q-DAT.1", lvl: 2,
  stem: "The table below shows how many answers each candidate got right and wrong on each paper. A right answer scores 2 points and a wrong answer loses 1 point. Which candidate scored highest on the computing paper?",
  fig: "k_table_scores", figW: 2.9,
  opts: ["Candidate 1", "Candidate 2", "Candidate 3", "Candidate 4"], ans: 3,
  trick: "the wrong answers COST points, so score each candidate as 2 × right − wrong. Picking the most right answers is the shortcut the table punishes",
  why: "On computing: candidate 1 scores 8 − 2 = 6, candidate 2 scores 8 − 2 = 6, candidate 3 scores 8 − 3 = 5 and candidate 4 scores 10 − 1 = 9. Candidate 4 is highest.",
  traps: ["A: the row read across all three papers instead of the computing column.",
          "B: the penalty ignored, leaving a tie read as the answer.",
          "C: the most wrong answers mistaken for the most right."] },

// ================================================================ WORD LOGIC
{ sig: "minute-hand-degrees", code: "GAT-Q-LOG.1", lvl: 2,
  stem: "A clock is 8 minutes slow. Through what angle must its minute hand be turned forward to correct it?",
  opts: ["8°", "48°", "96°", "240°"], ans: 1,
  trick: "the minute hand sweeps 360° in 60 minutes, so it turns 6° for every minute — this one number answers every question of this kind",
  why: "8 × 6 = 48°.",
  traps: ["A: the minutes given as degrees.",
          "C: 12° per minute used, the hour scale by mistake.",
          "D: 30° per minute used, the hour-hand mark spacing."] },

];
