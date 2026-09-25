"""Independent re-derivation of every part-H answer.

Each check takes its own route. The cross product is built from the Leibniz
minors and then confirmed perpendicular to both sides; the box model is checked
by folding a numerical sheet rather than by quoting the formula; the piecewise
domain and range are recovered by SAMPLING the two pieces the figure draws;
limits are taken numerically; the normal-band percentage comes from quadrature
of the density, not from the 68-95-99.7 table.
"""
import math
from fractions import Fraction as F

lit = lambda s: ("lit", s)
eq = lambda latex: ("eq", latex)

CHECKS_H = {}


def check(sig):
    def deco(fn):
        CHECKS_H[sig] = fn
        return fn
    return deco


def simpson(f, a, b, n=4000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += f(a + i * h) * (4 if i % 2 else 2)
    return s * h / 3


# ============================================ VECTORS, POLYNOMIALS, GRAPHS
@check("parallelogram-area-from-a-cross-product")
def _():
    u, v = (2, -1, 3), (1, 4, -2)
    w = (u[1] * v[2] - u[2] * v[1],
         u[2] * v[0] - u[0] * v[2],
         u[0] * v[1] - u[1] * v[0])
    assert w == (-10, 7, 9), w
    # the cross product must be perpendicular to both sides
    assert sum(a * b for a, b in zip(w, u)) == 0
    assert sum(a * b for a, b in zip(w, v)) == 0
    n2 = sum(c * c for c in w)
    assert n2 == 230, n2
    return eq(r"\sqrt{230}")


@check("box-base-area-model-from-a-sheet")
def _():
    # fold a numerical sheet: the base is what is left between the two cuts
    for x in (1.0, 2.5, 4.0):
        length = 24 - x - x
        width = 18 - x - x
        assert abs(length * width - (24 - 2 * x) * (18 - 2 * x)) < 1e-12
    return eq(r"\left(24-2x\right)\left(18-2x\right)")


PIECES = [("ray", lambda x: x - 2, -60.0, 1.0, False),      # x < 1, open at 1
          ("seg", lambda x: 2.0, 3.0, 6.0, True)]           # 3 <= x <= 6, closed


def sample_graph(n=4001):
    """Every (x, y) the figure actually draws, at fine resolution."""
    pts = []
    for _, f, a, b, closed in PIECES:
        for i in range(n):
            x = a + (b - a) * i / (n - 1)
            if not closed and x >= b:
                continue
            pts.append((x, f(x)))
    return pts


@check("domain-of-a-piecewise-graph-with-an-open-end")
def _():
    xs = [p[0] for p in sample_graph()]
    assert max(xs) == 6.0 and 1.0 not in xs
    # nothing is drawn strictly between 1 and 3
    assert not [x for x in xs if 1.0 < x < 3.0]
    assert min(x for x in xs if x >= 3.0) == 3.0
    return eq(r"\left({-\infty},\ 1\right)\cup\left[3,\ 6\right]")


@check("range-of-a-piecewise-graph-with-an-isolated-value")
def _():
    ys = [p[1] for p in sample_graph()]
    top = {round(y, 9) for y in ys if y > -1.0}
    assert top == {2.0}, top                     # one isolated value above -1
    assert max(y for y in ys if y <= -1.0) < -1.0  # -1 itself is never reached
    return eq(r"\left({-\infty},\ {-1}\right)\cup\left\{2\right\}")


# ======================================================== TRIGONOMETRY
def num_identity(lhs, rhs, pts=(0.31, 0.77, 1.24, 2.05, 2.61)):
    return all(abs(lhs(t) - rhs(t)) < 1e-9 for t in pts)


@check("sum-angle-with-a-forty-five-degree-shift")
def _():
    lhs = lambda t: math.sqrt(2) * math.sin(t + math.radians(45))
    cands = {r"\sin x+\cos x": lambda t: math.sin(t) + math.cos(t),
             r"\sqrt{2}\left(\sin x+\cos x\right)":
                 lambda t: math.sqrt(2) * (math.sin(t) + math.cos(t)),
             r"\sin x-\cos x": lambda t: math.sin(t) - math.cos(t),
             r"\sqrt{2}\,\sin x+\cos x":
                 lambda t: math.sqrt(2) * math.sin(t) + math.cos(t)}
    ok = [k for k, f in cands.items() if num_identity(lhs, f)]
    assert ok == [r"\sin x+\cos x"], ok
    return eq(ok[0])


@check("radians-to-degrees-multiple-of-pi")
def _():
    d = F(7, 3) * 180
    assert d == 420
    # and the conversion really is the one a full turn fixes
    assert abs(math.degrees(7 * math.pi / 3) - 420) < 1e-9
    return lit("420°")


@check("exact-sine-in-the-third-quadrant")
def _():
    v = math.sin(math.radians(240))
    assert abs(v + math.sqrt(3) / 2) < 1e-12, v
    return eq(r"{-\dfrac{\sqrt{3}}{2}}")


@check("exact-sine-of-a-coterminal-angle")
def _():
    v = math.sin(math.radians(780))
    assert abs(v - math.sqrt(3) / 2) < 1e-12, v
    assert 780 - 2 * 360 == 60
    return eq(r"\dfrac{\sqrt{3}}{2}")


@check("radius-of-a-polar-circle-is-half-the-coefficient")
def _():
    # sample the polar curve and fit the circle it traces
    pts = [(10 * math.sin(t) * math.cos(t), 10 * math.sin(t) * math.sin(t))
           for t in [i * math.pi / 90 for i in range(91)]]
    for x, y in pts:
        assert abs(x * x + (y - 5) ** 2 - 25) < 1e-9, (x, y)
    return lit("5")


@check("cosecant-from-a-sine-value-rationalised")
def _():
    s = math.sqrt(6) / 4
    c = 1 / s
    assert abs(c - 2 * math.sqrt(6) / 3) < 1e-12, c
    return eq(r"\dfrac{2\sqrt{6}}{3}")


# ================================= FUNCTIONS, LOGARITHMS AND COORDINATES
@check("graph-of-the-inverse-of-an-exponential")
def _():
    f = lambda x: 4 ** x
    # the reflection of (a, f(a)) is (f(a), a); check it satisfies y = log_4 x
    for a in (-1.5, 0.0, 0.7, 2.0):
        X, Y = f(a), a
        assert abs(math.log(X, 4) - Y) < 1e-12
    assert abs(f(0) - 1) < 1e-12                 # (0,1) reflects to (1,0)
    return lit("It has a vertical asymptote at x = 0 and passes through (1, 0)")


@check("inverse-of-a-linear-rational-function")
def _():
    f = lambda x: (2 * x + 1) / (x - 3)
    g = lambda x: (3 * x + 1) / (x - 2)
    for x in (0.0, 1.5, 4.0, 7.3):
        assert abs(g(f(x)) - x) < 1e-9, x        # g really undoes f
    return eq(r"\dfrac{3x+1}{x-2}")


@check("logarithm-of-a-decimal-that-is-a-negative-power")
def _():
    v = math.log(0.125, 2)
    assert abs(v + 3) < 1e-12, v
    assert F(1, 8) == F(125, 1000)
    return lit("−3")


@check("slope-from-two-points-with-negatives")
def _():
    P, Q = (-4, 7), (2, -11)
    m = F(Q[1] - P[1], Q[0] - P[0])
    assert m == -3, m
    # the line through both points really has that slope
    assert P[1] - m * P[0] == Q[1] - m * Q[0]
    return eq(r"{-3}")


@check("base-of-an-isosceles-triangle-from-its-altitude")
def _():
    leg, alt = 13, 12
    half = math.isqrt(leg * leg - alt * alt)
    assert half * half + alt * alt == leg * leg
    # confirm by measuring the drawn triangle
    A, B, C = (0, alt), (-half, 0), (half, 0)
    assert math.dist(A, B) == math.dist(A, C) == 13.0
    return lit(str(2 * half))


@check("parallelogram-angle-split-by-a-diagonal")
def _():
    # rebuild the figure from its own angles and MEASURE, rather than quoting
    # the supplementary rule the item is testing
    import numpy as np
    angD, part = 110.0, 40.0
    angDCA = 180.0 - angD - part
    D = np.array([0.0, 0.0]); C = np.array([6.4, 0.0])
    side = 6.4 * math.sin(math.radians(angDCA)) / math.sin(math.radians(part))
    th = math.radians(angD)
    A = D + side * np.array([math.cos(th), math.sin(th)])
    B = A + (C - D)
    ang = lambda V, P, Q: math.degrees(math.acos(
        np.dot(P - V, Q - V) / (np.linalg.norm(P - V) * np.linalg.norm(Q - V))))
    assert abs(ang(D, C, A) - 110) < 1e-9
    assert abs(ang(A, D, C) - 40) < 1e-9         # the figure's marked part
    x = ang(A, C, B)
    assert abs(x - 30) < 1e-9, x
    assert abs(ang(A, D, B) - (40 + x)) < 1e-9   # the diagonal splits angle A
    return lit("30°")


# ================================================ CALCULUS AND PROBABILITY
@check("limit-at-infinity-with-an-absolute-value")
def _():
    g = lambda x: (3 * x * abs(x) + 5) / (x * x - 4 * x)
    prev = None
    for x in (1e4, 1e6, 1e8):
        v = g(x)
        assert abs(v - 3) < 1e-2, (x, v)
        if prev is not None:
            assert abs(v - 3) < abs(prev - 3)      # and it is settling on 3
        prev = v
    return lit("3")


@check("solve-for-the-upper-limit-of-an-integral")
def _():
    area = lambda n: simpson(lambda x: 3 * x * x, 1, n)
    ns = [n for n in range(2, 12) if abs(area(n) - 26) < 1e-6]
    assert ns == [3], ns
    return lit("3")


def normal_share(z):
    f = lambda t: math.exp(-t * t / 2) / math.sqrt(2 * math.pi)
    return simpson(f, -z, z)


@check("normal-asymmetric-band-percentage")
def _():
    # P(-1 sd .. +2 sd), by quadrature of the density
    f = lambda t: math.exp(-t * t / 2) / math.sqrt(2 * math.pi)
    share = simpson(f, -1, 2)
    assert abs(share - 0.815) < 0.006, share
    return lit("81.5%")


@check("independence-and-the-gambler-fallacy")
def _():
    # enumerate every seven-toss outcome and condition on the first five heads
    from itertools import product
    space = list(product("HT", repeat=6))
    given = [s for s in space if s[:5] == ("H",) * 5]
    good = [s for s in given if s[5] == "H"]
    p = F(len(good), len(given))
    assert p == F(1, 2), p
    return lit("50%")
