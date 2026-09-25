# dar-alfikr-math-tools

Build tooling for Mr Malek Thiab's Mathematics Department materials at Dar Alfikr Schools
(Grades 9–12: Mawhiba, Core Algebra II, SAT, SAAT/Tahsili, GAT/Qudurat, AP Precalculus).

This repo holds the **engines and scripts**, not the deliverables. Finished PDFs/PPTX/DOCX
and the narrative decision-log docs live in the Claude Project "Math, Grade 9, 10, 11, 12" —
this repo is what a Claude Code session (local or cloud) reads and writes when it needs to
regenerate or extend a build, instead of reconstructing every engine from scratch each time.

## Why this repo exists

Every session working on this department's materials was rebuilding the same Python/JS
engines from memory of the Weekly Work Order log. That's wasted tokens and a real risk of
silently reintroducing a bug that was already fixed once (see `docs/LESSONS-LEARNED.md`).
Committing the actual code fixes both problems and makes the tooling usable from a
Claude Code cloud session tied to this repo.

## Layout

```
engines/            Reusable, config-driven builders — the core of the system.
  lesson_engine.js     18-slide FIKR lesson deck from one config object.
  docs_engine.js       FIKR Lesson Plan / Lesson Plan 2026-27 / Classwork / Routes / PBL docx.
  exam_engine.js       Exam-prep paper + answer key (GAT/SAT/SAAT), dense mode, bare mode,
                       comparison-note box, option-width guard, keep-together rows.
  presession.js        4-slide / 2-page pre-session material.
  animate_deck.py      Injects click-by-click PowerPoint animation into a built deck's XML.
  embed_geogebra.py    Drops a GeoGebra exploration clip into a slide (run AFTER animate_deck).

generators/          Content generators that feed the engines.
  make_math_*.py       LaTeX expression rendering (pdflatex + Computer Modern, ~460 dpi PNG).
  make_figs_*.py       matplotlib figures, house style, figure-asserts-its-own-numbers pattern.
  make_graphs_*.py     Function graphs for lesson decks.
  figlabel.py          Label-placement guard — refuses to ship a label sitting on a drawing.

verifiers/            Independent re-derivation / structural QA — never trust the item text.
  verify_sim.py         GAT bank — re-derives every answer independently.
  verify_saat.py (+ per-part)   SAAT bank — same, by independent method per item type.
  validate_set.js, audit_pair.js, audit_gat.js, lint_saat.js   structural + trick-binding checks.
  measure_rev.py, calibrate_pbl.py   page-fill / page-count measurement (never guess).

builders/            Per-product configs — thin files that call the engines above.
  lessons/             lessons_wN.js, wN_docs.js, presession_wN.js — one set per teaching week.
  exam-prep/           exam_wN.js, satgat_*.js — weekly/legacy exam-prep sets.
  gat-bank/            sim_items_a.js … sim_items_o.js, gat_bank_sim.js, make_gat_week.js,
                       make_gat_course.js, make_mock.js, make_mock_analysis.py.
  saat-bank/           saat_items_a.js … saat_items_m.js, saat_bank_sim.js, balance_saat_d.py.
  sat-bank/            SAT item bank source + the coverage-audit script.
  mawhiba/              build_mawhiba_a1/a2/a3.py and the shared self-checking renderer.
  ap-precalculus/       build_ap_session_schedule_v4.py + sched_full4b.json.

data/                 Machine-readable state — the actual bank contents and progress ledgers.
  banks/                GAT/SAAT/SAT item banks (JSON), kept in sync with the .md summaries
                       in the Claude Project.
  ledgers/              gat_ledger.json, gat_course_ledger.json — what has been issued, to whom.
  skill-maps/            saat_skill_map.js / SAAT Skill Map JSON, GAT classification map.

config/               House-rule constants shared across engines: branding, colour palette,
                       FIKR timing bands, banned-label list, page-fill thresholds (0.78–0.94
                       for a content page, the documented exceptions for short reference pages).

assets/
  logos/                dept_logo.png, cognia_badge.png, school_logo.png.
  templates/             FIKR Lesson Plan Template.docx, Lesson plan 2026.docx, meth_tpl.docx,
                       and any other fixed-format source templates that get filled in place.

docs/
  LESSONS-LEARNED.md    The standing "do not repeat this mistake" list — condensed from the
                       Weekly Work Order Standing Spec's house rules (§0) and every numbered
                       defect found during a QA pass. Read this before touching an engine.
  HOUSE-RULES.md        Branding, typography, four-pillars, FIKR model — the non-negotiables.
  ARCHITECTURE.md        How a request becomes a deliverable: config → engine → build → verify.

scripts/               One-off pipeline utilities not specific to one product.
  pdf_triage.py, ar_pdf_extract.py   Text-layer PDF triage and Arabic extraction pipeline.
  stitch_scroll.py                   Scrolling screen-recording → one tall stitched image.
  shrink_pdf.py, bilevel_pdf.py       Worksheet PDF slimming without visible quality loss.
```

## Working agreement for any session (human or Claude) touching this repo

1. **Read `docs/LESSONS-LEARNED.md` and the relevant `builders/<product>/README.md` first.**
   Every rule there was earned by shipping a broken item, an unreadable label, or a five-page
   worksheet that should have been four.
2. **Engines are config-driven.** Add a new lesson/week/bank part by writing a new config file
   under `builders/`, not by editing an engine — unless the change is a genuine engine bug or
   a new house rule.
3. **Every build that ships an answer runs its verifier.** No exceptions — see
   `verifiers/README.md` for which check applies to which product.
4. **The Claude Project is still the source of truth for decisions, not code.** This repo
   holds engines and data; narrative decisions, standing instructions, and delivered-document
   summaries stay in the Project's `claude/*.md` docs, cross-linked from here where useful.

## Status

Scaffolded 24 Sep 2026. Engines and configs referenced above exist from prior session work but
have not yet been committed here — this structure is the target layout for that migration.
See `docs/MIGRATION.md` for the file-by-file mapping from "built once, in an ephemeral session"
to "lives here, permanently."
