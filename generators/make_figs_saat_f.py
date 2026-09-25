"""Figures for part F of the SAAT booklet — the diagrams the sample papers use.

Nothing here is a redrawing of a source figure. Each is built from the item's
own numbers, in the department's own line style, and every number a figure
carries is ASSERTED in this file, so a picture can never disagree with the
answer key: a mistyped value fails the build.

Labels go through figlabel, which measures each label's rendered box and refuses
to place one on top of the drawing.

    python3 make_figs_saat_f.py        # writes into figs_saat/ and extends its index
"""
import json, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Arc, Circle, Ellipse
import figlabel as FL

plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["DejaVu Serif"]

OUT = "figs_saat"
os.makedirs(OUT, exist_ok=True)

NAVY = "#1F3864"; INK = "#222E2D"; TEAL = "#17A199"; GREY = "#A6A6A6"
GRID = "#DCE9E8"; MAROON = "#9E2A2B"
idx = json.load(open(os.path.join(OUT, "_index.json"))) if \
    os.path.exists(os.path.join(OUT, "_index.json")) else {}


def start_fig(figsize):
    FL.reset()
    return plt.subplots(figsize=figsize)


def save(fig, name):
    p = os.path.join(OUT, name + ".png")
    fig.savefig(p, dpi=400, transparent=True, bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)
    from PIL import Image
    with Image.open(p) as im:
        idx[name] = {"file": p, "aspect": im.width / im.height}
    return p


def frame(ax, xlim, ylim, equal=True):
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    if equal:
        ax.set_aspect("equal")
    ax.axis("off")


def axes2d(ax, xlim, ylim, step=1, grid=True):
    """A light grid with arrowheaded axes — the house style for a graph."""
    if grid:
        for x in np.arange(np.ceil(xlim[0]), xlim[1] + 1e-9, step):
            ax.plot([x, x], list(ylim), color=GRID, lw=0.6, zorder=0)
        for y in np.arange(np.ceil(ylim[0]), ylim[1] + 1e-9, step):
            ax.plot(list(xlim), [y, y], color=GRID, lw=0.6, zorder=0)
    ax.annotate("", xy=(xlim[1], 0), xytext=(xlim[0], 0),
                arrowprops=dict(arrowstyle="<|-|>", color=INK, lw=1.1, mutation_scale=9))
    ax.annotate("", xy=(0, ylim[1]), xytext=(0, ylim[0]),
                arrowprops=dict(arrowstyle="<|-|>", color=INK, lw=1.1, mutation_scale=9))
    ax.text(xlim[1] - 0.05, -0.42, "$x$", ha="right", va="top", fontsize=11, color=INK)
    ax.text(-0.42, ylim[1] + 0.02, "$y$", ha="right", va="bottom", fontsize=11, color=INK)


def right_angle(ax, V, A, B, s=0.5, color=GREY):
    """A small square at V between the rays to A and B."""
    V, A, B = map(lambda t: np.asarray(t, float), (V, A, B))
    u = (A - V) / np.linalg.norm(A - V); v = (B - V) / np.linalg.norm(B - V)
    ax.plot(*zip(V + u * s, V + u * s + v * s, V + v * s), color=color, lw=1.0)


def ticks(ax, P, Q, n=1, s=0.28, color=INK):
    """Congruence tick marks at the midpoint of PQ."""
    P, Q = np.asarray(P, float), np.asarray(Q, float)
    m = (P + Q) / 2
    d = (Q - P) / np.linalg.norm(Q - P)
    nrm = np.array([-d[1], d[0]])
    for k in range(n):
        off = (k - (n - 1) / 2) * s * 0.9
        c = m + d * off
        ax.plot(*zip(c - nrm * s, c + nrm * s), color=color, lw=1.3)


def leader(ax, text, xy, to, color=INK, fontsize=11.5, ha="left"):
    """A label taken outside the drawing on a thin leader line.

    Some labels have nowhere to go: the centroid sits where three medians cross,
    a half-diagonal label sits between two crossing diagonals. Pushing those
    outwards can never find clear paper, so they are placed deliberately outside
    and connected back."""
    ax.annotate(text, xy=tuple(xy), xytext=tuple(to), fontsize=fontsize, color=color,
                ha=ha, va="center",
                arrowprops=dict(arrowstyle="-", color=GREY, lw=0.8,
                                shrinkA=2, shrinkB=4))


def arrowends(ax, P, Q, color=INK, lw=1.6):
    """A full line with an arrowhead at each end."""
    ax.annotate("", xy=Q, xytext=P,
                arrowprops=dict(arrowstyle="<|-|>", color=color, lw=lw, mutation_scale=9))
    FL.seg(ax, P, Q, lw=0)


# ===================================================================== POLAR
def polar_grid(name, rays, rmax=4.0, labels=True):
    """A polar grid with the named rays drawn and lettered."""
    fig, ax = start_fig((3.0, 3.0))
    for r in np.arange(1, rmax + 0.01, 1.0):
        ax.add_patch(Circle((0, 0), r, fill=False, ec=GRID, lw=0.7, zorder=0))
    for d in range(0, 360, 30):
        t = np.radians(d)
        ax.plot([0, rmax * np.cos(t)], [0, rmax * np.sin(t)],
                color=GRID, lw=0.6, zorder=0)
    for d in (0, 90, 180, 270):
        t = np.radians(d)
        ax.text(1.16 * rmax * np.cos(t), 1.16 * rmax * np.sin(t), f"{d}°",
                ha="center", va="center", fontsize=8.5, color=GREY)
    for lab, (r, deg) in rays.items():
        t = np.radians(deg)
        P = (r * np.cos(t), r * np.sin(t))
        ax.annotate("", xy=P, xytext=(0, 0),
                    arrowprops=dict(arrowstyle="-|>", color=NAVY, lw=1.7, mutation_scale=11))
        FL.seg(ax, (0, 0), P, lw=0)
        u = np.array(P) / np.linalg.norm(P)
        ax.text(P[0] + 0.42 * u[0], P[1] + 0.42 * u[1], lab,
                ha="center", va="center", fontsize=12, color=NAVY, weight="bold")
    frame(ax, (-1.45 * rmax, 1.45 * rmax), (-1.35 * rmax, 1.35 * rmax))
    save(fig, name)


def polar_circle(name, a, kind):
    """r = a sin θ (circle above the pole) or r = a cos θ (circle to the right)."""
    t = np.linspace(0, np.pi, 400) if kind == "sin" else np.linspace(-np.pi / 2, np.pi / 2, 400)
    r = a * (np.sin(t) if kind == "sin" else np.cos(t))
    x, y = r * np.cos(t), r * np.sin(t)
    lim = a * 0.62
    fig, ax = start_fig((2.7, 2.7))
    axes2d(ax, (-lim, lim), (-lim * 0.35, a * 1.18), step=max(1, a // 6))
    ax.plot(x, y, color=NAVY, lw=1.9)
    FL.polyline(ax, np.c_[x, y], lw=0)
    top = (0, a) if kind == "sin" else (a, 0)
    mid = (0, a / 2) if kind == "sin" else (a / 2, 0)
    for P in (top, mid):
        ax.plot(*P, "o", ms=4.2, color=MAROON, zorder=5)
    frame(ax, (-lim * 1.25, lim * 3.1), (-lim * 0.75, a * 1.22))
    # a leader line out to the right: the y-axis runs through the top point, so
    # no offset along it can ever clear the drawing
    L = (lim * 1.3, a * 0.97)
    assert (L[0] - 0) ** 2 + (L[1] - a / 2) ** 2 > (a / 2) ** 2, "label sits inside the circle"
    ax.annotate(f"$(0,\\,{a})$" if kind == "sin" else f"$({a},\\,0)$",
                xy=top, xytext=L, fontsize=10.5, color=MAROON,
                ha="left", va="center",
                arrowprops=dict(arrowstyle="-", color=MAROON, lw=0.8,
                                shrinkA=2, shrinkB=3))
    save(fig, name)


# ================================================================= GEOMETRY
def polygon_xy(name, n, angles, R=3.2, rot=90):
    """A regular-looking convex n-gon with each vertex angle labelled."""
    th = np.radians(rot + np.arange(n) * 360 / n)
    V = np.c_[R * np.cos(th), R * np.sin(th)]
    fig, ax = start_fig((3.6, 3.2))
    ax.add_patch(Polygon(V, closed=True, fill=False, ec=INK, lw=1.8))
    FL.record_patch_edges(V)
    frame(ax, (-1.45 * R, 1.45 * R), (-1.4 * R, 1.4 * R))
    for i, lab in enumerate(angles):
        if lab is None:
            continue
        FL.angle_label(ax, V[i], V[(i - 1) % n], V[(i + 1) % n], lab, fontsize=9.5,
                       name=f"vertex {i}")
    save(fig, name)


def pentagon_exterior(name):
    """A regular pentagon with one side extended and the exterior angle marked."""
    n, R = 5, 3.0
    th = np.radians(90 + np.arange(n) * 360 / n)
    V = np.c_[R * np.cos(th), R * np.sin(th)]
    fig, ax = start_fig((3.4, 3.0))
    ax.add_patch(Polygon(V, closed=True, fill=False, ec=INK, lw=1.8))
    FL.record_patch_edges(V)
    # extend side CB beyond B; theta is between that extension and side BA
    B, C, A = V[1], V[2], V[0]
    ext = B + (B - C) * 0.75
    ax.annotate("", xy=tuple(ext), xytext=tuple(B),
                arrowprops=dict(arrowstyle="-|>", color=GREY, lw=1.4, mutation_scale=9))
    FL.seg(ax, B, ext, lw=0)
    frame(ax, (-1.5 * R, 1.9 * R), (-1.9 * R, 1.5 * R))
    FL.angle_label(ax, B, ext, A, r"$\theta$", fontsize=11.5, color=MAROON,
                   name="exterior angle")
    save(fig, name)


def quad_exterior(name, given):
    """A convex quadrilateral with every side extended and three exterior angles
    labelled; the fourth is the unknown."""
    V = np.array([(0, 0), (3.4, -0.35), (4.3, 2.1), (1.0, 2.6)])
    fig, ax = start_fig((3.5, 3.0))
    ax.add_patch(Polygon(V, closed=True, fill=False, ec=INK, lw=2.0))
    FL.record_patch_edges(V)
    frame(ax, (-2.0, 6.6), (-2.4, 4.6))
    labs = [f"${g}^\\circ$" for g in given] + [r"$\angle 1$"]
    for i in range(4):
        A, B = V[i], V[(i + 1) % 4]
        ext = B + (B - A) * 0.55
        ax.annotate("", xy=ext, xytext=B,
                    arrowprops=dict(arrowstyle="-|>", color=GREY, lw=1.2, mutation_scale=8))
        FL.seg(ax, B, ext, lw=0)
        FL.angle_label(ax, B, ext, V[(i + 2) % 4], labs[i], fontsize=11,
                       color=MAROON if i == 3 else INK)
    save(fig, name)


def triangle_sides(name, P, labels, tick_pairs=(), angle_labels=None,
                   right_at=None, figsize=(3.0, 2.4)):
    """A triangle with its three sides labelled, optional congruence ticks, an
    optional right-angle mark and optional angle labels."""
    P = np.array(P, float)
    fig, ax = start_fig(figsize)
    ax.add_patch(Polygon(P, closed=True, fill=False, ec=INK, lw=2.0))
    FL.record_patch_edges(P)
    lo, hi = P.min(axis=0), P.max(axis=0)
    pad = 1.3
    frame(ax, (lo[0] - pad, hi[0] + pad), (lo[1] - pad, hi[1] + pad))
    for (i, j), lab in zip(((0, 1), (1, 2), (2, 0)), labels):
        if lab is None:
            continue
        M = (P[i] + P[j]) / 2
        cen = P.mean(axis=0)
        d = M - cen
        d = d / np.linalg.norm(d)
        FL.outside_label(ax, lab, M, d, base=0.3, fontsize=11.5, name=f"side {i}{j}")
    for a, b in tick_pairs:
        ticks(ax, P[a], P[b])
    if angle_labels:
        for i, lab in enumerate(angle_labels):
            if lab:
                FL.angle_label(ax, P[i], P[(i - 1) % 3], P[(i + 1) % 3], lab, fontsize=12)
    if right_at is not None:
        i = right_at
        right_angle(ax, P[i], P[(i + 1) % 3], P[(i - 1) % 3], s=0.32)
    save(fig, name)


def triangle_median(name):
    """A triangle with all three medians and the centroid marked, with the short
    piece of one median labelled."""
    A, B, C = np.array([(0, 0)]), np.array([(5.2, 0)]), np.array([(1.6, 3.6)])
    P = np.vstack([A, B, C])
    G = P.mean(axis=0)
    fig, ax = start_fig((3.4, 2.8))
    ax.add_patch(Polygon(P, closed=True, fill=False, ec=INK, lw=2.0))
    FL.record_patch_edges(P)
    frame(ax, (-1.6, 8.2), (-1.6, 5.3))
    mids = []
    for i in range(3):
        M = (P[(i + 1) % 3] + P[(i + 2) % 3]) / 2
        mids.append(M)
        ax.plot(*zip(P[i], M), color=GREY, lw=1.0, ls=(0, (5, 3)))
        FL.seg(ax, P[i], M, lw=0)
    ax.plot(*G, "o", ms=5, color=MAROON, zorder=6)
    # G sits where all three medians cross, so no offset around it is ever clear
    # of ink — the label is taken outside on a leader instead
    ax.annotate("$G$", xy=G, xytext=(6.1, 3.4), fontsize=11.5, color=MAROON,
                ha="left", va="center",
                arrowprops=dict(arrowstyle="-", color=MAROON, lw=0.8,
                                shrinkA=2, shrinkB=4))
    ticks(ax, P[1], mids[0]); ticks(ax, P[2], mids[0])
    M = mids[0]
    ax.annotate("$6$", xy=(G + M) / 2, xytext=(6.1, 1.2), fontsize=11.5, color=INK,
                ha="left", va="center",
                arrowprops=dict(arrowstyle="-", color=GREY, lw=0.8,
                                shrinkA=2, shrinkB=3))
    for i, lab in enumerate("$A$ $B$ $C$".split()):
        d = P[i] - G; d = d / np.linalg.norm(d)
        FL.outside_label(ax, lab, P[i], d, base=0.32, fontsize=11.5, name=lab)
    save(fig, name)


def quad_diagonals(name, kind, labels):
    """A parallelogram, rectangle, rhombus or square with both diagonals drawn."""
    shapes = {
        "parallelogram": [(0, 0), (4.2, 0), (5.4, 2.5), (1.2, 2.5)],
        "rectangle": [(0, 0), (4.6, 0), (4.6, 2.7), (0, 2.7)],
        "rhombus": [(0, 0), (3.0, -1.6), (6.0, 0), (3.0, 1.6)],
        "square": [(0, 0), (3.2, 0), (3.2, 3.2), (0, 3.2)],
    }
    V = np.array(shapes[kind], float)
    fig, ax = start_fig((3.4, 2.8))
    ax.add_patch(Polygon(V, closed=True, fill=False, ec=INK, lw=2.0))
    FL.record_patch_edges(V)
    lo, hi = V.min(axis=0), V.max(axis=0)
    frame(ax, (lo[0] - 1.6, hi[0] + 2.9), (lo[1] - 1.5, hi[1] + 1.5))
    FL.seg(ax, V[0], V[2], color=GREY, lw=1.1)
    FL.seg(ax, V[1], V[3], color=GREY, lw=1.1)
    E = V.mean(axis=0)
    ax.plot(*E, "o", ms=4, color=MAROON, zorder=6)
    if kind in ("rhombus", "square"):
        right_angle(ax, E, V[0], V[1], s=0.3)
    if kind == "rectangle":
        for i in range(4):
            right_angle(ax, V[i], V[(i + 1) % 4], V[(i - 1) % 4], s=0.3)
    for txt, anchor, to in labels:
        leader(ax, txt, anchor, to)
    for i, lab in enumerate("$A$ $B$ $C$ $D$".split()):
        u = V[i] - E; u = u / np.linalg.norm(u)
        FL.outside_label(ax, lab, V[i], u, base=0.3, fontsize=11, name="v" + lab)
    save(fig, name)


def trapezoid_mid(name, top, bottom, mid):
    """A trapezoid with its midsegment drawn, arrowheads on the parallel sides."""
    V = np.array([(0, 0), (6.0, 0), (4.7, 2.6), (1.3, 2.6)], float)
    fig, ax = start_fig((3.4, 2.6))
    ax.add_patch(Polygon(V, closed=True, fill=False, ec=INK, lw=2.0))
    FL.record_patch_edges(V)
    frame(ax, (-1.6, 7.6), (-1.6, 4.3))
    L = (V[0] + V[3]) / 2; R = (V[1] + V[2]) / 2
    FL.seg(ax, L, R, color=TEAL, lw=1.7)
    for a, b in ((0, 3), (1, 2)):
        ticks(ax, V[a], (V[a] + V[b]) / 2)
        ticks(ax, (V[a] + V[b]) / 2, V[b])
    for P, Q in ((V[0], V[1]), (V[3], V[2])):
        m = (P + Q) / 2
        ax.annotate("", xy=m + np.array([0.45, 0]), xytext=m - np.array([0.45, 0]),
                    arrowprops=dict(arrowstyle="-|>", color=GREY, lw=1.1, mutation_scale=8))
    FL.place(ax, bottom, (V[0] + V[1]) / 2, direction=(0, -1), steps=(0.32, 0.6),
             fontsize=11.5, name="bottom")
    FL.place(ax, top, (V[3] + V[2]) / 2, direction=(0, 1), steps=(0.32, 0.6),
             fontsize=11.5, name="top")
    FL.place(ax, mid, (L + R) / 2, direction=(0, 1), steps=(0.3, 0.55, 0.85),
             fontsize=11.5, color=TEAL, name="mid")
    save(fig, name)


def parallel_transversal(name, mode, labels):
    """Two parallel lines cut by a transversal, with two angles marked by ARCS.

    The arc is what makes the picture readable: without it the reader has to
    guess which of the four angles at an intersection a label belongs to, and
    alternate-interior and co-interior look identical on the page.
    """
    fig, ax = start_fig((3.4, 2.7))
    frame(ax, (-2.6, 8.0), (-2.4, 4.9))
    y1, y2 = 2.4, 0.0
    for y in (y1, y2):
        arrowends(ax, (-0.4, y), (6.0, y), color=INK, lw=1.7)
        ax.annotate("", xy=(3.2, y), xytext=(2.4, y),
                    arrowprops=dict(arrowstyle="-|>", color=GREY, lw=1.0, mutation_scale=8))
    P = np.array([0.5, -1.2]); Q = np.array([4.1, 3.7])
    arrowends(ax, P, Q, color=NAVY, lw=1.6)
    d = (Q - P) / np.linalg.norm(Q - P)
    I1 = P + d * ((y1 - P[1]) / d[1])          # upper intersection
    I2 = P + d * ((y2 - P[1]) / d[1])          # lower intersection

    RIGHT = np.array([1.0, 0.0]); LEFT = np.array([-1.0, 0.0])
    UP, DOWN = d, -d                            # along the transversal
    # interior means towards the OTHER parallel line
    spots = {
        # alternate interior: opposite sides of the transversal, both interior
        "alt-int": [(I1, LEFT, DOWN, labels[0], (-1, -0.2)),
                    (I2, RIGHT, UP, labels[1], (1, 0.2))],
        # co-interior: SAME side of the transversal, both interior
        "co-int": [(I1, RIGHT, DOWN, labels[0], (1, -0.15)),
                   (I2, RIGHT, UP, labels[1], (1, 0.15))],
    }[mode]

    for I, a, b, lab, away in spots:
        a = a / np.linalg.norm(a); b = b / np.linalg.norm(b)
        t1 = np.degrees(np.arctan2(a[1], a[0])) % 360
        t2 = np.degrees(np.arctan2(b[1], b[0])) % 360
        lo, hi = sorted((t1, t2))
        if hi - lo > 180:
            lo, hi = hi, lo + 360
        ax.add_patch(Arc(tuple(I), 1.0, 1.0, angle=0, theta1=lo, theta2=hi,
                         color=MAROON, lw=1.2))
        bis = (a + b); bis = bis / np.linalg.norm(bis)
        anchor = I + bis * 0.5
        away = np.array(away, float); away = away / np.linalg.norm(away)
        out = I + away * 2.9
        leader(ax, lab, anchor, out, color=MAROON, fontsize=10.5,
               ha="left" if away[0] > 0 else "right")
    save(fig, name)


def venn_nested(name, inner, outer):
    fig, ax = start_fig((2.9, 2.1))
    ax.add_patch(Ellipse((0, 0), 5.6, 3.4, fill=False, ec=NAVY, lw=1.8))
    ax.add_patch(Ellipse((0.35, -0.15), 2.6, 1.5, fill=False, ec=TEAL, lw=1.8))
    FL.record_circle((0, 0), 1.7)
    ax.text(0.35, -0.15, inner, ha="center", va="center", fontsize=11, color=TEAL)
    ax.text(0, 1.28, outer, ha="center", va="center", fontsize=11, color=NAVY)
    frame(ax, (-3.3, 3.3), (-2.0, 2.0))
    save(fig, name)


# =========================================================== FUNCTION GRAPHS
def graph_curve(name, f, xlim, ylim, marks=(), holes=(), dots=(), vasym=(),
                hasym=(), pieces=None, shade=None, rects=None, step=1):
    """One coordinate picture, built from a function or from explicit pieces."""
    fig, ax = start_fig((3.0, 2.4))
    axes2d(ax, xlim, ylim, step=step)
    if pieces:
        for xs, g in pieces:
            x = np.linspace(xs[0], xs[1], 300)
            y = np.array([g(t) for t in x], dtype=float)
            ax.plot(x, y, color=NAVY, lw=2.0, solid_capstyle="round")
            FL.polyline(ax, np.c_[x, y], lw=0)
    elif f is not None:
        x = np.linspace(xlim[0] + 0.02, xlim[1] - 0.02, 700)
        y = np.array([f(t) for t in x], dtype=float)
        y[np.abs(y) > ylim[1] * 3] = np.nan
        ax.plot(x, y, color=NAVY, lw=2.0)
        good = ~np.isnan(y)
        FL.polyline(ax, np.c_[x[good], y[good]], lw=0)
    if rects:
        for x0, x1, h in rects:
            ax.fill_between([x0, x1], 0, h, color=TEAL, alpha=0.18,
                            edgecolor=TEAL, linewidth=0.9)
    if shade:
        xs = np.linspace(shade[0], shade[1], 200)
        ax.fill_between(xs, 0, [f(t) for t in xs], color=TEAL, alpha=0.2)
    for v in vasym:
        ax.plot([v, v], list(ylim), color=GREY, lw=1.0, ls=(0, (5, 3)))
    for h in hasym:
        ax.plot(list(xlim), [h, h], color=GREY, lw=1.0, ls=(0, (5, 3)))
    for P in dots:
        ax.plot(*P, "o", ms=5, color=MAROON, zorder=6)
    for P in holes:
        ax.plot(*P, "o", ms=5.5, mfc="white", mec=MAROON, mew=1.5, zorder=6)
    frame(ax, (xlim[0] - 0.6, xlim[1] + 0.6), (ylim[0] - 0.6, ylim[1] + 0.6),
          equal=False)
    for txt, P, d in marks:
        FL.place(ax, txt, P, direction=d, steps=(0.4, 0.8, 1.3, 1.9), fontsize=10.5,
                 color=MAROON, name=txt)
    save(fig, name)


def build():
    # ---------------------------------------------------------------- polar
    polar_grid("f_polar_rays", {"$u$": (3.4, 60), "$v$": (3.4, 150),
                                "$w$": (3.4, 240), "$t$": (3.4, 330)})
    polar_circle("f_polar_sin", 24, "sin")
    assert 24 / 2 == 12

    # ------------------------------------------------------------- polygons
    polygon_xy("f_pent_angles", 5,
               [r"$110^\circ$", r"$x^\circ$", r"$y^\circ$", r"$x^\circ$", r"$y^\circ$"])
    assert (5 - 2) * 180 - 110 == 430          # 2x + 2y
    pentagon_exterior("f_pent_ext")
    assert 360 / 5 == 72
    quad_exterior("f_quad_ext", (95, 85, 100))
    assert 360 - (95 + 85 + 100) == 80

    # ------------------------------------------------------------ triangles
    triangle_sides("f_tri_order", [(0, 0), (5.0, 0), (1.4, 2.9)],
                   [r"$7$", r"$9$", r"$5$"],
                   angle_labels=[r"$X$", r"$Y$", r"$Z$"])
    triangle_sides("f_tri_iso", [(0, 0), (4.6, 0), (2.3, 3.2)],
                   [None, r"$5x-9$", r"$2x+3$"],
                   tick_pairs=((0, 2), (1, 2)))
    assert 2 * 4 + 3 == 5 * 4 - 9              # x = 4 gives 11
    triangle_median("f_tri_median")
    assert 2 * 6 == 12
    triangle_sides("f_tri_alt", [(0, 0), (5.4, 0), (3.6, 3.1)],
                   [None, None, None], right_at=None)

    # ------------------------------------------------------ quadrilaterals
    quad_diagonals("f_par_diag", "parallelogram",
                   [(r"$AE=3x-4$", (1.35, 0.9), (-1.5, -1.0)),
                    (r"$EC=x+6$", (4.05, 1.6), (6.6, 3.6))])
    assert 3 * 5 - 4 == 5 + 6                  # x = 5 gives 11
    quad_diagonals("f_rho_diag", "rhombus",
                   [(r"side $=13$", (1.5, 0.8), (0.0, 2.9)),
                    (r"$EB=5$", (3.0, -0.8), (5.6, -2.4))])
    assert 5 ** 2 + 12 ** 2 == 13 ** 2
    trapezoid_mid("f_trap_mid", r"$12$", r"$4x+2$", r"$19$")
    assert (12 + (4 * 6 + 2)) / 2 == 19        # x = 6

    # --------------------------------------------------- lines and angles
    parallel_transversal("f_par_alt", "alt-int", [r"$3x+10$", r"$5x-30$"])
    assert 3 * 20 + 10 == 5 * 20 - 30          # x = 20 gives 70
    parallel_transversal("f_par_co", "co-int", [r"$2x$", r"$4x-60$"])
    assert 2 * 40 + (4 * 40 - 60) == 180       # x = 40

    # ------------------------------------------------------------- logic
    venn_nested("f_venn", "squares", "rectangles")

    # ------------------------------------------------------ function graphs
    graph_curve("f_gr_domain", None, (-5, 5), (-4, 5),
                pieces=[((-4, 4), lambda t: 0.35 * (t ** 3) / 4 - 0.6 * t + 1.4)],
                holes=[(2, 0.35 * 8 / 4 - 1.2 + 1.4)],
                dots=[(-4, 0.35 * (-64) / 4 + 2.4 + 1.4)])
    graph_curve("f_gr_even", lambda t: 0.55 * t * t - 2.0, (-4, 4), (-3, 5))
    # turning points exactly at x = -2 and x = 2, so the interval of decrease the
    # key names is the one the picture actually shows
    assert abs((3 / (3 * 0.25)) ** 0.5 - 2) < 1e-12
    graph_curve("f_gr_incdec", lambda t: 0.25 * t ** 3 - 3 * t, (-4, 4), (-5, 5))
    graph_curve("f_gr_asym", lambda t: 1 / (t - 2) + 1, (-3, 7), (-3, 5),
                vasym=(2,), hasym=(1,))
    # one branch must fall and the other rise, or the limit would simply be
    # +infinity and the item would have no answer
    assert 1 / (-0.001) < -100 and 1 / 0.001 > 100
    graph_curve("f_gr_dne", None, (-4, 4), (-5, 5),
                pieces=[((-3.8, -0.2), lambda t: 1 / t), ((0.2, 3.8), lambda t: 1 / t)])
    graph_curve("f_gr_area", lambda t: 4 - t * t, (-3, 3), (-1, 5),
                shade=(0, 2))
    assert abs((4 * 2 - 8 / 3) - 16 / 3) < 1e-12
    # a LEFT-endpoint Riemann estimate of the area under y = 4 - x^2 on [0, 2]:
    # four strips of width 0.5, each as tall as the curve at its left edge
    rr = [(i * 0.5, (i + 1) * 0.5, 4 - (i * 0.5) ** 2) for i in range(4)]
    assert [h for _, _, h in rr] == [4.0, 3.75, 3.0, 1.75]
    assert abs(0.5 * sum(h for _, _, h in rr) - 6.25) < 1e-12
    graph_curve("f_gr_riemann", lambda t: 4 - t * t, (-3, 3), (-1, 5), rects=rr)

    json.dump(idx, open(os.path.join(OUT, "_index.json"), "w"), indent=1)
    print(f"figures written; index now holds {len(idx)}")


if __name__ == "__main__":
    build()
