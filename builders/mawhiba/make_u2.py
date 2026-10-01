"""Mawhiba G9 Unit 2 Activity 1 — maths images + diagrams, with every value re-derived in code.
The printed Student Book lost the fractions in c, g and h; they are reconstructed from the Teacher's Guide
(scale factor, centre and fixed point stated for each) and re-derived here."""
import json, os
from fractions import Fraction as F
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image
from mathgen import render

# ---- the eight functions: (m, c) exactly
FUN = {"a": (F(-1), F(0)), "b": (F(1), F(-4)), "c": (F(1, 2), F(0)), "d": (F(3), F(-2)),
       "e": (F(2), F(1)), "f": (F(-1), F(3)), "g": (F(-1, 2), F(3)), "h": (F(1, 3), F(1))}
def val(k, x): m, c = FUN[k]; return m * x + c
def fixed(k):
    m, c = FUN[k]; return None if m == 1 else c / (1 - m)
# facts from the Teacher's Guide, checked
TG_FIXED = {"a": F(0), "b": None, "c": F(0), "d": F(1), "e": F(-1), "f": F(3, 2), "g": F(2), "h": F(3, 2)}
TG_SF = {"a": F(-1), "b": F(1), "c": F(1, 2), "d": F(3), "e": F(2), "f": F(-1), "g": F(-1, 2), "h": F(1, 3)}
for k in FUN:
    assert fixed(k) == TG_FIXED[k], k
    assert FUN[k][0] == TG_SF[k], k
    p = fixed(k)
    if p is not None: assert val(k, p) == p
    # position of the centre of the arrows (domain line at height 1, range line at height 0)
    m = FUN[k][0]
    if m != 1:
        s = 1 / (1 - m)
        if m > 1: assert s < 0
        elif 0 < m < 1: assert s > 1
        elif m < 0: assert 0 < s < 1
print("all eight functions re-derived; fixed points:", {k: (str(v) if v is not None else None) for k, v in {k: fixed(k) for k in FUN}.items()})

INK, NAVY, TEAL, GOLD, PLUM, GREY = "#222E2D", "#1F3864", "#17A199", "#F0B323", "#6B3FA0", "#8A9795"
LO, HI = -4, 10
os.makedirs("fig", exist_ok=True)

def lines(ax, ys=(1, 0)):
    for y, lab in zip(ys, ("domain  x", "range  f(x)")):
        ax.plot([LO - .4, HI + .4], [y, y], color=INK, lw=1.0, zorder=2)
        ax.plot([HI + .4], [y], ">", color=INK, ms=4, clip_on=False)
        for t in range(LO, HI + 1):
            ax.plot([t, t], [y - .07, y + .07], color=INK, lw=0.8, zorder=2)
            ax.text(t, y + (.2 if y == 1 else -.2), str(t).replace("-", "−"), ha="center",
                    va="bottom" if y == 1 else "top", fontsize=8, color=INK)
    ax.set_xlim(LO - .7, HI + .9); ax.set_ylim(-0.55, 1.55); ax.axis("off")

def blank(name):
    fig, ax = plt.subplots(figsize=(3.4, 0.78)); lines(ax)
    fig.subplots_adjust(0, 0, 1, 1); fig.savefig(f"fig/{name}.png", dpi=300, transparent=True); plt.close(fig)

blank("dbl")
XS = {"a": range(-3, 4), "b": range(0, 7), "c": range(0, 11, 2), "d": range(0, 5), "e": range(-2, 5),
      "f": range(-1, 7), "g": range(0, 11, 2), "h": range(0, 10, 3)}
def solved(k):
    fig, ax = plt.subplots(figsize=(3.4, 0.78)); lines(ax)
    for x in XS[k]:
        y = val(k, F(x)); assert LO <= y <= HI, (k, x, y)
        ax.plot([x, float(y)], [.97, .03], color=TEAL, lw=1.1, zorder=3)
    p = fixed(k)
    if p is not None:
        assert LO <= p <= HI
        ax.plot([float(p)], [1], "o", color=GOLD, ms=5, zorder=5, mec=INK, mew=.6)
        ax.plot([float(p)], [0], "o", color=GOLD, ms=5, zorder=5, mec=INK, mew=.6)
    fig.subplots_adjust(0, 0, 1, 1); fig.savefig(f"fig/s_{k}.png", dpi=300, transparent=True); plt.close(fig)
for k in FUN: solved(k)

# blank xy-grid (house rule: a grid wherever a sketch is asked for)
fig, ax = plt.subplots(figsize=(3.0, 3.0))
ax.set_xlim(-6, 6); ax.set_ylim(-6, 6); ax.set_aspect("equal")
ax.set_xticks(range(-6, 7)); ax.set_yticks(range(-6, 7)); ax.grid(True, color="#C9DEDC", lw=.6)
for s in ("right", "top"): ax.spines[s].set_color("none")
ax.spines["left"].set_position("zero"); ax.spines["bottom"].set_position("zero")
ax.tick_params(labelsize=8, colors=INK, length=2)
ax.plot(1, 0, ">", transform=ax.get_yaxis_transform(), color=INK, clip_on=False, ms=4)
ax.plot(0, 1, "^", transform=ax.get_xaxis_transform(), color=INK, clip_on=False, ms=4)
fig.tight_layout(); fig.savefig("fig/xy.png", dpi=300, transparent=False, facecolor="white"); plt.close(fig)

# key graph: y = x with d (one fixed point) and b (parallel)
fig, ax = plt.subplots(figsize=(3.0, 3.0))
ax.set_xlim(-6, 6); ax.set_ylim(-6, 6); ax.set_aspect("equal")
ax.set_xticks(range(-6, 7, 2)); ax.set_yticks(range(-6, 7, 2)); ax.grid(True, color="#C9DEDC", lw=.6)
for s in ("right", "top"): ax.spines[s].set_color("none")
ax.spines["left"].set_position("zero"); ax.spines["bottom"].set_position("zero")
ax.tick_params(labelsize=8, colors=INK, length=2)
xs = np.array([-6, 6])
ax.plot(xs, xs, color=GREY, lw=1.4, ls="--"); ax.plot(xs, 3 * xs - 2, color=TEAL, lw=1.8); ax.plot(xs, xs - 4, color=PLUM, lw=1.8)
ax.set_ylim(-6, 6)
ax.plot([1], [1], "o", color=GOLD, ms=6, mec=INK, zorder=5)
ax.text(1.4, 0.15, "(1, 1)", fontsize=8, color=INK)
ax.text(-5.8, -5.4, "y = x", fontsize=8, color=INK, rotation=45, rotation_mode="anchor")
ax.text(1.55, 4.7, "d: y = 3x − 2", fontsize=8, color=INK)
ax.text(2.6, -2.9, "b: y = x − 4", fontsize=8, color=INK)
fig.tight_layout(); fig.savefig("fig/key_graph.png", dpi=300, transparent=False, facecolor="white"); plt.close(fig)

E_ = {
 "fa": r"a(x)=-x", "fb": r"b(x)=x-4", "fc": r"c(x)=\dfrac{x}{2}", "fd": r"d(x)=3x-2", "fe": r"e(x)=2x+1",
 "ff": r"f(x)=3-x", "fg": r"g(x)=3-\dfrac{x}{2}", "fh": r"h(x)=\dfrac{x}{3}+1",
 "gen": r"f(x)=mx+c", "fixeq": r"mx+c=x\ \Longrightarrow\ x=\dfrac{c}{1-m}\qquad(m\neq 1)",
 "id": r"f(x)=x",
 "sa": r"-x=x\Rightarrow x=0", "sb": r"x-4=x\Rightarrow -4=0\ \ \text{(never)}", "sc": r"\dfrac{x}{2}=x\Rightarrow x=0",
 "sd": r"3x-2=x\Rightarrow x=1", "se": r"2x+1=x\Rightarrow x=-1", "sf": r"3-x=x\Rightarrow x=\dfrac{3}{2}",
 "sg": r"3-\dfrac{x}{2}=x\Rightarrow x=2", "sh": r"\dfrac{x}{3}+1=x\Rightarrow x=\dfrac{3}{2}",
 "refl": r"x\mapsto -x+c\ \text{is a reflection in}\ x=\dfrac{c}{2}", "tr": r"x\mapsto x+c\ \text{is a translation by}\ c",
 "enl": r"x\mapsto mx+c\ \text{is an enlargement, scale factor}\ m,\ \text{centre}\ \dfrac{c}{1-m}",
 "par": r"y=x+c\ \ (c\neq 0)\ \text{is parallel to}\ y=x",
 "pos": r"s=\dfrac{1}{1-m}",
}
E = {"u_" + k: (v, "222E2D") for k, v in E_.items()}
render(E, "mawu2", "math_mawu2")
print("done")
