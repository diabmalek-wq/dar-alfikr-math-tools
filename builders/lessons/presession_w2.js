// Week 2 pre-session sheets — Mawhiba G9, SAT & GAT G10, SAT & GAT G11, GAT G12.
// Each names the exact checklist codes its session covers, so the coverage
// workbook and the classroom material stay in one language.
const { build } = require("./presession");

// =====================================================================
// GRADE 12 · GAT · Week 2 — the ONLY paced programme, because the sitting
// is 27-31 December. The checklist has ARI.1 and ARI.2 planned for this week.
// =====================================================================
build({
  who: "Grade 12 GAT",
  out: "PreSession_Gr12_GAT_W2.docx",
  headerLine: "Grade 12 · GAT (Qudurat) · Week 2 · read this BEFORE Monday's session",
  title: "Pre-Session Skills Sheet — Number Sense",
  sub: "Classes 12A and 12B · the sitting is 27–31 December, so every week counts once. "
     + "Ten minutes on this page saves twenty in the room.",
  covers: [
    ["GAT-Q-ARI.1", "Primes, factors and divisibility rules"],
    ["GAT-Q-ARI.2", "LCM and HCF, ratio and proportion"],
  ],
  priors: [
    { skill: "Write a number as a product of primes", eq: "g12_fact",
      note: "Keep dividing by the smallest prime that goes in." },
    { skill: "Find HCF and LCM from the prime factors", eq: "g12_hcf",
      note: "HCF takes the LOWEST power of each shared prime; LCM takes the highest." },
    { skill: "Read a ratio as a fraction", eq: "g12_ratio",
      note: "The order of the ratio is the order of the fraction." },
    { skill: "Use divisibility rules without dividing",
      note: "By 3 if the digit sum divides by 3. By 4 if the last two digits do. "
          + "By 9 if the digit sum divides by 9." },
  ],
  vocab: [
    ["Prime", "a number with exactly two factors, itself and 1"],
    ["Factor", "a number that divides into another exactly"],
    ["Multiple", "the result of multiplying by a whole number"],
    ["HCF", "highest common factor — the biggest factor two numbers share"],
    ["LCM", "lowest common multiple — the first multiple they share"],
    ["Ratio", "a comparison of two quantities in order"],
  ],
  appearsTitle: "WHERE THIS APPEARS IN THE PAPER",
  appearsNote: "so you know what you are preparing for",
  appearsHead: "",
  appears: [
    ["How many items", "Arithmetic is about 36% of the quantitative half — the largest strand "
     + "on the paper. These two sub-skills alone are worth several marks every sitting."],
    ["What it looks like", "Rarely 'find the HCF of 24 and 36'. Far more often it is hidden: "
     + "how many tiles fit exactly, when do two buses next leave together, how many zeros end "
     + "a product."],
    ["Where you meet it", "Bus timetables leaving together from a Jeddah terminal, dividing a "
     + "quantity of SAR in a given ratio, and scale on a map of the Haramain railway."],
    ["Why it is worth the time", "No calculator is allowed, so a question you can factorise "
     + "in your head is a question you finish in twenty seconds instead of ninety."],
  ],
  notesSub: "GAT gives you about 75 seconds a question and no calculator. "
          + "These three ideas are what buy that time back.",
  keys: [
    { head: "Divisible by two numbers means divisible by their LCM", eq: "g12_div",
      body: "Testing 3 and 4 separately is slower than testing 12 once. On a counting "
          + "question this turns a list into a division." },
    { head: "Trailing zeros come from PAIRS of 2 and 5", eq: "g12_q",
      body: "This number ends in two zeros, because there are two 5s and plenty of 2s. "
          + "The 5s always decide it, so count those." },
    { head: "Chain a ratio by matching the shared term",
      body: "If a : b = 2 : 3 and b : c = 4 : 5, scale until b matches in both — 8 : 12 "
          + "and 12 : 15 — so a : c = 8 : 15. Never take the outer numbers straight." },
  ],
  misconception: "Adding percentages, and adding ratios. 20% of 60% is 12%, not 80%; "
    + "and a : b = 2 : 3 with b : c = 4 : 5 does NOT give a : c = 2 : 5. Both errors come "
    + "from treating a multiplying relationship as an adding one.",
  warmup: [
    { q: "Write 84 as a product of primes." },
    { q: "Find the HCF and LCM of 18 and 24." },
    { q: "How many integers from 1 to 60 divide by both 3 and 4?" },
    { q: "How many zeros end the product", eq: "w12_zeros" },
    { q: "If a : b = 3 : 4 and b : c = 2 : 5, what is a : c ?" },
    { q: "Is 4 173 divisible by 3? Answer without dividing." },
  ],
  routes: [
    "Do questions 1 and 2, then check your prime factors multiply back.",
    "Do questions 3 and 5 — both are ordinary GAT items in disguise.",
    "Question 6: explain WHY the digit-sum rule for 3 works.",
  ],
  doneWhen: "you can factorise a number into primes without hesitating, and you know which "
    + "of HCF and LCM takes the lowest power.",
  answers: "1) 2² × 3 × 7   2) HCF 6, LCM 72   3) 5   4) three   5) 3 : 10   "
    + "6) yes — the digits total 15, which divides by 3",
});

// =====================================================================
// GRADE 10 · SAT & GAT · Week 2 — anchored on 1-1 Key Features of Functions
// =====================================================================
build({
  who: "Grade 10 SAT & GAT",
  out: "PreSession_Gr10_SATGAT_W2.docx",
  headerLine: "Grade 10 · SAT and GAT · Week 2 · read this BEFORE the session",
  title: "Pre-Session Skills Sheet — Key Features of Functions",
  sub: "Classes 10A and 10B · this week's exam-prep session sits directly on top of "
     + "Lesson 1-1, so the vocabulary is the same in both rooms.",
  covers: [
    ["SAT-ALG.2", "Linear functions"],
    ["SAT-ADV.4", "Nonlinear functions — key features"],
    ["GAT-Q-ARI.3", "Fractions, decimals and percentages"],
    ["GAT-Q-ARI.5", "Numerical series and pattern recognition"],
  ],
  priors: [
    { skill: "Read a function in function notation", eq: "g10_lin",
      note: "f(5) means put 5 in for x. It is an instruction, not a multiplication." },
    { skill: "Find where a curve crosses the x-axis", eq: "g10_zero",
      note: "A product is zero when a bracket is zero, so x = 2 or x = −5. The sign flips." },
    { skill: "Find the turning point of a quadratic", eq: "g10_vert",
      note: "This gives you WHERE. Substitute it back to get the value there." },
    { skill: "Read a graph left to right",
      note: "Increasing and decreasing are always described along x, never up the y-axis." },
  ],
  vocab: [
    ["Domain", "every input the function is allowed"],
    ["Range", "every output it actually produces"],
    ["Zero", "an x where the graph meets the x-axis"],
    ["Intercept", "where the graph crosses an axis"],
    ["Vertex", "the turning point of a parabola"],
    ["Interval", "a stretch of x-values, written in x"],
  ],
  appearsTitle: "WHERE THIS APPEARS IN THE PAPERS",
  appearsNote: "two exams, one set of ideas",
  appearsHead: "",
  appears: [
    ["On the SAT", "Algebra and Advanced Math are about 35% each — the two biggest domains. "
     + "Key features of a function sit inside Advanced Math and come up in almost every module."],
    ["On the GAT", "Arithmetic is the largest strand at about 36%, and there is no calculator, "
     + "so the fraction and percentage work has to be quick."],
    ["Where you meet it", "A mobile plan with a monthly fee plus a rate per minute in SAR is a "
     + "linear function; a discount then VAT at 15% is a percentage of a percentage."],
    ["The habit to build", "Read the last four words of the question before answering. Most "
     + "lost marks here are the right calculation reported as the wrong quantity."],
  ],
  notesSub: "The SAT half of this session allows a calculator. The GAT half does not — "
          + "and the GAT questions are built so you do not need one.",
  keys: [
    { head: "The range is about y, and the vertex is the floor", eq: "g10_quad",
      body: "This curve turns at (1, −4) and rises both ways, so y takes every value from "
          + "−4 upwards. Students who answer with the x-coordinate have found the right "
          + "point and reported the wrong half of it." },
    { head: "Constant first differences mean the function is linear", eq: "g10_lin",
      body: "Given a table, subtract along the row. If the gaps are equal, the rule is "
          + "linear and the gap IS the coefficient of x." },
    { head: "A percentage of a percentage multiplies",
      body: "25% of 60% of 200 is 30, because 0.25 × 0.60 = 0.15. It is never 85%. "
          + "This is the single most common arithmetic slip on the GAT paper." },
  ],
  misconception: "Answering with x when the question asked for y. 'What is the minimum "
    + "VALUE' wants the y-coordinate; 'where is the minimum' wants the x. Read the last "
    + "four words of the question before you write anything.",
  warmup: [
    { q: "For", eq: "g10_lin", },
    { q: "Find the zeros of", eq: "w10_zero" },
    { q: "What is the minimum value of", eq: "g10_q" },
    { q: "A table gives f(0)=7, f(1)=11, f(2)=15. Find f(5)." },
    { q: "What is 20% of 60% of 400 ?" },
    { q: "Next term of 2, 6, 12, 20, 30, … ?" },
  ],
  routes: [
    "Questions 1 and 2 — substitution and zeros, the two you will use every week.",
    "Questions 3 and 4 — the same ideas inside a real SAT question shape.",
    "Question 6: find the rule of the sequence and say why the differences rise.",
  ],
  doneWhen: "you can say what domain, range, zero and vertex each mean without looking, "
    + "and you never confuse the x of a turning point with its y.",
  answers: "1) f(5) = 27   2) x = 3 and x = −4   3) −4   4) 27   5) 48   6) 42",
});

// =====================================================================
// GRADE 11 · SAT & GAT · Week 2 — anchored on 5-3 and 5-4, radical functions
// =====================================================================
build({
  who: "Grade 11 SAT & GAT",
  out: "PreSession_Gr11_SATGAT_W2.docx",
  headerLine: "Grade 11 · SAT and GAT · Week 2 · read this BEFORE the session",
  title: "Pre-Session Skills Sheet — Radical Functions",
  sub: "Class 11C · this session sits on Lessons 5-3 and 5-4. The one idea that matters "
     + "is that squaring both sides can invent a solution that was never there.",
  covers: [
    ["SAT-ADV.1", "Equivalent expressions — radicals and rational exponents"],
    ["SAT-ADV.2", "Nonlinear equations in one variable"],
    ["SAT-ADV.4", "Nonlinear functions — domain of a radical"],
    ["GAT-Q-ARI.4", "Exponent rules, roots and radicals"],
  ],
  priors: [
    { skill: "Solve a simple radical equation", eq: "g11_rad",
      note: "Square both sides, solve, then CHECK the answer in the original." },
    { skill: "State the domain of a square root", eq: "g11_dom",
      note: "The inside can never be negative, so x ≥ 4." },
    { skill: "Read a translated radical graph", eq: "g11_shift",
      note: "It starts where the inside is zero, at x = 4, lifted to y = 1." },
    { skill: "Turn a fractional exponent into a root", eq: "g11_rat",
      note: "Bottom is the root, top is the power. Take the root first — the numbers stay small." },
  ],
  vocab: [
    ["Radicand", "the expression under the root sign"],
    ["Index", "the small number saying which root"],
    ["Extraneous", "a solution the algebra produced but the original rejects"],
    ["Domain", "every input the function is allowed"],
    ["Rationalise", "clear a root out of a denominator"],
    ["Surd", "a root that cannot be written exactly as a fraction"],
  ],
  appearsTitle: "WHERE THIS APPEARS IN THE PAPERS",
  appearsNote: "two exams, one set of ideas",
  appearsHead: "",
  appears: [
    ["On the SAT", "Advanced Math is about 35% of the Math section, and radical and rational "
     + "exponent work sits squarely inside it — usually as 'equivalent expressions'."],
    ["On the GAT", "Roots and exponent rules fall under arithmetic, the largest strand, as "
     + "comparisons settled by matching bases rather than calculating."],
    ["Where you meet it", "Speed estimated from a vehicle's braking distance in a traffic "
     + "report is a square-root relationship."],
  ],
  notesSub: "Checking a solution is not tidiness here. It is part of the method, because "
          + "squaring is what creates the false root in the first place.",
  keys: [
    { head: "Squaring can invent a solution — always check", eq: "g11_rad",
      body: "Squaring turns a = b into a² = b², and −3 and 3 both square to 9. So the "
          + "squared equation can have roots the original never had. Substitute back into "
          + "the ORIGINAL equation, never the squared one." },
    { head: "A square root is never negative",
      body: "That is how you spot the false root: if substituting makes the right-hand side "
          + "negative while the left is a square root, that root is extraneous." },
    { head: "The graph starts where the inside is zero", eq: "g11_shift",
      body: "No part of the graph exists to the left of x = 4, because the radicand would "
          + "go negative. The domain and the starting point are the same fact." },
  ],
  misconception: "Accepting both roots of the squared equation. Solving √(x + 7) = x − 5 "
    + "gives x = 2 and x = 9, but at x = 2 the right side is −3 — and a square root is never "
    + "negative. Only x = 9 is real. Rejecting a root is not losing a mark; it is the answer.",
  warmup: [
    { q: "Solve and check", eq: "g11_q" },
    { q: "State the domain of", eq: "g11_shift" },
    { q: "Evaluate", eq: "w11_rat" },
    { q: "Simplify", eq: "w11_surd" },
    { q: "Evaluate the cube root of −64." },
    { q: "Does √(x + 5) = x − 1 have one solution or two?" },
  ],
  routes: [
    "Questions 1 to 3 — the mechanics, done slowly and checked.",
    "Questions 4 and 5 — surds and negative roots, both regular SAT shapes.",
    "Question 6: solve it, then explain which root the original equation refuses.",
  ],
  doneWhen: "you check every radical solution in the original equation without being told to.",
  answers: "1) x = 6   2) x ≥ 4   3) 9   4) 8√2   5) −4   "
    + "6) one — x = 4 works, x = −1 is extraneous",
});

// =====================================================================
// GRADE 9 MAWHIBA · Week 2 — Unit 1 Linear equations, Activity 1.
// Not an exam-prep class: no checklist codes, so it names the unit's own
// learning focus and the Mawhiba values the activity is built on.
// =====================================================================
build({
  who: "Grade 9 Mawhiba",
  out: "PreSession_Gr9_Mawhiba_W2.docx",
  headerLine: "Grade 9 Mawhiba · Week 2 · Unit 1 Linear Equations · read this BEFORE the session",
  title: "Pre-Session Skills Sheet — Always, Sometimes, or Never True",
  sub: "Classes 9A and 9B · Activity 1 of Unit 1. This session is not about getting an "
     + "answer; it is about deciding whether a statement holds for every number, some "
     + "numbers, or none — and saying how you know.",
  covers: [
    ["Unit 1", "Linear equations — about this unit"],
    ["Activity 1", "Always, sometimes, or never true?"],
  ],
  priors: [
    { skill: "Expand a bracket", eq: "g9_a",
      note: "Both sides are the same for EVERY x. That is an identity — always true." },
    { skill: "Recognise a rearrangement", eq: "g9_b",
      note: "Addition can be done in either order, so this is always true too." },
    { skill: "Collect like terms", eq: "g9_c",
      note: "x + 2x is 3x, so both sides always agree." },
    { skill: "Solve a linear equation", eq: "g9_e",
      note: "This one is true for exactly one value of x. Sometimes true." },
  ],
  vocab: [
    ["Equation", "a statement that two expressions are equal"],
    ["Identity", "an equation true for every value"],
    ["Solution", "a value that makes an equation true"],
    ["Variable", "a letter standing for a number"],
    ["Counter-example", "one case that disproves a claim"],
    ["Justify", "give the reason, not only the answer"],
  ],
  appearsTitle: "WHERE THIS LEADS",
  appearsNote: "why Mawhiba starts the year here",
  appearsHead: "",
  appears: [
    ["This unit", "Unit 1 is Linear Equations. Deciding whether a statement is always, "
     + "sometimes or never true is how the unit opens, because it forces you to think about "
     + "ALL numbers rather than one answer."],
    ["The values", "Inquiry — you are asked a question with no worked example. Risk taking — "
     + "a first guess you test is expected. Perseverance — the honest answer often takes a "
     + "second and third attempt."],
    ["Later in mathematics", "This is the beginning of proof. 'One counter-example disproves; "
     + "one example proves nothing' is a rule you will use for the rest of your studies."],
    ["In the world", "Engineers and planners in Saudi Arabia test whether a rule holds in "
     + "every case before they build on it — the same question, with larger consequences."],
  ],
  notesSub: "Mawhiba values in this activity: inquiry, risk taking and perseverance. "
          + "A wrong first guess that you test and correct is worth more here than a "
          + "right guess you cannot explain.",
  keys: [
    { head: "Three possibilities, not two",
      body: "An equation can be true ALWAYS (both sides identical for every x), SOMETIMES "
          + "(true for particular values), or NEVER (no value works). Most students only "
          + "look for 'sometimes', because that is what solving usually produces." },
    { head: "Never true has a signature", eq: "g9_d",
      body: "Subtract x from both sides and you are left with 1 = 2. When the variable "
          + "disappears and leaves something false, no number can rescue it." },
    { head: "One counter-example is enough to disprove",
      body: "To show a statement is NOT always true you need exactly one value where it "
          + "fails. To show it IS always true, one example is never enough — you must show "
          + "both sides are the same expression." },
  ],
  misconception: "Testing one number and deciding the statement is always true. Trying "
    + "x = 1 and finding both sides equal proves nothing on its own — it may be the one "
    + "value that happens to work. Ask what happens for every x, not for your favourite x.",
  warmup: [
    { q: "Always, sometimes or never true?", eq: "w9_a" },
    { q: "Always, sometimes or never true?", eq: "w9_b" },
    { q: "Always, sometimes or never true?", eq: "w9_c" },
    { q: "Write an equation that is never true." },
    { q: "Write an equation true only when x = 5." },
    { q: "Is x² = 4 always, sometimes, or never true?" },
  ],
  routes: [
    "Questions 1 to 3 — decide, then say which of the three it is and why.",
    "Questions 4 and 5 — build your own, then test them on a partner.",
    "Question 6: two values work. Explain why 'sometimes' is the honest answer.",
  ],
  doneWhen: "you can sort an equation into always, sometimes or never — and justify the "
    + "choice with either an argument or a counter-example.",
  answers: "1) always   2) never   3) sometimes, x = 4   4) e.g. x = x + 1   "
    + "5) e.g. x − 5 = 0   6) sometimes — x = 2 and x = −2",
});
