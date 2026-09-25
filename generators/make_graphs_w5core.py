"""
Week 5 core graphs. House style: recessive grid, arrowheads on axes, thin
marks, direct labels, Computer Modern. Every label placed explicitly, and
every picture asserts the numbers the slide states.

  A · Gr10 T1 L5  Solving Equations and Inequalities by Graphing
  B · Gr11 T6 L6-1  Key Features of Exponential Functions
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

OUT = "graphs_w5core"
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


# =============================================== A · Gr10 T1 L5
def lines_eq(name):
    """y = 3x - 2 and y = -x + 6, meeting at (2, 4)."""
    f = lambda x: 3 * x - 2
    g = lambda x: -x + 6
    assert f(2) == 4 and g(2) == 4
    fig, ax = plt.subplots(figsize=(5.2, 3.6))
    axes(ax, (-1, 6), (-3, 12), xstep=1, ystep=2)
    xs = np.linspace(-0.8, 5.8, 200)
    ax.plot(xs, f(xs), color=TEAL, lw=2.2, zorder=4)
    ax.plot(xs, g(xs), color=MAROON, lw=2.2, zorder=4)
    ax.plot(2, 4, "o", ms=7, color=DEEP, zorder=6)
    ax.annotate("$(2,4)$", (2, 4), xytext=(-64, -22), textcoords="offset points",
                color=DEEP, fontsize=10, bbox=BOX)
    ax.text(1.1, 9.6, r"$y=3x-2$", color=TEAL, fontsize=10, bbox=BOX, ha="center")
    ax.text(4.3, 3.9, r"$y=-x+6$", color=MAROON, fontsize=10, bbox=BOX, ha="center")
    ax.set_xlabel("$x$", color=MUTED, fontsize=9.5, labelpad=-2)
    fig.tight_layout()
    save(fig, name)


def lines_ineq(name):
    """Same two lines, with the region where 3x - 2 > -x + 6 shaded."""
    f = lambda x: 3 * x - 2
    g = lambda x: -x + 6
    fig, ax = plt.subplots(figsize=(5.2, 3.6))
    axes(ax, (-1, 6), (-3, 12), xstep=1, ystep=2)
    xs = np.linspace(-0.8, 5.8, 200)
    xs_r = np.linspace(2, 5.8, 100)
    ax.fill_between(xs_r, g(xs_r), 12, color=TEAL, alpha=0.13, zorder=1)
    ax.plot(xs, f(xs), color=TEAL, lw=2.2, zorder=4)
    ax.plot(xs, g(xs), color=MAROON, lw=2.2, zorder=4)
    ax.plot(2, 4, "o", ms=7, color=DEEP, zorder=6)
    ax.annotate("$(2,4)$", (2, 4), xytext=(-64, -22), textcoords="offset points",
                color=DEEP, fontsize=10, bbox=BOX)
    ax.text(4.3, 9.6, r"$3x-2>-x+6$" + "\n" + r"$\Longrightarrow x>2$", color=DEEP,
            fontsize=9.5, bbox=BOX, ha="center")
    ax.set_xlabel("$x$", color=MUTED, fontsize=9.5, labelpad=-2)
    fig.tight_layout()
    save(fig, name)


def table_approx(name):
    """y = x^2 and y = 2x + 1 meet at x = 1 ± sqrt(2); zoom shows the table
    narrowing between x = 2.4 and x = 2.5."""
    f = lambda x: x ** 2
    g = lambda x: 2 * x + 1
    root = 1 + np.sqrt(2)
    fig, ax = plt.subplots(figsize=(5.4, 3.6))
    axes(ax, (-2, 4.5), (-2, 12), xstep=1, ystep=2)
    xs = np.linspace(-1.9, 4.4, 300)
    ax.plot(xs, f(xs), color=TEAL, lw=2.2, zorder=4)
    ax.plot(xs, g(xs), color=MAROON, lw=2.2, zorder=4)
    for r in (root, 1 - np.sqrt(2)):
        ax.plot(r, f(r), "o", ms=6.5, color=DEEP, zorder=6)
    ax.annotate(r"$x\approx 2.41$", (root, f(root)), xytext=(28, 8),
                textcoords="offset points", color=DEEP, fontsize=9.5, bbox=BOX)
    ax.annotate(r"$x\approx -0.41$", (1 - np.sqrt(2), f(1 - np.sqrt(2))),
                xytext=(-14, 26), textcoords="offset points", color=DEEP,
                fontsize=9.5, bbox=BOX)
    ax.text(3.6, 10.6, r"$y=x^{2}$", color=TEAL, fontsize=10, bbox=BOX, ha="center")
    ax.text(-1.1, 8.4, r"$y=2x+1$", color=MAROON, fontsize=10, bbox=BOX, ha="center")
    fig.tight_layout()
    save(fig, name)


def gate_lines(name):
    """y = -2x + 9 and y = 3x - 1, meeting at (2, 5) — Mastery Gate graph."""
    f = lambda x: -2 * x + 9
    g = lambda x: 3 * x - 1
    assert f(2) == 5 and g(2) == 5
    fig, ax = plt.subplots(figsize=(4.6, 3.6))
    axes(ax, (-1, 5), (-3, 12), xstep=1, ystep=2)
    xs = np.linspace(-0.8, 4.8, 200)
    ax.plot(xs, f(xs), color=TEAL, lw=2.2, zorder=4)
    ax.plot(xs, g(xs), color=MAROON, lw=2.2, zorder=4)
    ax.plot(2, 5, "o", ms=7, color=DEEP, zorder=6)
    ax.text(3.6, 10.4, r"$y=-2x+9$", color=TEAL, fontsize=9.5, bbox=BOX, ha="center")
    ax.text(3.4, 1.0, r"$y=3x-1$", color=MAROON, fontsize=9.5, bbox=BOX, ha="center")
    fig.tight_layout()
    save(fig, name)


# =============================================== B · Gr11 T6 L6-1
def exp_growth(name):
    """f(x) = 2^x — intercept, asymptote, domain/range all labelled."""
    f = lambda x: 2.0 ** x
    fig, ax = plt.subplots(figsize=(5.0, 3.7))
    axes(ax, (-4.4, 3.4), (-2, 9), xstep=1, ystep=2)
    xs = np.linspace(-4.3, 3.15, 300)
    ax.axhline(0, color=MUTED, lw=1.0, ls=(0, (5, 4)), zorder=2)
    ax.plot(xs, f(xs), color=TEAL, lw=2.3, zorder=4)
    ax.plot(0, 1, "o", ms=6.5, color=DEEP, zorder=6)
    ax.annotate("$(0,1)$", (0, 1), xytext=(8, -16), textcoords="offset points",
                color=DEEP, fontsize=9.5, bbox=BOX)
    ax.text(-2.6, 6.6, r"$f(x)=2^{x}$", color=TEAL, fontsize=10.5, bbox=BOX, ha="center")
    ax.text(1.0, -1.55, r"asymptote $y=0$", color=MUTED, fontsize=9, bbox=BOX, ha="center")
    ax.annotate("", xy=(3.2, 8.2), xytext=(2.0, 4.5),
                arrowprops=dict(arrowstyle="->", color=DEEP, lw=1.1))
    ax.text(2.85, 5.0, "end behavior:\n" + r"$x\to\infty,\ f\to\infty$", color=DEEP,
            fontsize=8, bbox=BOX, ha="center")
    ax.annotate("", xy=(-4.1, 0.35), xytext=(-3.2, 1.6),
                arrowprops=dict(arrowstyle="->", color=DEEP, lw=1.1))
    ax.text(-3.55, 2.7, "end behavior:\n" + r"$x\to-\infty,\ f\to 0^{+}$", color=DEEP,
            fontsize=8, bbox=BOX, ha="center")
    ax.set_xlabel("$x$", color=MUTED, fontsize=9.5, labelpad=-2)
    fig.tight_layout()
    save(fig, name)


def exp_growth_decay(name):
    """f(x) = 2^x (growth) and g(x) = (0.5)^x (decay) meeting at (0, 1)."""
    f = lambda x: 2.0 ** x
    g = lambda x: 0.5 ** x
    fig, ax = plt.subplots(figsize=(5.2, 3.7))
    axes(ax, (-3.4, 3.4), (-1, 9), xstep=1, ystep=2)
    xs = np.linspace(-3.3, 3.3, 300)
    ax.axhline(0, color=MUTED, lw=1.0, ls=(0, (5, 4)), zorder=2)
    ax.plot(xs, f(xs), color=TEAL, lw=2.2, zorder=4)
    ax.plot(xs, g(xs), color=MAROON, lw=2.2, zorder=4)
    ax.plot(0, 1, "o", ms=6.5, color=DEEP, zorder=6)
    ax.annotate("$(0,1)$", (0, 1), xytext=(8, 8), textcoords="offset points",
                color=DEEP, fontsize=9.5, bbox=BOX)
    ax.text(1.75, 6.9, r"$f(x)=2^{x}$" + "\n" + "growth, $b=2>1$", color=TEAL,
            fontsize=9, bbox=BOX, ha="center")
    ax.text(-2.1, 4.4, r"$g(x)=(0.5)^{x}$" + "\n" + "decay, $b=0.5$", color=MAROON,
            fontsize=9, bbox=BOX, ha="center")
    ax.set_xlabel("$x$", color=MUTED, fontsize=9.5, labelpad=-2)
    fig.tight_layout()
    save(fig, name)


def exp_transform(name):
    """f(x) = 2^x, its vertical shift g(x) = 2^x - 3, and its reflection
    h(x) = -2^x, each with its own asymptote marked."""
    f = lambda x: 2.0 ** x
    g = lambda x: 2.0 ** x - 3
    h = lambda x: -(2.0 ** x)
    fig, ax = plt.subplots(figsize=(5.4, 4.0))
    axes(ax, (-3.6, 3.2), (-9, 8), xstep=1, ystep=2)
    xs = np.linspace(-3.5, 3.1, 300)
    ax.axhline(0, color=MUTED, lw=0.9, ls=(0, (5, 4)), zorder=2)
    ax.axhline(-3, color=GOLD, lw=0.9, ls=(0, (5, 4)), zorder=2)
    ax.plot(xs, f(xs), color=TEAL, lw=2.0, zorder=4)
    ax.plot(xs, g(xs), color=GOLD, lw=2.0, zorder=4)
    ax.plot(xs, h(xs), color=MAROON, lw=2.0, zorder=4)
    ax.plot(0, 1, "o", ms=5.5, color=TEAL, zorder=6)
    ax.plot(0, -2, "o", ms=5.5, color=GOLD, zorder=6)
    ax.plot(0, -1, "o", ms=5.5, color=MAROON, zorder=6)
    ax.text(-2.4, 5.6, r"$f(x)=2^{x}$", color=TEAL, fontsize=9.5, bbox=BOX, ha="center")
    ax.text(1.9, -6.4, r"$g(x)=2^{x}-3$", color=GOLD, fontsize=9.5, bbox=BOX, ha="center")
    ax.text(-2.0, -6.4, r"$h(x)=-2^{x}$", color=MAROON, fontsize=9.5, bbox=BOX, ha="center")
    fig.tight_layout()
    save(fig, name)


lines_eq("g_lines_eq")
lines_ineq("g_lines_ineq")
table_approx("g_table_approx")
gate_lines("g_gate_lines")
exp_growth("g_exp_growth")
exp_growth_decay("g_exp_growth_decay")
exp_transform("g_exp_transform")

json.dump(idx, open(os.path.join(OUT, "_index.json"), "w"), indent=1)
for k, v in idx.items():
    print(f"{k:18s} aspect {v['aspect']:.2f}")
