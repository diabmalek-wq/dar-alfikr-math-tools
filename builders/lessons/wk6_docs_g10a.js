// Week 6 · Gr10 · T2 L2-1 + L2-2 (taught as ONE lesson) Vertex and Standard Form — derived from lessons_g10q12.js.
const { ASSESS, T, AI_CRITIC, PILLAR_ADAPTIVE, WEEK_NOTE, PHASE_STD, STUB } = require("./wk6_common");

const GR10_L212 = {
  slug: "Wk6_Gr10_T2_L2-1-2_Vertex_and_Standard_Form",
  mathDocIndex: "math_wk6_doc/_index.json", graphIndex: "graphs_wk6/_index.json", timings: T,
  lessonTitle: "Vertex Form and Standard Form of a Quadratic Function",
  unit: "Topic 2 — Quadratic Functions and Equations · Lessons 2-1 and 2-2",
  gradeFull: "Grade 10 — Algebra II",
  week: "Week 6 · Semester 1, 2026–27", weekNum: "6",
  lessonLine: "Grade 10 · Algebra II · Topic 2: Quadratic Functions and Equations · Lessons 2-1 and 2-2 — Vertex Form and Standard Form",
  codes: ["HSF.IF.C.7.A", "HSF.IF.B.4", "HSF.BF.B.3", "HSA.CED.A.2", "HSA.REI.B.4", "HSA.REI.B.4.A", "HSF.IF.C.7", "HSS.ID.B.6.A"], mps: [],
  assessments: ASSESS,
  objectives: [
    "Graph quadratic functions given in vertex form.",
    "Write a quadratic function in vertex form given its key features.",
    "Write a quadratic function in standard form and analyze the significance of each term.",
    "Identify and explain the key features of quadratic functions in standard form.",
    "Graph quadratic functions using key features and symmetry to accurately represent their shape and position on the coordinate plane.",
  ],
  essentialQuestion: null,
  vocabList: "axis of symmetry ; maximum point ; maximum value ; minimum point ; minimum value ; parabola ; parent quadratic function ; quadratic function ; vertex ; vertex form ; constant term ; leading coefficient ; leading term ; linear coefficient ; linear term ; standard form (of a quadratic function)",

  plan: {
    outcome: [
      "Students will graph a function from vertex form using the vertex and symmetry (objective 1, Lesson 2-1) and write vertex form from a vertex and one other point (objective 2).",
      "Students will name the leading, linear and constant terms of standard form and say what each tells them, then find the axis, vertex and y-intercept and graph using symmetry (objectives 3–5, Lesson 2-2).",
      "Lessons 2-1 and 2-2 are taught as ONE lesson at the teacher’s request: four instruction slides and two vocabulary slides (16 terms).",
      "The curriculum map’s Essential Question and Math Practices columns for Topic 2 were not in the project text; they are left open, not invented.",
      WEEK_NOTE,
    ],
    preclass: [
      "Flipped video (4 min): “One parabola, two views” — expanding (x − 3)² and moving y = x² around the plane. Posted on the LMS 48 hours ahead.",
      "Two embedded EdPuzzle questions: one expansion, one horizontal shift.",
      "Evidence of readiness: EdPuzzle completion report plus both embedded answers submitted before the bell.",
    ],
    diagTool: [
      "5-question Quizizz (≤ 4 minutes) — the slide-5 warm-up: expand (x − 3)² ; f(x) = 2x² − 8x + 3, find f(0) ; how y = (x + 2)² − 5 moves from y = x² ; the axis of symmetry of y = x² ; the value halfway between x = 1 and x = 5.",
      "Cross-referenced against overnight EdPuzzle watch analytics — who watched, who skipped, who missed the embedded items.",
      "Answers: x² − 6x + 9 ; 3, the y-intercept ; left 2 and down 5 ; x = 0 ; x = 3 (anticipates the axis of symmetry).",
    ],
    diagGap: [
      "Expected gap 1 — expanding a squared bracket and describing a horizontal shift (questions 1 and 3); slow down on slide 8 if these fail.",
      "Expected gap 2 — Q5: the midpoint is the first sight of the axis of symmetry.",
      "Routing: 0–2 correct → re-teach expanding and transformations with the teacher.  3–4 → straight to vertex form.  5 → begin the Investigate prompt immediately.",
    ],
    instruction: [
      "Slide 7 — Vertex form: read the turning point (objective 1). f(x) = 2(x − 3)² − 1: vertex (3, −1), axis x = 3, opens up with minimum value −1. Symmetry: x = 2 and 4 give f = 1; x = 1 and 5 give f = 7. Say aloud: (x − 3) moves the graph RIGHT; the vertex is (h, k) with the sign of h flipped.",
      "Slide 8 — Writing vertex form from key features (objective 2). Vertex (−2, 5) and the point (0, −3): f(x) = a(x + 2)² + 5, then −3 = 4a + 5 gives a = −2, so f(x) = −2(x + 2)² + 5. Sense-check: it falls from 5 to −3, so a < 0.",
      "Slide 9 — Standard form: what each term tells you (objectives 3 and 4). ax² leading term, bx linear term, c constant term, f(0) = c. For x² − 6x + 5: a = 1, b = −6, c = 5; axis x = −b/(2a) = 3; vertex (3, −4). Say aloud: the sign of b is part of b, and the axis formula gives only the x-coordinate.",
      "Slide 10 — Graphing from standard form (objective 5). Direction, axis, vertex, y-intercept (0, 5) and its mirror (6, 5), then sketch. The same parabola is (x − 3)² − 4 — the bridge between the two forms. The zeros 1 and 5 are pointed out, not taught (factoring is Lesson 2-3).",
      "This is a NEW example — it does not repeat the flipped video.",
    ],
    quickCheck: [
      "On whiteboards, 60 seconds: state the vertex of f(x) = −3(x + 4)² + 7.",
      "Expected: (−4, 7); a = −3 so it opens down, maximum value 7. Watch for (4, 7).",
      "80% correct → release guided practice. Below 80% → one more modelled example, this time with a negative a.",
    ],
    guided: [
      "Two “Give it a go” problems, identical for every student, worked together with the teacher:",
      "(1) Vertex (1, −2), a = 3: write the function in vertex form and say whether it opens up or down.  (2) f(x) = 2x² + 8x − 3: name a, b and c, then find the y-intercept and the axis of symmetry.",
      "Answers: (1) f(x) = 3(x − 1)² − 2, opens up.  (2) a = 2, b = 8, c = −3; y-intercept (0, −3); axis x = −8/(2·2) = −2.",
      "Feedback: worked live on the board step by step; students self-mark and circle their OWN first error.",
    ],
    independent: [
      "Delivered through the “Choose Your Route” sheet with live feedback in Pear Deck. Routes are named for the task, not for the student.",
      "PRACTICE — Secure the method. Vertex, axis and direction from vertex form; vertex form written from a vertex; a, b, c, axis and vertex from x² − 4x + 3; a sketch on a grid. Done when: each vertex is an ordered pair with the sign of h checked, and your sketch is symmetric about the axis.",
      "APPLY — Use it in context. A function through (5, 7) with vertex (3, −1); a graph of −x² + 4x + 1 with its mirror point; fountain data (0, 1), (2, 5), (4, 1) fitted and checked. Done when: your function is checked by substituting a point, and every answer carries a sentence in context.",
      "INVESTIGATE — Find out why. Expanding vertex form to prove b = −2ah; why the y-intercept is ah² + k; and the sign error in reading y = (x + 3)² − 4. Done when: you have an argument grounded in expanding or in the graph, not just a computed answer.",
      "Every student sits the same Mastery Gate. The gate is not differentiated, because it is the evidence.",
    ],
    production: [
      "Non-routine transfer task — this context has not appeared in practice (slide 14).",
      "A water jet in a Jeddah Corniche park leaves the nozzle 1 m above the ground and reaches its highest point, 5 m, when 2 m away horizontally (an invented classroom model).",
      "(a) Write h(x) in vertex form using the vertex (2, 5) and the point (0, 1). (b) Expand to standard form; name a, b, c and say what c means. (c) Use −b/(2a) to confirm the axis. (d) Find where the jet lands, to one decimal place.",
      "Answers: (a) 4a + 5 = 1 gives a = −1, so h(x) = −(x − 2)² + 5. (b) h(x) = −x² + 4x + 1; a = −1, b = 4, c = 1; c is the nozzle height, 1 m. (c) −4/(2·(−1)) = 2. (d) −(x − 2)² + 5 = 0 gives x = 2 + √5 ≈ 4.2 m.",
      "Students then hand their reasoning to the AI critic and ask it to challenge any step they have not justified.",
    ],
    criteria: [
      "Minimum acceptable standard: the vertex substituted before the point, exact expressions before decimals, and units (metres) in every answer.",
      AI_CRITIC,
      "Completed independently by the student: the written justification for parts (a)–(d). AI may challenge it; it may not write it.",
    ],
    evidence: [
      "“Time to Check” — one individual task. No notes, no partner, no AI.",
      "1. Write the vertex form of the function with vertex (−1, 4) through (1, 0). 2. For f(x) = x² + 6x + 5 state c, the axis and the vertex. 3. In ONE sentence, say how you read the vertex in each of the two forms.",
      "Answers: 1. 4a + 4 = 0 gives a = −1: f(x) = −(x + 1)² + 4. 2. c = 5; axis x = −3; vertex (−3, −4). 3. Vertex form: read (h, k) with the sign of h flipped. Standard form: x = −b/(2a), then substitute.",
      "Done when: answers are exact and question 3 is a sentence about the two forms, not an example.",
      "Scored live in Pear Deck as submissions arrive; result logged in the Impact Dashboard Mastery Rate.",
    ],
    refinement: [
      "Students revise their fountain reasoning using the AI critique and the teacher’s micro-conference note.",
      "Final product, three equally acceptable formats: a Canva one-pager, a photographed hand-written solution, or a 45-second voice note.",
      "Required content: the fountain function in both forms, the axis check, and the landing point; ONE worked non-example — reading the vertex of y = (x + 3)² − 4 as (3, −4) — with a sentence on what point that wrong answer actually is; and a caption on why a park designer wants the highest point of a jet.",
      "Graded on originality and clarity of reasoning, not correctness alone.",
    ],
    publication: [
      "Published to the class LMS portfolio; the strongest go on the Mathematics Department wall as the Topic 2 modelling set.",
      "Reflection question: “Which is harder for you — reading a feature from vertex form, or from standard form?”",
    ],
    differentiation: [
      "PRACTICE — Secure the method. Features from vertex form, vertex form from a vertex, a, b, c and the axis from standard form, and a symmetric sketch. Done when: each vertex has the sign of h checked.",
      "APPLY — Use it in context. A function from its vertex and a point, graphing −x² + 4x + 1, and fitting the fountain data. Done when: the function is checked by substituting a point.",
      "INVESTIGATE — Find out why. Proving b = −2ah, the y-intercept ah² + k, and the sign error in (x + 3)² − 4. Done when: the argument rests on expanding or on the graph.",
      "No student is labelled. The routes describe tasks; every student sits the same Mastery Gate.",
    ],
    adaptive: PILLAR_ADAPTIVE,
    saudi: [
      "Production and project context: a water jet in a Jeddah Corniche park (invented model), modelled in both forms and compared with a second jet in the A3 task.",
      "Apply-route item: fountain-jet data (0, 1), (2, 5), (4, 1) fitted with a vertex-form function.",
      "Discussion prompt: why a park designer cares about the highest point and the landing point of a jet.",
    ],
    exams: [
      "SAAT (Tahsili) — minimum value of x² − 4x + 7 is 3 (axis x = 2, then substitute). No calculator. Name the trap: reading c = 7 as the minimum.",
      "SAT — Advanced Math: vertex (3, −2) through (5, 6) gives y = 2(x − 3)² − 2. Name the trap: flipping the sign of h.",
      "GAT (Qudurat) — least value of x² − 6x + 10 against 1: rewrite as (x − 3)² + 1, so they are equal. About 75 seconds, no calculator.",
    ],
  },

  plan2026: {
    day: "Week 6 · day per timetable", section: "Grade 10 — 10A and 10C",
    tools: "Quizizz (diagnostic) · Pear Deck (live practice feedback) · GeoGebra Graphing Calculator · Canva (final product) · Whiteboards",
    resources: "Lesson presentation (20 slides) · “Choose Your Route” differentiation sheet · “Two Jets, One Pond” project task (A3) · squared paper",
    competencies: ["Reading the vertex, axis and direction from vertex form and from standard form.", "Writing vertex form from a vertex and one point, and expanding it to standard form."],
    technology: ["Quizizz live diagnostic with instant gap analysis.", "GeoGebra sliders on a, h and k in f(x) = a(x − h)² + k, compared with a x² + b x + c."],
    reallife: ["A fountain jet in a Jeddah Corniche park, modelled as a parabola.", "Choosing a jet that lands inside a pond."],
    values: ["Precision — reading h with its sign flipped.", "Design thinking — using the highest point of a path to plan a space."],
    soft: ["Collaboration in assigned group roles.", "Explaining why two forms describe the same parabola."],
    hard: ["Graphing a parabola from vertex form and from standard form.", "Writing vertex form from key features."],
    phases: [
      "FIKR Phase 1 — Diagnose. 5-question Quizizz: expand a square, f(0), a shift, the axis of y = x², a midpoint. Gap map; routed to re-teach, vertex form, or Investigate.",
      "FIKR Phase 2 — Targeted Instruction. Re-teach expanding and shifts (flagged). Whole class: vertex form; vertex form from a vertex and a point; the terms of standard form; graphing from standard form. Whiteboard check.",
      "FIKR Phase 3 — Practice. Two identical “Give it a go” problems; then students choose a route (switching allowed). Pear Deck feedback; 2-minute micro-conferences.",
      "FIKR Phase 4 — Production. The fountain jet: vertex form, standard form, the axis check and the landing point. AI used as critic only. Extended in the A3 project task.",
      "FIKR Phase 5 — Proof of Learning. “Time to Check”: vertex form from a vertex and point; c, axis, vertex; a sentence on the two forms. No notes, partner or AI.",
      "FIKR Phase 6 — Smart Production. Final product with one worked non-example, published to the LMS portfolio.",
    ],
    assessment: PHASE_STD.assessment,
    closure: "Two minutes of peer show-and-tell on the final products, then the reflection question: “Which is harder for you — reading a feature from vertex form, or from standard form?”",
    homework: "Finish the final product and upload to the LMS portfolio (any of the three formats). Practice set on Pear Deck — 12 questions, choose your route. Watch the flipped video for the next lesson, Topic 2 · Lesson 2-3 — Factored Form. Clinic group: bring your Time to Check paper.",
  },

  classwork: STUB("k_q1"),

  diffSheet: {
    routes: [
      { note: "Read it, write it, sketch it", done: "each vertex is written as an ordered pair with the sign of h checked, and your sketch is symmetric about the axis.",
        intro: "Items 1–3: state the vertex, the axis of symmetry and whether the parabola opens up or down. Items 4–5: write the function in vertex form. Item 6: name a, b and c, then give the y-intercept, the axis and the vertex.",
        grid: [["1.", "k_q1"], ["2.", "k_q2"], ["3.", "k_q3"], ["4.", "k_q4"], ["5.", "k_q5"], ["6.", "k_q6"]],
        tasks: [
          "7.  Sketch f(x) = 3(x − 5)² − 2 using symmetry: plot the vertex, then the points one step either side.",
          { graph: "k_grid", w: 270 },
        ], lines: 2 },
      { note: "Fit it, graph it, test it", done: "your function is checked by substituting a point, and every answer carries a sentence in context.",
        tasks: [
          "1.  Write the function with vertex (3, −1) that passes through (5, 7).",
          "2.  Graph f(x) = −x² + 4x + 1: find a, b, c, the axis, the vertex and the y-intercept with its mirror point.",
          { graph: "k_grid", w: 235 },
          "3.  A fountain jet passes through (0, 1), (2, 5) and (4, 1), measured in metres. Fit a vertex-form function and check it with a fourth point of your own. Say in one sentence what the vertex means for the jet.",
        ], lines: 3 },
      { note: "Arguments, not answers", done: "you have an argument grounded in expanding or in the graph, not just a computed answer.",
        tasks: [
          ["1.  Expand ", { eq: "k_qform", k: 0.9 }, ". Show that b = −2ah, so h = −b/(2a)."],
          "2.  Explain why the y-intercept of vertex form is ah² + k, and check it with f(x) = 2(x − 3)² − 1.",
          "3.  A student says the vertex of y = (x + 3)² − 4 is (3, −4). Explain the error using the graph, and give the true vertex.",
        ], lines: 4 },
    ],
  },

  pbl: {
    title: "Two Jets, One Pond", minutes: 20,
    subtitle: "A 20-minute group project. Work in fours. Every member signs the sheet.",
    driving: "A park has two fountain jets and a pond whose far edge is 5 m from the nozzles. Which jet stays inside the pond — and how can the two forms of a quadratic tell you without drawing it?",
    situation: [
      "Jet 1 leaves a nozzle 1 m above the ground and peaks at 5 m when 2 m away horizontally: vertex (2, 5), through (0, 1).",
      "Jet 2 leaves ground level and peaks at 6 m when 3 m away horizontally: vertex (3, 6), through (0, 0).",
      "This is an invented classroom model; heights and distances are in metres.",
    ],
    eq: "k_qj",
    steps: [
      ["1", "VERTEX FORM  (4 min)", "Jet 1 is given above. Write Jet 2 in vertex form using its vertex and the point (0, 0). Find a and check by substitution."],
      ["2", "STANDARD FORM  (4 min)", "Expand both functions. Name a, b and c for each and say what c means for the nozzle."],
      ["3", "CHECK BY SYMMETRY  (4 min)", "Use −b/(2a) to confirm each axis. For Jet 1 find the mirror image of the nozzle point (0, 1) and check it lies on the curve."],
      ["4", "LANDING POINTS  (5 min)", "Find where each jet lands (height 0). Give Jet 1 as an exact value and then to one decimal place."],
      ["5", "PRESENT  (3 min)", "One sentence: which jet stays inside a pond whose far edge is 5 m from the nozzle, and how do you know?"],
    ],
    working: [["Step 1 — Jet 2 in vertex form:", 3], ["Step 2 — both in standard form:", 4],
              ["Step 3 — axes and the mirror point:", 3], ["Step 4 — landing points, exact then decimal:", 4],
              ["Step 5 — our sentence:", 2]],
    roles: ["Reader — states the two jets", "Calculator — expands both forms", "Checker — substitutes a point into each function", "Presenter — says the sentence"],
    doneWhen: ["Each function is checked by substituting a known point.", "Exact values are written before decimals.", "Units (metres) appear in every answer.", "Your sentence makes sense to someone who does not study maths."],
    materials: ["This sheet", "Squared paper", "A pencil and ruler", "A calculator"],
  },
};
module.exports = { GR10_L212 };
