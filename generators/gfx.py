"""Shared figure helpers (Quality Bar 22b): fixed palette, recorded axes, legibility asserted."""
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
NAVY, INK, TEAL, BLUE, ORANGE, GREY, GOLD, RED = "#1F3864", "#222E2D", "#17A199", "#3B5BA9", "#E8762C", "#A6A6A6", "#F0B323", "#C62828"
GRID = "#DCE9E8"
FONT_MIN_PT = 8.0
BASE_FONT = 10.5

class Set:
    def __init__(self, out, printed):
        self.out, self.printed, self.idx = out, printed, {}
        shutil.rmtree(out, ignore_errors=True); os.makedirs(out)

    def fig(self, w, h):
        fl.reset()
        return plt.subplots(figsize=(w, h))

    def axes(self, ax, xlim, ylim, xstep=1, ystep=1, equal=False):
        ax.set_xlim(*xlim); ax.set_ylim(*ylim)
        ax.set_xticks(np.arange(np.ceil(xlim[0] / xstep) * xstep, xlim[1] + 1e-9, xstep))
        ax.set_yticks(np.arange(np.ceil(ylim[0] / ystep) * ystep, ylim[1] + 1e-9, ystep))
        if equal: ax.set_aspect("equal", adjustable="box")
        ax.grid(True, color=GRID, lw=0.7, zorder=0)
        for s in ("right", "top"): ax.spines[s].set_color("none")
        ax.spines["left"].set_position("zero"); ax.spines["bottom"].set_position("zero")
        for s in ("left", "bottom"): ax.spines[s].set_color(GREY)
        ax.tick_params(colors=INK, labelsize=9)
        ax.plot(1, 0, ">", transform=ax.get_yaxis_transform(), color=GREY, clip_on=False, ms=5)
        ax.plot(0, 1, "^", transform=ax.get_xaxis_transform(), color=GREY, clip_on=False, ms=5)
        fl.polyline(ax, [(xlim[0], 0), (xlim[1], 0)], lw=0)
        fl.polyline(ax, [(0, ylim[0]), (0, ylim[1])], lw=0)

    def curve(self, ax, xs, ys, color, lw=2.4, **kw):
        ax.plot(xs, ys, color=color, lw=lw, zorder=4, **kw)
        fl.polyline(ax, np.column_stack([xs, ys]), lw=0)

    def line(self, ax, p, q, **kw):
        fl.seg(ax, p, q, **kw)

    def dot(self, ax, x, y, color=NAVY):
        ax.plot(x, y, "o", ms=6.5, color=color, zorder=6)
        fl.record_circle((x, y), 0.12, 24) if False else None

    def label(self, ax, text, xy, **kw):
        kw.setdefault("fontsize", BASE_FONT); kw.setdefault("color", INK); kw.setdefault("name", text)
        return fl.place(ax, text, xy, **kw)

    def save(self, fig, name):
        p = os.path.join(self.out, name + ".png")
        fig.savefig(p, dpi=460, transparent=True, bbox_inches="tight", pad_inches=0.04)
        plt.close(fig)
        with Image.open(p) as im:
            wpx = im.width / 460
            asp = im.width / im.height
        eff = 9.0 * self.printed[name] / wpx          # tick labels are 9 pt
        assert eff >= FONT_MIN_PT, f"{name}: smallest label prints at {eff:.1f} pt"
        self.idx[name] = {"file": p, "aspect": asp, "min_label_pt": round(eff, 1)}

    def done(self):
        json.dump(self.idx, open(os.path.join(self.out, "_index.json"), "w"), indent=1)
        print({k: (round(v["aspect"], 2), v["min_label_pt"]) for k, v in self.idx.items()})
