FIGSTYLE = r"""
\tikzset{axisline/.style={-{Stealth[length=2.2mm]},thick,INK},gridl/.style={LINE!80,very thin},
 ln/.style={very thick,BLUE},pt/.style={circle,fill=ORANGE,inner sep=1.6pt}}
"""
def axes(xmin, xmax, ymin, ymax, xs=1, ys=1, xl='x', yl='y', lab_x=None, lab_y=None, ymult=1):
    """return tikz code (inside picture) for a grid with axes and tick labels"""
    s = []
    s.append(r"\draw[gridl] (%s,%s) grid[xstep=%s,ystep=%s] (%s,%s);" % (xmin, ymin, xs, ys, xmax, ymax))
    s.append(r"\draw[axisline] (%s,0) -- (%s,0) node[right]{$%s$};" % (xmin, xmax + 0.35, xl))
    s.append(r"\draw[axisline] (0,%s) -- (0,%s) node[above]{$%s$};" % (ymin, ymax + 0.35, yl))
    lx = lab_x if lab_x is not None else xs
    ly = lab_y if lab_y is not None else ys
    x = xmin
    xt = []
    import math
    k = math.ceil(xmin / lx)
    while k * lx <= xmax:
        v = k * lx
        if abs(v) > 1e-9:
            xt.append(r"\draw (%s,0.07)--(%s,-0.07) node[below,font=\scriptsize]{$%g$};" % (v, v, v))
        k += 1
    k = math.ceil(ymin / ly)
    while k * ly <= ymax:
        v = k * ly
        if abs(v) > 1e-9:
            xt.append(r"\draw (0.07,%s)--(-0.07,%s) node[left,font=\scriptsize]{$%g$};" % (v, v, v*ymult))
        k += 1
    s += xt
    s.append(r"\node[below left,font=\scriptsize] at (0,0) {$O$};")
    return "\n".join(s)


def fig(body, scale=1.0, xu=0.55, yu=0.55):
    return (r"\begin{center}\begin{tikzpicture}[x=%scm,y=%scm,scale=%s]" % (xu, yu, scale)
            + FIGSTYLE + body + r"\end{tikzpicture}\end{center}")


