// SAAT BANK — part O: skills found by a web/Telegram sweep (Nov 2026) that no earlier sig held.
// Sourcing rule: skill and trap only; stems, numbers and options are original.
module.exports = [
  {
    "sig": "reflect-a-point-in-the-x-axis",
    "code": "SAAT-O.1",
    "unit": 5,
    "topic": "Coordinate geometry & transformations",
    "lvl": 1,
    "stem": "The point (−4, 7) is reflected in the x-axis. What are the coordinates of its image?",
    "opts": [
      "(4, −7)",
      "(7, −4)",
      "(−4, −7)",
      "(4, 7)"
    ],
    "ans": 2,
    "trick": "a reflection in the x-axis keeps the x-coordinate and changes only the SIGN of y — the other three answers each apply a different rule",
    "why": "The x-axis is the mirror, so the horizontal position is unchanged and the height flips sign: (−4, 7) → (−4, −7).",
    "traps": [
      "A: (4, −7) — both signs flipped, which is a half-turn about the origin.",
      "B: (7, −4) — the coordinates swapped, which is a reflection in y = x.",
      "D: (4, 7) — the y-axis rule applied (x negated instead of y)."
    ]
  },
  {
    "sig": "reflect-a-point-on-an-axis-in-the-y-axis",
    "code": "SAAT-O.2",
    "unit": 5,
    "topic": "Coordinate geometry & transformations",
    "lvl": 2,
    "stem": "The point (5, 0) is reflected in the y-axis. What are the coordinates of its image?",
    "opts": [
      "(0, 5)",
      "(−5, 0)",
      "(0, −5)",
      "(5, 0)"
    ],
    "ans": 1,
    "trick": "a point with a zero coordinate still follows the rule — negate x and leave y — so it does NOT stay put and does NOT jump onto the other axis",
    "why": "Reflection in the y-axis negates x only: (5, 0) → (−5, 0).",
    "traps": [
      "A: (0, 5) — the coordinates swapped with no sign change.",
      "C: (0, −5) — the coordinates swapped and a sign added, the commonest slip when one coordinate is 0.",
      "D: (5, 0) — assuming a point lying on an axis is unchanged by any reflection."
    ]
  },
  {
    "sig": "polar-equation-with-a-constant-angle-is-a-line",
    "code": "SAAT-O.3",
    "unit": 10,
    "topic": "Polar coordinates & equations",
    "lvl": 2,
    "stem": "In polar coordinates, r can take any real value. Which Cartesian equation describes the graph of θ = π/4?",
    "opts": [
      "y = x",
      "y = −x",
      "y = π/4",
      "x² + y² = π/4"
    ],
    "ans": 0,
    "trick": "a fixed angle with r free sweeps out a STRAIGHT LINE through the pole, with slope tan θ — it is not a circle and the angle is not a height",
    "why": "Every point on θ = π/4 satisfies y/x = tan(π/4) = 1, so y = x (negative r supplies the part of the line below the pole).",
    "traps": [
      "B: y = −x — the slope taken as tan(−π/4) or the quadrant mixed up.",
      "C: y = π/4 — the angle value read as a y-height.",
      "D: x² + y² = π/4 — confusing a constant angle with a constant radius."
    ]
  },
  {
    "sig": "secant-from-sine-in-the-second-quadrant",
    "code": "SAAT-O.4",
    "unit": 8,
    "topic": "Sine, cosine & tangent",
    "lvl": 3,
    "stem": "θ is an angle in the second quadrant with sin θ = 3/5. What is sec θ?",
    "opts": [
      "−5/3",
      "−5/4",
      "5/4",
      "−4/5"
    ],
    "ans": 1,
    "trick": "find cos first from the Pythagorean identity, give it the QUADRANT sign (negative in Q II), and only then take the reciprocal",
    "why": "cos²θ = 1 − 9/25 = 16/25, so cos θ = −4/5 in Q II; sec θ = 1/cos θ = −5/4.",
    "traps": [
      "A: −5/3 — this is csc θ (5/3) given a minus sign, so the wrong function was reciprocated.",
      "C: 5/4 — the quadrant sign forgotten.",
      "D: −4/5 — cos θ given instead of its reciprocal."
    ]
  },
  {
    "sig": "reciprocal-identities-as-a-quotient",
    "code": "SAAT-O.5",
    "unit": 9,
    "topic": "Trigonometric identities",
    "lvl": 2,
    "stem": "Simplify (sec θ)/(csc θ).",
    "opts": [
      "tan θ",
      "cot θ",
      "sin θ cos θ",
      "1"
    ],
    "ans": 0,
    "trick": "write each as its reciprocal and divide: (1/cos θ)÷(1/sin θ) flips to sin θ / cos θ — the inverted quotient cos θ / sin θ is the trap",
    "why": "(1/cos θ) ÷ (1/sin θ) = (1/cos θ)(sin θ/1) = sin θ / cos θ = tan θ.",
    "traps": [
      "B: cot θ — the quotient written upside down.",
      "C: sin θ cos θ — the two reciprocals multiplied out instead of divided.",
      "D: 1 — treating sec and csc as equal."
    ]
  },
  {
    "sig": "two-points-determine-exactly-one-line",
    "code": "SAAT-O.6",
    "unit": 4,
    "topic": "Points, lines & planes",
    "lvl": 1,
    "stem": "Which statement is always true?",
    "opts": [
      "Through any three points there is exactly one line.",
      "Any two lines intersect in exactly one point.",
      "Exactly one line passes through a given point.",
      "Through any two distinct points there is exactly one line."
    ],
    "ans": 3,
    "trick": "an 'always' statement must hold for EVERY case — three points can be non-collinear and two lines can be parallel, so only the two-point statement survives",
    "why": "Two distinct points fix a unique line (a basic axiom). Three points on no common line have no line through all of them; parallel lines never meet; infinitely many lines pass through one point.",
    "traps": [
      "A: Through any three points there is exactly one line. — three points need not be collinear, so no line may contain them.",
      "B: Any two lines intersect in exactly one point. — parallel lines do not intersect.",
      "C: Exactly one line passes through a given point. — infinitely many lines pass through any one point."
    ]
  },
  {
    "sig": "radius-from-the-area-of-a-circle",
    "code": "SAAT-O.7",
    "unit": 4,
    "topic": "Circles: area & circumference",
    "lvl": 1,
    "stem": "A circular garden has an area of 81π m². What is its radius?",
    "opts": [
      "9 m",
      "18 m",
      "40.5 m",
      "81 m"
    ],
    "ans": 0,
    "trick": "area is πr², so r² = 81 and r = 9 — not the diameter, and the area is not halved to find a radius",
    "why": "πr² = 81π gives r² = 81, so r = 9 m.",
    "traps": [
      "B: 18 m — the diameter reported as the radius.",
      "C: 40.5 m — the area halved, as if it were a circumference-style relation.",
      "D: 81 m — r² taken as r."
    ]
  },
  {
    "sig": "logarithm-of-two-powers-of-one-base",
    "code": "SAAT-O.8",
    "unit": 6,
    "topic": "Logarithms & their properties",
    "lvl": 3,
    "stem": "Evaluate log₈ 32.",
    "opts": [
      "4",
      "24",
      "5/3",
      "3/5"
    ],
    "ans": 2,
    "trick": "write both numbers as powers of 2 — 8 = 2³ and 32 = 2⁵ — so the answer is the exponent RATIO 5/3, not the quotient of the arguments",
    "why": "Let x = log₈ 32. Then 8^x = 32, so 2^(3x) = 2⁵, 3x = 5, x = 5/3.",
    "traps": [
      "A: 4 — dividing 32 by 8 as if the log were a quotient.",
      "B: 24 — 32 − 8 computed, as if the logarithm were a difference.",
      "D: 3/5 — the ratio of exponents inverted."
    ]
  },
  {
    "sig": "undefined-cotangent-angle",
    "code": "SAAT-O.9",
    "unit": 8,
    "topic": "Sine, cosine & tangent",
    "lvl": 2,
    "stem": "Which of these angles makes cot θ undefined?",
    "opts": [
      "0°",
      "45°",
      "90°",
      "135°"
    ],
    "ans": 0,
    "trick": "cot θ = cos θ / sin θ, so it is undefined where SIN θ = 0 — the angle that breaks tan θ (90°) is the one that makes cot θ equal zero",
    "why": "sin 0° = 0, so cos 0° / sin 0° has a zero denominator. At 90° cot θ = 0/1 = 0; at 45° it is 1; at 135° it is −1.",
    "traps": [
      "B: 45° — a special angle chosen at random.",
      "C: 90° — the angle where TAN is undefined, applied to cot.",
      "D: 135° — a quadrant-two angle with no zero denominator."
    ]
  },
  {
    "sig": "median-of-an-unsorted-list",
    "code": "SAAT-O.10",
    "unit": 5,
    "topic": "Data representation & measures of centre",
    "lvl": 2,
    "stem": "Find the median of 9, 3, 12, 5, 6.",
    "opts": [
      "9",
      "6",
      "7",
      "12"
    ],
    "ans": 1,
    "trick": "the median is the middle value AFTER ordering — taking the middle entry of the list as written, or the mean, are the two usual wrong turns",
    "why": "Ordered: 3, 5, 6, 9, 12. The middle (third) value is 6.",
    "traps": [
      "A: 9 — the fourth ordered value, an off-by-one count.",
      "C: 7 — the mean (35 ÷ 5) given instead of the median.",
      "D: 12 — the middle entry of the unordered list."
    ]
  },
  {
    "sig": "evaluate-a-function-at-a-negative-input",
    "code": "SAAT-O.11",
    "unit": 3,
    "topic": "Evaluating functions",
    "lvl": 2,
    "stem": "If f(x) = 2x² − 3, find f(−4).",
    "opts": [
      "−35",
      "61",
      "−11",
      "29"
    ],
    "ans": 3,
    "trick": "square the NEGATIVE input first so it becomes positive, then apply the 2 and the −3 — (−4)² is 16, not −16",
    "why": "f(−4) = 2(−4)² − 3 = 2(16) − 3 = 29.",
    "traps": [
      "A: −35 — (−4)² taken as −16, so 2(−16) − 3.",
      "B: 61 — the 2 placed inside the square: (2·(−4))² − 3.",
      "C: −11 — (−4)² dropped and 2(−4) − 3 used instead."
    ]
  }
];
