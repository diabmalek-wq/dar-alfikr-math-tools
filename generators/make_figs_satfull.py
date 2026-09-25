"""Figures for the full SAT bank booklet -- 15 Geometry & Trigonometry items
that reference a diagram in their source text. Same house style as the GAT
figures: recessive grid, thin marks, Computer Modern labels, transparent PNG,
400 dpi.
"""
import json, os, shutil
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, Rectangle, Wedge, Arc, FancyArrowPatch
import numpy as np

plt.rcParams.update({
    "mathtext.fontset": "cm", "font.family": "serif",
    "font.serif": ["DejaVu Serif"], "text.color": "#222E2D",
    "axes.edgecolor": "#222E2D", "savefig.transparent": True,
})
OUT, DPI = "figs_satfull", 400
shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(OUT)
TEAL, TEAL_L, MAROON, INK, GRID = "#17A199", "#CFEBE8", "#AD2A22", "#222E2D", "#DCE9E8"
idx = {}


def save(fig, name):
    p = os.path.join(OUT, name + ".png")
    fig.savefig(p, dpi=DPI, bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)
    from PIL import Image
    im = Image.open(p)
    idx[name] = {"file": p, "w": im.width, "h": im.height,
                 "aspect": im.width / im.height}


def blank(ax, pad=0.35):
    ax.set_aspect("equal")
    ax.axis("off")


def right_angle_mark(ax, corner, d1, d2, s=0.16):
    """small square at a right-angle vertex; d1,d2 unit vectors along the two legs"""
    p1 = corner + d1 * s
    p2 = corner + d1 * s + d2 * s
    p3 = corner + d2 * s
    ax.plot([p1[0], p2[0], p3[0]], [p1[1], p2[1], p3[1]], color=INK, lw=0.9)


# --------------------------------------------------------------------- GT-001
# right triangle ABC, right angle at C, generic (no numbers needed on figure)
fig, ax = plt.subplots(figsize=(2.6, 2.2))
A, B, C = np.array([0, 0]), np.array([4, 0]), np.array([4, 2.6])
ax.add_patch(Polygon([A, B, C], closed=True, facecolor=TEAL_L, edgecolor=INK, lw=1.2))
right_angle_mark(ax, C, np.array([-1, 0]), np.array([0, -1]))
ax.text(A[0] - 0.22, A[1] - 0.12, "$A$", fontsize=11, ha="right", va="top")
ax.text(B[0] + 0.15, B[1] - 0.12, "$B$", fontsize=11, ha="left", va="top")
ax.text(C[0] + 0.15, C[1] + 0.05, "$C$", fontsize=11, ha="left", va="bottom")
blank(ax); ax.set_xlim(-0.6, 4.8); ax.set_ylim(-0.6, 3.0)
save(fig, "sat_GT-001")

# --------------------------------------------------------------------- GT-002
# tower height h; two ground points, angle of elevation 30 and 60
fig, ax = plt.subplots(figsize=(3.6, 2.4))
base = np.array([0, 0])
top = np.array([0, 2.6])
p_near = np.array([1.5, 0])
p_far = np.array([4.2, 0])
ax.plot([base[0], top[0]], [base[1], top[1]], color=INK, lw=1.4)
ax.plot([p_far[0], base[0]], [0, 0], color=INK, lw=1.2)
right_angle_mark(ax, base, np.array([0, 1]), np.array([1, 0]))
ax.plot([p_near[0], top[0]], [p_near[1], top[1]], color=TEAL, lw=1.0, ls="--")
ax.plot([p_far[0], top[0]], [p_far[1], top[1]], color=MAROON, lw=1.0, ls="--")
ax.plot(*p_near, "o", color=INK, ms=3); ax.plot(*p_far, "o", color=INK, ms=3)
ax.text(top[0] - 0.1, top[1] + 0.12, "$h$", fontsize=11, ha="center")
ax.text(p_near[0], -0.28, "$60^\\circ$", fontsize=9, ha="center", color=TEAL)
ax.text(p_far[0], -0.28, "$30^\\circ$", fontsize=9, ha="center", color=MAROON)
ax.annotate("", xy=(p_near[0], 0), xytext=(p_far[0], 0),
            arrowprops=dict(arrowstyle="<->", color=INK, lw=0.8))
ax.text((p_near[0] + p_far[0]) / 2, 0.15, "$50$ m", fontsize=9, ha="center")
blank(ax); ax.set_xlim(-0.5, 4.8); ax.set_ylim(-0.6, 3.0)
save(fig, "sat_GT-002")

# --------------------------------------------------------------------- GT-003
# triangle, sides 7 and 8, included angle 120 deg
fig, ax = plt.subplots(figsize=(2.8, 2.4))
V = np.array([0, 0])
P1 = V + np.array([7 * np.cos(np.radians(30)), 7 * np.sin(np.radians(30))]) * 0.4
P2 = V + np.array([8 * np.cos(np.radians(150)), 8 * np.sin(np.radians(150))]) * 0.4
ax.add_patch(Polygon([V, P1, P2], closed=True, facecolor=TEAL_L, edgecolor=INK, lw=1.2))
arc = Arc(V, 1.1, 1.1, angle=0, theta1=30, theta2=150, color=MAROON, lw=1.1)
ax.add_patch(arc)
ax.text(0, 0.75, "$120^\\circ$", fontsize=9, ha="center", color=MAROON)
ax.text(*(V + (P1 - V) * 0.55 + np.array([0.05, -0.25])), "$8$ km", fontsize=9)
ax.text(*(V + (P2 - V) * 0.55 + np.array([-0.55, -0.2])), "$7$ km", fontsize=9)
blank(ax); ax.set_xlim(-3.2, 2.6); ax.set_ylim(-0.6, 2.0)
save(fig, "sat_GT-003")

# --------------------------------------------------------------------- GT-006
# circular plaza radius 45, arc subtending central angle 5pi/6 (=150 deg)
fig, ax = plt.subplots(figsize=(2.6, 2.6))
O = np.array([0, 0])
ax.add_patch(Circle(O, 2, facecolor="white", edgecolor=GRID, lw=1.0))
theta1, theta2 = -75, 75
arc = Arc(O, 4, 4, angle=0, theta1=theta1, theta2=theta2, color=MAROON, lw=2.2)
ax.add_patch(arc)
for th in (theta1, theta2):
    p = O + 2 * np.array([np.cos(np.radians(th)), np.sin(np.radians(th))])
    ax.plot([O[0], p[0]], [O[1], p[1]], color=INK, lw=0.9)
ax.plot(*O, "o", color=INK, ms=3); ax.text(0.1, -0.28, "$O$", fontsize=10, ha="left", va="top")
ax.text(1.0, -1.05, "$45$ m", fontsize=9, ha="center", va="center")
mid = np.radians((theta1 + theta2) / 2)
ax.text(2.75, 0, "$\\frac{5\\pi}{6}$", fontsize=10, color=MAROON, ha="center", va="center")
blank(ax); ax.set_xlim(-2.6, 3.3); ax.set_ylim(-2.6, 2.6)
save(fig, "sat_GT-006")

# --------------------------------------------------------------------- GT-007
# 12x8 rectangle with semicircle of diameter 8 on one 8m side
fig, ax = plt.subplots(figsize=(3.2, 2.4))
w, h = 3.0, 2.0
ax.add_patch(Rectangle((0, 0), w, h, facecolor=TEAL_L, edgecolor=INK, lw=1.2))
ax.add_patch(Wedge((w, h / 2), h / 2, -90, 90, facecolor=TEAL_L, edgecolor=INK, lw=1.2))
ax.text(w / 2, -0.28, "$12$ m", fontsize=9, ha="center")
ax.text(-0.28, h / 2, "$8$ m", fontsize=9, ha="center", va="center", rotation=90)
blank(ax); ax.set_xlim(-0.8, w + h / 2 + 0.5); ax.set_ylim(-0.6, h + 0.6)
save(fig, "sat_GT-007")

# --------------------------------------------------------------------- GT-010
# cylinder + hemisphere dome, same radius
fig, ax = plt.subplots(figsize=(2.2, 3.0))
cx, r, ht = 0, 1.0, 2.2
ax.add_patch(Rectangle((cx - r, 0), 2 * r, ht, facecolor=TEAL_L, edgecolor=INK, lw=1.2))
ax.add_patch(Wedge((cx, ht), r, 0, 180, facecolor=TEAL_L, edgecolor=INK, lw=1.2))
ax.add_patch(Arc((cx, 0), 2 * r, 0.4, angle=0, theta1=0, theta2=180, color=INK, lw=1.0))
ax.text(cx + r + 0.15, ht / 2, "$10$ m", fontsize=9, va="center")
ax.text(cx, ht + r + 0.15, "$r=6$ m", fontsize=9, ha="center")
blank(ax); ax.set_xlim(-1.8, 2.2); ax.set_ylim(-0.4, ht + r + 0.5)
save(fig, "sat_GT-010")

# --------------------------------------------------------------------- GT-011
# two parallel lines cut by a transversal
fig, ax = plt.subplots(figsize=(3.0, 2.2))
ax.plot([-1.6, 1.6], [1.0, 1.0], color=INK, lw=1.2)
ax.plot([-1.6, 1.6], [-1.0, -1.0], color=INK, lw=1.2)
ax.plot([-1.1, 1.1], [-1.7, 1.7], color=TEAL, lw=1.2)
ax.text(-1.85, 1.0, "$\\ell$", fontsize=11, ha="right", va="center")
ax.text(-1.85, -1.0, "$m$", fontsize=11, ha="right", va="center")
ax.text(1.25, 1.55, "$t$", fontsize=11, color=TEAL)
ax.text(0.62, 1.18, "$(3x+10)^\\circ$", fontsize=8.5, ha="left")
ax.text(0.38, -0.82, "$(5x-30)^\\circ$", fontsize=8.5, ha="left")
blank(ax); ax.set_xlim(-2.1, 2.1); ax.set_ylim(-2.0, 2.0)
save(fig, "sat_GT-011")

# --------------------------------------------------------------------- GT-012
# triangle PQR, S on PQ, T on PR, ST || QR
fig, ax = plt.subplots(figsize=(2.8, 2.6))
P = np.array([0, 2.4]); Q = np.array([-1.7, -0.6]); R = np.array([1.9, -0.6])
S = P + (Q - P) * 0.42
T = P + (R - P) * 0.42
ax.add_patch(Polygon([P, Q, R], closed=True, facecolor="none", edgecolor=INK, lw=1.2))
ax.plot([S[0], T[0]], [S[1], T[1]], color=MAROON, lw=1.3)
for pt, lab, dx, dy in [(P, "$P$", 0, 0.15), (Q, "$Q$", -0.2, -0.15), (R, "$R$", 0.2, -0.15),
                          (S, "$S$", -0.32, 0.02), (T, "$T$", 0.28, 0.02)]:
    ax.text(pt[0] + dx, pt[1] + dy, lab, fontsize=10, ha="center")
blank(ax); ax.set_xlim(-2.4, 2.5); ax.set_ylim(-1.2, 2.9)
save(fig, "sat_GT-012")

# --------------------------------------------------------------------- GT-013
# triangle XYZ with exterior angle at X
fig, ax = plt.subplots(figsize=(2.8, 2.2))
X = np.array([-1.8, 1.6]); Y = np.array([-1.8, -0.8]); Z = np.array([1.8, -0.8])
ax.add_patch(Polygon([X, Y, Z], closed=True, facecolor=TEAL_L, edgecolor=INK, lw=1.2))
ext = X + (X - Z) * 0.45
ax.plot([Z[0], ext[0]], [Z[1], ext[1]], color=INK, lw=1.1, ls="--")
arc = Arc(X, 0.9, 0.9, angle=0, theta1=-60, theta2=15, color=MAROON, lw=1.1)
ax.add_patch(arc)
ax.text(X[0] + 0.65, X[1] - 0.05, "$(5x-10)^\\circ$", fontsize=8, color=MAROON)
for pt, lab, dx, dy in [(X, "$X$", -0.05, 0.22), (Y, "$Y$", -0.25, -0.08), (Z, "$Z$", 0.2, -0.08)]:
    ax.text(pt[0] + dx, pt[1] + dy, lab, fontsize=10, ha="center")
blank(ax); ax.set_xlim(-2.6, 2.4); ax.set_ylim(-1.2, 2.2)
save(fig, "sat_GT-013")

# --------------------------------------------------------------------- GT-014
# right triangle DEF, right angle at F
fig, ax = plt.subplots(figsize=(2.6, 2.2))
D, E, F = np.array([0, 0]), np.array([4, 0]), np.array([4, 2.6])
ax.add_patch(Polygon([D, E, F], closed=True, facecolor=TEAL_L, edgecolor=INK, lw=1.2))
right_angle_mark(ax, F, np.array([-1, 0]), np.array([0, -1]))
ax.text(D[0] - 0.22, D[1] - 0.12, "$D$", fontsize=11, ha="right", va="top")
ax.text(E[0] + 0.15, E[1] - 0.12, "$E$", fontsize=11, ha="left", va="top")
ax.text(F[0] + 0.15, F[1] + 0.05, "$F$", fontsize=11, ha="left", va="bottom")
blank(ax); ax.set_xlim(-0.6, 4.8); ax.set_ylim(-0.6, 3.0)
save(fig, "sat_GT-014")

# --------------------------------------------------------------------- GT-016
# cylinder + cone, same radius, r=4, cyl h=12, cone h=3
fig, ax = plt.subplots(figsize=(2.0, 3.0))
cx, r, ht, ch = 0, 0.9, 2.0, 0.7
ax.add_patch(Rectangle((cx - r, 0), 2 * r, ht, facecolor=TEAL_L, edgecolor=INK, lw=1.2))
ax.add_patch(Polygon([[cx - r, ht], [cx + r, ht], [cx, ht + ch]], closed=True,
                      facecolor=TEAL_L, edgecolor=INK, lw=1.2))
ax.add_patch(Arc((cx, 0), 2 * r, 0.35, angle=0, theta1=0, theta2=180, color=INK, lw=1.0))
ax.text(cx + r + 0.15, ht / 2, "$12$ m", fontsize=9, va="center")
ax.text(cx + 0.55, ht + ch / 2, "$3$ m", fontsize=8.5, va="center")
ax.text(cx, -0.35, "$r=4$ m", fontsize=9, ha="center")
blank(ax); ax.set_xlim(-1.7, 2.0); ax.set_ylim(-0.6, ht + ch + 0.4)
save(fig, "sat_GT-016")

# --------------------------------------------------------------------- GT-017
# right triangle JKL, right angle at L
fig, ax = plt.subplots(figsize=(2.6, 2.2))
J, K, L = np.array([0, 0]), np.array([4, 0]), np.array([4, 2.6])
ax.add_patch(Polygon([J, K, L], closed=True, facecolor=TEAL_L, edgecolor=INK, lw=1.2))
right_angle_mark(ax, L, np.array([-1, 0]), np.array([0, -1]))
ax.text(J[0] - 0.22, J[1] - 0.12, "$J$", fontsize=11, ha="right", va="top")
ax.text(K[0] + 0.15, K[1] - 0.12, "$K$", fontsize=11, ha="left", va="top")
ax.text(L[0] + 0.15, L[1] + 0.05, "$L$", fontsize=11, ha="left", va="bottom")
blank(ax); ax.set_xlim(-0.6, 4.8); ax.set_ylim(-0.6, 3.0)
save(fig, "sat_GT-017")

# --------------------------------------------------------------------- GT-021
# circle, chord AB central angle 100, point C on major arc (inscribed angle)
fig, ax = plt.subplots(figsize=(2.6, 2.6))
O = np.array([0, 0]); r = 2
ax.add_patch(Circle(O, r, facecolor="white", edgecolor=GRID, lw=1.0))
aA, aB = 130, 230
A = O + r * np.array([np.cos(np.radians(aA)), np.sin(np.radians(aA))])
B = O + r * np.array([np.cos(np.radians(aB)), np.sin(np.radians(aB))])
C = O + r * np.array([np.cos(np.radians(10)), np.sin(np.radians(10))])
ax.plot([A[0], B[0]], [A[1], B[1]], color=INK, lw=1.1)
ax.plot([O[0], A[0]], [O[1], A[1]], color=INK, lw=0.8)
ax.plot([O[0], B[0]], [O[1], B[1]], color=INK, lw=0.8)
ax.plot([C[0], A[0]], [C[1], A[1]], color=MAROON, lw=1.1)
ax.plot([C[0], B[0]], [C[1], B[1]], color=MAROON, lw=1.1)
ax.plot(*O, "o", color=INK, ms=3)
ax.text(O[0], O[1] - 0.3, "$O$", fontsize=10, ha="center")
ax.text(A[0] - 0.2, A[1] + 0.1, "$A$", fontsize=10, ha="right")
ax.text(B[0] + 0.2, B[1] + 0.1, "$B$", fontsize=10, ha="left")
ax.text(C[0] + 0.2, C[1], "$C$", fontsize=10, ha="left")
arc = Arc(O, 1.0, 1.0, angle=0, theta1=aA, theta2=aB, color=MAROON, lw=1.0)
ax.add_patch(arc)
ax.text(0, 1.15, "$100^\\circ$", fontsize=8.5, ha="center", color=MAROON)
blank(ax); ax.set_xlim(-2.6, 2.6); ax.set_ylim(-2.6, 2.6)
save(fig, "sat_GT-021")

# --------------------------------------------------------------------- GT-029
# circle center O, tangent line at P, point Q on tangent, OP=9, OQ=15
fig, ax = plt.subplots(figsize=(3.0, 2.4))
O = np.array([0, 0]); r = 1.6
ax.add_patch(Circle(O, r, facecolor="white", edgecolor=GRID, lw=1.0))
P = O + np.array([r, 0])
Q = P + np.array([0, 2.0])
ax.plot([P[0], Q[0]], [P[1] - 0.4, Q[1]], color=TEAL, lw=1.2)
ax.plot([O[0], P[0]], [O[1], P[1]], color=INK, lw=1.0)
ax.plot([O[0], Q[0]], [O[1], Q[1]], color=MAROON, lw=1.0, ls="--")
right_angle_mark(ax, P, np.array([-1, 0]), np.array([0, 1]))
ax.plot(*O, "o", color=INK, ms=3); ax.plot(*P, "o", color=INK, ms=3); ax.plot(*Q, "o", color=INK, ms=3)
ax.text(O[0] - 0.2, O[1] - 0.1, "$O$", fontsize=10, ha="right")
ax.text(P[0] + 0.1, P[1] - 0.25, "$P$", fontsize=10)
ax.text(Q[0] + 0.1, Q[1], "$Q$", fontsize=10)
ax.text((O[0] + P[0]) / 2, -0.28, "$9$", fontsize=9, ha="center")
ax.text((O[0] + Q[0]) / 2 - 0.55, (O[1] + Q[1]) / 2 + 0.1, "$15$", fontsize=9, color=MAROON)
ax.text(P[0] + 0.35, (P[1] + Q[1]) / 2, "$\\ell$", fontsize=11, color=TEAL)
blank(ax); ax.set_xlim(-2.0, 2.6); ax.set_ylim(-2.0, 2.4)
save(fig, "sat_GT-029")

# --------------------------------------------------------------------- GT-031
# quadrilateral ABCD, two right triangles sharing diagonal AC
fig, ax = plt.subplots(figsize=(3.0, 2.6))
A = np.array([0, 0]); B = np.array([0, 1.8]); C = np.array([2.4, 0])
D = np.array([-1.6, -1.6])
ax.add_patch(Polygon([A, B, C], closed=True, facecolor=TEAL_L, edgecolor=INK, lw=1.2))
ax.add_patch(Polygon([A, C, D], closed=True, facecolor="#EFE3D9", edgecolor=INK, lw=1.2))
right_angle_mark(ax, B, np.array([0, -1]), np.array([1, 0]))
right_angle_mark(ax, A, np.array([1, 0]), np.array([-1, -1]) / np.linalg.norm([1, 1]))
for pt, lab, dx, dy in [(A, "$A$", -0.28, 0.05), (B, "$B$", -0.05, 0.2),
                          (C, "$C$", 0.25, -0.05), (D, "$D$", -0.05, -0.25)]:
    ax.text(pt[0] + dx, pt[1] + dy, lab, fontsize=10, ha="center")
ax.text((A[0] + B[0]) / 2 - 0.25, (A[1] + B[1]) / 2, "$9$", fontsize=9)
ax.text((B[0] + C[0]) / 2 + 0.15, (B[1] + C[1]) / 2 + 0.1, "$12$", fontsize=9)
ax.text((A[0] + D[0]) / 2 - 0.35, (A[1] + D[1]) / 2, "$8$", fontsize=9)
blank(ax); ax.set_xlim(-2.4, 3.0); ax.set_ylim(-2.2, 2.4)
save(fig, "sat_GT-031")

json.dump(idx, open(os.path.join(OUT, "_index.json"), "w"), indent=1)
print(f"{len(idx)} figures -> {OUT}")
