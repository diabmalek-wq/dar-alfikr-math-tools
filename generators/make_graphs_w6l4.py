from gfx import *
S = Set("graphs_w6l4", {"g_inv": 3.8, "g_shift": 5.6})

# ---- inverse pair, equal scales so the reflection across y = x is honest
fig, ax = S.fig(4.7, 4.7)
S.axes(ax, (-1.5, 10.5), (-1.5, 10.5), equal=True)
xs = np.linspace(-1.5, 2.2, 300); S.curve(ax, xs, 3.0 ** xs, TEAL)
xl = np.linspace(0.12, 10.4, 400); S.curve(ax, xl, np.log(xl) / np.log(3), ORANGE)
S.line(ax, (-1.5, -1.5), (10.5, 10.5), color=GREY, lw=1.2, ls=":")
pairs = [((0, 1), (1, 0)), ((1, 3), (3, 1)), ((2, 9), (9, 2))]
for (a, b), (c, d) in pairs:
    assert abs(3.0 ** a - b) < 1e-12 and abs(np.log(c) / np.log(3) - d) < 1e-12 and (a, b) == (d, c)
    S.dot(ax, a, b); S.dot(ax, c, d)
    S.line(ax, (a, b), (c, d), color=GREY, lw=0.8, ls="--")
S.label(ax, r"$f(x)=3^{x}$", (3.9, 8.3), direction=(1, 0), steps=(0.0, 0.4, 0.8), ha="center")
S.label(ax, r"$f^{-1}(x)=\log_3 x$", (8.0, 1.5), direction=(0, -1), steps=(0.3, 0.7, 1.1), ha="center")
S.label(ax, r"$y=x$", (8.2, 7.2), direction=(1, -1), steps=(0.3, 0.7, 1.1, 1.5), ha="center")
S.label(ax, r"$(2,9)$", (2, 9), direction=(-1, 0.3), steps=(1.0, 1.4, 1.8))
S.label(ax, r"$(9,2)$", (9, 2), direction=(0, 1), steps=(0.7, 1.1))
S.save(fig, "g_inv")

# ---- shift: f(x) = log3 x  and  g(x) = log3(x-2) + 1
fig, ax = S.fig(6.0, 3.9)
S.axes(ax, (-1.5, 12.5), (-3.5, 4.5))
x1 = np.linspace(0.04, 12.4, 500); S.curve(ax, x1, np.log(x1) / np.log(3), BLUE)
x2 = np.linspace(2.03, 12.4, 500); S.curve(ax, x2, np.log(x2 - 2) / np.log(3) + 1, ORANGE)
ax.plot([0, 0], [-3.5, 4.5], color=RED, lw=1.5, ls="--", zorder=3)
ax.plot([2, 2], [-3.5, 4.5], color=RED, lw=1.5, ls="--", zorder=3)
fl.polyline(ax, [(2, -3.5), (2, 4.5)], lw=0)
for x, y in [(1, 0), (3, 1), (9, 2)]:
    assert abs(np.log(x) / np.log(3) - y) < 1e-12; S.dot(ax, x, y, BLUE)
for x, y in [(3, 1), (5, 2), (11, 3)]:
    assert abs(np.log(x - 2) / np.log(3) + 1 - y) < 1e-12; S.dot(ax, x, y, ORANGE)
S.label(ax, r"$f(x)=\log_3 x$", (9.0, 0.6), direction=(0, -1), steps=(0.2, 0.6, 1.0), ha="center")
S.label(ax, r"$g(x)=\log_3(x-2)+1$", (9.5, 3.6), direction=(0, 1), steps=(0.2, 0.5), ha="center")
S.label(ax, r"$x=0$", (0.0, 4.0), direction=(1, 0), steps=(0.8, 0.9, 1.0), ha="center")
S.label(ax, r"$x=2$", (2.0, -3.0), direction=(1, 0), steps=(0.7, 1.1), ha="center")
S.label(ax, r"$(5,2)$", (5, 2), direction=(-1, 0.4), steps=(0.7, 1.1), ha="center")
S.save(fig, "g_shift")
S.done()
