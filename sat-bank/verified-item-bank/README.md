# SAT Verified Item Bank (1,078 items)

Single combined bank: house items, teacher-supplied items, gap-closing batches (§2.30–§2.39), web-research batches (§2.37, §2.38, §2.40 Trick Pack 2) and the 200 Trick Pack 1 challenge items. House-authored, archetype-only; no College Board text reproduced. Every answer is verified by script.

- `SAT_Bank_Verified_Item_Bank.md` — the bank (section index, bank summary, full index).
- `Gap_Analysis_vs_College_Board_Export.md` — coverage vs the 611 Hard Math items of the official export.
- `generators/` — item scripts and assembly scripts; `dedupe.py` screens new items against the bank for repeated wording and tricks.

Domain mix: Algebra 325 (30.1%), Advanced Math 321 (29.8%), Geometry and Trigonometry 257 (23.8%), Problem-Solving and Data Analysis 175 (16.2%).
Caveat: the 200 Trick Pack skill labels were assigned by content and need a spot-check; §2.35 was deduplicated (10 repeated items removed, IDs not renumbered).


Update 21 Oct 2026: §2.40 Trick Pack 2 adds 84 items (A-316–A-335, AM-303–AM-321, GT-232–GT-257, PS-157–PS-175); generators `batch40.py` and `gen40.py`. Worksheet and answers PDFs are in `sat-math/trick-pack-2/`.
