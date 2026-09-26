"""
Gr11 T6 L6-5 Properties of Logarithms — graph.

House style: figlabel.py's no-overlap guard for every label, the Quality Bar
palette (NAVY/INK/TEAL/BLUE/ORANGE/GREY/GOLD; RED reserved for drawn lines
only, never labels), and an assert in code for every value a label claims.

gm_growth  a_n = 40(1.12)^(n-1), a geometric-growth model (HSF.BF.A.2) for a
           solar plant's capacity in MW. Marks the target line at 100 MW and
           the point where the curve crosses it — the value change of base
           (HSF.LE.A.4) is used in instruction 3 to solve for.
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

OUT = "graphs_w6l5"
shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(OUT)

NAVY = "#1F3864"; INK = "#222E2D"; TEAL = "#17A199"; BLUE = "#3B5BA9"
ORANGE = "#E8762C"; GREY = "#A6A6A6"; GOLD = "#F0B323"; RED = "#C62828"
GRID = "#DCE9E8"; MUTED = "#5C6E6C"

idx = {}


def axes(ax, xlim, ylim, xstep=1, ystep=20):
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    ax.set_xticks(np.arange(np.ceil(xlim[0]), xlim[1] + 1e-9, xstep))
    ax.set_yticks(np.arange(0, ylim[1] + 1e-9, ystep))
    ax.grid(True, color=GRID, lw=0.7, zorder=0)
    ax.spines["left"].set_position("zero"); ax.spines["bottom"].set_position(("data", 0))
    ax.spines["right"].set_color("none"); ax.spines["top"].set_color("none")
    ax.spines["left"].set_color(MUTED); ax.spines["bottom"].set_color(MUTED)
    ax.tick_params(colors=MUTED, labelsize=9)
    ax.plot(1, 0, ">", transform=ax.get_yaxis_transform(), color=MUTED, clip_on=False, ms=5)
    ax.plot(0, 1, "^", transform=ax.get_xaxis_transform(), color=MUTED, clip_on=False, ms=5)


def save(fig, name, min_pt=8):
    p = os.path.join(OUT, name + ".png")
    fig.savefig(p, dpi=460, transparent=True, bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)
    with Image.open(p) as im:
        idx[name] = {"file": p, "aspect": im.width / im.height}
        native_w_in = im.width / 460.0
        printed_pt = min_pt * (3.96 / native_w_in) if native_w_in > 3.96 else min_pt
    print(f"  {name}: {im.width}x{im.height}px @460dpi -> {native_w_in:.2f}in native; "
          f"{min_pt}pt label prints as ~{printed_pt:.1f}pt at 3.96in doc width")


def growth(name):
    FL.reset()
    fig, ax = plt.subplots(figsize=(5.6, 3.9))
    axes(ax, (-0.5, 11.5), (0, 140), xstep=1, ystep=20)

    def a(n):
        return 40 * (1.12 ** (n - 1))

    # discrete geometric sequence (bars would clutter; use markers + a smooth
    # guide curve through them so the "target crossing" reads at a glance)
    ns = np.arange(1, 11)
    vals = a(ns)
    ns_smooth = np.linspace(1, 11, 300)
    ax.plot(ns_smooth, a(ns_smooth), color=GREY, lw=1.4, ls=":", zorder=2)
    ax.plot(ns, vals, "o", ms=6, color=TEAL, zorder=5)
    for n, v in zip(ns, vals):
        FL.record_circle((n, v), 0.18)

    # target line at 100 MW
    ax.axhline(100, color=RED, lw=1.4, ls="--", zorder=3)
    FL.polyline(ax, [(-0.5, 100), (11.5, 100)], color=RED, lw=0.1)

    # solved crossing point, from m_geo_solve: n ~= 9.09
    n_star = 1 + np.log(2.5) / np.log(1.12)
    assert abs(n_star - 9.0852) < 1e-3
    a_star = a(n_star)
    assert abs(a_star - 100) < 1e-6
    ax.plot(n_star, a_star, "o", ms=7, color=NAVY, zorder=6)
    FL.record_circle((n_star, a_star), 0.2)
    ax.plot([n_star, n_star], [0, a_star], color=NAVY, lw=1.0, ls=":", zorder=2)
    FL.polyline(ax, [(n_star, 0), (n_star, a_star)], color=NAVY, lw=0.1)

    FL.place(ax, r"$a_n = 40(1.12)^{\,n-1}$", (5.3, 128), fontsize=11.5,
              color=TEAL, name="model label")
    FL.place(ax, "target 100 MW", (1.8, 100), direction=(0, 1), steps=[0.5, 1.0, 2.0, 3.0],
              fontsize=11, color=INK, ha="left", va="bottom", name="target label")
    FL.place(ax, r"$n\approx 9.09$", (n_star, 10), direction=(1, 0.2),
              steps=[0.3, 0.6, 0.9, 1.3], fontsize=11, color=NAVY, ha="left", name="n label")
    FL.place(ax, "(1, 40)", (1, 40), direction=(1, 1), steps=[0.6, 1.0, 1.5, 2.2],
              fontsize=10.5, color=TEAL, ha="left", name="pt (1,40)")
    ax.set_xlabel("year $n$", color=MUTED, fontsize=11.5, labelpad=2)
    ax.set_ylabel("capacity (MW)", color=MUTED, fontsize=11, labelpad=2)
    fig.tight_layout()
    save(fig, name, min_pt=11)


growth("gm_growth")

json.dump(idx, open(os.path.join(OUT, "_index.json"), "w"), indent=1)
print(f"{len(idx)} graphs -> {OUT}")
