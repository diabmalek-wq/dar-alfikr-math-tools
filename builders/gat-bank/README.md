# builders/gat-bank/

The simulated GAT (Qudurat) item bank and everything that draws weekly/course
material from it. Read `docs/LESSONS-LEARNED.md` (especially "Content sourcing")
before touching any item here.

## What's in this folder

| File(s) | What it is |
|---|---|
| `sim_items_a.js` … `sim_items_o.js` | The bank itself — 15 parts, one skill-and-trick signature (`sig`) per item, no duplicates allowed |
| `gat_bank_sim.js` | The original 100-item simulated bank (5 transcribed departmental sets, rewritten from scratch — see file header for the department-internal sourcing note) |
| `make_gat_week.js` | Draws one or more weekly worksheets from the bank, ETEC-blueprint sampled, against `data/ledgers/gat_ledger.json` so no item repeats across a term |
| `make_gat_course.js` | The 20-week, topic-ordered arrangement of the *same* items — a separate ledger from `make_gat_week.js` so a class can be taught from one arrangement and revised from the other |
| `make_mock.js` | Blueprint-sampled full mocks (ARI 36% / ALG 18% / GEO 18% / DAT 18% / LOG 10%), built so the three mocks share no item |
| `make_mock_analysis.py` | Class analysis workbook for the three mocks — per-student strand profile, per-question facility, and a TEACH flag on any wrong option half the class or more picked |

## Conventions

- **`sig` uniqueness is a build-time guard, not a convention** — the bank refuses
  to build if two items share a skill-and-trick signature. Never remove this
  check (`docs/LESSONS-LEARNED.md`).
- **Every item is original writing.** Sub-skill and trick may come from a
  department-internal transcription source (credited, kept internal — never
  published externally); numbers, names, context and distractors are always
  rewritten. Never source from a live, still-rotating item pool.
- **Contexts are grounded in Saudi settings and SAR** (Pillar 3).
- **The ledger is what makes "no repeat" true.** `data/ledgers/gat_ledger.json`
  (weekly arrangement) and `data/ledgers/gat_course_ledger.json` (course
  arrangement) record every item already issued. Deleting a ledger deletes the
  no-repeat guarantee — keep it beside the bank it tracks.

## Running

```
node make_gat_week.js 6          # Week 6 worksheet + key
node make_gat_week.js 6 7 8      # three weeks at once
node make_gat_week.js --status   # what is used, what is left

node make_gat_course.js          # all twenty weeks
node make_gat_course.js 3 4      # just weeks 3 and 4
node make_gat_course.js --plan   # the coverage table, builds nothing

python3 make_mock_analysis.py
```

## Verification

`verifiers/verify_sim.py` re-derives every answer in the bank independently
(426 items as of the last full run) and is wired into CI
(`.github/workflows/verify.yml`) — it runs on every push. `verifiers/verify_gat.js`
/ `verify_gat2.js` / `audit_gat.js` check a built week's *output* (e.g.
`gat_worksheets.js`) rather than the bank itself, so they're run manually
against that week's build, not in CI (see `docs/ARCHITECTURE.md`).
