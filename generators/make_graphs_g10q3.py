from gfx import *
S = Set("graphs_g10q3", {"g_fac": 5.4, "g_pos": 5.2})
f = lambda x: (x + 1) * (x - 3)

# ---- factored form: zeros, vertex, y-intercept
fig, ax = S.fig(5.6, 3.9)
S.axes(ax, (-5.5, 8.5), (-6.5, 6.5))
xs = np.linspace(-2.6, 4.6, 400); S.curve(ax, xs, f(xs), TEAL)
ax.plot([1, 1], [-6.5, 6.5], color=RED, lw=1.5, ls="--", zorder=3); fl.polyline(ax, [(1, -5.5), (1, 6.5)], lw=0)
for x, y, c in [(-1, 0, ORANGE), (3, 0, ORANGE), (1, -4, NAVY), (0, -3, NAVY)]:
    assert f(x) == y; S.dot(ax, x, y, c)
S.label(ax, r"zero $x=-1$", (-1, 0), direction=(-1, 0.5), steps=(1.4, 1.8, 2.2, 2.6), ha="center")
S.label(ax, r"zero $x=3$", (3, 0), direction=(1, 0.5), steps=(1.4, 1.8, 2.2, 2.6), ha="center")
S.label(ax, r"vertex $(1,-4)$", (1, -4), direction=(1, -0.3), steps=(1.7, 2.1, 2.5), ha="center")
S.label(ax, r"$(0,-3)$", (0, -3), direction=(-1, -0.6), steps=(2.4, 2.8, 3.2), ha="center")
S.label(ax, r"axis $x=1$", (1, 6.0), direction=(1, 0), steps=(1.2, 1.6), ha="center")
S.label(ax, r"$f(x)=(x+1)(x-3)$", (5.8, -1.8), direction=(0, -1), steps=(0.0, 0.4, 0.8, 1.2), ha="center")
S.save(fig, "g_fac")

# ---- intervals: curve above the axis (teal) and below (orange)
fig, ax = S.fig(5.6, 3.9)
S.axes(ax, (-4.5, 7.5), (-6.5, 6.5))
xa = np.linspace(-2.6, -1, 100); xb = np.linspace(-1, 3, 200); xc = np.linspace(3, 4.6, 100)
S.curve(ax, xa, f(xa), TEAL); S.curve(ax, xb, f(xb), ORANGE); S.curve(ax, xc, f(xc), TEAL)
for x in (-1, 3):
    assert f(x) == 0; S.dot(ax, x, 0, NAVY)
assert f(-2) > 0 and f(0) < 0 and f(4) > 0
S.label(ax, r"$f(x)>0$", (-2.8, -2.0), direction=(0, -1), steps=(0.0, 0.4, 0.8, 1.2), ha="center")
S.label(ax, r"$f(x)>0$", (5.2, -2.0), direction=(0, -1), steps=(0.0, 0.4, 0.8, 1.2), ha="center")
S.label(ax, r"$f(x)<0$", (1, -4), direction=(0, -1), steps=(0.7, 1.0, 1.3), ha="center")
S.label(ax, r"$-1$", (-1, 0), direction=(-1, 1), steps=(0.7, 1.0, 1.4), ha="center")
S.label(ax, r"$3$", (3, 0), direction=(1, 1), steps=(0.7, 1.0, 1.4), ha="center")
S.save(fig, "g_pos")
S.done()
