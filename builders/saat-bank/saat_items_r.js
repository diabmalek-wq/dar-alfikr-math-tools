// SAAT BANK — part R: figure items redrawn from skills seen in leak/trial papers (Nov 2026). Figures drawn from the answer's own coordinates (spec_r.py).
module.exports = [
  {
    "sig": "smallest-angle-from-a-labelled-triangle",
    "code": "SAAT-R.1",
    "unit": 4,
    "topic": "Triangles, polygons & quadrilaterals",
    "lvl": 2,
    "fig": "r_tri_sides",
    "figW": 1.9,
    "stem": "Triangle ABC is drawn with its side lengths marked. Which angle is the smallest?",
    "opts": [
      "∠C",
      "∠A",
      "∠B",
      "∠B and ∠C are equal"
    ],
    "ans": 0,
    "trick": "the smallest angle sits opposite the SHORTEST side — find the side first, then read across the triangle to the vertex that faces it",
    "why": "The shortest side is AB = 6 cm; the vertex facing it is C, so ∠C is the smallest (about 41°).",
    "traps": [
      "B: ∠A — the angle facing the longest side (BC) is the LARGEST, not the smallest.",
      "C: ∠B — the middle side, CA, faces this angle; it is neither smallest nor largest.",
      "D: ∠B and ∠C are equal — the two sides facing them, 7 cm and 6 cm, are different, so the angles differ."
    ]
  },
  {
    "sig": "isosceles-base-angle-with-an-algebraic-label",
    "code": "SAAT-R.2",
    "unit": 4,
    "topic": "Triangles, polygons & quadrilaterals",
    "lvl": 2,
    "fig": "r_iso_ticks",
    "figW": 1.7,
    "stem": "In the figure, the tick marks show that AB = AC. The angle at A measures 48° and the angle at B measures (3x)°. What is the value of x?",
    "opts": [
      "66",
      "22",
      "16",
      "44"
    ],
    "ans": 1,
    "trick": "equal sides mean equal BASE angles — two of them — so the 180° sum is 48 + 3x + 3x, and 3x is not yet x",
    "why": "48 + 3x + 3x = 180 gives 6x = 132, so x = 22 (each base angle is 66°).",
    "traps": [
      "A: 66 — this is the size of one base angle, 3x, not the value of x.",
      "C: 16 — the base angle was set equal to the apex angle, 3x = 48.",
      "D: 44 — x was doubled after finding it, as if both base angles were added in."
    ]
  },
  {
    "sig": "angle-in-a-semicircle-with-algebraic-angles",
    "code": "SAAT-R.3",
    "unit": 4,
    "topic": "Circles",
    "lvl": 3,
    "fig": "r_thales",
    "figW": 1.8,
    "stem": "In the figure, O is the centre of the circle and AB is a diameter. The angles at A and B of triangle ABC measure (2x + 4)° and (3x + 1)°. What is the value of x?",
    "opts": [
      "35",
      "38",
      "17",
      "18"
    ],
    "ans": 2,
    "trick": "an angle in a semicircle is 90°, so the other two angles add to 90° — not 180° — before the constants are handled",
    "why": "∠C = 90° because AB is a diameter, so (2x + 4) + (3x + 1) = 90, 5x = 85 and x = 17.",
    "traps": [
      "A: 35 — the two angles were set to add to 180°, giving 5x + 5 = 180.",
      "B: 38 — this is the size of the angle at A, 2x + 4, not x.",
      "D: 18 — the constants 4 and 1 were left out, so 5x = 90."
    ]
  },
  {
    "sig": "alternate-angles-in-a-trapezoid-with-crossing-diagonals",
    "code": "SAAT-R.4",
    "unit": 4,
    "topic": "Triangles, polygons & quadrilaterals",
    "lvl": 3,
    "fig": "r_trap_diag",
    "figW": 2.0,
    "stem": "In trapezoid ABCD, AB ∥ DC (marked with arrows) and the diagonals AC and BD meet at E. If ∠AEB = 110° and ∠ABD = 40°, what is the measure of ∠ACD?",
    "opts": [
      "40",
      "70",
      "110",
      "30"
    ],
    "ans": 3,
    "trick": "parallel sides give alternate angles that carry the 40° across to D; then the vertical angle at E lets triangle DEC be closed",
    "why": "∠BDC = ∠ABD = 40° (alternate angles) and ∠DEC = ∠AEB = 110° (vertical), so ∠DCE = 180° − 110° − 40° = 30°, which is ∠ACD.",
    "traps": [
      "A: 40 — this is ∠BDC, which equals ∠ABD, but the question asks for the angle at C.",
      "B: 70 — this is the supplement of ∠AEB, 180° − 110°, a linear-pair angle.",
      "C: 110 — this is ∠DEC, which is vertical to ∠AEB, not an angle at C."
    ]
  },
  {
    "sig": "intervals-of-decrease-with-a-flat-segment",
    "code": "SAAT-R.5",
    "unit": 3,
    "topic": "Functions & graphs",
    "lvl": 2,
    "fig": "r_decreasing",
    "figW": 2.5,
    "stem": "The graph of a piecewise-linear function f is shown. On which intervals is f decreasing?",
    "opts": [
      "(−5, −3) and (2, 4)",
      "(−3, 0) and (4, 6)",
      "(−5, −3) and (0, 2) and (2, 4)",
      "(−3, 4)"
    ],
    "ans": 0,
    "trick": "'decreasing' means the graph FALLS as x increases — a flat piece does not count, and every falling piece must be listed",
    "why": "The graph falls from (−5, 1) to (−3, −2) and from (2, 3) to (4, −1), and is level on (0, 2), so f is decreasing on (−5, −3) and (2, 4).",
    "traps": [
      "B: (−3, 0) and (4, 6) — these are the intervals where the graph rises, so the direction was reversed.",
      "C: (−5, −3) and (0, 2) and (2, 4) — the flat segment from x = 0 to x = 2 was counted as decreasing; a level piece neither rises nor falls.",
      "D: (−3, 4) — the single stretch from the low point to the next low point was taken, ignoring that the graph rises in between."
    ]
  },
  {
    "sig": "slope-from-a-labelled-distance-time-graph",
    "code": "SAAT-R.6",
    "unit": 3,
    "topic": "Functions & graphs",
    "lvl": 2,
    "fig": "r_dist_time",
    "figW": 2.2,
    "stem": "The graph shows a cyclist's distance d from home (in km) against time t (in hours). The line passes through the two labelled points. What is the slope of the line?",
    "opts": [
      "48",
      "−8",
      "8",
      "−6"
    ],
    "ans": 1,
    "trick": "slope is rise over run with its sign — a distance that shrinks over time gives a negative slope, and the intercept is not the slope",
    "why": "(0 − 48) ÷ (6 − 0) = −8, so the slope is −8 km per hour.",
    "traps": [
      "A: 48 — the starting distance, the d-intercept, was reported instead of the slope.",
      "C: 8 — the sign was dropped, but d falls as t rises, so the slope is negative.",
      "D: −6 — the elapsed time was reported instead of the rate."
    ]
  },
  {
    "sig": "system-of-inequalities-from-a-shaded-wedge",
    "code": "SAAT-R.7",
    "unit": 2,
    "topic": "Equations & inequalities",
    "lvl": 3,
    "fig": "r_system_wedge",
    "figW": 2.1,
    "stem": "The shaded region is bounded by the two lines shown, with both boundaries included. Which system of inequalities describes it?",
    "opts": [
      "y ≥ x − 1  and  y ≥ −x + 5",
      "y ≤ x − 1  and  y ≥ −x + 5",
      "y ≥ x − 1  and  y ≤ −x + 5",
      "y ≤ x − 1  and  y ≤ −x + 5"
    ],
    "ans": 2,
    "trick": "test one point inside the shaded region in each inequality — a point such as (1, 2) is above y = x − 1 and below y = −x + 5",
    "why": "The shading is above the rising line y = x − 1 and below the falling line y = −x + 5, so y ≥ x − 1 and y ≤ −x + 5.",
    "traps": [
      "A: y ≥ x − 1  and  y ≥ −x + 5 — the region above BOTH lines is the wedge opening upward.",
      "B: y ≤ x − 1  and  y ≥ −x + 5 — the region above y = −x + 5 and below y = x − 1 is the wedge opening to the right.",
      "D: y ≤ x − 1  and  y ≤ −x + 5 — the region below BOTH lines is the wedge opening downward, not the one shown."
    ]
  },
  {
    "sig": "inscribed-angles-on-the-same-arc-are-equal",
    "code": "SAAT-R.8",
    "unit": 4,
    "topic": "Circles",
    "lvl": 3,
    "fig": "r_same_arc",
    "figW": 1.9,
    "stem": "In the circle shown, ∠ACB = (3x + 5)° and ∠ADB = (5x − 15)°. Both angles stand on the same chord AB. What is the measure of ∠ADB?",
    "opts": [
      "10",
      "70",
      "145",
      "35"
    ],
    "ans": 3,
    "trick": "two inscribed angles on the same arc are equal — set the two expressions equal, then substitute back to get the ANGLE, not x",
    "why": "3x + 5 = 5x − 15 gives x = 10, so ∠ADB = 5(10) − 15 = 35°.",
    "traps": [
      "A: 10 — this is the value of x, not the angle.",
      "B: 70 — this is the size of arc AB, double the inscribed angle.",
      "C: 145 — this is the supplement of the angle, as if the two angles were on opposite sides of the chord."
    ]
  }
];
