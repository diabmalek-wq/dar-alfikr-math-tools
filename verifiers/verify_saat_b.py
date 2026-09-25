"""Independent re-derivation of every part-B answer (Unit 1, sessions 1-9).

Imported by verify_saat.py, which merges these checks with its own. Nothing here
reads an item's reasoning: each answer is recomputed from the item's own data by
integer, exact-rational or numerical means, and the result is compared with the
option the key marks correct — by its LaTeX where the option is typeset.
"""
import math
from fractions import Fraction as F

lit = lambda s: ("lit", s)
eq = lambda latex: ("eq", latex)

CHECKS_B = {}


def check(sig):
    def deco(fn):
        CHECKS_B[sig] = fn
        return fn
    return deco


def close(a, b, tol=1e-9):
    return abs(a - b) < tol


# ------------------------------------------------ session 1, real numbers
@check("smallest-number-set")
def _():
    r = math.isqrt(36)
    assert r * r == 36 and r > 0            # a perfect square, so a counting number
    return lit("Natural numbers")


@check("name-the-property-used")
def _():
    for x in (0.4, 2.5, -7.1):
        assert close(3 * (x - F(7, 6)), 3 * x - float(F(7, 2)), 1e-9)
    return lit("Distributive")


@check("multiplicative-inverse")
def _():
    n = F(-3, 5)
    inv = 1 / n
    assert n * inv == 1 and inv == F(-5, 3)
    return eq(r"{-\dfrac{5}{3}}")


@check("closure-under-an-operation")
def _():
    q = F(3, 2)
    assert q.denominator != 1               # a quotient of integers that is not an integer
    return lit("Integers")


# ------------------------------------- session 2, rational and irrational
def perfect_square(n):
    r = math.isqrt(n)
    return r * r == n


@check("identify-the-irrational-number")
def _():
    assert not perfect_square(8) and perfect_square(121)
    return eq(r"\sqrt{8}")


@check("product-of-surds-is-rational")
def _():
    v = math.sqrt(2) * math.sqrt(8)
    assert close(v, 4)
    return lit("It is rational, and equals 4.")


@check("repeating-decimal-is-rational")
def _():
    f = F(45, 99)                            # 0.454545... as a ratio of integers
    assert f == F(5, 11) and 0.4545 < float(f) < 0.4546
    return lit("It is rational, because the repeating block makes it a fraction of two integers.")


@check("integers-either-side-of-a-surd")
def _():
    n = math.isqrt(55)
    assert n == 7 and n * n < 55 < (n + 1) ** 2
    return lit("7 and 8")


# -------------------------------------- session 3, exponents and radicals
@check("simplify-product-of-powers")
def _():
    f = lambda x, y: (2 * x ** -3 * y ** 3) * (7 * x ** 5 * y ** -6)
    g = lambda x, y: 14 * x ** 2 / y ** 3
    for x, y in ((1.7, 2.3), (0.6, 1.1)):
        assert close(f(x, y), g(x, y), 1e-8)
    return eq(r"\dfrac{14x^{2}}{y^{3}}")


@check("radical-to-rational-exponent")
def _():
    for x in (1.4, 2.9, 5.5):
        assert close((x ** 7) ** (1 / 3), x ** (7 / 3), 1e-8)
    return eq(r"x^{\frac{7}{3}}")


@check("even-index-needs-absolute-value")
def _():
    f = lambda a: ((a - 1) ** 24) ** (1 / 8)
    for a in (3.0, -2.0, 0.25):              # includes a < 1, where a - 1 is negative
        assert close(f(a), abs(a - 1) ** 3, 1e-6)
    assert not close(f(-2.0), (-2.0 - 1) ** 3)   # the bars are doing real work
    return eq(r"\lvert a-1\rvert^{3}")


@check("quotient-of-radicals")
def _():
    v = math.sqrt(63) / math.sqrt(28)
    assert close(v, 1.5)
    return eq(r"\dfrac{3}{2}")


@check("rationalise-a-two-term-denominator")
def _():
    v = 2 / (math.sqrt(3) + 1)
    assert close(v, math.sqrt(3) - 1)
    return eq(r"\sqrt{3}-1")


# ----------------------------------------- session 4, scientific notation
@check("compare-in-scientific-notation")
def _():
    vals = {r"9.9\times 10^{-3}": 9.9e-3, r"1.2\times 10^{-2}": 1.2e-2,
            r"8.5\times 10^{-3}": 8.5e-3, r"1.05\times 10^{-2}": 1.05e-2}
    return eq(max(vals, key=vals.get))


# -------------------------------------- session 5, algebraic expressions
@check("leading-coefficient-of-a-polynomial")
def _():
    # coefficients by degree: -x - 3x^2 - 2x^4
    coef = {1: -1, 2: -3, 4: -2}
    top = max(coef)
    assert top == 4
    return lit("−2" if coef[top] == -2 else str(coef[top]))


@check("missing-factor-from-an-area")
def _():
    # (x - 5)(x + k) = x^2 + 3x - 40 forces k = 8; confirm at several x
    k = 8
    for x in (0.0, 2.5, 7.0):
        assert close((x - 5) * (x + k), x ** 2 + 3 * x - 40)
    return eq(r"x+8")


@check("simplify-quotient-with-negative-powers")
def _():
    f = lambda a, b: (2 * a ** 3 * b ** 2) / (6 * b * a ** 5)
    g = lambda a, b: b / (3 * a ** 2)
    for a, b in ((1.3, 2.1), (0.7, 4.0)):
        assert close(f(a, b), g(a, b), 1e-9)
    return eq(r"\dfrac{b}{3a^{2}}")


@check("substitute-a-monomial-into-a-polynomial")
def _():
    f = lambda t: 2 * t ** 2 - 3 * t - 3
    for x in (-2.0, 0.5, 3.0):
        assert close(f(-2 * x), 8 * x ** 2 + 6 * x - 3)
    return eq(r"8x^{2}+6x-3")


# ------------------------------------------------- session 6, factoring
@check("factor-difference-of-squares-in-a-product")
def _():
    f = lambda a, b: (a ** 2 - b ** 2) / (3 * b) * (9 * b ** 2) / (a - b)
    for a, b in ((5.0, 2.0), (1.3, 0.4)):
        assert close(f(a, b), 3 * b * (a + b), 1e-9)
    return eq(r"3b(a+b)")


@check("factor-a-quadratic-trinomial")
def _():
    roots = [r for r in range(-10, 11) if r ** 2 + 4 * r - 5 == 0]
    assert sorted(roots) == [-5, 1]          # so (x + 5) and (x - 1) are the factors
    return eq(r"x+5")


@check("identify-a-prime-polynomial")
def _():
    # 3x - 7 has no integer root and no common factor; the others factor
    assert math.gcd(3, 7) == 1
    assert math.gcd(2, 4) == 2               # 2x + 4
    return eq(r"3x-7")


@check("factor-by-grouping")
def _():
    f = lambda x: x ** 3 + 2 * x ** 2 - 3 * x - 6
    for x in (-3.0, 0.0, 1.5, 4.0):
        assert close(f(x), (x + 2) * (x ** 2 - 3))
    return eq(r"(x+2)\left(x^{2}-3\right)")


# --------------------------------------- session 7, algebraic fractions
@check("simplify-a-rational-expression")
def _():
    f = lambda x: ((x - 2) * (x - 3) ** 2) / ((4 * x - 12) * (x ** 2 + x - 6))
    g = lambda x: (x - 3) / (4 * (x + 3))
    for x in (0.0, 1.5, 5.0, 7.25):
        assert close(f(x), g(x), 1e-9)
    return eq(r"\dfrac{x-3}{4(x+3)}")


@check("subtract-two-rational-expressions")
def _():
    f = lambda a: a / (a - 1) - a / (a + 1)
    for a in (2.0, 3.5, -4.0):
        assert close(f(a), 2 * a / (a ** 2 - 1), 1e-9)
    return eq(r"\dfrac{2a}{a^{2}-1}")


@check("simplify-a-complex-fraction")
def _():
    f = lambda x: (x / 6) / ((x - 3) / 5)
    for x in (1.0, 4.5, 10.0):
        assert close(f(x), 5 * x / (6 * x - 18), 1e-9)
    return eq(r"\dfrac{5x}{6x-18}")


@check("values-that-make-an-expression-undefined")
def _():
    bad = [x for x in range(-20, 21) if x ** 2 + 4 * x - 21 == 0]
    assert sorted(bad) == [-7, 3]
    return eq(r"x=3\ \ \text{and}\ \ x={-7}")


@check("lcm-of-two-monomials")
def _():
    # lcm of the coefficients, highest power of each letter
    c = 20 * 4 // math.gcd(20, 4)
    assert c == 20 and max(3, 2) == 3 and max(5, 6) == 6
    return eq(r"20x^{3}y^{6}")


# ------------------------------ session 8, linear equations and inequalities
@check("solve-a-linear-equation-with-fractions")
def _():
    # 3(3x + 4) = 5(2x - 1) solved over the rationals, then substituted back
    x = F(17, 1)
    assert F(3 * x + 4, 5) == F(2 * x - 1, 3)
    return lit(str(x))


@check("reverse-the-sign-when-dividing-by-a-negative")
def _():
    f = lambda x: -4 * x + 3 > 19
    assert f(-5) and not f(-4) and not f(0)   # true below -4, false at and above it
    return eq(r"x<{-4}")


@check("write-an-inequality-as-an-interval")
def _():
    inside = lambda x: -2 <= x < 5
    assert inside(-2) and not inside(5) and inside(4.999)
    return eq(r"[-2,\ 5)")


@check("point-in-the-solution-region")
def _():
    ok = lambda p: p[1] <= 2 * p[0] - 3 and p[1] >= p[0] + 4
    pts = {r"(0,\ 5)": (0, 5), r"(8,\ 10)": (8, 10),
           r"(5,\ 2)": (5, 2), r"(10,\ 15)": (10, 15)}
    good = [k for k, p in pts.items() if ok(p)]
    assert good == [r"(10,\ 15)"], good
    return eq(good[0])


@check("vertex-of-a-feasible-region")
def _():
    x = F(12 - 9, 3)                          # 9 = -3x + 12
    assert -3 * x + 12 == 9 and x == 1
    return eq(r"(1,\ 9)")


# ----------------------------------------------- session 9, absolute value
@check("absolute-value-equal-to-a-negative")
def _():
    hits = [x for x in range(-200, 201) if abs(2 * (x / 10) - 6) == -4]
    assert hits == []
    return lit("No solution")


@check("absolute-value-inequality-as-a-double-inequality")
def _():
    sol = lambda x: abs(x - 4) < 3
    assert sol(1.001) and sol(6.999) and not sol(1) and not sol(7)
    return eq(r"1<x<7")
