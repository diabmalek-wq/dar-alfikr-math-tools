# builders/saat-bank/

The simulated SAAT (Tahsili) item bank, organised by topic rather than by week —
a question is found by the skill it tests, not by the day it was taught. Read
`docs/LESSONS-LEARNED.md` (especially "Content sourcing") before touching any
item here.

## What's in this folder

| File(s) | What it is |
|---|---|
| `saat_items_a.js` … `saat_items_m.js` | The bank itself, 13 parts by source/topic — see each file's header for its specific source (the 2021 SAAT set, ETEC sample papers, the Arabic teaching book, reasoning/logic, etc.) |
| `saat_bank_sim.js` | The department's SAAT booklet build — assembles the parts into the Grades 11/12 booklet |
| `balance_saat_d.py` | Answer-position balancer for part D specifically — rotates (never shuffles) each option list so the correct answer lands on the least-used letter, and renumbers the trap notes to match; part D's multi-line item layout needs its own balancer separate from the one-line-per-item parts |

## Conventions

- **Same sourcing rules as `builders/gat-bank/`**: sub-skill and trick may come
  from a credited, department-internal or ETEC-official source; stem, numbers,
  options and figures are always original. An item with no valid derivable
  answer is dropped, never repaired.
- **`sig` uniqueness is enforced at build time**, same as the GAT bank — never
  remove the check.
- **Rotation preserves the author's intended option order** — `balance_saat_d.py`
  turns the list, it never shuffles it, so a deliberately-ordered list (e.g.
  2, 4, 6, 8) stays readable after rebalancing.

## Running

```
python3 balance_saat_d.py     # edits saat_items_d.js in place
node saat_bank_sim.js          # build the department SAAT booklet
```

## Verification

`verifiers/verify_saat.py` (with its 12 per-part check modules,
`verify_saat_b.py` … `verify_saat_m.py`, already in `verifiers/`) independently
re-derives every answer — 582 items as of the last full run — and
`verifiers/lint_saat.js` runs the structural/typographic lint (stem punctuation,
option-set sanity, figure references). Both are wired into CI
(`.github/workflows/verify.yml`) and run on every push, staged against this
folder's `saat_items_*.js` and `generators/make_math_saat*.py`.
