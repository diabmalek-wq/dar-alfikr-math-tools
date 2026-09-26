"""
Week 6 graphs — Grade 10 Topic 1 Lesson 6, "Linear Systems". House style:
recessive grid, arrowheads on axes, thin marks, direct labels, Computer
Modern. Every label placed explicitly, and every picture asserts the
numbers the slide/doc states.

  A · Gr10 T1 L6  Linear Systems
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

OUT = "graphs_w6"
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


# =============================================== A · Gr10 T1 L6
def sys_one(name):
    """y = 2x - 1 and y = -x + 5, meeting at (2, 3) — ONE solution."""
    f = lambda x: 2 * x - 1
    g = lambda x: -x + 5
    assert f(2) == 3 and g(2) == 3
    fig, ax = plt.subplots(figsize=(5.2, 3.6))
    axes(ax, (-1, 6), (-3, 12), xstep=1, ystep=2)
    xs = np.linspace(-0.8, 5.8, 200)
    ax.plot(xs, f(xs), color=TEAL, lw=2.2, zorder=4)
    ax.plot(xs, g(xs), color=MAROON, lw=2.2, zorder=4)
    ax.plot(2, 3, "o", ms=7, color=DEEP, zorder=6)
    ax.annotate("$(2,3)$", (2, 3), xytext=(-58, -22), textcoords="offset points",
                color=DEEP, fontsize=10, bbox=BOX)
    ax.text(1.15, 9.6, r"$y=2x-1$", color=TEAL, fontsize=10, bbox=BOX, ha="center")
    ax.text(4.3, 2.2, r"$y=-x+5$", color=MAROON, fontsize=10, bbox=BOX, ha="center")
    ax.set_xlabel("$x$", color=MUTED, fontsize=9.5, labelpad=-2)
    fig.tight_layout()
    save(fig, name)


def sys_ineq(name):
    """y <= -x + 6 (solid) and y > 2x - 1 (dashed); overlap shaded, with
    (0, 3) marked inside and (4, 4) marked outside the feasible region."""
    f = lambda x: -x + 6
    g = lambda x: 2 * x - 1
    fig, ax = plt.subplots(figsize=(5.4, 3.8))
    axes(ax, (-1, 6), (-3, 10), xstep=1, ystep=2)
    xs = np.linspace(-0.8, 5.8, 200)
    # overlap: below f(x) and above g(x)
    x_cross = 7 / 3  # f(x) = g(x) -> -x+6 = 2x-1 -> x = 7/3
    xr = np.linspace(-0.8, x_cross, 100)
    ax.fill_between(xr, g(xr), f(xr), color=TEAL, alpha=0.18, zorder=1)
    ax.plot(xs, f(xs), color=TEAL, lw=2.2, zorder=4)
    ax.plot(xs, g(xs), color=MAROON, lw=2.2, ls=(0, (6, 4)), zorder=4)
    ax.plot(0, 3, "o", ms=7, color=DEEP, zorder=6)
    ax.annotate("$(0,3)$ — feasible", (0, 3), xytext=(10, 14), textcoords="offset points",
                color=DEEP, fontsize=9.5, bbox=BOX)
    ax.plot(4, 4, "x", ms=9, mew=2.2, color=MAROON, zorder=6)
    ax.annotate("$(4,4)$ — not feasible", (4, 4), xytext=(8, -30), textcoords="offset points",
                color=MAROON, fontsize=9.5, bbox=BOX)
    ax.text(1.0, 8.6, r"$y\leq -x+6$", color=TEAL, fontsize=10, bbox=BOX, ha="center")
    ax.text(4.35, -2.2, r"$y> 2x-1$", color=MAROON, fontsize=10, bbox=BOX, ha="center")
    ax.set_xlabel("$x$", color=MUTED, fontsize=9.5, labelpad=-2)
    fig.tight_layout()
    save(fig, name)


def gate_sys(name):
    """x + y = 7 and 2x - y = 2, meeting at (3, 4) — Mastery Gate graph."""
    f = lambda x: 7 - x
    g = lambda x: 2 * x - 2
    assert f(3) == 4 and g(3) == 4
    fig, ax = plt.subplots(figsize=(4.6, 3.6))
    axes(ax, (-1, 6), (-3, 10), xstep=1, ystep=2)
    xs = np.linspace(-0.8, 5.8, 200)
    ax.plot(xs, f(xs), color=TEAL, lw=2.2, zorder=4)
    ax.plot(xs, g(xs), color=MAROON, lw=2.2, zorder=4)
    ax.plot(3, 4, "o", ms=7, color=DEEP, zorder=6)
    ax.text(1.1, 8.3, r"$x+y=7$", color=TEAL, fontsize=9.5, bbox=BOX, ha="center")
    ax.text(4.5, 1.0, r"$2x-y=2$", color=MAROON, fontsize=9.5, bbox=BOX, ha="center")
    ax.set_xlabel("$x$", color=MUTED, fontsize=9.5, labelpad=-2)
    fig.tight_layout()
    save(fig, name)


def cw_sys(name):
    """y = x + 4 and y = -3x + 8, meeting at (1, 5) — classwork Section C."""
    f = lambda x: x + 4
    g = lambda x: -3 * x + 8
    assert f(1) == 5 and g(1) == 5
    fig, ax = plt.subplots(figsize=(4.6, 3.6))
    axes(ax, (-2, 4), (-2, 12), xstep=1, ystep=2)
    xs = np.linspace(-1.8, 3.8, 200)
    ax.plot(xs, f(xs), color=TEAL, lw=2.2, zorder=4)
    ax.plot(xs, g(xs), color=MAROON, lw=2.2, zorder=4)
    ax.plot(1, 5, "o", ms=7, color=DEEP, zorder=6)
    ax.text(-0.9, 9.6, r"$y=x+4$", color=TEAL, fontsize=9.5, bbox=BOX, ha="center")
    ax.text(2.3, 9.6, r"$y=-3x+8$", color=MAROON, fontsize=9.5, bbox=BOX, ha="center")
    ax.set_xlabel("$x$", color=MUTED, fontsize=9.5, labelpad=-2)
    fig.tight_layout()
    save(fig, name)


def cw_poster(name):
    """Poster/bookmark fundraiser: 7p + 3b >= 210 and p + b <= 40, in the
    p-b plane. (20, 15) marked outside the feasible region, (30, 10) marked
    inside."""
    revenue = lambda p: (210 - 7 * p) / 3   # boundary of 7p + 3b = 210
    items = lambda p: 40 - p                # boundary of p + b = 40
    assert 7 * 20 + 3 * 15 < 210            # (20, 15) fails the revenue line
    assert 20 + 15 <= 40
    assert 7 * 30 + 3 * 10 >= 210 and 30 + 10 <= 40   # (30, 10) is feasible
    fig, ax = plt.subplots(figsize=(5.0, 4.0))
    axes(ax, (0, 42), (0, 72), xstep=5, ystep=10, grid=True)
    ps = np.linspace(0, 40, 200)
    rev = revenue(ps)
    itm = np.maximum(items(ps), 0)
    lo = np.maximum(rev, 0)
    hi = itm
    mask = lo <= hi
    ax.fill_between(ps[mask], lo[mask], hi[mask], color=TEAL, alpha=0.18, zorder=1)
    ax.plot(ps, np.clip(rev, 0, 72), color=TEAL, lw=2.2, zorder=4)
    ax.plot(ps, itm, color=MAROON, lw=2.2, zorder=4)
    ax.plot(20, 15, "x", ms=9, mew=2.2, color=MAROON, zorder=6)
    ax.annotate("$(20,15)$ — not feasible", xy=(20, 15), xytext=(2, 56), textcoords="data",
                color=MAROON, fontsize=9, bbox=BOX, ha="left",
                arrowprops=dict(arrowstyle="->", color=MAROON, lw=1))
    ax.plot(30, 10, "o", ms=7, color=DEEP, zorder=6)
    ax.annotate("$(30,10)$ — feasible", xy=(30, 10), xytext=(23, 46), textcoords="data",
                color=DEEP, fontsize=9, bbox=BOX, ha="left",
                arrowprops=dict(arrowstyle="->", color=DEEP, lw=1))
    ax.text(8, 62, r"$7p+3b=210$", color=TEAL, fontsize=9.5, bbox=BOX, ha="center")
    ax.text(32, 26, r"$p+b=40$", color=MAROON, fontsize=9.5, bbox=BOX, ha="center")
    ax.set_xlabel("posters ($p$)", color=MUTED, fontsize=9.5, labelpad=-2)
    ax.set_ylabel("bookmarks ($b$)", color=MUTED, fontsize=9.5)
    fig.tight_layout()
    save(fig, name)


sys_one("g_sys_one")
sys_ineq("g_sys_ineq")
gate_sys("g_gate_sys")
cw_sys("g_cw_sys")
cw_poster("g_cw_poster")

json.dump(idx, open(os.path.join(OUT, "_index.json"), "w"), indent=1)
for k, v in idx.items():
    print(f"{k:18s} aspect {v['aspect']:.2f}")
