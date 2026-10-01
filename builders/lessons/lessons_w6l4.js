// Grade 11 · Topic 6 · Lesson 6-4 — Logarithmic Functions
// Rebuilt 1 Oct 2026 from the verified map data (see the L6-4 rework handoff).
// EQ, MPs, objectives, vocabulary and standards are quoted from the curriculum map.
// IF.B.6 (average rate of change) and BF.B.4.C (read inverse values from a table or
// graph) are taught on the existing instruction slides.
const { build } = require("./lesson_engine");

const GR11_L64 = {
  out: "Gr11_T6_L6-4_Logarithmic_Functions.pptx",
  deckTitle: "Logarithmic Functions — Grade 11 Algebra II",
  mathIndex: "math_w6l4/_index.json", graphIndex: "graphs_w6l4/_index.json",
  topicLine: "TOPIC 6 · EXPONENTIAL AND LOGARITHMIC FUNCTIONS · LESSON 6-4",
  lessonTitle: "Logarithmic Functions", titleSize: 36,
  subtitle: "Every exponential has a mirror image — read its features off the graph",
  titleEq: "a_title_w", titleEqK: 2.4,
  titleEqAlt: "f of x equals 3 to the x, and its inverse f inverse of x equals log base 3 of x",
  grade: "Grade 11", week: "Week 6 · Semester 1, 2026–27",
  footerLeft: "Grade 11 · Algebra II · Topic 6 · Lesson 6-4",
  lessonRef: "Lesson 6-4 — Logarithmic Functions",
  nextLesson: "Topic 6 · Lesson 6-5 — Properties of Logarithms",
  codes: ["HSF.IF.B.5", "HSF.IF.B.6", "HSF.IF.C.7.E", "HSF.IF.C.9", "HSF.BF.B.3", "HSF.BF.B.4", "HSF.BF.B.4.C"],
  mps: ["MP.4", "MP.7"],
  assessments: ["“Give it a go” questions", "“Time to Check”"],

  objectives: [
    "Identify key features of logarithmic functions.",
    "Use inverse properties to analyze logarithmic and exponential functions.",
    "Graph logarithmic functions and interpret their key features.",
    "Write and interpret the inverses of exponential and logarithmic functions.",
  ],
  essentialQuestion: "How is the relationship between logarithmic and exponential functions revealed in the features of their graphs?",

  vocabulary: [
    { term: "Inverse relationship", def: "Two functions undo each other: f^{-1}(f(x)) = x and f(f^{-1}(x)) = x. Their graphs are reflections of each other across the line y = x.", eq: "a_v1", k: 1.5 },
    { term: "Logarithmic function", def: "A function f(x) = log_{b} x with b > 0 and b ≠ 1. It is the inverse of the exponential function g(x) = b^{x}.", eq: "a_v2", k: 1.5 },
  ],
  vocabSub: "Both terms the curriculum map lists for this lesson",

  prior: [
    { h: "Lesson 6-3: logarithms", eq: "a_p1", d: "log_{b} x = y means b^{y} = x. Today the logarithm becomes a whole function with a graph." },
    { h: "Lesson 6-1: graphs of b^{x}", eq: "a_p2", d: "You know its table, its y-intercept (0, 1) and its horizontal asymptote y = 0." },
    { h: "Inverse functions (Topic 5)", eq: "a_p3", d: "To undo a function, swap inputs and outputs; the graphs mirror across y = x." },
  ],
  priorSub: "Three things you already know — today joins them into one picture",
  carryOver: "Swap the inputs and outputs of an exponential and you get a logarithm. Every feature of the logarithm — domain, intercept, asymptote — is a feature of the exponential, turned through the mirror y = x.",
  carryOverEq: "a_co_w",

  diagnose: {
    title: "Warm-Up: What Happens When You Run It Backwards?",
    sub: "Answer on Quizizz — 5 questions, 4 minutes. This builds a gap map, not a grade.",
    questions: [
      { eq: "a_d1", t: "Evaluate." },
      { eq: "a_d2", t: "Evaluate — think about a negative exponent." },
      { eq: "a_d3", t: "Evaluate the exponential function." },
      { eq: "a_d4", t: "Which input gives an output of 9? This is an inverse question." },
      { eq: "a_d5", t: "Try to solve it. What happens, and what does that say about the graph of 3^{x}?" },
    ],
    routing: "0–2 correct → re-teach converting between forms with me.      3–4 correct → straight to the graphs.      5 correct → start the Investigate prompt now.",
  },

  instruction: [
    {
      title: "Exponential and Logarithmic Functions Are Inverses",
      sub: "Objectives 2 and 4 — swap the inputs and outputs, then read inverse values from a table",
      graph: "g_inv", graphW: 3.8, graphX: 0.45, graphY: 2.42,
      graphAlt: "Graphs of f of x equals 3 to the x and f inverse of x equals log base 3 of x, mirror images across the line y equals x, with the pairs 0 comma 1 and 1 comma 0, 1 comma 3 and 3 comma 1, 2 comma 9 and 9 comma 2 marked",
      rowsHead: ["STEP", "RESULT"],
      rowsTop: 2.42, rowH: 0.8, rowsX: 4.5, rowsW: 8.4,
      rows: [
        ["Find the inverse: swap x and y, then solve", { eq: "a_swap", k: 1.3 }],
        ["Inverse properties", { eq: "a_inv1", k: 1.3 }],
        ["Tables: swap the columns", { eq: "a_tabs", k: 0.95 }],
        ["Read an inverse value (BF.B.4.C)", { eq: "a_tab", k: 1.4 }],
      ],
      bar: ["THE SWAP RULE", "(a, b) is on f exactly when (b, a) is on f^{-1} — so the two graphs mirror across y = x, and a table of f read backwards is a table of f^{-1}."],
      barY: 6.32,
      notes: "Table of f(x)=3^x: x -1,0,1,2 gives 1/3,1,3,9. Swap the columns: f^-1 has inputs 1/3,1,3,9 and outputs -1,0,1,2. Reading f^-1(9): find 9 in the OUTPUT column of f, read the input, 2. Graph: the pairs (0,1)<->(1,0), (1,3)<->(3,1), (2,9)<->(9,2) sit mirror-wise across y=x. Inverse properties: log_3(3^x)=x for every x; 3^(log_3 x)=x only for x>0. Misconception to say aloud: f^-1(x) is NOT 1/f(x); the -1 marks the inverse function, not a reciprocal.",
    },
    {
      title: "Key Features of a Logarithmic Function",
      sub: "Objectives 1 and 3 — features of y = log_{b} x, and how fast it grows (IF.B.6)",
      panel: {
        h: "FEATURES OF f(x) = log_{3} x",
        items: [
          "Domain: x > 0. The argument of a logarithm must be positive.",
          "Range: all real numbers.",
          "x-intercept (1, 0) because log_{b} 1 = 0; there is no y-intercept.",
          "Vertical asymptote x = 0: the graph approaches the y-axis but never touches it.",
          "End behaviour: f(x) → −∞ as x → 0^{+}, and f(x) → ∞ as x → ∞, but slowly.",
          "For b > 1 the function is increasing — and its average rate of change keeps falling.",
        ],
        fs: 13,
      },
      panelX: 0.45, panelY: 2.5, panelW: 6.3, panelH: 3.75,
      rowsHead: ["INTERVAL", "AVERAGE RATE OF CHANGE"],
      rowsTop: 2.42, rowH: 1.0, rowsX: 7.0, rowsW: 5.9,
      rows: [
        ["[1, 3]", { eq: "a_arc1", k: 1.1 }],
        ["[3, 9]", { eq: "a_arc2", k: 1.1 }],
        ["[9, 27]", { eq: "a_arc3", k: 1.1 }],
      ],
      bar: ["READ THE RATES", "each interval is three times longer than the last, yet the output rises by exactly 1 each time — so the rate of change falls: increasing, but bending downward."],
      barY: 6.32,
      notes: "Average rate of change = (f(b)-f(a))/(b-a). log_3 on [1,3]: (1-0)/2 = 1/2. On [3,9]: (2-1)/6 = 1/6. On [9,27]: (3-2)/18 = 1/18. Each time the interval triples the output rises by 1. Domain from the exponential: 3^x is always positive, so its inverse only accepts positive inputs; range of log is the domain of 3^x. Misconceptions to say aloud: (1) 'the graph eventually crosses the y-axis' -- the asymptote x=0 comes from the exponential's asymptote y=0 reflected; (2) 'it levels off' -- log keeps increasing without bound, only slowly; (3) 'increasing means constant slope' -- the rate falls.",
    },
    {
      title: "Graphing Transformations of a Logarithm",
      sub: "Objective 3 — shift the graph, then move the asymptote and the key points with it",
      graph: "g_shift", graphW: 5.6, graphX: 0.45, graphY: 2.45,
      graphAlt: "Graph of f of x equals log base 3 of x in blue and g of x equals log base 3 of x minus 2 plus 1 in orange, with vertical asymptotes x equals 0 and x equals 2, and key points marked",
      panel: {
        h: "WATCH MY THINKING: g(x) = log_{3}(x − 2) + 1",
        items: [
          "x − 2 inside: shift right 2. The +1 outside: shift up 1.",
          "The asymptote moves with the horizontal shift: x = 0 becomes x = 2.",
          "Domain: x − 2 > 0, so x > 2. Check this before you draw anything.",
          "Key points: (1, 0) → (3, 1); (3, 1) → (5, 2); (9, 2) → (11, 3).",
          "Check one: g(5) = log_{3} 3 + 1 = 2 ✓",
        ],
        fs: 13,
      },
      panelX: 6.3, panelY: 2.5, panelW: 6.6, panelH: 3.75,
      bar: ["ONE CHECK THAT CATCHES MOST ERRORS", "the argument of the logarithm must stay positive — solve it > 0 for the new domain, and the asymptote is where the argument equals 0."],
      barY: 6.32,
      notes: "Horizontal shifts act on x with the opposite sign: x-2 moves the graph RIGHT. Vertical shift +1 moves the graph up and does not move the asymptote. Key points of f: (1,0),(3,1),(9,2). Shift each by (+2,+1): (3,1),(5,2),(11,3). Both curves pass through (3,1) -- point out the coincidence. Check g(11)=log_3 9+1=3. Misconceptions: (a) moving the asymptote with the vertical shift; (b) shifting left for x-2; (c) forgetting that the domain changes (x>2).",
    },
  ],

  quickCheck: {
    lead: "Write the inverse", leadW: 2.9,
    eq: "a_qc", k: 2.0,
    think: "Swap x and y: x = 3^{y}. Now ask: 3 to what power gives x?",
    rule: "80% correct → straight to guided practice.   Below 80% → one more modelled example with a different base.",
  },

  guided: {
    mins: 4,
    items: [
      { eq: "a_g1", t: "Find the inverse, then check it with f(3) = 8.", hint: "Swap x and y, then rewrite as a logarithm." },
      { eq: "a_g2", t: "Use the table of f: x = 0, 1, 2, 3 gives f(x) = 1, 5, 25, 125.", hint: "Find the output in the table; the input beside it is the answer." },
    ],
  },

  routes: {
    mins: 8,
    tiers: [
      { items: ["Find the inverse of f(x) = 4^{x}, and of g(x) = log_{5} x.", "State the domain, range, x-intercept and asymptote of y = log_{2} x.", "Use the table of f(x) = 2^{x} (x = 0 to 5) to read f^{-1}(16) and f^{-1}(32).", "Sketch y = log_{2} x through (1, 0), (2, 1) and (4, 2) with its asymptote."],
        help: "You may use: the swap rule on the board, the feature list, and a partner.",
        done: "each inverse composes back to x, and your sketch shows the asymptote and three labelled points.", eq: "a_ws1" },
      { items: ["Sketch g(x) = log_{2}(x + 3): give the asymptote, the domain and two key points.", "Find the average rate of change of y = log_{2} x on [1, 4] and on [4, 16].", "A model for a Vision 2030 solar farm says its output is P = 10·3^{t/5} MW after t years (an invented classroom model). Write t as a function of P, then find t when P = 90."],
        help: "You may use: the worked example, and the sentence frames.",
        done: "the asymptote is written as an equation, and the answer to the context question carries units (years).", eq: "a_ws3" },
      { items: ["Explain why the graph of y = log_{3} x can never touch the y-axis, using the graph of 3^{x}.", "Function B is given by the table x = 3, 5, 11 and B(x) = 1, 2, 3. Compare it with A(x) = log_{3} x: which is larger at x = 11, and which transformation of A gives B?", "Explain why the average rate of change of log_{3} x falls from [1, 3] to [3, 9], using what you know about 3^{x}."],
        help: "You may use: nothing but your reasoning.",
        done: "each argument uses the inverse relationship, not just a calculation.", eq: null },
    ],
  },

  production: {
    title: "When Does the Solar Farm Reach Its Target?",
    sub: "A context you have not seen before — this tests transfer",
    situation: "A classroom model for a Vision 2030 solar farm says its output triples every 5 years from 10 MW: P = 10·3^{t/5}, with t in years. Planners want t as a function of P — the inverse. The model is invented for practice, not a forecast.",
    eq: "a_model_w", eqK: 2.2,
    tasks: [
      "(a)  Complete the table for t = 0, 5, 10, 15 and read from it when P = 270 MW.",
      "(b)  Write the inverse t(P) and state its domain.",
      "(c)  Use your inverse to find t when P = 50 MW, to one decimal place.",
      "(d)  Find the average rate of change of t on [10, 30] and on [90, 270] (years per MW) and say what the change means for planners.",
    ],
    note: "Exact expressions shown before decimals; units named (MW, years); the table read BEFORE the inverse is used.",
    aiPrompt: "“Check whether I swapped input and output correctly, and challenge any step I have not justified.”",
  },

  geogebra: {
    sub: "Slide the base and the shifts — watch the asymptote and the key points move",
    preview: "g_inv",
    previewAlt: "Graphs of 3 to the x and log base 3 of x mirrored across the line y equals x",
    url: "https://www.geogebra.org/graphing",
    steps: [
      "Open the link (any browser, no sign-in needed).",
      "Type b = 3 and click the slider button that appears.",
      "Type f(x) = b^(x), then g(x) = log(b, x), then y = x.",
      "Type h = 0 and k = 0 (sliders), then s(x) = log(b, x − h) + k.",
      "Type A = (1, b) and B = (b, 1) and drag the b slider.",
    ],
    explore: "Move h and k: which one moves the asymptote? Set h = 2, k = 1 and read s(5). A and B always mirror across y = x — why?",
  },

  gate: {
    eq: "a_gate_w",
    items: [
      { t: "Write the inverse of the function shown.", eq: "a_gate_w" },
      { t: "State the domain and the asymptote of y = log_{5} x.", eq: null },
      { t: "Use f(2) = 25 to find f^{-1}(25). What does the point (25, 2) tell you about the graph of f^{-1}?", eq: null },
    ],
    footer: "Exact answers only. Question 3 needs the value AND the meaning of the point.",
    routing: "PASS → Enrichment & Challenge (compare a log and an exponential given in different forms).      NOT YET → Targeted Learning Clinic on swapping inputs and outputs, start of next lesson.",
  },

  smart: {
    steps: [
      { h: "Show the model", d: "Present the solar-farm table, the inverse t(P), and the time for one new target output." },
      { h: "Expose the trap", d: "Add one worked NON-example — reading f^{-1}(9) as the reciprocal of f(9) — and say what that wrong answer actually computes." },
      { h: "Say why it matters", d: "One caption — “why planners need time as a function of output” — for a non-maths reader." },
    ],
    published: "the class LMS portfolio; the strongest go on the Department wall as our Topic 6 modelling set.",
    reflection: "which is harder for you — reading an inverse value from a table, or writing the inverse as a formula?",
  },

  exams: [
    { code: "SAAT", full: "Tahsili — Achievement Test", skill: "Domain of a shifted logarithm, no calculator.",
      question: "Domain of f(x) = log_{3}(x − 1) + 2?   (A) x > 1   (B) x > −1   (C) x > 2   (D) all reals",
      steps: ["The argument must be positive: x − 1 > 0.", "So x > 1; the +2 does not change the domain.", "Answer (A)."],
      trap: "(B) flips the sign; (C) uses the vertical shift; (D) forgets the restriction." },
    { code: "SAT", full: "College Board — Advanced Math", skill: "Evaluate an inverse of an exponential function from its equation.",
      question: "f(x) = 2·3^{x}. What is f^{-1}(18)?   (A) 2   (B) 9   (C) 3   (D) 54",
      steps: ["Solve 2·3^{x} = 18.", "Divide by 2: 3^{x} = 9, so x = 2.", "Answer (A)."],
      trap: "(B) stops after dividing; (C) is the base; (D) is f(3), the wrong direction." },
    { code: "GAT", full: "Qudurat — Quantitative Comparison", skill: "Compare two logarithms by bracketing each between integers.",
      question: "A = log_{3} 50 and B = log_{5} 50.   (A) A greater   (B) B greater   (C) equal   (D) cannot tell",
      steps: ["27 < 50 < 81, so A is between 3 and 4.", "25 < 50 < 125, so B is between 2 and 3.", "A > B: answer (A)."],
      trap: "A bigger base does NOT give a bigger logarithm of the same number." },
  ],
  examBar: ["THE SINGLE MOST EXAMINED IDEA HERE:", "read a log or an inverse by swapping inputs and outputs — and keep the argument of the logarithm positive."],

  summary: [
    "Identify the domain, range, intercept, asymptote and end behaviour of a logarithmic function.",
    "Write the inverse of an exponential function and of a logarithmic function by swapping inputs and outputs.",
    "Graph a logarithmic function and its transformations, moving the asymptote with the shift.",
    "Calculate an average rate of change, and read inverse values from a table or a graph.",
  ],
  homework: [
    "Finish your product and upload it to the LMS portfolio — any of the three formats.",
    "Practice set on Pear Deck: 12 questions, choose your route.",
    "Watch the flipped video for our next lesson, Topic 6 · Lesson 6-5 — Properties of Logarithms (4 min, 2 embedded questions).",
    "Clinic group: bring your Time to Check paper — we start with 10 minutes on swapping inputs and outputs.",
  ],

  notes: {
    cover: "Week 6 lesson for 11B, continuing Topic 6 from Lesson 6-3 (Lesson 6-2 is not taught in this sequence). The deck replaces the 25 Sep version, which failed the house rules (see the rework handoff). Standards from the map: HSF.IF.B.5, IF.B.6, IF.C.7.E, IF.C.9, BF.B.3, BF.B.4, (+)BF.B.4.C. IF.B.6 is taught on slide 7 (average rate of change) and BF.B.4.C on slide 6 (reading inverse values from tables and graphs). IF.C.9 is the Investigate task comparing function B with function A. Protect the Mastery Gate if time runs short.",
    objectives: "All four objectives, the essential question and the practices MP.4 and MP.7 are quoted from the curriculum map. Do not add other practices.",
    vocabulary: "Both terms are the map's list. Make students say it aloud: an inverse relationship means each function undoes the other, and the graphs mirror across y = x.",
    prior: "If students cannot evaluate b^x or convert a log (Lesson 6-3), the lesson stalls. Watch diagnostic questions 1 to 3.",
    diagnose: "Answers: log_3 81 = 4; log_2(1/8) = -3; f(3) = 27; f(2) = 9 so the input is 2; 3^x = 0 has no solution, because 3^x is always positive -- this is why the graph of 3^x has asymptote y = 0 and why log has domain x > 0.",
    quickCheck: "Answer: f^-1(x) = log_3 x. Watch for 3^x reciprocal (1/3^x) -- the -1 does not mean reciprocal -- and for swapped base and argument.",
    guided: "Answers: (1) f^-1(x) = log_2 x; check f(3)=8 so f^-1(8)=3, log_2 8 = 3. (2) f^-1(25) = 2 and f^-1(125) = 3: read the output column, take the input.",
    routes: "Answers. Practice: log_4 x and 5^x; domain x>0, range all reals, x-int (1,0), asymptote x=0; f^-1(16)=4, f^-1(32)=5. Apply: asymptote x=-3, domain x>-3, points (-2,0),(1,2); ARC of log_2 on [1,4] is (2-0)/3 = 2/3 and on [4,16] is (4-2)/12 = 1/6; t = 5 log_3(P/10), and P=90 gives t = 5 log_3 9 = 10 years. Investigate: log_3 x is the mirror of 3^x, whose asymptote is y=0, so the mirror asymptote is x=0. B has table (3,1),(5,2),(11,3), so B(x) = log_3(x-2)+1 (shift right 2, up 1); at x=11, B = 3 and A = log_3 11, about 2.18, so B is larger. The ARC falls because 3^x grows faster and faster, so its mirror grows slower and slower.",
    production: "Answers: (a) P = 10, 30, 90, 270 at t = 0, 5, 10, 15, so P=270 at t=15. (b) t = 5 log_3(P/10), domain P > 0. (c) P=50: t = 5 log_3 5 = 5(1.465) = 7.3 years. (d) t(10)=0, t(30)=5, so the ARC on [10,30] is 5/20 = 1/4 year per MW; t(90)=10, t(270)=15, so the ARC on [90,270] is 5/180 = 1/36 year per MW. Each extra MW takes less and less time to reach as the farm gets bigger -- the inverse flattens.",
    geogebra: "The reflection across y=x is the visual proof that exp and log are inverses. With h and k sliders, h moves the vertical asymptote (x=h) and k only moves the curve vertically. A=(1,b) is on b^x at x=1 and its mirror B=(b,1) is on log_b x.",
    gate: "Answers: (1) f^-1(x) = log_5 x. (2) domain x > 0 (positive inputs only); asymptote x = 0. (3) f^-1(25) = 2; the point (25, 2) lies on f^-1 -- it is the mirror of (2, 25) on f. Score live and route privately.",
    smart: "The reciprocal non-example is the highest-value part: f^-1(9) is the INPUT that gives 9, not 1/f(9). The correction names what each wrong answer actually computes.",
    exams: "Show before homework. Format reminders: SAAT four-option, no calculator; SAT two 35-minute adaptive modules with a calculator; GAT about 75 seconds per item with no calculator. Answers: SAAT (A); SAT (A) since 2*3^x=18 gives 3^x=9; GAT (A). Name the trap before revealing it.",
    summary: "Route the clinic group privately through the LMS -- never announce the list to the class.",
  },
};

(async () => { await build(GR11_L64); })();
module.exports = { GR11_L64 };
