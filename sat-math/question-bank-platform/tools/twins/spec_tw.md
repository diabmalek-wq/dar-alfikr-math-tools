# Task: write a rephrased, trickier TWIN for each bank item (digital SAT Math)
Input: /home/claude/tw/b/tNN.json (list). Each item: src_id, domain, skill, sub, lv, mc, src_q, src_opts (MC) or null, src_key, src_spr.
Output: /home/claude/tw/out/tNN.json: JSON list, SAME ORDER, one object per input item:
{"id": src_id+"-2", "lv": "M"|"H", "mc": bool, "domain","skill","sub" (copy exactly), "q": stem, "opts": 4 strings (MC only), "key": 0-3 index (MC) OR numeric answer (SPR), "disp": LaTeX of the SPR answer without $ (SPR only), "steps": 3-4 strings}
Do NOT open any other file in /home/claude/tw/out. Keep your script as /home/claude/tw/gen_tNN.py.
## Rules
1. Same skill, subtopic, format (MC/SPR) and cognitive demand as the source, but a genuinely NEW problem: different numbers, a new context, and a fresh SAT-style trick. It must not resemble src_q in wording or numbers. The answer should differ from the source's.
2. SAT-tricky: extra step, asks for a different quantity than the obvious one, units or percent traps, "must be true / NOT", equivalent-form disguise, parameter conditions, partial-step answers as distractors.
3. For EVERY item compute the answer in Python (fractions/math/numpy; sympy is NOT installed) and assert it. For MC also assert each distractor is wrong. SPR: one definite gridable number (at most 5 characters if positive, 6 if negative; exact fraction or decimal). No ambiguity, no two correct options, no figure or table dependence (state data in words).
4. MC: 3 distractors each from a named real misconception. All four options distinct and plausible. Put the correct option at index (item position in your output list, starting at 1) mod 4.
5. All math in LaTeX inside $...$ (\dfrac, \sqrt, \le). No plain-text math, no \par, no \\, no \$ (write SAR or "dollars" in words), no em dashes, no emojis, no markdown tables, no figures.
6. Saudi/Vision 2030 contexts (SAR, Jeddah, Makkah, NEOM, Red Sea, Riyadh Metro, football, solar) where natural; pure math is fine for abstract skills.
7. steps: Desmos-first. What to type in <code>..</code>, what it returns, the algebra check, the trap. 3 to 4 short strings.
8. Hard (H) needs 3+ steps; Medium 2 steps. Keep the source lv unless clearly harder.
9. Validate before finishing: python3 /home/claude/tw/validate_tw.py /home/claude/tw/out/tNN.json must print BAD 0. Fix and rerun until it does.
10. Final reply: one line only ("tNN done, N items").
