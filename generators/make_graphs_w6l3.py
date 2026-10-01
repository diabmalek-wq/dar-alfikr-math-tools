"""Gr11 T6 L6-3 Logarithms — graphs (rebuilt to Quality Bar 22b).
figlabel guards every label; palette fixed; labels INK; RED only for drawn lines;
answer assertions in code; legibility measured (label pt x printed width / image width >= 8 pt).
"""
import json, os, shutil
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image
import figlabel as fl

plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["DejaVu Serif"]

OUT = "graphs_w6l3"
shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT)
NAVY, INK, TEAL, BLUE, ORANGE, GREY, GOLD, RED = "#1F3864", "#222E2D", "#17A199", "#3B5BA9", "#E8762C", "#A6A6A6", "#F0B323", "#C62828"
GRID = "#DCE9E8"
idx = {}
PRINTED_W = {"g_log_basic": 6.0, "g_exp_log_inverse": 5.9}   # inches on the slide
FONT_MIN_PT = 8.0


def axes(ax, xlim, ylim):
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    ax.set_xticks(np.arange(np.ceil(xlim[0]), xlim[1] + 1e-9, 1))
    ax.set_yticks(np.arange(np.ceil(ylim[0]), ylim[1] + 1e-9, 1))
    ax.grid(True, color=GRID, lw=0.7, zorder=0)
    for s in ("right", "top"): ax.spines[s].set_color("none")
    ax.spines["left"].set_position("zero"); ax.spines["bottom"].set_position("zero")
    for s in ("left", "bottom"): ax.spines[s].set_color(GREY)
    ax.tick_params(colors=INK, labelsize=9)
    ax.plot(1, 0, ">", transform=ax.get_yaxis_transform(), color=GREY, clip_on=False, ms=5)
    ax.plot(0, 1, "^", transform=ax.get_xaxis_transform(), color=GREY, clip_on=False, ms=5)
    # record axes so labels never sit on them
    fl.polyline(ax, [(xlim[0], 0), (xlim[1], 0)], lw=0)
    fl.polyline(ax, [(0, ylim[0]), (0, ylim[1])], lw=0)


def save(fig, name, figw):
    p = os.path.join(OUT, name + ".png")
    fig.savefig(p, dpi=460, transparent=True, bbox_inches="tight", pad_inches=0.04)
    plt.close(fig)
    with Image.open(p) as im:
        wpx = im.width / 460
    printed = PRINTED_W[name]
    eff = 9.0 * printed / wpx
    assert eff >= FONT_MIN_PT, f"{name}: smallest label prints at {eff:.1f} pt (< {FONT_MIN_PT})"
    with Image.open(p) as im:
        idx[name] = {"file": p, "aspect": im.width / im.height, "min_label_pt": round(eff, 1)}


def log_graph(name):
    fl.reset()
    fig, ax = plt.subplots(figsize=(5.2, 3.7))
    axes(ax, (-1.5, 9.5), (-3.5, 4.5))
    xs = np.linspace(0.07, 9.3, 400); ys = np.log2(xs)
    ax.plot(xs, ys, color=TEAL, lw=2.4, zorder=4)
    fl.polyline(ax, np.column_stack([xs, ys]), lw=0)
    ax.plot([0, 0], [-3.5, 4.5], color=RED, lw=1.5, ls="--", zorder=3)   # drawn line: asymptote
    # assert the answers the slide text states
    for (x, y) in [(1, 0), (2, 1), (4, 2), (8, 3)]:
        assert abs(np.log2(x) - y) < 1e-12
        ax.plot(x, y, "o", ms=6.5, color=NAVY, zorder=6)
    fl.place(ax, r"$(1,0)$", (1, 0), direction=(1, -1), steps=(0.9, 1.2, 1.6), fontsize=9.5, color=INK, name="p10")
    fl.place(ax, r"$(2,1)$", (2, 1), direction=(1, -1), steps=(0.9, 1.2, 1.6), fontsize=9.5, color=INK, name="p21")
    fl.place(ax, r"$(4,2)$", (4, 2), direction=(1, -1), steps=(0.9, 1.2, 1.6), fontsize=9.5, color=INK, name="p42")
    fl.place(ax, r"$(8,3)$", (8, 3), direction=(-0.3, -1), steps=(0.8, 1.1, 1.5), fontsize=9.5, color=INK, name="p83")
    fl.place(ax, r"$f(x)=\log_2 x$", (7.0, 1.6), direction=(0, -1), steps=(0.2, 0.5, 0.9), fontsize=10.5, color=INK, name="curve")
    fl.place(ax, r"asymptote $x=0$", (0, 3.9), direction=(1, 0), steps=(1.7, 2.0, 2.4), fontsize=9.5, color=INK, name="asym")
    ax.set_xlabel("$x$", color=INK, fontsize=10, labelpad=-2)
    ax.set_ylabel("$y$", color=INK, fontsize=10, rotation=0, labelpad=-4)
    fig.tight_layout(); save(fig, name, 5.2)


def inverse_pair(name):
    fl.reset()
    fig, ax = plt.subplots(figsize=(5.6, 4.1))
    axes(ax, (-3.5, 8.5), (-3.5, 8.5))
    xe = np.linspace(-3.4, 3.05, 400); ye = 2.0 ** xe
    xl = np.linspace(0.09, 8.4, 400); yl = np.log2(xl)
    ax.plot(xe, ye, color=TEAL, lw=2.4, zorder=4); fl.polyline(ax, np.column_stack([xe, ye]), lw=0)
    ax.plot(xl, yl, color=ORANGE, lw=2.4, zorder=4); fl.polyline(ax, np.column_stack([xl, yl]), lw=0)
    d = np.array([-3.5, 8.5])
    ax.plot(d, d, color=GREY, lw=1.2, ls=":", zorder=2); fl.polyline(ax, np.column_stack([d, d]), lw=0)
    pairs = [((0, 1), (1, 0)), ((1, 2), (2, 1)), ((2, 4), (4, 2))]
    for (a, b), (c, e) in pairs:
        assert 2 ** a == b and np.log2(c) == e and (a, b) == (e, c)     # reflection across y = x
        ax.plot(a, b, "o", ms=6, color=NAVY, zorder=6); ax.plot(c, e, "o", ms=6, color=NAVY, zorder=6)
        ax.plot([a, c], [b, e], color=GREY, lw=0.8, ls="--", zorder=3)
        fl.polyline(ax, [(a, b), (c, e)], lw=0)
    fl.place(ax, r"$f(x)=2^{x}$", (-1.0, 3.2), direction=(0, 1), steps=(0.3, 0.8, 1.4), fontsize=10.5, color=INK, name="exp")
    fl.place(ax, r"$g(x)=\log_2 x$", (7.2, 1.7), direction=(0, -1), steps=(0.2, 0.5, 0.9), fontsize=10.5, color=INK, name="log")
    fl.place(ax, r"$y=x$", (6.6, 6.6), direction=(-1, 1), steps=(0.7, 1.0, 1.4), fontsize=10, color=INK, name="diag")
    ax.set_xlabel("$x$", color=INK, fontsize=10, labelpad=-2)
    ax.set_ylabel("$y$", color=INK, fontsize=10, rotation=0, labelpad=-4)
    fig.tight_layout(); save(fig, name, 5.6)


log_graph("g_log_basic")
inverse_pair("g_exp_log_inverse")
json.dump(idx, open(os.path.join(OUT, "_index.json"), "w"), indent=1)
print(idx)
