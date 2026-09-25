# builders/exam-prep/

Weekly and combined exam-prep worksheet configs — one file per week or per
grade/week combination. Read `docs/LESSONS-LEARNED.md` and `docs/HOUSE-RULES.md`
before editing or adding a set here.

## What's in this folder

| Pattern | Calls | Produces |
|---|---|---|
| `exam_wN.js` | `engines/exam_engine.js` | GAT + SAAT exam-prep paper and answer key for that week, per the GAT & SAAT Classification Map |
| `satgat_gXXwN.js` | `engines/exam_engine.js` | Combined SAT + GAT worksheet for one grade/week — split into an SAT half and a GAT half by a section band |

Built so far: `exam_w2` (GAT + SAAT); `satgat_g10w2`…`w5`, `satgat_g11w2`,
`satgat_g11w3` (SAT + GAT, by grade).

## Conventions

- **Coverage is spiral, not local.** The week's lesson is the anchor, but every
  set also seeds topics not yet taught, off the term coverage grid — never chosen
  ad hoc. See the comment block at the top of `satgat_g10w2.js` for the exact
  reasoning.
- **Answer-letter balance is enforced in code**, not by hand — GAT options are
  ordered by value (matching the real paper), SAAT/expression options are
  rotated to a balanced key so no letter is eliminable by pattern.
- **SAT half follows the digital-SAT domain weights** (Algebra ~35%, Advanced
  Math ~35%, Problem-Solving & Data Analysis ~15%, Geometry & Trigonometry ~15%);
  **GAT half follows the paper's own strand mix.**
- **No leaked or circulated exam questions are used** — every item is written
  against the ETEC framework in the Classification Map (`docs/LESSONS-LEARNED.md`,
  "Content sourcing").
- **Every exam-prep item carries a named trick**, printed only in the key, per
  `docs/LESSONS-LEARNED.md`'s house rules.

## Running

```
node exam_w2.js
node satgat_g10w3.js
```

## Verification

`verifiers/audit_pair.js` and `verifiers/validate_set.js` check a built set's
structure (trick↔item binding, option counts, stem/why/traps completeness) — run
against the built output module, e.g. `node ../../verifiers/audit_pair.js
./exam_w2.js`. Page-count is measured, never assumed — exam-prep student papers
must be exactly 4 pages (`docs/LESSONS-LEARNED.md`).
