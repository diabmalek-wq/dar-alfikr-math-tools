# SAT Math mock-exam generator (Bluebook-style)

Turns one JSON file of 44 questions into a **single self-contained HTML exam** that looks and behaves like Bluebook: two timed 35-minute modules, lavender header and footer with dashed rules, numbered question bar with Mark for Review and the ABC eliminator, split-screen grid-in directions with the on-screen keypad, a question map, the reference sheet, a docked Desmos Graphing/Scientific calculator, and a score report with an **expected score band of 40 points** (for example `680–720`), section and type breakdowns, pacing chart, and a filterable review with worked Desmos steps.

```
exams/exam-NN_<topic>.json  --build.py-->  dist/<name>.html   (send the file to the student)
```

## Build an exam

```bash
cd sat-math/mock-exam-generator
python3 build.py exams/exam-01_sessions-1-3-4-10.json \
  --title "SAT Aceit" \
  --intro "44 questions from Sessions 1, 3, 4 and 10." \
  --sessions "01=Session 1 · Quadratics & Nonlinear Functions" "03=Session 3 · Nonlinear Equations & Systems" \
             "04=Session 4 · Equivalent Expressions" "10=Session 10 · Circles" \
  --desmos-key "$DESMOS_API_KEY" \
  --out dist/SAT_Aceit_Exam-01.html
python3 smoke_test.py dist/SAT_Aceit_Exam-01.html     # optional: answers everything, fails on JS errors or raw LaTeX
```

* `build.py` validates the JSON first (22 + 22 items, four distinct options, key index, even `$`, steps present, answer-position spread) and refuses to build on errors.
* The **Desmos API key is not stored in this repo.** Pass `--desmos-key` or set `DESMOS_API_KEY`. Without a key the calculator panel shows a link to the College Board test-mode Desmos. A key also works through the page URL: `...html?desmosKey=KEY`.
* Figures are optional: put `F001.svg` files in a folder, set `"fig":"F001"` on an item and pass `--figs folder`.

## Item format

```json
{"id":"AM-142T","sess":"03","lv":"M","mc":true,
 "q":"$$\\dfrac{9}{x^2-6x+9}=4$$\nWhat is the sum of the squares of all solutions?",
 "opts":["$6$","$\\dfrac{45}{2}$","$9$","$36$"],"key":1,
 "steps":["Type <code>y=9/(x^2-6x+9)</code> and <code>y=4</code>. ...","Trap: ..."],
 "domain":"Advanced Math","skill":"Nonlinear equations in one variable"}
```

Grid-in items use `"mc":false`, a numeric `"key"` and, for non-integers, `"disp":"\\dfrac{3}{4}"` (a tolerance of 0.002 is applied to non-integer keys). Module 1 is `m1` (Medium), module 2 is `m2` (Hard).

## House rules for new exams

1. **Verify every key with code** before building (a quick numpy or sympy check of the answer and of each distractor). `exams/exam-01_authoring-source.py` shows the pattern: item, trap, steps and assertion together.
2. **Every distractor is a named trap** (sign error, partial step, wrong quantity asked, using the vertex x instead of the minimum value) and the step list says which trap it is.
3. **LaTeX for all maths**, English only. Do not copy College Board or published items; write new numbers and a new angle, and keep the Desmos route in the steps.
4. Spread correct answers over A–D; the builder warns if one position holds more than 40%.
5. The score band uses the 44-question table in `template.html` (`PTS`). It is a non-adaptive estimate and is labelled as one on the report.

## Files

| File | Purpose |
|---|---|
| `template.html` | The exam app: Bluebook-style shell, calculators, keypad, scoring, review. Placeholders `{{TITLE}}`, `{{INTRO}}`, `{{DESMOS_KEY}}`, `/*DATA*/`, `/*SESS*/`, `/*FIGS*/` |
| `build.py` | Validates a JSON and fills the template |
| `smoke_test.py` | Headless Chromium run-through (needs `playwright`) |
| `exams/exam-01_sessions-1-3-4-10.json` | Exam 1 (SAT Aceit): Sessions 1, 3, 4 and 10, rewritten as trickier variants |
| `exams/exam-01_authoring-source.py` | Source that generated exam 1, with the numeric checks |

## Known limits

* Fixed layout: 2 modules × 22 questions, 35 minutes each.
* The embedded calculator is the public Desmos API, not the locked-down College Board test-mode build. Inside the Claude artifact preview Desmos is blocked; open the downloaded file in Chrome or Edge with internet access.
* Maths is typeset with KaTeX from cdnjs when reachable and otherwise by a built-in MathML renderer (supports fractions, roots with index, powers, subscripts, `\overline`, common symbols).
