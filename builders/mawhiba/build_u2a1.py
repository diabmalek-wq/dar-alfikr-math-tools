"""MAWHIBA Grade 9 · Unit 2 (Linear Functions) · Activity 1 — Mappings of linear functions. Week 6.
Worksheet 2 pages (student-facing, nothing pre-answered) + Key 1 page (teacher-facing, separate file).
Tasks 1-4 are the Student Book's own. Every transformation, scale factor, centre and fixed value is
re-derived in make_u2.py (exact fractions) and asserted against the Teacher's Guide.
SOURCE NOTE: the printed Student Book text drops the fractions in c, g and h. They are reconstructed
from the Teacher's Guide (scale factor, centre and fixed value stated for each) and re-derived."""
import json
from build_mawhiba_a1 import CSS, HEADER, render

IDX = json.load(open("math_mawu2/_index.json"))
SC = 0.80

def eq(key, scale=SC, inline=False):
    k = "u_" + key; assert k in IDX, k
    h = round(IDX[k]["hin"] * 25.4 * scale, 2)
    return f'<img class="{"inl" if inline else "eq"}" src="math_mawu2/{k}.png" style="max-height:{h}mm">'

def foot(left, page, of):
    return (f'<footer><span>{left}</span><span class="motto">Faith, Righteousness and Wisdom</span>'
            f'<span>Mr Malek Thiab · Page {page} of {of}</span></footer>')

TITLE = ('<div class="title"><h1><small>Mawhiba Grade 9 · Unit 2 Linear Functions · Activity 1 · Week 6</small>'
         'Mappings of Linear Functions</h1><div class="meta">Advanced Supplementary Mathematics<br>'
         'Mawhiba Schools Partnership</div></div>')
IDBAR = ('<div class="idbar"><div><b>Student</b> ..............................................</div>'
         '<div><b>Class</b> ....................</div><div><b>Date</b> ......... / ......... / 2026</div>'
         '<div><b>Teacher</b> Mr Malek Thiab</div></div>')
EXTRA = """
  .fc { border:1px solid var(--line); border-radius:2mm; padding:1.2mm 2.2mm 1mm; break-inside:avoid; }
  .fc .top { display:flex; justify-content:space-between; align-items:center; margin-bottom:.4mm; }
  .fc .top .n { color:#fff; background:var(--plum); border-radius:1mm; font-size:7.6pt; padding:.5mm 1.6mm; font-weight:bold; }
  .fc img.dbl { display:block; width:100%; }
  .fc .ln { border-bottom:1px dotted #9AA6A5; height:4.6mm; font-size:7.2pt; color:var(--grey); }
  table.cj { width:100%; border-collapse:collapse; font-size:8pt; }
  table.cj th { background:var(--tint); color:var(--navy); font-size:7.2pt; text-transform:uppercase; letter-spacing:.04em;
                padding:1.2mm; border:1px solid var(--line); }
  table.cj td { border:1px solid var(--line); padding:1.2mm 1.6mm; vertical-align:middle; height:9mm; }
  table.cj td.l { width:30mm; font-weight:bold; color:var(--plum); }
  table.t3 td { height:11mm; }
  .val { display:flex; flex-wrap:wrap; gap:1.8mm; font-size:7.8pt; margin-top:1mm; }
  .val span { border:1px solid var(--line); border-radius:1mm; padding:.8mm 1.8mm; }
  img.xy { display:block; margin:0 auto; width:62mm; }
"""

def card(k, n):
    return (f'<div class="fc"><div class="top">{eq("f"+k, 0.8, True)}<span class="n">{n}</span></div>'
            f'<img class="dbl" src="fig/dbl.png" alt="">'
            f'<div class="ln">Describe it as a transformation of the number line:</div>'
            f'<div class="ln">Does any value map onto itself?  Which?</div></div>')

def worksheet():
    cards = "".join(card(k, r) for k, r in zip("abcdefgh", ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii"]))
    p1 = f"""<style>{EXTRA}</style>{HEADER}{TITLE}{IDBAR}
<div class="grid g2" style="margin-bottom:2.2mm">
  <div class="card tint"><h2 class="p">What this activity is for</h2>
    <ul><li>Identify the properties of linear functions and their graphs.</li>
    <li>Use geometrical and algebraic reasoning to express generalisations and prove results.</li>
    <li>Visualise a function as a transformation of the number line, then generalise.</li></ul></div>
  <div class="card tint"><h2 class="t">How you will be judged</h2>
    <ul><li><b>Accuracy</b> — notation and mapping diagrams drawn correctly.</li>
    <li><b>Classifying</b> — naming each transformation: reflection, translation or enlargement.</li>
    <li><b>Generalising</b> — linking the algebra of mx + c to the geometry, and explaining why.</li></ul></div>
</div>
<div class="card" style="margin-bottom:2.2mm">
  <h2 class="g">Task 1 · Draw it, then name it</h2>
  <p>The identity function {eq("id", 0.8, True)} maps every value onto itself, so its mapping diagram is a set of
  <b>vertical</b> lines joining each number to itself. For each function below, draw the arrows from a few values of
  <b>x</b> on the top line to <b>f(x)</b> on the bottom line (use at least five values, including some negative ones where
  they fit), then describe the whole mapping as a transformation of the number line. Share the cards in a group of three or four.</p>
</div>
<div class="grid g2" style="gap:2mm">{cards}</div>
{foot("Week 6 · Mawhiba Unit 2 Activity 1", 1, 3)}"""

    rows = "".join(f'<tr><td class="l">{lab}</td><td></td><td></td></tr>' for lab in
                   ["m = 1", "m = −1", "m > 1", "0 < m < 1", "m < 0, m ≠ −1"])
    t3 = "".join(f'<tr><td class="l" style="width:46mm">{eq("f"+k, 0.8, True)}</td><td style="width:34mm"></td><td></td></tr>'
                 for k in "abcdefgh")
    p2 = f"""<style>{EXTRA}</style>{HEADER}
<div class="card" style="margin-bottom:2.2mm">
  <h2 class="g">Task 2 · Generalise: {eq("gen", 0.8, True)}</h2>
  <p style="margin-bottom:1.4mm">Sort your eight examples by the value of <b>m</b>. For each case write what the function does to
  the number line, and test your idea on a new example of your own. Discuss your conjectures with others.</p>
  <table class="cj"><tr><th>Value of m</th><th>Transformation of the number line</th><th>Where do the arrows meet? (evidence)</th></tr>{rows}</table>
  <p style="margin:1.4mm 0 .6mm"><b>What does c do?</b> Does it change the type of transformation, or only its position?</p>
  <div class="rule"></div>
</div>
<div class="card" style="margin-bottom:2.2mm">
  <h2 class="t">Task 3 · Does any value map onto itself?</h2>
  <p style="margin-bottom:1.4mm">For each function find the value of x that maps onto itself, (a) from your mapping diagram
  (extend the arrows if they have not met) and (b) by solving {eq("id", 0.8, True)} = f(x) algebraically. If there is none, say why.</p>
  <table class="cj t3"><tr><th>Function</th><th>(a) From the diagram</th><th>(b) By solving an equation</th></tr>{t3}</table>
</div>
{foot("Week 6 · Mawhiba Unit 2 Activity 1", 2, 3)}"""
    p3 = f"""<style>{EXTRA}</style>{HEADER}
<div class="card" style="margin-bottom:2.4mm">
  <h2 class="p">Task 4 · The general function {eq("gen", 0.8, True)}</h2>
  <p style="margin-bottom:1.2mm">Is there always a value of x that maps onto itself? Put {eq("gen", 0.8, True)} equal to x and investigate.
  Explain your findings in words and in algebra.</p>
  <div class="rule"></div><div class="rule"></div><div class="rule"></div><div class="rule"></div>
  <p style="margin:2mm 0 1mm">Which functions have <b>no</b> such value? Say why their graph never meets the graph of {eq("id", 0.8, True)}.</p>
  <div class="rule"></div><div class="rule"></div><div class="rule"></div>
</div>
<div class="grid g2" style="margin-bottom:2.4mm">
  <div class="card tint"><h2 class="t">Sketch it</h2>
    <p class="footnote" style="margin-bottom:1.2mm">On the grid draw y = x, then y = 3x − 2 (function d) and y = x − 4 (function b).
    Mark where each meets y = x and label the point.</p>
    <img class="xy" src="fig/xy.png" alt="blank grid" style="width:78mm"></div>
  <div class="card tint"><h2 class="g">Connect it</h2>
    <p style="margin-bottom:1.2mm">Look back at your mapping diagrams for d and b.</p>
    <ul><li>Where do the arrows of d meet, and which point on your graph is that?</li>
    <li>Why are the arrows of b parallel, and what does that say about its graph?</li></ul>
    <div class="rule" style="margin-top:2mm"></div><div class="rule"></div><div class="rule"></div><div class="rule"></div>
    <p style="margin:2mm 0 1mm"><b>Prove it:</b> show that m = 1 is the only case with no fixed value, unless c = 0.</p>
    <div class="rule"></div><div class="rule"></div></div>
</div>
<div class="done"><b>Done when:</b> every mapping diagram shows its arrows and a named transformation · Task 2 gives a rule for each
type of m, tested on an example of your own · Task 3 has both a diagram value and an algebraic value for each function · Task 4 gives an
algebraic answer, not only an example.</div>
<div class="card tint" style="margin-bottom:3mm"><h2 class="g">My Mawhiba record</h2>
  <p class="footnote">Keep this with your cumulative record. Tick the value you showed today and write one example.</p>
  <div class="val"><span>&#9744; Inquiry</span><span>&#9744; Risk taking</span><span>&#9744; Creativity</span>
  <span>&#9744; Perseverance</span><span>&#9744; Collaboration</span><span>&#9744; Concern for society</span></div>
  <div class="rule" style="margin-top:1.4mm"></div><div class="rule"></div></div>
{foot("Week 6 · Mawhiba Unit 2 Activity 1", 3, 3)}"""
    return [p1, p2, p3]

KEYROWS = [
 ("a", "Reflection in 0", "x = 0", "sa", "m &lt; 0"),
 ("b", "Translation by −4", "none — arrows parallel", "sb", "m = 1"),
 ("c", "Enlargement, scale factor ½, centre 0", "x = 0", "sc", "0 &lt; m &lt; 1"),
 ("d", "Enlargement, scale factor 3, centre 1", "x = 1", "sd", "m &gt; 1"),
 ("e", "Enlargement, scale factor 2, centre −1", "x = −1", "se", "m &gt; 1"),
 ("f", "Reflection in 1.5", "x = 1.5", "sf", "m &lt; 0"),
 ("g", "Enlargement, scale factor −½, centre 2", "x = 2", "sg", "m &lt; 0"),
 ("h", "Enlargement, scale factor ⅓, centre 1.5", "x = 1.5", "sh", "0 &lt; m &lt; 1"),
]

def key_pages():
    rows = "".join(
        f'<tr><td class="l" style="width:34mm">{eq("f"+k, 0.74, True)}</td><td style="width:50mm">{t}</td>'
        f'<td style="width:33mm">{fx}</td><td>{eq(s, 0.7, True)}</td></tr>' for k, t, fx, s, _ in KEYROWS)
    diag = "".join(f'<div style="border:1px solid var(--line);border-radius:1.5mm;padding:1mm 1.4mm">'
                   f'<div style="font-size:7.6pt">{eq("f"+k, 0.66, True)}</div><img src="fig/s_{k}.png" style="width:100%"></div>'
                   for k in "abcdefgh")
    k1 = f"""<style>{EXTRA}</style>{HEADER}
<div class="title"><h1><small>Teacher key · Mawhiba Unit 2 Activity 1 · Week 6</small>Mappings of Linear Functions</h1>
<div class="meta">Every value re-derived with exact fractions</div></div>
<div class="card" style="margin-bottom:2.2mm"><h2>Tasks 1 and 3 — answers</h2>
  <table class="cj"><tr><th>Function</th><th>Transformation</th><th>Value that maps to itself</th><th>Algebra, f(x) = x</th></tr>{rows}</table>
  <p class="footnote" style="margin-top:1.2mm"><b>Source note.</b> The printed Student Book drops the fractions in c, g and h. They are reconstructed from the
  Teacher’s Guide, which states scale factor, centre and fixed value for each; the sheet prints them as c(x) = x/2, g(x) = 3 − x/2, h(x) = x/3 + 1.
  The Guide’s own listing of vii as 2 − x and viii as x + 1 cannot give its stated centres 2 and 1.5, so those two are the ones to confirm against the book.</p>
</div>
<div class="card tint" style="margin-bottom:2.2mm"><h2 class="t">Model mapping diagrams (gold dots mark the value that maps onto itself)</h2>
<div class="grid g2" style="gap:1.8mm">{diag}</div></div>
{foot("Teacher key · Mawhiba Unit 2 Activity 1", 1, 2)}"""
    k2 = f"""<style>{EXTRA}</style>{HEADER}
<div class="grid g2" style="margin-bottom:2.2mm">
  <div class="card tint"><h2 class="p">Task 2 — what students should find</h2>
    <ul><li><b>m = 1:</b> translation by c (identity if c = 0). Arrows parallel.</li>
    <li><b>m = −1:</b> reflection in x = c/2.</li>
    <li><b>Other m:</b> enlargement, scale factor m, centre c/(1 − m); a negative m also turns the line over.</li>
    <li><b>Where the arrows meet</b> (domain line above, range line below), at height s = 1/(1 − m) measured from the domain line:
    for m &gt; 1 above the domain line (d, e); for 0 &lt; m &lt; 1 below the range line (c, h); for m &lt; 0 between the lines (a, f, g).</li>
    <li><b>c</b> never changes the type, only the position of the centre.</li></ul></div>
  <div class="card tint"><h2 class="t">Task 4 — the general result</h2>
    <p style="margin-bottom:1mm">{eq("fixeq", 0.7)}</p>
    <p class="footnote">If m = 1 and c ≠ 0 there is none: {eq("par", 0.62, True)}; with c = 0 every value maps to itself.
    On the grid, the fixed value is where y = mx + c crosses y = x.</p>
    <img src="fig/key_graph.png" style="width:62mm;display:block;margin:1.4mm auto 0"></div>
</div>
<div class="grid g2" style="margin-bottom:2.2mm">
  <div class="card tint"><h2 class="g">Misconceptions to name aloud</h2>
    <ul><li><b>“A negative m means a reflection.”</b> Only m = −1 is a pure reflection; m = −½ also shrinks it.</li>
    <li><b>“c is the centre.”</b> The centre is c/(1 − m); c is the centre only when m = 0.</li>
    <li><b>“Function b has a mistake.”</b> It has no fixed value and that is the point: x − 4 = x gives −4 = 0.</li>
    <li><b>“Only the arrows I drew matter.”</b> Extend the arrows: the meeting point is the same for every x.</li></ul></div>
  <div class="card tint"><h2 class="p">Assessment focus (from the Guide)</h2>
    <ul><li>Correct notation, accurate diagrams, geometrical features identified.</li>
    <li>Classify, generalise, and explain links between the algebra and the geometry.</li>
    <li>Task 4: link the fixed value to the Cartesian graph of the identity function.</li></ul></div>
</div>
<div class="card" style="margin-bottom:2.2mm"><h2>Suggested flow for one Mawhiba session</h2>
  <table class="cj"><tr><th style="width:24mm">Minutes</th><th>What happens</th></tr>
  <tr><td class="l">5</td><td>Check function notation and the words domain and range; model one diagram (the identity) on the board.</td></tr>
  <tr><td class="l">20</td><td>Task 1 in groups of three or four: each student draws two functions, then the group sorts the eight cards by transformation.</td></tr>
  <tr><td class="l">10</td><td>Task 2: groups state a rule for each value of m and test it on a new example; one group presents.</td></tr>
  <tr><td class="l">15</td><td>Tasks 3 and 4: fixed values by diagram and by algebra, then the general formula and the graph.</td></tr>
  <tr><td class="l">5</td><td>Plenary and the Mawhiba record: which value did each student show, with one example.</td></tr></table></div>
{foot("Teacher key · Mawhiba Unit 2 Activity 1", 2, 2)}"""
    return [k1, k2]

if __name__ == "__main__":
    a = render(worksheet(), "MAWHIBA_G9_U2_A1_Worksheet")
    b = render(key_pages(), "MAWHIBA_G9_U2_A1_Teacher_Key")
    if not (a and b): raise SystemExit("layout does not fit")
