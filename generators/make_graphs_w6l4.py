"""
Gr11 T6 L6-4 Logarithmic Functions — graphs. Same house style as
make_graphs_w6l3.py: recessive grid, arrowheads on axes, direct labels,
Computer Modern. Prefix gm_.
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

OUT = "graphs_w6l4"
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


def key_features(name):
    """f(x) = log3(x): key features labelled — x-intercept, asymptote, domain."""
    fig, ax = plt.subplots(figsize=(5.4, 3.8))
    axes(ax, (-2, 9), (-3, 4), xstep=1, ystep=1)
    xs = np.linspace(0.05, 8.8, 300)
    ax.plot(xs, np.log(xs) / np.log(3), color=TEAL, lw=2.2, zorder=4)
    ax.axvline(0, color=MAROON, lw=1.4, ls="--", zorder=2)
    ax.plot(1, 0, "o", ms=6.5, color=DEEP, zorder=6)
    ax.annotate(r"$(1,0)$" + "\n" + "$x$-intercept", (1, 0), xytext=(10, -34),
                textcoords="offset points", color=DEEP, fontsize=8.8, bbox=BOX)
    ax.annotate(r"$(3,1)$", (3, 1), xytext=(8, 8), textcoords="offset points",
                color=DEEP, fontsize=9, bbox=BOX)
    ax.plot(3, 1, "o", ms=6, color=DEEP, zorder=6)
    ax.text(6.2, 2.6, r"$f(x)=\log_3 x$", color=TEAL, fontsize=10, bbox=BOX, ha="center")
    ax.text(0.35, 3.2, r"asymptote$\ x=0$", color=MAROON, fontsize=8.6, bbox=BOX,
            ha="left", rotation=90, va="top")
    ax.text(4.8, -2.4, "domain: $x>0$", color=MUTED, fontsize=8.8, bbox=BOX, ha="center")
    ax.set_xlabel("$x$", color=MUTED, fontsize=9.5, labelpad=-2)
    fig.tight_layout()
    save(fig, name)


def inverse_pair(name):
    """f(x)=3^x and its inverse g(x)=log3(x), mirrored across y=x."""
    fig, ax = plt.subplots(figsize=(5.6, 4.0))
    axes(ax, (-4, 8), (-4, 8), xstep=1, ystep=1)
    xs_exp = np.linspace(-3.8, 2, 300)
    xs_log = np.linspace(0.05, 7.8, 300)
    ax.plot(xs_exp, 3 ** xs_exp, color=TEAL, lw=2.2, zorder=4)
    ax.plot(xs_log, np.log(xs_log) / np.log(3), color=MAROON, lw=2.2, zorder=4)
    diag = np.linspace(-4, 8, 50)
    ax.plot(diag, diag, color=MUTED, lw=1.0, ls=":", zorder=2)
    ax.plot(0, 1, "o", ms=6, color=DEEP, zorder=6)
    ax.plot(1, 0, "o", ms=6, color=DEEP, zorder=6)
    ax.text(1.9, 6.6, r"$f(x)=3^{x}$", color=TEAL, fontsize=10, bbox=BOX, ha="center")
    ax.text(6.0, 1.9, r"$f^{-1}(x)=\log_3 x$", color=MAROON, fontsize=10, bbox=BOX, ha="center")
    ax.text(5.5, 6.0, r"$y=x$", color=MUTED, fontsize=9, bbox=BOX, ha="center")
    ax.set_xlabel("$x$", color=MUTED, fontsize=9.5, labelpad=-2)
    fig.tight_layout()
    save(fig, name)


def shift_transform(name):
    """g(x) = log2(x - 3): asymptote shifted to x = 3, vs parent f(x) = log2(x)."""
    fig, ax = plt.subplots(figsize=(5.4, 3.8))
    axes(ax, (-2, 11), (-3, 4), xstep=1, ystep=1)
    xs1 = np.linspace(0.05, 10.8, 300)
    xs2 = np.linspace(3.05, 10.8, 300)
    ax.plot(xs1, np.log2(xs1), color=MUTED, lw=1.8, ls="--", zorder=3)
    ax.plot(xs2, np.log2(xs2 - 3), color=TEAL, lw=2.2, zorder=4)
    ax.axvline(0, color=MUTED, lw=1.1, ls=":", zorder=2)
    ax.axvline(3, color=MAROON, lw=1.4, ls="--", zorder=2)
    ax.text(6.6, 2.7, r"$g(x)=\log_2(x-3)$", color=TEAL, fontsize=9.6, bbox=BOX, ha="center")
    ax.text(7.6, -2.0, r"$f(x)=\log_2 x$", color=MUTED, fontsize=9, bbox=BOX, ha="center")
    ax.text(3.35, 3.2, r"asymptote$\ x=3$", color=MAROON, fontsize=8.4, bbox=BOX,
            ha="left", rotation=90, va="top")
    ax.set_xlabel("$x$", color=MUTED, fontsize=9.5, labelpad=-2)
    fig.tight_layout()
    save(fig, name)


key_features("gm_key_features")
inverse_pair("gm_exp_log_inverse")
shift_transform("gm_shift")

json.dump(idx, open(os.path.join(OUT, "_index.json"), "w"), indent=1)
print(f"{len(idx)} graphs -> {OUT}")
