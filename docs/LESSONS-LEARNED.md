# Lessons learned — read before touching any engine

Condensed from the Weekly Work Order Standing Spec's house rules and every numbered defect
found during a QA pass, across all products. Full narrative history stays in the Claude
Project; this file is the checklist, not the story.

## House rules (never violate these)
- English only, unless explicitly asked for Arabic.
- Standards/CCSS codes: bottom corner only, code form, never a full-text badge.
- Never label students by ability. Task routes only: Practice / Apply / Investigate,
  "Done when…" not "Success:".
- Quote curriculum-map objectives verbatim. Never paraphrase, merge, or invent standards.
- Teacher of record on every deliverable: Mr Malek Thiab (never a colleague's name, even if
  a source syllabus lists someone else).
- PBL project sheets: A3, one page. Exam-prep student papers: exactly 4 pages, measured with
  `pdfinfo`, never assumed. Every exam-prep item carries a named trick, printed only in the
  key.

## Build-time guards that must never be removed
- **`sig` uniqueness** on every item bank — the build throws on a duplicate skill signature.
- **Figure label placement** (`figlabel.py`) — refuses to ship a label sitting on the drawing.
- **A figure that carries an answer asserts that answer in its own drawing code** before it
  renders. Caught real defects every time it's been added retroactively — never skip it on a
  new figure.
- **Tricks bind to items by original source number, parsed from the item's own reasoning —
  never by array position.** A positional array has silently drifted trick↔item bindings at
  least twice historically.
- **Independent re-derivation in Python for every answer**, never by re-stating the item's own
  reasoning. Bugs this has caught: two correct answers on one item, a figure disagreeing with
  its own key, a float-precision trap, a geometry item unsolvable as drawn.

## Known traps, by category

**Page layout / Word & LibreOffice**
- Consecutive paragraphs with an identical border MERGE into one visual line — alternate the
  left indent by one twip to break it.
- Never assume page fill — measure last-ink-above-footer and target 0.78–0.94 (short
  reference/key pages are a documented, deliberate exception, not a bug).
- `keepNext` / `cantSplit` on every stem+options block — without it, stems orphan at page ends
  and two-way tables split across pages.
- Typeset math option width: too wide for 4-across → 2-across → stop the build. Never let text
  clip at a cell edge.

**Figures / matplotlib**
- `graphW ÷ aspect` must leave clearance above the bottom bar, or a tall graph runs off the
  slide.
- Label size must be set for the PRINTED width, not the source width — a figure shrunk on
  placement halves its label size unless sized for the target.
- `fig.text(wrap=True)` wraps against the whole figure width, not the panel — wrap by hand
  when a figure sits inside a smaller panel.
- Deleting a shape can leave its backing rectangle behind — check for and remove orphaned
  shapes at the same coordinates.

**PowerPoint animation**
- The worked-example "table" must stay individual shapes, never a real pptx table, or
  PowerPoint animates it as one object and row-by-row reveal becomes impossible.
- `embed_geogebra.py` (or any shape-adding step) must run AFTER `animate_deck.py`, never
  before — otherwise the new shape gets swept into an existing click group.
- Scan every `ppt/slides/slideN.xml` for the literal string `PLACEHOLDER` before shipping —
  cheap, and has caught six live decks with a leftover URL on screen.

**Content sourcing**
- Department-internal transcription banks (a colleague's own shared practice set) are
  credited to them and kept inside the department, never published externally.
- From a recall booklet or any circulated source: take the SKILL and TRICK only — never the
  stem, numbers, option list, or figure. Audit the source too; an item with no valid answer
  is dropped, not repaired.
- Never source from a live, still-rotating item pool (e.g. a computerised-sitting leak dated
  the same evening as its sitting) — the simulate-don't-copy argument doesn't reach a pool
  still in circulation.

**PDF / text extraction**
- Triage every PDF first (`pdf_triage.py`) — a text-layer PDF costs ~1/10th what an image-page
  extraction costs.
- Arabic extraction needs `-raw` (keeps blocks together) with token order reversed on Arabic
  lines — `-layout` alone interleaves columns, `-raw` alone reads Arabic backwards.

**File delivery**
- The Drive connector CAN transfer binary files (`base64Content` + `contentMimeType`), but
  cost is real: ~20 KB is the practical ceiling for connector upload; anything larger goes to
  the user directly or waits for a linked-computer session.
