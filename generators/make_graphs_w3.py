"""
Week 3 graphs. House style: recessive grid, arrowheads on axes, thin marks,
direct labels, Computer Modern. Every label placed explicitly.
  A · Gr10 1-3  Piecewise-Defined Functions
  B · Gr11 5-5  Operations on Functions
Diagrams 1-3 from make_diagrams_w3.tex are registered here too.
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

OUT = "graphs_w3"
shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT)

TEAL = "#17A199"; MAROON = "#AD2A22"; INK = "#222E2D"
MUTED = "#5C6E6C"; GRID = "#DCE9E8"; DEEP = "#0E4F4C"
BOX = dict(boxstyle="round,pad=0.18", fc="white", ec="none", alpha=0.88)

idx = {}

def frame(ax, xlim, ylim, xt=None, yt=None):
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    ax.grid(True, color=GRID, lw=0.7, zorder=0)
    for sp in ("top", "right"): ax.spines[sp].set_visible(False)
    ax.spines["left"].set_position(("data", 0))
    ax.spines["bottom"].set_position(("data", 0))
    for sp in ("left", "bottom"):
        ax.spines[sp].set_color(INK); ax.spines[sp].set_linewidth(1.0)
    ax.set_xticks(xt if xt is not None else np.arange(int(xlim[0])+1, int(xlim[1])+1, 2))
    ax.set_yticks(yt if yt is not None else np.arange(int(ylim[0])+1, int(ylim[1])+1, 2))
    ax.tick_params(colors=MUTED, labelsize=8, length=3, width=0.8)
    ax.plot(1, 0, ">", transform=ax.get_yaxis_transform(), clip_on=False, color=INK, ms=5)
    ax.plot(0, 1, "^", transform=ax.get_xaxis_transform(), clip_on=False, color=INK, ms=5)
    ax.set_axisbelow(True)

def save(fig, name):
    p = os.path.join(OUT, name + ".png")
    fig.savefig(p, dpi=300, transparent=True, bbox_inches="tight", pad_inches=0.06)
    plt.close(fig)
    with Image.open(p) as im:
        idx[name] = {"file": p, "aspect": im.width / im.height}

def dot(ax, x, y, closed, color):
    if closed: ax.plot(x, y, "o", ms=6.5, color=color, zorder=6)
    else: ax.plot(x, y, "o", ms=6.5, mfc="white", mec=color, mew=1.8, zorder=6)

# ============================================== A1 · three-panel overview
def pw_panel():
    fig, axes = plt.subplots(1, 3, figsize=(13.6, 3.7))
    # absolute value
    ax = axes[0]; frame(ax, (-5, 5), (-1.5, 6), yt=[1, 2, 3, 4, 5])
    x = np.linspace(-5, 5, 400)
    ax.plot(x, np.abs(x), color=TEAL, lw=2.0)
    ax.annotate(r"$f(x)=|x|$", (3.1, 3.1), xytext=(1.1, 4.9), color=DEEP,
                fontsize=11, bbox=BOX)
    ax.set_title("Absolute value function", fontsize=11, color=DEEP, pad=8)
    # two-piece linear
    ax = axes[1]; frame(ax, (-5, 5), (-3, 6), yt=[-2, 2, 4])
    xl = np.linspace(-5, 1, 200); xr = np.linspace(1, 5, 200)
    ax.plot(xl, 2*xl + 1, color=TEAL, lw=2.0)
    ax.plot(xr, 5 - xr, color=MAROON, lw=2.0)
    dot(ax, 1, 3, False, TEAL); dot(ax, 1, 4, True, MAROON)
    ax.annotate(r"$2x+1,\ x<1$", (-2, -3), xytext=(-4.8, -2.4), color=DEEP, fontsize=10, bbox=BOX)
    ax.annotate(r"$5-x,\ x\geq 1$", (3, 2), xytext=(1.4, 4.7), color=MAROON, fontsize=10, bbox=BOX)
    ax.set_title("Two-piece function", fontsize=11, color=DEEP, pad=8)
    # step function
    ax = axes[2]; frame(ax, (-3, 5), (-3.5, 5), xt=[-2, -1, 1, 2, 3, 4], yt=[-2, 2, 4])
    for n in range(-3, 5):
        ax.hlines(n, n, n + 1, color=TEAL, lw=2.0)
        dot(ax, n, n, True, TEAL); dot(ax, n + 1, n, False, TEAL)
    ax.annotate(r"$f(x)=\lfloor x\rfloor$", (2.5, 2), xytext=(-2.8, 3.6), color=DEEP,
                fontsize=11, bbox=BOX)
    ax.set_title("Step function (floor)", fontsize=11, color=DEEP, pad=8)
    fig.tight_layout()
    save(fig, "g_pw_panel")

# ============================================== A2 · worked example
def pw_worked():
    fig, ax = plt.subplots(figsize=(6.4, 4.6))
    frame(ax, (-4, 6), (-4, 7), yt=[-2, 2, 4, 6])
    xl = np.linspace(-4, 1, 200); xr = np.linspace(1, 6, 200)
    ax.plot(xl, 2*xl + 1, color=TEAL, lw=2.2)
    ax.plot(xr, 5 - xr, color=MAROON, lw=2.2)
    dot(ax, 1, 3, False, TEAL); dot(ax, 1, 4, True, MAROON)
    ax.annotate(r"$2x+1$", (-1.5, -2), xytext=(-3.8, 1.2), color=DEEP, fontsize=12, bbox=BOX,
                arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
    ax.annotate(r"$5-x$", (4, 1), xytext=(3.4, 3.6), color=MAROON, fontsize=12, bbox=BOX,
                arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
    ax.annotate("open at $(1,3)$\nnot included", (1, 3), xytext=(-3.9, 5.4), color=MUTED,
                fontsize=9, bbox=BOX, arrowprops=dict(arrowstyle="->", color=MUTED, lw=0.8))
    ax.annotate("closed at $(1,4)$\nthis is $f(1)$", (1, 4), xytext=(2.0, 5.8), color=MUTED,
                fontsize=9, bbox=BOX, arrowprops=dict(arrowstyle="->", color=MUTED, lw=0.8))
    fig.tight_layout()
    save(fig, "g_pw_worked")

# ============================================== A3 · mastery gate graph
def pw_gate():
    fig, ax = plt.subplots(figsize=(5.6, 4.3))
    frame(ax, (-4, 7), (-3, 7), yt=[-2, 2, 4, 6])
    xl = np.linspace(-4, 2, 200); xr = np.linspace(2, 7, 200)
    ax.plot(xl, 0*xl + 3, color=TEAL, lw=2.2)
    ax.plot(xr, xr - 1, color=TEAL, lw=2.2)
    dot(ax, 2, 3, False, TEAL); dot(ax, 2, 1, True, TEAL)
    ax.annotate("$(2,3)$", (2, 3), xytext=(-2.0, 4.6), color=MUTED, fontsize=9, bbox=BOX,
                arrowprops=dict(arrowstyle="->", color=MUTED, lw=0.8))
    ax.annotate("$(2,1)$", (2, 1), xytext=(3.4, -1.6), color=MUTED, fontsize=9, bbox=BOX,
                arrowprops=dict(arrowstyle="->", color=MUTED, lw=0.8))
    fig.tight_layout()
    save(fig, "g_pw_gate")

# ============================================== A4 · Saudi electricity tariff
def pw_tariff():
    fig, ax = plt.subplots(figsize=(6.6, 4.4))
    x1 = np.linspace(0, 6000, 200); x2 = np.linspace(6000, 12000, 200)
    ax.plot(x1, 0.18*x1, color=TEAL, lw=2.2)
    ax.plot(x2, 1080 + 0.30*(x2 - 6000), color=MAROON, lw=2.2)
    ax.plot(6000, 1080, "o", ms=6.5, color=DEEP, zorder=6)
    ax.set_xlim(0, 12500); ax.set_ylim(0, 3200)
    ax.grid(True, color=GRID, lw=0.7, zorder=0); ax.set_axisbelow(True)
    for sp in ("top", "right"): ax.spines[sp].set_visible(False)
    for sp in ("left", "bottom"):
        ax.spines[sp].set_color(INK); ax.spines[sp].set_linewidth(1.0)
    ax.set_xticks([2000, 4000, 6000, 8000, 10000, 12000])
    ax.set_yticks([500, 1000, 1500, 2000, 2500, 3000])
    ax.tick_params(colors=MUTED, labelsize=8, length=3, width=0.8)
    ax.plot(1, 0, ">", transform=ax.get_yaxis_transform(), clip_on=False, color=INK, ms=5)
    ax.plot(0, 1, "^", transform=ax.get_xaxis_transform(), clip_on=False, color=INK, ms=5)
    ax.set_xlabel("consumption, kWh per month", fontsize=9.5, color=MUTED)
    ax.set_ylabel("cost, SAR", fontsize=9.5, color=MUTED)
    ax.annotate("18 halalas per kWh", (3000, 540), xytext=(500, 1500), color=DEEP,
                fontsize=10, bbox=BOX, arrowprops=dict(arrowstyle="->", color=MUTED, lw=0.8))
    ax.annotate("30 halalas per kWh", (9500, 2130), xytext=(6100, 800), color=MAROON,
                fontsize=10, bbox=BOX, arrowprops=dict(arrowstyle="->", color=MUTED, lw=0.8))
    ax.annotate("the rate changes here\n$(6000,\\ 1080)$", (6000, 1080), xytext=(2700, 2500),
                color=MUTED, fontsize=9, bbox=BOX,
                arrowprops=dict(arrowstyle="->", color=MUTED, lw=0.8))
    fig.tight_layout()
    save(fig, "g_pw_tariff")

# ============================================== B1 · sum of two functions
def ops_sum():
    fig, ax = plt.subplots(figsize=(6.6, 4.6))
    frame(ax, (-6.5, 6.5), (-8, 12), xt=[-6, -4, -2, 2, 4, 6], yt=[-6, -3, 3, 6, 9])
    x = np.linspace(-6.5, 6.5, 400)
    ax.plot(x, x**2 - 4, color=TEAL, lw=2.0)
    ax.plot(x, x + 3, color=MUTED, lw=1.6, ls="--")
    ax.plot(x, x**2 + x - 1, color=MAROON, lw=2.2)
    ax.annotate(r"$f(x)=x^{2}-4$", (3.0, 5.0), xytext=(3.5, 1.4), color=DEEP, fontsize=10,
                bbox=BOX, arrowprops=dict(arrowstyle="->", color=MUTED, lw=0.8))
    ax.annotate(r"$g(x)=x+3$", (-4.2, -1.2), xytext=(-6.3, -5.6), color=MUTED, fontsize=10,
                bbox=BOX, arrowprops=dict(arrowstyle="->", color=MUTED, lw=0.8))
    ax.annotate(r"$(f+g)(x)=x^{2}+x-1$", (-3.0, 5.0), xytext=(-6.3, 8.6), color=MAROON,
                fontsize=10, bbox=BOX, arrowprops=dict(arrowstyle="->", color=MUTED, lw=0.8))
    fig.tight_layout()
    save(fig, "g_ops_sum")

# ============================================== B2 · order matters
def ops_order():
    fig, ax = plt.subplots(figsize=(6.6, 4.6))
    frame(ax, (-8.5, 5.5), (-6, 15), xt=[-8, -6, -4, -2, 2, 4], yt=[-3, 3, 6, 9, 12])
    x = np.linspace(-8.5, 5.5, 400)
    ax.plot(x, x**2 + 6*x + 5, color=TEAL, lw=2.2)
    ax.plot(x, x**2 - 1, color=MAROON, lw=2.2)
    ax.plot(-3, -4, "o", ms=6.5, color=TEAL, zorder=6)
    ax.plot(0, -1, "o", ms=6.5, color=MAROON, zorder=6)
    ax.annotate(r"$(f\circ g)(x)=x^{2}+6x+5$", (-6.2, 6.24), xytext=(-8.4, 11.0), color=DEEP,
                fontsize=10, bbox=BOX, arrowprops=dict(arrowstyle="->", color=MUTED, lw=0.8))
    ax.annotate(r"$(g\circ f)(x)=x^{2}-1$", (3.4, 10.6), xytext=(0.4, 13.2), color=MAROON,
                fontsize=10, bbox=BOX, arrowprops=dict(arrowstyle="->", color=MUTED, lw=0.8))
    ax.text(-3.0, -5.4, r"vertex $(-3,-4)$", color=DEEP, fontsize=9, ha="center", bbox=BOX)
    ax.text(1.9, -2.6, r"vertex $(0,-1)$", color=MAROON, fontsize=9, ha="center", bbox=BOX)
    fig.tight_layout()
    save(fig, "g_ops_order")

pw_panel(); pw_worked(); pw_gate(); pw_tariff(); ops_sum(); ops_order()

# register the TikZ diagrams
for name, f in [("d_comp_machine", "diagrams_w3/d-1.png"),
                ("d_order_matters", "diagrams_w3/d-2.png"),
                ("d_disjoint", "diagrams_w3/d-3.png")]:
    with Image.open(f) as im:
        idx[name] = {"file": f, "aspect": im.width / im.height}

json.dump(idx, open(os.path.join(OUT, "_index.json"), "w"), indent=1)
for k, v in idx.items(): print(f"{k:18s} aspect {v['aspect']:.2f}")
