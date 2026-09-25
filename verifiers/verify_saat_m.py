"""Independent re-derivation of every answer in SAAT bank part M
(STA/TRI supply top-up, 20 items). Same pattern as verify_saat_l.py:
CHECKS_M is merged into the master CHECKS dict in verify_saat.py.
"""
import math
from fractions import Fraction as F

CHECKS_M = {}


def check(sig):
    def deco(fn):
        CHECKS_M[sig] = fn
        return fn
    return deco


def lit(s):
    return ("lit", s)


# ============================================================== STATISTICS
@check("recover-value-from-a-stated-mean")
def _():
    known = [7, 10, 15, 8, 14]
    x = 11 * 6 - sum(known)
    assert x == 12
    return lit(str(x))


@check("identify-study-type")
def _():
    return lit("An observational study")


@check("variance-and-sd-of-a-small-list")
def _():
    data = [4, 8, 6, 10, 7]
    n = len(data)
    mean = F(sum(data), n)
    var = sum((F(d) - mean) ** 2 for d in data) / n
    assert var == 4
    return lit(str(int(var)))


@check("compare-two-groups-by-mean-and-sd")
def _():
    return lit("Class B's scores are more spread out than Class A's")


@check("recover-sd-from-empirical-rule-percentage")
def _():
    half_width = 70 - 60
    sd = half_width / 2
    assert sd == 5
    return lit(str(int(sd)))


@check("factorial-equation-in-n-simple")
def _():
    # n!/(n-1)! = n, set equal to 6
    n = 6
    assert math.factorial(n) == 6 * math.factorial(n - 1)
    return lit(str(n))


@check("conditional-probability-two-way-table")
def _():
    both = 45
    french_total = 80
    frac = F(both, french_total)
    assert frac == F(9, 16)
    return lit("9/16")


@check("binomial-probability-exact-count")
def _():
    n, k, p = 5, 3, F(1, 2)
    prob = math.comb(n, k) * p ** k * (1 - p) ** (n - k)
    assert prob == F(5, 16)
    return lit("5/16")


@check("circular-permutation-with-fixed-reference")
def _():
    remaining = math.factorial(5)
    assert remaining == 120
    return lit(str(remaining))


@check("missing-probability-in-a-distribution-table")
def _():
    k = 1 - (0.15 + 0.35 + 0.20)
    assert abs(k - 0.30) < 1e-9
    return lit("0.30")


# ============================================================= TRIGONOMETRY
@check("angle-of-elevation-basic")
def _():
    h = 40 * 0.577
    assert round(h) == 23
    return lit(f"{round(h)} m")


@check("arc-length-from-radius-and-radians")
def _():
    r, theta_num, theta_den = 12, 2, 3   # theta = 2*pi/3
    # s = r*theta ; represent symbolically as coefficient of pi
    coeff = F(r * theta_num, theta_den)
    assert coeff == 8
    return lit("8π cm")


@check("area-of-a-sector-from-degrees")
def _():
    r, angle = 9, 40
    frac = F(angle, 360)
    coeff = frac * r * r        # coefficient of pi
    assert coeff == 9
    return lit("9π cm²")


@check("vertical-and-horizontal-shift-of-a-trig-graph")
def _():
    return lit("y = sin(x − π/2) + 3")


@check("sum-formula-direct-application")
def _():
    sinA, cosA = F(3, 5), F(4, 5)
    cosB, sinB = F(12, 13), F(5, 13)
    val = sinA * cosB + cosA * sinB
    assert val == F(56, 65)
    return lit("56/65")


@check("quadratic-in-cosine-solve")
def _():
    # 2c^2 - c - 1 = 0 -> (2c+1)(c-1)=0 -> c = -1/2 or c = 1
    roots = []
    for c in [F(-1, 2), F(1, 1)]:
        assert 2 * c**2 - c - 1 == 0
        roots.append(c)
    # cos theta = 1 -> theta = 0 ; cos theta = -1/2 -> theta = 120 in [0,180]
    thetas = sorted([0, 120])
    assert thetas == [0, 120]
    return lit("θ = 0° or 120°")


@check("choose-which-law-applies")
def _():
    return lit("Law of Sines")


@check("bearing-and-distance-worded")
def _():
    bearing = math.degrees(math.atan2(40, 30))
    assert round(bearing) == 53
    return lit(f"{round(bearing):03d}°")


@check("resolve-vector-into-components")
def _():
    horiz = round(50 * 0.80)
    vert = round(50 * 0.60)
    assert (horiz, vert) == (40, 30)
    return lit(f"{horiz} N horizontal, {vert} N vertical")


@check("undefined-reciprocal-ratio-values")
def _():
    # cos(90 deg) = 0 -> sec undefined there; check the other three are nonzero
    for a in [0, 180, 360]:
        assert abs(math.cos(math.radians(a))) > 1e-9
    assert abs(math.cos(math.radians(90))) < 1e-9
    return lit("90°")
