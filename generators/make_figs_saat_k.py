"""Figures for part K of the SAAT booklet — the revision compilation.

Four drawings. Each asserts its own numbers, and the one carrying an angle is
built from that angle rather than placed by eye.

    python3 make_figs_saat_k.py
"""
import json, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle, Rectangle
import figlabel as FL
from make_figs_saat_f import (start_fig, save, frame, axes2d, right_angle, ticks,
                              leader, idx, OUT,
                              NAVY, INK, TEAL, GREY, GRID, MAROON)
from make_figs_saat_g import arc_between

ANG = lambda V, P, Q: np.degrees(np.arccos(
    np.dot(P - V, Q - V) / (np.linalg.norm(P - V) * np.linalg.norm(Q - V))))


# ------------------------------------- a force and its two components, angle t
def force_resultant(name):
    """A force F drawn at an unlabelled angle with both components shown.

    The question asks what is true for EVERY angle, so the drawing deliberately
    uses a general-looking angle rather than a special one."""
    deg = 38.0                      # nothing special: 38 is not a nice angle
    assert deg not in (30, 45, 60)
    L = 4.6
    tip = L * np.array([np.cos(np.radians(deg)), np.sin(np.radians(deg))])
    assert abs(ANG(np.zeros(2), np.array([1.0, 0.0]), tip) - deg) < 1e-9

    fig, ax = start_fig((3.2, 2.3))
    frame(ax, (-2.0, 7.8), (-1.8, 5.2))
    O = np.zeros(2)
    axes2d(ax, (-1.4, 7.0), (-1.2, 4.6), step=1, grid=False)
    ax.annotate("", xy=tip, xytext=O,
                arrowprops=dict(arrowstyle="-|>", color=MAROON, lw=2.2, mutation_scale=12))
    FL.seg(ax, O, tip, lw=0)
    for end in (np.array([tip[0], 0.0]), np.array([0.0, tip[1]])):
        ax.annotate("", xy=end, xytext=O,
                    arrowprops=dict(arrowstyle="-|>", color=TEAL, lw=1.5,
                                    linestyle=(0, (4, 3)), mutation_scale=10))
    # the dashed rectangle that closes the parallelogram
    for a, b in ((np.array([tip[0], 0.0]), tip), (np.array([0.0, tip[1]]), tip)):
        ax.plot(*zip(a, b), color=GREY, lw=1.0, ls=(0, (3, 3)))
    arc_between(ax, O, np.array([1.0, 0.0]), tip, r=1.0)
    FL.angle_label(ax, O, np.array([1.0, 0.0]), tip, r"$\theta$",
                   steps=[1.9, 2.3, 2.8], fontsize=11, name="th")
    leader(ax, r"$F$", tip * 0.78, (6.4, 4.7), fontsize=12, color=MAROON, ha="left")
    save(fig, name)


# ------------------------------------------- four angle pairs, one refutes it
def adjacent_angle_cases(name):
    """Four pairs of adjacent angles. Exactly ONE pair is not complementary —
    it is the counterexample the question asks the student to pick out."""
    pairs = [("A", 40.0, 50.0), ("B", 55.0, 35.0),
             ("C", 70.0, 65.0), ("D", 25.0, 65.0)]
    bad = [p[0] for p in pairs if abs(p[1] + p[2] - 90) > 1e-9]
    assert bad == ["C"], bad            # exactly one refutes "always complementary"

    fig, axs = plt.subplots(1, 4, figsize=(6.6, 1.9))
    for ax, (tag, a, b) in zip(axs, pairs):
        FL.reset()
        ax.set_xlim(-1.5, 1.5); ax.set_ylim(-0.55, 1.65)
        ax.set_aspect("equal"); ax.axis("off")
        V = np.zeros(2)
        for d in (0.0, a, a + b):
            r = np.radians(d)
            ax.annotate("", xy=(1.15 * np.cos(r), 1.15 * np.sin(r)), xytext=V,
                        arrowprops=dict(arrowstyle="-", color=INK, lw=1.6))
        arc_between(ax, V, np.array([1.0, 0.0]),
                    np.array([np.cos(np.radians(a)), np.sin(np.radians(a))]), r=0.36)
        arc_between(ax, V, np.array([np.cos(np.radians(a)), np.sin(np.radians(a))]),
                    np.array([np.cos(np.radians(a + b)), np.sin(np.radians(a + b))]),
                    r=0.52, color=TEAL)
        for d, val in ((a / 2, a), (a + b / 2, b)):
            r = np.radians(d)
            ax.text(0.78 * np.cos(r), 0.78 * np.sin(r), r"$%d^{\circ}$" % round(val),
                    fontsize=8.5, color=INK, ha="center", va="center")
        ax.text(0, -0.42, tag, fontsize=10.5, color=MAROON, ha="center",
                va="center", fontweight="bold")
    p = os.path.join(OUT, name + ".png")
    fig.savefig(p, dpi=400, transparent=True, bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)
    from PIL import Image
    with Image.open(p) as im:
        idx[name] = {"file": p, "aspect": im.width / im.height}


# --------------------------------------------------- a wheel on the coordinates
def wheel_on_axes(name):
    """A circle touching the origin with its top at (0, 30): centre (0, 15),
    radius 15, so the polar equation is r = 30 sin(theta)."""
    R, top = 15.0, 30.0
    assert 2 * R == top
    fig, ax = start_fig((2.5, 2.7))
    frame(ax, (-27.0, 27.0), (-9.0, 39.0))
    axes2d(ax, (-24.0, 24.0), (-6.0, 36.0), step=6, grid=False)
    ax.add_patch(Circle((0, R), R, fill=False, ec=NAVY, lw=2.0))
    FL.record_circle((0, R), R)
    for P in ((0.0, 0.0), (0.0, top)):
        ax.plot(*P, "o", ms=5, color=MAROON, zorder=6)
    leader(ax, r"$(0,\,30)$", (0.0, top), (13.0, 36.0), fontsize=10,
           color=MAROON, ha="left")
    leader(ax, r"$(0,\,0)$", (0.0, 0.0), (13.0, -7.0), fontsize=10,
           color=MAROON, ha="left")
    save(fig, name)


# ----------------------------------------------------- a two-leg walking path
def walk_path(name):
    """8 km north then 6 km east. The PATH is 14; the DISPLACEMENT is 10."""
    a, b = 8.0, 6.0
    assert a * a + b * b == 10.0 ** 2
    O, M, E = np.array([0.0, 0.0]), np.array([0.0, a]), np.array([b, a])

    fig, ax = start_fig((2.8, 2.6))
    frame(ax, (-4.4, 11.0), (-2.6, 11.6))
    for P, Q in ((O, M), (M, E)):
        ax.annotate("", xy=Q, xytext=P,
                    arrowprops=dict(arrowstyle="-|>", color=NAVY, lw=2.0, mutation_scale=11))
        FL.seg(ax, P, Q, lw=0)
    ax.plot(*zip(O, E), color=MAROON, lw=1.8, ls=(0, (5, 3)))
    FL.seg(ax, O, E, lw=0)
    right_angle(ax, M, O, E, s=0.8)
    FL.outside_label(ax, r"$8\ \mathrm{km}$", (O + M) / 2, (-1, 0), base=0.5,
                     fontsize=10.5, name="leg1")
    FL.outside_label(ax, r"$6\ \mathrm{km}$", (M + E) / 2, (0, 1), base=0.5,
                     fontsize=10.5, name="leg2")
    leader(ax, r"$?$", (O + E) / 2, (8.4, 1.2), fontsize=12, color=MAROON, ha="left")
    save(fig, name)


def build():
    force_resultant("kx_force_res")
    adjacent_angle_cases("kx_adj_cases")
    wheel_on_axes("kx_wheel")
    walk_path("kx_walk")
    assert 8 + 6 == 14 and 8 ** 2 + 6 ** 2 == 100   # path 14, displacement 10

    json.dump(idx, open(os.path.join(OUT, "_index.json"), "w"), indent=1)
    print(f"part-K figures written; index now holds {len(idx)}")


if __name__ == "__main__":
    build()
