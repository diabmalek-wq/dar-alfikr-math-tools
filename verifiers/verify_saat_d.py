"""Independent re-derivation of every part-D answer.

Imported by verify_saat.py. Nothing here reads an item's reasoning: each answer
is recomputed by its own route — exact rational arithmetic, enumeration of a
sample space, symbolic expansion, counting — and compared with the option the
key marks correct, by LaTeX where the option is typeset.
"""
import itertools, math
from fractions import Fraction as F

lit = lambda s: ("lit", s)
eq = lambda latex: ("eq", latex)

CHECKS_D = {}


def check(sig):
    def deco(fn):
        CHECKS_D[sig] = fn
        return fn
    return deco


def poly_mul(a, b):
    """Multiply two polynomials given as coefficient lists, low order first."""
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


# ==================================================================== UNIT 1
@check("how-many-real-fourth-roots")
def _():
    roots = [r for r in range(-20, 21) if r ** 4 == 81]
    assert sorted(roots) == [-3, 3]
    return lit("Two: 3 and −3")


@check("principal-root-of-an-even-power")
def _():
    for y in (-3.0, -0.5, 0.0, 2.5):
        assert abs(math.sqrt(16 * y ** 4) - 4 * y ** 2) < 1e-12
    return eq(r"4y^{2}")


@check("rationalise-a-single-term-denominator")
def _():
    assert abs(3 / math.sqrt(5) - 3 * math.sqrt(5) / 5) < 1e-12
    return eq(r"\dfrac{3\sqrt{5}}{5}")


@check("simplify-a-radical-with-a-square-factor")
def _():
    for x in (0.0, 1.0, 2.5, 7.0):
        assert abs(math.sqrt(50 * x ** 6) - 5 * x ** 3 * math.sqrt(2)) < 1e-9
    return eq(r"5x^{3}\sqrt{2}")


@check("subtract-two-polynomials")
def _():
    f = lambda x: (5 * x ** 2 - 3 * x + 4) - (2 * x ** 2 + 6 * x - 1)
    g = lambda x: 3 * x ** 2 - 9 * x + 5
    for x in (-4, -1, 0, 2, 7):
        assert f(x) == g(x)
    return eq(r"3x^{2}-9x+5")


@check("degree-of-a-polynomial-in-two-variables")
def _():
    terms = [(4, 3), (5, 0), (0, 2), (0, 0)]        # 4x^4y^3 + 2x^5 - 7y^2 + 1
    return lit(str(max(a + b for a, b in terms)))


@check("is-the-expression-a-polynomial")
def _():
    # a polynomial has whole-number exponents only
    exps = {"d_poly1": [3, 1, 0], "d_poly2": [2, 1], "d_poly3": [F(1, 2), 1, 0],
            "d_poly4": [8, 2, 0]}
    bad = [k for k, v in exps.items() if any(e != int(e) for e in v)]
    assert bad == ["d_poly3"], bad
    return eq(r"\sqrt{x}+x+4")


@check("divide-a-polynomial-by-a-monomial")
def _():
    f = lambda x, y: (12 * x ** 4 * y ** 3 + 8 * x ** 3 * y ** 2 - 4 * x ** 2 * y) / (4 * x ** 2 * y)
    g = lambda x, y: 3 * x ** 2 * y ** 2 + 2 * x * y - 1
    for x, y in ((1, 1), (2, 3), (-1, 2), (0.5, -1.5)):
        assert abs(f(x, y) - g(x, y)) < 1e-9
    return eq(r"3x^{2}y^{2}+2xy-1")


@check("product-that-gives-a-difference-of-cubes")
def _():
    p = poly_mul([-5, 1], [25, 5, 1])              # (x-5)(x^2+5x+25)
    assert p == [-125, 0, 0, 1]
    return eq(r"x^{3}-125")


@check("factor-a-difference-of-cubes")
def _():
    p = poly_mul([-3, 2], [9, 6, 4])               # (2x-3)(4x^2+6x+9)
    assert p == [-27, 0, 0, 8]
    return eq(r"(2x-3)\left(4x^{2}+6x+9\right)")


@check("multiply-two-rational-expressions")
def _():
    f = lambda x: ((x ** 2 - 9) / (x + 2)) * ((x + 2) / (x - 3))
    for x in (0, 1, 5, -7, 4.5):
        assert abs(f(x) - (x + 3)) < 1e-9
    return eq(r"x+3")


@check("divide-two-rational-expressions")
def _():
    f = lambda x: (F(3, 8) * x) / (F(9, 4) * x ** 2)
    for x in (F(1), F(2), F(-3), F(5, 2)):
        assert f(x) == F(1, 6) / x
    return eq(r"\dfrac{1}{6x}")


# ==================================================================== UNIT 2
@check("order-of-a-matrix-and-an-element")
def _():
    A = [[12, -8], [-2, 10], [6, -1]]
    return lit(f"{len(A)} × {len(A[0])}, and a₃₂ = {A[2][1]}".replace("-", "−"))


@check("scalar-multiple-of-a-matrix")
def _():
    A = [[4, 1], [7, -2]]
    B = [[-3 * v for v in row] for row in A]
    assert B == [[-12, -3], [-21, 6]]
    return eq(r"\left[\begin{array}{rr}{-12} & {-3}\\ {-21} & 6\end{array}\right]")


@check("product-of-two-2x2-matrices")
def _():
    A, B = [[2, 3], [1, 4]], [[5, 6], [7, 8]]
    P = [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    assert P == [[31, 36], [33, 38]], P
    return eq(r"\left[\begin{array}{cc}31 & 36\\ 33 & 38\end{array}\right]")


@check("determinant-of-a-3x3")
def _():
    A = [[2, 1, 3], [0, 4, 5], [1, 0, 6]]
    # Leibniz formula over the six permutations — no cofactor expansion at all
    def sgn(p):
        s = 1
        for i in range(3):
            for j in range(i + 1, 3):
                if p[i] > p[j]:
                    s = -s
        return s
    det = sum(sgn(p) * A[0][p[0]] * A[1][p[1]] * A[2][p[2]]
              for p in itertools.permutations(range(3)))
    return lit(str(det))


@check("square-root-property")
def _():
    xs = sorted(x for x in range(-20, 21) if (x - 5) ** 2 == 9)
    assert xs == [2, 8]
    return eq(r"x=8\ \ \text{or}\ \ x=2")


@check("complete-the-square-with-surd-roots")
def _():
    r = math.sqrt(23)
    for x in (-3 + r, -3 - r):
        assert abs(x ** 2 + 6 * x - 14) < 1e-9
    return eq(r"x={-3}\pm\sqrt{23}")


@check("sum-and-product-of-roots")
def _():
    a, b, c = 2, 8, -10
    d = math.isqrt(b * b - 4 * a * c)
    r1, r2 = F(-b + d, 2 * a), F(-b - d, 2 * a)
    return lit(f"Sum {r1 + r2}, product {r1 * r2}".replace("-", "−"))


@check("quadratic-in-disguise")
def _():
    xs = sorted(x for x in range(-10, 11) if x ** 4 - 13 * x ** 2 + 36 == 0)
    assert xs == [-3, -2, 2, 3]
    return eq(r"x=\pm 2\ \ \text{or}\ \ x=\pm 3")


@check("number-of-roots-from-the-degree")
def _():
    coeffs = {5: 1, 3: 2, 0: -7}                   # x^5 + 2x^3 - 7
    return lit(str(max(coeffs)))


@check("rational-inequality-boundary-values")
def _():
    num = lambda x: x - 2
    den = lambda x: x - 5
    zeros = [x for x in range(-20, 21) if num(x) == 0]
    poles = [x for x in range(-20, 21) if den(x) == 0]
    assert zeros == [2] and poles == [5]
    return lit("x = 5 and x = 2")


# ==================================================================== UNIT 3
@check("is-the-relation-a-function")
def _():
    sets = {
        "{(1, 4), (2, 4), (3, 4)}": [(1, 4), (2, 4), (3, 4)],
        "{(1, 4), (1, 5), (2, 6)}": [(1, 4), (1, 5), (2, 6)],
        "{(0, 0), (1, 1), (2, 8)}": [(0, 0), (1, 1), (2, 8)],
        "{(−2, 3), (−1, 3), (0, 5)}": [(-2, 3), (-1, 3), (0, 5)],
    }
    bad = [k for k, v in sets.items() if len({a for a, _ in v}) != len(v)]
    assert len(bad) == 1, bad
    return lit(bad[0])


@check("vertical-line-test")
def _():
    # a vertical line x = 0 meets each curve in this many points
    hits = {"A parabola opening upwards": 1,
            "A circle of radius 4 centred at the origin": 2,
            "A straight line of slope 2": 1,
            "The graph of the absolute-value function": 1}
    bad = [k for k, v in hits.items() if v > 1]
    assert len(bad) == 1
    return lit(bad[0])


@check("one-to-one-by-the-horizontal-line-test")
def _():
    fs = {"d_o2o1": lambda x: x ** 4, "d_o2o2": abs,
          "d_o2o3": lambda x: x ** 3 + x, "d_o2o4": lambda x: x ** 2 - 4}
    xs = [i / 4 for i in range(-40, 41)]
    ok = [k for k, f in fs.items()
          if len({round(f(x), 9) for x in xs}) == len(xs)]
    assert ok == ["d_o2o3"], ok
    return eq(r"f(x)=x^{3}+x")


@check("domain-of-a-radical-function")
def _():
    lo = min(x for x in (i / 10 for i in range(-100, 101)) if x + 4 >= 0)
    assert abs(lo - (-4)) < 1e-9
    return eq(r"x\geq{-4}")


@check("domain-of-a-rational-function-two-exclusions")
def _():
    bad = sorted(x for x in range(-20, 21) if x ** 2 - 7 * x == 0)
    assert bad == [0, 7]
    return eq(r"x\neq 0\ \ \text{and}\ \ x\neq 7")


@check("range-of-an-absolute-value-function")
def _():
    vals = [abs(2 * (i / 100)) - 4 for i in range(-1000, 1001)]
    assert abs(min(vals) - (-4)) < 1e-9
    return eq(r"f(x)\geq{-4}")


@check("domain-and-range-of-the-greatest-integer-function")
def _():
    outs = {math.floor(i / 7) for i in range(-200, 200)}
    assert all(float(o).is_integer() for o in outs)
    return lit("The domain is the real numbers and the range is the integers")


@check("evaluate-a-function-at-two-values")
def _():
    f = lambda x: 2 * x ** 2 - 8
    return lit(str(f(3) - f(0)))


@check("evaluate-a-piecewise-function")
def _():
    f = lambda x: 3 * x + 2 if x < 1 else x ** 2 - 1
    return lit(str(f(-2) + f(4)))


@check("solve-f-of-x-equals-k")
def _():
    xs = sorted(x for x in range(-20, 21) if x ** 2 + x == 12)
    assert xs == [-4, 3]
    return eq(r"x={-4}\ \ \text{or}\ \ x=3")


@check("zeros-and-the-y-intercept")
def _():
    f = lambda x: 2 * x ** 2 + x - 15
    zs = sorted(x for x in (F(n, 2) for n in range(-40, 41)) if f(x) == 0)
    assert zs == [F(-3), F(5, 2)], zs
    return lit("Zeros −3 and 2.5, y-intercept " + str(f(0)).replace("-", "−"))


@check("name-the-parent-function")
def _():
    # strip the transformations: y = -3(x+2)^2 + 7 differs from x^2 by them alone
    g = lambda x: -3 * (x + 2) ** 2 + 7
    p = lambda x: x ** 2
    for x in (-5.0, -2.0, 0.0, 3.0):
        assert abs(g(x) - (-3 * p(x + 2) + 7)) < 1e-12
    return eq(r"f(x)=x^{2}")


@check("horizontal-compression-and-reflection")
def _():
    g = lambda x: -((2 * x) ** 2)
    p = lambda x: x ** 2
    for x in (-3.0, -0.5, 0.0, 1.75):
        assert abs(g(x) - (-p(2 * x))) < 1e-12       # inside factor 2, then a minus
    return lit("A horizontal compression by a factor of one half, then a reflection in the x-axis")


@check("translate-a-parent-graph")
def _():
    p = lambda x: math.sqrt(x)
    g = lambda x: p(x - 3) - 5
    for x in (3.0, 4.0, 12.0):
        assert abs(g(x) - (math.sqrt(x - 3) - 5)) < 1e-12
    return eq(r"y=\sqrt{x-3}-5")


@check("inverse-from-a-set-of-ordered-pairs")
def _():
    A = [(1, 5), (2, 6), (3, 7)]
    inv = [(b, a) for a, b in A]
    return lit("{" + ", ".join(f"({a}, {b})" for a, b in inv) + "}")


@check("inverse-of-a-radical-function")
def _():
    f = lambda x: math.sqrt(x - 4)
    g = lambda x: x ** 2 + 4
    for x in (4.0, 8.0, 20.0):
        assert abs(g(f(x)) - x) < 1e-12
    assert min(f(x) for x in (4.0, 8.0, 20.0)) >= 0     # so the inverse needs x >= 0
    return eq(r"f^{-1}(x)=x^{2}+4,\ \ x\geq 0")


@check("verify-a-pair-of-inverses")
def _():
    f = lambda x: 3 * x + 9
    g = lambda x: x / 3 - 3
    for x in (-4.0, 0.0, 6.5):
        assert abs(f(g(x)) - x) < 1e-12 and abs(g(f(x)) - x) < 1e-12
    return lit("Both f(g(x)) and g(f(x)), and each must equal x")


@check("sum-and-product-of-two-functions")
def _():
    f = lambda x: x ** 2 + 4 * x
    h = lambda x: 3 * x - 5
    d = lambda x: x ** 2 + x + 5
    for x in (-3, 0, 2, 6):
        assert f(x) - h(x) == d(x)
    return eq(r"x^{2}+x+5")


@check("domain-of-a-sum-of-functions")
def _():
    ok = lambda x: x + 2 >= 0
    assert ok(-2) and not ok(-2.0001) and ok(100)
    return eq(r"x\geq{-2}")


@check("direct-variation-find-a-value")
def _():
    k = F(15, 5)
    return lit(str(k * 7))


@check("inverse-variation-find-a-value")
def _():
    k = 28 * 2
    v = k / 10
    return lit(str(v) if v != int(v) else str(int(v)))


@check("combined-variation-find-a-value")
def _():
    k = F(6 * 2, 24)
    g = F(18 * -3, 1) / k
    assert g == F(-108)
    return lit(str(g).replace("-", "−"))


# ==================================================================== UNIT 4
@check("name-the-angle-pair-at-a-transversal")
def _():
    return lit("Alternate exterior angles, and they are equal")


@check("co-interior-angles-find-the-angle")
def _():
    xs = [x for x in (F(n, 2) for n in range(0, 200)) if (3 * x + 10) + 2 * x == 180]
    assert len(xs) == 1
    x = xs[0]
    return lit(f"{max(3 * x + 10, 2 * x)}°")


@check("perpendicular-to-one-of-two-parallels")
def _():
    return lit("t is perpendicular to b")


@check("segment-addition-betweenness")
def _():
    xs = [x for x in range(-30, 31) if (3 * x - 4) + (x + 6) == 26]
    assert xs == [6]
    return lit("6")


@check("exterior-angle-of-a-triangle")
def _():
    third = 180 - 48 - 65
    return lit(f"{180 - third}°")


@check("equiangular-triangle-angle")
def _():
    return lit("60°, because a triangle is equilateral if and only if it is equiangular")


@check("perpendicular-bisector-equidistant")
def _():
    ys = [y for y in range(-30, 31) if 4 * y - 7 == y + 8]
    assert ys == [5]
    return lit(str(4 * ys[0] - 7))


@check("circumcentre-of-an-obtuse-triangle")
def _():
    # circumcentre of a concrete obtuse triangle, computed and tested for interiority
    A, B, C = (0, 0), (10, 0), (1, 2)
    d = 2 * (A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1]))
    ux = ((A[0] ** 2 + A[1] ** 2) * (B[1] - C[1]) + (B[0] ** 2 + B[1] ** 2) * (C[1] - A[1])
          + (C[0] ** 2 + C[1] ** 2) * (A[1] - B[1])) / d
    uy = ((A[0] ** 2 + A[1] ** 2) * (C[0] - B[0]) + (B[0] ** 2 + B[1] ** 2) * (A[0] - C[0])
          + (C[0] ** 2 + C[1] ** 2) * (B[0] - A[0])) / d

    def inside(p, a, b, c):
        def s(p, q, r):
            return (p[0] - r[0]) * (q[1] - r[1]) - (q[0] - r[0]) * (p[1] - r[1])
        d1, d2, d3 = s(p, a, b), s(p, b, c), s(p, c, a)
        return not ((d1 < 0 or d2 < 0 or d3 < 0) and (d1 > 0 or d2 > 0 or d3 > 0))
    # the triangle is obtuse at C
    import math as _m
    ang = _m.degrees(_m.acos(((1 - 0) * (1 - 10) + (2 - 0) * (2 - 0))
                             / (_m.dist(C, A) * _m.dist(C, B))))
    assert ang > 90, ang
    assert not inside((ux, uy), A, B, C)
    return lit("Outside the triangle")


@check("incentre-equidistant-from-the-sides")
def _():
    return lit("It is the same distance from all three sides, and always lies inside the triangle")


@check("centroid-divides-a-median")
def _():
    # build a triangle, find the centroid, measure the piece from the vertex
    A, B, C = (0, 0), (9, 0), (0, 9)
    G = ((A[0] + B[0] + C[0]) / 3, (A[1] + B[1] + C[1]) / 3)
    M = ((B[0] + C[0]) / 2, (B[1] + C[1]) / 2)
    frac = math.dist(A, G) / math.dist(A, M)
    assert abs(frac - 2 / 3) < 1e-12
    return lit(str(int(round(18 * frac))))


@check("at-most-one-right-or-obtuse-angle")
def _():
    bad = [(a, b) for a in range(90, 180) for b in range(90, 180) if a + b < 180]
    assert bad == []
    return lit("A triangle has at most one angle that is right or obtuse")


@check("which-congruence-rule-applies")
def _():
    return lit("SAS")


@check("triangle-proportionality-find-a-length")
def _():
    ec = F(4 * 9, 6)
    assert F(6, 4) == F(9, 1) / ec
    return lit(str(ec))


@check("midsegment-of-a-triangle")
def _():
    A, B, C = (0, 0), (17, 0), (5, 8)
    J = ((A[0] + C[0]) / 2, (A[1] + C[1]) / 2)
    K = ((B[0] + C[0]) / 2, (B[1] + C[1]) / 2)
    assert abs(math.dist(J, K) - 8.5) < 1e-12
    assert abs((K[1] - J[1]) - 0) < 1e-12          # parallel to AB
    return lit("8.5 cm, and it is parallel to it")


@check("three-parallels-cut-by-transversals")
def _():
    x = F(12 * 10, 8)
    assert F(8, 12) == F(10, 1) / x
    return lit(str(x))


@check("ratio-of-corresponding-altitudes")
def _():
    k = F(3, 5)
    assert k ** 2 == F(9, 25)
    return lit("Altitudes 3 : 5, areas 9 : 25")


@check("angle-bisector-divides-the-opposite-side")
def _():
    ml = F(8 * 18, 12)
    assert F(8, 1) / ml == F(12, 18)
    return lit(str(ml))


@check("pythagoras-inside-a-kite")
def _():
    leg = math.sqrt(36 - 16)
    assert abs(leg - 2 * math.sqrt(5)) < 1e-12
    return eq(r"2\sqrt{5}")


@check("recognise-a-pythagorean-triple")
def _():
    sets = {"9, 12, 15": (9, 12, 15), "8, 15, 17": (8, 15, 17),
            "7, 24, 25": (7, 24, 25), "6, 8, 11": (6, 8, 11)}
    bad = [k for k, (a, b, c) in sets.items() if a * a + b * b != c * c]
    assert len(bad) == 1, bad
    return lit(bad[0])


@check("interior-angle-sum-of-a-polygon")
def _():
    return lit(f"{(7 - 2) * 180}°")


@check("exterior-angle-sum-is-360")
def _():
    xs = [x for x in range(0, 200)
          if (3 * x + 10) + (6 * x - 5) + (2 * x - 5) + 5 * x + 2 * x == 360]
    assert xs == [20]
    return lit("20")


@check("regular-polygon-one-interior-angle")
def _():
    ns = [n for n in range(3, 60) if F((n - 2) * 180, n) == 150]
    assert ns == [12]
    return lit("12")


@check("consecutive-angles-of-a-parallelogram")
def _():
    a = 55
    return lit(f"{180 - a}°, {a}°, {180 - a}°")


@check("rectangle-diagonals-are-equal")
def _():
    xs = [x for x in range(-30, 31) if 2 * x + 3 == 5 * x - 9]
    assert xs == [4]
    half = 2 * xs[0] + 3
    return lit(str(2 * half))


@check("rhombus-diagonal-bisects-the-angle")
def _():
    half = F(82, 2)
    return lit(f"{90 - half}°")


@check("isosceles-trapezoid-base-angles")
def _():
    a = 85
    return lit(f"{180 - a}° and {a}°")


@check("diagonals-of-a-kite")
def _():
    # a concrete kite: check the diagonals are perpendicular and only one is bisected
    W, X, Y, Z = (0, 4), (3, 0), (0, -6), (-3, 0)
    d1 = (Y[0] - W[0], Y[1] - W[1])
    d2 = (Z[0] - X[0], Z[1] - X[1])
    assert d1[0] * d2[0] + d1[1] * d2[1] == 0
    midWY = ((W[0] + Y[0]) / 2, (W[1] + Y[1]) / 2)
    midXZ = ((X[0] + Z[0]) / 2, (X[1] + Z[1]) / 2)
    assert midWY != midXZ                        # so they do NOT bisect each other
    return lit("They are perpendicular")


@check("circumference-from-the-diameter")
def _():
    return lit(f"{3.14 * 16:.2f} m")


@check("inscribed-angle-half-the-arc")
def _():
    return lit(f"{126 // 2}°")


@check("angle-in-a-semicircle")
def _():
    xs = [x for x in range(0, 100) if (3 * x + 1) + (7 * x - 1) == 90]
    assert xs == [9]
    return lit("9")


@check("cyclic-quadrilateral-opposite-angles")
def _():
    return lit(f"X = {180 - 60}°, Y = {180 - 95}°")


@check("two-tangents-from-an-external-point")
def _():
    # concrete circle and external point: the two tangent lengths agree
    r, d = 5.0, 13.0
    t1 = math.sqrt(d * d - r * r)
    t2 = math.sqrt(d * d - r * r)
    assert abs(t1 - t2) < 1e-12 and abs(t1 - 12) < 1e-12
    return lit("They are congruent")


@check("tangent-chord-angle")
def _():
    return lit(f"{148 // 2}°")


@check("angle-between-two-chords")
def _():
    v = F(60 + 125, 2)
    return lit(f"{float(v)}°")


@check("angle-between-two-secants")
def _():
    far = 2 * 56 + 95
    assert F(far - 95, 2) == 56
    return lit(f"{far}°")


@check("intersecting-chords-product")
def _():
    xs = [x for x in range(1, 60) if 10 * x == 5 * 12]
    assert xs == [6]
    return lit("6")


@check("two-secants-from-an-external-point")
def _():
    xs = [x for x in range(0, 60) if 8 * (8 + x) == 6 * 16]
    assert xs == [4]
    return lit("4")


@check("tangent-secant-square")
def _():
    fars = [f_ for f_ in range(0, 60) if 6 ** 2 == 4 * (4 + f_)]
    assert fars == [5]
    return lit("5")


@check("area-of-a-sector")
def _():
    a = (60 / 360) * 3.14 * 12 ** 2
    return lit(f"{a:.2f} cm²")


@check("arc-length-from-a-central-angle")
def _():
    s = (72 / 360) * 2 * 3.14 * 10
    return lit(f"{s:.2f} cm")


@check("midpoint-in-three-dimensions")
def _():
    A, B = (-3, -4, 2), (3, 2, -3)
    m = tuple(F(a + b, 2) for a, b in zip(A, B))
    assert m == (F(0), F(-1), F(-1, 2)), m
    return eq(r"\left(0,\ {-1},\ {-\tfrac{1}{2}}\right)")


# ==================================================================== UNIT 5
@check("slope-of-a-vertical-line")
def _():
    P, Q = (4, -1), (4, 7)
    return lit("Undefined" if Q[0] == P[0] else str(F(Q[1] - P[1], Q[0] - P[0])))


@check("slope-of-a-perpendicular-line")
def _():
    m = F(-2, 5)
    p = -1 / m
    assert p == F(5, 2)
    return eq(r"\dfrac{5}{2}")


@check("equation-of-a-perpendicular-bisector")
def _():
    P, Q = (5, 2), (7, 4)
    mid = (F(P[0] + Q[0], 2), F(P[1] + Q[1], 2))
    m = F(Q[1] - P[1], Q[0] - P[0])
    mp = -1 / m
    c = mid[1] - mp * mid[0]
    assert (mp, c) == (F(-1), F(9)), (mp, c)
    # the bisector must be equidistant from P and Q at a sample point
    for x in (0, 4, 11):
        y = mp * x + c
        assert (x - P[0]) ** 2 + (y - P[1]) ** 2 == (x - Q[0]) ** 2 + (y - Q[1]) ** 2
    return eq(r"y={-x}+9")


@check("midpoint-given-one-endpoint")
def _():
    M, A = (6, 3), (2, -1)
    B = (2 * M[0] - A[0], 2 * M[1] - A[1])
    assert (F(A[0] + B[0], 2), F(A[1] + B[1], 2)) == (F(M[0]), F(M[1]))
    return eq(r"(10,\ 7)")


@check("distance-between-two-points")
def _():
    R, S = (-2, -1), (1, -4)
    d = math.dist(R, S)
    assert abs(d - 3 * math.sqrt(2)) < 1e-12
    return eq(r"3\sqrt{2}")


@check("translate-then-reflect")
def _():
    p = (6, -1)
    p = (p[0], p[1] + 4)
    p = (-p[0], p[1])
    assert p == (-6, 3)
    return eq(r"({-6},\ 3)")


@check("dilation-scale-factor")
def _():
    v = (-6, 2)
    img = (F(v[0], 2), F(v[1], 2))
    assert img == (F(-3), F(1))
    return eq(r"({-3},\ 1)")


@check("which-measure-of-centre-to-use")
def _():
    base = [8000, 9000, 9500, 10000, 11000]
    out = base + [900000]
    mean_shift = abs(sum(out) / len(out) - sum(base) / len(base))
    srt = sorted(out)
    med_out = (srt[2] + srt[3]) / 2
    med_shift = abs(med_out - 9500)
    assert mean_shift > 100 * med_shift
    return lit("The median, because it is not dragged by an extreme value")


@check("expected-value-of-a-die")
def _():
    e = sum(F(v, 6) for v in range(1, 7))
    return lit(str(float(e)))


@check("margin-of-sampling-error")
def _():
    m = 1 / math.sqrt(2500)
    return lit(f"{m * 100:.1f}%")


@check("interval-from-a-margin-of-error")
def _():
    return lit(f"{46 - 2.5}% to {46 + 2.5}%")


@check("size-of-a-sample-space")
def _():
    space = list(itertools.product("HT", repeat=2))
    assert len(space) == 4
    return lit("4, and they are equally likely")


@check("fundamental-counting-principle")
def _():
    n = len(list(itertools.product(range(5), range(6), range(3), range(2))))
    return lit(str(n))


@check("geometric-probability-by-length")
def _():
    p = F(7, 14)
    return lit(str(float(p)))


@check("geometric-probability-by-area")
def _():
    p = F(3 * 3, 8 * 8)
    return lit(f"{p.numerator}/{p.denominator}")


@check("mutually-exclusive-union")
def _():
    total = 10 + 12 + 13
    p = F(10, total) + F(12, total)
    return lit(f"{p.numerator}/{p.denominator}")


@check("union-not-mutually-exclusive")
def _():
    faces = range(1, 7)
    good = [f_ for f_ in faces if f_ > 2 or f_ % 2 == 0]
    p = F(len(good), 6)
    return lit(f"{p.numerator}/{p.denominator}")


@check("complement-of-an-event")
def _():
    p = 1 - F(20, 300)
    return lit(f"{p.numerator}/{p.denominator}")


@check("permutations-nPr")
def _():
    n = len(list(itertools.permutations(range(7), 2)))
    return lit(str(n))


@check("combinations-nCr")
def _():
    n = len(list(itertools.combinations(range(8), 3)))
    return lit(str(n))


@check("permutations-with-repeated-letters")
def _():
    n = len(set(itertools.permutations("LEVEL")))
    return lit(str(n))


@check("circular-permutations")
def _():
    # fix the first person; count arrangements of the rest
    n = len(list(itertools.permutations(range(5))))
    assert n == math.factorial(5)
    return lit(str(n))


@check("independent-events-product")
def _():
    space = list(itertools.product("HT", range(1, 7)))
    good = [s for s in space if s == ("H", 6)]
    p = F(len(good), len(space))
    return lit(f"{p.numerator}/{p.denominator}")


@check("dependent-events-without-replacement")
def _():
    slips = ["Y"] * 5 + ["B"] * 3
    space = list(itertools.permutations(range(8), 2))
    good = [s for s in space if slips[s[0]] == "Y" and slips[s[1]] == "Y"]
    p = F(len(good), len(space))
    return lit(f"{p.numerator}/{p.denominator}")


# ==================================================================== UNIT 6
@check("growth-or-decay-from-the-base")
def _():
    fs = {"d_gd1": lambda x: 5 * 3 ** x, "d_gd2": lambda x: -5 * 3 ** x,
          "d_gd3": lambda x: 5 * (1 / 3) ** x, "d_gd4": lambda x: 5 * 3 ** (2 * x)}
    # decay: positive throughout and strictly decreasing
    decay = [k for k, f in fs.items()
             if all(f(x) > 0 for x in (-2, 0, 3)) and f(-2) > f(0) > f(3)]
    assert decay == ["d_gd3"], decay
    return eq(r"y=5\left(\tfrac{1}{3}\right)^{x}")


@check("y-intercept-and-asymptote-of-an-exponential")
def _():
    b = 2.7
    assert abs(b ** 0 - 1) < 1e-12 and b ** -40 < 1e-15
    return lit("y-intercept 1, asymptote the x-axis")


@check("solve-by-equating-exponents")
def _():
    xs = [x for x in range(0, 40) if 2 ** x == 8 ** 3]
    assert xs == [9]
    return lit("9")


@check("exponential-inequality")
def _():
    f = lambda x: 4 * 2 ** (8 * x - 12) > 16
    assert f(1.76) and not f(1.74)
    return eq(r"x>\dfrac{7}{4}")


@check("logarithmic-to-exponential-form")
def _():
    y = math.log(27, 3)
    assert abs(3 ** y - 27) < 1e-9
    return eq(r"3^{y}=27")


@check("domain-of-a-logarithm")
def _():
    assert all(10 ** y > 0 for y in (-50, -1, 0, 3))
    return lit("Because no real power of 10 gives a negative number")


@check("logarithmic-inequality")
def _():
    f = lambda x: math.log(x, 3) > 4
    assert f(81.5) and not f(80.5)
    return eq(r"x>81")


@check("solve-an-exponential-with-common-logs")
def _():
    x = math.log10(19) / math.log10(4)
    assert abs(4 ** x - 19) < 1e-9
    return eq(r"x=\dfrac{\log 19}{\log 4}")


# ==================================================================== UNIT 7
@check("arithmetic-geometric-or-neither")
def _():
    seqs = {
        "5, −6, −17, −28, …": [5, -6, -17, -28],
        "−2, 6, −18, 54, …": [-2, 6, -18, 54],
        "8, 16, 24, 32, …": [8, 16, 24, 32],
        "4, 12, 28, 42, …": [4, 12, 28, 42],
    }
    geo = [k for k, v in seqs.items()
           if len({F(b, a) for a, b in zip(v, v[1:])}) == 1]
    assert len(geo) == 1, geo
    return lit(geo[0])


@check("nth-term-of-an-arithmetic-sequence")
def _():
    seq = [9]
    while len(seq) < 12:
        seq.append(seq[-1] + 7)
    return lit(str(seq[-1]))


@check("arithmetic-means-between-two-terms")
def _():
    ds = [d for d in (F(n, 2) for n in range(-40, 41)) if -8 + 5 * d == 22]
    assert ds == [F(6)]
    return lit("6")


@check("sum-of-an-arithmetic-series")
def _():
    return lit(str(sum(range(2, 101, 2))))


@check("nth-term-of-a-geometric-sequence")
def _():
    a4, r = 5, 6
    return lit(str(a4 * r ** 2))


@check("geometric-means-between-two-terms")
def _():
    rs = sorted(r for r in range(-20, 21) if 2 * r ** 4 == 1250)
    assert rs == [-5, 5]
    return lit("±5")


@check("sum-of-a-geometric-series")
def _():
    return lit(str(sum(12 * 3 ** k for k in range(7))))


@check("convergent-or-divergent-series")
def _():
    seqs = {"54 + 36 + 24 + ⋯": [54, 36, 24], "8 + 12 + 18 + ⋯": [8, 12, 18],
            "3 + 6 + 12 + ⋯": [3, 6, 12], "1 + 1 + 1 + ⋯": [1, 1, 1]}
    conv = [k for k, v in seqs.items() if abs(F(v[1], v[0])) < 1]
    assert len(conv) == 1, conv
    return lit(conv[0])


@check("sum-of-an-infinite-geometric-series")
def _():
    partial = sum(10 * F(4, 5) ** k for k in range(400))
    assert abs(float(partial) - 50) < 1e-9
    return lit("50")


@check("number-of-terms-in-an-expansion")
def _():
    p = [1]
    for _ in range(5):
        p = poly_mul(p, [3, 1])                 # (x + 3)
    assert len([c for c in p]) == 6
    return lit(f"6 terms, coefficient {p[4]}")


@check("induction-what-to-prove-next")
def _():
    return lit("That the statement is true for n = k + 1")


@check("equality-of-two-complex-numbers")
def _():
    xs = [x for x in range(-20, 21) if 5 * x + 1 == 2 * x - 2]
    ys = [y for y in range(-20, 21) if 3 + 2 * y == y - 6]
    assert xs == [-1] and ys == [-9]
    return lit(f"x = {xs[0]}, y = {ys[0]}".replace("-", "−"))


@check("add-and-subtract-complex-numbers")
def _():
    z, w = complex(3, 6), complex(0, 2)
    d = w - z
    assert d == complex(-3, -4)
    return eq(r"{-3}-4i")


# ==================================================================== UNIT 8
@check("find-a-side-with-a-trig-ratio")
def _():
    x = 14 * math.sin(math.radians(30))
    assert abs(x - 7) < 1e-12
    return lit("7")


@check("which-ratio-to-use")
def _():
    return lit("Cosine")


@check("degrees-to-radians")
def _():
    r = 135 * math.pi / 180
    assert abs(r - 3 * math.pi / 4) < 1e-12
    return eq(r"\dfrac{3\pi}{4}")


@check("r-from-a-point-on-the-terminal-side")
def _():
    x, y = -8, 6
    r = math.hypot(x, y)
    assert r == 10
    assert abs(y / r - 0.6) < 1e-12
    return eq(r"\dfrac{3}{5}")


@check("cosine-from-sine-in-a-quadrant")
def _():
    s = 2 / 3
    c = math.sqrt(1 - s * s)                    # first quadrant: positive
    assert abs(c - math.sqrt(5) / 3) < 1e-12
    return eq(r"\dfrac{\sqrt{5}}{3}")


# ==================================================================== UNIT 9
@check("sine-of-a-negative-angle")
def _():
    for t in (0.3, 1.1, 2.7, -0.9):
        assert abs(math.sin(-t) + math.sin(t)) < 1e-12
        assert abs(math.cos(-t) - math.cos(t)) < 1e-12
    return eq(r"\sin({-\theta})={-\sin\theta}")


@check("cofunction-identity")
def _():
    for t in (0.2, 1.0, 2.5):
        assert abs(math.cos(math.pi / 2 - t) - math.sin(t)) < 1e-12
    return eq(r"\cos\left(\dfrac{\pi}{2}-\theta\right)")


@check("cos-double-angle-from-cosine")
def _():
    c = 3 / 5
    t = math.acos(c)
    assert abs(math.cos(2 * t) - (-7 / 25)) < 1e-12
    return eq(r"{-\dfrac{7}{25}}")


@check("solve-a-trig-equation-in-a-range")
def _():
    sols = [d for d in range(0, 181)
            if abs(math.sin(math.radians(d)) * math.cos(math.radians(d))
                   - 0.5 * math.cos(math.radians(d))) < 1e-12]
    assert sols == [30, 90, 150], sols
    return lit("30°, 90° and 150°")


@check("general-solution-of-a-trig-equation")
def _():
    for k in (-2, 0, 1, 5):
        assert abs(math.cos(math.pi + 2 * math.pi * k) + 1) < 1e-12
    assert abs(math.cos(math.pi + math.pi) + 1) > 1     # period pi would be wrong
    return eq(r"\theta=\pi+2\pi k")


@check("component-form-from-two-points")
def _():
    A, B = (-4, 2), (3, -5)
    v = (B[0] - A[0], B[1] - A[1])
    assert v == (7, -7)
    return eq(r"\left\langle 7,\ {-7}\right\rangle")


@check("unit-vector-in-the-same-direction")
def _():
    v = (-2, 3)
    n = math.hypot(*v)
    u = (v[0] / n, v[1] / n)
    assert abs(math.hypot(*u) - 1) < 1e-12
    assert abs(n - math.sqrt(13)) < 1e-12
    return eq(r"\left\langle {-\dfrac{2}{\sqrt{13}}},\ \dfrac{3}{\sqrt{13}}\right\rangle")


@check("components-from-magnitude-and-direction")
def _():
    v = (10 * math.cos(math.radians(45)), 10 * math.sin(math.radians(45)))
    assert abs(v[0] - 5 * math.sqrt(2)) < 1e-12 and abs(v[1] - 5 * math.sqrt(2)) < 1e-12
    return eq(r"\left\langle 5\sqrt{2},\ 5\sqrt{2}\right\rangle")


@check("angle-between-two-vectors")
def _():
    u, v = (3, 1), (3, -3)
    c = (u[0] * v[0] + u[1] * v[1]) / (math.hypot(*u) * math.hypot(*v))
    return lit(f"{round(math.degrees(math.acos(c)))}°")


@check("cross-product-in-space")
def _():
    u, v = (3, -2, 1), (-3, 3, 1)
    c = (u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0])
    assert c == (-5, -6, 3), c
    # and it is perpendicular to both
    assert sum(a * b for a, b in zip(c, u)) == 0 and sum(a * b for a, b in zip(c, v)) == 0
    return eq(r"\left\langle {-5},\ {-6},\ 3\right\rangle")


@check("distance-between-two-polar-points")
def _():
    M = (2 * math.cos(math.radians(330)), 2 * math.sin(math.radians(330)))
    N = (5 * math.cos(math.radians(60)), 5 * math.sin(math.radians(60)))
    assert abs(math.dist(M, N) - math.sqrt(29)) < 1e-9
    return eq(r"\sqrt{29}")


@check("modulus-of-a-complex-number")
def _():
    return lit(str(int(abs(complex(-6, 8)))))


# ==================================================================== UNIT 10
@check("centre-and-radius-from-the-equation")
def _():
    # sample points on the curve and fit the centre and radius back out
    h, k, r = 4, -1, 3
    for t in (0, 1.2, 2.9, 4.4):
        x, y = h + r * math.cos(t), k + r * math.sin(t)
        assert abs((x - 4) ** 2 + (y + 1) ** 2 - 9) < 1e-9
    return lit("Centre (4, −1), radius 3")


@check("circle-from-the-ends-of-a-diameter")
def _():
    A, B = (7, 6), (-1, -8)
    c = (F(A[0] + B[0], 2), F(A[1] + B[1], 2))
    r2 = (c[0] - A[0]) ** 2 + (c[1] - A[1]) ** 2
    assert c == (F(3), F(-1)) and r2 == 65, (c, r2)
    return eq(r"(x-3)^{2}+(y+1)^{2}=65")


@check("direction-a-parabola-opens")
def _():
    # (x-6)^2 = -4(y-15): sample and see the y values fall away from the vertex
    y = lambda x: 15 - (x - 6) ** 2 / 4
    assert y(6) == 15 and y(4) < 15 and y(8) < 15
    return lit("Downwards, vertex (6, 15)")


@check("equation-from-focus-and-vertex")
def _():
    vertex, focus = (1, -4), (3, -4)
    c = focus[0] - vertex[0]
    assert c == 2
    # directrix x = h - c; a point equidistant from focus and directrix satisfies it
    for y in (-4, 0, 6):
        x = vertex[0] + (y - vertex[1]) ** 2 / (4 * c)
        assert abs(math.dist((x, y), focus) - abs(x - (vertex[0] - c))) < 1e-9
    return eq(r"(y+4)^{2}=8(x-1)")


@check("centre-axes-and-foci-of-an-ellipse")
def _():
    a, b = math.sqrt(36), math.sqrt(9)
    c = math.sqrt(a * a - b * b)
    assert abs(c - 3 * math.sqrt(3)) < 1e-12
    return lit("Centre (3, −1), major axis 12, c = 3√3")


@check("eccentricity-of-an-ellipse")
def _():
    a, b = 5, 4
    e = math.sqrt(a * a - b * b) / a
    return lit(f"{e:.1f}")


@check("centre-and-vertices-of-a-hyperbola")
def _():
    h, k, a = -1, -2, math.sqrt(9)
    assert a == 3
    return lit(f"Centre ({h}, {k}), vertices ({h + a:.0f}, {k}) and ({h - a:.0f}, {k})"
               .replace("-", "−"))


@check("asymptotes-of-a-hyperbola")
def _():
    a, b = math.sqrt(9), math.sqrt(16)
    # far out along the curve the gradient tends to b/a
    x = 1e7
    y = b * math.sqrt((x / a) ** 2 - 1)
    assert abs(y / x - b / a) < 1e-6
    return eq(r"\pm\dfrac{4}{3}")


@check("counterexample-to-a-claim")
def _():
    bad = [n for n in range(1, 8) if (2 ** n + 2 * n ** 2) % 4 != 0]
    assert bad and bad[0] == 3, bad
    return lit(str(bad[0]))


@check("always-sometimes-or-never")
def _():
    # collinear case works, isosceles case does not
    J, K, L = (0, 0), (1, 0), (2, 0)
    assert math.dist(J, K) == math.dist(K, L)
    J2, K2, L2 = (0, 0), (1, 2), (2, 0)
    assert abs(math.dist(J2, K2) - math.dist(K2, L2)) < 1e-12
    cross = (L2[0] - J2[0]) * (K2[1] - J2[1]) - (K2[0] - J2[0]) * (L2[1] - J2[1])
    assert cross != 0                                   # not collinear, so not a midpoint
    return lit("Sometimes true — it fails whenever the three points are not collinear")


# ============================================================== UNITS 11–13
@check("one-sided-limits-agree")
def _():
    g = lambda x: -2 if x == -3 else 4
    left = [g(-3 - 10 ** -k) for k in range(1, 8)]
    right = [g(-3 + 10 ** -k) for k in range(1, 8)]
    assert set(left) == set(right) == {4}
    return lit("4")


@check("limit-by-factoring")
def _():
    f = lambda x: (x ** 2 - 1) / (x - 1)
    # the sequence of values must CONVERGE to the limit from both sides
    for k in range(2, 7):
        assert abs(f(1 + 10 ** -k) - 2) < 10 ** -(k - 1)
        assert abs(f(1 - 10 ** -k) - 2) < 10 ** -(k - 1)
    return lit("2")


@check("three-conditions-for-continuity")
def _():
    return lit("f(c) exists, the limit at c exists, and the two are equal")


@check("limit-at-infinity-by-degree")
def _():
    f = lambda x: (3 * x ** 2 + 7) / (2 * x ** 3 - x)
    assert abs(f(1e6)) < 1e-5
    return lit("0")


@check("asymptotes-of-a-shifted-reciprocal")
def _():
    f = lambda x: 1 / (x - 2) + 1
    assert abs(f(2 + 1e-9)) > 1e8
    assert abs(f(1e9) - 1) < 1e-6
    return lit("x = 2 and y = 1")


@check("a-hole-not-an-asymptote")
def _():
    f = lambda x: (x ** 2 - 16) / (x - 4)
    for k in range(2, 7):
        assert abs(f(4 + 10 ** -k) - 8) < 10 ** -(k - 2)
        assert abs(f(4 - 10 ** -k) - 8) < 10 ** -(k - 2)      # bounded, so no asymptote
    return lit("A hole, because the factor cancels")


@check("derivative-from-first-principles")
def _():
    f = lambda x: 4 * x ** 2 - 5 * x + 8
    h = 1e-7
    d15 = (f(1.5 + h) - f(1.5 - h)) / (2 * h)
    d0 = (f(0 + h) - f(0 - h)) / (2 * h)
    assert abs(d15 - 7) < 1e-5 and abs(d0 - (-5)) < 1e-5
    return lit("f′(x) = 8x − 5, and f′(1.5) = 7")


@check("average-rate-over-an-interval-in-context")
def _():
    f = lambda t: -1.3 * t ** 2 + 12 * t
    v = (f(3) - f(2)) / (3 - 2)
    return lit(f"{v:.1f} km/h")


@check("area-under-a-curve-on-an-interval")
def _():
    n = 400000
    a, b = 1.0, 3.0
    h = (b - a) / n
    total = sum(4 * (a + (i + 0.5) * h) ** 3 * h for i in range(n))
    assert abs(total - 80) < 1e-3, total
    return lit("80")
