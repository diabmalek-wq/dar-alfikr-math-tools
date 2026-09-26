"""
Week 7 graphs — Grade 10 Topic 2 Lesson 1, "Vertex Form of a Quadratic
Function". House style: recessive grid, arrowheads on axes, thin marks,
direct labels, Computer Modern. Every label placed explicitly, and every
picture asserts the numbers the slide states.

  A · Gr10 T2 L1  Vertex Form of a Quadratic Function
"""
import json, os, shutil
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image

plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["DejaVu Serif"]

OUT = "graphs_w7"
shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(OUT)

TEAL = "#17A199"; MAROON = "#AD2A22"; INK = "#222E2D"
MUTED = "#5C6E6C"; GRID = "#DCE9E8"; DEEP = "#0E4F4C"; GOLD = "#C8912A"
BOX = dict(boxstyle="round,pad=0.18", fc="white", ec="none", alpha=0.88)

idx = {}


def axes(ax, xlim, ylim, xstep=1, ystep=1, grid=True):
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    if grid:
        ax.set_xticks(np.arange(np.ceil(xlim[0]), xlim[1] + 1e-9, xstep))
        ax.set_yticks(np.arange(np.ceil(ylim[0]), ylim[1] + 1e-9, ystep))
        ax.grid(True, color=GRID, lw=0.7, zorder=0)
    ax.spines["left"].set_position("zero"); ax.spines["bottom"].set_position("zero")
    ax.spines["right"].set_color("none"); ax.spines["top"].set_color("none")
    ax.spines["left"].set_color(MUTED); ax.spines["bottom"].set_color(MUTED)
    ax.tick_params(colors=MUTED, labelsize=8)
    ax.plot(1, 0, ">", transform=ax.get_yaxis_transform(), color=MUTED,
            clip_on=False, ms=5)
    ax.plot(0, 1, "^", transform=ax.get_xaxis_transform(), color=MUTED,
            clip_on=False, ms=5)


def save(fig, name):
    p = os.path.join(OUT, name + ".png")
    fig.savefig(p, dpi=460, transparent=True, bbox_inches="tight", pad_inches=0.04)
    plt.close(fig)
    with Image.open(p) as im:
        idx[name] = {"file": p, "aspect": im.width / im.height}


# =============================================== A · Gr10 T2 L1
def vertex_transform(name):
    """Parent y = x^2 (dashed) and f(x) = 2(x-3)^2 + 4 (solid), vertex
    marked at (3, 4), axis of symmetry x = 3 shown dashed."""
    parent = lambda x: x ** 2
    f = lambda x: 2 * (x - 3) ** 2 + 4
    assert f(3) == 4
    fig, ax = plt.subplots(figsize=(5.6, 4.0))
    axes(ax, (-2.5, 6.5), (-2, 20), xstep=1, ystep=4)
    xs = np.linspace(-2.3, 2.3, 200)
    xs2 = np.linspace(1.2, 4.8, 200)
    ax.plot(xs, parent(xs), color=MUTED, lw=1.8, ls=(0, (5, 4)), zorder=3)
    ax.axvline(3, color=GOLD, lw=1.1, ls=(0, (4, 4)), zorder=2)
    ax.plot(xs2, f(xs2), color=TEAL, lw=2.3, zorder=4)
    ax.plot(3, 4, "o", ms=7, color=DEEP, zorder=6)
    ax.plot(0, 0, "o", ms=6, color=MUTED, zorder=6)
    ax.annotate("$(3,4)$", (3, 4), xytext=(10, -20), textcoords="offset points",
                color=DEEP, fontsize=9.5, bbox=BOX)
    ax.annotate("$(0,0)$", (0, 0), xytext=(-38, 6), textcoords="offset points",
                color=MUTED, fontsize=9, bbox=BOX)
    ax.text(-1.7, 15, r"$y=x^{2}$", color=MUTED, fontsize=10, bbox=BOX, ha="center")
    ax.text(5.1, 15, r"$f(x)=2(x-3)^{2}+4$", color=TEAL, fontsize=9.5, bbox=BOX, ha="center")
    ax.text(3.35, 18.5, r"$x=3$", color=GOLD, fontsize=9, bbox=BOX, ha="left")
    ax.set_xlabel("$x$", color=MUTED, fontsize=9.5, labelpad=-2)
    fig.tight_layout()
    save(fig, name)


def fountain(name):
    """Decorative fountain arc: h(x) = -(x-2)^2 + 4, vertex (2, 4),
    ground at x = 0 and x = 4."""
    h = lambda x: -(x - 2) ** 2 + 4
    assert h(0) == 0 and h(4) == 0 and h(2) == 4
    fig, ax = plt.subplots(figsize=(5.2, 3.8))
    axes(ax, (-0.6, 4.6), (-1, 5.5), xstep=1, ystep=1)
    xs = np.linspace(-0.2, 4.2, 200)
    ax.axvline(2, color=GOLD, lw=1.0, ls=(0, (4, 4)), zorder=2)
    ax.fill_between(xs, 0, h(xs), where=(h(xs) >= 0), color=TEAL, alpha=0.15, zorder=1)
    ax.plot(xs, h(xs), color=TEAL, lw=2.3, zorder=4)
    ax.plot([0, 4], [0, 0], "o", ms=7, color=MUTED, zorder=6)
    ax.plot(2, 4, "o", ms=7, color=DEEP, zorder=6)
    ax.annotate("$(2,4)$", (2, 4), xytext=(10, 6), textcoords="offset points",
                color=DEEP, fontsize=9.5, bbox=BOX)
    ax.annotate("$(0,0)$", (0, 0), xytext=(18, 10), textcoords="offset points",
                color=MUTED, fontsize=9, bbox=BOX, ha="center")
    ax.annotate("$(4,0)$", (4, 0), xytext=(-18, 10), textcoords="offset points",
                color=MUTED, fontsize=9, bbox=BOX, ha="center")
    ax.text(3.55, 4.9, r"$x=2$", color=GOLD, fontsize=9, bbox=BOX, ha="left")
    ax.set_xlabel("horizontal distance (m)", color=MUTED, fontsize=9, labelpad=-2)
    ax.set_ylabel("height (m)", color=MUTED, fontsize=9.5)
    fig.tight_layout()
    save(fig, name)


vertex_transform("g_vertex_transform")
fountain("g_fountain")

json.dump(idx, open(os.path.join(OUT, "_index.json"), "w"), indent=1)
for k, v in idx.items():
    print(f"{k:18s} aspect {v['aspect']:.2f}")
