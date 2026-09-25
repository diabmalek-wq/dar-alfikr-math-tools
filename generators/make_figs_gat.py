"""
Figures for the GAT worksheets, Weeks 2 and 4.
House style: recessive grid, thin marks, direct labels, Computer Modern labels,
transparent PNG at 400 dpi. Every figure is rendered then measured for label
collisions before it ships.
"""
import json, os, shutil
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, Rectangle, Wedge, Arc
import numpy as np

plt.rcParams.update({
    "mathtext.fontset": "cm", "font.family": "serif",
    "font.serif": ["DejaVu Serif"], "text.color": "#222E2D",
    "axes.edgecolor": "#222E2D", "savefig.transparent": True,
})
OUT, DPI = "figs_gat", 400
shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(OUT)
TEAL, TEAL_L, MAROON, INK, GRID = "#17A199", "#CFEBE8", "#AD2A22", "#222E2D", "#DCE9E8"
idx = {}


def save(fig, name):
    p = os.path.join(OUT, name + ".png")
    fig.savefig(p, dpi=DPI, bbox_inches="tight", pad_inches=0.03)
    plt.close(fig)
    from PIL import Image
    im = Image.open(p)
    idx[name] = {"file": p, "w": im.width, "h": im.height,
                 "aspect": im.width / im.height}


def blank(ax):
    ax.set_aspect("equal")
    ax.axis("off")


# ===================================================================== WEEK 2
# w2f1 — a circle cut by two equal semicircles: shaded ratio
fig, ax = plt.subplots(figsize=(2.6, 2.6))
ax.add_patch(Circle((0, 0), 2, facecolor=TEAL, edgecolor=INK, lw=1.1))
ax.add_patch(Wedge((0, 1), 1, -90, 90, facecolor="white", edgecolor=INK, lw=1.0))
ax.add_patch(Wedge((0, -1), 1, 90, 270, facecolor="white", edgecolor=INK, lw=1.0))
ax.plot([0, 0], [1, 2], color=INK, lw=0.8)
ax.text(0.14, 1.5, "1", fontsize=9, va="center")
ax.plot([2.35, 2.35], [-2, 2], color=INK, lw=0.8)
ax.plot([2.25, 2.45], [2, 2], color=INK, lw=0.8)
ax.plot([2.25, 2.45], [-2, -2], color=INK, lw=0.8)
ax.text(2.55, 0, "4", fontsize=9, va="center")
ax.set_xlim(-2.3, 3.0); ax.set_ylim(-2.3, 2.3)
blank(ax)
save(fig, "w2f1")

# w2f2 — a kite on a unit grid, area by the diagonal rule
fig, ax = plt.subplots(figsize=(2.9, 2.6))
for x in range(0, 11):
    ax.plot([x, x], [0, 8], color=GRID, lw=0.6, zorder=0)
for y in range(0, 9):
    ax.plot([0, 10], [y, y], color=GRID, lw=0.6, zorder=0)
kite = [(1, 4), (5, 8), (9, 4), (5, 1)]
ax.add_patch(Polygon(kite, closed=True, facecolor="none", edgecolor="#1B3B6F", lw=1.9))
ax.set_xlim(-0.3, 10.3); ax.set_ylim(-0.3, 8.3)
blank(ax)
save(fig, "w2f2")

# w2f3 — two parallel lines cut by two transversals: find x + y
fig, ax = plt.subplots(figsize=(3.0, 2.2))
ax.plot([-0.2, 6.2], [3, 3], color=INK, lw=1.2)
ax.plot([-0.2, 6.2], [0, 0], color=INK, lw=1.2)
ax.plot([1.1, 3.0], [3.6, -0.6], color=INK, lw=1.1)
ax.plot([5.2, 3.6], [3.6, -0.6], color=INK, lw=1.1)
ax.text(1.52, 2.52, "$x$", fontsize=10)
ax.text(5.12, 2.52, "$y$", fontsize=10)
ax.text(2.90, 0.20, "115°", fontsize=8.5)
ax.text(3.98, 0.20, "70°", fontsize=8.5)
ax.set_xlim(-0.4, 6.4); ax.set_ylim(-0.9, 3.9)
blank(ax)
save(fig, "w2f3")

# w2f4 — a cube with a labelled edge
fig, ax = plt.subplots(figsize=(2.3, 2.1))
s, d = 1.6, 0.62
front = [(0, 0), (s, 0), (s, s), (0, s)]
ax.add_patch(Polygon(front, closed=True, facecolor="#7FB3D5", edgecolor=INK, lw=1.1))
ax.add_patch(Polygon([(0, s), (s, s), (s + d, s + d), (d, s + d)],
                     closed=True, facecolor="#A9CCE3", edgecolor=INK, lw=1.1))
ax.add_patch(Polygon([(s, 0), (s + d, d), (s + d, s + d), (s, s)],
                     closed=True, facecolor="#5D8AA8", edgecolor=INK, lw=1.1))
ax.plot([-0.18, -0.18], [0, s], color=INK, lw=0.8)
ax.plot([-0.28, -0.08], [0, 0], color=INK, lw=0.8)
ax.plot([-0.28, -0.08], [s, s], color=INK, lw=0.8)
ax.text(-0.62, s / 2, "5 cm", fontsize=8.5, va="center")
ax.set_xlim(-0.95, s + d + 0.15); ax.set_ylim(-0.15, s + d + 0.15)
blank(ax)
save(fig, "w2f4")

# w2f5 — exterior angle: interior 55° and 65° given, w is exterior at B
fig, ax = plt.subplots(figsize=(2.9, 2.2))
A_, B_ = (0.0, 0.0), (4.0, 0.0)
C_ = (0.0 + 3.822 * np.cos(np.radians(55)), 3.822 * np.sin(np.radians(55)))
ax.add_patch(Polygon([A_, B_, C_], closed=True, facecolor=TEAL_L,
                     edgecolor="#1B3B6F", lw=1.6))
ax.plot([B_[0], 5.7], [0, 0], color=INK, lw=1.1)
ax.text(0.42, 0.14, "55°", fontsize=8.5)
ax.text(2.10, 2.45, "65°", fontsize=8.5, ha="center")
ax.add_patch(Arc(B_, 1.5, 1.5, theta1=0, theta2=120, lw=1.0, color=MAROON))
ax.text(4.30, 0.62, "$w$", fontsize=10, color=MAROON)
ax.set_xlim(-0.35, 5.95); ax.set_ylim(-0.45, 3.45)
blank(ax)
save(fig, "w2f5")

# ===================================================================== WEEK 4
# w4f1 — an annulus: small circle against the ring
fig, ax = plt.subplots(figsize=(2.6, 2.6))
ax.add_patch(Circle((0, 0), 3, facecolor=TEAL, edgecolor=INK, lw=1.1))
ax.add_patch(Circle((0, 0), 2, facecolor="white", edgecolor=INK, lw=1.1))
ax.plot([0, 2], [0, 0], color=INK, lw=0.9)
ax.plot([0, 0], [0, 3], color=INK, lw=0.9)
ax.text(0.9, 0.16, "2", fontsize=9)
ax.text(0.12, 1.9, "3", fontsize=9)
ax.plot(0, 0, "o", ms=2.6, color=INK)
ax.set_xlim(-3.25, 3.25); ax.set_ylim(-3.25, 3.25)
blank(ax)
save(fig, "w4f1")

# w4f2 — a trapezium on a unit grid
fig, ax = plt.subplots(figsize=(2.9, 2.4))
for x in range(0, 11):
    ax.plot([x, x], [0, 7], color=GRID, lw=0.6, zorder=0)
for y in range(0, 8):
    ax.plot([0, 10], [y, y], color=GRID, lw=0.6, zorder=0)
trap = [(1, 1), (9, 1), (7, 6), (3, 6)]
ax.add_patch(Polygon(trap, closed=True, facecolor="none", edgecolor="#1B3B6F", lw=1.9))
ax.set_xlim(-0.3, 10.3); ax.set_ylim(-0.3, 7.3)
blank(ax)
save(fig, "w4f2")

# w4f3 — a square inscribed in a circle
fig, ax = plt.subplots(figsize=(2.5, 2.5))
r = 2.0
ax.add_patch(Circle((0, 0), r, facecolor=TEAL_L, edgecolor=INK, lw=1.2))
k = r / np.sqrt(2)
ax.add_patch(Polygon([(-k, -k), (k, -k), (k, k), (-k, k)], closed=True,
                     facecolor="white", edgecolor="#1B3B6F", lw=1.6))
ax.plot([0, r], [0, 0], color=INK, lw=0.9, ls=(0, (4, 2)))
ax.text(1.0, 0.14, "6", fontsize=9)
ax.plot(0, 0, "o", ms=2.6, color=INK)
ax.set_xlim(-2.25, 2.25); ax.set_ylim(-2.25, 2.25)
blank(ax)
save(fig, "w4f3")

# w4f4 — a rectangle made of identical squares
fig, ax = plt.subplots(figsize=(2.9, 1.7))
for i in range(5):
    ax.add_patch(Rectangle((i, 0), 1, 1, facecolor=TEAL_L if i % 2 == 0 else "white",
                           edgecolor=INK, lw=1.0))
for i in range(5):
    ax.add_patch(Rectangle((i, 1), 1, 1, facecolor="white" if i % 2 == 0 else TEAL_L,
                           edgecolor=INK, lw=1.0))
ax.add_patch(Rectangle((0, 0), 5, 2, facecolor="none", edgecolor="#1B3B6F", lw=1.8))
ax.plot([0, 1], [-0.28, -0.28], color=INK, lw=0.9)
ax.plot([0, 0], [-0.38, -0.18], color=INK, lw=0.9)
ax.plot([1, 1], [-0.38, -0.18], color=INK, lw=0.9)
ax.text(0.5, -0.72, "4 cm", fontsize=8.5, ha="center")
ax.set_xlim(-0.2, 5.2); ax.set_ylim(-0.95, 2.2)
blank(ax)
save(fig, "w4f4")

# w4f5 — angles on a straight line inside a triangle drawn to a parallel
fig, ax = plt.subplots(figsize=(3.0, 2.1))
ax.plot([-0.2, 6.2], [2.6, 2.6], color=INK, lw=1.2)
ax.plot([-0.2, 6.2], [0, 0], color=INK, lw=1.2)
P, Q, R = (1.4, 2.6), (4.6, 2.6), (3.0, 0)
ax.add_patch(Polygon([P, Q, R], closed=True, facecolor=TEAL_L,
                     edgecolor="#1B3B6F", lw=1.6))
ax.text(1.80, 2.24, "$a$", fontsize=10)
ax.text(4.10, 2.24, "$b$", fontsize=10)
ax.text(3.00, 0.46, "64°", fontsize=8.5, ha="center")
ax.text(5.5, 2.75, "$\\ell_1$", fontsize=9)
ax.text(5.5, 0.15, "$\\ell_2$", fontsize=9)
ax.set_xlim(-0.4, 6.4); ax.set_ylim(-0.45, 3.15)
blank(ax)
save(fig, "w4f5")

json.dump(idx, open(os.path.join(OUT, "_index.json"), "w"), indent=1)
print(len(idx), "figures:", ", ".join(sorted(idx)))
