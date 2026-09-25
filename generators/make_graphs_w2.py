"""
Week 2 graphs. House style: recessive grid, arrowheads on axes, thin marks,
direct labels, Computer Modern throughout. Rendered and inspected before use.
"""
import json, os, shutil
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["DejaVu Serif"]

OUT = "graphs_w2"
shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT)

TEAL = "#17A199"; MAROON = "#AD2A22"; INK = "#222E2D"
MUTED = "#5C6E6C"; GRID = "#DCE9E8"; DEEP = "#0E4F4C"


def frame(ax, xlim, ylim, xt=None, yt=None):
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    ax.set_aspect("auto")
    ax.grid(True, color=GRID, lw=0.7, zorder=0)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    ax.spines["left"].set_position(("data", 0))
    ax.spines["bottom"].set_position(("data", 0))
    for sp in ("left", "bottom"):
        ax.spines[sp].set_color(INK); ax.spines[sp].set_linewidth(1.0)
    ax.set_xticks(xt if xt is not None else np.arange(int(xlim[0]) + 1, int(xlim[1]) + 1, 2))
    ax.set_yticks(yt if yt is not None else np.arange(int(ylim[0]) + 1, int(ylim[1]) + 1, 2))
    ax.tick_params(colors=MUTED, labelsize=8, length=3, width=0.8)
    # arrowheads
    ax.plot(1, 0, ">", transform=ax.get_yaxis_transform(), clip_on=False, color=INK, ms=5)
    ax.plot(0, 1, "^", transform=ax.get_xaxis_transform(), clip_on=False, color=INK, ms=5)
    ax.set_axisbelow(True)


def save(fig, name):
    p = os.path.join(OUT, name + ".png")
    fig.savefig(p, dpi=300, transparent=True, bbox_inches="tight", pad_inches=0.06)
    plt.close(fig)
    return p


idx = {}


def reg(name, path):
    from PIL import Image
    with Image.open(path) as im:
        idx[name] = {"file": path, "aspect": im.width / im.height}


# ======================================================= A · TRANSFORMATIONS
# parent quadratic with the four transformation families, one panel each
def transform_panel():
    """Four panels. Every label is placed explicitly — the generic
    'annotate at the top of the curve' rule collided badly."""
    fig, axes = plt.subplots(1, 4, figsize=(13.6, 3.5))
    x = np.linspace(-4, 4, 400)
    pan = [
        ("Translation", [(x**2, TEAL, "-", "$f(x)$", (-3.5, 6.4)),
                         (x**2 + 3, MAROON, "-", "$f(x)+3$", (0.5, 7.6))]),
        ("Translation", [(x**2, TEAL, "-", "$f(x)$", (-3.6, 6.4)),
                         ((x - 2)**2, MAROON, "-", "$f(x-2)$", (0.7, 7.6))]),
        ("Reflection", [(x**2, TEAL, "-", "$f(x)$", (-3.6, 6.4)),
                        (-x**2, MAROON, "-", "$-f(x)$", (0.9, -5.2))]),
        ("Stretch and compression", [(x**2, TEAL, "-", "$f(x)$", (-3.9, 6.4)),
                                     (3 * x**2, MAROON, "-", "$3f(x)$", (1.1, 7.6)),
                                     (0.25 * x**2, DEEP, "--", r"$\frac{1}{4}f(x)$", (2.1, 0.6))]),
    ]
    for ax, (title, curves) in zip(axes, pan):
        frame(ax, (-4.4, 4.4), (-6.5, 9.5), xt=[-4, -2, 2, 4], yt=[-6, -3, 3, 6, 9])
        for ys, c, ls, lab, pos in curves:
            m = (ys > -6.5) & (ys < 9.5)
            ax.plot(x[m], ys[m], color=c, lw=2.0, ls=ls, zorder=3)
            ax.annotate(lab, pos, color=c, fontsize=10.5, zorder=6,
                        bbox=dict(boxstyle="round,pad=0.12", fc="white", ec="none", alpha=0.85))
        ax.set_title(title, fontsize=11, color=DEEP, pad=8)
    fig.tight_layout()
    return save(fig, "g_transform_panel")


reg("g_transform_panel", transform_panel())


def transform_worked():
    fig, ax = plt.subplots(figsize=(6.4, 4.4))
    x = np.linspace(-2, 8, 500)
    frame(ax, (-2.4, 8.4), (-7.5, 8.5), xt=[-2, 2, 4, 6, 8], yt=[-6, -3, 3, 6])
    ax.plot(x, x**2, color=TEAL, lw=1.6, ls="--", zorder=3)
    g = -2 * (x - 3)**2 + 5
    m = g > -7.5
    ax.plot(x[m], g[m], color=MAROON, lw=2.4, zorder=4)
    ax.annotate("$f(x)=x^2$", (-1.9, 5.4), color=TEAL, fontsize=11, zorder=6,
                bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.9))
    ax.annotate("$g(x)=-2(x-3)^2+5$", (3.5, 7.0), color=MAROON, fontsize=11, zorder=6,
                bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.9))
    ax.plot([3], [5], "o", color=MAROON, ms=6, zorder=5)
    ax.annotate("vertex $(3,\\,5)$", (3, 5), color=MAROON, fontsize=9.5, zorder=6,
                xytext=(16, -26), textcoords="offset points")
    fig.tight_layout()
    return save(fig, "g_transform_worked")


reg("g_transform_worked", transform_worked())


def transform_gate():
    fig, ax = plt.subplots(figsize=(5.6, 4.2))
    x = np.linspace(-7, 3, 400)
    frame(ax, (-7.4, 3.4), (-5.5, 8.5), xt=[-6, -4, -2, 2], yt=[-4, -2, 2, 4, 6, 8])
    g = -(x + 2)**2 + 7
    m = g > -5.5
    ax.plot(x[m], g[m], color=MAROON, lw=2.4, zorder=4)
    ax.plot([-2], [7], "o", color=MAROON, ms=6, zorder=5)
    fig.tight_layout()
    return save(fig, "g_transform_gate")


reg("g_transform_gate", transform_gate())


# arch context — Saudi: a parabolic arch
def arch():
    fig, ax = plt.subplots(figsize=(6.6, 3.6))
    x = np.linspace(0, 60, 400)
    h = -0.02 * (x - 30)**2 + 18
    ax.set_xlim(-3, 64); ax.set_ylim(-1.5, 22)
    ax.grid(True, color=GRID, lw=0.7, zorder=0); ax.set_axisbelow(True)
    for sp in ("top", "right"): ax.spines[sp].set_visible(False)
    for sp in ("left", "bottom"):
        ax.spines[sp].set_color(INK); ax.spines[sp].set_linewidth(1.0)
    ax.spines["left"].set_position(("data", 0)); ax.spines["bottom"].set_position(("data", 0))
    ax.plot(x, h, color=TEAL, lw=2.6, zorder=3)
    ax.fill_between(x, 0, h, color=TEAL, alpha=0.08, zorder=1)
    ax.plot([30], [18], "o", color=MAROON, ms=6, zorder=5)
    ax.annotate("highest point $(30,\\,18)$", (30, 18), color=MAROON, fontsize=9.5,
                xytext=(8, -6), textcoords="offset points")
    ax.set_xticks([0, 15, 30, 45, 60]); ax.set_yticks([5, 10, 15, 20])
    ax.tick_params(colors=MUTED, labelsize=8, length=3, width=0.8)
    ax.set_xlabel("distance across the span, metres", fontsize=9.5, color=MUTED)
    ax.set_ylabel("height, metres", fontsize=9.5, color=MUTED)
    ax.plot(1, 0, ">", transform=ax.get_yaxis_transform(), clip_on=False, color=INK, ms=5)
    ax.plot(0, 1, "^", transform=ax.get_xaxis_transform(), clip_on=False, color=INK, ms=5)
    fig.tight_layout()
    return save(fig, "g_arch")


reg("g_arch", arch())


# ======================================================= B · RADICAL GRAPHS
def radical_parents():
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 3.9))
    # square root
    ax = axes[0]
    x = np.linspace(0, 9, 400)
    frame(ax, (-5.4, 9.4), (-3.5, 4.5), xt=[-4, -2, 2, 4, 6, 8], yt=[-2, 2, 4])
    ax.plot(x, np.sqrt(x), color=TEAL, lw=2.4, zorder=3)
    ax.plot([0], [0], "o", color=TEAL, ms=6, zorder=5)
    ax.annotate(r"$f(x)=\sqrt{x}$", (3.4, 3.5), color=TEAL, fontsize=11, zorder=6,
                bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.9))
    ax.annotate("domain $[0,\\infty)$", (1.2, -2.4), color=MUTED, fontsize=9.5)
    ax.set_title("Even index — half a curve", fontsize=11, color=DEEP, pad=8)
    # cube root
    ax = axes[1]
    x = np.linspace(-8, 8, 500)
    frame(ax, (-8.4, 8.4), (-3.5, 3.5), xt=[-8, -4, 4, 8], yt=[-2, 2])
    ax.plot(x, np.cbrt(x), color=MAROON, lw=2.4, zorder=3)
    ax.plot([0], [0], "o", color=MAROON, ms=6, zorder=5)
    ax.annotate(r"$f(x)=\sqrt[3]{x}$", (1.6, 2.5), color=MAROON, fontsize=11, zorder=6,
                bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.9))
    ax.annotate("domain $(-\\infty,\\infty)$", (-7.6, -2.6), color=MUTED, fontsize=9.5)
    ax.set_title("Odd index — the whole plane", fontsize=11, color=DEEP, pad=8)
    fig.tight_layout()
    return save(fig, "g_radical_parents")


reg("g_radical_parents", radical_parents())


def radical_worked():
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    frame(ax, (-1.4, 12.4), (-2.5, 7.5), xt=[2, 4, 6, 8, 10, 12], yt=[-2, 2, 4, 6])
    x0 = np.linspace(0, 12, 400)
    ax.plot(x0, np.sqrt(x0), color=TEAL, lw=1.6, ls="--", zorder=3)
    ax.annotate(r"$f(x)=\sqrt{x}$", (8.6, 2.2), color=TEAL, fontsize=10.5, zorder=6,
                bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.9))
    x = np.linspace(3, 12, 400)
    ax.plot(x, 2 * np.sqrt(x - 3) + 1, color=MAROON, lw=2.4, zorder=4)
    ax.plot([3], [1], "o", color=MAROON, ms=6, zorder=5)
    ax.annotate(r"$g(x)=2\sqrt{x-3}+1$", (4.2, 6.4), color=MAROON, fontsize=11, zorder=6,
                bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.9))
    ax.annotate("start point $(3,\\,1)$", (3, 1), color=MAROON, fontsize=9.5,
                xytext=(8, -16), textcoords="offset points")
    fig.tight_layout()
    return save(fig, "g_radical_worked")


reg("g_radical_worked", radical_worked())


def radical_gate():
    fig, ax = plt.subplots(figsize=(5.6, 4.0))
    frame(ax, (-2.4, 10.4), (-5.5, 6.5), xt=[-2, 2, 4, 6, 8, 10], yt=[-4, -2, 2, 4, 6])
    x = np.linspace(-1, 10, 400)
    ax.plot(x, 3 * np.sqrt(x + 1) - 4, color=MAROON, lw=2.4, zorder=4)
    ax.plot([-1], [-4], "o", color=MAROON, ms=6, zorder=5)
    fig.tight_layout()
    return save(fig, "g_radical_gate")


reg("g_radical_gate", radical_gate())


# ======================================================= C · RADICAL EQUATIONS
def extraneous():
    """Why squaring creates a solution that was never there."""
    fig, ax = plt.subplots(figsize=(6.8, 4.4))
    frame(ax, (-3.4, 8.4), (-3.5, 6.5), xt=[-2, 2, 4, 6, 8], yt=[-2, 2, 4, 6])
    x = np.linspace(-5, 8, 500)
    xs = np.linspace(-5, 8, 500)
    m = xs >= -5
    ax.plot(xs[m], np.sqrt(xs[m] + 5), color=TEAL, lw=2.4, zorder=4)
    ax.annotate(r"$y=\sqrt{x+5}$", (4.6, 4.4), color=TEAL, fontsize=11, zorder=7,
                bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.9))
    ax.plot(x, x - 1, color=MAROON, lw=2.2, zorder=4)
    ax.annotate("$y=x-1$", (6.5, 5.6), color=MAROON, fontsize=11, zorder=7,
                bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.9))
    # true intersection at x = 4
    ax.plot([4], [3], "o", color=DEEP, ms=8, zorder=6)
    ax.annotate("$x=4$  they really meet", (4, 3), color=DEEP, fontsize=10,
                xytext=(10, -6), textcoords="offset points")
    # the extraneous root at x = -1
    ax.plot([-1], [2], "o", mfc="none", mec=MUTED, mew=1.6, ms=8, zorder=6)
    ax.plot([-1], [-2], "o", mfc="none", mec=MUTED, mew=1.6, ms=8, zorder=6)
    ax.plot([-1, -1], [-2, 2], color=MUTED, lw=1.0, ls=":", zorder=3)
    # At x = -1 the curve is at 2 and the line at -2, so the gap is 4, not 2.
    # The slide's own panel says "4 apart"; the label used to say 2 and the
    # slide contradicted itself.
    ax.annotate("$x=-1$  the curves are\n4 apart, not equal", (-1, -2), color=MUTED, fontsize=9.5,
                ha="left", xytext=(12, -30), textcoords="offset points")
    fig.tight_layout()
    return save(fig, "g_extraneous")


reg("g_extraneous", extraneous())


def inequality():
    fig, ax = plt.subplots(figsize=(6.6, 3.6))
    frame(ax, (-1.4, 14.4), (-1.5, 5.5), xt=[2, 4, 6, 8, 10, 12, 14], yt=[1, 2, 3, 4, 5])
    x = np.linspace(2, 14, 400)
    ax.plot(x, np.sqrt(x - 2), color=TEAL, lw=2.4, zorder=4)
    ax.annotate(r"$y=\sqrt{x-2}$", (10.6, 1.6), color=TEAL, fontsize=11, zorder=7,
                bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.9))
    ax.axhline(3, color=MAROON, lw=1.8, ls="--", zorder=3)
    ax.annotate("$y=3$", (0.4, 3.15), color=MAROON, fontsize=10.5)
    ax.plot([11], [3], "o", mfc="white", mec=MAROON, mew=2, ms=8, zorder=6)
    ax.plot([2], [0], "o", color=TEAL, ms=7, zorder=6)
    ax.plot([2, 11], [-0.75, -0.75], color=DEEP, lw=3.4, solid_capstyle="butt", zorder=5)
    ax.annotate("$2 \\leq x < 11$", (6.0, -1.35), color=DEEP, fontsize=11, ha="center")
    fig.tight_layout()
    return save(fig, "g_inequality")


reg("g_inequality", inequality())


json.dump(idx, open(os.path.join(OUT, "_index.json"), "w"), indent=1)
print(len(idx), "graphs rendered")
