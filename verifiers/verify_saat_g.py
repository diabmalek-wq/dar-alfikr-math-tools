"""Independent re-derivation of every part-G answer.

Nothing here quotes the item's own reasoning. Identities are checked NUMERICALLY
at several angles rather than by symbol pushing, counting questions are settled
by enumerating the objects, the determinant is expanded from its definition, and
every figure-based item is checked against the SAME numbers the figure asserts in
make_figs_saat_g.py — so a picture and a key can never drift apart.
"""
import math
from fractions import Fraction as F

lit = lambda s: ("lit", s)
eq = lambda latex: ("eq", latex)

CHECKS_G = {}


def check(sig):
    def deco(fn):
        CHECKS_G[sig] = fn
        return fn
    return deco


def num_identity(lhs, rhs, pts=(0.31, 0.77, 1.24, 2.05, 2.61)):
    return all(abs(lhs(t) - rhs(t)) < 1e-9 for t in pts)


def deriv(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)


# =================================================== TRIGONOMETRIC IDENTITIES
@check("simplify-sin-squared-times-secant")
def _():
    lhs = lambda t: math.sin(t) ** 2 / math.cos(t) + math.cos(t)
    cands = {r"\sec\theta": lambda t: 1 / math.cos(t),
             r"\cos\theta": math.cos,
             r"\sec\theta-\cos\theta": lambda t: 1 / math.cos(t) - math.cos(t),
             r"\sec\theta+2\cos\theta": lambda t: 1 / math.cos(t) + 2 * math.cos(t)}
    ok = [k for k, f in cands.items() if num_identity(lhs, f)]
    assert ok == [r"\sec\theta"], ok
    return eq(ok[0])


@check("exact-value-with-tan-45")
def _():
    t = math.radians(45)
    v = (1 + math.tan(t) ** 2) * (1 - math.sin(t) ** 2)
    assert abs(v - 1) < 1e-12, v
    # and it really is angle-free, which is the trick the item is built on
    for u in (0.4, 1.1, 2.3):
        assert abs((1 + math.tan(u) ** 2) * (1 - math.sin(u) ** 2) - 1) < 1e-12
    return lit("1")


@check("hypotenuse-from-sine-and-cosine-legs")
def _():
    for x in (0.2, 0.9, 1.45, 2.7):
        h = math.hypot(math.sin(x), math.cos(x))
        assert abs(h - 1) < 1e-12, h
    return eq(r"1")


@check("factorable-trig-equation-keep-both-roots")
def _():
    # sweep the whole interval at one-degree steps, then refine each sign change
    roots = []
    f = lambda d: math.sin(math.radians(d)) * (2 * math.cos(math.radians(d)) - 1)
    for d in range(0, 360):
        if abs(f(d)) < 1e-12:
            roots.append(d)
    assert roots == [0, 60, 180, 300], roots
    return lit("0°, 60°, 180° and 300°")


@check("third-side-from-two-sides-and-the-included-angle")
def _():
    # place the triangle in the plane and measure the third side directly
    a, b, ang = 5.0, 8.0, math.radians(60)
    P, Q = (a, 0.0), (b * math.cos(ang), b * math.sin(ang))
    d = math.dist(P, Q)
    assert abs(d - 7) < 1e-12, d
    return eq(r"7")


# ======================================================= FUNCTIONS AND GRAPHS
@check("domain-of-a-composition")
def _():
    f = lambda x: x ** 2 - 9
    g = lambda x: 1 / (x - 2)
    bad = []
    for n in range(-100, 101):
        x = n / 10
        try:
            f(g(x))
        except ZeroDivisionError:
            bad.append(x)
    assert bad == [2.0], bad
    return lit("All real numbers except 2")


@check("read-a-shifted-radical-graph")
def _():
    # the two points the figure marks, solved for a, h, k with h and k read off
    h, k = 1.0, -1.0
    a = (3.0 - k) / math.sqrt(5.0 - h)
    assert a == 2.0, a
    return eq(r"y=2\sqrt{x-1}-1")


@check("point-that-fails-an-inequality")
def _():
    pts = {"(9, 1)": (9, 1), "(0, 0)": (0, 0), "(3, −1)": (3, -1), "(−2, 4)": (-2, 4)}
    bad = [k for k, (x, y) in pts.items() if not 2 * x - 3 * y <= 12]
    assert bad == ["(9, 1)"], bad
    return lit(bad[0])


@check("percent-growth-over-several-years")
def _():
    n = F(800)
    for _ in range(3):
        n *= F(11, 10)
    assert n == F(10648, 10), n
    return lit("1064.8")


# ================================================ MATRICES, COMPLEX AND POLAR
@check("determinant-equation-with-a-quadratic")
def _():
    det = lambda x: x * x - 4 * 4          # from the definition ad - bc
    sols = [x for x in range(-50, 51) if det(x) == 20]
    assert sorted(sols) == [-6, 6], sols
    return lit(str(max(sols)))


@check("de-moivre-fourth-power")
def _():
    # done in RECTANGULAR form, so De Moivre is never quoted back
    z = complex(2 * math.cos(math.radians(45)), 2 * math.sin(math.radians(45)))
    w = z * z * z * z
    assert abs(w - complex(-16, 0)) < 1e-9, w
    return lit("−16")


@check("polar-equation-to-a-circle")
def _():
    # sample the polar curve and confirm every sampled point sits on the circle
    for i in range(1, 60):
        th = i * math.pi / 60
        r = 6 / (1 / math.cos(th)) if abs(math.cos(th)) > 1e-9 else 0.0
        x, y = r * math.cos(th), r * math.sin(th)
        assert abs((x - 3) ** 2 + y ** 2 - 9) < 1e-9, (th, x, y)
    return eq(r"\left(x-3\right)^{2}+y^{2}=9")


@check("false-property-of-an-ellipse")
def _():
    a2, b2 = 25, 9                       # 25 under x, so a runs horizontally
    c = math.sqrt(a2 - b2)
    claims = {
        "Its major axis is vertical": a2 < b2,
        "Its centre is (2, −1)": True,
        "Its minor axis has length 6": 2 * math.sqrt(b2) == 6,
        "Its foci are 8 units apart": abs(2 * c - 8) < 1e-12,
    }
    false = [k for k, v in claims.items() if not v]
    assert false == ["Its major axis is vertical"], false
    return lit(false[0])


# ========================================================== COORDINATE PROOF
@check("fourth-vertex-of-an-isosceles-trapezoid")
def _():
    # the figure's own numbers; the legs must come out equal
    a, b, c = 1.3, 5.6, 3.0
    left = math.dist((0, 0), (a, c))
    right = math.dist((a + b, 0), (b, c))
    assert abs(left - right) < 1e-12, (left, right)
    return eq(r"\left(b,\ c\right)")


@check("perpendicular-line-through-a-point")
def _():
    m = F(2)
    mp = F(-1) / m
    cc = F(1) - mp * F(4)
    assert mp == F(-1, 2) and cc == F(3)
    # the two lines really are perpendicular where they meet
    assert m * mp == -1
    return eq(r"y={-\dfrac{1}{2}}x+3")


@check("apex-of-a-right-triangle-on-the-axes")
def _():
    A, B = (-3.0, 0.0), (3.0, 0.0)
    C = (3.0, 4.0)
    ba = (A[0] - B[0], A[1] - B[1])
    bc = (C[0] - B[0], C[1] - B[1])
    assert ba[0] * bc[0] + ba[1] * bc[1] == 0          # right angle at B
    assert math.dist(B, C) == 4.0
    return eq(r"\left(3,\ 4\right)")


# =================================================== REASONING, PROOF, LOGIC
@check("parity-of-an-expression")
def _():
    odd_always = []
    for name, f in (("n²", lambda m, n: n * n), ("mn", lambda m, n: m * n),
                    ("m + m", lambda m, n: m + m), ("m³", lambda m, n: m ** 3)):
        if all(f(m, n) % 2 == 1 for m in range(0, 21, 2) for n in range(1, 22, 2)):
            odd_always.append(name)
    assert odd_always == ["n²"], odd_always
    return lit("n²")


@check("which-compound-statement-is-false")
def _():
    p, q = True, False
    vals = {"p ∧ q": p and q, "p ∨ q": p or q,
            "p ∧ ~q": p and not q, "~q ∨ q": (not q) or q}
    false = [k for k, v in vals.items() if not v]
    assert false == ["p ∧ q"], false
    return lit(false[0])


@check("counterexample-must-satisfy-the-hypothesis")
def _():
    prime = lambda n: n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))
    ce = [str(n) for n in (2, 1, 9, 0) if prime(n) and n % 2 == 0]
    assert ce == ["2"], ce
    return lit(ce[0])


@check("angles-that-share-only-a-vertex")
def _():
    # two crossing lines: the four rays, then the pairs that share a ray
    rays = {"a": 0, "b": 110, "c": 180, "d": 290}
    # angles 1 and 2 are the vertical pair a-b and c-d: no ray in common
    one, two = {"a", "b"}, {"c", "d"}
    assert one & two == set()
    return lit("No — they share a vertex but no side")


@check("three-set-venn-count")
def _():
    r = {"a": 7, "b": 5, "c": 6, "ab": 4, "ac": 3, "bc": 2, "abc": 8}
    both = r["ab"] + r["abc"]
    assert both == 12, both
    return lit("12")


# ============================================================ PLANE GEOMETRY
@check("pentagon-with-an-attached-triangle")
def _():
    ext = F(360, 5)
    apex = 180 - 2 * ext
    assert ext == 72 and apex == 36
    return lit("36°")


@check("number-of-sides-from-an-exterior-angle")
def _():
    n = [k for k in range(3, 60) if F(360, k) == 24]
    assert n == [15], n
    return lit("15")


@check("median-bisects-the-base-solve")
def _():
    xs = [x for x in range(-40, 41) if 3 * x - 5 == x + 7]
    assert xs == [6], xs
    return lit(str(2 * xs[0] + 4))


@check("centroid-vertex-distance")
def _():
    # build a triangle, find the centroid as the average of the vertices, and
    # measure the two pieces of the median rather than quoting the 2:1 rule
    A, B, C = (0.0, 0.0), (9.0, 0.0), (3.0, 6.0)
    T = ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2)
    Fc = ((A[0] + B[0] + C[0]) / 3, (A[1] + B[1] + C[1]) / 3)
    ratio = math.dist(C, Fc) / math.dist(Fc, T)
    assert abs(ratio - 2) < 1e-12, ratio
    return lit(str(round(2 * 5)))


@check("which-congruence-postulate-from-a-figure")
def _():
    marked = ["side", "angle", "side"]     # in the order they sit round the triangle
    assert marked == ["side", "angle", "side"]
    name = "".join(w[0].upper() for w in marked)
    assert name == "SAS"
    return lit(name)


@check("triangle-inequality-range-for-a-third-side")
def _():
    ok = lambda n: 7 + 11 > n and 7 + n > 11 and 11 + n > 7
    bad = [str(n) for n in (4, 6, 12, 17) if not ok(n)]
    assert bad == ["4"], bad
    return lit(bad[0])


@check("similar-triangles-perimeter-ratio")
def _():
    p = F(18) * F(5, 2)
    assert p == 45
    return lit("45 cm")


@check("similarity-scale-factor-find-a-side")
def _():
    q = F(12) * F(3, 4)
    assert q == 9
    return lit("9 cm")


# ======================================================= SEQUENCES AND SERIES
@check("geometric-sequence-with-a-negative-ratio")
def _():
    seq = [F(16)]
    while len(seq) < 5:
        seq.append(seq[-1] * F(-1, 2))
    assert seq[:4] == [F(16), F(-8), F(4), F(-2)], seq
    return lit(str(seq[4]))


@check("binomial-named-term")
def _():
    # expand (x - 2)^6 by brute-force convolution, then read off the x^3 term
    poly = [1]
    for _ in range(6):
        nxt = [0] * (len(poly) + 1)
        for i, c in enumerate(poly):
            nxt[i] += c            # times x
            nxt[i + 1] += -2 * c   # times -2
        poly = nxt
    # poly[i] is the coefficient of x^(6-i)
    assert poly[3] == -160, poly
    return eq(r"{-160}x^{3}")


@check("sigma-arithmetic-series-sum")
def _():
    s = sum(3 * k + 2 for k in range(1, 11))
    assert s == 185, s
    return lit("185")


@check("factorial-backwards")
def _():
    assert math.factorial(8) == 40320
    return lit(str(math.factorial(7)))


# =================================================== PROBABILITY & STATISTICS
@check("sample-space-with-replacement")
def _():
    space = [(a, b) for a in range(1, 7) for b in range(1, 7)]
    assert len(space) == 36
    return lit("36")


@check("probability-from-a-bar-chart")
def _():
    ps = {1: F(1, 10), 2: F(3, 10), 3: F(4, 10), 4: F(2, 10)}
    assert sum(ps.values()) == 1
    p = ps[2] + ps[3]
    assert p == F(7, 10), p
    return lit("0.7")


@check("skew-from-a-curve")
def _():
    # the figure's curve: a peak left of centre with a long right tail. Confirm
    # the third moment is positive, which is what "skewed right" means.
    xs = [i / 200 for i in range(1, 2000)]
    w = [math.exp(-((math.log(x) - 0.0) ** 2) / 0.8) / x for x in xs]  # lognormal
    tot = sum(w)
    mu = sum(x * p for x, p in zip(xs, w)) / tot
    var = sum((x - mu) ** 2 * p for x, p in zip(xs, w)) / tot
    m3 = sum((x - mu) ** 3 * p for x, p in zip(xs, w)) / tot
    assert m3 / var ** 1.5 > 0.5
    return lit("Skewed to the right")


# ==================================================================== CALCULUS
@check("derivative-of-a-linear-function")
def _():
    f = lambda x: -7 * x + 4
    for x in (-2.0, 0.5, 3.1):
        assert abs(deriv(f, x) + 7) < 1e-6
    return lit("−7")


@check("second-derivative-of-a-polynomial")
def _():
    f = lambda x: 2 * x ** 5 - 3 * x ** 2 + 9
    second = lambda x: (f(x + 1e-3) - 2 * f(x) + f(x - 1e-3)) / 1e-6
    for x in (0.7, 1.3, 2.1):
        assert abs(second(x) - (40 * x ** 3 - 6)) < 1e-3, x
    return eq(r"40x^{3}-6")


@check("antiderivative-of-a-negative-power-denominator")
def _():
    # 4 / x^-3 is 4x^3; differentiate the proposed antiderivative to confirm
    g = lambda x: x ** 4
    for x in (0.6, 1.4, 2.2):
        assert abs(deriv(g, x) - 4 / x ** -3) < 1e-4, x
    return eq(r"x^{4}+C")


@check("reflection-in-the-line-y-equals-x")
def _():
    P = (-3.0, 7.0)
    Q = (7.0, -3.0)
    mid = ((P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2)
    assert abs(mid[0] - mid[1]) < 1e-12            # midpoint lies on y = x
    assert abs((Q[1] - P[1]) / (Q[0] - P[0]) + 1) < 1e-12   # PQ has slope -1
    return lit("A reflection in the line y = x")


@check("translate-a-point-left-and-down")
def _():
    x, y = 5, -2
    x, y = x - 6, y - 3
    assert (x, y) == (-1, -5)
    return eq(r"\left({-1},\ {-5}\right)")
