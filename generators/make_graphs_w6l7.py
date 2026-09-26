"""
Week 9 graphs — Grade 11 Topic 6 Lesson 6-7, "Geometric Sequences and
Series". House style: recessive grid, arrowheads on axes, thin marks,
direct labels, Computer Modern. Every label placed explicitly, and every
picture asserts the numbers the slide states.

  A · Gr11 T6 L6-7  Geometric Sequences and Series
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

OUT = "graphs_w6l7"
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


# =============================================== A · Gr11 T6 L6-7
def geo_seq(name):
    """The sequence 3, 6, 12, 24, 48 (n=1..5) sitting exactly on the
    continuous curve y = 3(2)^(x-1) — a geometric sequence is a discrete
    exponential function."""
    a1, r = 3, 2
    terms = [a1 * r ** (n - 1) for n in range(1, 6)]
    assert terms == [3, 6, 12, 24, 48]
    f = lambda x: a1 * r ** (x - 1)
    fig, ax = plt.subplots(figsize=(5.4, 3.8))
    axes(ax, (0, 6), (-4, 52), xstep=1, ystep=8)
    xs = np.linspace(0.3, 5.7, 200)
    ax.plot(xs, f(xs), color=TEAL, lw=1.8, ls=(0, (5, 4)), zorder=3)
    ns = list(range(1, 6))
    for n, v in zip(ns, terms):
        ax.plot([n, n], [0, v], color=MUTED, lw=0.9, zorder=2)
    ax.plot(ns, terms, "o", ms=8, color=DEEP, zorder=6)
    for n, v in zip(ns, terms):
        ax.annotate(f"${v}$", (n, v), xytext=(0, 9), textcoords="offset points",
                    color=DEEP, fontsize=9.5, ha="center")
    ax.text(1.35, 44, r"$y=3(2)^{x-1}$", color=TEAL, fontsize=10, bbox=BOX, ha="center")
    ax.set_xlabel("term number $n$", color=MUTED, fontsize=9.5, labelpad=-2)
    ax.set_ylabel("$a_n$", color=MUTED, fontsize=10)
    fig.tight_layout()
    save(fig, name)


def geo_series(name):
    """Waqf donation drive: a1=10,000 SAR, r=1.2, 5 years. Bars are each
    year's donation; the annotated running total is the partial sum."""
    a1, r, n = 10_000, 1.2, 5
    terms = [a1 * r ** (k - 1) for k in range(1, n + 1)]
    cum = np.cumsum(terms)
    assert abs(cum[-1] - 74_416) < 1
    fig, ax = plt.subplots(figsize=(5.6, 3.9))
    ax.set_xlim(0.3, 5.7); ax.set_ylim(0, 24_000)
    ax.set_xticks(range(1, 6))
    ax.set_yticks(np.arange(0, 24_001, 4_000))
    ax.grid(True, axis="y", color=GRID, lw=0.7, zorder=0)
    ax.spines["right"].set_color("none"); ax.spines["top"].set_color("none")
    ax.spines["left"].set_color(MUTED); ax.spines["bottom"].set_color(MUTED)
    ax.tick_params(colors=MUTED, labelsize=8)
    ax.bar(range(1, 6), terms, color=TEAL, width=0.55, zorder=3)
    for k, (v, c) in enumerate(zip(terms, cum), start=1):
        ax.text(k, v + 500, f"{v:,.0f}", color=DEEP, fontsize=8.5, ha="center")
        ax.text(k, v + 1650, f"total {c:,.0f}", color=MAROON, fontsize=7.8, ha="center")
    ax.set_xlabel("year ($k$)", color=MUTED, fontsize=9.5, labelpad=-2)
    ax.set_ylabel("that year's donation (SAR)", color=MUTED, fontsize=9)
    fig.tight_layout()
    save(fig, name)


geo_seq("g_geo_seq")
geo_series("g_geo_series")

json.dump(idx, open(os.path.join(OUT, "_index.json"), "w"), indent=1)
for k, v in idx.items():
    print(f"{k:18s} aspect {v['aspect']:.2f}")
