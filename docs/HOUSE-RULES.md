# House rules — branding, typography, and the FIKR model

The non-negotiables a builder-script author checks *before* writing a new `builders/`
config, not after a build fails review. These are pulled together from `README.md`'s
layout section and `docs/LESSONS-LEARNED.md`; that file remains the fuller "why," this
one is the quick-check list. If the two ever disagree, `LESSONS-LEARNED.md` wins — it's
condensed from the Weekly Work Order Standing Spec directly.

## Branding

- **Teacher of record on every deliverable: Mr Malek Thiab.** Never a colleague's name,
  even when a source syllabus lists someone else.
- **Department logos only**, from `assets/logos/` — `dept_logo.png`, `cognia_badge.png`,
  `school_logo.png`. Don't substitute a generic or template logo.
- **Fixed-format templates get filled in place, not rebuilt.** `assets/templates/`
  (`FIKR Lesson Plan Template.docx`, `Lesson plan 2026.docx`, `meth_tpl.docx`) are the
  source of the department's document shell — a new config fills them, it doesn't
  reinvent their layout.
- **Standards/CCSS codes: bottom corner only, code form, never a full-text badge.** A
  code (e.g. `HSA-REI.B.3`) is fine; the spelled-out standard text is not, and it never
  moves to a header or title position.
- **Colour palette and general branding constants live in `config/`**, shared across
  engines — a builder config references them, it doesn't hard-code a colour or redefine
  the palette locally.

## Typography and layout

- **English only, unless explicitly asked for Arabic.** When Arabic is asked for, see the
  extraction rules in `LESSONS-LEARNED.md` (`-raw`, reversed token order) — those are for
  *sourcing* text, not for how a deliverable is typeset, but they're the closest existing
  guidance and should inform any Arabic layout work until a dedicated rule exists.
- **Math is rendered via `pdflatex` + Computer Modern**, not a screenshot or a Unicode
  approximation — see `generators/make_math_*.py`. Output is ~460 dpi PNG so it stays
  sharp at print size.
- **Task routes, never ability labels.** Differentiated work is always framed as
  Practice / Apply / Investigate, with "Done when…" phrasing — never "Success:" and
  never a route that implies who is "behind" or "ahead."
- **Fixed page budgets, measured, not assumed:**
  - PBL project sheets: A3, one page.
  - Exam-prep student papers: exactly 4 pages, verified with `pdfinfo` after every build.
  - General content pages: target 0.78–0.94 page-fill (last-ink-above-footer ÷ page
    height). Short reference/key pages are a documented, deliberate exception — not a
    bug to silently "fix" by padding them.
- **Word/LibreOffice layout guards are non-negotiable on any docx build:**
  identical-border paragraphs need an alternating one-twip indent to avoid merging into
  one visual line; `keepNext`/`cantSplit` goes on every stem+options block; typeset math
  options that don't fit 4-across drop to 2-across before anything is allowed to clip.
- **Figure labels must never sit on the drawing** — enforced by `figlabel.py`, and that
  guard is never bypassed for a "just this once" figure.

## The FIKR model

FIKR is the department's lesson framework — it's what `engines/lesson_engine.js` builds
(the "18-slide FIKR lesson deck") and what `config/` encodes timing bands for ("FIKR
timing bands"). Its full pedagogical definition — what each of the four pillars means,
how time is allocated across them, and the narrative rationale — is a **standing decision
of the Claude Project**, not something duplicated into this repo (see the working
agreement in `README.md`, point 4: the Project is the source of truth for decisions, not
code). A builder-script author needing the actual FIKR breakdown to write a new lesson
config should pull it from the Project's `claude/*.md` docs rather than guessing from this
file.

What *is* safe to assume from this repo alone:
- Every lesson deck goes through `lesson_engine.js` as a FIKR deck — there is no
  non-FIKR lesson format in this system.
- Timing bands are config-driven (`config/`), not hard-coded per lesson — a new week's
  config supplies content, not a new timing scheme.
- The `FIKR Lesson Plan Template.docx` and `Lesson Plan 2026-27` outputs
  (`engines/docs_engine.js`) follow the same four-pillar structure as the slide deck —
  they are two renderings of one lesson, not two different lesson models.

## Content integrity (feeds the build-time guards)

These are rules about *what* goes into a build; `LESSONS-LEARNED.md` has the matching
*build-time guard* for each one — treat the two as a pair, not a redundancy:

- Curriculum-map objectives are quoted verbatim. Never paraphrased, merged, or invented.
- A trick binds to an item by the item's own original source number, parsed from its
  reasoning — never by array position.
- Every answer is independently re-derived in Python, never re-stated from the item's own
  reasoning.
- Sourcing rules (department-internal banks stay internal; recalled-booklet material
  takes only skill + trick, never stem/numbers/options/figure; never source from a still-
  rotating item pool) apply before an item is written, not after.

## Cost efficiency (Mr Thiab's standing instruction, 26 Sep 2026)

Every deliverable must be produced at the lowest reasonable token/compute cost. This
governs *how* an assistant works in this repo, not just what it produces:

- **Read PDFs as text, not as images.** Use `markitdown <file>.pdf` (installed via
  `pip3 install markitdown`) or `pdftotext` to extract a source PDF's content. Never
  render a PDF to PNG and read it as an image just to get its text — that is a vision
  call for something a text extractor does for free.
- **Visual (image) verification is reserved for final delivery, not every draft.**
  Check a build with `pdfinfo` (page count) and `pdftotext`/`markitdown` (content,
  clipped text, missing sections) first. Only render pages to PNG and read them back
  visually once, right before a file is actually handed to Mr Thiab — not after every
  intermediate fix.
- **Don't re-read whole files you already have.** Once an engine or config file has
  been read this session, use `grep`/`sed`/targeted line ranges to check or change one
  part of it rather than reading the entire file again. This applies especially to the
  large shared engines (`lesson_engine.js`, `docs_engine.js`, `exam_engine.js`,
  `presession.js`) — their structure doesn't change between builds.
- **Don't re-research settled precedent.** Once a format, code list, or convention has
  been confirmed from a source (a curriculum map, a real delivered PDF, a spreadsheet),
  reuse that finding for the rest of the session instead of re-fetching it.
- **Batch fixes, then verify once**, instead of a fix → rebuild → visually inspect →
  fix → rebuild loop. Read the engine/generator code carefully enough on the first pass
  to get layout right without needing a render to find out.

## Where to look next

- `docs/LESSONS-LEARNED.md` — the full list of known traps and why each guard exists.
- `docs/ARCHITECTURE.md` — how a config becomes a deliverable through engines → generators
  → verifiers.
- `verifiers/README.md` — which verifier applies to which product (once committed; see
  `docs/MIGRATION.md`).
