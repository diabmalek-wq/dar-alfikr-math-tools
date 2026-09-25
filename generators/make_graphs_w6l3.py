"""
Gr11 T6 L6-3 Logarithms — graphs. Same house style as make_graphs_w5core.py:
recessive grid, arrowheads on axes, direct labels, Computer Modern.
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

OUT = "graphs_w6l3"
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


def log_graph(name):
    """f(x) = log2(x): vertical asymptote x=0, through (1,0) and (2,1)."""
    fig, ax = plt.subplots(figsize=(5.2, 3.6))
    axes(ax, (-1, 9), (-3, 4), xstep=1, ystep=1)
    xs = np.linspace(0.08, 8.8, 300)
    ax.plot(xs, np.log2(xs), color=TEAL, lw=2.2, zorder=4)
    ax.axvline(0, color=MAROON, lw=1.4, ls="--", zorder=2)
    ax.plot(1, 0, "o", ms=6.5, color=DEEP, zorder=6)
    ax.plot(2, 1, "o", ms=6.5, color=DEEP, zorder=6)
    ax.annotate(r"$(1,0)$", (1, 0), xytext=(6, -20), textcoords="offset points",
                color=DEEP, fontsize=9.5, bbox=BOX)
    ax.annotate(r"$(2,1)$", (2, 1), xytext=(8, 8), textcoords="offset points",
                color=DEEP, fontsize=9.5, bbox=BOX)
    ax.text(6.4, 2.6, r"$f(x)=\log_2 x$", color=TEAL, fontsize=10, bbox=BOX, ha="center")
    ax.text(0.35, 3.2, r"asymptote$\ x=0$", color=MAROON, fontsize=8.8, bbox=BOX,
            ha="left", rotation=90, va="top")
    ax.set_xlabel("$x$", color=MUTED, fontsize=9.5, labelpad=-2)
    fig.tight_layout()
    save(fig, name)


def inverse_pair(name):
    """f(x)=2^x and its inverse g(x)=log2(x), mirrored across y=x."""
    fig, ax = plt.subplots(figsize=(5.6, 4.0))
    axes(ax, (-4, 8), (-4, 8), xstep=1, ystep=1)
    xs_exp = np.linspace(-3.8, 3, 300)
    xs_log = np.linspace(0.05, 7.8, 300)
    ax.plot(xs_exp, 2 ** xs_exp, color=TEAL, lw=2.2, zorder=4)
    ax.plot(xs_log, np.log2(xs_log), color=MAROON, lw=2.2, zorder=4)
    diag = np.linspace(-4, 8, 50)
    ax.plot(diag, diag, color=MUTED, lw=1.0, ls=":", zorder=2)
    ax.plot(0, 1, "o", ms=6, color=DEEP, zorder=6)
    ax.plot(1, 0, "o", ms=6, color=DEEP, zorder=6)
    ax.text(2.2, 6.6, r"$f(x)=2^{x}$", color=TEAL, fontsize=10, bbox=BOX, ha="center")
    ax.text(6.1, 2.1, r"$f^{-1}(x)=\log_2 x$", color=MAROON, fontsize=10, bbox=BOX, ha="center")
    ax.text(5.6, 5.9, r"$y=x$", color=MUTED, fontsize=9, bbox=BOX, ha="center")
    ax.set_xlabel("$x$", color=MUTED, fontsize=9.5, labelpad=-2)
    fig.tight_layout()
    save(fig, name)


log_graph("g_log_basic")
inverse_pair("g_exp_log_inverse")

json.dump(idx, open(os.path.join(OUT, "_index.json"), "w"), indent=1)
print(f"{len(idx)} graphs -> {OUT}")
