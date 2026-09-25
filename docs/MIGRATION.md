# Migration plan — from "rebuilt each session" to "lives in this repo"

Status: not started. This is the target mapping for the next session that has time to do it.

| Known from session history | Target path |
|---|---|
| `lesson_engine.js` | `engines/lesson_engine.js` |
| `docs_engine.js` | `engines/docs_engine.js` |
| `exam_engine.js` | `engines/exam_engine.js` |
| `presession.js`, `build_presession.js` | `engines/presession.js` |
| `animate_deck.py` | `engines/animate_deck.py` |
| `embed_geogebra.py`, `build_geogebra_clip.py` | `engines/embed_geogebra.py` |
| `make_math_*.py`, `make_figs_*.py`, `make_graphs_*.py` | `generators/` (keep the per-week/part suffix, e.g. `make_math_w3.py`) |
| `figlabel.py` | `generators/figlabel.py` |
| `verify_sim.py`, `verify_saat*.py`, `verify_gat*.js` | `verifiers/` |
| `validate_set.js`, `audit_pair.js`, `audit_gat.js`, `lint_saat.js` | `verifiers/` |
| `measure_rev.py`, `calibrate_pbl.py` | `verifiers/` |
| `lessons_wN.js`, `wN_docs.js`, `presession_wN.js` | `builders/lessons/` |
| `exam_wN.js`, `satgat_*.js` | `builders/exam-prep/` |
| `sim_items_a.js` … `sim_items_o.js`, `gat_bank_sim.js`, `make_gat_week.js`, `make_gat_course.js`, `make_mock.js`, `make_mock_analysis.py` | `builders/gat-bank/` |
| `saat_items_a.js` … `saat_items_m.js`, `saat_bank_sim.js`, `balance_saat_d.py` | `builders/saat-bank/` |
| SAT item bank source (currently a project doc, not a script — see below) | `builders/sat-bank/` once scripted |
| `build_mawhiba_a1/a2/a3.py` | `builders/mawhiba/` |
| `build_ap_session_schedule_v4.py`, `sched_full4b.json` | `builders/ap-precalculus/` |
| `gat_ledger.json`, `gat_course_ledger.json` | `data/ledgers/` |
| `GAT Bank — 426 items (machine readable).json`, `SAAT Skill Map — 135 sessions.json` | `data/banks/` and `data/skill-maps/` (mirror the copies already kept in the Claude Project — treat the Project copy as canonical for now, this repo's copy as a working mirror, until the two are reconciled) |
| `dept_logo.png`, `cognia_badge.png`, `school_logo.png` | `assets/logos/` |
| `FIKR Lesson Plan Template.docx`, `Lesson plan 2026.docx`, `meth_tpl.docx` | `assets/templates/` |
| `pdf_triage.py`, `ar_pdf_extract.py`, `stitch_scroll.py`, `shrink_pdf.py`, `bilevel_pdf.py` | `scripts/` |

## How to do the migration

Each of these files currently only exists inside a session's ephemeral cloud workspace at the
moment it was last built or edited — none of them have been committed anywhere permanent yet.
The practical path:

1. Next time a session already has one of these files open in its workspace (e.g. because a
   new lesson/bank part is being built), commit it into this repo at the target path above
   instead of leaving it in the throwaway container.
2. Once a handful of the core engines (`lesson_engine.js`, `exam_engine.js`, `docs_engine.js`,
   `gat_bank_sim.js`) are committed, future sessions can `git clone` this repo at the start of
   a build instead of reconstructing engines from the Weekly Work Order narrative — that's
   the token saving this repo exists for.
3. Data files (`data/`) should be treated as the working copy; the `.md`/`.json` summaries
   already living in the Claude Project remain the human-readable source of truth until a
   session explicitly reconciles the two and this note is updated.
