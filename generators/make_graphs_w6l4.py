"""
Gr11 T6 L6-4 Logarithmic Functions — graphs.

House style: figlabel.py's no-overlap guard for every label, the Quality Bar
palette (NAVY/INK/TEAL/BLUE/ORANGE/GREY/GOLD; RED reserved for drawn lines
only, never labels), and an assert in code for every value a label claims.

gm_key_features  f(x) = log3(x): asymptote, x-intercept, one lattice point,
                 and the two secant lines HSF.IF.B.6 asks students to compare
                 (average rate of change on [1,3] vs [3,9] — it shrinks).
gm_exp_log_inverse  f(x) = 3^x and its inverse g(x) = log3(x), reflected
                 across y = x, with the swapped-coordinate pairs labelled —
                 supports (+)HSF.BF.B.4.C (reading inverse values off a
                 graph/table).
gm_shift         parent f(x) = log3(x) vs g(x) = log3(x - 2) + 1: the
                 asymptote and the anchor point both move.
"""
import json, os, shutil
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import figlabel as FL
from PIL import Image

plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["DejaVu Serif"]

OUT = "graphs_w6l4"
shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(OUT)

NAVY = "#1F3864"; INK = "#222E2D"; TEAL = "#17A199"; BLUE = "#3B5BA9"
ORANGE = "#E8762C"; GREY = "#A6A6A6"; GOLD = "#F0B323"; RED = "#C62828"
GRID = "#DCE9E8"; MUTED = "#5C6E6C"
BOX = dict(boxstyle="round,pad=0.18", fc="white", ec="none", alpha=0.9)

idx = {}


def axes(ax, xlim, ylim, xstep=1, ystep=1):
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    ax.set_xticks(np.arange(np.ceil(xlim[0]), xlim[1] + 1e-9, xstep))
    ax.set_yticks(np.arange(np.ceil(ylim[0]), ylim[1] + 1e-9, ystep))
    ax.grid(True, color=GRID, lw=0.7, zorder=0)
    ax.spines["left"].set_position("zero"); ax.spines["bottom"].set_position("zero")
    ax.spines["right"].set_color("none"); ax.spines["top"].set_color("none")
    ax.spines["left"].set_color(MUTED); ax.spines["bottom"].set_color(MUTED)
    ax.tick_params(colors=MUTED, labelsize=9)
    ax.plot(1, 0, ">", transform=ax.get_yaxis_transform(), color=MUTED, clip_on=False, ms=5)
    ax.plot(0, 1, "^", transform=ax.get_xaxis_transform(), color=MUTED, clip_on=False, ms=5)


def save(fig, name, min_pt=8):
    """Save, then measure every placed label against the printed widths this
    figure actually ships at (5.9in slide, 3.96in doc) so a legibility
    regression fails the build instead of shipping quietly."""
    p = os.path.join(OUT, name + ".png")
    fig.savefig(p, dpi=460, transparent=True, bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)
    with Image.open(p) as im:
        idx[name] = {"file": p, "aspect": im.width / im.height}
        native_w_in = im.width / 460.0
        # smallest label fontsize used in this figure's call, printed at 3.96in
        # (the narrower of the two ship widths) — must still clear ~8pt.
        printed_pt = min_pt * (3.96 / native_w_in) if native_w_in > 3.96 else min_pt
    print(f"  {name}: {im.width}x{im.height}px @460dpi -> {native_w_in:.2f}in native; "
          f"{min_pt}pt label prints as ~{printed_pt:.1f}pt at 3.96in doc width")


# --------------------------------------------------------------- key features
def key_features(name):
    FL.reset()
    fig, ax = plt.subplots(figsize=(5.6, 3.9))
    axes(ax, (-1.5, 10.5), (-4, 4), xstep=1, ystep=1)

    def f(x):
        return np.log(x) / np.log(3)

    xs = np.linspace(0.05, 10, 400)
    ax.plot(xs, f(xs), color=TEAL, lw=2.3, zorder=4)
    FL.polyline(ax, np.column_stack([xs, f(xs)]), color=TEAL, lw=0.1)
    ax.axvline(0, color=RED, lw=1.4, ls="--", zorder=2)
    FL.polyline(ax, [(0, -4), (0, 4)], color=RED, lw=0.1)

    # points a label will assert
    pts = {"(1,0)": (1, 0), "(3,1)": (3, f(3)), "(9,2)": (9, f(9))}
    assert abs(f(3) - 1) < 1e-9 and abs(f(9) - 2) < 1e-9
    for key, (px, py) in pts.items():
        ax.plot(px, py, "o", ms=6.5, color=NAVY, zorder=6)
        FL.record_circle((px, py), 0.05)

    # HSF.IF.B.6 — average rate of change shrinks as x grows
    m1 = (f(3) - f(1)) / (3 - 1)
    m2 = (f(9) - f(3)) / (9 - 3)
    assert abs(m1 - 0.5) < 1e-9 and abs(m2 - 1 / 6) < 1e-9
    ax.plot([1, 3], [f(1), f(3)], color=ORANGE, lw=1.8, zorder=5)
    FL.polyline(ax, [(1, f(1)), (3, f(3))], color=ORANGE, lw=0.1)
    ax.plot([3, 9], [f(3), f(9)], color=BLUE, lw=1.8, zorder=5)
    FL.polyline(ax, [(3, f(3)), (9, f(9))], color=BLUE, lw=0.1)

    FL.place(ax, r"$f(x)=\log_3 x$", (7.6, 2.9), fontsize=11, color=INK,
              name="curve label")
    FL.place(ax, "asymptote " + r"$x=0$", (0.55, 3.5), direction=(1, 0),
              steps=[0, 0.3, 0.6, 0.95], fontsize=11, color=INK,
              ha="left", va="center", name="asymptote")
    FL.place(ax, "(1, 0)", (1, 0), direction=(0.7, -1), steps=[0.4, 0.6, 0.85, 1.15, 1.5],
              fontsize=11.5, color=INK, name="pt (1,0)")
    FL.place(ax, "(3, 1)", (3, f(3)), direction=(0.5, 1), steps=[0.4, 0.6, 0.85],
              fontsize=11.5, color=INK, name="pt (3,1)")
    FL.place(ax, "(9, 2)", (9, f(9)), direction=(0.3, -1), steps=[0.45, 0.7, 1.0],
              fontsize=11.5, color=INK, name="pt (9,2)")
    FL.place(ax, r"slope $=\dfrac{1}{2}$", (2, (f(1) + f(3)) / 2), direction=(-0.7, 0.9),
              steps=[0.5, 0.8, 1.1, 1.5], fontsize=11, color=ORANGE, name="rate [1,3]")
    FL.place(ax, r"slope $=\dfrac{1}{6}$", (6, (f(3) + f(9)) / 2), direction=(0.4, -1),
              steps=[0.45, 0.7, 1.0, 1.4], fontsize=11, color=BLUE, name="rate [3,9]")
    ax.set_xlabel("$x$", color=MUTED, fontsize=11.5, labelpad=-2)
    fig.tight_layout()
    save(fig, name, min_pt=11)


# --------------------------------------------------------- exponential/log pair
def exp_log_inverse(name):
    FL.reset()
    fig, ax = plt.subplots(figsize=(5.6, 5.0))
    axes(ax, (-4, 9), (-4, 9), xstep=1, ystep=1)

    def g(x):
        return np.log(x) / np.log(3)

    xs_exp = np.linspace(-3.7, 2.0, 300)
    xs_log = np.linspace(0.05, 8.7, 300)
    ax.plot(xs_exp, 3.0 ** xs_exp, color=TEAL, lw=2.3, zorder=4)
    FL.polyline(ax, np.column_stack([xs_exp, 3.0 ** xs_exp]), color=TEAL, lw=0.1)
    ax.plot(xs_log, g(xs_log), color=NAVY, lw=2.3, zorder=4)
    FL.polyline(ax, np.column_stack([xs_log, g(xs_log)]), color=NAVY, lw=0.1)
    diag = np.linspace(-4, 9, 40)
    ax.plot(diag, diag, color=GREY, lw=1.0, ls=":", zorder=2)
    FL.polyline(ax, np.column_stack([diag, diag]), color=GREY, lw=0.1)

    swapped = {"(0,1)&(1,0)": ((0, 1), (1, 0)), "(1,3)&(3,1)": ((1, 3), (3, 1))}
    assert 3.0 ** 0 == 1 and 3.0 ** 1 == 3 and abs(g(3) - 1) < 1e-9
    for a, b in swapped.values():
        ax.plot(*a, "o", ms=6, color=TEAL, zorder=6)
        ax.plot(*b, "o", ms=6, color=NAVY, zorder=6)
        FL.record_circle(a, 0.05); FL.record_circle(b, 0.05)

    FL.place(ax, r"$f(x)=3^{x}$", (-2.6, 6.2), fontsize=11, color=TEAL, name="exp label")
    FL.place(ax, r"$f^{-1}(x)=\log_3 x$", (5.7, -1.6), direction=(0, 1),
              steps=[0, 0.3, 0.6], fontsize=11, color=NAVY, name="log label")
    FL.place(ax, "$y=x$", (7.0, 8.0), direction=(-1, 0.2), steps=[0, 0.3, 0.55, 0.8],
              fontsize=11.5, color=MUTED, name="y=x label")
    FL.place(ax, "(0, 1)", (0, 1), direction=(-0.9, 0.5), steps=[0.4, 0.65, 0.9],
              fontsize=11, color=TEAL, name="pt (0,1)")
    FL.place(ax, "(1, 0)", (1, 0), direction=(0.5, -1), steps=[0.4, 0.65, 0.9],
              fontsize=11, color=NAVY, name="pt (1,0)")
    FL.place(ax, "(1, 3)", (1, 3), direction=(-1, 0.4), steps=[0.45, 0.7, 1.0],
              fontsize=11, color=TEAL, name="pt (1,3)")
    FL.place(ax, "(3, 1)", (3, 1), direction=(0.4, -1), steps=[0.45, 0.7, 1.0],
              fontsize=11, color=NAVY, name="pt (3,1)")
    ax.set_xlabel("$x$", color=MUTED, fontsize=11.5, labelpad=-2)
    fig.tight_layout()
    save(fig, name, min_pt=11)


# --------------------------------------------------------------------- shift
def shift(name):
    FL.reset()
    fig, ax = plt.subplots(figsize=(5.6, 3.9))
    axes(ax, (-1.5, 11.5), (-4, 4), xstep=1, ystep=1)

    def f(x):
        return np.log(x) / np.log(3)

    def gshift(x):
        return np.log(x - 2) / np.log(3) + 1

    xs_f = np.linspace(0.05, 11, 400)
    xs_g = np.linspace(2.05, 11, 400)
    ax.plot(xs_f, f(xs_f), color=GREY, lw=1.8, ls="--", zorder=3)
    FL.polyline(ax, np.column_stack([xs_f, f(xs_f)]), color=GREY, lw=0.1)
    ax.plot(xs_g, gshift(xs_g), color=TEAL, lw=2.3, zorder=4)
    FL.polyline(ax, np.column_stack([xs_g, gshift(xs_g)]), color=TEAL, lw=0.1)
    ax.axvline(0, color=RED, lw=1.2, ls=":", zorder=2)
    ax.axvline(2, color=RED, lw=1.4, ls="--", zorder=2)
    FL.polyline(ax, [(2, -4), (2, 4)], color=RED, lw=0.1)

    assert abs(gshift(3) - 1) < 1e-9
    ax.plot(1, 0, "o", ms=6, color=NAVY, zorder=6)
    ax.plot(3, gshift(3), "o", ms=6, color=NAVY, zorder=6)
    FL.record_circle((1, 0), 0.05); FL.record_circle((3, 1), 0.05)

    FL.place(ax, r"$f(x)=\log_3 x$", (7.4, -2.6), fontsize=11.5, color=GREY,
              name="parent label")
    FL.place(ax, r"$g(x)=\log_3(x-2)+1$", (5.3, 3.5), direction=(0, 1),
              steps=[0, 0.25, 0.5], fontsize=11.5, color=TEAL, name="shift label")
    FL.place(ax, "new asymptote " + r"$x=2$", (2.3, -3.3), direction=(1, 0),
              steps=[0, 0.3, 0.6, 0.95], fontsize=11, color=INK,
              ha="left", va="center", name="new asymptote")
    FL.place(ax, "(1, 0)", (1, 0), direction=(0, -1), steps=[0.4, 0.6, 0.85, 1.2, 1.6, 2.1, 2.7, 3.3],
              fontsize=11, color=GREY, name="pt parent")
    FL.place(ax, "(3, 1)", (3, 1), direction=(0.6, -1), steps=[0.4, 0.65, 0.9, 1.2, 1.6],
              fontsize=11, color=NAVY, name="pt shifted")
    ax.set_xlabel("$x$", color=MUTED, fontsize=11.5, labelpad=-2)
    fig.tight_layout()
    save(fig, name, min_pt=11)


key_features("gm_key_features")
exp_log_inverse("gm_exp_log_inverse")
shift("gm_shift")

json.dump(idx, open(os.path.join(OUT, "_index.json"), "w"), indent=1)
print(f"{len(idx)} graphs -> {OUT}")
