# SAT Aceit question-bank platform

Single-file Bluebook-style SAT Math practice platform (Mr Malek Thiab, Dar Al-Fikr). Live: https://acesat.pages.dev

- **1,646 questions**: 1,146 rephrased from the verified bank + 500 new variants (ids ending `-2`). Every key checked in code; the 500 new items were also solved blind by an independent pass.
- **Three-level topics**: domain > skill > subtopic (e.g. Geometry > Circles > Tangent lines). The builder filters at any level.
- **Builder**: topics, difficulty, format, length, balanced SAT weights, seeded random draw, share link (`#x=`), single-exam export.
- **Exam**: Bluebook look, Desmos (graphing + scientific), reference sheet, keypad, 40-point expected-score band, review with Desmos-first solutions.

## Build
```
DESMOS_API_KEY=xxxx python3 build.py      # writes dist/index.html, _headers, robots.txt
```
Deploy `dist/` to Cloudflare Pages (zip with files at the root, or drag the folder). The Desmos key is never committed.

## Layout
| Path | Purpose |
|---|---|
| `tpl_src.html` | exam shell (UI, KaTeX + MathML fallback, calculators, scoring) |
| `mkbank.py` | patches the shell into the builder app (topic tree, draw logic, export) |
| `results_bank.js` | score band + results page |
| `bld.css` | builder styles |
| `subtopics.py` | subtopic taxonomy and keyword rules |
| `data/bank_all.json` | the 1,646 questions: `id, domain, skill, sub, lv (M/H), mc, q, opts, key, disp, steps` |
| `data/orig.json` | parsed source bank (used to check answers) |
| `tools/` | question-writing specs (`spec*.md`), `validate.py`, source parser |

## Adding questions
Append items to `data/bank_all.json` (unique `id`, valid `domain|skill|sub`), keep math in `$...$` LaTeX, no `\par`/`\$`/tables, verify the key in code, then run `build.py`. Rules: answer keys computed in Python, distractors from named SAT traps, correct option spread over A-D, steps Desmos-first.

## Notes
- Keys are in the page: for practice, not graded/secure exams.
- Subtopic labels on the original 1,146 items come from keyword rules (`subtopics.py`) and may need manual fixes.
