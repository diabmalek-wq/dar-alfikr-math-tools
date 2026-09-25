"""The three diagrams from GAT part 10, redrawn.

Every figure is constructed from the geometry the question states, not traced by
eye — the 40/60/80 triangles really are 40-60-80, and the divided rectangle
really is five equal columns on a 10 x 4 frame. House rule: when a figure
carries the question, the drawing has to be true or the item is broken.
"""
import json, os, shutil
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["DejaVu Serif"]

OUT = "figs_p10"
shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT)

NAVY = "#1F3864"; INK = "#222E2D"
RED = "#C62828"; BLUE = "#3B5BA9"
idx = {}


def save(fig, name):
    p = os.path.join(OUT, name + ".png")
    fig.savefig(p, dpi=400, transparent=True, bbox_inches="tight", pad_inches=0.04)
    plt.close(fig)
    from PIL import Image
    with Image.open(p) as im:
        idx[name] = {"file": p, "aspect": im.width / im.height}
    return p


# ---------------------------------------------------------------- Q33
# Perimeter 28 with height 4 forces length 10, so the frame is drawn 10 x 4
# and cut into five equal 2 x 4 columns — the answer is readable off the
# picture, which is the point of the item.
def rect5():
    fig, ax = plt.subplots(figsize=(4.0, 1.9))
    L, H = 10.0, 4.0
    ax.add_patch(plt.Rectangle((0, 0), L, H, fill=False, ec=NAVY, lw=2.6))
    for i in range(1, 5):
        ax.plot([i * L / 5, i * L / 5], [0, H], color=NAVY, lw=1.6)
    ax.annotate("4 cm", (-0.55, H / 2), rotation=90, ha="center", va="center",
                fontsize=18, color=INK)
    ax.set_xlim(-1.5, L + 0.4); ax.set_ylim(-0.5, H + 0.5)
    ax.set_aspect("equal"); ax.axis("off")
    return save(fig, "p10_rect5")


# ---------------------------------------------------------------- Q41
# Two similar triangles on one baseline. Base angles 40 and 60 are CONSTRUCTED,
# so the apex really is 80 and a student measuring the drawing is not misled.
def tri_similar():
    fig, ax = plt.subplots(figsize=(4.6, 1.95))
    b = 5.0
    t40, t60 = np.tan(np.radians(40)), np.tan(np.radians(60))
    ax_ = t60 * b / (t40 + t60)                 # apex x from the left vertex
    ay = t40 * ax_
    d = 2.6                                     # how far the second copy sits along

    for x0 in (0.0, d):
        pts = [(x0, 0), (x0 + ax_, ay), (x0 + b, 0)]
        ax.add_patch(Polygon(pts, closed=True, fill=False, ec=INK, lw=2.2))

    ax.annotate(r"$40^{\circ}$", (0.55, 0.22), fontsize=17, color=INK)
    ax.annotate(r"$60^{\circ}$", (d + b - 1.45, 0.22), fontsize=17, color=INK)
    ax.annotate(r"$x^{\circ}$", (d + ax_ - 0.58, ay - 0.80), fontsize=17, color=INK)

    ax.set_xlim(-0.4, d + b + 0.4); ax.set_ylim(-0.35, ay + 0.4)
    ax.set_aspect("equal"); ax.axis("off")
    return save(fig, "p10_tri2")


# ---------------------------------------------------------------- Q3
# Midpoints joined: four congruent triangles. The two BOTTOM CORNER triangles
# are shaded — checked against the source at 2.4x, because which two are shaded
# is the whole question.
def tri4():
    fig, ax = plt.subplots(figsize=(3.1, 2.7))
    A, B, C = np.array([0, 0]), np.array([6, 0]), np.array([3, 5.196])
    Mab, Mac, Mbc = (A + B) / 2, (A + C) / 2, (B + C) / 2

    for tri in ([A, Mab, Mac], [Mab, B, Mbc]):          # shaded corners
        ax.add_patch(Polygon(np.array(tri), closed=True, fc=BLUE, ec=RED, lw=1.8))
    for tri in ([Mac, Mbc, C], [Mac, Mab, Mbc]):        # white top and middle
        ax.add_patch(Polygon(np.array(tri), closed=True, fc="white", ec=RED, lw=1.8))
    ax.add_patch(Polygon(np.array([A, B, C]), closed=True, fill=False, ec=RED, lw=1.8))

    ax.set_xlim(-0.3, 6.3); ax.set_ylim(-0.3, 5.5)
    ax.set_aspect("equal"); ax.axis("off")
    return save(fig, "p10_tri4")


rect5(); tri_similar(); tri4()
json.dump(idx, open(os.path.join(OUT, "_index.json"), "w"), indent=1)
print(len(idx), "figures ->", OUT)
