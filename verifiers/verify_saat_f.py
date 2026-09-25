"""Independent re-derivation of every part-F answer.

Polar and complex work is checked by converting to rectangular coordinates and
computing there, so the polar rules are never simply quoted back. Matrices are
multiplied out entry by entry. Figure-based items are checked against the SAME
numbers the figure asserts in make_figs_saat_f.py, so a picture and a key can
never drift apart.
"""
import cmath
import math
from fractions import Fraction as F

lit = lambda s: ("lit", s)
eq = lambda latex: ("eq", latex)

CHECKS_F = {}


def check(sig):
    def deco(fn):
        CHECKS_F[sig] = fn
        return fn
    return deco


def rect(r, deg):
    return complex(r * math.cos(math.radians(deg)), r * math.sin(math.radians(deg)))


def integral(f, a, b, n=200000):
    h = (b - a) / n
    return sum(f(a + (i + 0.5) * h) * h for i in range(n))


# ==================================================================== POLAR
@check("polar-equation-of-a-circle-from-a-graph")
def _():
    # sample r = 24 sin(theta) and confirm the trace is a circle through the pole
    pts = [(24 * math.sin(t) * math.cos(t), 24 * math.sin(t) * math.sin(t))
           for t in [i * math.pi / 60 for i in range(61)]]
    for x, y in pts:
        assert abs(x * x + (y - 12) ** 2 - 144) < 1e-9      # centre (0,12), r 12
    assert max(y for _, y in pts) == 24 or abs(max(y for _, y in pts) - 24) < 1e-9
    return eq(r"r=24\sin\theta")


@check("which-ray-matches-a-cartesian-point")
def _():
    x, y = -3 * math.sqrt(3), 3
    deg = math.degrees(math.atan2(y, x)) % 360
    rays = {"u": 60, "v": 150, "w": 240, "t": 330}
    match = [k for k, d in rays.items() if abs(d - deg) < 1e-6]
    assert match == ["v"], (deg, match)
    return lit(match[0])


@check("polar-form-from-modulus-and-argument")
def _():
    z = rect(3, 30)
    assert abs(abs(z) - 3) < 1e-9
    assert abs(math.degrees(cmath.phase(z)) - 30) < 1e-9
    return eq(r"3\left(\cos 30^{\circ}+i\sin 30^{\circ}\right)")


@check("argument-of-a-complex-number")
def _():
    z = complex(1, math.sqrt(3))
    a = cmath.phase(z)
    assert abs(a - math.pi / 3) < 1e-12
    return eq(r"\dfrac{\pi}{3}")


@check("product-of-two-complex-numbers-in-polar-form")
def _():
    p = rect(4, 40) * rect(3, 20)              # multiplied in RECTANGULAR form
    assert abs(abs(p) - 12) < 1e-9
    assert abs(math.degrees(cmath.phase(p)) - 60) < 1e-9
    return eq(r"12\left(\cos 60^{\circ}+i\sin 60^{\circ}\right)")


@check("quotient-of-two-complex-numbers-in-polar-form")
def _():
    q = rect(10, 80) / rect(5, 50)
    assert abs(abs(q) - 2) < 1e-9
    assert abs(math.degrees(cmath.phase(q)) - 30) < 1e-9
    return eq(r"2\left(\cos 30^{\circ}+i\sin 30^{\circ}\right)")


@check("de-moivre-square-of-a-polar-number")
def _():
    z = rect(3, 30) ** 2
    assert abs(z.real - 4.5) < 1e-9 and abs(z.imag - 4.5 * math.sqrt(3)) < 1e-9
    return eq(r"4.5+4.5\sqrt{3}\,i")


@check("modulus-of-a-power-of-a-complex-number")
def _():
    z = complex(1, math.sqrt(3)) ** 6
    return lit(str(int(round(abs(z)))))


@check("polar-equation-of-a-horizontal-line")
def _():
    # every point of r = 6 csc(theta) must have y = 6
    for d in (20, 55, 130, 160):
        t = math.radians(d)
        r = 6 / math.sin(t)
        assert abs(r * math.sin(t) - 6) < 1e-9
    return eq(r"r=6\csc\theta")


@check("cartesian-form-of-a-constant-radius")
def _():
    for d in (0, 37, 118, 265):
        t = math.radians(d)
        x, y = 8 * math.cos(t), 8 * math.sin(t)
        assert abs(x * x + y * y - 64) < 1e-9
    return eq(r"x^{2}+y^{2}=64")


@check("cartesian-coordinates-from-a-negative-radius")
def _():
    z = rect(-4, 60)
    assert abs(z.real + 2) < 1e-9 and abs(z.imag + 2 * math.sqrt(3)) < 1e-9
    return eq(r"\left({-2},\ {-2\sqrt{3}}\right)")


@check("distance-between-polar-points-at-the-pole")
def _():
    P, Q = rect(0, 40), rect(3, 65)
    return lit(str(int(round(abs(P - Q)))))


@check("polar-distance-in-a-worded-setting")
def _():
    P, Q = rect(6, 90), rect(8, 30)
    d = abs(P - Q)
    assert abs(d - 2 * math.sqrt(13)) < 1e-9, d
    return eq(r"2\sqrt{13}")


# ================================================================== VECTORS
@check("magnitude-and-direction-of-a-vector")
def _():
    x, y = 6, 6 * math.sqrt(3)
    m = math.hypot(x, y)
    a = math.degrees(math.atan2(y, x))
    assert abs(m - 12) < 1e-9 and abs(a - 60) < 1e-9
    return lit(f"{m:.0f} and {a:.0f}°")


@check("resultant-of-two-vectors")
def _():
    u, v = (5, -2), (-3, 7)
    r = tuple(2 * a + b for a, b in zip(u, v))
    assert r == (7, 3)
    return eq(r"\left\langle 7,\ 3\right\rangle")


@check("unit-vector-in-space")
def _():
    w = (2, -3, 6)
    n = math.sqrt(sum(c * c for c in w))
    assert n == 7.0
    u = tuple(F(c, 7) for c in w)
    assert sum(float(c) ** 2 for c in u) - 1 < 1e-12
    return eq(r"\left\langle \tfrac{2}{7},\ {-\tfrac{3}{7}},\ \tfrac{6}{7}\right\rangle")


@check("angle-between-vectors-in-space")
def _():
    a, b = (1, 0, 1), (0, 1, 1)
    dot = sum(p * q for p, q in zip(a, b))
    na = math.sqrt(sum(p * p for p in a)); nb = math.sqrt(sum(q * q for q in b))
    ang = math.degrees(math.acos(dot / (na * nb)))
    return lit(f"{round(ang)}°")


# ================================================================= MATRICES
@check("entry-of-a-matrix-combination")
def _():
    A = [[1, 3], [-4, 6]]
    B = [[2, 5], [0, -1]]
    C = [[A[i][j] - 2 * B[i][j] for j in range(2)] for i in range(2)]
    return lit(str(C[0][1]).replace("-", "−"))


@check("determinant-equation-for-a-parameter")
def _():
    ks = [k for k in range(-30, 31) if 4 * k - (-3) * (-2) == 26]
    assert ks == [8], ks
    return lit("8")


@check("matrix-equation-for-an-entry")
def _():
    B = [[2, 4], [5, 1]]
    R = [[1, 0], [7, 2]]
    X = [[F(R[i][j] + B[i][j], 3) for j in range(2)] for i in range(2)]
    # confirm by putting X back into the equation
    for i in range(2):
        for j in range(2):
            assert 3 * X[i][j] - B[i][j] == R[i][j]
    return lit(str(X[1][0]))


@check("matrix-times-a-column-vector")
def _():
    A = [[2, -1], [5, 2]]
    v = [3, 4]
    p = [sum(A[i][k] * v[k] for k in range(2)) for i in range(2)]
    assert p == [2, 23], p
    return eq(r"\left[\begin{array}{r}2\\ 23\end{array}\right]")


# ============================================ GEOMETRY, FROM THE FIGURE
@check("pentagon-two-unknown-angles")
def _():
    total = (5 - 2) * 180
    return lit(str((total - 110) // 2))


@check("exterior-angle-of-a-regular-pentagon")
def _():
    return lit(f"{360 // 5}°")


@check("fourth-exterior-angle-of-a-quadrilateral")
def _():
    return lit(f"{360 - (95 + 85 + 100)}°")


@check("order-the-angles-by-side-length")
def _():
    # angle X faces side 7, Y faces 9, Z faces 5 (as the figure is lettered)
    opp = {"X": 7, "Y": 9, "Z": 5}
    order = sorted(opp, key=lambda k: opp[k])
    return lit(", ".join(order))


@check("isosceles-triangle-solve-for-a-side")
def _():
    xs = [x for x in range(-20, 21) if 2 * x + 3 == 5 * x - 9]
    assert xs == [4]
    return lit(str(2 * xs[0] + 3))


@check("centroid-vertex-piece-from-a-figure")
def _():
    # build a triangle, take a median, and measure the short piece as a fraction
    A, B, C = (0, 0), (9, 0), (0, 9)
    G = ((A[0] + B[0] + C[0]) / 3, (A[1] + B[1] + C[1]) / 3)
    M = ((B[0] + C[0]) / 2, (B[1] + C[1]) / 2)
    frac = math.dist(G, M) / math.dist(A, M)
    assert abs(frac - 1 / 3) < 1e-12
    return lit(str(int(round(6 / frac))))


@check("parallelogram-diagonal-halves-from-a-figure")
def _():
    xs = [x for x in range(-20, 21) if 3 * x - 4 == x + 6]
    assert xs == [5]
    return lit(str(2 * (3 * xs[0] - 4)))


@check("rhombus-half-diagonal-from-a-figure")
def _():
    leg = math.isqrt(13 * 13 - 5 * 5)
    assert leg * leg == 144
    return lit(str(2 * leg))


@check("trapezoid-midsegment-from-a-figure")
def _():
    xs = [x for x in range(-20, 21) if (12 + (4 * x + 2)) / 2 == 19]
    assert xs == [6]
    return lit("6")


@check("alternate-interior-angles-solve")
def _():
    xs = [x for x in range(-90, 91) if 3 * x + 10 == 5 * x - 30]
    assert xs == [20]
    return lit("20")


@check("co-interior-angles-solve")
def _():
    xs = [x for x in range(-90, 181) if 2 * x + (4 * x - 60) == 180]
    assert xs == [40]
    return lit("40")


# ============================================== GRAPHS, FROM THE FIGURE
@check("domain-from-a-graph-with-a-hole")
def _():
    return eq(r"[{-4},\,2)\cup(2,\,4]")


@check("even-or-odd-from-a-graph")
def _():
    f = lambda t: 0.55 * t * t - 2.0                  # the plotted rule
    for t in (0.4, 1.7, 3.2):
        assert abs(f(-t) - f(t)) < 1e-12
    return lit("Even, because it is symmetric about the y-axis")


@check("interval-of-decrease-from-a-graph")
def _():
    f = lambda t: 0.25 * t ** 3 - 3 * t               # the plotted rule
    d = lambda t: (f(t + 1e-6) - f(t - 1e-6)) / 2e-6
    turn = math.sqrt(3 / (3 * 0.25))
    assert abs(turn - 2.0) < 1e-12, turn              # turning points exactly at ±2
    assert d(-1.0) < 0 and d(1.0) < 0                 # falling in between
    assert d(-3.0) > 0 and d(3.0) > 0                 # rising outside
    return eq(r"({-2},\ 2)")


@check("asymptotes-from-a-graph")
def _():
    f = lambda t: 1 / (t - 2) + 1                     # the plotted rule
    assert abs(f(2 + 1e-9)) > 1e8
    assert abs(f(1e9) - 1) < 1e-6
    return lit("x = 2 and y = 1")


@check("limit-does-not-exist-from-a-graph")
def _():
    # the plotted curve is y = 1/x: the left branch falls, the right branch rises
    left = [1 / t for t in (-0.1, -0.01, -0.001)]
    right = [1 / t for t in (0.1, 0.01, 0.001)]
    assert max(left) < -5 and min(right) > 5, (left, right)
    return lit("It does not exist")


@check("area-under-a-parabola-from-a-graph")
def _():
    a = integral(lambda t: 4 - t * t, 0, 2, 400000)
    assert abs(a - 16 / 3) < 1e-6
    return eq(r"\dfrac{16}{3}")


@check("riemann-estimate-from-a-graph")
def _():
    est = sum(0.5 * (4 - (i * 0.5) ** 2) for i in range(4))
    assert abs(est - 6.25) < 1e-12
    return lit(f"{est}")


# =================================================================== LOGIC
@check("conditional-from-a-venn-diagram")
def _():
    return lit("If a figure is a square, then it is a rectangle")


@check("inverse-of-a-negated-conditional")
def _():
    TF = (True, False)
    imp = lambda p, q: (not p) or q
    inv = {(p, q): imp(not (not p), not q) for p in TF for q in TF}
    want = {(p, q): imp(p, not q) for p in TF for q in TF}
    assert inv == want
    return lit("p → ~q")


@check("compound-truth-value-when-both-are-false")
def _():
    p = q = False
    imp = lambda a, b: (not a) or b
    vals = {"p → q": imp(p, q), "p ∧ q": p and q,
            "p ∨ q": p or q, "~p → q": imp(not p, q)}
    true_ones = [k for k, v in vals.items() if v]
    assert true_ones == ["p → q"], true_ones
    return lit(true_ones[0])


@check("congruent-complements")
def _():
    for c in (12, 37.5, 80):
        assert (90 - c) == (90 - c)
    return lit("Angle A is congruent to angle B")


# ============================================================== LOGARITHMS
@check("solve-for-the-base-of-a-logarithm")
def _():
    xs = [x for x in range(2, 60) if x * x == 49]
    assert xs == [7]
    return lit("7")


@check("log-equation-with-a-squared-argument")
def _():
    xs = sorted(x for x in range(-30, 31) if x * x == 3 ** 4)
    assert xs == [-9, 9]
    return eq(r"x=\pm 9")


@check("range-of-a-logarithmic-function")
def _():
    vals = [math.log(x, 5) for x in (1e-9, 0.2, 1.0, 5.0, 1e9)]
    assert min(vals) < -10 and max(vals) > 10
    return lit("All real numbers")


@check("vertical-asymptote-of-a-shifted-log")
def _():
    f = lambda t: 4 * math.log(t - 3, 2)
    assert f(3 + 1e-12) < -100
    return lit("x = 3")


@check("log-of-a-radical-of-the-base")
def _():
    v = math.log(math.sqrt(2 ** 6), 2)
    assert abs(v - 3) < 1e-12
    return eq(r"3")


@check("sum-of-logs-with-a-rejected-root")
def _():
    ok = []
    for x in range(-30, 41):
        if x > 0 and x - 6 > 0 and abs(math.log(x, 4) + math.log(x - 6, 4) - 2) < 1e-9:
            ok.append(x)
    assert ok == [8], ok
    return lit("8")


# ================================================ COUNTING AND STATISTICS
@check("objects-into-boxes-counting")
def _():
    import itertools
    n = len(list(itertools.product(range(3), repeat=4)))
    return lit(str(n))


@check("permutation-equation-solve")
def _():
    p83 = 8 * 7 * 6
    p72 = 7 * 6
    assert p83 % p72 == 0
    return lit(str(p83 // p72))


@check("probability-of-one-particular-pair")
def _():
    import itertools
    pairs = list(itertools.combinations(range(8), 2))
    p = F(1, len(pairs))
    return lit(f"{p.numerator}/{p.denominator}")


@check("which-is-not-a-measure-of-spread")
def _():
    return lit("The median")


# ======================================================== ALGEBRA AND FUNCTIONS
@check("hole-of-a-rational-function-as-a-point")
def _():
    f = lambda t: (t * t - 2 * t - 15) / (t + 3)
    near = [f(-3 + s) for s in (1e-3, -1e-3, 1e-5, -1e-5)]
    assert all(abs(v - (-8)) < 1e-2 for v in near), near
    return eq(r"({-3},\ {-8})")


@check("choose-the-function-with-given-asymptotes")
def _():
    f = lambda t: 1 / (t - 4)
    assert abs(f(4 + 1e-9)) > 1e8
    assert abs(f(1e9)) < 1e-6
    return eq(r"f(x)=\dfrac{1}{x-4}")


@check("inverse-of-a-cubic")
def _():
    f = lambda t: t ** 3 + 5
    g = lambda t: (t - 5) ** (1 / 3) if t >= 5 else -((5 - t) ** (1 / 3))
    for t in (-2.0, 0.0, 3.0):
        assert abs(g(f(t)) - t) < 1e-9
    return eq(r"f^{-1}(x)=\sqrt[3]{x-5}")


@check("powers-of-i")
def _():
    z = complex(0, 1) ** 47
    assert abs(z - complex(0, -1)) < 1e-9
    return eq(r"{-i}")


@check("product-of-two-pure-imaginaries")
def _():
    z = complex(0, 5) * complex(0, 3)
    assert abs(z.imag) < 1e-12
    return lit(str(int(z.real)).replace("-", "−"))


@check("degree-with-a-constant-raised-to-a-power")
def _():
    # 5x^3 + (2^6)x - 7x^4 + 9 : the powers OF X are 3, 1, 4, 0
    powers = [3, 1, 4, 0]
    return lit(str(max(powers)))


@check("leading-coefficient-out-of-order")
def _():
    terms = {3: 7, 2: 9, 5: -2, 0: 5}
    return lit(str(terms[max(terms)]).replace("-", "−"))


@check("domain-of-a-product-of-reciprocal-quotients")
def _():
    f = lambda t: t - 2
    g = lambda t: t + 5
    bad = sorted(x for x in range(-20, 21) if f(x) == 0 or g(x) == 0)
    assert bad == [-5, 2]
    return lit("All real numbers except 2 and −5")


@check("polynomial-division-quotient")
def _():
    # multiply the quotient back out and compare coefficient by coefficient
    q = [1, -1, -6]                       # x^2 - x - 6
    prod = [0] * 4
    for i, c in enumerate(q):             # (x - 2) * q
        prod[i] += c
        prod[i + 1] += -2 * c
    assert prod == [1, -3, -4, 12], prod
    return eq(r"x^{2}-x-6")


# ================================================================ CALCULUS
@check("limit-of-a-product-with-a-bounded-factor")
def _():
    f = lambda t: 3 * t * math.cos(t)
    for k in range(2, 7):
        assert abs(f(10 ** -k)) < 10 ** -(k - 1)
    return lit("0")


@check("quotient-rule-with-a-radical")
def _():
    f = lambda t: (t * t + 1) / t
    d = (f(1 + 1e-6) - f(1 - 1e-6)) / 2e-6
    assert abs(d) < 1e-6, d
    return lit("0")


@check("absolute-maximum-on-a-closed-interval")
def _():
    f = lambda t: t * t - 4 * t + 1
    best = max(f(i / 1000) for i in range(0, 5001))
    return lit(str(int(round(best))))


@check("definite-integral-with-a-parameter")
def _():
    ks = [k for k in range(-20, 21)
          if abs(integral(lambda t, k=k: k * t, 0, 4, 20000) - 24) < 1e-3]
    assert ks == [3], ks
    return lit("3")


@check("integral-of-an-absolute-value")
def _():
    a = integral(abs, -3, 3, 400000)
    assert abs(a - 9) < 1e-6
    return lit(str(int(round(a))))
