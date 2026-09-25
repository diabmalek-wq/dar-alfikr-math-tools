"""Build the AP Precalculus weekly session-distribution PDF — 4 sessions/week version."""
import json, datetime

data = json.load(open("sched_full4b.json"))
schedule = data["schedule"]
review_weeks = data["review_weeks"]

def fmt_range(s, e):
    s = datetime.date.fromisoformat(s); e = datetime.date.fromisoformat(e)
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    if s.month == e.month:
        return f"{s.day}–{e.day} {months[s.month-1]} {s.year}"
    return f"{s.day} {months[s.month-1]} – {e.day} {months[e.month-1]} {e.year}"

def session_cell(sess):
    if sess is None:
        return '<span class="dash">—</span>'
    typ, payload = sess
    if typ == "B":
        return '<span class="badge b">B</span> FRQ &amp; Calculator Lab'
    if typ == "D":
        return f'<span class="badge d">D</span> Mixed Review — {payload}'
    unit, num, lbl, title = payload
    return f'<span class="badge a">A</span> <b>{lbl}</b> · CED {unit}.{num} · {title}'

rows = []
for w in schedule:
    td = w["teaching_days"]
    sessions = w["sessions"]
    total_min = len(sessions) * 40
    if td == 0:
        rows.append(f'''<tr class="break-row"><td class="wk">W{w["week"]}</td>
          <td class="dates">{fmt_range(w["start"], w["end"])}</td>
          <td colspan="4" class="break-cell">{w["break"]} — no sessions</td>
          <td class="mins">0</td></tr>''')
        continue
    cells = [session_cell(tuple(sessions[i])) if i < len(sessions) else '<span class="dash">—</span>' for i in range(4)]
    rows.append(f'''<tr>
      <td class="wk">W{w["week"]}</td>
      <td class="dates">{fmt_range(w["start"], w["end"])}</td>
      <td class="sess">{cells[0]}</td>
      <td class="sess">{cells[1]}</td>
      <td class="sess">{cells[2]}</td>
      <td class="sess">{cells[3]}</td>
      <td class="mins">{total_min}</td>
    </tr>''')

review_activities = [
    ("Mock 1 — full timed paper, Section I (MCQ, calc + no-calc)",
     "Mock 1 — full timed paper, Section II (FRQ, all 4 questions)",
     "Rubric-based repair, Mock 1",
     "Calculator-fluency drill — regression, zeros, intersections"),
    ("Targeted repair by unit — Unit 1 &amp; 2 gaps from Mock 1",
     "Targeted repair by unit — Unit 3 gaps from Mock 1",
     "Mixed retrieval practice — Units 1–3 interleaved",
     "No-calculator periodic FRQ (FRQ 3) rehearsal"),
    ("Mock 2 — full timed paper, Section I",
     "Mock 2 — full timed paper, Section II",
     "Rubric-based repair, Mock 2",
     "Mixed retrieval practice — Units 1–3 interleaved"),
    ("Rubric drill — Communication &amp; Reasoning, timed",
     "No-calculator periodic FRQ (FRQ 3), final rehearsal",
     "Bluebook digital-testing rehearsal &amp; exam-day logistics check",
     None),
]
rev_rows = []
total_review_sessions = 0
for i, w in enumerate(review_weeks):
    acts = review_activities[i] if i < len(review_activities) else (None, None, None, None)
    td = w["teaching_days"]
    n_show = min(4, td)
    cells = []
    n_sess = 0
    for j in range(4):
        a = acts[j] if j < len(acts) else None
        if a is None or j >= n_show:
            cells.append('<span class="dash">—</span>')
        else:
            cells.append(f'<span class="badge r">R</span> {a}')
            n_sess += 1
    total_min = n_sess * 40
    total_review_sessions += n_sess
    rev_rows.append(f'''<tr>
      <td class="wk">W{w["week"]}</td>
      <td class="dates">{fmt_range(w["start"], w["end"])}</td>
      <td class="sess">{cells[0]}</td>
      <td class="sess">{cells[1]}</td>
      <td class="sess">{cells[2]}</td>
      <td class="sess">{cells[3]}</td>
      <td class="mins">{total_min}</td>
    </tr>''')

total_content_sessions = sum(len(w["sessions"]) for w in schedule)
total_content_minutes = total_content_sessions * 40
total_review_minutes = total_review_sessions * 40

def page_header(subtitle_suffix, page_no):
    return f'''<header><img src="dept_logo.png" alt=""><img class="cognia" src="cognia_badge.png" alt="Cognia School of Distinction 2024"><img src="school_logo.png" alt=""></header>
<div class="title"><h1><small>Weekly Session Distribution · 2026–27{subtitle_suffix}</small>AP Precalculus</h1>
<div class="meta">Dar Alfikr Schools<br>Prepared by Mr Malek Thiab</div></div>'''

html = f"""<!doctype html><html><head><meta charset="utf-8"><style>
@page {{ size: A4 landscape; margin: 0; }}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
:root {{
  --navy:#1F3864; --teal:#17A199; --ink:#222E2D; --gold:#F0B323; --grey:#6B7674;
  --tint:#EDF5F4; --tint2:#F7FAFA; --line:#C9DEDC; --plum:#6B3FA0; --red:#C62828;
}}
body {{ font-family:"DejaVu Sans",sans-serif; color:var(--ink); font-size:7.6pt; line-height:1.28; }}
.page {{ width:297mm; height:210mm; padding:6.5mm 9mm 10mm; position:relative; page-break-after:always; overflow:hidden; }}
.page:last-child {{ page-break-after:auto; }}
header {{ display:flex; align-items:center; justify-content:space-between; border-bottom:2px solid var(--teal); padding-bottom:1.6mm; margin-bottom:1.8mm; }}
header img {{ height:9mm; }} header img.cognia {{ height:12mm; }}
.title {{ display:flex; align-items:flex-end; justify-content:space-between; margin-bottom:1.6mm; }}
.title h1 {{ font-size:13pt; color:var(--navy); line-height:1.1; }}
.title h1 small {{ display:block; font-size:7.2pt; color:var(--plum); font-weight:600; letter-spacing:.06em; text-transform:uppercase; margin-bottom:.7mm; }}
.title .meta {{ text-align:right; font-size:6.8pt; color:var(--grey); }}
.idbar {{ display:flex; gap:3mm; font-size:7.2pt; margin-bottom:2mm; }}
.idbar div {{ flex:1; border-bottom:1px solid var(--line); padding-bottom:.9mm; }}
.idbar b {{ color:var(--navy); }}
.pattern-hl {{ font-weight:bold; font-size:10.5pt; color:var(--red); }}
h2.sec {{ font-size:8.2pt; color:#fff; background:var(--navy); display:inline-block; padding:.7mm 2.1mm; border-radius:1mm; letter-spacing:.04em; text-transform:uppercase; margin-bottom:1.4mm; }}
h2.sec.r {{ background:var(--plum); }}
table.sched {{ width:100%; border-collapse:collapse; font-size:6.9pt; }}
table.sched th {{ background:var(--tint); color:var(--navy); font-size:6.4pt; text-transform:uppercase; letter-spacing:.03em; padding:1mm 1.2mm; border:1px solid var(--line); text-align:left; }}
table.sched td {{ border:1px solid var(--line); padding:1mm 1.4mm; vertical-align:middle; }}
table.sched td.wk {{ font-weight:bold; color:var(--plum); width:10mm; text-align:center; }}
table.sched td.dates {{ width:29mm; color:var(--grey); }}
table.sched td.mins {{ width:11mm; text-align:center; font-weight:bold; color:var(--navy); }}
table.sched tr.break-row td {{ background:var(--tint2); color:var(--grey); font-style:italic; }}
td.break-cell {{ text-align:center; }}
.badge {{ display:inline-block; width:3.8mm; height:3.8mm; line-height:3.8mm; text-align:center; border-radius:50%; color:#fff; font-size:6.1pt; font-weight:bold; margin-right:.9mm; }}
.badge.a {{ background:var(--teal); }} .badge.b {{ background:var(--gold); color:#4A3400; }}
.badge.d {{ background:var(--plum); }} .badge.r {{ background:var(--red); }}
.dash {{ color:var(--line); }}
.legend {{ display:flex; gap:4.5mm; font-size:6.7pt; color:var(--grey); margin-top:1.4mm; flex-wrap:wrap; }}
.legend span {{ display:flex; align-items:center; }}
.summary-grid {{ display:grid; grid-template-columns:repeat(4,1fr); gap:3mm; margin-bottom:2.2mm; }}
.stat {{ border:1px solid var(--line); border-radius:2mm; padding:1.8mm 2.4mm; background:#fff; }}
.stat .n {{ font-size:14pt; font-weight:bold; color:var(--navy); }}
.stat .lab {{ font-size:6.3pt; color:var(--grey); text-transform:uppercase; letter-spacing:.03em; }}
footer {{ position:absolute; left:9mm; right:9mm; bottom:3.6mm; display:flex; align-items:center; justify-content:space-between; font-size:6.4pt; color:var(--grey); border-top:1px solid var(--line); padding-top:1.3mm; }}
footer .motto {{ color:var(--navy); font-size:6.8pt; letter-spacing:.1em; text-transform:uppercase; font-weight:bold; }}
</style></head><body>

<div class="page">
{page_header("", 1)}
<div class="idbar">
<div><b>Period length</b> 40 min</div>
<div><b>Pattern</b> <span class="pattern-hl">4 sessions/week</span> (2 Type A + 1 Type B + 1 Type D)</div>
<div><b>Window</b> Week 5 (27 Sep 2026) – Week 31 (2 wks before exam)</div>
<div><b>Exam</b> Tue 11 May 2027</div>
</div>

<div class="summary-grid">
<div class="stat"><div class="n">44</div><div class="lab">CED topics to teach, starting L1-1 (Units 1–3)</div></div>
<div class="stat"><div class="n">{total_content_sessions}</div><div class="lab">Sessions, Weeks 5–31 ({total_content_minutes} min)</div></div>
<div class="stat"><div class="n">{total_review_sessions}</div><div class="lab">Review/mock sessions, Weeks 32–35 ({total_review_minutes} min)</div></div>
<div class="stat"><div class="n">160</div><div class="lab">Minutes/week, full 4-session weeks</div></div>
</div>

<h2 class="sec">Content delivery — Weeks 5–31</h2>
<table class="sched">
<tr><th>Wk</th><th>Dates</th><th>Session 1</th><th>Session 2</th><th>Session 3</th><th>Session 4</th><th>Min/wk</th></tr>
{''.join(rows[:11])}
</table>
<footer><span>AP Precalculus · Weekly Session Distribution</span><span class="motto">Faith, Righteousness and Wisdom</span><span>Mr Malek Thiab · Page 1 of 3</span></footer>
</div>

<div class="page">
{page_header(" · continued", 2)}
<h2 class="sec">Content delivery — Weeks 5–31, continued</h2>
<table class="sched">
<tr><th>Wk</th><th>Dates</th><th>Session 1</th><th>Session 2</th><th>Session 3</th><th>Session 4</th><th>Min/wk</th></tr>
{''.join(rows[11:])}
</table>
<div class="legend">
<span><span class="badge a">A</span>&nbsp;Core teaching — one new CED topic per session</span>
<span><span class="badge b">B</span>&nbsp;FRQ &amp; Calculator Lab — rubric-marked reasoning + calculator drill</span>
<span><span class="badge d">D</span>&nbsp;Mixed Review — interleaved retrieval practice across units already taught (raises the exam's own mixed-topic format)</span>
</div>
<p style="margin-top:2mm;font-size:6.7pt;color:var(--grey)">Teaching starts at <b>L1-1</b> in Week&nbsp;5 — all 44 CED topics (1.1–1.14, 2.1–2.15, 3.1–3.15)
are delivered by Week&nbsp;30, two Type A sessions/week throughout. L1-1–L1-5 materials (study guides,
decks, worksheets) are already built and ready to teach; L1-6 onward still need building ahead of their week.</p>
<footer><span>AP Precalculus · Weekly Session Distribution</span><span class="motto">Faith, Righteousness and Wisdom</span><span>Mr Malek Thiab · Page 2 of 3</span></footer>
</div>

<div class="page">
{page_header(" · continued", 3)}
<h2 class="sec r">Review &amp; mock cycle — Weeks 32–35 (content-freeze block)</h2>
<table class="sched">
<tr><th>Wk</th><th>Dates</th><th>Session 1</th><th>Session 2</th><th>Session 3</th><th>Session 4</th><th>Min/wk</th></tr>
{''.join(rev_rows)}
</table>
<div class="legend"><span><span class="badge r">R</span>&nbsp;Review/mock — no new content; matches the department's standing pre-exam pattern (SAT/SAAT/GAT)</span></div>
<p style="margin-top:2.2mm;font-size:6.7pt;color:var(--grey)">Two weeks remain after Week&nbsp;35 (26 Apr–10 May) before the exam (Tue&nbsp;11&nbsp;May 2027) as
unscheduled buffer, plus the exam itself falling inside the school's Eid al-Adha break (7–22 May) —
logistics to confirm with the AP coordinator. Still open: which timetable slot(s) supply the fourth
weekly period.</p>
<footer><span>AP Precalculus · Weekly Session Distribution</span><span class="motto">Faith, Righteousness and Wisdom</span><span>Mr Malek Thiab · Page 3 of 3</span></footer>
</div>

</body></html>"""

open("AP_Precalculus_Weekly_Session_Distribution.html", "w", encoding="utf-8").write(html)
print("written, rows:", len(rows), "review rows:", len(rev_rows))
print("content sessions:", total_content_sessions, "review sessions:", total_review_sessions)
