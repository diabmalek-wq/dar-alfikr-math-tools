// Week 2 documents — lesson plans, classwork, differentiation, PBL.
// Objectives / EQ / vocabulary / assessments verbatim from the curriculum map.
const { buildAll } = require("./docs_engine");

const MATHDOC = "math_w2_doc/_index.json";
const GRAPH = "graphs_w2/_index.json";
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
// GR10 · 1-2 · Transformations of Functions
// =====================================================================
const GR10_L2 = {
  slug: "Gr10_T1_L2_Transformations_of_Functions",
  mathDocIndex: MATHDOC, graphIndex: GRAPH, timings: T,
  lessonTitle: "Transformations of Functions",
  unit: "Topic 1 — Linear Functions · Lesson 2",
  gradeFull: "Grade 10 — Algebra II",
  week: "Week 2 · Semester 1, 2026–27",
  lessonLine: "Grade 10 · Algebra II · Topic 1: Linear Functions · Lesson 2 — Transformations of Functions",
  codes: ["HSF.BF.B.3", "HSF.IF.B.5"], mps: ["MP.5", "MP.7"],
  assessments: ASSESS,
  objectives: [
    "Identify the different types of transformations (translations, reflections, stretches, and compressions) applied to functions and their graphical representations.",
    "Apply transformations to various functions and predict the changes in their graphs, enhancing their ability to visualize and manipulate mathematical functions.",
  ],
  essentialQuestion: "How do transformations affect the shape and position of a function’s graph?",
  vocabList: "compression ; reflection ; scaling ; stretch ; transformation ; translation",

  plan: {
    outcome: [
      "Students will name all four families of transformation and identify each one from an equation.",
      "Students will read a, b, h and k from the general form and predict the transformed graph before plotting.",
      "Students will write the equation of a transformed graph from its picture.",
    ],
    preclass: [
      "Flipped video (4 min): “Move it, flip it, stretch it” — the four families applied to a parabola. Posted on the LMS 48 hours ahead.",
      "Two embedded EdPuzzle questions: one vertical shift, one horizontal shift.",
      "Evidence of readiness: EdPuzzle completion report plus both embedded answers submitted before the bell.",
    ],
    diagTool: [
      "5-question Quizizz (≤ 4 minutes): describe f(x)+3, f(x−2), −f(x), 4f(x) and f(−x).",
      "Cross-referenced against overnight EdPuzzle watch analytics — who watched, who skipped, who missed the embedded items.",
      "Answers: up 3 ; right 2 ; reflection in the x-axis ; vertical stretch by 4 ; reflection in the y-axis.",
    ],
    diagGap: [
      "Expected gap 1 — the horizontal shift: students read f(x−2) as “left 2”. This is the single most common error in the lesson.",
      "Expected gap 2 — confusing a vertical stretch with a horizontal one when the factor sits inside the bracket.",
      "If more than half miss the horizontal shift, run that re-teach before the modelled example.",
      "Routing: 0–2 correct → re-teach table.  3–4 → straight to modelling.  5 → begin the Investigate prompt immediately.",
    ],
    instruction: [
      "Direct explanation (3–5 min, flagged students only): why f(x−h) moves the graph RIGHT. The input must be h larger to produce the same output.",
      "Whole class: the four families shown on one parent parabola — translation, reflection, stretch, compression — as a four-panel comparison.",
      "The general form g(x) = a·f(b(x−h)) + k read one letter at a time, with a worked line for each.",
      "Modelled example, thinking aloud: g(x) = −2(x−3)² + 5. Read the form first, predict the vertex at (3, 5), then plot to confirm.",
      "Narration focus — the ORDER of transformations: reflect and stretch first, then translate. Swapping the order gives a different graph.",
      "This is a NEW example — it does not repeat the flipped video.",
    ],
    quickCheck: [
      "On whiteboards, 60 seconds: describe every transformation in g(x) = ½(x+4)² − 1.",
      "Expected: vertical compression by a factor of one half ; translation 4 left ; translation 1 down.",
      "80% correct → release guided practice. Below 80% → one further modelled example built one step at a time.",
    ],
    guided: [
      "Two “Give it a go” problems, identical for every student, worked together with the teacher:",
      "(1) g(x) = (x−5)² + 2 — describe the transformation and state the new vertex.  (2) g(x) = −3x² — describe every transformation.",
      "Answers: translation 5 right and 2 up, vertex (5, 2) ; reflection in the x-axis with a vertical stretch by 3.",
      "Feedback: worked live on the board step by step; students self-mark and circle their OWN first error.",
    ],
    independent: [
      "Delivered through the “Choose Your Route” sheet with live feedback in Pear Deck. Routes are named for the task, not for the student.",
      "PRACTICE — Secure the method. Identify transformations from equations, match equations to graphs, state new vertices, sketch two translations. Done when: you can name each transformation from the equation alone.",
      "APPLY — Use it in context. Write equations from graphs, apply three transformations in order, explain the effect of swapping two, one arch context question. Done when: your sketch matches your equation and the vertex is exact.",
      "INVESTIGATE — Find out why. Prove two forms are not equivalent, find a single equivalent transformation, explain the 1/b horizontal factor. Done when: you have an argument, not just an answer.",
      "Every student sits the same Mastery Gate. The gate is not differentiated, because it is the evidence.",
    ],
    production: [
      "Non-routine transfer task — this context has not appeared in practice.",
      "A pedestrian bridge over a Riyadh highway has a parabolic arch, h(x) = −0.02(x−30)² + 18, with x the distance across the span in metres.",
      "(a) State the vertex and interpret it with units. (b) The arch must be 4 m taller — write the new equation and name the transformation. (c) A second identical arch starts 80 m further along — write its equation. (d) Explain why changing the 0.02 would be a poor way to make it taller.",
      "Answers: (a) (30, 18) — highest point 18 m, 30 m across. (b) h(x) = −0.02(x−30)² + 22, translation 4 up. (c) h(x) = −0.02(x−110)² + 18, translation 80 right. (d) it changes the width and the whole shape, so the supports would no longer be 60 m apart.",
      "Students then hand their reasoning to the AI critic and ask it to challenge any step they have not justified.",
    ],
    criteria: [
      "Minimum acceptable standard: every transformation named, the vertex exact, and each answer justified by reference to a, h or k.",
      AI_CRITIC,
      "Completed independently by the student: the written justification for parts (a)–(d). AI may challenge it; it may not write it.",
    ],
    evidence: [
      "“Time to Check” — one individual task. No notes, no partner, no AI.",
      "Given the graph of a downward parabola with vertex (−2, 7): 1. write its equation in the form g(x) = a(x−h)² + k. 2. name every transformation applied to f(x) = x². 3. in ONE sentence explain why the horizontal shift uses the opposite sign.",
      "Answer: g(x) = −(x+2)² + 7 ; reflection in the x-axis, translation 2 left and 7 up ; the input must change to compensate, so the sign reverses.",
      "Done when: the equation is exact, every transformation is named, and question 3 gives a reason rather than a restatement.",
      "Scored live in Pear Deck as submissions arrive; result logged in the Impact Dashboard Mastery Rate.",
    ],
    refinement: [
      "Students revise their bridge reasoning using the AI critique and the teacher's micro-conference note.",
      "Final product, three equally acceptable formats: a Canva one-pager, a photographed hand-written solution, or a 45-second voice note.",
      "Required content: the parent function transformed one step at a time with a sketch at each stage; ONE worked non-example with the horizontal sign reversed; and a caption on why an engineer transforms a function rather than starting again.",
      "Graded on originality and clarity of reasoning, not correctness alone.",
    ],
    publication: [
      "Published to the class LMS portfolio; the strongest go on the Mathematics Department wall as the Topic 1 anchor set.",
      "Reflection question: “Which is still harder for you — the vertical moves, or the horizontal ones?”",
    ],
    differentiation: [
      "PRACTICE — Secure the method. Identification from equations, matching, and two sketches; the general-form table stays on the board and a partner is allowed. Done when: each transformation can be named from the equation alone.",
      "APPLY — Use it in context. Equations from graphs, ordered transformations, and an arch application. Done when: the sketch matches the equation and the vertex is exact.",
      "INVESTIGATE — Find out why. Non-equivalence proof, an equivalent single transformation, and the 1/b explanation. Done when: there is an argument, not just an answer.",
      "No student is labelled. The routes describe tasks; every student sits the same Mastery Gate.",
    ],
    adaptive: PILLAR_ADAPTIVE,
    saudi: [
      "Production context: a pedestrian bridge over a Riyadh highway, modelled by a parabolic arch — translating the design along the span and raising its clearance.",
      "In-class project: redesigning the arch of a shaded walkway for a school courtyard, with a fixed span and a required clearance height.",
      "Discussion prompt: why civil engineers transform a standard curve rather than deriving a new one for every bridge.",
    ],
    exams: [
      "SAT — Advanced Math: nonlinear functions and equivalent transformed forms, roughly 35% of the Mathematics section. Practice tip: Desmos is allowed for the whole section — graph it and compare.",
      "SAAT (Tahsili) — transformations of functions sit in the Grade 11 band, 30% of the mathematics items. Practice tip: read the sign inside the bracket twice.",
      "GAT (Qudurat) — recognising a shifted or reflected graph at a glance inside a data item, about 75 seconds per question. Practice tip: find the vertex first; it gives h and k immediately.",
    ],
  },

  plan2026: {
    day: "Sunday, Week 2", section: "Grade 10 — 10A and 10C",
    tools: "Quizizz (diagnostic) · Pear Deck (live practice feedback) · GeoGebra Graphing Calculator with sliders · Canva (final product) · Whiteboards",
    resources: "Lesson presentation (18 slides) · “Choose Your Route” differentiation sheet · “Give It a Go” classwork · “Raising the Walkway” project task · squared paper",
    competencies: ["Predicting the effect of a change before carrying it out.", "Justifying an algebraic step by reference to a named parameter."],
    technology: ["Quizizz live diagnostic with instant gap analysis.", "GeoGebra sliders on a, b, h and k — changing one at a time and describing the effect."],
    reallife: ["The parabolic arch of a pedestrian bridge over a Riyadh highway.", "A shaded walkway for the school courtyard, raised and repositioned."],
    values: ["Precision — an exact vertex, not an approximate one.", "Responsibility for one's own learning route."],
    soft: ["Collaboration in assigned group roles.", "Explaining a prediction to a peer before testing it."],
    hard: ["Identifying translations, reflections, stretches and compressions.", "Reading a, b, h and k from the general form and writing equations from graphs."],
    phases: [
      "FIKR Phase 1 — Diagnose. 5-question Quizizz on the four families. Results read as a gap map; students routed to the re-teach table, straight to modelling, or the Investigate prompt.",
      "FIKR Phase 2 — Targeted Instruction. Focused re-teach on the horizontal shift for flagged students. Whole class: four families on one parent parabola; the general form read one letter at a time; modelled example g(x) = −2(x−3)² + 5 with the vertex predicted before plotting. Quick check on whiteboards.",
      "FIKR Phase 3 — Practice. Two identical “Give it a go” problems worked together. Students then choose a route on the “Choose Your Route” sheet and may switch at any time. Live feedback via Pear Deck; 2-minute micro-conferences.",
      "FIKR Phase 4 — Production. Riyadh pedestrian-bridge arch: interpret the vertex, raise the arch, translate a second arch, and critique a proposed change to the leading coefficient. AI used as critic only.",
      "FIKR Phase 5 — Proof of Learning. “Time to Check” — write the equation of an unseen transformed parabola. No notes, no partner, no AI.",
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
    closure: "Two minutes of peer show-and-tell on the final products, then the reflection question: “Which is still harder for you — the vertical moves, or the horizontal ones?”",
    homework: "Finish the final product and upload to the LMS portfolio (any of the three formats). Practice set on Pear Deck — 12 questions, choose your route. Watch the flipped video for Lesson 1-3: Piecewise-Defined Functions. Clinic group: bring your Time to Check paper.",
  },

  classwork: {
    subtitle: "Show all your working. Naming the transformation is half the answer — the other half is saying which way it moves.",
    sections: [
      { h: "SECTION A — Naming the transformation", note: "Objective 1", lines: 4,
        q: [
          { n: "Q1", eq: "t_ws1", t: "Describe every transformation applied to the parent function, and state the new vertex." },
          { n: "Q2", eq: "t_ws2", t: "Describe every transformation. There are two." },
          { n: "Q3", eq: "t_ws3", t: "Describe every transformation. There are three." },
          { n: "Q4", eq: "t_ws4", t: "Is this a vertical or a horizontal scaling? By what factor?" },
        ] },
      { h: "SECTION B — Reading the general form", note: "Objective 2", lines: 4,
        intro: "Use the four-panel comparison from the lesson if you need to.",
        graph: "g_transform_panel", graphW: 560,
        q: [
          { n: "Q5", eq: "t_ws5", t: "State the vertex, then sketch the graph on squared paper." },
          { n: "Q6", eq: "t_ws6", t: "State the vertex and say whether the parabola is narrower or wider than the parent." },
        ] },
      { h: "SECTION C — Working backwards from a graph", note: "Objective 2", lines: 5,
        intro: "The graph below shows a transformed parabola.",
        graph: "g_transform_gate", graphW: 380,
        text: [
          "Q7.  Write the equation of the graph shown, in the form g(x) = a(x−h)² + k.",
          "Q8.  Name every transformation that has been applied to the parent function.",
          "Q9.  A student writes the answer as g(x) = −(x−2)² + 7. Explain, in one sentence, exactly what they got wrong.",
        ] },
      { h: "SECTION D — Order matters", note: "MP.7 — using structure", lines: 4,
        text: [
          "Q10.  Take f(x) = x². Apply a vertical stretch by 3, THEN a translation 2 up. Write the equation.",
          "Q11.  Now apply the same two transformations in the opposite order. Write the equation.",
          "Q12.  Your two answers are different. Explain why, in one sentence.",
        ] },
    ],
  },

  diffSheet: {
    routes: [
      { note: "Identify and match", done: "you can name each transformation from the equation alone.",
        intro: "Describe every transformation applied to the parent function f(x) = x².",
        grid: [["1.", "t_ws1"], ["2.", "t_ws2"], ["3.", "t_ws3"], ["4.", "t_ws4"], ["5.", "t_ws5"], ["6.", "t_ws6"]],
        tasks: ["7.  Choose any two of the equations above and sketch them on squared paper, showing the parent function as a dashed curve."],
        lines: 2 },
      { note: "Equations from graphs, and one context", done: "your sketch matches your equation, and the vertex is exact.",
        intro: "Work from the picture to the equation, then apply what you find.",
        graph: "g_transform_worked", graphW: 400,
        tasks: [
          "1.  The graph above shows g(x) = −2(x−3)² + 5. Without plotting, write the equation of the graph obtained by translating it 4 left and 3 down.",
          "2.  A parabola has vertex (−1, −6) and passes through (0, −4). Find its equation in the form g(x) = a(x−h)² + k.",
          "3.  Apply a reflection in the x-axis, then a vertical stretch by 2, then a translation 5 up, to f(x) = x². Write the equation at each stage.",
          "4.  A shaded walkway arch is modelled by h(x) = −0.05(x−20)² + 12. The arch must be raised by 3 m without changing its width. Write the new equation and name the transformation.",
        ], lines: 4 },
      { note: "Arguments, not answers", done: "you have an argument, not just an answer.",
        tasks: [
          ["1.  Show that   ", { eq: "t_ws1", k: 1.15 }, "   and a translation 1 right followed by 4 down of the parent function are NOT the same graph. Explain the difference precisely."],
          "2.  Find a SINGLE transformation that has the same effect as: reflect in the y-axis, then reflect in the x-axis. Justify your answer.",
          "3.  Explain why a horizontal stretch by a factor of 3 appears in the equation as f(x/3) and not f(3x). Use the idea of what the input must do.",
        ], lines: 5 },
    ],
  },

  pbl: {
    title: "Raising the Walkway", minutes: 20,
    subtitle: "A 20-minute group project. Work in fours. Every member signs the sheet.",
    driving: "The school needs a shaded walkway between two buildings. How do we move and reshape one standard arch to fit a space it was never designed for?",
    situation: [
      "The Maintenance Department has one standard arch design already costed and approved. Its height in metres, measured from the left support, is given by the function below, where x is the distance across the span.",
      "The new walkway must span the same 60 m but needs 4 m more clearance at the centre for a service vehicle. A second, identical arch must begin 80 m along the same path.",
      "Re-deriving the design would mean a new costing and a new approval. Transforming the existing one would not.",
    ],
    eq: "ctx_arch",
    steps: [
      ["1", "READ THE DESIGN  (4 min)", "State the vertex of the existing arch and say, in one sentence with units, what it means for the walkway."],
      ["2", "RAISE IT  (4 min)", "Write the equation of the arch raised by 4 m. Name the transformation you used."],
      ["3", "MOVE IT  (4 min)", "Write the equation of the second arch, beginning 80 m further along. Name the transformation."],
      ["4", "REJECT A BAD IDEA  (5 min)", "A colleague suggests changing the 0.02 instead, to make the arch taller. Explain in writing why that is a poor solution."],
      ["5", "PRESENT  (3 min)", "Prepare one sentence your presenter will say: why transforming a known design beats starting again."],
    ],
    working: [["Step 1 — the vertex, and what it means:", 2], ["Step 2 — the raised arch:", 2],
              ["Step 3 — the second arch:", 2], ["Step 4 — why the colleague is wrong:", 4],
              ["Step 5 — our sentence:", 2]],
    roles: ["Reader — states the vertex", "Designer — writes the new equations", "Checker — tests every claim", "Presenter — says the sentence"],
    doneWhen: ["Both new equations are exact.", "Every transformation is named, not just applied.", "Step 4 explains the effect on the SHAPE, not just the height.", "Your sentence makes sense to someone who does not study maths."],
    materials: ["This sheet", "Squared paper", "A pencil and ruler", "The general-form table from the board"],
  },
};

// =====================================================================
// GR11 · 5-3 · Graphing Radical Functions
// =====================================================================
const GR11_L3 = {
  slug: "Gr11_T5_L3_Graphing_Radical_Functions",
  mathDocIndex: MATHDOC, graphIndex: GRAPH, timings: T,
  lessonTitle: "Graphing Radical Functions",
  unit: "Topic 5 — Rational Exponents and Radical Functions · Lesson 5-3",
  gradeFull: "Grade 11 — Algebra II",
  week: "Week 2 · Semester 1, 2026–27",
  lessonLine: "Grade 11 · Algebra II · Topic 5: Rational Exponents and Radical Functions · Lesson 5-3 — Graphing Radical Functions",
  codes: ["HSA.REI.A.2", "HSF.IF.C.7.B", "HSF.BF.B.3", "HSF.BF.B.4"], mps: ["MP.4", "MP.7"],
  assessments: ASSESS,
  objectives: [
    "Graph radical functions and transformations of radical functions.",
    "Write an equation for the transformation of a radical function given a graph.",
  ],
  essentialQuestion: "How does the graph of f(x) = nth root of x change depending on whether n is even or odd?",
  vocabList: "cube root function ; nth root function ; parent radical function ; radical function ; square root function ; transformations",

  plan: {
    outcome: [
      "Students will sketch both parent radical functions and state why an even index halves the plane while an odd index does not.",
      "Students will find the start point of a transformed radical function and state its domain and range in interval notation.",
      "Students will write the equation of a radical graph they are shown, using a five-step method.",
    ],
    preclass: [
      "Flipped video (4 min): “Two parents, one question” — the square root and cube root graphs side by side. Posted on the LMS 48 hours ahead.",
      "Two embedded EdPuzzle questions: one domain, one transformation.",
      "Evidence of readiness: EdPuzzle completion report plus both embedded answers submitted before the bell.",
    ],
    diagTool: [
      "5-question Quizizz (≤ 4 minutes): domains of √(x−2) and ∛(x+4); transformations of −√x and √x + 5; and the domain of √(−x).",
      "Cross-referenced against overnight EdPuzzle watch analytics.",
      "Answers: [2, ∞) ; (−∞, ∞) ; reflection in the x-axis ; translation 5 up ; (−∞, 0].",
    ],
    diagGap: [
      "Expected gap 1 — students give the domain of √(x−2) as x ≥ −2, reversing the sign.",
      "Expected gap 2 — the final item, √(−x): students assume x ≥ 0 out of habit rather than solving −x ≥ 0.",
      "If more than half miss the domain items, reteach “set the radicand ≥ 0 and solve” before the modelled example.",
      "Routing: 0–2 correct → re-teach table.  3–4 → straight to modelling.  5 → begin the Investigate prompt immediately.",
    ],
    instruction: [
      "Direct explanation (3–5 min, flagged students only): the domain of a radical function is found by setting the radicand ≥ 0 and solving — it is not read off the equation by eye.",
      "Whole class: the two parent functions side by side. An EVEN index cannot take a negative radicand, so the graph is half a curve from a start point; an ODD index accepts anything, so it runs across the whole plane. This answers the essential question directly.",
      "Modelled example, thinking aloud: g(x) = 2√(x−3) + 1. Find the start point (3, 1) FIRST, then the domain [3, ∞), then plot two easy points.",
      "Narration focus — students who build a table of values from x = 0 waste four minutes and get the domain wrong. The start point is the technique.",
      "Objective 2: reading a graph backwards in five steps — start point, index, direction, one more point, then test.",
      "This is a NEW example — it does not repeat the flipped video.",
    ],
    quickCheck: [
      "On whiteboards, 60 seconds: sketch g(x) = √(x+5) − 2 and state its domain.",
      "Expected: start point (−5, −2), domain [−5, ∞).",
      "80% correct → release guided practice. Below 80% → one further modelled example with a negative value of a.",
    ],
    guided: [
      "Two “Give it a go” problems, identical for every student, worked together with the teacher:",
      "(1) g(x) = √(x−4) — state the start point and domain, then sketch.  (2) g(x) = −∛x + 2 — describe every transformation and state the domain.",
      "Answers: start (4, 0), domain [4, ∞) ; reflection in the x-axis with a translation 2 up, domain (−∞, ∞).",
      "Feedback: worked live on the board step by step; students self-mark and circle their OWN first error.",
    ],
    independent: [
      "Delivered through the “Choose Your Route” sheet with live feedback in Pear Deck. Routes are named for the task, not for the student.",
      "PRACTICE — Secure the method. Domains, matching equations to graphs, two sketches, three start points. Done when: every domain is in correct interval notation.",
      "APPLY — Use it in context. Three transformed sketches including a cube root, two equations from graphs, a domain comparison, one stopping-distance context. Done when: your equation reproduces the graph you were given.",
      "INVESTIGATE — Find out why. Why √(−x) is a reflection, the rotational symmetry of the cube root, and constructing a function with domain (−∞, 4]. Done when: you have an argument, not just an answer.",
      "Every student sits the same Mastery Gate. The gate is not differentiated, because it is the evidence.",
    ],
    production: [
      "Non-routine transfer task — this context has not appeared in practice.",
      "A maintenance crew works on a tower in the King Abdullah Financial District. Ignoring air resistance, the speed of a dropped object on reaching the ground is v = √(2gh), with g = 9.8 m/s² and h the drop height in metres.",
      "(a) Name the parent function and state the domain in this context. (b) Sketch v against h from 0 to 50 m, labelling two exact points. (c) Use the graph to explain why doubling the height does not double the speed. (d) By what factor must the height increase for the speed to double? Justify algebraically.",
      "Answers: (a) square root parent, domain h ≥ 0. (b) (0, 0) and (5, 9.9). (c) the graph flattens — equal increases in height give smaller increases in speed. (d) a factor of 4, since v is proportional to √h.",
      "Students then hand their reasoning to the AI critic and ask it to challenge the domain they chose.",
    ],
    criteria: [
      "Minimum acceptable standard: the domain correct for the CONTEXT, not just the algebra; two exact labelled points; and part (d) justified by proportionality rather than by trial.",
      AI_CRITIC,
      "Completed independently by the student: the written justification for parts (c) and (d).",
    ],
    evidence: [
      "“Time to Check” — one individual task. No notes, no partner, no AI.",
      "Given the graph of a square root curve starting at (−1, −4): 1. write its equation. 2. state domain and range in interval notation. 3. in ONE sentence, say how you knew the index was even.",
      "Answer: g(x) = 3√(x+1) − 4 ; domain [−1, ∞), range [−4, ∞) ; the graph is half a curve with a definite start point.",
      "Done when: the equation reproduces the graph, both intervals are exact, and question 3 gives a reason from the picture.",
      "Scored live in Pear Deck as submissions arrive; result logged in the Impact Dashboard Mastery Rate.",
    ],
    refinement: [
      "Students revise their falling-object reasoning using the AI critique and the teacher's micro-conference note.",
      "Final product, three equally acceptable formats: a Canva one-pager, a photographed hand-written solution, or a 45-second voice note.",
      "Required content: parent → domain → transformation → sketch as a justified chain; ONE worked non-example where the domain was taken from the equation without checking the radicand; and a caption on why the speed does not double when the height does.",
      "Graded on originality and clarity of reasoning, not correctness alone.",
    ],
    publication: [
      "Published to the class LMS portfolio; the strongest go on the Mathematics Department wall as the Topic 5 anchor set.",
      "Reflection question: “Which is still harder for you — finding the start point, or getting the domain right?”",
    ],
    differentiation: [
      "PRACTICE — Secure the method. Domains, matching, sketching translations, naming start points; the five-step table stays on the board and a partner is allowed. Done when: every domain is in correct interval notation.",
      "APPLY — Use it in context. Transformed sketches including a cube root, equations from graphs, and a stopping-distance application. Done when: the equation reproduces the given graph.",
      "INVESTIGATE — Find out why. Reflection of √(−x), rotational symmetry of the cube root, and constructing a required domain. Done when: there is an argument, not just an answer.",
      "No student is labelled. The routes describe tasks; every student sits the same Mastery Gate.",
    ],
    adaptive: PILLAR_ADAPTIVE,
    saudi: [
      "Production context: safety planning for a maintenance crew on a tower in the King Abdullah Financial District, Riyadh.",
      "In-class project: sizing the emergency braking zone for a Riyadh Metro platform, where stopping distance and speed are related by a square root.",
      "Discussion prompt: why a safety engineer plots the whole curve rather than checking one value.",
    ],
    exams: [
      "SAT — Advanced Math: nonlinear functions and equivalent forms of a radical expression, roughly 35% of the Mathematics section. Practice tip: Desmos is allowed — graph it and read the start point off.",
      "SAAT (Tahsili) — radical and rational expressions sit in the Grade 11 band, 30% of the mathematics items. Practice tip: check the domain before you check the answer; wrong-domain options are always offered.",
      "GAT (Qudurat) — recognising a root relationship in a data item and estimating quickly, about 75 seconds per question. Practice tip: if doubling the input does not double the output, suspect a root.",
    ],
  },

  plan2026: {
    day: "Sunday, Week 2", section: "Grade 11 — 11B",
    tools: "Quizizz (diagnostic) · Pear Deck (live practice feedback) · GeoGebra with an index slider · Canva (final product) · Whiteboards",
    resources: "Lesson presentation (18 slides) · “Choose Your Route” differentiation sheet · “Give It a Go” classwork · “The Braking Zone” project task · squared paper",
    competencies: ["Determining a domain from a condition rather than by inspection.", "Reconstructing an equation from a graph systematically."],
    technology: ["Quizizz live diagnostic with instant gap analysis.", "GeoGebra with a slider on the index n — stepping through 2, 3, 4, 5 to discover the parity pattern."],
    reallife: ["Speed of a dropped object during tower maintenance in the King Abdullah Financial District.", "Braking distance and speed on the Riyadh Metro."],
    values: ["Precision — an exact domain, not an approximate one.", "Responsibility for one's own learning route."],
    soft: ["Collaboration in assigned group roles.", "Explaining a safety conclusion to a non-specialist."],
    hard: ["Sketching both parent radical functions and their transformations.", "Stating domain and range in interval notation; writing an equation from a graph."],
    phases: [
      "FIKR Phase 1 — Diagnose. 5-question Quizizz on domains and transformations of radical functions. Results read as a gap map; students routed to the re-teach table, straight to modelling, or the Investigate prompt.",
      "FIKR Phase 2 — Targeted Instruction. Focused re-teach on finding a domain by solving radicand ≥ 0. Whole class: the two parent functions side by side, answering the essential question about even and odd indices; modelled example g(x) = 2√(x−3) + 1 with the start point found first; then the five-step method for writing an equation from a graph. Quick check on whiteboards.",
      "FIKR Phase 3 — Practice. Two identical “Give it a go” problems worked together. Students then choose a route on the “Choose Your Route” sheet and may switch at any time. Live feedback via Pear Deck; 2-minute micro-conferences.",
      "FIKR Phase 4 — Production. Falling-object speed during tower maintenance: name the parent, sketch with exact points, explain why doubling height does not double speed, and find the factor that does. AI used as critic only.",
      "FIKR Phase 5 — Proof of Learning. “Time to Check” — write the equation of an unseen radical graph and state domain and range. No notes, no partner, no AI.",
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
    closure: "Two minutes of peer show-and-tell on the final products, then the reflection question: “Which is still harder for you — finding the start point, or getting the domain right?”",
    homework: "Finish the final product and upload to the LMS portfolio (any of the three formats). Practice set on Pear Deck — 12 questions, choose your route. Watch the flipped video for Lesson 5-4: Solving Radical Equations. Clinic group: bring your Time to Check paper.",
  },

  classwork: {
    subtitle: "Show all your working. State every domain in interval notation — an answer without a domain is incomplete.",
    sections: [
      { h: "SECTION A — Domains first", note: "Objective 1", lines: 4,
        intro: "For each function, set the radicand ≥ 0, solve, and write the domain in interval notation.",
        q: [
          { n: "Q1", eq: "r_ws2", t: "State the domain." },
          { n: "Q2", eq: "r_ws8", t: "State the domain. Solve the condition — do not guess." },
          { n: "Q3", eq: "r_ws4", t: "State the domain. Check the index first." },
          { n: "Q4", eq: "r_ws6", t: "State the domain. This one is not what it looks like." },
        ] },
      { h: "SECTION B — Even index or odd index", note: "The essential question", lines: 3,
        intro: "The two parent functions are shown below.",
        graph: "g_radical_parents", graphW: 540,
        text: [
          "Q5.  In one sentence, say why the square root graph is only half a curve.",
          "Q6.  In one sentence, say why the cube root graph runs through every quadrant.",
        ] },
      { h: "SECTION C — Sketching transformations", note: "Objective 1", lines: 4,
        q: [
          { n: "Q7", eq: "r_ws1", t: "State the start point, then sketch on squared paper." },
          { n: "Q8", eq: "r_ws5", t: "Describe the transformation and sketch it against the parent." },
          { n: "Q9", eq: "r_ws7", t: "Describe every transformation, then state the domain." },
        ] },
      { h: "SECTION D — Working backwards from a graph", note: "Objective 2", lines: 5,
        intro: "The graph below shows a transformed square root function.",
        graph: "g_radical_worked", graphW: 400,
        text: [
          "Q10.  Using the five-step method, write the equation of the solid curve shown.",
          "Q11.  State its domain and range in interval notation.",
          "Q12.  A student says the start point is (3, 0). Explain, in one sentence, what they have missed.",
        ] },
    ],
  },

  diffSheet: {
    routes: [
      { note: "Domains and sketches", done: "every domain is in correct interval notation.",
        intro: "State the domain of each function in interval notation.",
        grid: [["1.", "r_ws1"], ["2.", "r_ws2"], ["3.", "r_ws3"], ["4.", "r_ws4"], ["5.", "r_ws6"], ["6.", "r_ws8"]],
        tasks: ["7.  Choose any two of the functions above and sketch them on squared paper, marking the start point clearly."],
        lines: 2 },
      { note: "Equations from graphs, and one context", done: "your equation reproduces the graph you were given.",
        intro: "Work from the picture to the equation, then apply what you find.",
        graph: "g_radical_gate", graphW: 360,
        tasks: [
          "1.  Write the equation of the curve shown above, using the five-step method. Show each step.",
          "2.  State the domain and range of your answer in interval notation.",
          "3.  Sketch g(x) = −2∛(x−1) + 3, marking the point of symmetry. State its domain.",
          "4.  On a Riyadh Metro platform, emergency braking distance d metres and entry speed v m/s satisfy v = √(2ad) with a = 1.2 m/s². Sketch v against d for 0 ≤ d ≤ 60 and state the exact speed at d = 24.",
        ], lines: 4 },
      { note: "Arguments, not answers", done: "you have an argument, not just an answer.",
        tasks: [
          ["1.  Explain why the graph of   ", { eq: "r_ws6", k: 1.15 }, "   is a reflection of the parent function rather than an error. Refer to the radicand condition."],
          "2.  Show that the cube root function has rotational symmetry of order 2 about the origin. Justify it algebraically, not just from the picture.",
          "3.  Construct a transformation of the square root function whose domain is (−∞, 4]. Explain how you built it.",
        ], lines: 5 },
    ],
  },

  pbl: {
    title: "The Braking Zone", minutes: 20,
    subtitle: "A 20-minute group project. Work in fours. Every member signs the sheet. Exact values only.",
    driving: "A Metro train entering a platform must stop safely. How long does the braking zone need to be — and why does doubling it not let the train arrive twice as fast?",
    situation: [
      "The Riyadh Metro operations team is reviewing platform approach speeds. Under emergency braking at a constant deceleration a, the entry speed v in metres per second and the braking distance d in metres are related by the formula below.",
      "For this review, take a = 1.2 m/s². The team needs to understand the SHAPE of the relationship, not just one value — because their safety margin depends on how the curve behaves as distance grows.",
    ],
    eq: "ctx_speed",
    data: [["braking distance d (m)", "6", "24", "54", "96"], ["entry speed v (m/s)", "", "", "", ""]],
    steps: [
      ["1", "NAME THE FAMILY  (3 min)", "What kind of function is v in terms of d? Name the parent function and state the domain in this context."],
      ["2", "FILL THE TABLE  (4 min)", "Complete the table above with exact values. Leave surds as surds — do not round."],
      ["3", "DRAW IT  (5 min)", "Plot v against d on squared paper for 0 ≤ d ≤ 100. Label the four points from your table."],
      ["4", "THE SAFETY QUESTION  (5 min)", "The team doubles the braking zone from 24 m to 48 m. By what factor does the safe entry speed increase? Justify it algebraically, then confirm it from your graph."],
      ["5", "PRESENT  (3 min)", "Prepare one sentence your presenter will say: why the safety margin gets WORSE, not better, as speeds rise."],
    ],
    working: [["Step 1 — parent function and domain:", 2], ["Step 2 — show one exact calculation:", 3],
              ["Step 4 — the factor, justified:", 4], ["Step 5 — our sentence:", 2]],
    roles: ["Calculator — fills the table exactly", "Plotter — draws the curve", "Checker — tests every claim", "Presenter — says the sentence"],
    doneWhen: ["Every table value is exact, not rounded.", "Your curve starts at the origin and flattens.", "Step 4 is justified by proportionality, not by trial.", "Your sentence makes sense to someone who does not study maths."],
    materials: ["This sheet", "Squared paper", "A pencil and ruler", "Scientific calculator for the final check only"],
  },
};

// =====================================================================
// GR11 · 5-4 · Solving Radical Equations
// =====================================================================
const GR11_L4 = {
  slug: "Gr11_T5_L4_Solving_Radical_Equations",
  mathDocIndex: MATHDOC, graphIndex: GRAPH, timings: T,
  lessonTitle: "Solving Radical Equations",
  unit: "Topic 5 — Rational Exponents and Radical Functions · Lesson 5-4",
  gradeFull: "Grade 11 — Algebra II",
  week: "Week 2 · Semester 1, 2026–27",
  lessonLine: "Grade 11 · Algebra II · Topic 5: Rational Exponents and Radical Functions · Lesson 5-4 — Solving Radical Equations",
  codes: ["HSA.REI.A.1", "HSA.REI.A.2", "HSA.CED.A.4"], mps: ["MP.2", "MP.3"],
  assessments: ASSESS,
  objectives: [
    "Solve an equation involving radicals.",
    "Determine if a solution to an equation involving radicals is valid or extraneous.",
    "Solve an inequality involving radicals.",
  ],
  essentialQuestion: "What strategy can be used to solve equations involving radicals?",
  vocabList: "extraneous solution",

  plan: {
    outcome: [
      "Students will solve a radical equation by isolating the radical and squaring both sides.",
      "Students will check every candidate in the original equation and identify extraneous solutions, explaining where they come from.",
      "Students will solve a radical inequality using both the domain condition and the inequality itself.",
    ],
    preclass: [
      "Flipped video (4 min): “Square both sides — then check” — the five-step method with one worked example. Posted on the LMS 48 hours ahead.",
      "Two embedded EdPuzzle questions: one simple solve, one expansion of a squared bracket.",
      "Evidence of readiness: EdPuzzle completion report plus both embedded answers submitted before the bell.",
    ],
    diagTool: [
      "5-question Quizizz (≤ 4 minutes): solve √x = 7, √(x+4) = 5, ∛(2x) = 4, √(5x−1) = 2, and expand (x−1)².",
      "Cross-referenced against overnight EdPuzzle watch analytics.",
      "Answers: 49 ; 21 ; 32 ; 1 ; x² − 2x + 1.",
    ],
    diagGap: [
      "Expected gap 1 — the expansion item. A student who writes (x−1)² = x² − 1 will fail every question in this lesson at step 3.",
      "Expected gap 2 — the cube root item: students square instead of cubing, out of habit.",
      "If more than half miss the expansion, reteach it before the modelled example — it is the load-bearing skill.",
      "Routing: 0–2 correct → re-teach table.  3–4 → straight to modelling.  5 → begin the Investigate prompt immediately.",
    ],
    instruction: [
      "Direct explanation (3–5 min, flagged students only): expanding a squared binomial, with (x−1)² done on the board by a student.",
      "Whole class: the five-step method — isolate, square, expand, collect, factorise — worked on √(x+5) = x−1, giving candidates x = 4 and x = −1.",
      "Step 5 is the lesson: both candidates are CHECKED in the original equation. x = 4 survives; x = −1 does not.",
      "The graph makes it visible: y = √(x+5) and y = x−1 meet ONCE, at x = 4. At x = −1 the curve is at 2 and the line at −2 — four apart, but squaring makes 2 and −2 identical. That is exactly how the false solution enters.",
      "Objective 3: radical inequalities need TWO conditions — the radicand ≥ 0, and the inequality itself. Worked on √(x−2) < 3, giving 2 ≤ x < 11.",
      "This is a NEW example — it does not repeat the flipped video.",
    ],
    quickCheck: [
      "On whiteboards, 60 seconds: solve √(2x+3) = x, and check every candidate.",
      "Expected: candidates x = 3 and x = −1; only x = 3 survives, since √1 = 1 ≠ −1.",
      "80% correct → release guided practice. Below 80% → one further modelled example with two extraneous candidates.",
    ],
    guided: [
      "Two “Give it a go” problems, identical for every student, worked together with the teacher:",
      "(1) √(3x−2) = 4 — solve and verify.  (2) √(3x+1) = x−3 — solve, then check both candidates.",
      "Answers: x = 6 ; candidates x = 8 and x = 1, only x = 8 survives.",
      "Feedback: worked live on the board step by step; students self-mark and circle their OWN first error.",
    ],
    independent: [
      "Delivered through the “Choose Your Route” sheet with live feedback in Pear Deck. Routes are named for the task, not for the student.",
      "PRACTICE — Secure the method. Four single-candidate equations with substitution shown, two cube root equations, and one sentence on why checking still matters. Done when: every answer is substituted back and shown to work.",
      "APPLY — Use it in context. Three two-candidate equations, extraneous roots rejected with reasons, two inequalities with both conditions, one pendulum context. Done when: every rejected candidate has a reason written beside it.",
      "INVESTIGATE — Find out why. Why squaring creates but never loses solutions, constructing an equation whose only candidate is extraneous, and why cube roots do not produce them. Done when: you have an argument, not just an answer.",
      "Every student sits the same Mastery Gate. The gate is not differentiated, because it is the evidence.",
    ],
    production: [
      "Non-routine transfer task — this context has not appeared in practice.",
      "A science museum in Riyadh is installing a Foucault pendulum. The period T seconds of a pendulum of length L metres is T = 2π√(L/g), with g = 9.8 m/s². The designers need a period of exactly 6 seconds.",
      "(a) Rearrange the formula to make L the subject, showing every step. (b) Find the exact length for T = 6 s, then to two decimal places. (c) The atrium takes at most a 12 m cable — what is the longest achievable period? (d) Explain why doubling the length does not double the period.",
      "Answers: (a) L = gT²/(4π²). (b) 88.2/π² m ≈ 8.94 m. (c) T = 2π√(12/9.8) ≈ 6.95 s. (d) T is proportional to √L, so quadrupling L doubles T.",
      "Rearranging is HSA.CED.A.4 in disguise — name the standard when you set the task.",
    ],
    criteria: [
      "Minimum acceptable standard: the rearrangement justified step by step, the exact value given before the decimal, and part (d) argued from proportionality.",
      AI_CRITIC,
      "Completed independently by the student: the rearrangement in part (a) and the justification in part (d).",
    ],
    evidence: [
      "“Time to Check” — one individual task. No notes, no partner, no AI.",
      "1. Solve √(x+7) = x−5, showing every step. 2. Check BOTH candidates in the original equation and state which is extraneous. 3. In ONE sentence, explain why squaring both sides can create a solution that was never there.",
      "Answer: squaring gives x² − 11x + 18 = 0, candidates x = 9 and x = 2. Only x = 9 survives: √9 = 3 ≠ −3.",
      "Done when: the algebra is correct, BOTH candidates are substituted, and question 3 explains rather than restates. A correct value with no check does not pass question 2.",
      "Scored live in Pear Deck as submissions arrive; result logged in the Impact Dashboard Mastery Rate.",
    ],
    refinement: [
      "Students revise their pendulum reasoning using the AI critique and the teacher's micro-conference note.",
      "Final product, three equally acceptable formats: a Canva one-pager, a photographed hand-written solution, or a 45-second voice note.",
      "Required content: the solution as a chain of equivalent equations with each step justified; ONE worked non-example solved without checking, with the extraneous answer left in and a note on how to catch it; and a caption on why an engineer checks against the original problem.",
      "Graded on originality and clarity of reasoning, not correctness alone.",
    ],
    publication: [
      "Published to the class LMS portfolio; the strongest go on the Mathematics Department wall as the Topic 5 anchor set.",
      "Reflection question: “Which is still harder for you — the algebra of squaring, or remembering that the check is part of the method?”",
    ],
    differentiation: [
      "PRACTICE — Secure the method. Single-candidate equations with substitution shown, and two cube root equations; the five-step method stays on the board and a partner is allowed. Done when: every answer is substituted back and shown to work.",
      "APPLY — Use it in context. Two-candidate equations, inequalities with both conditions, and a pendulum application. Done when: every rejected candidate has a reason written beside it.",
      "INVESTIGATE — Find out why. Why squaring creates but never loses solutions, and why cube roots are immune. Done when: there is an argument, not just an answer.",
      "No student is labelled. The routes describe tasks; every student sits the same Mastery Gate.",
    ],
    adaptive: PILLAR_ADAPTIVE,
    saudi: [
      "Production context: a Foucault pendulum for a science museum in Riyadh — rearranging the period formula to find the cable length.",
      "In-class project: specifying the swing period of a shaded courtyard swing set against a safety standard.",
      "Discussion prompt: why an engineer substitutes an answer back into the original specification rather than trusting the algebra.",
    ],
    exams: [
      "SAT — Advanced Math: nonlinear equations in one variable and rearranging a formula, roughly 35% of the Mathematics section. Practice tip: on typed responses there are no options to check against, so verify your own answer.",
      "SAAT (Tahsili) — radical equations and rearranging formulae sit in the Grade 11 band, 30% of the mathematics items. Practice tip: extraneous roots are deliberately offered as distractors.",
      "GAT (Qudurat) — quick solution of simple root equations inside a word problem, about 75 seconds per question. Practice tip: substitute the options back; with four choices it is often faster than solving.",
    ],
  },

  plan2026: {
    day: "Sunday, Week 2", section: "Grade 11 — 11B",
    tools: "Quizizz (diagnostic) · Pear Deck (live practice feedback) · GeoGebra (comparing original and squared equations) · Canva (final product) · Whiteboards",
    resources: "Lesson presentation (18 slides) · “Choose Your Route” differentiation sheet · “Give It a Go” classwork · “The Museum Pendulum” project task · squared paper",
    competencies: ["Recognising when an algebraic step is not reversible.", "Verifying a result against the original problem rather than the working."],
    technology: ["Quizizz live diagnostic with instant gap analysis.", "GeoGebra: plotting the original pair and the squared pair to make the extra intersection visible."],
    reallife: ["A Foucault pendulum installation in a Riyadh science museum.", "Swing period against a safety standard in a school courtyard."],
    values: ["Honesty — reporting a candidate that failed, rather than hiding it.", "Precision in checking, not just in solving."],
    soft: ["Collaboration in assigned group roles.", "Explaining to a peer why an answer must be rejected."],
    hard: ["Solving radical equations and identifying extraneous solutions.", "Rearranging a formula; solving radical inequalities with both conditions."],
    phases: [
      "FIKR Phase 1 — Diagnose. 5-question Quizizz on simple radical solves and expanding a squared binomial. Results read as a gap map; students routed to the re-teach table, straight to modelling, or the Investigate prompt.",
      "FIKR Phase 2 — Targeted Instruction. Focused re-teach on expanding (x−1)². Whole class: the five-step method worked on √(x+5) = x−1, with both candidates checked; then the graph showing why the extraneous root appears; then radical inequalities with both conditions. Quick check on whiteboards.",
      "FIKR Phase 3 — Practice. Two identical “Give it a go” problems worked together. Students then choose a route on the “Choose Your Route” sheet and may switch at any time. Live feedback via Pear Deck; 2-minute micro-conferences.",
      "FIKR Phase 4 — Production. Museum pendulum: rearrange the period formula, find the exact cable length, work within a physical constraint, and explain the square root relationship. AI used as critic only.",
      "FIKR Phase 5 — Proof of Learning. “Time to Check” — solve an unseen radical equation and identify the extraneous candidate. No notes, no partner, no AI.",
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
    closure: "Two minutes of peer show-and-tell on the final products, then the reflection question: “Which is still harder for you — the algebra of squaring, or remembering that the check is part of the method?”",
    homework: "Finish the final product and upload to the LMS portfolio (any of the three formats). Practice set on Pear Deck — 14 questions, choose your route. Watch the flipped video for Lesson 5-5: Function Operations and Composition. Clinic group: bring your Time to Check paper.",
  },

  classwork: {
    subtitle: "Show all your working. Every candidate must be checked in the ORIGINAL equation — an unchecked answer is not an answer.",
    sections: [
      { h: "SECTION A — One candidate each", note: "Objective 1", lines: 4,
        intro: "Solve each equation. Substitute your answer back into the original equation and show that it works.",
        q: [
          { n: "Q1", eq: "s_ws1", t: "Solve and verify." },
          { n: "Q2", eq: "s_ws2", t: "Solve and verify." },
          { n: "Q3", eq: "s_ws3", t: "Solve and verify. Check the index." },
          { n: "Q4", eq: "s_ws4", t: "Solve and verify." },
        ] },
      { h: "SECTION B — Two candidates, one survivor", note: "Objective 2 · extraneous solutions", lines: 5,
        intro: "Each equation below produces two candidates. Check BOTH, and write a reason beside the one you reject.",
        q: [
          { n: "Q5", eq: "s_ws5", t: "Solve, then check both candidates." },
          { n: "Q6", eq: "s_ws6", t: "Solve, then check both candidates." },
        ] },
      { h: "SECTION C — Why it happens", note: "Objective 2 · MP.3", lines: 4,
        intro: "The graph below shows y = √(x+5) and y = x−1.",
        graph: "g_extraneous", graphW: 420,
        text: [
          "Q7.  How many times do the two graphs actually meet? At what value of x?",
          "Q8.  At x = −1 the curve is at 2 and the line is at −2. Explain, in one sentence, why squaring makes these look equal.",
          "Q9.  Complete this sentence: “An extraneous solution is created by ______________, and the only way to catch it is ______________.”",
        ] },
      { h: "SECTION D — Inequalities need two conditions", note: "Objective 3", lines: 4,
        q: [
          { n: "Q10", eq: "s_ws7", t: "Solve. State both conditions before you combine them." },
          { n: "Q11", eq: "s_ws8", t: "Solve. State both conditions before you combine them." },
        ],
        text: ["Q12.  A student solves √(x−2) < 3 and answers x < 11. Explain what they have forgotten, and give the correct answer."] },
    ],
  },

  diffSheet: {
    routes: [
      { note: "Solve and verify", done: "every answer is substituted back and shown to work.",
        intro: "Solve each equation, then substitute your answer into the ORIGINAL equation and show the check.",
        grid: [["1.", "s_ws1"], ["2.", "s_ws2"], ["3.", "s_ws3"], ["4.", "s_ws4"], ["5.", "s_g1"], ["6.", "s_g2"]],
        tasks: ["7.  Two of the equations above have a cube root rather than a square root. Say in one sentence why those two cannot produce an extraneous solution."],
        lines: 3 },
      { note: "Two candidates, inequalities, and one context", done: "every rejected candidate has a reason written beside it.",
        tasks: [
          ["1.  Solve   ", { eq: "s_ws5", k: 1.15 }, "   . Check both candidates and reject with a reason."],
          ["2.  Solve   ", { eq: "s_ws6", k: 1.15 }, "   . Check both candidates and reject with a reason."],
          ["3.  Solve   ", { eq: "s_ws7", k: 1.15 }, "   , stating both conditions before combining them."],
          ["4.  Solve   ", { eq: "s_ws8", k: 1.15 }, "   , stating both conditions before combining them."],
          "5.  A swing in a school courtyard has period T = 2π√(L/9.8) seconds. Safety requires a period of at least 3 seconds. Find the minimum chain length, exactly and then to two decimal places.",
        ], lines: 5 },
      { note: "Arguments, not answers", done: "you have an argument, not just an answer.",
        tasks: [
          "1.  Explain why squaring both sides can CREATE a solution but can never LOSE one. Refer to what squaring does to a negative number.",
          "2.  Construct a radical equation whose only candidate is extraneous — so the equation has no solution at all. Show that your example works.",
          "3.  Explain why cube root equations never produce extraneous solutions, while square root equations often do.",
        ], lines: 5 },
    ],
  },

  pbl: {
    title: "The Museum Pendulum", minutes: 20,
    subtitle: "A 20-minute group project. Work in fours. Every member signs the sheet. Exact values before decimals.",
    driving: "A museum wants a pendulum that swings with a period of exactly 6 seconds. How long must the cable be — and what happens when the building will not allow it?",
    situation: [
      "A science museum in Riyadh is installing a Foucault pendulum in its atrium, to demonstrate the rotation of the Earth. The period T in seconds of a pendulum of length L metres is given by the formula below, with g = 9.8 m/s².",
      "The exhibit designers have specified a period of exactly 6 seconds so that the swing is slow enough to watch. The atrium structure, however, can only carry a cable up to 12 metres long.",
    ],
    eq: "ctx_pend",
    steps: [
      ["1", "REARRANGE  (5 min)", "Make L the subject of the formula. Show every step, and name the operation you used at each one."],
      ["2", "THE DESIGN LENGTH  (4 min)", "Find the exact cable length needed for a 6-second period. Then give it to two decimal places."],
      ["3", "THE CONSTRAINT  (4 min)", "The atrium allows at most 12 m. What is the longest period actually achievable? Does the design specification survive?"],
      ["4", "THE SURPRISE  (4 min)", "The designers ask for a 12-second period instead. What length would that need? Explain why the answer is not simply double."],
      ["5", "PRESENT  (3 min)", "Prepare one sentence your presenter will say: what the square root does to the relationship between length and period."],
    ],
    working: [["Step 1 — the rearrangement, step by step:", 4], ["Step 2 — exact, then to 2 d.p.:", 3],
              ["Step 3 — longest achievable period, and the verdict:", 3], ["Step 4 — the length for 12 seconds, and why:", 3],
              ["Step 5 — our sentence:", 2]],
    roles: ["Algebraist — leads the rearrangement", "Calculator — finds the values", "Checker — substitutes back into the original formula", "Presenter — says the sentence"],
    doneWhen: ["The rearrangement is shown step by step, not stated.", "Every value is exact before it is rounded.", "Step 3 gives a clear verdict on the specification.", "Step 4 explains the factor of four."],
    materials: ["This sheet", "Scientific calculator", "A pencil", "The five-step method from the board"],
  },
};

(async () => {
  for (const cfg of [GR10_L2, GR11_L3, GR11_L4]) {
    console.log(cfg.slug);
    await buildAll(cfg);
  }
})();
