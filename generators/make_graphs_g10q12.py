from gfx import *
S = Set("graphs_g10q12", {"g_vertex": 5.6, "g_std": 5.0})

# ---- vertex form: f(x) = 2(x-3)^2 - 1
fig, ax = S.fig(6.0, 3.9)
S.axes(ax, (-1.5, 7.5), (-2.5, 9.5))
f = lambda x: 2 * (x - 3) ** 2 - 1
xs = np.linspace(-0.2, 6.2, 400); S.curve(ax, xs, f(xs), TEAL)
ax.plot([3, 3], [-2.5, 9.5], color=RED, lw=1.5, ls="--", zorder=3); fl.polyline(ax, [(3, -2.5), (3, 9.5)], lw=0)
for x, y in [(3, -1), (2, 1), (4, 1), (1, 7), (5, 7)]:
    assert f(x) == y; S.dot(ax, x, y)
S.label(ax, r"vertex $(3,-1)$", (3, -1), direction=(1, -0.4), steps=(1.6, 2.0, 2.4), ha="center")
S.label(ax, r"axis $x=3$", (3, 8.6), direction=(1, 0), steps=(1.3, 1.6), ha="center")
S.label(ax, r"$f(x)=2(x-3)^{2}-1$", (6.0, 5.5), direction=(0, -1), steps=(0.2, 0.6, 1.0, 1.4), ha="center")
S.label(ax, r"$(1,7)$", (1, 7), direction=(1, 0), steps=(1.3, 1.5, 1.7), ha="center")
S.label(ax, r"$(5,7)$", (5, 7), direction=(-1, 0), steps=(1.3, 1.5, 1.7), ha="center")
S.save(fig, "g_vertex")

# ---- standard form: f(x) = x^2 - 6x + 5
fig, ax = S.fig(5.6, 3.9)
S.axes(ax, (-1.5, 9.5), (-6.5, 7.5))
g = lambda x: x ** 2 - 6 * x + 5
xs = np.linspace(-0.6, 6.6, 400); S.curve(ax, xs, g(xs), BLUE)
ax.plot([3, 3], [-6.5, 7.5], color=RED, lw=1.5, ls="--", zorder=3); fl.polyline(ax, [(3, -6.5), (3, 7.5)], lw=0)
for x, y in [(3, -4), (0, 5), (6, 5), (1, 0), (5, 0)]:
    assert g(x) == y; S.dot(ax, x, y, NAVY if (x, y) != (0, 5) else ORANGE)
S.label(ax, r"vertex $(3,-4)$", (3, -4), direction=(1, -0.45), steps=(2.0, 2.4, 2.8), ha="center")
S.label(ax, r"$(0,5)$", (0, 5), direction=(1, 0.8), steps=(1.2, 1.5, 1.8), ha="center")
S.label(ax, r"axis $x=3$", (3, 6.8), direction=(1, 0), steps=(1.3, 1.7), ha="center")
S.label(ax, r"$(6,5)$", (6, 5), direction=(-1, 0.6), steps=(1.0, 1.3, 1.6), ha="center")
S.label(ax, r"$f(x)=x^{2}-6x+5$", (7.6, 2.6), direction=(0, 1), steps=(0.0, 0.5, 1.0, 1.5), ha="center")
S.save(fig, "g_std")
S.done()
