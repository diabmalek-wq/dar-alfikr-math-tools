"""Independent re-derivation of every part-L answer.

Nothing here restates the item's own reasoning. The logarithm is found by
SEARCHING for the exponent that reproduces the number, the complex quotient is
confirmed by multiplying the answer back by the divisor, and the binomial
parameters are recovered by simulating the distribution's exact pmf rather than
by quoting np and npq.
"""
import math
from fractions import Fraction as F

lit = lambda s: ("lit", s)
eq = lambda latex: ("eq", latex)

CHECKS_L = {}


def check(sig):
    def deco(fn):
        CHECKS_L[sig] = fn
        return fn
    return deco


@check("log-with-a-radical-base")
def _():
    base = math.sqrt(3)
    # find the exponent by search, not by the log laws the item is testing
    hits = [F(n, 4) for n in range(1, 41) if abs(base ** float(F(n, 4)) - 9) < 1e-9]
    assert hits == [F(4)], hits
    assert abs(base ** 2 - 3) < 1e-12          # and 2 is the base-3 answer, the trap
    return eq(r"4")


@check("quotient-by-a-pure-imaginary")
def _():
    z = complex(5, 2) / complex(0, 3)
    assert abs(z - complex(2 / 3, -5 / 3)) < 1e-12, z
    # multiply back: the only test that matters
    assert abs(z * complex(0, 3) - complex(5, 2)) < 1e-12
    # and the sign-flipped option does NOT reproduce it
    assert abs(complex(-2 / 3, 5 / 3) * complex(0, 3) - complex(5, 2)) > 1e-6
    return eq(r"\dfrac{2}{3}-\dfrac{5}{3}i")


@check("binomial-mean-and-standard-deviation")
def _():
    n, p = 100, F(1, 5)
    q = 1 - p
    # exact pmf, then mean and variance from their definitions
    pmf = [math.comb(n, k) * float(p) ** k * float(q) ** (n - k) for k in range(n + 1)]
    assert abs(sum(pmf) - 1) < 1e-12
    mean = sum(k * pmf[k] for k in range(n + 1))
    var = sum((k - mean) ** 2 * pmf[k] for k in range(n + 1))
    assert abs(mean - 20) < 1e-9, mean
    assert abs(math.sqrt(var) - 4) < 1e-9, math.sqrt(var)
    assert abs(var - 16) < 1e-9                # 16 is the variance, the trap
    return eq(r"\mu=20,\ \ \sigma=4")
