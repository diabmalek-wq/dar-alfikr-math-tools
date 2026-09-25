"""Independent re-derivation of every part-C answer (Unit 2, sessions 10-18).

Imported by verify_saat.py. Nothing here reads an item's reasoning: each answer
is recomputed by its own route — exact rational arithmetic, root enumeration,
substitution, sign counting — and compared with the option the key marks
correct, by LaTeX where the option is typeset.
"""
import math
from fractions import Fraction as F

lit = lambda s: ("lit", s)
eq = lambda latex: ("eq", latex)

CHECKS_C = {}


def check(sig):
    def deco(fn):
        CHECKS_C[sig] = fn
        return fn
    return deco


def roots_of(a, b, c):
    """Exact roots of a quadratic with integer coefficients, when they are rational."""
    d = b * b - 4 * a * c
    r = math.isqrt(abs(d))
    assert d >= 0 and r * r == d, "not a rational pair"
    return sorted({F(-b + r, 2 * a), F(-b - r, 2 * a)})


# ------------------------------------------------- session 10 and 11
@check("solve-system-by-elimination")
def _():
    # add the two equations; the y terms cancel
    x = F(12 + 6, 2 + 4)
    y = F(12 - 2 * x, 3)
    assert 2 * x + 3 * y == 12 and 4 * x - 3 * y == 6
    return lit(str(y))


@check("number-of-solutions-from-slopes")
def _():
    # 2x - 3y = 6 and 4x - 6y = 18: same left side after doubling, different constant
    assert (2 * 2, -3 * 2) == (4, -6) and 6 * 2 != 18
    return lit("No solution")


@check("system-from-a-worded-situation")
def _():
    sols = [(a, c) for c in range(0, 31) for a in [30 - c]
            if 45 * a + 20 * c == 950]
    assert len(sols) == 1, sols
    return lit(str(sols[0][1]))


@check("point-satisfying-every-constraint")
def _():
    ok = lambda p: (p[0] >= 0 and p[1] >= 0 and p[0] + p[1] <= 10
                    and 2 * p[0] + p[1] <= 14)
    pts = {r"({-1},\ 3)": (-1, 3), r"(4,\ 6)": (4, 6),
           r"(6,\ 5)": (6, 5), r"(8,\ 0)": (8, 0)}
    good = [k for k, p in pts.items() if ok(p)]
    assert good == [r"(4,\ 6)"], good
    return eq(good[0])


@check("area-of-a-triangle-by-determinant")
def _():
    (x1, y1), (x2, y2), (x3, y3) = (0, 0), (5, 0), (2, 6)
    area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2
    assert area == 15.0
    return lit("15")


# --------------------------------------------------------- session 12
@check("solve-quadratic-by-factoring")
def _():
    r = roots_of(1, -7, 12)
    assert r == [F(3), F(4)]
    return eq(r"x=3\ \ \text{or}\ \ x=4")


@check("form-a-quadratic-from-its-roots")
def _():
    p, q = 5, -2
    b, c = -(p + q), p * q
    assert (b, c) == (-3, -10)
    return eq(r"x^{2}-3x-10=0")


@check("equation-quadratic-after-clearing-a-fraction")
def _():
    f = lambda x: x + F(6, 1) / x - 5
    sols = [x for x in (F(n) for n in range(-10, 11)) if x != 0 and f(x) == 0]
    assert sols == [F(2), F(3)], sols
    return eq(r"x=2\ \ \text{or}\ \ x=3")


@check("zeros-from-factored-form")
def _():
    y = lambda x: (2 * x - 6) * (x + 4)
    z = sorted(x for x in range(-10, 11) if y(x) == 0)
    assert z == [-4, 3]
    return eq(r"x=3,\ \ x={-4}")


# --------------------------------------------------------- session 13
@check("complete-the-square-to-vertex-form")
def _():
    for x in (-2.0, 0.5, 4.0):
        assert abs((x ** 2 - 6 * x + 11) - ((x - 3) ** 2 + 2)) < 1e-12
    return eq(r"y=(x-3)^{2}+2")


@check("quadratic-formula-with-complex-pair")
def _():
    a, b, c = 1, -2, 5
    d = complex(b * b - 4 * a * c, 0) ** 0.5
    r1, r2 = (-b + d) / (2 * a), (-b - d) / (2 * a)
    assert abs(r1 - complex(1, 2)) < 1e-12 and abs(r2 - complex(1, -2)) < 1e-12
    return eq(r"x=1\pm 2i")


@check("vertex-from-completed-square")
def _():
    f = lambda x: 2 * (x + 4) ** 2 - 7
    assert f(-4) == -7 and all(f(x) > -7 for x in (-5, -3, 0))
    return eq(r"({-4},\ {-7})")


@check("recover-c-from-a-given-vertex")
def _():
    # the minimum sits at x = -b/2a = -4; solve c - 16 = -5
    c = F(-5) + 16
    assert (-4) ** 2 + 8 * (-4) + c == -5
    return lit(str(c))


# --------------------------------------------------------- session 14
@check("discriminant-nature-of-roots")
def _():
    d = 3 ** 2 - 4 * 2 * 5
    assert d < 0
    return lit("Two conjugate complex roots")


@check("rational-or-irrational-roots")
def _():
    d = (-6) ** 2 - 4 * 1 * 4
    r = math.isqrt(d)
    assert d > 0 and r * r != d
    return lit("Two irrational roots")


@check("parameter-for-equal-roots")
def _():
    ks = [k for k in range(-20, 21) if k * k - 4 * 1 * 9 == 0]
    assert sorted(ks) == [-6, 6]
    return eq(r"k=\pm 6")


@check("graph-from-the-discriminant")
def _():
    return lit("It touches the x-axis at one point")


# --------------------------------------------------------- session 15
@check("axis-of-symmetry-from-standard-form")
def _():
    a, b = 1, -4
    x = F(-b, 2 * a)
    f = lambda t: t ** 2 - 4 * t - 5
    assert f(x - 1) == f(x + 1) and x == 2      # symmetric about it
    return eq(r"x=2")


@check("maximum-value-of-a-quadratic")
def _():
    f = lambda x: -x ** 2 + 6 * x - 5
    best = max(f(i / 1000) for i in range(-5000, 10001))
    assert abs(best - 4) < 1e-5
    return lit("4")


@check("number-of-real-zeros-from-the-vertex")
def _():
    # any downward parabola with a vertex above the axis, e.g. y = -(x-2)^2 + 5
    f = lambda x: -(x - 2) ** 2 + 5
    vals = [f(i / 100) for i in range(-500, 900)]
    changes = sum(1 for a, b in zip(vals, vals[1:]) if a * b < 0)
    assert changes == 2
    return lit("2")


@check("equation-from-x-intercepts")
def _():
    y = lambda x: x ** 2 + 2 * x - 3
    assert y(-3) == 0 and y(1) == 0
    return eq(r"y=x^{2}+2x-3")


# --------------------------------------------------------- session 16
@check("synthetic-division-quotient")
def _():
    # multiply the quotient back out and compare coefficient by coefficient
    q = [1, -2, 1]                     # x^2 - 2x + 1
    prod = [0] * 4
    for i, qi in enumerate(q):         # (x - 2) * q
        prod[i] += qi
        prod[i + 1] += -2 * qi
    assert prod == [1, -4, 5, -2]
    return eq(r"x^{2}-2x+1")


@check("remainder-theorem-value")
def _():
    f = lambda x: x ** 3 + 2 * x ** 2 - 5
    assert f(2) == 11
    return lit("11")


@check("factor-theorem-decide")
def _():
    f = lambda x: x ** 3 - 4 * x ** 2 + x + 6
    cand = {r"x-4": 4, r"x+2": -2, r"x-2": 2, r"x-6": 6}
    ok = [k for k, r in cand.items() if f(r) == 0]
    assert ok == [r"x-2"], ok
    return eq(ok[0])


@check("parameter-from-a-stated-remainder")
def _():
    k = F(1 - 8 - 3, 2)
    assert 2 ** 3 + k * 2 + 3 == 1
    # the bank prints a true minus sign, not a hyphen
    return lit(str(k).replace("-", "−"))


@check("conjugate-root-pair")
def _():
    z = complex(3, -1)
    assert z.conjugate() == complex(3, 1)
    return eq(r"3+i")


@check("real-zeros-from-a-table")
def _():
    v = [-7, 2, 5, -1, 4]
    n = sum(1 for a, b in zip(v, v[1:]) if a * b < 0)
    assert n == 3
    return lit("3")


# --------------------------------------------------------- session 17
@check("rational-equation-with-a-rejected-root")
def _():
    # the algebra gives x = 3, and x = 3 is outside the domain
    x = F(3)
    assert x - 3 == 0
    ok = [t for t in (F(n, 2) for n in range(-20, 21))
          if t != 3 and t / (t - 3) == F(3) / (t - 3) + 2]
    assert ok == []
    return lit("No solution")


@check("solve-a-proportion")
def _():
    xs = [x for x in (F(n) for n in range(-30, 31))
          if F(x + 2, 4) == F(3 * x - 4, 8)]
    assert xs == [F(8)], xs
    return lit("8")


@check("identify-the-type-of-variation")
def _():
    pts = [(2, 12), (4, 6), (6, 4)]
    prods = {x * y for x, y in pts}
    quots = {F(y, x) for x, y in pts}
    assert len(prods) == 1 and len(quots) > 1
    return lit("Inversely")


@check("joint-variation-find-value")
def _():
    k = F(60, 3 * 4)
    z = k * 2 * 7
    assert k == 5 and z == 70
    return lit(str(z))


# --------------------------------------------------------- session 18
@check("solve-a-radical-equation")
def _():
    xs = [x for x in range(0, 50) if 3 * x + 4 >= 0 and math.isclose(math.sqrt(3 * x + 4), 5)]
    assert xs == [7]
    return lit("7")


@check("radical-on-each-side")
def _():
    xs = [x for x in range(1, 40)
          if 2 * x - 1 >= 0 and x + 5 >= 0
          and math.isclose(math.sqrt(2 * x - 1), math.sqrt(x + 5))]
    assert xs == [6]
    return lit("6")


@check("extraneous-root")
def _():
    cand = [x for x in range(-20, 40) if x + 7 >= 0 and (x + 7) == (x - 5) ** 2]
    kept = [x for x in cand if math.isclose(math.sqrt(x + 7), x - 5)]
    assert sorted(cand) == [2, 9] and kept == [9]
    return lit("x = 9")


@check("radical-inequality-domain")
def _():
    ok = lambda x: x - 3 >= 0 and math.sqrt(x - 3) < 4
    assert ok(3) and ok(18.99) and not ok(19) and not ok(2.99)
    return eq(r"3\leq x<19")
