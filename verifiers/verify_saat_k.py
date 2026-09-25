"""Independent re-derivation of every part-K answer.

The source's own answer strip is unreliable, so nothing here consults it.
Domains are found by SEARCHING for the inputs that raise an error rather than by
reading a denominator; the absolute-value integral is checked by quadrature, not
by the triangle rule the item is testing; the trig equation is swept round the
whole circle; and the figure-based counterexample is checked against the same
angle pairs the drawing asserts.
"""
import math
from fractions import Fraction as F

lit = lambda s: ("lit", s)
eq = lambda latex: ("eq", latex)

CHECKS_K = {}


def check(sig):
    def deco(fn):
        CHECKS_K[sig] = fn
        return fn
    return deco


def simpson(f, a, b, n=20000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += f(a + i * h) * (4 if i % 2 else 2)
    return s * h / 3


# ==================================================== THE FLOOR FUNCTION
@check("floor-of-a-negative-value")
def _():
    f = lambda x: math.floor(0.4 * x) + 2
    assert f(-7) == -1, f(-7)
    assert math.floor(-2.8) == -3            # down, not towards zero
    assert int(-2.8) == -2                   # and truncation is the trap
    return lit("−1")


@check("range-of-a-floor-function")
def _():
    g = lambda x: math.floor(abs(x)) + 5
    vals = {g(n / 20) for n in range(-400, 401)}
    assert min(vals) == 5
    assert all(float(v).is_integer() for v in vals)
    assert vals == set(range(5, max(vals) + 1))   # every integer from 5 up
    return lit("All integers greater than or equal to 5")


# ============================================ VECTORS, ANGLES AND MODELLING
@check("components-recombine-to-the-force")
def _():
    F0 = 137.0
    for deg in (5.0, 30.0, 44.0, 75.0, 89.0):
        t = math.radians(deg)
        h, v = F0 * math.cos(t), F0 * math.sin(t)
        assert abs(math.hypot(h, v) - F0) < 1e-9        # A holds for every angle
        assert h + v > F0                               # B fails
    t = math.radians(5)
    assert F0 * math.cos(t) > F0 / 2                    # C fails
    t = math.radians(75)
    assert F0 * math.sin(t) > F0 * math.cos(t)          # D fails
    return lit("The two components combine by Pythagoras to give F")


@check("angular-displacement-over-time")
def _():
    a = F(6, 9) * 2                       # in units of pi
    assert a == F(4, 3)
    assert abs(float(a) * math.pi - 4 * math.pi / 3) < 1e-12
    return eq(r"\dfrac{4\pi}{3}")


@check("displacement-is-not-distance")
def _():
    d = math.hypot(8, 6)
    assert d == 10.0
    assert 8 + 6 == 14                    # the path, which is the trap
    return lit("10 km")


@check("polar-equation-from-a-worded-circle")
def _():
    # sample r = 30 sin(theta) and confirm the trace touches (0,0) and (0,30)
    pts = [(30 * math.sin(t) * math.cos(t), 30 * math.sin(t) * math.sin(t))
           for t in [i * math.pi / 180 for i in range(181)]]
    for x, y in pts:
        assert abs(x * x + (y - 15) ** 2 - 225) < 1e-9
    assert min(y for _, y in pts) < 1e-9
    assert abs(max(y for _, y in pts) - 30) < 1e-9
    return eq(r"r=30\sin\theta")


@check("hijri-year-span-in-compound-growth")
def _():
    n = F(256)
    years = 1445 - 1442
    assert years == 3
    for _ in range(years):
        n *= F(5, 4)
    assert n == 500, n
    return lit("500")


# ==================================================== PLANE GEOMETRY
@check("two-reflections-in-parallel-lines")
def _():
    import numpy as np
    # reflect in x = 0 then in x = d; the composite must be a pure translation
    P = np.array([(1.0, 2.0), (3.0, -1.0), (-2.0, 4.0)])
    d = 2.5
    Q = P.copy(); Q[:, 0] *= -1              # reflect in x = 0
    R = Q.copy(); R[:, 0] = 2 * d - R[:, 0]  # reflect in x = d
    shift = R - P
    assert np.allclose(shift, shift[0])      # every point moves the same way
    assert np.allclose(shift[0], [2 * d, 0.0])
    return lit("A translation")


@check("which-value-cannot-be-an-exterior-angle")
def _():
    angles = [55, 65, 180 - 55 - 65]
    ext = {180 - a for a in angles}
    assert ext == {125, 115, 120}, ext
    bad = [v for v in (130, 125, 115, 120) if v not in ext]
    assert bad == [130], bad
    return lit("130°")


@check("counterexample-from-a-figure")
def _():
    # the same pairs the drawing asserts in make_figs_saat_k.py
    pairs = {"A": (40, 50), "B": (55, 35), "C": (65, 70), "D": (25, 65)}
    bad = [k for k, (a, b) in pairs.items() if a + b != 90]
    assert bad == ["C"], bad
    return lit("C")


@check("smallest-integer-third-side")
def _():
    ok = lambda n: 11 + 4 > n and 11 + n > 4 and 4 + n > 11
    good = [n for n in range(1, 30) if ok(n)]
    assert min(good) == 8 and max(good) == 14, good
    return lit("8 cm")


@check("dilation-with-a-negative-factor")
def _():
    k = F(-1, 2)
    img = (k * -6, k * 4)
    assert img == (F(3), F(-2)), img
    return eq(r"\left(3,\ {-2}\right)")


# ================================== WHAT THE ALGEBRA SETS AND THE DOMAIN KILLS
@check("restrictions-from-the-divisor-when-dividing")
def _():
    def q(x):
        a = (x * x + 5 * x - 14) / (x - 2)
        b = (x * x - 9) / (x + 3)
        return a / b                       # raises where either step fails
    bad = []
    for n in range(-100, 101):
        x = n / 10
        try:
            q(x)
        except ZeroDivisionError:
            bad.append(x)
    assert sorted(bad) == [-3.0, 2.0, 3.0], bad
    return lit("2, 3 and −3")


@check("composite-domain-with-a-hidden-exclusion")
def _():
    def h(x):
        return 1 / (math.sqrt(x + 5) - 4)
    bad = []
    for n in range(-200, 401):
        x = n / 10
        try:
            h(x)
        except (ValueError, ZeroDivisionError):
            bad.append(x)
    assert min(v for v in bad if v < 0) == -20.0      # everything below -5
    assert max(bad) == 11.0 and 11.0 in bad
    assert all(v < -5 or v == 11.0 for v in bad), [v for v in bad if -5 <= v != 11]
    return lit("x ≥ −5 and x ≠ 11")


@check("trig-equation-with-no-solution")
def _():
    # sweep the circle finely; a solution must satisfy the equation AND exist
    hits = []
    for i in range(0, 360000):
        t = i * 2 * math.pi / 360000
        if abs(math.cos(t)) < 1e-12:
            continue                            # sec and tan undefined here
        if abs(1 / math.cos(t) - math.tan(t)) < 1e-9:
            hits.append(t)
    assert hits == [], hits[:5]
    # and the algebra's candidate really is the excluded point
    assert abs(math.sin(math.pi / 2) - 1) < 1e-12
    assert abs(math.cos(math.pi / 2)) < 1e-15
    return lit("No solution")


# ======================================= WORK THAT DISAPPEARS IF YOU LOOK FIRST
@check("average-rate-zero-by-symmetry")
def _():
    f = lambda x: x * x - 6 * x + 5
    r = F(int(f(5)) - int(f(1)), 5 - 1)
    assert r == 0, r
    assert f(1) == f(5) == 0
    return lit("0")


@check("composition-with-a-constant-outer-function")
def _():
    f = lambda x: 4 * x * x - 3 * x
    g = lambda x: 7
    for x in (-2.5, 0.0, 1.3, 9.0):
        assert g(f(x)) == 7
    return eq(r"7")


@check("simplify-the-radical-before-differentiating")
def _():
    f = lambda x: 1 / (3 * (x ** -8) ** 0.25)
    d = lambda x: (f(x + 1e-6) - f(x - 1e-6)) / 2e-6
    for x in (0.7, 1.4, 2.6):
        assert abs(d(x) - 2 * x / 3) < 1e-5, x
        assert abs(f(x) - x * x / 3) < 1e-9          # it really is x^2/3
    return eq(r"\dfrac{2x}{3}")


@check("substitution-works-not-indeterminate")
def _():
    g = lambda x: (x + math.pi) / math.cos(x + math.pi)
    assert abs(math.cos(math.pi) + 1) < 1e-15        # the denominator is -1
    for h in (1e-4, -1e-4, 1e-7, -1e-7):
        assert abs(g(h) + math.pi) < 10 * abs(h), h
    return eq(r"{-\pi}")


@check("limit-versus-the-function-value")
def _():
    left, right, value = 5.0, -5.0, 9.0
    assert left != right                              # so no two-sided limit
    assert value not in (left, right)                 # and f(2) is irrelevant
    return lit("It does not exist")


@check("name-the-type-of-discontinuity")
def _():
    f = lambda x: 2 * x if x >= 3 else x * x - 5
    lo = [f(3 - h) for h in (1e-3, 1e-5, 1e-7)]
    hi = [f(3 + h) for h in (1e-3, 1e-5, 1e-7)]
    assert abs(lo[-1] - 4) < 1e-4 and abs(hi[-1] - 6) < 1e-4
    assert all(abs(v) < 1e6 for v in lo + hi)         # both finite: not infinite
    assert abs(lo[-1] - hi[-1]) > 1                   # unequal: not removable
    return lit("Jump")


@check("coefficient-from-an-absolute-value-integral")
def _():
    area = simpson(lambda x: abs(x - 1), -2, 4)
    assert abs(area - 9) < 1e-6, area
    k = F(36, 9)
    assert k == 4
    return lit("4")


# ==================================================== ALGEBRA, SEEN PROPERLY
@check("difference-of-squares-in-a-radical")
def _():
    f = lambda x: (x - 9) / (math.sqrt(x) - 3)
    for x in (0.5, 2.0, 16.0, 40.0):
        assert abs(f(x) - (math.sqrt(x) + 3)) < 1e-9, x
    return eq(r"\sqrt{x}+3")


@check("exponential-with-an-added-constant")
def _():
    xs = [x for x in range(-10, 11) if 4 ** (x - 1) + 6 == 70]
    assert xs == [4], xs
    return lit("4")


@check("values-for-which-a-series-converges")
def _():
    coef = [9, 18, 36, 72]
    # the ratio of consecutive terms, as a function of x, is a constant times x
    assert all(coef[i + 1] == 2 * coef[i] for i in range(3))
    # partial sums settle just inside |x| < 1/2 and run away just outside
    def partial(x, n=400):
        s, t = 0.0, 9.0
        for _ in range(n):
            s += t
            t *= 2 * x
        return s
    assert abs(partial(0.49, 5000) - 9 / (1 - 0.98)) < 1e-6   # settles
    assert abs(partial(0.51, 2000)) > 1e12                    # runs away
    return eq(r"\left\lvert x\right\rvert<\dfrac{1}{2}")
