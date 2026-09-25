"""Figures for the SIMULATED GAT bank.

These are not redrawings of Mr Elsawy's figures. Each one keeps the geometry or
the chart structure that makes its item work and changes everything else — the
numbers, the labelling, and where possible the shape of the picture itself
(circles where the source used rectangles, a clock face where it used a pie,
an octagon where it used a hexagon). The point is that a student who has seen
the original still has to do the work.

Every figure that carries an answer asserts that answer here, so a mistyped
value fails the build instead of shipping an item whose picture disagrees with
its key.
"""
import json, os, shutil
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle, Rectangle, Wedge
import figlabel as FL

plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["DejaVu Serif"]

OUT = "figs_sim"
shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT)

NAVY = "#1F3864"; INK = "#222E2D"; RED = "#C62828"
BLUE = "#3B5BA9"; ORANGE = "#E8762C"; GREY = "#A6A6A6"; GOLD = "#F0B323"
TEAL = "#17A199"; PALE = "#D9D9D9"; GRID = "#DCE9E8"
idx = {}


def start(figsize):
    """Every figure begins by clearing the ink record the label guard tests against."""
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
    """Fix the axes NOW. Label boxes are measured in display space, so the limits
    have to be final before the first label is placed or every measurement is
    taken against a transform that is about to change."""
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    if equal:
        ax.set_aspect("equal")
    ax.axis("off")


def _clean(ax):
    ax.grid(axis="y", color=GRID, lw=0.7); ax.set_axisbelow(True)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)


# ============================================================ GEOMETRY
def medial():
    """Equilateral side 16. Shaded is R-T-B — the MIRROR of the source's piece,
    so a student who memorised 'the left one' still has to think. Area 8*sqrt(3)."""
    s = 16.0
    A = np.array([s / 2, s * np.sqrt(3) / 2]); P = np.array([0.0, 0.0])
    Q = np.array([s, 0.0])
    L = (A + P) / 2; R = (A + Q) / 2; B = (P + Q) / 2; T = (A + B) / 2
    shaded = abs(np.cross(np.append(T - R, 0), np.append(B - R, 0))[2]) / 2
    assert abs(shaded - 8 * np.sqrt(3)) < 1e-9, shaded

    fig, ax = start(figsize=(2.9, 2.5))
    ax.add_patch(Polygon(np.array([R, T, B]), closed=True, fc=TEAL, ec=TEAL))
    for a, b in ((L, T), (T, R), (R, B), (B, L), (A, B)):
        ax.plot([a[0], b[0]], [a[1], b[1]], color="#7A8A89", lw=0.9)
    ax.add_patch(Polygon(np.array([P, Q, A]), closed=True, fill=False, ec=INK, lw=2.2))
    FL.record_patch_edges([P, Q, A])
    for a, b in ((L, T), (T, R), (R, B), (B, L), (A, B)):
        FL.record_patch_edges([a, b], close=False)
    frame(ax, (-0.8, s + 0.8), (-3.0, s * np.sqrt(3) / 2 + 0.6))
    FL.outside_label(ax, "16 cm", (s / 2, 0), (0, -1), base=0.9,
                     fontsize=12, name="medial side")
    return save(fig, "sim_medial")


def similar():
    """Base angles 35 and 60, so the apex is 85 — not the source's 40/60/80."""
    assert 180 - 35 - 60 == 85
    fig, ax = start(figsize=(5.2, 2.4))
    b = 5.0
    t1, t2 = np.tan(np.radians(35)), np.tan(np.radians(60))
    apx = t2 * b / (t1 + t2); apy = t1 * apx
    d = b + 1.1
    tri = {}
    for x0 in (0.0, d):
        pts = [(x0, 0), (x0 + apx, apy), (x0 + b, 0)]
        ax.add_patch(Polygon(np.array(pts), closed=True, fill=False, ec=INK, lw=2.2))
        FL.record_patch_edges(pts)
        tri[x0] = pts
    L0, AP0, R0 = tri[0.0]
    L1, AP1, R1 = tri[d]
    frame(ax, (-0.4, d + b + 0.4), (-0.35, apy + 0.4))
    FL.angle_label(ax, L0, R0, AP0, r"$35^{\circ}$", fontsize=12, name="35 deg")
    FL.angle_label(ax, R1, L1, AP1, r"$60^{\circ}$", fontsize=12, name="60 deg")
    FL.angle_label(ax, AP1, L1, R1, r"$x^{\circ}$", fontsize=12, name="x deg")
    return save(fig, "sim_similar")


def rect_parts():
    """Perimeter 34 with height 5 forces length 12; SIX equal parts of 10 each."""
    H, per, n = 5.0, 34.0, 6
    L = per / 2 - H
    assert L == 12.0 and L * H / n == 10.0
    fig, ax = start(figsize=(4.0, 2.1))
    ax.add_patch(Rectangle((0, 0), L, H, fill=False, ec=NAVY, lw=2.6))
    FL.record_patch_edges([(0, 0), (L, 0), (L, H), (0, H)])
    for i in range(1, n):
        FL.seg(ax, (i * L / n, 0), (i * L / n, H), color=NAVY, lw=1.6)
    frame(ax, (-3.6, L + 0.4), (-0.5, H + 0.5))
    FL.outside_label(ax, "5 cm", (0, H / 2), (-1, 0), base=0.5, fontsize=15,
                     name="rect height")
    return save(fig, "sim_rect_parts")


def circle_tangent():
    """Radius 5, and the shading is MIRRORED into the other pair of
    vertical wedges. Each right triangle has legs r and r, so the pair is r^2 = 25."""
    r = 5.0
    assert 2 * (0.5 * r * r) == 25.0
    fig, ax = start(figsize=(2.9, 2.6))
    ax.add_patch(Circle((0, 0), 1, fill=False, ec=INK, lw=1.7))
    FL.record_circle((0, 0), 1)
    for tri in ([(0, 0), (1, 0), (1, -1)], [(0, 0), (-1, 0), (-1, 1)]):
        ax.add_patch(Polygon(np.array(tri), closed=True, fc=TEAL, ec=TEAL, alpha=0.85))
        FL.record_patch_edges(tri)
    FL.seg(ax, (-1, 0), (1, 0), color=INK, lw=1.7)
    FL.seg(ax, (-1, 1), (1, -1), color=INK, lw=1.7)      # mirrored: down to the right
    FL.seg(ax, (1, 0), (1, -1), color=INK, lw=1.7)
    FL.seg(ax, (-1, 0), (-1, 1), color=INK, lw=1.7)
    for (x, sg) in ((1, 1), (-1, -1)):
        d = 0.11
        ax.add_patch(Rectangle((x - sg * d, -d if sg > 0 else 0), sg * d, d,
                               fc=INK, ec=INK))
    # the 135 is marked in the UNSHADED upper-right wedge, between the rightward
    # radius and the up-left ray, so the label never sits on the shading
    frame(ax, (-1.55, 1.60), (-1.50, 1.50))
    from matplotlib.patches import Arc
    ax.add_patch(Arc((0, 0), 0.66, 0.66, angle=0, theta1=0, theta2=135,
                     color=INK, lw=1.1))
    bis = np.array([1, 0]) + np.array([-1, 1]) / np.sqrt(2)
    bis = bis / np.linalg.norm(bis)
    FL.place(ax, r"$135^{\circ}$", bis * 0.33, direction=bis,
             steps=[0.22, 0.30, 0.40, 0.52, 0.66], fontsize=12, name="135 deg")
    # the lower-left wedge is the only one with neither shading nor a label in it
    FL.outside_label(ax, "O", (0, 0), (-0.40, -0.92), base=0.16, fontsize=13,
                     name="centre O")
    return save(fig, "sim_circle_tangent")


def circle_arcs():
    """Two diameters 74 degrees apart, points renamed P Q R S T.
    Arc PQR = 74, arc PTS = 106."""
    assert 180 - 74 == 106
    fig, ax = start(figsize=(2.7, 2.7))
    ax.add_patch(Circle((0, 0), 1, fill=False, ec=NAVY, lw=1.9))
    FL.record_circle((0, 0), 1)
    ang = {"T": 150, "P": 44, "S": 100, "Q": 8, "R": 330}
    for a in (150, 44):
        t = np.radians(a)
        FL.seg(ax, (np.cos(t), np.sin(t)), (-np.cos(t), -np.sin(t)), color=INK, lw=1.5)
    for k, a in ang.items():
        t = np.radians(a)
        u = (np.cos(t), np.sin(t))
        frame(ax, (-1.55, 1.55), (-1.55, 1.55))
        FL.outside_label(ax, k, u, u, base=0.14, fontsize=13, name="point " + k)
    ax.plot([np.cos(np.radians(8))], [np.sin(np.radians(8))], marker="o", ms=6, color=NAVY)
    # the 74 goes in the wedge between the two leftward halves of the diameters
    lo = np.radians(150); hi = np.radians(44 + 180)
    FL.angle_label(ax, (0, 0), (np.cos(lo), np.sin(lo)), (np.cos(hi), np.sin(hi)),
                   r"$74^{\circ}$", fontsize=12, name="74 deg")
    FL.outside_label(ax, "O", (0, 0), (-0.17, -0.98), base=0.14, fontsize=12,
                     name="centre O")
    return save(fig, "sim_circle_arcs")


def segments():
    """p q r s t u v w, and this time eg = (1/4) of ce, so the ratio is 9/14 —
    a student who remembers 7/11 from the original set gets it wrong."""
    k = 1
    ce, eg, ca = 4 * k, k, 5 * k
    assert (ce + eg + ce) / (2 * ca + ce) == 9 / 14
    fig, ax = start(figsize=(3.6, 1.35))
    W, H = 10.0, 2.0
    ax.add_patch(Rectangle((0, 0), W, H, fill=False, ec=NAVY, lw=2.3))
    FL.record_patch_edges([(0, 0), (W, 0), (W, H), (0, H)])
    for x in (5.0, 9.0):
        FL.seg(ax, (x, 0), (x, H), color=NAVY, lw=1.7)
    for x, top, bot in ((0, "p", "q"), (5.0, "r", "s"), (9.0, "t", "u"), (10.0, "v", "w")):
        dx = -0.30 if top == "t" else 0.30 if top == "v" else 0.0
        frame(ax, (-0.9, 10.9), (-1.5, 3.3))
        FL.outside_label(ax, top, (x + dx, H), (dx * 0.5, 1), base=0.30,
                         fontsize=12, name="vertex " + top)
        FL.outside_label(ax, bot, (x + dx, 0), (dx * 0.5, -1), base=0.30,
                         fontsize=12, name="vertex " + bot)
    return save(fig, "sim_segments")


def venn():
    """Three overlapping CIRCLES with dots, not rectangles with stars.
    P = 6, Q = 5, R = 3;  Q and R = 1;  Q or R = 7."""
    C = {"P": (3.3, 3.0, 2.25), "Q": (5.6, 3.4, 2.05), "R": (5.0, 1.7, 1.75)}
    DOTS = [(2.72, 3.12), (4.00, 3.64), (4.28, 4.44), (4.96, 3.88), (4.72, 2.28),
            (3.80, 1.52), (4.96, 0.92), (5.76, 4.56), (5.68, 6.00), (8.28, 4.24)]
    CLEAR = 0.30      # a dot must be this far from EVERY circle, or it reads as
                      # sitting on the line and the item becomes unanswerable

    def inside(p, c):
        return (p[0] - c[0]) ** 2 + (p[1] - c[1]) ** 2 < c[2] ** 2
    n = {k: sum(inside(d, c) for d in DOTS) for k, c in C.items()}
    both = sum(inside(d, C["Q"]) and inside(d, C["R"]) for d in DOTS)
    either = sum(inside(d, C["Q"]) or inside(d, C["R"]) for d in DOTS)
    assert n == {"P": 6, "Q": 5, "R": 3}, n
    assert (both, either) == (1, 7), (both, either)
    # No dot may sit on a circumference. Counting is the whole question, so a dot
    # the reader cannot place is the same defect as a label lying on a line.
    for d in DOTS:
        for k, (cx, cy, r) in C.items():
            gap = ((d[0] - cx) ** 2 + (d[1] - cy) ** 2) ** 0.5 - r
            assert abs(gap) >= CLEAR, f"dot {d} is only {gap:+.3f} from circle {k}"

    fig, ax = start(figsize=(3.0, 2.4))
    for k, (cx, cy, r) in C.items():
        ax.add_patch(Circle((cx, cy), r, fill=False, ec=NAVY, lw=2.0))
        FL.record_circle((cx, cy), r)
    ax.plot([d[0] for d in DOTS], [d[1] for d in DOTS], "o", ms=7,
            mfc=RED, mec="#7B1010", mew=0.8, ls="none")
    for k, (cx, cy, r) in C.items():                 # names OUTSIDE their circle
        t = np.radians({"P": 152, "Q": 32, "R": 288}[k])
        u = np.array([np.cos(t), np.sin(t)])
        frame(ax, (0.0, 9.9), (-1.6, 7.4))
        FL.outside_label(ax, k, (cx + r * u[0], cy + r * u[1]), u, base=0.30,
                         fontsize=13, name="set " + k)
    return save(fig, "sim_venn")


def clock():
    """A clock FACE with hands, not a pie chart. The item asks how far the minute
    hand turns in one minute: 360 / 60 = 6 degrees."""
    assert 360 / 60 == 6
    fig, ax = start(figsize=(2.4, 2.4))
    ax.add_patch(Circle((0, 0), 1, fill=False, ec=NAVY, lw=2.2))
    for i in range(60):
        t = np.radians(90 - 6 * i)
        r0 = 0.90 if i % 5 else 0.84
        lw = 0.7 if i % 5 else 1.6
        ax.plot([r0 * np.cos(t), np.cos(t)], [r0 * np.sin(t), np.sin(t)],
                color=INK, lw=lw)
    for h in range(1, 13):
        t = np.radians(90 - 30 * h)
        frame(ax, (-1.35, 1.50), (-1.35, 1.60))
        # the dial numerals are decoration, not question data — they do not go
        # through the guard, but they ARE recorded so x has to dodge them
        ax.annotate(str(h), (0.72 * np.cos(t), 0.72 * np.sin(t)), fontsize=8,
                    color=INK, ha="center", va="center")
        FL.record_patch_edges([(0.66 * np.cos(t), 0.66 * np.sin(t)),
                               (0.78 * np.cos(t), 0.78 * np.sin(t))], close=False)
    # one minute of the minute hand, shaded and labelled — that IS the question
    ax.add_patch(Wedge((0, 0), 0.62, 84, 90, fc=TEAL, ec=TEAL, alpha=0.9))
    ax.plot([0, 0], [0, 0.62], color=TEAL, lw=2.2)
    ax.plot([0], [0], "o", ms=4, color=TEAL)
    FL.record_circle((0, 0), 1)
    # x sits just outside the rim, on the bisector of the shaded minute, so it
    # touches neither the dial ring nor a numeral
    u = np.array([np.cos(np.radians(87)), np.sin(np.radians(87))])
    FL.outside_label(ax, r"$x$", u, u, base=0.16, fontsize=14, name="clock x")
    return save(fig, "sim_clock")


def rhombus():
    """Diagonals 12 and 8 on a 12 x 8 grid, so the area is 48 — not the source's 50,
    and the two diagonals are no longer equal."""
    assert 12 * 8 / 2 == 48
    fig, ax = start(figsize=(3.0, 2.2))
    for i in range(9):
        ax.plot([0, 12], [i, i], color="#9AA6A5", lw=0.55)
    for i in range(13):
        ax.plot([i, i], [0, 8], color="#9AA6A5", lw=0.55)
    ax.add_patch(Polygon(np.array([(6, 8), (12, 4), (6, 0), (0, 4)]),
                         closed=True, fill=False, ec=NAVY, lw=2.6))
    frame(ax, (-1.2, 13.2), (-1.3, 9.3))
    return save(fig, "sim_rhombus")


def trapezoid():
    """8-15-17 rather than 5-12-13, and the slant leans the other way."""
    top, bot, h = 11, 19, 15
    assert (bot - top) ** 2 + h ** 2 == 17 ** 2
    fig, ax = start(figsize=(3.3, 2.1))
    pts = np.array([(0, 0), (bot, 0), (top, h), (0, h)])
    ax.add_patch(Polygon(pts, closed=True, fill=False, ec=NAVY, lw=2.4))
    FL.record_patch_edges(pts)
    for py in (0, h - 1.5):
        ax.add_patch(Rectangle((0, py), 1.5, 1.5, fill=False, ec=NAVY, lw=1.4))
        FL.record_patch_edges([(0, py), (1.5, py), (1.5, py + 1.5), (0, py + 1.5)])
    frame(ax, (-7.5, 24.0), (-6.5, 21.0))
    FL.outside_label(ax, "19", (bot / 2, 0), (0, -1), base=0.9, name="base 19")
    FL.outside_label(ax, "11", (top / 2, h), (0, 1), base=0.9, name="top 11")
    FL.outside_label(ax, "15", (0, h / 2), (-1, 0), base=0.9, name="height 15")
    mid = ((bot + top) / 2, h / 2)                        # midpoint of the slant
    FL.outside_label(ax, r"$x$", mid, (1, 0.55), base=1.0, fontsize=14, name="slant x")
    return save(fig, "sim_trapezoid")


def polygon_ext():
    """A regular OCTAGON on a line, not a hexagon: each exterior angle is 45,
    so x + y = 90 rather than 120."""
    n = 8
    assert 2 * (360 / n) == 90
    ang = np.radians(np.arange(n) * 360 / n + 90 + 180 / n)
    pts = np.stack([np.cos(ang), np.sin(ang)], axis=1)
    pts = pts - [0, pts[:, 1].min()]                     # sit it on y = 0
    fig, ax = start(figsize=(3.2, 1.9))
    ax.add_patch(Polygon(pts, closed=True, fill=False, ec=NAVY, lw=2.0))
    FL.record_patch_edges(pts)
    FL.seg(ax, (-1.55, 0), (1.55, 0), color=INK, lw=1.6)
    lo = sorted(pts[np.isclose(pts[:, 1], 0)], key=lambda p: p[0])
    up = sorted(pts, key=lambda p: p[1])[2:]              # the next vertex up each side
    upl = min(up, key=lambda p: p[0]); upr = max(up, key=lambda p: p[0])
    # each exterior angle sits between the line going AWAY and the slant side
    frame(ax, (-1.95, 1.95), (-0.95, 2.85))
    FL.angle_label(ax, lo[0], (lo[0][0] - 1.0, 0), upl, r"$x$", fontsize=14,
                   color=NAVY, name="ext x")
    FL.angle_label(ax, lo[1], (lo[1][0] + 1.0, 0), upr, r"$y$", fontsize=14,
                   color=NAVY, name="ext y")
    return save(fig, "sim_polygon_ext")


def parallel_iso():
    """Apex 40, so the base angles are 70 and the parallel ray gives x = 70."""
    apex = 40
    base = (180 - apex) / 2
    assert base == 70
    fig, ax = start(figsize=(3.8, 2.1))
    P = np.array([0.0, 0.0]); Q = np.array([4.0, 0.0])
    t = np.radians(base)
    ap = np.array([2.0, 2.0 * np.tan(t)])
    end = np.array([Q[0] + 2.8, 0.0])
    ray = Q + np.array([np.cos(t), np.sin(t)]) * 2.4
    FL.seg(ax, P, end, color=INK, lw=1.8)
    FL.seg(ax, P, ap, color=INK, lw=1.8)
    FL.seg(ax, ap, Q, color=INK, lw=1.8)
    FL.seg(ax, Q, ray, color=INK, lw=1.8)
    for (a, b) in ((P, ap), (Q, ray)):                    # parallel arrowheads
        m = (a + b) / 2; d = (b - a) / np.linalg.norm(b - a)
        ax.annotate("", xy=m + d * 0.16, xytext=m - d * 0.16,
                    arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.4))
    for (a, b) in ((P, Q), (ap, Q)):                      # equal-length ticks
        m = (a + b) / 2; d = (b - a) / np.linalg.norm(b - a)
        nrm = np.array([-d[1], d[0]]) * 0.13
        ax.plot([m[0] - nrm[0], m[0] + nrm[0]], [m[1] - nrm[1], m[1] + nrm[1]],
                color=INK, lw=1.4)
    frame(ax, (-0.5, end[0] + 0.4), (-0.5, ap[1] + 0.6))
    FL.angle_label(ax, ap, P, Q, r"$30^{\circ}$", fontsize=13, name="apex 40")
    FL.angle_label(ax, Q, end, ray, r"$x$", fontsize=14, name="exterior x")
    return save(fig, "sim_parallel_iso")


def angles_point():
    """Three rays from one point: 140 degrees marked, one right angle, x closes
    the full turn at 130 — the source used 150 and 90 for 120."""
    assert 360 - 140 - 90 == 130
    fig, ax = start(figsize=(2.9, 2.6))
    O = np.array([0.0, 0.0])
    tips = {a: np.array([np.cos(np.radians(a)), np.sin(np.radians(a))])
            for a in (180, 40, 270)}
    for a, tip in tips.items():
        ax.annotate("", xy=tip, xytext=(0, 0),
                    arrowprops=dict(arrowstyle="-|>", color=NAVY, lw=2.4))
        FL.record_patch_edges([O, tip], close=False)
    d = 0.15                       # the square sits between the left and down rays
    ax.plot([-d, -d, 0], [0, -d, -d], color=NAVY, lw=1.5)
    FL.record_patch_edges([(-d, 0), (-d, -d), (0, -d)], close=False)
    frame(ax, (-1.55, 1.55), (-1.50, 1.40))
    FL.angle_label(ax, O, tips[180], tips[40], r"$140^{\circ}$", fontsize=13,
                   name="140 deg")
    FL.angle_label(ax, O, tips[270], tips[40], r"$x$", fontsize=15, name="x deg",
                   steps=[0.42, 0.50, 0.58, 0.68, 0.80])
    return save(fig, "sim_angles_point")


def strip():
    """Top cut 5, 2, 3 (total 10) with a slanted strip of width 2, so the ratio
    is 1 : 5 — the source's cut was 4, 3, 2 for 1 : 3."""
    a, w, c = 5, 2, 3
    assert w / (a + w + c) == 1 / 5
    fig, ax = start(figsize=(4.0, 1.7))
    H, W = 4.0, 10.0
    lean = 1.4
    ax.add_patch(Rectangle((0, 0), W, H, fill=False, ec=NAVY, lw=2.2))
    FL.record_patch_edges([(0, 0), (W, 0), (W, H), (0, H)])
    quad = np.array([(a, H), (a + w, H), (a + w - lean, 0), (a - lean, 0)])
    ax.add_patch(Polygon(quad, closed=True, fc=BLUE, ec=NAVY, lw=1.4, alpha=0.85))
    FL.record_patch_edges(quad)
    for x0, x1, lab in ((0, a, "5"), (a, a + w, "2"), (a + w, W, "3")):
        frame(ax, (-0.4, W + 0.4), (-0.4, H + 1.4))
        FL.outside_label(ax, lab, ((x0 + x1) / 2, H), (0, 1), base=0.30,
                         fontsize=13, name="strip " + lab)
    return save(fig, "sim_strip")


# ================================================================= DATA
def scatter():
    """Four groups of three. The item asks for the THIRD group: 45, 55, 50 -> 50."""
    G = {"Quarter 1": [30, 45, 40], "Quarter 2": [55, 35, 60],
         "Quarter 3": [45, 55, 50], "Quarter 4": [65, 40, 45]}
    assert sum(G["Quarter 3"]) / 3 == 50
    fig, ax = start(figsize=(4.2, 2.3))
    for i, (k, vs) in enumerate(G.items()):
        ax.plot([i - 0.26, i, i + 0.26], vs, "o", ms=8, mfc=TEAL,
                mec="#0E6E68", mew=0.9, ls="none")
        if i:
            ax.axvline(i - 0.5, color="#C9D2D1", lw=0.8)
    ax.set_xticks(range(4)); ax.set_xticklabels(list(G), fontsize=11)
    ax.set_xlim(-0.55, 3.55); ax.set_ylim(0, 78); ax.set_yticks(range(0, 71, 10))
    ax.tick_params(axis="y", labelsize=9.8)
    _clean(ax)
    return save(fig, "sim_scatter")


def line_months():
    """Rajab 5 -> Shaaban 12 is a 140 per cent increase, not the source's 150."""
    M = ["Jumada I", "Rajab", "Shaaban", "Ramadan", "Shawwal"]
    V = [3, 5, 12, 9, 7]
    assert (V[2] - V[1]) / V[1] == 1.4
    fig, ax = start(figsize=(4.2, 2.1))
    ax.plot(M, V, "-o", color=ORANGE, lw=2.0, ms=6)
    ax.set_ylim(0, 15); ax.set_yticks(range(0, 15, 3))
    ax.set_xticklabels(M, fontsize=10.4)
    ax.tick_params(axis="y", labelsize=9.8)
    _clean(ax)
    return save(fig, "sim_line_months")


def invest():
    """Same shape as the source, opposite window: the item asks about the LAST
    three years, so the fund that dipped only in the first year is the answer."""
    F = {"Fund A": [-3, 8, 6, 10], "Fund B": [9, -5, 12, 4],
         "Fund C": [14, 7, -2, 9], "Fund D": [6, 11, 5, -4]}
    Y = ["2021", "2022", "2023", "2024"]
    clean = [k for k, v in F.items() if all(x >= 0 for x in v[1:])]
    assert clean == ["Fund A"], clean
    fig, ax = start(figsize=(4.4, 2.3))
    x = np.arange(4); w = 0.2
    for i, (k, v) in enumerate(F.items()):
        ax.bar(x + (i - 1.5) * w, v, w, label=k, color=[BLUE, ORANGE, GREY, GOLD][i])
    ax.axhline(0, color=INK, lw=0.9)
    ax.set_xticks(x); ax.set_xticklabels(Y, fontsize=11)
    ax.set_ylim(-8, 18); ax.set_yticks(range(-8, 19, 4))
    ax.tick_params(axis="y", labelsize=9.8)
    ax.legend(fontsize=9.8, ncol=4, frameon=False, loc="upper center",
              bbox_to_anchor=(0.5, 1.14))
    _clean(ax)
    return save(fig, "sim_invest")


def subjects():
    """Mean of Physics (90) and Arabic (30) is 60 = Geography."""
    S = {"Physics": 90, "Arabic": 30, "Geography": 60, "English": 75, "Art": 45}
    m = (S["Physics"] + S["Arabic"]) / 2
    assert [k for k, v in S.items() if v == m] == ["Geography"]
    fig, ax = start(figsize=(3.9, 2.2))
    ax.bar(list(S), list(S.values()), color=TEAL, width=0.38)
    ax.set_ylim(0, 100); ax.set_yticks(range(0, 101, 10))
    ax.set_title("End-of-term results", fontsize=11, color=INK, pad=6)
    ax.tick_params(labelsize=9.8)
    _clean(ax)
    return save(fig, "sim_subjects")


def visitors():
    """Overseas visitors to AlUla, in thousands. With 300 thousand domestic in
    1447, the domestic share of the total is 300 / 1500 = 20 per cent."""
    Y = ["1444", "1445", "1446", "1447"]
    V = [900, 1050, 1000, 1200]
    assert 300 / (300 + V[3]) == 0.2
    fig, ax = start(figsize=(3.5, 2.1))
    ax.bar(Y, V, color=ORANGE, width=0.42)
    ax.set_ylim(0, 1400); ax.set_yticks(range(0, 1401, 200))
    ax.set_title("Overseas visitors to AlUla (thousands)", fontsize=11,
                 color=INK, pad=6)
    ax.tick_params(labelsize=10.4)
    _clean(ax)
    return save(fig, "sim_visitors")


def two_bars():
    """800 against 200, so 4 : 1 — not the source's 3 : 1."""
    assert 800 / 200 == 4
    fig, ax = start(figsize=(3.1, 2.1))
    ax.bar(["Branch one", "Branch two"], [800, 200], color=BLUE, width=0.38)
    ax.set_ylim(0, 900); ax.set_yticks(range(0, 801, 200))
    ax.tick_params(labelsize=10.4)
    _clean(ax)
    return save(fig, "sim_two_bars")


def grouped_min():
    """Buses + lorries is lowest at Gate 3 (65). Cars are a decoy column."""
    G = {"Buses": [40, 55, 30, 45], "Lorries": [50, 40, 35, 60],
         "Cars": [90, 70, 95, 80]}
    GATES = ["Gate 1", "Gate 2", "Gate 3", "Gate 4"]
    tot = [G["Buses"][i] + G["Lorries"][i] for i in range(4)]
    assert GATES[tot.index(min(tot))] == "Gate 3", tot
    fig, ax = start(figsize=(4.3, 2.2))
    x = np.arange(4); w = 0.26
    for i, (k, v) in enumerate(G.items()):
        b = ax.bar(x + (i - 1) * w, v, w, label=k, color=[BLUE, ORANGE, GREY][i])
        ax.bar_label(b, fontsize=9.1, padding=1)
    ax.set_xticks(x); ax.set_xticklabels(GATES, fontsize=11)
    ax.set_ylim(0, 118); ax.set_yticks([])
    ax.legend(fontsize=9.8, ncol=3, frameon=False, loc="upper center",
              bbox_to_anchor=(0.5, 1.16))
    for sp in ("top", "right", "left"):
        ax.spines[sp].set_visible(False)
    return save(fig, "sim_grouped_min")


def grouped_double():
    """Tea + juice is double the coffee bar on Thursday only (45 + 35 = 2 x 40)."""
    G = {"Tea": [45, 30, 50, 40], "Juice": [35, 45, 30, 50], "Coffee": [40, 50, 60, 30]}
    DAYS = ["Thursday", "Friday", "Saturday", "Sunday"]
    hit = [DAYS[i] for i in range(4)
           if G["Tea"][i] + G["Juice"][i] == 2 * G["Coffee"][i]]
    assert hit == ["Thursday"], hit
    fig, ax = start(figsize=(4.3, 2.2))
    x = np.arange(4); w = 0.26
    for i, (k, v) in enumerate(G.items()):
        b = ax.bar(x + (i - 1) * w, v, w, label=k, color=[TEAL, GOLD, GREY][i])
        ax.bar_label(b, fontsize=9.1, padding=1)
    ax.set_xticks(x); ax.set_xticklabels(DAYS, fontsize=11)
    ax.set_ylim(0, 72); ax.set_yticks([])
    ax.legend(fontsize=9.8, ncol=3, frameon=False, loc="upper center",
              bbox_to_anchor=(0.5, 1.16))
    for sp in ("top", "right", "left"):
        ax.spines[sp].set_visible(False)
    return save(fig, "sim_grouped_double")



# ==================================================== PART 6 SKILLS (new)
def pie_years():
    """Six harvests, 1080 tons in all, so 3 tons to the degree. Years 2 and 5
    together are 210 tons = 70 degrees, and year 2 is marked 40, so year 5 is 30.
    The year names sit OUTSIDE the rim: a 30 degree wedge cannot hold a label and
    the given angle needs the room inside."""
    assert 1080 / 360 == 3
    assert 210 / 3 == 70 and 70 - 40 == 30
    seg = [("1st", 95), ("2nd", 40), ("3rd", 70), ("4th", 85), ("5th", 30), ("6th", 40)]
    assert sum(a for _, a in seg) == 360
    fig, ax = start(figsize=(3.1, 3.1))
    frame(ax, (-2.05, 2.05), (-1.95, 1.95))
    FL.record_circle((0, 0), 1)
    a0 = 90.0
    mids = {}
    for name, ang in seg:
        ax.add_patch(Wedge((0, 0), 1, a0 - ang, a0, fc="#EFEFEF", ec=INK, lw=1.3))
        t = np.radians(a0)
        FL.record_patch_edges([(0, 0), (np.cos(t), np.sin(t))], close=False)
        mids[name] = np.radians(a0 - ang / 2)
        a0 -= ang
    for name, _ in seg:                       # names outside the rim
        u = np.array([np.cos(mids[name]), np.sin(mids[name])])
        FL.outside_label(ax, name + " yr", u, u, base=0.12, fontsize=9,
                         color=INK, name="year " + name)
    # THE ONE ANGLE THE QUESTION GIVES YOU — the second year's wedge. The label
    # text is taken from the data, not typed: a hand-typed angle on a drawn wedge
    # is how a figure ends up contradicting its own key.
    given = dict(seg)["2nd"]
    start_2nd = 90 - seg[0][1]
    lo = np.radians(start_2nd); hi = np.radians(start_2nd - given)
    assert given == 40
    FL.angle_label(ax, (0, 0), (np.cos(lo), np.sin(lo)), (np.cos(hi), np.sin(hi)),
                   rf"${given}^{{\circ}}$", fontsize=10, name="given angle")
    return save(fig, "sim_pie_years")


def pie_equal():
    """Ten equal parts, four shaded: 4 x 36 = 144 degrees."""
    n, shaded = 10, 4
    assert shaded * (360 // n) == 144
    fig, ax = start(figsize=(2.3, 2.3))
    frame(ax, (-1.25, 1.25), (-1.25, 1.25))
    for i in range(n):
        a0 = 90 - (360 / n) * (i + 1)
        ax.add_patch(Wedge((0, 0), 1, a0, a0 + 360 / n,
                           fc=("#C62828" if i < shaded else "#DDDDDD"),
                           ec="white", lw=1.6))
    return save(fig, "sim_pie_equal")


def pie_exam():
    """Right half completed (180), a 45 degree slice withdrew, the rest deferred.
    Used by TWO items: one converts an angle to a count, the other finds the
    missing angle. The slice names are kept short on purpose — a long word will
    not fit beside a circle this size without shoving the figure out of shape."""
    assert 360 - 180 - 45 == 135
    fig, ax = start(figsize=(2.5, 2.5))
    frame(ax, (-2.30, 2.55), (-1.85, 2.20))
    FL.record_circle((0, 0), 1)
    ax.add_patch(Circle((0, 0), 1, fill=False, ec="#1F4E5F", lw=2.4))
    for a in (90, 270, 135):
        t = np.radians(a)
        FL.seg(ax, (0, 0), (np.cos(t), np.sin(t)), color="#3FB0D8", lw=2.2)
    # The 45 degree wedge is too narrow to hold its own label, so the angle is
    # marked just outside the rim on that wedge's bisector — and it is placed
    # FIRST, so the three slice names are pushed clear of it by the guard.
    ub = np.array([np.cos(np.radians(99)), np.sin(np.radians(99))])
    FL.outside_label(ax, r"$45^{\circ}$", ub, ub, base=0.10, fontsize=9,
                     name="45 deg")
    ax.annotate("", xy=ub * 0.72, xytext=ub * 1.02,
                arrowprops=dict(arrowstyle="-", color=INK, lw=0.8))
    for lab, a in (("Passed", 0), ("Absent", 129), ("Failed", 205)):
        u = np.array([np.cos(np.radians(a)), np.sin(np.radians(a))])
        FL.outside_label(ax, lab, u, u, base=0.14, fontsize=8.5,
                         name="slice " + lab)
    return save(fig, "sim_pie_exam")


def squares_block():
    """Twelve shaded unit squares in a clean 3 x 4 block — no shared-corner
    ambiguity, so the count is not open to argument."""
    assert 12 / 0.20 == 60
    fig, ax = start(figsize=(3.0, 1.9))
    W, H = 10, 6
    frame(ax, (-0.4, W + 0.4), (-0.4, H + 0.4))
    for i in range(4):
        for j in range(3):
            ax.add_patch(Rectangle((1 + i, 1 + j), 1, 1, fc="#5B8FCB",
                                   ec="#2F4E7A", lw=1.1))
    ax.add_patch(Rectangle((0, 0), W, H, fill=False, ec=INK, lw=1.8))
    FL.record_patch_edges([(0, 0), (W, 0), (W, H), (0, H)])
    return save(fig, "sim_squares_block")


def ext_angle():
    """Angle P = 55 and the exterior angle at R = 130, so P + Q = 130 exactly."""
    assert 55 < 130 and 130 < 180
    fig, ax = start(figsize=(3.4, 1.9))
    P = np.array([0.6, 2.1]); Q = np.array([0.0, 0.0]); R = np.array([3.6, 0.0])
    end = np.array([5.0, 0.0])
    frame(ax, (-1.6, 6.4), (-1.5, 3.5))
    for a, b in ((Q, end), (Q, P), (P, R)):
        FL.seg(ax, a, b, color="#1F4E5F", lw=1.9)
    FL.angle_label(ax, P, Q, R, r"$55^{\circ}$", fontsize=11, name="55 deg")
    FL.angle_label(ax, R, P, end, r"$130^{\circ}$", fontsize=11, name="130 deg")
    FL.outside_label(ax, "P", P, (0, 1), base=0.20, fontsize=11, name="vertex P")
    FL.outside_label(ax, "Q", Q, (-1, -0.3), base=0.20, fontsize=11, name="vertex Q")
    FL.outside_label(ax, "R", R, (0, -1), base=0.20, fontsize=11, name="vertex R")
    return save(fig, "sim_ext_angle")


def circles_row():
    """Eight congruent circles along an 80 cm diameter: each has radius 5, the
    big one 40, so the areas are 25 : 1600 = 1 : 64."""
    n, D = 8, 80
    r, Rbig = D / n / 2, D / 2
    assert (r * r) / (Rbig * Rbig) == 1 / 64
    fig, ax = start(figsize=(3.0, 3.0))
    frame(ax, (-1.30, 1.30), (-1.40, 1.20))
    FL.record_circle((0, 0), 1)
    ax.add_patch(Circle((0, 0), 1, fill=False, ec=NAVY, lw=2.2))
    for i in range(n):
        cx = -1 + (2 * i + 1) / n
        ax.add_patch(Circle((cx, 0), 1 / n, fill=False, ec=TEAL, lw=1.5))
    FL.seg(ax, (-1, 0), (1, 0), color=INK, lw=0.9, ls=(0, (4, 3)))
    FL.outside_label(ax, "80 cm", (0, -1), (0, -1), base=0.10, fontsize=11,
                     name="diameter")
    return save(fig, "sim_circles_row")


def _table(name, cols, rows, figsize, missing=None, title=None, first_col=0.30):
    """Column widths are set explicitly: matplotlib will happily render a header
    wider than its column and let it collide with the neighbour."""
    fig, ax = start(figsize=figsize)
    ax.axis("off")
    rest = (1.0 - first_col) / (len(cols) - 1)
    widths = [first_col] + [rest] * (len(cols) - 1)
    t = ax.table(cellText=rows, colLabels=cols, loc="center", cellLoc="center",
                 colWidths=widths)
    t.auto_set_font_size(False); t.set_fontsize(8.0); t.scale(1, 1.5)
    for (r, c), cell in t.get_celld().items():
        cell.set_edgecolor("#9AA6A5"); cell.set_linewidth(0.7)
        if r == 0:
            cell.set_facecolor("#E8EFEF"); cell.set_text_props(weight="bold")
        elif c == 0:
            cell.set_text_props(weight="bold")
        if missing and (r, c) == missing:
            cell.set_facecolor("#FDECEA")
    if title:
        ax.set_title(title, fontsize=9, color=INK, pad=6)
    return save(fig, name)


def table_cells():
    """Row and column totals are given; one cell is blank. Filling it needs the
    ROW total, not the column total — that is the whole item."""
    # Riyadh 42, Jeddah ?, Dammam 55, Abha 24 ; row total 186
    assert 186 - 42 - 55 - 24 == 65
    cols = ["Centre", "Riyadh", "Jeddah", "Dammam", "Abha", "Total"]
    rows = [["Trainers", "42", "?", "55", "24", "186"],
            ["Classrooms", "18", "31", "22", "9", "80"],
            ["Courses", "64", "97", "70", "38", "269"],
            ["Total", "124", "193", "147", "71", "535"]]
    return _table("sim_table_cells", cols, rows, (5.6, 1.7),
                  missing=(1, 2), first_col=0.26)


def table_years():
    """Which categories at least TREBLED from 1443 to 1447. Housing 40 -> 120 and
    Transport 25 -> 75 both do; Food 60 -> 150 is only two and a half times."""
    d = {"Food": (60, 150), "Housing": (40, 120), "Transport": (25, 75),
         "Health": (30, 66)}
    trebled = sorted(k for k, (a, b) in d.items() if b >= 3 * a)
    assert trebled == ["Housing", "Transport"], trebled
    cols = ["Category", "1443", "1445", "1447"]
    rows = [["Food", "60", "95", "150"], ["Housing", "40", "70", "120"],
            ["Transport", "25", "44", "75"], ["Health", "30", "51", "66"]]
    return _table("sim_table_years", cols, rows, (3.6, 1.6), first_col=0.34,
                  title="Spending, in hundreds of SAR")


# ================================================= PART 5 SKILLS (new)
def count_squares():
    """A plain 4 x 4 grid. Squares of every size count: 16 + 9 + 4 + 1 = 30.
    Drawn without an outer frame around the grid, so there is no argument about
    whether a surrounding rectangle counts — the source figure had exactly that
    ambiguity and it changed the answer."""
    n = 4
    total = sum((n - k) ** 2 for k in range(n))
    assert total == 30, total
    fig, ax = start(figsize=(2.2, 2.2))
    frame(ax, (-0.35, n + 0.35), (-0.35, n + 0.35))
    for i in range(n + 1):
        FL.seg(ax, (0, i), (n, i), color=NAVY, lw=1.8)
        FL.seg(ax, (i, 0), (i, n), color=NAVY, lw=1.8)
    return save(fig, "sim_count_squares")


def shaded_square():
    """Side 8, cut into four quadrants. The top-right quadrant is fully shaded
    and the top-left is halved by its diagonal: 16 + 8 = 24."""
    side = 8.0
    q = (side / 2) ** 2
    assert q + q / 2 == 24
    fig, ax = start(figsize=(2.3, 2.3))
    h = side / 2
    frame(ax, (-0.6, side + 0.6), (-1.5, side + 0.6))
    ax.add_patch(Rectangle((h, h), h, h, fc=BLUE, ec=NAVY, lw=1.4))
    ax.add_patch(Polygon(np.array([(0, side), (h, side), (h, h)]),
                         closed=True, fc=BLUE, ec=NAVY, lw=1.4))
    ax.add_patch(Rectangle((0, 0), side, side, fill=False, ec=INK, lw=2.2))
    FL.record_patch_edges([(0, 0), (side, 0), (side, side), (0, side)])
    FL.seg(ax, (0, h), (side, h), color=INK, lw=1.5)
    FL.seg(ax, (h, 0), (h, side), color=INK, lw=1.5)
    FL.seg(ax, (0, side), (h, h), color=NAVY, lw=1.4)
    FL.outside_label(ax, "8 cm", (side / 2, 0), (0, -1), base=0.45, fontsize=11,
                     name="square side")
    return save(fig, "sim_shaded_square")


def clock_hands():
    """08:24. The hour hand has drifted 24 x 0.5 = 12 degrees past the 8, which
    is the whole point of the item: 252 against 144 leaves 108."""
    hour_ang = 8 * 30 + 24 * 0.5
    min_ang = 24 * 6
    assert abs(hour_ang - min_ang) == 108
    fig, ax = start(figsize=(2.3, 2.3))
    frame(ax, (-1.20, 1.20), (-1.20, 1.20))
    ax.add_patch(Circle((0, 0), 1, fill=False, ec=NAVY, lw=2.2))
    for i in range(60):
        t = np.radians(90 - 6 * i)
        r0 = 0.90 if i % 5 else 0.84
        ax.plot([r0 * np.cos(t), np.cos(t)], [r0 * np.sin(t), np.sin(t)],
                color=INK, lw=0.7 if i % 5 else 1.6)
    for h in range(1, 13):
        t = np.radians(90 - 30 * h)
        ax.annotate(str(h), (0.72 * np.cos(t), 0.72 * np.sin(t)), fontsize=8,
                    color=INK, ha="center", va="center")
    for ang, ln, lw in ((hour_ang, 0.45, 3.2), (min_ang, 0.66, 2.0)):
        t = np.radians(90 - ang)
        ax.plot([0, ln * np.cos(t)], [0, ln * np.sin(t)], color=TEAL, lw=lw)
    ax.plot([0], [0], "o", ms=4, color=TEAL)
    return save(fig, "sim_clock_hands")


# ============================== FORMULA-BOOK SKILLS (new) ==============
def inscribed():
    """Central angle 80 on arc AB, inscribed angle at C on the same arc: 40."""
    assert 80 / 2 == 40
    fig, ax = start(figsize=(2.5, 2.5))
    frame(ax, (-1.85, 1.85), (-1.85, 1.85))
    ax.add_patch(Circle((0, 0), 1, fill=False, ec=NAVY, lw=2.0))
    FL.record_circle((0, 0), 1)
    A = np.array([np.cos(np.radians(250)), np.sin(np.radians(250))])
    B = np.array([np.cos(np.radians(330)), np.sin(np.radians(330))])
    C = np.array([np.cos(np.radians(95)), np.sin(np.radians(95))])
    for p, q in ((A, (0, 0)), (B, (0, 0)), (A, C), (B, C)):
        FL.seg(ax, p, q, color=INK, lw=1.6)
    FL.angle_label(ax, (0, 0), A, B, r"$80^{\circ}$", fontsize=10, name="central 80")
    FL.angle_label(ax, C, A, B, r"$x$", fontsize=12, name="inscribed x")
    for lab, p in (("A", A), ("B", B), ("C", C)):
        FL.outside_label(ax, lab, p, p, base=0.13, fontsize=11, name="pt " + lab)
    FL.outside_label(ax, "O", (0, 0), (-1, 0.25), base=0.13, fontsize=11, name="centre")
    return save(fig, "sim_inscribed")


def semicircle():
    """A triangle on a diameter: the angle at the circumference is a right angle."""
    fig, ax = start(figsize=(2.6, 1.9))
    frame(ax, (-1.75, 1.75), (-0.95, 1.95))
    th = np.linspace(0, np.pi, 200)
    ax.plot(np.cos(th), np.sin(th), color=NAVY, lw=2.0)
    FL.record_patch_edges(np.stack([np.cos(th), np.sin(th)], 1), close=False)
    P = np.array([np.cos(np.radians(62)), np.sin(np.radians(62))])
    for a, b in (((-1, 0), (1, 0)), ((-1, 0), P), (P, (1, 0))):
        FL.seg(ax, a, b, color=INK, lw=1.7)
    d = 0.11
    u = (np.array([-1, 0]) - P); v = (np.array([1, 0]) - P)
    u = u / np.linalg.norm(u); v = v / np.linalg.norm(v)
    ax.plot(*zip(P + u * d, P + (u + v) * d, P + v * d), color=INK, lw=1.2)
    for lab, p in (("A", (-1, 0)), ("B", (1, 0)), ("C", P)):
        FL.outside_label(ax, lab, p, np.array(p) - np.array([0, 0.15]) if lab != "C"
                         else np.array([0, 1]), base=0.14, fontsize=11, name="pt " + lab)
    return save(fig, "sim_semicircle")


def tri_306090():
    """Hypotenuse 12, angles 30 and 60. The side facing 30 is half the hypotenuse."""
    assert 12 / 2 == 6
    fig, ax = start(figsize=(2.9, 2.0))
    h = 12.0
    B = np.array([0.0, 0.0]); C = np.array([h * np.sqrt(3) / 2, 0.0])
    A = np.array([h * np.sqrt(3) / 2, h / 2])
    frame(ax, (-3.6, 14.0), (-3.6, 10.2))
    for p, q in ((B, C), (C, A), (A, B)):
        FL.seg(ax, p, q, color=NAVY, lw=1.9)
    d = 0.9
    ax.plot(*zip(C + [-d, 0], C + [-d, d], C + [0, d]), color=NAVY, lw=1.2)
    FL.angle_label(ax, B, C, A, r"$30^{\circ}$", fontsize=11, name="30 deg")
    FL.outside_label(ax, "12", (B + A) / 2, (-0.6, 1), base=0.7, fontsize=12,
                     name="hyp 12")
    FL.outside_label(ax, r"$x$", (C + A) / 2, (1, 0), base=0.7, fontsize=13,
                     name="side x")
    return save(fig, "sim_306090")


def tri_4545():
    """Both legs 7, so the hypotenuse is 7 root 2."""
    fig, ax = start(figsize=(2.4, 2.2))
    L = 7.0
    B = np.array([0.0, 0.0]); C = np.array([L, 0.0]); A = np.array([0.0, L])
    frame(ax, (-3.4, 10.4), (-3.4, 10.4))
    for p, q in ((B, C), (C, A), (A, B)):
        FL.seg(ax, p, q, color=NAVY, lw=1.9)
    d = 0.7
    ax.plot(*zip(B + [d, 0], B + [d, d], B + [0, d]), color=NAVY, lw=1.2)
    FL.outside_label(ax, "7", (B + C) / 2, (0, -1), base=1.0, fontsize=12, name="leg a")
    FL.outside_label(ax, "7", (B + A) / 2, (-1, 0), base=1.0, fontsize=12, name="leg b")
    FL.outside_label(ax, r"$x$", (A + C) / 2, (1, 1), base=1.0, fontsize=13,
                     name="hyp x")
    return save(fig, "sim_4545")


def midseg():
    """MN joins two midpoints, so it is parallel to BC and half of it."""
    fig, ax = start(figsize=(2.9, 1.9))
    A = np.array([2.4, 4.0]); B = np.array([0.0, 0.0]); C = np.array([7.0, 0.0])
    M = (A + B) / 2; N = (A + C) / 2
    frame(ax, (-2.2, 9.2), (-2.4, 6.2))
    for p, q in ((A, B), (A, C), (B, C), (M, N)):
        FL.seg(ax, p, q, color=NAVY, lw=1.8)
    for lab, p, d in (("A", A, (0, 1)), ("B", B, (-1, -0.6)), ("C", C, (1, -0.6)),
                      ("M", M, (-1, 0)), ("N", N, (1, 0))):
        FL.outside_label(ax, lab, p, d, base=0.30, fontsize=11, name="pt " + lab)
    FL.outside_label(ax, "18 cm", (B + C) / 2, (0, -1), base=0.45, fontsize=11,
                     name="base BC")
    return save(fig, "sim_midseg")


def thales():
    """DE parallel to BC cuts the two sides in the same ratio."""
    fig, ax = start(figsize=(2.7, 2.1))
    A = np.array([2.2, 5.0]); B = np.array([0.0, 0.0]); C = np.array([6.4, 0.0])
    D = A + (B - A) * 0.4; E = A + (C - A) * 0.4
    frame(ax, (-2.4, 8.8), (-2.2, 7.2))
    for p, q in ((A, B), (A, C), (B, C), (D, E)):
        FL.seg(ax, p, q, color=NAVY, lw=1.8)
    for lab, p, d in (("A", A, (0, 1)), ("B", B, (-1, -0.6)), ("C", C, (1, -0.6)),
                      ("D", D, (-1, 0)), ("E", E, (1, 0.2))):
        FL.outside_label(ax, lab, p, d, base=0.30, fontsize=11, name="pt " + lab)
    return save(fig, "sim_thales")


def sector():
    """A 120 degree sector — one third of the circle."""
    assert 120 / 360 == 1 / 3
    fig, ax = start(figsize=(2.2, 2.2))
    frame(ax, (-1.75, 1.75), (-1.75, 1.75))
    ax.add_patch(Wedge((0, 0), 1, 90, 210, fc=TEAL, ec=NAVY, lw=1.6, alpha=0.85))
    ax.add_patch(Circle((0, 0), 1, fill=False, ec=NAVY, lw=2.0))
    FL.record_circle((0, 0), 1)
    for a in (90, 210):
        t = np.radians(a)
        FL.record_patch_edges([(0, 0), (np.cos(t), np.sin(t))], close=False)
    FL.angle_label(ax, (0, 0), (0, 1),
                   (np.cos(np.radians(210)), np.sin(np.radians(210))),
                   r"$120^{\circ}$", fontsize=10, name="120 deg")
    return save(fig, "sim_sector")


def hexagon_reg():
    """A regular hexagon with its LONG diagonal drawn, which is twice the side."""
    fig, ax = start(figsize=(2.4, 2.2))
    ang = np.radians(np.arange(6) * 60)
    P = np.stack([np.cos(ang), np.sin(ang)], 1)
    frame(ax, (-1.95, 1.95), (-1.75, 1.75))
    ax.add_patch(Polygon(P, closed=True, fill=False, ec=NAVY, lw=2.0))
    FL.record_patch_edges(P)
    # only the LONG diagonal is drawn; a second diagonal in the picture makes it
    # ambiguous which one the label belongs to, and the item turns on that
    FL.seg(ax, P[0], P[3], color=TEAL, lw=1.8)             # long: 2 x side
    top = (P[1] + P[2]) / 2                                # midpoint of the top edge
    FL.outside_label(ax, "6 cm", top, (0, 1), base=0.16, fontsize=10,
                     name="hex side")
    FL.outside_label(ax, r"$d$", (P[0] + P[3]) / 2, (0, -1), base=0.16, fontsize=12,
                     color="#0E6E68", name="long diagonal")
    return save(fig, "sim_hexagon_reg")


def trapezium():
    """Parallel sides 9 and 15, height 6."""
    assert (9 + 15) / 2 * 6 == 72
    fig, ax = start(figsize=(2.9, 1.9))
    pts = np.array([(0, 0), (15, 0), (12, 6), (3, 6)])
    frame(ax, (-4.5, 19.5), (-4.5, 11.0))
    ax.add_patch(Polygon(pts, closed=True, fill=False, ec=NAVY, lw=2.0))
    FL.record_patch_edges(pts)
    FL.seg(ax, (3, 0), (3, 6), color=INK, lw=1.0, ls=(0, (3, 2)))
    FL.outside_label(ax, "15", (7.5, 0), (0, -1), base=0.7, fontsize=11, name="base b")
    FL.outside_label(ax, "9", (7.5, 6), (0, 1), base=0.7, fontsize=11, name="base a")
    FL.outside_label(ax, "6", (3, 3), (-1, 0), base=0.7, fontsize=11, name="height")
    return save(fig, "sim_trapezium")


def mid_square():
    """Joining the midpoints of a square gives a square of HALF the area."""
    fig, ax = start(figsize=(2.2, 2.2))
    s = 8.0
    frame(ax, (-2.6, 10.6), (-3.0, 10.6))
    inner = np.array([(s / 2, 0), (s, s / 2), (s / 2, s), (0, s / 2)])
    ax.add_patch(Polygon(inner, closed=True, fc=TEAL, ec=NAVY, lw=1.6, alpha=0.85))
    FL.record_patch_edges(inner)
    ax.add_patch(Rectangle((0, 0), s, s, fill=False, ec=INK, lw=2.0))
    FL.record_patch_edges([(0, 0), (s, 0), (s, s), (0, s)])
    FL.outside_label(ax, "8 cm", (s / 2, 0), (0, -1), base=0.55, fontsize=11,
                     name="outer side")
    return save(fig, "sim_mid_square")



# ==================================================== PART F — added figures
def bisector():
    """AD bisects angle A. AB=9, AC=15, BD=6 so DC=10 by the bisector ratio."""
    assert 6 * 15 / 9 == 10
    fig, ax = start(figsize=(2.7, 2.0))
    B, C, A, D = (0, 0), (16, 0), (4.6, 9.0), (6, 0)
    frame(ax, (-4.5, 21.0), (-4.6, 13.6))
    FL.polyline(ax, [B, C, A], close=True, color=NAVY, lw=2.0)
    FL.seg(ax, A, D, color=RED, lw=1.5)
    FL.angle_label(ax, np.array(A, float), np.array(B, float), np.array(D, float),
                   "", name="bis1")
    FL.outside_label(ax, "A", A, (0, 1), base=0.9, fontsize=12, name="A")
    FL.outside_label(ax, "B", B, (-1, -0.6), base=0.9, fontsize=12, name="B")
    FL.outside_label(ax, "C", C, (1, -0.6), base=0.9, fontsize=12, name="C")
    FL.outside_label(ax, "D", D, (0, -1), base=0.9, fontsize=12, name="D")
    FL.outside_label(ax, "9", (2.3, 4.5), (-1, 0.3), base=0.8, fontsize=11, name="AB")
    FL.outside_label(ax, "15", (10.3, 4.5), (1, 0.3), base=0.8, fontsize=11, name="AC")
    FL.outside_label(ax, "6", (3, 0), (0, -1), base=1.7, fontsize=11, name="BD")
    FL.outside_label(ax, "?", (11, 0), (0, -1), base=1.7, fontsize=11, name="DC")
    return save(fig, "sim_bisector")


def cyclic():
    """Opposite angles of a cyclic quadrilateral add to 180; y = 180 - 78 = 102."""
    assert 180 - 78 == 102
    fig, ax = start(figsize=(2.6, 2.6))
    R0 = 3.0
    frame(ax, (-4.5, 4.5), (-4.5, 4.5))
    ax.add_patch(Circle((0, 0), R0, fill=False, ec=GREY, lw=1.2))
    FL.record_circle((0, 0), R0)
    th = np.radians([133, 38, -52, 208])
    P = np.array([[R0 * np.cos(t), R0 * np.sin(t)] for t in th])   # A, B, C, D
    ax.add_patch(Polygon(P, closed=True, fill=False, ec=NAVY, lw=2.0))
    FL.record_patch_edges(P)
    A, Bv, Cv, Dv = P
    def near(V, X, t=1.5):
        V = np.asarray(V, float); X = np.asarray(X, float)
        return V + (X - V) / np.linalg.norm(X - V) * t
    FL.angle_label(ax, A, near(A, Dv), near(A, Bv), r"$78^{\circ}$", fontsize=11, name="angA")
    FL.angle_label(ax, Bv, near(Bv, A), near(Bv, Cv), r"$68^{\circ}$", fontsize=11, name="angB")
    FL.angle_label(ax, Cv, near(Cv, Bv), near(Cv, Dv), r"$y$", fontsize=13,
                   color=INK, name="angY")
    return save(fig, "sim_cyclic")


def parallel_pair():
    """Co-interior angles: (3x+10) + (5x+10) = 180 gives x = 20."""
    assert 3 * 20 + 10 + 5 * 20 + 10 == 180
    fig, ax = start(figsize=(3.0, 1.9))
    frame(ax, (-1.6, 9.4), (-1.7, 4.9), equal=False)
    for y in (0, 3):
        FL.seg(ax, (-1.0, y), (8.6, y), color=NAVY, lw=2.0)
    Q = np.array([2.0, 0.0]); P = np.array([3.092, 3.0])
    d = (P - Q) / np.linalg.norm(P - Q)
    FL.seg(ax, Q - d * 1.5, P + d * 1.6, color=INK, lw=1.6)
    # Both labels sit INSIDE the strip on the right of the transversal, which is
    # the wedge each angle actually occupies; the guard still refuses a collision.
    from matplotlib.patches import Arc
    for V, a0, a1 in ((Q, 0, 70), (P, -70, 0)):
        ax.add_patch(Arc(V, 1.5, 1.1, angle=0, theta1=a0, theta2=a1,
                         color=RED, lw=1.2))
    FL.place(ax, r"$(3x+10)^{\circ}$", (5.05, 0.80), fontsize=10, color=INK,
             name="lower angle")
    FL.place(ax, r"$(5x+10)^{\circ}$", (5.75, 2.22), fontsize=10, color=INK,
             name="upper angle")
    return save(fig, "sim_parallel_pair")


def same_base():
    """Same base, apexes on a line parallel to it — the areas are EQUAL."""
    fig, ax = start(figsize=(3.1, 1.9))
    Pp, Qq = (0.0, 0.0), (6.0, 0.0)
    R, S = (1.5, 4.0), (8.2, 4.0)
    frame(ax, (-2.4, 11.4), (-2.2, 6.6))
    FL.seg(ax, (-1.6, 4.0), (10.4, 4.0), color=GREY, lw=1.1, ls=(0, (4, 3)))
    FL.polyline(ax, [Pp, Qq, R], close=True, color=NAVY, lw=1.9)
    FL.polyline(ax, [Pp, Qq, S], close=True, color=TEAL, lw=1.9)
    FL.outside_label(ax, "P", Pp, (-1, -0.5), base=0.55, fontsize=11, name="P")
    FL.outside_label(ax, "Q", Qq, (0.1, -1), base=0.85, fontsize=11, name="Q")
    FL.outside_label(ax, "R", R, (-0.4, 1), base=0.55, fontsize=11, name="R")
    FL.outside_label(ax, "S", S, (0.4, 1), base=0.55, fontsize=11, name="S")
    return save(fig, "sim_circle_in_square_placeholder") if False else \
        save(fig, "sim_same_base")


def circle_square():
    """Side 14, inscribed circle r = 7. Shaded corners = 196 - 154 = 42."""
    assert 14 * 14 - 22 * 49 // 7 == 42
    fig, ax = start(figsize=(2.0, 2.0))
    s = 14.0
    frame(ax, (-3.4, 17.4), (-4.2, 16.6))
    ax.add_patch(Rectangle((0, 0), s, s, fc=TEAL, ec=NAVY, lw=1.9, alpha=0.85))
    FL.record_patch_edges([(0, 0), (s, 0), (s, s), (0, s)])
    ax.add_patch(Circle((s / 2, s / 2), s / 2, fc="white", ec=NAVY, lw=1.6))
    FL.record_circle((s / 2, s / 2), s / 2)
    FL.outside_label(ax, "14 cm", (s / 2, 0), (0, -1), base=0.9, fontsize=11,
                     name="side")
    return save(fig, "sim_circle_square")


def two_circles():
    """12 by 6 rectangle, two touching circles of radius 3. Shaded 72 - 56.52."""
    assert abs((12 * 6 - 2 * 3.14 * 9) - 15.48) < 1e-9
    fig, ax = start(figsize=(3.2, 1.9))
    L, H, r = 12.0, 6.0, 3.0
    frame(ax, (-6.2, 18.0), (-3.4, 9.4))
    ax.add_patch(Rectangle((0, 0), L, H, fc=TEAL, ec=NAVY, lw=1.9, alpha=0.85))
    FL.record_patch_edges([(0, 0), (L, 0), (L, H), (0, H)])
    for cx in (r, 3 * r):
        ax.add_patch(Circle((cx, H / 2), r, fc="white", ec=NAVY, lw=1.6))
        FL.record_circle((cx, H / 2), r)
    FL.outside_label(ax, "12 cm", (L / 2, 0), (0, -1), base=0.5, fontsize=11,
                     name="length")
    FL.outside_label(ax, "6 cm", (0, H / 2), (-1, 0), base=0.5, fontsize=11,
                     name="height")
    return save(fig, "sim_two_circles")


def grid_rects():
    """4 vertical lines and 3 horizontal ones: C(4,2) x C(3,2) = 6 x 3 = 18."""
    from math import comb
    assert comb(4, 2) * comb(3, 2) == 18
    fig, ax = start(figsize=(2.3, 1.7))
    frame(ax, (-0.55, 3.55), (-0.55, 2.55))
    for x in range(4):
        FL.seg(ax, (x, 0), (x, 2), color=NAVY, lw=1.7)
    for y in range(3):
        FL.seg(ax, (0, y), (3, y), color=NAVY, lw=1.7)
    return save(fig, "sim_grid_rects")



# ================================== PART G — data strand, the blueprint gap
def pie_missing():
    """Three sectors given as percentages, the fourth blank. 100 - 60 = 40%,
    and 40% of 360 is 144 degrees. The item is a two-step: percent, then angle."""
    given = {"Transport": 20, "Food": 15, "Housing": 25}
    rest = 100 - sum(given.values())
    assert rest == 40 and rest * 360 // 100 == 144
    seg = [("Transport", 20), ("Food", 15), ("Housing", 25), ("?", rest)]
    fig, ax = start(figsize=(2.9, 2.9))
    frame(ax, (-2.55, 2.55), (-2.35, 2.35))
    FL.record_circle((0, 0), 1)
    a0, mids = 90.0, {}
    for name, pc in seg:
        ang = pc * 3.6
        ax.add_patch(Wedge((0, 0), 1, a0 - ang, a0,
                           fc="#FDECEA" if name == "?" else "#EFEFEF",
                           ec=INK, lw=1.3))
        t = np.radians(a0)
        FL.record_patch_edges([(0, 0), (np.cos(t), np.sin(t))], close=False)
        mids[name] = np.radians(a0 - ang / 2)
        a0 -= ang
    for name, pc in seg:
        u = np.array([np.cos(mids[name]), np.sin(mids[name])])
        txt = "?" if name == "?" else f"{name}\n{pc}%"
        FL.outside_label(ax, txt, u, u, base=0.13, fontsize=11,
                         color=INK, name="sector " + name)
    return save(fig, "sim_pie_missing")


def hist_grouped_freq():
    """Five classes, 50 values. The mean must be estimated from class MIDPOINTS
    (5, 15, 25, 35, 45), not from the upper class boundaries — using the
    boundaries instead inflates the estimate from 24.6 to 29.6."""
    f = [5, 12, 18, 10, 5]
    lab = ["0–10", "10–20", "20–30", "30–40", "40–50"]
    mids = [5, 15, 25, 35, 45]
    mean = sum(m * x for m, x in zip(mids, f)) / sum(f)
    assert abs(mean - 24.6) < 1e-9, mean
    fig, ax = start(figsize=(3.1, 2.0))
    ax.bar(lab, f, color=TEAL, width=0.98, edgecolor="white", lw=1.2)
    ax.set_ylim(0, 21); ax.set_yticks(range(0, 21, 5))
    ax.tick_params(labelsize=8)
    _clean(ax)
    return save(fig, "sim_hist_grouped_freq")


def bar_revenue_quarters():
    """Units sold per quarter, in thousands. At 25 SAR a unit, only Q4's
    revenue clears 1,500,000 SAR — Q2 comes close (1,375,000) and is the
    trap the distractors are built around."""
    u = [40, 55, 35, 70]
    price = 25
    revs = [x * 1000 * price for x in u]
    assert revs[3] > 1_500_000 and all(r <= 1_500_000 for r in revs[:3]), revs
    fig, ax = start(figsize=(3.0, 2.0))
    ax.bar(["Q1", "Q2", "Q3", "Q4"], u, color=BLUE, width=0.5)
    ax.set_ylim(0, 80); ax.set_yticks(range(0, 71, 20))
    ax.tick_params(labelsize=8)
    _clean(ax)
    return save(fig, "sim_bar_revenue_quarters")


def line_temp_rise():
    """Temperature readings every two hours. The steepest RISE is between
    hours 2 and 4 (a jump of 7 degrees) even though the highest single
    reading comes later, at hour 8."""
    hrs = [0, 2, 4, 6, 8]
    temp = [18, 22, 29, 31, 33]
    diffs = [temp[i + 1] - temp[i] for i in range(4)]
    assert diffs.index(max(diffs)) == 1, diffs
    fig, ax = start(figsize=(3.0, 2.0))
    ax.plot(hrs, temp, marker="o", ms=4.5, color=ORANGE, lw=1.9)
    ax.set_xticks(hrs)
    ax.set_ylim(14, 36); ax.set_yticks(range(15, 36, 5))
    ax.tick_params(labelsize=9.6)
    _clean(ax)
    return save(fig, "sim_line_temp_rise")


def line_cyclist_distance():
    """A single series, hours 0-4, distance 2-22 km. Reused by three level-1/2
    items (read a value, total increase, average rate) — the start point is
    2, not 0, so 'just read the final value' is a real, distinct trap from
    'subtract the start from the end'."""
    hrs = [0, 1, 2, 3, 4]
    dist = [2, 7, 14, 17, 22]
    assert dist[2] == 14 and dist[4] - dist[0] == 20
    fig, ax = start(figsize=(3.0, 2.0))
    ax.plot(hrs, dist, marker="o", ms=4.5, color=BLUE, lw=1.9)
    ax.set_xticks(hrs)
    ax.set_ylim(0, 25); ax.set_yticks(range(0, 26, 5))
    ax.tick_params(labelsize=9.6)
    _clean(ax)
    return save(fig, "sim_line_cyclist_distance")


def hist_test_scores():
    """40 students, five 10-point classes. Reused by three level-1/2 items
    (modal class, total count, count above 80) — the modal class (70-80) is
    NOT the top class, so reading the chart by shape rather than by height
    is the trap running through all three."""
    f = [4, 9, 15, 10, 2]
    lab = ["50–60", "60–70", "70–80", "80–90", "90–100"]
    assert sum(f) == 40 and lab[f.index(max(f))] == "70–80"
    assert f[3] + f[4] == 12
    fig, ax = start(figsize=(3.1, 2.0))
    ax.bar(lab, f, color=TEAL, width=0.98, edgecolor="white", lw=1.2)
    ax.set_ylim(0, 17); ax.set_yticks(range(0, 16, 5))
    ax.tick_params(labelsize=8)
    _clean(ax)
    return save(fig, "sim_hist_test_scores")


def line_gap():
    """Two series over five months. The largest GAP is in April, which is not the
    month where either series peaks — that is the whole item."""
    M = ["Jan", "Feb", "Mar", "Apr", "May"]
    A = [30, 42, 38, 55, 50]
    B = [22, 26, 34, 31, 44]
    gaps = [a - b for a, b in zip(A, B)]
    assert gaps.index(max(gaps)) == 3, gaps
    fig, ax = start(figsize=(3.2, 2.1))
    ax.plot(M, A, marker="o", ms=4, color=BLUE, lw=1.8, label="Branch A")
    ax.plot(M, B, marker="s", ms=4, color=ORANGE, lw=1.8, label="Branch B")
    ax.set_ylim(0, 66); ax.set_yticks(range(0, 61, 20))
    ax.tick_params(labelsize=10.4)
    ax.legend(fontsize=9.8, frameon=False, loc="upper left")
    _clean(ax)
    return save(fig, "sim_line_gap")


def bar_pct_change():
    """Q3 to Q4: 45 to 63 is a rise of 18, which is 40% of 45. Reading the rise
    of 18 as '18%' is the trap the distractors are built around."""
    v = [40, 50, 45, 63]
    assert (v[3] - v[2]) * 100 // v[2] == 40
    fig, ax = start(figsize=(3.0, 2.0))
    ax.bar(["Q1", "Q2", "Q3", "Q4"], v, color=BLUE, width=0.5)
    ax.set_ylim(0, 72); ax.set_yticks(range(0, 71, 20))
    ax.tick_params(labelsize=8)
    _clean(ax)
    return save(fig, "sim_bar_pct_change")


def hist_class():
    """48 values. The middle pair is the 24th and 25th, and the running total
    reaches 24 inside 20-30. The TALLEST bar is 30-40, which is the trap."""
    f = [9, 12, 8, 14, 5]
    lab = ["0–10", "10–20", "20–30", "30–40", "40–50"]
    run, k = 0, None
    for i, x in enumerate(f):
        run += x
        if k is None and run >= sum(f) / 2:
            k = i
    assert k == 2 and lab[f.index(max(f))] == "30–40"
    fig, ax = start(figsize=(3.1, 2.0))
    ax.bar(lab, f, color=TEAL, width=0.98, edgecolor="white", lw=1.2)
    ax.set_ylim(0, 17); ax.set_yticks(range(0, 16, 5))
    ax.tick_params(labelsize=8)
    _clean(ax)
    return save(fig, "sim_hist_class")


def table_growth():
    """Dammam has the largest PERCENTAGE rise (35%) on the smallest numbers;
    Makkah has the largest rise in absolute terms (+54) and is the trap."""
    d = {"Jeddah": (240, 288), "Makkah": (180, 234),
         "Madinah": (120, 132), "Dammam": (60, 81)}
    pct = {k: (b - a) * 100 / a for k, (a, b) in d.items()}
    absr = {k: b - a for k, (a, b) in d.items()}
    assert max(pct, key=pct.get) == "Dammam"
    assert max(absr, key=absr.get) == "Makkah"
    cols = ["Campus", "1446", "1447"]
    rows = [[k, str(a), str(b)] for k, (a, b) in d.items()]
    return _table("sim_table_growth", cols, rows, (2.9, 1.6), first_col=0.38,
                  title="Applicants by campus")


def stacked_schools():
    """Girls are more than half at School B only. School C is EXACTLY half, and
    a student who reads 'at least half' takes C as well."""
    d = {"School A": (120, 80), "School B": (90, 110), "School C": (150, 150)}
    more = [k for k, (b, g) in d.items() if g > b + g - g and g * 2 > b + g]
    assert more == ["School B"], more
    fig, ax = start(figsize=(3.0, 2.1))
    names = list(d)
    boys = [d[k][0] for k in names]; girls = [d[k][1] for k in names]
    ax.bar(names, boys, color=BLUE, width=0.5, label="Boys")
    ax.bar(names, girls, bottom=boys, color=GOLD, width=0.5, label="Girls")
    ax.set_ylim(0, 360); ax.set_yticks(range(0, 301, 100))
    ax.tick_params(labelsize=10.4)
    ax.legend(fontsize=9.8, frameon=False, ncol=2, loc="upper left")
    _clean(ax)
    return save(fig, "sim_stacked_schools")


def pictogram():
    """Each symbol is 8 books. Week 2 has 7 symbols and week 3 has 4, so the
    difference is 3 SYMBOLS but 24 books. Answering 3 is the trap."""
    n = {"Week 1": 5, "Week 2": 7, "Week 3": 4, "Week 4": 6}
    assert (n["Week 2"] - n["Week 3"]) * 8 == 24
    fig, ax = start(figsize=(3.3, 1.9))
    rows = list(n)
    frame(ax, (-4.6, 10.6), (-2.1, 4.7), equal=False)
    for r, k in enumerate(rows):
        y = len(rows) - 1 - r
        for i in range(n[k]):
            ax.add_patch(Rectangle((i * 0.92, y + 0.18), 0.62, 0.5,
                                   fc=TEAL, ec=NAVY, lw=0.8))
        FL.outside_label(ax, k, (0, y + 0.43), (-1, 0), base=0.15,
                         fontsize=8.5, name="row " + k)
    ax.add_patch(Rectangle((0.0, -1.03), 0.5, 0.38, fc=TEAL, ec=NAVY, lw=0.8))
    FL.place(ax, "= 8 books", (0.8, -0.85), fontsize=9.5, color=INK,
             ha="left", name="key value")
    return save(fig, "sim_pictogram")



# ============================ PART H — skills mined from Elsawy Part 1
def stairs():
    """A rectilinear outline: 7 wide, 5 tall. Every horizontal piece slides out
    to the full width and every vertical piece to the full height, so the
    perimeter is the enclosing rectangle's, 2(7 + 5) = 24. The steps are drawn
    unequal on purpose — equal steps let a student guess the trick from symmetry
    instead of understanding it."""
    pts = [(0, 0), (7, 0), (7, 2), (4, 2), (4, 3.5), (2, 3.5), (2, 5), (0, 5)]
    hor = sum(abs(pts[i][0] - pts[i-1][0]) for i in range(len(pts)))
    ver = sum(abs(pts[i][1] - pts[i-1][1]) for i in range(len(pts)))
    assert hor == 14 and ver == 10 and hor + ver == 24, (hor, ver)
    fig, ax = start(figsize=(2.3, 2.0))
    frame(ax, (-4.6, 9.4), (-2.4, 7.0))
    ax.add_patch(Polygon(pts, closed=True, fill=False, ec=NAVY, lw=2.2))
    FL.record_patch_edges(pts)
    FL.outside_label(ax, "7 cm", (3.5, 0), (0, -1), base=0.55, fontsize=11, name="width")
    FL.outside_label(ax, "5 cm", (0, 2.5), (-1, 0), base=0.55, fontsize=11, name="height")
    return save(fig, "h_stairs")


def tri_in_circle():
    """Right triangle inside a circle with the hypotenuse as the diameter.
    Legs 6 and 8, so the hypotenuse is 10 and the radius is 5. The right angle
    is marked, because without it the item is a different question."""
    r = 5.0
    V = np.array([-1.4, 4.8])          # 6 from (-5,0) and 8 from (5,0)
    A = np.array([-r, 0.0]); B = np.array([r, 0.0])
    assert abs(np.linalg.norm(V - A) - 6) < 1e-9
    assert abs(np.linalg.norm(V - B) - 8) < 1e-9
    fig, ax = start(figsize=(2.5, 2.0))
    frame(ax, (-7.6, 7.6), (-6.6, 7.8))
    ax.add_patch(Circle((0, 0), r, fill=False, ec=GREY, lw=1.4))
    FL.record_circle((0, 0), r)
    FL.polyline(ax, [tuple(A), tuple(B), tuple(V)], close=True, color=NAVY, lw=2.0)
    # right-angle square at V
    u = (A - V) / np.linalg.norm(A - V); w = (B - V) / np.linalg.norm(B - V)
    k = 0.75
    FL.polyline(ax, [tuple(V + u * k), tuple(V + (u + w) * k), tuple(V + w * k)],
                color=INK, lw=1.1)
    FL.outside_label(ax, "6", tuple((V + A) / 2), (-1, 0.35), base=0.55,
                     fontsize=11, name="leg 6")
    FL.outside_label(ax, "8", tuple((V + B) / 2), (1, 0.35), base=0.55,
                     fontsize=11, name="leg 8")
    return save(fig, "h_tri_circle")



# ============ PART I — diagrams rebuilt from scratch for the expanded booklet
def circles_grid():
    """Six equal circles packed 3 by 2 in a 6 by 4 rectangle. The diameter is
    forced twice over — 6/3 and 4/2 both give 2 — and drawing it that way is the
    point: the booklet's original figure was lost in the PDF, and a student who
    only reads '3 by 2 grid' does not see that both directions must agree."""
    W, H, nx, ny = 6.0, 4.0, 3, 2
    d = W / nx
    assert d == H / ny == 2.0, d
    fig, ax = start(figsize=(2.7, 2.0))
    frame(ax, (-1.5, 7.5), (-1.6, 5.4))
    ax.add_patch(Rectangle((0, 0), W, H, fill=False, ec=NAVY, lw=2.0))
    FL.record_patch_edges([(0, 0), (W, 0), (W, H), (0, H)])
    for i in range(nx):
        for j in range(ny):
            c = (d / 2 + i * d, d / 2 + j * d)
            ax.add_patch(Circle(c, d / 2, fill=False, ec=TEAL, lw=1.6))
            FL.record_circle(c, d / 2)
    FL.outside_label(ax, "6", (W / 2, 0), (0, -1), base=0.4, fontsize=11, name="width")
    FL.outside_label(ax, "4", (0, H / 2), (-1, 0), base=0.4, fontsize=11, name="height")
    return save(fig, "i_circles_grid")


def two_curves():
    """Two weight curves that cross exactly four times. The count is what the
    item asks for, so the crossings are placed far apart and away from the ends —
    a curve that grazes near a boundary makes the answer arguable."""
    x = np.linspace(0, 12, 800)
    f = 62 + 5.0 * np.sin(x - 0.929)
    g = 62 + 4.5 * np.sin(x - 0.929 + 2.2)
    sign = np.sign(f - g)
    cross_x = x[:-1][sign[1:] * sign[:-1] < 0]
    assert len(cross_x) == 4, len(cross_x)
    # no crossing may sit within a month of either end, or the count is arguable
    assert cross_x.min() > 1.0 and cross_x.max() < 11.0, cross_x
    fig, ax = start(figsize=(3.0, 2.0))
    ax.plot(x, f, color=BLUE, lw=1.9, label="Yasser")
    ax.plot(x, g, color=ORANGE, lw=1.9, label="Saad")
    ax.set_xlim(0, 12); ax.set_ylim(54, 73)
    ax.set_xlabel("month", fontsize=10.4); ax.set_ylabel("weight (kg)", fontsize=10.4)
    ax.tick_params(labelsize=10.4)
    ax.legend(fontsize=9.8, frameon=False, loc="upper right")
    _clean(ax)
    return save(fig, "i_two_curves")


def lshape_area():
    """An L: a 5 by 4 rectangle with a 2 by 2 corner removed, so the area is
    20 - 4 = 16. Only the outer sides are labelled; the two short edges of the
    notch must be inferred, which is the whole skill."""
    pts = [(0, 0), (5, 0), (5, 2), (3, 2), (3, 4), (0, 4)]
    assert 5 * 4 - 2 * 2 == 16
    fig, ax = start(figsize=(2.4, 2.0))
    frame(ax, (-2.6, 7.6), (-2.2, 6.0))
    ax.add_patch(Polygon(pts, closed=True, fc=TEAL, ec=NAVY, lw=2.0, alpha=0.8))
    FL.record_patch_edges(pts)
    FL.outside_label(ax, "5", (2.5, 0), (0, -1), base=0.45, fontsize=11, name="bottom")
    FL.outside_label(ax, "4", (0, 2), (-1, 0), base=0.45, fontsize=11, name="left")
    FL.outside_label(ax, "3", (1.5, 4), (0, 1), base=0.45, fontsize=11, name="top")
    FL.outside_label(ax, "2", (5, 1), (1, 0), base=0.45, fontsize=11, name="right")
    return save(fig, "i_lshape")



# ================================================= PART K SKILLS (new)
def square_corner_cut():
    """A square of side 8 with one corner cut off by a straight line. What is
    labelled is what REMAINS of the top and right sides (4 and 5); the triangle's
    legs are the leftovers, 8 - 4 = 4 and 8 - 5 = 3, which is the whole skill.
    Shaded area = 64 - (1/2)(4)(3) = 58."""
    S, top_keep, right_keep = 8, 4, 5
    leg_top, leg_right = S - top_keep, S - right_keep
    assert S * S - leg_top * leg_right / 2 == 58
    pts = [(0, 0), (S, 0), (S, right_keep), (top_keep, S), (0, S)]
    fig, ax = start(figsize=(2.6, 2.5))
    frame(ax, (-3.0, 11.6), (-2.8, 11.2))
    ax.add_patch(Polygon(pts, closed=True, fc=NAVY, ec=NAVY, lw=1.6, alpha=0.9))
    ax.plot([top_keep, S, S], [S, S, right_keep], color=INK, lw=1.4,
            ls=(0, (3, 3)))
    FL.record_patch_edges(pts)
    FL.place(ax, "4", (top_keep / 2, S + 1.0), fontsize=11, name="top kept")
    FL.place(ax, "5", (S + 1.2, right_keep / 2), fontsize=11, name="right kept")
    FL.place(ax, "8", (S / 2, -1.4), fontsize=11, name="bottom")
    FL.place(ax, "8", (-1.4, S / 2), fontsize=11, name="left")
    return save(fig, "k_corner_cut")


def rays_expression():
    """THREE rays from one point, so the three marked angles close the full turn:
    2x + 2y + a = 360, and the item asks for 180 - x - y, which is a/2. Nothing
    numeric appears — the picture must not hint at a size."""
    fig, ax = start(figsize=(3.2, 2.7))
    O = np.array([0.0, 0.0])
    angs = {"right": 10, "upleft": 105, "down": 240}
    tips = {k: np.array([np.cos(np.radians(a)), np.sin(np.radians(a))])
            for k, a in angs.items()}
    for tip in tips.values():
        ax.annotate("", xy=tip, xytext=(0, 0),
                    arrowprops=dict(arrowstyle="-|>", color=NAVY, lw=2.2))
        FL.record_patch_edges([O, tip], close=False)
    frame(ax, (-1.85, 1.85), (-1.60, 1.60))
    FL.angle_label(ax, O, tips["right"], tips["upleft"], r"$2x$", fontsize=13,
                   name="2x")
    FL.angle_label(ax, O, tips["upleft"], tips["down"], r"$2y$", fontsize=13,
                   name="2y")
    FL.angle_label(ax, O, tips["down"], tips["right"], r"$a$", fontsize=13,
                   name="a")
    return save(fig, "k_rays_expr")


def strip_rectangles():
    """A single row of 6 cells. Rectangles are chosen by picking two of the 7
    vertical lines: C(7,2) = 21."""
    n = 6
    total = n * (n + 1) // 2
    assert total == 21, total
    fig, ax = start(figsize=(3.4, 1.0))
    frame(ax, (-0.6, n + 0.6), (-0.9, 1.9))
    for i in range(n):
        ax.add_patch(Rectangle((i, 0), 1, 1, fc="none", ec=NAVY, lw=1.8))
    FL.record_patch_edges([(0, 0), (n, 0), (n, 1), (0, 1)])
    return save(fig, "k_strip_rects")


def dart_quadrilateral():
    """A concave (arrowhead) quadrilateral, built from its angles rather than
    drawn by eye: 60 at the apex, 30 and 20 at the two tips, so the REFLEX angle
    at the notch is 360 - 110 = 250. The construction is checked below, because a
    dart drawn approximately is a dart whose answer is wrong."""
    def _rot(v, d):
        t = np.radians(d)
        return np.array([v[0]*np.cos(t) - v[1]*np.sin(t),
                         v[0]*np.sin(t) + v[1]*np.cos(t)])

    def _ang(P, Q, R):                      # angle at Q, in degrees
        u = (P - Q) / np.linalg.norm(P - Q)
        v = (R - Q) / np.linalg.norm(R - Q)
        return np.degrees(np.arccos(np.clip(u @ v, -1, 1)))

    A = np.array([0.0, 0.0])                # apex
    down = np.array([0.0, -1.0])
    L = A + 9.0 * _rot(down, 30)            # right-hand tip
    R = A + 10.2 * _rot(down, -30)          # left-hand tip
    dL = _rot((A - L) / np.linalg.norm(A - L), 30)
    dR = _rot((A - R) / np.linalg.norm(A - R), -20)
    M = np.array([dL, -dR]).T
    t = np.linalg.solve(M, R - L)
    N = L + t[0] * dL                       # the notch
    assert abs(_ang(L, A, R) - 60) < 1e-6
    assert abs(_ang(A, L, N) - 30) < 1e-6
    assert abs(_ang(A, R, N) - 20) < 1e-6
    assert abs((360 - _ang(L, N, R)) - 250) < 1e-6

    pts = [A, L, N, R]
    fig, ax = start(figsize=(5.6, 4.4))
    frame(ax, (-14.0, 13.5), (-13.0, 3.0))
    ax.add_patch(Polygon(pts, closed=True, fc="none", ec=NAVY, lw=2.2))
    FL.record_patch_edges(pts)
    near = lambda V, X, t: V + t * (X - V) / np.linalg.norm(X - V)  # unit arm
    FL.angle_label(ax, A, near(A, L, 3.0), near(A, R, 3.0), r"$60^{\circ}$",
                   fontsize=10, name="60")
    FL.angle_label(ax, L, near(L, A, 3.0), near(L, N, 3.0), r"$30^{\circ}$",
                   fontsize=10, name="30a",
                   steps=[2.2, 2.8, 3.4, 4.0, 4.8, 5.6])
    FL.angle_label(ax, R, near(R, A, 3.0), near(R, N, 3.0), r"$20^{\circ}$",
                   fontsize=10, name="20",
                   steps=[2.4, 3.0, 3.7, 4.4, 5.2, 6.2])
    FL.place(ax, r"$x$", (N[0], N[1]), direction=(0, 1),
             steps=[1.6, 2.2, 2.8, 3.4], fontsize=12, name="x")
    return save(fig, "k_dart")


def circle_with_triangle():
    """A circle with a triangle on a diameter: the diameter is the base and the
    radius is the height. With circumference 20*pi the radius is 10, so the
    circumference is 62.8 and the triangle's area 100 — the AREA wins, which is
    the opposite of what the picture suggests."""
    r = 10
    circ = 2 * np.pi * r
    area = 0.5 * (2 * r) * r
    assert area > circ
    fig, ax = start(figsize=(2.5, 2.5))
    frame(ax, (-1.55, 1.55), (-1.45, 1.55))
    ax.add_patch(Circle((0, 0), 1.0, fc="none", ec=NAVY, lw=2.0))
    ax.plot([-1, 1], [0, 0], color=GREY, lw=1.2)
    tri = [(-1, 0), (1, 0), (0, 1)]
    ax.add_patch(Polygon(tri, closed=True, fc=TEAL, ec=NAVY, lw=1.8, alpha=0.35))
    FL.record_patch_edges(tri)
    FL.record_circle((0, 0), 1.0)
    ax.plot([0, 0], [0, 1], color=INK, lw=1.2, ls=(0, (3, 3)))
    FL.record_patch_edges([(0, 0), (0, 1)], close=False)
    FL.place(ax, r"$r$", (0, 0.5), direction=(-1, 0), steps=[0.16, 0.24, 0.32],
             fontsize=12, name="r")
    return save(fig, "k_circ_tri")


def three_quarter_sector():
    """Three quarters of a circle shaded. The item gives the DIAMETER, so the
    radius is half of it — the whole trap. With diameter 8 the shaded area is
    (3/4)*pi*16 = 12*pi."""
    d = 8
    r = d / 2
    shaded = 0.75 * r ** 2
    assert shaded == 12, shaded
    fig, ax = start(figsize=(2.1, 2.1))
    frame(ax, (-1.45, 1.45), (-1.45, 1.45))
    ax.add_patch(Wedge((0, 0), 1.0, 90, 360, fc=NAVY, ec=NAVY, lw=1.2))
    ax.add_patch(Wedge((0, 0), 1.0, 0, 90, fc="none", ec=NAVY, lw=1.6))
    FL.record_circle((0, 0), 1.0)
    return save(fig, "k_three_quarter")


def bar_employees():
    """Employees per branch. Branch 1 has 150, and a bonus of 60 000 SAR shared
    among them gives 400 each. The other bars exist to make the reader find the
    right one before dividing."""
    B = {"1": 150, "2": 120, "3": 45, "4": 60, "5": 90}
    assert 60000 / B["1"] == 400
    fig, ax = start(figsize=(3.4, 2.0))
    b = ax.bar(list(B), list(B.values()), color=BLUE, width=0.55)
    ax.bar_label(b, fontsize=9.8, padding=1)
    ax.set_ylim(0, 180); ax.set_yticks(range(0, 181, 60))
    ax.set_xlabel("branch", fontsize=10.4); ax.set_ylabel("employees", fontsize=10.4)
    ax.tick_params(labelsize=10.4)
    _clean(ax)
    return save(fig, "k_bar_branches")


def table_scores():
    """Four candidates, three papers, two marks for a correct answer and one
    LOST for a wrong one. In computing, candidate 4 scores 5 correct and 1 wrong
    -> 9, the highest; candidate 1 has more correct answers overall, which is the
    decoy."""
    comp = {"1": (4, 2), "2": (4, 2), "3": (4, 3), "4": (5, 1)}
    sc = {k: 2 * c - w for k, (c, w) in comp.items()}
    assert max(sc, key=sc.get) == "4", sc
    cols = ["Candidate", "Arabic", "Computing", "French"]
    rows = [["1", "3 / 2", "4 / 2", "2 / 4"],
            ["2", "2 / 3", "4 / 2", "4 / 2"],
            ["3", "5 / 1", "4 / 3", "3 / 3"],
            ["4", "3 / 3", "5 / 1", "6 / 1"]]
    return _table("k_table_scores", cols, rows, (3.7, 1.7), first_col=0.28,
                  title="correct / wrong")



# ================================================= PART L SKILLS (new)
def rect_diagonals():
    """A rectangle with both diagonals drawn. Four small triangles meet at the
    centre and each diagonal also cuts the rectangle into two large ones, so the
    count is 4 + 4 = 8 — which the item asks for, so the figure asserts it."""
    W, H = 3.2, 2.0
    small, large = 4, 4
    assert small + large == 8
    P = [(0, 0), (W, 0), (W, H), (0, H)]
    fig, ax = start(figsize=(2.6, 1.9))
    frame(ax, (-0.5, W + 0.5), (-0.45, H + 0.45))
    ax.add_patch(Polygon(P, closed=True, fill=False, ec=NAVY, lw=2.0))
    FL.record_patch_edges(P)
    FL.seg(ax, P[0], P[2], color=NAVY, lw=1.4)
    FL.seg(ax, P[1], P[3], color=NAVY, lw=1.4)
    return save(fig, "l_rect_diagonals")


def median_grid():
    """Sixteen values in a 4 by 4 table. The median is the average of the 8th
    and 9th once they are SORTED, which is 6.5 here — the point of the item is
    that nothing about the table's layout gives it to you."""
    rows = [[3, 8, 5, 12], [7, 2, 9, 4], [11, 6, 10, 1], [5, 13, 8, 6]]
    flat = sorted(v for r in rows for v in r)
    med = (flat[7] + flat[8]) / 2
    assert len(flat) == 16 and med == 6.5, (flat, med)
    cols = ["", "", "", ""]
    body = [[str(v) for v in r] for r in rows]
    fig, ax = start(figsize=(2.5, 1.6))
    ax.axis("off")
    tb = ax.table(cellText=body, loc="center", cellLoc="center",
                  colWidths=[0.25] * 4)
    tb.auto_set_font_size(False); tb.set_fontsize(9.5); tb.scale(1, 1.6)
    for _, cell in tb.get_celld().items():
        cell.set_edgecolor("#9AA6A5"); cell.set_linewidth(0.7)
    return save(fig, "u_median_grid")


for f in (medial, similar, rect_parts, circle_tangent, circle_arcs, segments,
          venn, clock, rhombus, trapezoid, polygon_ext, parallel_iso,
          angles_point, strip, scatter, line_months, invest, subjects,
          visitors, two_bars, grouped_min, grouped_double,
          pie_years, pie_equal, pie_exam, squares_block, ext_angle,
          circles_row, table_cells, table_years,
          count_squares, shaded_square, clock_hands,
          bisector, cyclic, parallel_pair, same_base,
          circle_square, two_circles, grid_rects,
          stairs, tri_in_circle, circles_grid, two_curves, lshape_area,
          square_corner_cut, rays_expression, strip_rectangles, dart_quadrilateral,
          circle_with_triangle, three_quarter_sector, bar_employees, table_scores,
          median_grid, rect_diagonals,
          pie_missing, line_gap, bar_pct_change, hist_class,
          table_growth, stacked_schools, pictogram,
          hist_grouped_freq, bar_revenue_quarters, line_temp_rise,
          line_cyclist_distance, hist_test_scores,
          inscribed, semicircle, tri_306090, tri_4545, midseg, thales,
          sector, hexagon_reg, trapezium, mid_square):
    f()
json.dump(idx, open(os.path.join(OUT, "_index.json"), "w"), indent=1)
print(len(idx), "figures ->", OUT)
