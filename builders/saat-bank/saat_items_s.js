// SAAT BANK — part S: ideas read (skill and trap only) from the 205-item FikrCounts SAAT set (6 pages, Nov 2026).
// Stems, numbers and options are original; every key is re-derived by a predicate (sympy / brute force) in spec_s.py, not copied from the source key.
module.exports = [
  {
    "sig": "parameter-for-a-linear-equation-with-no-solution",
    "code": "SAAT-S.1",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 3,
    "stem": "For which value of m does the equation mx + 7 = 4x + 2m have no solution?",
    "opts": [
      "4",
      "7/2",
      "2",
      "−4"
    ],
    "ans": 0,
    "trick": "no solution needs the x-terms to cancel (m − 4 = 0) while the constants stay different — checking the constants is the last step",
    "why": "Move terms: (m − 4)x = 2m − 7. At m = 4 this reads 0·x = 1, which is never true.",
    "traps": [
      "B: 7/2 — the constant side 2m − 7 was set to zero, but then the equation still has the solution x = 0.",
      "C: 2 — the m on the left was matched to the 2 in 2m.",
      "D: −4 — the sign of the coefficient was flipped when moving 4x across."
    ]
  },
  {
    "sig": "sum-of-two-parameters-for-infinitely-many-solutions",
    "code": "SAAT-S.2",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 3,
    "stem": "The equation 3(2x − 1) + a = bx + 5 is true for every real value of x. What is the value of a + b?",
    "opts": [
      "2",
      "14",
      "8",
      "6"
    ],
    "ans": 1,
    "trick": "'true for every x' means the x-coefficients match AND the constants match — two conditions, two unknowns",
    "why": "6x − 3 + a = bx + 5. Matching x-terms gives b = 6; matching constants gives a − 3 = 5, so a = 8. Then a + b = 14.",
    "traps": [
      "A: 2 — the difference b − a = 6 − 8 was reported with the sign changed.",
      "C: 8 — only a was found; b was forgotten.",
      "D: 6 — only b was found; a was forgotten."
    ]
  },
  {
    "sig": "pick-the-equation-with-exactly-one-solution",
    "code": "SAAT-S.3",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 2,
    "stem": "Which of the following equations has exactly one solution?",
    "opts": [
      "2x + 5 = 2x − 1",
      "−x + 4 = 4 − x",
      "7x − 2 = 3x + 10",
      "6x − 9 = 3(2x − 3)"
    ],
    "ans": 2,
    "trick": "simplify both sides first: matching x-coefficients mean 'none' or 'all', never 'exactly one'",
    "why": "7x − 2 = 3x + 10 gives 4x = 12, x = 3. The other three have equal x-coefficients, so they are either never true or always true.",
    "traps": [
      "A: 2x + 5 = 2x − 1 — it simplifies to 5 = −1, so no x works.",
      "B: −x + 4 = 4 − x — both sides are identical, so every x works.",
      "D: 6x − 9 = 3(2x − 3) — it simplifies to 0 = 0, so every x works."
    ]
  },
  {
    "sig": "system-parameter-that-gives-no-solution",
    "code": "SAAT-S.4",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 3,
    "stem": "For which value of k does the system kx + 6y = 7 and 2x − 3y = 4 have no solution?",
    "opts": [
      "4",
      "−9",
      "9",
      "−4"
    ],
    "ans": 3,
    "trick": "no solution = parallel lines: the x- and y-coefficients are proportional but the constants are not",
    "why": "Multiply the second equation by −2: −4x + 6y = −8. The y-terms already match the first equation, so k = −4, and 7 ≠ −8 keeps the lines distinct.",
    "traps": [
      "A: 4 — the sign was lost when scaling the second equation by −2.",
      "B: −9 — the two y-coefficients were multiplied instead of matched.",
      "C: 9 — the two y-coefficients were multiplied and the sign was lost."
    ]
  },
  {
    "sig": "two-parameters-for-infinitely-many-system-solutions",
    "code": "SAAT-S.5",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 3,
    "stem": "The system ax + 6y = 12 and 2x + 3y = c has infinitely many solutions. What is a + c?",
    "opts": [
      "10",
      "4",
      "6",
      "16"
    ],
    "ans": 0,
    "trick": "infinitely many solutions = the second equation is a multiple of the first, so EVERY coefficient and the constant scale together",
    "why": "Doubling 2x + 3y = c gives 4x + 6y = 2c. Matching ax + 6y = 12 gives a = 4 and 2c = 12, so c = 6 and a + c = 10.",
    "traps": [
      "B: 4 — only a was found.",
      "C: 6 — only c was found.",
      "D: 16 — the second equation was doubled but c was not."
    ]
  },
  {
    "sig": "value-that-breaks-a-unique-solution",
    "code": "SAAT-S.6",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 3,
    "stem": "The system 5x + ky = 3 and x + 4y = 2 has exactly one solution for every real k except one value. What is that value?",
    "opts": [
      "10",
      "20",
      "4",
      "5"
    ],
    "ans": 1,
    "trick": "a unique solution fails exactly when the coefficient determinant is zero: 5·4 − k·1 = 0",
    "why": "The lines are parallel (or the same) when 5/1 = k/4, so k = 20. For every other k they cross once.",
    "traps": [
      "A: 10 — the equations were compared using the constants 3 and 2.",
      "C: 4 — the coefficient of y in the second equation was reported directly.",
      "D: 5 — the coefficient of x in the first equation was reported directly."
    ]
  },
  {
    "sig": "difference-of-two-variables-without-solving",
    "code": "SAAT-S.7",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 2,
    "stem": "If 4x + 3y = 23 and 3x + 4y = 19, what is the value of x − y?",
    "opts": [
      "42",
      "2",
      "4",
      "6"
    ],
    "ans": 2,
    "trick": "when the coefficients swap, SUBTRACT the equations for x − y and ADD them for x + y — no need to find x and y",
    "why": "Subtracting gives (4x + 3y) − (3x + 4y) = x − y = 23 − 19 = 4.",
    "traps": [
      "A: 42 — the equations were added and the total was reported.",
      "B: 2 — the two constants were subtracted and halved.",
      "D: 6 — the equations were added and divided, giving x + y instead."
    ]
  },
  {
    "sig": "target-combination-of-two-equations",
    "code": "SAAT-S.8",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 2,
    "stem": "If 2a + 3b = 12 and 4a − b = 10, what is the value of 6a + 2b?",
    "opts": [
      "11",
      "44",
      "2",
      "22"
    ],
    "ans": 3,
    "trick": "look for the combination that is asked for — here simply adding the two equations produces 6a + 2b",
    "why": "(2a + 3b) + (4a − b) = 6a + 2b = 12 + 10 = 22.",
    "traps": [
      "A: 11 — the sum 22 was halved because the coefficients looked like they doubled.",
      "B: 44 — the sum was doubled.",
      "C: 2 — the right-hand sides were subtracted."
    ]
  },
  {
    "sig": "triangle-bounded-by-two-lines-and-the-y-axis",
    "code": "SAAT-S.9",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 3,
    "stem": "The lines y = 2x − 4 and y = −x + 5 and the y-axis form a triangle. What is its area?",
    "opts": [
      "27/2",
      "27",
      "9",
      "3"
    ],
    "ans": 0,
    "trick": "with the y-axis as one side, the base is the gap between the y-intercepts and the height is the x-coordinate of the crossing point",
    "why": "The lines cross where 2x − 4 = −x + 5, so x = 3. The y-intercepts are −4 and 5, so the base is 9 and the area is ½ · 9 · 3 = 27/2.",
    "traps": [
      "B: 27 — the factor of 1/2 was left out.",
      "C: 9 — the distance between the y-intercepts was used as if it were the area.",
      "D: 3 — the x-axis was used as the third side, so the wrong triangle was measured."
    ]
  },
  {
    "sig": "count-the-integers-in-a-compound-inequality",
    "code": "SAAT-S.10",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 2,
    "stem": "How many integers x satisfy −5 < 2x + 1 ≤ 13?",
    "opts": [
      "7",
      "9",
      "8",
      "10"
    ],
    "ans": 1,
    "trick": "solve the double inequality first, then count integers while checking each end for < or ≤ — do not subtract the ends",
    "why": "Subtract 1: −6 < 2x ≤ 12, then divide by 2: −3 < x ≤ 6. The integers −2, −1, 0, 1, 2, 3, 4, 5, 6 give 9.",
    "traps": [
      "A: 7 — both endpoints were dropped.",
      "C: 8 — the right endpoint x = 6 was dropped although ≤ includes it.",
      "D: 10 — the left endpoint x = −3 was counted although < excludes it."
    ]
  },
  {
    "sig": "count-the-integers-in-an-absolute-value-inequality",
    "code": "SAAT-S.11",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 2,
    "stem": "How many integers x satisfy |3x − 2| < 10?",
    "opts": [
      "7",
      "4",
      "6",
      "5"
    ],
    "ans": 2,
    "trick": "|expression| < c is a double inequality; the ends are usually not integers, so round toward the inside",
    "why": "−10 < 3x − 2 < 10 gives −8 < 3x < 12, so −8/3 < x < 4. The integers −2, −1, 0, 1, 2, 3 give 6.",
    "traps": [
      "A: 7 — the endpoint 4 was counted although the inequality is strict.",
      "B: 4 — only the positive side was counted.",
      "D: 5 — the lower end −8/3 was rounded the wrong way so −2 was lost."
    ]
  },
  {
    "sig": "coefficient-from-a-stated-solution-set",
    "code": "SAAT-S.12",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 3,
    "stem": "The solution set of 4x − 3k > 9 is x > 6. What is the value of k?",
    "opts": [
      "−5",
      "−1",
      "15",
      "5"
    ],
    "ans": 3,
    "trick": "solve the inequality for x in terms of k, then match its boundary to the boundary you are given",
    "why": "4x > 9 + 3k gives x > (9 + 3k)/4. Setting (9 + 3k)/4 = 6 gives 9 + 3k = 24, so k = 5.",
    "traps": [
      "A: −5 — 3k was moved across with the wrong sign, giving (9 − 3k)/4.",
      "B: −1 — the 4 was not divided out of 3k, giving x > 9 + 3k.",
      "C: 15 — the final division by 3 was forgotten (3k = 15)."
    ]
  },
  {
    "sig": "centre-and-radius-product-from-an-interval",
    "code": "SAAT-S.13",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 3,
    "stem": "The solution set of |x − p| < q, where q > 0, is the interval (−3, 9). What is the value of pq?",
    "opts": [
      "18",
      "9",
      "27",
      "12"
    ],
    "ans": 0,
    "trick": "|x − p| < q describes the points within q of the centre p, so p is the midpoint and q is HALF the width",
    "why": "The midpoint of (−3, 9) is p = 3 and the half-width is q = 6, so pq = 18.",
    "traps": [
      "B: 9 — p + q = 9 was reported, which is the right end of the interval.",
      "C: 27 — the right end 9 was multiplied by 3.",
      "D: 12 — the width 12 of the interval was reported."
    ]
  },
  {
    "sig": "parameter-from-a-closed-absolute-value-solution-set",
    "code": "SAAT-S.14",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 3,
    "stem": "The solution set of |3x − k| ≤ 12 is [−2, 6]. What is the value of k?",
    "opts": [
      "12",
      "6",
      "2",
      "4"
    ],
    "ans": 1,
    "trick": "|3x − k| ≤ 12 means −12 ≤ 3x − k ≤ 12, so x runs from (k − 12)/3 to (k + 12)/3 — match one end",
    "why": "(k − 12)/3 = −2 gives k = 6, and (k + 12)/3 = 6 agrees.",
    "traps": [
      "A: 12 — the bound in the inequality was copied.",
      "C: 2 — k was taken as the average of the endpoints and the 3 was ignored.",
      "D: 4 — the half-width 4 of the interval was reported."
    ]
  },
  {
    "sig": "sum-of-the-two-solutions-of-an-absolute-value-equation",
    "code": "SAAT-S.15",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 2,
    "stem": "What is the sum of the solutions of |4x − 3| = 9?",
    "opts": [
      "−3/2",
      "0",
      "3/2",
      "3"
    ],
    "ans": 2,
    "trick": "an absolute value equation has two cases — solve both before you add",
    "why": "4x − 3 = 9 gives x = 3 and 4x − 3 = −9 gives x = −3/2, so the sum is 3/2.",
    "traps": [
      "A: −3/2 — only the negative case 4x − 3 = −9 was solved.",
      "B: 0 — the two right-hand sides 9 and −9 were added.",
      "D: 3 — only the positive case 4x − 3 = 9 was solved."
    ]
  },
  {
    "sig": "product-of-the-solutions-when-two-absolute-values-are-equal",
    "code": "SAAT-S.16",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 3,
    "stem": "What is the product of the solutions of |x + 2| = |3x − 4|?",
    "opts": [
      "7/2",
      "3",
      "−3/2",
      "3/2"
    ],
    "ans": 3,
    "trick": "|A| = |B| splits into A = B and A = −B — use both cases and then multiply",
    "why": "x + 2 = 3x − 4 gives x = 3; x + 2 = −(3x − 4) gives x = 1/2. The product is 3/2.",
    "traps": [
      "A: 7/2 — the sum of the solutions was reported.",
      "B: 3 — only the first case x + 2 = 3x − 4 was solved and its solution was reported.",
      "C: −3/2 — the sign of the second solution was mishandled."
    ]
  },
  {
    "sig": "parameter-for-exactly-one-absolute-value-solution",
    "code": "SAAT-S.17",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 3,
    "stem": "For which value of m does the equation |2x − 1| = 3m − 12 have exactly one solution?",
    "opts": [
      "4",
      "5",
      "6",
      "3"
    ],
    "ans": 0,
    "trick": "|expression| = c has one solution only when c = 0; two when c > 0; none when c < 0",
    "why": "Exactly one solution needs 3m − 12 = 0, so m = 4 (then 2x − 1 = 0 gives x = 1/2).",
    "traps": [
      "B: 5 — the right-hand side was made positive rather than zero.",
      "C: 6 — the right-hand side was set equal to 6.",
      "D: 3 — the right-hand side was set equal to −3."
    ]
  },
  {
    "sig": "tolerance-as-an-absolute-value-inequality",
    "code": "SAAT-S.18",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 2,
    "stem": "A pipe is labelled 80 cm long with a tolerance of 3%. Which inequality describes the acceptable length L, in cm?",
    "opts": [
      "|L − 77.6| ≤ 2.4",
      "|L − 80| ≤ 2.4",
      "|L − 80| ≤ 3",
      "|L − 2.4| ≤ 80"
    ],
    "ans": 1,
    "trick": "tolerance of p% means the allowed error is p% OF THE LABEL, and the centre of the interval is the label",
    "why": "3% of 80 is 2.4, so the acceptable lengths satisfy |L − 80| ≤ 2.4.",
    "traps": [
      "A: |L − 77.6| ≤ 2.4 — the centre was moved to the lower limit.",
      "C: |L − 80| ≤ 3 — the percentage was used as if it were centimetres.",
      "D: |L − 2.4| ≤ 80 — the target and the allowed error were swapped."
    ]
  },
  {
    "sig": "within-a-distance-as-an-absolute-value-inequality",
    "code": "SAAT-S.19",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 2,
    "stem": "Which inequality describes all real numbers within 5 units of −2 on the number line?",
    "opts": [
      "|x + 5| ≤ 2",
      "|x + 2| ≥ 5",
      "|x + 2| ≤ 5",
      "|x − 2| ≤ 5"
    ],
    "ans": 2,
    "trick": "'within r of c' is |x − c| ≤ r — and subtracting a negative centre gives x + 2",
    "why": "The centre is −2, so |x − (−2)| = |x + 2|, and 'within 5' means ≤ 5.",
    "traps": [
      "A: |x + 5| ≤ 2 — the centre and the radius were swapped.",
      "B: |x + 2| ≥ 5 — 'at least 5 away' was written instead of 'within 5'.",
      "D: |x − 2| ≤ 5 — the centre was written as +2 instead of −2."
    ]
  },
  {
    "sig": "intersection-of-two-absolute-value-conditions",
    "code": "SAAT-S.20",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 3,
    "stem": "What is the set of all real numbers x that satisfy both |x − 2| < 5 and |x + 1| ≥ 2?",
    "opts": [
      "(−3, 7)",
      "(−3, 1]",
      "[1, 7]",
      "[1, 7)"
    ],
    "ans": 3,
    "trick": "solve each condition as an interval, draw both on one line, and keep only the overlap — mind which ends are open",
    "why": "|x − 2| < 5 gives (−3, 7). |x + 1| ≥ 2 gives x ≤ −3 or x ≥ 1. The overlap is [1, 7).",
    "traps": [
      "A: (−3, 7) — the second condition was ignored.",
      "B: (−3, 1] — the part that FAILS the second condition was kept.",
      "C: [1, 7] — the strict end of the first condition was made inclusive."
    ]
  },
  {
    "sig": "absolute-value-at-most-zero",
    "code": "SAAT-S.21",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 2,
    "stem": "What is the solution set of |2x − 6| ≤ 0?",
    "opts": [
      "{3}",
      "∅",
      "(−∞, 3]",
      "all real numbers"
    ],
    "ans": 0,
    "trick": "an absolute value is never negative, so |A| ≤ 0 can only happen when A = 0 exactly",
    "why": "|2x − 6| ≤ 0 forces 2x − 6 = 0, so x = 3 and the solution set is {3}.",
    "traps": [
      "B: ∅ — 'at most 0' was read as impossible, but the value 0 itself is allowed.",
      "C: (−∞, 3] — the inequality was solved as if it were 2x − 6 ≤ 0.",
      "D: all real numbers — the absolute value was treated as always satisfying ≤."
    ]
  },
  {
    "sig": "greatest-integer-that-satisfies-a-strict-inequality",
    "code": "SAAT-S.22",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 2,
    "stem": "What is the greatest integer x that satisfies 7 − 3x > −8?",
    "opts": [
      "15",
      "4",
      "5",
      "6"
    ],
    "ans": 1,
    "trick": "dividing by a negative flips the sign, and a strict boundary itself is NOT allowed",
    "why": "−3x > −15 gives x < 5, so the greatest integer is 4.",
    "traps": [
      "A: 15 — the value of 3x was reported instead of x.",
      "C: 5 — the boundary value was accepted although the inequality is strict.",
      "D: 6 — the sign was not flipped when dividing by −3, giving x > 5, and the next integer was taken."
    ]
  },
  {
    "sig": "two-plans-and-a-budget-in-one-inequality",
    "code": "SAAT-S.23",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 3,
    "stem": "Plan P costs SAR 25 + 6g per month and plan Q costs SAR 55 + 3g per month, where g ≥ 0 is the number of gigabytes used. For which values of g is plan P cheaper than plan Q AND at most SAR 70?",
    "opts": [
      "0 ≤ g ≤ 7",
      "0 ≤ g ≤ 5",
      "0 ≤ g ≤ 15/2",
      "0 ≤ g < 10"
    ],
    "ans": 2,
    "trick": "two conditions joined by AND need BOTH solved separately, then the stricter bound wins",
    "why": "25 + 6g < 55 + 3g gives g < 10. 25 + 6g ≤ 70 gives g ≤ 15/2. The stricter bound is 15/2, so 0 ≤ g ≤ 15/2.",
    "traps": [
      "A: 0 ≤ g ≤ 7 — 15/2 was rounded down although g may be any non-negative number.",
      "B: 0 ≤ g ≤ 5 — the SAR 70 budget was applied to plan Q instead of plan P.",
      "D: 0 ≤ g < 10 — only the 'cheaper than Q' condition was used."
    ]
  },
  {
    "sig": "convert-a-temperature-range-through-a-formula",
    "code": "SAAT-S.24",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 3,
    "stem": "A medicine cooler must stay between 2°C and 8°C, inclusive. A sensor displays degrees Fahrenheit, where F = (9/5)C + 32. Which inequality gives the allowed readings F?",
    "opts": [
      "3.6 ≤ F ≤ 14.4",
      "34 ≤ F ≤ 40",
      "2 ≤ F ≤ 8",
      "35.6 ≤ F ≤ 46.4"
    ],
    "ans": 3,
    "trick": "apply the whole formula to BOTH ends: multiply by 9/5 first, then add 32",
    "why": "At 2°C, F = 3.6 + 32 = 35.6. At 8°C, F = 14.4 + 32 = 46.4. So 35.6 ≤ F ≤ 46.4.",
    "traps": [
      "A: 3.6 ≤ F ≤ 14.4 — only (9/5)C was computed and the +32 was left out.",
      "B: 34 ≤ F ≤ 40 — 32 was added to the Celsius values without the 9/5 factor.",
      "C: 2 ≤ F ≤ 8 — the Celsius bounds were copied."
    ]
  },
  {
    "sig": "strict-budget-with-an-exact-boundary",
    "code": "SAAT-S.25",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 2,
    "stem": "An internet café charges a SAR 30 joining fee plus SAR 7 per hour. Huda wants to pay less than SAR 100 in total. What is the greatest whole number of hours she can use?",
    "opts": [
      "9",
      "10",
      "13",
      "14"
    ],
    "ans": 0,
    "trick": "when the boundary lands on a whole number, a STRICT inequality excludes it — step down by one",
    "why": "30 + 7h < 100 gives h < 10. The greatest whole number below 10 is 9.",
    "traps": [
      "B: 10 — the boundary value was accepted, but 10 hours cost exactly SAR 100, which is not less than 100.",
      "C: 13 — the hourly rate 7 was subtracted from 100 instead of the joining fee.",
      "D: 14 — the joining fee was left out: 100 ÷ 7."
    ]
  },
  {
    "sig": "inequality-that-is-true-for-every-real-number",
    "code": "SAAT-S.26",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 2,
    "stem": "Which of the following inequalities is true for EVERY real number x?",
    "opts": [
      "|x| < 2",
      "3x + 2 < 3x + 7",
      "5(x − 1) ≥ 5x − 4",
      "x + 1 < x"
    ],
    "ans": 1,
    "trick": "if the x-terms cancel, what is left is a statement about numbers only — true means 'all x', false means 'no x'",
    "why": "3x + 2 < 3x + 7 reduces to 2 < 7, which is always true.",
    "traps": [
      "A: |x| < 2 — it is true only for −2 < x < 2.",
      "C: 5(x − 1) ≥ 5x − 4 — it simplifies to −5 ≥ −4, which is false, so it is never true.",
      "D: x + 1 < x — it simplifies to 1 < 0, which is never true."
    ]
  },
  {
    "sig": "make-a-variable-the-subject-of-a-surface-area-formula",
    "code": "SAAT-S.27",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 2,
    "stem": "The total surface area of a closed cylinder is S = 2πr(r + h). Which expression gives h?",
    "opts": [
      "h = (S − r)/(2πr)",
      "h = S/(2π) − r",
      "h = S/(2πr) − r",
      "h = S/(2πr) + r"
    ],
    "ans": 2,
    "trick": "undo the outside multiplication first (divide by 2πr), and only then move the r — do not touch the bracket early",
    "why": "S/(2πr) = r + h, so h = S/(2πr) − r.",
    "traps": [
      "A: h = (S − r)/(2πr) — r was subtracted from S before dividing, ignoring that r multiplies the bracket.",
      "B: h = S/(2π) − r — the division by r was forgotten.",
      "D: h = S/(2πr) + r — the r was added instead of subtracted after dividing."
    ]
  },
  {
    "sig": "isolate-x-when-it-appears-on-both-sides",
    "code": "SAAT-S.28",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 2,
    "stem": "If p(x − q) = r − sx, where p + s ≠ 0, what is x in terms of p, q, r and s?",
    "opts": [
      "x = (r − pq)/(p + s)",
      "x = (r + pq)/(p − s)",
      "x = (r + q)/(p + s)",
      "x = (r + pq)/(p + s)"
    ],
    "ans": 3,
    "trick": "distribute, gather every x-term on one side, factor x out, then divide by its coefficient",
    "why": "px − pq = r − sx gives px + sx = r + pq, so x(p + s) = r + pq and x = (r + pq)/(p + s).",
    "traps": [
      "A: x = (r − pq)/(p + s) — the sign of pq was lost when it crossed the equals sign.",
      "B: x = (r + pq)/(p − s) — the sx was moved with the wrong sign, giving p − s.",
      "C: x = (r + q)/(p + s) — p was not distributed across (x − q)."
    ]
  },
  {
    "sig": "combine-fractions-then-isolate-the-variable",
    "code": "SAAT-S.29",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 2,
    "stem": "If x/a − x/b = 1 with a, b > 0 and a ≠ b, what is x?",
    "opts": [
      "x = ab/(b − a)",
      "x = ab/(a − b)",
      "x = ab(b − a)",
      "x = (b − a)/(ab)"
    ],
    "ans": 0,
    "trick": "factor x out: x(1/a − 1/b) = 1, then combine the bracket over ab and flip",
    "why": "x(b − a)/(ab) = 1, so x = ab/(b − a).",
    "traps": [
      "B: x = ab/(a − b) — the subtraction b − a was written in the wrong order.",
      "C: x = ab(b − a) — the bracket was multiplied instead of divided.",
      "D: x = (b − a)/(ab) — the whole fraction was inverted."
    ]
  },
  {
    "sig": "which-provider-is-cheaper-and-from-where",
    "code": "SAAT-S.30",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 2,
    "stem": "Courier X charges SAR 14 plus SAR 3 per kilometre. Courier Y charges SAR 26 plus SAR 2 per kilometre. Which statement is true?",
    "opts": [
      "Both couriers charge the same for every trip.",
      "X is cheaper for trips under 12 km; Y is cheaper for longer trips.",
      "Y is cheaper for trips under 12 km; X is cheaper for longer trips.",
      "X is cheaper for trips under 40 km; Y is cheaper for longer trips."
    ],
    "ans": 1,
    "trick": "the crossing point splits the range: the plan with the lower fixed fee wins short, the plan with the lower rate wins long",
    "why": "14 + 3k = 26 + 2k gives k = 12. Below 12 km X is cheaper; above it Y is cheaper.",
    "traps": [
      "A: Both couriers charge the same for every trip. — the single crossing point was mistaken for equality everywhere.",
      "C: Y is cheaper for trips under 12 km; X is cheaper for longer trips. — the two couriers were swapped: Y has the higher fixed fee, so X wins short trips.",
      "D: X is cheaper for trips under 40 km; Y is cheaper for longer trips. — 14 + 26 = 40 was used as the crossing point."
    ]
  },
  {
    "sig": "years-until-two-simple-interest-balances-match",
    "code": "SAAT-S.31",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 2,
    "stem": "Account A holds SAR 2,600 and earns simple interest at 4% per year. Account B holds SAR 1,800 and earns simple interest at 8% per year. After how many years will the two balances be equal?",
    "opts": [
      "25",
      "8",
      "20",
      "40"
    ],
    "ans": 2,
    "trick": "simple interest adds the SAME amount each year: yearly gain = principal × rate — set the two balances equal",
    "why": "A gains 104 a year and B gains 144 a year. 2600 + 104t = 1800 + 144t gives 40t = 800, so t = 20.",
    "traps": [
      "A: 25 — the gap 800 was divided by 32 instead of 40.",
      "B: 8 — the gap 800 was divided by 100 as if the rates were not applied.",
      "D: 40 — the yearly difference in gains (SAR 40) was reported instead of the number of years."
    ]
  },
  {
    "sig": "average-speed-for-a-round-trip",
    "code": "SAAT-S.32",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 2,
    "stem": "Salma drives from Jeddah to Makkah at an average speed of 60 km/h and returns along the same road at 90 km/h. What is her average speed for the whole trip, in km/h?",
    "opts": [
      "75",
      "150",
      "70",
      "72"
    ],
    "ans": 3,
    "trick": "average speed = total distance ÷ total time — never the average of the two speeds",
    "why": "For a distance d each way, time = d/60 + d/90 = d/36, so the average speed is 2d ÷ (d/36) = 72 km/h.",
    "traps": [
      "A: 75 — the two speeds were averaged, but she spends more TIME at the slower speed.",
      "B: 150 — the speeds were added.",
      "C: 70 — a weighted guess toward the slower speed."
    ]
  },
  {
    "sig": "pure-water-added-to-a-solution",
    "code": "SAAT-S.33",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 2,
    "stem": "How many litres of pure water must be added to 15 litres of a 40% salt solution to make a 25% solution?",
    "opts": [
      "9",
      "6",
      "15",
      "24"
    ],
    "ans": 0,
    "trick": "pure water adds volume but no salt: the amount of salt stays the same, so use salt = percentage × volume on both sides",
    "why": "Salt = 0.40 × 15 = 6 L. Final volume = 6 ÷ 0.25 = 24 L. Water added = 24 − 15 = 9 L.",
    "traps": [
      "B: 6 — the amount of salt was reported, not the water to add.",
      "C: 15 — the same volume was added without checking the concentration.",
      "D: 24 — the new TOTAL volume was reported instead of the water added."
    ]
  },
  {
    "sig": "how-much-of-the-stronger-solution",
    "code": "SAAT-S.34",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 3,
    "stem": "A lab mixes a 20% acid solution with a 50% acid solution to make 60 litres of a 38% acid solution. How many litres of the 50% solution are used?",
    "opts": [
      "18",
      "36",
      "24",
      "30"
    ],
    "ans": 1,
    "trick": "write acid from each part: 0.20(60 − t) + 0.50t = 0.38 × 60 and read which unknown the question wants",
    "why": "12 + 0.3t = 22.8 gives t = 36 litres of the 50% solution.",
    "traps": [
      "A: 18 — the distance from 38 to 20 was used as litres.",
      "C: 24 — the amount of the 20% solution was reported.",
      "D: 30 — an equal split of the 60 litres was assumed."
    ]
  },
  {
    "sig": "filling-with-a-drain-open",
    "code": "SAAT-S.35",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 2,
    "stem": "A tap can fill a tank in 6 hours. A drain can empty a full tank in 15 hours. With both open, how many hours does it take to fill the empty tank?",
    "opts": [
      "21",
      "30/7",
      "10",
      "9"
    ],
    "ans": 2,
    "trick": "work in rates per hour — a drain is a NEGATIVE rate: 1/6 − 1/15",
    "why": "Net rate = 1/6 − 1/15 = 3/30 = 1/10 of the tank per hour, so it takes 10 hours.",
    "traps": [
      "A: 21 — the times were added.",
      "B: 30/7 — the drain was added to the rate instead of subtracted.",
      "D: 9 — the times were subtracted: 15 − 6."
    ]
  },
  {
    "sig": "one-worker-finishes-the-remaining-job",
    "code": "SAAT-S.36",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 3,
    "stem": "Worker A can finish a job in 10 hours and worker B in 15 hours. They work together for 3 hours, then B leaves. How many more hours does A need to finish the job alone?",
    "opts": [
      "6",
      "3",
      "5/2",
      "5"
    ],
    "ans": 3,
    "trick": "count the fraction of the job done, subtract from 1, and divide by the rate of whoever is left",
    "why": "Together they do 1/10 + 1/15 = 1/6 per hour, so in 3 hours they finish 1/2. The remaining 1/2 at A's rate of 1/10 takes 5 hours.",
    "traps": [
      "A: 6 — the time for both together to do the WHOLE job (1 ÷ 1/6) was reported.",
      "B: 3 — the remaining half was divided by the combined rate 1/6 instead of A's rate.",
      "C: 5/2 — A's rate was taken as 1/5 instead of 1/10."
    ]
  },
  {
    "sig": "speed-of-a-boat-in-still-water",
    "code": "SAAT-S.37",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 2,
    "stem": "A boat travels 30 km upstream in 5 hours and returns the same 30 km downstream in 2 hours. The boat's speed in still water and the current are both constant. What is the boat's speed in still water, in km/h?",
    "opts": [
      "21/2",
      "9/2",
      "9",
      "21"
    ],
    "ans": 0,
    "trick": "upstream = boat − current and downstream = boat + current — the boat speed is their AVERAGE, the current is half their difference",
    "why": "Upstream speed 30/5 = 6 and downstream speed 30/2 = 15. Boat = (6 + 15)/2 = 10.5 km/h and the current is 4.5 km/h.",
    "traps": [
      "B: 9/2 — the speed of the current was reported.",
      "C: 9 — the difference of the two speeds was reported.",
      "D: 21 — the two speeds 6 and 15 were added."
    ]
  },
  {
    "sig": "time-for-a-second-vehicle-to-catch-up",
    "code": "SAAT-S.38",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 2,
    "stem": "A bus leaves a station at 50 km/h. Two hours later a car leaves the same station along the same road at 75 km/h. How many hours after the car leaves does it catch up with the bus?",
    "opts": [
      "25",
      "4",
      "6",
      "2"
    ],
    "ans": 1,
    "trick": "the head start is a DISTANCE (50 × 2); it closes at the DIFFERENCE of the speeds — and read which clock the question uses",
    "why": "Head start = 100 km. Closing speed = 75 − 50 = 25 km/h. Time = 100 ÷ 25 = 4 hours after the car leaves.",
    "traps": [
      "A: 25 — the closing speed itself was reported.",
      "C: 6 — the hours since the BUS left were reported, not since the car left.",
      "D: 2 — the head start in hours was reported."
    ]
  },
  {
    "sig": "age-problem-with-two-conditions",
    "code": "SAAT-S.39",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 2,
    "stem": "A father is 5 times as old as his son. In 8 years he will be 3 times as old as his son. How old is the father now?",
    "opts": [
      "48",
      "24",
      "40",
      "8"
    ],
    "ans": 2,
    "trick": "define the son as s, write both ages now, add the SAME number of years to both, and answer the person asked about",
    "why": "5s + 8 = 3(s + 8) gives 2s = 16, so s = 8. The father is 5 × 8 = 40 now.",
    "traps": [
      "A: 48 — the father's age in 8 years was reported.",
      "B: 24 — three times the son's present age was reported.",
      "D: 8 — the son's age was reported."
    ]
  },
  {
    "sig": "money-split-between-two-rates",
    "code": "SAAT-S.40",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 3,
    "stem": "SAR 9,000 is split between an account paying 6% a year and an account paying 9% a year. After one year the 9% account has earned SAR 180 more than the 6% account. How much was placed in the 6% account?",
    "opts": [
      "4800",
      "6600",
      "1200",
      "4200"
    ],
    "ans": 3,
    "trick": "let x be the 6% amount, so the other is 8000 − x, and compare INTERESTS, not amounts",
    "why": "0.09(9000 − x) − 0.06x = 180 gives 810 − 0.15x = 180, so x = 4,200.",
    "traps": [
      "A: 4800 — the amount in the 9% account was reported instead of the 6% account.",
      "B: 6600 — the gap of SAR 180 was subtracted instead of added when the equation was set up.",
      "C: 1200 — only 180 ÷ 0.15 was computed and the 9,000 term was left out."
    ]
  },
  {
    "sig": "change-in-area-when-the-dimensions-change",
    "code": "SAAT-S.41",
    "unit": 2,
    "topic": "Polynomials & factoring",
    "lvl": 2,
    "stem": "A square has side x metres. Its length is increased by 7 m and its width is decreased by 2 m. By how many square metres does the area change?",
    "opts": [
      "5x − 14",
      "5x + 14",
      "x² + 5x − 14",
      "−14"
    ],
    "ans": 0,
    "trick": "change = new area − old area — expand the new area, then subtract x²",
    "why": "(x + 7)(x − 2) = x² + 5x − 14. Subtracting the original x² leaves 5x − 14.",
    "traps": [
      "B: 5x + 14 — the product of the constants was given the wrong sign.",
      "C: x² + 5x − 14 — the new area was reported without subtracting the old one.",
      "D: −14 — the x-terms were dropped and only the product of the constants was kept."
    ]
  },
  {
    "sig": "inner-area-after-a-border-on-all-sides",
    "code": "SAAT-S.42",
    "unit": 1,
    "topic": "Polynomials & factoring",
    "lvl": 2,
    "stem": "A poster is (2x + 9) cm long and (x + 6) cm wide. A border 2 cm wide is printed along all four edges. Which expression gives the area of the inner region, in square centimetres?",
    "opts": [
      "2x² + 17x + 30",
      "2x² + 9x + 10",
      "2x² + 15x + 28",
      "2x² + 21x + 54"
    ],
    "ans": 1,
    "trick": "a border on all four edges removes TWICE its width from each dimension",
    "why": "The inner length is 2x + 9 − 4 = 2x + 5 and the inner width is x + 6 − 4 = x + 2. The area is (2x + 5)(x + 2) = 2x² + 9x + 10.",
    "traps": [
      "A: 2x² + 17x + 30 — the border was removed from the length only.",
      "C: 2x² + 15x + 28 — only ONE border width was removed from each dimension, giving (2x + 7)(x + 4).",
      "D: 2x² + 21x + 54 — the border was ignored and the full poster area was given."
    ]
  },
  {
    "sig": "perimeter-of-a-base-from-a-volume-and-a-height",
    "code": "SAAT-S.43",
    "unit": 1,
    "topic": "Polynomials & factoring",
    "lvl": 3,
    "stem": "A box has volume (x³ + 10x² + 31x + 30) cubic units and height (x + 3) units. Its base is a rectangle whose sides are linear expressions in x. What is the perimeter of the base, in units?",
    "opts": [
      "x² + 7x + 10",
      "4x + 10",
      "4x + 14",
      "2x + 7"
    ],
    "ans": 2,
    "trick": "volume ÷ height gives the base area — factor that area into two sides before finding the perimeter",
    "why": "(x³ + 10x² + 31x + 30) ÷ (x + 3) = x² + 7x + 10 = (x + 2)(x + 5). The perimeter is 2(x + 2) + 2(x + 5) = 4x + 14.",
    "traps": [
      "A: x² + 7x + 10 — the base AREA was reported instead of the perimeter.",
      "B: 4x + 10 — the constants were added as 2 + 3 instead of 2 + 5.",
      "D: 2x + 7 — the sum of the two sides was reported instead of the perimeter."
    ]
  },
  {
    "sig": "volume-of-an-open-box-from-a-rectangular-sheet",
    "code": "SAAT-S.44",
    "unit": 1,
    "topic": "Polynomials & factoring",
    "lvl": 3,
    "stem": "An open box is made from a rectangular sheet 30 cm by 18 cm by cutting a square of side x cm from each corner and folding up the sides. Which polynomial gives the volume of the box, in cubic centimetres?",
    "opts": [
      "x³ − 48x² + 540x",
      "4x³ − 48x² + 540x",
      "2x³ − 96x² + 540x",
      "4x³ − 96x² + 540x"
    ],
    "ans": 3,
    "trick": "cutting a square from BOTH corners of a side removes 2x from that dimension",
    "why": "The base is (30 − 2x) by (18 − 2x) and the height is x, so V = x(30 − 2x)(18 − 2x) = 4x³ − 96x² + 540x.",
    "traps": [
      "A: x³ − 48x² + 540x — only ONE x was removed from each dimension.",
      "B: 4x³ − 48x² + 540x — the middle coefficient was halved when the bracket was expanded.",
      "C: 2x³ − 96x² + 540x — the leading coefficient 2·2 = 4 was written as 2."
    ]
  },
  {
    "sig": "touch-or-cross-from-the-multiplicities",
    "code": "SAAT-S.45",
    "unit": 1,
    "topic": "Polynomials & factoring",
    "lvl": 2,
    "stem": "The graph of P(x) = (x − 1)²(x + 3)³(x − 4) meets the x-axis at three points. Which statement is true?",
    "opts": [
      "Touches at x = 1; crosses at x = −3 and x = 4.",
      "Touches at x = −3; crosses at x = 1 and x = 4.",
      "Touches at x = 1 and x = 4; crosses at x = −3.",
      "Crosses at all three points."
    ],
    "ans": 0,
    "trick": "even multiplicity → the graph touches and turns back; odd multiplicity → it crosses",
    "why": "(x − 1) has power 2 (touches), (x + 3) has power 3 (crosses, flattening), (x − 4) has power 1 (crosses).",
    "traps": [
      "B: Touches at x = −3; crosses at x = 1 and x = 4. — the parity was reversed: an ODD power crosses and an EVEN power touches.",
      "C: Touches at x = 1 and x = 4; crosses at x = −3. — x = 4 was taken as a touching point although its power is 1.",
      "D: Crosses at all three points. — every zero was assumed to cross regardless of its multiplicity."
    ]
  },
  {
    "sig": "divisible-by-a-product-of-two-binomials",
    "code": "SAAT-S.46",
    "unit": 1,
    "topic": "Polynomials & factoring",
    "lvl": 3,
    "stem": "The polynomial P(x) = x³ + px + q is divisible by (x − 2)(x + 1). What is the value of pq?",
    "opts": [
      "3",
      "6",
      "−6",
      "−2"
    ],
    "ans": 1,
    "trick": "divisible by (x − 2)(x + 1) means P(2) = 0 AND P(−1) = 0 — two equations for p and q",
    "why": "P(2) = 8 + 2p + q = 0 and P(−1) = −1 − p + q = 0. Subtracting gives 9 + 3p = 0, so p = −3, then q = −2 and pq = 6.",
    "traps": [
      "A: 3 — only p was reported with its sign dropped.",
      "C: −6 — the sign of p was lost when P(−1) = −1 − p + q was set up.",
      "D: −2 — only q was reported."
    ]
  },
  {
    "sig": "sum-of-all-zeros-of-a-cubic-without-finding-them",
    "code": "SAAT-S.47",
    "unit": 1,
    "topic": "Polynomials & factoring",
    "lvl": 2,
    "stem": "What is the sum of the three zeros of P(x) = 4x³ + 10x² − 7x + 3?",
    "opts": [
      "−7/4",
      "3/4",
      "−5/2",
      "5/2"
    ],
    "ans": 2,
    "trick": "for ax³ + bx² + cx + d the zeros add up to −b/a — you do not need to factor",
    "why": "The sum of the zeros is −10/4 = −5/2.",
    "traps": [
      "A: −7/4 — the coefficient of x was divided by the leading coefficient.",
      "B: 3/4 — the constant term was divided by the leading coefficient.",
      "D: 5/2 — the sign was lost: the sum of the zeros is −b/a, not b/a."
    ]
  },
  {
    "sig": "value-that-makes-a-trinomial-a-perfect-square",
    "code": "SAAT-S.48",
    "unit": 1,
    "topic": "Polynomials & factoring",
    "lvl": 2,
    "stem": "The trinomial 9x² + kx + 25 is a perfect square and k is positive. What is the value of k?",
    "opts": [
      "15",
      "45",
      "225",
      "30"
    ],
    "ans": 3,
    "trick": "a perfect square (ax + b)² has middle term 2ab — remember the factor of 2 and the square roots of BOTH ends",
    "why": "9x² + 25 + kx = (3x + 5)², whose middle term is 2 · 3 · 5 = 30, so k = 30.",
    "traps": [
      "A: 15 — the middle term was taken as 3 · 5.",
      "B: 45 — the coefficient 9 was multiplied by the constant 5.",
      "C: 225 — the first and last coefficients were multiplied."
    ]
  },
  {
    "sig": "count-the-constants-that-let-a-trinomial-factor",
    "code": "SAAT-S.49",
    "unit": 1,
    "topic": "Polynomials & factoring",
    "lvl": 3,
    "stem": "For how many different positive integer values of k can x² − 12x + k be written as (x − p)(x − q), where p and q are positive integers?",
    "opts": [
      "6",
      "5",
      "11",
      "12"
    ],
    "ans": 0,
    "trick": "p + q = 12 with p, q positive gives the pairs; different k means different products — pairs like (3, 9) and (9, 3) give the same k",
    "why": "The pairs {1, 11}, {2, 10}, {3, 9}, {4, 8}, {5, 7}, {6, 6} give k = 11, 20, 27, 32, 35, 36 — six different values.",
    "traps": [
      "B: 5 — the case p = q = 6 was not counted.",
      "C: 11 — the ordered pairs (p, q) were counted, so each product was counted twice or more.",
      "D: 12 — the sum p + q was reported."
    ]
  },
  {
    "sig": "count-the-n-for-which-x-squared-minus-n-factors",
    "code": "SAAT-S.50",
    "unit": 1,
    "topic": "Polynomials & factoring",
    "lvl": 3,
    "stem": "For how many integers n from 1 to 100, inclusive, can x² − n be written as the product of two binomials with integer coefficients?",
    "opts": [
      "100",
      "10",
      "9",
      "11"
    ],
    "ans": 1,
    "trick": "x² − n factors over the integers only when n is a perfect square, so count squares in the range",
    "why": "n must be 1, 4, 9, 16, 25, 36, 49, 64, 81 or 100 — ten values.",
    "traps": [
      "A: 100 — every n was assumed to factor.",
      "C: 9 — the case n = 100 was left out.",
      "D: 11 — the square 0 was counted although n starts at 1."
    ]
  },
  {
    "sig": "greatest-linear-coefficient-for-a-factorable-trinomial",
    "code": "SAAT-S.51",
    "unit": 1,
    "topic": "Polynomials & factoring",
    "lvl": 3,
    "stem": "The trinomial x² + kx − 24 can be factored into two binomials with integer coefficients. What is the greatest possible value of k?",
    "opts": [
      "10",
      "2",
      "23",
      "5"
    ],
    "ans": 2,
    "trick": "k is the SUM of the two numbers whose product is −24 — to make it largest, make the numbers as far apart as possible",
    "why": "The pairs (−1, 24), (−2, 12), (−3, 8), (−4, 6), ... have sums 23, 10, 5, 2, ... The greatest is 23.",
    "traps": [
      "A: 10 — only the pair (−2, 12) was tried.",
      "B: 2 — only the pair (−4, 6) was tried.",
      "D: 5 — only the pair (−3, 8) was tried."
    ]
  },
  {
    "sig": "sum-of-squares-of-the-real-solutions-of-a-quartic",
    "code": "SAAT-S.52",
    "unit": 1,
    "topic": "Polynomials & factoring",
    "lvl": 3,
    "stem": "What is the sum of the squares of all the real solutions of x⁴ − 10x² + 9 = 0?",
    "opts": [
      "10",
      "18",
      "9",
      "20"
    ],
    "ans": 3,
    "trick": "substitute u = x²: each u > 0 gives TWO real solutions ±√u, and both get squared",
    "why": "u² − 10u + 9 = 0 gives u = 1 or 9, so x = ±1 or ±3. The squares add to 1 + 1 + 9 + 9 = 20.",
    "traps": [
      "A: 10 — the two values u = 1 and u = 9 were added without doubling for ±.",
      "B: 18 — only u = 9 was used and counted twice (x = ±3).",
      "C: 9 — only the larger value of x² was reported."
    ]
  },
  {
    "sig": "difference-of-cubes-from-a-difference-and-a-product",
    "code": "SAAT-S.53",
    "unit": 1,
    "topic": "Polynomials & factoring",
    "lvl": 3,
    "stem": "If a − b = 2 and ab = 15, what is the value of a³ − b³?",
    "opts": [
      "98",
      "38",
      "34",
      "53"
    ],
    "ans": 0,
    "trick": "a³ − b³ = (a − b)(a² + ab + b²), and a² + b² comes from squaring a − b: (a − b)² + 2ab",
    "why": "a² + b² = 2² + 2·15 = 34, so a² + ab + b² = 49 and a³ − b³ = 2 · 49 = 98.",
    "traps": [
      "B: 38 — the factor a² − ab + b² was used instead of a² + ab + b².",
      "C: 34 — only a² + b² was reported.",
      "D: 53 — (a − b)³ + 3ab was computed instead of (a − b)³ + 3ab(a − b)."
    ]
  },
  {
    "sig": "sum-of-cubes-from-a-sum-and-a-sum-of-squares",
    "code": "SAAT-S.54",
    "unit": 1,
    "topic": "Polynomials & factoring",
    "lvl": 2,
    "stem": "If x + y = 9 and x² + y² = 45, what is the value of x³ + y³?",
    "opts": [
      "81",
      "243",
      "405",
      "729"
    ],
    "ans": 1,
    "trick": "x³ + y³ = (x + y)(x² − xy + y²), and xy comes from (x + y)² = x² + 2xy + y²",
    "why": "81 = 45 + 2xy gives xy = 18. Then x³ + y³ = 9 × (45 − 18) = 243.",
    "traps": [
      "A: 81 — only (x + y)² was reported.",
      "C: 405 — x³ + y³ was computed as 9 × 45.",
      "D: 729 — only (x + y)³ was reported."
    ]
  },
  {
    "sig": "degree-after-the-leading-terms-cancel",
    "code": "SAAT-S.55",
    "unit": 1,
    "topic": "Polynomials & factoring",
    "lvl": 2,
    "stem": "What is the degree of the polynomial (2x² − x)² − 4x⁴?",
    "opts": [
      "2",
      "1",
      "3",
      "4"
    ],
    "ans": 2,
    "trick": "expand fully: the highest power may cancel, so the degree is the highest power that survives",
    "why": "(2x² − x)² = 4x⁴ − 4x³ + x². Subtracting 4x⁴ leaves −4x³ + x², whose degree is 3.",
    "traps": [
      "A: 2 — the expansion stopped at the x² term.",
      "B: 1 — only the last term −x was considered.",
      "D: 4 — the leading terms were assumed not to cancel."
    ]
  },
  {
    "sig": "coefficient-of-a-single-power-in-a-product-of-three-binomials",
    "code": "SAAT-S.56",
    "unit": 1,
    "topic": "Polynomials & factoring",
    "lvl": 2,
    "stem": "What is the coefficient of x in the expansion of (x + 3)(x − 2)(x − 5)?",
    "opts": [
      "−4",
      "11",
      "30",
      "−11"
    ],
    "ans": 3,
    "trick": "the x-coefficient is the SUM OF PAIR PRODUCTS of the three constants: 3(−2) + 3(−5) + (−2)(−5)",
    "why": "−6 − 15 + 10 = −11.",
    "traps": [
      "A: −4 — the coefficient of x² was reported.",
      "B: 11 — the sign of the sum of pair products was lost.",
      "C: 30 — the constant term was reported."
    ]
  },
  {
    "sig": "difference-of-two-squared-binomials",
    "code": "SAAT-S.57",
    "unit": 1,
    "topic": "Polynomials & factoring",
    "lvl": 2,
    "stem": "Which expression is equal to (5x + 3)² − (5x − 3)²?",
    "opts": [
      "60x",
      "50x²",
      "18",
      "30x"
    ],
    "ans": 0,
    "trick": "the squares cancel, and each bracket contributes a cross term of ±30x — so they ADD to 60x",
    "why": "(25x² + 30x + 9) − (25x² − 30x + 9) = 60x.",
    "traps": [
      "B: 50x² — the squares were added instead of subtracted, ignoring the cross terms.",
      "C: 18 — the two constants 9 and 9 were added.",
      "D: 30x — the cross term was counted once instead of twice for each bracket."
    ]
  },
  {
    "sig": "power-of-i-with-a-large-exponent",
    "code": "SAAT-S.58",
    "unit": 7,
    "topic": "Complex numbers",
    "lvl": 2,
    "stem": "What is the value of i⁵⁸?",
    "opts": [
      "−i",
      "−1",
      "1",
      "i"
    ],
    "ans": 1,
    "trick": "powers of i repeat every 4 — divide the exponent by 4 and use the remainder",
    "why": "58 = 4 × 14 + 2, so i⁵⁸ = i² = −1.",
    "traps": [
      "A: −i — the remainder was taken as 3.",
      "C: 1 — the remainder was taken as 0 after dividing 58 by 4, instead of 2.",
      "D: i — the remainder was taken as 1."
    ]
  },
  {
    "sig": "power-of-a-complex-binomial",
    "code": "SAAT-S.59",
    "unit": 7,
    "topic": "Complex numbers",
    "lvl": 3,
    "stem": "What is the value of (1 + i)⁶?",
    "opts": [
      "8",
      "−8",
      "−8i",
      "8i"
    ],
    "ans": 2,
    "trick": "square first: (1 + i)² = 2i, then cube it: (2i)³ = 8i³ and i³ = −i",
    "why": "(1 + i)² = 2i, so (1 + i)⁶ = (2i)³ = 8i³ = −8i.",
    "traps": [
      "A: 8 — the factor i³ was dropped.",
      "B: −8 — i³ was taken as −1.",
      "D: 8i — i³ was taken as i instead of −i."
    ]
  },
  {
    "sig": "equate-real-and-imaginary-parts",
    "code": "SAAT-S.60",
    "unit": 7,
    "topic": "Complex numbers",
    "lvl": 2,
    "stem": "If (3x − 2) + (y + 4)i = 10 − 2i, where x and y are real numbers, what is the value of x + y?",
    "opts": [
      "6",
      "2",
      "10",
      "−2"
    ],
    "ans": 3,
    "trick": "two complex numbers are equal when their REAL parts match and their IMAGINARY parts match",
    "why": "3x − 2 = 10 gives x = 4. y + 4 = −2 gives y = −6. So x + y = −2.",
    "traps": [
      "A: 6 — y + 4 = −2 was solved as y = 2 (the 4 was added instead of subtracted).",
      "B: 2 — y + 4 = −2 was solved as y = −2 (the 4 was ignored).",
      "C: 10 — the real part of the right-hand side was reported."
    ]
  },
  {
    "sig": "condition-for-two-distinct-nonreal-roots",
    "code": "SAAT-S.61",
    "unit": 7,
    "topic": "Complex numbers",
    "lvl": 2,
    "stem": "For which values of k does x² − 6x + k = 0 have two distinct nonreal complex solutions?",
    "opts": [
      "k > 9",
      "k < 9",
      "k = 9",
      "k > 36"
    ],
    "ans": 0,
    "trick": "nonreal roots need a NEGATIVE discriminant: b² − 4ac < 0",
    "why": "36 − 4k < 0 gives k > 9.",
    "traps": [
      "B: k < 9 — the discriminant inequality was written the wrong way round.",
      "C: k = 9 — the discriminant was set to zero, which gives one repeated real root.",
      "D: k > 36 — 36 − 4k < 0 was solved as k > 36."
    ]
  },
  {
    "sig": "complex-quotient-with-a-binomial-denominator",
    "code": "SAAT-S.62",
    "unit": 7,
    "topic": "Complex numbers",
    "lvl": 3,
    "stem": "Which of the following is equal to (5 − i)/(2 + i)?",
    "opts": [
      "9 − 7i",
      "9/5 − (7/5)i",
      "9/5 + (7/5)i",
      "11/5 − (7/5)i"
    ],
    "ans": 1,
    "trick": "multiply top and bottom by the conjugate of the denominator, then replace i² with −1",
    "why": "(5 − i)(2 − i) = 10 − 5i − 2i + i² = 9 − 7i and (2 + i)(2 − i) = 5, so the quotient is 9/5 − (7/5)i.",
    "traps": [
      "A: 9 − 7i — the denominator 5 was not divided out.",
      "C: 9/5 + (7/5)i — the sign of the imaginary part was lost.",
      "D: 11/5 − (7/5)i — i² was replaced by +1 instead of −1 in the numerator."
    ]
  },
  {
    "sig": "solutions-of-a-quadratic-with-a-negative-discriminant",
    "code": "SAAT-S.63",
    "unit": 7,
    "topic": "Complex numbers",
    "lvl": 2,
    "stem": "What are the solutions of x² + 2x + 10 = 0?",
    "opts": [
      "−1 ± 9i",
      "−2 ± 6i",
      "−1 ± 3i",
      "1 ± 3i"
    ],
    "ans": 2,
    "trick": "use x = (−b ± √D)/2a — with D = −36 the square root is 6i, and the whole numerator is divided by 2",
    "why": "D = 4 − 40 = −36, so x = (−2 ± 6i)/2 = −1 ± 3i.",
    "traps": [
      "A: −1 ± 9i — √−36 was written as 18i instead of 6i.",
      "B: −2 ± 6i — the division by 2a = 2 was forgotten.",
      "D: 1 ± 3i — the sign of −b/2a was lost."
    ]
  },
  {
    "sig": "first-error-distributing-a-factor",
    "code": "SAAT-S.64",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 2,
    "stem": "A student solves 2(x − 3) + 4 = x + 5 as follows. Step 1: 2x − 3 + 4 = x + 5. Step 2: 2x + 1 = x + 5. Step 3: x = 4. In which step does the first error occur?",
    "opts": [
      "There is no error.",
      "Step 1",
      "Step 2",
      "Step 3"
    ],
    "ans": 1,
    "trick": "check each line against the one before it — the first line that is not equivalent is the error",
    "why": "Step 1 multiplied only the x by 2: 2(x − 3) = 2x − 6, not 2x − 3. The correct solution is x = 7.",
    "traps": [
      "A: There is no error. — the answer x = 4 does not satisfy the original equation: 2(1) + 4 = 6 but x + 5 = 9.",
      "C: Step 2 — 2x − 3 + 4 does equal 2x + 1; the arithmetic here is right.",
      "D: Step 3 — from 2x + 1 = x + 5, x = 4 is the correct next line, so the slip is earlier."
    ]
  },
  {
    "sig": "first-error-reversing-an-inequality-sign",
    "code": "SAAT-S.65",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 2,
    "stem": "A student solves 5 − 2x < 11 as follows. Step 1: −2x < 6. Step 2: x < −3. Step 3: The solution set is (−∞, −3). In which step does the first error occur?",
    "opts": [
      "There is no error.",
      "Step 1",
      "Step 2",
      "Step 3"
    ],
    "ans": 2,
    "trick": "dividing or multiplying an inequality by a NEGATIVE number reverses the sign",
    "why": "Step 2 divides by −2 without reversing: the correct line is x > −3, so the solution set is (−3, ∞).",
    "traps": [
      "A: There is no error. — dividing −2x < 6 by −2 requires the sign to flip, so x < −3 is wrong.",
      "B: Step 1 — 5 − 2x < 11 does give −2x < 6.",
      "D: Step 3 — the set (−∞, −3) is the correct translation of x < −3; the slip came earlier."
    ]
  },
  {
    "sig": "first-error-keeping-only-one-absolute-value-case",
    "code": "SAAT-S.66",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 2,
    "stem": "A student solves |3x − 1| = 8 as follows. Step 1: 3x − 1 = 8. Step 2: 3x = 9. Step 3: x = 3, so the only solution is x = 3. In which step does the first error occur?",
    "opts": [
      "There is no error.",
      "Step 1",
      "Step 2",
      "Step 3"
    ],
    "ans": 1,
    "trick": "an absolute value equation |A| = c (c > 0) always splits into A = c AND A = −c",
    "why": "Step 1 uses only one case. The second case 3x − 1 = −8 gives x = −7/3, so the solutions are 3 and −7/3.",
    "traps": [
      "A: There is no error. — the equation also has the solution x = −7/3, so the work is incomplete.",
      "C: Step 2 — 3x − 1 = 8 does give 3x = 9; the arithmetic is right.",
      "D: Step 3 — x = 3 follows correctly from 3x = 9; the claim 'only solution' comes from Step 1."
    ]
  },
  {
    "sig": "first-error-in-elimination-back-substitution",
    "code": "SAAT-S.67",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 2,
    "stem": "A student solves x + 2y = 7 and 3x − 2y = 5 as follows. Step 1: Add the equations: 4x = 12. Step 2: x = 3. Step 3: Substitute: 3 + 2y = 7, so y = 5. In which step does the first error occur?",
    "opts": [
      "There is no error.",
      "Step 1",
      "Step 2",
      "Step 3"
    ],
    "ans": 3,
    "trick": "after finding one variable, finish the substitution carefully — and check the pair in the other equation",
    "why": "Steps 1 and 2 are correct. In Step 3, 3 + 2y = 7 gives 2y = 4, so y = 2. Check: 3(3) − 2(2) = 5.",
    "traps": [
      "A: There is no error. — 3 + 2y = 7 gives 2y = 4, so y = 2, not 5.",
      "B: Step 1 — adding the equations eliminates y correctly: 4x = 12.",
      "C: Step 2 — 4x = 12 gives x = 3 correctly."
    ]
  },
  {
    "sig": "first-error-clearing-fractions",
    "code": "SAAT-S.68",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 2,
    "stem": "A student solves (x + 1)/3 = 2 − x/2 as follows. Step 1: Multiply by 6: 2x + 1 = 12 − 3x. Step 2: 5x = 11. Step 3: x = 11/5. In which step does the first error occur?",
    "opts": [
      "There is no error.",
      "Step 1",
      "Step 2",
      "Step 3"
    ],
    "ans": 1,
    "trick": "when you multiply by the common denominator, EVERY term on both sides is multiplied — including the whole bracket",
    "why": "Step 1 should read 2(x + 1) = 12 − 3x, i.e. 2x + 2 = 12 − 3x. Then 5x = 10 and x = 2.",
    "traps": [
      "A: There is no error. — the answer 11/5 does not satisfy the original equation.",
      "C: Step 2 — 2x + 1 = 12 − 3x does give 5x = 11; the arithmetic is right.",
      "D: Step 3 — 5x = 11 gives x = 11/5 correctly."
    ]
  },
  {
    "sig": "synthetic-division-by-a-sum-uses-the-opposite-sign",
    "code": "SAAT-S.69",
    "unit": 1,
    "topic": "Polynomials & factoring",
    "lvl": 3,
    "stem": "A student divides 2x³ − x² + 5 by (x + 2) using synthetic division. The student writes c = 2 and uses the coefficients 2, −1, 0, 5. What is the mistake?",
    "opts": [
      "The sign of c is wrong: it should be −2.",
      "There is no mistake.",
      "The coefficient 0 should not be written.",
      "The remainder must be subtracted from the quotient."
    ],
    "ans": 0,
    "trick": "synthetic division by (x − c) uses c — so for (x + 2) you use c = −2",
    "why": "x + 2 = x − (−2), so c = −2. The coefficients 2, −1, 0, 5 (with the zero for the missing x-term) are correct.",
    "traps": [
      "B: There is no mistake. — the divisor x + 2 means c = −2, so c = 2 is wrong.",
      "C: The coefficient 0 should not be written. — the zero is needed: the missing x term must be written as 0, so the coefficients are right.",
      "D: The remainder must be subtracted from the quotient. — the remainder is never subtracted from the quotient; it is reported separately."
    ]
  },
  {
    "sig": "synthetic-division-with-a-missing-term",
    "code": "SAAT-S.70",
    "unit": 1,
    "topic": "Polynomials & factoring",
    "lvl": 3,
    "stem": "A student divides x³ − 13x + 12 by (x − 3) using synthetic division and writes c = 3 with the coefficients 1, −13, 12. What is the mistake?",
    "opts": [
      "The last coefficient should be −12.",
      "The coefficient 0 of the missing x² term was left out.",
      "The value of c should be −3.",
      "There is no mistake."
    ],
    "ans": 1,
    "trick": "write EVERY power from the highest down to the constant — a missing power still needs a 0",
    "why": "x³ − 13x + 12 = 1x³ + 0x² − 13x + 12, so the coefficients are 1, 0, −13, 12.",
    "traps": [
      "A: The last coefficient should be −12. — the constant 12 is the given constant term and must be written as it is.",
      "C: The value of c should be −3. — c = 3 is correct because the divisor is x − 3.",
      "D: There is no mistake. — the missing x² term must be written as 0, so there is a mistake."
    ]
  }
];
