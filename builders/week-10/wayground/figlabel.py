"""Label placement with a mechanical no-overlap guarantee.

Mr Thiab's rule: a variable or an angle must never sit on top of the shape it
labels. Judging that by eye across twenty figures does not scale and does not
survive the next edit, so it is enforced here instead.

How it works. Every line, polygon edge and circle drawn through these helpers is
recorded as a polyline in DATA coordinates. When a label is placed, its rendered
bounding box is measured, padded, and tested against every recorded polyline. If
any ink passes through the box the label is pushed further out along its own
escape direction and measured again; if nothing clears, the build fails rather
than shipping a figure with a label sitting on a line.

`angle_label` puts an angle where a mathematician would — on the internal
bisector of the angle, inside the shape — and then lets the same guard push it
until it is clear of both arms.
"""
import numpy as np

_SEGS = []          # list of (N,2) polylines in data coords
_LABELS = []        # texts placed since the last reset
_BOXES = []         # their data-coordinate boxes, so labels also avoid each other


def reset():
    _SEGS.clear(); _LABELS.clear(); _BOXES.clear()


def _record(pts):
    _SEGS.append(np.asarray(pts, dtype=float))


def seg(ax, p, q, **kw):
    """A straight segment, drawn and recorded."""
    p = np.asarray(p, float); q = np.asarray(q, float)
    ax.plot([p[0], q[0]], [p[1], q[1]], **kw)
    _record([p, q])


def polyline(ax, pts, close=False, **kw):
    pts = np.asarray(pts, float)
    if close:
        pts = np.vstack([pts, pts[:1]])
    ax.plot(pts[:, 0], pts[:, 1], **kw)
    _record(pts)


def record_patch_edges(pts, close=True):
    """Record the outline of a patch that was added with add_patch."""
    pts = np.asarray(pts, float)
    if close:
        pts = np.vstack([pts, pts[:1]])
    _record(pts)


def record_circle(c, r, n=180):
    t = np.linspace(0, 2 * np.pi, n)
    _record(np.stack([c[0] + r * np.cos(t), c[1] + r * np.sin(t)], axis=1))


def _bbox_data(ax, txt, pad_pts=2.5):
    """The label's rendered box, in data coordinates, padded a little."""
    fig = ax.figure
    fig.canvas.draw()
    bb = txt.get_window_extent(fig.canvas.get_renderer())
    pad = pad_pts * fig.dpi / 72.0
    bb = bb.expanded(1.0, 1.0)
    inv = ax.transData.inverted()
    (x0, y0) = inv.transform((bb.x0 - pad, bb.y0 - pad))
    (x1, y1) = inv.transform((bb.x1 + pad, bb.y1 + pad))
    return min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1)


def _overlaps(a, b):
    return not (a[2] < b[0] or b[2] < a[0] or a[3] < b[1] or b[3] < a[1])


def _hits(box, samples=90):
    for other in _BOXES:                       # a label must not sit on a label
        if _overlaps(box, other):
            return True
    x0, y0, x1, y1 = box
    for poly in _SEGS:
        for i in range(len(poly) - 1):
            a, b = poly[i], poly[i + 1]
            t = np.linspace(0, 1, samples)[:, None]
            pts = a + (b - a) * t
            if np.any((pts[:, 0] >= x0) & (pts[:, 0] <= x1)
                      & (pts[:, 1] >= y0) & (pts[:, 1] <= y1)):
                return True
    return False


def _inside_axes(ax, box):
    """A label pushed past the axes does not render at all — it just goes missing
    from the saved figure, which reads as a forgotten label rather than a bug.
    Reject those positions here so the build fails loudly instead."""
    (ax0, ax1), (ay0, ay1) = ax.get_xlim(), ax.get_ylim()
    x0, y0, x1, y1 = box
    return x0 >= min(ax0, ax1) and x1 <= max(ax0, ax1) \
        and y0 >= min(ay0, ay1) and y1 <= max(ay0, ay1)


def place(ax, text, xy, direction=(0, 0), steps=(0,), fontsize=13,
          color="#222E2D", name="label", pad=2.5, **kw):
    """Draw `text` at `xy`, pushing it along `direction` until nothing is under it.

    `steps` are the distances to try, in data units, in order. The first that
    leaves the box clear of every recorded line wins.
    """
    d = np.asarray(direction, float)
    if np.linalg.norm(d) > 0:
        d = d / np.linalg.norm(d)
    xy = np.asarray(xy, float)
    ha = kw.pop("ha", "center"); va = kw.pop("va", "center")
    for s in steps:
        t = ax.annotate(text, xy + d * s, fontsize=fontsize, color=color,
                        ha=ha, va=va, **kw)
        box = _bbox_data(ax, t, pad_pts=pad)
        if not _hits(box) and _inside_axes(ax, box):
            _LABELS.append(t); _BOXES.append(box)
            return t
        t.remove()
    raise AssertionError(
        f"{name}: no offset in {steps} both clears the drawing and stays inside "
        f"the axes — widen the axes limits or move the label somewhere else")


def angle_label(ax, V, A, B, text, steps=None, fontsize=13, color="#222E2D",
                name="angle", pad=1.0):
    """Put an angle label on the INTERNAL bisector of angle AVB, clear of both arms.

    The steps are scaled by the SHORTER arm and start close in, because a label
    pushed too far along the bisector of a narrow angle runs into the far side."""
    V = np.asarray(V, float); A = np.asarray(A, float); B = np.asarray(B, float)
    u = (A - V) / np.linalg.norm(A - V)
    v = (B - V) / np.linalg.norm(B - V)
    bis = u + v
    if np.linalg.norm(bis) < 1e-9:                 # a straight angle
        bis = np.array([-u[1], u[0]])
    bis = bis / np.linalg.norm(bis)
    span = min(np.linalg.norm(A - V), np.linalg.norm(B - V))
    if steps is None:
        steps = [span * f for f in (0.16, 0.20, 0.25, 0.30, 0.36, 0.43, 0.52,
                                    0.62, 0.74, 0.88, 1.05, 1.25)]
    return place(ax, text, V, bis, steps, fontsize=fontsize, color=color,
                 name=name, pad=pad, ha="center", va="center")


def outside_label(ax, text, anchor, direction, base=0.18, fontsize=13,
                  color="#222E2D", name="label", grow_out=True):
    """A label placed OUTSIDE the shape, pushed along `direction` until clear.

    With grow_out, the box is anchored by the EDGE facing the shape rather than
    by its centre, so a long word grows away from the drawing instead of forcing
    the guard to shove the whole label halfway across the figure."""
    d = np.asarray(direction, float)
    ha, va = "center", "center"
    if grow_out and np.linalg.norm(d) > 0:
        d = d / np.linalg.norm(d)
        if abs(d[0]) > 0.35:
            ha = "left" if d[0] > 0 else "right"
        if abs(d[1]) > 0.35:
            va = "bottom" if d[1] > 0 else "top"
    steps = [base * f for f in (1.0, 1.4, 1.9, 2.5, 3.2, 4.2, 5.5, 7.0)]
    return place(ax, text, anchor, direction, steps, fontsize=fontsize,
                 color=color, name=name, ha=ha, va=va)
