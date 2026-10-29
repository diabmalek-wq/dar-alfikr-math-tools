# Desmos Graphs: Parabola, Focus and Directrix

Interactive graphs for Algebra II / Precalculus (conic sections: parabolas). Author: Mr. Malek Thiab.

| Graph | Link |
|---|---|
| Vertical parabola | https://www.desmos.com/calculator/8yn8qatrhw |
| Horizontal parabola | https://www.desmos.com/calculator/y7yvepvvyq |

## What each graph shows

Every point $P$ on a parabola is the same distance from the focus $F$ and the directrix: $d_{PF}=d_{PD}$, where $D$ is the foot of the perpendicular from $P$ to the directrix.

| | Vertical | Horizontal |
|---|---|---|
| Equation | $(x-h)^2=4p(y-k)$ | $(y-k)^2=4p(x-h)$ |
| Vertex | $V(h,k)$ | $V(h,k)$ |
| Focus | $F(h,\,k+p)$ | $F(h+p,\,k)$ |
| Directrix | $y=k-p$ | $x=h-p$ |
| Point on curve | $P\left(t,\ k+\dfrac{(t-h)^2}{4p}\right)$ | $P\left(h+\dfrac{(t-k)^2}{4p},\ t\right)$ |
| Foot on directrix | $D(t,\ k-p)$ | $D(h-p,\ t)$ |

Sliders: `h`, `k` move the vertex; `p` is the signed distance from vertex to focus (a negative `p` flips the opening); `t` slides $P$ along the curve.

## Distance labels on the grid

The green segment $PF$ and the red segment $PD$ carry live labels ("PF = ...", "PD = ..."), placed on the midpoints $M_1=\frac{P+F}{2}$ and $M_2=\frac{P+D}{2}$. Desmos point labels are static text, so the numbers are refreshed by a short script (a `HelperExpression` on $d_{PF}$ and $d_{PD}$ that rewrites the two labels). If a graph is saved and reopened, the labels show the values from the moment of saving until the script is run again.

## Rebuilding a graph

Run in the browser console on desmos.com/calculator: `Calc.setBlank()`, then `Calc.setExpressions([...])` with the expressions in the table above (sliders `h`, `k`, `p`, `t`; the parabola; the directrix; points $V$, $F$, $P$, $D$; `polygon(P,F)` and `polygon(P,D)`; $d_{PF}=\operatorname{distance}(P,F)$, $d_{PD}=\operatorname{distance}(P,D)$). Note: `Calc.setState` with a hand-written state did not evaluate; use `setBlank` plus `setExpressions`.
