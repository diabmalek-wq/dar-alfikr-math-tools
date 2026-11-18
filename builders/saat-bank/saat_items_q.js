// SAAT BANK — part Q: skills read (skill and trap only) from nine leak and trial PDFs (Nov 2026).
// Stems, numbers and options are original; every key is re-derived by a predicate in spec_q.py.
module.exports = [
  {
    "sig": "largest-angle-is-opposite-the-longest-side",
    "code": "SAAT-Q.1",
    "unit": 4,
    "topic": "Triangles, polygons & quadrilaterals",
    "lvl": 2,
    "stem": "In triangle ABC, AB = 9 cm, BC = 14 cm and CA = 11 cm. Which angle is the largest?",
    "opts": [
      "∠A",
      "∠B",
      "∠C",
      "They are all equal"
    ],
    "ans": 0,
    "trick": "the largest angle faces the longest side — it is NOT the angle where the longest side ends",
    "why": "BC = 14 cm is the longest side and it lies opposite vertex A, so ∠A is the largest.",
    "traps": [
      "B: ∠B — the angle was matched to the side that ends at it (CA) instead of the side opposite it.",
      "C: ∠C — the angle at the end of the shortest side was chosen.",
      "D: They are all equal — equal angles need equal sides, and these three sides all differ."
    ]
  },
  {
    "sig": "equilateral-triangle-solve-then-find-the-perimeter",
    "code": "SAAT-Q.2",
    "unit": 4,
    "topic": "Triangles, polygons & quadrilaterals",
    "lvl": 2,
    "stem": "A triangle is equilateral. Its sides measure (3x − 4), (x + 6) and (2x + 1) cm. What is its perimeter?",
    "opts": [
      "21",
      "33",
      "15",
      "11"
    ],
    "ans": 1,
    "trick": "solving for x is only the middle step — the question asks for the perimeter, which is three sides",
    "why": "3x − 4 = x + 6 gives x = 5. Each side is 11 cm (2x + 1 = 11 agrees), so the perimeter is 33 cm.",
    "traps": [
      "A: 21 — x = 3 was substituted by mistake, giving 5 + 9 + 7.",
      "C: 15 — x = 5 was reported as if it were the answer to the question asked.",
      "D: 11 — a single side was reported instead of the perimeter."
    ]
  },
  {
    "sig": "typical-value-when-an-outlier-is-present",
    "code": "SAAT-Q.3",
    "unit": 5,
    "topic": "Statistics",
    "lvl": 2,
    "stem": "A shop records its daily sales of an item over eight days: 12, 13, 14, 15, 15, 16, 17 and 58. Which measure best describes a typical day?",
    "opts": [
      "Range",
      "Standard deviation",
      "Median",
      "Mean"
    ],
    "ans": 2,
    "trick": "an extreme value pulls the mean but barely moves the median — and spread measures are not measures of the centre at all",
    "why": "The median is 15 and ignores the size of 58, while the mean is 20 and is pulled toward it.",
    "traps": [
      "A: Range — the range measures spread, not a typical value.",
      "B: Standard deviation — the standard deviation also measures spread and is inflated by the extreme day.",
      "D: Mean — the mean is dragged upward by the single extreme day."
    ]
  },
  {
    "sig": "square-an-expression-to-find-a-sum-of-squares",
    "code": "SAAT-Q.4",
    "unit": 1,
    "topic": "Number & algebra",
    "lvl": 3,
    "stem": "If x − 1/x = 3, what is the value of x² + 1/x²?",
    "opts": [
      "9",
      "7",
      "13",
      "11"
    ],
    "ans": 3,
    "trick": "squaring (x − 1/x) produces a middle term of −2, which has to be ADDED back to isolate x² + 1/x²",
    "why": "(x − 1/x)² = x² − 2 + 1/x² = 9, so x² + 1/x² = 9 + 2 = 11.",
    "traps": [
      "A: 9 — the −2 from the cross term was dropped when squaring, giving 3².",
      "B: 7 — the cross term was subtracted twice instead of added back.",
      "C: 13 — the cross term 2 was added twice."
    ]
  },
  {
    "sig": "recognise-the-cosine-difference-formula",
    "code": "SAAT-Q.5",
    "unit": 9,
    "topic": "Trigonometry II",
    "lvl": 2,
    "stem": "What is the exact value form of cos 70° cos 20° + sin 70° sin 20°?",
    "opts": [
      "cos 50°",
      "cos 90°",
      "sin 50°",
      "sin 90°"
    ],
    "ans": 0,
    "trick": "cos A cos B + sin A sin B (a PLUS sign) is cos(A − B) — the sum formula has a minus sign",
    "why": "The expression has the form cos A cos B + sin A sin B = cos(A − B), so it equals cos(70° − 20°) = cos 50°.",
    "traps": [
      "B: cos 90° — the pattern was read as the sum formula, which has a minus sign, giving cos(70° + 20°).",
      "C: sin 50° — the cosine pattern was converted to a sine of the same difference.",
      "D: sin 90° — the sum of the angles was used with sine."
    ]
  },
  {
    "sig": "sign-of-a-simplified-trig-ratio",
    "code": "SAAT-Q.6",
    "unit": 8,
    "topic": "Trigonometry I",
    "lvl": 3,
    "stem": "For 0° < x < 360° (x ≠ 90°, 180°, 270°), in which quadrants is sin x ÷ tan x negative?",
    "opts": [
      "I and IV",
      "II and III",
      "III and IV",
      "II and IV"
    ],
    "ans": 1,
    "trick": "simplify first: sin x ÷ tan x = cos x, so the question is only where cosine is negative",
    "why": "Since tan x = sin x ÷ cos x, the ratio equals cos x, which is negative in quadrants II and III.",
    "traps": [
      "A: I and IV — the quadrants where cos x is positive were chosen.",
      "C: III and IV — only the sign of sin x was tracked, which is negative in III and IV.",
      "D: II and IV — only the sign of tan x was tracked, which is negative in II and IV."
    ]
  },
  {
    "sig": "minutes-to-seconds-in-scientific-notation",
    "code": "SAAT-Q.7",
    "unit": 1,
    "topic": "Number & algebra",
    "lvl": 1,
    "stem": "A reaction takes 4 minutes. Write its duration in seconds in scientific notation.",
    "opts": [
      "2.4 × 10³",
      "0.24 × 10³",
      "2.4 × 10²",
      "2.4 × 10¹"
    ],
    "ans": 2,
    "trick": "after converting to 240 s, the coefficient must lie between 1 and 10 — 0.24 × 10³ is the right number in the wrong form",
    "why": "4 × 60 = 240 s = 2.4 × 10² s.",
    "traps": [
      "A: 2.4 × 10³ — the power of ten is one too large, which describes 2 400 seconds.",
      "B: 0.24 × 10³ — the value is 240, but the coefficient is not between 1 and 10 so it is not scientific notation.",
      "D: 2.4 × 10¹ — the power of ten is one too small, which describes 24 seconds."
    ]
  },
  {
    "sig": "derivative-of-a-constant-power",
    "code": "SAAT-Q.8",
    "unit": 11,
    "topic": "Limits & calculus",
    "lvl": 1,
    "stem": "If f(x) = e³, what is f′(x)?",
    "opts": [
      "3e²",
      "e³",
      "3",
      "0"
    ],
    "ans": 3,
    "trick": "e³ is just a number — a constant — so its derivative is 0; e is not the variable here",
    "why": "f(x) = e³ does not change with x, so its rate of change is 0.",
    "traps": [
      "A: 3e² — the power rule was applied to e³ as if e were the variable.",
      "B: e³ — the constant was left unchanged by the derivative.",
      "C: 3 — the exponent was treated as the derivative."
    ]
  },
  {
    "sig": "at-most-budget-as-an-inequality",
    "code": "SAAT-Q.9",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 1,
    "stem": "A student buys x notebooks at SAR 7 each and y pens at SAR 4 each and may spend at most SAR 60 in total. Which inequality models this?",
    "opts": [
      "7x + 4y ≤ 60",
      "7x + 4y ≥ 60",
      "7x + 4y < 60",
      "4x + 7y ≤ 60"
    ],
    "ans": 0,
    "trick": "'at most' allows the limit itself, so it is ≤ — and each price must stay with its own item",
    "why": "Total cost 7x + 4y must not exceed 60, so 7x + 4y ≤ 60.",
    "traps": [
      "B: 7x + 4y ≥ 60 — 'at most' was reversed, so the total would have to reach SAR 60.",
      "C: 7x + 4y < 60 — the strict sign excludes spending exactly SAR 60, which is allowed.",
      "D: 4x + 7y ≤ 60 — the two prices were attached to the wrong items."
    ]
  },
  {
    "sig": "matrix-that-is-its-own-inverse",
    "code": "SAAT-Q.10",
    "unit": 2,
    "topic": "Equations, matrices & systems",
    "lvl": 3,
    "stem": "Which of these 2 × 2 matrices is equal to its own inverse?",
    "opts": [
      "rows (0, −1) and (1, 0)",
      "rows (0, 1) and (1, 0)",
      "rows (1, 1) and (0, 1)",
      "rows (2, 0) and (0, 2)"
    ],
    "ans": 1,
    "trick": "a matrix equals its own inverse when squaring it gives the identity — having determinant 1 or being diagonal is not enough",
    "why": "The swap matrix squared is the identity, so A × A = I and A⁻¹ = A.",
    "traps": [
      "A: rows (0, −1) and (1, 0) — it is a quarter-turn, whose inverse is the opposite quarter-turn.",
      "C: rows (1, 1) and (0, 1) — it has determinant 1, but its inverse has −1 in the corner, so it differs from itself.",
      "D: rows (2, 0) and (0, 2) — it is a multiple of the identity, but its inverse has entries ½, not 2."
    ]
  },
  {
    "sig": "solve-for-an-exponent-after-dividing-the-coefficient",
    "code": "SAAT-Q.11",
    "unit": 6,
    "topic": "Exponentials & logarithms",
    "lvl": 2,
    "stem": "If 5 · 2^m = 80, what is the value of m?",
    "opts": [
      "8",
      "5",
      "4",
      "16"
    ],
    "ans": 2,
    "trick": "divide by the coefficient first — then 2^m = 16 is a power of 2, and m is its exponent, not 16",
    "why": "5 · 2^m = 80 gives 2^m = 16 = 2⁴, so m = 4.",
    "traps": [
      "A: 8 — the coefficient 5 was multiplied into the base, giving 10^m = 80, and then m was guessed.",
      "B: 5 — the coefficient 5 was read as the exponent.",
      "D: 16 — this is the value of 2^m, not of m."
    ]
  },
  {
    "sig": "complete-roots-of-a-quintic-over-the-complex-numbers",
    "code": "SAAT-Q.12",
    "unit": 7,
    "topic": "Sequences, series & complex numbers",
    "lvl": 3,
    "stem": "What is the complete solution set of x⁵ − 81x = 0 over the complex numbers?",
    "opts": [
      "0, ±3",
      "0, ±9, ±9i",
      "±3, ±3i",
      "0, ±3, ±3i"
    ],
    "ans": 3,
    "trick": "factor out x first, then x² − 9 and x² + 9 — the second factor supplies the imaginary pair and the first gives the root 0",
    "why": "x(x⁴ − 81) = x(x² − 9)(x² + 9) = 0 gives 0, ±3 and ±3i — five roots in all.",
    "traps": [
      "A: 0, ±3 — only the real roots were kept and the pair from x² + 9 = 0 was dropped.",
      "B: 0, ±9, ±9i — 81 was used where 9 belongs, so the fourth root of 81 was not taken.",
      "C: ±3, ±3i — the common factor x was lost when factoring, so the root 0 disappeared."
    ]
  },
  {
    "sig": "slope-of-a-distance-time-line-is-signed-velocity",
    "code": "SAAT-Q.13",
    "unit": 3,
    "topic": "Functions & graphs",
    "lvl": 2,
    "stem": "A cyclist's distance from home is 60 km at t = 0 hours and 0 km at t = 4 hours, and the graph is a straight line. What is the slope of this line?",
    "opts": [
      "−15",
      "15",
      "−4",
      "60"
    ],
    "ans": 0,
    "trick": "slope is rise over run with the sign kept — a distance that falls over time gives a negative velocity",
    "why": "(0 − 60) ÷ (4 − 0) = −15, so the slope is −15 km per hour.",
    "traps": [
      "B: 15 — the sign was lost; the cyclist is moving toward home, so the slope is negative.",
      "C: −4 — the elapsed time was reported instead of the rate.",
      "D: 60 — the starting distance was reported instead of the rate."
    ]
  }
];
