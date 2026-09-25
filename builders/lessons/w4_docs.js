// Week 4 documents — lesson plans, classwork, differentiation, PBL.
// Objectives / EQ / vocabulary / assessments verbatim from the curriculum map.
//
// ⚠ GRADE 11: the map's objectives column for Topic 5 Lesson 6 has been copied
// from the Inverse Variation lesson. It is printed below VERBATIM, as the house
// rule requires, with the mismatch flagged in the outcome list so the reader
// sees it. The lesson is taught to the row's own standards (BF.B.4.A-D).
const { buildAll } = require("./docs_engine");

const MATHDOC = "math_w4_doc/_index.json";
const GRAPH = "graphs_w4/_index.json";
const ASSESS = ["“Give it a go” questions", "“Time to Check”"];
const T = { t1: 6, t2: 18, t3: 12, t4: 12, t5: 6, t6: 6 };

const AI_CRITIC = "Role of AI: critic only. Briefed prompt — “Challenge my reasoning and point out any step I have not justified.” Never “solve this”.";
const PILLAR_ADAPTIVE = [
  "Entry branch — the Quizizz result routes each student to the re-teach table, straight to modelling, or the Investigate prompt.",
  "Mid-lesson branch — Pear Deck flags error patterns during independent practice; flagged students get a 2-minute micro-conference while others continue.",
  "Exit branch — the Mastery Gate routes each student: PASS → Enrichment & Challenge; NOT YET → Targeted Learning Clinic at the start of the next lesson.",
  "Routing is communicated privately through the LMS, never read aloud.",
];
const WEEK_NOTE = "Three teaching days this week. If time runs short, cut Smart Production and carry it into the next session — never the Mastery Gate, which is the evidence.";

// =====================================================================
// GR10 · 1-4 · Arithmetic Sequences and Series
// =====================================================================
const GR10_L4 = {
  slug: "Gr10_T1_L4_Arithmetic_Sequences_and_Series",
  mathDocIndex: MATHDOC, graphIndex: GRAPH, timings: T,
  lessonTitle: "Arithmetic Sequences and Series",
  unit: "Topic 1 — Linear Functions · Lesson 4",
  gradeFull: "Grade 10 — Algebra II",
  week: "Week 4 · Semester 1, 2026–27",
  lessonLine: "Grade 10 · Algebra II · Topic 1: Linear Functions · Lesson 4 — Arithmetic Sequences and Series",
  codes: ["HSF.LE.A.2", "HSF.IF.A.3", "HSF.BF.A.1", "HSF.BF.A.1.A", "HSF.BF.A.2"],
  mps: ["MP.4", "MP.6"],
  assessments: ASSESS,
  objectives: [
    "Calculate the common difference in an arithmetic sequence.",
    "Write recursive and explicit formulas of arithmetic sequences.",
    "Find the sums of arithmetic series.",
  ],
  essentialQuestion: "How can the concepts of arithmetic sequences and series be identified and applied to real-world situations?",
  vocabList: "arithmetic sequence ; arithmetic series ; common difference ; explicit formula ; recursive formula ; sequence ; series ; sigma notation",

  plan: {
    outcome: [
      "Students will find the common difference of a sequence and keep its sign when the sequence falls.",
      "Students will write both a recursive and an explicit formula, and say which job each one does.",
      "Students will count the terms of a finite sequence and find its sum, and model a savings plan in SAR.",
      WEEK_NOTE,
    ],
    preclass: [
      "Flipped video (4 min): “The same step, every time” — finding a common difference and reaching a term from its position. Posted on the LMS 48 hours ahead.",
      "Two embedded EdPuzzle questions: one common difference from a falling sequence, one term from a given rule.",
      "Evidence of readiness: EdPuzzle completion report plus both embedded answers submitted before the bell.",
    ],
    diagTool: [
      "5-question Quizizz (≤ 4 minutes): the common difference of 7, 12, 17, 22; the fourth term from a₁ = 3 and d = 5; whether 2, 6, 18, 54 is arithmetic; the first term from aₙ = 6n − 1; and the sum of the first four square numbers.",
      "Cross-referenced against overnight EdPuzzle watch analytics — who watched, who skipped, who missed the embedded items.",
      "Answers: d = 5 ; a₄ = 18 ; no, it multiplies by 3 ; a₁ = 5 ; 30.",
    ],
    diagGap: [
      "Expected gap 1 — n versus n − 1: students multiply the step by the position rather than by one less, and every term comes out one step too big.",
      "Expected gap 2 — the sign of d: a falling sequence is read as rising, because students subtract the later term from the earlier one.",
      "Expected gap 3 — Q3: students answer “yes, it is arithmetic” because the numbers rise steadily. Rising is not the test; a CONSTANT difference is.",
      "Routing: 0–2 correct → re-teach table.  3–4 → straight to the explicit formula.  5 → begin the Investigate prompt immediately.",
    ],
    instruction: [
      "Direct explanation (3–5 min, flagged students only): subtract in one direction and keep it, and test any rule you write on n = 1.",
      "Whole class: the sequence 5, 9, 13, 17, 21 plotted against its positions — the points are the sequence, the dashed line only shows that a constant step means collinear. This is HSF.IF.A.3 made visible.",
      "The two formulas side by side: recursive a₁ = 5, aₙ = aₙ₋₁ + 4, and explicit aₙ = 5 + (n−1)4 = 4n + 1. Which job each one does, and why a recursive rule without a₁ is useless.",
      "Modelled example, thinking aloud: the pairing picture for the sum. Write 5 + 9 + 13 + 17 + 21 forwards, write it backwards underneath, and add in pairs — every pair is 26, and there are 5 of them, so 2S = 130 and S = 65.",
      "Narration focus — do the pairing with the actual five numbers BEFORE the formula appears. A student who has seen it can rebuild the formula in the exam room.",
      "This is a NEW example — it does not repeat the flipped video.",
    ],
    quickCheck: [
      "On whiteboards, 60 seconds: write the explicit rule and find the tenth term for a₁ = −8, d = 3.",
      "Expected: aₙ = 3n − 11, so a₁₀ = 19. Watch for aₙ = 3n − 8, which is the n-instead-of-(n−1) error.",
      "80% correct → release guided practice. Below 80% → one further modelled example starting from a negative first term.",
    ],
    guided: [
      "Two “Give it a go” problems, identical for every student, worked together with the teacher:",
      "(1) 11, 4, −3, −10, … — write the explicit rule and find a₁₅.  (2) a₁ = 2 and a₂₀ = 97 — find d, then S₂₀.",
      "Answers: d = −7, aₙ = 18 − 7n, a₁₅ = −87 ; d = (97 − 2)/19 = 5, S₂₀ = 20/2 (2 + 97) = 990.",
      "Feedback: worked live on the board step by step; students self-mark and circle their OWN first error.",
    ],
    independent: [
      "Delivered through the “Choose Your Route” sheet with live feedback in Pear Deck. Routes are named for the task, not for the student.",
      "PRACTICE — Secure the method. Four common differences including two falling sequences, two explicit rules tested on n = 1, one recursive rule turned explicit, one term from a₁ and d. Done when: your rule gives the right first term when you test it.",
      "APPLY — Use it in context. Count the terms of a finite sequence then sum it, evaluate a sum in sigma notation, find a₁ and d from two non-adjacent terms, and price a twelve-month savings plan in SAR. Done when: you have counted the terms before summing, and your answer carries SAR.",
      "INVESTIGATE — Find out why. Show the two sum formulas are one formula, explain why a constant difference forces linearity in n, and find a rule from a₃ and a₈. Done when: you have an argument, not just an answer.",
      "Every student sits the same Mastery Gate. The gate is not differentiated, because it is the evidence.",
    ],
    production: [
      "Non-routine transfer task — this context has not appeared in practice.",
      "A graduate in Jeddah joins a twelve-month savings scheme. She deposits 400 SAR in the first month and increases the deposit by 150 SAR every month after that. The scheme pays no interest — the growth is her own rising deposit.",
      "(a) Write both formulas for the monthly deposit and say which you would use for the twelfth. (b) Find the twelfth deposit in SAR. (c) Find the twelve-month total in SAR. (d) A friend says “she saves about 400 a month, so roughly 4 800 a year” — say in one sentence what the friend has missed.",
      "Answers: (a) recursive a₁ = 400, aₙ = aₙ₋₁ + 150 ; explicit aₙ = 150n + 250 ; explicit for the twelfth. (b) a₁₂ = 400 + 11(150) = 2 050 SAR. (c) S₁₂ = 12/2 (400 + 2 050) = 14 700 SAR. (d) the friend has treated a rising deposit as a flat one — 400 is only the FIRST month.",
      "Students then hand their reasoning to the AI critic and ask it to challenge any step they have not justified.",
    ],
    criteria: [
      "Minimum acceptable standard: both formulas written correctly, every answer in SAR, and the formula named for each step.",
      AI_CRITIC,
      "Completed independently by the student: the written justification for parts (a)–(d). AI may challenge it; it may not write it.",
    ],
    evidence: [
      "“Time to Check” — one individual task. No notes, no partner, no AI.",
      "For the finite sequence 6, 11, 16, …, 201: 1. how many terms are there — show the counting, not a guess. 2. find the sum of all of them. 3. in ONE sentence explain why you had to add one when you counted.",
      "Answers: n = (201 − 6)/5 + 1 = 40 ; S₄₀ = 40/2 (6 + 201) = 4 140 ; you add one because the first term was already there before any step was taken.",
      "Done when: the counting is shown, the sum is exact, and question 3 gives a reason rather than a restatement.",
      "Scored live in Pear Deck as submissions arrive; result logged in the Impact Dashboard Mastery Rate.",
    ],
    refinement: [
      "Students revise their savings reasoning using the AI critique and the teacher's micro-conference note.",
      "Final product, three equally acceptable formats: a Canva one-pager, a photographed hand-written solution, or a 45-second voice note.",
      "Required content: both formulas, the twelfth deposit and the twelve-month total in SAR; ONE worked non-example — the total found as 12 × 400 — with a sentence on how a reader would spot it; and a caption on why a rising deposit beats a flat one.",
      "Graded on originality and clarity of reasoning, not correctness alone.",
    ],
    publication: [
      "Published to the class LMS portfolio; the strongest go on the Mathematics Department wall as the Topic 1 modelling set.",
      "Reflection question: “Which still catches you out — the n − 1, or counting how many terms there are?”",
    ],
    differentiation: [
      "PRACTICE — Secure the method. Common differences, explicit rules tested on n = 1, one recursive rule converted, one term from a₁ and d; the two formulas stay on the board and a partner is allowed. Done when: your rule gives the right first term when you test it.",
      "APPLY — Use it in context. Counting terms then summing, sigma notation, two non-adjacent terms, and the SAR savings plan. Done when: the terms are counted before summing and the answer carries SAR.",
      "INVESTIGATE — Find out why. The two sum formulas shown to be one, the linearity argument, and a rule from a₃ and a₈. Done when: there is an argument, not just an answer.",
      "No student is labelled. The routes describe tasks; every student sits the same Mastery Gate.",
    ],
    adaptive: PILLAR_ADAPTIVE,
    saudi: [
      "Production context: a twelve-month savings scheme in Jeddah — 400 SAR in the first month rising by 150 SAR a month — priced term by term and in total, in SAR.",
      "In-class project: seating in a Jeddah stadium stand, where each row holds a fixed number more than the row in front, costed for a Vision 2030 events programme.",
      "Discussion prompt: why a rising monthly commitment reaches a savings target faster than a flat one of the same starting size.",
    ],
    exams: [
      "GAT (Qudurat) — numerical series and pattern recognition, inside arithmetic, the largest quantitative strand at about 36%. About 75 seconds per item, no calculator. Practice tip: take the step from the first pair and confirm it on the second; if it changes, the pattern is not arithmetic.",
      "SAAT (Tahsili) — sequences and series in the Grade 11 band, 30% of the mathematics section; both the explicit formula and the sum appear. Practice tip: write d before anything else — most wrong options are the right method with the wrong sign.",
      "SAT — Algebra, linear functions and linear equations in two variables, about 35% of the Mathematics section. Practice tip: rewrite the sequence as y = mx + b with m = d and let Desmos finish it.",
    ],
  },

  plan2026: {
    day: "Sunday, Week 4", section: "Grade 10 — 10A and 10C",
    tools: "Quizizz (diagnostic) · Pear Deck (live practice feedback) · GeoGebra Graphing Calculator · Canva (final product) · Whiteboards",
    resources: "Lesson presentation (18 slides) · “Choose Your Route” differentiation sheet · “Give It a Go” classwork · “The Rising Deposit” project task · squared paper",
    competencies: ["Choosing between a recursive and an explicit rule for the job in hand.", "Interpreting a savings model and pricing a year of it in SAR."],
    technology: ["Quizizz live diagnostic with instant gap analysis.", "GeoGebra Sequence( ) to plot terms as points and see why the line is not the sequence."],
    reallife: ["A twelve-month savings scheme with a rising monthly deposit.", "Stadium seating that grows by a fixed number of seats each row."],
    values: ["Precision — the step applied n − 1 times, not n.", "Responsibility for a long-term financial commitment."],
    soft: ["Collaboration in assigned group roles.", "Explaining which formula was chosen, and why, before computing."],
    hard: ["Finding a common difference and writing recursive and explicit formulas.", "Counting the terms of a finite sequence and finding its sum."],
    phases: [
      "FIKR Phase 1 — Diagnose. 5-question Quizizz on steps, positions and a non-example. Results read as a gap map; students routed to the re-teach table, straight to the explicit formula, or the Investigate prompt.",
      "FIKR Phase 2 — Targeted Instruction. Focused re-teach on n versus n − 1 for flagged students. Whole class: the sequence plotted against its positions; the two formulas side by side; the pairing picture for the sum. Quick check on whiteboards.",
      "FIKR Phase 3 — Practice. Two identical “Give it a go” problems worked together. Students then choose a route and may switch at any time. Live feedback via Pear Deck; 2-minute micro-conferences.",
      "FIKR Phase 4 — Production. The rising savings deposit: both formulas, the twelfth deposit, the twelve-month total, and the friend's mistake. AI used as critic only.",
      "FIKR Phase 5 — Proof of Learning. “Time to Check” — count the terms of an unseen finite sequence and sum them. No notes, no partner, no AI.",
      "FIKR Phase 6 — Smart Production. Students refine their reasoning into a final product including one worked non-example, and publish to the LMS portfolio.",
    ],
    assessment: [
      "Diagnostic quiz — gap map, not a grade.",
      "Quick check for understanding on whiteboards (80% threshold).",
      "“Give it a go” questions — self-marked, teacher circulates.",
      "Project task sheet against its “Done when…” criteria.",
      "“Time to Check” — Mastery Gate, scored live. PASS → Enrichment & Challenge. NOT YET → Targeted Learning Clinic next lesson.",
      "Final product graded on reasoning and clarity, not correctness alone.",
    ],
    closure: "Two minutes of peer show-and-tell on the final products, then the reflection question: “Which still catches you out — the n − 1, or counting how many terms there are?”",
    homework: "Finish the final product and upload to the LMS portfolio (any of the three formats). Practice set on Pear Deck — 12 questions, choose your route. Watch the flipped video for Lesson 1-5: Solving Equations and Inequalities by Graphing. Clinic group: bring your Time to Check paper.",
  },

  classwork: {
    subtitle: "Show all your working. Write down d before you write anything else, and test every rule you make on n = 1.",
    sections: [
      { h: "SECTION A — The common difference", note: "Objective 1", lines: 4,
        q: [
          { n: "Q1", eq: "a_ws1", t: "Find the common difference and the next two terms." },
          { n: "Q2", eq: "a_ws2", t: "Find the common difference. Say what its sign tells you about the sequence." },
          { n: "Q3", eq: "a_ws3", t: "This rule is recursive. Write the first four terms." },
          { n: "Q4", eq: "a_ws4", t: "Read d straight off this explicit rule, and find a₁." },
        ] },
      { h: "SECTION B — Recursive and explicit", note: "Objective 2", lines: 4,
        intro: "Use the two-formula table from the lesson if you need it.",
        q: [
          { n: "Q5", eq: "a_ws1", t: "Write the explicit rule for this sequence, then test it on n = 1." },
          { n: "Q6", eq: "a_ws3", t: "Turn this recursive rule into an explicit one." },
        ] },
      { h: "SECTION C — Sums and sigma notation", note: "Objective 3", lines: 5,
        intro: "Count the terms before you sum them. The count is where the marks are lost.",
        text: [
          "Q7.  How many terms are in 9, 14, 19, …, 124? Show the counting, then find the sum.",
          "Q8.  Evaluate the sum written in sigma notation below, and say what its first and last terms are.",
          "Q9.  A student finds the sum of 6, 11, 16, …, 201 by working out (201 − 6) ÷ 5 = 39 and then using n = 39. Explain in one sentence exactly what they got wrong.",
        ],
        graph: "g_ar_pair", graphW: 420 },
      { h: "SECTION D — A savings plan in SAR", note: "MP.4 · the real-world objective", lines: 5,
        intro: "A savings scheme takes 400 SAR in the first month and 150 SAR more each month after that.",
        text: [
          "Q10.  Write the explicit rule for the monthly deposit, and find the deposit in month 12.",
          "Q11.  Find the total saved over the twelve months, in SAR.",
          "Q12.  How many months would it take for a single monthly deposit to first exceed 3 000 SAR? Show your reasoning.",
        ] },
    ],
  },

  diffSheet: {
    routes: [
      { note: "Steps and rules", done: "your rule gives the right first term when you test it.",
        intro: "For each sequence, find d first. Then write the rule and test it on n = 1.",
        grid: [["1.", "a_ws1"], ["2.", "a_ws2"], ["3.", "a_ws3"], ["4.", "a_ws4"], ["5.", "a_g1"], ["6.", "a_qc"]],
        tasks: ["7.  Choose any two of the sequences above and write BOTH formulas for each — recursive and explicit."],
        lines: 2 },
      { note: "Counting, summing, and one Saudi context", done: "you have counted the terms before summing, and your answer carries SAR.",
        graph: "g_ar_pair", graphW: 380,
        tasks: [
          "1.  How many terms are in 9, 14, 19, …, 124? Show the counting, then find the sum.",
          "2.  Evaluate the sum in sigma notation from the classwork, and state its first and last terms.",
          "3.  A sequence has a₃ = 17 and a₈ = 42. Find d, then a₁, then the rule.",
          "4.  A savings scheme takes 400 SAR in month 1 and 150 SAR more each month. Find the twelfth deposit and the twelve-month total, both in SAR.",
        ], lines: 4 },
      { note: "Arguments, not answers", done: "you have an argument, not just an answer.",
        tasks: [
          ["1.  Show that   ", { eq: "a_ws8", k: 0.95 }, "   are the same formula, by substituting the explicit rule for aₙ."],
          "2.  Explain why a sequence with a constant difference must be a linear function of n — and why the graph is still dots rather than a line.",
          "3.  Two terms are always enough to find an arithmetic sequence. Explain why, and say what would go wrong if you were given two terms of a sequence that was not arithmetic.",
        ], lines: 5 },
    ],
  },

  pbl: {
    title: "The Rising Deposit", minutes: 20,
    subtitle: "A 20-minute group project. Work in fours. Every member signs the sheet.",
    driving: "Two savers put money aside for a year. One pays the same amount every month; the other starts smaller and raises it each month. Which one ends the year ahead, and by how much?",
    situation: [
      "A graduate in Jeddah joins a twelve-month savings scheme. She deposits 400 SAR in the first month and increases the deposit by 150 SAR every month after that. The scheme pays no interest.",
      "Her colleague puts aside a flat 1 000 SAR every month for the same twelve months.",
      "They want to know who ends the year with more, and at which month the rising plan overtakes the flat one.",
    ],
    eq: "ctx_save",
    steps: [
      ["1", "WRITE THE MODEL  (4 min)", "Write both formulas for the rising deposit — recursive and explicit — and say which one you will use."],
      ["2", "PRICE THE YEAR  (5 min)", "Find the twelfth deposit and the twelve-month total for the rising plan. Then find the flat plan's total. Both in SAR."],
      ["3", "FIND THE CROSSOVER  (4 min)", "In which month does the rising DEPOSIT first exceed 1 000 SAR? Show the reasoning, not a guess."],
      ["4", "EXPLAIN THE GAP  (4 min)", "Explain in writing why the rising plan wins the year even though it starts at less than half the flat deposit."],
      ["5", "PRESENT  (3 min)", "Prepare one sentence your presenter will say: which plan you would advise, and why."],
    ],
    working: [["Step 1 — both formulas:", 2], ["Step 2 — the twelfth deposit and both totals:", 3],
              ["Step 3 — the crossover month:", 2], ["Step 4 — why the rising plan wins:", 4],
              ["Step 5 — our sentence:", 2]],
    roles: ["Reader — states the two plans", "Calculator — prices both years", "Checker — tests every claim", "Presenter — says the sentence"],
    doneWhen: ["Both totals are exact and in SAR.", "The formula used is named for every calculation.", "Step 3 shows reasoning, not a list of twelve deposits.", "Your sentence makes sense to someone who does not study maths."],
    materials: ["This sheet", "Squared paper", "A pencil and ruler", "A calculator"],
  },
};

// =====================================================================
// GR11 · 5-6 · Inverse Relations and Functions
// =====================================================================
const GR11_L6 = {
  slug: "Gr11_T5_L6_Inverse_Relations_and_Functions",
  mathDocIndex: MATHDOC, graphIndex: GRAPH, timings: T,
  lessonTitle: "Inverse Relations and Functions",
  unit: "Topic 5 — Radical Functions · Lesson 6",
  gradeFull: "Grade 11 — Algebra II",
  week: "Week 4 · Semester 1, 2026–27",
  lessonLine: "Grade 11 · Algebra II · Topic 5: Radical Functions · Lesson 6 — Inverse Relations and Functions",
  codes: ["HSF.BF.B.4.A", "HSF.BF.B.4.B", "HSF.BF.B.4.C", "HSF.BF.B.4.D"],
  mps: ["MP.2", "MP.7"],
  assessments: ASSESS,
  // VERBATIM from the curriculum map's objectives column for this row.
  objectives: [
    "Distinguish between direct and inverse variation.",
    "Write equations that represent inverse variation, including reciprocal functions.",
    "Describe the effects of transformations on the graph of the parent reciprocal function f(x)=1/(x-h)+k.",
    "Apply inverse variation concepts to solve real-world problems.",
  ],
  essentialQuestion: "How can we analyze and represent exponential and logarithmic relationships in different mathematical and real-world contexts?",
  vocabList: "inverse functions ; inverse relation",

  plan: {
    outcome: [
      "⚠ MAP DEFECT, FLAGGED NOT CORRECTED. The four objectives printed above are quoted verbatim from the curriculum map's row for this lesson, but they belong to the Inverse VARIATION lesson — as does the essential question, which is about exponential and logarithmic relationships. The row's title, its two vocabulary terms and all four of its standards are about INVERSE FUNCTIONS. This lesson is taught to the STANDARDS. Raise the row with the HOD; do not amend the map locally.",
      "Students will find the inverse of a function by swapping x and y and then solving (BF.B.4.A).",
      "Students will verify a claimed inverse by composition in both directions (BF.B.4.B).",
      "Students will read a value of an inverse function from a graph or a table (BF.B.4.C).",
      "Students will restrict the domain of a non-invertible function so that an inverse exists, and state that inverse's domain (BF.B.4.D).",
      WEEK_NOTE,
    ],
    preclass: [
      "Flipped video (4 min): “Undoing a rule” — swapping x and y, and checking by composition. Posted on the LMS 48 hours ahead.",
      "Two embedded EdPuzzle questions: one linear inverse, one composition that cancels to x.",
      "Evidence of readiness: EdPuzzle completion report plus both embedded answers submitted before the bell.",
    ],
    diagTool: [
      "5-question Quizizz (≤ 4 minutes): evaluate f(4) for f(x) = 2x + 9; evaluate f(g(2)) where f and g undo each other; make x the subject of y = 5x − 1; simplify √(x²) for negative x; and decide whether {(1,4), (2,4), (3,9)} is one-to-one.",
      "Cross-referenced against overnight EdPuzzle watch analytics — who watched, who skipped, who missed the embedded items.",
      "Answers: 17 ; 2, and f and g undo each other ; x = (y + 1)/5 ; −x ; no, 1 and 2 both map to 4.",
    ],
    diagGap: [
      "Expected gap 1 — the reciprocal error: students read f⁻¹ as 1/f. This is the single commonest error in the topic on both the SAT and the Tahsili.",
      "Expected gap 2 — solving before swapping, which produces the same algebra with the letters in the wrong places.",
      "Expected gap 3 — Q4 and Q5, which decide whether the domain-restriction idea lands later in the lesson.",
      "Routing: 0–2 correct → re-teach table.  3–4 → straight to swap-and-solve.  5 → begin the Investigate prompt immediately.",
    ],
    instruction: [
      "Direct explanation (3–5 min, flagged students only): the −1 names the undoing function; it is not an exponent, and f⁻¹ is not 1/f. Write it on the board and cross it out.",
      "Whole class, BF.B.4.A: swap then solve, on y = 3x − 8. Swap first, before any algebra; the reversed-pairs statement (a, b) ∈ f ⟺ (b, a) ∈ f⁻¹ says the same thing.",
      "Whole class, BF.B.4.B: the check is composition, not the graph. f(f⁻¹(x)) = x AND f⁻¹(f(x)) = x — one direction alone can hold on a restricted set. The reflection in y = x is the picture of the same fact.",
      "Whole class, BF.B.4.C and BF.B.4.D: the horizontal line test on y = x², and the cut to x ≥ 0 that makes √x a function. The inverse's DOMAIN is the original's RANGE.",
      "Narration focus — say plainly that the restriction is not a technicality the examiner added; it is the reason the radical sign is defined to give the non-negative root.",
      "This is a NEW example — it does not repeat the flipped video.",
    ],
    quickCheck: [
      "On whiteboards, 60 seconds: find the inverse of f(x) = (x − 5)/2 and check it by composing both ways.",
      "Expected: f⁻¹(x) = 2x + 5, with f(f⁻¹(x)) = x and f⁻¹(f(x)) = x. Watch for 2/(x − 5), the reciprocal error, and (x/2) − 5, which is solving before swapping.",
      "80% correct → release guided practice. Below 80% → one further modelled example, this time with a fraction in the rule.",
    ],
    guided: [
      "Two “Give it a go” problems, identical for every student, worked together with the teacher:",
      "(1) f(x) = 7x + 3 — find the inverse and verify by composition both ways.  (2) f(x) = x³ − 4 — find the inverse and state its domain.",
      "Answers: f⁻¹(x) = (x − 3)/7, both compositions give x ; f⁻¹(x) = ∛(x + 4), domain all real numbers, because a cube root accepts negatives.",
      "Feedback: worked live on the board step by step; students self-mark and circle their OWN first error.",
    ],
    independent: [
      "Delivered through the “Choose Your Route” sheet with live feedback in Pear Deck. Routes are named for the task, not for the student.",
      "PRACTICE — Secure the method. Four linear inverses by swap-and-solve, two verified by composition, one value of f⁻¹ read off a graph, one table reversed. Done when: your composition gives x both ways round, every time.",
      "APPLY — Use it in context. A radical inverse with its domain, a rational inverse with its excluded value, a quadratic restricted then inverted, and the SAR–dollar conversion pair. Done when: every inverse comes with its domain and your conversion carries units.",
      "INVESTIGATE — Find out why. Why one composition is not enough, f(x) = |x| restricted and what was lost, and the reflection in y = x proved from the pairs. Done when: you have an argument, not just an answer.",
      "Every student sits the same Mastery Gate. The gate is not differentiated, because it is the evidence.",
    ],
    production: [
      "Non-routine transfer task — this context has not appeared in practice.",
      "The Saudi riyal is pegged at 3.75 SAR to the US dollar, so converting one way and back is an exact undoing. A Jeddah taxi charges a 10 SAR flag fall plus 2.50 SAR per kilometre.",
      "(a) Write the two conversion functions and verify by composition that they are inverses. (b) Write the fare as F(d) and find F⁻¹. (c) A passenger is charged 47.50 SAR — use the inverse to find the distance. (d) A second firm adds a 15% surcharge to the whole fare: is “convert then surcharge” the same as “surcharge then convert”? Justify.",
      "Answers: (a) U(S(u)) = 3.75u/3.75 = u and S(U(s)) = s. (b) F(d) = 10 + 2.5d, F⁻¹(c) = (c − 10)/2.5. (c) (47.50 − 10)/2.5 = 15 km. (d) yes for this pair, because multiplying by 1.15 and dividing by 3.75 are both multiplications by a constant and constants commute. Push for the REASON, not the yes.",
      "Students then hand their reasoning to the AI critic and ask it to challenge any step they have not justified.",
    ],
    criteria: [
      "Minimum acceptable standard: every inverse verified in BOTH directions, units named, and the distance exact.",
      AI_CRITIC,
      "Completed independently by the student: the written justification for parts (a)–(d). AI may challenge it; it may not write it.",
    ],
    evidence: [
      "“Time to Check” — one individual task. No notes, no partner, no AI.",
      "For f(x) = (2x + 1)/5: 1. find the inverse. 2. verify it by composition, both ways round. 3. in ONE sentence explain why checking only one direction would not be enough.",
      "Answers: f⁻¹(x) = (5x − 1)/2 ; f(f⁻¹(x)) = x and f⁻¹(f(x)) = x, both shown in full ; one direction alone can hold on a restricted set, so it does not prove the two functions undo each other everywhere.",
      "Done when: the inverse is exact, BOTH compositions are written out, and question 3 gives a reason rather than a restatement.",
      "Scored live in Pear Deck as submissions arrive; result logged in the Impact Dashboard Mastery Rate.",
    ],
    refinement: [
      "Students revise their taxi and conversion reasoning using the AI critique and the teacher's micro-conference note.",
      "Final product, three equally acceptable formats: a Canva one-pager, a photographed hand-written solution, or a 45-second voice note.",
      "Required content: the fare function with its inverse and the 47.50 SAR fare converted back to a distance; ONE worked non-example — the inverse written as 1/(10 + 2.5d) — with a sentence on how a reader would spot it; and a caption on what it means to undo a rule.",
      "Graded on originality and clarity of reasoning, not correctness alone.",
    ],
    publication: [
      "Published to the class LMS portfolio; the strongest go on the Mathematics Department wall as the Topic 5 modelling set.",
      "Reflection question: “Which is still harder for you — remembering to swap first, or remembering to check both ways?”",
    ],
    differentiation: [
      "PRACTICE — Secure the method. Four linear inverses, two compositions, one value read off a graph, one table reversed; the four-step method stays on the board and a partner is allowed. Done when: the composition gives x both ways round.",
      "APPLY — Use it in context. A radical inverse with its domain, a rational inverse with its exclusion, a restricted quadratic, and the SAR–dollar pair. Done when: every inverse carries its domain.",
      "INVESTIGATE — Find out why. One composition is not enough; |x| restricted and what was lost; the reflection proved from the pairs. Done when: there is an argument, not just an answer.",
      "No student is labelled. The routes describe tasks; every student sits the same Mastery Gate.",
    ],
    adaptive: PILLAR_ADAPTIVE,
    saudi: [
      "Production context: the riyal's peg at 3.75 SAR to the dollar, which makes the two conversion functions an exact inverse pair, and a Jeddah taxi fare read backwards from the meter.",
      "In-class project: a delivery firm's pricing rule in SAR, inverted so a customer can work out the distance from the price they were charged.",
      "Discussion prompt: which everyday rules can be undone exactly, and which cannot — a discount followed by VAT, against a fare followed by a surcharge.",
    ],
    exams: [
      "SAAT (Tahsili) — inverse functions in the Grade 11 band, 30% of the mathematics section: find f⁻¹, identify the inverse's graph, and spot a composition that cancels to x. Practice tip: before expanding anything, check whether the two functions are inverses — many items collapse in one line.",
      "SAT — Advanced Math, equivalent expressions and nonlinear functions, about 35% of the Mathematics section, with the domain restriction supplying most of the wrong options. Practice tip: test a number — put 2 in, take the output through your candidate inverse, and see whether 2 comes back.",
      "GAT (Qudurat) — undoing a rule inside algebra and word problems, about 18% of the quantitative half, no calculator. Practice tip: reverse the operations in reverse order; it is the same idea with no notation attached.",
    ],
  },

  plan2026: {
    day: "Sunday, Week 4", section: "Grade 11 — 11B",
    tools: "Quizizz (diagnostic) · Pear Deck (live practice feedback) · GeoGebra Graphing Calculator · Canva (final product) · Whiteboards",
    resources: "Lesson presentation (18 slides) · “Choose Your Route” differentiation sheet · “Give It a Go” classwork · “Read the Meter Backwards” project task · squared paper",
    competencies: ["Choosing a method that can be checked, and then checking it.", "Interpreting a pricing rule in both directions."],
    technology: ["Quizizz live diagnostic with instant gap analysis.", "GeoGebra to graph a function, its inverse and y = x, and drag a point along the mirror."],
    reallife: ["The riyal's peg to the US dollar, and converting back and forth.", "A Jeddah taxi meter read backwards from the fare."],
    values: ["Honesty in verification — a claim is checked in both directions before it is made.", "Care with money and with units."],
    soft: ["Collaboration in assigned group roles.", "Explaining why a check was needed, not just that it passed."],
    hard: ["Finding an inverse by swapping and solving, and verifying by composition.", "Restricting a domain so that an inverse exists, and stating that inverse's domain."],
    phases: [
      "FIKR Phase 1 — Diagnose. 5-question Quizizz on evaluating, undoing, rearranging, √(x²) and one-to-one. Results read as a gap map; students routed to the re-teach table, straight to swap-and-solve, or the Investigate prompt.",
      "FIKR Phase 2 — Targeted Instruction. Focused re-teach on f⁻¹ versus 1/f for flagged students. Whole class: swap then solve; verification by composition both ways; the horizontal line test and the cut to x ≥ 0. Quick check on whiteboards.",
      "FIKR Phase 3 — Practice. Two identical “Give it a go” problems worked together. Students then choose a route and may switch at any time. Live feedback via Pear Deck; 2-minute micro-conferences.",
      "FIKR Phase 4 — Production. The pegged riyal and the taxi meter: verify the conversion pair, invert the fare, recover a distance from 47.50 SAR, and decide whether a surcharge commutes with conversion. AI used as critic only.",
      "FIKR Phase 5 — Proof of Learning. “Time to Check” — invert an unseen function and verify it both ways. No notes, no partner, no AI.",
      "FIKR Phase 6 — Smart Production. Students refine their reasoning into a final product including one worked non-example, and publish to the LMS portfolio.",
    ],
    assessment: [
      "Diagnostic quiz — gap map, not a grade.",
      "Quick check for understanding on whiteboards (80% threshold).",
      "“Give it a go” questions — self-marked, teacher circulates.",
      "Project task sheet against its “Done when…” criteria.",
      "“Time to Check” — Mastery Gate, scored live. PASS → Enrichment & Challenge. NOT YET → Targeted Learning Clinic next lesson.",
      "Final product graded on reasoning and clarity, not correctness alone.",
    ],
    closure: "Two minutes of peer show-and-tell on the final products, then the reflection question: “Which is still harder for you — remembering to swap first, or remembering to check both ways?”",
    homework: "Finish the final product and upload to the LMS portfolio (any of the three formats). Practice set on Pear Deck — 12 questions, choose your route. Watch the flipped video for Lesson 6-1: Key Features of Exponential Functions. Clinic group: bring your Time to Check paper.",
  },

  classwork: {
    subtitle: "Show all your working. Swap BEFORE you solve, and check every inverse by composing it both ways round.",
    sections: [
      { h: "SECTION A — Swap and solve", note: "Standard BF.B.4.A", lines: 4,
        q: [
          { n: "Q1", eq: "v_ws1", t: "Find the inverse." },
          { n: "Q2", eq: "v_ws2", t: "Find the inverse." },
          { n: "Q3", eq: "v_ws6", t: "Find the inverse, and say why no domain has to be cut." },
          { n: "Q4", eq: "v_ws5", t: "Find the inverse. Which value must be excluded, and from which function?" },
        ] },
      { h: "SECTION B — Verify by composition", note: "Standard BF.B.4.B", lines: 4,
        intro: "For each pair, compose BOTH ways round. One direction is not a proof.",
        q: [
          { n: "Q5", eq: "v_bothc", t: "Using your answers to Q1 and Q2, show that BOTH of these compositions give x." },
          { n: "Q6", eq: "v_ws3n", t: "For x ≥ 2. Find the inverse, state its domain, and verify by composition on the allowed values only." },
        ] },
      { h: "SECTION C — Reading an inverse off a graph", note: "Standard BF.B.4.C", lines: 5,
        intro: "The graph below shows a one-to-one function g. Answer WITHOUT finding a formula.",
        graph: "g_inv_gate", graphW: 360,
        text: [
          "Q7.  Find g⁻¹(5) and g⁻¹(−3). Say which point on the graph told you each answer.",
          "Q8.  Write down three ordered pairs that belong to g⁻¹.",
          "Q9.  A student says “g⁻¹(0) = 1 because the graph passes through (0, 1)”. Explain in one sentence exactly what they have confused.",
        ] },
      { h: "SECTION D — Restricting a domain, and a fare in SAR", note: "Standard BF.B.4.D · MP.4", lines: 5,
        intro: "A Jeddah taxi charges a 10 SAR flag fall plus 2.50 SAR per kilometre.",
        text: [
          "Q10.  Show that f(x) = |x| has no inverse. Then restrict its domain so that it does, and write the inverse.",
          "Q11.  Write the fare as a function of distance, find its inverse, and use the inverse to find the distance for a 47.50 SAR fare.",
          "Q12.  Explain why the fare function has an inverse without any restriction, but f(x) = x² − 6x + 5 needs one.",
        ] },
    ],
  },

  diffSheet: {
    routes: [
      { note: "Swap, solve, check", done: "your composition gives x both ways round, every time.",
        intro: "Find the inverse of each function, then check it by composing both ways.",
        grid: [["1.", "v_ws1"], ["2.", "v_ws2"], ["3.", "v_g1"], ["4.", "v_g2"], ["5.", "v_qc"], ["6.", "v_ws6"]],
        tasks: ["7.  Choose any two of the functions above and write out BOTH compositions in full."],
        lines: 2 },
      { note: "Domains, and one Saudi context", done: "every inverse you write comes with its domain, and your conversion answer carries units.",
        graph: "g_inv_restrict", graphW: 330,
        tasks: [
          "1.  Find the inverse of f(x) = √(x − 2) for x ≥ 2, and state its domain.",
          "2.  Find the inverse of f(x) = 3/(x − 4), and say which value is excluded from each function.",
          "3.  Restrict the domain of f(x) = x² − 6x + 5 so that an inverse exists, then find it. (Complete the square first.)",
          "4.  The riyal is pegged at 3.75 SAR to the dollar. Write both conversion functions, verify they are inverses, and convert 1 500 SAR to dollars and back.",
        ], lines: 4 },
      { note: "Arguments, not answers", done: "you have an argument, not just an answer.",
        tasks: [
          ["1.  Explain why   ", { eq: "v_ws7", k: 0.95 }, "   must BOTH be shown, and give an example where only one of them holds."],
          "2.  Show that f(x) = |x| has no inverse. Restrict its domain so that it does, and say precisely what information was lost by restricting it.",
          "3.  Prove that the graph of f⁻¹ is the reflection of the graph of f in the line y = x, arguing from the ordered pairs rather than from a picture.",
        ], lines: 5 },
    ],
  },

  pbl: {
    title: "Read the Meter Backwards", minutes: 20,
    subtitle: "A 20-minute group project. Work in fours. Every member signs the sheet.",
    driving: "A receipt shows only the fare. Can you recover the journey from it — and does the order in which charges are applied change what you owe?",
    situation: [
      "A Jeddah taxi charges a 10 SAR flag fall plus 2.50 SAR for every kilometre travelled.",
      "The Saudi riyal is pegged at 3.75 SAR to the US dollar, so converting one way and back returns exactly what you started with.",
      "A second firm adds a 15% surcharge to the whole fare. A visitor wants the price in dollars and asks whether it matters which is done first.",
    ],
    eq: "ctx_taxi",
    steps: [
      ["1", "WRITE THE RULE  (3 min)", "Write the fare as a function of distance, and write its inverse."],
      ["2", "READ A RECEIPT  (4 min)", "A receipt shows 47.50 SAR. Use your inverse to find the distance, and check it forwards."],
      ["3", "CHECK THE PEG  (4 min)", "Write both conversion functions and verify by composition that they undo each other."],
      ["4", "TEST THE ORDER  (6 min)", "Work out the dollar price of the 47.50 SAR fare both ways — surcharge then convert, and convert then surcharge. Are they equal? Explain WHY, using the operations rather than the numbers."],
      ["5", "PRESENT  (3 min)", "Prepare one sentence your presenter will say: what the visitor should be told about the order."],
    ],
    working: [["Step 1 — the rule and its inverse:", 2], ["Step 2 — the distance from the receipt:", 3],
              ["Step 3 — the conversion pair, verified:", 3], ["Step 4 — both orders, and why:", 4],
              ["Step 5 — our sentence:", 2]],
    roles: ["Reader — states the two rules", "Calculator — works both orders", "Checker — composes every inverse both ways", "Presenter — says the sentence"],
    doneWhen: ["The distance is exact and checked forwards.", "Every inverse is verified in BOTH directions.", "Step 4 explains the result with the operations, not just the arithmetic.", "Your sentence makes sense to someone who does not study maths."],
    materials: ["This sheet", "Squared paper", "A pencil and ruler", "A calculator"],
  },
};

(async () => {
  for (const cfg of [GR10_L4, GR11_L6]) await buildAll(cfg);
})();
