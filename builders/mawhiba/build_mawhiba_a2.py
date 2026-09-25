"""MAWHIBA Grade 9 · Unit 1 (Linear Equations) · Activity 2 — redesigned.

WHAT WAS WRONG WITH THE SOURCE SHEET

  * Two pages of which most was blank. No working space was SIZED to its task:
    task 1 asks for three different dissections and gave one gap; task 3 asks a
    pair to invent and swap a problem and gave half a page of nothing.
  * The figures carried ambiguous labelling. Figure 4 in particular showed
    2, 6, r, q, p and 10 with no statement of which measured what, so two
    students could read two different shapes out of it and both be right.
  * The mathematical point — that several dissections of one rectangle must
    simplify to the SAME expression, and that this is what an identity is —
    was never said out loud. It was left to be inferred from "verify that this
    is the case".
  * No objectives, no assessment criteria, no routes, no "Done when", and no
    teacher key.

WHAT THIS BUILD IS

    Worksheet   2 pages, student-facing, nothing pre-answered
    Key         1 page, teacher-facing, separate file, every route worked

The five tasks are the source's own and are unchanged in substance: the four
area figures, the invent-your-own, the (a + b)(c + d) diagram with 27 x 38,
and the a^2 - b^2 shape. Only the layout, the labelling, the working space and
the ordering are new.

    python3 make_math_maw2.py && python3 make_figs_maw2.py && python3 build_mawhiba_a2.py
"""
import json
from build_mawhiba_a1 import CSS, HEADER, render

MATH = json.load(open("maw_math/_index.json"))
FIGS = json.load(open("figs_maw2/_index.json"))
SCALE = 0.80


def eq(key, scale=SCALE, inline=False):
    assert key in MATH, key
    h = round(MATH[key]["hin"] * 25.4 * scale, 2)
    return (f'<img class="{"inl" if inline else "eq"}" src="maw_math/{key}.png" '
            f'style="max-height:{h}mm">')


def fg(key, width_mm):
    """A figure is sized by its WIDTH: the shapes differ in proportion, and
    matching their heights would make the wide ones unreadably small."""
    assert key in FIGS, key
    return (f'<img src="figs_maw2/{key}.png" '
            f'style="width:{width_mm}mm;display:block;margin:0 auto">')


def foot(left, page, of):
    return (f'<footer><span>{left}</span>'
            f'<span class="motto">Faith, Righteousness and Wisdom</span>'
            f'<span>Mr Malek Thiab · Page {page} of {of}</span></footer>')


TITLE = ('<div class="title">'
         '<h1><small>Mawhiba Grade 9 · Unit 1 Linear Equations · Activity 2</small>'
         'Rectangular Areas</h1>'
         '<div class="meta">Advanced Supplementary Mathematics<br>'
         'Mawhiba Schools Partnership</div></div>')

IDBAR = ('<div class="idbar"><div><b>Student</b> ..............................................</div>'
         '<div><b>Class</b> ....................</div>'
         '<div><b>Date</b> ......... / ......... / 2026</div>'
         '<div><b>Teacher</b> Mr Malek Thiab</div></div>')


def worksheet():
    p1 = f"""{HEADER}{TITLE}{IDBAR}

<div class="grid g2" style="margin-bottom:2.4mm">
  <div class="card tint"><h2 class="p">What this activity is for</h2>
    <ul><li>Construct algebraic expressions for an area by dissecting a shape in more than one way.</li>
    <li>Show that different expressions for the same area are equivalent by simplifying them.</li>
    <li>Use area to explain why an algebraic identity is true.</li></ul></div>
  <div class="card tint"><h2 class="t">How you will be judged</h2>
    <ul><li><b>Flexibility</b> — how many genuinely different dissections you find, not how fast.</li>
    <li><b>Justification</b> — simplifying to show equivalence, rather than asserting it.</li>
    <li><b>Communication</b> — a labelled diagram that another pair can follow without you.</li></ul></div>
</div>

<div class="card" style="margin-bottom:2.4mm">
  <h2>Task 1 · One area, several expressions</h2>
  <div class="grid g2w">
    <div>
      <p style="margin-bottom:1.6mm">The shaded rectangle sits inside the larger one.
      <b>Find an expression for the UNSHADED area — in as many different ways as you can.</b>
      A different way means a different <i>cut</i>, not the same cut rearranged.</p>
      <p style="margin-bottom:1.4mm"><b>1 · Describe each way in words first.</b></p>
      <div class="rule"></div><div class="rule"></div>
      <p style="margin:1.6mm 0 1.2mm"><b>2 · Now write the expression for each way.</b></p>
      <div class="box" style="height:17mm"></div>
    </div>
    <div>
      {fg("m2_f1", 54)}
      <p class="footnote" style="text-align:center;margin-top:.8mm">fig 1</p>
      <div class="card tint" style="margin-top:2mm;padding:2mm 2.4mm">
        <p style="margin-bottom:1.2mm"><b>One way, to start you off.</b> Take the whole
        rectangle and remove the shaded piece:</p>
        <div class="big" style="margin:1.2mm 0">{eq("n2_whole", 0.92)}</div>
        <p class="say">Two more ways are waiting in this figure.</p>
      </div>
    </div>
  </div>
  <p style="margin:2mm 0 1.2mm"><b>3 · They must agree.</b> Every expression measures the same
  area, so simplifying them must give one and the same expression. Show that it does.</p>
  <div class="box" style="height:13mm"></div>
</div>

<div class="card">
  <h2 class="t">Task 2 · Three more</h2>
  <p style="margin-bottom:1.6mm">For each figure, find expressions for the <b>unshaded</b> area in
  as many ways as you can, then simplify them to show they agree.</p>
  <div class="grid g3">
    <div>
      {fg("m2_f2", 38)}
      <p class="footnote" style="text-align:center;margin:.6mm 0 1.4mm"><b>i.</b> fig 2</p>
      <div class="box" style="height:21mm"></div>
    </div>
    <div>
      {fg("m2_f3", 50)}
      <p class="footnote" style="text-align:center;margin:.6mm 0 1.4mm"><b>ii.</b> fig 3</p>
      <div class="box" style="height:21mm"></div>
    </div>
    <div>
      {fg("m2_f4", 42)}
      <p class="footnote" style="text-align:center;margin:.6mm 0 1.4mm"><b>iii.</b> fig 4</p>
      <div class="box" style="height:21mm"></div>
    </div>
  </div>
  <p class="footnote" style="margin-top:1.4mm">In <b>fig 4</b> the edges give two equations
  connecting <i>p</i>, <i>q</i> and <i>r</i>. Write them down before you start.</p>
</div>
{foot("Mawhiba · Unit 1 · Activity 2 · Rectangular Areas", 1, 3)}"""

    p2 = f"""{HEADER}
<div class="title"><h1><small>Activity 2 continued</small>From area to identity</h1>
  <div class="meta">Work with a partner from Task 3 onwards</div></div>

<div class="card" style="margin-bottom:2.4mm">
  <h2 class="g">Task 3 · Write one of your own</h2>
  <div class="grid g2">
    <div>
      <p style="margin-bottom:1.4mm"><b>Draw your problem here.</b> Mark every length. Use at
      least one letter, and make sure the figure alone tells the reader what is shaded.</p>
      <div class="box" style="height:79mm"></div>
    </div>
    <div>
      <p style="margin-bottom:1.4mm"><b>Your own answer</b> — keep it covered while another pair
      solves it, then compare.</p>
      <div class="box" style="height:40mm;margin-bottom:2mm"></div>
      <p style="margin-bottom:1.2mm"><b>After the swap.</b> Did the other pair cut your shape the
      same way you did?</p>
      <div class="rule"></div><div class="rule"></div>
    </div>
  </div>
</div>

<div class="card">
  <h2>Task 4 · The identity behind long multiplication</h2>
  <div class="grid g2w">
    <div>
      <p style="margin-bottom:1.2mm"><b>4 · Draw a rectangle that shows this identity.</b>
      One side is split into <i>a</i> and <i>b</i>; the other into <i>c</i> and <i>d</i>.</p>
      <div class="big" style="margin:1.2mm 0 1.8mm">{eq("n2_id", 0.86)}</div>
      <div class="box" style="height:62mm"></div>
    </div>
    <div>
      <p style="margin-bottom:1.2mm"><b>5 · Now use it on a number.</b> Any two-digit product is
      this identity in disguise:</p>
      <div class="big" style="margin:1.2mm 0">{eq("n2_2738", 0.82)}</div>
      <p style="margin-bottom:1.4mm">Write the four products your rectangle gives, add them, and
      check against the multiplication you already know.</p>
      <div class="box" style="height:40mm"></div>
    </div>
  </div>
</div>
{foot("Mawhiba · Unit 1 · Activity 2 · Rectangular Areas", 2, 3)}"""

    p3 = f"""{HEADER}
<div class="title"><h1><small>Activity 2 continued</small>The shape that proves a factorisation</h1>
  <div class="meta">Task 5 is the Investigate route<br>Work with your partner</div></div>

<div class="card" style="margin-bottom:2.6mm">
  <h2 class="t">Task 5 · Two expressions for one shape</h2>
  <div class="grid g2w">
    <div>
      <p style="margin-bottom:1.4mm"><b>6 · Find the shaded area in more than one way.</b>
      One way removes a square from a square. Another cuts the shape into two rectangles —
      and that one does not need {eq("n2_diff", 0.62, inline=True)} at all.</p>
      <div class="box" style="height:27mm;margin-bottom:1.8mm"></div>
      <p style="margin-bottom:1.4mm"><b>7 · Say what you have proved.</b> Simplify your two
      expressions and write the identity they give.</p>
      <div class="rule"></div><div class="rule"></div>
    </div>
    <div>
      {fg("m2_f5", 52)}
      <p class="footnote" style="text-align:center;margin-top:.6mm">fig 5 · the dashed square is
      the piece that was removed</p>
    </div>
  </div>
</div>

<div class="card tint" style="margin-bottom:2.4mm">
  <h2 class="p">Task 5 continued · show it with scissors, not algebra</h2>
  <p style="margin-bottom:1.4mm">Cut the shape into two rectangles and lay them side by side.
  The area cannot change, so whatever the new rectangle measures must equal the old area — and
  that is a proof a reader can see rather than follow.</p>
  {fg("m2_f6", 132)}
  <p style="margin-top:1.6mm;margin-bottom:1.4mm"><b>8 · Write the new rectangle's two sides,
  and then the identity they give.</b></p>
  <div class="box" style="height:19mm;background:#fff"></div>
</div>

<div class="grid g3" style="margin-bottom:2.4mm">
  <div class="card"><h2 class="t">Practice — secure the method</h2>
    <p>Tasks 1 and 2. For each figure find at least two different cuts and show they simplify
    to the same expression.</p></div>
  <div class="card"><h2 class="t">Apply — use it in context</h2>
    <p>Tasks 3 and 4. Invent a figure another pair can solve, then use the identity on
    27 &times; 38 without writing the usual column method.</p></div>
  <div class="card"><h2 class="t">Investigate — find out why</h2>
    <p>Task 5. Explain why cutting the shape proves the factorisation, and say what the proof
    needs <i>a</i> to be bigger than.</p></div>
</div>

<div class="done"><b>Done when…</b> you can write two different expressions for the same area,
simplify both to one expression, and use a cut-up rectangle to explain why
{eq("n2_factor_w", 0.62, inline=True)} is true for every <i>a</i> and <i>b</i>.</div>
{foot("Mawhiba · Unit 1 · Activity 2 · Rectangular Areas", 3, 3)}"""
    return [p1, p2, p3]


def key_page():
    return f"""{HEADER}
<div class="title"><h1><small>Teacher Key · Mawhiba Grade 9 · Unit 1 · Activity 2</small>
Rectangular Areas</h1>
  <div class="meta">Every route re-derived and checked<br>Not for student issue</div></div>

<div class="card" style="margin-bottom:2.2mm">
  <h2>Task 1 · fig 1 — the unshaded area is 84 &minus; 3<i>x</i></h2>
  <div class="grid g2">
    <div>
      <p style="margin-bottom:1mm"><b>Whole minus part.</b></p>
      <div style="margin-bottom:1.6mm">{eq("k2_f1a", 0.74)}</div>
      <p style="margin-bottom:1mm"><b>Two horizontal strips</b> — the full band below the shaded
      row, plus what is left of the shaded row.</p>
      <div>{eq("k2_f1b", 0.74)}</div>
    </div>
    <div>
      <p style="margin-bottom:1mm"><b>Two vertical strips</b> — the column under the shaded piece,
      plus the full-height column beside it.</p>
      <div style="margin-bottom:1.6mm">{eq("k2_f1c", 0.74)}</div>
      <p class="say">All three land on 84 &minus; 3<i>x</i>. That agreement is the teaching point:
      the expressions look different because the CUTS were different, not because anyone is wrong.
      Ask which cut they would choose if <i>x</i> were 11, and why.</p>
    </div>
  </div>
</div>

<div class="card" style="margin-bottom:2.2mm">
  <h2 class="t">Task 2 · the three figures</h2>
  <div class="grid g3">
    <div><p><b>i · fig 2 &nbsp;&rarr;&nbsp; 64 &minus; 2<i>p</i></b></p>
      <div style="margin:1.2mm 0">{eq("k2_f2a", 0.70)}</div>
      <div>{eq("k2_f2b", 0.70)}</div></div>
    <div><p><b>ii · fig 3 &nbsp;&rarr;&nbsp; 12<i>m</i> &minus; 7</b></p>
      <div style="margin:1.2mm 0">{eq("k2_f3a", 0.70)}</div>
      <div>{eq("k2_f3b", 0.70)}</div>
      <p class="say" style="margin-top:1.2mm">The strip is 12 &minus; 3 &minus; 2 = 7 wide. Most
      errors here are reading the 3 and the 2 as the strip's own length.</p></div>
    <div><p><b>iii · fig 4 &nbsp;&rarr;&nbsp; 10<i>p</i> &minus; 12</b></p>
      <div style="margin:1.2mm 0">{eq("k2_f4a", 0.70)}</div>
      <div>{eq("k2_f4b", 0.66)}</div>
      <p class="say" style="margin-top:1.2mm">The two relations along the edges are
      <i>p</i> = 2 + 6 + <i>r</i> and 10 = 2 + 2 + <i>q</i>, so <i>q</i> is just 6.</p></div>
  </div>
</div>

<div class="card" style="margin-bottom:2.2mm">
  <h2 class="t">Task 3 · what to expect when they invent one</h2>
  <div class="grid g3">
    <div><p><b>The commonest shape</b> is a copy of fig 1 with new numbers. Accept it, then ask
      for one where the shaded piece touches no corner — that is fig 4, and it is harder to
      write than to draw.</p></div>
    <div><p><b>The commonest fault</b> is a figure whose letters are not pinned to edges, so the
      solver cannot tell what is measured. Send it back to the author rather than fixing it:
      the fault is the lesson.</p></div>
    <div><p><b>Worth collecting</b> — any pair whose shaded piece is allowed to be as wide as the
      whole rectangle. Their expression still works, and that is the moment to ask what values of
      the letter make the figure impossible.</p></div>
  </div>
</div>

<div class="card" style="margin-bottom:2.2mm">
  <h2 class="g">Task 4 · the identity and 27 &times; 38</h2>
  <div class="grid g2w">
    <div><p>The rectangle has sides <i>a</i> + <i>b</i> and <i>c</i> + <i>d</i>, and the two cuts
      make four smaller rectangles of areas <i>ac</i>, <i>ad</i>, <i>bc</i> and <i>bd</i>. Adding
      them is the identity; there is nothing else to prove.</p>
      <p style="margin-top:1.4mm"><b>27 &times; 38</b> splits as 20 + 7 and 30 + 8:</p>
      <div style="margin-top:1.2mm">{eq("n2_2738b", 0.78)}</div></div>
    <div class="card tint" style="padding:2mm 2.4mm">
      <p><b>Where to push.</b> Ask them to find the four products inside the column method they
      already use. 600 and 56 are easy to spot; 160 and 210 are the two that get merged into one
      line, which is exactly why the column method feels like a rule rather than a reason.</p></div>
  </div>
</div>

<div class="card">
  <h2 class="p">Task 5 · a<sup>2</sup> &minus; b<sup>2</sup></h2>
  <div class="grid g2">
    <div>
      <p style="margin-bottom:1mm"><b>Cut into two rectangles:</b> one <i>a</i> by
      (<i>a</i> &minus; <i>b</i>), one <i>b</i> by (<i>a</i> &minus; <i>b</i>).</p>
      <div style="margin-bottom:1.6mm">{eq("k2_f5a", 0.74)}</div>
      <p style="margin-bottom:1mm"><b>Expanding confirms it:</b></p>
      <div>{eq("k2_f5b", 0.74)}</div>
    </div>
    <div class="card tint" style="padding:2mm 2.4mm">
      <p><b>The answer to watch for.</b> A pair who write <i>a</i><sup>2</sup> &minus;
      <i>b</i><sup>2</sup> and stop have not done the task — the point is the SECOND expression,
      the one with no squares in it.</p>
      <p style="margin-top:1.4mm"><b>The question worth asking at the end.</b> The picture needs
      <i>a</i> &gt; <i>b</i>, or there is no shape to cut. The identity does not. Ask whether a
      proof that only works for some numbers is still a proof — and what it would take to close
      the gap. That is the Investigate route, and it is where the strongest pairs should end up.</p>
    </div>
  </div>
</div>
{foot("Teacher Key · Activity 2", 1, 1)}"""


if __name__ == "__main__":
    a = render(worksheet(), "MAWHIBA_G9_U1_A2_Worksheet")
    b = render([key_page()], "MAWHIBA_G9_U1_A2_Teacher_Key")
    if not (a and b):
        raise SystemExit("layout does not fit")
