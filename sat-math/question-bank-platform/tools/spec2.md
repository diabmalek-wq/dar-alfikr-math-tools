# Task: write NEW SAT Math questions modelled on bank items (tricky Bluebook style)
Input: /home/claude/bank/batches/nNN.json: items with src_id, domain, skill, sub (subtopic), lv, src_q/src_opts/src_key/src_spr (original), first_rewrite (an earlier rewrite), mis (misconception notes).
Output: /home/claude/bank/out/nNN.json, JSON list, same order, one object per item:
{"id": src_id + "-2", "src": src_id, "lv": "M"|"H", "mc": bool, "domain","skill","sub" (copy), "q": stem, "opts": 4 strings (MC only), "key": 0-3 index (MC) OR numeric answer (SPR), "disp": LaTeX of SPR answer without $ (SPR only), "steps": 3-4 strings}
## Rules
1. Same skill, subtopic and cognitive demand as the source, but a genuinely NEW problem: different numbers, a new context and a new twist. It must not resemble src_q or first_rewrite. It may have a different answer. Keep MC/SPR format of the source (src_opts null means SPR).
2. SAT-tricky: extra step, asks for a different quantity than the obvious one, units/percent traps, "must be true / NOT", equivalent-form disguise, parameter conditions.
3. Compute the answer in Python (fractions/numpy) for EVERY item and assert it before writing; keep your script as /home/claude/bank/gen_nNN.py. SPR answers must be a single number (or exact fraction/decimal) with a definite unique answer. No ambiguous wording, no questions with two correct options, no figure or table dependence (state data in words; HTML tables not allowed).
4. MC: 3 distractors each from a real named misconception (sign error, partial step, forgot to divide, percent vs percentage point...). All four options distinct and plausible. Put the correct option at index (item position starting at 1) mod 4.
5. All math in LaTeX inside $...$ (\dfrac, \sqrt, \le). No plain-text math, no \par, no \\, no \$ (write SAR or "dollars" as words), no em dashes, no emojis.
6. Saudi/Vision 2030 contexts (SAR, Jeddah, Makkah, NEOM, Red Sea, Riyadh Metro, football, solar) where natural; pure math is fine for abstract skills.
7. steps: Desmos-first. What to type in <code>..</code>, what it returns, algebra check, the trap. 3-4 short strings.
8. Hard (lv H) must need 3+ steps; Medium 2 steps. Keep the source's lv unless the new problem is clearly harder.
