"""Figures for MAWHIBA Grade 9 · Unit 1 · Activity 2 — Rectangular Areas.

The source's drawings are the weakest part of the activity: figure 4 carries six
labels with no statement of how they relate, so two students can read two
different shapes out of it and both be right. Every figure here therefore

  * draws the shape to scale from the numbers the task states,
  * puts each label on the side it measures, outside the outline, and
  * ASSERTS its own dimensions before the file is written, so a picture can
    never disagree with the answer key.

    python3 make_figs_maw2.py        -> figs_maw2/ + _index.json
"""
import json, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrow
from PIL import Image

matplotlib.rcParams["mathtext.fontset"] = "cm"

OUT = "figs_maw2"
DPI = 460
INK = "#222E2D"
NAVY = "#1F3864"
GOLD = "#F2C230"
GOLD_E = "#B8860B"
GREY = "#6B7674"
os.makedirs(OUT, exist_ok=True)
idx = {}


def start(w, h):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_aspect("equal")
    ax.axis("off")
    return fig, ax


def save(fig, name):
    p = os.path.join(OUT, name + ".png")
    fig.savefig(p, dpi=DPI, transparent=True, bbox_inches="tight", pad_inches=0.02)
    plt.close(fig)
    with Image.open(p) as im:
        idx[name] = {"file": p, "win": im.width / DPI, "hin": im.height / DPI,
                     "aspect": im.width / im.height}


def outline(ax, x, y, w, h, **kw):
    ax.add_patch(Rectangle((x, y), w, h, fill=False, ec=kw.get("ec", INK),
                           lw=kw.get("lw", 1.6), zorder=3))


def shade(ax, x, y, w, h):
    ax.add_patch(Rectangle((x, y), w, h, facecolor=GOLD, ec=GOLD_E, lw=1.2, zorder=2))


def lab(ax, x, y, t, **kw):
    ax.text(x, y, t, fontsize=kw.get("fs", 11), color=kw.get("c", INK),
            ha=kw.get("ha", "center"), va=kw.get("va", "center"), zorder=5)


def dim_h(ax, x0, x1, y, text, fs=10.5, c=NAVY, off=0.0):
    """A horizontal measurement, drawn OUTSIDE the shape with end ticks."""
    ax.annotate("", xy=(x1, y), xytext=(x0, y),
                arrowprops=dict(arrowstyle="<|-|>", color=c, lw=1.0,
                                mutation_scale=8, shrinkA=0, shrinkB=0), zorder=4)
    for x in (x0, x1):
        ax.plot([x, x], [y - 0.14, y + 0.14], color=c, lw=0.9, zorder=4)
    lab(ax, (x0 + x1) / 2, y + 0.42 + off, text, fs=fs, c=c)


def dim_v(ax, y0, y1, x, text, fs=10.5, c=NAVY, off=0.0, side="left"):
    ax.annotate("", xy=(x, y1), xytext=(x, y0),
                arrowprops=dict(arrowstyle="<|-|>", color=c, lw=1.0,
                                mutation_scale=8, shrinkA=0, shrinkB=0), zorder=4)
    for y in (y0, y1):
        ax.plot([x - 0.14, x + 0.14], [y, y], color=c, lw=0.9, zorder=4)
    dx = -0.42 - off if side == "left" else 0.42 + off
    lab(ax, x + dx, (y0 + y1) / 2, text, fs=fs, c=c,
        ha="right" if side == "left" else "left")


# ------------------------------------------------------------------ figure 1
def fig1(name):
    """12 by 7, with an x by 3 rectangle shaded in the top-left corner.
    Unshaded area = 84 - 3x."""
    W, H, SH, SW = 12.0, 7.0, 3.0, 4.5      # x drawn as 4.5: a length, not a nice number
    assert W * H - SH * SW == 84 - 3 * SW
    fig, ax = start(3.5, 2.5)
    ax.set_xlim(-2.2, W + 1.2)
    ax.set_ylim(-1.7, H + 1.9)
    outline(ax, 0, 0, W, H)
    shade(ax, 0, H - SH, SW, SH)
    dim_h(ax, 0, W, H + 0.95, r"$12$")
    dim_v(ax, 0, H, -1.15, r"$7$")
    dim_v(ax, H - SH, H, SW + 0.75, r"$3$", side="right")
    dim_h(ax, 0, SW, H - SH - 0.85, r"$x$", off=-0.9)
    save(fig, name)


# ------------------------------------------------------------------ figure 2
def fig2(name):
    """8 by 8, with a 2 by p rectangle shaded in the bottom-right corner.
    Unshaded area = 64 - 2p."""
    S, SW, SH = 8.0, 2.0, 3.0               # p drawn as 3
    assert S * S - SW * SH == 64 - 2 * SH
    fig, ax = start(2.6, 2.5)
    ax.set_xlim(-2.0, S + 1.9)
    ax.set_ylim(-1.5, S + 1.9)
    outline(ax, 0, 0, S, S)
    shade(ax, S - SW, 0, SW, SH)
    dim_h(ax, 0, S, S + 0.95, r"$8$")
    dim_v(ax, 0, S, -1.15, r"$8$")
    dim_h(ax, S - SW, S, -0.95, r"$2$", off=-0.85)
    dim_v(ax, 0, SH, S - SW - 0.75, r"$p$")
    save(fig, name)


# ------------------------------------------------------------------ figure 3
def fig3(name):
    """12 wide by m tall, with a strip 1 tall shaded across the middle, clear
    of the left edge by 3 and of the right edge by 2. The shaded strip is
    therefore 7 wide, and the unshaded area is 12m - 7."""
    W, H, T, L, R = 12.0, 6.0, 1.0, 3.0, 2.0
    assert W - L - R == 7.0
    assert W * H - (W - L - R) * T == 12 * H - 7
    fig, ax = start(3.4, 2.3)
    ax.set_xlim(-2.2, W + 1.3)
    ax.set_ylim(-1.5, H + 2.3)
    outline(ax, 0, 0, W, H)
    y0 = H - 1.6
    shade(ax, L, y0, W - L - R, T)
    dim_h(ax, 0, W, -0.95, r"$12$", off=-0.85)
    dim_v(ax, 0, H, -1.15, r"$m$")
    dim_h(ax, 0, L, H + 0.75, r"$3$", fs=9.5)
    dim_h(ax, W - R, W, H + 0.75, r"$2$", fs=9.5)
    dim_v(ax, y0, y0 + T, W + 0.7, r"$1$", fs=9.5, side="right")
    save(fig, name)


# ------------------------------------------------------------------ figure 4
def fig4(name):
    """p wide by 10 tall, with a 6 by 2 rectangle shaded, set in from the left
    by 2 and from the top by 2. The remaining gaps are r on the right and q
    below, so p = 8 + r and q = 6. Unshaded area = 10p - 12.

    THE SOURCE'S FIGURE 4 IS THE ONE THAT NEEDED THIS: it carried 2, 6, r, q,
    p and 10 with nothing saying which measured what, so the relations had to
    be guessed. Here every label sits on the side it measures."""
    H, SW, SH, LEFT, TOP, R = 10.0, 6.0, 2.0, 2.0, 2.0, 3.0
    P = LEFT + SW + R
    Q = H - TOP - SH
    assert P == 11.0 and Q == 6.0
    assert H * P - SW * SH == 10 * P - 12
    # and the dissection the task is fishing for agrees
    assert TOP * P + Q * P + SH * (LEFT + R) == 10 * P - 12
    fig, ax = start(3.3, 2.7)
    ax.set_xlim(-2.2, P + 2.0)
    ax.set_ylim(-1.7, H + 1.9)
    outline(ax, 0, 0, P, H)
    sx, sy = LEFT, H - TOP - SH
    shade(ax, sx, sy, SW, SH)
    dim_v(ax, 0, H, -1.15, r"$10$")
    dim_h(ax, 0, P, -0.95, r"$p$", off=-0.85)
    dim_h(ax, 0, LEFT, sy + SH + 0.55, r"$2$", fs=9.5)
    dim_v(ax, H - TOP, H, sx + SW + 0.6, r"$2$", fs=9.5, side="right")
    dim_h(ax, sx, sx + SW, sy + SH / 2 - 0.05, r"$6$", off=-0.55, fs=10)
    dim_h(ax, sx + SW, P, sy - 0.55, r"$r$", off=-0.85, fs=9.5)
    dim_v(ax, 0, sy, P + 0.75, r"$q$", fs=9.5, side="right")
    save(fig, name)


# ------------------------------------------------------------------ figure 5
def fig5(name):
    """An a by a square with a b by b square cut from the top-right corner.
    Area = a^2 - b^2."""
    A, B = 8.0, 3.0
    assert A * A - B * B == (A - B) * (A + B)
    fig, ax = start(2.7, 2.6)
    ax.set_xlim(-2.0, A + 1.6)
    ax.set_ylim(-1.5, A + 1.9)
    pts = [(0, 0), (A, 0), (A, A - B), (A - B, A - B), (A - B, A), (0, A)]
    ax.add_patch(plt.Polygon(pts, facecolor=GOLD, ec=GOLD_E, lw=1.5, zorder=2))
    # the removed square, dashed
    ax.add_patch(Rectangle((A - B, A - B), B, B, fill=False, ec=GREY, lw=1.1,
                           ls=(0, (3, 2)), zorder=3))
    dim_v(ax, 0, A, -1.15, r"$a$")
    dim_h(ax, 0, A, -0.95, r"$a$", off=-0.85)
    dim_h(ax, A - B, A, A + 0.75, r"$b$", fs=10)
    dim_v(ax, A - B, A, A + 0.7, r"$b$", fs=10, side="right")
    save(fig, name)


# ------------------------------------------------------------------ figure 6
def fig6(name):
    """The rearrangement that PROVES a^2 - b^2 = (a - b)(a + b): the L-shape is
    cut into two rectangles and they are laid side by side."""
    A, B = 8.0, 3.0
    W1, W2 = A - B, B                       # the two pieces the cut makes
    assert W1 * A + W2 * W1 == (A - B) * (A + B)
    gap = 4.0
    fig, ax = start(6.4, 2.4)
    ax.set_xlim(-2.0, A + gap + (A + B) + 2.2)
    ax.set_ylim(-3.2, A + 2.4)

    # ---- left: the L-shape with the cut marked
    pts = [(0, 0), (A, 0), (A, A - B), (A - B, A - B), (A - B, A), (0, A)]
    ax.add_patch(plt.Polygon(pts, facecolor=GOLD, ec=GOLD_E, lw=1.3, zorder=2))
    ax.add_patch(Rectangle((A - B, 0), B, A - B, facecolor="#F7E3A1",
                           ec=GOLD_E, lw=1.3, zorder=3))
    ax.plot([A - B, A - B], [0, A], color=INK, lw=1.5, ls=(0, (4, 2)), zorder=4)
    lab(ax, (A - B) / 2, A / 2 + 0.3, r"$a-b$", fs=10)
    lab(ax, (A - B) / 2, A / 2 - 1.0, r"$\mathrm{by}\ a$", fs=10)
    lab(ax, A - B + B / 2, (A - B) / 2 + 0.55, r"$b\ \mathrm{by}$", fs=9)
    lab(ax, A - B + B / 2, (A - B) / 2 - 0.75, r"$a-b$", fs=9)
    lab(ax, A / 2, -2.4, "cut along the dashed line", fs=9.5, c=GREY)

    # ---- the move
    ax.annotate("", xy=(A + gap - 1.1, A / 2), xytext=(A + 1.1, A / 2),
                arrowprops=dict(arrowstyle="-|>", color=NAVY, lw=1.8, mutation_scale=15))

    # ---- right: one rectangle, (a + b) wide and (a - b) tall, drawn to scale
    ox, hgt = A + gap, A - B
    ax.add_patch(Rectangle((ox, 0), A, hgt, facecolor=GOLD, ec=GOLD_E, lw=1.3, zorder=3))
    ax.add_patch(Rectangle((ox + A, 0), B, hgt, facecolor="#F7E3A1",
                           ec=GOLD_E, lw=1.3, zorder=3))
    ax.plot([ox + A, ox + A], [0, hgt], color=INK, lw=1.3, ls=(0, (4, 2)), zorder=4)
    dim_h(ax, ox, ox + A + B, -1.5, r"$a+b$", off=-0.8)
    dim_v(ax, 0, hgt, ox - 0.9, r"$a-b$", fs=10)
    lab(ax, ox + (A + B) / 2, hgt + 1.5, "same area, one rectangle", fs=9.5, c=GREY)
    save(fig, name)


def build():
    fig1("m2_f1"); fig2("m2_f2"); fig3("m2_f3")
    fig4("m2_f4"); fig5("m2_f5"); fig6("m2_f6")
    # the arithmetic behind task 4, checked here so the key cannot drift
    assert (20 + 7) * (30 + 8) == 27 * 38 == 1026
    assert 20 * 30 + 20 * 8 + 7 * 30 + 7 * 8 == 1026
    json.dump(idx, open(os.path.join(OUT, "_index.json"), "w"), indent=1)
    print(f"{len(idx)} Activity 2 figures written to {OUT}/")


if __name__ == "__main__":
    build()
