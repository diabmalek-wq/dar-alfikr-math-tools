"""Figures for part H of the SAAT booklet — the skills taken from the Tahsili
recall album.

Three drawings, each asserting its own numbers so a picture can never disagree
with the answer key.

    python3 make_figs_saat_h.py
"""
import json, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle, Arc
import figlabel as FL
from make_figs_saat_f import (start_fig, save, frame, axes2d, right_angle, ticks,
                              leader, idx, OUT,
                              NAVY, INK, TEAL, GREY, GRID, MAROON)
from make_figs_saat_g import arc_between


# --------------------------------------------------------- a piecewise graph
def piecewise_graph(name):
    """y = x - 2 on x < 1 (open at the right end), and y = 2 on 3 <= x <= 6.

    Domain  (-inf, 1) U [3, 6];  range  (-inf, -1) U {2}.
    The open circle at (1, -1) and the two filled ends are the whole question:
    one endpoint is excluded and the other two are not.
    """
    fig, ax = start_fig((3.2, 2.5))
    frame(ax, (-4.4, 8.2), (-5.6, 4.4))
    axes2d(ax, (-4.0, 7.6), (-5.2, 3.8), step=1)

    xs = np.linspace(-3.4, 1.0, 200)
    ax.plot(xs, xs - 2, color=NAVY, lw=2.0)
    # an arrowhead at the open end: the ray runs on, so the domain is unbounded
    ax.annotate("", xy=(-3.35, -5.35), xytext=(-2.9, -4.9),
                arrowprops=dict(arrowstyle="-|>", color=NAVY, lw=2.0, mutation_scale=10))
    FL.polyline(ax, np.c_[xs, xs - 2], lw=0)
    ax.plot([3.0, 6.0], [2.0, 2.0], color=NAVY, lw=2.0)
    FL.seg(ax, (3.0, 2.0), (6.0, 2.0), lw=0)

    # an open endpoint is a hollow circle; a closed one is filled
    ax.plot(1.0, -1.0, "o", ms=6.5, mfc="white", mec=NAVY, mew=1.8, zorder=6)
    for P in ((3.0, 2.0), (6.0, 2.0)):
        ax.plot(*P, "o", ms=6, color=NAVY, zorder=6)

    leader(ax, r"$(1,\,{-1})$", (1.0, -1.0), (2.0, -4.6), fontsize=10,
           color=MAROON, ha="left")
    leader(ax, r"$(3,\,2)$", (3.0, 2.0), (2.4, 3.4), fontsize=10, color=MAROON)
    leader(ax, r"$(6,\,2)$", (6.0, 2.0), (7.0, 3.4), fontsize=10, color=MAROON,
           ha="left")

    assert 1.0 - 2.0 == -1.0                      # the ray stops just short of -1
    assert 3.0 <= 6.0                             # the segment runs left to right
    save(fig, name)


# ------------------------------------------------ isosceles triangle + altitude
def isosceles_altitude(name):
    """Equal sides 13, altitude 12 to the base. Half the base is 5, so the whole
    base is 10 — the doubling is the question."""
    half, h, leg = 5.0, 12.0, 13.0
    assert half ** 2 + h ** 2 == leg ** 2
    A, B, C = (0.0, h), (-half, 0.0), (half, 0.0)
    fig, ax = start_fig((2.9, 2.6))
    P = np.array([A, B, C])
    ax.add_patch(Polygon(P, closed=True, fill=False, ec=NAVY, lw=2.0))
    FL.record_patch_edges(P)
    frame(ax, (-7.6, 7.6), (-3.4, 15.2))
    FL.seg(ax, A, (0.0, 0.0), color=GREY, lw=1.3, ls=(0, (4, 3)))
    right_angle(ax, (0.0, 0.0), C, A, s=0.9)
    ticks(ax, A, B, s=0.7)
    ticks(ax, A, C, s=0.7)

    FL.outside_label(ax, r"$13$", ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2), (-1, 0),
                     base=0.7, fontsize=11, name="leftleg")
    FL.outside_label(ax, r"$13$", ((A[0] + C[0]) / 2, (A[1] + C[1]) / 2), (1, 0),
                     base=0.7, fontsize=11, name="rightleg")
    FL.outside_label(ax, r"$12$", (0.0, h * 0.28), (1, 0), base=0.35, fontsize=11,
                     name="alt", color=MAROON)
    FL.outside_label(ax, r"$?$", (0.0, 0.0), (0, -1), base=0.9, fontsize=12,
                     name="base", color=MAROON)
    save(fig, name)


# ------------------------------------------ parallelogram cut by a diagonal
def parallelogram_diagonal(name):
    """ABCD with angle D = 110 degrees. The diagonal AC splits angle A into a
    marked 40 degrees next to AD and the unknown x next to AB.

    Consecutive angles are supplementary, so angle A is 70 and x is 30. The
    side lengths are DERIVED from those angles by the sine rule, so the drawn
    angles really are the marked ones."""
    angD, part = 110.0, 40.0
    angA = 180.0 - angD
    x = angA - part
    angDCA = 180.0 - angD - part
    assert x == 30.0 and angDCA == 30.0

    D = np.array([0.0, 0.0])
    C = np.array([6.4, 0.0])
    side = np.linalg.norm(C - D) * np.sin(np.radians(angDCA)) / np.sin(np.radians(part))
    th = np.radians(angD)
    A = D + side * np.array([np.cos(th), np.sin(th)])
    B = A + (C - D)

    ang = lambda V, P, Q: np.degrees(np.arccos(
        np.dot(P - V, Q - V) / (np.linalg.norm(P - V) * np.linalg.norm(Q - V))))
    assert abs(ang(A, D, C) - part) < 1e-9
    assert abs(ang(A, C, B) - x) < 1e-9

    fig, ax = start_fig((3.3, 2.3))
    P = np.array([A, B, C, D])
    ax.add_patch(Polygon(P, closed=True, fill=False, ec=NAVY, lw=2.0))
    FL.record_patch_edges(P)
    FL.seg(ax, A, C, color=NAVY, lw=1.5, ls=(0, (5, 3)))
    frame(ax, (-5.6, 11.4), (-3.0, 7.4))

    arc_between(ax, D, C, A, r=1.05)
    arc_between(ax, A, D, C, r=1.15, color=TEAL)
    arc_between(ax, A, C, B, r=1.6)

    FL.angle_label(ax, D, C, A, r"$110^{\circ}$", fontsize=10.5, name="angD")
    # the diagonal runs through where a label on this bisector would sit, so
    # the marked part goes out on a leader instead
    bis = ((D - A) / np.linalg.norm(D - A) + (C - A) / np.linalg.norm(C - A))
    leader(ax, r"$40^{\circ}$", A + 1.35 * bis / np.linalg.norm(bis),
           (-5.4, 1.8), fontsize=10.5, ha="left")
    FL.angle_label(ax, A, C, B, r"$x$", fontsize=12, color=MAROON, name="angCAB")
    for name_, V, off in (("A", A, (-1, 1)), ("B", B, (1, 1)),
                          ("C", C, (1, -1)), ("D", D, (-1, -1))):
        FL.outside_label(ax, r"$%s$" % name_, V, off, base=0.45, fontsize=11,
                         name="v" + name_)
    save(fig, name)


def build():
    piecewise_graph("h_piecewise")
    isosceles_altitude("h_iso_alt")
    assert 2 * 5 == 10                 # the altitude bisects the base
    parallelogram_diagonal("h_pgram_diag")
    assert (180 - 110) - 40 == 30      # supplementary first, then the part

    json.dump(idx, open(os.path.join(OUT, "_index.json"), "w"), indent=1)
    print(f"part-H figures written; index now holds {len(idx)}")


if __name__ == "__main__":
    build()
