"""The eight diagrams from Mr Tamer Elsawy's part-8 practice set, redrawn.

Same rule as part 10: every figure is CONSTRUCTED from the geometry or the data
the question states, never traced by eye. The 135 degree line in Q6 really is at
135 degrees, the 58 degree chords really are 58 degrees apart, and the star
regions carry exactly the seven stars that are on the original — because in Q21
and Q22 the count IS the question, so a star in the wrong region breaks the item.
"""
import json, os, shutil
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle, Rectangle

plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["DejaVu Serif"]

OUT = "figs_p8"
shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT)

NAVY = "#1F3864"; INK = "#222E2D"; RED = "#C62828"
BLUE = "#3B5BA9"; ORANGE = "#E8762C"; GREY = "#A6A6A6"
idx = {}


def save(fig, name):
    p = os.path.join(OUT, name + ".png")
    fig.savefig(p, dpi=400, transparent=True, bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)
    from PIL import Image
    with Image.open(p) as im:
        idx[name] = {"file": p, "aspect": im.width / im.height}
    return p


# ---------------------------------------------------------------- Q6
# Circle centre M, horizontal diameter, a TANGENT at each end of it, and a line
# through M at 135 degrees to the leftward ray. Each shaded piece is a right
# triangle with legs r and r, so the pair comes to r squared exactly — which is
# why the radius is given as 2*sqrt(2) and the answer is 8.
def circle135():
    fig, ax = plt.subplots(figsize=(2.9, 2.6))
    r = 1.0
    ax.add_patch(Circle((0, 0), r, fill=False, ec=INK, lw=1.7))
    ax.plot([-r, r], [0, 0], color=INK, lw=1.7)                 # diameter
    ax.plot([-r, r], [-r, r], color=INK, lw=1.7)                # the 135 line

    for tri in ([(0, 0), (r, 0), (r, r)], [(0, 0), (-r, 0), (-r, -r)]):
        ax.add_patch(Polygon(np.array(tri), closed=True, fc=BLUE, ec=BLUE, alpha=0.85))
    # tangent segments, drawn so the right angle is visible as a real corner
    ax.plot([r, r], [0, r], color=INK, lw=1.7)
    ax.plot([-r, -r], [0, -r], color=INK, lw=1.7)
    for (x, s) in ((r, 1), (-r, -1)):                            # right-angle marks
        d = 0.11
        ax.add_patch(Rectangle((x - s * d, 0 if s > 0 else -d), s * d, d,
                               fc=INK, ec=INK))
    ax.annotate(r"$135^{\circ}$", (-0.50, 0.10), fontsize=15, color=INK)
    ax.annotate("M", (0.04, -0.19), fontsize=15, color=INK)
    ax.set_xlim(-1.3, 1.35); ax.set_ylim(-1.3, 1.3)
    ax.set_aspect("equal"); ax.axis("off")
    return save(fig, "p8_circle135")


# ---------------------------------------------------------------- Q21 and Q22
# Three overlapping rectangles and seven stars. Membership, read off the source
# at 3.6x:  A holds 5,  B holds 4,  C holds 4,  B and C together hold 2,
# B or C together hold 6. Both items use this ONE picture.
BOXES = {"A": (3.48, 0.80, 6.08, 5.32),        # x0, y0, x1, y1
         "B": (4.70, 1.05, 8.40, 4.70),
         "C": (2.85, 0.35, 6.55, 3.38)}
STARS = [(4.10, 4.25), (4.10, 2.80), (5.45, 2.80), (4.10, 1.65),
         (5.45, 1.70), (7.20, 3.25), (7.20, 2.42)]


def _inside(p, b):
    return b[0] < p[0] < b[2] and b[1] < p[1] < b[3]


def stars():
    counts = {k: sum(_inside(s, b) for s in STARS) for k, b in BOXES.items()}
    both = sum(_inside(s, BOXES["B"]) and _inside(s, BOXES["C"]) for s in STARS)
    either = sum(_inside(s, BOXES["B"]) or _inside(s, BOXES["C"]) for s in STARS)
    assert counts == {"A": 5, "B": 4, "C": 4}, counts
    assert (both, either) == (2, 6), (both, either)

    fig, ax = plt.subplots(figsize=(3.0, 2.35))
    lab = {"A": (-0.32, 0.18), "B": (0.18, 0.16), "C": (-0.95, 0.30)}
    for k, (x0, y0, x1, y1) in BOXES.items():
        ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0,
                               fill=False, ec=NAVY, lw=2.2))
        dx, dy = lab[k]
        ax.annotate(k, (x1 if dx > 0 else x0, y1 if dy > 0 else y0),
                    xytext=(dx, dy), textcoords="offset fontsize",
                    fontsize=13, color=INK)
    ax.plot([s[0] for s in STARS], [s[1] for s in STARS], marker="*",
            ls="none", ms=17, mfc=RED, mec="#7B1010", mew=0.8)
    ax.set_xlim(2.4, 9.0); ax.set_ylim(0.0, 5.8)
    ax.set_aspect("equal"); ax.axis("off")
    return save(fig, "p8_stars")


# ---------------------------------------------------------------- Q27
# Two DIAMETERS crossing at the centre M, 58 degrees apart. Placing H at 160
# and A at 38 makes arc ACD = 58 and arc ABH = 122 — the comparison is decided
# by construction, not by how the picture happens to look.
def circle58():
    fig, ax = plt.subplots(figsize=(2.7, 2.7))
    ax.add_patch(Circle((0, 0), 1, fill=False, ec=NAVY, lw=1.9))
    ang = {"H": 160, "A": 38, "B": 75, "C": 0, "D": 340}
    for a in (160, 38):                                   # the two diameters
        t = np.radians(a)
        ax.plot([np.cos(t), -np.cos(t)], [np.sin(t), -np.sin(t)], color=INK, lw=1.5)
    for k, a in ang.items():
        t = np.radians(a)
        ax.annotate(k, (1.14 * np.cos(t), 1.14 * np.sin(t)), fontsize=13,
                    color=INK, ha="center", va="center")
    ax.plot([np.cos(np.radians(0))], [0], marker="o", ms=6, color=NAVY)
    ax.annotate(r"$58^{\circ}$", (-0.60, -0.10), fontsize=13, color=INK)
    ax.annotate("M", (0.05, -0.17), fontsize=13, color=INK)
    ax.set_xlim(-1.35, 1.35); ax.set_ylim(-1.35, 1.35)
    ax.set_aspect("equal"); ax.axis("off")
    return save(fig, "p8_circle58")


# ---------------------------------------------------------------- Q35
def hajj():
    fig, ax = plt.subplots(figsize=(3.5, 2.1))
    yrs = ["1418", "1419", "1420", "1421"]
    vals = [1000000, 1000000, 1200000, 1050000]
    ax.bar(yrs, vals, color=ORANGE, width=0.42)
    ax.set_ylim(0, 1400000)
    ax.set_yticks(range(0, 1400001, 200000))
    ax.set_yticklabels([f"{v:,}".replace(",", " ") for v in range(0, 1400001, 200000)],
                       fontsize=7)
    ax.set_title("Hajj pilgrims coming from abroad", fontsize=9, color=INK, pad=7)
    ax.tick_params(axis="x", labelsize=9)
    ax.grid(axis="y", color="#DCE9E8", lw=0.7)
    ax.set_axisbelow(True)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    return save(fig, "p8_hajj")


# ---------------------------------------------------------------- Q38
def twocols():
    fig, ax = plt.subplots(figsize=(3.1, 2.1))
    ax.bar(["First column", "Second column"], [600, 200], color=BLUE, width=0.38)
    ax.set_ylim(0, 650); ax.set_yticks(range(0, 601, 100))
    ax.tick_params(labelsize=8)
    ax.grid(axis="y", color="#DCE9E8", lw=0.7); ax.set_axisbelow(True)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    return save(fig, "p8_twocols")


# ---------------------------------------------------------------- Q53
# a c e g along the top, b d f h along the bottom. c is the midpoint of ag and
# d the midpoint of bh, so with ce = 3k and eg = k the drawing is 0, 4, 7, 8 —
# and the ratio asked for reads straight off it.
def rect_abgh():
    fig, ax = plt.subplots(figsize=(3.6, 1.35))
    W, H = 8.0, 2.0
    ax.add_patch(Rectangle((0, 0), W, H, fill=False, ec=NAVY, lw=2.3))
    for x in (4.0, 7.0):
        ax.plot([x, x], [0, H], color=NAVY, lw=1.7)
    for x, top, bot in ((0, "a", "b"), (4.0, "c", "d"), (7.0, "e", "f"), (8.0, "g", "h")):
        ax.annotate(top, (x + (-0.16 if top == "e" else 0.16 if top == "g" else 0),
                        H + 0.16), fontsize=12, color=INK, ha="center")
        ax.annotate(bot, (x + (-0.16 if bot == "f" else 0.16 if bot == "h" else 0),
                        -0.62), fontsize=12, color=INK, ha="center")
    ax.set_xlim(-0.5, 8.5); ax.set_ylim(-0.9, 2.7)
    ax.set_aspect("equal"); ax.axis("off")
    return save(fig, "p8_rect_abgh")


# ---------------------------------------------------------------- last item
def traffic():
    days = ["Saturday", "Sunday", "Monday", "Tuesday"]
    data = {"private": [80, 70, 100, 50], "light trucks": [90, 60, 70, 50],
            "heavy trucks": [70, 90, 100, 70]}
    fig, ax = plt.subplots(figsize=(4.3, 2.2))
    x = np.arange(4); w = 0.26
    for i, (k, v) in enumerate(data.items()):
        b = ax.bar(x + (i - 1) * w, v, w, label=k,
                   color=[BLUE, ORANGE, GREY][i])
        ax.bar_label(b, fontsize=7, padding=1)
    ax.set_xticks(x); ax.set_xticklabels(days, fontsize=9)
    ax.set_ylim(0, 125); ax.set_yticks([])
    ax.legend(fontsize=7.5, ncol=3, frameon=False, loc="upper center",
              bbox_to_anchor=(0.5, 1.16))
    for sp in ("top", "right", "left"):
        ax.spines[sp].set_visible(False)
    return save(fig, "p8_traffic")


circle135(); stars(); circle58(); hajj(); twocols(); rect_abgh(); traffic()
json.dump(idx, open(os.path.join(OUT, "_index.json"), "w"), indent=1)
print(len(idx), "figures ->", OUT)
