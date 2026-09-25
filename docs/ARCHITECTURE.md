# Architecture — how a request becomes a deliverable

High-level only. No engine code is committed to this repo yet (see `docs/MIGRATION.md`
for the file-by-file plan), so this describes the shape of the pipeline each engine will
fill, not the implementation of any one of them.

## The pipeline

```
builders/<product>/<config>.js|py
        │  (a thin, per-product config: content + which engine to call)
        ▼
engines/<name>_engine.js|py
        │  (reusable, config-driven — the same engine builds every week's deck/paper/docx)
        ▼
generators/  ──►  fills in the content the engine needs
        │  (LaTeX math PNGs, matplotlib figures, function graphs — each generator
        │   asserts its own correctness before handing content back, e.g.
        │   figlabel.py, "a figure that carries an answer asserts that answer
        │   in its own drawing code")
        ▼
verifiers/  ──►  independent QA, never trusting the item text
        │  (re-derives every answer by an independent method; structural checks —
        │   sig uniqueness, trick↔item binding, page-count/page-fill measurement)
        ▼
output: PDF / PPTX / DOCX
        (the deliverable — lives in the Claude Project, not this repo)
```

## What each stage owns

**`builders/`** — one file per product per week/part (e.g. `lessons_w3.js`,
`exam_w3.js`, `sim_items_c.js`). A builder never contains engine logic; it supplies data
and config to an engine. Adding a new week or bank part means adding a new file here, not
editing an engine — see the working agreement in `README.md`, point 2. An engine change is
only justified by a genuine engine bug or a new house rule (`docs/HOUSE-RULES.md`).

**`engines/`** — the reusable builders: `lesson_engine.js` (FIKR deck),
`docs_engine.js` (lesson-plan/classwork/routes/PBL docx), `exam_engine.js`
(exam-prep paper + key), `presession.js`, plus two post-processing steps that run on an
already-built deck (`animate_deck.py`, then `embed_geogebra.py` — order matters, see
`docs/LESSONS-LEARNED.md`). An engine takes a config object and produces the deliverable;
it has no knowledge of any one week's content.

**`generators/`** — content that an engine's config references rather than authors
inline: rendered math (`make_math_*.py`, `pdflatex` + Computer Modern), figures
(`make_figs_*.py`, matplotlib, house style), function graphs (`make_graphs_*.py`), and the
label-placement guard (`figlabel.py`) that runs before any figure ships. Generators are
called by builder configs or by engines while assembling a deliverable, not run standalone
against a finished output.

**`verifiers/`** — runs after content exists, before it ships. Two kinds: independent
re-derivation (`verify_sim.py`, `verify_saat.py` — re-solve every item by a method that
doesn't read the item's own stated reasoning) and structural/consistency checks
(`validate_set.js`, `audit_pair.js`, `audit_gat.js`, `lint_saat.js`,
`measure_rev.py`/`calibrate_pbl.py` for page-fill). Per the working agreement in
`README.md`, point 3: every build that ships an answer runs its verifier — no exceptions.

**`config/`** and **`data/`** feed every stage rather than sitting in the pipeline
themselves: `config/` holds the shared constants (branding, FIKR timing bands, banned-
label list, page-fill thresholds) that engines and verifiers both read; `data/` holds the
actual bank contents and ledgers (`data/banks/`, `data/ledgers/`, `data/skill-maps/`) that
a `builders/gat-bank/` or `builders/saat-bank/` config draws items from.

**`assets/`** is passive input, not a pipeline stage — logos and fixed-format templates
that `docs_engine.js` and the branding rules in `docs/HOUSE-RULES.md` reference.

## Why it's a pipeline and not a monolith

The split exists so that a new week's material is *only* a new `builders/` file: the
engine, its generators, and its verifier are already correct and already caught last
week's bugs (that's the point of `docs/LESSONS-LEARNED.md`). Skipping a stage — hand-
editing an engine for one week, or shipping without the verifier — is exactly the pattern
that has silently reintroduced fixed bugs in the past.

## Current status

None of `engines/`, `generators/`, or `verifiers/` are committed yet — this document
describes the target shape. See `docs/MIGRATION.md` for what exists where today and the
plan for moving it into this repo.
