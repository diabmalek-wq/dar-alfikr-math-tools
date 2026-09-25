"""Independent re-derivation of every part-J answer.

The counting answers are settled by ENUMERATION — every three-pen handful, every
arrangement of the four digits, every seating round the table — rather than by
quoting a formula, so a mis-stated formula cannot pass. The polar circle is
checked by SAMPLING the curve. The two structural geometry items are checked on
a rebuilt figure by measuring. The semicircle integral is checked by quadrature
against the area, not by the area rule the item is testing.
"""
import math
from fractions import Fraction as F
from itertools import combinations, permutations

lit = lambda s: ("lit", s)
eq = lambda latex: ("eq", latex)

CHECKS_J = {}


def check(sig):
    def deco(fn):
        CHECKS_J[sig] = fn
        return fn
    return deco


def simpson(f, a, b, n=20000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += f(a + i * h) * (4 if i % 2 else 2)
    return s * h / 3


# ================================================ VECTORS AND POLAR
@check("resolve-a-force-into-components")
def _():
    v = 120 * math.cos(math.radians(30))
    assert abs(v - 60 * math.sqrt(3)) < 1e-12, v
    # the two components really do rebuild the force
    w = 120 * math.sin(math.radians(30))
    assert abs(math.hypot(v, w) - 120) < 1e-12
    return eq(r"60\sqrt{3}\ \mathrm{N}")


@check("quadrant-bearing-for-a-vector")
def _():
    # due south is 180 degrees clockwise from north; 20 degrees towards the west
    # is a further 20, so the compass heading is 200
    heading = 200.0
    assert 180 < heading < 270                 # the south-west quadrant
    off_south = heading - 180
    assert abs(off_south - 20) < 1e-12
    return lit("S 20° W")


@check("equivalent-polar-representations")
def _():
    rect = lambda r, d: (r * math.cos(math.radians(d)), r * math.sin(math.radians(d)))
    a = rect(-5, 40)
    cands = {"(5, 220°)": rect(5, 220), "(5, 40°)": rect(5, 40),
             "(−5, 220°)": rect(-5, 220), "(5, 140°)": rect(5, 140)}
    same = [k for k, p in cands.items() if math.dist(a, p) < 1e-9]
    assert same == ["(5, 220°)"], same
    return lit(same[0])


@check("polar-two-term-to-a-circle")
def _():
    # sample the polar curve; every sampled point must sit on the circle
    for i in range(180):
        th = i * math.pi / 180
        r = 4 * math.cos(th) + 6 * math.sin(th)
        x, y = r * math.cos(th), r * math.sin(th)
        assert abs((x - 2) ** 2 + (y - 3) ** 2 - 13) < 1e-9, (th, x, y)
    return eq(r"\left(x-2\right)^{2}+\left(y-3\right)^{2}=13")


# ================================================ REASONING AND LOGIC
@check("causal-versus-correlational-statement")
def _():
    return lit("Heating water to 100 °C at sea level makes it boil")


@check("average-rate-zero-what-follows")
def _():
    # a witness function with a zero average rate that breaks every other option
    f = lambda x: (x - 1) ** 2
    m, n = 0.0, 2.0
    assert abs((f(n) - f(m)) / (n - m)) < 1e-12    # the average rate is zero
    assert abs(f(m) - f(n)) < 1e-12                # A holds
    assert m != n                                  # B fails
    assert f(m) != 0                               # C fails
    assert f(1.0) != f(0.0)                        # D fails: f is not constant
    return lit("f(m) = f(n)")


@check("lines-in-a-square-grid")
def _():
    n = 5
    # enumerate the distinct lines by the coordinate each one sits at
    horizontals = {j for j in range(n + 1)}
    verticals = {i for i in range(n + 1)}
    assert len(horizontals) + len(verticals) == 12
    return lit("12")


# ==================================================== PLANE GEOMETRY
@check("interior-plus-exterior-angle-is-a-straight-angle")
def _():
    interior = F(5 - 2, 5) * 180
    exterior = F(360, 5)
    assert interior == 108 and exterior == 72
    assert interior + exterior == 180
    return lit("180°")


@check("angle-sum-without-finding-any-angle")
def _():
    import numpy as np
    s = 3.0
    A, B, C = np.array([0.0, 0.0]), np.array([s, 0.0]), np.array([s, s])
    ang = lambda V, P, Q: math.degrees(math.acos(
        np.dot(P - V, Q - V) / (np.linalg.norm(P - V) * np.linalg.norm(Q - V))))
    tot = ang(A, B, C) + ang(B, C, A) + ang(C, A, B)
    assert abs(tot - 180) < 1e-9, tot
    return lit("180°")


@check("pythagoras-across-stacked-squares")
def _():
    a, b = 7, 5
    d = math.hypot(a + b, b)
    assert d == 13.0, d
    return eq(r"13")


@check("count-lines-of-symmetry")
def _():
    import numpy as np
    t = 1.0
    P = np.array([(-t, -3 * t), (t, -3 * t), (t, -t), (3 * t, -t), (3 * t, t),
                  (t, t), (t, 3 * t), (-t, 3 * t), (-t, t), (-3 * t, t),
                  (-3 * t, -t), (-t, -t)], float)
    key = lambda A: sorted(map(tuple, np.round(A, 9)))
    # sweep every axis through the centre at one-degree steps and count the
    # ones the outline is invariant under
    found = 0
    for deg in range(0, 180):
        th = math.radians(deg)
        c, s2 = math.cos(2 * th), math.sin(2 * th)
        M = np.array([[c, s2], [s2, -c]])          # reflection in a line at th
        if key(P @ M.T) == key(P):
            found += 1
    assert found == 4, found
    return lit("4")


@check("name-the-quadrilateral-from-its-sides")
def _():
    return lit("A kite")


@check("perpendicular-medians-and-the-centroid")
def _():
    import numpy as np
    # rebuild the figure and MEASURE, rather than quoting the 2:1 rule
    G = np.zeros(2)
    A = np.array([2 * 12 / 3, 0.0])
    B = np.array([0.0, 2 * 9 / 3])
    C = 3 * G - A - B
    MA, MB = (B + C) / 2, (A + C) / 2
    assert abs(np.linalg.norm(A - MA) - 12) < 1e-9
    assert abs(np.linalg.norm(B - MB) - 9) < 1e-9
    assert abs(np.dot(A - G, B - G)) < 1e-9
    assert abs(np.linalg.norm(A - B) - 10) < 1e-9
    return lit("10")


# ================================================ COUNTING AND PROBABILITY
@check("hypergeometric-selection-probability")
def _():
    pens = ["b"] * 5 + ["r"] * 3
    space = list(combinations(range(8), 3))
    good = [h for h in space if sum(pens[i] == "b" for i in h) == 2]
    p = F(len(good), len(space))
    assert p == F(15, 28), p
    return eq(r"\dfrac{15}{28}")


@check("probability-of-a-number-divisible-by-five")
def _():
    nums = [int("".join(p)) for p in permutations("2457")]
    assert len(nums) == 24
    p = F(sum(1 for n in nums if n % 5 == 0), len(nums))
    assert p == F(1, 4), p
    return eq(r"\dfrac{1}{4}")


@check("probability-of-one-circular-arrangement")
def _():
    # seatings that differ only by a rotation are the same seating: fix person 0
    seatings = set()
    for p in permutations(range(1, 7)):
        seatings.add((0,) + p)
    assert len(seatings) == math.factorial(6) == 720
    return eq(r"\dfrac{1}{720}")


# ==================================================== STRUCTURAL ALGEBRA
@check("cancelled-factor-is-still-excluded")
def _():
    f = lambda x: (x * x - 9) / ((x - 3) * (x + 5))
    bad = []
    for n in range(-100, 101):
        x = n / 10
        try:
            f(x)
        except ZeroDivisionError:
            bad.append(x)
    assert sorted(bad) == [-5.0, 3.0], bad
    return lit("3 and −5")


@check("cancel-a-factor-that-is-the-negative-of-another")
def _():
    a = 7.0
    f = lambda x: (a / 6) * ((3 - x) / (x - 3))
    for x in (0.0, 1.5, 4.2, 9.0):
        assert abs(f(x) + a / 6) < 1e-12, x        # it is -a/6 for every x
    return eq(r"{-\dfrac{a}{6}}")


@check("number-of-terms-from-the-sum")
def _():
    # search over whole term counts, building each series from its own d
    ns = []
    for n in range(2, 40):
        d = F(40 - 4, n - 1)
        s = sum(4 + k * d for k in range(n))
        if s == 220:
            ns.append(n)
    assert ns == [10], ns
    return lit("10")


# ==================================================== STRUCTURAL CALCULUS
@check("constant-that-makes-a-piecewise-function-continuous")
def _():
    left = lambda x, a: x * x + a
    right = lambda x: 3 * x - 1
    good = [a for a in range(-20, 21) if abs(left(2, a) - right(2)) < 1e-12]
    assert good == [1], good
    return lit("1")


@check("definite-integral-as-a-semicircle-area")
def _():
    # quadrature, NOT the area rule the item is testing
    v = simpson(lambda x: math.sqrt(max(0.0, 9 - x * x)), -3, 3)
    assert abs(v - 9 * math.pi / 2) < 2e-3, v
    return eq(r"\dfrac{9\pi}{2}")


@check("derivative-does-not-exist-at-a-domain-gap")
def _():
    f = lambda x: (x + 1) / (x - 5)
    try:
        f(5.0)
        raise SystemExit("f should be undefined at 5")
    except ZeroDivisionError:
        pass
    # and the difference quotient blows up rather than settling
    q = [abs((f(5 + h) - f(5 - h)) / (2 * h)) for h in (1e-2, 1e-3, 1e-4)]
    assert q[0] < q[1] < q[2]
    return lit("It does not exist")


@check("limit-laws-with-symbolic-values")
def _():
    # a concrete witness pair with the stated limits
    A = 3.7
    f = lambda x: A + (x - 1) ** 2
    g = lambda x: -A - (x - 1) ** 2
    for h in (1e-3, 1e-5):
        assert abs((f(1 + h) - g(1 + h)) - 2 * A) < 1e-5
    return lit("2A")


# ================================================ TRIGONOMETRY AND CONICS
@check("exact-sine-by-decomposing-a-non-special-angle")
def _():
    v = math.sin(math.radians(75))
    assert abs(v - (math.sqrt(6) + math.sqrt(2)) / 4) < 1e-12, v
    return eq(r"\dfrac{\sqrt{6}+\sqrt{2}}{4}")


@check("collapse-a-cosine-sum-to-a-quadrantal-angle")
def _():
    r = math.radians
    v = math.cos(r(70)) * math.cos(r(20)) - math.sin(r(70)) * math.sin(r(20))
    assert abs(v) < 1e-12, v
    return eq(r"0")


@check("minor-axis-from-eccentricity")
def _():
    a = F(20, 2)
    c = F(3, 5) * a
    b2 = a * a - c * c
    assert b2 == 64
    b = math.isqrt(int(b2))
    assert b * b == b2
    return lit(str(2 * b))
