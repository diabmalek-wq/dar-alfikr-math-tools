// Week 4 — one lesson per grade, per the Curriculum Distribution.
//   Gr10  Lesson 1-4  Arithmetic Sequences and Series
//   Gr11  Lesson 5-6  Inverse Relations and Functions
//
// Objectives, essential questions, vocabulary, standards, MPs and assessment
// names are quoted VERBATIM from the curriculum map (cmap.docx).
//
// ⚠ GRADE 11, RECORDED SO IT IS NOT LOST: the map's row for Topic 5 Lesson 6
// carries OBJECTIVES COPIED FROM THE INVERSE VARIATION LESSON — direct versus
// inverse variation, reciprocal functions, f(x) = 1/(x−h)+k — and an essential
// question about exponential and logarithmic relationships. Its title, its
// vocabulary (inverse functions, inverse relation) and its five standards
// (HSF.BF.B.4.A and the three (+) BF.B.4 clauses) are all about INVERSE
// FUNCTIONS. Mr Thiab's decision, 16 Sep 2026: teach the standards, and quote
// the map. The deck's learning targets below are therefore the map's own
// STANDARDS, word for word; the map's objectives text is printed verbatim in
// the lesson plan with the mismatch flagged. Nothing in the map was altered.
const { build } = require("./lesson_engine");

const MATH = "math_w4/_index.json";
const GRAPH = "graphs_w4/_index.json";
const ASSESS = ["“Give it a go” questions", "“Time to Check”"];

// =====================================================================
// GRADE 10 · TOPIC 1 · LESSON 4 — Arithmetic Sequences and Series
// =====================================================================
const GR10_L4 = {
  out: "Gr10_T1_L4_Arithmetic_Sequences_and_Series.pptx",
  deckTitle: "Arithmetic Sequences and Series — Grade 10 Algebra II",
  mathIndex: MATH, graphIndex: GRAPH,
  topicLine: "TOPIC 1 · LINEAR FUNCTIONS · LESSON 4",
  lessonTitle: "Arithmetic Sequences and Series",
  titleSize: 38,
  subtitle: "A list that grows by the same step every time — and the fast way to add it up",
  titleEq: "a_seq_w", titleEqK: 1.5,
  titleEqAlt: "The sequence 5, 9, 13, 17, 21 and so on",
  grade: "Grade 10", week: "Week 4 · Semester 1, 2026–27",
  footerLeft: "Grade 10 · Algebra II · Topic 1 · Lesson 4",
  lessonRef: "Lesson 1-4 — Arithmetic Sequences and Series",
  nextLesson: "Solving Equations and Inequalities by Graphing",

  codes: ["HSF.LE.A.2", "HSF.IF.A.3", "HSF.BF.A.1", "HSF.BF.A.1.A", "HSF.BF.A.2"],
  mps: ["MP.4", "MP.6"],
  assessments: ASSESS,

  objectives: [
    "Calculate the common difference in an arithmetic sequence.",
    "Write recursive and explicit formulas of arithmetic sequences.",
    "Find the sums of arithmetic series.",
  ],
  essentialQuestion: "How can the concepts of arithmetic sequences and series be identified and applied to real-world situations?",

  vocabulary: [
    { term: "Sequence", def: "An ordered list of numbers. The order is part of the object — 5, 9, 13 is not the same sequence as 13, 9, 5." },
    { term: "Series", def: "The SUM of the terms of a sequence, not the list of them. One word apart, and it is the commonest confusion in the lesson." },
    { term: "Arithmetic sequence", def: "A sequence in which the step from each term to the next never changes." },
    { term: "Common difference", def: "That fixed step, written d. Found by subtracting any term from the one after it." },
    { term: "Recursive formula", def: "A rule that gives each term from the one before it. It needs a starting term to mean anything." },
    { term: "Explicit formula", def: "A rule that gives any term straight from its position n, with no earlier term needed." },
    { term: "Arithmetic series", def: "The sum of the terms of an arithmetic sequence." },
    { term: "Sigma notation", def: "Σ — a compact way of writing a sum, giving the rule, the starting index and the last index." },
  ],
  vocabSub: "The eight terms the curriculum map lists for this lesson",

  prior: [
    { h: "Subtracting in order", eq: "a_d", d: "Later term minus earlier term. Keep the direction." },
    { h: "Substituting into a rule", eq: "a_exp", d: "n is a position, not a value. Positions start at 1." },
    { h: "Slope of a line", eq: "a_lin", d: "From Lesson 1-1. The step and the slope are the same number." },
  ],
  priorSub: "Three things from Topic 1 — today they become a rule for a whole list",
  carryOver: "An arithmetic sequence is a linear function whose inputs are the positions 1, 2, 3, … The common difference IS the slope. Everything else in this lesson is that one fact, used twice: once to reach a term, once to add them all.",
  carryOverEq: "a_lin",

  diagnose: {
    title: "Warm-Up: Steps and Positions",
    sub: "Answer on Quizizz — 5 questions, 4 minutes. This builds a gap map, not a grade.",
    questions: [
      { eq: "a_d1", t: "Find the common difference." },
      { eq: "a_d2", t: "Find the fourth term." },
      { eq: "a_d3", t: "Answer yes or no, and say how you decided." },
      { eq: "a_d4", t: "Find the first term from the rule." },
      { eq: "a_d5", t: "Work out the sum." },
    ],
    routing: "0–2 correct → re-teach table with me.      3–4 correct → straight to the explicit formula.      5 correct → start the Investigate prompt now.",
  },

  instruction: [
    {
      title: "A Sequence Is a Function on the Positions",
      sub: "Objective 1 — the common difference is the slope, and the points are the sequence",
      graph: "g_ar_points", graphW: 6.4, graphY: 2.5,
      graphAlt: "The terms 5, 9, 13, 17 and 21 plotted against positions 1 to 5, with curved arrows marking a step of plus 4 between consecutive points, and a dashed line through them labelled a n equals 4n plus 1",
      panel: {
        h: "READ IT THIS WAY",
        items: [
          "The sequence is the five POINTS.",
          "There is no term at n = 2.5 — positions are whole numbers.",
          "The dashed line is only there to show the points are collinear.",
          "Collinear is exactly what a constant step means.",
          "So d is the slope, and the sequence is a linear function on the positions.",
        ],
      },
      panelX: 7.3, panelW: 5.6, panelH: 4.0,
      bar: ["WHY THE LINE IS DASHED", "a sequence is a function whose domain is the positive integers, so the graph is dots — never a continuous line."],
      barY: 6.32,
      notes: "Ask for the step before you name it. Misconception to address aloud: students read the dashed line as the sequence and start giving values at non-integer positions. The domain is the positive integers — that is HSF.IF.A.3, and it is why the line is dashed.",
    },
    {
      title: "Two Formulas, Two Different Jobs",
      sub: "Objective 2 — recursive needs the term before; explicit does not",
      rowsHead: ["WHAT IT GIVES YOU", "THE RULE"],
      rowsTop: 2.42, rowH: 0.82,
      rows: [
        ["Recursive — each term from the one before it", { eq: "a_rec", k: 1.55 }],
        ["Explicit — any term straight from its position", { eq: "a_exp", k: 1.75 }],
        ["The same sequence, written explicitly", { eq: "a_exp_ex", k: 1.7 }],
        ["Need the next term? Recursive. Need the 200th? Explicit.", "The number in front of n is always d"],
      ],
      bar: ["A RECURSIVE RULE WITHOUT a₁ IS USELESS", "it has nowhere to start. And whichever rule you write, test it on n = 1 before you trust it — that one substitution catches the n-instead-of-(n−1) error every time."],
      barY: 6.32,
      notes: "Answers: a₁ = 5, d = 4, so aₙ = 5 + (n−1)4 = 4n + 1. Misconception to address aloud: using n instead of n − 1, which gives every term one step too big. Make them test aₙ on n = 1.",
    },
    {
      title: "Modelled Example — I Think Aloud",
      sub: "Objective 3 — adding a run of terms without adding them one at a time",
      graph: "g_ar_pair", graphW: 6.9, graphY: 2.42,
      graphAlt: "Five bars showing the terms 5, 9, 13, 17, 21 in teal, each topped in gold by the same sequence reversed, so every bar reaches the same height of 26, over a width of 5 terms",
      panel: {
        h: "WATCH MY THINKING",
        items: [
          "Write the sum forwards: 5 + 9 + 13 + 17 + 21.",
          "Write it backwards underneath and add in pairs.",
          "Every pair totals 26 — that is a₁ + aₙ.",
          "There are n = 5 pairs, so 2S = 5 × 26 and S = 65.",
          "Check by adding: 5 + 9 + 13 + 17 + 21 = 65.",
        ],
      },
      panelX: 7.6, panelW: 5.3, panelH: 4.0,
      bar: ["THE WHOLE PROOF, IN ONE PICTURE", "twice the sum is n lots of (a₁ + aₙ), so the sum is half of that. Rebuild it this way if the formula ever slips."],
      barY: 6.32,
      notes: "Do the pairing out loud with the five numbers before showing the formula: 5+21, 9+17, 13+13 — all 26. Then 2S = 5 × 26, so S = 65. Check by adding: 5+9+13+17+21 = 65. A student who has seen this picture can rebuild the formula in the exam room.",
    },
  ],

  quickCheck: {
    lead: "Write the explicit rule, then find the tenth term, for", leadW: 5.8,
    eq: "a_qc", k: 1.6,
    think: "Write down d first. Then decide whether you are multiplying by n or by n − 1, and test your rule on n = 1.",
    rule: "80% correct → straight to guided practice.   Below 80% → one more modelled example, this time starting from a negative first term.",
  },

  guided: {
    mins: 4,
    items: [
      { eq: "a_g1", t: "Write the explicit rule and find the fifteenth term.", hint: "The sequence is falling, so d is negative. Keep the sign all the way through." },
      { eq: "a_g2", t: "Find the common difference, then the sum of the first twenty terms.", hint: "From a₁ to a₂₀ is nineteen steps, not twenty." },
    ],
  },

  routes: {
    mins: 8,
    tiers: [
      { items: ["Find the common difference for four sequences, two of them falling.", "Write the explicit rule for two sequences and test each on n = 1.", "Turn a recursive rule into an explicit one.", "Find the twelfth term of a sequence given a₁ and d."],
        help: "You may use: the two formulas on the board, and a partner.",
        done: "your rule gives the right first term when you test it.", eq: "a_ws1" },
      { items: ["Find how many terms a finite sequence has, then its sum.", "Evaluate a sum written in sigma notation.", "Find a₁ and d from two terms that are not next to each other.", "Model a Vision 2030 monthly savings plan and price one year of it in SAR."],
        help: "You may use: the worked example, and the sentence frames.",
        done: "you have counted the terms before you summed them, and your answer carries SAR.", eq: "a_ws6" },
      { items: ["Show that the two sum formulas are the same formula, using the explicit rule.", "Explain why a sequence with a constant difference must be linear in n.", "A sequence has a₃ = 17 and a₈ = 42. Find the rule, and explain why two terms are always enough."],
        help: "You may use: nothing but your reasoning.",
        done: "you have an argument, not just an answer.", eq: "a_ws8" },
    ],
  },

  production: {
    title: "A Vision 2030 Savings Plan",
    sub: "A context you have not seen before — this tests transfer",
    situation: "A graduate in Jeddah joins a savings scheme. She deposits 400 SAR in the first month and increases the deposit by 150 SAR every month after that. The scheme runs for twelve months and pays no interest — the growth is entirely her own increasing deposit.",
    eq: "ctx_save_w", eqK: 1.25,
    tasks: [
      "(a)  Write both formulas for her monthly deposit — recursive and explicit — and say which you would use to find the twelfth deposit.",
      "(b)  Find the twelfth deposit, in SAR.",
      "(c)  Find the total she has saved over the twelve months, in SAR.",
      "(d)  A friend says “she saves about 400 a month, so roughly 4 800 a year”. In one sentence, say what the friend has missed.",
    ],
    note: "Exact values in SAR, and the formula named for every step.",
    aiPrompt: "“Check whether I have used n or n − 1 correctly, and challenge any step I have not justified.”",
  },

  geogebra: {
    sub: "Plot the terms and see the line that is not there",
    explore: "enter Sequence((n, 4n+1), n, 1, 8) and then plot y = 4x + 1 over it. Say aloud why the points are the sequence and the line is not, and what a value at x = 2.5 would mean.",
  },

  gate: {
    eq: "a_gate_w",
    items: [
      { t: "How many terms are in this finite sequence? Show the counting, not a guess.", eq: null },
      { t: "Find the sum of all of them.", eq: null },
      { t: "In ONE sentence, explain why you had to add one when you counted the terms.", eq: null },
    ],
    footer: "Exact answers only. The count shown, the sum exact, and question 3 a reason rather than a restatement.",
    routing: "PASS → Enrichment & Challenge (a sequence given by two non-adjacent terms).      NOT YET → Targeted Learning Clinic on n versus n − 1, start of next lesson.",
  },

  smart: {
    steps: [
      { h: "Show the model", d: "Present the savings plan: both formulas, the twelfth deposit and the twelve-month total, all in SAR." },
      { h: "Expose the trap", d: "Add one worked NON-example — the total found by multiplying the first deposit by twelve — and a sentence saying how a reader would spot the error." },
      { h: "Say why it matters", d: "One caption — “why a rising deposit beats a flat one over a year” — for a non-maths reader." },
    ],
    published: "the class LMS portfolio; the strongest go on the Department wall as our Topic 1 modelling set.",
    reflection: "which still catches you out — the n − 1, or counting how many terms there are?",
  },

  exams: [
    { code: "GAT", full: "Qudurat — General Aptitude", skill: "Numerical series and pattern recognition — finding the next term or the missing one. Arithmetic is about 36% of the quantitative half, the largest strand on the paper.", fmt: "Multiple choice, about 75 seconds per item, no calculator.", tip: "Find the step from the FIRST pair, then confirm it on the second. If it changes, the pattern is not arithmetic and you are looking for something else." },
    { code: "SAAT", full: "Tahsili — Achievement Test", skill: "Sequences and series sit in the Grade 11 band, which is 30% of the mathematics section; the explicit formula and the sum both appear.", fmt: "Four-option multiple choice, mixed with the other subjects.", tip: "Write d before you write anything else. Most wrong options are the right method with the wrong sign of d." },
    { code: "SAT", full: "College Board", skill: "Algebra — linear functions and linear equations in two variables. A table with a constant difference is a linear function, and the SAT asks for the rule rather than the next term.", fmt: "Two 35-minute adaptive modules; calculator allowed throughout.", tip: "Turn the sequence into y = mx + b with m = d. Desmos will then answer the question for you." },
  ],
  examBar: ["THE SINGLE MOST EXAMINED IDEA HERE:", "the step is applied n − 1 times, not n — and when you count terms you divide by the step and ADD ONE."],

  summary: [
    "Find the common difference, keeping its sign.",
    "Write both a recursive and an explicit formula, and say which job each does.",
    "Find any term from its position without listing the ones before it.",
    "Count how many terms a finite sequence has, and sum them.",
    "Model a real savings plan and price a year of it in SAR.",
  ],
  homework: [
    "Finish your product and upload it to the LMS portfolio — any of the three formats.",
    "Practice set on Pear Deck: 12 questions, choose your route.",
    "Watch the flipped video for Lesson 1-5: Solving Equations and Inequalities by Graphing (4 min, 2 embedded questions).",
    "Clinic group: bring your Time to Check paper — we start with 10 minutes on counting terms.",
  ],

  notes: {
    cover: "Week 4 lesson for 10A and 10C, following Piecewise-Defined Functions. Three teaching days this week, so the Smart Production step may run into the next session — protect the Mastery Gate instead.",
    objectives: "All three objectives are verbatim from the curriculum map. The map lists HSF.LE.A.2, HSF.IF.A.3, HSF.BF.A.1, HSF.BF.A.1.A and HSF.BF.A.2 for this lesson, and only MP.4 and MP.6 — do not add others.",
    vocabulary: "All eight terms are the map's list. 'Sequence' and 'series' are one word apart and are the commonest confusion here; make students say which one they are being asked for before they compute.",
    prior: "If a student cannot keep the sign of d when the sequence falls, nothing later in the lesson will hold. Watch for it in the diagnostic.",
    diagnose: "Answers: d = 5; a₄ = 18; no — 2, 6, 18, 54 multiplies by 3, it does not add a constant; a₁ = 5; 30. Expected gap: Q3, where students answer 'yes' because the numbers rise steadily.",
    quickCheck: "Answers: aₙ = 3n − 11, and a₁₀ = 19. Watch for aₙ = 3n − 8, which is the n-instead-of-(n−1) error.",
    guided: "Answers — 1: d = −7, aₙ = 18 − 7n, a₁₅ = −87. 2: d = (97 − 2)/19 = 5, S₂₀ = 20/2 (2 + 97) = 990. Do not release independent work until roughly 80% have both.",
    routes: "Students choose their own route and may switch mid-task. Pear Deck flags error patterns live; use it to decide who gets a two-minute conference.",
    production: "Answers — (a) recursive a₁ = 400, aₙ = aₙ₋₁ + 150; explicit aₙ = 400 + (n−1)150 = 150n + 250; explicit for the twelfth. (b) a₁₂ = 400 + 11(150) = 2 050 SAR. (c) S₁₂ = 12/2 (400 + 2 050) = 14 700 SAR. (d) the friend has treated a rising deposit as a flat one — the deposit is 400 only in the first month.",
    geogebra: "The point of the Sequence( ) command is that GeoGebra draws dots, not a line. A value at x = 2.5 would be a term at position two and a half, which does not exist.",
    gate: "Answers: n = (201 − 6)/5 + 1 = 40 terms; S₄₀ = 40/2 (6 + 201) = 4 140; you add one because the first term was already there before any step was taken. Score live and route privately.",
    smart: "The non-example in step 2 is the highest-value part — 12 × 400 = 4 800 is exactly the mistake a real saver would make.",
    exams: "Show this before homework so the practice set has an obvious purpose.",
    summary: "Route the clinic group privately through the LMS — never announce the list to the class.",
  },
};

// =====================================================================
// GRADE 11 · TOPIC 5 · LESSON 6 — Inverse Relations and Functions
// The learning targets below are the map's own STANDARDS, quoted word for
// word, because the map's objectives text for this row belongs to the
// Inverse Variation lesson. See the header note.
// =====================================================================
const GR11_L6 = {
  out: "Gr11_T5_L6_Inverse_Relations_and_Functions.pptx",
  deckTitle: "Inverse Relations and Functions — Grade 11 Algebra II",
  mathIndex: MATH, graphIndex: GRAPH,
  topicLine: "TOPIC 5 · RADICAL FUNCTIONS · LESSON 6",
  lessonTitle: "Inverse Relations and Functions",
  titleSize: 38,
  subtitle: "Every step you took, taken back — and the one condition that makes it possible",
  titleEq: "v_def_w", titleEqK: 1.25,
  titleEqAlt: "f of f inverse of x equals x, and f inverse of f of x equals x",
  grade: "Grade 11", week: "Week 4 · Semester 1, 2026–27",
  footerLeft: "Grade 11 · Algebra II · Topic 5 · Lesson 6",
  lessonRef: "Lesson 5-6 — Inverse Relations and Functions",
  nextLesson: "Key Features of Exponential Functions",

  codes: ["HSF.BF.B.4.A", "HSF.BF.B.4.B", "HSF.BF.B.4.C", "HSF.BF.B.4.D"],
  mps: ["MP.2", "MP.7"],
  assessments: ASSESS,

  objectives: [
    "Solve an equation of the form f(x) = c for a simple function f that has an inverse and write an expression for the inverse.",
    "Verify by composition that one function is the inverse of another.",
    "Read values of an inverse function from a graph or a table, given that the function has an inverse.",
    "Produce an invertible function from a non-invertible function by restricting the domain.",
  ],
  essentialQuestion: "How can we analyze and represent exponential and logarithmic relationships in different mathematical and real-world contexts?",

  vocabulary: [
    { term: "Inverse relation", def: "The set of ordered pairs with every pair of the original relation reversed: (a, b) becomes (b, a). Every relation has one." },
    { term: "Inverse functions", def: "A pair of functions each of which undoes the other, so that f(f⁻¹(x)) = x and f⁻¹(f(x)) = x. Not every function has one." },
  ],
  vocabSub: "The two terms the curriculum map lists for this lesson",

  prior: [
    { h: "Composing two functions", eq: "v_def", d: "From Lesson 5-5. This is now the CHECK, not the topic." },
    { h: "Making a variable the subject", eq: "v_swap", d: "Swap first, then solve. Two steps, in that order." },
    { h: "The square root of a square", eq: "v_restrict", d: "Why a domain has to be cut before an inverse exists." },
  ],
  priorSub: "Three things from Topic 5 — today they combine into one idea",
  carryOver: "An inverse undoes. That single sentence gives you the method (swap and solve), the check (compose and get x), the graph (reflect in y = x) and the condition (each output may be reached by only one input). Everything in this lesson is that sentence, read four ways.",
  carryOverEq: "v_def",

  diagnose: {
    title: "Warm-Up: Undoing and Checking",
    sub: "Answer on Quizizz — 5 questions, 4 minutes. This builds a gap map, not a grade.",
    questions: [
      { eq: "v_d1", t: "Evaluate." },
      { eq: "v_d2", t: "Evaluate. What do you notice about f and g?" },
      { eq: "v_d3", t: "Rearrange." },
      { eq: "v_d4", t: "Simplify, for a negative x." },
      { eq: "v_d5", t: "Answer yes or no, and say how you decided." },
    ],
    routing: "0–2 correct → re-teach table with me.      3–4 correct → straight to the swap-and-solve method.      5 correct → start the Investigate prompt now.",
  },

  instruction: [
    {
      title: "Swap, Then Solve",
      sub: "Standard BF.B.4.A — solve f(x) = c and write an expression for the inverse",
      rowsHead: ["THE STEP", "WHAT IT LOOKS LIKE"],
      rowsTop: 2.42, rowH: 0.86,
      rows: [
        ["Write y = f(x), then SWAP x and y — before any algebra", { eq: "v_swap", k: 1.45 }],
        ["Reversing the pairs is the same thing said another way", { eq: "v_relation", k: 1.6 }],
        ["What the −1 does NOT mean", { eq: "v_notrecip", k: 1.6 }],
      ],
      bar: ["SWAP FIRST, SOLVE SECOND", "solving before you swap gives the same algebra with the letters in the wrong places. And the −1 names the undoing function — it is not an exponent."],
      barY: 6.32,
      notes: "Answer: f⁻¹(x) = (x + 8)/3. Misconception to address aloud, and it is the big one: students write 1/(3x − 8). Say it out loud once, write it on the board, and cross it out.",
    },
    {
      title: "The Check Is Composition, Not the Graph",
      sub: "Standard BF.B.4.B — verify by composition that one function is the inverse of another",
      graph: "g_inv_reflect", graphW: 4.0, graphY: 2.42,
      graphAlt: "The line f of x equals 3x minus 8 and its inverse the line x plus 8 over 3, mirrored in the dashed line y equals x, with the points 3 comma 1 and 1 comma 3 marked and joined by an arrow",
      panel: {
        h: "TWO WAYS ROUND, EVERY TIME",
        items: [
          "Put f⁻¹ inside f. You should get x.",
          "Put f inside f⁻¹. You should get x as well.",
          "One direction alone is not proof — it can hold on a restricted set.",
          "The reflection in y = x is the picture of the same fact.",
          "This check works in the exam room, where drawing a graph does not.",
        ],
      },
      panelX: 8.0, panelW: 4.9, panelH: 4.1,
      notes: "Work f(f⁻¹(x)) = 3((x+8)/3) − 8 = x aloud, then the other way. Misconception: students check one direction and stop. Point at (3, 1) and (1, 3) on the graph and ask which function each belongs to.",
    },
    {
      title: "When There Is No Inverse — Yet",
      sub: "Standards BF.B.4.C and BF.B.4.D — read values off a graph, and restrict a domain",
      graph: "g_inv_restrict", graphW: 4.0, graphY: 2.42,
      graphAlt: "The parabola y equals x squared drawn solid for x greater than or equal to zero and dashed for x less than zero, with its inverse the square root curve reflected in the dashed line y equals x",
      panel: {
        h: "THE HORIZONTAL LINE TEST",
        items: [
          "Slide a horizontal line down the graph.",
          "If it ever meets the curve twice, two inputs share an output.",
          "Reverse the pairs and that output would need two outputs — not a function.",
          "Cutting the domain to x ≥ 0 throws away the duplicate.",
          "The inverse's DOMAIN is the original's RANGE. Write both down.",
        ],
      },
      panelX: 7.8, panelW: 5.1, panelH: 4.1,
      notes: "Answers: y = x² fails the horizontal line test because 3 and −3 both give 9. Restricted to x ≥ 0 its inverse is √x, with domain x ≥ 0. Say plainly that the restriction is not a technicality the examiner added — it is the reason the radical sign is defined to give the non-negative root.",
    },
  ],

  quickCheck: {
    lead: "Find the inverse, then check it by composing both ways, for", leadW: 6.4,
    eq: "v_qc", k: 1.6,
    think: "Swap first. Then, before you write the answer, put one function inside the other and see whether you get x.",
    rule: "80% correct → straight to guided practice.   Below 80% → one more modelled example, this time with a fraction in the rule.",
  },

  guided: {
    mins: 4,
    items: [
      { eq: "v_g1", t: "Find the inverse and verify it by composition, both ways round.", hint: "Swap, subtract, then divide — in that order." },
      { eq: "v_g2", t: "Find the inverse and state its domain.", hint: "A cube root accepts negatives, so nothing has to be cut here. Say why." },
    ],
  },

  routes: {
    mins: 8,
    tiers: [
      { items: ["Find the inverse of four linear functions by swapping and solving.", "Verify two of them by composition, both ways round.", "Read f⁻¹(5) off a given graph without finding a formula.", "Reverse a table of values to write the inverse as a set of pairs."],
        help: "You may use: the four-step method on the board, and a partner.",
        done: "your composition gives x both ways round, every time.", eq: "v_ws1" },
      { items: ["Find the inverse of a radical function and state its domain.", "Find the inverse of a rational function and say which value is excluded.", "Restrict the domain of a quadratic so that an inverse exists, then find it.", "Convert SAR to US dollars and back, and say why the pegged rate makes these exact inverses."],
        help: "You may use: the worked example, and the sentence frames.",
        done: "every inverse you write comes with its domain, and your conversion answer carries units.", eq: "v_ws3" },
      { items: ["Explain why one composition is not enough to prove two functions are inverses, with an example.", "Show that f(x) = |x| has no inverse, then produce one by restricting the domain — and say what you lost.", "Prove that the graph of any inverse is the reflection of the original in y = x, using the pairs."],
        help: "You may use: nothing but your reasoning.",
        done: "you have an argument, not just an answer.", eq: "v_ws8" },
    ],
  },

  production: {
    title: "Riyals, Dollars and a Jeddah Taxi",
    sub: "A context you have not seen before — this tests transfer",
    situation: "The Saudi riyal is pegged at 3.75 SAR to the US dollar, so converting one way and back is an exact undoing. A Jeddah taxi charges a 10 SAR flag fall plus 2.50 SAR per kilometre.",
    eq: "ctx_sar_w", eqK: 1.25,
    tasks: [
      "(a)  Write the two conversion functions and verify by composition that they are inverses.",
      "(b)  Write the taxi fare as a function F of distance d, and find its inverse.",
      "(c)  A passenger is charged 47.50 SAR. Use your inverse to find the distance travelled.",
      "(d)  A second taxi firm adds a 15% surcharge to the whole fare. Is “convert then surcharge” the same as “surcharge then convert”? Justify your answer.",
    ],
    note: "Exact values, units named, and every inverse checked by composition.",
    aiPrompt: "“Check whether I have verified the inverse in both directions, and challenge any step I have not justified.”",
  },

  geogebra: {
    sub: "Type a function and its inverse, and watch the mirror",
    explore: "enter f(x) = 3x − 8 and g(x) = (x + 8)/3, then the line y = x. Drag a point along f and watch its mirror on g. Then try f(x) = x² and say aloud why the reflection is not a function.",
  },

  gate: {
    eq: "v_gate_w",
    items: [
      { t: "Find the inverse of the function shown.", eq: null },
      { t: "Verify your answer by composition — both ways round.", eq: null },
      { t: "In ONE sentence, explain why checking only one direction would not be enough.", eq: null },
    ],
    footer: "Exact answers only. Both compositions shown in full, and question 3 a reason rather than a restatement.",
    routing: "PASS → Enrichment & Challenge (restrict a quadratic's domain and invert it).      NOT YET → Targeted Learning Clinic on swap-then-solve, start of next lesson.",
  },

  smart: {
    steps: [
      { h: "Show the model", d: "Present the taxi fare function and its inverse, with the 47.50 SAR fare converted back to a distance." },
      { h: "Expose the trap", d: "Add one worked NON-example — the inverse written as the reciprocal, 1 over the fare rule — and a sentence saying how a reader would spot the error." },
      { h: "Say why it matters", d: "One caption — “why a meter can be read backwards but a surcharge cannot be undone in any order” — for a non-maths reader." },
    ],
    published: "the class LMS portfolio; the strongest go on the Department wall as our Topic 5 modelling set.",
    reflection: "which is still harder for you — remembering to swap first, or remembering to check both ways?",
  },

  exams: [
    { code: "SAAT", full: "Tahsili — Achievement Test", skill: "Inverse functions sit in the Grade 11 band, which is 30% of the mathematics section. Asked as ‘find f⁻¹’, as ‘which graph is the inverse’, and as a composition that quietly cancels to x.", fmt: "Four-option multiple choice, no calculator.", tip: "If an expression looks like heavy algebra, check whether the two functions are inverses before you expand anything. Many items collapse to x in one line." },
    { code: "SAT", full: "College Board", skill: "Advanced Math — equivalent expressions and nonlinear functions, about 35% of the Mathematics section. The domain restriction is usually where the wrong options come from.", fmt: "Two 35-minute adaptive modules; calculator allowed throughout.", tip: "Test a number. Put 2 into f, take the output into your candidate inverse, and see whether 2 comes back." },
    { code: "GAT", full: "Qudurat — General Aptitude", skill: "Undoing a rule appears inside algebra and word problems — given the output of a process, find the input. Algebra is about 18% of the quantitative half.", fmt: "Multiple choice, about 75 seconds per item, no calculator.", tip: "Work backwards through the operations in reverse order. It is the same idea with no notation attached." },
  ],
  examBar: ["THE SINGLE MOST EXAMINED IDEA HERE:", "f⁻¹ is not 1/f — and an inverse is only proved when the composition gives x in BOTH directions."],

  summary: [
    "Find an inverse by swapping x and y and then solving.",
    "Verify an inverse by composition, both ways round.",
    "Read a value of an inverse function straight off a graph or a table.",
    "Say why a function fails the horizontal line test, and restrict its domain so that it passes.",
    "State the inverse's domain as the original's range, without being asked twice.",
  ],
  homework: [
    "Finish your product and upload it to the LMS portfolio — any of the three formats.",
    "Practice set on Pear Deck: 12 questions, choose your route.",
    "Watch the flipped video for Lesson 6-1: Key Features of Exponential Functions (4 min, 2 embedded questions).",
    "Clinic group: bring your Time to Check paper — we start with 10 minutes on swap-then-solve.",
  ],

  notes: {
    cover: "Week 4 lesson for 11B, following Operations on Functions. Three teaching days this week, so the Smart Production step may run into the next session — protect the Mastery Gate instead.",
    objectives: "IMPORTANT. The learning targets on this slide are the map's own STANDARDS for this row, quoted word for word. The map's objectives COLUMN for Lesson 5-6 has been copied from the Inverse Variation lesson — it names direct and inverse variation and the reciprocal function, and the essential question is about exponentials and logarithms. The lesson plan prints that column verbatim with the mismatch flagged. Raise it with the HOD; do not quietly correct the map.",
    vocabulary: "Only two terms are listed by the map, and they are not the same thing: every relation has an inverse RELATION, but only a one-to-one function has an inverse FUNCTION. Make that distinction explicitly — it is the whole of standard BF.B.4.D.",
    prior: "Composition was Lesson 5-5. It is no longer the topic; it is the tool that proves the answer. Say that out loud so students see the continuity.",
    diagnose: "Answers: f(4) = 17; f(g(2)) = 2, and f and g undo each other; x = (y + 1)/5; √(x²) = −x when x is negative; no, 1 and 2 both map to 4. Expected gap: Q4 and Q5, which are the two that decide whether the restriction idea lands later.",
    quickCheck: "Answer: f⁻¹(x) = 2x + 5. Watch for 2/(x − 5) and for (x/2) − 5 — the first is the reciprocal error, the second is solving before swapping.",
    guided: "Answers — 1: f⁻¹(x) = (x − 3)/7, and both compositions give x. 2: f⁻¹(x) = ∛(x + 4), domain all real numbers, because a cube root accepts negatives. Do not release independent work until roughly 80% have both.",
    routes: "Students choose their own route and may switch mid-task. Pear Deck flags error patterns live; use it to decide who gets a two-minute conference.",
    production: "Answers — (a) U(S(u)) = 3.75u/3.75 = u and S(U(s)) = s. (b) F(d) = 10 + 2.5d, F⁻¹(c) = (c − 10)/2.5. (c) (47.50 − 10)/2.5 = 15 km. (d) yes for this pair — multiplying by 1.15 and dividing by 3.75 commute, because both are multiplications by a constant. Push for that REASON, not the yes.",
    geogebra: "The x² case is the one that matters: the reflection of a parabola in y = x is a sideways parabola, which fails the vertical line test. That picture is standard BF.B.4.D in one image.",
    gate: "Answer: f⁻¹(x) = (5x − 1)/2. Both compositions must be shown: f(f⁻¹(x)) = (2((5x−1)/2) + 1)/5 = x, and f⁻¹(f(x)) = (5((2x+1)/5) − 1)/2 = x. One direction alone can hold on a restricted set, which is why both are required. Score live and route privately.",
    smart: "The non-example in step 2 is the highest-value part — writing 1/(10 + 2.5d) is the single most common error in this topic on both papers.",
    exams: "Show this before homework so the practice set has an obvious purpose.",
    summary: "Route the clinic group privately through the LMS — never announce the list to the class.",
  },
};

(async () => {
  for (const cfg of [GR10_L4, GR11_L6]) await build(cfg);
})();
