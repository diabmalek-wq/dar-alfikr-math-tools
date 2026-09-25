"""Figures for part I of the SAAT booklet — the eleventh ETEC sample paper.

Four drawings, each asserting its own numbers so a picture can never disagree
with the answer key.

    python3 make_figs_saat_i.py
"""
import json, os
from itertools import combinations
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle
import figlabel as FL
from make_figs_saat_f import (start_fig, save, frame, axes2d, right_angle, ticks,
                              leader, idx, OUT,
                              NAVY, INK, TEAL, GREY, GRID, MAROON)
from make_figs_saat_g import arc_between


# ------------------------------------------------------- law of sines triangle
def sine_rule_triangle(name):
    """Angle A = 60, angle B = 45, side b = 14 opposite B, x opposite A.

    The triangle is BUILT from the two angles and that one side, so the drawn
    shape really is the one the numbers describe."""
    angA, angB = 60.0, 45.0
    angC = 180.0 - angA - angB
    assert angC == 75.0
    b = 14.0
    a = b * np.sin(np.radians(angA)) / np.sin(np.radians(angB))     # the answer
    c = b * np.sin(np.radians(angC)) / np.sin(np.radians(angB))
    assert abs(a - 7 * np.sqrt(6)) < 1e-9, a

    # place A at the origin with AB along the x-axis
    A = np.array([0.0, 0.0])
    B = A + np.array([c, 0.0])
    C = A + b * np.array([np.cos(np.radians(angA)), np.sin(np.radians(angA))])
    assert abs(np.linalg.norm(C - B) - a) < 1e-9

    fig, ax = start_fig((3.6, 2.2))
    P = np.array([A, B, C])
    ax.add_patch(Polygon(P, closed=True, fill=False, ec=NAVY, lw=2.0))
    FL.record_patch_edges(P)
    frame(ax, (-5.6, 24.6), (-4.6, 16.8))

    arc_between(ax, A, B, C, r=1.5)
    arc_between(ax, B, A, C, r=1.5, color=TEAL)

    FL.angle_label(ax, A, B, C, r"$60^{\circ}$", fontsize=10.5, name="angA")
    FL.angle_label(ax, B, A, C, r"$45^{\circ}$", fontsize=10.5, name="angB")
    FL.outside_label(ax, r"$14$", (A + C) / 2, (-1, 0), base=0.6, fontsize=11,
                     name="sideb")
    FL.outside_label(ax, r"$x$", (B + C) / 2, (1, 1), base=0.6, fontsize=12,
                     name="sidex", color=MAROON)
    for nm, V, off in (("A", A, (0, -1)), ("B", B, (1, -1)), ("C", C, (0, 1))):
        FL.outside_label(ax, r"$%s$" % nm, V, off, base=0.5, fontsize=11,
                         name="v" + nm)
    save(fig, name)


# --------------------------------------------------- square inside a square
def midpoint_square(name):
    """A square with the midpoints of its sides joined. The inner square always
    has exactly half the area, whatever the side length."""
    s = 10.0
    V = np.array([(0, 0), (s, 0), (s, s), (0, s)], float)
    M = np.array([(s / 2, 0), (s, s / 2), (s / 2, s), (0, s / 2)])
    area_out = s * s
    area_in = 0.5 * np.abs(np.dot(M[:, 0], np.roll(M[:, 1], -1))
                           - np.dot(np.roll(M[:, 0], -1), M[:, 1]))
    assert abs(area_in / area_out - 0.5) < 1e-12, area_in / area_out

    fig, ax = start_fig((2.7, 2.6))
    # fill and outline are separate patches: alpha on one patch would wash the
    # edge out along with the shading
    ax.add_patch(Polygon(M, closed=True, facecolor=TEAL, alpha=0.30, lw=0))
    ax.add_patch(Polygon(M, closed=True, fill=False, ec=NAVY, lw=1.6))
    ax.add_patch(Polygon(V, closed=True, fill=False, ec=NAVY, lw=2.0))
    FL.record_patch_edges(V)
    FL.record_patch_edges(M)
    frame(ax, (-4.2, 14.6), (-3.4, 12.4))
    for P in M:
        ax.plot(*P, "o", ms=4.5, color=MAROON, zorder=6)
    FL.outside_label(ax, r"$10\ \mathrm{cm}$", (s / 2, 0), (0, -1), base=0.6,
                     fontsize=10.5, name="base")
    save(fig, name)


# ------------------------------------------------------------ a 3 by 3 lattice
def lattice_points(name):
    """Nine points in a 3 by 3 grid. Eight of the 84 triples are collinear:
    three rows, three columns and the two diagonals."""
    pts = [(i, j) for j in range(3) for i in range(3)]
    coll = [t for t in combinations(pts, 3)
            if abs((t[1][0] - t[0][0]) * (t[2][1] - t[0][1])
                   - (t[2][0] - t[0][0]) * (t[1][1] - t[0][1])) < 1e-12]
    assert len(list(combinations(pts, 3))) == 84
    assert len(coll) == 8, len(coll)

    fig, ax = start_fig((2.4, 2.4))
    frame(ax, (-0.65, 2.65), (-0.65, 2.65))
    for x, y in pts:
        ax.plot(x, y, "o", ms=7, color=NAVY, zorder=6)
        FL.record_circle((x, y), 0.13)
    save(fig, name)


# ------------------------------------------ a shaded square-root inequality
def radical_inequality(name):
    """y = sqrt(x + 2) with the region BELOW it shaded — so the inequality is
    y <= sqrt(x + 2), and the endpoint at x = -2 fixes the shift."""
    h = -2.0
    assert np.sqrt(0 - h) == np.sqrt(2)          # the curve cuts x = 0 at root 2
    xs = np.linspace(h, 7.0, 400)
    ys = np.sqrt(xs - h)

    fig, ax = start_fig((3.1, 2.4))
    frame(ax, (-4.6, 8.4), (-4.2, 4.6))
    axes2d(ax, (-4.2, 7.8), (-3.8, 4.0), step=1)
    # the inequality only lives where the root is defined, so nothing left of
    # the endpoint is shaded
    ax.fill_between(xs, -3.8, ys, color=TEAL, alpha=0.22, lw=0, zorder=1)
    ax.plot(xs, ys, color=NAVY, lw=2.2, zorder=4)
    FL.polyline(ax, np.c_[xs, ys], lw=0)
    ax.plot(h, 0.0, "o", ms=6, color=MAROON, zorder=6)
    leader(ax, r"$({-2},\,0)$", (h, 0.0), (-4.4, 2.9), fontsize=10,
           color=MAROON, ha="left")
    save(fig, name)


def build():
    sine_rule_triangle("i_sine_rule")
    midpoint_square("i_mid_square")
    lattice_points("i_grid_points")
    radical_inequality("i_rad_ineq")

    json.dump(idx, open(os.path.join(OUT, "_index.json"), "w"), indent=1)
    print(f"part-I figures written; index now holds {len(idx)}")


if __name__ == "__main__":
    build()
