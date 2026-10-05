# dar-alfikr-math-tools

Tooling and finished worksheets for Mr Malek Thiab's mathematics work (Dar Alfikr Schools: Grades 9–12, SAT, SAAT/Tahsili, GAT/Qudurat, AP Precalculus) and private tutoring (SAT, Calculus 2, Linear Algebra).

Read `docs/HOUSE-RULES.md` and `docs/LESSONS-LEARNED.md` before changing an engine or a worksheet.

## Where things are

| Folder | What it holds |
|---|---|
| `calculus-2-tutoring/` | Calculus 2 course: `COURSE-MAP-15-WEEKS.md`, one `week-XX/` folder per week (worksheet PDF, with-solutions PDF, markdown source), `tools/` (build scripts), `_staged/` (older source copies) |
| `linear-algebra-tutoring/` | Linear Algebra course: `00-Weekly-Schedule.md`, `week-XX/` source and `week-XX-v2/` current PDFs, `tools/`, `sources/`, `gap-analysis/` |
| `sat-math/` | `9-week-levelup/` (36 level-up PDFs, 36 Plus PDFs, README), `trick-pack/` (Trick Pack 1 A–M, 26 PDFs, README), older Week 1 files |
| `engines/` | Config-driven builders: lesson deck, lesson-plan docs, exam paper, pre-session, deck animation, GeoGebra embed |
| `generators/` | LaTeX, figure and graph generators that feed the engines |
| `builders/` | Per-product configs: `lessons`, `exam-prep`, `gat-bank`, `saat-bank`, `sat-bank`, `mawhiba`, `ap-precalculus` |
| `data/` | Item banks, ledgers and skill maps (JSON) |
| `config/` | Shared house-rule constants: branding, colours, FIKR timing, page-fill limits |
| `assets/` | Logos and fixed-format templates |
| `docs/` | `HOUSE-RULES.md`, `LESSONS-LEARNED.md`, `ARCHITECTURE.md`, `MIGRATION.md`, `WEEK6.md` |
| `scripts/` | One-off PDF and media utilities |

## Current versions (use these)

| Course | Current files |
|---|---|
| Calculus 2 Week 3 | `calculus-2-tutoring/week-03/Week-03-worksheet-with-solutions.pdf` |
| Calculus 2 Week 4 | `calculus-2-tutoring/week-04/Week-04-worksheet.pdf` and `Week-04-worksheet-with-solutions.pdf` |
| Linear Algebra Week 2 | `linear-algebra-tutoring/week-02-v2/` |
| Linear Algebra Week 3 | `linear-algebra-tutoring/week-03-v2/` (fully detailed solutions) |
| SAT Math sessions | `sat-math/9-week-levelup/` (level-up and Plus sheets, worksheet + answers pairs) |
| SAT Trick Pack | `sat-math/trick-pack/` |

Folders without a `-v2` suffix and the `_staged/` folder hold older copies and markdown sources. The old `Week-04-Trigonometric-...md` source in `calculus-2-tutoring/week-04/` has a wrong sign in the problem 8 key; the corrected solution is in `Week-04-worksheet-solutions.md`.

## Rules for tutoring worksheets (SAT, Calculus 2, Linear Algebra)

- English only, no logos, no Saudi context, no hints or cautions, no grey subtitle.
- Label by week and title. Answers version = identical copy of the worksheet with every solution step in green under each problem.
- Never remove questions; more questions is better.
- File names carry chapter number, lesson number, lesson title and file type (for example `Lesson 6-4 Logarithmic Functions presentation`). Deliver PDF, plus .pptx for presentations; no .docx.

## Working agreement

1. Read `docs/LESSONS-LEARNED.md` and the relevant `builders/<product>/README.md` first.
2. Engines are config-driven: add a new week or bank part with a new config under `builders/`, not by editing an engine, unless it is a genuine engine bug or a new house rule.
3. Every build that ships an answer runs its verifier.
4. The Claude Project "Math, Grade 9, 10, 11, 12" holds decisions and standing instructions; this repo holds code, data and tutoring worksheets.

## Status

Updated 3 Oct 2026. Tutoring materials now live in this repo alongside the engines. `docs/MIGRATION.md` still describes the engine migration plan.


## Presentations (Prezi style, from 4 Oct 2026)

All presentations use the Prezi-style design of the Lesson 6-5 Properties of Logarithms deck: a dark journey map of six numbered stations, Morph zoom transitions into a top breadcrumb, light content slides with rounded white cards, and typeset math images. FIKR decks keep the 60-minute structure (Diagnose 6, Targeted Instruction 18, Practice 12, Production 12, Mastery Gate 6, Smart Production 6). Mawhiba activity decks are student-run and not FIKR.

Engine: engines/prezi/ (engine.js builds a deck from one lesson config; build.sh renders the math, builds, injects Morph, validates and makes a contact sheet; BRIEF.md is the authoring brief). Lesson configs: builders/lessons/prezi/cfg/ with figures in builders/lessons/prezi/figs/. Finished Week 6 decks (pptx and PDF): presentations/week-06/.

To add a lesson: write builders/lessons/prezi/cfg/ID.json (see _example_L2-4_abridged.json and BRIEF.md), run validate_cfg.py, then build.sh ID. Objectives, vocabulary and standards are quoted verbatim; never invent essential questions or practices.
