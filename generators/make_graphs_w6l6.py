"""
Week 8 graphs — Grade 11 Topic 6 Lesson 6-6, "Exponential and Logarithmic
Equations and Inequalities". House style: recessive grid, arrowheads on
axes, thin marks, direct labels, Computer Modern. Every label placed
explicitly, and every picture asserts the numbers the slide states.

  A · Gr11 T6 L6-6  Exponential and Logarithmic Equations and Inequalities
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

OUT = "graphs_w6l6"
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


# =============================================== A · Gr11 T6 L6-6
def flip(name):
    """(1/2)^x < 8: a DECREASING curve crossing y=8 at x=-3; the inequality
    solution x>-3 is where the curve sits BELOW the horizontal target line."""
    f = lambda x: 0.5 ** x
    assert abs(f(-3) - 8) < 1e-9
    fig, ax = plt.subplots(figsize=(5.4, 3.8))
    axes(ax, (-4.4, 3.2), (-2, 16), xstep=1, ystep=2)
    xs = np.linspace(-4.3, 3.1, 300)
    xr = np.linspace(-3, 3.1, 150)
    ax.fill_between(xr, 0, f(xr), color=TEAL, alpha=0.18, zorder=1)
    ax.axhline(8, color=MAROON, lw=1.6, ls=(0, (6, 4)), zorder=3)
    ax.plot(xs, f(xs), color=TEAL, lw=2.3, zorder=4)
    ax.plot(-3, 8, "o", ms=7, color=DEEP, zorder=6)
    ax.annotate("$(-3,8)$", (-3, 8), xytext=(10, 10), textcoords="offset points",
                color=DEEP, fontsize=9.5, bbox=BOX)
    ax.text(-3.2, 13.4, r"$f(x)=\left(\frac{1}{2}\right)^{x}$", color=TEAL,
            fontsize=10, bbox=BOX, ha="center")
    ax.text(1.7, 8.9, r"$y=8$", color=MAROON, fontsize=10, bbox=BOX, ha="center")
    ax.text(1.2, 3.2, r"$f(x)<8$" + "\n" + r"for $x>-3$", color=DEEP,
            fontsize=9, bbox=BOX, ha="center")
    ax.set_xlabel("$x$", color=MUTED, fontsize=9.5, labelpad=-2)
    fig.tight_layout()
    save(fig, name)


def emissions(name):
    """E(t) = 500,000(0.9)^t crossing the 250,000-ton half-target at
    t = log(0.5)/log(0.9) ~= 6.58 years."""
    E0 = 500_000
    f = lambda t: E0 * 0.9 ** t
    t_half = np.log(0.5) / np.log(0.9)
    assert abs(f(t_half) - 250_000) < 1
    fig, ax = plt.subplots(figsize=(5.6, 3.9))
    ax.set_xlim(0, 15); ax.set_ylim(0, 550_000)
    ax.set_xticks(np.arange(0, 16, 2))
    ax.set_yticks(np.arange(0, 550_001, 100_000))
    ax.grid(True, color=GRID, lw=0.7, zorder=0)
    ax.spines["right"].set_color("none"); ax.spines["top"].set_color("none")
    ax.spines["left"].set_color(MUTED); ax.spines["bottom"].set_color(MUTED)
    ax.tick_params(colors=MUTED, labelsize=8)
    ts = np.linspace(0, 15, 300)
    ax.axhline(250_000, color=MAROON, lw=1.6, ls=(0, (6, 4)), zorder=3)
    ax.plot(ts, f(ts), color=TEAL, lw=2.3, zorder=4)
    ax.plot(t_half, 250_000, "o", ms=7, color=DEEP, zorder=6)
    ax.annotate(r"$t\approx 6.58$", (t_half, 250_000), xytext=(10, 22),
                textcoords="offset points", color=DEEP, fontsize=9.5, bbox=BOX)
    ax.text(2.2, 460_000, r"$E(t)=500{,}000(0.9)^{t}$", color=TEAL,
            fontsize=10, bbox=BOX, ha="center")
    ax.text(11.5, 280_000, "half-target\n250,000 t", color=MAROON,
            fontsize=9, bbox=BOX, ha="center")
    ax.set_xlabel("years from now ($t$)", color=MUTED, fontsize=9.5, labelpad=-2)
    ax.set_ylabel("emissions (metric tons CO$_2$)", color=MUTED, fontsize=9)
    fig.tight_layout()
    save(fig, name)


flip("g_flip")
emissions("g_emissions")

json.dump(idx, open(os.path.join(OUT, "_index.json"), "w"), indent=1)
for k, v in idx.items():
    print(f"{k:18s} aspect {v['aspect']:.2f}")
