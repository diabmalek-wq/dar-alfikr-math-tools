# builders/mawhiba/

Redesigned Mawhiba Grade 9, Unit 1 (Linear Equations) activities. Each file is a
full rebuild of one source activity sheet — not a template, a specific,
independently-checked redesign.

## What's in this folder

| File | What it is |
|---|---|
| `build_mawhiba_a1.py` | Activity 1 — worksheet (2 pages, student-facing, nothing pre-answered) + key (1 page, teacher-facing, separate file). The source ran to 4 pages and printed answers in the student's own justification column. |
| `build_mawhiba_a2.py` | Activity 2 — rebuilds working space sized to each task, disambiguates the source's unlabelled figure, and states the mathematical point (that several dissections of one rectangle simplify to the same expression — an identity) explicitly instead of leaving it implied. |
| `build_mawhiba_a3.py` | Activity 3 — Number Pyramids, compressed to 2 pages (worksheet) + 1 page (key). Every pyramid total in the file's header comment is independently re-derived, not copied from the source. |

## Conventions

- **Content and numbers are the source book's own** (Student Book + Teacher's
  Guide, Unit 1 Activity 3, etc.) — **independently re-derived and checked**, not
  copied from the source's stated answers. See each file's header for the
  worked re-derivation.
- **Objectives, assessment criteria, routes, and "Done when…" are always
  present** — the source sheets often lacked these; the redesign adds them per
  the Tierless Differentiation pillar (`docs/HOUSE-RULES.md`).
- **Self-checking is inline, not a separate verifier**: each build script asserts
  its own page-fill and spill/gap bounds before it ships (e.g.
  `assert o["spill"] <= 1`, `assert o["gap"] >= 4` in `build_mawhiba_a1.py`) —
  the build itself fails loudly rather than shipping an overflowing page.
- **Branding follows the current house rule** — department logo, Cognia badge,
  school logo, motto footer (`docs/HOUSE-RULES.md`, `docs/Branding` note).
- A fourth activity (`build_mawhiba_a4.py`) exists in the pre-migration
  workspace but was **deliberately not migrated** — see `docs/MIGRATION.md`.

## Running

```
python3 make_math_maw1.py && python3 build_mawhiba_a1.py
```

Each build script depends on its matching `generators/make_math_mawN.py` run
first, for the rendered math it places on the page.

## Verification

No dedicated verifier folder entry — QA is the inline self-check described
above, plus the manual page-fill/last-ink-above-footer measurement pattern in
`docs/LESSONS-LEARNED.md` (target 0.78–0.94, short reference pages excepted).
