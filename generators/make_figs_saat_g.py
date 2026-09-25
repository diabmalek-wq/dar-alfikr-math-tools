"""Figures for part G of the SAAT booklet — the ninth sample paper, plus the
sample-paper skills the earlier parts had not reached.

Every number a figure carries is ASSERTED here, so a picture can never disagree
with the answer key. Labels go through figlabel, which refuses to place one on
top of the drawing; where no offset can ever be clear the label is taken outside
on a leader line.

    python3 make_figs_saat_g.py
"""
import json, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle, Arc, Rectangle
import figlabel as FL
from make_figs_saat_f import (start_fig, save, frame, axes2d, right_angle, ticks,
                              arrowends, leader, idx, OUT,
                              NAVY, INK, TEAL, GREY, GRID, MAROON)


# ------------------------------------------------------- trig from a triangle
def tri_trig(name):
    """A right triangle whose two legs are labelled with sin x and cos x."""
    P = np.array([(0, 0), (3.4, 0), (0, 2.4)], float)
    fig, ax = start_fig((2.8, 2.3))
    ax.add_patch(Polygon(P, closed=True, fill=False, ec=INK, lw=2.0))
    FL.record_patch_edges(P)
    frame(ax, (-1.7, 4.6), (-1.4, 3.6))
    right_angle(ax, P[0], P[1], P[2], s=0.32)
    FL.outside_label(ax, r"$\cos x$", (P[0] + P[1]) / 2, (0, -1), base=0.35,
                     fontsize=11, name="base")
    FL.outside_label(ax, r"$\sin x$", (P[0] + P[2]) / 2, (-1, 0), base=0.35,
                     fontsize=11, name="height")
    FL.angle_label(ax, P[1], P[0], P[2], r"$x$", fontsize=11)
    save(fig, name)


def rect_with_triangle(name):
    """A rectangle with a right triangle on its right-hand side, 30° at the far
    base vertex — the composite-area setting."""
    fig, ax = start_fig((3.4, 2.2))
    frame(ax, (-2.8, 9.4), (-1.9, 4.4))
    a, b = 4.0, 2.0                      # rectangle 4 by 2
    R = np.array([(0, 0), (a, 0), (a, b), (0, b)])
    ax.add_patch(Polygon(R, closed=True, fill=False, ec=INK, lw=2.0))
    FL.record_patch_edges(R)
    # the triangle: right angle at (a, 0), hypotenuse 4, angle 30 at the far vertex
    far = (a + 4.0 * np.cos(np.radians(30)), 0.0)
    T = np.array([(a, 0), far, (a, b)])
    ax.add_patch(Polygon(T, closed=True, fill=False, ec=INK, lw=2.0))
    FL.record_patch_edges(T)
    right_angle(ax, T[0], T[1], T[2], s=0.3)
    FL.angle_label(ax, T[1], T[0], T[2], r"$30^{\circ}$", fontsize=10)
    leader(ax, r"$4\ \mathrm{cm}$", ((a + far[0]) / 2, b / 2 + 0.2), (8.0, 3.4))
    FL.outside_label(ax, r"$4\ \mathrm{cm}$", (a / 2, b), (0, 1), base=0.3,
                     fontsize=10.5, name="top")
    FL.outside_label(ax, r"$2\ \mathrm{cm}$", (0, b / 2), (-1, 0), base=0.3,
                     fontsize=10.5, name="left")
    assert abs(4.0 * np.sin(np.radians(30)) - 2.0) < 1e-12   # the triangle closes
    save(fig, name)


def circle_radius(name, label):
    fig, ax = start_fig((2.4, 2.2))
    frame(ax, (-2.4, 2.9), (-2.1, 2.1))
    ax.add_patch(Circle((0, 0), 1.5, fill=False, ec=NAVY, lw=1.9))
    FL.record_circle((0, 0), 1.5)
    ax.plot(0, 0, "o", ms=4, color=INK)
    FL.seg(ax, (0, 0), (1.5, 0), color=GREY, lw=1.2)
    leader(ax, label, (0.75, 0.0), (0.2, -1.75), fontsize=11)
    save(fig, name)


# --------------------------------------------------------- coordinate figures
def trap_on_axes(name):
    """An isosceles trapezoid placed on the axes with literal coordinates.

    It sits a little away from the origin so that no coordinate label has to
    share paper with an axis."""
    fig, ax = start_fig((3.3, 2.5))
    frame(ax, (-2.6, 9.2), (-2.6, 5.6))
    axes2d(ax, (-1.6, 8.6), (-1.6, 5.0), step=1, grid=False)
    a, b, c = 1.3, 5.6, 3.0
    V = np.array([(0, 0), (b + a, 0), (b, c), (a, c)], float)
    ax.add_patch(Polygon(V, closed=True, fill=False, ec=NAVY, lw=2.0))
    FL.record_patch_edges(V)
    ticks(ax, V[0], V[3]); ticks(ax, V[1], V[2])
    leader(ax, r"$(0,\ 0)$", V[0], (-2.4, -1.6), fontsize=10, ha="left")
    leader(ax, r"$(a+b,\ 0)$", V[1], (7.4, -1.6), fontsize=10)
    leader(ax, r"$(a,\ c)$", V[3], (-2.4, 4.4), fontsize=10, ha="left")
    leader(ax, r"$M$", V[2], (7.6, 4.4), fontsize=11, color=MAROON)
    save(fig, name)


def tri_on_axes(name):
    """A right triangle with two vertices on the x-axis and the apex above."""
    fig, ax = start_fig((3.0, 2.4))
    frame(ax, (-4.6, 6.4), (-2.4, 5.0))
    axes2d(ax, (-4.2, 6.0), (-1.2, 4.6), step=1)
    A, B, C = (-3.0, 0.0), (3.0, 0.0), (3.0, 4.0)
    P = np.array([A, B, C])
    ax.add_patch(Polygon(P, closed=True, fill=False, ec=NAVY, lw=2.0))
    FL.record_patch_edges(P)
    right_angle(ax, B, A, C, s=0.4)
    leader(ax, r"$A({-3},\,0)$", A, (-4.4, -2.0), fontsize=10, ha="left")
    leader(ax, r"$B(3,\,0)$", B, (4.4, -2.0), fontsize=10)
    leader(ax, r"$C$", C, (4.6, 4.4), fontsize=11, color=MAROON)
    save(fig, name)


def radical_graph(name):
    """y = a*sqrt(x - h) + k, drawn so the endpoint and one more lattice point
    are both exactly on the grid."""
    a, h, k = 2.0, 1.0, -1.0
    assert a * np.sqrt(5 - h) + k == 3.0            # (5, 3) is a lattice point
    x = np.linspace(h, 8.0, 400)
    y = a * np.sqrt(x - h) + k
    fig, ax = start_fig((3.0, 2.4))
    frame(ax, (-2.2, 9.0), (-2.9, 6.0))
    axes2d(ax, (-1.6, 8.4), (-2.4, 5.4), step=1)
    ax.plot(x, y, color=NAVY, lw=2.0)
    FL.polyline(ax, np.c_[x, y], lw=0)
    for P in ((h, k), (5.0, 3.0)):
        ax.plot(*P, "o", ms=5, color=MAROON, zorder=6)
    leader(ax, r"$(1,\,{-1})$", (h, k), (2.6, -2.4), fontsize=10, color=MAROON,
           ha="left")
    leader(ax, r"$(5,\,3)$", (5.0, 3.0), (6.4, 4.8), fontsize=10, color=MAROON)
    save(fig, name)


# ------------------------------------------------------------------ geometry
def pentagon_with_triangle(name):
    """A regular pentagon with an isosceles triangle standing on its BOTTOM side.

    The apex height is DERIVED from the base angle the question states — each
    base angle equals the pentagon's exterior angle, 72° — so the drawn triangle
    really is the one the question describes. An arbitrary height would make the
    picture contradict the stem, which is exactly the fault this rebuild fixes.
    """
    R = 1.55
    ext = 360.0 / 5                                   # exterior angle, 72
    th = np.radians(90 + np.arange(5) * 72)
    V = np.c_[R * np.cos(th), R * np.sin(th)]
    # the side whose midpoint is lowest is the bottom one
    mids = [((V[i] + V[(i + 1) % 5]) / 2, i) for i in range(5)]
    mid, i = min(mids, key=lambda t: t[0][1])
    A, B = V[i], V[(i + 1) % 5]
    half = np.linalg.norm(B - A) / 2
    out = mid / np.linalg.norm(mid)                   # pentagon centred on origin
    apex = mid + out * half * np.tan(np.radians(ext))  # base angles are now 72

    ang = lambda P, Q, S: np.degrees(np.arccos(
        np.dot(Q - P, S - P) / (np.linalg.norm(Q - P) * np.linalg.norm(S - P))))
    assert abs(ang(A, B, apex) - ext) < 1e-9, ang(A, B, apex)
    assert abs(ang(B, A, apex) - ext) < 1e-9, ang(B, A, apex)
    assert abs(ang(apex, A, B) - (180 - 2 * ext)) < 1e-9   # the answer, 36
    assert abs(np.linalg.norm(apex - A) - np.linalg.norm(apex - B)) < 1e-12
    assert apex[1] < min(V[:, 1]) - 0.2, "the apex must fall clear of the pentagon"

    fig, ax = start_fig((2.6, 3.4))
    ax.add_patch(Polygon(V, closed=True, fill=False, ec=INK, lw=1.9))
    FL.record_patch_edges(V)
    T = np.array([A, B, apex])
    ax.add_patch(Polygon(T, closed=True, fill=False, ec=NAVY, lw=1.9))
    FL.record_patch_edges(T)
    # the congruence marks go on the UPPER half of each equal side, so the
    # apex angle keeps clear paper for its label
    ticks(ax, A, (A + apex) / 2, s=0.22)
    ticks(ax, B, (B + apex) / 2, s=0.22)
    frame(ax, (-2.5 * R, 2.5 * R), (apex[1] - 0.9, 1.45 * R))
    FL.angle_label(ax, apex, A, B, r"$x$", fontsize=11.5, color=MAROON,
                   name="apex angle")
    save(fig, name)


def triangle_cevian(name):
    """A triangle with a median to the base, the two base pieces and one side
    labelled with linear expressions."""
    A, B, C = np.array([(2.6, 3.4)]), np.array([(5.6, 0.0)]), np.array([(0.0, 0.0)])
    P = np.vstack([A, B, C])
    D = (B + C) / 2
    fig, ax = start_fig((3.4, 2.6))
    ax.add_patch(Polygon(P, closed=True, fill=False, ec=INK, lw=2.0))
    FL.record_patch_edges(P)
    frame(ax, (-1.8, 8.4), (-1.9, 4.9))
    FL.seg(ax, A[0], D[0], color=GREY, lw=1.2)
    ticks(ax, C[0], D[0]); ticks(ax, D[0], B[0])
    for lab, P_, dvec in ((r"$A$", A[0], (0, 1)), (r"$B$", B[0], (1, -0.4)),
                          (r"$C$", C[0], (-1, -0.4)), (r"$D$", D[0], (0, -1))):
        FL.outside_label(ax, lab, P_, dvec, base=0.32, fontsize=11, name=lab)
    leader(ax, r"$CD=3x-5$", (C[0] + D[0]) / 2, (-1.6, -1.4), fontsize=10,
           ha="left")
    leader(ax, r"$DB=x+7$", (D[0] + B[0]) / 2, (6.3, -1.4), fontsize=10)
    leader(ax, r"$AC=2x+4$", (A[0] + C[0]) / 2, (-1.6, 4.2), fontsize=10,
           ha="left")
    save(fig, name)


def centroid_fig(name):
    """A triangle with its three medians, the centroid marked and the short
    piece of one median labelled."""
    P = np.array([(0, 0), (5.8, 0), (1.9, 3.9)], float)
    G = P.mean(axis=0)
    fig, ax = start_fig((3.4, 2.7))
    ax.add_patch(Polygon(P, closed=True, fill=False, ec=INK, lw=2.0))
    FL.record_patch_edges(P)
    frame(ax, (-1.6, 8.6), (-1.6, 5.4))
    mids = []
    for i in range(3):
        M = (P[(i + 1) % 3] + P[(i + 2) % 3]) / 2
        mids.append(M)
        ax.plot(*zip(P[i], M), color=GREY, lw=1.0, ls=(0, (5, 3)))
        FL.seg(ax, P[i], M, lw=0)
    ax.plot(*G, "o", ms=5, color=MAROON, zorder=6)
    leader(ax, r"$F$", G, (6.4, 3.4), fontsize=11, color=MAROON)
    leader(ax, r"$FT=5$", (G + mids[2]) / 2, (6.4, 1.0), fontsize=10.5)
    FL.outside_label(ax, r"$T$", mids[2], (0, -1), base=0.32, fontsize=11, name="T")
    for i, lab in enumerate(("$A$", "$B$", "$C$")):
        d = P[i] - G; d = d / np.linalg.norm(d)
        FL.outside_label(ax, lab, P[i], d, base=0.32, fontsize=11, name=lab)
    save(fig, name)


def arc_between(ax, V, P, Q, r=1.1, color=MAROON):
    """An arc at V spanning the angle from ray VP to ray VQ, the short way."""
    V, P, Q = map(lambda t: np.asarray(t, float), (V, P, Q))
    t1 = np.degrees(np.arctan2(*(P - V)[::-1])) % 360
    t2 = np.degrees(np.arctan2(*(Q - V)[::-1])) % 360
    lo, hi = sorted((t1, t2))
    if hi - lo > 180:
        lo, hi = hi, lo + 360
    ax.add_patch(Arc(tuple(V), 2 * r, 2 * r, theta1=lo, theta2=hi,
                     color=color, lw=1.2))


def congruence_pair(name):
    """Two triangles on opposite sides of a shared side, with one pair of sides
    and one pair of angles marked — the postulate-identification setting."""
    fig, ax = start_fig((3.3, 2.6))
    frame(ax, (-2.6, 8.8), (-4.6, 4.4))
    A, C = np.array([0.0, 0.0]), np.array([6.0, 0.0])
    B, D = np.array([2.2, 2.6]), np.array([3.8, -2.6])
    for T in (np.array([A, C, B]), np.array([A, C, D])):
        ax.add_patch(Polygon(T, closed=True, fill=False, ec=INK, lw=1.9))
        FL.record_patch_edges(T)
    ticks(ax, A, B); ticks(ax, C, D)          # one congruent pair of sides
    ticks(ax, A, C, n=2)                       # the shared side
    arc_between(ax, A, C, B)                   # angle BAC
    arc_between(ax, C, A, D)                   # angle DCA
    for lab, P_, d in ((r"$A$", A, (-1, 0.2)), (r"$C$", C, (1, 0.2)),
                       (r"$B$", B, (0, 1)), (r"$D$", D, (0, -1))):
        FL.outside_label(ax, lab, P_, d, base=0.5, fontsize=11, name=lab)
    save(fig, name)


def vertical_angles(name):
    """Two lines crossing, with the two VERTICAL angles numbered — the pair that
    shares a vertex but no side."""
    fig, ax = start_fig((2.8, 2.1))
    frame(ax, (-3.4, 3.4), (-2.6, 2.6))
    O = np.array([0.0, 0.0])
    for ang in (25, 115):
        d = np.array([np.cos(np.radians(ang)), np.sin(np.radians(ang))])
        arrowends(ax, tuple(O - d * 2.7), tuple(O + d * 2.7), color=INK, lw=1.6)
    u = np.array([np.cos(np.radians(25)), np.sin(np.radians(25))])
    v = np.array([np.cos(np.radians(115)), np.sin(np.radians(115))])
    FL.angle_label(ax, O, O + u * 2, O + v * 2, r"$1$", fontsize=11, color=MAROON)
    FL.angle_label(ax, O, O - u * 2, O - v * 2, r"$2$", fontsize=11, color=MAROON)
    save(fig, name)


# ------------------------------------------------------------------ diagrams
def venn3(name, counts):
    """Three overlapping circles with a count in each of the seven regions."""
    fig, ax = start_fig((3.2, 2.9))
    frame(ax, (-3.4, 3.4), (-3.2, 3.2))
    R = 1.65
    cs = [(-0.85, 0.55), (0.85, 0.55), (0.0, -0.95)]
    for c in cs:
        ax.add_patch(Circle(c, R, fill=False, ec=NAVY, lw=1.7))
    spots = {
        "a": (-1.6, 1.1), "b": (1.6, 1.1), "c": (0.0, -1.95),
        "ab": (0.0, 1.25), "ac": (-1.05, -0.55), "bc": (1.05, -0.55),
        "abc": (0.0, -0.1),
    }
    for k, (x, y) in spots.items():
        ax.text(x, y, str(counts[k]), ha="center", va="center",
                fontsize=11, color=INK)
    for lab, (x, y) in (("Maths", (-2.3, 2.25)), ("Physics", (2.3, 2.25)),
                        ("Chemistry", (0.0, -2.95))):
        ax.text(x, y, lab, ha="center", va="center", fontsize=10, color=TEAL)
    save(fig, name)


def bar_chart(name, xs, ps):
    """A discrete probability distribution as a bar chart."""
    fig, ax = start_fig((2.9, 2.3))
    top = max(ps) + 0.12
    frame(ax, (-1.0, max(xs) + 1.4), (-0.12, top + 0.12), equal=False)
    for y in np.arange(0, top, 0.1):
        ax.plot([-0.2, max(xs) + 1.0], [y, y], color=GRID, lw=0.6, zorder=0)
    for x, p in zip(xs, ps):
        ax.add_patch(Rectangle((x - 0.3, 0), 0.6, p, facecolor=TEAL, alpha=0.35,
                               edgecolor=TEAL, lw=1.2))
        ax.text(x, -0.055, str(x), ha="center", va="top", fontsize=9.5, color=INK)
    for y in np.arange(0.1, top, 0.1):
        ax.text(-0.32, y, f"{y:.1f}", ha="right", va="center", fontsize=8.5,
                color=GREY)
    ax.annotate("", xy=(max(xs) + 1.0, 0), xytext=(-0.2, 0),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.1, mutation_scale=9))
    ax.annotate("", xy=(-0.2, top), xytext=(-0.2, 0),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.1, mutation_scale=9))
    ax.text(max(xs) + 1.05, -0.06, "$x$", fontsize=10.5, color=INK, va="top")
    ax.text(-0.2, top + 0.03, "$P(x)$", fontsize=10.5, color=INK,
            ha="center", va="bottom")
    assert abs(sum(ps) - 1.0) < 1e-9, "a distribution must total 1"
    save(fig, name)


def skew_curve(name):
    """A density curve with its long tail to the RIGHT — positively skewed."""
    x = np.linspace(0.02, 9.5, 500)
    y = (x ** 1.6) * np.exp(-x / 1.1)
    y = y / y.max()
    fig, ax = start_fig((2.9, 2.0))
    frame(ax, (-1.0, 10.4), (-0.45, 1.5), equal=False)
    ax.annotate("", xy=(10.0, 0), xytext=(-0.6, 0),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.1, mutation_scale=9))
    ax.annotate("", xy=(-0.6, 1.35), xytext=(-0.6, 0),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.1, mutation_scale=9))
    ax.plot(x, y, color=NAVY, lw=2.0)
    FL.polyline(ax, np.c_[x, y], lw=0)
    peak = x[int(np.argmax(y))]
    assert peak < 3.0 and y[-1] < 0.05, "the long tail must run to the right"
    save(fig, name)


def build():
    tri_trig("g_tri_trig")
    rect_with_triangle("g_rect_tri")
    circle_radius("g_circle_r", r"$r=3x^{3/2}$")
    trap_on_axes("g_trap_coord")
    tri_on_axes("g_tri_coord")
    radical_graph("g_radical")
    pentagon_with_triangle("g_pent_tri")
    triangle_cevian("g_cevian")
    assert 3 * 6 - 5 == 6 + 7          # x = 6 makes the two base pieces equal
    centroid_fig("g_centroid")
    assert 2 * 5 == 10                 # vertex distance is twice the short piece
    congruence_pair("g_congruence")
    vertical_angles("g_vertical")
    venn3("g_venn3", {"a": 7, "b": 5, "c": 6, "ab": 4, "ac": 3, "bc": 2, "abc": 8})
    assert 4 + 8 == 12                 # Maths AND Physics, triple region included
    bar_chart("g_bars", [1, 2, 3, 4], [0.1, 0.3, 0.4, 0.2])
    assert 0.3 + 0.4 == 0.7000000000000001 or abs(0.3 + 0.4 - 0.7) < 1e-9
    skew_curve("g_skew")

    json.dump(idx, open(os.path.join(OUT, "_index.json"), "w"), indent=1)
    print(f"part-G figures written; index now holds {len(idx)}")


if __name__ == "__main__":
    build()
