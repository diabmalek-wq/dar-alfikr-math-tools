"""The GeoGebra exploration for Gr11 Lesson 5-4, rendered as a clip that plays
INSIDE the slide — no add-in, no internet, nothing to install in front of a class.

It answers the slide's own question:
    plot y = sqrt(x+5) and y = x-1        -> they meet ONCE
    then plot y = x+5 and y = (x-1)^2     -> they meet TWICE
    where did the extra one come from?

The extra intersection IS the extraneous root. Squaring both sides is exactly
what creates it, and the picture is the proof.

House graph style throughout (make_graphs_w2.py): recessive grid, arrowheads on
the axes, Computer Modern mathtext, brand ink.
"""
import subprocess
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg

plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["DejaVu Serif"]

W, H, FPS = 1920, 1080, 30
DPI = 120
TEAL = "#17A199"; MAROON = "#AD2A22"; INK = "#222E2D"
MUTED = "#5C6E6C"; GRID = "#DCE9E8"; NAVY = "#1F3864"; BG = "#FAF9F6"

XLIM = (-6.5, 8.5)
YLIM = (-4.5, 11.5)


def ease(p):
    p = max(0.0, min(1.0, p))
    return p * p * (3 - 2 * p)


def axes(ax):
    ax.set_xlim(*XLIM); ax.set_ylim(*YLIM)
    ax.grid(True, color=GRID, lw=0.8, zorder=0)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    ax.spines["left"].set_position(("data", 0))
    ax.spines["bottom"].set_position(("data", 0))
    for sp in ("left", "bottom"):
        ax.spines[sp].set_color(INK); ax.spines[sp].set_linewidth(1.2)
    ax.set_xticks(np.arange(-6, 9, 2))
    ax.set_yticks(np.arange(-4, 12, 2))
    ax.tick_params(colors=MUTED, labelsize=11, length=4, width=1.0)
    ax.plot(1, 0, ">", transform=ax.get_yaxis_transform(), clip_on=False, color=INK, ms=7)
    ax.plot(0, 1, "^", transform=ax.get_xaxis_transform(), clip_on=False, color=INK, ms=7)
    ax.set_axisbelow(True)


def partial(ax, xs, ys, prog, colour, lw=3.0, z=4):
    """Draw a curve progressively, so it is seen being plotted."""
    n = max(2, int(len(xs) * min(1.0, max(0.0, prog))))
    if n >= 2:
        ax.plot(xs[:n], ys[:n], color=colour, lw=lw, zorder=z, solid_capstyle="round")


# ---- the four curves --------------------------------------------------------
XR = np.linspace(-5, 8.5, 700)                 # domain of sqrt(x+5)
YR = np.sqrt(XR + 5)
XL = np.linspace(-6.5, 8.5, 700)
YL = XL - 1                                    # y = x - 1
YLIN = XL + 5                                  # y = x + 5   (squared side)
YPAR = (XL - 1) ** 2                           # y = (x-1)^2 (squared side)

# intersections
ORIG_HIT = (4.0, 3.0)                          # sqrt(9) = 3 = 4 - 1
SQ_HITS = [(4.0, 9.0), (-1.0, 4.0)]            # x+5 = (x-1)^2 at x = 4 and x = -1


def caption(fig, text, y, colour, size, alpha=1.0, weight="normal", style="normal"):
    if alpha <= 0.01:
        return
    fig.text(0.5, y, text, ha="center", va="center", color=colour, fontsize=size,
             alpha=min(1.0, alpha), fontweight=weight, style=style)


def build_frame(t):
    fig = plt.figure(figsize=(W / DPI, H / DPI), dpi=DPI)
    fig.patch.set_facecolor(BG)
    ax = fig.add_axes([0.07, 0.13, 0.62, 0.80])
    ax.set_facecolor(BG)
    axes(ax)

    # ================= ACT 1 — the original equation (0 - 13 s) ==============
    if t < 13.0:
        caption(fig, "The original equation", 0.945, NAVY, 30, ease((t - 0.2) / 0.6),
                weight="bold")
        caption(fig, r"$\sqrt{x+5} = x-1$", 0.055, INK, 30, ease((t - 0.6) / 0.6))

        partial(ax, XR, YR, (t - 1.4) / 2.0, TEAL)
        if t > 2.6:
            ax.text(5.2, 3.9, r"$y=\sqrt{x+5}$", color=TEAL, fontsize=19,
                    alpha=ease((t - 2.6) / 0.6))
        partial(ax, XL, YL, (t - 3.6) / 2.0, MAROON)
        if t > 4.8:
            ax.text(5.6, 6.4, r"$y=x-1$", color=MAROON, fontsize=19,
                    alpha=ease((t - 4.8) / 0.6))

        if t > 6.4:
            a = ease((t - 6.4) / 0.6)
            ax.plot(*ORIG_HIT, "o", ms=15, mfc="none", mec=INK, mew=2.6,
                    alpha=a, zorder=8)
            ax.annotate(r"$(4,\,3)$", ORIG_HIT, xytext=(16, -34),
                        textcoords="offset points", color=INK, fontsize=18, alpha=a)

        panel(fig, t, 7.2, "ONE", "They cross once, and once only.",
              ["x = 4 is the solution.",
               "There is no second crossing anywhere.",
               "Nothing here is extraneous — yet."], TEAL)

    # ================= ACT 2 — square both sides (13 - 27 s) ================
    elif t < 27.0:
        u = t - 13.0
        caption(fig, "Now square both sides", 0.945, NAVY, 30, ease((u - 0.2) / 0.6),
                weight="bold")
        caption(fig, r"$x+5 = (x-1)^{2}$", 0.055, INK, 30, ease((u - 0.6) / 0.6))

        # the originals fade out as their squared versions arrive
        fade = 1.0 - ease((u - 0.8) / 1.2)
        if fade > 0.02:
            ax.plot(XR, YR, color=TEAL, lw=3.0, alpha=fade * 0.35, zorder=2)
            ax.plot(XL, YL, color=MAROON, lw=3.0, alpha=fade * 0.35, zorder=2)

        partial(ax, XL, YLIN, (u - 1.8) / 2.0, TEAL)
        if u > 3.0:
            ax.text(-5.9, 0.6, r"$y=x+5$", color=TEAL, fontsize=19,
                    alpha=ease((u - 3.0) / 0.6))
        partial(ax, XL, YPAR, (u - 4.0) / 2.2, MAROON)
        if u > 5.4:
            ax.text(-5.6, 9.4, r"$y=(x-1)^{2}$", color=MAROON, fontsize=19,
                    alpha=ease((u - 5.4) / 0.6))

        if u > 7.0:
            a = ease((u - 7.0) / 0.6)
            ax.plot(*SQ_HITS[0], "o", ms=15, mfc="none", mec=INK, mew=2.6,
                    alpha=a, zorder=8)
            ax.annotate(r"$(4,\,9)$", SQ_HITS[0], xytext=(16, -30),
                        textcoords="offset points", color=INK, fontsize=18, alpha=a)
        if u > 8.6:
            a = ease((u - 8.6) / 0.6)
            ax.plot(*SQ_HITS[1], "o", ms=17, mfc="none", mec=MAROON, mew=3.0,
                    alpha=a, zorder=9)
            ax.annotate(r"$(-1,\,4)$", SQ_HITS[1], xytext=(-96, 22),
                        textcoords="offset points", color=MAROON, fontsize=18, alpha=a)

        panel(fig, t, 13.0 + 8.0, "TWO", "A second crossing has appeared.",
              ["x = 4 is still there.",
               "But now x = \u22121 crosses as well.",
               "Squaring created it. It was never in the original."], MAROON)

    # ================= ACT 3 — the verdict (27 - 40 s) =======================
    else:
        u = t - 27.0
        caption(fig, "Where did the extra one come from?", 0.945, NAVY, 30,
                ease((u - 0.2) / 0.6), weight="bold")

        ax.plot(XR, YR, color=TEAL, lw=3.0, alpha=0.30, zorder=2)
        ax.plot(XL, YL, color=MAROON, lw=3.0, alpha=0.30, zorder=2)
        ax.plot(XL, YLIN, color=TEAL, lw=3.0, zorder=4)
        ax.plot(XL, YPAR, color=MAROON, lw=3.0, zorder=4)
        ax.plot(*SQ_HITS[0], "o", ms=15, mfc="none", mec=INK, mew=2.6, zorder=8)

        if u > 0.8:
            a = ease((u - 0.8) / 0.8)
            ax.plot(*SQ_HITS[1], "o", ms=17 + 6 * np.sin(u * 3.2) ** 2,
                    mfc="none", mec=MAROON, mew=3.2, alpha=a, zorder=9)

        # at x = -1 the ORIGINAL curve is at 2 and the ORIGINAL line at -2
        if u > 2.4:
            a = ease((u - 2.4) / 0.8)
            ax.plot([-1, -1], [-2, 2], color=MUTED, lw=1.6, ls=":", zorder=6, alpha=a)
            ax.plot([-1], [2], "o", ms=10, mfc="none", mec=TEAL, mew=2.2, alpha=a, zorder=7)
            ax.plot([-1], [-2], "o", ms=10, mfc="none", mec=MAROON, mew=2.2, alpha=a, zorder=7)
            ax.annotate(r"$2$ and $-2$", (-1, 0), xytext=(-152, -44),
                        textcoords="offset points", color=MUTED, fontsize=17, alpha=a)

        caption(fig, r"$2 \neq -2$,  but  $2^{2} = (-2)^{2}$", 0.055, INK, 30,
                ease((u - 4.2) / 0.8))

        panel(fig, t, 27.0 + 5.2, "THE ANSWER",
              "Squaring makes 2 and \u22122 the same number.",
              ["That is how x = \u22121 gets in.",
               "It satisfies the squared equation.",
               "It does NOT satisfy the original.",
               "The check at the end throws it out."], NAVY)

    canvas = FigureCanvasAgg(fig)
    canvas.draw()
    buf = np.asarray(canvas.buffer_rgba())[:, :, :3].copy()
    plt.close(fig)
    return buf


def _wrap(text, n):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if len(t) <= n:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    return lines


def panel(fig, t, t0, tag, lead, bullets, colour):
    """The reading panel on the right, revealed a line at a time.
    fig.text(wrap=True) wraps against the FIGURE width, not the panel, so the
    lead ran outside the box — every line is wrapped by hand here instead."""
    a = ease((t - t0) / 0.6)
    if a <= 0.02:
        return
    fig.patches.append(plt.Rectangle((0.715, 0.17), 0.245, 0.64, transform=fig.transFigure,
                                     facecolor="#0E4F4C", edgecolor="none", alpha=a * 0.96,
                                     zorder=20))
    fig.text(0.735, 0.768, tag, color="#7FD9D2", fontsize=17, fontweight="bold",
             alpha=a, zorder=21, va="center")

    y = 0.722
    for ln in _wrap(lead, 24):
        fig.text(0.735, y, ln, color="white", fontsize=17.5, alpha=a, zorder=21,
                 va="center", fontweight="bold")
        y -= 0.042
    y -= 0.030

    for i, b in enumerate(bullets):
        ai = ease((t - t0 - 0.7 - i * 0.7) / 0.5)
        if ai <= 0.02:
            y -= 0.042 * len(_wrap(b, 33))
            continue
        for ln in _wrap(b, 33):
            fig.text(0.735, y, ln, color="#DDEEEC", fontsize=14.5, alpha=ai,
                     zorder=21, va="center")
            y -= 0.042
        y -= 0.018


TOTAL = 40.0

if __name__ == "__main__":
    n = int(TOTAL * FPS)
    print(f"{TOTAL:.0f}s, {n} frames")
    p = subprocess.Popen(
        ["ffmpeg", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
         "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium",
         "-crf", "21", "-pix_fmt", "yuv420p", "GeoGebra_Gr11_5-4_Extraneous.mp4"],
        stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for i in range(n):
        p.stdin.write(build_frame(i / FPS).tobytes())
        if i % 200 == 0:
            print(f"  {i}/{n}", flush=True)
    p.stdin.close(); p.wait()
    print("done")
