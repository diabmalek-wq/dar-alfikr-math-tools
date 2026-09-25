"""The one figure this worksheet needs.

A square with a quarter circle cut from a corner. Drawn rather than described
because the GAT is a visual test: a student who has only ever met this in words
does not recognise it when it appears as a picture in the hall.
"""
import json, os, shutil
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Wedge
import figlabel as FL

plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["DejaVu Serif"]

OUT = "figs_s4"
shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT)
NAVY = "#1F3864"; INK = "#222E2D"; TEAL = "#17A199"
idx = {}

# side 14, quarter circle radius 14 from the bottom-left corner
s = 14.0
assert abs((s * s - 0.25 * (22 / 7) * s * s) - 42) < 1e-9
FL.reset()
fig, ax = plt.subplots(figsize=(2.5, 2.3))
ax.set_xlim(-7.5, 18.5); ax.set_ylim(-4.6, 17.6)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(Rectangle((0, 0), s, s, fc=TEAL, ec=NAVY, lw=1.9, alpha=0.85))
FL.record_patch_edges([(0, 0), (s, 0), (s, s), (0, s)])
ax.add_patch(Wedge((0, 0), s, 0, 90, fc="white", ec=NAVY, lw=1.6))
FL.polyline(ax, [(np.cos(t) * s, np.sin(t) * s)
                 for t in np.linspace(0, np.pi / 2, 60)], color=NAVY, lw=0.1)
FL.outside_label(ax, "14 m", (s / 2, 0), (0, -1), base=0.9, fontsize=11, name="side")
FL.place(ax, "14 m", (-4.3, s / 2), fontsize=11, name="height")
p = os.path.join(OUT, "s4_quarter.png")
fig.savefig(p, dpi=400, transparent=True, bbox_inches="tight", pad_inches=0.05)
plt.close(fig)
from PIL import Image
with Image.open(p) as im:
    idx["s4_quarter"] = {"file": p, "aspect": im.width / im.height}
json.dump(idx, open(os.path.join(OUT, "_index.json"), "w"), indent=1)
print(len(idx), "figure ->", OUT)
