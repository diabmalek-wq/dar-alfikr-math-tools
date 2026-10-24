# Task: rewrite SAT Math bank items in tricky Bluebook style
Input: /home/claude/bank/batches/bNN.json (40 items: id, domain, skill, diff, q, opts, key(index for MC), spr, key_num, rat, mis).
Output: /home/claude/bank/out/bNN.json — a JSON list, same order, one object per item:
{"id": same id, "lv": "M"|"H" (from diff), "mc": bool, "domain":..., "skill":... (copy),
 "q": new stem, "opts": 4 strings (MC only, else omit), "key": 0-3 index (MC) OR the numeric answer (SPR),
 "disp": LaTeX of SPR answer without $ (SPR only), "steps": 3-4 strings}
## Rewrite rules
1. DO NOT copy. New context (Saudi: SAR, Jeddah/Makkah, NEOM, Red Sea, solar, Riyadh Metro, football; or pure math), new numbers where possible, new surface form, SAT-tricky: extra step, a rephrased condition, inverse/"which is NOT", ask for a different quantity (e.g. 2x instead of x, the y-intercept instead of slope), units/percent traps, "must be true", equivalent-form disguise.
2. The FINAL ANSWER MUST BE THE SAME VALUE as the original key (MC: the correct option text value equals original correct option's value; SPR: key equals key_num). Build a new problem whose answer is that value, or keep the same numbers but change the framing. Verify by computing in python (numpy/fractions) for every item before writing. If you cannot hold the answer fixed, keep the original numbers and only reframe.
3. Distractors: 3 wrong options each from a real misconception (use `mis` field; sign error, partial step, forgot to divide by 2, percent vs. percentage point, etc.). Put the correct one at position (index) = (item number in batch) mod 4 so keys are balanced. Options must be distinct.
4. All math in LaTeX with $...$ (\dfrac, \sqrt, \le). No plain-text math. No markdown tables, no figures: if the original relies on a table or figure that cannot be put in words, describe the data in a sentence ("x=2 gives 11, x=5 gives 20"); if truly impossible without a picture, keep the item but state all coordinates/lengths in words.
5. SPR answers must be gridable (≤5 chars positive, ≤6 negative, a fraction or decimal). 
6. steps: Desmos-first. Say what to type, in <code>..</code> (Desmos syntax: sqrt(), ^, pi), what it returns, then the algebra check and the trap, 3-4 short strings with inline $..$ math.
7. Keep difficulty (lv) as original or one level harder. Do not mention "original".
8. No emojis, no em dashes. Valid JSON (escape backslashes as \\).
