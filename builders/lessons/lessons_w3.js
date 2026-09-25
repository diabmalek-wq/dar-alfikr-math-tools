// Week 3 — one lesson per grade, per the Curriculum Distribution.
//   Gr10  Lesson 1-3  Piecewise-Defined Functions
//   Gr11  Lesson 5-5  Operations on Functions
//
// Objectives, essential questions, vocabulary, standards, MPs and assessment
// names are quoted VERBATIM from "Curriculum map A2 OBLAS.docx".
const { build } = require("./lesson_engine");

const MATH = "math_w3/_index.json";
const GRAPH = "graphs_w3/_index.json";
const ASSESS = ["“Give it a go” questions", "“Time to Check”"];

// =====================================================================
// GRADE 10 · TOPIC 1 · LESSON 3 — Piecewise-Defined Functions
// =====================================================================
const GR10_L3 = {
  out: "Gr10_T1_L3_Piecewise_Defined_Functions.pptx",
  deckTitle: "Piecewise-Defined Functions — Grade 10 Algebra II",
  mathIndex: MATH, graphIndex: GRAPH,
  topicLine: "TOPIC 1 · LINEAR FUNCTIONS · LESSON 3",
  lessonTitle: "Piecewise-Defined Functions",
  titleSize: 40,
  subtitle: "One function, more than one rule — because the real world changes its mind",
  titleEq: "p_general_w", titleEqK: 1.5,
  titleEqAlt: "f of x defined by rule one for x less than a, and rule two for x greater than or equal to a",
  grade: "Grade 10", week: "Week 3 · Semester 1, 2026–27",
  footerLeft: "Grade 10 · Algebra II · Topic 1 · Lesson 3",
  lessonRef: "Lesson 1-3 — Piecewise-Defined Functions",
  nextLesson: "Arithmetic Sequences and Series",

  codes: ["HSF.IF.B.5", "HSF.IF.C.7.B", "HSF.LE.A.2", "HSS.ID.B.6.A"],
  mps: ["MP.4", "MP.5"],
  assessments: ASSESS,

  objectives: [
    "Create and graph piecewise-defined functions, including absolute value and step functions.",
    "Write piecewise-defined functions based on given graphs.",
    "Create and use piecewise-defined functions to model and analyze real-world data.",
  ],
  essentialQuestion: "How can piecewise-defined functions be used to model real-world situations?",

  vocabulary: [
    { term: "Piecewise-defined function", def: "A function built from two or more rules, each one used on its own part of the domain." },
    { term: "Subintervals", def: "The separate pieces of the domain. Each subinterval carries exactly one rule." },
    { term: "Disjoint", def: "Sharing no point. The subintervals must be disjoint, or an input would have two outputs." },
    { term: "Absolute value function", def: "f(x) = |x|. A piecewise function in disguise: x when x ≥ 0, and −x when x < 0." },
    { term: "Step function", def: "A function whose graph is a series of horizontal segments — it jumps rather than slopes." },
    { term: "Floor function", def: "⌊x⌋ rounds DOWN to the nearest integer. ⌊3.7⌋ = 3 and ⌊−1.2⌋ = −2." },
    { term: "Ceiling function", def: "⌈x⌉ rounds UP to the nearest integer. ⌈3.2⌉ = 4 and ⌈−1.8⌉ = −1." },
  ],
  vocabSub: "The seven terms the curriculum map lists for this lesson",

  prior: [
    { h: "Evaluating a function", eq: "p_ex_a", d: "Substitute — but first decide WHICH rule applies." },
    { h: "Inequalities on a line", eq: "p_sub", d: "Every input belongs to exactly one subinterval." },
    { h: "Domain in interval form", eq: "p_dom", d: "The pieces together still cover the whole domain." },
  ],
  priorSub: "Three things from Lessons 1 and 2 — today one function carries several rules",
  carryOver: "A piecewise-defined function is still a function. Every input has exactly one output, because the subintervals are disjoint — no x can obey two rules at once. That is the whole idea, and everything else in the lesson follows from it.",
  carryOverEq: "p_general",

  diagnose: {
    title: "Warm-Up: Which Rule Applies?",
    sub: "Answer on Quizizz — 5 questions, 4 minutes. This builds a gap map, not a grade.",
    questions: [
      { eq: "p_d1", t: "Find f(−2). Say which rule you used and why." },
      { eq: "p_d2", t: "Evaluate." },
      { eq: "p_d3", t: "Evaluate the floor." },
      { eq: "p_d4", t: "Evaluate the ceiling." },
      { eq: "p_d5", t: "Is x = −3 inside this subinterval? Open or closed circle?" },
    ],
    routing: "0–2 correct → re-teach table with me.      3–4 correct → straight to modelling.      5 correct → start the Investigate prompt now.",
  },

  instruction: [
    {
      title: "Three Functions You Already Half Know",
      sub: "Objective 1 — absolute value, two-piece linear and step functions are all piecewise",
      graph: "g_pw_panel", graphW: 12.43, graphY: 2.5,
      graphAlt: "Three panels: the absolute value function forming a V, a two-piece linear function with an open circle and a closed circle at x equals 1, and the floor step function",
      bar: ["THE PATTERN", "Every one of these is a single function. The graph changes rule at a boundary, and at every boundary exactly one circle is filled — that is what keeps it a function."],
      barY: 6.32,
      notes: "Work left to right. Ask what the three graphs have in common before naming anything. Misconception to name aloud: students read the two-piece graph as 'two functions' — it is one function with two rules.",
    },
    {
      title: "Why the Subintervals Must Be Disjoint",
      sub: "Objective 1 — open circle, closed circle, and the reason it matters",
      graph: "d_disjoint", graphW: 7.6, graphY: 2.42,
      graphAlt: "A number line showing x less than 1 shaded with an open circle at 1, and x greater than or equal to 1 shaded with a closed circle at 1, described as disjoint subintervals",
      panel: {
        h: "READ IT THIS WAY",
        items: [
          "Pick an input. Ask which subinterval it lives in.",
          "That subinterval names the one rule you use.",
          "The boundary belongs to whichever piece has ≤ or ≥.",
          "Open circle = not included. Closed circle = included.",
          "If both pieces claimed the boundary, one input would have two outputs — and it would not be a function.",
        ],
      },
      panelX: 8.4, panelW: 4.5, panelH: 4.1,
      notes: "Do not let students memorise 'open means less than'. Make them say the reason: the boundary can only be owned once. Ask what would go wrong if both pieces used ≤.",
    },
    {
      title: "Modelled Example — I Think Aloud",
      sub: "Objectives 1 and 2 — graph it, then read values off it",
      graph: "g_pw_worked", graphW: 5.6, graphY: 2.42,
      graphAlt: "The graph of f of x equals 2x plus 1 for x less than 1 and 5 minus x for x greater than or equal to 1, with an open circle at 1 comma 3 and a closed circle at 1 comma 4",
      panel: {
        h: "WATCH MY THINKING",
        items: [
          "Rule one: 2x + 1, but only to the LEFT of x = 1.",
          "I graph the whole line lightly, then rub out what I do not own.",
          "At x = 1 the first rule gives 3 — open circle, it is not included.",
          "Rule two: 5 − x, from x = 1 to the right.",
          "At x = 1 the second rule gives 4 — closed circle, so f(1) = 4.",
          "The jump at x = 1 is real. Piecewise graphs are allowed to break.",
        ],
      },
      panelX: 6.35, panelW: 6.53, panelH: 4.1,
      notes: "Narrate the rubbing-out step — that is the part students skip, and it is why they draw full lines across the whole plane. Answers: f(−2) = −3, f(1) = 4, f(4) = 1.",
    },
  ],

  quickCheck: {
    lead: "Find f(−1) and f(0) for", leadW: 4.6,
    eq: "p_qc", k: 1.6,
    think: "Two inputs, two different rules. For each one, say which subinterval it belongs to BEFORE you substitute.",
    rule: "80% correct → straight to guided practice.   Below 80% → one more modelled example, this time reading values from the graph.",
  },

  guided: {
    mins: 4,
    items: [
      { eq: "p_g1", t: "Graph this function and state f(0), f(2) and f(5).", hint: "The boundary at x = 2 uses ≥, so the closed circle belongs to the second rule." },
      { eq: "p_g2", t: "Graph this function. Where is the vertex, and what is the domain?", hint: "An absolute value graph is a V. This one has been moved." },
    ],
  },

  routes: {
    mins: 8,
    tiers: [
      { items: ["Evaluate four piecewise functions at given inputs.", "Graph two two-piece linear functions with correct open and closed circles.", "Evaluate four floor and ceiling expressions.", "Sketch the absolute value function and one translation of it."],
        help: "You may use: the boundary rule on the board, and a partner.",
        done: "you choose the correct rule every time, and your circles are right.", eq: "p_ws1" },
      { items: ["Write the piecewise function for a graph you are shown.", "Model a Saudi electricity bill as a two-rule function and use it.", "Graph a three-piece function including a curved piece.", "Explain what a step function means for a parking charge."],
        help: "You may use: the worked example, and the sentence frames.",
        done: "your function matches the graph exactly, and your context answer carries units in SAR.", eq: "p_ws7" },
      { items: ["Explain why the absolute value function is a piecewise function, using the definition.", "Show that a floor function and a ceiling function are never equal for a non-integer input.", "Design a piecewise function that is continuous at its boundary, and prove it."],
        help: "You may use: nothing but your reasoning.",
        done: "you have an argument, not just an answer.", eq: "p_abs_pw" },
    ],
  },

  production: {
    title: "The Saudi Electricity Tariff",
    sub: "A context you have not seen before — this tests transfer",
    situation: "Residential electricity in the Kingdom is billed at two rates: 18 halalas per kWh for the first 6000 kWh in a month, and 30 halalas per kWh for everything above that. A family in Jeddah is deciding whether to install a split-unit timer.",
    eq: "ctx_tariff_w", eqK: 1.25,
    tasks: [
      "(a)  Explain in one sentence why the cost cannot be written as a single linear rule.",
      "(b)  Find the bill for a month of 5200 kWh, and for a month of 8400 kWh. Give both in SAR.",
      "(c)  The family cuts usage from 8400 to 6900 kWh. How much do they save, and why is the saving bigger than 18 halalas per unit?",
      "(d)  Sketch the graph and mark the point where the rule changes.",
    ],
    note: "Exact values in SAR, and the boundary named.",
    aiPrompt: "“Check whether I have used the correct rule for each consumption level, and challenge any step I cannot justify.”",
  },

  geogebra: {
    sub: "Type a piecewise function and watch the circles appear",
    explore: "enter If(x < 1, 2x + 1, 5 - x) and zoom in on x = 1. Then change the < to ≤ and see what GeoGebra refuses to do. Say aloud why.",
  },

  gate: {
    graph: "g_pw_gate",
    graphAlt: "A graph made of a horizontal segment at y equals 3 for x less than 2 with an open circle at 2 comma 3, and a line rising from a closed circle at 2 comma 1",
    items: [
      { t: "Write the piecewise-defined function for the graph shown.", eq: null },
      { t: "State f(2), and say how the graph told you which rule to use.", eq: null },
      { t: "In ONE sentence, explain why one of the circles at x = 2 must be open.", eq: null },
    ],
    footer: "Exact answers only. Both rules, both subintervals, and the correct inequality signs.",
    routing: "PASS → Enrichment & Challenge (a three-piece model of a taxi fare).      NOT YET → Targeted Learning Clinic on boundaries and circles, start of next lesson.",
  },

  smart: {
    steps: [
      { h: "Show the model", d: "Present your tariff function and its graph, with the boundary at 6000 kWh clearly marked and labelled in SAR." },
      { h: "Expose the trap", d: "Add one worked NON-example: a bill calculated with the wrong rule, and a sentence saying how a reader would spot the error." },
      { h: "Say why it matters", d: "One caption — “why a utility company charges in bands rather than one flat rate” — for a non-maths reader." },
    ],
    published: "the class LMS portfolio; the strongest go on the Department wall as our Topic 1 modelling set.",
    reflection: "which is still harder for you — choosing the rule, or drawing the circles?",
  },

  exams: [
    { code: "GAT", full: "Qudurat — General Aptitude", skill: "Reading a two-rate charge from a table or graph and applying the correct band — an arithmetic and data item, the largest quantitative strand.", fmt: "Multiple choice, about 75 seconds per item.", tip: "Find the boundary value first. Most wrong options come from using one rate for the whole amount." },
    { code: "SAAT", full: "Tahsili — Achievement Test", skill: "Evaluating a piecewise function and reading a step graph, in the Grade 10 and 11 function bands.", fmt: "Four-option multiple choice, mixed with the other subjects.", tip: "Underline the inequality signs before you substitute. Which side owns the boundary decides the answer." },
    { code: "SAT", full: "College Board", skill: "Advanced Math and Problem-Solving & Data Analysis — piecewise and absolute value models, and rate-of-change reading.", fmt: "Roughly 35% Advanced Math and 15% Problem-Solving & Data Analysis; some items are typed responses.", tip: "Desmos accepts piecewise notation with braces — graph it and read the value rather than guessing." },
  ],
  examBar: ["THE SINGLE MOST EXAMINED IDEA HERE:", "decide which subinterval the input belongs to BEFORE you substitute — the boundary is where the marks are won or lost."],

  summary: [
    "Choose the correct rule for any input, and say why.",
    "Graph a piecewise function with the circles the right way round.",
    "Write a piecewise function from a graph you are given.",
    "Recognise absolute value and step functions as piecewise functions.",
    "Model a two-rate real-world charge and use it to answer a question in SAR.",
  ],
  homework: [
    "Finish your product and upload it to the LMS portfolio — any of the three formats.",
    "Practice set on Pear Deck: 12 questions, choose your route.",
    "Watch the flipped video for Lesson 1-4: Arithmetic Sequences and Series (4 min, 2 embedded questions).",
    "Clinic group: bring your Time to Check paper — we start with 10 minutes on boundaries and circles.",
  ],

  notes: {
    cover: "Week 3 lesson for 10A and 10C, following Transformations of Functions.",
    objectives: "All three objectives are verbatim from the curriculum map. The map lists HSF.IF.B.5, HSF.IF.C.7.B, HSF.LE.A.2 and HSS.ID.B.6.A for this lesson, and only MP.4 and MP.5 — do not add others.",
    vocabulary: "All seven terms are the map's list. 'Disjoint' is the one students skip; it is the reason the definition works, so spend a minute on it.",
    prior: "If a student cannot decide which subinterval an input belongs to, nothing else in this lesson will land. Watch for it in the diagnostic.",
    diagnose: "Answers: f(−2) = 2 using the first rule; |3−5| = 2; ⌊7.9⌋ = 7; ⌈2.1⌉ = 3; yes, x = −3 is included, closed circle. Expected gap: Q3 and Q4 — students round to nearest rather than down or up.",
    quickCheck: "Answers: f(−1) = 2 from the first rule since −1 ≤ −1; f(0) = 0 from the second rule. Watch for students who use x² at x = −1.",
    guided: "Answers — 1: f(0) = −2, f(2) = 4, f(5) = 4. 2: vertex (−3, −2), domain all real numbers. Do not release independent work until roughly 80% have both.",
    routes: "Students choose their own route and may switch mid-task. Pear Deck flags error patterns live; use it to decide who gets a two-minute conference.",
    production: "Answers — (a) the rate changes at 6000 kWh, so no single slope fits. (b) 5200 kWh → 936 SAR; 8400 kWh → 1080 + 0.30(2400) = 1800 SAR. (c) 6900 kWh → 1080 + 0.30(900) = 1350 SAR, a saving of 450 SAR; the saving is larger because every unit removed came out of the 30-halala band. (d) two segments meeting at (6000, 1080).",
    geogebra: "GeoGebra will graph If(x ≤ 1, 2x+1, 5−x) happily — the point is that the boundary can only be owned once, and the student must say which piece owns it.",
    gate: "Answer: f(x) = 3 for x < 2, and f(x) = x − 1 for x ≥ 2; f(2) = 1 because the closed circle sits on the second rule; one circle must be open or x = 2 would have two outputs. Score live and route privately.",
    smart: "The non-example in step 2 is the highest-value part — a bill computed entirely at 30 halalas is the error a real customer would make.",
    exams: "Show this before homework so the practice set has an obvious purpose.",
    summary: "Route the clinic group privately through the LMS — never announce the list to the class.",
  },
};

// =====================================================================
// GRADE 11 · TOPIC 5 · LESSON 5 — Operations on Functions
// =====================================================================
const GR11_L5 = {
  out: "Gr11_T5_L5_Operations_on_Functions.pptx",
  deckTitle: "Operations on Functions — Grade 11 Algebra II",
  mathIndex: MATH, graphIndex: GRAPH,
  topicLine: "TOPIC 5 · RATIONAL EXPONENTS AND RADICAL FUNCTIONS · LESSON 5",
  lessonTitle: "Operations on Functions",
  titleSize: 42,
  subtitle: "Add them, multiply them — or feed one straight into the other",
  titleEq: "o_comp_w", titleEqK: 2.0,
  titleEqAlt: "f composed with g of x equals f of g of x",
  grade: "Grade 11", week: "Week 3 · Semester 1, 2026–27",
  footerLeft: "Grade 11 · Algebra II · Topic 5 · Lesson 5-5",
  lessonRef: "Lesson 5-5 — Operations on Functions",
  nextLesson: "Inverse Relations and Functions",

  codes: ["HSF.BF.A.1.B", "(+)HSF.BF.A.1"],
  mps: ["MP.4", "MP.7"],
  assessments: ASSESS,

  objectives: [
    "Combine functions using arithmetic operations.",
    "Combine functions using function composition.",
  ],
  essentialQuestion: "In what ways can we combine functions to create new functions?",

  vocabulary: [
    { term: "Composite function", def: "The function you get when the output of one function becomes the input of another, written (f ∘ g)(x)." },
    { term: "Composition", def: "The operation itself — feeding one function into another, rather than adding or multiplying them." },
  ],
  vocabSub: "The two terms the curriculum map lists for this lesson",

  prior: [
    { h: "Evaluating a function", eq: "o_pk1", d: "Work from the inside out. This is composition already." },
    { h: "Expanding a bracket", eq: "o_pk2", d: "Composition almost always ends in an expansion." },
    { h: "Undefined values", eq: "o_pk3", d: "A denominator of zero rules a value out of the domain." },
  ],
  priorSub: "Three things you can already do — today we give them names",
  carryOver: "You have been composing functions since Lesson 5-2 without calling it that. Every time you worked out f(g(2)) from the inside out, you evaluated a composite function. Today we do it with x instead of a number, and the order becomes the whole story.",
  carryOverEq: "o_comp",

  diagnose: {
    title: "Warm-Up: Combine Them",
    sub: "Answer on Quizizz — 5 questions, 4 minutes. This builds a gap map, not a grade.",
    questions: [
      { eq: "o_d1", t: "Write the sum as a single expression." },
      { eq: "o_d2", t: "Find the value of the product at x = 2." },
      { eq: "o_d3", t: "Evaluate. Work from the inside out." },
      { eq: "o_d4", t: "Complete the sentence." },
      { eq: "o_d5", t: "Complete the sentence in words." },
    ],
    routing: "0–2 correct → re-teach table with me.      3–4 correct → straight to modelling.      5 correct → start the Investigate prompt now.",
  },

  instruction: [
    {
      title: "Four Arithmetic Operations on Functions",
      sub: "Objective 1 — you already do this with numbers; the notation is the only new part",
      rows: [
        [{ eq: "o_sum" }, "Add the outputs. The domain is where BOTH functions are defined."],
        [{ eq: "o_diff" }, "Subtract the outputs, in the order written. f − g is not g − f."],
        [{ eq: "o_prod" }, "Multiply the outputs. Expect to expand a bracket."],
        [{ eq: "o_quot" }, "Divide the outputs — and exclude every x that makes the bottom zero."],
        [{ eq: "o_dom" }, "The domain rule for the first three: the overlap of the two domains."],
      ],
      rowsHead: ["The operation", "What you actually do"],
      rowsCw: [5.2, 7.23], rowH: 0.7, rowsTop: 2.4,
      notes: "Read each row aloud with a different student. Misconception to name: students think (f/g)(x) has the same domain as f. It does not — every zero of g is excluded, even if f is fine there.",
    },
    {
      title: "Composition — Feeding One Function Into Another",
      sub: "Objective 2 — the inside function runs first",
      graph: "d_comp_machine", graphW: 12.0, graphY: 2.7,
      graphAlt: "A machine diagram: x enters function g, producing g of x, which enters function f, producing f of g of x, labelled inside first and outside second",
      bar: ["THE PATTERN", "Read (f ∘ g)(x) from the INSIDE out: g acts on x first, and f acts on whatever g produced. The symbol order and the working order are opposites."],
      barY: 6.32,
      notes: "Say 'inside first' three times. Then ask: which function does x meet first in (f ∘ g)(x)? If more than a few say f, stop and redraw the machine.",
    },
    {
      title: "Modelled Example — I Think Aloud",
      sub: "Objectives 1 and 2 — one pair of functions, both compositions",
      graph: "g_ops_order", graphW: 6.0, graphY: 2.42,
      graphAlt: "Two parabolas: f composed with g equals x squared plus 6x plus 5 with vertex minus 3 comma minus 4, and g composed with f equals x squared minus 1 with vertex 0 comma minus 1",
      panel: {
        h: "WATCH MY THINKING",
        items: [
          "f(x) = x² − 4 and g(x) = x + 3.",
          "(f ∘ g)(x): g acts first, so I replace every x in f with (x + 3).",
          "(x + 3)² − 4 expands to x² + 6x + 5.",
          "(g ∘ f)(x): f acts first, so I add 3 to x² − 4.",
          "That gives x² − 1. A different function entirely.",
          "The graphs prove it — different vertices, different curves.",
        ],
      },
      panelX: 6.75, panelW: 6.13, panelH: 4.1,
      notes: "Do the substitution slowly and out loud: 'every x in f becomes the whole of g'. The bracket is the step students drop. Answers: x² + 6x + 5 and x² − 1.",
    },
  ],

  quickCheck: {
    lead: "Find (f ∘ g)(x) and (g ∘ f)(x) for", leadW: 5.6,
    eq: "o_qc", k: 1.9,
    think: "Substitute the whole function, not just its variable. Keep the bracket until you have finished expanding.",
    rule: "80% correct → straight to guided practice.   Below 80% → one more modelled example, this time substituting one step at a time.",
  },

  guided: {
    mins: 4,
    items: [
      { eq: "o_g1", t: "Find (f + g)(x), (fg)(x) and (f ∘ g)(x).", hint: "For the composition, replace the x in f with all of 2x − 1." },
      { eq: "o_g2", t: "Find (f ∘ g)(x) and state its domain.", hint: "The inside must be non-negative before the root can act on it." },
    ],
  },

  routes: {
    mins: 8,
    tiers: [
      { items: ["Find the sum, difference, product and quotient for four pairs of functions.", "State the excluded value for each quotient.", "Evaluate three compositions at given numbers.", "Find (f ∘ g)(x) for two straightforward pairs."],
        help: "You may use: the four-operation table on the board, and a partner.",
        done: "you can substitute a whole function into another without losing the bracket.", eq: "o_ws1" },
      { items: ["Find both compositions for a radical pair and state each domain.", "Decompose a given function into an inside and an outside function.", "Model a Saudi retail price with a discount function and a VAT function, composed in both orders.", "Explain what the composite means in context, with units in SAR."],
        help: "You may use: the worked example, and the sentence frames.",
        done: "your domains are stated in interval form, and your context answer carries SAR.", eq: "o_ws4" },
      { items: ["Find every function pair for which f ∘ g = g ∘ f, and describe what they have in common.", "Prove that the domain of f ∘ g can be smaller than the domain of g.", "Show that composition is associative but not commutative, with a counterexample for each claim."],
        help: "You may use: nothing but your reasoning.",
        done: "you have an argument, not just an answer.", eq: "o_ws8" },
    ],
  },

  production: {
    title: "Discount Then VAT, or VAT Then Discount?",
    sub: "A context you have not seen before — this tests transfer",
    situation: "A store in Jeddah runs a 20% sale. VAT in the Kingdom is 15%. A customer argues that the shop should apply the discount first, because “taking VAT off a smaller number is cheaper”. Two functions model the two steps, where p is the marked price in SAR.",
    eq: "ctx_disc_w", eqK: 1.5,
    tasks: [
      "(a)  Write (V ∘ D)(p) and (D ∘ V)(p) as single expressions.",
      "(b)  A jacket is marked 480 SAR. Find the final price under each order.",
      "(c)  The customer is wrong. Explain why, using the structure of the two expressions rather than the numbers.",
      "(d)  Now the shop adds a fixed 25 SAR delivery charge AFTER VAT. Write the new composite and explain why the order now DOES matter.",
    ],
    note: "Exact values in SAR, and the reason expressed in terms of the functions.",
    aiPrompt: "“Challenge my explanation of why the order does not matter in part (c), and tell me if I have only shown it for one number.”",
  },

  geogebra: {
    sub: "Define two functions and compose them both ways",
    explore: "enter f(x)=x^2-4 and g(x)=x+3, then plot f(g(x)) and g(f(x)) together. Drag a point along one and read the other. Then find any x where the two curves meet, and say what that means.",
  },

  gate: {
    graph: "g_ops_sum",
    graphAlt: "The graphs of f of x equals x squared minus 4, g of x equals x plus 3, and their sum f plus g of x equals x squared plus x minus 1",
    items: [
      { t: "For f(x) = x² + 1 and g(x) = 3x − 2, find (f + g)(x) and (fg)(x).", eq: null },
      { t: "Find (f ∘ g)(x) and (g ∘ f)(x) for the same pair. Show the substitution step.", eq: null },
      { t: "In ONE sentence, explain why your two answers to question 2 are different.", eq: null },
    ],
    footer: "Fully expanded answers. The substitution step must be visible.",
    routing: "PASS → Enrichment & Challenge (decomposing a three-layer composite).      NOT YET → Targeted Learning Clinic on substitution and brackets, start of next lesson.",
  },

  smart: {
    steps: [
      { h: "Show the chain", d: "Present your two composites side by side with the substitution step visible, and the graph that shows they are different functions." },
      { h: "Expose the trap", d: "Add one worked NON-example: a composition done in the wrong order, or with the bracket dropped, and a sentence saying how a reader would catch it." },
      { h: "Say why it matters", d: "One caption — “why a shop's billing system must fix the order of its operations” — for a non-maths reader." },
    ],
    published: "the class LMS portfolio; the strongest go on the Department wall as our Topic 5 anchor set.",
    reflection: "which is still harder for you — keeping the bracket, or keeping the order?",
  },

  exams: [
    { code: "GAT", full: "Qudurat — General Aptitude", skill: "Two-step percentage and rate chains — discount then tax, conversion then charge — which are compositions in disguise.", fmt: "Multiple choice, about 75 seconds per item.", tip: "Chain the multipliers: 0.80 then 1.15 is one multiplication by 0.92. Far faster than two steps." },
    { code: "SAAT", full: "Tahsili — Achievement Test", skill: "Function operations and composition sit in the Grade 11 band, which is 30% of the mathematics questions.", fmt: "Four-option multiple choice, mixed with the other subjects.", tip: "Check the order before you compute. The wrong-order answer is always one of the four options." },
    { code: "SAT", full: "College Board", skill: "Advanced Math — building and interpreting composite and equivalent function forms.", fmt: "Roughly 35% of the Mathematics section; some items are typed responses.", tip: "If the question gives f(g(x)) and asks for g, substitute a simple number first and work backwards." },
  ],
  examBar: ["THE SINGLE MOST EXAMINED IDEA HERE:", "in (f ∘ g)(x) the inside function acts first — the symbol order and the working order are opposites."],

  summary: [
    "Add, subtract, multiply and divide two functions, and state the domain.",
    "Exclude every value that makes a quotient's denominator zero.",
    "Build a composite function by substituting one function into another.",
    "Show that f ∘ g and g ∘ f are usually different, and say why.",
    "Model a two-step real-world charge as a composition and interpret it in SAR.",
  ],
  homework: [
    "Finish your product and upload it to the LMS portfolio — any of the three formats.",
    "Practice set on Pear Deck: 12 questions, choose your route.",
    "Watch the flipped video for Lesson 5-6: Inverse Relations and Functions (4 min, 2 embedded questions).",
    "Clinic group: bring your Time to Check paper — we start with 10 minutes on substitution and brackets.",
  ],

  notes: {
    cover: "Week 3 lesson for 11B, following Solving Radical Equations.",
    objectives: "Both objectives are verbatim from the curriculum map. The map lists HSF.BF.A.1.B and a plus-standard for composing functions — printed here as the map writes it — and only MP.4 and MP.7.",
    vocabulary: "The map lists exactly two terms for this lesson. Do not add 'domain' or 'inverse' to the vocabulary slide — inverse functions are Lesson 5-6.",
    prior: "Students who cannot expand (x + 3)² will stall at the modelled example. Check it in the diagnostic.",
    diagnose: "Answers: 3x − 5; −21; 9; g(x) = 0; f of g of x, inside first. Expected gap: Q5 — students describe it as 'f times g'.",
    quickCheck: "Answers: (f ∘ g)(x) = 3x² − 1 and (g ∘ f)(x) = (3x − 1)² = 9x² − 6x + 1. The second is where brackets get dropped.",
    guided: "Answers — 1: (f+g)(x) = 3x + 5; (fg)(x) = 2x² + 11x − 6; (f ∘ g)(x) = 2x + 5. 2: (f ∘ g)(x) = √(x − 9), domain x ≥ 9. Do not release independent work until roughly 80% have both.",
    routes: "Students choose their own route and may switch mid-task. Pear Deck flags error patterns live; use it to decide who gets a two-minute conference.",
    production: "Answers — (a) both give 0.92p. (b) 441.60 SAR either way. (c) both composites are a product of the same two constants, and multiplication is commutative — so the order cannot matter here. (d) adding 25 is not a multiplication, so it does not commute with the other two: 1.15(0.80p) + 25 is not 1.15(0.80p + 25).",
    geogebra: "The two composites meet where x² + 6x + 5 = x² − 1, that is x = −1. Ask what the shared point means: one input for which both orders agree.",
    gate: "Answers: (f+g)(x) = x² + 3x − 1; (fg)(x) = 3x³ − 2x² + 3x − 2; (f ∘ g)(x) = 9x² − 12x + 5; (g ∘ f)(x) = 3x² + 1. They differ because the inside function acts first, and squaring then scaling is not the same as scaling then squaring. Score live and route privately.",
    smart: "The non-example in step 2 is the highest-value part — a dropped bracket is the single most common error in this topic.",
    exams: "Show this before homework so the practice set has an obvious purpose.",
    summary: "Route the clinic group privately through the LMS — never announce the list to the class.",
  },
};

(async () => {
  for (const cfg of [GR10_L3, GR11_L5]) await build(cfg);
})();
