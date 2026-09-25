// PART G of the SAAT booklet — the ninth ETEC sample paper, together with the
// skills from the earlier eight that part F had not yet reached.
//
// Same rule as part F: the papers were read for the SKILL and the TRICK only.
// Every stem is newly worded, every number set is new, every option list is
// rebuilt, and every figure is drawn from scratch in make_figs_saat_g.py.
//
// The ninth paper is a revision deck rather than a secure form — it prints the
// topic on the page and shades the right answer — so it was mined purely for
// coverage. Its profile is unusual: reasoning and proof take nearly a quarter of
// it, trigonometric identities another fifth, and there is no algebra-basics or
// probability content at all. That shape is why this part leans on logic,
// identities and coordinate proof, and why the probability and sequence skills
// left over from samples 2 and 3 are finished off here.
//
// Every answer is re-derived independently in verify_saat_g.py.

module.exports = [
  // ============================================ TRIGONOMETRIC IDENTITIES
  {
    sig: "simplify-sin-squared-times-secant",
    code: "SAAT-M-TRI.43", ses: 73, lvl: 4,
    stem: "Simplify the expression below.",
    stemEq: "g_id1",
    opts: [
      { eq: "g_id1a" },
      { eq: "g_id1b" },
      { eq: "g_id1c" },
      { eq: "g_id1d" }
    ],
    ans: 0,
    trick: "turn the secant into 1 over the cosine FIRST, then put everything over that one denominator — the sin² becomes 1 − cos², the cos² cancels against it, and what survives is a single reciprocal",
    why: "sin²θ·secθ + cosθ = (1 − cos²θ)/cos θ + cos θ = 1/cos θ = sec θ.",
    traps: [
      "B: the reciprocal of the answer.",
      "C: the cos θ term dropped before combining.",
      "D: sin² replaced by 1 + cos².",
    ],
  },
  {
    sig: "exact-value-with-tan-45",
    code: "SAAT-M-TRI.44", ses: 74, lvl: 4,
    stem: "Find the exact value of the product below.",
    stemEq: "g_id2",
    opts: [
      "1.5",
      "1",
      "2",
      "0.5"
    ],
    ans: 1,
    trick: "1 + tan²θ is sec²θ and 1 − sin²θ is cos²θ, so the product is sec²θ · cos²θ, which is 1 for EVERY angle — the 45° is decoration and nothing ever has to be evaluated",
    why: "1 + tan²45° = sec²45° = 2 and 1 − sin²45° = cos²45° = 1/2, so the product is 2 × 1/2 = 1.",
    traps: [
      "A: sin 45° read as 1/2 rather than √2/2.",
      "C: the second bracket evaluated as 1, leaving sec²45°.",
      "D: the tan² term dropped, leaving the first bracket as 1.",
    ],
  },
  {
    sig: "hypotenuse-from-sine-and-cosine-legs",
    code: "SAAT-M-TRI.45", ses: 73, lvl: 3,
    stem: "In the right triangle below the two legs are sin x and cos x. How long is the hypotenuse?",
    fig: "g_tri_trig", figW: 1.7,
    opts: [
      { eq: "g_hy3" },
      { eq: "g_hy4" },
      { eq: "g_hy1" },
      { eq: "g_hy2" }
    ],
    ans: 2,
    trick: "Pythagoras SQUARES the legs before adding, and sin² + cos² is exactly 1 — adding the legs themselves gives an expression that is not even constant, which is the option the eye reaches for",
    why: "√(sin²x + cos²x) = √1 = 1.",
    traps: [
      "A: the identity misquoted as sin x · cos x.",
      "B: each square read as 1, giving \u221a2.",
      "D: the two legs simply added.",
    ],
  },
  {
    sig: "factorable-trig-equation-keep-both-roots",
    code: "SAAT-M-TRI.46", ses: 76, lvl: 4,
    stem: "Solve sin θ (2 cos θ − 1) = 0 for 0° ≤ θ < 360°.",
    opts: [
      "60° and 300° only",
      "0° and 180° only",
      "0°, 60° and 180°",
      "0°, 60°, 180° and 300°"
    ],
    ans: 3,
    trick: "set EACH factor to zero and keep every root of both — dividing the equation through by sin θ throws away the whole first family, and the shortened answer is always offered",
    why: "sin θ = 0 gives 0° and 180°; cos θ = 1/2 gives 60° and 300°.",
    traps: [
      "A: the equation divided through by sin θ.",
      "B: only the sine factor solved.",
      "C: the second cosine root, in the fourth quadrant, missed.",
    ],
  },
  {
    sig: "third-side-from-two-sides-and-the-included-angle",
    code: "SAAT-M-TRI.47", ses: 77, lvl: 4,
    stem: "A triangle has sides of 5 cm and 8 cm with an angle of 60° between them. How long is the third side?",
    opts: [
      { eq: "g_lc1" },
      { eq: "g_lc2" },
      { eq: "g_lc3" },
      { eq: "g_lc4" }
    ],
    ans: 0,
    trick: "two sides and the angle BETWEEN them is the law of cosines, not the law of sines — and the middle term is SUBTRACTED, so the answer is shorter than the hypotenuse Pythagoras would give",
    why: "√(25 + 64 − 2·5·8·cos 60°) = √(89 − 40) = 7.",
    traps: [
      "B: the cosine term added instead of subtracted.",
      "C: Pythagoras used, ignoring the angle.",
      "D: the two sides simply subtracted.",
    ],
  },

  // ==================================================== FUNCTIONS AND GRAPHS
  {
    sig: "domain-of-a-composition",
    code: "SAAT-M-ALG.145", ses: 25, lvl: 4,
    stem: "For f(x) = x² − 9 and g(x) = 1 ÷ (x − 2), what is the domain of f∘g?",
    opts: [
      "All real numbers",
      "All real numbers except 2",
      "All real numbers except 3 and −3",
      "All real numbers except −2"
    ],
    ans: 1,
    trick: "the INNER function runs first, so its restriction is inherited whatever the outer function does — the zeros of f are not exclusions at all, and they are the option placed beside the answer",
    why: "g is undefined at x = 2, and f accepts every real input, so only x = 2 is excluded.",
    traps: [
      "A: the inner function's restriction overlooked.",
      "C: the zeros of the outer function excluded.",
      "D: the sign of the exclusion reversed.",
    ],
  },
  {
    sig: "read-a-shifted-radical-graph",
    code: "SAAT-M-ALG.146", ses: 23, lvl: 4,
    stem: "The graph below is a transformation of the parent function shown. What is its rule?",
    stemEq: "j_shiftroot",
    fig: "g_radical", figW: 1.9,
    opts: [
      { eq: "g_rg3" },
      { eq: "g_rg4" },
      { eq: "g_rg1" },
      { eq: "g_rg2" }
    ],
    ans: 2,
    trick: "the ENDPOINT gives both shifts — its x is the horizontal one with the sign reversed, its y the vertical one as it stands — and a second marked point is what fixes the stretch",
    why: "The endpoint (1, −1) gives y = a√(x − 1) − 1, and (5, 3) gives 3 = a(2) − 1, so a = 2.",
    traps: [
      "A: the stretch left out.",
      "B: the stretch inverted.",
      "D: the horizontal shift's sign not reversed.",
    ],
  },
  {
    sig: "point-that-fails-an-inequality",
    code: "SAAT-M-ALG.147", ses: 8, lvl: 3,
    stem: "Which ordered pair does NOT satisfy the inequality 2x − 3y ≤ 12?",
    opts: [
      "(0, 0)",
      "(3, −1)",
      "(−2, 4)",
      "(9, 1)"
    ],
    ans: 3,
    trick: "substitute and compare — the question is NEGATIVE, so three of the four will work and the odd one out is the pair that pushes the left side ABOVE 12",
    why: "2(9) − 3(1) = 15, which is greater than 12.",
    traps: [
      "A: 0 ≤ 12 holds.",
      "B: 6 + 3 = 9 ≤ 12 holds.",
      "C: −4 − 12 = −16 ≤ 12 holds.",
    ],
  },
  {
    sig: "percent-growth-over-several-years",
    code: "SAAT-M-ALG.148", ses: 53, lvl: 4,
    stem: "A school had 800 students and its roll grows by 10% each year. How many students will it have after 3 years?",
    opts: [
      "1064.8",
      "1040",
      "880",
      "1100"
    ],
    ans: 0,
    trick: "growth COMPOUNDS: multiply by 1.1 three times, not add 10% of the original three times — the simple-interest answer is always offered and is always smaller",
    why: "800(1.1)³ = 800(1.331) = 1064.8.",
    traps: [
      "B: simple growth, 10% of 800 added three times.",
      "C: only one year applied.",
      "D: the percentage applied to a rounded figure.",
    ],
  },

  // ============================================ MATRICES, COMPLEX AND POLAR
  {
    sig: "determinant-equation-with-a-quadratic",
    code: "SAAT-M-ALG.149", ses: 10, lvl: 4,
    stem: "For which positive value of x is the determinant below equal to 20?",
    stemEq: "g_det",
    opts: [
      "−6",
      "6",
      "4",
      "36"
    ],
    ans: 1,
    trick: "expand to ad − bc, and if the unknown appears in both diagonal entries the equation is QUADRATIC — the value of x² is not x, and it is the large option on the page",
    why: "x·x − 4·4 = 20 gives x² = 36, so the positive root is 6.",
    traps: [
      "A: the negative root, which the question excludes.",
      "C: the 16 added instead of subtracted.",
      "D: x² reported instead of x.",
    ],
  },
  {
    sig: "de-moivre-fourth-power",
    code: "SAAT-M-ALG.150", ses: 80, lvl: 4,
    stem: "Evaluate [2(cos 45° + i sin 45°)]⁴ and give the answer in rectangular form.",
    opts: [
      "16i",
      "−16i",
      "−16",
      "16"
    ],
    ans: 2,
    trick: "the modulus is raised to the power and the argument MULTIPLIED by it — 4 × 45° is 180°, which lands on the negative real axis, so the answer carries no i at all",
    why: "2⁴ = 16 and 4(45°) = 180°, so the result is 16(cos 180° + i sin 180°) = −16.",
    traps: [
      "A: the angle taken as 90°.",
      "B: the angle taken as 270°.",
      "D: the sign at 180° lost.",
    ],
  },
  {
    sig: "polar-equation-to-a-circle",
    code: "SAAT-M-TRI.48", ses: 80, lvl: 4,
    stem: "What is the rectangular form of the polar equation below?",
    stemEq: "g_pol",
    opts: [
      { eq: "g_pc2" },
      { eq: "g_pc3" },
      { eq: "g_pc4" },
      { eq: "g_pc1" }
    ],
    ans: 3,
    trick: "1 over the secant is the COSINE, so the equation is r = 6 cos θ; multiply through by r to get r² and r cos θ, both of which convert — the result is a circle OFF the origin, not centred on it",
    why: "r = 6 cos θ gives r² = 6r cos θ, so x² + y² = 6x, that is (x − 3)² + y² = 9.",
    traps: [
      "A: the circle taken as centred at the origin.",
      "B: the cosine read as a sine.",
      "C: the radius not halved.",
    ],
  },
  {
    sig: "false-property-of-an-ellipse",
    code: "SAAT-M-GEO.83", ses: 84, lvl: 4,
    stem: "For the ellipse (x − 2)²/25 + (y + 1)²/9 = 1, which statement is FALSE?",
    opts: [
      "Its major axis is vertical",
      "Its centre is (2, −1)",
      "Its minor axis has length 6",
      "Its foci are 8 units apart"
    ],
    ans: 0,
    trick: "the LARGER denominator sits under the variable whose axis is major — 25 is under the x, so the major axis is horizontal; and c comes from a SUBTRACTION, the hyperbola's rule being the sum",
    why: "25 > 9 and 25 is under x, so the major axis is horizontal; c = √(25 − 9) = 4 and the foci are 2c = 8 apart.",
    traps: [
      "B: the centre signs are correctly reversed, so this is true.",
      "C: 2b = 6, so this is true.",
      "D: 2c = 8, so this is true.",
    ],
  },

  // ====================================================== COORDINATE PROOF
  {
    sig: "fourth-vertex-of-an-isosceles-trapezoid",
    code: "SAAT-M-GEO.84", ses: 39, lvl: 4,
    stem: "The trapezoid below is isosceles and three of its vertices are labelled. What are the coordinates of M?",
    fig: "g_trap_coord", figW: 2.0,
    opts: [
      { eq: "g_tz4" },
      { eq: "g_tz1" },
      { eq: "g_tz2" },
      { eq: "g_tz3" }
    ],
    ans: 1,
    trick: "isosceles means the two legs are congruent, so the top side must be inset by the SAME amount at each end — the left end is inset by a, so the right end must be inset by a from a + b",
    why: "The top-left vertex is (a, c) and the base runs to (a + b, 0), so M is (b, c).",
    traps: [
      "A: the coordinates interchanged.",
      "C: the inset not applied at the right-hand end.",
      "D: the two parameters added.",
    ],
  },
  {
    sig: "perpendicular-line-through-a-point",
    code: "SAAT-M-GEO.85", ses: 38, lvl: 4,
    stem: "What is the equation of the line through (4, 1) perpendicular to y = 2x − 5?",
    opts: [
      { eq: "g_pp3" },
      { eq: "g_pp4" },
      { eq: "g_pp1" },
      { eq: "g_pp2" }
    ],
    ans: 2,
    trick: "take the NEGATIVE RECIPROCAL of the slope, then use the point — keeping the original slope gives a parallel line, which is the option that looks most like the question",
    why: "The perpendicular slope is −1/2, and 1 = −1/2(4) + c gives c = 3.",
    traps: [
      "A: the reciprocal taken without the sign change.",
      "B: the intercept's sign reversed.",
      "D: the original slope kept, giving a parallel line.",
    ],
  },
  {
    sig: "apex-of-a-right-triangle-on-the-axes",
    code: "SAAT-M-GEO.86", ses: 39, lvl: 3,
    stem: "In the figure below the right angle is at B. What are the coordinates of C, given that BC measures 4?",
    fig: "g_tri_coord", figW: 1.95,
    opts: [
      { eq: "g_ax2" },
      { eq: "g_ax3" },
      { eq: "g_ax4" },
      { eq: "g_ax1" }
    ],
    ans: 3,
    trick: "a right angle at B on the x-axis makes BC VERTICAL, so C sits directly above B and keeps B's x coordinate — swapping the two coordinates is the error the options are built on",
    why: "B is (3, 0) and BC is vertical of length 4, so C is (3, 4).",
    traps: [
      "A: the coordinates interchanged.",
      "B: the length measured from the origin instead of from B.",
      "C: the sign of the x coordinate taken from A.",
    ],
  },

  // ============================================ REASONING, PROOF AND LOGIC
  {
    sig: "parity-of-an-expression",
    code: "SAAT-M-ALG.151", unit: 0, topic: "Statements, truth values & reasoning", lvl: 3,
    stem: "m is even and n is odd. Which expression below is always ODD?",
    opts: [
      "n²",
      "mn",
      "m + m",
      "m³"
    ],
    ans: 0,
    trick: "an odd number stays odd under any power, and any product with an EVEN factor is even — so the only way to stay odd is to keep every factor odd",
    why: "An odd number times an odd number is odd, so n² is odd.",
    traps: [
      "B: an even factor makes the product even.",
      "C: the sum of two evens is even.",
      "D: any power of an even number is even.",
    ],
  },
  {
    sig: "which-compound-statement-is-false",
    code: "SAAT-M-ALG.152", unit: 0, topic: "Statements, truth values & reasoning", lvl: 3,
    stem: "p is true and q is false. Which compound statement below is FALSE?",
    opts: [
      "~q ∨ q",
      "p ∧ q",
      "p ∨ q",
      "p ∧ ~q"
    ],
    ans: 1,
    trick: "AND needs BOTH parts true and OR needs only one — the question is negative, so three of these survive and only the conjunction of a true with a false fails",
    why: "p ∧ q needs q, which is false.",
    traps: [
      "A: a statement or its negation is always true.",
      "C: p alone carries the disjunction.",
      "D: ~q is true, so both parts hold.",
    ],
  },
  {
    sig: "counterexample-must-satisfy-the-hypothesis",
    code: "SAAT-M-ALG.153", unit: 0, topic: "Statements, truth values & reasoning", lvl: 4,
    stem: "Which number is a counterexample to the claim \"if n is prime, then n is odd\"?",
    opts: [
      "9",
      "0",
      "2",
      "1"
    ],
    ans: 2,
    trick: "a counterexample must make the HYPOTHESIS TRUE and the conclusion FALSE — a number that simply fails to be prime refutes nothing, however even it is, and two of these are exactly that",
    why: "2 is prime and it is not odd.",
    traps: [
      "A: 9 is odd, so the conclusion holds.",
      "B: 0 is not prime.",
      "D: 1 is not prime, so the hypothesis fails.",
    ],
  },
  {
    sig: "angles-that-share-only-a-vertex",
    code: "SAAT-M-GEO.87", ses: 28, lvl: 3,
    stem: "The figure below shows two lines crossing. Are angles 1 and 2 adjacent, and why?",
    fig: "g_vertical", figW: 1.7,
    opts: [
      "Yes — they share a vertex",
      "Yes — they are formed by the same two lines",
      "No — they are supplementary",
      "No — they share a vertex but no side"
    ],
    ans: 3,
    trick: "adjacent angles must share a VERTEX and a SIDE and overlap nowhere — vertical angles share the vertex only, so sharing a point is not enough",
    why: "Angles 1 and 2 are vertical angles; they have no common ray.",
    traps: [
      "A: a common vertex alone does not make angles adjacent.",
      "B: being formed by the same lines is not the test.",
      "C: vertical angles are congruent, not supplementary.",
    ],
  },
  {
    sig: "three-set-venn-count",
    code: "SAAT-M-STA.24", ses: 43, lvl: 4,
    stem: "The diagram below shows how many students take each subject. How many take Maths AND Physics?",
    fig: "g_venn3", figW: 2.0,
    opts: [
      "12",
      "4",
      "8",
      "24"
    ],
    ans: 0,
    trick: "\"Maths and Physics\" means EVERY student inside both circles, so the region shared by all three counts too — taking only the two-way sliver is the standard error and it is the option beside the answer",
    why: "4 in the Maths-Physics-only region plus 8 in the triple region gives 12.",
    traps: [
      "B: the triple region left out.",
      "C: only the triple region counted.",
      "D: the whole Maths circle counted.",
    ],
  },

  // ========================================================= PLANE GEOMETRY
  {
    sig: "pentagon-with-an-attached-triangle",
    code: "SAAT-M-GEO.88", ses: 32, lvl: 4,
    stem: "An isosceles triangle stands on one side of the regular pentagon below, with its two equal sides marked. If each base angle of the triangle equals the pentagon's exterior angle, what is x?",
    fig: "g_pent_tri", figW: 1.85,
    opts: [
      "144°",
      "36°",
      "72°",
      "108°"
    ],
    ans: 1,
    trick: "two steps, and the paper wants you to stop after the first — find the pentagon's exterior angle, 72°, then remember the triangle still has to add to 180°, so the apex is 180 − 2(72)",
    why: "The exterior angle is 360 ÷ 5 = 72°, so x = 180 − 144 = 36.",
    traps: [
      "A: the two base angles added.",
      "C: the exterior angle reported as the answer.",
      "D: the interior angle reported.",
    ],
  },
  {
    sig: "number-of-sides-from-an-exterior-angle",
    code: "SAAT-M-GEO.89", ses: 32, lvl: 3,
    stem: "Each exterior angle of a regular polygon is 24°. How many sides has it?",
    opts: [
      "12",
      "156",
      "15",
      "24"
    ],
    ans: 2,
    trick: "the exterior angles always total 360°, so n = 360 ÷ exterior — using 180 instead, or reporting the interior angle, are the two errors the options carry",
    why: "360 ÷ 24 = 15.",
    traps: [
      "A: 180 ÷ 15 used.",
      "B: the interior angle given.",
      "D: the angle copied as the count.",
    ],
  },
  {
    sig: "median-bisects-the-base-solve",
    code: "SAAT-M-GEO.90", ses: 29, lvl: 4,
    stem: "In the triangle below AD is a median. What is the length of AC?",
    fig: "g_cevian", figW: 2.1,
    opts: [
      "6",
      "13",
      "26",
      "16"
    ],
    ans: 3,
    trick: "the median bisects the base, so the two BASE pieces are equal — solve that equation, then substitute into the side the question actually asks for, which is a different expression",
    why: "3x − 5 = x + 7 gives x = 6, so AC = 2(6) + 4 = 16.",
    traps: [
      "A: the value of x reported as a length.",
      "B: one of the base pieces given.",
      "C: the whole base given.",
    ],
  },
  {
    sig: "centroid-vertex-distance",
    code: "SAAT-M-GEO.91", ses: 29, lvl: 3,
    stem: "In the triangle below F is the centroid and T is the midpoint of AB. How long is CF?",
    fig: "g_centroid", figW: 2.05,
    opts: [
      "10",
      "15",
      "5",
      "2.5"
    ],
    ans: 0,
    trick: "the centroid cuts a median in the ratio 2 : 1 measured FROM THE VERTEX, so the vertex piece is TWICE the short one — three times it is the whole median, and that is offered",
    why: "CF = 2 × FT = 2 × 5 = 10.",
    traps: [
      "B: the whole median given.",
      "C: the short piece repeated.",
      "D: the ratio applied as 1 : 2.",
    ],
  },
  {
    sig: "which-congruence-postulate-from-a-figure",
    code: "SAAT-M-GEO.92", ses: 30, lvl: 4,
    stem: "In the figure below AB ≅ CD, the marked angles are congruent and AC is shared. Which postulate proves the two triangles congruent?",
    fig: "g_congruence", figW: 2.0,
    opts: [
      "SSA",
      "SAS",
      "ASA",
      "SSS"
    ],
    ans: 1,
    trick: "count what is marked: TWO sides and ONE angle, and the angle sits BETWEEN them — that is SAS; if the angle were anywhere else the marks would prove nothing at all",
    why: "AB ≅ CD, AC is common, and the angles between those pairs of sides are congruent.",
    traps: [
      "A: SSA is not a congruence postulate.",
      "C: ASA needs two angles.",
      "D: SSS needs three sides.",
    ],
  },
  {
    sig: "triangle-inequality-range-for-a-third-side",
    code: "SAAT-M-GEO.93", ses: 29, lvl: 3,
    stem: "Two sides of a triangle measure 7 cm and 11 cm. Which value can NOT be the third side?",
    opts: [
      "12",
      "17",
      "4",
      "6"
    ],
    ans: 2,
    trick: "the third side must lie strictly BETWEEN the difference and the sum — a value exactly equal to the difference gives a flat, degenerate triangle, and that boundary case is what the paper is testing",
    why: "The third side must satisfy 4 < n < 18, so 4 itself is impossible.",
    traps: [
      "A: 12 lies inside the range.",
      "B: 17 lies inside the range.",
      "D: 6 lies inside the range.",
    ],
  },
  {
    sig: "similar-triangles-perimeter-ratio",
    code: "SAAT-M-GEO.94", ses: 30, lvl: 3,
    stem: "Two similar triangles have corresponding sides in the ratio 2 : 5. The perimeter of the smaller is 18 cm. What is the perimeter of the larger?",
    opts: [
      "7.2 cm",
      "36 cm",
      "112.5 cm",
      "45 cm"
    ],
    ans: 3,
    trick: "perimeter is a LENGTH, so it scales by the plain ratio and not by its square — and the ratio must be applied the right way up, since the larger perimeter has to come out larger",
    why: "18 × 5/2 = 45.",
    traps: [
      "A: the ratio applied upside down.",
      "B: the ratio applied as a difference.",
      "C: the square of the ratio used.",
    ],
  },
  {
    sig: "similarity-scale-factor-find-a-side",
    code: "SAAT-M-GEO.95", ses: 30, lvl: 3,
    stem: "Rectangle ABCD is mapped to rectangle QRST by a scale factor of 3/4. If AB measures 12 cm, how long is QR?",
    opts: [
      "9 cm",
      "16 cm",
      "12 cm",
      "36 cm"
    ],
    ans: 0,
    trick: "a scale factor maps the FIRST figure to the second, so you multiply by it — dividing instead enlarges when the factor is less than one, and that enlarged value is offered",
    why: "12 × 3/4 = 9.",
    traps: [
      "B: divided by the factor instead of multiplied.",
      "C: the original length repeated.",
      "D: multiplied by the reciprocal's numerator only.",
    ],
  },

  // ==================================================== SEQUENCES AND SERIES
  {
    sig: "geometric-sequence-with-a-negative-ratio",
    code: "SAAT-M-ALG.154", ses: 57, lvl: 3,
    stem: "What is the next term of the sequence 16, −8, 4, −2, …?",
    opts: [
      "−4",
      "1",
      "−1",
      "2"
    ],
    ans: 1,
    trick: "the ratio is NEGATIVE, so the signs alternate — the next term after a negative one must be positive, and taking the ratio as one half without its sign gives the same number with the wrong sign",
    why: "The ratio is −1/2, and −2 × (−1/2) = 1.",
    traps: [
      "A: the ratio taken as 2.",
      "C: the ratio taken as positive one half.",
      "D: the difference of the last two terms used.",
    ],
  },
  {
    sig: "binomial-named-term",
    code: "SAAT-M-ALG.155", ses: 59, lvl: 4,
    stem: "What is the fourth term in the expansion of (x − 2)⁶, written in descending powers of x?",
    opts: [
      { eq: "g_bt3" },
      { eq: "g_bt4" },
      { eq: "g_bt1" },
      { eq: "g_bt2" }
    ],
    ans: 2,
    trick: "the FOURTH term carries k = 3, not 4 — the index is always one less than the term's name, and the odd power of a negative second term makes the coefficient negative",
    why: "C(6,3)·x³·(−2)³ = 20(−8)x³ = −160x³.",
    traps: [
      "A: k taken as 4.",
      "B: the binomial coefficient left off.",
      "D: the sign of the cube lost.",
    ],
  },
  {
    sig: "sigma-arithmetic-series-sum",
    code: "SAAT-M-ALG.156", ses: 59, lvl: 4,
    stem: "Evaluate the sum below.",
    stemEq: "g_sig",
    opts: [
      "165",
      "32",
      "370",
      "185"
    ],
    ans: 3,
    trick: "write out the first and last terms, count HOW MANY there are, and use n(a₁ + aₙ)/2 — dropping the constant term, or counting the terms wrong, are the two errors on the page",
    why: "The terms run 5, 8, …, 32 with n = 10, so the sum is 10(5 + 32)/2 = 185.",
    traps: [
      "A: the constant term left out of every term.",
      "B: only the last term given.",
      "C: the sum doubled.",
    ],
  },
  {
    sig: "factorial-backwards",
    code: "SAAT-M-ALG.157", ses: 44, lvl: 3,
    stem: "Given that 8! = 40320, what is 7!?",
    opts: [
      "5040",
      "40319",
      "20160",
      "4480"
    ],
    ans: 0,
    trick: "n! = n × (n − 1)!, so 7! is 8! DIVIDED by 8 — subtracting one, or halving, are the two shortcuts the options punish",
    why: "40320 ÷ 8 = 5040.",
    traps: [
      "B: one subtracted instead of dividing.",
      "C: halved instead of divided by 8.",
      "D: divided by 9.",
    ],
  },

  // ================================================ PROBABILITY AND STATISTICS
  {
    sig: "sample-space-with-replacement",
    code: "SAAT-M-STA.25", ses: 43, lvl: 3,
    stem: "A card is drawn from 6 numbered cards, replaced, and a second card is drawn. How many outcomes are in the sample space?",
    opts: [
      "15",
      "36",
      "30",
      "12"
    ],
    ans: 1,
    trick: "WITH replacement the second draw has the full set available again, so the count is n² — without replacement it would be n(n − 1), and that smaller number is always offered",
    why: "6 × 6 = 36.",
    traps: [
      "A: the unordered pairs counted.",
      "C: the without-replacement count.",
      "D: the two numbers added as a product of 2.",
    ],
  },
  {
    sig: "probability-from-a-bar-chart",
    code: "SAAT-M-STA.26", ses: 41, lvl: 3,
    stem: "The bar chart below gives the probability distribution of X. What is P(X = 2 or X = 3)?",
    fig: "g_bars", figW: 1.9,
    opts: [
      "0.3",
      "0.12",
      "0.7",
      "0.4"
    ],
    ans: 2,
    trick: "the two outcomes cannot both happen, so their probabilities simply ADD — multiplying is what \"and\" would need, and that product is on the page",
    why: "0.3 + 0.4 = 0.7.",
    traps: [
      "A: only the shorter bar read.",
      "B: the two probabilities multiplied.",
      "D: only the taller bar read.",
    ],
  },
  {
    sig: "skew-from-a-curve",
    code: "SAAT-M-STA.27", ses: 41, lvl: 3,
    stem: "How would you describe the distribution sketched below?",
    fig: "g_skew", figW: 1.85,
    opts: [
      "Skewed to the left",
      "Symmetric",
      "Normal",
      "Skewed to the right"
    ],
    ans: 3,
    trick: "skew is named for the side the long TAIL runs to, not the side the peak sits on — the peak here is on the left, which is exactly why the tail, and the name, go right",
    why: "The peak is near the left and the tail stretches away to the right.",
    traps: [
      "A: the direction named from the peak.",
      "B: a symmetric curve has no tail on either side.",
      "C: a normal curve is symmetric.",
    ],
  },

  // ================================================================ CALCULUS
  {
    sig: "derivative-of-a-linear-function",
    code: "SAAT-M-CAL.52", ses: 95, lvl: 2,
    stem: "What is the derivative of f(x) = −7x + 4?",
    opts: [
      "−7",
      "−7x",
      "4",
      "−3"
    ],
    ans: 0,
    trick: "the derivative of a linear function is its SLOPE, a constant, and the constant term dies — an answer that still contains x has not been differentiated at all",
    why: "f′(x) = −7.",
    traps: [
      "B: the term copied without differentiating.",
      "C: the constant term returned.",
      "D: the two coefficients added.",
    ],
  },
  {
    sig: "second-derivative-of-a-polynomial",
    code: "SAAT-M-CAL.53", ses: 95, lvl: 3,
    stem: "For f(x) = 2x⁵ − 3x² + 9, what is f″(x)?",
    opts: [
      { eq: "g_sd4" },
      { eq: "g_sd1" },
      { eq: "g_sd2" },
      { eq: "g_sd3" }
    ],
    ans: 1,
    trick: "apply the power rule TWICE, bringing a new coefficient down each time — stopping at the first derivative is the commonest slip, and that answer is offered",
    why: "f′ = 10x⁴ − 6x, so f″ = 40x³ − 6.",
    traps: [
      "A: the squared term differentiated only once.",
      "C: the first derivative given.",
      "D: the exponent reduced twice but the coefficient only once.",
    ],
  },
  {
    sig: "antiderivative-of-a-negative-power-denominator",
    code: "SAAT-M-CAL.54", ses: 109, lvl: 4,
    stem: "Find the indefinite integral below.",
    stemEq: "g_ai",
    opts: [
      { eq: "g_ai3" },
      { eq: "g_ai4" },
      { eq: "g_ai1" },
      { eq: "g_ai2" }
    ],
    ans: 2,
    trick: "rewrite the negative power in the DENOMINATOR as a positive power on top before integrating — 4 over x to the minus three is 4x³, and integrating the fraction as it stands is what the wrong options do",
    why: "∫4x³ dx = x⁴ + C.",
    traps: [
      "A: the expression integrated without being rewritten.",
      "B: the power lowered instead of raised when integrating.",
      "D: the constant of integration left off.",
    ],
  },
  {
    sig: "reflection-in-the-line-y-equals-x",
    code: "SAAT-M-GEO.96", ses: 40, lvl: 2,
    stem: "The point (−3, 7) is mapped to (7, −3). Which transformation is this?",
    opts: [
      "A reflection in the x-axis",
      "A reflection in the y-axis",
      "A rotation of 180° about the origin",
      "A reflection in the line y = x"
    ],
    ans: 3,
    trick: "the coordinates were SWAPPED, and only y = x does that — every other option changes a sign in place and leaves the coordinates in their original order",
    why: "(a, b) → (b, a) is reflection in y = x.",
    traps: [
      "A: that would give (−3, −7).",
      "B: that would give (3, 7).",
      "C: that would give (3, −7).",
    ],
  },
  {
    sig: "translate-a-point-left-and-down",
    code: "SAAT-M-GEO.97", ses: 40, lvl: 2,
    stem: "The point (5, −2) is moved 6 units left and 3 units down. Where does it land?",
    opts: [
      { eq: "g_tr1" },
      { eq: "g_tr2" },
      { eq: "g_tr3" },
      { eq: "g_tr4" }
    ],
    ans: 0,
    trick: "LEFT subtracts from x and DOWN subtracts from y — unlike a function transformation, a point moves in the direction the words say, with no sign reversal anywhere",
    why: "(5 − 6, −2 − 3) = (−1, −5).",
    traps: [
      "B: the shifts applied to the wrong coordinates.",
      "C: both shifts added instead of subtracted.",
      "D: only the horizontal shift applied.",
    ],
  },
];
