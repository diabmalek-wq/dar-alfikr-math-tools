# Private Linear Algebra Tutoring — Weekly Schedule (Fall 2026 → January Exam)

**Student level:** College (Linear Algebra I, equivalent to U of T MAT223 / MAT A22)
**Format:** 1 session per week, 3 hours per session
**Sources:** Kielstra, *MAT A22 Course Notes* (Weeks 0–2: field/vector-space foundations); Siefken, *MAT223 Workbook* (16 modules + Appendices 1–4)
**Exam window:** Early January 2027 (Jan 5–9) → last content session is Dec 28, 2026; Jan 4, 2027 is pure review/mock exam.

| # | Week of | Topic(s) | Source | Worksheet |
|---|---------|----------|---|---|
| 1 | Sep 28, 2026 | Fields, Vector Space Axioms, Complex Numbers | Kielstra Wk 0–1 (1A, 1B) | `week-01` |
| 2 | Oct 5, 2026 | Vector Spaces of $n$-tuples, Matrices & Functions; Matrix Operations | Kielstra Wk 0 (0A–0C) + Siefken App. 3 | `week-02` |
| 3 | Oct 12, 2026 | Systems of Linear Equations I & II | Siefken App. 1–2 | `week-03` |
| 4 | Oct 19, 2026 | Sets, Vectors & Notation | Siefken Module 1 | `week-04` |
| 5 | Oct 26, 2026 | Sets of Vectors, Lines & Planes | Siefken Module 2 | `week-05` |
| 6 | Nov 2, 2026 | Spans, Translated Spans, Linear (In)dependence | Siefken Module 3 | `week-06` |
| 7 | Nov 9, 2026 | Dot Products, Normal Forms & Projections | Siefken Modules 4–5 | `week-07` |
| 8 | Nov 16, 2026 | Subspaces & Bases | Siefken Module 6 | `week-08` |
| 9 | Nov 23, 2026 | Matrix Representations of Systems; Coordinates & Change of Basis I | Siefken Modules 7–8 | `week-09` |
| 10 | Nov 30, 2026 | Linear Transformations | Siefken Module 9 | `week-10` |
| 11 | Dec 7, 2026 | Composition of Linear Transformations; Range & Nullspace | Siefken Modules 10–11 | `week-11` |
| 12 | Dec 14, 2026 | Inverse Functions & Inverse Matrices; Change of Basis II | Siefken Modules 12–13 | `week-12` |
| 13 | Dec 21, 2026 | Determinants (incl. 2×2/3×3 formulas) | Siefken Module 14 + App. 4 | `week-13` |
| 14 | Dec 28, 2026 | Eigenvalues, Eigenvectors & Diagonalization | Siefken Modules 15–16 | `week-14` |
| 15 | Jan 4, 2027 | **Full-course review + timed mock exam** | All | `week-15` |

**Exam:** Jan 5–9, 2027

## Worksheet format (every week, no logos/branding)

1. **Page 1** — Introduction, rules, key facts, definitions (verbatim from source, cited).
2. **Pages 2–3** — Fully solved worked examples.
3. **Pages 4–5** — Unsolved practice problems/questions (answer key provided separately at the end of the file, not inline, so the student works blind).

**Delivery format:** each week's `.md` file is the committed source of record. The actual
deliverable handed to the tutor/student is a **designed PDF** — not a plain rendering of
the markdown — built by `linear-algebra-tutoring/tools/`:

```
tools/build.sh 0N  week-0N/Week-0N-<Topic-Slug>.md  tools/hints/week-0N.json  <out-dir>
```

This produces `Week-0N-worksheet.pdf` (student-facing) and `Week-0N-answerkey.pdf`
(tutor-only, separate file) from the one `.md` source. What `tools/render.py` +
`tools/preamble.tex` add on top of the raw markdown:

- Every `### Definition:` / `### Fact:` / `### Key Fact:` / `### Theorem:` block on Page 1
  becomes a colour-coded box (blue/teal), auto-classified from its heading — not left as
  plain text.
- Every worked example becomes its own numbered card.
- Every unsolved practice problem gets a **HINT** box (method nudge, no answer given) and
  a **CAUTION** box (the answer key's own misconception, reworded as advice given
  *before* solving, not after) — authored per-problem in `tools/hints/week-0N.json` —
  followed by ruled blank space for the student to work in. Line count scales with the
  problem (multi-part items and long stems get more lines).
- The answer key is rendered separately, as one card per problem (answer + misconception),
  never merged into the student PDF.
- Title is simplified to "Linear Algebra — Week 0N", with the topic and source citation as
  a subtitle underneath.

`tools/hints/week-0N.json` must exist before building — write it (or have an agent write
it) as `{"1": {"hint": "...", "caution": "..."}, ...}`, one entry per practice problem,
with the caution derived from that problem's existing answer-key misconception note.

Technical notes for future maintenance:
- `xelatex` (not `pdflatex`) is required — the source files use literal Unicode characters
  (×, –, —, ✓) that `pdflatex`'s default font can't render, and `DejaVu Serif` covers them.
- Content that ends up inside a custom `tcolorbox` (`\begin{definitionbox}...}` etc.) is
  treated by pandoc's `raw_tex` extension as ONE opaque block and never reprocessed as
  markdown — `render.py`'s `md2tex()` helper pre-converts each box's inner markdown to
  LaTeX via a separate `pandoc -f markdown -t latex` pass before wrapping it, which is why
  that helper must not be skipped when extending the script.
- A long display equation (e.g. a multi-step row-reduction chain) that fit the *full* page
  width as plain text can overflow a box's narrower content width. `render.py` auto-wraps
  every display-math block in `adjustbox{max width=\boxmathwidth}` to shrink it back down —
  and that `adjustbox` must be on its own `\par`-separated line (not inline with surrounding
  text), or `\linewidth`/box measurement gets confused and the shrink silently fails.
- Neither the rendered PDFs nor `tools/out/`-style scratch output are committed — they're
  build artifacts of the `.md` source and the hints JSON; regenerate and re-deliver them
  whenever either changes.
