# Architecture — how a request becomes a deliverable

The pipeline described below is now populated with real code (see `docs/MIGRATION.md`
for the file-by-file migration record). This document describes both the shape of the
pipeline and, in "Current status" below, exactly what exists in each stage today.

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
Populated subfolders today: `lessons/`, `exam-prep/`, `gat-bank/`, `saat-bank/`,
`mawhiba/`, `ap-precalculus/`. `sat-bank/` does not exist yet — the SAT item bank still
lives only as a Claude Project doc, not a script (see `docs/MIGRATION.md`).

**`engines/`** — the reusable builders: `lesson_engine.js` (FIKR deck),
`docs_engine.js` (lesson-plan/classwork/routes/PBL docx), `exam_engine.js`
(exam-prep paper + key), `presession.js`, plus two post-processing steps that run on an
already-built deck (`animate_deck.py`, then `embed_geogebra.py` — order matters, see
`docs/LESSONS-LEARNED.md`). An engine takes a config object and produces the deliverable;
it has no knowledge of any one week's content. All six engines above are committed.

**`generators/`** — content that an engine's config references rather than authors
inline: rendered math (`make_math_*.py`, `pdflatex` + Computer Modern), figures
(`make_figs_*.py`, matplotlib, house style), function graphs (`make_graphs_*.py`), and the
label-placement guard (`figlabel.py`) that runs before any figure ships. Generators are
called by builder configs or by engines while assembling a deliverable, not run standalone
against a finished output. 74 generator scripts are committed, covering every week/part
suffix referenced by the builders above.

**`verifiers/`** — runs after content exists, before it ships. Two kinds: independent
re-derivation (`verify_sim.py`, `verify_saat.py` + 12 per-part variants — re-solve every
item by a method that doesn't read the item's own stated reasoning) and
structural/consistency checks (`validate_set.js`, `audit_pair.js`, `audit_gat.js`,
`lint_saat.js`, `measure_rev.py`/`calibrate_pbl.py` for page-fill). Per the working
agreement in `README.md`, point 3: every build that ships an answer runs its verifier —
no exceptions. All verifiers listed in `docs/MIGRATION.md` are committed.

**`config/`** and **`data/`** feed every stage rather than sitting in the pipeline
themselves: `config/` is meant to hold the shared constants (branding, FIKR timing bands,
banned-label list, page-fill thresholds) that engines and verifiers both read — **this is
still an empty placeholder today**. Those constants are hardcoded inline inside each
engine rather than factored into a shared module; extracting them is a deliberate
follow-up refactor, not a migration (see `docs/MIGRATION.md`). `data/` holds the actual
bank contents and ledgers (`data/banks/`, `data/ledgers/`, `data/skill-maps/`) that a
`builders/gat-bank/` or `builders/saat-bank/` config draws items from — these are
committed and populated.

**`assets/`** is passive input, not a pipeline stage — logos (`assets/logos/`, fully
populated) and fixed-format templates (`assets/templates/`, partially populated — only
`meth_tpl.docx`; the two blank lesson-plan templates were never found as standalone files
and are noted as skipped in `docs/MIGRATION.md`) that `docs_engine.js` and the branding
rules in `docs/HOUSE-RULES.md` reference.

## Why it's a pipeline and not a monolith

The split exists so that a new week's material is *only* a new `builders/` file: the
engine, its generators, and its verifier are already correct and already caught last
week's bugs (that's the point of `docs/LESSONS-LEARNED.md`). Skipping a stage — hand-
editing an engine for one week, or shipping without the verifier — is exactly the pattern
that has silently reintroduced fixed bugs in the past.

## Current status

`engines/`, `generators/`, `verifiers/`, and `builders/` (all six product subfolders
except `sat-bank/`) are committed and populated — this is no longer a target shape, it's
the current repo. What's still open:

- **`config/`** — empty; constants remain inline in each engine.
- **`builders/sat-bank/`** — doesn't exist; the SAT item bank hasn't been turned into a
  script yet.
- **`assets/templates/`** — missing the two blank lesson-plan templates.
- **No dependency install has been exercised end-to-end** — `package.json` and
  `requirements.txt` list what the code imports, but no session has yet run a build from
  a clean clone to confirm the pipeline actually executes top to bottom.
- **No CI** — nothing runs the verifiers automatically on a push.

See `docs/MIGRATION.md` for the full file-by-file record of what was migrated, what was
skipped, and why.
