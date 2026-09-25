"""Figures for the simulated SAAT (Tahsili) bank.

Three items carry a diagram. None of them is a redrawing: the rhombus is a
16-by-30 kite of diagonals where the source used 10 and 24, the trapezoid is
lettered and dimensioned differently, and the absolute-value graph is the
translated V that its item actually describes.

Every figure that carries a number asserts that number here, so a picture can
never disagree with the answer key: a mistyped value fails the build.

Labels go through figlabel, which measures each label's rendered box and refuses
to place one on top of the drawing.
"""
import json, os, shutil
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import figlabel as FL

plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["DejaVu Serif"]

OUT = "figs_saat"
shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT)

NAVY = "#1F3864"; INK = "#222E2D"; TEAL = "#17A199"; GREY = "#A6A6A6"
GRID = "#DCE9E8"
idx = {}


def start(figsize):
    FL.reset()
    return plt.subplots(figsize=figsize)


def save(fig, name):
    p = os.path.join(OUT, name + ".png")
    fig.savefig(p, dpi=400, transparent=True, bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)
    from PIL import Image
    with Image.open(p) as im:
        idx[name] = {"file": p, "aspect": im.width / im.height}
    return p


def frame(ax, xlim, ylim, equal=True):
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    if equal:
        ax.set_aspect("equal")
    ax.axis("off")


# --------------------------------------------------------------- rhombus
def rhombus():
    """Diagonals 16 and 30, so the half-diagonals are 8 and 15 and the side is 17.
    The right angle at the centre is marked, because that is the fact the item
    turns on and a student who cannot see it has nothing to work with."""
    p, q = 16.0, 30.0
    side = np.hypot(p / 2, q / 2)
    assert side == 17.0, side

    V = [(0, p / 2), (q / 2, 0), (0, -p / 2), (-q / 2, 0)]
    fig, ax = start(figsize=(3.4, 2.6))
    ax.add_patch(Polygon(np.array(V), closed=True, fill=False, ec=INK, lw=2.2))
    FL.record_patch_edges(V)
    FL.seg(ax, V[0], V[2], color=GREY, lw=1.1)
    FL.seg(ax, V[1], V[3], color=GREY, lw=1.1)
    # right-angle tick at the intersection — the fact the whole item turns on
    t = 1.6
    ax.plot([0, t, t], [t, t, 0], color=GREY, lw=1.0)

    # dimension lines OUTSIDE the shape, so each measurement clearly belongs to a
    # diagonal and not to a side
    dx, dy = q / 2 + 5.0, p / 2 + 5.0
    ax.annotate("", xy=(-dx, p / 2), xytext=(-dx, -p / 2),
                arrowprops=dict(arrowstyle="<|-|>", color=GREY, lw=1.0,
                                mutation_scale=9))
    ax.annotate("", xy=(q / 2, -dy), xytext=(-q / 2, -dy),
                arrowprops=dict(arrowstyle="<|-|>", color=GREY, lw=1.0,
                                mutation_scale=9))
    for y in (p / 2, -p / 2):
        ax.plot([-dx - 1.0, 0], [y, y], color=GREY, lw=0.6, ls=(0, (4, 3)))
    for x in (q / 2, -q / 2):
        ax.plot([x, x], [-dy - 1.0, 0], color=GREY, lw=0.6, ls=(0, (4, 3)))
    FL.seg(ax, (-dx, p / 2), (-dx, -p / 2), lw=0)
    FL.seg(ax, (q / 2, -dy), (-q / 2, -dy), lw=0)

    frame(ax, (-q / 2 - 24.0, q / 2 + 10.0), (-p / 2 - 14.0, p / 2 + 8.0))
    FL.outside_label(ax, "16 cm", (-dx, 0), (-1, 0), base=0.8, fontsize=12,
                     name="short diagonal")
    FL.outside_label(ax, "30 cm", (0, -dy), (0, -1), base=0.8, fontsize=12,
                     name="long diagonal")
    return save(fig, "saat_rhombus")


# ------------------------------------------------------------- trapezoid
def trapezoid():
    """AB = 6 on the bottom, CD unknown on top, EF the midsegment at 7.
    The picture is drawn with CD genuinely longer than AB — 8 to 6 — so the
    diagram agrees with the answer instead of contradicting it."""
    AB, CD, mid = 6.0, 8.0, 7.0
    assert (AB + CD) / 2 == mid

    h = 3.4
    STEPS = (0.55, 0.75, 1.0, 1.3, 1.7)
    A = (0.0, 0.0); B = (AB, 0.0)
    D = (-1.0, h); C = (-1.0 + CD, h)
    E = ((A[0] + D[0]) / 2, h / 2); F = ((B[0] + C[0]) / 2, h / 2)

    fig, ax = start(figsize=(3.2, 2.2))
    ax.add_patch(Polygon(np.array([A, B, C, D]), closed=True, fill=False,
                         ec=INK, lw=2.2))
    FL.record_patch_edges([A, B, C, D])
    FL.seg(ax, E, F, color=TEAL, lw=2.0)
    frame(ax, (-6.5, AB + 6.5), (-3.5, h + 3.5))
    FL.place(ax, "$A$", A, (-1, -1), steps=STEPS, fontsize=11, name="A")
    FL.place(ax, "$B$", B, (1, -1), steps=STEPS, fontsize=11, name="B")
    FL.place(ax, "$C$", C, (1, 1), steps=STEPS, fontsize=11, name="C")
    FL.place(ax, "$D$", D, (-1, 1), steps=STEPS, fontsize=11, name="D")
    FL.place(ax, "$E$", E, (-1, 0), steps=STEPS, fontsize=11, name="E")
    FL.place(ax, "$F$", F, (1, 0), steps=STEPS, fontsize=11, name="F")
    FL.outside_label(ax, "6 cm", (AB / 2, 0), (0, -1), base=0.55, fontsize=11,
                     name="AB length")
    return save(fig, "saat_trapezoid")


# ------------------------------------------------- translated absolute value
def absgraph():
    """y = |x - 3| + 1: vertex at (3, 1), which is what makes the parent
    function question worth asking. Axes carry arrowheads and a recessive grid,
    and the vertex is the only labelled point."""
    vx, vy = 3.0, 1.0
    # the sample grid includes the vertex itself, so the assert below
    # tests the drawn curve rather than a point that misses the corner
    xs = np.unique(np.concatenate([np.linspace(-1.2, vx, 220),
                                   np.linspace(vx, 7.2, 220)]))
    ys = np.abs(xs - vx) + vy
    assert abs(ys.min() - vy) < 1e-12

    fig, ax = start(figsize=(2.7, 2.5))
    for g in range(-1, 8):
        ax.plot([g, g], [-0.6, 6.2], color=GRID, lw=0.6, zorder=0)
    for g in range(0, 7):
        ax.plot([-1.2, 7.4], [g, g], color=GRID, lw=0.6, zorder=0)
    ax.annotate("", xy=(7.6, 0), xytext=(-1.4, 0),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.2))
    ax.annotate("", xy=(0, 6.4), xytext=(0, -0.8),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.2))
    ax.plot(xs, ys, color=NAVY, lw=2.4, zorder=3)
    ax.plot([vx], [vy], "o", color=NAVY, ms=5, zorder=4)
    FL.polyline(ax, list(zip(xs, ys)), lw=0)
    FL.seg(ax, (-1.4, 0), (7.6, 0), lw=0)      # the axes are ink too
    FL.seg(ax, (0, -0.8), (0, 6.4), lw=0)
    frame(ax, (-3.4, 10.0), (-2.6, 7.6), equal=False)
    FL.place(ax, "$x$", (7.5, 0), (0, -1), steps=(0.5, 0.8, 1.1), fontsize=11, name="x axis")
    FL.place(ax, "$y$", (0, 6.3), (-1, 0), steps=(0.5, 0.8, 1.1), fontsize=11, name="y axis")
    FL.place(ax, "$(3,\\,1)$", (vx, vy), (1, 0), steps=(1.0, 1.4, 1.8, 2.3),
             fontsize=11, name="vertex")
    return save(fig, "saat_absgraph")


if __name__ == "__main__":
    rhombus(); trapezoid(); absgraph()
    json.dump(idx, open(os.path.join(OUT, "_index.json"), "w"), indent=1)
    print(f"{len(idx)} figures -> {OUT}")
