"""Diagrams for the Grade 10 and Grade 11 Week 4 SAT worksheets.

Six figures, one per item that reads better with a picture: two Grade 10
SAT geometry items (Law of Cosines triangle, similar-triangle shadows),
two Grade 10 GAT geometry items (angles on a line, circle in a square),
and two Grade 11 SAT algebra items (a parallel-line pair, an intersecting
line pair) shown on a coordinate plane. Every number drawn matches the
worksheet's own numbers exactly.

    python3 make_figs_w4.py        # writes into figs_w4/ and its _index.json
"""
import json, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Arc, Rectangle, Circle
from PIL import Image

plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["DejaVu Serif"]

OUT = "figs_w4"
os.makedirs(OUT, exist_ok=True)

NAVY = "#1F3864"; INK = "#222E2D"; TEAL = "#17A199"; GREY = "#A6A6A6"
GRID = "#DCE9E8"; MAROON = "#9E2A2B"

idx = {}


def save(fig, name):
    p = os.path.join(OUT, name + ".png")
    fig.savefig(p, dpi=400, transparent=True, bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)
    with Image.open(p) as im:
        idx[name] = {"file": p.replace(os.sep, "/"), "aspect": im.width / im.height}
    print("wrote", p)


# --------------------------------------------------------------- G10 SAT-GEO.1
# Law of Cosines: sides 80 m and 95 m with a 62 degree included angle.
def geo1_triangle(name):
    fig, ax = plt.subplots(figsize=(2.6, 2.2))
    A = np.array([0.0, 0.0])
    deg = 62.0
    B = A + 3.2 * np.array([np.cos(np.radians(deg)), np.sin(np.radians(deg))])  # side 80
    C = A + 3.9 * np.array([1.0, 0.0])                                          # side 95
    ax.add_patch(Polygon([A, B, C], closed=True, fill=False, edgecolor=NAVY, lw=1.8))
    ax.plot(*zip(A, B), color=NAVY, lw=1.8)
    ax.plot(*zip(A, C), color=NAVY, lw=1.8)
    ax.plot(*zip(B, C), color=TEAL, lw=1.8, ls=(0, (4, 3)))
    arc = Arc(A, 0.9, 0.9, angle=0, theta1=0, theta2=deg, color=MAROON, lw=1.4)
    ax.add_patch(arc)
    mid = A + 0.58 * np.array([np.cos(np.radians(deg / 2)), np.sin(np.radians(deg / 2))])
    ax.text(*mid, r"$62^\circ$", fontsize=10, color=MAROON, ha="left", va="bottom")
    ax.text(*(A + B) / 2 + np.array([-0.32, 0.05]), "80 m", fontsize=10, color=INK,
            ha="right", va="center", rotation=deg, rotation_mode="anchor")
    ax.text(*(A + C) / 2, "95 m", fontsize=10, color=INK, ha="center", va="top")
    ax.text(*(B + C) / 2 + np.array([0.15, 0.05]), "?", fontsize=12, color=TEAL,
            ha="left", va="center", fontweight="bold")
    ax.set_xlim(-0.6, 4.4); ax.set_ylim(-0.6, 3.4)
    ax.set_aspect("equal"); ax.axis("off")
    save(fig, name)


# --------------------------------------------------------------- G10 SAT-GEO.2
# Similar triangles: pole 2.4 m / shadow 3.2 m, tower ? / shadow 52 m (drawn
# compressed since the real ratio would make the tower panel absurdly wide).
def geo2_shadows(name):
    fig, ax = plt.subplots(figsize=(3.1, 1.7))
    # pole triangle
    p0 = np.array([0.0, 0.0])
    ax.plot([p0[0], p0[0]], [0, 0.9], color=NAVY, lw=2.2)                     # pole
    ax.plot([p0[0], p0[0] + 1.2], [0, 0], color=GREY, lw=1.6)                 # shadow
    ax.plot([p0[0], p0[0] + 1.2], [0.9, 0], color=MAROON, lw=1.3, ls=(0, (3, 2)))  # sun ray
    ax.text(p0[0] - 0.12, 0.45, "2.4 m", fontsize=9, color=INK, ha="right", va="center")
    ax.text(p0[0] + 0.6, -0.16, "3.2 m", fontsize=9, color=INK, ha="center", va="top")
    # tower triangle (same angle, longer shadow — drawn to a smaller scale)
    t0 = np.array([2.6, 0.0])
    ax.plot([t0[0], t0[0]], [0, 1.9], color=NAVY, lw=2.2)                     # tower
    ax.plot([t0[0], t0[0] + 3.1], [0, 0], color=GREY, lw=1.6)                 # shadow
    ax.plot([t0[0], t0[0] + 3.1], [1.9, 0], color=MAROON, lw=1.3, ls=(0, (3, 2)))  # sun ray
    ax.text(t0[0] - 0.12, 0.95, "? m", fontsize=10, color=TEAL, ha="right", va="center", fontweight="bold")
    ax.text(t0[0] + 1.55, -0.16, "52 m (shadow)", fontsize=9, color=INK, ha="center", va="top")
    ax.plot([0, 5.9], [0, 0], color=GREY, lw=0.8)  # ground line
    ax.set_xlim(-0.7, 6.1); ax.set_ylim(-0.5, 2.3)
    ax.set_aspect("equal"); ax.axis("off")
    save(fig, name)


# --------------------------------------------------------------- G10 GAT-Q-GEO.1
# Three angles on a straight line: 3x, 2x+10, 4x-10 (with x = 20).
def gat_angles(name):
    fig, ax = plt.subplots(figsize=(4.2, 2.1))
    O = np.array([0.0, 0.0])
    ax.plot([-3.4, 3.4], [0, 0], color=GREY, lw=1.2)
    x = 20.0
    a1, a2, a3 = 3 * x, 2 * x + 10, 4 * x - 10   # 60, 50, 70 -> sum 180
    starts = [0.0, a1, a1 + a2]
    labels = ["3x", "2x + 10", "4x − 10"]
    label_r = [1.55, 1.85, 1.55]
    ha_for = ["left", "center", "right"]
    R = 1.05
    for s, a in zip(starts[1:], [a2, a3]):
        ray = np.array([3.0 * np.cos(np.radians(s)), 3.0 * np.sin(np.radians(s))])
        ax.plot([0, ray[0]], [0, ray[1]], color=NAVY, lw=1.4)
    for s, a, lab, lr, ha in zip(starts, [a1, a2, a3], labels, label_r, ha_for):
        arc = Arc(O, R * 2, R * 2, angle=0, theta1=s, theta2=s + a, color=NAVY, lw=1.2)
        ax.add_patch(arc)
        mid = np.radians(s + a / 2)
        ax.text(lr * np.cos(mid), lr * np.sin(mid) + 0.12, lab, fontsize=10.5, color=INK,
                ha=ha, va="bottom")
    ax.set_xlim(-3.4, 3.4); ax.set_ylim(-0.35, 2.6)
    ax.set_aspect("equal"); ax.axis("off")
    save(fig, name)


# --------------------------------------------------------------- G10 GAT-Q-GEO.3
# A circle of radius 6 cm inscribed in a square.
def gat_circle_square(name):
    fig, ax = plt.subplots(figsize=(1.9, 1.9))
    s = 12.0
    ax.add_patch(Rectangle((0, 0), s, s, fill=False, edgecolor=NAVY, lw=1.8))
    ax.add_patch(Circle((s / 2, s / 2), s / 2, fill=False, edgecolor=TEAL, lw=1.8))
    ax.plot([s / 2, s], [s / 2, s / 2], color=MAROON, lw=1.2, ls=(0, (3, 2)))
    ax.text(s * 0.75, s / 2 + 0.5, "6 cm", fontsize=9.5, color=MAROON, ha="center", va="bottom")
    ax.set_xlim(-0.8, s + 0.8); ax.set_ylim(-0.8, s + 0.8)
    ax.set_aspect("equal"); ax.axis("off")
    save(fig, name)


# --------------------------------------------------------------- shared axes helper
def axes2d(ax, xlim, ylim, step=1):
    for x in np.arange(np.ceil(xlim[0]), xlim[1] + 1e-9, step):
        ax.plot([x, x], list(ylim), color=GRID, lw=0.6, zorder=0)
    for y in np.arange(np.ceil(ylim[0]), ylim[1] + 1e-9, step):
        ax.plot(list(xlim), [y, y], color=GRID, lw=0.6, zorder=0)
    ax.annotate("", xy=(xlim[1], 0), xytext=(xlim[0], 0),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.1, mutation_scale=9))
    ax.annotate("", xy=(0, ylim[1]), xytext=(0, ylim[0]),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.1, mutation_scale=9))
    ax.text(xlim[1] - 0.1, -0.55, "$x$", ha="right", va="top", fontsize=10, color=INK)
    ax.text(-0.55, ylim[1] + 0.05, "$y$", ha="right", va="bottom", fontsize=10, color=INK)


# --------------------------------------------------------------- G11 SAT-ALG.2
# y = -2x + 7 and the parallel line y = -2x + 13 through (4, 5).
def alg2_parallel(name):
    fig, ax = plt.subplots(figsize=(2.6, 2.6))
    xlim, ylim = (-1.5, 7.5), (-1.5, 14.5)
    axes2d(ax, xlim, ylim, step=2)
    xs = np.linspace(xlim[0], xlim[1], 2)
    ax.plot(xs, -2 * xs + 7, color=NAVY, lw=1.8)
    ax.plot(xs, -2 * xs + 13, color=TEAL, lw=1.8)
    ax.plot([4], [5], marker="o", ms=4.5, color=MAROON, zorder=5)
    ax.text(4.25, 5.1, "(4, 5)", fontsize=9, color=MAROON, ha="left", va="bottom")
    ax.text(0.3, -2 * 0.3 + 7 + 0.5, r"$y=-2x+7$", fontsize=9.5, color=NAVY, ha="left", va="bottom")
    ax.text(5.9, -2 * 5.9 + 13 + 0.5, r"$k$", fontsize=11, color=TEAL, ha="left", va="bottom", fontweight="bold")
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    ax.set_aspect("auto"); ax.axis("off")
    save(fig, name)


# --------------------------------------------------------------- G11 SAT-ALG.3
# 3x + y = 15 and x - 2y = -2, intersecting at (4, 3).
def alg3_intersect(name):
    fig, ax = plt.subplots(figsize=(2.6, 2.6))
    xlim, ylim = (-1.5, 7.5), (-1.5, 16.5)
    axes2d(ax, xlim, ylim, step=2)
    xs = np.linspace(xlim[0], xlim[1], 2)
    ax.plot(xs, 15 - 3 * xs, color=NAVY, lw=1.8)
    ax.plot(xs, (xs + 2) / 2, color=TEAL, lw=1.8)
    ax.plot([4], [3], marker="o", ms=4.5, color=MAROON, zorder=5)
    ax.text(4.25, 3.3, "(x, y)", fontsize=9, color=MAROON, ha="left", va="bottom")
    ax.text(1.0, 15 - 3 * 1.0 + 0.5, r"$3x+y=15$", fontsize=9, color=NAVY, ha="left")
    ax.text(5.4, (5.4 + 2) / 2 - 1.0, r"$x-2y=-2$", fontsize=9, color=TEAL, ha="left")
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    ax.set_aspect("auto"); ax.axis("off")
    save(fig, name)


geo1_triangle("g10_geo1_tri")
geo2_shadows("g10_geo2_shadow")
gat_angles("g10_gat_angles")
gat_circle_square("g10_gat_circle")
alg2_parallel("g11_alg2_parallel")
alg3_intersect("g11_alg3_intersect")

with open(os.path.join(OUT, "_index.json"), "w") as f:
    json.dump(idx, f, indent=1)
print("index written with", len(idx), "entries")
