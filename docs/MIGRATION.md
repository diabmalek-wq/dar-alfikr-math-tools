# Migration plan — from "rebuilt each session" to "lives in this repo"

Status: **done**, except two items intentionally skipped (see below) and one item that
isn't a script yet. Completed 25 Sep 2026, verified file-by-file (byte-for-byte diff
against the source workspace) after every commit.

| Known from session history | Target path | Status |
|---|---|---|
| `lesson_engine.js` | `engines/lesson_engine.js` | ✅ migrated |
| `docs_engine.js` | `engines/docs_engine.js` | ✅ migrated |
| `exam_engine.js` | `engines/exam_engine.js` | ✅ migrated |
| `presession.js`, `build_presession.js` | `engines/presession.js` | ✅ migrated |
| `animate_deck.py` | `engines/animate_deck.py` | ✅ migrated |
| `embed_geogebra.py`, `build_geogebra_clip.py` | `engines/embed_geogebra.py` | ✅ migrated |
| `make_math_*.py`, `make_figs_*.py`, `make_graphs_*.py` | `generators/` (keep the per-week/part suffix, e.g. `make_math_w3.py`) | ✅ migrated (74 files) |
| `figlabel.py` | `generators/figlabel.py` | ✅ migrated |
| `verify_sim.py`, `verify_saat*.py`, `verify_gat*.js` | `verifiers/` | ✅ migrated |
| `validate_set.js`, `audit_pair.js`, `audit_gat.js`, `lint_saat.js` | `verifiers/` | ✅ migrated |
| `measure_rev.py`, `calibrate_pbl.py` | `verifiers/` | ✅ migrated |
| `lessons_wN.js`, `wN_docs.js`, `presession_wN.js` | `builders/lessons/` | ✅ migrated (12 files: w2–w6l3) |
| `exam_wN.js`, `satgat_*.js` | `builders/exam-prep/` | ✅ migrated (7 files) |
| `sim_items_a.js` … `sim_items_o.js`, `gat_bank_sim.js`, `make_gat_week.js`, `make_gat_course.js`, `make_mock.js`, `make_mock_analysis.py` | `builders/gat-bank/` | ✅ migrated |
| `saat_items_a.js` … `saat_items_m.js`, `saat_bank_sim.js`, `balance_saat_d.py` | `builders/saat-bank/` | ✅ migrated |
| SAT item bank source (currently a project doc, not a script — see below) | `builders/sat-bank/` once scripted | ⏳ not started — still only exists as a Claude Project doc, not a script; nothing to migrate until a session turns it into one |
| `build_mawhiba_a1/a2/a3.py` | `builders/mawhiba/` | ✅ migrated |
| `build_ap_session_schedule_v4.py`, `sched_full4b.json` | `builders/ap-precalculus/` | ✅ migrated |
| `gat_ledger.json`, `gat_course_ledger.json` | `data/ledgers/` | ✅ migrated |
| `GAT Bank — 426 items (machine readable).json` | `data/banks/` | ✅ migrated |
| `SAAT Skill Map — 135 sessions.json`, `saat_skill_map.js`, `saat_skill_map.json`, `GAT_SAAT_Classification_Map_Sem1_2026-27.docx` | `data/skill-maps/` | ✅ migrated |
| `dept_logo.png`, `cognia_badge.png`, `school_logo.png` | `assets/logos/` | ✅ migrated |
| `meth_tpl.docx` | `assets/templates/` | ✅ migrated |
| `FIKR Lesson Plan Template.docx`, `Lesson plan 2026.docx` | `assets/templates/` | ⏭️ skipped — no source binary exists locally; `Lesson plan 2026.docx` survives only as extracted table content in the Claude Project, and `FIKR Lesson Plan Template.docx` wasn't found as a distinct file anywhere (only hundreds of per-lesson *filled* deliverables). Revisit if either turns up, or reconstruct deliberately rather than guess. |
| `pdf_triage.py`, `ar_pdf_extract.py`, `stitch_scroll.py`, `shrink_pdf.py`, `bilevel_pdf.py` | `scripts/` | ✅ migrated |
| — | `config/` | ⏭️ skipped — no dedicated config file ever existed; house-rule constants (branding, colour palette, FIKR timing bands, page-fill thresholds) are hardcoded inline inside each engine, not factored into a shared module. Populating this is a real refactor, not a migration — do it deliberately in its own session if/when it's worth the risk of touching working engines. |

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

## What's left

- **SAT item bank**: still lives only as a Claude Project doc. Migrate once it's turned into
  an actual `builders/sat-bank/` script, per the table above.
- **`config/`**: intentionally empty. Extracting the inline constants from the engines into a
  shared config module is a deliberate follow-up task, not something to do incidentally.
- **`assets/templates/`**: missing the two blank lesson-plan templates (see table above) —
  attach the real `.docx` files here (or a session with local-file access) if they turn up.
- Every other row in this table is committed to `main` and was verified with a fresh
  `git clone` + byte-for-byte `diff` against its source immediately after each commit.
