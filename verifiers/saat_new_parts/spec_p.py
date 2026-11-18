# SAAT part P — skills read (skill+trap only) from the 1,105-question teacher booklet pasted 17 Nov 2026.
# Every item: vals[0] is the typed intended key; pred() independently tests every option against the stem.
import math, cmath, statistics
from fractions import Fraction as F
import numpy as np

def m(s): return str(s).replace('-', '−')
def fr(v):
    if isinstance(v, F): return m(v.numerator) if v.denominator == 1 else m(f"{v.numerator}/{v.denominator}")
    return m(v)
def dec(v): return m(('%g' % v))
def pt(v): return m(f"({v[0]}, {v[1]})")

ITEMS = []
def I(sig, unit, topic, lvl, stem, vals, pred, notes, trick, why, fmt=fr):
    ITEMS.append(dict(sig=sig, unit=unit, topic=topic, lvl=lvl, stem=stem, vals=vals, pred=pred, notes=notes, trick=trick, why=why, fmt=fmt))

G = "Transformations & symmetry"; G2 = "Triangles, polygons & quadrilaterals"; G3 = "Circles"; G4 = "Similarity & scale"
L = "Linear equations & lines"

# ---------------- transformations
z = complex(4, 1)
I("rotation-of-a-point-90-degrees-about-the-origin", 4, G, 2,
  "The point (4, 1) is rotated 90° anticlockwise about the origin. What are the coordinates of its image?",
  [(-1, 4), (1, -4), (-4, -1), (1, 4)], lambda v: (round((z*1j).real), round((z*1j).imag)) == v,
  ["B: the rotation was taken clockwise.", "C: a half-turn was applied instead of a quarter-turn.", "D: the coordinates were swapped with no sign change, which is a reflection in y = x."],
  "a quarter-turn anticlockwise sends (x, y) to (−y, x) — swapping with no sign change is a reflection, not a rotation",
  "Multiplying 4 + i by i gives −1 + 4i, so (4, 1) → (−1, 4).", pt)
z2 = complex(-2, 5)
I("rotation-of-a-point-270-degrees-about-the-origin", 4, G, 3,
  "The point (−2, 5) is rotated 270° anticlockwise about the origin. What are the coordinates of its image?",
  [(5, 2), (-5, -2), (2, -5), (-5, 2)], lambda v: (round((z2*(1j**3)).real), round((z2*(1j**3)).imag)) == v,
  ["B: only a 90° anticlockwise turn was applied.", "C: a 180° turn was applied.", "D: the coordinates were swapped and the wrong sign was changed."],
  "270° anticlockwise equals 90° clockwise, which sends (x, y) to (y, −x)",
  "Multiplying −2 + 5i by i³ = −i gives 5 + 2i, so the image is (5, 2).", pt)
I("point-reflection-through-the-origin", 4, G, 1,
  "What is the image of the point (−3, 1) under a reflection through the origin (a point reflection)?",
  [(3, -1), (3, 1), (-3, -1), (1, -3)], lambda v: v == (3, -1),
  ["B: reflected in the y-axis only.", "C: reflected in the x-axis only.", "D: the coordinates were swapped."],
  "a point reflection through the origin negates BOTH coordinates — negating only one is an axis reflection",
  "(x, y) → (−x, −y), so (−3, 1) → (3, −1).", pt)
def two_refl():
    A = np.array([[1, 0], [0, -1]]); B = np.array([[-1, 0], [0, 1]]); R = B @ A
    return round(math.degrees(math.atan2(R[1][0], R[0][0]))) % 360
I("two-axis-reflections-make-a-half-turn", 4, G, 2,
  "A figure is reflected in the x-axis and then in the y-axis. The single transformation that does the same is a rotation about the origin through:",
  [180, 90, 270, 360], lambda v: v % 360 == two_refl(),
  ["B: two reflections were taken to make a quarter-turn.", "C: a three-quarter turn was chosen.", "D: a full turn would leave the figure unchanged, but the figure ends up on the opposite side."],
  "reflecting in two perpendicular lines is the same as turning through TWICE the angle between them — 180° for the axes",
  "The first reflection gives (x, −y), the second gives (−x, −y), which is a half-turn.", lambda v: f"{v}°")
I("translation-rule-from-two-points", 4, G, 2,
  "A translation moves the point A(2, −1) to B(7, 3). Which rule describes it?",
  [(5, 4), (4, 5), (-5, -4), (9, 2)], lambda v: v == (7-2, 3-(-1)),
  ["B: the horizontal and vertical shifts were swapped.", "C: the rule was written in the reverse direction, B to A.", "D: the coordinates of A and B were added instead of subtracted."],
  "the shift is image minus original, coordinate by coordinate — in that order",
  "dx = 7 − 2 = 5 and dy = 3 − (−1) = 4, so (x, y) → (x + 5, y + 4).",
  lambda v: m(f"(x, y) → (x {'+' if v[0]>=0 else '-'} {abs(v[0])}, y {'+' if v[1]>=0 else '-'} {abs(v[1])})"))
I("rotational-symmetry-angle-of-a-regular-polygon", 4, G, 2,
  "What is the smallest angle of rotation, about its centre, that maps a regular hexagon onto itself?",
  [60, 120, 30, 90], lambda v: v == 360/6,
  ["B: the interior angle of a regular hexagon was given.", "C: half of the correct angle was taken.", "D: a quarter-turn was assumed for every polygon."],
  "the smallest turn is 360° divided by the number of sides — not the interior angle",
  "360° ÷ 6 = 60°.", lambda v: f"{v}°")
# ---------------- triangles / polygons
def sides_from_interior(a):
    return [n for n in range(3, 200) if abs(180*(n-2)/n - a) < 1e-9][0]
I("number-of-sides-from-an-interior-angle", 4, G2, 2,
  "Each interior angle of a regular polygon measures 156°. How many sides does the polygon have?",
  [15, 24, 14, 16], lambda v: v == sides_from_interior(156),
  ["B: the exterior angle, 24°, was reported as the number of sides.", "C: the division was off by one.", "D: the division was off by one in the other direction."],
  "go through the exterior angle: 180° − 156° = 24°, then 360° ÷ 24° — the 24 is an angle, not the answer",
  "Exterior angle = 24°, so n = 360 ÷ 24 = 15.")
I("number-of-sides-from-the-interior-angle-sum", 4, G2, 2,
  "The interior angles of a polygon add up to 1620°. How many sides does it have?",
  [11, 9, 10, 12], lambda v: 180*(v-2) == 1620,
  ["B: 1620 ÷ 180 was taken without adding the 2.", "C: the sum formula was solved with an off-by-one slip.", "D: the sum formula was solved with an off-by-one slip the other way."],
  "the sum is 180(n − 2), so after dividing by 180 you must ADD 2 to reach n",
  "180(n − 2) = 1620 gives n − 2 = 9, so n = 11.")
def is_tri(t): a, b, c = sorted(t); return a + b > c
I("which-lengths-form-a-triangle", 4, G2, 2,
  "Which set of three lengths can be the sides of a triangle?",
  [(5, 7, 11), (3, 4, 8), (6, 6, 13), (4, 9, 13)], lambda v: is_tri(v),
  ["B: 3 + 4 = 7, which is less than 8.", "C: 6 + 6 = 12, which is less than 13.", "D: 4 + 9 = 13 exactly, so the three lengths collapse into a straight line."],
  "the two shorter sides must add to MORE than the longest — equal is a flat line, not a triangle",
  "5 + 7 = 12 > 11, so only 5, 7, 11 passes.", lambda v: m(f"{v[0]}, {v[1]}, {v[2]}"))
def perim_possible(p): x = p - 17; return 5 < x < 17
I("impossible-perimeter-from-two-sides", 4, G2, 3,
  "Two sides of a triangle measure 6 and 11. Which of these cannot be the perimeter of the triangle?",
  [22, 25, 30, 33], lambda v: not perim_possible(v),
  ["B: the third side would be 8, which is allowed.", "C: the third side would be 13, which is allowed.", "D: the third side would be 16, which is allowed."],
  "the third side lies strictly between 5 and 17, so the perimeter lies strictly between 22 and 34 — the end values are excluded",
  "A perimeter of 22 would make the third side 5, and 6 + 5 = 11 is not greater than 11.")
I("larger-of-two-supplementary-angles-in-a-ratio", 4, G2, 2,
  "Two supplementary angles are in the ratio 2 : 3. What is the measure of the larger angle?",
  [108, 72, 120, 90], lambda v: v == 180*3/5,
  ["B: the smaller angle was given.", "C: 180° was split 1 : 2 instead of 2 : 3.", "D: the two angles were assumed to be equal."],
  "split 180° into 2 + 3 = 5 parts and then read off the part that is asked for",
  "One part is 36°, so the larger angle is 3 × 36° = 108°.", lambda v: f"{v}°")
def classify(a, b):
    c = 180 - a - b; ang = "Right" if c == 90 or a == 90 or b == 90 else ("Obtuse" if max(a, b, c) > 90 else "Acute")
    sd = "isosceles" if len({a, b, c}) < 3 else "scalene"
    return f"{ang} and {sd}"
I("classify-a-triangle-from-two-angles", 4, G2, 2,
  "A triangle has two angles of 35° and 55°. How is the triangle best described?",
  ["Right and scalene", "Acute and isosceles", "Obtuse and scalene", "Right and isosceles"], lambda v: v == classify(35, 55),
  ["B: the third angle was left unchecked and the triangle was assumed acute.", "C: the third angle was taken to be obtuse.", "D: the right angle was found, but equal sides were assumed."],
  "find the THIRD angle first, then classify by angles and by sides separately — three different angles mean scalene",
  "The third angle is 180° − 90° = 90°, and 35°, 55°, 90° are all different.", lambda v: v)
I("fourth-vertex-of-a-parallelogram-from-three-vertices", 4, "Coordinate geometry & quadrilaterals", 3,
  "A(1, 2), B(5, 2) and C(7, 6) are three consecutive vertices of parallelogram ABCD. What are the coordinates of D?",
  [(3, 6), (11, 6), (-1, -2), (3, 2)], lambda v: v == (1 + 7 - 5, 2 + 6 - 2) and (v[0]-1, v[1]-2) == (7-5, 6-2),
  ["B: B + C − A was used, pairing the wrong vertices.", "C: A + B − C was used.", "D: the x-coordinate is right but the y-coordinate was copied from A."],
  "in ABCD the diagonals share a midpoint, so D = A + C − B — check that AB and DC are equal vectors",
  "AB = (4, 0), so DC must equal (4, 0): D = C − (4, 0) = (3, 6).", pt)
I("half-diagonal-of-a-rectangle", 4, "Coordinate geometry & quadrilaterals", 2,
  "A rectangle measures 9 by 12. Its diagonals meet at O. How far is O from each vertex?",
  [F(15, 2), F(15), F(21, 2), F(6)], lambda v: v == F(math.hypot(9, 12)).limit_denominator(10)/2,
  ["B: the full diagonal was given.", "C: the average of the two sides was used.", "D: half of the shorter side was used."],
  "diagonals of a rectangle are equal and bisect each other, so the distance to a vertex is HALF the diagonal",
  "Diagonal = √(9² + 12²) = 15, so OA = 7.5.", lambda v: ('%g' % float(v)))
# ---------------- scale / similarity
I("map-scale-to-actual-distance", 4, G4, 1,
  "On a map, 1 cm represents 40 km. Two cities are 2.5 cm apart on the map. What is the actual distance between them, in km?",
  [100, 42.5, 16, 10], lambda v: abs(v - 2.5*40) < 1e-9,
  ["B: 40 and 2.5 were added.", "C: 40 was divided by 2.5.", "D: a decimal-place slip gave 2.5 × 4."],
  "multiply the map length by the scale — the two quantities are in proportion, not added",
  "2.5 × 40 = 100 km.", lambda v: dec(v))
I("height-from-shadows-by-similar-triangles", 4, G4, 2,
  "A 2 m pole casts a shadow 1.2 m long. At the same moment a tree casts a shadow 9 m long. How tall is the tree, in metres?",
  [15, 5.4, 9.8, 18], lambda v: abs(v - 2/1.2*9) < 1e-9,
  ["B: the proportion was written upside down (1.2 × 9 ÷ 2).", "C: the difference in shadow lengths was added to the pole's height.", "D: the shadow was simply doubled."],
  "same sun angle means similar triangles — height : shadow is the same ratio for both, so multiply, not add",
  "h/9 = 2/1.2, so h = 15 m.", lambda v: dec(v))
# ---------------- circles
I("perpendicular-from-the-centre-bisects-a-chord", 4, G3, 2,
  "In a circle with centre O, a line from O perpendicular to chord AB meets it at M. If AB = 18, what is AM?",
  [9, 18, 36, 6], lambda v: v == 18/2,
  ["B: the whole chord was reported.", "C: the chord was doubled.", "D: a third of the chord was taken instead of a half."],
  "the perpendicular from the centre BISECTS the chord — half, not the whole and not a third",
  "AM = MB, so AM = 18 ÷ 2 = 9.")
I("central-angle-between-equally-spaced-points", 4, G3, 2,
  "Eight points are equally spaced around a circle. What is the central angle between two neighbouring points?",
  [45, 60, 90, 135], lambda v: v == 360/8,
  ["B: the angle for six points was used.", "C: a quarter-turn was assumed.", "D: the interior angle of a regular octagon was given."],
  "equal spacing splits the full 360° into equal parts — divide by the number of points",
  "360° ÷ 8 = 45°.", lambda v: f"{v}°")
I("point-on-a-circle-from-centre-and-radius", 4, G3, 2,
  "A circle has centre (−2, 3) and radius 5. Which point lies on the circle?",
  [(1, 7), (3, 6), (-4, 8), (0, 0)], lambda v: abs(math.hypot(v[0]+2, v[1]-3) - 5) < 1e-9,
  ["B: its squared distance from the centre is 34, not 25.", "C: its squared distance from the centre is 29, not 25.", "D: its squared distance from the centre is 13, not 25."],
  "a point is on the circle only if its squared distance from the centre equals r² — compute (x + 2)² + (y − 3)² for each",
  "For (1, 7): 3² + 4² = 25 = 5².", pt)
# ---------------- number & algebra
I("additive-inverse-of-a-decimal", 1, "Real numbers & their properties", 1,
  "What is the additive inverse of −4.5?",
  [F(9, 2), F(-9, 2), F(-2, 9), F(2, 9)], lambda v: v + F(-9, 2) == 0,
  ["B: the number itself was given.", "C: the multiplicative inverse was found.", "D: the reciprocal was found and its sign changed."],
  "the additive inverse is what you ADD to reach 0 — it only changes the sign; it is not the reciprocal",
  "−4.5 + 4.5 = 0.", lambda v: {F(9,2): '4.5', F(-9,2): '−4.5'}.get(v, fr(v)))
I("linear-rule-from-a-table-of-values", 3, "Linear functions & equations", 2,
  "The table shows x = 1, 2, 3, 4 and y = 5, 8, 11, 14. Which equation fits every pair?",
  [(3, 2), (2, 3), (3, -2), (4, 1)], lambda v: all(v[0]*x + v[1] == y for x, y in zip([1, 2, 3, 4], [5, 8, 11, 14])),
  ["B: the slope and the intercept were swapped; it fits only the first pair.", "C: the intercept has the wrong sign.", "D: it fits the first pair only."],
  "test the rule on at least TWO pairs — several wrong rules still match the first row",
  "The differences in y are 3, so the slope is 3, and 5 = 3(1) + 2.",
  lambda v: m(f"y = {v[0]}x {'+' if v[1]>=0 else '-'} {abs(v[1])}"))
I("equation-of-a-horizontal-line-through-two-points", 3, "Linear functions & equations", 1,
  "Which equation describes the line through (3, −2) and (−4, −2)?",
  [('y', -2), ('x', -2), ('y', 3), ('x', 3)], lambda v: v == ('y', -2),
  ["B: the vertical-line form was used with the y-value.", "C: an x-value was placed in the y-equation.", "D: a vertical line through the first x-value was written."],
  "equal y-values mean a HORIZONTAL line y = constant — the equation takes the shared y, not an x",
  "Both points have y = −2, so the line is y = −2.", lambda v: m(f"{v[0]} = {v[1]}"))
I("parameter-that-makes-a-line-horizontal", 3, "Linear functions & equations", 2,
  "For what value of k is the graph of y = (k − 4)x + 7 a horizontal line?",
  [4, -4, 0, 7], lambda v: v - 4 == 0,
  ["B: a sign slip gave −4.", "C: k was set to 0 instead of making the coefficient 0.", "D: the intercept was reported."],
  "a horizontal line has slope 0, so the whole coefficient of x must vanish — solve k − 4 = 0",
  "k − 4 = 0, so k = 4.", lambda v: m(v))
I("distance-between-two-vertical-lines", 3, "Linear functions & equations", 1,
  "What is the distance between the parallel lines x = −3 and x = 5?",
  [8, 2, 4, -8], lambda v: v == abs(5 - (-3)),
  ["B: the two values were added.", "C: the gap was halved.", "D: a negative distance was reported."],
  "distance between parallel vertical lines is the DIFFERENCE of the x-values, taken as a positive number",
  "|5 − (−3)| = 8.", lambda v: m(v))
I("slope-of-a-parallel-line", 3, "Linear functions & equations", 1,
  "What is the slope of any line parallel to y = (3/5)x − 5?",
  [F(3, 5), F(-3, 5), F(5, 3), F(-5, 3)], lambda v: v == F(3, 5),
  ["B: only the sign was changed.", "C: the reciprocal was taken.", "D: the negative reciprocal (a perpendicular slope) was taken."],
  "parallel lines share the SAME slope — reciprocals and negatives belong to perpendicular lines",
  "Parallel lines have equal slopes, so the slope is 3/5.")
I("equation-from-a-slope-and-a-y-intercept", 3, "Linear functions & equations", 1,
  "Which equation has slope 4 and y-intercept −3?",
  [(4, -3), (-3, 4), (4, 3), (-4, -3)], lambda v: v == (4, -3),
  ["B: the slope and the intercept were swapped.", "C: the sign of the intercept was lost.", "D: the sign of the slope was changed."],
  "slope-intercept form is y = mx + b — m is the slope and b the intercept, each with its own sign",
  "y = 4x + (−3) = 4x − 3.", lambda v: m(f"y = {v[0]}x {'+' if v[1]>=0 else '-'} {abs(v[1])}"))
I("inequality-from-a-spending-limit", 3, "Inequalities & their graphs", 2,
  "Sara has SAR 60. A pen costs SAR 4 and a notebook costs SAR 7. If she buys x pens and y notebooks, which inequality shows every purchase she can afford?",
  [(4, 7, '≤'), (4, 7, '≥'), (4, 7, '<'), (7, 4, '≤')],
  lambda v: v == (4, 7, '≤'),
  ["B: the inequality sign is reversed, which would mean spending at least SAR 60.", "C: the strict sign excludes spending exactly SAR 60.", "D: the prices were attached to the wrong items."],
  "'has SAR 60' means the total may equal 60 or be less — use ≤, with each price on its own item",
  "Total cost 4x + 7y must not exceed 60.", lambda v: f"{v[0]}x + {v[1]}y {v[2]} 60")
I("negative-fractional-exponent", 1, "Exponents & radicals", 3,
  "Evaluate 16^(−3/4).",
  [F(1, 8), F(-8), F(8), F(-1, 8)], lambda v: abs(16**(-0.75) - float(v)) < 1e-12,
  ["B: the negative exponent was turned into a negative value.", "C: the negative sign of the exponent was ignored.", "D: the reciprocal was taken but a negative sign was kept."],
  "a negative exponent means RECIPROCAL, never a negative number — and 3/4 means fourth root, then cube",
  "16^(3/4) = 2³ = 8, so 16^(−3/4) = 1/8.")
I("cube-root-of-a-negative-decimal", 1, "Exponents & radicals", 2,
  "Evaluate the cube root of −0.008.",
  [F(-1, 5), F(-1, 50), F(1, 5), F(-2)], lambda v: v**3 == F(-8, 1000),
  ["B: a decimal-place slip gave −0.02.", "C: the sign was lost.", "D: the magnitude of the root was slipped by a power of ten."],
  "an odd root of a negative number is negative, and 0.008 = 0.2³ — count decimal places in threes",
  "(−0.2)³ = −0.008.", lambda v: {F(-1,5): '−0.2', F(-1,50): '−0.02', F(1,5): '0.2'}.get(v, fr(v)))
I("principal-square-root-of-a-negative-number", 7, "Complex numbers", 2,
  "What is the principal square root of −49?",
  [7j, -7j, 7, 49j], lambda v: abs(v*v + 49) < 1e-9 and v.imag > 0,
  ["B: this is also a square root of −49, but it is not the principal one.", "C: the number was treated as a real square root of 49.", "D: the number was not square-rooted."],
  "√(−a) = i√a for the principal root — the positive imaginary one, not 7 and not 49i",
  "√(−49) = √49 · √(−1) = 7i.", lambda v: {7j: '7i', -7j: '−7i', 7: '7', 49j: '49i'}[v])
I("pure-imaginary-solutions-of-a-quadratic", 7, "Complex numbers", 2,
  "Solve x² = −64 over the complex numbers.",
  [('im', 8), ('re', 8), ('im', 32), ('none', 0)],
  lambda v: (v[0] == 'im' and -v[1]**2 == -64),
  ["B: real roots were assumed, but a real square cannot be negative.", "C: 64 was divided by 2 before rooting.", "D: 'no real solutions' was reported as 'no solutions at all'."],
  "no REAL number squares to a negative, but over the complex numbers x = ±√64 · i",
  "x = ±√(−64) = ±8i.", lambda v: {'im': m(f"x = ±{v[1]}i"), 're': m(f"x = ±{v[1]}"), 'none': 'No solution'}[v[0]])
I("product-of-a-complex-number-and-its-conjugate", 7, "Complex numbers", 2,
  "Find (5 + 2i)(5 − 2i).",
  [29, 21, 10, 25], lambda v: (5 + 2j)*(5 - 2j) == v,
  ["B: a² − b² was used, forgetting that i² = −1.", "C: 2a was taken as the product.", "D: only a² was kept."],
  "a number times its conjugate is a² + b² — the cross terms cancel and −b²i² becomes +b²",
  "25 − 4i² = 25 + 4 = 29.")
I("complex-polar-form-converted-to-rectangular", 7, "Complex numbers", 2,
  "Write 2(cos 90° + i sin 90°) in rectangular form.",
  [2j, 2, -2j, 2 + 2j], lambda v: abs(cmath.rect(2, math.pi/2) - v) < 1e-9,
  ["B: only the cosine term was kept.", "C: the sign of the sine term was lost.", "D: the modulus was added to both parts."],
  "evaluate cos 90° = 0 and sin 90° = 1 before multiplying by the modulus",
  "2(0 + i) = 2i.", lambda v: {2j: '2i', 2: '2', -2j: '−2i', 2 + 2j: '2 + 2i'}[v])
# ---------------- sequences
def an(n): return n*n - 2*n
I("position-of-a-term-with-a-given-value", 7, "Sequences & series", 3,
  "In a sequence, aₙ = n² − 2n. Which term (position n) is equal to 15?",
  [5, -3, 3, 15], lambda v: v >= 1 and an(v) == 15,
  ["B: the second root of the equation is not a valid position.", "C: this is the position whose value is 3, not 15.", "D: the value 15 was reported as the position."],
  "solve for n and then reject any root that is not a positive whole number — positions cannot be negative",
  "n² − 2n − 15 = 0 gives n = 5 or n = −3; only n = 5 is a position.")
I("ratio-from-two-block-sums", 7, "Sequences & series", 3,
  "In a geometric sequence the first three terms add up to 14 and the next three terms add up to 112. What is the common ratio?",
  [2, 8, 4, 14], lambda v: v**3 == F(112, 14),
  ["B: r³ = 8 was reported instead of r.", "C: r² was reported instead of r.", "D: the first sum was reported."],
  "the second block is the first block times r³, so r³ = 112 ÷ 14 — then take the cube root",
  "r³ = 8, so r = 2 (terms 2, 4, 8 then 16, 32, 64).")
I("total-over-days-with-percentage-growth", 7, "Sequences & series", 3,
  "A page has 80 visitors on day 1. Each day the number of visitors is 50% more than the day before. How many visitors in total over the first 3 days?",
  [380, 360, 180, 440], lambda v: v == 80 + 80*F(3, 2) + 80*F(3, 2)**2,
  ["B: the 50% was added to the ORIGINAL 80 each day (linear growth).", "C: only day 3 was counted.", "D: a doubling slip was made on day 3."],
  "'50% more than the day before' multiplies by 1.5 EACH day — it compounds; it is not a fixed addition",
  "80 + 120 + 180 = 380.")
I("next-term-when-each-term-is-the-sum-of-the-previous-two", 7, "Sequences & series", 1,
  "In the sequence 2, 3, 5, 8, 13, … each term is the sum of the two terms before it. What is the next term?",
  [21, 18, 26, 20], lambda v: v == 8 + 13,
  ["B: the previous gap (5) was added again.", "C: the last term was doubled.", "D: an off-by-one slip."],
  "test the rule on the earlier terms, then add the LAST TWO terms — not the last term plus a pattern of gaps",
  "8 + 13 = 21.")
def alt_sum(): return sum(5*(-1)**(k-1) for k in range(1, 10))
I("sum-of-an-alternating-series", 7, "Sequences & series", 2,
  "Evaluate the sum of 5(−1)^(k−1) for k = 1 to 9.",
  [5, 0, -5, 45], lambda v: v == alt_sum(),
  ["B: the terms were assumed to cancel in pairs, forgetting that 9 is odd.", "C: the first term was taken as negative.", "D: the signs were ignored."],
  "count the terms — an ODD number of alternating terms leaves the first one uncancelled",
  "5 − 5 + 5 − … + 5 has four cancelling pairs and one extra +5.", lambda v: m(v))
# ---------------- trigonometry
I("unit-circle-y-coordinate-from-x", 8, "Sine, cosine & tangent", 2,
  "P(3/5, y) is a point on the unit circle in the first quadrant. What is y?",
  [F(4, 5), F(-4, 5), F(2, 5), F(16, 25)], lambda v: v > 0 and F(3, 5)**2 + v**2 == 1,
  ["B: the sign of y is wrong for the first quadrant.", "C: y was found as 1 − x.", "D: y² was reported without taking the root."],
  "a point on the unit circle satisfies x² + y² = 1 — solve for y, then check the quadrant's sign",
  "y² = 1 − 9/25 = 16/25, so y = 4/5.")
I("reference-angle-in-the-third-quadrant", 8, "Degree & radian measure", 1,
  "What is the reference angle of 230°?",
  [50, 130, 40, 310], lambda v: v == 230 - 180,
  ["B: 360° − 230° was used, which is the rule for the fourth quadrant.", "C: 270° − 230° was used.", "D: a coterminal-type slip, 360° − 50°."],
  "the reference angle is the acute angle to the NEAREST x-axis — in the third quadrant subtract 180°",
  "230° − 180° = 50°.", lambda v: f"{v}°")
I("inverse-tangent-of-negative-one", 9, "Basic trigonometric equations", 3,
  "Find tan⁻¹(−1), the principal value, in degrees.",
  [-45, 135, 45, 315], lambda v: abs(math.degrees(math.atan(-1)) - v) < 1e-9,
  ["B: this has tan = −1 but is outside the principal range (−90°, 90°).", "C: the sign was dropped.", "D: this has tan = −1 but is outside the principal range."],
  "the principal value of tan⁻¹ lies between −90° and 90° — a negative input gives a negative angle",
  "tan(−45°) = −1 and −45° is in (−90°, 90°).", lambda v: m(f"{v}°"))
cands_sq = [lambda t: 1 + math.sin(2*t), lambda t: 1, lambda t: 1 + math.sin(t)*math.cos(t), lambda t: math.sin(2*t)]
I("square-of-a-sine-plus-cosine", 9, "Trigonometric identities", 3,
  "Which expression is equal to (sin θ + cos θ)² for every θ?",
  [0, 1, 2, 3], lambda v: all(abs((math.sin(t)+math.cos(t))**2 - cands_sq[v](t)) < 1e-9 for t in (0.3, 0.9, 1.7, 2.6, 4.0)),
  ["B: the cross term was forgotten, leaving sin²θ + cos²θ only.", "C: the cross term was halved.", "D: only the cross term was kept."],
  "squaring a sum keeps the CROSS TERM 2 sin θ cos θ = sin 2θ — it does not vanish",
  "sin²θ + 2 sinθ cosθ + cos²θ = 1 + sin 2θ.", lambda v: ['1 + sin 2θ', '1', '1 + sin θ cos θ', 'sin 2θ'][v])
I("tangent-equation-with-a-negative-value", 9, "Basic trigonometric equations", 2,
  "Solve tan θ = −1 for 0° ≤ θ < 180°.",
  [135, 45, 315, 225], lambda v: 0 <= v < 180 and abs(math.tan(math.radians(v)) + 1) < 1e-9,
  ["B: the sign was ignored, giving tan = +1.", "C: tan = −1 here, but it is outside the stated range.", "D: it is outside the range, and tan 225° = +1."],
  "tan is negative in the second quadrant — within a half-turn the answer is 180° minus the reference angle",
  "Reference angle 45°, second quadrant: 180° − 45° = 135°.", lambda v: f"{v}°")
# ---------------- vectors & polar
def net(): return 9 - 6
I("net-of-two-opposite-forces", 9, "Vectors & their basic applications", 1,
  "A body is pulled with a force of 9 N to the east and 6 N to the west. What is the net force?",
  [(3, 'east'), (15, 'east'), (3, 'west'), (6, 'east')], lambda v: v == (abs(net()), 'east'),
  ["B: the magnitudes were added although the forces oppose each other.", "C: the direction of the smaller force was used.", "D: only the smaller force was reported."],
  "opposite vectors SUBTRACT, and the net points the way of the larger force",
  "9 − 6 = 3 N, in the direction of the 9 N force: east.", lambda v: f"{v[0]} N {v[1]}")
I("terminal-point-from-an-initial-point-and-a-vector", 9, "Vectors & their basic applications", 2,
  "A vector ⟨4, 5⟩ starts at the point (2, −3). Where does it end?",
  [(6, 2), (-2, -8), (8, -15), (4, 5)], lambda v: v == (2 + 4, -3 + 5),
  ["B: the vector was subtracted from the start.", "C: the components were multiplied by the coordinates.", "D: the vector itself was given as the end point."],
  "terminal point = initial point + components of the vector, coordinate by coordinate",
  "(2 + 4, −3 + 5) = (6, 2).", pt)
def on_curve_polar(pts, c=5): return all(abs(math.hypot(x, y)*(x/math.hypot(x, y)) - c) < 1e-9 for x, y in pts)
curves = {('x', 5): [(5, t) for t in (-3, 0.5, 2, 7)], ('y', 5): [(t, 5) for t in (-3, 0.5, 2, 7)],
          ('c', 25): [(5*math.cos(a), 5*math.sin(a)) for a in (0.4, 1.3, 2.2, 5)], ('l', 5): [(t, 5*t) for t in (-2, 0.5, 1, 3)]}
I("polar-equation-of-a-vertical-line", 10, "Polar coordinates & equations", 3,
  "Which Cartesian equation is the same as the polar equation r = 5 sec \u03b8?",
  [('x', 5), ('y', 5), ('c', 25), ('l', 5)],
  lambda v: all(abs(math.hypot(x, y) - 5/math.cos(math.atan2(y, x))) < 1e-9 for x, y in curves[v]),
  ["B: sec θ was confused with csc θ, giving a horizontal line.", "C: r = 5 (constant radius) was assumed.", "D: sec θ was confused with tan θ."],
  "multiply both sides by cos θ: r cos θ = 5, and r cos θ is x — so the graph is a vertical line",
  "r = 5/cos θ gives r cos θ = 5, i.e. x = 5.", lambda v: {'x': 'x = 5', 'y': 'y = 5', 'c': 'x² + y² = 25', 'l': 'y = 5x'}[v[0]])
# ---------------- rational functions
def recip_ok(v):
    h, k = v; f = lambda x: 1/(x - h) + k
    return abs(f(2 + 1e-9)) > 1e6 and abs(f(1e12) - (-4)) < 1e-6 and h == 2
I("reciprocal-function-from-its-asymptotes", 3, "Rational functions", 3,
  "A reciprocal function has a vertical asymptote x = 2 and a horizontal asymptote y = −4. Which equation could it be?",
  [(2, -4), (-2, -4), (2, 4), (-2, 4)], recip_ok,
  ["B: the sign of the horizontal shift is wrong, giving a vertical asymptote at x = −2.", "C: the sign of the vertical shift is wrong, giving y = 4.", "D: both signs are wrong."],
  "f(x) = 1/(x − h) + k has x = h and y = k as asymptotes — the horizontal shift carries the OPPOSITE sign inside the bracket",
  "x = 2 means the denominator is x − 2, and y = −4 means adding −4.",
  lambda v: m(f"f(x) = 1/(x {'-' if v[0]>0 else '+'} {abs(v[0])}) {'+' if v[1]>0 else '-'} {abs(v[1])}"))
I("rational-function-with-no-horizontal-asymptote", 3, "Rational functions", 3,
  "Which function has NO horizontal asymptote?",
  [(2, 1), (1, 2), (1, 1), (1, 2.5)], lambda v: v[0] > v[1],
  ["B: the denominator has the higher degree, so y = 0 is an asymptote.", "C: the degrees are equal, so y = (ratio of leading coefficients) is an asymptote.", "D: the denominator has the higher degree, so y = 0 is an asymptote."],
  "compare the degrees — a horizontal asymptote exists unless the NUMERATOR's degree is the larger one",
  "Only (x² + 1)/(x − 3) has a numerator of higher degree than its denominator.",
  lambda v: {(2, 1): "(x² + 1)/(x − 3)", (1, 2): "(x + 1)/(x² − 3)", (1, 1): "5x/(x − 1)", (1, 2.5): "x/(x² + 1)"}[v])
# ---------------- statistics
xs = [0, 1, 2, 3]; ps = [F(1, 10), F(3, 10), F(4, 10), F(2, 10)]
I("expected-value-from-a-distribution-table", 5, "Probability, sample spaces & counting principles", 2,
  "A random variable X takes the values 0, 1, 2, 3 with probabilities 0.1, 0.3, 0.4, 0.2. What is E(X)?",
  [F(17, 10), F(15, 10), F(1), F(4, 10)], lambda v: v == sum(x*p for x, p in zip(xs, ps)),
  ["B: the plain average of the four values was used.", "C: the probabilities were added.", "D: the largest probability was reported."],
  "E(X) is the SUM of value × probability — not the plain mean of the values",
  "0(0.1) + 1(0.3) + 2(0.4) + 3(0.2) = 1.7.", lambda v: dec(float(v)))
I("zero-standard-deviation-means-equal-values", 5, "Measures of dispersion & standard deviation", 1,
  "If the standard deviation of a set of marks is zero, which data set could it be?",
  [(20, 20, 20), (19, 20, 21), (10, 20, 30), (-1, 0, 1)], lambda v: statistics.pstdev(v) == 0,
  ["B: the values are close together, but not equal, so the deviation is not zero.", "C: the values are far apart.", "D: the mean is zero, which is unrelated to the spread."],
  "standard deviation measures SPREAD about the mean — it is zero only when every value is identical",
  "Every deviation from the mean is 0 only for 20, 20, 20.", lambda v: ", ".join(m(x) for x in v))
I("data-set-with-the-smallest-spread", 5, "Measures of dispersion & standard deviation", 2,
  "Four sets of marks all have mean 20. Which set has the smallest standard deviation?",
  [(19, 20, 21), (18, 20, 22), (15, 20, 25), (12, 20, 28)], lambda v: statistics.pstdev(v) == min(statistics.pstdev(s) for s in [(19, 20, 21), (18, 20, 22), (15, 20, 25), (12, 20, 28)]),
  ["B: this set is more spread out than the keyed one.", "C: this set is much more spread out.", "D: this set is the most spread out."],
  "with the same mean, the set whose values sit CLOSEST to it has the smallest standard deviation",
  "The deviations are ±1 for 19, 20, 21 — smaller than in every other set.", lambda v: ", ".join(m(x) for x in v))
I("number-of-observations-above-one-standard-deviation", 5, "Normal distribution", 3,
  "Marks of 2000 students are normally distributed with mean 70 and standard deviation 8. About how many scored above 78?",
  [320, 640, 680, 1360], lambda v: v == round(2000*(1 - 0.68)/2),
  ["B: both tails were counted.", "C: 34% (the band between the mean and 78) was used.", "D: the 68% central band was used."],
  "78 is one standard deviation above the mean — only ONE tail (16%) lies above it, and then it must be applied to the 2000 students",
  "(100% − 68%) ÷ 2 = 16%, and 16% of 2000 = 320.")
data = [2, 4, 4, 5, 10]
rel = [lambda a, b, c: a > b and b == c, lambda a, b, c: a == b == c, lambda a, b, c: c > b > a, lambda a, b, c: b > a and a == c]
I("order-of-mean-median-and-mode", 5, "Data representation & measures of centre", 3,
  "For the data 2, 4, 4, 5, 10, which statement about the mean, median and mode is true?",
  [0, 1, 2, 3], lambda v: rel[v](statistics.mean(data), statistics.median(data), statistics.mode(data)),
  ["B: the three measures are not all equal; the outlier 10 pulls the mean up.", "C: the mode is not the largest of the three.", "D: the median is not larger than the mean here."],
  "an unusually LARGE value pulls the mean above the median and mode — compute all three before comparing",
  "Mean = 25 ÷ 5 = 5, median = 4, mode = 4, so mean > median = mode.",
  lambda v: ['Mean > median = mode', 'Mean = median = mode', 'Mode > median > mean', 'Median > mean = mode'][v])
# ---------------- limits
def a_n(n): return (3*n + 1)/(n + 4)
I("limit-of-a-sequence-by-leading-coefficients", 11, "Limits", 2,
  "Find the limit as n → ∞ of (3n + 1)/(n + 4).",
  [3, F(1, 4), 4, 0], lambda v: abs(a_n(10**9) - float(v)) < 1e-6,
  ["B: the constant terms 1 and 4 were divided.", "C: the denominator's constant was reported.", "D: the terms were assumed to shrink to 0."],
  "for a ratio of equal-degree terms, the limit is the RATIO OF LEADING COEFFICIENTS — the constants stop mattering",
  "Divide by n: (3 + 1/n)/(1 + 4/n) → 3/1 = 3.", lambda v: fr(v))
def f3(x): return 1/(x - 3)**2
I("limit-that-grows-without-bound", 11, "Limits", 2,
  "Find the limit as x → 3 of 1/(x − 3)².",
  ['+inf', '-inf', 0, F(1, 9)], lambda v: (v == '+inf') and f3(3 + 1e-4) > 1e6 and f3(3 - 1e-4) > 1e6,
  ["B: the squared bracket is never negative, so the values cannot head to −∞.", "C: the denominator was treated as large rather than as approaching zero.", "D: x = 0 was substituted instead of x = 3."],
  "a squared denominator approaching 0 gives HUGE POSITIVE values from both sides",
  "Both one-sided values grow without bound, positively.", lambda v: {'+inf': '+∞', '-inf': '−∞', 0: '0', F(1, 9): '1/9'}[v])
def lim_a(a): return F(6) / a
I("coefficient-from-a-limit-at-infinity", 11, "Limits", 3,
  "If the limit as x → ∞ of (6x² − x)/(ax² + 5) equals 2, find a.",
  [3, 12, 2, F(1, 3)], lambda v: lim_a(F(v)) == 2,
  ["B: 6 and 2 were multiplied.", "C: the limit value was copied as a.", "D: the ratio was inverted, giving 2/6."],
  "equal degrees: the limit is 6/a, so set 6/a = 2 — don't multiply 6 by 2",
  "6/a = 2 gives a = 3.")
I("end-behaviour-of-an-odd-degree-polynomial", 11, "Limits", 3,
  "Find the limit as x → −∞ of (−2x³ + x²).",
  ['+inf', '-inf', 0, -2], lambda v: (-2*(-1e6)**3 + (-1e6)**2) > 1e12 and v == '+inf',
  ["B: the sign change of an odd power was missed.", "C: the polynomial was treated as bounded.", "D: the leading coefficient was reported."],
  "for x → −∞ the leading term decides; an ODD power turns negative into negative, and −2 × negative is positive",
  "−2x³ is positive for large negative x and dominates x².", lambda v: {'+inf': '+∞', '-inf': '−∞', 0: '0', -2: '−2'}[v])
# ---------------- conics
def dirx():  # (x-1)^2 = 8(y+2): vertex (1,-2), 4p = 8
    return ('y', -2 - 8/4)
I("directrix-from-a-vertical-parabola-equation", 10, "Parabolas", 2,
  "What is the directrix of (x − 1)² = 8(y + 2)?",
  [('y', -4), ('y', 0), ('x', -1), ('y', 4)], lambda v: v == dirx(),
  ["B: this is the y-value of the focus, not the directrix.", "C: a vertical line was written for an upward-opening parabola.", "D: the sign was reversed."],
  "4p = 8 gives p = 2; the directrix sits p BELOW the vertex of an upward parabola and the focus sits p above",
  "Vertex (1, −2), p = 2, so the directrix is y = −2 − 2 = −4.", lambda v: m(f"{v[0]} = {v[1]}"))
I("focus-of-a-horizontal-parabola-at-the-origin", 10, "Parabolas", 2,
  "What is the focus of y² = 12x?",
  [(3, 0), (12, 0), (6, 0), (0, 3)], lambda v: v == (12/4, 0),
  ["B: 4p was reported as p.", "C: 2p was used.", "D: the coordinates were swapped."],
  "match y² = 4px, so p = 12 ÷ 4 = 3 — the focus is (p, 0), not (4p, 0)",
  "4p = 12 gives p = 3, so the focus is (3, 0).", lambda v: pt(v))
I("opening-direction-from-the-vertex-and-a-point", 10, "Parabolas", 2,
  "A parabola with vertex (0, 5) passes through (5, 8) and (−5, 8). In which direction does it open?",
  ["Upwards", "Downwards", "To the left", "To the right"], lambda v: v == ("Upwards" if 8 > 5 else "Downwards"),
  ["B: the points lie above the vertex, so it cannot open downwards.", "C: a horizontal axis would need points at different y-values on both sides of the vertex.", "D: the symmetric pair (±5, 8) shows the axis is the y-axis, not horizontal."],
  "the two symmetric points tell you the axis is vertical; they lie ABOVE the vertex, so it opens up",
  "Points with y = 8 > 5 sit above the vertex of a parabola symmetric about x = 0.", lambda v: v)
I("distance-between-the-foci-of-an-ellipse", 10, "Ellipses", 3,
  "What is the distance between the foci of x²/25 + y²/9 = 1?",
  [8, 4, 10, 6], lambda v: v == 2*math.sqrt(25 - 9),
  ["B: c was found but not doubled.", "C: the length of the major axis was given.", "D: the length of the minor axis was given."],
  "c² = a² − b² gives c, but the foci are 2c apart — don't stop at c",
  "c = √(25 − 9) = 4, so the foci are 8 apart.", lambda v: m(v))
I("transverse-axis-of-a-hyperbola", 10, "Hyperbolas", 3,
  "What is the equation of the transverse axis of (x + 1)²/9 − (y − 3)²/25 = 1?",
  [('y', 3), ('x', -1), ('y', -3), ('x', 3)], lambda v: v == ('y', 3),
  ["B: this is the conjugate axis.", "C: the sign of the centre's y-value was changed.", "D: the centre's y-value was used as an x-value."],
  "the positive term (here x) gives the direction of the transverse axis — it runs through the centre, so it is the HORIZONTAL line y = 3",
  "The centre is (−1, 3) and the transverse axis is horizontal: y = 3.", lambda v: m(f"{v[0]} = {v[1]}"))
I("ellipse-from-the-sum-and-difference-of-its-axes", 10, "Ellipses", 4,
  "An ellipse centred at the origin has a horizontal major axis. The lengths of its major and minor axes add to 16 and differ by 4. What is its equation?",
  [(25, 9), (9, 25), (100, 36), (10, 6)], lambda v: v == (((16 + 4)/2/2)**2, ((16 - 4)/2/2)**2),
  ["B: the denominators were put under the wrong variables.", "C: the axis lengths 10 and 6 were squared instead of the semi-axes 5 and 3.", "D: the axis lengths were used as denominators with no squaring."],
  "axes are 2a and 2b — halve them FIRST, then square for the denominators, with a² under x for a horizontal major axis",
  "Major = 10, minor = 6, so a = 5, b = 3 and the equation is x²/25 + y²/9 = 1.",
  lambda v: m(f"x²/{int(v[0])} + y²/{int(v[1])} = 1"))
# ---------------- logs
I("logarithm-of-a-reciprocal-power", 6, "Logarithms & their properties", 2,
  "Evaluate log₃(1/81).",
  [-4, 4, F(-1, 4), F(1, 4)], lambda v: abs(3**float(v) - 1/81) < 1e-12,
  ["B: the sign was lost.", "C: the answer was inverted.", "D: the answer was inverted and its sign lost."],
  "1/81 = 3⁻⁴, so the exponent is NEGATIVE four — a fraction below 1 gives a negative logarithm",
  "3⁻⁴ = 1/81, so log₃(1/81) = −4.", lambda v: fr(F(v)))
I("zero-of-a-logarithmic-function", 6, "Logarithmic functions", 2,
  "Find the zero of f(x) = log₄(x + 1).",
  [0, 1, 3, -1], lambda v: v + 1 > 0 and abs(math.log(v + 1, 4)) < 1e-12,
  ["B: x was set to 1 instead of the argument being set to 1.", "C: the argument was set equal to the base, which gives log = 1.", "D: x = −1 makes the argument 0, which is outside the domain."],
  "a logarithm is 0 when its ARGUMENT equals 1 — so set x + 1 = 1, not x = 1",
  "log₄(1) = 0, so x + 1 = 1 and x = 0.", lambda v: m(v))
I("y-intercept-of-a-shifted-logarithm", 6, "Logarithmic functions", 2,
  "Find the y-intercept of y = log₂(x + 2) + 3.",
  [4, 3, 5, 2], lambda v: abs(math.log2(0 + 2) + 3 - v) < 1e-12,
  ["B: log₂ 2 was taken as 0.", "C: log₂ 2 was taken as 2.", "D: only the horizontal shift was reported."],
  "substitute x = 0 and evaluate the log exactly — log₂ 2 = 1, not 0 and not 2",
  "y = log₂(2) + 3 = 1 + 3 = 4.", lambda v: m(v))
I("sound-level-from-the-logarithmic-formula", 6, "Applications of logarithms", 3,
  "Sound level is L = 10 log(I/I₀) decibels. If I₀ = 10⁻¹² and I = 10⁻³, find L.",
  [90, 9, 120, 80], lambda v: abs(10*math.log10(1e-3/1e-12) - v) < 1e-9,
  ["B: the factor of 10 was forgotten.", "C: only the exponent 12 was used.", "D: the exponents were subtracted with an arithmetic slip."],
  "divide first: 10⁻³ ÷ 10⁻¹² = 10⁹, so log = 9, then apply the factor 10",
  "L = 10 × log(10⁹) = 90 dB.", lambda v: f"{v} dB")
I("logarithm-with-a-reciprocal-base-relation", 6, "Logarithms & their properties", 4,
  "If (1/b)^x = y with b > 0 and b ≠ 1, which expression equals log_b y?",
  [0, 1, 2, 3], lambda v: all(abs([lambda x: -x, lambda x: x, lambda x: 1/x, lambda x: -1/x][v](x) - math.log((1/b)**x, b)) < 1e-9 for b in (2, 3, 5) for x in (1.5, 2, 3)),
  ["B: the reciprocal base was ignored, losing the sign.", "C: x was inverted.", "D: x was inverted and the sign changed."],
  "(1/b)^x = b^(−x), so the exponent on b is −x — a reciprocal base flips the sign",
  "y = b^(−x), so log_b y = −x.", lambda v: ['−x', 'x', '1/x', '−1/x'][v])
# ---------------- matrices
I("order-of-a-difference-of-matrices", 2, "Matrices", 1,
  "A and B are both 3 × 5 matrices. What is the order of A − B?",
  [(3, 5), (5, 3), (3, 3), None], lambda v: v == (np.zeros((3, 5)) - np.zeros((3, 5))).shape,
  ["B: the order was transposed.", "C: a square matrix was assumed.", "D: subtraction was thought to be undefined, which is true only for matrices of different orders."],
  "addition and subtraction need EQUAL orders and keep that order — multiplication is the operation with the inner-dimension rule",
  "Entry-by-entry subtraction of two 3 × 5 matrices is again 3 × 5.", lambda v: "Not defined" if v is None else f"{v[0]} × {v[1]}")
I("percentage-of-a-matrix", 2, "Matrices", 2,
  "Find 25% of the matrix [16  5  24].",
  [(4, 1.25, 6), (8, 2.5, 12), (64, 20, 96), (4, 5, 24)], lambda v: v == tuple(0.25*x for x in (16, 5, 24)),
  ["B: 50% (half) was taken.", "C: every entry was multiplied by 4.", "D: only the first entry was scaled."],
  "a percentage of a matrix is a scalar multiple — multiply EVERY entry by 0.25",
  "0.25 × (16, 5, 24) = (4, 1.25, 6).", lambda v: "[" + "  ".join(dec(x) for x in v) + "]")
I("two-planes-meet-in-a-line", 4, "Points, lines & planes", 2,
  "Two distinct planes that are not parallel intersect in:",
  [1, 0, 2, 'two'], lambda v: v == 3 - np.linalg.matrix_rank(np.array([[1, 1, 1], [1, -1, 0]])),
  ["B: two planes give a whole line of common points, not a single point.", "C: a shared plane would make the two planes the same plane.", "D: if two points are shared, the whole line through them is shared."],
  "two non-parallel planes share a whole LINE — not a point, and never exactly two points",
  "The common solutions of two independent plane equations form a one-dimensional set: a line.",
  lambda v: {1: "A line", 0: "A single point", 2: "A plane", 'two': "Exactly two points"}[v])
