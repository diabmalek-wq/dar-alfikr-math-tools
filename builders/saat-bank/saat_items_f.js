// PART F of the SAAT booklet — written from the eight official ETEC Tahsili
// sample papers in the project uploads.
//
// WHAT CROSSED OVER. The papers were read for two things only: which SKILL each
// question tests, and which TRICK its distractors are built to catch. Nothing
// else. Every stem below is newly worded in English, every number set is new,
// every option list is rebuilt, and every figure is DRAWN FROM SCRATCH in
// make_figs_saat_f.py in the department's own line style — no source figure is
// traced, redrawn or reproduced.
//
// WHY THIS PART EXISTS. The earlier parts were thin exactly where the real
// papers are thick: polar coordinates, complex numbers in polar form, vectors,
// matrices, and questions that hand the student a PICTURE rather than an
// expression. Sample 1 is almost entirely polar and complex; samples 4, 6, 7
// and 9 are full of labelled polygons, triangles and transversals; sample 5
// reads limits and areas off graphs. This part answers that.
//
// Every answer is re-derived independently in verify_saat_f.py.

module.exports = [
  // ============================================== POLAR COORDINATES
  {
    sig: "polar-equation-of-a-circle-from-a-graph",
    code: "SAAT-M-TRI.32", ses: 80, lvl: 4,
    stem: "The circle below passes through the pole and through the point marked on it. What is its polar equation?",
    fig: "f_polar_sin", figW: 1.75,
    opts: [
      { eq: "f_pc1" },
      { eq: "f_pc2" },
      { eq: "f_pc3" },
      { eq: "f_pc4" }
    ],
    ans: 0,
    trick: "a circle sitting ABOVE the pole on the y-axis is r = a sin θ, and a is the DIAMETER, not the radius — a circle to the right of the pole would be the cosine, and halving a is the other half of the same error",
    why: "r = 24 sin θ passes through the pole and reaches its greatest value 24 at θ = 90°, which is the point (0, 24).",
    traps: [
      "B: the cosine form, whose circle lies along the x-axis.",
      "C: the radius used in place of the diameter.",
      "D: both errors together.",
    ],
  },
  {
    sig: "which-ray-matches-a-cartesian-point",
    code: "SAAT-M-TRI.33", ses: 80, lvl: 3,
    stem: "On the polar grid below, which arrow ends at the point whose rectangular coordinates are given below?",
    stemEq: "j_raypoint",
    fig: "f_polar_rays", figW: 1.65,
    opts: [
      "t",
      "v",
      "u",
      "w"
    ],
    ans: 1,
    trick: "read the SIGNS first — a negative x with a positive y puts the point in the second quadrant, so only one arrow can be right before any angle is computed",
    why: "tan θ = 3 ÷ (−3√3) = −1/√3 with x < 0 and y > 0, giving θ = 150°.",
    traps: [
      "A: 330°, the reference angle measured the wrong way.",
      "C: 60°, the first-quadrant arrow, from ignoring the sign of x.",
      "D: 240°, from taking both coordinates negative.",
    ],
  },
  {
    sig: "polar-form-from-modulus-and-argument",
    code: "SAAT-M-ALG.114", ses: 80, lvl: 2,
    stem: "A complex number has modulus 3 and argument 30°. What is its polar form?",
    opts: [
      { eq: "f_pf3" },
      { eq: "f_pf4" },
      { eq: "f_pf1" },
      { eq: "f_pf2" }
    ],
    ans: 2,
    trick: "the modulus multiplies the WHOLE bracket and the cosine comes first — an answer with the sine in front, or with the modulus left off, is on the page for exactly that slip",
    why: "z = r(cos θ + i sin θ) = 3(cos 30° + i sin 30°).",
    traps: [
      "A: the modulus dropped.",
      "B: the argument used as the modulus.",
      "D: sine and cosine interchanged.",
    ],
  },
  {
    sig: "argument-of-a-complex-number",
    code: "SAAT-M-ALG.115", ses: 80, lvl: 3,
    stem: "What is the argument of the complex number below?",
    stemEq: "j_argz",
    opts: [
      { eq: "f_ar2" },
      { eq: "f_ar3" },
      { eq: "f_ar4" },
      { eq: "f_ar1" }
    ],
    ans: 3,
    trick: "the argument is arctan of the IMAGINARY part over the REAL part, in that order — inverting the fraction gives π/6 instead of π/3, and both are offered",
    why: "tan θ = √3 ÷ 1 = √3, so θ = π/3 in the first quadrant.",
    traps: [
      "A: the fraction inverted.",
      "B: the modulus's angle guessed as a right angle.",
      "C: the 45° answer of a number with equal parts.",
    ],
  },
  {
    sig: "product-of-two-complex-numbers-in-polar-form",
    code: "SAAT-M-ALG.116", ses: 80, lvl: 3,
    stem: "For z₁ = 4(cos 40° + i sin 40°) and z₂ = 3(cos 20° + i sin 20°), what is z₁z₂?",
    opts: [
      { eq: "f_pp1" },
      { eq: "f_pp2" },
      { eq: "f_pp3" },
      { eq: "f_pp4" }
    ],
    ans: 0,
    trick: "MULTIPLY the moduli and ADD the arguments — multiplying the angles as well is the error the paper is built on, and it produces an angle nobody can place",
    why: "4 × 3 = 12 and 40° + 20° = 60°, so the product is 12(cos 60° + i sin 60°).",
    traps: [
      "B: the arguments multiplied instead of added.",
      "C: the moduli added instead of multiplied.",
      "D: the arguments subtracted, which is the quotient rule.",
    ],
  },
  {
    sig: "quotient-of-two-complex-numbers-in-polar-form",
    code: "SAAT-M-ALG.117", ses: 80, lvl: 3,
    stem: "For z₁ = 10(cos 80° + i sin 80°) and z₂ = 5(cos 50° + i sin 50°), what is z₁ ÷ z₂?",
    opts: [
      { eq: "f_pq4" },
      { eq: "f_pq1" },
      { eq: "f_pq2" },
      { eq: "f_pq3" }
    ],
    ans: 1,
    trick: "DIVIDE the moduli and SUBTRACT the arguments, in that order — reversing the subtraction gives a negative angle, which is the option beside the answer",
    why: "10 ÷ 5 = 2 and 80° − 50° = 30°.",
    traps: [
      "A: the moduli subtracted instead of divided.",
      "C: the arguments subtracted the other way round.",
      "D: the arguments added, which is the product rule.",
    ],
  },
  {
    sig: "de-moivre-square-of-a-polar-number",
    code: "SAAT-M-ALG.118", ses: 80, lvl: 4,
    stem: "Evaluate [3(cos 30° + i sin 30°)]² and give the answer in rectangular form.",
    opts: [
      { eq: "f_dm3" },
      { eq: "f_dm4" },
      { eq: "f_dm1" },
      { eq: "f_dm2" }
    ],
    ans: 2,
    trick: "De Moivre raises the MODULUS to the power and MULTIPLIES the argument by it — the modulus is squared, not doubled, and the angle is doubled, not squared",
    why: "9(cos 60° + i sin 60°) = 9(1/2) + 9(√3/2)i = 4.5 + 4.5√3 i.",
    traps: [
      "A: the argument left unchanged.",
      "B: the real and imaginary parts interchanged.",
      "D: the modulus doubled instead of squared.",
    ],
  },
  {
    sig: "modulus-of-a-power-of-a-complex-number",
    code: "SAAT-M-ALG.119", ses: 80, lvl: 4,
    stem: "What is the absolute value of the power below?",
    stemEq: "j_modpow",
    opts: [
      "32",
      "64√3",
      "12",
      "64"
    ],
    ans: 3,
    trick: "take the modulus FIRST and then raise it — the modulus of a power is the power of the modulus, so no argument is needed at all and expanding the bracket is wasted work",
    why: "|1 + √3 i| = 2, and 2⁶ = 64.",
    traps: [
      "A: 2⁵ taken, one power short.",
      "B: the √3 carried into the modulus.",
      "C: the modulus multiplied by the exponent.",
    ],
  },
  {
    sig: "polar-equation-of-a-horizontal-line",
    code: "SAAT-M-TRI.34", ses: 80, lvl: 3,
    stem: "What is the polar form of the equation y = 6?",
    opts: [
      { eq: "f_pl1" },
      { eq: "f_pl2" },
      { eq: "f_pl3" },
      { eq: "f_pl4" }
    ],
    ans: 0,
    trick: "y = r sin θ, so a horizontal line becomes r = 6 ÷ sin θ, which is a COSECANT — the secant belongs to a vertical line, x = k, and the two are the whole question",
    why: "r sin θ = 6 gives r = 6 csc θ.",
    traps: [
      "B: the secant used, which converts x = 6.",
      "C: the constant halved.",
      "D: the reciprocal not taken.",
    ],
  },
  {
    sig: "cartesian-form-of-a-constant-radius",
    code: "SAAT-M-TRI.35", ses: 80, lvl: 2,
    stem: "What is the rectangular form of the polar equation r = 8?",
    opts: [
      { eq: "f_cr4" },
      { eq: "f_cr1" },
      { eq: "f_cr2" },
      { eq: "f_cr3" }
    ],
    ans: 1,
    trick: "r² = x² + y², so a constant r must be SQUARED when it crosses over — leaving 8 on the right gives a circle of the wrong size, and it is the option that looks most like the question",
    why: "r = 8 gives r² = 64, so x² + y² = 64.",
    traps: [
      "A: a difference of squares, which is a hyperbola.",
      "C: the 8 not squared.",
      "D: the squares dropped from the left.",
    ],
  },
  {
    sig: "cartesian-coordinates-from-a-negative-radius",
    code: "SAAT-M-TRI.36", ses: 80, lvl: 4,
    stem: "What are the rectangular coordinates of the polar point (−4, 60°)?",
    opts: [
      { eq: "f_nr3" },
      { eq: "f_nr4" },
      { eq: "f_nr1" },
      { eq: "f_nr2" }
    ],
    ans: 2,
    trick: "a NEGATIVE r sends the point through the pole to the opposite ray, so both coordinates change sign — the formula still works, provided the minus is carried into both products",
    why: "x = −4 cos 60° = −2 and y = −4 sin 60° = −2√3.",
    traps: [
      "A: sine and cosine interchanged.",
      "B: both errors together.",
      "D: the negative sign dropped.",
    ],
  },
  {
    sig: "distance-between-polar-points-at-the-pole",
    code: "SAAT-M-TRI.37", ses: 80, lvl: 3,
    stem: "What is the distance between the polar points P(0, 40°) and Q(3, 65°)?",
    opts: [
      "0",
      "40",
      "25",
      "3"
    ],
    ans: 3,
    trick: "a radius of ZERO puts the first point at the pole whatever its angle, so the distance is simply the other radius — reaching for the law of cosines works too, but the angles are a distraction",
    why: "P is the pole, so PQ = 3.",
    traps: [
      "A: the zero radius read as the distance.",
      "B: the first angle given.",
      "C: the difference of the angles given.",
    ],
  },
  {
    sig: "polar-distance-in-a-worded-setting",
    code: "SAAT-M-TRI.38", ses: 80, lvl: 4,
    stem: "A control tower at the pole tracks two drones at the polar positions (6, 90°) and (8, 30°). How far apart are the drones?",
    opts: [
      { eq: "f_pd1" },
      { eq: "f_pd2" },
      { eq: "f_pd3" },
      { eq: "f_pd4" }
    ],
    ans: 0,
    trick: "the law of cosines takes the DIFFERENCE of the two angles as the included angle — using either angle on its own, or their sum, is the error, and 60° here makes the cosine exactly one half",
    why: "√(36 + 64 − 2·6·8·cos 60°) = √(100 − 48) = √52 = 2√13.",
    traps: [
      "B: the angles added rather than subtracted.",
      "C: the two radii simply subtracted.",
      "D: the cosine term left out.",
    ],
  },

  // ================================================================ VECTORS
  {
    sig: "magnitude-and-direction-of-a-vector",
    code: "SAAT-M-TRI.39", ses: 79, lvl: 3,
    stem: "A vector has the component form below. What are its magnitude and its direction angle with the positive x-axis?",
    stemEq: "j_vec",
    opts: [
      "24 and 60°",
      "12 and 60°",
      "12 and 30°",
      "6√3 and 60°"
    ],
    ans: 1,
    trick: "the direction angle is arctan of the y component over the x component — inverting that fraction gives 30° instead of 60°, and both are on the page",
    why: "|v| = √(36 + 108) = 12 and tan θ = 6√3 ÷ 6 = √3, so θ = 60°.",
    traps: [
      "A: the components added before squaring.",
      "C: the tangent ratio inverted.",
      "D: one component given as the magnitude.",
    ],
  },
  {
    sig: "resultant-of-two-vectors",
    code: "SAAT-M-TRI.40", ses: 79, lvl: 2,
    stem: "For u = ⟨5, −2⟩ and v = ⟨−3, 7⟩, find 2u + v.",
    opts: [
      { eq: "f_rv3" },
      { eq: "f_rv4" },
      { eq: "f_rv1" },
      { eq: "f_rv2" }
    ],
    ans: 2,
    trick: "the scalar multiplies BOTH components of u before anything is added — doubling only the first component is the standard slip and it changes only one entry of the answer",
    why: "2⟨5, −2⟩ + ⟨−3, 7⟩ = ⟨10, −4⟩ + ⟨−3, 7⟩ = ⟨7, 3⟩.",
    traps: [
      "A: only the first component of u doubled.",
      "B: the vectors subtracted.",
      "D: v doubled instead of u.",
    ],
  },
  {
    sig: "unit-vector-in-space",
    code: "SAAT-M-TRI.41", ses: 79, lvl: 4,
    stem: "Find the unit vector in the direction of w = ⟨2, −3, 6⟩.",
    opts: [
      { eq: "f_uv32" },
      { eq: "f_uv33" },
      { eq: "f_uv34" },
      { eq: "f_uv31" }
    ],
    ans: 3,
    trick: "the magnitude in space is the root of the sum of THREE squares — here it comes out to a whole number, 7, which is the sign that the arithmetic is right",
    why: "|w| = √(4 + 9 + 36) = 7, so the unit vector is ⟨2/7, −3/7, 6/7⟩.",
    traps: [
      "A: divided by 49 rather than by its root.",
      "B: the z component left out of the magnitude.",
      "C: the components divided by the largest one.",
    ],
  },
  {
    sig: "angle-between-vectors-in-space",
    code: "SAAT-M-TRI.42", ses: 79, lvl: 4,
    stem: "What is the angle between a = ⟨1, 0, 1⟩ and b = ⟨0, 1, 1⟩?",
    opts: [
      "60°",
      "45°",
      "90°",
      "30°"
    ],
    ans: 0,
    trick: "the dot product over the product of the magnitudes gives the COSINE, not the angle — a cosine of one half is 60°, and reading it as 45° is the reflex of anyone who saw two ones",
    why: "a·b = 1 and |a||b| = 2, so cos θ = 1/2 and θ = 60°.",
    traps: [
      "B: the value 1/√2 assumed from the shape of the vectors.",
      "C: the vectors read as perpendicular because a zero appears in each.",
      "D: the arcsine taken instead of the arccosine.",
    ],
  },

  // =============================================================== MATRICES
  {
    sig: "entry-of-a-matrix-combination",
    code: "SAAT-M-ALG.120", ses: 10, lvl: 3,
    stem: "For the matrices below, what is the entry in row 1, column 2 of A − 2B?",
    stemEq: "f_mc",
    opts: [
      "11",
      "−7",
      "7",
      "−1"
    ],
    ans: 1,
    trick: "row FIRST, column second — and the 2 multiplies the entry of B before the subtraction, not after; computing the whole matrix wastes time when one entry is asked for",
    why: "A₁₂ − 2B₁₂ = 3 − 2(5) = −7.",
    traps: [
      "A: the entry at row 2, column 1 given.",
      "C: the subtraction taken the other way round.",
      "D: the scalar applied after subtracting.",
    ],
  },
  {
    sig: "determinant-equation-for-a-parameter",
    code: "SAAT-M-ALG.121", ses: 10, lvl: 4,
    stem: "For which value of k is the determinant below equal to 26?",
    stemEq: "f_dk",
    opts: [
      "5",
      "6.5",
      "8",
      "−8"
    ],
    ans: 2,
    trick: "the determinant is ad MINUS bc, and bc here is a product of two negatives, so the minus in the rule meets a positive product — dropping either sign gives an option on this page",
    why: "4k − (−3)(−2) = 4k − 6 = 26 gives k = 8.",
    traps: [
      "A: bc added instead of subtracted, giving 4k + 6 = 26.",
      "B: the target simply divided by 4.",
      "D: the sign of the answer reversed.",
    ],
  },
  {
    sig: "matrix-equation-for-an-entry",
    code: "SAAT-M-ALG.122", ses: 10, lvl: 4,
    stem: "If 3X − B equals the matrix shown, and B is as given, what is the entry in row 2, column 1 of X?",
    stemEq: "f_me",
    opts: [
      "12",
      "2",
      "−4",
      "4"
    ],
    ans: 3,
    trick: "undo the operations in REVERSE order — add B back first, then divide by 3; dividing before adding leaves a third of B in the answer",
    why: "3X₂₁ − 5 = 7 gives 3X₂₁ = 12, so X₂₁ = 4.",
    traps: [
      "A: the division by 3 not carried out.",
      "B: B subtracted again instead of added.",
      "C: the sign lost.",
    ],
  },
  {
    sig: "matrix-times-a-column-vector",
    code: "SAAT-M-ALG.123", ses: 10, lvl: 3,
    stem: "Find the product below.",
    stemEq: "f_mv",
    opts: [
      { eq: "f_mv1" },
      { eq: "f_mv2" },
      { eq: "f_mv3" },
      { eq: "f_mv4" }
    ],
    ans: 0,
    trick: "a 2 × 2 times a 2 × 1 gives a 2 × 1 — the answer is a COLUMN, and each entry is one row of the matrix against the whole column, never entry by entry",
    why: "⟨2·3 + (−1)·4, 5·3 + 2·4⟩ = ⟨2, 23⟩ as a column.",
    traps: [
      "B: the entries multiplied in place.",
      "C: the rows and columns interchanged.",
      "D: the two products added into a single number.",
    ],
  },

  // ============================================ GEOMETRY, FROM THE FIGURE
  {
    sig: "pentagon-two-unknown-angles",
    code: "SAAT-M-GEO.71", ses: 32, lvl: 4,
    stem: "In the pentagon below, what is the value of x + y?",
    fig: "f_pent_angles", figW: 1.75,
    opts: [
      "250",
      "215",
      "430",
      "107.5"
    ],
    ans: 1,
    trick: "the five angles add to (5 − 2) × 180 = 540, and the two unknowns each appear TWICE — so what the subtraction leaves is 2x + 2y, and the answer wanted is half of it",
    why: "540 − 110 = 430 = 2(x + y), so x + y = 215.",
    traps: [
      "A: 360 used as the angle sum.",
      "C: 2x + 2y reported instead of x + y.",
      "D: the total halved twice.",
    ],
  },
  {
    sig: "exterior-angle-of-a-regular-pentagon",
    code: "SAAT-M-GEO.72", ses: 32, lvl: 3,
    stem: "The figure below shows a regular pentagon with one side extended. What is θ?",
    fig: "f_pent_ext", figW: 1.75,
    opts: [
      "36°",
      "60°",
      "72°",
      "108°"
    ],
    ans: 2,
    trick: "an exterior angle of a regular n-gon is 360 ÷ n, whatever n is — the interior angle is its supplement and is always the option beside it",
    why: "360 ÷ 5 = 72.",
    traps: [
      "A: the exterior angle halved.",
      "B: 360 ÷ 6, a hexagon's exterior angle.",
      "D: the interior angle given.",
    ],
  },
  {
    sig: "fourth-exterior-angle-of-a-quadrilateral",
    code: "SAAT-M-GEO.73", ses: 32, lvl: 3,
    stem: "In the figure below, every side of the quadrilateral has been extended. What is the measure of ∠1?",
    fig: "f_quad_ext", figW: 2.0,
    opts: [
      "100°",
      "180°",
      "260°",
      "80°"
    ],
    ans: 3,
    trick: "the exterior angles of ANY convex polygon add to 360°, whatever the number of sides — reaching for (n − 2) × 180 gives 360 for a quadrilateral too, which is why this one is so easy to get right for the wrong reason and wrong on a pentagon",
    why: "360 − (95 + 85 + 100) = 80.",
    traps: [
      "A: the supplement of the answer given.",
      "B: 540 used as the total.",
      "C: the three given angles simply added.",
    ],
  },
  {
    sig: "order-the-angles-by-side-length",
    code: "SAAT-M-GEO.74", ses: 29, lvl: 3,
    stem: "In the triangle below, list the angles from smallest to largest.",
    fig: "f_tri_order", figW: 1.85,
    opts: [
      "Z, X, Y",
      "Y, X, Z",
      "X, Y, Z",
      "Z, Y, X"
    ],
    ans: 0,
    trick: "each angle is opposite the side NOT touching it — the smallest angle faces the shortest side, so the ordering of the angles copies the ordering of the opposite sides, not of the sides beside them",
    why: "Side 5 is opposite Z, side 7 opposite X and side 9 opposite Y, so Z < X < Y.",
    traps: [
      "B: the order reversed.",
      "C: the angles listed in the order the letters appear.",
      "D: two of the three correspondences swapped.",
    ],
  },
  {
    sig: "isosceles-triangle-solve-for-a-side",
    code: "SAAT-M-GEO.75", ses: 29, lvl: 3,
    stem: "The two marked sides of the triangle below are congruent. What is the length of each of them?",
    fig: "f_tri_iso", figW: 1.85,
    opts: [
      "7",
      "11",
      "4",
      "22"
    ],
    ans: 1,
    trick: "solve the equation the tick marks give you, then SUBSTITUTE — the value of x is not a length, and it is always offered as though it were",
    why: "2x + 3 = 5x − 9 gives x = 4, and 2(4) + 3 = 11.",
    traps: [
      "A: the difference of the two constants taken.",
      "C: the value of x reported as the length.",
      "D: the two equal sides added.",
    ],
  },
  {
    sig: "centroid-vertex-piece-from-a-figure",
    code: "SAAT-M-GEO.76", ses: 29, lvl: 3,
    stem: "In the triangle below the three medians meet at G, and the piece of one median from G to the opposite side measures 6. How long is that whole median?",
    fig: "f_tri_median", figW: 2.0,
    opts: [
      "9",
      "3",
      "18",
      "12"
    ],
    ans: 2,
    trick: "the centroid cuts a median into pieces of 2 and 1 parts, so the SHORT piece is one THIRD of the whole — the answer is three times it, not twice",
    why: "The short piece is one third of the median, so the median is 3 × 6 = 18.",
    traps: [
      "A: the ratio applied as 3 : 2.",
      "B: the short piece halved.",
      "D: the long piece given instead of the whole median.",
    ],
  },
  {
    sig: "parallelogram-diagonal-halves-from-a-figure",
    code: "SAAT-M-GEO.77", ses: 32, lvl: 3,
    stem: "In the parallelogram below the diagonals meet at E. What is the length of the whole diagonal AC?",
    fig: "f_par_diag", figW: 2.05,
    opts: [
      "11",
      "5",
      "44",
      "22"
    ],
    ans: 3,
    trick: "the diagonals of a parallelogram BISECT each other, so AE and EC are equal — solving gives one half, and the diagonal asked for is twice it",
    why: "3x − 4 = x + 6 gives x = 5, so AE = 11 and AC = 22.",
    traps: [
      "A: the half-diagonal given.",
      "B: the value of x reported as a length.",
      "C: the diagonal doubled a second time.",
    ],
  },
  {
    sig: "rhombus-half-diagonal-from-a-figure",
    code: "SAAT-M-GEO.78", ses: 32, lvl: 4,
    stem: "In the rhombus below the diagonals meet at E. Given the side and the half-diagonal marked, what is the length of the whole diagonal AC?",
    fig: "f_rho_diag", figW: 2.05,
    opts: [
      "24",
      "12",
      "18",
      "26"
    ],
    ans: 0,
    trick: "the diagonals of a rhombus are PERPENDICULAR, so half of each diagonal and a side make a right triangle — the side is the hypotenuse, and the answer is twice the leg you find, not the leg itself",
    why: "EA = √(13² − 5²) = 12, so AC = 24.",
    traps: [
      "B: the half-diagonal given instead of the whole.",
      "C: the two given lengths added and halved.",
      "D: the two diagonals confused, giving twice the side.",
    ],
  },
  {
    sig: "trapezoid-midsegment-from-a-figure",
    code: "SAAT-M-GEO.79", ses: 32, lvl: 3,
    stem: "In the trapezoid below the drawn segment joins the midpoints of the two legs. What is x?",
    fig: "f_trap_mid", figW: 2.1,
    opts: [
      "5",
      "6",
      "8.5",
      "12"
    ],
    ans: 1,
    trick: "the midsegment is HALF THE SUM of the two parallel sides, so the two bases add to twice it — setting the midsegment equal to one base is the error the paper wants",
    why: "12 + (4x + 2) = 2(19) = 38 gives 4x = 24, so x = 6.",
    traps: [
      "A: the 2 not subtracted before dividing.",
      "C: the midsegment set equal to the unknown base.",
      "D: the two given numbers averaged and reported as x.",
    ],
  },
  {
    sig: "alternate-interior-angles-solve",
    code: "SAAT-M-GEO.80", ses: 28, lvl: 3,
    stem: "In the figure below the two horizontal lines are parallel. What is the value of x?",
    fig: "f_par_alt", figW: 2.05,
    opts: [
      "70",
      "14",
      "20",
      "25"
    ],
    ans: 2,
    trick: "the two marked angles are ALTERNATE INTERIOR, so they are EQUAL — setting them to add to 180 is what the co-interior pair would need, and it gives a different, plausible x",
    why: "3x + 10 = 5x − 30 gives 2x = 40, so x = 20.",
    traps: [
      "A: the angle itself reported instead of x.",
      "B: the constants added rather than subtracted.",
      "D: the two expressions set to add to 180.",
    ],
  },
  {
    sig: "co-interior-angles-solve",
    code: "SAAT-M-GEO.81", ses: 28, lvl: 3,
    stem: "In the figure below the two horizontal lines are parallel. What is the value of x?",
    fig: "f_par_co", figW: 2.05,
    opts: [
      "30",
      "80",
      "20",
      "40"
    ],
    ans: 3,
    trick: "these two are on the SAME side of the transversal and between the parallels, so they are SUPPLEMENTARY, not equal — the arc in the figure is what tells you which pair you have",
    why: "2x + (4x − 60) = 180 gives 6x = 240, so x = 40.",
    traps: [
      "A: the two expressions set equal to each other.",
      "B: the angle 2x reported instead of x.",
      "C: 120 used as the total instead of 180.",
    ],
  },

  // ================================================ GRAPHS, FROM THE FIGURE
  {
    sig: "domain-from-a-graph-with-a-hole",
    code: "SAAT-M-ALG.124", ses: 20, lvl: 4,
    stem: "The graph below begins at the solid dot and has an open circle at one point. What is its domain?",
    fig: "f_gr_domain", figW: 1.9,
    opts: [
      { eq: "f_gd1" },
      { eq: "f_gd2" },
      { eq: "f_gd3" },
      { eq: "f_gd4" }
    ],
    ans: 0,
    trick: "a SOLID dot is included and an OPEN circle is not, so the domain is a union with one value taken out — reading the open circle's y-value instead of its x-value is the other error",
    why: "The graph runs from x = −4 inclusive to x = 4, with x = 2 removed.",
    traps: [
      "B: the open circle included.",
      "C: the left endpoint excluded.",
      "D: the range given instead of the domain.",
    ],
  },
  {
    sig: "even-or-odd-from-a-graph",
    code: "SAAT-M-ALG.125", ses: 22, lvl: 2,
    stem: "Is the function whose graph is shown below even, odd, or neither?",
    fig: "f_gr_even", figW: 1.8,
    opts: [
      "Even, because it is symmetric about the x-axis",
      "Even, because it is symmetric about the y-axis",
      "Odd, because it is symmetric about the origin",
      "Neither"
    ],
    ans: 1,
    trick: "EVEN is symmetry in the y-AXIS and ODD is symmetry about the ORIGIN — symmetry about the x-axis would mean the graph is not a function at all, which is why that option can be struck out on sight",
    why: "The curve to the left of the y-axis is the mirror image of the curve to the right.",
    traps: [
      "A: a graph symmetric in the x-axis fails the vertical line test.",
      "C: origin symmetry would send the left branch downwards.",
      "D: the graph is plainly symmetric.",
    ],
  },
  {
    sig: "interval-of-decrease-from-a-graph",
    code: "SAAT-M-ALG.126", ses: 22, lvl: 3,
    stem: "On which interval is the function graphed below decreasing?",
    fig: "f_gr_incdec", figW: 1.8,
    opts: [
      { eq: "f_id3" },
      { eq: "f_id4" },
      { eq: "f_id1" },
      { eq: "f_id2" }
    ],
    ans: 2,
    trick: "decreasing means the curve FALLS as you read left to right, and the interval runs between the turning points — it is described by x values, never by the y values the curve passes through",
    why: "The curve rises to a maximum near x = −2, falls to a minimum near x = 2, then rises again.",
    traps: [
      "A: the y values of the two turning points given.",
      "B: only half of the falling stretch.",
      "D: the interval where the curve rises.",
    ],
  },
  {
    sig: "asymptotes-from-a-graph",
    code: "SAAT-M-CAL.43", ses: 93, lvl: 3,
    stem: "The dashed lines on the graph below are its asymptotes. What are they?",
    fig: "f_gr_asym", figW: 1.85,
    opts: [
      "x = 1 and y = 2",
      "x = 2 and y = 0",
      "x = −2 and y = 1",
      "x = 2 and y = 1"
    ],
    ans: 3,
    trick: "the VERTICAL asymptote is an x-equation and the HORIZONTAL one is a y-equation — writing them the other way round is the standard slip, and both versions are on the page",
    why: "The curve runs away at x = 2 and levels off at height 1.",
    traps: [
      "A: the two equations interchanged.",
      "B: the horizontal asymptote read as the axis.",
      "C: the sign of the vertical asymptote reversed.",
    ],
  },
  {
    sig: "limit-does-not-exist-from-a-graph",
    code: "SAAT-M-CAL.44", ses: 91, lvl: 3,
    stem: "From the graph below, what is the limit of the function as x approaches 0?",
    fig: "f_gr_dne", figW: 1.85,
    opts: [
      "It does not exist",
      "+∞",
      "0",
      "−∞"
    ],
    ans: 0,
    trick: "a two-sided limit needs the two one-sided limits to AGREE — here one branch runs up and the other runs down, so reading only the branch nearest the pencil gives a confident wrong answer",
    why: "The left branch falls without bound and the right branch rises without bound, so the two one-sided limits differ.",
    traps: [
      "B: only the right branch read.",
      "C: the y-intercept read off instead.",
      "D: only the left branch read.",
    ],
  },
  {
    sig: "area-under-a-parabola-from-a-graph",
    code: "SAAT-M-CAL.45", ses: 115, lvl: 4,
    stem: "What is the area of the shaded region in the graph below, between the curve y = 4 − x², the y-axis and the line x = 2?",
    opts: [
      { eq: "f_ar4a" },
      { eq: "f_ar1a" },
      { eq: "f_ar2a" },
      { eq: "f_ar3a" }
    ],
    fig: "f_gr_area", figW: 1.85,
    ans: 1,
    trick: "only HALF the arch is shaded, so the limits run from 0 to 2 and not from −2 to 2 — integrating across the whole arch doubles the answer, and that doubled value is offered",
    why: "∫₀² (4 − x²) dx = 8 − 8/3 = 16/3.",
    traps: [
      "A: the rectangle 2 × 4 given instead.",
      "C: the whole arch integrated.",
      "D: the antiderivative not divided by 3.",
    ],
  },
  {
    sig: "riemann-estimate-from-a-graph",
    code: "SAAT-M-CAL.46", ses: 115, lvl: 4,
    stem: "The four rectangles drawn under the curve below each have width 0.5 and take their height from the curve at their LEFT edge. What is the area they give?",
    fig: "f_gr_riemann", figW: 1.85,
    opts: [
      "12.5",
      "16/3",
      "6.25",
      "5.25"
    ],
    ans: 2,
    trick: "multiply EVERY height by the common width once — adding the four heights and forgetting the width is the error, and so is reporting the exact area instead of the estimate the rectangles give",
    why: "0.5(4 + 3.75 + 3 + 1.75) = 0.5(12.5) = 6.25.",
    traps: [
      "A: the heights added with no width applied.",
      "B: the exact area given instead of the estimate.",
      "D: the first rectangle left out.",
    ],
  },

  // =========================================================== LOGIC
  {
    sig: "conditional-from-a-venn-diagram",
    code: "SAAT-M-ALG.127", unit: 0, topic: "Statements, truth values & reasoning", lvl: 3,
    stem: "Which statement does the diagram below assert?",
    fig: "f_venn", figW: 1.9,
    opts: [
      "If a figure is a rectangle, then it is a square",
      "If a figure is not a square, then it is not a rectangle",
      "A figure is a square if and only if it is a rectangle",
      "If a figure is a square, then it is a rectangle"
    ],
    ans: 3,
    trick: "the INNER set is the hypothesis and the OUTER set is the conclusion — the picture reads inwards to outwards, and the reverse reading is exactly the converse",
    why: "Every member of the inner set lies inside the outer one.",
    traps: [
      "A: the converse, which the picture denies.",
      "B: the inverse.",
      "C: the biconditional, which would need the two ovals to coincide.",
    ],
  },
  {
    sig: "inverse-of-a-negated-conditional",
    code: "SAAT-M-ALG.128", unit: 0, topic: "Statements, truth values & reasoning", lvl: 4,
    stem: "What is the inverse of the statement ~p → q?",
    opts: [
      "p → ~q",
      "~q → p",
      "q → ~p",
      "~p → ~q"
    ],
    ans: 0,
    trick: "the inverse negates BOTH parts and keeps the order — negating a part that is ALREADY negated returns it to p, which is the step that separates this from the contrapositive",
    why: "Negating ~p gives p and negating q gives ~q, with the order unchanged.",
    traps: [
      "B: the contrapositive, which swaps as well as negates.",
      "C: the converse with one negation.",
      "D: only the conclusion negated.",
    ],
  },
  {
    sig: "compound-truth-value-when-both-are-false",
    code: "SAAT-M-ALG.129", unit: 0, topic: "Statements, truth values & reasoning", lvl: 4,
    stem: "p and q are both false. Which compound statement below is TRUE?",
    opts: [
      "~p → q",
      "p → q",
      "p ∧ q",
      "p ∨ q"
    ],
    ans: 1,
    trick: "a conditional with a FALSE hypothesis is true whatever the conclusion does — but negating the hypothesis makes it true, and the conditional then fails, which is the option placed last",
    why: "p is false, so p → q is vacuously true; ~p is true and q is false, so ~p → q is false.",
    traps: [
      "A: a true hypothesis with a false conclusion.",
      "C: a conjunction of two falses is false.",
      "D: a disjunction of two falses is false.",
    ],
  },
  {
    sig: "congruent-complements",
    code: "SAAT-M-GEO.82", ses: 28, lvl: 2,
    stem: "Angle A and angle B are both complementary to angle C. What follows?",
    opts: [
      "Angle A is twice angle B",
      "Nothing follows without the measure of angle C",
      "Angle A is congruent to angle B",
      "Angle A and angle B are supplementary"
    ],
    ans: 2,
    trick: "both angles equal 90° minus the SAME angle, so they must be equal — the corresponding theorem for supplements uses 180°, and mixing the two is the whole trap",
    why: "A = 90 − C and B = 90 − C, so A = B.",
    traps: [
      "A: no such relation follows.",
      "B: the measure of C cancels and is never needed.",
      "D: the supplementary version of the theorem.",
    ],
  },

  // ======================================================== LOGARITHMS
  {
    sig: "solve-for-the-base-of-a-logarithm",
    code: "SAAT-M-ALG.130", ses: 51, lvl: 3,
    stem: "Solve log_x 49 = 2 for x.",
    opts: [
      "49",
      "2",
      "2401",
      "7"
    ],
    ans: 3,
    trick: "the unknown is the BASE, so the exponential form is x² = 49 and the answer is a square ROOT — solving for the argument instead returns the number already in the question",
    why: "x² = 49 with x > 0 gives x = 7.",
    traps: [
      "A: the argument returned as the base.",
      "B: the logarithm's value returned.",
      "C: 49 squared.",
    ],
  },
  {
    sig: "log-equation-with-a-squared-argument",
    code: "SAAT-M-ALG.131", ses: 51, lvl: 4,
    stem: "Solve log₃(x²) = 4.",
    opts: [
      { eq: "f_ls1" },
      { eq: "f_ls2" },
      { eq: "f_ls3" },
      { eq: "f_ls4" }
    ],
    ans: 0,
    trick: "x² = 81 has TWO solutions — a squared argument is positive for both signs, so neither is extraneous here, and giving only the positive one is half an answer",
    why: "x² = 3⁴ = 81, so x = ±9.",
    traps: [
      "B: only the positive root kept.",
      "C: the square root of 4 taken.",
      "D: 81 given without taking the root.",
    ],
  },
  {
    sig: "range-of-a-logarithmic-function",
    code: "SAAT-M-ALG.132", ses: 49, lvl: 2,
    stem: "What is the range of y = log₅ x?",
    opts: [
      "All real numbers greater than 5",
      "All real numbers",
      "All positive real numbers",
      "All real numbers except 0"
    ],
    ans: 1,
    trick: "it is the DOMAIN of a logarithm that is restricted to positives, not its range — the two are swapped so often that the domain is always offered as the answer",
    why: "log₅ x takes every real value as x runs over the positive reals.",
    traps: [
      "A: the base mistaken for a bound.",
      "C: the domain given instead of the range.",
      "D: no value is excluded from the range.",
    ],
  },
  {
    sig: "vertical-asymptote-of-a-shifted-log",
    code: "SAAT-M-ALG.133", ses: 49, lvl: 3,
    stem: "What is the vertical asymptote of y = 4 log₂(x − 3)?",
    opts: [
      "x = 4",
      "y = 3",
      "x = 3",
      "x = −3"
    ],
    ans: 2,
    trick: "the asymptote sits where the ARGUMENT is zero, so its sign is the opposite of the one written — the 4 in front stretches the curve and moves nothing",
    why: "x − 3 = 0 gives x = 3.",
    traps: [
      "A: the stretch factor read as the shift.",
      "B: a horizontal line given for a vertical asymptote.",
      "D: the sign of the shift not reversed.",
    ],
  },
  {
    sig: "log-of-a-radical-of-the-base",
    code: "SAAT-M-ALG.134", ses: 50, lvl: 3,
    stem: "Evaluate the expression below.",
    stemEq: "f_lr",
    opts: [
      { eq: "f_lr2" },
      { eq: "f_lr3" },
      { eq: "f_lr4" },
      { eq: "f_lr1" }
    ],
    ans: 3,
    trick: "a square root is the power one HALF, so the exponent inside is halved — the whole question is whether you convert the radical to a power before applying the rule",
    why: "log₂ √(2⁶) = log₂ 2³ = 3.",
    traps: [
      "A: the half not applied.",
      "B: the reciprocal of the answer taken.",
      "C: the sign reversed.",
    ],
  },
  {
    sig: "sum-of-logs-with-a-rejected-root",
    code: "SAAT-M-ALG.135", ses: 51, lvl: 4,
    stem: "Solve log₄ x + log₄(x − 6) = 2.",
    opts: [
      "8",
      "−2",
      "8 and −2",
      "10"
    ],
    ans: 0,
    trick: "combine the two logarithms into one, solve the QUADRATIC, and then throw away any root that makes an argument zero or negative — the rejected root is always on the page",
    why: "x(x − 6) = 16 gives x² − 6x − 16 = 0, so x = 8 or x = −2; only x = 8 keeps both arguments positive.",
    traps: [
      "B: the rejected root kept.",
      "C: both roots kept, though one is outside the domain.",
      "D: the arguments added rather than multiplied.",
    ],
  },

  // ============================================ COUNTING AND STATISTICS
  {
    sig: "objects-into-boxes-counting",
    code: "SAAT-M-STA.20", ses: 43, lvl: 3,
    stem: "Each of 4 different letters is posted into one of 3 postboxes. In how many ways can this be done?",
    opts: [
      "7",
      "81",
      "64",
      "12"
    ],
    ans: 1,
    trick: "each LETTER makes an independent choice among the boxes, so the count is (boxes) to the power (letters) — swapping the base and the exponent gives the option beside it",
    why: "3⁴ = 81.",
    traps: [
      "A: the two numbers added.",
      "C: base and exponent swapped.",
      "D: the two numbers multiplied.",
    ],
  },
  {
    sig: "permutation-equation-solve",
    code: "SAAT-M-STA.21", ses: 44, lvl: 4,
    stem: "If ₈P₃ = k × ₇P₂, what is k?",
    opts: [
      "7",
      "2",
      "8",
      "3"
    ],
    ans: 2,
    trick: "write both as falling products and CANCEL — 8 × 7 × 6 over 7 × 6 leaves the 8, so the answer is the leading factor and not any of the small numbers in the symbols",
    why: "336 ÷ 42 = 8.",
    traps: [
      "A: the upper index of the second symbol copied.",
      "B: the lower index of the second symbol copied.",
      "D: the lower index of the first symbol copied.",
    ],
  },
  {
    sig: "probability-of-one-particular-pair",
    code: "SAAT-M-STA.22", ses: 44, lvl: 4,
    stem: "Two of 8 students are chosen at random to represent the class. What is the probability that a particular pair of friends is the pair chosen?",
    opts: [
      "1/56",
      "2/28",
      "1/8",
      "1/28"
    ],
    ans: 3,
    trick: "a committee has no ORDER, so the denominator is a COMBINATION — using the permutation count doubles the denominator, and that value is offered",
    why: "There are C(8, 2) = 28 possible pairs, and one of them is the pair in question.",
    traps: [
      "A: the ordered count used in the denominator.",
      "B: an ordered numerator over an unordered denominator.",
      "C: the probability of choosing one named student.",
    ],
  },
  {
    sig: "which-is-not-a-measure-of-spread",
    code: "SAAT-M-STA.23", ses: 42, lvl: 2,
    stem: "Which of the following is NOT a measure of dispersion?",
    opts: [
      "The median",
      "The range",
      "The variance",
      "The standard deviation"
    ],
    ans: 0,
    trick: "the question is NEGATIVE — three of these describe how spread out the data are and one describes where its centre is, so the odd one out is the measure of CENTRE",
    why: "The median is a measure of central tendency, not of spread.",
    traps: [
      "B: the range is the simplest measure of spread.",
      "C: the variance is a measure of spread.",
      "D: the standard deviation is a measure of spread.",
    ],
  },

  // ================================================= ALGEBRA AND FUNCTIONS
  {
    sig: "hole-of-a-rational-function-as-a-point",
    code: "SAAT-M-ALG.136", ses: 93, lvl: 4,
    stem: "The function below has a hole in its graph. At which point is it?",
    stemEq: "f_hole",
    opts: [
      { eq: "f_h4" },
      { eq: "f_h1" },
      { eq: "f_h2" },
      { eq: "f_h3" }
    ],
    ans: 1,
    trick: "the x value comes from the CANCELLED factor and the y value from the REDUCED function — reading the y value off the original numerator, or forgetting to reverse the sign inside the bracket, gives the two nearby options",
    why: "(x + 3)(x − 5)/(x + 3) = x − 5 for x ≠ −3, and at x = −3 that reduced form is −8.",
    traps: [
      "A: both signs reversed.",
      "C: the sign of the x value not reversed.",
      "D: the y value taken from the other factor.",
    ],
  },
  {
    sig: "choose-the-function-with-given-asymptotes",
    code: "SAAT-M-ALG.137", ses: 93, lvl: 4,
    stem: "Which function has a vertical asymptote at x = 4 and a horizontal asymptote at y = 0?",
    opts: [
      { eq: "f_ca3" },
      { eq: "f_ca4" },
      { eq: "f_ca1" },
      { eq: "f_ca2" }
    ],
    ans: 2,
    trick: "a factor that CANCELS gives a hole, not an asymptote, and a horizontal asymptote at zero needs the bottom to outrank the top in degree — both conditions must be checked, not one",
    why: "1/(x − 4) has a zero denominator at x = 4 that does not cancel, and its numerator has lower degree.",
    traps: [
      "A: the degrees are equal, so the horizontal asymptote is not zero.",
      "B: the sign of the asymptote is wrong.",
      "D: the factor cancels, leaving a hole at x = 4.",
    ],
  },
  {
    sig: "inverse-of-a-cubic",
    code: "SAAT-M-ALG.138", ses: 24, lvl: 3,
    stem: "What is the inverse of f(x) = x³ + 5?",
    opts: [
      { eq: "f_ic2" },
      { eq: "f_ic3" },
      { eq: "f_ic4" },
      { eq: "f_ic1" }
    ],
    ans: 3,
    trick: "undo the operations in REVERSE order — subtract the 5 first, then take the CUBE root; taking a square root, or adding the 5 back, are the two errors on the page",
    why: "y = x³ + 5 gives x = ∛(y − 5).",
    traps: [
      "A: the sign of the 5 not reversed.",
      "B: a square root taken instead of a cube root.",
      "C: the whole expression cubed.",
    ],
  },
  {
    sig: "powers-of-i",
    code: "SAAT-M-ALG.139", ses: 61, lvl: 2,
    stem: "What is the value of i⁴⁷?",
    opts: [
      { eq: "f_pi1" },
      { eq: "f_pi2" },
      { eq: "f_pi3" },
      { eq: "f_pi4" }
    ],
    ans: 0,
    trick: "divide the exponent by 4 and keep the REMAINDER — 47 leaves 3, and i³ is −i; the cycle is 1, i, −1, −i, so any answer can be reached by counting wrong by one",
    why: "47 = 4(11) + 3, so i⁴⁷ = i³ = −i.",
    traps: [
      "B: the remainder taken as 1.",
      "C: the remainder taken as 2.",
      "D: the sign of the answer dropped.",
    ],
  },
  {
    sig: "product-of-two-pure-imaginaries",
    code: "SAAT-M-ALG.140", ses: 61, lvl: 2,
    stem: "Simplify (5i)(3i).",
    opts: [
      "−15i",
      "−15",
      "15",
      "15i"
    ],
    ans: 1,
    trick: "i × i is −1, so the product of two pure imaginaries is a REAL number with the sign flipped — leaving an i in the answer means the i² was never used",
    why: "15i² = 15(−1) = −15.",
    traps: [
      "A: one i left in the answer.",
      "C: i² taken as +1.",
      "D: the i's not multiplied at all.",
    ],
  },
  {
    sig: "degree-with-a-constant-raised-to-a-power",
    code: "SAAT-M-ALG.141", ses: 5, lvl: 3,
    stem: "What is the degree of the polynomial below?",
    stemEq: "f_deg2",
    opts: [
      "3",
      "5",
      "4",
      "6"
    ],
    ans: 2,
    trick: "an exponent on a CONSTANT is just arithmetic, not degree — only the powers of the variable count, and the terms need not be written in order",
    why: "The powers of x present are 4, 3 and 1, so the degree is 4; the 2⁶ is a number.",
    traps: [
      "A: the first-written term's power taken.",
      "B: the exponents of two terms added.",
      "D: the exponent on the constant counted.",
    ],
  },
  {
    sig: "leading-coefficient-out-of-order",
    code: "SAAT-M-ALG.142", ses: 5, lvl: 2,
    stem: "What is the leading coefficient of the polynomial below?",
    stemEq: "f_lead",
    opts: [
      "9",
      "7",
      "5",
      "−2"
    ],
    ans: 3,
    trick: "order the terms by DEGREE first — the leading coefficient belongs to the highest power, not to the term written first and not to the biggest number",
    why: "The highest power is x⁵, whose coefficient is −2.",
    traps: [
      "A: the coefficient of the first-written term.",
      "B: the largest coefficient taken.",
      "C: the constant term taken.",
    ],
  },
  {
    sig: "domain-of-a-product-of-reciprocal-quotients",
    code: "SAAT-M-ALG.143", ses: 20, lvl: 4,
    stem: "For f(x) = x − 2 and g(x) = x + 5, what is the domain of (f/g)·(g/f)?",
    opts: [
      "All real numbers except 2 and −5",
      "All real numbers",
      "All real numbers except 2",
      "All real numbers except −5"
    ],
    ans: 0,
    trick: "the product simplifies to 1, but the DOMAIN is decided before any cancelling — every value that made a denominator zero anywhere in the expression stays excluded",
    why: "g(x) = 0 at x = −5 and f(x) = 0 at x = 2, and both appear as denominators.",
    traps: [
      "B: the expression cancelled before the domain was taken.",
      "C: only one exclusion found.",
      "D: only the other exclusion found.",
    ],
  },
  {
    sig: "polynomial-division-quotient",
    code: "SAAT-M-ALG.144", ses: 16, lvl: 4,
    stem: "Divide the polynomial below by x − 2.",
    stemEq: "f_div",
    opts: [
      { eq: "f_dv4" },
      { eq: "f_dv1" },
      { eq: "f_dv2" },
      { eq: "f_dv3" }
    ],
    ans: 1,
    trick: "the quotient of a CUBIC by a linear factor is a QUADRATIC — an answer of the wrong degree can be struck out before any arithmetic, and the zero used in synthetic division is +2, not −2",
    why: "x³ − 3x² − 4x + 12 = (x − 2)(x² − x − 6).",
    traps: [
      "A: the middle term lost.",
      "C: the sign of the divisor's zero taken as −2.",
      "D: a quotient of the wrong degree.",
    ],
  },

  // ================================================================ CALCULUS
  {
    sig: "limit-of-a-product-with-a-bounded-factor",
    code: "SAAT-M-CAL.47", ses: 91, lvl: 3,
    stem: "Evaluate the limit below.",
    stemEq: "f_lim",
    opts: [
      "3",
      "It does not exist",
      "0",
      "1"
    ],
    ans: 2,
    trick: "substitute directly — the cosine is perfectly well behaved at zero and equals 1, so the whole limit is the polynomial factor's value, which is zero; evaluating only the trig factor is the trap",
    why: "3x·cos x at x = 0 is 0 × 1 = 0.",
    traps: [
      "A: only the coefficient reported.",
      "B: the product wrongly treated as indeterminate.",
      "D: only the cosine factor evaluated.",
    ],
  },
  {
    sig: "quotient-rule-with-a-radical",
    code: "SAAT-M-CAL.48", ses: 95, lvl: 4,
    stem: "For f(x) = (x² + 1) ÷ x, what is f′(1)?",
    opts: [
      "2",
      "1",
      "3",
      "0"
    ],
    ans: 3,
    trick: "either use the quotient rule or split the fraction first — differentiating the top and the bottom separately is not a rule at all, and it is what the wrong options are built from",
    why: "f(x) = x + 1/x, so f′(x) = 1 − 1/x² and f′(1) = 0.",
    traps: [
      "A: the function's value at 1 given instead of the derivative.",
      "B: numerator and denominator differentiated separately.",
      "C: the reciprocal term's sign lost.",
    ],
  },
  {
    sig: "absolute-maximum-on-a-closed-interval",
    code: "SAAT-M-CAL.49", ses: 102, lvl: 4,
    stem: "What is the absolute maximum of f(x) = x² − 4x + 1 on the closed interval [0, 5]?",
    opts: [
      "6",
      "1",
      "−3",
      "5"
    ],
    ans: 0,
    trick: "an upward parabola takes its greatest value on a closed interval at an ENDPOINT, never at the vertex — the vertex gives the MINIMUM, and it is offered",
    why: "f(0) = 1, f(5) = 6 and the vertex value f(2) = −3, so the maximum is 6.",
    traps: [
      "B: the value at the left endpoint.",
      "C: the minimum, at the vertex.",
      "D: the endpoint's x value reported instead of the function's value.",
    ],
  },
  {
    sig: "definite-integral-with-a-parameter",
    code: "SAAT-M-CAL.50", ses: 112, lvl: 4,
    stem: "For which value of k does the integral of kx from 0 to 4 equal 24?",
    opts: [
      "24",
      "3",
      "6",
      "1.5"
    ],
    ans: 1,
    trick: "integrate FIRST and set the result equal to the target — the x integrates to x²/2, so the constant is multiplied by 8, and forgetting that half doubles the answer",
    why: "∫₀⁴ kx dx = k(16/2) = 8k = 24, so k = 3.",
    traps: [
      "A: the target itself reported.",
      "C: the half from integrating x left out.",
      "D: the target divided by the interval length squared.",
    ],
  },
  {
    sig: "integral-of-an-absolute-value",
    code: "SAAT-M-CAL.51", ses: 112, lvl: 4,
    stem: "Evaluate the integral of |x| from −3 to 3.",
    opts: [
      "4.5",
      "18",
      "9",
      "0"
    ],
    ans: 2,
    trick: "split the interval where the inside changes sign — integrating x straight through gives zero by symmetry, and that zero is the option the whole question is built to catch",
    why: "Two triangles of base 3 and height 3: 2 × (1/2)(3)(3) = 9.",
    traps: [
      "A: only one of the two halves counted.",
      "B: the bounding rectangle's area given.",
      "D: the absolute-value bars ignored.",
    ],
  },
];
