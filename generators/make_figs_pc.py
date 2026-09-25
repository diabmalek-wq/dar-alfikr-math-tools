"""The nine diagrams from Mr Tamer Elsawy's third practice set (Set C), redrawn.

Same rule as parts 8 and 10: CONSTRUCTED, never traced. The chart values were
read off the source at 3-8x and are written here as data, so the figure and the
answer key cannot drift apart. Two figures are asserted against the arithmetic
they are supposed to support (Q10's "no losses in the first three years", Q15's
"light + heavy is double private") — if a value is ever mistyped the build fails
instead of shipping an item whose picture disagrees with its answer.
"""
import json, os, shutil
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Wedge, Rectangle

plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["DejaVu Serif"]

OUT = "figs_pc"
shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT)

NAVY = "#1F3864"; INK = "#222E2D"
BLUE = "#3B5BA9"; ORANGE = "#E8762C"; GREY = "#A6A6A6"; GOLD = "#F0B323"
PALE = "#D9D9D9"; GRID = "#DCE9E8"
idx = {}


def save(fig, name):
    p = os.path.join(OUT, name + ".png")
    fig.savefig(p, dpi=400, transparent=True, bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)
    from PIL import Image
    with Image.open(p) as im:
        idx[name] = {"file": p, "aspect": im.width / im.height}
    return p


def _clean(ax, ygrid=True):
    if ygrid:
        ax.grid(axis="y", color=GRID, lw=0.7); ax.set_axisbelow(True)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)


# ---------------------------------------------------------------- Q5
ACADEMIC = {"BIO": 80, "MATH": 40, "CHEMISTRY": 60, "GRAMMER": 70, "HISTORY": 50}


def academic():
    # the item asks which subject equals the mean of Math and Bio
    mean = (ACADEMIC["MATH"] + ACADEMIC["BIO"]) / 2
    match = [k for k, v in ACADEMIC.items() if v == mean]
    assert match == ["CHEMISTRY"], match
    fig, ax = plt.subplots(figsize=(3.9, 2.2))
    ax.bar(list(ACADEMIC), list(ACADEMIC.values()), color=BLUE, width=0.38)
    ax.set_ylim(0, 95); ax.set_yticks(range(0, 91, 10))
    ax.set_title("Academic subject results", fontsize=9, color=INK, pad=6)
    ax.tick_params(axis="x", labelsize=7.5); ax.tick_params(axis="y", labelsize=7.5)
    _clean(ax)
    return save(fig, "pc_academic")


# ---------------------------------------------------------------- Q6
# A clock face: twelve CONGRUENT sectors of 30 degrees, one shaded. The source
# scan leaves the dividers off the right-hand sectors, but the question states
# the sectors are congruent, so they are all drawn here.
def clock():
    fig, ax = plt.subplots(figsize=(2.3, 2.3))
    for i in range(12):
        a0 = 90 - 30 * (i + 1)
        fc = NAVY if i == 8 else PALE
        ax.add_patch(Wedge((0, 0), 1, a0, a0 + 30, fc=fc, ec="white", lw=1.6))
    ax.set_xlim(-1.1, 1.1); ax.set_ylim(-1.1, 1.1)
    ax.set_aspect("equal"); ax.axis("off")
    return save(fig, "pc_clock")


# ---------------------------------------------------------------- Q7
# Rhombus on a 10 x 10 grid, vertices at the midpoints of the four edges, so
# both diagonals are 10 and the area is 50 — readable straight off the squares.
def rhombus():
    fig, ax = plt.subplots(figsize=(2.6, 2.6))
    for i in range(11):
        ax.plot([0, 10], [i, i], color="#9AA6A5", lw=0.55)
        ax.plot([i, i], [0, 10], color="#9AA6A5", lw=0.55)
    ax.add_patch(Polygon(np.array([(5, 10), (10, 5), (5, 0), (0, 5)]),
                         closed=True, fill=False, ec=NAVY, lw=2.6))
    ax.set_xlim(-0.3, 10.3); ax.set_ylim(-0.3, 10.3)
    ax.set_aspect("equal"); ax.axis("off")
    return save(fig, "pc_rhombus")


# ---------------------------------------------------------------- Q10
INVEST = {"box 1": [-2, 11, 9, 5], "box 2": [10, 9, -4, 7],
          "box 3": [20, -2, 15, 12], "box 4": [7, 9, 3, -2]}
YEARS = ["2020", "2021", "2022", "2023"]


def invest():
    # "no losses over the FIRST THREE years" — box 4's loss is in 2023, outside
    # the window, and every other box dips inside it. That is the whole item.
    clean = [k for k, v in INVEST.items() if all(x >= 0 for x in v[:3])]
    assert clean == ["box 4"], clean
    assert INVEST["box 4"][3] < 0                     # the distractor's bait
    fig, ax = plt.subplots(figsize=(4.4, 2.3))
    x = np.arange(4); w = 0.2
    for i, (k, v) in enumerate(INVEST.items()):
        ax.bar(x + (i - 1.5) * w, v, w, label=k,
               color=[BLUE, ORANGE, GREY, GOLD][i])
    ax.axhline(0, color=INK, lw=0.9)
    ax.set_xticks(x); ax.set_xticklabels(YEARS, fontsize=9)
    ax.set_ylim(-10, 26); ax.set_yticks(range(-10, 26, 5))
    ax.tick_params(axis="y", labelsize=7.5)
    ax.legend(fontsize=7.5, ncol=4, frameon=False, loc="upper center",
              bbox_to_anchor=(0.5, 1.14))
    _clean(ax)
    return save(fig, "pc_invest")


# ---------------------------------------------------------------- Q11
QUARTERS = {"First quarter": [50, 40, 35], "Second quarter": [40, 30, 35],
            "Third quarter": [60, 30, 50], "Fourth quarter": [40, 45, 60]}


def scatter():
    assert sum(QUARTERS["Second quarter"]) / 3 == 35
    fig, ax = plt.subplots(figsize=(4.2, 2.3))
    for i, (k, vs) in enumerate(QUARTERS.items()):
        xs = [i + off for off in (-0.26, 0.0, 0.26)]
        ax.plot(xs, vs, "o", ms=8, mfc=BLUE, mec="#25407A", mew=0.9)
        if i:
            ax.axvline(i - 0.5, color="#C9D2D1", lw=0.8)
    ax.set_xticks(range(4))
    ax.set_xticklabels([k.replace(" ", "\n") for k in QUARTERS], fontsize=7.5)
    ax.set_xlim(-0.55, 3.55); ax.set_ylim(0, 72); ax.set_yticks(range(0, 71, 10))
    ax.tick_params(axis="y", labelsize=7.5)
    _clean(ax)
    return save(fig, "pc_scatter")


# ---------------------------------------------------------------- Q13
MONTHS = ["Muharram", "Safar", "Rabie Awal", "Rabie Thani", "Jumada Awal"]
MVALS = [2, 4, 10, 8, 6]


def months():
    assert (MVALS[2] - MVALS[1]) / MVALS[1] == 1.5      # 150 per cent
    fig, ax = plt.subplots(figsize=(4.2, 2.1))
    ax.plot(MONTHS, MVALS, "-o", color=ORANGE, lw=2.0, ms=6)
    ax.set_xticks(range(5))
    ax.set_xticklabels([m.replace(" ", "\n") for m in MONTHS], fontsize=7.5)
    ax.set_ylim(0, 13); ax.set_yticks(range(0, 13, 2))
    ax.tick_params(axis="y", labelsize=7.5)
    _clean(ax)
    return save(fig, "pc_months")


# ---------------------------------------------------------------- Q15
CARS = {"Light cars": [60, 50, 50, 60], "Heavy cars": [80, 30, 40, 30],
        "Private cars": [70, 70, 90, 40]}
DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday"]


def cars():
    hits = [DAYS[i] for i in range(4)
            if CARS["Light cars"][i] + CARS["Heavy cars"][i]
            == 2 * CARS["Private cars"][i]]
    assert hits == ["Sunday"], hits
    fig, ax = plt.subplots(figsize=(4.3, 2.3))
    x = np.arange(4); w = 0.24
    for i, (k, v) in enumerate(CARS.items()):
        ax.bar(x + (i - 1) * w, v, w, label=k, color=[BLUE, ORANGE, GREY][i])
    ax.set_xticks(x); ax.set_xticklabels(DAYS, fontsize=8.5)
    ax.set_ylim(0, 105); ax.set_yticks(range(0, 101, 10))
    ax.tick_params(axis="y", labelsize=7.5)
    ax.legend(fontsize=7.5, ncol=3, frameon=False, loc="upper center",
              bbox_to_anchor=(0.5, 1.15))
    _clean(ax)
    return save(fig, "pc_cars")


# ---------------------------------------------------------------- Q23b
# Right trapezoid: parallel sides 14 and 19, height 12. The slant closes a
# 5-12-13 triangle, so it is drawn with a horizontal run of exactly 5.
def trapezoid():
    run = 19 - 14
    assert run ** 2 + 12 ** 2 == 13 ** 2
    fig, ax = plt.subplots(figsize=(3.5, 1.8))
    pts = np.array([(0, 0), (19, 0), (19, 12), (run, 12)])
    ax.add_patch(Polygon(pts, closed=True, fill=False, ec=NAVY, lw=2.4))
    for (px, py) in ((19, 0), (19, 12)):                       # right angles
        d = 1.15
        ax.add_patch(Rectangle((px - d, py if py == 0 else py - d), d, d,
                               fill=False, ec=NAVY, lw=1.4))
    ax.annotate("19", (9.5, -1.9), fontsize=13, color=INK, ha="center")
    ax.annotate("14", ((run + 19) / 2, 13.3), fontsize=13, color=INK, ha="center")
    ax.annotate("12", (20.2, 6), fontsize=13, color=INK, va="center")
    ax.annotate(r"$x$", (0.4, 7.4), fontsize=14, color=INK, ha="right")
    ax.set_xlim(-2.6, 22.5); ax.set_ylim(-3.6, 15.4)
    ax.set_aspect("equal"); ax.axis("off")
    return save(fig, "pc_trapezoid")


# ---------------------------------------------------------------- Q24
# Equilateral triangle of side 12. L, R are the midpoints of the two slant
# sides, B the midpoint of the base, and T the midpoint of the median from the
# apex to B — which is also the midpoint of LR. The shaded piece is L-T-B, and
# it comes to exactly one eighth of the whole, 4.5*sqrt(3).
def tri_medial():
    s = 12.0
    A = np.array([s / 2, s * np.sqrt(3) / 2]); P = np.array([0.0, 0.0])
    Q = np.array([s, 0.0])
    L = (A + P) / 2; R = (A + Q) / 2; B = (P + Q) / 2; T = (A + B) / 2
    assert np.allclose(T, (L + R) / 2)                 # T is the midpoint of LR
    shaded = abs(np.cross(T - L, B - L)) / 2
    whole = np.sqrt(3) / 4 * s * s
    assert abs(shaded - 4.5 * np.sqrt(3)) < 1e-9, shaded
    assert abs(shaded / whole - 1 / 8) < 1e-12

    fig, ax = plt.subplots(figsize=(2.9, 2.5))
    ax.add_patch(Polygon(np.array([L, T, B]), closed=True, fc=BLUE, ec=BLUE))
    for a, b in ((L, T), (T, R), (R, B), (B, L), (A, B)):
        ax.plot([a[0], b[0]], [a[1], b[1]], color="#7A8A89", lw=0.9)
    ax.add_patch(Polygon(np.array([P, Q, A]), closed=True, fill=False,
                         ec=INK, lw=2.2))
    ax.annotate("12 cm", (s / 2, -1.15), fontsize=12, color=INK, ha="center")
    ax.set_xlim(-0.6, s + 0.6); ax.set_ylim(-2.2, s * np.sqrt(3) / 2 + 0.5)
    ax.set_aspect("equal"); ax.axis("off")
    return save(fig, "pc_tri_medial")


academic(); clock(); rhombus(); invest(); scatter()
months(); cars(); trapezoid(); tri_medial()
json.dump(idx, open(os.path.join(OUT, "_index.json"), "w"), indent=1)
print(len(idx), "figures ->", OUT)
