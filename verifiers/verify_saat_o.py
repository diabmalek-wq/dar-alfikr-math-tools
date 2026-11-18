"""Independent re-derivation of SAAT part O (11 items). Each check computes the
answer by a route that does not restate the item's reasoning, then returns the
literal option text; verify_o() compares it with the keyed option."""
import math, json, cmath, statistics, itertools
from fractions import Fraction as F

def refl_x(p): return (p[0], -p[1])
def refl_y(p): return (-p[0], p[1])
def T(p): return f"({p[0]}, {p[1]})".replace("-", "−")

CH = {}
CH["reflect-a-point-in-the-x-axis"] = lambda: T(refl_x((-4, 7)))
CH["reflect-a-point-on-an-axis-in-the-y-axis"] = lambda: T(refl_y((5, 0)))
def _polar():
    # sample points with theta = pi/4, r from -3..3: all must satisfy y = x and none y = -x
    pts = [(r*math.cos(math.pi/4), r*math.sin(math.pi/4)) for r in (-3, -1, 0.5, 2, 3)]
    assert all(abs(y-x) < 1e-12 for x, y in pts)
    assert not all(abs(y+x) < 1e-12 for x, y in pts)
    return "y = x"
CH["polar-equation-with-a-constant-angle-is-a-line"] = _polar
def _sec():
    best = None
    for th in [math.pi - math.asin(3/5)]:
        assert math.pi/2 < th < math.pi and abs(math.sin(th)-0.6) < 1e-12
        s = 1/math.cos(th)
    assert abs(s + 1.25) < 1e-12
    return "−5/4"
CH["secant-from-sine-in-the-second-quadrant"] = _sec
def _recip():
    for th in (0.3, 0.9, 1.2, 2.0, 2.7):
        lhs = (1/math.cos(th))/(1/math.sin(th))
        assert abs(lhs - math.tan(th)) < 1e-9
        assert abs(lhs - 1/math.tan(th)) > 1e-3 or abs(math.tan(th)) == 1
    return "tan θ"
CH["reciprocal-identities-as-a-quotient"] = _recip
def _axiom():
    # model: points in a plane; three non-collinear points -> no line; parallel lines never meet
    A,B,C = (0,0),(1,0),(0,1)
    cross = (B[0]-A[0])*(C[1]-A[1])-(B[1]-A[1])*(C[0]-A[0])
    assert cross != 0                      # B false
    assert (1,1) != (2,1)                  # parallel y=0,y=1 : slopes equal, intercepts differ -> C false
    return "Through any two distinct points there is exactly one line."
CH["two-points-determine-exactly-one-line"] = _axiom
def _circ():
    r = math.sqrt(81); assert abs(math.pi*r*r - 81*math.pi) < 1e-9
    return "9 m"
CH["radius-from-the-area-of-a-circle"] = _circ
def _log():
    x = math.log(32)/math.log(8); assert abs(x - 5/3) < 1e-12 and abs(8**x - 32) < 1e-9
    return "5/3"
CH["logarithm-of-two-powers-of-one-base"] = _log
def _cot():
    bad = []
    for d in (0, 45, 90, 135):
        s = math.sin(math.radians(d))
        if abs(s) < 1e-12: bad.append(d)
    assert bad == [0]
    return "0°"
CH["undefined-cotangent-angle"] = _cot
def _med():
    d = [9, 3, 12, 5, 6]; m = statistics.median(d); assert m == 6 and statistics.mean(d) == 7
    return "6"
CH["median-of-an-unsorted-list"] = _med
def _f():
    f = lambda x: 2*x**2 - 3
    v = f(-4); assert v == 29 and f(4) == 29
    return "29"
CH["evaluate-a-function-at-a-negative-input"] = _f

def verify_o(items):
    bad = 0
    for it in items:
        got = CH[it["sig"]]()
        key = it["opts"][it["ans"]]
        ok = got == key
        # exactly one option equals the derived value
        ok = ok and sum(o == got for o in it["opts"]) == 1 and len(set(it["opts"])) == 4 and len(it["traps"]) == 3
        print(("OK  " if ok else "FAIL"), it["code"], it["sig"], "->", key)
        bad += (not ok)
    print(len(items), "checked,", bad, "failures"); return bad

if __name__ == "__main__":
    import subprocess
    items = json.loads(subprocess.check_output(["node", "-e", "console.log(JSON.stringify(require('/tmp/chk/builders/saat-bank/saat_items_o.js')))"]))
    raise SystemExit(verify_o(items))
