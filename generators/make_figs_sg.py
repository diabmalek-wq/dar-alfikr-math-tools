"""Figures for the SAT + GAT worksheets. House style: recessive grid, arrowheads
on the axes, thin marks, direct labels, Computer Modern throughout.

The SAT half of Grade 10 Week 2 is about KEY FEATURES of a function, so the
graph has to show them honestly — a real vertex, real intercepts, and a curve
that is unmistakably a parabola rather than a decorative squiggle.
"""
import json, os, shutil
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT, DPI = "figs_sg", 400
shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT)

TEAL, TINT, MAROON, INK = "#17A199", "#CFEBE8", "#AD2A22", "#222E2D"
GRID = "#DCE9E8"
plt.rcParams.update({"mathtext.fontset": "cm", "font.family": "serif",
                     "font.serif": ["DejaVu Serif"]})

idx = {}
def save(name, fig):
    p = os.path.join(OUT, name + ".png")
    fig.savefig(p, dpi=DPI, transparent=True, bbox_inches="tight", pad_inches=0.02)
    plt.close(fig)
    from PIL import Image
    im = Image.open(p)
    idx[name] = {"file": p, "win": im.width / DPI, "hin": im.height / DPI,
                 "aspect": im.width / im.height}

def axes(ax, xlim, ylim):
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    ax.grid(True, color=GRID, lw=0.6, zorder=0)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.spines["left"].set_position("zero"); ax.spines["bottom"].set_position("zero")
    ax.spines["left"].set_color(INK); ax.spines["bottom"].set_color(INK)
    ax.spines["left"].set_linewidth(0.9); ax.spines["bottom"].set_linewidth(0.9)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False, ms=4)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False, ms=4)
    ax.set_xticks([t for t in range(xlim[0] + 1, xlim[1]) if t])
    ax.set_yticks([t for t in range(ylim[0] + 1, ylim[1]) if t])
    ax.tick_params(labelsize=9.5, colors=INK, length=2.5)

# --- g10w2 : y = x^2 - 2x - 3, vertex (1, -4), roots -1 and 3 --------------
fig, ax = plt.subplots(figsize=(3.6, 3.1))
axes(ax, (-4, 6), (-6, 8))
x = np.linspace(-2.6, 4.6, 400)
ax.plot(x, x**2 - 2*x - 3, color=TEAL, lw=1.9, zorder=3)
# The vertex and the intercepts are marked but NOT labelled — reading their
# coordinates off the grid is the skill the item is testing. Labelling them
# would hand the student the answer to three of the four questions.
ax.plot([1], [-4], "o", color=MAROON, ms=4.5, zorder=4)
ax.plot([-1, 3], [0, 0], "o", color=INK, ms=3.5, zorder=4)
ax.annotate("$y=f(x)$", (1.9, 6.1), fontsize=11, color=TEAL)
save("g10w2_graph", fig)

json.dump(idx, open(os.path.join(OUT, "_index.json"), "w"), indent=1)
print(len(idx), "figures rendered")
