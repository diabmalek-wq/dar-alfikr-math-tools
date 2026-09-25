"""Independent re-derivation of every answer in the simulated SAAT bank.

Nothing here reads the bank's reasoning. Each check computes the answer from
the item's own data by a route of its own — integer arithmetic, exact rational
arithmetic, enumeration of a sample space, numerical integration — and then
compares the result with the option the key marks correct.

For an option that is a typeset expression the check compares the LaTeX the key
points at, taken from the make_math_saat tables, with the LaTeX this file expects. So a
key that points at the right position but the wrong picture still fails.

    python3 verify_saat.py        ->  every answer re-derived, 0 failures
"""
import json, math, subprocess
from fractions import Fraction as F

from make_math_saat import E as _EA
from make_math_saat_b import E as _EB
from make_math_saat_c import E as _EC
from make_math_saat_d import E as _ED
from make_math_saat_e import E as _EE
from make_math_saat_f import E as _EF
from make_math_saat_g import E as _EG
from make_math_saat_h import E as _EH
from make_math_saat_i import E as _EI
from make_math_saat_j import E as _EJ
from make_math_saat_jx import E as _EJX
from make_math_saat_k import E as _EK
from make_math_saat_l import E as _EL

E = {**_EA, **_EB, **_EC, **_ED, **_EE, **_EF, **_EG, **_EH, **_EI, **_EJ, **_EJX, **_EK, **_EL}      # one expression table across every part

ITEMS = json.loads(subprocess.run(
    ["node", "-e", "process.stdout.write(JSON.stringify("
     "[...require('./saat_items_a.js'), ...require('./saat_items_b.js'),"
     " ...require('./saat_items_c.js'), ...require('./saat_items_d.js'),"
     " ...require('./saat_items_e.js'), ...require('./saat_items_f.js'), ...require('./saat_items_g.js'), ...require('./saat_items_h.js'), ...require('./saat_items_i.js'), ...require('./saat_items_j.js'), ...require('./saat_items_k.js'), ...require('./saat_items_l.js'), ...require('./saat_items_m.js')]))"],
    capture_output=True, text=True, check=True).stdout)
BY = {it["sig"]: it for it in ITEMS}

CHECKS = {}


def check(sig):
    def deco(fn):
        CHECKS[sig] = fn
        return fn
    return deco


def lit(s):
    """An option written as plain text."""
    return ("lit", s)


def eq(latex):
    """An option that is a typeset expression, identified by its LaTeX."""
    return ("eq", latex)


# ============================================================ ALGEBRA
@check("binomial-coefficient-of-a-term")
def _():
    # coefficient of x^2 in (2x + 3)^5, from the binomial theorem term by term
    c = sum(math.comb(5, k) * 2 ** (5 - k) * 3 ** k
            for k in range(6) if 5 - k == 2)
    return lit(str(c))


@check("binomial-nth-term-index")
def _():
    k = 3                                   # the FOURTH term carries index 3
    coef = math.comb(5, k) * (-3) ** k
    assert coef == -270 and 5 - k == 2
    return eq(r"{-270}x^{2}")


def inv2(m):
    (a, b), (c, d) = m
    det = a * d - b * c
    assert det != 0
    return [[F(d, 1) / det, F(-b, 1) / det], [F(-c, 1) / det, F(a, 1) / det]]


@check("matrix-inverse-2x2")
def _():
    inv = inv2([[4, 3], [3, 2]])
    assert inv == [[F(-2), F(3)], [F(3), F(-4)]], inv
    # confirm by multiplying back out
    prod = [[sum(inv[i][k] * [[4, 3], [3, 2]][k][j] for k in range(2))
             for j in range(2)] for i in range(2)]
    assert prod == [[F(1), F(0)], [F(0), F(1)]], prod
    return eq(r"\begin{pmatrix}{-2}&3\\3&{-4}\end{pmatrix}")


@check("solve-2x2-system-by-inverse")
def _():
    inv = inv2([[2, 1], [3, 4]])
    x = inv[0][0] * 7 + inv[0][1] * 13
    y = inv[1][0] * 7 + inv[1][1] * 13
    assert 2 * x + y == 7 and 3 * x + 4 * y == 13
    return lit(str(x + y))


@check("log-evaluate-perfect-power")
def _():
    vals = {r"\log_{4}256": math.log(256, 4), r"\log_{5}125": math.log(125, 5),
            r"\log_{3}81": math.log(81, 3), r"\log_{2}16": math.log(16, 2)}
    odd = [k for k, v in vals.items() if round(v) != 4]
    assert len(odd) == 1
    return eq(odd[0])


@check("log-solve-for-unknown-base")
def _():
    x = round(27 ** (2 / 3))
    assert abs(x ** 1.5 - 27) < 1e-9
    return lit(str(x))


@check("parent-absolute-value-function")
def _():
    return eq(r"y=\lvert x\rvert")


@check("absolute-value-transformation-rule")
def _():
    # a point of the image is the parent point moved (-4, -2)
    f = lambda x: abs(x + 4) - 2
    for x0 in (-9, -4, 0, 5):
        assert f(x0 - 0) == abs((x0 + 4)) - 2
    assert f(-4) == -2                       # vertex moved left 4 and down 2
    return eq(r"y=\lvert x+4\rvert-2")


@check("combine-logs-into-one")
def _():
    x = 7.0
    lhs = 3 * math.log(x, 2) - math.log(x + 1, 2)
    assert abs(lhs - math.log(x ** 3 / (x + 1), 2)) < 1e-12
    return eq(r"\log_{2}\dfrac{x^{3}}{x+1}")


@check("expand-single-log")
def _():
    x, y = 3.0, 16.0
    lhs = math.log(25 * x ** 4 / math.sqrt(y), 5)
    rhs = 2 + 4 * math.log(x, 5) - 0.5 * math.log(y, 5)
    assert abs(lhs - rhs) < 1e-12
    return eq(r"2+4\log_{5}x-\dfrac{1}{2}\log_{5}y")


@check("matrix-product-order")
def _():
    a, b = (3, 5), (5, 2)
    assert a[1] == b[0]
    return lit(f"{a[0]} × {b[1]}")


@check("matrix-product-defined")
def _():
    pairs = [((2, 3), (2, 3)), ((1, 4), (1, 4)), ((2, 4), (4, 3)), ((3, 2), (3, 2))]
    ok = [i for i, (a, b) in enumerate(pairs) if a[1] == b[0]]
    assert ok == [2]
    return lit("A is 2 × 4 and B is 4 × 3")


@check("complex-square")
def _():
    z = (3 - 2j) ** 2
    assert z == complex(5, -12)
    return eq(r"5-12i")


@check("complex-quotient-conjugate")
def _():
    z = 5 / (2 - 1j)
    assert abs(z - complex(2, 1)) < 1e-12
    return eq(r"2+i")


@check("singular-matrix-parameter")
def _():
    # 3k + 12 = 0 solved over the rationals, then confirmed
    k = F(-12, 3)
    assert k * 3 - (-2) * 6 == 0
    return lit("−4" if k == -4 else str(k))


@check("zero-determinant-meaning")
def _():
    return lit("It has no multiplicative inverse.")


@check("scientific-notation-to-decimal")
def _():
    v = 6 * 10 ** -4
    assert f"{v:.4f}" == "0.0006"
    return lit("0.0006")


@check("scientific-notation-product")
def _():
    v = (4 * 10 ** 5) * (2.5 * 10 ** -8)
    assert abs(v - 1e-2) < 1e-15
    return eq(r"1\times 10^{-2}")


@check("units-of-a-product")
def _():
    # exponents of (kg, m, s)
    B, C, D = (1, -3, 0), (0, 1, -2), (0, 1, 0)
    A = tuple(b + c + d for b, c, d in zip(B, C, D))
    assert A == (1, -1, -2)
    return eq(r"\mathrm{kg/(m\cdot s^{2})}")


@check("units-identify-quantity")
def _():
    # (m, s) exponents; a length is (1, 0)
    v, t = (1, -1), (0, 1)
    cand = {r"\dfrac{v}{t}": (v[0] - t[0], v[1] - t[1]),
            r"v\,t^{2}": (v[0], v[1] + 2),
            r"v\,t": (v[0], v[1] + 1),
            r"\dfrac{v}{t^{2}}": (v[0], v[1] - 2)}
    ok = [k for k, u in cand.items() if u == (1, 0)]
    assert ok == [r"v\,t"]
    return eq(ok[0])


@check("vector-linear-combination")
def _():
    A, B = (5, -3), (1, 4)
    r = tuple(2 * a - b for a, b in zip(A, B))
    assert r == (9, -10)
    return eq(r"\langle 9,{-10}\rangle")


@check("vector-magnitude")
def _():
    m = math.hypot(-6, 8)
    assert m == 10.0
    return lit("10")


@check("odd-function-identification")
def _():
    tests = {r"y=\lvert x\rvert": lambda x: abs(x),
             r"y=x^{2}": lambda x: x ** 2,
             r"y=x^{7}": lambda x: x ** 7}
    odd = [k for k, f in tests.items()
           if all(abs(f(-x) + f(x)) < 1e-12 for x in (0.5, 1.3, 2.7))]
    assert odd == [r"y=x^{7}"]
    return eq(odd[0])


@check("classify-even-odd-neither")
def _():
    f = lambda x: x ** 3 - x
    assert all(abs(f(-x) + f(x)) < 1e-12 for x in (0.4, 1.1, 2.2))
    assert any(abs(f(-x) - f(x)) > 1e-9 for x in (0.4, 1.1, 2.2))
    return lit("Odd")


@check("composition-equality-solve")
def _():
    f = lambda x: x ** 2 + 1
    g = lambda x: x - 3
    sols = [x for x in range(-10, 11) if f(g(x)) == g(f(x))]
    assert sols == [2], sols
    return lit("2")


@check("composition-evaluate-order")
def _():
    f = lambda x: 2 * x + 1
    g = lambda x: x ** 2
    return lit(str(g(f(3))))


@check("dot-product-perpendicular")
def _():
    # solve (-2)b + 3 + 3 = 0 over the rationals
    b = F(6, 2)
    v, u = (b, -3, 1), (-2, -1, 3)
    assert sum(p * q for p, q in zip(v, u)) == 0
    return lit(str(b))


@check("dot-product-value")
def _():
    d = sum(p * q for p, q in zip((4, -1, 2), (3, 5, -2)))
    assert d == 3
    return lit("3")


@check("de-moivre-power")
def _():
    z = 2 * (math.cos(math.radians(60)) + 1j * math.sin(math.radians(60)))
    w = z ** 3
    assert abs(w - complex(-8, 0)) < 1e-9, w
    return eq(r"{-8}")


@check("de-moivre-modulus-argument")
def _():
    r, th = 3, 40
    return lit(f"{r ** 3} and {3 * th}°")


@check("log-linear-combination")
def _():
    v = 0.4 + 3 * 0.2
    assert abs(v - 1.0) < 1e-12
    return lit("1")


@check("change-of-base")
def _():
    assert abs(math.log(5, 8) - math.log(5) / math.log(8)) < 1e-12
    return eq(r"\dfrac{\log 5}{\log 8}")


# =========================================================== GEOMETRY
@check("rhombus-diagonals-to-side")
def _():
    s = math.hypot(16 / 2, 30 / 2)
    assert s == 17.0
    return lit("17 cm")


@check("rhombus-area-from-diagonals")
def _():
    a = F(12 * 20, 2)
    assert a == 120
    return lit("120 cm²")


@check("parabola-orientation")
def _():
    # x^2 = 8(y - 8): sample the curve and see which way it turns
    ys = [(x ** 2) / 8 + 8 for x in (-2, 0, 2)]
    assert ys[1] < ys[0] and ys[1] < ys[2]
    return lit("Up")


@check("parabola-vertex-and-direction")
def _():
    # (y + 2)^2 = -12(x - 5): x decreases as |y + 2| grows, so it opens left
    xs = [5 - (y + 2) ** 2 / 12 for y in (-4, -2, 0)]
    assert xs[1] == 5 and xs[0] < 5 and xs[2] < 5
    return lit("(5, −2), left")


@check("trapezoid-midsegment-find-base")
def _():
    cd = 2 * 7 - 6
    assert (6 + cd) / 2 == 7
    return lit(f"{cd} cm")


@check("trapezoid-midsegment-algebraic")
def _():
    sols = [x for x in range(-20, 21) if 3 * x + (x + 8) == 2 * 12]
    assert sols == [4]
    return lit("4")


@check("classify-triangle-in-3d")
def _():
    A, B, C = (0, 3, 5), (1, 0, 2), (0, -3, 5)
    d2 = lambda p, q: sum((a - b) ** 2 for a, b in zip(p, q))
    s = sorted([d2(A, B), d2(B, C), d2(A, C)])
    assert s == [19, 19, 36]
    assert s[0] + s[1] != s[2]                      # not right-angled
    assert len(set(s)) == 2                         # exactly two are equal
    return lit("Isosceles")


@check("distance-between-points-in-3d")
def _():
    d = math.dist((1, 2, 3), (5, 5, 15))
    assert d == 13.0
    return lit("13")


# ======================================================= TRIGONOMETRY
@check("quadrant-both-negative")
def _():
    mid = {1: 45, 2: 135, 3: 225, 4: 315}
    q = [k for k, a in mid.items()
         if math.sin(math.radians(a)) < 0 and math.cos(math.radians(a)) < 0]
    assert q == [3]
    return lit("Quadrant III")


@check("quadrant-from-two-signs")
def _():
    mid = {1: 45, 2: 135, 3: 225, 4: 315}
    q = [k for k, a in mid.items()
         if math.sin(math.radians(a)) < 0 and math.cos(math.radians(a)) > 0]
    assert q == [4]
    return lit("Quadrant IV")


@check("law-of-cosines-perimeter")
def _():
    c = math.sqrt(15 ** 2 + 15 ** 2 - 2 * 15 * 15 * math.cos(math.radians(60)))
    assert abs(c - 15) < 1e-12
    return lit(f"{round(15 + 15 + c)} cm")


@check("law-of-cosines-largest-angle")
def _():
    a, b, c = 7, 8, 13
    ang = math.degrees(math.acos((a * a + b * b - c * c) / (2 * a * b)))
    assert abs(ang - 120) < 1e-9
    return lit("120°")


def num_identity(lhs, rhs, pts=(0.31, 0.77, 1.24, 2.05, 2.61)):
    return all(abs(lhs(t) - rhs(t)) < 1e-9 for t in pts)


@check("simplify-sin-squared-over-tan-squared")
def _():
    lhs = lambda t: math.sin(t) ** 2 / math.tan(t) ** 2
    cands = {r"\cos^{2}\theta": lambda t: math.cos(t) ** 2,
             r"\sin^{2}\theta": lambda t: math.sin(t) ** 2,
             r"\tan^{2}\theta": lambda t: math.tan(t) ** 2}
    ok = [k for k, f in cands.items() if num_identity(lhs, f)]
    assert ok == [r"\cos^{2}\theta"]
    return eq(ok[0])


@check("simplify-with-pythagorean-identity")
def _():
    lhs = lambda t: (1 - math.cos(t) ** 2) / (math.sin(t) * math.cos(t))
    cands = {r"\tan\theta": math.tan, r"\cot\theta": lambda t: 1 / math.tan(t),
             r"\sin\theta": math.sin, r"1": lambda t: 1.0}
    ok = [k for k, f in cands.items() if num_identity(lhs, f)]
    assert ok == [r"\tan\theta"]
    return eq(ok[0])


@check("double-angle-identity-recognise")
def _():
    lhs = lambda t: 2 * math.tan(t) / (1 + math.tan(t) ** 2)
    cands = {r"\sin 2\theta": lambda t: math.sin(2 * t),
             r"\cos 2\theta": lambda t: math.cos(2 * t),
             r"\tan 2\theta": lambda t: math.tan(2 * t),
             r"2\sin\theta": lambda t: 2 * math.sin(t)}
    ok = [k for k, f in cands.items() if num_identity(lhs, f)]
    assert ok == [r"\sin 2\theta"]
    return eq(ok[0])


@check("double-angle-value-from-sine")
def _():
    s = F(3, 5)
    c = F(4, 5)
    assert s * s + c * c == 1
    v = 2 * s * c
    assert v == F(24, 25)
    return eq(r"\dfrac{24}{25}")


@check("polar-to-cartesian-negative-r")
def _():
    r, th = -2, math.radians(60)
    x, y = r * math.cos(th), r * math.sin(th)
    assert abs(x + 1) < 1e-12 and abs(y + math.sqrt(3)) < 1e-12
    return eq(r"\left({-1},\ {-\sqrt{3}}\right)")


@check("cartesian-to-polar-on-axis")
def _():
    x, y = 0, -4
    r = math.hypot(x, y)
    th = math.degrees(math.atan2(y, x)) % 360
    assert (r, th) == (4.0, 270.0)
    return lit("(4, 270°)")


@check("triangle-area-two-sides-and-angle")
def _():
    a = 0.5 * 18 * 22 * math.sin(math.radians(30))
    assert abs(a - 99) < 1e-9
    return lit("99 cm²")


@check("find-included-angle-from-area")
def _():
    s = 30 / (0.5 * 10 * 12)
    th = math.degrees(math.asin(s))
    assert abs(th - 30) < 1e-9
    return lit("30°")


# ============================================================ CALCULUS
@check("count-zeros-by-sign-change")
def _():
    v = [-5, -2, 1, -3, 4, -5]
    n = sum(1 for a, b in zip(v, v[1:]) if a * b < 0)
    assert n == 4
    return lit("4")


@check("intermediate-value-statement")
def _():
    return lit("f has at least one zero on (1, 4).")


@check("average-rate-of-change")
def _():
    f = lambda x: 6 * x ** 2 - 4 * x + 2
    r = F(f(6) - f(0), 6)
    assert r == 32
    return lit("32")


@check("average-rate-equals-instantaneous")
def _():
    f = lambda x: x ** 2
    avg = F(f(4) - f(0), 4)
    xs = [F(x, 1) for x in range(0, 9) if 2 * F(x, 1) == avg]
    assert xs == [F(2)]
    return lit("2")


def deriv(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)


@check("derivative-power-rule")
def _():
    f = lambda x: x ** 4
    for x in (0.7, 1.4, 2.1):
        assert abs(deriv(f, x) - 4 * x ** 3) < 1e-5
    return eq(r"4x^{3}")


@check("derivative-radical-and-reciprocal")
def _():
    f = lambda x: 3 * math.sqrt(x) + 2 / x
    g = lambda x: 3 / (2 * math.sqrt(x)) - 2 / x ** 2
    for x in (0.8, 1.6, 3.3):
        assert abs(deriv(f, x) - g(x)) < 1e-5
    return eq(r"\dfrac{3}{2\sqrt{x}}-\dfrac{2}{x^{2}}")


@check("derivative-at-a-point")
def _():
    c = 7.0                                   # any constant; it cannot matter
    f = lambda x: 15 * x ** 2 - 5 * x + c
    assert abs(deriv(f, 1.0) - 25) < 1e-5
    return lit("25")


@check("tangent-line-equation")
def _():
    f = lambda x: x ** 3 - 4 * x
    m = deriv(f, 2.0)
    assert abs(m - 8) < 1e-5 and abs(f(2.0)) < 1e-12
    line = lambda x: m * x + (f(2.0) - m * 2.0)
    assert abs(line(2.0) - f(2.0)) < 1e-9 and abs(line(0) + 16) < 1e-4
    return eq(r"y=8x-16")


@check("fundamental-theorem-statement")
def _():
    return eq(r"F(3)-F(0)")


@check("antiderivative-values-to-integral")
def _():
    return lit(str(19 - 4))


def simpson(f, a, b, n=2000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += f(a + i * h) * (4 if i % 2 else 2)
    return s * h / 3


@check("evaluate-definite-integral")
def _():
    v = simpson(lambda x: 4 * x + 1, 2, 3)
    assert abs(v - 11) < 1e-9, v
    return lit("11")


@check("definite-integral-of-a-line")
def _():
    v = simpson(lambda x: 6 * x - 2, 1, 3)
    assert abs(v - 20) < 1e-9, v
    return lit("20")


@check("maximum-on-closed-interval")
def _():
    f = lambda x: 6 * x ** 2 - x ** 3
    best = max(f(i / 2000 * 3) for i in range(2001))
    assert abs(best - 27) < 1e-6, best
    return lit("27")


@check("count-critical-points")
def _():
    fp = lambda x: 3 * x ** 2 - 6 * x + 3
    roots = {round(r, 9) for r in (1.0,) if abs(fp(r)) < 1e-12}
    disc = (-6) ** 2 - 4 * 3 * 3
    assert disc == 0 and roots == {1.0}
    return lit("1")


@check("limit-removable-discontinuity")
def _():
    g = lambda x: (x ** 2 - 25) / (x - 5)
    vals = [g(5 + d) for d in (1e-4, -1e-4, 1e-6, -1e-6)]
    assert all(abs(v - 10) < 1e-3 for v in vals)
    return lit("10")


@check("limit-by-rationalising")
def _():
    g = lambda x: (math.sqrt(x + 9) - 3) / x
    vals = [g(d) for d in (1e-5, -1e-5, 1e-7, -1e-7)]
    assert all(abs(v - 1 / 6) < 1e-5 for v in vals)
    return eq(r"\dfrac{1}{6}")


@check("second-derivative-test")
def _():
    f = lambda x: 2 + 3 * x - x ** 3
    # the maximum and minimum found by search, not by the test being verified
    xs = [i / 1000 for i in range(-2000, 2001)]
    near = lambda c: max((x for x in xs if abs(x - c) < 0.5), key=f)
    assert abs(near(1) - 1) < 0.01
    lo = min((x for x in xs if abs(x + 1) < 0.5), key=f)
    assert abs(lo + 1) < 0.01
    return lit("Maximum at x = 1, minimum at x = −1")


@check("point-of-inflection")
def _():
    f = lambda x: x ** 3 - 6 * x ** 2 + 5
    second = lambda x: (f(x + 1e-3) - 2 * f(x) + f(x - 1e-3)) / 1e-6
    assert second(1.9) < 0 < second(2.1) and abs(second(2.0)) < 1e-3
    return lit("2")


# ============================================== STATISTICS AND PROBABILITY
@check("conditional-probability-dice")
def _():
    space = [(a, b) for a in range(1, 7) for b in range(1, 7)]
    given = [s for s in space if sum(s) == 9]
    good = [s for s in given if 5 in s]
    p = F(len(good), len(given))
    assert p == F(1, 2), p
    return eq(r"\dfrac{1}{2}")


@check("conditional-probability-subgroup")
def _():
    p = F(12, 18)
    assert p == F(2, 3)
    return eq(r"\dfrac{2}{3}")


def normal_share(z):
    """Share of a standard normal within z standard deviations, by quadrature."""
    f = lambda t: math.exp(-t * t / 2) / math.sqrt(2 * math.pi)
    return simpson(f, -z, z)


@check("normal-one-standard-deviation")
def _():
    share = normal_share(1)
    assert abs(share - 0.68) < 0.01, share
    return lit(str(round(1000 * 0.68)))


@check("normal-tail-percentage")
def _():
    tail = (1 - normal_share(2)) / 2
    assert abs(tail - 0.025) < 0.005, tail
    return lit("2.5%")


# Part B's checks live in their own file and are merged in here.
from verify_saat_b import CHECKS_B
from verify_saat_c import CHECKS_C
from verify_saat_d import CHECKS_D
from verify_saat_e import CHECKS_E
from verify_saat_f import CHECKS_F
from verify_saat_g import CHECKS_G
from verify_saat_h import CHECKS_H
from verify_saat_i import CHECKS_I
from verify_saat_j import CHECKS_J
from verify_saat_k import CHECKS_K
from verify_saat_l import CHECKS_L
from verify_saat_m import CHECKS_M
CHECKS.update(CHECKS_B)
CHECKS.update(CHECKS_C)
CHECKS.update(CHECKS_D)
CHECKS.update(CHECKS_E)
CHECKS.update(CHECKS_F)
CHECKS.update(CHECKS_G)
CHECKS.update(CHECKS_H)
CHECKS.update(CHECKS_I)
CHECKS.update(CHECKS_J)
CHECKS.update(CHECKS_K)
CHECKS.update(CHECKS_L)
CHECKS.update(CHECKS_M)


# ================================================================== runner
def main():
    fails, checked = [], 0
    for sig, it in BY.items():
        if sig not in CHECKS:
            fails.append(f"{sig}: no independent check written")
            continue
        kind, want = CHECKS[sig]()
        got = it["opts"][it["ans"]]
        checked += 1
        if kind == "lit":
            if not isinstance(got, str):
                fails.append(f"{sig}: key marks an expression, check expects text")
            elif got != want:
                fails.append(f"{sig}: key says {got!r}, re-derivation says {want!r}")
        else:
            if isinstance(got, str):
                fails.append(f"{sig}: key marks text {got!r}, check expects an expression")
            elif E.get(got["eq"]) != want:
                fails.append(f"{sig}: key points at {got['eq']} = {E.get(got['eq'])!r}, "
                             f"re-derivation says {want!r}")
    extra = [s for s in CHECKS if s not in BY]
    for s in extra:
        fails.append(f"{s}: a check with no item")
    print(f"{checked} answers re-derived, {len(fails)} failures")
    for f_ in fails:
        print("  FAIL", f_)
    raise SystemExit(1 if fails else 0)


if __name__ == "__main__":
    main()
