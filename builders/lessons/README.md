# builders/lessons/

Weekly configs for the FIKR lesson deck, its docx companions, and the pre-session
sheets — one set of files per teaching week. Read `docs/LESSONS-LEARNED.md` and
`docs/HOUSE-RULES.md` before editing or adding a week here.

## What's in this folder

| Pattern | Calls | Produces |
|---|---|---|
| `lessons_wN.js` | `engines/lesson_engine.js` | The 18-slide FIKR deck (`.pptx`) for each lesson that week |
| `wN_docs.js` | `engines/docs_engine.js` | Lesson Plan / Lesson Plan 2026-27 / Classwork / Routes / PBL `.docx` set |
| `presession_wN.js` | `engines/presession.js` | 4-slide / 2-page pre-session material, per grade/track |

Weeks currently built: `w2`, `w3`, `w4`, `w5core`, `w6l3` (lessons/docs);
`w2`, `w3`, `w4` (pre-session).

## Conventions

- **One file per week, never edit the engine.** A new week is a new
  `lessons_wN.js` / `wN_docs.js` / `presession_wN.js`; the engine stays generic.
  See the working agreement in the top-level `README.md`, point 2.
- **Objectives, essential questions, vocabulary, standards, and MPs are quoted
  verbatim** from the curriculum map (e.g. "Curriculum map A2 OBLAS.docx") — never
  paraphrased or merged, per `docs/HOUSE-RULES.md`.
- **Math and figures are referenced, not authored inline** — each config points at
  a generator index (e.g. `"math_w2/_index.json"`, `"graphs_w2/_index.json"`) built
  by the matching `generators/make_math_wN.py` / `make_graphs_wN.py`. Run those
  generators before building the week's deck/docs.
- **Adaptive routing and the Four Pillars are named on the slide**, not just
  implemented — Tierless Differentiation task labels (Practice / Apply /
  Investigate, "Done when…"), the AI-critic role, and the branch logic all live
  in the config, per `docs/HOUSE-RULES.md`.

## Running

```
node lessons_w3.js        # build week 3's FIKR decks
node w3_docs.js            # build week 3's docx set
node presession_w3.js      # build week 3's pre-session sheets
```

## Verification

No dedicated verifier is committed for lesson decks/docs specifically (unlike the
item banks). QA is manual against `docs/LESSONS-LEARNED.md`'s known traps —
page-fill, `keepNext`/`cantSplit`, figure clearance, and the `PLACEHOLDER` string
scan before shipping any built deck.
