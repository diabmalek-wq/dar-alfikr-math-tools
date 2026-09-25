"""Figures for part J of the SAAT booklet — the three recalled summer papers.

Seven drawings. Every one asserts its own numbers, and the two that carry
angles BUILD the shape from those angles rather than placing a vertex by eye.

    python3 make_figs_saat_j.py
"""
import json, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle, Rectangle, Wedge
import figlabel as FL
from make_figs_saat_f import (start_fig, save, frame, axes2d, right_angle, ticks,
                              leader, idx, OUT,
                              NAVY, INK, TEAL, GREY, GRID, MAROON)
from make_figs_saat_g import arc_between

ANG = lambda V, P, Q: np.degrees(np.arccos(
    np.dot(P - V, Q - V) / (np.linalg.norm(P - V) * np.linalg.norm(Q - V))))


# ------------------------------------------------------ a force on an incline
def force_components(name):
    """A 120 N pull at 30° above the horizontal, with its two components drawn.

    The arrow really is at 30°, so a student measuring the picture gets the
    same angle the stem states."""
    deg = 30.0
    L = 5.0
    tip = L * np.array([np.cos(np.radians(deg)), np.sin(np.radians(deg))])
    assert abs(ANG(np.zeros(2), np.array([1.0, 0.0]), tip) - deg) < 1e-9

    fig, ax = start_fig((3.4, 2.0))
    frame(ax, (-1.6, 8.4), (-1.9, 4.2))
    # the ground line and the block
    ax.plot([-1.0, 7.6], [0, 0], color=INK, lw=1.6)
    FL.seg(ax, (-1.0, 0), (7.6, 0), lw=0)
    ax.add_patch(Rectangle((-0.5, 0), 1.6, 1.0, fill=False, ec=INK, lw=1.6))
    FL.record_patch_edges(np.array([(-0.5, 0), (1.1, 0), (1.1, 1.0), (-0.5, 1.0)]))

    O = np.array([1.1, 0.5])
    ax.annotate("", xy=O + tip, xytext=O,
                arrowprops=dict(arrowstyle="-|>", color=MAROON, lw=2.0, mutation_scale=12))
    FL.seg(ax, O, O + tip, lw=0)
    # the two components, dashed
    for end in (O + np.array([tip[0], 0.0]), O + np.array([0.0, tip[1]])):
        ax.annotate("", xy=end, xytext=O,
                    arrowprops=dict(arrowstyle="-|>", color=TEAL, lw=1.4,
                                    linestyle=(0, (4, 3)), mutation_scale=9))
    arc_between(ax, O, O + np.array([1.0, 0.0]), O + tip, r=1.1)
    # the 30 degree gap is narrow and the dashed component runs through its
    # bisector, so the label goes out on a leader
    FL.angle_label(ax, O, O + np.array([1.0, 0.0]), O + tip, r"$30^{\circ}$",
                   steps=[2.0, 2.4, 2.9, 3.5], fontsize=10.5, name="ang")
    leader(ax, r"$120\ \mathrm{N}$", O + tip * 0.72, (6.6, 3.9), fontsize=11,
           color=MAROON, ha="left")
    save(fig, name)


# -------------------------------------------- pentagon with one side produced
def pentagon_exterior(name):
    """A regular pentagon with one side produced. x is the interior angle at
    that vertex and y the exterior angle beside it — a linear pair, so their
    sum is 180 whatever the polygon."""
    R = 2.3
    th = np.radians(90 + np.arange(5) * 72)
    V = np.c_[R * np.cos(th), R * np.sin(th)]
    # produce the side V[1] -> V[0] beyond V[0]
    d = (V[0] - V[1]) / np.linalg.norm(V[0] - V[1])
    P = V[0] + d * 2.3
    interior = ANG(V[0], V[1], V[4])
    exterior = ANG(V[0], P, V[4])
    assert abs(interior - 108) < 1e-9, interior
    assert abs(exterior - 72) < 1e-9, exterior
    assert abs(interior + exterior - 180) < 1e-9

    fig, ax = start_fig((3.0, 2.6))
    ax.add_patch(Polygon(V, closed=True, fill=False, ec=INK, lw=1.9))
    FL.record_patch_edges(V)
    ax.annotate("", xy=P, xytext=V[0],
                arrowprops=dict(arrowstyle="-|>", color=GREY, lw=1.5, mutation_scale=10))
    FL.seg(ax, V[0], P, lw=0)
    frame(ax, (-5.8, 6.8), (-3.6, 6.0))
    arc_between(ax, V[0], V[1], V[4], r=0.85)
    arc_between(ax, V[0], P, V[4], r=0.6, color=TEAL)
    bx = ((V[1] - V[0]) / np.linalg.norm(V[1] - V[0])
          + (V[4] - V[0]) / np.linalg.norm(V[4] - V[0]))
    leader(ax, r"$x$", V[0] + 1.0 * bx / np.linalg.norm(bx), (-5.4, 5.0),
           fontsize=12, color=MAROON, ha="left")
    # the produced ray runs through the bisector of the exterior angle, so y
    # goes outside on a leader rather than on top of the arrow
    bis = ((P - V[0]) / np.linalg.norm(P - V[0])
           + (V[4] - V[0]) / np.linalg.norm(V[4] - V[0]))
    leader(ax, r"$y$", V[0] + 0.75 * bis / np.linalg.norm(bis), (5.4, 5.0),
           fontsize=12, color=MAROON, ha="left")
    save(fig, name)


# ------------------------------------------------ a square cut by a diagonal
def square_diagonal(name):
    """x and y are the two acute angles of the triangle the diagonal makes and
    z is the right angle at the corner — the three angles of ONE triangle."""
    s = 3.0
    V = np.array([(0, 0), (s, 0), (s, s), (0, s)], float)
    A, B, C = V[0], V[1], V[2]
    assert abs(ANG(A, B, C) + ANG(B, C, A) + ANG(C, A, B) - 180) < 1e-9
    assert abs(ANG(B, A, C) - 90) < 1e-9        # the corner really is square

    fig, ax = start_fig((2.6, 2.5))
    ax.add_patch(Polygon(V, closed=True, fill=False, ec=NAVY, lw=2.0))
    FL.record_patch_edges(V)
    FL.seg(ax, A, C, color=GREY, lw=1.5)
    frame(ax, (-1.5, 4.5), (-1.5, 4.4))
    right_angle(ax, B, A, C, s=0.35)
    FL.angle_label(ax, A, B, C, r"$x$", fontsize=12, color=MAROON, name="xa")
    FL.angle_label(ax, C, A, B, r"$y$", fontsize=12, color=MAROON, name="ya")
    leader(ax, r"$z$", B + np.array([-0.55, 0.55]), (4.3, -1.2), fontsize=12,
           color=MAROON)
    save(fig, name)


# --------------------------------------------- two squares on a common line
def stacked_squares(name):
    """Squares of side 7 and 5 standing on one line. The marked segment runs
    from the far bottom-left corner to the top-right corner of the second, so
    its legs are 12 and 5 — a 5-12-13 hidden inside a stair figure."""
    a, b = 7.0, 5.0
    run, rise = a + b, b
    assert run ** 2 + rise ** 2 == 13.0 ** 2

    fig, ax = start_fig((3.4, 2.2))
    S1 = np.array([(0, 0), (a, 0), (a, a), (0, a)])
    S2 = np.array([(a, 0), (a + b, 0), (a + b, b), (a, b)])
    for S in (S1, S2):
        ax.add_patch(Polygon(S, closed=True, fill=False, ec=INK, lw=1.8))
        FL.record_patch_edges(S)
    frame(ax, (-3.2, 15.6), (-2.6, 9.4))
    P, Q = np.array([0.0, 0.0]), np.array([a + b, b])
    ax.plot(*zip(P, Q), color=MAROON, lw=2.0)
    FL.seg(ax, P, Q, lw=0)
    FL.outside_label(ax, r"$7$", (a / 2, a), (0, 1), base=0.35, fontsize=11, name="s1")
    FL.outside_label(ax, r"$5$", (a + b / 2, b), (0, 1), base=0.35, fontsize=11, name="s2")
    leader(ax, r"$?$", (P + Q) / 2, (5.6, -2.2), fontsize=12, color=MAROON)
    save(fig, name)


# ------------------------------------------------------------ a Greek cross
def greek_cross(name):
    """A plus sign: four axes of symmetry — two through the arms and two
    diagonal. Counting each axis as two rays is the trap, and gives eight."""
    t = 1.0
    P = np.array([(-t, -3 * t), (t, -3 * t), (t, -t), (3 * t, -t), (3 * t, t),
                  (t, t), (t, 3 * t), (-t, 3 * t), (-t, t), (-3 * t, t),
                  (-3 * t, -t), (-t, -t)], float)
    # the shape really is symmetric in all four axes
    for M in (np.array([[-1, 0], [0, 1]]), np.array([[1, 0], [0, -1]]),
              np.array([[0, 1], [1, 0]]), np.array([[0, -1], [-1, 0]])):
        R = P @ M.T
        assert sorted(map(tuple, np.round(R, 9))) == sorted(map(tuple, np.round(P, 9)))

    fig, ax = start_fig((2.5, 2.5))
    ax.add_patch(Polygon(P, closed=True, facecolor=TEAL, alpha=0.25, lw=0))
    ax.add_patch(Polygon(P, closed=True, fill=False, ec=NAVY, lw=2.0))
    FL.record_patch_edges(P)
    frame(ax, (-4.4, 4.4), (-4.4, 4.4))
    save(fig, name)


# ------------------------------------------------- two perpendicular medians
def perpendicular_medians(name):
    """Medians from A and B meet at right angles. The triangle is CONSTRUCTED
    so that they do, and the construction is checked before the figure ships."""
    mA, mB = 12.0, 9.0                     # the two median lengths
    # put the centroid at the origin with the two 2/3 pieces along the axes
    G = np.zeros(2)
    A = G + np.array([2 * mA / 3, 0.0])
    B = G + np.array([0.0, 2 * mB / 3])
    # C follows from A + B + C = 3G
    C = 3 * G - A - B
    MA = (B + C) / 2                       # midpoint of the side opposite A
    MB = (A + C) / 2
    assert abs(np.linalg.norm(A - MA) - mA) < 1e-9
    assert abs(np.linalg.norm(B - MB) - mB) < 1e-9
    assert abs(np.dot(A - G, B - G)) < 1e-9            # the medians are perpendicular
    assert abs(np.linalg.norm(A - B) - 10.0) < 1e-9    # the answer

    fig, ax = start_fig((3.2, 2.6))
    T = np.array([A, B, C])
    ax.add_patch(Polygon(T, closed=True, fill=False, ec=NAVY, lw=2.0))
    FL.record_patch_edges(T)
    for V, M in ((A, MA), (B, MB)):
        FL.seg(ax, V, M, color=GREY, lw=1.4, ls=(0, (4, 3)))
    ticks(ax, B, MA, s=0.5); ticks(ax, C, MA, s=0.5)
    ticks(ax, A, MB, n=2, s=0.5); ticks(ax, C, MB, n=2, s=0.5)
    right_angle(ax, G, A, B, s=0.9)
    lo = T.min(axis=0); hi = T.max(axis=0)
    frame(ax, (lo[0] - 4.2, hi[0] + 4.2), (lo[1] - 3.0, hi[1] + 3.0))
    for nm, V, off in (("A", A, (1, -1)), ("B", B, (0, 1)), ("C", C, (-1, -1))):
        FL.outside_label(ax, r"$%s$" % nm, V, off, base=0.6, fontsize=11, name="v" + nm)

    save(fig, name)


# --------------------------------------------- the upper half of a circle
def semicircle_area(name):
    """y = sqrt(9 - x^2) on [-3, 3] — the UPPER half of the circle of radius 3,
    shaded, so the integral is half of 9*pi."""
    r = 3.0
    xs = np.linspace(-r, r, 400)
    ys = np.sqrt(r * r - xs * xs)
    # the drawn curve really is the semicircle
    assert np.allclose(xs ** 2 + ys ** 2, r * r)

    fig, ax = start_fig((3.0, 2.0))
    frame(ax, (-5.2, 5.4), (-2.4, 4.6))
    axes2d(ax, (-4.8, 5.0), (-2.0, 4.2), step=1)
    ax.fill_between(xs, 0, ys, color=TEAL, alpha=0.25, lw=0, zorder=1)
    ax.plot(xs, ys, color=NAVY, lw=2.2, zorder=4)
    FL.polyline(ax, np.c_[xs, ys], lw=0)
    for P in ((-r, 0.0), (r, 0.0)):
        ax.plot(*P, "o", ms=5, color=MAROON, zorder=6)
    leader(ax, r"${-3}$", (-r, 0.0), (-5.0, -1.9), fontsize=10, color=MAROON, ha="left")
    leader(ax, r"$3$", (r, 0.0), (4.4, -1.9), fontsize=10, color=MAROON)
    save(fig, name)


def build():
    force_components("jx_force")
    pentagon_exterior("jx_pent_ext")
    assert 108 + 72 == 180
    square_diagonal("jx_square_diag")
    stacked_squares("jx_stacked_sq")
    assert 12 ** 2 + 5 ** 2 == 169
    greek_cross("jx_symmetry")
    perpendicular_medians("jx_perp_medians")
    assert 8 ** 2 + 6 ** 2 == 100
    semicircle_area("jx_semicircle")

    json.dump(idx, open(os.path.join(OUT, "_index.json"), "w"), indent=1)
    print(f"part-J figures written; index now holds {len(idx)}")


if __name__ == "__main__":
    build()
