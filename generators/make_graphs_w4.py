"""
Week 4 graphs. House style: recessive grid, arrowheads on axes, thin marks,
direct labels, Computer Modern. Every label placed explicitly, and every
picture asserts the numbers the slide states.

  A · Gr10 1-4  Arithmetic Sequences and Series
  B · Gr11 5-6  Inverse Relations and Functions
"""
import json, os, shutil
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from PIL import Image

plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["DejaVu Serif"]

OUT = "graphs_w4"
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


# =============================================== A · Gr10 1-4
def arith_points(name):
    """5, 9, 13, 17, 21 plotted against position. The POINTS are the sequence;
    the dashed line only shows that they are collinear."""
    n = np.arange(1, 6)
    a = 4 * n + 1
    assert list(a) == [5, 9, 13, 17, 21]
    fig, ax = plt.subplots(figsize=(5.4, 3.3))
    axes(ax, (-0.6, 7.4), (-2.5, 26), xstep=1, ystep=4)
    xs = np.linspace(0.2, 7.0, 50)
    ax.plot(xs, 4 * xs + 1, color=MUTED, lw=1.1, ls=(0, (5, 4)), zorder=2)
    ax.plot(n, a, "o", ms=7, color=TEAL, zorder=5)
    for k, v in zip(n, a):
        ax.annotate(f"${v}$", (k, v), xytext=(0, 9), textcoords="offset points",
                    ha="center", color=DEEP, fontsize=9.5)
    for k in range(1, 5):
        ax.annotate("", xy=(k + 1, 4 * (k + 1) + 1), xytext=(k, 4 * k + 1),
                    arrowprops=dict(arrowstyle="->", color=MAROON, lw=1.1,
                                    connectionstyle="arc3,rad=-0.28"), zorder=4)
    ax.text(3.5, 3.0, r"each step $+4$", color=MAROON, fontsize=10, bbox=BOX, ha="center")
    ax.text(6.0, 21.0, r"$a_{n}=4n+1$", color=MUTED, fontsize=10, bbox=BOX, ha="center")
    ax.set_xlabel(r"position $n$", color=MUTED, fontsize=9.5, labelpad=-2)
    fig.tight_layout()
    save(fig, name)


def arith_pair(name):
    """The pairing picture behind S_n = n/2 (a_1 + a_n): a staircase and its
    reverse stack into a rectangle n wide and (a_1 + a_n) tall."""
    a1, d, n = 5, 4, 5
    terms = [a1 + i * d for i in range(n)]
    tot = a1 + terms[-1]
    assert sum(terms) * 2 == n * tot
    fig, ax = plt.subplots(figsize=(5.4, 3.0))
    ax.set_xlim(-0.6, n + 1.4); ax.set_ylim(-3.4, tot + 3.2)
    ax.axis("off")
    for i, t in enumerate(terms):
        ax.add_patch(Rectangle((i + 0.1, 0), 0.8, t, facecolor=TEAL,
                               ec="white", lw=1.0, zorder=3))
        ax.add_patch(Rectangle((i + 0.1, t), 0.8, tot - t, facecolor="#F2C230",
                               ec="white", lw=1.0, zorder=3))
        ax.text(i + 0.5, t / 2, f"${t}$", ha="center", va="center",
                color="white", fontsize=9.5, zorder=5)
        ax.text(i + 0.5, t + (tot - t) / 2, f"${tot - t}$", ha="center", va="center",
                color=INK, fontsize=9.5, zorder=5)
    ax.plot([0.1, n - 0.1 + 0.8], [tot, tot], color=INK, lw=1.2, zorder=4)
    ax.annotate("", xy=(n + 0.75, 0), xytext=(n + 0.75, tot),
                arrowprops=dict(arrowstyle="<|-|>", color=DEEP, lw=1.1, mutation_scale=9))
    ax.text(n + 0.95, tot / 2, f"$a_1+a_n={tot}$", color=DEEP, fontsize=10,
            va="center", ha="left")
    ax.annotate("", xy=(n - 0.1 + 0.8, -1.5), xytext=(0.1, -1.5),
                arrowprops=dict(arrowstyle="<|-|>", color=DEEP, lw=1.1, mutation_scale=9))
    ax.text((n + 0.8) / 2, -2.8, f"$n={n}$ terms", color=DEEP, fontsize=10, ha="center")
    ax.text(0.1, tot + 1.4, "the sequence, and the same sequence upside down",
            color=MUTED, fontsize=9)
    fig.tight_layout()
    save(fig, name)


# =============================================== B · Gr11 5-6
def inv_reflect(name):
    """f(x) = 3x - 8 and its inverse, mirrored in y = x."""
    f = lambda x: 3 * x - 8
    g = lambda x: (x + 8) / 3
    for t in (-2.0, 0.0, 4.0):
        assert abs(g(f(t)) - t) < 1e-12 and abs(f(g(t)) - t) < 1e-12
    fig, ax = plt.subplots(figsize=(4.3, 4.1))
    axes(ax, (-10, 10), (-10, 10), xstep=2, ystep=2)
    xs = np.linspace(-10, 10, 200)
    ax.plot(xs, xs, color=MUTED, lw=1.0, ls=(0, (5, 4)), zorder=2)
    ax.plot(xs, f(xs), color=TEAL, lw=2.1, zorder=4)
    ax.plot(xs, g(xs), color=MAROON, lw=2.1, zorder=4)
    ax.plot(4, 4, "o", ms=5, color=MUTED, zorder=6)
    ax.plot(3, 1, "o", ms=6, color=TEAL, zorder=6)
    ax.plot(1, 3, "o", ms=6, color=MAROON, zorder=6)
    ax.annotate("", xy=(1, 3), xytext=(3, 1),
                arrowprops=dict(arrowstyle="<->", color=MUTED, lw=0.9,
                                connectionstyle="arc3,rad=0.22"), zorder=5)
    ax.text(1.4, 9.1, r"$f(x)=3x-8$", color=TEAL, fontsize=9.5, bbox=BOX, ha="center")
    ax.text(-5.4, 4.6, r"$f^{-1}(x)=\dfrac{x+8}{3}$", color=MAROON, fontsize=9.5,
            bbox=BOX, ha="center")
    ax.text(8.6, 7.0, r"$y=x$", color=MUTED, fontsize=9.5, bbox=BOX, ha="center")
    ax.text(3.3, -1.4, r"$(3,1)\leftrightarrow(1,3)$", color=INK, fontsize=9,
            bbox=BOX, ha="center")
    fig.tight_layout()
    save(fig, name)


def inv_restrict(name):
    """y = x^2 has no inverse until the domain is cut to x >= 0."""
    fig, ax = plt.subplots(figsize=(4.3, 4.1))
    axes(ax, (-6, 9), (-6, 9), xstep=2, ystep=2)
    xs = np.linspace(-6, 9, 300)
    ax.plot(xs, xs, color=MUTED, lw=1.0, ls=(0, (5, 4)), zorder=2)
    neg = np.linspace(-3.0, 0, 120)
    ax.plot(neg, neg ** 2, color=MUTED, lw=1.6, ls=(0, (3, 3)), zorder=3)
    pos = np.linspace(0, 3.0, 120)
    ax.plot(pos, pos ** 2, color=TEAL, lw=2.2, zorder=4)
    r = np.linspace(0, 9, 200)
    ax.plot(r, np.sqrt(r), color=MAROON, lw=2.2, zorder=4)
    ax.plot(0, 0, "o", ms=5.5, color=INK, zorder=6)
    ax.text(5.9, 7.4, r"$f(x)=x^{2},\ x\geq 0$", color=TEAL, fontsize=9.5,
            bbox=BOX, ha="center")
    ax.text(6.4, 1.3, r"$f^{-1}(x)=\sqrt{x}$", color=MAROON, fontsize=9.5,
            bbox=BOX, ha="center")
    ax.text(-3.9, 3.6, "the part we cut off", color=MUTED, fontsize=9,
            bbox=BOX, ha="center")
    fig.tight_layout()
    save(fig, name)


def inv_gate(name):
    """The Mastery Gate graph: a one-to-one function with three points marked,
    so an inverse value can be READ rather than calculated."""
    pts = [(-2, -3), (0, 1), (2, 5), (4, 9)]
    for x, y in pts:
        assert y == 2 * x + 1
    fig, ax = plt.subplots(figsize=(4.2, 3.6))
    axes(ax, (-5, 7), (-6, 11), xstep=1, ystep=2)
    xs = np.linspace(-4.6, 4.8, 100)
    ax.plot(xs, 2 * xs + 1, color=TEAL, lw=2.2, zorder=4)
    for x, y in pts:
        ax.plot(x, y, "o", ms=6, color=DEEP, zorder=6)
        ax.annotate(f"$({x},{y})$", (x, y), xytext=(9, 4),
                    textcoords="offset points", color=DEEP, fontsize=8.5, bbox=BOX)
    ax.text(-3.4, 8.4, r"$y=g(x)$", color=TEAL, fontsize=10, bbox=BOX, ha="center")
    fig.tight_layout()
    save(fig, name)


arith_points("g_ar_points")
arith_pair("g_ar_pair")
inv_reflect("g_inv_reflect")
inv_restrict("g_inv_restrict")
inv_gate("g_inv_gate")

json.dump(idx, open(os.path.join(OUT, "_index.json"), "w"), indent=1)
for k, v in idx.items():
    print(f"{k:16s} aspect {v['aspect']:.2f}")
