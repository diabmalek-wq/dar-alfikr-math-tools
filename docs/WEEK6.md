# Week 6 build notes (Mr Malek Thiab)

Delivered as `DAF_Math_W6.zip` (4 lessons, Mawhiba, SAT, SAAT). Not stored here; rebuild from the files below.

## Lessons
Gr11 6-3 Logarithms, Gr11 6-4 Logarithmic Functions, Gr10 2-1+2 Vertex and Standard Form (one lesson), Gr10 2-3 Factored Form.
- Decks: `builders/lessons/lessons_w6l3.js`, `lessons_w6l4.js`, `lessons_g10q12.js`, `lessons_g10q3.js` via `rebuild.sh`.
- Plans, route sheets, A3 PBLs: `wk6_docs_*.js` + `wk6_common.js`, built by `build_wk6_docs.js`; PBL fill calibrated by `calib_wk6.py` into `pbl_extra.json`.
- Images: `generators/make_math_*`, `make_graphs_*`, `make_math_wk6doc.py` (doc-size equation images).

## Engine fixes (`engines/docs_engine.js`)
- Ruled writing lines need BOTH `bottom` and `between` borders, otherwise Word/LibreOffice merge them into one line.
- 2026/27 plan: page break before "Lesson Integral Parts", smaller table type, no empty Essential Question line, so it stays 2 pages.
- Route sheets: page break before Apply, so each is 2 pages. PBL is 1 A3 page.
- Earlier sheets built with the old engine may lack ruled lines; rebuild them to fix.

## Mawhiba
`builders/mawhiba/make_u2.py`, `build_u2a1.py`: Grade 9 Unit 2 Activity 1 worksheet (3 pp) and teacher key (2 pp).

## SAT / SAAT (Grade 11)
`builders/exam-prep/sat6.py` + `build_sat6.py` (22 items, 4-page paper, key with named tricks) and `saat6.py` + `build_saat6.py` (24 items). Every answer is re-derived in code when the data file runs; answer letters balanced.
Note: house rule 1a puts SAAT in Grade 11 Term 2; both were built on request.
