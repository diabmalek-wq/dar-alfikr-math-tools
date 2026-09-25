// ---------------------------------------------------------------------------
// SAAT (TAHSILI) MATHEMATICS — MASTER SKILL MAP
//
// WHAT THIS IS. One row per session of the department's 45-week Tahsili course
// (15 units, 135 sessions), carrying the session title VERBATIM from the
// syllabus and, under it, the testable skills the question bank must hold for
// that session. The skills were extracted from two sources plus the bank the
// department already has:
//
//   BOOK   a commercial Tahsili preparation book, mathematics section, 17
//          chapters (book pages 92-177). Skills and tricks only — no stem,
//          number set, option list or figure from it is ever reproduced.
//   SHEET  a handwritten Arabic formula compendium covering the whole
//          secondary syllabus. Standard formulas, used as a memorisation
//          checklist, rewritten in English.
//   BANK   saat_items_a.js, 74 items over 37 skills, already built.
//
// FIELDS
//   s      session number, 1-135          u  unit        w  week
//   title  the syllabus session title, quoted verbatim — never paraphrased
//   obj    the skills an item can be written on, one line each
//   src    which source chapter the skills came from
//   sigs   signatures of the Part A items that already cover this session
//   kind   "skill" a teaching session that needs items
//          "practice" a Tahsili-style session that DRAWS from the pool
//          "assess" a benchmark, mock, review or diagnostic — draws, never adds
//
// HOW TO READ THE COVERAGE. A session with an empty `sigs` has nothing in the
// bank yet. The build target is two items per skill line: one plain, one with
// the trick turned, which is the shape Part A already uses.
// ---------------------------------------------------------------------------
module.exports = [

// ============================== PHASE 1 — GRADE 11 TERM 2 (weeks 1-15) ======
// UNIT 1 — Number, Algebra & Algebraic Reasoning
{ s: 1, u: 1, w: 1, kind: "skill", title: "Real numbers & their properties", src: "BOOK ch05",
  obj: ["Classify a number into N, W, Z, Q, I, R and name the smallest set containing it",
        "Name the property used in a written step: commutative, associative, distributive, identity, inverse",
        "Additive and multiplicative inverse of a given number, including a fraction",
        "Closure: decide whether a set is closed under a stated operation"], sigs: [] },

{ s: 2, u: 1, w: 1, kind: "skill", title: "Rational & irrational numbers", src: "BOOK ch05",
  obj: ["Decide whether a given surd, decimal or root is rational or irrational",
        "Recognise a repeating decimal as rational and a non-terminating non-repeating one as irrational",
        "Classify a product or sum such as √2 × √8 whose form hides a rational value",
        "Place an irrational number between two consecutive integers"], sigs: [] },

{ s: 3, u: 1, w: 1, kind: "skill", title: "Exponents & radicals", src: "BOOK ch07",
  obj: ["Apply the laws of indices to simplify a product or quotient of powers",
        "Convert between radical form and rational-exponent form",
        "Simplify a radical with an even index using absolute value",
        "Multiply and divide radicals of the same index; simplify √a·√b and √(a/b)",
        "Rationalise a denominator, including a two-term denominator by its conjugate"], sigs: [] },

{ s: 4, u: 1, w: 2, kind: "skill", title: "Scientific notation", src: "BOOK ch05",
  obj: ["Write an ordinary decimal in scientific notation and back",
        "Multiply and divide numbers in scientific notation and renormalise the result",
        "Compare two numbers written in scientific notation"],
  sigs: ["scientific-notation-to-decimal", "scientific-notation-product"] },

{ s: 5, u: 1, w: 2, kind: "skill", title: "Algebraic expressions & operations", src: "BOOK ch06",
  obj: ["Degree and leading coefficient of a polynomial in one or more variables",
        "Add, subtract and multiply polynomials; expand a product of binomials",
        "Simplify an expression with negative and fractional exponents",
        "Evaluate an expression at given values, including a squared substitution"], sigs: [] },

{ s: 6, u: 1, w: 2, kind: "skill", title: "Factoring polynomials", src: "BOOK ch06",
  obj: ["Common factor, difference of two squares, sum and difference of cubes",
        "Factor a trinomial with leading coefficient 1 and with a leading coefficient",
        "Decide whether a polynomial is prime",
        "Factor by grouping"], sigs: [] },

{ s: 7, u: 1, w: 3, kind: "skill", title: "Algebraic fractions", src: "BOOK ch07",
  obj: ["Simplify a rational expression by factoring numerator and denominator",
        "Multiply, divide, add and subtract rational expressions",
        "Simplify a complex fraction",
        "State the values that make a rational expression undefined",
        "Find the LCM of two polynomials"], sigs: [] },

{ s: 8, u: 1, w: 3, kind: "skill", title: "Linear equations & inequalities", src: "BOOK ch05",
  obj: ["Solve a linear equation with fractions or brackets",
        "Solve a linear inequality and express the solution as an interval",
        "Reverse the inequality sign when multiplying or dividing by a negative",
        "Write an interval in set-builder notation and read one off a number line",
        "Test whether a point satisfies a linear inequality or a system of them"], sigs: [] },

{ s: 9, u: 1, w: 3, kind: "skill", title: "Absolute-value equations & inequalities", src: "BOOK ch05",
  obj: ["Solve |ax + b| = c, including the no-solution case c < 0",
        "Solve |ax + b| < c as a double inequality and |ax + b| > c as two branches",
        "Domain and range of f(x) = |x − a| + b",
        "Recognise the parent function of an absolute-value graph and its transformations"],
  sigs: ["parent-absolute-value-function", "absolute-value-transformation-rule"] },

// UNIT 2 — Equations, Systems & Quadratics
{ s: 10, u: 2, w: 4, kind: "skill", title: "Systems of linear equations", src: "BOOK ch05",
  obj: ["Solve a 2x2 system by substitution and by elimination",
        "Solve a 2x2 system with the inverse matrix and with determinants",
        "Order of a matrix, the element a_ij, and when a product is defined",
        "Matrix addition, scalar multiplication and multiplication of two matrices",
        "Determinant of a 2x2 and of a 3x3 matrix; the inverse of a 2x2",
        "The value of a parameter that makes a matrix singular"],
  sigs: ["matrix-inverse-2x2", "solve-2x2-system-by-inverse", "matrix-product-order",
         "matrix-product-defined", "singular-matrix-parameter", "zero-determinant-meaning"] },

{ s: 11, u: 2, w: 4, kind: "skill", title: "Systems in context & number of solutions", src: "BOOK ch05",
  obj: ["Decide whether a system has one solution, none, or infinitely many, from slopes or from the equations",
        "Build a system from a worded situation in SAR and solve it",
        "Read the vertices of a feasible region and identify which point satisfies every constraint",
        "Area of a triangle from the coordinates of its vertices using a determinant"], sigs: [] },

{ s: 12, u: 2, w: 4, kind: "skill", title: "Quadratic equations by factoring", src: "BOOK ch06",
  obj: ["Solve a quadratic by factoring and by the zero-product property",
        "Form a quadratic from its two roots",
        "Solve an equation that becomes quadratic after clearing a fraction",
        "Interpret a factored form as the zeros of the related function"], sigs: [] },

{ s: 13, u: 2, w: 5, kind: "skill", title: "Completing the square & the quadratic formula", src: "BOOK ch06",
  obj: ["Complete the square to write ax² + bx + c in vertex form",
        "Solve a quadratic by the formula, including a complex pair",
        "Read the vertex, axis of symmetry and maximum or minimum from the completed square",
        "Recover b or c from a given vertex"], sigs: [] },

{ s: 14, u: 2, w: 5, kind: "skill", title: "The discriminant & nature of roots", src: "BOOK ch06",
  obj: ["Compute b² − 4ac and name the nature of the roots in each of the three cases",
        "Decide from the discriminant whether the roots are rational or irrational",
        "Find the parameter that gives equal roots, or complex roots",
        "Match a graph to the sign of the discriminant"], sigs: [] },

{ s: 15, u: 2, w: 5, kind: "skill", title: "Quadratic functions & their graphs", src: "BOOK ch06, ch11",
  obj: ["Direction of opening, vertex, axis of symmetry and intercepts from any form",
        "Maximum or minimum value and where it occurs",
        "Number of real zeros from a sketch",
        "Match a parabola to its equation"], sigs: [] },

{ s: 16, u: 2, w: 6, kind: "skill", title: "Polynomial equations", src: "BOOK ch06",
  obj: ["Synthetic division and the quotient it produces",
        "Remainder theorem: the remainder on dividing by (x − r) is f(r)",
        "Factor theorem: decide whether (x − r) is a factor",
        "Find a parameter k from a stated remainder",
        "Number of complex roots of a degree-n polynomial; conjugate root pairs",
        "Read the real zeros of a polynomial from its graph or from a table of values"], sigs: [] },

{ s: 17, u: 2, w: 6, kind: "skill", title: "Rational equations", src: "BOOK ch07",
  obj: ["Solve a rational equation by clearing denominators and reject values outside the domain",
        "Solve a proportion, including one with a binomial denominator",
        "Direct, inverse, joint and combined variation: find the constant and a missing value",
        "Identify the type of variation from a table or from an equation"], sigs: [] },

{ s: 18, u: 2, w: 6, kind: "skill", title: "Radical equations", src: "BOOK ch07",
  obj: ["Solve an equation with one radical by raising both sides to the index",
        "Solve an equation with a radical on each side",
        "Identify and reject an extraneous root",
        "Solve a radical inequality, using the domain of the radicand"], sigs: [] },

// UNIT 3 — Functions & Modeling
{ s: 19, u: 3, w: 7, kind: "skill", title: "Relations & functions", src: "BOOK ch05",
  obj: ["Decide whether a relation given as a set, a mapping diagram, a table or an equation is a function",
        "Apply the vertical line test to a graph",
        "Distinguish a one-to-one function from a many-to-one function"], sigs: [] },

{ s: 20, u: 3, w: 7, kind: "skill", title: "Domain & range", src: "BOOK ch05, ch07, ch11",
  obj: ["Domain of a rational function from the zeros of its denominator",
        "Domain and range of a radical function",
        "Domain and range read from a graph, in interval notation",
        "Range of a linear function on a restricted domain",
        "Domain and range of the greatest-integer and absolute-value functions"], sigs: [] },

{ s: 21, u: 3, w: 7, kind: "skill", title: "Function notation", src: "BOOK ch05",
  obj: ["Evaluate f(a), f(−a), f(a + 1) and f(2a) for a given rule",
        "Evaluate a piecewise function at a value in each branch",
        "Solve f(x) = k for x",
        "Find a parameter from a stated function value"], sigs: [] },

{ s: 22, u: 3, w: 8, kind: "skill", title: "Graphs of functions", src: "BOOK ch11",
  obj: ["Read intercepts, and solve f(x) = 0, from a graph",
        "Intervals where a function is increasing, decreasing or constant",
        "Absolute and local maxima and minima from a graph",
        "Decide even, odd or neither, algebraically and from symmetry",
        "Recover the rule of a piecewise function from its graph"],
  sigs: ["odd-function-identification", "classify-even-odd-neither"] },

{ s: 23, u: 3, w: 8, kind: "skill", title: "Transformations of functions", src: "BOOK ch11",
  obj: ["Name the parent function of a given rule or graph",
        "Horizontal and vertical translations: g(x) = f(x − h) + k",
        "Reflection in the x-axis, −f(x), and in the y-axis, f(−x)",
        "Vertical stretch and compression",
        "Combine two or more transformations in the stated order"], sigs: [] },

{ s: 24, u: 3, w: 8, kind: "skill", title: "Inverse functions", src: "BOOK ch07",
  obj: ["Find the inverse of a linear, quadratic-with-restriction or radical function",
        "Verify a pair of inverses by composition",
        "Domain of f inverse equals the range of f",
        "Recognise the graph of an inverse as a reflection in y = x"], sigs: [] },

{ s: 25, u: 3, w: 9, kind: "skill", title: "Composite functions", src: "BOOK ch07",
  obj: ["Evaluate f(g(a)) and g(f(a)), including from a table or a set of ordered pairs",
        "Form the rule of f∘g and state its domain",
        "Solve f(g(x)) = g(f(x))",
        "Find a parameter from a stated value of a composition"],
  sigs: ["composition-equality-solve", "composition-evaluate-order"] },

{ s: 26, u: 3, w: 9, kind: "skill", title: "Modeling with functions", src: "BOOK ch06, SHEET",
  obj: ["Build a linear or quadratic model from a worded situation in SAR and answer with it",
        "Express an area or a volume as a polynomial in one variable",
        "Units of a derived quantity by cancelling units of the quantities it is built from",
        "Choose which of four expressions has the units of a stated quantity"],
  sigs: ["units-of-a-product", "units-identify-quantity"] },

{ s: 27, u: 3, w: 9, kind: "practice", title: "Tahsili-style function problems", src: "—",
  obj: ["Draws from Unit 3; no new skills"], sigs: [] },

// UNIT 4 — Geometry & Measurement
{ s: 28, u: 4, w: 10, kind: "skill", title: "Points, lines, planes & angles", src: "BOOK ch01",
  obj: ["Name angle pairs at a transversal: corresponding, alternate interior, alternate exterior, co-interior",
        "Find an unknown angle from a pair of parallel lines cut by a transversal",
        "Complementary, supplementary and vertically opposite angles",
        "Segment addition: AB + BC = AC and the betweenness it implies"], sigs: [] },

{ s: 29, u: 4, w: 10, kind: "skill", title: "Properties of triangles", src: "BOOK ch02",
  obj: ["Angle sum of a triangle and the exterior angle theorem",
        "Classify a triangle by its angles and by its sides",
        "Base angles of an isosceles triangle; every angle of an equilateral triangle is 60°",
        "Perpendicular bisector and angle bisector theorems",
        "Median, altitude, angle bisector and midsegment — tell them apart in a figure",
        "Centroid divides each median in the ratio 2 : 1",
        "Triangle inequality, and the range of the third side",
        "Longest side faces the largest angle"], sigs: [] },

{ s: 30, u: 4, w: 10, kind: "skill", title: "Congruence & similarity", src: "BOOK ch02, ch03",
  obj: ["Name the congruence postulate a marked figure shows: SSS, SAS, ASA, AAS",
        "Find a length or an angle from a stated congruence",
        "Similar triangles by AA, SSS and SAS; find the scale factor",
        "Ratio of perimeters equals the scale factor; ratio of areas is its square",
        "Triangle proportionality theorem with a line parallel to one side",
        "Angle-bisector ratio theorem",
        "Triangle midsegment: parallel to a side and half its length",
        "Shadow and mirror problems solved by similar triangles"], sigs: [] },

{ s: 31, u: 4, w: 11, kind: "skill", title: "Pythagorean theorem", src: "BOOK ch01",
  obj: ["Find a missing side of a right triangle",
        "Recognise the 3-4-5, 5-12-13 and 8-15-17 triples and their multiples",
        "Decide from three sides whether a triangle is right, acute or obtuse",
        "Distance from a point to a line as the length of the perpendicular segment",
        "Apply the theorem inside a rectangle, a rhombus or a cone"], sigs: [] },

{ s: 32, u: 4, w: 11, kind: "skill", title: "Quadrilaterals & polygons", src: "BOOK ch02, ch03",
  obj: ["Properties of a parallelogram, and the conditions that prove one",
        "Rectangle, rhombus and square: which diagonals are equal, which are perpendicular, which bisect the angles",
        "Side of a rhombus from its diagonals; area from the diagonals",
        "Trapezoid midsegment as the average of the two bases, forwards and backwards",
        "Isosceles trapezoid: equal diagonals and equal base angles",
        "Interior angle sum 180(n − 2); one interior angle of a regular polygon",
        "Exterior angles sum to 360°; find n from one exterior angle"],
  sigs: ["rhombus-diagonals-to-side", "rhombus-area-from-diagonals",
         "trapezoid-midsegment-find-base", "trapezoid-midsegment-algebraic"] },

{ s: 33, u: 4, w: 11, kind: "skill", title: "Circles", src: "BOOK ch04",
  obj: ["Circumference and area, forwards and backwards from either one",
        "Central angle, minor and major arc, and arc addition",
        "A diameter perpendicular to a chord bisects the chord and its arc",
        "Inscribed angle is half its intercepted arc; an angle in a semicircle is 90°",
        "Two inscribed angles on the same arc are equal",
        "Opposite angles of a cyclic quadrilateral are supplementary",
        "A tangent is perpendicular to the radius at the point of contact",
        "Two tangents from an external point are equal",
        "Tangent-chord angle is half the intercepted arc",
        "Intersecting chords: AB × BC = DB × BE",
        "Tangent-secant: the tangent squared equals the whole secant times its external part"], sigs: [] },

{ s: 34, u: 4, w: 12, kind: "skill", title: "Perimeter & area", src: "BOOK ch02, ch03, SHEET",
  obj: ["Area and perimeter of triangle, parallelogram, rhombus, trapezoid and circle",
        "Area of a sector and length of an arc, in degrees and in radians",
        "Shaded-region problems: a composite area found by subtraction",
        "Recover a missing length from a given area or perimeter",
        "Effect on area of scaling every length by a factor k"], sigs: [] },

{ s: 35, u: 4, w: 12, kind: "skill", title: "Surface area & volume", src: "BOOK ch01, SHEET",
  obj: ["Volume and surface area of a prism, a cylinder, a pyramid, a cone and a sphere",
        "Slant height of a cone from its radius and height",
        "Volume expressed as a polynomial and the base area recovered from it",
        "Effect on volume of scaling every length by a factor k",
        "Capacity problems in litres and cubic centimetres"], sigs: [] },

{ s: 36, u: 4, w: 12, kind: "skill", title: "Three-dimensional geometry", src: "BOOK ch01, ch14",
  obj: ["Distance between two points in space",
        "Midpoint of a segment in space",
        "Classify a triangle in space by comparing the squares of its side lengths",
        "Diagonal of a rectangular box",
        "Decide whether four points are coplanar or whether three are collinear"],
  sigs: ["classify-triangle-in-3d", "distance-between-points-in-3d"] },

// UNIT 5 — Coordinate Geometry, Statistics & Probability
{ s: 37, u: 5, w: 13, kind: "skill", title: "Coordinate plane, slope & equations of lines", src: "BOOK ch01",
  obj: ["Slope from two points, and the parameter that makes a slope take a stated value",
        "Slope-intercept, point-slope and standard form; convert between them",
        "Equation of a horizontal line and of a vertical line, and their slopes",
        "Read the slope and both intercepts from an equation or a graph",
        "Decide whether a point lies on a given line"], sigs: [] },

{ s: 38, u: 5, w: 13, kind: "skill", title: "Parallel & perpendicular lines", src: "BOOK ch01",
  obj: ["Parallel lines have equal slopes; perpendicular slopes multiply to −1",
        "Equation of the line through a point parallel to a given line",
        "Equation of the line through a point perpendicular to a given line",
        "Decide from two equations whether the lines are parallel, perpendicular or the same line",
        "Distance between two parallel horizontal or vertical lines"], sigs: [] },

{ s: 39, u: 5, w: 13, kind: "skill", title: "Distance & midpoint formulas", src: "BOOK ch01, ch03",
  obj: ["Distance between two points in the plane",
        "Midpoint of a segment, and the missing endpoint from a midpoint",
        "Use distance to classify a triangle or a quadrilateral from its vertices",
        "Coordinate proof: place a figure on the axes and read off the coordinates of a vertex"], sigs: [] },

{ s: 40, u: 5, w: 14, kind: "skill", title: "Transformations in the plane", src: "BOOK ch03",
  obj: ["Reflection in the x-axis, the y-axis, the origin and the line y = x",
        "Translation (x, y) → (x + a, y + b), and the translation that maps one point to another",
        "Rotation about the origin through 90°, 180° and 270° anticlockwise",
        "Rotational symmetry: order and angle for a regular polygon",
        "Dilation with factor k, including 0 < k < 1 and a negative k",
        "Decide which transformations preserve size and which do not"], sigs: [] },

{ s: 41, u: 5, w: 14, kind: "skill", title: "Data representation & measures of centre", src: "BOOK ch09",
  obj: ["Mean, median and mode of a list, and of a frequency table",
        "Choose the best measure of centre when the data carry an outlier",
        "Recover a missing value from a stated mean",
        "Read a bar chart, a histogram or a probability distribution graph and answer with it",
        "Name the study type: survey, observational study or experiment"],
  sigs: [] },

{ s: 42, u: 5, w: 14, kind: "skill", title: "Measures of dispersion & standard deviation", src: "BOOK ch09",
  obj: ["Range, variance and standard deviation of a small data set",
        "Interpret a larger standard deviation as a wider spread",
        "Compare two groups from their means and standard deviations",
        "Empirical rule: the 68, 95 and 99.7 percentages within one, two and three standard deviations",
        "Find a count or a percentage above, below or between two values of a normal variable",
        "Recover the mean or the standard deviation from a stated percentage",
        "Name a distribution as symmetric, positively skewed or negatively skewed",
        "Margin of error from a sample size"],
  sigs: ["normal-one-standard-deviation", "normal-tail-percentage"] },

{ s: 43, u: 5, w: 15, kind: "skill", title: "Probability, sample spaces & counting principles", src: "BOOK ch09",
  obj: ["Size of a sample space by the fundamental counting principle",
        "Probability of an event from equally likely outcomes",
        "Probability of the complement",
        "Mutually exclusive events: P(A or B) = P(A) + P(B); the correction term when they are not",
        "Geometric probability from a length ratio and from an area ratio",
        "Independent events: P(A and B) = P(A)P(B), with replacement and without"], sigs: [] },

{ s: 44, u: 5, w: 15, kind: "skill", title: "Permutations, combinations & conditional probability", src: "BOOK ch09",
  obj: ["Factorial, and an equation in n involving factorials",
        "Permutations nPr, and permutations with repeated letters",
        "Circular permutations, with and without a fixed reference point",
        "Combinations nCr, and when order does not matter",
        "Probability built from a combination count, such as drawing r of one colour",
        "Conditional probability from a shrunken sample space and from a two-way table",
        "Binomial probability, and the mean, variance and standard deviation of a binomial variable"],
  sigs: ["conditional-probability-dice", "conditional-probability-subgroup"] },

{ s: 45, u: 5, w: 15, kind: "assess", title: "Grade 11 Tahsili Benchmark", src: "—",
  obj: ["Timed Tahsili-format paper over Units 1-5; draws from the bank"], sigs: [] },

// ============================== PHASE 2 — GRADE 12 TERM 1 (weeks 16-33) =====
// UNIT 6 — Exponential & Logarithmic Functions
{ s: 46, u: 6, w: 16, kind: "assess", title: "Retrieval diagnostic: Phase 1 foundations", src: "—",
  obj: ["Draws from Units 1-5"], sigs: [] },

{ s: 47, u: 6, w: 16, kind: "skill", title: "Exponential functions & their graphs", src: "BOOK ch12",
  obj: ["Domain, range and the y-intercept of f(x) = b^x",
        "Decide growth or decay from the base",
        "Horizontal asymptote, and the effect of a vertical shift on it",
        "Match an exponential graph to its rule"], sigs: [] },

{ s: 48, u: 6, w: 16, kind: "skill", title: "Exponential equations", src: "BOOK ch12",
  obj: ["Solve by writing both sides to the same base",
        "Solve an equation whose bases are powers of one another, such as 4 and 2 or 8 and 16",
        "Solve an exponential inequality, reversing the sign when the base is between 0 and 1",
        "Find the parameter that makes an exponential expression take a stated value"], sigs: [] },

{ s: 49, u: 6, w: 17, kind: "skill", title: "Logarithmic functions & their graphs", src: "BOOK ch12",
  obj: ["Domain, range and the x-intercept of f(x) = log_b x",
        "Domain of a shifted logarithm from the inequality x − h > 0",
        "Vertical asymptote of a logarithmic function",
        "The logarithmic function as the inverse of the exponential, and the graph that shows it"], sigs: [] },

{ s: 50, u: 6, w: 17, kind: "skill", title: "Laws of logarithms", src: "BOOK ch12",
  obj: ["Convert between exponential and logarithmic form",
        "Evaluate a logarithm as the power the base must be raised to, including fractional and negative results",
        "Product, quotient and power laws; write several logarithms as one",
        "Expand a single logarithm into a sum and difference",
        "Change of base, and a logarithm evaluated from two given values"],
  sigs: ["log-evaluate-perfect-power", "log-solve-for-unknown-base", "combine-logs-into-one",
         "expand-single-log", "log-linear-combination", "change-of-base"] },

{ s: 51, u: 6, w: 17, kind: "skill", title: "Logarithmic equations", src: "BOOK ch12",
  obj: ["Solve log_b A = log_b B by equating the arguments, then reject values outside the domain",
        "Solve an equation with a logarithm on one side only",
        "Solve a nested logarithm",
        "Solve a logarithmic inequality using the domain of both sides"], sigs: [] },

{ s: 52, u: 6, w: 18, kind: "skill", title: "Exponential–logarithmic systems", src: "BOOK ch12",
  obj: ["Solve a system with one exponential and one logarithmic equation",
        "Composition of a logarithmic and an exponential function",
        "Find the inverse of a logarithmic or an exponential function"], sigs: [] },

{ s: 53, u: 6, w: 18, kind: "skill", title: "Applications: growth, decay & interest", src: "BOOK ch12, SHEET",
  obj: ["Compound interest, and the number of periods needed to reach a target in SAR",
        "Exponential growth or decay from a stated rate, and half-life",
        "Average rate of change of a logarithmic function over an interval"], sigs: [] },

{ s: 54, u: 6, w: 18, kind: "practice", title: "Tahsili-style exponential & logarithmic problems", src: "—",
  obj: ["Draws from Unit 6"], sigs: [] },

// UNIT 7 — Sequences, Series & Complex Numbers
{ s: 55, u: 7, w: 19, kind: "skill", title: "Mathematical patterns & relationships", src: "BOOK ch08",
  obj: ["Continue a numerical or figural pattern and state its rule",
        "Decide whether a sequence is arithmetic, geometric or neither",
        "Find the next term of a sequence given as a graph or a table"], sigs: [] },

{ s: 56, u: 7, w: 19, kind: "skill", title: "Arithmetic sequences & series", src: "BOOK ch08",
  obj: ["Common difference, and the nth term a_n = a_1 + (n − 1)d",
        "Find a_1 or d from two given terms",
        "Insert arithmetic means between two numbers",
        "Sum of n terms, from the last term and from the common difference",
        "Find n from a given sum, and solve a worded growth situation"], sigs: [] },

{ s: 57, u: 7, w: 19, kind: "skill", title: "Geometric sequences & series", src: "BOOK ch08",
  obj: ["Common ratio, and the nth term a_n = a_1 r^(n−1)",
        "Find r or a_1 from two given terms",
        "Insert geometric means between two numbers",
        "Sum of n terms of a geometric series",
        "Worded halving and doubling situations"], sigs: [] },

{ s: 58, u: 7, w: 20, kind: "skill", title: "Infinite geometric series", src: "BOOK ch08",
  obj: ["Decide convergence from |r| < 1",
        "Sum to infinity S = a_1 ÷ (1 − r)",
        "Find a_1 or r from a stated infinite sum",
        "Find the values of x for which a series in x converges"], sigs: [] },

{ s: 59, u: 7, w: 20, kind: "skill", title: "Sigma notation & applications", src: "BOOK ch08",
  obj: ["Number of terms of a sum written in sigma notation, and its first and last terms",
        "Evaluate an arithmetic or a geometric sum written in sigma notation",
        "Rewrite a listed series in sigma notation",
        "Binomial theorem: number of terms, the general term, the term in a stated power, and the constant term"],
  sigs: ["binomial-coefficient-of-a-term", "binomial-nth-term-index"] },

{ s: 60, u: 7, w: 20, kind: "skill", title: "Sequence-based reasoning problems", src: "BOOK ch08",
  obj: ["Angles of a polygon that form an arithmetic sequence",
        "A worded situation where a fixed increase competes with a fixed multiplier",
        "Compare an arithmetic and a geometric model over the same number of steps"], sigs: [] },

{ s: 61, u: 7, w: 21, kind: "skill", title: "Complex numbers & operations", src: "BOOK ch06",
  obj: ["Powers of i by the remainder on division by 4",
        "Simplify the square root of a negative number",
        "Add, subtract and multiply complex numbers; expand a square",
        "Divide by multiplying by the conjugate of the denominator",
        "Equality of two complex numbers: match real and imaginary parts"],
  sigs: ["complex-square", "complex-quotient-conjugate"] },

{ s: 62, u: 7, w: 21, kind: "skill", title: "Complex roots & the quadratic connection", src: "BOOK ch06",
  obj: ["Solve a quadratic with a negative discriminant",
        "Conjugate root pairs, and the least degree of a polynomial with given complex zeros",
        "Count the imaginary roots of a polynomial equation such as x⁴ − k = 0",
        "Number of complex roots of a degree-n equation"], sigs: [] },

{ s: 63, u: 7, w: 21, kind: "practice", title: "Tahsili-style sequences & complex numbers", src: "—",
  obj: ["Draws from Unit 7"], sigs: [] },

// UNIT 8 — Trigonometry I
{ s: 64, u: 8, w: 22, kind: "skill", title: "Right-triangle trigonometry", src: "BOOK ch10",
  obj: ["Find a side or an angle of a right triangle from a given ratio",
        "Angle of elevation and angle of depression",
        "Two-triangle height and shadow problems",
        "Area of a right triangle used to recover a missing side"], sigs: [] },

{ s: 65, u: 8, w: 22, kind: "skill", title: "Sine, cosine & tangent", src: "BOOK ch10",
  obj: ["The three ratios and their reciprocals cosecant, secant and cotangent",
        "Given one ratio, find the other five",
        "Simplify a product such as sin θ × cot θ",
        "Values that make a reciprocal ratio undefined"], sigs: [] },

{ s: 66, u: 8, w: 22, kind: "skill", title: "Special right triangles", src: "BOOK ch10",
  obj: ["Exact ratios at 30°, 45° and 60° and the two special triangles they come from",
        "Find a side using the 30-60-90 relationship without a calculator",
        "Exact value of an expression built from special angles"], sigs: [] },

{ s: 67, u: 8, w: 23, kind: "skill", title: "Degree & radian measure", src: "BOOK ch10",
  obj: ["Convert degrees to radians and radians to degrees",
        "Coterminal angles by adding or subtracting a full turn",
        "Arc length s = rθ in radians and the degree version",
        "Area of a sector in both measures",
        "Angle turned in a stated time by a rotating object"], sigs: [] },

{ s: 68, u: 8, w: 23, kind: "skill", title: "Unit-circle concepts", src: "BOOK ch10",
  obj: ["Coordinates on the unit circle as (cos θ, sin θ)",
        "Signs of the six ratios in each quadrant",
        "Quadrant of an angle from the signs of two ratios",
        "Values of the ratios at the quadrantal angles"],
  sigs: ["quadrant-both-negative", "quadrant-from-two-signs"] },

{ s: 69, u: 8, w: 23, kind: "skill", title: "Trigonometric ratios of any angle", src: "BOOK ch10",
  obj: ["Reference angle in each quadrant, and the sign attached to it",
        "Exact value of a ratio at an angle beyond 90°, positive or negative",
        "Ratios from a point (x, y) on the terminal side, with r = √(x² + y²)",
        "Given one ratio and a quadrant, find another"], sigs: [] },

{ s: 70, u: 8, w: 24, kind: "skill", title: "Graphs of trigonometric functions", src: "BOOK ch10",
  obj: ["Shape, domain and range of the sine, cosine and tangent graphs",
        "Match a graph to its rule",
        "Read the maximum, minimum and zeros from a trigonometric graph"], sigs: [] },

{ s: 71, u: 8, w: 24, kind: "skill", title: "Amplitude, period & phase shift", src: "BOOK ch10",
  obj: ["Amplitude |a| and period 360°/|b| or 2π/|b| for sine and cosine",
        "Period 180°/|b| for the tangent, which has no amplitude",
        "Find b from a stated period",
        "Vertical and horizontal shift of a trigonometric graph"], sigs: [] },

{ s: 72, u: 8, w: 24, kind: "practice", title: "Tahsili-style trigonometric graphs", src: "—",
  obj: ["Draws from Unit 8"], sigs: [] },

// UNIT 9 — Trigonometry II
{ s: 73, u: 9, w: 25, kind: "skill", title: "Fundamental trigonometric identities", src: "BOOK ch10",
  obj: ["Quotient identities and reciprocal identities",
        "The three Pythagorean identities and the two derived by dividing",
        "Simplify an expression to a single ratio",
        "Find a second ratio from a first using an identity and a quadrant",
        "Cofunction identities and the even-odd identities"],
  sigs: ["simplify-sin-squared-over-tan-squared", "simplify-with-pythagorean-identity"] },

{ s: 74, u: 9, w: 25, kind: "skill", title: "Sum, difference & double-angle identities", src: "BOOK ch10",
  obj: ["sin(A ± B), cos(A ± B) and tan(A ± B), with attention to the reversed sign in the cosine",
        "Exact value of a ratio at 15°, 75° or 105° by splitting the angle",
        "Recognise a written expression as an expanded sum or difference identity",
        "The three forms of cos 2θ, and sin 2θ and tan 2θ",
        "Evaluate a double angle from a given ratio and quadrant"],
  sigs: ["double-angle-identity-recognise", "double-angle-value-from-sine"] },

{ s: 75, u: 9, w: 25, kind: "skill", title: "Proving identities", src: "BOOK ch10",
  obj: ["Show two expressions are equal by working one side into the other",
        "Choose which identity removes the mixed terms",
        "Recognise an expression that is NOT an identity by a counterexample"], sigs: [] },

{ s: 76, u: 9, w: 26, kind: "skill", title: "Basic trigonometric equations", src: "BOOK ch10",
  obj: ["Solve sin θ = k, cos θ = k, tan θ = k on 0° to 360°, giving every solution",
        "Solve an equation that factors into two trigonometric factors",
        "Solve a quadratic in sin θ or cos θ",
        "Inverse trigonometric functions and their principal values"], sigs: [] },

{ s: 77, u: 9, w: 26, kind: "skill", title: "Laws of Sines & Cosines", src: "BOOK ch10",
  obj: ["Law of sines to find a side or an angle",
        "Law of cosines for three sides, and for two sides and the included angle",
        "Find the largest angle of a triangle, and read an obtuse angle from a negative cosine",
        "Choose which law the given information calls for"],
  sigs: ["law-of-cosines-perimeter", "law-of-cosines-largest-angle"] },

{ s: 78, u: 9, w: 26, kind: "skill", title: "Applications of trigonometry", src: "BOOK ch10",
  obj: ["Area of a triangle from two sides and the included angle",
        "Recover an angle or a side from a stated area",
        "Bearings, heights and distances in a worded setting",
        "A quadrilateral split into two triangles"],
  sigs: ["triangle-area-two-sides-and-angle", "find-included-angle-from-area"] },

{ s: 79, u: 9, w: 27, kind: "skill", title: "Vectors & their basic applications", src: "BOOK ch14",
  obj: ["Equal, parallel and opposite vectors",
        "Resultant by the triangle and the parallelogram rule; magnitude of a perpendicular resultant",
        "Resolve a vector into horizontal and vertical components, N cos θ and N sin θ",
        "Component form of AB from two points, and the magnitude of a vector",
        "Add, subtract and scale vectors; find a linear combination such as 2A − B",
        "Unit vector in the direction of a vector, and the i, j form",
        "Direction angle of a vector",
        "Dot product, the angle between two vectors, and the perpendicularity condition",
        "Vectors in space: components, magnitude, dot product",
        "Cross product, the area of a parallelogram, and the scalar triple product as a volume"],
  sigs: ["vector-linear-combination", "vector-magnitude", "dot-product-perpendicular", "dot-product-value"] },

{ s: 80, u: 9, w: 27, kind: "skill", title: "Polar & parametric concepts", src: "BOOK ch15",
  obj: ["Plot a polar point and give three other names for the same point",
        "Convert polar to Cartesian and Cartesian to polar, keeping the quadrant",
        "A negative r sends the point to the opposite side of the pole",
        "Convert a simple equation between polar and Cartesian form",
        "Distance between two points in polar form",
        "Modulus and argument of a complex number, and its polar form",
        "De Moivre's theorem for a power, and products and quotients in polar form"],
  sigs: ["polar-to-cartesian-negative-r", "cartesian-to-polar-on-axis",
         "de-moivre-power", "de-moivre-modulus-argument"] },

{ s: 81, u: 9, w: 27, kind: "practice", title: "Tahsili-style trigonometry problems", src: "—",
  obj: ["Draws from Unit 9"], sigs: [] },

// UNIT 10 — Analytic Geometry & Conic Sections
{ s: 82, u: 10, w: 28, kind: "skill", title: "Circles in the coordinate plane", src: "BOOK ch04",
  obj: ["Equation of a circle from its centre and radius, and the reverse",
        "Complete the square to find the centre and radius from a general equation",
        "Decide whether a given point lies on a circle",
        "Condition for a circle to touch an axis",
        "Recognise which of four equations is a circle"], sigs: [] },

{ s: 83, u: 10, w: 28, kind: "skill", title: "Parabolas", src: "BOOK ch13",
  obj: ["Vertex, focus, directrix and axis of symmetry from the standard form",
        "Direction of opening from which variable is squared and the sign of 4c",
        "Length of the focal chord, |4c|",
        "Write the equation from a vertex and a directrix, or from a focus and a directrix",
        "Distance from the focus to the directrix",
        "Complete the square to reach standard form"],
  sigs: ["parabola-orientation", "parabola-vertex-and-direction"] },

{ s: 84, u: 10, w: 28, kind: "skill", title: "Ellipses", src: "BOOK ch13",
  obj: ["Centre, vertices, co-vertices and foci for a horizontal and a vertical major axis",
        "Lengths of the major and minor axes from the equation",
        "The relation c² = a² − b²",
        "Eccentricity e = c/a, and what e = 0 means",
        "Match an ellipse to its equation"], sigs: [] },

{ s: 85, u: 10, w: 29, kind: "skill", title: "Hyperbolas", src: "BOOK ch13",
  obj: ["Centre, vertices and foci for a horizontal and a vertical transverse axis",
        "The relation c² = a² + b²",
        "Equations of the asymptotes",
        "Eccentricity, which is greater than 1",
        "Write the equation from a centre, a focus and an axis length"], sigs: [] },

{ s: 86, u: 10, w: 29, kind: "skill", title: "Identifying conics from their equations", src: "BOOK ch13",
  obj: ["Classify by the discriminant B² − 4AC",
        "Classify from the coefficients of x² and y²: equal, unequal same sign, opposite signs, one missing",
        "Recognise the case where an ellipse degenerates to a circle"], sigs: [] },

{ s: 87, u: 10, w: 29, kind: "skill", title: "Conics in context", src: "BOOK ch13",
  obj: ["A parabolic arch or dish: find the focus or a height from the equation",
        "An elliptical room or orbit: find a distance from the centre or a focus",
        "Build the equation from a described physical setting"], sigs: [] },

{ s: 88, u: 10, w: 30, kind: "skill", title: "Mixed analytic geometry problems", src: "BOOK ch01, ch03, ch13",
  obj: ["Combine slope, distance and midpoint in one multi-step problem",
        "Image of a conic or a point under a reflection followed by a rotation",
        "Find a vertex of a figure from the conditions its sides satisfy"], sigs: [] },

{ s: 89, u: 10, w: 30, kind: "skill", title: "Geometric relationships & reasoning", src: "BOOK ch02, ch03",
  obj: ["Decide which single piece of extra information proves a stated conclusion",
        "Judge whether a general statement about a figure is always, sometimes or never true",
        "Find the counterexample that refutes a stated claim"], sigs: [] },

{ s: 90, u: 10, w: 30, kind: "practice", title: "Tahsili-style analytic geometry", src: "—",
  obj: ["Draws from Unit 10"], sigs: [] },

// UNIT 11 — Limits & Derivatives
{ s: 91, u: 11, w: 31, kind: "skill", title: "Limits & limit laws", src: "BOOK ch16",
  obj: ["Estimate a limit from a graph, including one-sided limits",
        "A limit exists only when the two one-sided limits agree",
        "Evaluate a limit by direct substitution",
        "The 0/0 case: factor and cancel, or multiply by the conjugate",
        "The k/0 case, where the limit does not exist",
        "Find a parameter from a stated limit"],
  sigs: ["limit-removable-discontinuity", "limit-by-rationalising"] },

{ s: 92, u: 11, w: 31, kind: "skill", title: "Continuity", src: "BOOK ch16",
  obj: ["The three conditions for continuity at a point",
        "Name the type of discontinuity: removable, jump or infinite",
        "Find the constant that makes a piecewise function continuous",
        "Locate the discontinuities of a rational function",
        "Intermediate value theorem: a sign change forces a zero, and counting sign changes in a table"],
  sigs: ["count-zeros-by-sign-change", "intermediate-value-statement"] },

{ s: 93, u: 11, w: 31, kind: "skill", title: "Limits at infinity & asymptotes", src: "BOOK ch16",
  obj: ["Limit of a polynomial at infinity from its leading term",
        "Limit of a rational function by comparing the degrees, in all three cases",
        "Horizontal asymptote from a limit at infinity, and vertical asymptotes from the denominator",
        "Describe the end behaviour of a graph in limit notation",
        "Point of discontinuity of a rational function where a factor cancels"], sigs: [] },

{ s: 94, u: 11, w: 32, kind: "skill", title: "The derivative: definition & interpretation", src: "BOOK ch11, ch17",
  obj: ["Average rate of change over an interval as the slope of a chord",
        "The derivative as the limit of the difference quotient",
        "Evaluate a limit of difference-quotient form",
        "The derivative as the slope of the tangent at a point",
        "Where the average rate of change equals the instantaneous rate"],
  sigs: ["average-rate-of-change", "average-rate-equals-instantaneous", "derivative-at-a-point"] },

{ s: 95, u: 11, w: 32, kind: "skill", title: "Power, product & quotient rules", src: "BOOK ch17",
  obj: ["Power rule, including negative and fractional powers and a radical rewritten as a power",
        "Derivative of a constant and of a constant multiple",
        "Derivative of a sum and a difference",
        "Product rule and quotient rule",
        "Second and higher derivatives, and the order at which they vanish"],
  sigs: ["derivative-power-rule", "derivative-radical-and-reciprocal"] },

{ s: 96, u: 11, w: 32, kind: "skill", title: "The chain rule", src: "BOOK ch17",
  obj: ["Differentiate a power of a function",
        "Differentiate a radical of a function",
        "Combine the chain rule with the product or the quotient rule",
        "Evaluate the derivative of a composition at a point"], sigs: [] },

{ s: 97, u: 11, w: 33, kind: "skill", title: "Derivatives of trigonometric, exponential & logarithmic functions", src: "SHEET",
  obj: ["Derivatives of sin x, cos x and tan x, and with the chain rule",
        "Derivative of e^x and of b^x",
        "Derivative of ln x and of log_b x",
        "Combine one of these with the product or quotient rule"], sigs: [] },

{ s: 98, u: 11, w: 33, kind: "skill", title: "Implicit differentiation", src: "SHEET",
  obj: ["Differentiate an equation in x and y and solve for dy/dx",
        "Slope of the tangent to an implicitly defined curve at a point",
        "Differentiate a product of x and y implicitly"], sigs: [] },

{ s: 99, u: 11, w: 33, kind: "practice", title: "Tahsili-style differentiation", src: "—",
  obj: ["Draws from Unit 11"], sigs: [] },

// UNIT 12 — Applications of Derivatives
{ s: 100, u: 12, w: 34, kind: "skill", title: "Tangent lines & rates of change", src: "BOOK ch17",
  obj: ["Slope of the tangent at a point, and the equation of that tangent",
        "Equation of the normal at a point",
        "The point where a curve has a stated tangent slope",
        "Rate of change read from a derivative in a worded setting"],
  sigs: ["tangent-line-equation"] },

{ s: 101, u: 12, w: 34, kind: "skill", title: "Increasing, decreasing & critical points", src: "BOOK ch11, ch17",
  obj: ["Critical points where the derivative is zero or undefined",
        "Sign of the derivative to decide increasing or decreasing",
        "Count the critical points, including a repeated root that gives only one",
        "Read intervals of increase and decrease from a graph"],
  sigs: ["count-critical-points"] },

{ s: 102, u: 12, w: 34, kind: "skill", title: "Maxima & minima", src: "BOOK ch17",
  obj: ["First derivative test for a local maximum or minimum",
        "Second derivative test, where a negative second derivative marks the maximum",
        "Absolute maximum and minimum on a closed interval, testing the endpoints too",
        "Distinguish local from absolute extrema on a graph"],
  sigs: ["maximum-on-closed-interval", "second-derivative-test"] },

{ s: 103, u: 12, w: 35, kind: "skill", title: "Concavity & points of inflection", src: "BOOK ch17",
  obj: ["Concave up and concave down from the sign of the second derivative",
        "Point of inflection where the second derivative changes sign",
        "Tell an inflection point from a turning point"],
  sigs: ["point-of-inflection"] },

{ s: 104, u: 12, w: 35, kind: "skill", title: "Curve sketching", src: "BOOK ch11, ch17",
  obj: ["Assemble intercepts, asymptotes, extrema and concavity into one sketch",
        "Match a function to its graph using its derivative information",
        "Sketch a curve satisfying stated conditions on f, f′ and f″"], sigs: [] },

{ s: 105, u: 12, w: 35, kind: "skill", title: "Optimization problems", src: "BOOK ch17",
  obj: ["Maximum area for a fixed perimeter, and minimum perimeter for a fixed area",
        "Maximum volume of an open box cut from a sheet",
        "Minimum cost or maximum profit in SAR",
        "Write the constraint, substitute, differentiate and check the endpoints"], sigs: [] },

{ s: 106, u: 12, w: 36, kind: "skill", title: "Related rates", src: "SHEET",
  obj: ["Differentiate a relation with respect to time and substitute the known rates",
        "Expanding circle, ladder against a wall, filling cone or cylinder",
        "Keep the units of the answer straight"], sigs: [] },

{ s: 107, u: 12, w: 36, kind: "skill", title: "Motion problems", src: "BOOK ch17",
  obj: ["Velocity as the derivative of displacement and acceleration as its second derivative",
        "Velocity at a stated time, and the time at which the object is at rest",
        "Maximum height of a projectile",
        "Decide whether the object is speeding up or slowing down"], sigs: [] },

{ s: 108, u: 12, w: 36, kind: "practice", title: "Tahsili-style derivative applications", src: "—",
  obj: ["Draws from Unit 12"], sigs: [] },

// UNIT 13 — Integration & Its Applications
{ s: 109, u: 13, w: 37, kind: "skill", title: "Antiderivatives & indefinite integrals", src: "BOOK ch17",
  obj: ["Antiderivative of a power, and the constant of integration",
        "Recover F(x) from a given f′(x)",
        "Antiderivative of a radical rewritten as a power",
        "Find the particular antiderivative through a given point"], sigs: [] },

{ s: 110, u: 13, w: 37, kind: "skill", title: "Basic integration rules", src: "BOOK ch17",
  obj: ["Integral of a constant and of a constant multiple",
        "Integral of a sum and a difference, term by term",
        "Integral of a negative power",
        "Rewrite a product or a quotient into integrable terms before integrating"], sigs: [] },

{ s: 111, u: 13, w: 37, kind: "skill", title: "Integration by substitution", src: "SHEET",
  obj: ["Choose u and compute du",
        "Integrate a power of a function times its derivative",
        "Change the limits when substituting in a definite integral"], sigs: [] },

{ s: 112, u: 13, w: 38, kind: "skill", title: "Definite integrals", src: "BOOK ch17",
  obj: ["Evaluate a definite integral of a polynomial",
        "Find a limit or a parameter from a stated value of a definite integral",
        "Integrate a piecewise or an absolute-value integrand by splitting the interval"],
  sigs: ["evaluate-definite-integral", "definite-integral-of-a-line"] },

{ s: 113, u: 13, w: 38, kind: "skill", title: "The Fundamental Theorem of Calculus", src: "BOOK ch17",
  obj: ["The integral equals F(b) − F(a), in that order",
        "Compute an integral from two given values of an antiderivative",
        "Differentiate an integral with a variable upper limit"],
  sigs: ["fundamental-theorem-statement", "antiderivative-values-to-integral"] },

{ s: 114, u: 13, w: 38, kind: "skill", title: "Properties of definite integrals", src: "BOOK ch17",
  obj: ["An integral from a to a is zero, and reversing the limits changes the sign",
        "Split an integral at an interior point and add",
        "Sum and difference of integrals over the same interval",
        "Combine several given integrals to reach the one asked for"], sigs: [] },

{ s: 115, u: 13, w: 39, kind: "skill", title: "Area under a curve", src: "BOOK ch17",
  obj: ["Area between a curve and the x-axis on an interval",
        "Treat an area below the axis as positive by splitting at the zeros",
        "Read the area of a shaded region from a graph and its integral",
        "Approximate an area by rectangles"], sigs: [] },

{ s: 116, u: 13, w: 39, kind: "skill", title: "Area between curves", src: "SHEET",
  obj: ["Find the intersection points that give the limits",
        "Integrate the upper curve minus the lower curve",
        "Area between a curve and a line",
        "Split the interval where the curves swap positions"], sigs: [] },

{ s: 117, u: 13, w: 39, kind: "practice", title: "Tahsili-style integration problems", src: "—",
  obj: ["Draws from Unit 13"], sigs: [] },

// ============================== PHASE 3 — review and mastery ================
{ s: 118, u: 14, w: 40, kind: "assess", title: "Number & algebra review", src: "—", obj: ["Draws from Units 1, 2, 7"], sigs: [] },
{ s: 119, u: 14, w: 40, kind: "assess", title: "Functions, exponentials & logarithms review", src: "—", obj: ["Draws from Units 3, 6"], sigs: [] },
{ s: 120, u: 14, w: 40, kind: "assess", title: "Mixed algebra–function problems", src: "—", obj: ["Draws from Units 1-3, 6, 7"], sigs: [] },
{ s: 121, u: 14, w: 41, kind: "assess", title: "Geometry & analytic geometry review", src: "—", obj: ["Draws from Units 4, 5, 10"], sigs: [] },
{ s: 122, u: 14, w: 41, kind: "assess", title: "Trigonometry review", src: "—", obj: ["Draws from Units 8, 9"], sigs: [] },
{ s: 123, u: 14, w: 41, kind: "assess", title: "Mixed geometry–trigonometry problems", src: "—", obj: ["Draws from Units 4, 8, 9, 10"], sigs: [] },
{ s: 124, u: 14, w: 42, kind: "assess", title: "Sequences, statistics & probability review", src: "—", obj: ["Draws from Units 5, 7"], sigs: [] },
{ s: 125, u: 14, w: 42, kind: "assess", title: "Calculus review", src: "—", obj: ["Draws from Units 11, 12, 13"], sigs: [] },
{ s: 126, u: 14, w: 42, kind: "assess", title: "Cross-domain mixed problems", src: "—", obj: ["Draws from every unit"], sigs: [] },

{ s: 127, u: 15, w: 43, kind: "assess", title: "Weighted practice: Grade 10 & 11 content (50%)", src: "—", obj: ["Draws from Units 1-5"], sigs: [] },
{ s: 128, u: 15, w: 43, kind: "assess", title: "Weighted practice: Grade 12 content (50%)", src: "—", obj: ["Draws from Units 6-13"], sigs: [] },
{ s: 129, u: 15, w: 43, kind: "assess", title: "Timed mixed-domain set", src: "—", obj: ["Draws from every unit"], sigs: [] },
{ s: 130, u: 15, w: 44, kind: "assess", title: "Full Tahsili Mathematics Mock 1", src: "—", obj: ["Draws from every unit"], sigs: [] },
{ s: 131, u: 15, w: 44, kind: "assess", title: "Mock 1 analysis & error correction", src: "—", obj: ["No items"], sigs: [] },
{ s: 132, u: 15, w: 44, kind: "assess", title: "Targeted intervention", src: "—", obj: ["Draws by skill profile"], sigs: [] },
{ s: 133, u: 15, w: 45, kind: "assess", title: "Full Tahsili Mathematics Mock 2", src: "—", obj: ["Draws from every unit"], sigs: [] },
{ s: 134, u: 15, w: 45, kind: "assess", title: "Mock 2 analysis & final correction", src: "—", obj: ["No items"], sigs: [] },
{ s: 135, u: 15, w: 45, kind: "assess", title: "Final readiness & test-day strategy", src: "—", obj: ["No items"], sigs: [] },

];
