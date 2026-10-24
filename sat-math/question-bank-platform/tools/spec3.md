# Task: blind-solve SAT Math questions
Input /home/claude/bank/batches/vNN.json: list of {id, q, opts}. opts null = grid-in (give a number).
Solve every question INDEPENDENTLY, computing with Python (fractions/sympy/numpy) wherever possible. Do NOT open any other files in /home/claude/bank (no out/, gen_*.py, new500.json): the point is an independent check.
Write /home/claude/bank/out/vNN_ans.json: list of {"id", "ans": for MC the option index 0-3 you believe correct, else the number, "ok": true if the question is well posed (unique correct answer, no ambiguity, consistent), "note": short reason if not ok}.
Flag ok=false for ambiguity, two correct options, no correct option, missing info, or an answer that is not a clean gridable number.
