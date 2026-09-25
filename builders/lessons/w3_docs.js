// Week 3 documents — lesson plans, classwork, differentiation, PBL.
// Objectives / EQ / vocabulary / assessments verbatim from the curriculum map.
const { buildAll } = require("./docs_engine");

const MATHDOC = "math_w3_doc/_index.json";
const GRAPH = "graphs_w3/_index.json";
const ASSESS = ["“Give it a go” questions", "“Time to Check”"];
const T = { t1: 6, t2: 18, t3: 12, t4: 12, t5: 6, t6: 6 };

const AI_CRITIC = "Role of AI: critic only. Briefed prompt — “Challenge my reasoning and point out any step I have not justified.” Never “solve this”.";
const PILLAR_ADAPTIVE = [
  "Entry branch — the Quizizz result routes each student to the re-teach table, straight to modelling, or the Investigate prompt.",
  "Mid-lesson branch — Pear Deck flags error patterns during independent practice; flagged students get a 2-minute micro-conference while others continue.",
  "Exit branch — the Mastery Gate routes each student: PASS → Enrichment & Challenge; NOT YET → Targeted Learning Clinic at the start of the next lesson.",
  "Routing is communicated privately through the LMS, never read aloud.",
];

// =====================================================================
// GR10 · 1-3 · Piecewise-Defined Functions
// =====================================================================
const GR10_L3 = {
  slug: "Gr10_T1_L3_Piecewise_Defined_Functions",
  mathDocIndex: MATHDOC, graphIndex: GRAPH, timings: T,
  lessonTitle: "Piecewise-Defined Functions",
  unit: "Topic 1 — Linear Functions · Lesson 3",
  gradeFull: "Grade 10 — Algebra II",
  week: "Week 3 · Semester 1, 2026–27",
  lessonLine: "Grade 10 · Algebra II · Topic 1: Linear Functions · Lesson 3 — Piecewise-Defined Functions",
  codes: ["HSF.IF.B.5", "HSF.IF.C.7.B", "HSF.LE.A.2", "HSS.ID.B.6.A"], mps: ["MP.4", "MP.5"],
  assessments: ASSESS,
  objectives: [
    "Create and graph piecewise-defined functions, including absolute value and step functions.",
    "Write piecewise-defined functions based on given graphs.",
    "Create and use piecewise-defined functions to model and analyze real-world data.",
  ],
  essentialQuestion: "How can piecewise-defined functions be used to model real-world situations?",
  vocabList: "absolute value function ; ceiling function ; disjoint ; floor function ; piecewise-defined function ; step function ; subintervals",

  plan: {
    outcome: [
      "Students will choose the correct rule for any input and justify the choice by naming the subinterval.",
      "Students will graph piecewise, absolute value and step functions with open and closed circles placed correctly.",
      "Students will write a piecewise-defined function from a graph, and model a two-rate charge in SAR.",
    ],
    preclass: [
      "Flipped video (4 min): “One function, more than one rule” — reading a two-rule function and choosing the rule. Posted on the LMS 48 hours ahead.",
      "Two embedded EdPuzzle questions: one evaluation either side of a boundary, one floor value.",
      "Evidence of readiness: EdPuzzle completion report plus both embedded answers submitted before the bell.",
    ],
    diagTool: [
      "5-question Quizizz (≤ 4 minutes): evaluate a two-rule function, evaluate |3 − 5|, evaluate ⌊7.9⌋ and ⌈2.1⌉, and decide whether −3 sits inside x ≥ −3.",
      "Cross-referenced against overnight EdPuzzle watch analytics — who watched, who skipped, who missed the embedded items.",
      "Answers: f(−2) = 2 by the first rule ; 2 ; 7 ; 3 ; yes, closed circle.",
    ],
    diagGap: [
      "Expected gap 1 — the boundary: students substitute into whichever rule they read first instead of checking the subinterval.",
      "Expected gap 2 — floor and ceiling: students round to the nearest integer rather than down or up, and negatives make it worse.",
      "If more than half miss the floor and ceiling items, run that re-teach before the modelled example.",
      "Routing: 0–2 correct → re-teach table.  3–4 → straight to modelling.  5 → begin the Investigate prompt immediately.",
    ],
    instruction: [
      "Direct explanation (3–5 min, flagged students only): the boundary can be owned by only one piece, so exactly one circle is filled.",
      "Whole class: three familiar graphs shown as one family — the absolute value V, a two-piece linear function, and the floor step function.",
      "The number-line picture of disjoint subintervals, with the open and closed circle convention read off it.",
      "Modelled example, thinking aloud: f(x) = 2x + 1 for x < 1 and 5 − x for x ≥ 1. Graph each rule lightly, then rub out what it does not own.",
      "Narration focus — the rubbing-out step, which is the step students skip and the reason they draw full lines across the plane.",
      "This is a NEW example — it does not repeat the flipped video.",
    ],
    quickCheck: [
      "On whiteboards, 60 seconds: find f(−1) and f(0) for f(x) = −2x when x ≤ −1 and x² when x > −1.",
      "Expected: f(−1) = 2 by the first rule, since −1 ≤ −1 ; f(0) = 0 by the second.",
      "80% correct → release guided practice. Below 80% → one further modelled example, this time reading values off the graph.",
    ],
    guided: [
      "Two “Give it a go” problems, identical for every student, worked together with the teacher:",
      "(1) f(x) = 3x − 2 for x < 2 and 4 for x ≥ 2 — graph it and state f(0), f(2), f(5).  (2) f(x) = |x + 3| − 2 — graph it, state the vertex and the domain.",
      "Answers: f(0) = −2, f(2) = 4, f(5) = 4 ; vertex (−3, −2), domain all real numbers.",
      "Feedback: worked live on the board step by step; students self-mark and circle their OWN first error.",
    ],
    independent: [
      "Delivered through the “Choose Your Route” sheet with live feedback in Pear Deck. Routes are named for the task, not for the student.",
      "PRACTICE — Secure the method. Evaluate four piecewise functions, graph two two-piece linear functions, evaluate floor and ceiling expressions, sketch an absolute value translation. Done when: you choose the correct rule every time and your circles are right.",
      "APPLY — Use it in context. Write a function from a graph, model a Saudi electricity bill, graph a three-piece function, interpret a step-function parking charge. Done when: your function matches the graph exactly and your context answer carries SAR.",
      "INVESTIGATE — Find out why. Justify the absolute value function as piecewise, show floor and ceiling never agree on a non-integer, design a continuous piecewise function and prove it. Done when: you have an argument, not just an answer.",
      "Every student sits the same Mastery Gate. The gate is not differentiated, because it is the evidence.",
    ],
    production: [
      "Non-routine transfer task — this context has not appeared in practice.",
      "Residential electricity in the Kingdom is billed at 18 halalas per kWh for the first 6000 kWh in a month and 30 halalas per kWh above that: C(x) = 0.18x for 0 ≤ x ≤ 6000, and 1080 + 0.30(x − 6000) for x > 6000.",
      "(a) Explain why the cost is not a single linear rule. (b) Find the bill for 5200 kWh and for 8400 kWh, in SAR. (c) The family cuts usage from 8400 to 6900 kWh — find the saving and explain why it exceeds 18 halalas per unit. (d) Sketch the graph and mark the boundary.",
      "Answers: (a) the rate changes at 6000 kWh, so no single slope fits. (b) 936 SAR and 1800 SAR. (c) 6900 kWh costs 1350 SAR, a saving of 450 SAR, because every unit removed came out of the 30-halala band. (d) two segments meeting at (6000, 1080).",
      "Students then hand their reasoning to the AI critic and ask it to challenge any step they have not justified.",
    ],
    criteria: [
      "Minimum acceptable standard: the correct rule used for each consumption level, every answer in SAR, and the boundary named.",
      AI_CRITIC,
      "Completed independently by the student: the written justification for parts (a)–(d). AI may challenge it; it may not write it.",
    ],
    evidence: [
      "“Time to Check” — one individual task. No notes, no partner, no AI.",
      "Given a graph made of a horizontal segment at y = 3 for x < 2 with an open circle at (2, 3), and a line from a closed circle at (2, 1): 1. write the piecewise-defined function. 2. state f(2) and say how the graph told you which rule to use. 3. in ONE sentence explain why one circle at x = 2 must be open.",
      "Answer: f(x) = 3 for x < 2 and x − 1 for x ≥ 2 ; f(2) = 1, from the closed circle ; if both were closed, x = 2 would have two outputs and it would not be a function.",
      "Done when: both rules and both subintervals are exact, the inequality signs match the circles, and question 3 gives a reason rather than a restatement.",
      "Scored live in Pear Deck as submissions arrive; result logged in the Impact Dashboard Mastery Rate.",
    ],
    refinement: [
      "Students revise their tariff reasoning using the AI critique and the teacher's micro-conference note.",
      "Final product, three equally acceptable formats: a Canva one-pager, a photographed hand-written solution, or a 45-second voice note.",
      "Required content: the tariff function with its graph and the boundary marked in SAR; ONE worked non-example, a bill computed entirely at the wrong rate, with a sentence on how a reader would spot it; and a caption on why a utility charges in bands.",
      "Graded on originality and clarity of reasoning, not correctness alone.",
    ],
    publication: [
      "Published to the class LMS portfolio; the strongest go on the Mathematics Department wall as the Topic 1 modelling set.",
      "Reflection question: “Which is still harder for you — choosing the rule, or drawing the circles?”",
    ],
    differentiation: [
      "PRACTICE — Secure the method. Evaluation, two graphs, floor and ceiling values, and one absolute value sketch; the boundary rule stays on the board and a partner is allowed. Done when: the correct rule is chosen every time and the circles are right.",
      "APPLY — Use it in context. A function written from a graph, a two-rate electricity model, a three-piece graph, and a step-function parking charge. Done when: the function matches the graph and the context answer carries SAR.",
      "INVESTIGATE — Find out why. The absolute value justification, the floor-versus-ceiling argument, and a continuity design task. Done when: there is an argument, not just an answer.",
      "No student is labelled. The routes describe tasks; every student sits the same Mastery Gate.",
    ],
    adaptive: PILLAR_ADAPTIVE,
    saudi: [
      "Production context: the Saudi residential electricity tariff — 18 halalas per kWh to 6000 kWh, 30 halalas above it — used to compare two months and price a saving in SAR.",
      "In-class project: a shopping-centre car park in Jeddah charging 3 SAR for every started hour, modelled as a ceiling step function.",
      "Discussion prompt: why Vision 2030 efficiency programmes publish banded tariffs rather than one flat rate.",
    ],
    exams: [
      "SAT — Advanced Math and Problem-Solving & Data Analysis: piecewise and absolute value models and rate-of-change reading, roughly 35% and 15% of the Mathematics section. Practice tip: Desmos accepts brace notation — graph it and read the value.",
      "SAAT (Tahsili) — evaluating a piecewise function and reading a step graph, in the Grade 10 and 11 function bands. Practice tip: underline the inequality signs before substituting.",
      "GAT (Qudurat) — two-rate charges inside arithmetic and data items, the largest quantitative strand, about 75 seconds per question. Practice tip: find the boundary value first; most wrong options apply one rate to the whole amount.",
    ],
  },

  plan2026: {
    day: "Sunday, Week 3", section: "Grade 10 — 10A and 10C",
    tools: "Quizizz (diagnostic) · Pear Deck (live practice feedback) · GeoGebra Graphing Calculator · Canva (final product) · Whiteboards",
    resources: "Lesson presentation (18 slides) · “Choose Your Route” differentiation sheet · “Give It a Go” classwork · “Three Rates, One Bill” project task · squared paper",
    competencies: ["Selecting the correct rule before computing.", "Interpreting a mathematical model of a real charge in SAR."],
    technology: ["Quizizz live diagnostic with instant gap analysis.", "GeoGebra If( ) syntax to graph a piecewise function and inspect the boundary."],
    reallife: ["The Saudi residential electricity tariff and a family's monthly bill.", "A Jeddah car park charging by the started hour."],
    values: ["Precision — the right rule for the right input.", "Responsibility for household consumption and its cost."],
    soft: ["Collaboration in assigned group roles.", "Explaining a choice of rule to a peer before computing."],
    hard: ["Evaluating and graphing piecewise, absolute value and step functions.", "Writing a piecewise function from a graph and modelling a banded charge."],
    phases: [
      "FIKR Phase 1 — Diagnose. 5-question Quizizz on choosing a rule, absolute value, floor and ceiling. Results read as a gap map; students routed to the re-teach table, straight to modelling, or the Investigate prompt.",
      "FIKR Phase 2 — Targeted Instruction. Focused re-teach on boundaries for flagged students. Whole class: the three familiar graphs as one family; disjoint subintervals on a number line; modelled example graphed rule by rule. Quick check on whiteboards.",
      "FIKR Phase 3 — Practice. Two identical “Give it a go” problems worked together. Students then choose a route on the “Choose Your Route” sheet and may switch at any time. Live feedback via Pear Deck; 2-minute micro-conferences.",
      "FIKR Phase 4 — Production. The Saudi electricity tariff: compare two months, price a saving, and sketch the banded graph. AI used as critic only.",
      "FIKR Phase 5 — Proof of Learning. “Time to Check” — write the piecewise function for an unseen graph. No notes, no partner, no AI.",
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
    closure: "Two minutes of peer show-and-tell on the final products, then the reflection question: “Which is still harder for you — choosing the rule, or drawing the circles?”",
    homework: "Finish the final product and upload to the LMS portfolio (any of the three formats). Practice set on Pear Deck — 12 questions, choose your route. Watch the flipped video for Lesson 1-4: Arithmetic Sequences and Series. Clinic group: bring your Time to Check paper.",
  },

  classwork: {
    subtitle: "Show all your working. Before you substitute, write down which subinterval the input belongs to.",
    sections: [
      { h: "SECTION A — Choosing the rule", note: "Objective 1", lines: 4,
        q: [
          { n: "Q1", eq: "p_ws1", t: "Find f(−4), f(−1) and f(3). State the rule you used each time." },
          { n: "Q2", eq: "p_ws2", t: "Find f(−2), f(0) and f(5). One of these is on a boundary — say which." },
          { n: "Q3", eq: "p_ws3", t: "State the vertex and sketch the graph." },
          { n: "Q4", eq: "p_ws4", t: "Describe the graph in words, then sketch it." },
        ] },
      { h: "SECTION B — Step functions", note: "Objective 1", lines: 4,
        intro: "Use the three-panel comparison from the lesson if you need it.",
        graph: "g_pw_panel", graphW: 560,
        q: [
          { n: "Q5", eq: "p_ws5", t: "Find f(2.4), f(−0.5) and f(3). Then sketch the graph for −2 ≤ x ≤ 4." },
          { n: "Q6", eq: "p_ws6", t: "Find f(1.2) and f(−1.6). Explain what the 2 inside the ceiling does to the width of each step." },
        ] },
      { h: "SECTION C — Working backwards from a graph", note: "Objective 2", lines: 5,
        intro: "The graph below shows a piecewise-defined function.",
        graph: "g_pw_gate", graphW: 380,
        text: [
          "Q7.  Write the piecewise-defined function for the graph shown.",
          "Q8.  State f(2), and say how the graph told you which rule to use.",
          "Q9.  A student writes the second rule as x + 1. Explain, in one sentence, exactly what they got wrong.",
        ] },
      { h: "SECTION D — Modelling a real charge", note: "Objective 3 · MP.4", lines: 5,
        intro: "A Jeddah car park charges 3 SAR for every started hour: P(t) = 3⌈t⌉.",
        text: [
          "Q10.  Find the charge for a stay of 2 hours 10 minutes, and for a stay of exactly 3 hours.",
          "Q11.  A driver stays 4 hours 55 minutes and is charged 15 SAR. Explain why, using the ceiling function.",
          "Q12.  Sketch the graph of P for 0 < t ≤ 5, with the circles the right way round.",
        ] },
    ],
  },

  diffSheet: {
    routes: [
      { note: "Evaluate and graph", done: "you choose the correct rule every time, and your circles are right.",
        intro: "For each function, find the values asked for and state which rule you used.",
        grid: [["1.", "p_ws1"], ["2.", "p_ws2"], ["3.", "p_d1"], ["4.", "p_g1"], ["5.", "p_ws5"], ["6.", "p_ws6"]],
        tasks: ["7.  Choose any two of the functions above and sketch them on squared paper, with open and closed circles marked."],
        lines: 2 },
      { note: "From graphs, and one Saudi context", done: "your function matches the graph exactly, and your context answer carries SAR.",
        intro: "Work from the picture to the function, then apply what you find.",
        graph: "g_pw_tariff", graphW: 400,
        tasks: [
          "1.  The graph above shows the residential electricity tariff. Write the piecewise function it represents, using x for kWh and C for SAR.",
          "2.  Find the bill for 4500 kWh and for 7800 kWh. Show which rule you used each time.",
          "3.  A household pays 1620 SAR. How many kWh did it use? Explain why you must test the boundary first.",
          "4.  Graph f(x) = ½x + 3 for x < −2, x² − 1 for −2 ≤ x ≤ 2, and 5 for x > 2. Mark every circle.",
        ], lines: 4 },
      { note: "Arguments, not answers", done: "you have an argument, not just an answer.",
        tasks: [
          ["1.  Show that   ", { eq: "p_abs_pw", k: 1.1 }, "   really is the definition of the absolute value function, and explain why the two pieces cannot both own x = 0."],
          "2.  Prove that ⌊x⌋ and ⌈x⌉ are never equal when x is not an integer, and always equal when it is.",
          "3.  Design a two-piece function that is continuous at its boundary — the graph has no jump. State your two rules and prove the two pieces agree at the boundary.",
        ], lines: 5 },
    ],
  },

  pbl: {
    title: "Three Rates, One Bill", minutes: 20,
    subtitle: "A 20-minute group project. Work in fours. Every member signs the sheet.",
    driving: "A family wants a lower electricity bill. Where exactly does the money go, and which unit of consumption is worth cutting first?",
    situation: [
      "Residential electricity in the Kingdom is billed in bands: 18 halalas per kWh for the first 6000 kWh in a month, and 30 halalas per kWh for everything above it.",
      "The family's bills for two summer months were 5200 kWh and 8400 kWh. They are considering a timer on the split units, which the supplier says would cut about 1500 kWh from the higher month.",
      "They want to know the saving before they spend anything on the timer.",
    ],
    eq: "ctx_tariff",
    steps: [
      ["1", "READ THE MODEL  (4 min)", "Write the piecewise function in your own notation and state, in one sentence, what changes at 6000 kWh."],
      ["2", "PRICE BOTH MONTHS  (4 min)", "Find the bill for 5200 kWh and for 8400 kWh. Give both in SAR and name the rule you used each time."],
      ["3", "PRICE THE SAVING  (4 min)", "Find the bill after the 1500 kWh cut, and the saving in SAR."],
      ["4", "EXPLAIN THE SURPRISE  (5 min)", "The saving is more than 1500 × 18 halalas. Explain in writing why, using the bands rather than the numbers."],
      ["5", "PRESENT  (3 min)", "Prepare one sentence your presenter will say: which units are the expensive ones, and why."],
    ],
    working: [["Step 1 — the model, and what changes at 6000:", 2], ["Step 2 — both bills:", 3],
              ["Step 3 — the saving:", 2], ["Step 4 — why the saving is bigger than expected:", 4],
              ["Step 5 — our sentence:", 2]],
    roles: ["Reader — states the two bands", "Calculator — prices both months", "Checker — tests every claim", "Presenter — says the sentence"],
    doneWhen: ["Both bills are exact and in SAR.", "The rule used is named for every calculation.", "Step 4 explains the saving using the BANDS, not just arithmetic.", "Your sentence makes sense to someone who does not study maths."],
    materials: ["This sheet", "Squared paper", "A pencil and ruler", "A calculator"],
  },
};

// =====================================================================
// GR11 · 5-5 · Operations on Functions
// =====================================================================
const GR11_L5 = {
  slug: "Gr11_T5_L5_Operations_on_Functions",
  mathDocIndex: MATHDOC, graphIndex: GRAPH, timings: T,
  lessonTitle: "Operations on Functions",
  unit: "Topic 5 — Rational Exponents and Radical Functions · Lesson 5",
  gradeFull: "Grade 11 — Algebra II",
  week: "Week 3 · Semester 1, 2026–27",
  lessonLine: "Grade 11 · Algebra II · Topic 5: Rational Exponents and Radical Functions · Lesson 5-5 — Operations on Functions",
  codes: ["HSF.BF.A.1.B", "(+)HSF.BF.A.1"], mps: ["MP.4", "MP.7"],
  assessments: ASSESS,
  objectives: [
    "Combine functions using arithmetic operations.",
    "Combine functions using function composition.",
  ],
  essentialQuestion: "In what ways can we combine functions to create new functions?",
  vocabList: "composite function ; composition",

  plan: {
    outcome: [
      "Students will add, subtract, multiply and divide two functions and state the domain of the result.",
      "Students will build a composite function by substituting one whole function into another.",
      "Students will show that f ∘ g and g ∘ f are generally different, and model a two-step charge as a composition.",
    ],
    preclass: [
      "Flipped video (4 min): “Inside first” — the function machine, and why the symbol order and the working order are opposites. Posted on the LMS 48 hours ahead.",
      "Two embedded EdPuzzle questions: one numerical composition, one expansion of a squared bracket.",
      "Evidence of readiness: EdPuzzle completion report plus both embedded answers submitted before the bell.",
    ],
    diagTool: [
      "5-question Quizizz (≤ 4 minutes): a sum of two functions, a product evaluated at a point, a numerical composition, the condition for a quotient to be undefined, and the meaning of (f ∘ g)(x) in words.",
      "Cross-referenced against overnight EdPuzzle watch analytics — who watched, who skipped, who missed the embedded items.",
      "Answers: 3x − 5 ; −21 ; 9 ; when g(x) = 0 ; f of g of x, inside first.",
    ],
    diagGap: [
      "Expected gap 1 — order: students read (f ∘ g)(x) left to right and apply f first.",
      "Expected gap 2 — the bracket: substituting g into f and then expanding without keeping the bracket, so (x + 3)² becomes x² + 9.",
      "If more than half describe (f ∘ g)(x) as a product, stop and redraw the machine before anything else.",
      "Routing: 0–2 correct → re-teach table.  3–4 → straight to modelling.  5 → begin the Investigate prompt immediately.",
    ],
    instruction: [
      "Direct explanation (3–5 min, flagged students only): the inside function runs first, because its output is what the outside function receives.",
      "Whole class: the four arithmetic operations in a single table, with the domain rule for each — including the exclusion of every zero of g in a quotient.",
      "The composition machine read aloud: x enters g, g(x) leaves g and enters f, f(g(x)) leaves f.",
      "Modelled example, thinking aloud: f(x) = x² − 4 and g(x) = x + 3, both compositions worked, then graphed side by side.",
      "Narration focus — “every x in f becomes the WHOLE of g”, and the bracket stays until the expansion is finished.",
      "This is a NEW example — it does not repeat the flipped video.",
    ],
    quickCheck: [
      "On whiteboards, 60 seconds: for f(x) = 3x − 1 and g(x) = x², find (f ∘ g)(x) and (g ∘ f)(x).",
      "Expected: 3x² − 1 and (3x − 1)² = 9x² − 6x + 1.",
      "80% correct → release guided practice. Below 80% → one further modelled example, substituting one step at a time.",
    ],
    guided: [
      "Two “Give it a go” problems, identical for every student, worked together with the teacher:",
      "(1) f(x) = x + 6 and g(x) = 2x − 1 — find (f + g)(x), (fg)(x) and (f ∘ g)(x).  (2) f(x) = √x and g(x) = x − 9 — find (f ∘ g)(x) and state its domain.",
      "Answers: 3x + 5 ; 2x² + 11x − 6 ; 2x + 5 — and √(x − 9) with domain x ≥ 9.",
      "Feedback: worked live on the board step by step; students self-mark and circle their OWN first error.",
    ],
    independent: [
      "Delivered through the “Choose Your Route” sheet with live feedback in Pear Deck. Routes are named for the task, not for the student.",
      "PRACTICE — Secure the method. Four operations on four pairs, excluded values, three numerical compositions, two straightforward compositions. Done when: you can substitute a whole function into another without losing the bracket.",
      "APPLY — Use it in context. Both compositions of a radical pair with domains, decomposition of a given function, and a Saudi discount-and-VAT model in both orders. Done when: your domains are in interval form and your context answer carries SAR.",
      "INVESTIGATE — Find out why. When f ∘ g equals g ∘ f, why the domain of a composite can shrink, and associativity with a counterexample for commutativity. Done when: you have an argument, not just an answer.",
      "Every student sits the same Mastery Gate. The gate is not differentiated, because it is the evidence.",
    ],
    production: [
      "Non-routine transfer task — this context has not appeared in practice.",
      "A store in Jeddah runs a 20% sale and VAT is 15%: D(p) = 0.80p and V(p) = 1.15p, with p the marked price in SAR. A customer insists the discount must be applied first.",
      "(a) Write (V ∘ D)(p) and (D ∘ V)(p). (b) Price a 480 SAR jacket under each order. (c) Explain why the customer is wrong, using the structure of the expressions rather than the numbers. (d) Add a fixed 25 SAR delivery charge after VAT — write the new composite and explain why the order now DOES matter.",
      "Answers: (a) both equal 0.92p. (b) 441.60 SAR either way. (c) both are a product of the same two constants and multiplication is commutative. (d) 1.15(0.80p) + 25 is not 1.15(0.80p + 25); adding is not a scaling, so it does not commute with the multipliers.",
      "Students then hand their reasoning to the AI critic and ask it to challenge any step they have not justified.",
    ],
    criteria: [
      "Minimum acceptable standard: both composites written correctly, the substitution step visible, and the explanation given in terms of the functions rather than one example.",
      AI_CRITIC,
      "Completed independently by the student: the written justification for parts (a)–(d). AI may challenge it; it may not write it.",
    ],
    evidence: [
      "“Time to Check” — one individual task. No notes, no partner, no AI.",
      "For f(x) = x² + 1 and g(x) = 3x − 2: 1. find (f + g)(x) and (fg)(x). 2. find (f ∘ g)(x) and (g ∘ f)(x), showing the substitution step. 3. in ONE sentence explain why the two answers to question 2 are different.",
      "Answers: x² + 3x − 1 ; 3x³ − 2x² + 3x − 2 ; 9x² − 12x + 5 ; 3x² + 1 ; they differ because the inside function acts first, and squaring then scaling is not the same as scaling then squaring.",
      "Done when: every answer is fully expanded, the substitution step is visible, and question 3 gives a reason rather than a restatement.",
      "Scored live in Pear Deck as submissions arrive; result logged in the Impact Dashboard Mastery Rate.",
    ],
    refinement: [
      "Students revise their pricing reasoning using the AI critique and the teacher's micro-conference note.",
      "Final product, three equally acceptable formats: a Canva one-pager, a photographed hand-written solution, or a 45-second voice note.",
      "Required content: both composites side by side with the substitution step visible; ONE worked non-example with the order reversed or the bracket dropped, and a sentence on how a reader would catch it; and a caption on why a billing system must fix the order of its operations.",
      "Graded on originality and clarity of reasoning, not correctness alone.",
    ],
    publication: [
      "Published to the class LMS portfolio; the strongest go on the Mathematics Department wall as the Topic 5 anchor set.",
      "Reflection question: “Which is still harder for you — keeping the bracket, or keeping the order?”",
    ],
    differentiation: [
      "PRACTICE — Secure the method. Four operations on four pairs, excluded values, and simple compositions; the operation table stays on the board and a partner is allowed. Done when: a whole function can be substituted without losing the bracket.",
      "APPLY — Use it in context. Radical compositions with domains, decomposition, and the discount-and-VAT model in both orders. Done when: domains are in interval form and the context answer carries SAR.",
      "INVESTIGATE — Find out why. Commuting pairs, shrinking domains, and associativity with counterexamples. Done when: there is an argument, not just an answer.",
      "No student is labelled. The routes describe tasks; every student sits the same Mastery Gate.",
    ],
    adaptive: PILLAR_ADAPTIVE,
    saudi: [
      "Production context: a Jeddah store's 20% sale combined with the Kingdom's 15% VAT, modelled as two functions composed in both orders and priced in SAR.",
      "In-class project: a rooftop solar array — energy generated as a function of time, and the bill credit as a function of energy, composed into one function of time.",
      "Discussion prompt: why a retailer's billing system must define the order of discount, VAT and delivery once and for all.",
    ],
    exams: [
      "SAT — Advanced Math: building and interpreting composite and equivalent function forms, roughly 35% of the Mathematics section. Practice tip: if given f(g(x)) and asked for g, substitute a simple number and work backwards.",
      "SAAT (Tahsili) — function operations and composition sit in the Grade 11 band, 30% of the mathematics items. Practice tip: check the order before computing; the wrong-order answer is always one of the four options.",
      "GAT (Qudurat) — two-step percentage and rate chains, which are compositions in disguise, about 75 seconds per question. Practice tip: chain the multipliers — 0.80 then 1.15 is a single multiplication by 0.92.",
    ],
  },

  plan2026: {
    day: "Sunday, Week 3", section: "Grade 11 — 11B",
    tools: "Quizizz (diagnostic) · Pear Deck (live practice feedback) · GeoGebra Graphing Calculator · Canva (final product) · Whiteboards",
    resources: "Lesson presentation (18 slides) · “Choose Your Route” differentiation sheet · “Give It a Go” classwork · “Sale Price, Fair Price” project task · squared paper",
    competencies: ["Substituting a whole function, not just a variable.", "Judging whether an order of operations changes a result, and saying why."],
    technology: ["Quizizz live diagnostic with instant gap analysis.", "GeoGebra: define f and g, then plot f(g(x)) and g(f(x)) together and find where they meet."],
    reallife: ["A 20% sale combined with 15% VAT in a Jeddah store.", "A rooftop solar array: energy from time, then bill credit from energy."],
    values: ["Fairness and transparency in pricing.", "Precision — the order of operations is not a matter of opinion."],
    soft: ["Collaboration in assigned group roles.", "Defending a claim about order with a general argument, not one example."],
    hard: ["Adding, subtracting, multiplying and dividing functions, with domains.", "Forming and interpreting composite functions."],
    phases: [
      "FIKR Phase 1 — Diagnose. 5-question Quizizz on combining functions and reading composition notation. Results read as a gap map; students routed to the re-teach table, straight to modelling, or the Investigate prompt.",
      "FIKR Phase 2 — Targeted Instruction. Focused re-teach on order for flagged students. Whole class: the four operations table with domain rules; the composition machine; modelled example with both compositions and their graphs. Quick check on whiteboards.",
      "FIKR Phase 3 — Practice. Two identical “Give it a go” problems worked together. Students then choose a route on the “Choose Your Route” sheet and may switch at any time. Live feedback via Pear Deck; 2-minute micro-conferences.",
      "FIKR Phase 4 — Production. Discount and VAT composed in both orders, then a delivery charge that breaks the symmetry. AI used as critic only.",
      "FIKR Phase 5 — Proof of Learning. “Time to Check” — both operations and both compositions for an unseen pair. No notes, no partner, no AI.",
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
    closure: "Two minutes of peer show-and-tell on the final products, then the reflection question: “Which is still harder for you — keeping the bracket, or keeping the order?”",
    homework: "Finish the final product and upload to the LMS portfolio (any of the three formats). Practice set on Pear Deck — 12 questions, choose your route. Watch the flipped video for Lesson 5-6: Inverse Relations and Functions. Clinic group: bring your Time to Check paper.",
  },

  classwork: {
    subtitle: "Show all your working. Keep the bracket until the expansion is finished — that is where the marks are.",
    sections: [
      { h: "SECTION A — The four operations", note: "Objective 1", lines: 4,
        q: [
          { n: "Q1", eq: "o_ws1", t: "Find (f + g)(x), (f − g)(x), (fg)(x) and (f/g)(x). State the excluded value." },
          { n: "Q2", eq: "o_ws2", t: "Find (f/g)(x) and simplify it. State the excluded value, and explain why it survives the simplification." },
          { n: "Q3", eq: "o_ws3", t: "Find (f + g)(x) and state the domain in interval form." },
          { n: "Q4", eq: "o_qc", t: "Find (fg)(x), fully expanded." },
        ] },
      { h: "SECTION B — Composition", note: "Objective 2", lines: 4,
        intro: "Read the machine diagram from the lesson if you need to: the inside function runs first.",
        graph: "d_comp_machine", graphW: 560,
        q: [
          { n: "Q5", eq: "o_ws4", t: "Find (f ∘ g)(x) and (g ∘ f)(x). State the domain of each." },
          { n: "Q6", eq: "o_g1", t: "Find (f ∘ g)(x) and (g ∘ f)(x). Are they equal? Show the substitution step." },
        ] },
      { h: "SECTION C — Reading a composite backwards", note: "Objective 2 · MP.7", lines: 5,
        text: [
          "Q7.  h(x) = (2x + 5)³. Find functions f and g so that h(x) = f(g(x)). Say which one is the inside function.",
          "Q8.  h(x) = √(x² + 1). Find f and g so that h(x) = f(g(x)).",
          "Q9.  A student says (f ∘ g)(x) means “multiply f by g”. Write one sentence correcting them, and one example that proves the point.",
        ] },
      { h: "SECTION D — A two-step charge", note: "Objective 1 · MP.4", lines: 5,
        intro: "A Jeddah store's 20% sale is D(p) = 0.80p and VAT is V(p) = 1.15p, with p in SAR.",
        text: [
          "Q10.  Find (V ∘ D)(p) and (D ∘ V)(p). Price a 480 SAR jacket under each order.",
          "Q11.  Explain, using the expressions and not the numbers, why the order makes no difference here.",
          "Q12.  The store now adds a fixed 25 SAR delivery charge after VAT. Write the new composite and explain why the order now matters.",
        ] },
    ],
  },

  diffSheet: {
    routes: [
      { note: "Combine and substitute", done: "you can substitute a whole function into another without losing the bracket.",
        intro: "For each pair, find the sum, the product and (f ∘ g)(x).",
        grid: [["1.", "o_ws1"], ["2.", "o_qc"], ["3.", "o_g1"], ["4.", "o_ws2"], ["5.", "o_gate"], ["6.", "o_ws3"]],
        tasks: ["7.  For any two of the pairs above, state the excluded value of (f/g)(x), or write “none” and say why."],
        lines: 2 },
      { note: "Domains, decomposition and one Saudi context", done: "your domains are stated in interval form, and your context answer carries SAR.",
        intro: "Work carefully — the domain of a composite is not always the domain of the inside function.",
        graph: "d_order_matters", graphW: 400,
        tasks: [
          "1.  For f(x) = √(x + 4) and g(x) = x², find (f ∘ g)(x) and (g ∘ f)(x), and state the domain of each in interval form.",
          "2.  Decompose h(x) = (2x + 5)³ and h(x) = √(x² + 1) into an inside and an outside function.",
          "3.  A store's sale is D(p) = 0.80p and VAT is V(p) = 1.15p. Find both composites, price a 480 SAR jacket under each, and say which order the shop should publish.",
          "4.  A rooftop array generates E(t) = 4.5At kWh in t hours from A square metres, and the bill credit is R(E) = 0.18E SAR. Write the credit as a function of time and interpret the number in front of t.",
        ], lines: 4 },
      { note: "Arguments, not answers", done: "you have an argument, not just an answer.",
        tasks: [
          ["1.  Find every pair of linear functions for which   ", { eq: "o_noncomm", k: 1.1 }, "   fails — that is, for which the two composites ARE equal. Describe what those pairs have in common."],
          "2.  Prove that the domain of f ∘ g can be strictly smaller than the domain of g, using a radical example, and explain the mechanism in one sentence.",
          "3.  Show that composition is associative — f ∘ (g ∘ h) = (f ∘ g) ∘ h — and give a counterexample proving it is not commutative.",
        ], lines: 5 },
    ],
  },

  pbl: {
    title: "Sale Price, Fair Price", minutes: 20,
    subtitle: "A 20-minute group project. Work in fours. Every member signs the sheet.",
    driving: "A shop must decide, once and for all, in what order to apply its discount, its VAT and its delivery charge. Which orders change the price, and which do not?",
    situation: [
      "A store in Jeddah is running a 20% sale. VAT in the Kingdom is 15%. The two steps are modelled by D(p) = 0.80p and V(p) = 1.15p, where p is the marked price in SAR.",
      "A customer complains that the shop applies VAT first and says this costs them more. The manager is not sure and asks your group to settle it in writing.",
      "The store is also about to add a fixed 25 SAR delivery charge, and needs to know where in the chain it belongs.",
    ],
    eq: "ctx_disc",
    steps: [
      ["1", "WRITE BOTH ORDERS  (4 min)", "Write (V ∘ D)(p) and (D ∘ V)(p) as single simplified expressions."],
      ["2", "PRICE ONE ITEM  (4 min)", "A jacket is marked 480 SAR. Find the final price under each order. Give both in SAR."],
      ["3", "SETTLE THE COMPLAINT  (4 min)", "Say whether the customer is right, and justify it from the EXPRESSIONS, not from the one number you tested."],
      ["4", "BREAK IT  (5 min)", "Add the fixed 25 SAR delivery charge after VAT. Write the new composite, then write the version where delivery comes before VAT. Explain why these two are different when the first two were not."],
      ["5", "PRESENT  (3 min)", "Prepare one sentence your presenter will say: which operations can safely swap places, and which cannot."],
    ],
    working: [["Step 1 — both composites:", 2], ["Step 2 — the jacket, both orders:", 2],
              ["Step 3 — is the customer right, and why:", 4], ["Step 4 — with delivery added:", 4],
              ["Step 5 — our sentence:", 2]],
    roles: ["Reader — states the two functions", "Algebraist — writes the composites", "Checker — tests every claim", "Presenter — says the sentence"],
    doneWhen: ["Both composites are simplified to a single expression.", "Both jacket prices are exact and in SAR.", "Step 3 argues from the expressions, not from one number.", "Step 4 explains WHY adding behaves differently from multiplying.", "Your sentence makes sense to someone who does not study maths."],
    materials: ["This sheet", "A calculator", "A pencil", "The four-operation table from the board"],
  },
};

(async () => {
  for (const cfg of [GR10_L3, GR11_L5]) await buildAll(cfg);
})();
