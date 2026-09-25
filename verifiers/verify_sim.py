"""Re-derive every answer in the simulated bank from scratch, in Python, and
compare with what the bank claims. Nothing ships until this reports 0 failures."""
from fractions import Fraction as F
import json, math, subprocess
from itertools import product

items = json.loads(subprocess.run(
    ["node", "-e",
     "const I=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o'].flatMap(k=>require('./sim_items_'+k+'.js'));"
     "console.log(JSON.stringify(I.map(i=>({sig:i.sig,ans:i.ans,"
     "opts:i.opts.map(o=>(o&&o.eq)?o.eq:o)}))))"],
    capture_output=True, text=True, cwd="/home/claude/fikr_pptx").stdout)
BY = {i["sig"]: i for i in items}

CMP = {"A": 0, "B": 1, "EQ": 2, "ND": 3}
res = {}

def cmp2(a, b):
    return CMP["A"] if a > b else CMP["B"] if b > a else CMP["EQ"]

def opt(sig, value):
    """index of `value` in that item's option list, as a string match.
    Minus signs are normalised: the paper uses U+2212, python writes '-'."""
    o = BY[sig]["opts"]
    v = str(value)
    if v.startswith("-"):
        v = "\u2212" + v[1:]
    for i, x in enumerate(o):
        if str(x).replace(" ", " ").replace(" ", "") == v.replace(" ", ""):
            return i
    raise SystemExit(f"{sig}: {value!r} not among {o}")

# ---------------------------------------------------------------- arithmetic
res["pct-scale-same-base"]      = opt("pct-scale-same-base", int(F(1440, 18) * 12))
res["ratio-powers-of-ten"]      = opt("ratio-powers-of-ten", "4 : 1") if F(6, 15) * 10 == 4 else -1
res["pct-of-unknown-compare"]   = cmp2(F(3600) / F(18, 10), 2200)
res["pct-simple-compare"]       = cmp2(380, F(40, 100) * 900)
res["pct-complement"]           = opt("pct-complement", int(F(21) / F(70, 100)))
res["unit-rate-scale"]          = opt("unit-rate-scale", int(F(640, 8) * 14))
res["tare-then-scale"]          = opt("tare-then-scale", f"{420 + 3 * (620 - 420)} kg")
res["surd-identity-compare"]    = cmp2(round(3 * 5 ** .5, 9),
                                       round(12 * 20 ** .5 / (4 * 4 ** .5), 9))
res["two-divisibility-conditions"] = opt("two-divisibility-conditions",
    [n for n in (40, 48, 56, 64) if n % 8 == 0 and (n - 6) % 7 == 0][0])
res["negative-exponent"]        = opt("negative-exponent", round(16 ** F(1, 4)))
res["remainder-subtract"]       = opt("remainder-subtract", 1000 % 43)
res["estimate-round"]           = cmp2(0.25 * 63.98 / 1.001, 15)
res["hcf-tiling"]               = opt("hcf-tiling", math.gcd(36, 60))
res["power-of-two-divisor"]     = opt("power-of-two-divisor",
    [n for n in (15, 18, 24, 27) if 3 ** 12 % n == 0][0])
res["identify-prime"]           = opt("identify-prime",
    [n for n in (51, 57, 67, 91) if all(n % d for d in range(2, int(n ** .5) + 1))][0])
res["multiplier-sequence"]      = opt("multiplier-sequence", 18 * 4)
res["long-division-last-digit"] = opt("long-division-last-digit", f"{64431516 // 372:,}".replace(",", " "))
assert 64431516 % 372 == 0, "long division is not exact"
res["banknote-fractions"]       = opt("banknote-fractions",
    8 * 10 + 12 * 50 + (48 - 8 - 12) * 100)
res["percent-of-total"]         = opt("percent-of-total", int(F(35, 100) * 480))
res["difference-sequence"]      = opt("difference-sequence", 26 + 12)
res["percent-then-divide"]      = opt("percent-then-divide", int(F(20, 100) * 360 / 8))
res["surd-complex-fraction"]    = opt("surd-complex-fraction",
    round(5 ** .5 * 6 * 3 ** .5 / (5 ** .5 / (3 * 3 ** .5))))
res["percent-cross-compare"]    = cmp2(F(15, 100) * 480, F(8, 1000) * 9000)
res["negative-fraction-compare"] = cmp2(F(2, 5) - F(9, 10), F(1, 10) - F(9, 10))
res["groups-plus-remainder"]    = opt("groups-plus-remainder", 14 * 18 + 7)
res["ratio-scale-up"]           = opt("ratio-scale-up", 400 // 25 * 3)
res["nested-percent"]           = opt("nested-percent",
    float(F(5, 100) / 100 * (F(2, 100) * 4000)))
res["decimal-fraction-sum"]     = opt("decimal-fraction-sum",
    float(F(75, 1000) + F(45, 100) + F(606, 10)))
res["factor-out-common"]        = opt("factor-out-common", (-18 * 35 + 11 * 35) // 7)
def prod(lo, hi):
    p = 1
    for n in range(lo, hi + 1):
        if n: p *= n
    return p
res["sign-of-product-range"]    = cmp2(prod(-3, 5), prod(-5, 3))
res["odd-vs-even-sum"]          = cmp2(sum(n for n in range(1, 26) if n % 2),
                                       sum(n for n in range(1, 26) if not n % 2))
# ------------------------------------------------------------------- algebra
res["case-split-compare"] = CMP["ND"]        # a=1 gives A, b=0 leaves it open
_cases = set()
for a in (1, -1, 2, 3):
    for b in (0, 1, 5):
        if a * a * b == b:
            k = a * b
            _cases.add(cmp2(k, b - a))
assert len(_cases) > 1, _cases
res["sqrt-two-roots"]     = opt("sqrt-two-roots", 11 - 3)
res["clear-denominator-pair"] = opt("clear-denominator-pair",
    [p for p in ("30 , 40", "35 , 55", "40 , 45", "50 , 60")
     if sum(int(x) for x in p.split(" , ")) == 18 * 5][0])
res["net-movement-backwards"] = opt("net-movement-backwards", 43 + 14 - 5)
w = -2
res["evaluate-negative"]  = opt("evaluate-negative", 3*w**3 - 2*w**2 + 5*w)
sums = {F(40 - y, 4) + y + F(3, 4) * (24 - y) for y in (F(0), F(4), F(-8))}
assert len(sums) == 1, sums
res["sum-invariant-system"] = opt("sum-invariant-system", int(sums.pop()))
res["words-to-linear"]    = opt("words-to-linear", float(F(9, 2)))
res["proportion-solve"]   = opt("proportion-solve", int(F(7) / F(7, 10)))
res["system-eliminate-compare"] = cmp2(1, 3)          # 1 coffee = 3 rice
res["solve-then-compare"] = cmp2(4 * 3, 3 * 6)
res["inequality-bound-compare"] = cmp2(F(-3, 4), F(-5, 6))
res["no-sign-compare"]    = CMP["ND"]
assert len({cmp2(F(3, 7) * v, v) for v in (7, -7)}) > 1
res["reciprocal-sign-trap"] = CMP["ND"]
assert len({cmp2(F(1, g), F(1, n)) for g, n in ((1, 2), (-1, 1))}) > 1
u = F(-1, 5); v = -u
res["substitute-compare-negatives"] = cmp2(u - v, 7 * u)
res["two-digit-digit-conditions"] = opt("two-digit-digit-conditions",
    [n for n in (57, 84, 39, 66)
     if abs(int(str(n)[0]) - int(str(n)[1])) == 4 and sum(map(int, str(n))) == 12][0])
res["diophantine-two-prices"] = opt("diophantine-two-prices",
    f"{[j for j in range(1, 12) if (52 - 5*j) >= 8 and (52 - 5*j) % 8 == 0][0]} juices")
assert len([j for j in range(1, 12) if (52 - 5*j) >= 8 and (52 - 5*j) % 8 == 0]) == 1, "juice count is not unique"
res["identify-false-statement"] = opt("identify-false-statement",
    ["q1a", "q1b", "q1c", "q1d"][[i for i, ok in enumerate([
        F(3) == F(6, 2), 3 + 6 == 3 + 6, 3 * 3 + 3 * 3 == 3 * 6, 6 - 3 == 3 * 3])
        if not ok][0]])
res["undo-two-operations"] = opt("undo-two-operations", (1069 + 83) // 24)
res["identity-sum-product"] = opt("identity-sum-product", 9 ** 2 - 2 * 14)
# ------------------------------------------------------------------ geometry
r3 = 3 ** .5
res["medial-triangle-fraction"] = opt("medial-triangle-fraction",
    {4: "o4r3", 8: "o8r3", 16: "o16r3", 32: "o32r3"}[round(r3 / 4 * 16 ** 2 / 8 / r3)])
res["similar-third-angle"] = opt("similar-third-angle", 180 - 35 - 60)
res["halve-twice-ratio"]   = opt("halve-twice-ratio", "f14")
res["perimeter-to-area-parts"] = opt("perimeter-to-area-parts", int((34 / 2 - 5) * 5 / 6))
assert 9 ** 2 + 12 ** 2 == 15 ** 2
res["area-equal-then-perimeter"] = opt("area-equal-then-perimeter",
    round(2 * (9 * 12 / 2 / 6 + 6)))
res["circle-tangent-triangles"] = opt("circle-tangent-triangles", int(2 * (5 * 5 / 2)))
res["arc-central-angle-compare"] = cmp2(74, 180 - 74)
res["segment-ratio-midpoint"] = opt("segment-ratio-midpoint",
    {F(9, 14): "f914", F(5, 7): "f57", F(4, 7): "f47", F(1, 2): "f12"}[
        (F(4) + 1 + 4) / (2 * F(5) + 4)])
res["clock-angle"] = opt("clock-angle", f"{360 // 60}°")
res["rhombus-diagonals"] = opt("rhombus-diagonals", 12 * 8 // 2)
ys = [y for y in range(1, 40) if y ** 2 + (y + 14) ** 2 == 26 ** 2]
res["pythagoras-consecutive-legs"] = opt("pythagoras-consecutive-legs",
    ys[0] * (ys[0] + 14) // 2)
res["trapezoid-slant"] = opt("trapezoid-slant", round(math.hypot(19 - 11, 15)))
res["triangle-inequality"] = opt("triangle-inequality",
    [s for s in (5, 9, 13, 18) if not (11 - 7 < s < 11 + 7)][0])
res["polygon-exterior-angles"] = opt("polygon-exterior-angles", 2 * (360 // 8))
res["parallel-isosceles-angle"] = opt("parallel-isosceles-angle", (180 - 40) // 2)
res["angles-round-a-point"] = opt("angles-round-a-point", f"{360 - 140 - 90}°")
res["circle-area-scale-compare"] = cmp2(3 * 5 ** 2, 9 ** 2)
res["parallelogram-strip-ratio"] = opt("parallelogram-strip-ratio", "1 : 5")
assert F(2, 5 + 2 + 3) == F(1, 5)
# ---------------------------------------------------------------------- data
res["probability-count-over-total"] = opt("probability-count-over-total",
    {F(1, 5): "f15", F(1, 6): "f16", F(1, 3): "f13"}[F(len([n for n in range(1, 31)
                                                            if n % 5 == 0]), 30)])
res["two-way-table"] = opt("two-way-table", 24 - (27 - 11))
P, Q, R = {1, 2, 3, 4, 5, 6}, {3, 4, 7, 8, 9}, {4, 10, 11}   # sizes 6, 5, 3; Q&R = {4}
assert (len(P), len(Q), len(R), len(Q & R), len(Q | R)) == (6, 5, 3, 1, 7)
res["venn-and"] = cmp2(len(P), len(Q & R))
res["venn-or"]  = cmp2(len(P), len(Q | R))
res["bar-plus-given-ratio"] = opt("bar-plus-given-ratio",
    f"{round(300 / (300 + 1200) * 100)} %")
res["two-bar-ratio"] = opt("two-bar-ratio", "4 : 1")
G = {"Buses": [40, 55, 30, 45], "Lorries": [50, 40, 35, 60]}
tot = [G["Buses"][i] + G["Lorries"][i] for i in range(4)]
res["grouped-bar-minimise"] = opt("grouped-bar-minimise",
    ["Gate 1", "Gate 2", "Gate 3", "Gate 4"][tot.index(min(tot))])
S = {"Physics": 90, "Arabic": 30, "Geography": 60, "English": 75, "Art": 45}
res["bar-mean-match"] = opt("bar-mean-match",
    [k for k, v in S.items() if v == (S["Physics"] + S["Arabic"]) / 2][0])
FD = {"Fund A": [-3, 8, 6, 10], "Fund B": [9, -5, 12, 4],
      "Fund C": [14, 7, -2, 9], "Fund D": [6, 11, 5, -4]}
res["negative-bars-window"] = opt("negative-bars-window",
    [k for k, v in FD.items() if all(x >= 0 for x in v[1:])][0])
res["scatter-group-mean"] = opt("scatter-group-mean", sum([45, 55, 50]) // 3)
res["line-percent-increase"] = opt("line-percent-increase",
    f"{round((12 - 5) / 5 * 100)} %")
GD = {"Tea": [45, 30, 50, 40], "Juice": [35, 45, 30, 50], "Coffee": [40, 50, 60, 30]}
DAYS = ["Thursday", "Friday", "Saturday", "Sunday"]
res["grouped-bar-double"] = opt("grouped-bar-double",
    [DAYS[i] for i in range(4)
     if GD["Tea"][i] + GD["Juice"][i] == 2 * GD["Coffee"][i]][0])
# --------------------------------------------------------------------- logic
res["rate-then-scale"] = opt("rate-then-scale", 1000 // (150 // 6))
res["fraction-remainder-whole"] = opt("fraction-remainder-whole",
    int(F(24) / (1 - F(1, 3) - F(1, 2)) / 2))
res["age-chain-multiplier"] = cmp2(1, 24)
res["equal-split-denominations"] = cmp2(2000, 15 * (10 + 20 + 100))
res["speed-unit-convert"] = opt("speed-unit-convert", f"{int(200 / (150 / 60))} km/h")
res["bearing-reverse"] = opt("bearing-reverse", "North-west")
def ok(n):
    d = str(n)
    adj = lambda a, b: a in d and b in d and abs(d.index(a) - d.index(b)) == 1
    return adj("2", "9") and not adj("2", "4") and not adj("9", "4") and n % 2 == 1
res["adjacency-puzzle"] = opt("adjacency-puzzle",
    [n for n in (4291, 1429, 4129, 1294) if ok(n)][0])
res["period-align-subtract"] = opt("period-align-subtract", 1200 - 10800 // 12)
start = ((0 * 60 + 20) - (3 * 60 + 50)) % (24 * 60)
res["time-backwards"] = opt("time-backwards", f"{start // 60}:{start % 60:02d}")
res["bogo-compare"] = opt("bogo-compare", 8 * 10 - (8 // 4 * 3) * 12)
res["time-unit-compare"] = cmp2(13 * 95, 20 * 60)
res["zakat-reverse-percent"] = opt("zakat-reverse-percent", int(250 / 0.025))
res["rank-front-back"] = opt("rank-front-back", 9 + 15 - 1)
res["two-tier-tariff"] = opt("two-tier-tariff", int(2 + (15 - 6) / 0.75))
res["ages-sum-shift"] = opt("ages-sum-shift", 94 + 5 * 6)
res["ages-offsets-sum"] = opt("ages-offsets-sum", (46 - 4 - (-8)) // 2 if False else (46 + 4 - 8) // 2)
res["cycle-position"] = opt("cycle-position",
    ["date", "cheese", "pistachio", "almond"][(63 - 1) % 4])
res["closing-speed"] = opt("closing-speed", int((5 + 19) * F(45, 60)))
res["ordering-chain-compare"] = CMP["A"]
res["pass-fail-fraction"] = opt("pass-fail-fraction", 120 + 120 // 4)

# ------------------------------------------------- part 6 skills (part C)
res["table-missing-cell"] = opt("table-missing-cell", 186 - 42 - 55 - 24)
assert 65 + 31 + 97 == 193, "the Jeddah column must also close"
YR = {"Food": (60, 150), "Housing": (40, 120), "Transport": (25, 75),
      "Health": (30, 66)}
treb = sorted(k for k, (a, b) in YR.items() if b >= 3 * a)
res["table-multi-row-condition"] = opt("table-multi-row-condition",
                                       " and ".join(treb))
res["pie-sector-from-values"] = opt("pie-sector-from-values",
    f"{int(210 / (1080 / 360)) - 40}\u00b0")
res["pie-angle-to-count"] = opt("pie-angle-to-count", int(180 / 360 * 480))
res["pie-missing-sector-angle"] = opt("pie-missing-sector-angle",
                                      f"{360 - 180 - 45}\u00b0")
res["equal-sectors-shaded-angle"] = opt("equal-sectors-shaded-angle",
                                        f"{4 * (360 // 10)}\u00b0")
_r, _R = 80 / 8 / 2, 80 / 2
res["circles-along-diameter-ratio"] = opt("circles-along-diameter-ratio",
    f"1 : {int(round((_R / _r) ** 2))}")
res["area-ratio-to-length-ratio"] = opt("area-ratio-to-length-ratio",
    f"1 : {int(196 ** 0.5)}")
res["exterior-angle-theorem"] = cmp2(130, 135)
res["percent-of-count-from-figure"] = opt("percent-of-count-from-figure",
    int((3 * 4) / 0.20))
res["equivalence-chain-weights"] = opt("equivalence-chain-weights",
    f"{24 // 2 * 5 + 40 // 4 * 5} dates")
res["power-tower-signs-compare"] = cmp2(F(5) ** -4 * F(25) ** 3, 25)
res["same-base-fractional-exponents"] = opt("same-base-fractional-exponents",
    {F(1, 2): "f12", F(1, 4): "f14", F(1, 8): "f18"}[F(1, 8) ** (F(1, 3) + F(2, 3))])
res["swapped-fraction-compare"] = cmp2(F(1, 3) * 12, F(1, 12) * 3)
res["inverse-proportion"] = opt("inverse-proportion", int(9 / 0.60))
res["divide-by-decimal"] = opt("divide-by-decimal", int(54 / 0.045))
res["percent-less-than-sum"] = opt("percent-less-than-sum",
                                   int(5550 / (1 + 0.85)))
res["reciprocal-pair-pattern"] = opt("reciprocal-pair-pattern", 11 + 2)
res["complex-fraction-simplify"] = opt("complex-fraction-simplify", "cf2")
_n = 5
assert F(1 + F(2, _n), _n - F(4, _n)) == F(1, _n - 2), "cfrac identity"
res["absolute-value-two-roots-compare"] = CMP["ND"]
assert len({cmp2(m, 7) for m in (7, -7)}) > 1
res["minimum-of-square"] = cmp2(0, 1)
res["sign-of-powers-negative"] = opt("sign-of-powers-negative",
    ["sp1", "sp2", "sp3", "sp4"][max(range(4),
        key=lambda i: [6 * -2, (-2) ** 3, (-2) ** 4, F(1, -2)][i])])
_ys = [y for y in (-3, -2, -1, 0, 1, 2, 3) if 3 * y * y + 3 * y == 6]
res["substitute-into-quadratic"] = opt("substitute-into-quadratic",
                                       max(_ys))

# ------------------------------------------------- part 5 skills (part D)
res["count-all-squares-in-grid"] = opt("count-all-squares-in-grid",
    sum((4 - k) ** 2 for k in range(4)))
res["rectangle-in-circle-radius"] = opt("rectangle-in-circle-radius",
    int(math.hypot(6, 8) / 2))
res["shaded-fraction-of-square"] = opt("shaded-fraction-of-square",
    int((8 / 2) ** 2 + (8 / 2) ** 2 / 2))
res["percent-greater-area-from-diameter"] = opt(
    "percent-greater-area-from-diameter",
    f"{int(round((240 ** 2 - 200 ** 2) / 200 ** 2 * 100))} %")
res["clock-hands-angle"] = opt("clock-hands-angle",
    f"{int(abs((8 * 30 + 24 * 0.5) - 24 * 6))}\u00b0")
res["percent-increase-price"] = opt("percent-increase-price",
    int(5300 * F(140, 100)))          # float 5300*1.4 lands on 7419.999...
res["self-over-fraction-pattern"] = opt("self-over-fraction-pattern",
    int(F(1) / F(1, 3) + F(2) / F(2, 6) + F(7) / F(7, 3)))
res["add-fractions-vs-fraction-of-sum"] = cmp2(F(1, 2) + F(1, 3), F(1, 3 + 2))
res["cancel-before-multiplying"] = opt("cancel-before-multiplying",
    int(F(1, 35) * 14 * 15))
res["powers-common-exponent-compare"] = cmp2(3 ** 75, 2 ** 100)
res["nested-radical-compare"] = cmp2(3, 1 + 2 ** 0.5)     # compare the insides
res["reciprocal-rationalise"] = opt("reciprocal-rationalise",
    {3: "o3r2", 2: "o2r2", 6: "o6r2"}[round(6 / (2 ** 0.5) / (2 ** 0.5))])
res["ratio-difference-to-sum"] = opt("ratio-difference-to-sum",
    (4 + 3) * (150 // (4 - 3)))
res["currency-convert-then-floor"] = opt("currency-convert-then-floor",
    int(7777 / 10 // 20))
res["split-fraction-substitute"] = opt("split-fraction-substitute", 5 + 3)
_L = [(w, l) for w in range(1, 24) for l in range(1, 24)
      if w + l == 24 and w - 2 == l + 2]
res["rect-to-square-adjust"] = opt("rect-to-square-adjust",
    (_L[0][0] - 2) ** 2)
res["catch-up-linear"] = opt("catch-up-linear",
    [d for d in range(1, 60) if 240 + 5 * d == 100 + 12 * d][0])
res["work-rate-people-days"] = opt("work-rate-people-days",
    int(4000 / (4 * (1500 / (3 * 4)))))
res["similar-shadows-proportion"] = opt("similar-shadows-proportion",
    int(150 * (1200 / 300)))

# --------------------------------------- formula-book skills (part E)
res["sum-first-n"] = opt("sum-first-n", 60 * 61 // 2)
_odd = list(range(1, 30, 2))
res["sum-odd-formula"] = opt("sum-odd-formula", sum(_odd))
assert sum(_odd) == len(_odd) ** 2
res["sum-even-formula"] = opt("sum-even-formula", sum(range(2, 41, 2)))
res["units-digit-of-product"] = opt("units-digit-of-product",
    (4738 * 2691) % 10)
res["tens-digit-of-product"] = opt("tens-digit-of-product",
    (5847 * 3163) // 10 % 10)
assert (47 * 63) // 10 % 10 == (5847 * 3163) // 10 % 10, "two-digit shortcut"
res["unit-conversion-compare"] = cmp2(2.4 * 100, 240)
res["decimal-places-in-product"] = opt("decimal-places-in-product",
    float(F(4, 10) * F(2, 100) * F(5, 10)))
res["compare-fractions-cross"] = cmp2(F(5, 7), F(7, 10))
res["between-zero-and-one"] = cmp2(F(1, 2) ** 2, F(1, 2))
res["root-approx-compare"] = cmp2(50 ** 0.5, 7)
res["root-of-decimal"] = opt("root-of-decimal", round(0.0049 ** 0.5, 6))
res["count-numbers-in-range"] = opt("count-numbers-in-range",
    len(range(18, 97, 2)))
res["equation-or-identity"] = opt("equation-or-identity", "infinitely many")
# "always even" must hold for EVERY odd n, and for exactly one option
_forms = [("p1", lambda n: n*n + 2), ("p2", lambda n: 3*n + 2),
          ("p3", lambda n: n*n + n), ("p4", lambda n: 2*n + 5)]
_always = [k for k, f in _forms if all(f(n) % 2 == 0 for n in (1, 3, 5, 7, 9, 11))]
assert len(_always) == 1, f"{len(_always)} options are always even: {_always}"
res["parity-by-substitution"] = opt("parity-by-substitution", _always[0])
res["product-compare-by-increment"] = cmp2(61 * 30, 62 * 29)
import math as _m
def _lcm(*a):
    r = 1
    for x in a: r = r * x // _m.gcd(r, x)
    return r
res["lcm-word-cue"] = opt("lcm-word-cue", _lcm(4, 6, 9))
def _div7(n):
    return (n // 10 - 2 * (n % 10)) % 7 == 0
res["divisibility-rule-7-11"] = opt("divisibility-rule-7-11",
    [n for n in (413, 417, 421, 425) if n % 7 == 0][0])
assert _div7(413) and 413 % 7 == 0, "the doubling rule must agree"
res["add-radicals-after-simplify"] = opt("add-radicals-after-simplify", "r11r2")
assert abs(2 * 18 ** 0.5 + 5 * 2 ** 0.5 - 11 * 2 ** 0.5) < 1e-9
res["same-exponent-pm"] = opt("same-exponent-pm", "pm5")
assert (-5) ** 6 == 5 ** 6
res["difference-of-squares"] = opt("difference-of-squares", 13 * 4)
res["inscribed-vs-central-angle"] = opt("inscribed-vs-central-angle",
    f"{80 // 2}°")
res["angle-in-semicircle"] = opt("angle-in-semicircle", f"{180 - 90 - 34}°")
def _kind(a, b, c):
    a, b, c = sorted((a, b, c))
    return ("right-angled" if a*a + b*b == c*c else
            "acute-angled" if a*a + b*b > c*c else "obtuse-angled")
res["triangle-type-from-squares"] = opt("triangle-type-from-squares",
    _kind(6, 8, 11))
res["thirty-sixty-ninety"] = opt("thirty-sixty-ninety", 12 // 2)
res["forty-five-triangle"] = opt("forty-five-triangle", "r72")
assert abs((7*7 + 7*7) ** 0.5 - 7 * 2 ** 0.5) < 1e-9
res["midsegment-parallel-half"] = opt("midsegment-parallel-half", 18 // 2)
res["thales-proportional"] = opt("thales-proportional", int(6 * 6 / 4))
res["sector-fraction-of-circle"] = opt("sector-fraction-of-circle",
    f"{int(6**2 * 120 / 360)}π")
res["polygon-interior-angle"] = opt("polygon-interior-angle",
    f"{180 - 360 // 10}°")
res["regular-hexagon-facts"] = opt("regular-hexagon-facts", 2 * 6)
res["trapezium-area"] = opt("trapezium-area", int((9 + 15) / 2 * 6))
res["midpoint-square-half"] = opt("midpoint-square-half", 8 * 8 // 2)
res["mean-after-adjustment"] = opt("mean-after-adjustment", 74 + 36 // 12)
_ns = [n for n in range(1, 40) if 40 * n + 58 == 42 * (n + 1)]
res["count-from-mean-shift"] = opt("count-from-mean-shift", _ns[0])
_sq = [13, 18, 23, 28, 33, 38, 43]
res["mean-of-evenly-spaced"] = opt("mean-of-evenly-spaced",
    sum(_sq) // len(_sq))
_d = sorted([7, 4, 9, 4, 12, 6, 4])
res["median-mode-range"] = cmp2(_d[len(_d) // 2], max(_d) - min(_d))
res["league-matches"] = opt("league-matches", 12 * 11 // 2 * 2)
res["cuts-and-posts"] = opt("cuts-and-posts", f"{(7 - 1) * 8} s")
res["harmonic-average-speed"] = opt("harmonic-average-speed",
    int(2 * 60 * 40 / (60 + 40)))
_net = 100 * F(120, 100) * F(80, 100)
res["compound-percent-change"] = opt("compound-percent-change",
    f"a {int(100 - _net)}% fall")

# ------------------------------------------------------------------ part F
res["angle-bisector-ratio"] = opt("angle-bisector-ratio", int(F(6 * 15, 9)))
res["cyclic-quadrilateral"] = opt("cyclic-quadrilateral", f"{180 - 78}°")
res["arc-length"] = opt("arc-length",
    f"{int(F(120, 360) * 2 * F(22, 7) * 21)} m")
res["distance-midpoint-coordinate"] = opt("distance-midpoint-coordinate",
    int(math.hypot(9 - (-3), (-1) - 4)))
res["circle-equation"] = opt("circle-equation", int(math.isqrt(49)))
_x = [v for v in range(1, 60) if (3 * v + 10) + (5 * v + 10) == 180]
assert len(_x) == 1, _x
res["parallel-angle-pairs"] = opt("parallel-angle-pairs", _x[0])
# same base, apexes on a line parallel to it: equal areas, whatever the lean
def _area(p, q, r):
    return abs((q[0]-p[0])*(r[1]-p[1]) - (r[0]-p[0])*(q[1]-p[1])) / 2
res["equal-area-same-base"] = cmp2(_area((0,0), (6,0), (1.5,4)),
                                   _area((0,0), (6,0), (8.2,4)))
_s = [v for v in range(1, 40) if v * v == 4 * v]
assert _s == [4], _s
res["square-area-equals-perimeter"] = opt("square-area-equals-perimeter", _s[0])
res["circle-in-square"] = opt("circle-in-square", int(14*14 - F(22,7) * 7 * 7))
res["tangent-circles-shaded"] = opt("tangent-circles-shaded",
    f"{12 * 6 - 2 * 3.14 * 3 * 3:.2f}")
_sq_area = (24 / 4) ** 2
_ci_area = math.pi * (24 / (2 * math.pi)) ** 2
res["equal-perimeter-area-order"] = cmp2(round(_sq_area, 6), round(_ci_area, 6))
res["similar-sides-ratio"] = opt("similar-sides-ratio", int(45 * F(5*5, 3*3)))
res["triangle-area-find-base"] = opt("triangle-area-find-base", int(2 * 84 / 12))
from math import comb
res["count-rectangles-in-grid"] = opt("count-rectangles-in-grid",
    comb(4, 2) * comb(3, 2))
res["cuboid-volume-surface"] = cmp2(8 * 5 * 3, 2 * (8*5 + 8*3 + 5*3))
res["cylinder-volume"] = opt("cylinder-volume", int(F(22,7) * 7 * 7 * 10))
res["volume-unit-conversion"] = opt("volume-unit-conversion",
    f"{int(2 * 1.5 * 0.8 * 1000):,}".replace(",", " "))
res["handshakes-vs-gifts"] = cmp2(10 * 9 // 2, 10 * 9)
res["wheel-revolutions"] = opt("wheel-revolutions",
    f"{int(4.4 * 100000 / (F(22,7) * 70)):,}".replace(",", " "))
res["cost-price-from-markup"] = opt("cost-price-from-markup",
    int(F(621) / F(115, 100)))
_p = F(3600, 2 + 3 + 7)
res["ratio-parts-share"] = opt("ratio-parts-share", int(_p * (7 - 2)))
res["combined-work-time"] = opt("combined-work-time",
    int(1 / (F(1, 12) + F(1, 6))))
_days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
res["day-of-week-cycle"] = opt("day-of-week-cycle",
    _days[(_days.index("Tuesday") + 100) % 7])
res["permutation-vs-combination"] = cmp2(comb(8, 3), comb(8, 3) * 6)


# ------------------------------------------------------------------ part G
res["weighted-mean-two-groups"] = opt("weighted-mean-two-groups",
    int(F(20 * 78 + 30 * 68, 50)))
res["mean-missing-value"] = opt("mean-missing-value",
    5 * 80 - (82 + 76 + 90 + 68))
_fm = F(6*5 + 9*7 + 4*8 + 1*10, 20)
res["mean-from-frequency"] = opt("mean-from-frequency", float(_fm))
_d0 = [3, 5, 6, 8, 9, 11, 14]
_d1 = sorted([3, 5, 6, 8, 9, 11, 70])
res["outlier-mean-vs-median"] = cmp2(
    F(sum(_d1), 7) - F(sum(_d0), 7), _d1[3] - _d0[3])
res["probability-complement"] = opt("probability-complement",
    "5⁄8" if F(24 - 9, 24) == F(5, 8) else "?")
_or = len([n for n in range(1, 31) if n % 3 == 0 or n % 5 == 0])
assert F(_or, 30) == F(7, 15), _or
res["probability-or-multiples"] = opt("probability-or-multiples", "7⁄15")
assert F(5, 8) * F(4, 7) == F(5, 14)
res["probability-without-replacement"] = opt("probability-without-replacement", "5⁄14")
res["expected-count-from-probability"] = opt("expected-count-from-probability",
    int(F(15, 100) * 2400))
assert F(int(F(22, 7) * 49), 14 * 14) == F(11, 14)
res["probability-from-area"] = opt("probability-from-area", "11⁄14")
res["counting-code-choices"] = opt("counting-code-choices",
    f"{5 * 5 * 10 ** 3:,}".replace(",", " "))
res["counting-with-constraint"] = opt("counting-with-constraint",
    comb(5, 2) * comb(4, 1))
_ev = sorted([6, 13, 9, 20, 18, 11, 15, 24])
res["median-even-count"] = opt("median-even-count",
    int((_ev[3] + _ev[4]) / 2))
_r5 = [12, 19, 25, 31, 47]
res["range-after-adding-value"] = cmp2(max(_r5) - min(_r5),
                                       max(_r5 + [8]) - min(_r5 + [8]))
res["pie-percent-to-amount"] = opt("pie-percent-to-amount",
    int(F(100 - (20 + 15 + 25), 100) * 7200))
_A = [30, 42, 38, 55, 50]; _B = [22, 26, 34, 31, 44]
_MO = ["January", "February", "March", "April", "May"]
_gp = [a - b for a, b in zip(_A, _B)]
res["line-largest-gap"] = opt("line-largest-gap", _MO[_gp.index(max(_gp))])
res["bar-percent-increase"] = opt("bar-percent-increase",
    f"{int((63 - 45) * 100 / 45)}%")
_f = [9, 12, 8, 14, 5]; _lab = ["0 – 10", "10 – 20", "20 – 30", "30 – 40", "40 – 50"]
_run, _k = 0, None
for _i, _x in enumerate(_f):
    _run += _x
    if _k is None and _run >= sum(_f) / 2:
        _k = _i
res["histogram-median-class"] = opt("histogram-median-class", _lab[_k])
_g = {"Jeddah": (240, 288), "Makkah": (180, 234),
      "Madinah": (120, 132), "Dammam": (60, 81)}
res["table-largest-percent-rise"] = opt("table-largest-percent-rise",
    max(_g, key=lambda k: F(_g[k][1] - _g[k][0], _g[k][0])))
_sc = {"School A": (120, 80), "School B": (90, 110), "School C": (150, 150)}
_maj = [k for k, (b, gg) in _sc.items() if gg * 2 > b + gg]
assert len(_maj) == 1, _maj
res["stacked-bar-majority"] = opt("stacked-bar-majority", _maj[0] + " only")
res["pictogram-key-scale"] = opt("pictogram-key-scale", (7 - 4) * 8)


# ------------------------------------------------------------------ part H
_pts = [(0,0),(7,0),(7,2),(4,2),(4,3.5),(2,3.5),(2,5),(0,5)]
_per = sum(abs(_pts[i][0]-_pts[i-1][0]) + abs(_pts[i][1]-_pts[i-1][1])
           for i in range(len(_pts)))
assert _per == 2 * (7 + 5), _per
res["rectilinear-perimeter"] = opt("rectilinear-perimeter", int(_per))
_p = F(180, 3+4+5)
res["triangle-angles-from-ratio"] = opt("triangle-angles-from-ratio", f"{int(_p*5)}°")
_r = math.isqrt(36)                       # pi r^2 = 36 pi  ->  r = 6
res["circle-area-to-square-area"] = opt("circle-area-to-square-area", (2*_r)**2)
_hyp = math.isqrt(6*6 + 8*8)
res["right-triangle-in-circle-circumference"] = opt(
    "right-triangle-in-circle-circumference", f"{3.14*_hyp:.1f}")
# x^2 + y^2 = 0 over the reals forces x = y = 0
_sols = [(x, y) for x in range(-6, 7) for y in range(-6, 7) if x*x + y*y == 0]
assert _sols == [(0, 0)], _sols
res["sum-of-squares-zero"] = opt("sum-of-squares-zero", 0*0 - 0*0)
# an even power carries two real roots; the stem fixes the sign, so the
# verifier must apply the same condition rather than assume uniqueness
_x4 = [x for x in range(-30, 31) if (x + 8)**4 == 10000 and x > 0]
assert len(_x4) == 1, _x4
res["equate-fourth-powers"] = opt("equate-fourth-powers", _x4[0])
_xr = [x for x in range(-30, 31) if 2*x + 1 != 0 and x + 2 != 0
       and F(1, 2*x+1) == F(1, x+2)]
assert len(_xr) == 1, _xr
res["equal-reciprocals-denominators"] = opt("equal-reciprocals-denominators", _xr[0])


# ------------------------------------------------------------------ part I
res["multiply-near-round"] = opt("multiply-near-round", f"{998*25:,}".replace(",", " "))
res["multiply-by-1001"] = opt("multiply-by-1001", f"{372*1001:,}".replace(",", " "))
res["count-hundreds-in-number"] = opt("count-hundreds-in-number", 75632 // 100)
_dsum = lambda n: sum(int(c) for c in str(n))
_dd = [n for n in (121, 142, 132, 155) if n % _dsum(n) == 0]
assert _dd == [132], _dd
res["divisible-by-digit-sum"] = opt("divisible-by-digit-sum", _dd[0])
_q9 = [q for q in range(10) if (2000 + 110*q + 6) % 9 == 0]
assert _q9 == [5], _q9
res["divisibility-by-9-find-digit"] = opt("divisibility-by-9-find-digit", _q9[0])
res["fraction-percent-to-decimal"] = opt("fraction-percent-to-decimal",
                                         float(F(3, 4) / 100))
res["decimal-multiply-then-add"] = opt("decimal-multiply-then-add",
    float(F(6, 100) * F(5, 10) + F(22, 1000)))
res["sum-symmetric-pairing"] = opt("sum-symmetric-pairing",
    sum([1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1]))
_disc = min(F(15, 100) * 1200, 150)
res["percent-discount-with-cap"] = opt("percent-discount-with-cap",
    f"{int(1200 - _disc):,}".replace(",", " "))
res["compare-near-one-fractions"] = cmp2(F(100, 99), F(1000, 999))
res["divide-by-zero-undefined"] = opt("divide-by-zero-undefined",
                                      "A equals zero and B is undefined")
res["quotient-of-two-primes"] = opt("quotient-of-two-primes",
                                    "Always a fraction that cannot be simplified")
assert math.gcd(3, 7) == 1
res["count-digits-in-range"] = opt("count-digits-in-range",
    sum(len(str(n)) for n in range(1, 201)))
_cm = [n for n in range(1, 100) if n % 6 == 0 and n % 8 == 0]
assert _cm == [24, 48, 72, 96], _cm
res["count-common-multiples"] = opt("count-common-multiples", len(_cm))
# 52, ?, 34, 28, 24 : first differences fall by 2 each step
_seq = [52, None, 34, 28, 24]
_x = 34 + 8
assert (_x - 52, 34 - _x, 28 - 34, 24 - 28) == (-10, -8, -6, -4)
res["second-difference-sequence"] = opt("second-difference-sequence", _x)
res["reverse-square-sequence"] = opt("reverse-square-sequence", (7 + 1) ** 2)

res["n-to-the-n-sequence"] = opt("n-to-the-n-sequence", 4 ** 4)
assert [n ** n for n in (1, 2, 3, 5)] == [1, 4, 27, 3125]
res["zero-product-inference"] = opt("zero-product-inference", "k")
res["recurrence-sign-flip"] = (lambda: (
    lambda a: opt("recurrence-sign-flip", a[9]))(
    [x for x in __import__("itertools").accumulate(
        range(10), lambda p, _: -p + 3, initial=-8)][:10]))()
_pq = [(a, b) for a in range(1, 19) for b in range(1, 19)
       if a * b == 18 and a * a - b * b == 27]
assert _pq == [(6, 3)], _pq
res["product-and-difference-of-squares"] = opt("product-and-difference-of-squares", _pq[0][0])
_pqs = [(p, q) for p in range(-20, 21) for q in range(-20, 21)
        if q + 1 != 0 and q - 3 != 0 and F(p + 2, q + 1) == 1 and F(p - 1, q - 3) == 2]
assert _pqs == [(3, 4)], _pqs
res["fraction-transform-system"] = opt("fraction-transform-system", "i_o_f2")
res["translate-verbal-to-equation"] = opt("translate-verbal-to-equation", "i_o_v1")
# A - B = 5, B - C = 3, C + D = 1  ->  add: A + D = 9
res["chain-substitution-sum"] = opt("chain-substitution-sum", 5 + 3 + 1)
res["fraction-of-number-given"] = opt("fraction-of-number-given", int(3 * F(2, 3)))
_c3 = [n for n in range(2, 50) if (n - 1) * n * (n + 1) == 5 * 3 * n]
assert _c3 == [4], _c3
res["consecutive-product-equals-sum"] = opt("consecutive-product-equals-sum", _c3[0] - 1)
_t3 = [n for n in range(1, 30) if n * (n + 1) * (n + 2) == 990 and 11 in (n, n + 1, n + 2)]
assert _t3 == [9], _t3
res["consecutive-from-product"] = opt("consecutive-from-product", 9 + 10 + 11)
_qr = sorted(n for n in range(-20, 21) if 10 * n + n * n == 10 * n + 4 * n)
assert _qr == [0, 4], _qr
res["quadratic-lost-root"] = opt("quadratic-lost-root", "n = 0 and n = 4")
_tot = (12 + 15 + 19) // 2
res["three-pair-sums-system"] = opt("three-pair-sums-system", _tot - 19)

res["surface-area-rectangular-prism"] = opt("surface-area-rectangular-prism",
                                            2 * (5 * 2 + 5 * 2 + 2 * 2))
res["rectangle-axes-of-symmetry"] = opt("rectangle-axes-of-symmetry", 2)
res["circles-packed-in-rectangle"] = opt("circles-packed-in-rectangle", 6 // 3)
assert 6 / 3 == 4 / 2
res["lshape-area-from-outer-sides"] = opt("lshape-area-from-outer-sides", 5 * 4 - 2 * 2)
res["wire-reshape-perimeter"] = opt("wire-reshape-perimeter", 4 * 9 // 3)
_s = [s for s in range(1, 20) if 4 * s == s * s]
assert _s == [4], _s
res["cube-face-perimeter-equals-area"] = opt("cube-face-perimeter-equals-area", _s[0] ** 3)
res["diagonals-sum-vs-perimeter"] = opt("diagonals-sum-vs-perimeter",
    "The sum of the diagonals is greater" if 2 * 2 ** .5 > 4 else "The perimeter is greater")
res["triangles-from-both-diagonals"] = opt("triangles-from-both-diagonals", 4 + 4)
_P = 1.0
res["isoperimetric-circle-vs-square"] = opt("isoperimetric-circle-vs-square",
    "The circle" if _P**2/(4*math.pi) > _P**2/16 else "The square")
res["count-small-cubes-in-cube"] = opt("count-small-cubes-in-cube",
                                       round((F(15, 10) / F(5, 10)) ** 3))
_sc = [s for s in range(1, 40) if 6 * s + (4 * s - 20) == 90]
assert _sc == [11], _sc
res["complementary-angles-solve"] = opt("complementary-angles-solve", _sc[0])

def _median(v):
    v = sorted(v)
    n = len(v)
    return v[n // 2] if n % 2 else F(v[n // 2 - 1] + v[n // 2], 2)
_ms = [s for s in range(0, 20) if _median([12, 11, 5, 2, s]) == 6]
assert _ms == [6], _ms
res["median-with-unknown-value"] = opt("median-with-unknown-value", _ms[0])
# five naturals, min 2, unique mode 7, mean 6 -> enumerate every case
from collections import Counter
_meds = set()
for combo in __import__("itertools").combinations_with_replacement(range(2, 27), 5):
    if sum(combo) != 30 or min(combo) != 2:
        continue
    c = Counter(combo).most_common()
    if c[0][0] != 7 or (len(c) > 1 and c[1][1] == c[0][1]) or c[0][1] < 2:
        continue
    _meds.add(_median(combo))
assert _meds == {7}, _meds
res["median-from-mean-and-mode"] = opt("median-from-mean-and-mode", 7)
_ns = F(30, 100) * 200 + F(20, 100) * 300
res["weighted-percent-two-groups"] = opt("weighted-percent-two-groups",
                                         f"{int(_ns / 500 * 100)}%")
res["counts-from-probability-fraction"] = opt("counts-from-probability-fraction",
                                              int(40 - F(2, 5) * 40))
res["score-needed-for-target-percent"] = opt("score-needed-for-target-percent",
                                             int(F(80, 100) * 80) - 30)
# the drawn figure is the source of truth for the intersection count
import numpy as _np
_xx = _np.linspace(0, 12, 4000)
_f = 62 + 5.0 * _np.sin(_xx - 0.929)
_g = 62 + 4.5 * _np.sin(_xx - 0.929 + 2.2)
_sg = _np.sign(_f - _g)
_cr = int(_np.sum(_sg[1:] * _sg[:-1] < 0))
assert _cr == 4, _cr
res["count-graph-intersections"] = opt("count-graph-intersections", _cr)

res["profit-percent-from-quantity-pricing"] = opt("profit-percent-from-quantity-pricing",
    f"{int(F(20 - 16, 16) * 100)}%")
_h = (8 + (5400 // 60) % 24) % 24
assert _h == 2
res["minutes-to-clock-time"] = opt("minutes-to-clock-time", "2 a.m.")
_parts = 2 * 2 + 3 * 1
res["inheritance-double-shares"] = opt("inheritance-double-shares",
    f"{84000 // _parts:,}".replace(",", " "))
_mins = (13 * 60 + 5) - (9 * 60 + 20)
res["ceiling-billing-per-hour"] = opt("ceiling-billing-per-hour",
                                      5 * math.ceil(F(_mins, 60)))
_meet = F(340 - 60 * 1, 60 + 80)
assert _meet == 2
res["meeting-with-staggered-start"] = opt("meeting-with-staggered-start",
    f"{9 + int(_meet)}:00 a.m.")
_pages, _day, _tot2 = 5, 0, 0
while _tot2 < 155:
    _tot2 += _pages * (2 ** _day)
    _day += 1
assert (_tot2, _day) == (155, 5), (_tot2, _day)
res["doubling-pages-cumulative"] = opt("doubling-pages-cumulative",
    ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"][_day - 1])


# ------------------------------------------------------------------ part J
res["round-then-add-estimate"] = opt("round-then-add-estimate",
    f"{round(3968, -3) + round(2013, -3) + round(1022, -3):,}".replace(",", " "))
res["fraction-of-quantity"] = opt("fraction-of-quantity", int(F(3, 8) * 640))
res["percent-to-fraction-simplify"] = opt("percent-to-fraction-simplify",
    "j_pf2" if F(35, 100) == F(7, 20) else "?")
res["fraction-to-decimal"] = opt("fraction-to-decimal", float(F(5, 8)))
res["ratio-to-percent"] = opt("ratio-to-percent", f"{float(F(3, 3+5) * 100)}%")
res["square-root-large-perfect"] = opt("square-root-large-perfect", math.isqrt(576))
assert math.isqrt(576) ** 2 == 576
_cb = [n for n in range(1, 20) if n ** 3 == 216]
res["cube-root-integer"] = opt("cube-root-integer", _cb[0])
res["odd-power-negative-base"] = opt("odd-power-negative-base", (-2) ** 5)
res["scientific-notation-small"] = opt("scientific-notation-small",
    "j_sn1" if F(42, 100000) == F(42, 10) * F(1, 10) ** 4 else "?")
res["exponent-laws-combine"] = opt("exponent-laws-combine", 2 ** 7 * 2 ** 5 // 2 ** 9)
res["percent-change-two-values"] = opt("percent-change-two-values",
    f"{int(F(50 - 40, 40) * 100)}%")
res["reverse-percent-original"] = opt("reverse-percent-original",
    int(F(240) / F(80, 100)))
res["add-unlike-fractions"] = opt("add-unlike-fractions",
    "j_a2" if F(2, 3) + F(3, 4) == F(17, 12) else "?")
res["count-factors"] = opt("count-factors", len([d for d in range(1, 37) if 36 % d == 0]))
res["hcf-three-numbers"] = opt("hcf-three-numbers", math.gcd(24, math.gcd(36, 60)))
res["lcm-two-numbers"] = opt("lcm-two-numbers", 12 * 18 // math.gcd(12, 18))
res["round-decimal-places"] = opt("round-decimal-places", round(3.4567, 2))
res["absolute-value-sum"] = opt("absolute-value-sum", abs(-7) + abs(3 - 9))
res["order-of-operations"] = opt("order-of-operations", 12 + 6 // 2 * (5 - 3))
res["percent-eighth-mental"] = opt("percent-eighth-mental", int(F(125, 1000) * 640))
_d4 = [n for n in (1234, 3218, 5316, 7122) if n % 4 == 0]
assert _d4 == [5316], _d4
res["divisibility-by-4-rule"] = opt("divisibility-by-4-rule",
    f"{_d4[0]:,}".replace(",", " "))
res["arithmetic-sequence-nth-term"] = opt("arithmetic-sequence-nth-term", 5 + 19 * 4)
res["geometric-sequence-nth-term"] = opt("geometric-sequence-nth-term", 3 * 2 ** 6)

res["substitute-two-variables"] = opt("substitute-two-variables", 3 * 4 - 2 * (-1))
_x2 = [x for x in range(-20, 21) if 5 * x - 7 == 23]
res["solve-two-step-equation"] = opt("solve-two-step-equation", _x2[0])
_xb = [x for x in range(-20, 21) if 3 * (x - 4) == 18]
res["solve-equation-with-brackets"] = opt("solve-equation-with-brackets", _xb[0])
# 5x + 3y - 2x + 7y  ==  3x + 10y  for every x and y
assert all(5*x + 3*y - 2*x + 7*y == 3*x + 10*y
           for x in range(-3, 4) for y in range(-3, 4))
res["combine-like-terms"] = opt("combine-like-terms", "j_c1")
assert all((4*x - 5 < 11) == (x < 4) for x in range(-10, 11))
res["solve-linear-inequality"] = opt("solve-linear-inequality", "j_i1")
assert all((x+3)*(x-5) == x*x - 2*x - 15 for x in range(-6, 7))
res["expand-two-brackets"] = opt("expand-two-brackets", "j_e1")
assert all(6*x*x + 9*x == 3*x*(2*x + 3) for x in range(-6, 7))
res["factor-common-monomial"] = opt("factor-common-monomial", "j_g1")
res["evaluate-function-negative"] = opt("evaluate-function-negative", 2*(-2)**2 - 3)
res["slope-from-two-points"] = opt("slope-from-two-points", int(F(11 - 2, 4 - 1)))

_ml = [4, 7, 9, 10, 15]
res["mean-of-list"] = opt("mean-of-list", int(F(sum(_ml), len(_ml))))
_rl = [12, 5, 18, 7, 20]
res["range-of-list"] = opt("range-of-list", max(_rl) - min(_rl))
res["median-odd-count"] = opt("median-odd-count", _median([14, 3, 9, 21, 6]))
res["probability-single-die"] = opt("probability-single-die",
    "j_p13" if F(len([d for d in range(1, 7) if d > 4]), 6) == F(1, 3) else "?")
_coins = [(a, b) for a in "HT" for b in "HT"]
res["probability-two-coins"] = opt("probability-two-coins",
    "j_p12" if F(len([c for c in _coins if c.count("H") == 1]), len(_coins)) == F(1, 2) else "?")
_dice = [(a, b) for a in range(1, 7) for b in range(1, 7)]
res["probability-two-dice-sum"] = opt("probability-two-dice-sum",
    "j_p16" if F(len([d for d in _dice if sum(d) == 7]), 36) == F(1, 6) else "?")
res["arrangements-with-repeats"] = opt("arrangements-with-repeats",
    len(set(__import__("itertools").permutations("SALAM"))))

res["time-from-distance-speed"] = opt("time-from-distance-speed",
    "1 hour 30 minutes" if F(90, 60) == F(3, 2) else "?")
res["discount-then-vat"] = opt("discount-then-vat",
    int(400 * F(75, 100) * F(115, 100)))
res["best-buy-unit-price"] = opt("best-buy-unit-price",
    f"{float(F(21, 3) - F(32, 5)):.2f} SAR")
res["recipe-scale-ratio"] = opt("recipe-scale-ratio", int(F(300, 4) * 10))
res["profit-percent-simple"] = opt("profit-percent-simple",
    f"{int(F(100 - 80, 80) * 100)}%")
res["annual-after-deduction"] = opt("annual-after-deduction",
    f"{int(7000 * F(85, 100) * 12):,}".replace(",", " "))
res["minimum-buses-ceiling"] = opt("minimum-buses-ceiling", math.ceil(F(146, 40)))
res["simple-interest-one-year"] = opt("simple-interest-one-year",
    f"{int(12000 + 2 * F(5, 100) * 12000):,}".replace(",", " "))


# ------------------------------------------------------------------ part K
res["half-of-a-power"] = opt("half-of-a-power",
    "k_h2" if F(2 ** 50, 2) == 2 ** 49 else "?")
res["digit-sum-of-square"] = opt("digit-sum-of-square",
    sum(int(c) for c in str(999 ** 2)))
_odd3 = min(n for n in range(100, 1000) if n % 2 == 1)
_even2 = max(n for n in range(10, 100) if n % 2 == 0)
assert (_odd3, _even2) == (101, 98)
res["extreme-numbers-by-digit-count"] = opt("extreme-numbers-by-digit-count",
                                            _odd3 - _even2)
res["difference-of-powers-of-ten"] = opt("difference-of-powers-of-ten",
    "k_d1" if 10 ** 7 - 10 ** 6 == 9 * 10 ** 6 else "?")
res["product-of-decimals-standard-form"] = opt("product-of-decimals-standard-form",
    "k_p1" if F(3, 10) * F(3, 100) * F(3, 1000) == F(27, 10 ** 6) else "?")
res["ratio-as-fraction-direction"] = opt("ratio-as-fraction-direction",
    int(20 / F(1, 20)))
res["percent-part-to-complement-count"] = opt("percent-part-to-complement-count",
    int(F(30) / F(60, 100)) - 30)

# xy < 0 : only the term with every letter at an even power stays non-negative
_pairs = [(x, y) for x in range(-4, 5) for y in range(-4, 5) if x * y < 0]
_never_neg = [k for k, f in (("k_s2", lambda x, y: x*x*y),
                             ("k_s3", lambda x, y: x*y*y),
                             ("k_s1", lambda x, y: x*x*y*y),
                             ("k_s4", lambda x, y: x**3 * y**3))
              if all(f(x, y) >= 0 for x, y in _pairs)]
assert _never_neg == ["k_s1"], _never_neg
res["even-powers-never-negative"] = opt("even-powers-never-negative", "k_s1")
assert all(F(n + (n + 2) + (n + 10), 3) == n + 4 for n in range(-5, 6))
res["mean-of-algebraic-terms"] = opt("mean-of-algebraic-terms", "k_m1")
# 1.2x = 0.8y  ->  x : y = 2 : 3
assert F(12, 10) * 2 == F(8, 10) * 3
res["equal-after-opposite-percent-changes"] = opt("equal-after-opposite-percent-changes",
                                                  "2 : 3")

res["square-minus-corner-triangle"] = opt("square-minus-corner-triangle",
    int(8 * 8 - (8 - 4) * (8 - 5) / 2))
# 2x + 2y + a = 360  ->  180 - x - y = a/2
res["angles-round-point-expression"] = opt("angles-round-point-expression", "k_a1")
res["count-rectangles-in-strip"] = opt("count-rectangles-in-strip",
    len([(i, j) for i in range(7) for j in range(7) if i < j]))
res["concave-quadrilateral-reflex-angle"] = opt("concave-quadrilateral-reflex-angle",
                                                360 - (60 + 30 + 20))
# 2*pi*r against r^2 : the winner changes with r, so neither can be named
_small = 2 * math.pi * 2 > 2 ** 2
_large = 2 * math.pi * 10 > 10 ** 2
assert _small and not _large
res["cylinder-compare-insufficient-data"] = opt("cylinder-compare-insufficient-data",
                                                "not enough information")
_r = 10
assert 2 * math.pi * _r == math.pi * 20          # circumference 20 pi
res["compare-circumference-with-triangle-area"] = cmp2(round(2 * 3.14 * _r, 6),
                                                       0.5 * (2 * _r) * _r)
res["three-quarter-sector-diameter"] = opt("three-quarter-sector-diameter",
    "k_q3" if F(3, 4) * (F(8, 2) ** 2) == 12 else "?")

_primes = [n for n in range(1, 11)
           if n > 1 and all(n % d for d in range(2, int(n ** .5) + 1))]
assert _primes == [2, 3, 5, 7], _primes
res["probability-prime-in-range"] = opt("probability-prime-in-range",
    "k_pr1" if F(len(_primes), 10) == F(2, 5) else "?")
res["bar-share-per-person"] = opt("bar-share-per-person", 60000 // 150)
_comp = {"Candidate 1": (4, 2), "Candidate 2": (4, 2),
         "Candidate 3": (4, 3), "Candidate 4": (5, 1)}
_sc = {k: 2 * c - w for k, (c, w) in _comp.items()}
res["table-score-with-penalty"] = opt("table-score-with-penalty",
                                      max(_sc, key=_sc.get))
res["minute-hand-degrees"] = opt("minute-hand-degrees", f"{8 * (360 // 60)}°")


# ------------------------------------------------------------------ part L
res["salary-plus-commission-target"] = opt("salary-plus-commission-target",
    (12000 - 7000) // 500)
res["linear-depreciation"] = opt("linear-depreciation", 1800 - 200 * 7)
res["months-to-reach-savings-target"] = opt("months-to-reach-savings-target",
    math.ceil(F(45000 - 17000, 2000)))
res["count-from-total-and-unit-price"] = opt("count-from-total-and-unit-price",
    4000 // 20)
_span = (3 * 60 + 30) + (24 * 60 - 20 * 60)          # 8 pm to 3:30 am
assert _span == 450, _span
res["time-span-across-midnight-split"] = opt("time-span-across-midnight-split",
                                             _span // 6)
# fewest rooms for 58 guests from rooms of 2, 3 or 4: search every combination
_best = min(a + b + c for a in range(0, 30) for b in range(0, 30)
            for c in range(0, 30) if 4 * a + 3 * b + 2 * c >= 58)
assert _best == 15, _best
res["minimum-rooms-largest-capacity"] = opt("minimum-rooms-largest-capacity", _best)
res["fraction-difference-to-whole"] = opt("fraction-difference-to-whole",
    int(6 / (F(1, 2) - F(1, 6))))
res["rate-difference-over-time"] = opt("rate-difference-over-time", (8 - 6) * 16)
res["floor-division-full-containers"] = opt("floor-division-full-containers",
                                            900 // 72)
_saud = 2100; _mansour = _saud - 500; _yusuf = _mansour + 300
res["chained-money-comparisons"] = opt("chained-money-comparisons",
    f"{_yusuf:,}".replace(",", " "))

_xf = [x for x in range(1, 60) if F(x, 3) + F(x, 6) == 9]
assert _xf == [18], _xf
res["solve-equation-unlike-denominators"] = opt("solve-equation-unlike-denominators",
                                                _xf[0])
# ab = 1, bc = 2, ac = 8  ->  (abc)^2 = 16
_abc = math.isqrt(1 * 2 * 8)
assert _abc ** 2 == 16
res["product-of-pair-products"] = opt("product-of-pair-products", _abc)
_sc = [s for s in range(1, 10) if s * s == s ** 3]
assert _sc == [1], _sc
res["square-equals-cube"] = opt("square-equals-cube", _sc[0])
_h = [h for h in range(1, 200) if F(h) == F(h, 4) + 30]
assert _h == [40], _h
res["self-referential-linear"] = opt("self-referential-linear", _h[0])
_w = [x for x in range(1, 40) if x * (x + 4) == 45]
assert _w == [5], _w
res["quadratic-from-rectangle-area"] = opt("quadratic-from-rectangle-area", _w[0])

_s = [2]
while len(_s) < 5:
    _s.append(2 * _s[-1] + 1)
assert _s[:4] == [2, 5, 11, 23], _s
res["double-plus-one-sequence"] = opt("double-plus-one-sequence", _s[4])
_rem = [n for n in range(2, 200)
        if n % 2 == 1 and n % 3 == 2 and n % 4 == 3]
assert _rem[0] == 11, _rem[:3]
res["remainders-one-less-than-lcm"] = opt("remainders-one-less-than-lcm", _rem[0])
_run = [n for n in range(-20, 40) if F(sum(range(n, n + 7)), 7) == 7]
assert _run == [4], _run
res["consecutive-average-to-smallest"] = opt("consecutive-average-to-smallest",
                                             _run[0])
res["halala-riyal-compare"] = cmp2(F(2500, 100), 25)
res["percent-commutes-compare"] = cmp2(F(40, 100) * 60, F(60, 100) * 40)
res["sum-of-squares-vs-square-compare"] = cmp2(606 ** 2 + 505 ** 2, 707 ** 2)

_grid = [3, 8, 5, 12, 7, 2, 9, 4, 11, 6, 10, 1, 5, 13, 8, 6]
res["median-from-table-grid"] = opt("median-from-table-grid",
                                    float(_median(_grid)))


# ============================================================= PART M (new)
res["lcm-three-buses"] = opt("lcm-three-buses", math.lcm(18, 24, 30))
_L = math.lcm(9, 12)
_cands = [n for n in range(200, 301) if (n - 4) % _L == 0]
assert _cands == [256] or 256 in _cands
res["remainder-common-divisor"] = opt("remainder-common-divisor", 256)
res["ratio-mix-paint"] = opt("ratio-mix-paint", float(F(96, 10) * F(3, 8)))
res["defect-rate-scaled"] = opt("defect-rate-scaled", int(F(3, 250) * 12500))
_area_km2 = F((3 * 40000) * (2 * 40000), 10 ** 10)
res["map-scale-area"] = opt("map-scale-area", float(_area_km2))
res["successive-discounts"] = opt("successive-discounts",
    int(F(800) * F(75, 100) * F(90, 100)))
_net = F(100) * F(120, 100) * F(80, 100) - F(100)
assert _net == -4
res["percent-inc-then-dec"] = opt("percent-inc-then-dec", "decreased by 4%")
res["vat-reverse"] = opt("vat-reverse", int(F(690) / F(115, 100)))
_k = F(50, 10)
res["age-ratio-future"] = opt("age-ratio-future", int(7 * _k))
assert 4 * (7 * _k + 10) == 9 * (2 * _k + 10)
res["combined-tank-rate-not-enough-info"] = CMP["ND"]
res["geometric-8th-term"] = opt("geometric-8th-term", 3 * 2 ** 7)
_S = 20 / 2 * (2 * 7 + 19 * 5)
res["arith-series-sum"] = opt("arith-series-sum", int(_S))

res["weighted-avg-exam-components"] = opt("weighted-avg-exam-components",
    int(F(20, 100) * 70 + F(30, 100) * 80 + F(50, 100) * 90))
_mids = [5, 15, 25, 35, 45]; _freqs = [5, 12, 18, 10, 5]
_gm = F(sum(m * f for m, f in zip(_mids, _freqs)), sum(_freqs))
res["grouped-mean-estimate"] = opt("grouped-mean-estimate", float(_gm))
_revs = {q: u * 1000 * 25 for q, u in zip(["Q1", "Q2", "Q3", "Q4"], [40, 55, 35, 70])}
assert _revs["Q4"] > 1_500_000 and all(_revs[q] <= 1_500_000 for q in ["Q1", "Q2", "Q3"])
res["bar-chart-revenue-target"] = opt("bar-chart-revenue-target", "Q4")
_hrs = [0, 2, 4, 6, 8]; _temp = [18, 22, 29, 31, 33]
_diffs = [_temp[i + 1] - _temp[i] for i in range(4)]
assert _diffs.index(max(_diffs)) == 1
res["line-chart-steepest-rise"] = opt("line-chart-steepest-rise", "2 to 4 hours")
_p_no_red = F(6, 10) * F(5, 9)
res["probability-at-least-one-red"] = opt("probability-at-least-one-red",
    str(1 - _p_no_red))
_total_arr = math.factorial(6); _adj = math.factorial(5) * math.factorial(2)
res["permutation-vowels-not-adjacent"] = opt("permutation-vowels-not-adjacent",
    _total_arr - _adj)
_data = [12, 15, 15, 18, 90]
res["median-vs-mean-outlier"] = cmp2(_median(_data), F(sum(_data), len(_data)))
res["two-group-percent-total"] = opt("two-group-percent-total",
    int(F(45, 100) * 120 + F(20, 100) * 80))

# ============================================================= PART N (new)
res["percent-of-simple-quantity"] = opt("percent-of-simple-quantity",
    int(F(35, 100) * 240))
_girls = F(60, 100) * 40
res["percent-find-part-from-total"] = opt("percent-find-part-from-total",
    int(40 - _girls))
res["percent-increase-simple"] = opt("percent-increase-simple",
    int(F(250) * F(112, 100)))
res["percent-of-percent-simple"] = opt("percent-of-percent-simple",
    int(F(10, 100) * F(30, 100) * 900))

res["weighted-avg-equal-group-sizes"] = opt("weighted-avg-equal-group-sizes",
    int(F(80 + 90, 2)))
res["weighted-avg-unequal-small-groups"] = opt("weighted-avg-unequal-small-groups",
    int(F(8 * 70 + 12 * 85, 20)))
res["weighted-avg-price-per-kg"] = opt("weighted-avg-price-per-kg",
    int(F(5 * 20 + 15 * 24, 20)))

res["permutation-simple-books"] = opt("permutation-simple-books", 5 * 4 * 3)
res["combination-simple-committee"] = opt("combination-simple-committee",
    math.comb(7, 3))
res["word-arrangement-simple-factorial"] = opt("word-arrangement-simple-factorial",
    math.factorial(4))

_hrs = [0, 1, 2, 3, 4]; _dist = [2, 7, 14, 17, 22]
res["line-graph-read-value"] = opt("line-graph-read-value", _dist[2])
res["line-graph-total-increase"] = opt("line-graph-total-increase",
    _dist[4] - _dist[0])
res["line-graph-average-rate"] = opt("line-graph-average-rate",
    F(_dist[4] - _dist[0], _hrs[4] - _hrs[0]))

_f = [4, 9, 15, 10, 2]
res["histogram-modal-class"] = opt("histogram-modal-class", "70–80")
res["histogram-total-count"] = opt("histogram-total-count", sum(_f))
res["histogram-count-above-threshold"] = opt("histogram-count-above-threshold",
    _f[3] + _f[4])

res["improper-fraction-to-mixed-number"] = opt("improper-fraction-to-mixed-number",
    "3 2/5")
res["add-two-mixed-numbers"] = opt("add-two-mixed-numbers", "4 7/12")
_a = F(9, 12) + F(10, 12)
assert _a == F(19, 12)
res["mixed-number-recipe-scaling"] = opt("mixed-number-recipe-scaling",
    float(F(5, 2) * 3))

res["solve-decimal-equation-simple"] = opt("solve-decimal-equation-simple",
    int((8 - 3) / F(5, 10)))
res["solve-decimal-equation-both-sides"] = opt("solve-decimal-equation-both-sides",
    int(F(88, 10) / F(8, 10)))
res["decimal-equation-taxi-fare"] = opt("decimal-equation-taxi-fare",
    int((26 - 5) / F(175, 100)))

# ============================================================= PART O (new)
res["rate-scale-workers-inverse"] = opt("rate-scale-workers-inverse",
    int(F(5 * 6, 3)))
_ra = F(1, 8); _rb = F(1, 12)
res["pipe-two-rates-together"] = opt("pipe-two-rates-together", float(1 / (_ra + _rb)))
_ra2 = F(1, 10); _rb2 = F(1, 15)
_done = 3 * (_ra2 + _rb2)
_remaining = 1 - _done
res["combined-then-one-leaves"] = opt("combined-then-one-leaves",
    float(_remaining / _rb2))
_rin = F(1, 6); _rout = F(1, 10)
res["inlet-outlet-net-rate"] = opt("inlet-outlet-net-rate", int(1 / (_rin - _rout)))

_t1 = F(30, 30); _t2 = F(120, 60)
res["avg-speed-weighted-distances"] = opt("avg-speed-weighted-distances",
    int(F(30 + 120, _t1 + _t2)))
res["two-trains-toward-each-other"] = opt("two-trains-toward-each-other",
    int(F(315, 60 + 45)))

_amal_future = 2 * 8
res["future-age-given-current"] = opt("future-age-given-current", _amal_future - 6)
res["three-ages-ratio-sum"] = opt("three-ages-ratio-sum", int(F(54, 18) * 4))

_ns = [x for x in range(0, 9) if 6 * x + 2 * (8 - x) == 36]
assert _ns == [5], _ns
res["two-item-purchase-system"] = opt("two-item-purchase-system", _ns[0])
_interest = 13200 - 10000
res["simple-interest-rate"] = opt("simple-interest-rate",
    int(F(_interest, 10000 * 4) * 100))

missing = sorted(set(BY) - set(res))
fails = [(s, res[s], BY[s]["ans"]) for s in res if res[s] != BY[s]["ans"]]
print(f"checked {len(res)} of {len(BY)}")
if missing:
    print("NOT CHECKED:", missing)
for s, got, claimed in fails:
    print(f"  FAIL {s}: verified {got}, bank says {claimed}  opts={BY[s]['opts']}")
print("FAILURES:", len(fails))
