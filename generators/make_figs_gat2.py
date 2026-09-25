"""
Figures for the GAT worksheets, Weeks 3 and 5 (higher difficulty).
None of these shapes appears in Weeks 2 or 4.
House style: recessive grid, thin marks, direct labels, transparent PNG 400 dpi.
"""
import json, os, shutil
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, Rectangle, Wedge, Arc, Ellipse
import numpy as np

plt.rcParams.update({
    "mathtext.fontset": "cm", "font.family": "serif",
    "font.serif": ["DejaVu Serif"], "text.color": "#222E2D",
    "savefig.transparent": True,
})
OUT, DPI = "figs_gat2", 400
shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(OUT)
TEAL, TEAL_L, MAROON, INK, GRID = "#17A199", "#CFEBE8", "#AD2A22", "#222E2D", "#DCE9E8"
NAVY = "#1B3B6F"
idx = {}


def save(fig, name):
    p = os.path.join(OUT, name + ".png")
    fig.savefig(p, dpi=DPI, bbox_inches="tight", pad_inches=0.03)
    plt.close(fig)
    from PIL import Image
    im = Image.open(p)
    idx[name] = {"file": p, "w": im.width, "h": im.height, "aspect": im.width / im.height}


def blank(ax):
    ax.set_aspect("equal"); ax.axis("off")


def tick(ax, x0, y0, x1, y1, label, off=(0, 0), fs=8.5, ha="center", va="center"):
    ax.plot([x0, x1], [y0, y1], color=INK, lw=0.8)
    n = 0.09
    if x0 == x1:
        ax.plot([x0 - n, x0 + n], [y0, y0], color=INK, lw=0.8)
        ax.plot([x1 - n, x1 + n], [y1, y1], color=INK, lw=0.8)
    else:
        ax.plot([x0, x0], [y0 - n, y0 + n], color=INK, lw=0.8)
        ax.plot([x1, x1], [y1 - n, y1 + n], color=INK, lw=0.8)
    ax.text((x0 + x1) / 2 + off[0], (y0 + y1) / 2 + off[1], label,
            fontsize=fs, ha=ha, va=va)


# ===================================================================== WEEK 3
# w3f1 — a square with a quarter circle removed at each corner
fig, ax = plt.subplots(figsize=(2.5, 2.5))
s = 4.0
ax.add_patch(Rectangle((0, 0), s, s, facecolor=TEAL, edgecolor=INK, lw=1.2))
for cx, cy, t1, t2 in [(0, 0, 0, 90), (s, 0, 90, 180), (s, s, 180, 270), (0, s, 270, 360)]:
    ax.add_patch(Wedge((cx, cy), s / 2, t1, t2, facecolor="white", edgecolor=INK, lw=1.0))
tick(ax, 0, -0.45, s, -0.45, "4 cm", off=(0, -0.35))
ax.set_xlim(-0.35, s + 0.35); ax.set_ylim(-1.15, s + 0.3)
blank(ax)
save(fig, "w3f1")

# w3f2 — an irregular quadrilateral on a unit grid
fig, ax = plt.subplots(figsize=(2.8, 2.5))
for x in range(0, 9):
    ax.plot([x, x], [0, 7], color=GRID, lw=0.6, zorder=0)
for y in range(0, 8):
    ax.plot([0, 8], [y, y], color=GRID, lw=0.6, zorder=0)
quad = [(1, 1), (7, 2), (6, 6), (2, 5)]
ax.add_patch(Polygon(quad, closed=True, facecolor=TEAL_L, edgecolor=NAVY, lw=1.9))
for (x, y) in quad:
    ax.plot(x, y, "o", ms=3.0, color=NAVY)
ax.set_xlim(-0.3, 8.3); ax.set_ylim(-0.3, 7.3)
blank(ax)
save(fig, "w3f2")

# w3f3 — two similar right triangles
fig, ax = plt.subplots(figsize=(3.0, 2.0))
ax.add_patch(Polygon([(0, 0), (3, 0), (0, 2)], closed=True, facecolor=TEAL_L,
                     edgecolor=NAVY, lw=1.6))
ax.add_patch(Polygon([(4.6, 0), (11.2, 0), (4.6, 4.4)], closed=True, facecolor="white",
                     edgecolor=NAVY, lw=1.6))
tick(ax, 0, -0.42, 3, -0.42, "6", off=(0, -0.34))
ax.text(-0.35, 1.0, "4", fontsize=8.5, ha="right", va="center")
tick(ax, 4.6, -0.42, 11.2, -0.42, "9", off=(0, -0.34))
ax.text(4.25, 2.2, "$x$", fontsize=10, ha="right", va="center")
ax.set_xlim(-0.9, 11.6); ax.set_ylim(-1.25, 4.7)
blank(ax)
save(fig, "w3f3")

# w3f4 — an inscribed angle and the angle at the centre on the same arc
fig, ax = plt.subplots(figsize=(2.5, 2.5))
r = 2.0
ax.add_patch(Circle((0, 0), r, facecolor="white", edgecolor=INK, lw=1.2))
A_ = (r * np.cos(np.radians(215)), r * np.sin(np.radians(215)))
B_ = (r * np.cos(np.radians(325)), r * np.sin(np.radians(325)))
P_ = (r * np.cos(np.radians(80)),  r * np.sin(np.radians(80)))
for X in (A_, B_):
    ax.plot([0, X[0]], [0, X[1]], color=NAVY, lw=1.4)
    ax.plot([P_[0], X[0]], [P_[1], X[1]], color=MAROON, lw=1.3)
ax.plot(0, 0, "o", ms=3.0, color=INK)
ax.add_patch(Arc((0, 0), 1.05, 1.05, theta1=215, theta2=325, lw=1.0, color=NAVY))
ax.text(0.0, -0.95, "$y$", fontsize=10, ha="center", color=NAVY)
ax.text(P_[0] - 0.02, P_[1] - 0.52, "35°", fontsize=8.5, ha="center", color=MAROON)
for X, lab, dx, dy in [(A_, "A", -0.28, -0.16), (B_, "B", 0.22, -0.16), (P_, "P", 0.0, 0.24)]:
    ax.plot(X[0], X[1], "o", ms=3.0, color=INK)
    ax.text(X[0] + dx, X[1] + dy, lab, fontsize=9, ha="center")
ax.text(0.16, 0.06, "O", fontsize=9)
ax.set_xlim(-2.45, 2.45); ax.set_ylim(-2.45, 2.6)
blank(ax)
save(fig, "w3f4")

# w3f5 — a clock face reading half past three
fig, ax = plt.subplots(figsize=(2.4, 2.4))
ax.add_patch(Circle((0, 0), 1.0, facecolor="white", edgecolor=INK, lw=1.6))
for h in range(12):
    a = np.radians(90 - 30 * h)
    ax.plot([0.88 * np.cos(a), 0.97 * np.cos(a)], [0.88 * np.sin(a), 0.97 * np.sin(a)],
            color=INK, lw=1.1)
    ax.text(0.75 * np.cos(a), 0.75 * np.sin(a), str(12 if h == 0 else h),
            fontsize=7.5, ha="center", va="center")
# minute hand at 6, hour hand half way between 3 and 4
am = np.radians(90 - 180)
ah = np.radians(90 - 105)
ax.plot([0, 0.66 * np.cos(am)], [0, 0.66 * np.sin(am)], color=NAVY, lw=2.0,
        solid_capstyle="round")
ax.plot([0, 0.46 * np.cos(ah)], [0, 0.46 * np.sin(ah)], color=MAROON, lw=2.4,
        solid_capstyle="round")
ax.plot(0, 0, "o", ms=3.4, color=INK)
ax.set_xlim(-1.12, 1.12); ax.set_ylim(-1.12, 1.12)
blank(ax)
save(fig, "w3f5")

# ===================================================================== WEEK 5
# w5f1 — a uniform path around a rectangular garden
fig, ax = plt.subplots(figsize=(2.9, 2.1))
ax.add_patch(Rectangle((0, 0), 12, 8, facecolor=TEAL, edgecolor=INK, lw=1.2))
ax.add_patch(Rectangle((1, 1), 10, 6, facecolor="white", edgecolor=INK, lw=1.2))
tick(ax, 1, 8.75, 11, 8.75, "10 m", off=(0, 0.45))
ax.text(11.55, 4.0, "6 m", fontsize=8.5, ha="left", va="center")
ax.plot([11.05, 11.45], [1, 1], color=INK, lw=0.8)
ax.plot([11.05, 11.45], [7, 7], color=INK, lw=0.8)
ax.plot([11.25, 11.25], [1, 7], color=INK, lw=0.8)
ax.set_xlim(-0.4, 13.2); ax.set_ylim(-0.6, 9.9)
blank(ax)
save(fig, "w5f1")

# w5f2 — an L-shaped compound figure
fig, ax = plt.subplots(figsize=(2.6, 2.3))
L = [(0, 0), (10, 0), (10, 5), (6, 5), (6, 8), (0, 8)]
ax.add_patch(Polygon(L, closed=True, facecolor=TEAL_L, edgecolor=NAVY, lw=1.8))
tick(ax, 0, -0.55, 10, -0.55, "10 cm", off=(0, -0.5))
ax.text(-0.5, 4.0, "8 cm", fontsize=8.5, ha="right", va="center", rotation=90)
ax.plot([-0.25, -0.25], [0, 8], color=INK, lw=0.8)
tick(ax, 6.0, 8.5, 10.0, 8.5, "4 cm", off=(0, 0.45))
ax.text(10.45, 2.5, "5 cm", fontsize=8.5, ha="left", va="center", rotation=90)
ax.plot([10.25, 10.25], [0, 5], color=INK, lw=0.8)
ax.set_xlim(-1.5, 11.9); ax.set_ylim(-1.6, 9.5)
blank(ax)
save(fig, "w5f2")

# w5f3 — a growing matchstick pattern
fig, ax = plt.subplots(figsize=(3.2, 1.4))
def square(ax, x, y, s=1.0):
    for (a, b, c, d) in [(x, y, x + s, y), (x + s, y, x + s, y + s),
                         (x + s, y + s, x, y + s), (x, y + s, x, y)]:
        ax.plot([a, c], [b, d], color=NAVY, lw=1.8, solid_capstyle="round")
xoff = 0
for n in (1, 2, 3):
    for i in range(n):
        square(ax, xoff + i, 0)
    ax.text(xoff + n / 2, -0.55, f"Figure {n}", fontsize=8, ha="center")
    xoff += n + 1.1
ax.set_xlim(-0.3, xoff + 0.1); ax.set_ylim(-1.05, 1.3)
blank(ax)
save(fig, "w5f3")

# w5f4 — a cylinder with radius and height marked
fig, ax = plt.subplots(figsize=(2.0, 2.4))
r, h = 1.0, 2.6
ax.add_patch(Rectangle((-r, 0), 2 * r, h, facecolor="#A9CCE3", edgecolor="none"))
ax.add_patch(Ellipse((0, h), 2 * r, 0.62, facecolor="#D6EAF8", edgecolor=INK, lw=1.1))
ax.add_patch(Ellipse((0, 0), 2 * r, 0.62, facecolor="#A9CCE3", edgecolor=INK, lw=1.1))
ax.plot([-r, -r], [0, h], color=INK, lw=1.1)
ax.plot([r, r], [0, h], color=INK, lw=1.1)
ax.annotate("", xy=(0, h), xytext=(r, h), arrowprops=dict(arrowstyle="<->", lw=0.8, color=INK))
ax.text(r / 2, h + 0.28, "3 cm", fontsize=8.5, ha="center")
ax.plot([-r - 0.42, -r - 0.42], [0, h], color=INK, lw=0.8)
ax.plot([-r - 0.55, -r - 0.29], [0, 0], color=INK, lw=0.8)
ax.plot([-r - 0.55, -r - 0.29], [h, h], color=INK, lw=0.8)
ax.text(-r - 0.62, h / 2, "10 cm", fontsize=8.5, ha="right", va="center", rotation=90)
ax.set_xlim(-2.35, 1.5); ax.set_ylim(-0.55, h + 0.75)
blank(ax)
save(fig, "w5f4")

# w5f5 — an isosceles triangle with angles given in x
fig, ax = plt.subplots(figsize=(2.7, 2.0))
A_, B_, C_ = (0, 0), (4.4, 0), (2.2, 2.7)
ax.add_patch(Polygon([A_, B_, C_], closed=True, facecolor=TEAL_L, edgecolor=NAVY, lw=1.7))
ax.text(2.2, 2.12, "$4x$", fontsize=9.5, ha="center")
ax.text(0.78, 0.20, "$x+30$", fontsize=9, ha="center")
ax.text(3.62, 0.20, "$x+30$", fontsize=9, ha="center")
for (px, py) in (A_, B_):
    ax.plot(px, py, "o", ms=2.6, color=NAVY)
# equal-side marks
for (p, q) in ((A_, C_), (B_, C_)):
    mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
    dx, dy = q[0] - p[0], q[1] - p[1]
    L = np.hypot(dx, dy); nx, ny = -dy / L, dx / L
    ax.plot([mx - 0.12 * nx, mx + 0.12 * nx], [my - 0.12 * ny, my + 0.12 * ny],
            color=NAVY, lw=1.3)
ax.set_xlim(-0.4, 4.8); ax.set_ylim(-0.45, 3.1)
blank(ax)
save(fig, "w5f5")

json.dump(idx, open(os.path.join(OUT, "_index.json"), "w"), indent=1)
print(len(idx), "figures:", ", ".join(sorted(idx)))
