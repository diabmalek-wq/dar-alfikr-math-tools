"""Independent re-derivation of every part-I answer.

Counting answers are settled by ENUMERATING the objects — every ordering of the
five books, every triple of the nine lattice points — rather than by quoting a
formula, so a mis-stated formula cannot pass. Complex arithmetic is done in
rectangular form with Python's own complex type. The trig values are checked
numerically and, where a range matters, the whole circle is swept to confirm
the answer is the only one inside it.
"""
import math
from fractions import Fraction as F
from itertools import combinations, permutations

lit = lambda s: ("lit", s)
eq = lambda latex: ("eq", latex)

CHECKS_I = {}


def check(sig):
    def deco(fn):
        CHECKS_I[sig] = fn
        return fn
    return deco


# =============================================== FUNCTIONS AND EXPRESSIONS
@check("expand-a-horizontally-shifted-quadratic")
def _():
    f = lambda x: x ** 2
    g = lambda x: x ** 2 - 8 * x + 16
    for x in (-3.0, 0.0, 2.5, 7.1):
        assert abs(f(x - 4) - g(x)) < 1e-12, x
    return eq(r"x^{2}-8x+16")


@check("which-expression-is-not-rational")
def _():
    # a rational expression is P/Q with P and Q POLYNOMIALS: every exponent of
    # the variable a non-negative integer. Coefficients may be any reals.
    tops = {
        r"\dfrac{\sqrt{x}+1}{x^{2}+4}": [F(1, 2), 0],       # exponents present
        r"\dfrac{\sqrt{7}\,x+1}{x^{2}+4}": [F(1), F(0)],
        r"\dfrac{x^{5}-3x+2}{x-6}": [F(5), F(1), F(0)],
        r"\dfrac{3}{x}": [F(0)],
    }
    bad = [k for k, es in tops.items()
           if any(e.denominator != 1 or e < 0 for e in es)]
    assert bad == [r"\dfrac{\sqrt{x}+1}{x^{2}+4}"], bad
    return eq(bad[0])


@check("radical-inequality-from-a-shaded-graph")
def _():
    # the figure shades every point under the curve, for x >= -2 only.
    # test a point the shading covers and one it does not
    inside, outside = (1.0, 0.5), (1.0, 2.5)
    f = lambda x: math.sqrt(x + 2)
    assert inside[1] <= f(inside[0]) and not (outside[1] <= f(outside[0]))
    assert abs(f(-2.0)) < 1e-12                 # the endpoint the figure marks
    return eq(r"y\leq\sqrt{x+2}")


@check("add-radicals-after-simplifying")
def _():
    v = math.sqrt(75) + math.sqrt(48) - math.sqrt(12)
    assert abs(v - 7 * math.sqrt(3)) < 1e-12, v
    return eq(r"7\sqrt{3}")


# ================================================== COMPLEX NUMBERS
@check("product-of-two-complex-binomials")
def _():
    z = complex(3, 2) * complex(2, -1)
    assert z == complex(8, 1), z
    return eq(r"8+i")


@check("power-of-one-plus-i-by-squaring")
def _():
    z = complex(1, 1)
    w = z
    for _ in range(5):
        w *= z                                   # sixth power by repeated product
    assert abs(w - complex(0, -8)) < 1e-9, w
    assert abs(z * z - complex(0, 2)) < 1e-12    # and (1+i)^2 really is 2i
    return eq(r"{-8i}")


# ======================================================== TRIGONOMETRY
@check("principal-value-of-an-inverse-cosine")
def _():
    d = math.degrees(math.acos(-math.sqrt(2) / 2))
    assert abs(d - 135) < 1e-9, d
    # sweep the circle: only one solution lies in the inverse cosine's range
    sols = [a for a in range(0, 360)
            if abs(math.cos(math.radians(a)) + math.sqrt(2) / 2) < 1e-9]
    assert [a for a in sols if 0 <= a <= 180] == [135], sols
    return lit("135°")


@check("cosine-of-a-negative-angle-is-even")
def _():
    v = math.cos(math.radians(-150))
    assert abs(v + math.sqrt(3) / 2) < 1e-12, v
    # and the cosine really is even, which is the point of the item
    for a in (17.0, 63.5, 211.0):
        assert abs(math.cos(math.radians(-a)) - math.cos(math.radians(a))) < 1e-12
    return eq(r"{-\dfrac{\sqrt{3}}{2}}")


@check("law-of-sines-find-a-side")
def _():
    # build the triangle in the plane from its angles and MEASURE the side
    angA, angB = 60.0, 45.0
    angC = 180 - angA - angB
    b = 14.0
    c = b * math.sin(math.radians(angC)) / math.sin(math.radians(angB))
    A = (0.0, 0.0)
    B = (c, 0.0)
    C = (b * math.cos(math.radians(angA)), b * math.sin(math.radians(angA)))
    x = math.dist(B, C)
    assert abs(x - 7 * math.sqrt(6)) < 1e-9, x
    return eq(r"7\sqrt{6}")


@check("inverse-sine-of-a-cosine-does-not-cancel")
def _():
    v = math.asin(math.cos(math.radians(30)))
    assert abs(v - math.pi / 3) < 1e-12, v
    return eq(r"\dfrac{\pi}{3}")


# =============================================== COUNTING AND PROBABILITY
@check("probability-of-one-specific-arrangement")
def _():
    orders = list(permutations("ABCDE"))
    p = F(1, len(orders))
    assert p == F(1, 120), p
    return eq(r"\dfrac{1}{120}")


@check("midpoint-square-is-half-the-area")
def _():
    # shoelace on the midpoint square of a square of ANY side
    for s in (10.0, 3.7, 41.2):
        M = [(s / 2, 0), (s, s / 2), (s / 2, s), (0, s / 2)]
        a = 0.5 * abs(sum(M[i][0] * M[(i + 1) % 4][1] - M[(i + 1) % 4][0] * M[i][1]
                          for i in range(4)))
        assert abs(a / (s * s) - 0.5) < 1e-12, (s, a / (s * s))
    return eq(r"\dfrac{1}{2}")


@check("probability-of-an-arrangement-with-end-constraints")
def _():
    people = ["b1", "b2", "b3", "g1", "g2"]
    orders = list(permutations(people))
    good = [o for o in orders if o[0].startswith("g") and o[-1].startswith("g")]
    p = F(len(good), len(orders))
    assert p == F(1, 10), p
    return eq(r"\dfrac{1}{10}")


@check("lines-determined-by-points")
def _():
    # 12 points on a circle: no three are collinear, so every pair gives a line
    n = len(list(combinations(range(12), 2)))
    assert n == 66
    return lit("66")


@check("probability-that-three-points-are-collinear")
def _():
    pts = [(i, j) for j in range(3) for i in range(3)]
    trip = list(combinations(pts, 3))
    coll = [t for t in trip
            if (t[1][0] - t[0][0]) * (t[2][1] - t[0][1])
            == (t[2][0] - t[0][0]) * (t[1][1] - t[0][1])]
    assert len(trip) == 84 and len(coll) == 8, (len(trip), len(coll))
    p = F(len(coll), len(trip))
    assert p == F(2, 21), p
    return eq(r"\dfrac{2}{21}")
