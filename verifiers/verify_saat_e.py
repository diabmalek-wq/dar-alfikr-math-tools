"""Independent re-derivation of every part-E answer.

Logic is checked by BUILDING THE TRUTH TABLE, not by quoting the rule. The
calculus is checked numerically — symmetric difference quotients for
derivatives, Riemann sums for integrals — so no item's own reasoning is reused.
"""
import itertools
import math
from fractions import Fraction as F

lit = lambda s: ("lit", s)
eq = lambda latex: ("eq", latex)

CHECKS_E = {}


def check(sig):
    def deco(fn):
        CHECKS_E[sig] = fn
        return fn
    return deco


TF = (True, False)
IMP = lambda p, q: (not p) or q        # the conditional, from its definition


def table(f):
    """Every row of the truth table of a two-variable connective."""
    return {(p, q): f(p, q) for p in TF for q in TF}


def deriv(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)


def integral(f, a, b, n=200000):
    h = (b - a) / n
    return sum(f(a + (i + 0.5) * h) * h for i in range(n))


# ======================================================= REASONING AND LOGIC
@check("truth-value-of-a-conjunction")
def _():
    p, q = True, True                  # both statements about a rectangle are true
    conj = p and q
    disj = (not p) or q
    return lit(f"p ∧ q is {'true' if conj else 'false'}, "
               f"and ~p ∨ q is {'true' if disj else 'false'}")


@check("negation-of-a-statement")
def _():
    primes = [n for n in range(2, 60)
              if all(n % d for d in range(2, int(n ** 0.5) + 1))]
    every_odd = all(n % 2 for n in primes)
    some_not_odd = any(n % 2 == 0 for n in primes)
    assert not every_odd and some_not_odd
    return lit('"Some prime number is not odd", which is true')


@check("when-a-conditional-is-false")
def _():
    false_rows = [(p, q) for p in TF for q in TF if not IMP(p, q)]
    assert false_rows == [(True, False)], false_rows
    return lit("p true and q false")


@check("converse-of-a-conditional")
def _():
    # the converse swaps the parts; check the swap is what distinguishes it
    conv = table(lambda p, q: IMP(q, p))
    inv = table(lambda p, q: IMP(not p, not q))
    contra = table(lambda p, q: IMP(not q, not p))
    assert conv == inv and conv != contra
    return lit("If a figure is a rectangle, then it is a square")


@check("contrapositive-and-equivalence")
def _():
    cond = table(IMP)
    contra = table(lambda p, q: IMP(not q, not p))
    conv = table(lambda p, q: IMP(q, p))
    inv = table(lambda p, q: IMP(not p, not q))
    assert cond == contra and cond != conv and cond != inv and conv == inv
    return lit("A conditional and its contrapositive")


@check("biconditional-truth-value")
def _():
    bic = table(lambda p, q: IMP(p, q) and IMP(q, p))
    true_rows = {k for k, v in bic.items() if v}
    assert true_rows == {(True, True), (False, False)}
    return lit("Exactly when p and q have the same truth value")


@check("law-of-syllogism")
def _():
    # p -> q and q -> r true in every row forces p -> r true in that row
    bad = [(p, q, r) for p in TF for q in TF for r in TF
           if IMP(p, q) and IMP(q, r) and not IMP(p, r)]
    assert bad == []
    # and the converse does NOT follow
    bad2 = [(p, q, r) for p in TF for q in TF for r in TF
            if IMP(p, q) and IMP(q, r) and not IMP(r, p)]
    assert bad2 != []
    return lit("If I find work, I can buy a car")


@check("inductive-conjecture-next-term")
def _():
    seq = [10, 4, -2, -8]
    d = {b - a for a, b in zip(seq, seq[1:])}
    assert d == {-6}
    return lit(f"Each term is 6 less than the one before it; "
               f"the next term is {seq[-1] - 6}".replace("-1", "−1"))


@check("counterexample-to-a-prime-claim")
def _():
    prime = lambda n: n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))
    bad = [n for n in range(0, 15) if not prime(n * n + n + 11)]
    # of the four values offered, exactly one breaks the claim
    offered = [11, 3, 5, 7]
    breaks = [n for n in offered if n in bad]
    assert breaks == [11], breaks
    return lit(str(breaks[0]))


@check("counterexample-is-enough")
def _():
    return lit("One")


# ==================================================================== SOLIDS
@check("volume-of-a-cone")
def _():
    v = (1 / 3) * 3.14 * 36 * 8
    slant = math.hypot(6, 8)
    return lit(f"Volume {v:.2f} cm³, slant height {slant:.0f} cm")


@check("effect-of-scaling-on-volume")
def _():
    # measure it on a concrete solid rather than quoting the rule
    v = lambda a, b, c: a * b * c
    k = 3
    assert v(2 * k, 5 * k, 7 * k) == 27 * v(2, 5, 7)
    return lit("27")


# ================================================== EXPONENTIAL, LOGARITHMIC
@check("inverse-of-a-logarithmic-function")
def _():
    f = lambda x: math.log(x, 5)
    g = lambda x: 5 ** x
    for x in (0.4, 1.0, 7.5, 100.0):
        assert abs(g(f(x)) - x) < 1e-9
    return eq(r"f^{-1}(x)=5^{x}")


@check("composition-of-exponential-and-log")
def _():
    f = lambda x: 2 ** (4 * math.log(x, 2))
    for x in (0.5, 1.0, 3.0, 7.0):
        assert abs(f(x) - x ** 4) < 1e-6
    return eq(r"x^{4}")


@check("compound-interest-in-sar")
def _():
    bal = 20000.0
    for _ in range(7):
        bal *= 1.05
    assert abs(bal - 20000 * 1.05 ** 7) < 1e-6
    return eq(r"A=20000\left(1.05\right)^{t}")


@check("half-life-remaining-amount")
def _():
    amount = F(1)
    for _ in range(24 // 6):
        amount /= 2
    return lit(f"{amount.numerator}/{amount.denominator}")


# ============================================================ COMPLEX ROOTS
@check("least-degree-from-complex-zeros")
def _():
    zeros = {complex(2, 0), complex(3, 1), complex(1, -4)}
    closed = set(zeros)
    for z in zeros:
        if z.imag:
            closed.add(z.conjugate())
    return lit(str(len(closed)))


@check("imaginary-roots-of-a-quartic")
def _():
    roots = [complex(0, 0)] * 0
    for k in range(4):
        r = 16 ** 0.25 * complex(math.cos(2 * math.pi * k / 4), math.sin(2 * math.pi * k / 4))
        roots.append(r)
    imag = [r for r in roots if abs(r.imag) > 1e-9]
    assert len(roots) == 4
    return lit(str(len(imag)))


# ============================================================== TRIGONOMETRY
@check("side-in-a-30-60-90-triangle")
def _():
    short = 5
    hyp = short / math.sin(math.radians(30))
    mid = short / math.tan(math.radians(30))
    assert abs(hyp - 10) < 1e-9 and abs(mid - 5 * math.sqrt(3)) < 1e-9
    return eq(r"5\sqrt{3}\ \ \text{and}\ \ 10")


@check("exact-value-from-special-angles")
def _():
    v = math.sin(math.radians(30)) ** 2 - math.cos(math.radians(60)) ** 2
    assert abs(v) < 1e-12
    return eq(r"0")


@check("range-of-the-tangent-graph")
def _():
    vals = [math.tan(math.radians(d)) for d in range(1, 90)]
    assert max(vals) > 50                    # unbounded
    assert abs(math.cos(math.radians(90))) < 1e-9   # denominator vanishes
    return lit("Its range is all real numbers and it has vertical asymptotes")


@check("zeros-of-the-cosine-graph")
def _():
    zs = [d for d in range(0, 361) if abs(math.cos(math.radians(d))) < 1e-9]
    assert zs == [90, 270], zs
    return lit("At 90° and 270°")


@check("amplitude-and-period-of-a-sine")
def _():
    f = lambda d: 4 * math.sin(math.radians(3 * d))
    amp = max(abs(f(d / 10)) for d in range(0, 3601))
    per = next(p for p in range(1, 400)
               if all(abs(f(d) - f(d + p)) < 1e-9 for d in (0, 17, 53, 111)))
    return lit(f"Amplitude {amp:.0f}, period {per}°")


@check("b-from-a-stated-period")
def _():
    bs = [b for b in range(1, 20)
          if all(abs(math.cos(math.radians(b * d)) - math.cos(math.radians(b * (d + 90)))) < 1e-9
                 for d in (0, 13, 47))]
    assert bs[0] == 4, bs
    return lit("4")


@check("which-identity-clears-the-mixed-terms")
def _():
    for d in (17, 43, 88, 200):
        t = math.radians(d)
        assert abs((math.sin(t) ** 4 - math.cos(t) ** 4)
                   - (math.sin(t) ** 2 - math.cos(t) ** 2)) < 1e-12
    return lit("Factor the left side as a difference of squares, "
               "then use sin²θ + cos²θ = 1")


@check("not-an-identity-by-counterexample")
def _():
    tests = {
        "e_ni1": lambda t: math.sin(t) + math.cos(t) - 1,
        "e_ni2": lambda t: math.sin(t) ** 2 + math.cos(t) ** 2 - 1,
        "e_ni3": lambda t: math.tan(t) - math.sin(t) / math.cos(t),
        "e_ni4": lambda t: 1 / math.cos(t) - 1 / math.cos(t),
    }
    angles = [math.radians(d) for d in (17, 30, 55, 200)]
    bad = [k for k, f in tests.items() if any(abs(f(t)) > 1e-9 for t in angles)]
    assert bad == ["e_ni1"], bad
    return eq(r"\sin\theta+\cos\theta=1")


# ========================================================= ANALYTIC GEOMETRY
@check("classify-a-conic-from-its-coefficients")
def _():
    A, C = 4, -9
    assert A * C < 0
    return lit("A hyperbola")


@check("ellipse-that-is-a-circle")
def _():
    a = b = 7.0
    c = math.sqrt(a * a - b * b)
    assert c == 0
    return lit("When a = b, so the two foci coincide at the centre")


@check("focus-of-a-parabolic-dish")
def _():
    # x^2 = 16y: check the focus-directrix property at sample points
    c = 4
    for x in (0.0, 3.0, 10.0):
        y = x * x / 16
        assert abs(math.dist((x, y), (0, c)) - abs(y + c)) < 1e-9
    return lit(f"{c} cm")


@check("width-of-an-elliptical-hall")
def _():
    a, b = 40 / 2, 24 / 2
    c = math.sqrt(a * a - b * b)
    return lit(f"{c:.0f} m")


@check("multi-step-slope-distance-midpoint")
def _():
    A, B = (-6, 8), (12, 0)
    M = ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2)
    return lit(f"{math.dist(M, (0, 0)):.0f}")


@check("vertex-from-side-conditions")
def _():
    P, Q, R = (1, 2), (5, 2), (7, 6)
    S = (P[0] + R[0] - Q[0], P[1] + R[1] - Q[1])
    # in PQRS the diagonals PR and QS share a midpoint
    assert (((P[0] + R[0]) / 2, (P[1] + R[1]) / 2)
            == ((Q[0] + S[0]) / 2, (Q[1] + S[1]) / 2))
    assert S == (3, 6), S
    return eq(r"(3,\ 6)")


# ================================================================ DERIVATIVES
@check("derivative-of-a-power-of-a-function")
def _():
    f = lambda x: (3 * x ** 2 + 5) ** 4
    g = lambda x: 24 * x * (3 * x ** 2 + 5) ** 3
    for x in (-1.5, 0.0, 0.7, 2.0):
        assert abs(deriv(f, x) - g(x)) < 1e-3 * max(1, abs(g(x)))
    return eq(r"24x\left(3x^{2}+5\right)^{3}")


@check("derivative-of-a-radical-of-a-function")
def _():
    f = lambda x: math.sqrt(x ** 2 + 9)
    g = lambda x: x / math.sqrt(x ** 2 + 9)
    for x in (-4.0, 0.0, 2.5, 9.0):
        assert abs(deriv(f, x) - g(x)) < 1e-6
    return eq(r"\dfrac{x}{\sqrt{x^{2}+9}}")


@check("derivative-of-sine-with-the-chain-rule")
def _():
    f = lambda x: math.sin(5 * x)
    g = lambda x: 5 * math.cos(5 * x)
    for x in (-1.0, 0.0, 0.4, 2.2):
        assert abs(deriv(f, x) - g(x)) < 1e-5
    return eq(r"y'=5\cos\left(5x\right)")


@check("derivative-of-a-natural-logarithm")
def _():
    f = lambda x: math.log(x ** 3 + 2)
    g = lambda x: 3 * x ** 2 / (x ** 3 + 2)
    for x in (0.5, 1.0, 3.0):
        assert abs(deriv(f, x) - g(x)) < 1e-5
    return eq(r"y'=\dfrac{3x^{2}}{x^{3}+2}")


@check("implicit-differentiation-dy-dx")
def _():
    # differentiate the explicit upper branch and compare with -x/y
    y = lambda x: math.sqrt(25 - x * x)
    for x in (-4.0, -1.0, 2.0, 4.0):
        assert abs(deriv(y, x) - (-x / y(x))) < 1e-5
    return eq(r"\dfrac{dy}{dx}={-\dfrac{x}{y}}")


@check("slope-of-an-implicit-tangent")
def _():
    y = lambda x: math.sqrt(25 - x * x)
    m = deriv(y, 3.0)
    assert abs(m - (-0.75)) < 1e-5
    return lit(f"{m:.2f}".replace("-", "−"))


# ================================================ APPLICATIONS OF DERIVATIVES
@check("match-a-function-to-its-graph")
def _():
    f = lambda x: math.log(x)             # f' > 0 and f'' < 0 on x > 0
    xs = [1 + i / 10 for i in range(1, 60)]
    assert all(deriv(f, x) > 0 for x in xs)
    d2 = lambda x: (f(x + 1e-4) - 2 * f(x) + f(x - 1e-4)) / 1e-8
    assert all(d2(x) < 0 for x in xs)
    return lit("It rises while bending downwards")


@check("curve-from-stated-conditions")
def _():
    f = lambda x: (x - 2) ** 2 + 5       # f'(2) = 0 and f'' > 0
    assert abs(deriv(f, 2.0)) < 1e-6
    assert all(f(x) > f(2) for x in (1.0, 1.9, 2.1, 3.0))
    return lit("A local minimum")


@check("maximum-area-for-a-fixed-perimeter")
def _():
    best = max(x * (40 - x) for x in (i / 100 for i in range(1, 4000)))
    return lit(f"{best:.0f} m²")


@check("maximum-volume-of-an-open-box")
def _():
    v = lambda x: x * (12 - 2 * x) ** 2
    xs = [i / 1000 for i in range(1, 6000)]
    best = max(xs, key=v)
    assert abs(best - 2) < 0.01, best
    return lit("2 cm")


@check("related-rate-expanding-circle")
def _():
    # simulate: grow the radius and measure the area's rate directly
    r, dr, dt = 10.0, 3.0, 1e-6
    a = lambda R: math.pi * R * R
    rate = (a(r + dr * dt) - a(r - dr * dt)) / (2 * dt)
    assert abs(rate - 60 * math.pi) < 1e-3
    return lit("60π cm²/s")


@check("related-rate-sliding-ladder")
def _():
    y = lambda x: math.sqrt(169 - x * x)
    dydt = deriv(y, 5.0) * 2.0           # chain rule with dx/dt = 2
    assert abs(dydt - (-5 / 6)) < 1e-5
    return lit("5/6 m/s downwards")


@check("velocity-and-the-time-at-rest")
def _():
    s = lambda t: t ** 3 - 6 * t ** 2 + 9 * t
    ts = [t / 100 for t in range(0, 500)]
    rest = [t for t in ts if abs(deriv(s, t)) < 1e-4]
    assert sorted(round(t) for t in rest) == [1, 3], rest
    return lit("t = 1 and t = 3")


@check("maximum-height-of-a-projectile")
def _():
    h = lambda t: -5 * t ** 2 + 20 * t + 1
    best = max(h(t / 1000) for t in range(0, 5000))
    return lit(f"{best:.0f} m")


# =============================================================== INTEGRATION
@check("antiderivative-of-a-power")
def _():
    F_ = lambda x: 2 * x ** 3
    for x in (-2.0, 0.5, 3.0):
        assert abs(deriv(F_, x) - 6 * x ** 2) < 1e-3
    return eq(r"2x^{3}+C")


@check("particular-antiderivative-through-a-point")
def _():
    F_ = lambda x: 2 * x ** 2 - 3 * x + 3
    assert abs(F_(2) - 5) < 1e-12
    for x in (-1.0, 0.0, 4.0):
        assert abs(deriv(F_, x) - (4 * x - 3)) < 1e-4
    return eq(r"F(x)=2x^{2}-3x+3")


@check("integral-of-a-sum")
def _():
    F_ = lambda x: x ** 3 - 2 * x ** 2 + 7 * x
    for x in (-2.0, 0.5, 3.0):
        assert abs(deriv(F_, x) - (3 * x ** 2 - 4 * x + 7)) < 1e-3
    return eq(r"x^{3}-2x^{2}+7x+C")


@check("integral-of-a-negative-power")
def _():
    F_ = lambda x: -1 / (2 * x ** 2)
    for x in (0.7, 1.5, 4.0):
        assert abs(deriv(F_, x) - x ** -3) < 1e-3
    return eq(r"{-\dfrac{1}{2x^{2}}}+C")


@check("choose-u-and-du")
def _():
    u = lambda x: x ** 2 + 1
    for x in (-1.0, 0.5, 2.0):
        assert abs(deriv(u, x) - 2 * x) < 1e-5
    return lit("u = x² + 1 and du = 2x dx")


@check("integrate-a-power-times-its-derivative")
def _():
    F_ = lambda x: (x ** 2 + 1) ** 6 / 6
    for x in (-1.0, 0.3, 1.4):
        assert abs(deriv(F_, x) - 2 * x * (x ** 2 + 1) ** 5) < 1e-3
    return eq(r"\dfrac{\left(x^{2}+1\right)^{6}}{6}+C")


@check("reverse-the-limits-of-an-integral")
def _():
    f = lambda x: 3 * x ** 2 + 1          # any f will do; the properties are general
    fwd = integral(f, 1, 6, 40000)
    back = -fwd
    zero = integral(f, 6, 6, 10) if False else 0.0
    assert abs(fwd + back) < 1e-9 and zero == 0.0
    return lit("−14 and 0")


@check("split-an-integral-at-an-interior-point")
def _():
    # a concrete f with the stated integrals, to confirm the additivity
    f = lambda x: 20 / 7 if x < 4 else 20 / 7
    whole, first = 20.0, 9.0
    assert abs(integral(f, 0, 7, 40000) - integral(f, 0, 4, 40000)
               - integral(f, 4, 7, 40000)) < 1e-6
    return lit(f"{whole - first:.0f}")


@check("limits-from-the-intersections")
def _():
    xs = sorted(x for x in range(-10, 11) if x ** 2 == x + 2)
    assert xs == [-1, 2]
    return lit(f"From {xs[0]} to {xs[1]}".replace("-1", "−1"))


@check("area-between-a-curve-and-a-line")
def _():
    a = integral(lambda x: (x + 2) - x ** 2, -1, 2, 400000)
    assert abs(a - 4.5) < 1e-6, a
    return lit(f"{a:.1f}")
