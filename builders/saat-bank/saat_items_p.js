// SAAT BANK — part P: skills read (skill and trap only) from a 1,105-question teacher booklet (Nov 2026).
// Stems, numbers and options are original; every key is re-derived by a predicate in spec_p.py.
module.exports = [
  {
    "sig": "rotation-of-a-point-90-degrees-about-the-origin",
    "code": "SAAT-P.1",
    "unit": 4,
    "topic": "Transformations & symmetry",
    "lvl": 2,
    "stem": "The point (4, 1) is rotated 90° anticlockwise about the origin. What are the coordinates of its image?",
    "opts": [
      "(−1, 4)",
      "(1, −4)",
      "(−4, −1)",
      "(1, 4)"
    ],
    "ans": 0,
    "trick": "a quarter-turn anticlockwise sends (x, y) to (−y, x) — swapping with no sign change is a reflection, not a rotation",
    "why": "Multiplying 4 + i by i gives −1 + 4i, so (4, 1) → (−1, 4).",
    "traps": [
      "B: (1, −4) — the rotation was taken clockwise.",
      "C: (−4, −1) — a half-turn was applied instead of a quarter-turn.",
      "D: (1, 4) — the coordinates were swapped with no sign change, which is a reflection in y = x."
    ]
  },
  {
    "sig": "rotation-of-a-point-270-degrees-about-the-origin",
    "code": "SAAT-P.2",
    "unit": 4,
    "topic": "Transformations & symmetry",
    "lvl": 3,
    "stem": "The point (−2, 5) is rotated 270° anticlockwise about the origin. What are the coordinates of its image?",
    "opts": [
      "(−5, 2)",
      "(5, 2)",
      "(−5, −2)",
      "(2, −5)"
    ],
    "ans": 1,
    "trick": "270° anticlockwise equals 90° clockwise, which sends (x, y) to (y, −x)",
    "why": "Multiplying −2 + 5i by i³ = −i gives 5 + 2i, so the image is (5, 2).",
    "traps": [
      "A: (−5, 2) — the coordinates were swapped and the wrong sign was changed.",
      "C: (−5, −2) — only a 90° anticlockwise turn was applied.",
      "D: (2, −5) — a 180° turn was applied."
    ]
  },
  {
    "sig": "point-reflection-through-the-origin",
    "code": "SAAT-P.3",
    "unit": 4,
    "topic": "Transformations & symmetry",
    "lvl": 1,
    "stem": "What is the image of the point (−3, 1) under a reflection through the origin (a point reflection)?",
    "opts": [
      "(−3, −1)",
      "(1, −3)",
      "(3, −1)",
      "(3, 1)"
    ],
    "ans": 2,
    "trick": "a point reflection through the origin negates BOTH coordinates — negating only one is an axis reflection",
    "why": "(x, y) → (−x, −y), so (−3, 1) → (3, −1).",
    "traps": [
      "A: (−3, −1) — reflected in the x-axis only.",
      "B: (1, −3) — the coordinates were swapped.",
      "D: (3, 1) — reflected in the y-axis only."
    ]
  },
  {
    "sig": "two-axis-reflections-make-a-half-turn",
    "code": "SAAT-P.4",
    "unit": 4,
    "topic": "Transformations & symmetry",
    "lvl": 2,
    "stem": "A figure is reflected in the x-axis and then in the y-axis. The single transformation that does the same is a rotation about the origin through:",
    "opts": [
      "90°",
      "270°",
      "360°",
      "180°"
    ],
    "ans": 3,
    "trick": "reflecting in two perpendicular lines is the same as turning through TWICE the angle between them — 180° for the axes",
    "why": "The first reflection gives (x, −y), the second gives (−x, −y), which is a half-turn.",
    "traps": [
      "A: 90° — two reflections were taken to make a quarter-turn.",
      "B: 270° — a three-quarter turn was chosen.",
      "C: 360° — a full turn would leave the figure unchanged, but the figure ends up on the opposite side."
    ]
  },
  {
    "sig": "translation-rule-from-two-points",
    "code": "SAAT-P.5",
    "unit": 4,
    "topic": "Transformations & symmetry",
    "lvl": 2,
    "stem": "A translation moves the point A(2, −1) to B(7, 3). Which rule describes it?",
    "opts": [
      "(x, y) → (x + 5, y + 4)",
      "(x, y) → (x + 4, y + 5)",
      "(x, y) → (x − 5, y − 4)",
      "(x, y) → (x + 9, y + 2)"
    ],
    "ans": 0,
    "trick": "the shift is image minus original, coordinate by coordinate — in that order",
    "why": "dx = 7 − 2 = 5 and dy = 3 − (−1) = 4, so (x, y) → (x + 5, y + 4).",
    "traps": [
      "B: (x, y) → (x + 4, y + 5) — the horizontal and vertical shifts were swapped.",
      "C: (x, y) → (x − 5, y − 4) — the rule was written in the reverse direction, B to A.",
      "D: (x, y) → (x + 9, y + 2) — the coordinates of A and B were added instead of subtracted."
    ]
  },
  {
    "sig": "rotational-symmetry-angle-of-a-regular-polygon",
    "code": "SAAT-P.6",
    "unit": 4,
    "topic": "Transformations & symmetry",
    "lvl": 2,
    "stem": "What is the smallest angle of rotation, about its centre, that maps a regular hexagon onto itself?",
    "opts": [
      "90°",
      "60°",
      "120°",
      "30°"
    ],
    "ans": 1,
    "trick": "the smallest turn is 360° divided by the number of sides — not the interior angle",
    "why": "360° ÷ 6 = 60°.",
    "traps": [
      "A: 90° — a quarter-turn was assumed for every polygon.",
      "C: 120° — the interior angle of a regular hexagon was given.",
      "D: 30° — half of the correct angle was taken."
    ]
  },
  {
    "sig": "number-of-sides-from-an-interior-angle",
    "code": "SAAT-P.7",
    "unit": 4,
    "topic": "Triangles, polygons & quadrilaterals",
    "lvl": 2,
    "stem": "Each interior angle of a regular polygon measures 156°. How many sides does the polygon have?",
    "opts": [
      "14",
      "16",
      "15",
      "24"
    ],
    "ans": 2,
    "trick": "go through the exterior angle: 180° − 156° = 24°, then 360° ÷ 24° — the 24 is an angle, not the answer",
    "why": "Exterior angle = 24°, so n = 360 ÷ 24 = 15.",
    "traps": [
      "A: 14 — the division was off by one.",
      "B: 16 — the division was off by one in the other direction.",
      "D: 24 — the exterior angle, 24°, was reported as the number of sides."
    ]
  },
  {
    "sig": "number-of-sides-from-the-interior-angle-sum",
    "code": "SAAT-P.8",
    "unit": 4,
    "topic": "Triangles, polygons & quadrilaterals",
    "lvl": 2,
    "stem": "The interior angles of a polygon add up to 1620°. How many sides does it have?",
    "opts": [
      "9",
      "10",
      "12",
      "11"
    ],
    "ans": 3,
    "trick": "the sum is 180(n − 2), so after dividing by 180 you must ADD 2 to reach n",
    "why": "180(n − 2) = 1620 gives n − 2 = 9, so n = 11.",
    "traps": [
      "A: 9 — 1620 ÷ 180 was taken without adding the 2.",
      "B: 10 — the sum formula was solved with an off-by-one slip.",
      "C: 12 — the sum formula was solved with an off-by-one slip the other way."
    ]
  },
  {
    "sig": "which-lengths-form-a-triangle",
    "code": "SAAT-P.9",
    "unit": 4,
    "topic": "Triangles, polygons & quadrilaterals",
    "lvl": 2,
    "stem": "Which set of three lengths can be the sides of a triangle?",
    "opts": [
      "5, 7, 11",
      "3, 4, 8",
      "6, 6, 13",
      "4, 9, 13"
    ],
    "ans": 0,
    "trick": "the two shorter sides must add to MORE than the longest — equal is a flat line, not a triangle",
    "why": "5 + 7 = 12 > 11, so only 5, 7, 11 passes.",
    "traps": [
      "B: 3, 4, 8 — 3 + 4 = 7, which is less than 8.",
      "C: 6, 6, 13 — 6 + 6 = 12, which is less than 13.",
      "D: 4, 9, 13 — 4 + 9 = 13 exactly, so the three lengths collapse into a straight line."
    ]
  },
  {
    "sig": "impossible-perimeter-from-two-sides",
    "code": "SAAT-P.10",
    "unit": 4,
    "topic": "Triangles, polygons & quadrilaterals",
    "lvl": 3,
    "stem": "Two sides of a triangle measure 6 and 11. Which of these cannot be the perimeter of the triangle?",
    "opts": [
      "33",
      "22",
      "25",
      "30"
    ],
    "ans": 1,
    "trick": "the third side lies strictly between 5 and 17, so the perimeter lies strictly between 22 and 34 — the end values are excluded",
    "why": "A perimeter of 22 would make the third side 5, and 6 + 5 = 11 is not greater than 11.",
    "traps": [
      "A: 33 — the third side would be 16, which is allowed.",
      "C: 25 — the third side would be 8, which is allowed.",
      "D: 30 — the third side would be 13, which is allowed."
    ]
  },
  {
    "sig": "larger-of-two-supplementary-angles-in-a-ratio",
    "code": "SAAT-P.11",
    "unit": 4,
    "topic": "Triangles, polygons & quadrilaterals",
    "lvl": 2,
    "stem": "Two supplementary angles are in the ratio 2 : 3. What is the measure of the larger angle?",
    "opts": [
      "120°",
      "90°",
      "108°",
      "72°"
    ],
    "ans": 2,
    "trick": "split 180° into 2 + 3 = 5 parts and then read off the part that is asked for",
    "why": "One part is 36°, so the larger angle is 3 × 36° = 108°.",
    "traps": [
      "A: 120° — 180° was split 1 : 2 instead of 2 : 3.",
      "B: 90° — the two angles were assumed to be equal.",
      "D: 72° — the smaller angle was given."
    ]
  },
  {
    "sig": "classify-a-triangle-from-two-angles",
    "code": "SAAT-P.12",
    "unit": 4,
    "topic": "Triangles, polygons & quadrilaterals",
    "lvl": 2,
    "stem": "A triangle has two angles of 35° and 55°. How is the triangle best described?",
    "opts": [
      "Acute and isosceles",
      "Obtuse and scalene",
      "Right and isosceles",
      "Right and scalene"
    ],
    "ans": 3,
    "trick": "find the THIRD angle first, then classify by angles and by sides separately — three different angles mean scalene",
    "why": "The third angle is 180° − 90° = 90°, and 35°, 55°, 90° are all different.",
    "traps": [
      "A: Acute and isosceles — the third angle was left unchecked and the triangle was assumed acute.",
      "B: Obtuse and scalene — the third angle was taken to be obtuse.",
      "C: Right and isosceles — the right angle was found, but equal sides were assumed."
    ]
  },
  {
    "sig": "fourth-vertex-of-a-parallelogram-from-three-vertices",
    "code": "SAAT-P.13",
    "unit": 4,
    "topic": "Coordinate geometry & quadrilaterals",
    "lvl": 3,
    "stem": "A(1, 2), B(5, 2) and C(7, 6) are three consecutive vertices of parallelogram ABCD. What are the coordinates of D?",
    "opts": [
      "(3, 6)",
      "(11, 6)",
      "(−1, −2)",
      "(3, 2)"
    ],
    "ans": 0,
    "trick": "in ABCD the diagonals share a midpoint, so D = A + C − B — check that AB and DC are equal vectors",
    "why": "AB = (4, 0), so DC must equal (4, 0): D = C − (4, 0) = (3, 6).",
    "traps": [
      "B: (11, 6) — B + C − A was used, pairing the wrong vertices.",
      "C: (−1, −2) — A + B − C was used.",
      "D: (3, 2) — the x-coordinate is right but the y-coordinate was copied from A."
    ]
  },
  {
    "sig": "half-diagonal-of-a-rectangle",
    "code": "SAAT-P.14",
    "unit": 4,
    "topic": "Coordinate geometry & quadrilaterals",
    "lvl": 2,
    "stem": "A rectangle measures 9 by 12. Its diagonals meet at O. How far is O from each vertex?",
    "opts": [
      "6",
      "7.5",
      "15",
      "10.5"
    ],
    "ans": 1,
    "trick": "diagonals of a rectangle are equal and bisect each other, so the distance to a vertex is HALF the diagonal",
    "why": "Diagonal = √(9² + 12²) = 15, so OA = 7.5.",
    "traps": [
      "A: 6 — half of the shorter side was used.",
      "C: 15 — the full diagonal was given.",
      "D: 10.5 — the average of the two sides was used."
    ]
  },
  {
    "sig": "map-scale-to-actual-distance",
    "code": "SAAT-P.15",
    "unit": 4,
    "topic": "Similarity & scale",
    "lvl": 1,
    "stem": "On a map, 1 cm represents 40 km. Two cities are 2.5 cm apart on the map. What is the actual distance between them, in km?",
    "opts": [
      "16",
      "10",
      "100",
      "42.5"
    ],
    "ans": 2,
    "trick": "multiply the map length by the scale — the two quantities are in proportion, not added",
    "why": "2.5 × 40 = 100 km.",
    "traps": [
      "A: 16 — 40 was divided by 2.5.",
      "B: 10 — a decimal-place slip gave 2.5 × 4.",
      "D: 42.5 — 40 and 2.5 were added."
    ]
  },
  {
    "sig": "height-from-shadows-by-similar-triangles",
    "code": "SAAT-P.16",
    "unit": 4,
    "topic": "Similarity & scale",
    "lvl": 2,
    "stem": "A 2 m pole casts a shadow 1.2 m long. At the same moment a tree casts a shadow 9 m long. How tall is the tree, in metres?",
    "opts": [
      "5.4",
      "9.8",
      "18",
      "15"
    ],
    "ans": 3,
    "trick": "same sun angle means similar triangles — height : shadow is the same ratio for both, so multiply, not add",
    "why": "h/9 = 2/1.2, so h = 15 m.",
    "traps": [
      "A: 5.4 — the proportion was written upside down (1.2 × 9 ÷ 2).",
      "B: 9.8 — the difference in shadow lengths was added to the pole's height.",
      "C: 18 — the shadow was simply doubled."
    ]
  },
  {
    "sig": "perpendicular-from-the-centre-bisects-a-chord",
    "code": "SAAT-P.17",
    "unit": 4,
    "topic": "Circles",
    "lvl": 2,
    "stem": "In a circle with centre O, a line from O perpendicular to chord AB meets it at M. If AB = 18, what is AM?",
    "opts": [
      "9",
      "18",
      "36",
      "6"
    ],
    "ans": 0,
    "trick": "the perpendicular from the centre BISECTS the chord — half, not the whole and not a third",
    "why": "AM = MB, so AM = 18 ÷ 2 = 9.",
    "traps": [
      "B: 18 — the whole chord was reported.",
      "C: 36 — the chord was doubled.",
      "D: 6 — a third of the chord was taken instead of a half."
    ]
  },
  {
    "sig": "central-angle-between-equally-spaced-points",
    "code": "SAAT-P.18",
    "unit": 4,
    "topic": "Circles",
    "lvl": 2,
    "stem": "Eight points are equally spaced around a circle. What is the central angle between two neighbouring points?",
    "opts": [
      "135°",
      "45°",
      "60°",
      "90°"
    ],
    "ans": 1,
    "trick": "equal spacing splits the full 360° into equal parts — divide by the number of points",
    "why": "360° ÷ 8 = 45°.",
    "traps": [
      "A: 135° — the interior angle of a regular octagon was given.",
      "C: 60° — the angle for six points was used.",
      "D: 90° — a quarter-turn was assumed."
    ]
  },
  {
    "sig": "point-on-a-circle-from-centre-and-radius",
    "code": "SAAT-P.19",
    "unit": 4,
    "topic": "Circles",
    "lvl": 2,
    "stem": "A circle has centre (−2, 3) and radius 5. Which point lies on the circle?",
    "opts": [
      "(−4, 8)",
      "(0, 0)",
      "(1, 7)",
      "(3, 6)"
    ],
    "ans": 2,
    "trick": "a point is on the circle only if its squared distance from the centre equals r² — compute (x + 2)² + (y − 3)² for each",
    "why": "For (1, 7): 3² + 4² = 25 = 5².",
    "traps": [
      "A: (−4, 8) — its squared distance from the centre is 29, not 25.",
      "B: (0, 0) — its squared distance from the centre is 13, not 25.",
      "D: (3, 6) — its squared distance from the centre is 34, not 25."
    ]
  },
  {
    "sig": "additive-inverse-of-a-decimal",
    "code": "SAAT-P.20",
    "unit": 1,
    "topic": "Real numbers & their properties",
    "lvl": 1,
    "stem": "What is the additive inverse of −4.5?",
    "opts": [
      "−4.5",
      "−2/9",
      "2/9",
      "4.5"
    ],
    "ans": 3,
    "trick": "the additive inverse is what you ADD to reach 0 — it only changes the sign; it is not the reciprocal",
    "why": "−4.5 + 4.5 = 0.",
    "traps": [
      "A: −4.5 — the number itself was given.",
      "B: −2/9 — the multiplicative inverse was found.",
      "C: 2/9 — the reciprocal was found and its sign changed."
    ]
  },
  {
    "sig": "linear-rule-from-a-table-of-values",
    "code": "SAAT-P.21",
    "unit": 3,
    "topic": "Linear functions & equations",
    "lvl": 2,
    "stem": "The table shows x = 1, 2, 3, 4 and y = 5, 8, 11, 14. Which equation fits every pair?",
    "opts": [
      "y = 3x + 2",
      "y = 2x + 3",
      "y = 3x − 2",
      "y = 4x + 1"
    ],
    "ans": 0,
    "trick": "test the rule on at least TWO pairs — several wrong rules still match the first row",
    "why": "The differences in y are 3, so the slope is 3, and 5 = 3(1) + 2.",
    "traps": [
      "B: y = 2x + 3 — the slope and the intercept were swapped; it fits only the first pair.",
      "C: y = 3x − 2 — the intercept has the wrong sign.",
      "D: y = 4x + 1 — it fits the first pair only."
    ]
  },
  {
    "sig": "equation-of-a-horizontal-line-through-two-points",
    "code": "SAAT-P.22",
    "unit": 3,
    "topic": "Linear functions & equations",
    "lvl": 1,
    "stem": "Which equation describes the line through (3, −2) and (−4, −2)?",
    "opts": [
      "x = 3",
      "y = −2",
      "x = −2",
      "y = 3"
    ],
    "ans": 1,
    "trick": "equal y-values mean a HORIZONTAL line y = constant — the equation takes the shared y, not an x",
    "why": "Both points have y = −2, so the line is y = −2.",
    "traps": [
      "A: x = 3 — a vertical line through the first x-value was written.",
      "C: x = −2 — the vertical-line form was used with the y-value.",
      "D: y = 3 — an x-value was placed in the y-equation."
    ]
  },
  {
    "sig": "parameter-that-makes-a-line-horizontal",
    "code": "SAAT-P.23",
    "unit": 3,
    "topic": "Linear functions & equations",
    "lvl": 2,
    "stem": "For what value of k is the graph of y = (k − 4)x + 7 a horizontal line?",
    "opts": [
      "0",
      "7",
      "4",
      "−4"
    ],
    "ans": 2,
    "trick": "a horizontal line has slope 0, so the whole coefficient of x must vanish — solve k − 4 = 0",
    "why": "k − 4 = 0, so k = 4.",
    "traps": [
      "A: 0 — k was set to 0 instead of making the coefficient 0.",
      "B: 7 — the intercept was reported.",
      "D: −4 — a sign slip gave −4."
    ]
  },
  {
    "sig": "distance-between-two-vertical-lines",
    "code": "SAAT-P.24",
    "unit": 3,
    "topic": "Linear functions & equations",
    "lvl": 1,
    "stem": "What is the distance between the parallel lines x = −3 and x = 5?",
    "opts": [
      "2",
      "4",
      "−8",
      "8"
    ],
    "ans": 3,
    "trick": "distance between parallel vertical lines is the DIFFERENCE of the x-values, taken as a positive number",
    "why": "|5 − (−3)| = 8.",
    "traps": [
      "A: 2 — the two values were added.",
      "B: 4 — the gap was halved.",
      "C: −8 — a negative distance was reported."
    ]
  },
  {
    "sig": "slope-of-a-parallel-line",
    "code": "SAAT-P.25",
    "unit": 3,
    "topic": "Linear functions & equations",
    "lvl": 1,
    "stem": "What is the slope of any line parallel to y = (3/5)x − 5?",
    "opts": [
      "3/5",
      "−3/5",
      "5/3",
      "−5/3"
    ],
    "ans": 0,
    "trick": "parallel lines share the SAME slope — reciprocals and negatives belong to perpendicular lines",
    "why": "Parallel lines have equal slopes, so the slope is 3/5.",
    "traps": [
      "B: −3/5 — only the sign was changed.",
      "C: 5/3 — the reciprocal was taken.",
      "D: −5/3 — the negative reciprocal (a perpendicular slope) was taken."
    ]
  },
  {
    "sig": "equation-from-a-slope-and-a-y-intercept",
    "code": "SAAT-P.26",
    "unit": 3,
    "topic": "Linear functions & equations",
    "lvl": 1,
    "stem": "Which equation has slope 4 and y-intercept −3?",
    "opts": [
      "y = −4x − 3",
      "y = 4x − 3",
      "y = −3x + 4",
      "y = 4x + 3"
    ],
    "ans": 1,
    "trick": "slope-intercept form is y = mx + b — m is the slope and b the intercept, each with its own sign",
    "why": "y = 4x + (−3) = 4x − 3.",
    "traps": [
      "A: y = −4x − 3 — the sign of the slope was changed.",
      "C: y = −3x + 4 — the slope and the intercept were swapped.",
      "D: y = 4x + 3 — the sign of the intercept was lost."
    ]
  },
  {
    "sig": "inequality-from-a-spending-limit",
    "code": "SAAT-P.27",
    "unit": 3,
    "topic": "Inequalities & their graphs",
    "lvl": 2,
    "stem": "Sara has SAR 60. A pen costs SAR 4 and a notebook costs SAR 7. If she buys x pens and y notebooks, which inequality shows every purchase she can afford?",
    "opts": [
      "4x + 7y < 60",
      "7x + 4y ≤ 60",
      "4x + 7y ≤ 60",
      "4x + 7y ≥ 60"
    ],
    "ans": 2,
    "trick": "'has SAR 60' means the total may equal 60 or be less — use ≤, with each price on its own item",
    "why": "Total cost 4x + 7y must not exceed 60.",
    "traps": [
      "A: 4x + 7y < 60 — the strict sign excludes spending exactly SAR 60.",
      "B: 7x + 4y ≤ 60 — the prices were attached to the wrong items.",
      "D: 4x + 7y ≥ 60 — the inequality sign is reversed, which would mean spending at least SAR 60."
    ]
  },
  {
    "sig": "negative-fractional-exponent",
    "code": "SAAT-P.28",
    "unit": 1,
    "topic": "Exponents & radicals",
    "lvl": 3,
    "stem": "Evaluate 16^(−3/4).",
    "opts": [
      "−8",
      "8",
      "−1/8",
      "1/8"
    ],
    "ans": 3,
    "trick": "a negative exponent means RECIPROCAL, never a negative number — and 3/4 means fourth root, then cube",
    "why": "16^(3/4) = 2³ = 8, so 16^(−3/4) = 1/8.",
    "traps": [
      "A: −8 — the negative exponent was turned into a negative value.",
      "B: 8 — the negative sign of the exponent was ignored.",
      "C: −1/8 — the reciprocal was taken but a negative sign was kept."
    ]
  },
  {
    "sig": "cube-root-of-a-negative-decimal",
    "code": "SAAT-P.29",
    "unit": 1,
    "topic": "Exponents & radicals",
    "lvl": 2,
    "stem": "Evaluate the cube root of −0.008.",
    "opts": [
      "−0.2",
      "−0.02",
      "0.2",
      "−2"
    ],
    "ans": 0,
    "trick": "an odd root of a negative number is negative, and 0.008 = 0.2³ — count decimal places in threes",
    "why": "(−0.2)³ = −0.008.",
    "traps": [
      "B: −0.02 — a decimal-place slip gave −0.02.",
      "C: 0.2 — the sign was lost.",
      "D: −2 — the magnitude of the root was slipped by a power of ten."
    ]
  },
  {
    "sig": "principal-square-root-of-a-negative-number",
    "code": "SAAT-P.30",
    "unit": 7,
    "topic": "Complex numbers",
    "lvl": 2,
    "stem": "What is the principal square root of −49?",
    "opts": [
      "49i",
      "7i",
      "−7i",
      "7"
    ],
    "ans": 1,
    "trick": "√(−a) = i√a for the principal root — the positive imaginary one, not 7 and not 49i",
    "why": "√(−49) = √49 · √(−1) = 7i.",
    "traps": [
      "A: 49i — the number was not square-rooted.",
      "C: −7i — this is also a square root of −49, but it is not the principal one.",
      "D: 7 — the number was treated as a real square root of 49."
    ]
  },
  {
    "sig": "pure-imaginary-solutions-of-a-quadratic",
    "code": "SAAT-P.31",
    "unit": 7,
    "topic": "Complex numbers",
    "lvl": 2,
    "stem": "Solve x² = −64 over the complex numbers.",
    "opts": [
      "x = ±32i",
      "No solution",
      "x = ±8i",
      "x = ±8"
    ],
    "ans": 2,
    "trick": "no REAL number squares to a negative, but over the complex numbers x = ±√64 · i",
    "why": "x = ±√(−64) = ±8i.",
    "traps": [
      "A: x = ±32i — 64 was divided by 2 before rooting.",
      "B: No solution — 'no real solutions' was reported as 'no solutions at all'.",
      "D: x = ±8 — real roots were assumed, but a real square cannot be negative."
    ]
  },
  {
    "sig": "product-of-a-complex-number-and-its-conjugate",
    "code": "SAAT-P.32",
    "unit": 7,
    "topic": "Complex numbers",
    "lvl": 2,
    "stem": "Find (5 + 2i)(5 − 2i).",
    "opts": [
      "21",
      "10",
      "25",
      "29"
    ],
    "ans": 3,
    "trick": "a number times its conjugate is a² + b² — the cross terms cancel and −b²i² becomes +b²",
    "why": "25 − 4i² = 25 + 4 = 29.",
    "traps": [
      "A: 21 — a² − b² was used, forgetting that i² = −1.",
      "B: 10 — 2a was taken as the product.",
      "C: 25 — only a² was kept."
    ]
  },
  {
    "sig": "complex-polar-form-converted-to-rectangular",
    "code": "SAAT-P.33",
    "unit": 7,
    "topic": "Complex numbers",
    "lvl": 2,
    "stem": "Write 2(cos 90° + i sin 90°) in rectangular form.",
    "opts": [
      "2i",
      "2",
      "−2i",
      "2 + 2i"
    ],
    "ans": 0,
    "trick": "evaluate cos 90° = 0 and sin 90° = 1 before multiplying by the modulus",
    "why": "2(0 + i) = 2i.",
    "traps": [
      "B: 2 — only the cosine term was kept.",
      "C: −2i — the sign of the sine term was lost.",
      "D: 2 + 2i — the modulus was added to both parts."
    ]
  },
  {
    "sig": "position-of-a-term-with-a-given-value",
    "code": "SAAT-P.34",
    "unit": 7,
    "topic": "Sequences & series",
    "lvl": 3,
    "stem": "In a sequence, aₙ = n² − 2n. Which term (position n) is equal to 15?",
    "opts": [
      "15",
      "5",
      "−3",
      "3"
    ],
    "ans": 1,
    "trick": "solve for n and then reject any root that is not a positive whole number — positions cannot be negative",
    "why": "n² − 2n − 15 = 0 gives n = 5 or n = −3; only n = 5 is a position.",
    "traps": [
      "A: 15 — the value 15 was reported as the position.",
      "C: −3 — the second root of the equation is not a valid position.",
      "D: 3 — this is the position whose value is 3, not 15."
    ]
  },
  {
    "sig": "ratio-from-two-block-sums",
    "code": "SAAT-P.35",
    "unit": 7,
    "topic": "Sequences & series",
    "lvl": 3,
    "stem": "In a geometric sequence the first three terms add up to 14 and the next three terms add up to 112. What is the common ratio?",
    "opts": [
      "4",
      "14",
      "2",
      "8"
    ],
    "ans": 2,
    "trick": "the second block is the first block times r³, so r³ = 112 ÷ 14 — then take the cube root",
    "why": "r³ = 8, so r = 2 (terms 2, 4, 8 then 16, 32, 64).",
    "traps": [
      "A: 4 — r² was reported instead of r.",
      "B: 14 — the first sum was reported.",
      "D: 8 — r³ = 8 was reported instead of r."
    ]
  },
  {
    "sig": "total-over-days-with-percentage-growth",
    "code": "SAAT-P.36",
    "unit": 7,
    "topic": "Sequences & series",
    "lvl": 3,
    "stem": "A page has 80 visitors on day 1. Each day the number of visitors is 50% more than the day before. How many visitors in total over the first 3 days?",
    "opts": [
      "360",
      "180",
      "440",
      "380"
    ],
    "ans": 3,
    "trick": "'50% more than the day before' multiplies by 1.5 EACH day — it compounds; it is not a fixed addition",
    "why": "80 + 120 + 180 = 380.",
    "traps": [
      "A: 360 — the 50% was added to the ORIGINAL 80 each day (linear growth).",
      "B: 180 — only day 3 was counted.",
      "C: 440 — a doubling slip was made on day 3."
    ]
  },
  {
    "sig": "next-term-when-each-term-is-the-sum-of-the-previous-two",
    "code": "SAAT-P.37",
    "unit": 7,
    "topic": "Sequences & series",
    "lvl": 1,
    "stem": "In the sequence 2, 3, 5, 8, 13, … each term is the sum of the two terms before it. What is the next term?",
    "opts": [
      "21",
      "18",
      "26",
      "20"
    ],
    "ans": 0,
    "trick": "test the rule on the earlier terms, then add the LAST TWO terms — not the last term plus a pattern of gaps",
    "why": "8 + 13 = 21.",
    "traps": [
      "B: 18 — the previous gap (5) was added again.",
      "C: 26 — the last term was doubled.",
      "D: 20 — an off-by-one slip."
    ]
  },
  {
    "sig": "sum-of-an-alternating-series",
    "code": "SAAT-P.38",
    "unit": 7,
    "topic": "Sequences & series",
    "lvl": 2,
    "stem": "Evaluate the sum of 5(−1)^(k−1) for k = 1 to 9.",
    "opts": [
      "45",
      "5",
      "0",
      "−5"
    ],
    "ans": 1,
    "trick": "count the terms — an ODD number of alternating terms leaves the first one uncancelled",
    "why": "5 − 5 + 5 − … + 5 has four cancelling pairs and one extra +5.",
    "traps": [
      "A: 45 — the signs were ignored.",
      "C: 0 — the terms were assumed to cancel in pairs, forgetting that 9 is odd.",
      "D: −5 — the first term was taken as negative."
    ]
  },
  {
    "sig": "unit-circle-y-coordinate-from-x",
    "code": "SAAT-P.39",
    "unit": 8,
    "topic": "Sine, cosine & tangent",
    "lvl": 2,
    "stem": "P(3/5, y) is a point on the unit circle in the first quadrant. What is y?",
    "opts": [
      "2/5",
      "16/25",
      "4/5",
      "−4/5"
    ],
    "ans": 2,
    "trick": "a point on the unit circle satisfies x² + y² = 1 — solve for y, then check the quadrant's sign",
    "why": "y² = 1 − 9/25 = 16/25, so y = 4/5.",
    "traps": [
      "A: 2/5 — y was found as 1 − x.",
      "B: 16/25 — y² was reported without taking the root.",
      "D: −4/5 — the sign of y is wrong for the first quadrant."
    ]
  },
  {
    "sig": "reference-angle-in-the-third-quadrant",
    "code": "SAAT-P.40",
    "unit": 8,
    "topic": "Degree & radian measure",
    "lvl": 1,
    "stem": "What is the reference angle of 230°?",
    "opts": [
      "130°",
      "40°",
      "310°",
      "50°"
    ],
    "ans": 3,
    "trick": "the reference angle is the acute angle to the NEAREST x-axis — in the third quadrant subtract 180°",
    "why": "230° − 180° = 50°.",
    "traps": [
      "A: 130° — 360° − 230° was used, which is the rule for the fourth quadrant.",
      "B: 40° — 270° − 230° was used.",
      "C: 310° — a coterminal-type slip, 360° − 50°."
    ]
  },
  {
    "sig": "inverse-tangent-of-negative-one",
    "code": "SAAT-P.41",
    "unit": 9,
    "topic": "Basic trigonometric equations",
    "lvl": 3,
    "stem": "Find tan⁻¹(−1), the principal value, in degrees.",
    "opts": [
      "−45°",
      "135°",
      "45°",
      "315°"
    ],
    "ans": 0,
    "trick": "the principal value of tan⁻¹ lies between −90° and 90° — a negative input gives a negative angle",
    "why": "tan(−45°) = −1 and −45° is in (−90°, 90°).",
    "traps": [
      "B: 135° — this has tan = −1 but is outside the principal range (−90°, 90°).",
      "C: 45° — the sign was dropped.",
      "D: 315° — this has tan = −1 but is outside the principal range."
    ]
  },
  {
    "sig": "square-of-a-sine-plus-cosine",
    "code": "SAAT-P.42",
    "unit": 9,
    "topic": "Trigonometric identities",
    "lvl": 3,
    "stem": "Which expression is equal to (sin θ + cos θ)² for every θ?",
    "opts": [
      "sin 2θ",
      "1 + sin 2θ",
      "1",
      "1 + sin θ cos θ"
    ],
    "ans": 1,
    "trick": "squaring a sum keeps the CROSS TERM 2 sin θ cos θ = sin 2θ — it does not vanish",
    "why": "sin²θ + 2 sinθ cosθ + cos²θ = 1 + sin 2θ.",
    "traps": [
      "A: sin 2θ — only the cross term was kept.",
      "C: 1 — the cross term was forgotten, leaving sin²θ + cos²θ only.",
      "D: 1 + sin θ cos θ — the cross term was halved."
    ]
  },
  {
    "sig": "tangent-equation-with-a-negative-value",
    "code": "SAAT-P.43",
    "unit": 9,
    "topic": "Basic trigonometric equations",
    "lvl": 2,
    "stem": "Solve tan θ = −1 for 0° ≤ θ < 180°.",
    "opts": [
      "315°",
      "225°",
      "135°",
      "45°"
    ],
    "ans": 2,
    "trick": "tan is negative in the second quadrant — within a half-turn the answer is 180° minus the reference angle",
    "why": "Reference angle 45°, second quadrant: 180° − 45° = 135°.",
    "traps": [
      "A: 315° — tan = −1 here, but it is outside the stated range.",
      "B: 225° — it is outside the range, and tan 225° = +1.",
      "D: 45° — the sign was ignored, giving tan = +1."
    ]
  },
  {
    "sig": "net-of-two-opposite-forces",
    "code": "SAAT-P.44",
    "unit": 9,
    "topic": "Vectors & their basic applications",
    "lvl": 1,
    "stem": "A body is pulled with a force of 9 N to the east and 6 N to the west. What is the net force?",
    "opts": [
      "15 N east",
      "3 N west",
      "6 N east",
      "3 N east"
    ],
    "ans": 3,
    "trick": "opposite vectors SUBTRACT, and the net points the way of the larger force",
    "why": "9 − 6 = 3 N, in the direction of the 9 N force: east.",
    "traps": [
      "A: 15 N east — the magnitudes were added although the forces oppose each other.",
      "B: 3 N west — the direction of the smaller force was used.",
      "C: 6 N east — only the smaller force was reported."
    ]
  },
  {
    "sig": "terminal-point-from-an-initial-point-and-a-vector",
    "code": "SAAT-P.45",
    "unit": 9,
    "topic": "Vectors & their basic applications",
    "lvl": 2,
    "stem": "A vector ⟨4, 5⟩ starts at the point (2, −3). Where does it end?",
    "opts": [
      "(6, 2)",
      "(−2, −8)",
      "(8, −15)",
      "(4, 5)"
    ],
    "ans": 0,
    "trick": "terminal point = initial point + components of the vector, coordinate by coordinate",
    "why": "(2 + 4, −3 + 5) = (6, 2).",
    "traps": [
      "B: (−2, −8) — the vector was subtracted from the start.",
      "C: (8, −15) — the components were multiplied by the coordinates.",
      "D: (4, 5) — the vector itself was given as the end point."
    ]
  },
  {
    "sig": "polar-equation-of-a-vertical-line",
    "code": "SAAT-P.46",
    "unit": 10,
    "topic": "Polar coordinates & equations",
    "lvl": 3,
    "stem": "Which Cartesian equation is the same as the polar equation r = 5 sec θ?",
    "opts": [
      "y = 5x",
      "x = 5",
      "y = 5",
      "x² + y² = 25"
    ],
    "ans": 1,
    "trick": "multiply both sides by cos θ: r cos θ = 5, and r cos θ is x — so the graph is a vertical line",
    "why": "r = 5/cos θ gives r cos θ = 5, i.e. x = 5.",
    "traps": [
      "A: y = 5x — sec θ was confused with tan θ.",
      "C: y = 5 — sec θ was confused with csc θ, giving a horizontal line.",
      "D: x² + y² = 25 — r = 5 (constant radius) was assumed."
    ]
  },
  {
    "sig": "reciprocal-function-from-its-asymptotes",
    "code": "SAAT-P.47",
    "unit": 3,
    "topic": "Rational functions",
    "lvl": 3,
    "stem": "A reciprocal function has a vertical asymptote x = 2 and a horizontal asymptote y = −4. Which equation could it be?",
    "opts": [
      "f(x) = 1/(x − 2) + 4",
      "f(x) = 1/(x + 2) + 4",
      "f(x) = 1/(x − 2) − 4",
      "f(x) = 1/(x + 2) − 4"
    ],
    "ans": 2,
    "trick": "f(x) = 1/(x − h) + k has x = h and y = k as asymptotes — the horizontal shift carries the OPPOSITE sign inside the bracket",
    "why": "x = 2 means the denominator is x − 2, and y = −4 means adding −4.",
    "traps": [
      "A: f(x) = 1/(x − 2) + 4 — the sign of the vertical shift is wrong, giving y = 4.",
      "B: f(x) = 1/(x + 2) + 4 — both signs are wrong.",
      "D: f(x) = 1/(x + 2) − 4 — the sign of the horizontal shift is wrong, giving a vertical asymptote at x = −2."
    ]
  },
  {
    "sig": "rational-function-with-no-horizontal-asymptote",
    "code": "SAAT-P.48",
    "unit": 3,
    "topic": "Rational functions",
    "lvl": 3,
    "stem": "Which function has NO horizontal asymptote?",
    "opts": [
      "(x + 1)/(x² − 3)",
      "5x/(x − 1)",
      "x/(x² + 1)",
      "(x² + 1)/(x − 3)"
    ],
    "ans": 3,
    "trick": "compare the degrees — a horizontal asymptote exists unless the NUMERATOR's degree is the larger one",
    "why": "Only (x² + 1)/(x − 3) has a numerator of higher degree than its denominator.",
    "traps": [
      "A: (x + 1)/(x² − 3) — the denominator has the higher degree, so y = 0 is an asymptote.",
      "B: 5x/(x − 1) — the degrees are equal, so y = (ratio of leading coefficients) is an asymptote.",
      "C: x/(x² + 1) — the denominator has the higher degree, so y = 0 is an asymptote."
    ]
  },
  {
    "sig": "expected-value-from-a-distribution-table",
    "code": "SAAT-P.49",
    "unit": 5,
    "topic": "Probability, sample spaces & counting principles",
    "lvl": 2,
    "stem": "A random variable X takes the values 0, 1, 2, 3 with probabilities 0.1, 0.3, 0.4, 0.2. What is E(X)?",
    "opts": [
      "1.7",
      "1.5",
      "1",
      "0.4"
    ],
    "ans": 0,
    "trick": "E(X) is the SUM of value × probability — not the plain mean of the values",
    "why": "0(0.1) + 1(0.3) + 2(0.4) + 3(0.2) = 1.7.",
    "traps": [
      "B: 1.5 — the plain average of the four values was used.",
      "C: 1 — the probabilities were added.",
      "D: 0.4 — the largest probability was reported."
    ]
  },
  {
    "sig": "zero-standard-deviation-means-equal-values",
    "code": "SAAT-P.50",
    "unit": 5,
    "topic": "Measures of dispersion & standard deviation",
    "lvl": 1,
    "stem": "If the standard deviation of a set of marks is zero, which data set could it be?",
    "opts": [
      "−1, 0, 1",
      "20, 20, 20",
      "19, 20, 21",
      "10, 20, 30"
    ],
    "ans": 1,
    "trick": "standard deviation measures SPREAD about the mean — it is zero only when every value is identical",
    "why": "Every deviation from the mean is 0 only for 20, 20, 20.",
    "traps": [
      "A: −1, 0, 1 — the mean is zero, which is unrelated to the spread.",
      "C: 19, 20, 21 — the values are close together, but not equal, so the deviation is not zero.",
      "D: 10, 20, 30 — the values are far apart."
    ]
  },
  {
    "sig": "data-set-with-the-smallest-spread",
    "code": "SAAT-P.51",
    "unit": 5,
    "topic": "Measures of dispersion & standard deviation",
    "lvl": 2,
    "stem": "Four sets of marks all have mean 20. Which set has the smallest standard deviation?",
    "opts": [
      "15, 20, 25",
      "12, 20, 28",
      "19, 20, 21",
      "18, 20, 22"
    ],
    "ans": 2,
    "trick": "with the same mean, the set whose values sit CLOSEST to it has the smallest standard deviation",
    "why": "The deviations are ±1 for 19, 20, 21 — smaller than in every other set.",
    "traps": [
      "A: 15, 20, 25 — this set is much more spread out.",
      "B: 12, 20, 28 — this set is the most spread out.",
      "D: 18, 20, 22 — this set is more spread out than the keyed one."
    ]
  },
  {
    "sig": "number-of-observations-above-one-standard-deviation",
    "code": "SAAT-P.52",
    "unit": 5,
    "topic": "Normal distribution",
    "lvl": 3,
    "stem": "Marks of 2000 students are normally distributed with mean 70 and standard deviation 8. About how many scored above 78?",
    "opts": [
      "640",
      "680",
      "1360",
      "320"
    ],
    "ans": 3,
    "trick": "78 is one standard deviation above the mean — only ONE tail (16%) lies above it, and then it must be applied to the 2000 students",
    "why": "(100% − 68%) ÷ 2 = 16%, and 16% of 2000 = 320.",
    "traps": [
      "A: 640 — both tails were counted.",
      "B: 680 — 34% (the band between the mean and 78) was used.",
      "C: 1360 — the 68% central band was used."
    ]
  },
  {
    "sig": "order-of-mean-median-and-mode",
    "code": "SAAT-P.53",
    "unit": 5,
    "topic": "Data representation & measures of centre",
    "lvl": 3,
    "stem": "For the data 2, 4, 4, 5, 10, which statement about the mean, median and mode is true?",
    "opts": [
      "Mean > median = mode",
      "Mean = median = mode",
      "Mode > median > mean",
      "Median > mean = mode"
    ],
    "ans": 0,
    "trick": "an unusually LARGE value pulls the mean above the median and mode — compute all three before comparing",
    "why": "Mean = 25 ÷ 5 = 5, median = 4, mode = 4, so mean > median = mode.",
    "traps": [
      "B: Mean = median = mode — the three measures are not all equal; the outlier 10 pulls the mean up.",
      "C: Mode > median > mean — the mode is not the largest of the three.",
      "D: Median > mean = mode — the median is not larger than the mean here."
    ]
  },
  {
    "sig": "limit-of-a-sequence-by-leading-coefficients",
    "code": "SAAT-P.54",
    "unit": 11,
    "topic": "Limits",
    "lvl": 2,
    "stem": "Find the limit as n → ∞ of (3n + 1)/(n + 4).",
    "opts": [
      "0",
      "3",
      "1/4",
      "4"
    ],
    "ans": 1,
    "trick": "for a ratio of equal-degree terms, the limit is the RATIO OF LEADING COEFFICIENTS — the constants stop mattering",
    "why": "Divide by n: (3 + 1/n)/(1 + 4/n) → 3/1 = 3.",
    "traps": [
      "A: 0 — the terms were assumed to shrink to 0.",
      "C: 1/4 — the constant terms 1 and 4 were divided.",
      "D: 4 — the denominator's constant was reported."
    ]
  },
  {
    "sig": "limit-that-grows-without-bound",
    "code": "SAAT-P.55",
    "unit": 11,
    "topic": "Limits",
    "lvl": 2,
    "stem": "Find the limit as x → 3 of 1/(x − 3)².",
    "opts": [
      "0",
      "1/9",
      "+∞",
      "−∞"
    ],
    "ans": 2,
    "trick": "a squared denominator approaching 0 gives HUGE POSITIVE values from both sides",
    "why": "Both one-sided values grow without bound, positively.",
    "traps": [
      "A: 0 — the denominator was treated as large rather than as approaching zero.",
      "B: 1/9 — x = 0 was substituted instead of x = 3.",
      "D: −∞ — the squared bracket is never negative, so the values cannot head to −∞."
    ]
  },
  {
    "sig": "coefficient-from-a-limit-at-infinity",
    "code": "SAAT-P.56",
    "unit": 11,
    "topic": "Limits",
    "lvl": 3,
    "stem": "If the limit as x → ∞ of (6x² − x)/(ax² + 5) equals 2, find a.",
    "opts": [
      "12",
      "2",
      "1/3",
      "3"
    ],
    "ans": 3,
    "trick": "equal degrees: the limit is 6/a, so set 6/a = 2 — don't multiply 6 by 2",
    "why": "6/a = 2 gives a = 3.",
    "traps": [
      "A: 12 — 6 and 2 were multiplied.",
      "B: 2 — the limit value was copied as a.",
      "C: 1/3 — the ratio was inverted, giving 2/6."
    ]
  },
  {
    "sig": "end-behaviour-of-an-odd-degree-polynomial",
    "code": "SAAT-P.57",
    "unit": 11,
    "topic": "Limits",
    "lvl": 3,
    "stem": "Find the limit as x → −∞ of (−2x³ + x²).",
    "opts": [
      "+∞",
      "−∞",
      "0",
      "−2"
    ],
    "ans": 0,
    "trick": "for x → −∞ the leading term decides; an ODD power turns negative into negative, and −2 × negative is positive",
    "why": "−2x³ is positive for large negative x and dominates x².",
    "traps": [
      "B: −∞ — the sign change of an odd power was missed.",
      "C: 0 — the polynomial was treated as bounded.",
      "D: −2 — the leading coefficient was reported."
    ]
  },
  {
    "sig": "directrix-from-a-vertical-parabola-equation",
    "code": "SAAT-P.58",
    "unit": 10,
    "topic": "Parabolas",
    "lvl": 2,
    "stem": "What is the directrix of (x − 1)² = 8(y + 2)?",
    "opts": [
      "y = 4",
      "y = −4",
      "y = 0",
      "x = −1"
    ],
    "ans": 1,
    "trick": "4p = 8 gives p = 2; the directrix sits p BELOW the vertex of an upward parabola and the focus sits p above",
    "why": "Vertex (1, −2), p = 2, so the directrix is y = −2 − 2 = −4.",
    "traps": [
      "A: y = 4 — the sign was reversed.",
      "C: y = 0 — this is the y-value of the focus, not the directrix.",
      "D: x = −1 — a vertical line was written for an upward-opening parabola."
    ]
  },
  {
    "sig": "focus-of-a-horizontal-parabola-at-the-origin",
    "code": "SAAT-P.59",
    "unit": 10,
    "topic": "Parabolas",
    "lvl": 2,
    "stem": "What is the focus of y² = 12x?",
    "opts": [
      "(6, 0)",
      "(0, 3)",
      "(3, 0)",
      "(12, 0)"
    ],
    "ans": 2,
    "trick": "match y² = 4px, so p = 12 ÷ 4 = 3 — the focus is (p, 0), not (4p, 0)",
    "why": "4p = 12 gives p = 3, so the focus is (3, 0).",
    "traps": [
      "A: (6, 0) — 2p was used.",
      "B: (0, 3) — the coordinates were swapped.",
      "D: (12, 0) — 4p was reported as p."
    ]
  },
  {
    "sig": "opening-direction-from-the-vertex-and-a-point",
    "code": "SAAT-P.60",
    "unit": 10,
    "topic": "Parabolas",
    "lvl": 2,
    "stem": "A parabola with vertex (0, 5) passes through (5, 8) and (−5, 8). In which direction does it open?",
    "opts": [
      "Downwards",
      "To the left",
      "To the right",
      "Upwards"
    ],
    "ans": 3,
    "trick": "the two symmetric points tell you the axis is vertical; they lie ABOVE the vertex, so it opens up",
    "why": "Points with y = 8 > 5 sit above the vertex of a parabola symmetric about x = 0.",
    "traps": [
      "A: Downwards — the points lie above the vertex, so it cannot open downwards.",
      "B: To the left — a horizontal axis would need points at different y-values on both sides of the vertex.",
      "C: To the right — the symmetric pair (±5, 8) shows the axis is the y-axis, not horizontal."
    ]
  },
  {
    "sig": "distance-between-the-foci-of-an-ellipse",
    "code": "SAAT-P.61",
    "unit": 10,
    "topic": "Ellipses",
    "lvl": 3,
    "stem": "What is the distance between the foci of x²/25 + y²/9 = 1?",
    "opts": [
      "8",
      "4",
      "10",
      "6"
    ],
    "ans": 0,
    "trick": "c² = a² − b² gives c, but the foci are 2c apart — don't stop at c",
    "why": "c = √(25 − 9) = 4, so the foci are 8 apart.",
    "traps": [
      "B: 4 — c was found but not doubled.",
      "C: 10 — the length of the major axis was given.",
      "D: 6 — the length of the minor axis was given."
    ]
  },
  {
    "sig": "transverse-axis-of-a-hyperbola",
    "code": "SAAT-P.62",
    "unit": 10,
    "topic": "Hyperbolas",
    "lvl": 3,
    "stem": "What is the equation of the transverse axis of (x + 1)²/9 − (y − 3)²/25 = 1?",
    "opts": [
      "x = 3",
      "y = 3",
      "x = −1",
      "y = −3"
    ],
    "ans": 1,
    "trick": "the positive term (here x) gives the direction of the transverse axis — it runs through the centre, so it is the HORIZONTAL line y = 3",
    "why": "The centre is (−1, 3) and the transverse axis is horizontal: y = 3.",
    "traps": [
      "A: x = 3 — the centre's y-value was used as an x-value.",
      "C: x = −1 — this is the conjugate axis.",
      "D: y = −3 — the sign of the centre's y-value was changed."
    ]
  },
  {
    "sig": "ellipse-from-the-sum-and-difference-of-its-axes",
    "code": "SAAT-P.63",
    "unit": 10,
    "topic": "Ellipses",
    "lvl": 4,
    "stem": "An ellipse centred at the origin has a horizontal major axis. The lengths of its major and minor axes add to 16 and differ by 4. What is its equation?",
    "opts": [
      "x²/100 + y²/36 = 1",
      "x²/10 + y²/6 = 1",
      "x²/25 + y²/9 = 1",
      "x²/9 + y²/25 = 1"
    ],
    "ans": 2,
    "trick": "axes are 2a and 2b — halve them FIRST, then square for the denominators, with a² under x for a horizontal major axis",
    "why": "Major = 10, minor = 6, so a = 5, b = 3 and the equation is x²/25 + y²/9 = 1.",
    "traps": [
      "A: x²/100 + y²/36 = 1 — the axis lengths 10 and 6 were squared instead of the semi-axes 5 and 3.",
      "B: x²/10 + y²/6 = 1 — the axis lengths were used as denominators with no squaring.",
      "D: x²/9 + y²/25 = 1 — the denominators were put under the wrong variables."
    ]
  },
  {
    "sig": "logarithm-of-a-reciprocal-power",
    "code": "SAAT-P.64",
    "unit": 6,
    "topic": "Logarithms & their properties",
    "lvl": 2,
    "stem": "Evaluate log₃(1/81).",
    "opts": [
      "4",
      "−1/4",
      "1/4",
      "−4"
    ],
    "ans": 3,
    "trick": "1/81 = 3⁻⁴, so the exponent is NEGATIVE four — a fraction below 1 gives a negative logarithm",
    "why": "3⁻⁴ = 1/81, so log₃(1/81) = −4.",
    "traps": [
      "A: 4 — the sign was lost.",
      "B: −1/4 — the answer was inverted.",
      "C: 1/4 — the answer was inverted and its sign lost."
    ]
  },
  {
    "sig": "zero-of-a-logarithmic-function",
    "code": "SAAT-P.65",
    "unit": 6,
    "topic": "Logarithmic functions",
    "lvl": 2,
    "stem": "Find the zero of f(x) = log₄(x + 1).",
    "opts": [
      "0",
      "1",
      "3",
      "−1"
    ],
    "ans": 0,
    "trick": "a logarithm is 0 when its ARGUMENT equals 1 — so set x + 1 = 1, not x = 1",
    "why": "log₄(1) = 0, so x + 1 = 1 and x = 0.",
    "traps": [
      "B: 1 — x was set to 1 instead of the argument being set to 1.",
      "C: 3 — the argument was set equal to the base, which gives log = 1.",
      "D: −1 — x = −1 makes the argument 0, which is outside the domain."
    ]
  },
  {
    "sig": "y-intercept-of-a-shifted-logarithm",
    "code": "SAAT-P.66",
    "unit": 6,
    "topic": "Logarithmic functions",
    "lvl": 2,
    "stem": "Find the y-intercept of y = log₂(x + 2) + 3.",
    "opts": [
      "2",
      "4",
      "3",
      "5"
    ],
    "ans": 1,
    "trick": "substitute x = 0 and evaluate the log exactly — log₂ 2 = 1, not 0 and not 2",
    "why": "y = log₂(2) + 3 = 1 + 3 = 4.",
    "traps": [
      "A: 2 — only the horizontal shift was reported.",
      "C: 3 — log₂ 2 was taken as 0.",
      "D: 5 — log₂ 2 was taken as 2."
    ]
  },
  {
    "sig": "sound-level-from-the-logarithmic-formula",
    "code": "SAAT-P.67",
    "unit": 6,
    "topic": "Applications of logarithms",
    "lvl": 3,
    "stem": "Sound level is L = 10 log(I/I₀) decibels. If I₀ = 10⁻¹² and I = 10⁻³, find L.",
    "opts": [
      "120 dB",
      "80 dB",
      "90 dB",
      "9 dB"
    ],
    "ans": 2,
    "trick": "divide first: 10⁻³ ÷ 10⁻¹² = 10⁹, so log = 9, then apply the factor 10",
    "why": "L = 10 × log(10⁹) = 90 dB.",
    "traps": [
      "A: 120 dB — only the exponent 12 was used.",
      "B: 80 dB — the exponents were subtracted with an arithmetic slip.",
      "D: 9 dB — the factor of 10 was forgotten."
    ]
  },
  {
    "sig": "logarithm-with-a-reciprocal-base-relation",
    "code": "SAAT-P.68",
    "unit": 6,
    "topic": "Logarithms & their properties",
    "lvl": 4,
    "stem": "If (1/b)^x = y with b > 0 and b ≠ 1, which expression equals log_b y?",
    "opts": [
      "x",
      "1/x",
      "−1/x",
      "−x"
    ],
    "ans": 3,
    "trick": "(1/b)^x = b^(−x), so the exponent on b is −x — a reciprocal base flips the sign",
    "why": "y = b^(−x), so log_b y = −x.",
    "traps": [
      "A: x — the reciprocal base was ignored, losing the sign.",
      "B: 1/x — x was inverted.",
      "C: −1/x — x was inverted and the sign changed."
    ]
  },
  {
    "sig": "order-of-a-difference-of-matrices",
    "code": "SAAT-P.69",
    "unit": 2,
    "topic": "Matrices",
    "lvl": 1,
    "stem": "A and B are both 3 × 5 matrices. What is the order of A − B?",
    "opts": [
      "3 × 5",
      "5 × 3",
      "3 × 3",
      "Not defined"
    ],
    "ans": 0,
    "trick": "addition and subtraction need EQUAL orders and keep that order — multiplication is the operation with the inner-dimension rule",
    "why": "Entry-by-entry subtraction of two 3 × 5 matrices is again 3 × 5.",
    "traps": [
      "B: 5 × 3 — the order was transposed.",
      "C: 3 × 3 — a square matrix was assumed.",
      "D: Not defined — subtraction was thought to be undefined, which is true only for matrices of different orders."
    ]
  },
  {
    "sig": "percentage-of-a-matrix",
    "code": "SAAT-P.70",
    "unit": 2,
    "topic": "Matrices",
    "lvl": 2,
    "stem": "Find 25% of the matrix [16  5  24].",
    "opts": [
      "[4  5  24]",
      "[4  1.25  6]",
      "[8  2.5  12]",
      "[64  20  96]"
    ],
    "ans": 1,
    "trick": "a percentage of a matrix is a scalar multiple — multiply EVERY entry by 0.25",
    "why": "0.25 × (16, 5, 24) = (4, 1.25, 6).",
    "traps": [
      "A: [4  5  24] — only the first entry was scaled.",
      "C: [8  2.5  12] — 50% (half) was taken.",
      "D: [64  20  96] — every entry was multiplied by 4."
    ]
  },
  {
    "sig": "two-planes-meet-in-a-line",
    "code": "SAAT-P.71",
    "unit": 4,
    "topic": "Points, lines & planes",
    "lvl": 2,
    "stem": "Two distinct planes that are not parallel intersect in:",
    "opts": [
      "A plane",
      "Exactly two points",
      "A line",
      "A single point"
    ],
    "ans": 2,
    "trick": "two non-parallel planes share a whole LINE — not a point, and never exactly two points",
    "why": "The common solutions of two independent plane equations form a one-dimensional set: a line.",
    "traps": [
      "A: A plane — a shared plane would make the two planes the same plane.",
      "B: Exactly two points — if two points are shared, the whole line through them is shared.",
      "D: A single point — two planes give a whole line of common points, not a single point."
    ]
  }
];
