# Task: pick worthy SAT Math questions from a 2016 prep book and write NEW original questions modelled on them
Source PDF (read page IMAGES with the Read tool, `pages` parameter, max 20 pages per call; the text layer garbles math):
/root/.claude/uploads/56214d6e-9327-5adb-98f6-b897111d58bd/32999a31-SAT-Quantitative-Question-Bank.pdf
Your chunk (question numbers and PDF pages) is given in your prompt. Answer key (letter or number per question) is in /home/claude/mr/key.json (use it only to make sure you understood the source problem).
Do NOT open any file in /home/claude/bank/out or /home/claude/bank/new500.json.

## Step 1: choose
Read your pages. For EACH question number in your chunk decide WRITE or SKIP. WRITE only if the question is worthy:
 - relevant to the DIGITAL SAT Math (Algebra, Advanced Math, Problem-Solving and Data Analysis, Geometry and Trigonometry);
 - Medium or Hard, needs 2+ steps, has a clear SAT trap (sign error, partial step, units, percent vs percentage point, wrong quantity asked, "must be true / NOT");
 - priority to THIN subtopics in our bank (count in brackets): Polynomial division and remainder [4], Solving by substitution or elimination [4], Other area and volume problems [2], Surface area and scaling [6], Circle measurements [8], Other trigonometry [6], Sample estimates and populations [7], Data displays and distributions [4], Spread: range and standard deviation [3], Basic and compound probability [10], Equations with constants and parameters [9], Slope and graph features [11], Compound and absolute value inequalities [13], Congruence and special triangles [11], Inscribed angles and chords [10], Margin of error and confidence [19], Conditional probability and two-way tables [19], Radical and rational equations [14].
SKIP if: complex numbers, permutations or combinatorics counting, pure arithmetic or one-step, depends on a printed graph/table/figure you cannot restate fully in words, off the digital SAT, or ambiguous/erroneous in the book. Aim to WRITE roughly 8 to 12 of your 25 questions. Quality over quantity.

## Step 2: write (one new item per WRITE question)
Output /home/claude/mr/out/<chunkid>.json (JSON list) and /home/claude/mr/out/<chunkid>_skip.json (list of {"q": number, "why": short reason}). Every question number of your chunk must appear exactly once across the two files.
Item object: {"id": "MR-" + 3-digit question number, "src_q": number, "lv": "M"|"H", "mc": bool, "domain","skill","sub" (EXACT strings from the taxonomy below), "q": stem, "opts": 4 strings (MC only), "key": 0-3 index (MC) OR numeric answer (SPR), "disp": LaTeX of the SPR answer without $ (SPR only), "steps": 3-4 strings}
## Rules
1. Genuinely NEW problem: same skill and cognitive demand as the book question, but different numbers, new context and a new twist. Never copy the book's wording or numbers. Do not mention the book.
2. SAT-tricky: extra step, asks for a different quantity than the obvious one, units/percent traps, "must be true / NOT", equivalent-form disguise, parameter conditions.
3. Compute the answer in Python (fractions/sympy/numpy) for EVERY item and assert it before writing; keep the script as /home/claude/mr/gen_<chunkid>.py. SPR answers: one definite number (exact fraction or decimal), gridable (at most 5 characters if positive, 6 if negative). No ambiguity, no two correct options.
4. MC: 3 distractors, each from a real named misconception. All four options distinct and plausible. Put the correct option at index (position of the item in your output list, starting at 1) mod 4.
5. All math in LaTeX inside $...$ (\dfrac, \sqrt, \le). No plain-text math. No \par, no \\, no \$ (write SAR or "dollars" in words), no em dashes, no emojis, no markdown tables, no figures: state all data in words or a sentence.
6. Saudi/Vision 2030 contexts (SAR, Jeddah, Makkah, NEOM, Red Sea, Riyadh Metro, football, solar) where natural; pure math is fine.
7. steps: Desmos-first. What to type in <code>..</code> (Desmos syntax: sqrt(), ^, pi), what it returns, the algebra check, the trap. 3-4 short strings.
8. Hard (lv H) needs 3+ steps; Medium 2 steps.
## Taxonomy (domain | skill | sub), use exactly
Advanced Math | Equivalent expressions | Exponents and radicals / Factoring and expanding / Polynomial division and remainder / Rational expressions
Advanced Math | Nonlinear equations and systems | Exponential and other equations / Linear-nonlinear and nonlinear systems / Quadratic equations and discriminant / Radical and rational equations
Advanced Math | Nonlinear functions | Exponential growth and decay / Function transformations and notation / Polynomial and rational function graphs / Quadratic functions and vertex form
Algebra | Linear equations in one variable | Equations with constants and parameters / Number of solutions (none or infinite) / Solving and rearranging / Word problems and writing equations
Algebra | Linear equations in two variables | Graphs and points on lines / Intercepts and slope from an equation / Parallel and perpendicular lines / Writing and interpreting models
Algebra | Linear functions | Evaluating and transforming linear functions / Interpreting slope and intercept in context / Slope and graph features / Writing a linear function
Algebra | Linear inequalities | Compound and absolute value inequalities / Inequality word problems / Solving and solution sets / Systems of inequalities
Algebra | Systems of linear equations | Finding a value from the solution / No solution or infinitely many solutions / Solving by substitution or elimination / Word problems with systems
Geometry and Trigonometry | Area and volume | Area of plane figures / Other area and volume problems / Surface area and scaling / Volume of solids
Geometry and Trigonometry | Circles | Arc length and sector area / Circle measurements / Equation of a circle / Inscribed angles and chords / Tangent lines
Geometry and Trigonometry | Lines, angles, and triangles | Congruence and special triangles / Other triangle problems / Parallel lines and angle relationships / Similar triangles
Geometry and Trigonometry | Right triangles and trigonometry | Other trigonometry / Pythagorean theorem applications / Sine, cosine, tangent ratios / Special right triangles
Problem-Solving and Data Analysis | Inference and margin of error | Margin of error and confidence / Sample estimates and populations
Problem-Solving and Data Analysis | One-variable data | Data displays and distributions / Mean, median and mode / Spread: range and standard deviation
Problem-Solving and Data Analysis | Percentages | Percent change and growth / Percent of a quantity and parts
Problem-Solving and Data Analysis | Probability | Basic and compound probability / Conditional probability and two-way tables
Problem-Solving and Data Analysis | Ratios, rates and units | (check list below)
Problem-Solving and Data Analysis | Statistical claims and studies | (check list below)
Problem-Solving and Data Analysis | Two-variable data and scatterplots | (check list below)
For the last three skills use the sub strings found in /home/claude/repo/qb/tools/subtopic_counts.md (read that file for their exact subtopic names).
