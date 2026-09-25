"""MAWHIBA Grade 9 · Unit 1 (Linear Equations) · Activity 1 — redesigned.

The source ran to four pages and printed the ANSWERS in the student's own
justification column, so the classification task gave itself away. This build is:

    Worksheet   2 pages, student-facing, nothing pre-answered
    Key         1 page, teacher-facing, separate file

Objectives, cognitive attributes and the three tasks are the source's own; only
the layout, the working space and the ordering are new. Branding follows the
current house rule (department logo, Cognia badge, school logo, motto footer).

    python3 make_math_maw1.py && python3 build_mawhiba_a1.py
"""
import json, os, subprocess, pathlib
import numpy as np
from PIL import Image

IDX = json.load(open("maw_math/_index.json"))
OUT = pathlib.Path(".").resolve()
SCALE = 0.80                       # one type size across the sheet

CSS = """
  @page { size: A4; margin: 0; }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  :root{ --navy:#1F3864; --teal:#17A199; --ink:#222E2D; --gold:#F0B323;
         --grey:#6B7674; --tint:#EDF5F4; --tint2:#F7FAFA; --line:#C9DEDC;
         --plum:#6B3FA0; --red:#C62828; }
  body { font-family:"DejaVu Sans",sans-serif; color:var(--ink); font-size:8.3pt; line-height:1.3; }
  .page { width:210mm; height:297mm; padding:8mm 9mm 13mm; position:relative;
          page-break-after:always; overflow:hidden; }
  .page:last-child { page-break-after:auto; }
  header { display:flex; align-items:center; justify-content:space-between;
           border-bottom:2px solid var(--teal); padding-bottom:2.2mm; margin-bottom:2.6mm; }
  header img { height:10.5mm; }
  header img.cognia { height:14mm; }
  .title { display:flex; align-items:flex-end; justify-content:space-between; margin-bottom:2.4mm; }
  .title h1 { font-size:15pt; color:var(--navy); line-height:1.1; }
  .title h1 small { display:block; font-size:8pt; color:var(--plum); font-weight:600;
                    letter-spacing:.07em; text-transform:uppercase; margin-bottom:1mm; }
  .title .meta { text-align:right; font-size:7.4pt; color:var(--grey); }
  .idbar { display:flex; gap:3mm; font-size:8pt; margin-bottom:2.6mm; }
  .idbar div { flex:1; border-bottom:1px solid var(--line); padding-bottom:1.4mm; }
  .idbar b { color:var(--navy); }
  .grid { display:grid; gap:2.6mm; }
  .g2 { grid-template-columns:1fr 1fr; }
  .g2w { grid-template-columns:1.18fr 0.82fr; }
  .g3 { grid-template-columns:1fr 1fr 1fr; }
  .card { border:1px solid var(--line); border-radius:2mm; padding:2.3mm 2.7mm 2.5mm;
          background:#fff; break-inside:avoid; }
  .card.tint { background:var(--tint2); }
  .card h2 { font-size:8.4pt; color:#fff; background:var(--navy); display:inline-block;
             padding:.9mm 2.2mm; border-radius:1mm; letter-spacing:.05em;
             text-transform:uppercase; margin-bottom:1.8mm; }
  .card h2.t { background:var(--teal); }
  .card h2.p { background:var(--plum); }
  .card h2.g { background:var(--gold); color:#4A3400; }
  ul { list-style:none; }
  li { margin-bottom:1.2mm; padding-left:3.6mm; position:relative; }
  li::before { content:"\\25B8"; position:absolute; left:0; color:var(--teal); }
  li:last-child { margin-bottom:0; }
  ol.num { list-style:none; counter-reset:n; }
  ol.num li { counter-increment:n; padding-left:5mm; }
  ol.num li::before { content:counter(n); color:#fff; background:var(--plum); border-radius:50%;
                      width:3.7mm; height:3.7mm; font-size:6.8pt; display:flex;
                      align-items:center; justify-content:center; top:.4mm; }
  b, strong { color:var(--navy); }
  .say { color:var(--grey); font-style:italic; }
  img.eq { display:block; max-width:100%; }
  img.inl { display:inline-block; vertical-align:middle; margin:0 .6mm; }
  .big { text-align:center; margin:2mm 0 2.4mm; }
  .big img { display:inline-block; }
  .rule { border-bottom:1px dotted #9AA6A5; height:5.8mm; }
  .box { border:1px dashed var(--line); border-radius:1.5mm; }
  table.st { width:100%; border-collapse:collapse; font-size:7.8pt; }
  table.st th { background:var(--tint); color:var(--navy); font-size:7.2pt; text-transform:uppercase;
                letter-spacing:.04em; padding:1.2mm 1mm; border:1px solid var(--line); }
  table.st td { border:1px solid var(--line); padding:1.1mm 1.4mm; vertical-align:middle; height:10.2mm; }
  table.st td.lab { width:6mm; text-align:center; font-weight:bold; color:var(--plum); }
  table.st td.stmt { width:27mm; }
  table.st td.cls { width:26mm; font-size:6.6pt; color:var(--grey); }
  table.st td.cls b { color:var(--ink); font-weight:normal; }
  .vals { display:flex; gap:1.6mm; flex-wrap:wrap; font-size:7.6pt; }
  .vals span { border:1px solid var(--line); border-radius:1mm; padding:.8mm 1.6mm; }
  .footnote { font-size:7.4pt; color:var(--grey); }
  .done { background:var(--navy); color:#fff; border-radius:2mm; padding:2.2mm 3mm;
          font-size:8.1pt; margin-bottom:8mm; }
  .done b { color:var(--gold); }
  footer { position:absolute; left:9mm; right:9mm; bottom:4.5mm; display:flex;
           align-items:center; justify-content:space-between; font-size:6.8pt;
           color:var(--grey); border-top:1px solid var(--line); padding-top:1.6mm; }
  footer .motto { color:var(--navy); font-size:7.4pt; letter-spacing:.14em;
                  text-transform:uppercase; font-weight:bold; }
  footer span:first-child, footer span:last-child { width:60mm; }
  footer span:last-child { text-align:right; }
"""

HEADER = ('<header><img src="dept_logo.png" alt="">'
          '<img class="cognia" src="cognia_badge.png" alt="Cognia School of Distinction 2024">'
          '<img src="school_logo.png" alt=""></header>')


def eq(key, scale=SCALE, inline=False):
    """One type size across the sheet: every image is shown at the same fraction of
    its natural height. `inline` keeps an expression inside its sentence."""
    assert key in IDX, key
    h = round(IDX[key]["hin"] * 25.4 * scale, 2)
    cls = "inl" if inline else "eq"
    return f'<img class="{cls}" src="maw_math/{key}.png" style="max-height:{h}mm">'


def foot(left, page, of=2):
    return (f'<footer><span>{left}</span>'
            f'<span class="motto">Faith, Righteousness and Wisdom</span>'
            f'<span>Mr Malek Thiab · Page {page} of {of}</span></footer>')


STATEMENTS = list("ABCDEFGHIJKL")
CHOICE = ('<b>&#9744;</b> Always<br><b>&#9744;</b> Sometimes<br><b>&#9744;</b> Never')


def worksheet():
    rows = "".join(
        f'<tr><td class="lab">{L}</td><td class="stmt">{eq("s_"+L)}</td>'
        f'<td class="cls">{CHOICE}</td><td></td></tr>' for L in STATEMENTS)

    p1 = f"""{HEADER}
<div class="title">
  <h1><small>Mawhiba Grade 9 · Unit 1 Linear Equations · Activity 1</small>
  Sometimes, Always or Never True?</h1>
  <div class="meta">Advanced Supplementary Mathematics<br>Mawhiba Schools Partnership</div>
</div>
<div class="idbar"><div><b>Student</b> ..............................................</div>
  <div><b>Class</b> ....................</div>
  <div><b>Date</b> ......... / ......... / 2026</div>
  <div><b>Teacher</b> Mr Malek Thiab</div></div>

<div class="grid g2" style="margin-bottom:2.6mm">
  <div class="card tint"><h2 class="p">What this activity is for</h2>
    <ul><li>Construct linear algebraic expressions and equations in diverse contexts.</li>
    <li>Investigate and classify solution sets — always, sometimes or never true.</li>
    <li>Distinguish conditional equations, inconsistent statements and identities.</li></ul></div>
  <div class="card tint"><h2 class="t">How you will be judged</h2>
    <ul><li><b>Conceptual clarity</b> — telling an identity apart from an equality, and saying why.</li>
    <li><b>Creativity and flexibility</b> — the variety of the statements you invent yourself.</li>
    <li><b>Justification</b> — a proof or a counterexample, not an opinion.</li></ul></div>
</div>

<div class="card" style="margin-bottom:2.6mm">
  <h2>Task 1 · The sum and the product</h2>
  <p>Some pairs of numbers add to the same value that they multiply to. This statement claims
  that this always happens:</p>
  <div class="big">{eq("m_stmt", 1.5)}</div>
  <p style="margin-bottom:2mm"><b>Is it always true, sometimes true, or never true?</b> Do not
  answer yet — test it first, and let the testing decide.</p>
  <div class="grid g2">
    <div>
      <p style="margin-bottom:1.4mm"><b>1 · Test whole numbers.</b> Find a pair that works.</p>
      <div class="vals"><span>a = 2 &nbsp; b = ........</span><span>a = 0 &nbsp; b = ........</span>
        <span>a = 5 &nbsp; b = ........</span></div>
      <p style="margin:2.2mm 0 1.4mm"><b>2 · Now allow fractions.</b> Solve each one for b.</p>
      <div style="margin-bottom:1mm">{eq("m_a3")}</div>
      <div class="rule"></div><div class="rule"></div>
      <div style="margin:1.8mm 0 1mm">{eq("m_a4")}</div>
      <div class="rule"></div><div class="rule"></div>
    </div>
    <div>
      <p style="margin-bottom:1.4mm"><b>3 · Rearrange to get b on its own.</b> Collect the b
      terms, factorise, then divide.</p>
      <div class="box" style="height:27mm;margin-bottom:2mm"></div>
      <p style="margin-bottom:1.4mm"><b>4 · One value of a breaks it.</b> Substitute a = 1 and
      write what happens. What does that tell you about your formula?</p>
      <div class="box" style="height:20mm"></div>
    </div>
  </div>
  <p style="margin:2.4mm 0 1.4mm"><b>5 · Keep a record.</b> Every pair you test goes in the
  table — a pattern is easier to see in a column than in scattered working.</p>
  <table class="st" style="font-size:8pt">
    <tr><th style="width:20mm">a</th><th style="width:20mm">b</th>
        <th style="width:26mm">a + b</th><th style="width:26mm">ab</th>
        <th>Equal? What do you notice?</th></tr>
    <tr><td style="height:7.4mm"></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="height:7.4mm"></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="height:7.4mm"></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="height:7.4mm"></td><td></td><td></td><td></td><td></td></tr>
  </table>
  <p style="margin-top:2.2mm"><b>Your conclusion.</b> The statement is
  &nbsp;<b>&#9744;</b> always &nbsp;<b>&#9744;</b> sometimes &nbsp;<b>&#9744;</b> never
  &nbsp;true, because ...................................................................................
  ..............................................................................................................</p>
</div>

<div class="card tint">
  <h2 class="g">Before you turn over — the three words mean three different things</h2>
  <div class="grid g3">
    <div><b>Identity.</b> True for <b>every</b> permissible value. Write it with {eq("m_idsym", 0.62, inline=True)}
      rather than an equals sign.</div>
    <div><b>Conditional equation.</b> True only for particular values — those values are its
      solution set.</div>
    <div><b>Inconsistent statement.</b> True for <b>no</b> value at all: rearranging leaves a
      false numerical claim.</div>
  </div>
</div>
{foot("Mawhiba Grade 9 · Unit 1 · Activity 1", 1)}"""

    p2 = f"""{HEADER}
<div class="title">
  <h1><small>Task 2 and Task 3</small>Classify, then Create</h1>
  <div class="meta">Justify every classification —<br>a solution set, a condition or a counterexample</div>
</div>

<div class="grid g2w" style="margin-bottom:2.4mm">
  <div class="card" style="padding-bottom:2mm">
    <h2>Task 2 · Classify each statement</h2>
    <p style="margin-bottom:2mm">Tick one box, then justify it. If it is always true, rewrite it
    as an identity in the last column.</p>
    <table class="st">
      <tr><th></th><th>Statement</th><th>Always / Sometimes / Never</th>
          <th>Justification — solution set, condition or counterexample</th></tr>
      {rows}
    </table>
  </div>

  <div>
    <div class="card" style="margin-bottom:2.4mm">
      <h2 class="t">Task 3 · Write your own</h2>
      <p style="margin-bottom:1.8mm">Two of each, and make them different from anything above —
      use brackets, two variables or a power.</p>
      <p><b>Always true</b> — identities</p>
      <div class="rule"></div><div class="rule"></div>
      <p style="margin-top:1.6mm"><b>Sometimes true</b> — conditional</p>
      <div class="rule"></div><div class="rule"></div>
      <p style="margin-top:1.6mm"><b>Never true</b> — inconsistent</p>
      <div class="rule"></div><div class="rule"></div>
      <p style="margin-top:2mm"><b>Swap with a partner.</b> Classify each other's six, then write
      the one that was hardest to settle and why.</p>
      <div class="box" style="height:15mm"></div>
    </div>

    <div class="card tint">
      <h2 class="p">Investigate</h2>
      <ol class="num">
        <li style="margin-bottom:1.6mm">Prove that {eq("m_stmt", 0.6, inline=True)} has no solution when a = 1.
          Your proof must end in a statement that is plainly false.</li>
        <li style="margin-bottom:1.6mm">Classify {eq("m_ch2", 0.62, inline=True)} for real x, and justify it from
          a property of squares rather than by testing values.</li>
        <li>Write a statement in two variables that is always true whenever {eq("m_ch3", 0.62, inline=True)},
          and show why.</li>
      </ol>
      <div class="box" style="height:24mm;margin-top:1.8mm"></div>
    </div>
  </div>
</div>

<div class="card" style="margin-bottom:2.4mm">
  <h2 class="g">Tick what you can do now</h2>
  <div class="grid g3">
    <div><b>&#9744;</b> I can tell an identity from a conditional equation and say which is which
      on any of the twelve statements.</div>
    <div><b>&#9744;</b> I can justify a classification with a solution set or a counterexample,
      not with an opinion.</div>
    <div><b>&#9744;</b> I can write an original statement of each of the three kinds.</div>
  </div>
  <p style="margin-top:2mm"><b>The one thing I want to ask about:</b>
    ....................................................................................................................
    ....................................................................................................................</p>
</div>

<div class="done"><b>Done when…</b> every statement carries a tick and a reason, your own six are
written and swapped, and at least one of the three investigations is finished with a proof rather
than an example.</div>
{foot("Mawhiba · Unit 1 Activity 1 · Linear Equations", 2)}"""

    return p1, p2


def key_page():
    def row(L, cls, why):
        return (f'<tr><td class="lab">{L}</td><td class="stmt">{eq("s_"+L)}</td>'
                f'<td style="width:26mm;color:var(--navy);font-weight:bold">{cls}</td>'
                f'<td>{why}</td></tr>')
    rows = "".join([
        row("A", "Sometimes", "true only when a = 13 — a conditional equation."),
        row("B", "<span style='color:#C62828'>Never</span>",
            f'subtracting m leaves {eq("k_B", 0.62, inline=True)}.'),
        row("C", "Always", f'commutative addition: {eq("k_C", 0.62, inline=True)}'),
        row("D", "Sometimes", eq("k_D", 0.62, inline=True)),
        row("E", "Sometimes", eq("k_E", 0.62, inline=True)),
        row("F", "Sometimes", "true whenever r = s — a relation between two variables, not a value."),
        row("G", "Sometimes", eq("k_G", 0.62, inline=True)),
        row("H", "Sometimes", f'holds for {eq("k_H", 0.62, inline=True)}'),
        row("I", "Always", f'distributive law: {eq("k_I", 0.62, inline=True)}'),
        row("J", "Always", f'distributive law: {eq("k_J", 0.62, inline=True)}'),
        row("K", "Sometimes", f'{eq("k_K", 0.62, inline=True)} — and false at y = 0, which is the counterexample to ask for.'),
        row("L", "Sometimes", eq("k_L", 0.62, inline=True)),
    ])
    return f"""{HEADER}
<div class="title">
  <h1><small>Teacher key · Mawhiba Grade 9 · Unit 1 · Activity 1</small>
  Answers, Misconceptions and What to Push On</h1>
  <div class="meta">Not for issue to students</div>
</div>

<div class="card" style="margin-bottom:2.4mm">
  <h2>Task 1 · the sum and the product</h2>
  <div class="grid g2">
    <div>
      <p><b>The statement:</b> {eq("m_stmt", 0.7, inline=True)}</p>
      <p style="margin-top:1.4mm"><b>Classification: sometimes true.</b> Collecting and factorising gives
      {eq("m_rearr", 0.62, inline=True)}, so {eq("m_gen", 0.7, inline=True)}</p>
      <p style="margin-top:1.6mm">Whole-number pairs: {eq("m_int", 0.7, inline=True)}</p>
      <p style="margin-top:1.6mm">With fractions allowed: {eq("k_a3", 0.7, inline=True)}</p>
    </div>
    <div>
      <p><b>The singular case.</b> {eq("m_a1", 0.7, inline=True)} — a false statement, so no b exists when
      a = 1. This is the point of the task: the formula is undefined exactly where the equation
      has no solution, and the two facts are the same fact.</p>
      <p style="margin-top:1.6mm"><b>Push on:</b> a student who answers “sometimes” from two
      integer pairs has guessed. Ask for the general b, then ask what happens at a = 1.</p>
    </div>
  </div>
</div>

<div class="card" style="margin-bottom:2mm">
  <h2 class="t">Task 2 · Classification key</h2>
  <table class="st">
    <tr><th></th><th>Statement</th><th>Classification</th><th>Justification</th></tr>
    {rows}
  </table>
  <p class="footnote" style="margin-top:1.2mm"><b>Three always, one never, eight sometimes.</b>
  The count is worth saying aloud — students expect the three kinds to be evenly spread, and B
  is the only inconsistent statement on the sheet.</p>
</div>

<div class="grid g2">
  <div class="card tint"><h2 class="p">Investigate — expected answers</h2>
    <ol class="num">
      <li style="margin-bottom:1.4mm">{eq("m_a1", 0.66, inline=True)} — the contradiction IS the proof.</li>
      <li style="margin-bottom:1.4mm">Never true: {eq("k_ch2", 0.66, inline=True)}</li>
      <li>Any identity in two non-zero variables, for example {eq("k_ch3", 0.66, inline=True)}</li>
    </ol>
  </div>
  <div class="card tint"><h2 class="g">The three misconceptions to name aloud</h2>
    <ul>
      <li><b>“It works for the numbers I tried, so it is always true.”</b> Examples never prove
      “always”. One counterexample disproves it; only algebra proves it.</li>
      <li><b>Using = where ≡ belongs.</b> C, I and J are identities; writing them with an equals
      sign loses the distinction the unit is built on.</li>
      <li><b>Treating an inequality as unclassifiable.</b> G and H are ordinary sometimes-true
      statements with a solution set — an interval instead of a point.</li>
    </ul>
  </div>
</div>
{foot("Teacher key · Mawhiba Unit 1 Activity 1", 1, 1)}"""


def render(pages, name):
    from playwright.sync_api import sync_playwright
    html = (f'<meta charset="utf-8"><title>{name}</title><style>{CSS}</style>'
            + "".join(f'<div class="page">{p}</div>' for p in pages))
    src = OUT / (name + ".html")
    src.write_text(html)
    pdf = OUT / (name + ".pdf")
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        pg.goto(src.as_uri())
        pg.wait_for_load_state("networkidle")
        over = pg.evaluate("""() => [...document.querySelectorAll('.page')].map(p => {
            const foot = p.querySelector('footer').getBoundingClientRect().top;
            let low = 0;
            for (const el of p.children) {
              if (el.tagName === 'FOOTER') continue;
              low = Math.max(low, el.getBoundingClientRect().bottom);
            }
            return { spill: p.scrollHeight - p.clientHeight, gap: foot - low };
          })""")
        pg.pdf(path=str(pdf), format="A4", print_background=True,
               margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
        b.close()
    for i, o in enumerate(over, 1):
        assert o["spill"] <= 1, f"{name} page {i}: content overflows the page by {o['spill']}px"
        assert o["gap"] >= 4, f"{name} page {i}: content runs into the footer (gap {o['gap']:.0f}px)"
    info = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
    n = int([l for l in info.splitlines() if l.startswith("Pages")][0].split()[-1])
    subprocess.run(["pdftoppm", "-png", "-r", "100", str(pdf), "_f"], check=True)
    fills = []
    for i in range(1, n + 1):
        im = np.array(Image.open(f"_f-{i}.png").convert("L"))
        cut = int(im.shape[0] * 0.93)          # the footer always sits below this
        rows = np.where((im[:cut] < 240).any(axis=1))[0]
        fills.append(rows.max() / im.shape[0])
        os.remove(f"_f-{i}.png")
    ok = n == len(pages) and all(0.78 <= f < 0.94 for f in fills)
    gaps = " / ".join(f"{o['gap']:.0f}px" for o in over)
    print(f"  {name}.pdf · {n} pages · fill " + " / ".join(f"{f:.3f}" for f in fills)
          + f" · clear of the footer by {gaps}" + ("" if ok else "   <-- FIX"))
    return ok


if __name__ == "__main__":
    a = render(worksheet(), "MAWHIBA_G9_U1_A1_Worksheet")
    b = render([key_page()], "MAWHIBA_G9_U1_A1_Teacher_Key")
    if not (a and b):
        raise SystemExit("layout does not fit")
