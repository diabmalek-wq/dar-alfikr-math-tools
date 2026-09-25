"""MAWHIBA Grade 9 · Unit 1 (Linear Equations) · Activity 3 — Number Pyramids.

Compressed to 2 pages (worksheet) + 1 page (teacher key) per this round's
request — shorter than Activities 1-2's 3-page worksheets. Content and
numbers are the source book's own (Student Book + Teacher's Guide, Unit 1
Activity 3), independently re-derived and checked here:

  Task 1 (fig 6, worked demo): bottom 23, n, 17, 31 -> top 267 -> n = 54
  Task 2 (three more):
    i.   bottom 16, n, 5, 42  -> top 157        -> n = 28
    ii.  bottom 62, 14, n, 41 -> top 217        -> n = 24
    iii. bottom 24, 17, 2, n  -> top 119        -> n = 38
  Task 3: general formula t = a + 3b + 3c + d, and the rearrangement for
    each letter.
  Task 4 (top itself an expression in n):
    i.   bottom 3, n, 17, 5   -> top 10n + 3    -> n = 8
    ii.  bottom 26, 50, n, 31 -> top 417 - 2n   -> n = 42

All six re-verified by direct pyramid summation before use (see check() in
the build notes / session log) — every one closes exactly.

    python3 make_math_maw3.py && python3 build_mawhiba_a3.py
"""
import json
from build_mawhiba_a1 import CSS, HEADER, render

MATH = json.load(open("maw_math3/_index.json"))
SCALE = 0.80

PYR_CSS = """
  .pyr { display:flex; flex-direction:column; align-items:center; gap:1.4mm; margin:1.6mm 0; }
  .pyr .row { display:flex; gap:1.4mm; }
  .pyr .brick { width:13mm; height:9mm; border:1px solid var(--line); border-radius:1mm;
                display:flex; align-items:center; justify-content:center; font-size:7.6pt;
                background:#fff; text-align:center; padding:0 .6mm; }
  .pyr .brick.blank { background:var(--tint2); border-style:dashed; color:var(--grey); }
  .pyr .brick.given { font-weight:bold; color:var(--navy); }
  .pyr .brick.unk { font-weight:bold; color:var(--plum); border-color:var(--plum); }
  .pyr .brick.top { width:22mm; font-size:8pt; }
"""


def eq(key, scale=SCALE, inline=False):
    assert key in MATH, key
    h = round(MATH[key]["hin"] * 25.4 * scale, 2)
    return (f'<img class="{"inl" if inline else "eq"}" src="maw_math3/{key}.png" '
            f'style="max-height:{h}mm">')


def brick(text, cls="given"):
    return f'<div class="brick {cls}">{text}</div>'


def pyramid(bottom, top, blank_middle=True, top_cls="given"):
    """bottom: list of 4 cell strings (use 'n' for the unknown). top: the top
    cell's text. blank_middle=True leaves rows 2-3 as working space."""
    a, b, c, d = bottom
    rows = [f'<div class="row">{brick(top, top_cls + " top")}</div>']
    if blank_middle:
        rows.append(f'<div class="row">{brick("", "blank")}{brick("", "blank")}</div>')
        rows.append(f'<div class="row">{brick("", "blank")}{brick("", "blank")}{brick("", "blank")}</div>')
    def cell(v):
        return brick(v, "unk" if v == "n" else "given")
    rows.append(f'<div class="row">{cell(a)}{cell(b)}{cell(c)}{cell(d)}</div>')
    return f'<div class="pyr">{"".join(rows)}</div>'


def foot(left, page, of):
    return (f'<footer><span>{left}</span>'
            f'<span class="motto">Faith, Righteousness and Wisdom</span>'
            f'<span>Mr Malek Thiab · Page {page} of {of}</span></footer>')


TITLE = ('<div class="title">'
         '<h1><small>Mawhiba Grade 9 · Unit 1 Linear Equations · Activity 3</small>'
         'Number Pyramids</h1>'
         '<div class="meta">Advanced Supplementary Mathematics<br>'
         'Mawhiba Schools Partnership</div></div>')

IDBAR = ('<div class="idbar"><div><b>Student</b> ..............................................</div>'
         '<div><b>Class</b> ....................</div>'
         '<div><b>Date</b> ......... / ......... / 2026</div>'
         '<div><b>Teacher</b> Mr Malek Thiab</div></div>')


def worksheet():
    p1 = f"""<style>{PYR_CSS}</style>{HEADER}{TITLE}{IDBAR}

<div class="grid g2" style="margin-bottom:2.2mm">
  <div class="card tint"><h2 class="p">What this activity is for</h2>
    <ul><li>Turn a number puzzle into an algebraic equation.</li>
    <li>Solve an equation where the unknown appears more than once.</li>
    <li>Generalise a method into a formula that works for every case.</li></ul></div>
  <div class="card tint"><h2 class="t">How you will be judged</h2>
    <ul><li><b>Formulating</b> — building the equation from the pyramid rule, not guessing.</li>
    <li><b>Accuracy</b> — solving it correctly and checking it back in the pyramid.</li>
    <li><b>Generalising</b> — Task 3 asks for a rule that works for ANY pyramid like this.</li></ul></div>
</div>

<div class="card" style="margin-bottom:2.2mm">
  <h2>The rule</h2>
  <p>In a number pyramid, the number in each brick is the <b>sum of the two numbers
  beneath it</b>. Below is a 4-layer pyramid with the top number and three of the four
  bottom numbers given.</p>
</div>

<div class="grid g2w" style="margin-bottom:2.2mm">
  <div class="card">
    <h2 class="g">Task 1 · Find the missing number</h2>
    <p style="margin-bottom:1.2mm"><b>1 &middot; Form an equation for n</b>, using the working
    bricks to build up from the bottom row.</p>
    <div class="rule"></div><div class="rule"></div>
    <p style="margin:1.6mm 0 1mm"><b>2 &middot; Solve it, then check</b> your value of n by
    putting it back into the original pyramid.</p>
    <div class="box" style="height:15mm"></div>
  </div>
  <div class="card tint" style="text-align:center">
    <h2 class="p">fig 6</h2>
    {pyramid(["23", "n", "17", "31"], "267")}
    <p class="footnote">bottom row given except n &middot; top = 267</p>
  </div>
</div>

<div class="card">
  <h2 class="t">Task 2 · Three more 4-layer pyramids</h2>
  <p style="margin-bottom:1.6mm">For each pyramid, form an equation for n, solve it, and check
  your answer back in the pyramid. Use the working space under each one.</p>
  <div class="grid g3">
    <div style="text-align:center">
      <p class="footnote"><b>i.</b></p>
      {pyramid(["16", "n", "5", "42"], "157")}
      <div class="box" style="height:16mm;margin-top:1mm"></div>
    </div>
    <div style="text-align:center">
      <p class="footnote"><b>ii.</b></p>
      {pyramid(["62", "14", "n", "41"], "217")}
      <div class="box" style="height:16mm;margin-top:1mm"></div>
    </div>
    <div style="text-align:center">
      <p class="footnote"><b>iii.</b></p>
      {pyramid(["24", "17", "2", "n"], "119")}
      <div class="box" style="height:16mm;margin-top:1mm"></div>
    </div>
  </div>
</div>
{foot("Mawhiba · Unit 1 · Activity 3 · Number Pyramids", 1, 2)}"""

    p2 = f"""<style>{PYR_CSS}</style>{HEADER}
<div class="title"><h1><small>Activity 3 continued</small>A formula for any pyramid</h1>
  <div class="meta">Task 4 is the Investigate route<br>Work with a partner from here</div></div>

<div class="card" style="margin-bottom:2.2mm">
  <h2 class="p">Task 3 · Find the general formula</h2>
  <div class="grid g2w">
    <div>
      <p style="margin-bottom:1.4mm"><b>3 &middot; Can you find a formula that solves ANY
      4-layer pyramid like these?</b> Let the top number be <i>t</i>, and the four bottom
      numbers be <i>a</i>, <i>b</i>, <i>c</i> and <i>d</i>. Build up the pyramid in letters, the
      same way you built up Tasks 1 and 2 in numbers.</p>
      <div class="box" style="height:26mm;margin-bottom:1.8mm"></div>
      <p style="margin-bottom:1mm"><b>4 &middot; Your formula for t, in terms of a, b, c, d:</b></p>
      <div class="rule"></div>
      <p style="margin:1.6mm 0 1mm"><b>5 &middot; Rearrange it</b> to give a formula for
      whichever letter is missing — for example, if b is the unknown:</p>
      <div class="rule"></div>
      <p class="footnote" style="margin-top:1mm"><b>6 &middot; Check</b> your formula by
      substituting the numbers from Task 1 or Task 2.</p>
    </div>
    <div class="card tint" style="text-align:center;padding:2.2mm">
      {pyramid(["a", "b", "c", "d"], "t", top_cls="unk")}
      <p class="footnote" style="margin-top:1mm">Label each blank brick in letters as you go —
      the pattern is the same rule you used with numbers.</p>
    </div>
  </div>
</div>

<div class="card" style="margin-bottom:2.2mm">
  <h2 class="g">Task 4 · When the top is an expression too</h2>
  <p style="margin-bottom:1.6mm">In these two pyramids the top number is not given directly —
  it is written in terms of n as well. Form the equation, solve for n, and state the actual top
  number.</p>
  <div class="grid g2">
    <div style="text-align:center">
      <p class="footnote"><b>i.</b></p>
      {pyramid(["3", "n", "17", "5"], eq("m3_top1", 0.62, inline=True), top_cls="unk")}
      <div class="box" style="height:18mm;margin-top:1mm"></div>
    </div>
    <div style="text-align:center">
      <p class="footnote"><b>ii.</b></p>
      {pyramid(["26", "50", "n", "31"], eq("m3_top2", 0.62, inline=True), top_cls="unk")}
      <div class="box" style="height:18mm;margin-top:1mm"></div>
    </div>
  </div>
</div>

<div class="grid g3" style="margin-bottom:2.2mm">
  <div class="card"><h2 class="t">Practice — secure the method</h2>
    <p>Tasks 1 and 2. Form the equation, solve it, and check your value of n back in the
    pyramid.</p></div>
  <div class="card"><h2 class="t">Apply — use it in context</h2>
    <p>Task 4. The top is itself an expression in n — the unknown appears on both sides of
    your equation.</p></div>
  <div class="card"><h2 class="t">Investigate — find out why</h2>
    <p>Task 3. Generalise the method into a formula, then rearrange it for any missing
    letter.</p></div>
</div>

<div class="done"><b>Done when&hellip;</b> you can turn a number pyramid into an equation, solve
it even when the unknown appears more than once, and state the general formula
{eq("m3_formula_w", 0.66, inline=True)} for any 4-layer pyramid.</div>
{foot("Mawhiba · Unit 1 · Activity 3 · Number Pyramids", 2, 2)}"""
    return [p1, p2]


def key_page():
    return f"""<style>{PYR_CSS}</style>{HEADER}
<div class="title"><h1><small>Teacher Key &middot; Mawhiba Grade 9 &middot; Unit 1 &middot; Activity 3</small>
Number Pyramids</h1>
  <div class="meta">Every equation re-derived and checked<br>Not for student issue</div></div>

<div class="card" style="margin-bottom:2mm">
  <h2>Task 1 &middot; fig 6 &mdash; n = 54</h2>
  <p style="margin-bottom:1mm">Building up from the bottom row (23, n, 17, 31): row 3 is
  23 + n, n + 17, 48; row 2 is 40 + 2n, n + 65; the top is their sum.</p>
  <div style="margin-bottom:1mm">{eq("m3_t1eq", 0.68)}</div>
  <p class="say">Check: with n = 54, the pyramid reads 23, 54, 17, 31 &rarr; 77, 71, 48 &rarr;
  148, 119 &rarr; 267. &#10003;</p>
</div>

<div class="card" style="margin-bottom:2mm">
  <h2 class="t">Task 2 &middot; the three pyramids</h2>
  <div class="grid g3">
    <div><p><b>i &middot; n = 28</b></p><div style="margin:1mm 0">{eq("m3_t2i", 0.62)}</div></div>
    <div><p><b>ii &middot; n = 24</b></p><div style="margin:1mm 0">{eq("m3_t2ii", 0.62)}</div></div>
    <div><p><b>iii &middot; n = 38</b></p><div style="margin:1mm 0">{eq("m3_t2iii", 0.62)}</div>
      <p class="say" style="margin-top:1mm">iii is the short one &mdash; c = 2 makes the 3c
      term small enough that the equation looks almost linear. Worth asking why.</p></div>
  </div>
</div>

<div class="card" style="margin-bottom:2mm">
  <h2 class="p">Task 3 &middot; the general formula</h2>
  <div class="grid g2w">
    <div>
      <p style="margin-bottom:1mm">Building the pyramid in letters: row 3 is a + b, b + c,
      c + d; row 2 is a + 2b + c, b + 2c + d; the top is their sum.</p>
      <div style="margin-bottom:1.4mm">{eq("m3_formula2", 0.72)}</div>
      <p>Rearranged for whichever letter is missing:</p>
      <div>{eq("m3_rearr", 0.68)}</div>
    </div>
    <div class="card tint" style="padding:2mm 2.4mm">
      <p><b>Where this checks itself.</b> Substituting fig 6's own numbers
      (a = 23, b = 54, c = 17, d = 31) into t = a + 3b + 3c + d gives
      23 + 162 + 51 + 31 = 267 &mdash; exactly the top of Task 1. That agreement IS the
      check the task asks for.</p>
    </div>
  </div>
</div>

<div class="card">
  <h2 class="g">Task 4 &middot; the unknown on both sides</h2>
  <div class="grid g2">
    <div><p><b>i &middot; n = 8, top = 83</b></p>
      <div style="margin:1mm 0">{eq("m3_t4i", 0.66)}</div></div>
    <div><p><b>ii &middot; n = 42, top = 333</b></p>
      <div style="margin:1mm 0">{eq("m3_t4ii", 0.66)}</div></div>
  </div>
  <p class="say" style="margin-top:1.4mm">The pyramid rule builds the LEFT side exactly as
  before; the only new step is that the top was already written as an expression, so the
  equation has n on both sides from the start. Students who try trial-and-improvement here
  will feel the method break down &mdash; that discomfort is the point of Task 4.</p>
</div>
{foot("Teacher Key · Activity 3", 1, 1)}"""


if __name__ == "__main__":
    a = render(worksheet(), "MAWHIBA_G9_U1_A3_Worksheet")
    # The key is a compact one-page teacher reference, not a content page the
    # 0.78-0.94 fill gate was designed for -- same accepted exception as the
    # Activity 1/2 keys and the AP Precalculus compact answer key.
    render([key_page()], "MAWHIBA_G9_U1_A3_Teacher_Key")
    if not a:
        raise SystemExit("worksheet layout does not fit")
