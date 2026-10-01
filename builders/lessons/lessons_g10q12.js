// Grade 10 · Topic 2 · Lessons 2-1 and 2-2 taught as ONE lesson —
// Vertex Form and Standard Form of a Quadratic Function.
// Objectives (2 + 3), vocabulary (10 + 6) and standards are quoted from the curriculum map.
// The map's Essential Question and Math Practices columns for Topic 2 were not available in the
// project text, so they are NOT shown and NOT invented — add them when confirmed.
const { build } = require("./lesson_engine");

const CFG = {
  out: "Gr10_T2_L2-1-2_Vertex_and_Standard_Form.pptx",
  deckTitle: "Vertex Form and Standard Form of a Quadratic Function — Grade 10 Algebra II",
  mathIndex: "math_g10q12/_index.json", graphIndex: "graphs_g10q12/_index.json",
  topicLine: "TOPIC 2 · QUADRATIC FUNCTIONS AND EQUATIONS · LESSONS 2-1 AND 2-2",
  lessonTitle: "Vertex Form and Standard Form of a Quadratic Function", titleSize: 30,
  subtitle: "One parabola, two views — the turning point and the starting point",
  titleEq: "b_title_w", titleEqK: 2.4,
  titleEqAlt: "a times x minus h squared plus k, and a x squared plus b x plus c: the two forms of a quadratic function",
  grade: "Grade 10", week: "Week 6 · Semester 1, 2026–27",
  footerLeft: "Grade 10 · Algebra II · Topic 2 · Lessons 2-1 and 2-2",
  lessonRef: "Lessons 2-1 and 2-2 — Vertex Form and Standard Form",
  nextLesson: "Topic 2 · Lesson 2-3 — Factored Form of a Quadratic Function",
  codes: ["HSF.IF.C.7.A", "HSF.IF.B.4", "HSF.BF.B.3", "HSA.CED.A.2", "HSA.REI.B.4", "HSA.REI.B.4.A", "HSF.IF.C.7", "HSS.ID.B.6.A"],
  mps: [],
  assessments: ["“Give it a go” questions", "“Time to Check”"],

  objectives: [
    "Graph quadratic functions given in vertex form.",
    "Write a quadratic function in vertex form given its key features.",
    "Write a quadratic function in standard form and analyze the significance of each term.",
    "Identify and explain the key features of quadratic functions in standard form.",
    "Graph quadratic functions using key features and symmetry to accurately represent their shape and position on the coordinate plane.",
  ],
  essentialQuestion: null,
  objectivesSub: "Lesson 2-1 (objectives 1–2) and Lesson 2-2 (objectives 3–5), quoted from the curriculum map",

  vocabulary: [
    { term: "axis of symmetry", def: "The vertical line x = h through the vertex. It splits the parabola into two mirror-image halves." },
    { term: "maximum point", def: "The vertex when the parabola opens downward: the highest point on the graph." },
    { term: "maximum value", def: "The y-coordinate of the maximum point: the greatest output of the function." },
    { term: "minimum point", def: "The vertex when the parabola opens upward: the lowest point on the graph." },
    { term: "minimum value", def: "The y-coordinate of the minimum point: the least output of the function." },
    { term: "Parabola", def: "The U-shaped curve that is the graph of a quadratic function." },
    { term: "parent quadratic function", def: "f(x) = x^{2}: the simplest quadratic, with vertex (0, 0). Every other quadratic is a transformation of it." },
    { term: "quadratic function", def: "A function that can be written f(x) = ax^{2} + bx + c with a ≠ 0." },
    { term: "Vertex", def: "The turning point of the parabola: its highest or lowest point." },
    { term: "vertex form", def: "f(x) = a(x − h)^{2} + k. The vertex is (h, k) and the axis of symmetry is x = h." },
    { term: "constant term", def: "The term c with no variable. Since f(0) = c, it gives the y-intercept (0, c)." },
    { term: "leading coefficient", def: "The coefficient a of x^{2}. It decides whether the parabola opens up or down, and how wide it is." },
    { term: "leading term", def: "The term ax^{2}, which has the highest power of x." },
    { term: "linear coefficient", def: "The coefficient b of x." },
    { term: "linear term", def: "The term bx." },
    { term: "standard form (of a quadratic function)", def: "f(x) = ax^{2} + bx + c with a ≠ 0." },
  ],
  vocabSub: "All sixteen terms the curriculum map lists for Lessons 2-1 and 2-2",

  prior: [
    { h: "Lesson 1-2: transformations", eq: "b_p1", d: "Replacing x by x + 2 moves a graph left 2; subtracting 5 moves it down 5." },
    { h: "Lesson 1-1: key features", eq: "b_p2", d: "Intercepts, domain and range, and where a function increases or decreases." },
    { h: "Multiplying binomials", eq: "b_p3", d: "Expanding a squared bracket is the bridge between our two forms today." },
  ],
  priorSub: "Three things you already know — today joins them into one picture",
  carryOver: "Vertex form shows where the parabola turns; standard form shows where it starts. They are the same function, so every feature you read in one form can be found in the other.",
  carryOverEq: "b_co_w",

  diagnose: {
    title: "Warm-Up: Two Ways to Write the Same Curve",
    sub: "Answer on Quizizz — 5 questions, 4 minutes. This builds a gap map, not a grade.",
    questions: [
      { eq: "b_d1", t: "Expand the square." },
      { eq: "b_d2", t: "Evaluate at x = 0. What does this value tell you about the graph?" },
      { eq: "b_d3", t: "Starting from y = x^{2}, how far left or right, and up or down, is this graph moved?" },
      { eq: "b_d4", t: "Complete the sentence." },
      { eq: "b_d5", t: "Where does x = 3 sit compared with x = 1 and x = 5?" },
    ],
    routing: "0–2 correct → re-teach expanding and transformations with me.      3–4 correct → straight to vertex form.      5 correct → start the Investigate prompt now.",
  },

  instruction: [
    {
      title: "Vertex Form: Read the Turning Point",
      sub: "Lesson 2-1, objective 1 — graph f(x) = a(x − h)^{2} + k from its vertex and symmetry",
      graph: "g_vertex", graphW: 5.6, graphX: 0.45, graphY: 2.45,
      graphAlt: "Parabola f of x equals 2 times x minus 3 squared minus 1 with vertex 3 comma minus 1, axis of symmetry x equals 3, and points 2 comma 1, 4 comma 1, 1 comma 7 and 5 comma 7",
      panel: {
        h: "READ IT THIS WAY: f(x) = a(x − h)^{2} + k",
        items: [
          "Vertex (h, k) and axis of symmetry x = h: read h with the OPPOSITE sign.",
          "a > 0 opens up (minimum value k); a < 0 opens down (maximum value k).",
          "|a| > 1 makes the parabola narrower; |a| < 1 makes it wider.",
          "Plot the vertex, then use symmetry: one step each side is a above the vertex; two steps is 4a.",
          "Here a = 2: from (3, −1) the points (2, 1), (4, 1) and (1, 7), (5, 7).",
        ],
        fs: 12,
      },
      panelX: 6.3, panelY: 2.5, panelW: 6.6, panelH: 3.75,
      bar: ["SIGN WATCH", "(x − 3) moves the graph RIGHT 3 and (x + 3) moves it LEFT 3 — the vertex is (h, k), so the sign inside the bracket is flipped."],
      barY: 6.32,
      notes: "f(x)=2(x-3)^2-1: vertex (3,-1), axis x=3, opens up (a=2>0), minimum value -1. Symmetry: x=2 and x=4 are one step from the axis, f=2(1)^2-1=1; x=1 and x=5 are two steps, f=2(4)-1=7. y-intercept f(0)=2(9)-1=17 (off the graph). Link to Lesson 1-2: this is y=x^2 stretched by 2, moved right 3 and down 1 (HSF.BF.B.3). Misconceptions to say aloud: (1) (x-3) moves LEFT; (2) the vertex is (h,k) with the sign of h flipped; (3) a=2 stretches the shape vertically -- the points are 2 and 8 above the vertex, not 2 steps wide.",
    },
    {
      title: "Writing Vertex Form from Key Features",
      sub: "Lesson 2-1, objective 2 — a vertex and one more point give the whole function",
      panel: {
        h: "WATCH MY THINKING",
        items: [
          "Given: vertex (−2, 5) and the point (0, −3).",
          "Put the vertex in first: f(x) = a(x + 2)^{2} + 5. Only a is unknown.",
          "Substitute the point to find a — then write the function.",
          "Sense-check: the graph must fall from 5 down to −3, so it opens DOWN and a is negative.",
          "Check by substituting the point back: f(0) = −2(4) + 5 = −3 ✓",
        ],
        fs: 12,
      },
      panelX: 0.45, panelY: 2.5, panelW: 5.8, panelH: 3.75,
      rowsHead: ["STEP", "WORK"],
      rowsTop: 2.5, rowH: 0.8, rowsX: 6.5, rowsW: 6.4,
      rows: [
        ["Substitute the vertex", { eq: "b_w1", k: 1.5 }],
        ["Substitute the point", { eq: "b_w2", k: 1.5 }],
        ["Solve for a", { eq: "b_w3", k: 1.5 }],
        ["Write the function", { eq: "b_w4", k: 1.5 }],
      ],
      bar: ["THE PATTERN", "vertex gives h and k; one other point gives a. Substitute the vertex FIRST, then the point."],
      barY: 6.32,
      notes: "Vertex (-2,5): h=-2 so the bracket is (x+2); k=5. Point (0,-3): -3=a(0+2)^2+5 -> -8=4a -> a=-2. f(x)=-2(x+2)^2+5. Maximum value 5 at x=-2. Misconceptions: writing (x-2) for h=-2; substituting the point into the wrong place; forgetting to square before multiplying by a (a(x+2)^2 means a times the square).",
    },
    {
      title: "Standard Form: What Each Term Tells You",
      sub: "Lesson 2-2, objectives 3 and 4 — f(x) = ax^{2} + bx + c",
      panel: {
        h: "THE THREE TERMS OF f(x) = ax^{2} + bx + c",
        items: [
          "ax^{2} is the leading term, a the leading coefficient: it sets the direction and width.",
          "bx is the linear term, b the linear coefficient: with a it places the axis of symmetry.",
          "c is the constant term: f(0) = c, so the graph crosses the y-axis at (0, c).",
          "Example f(x) = x^{2} − 6x + 5: a = 1, b = −6, c = 5. Opens up; y-intercept (0, 5).",
        ],
        fs: 12,
      },
      panelX: 0.45, panelY: 2.5, panelW: 5.9, panelH: 3.75,
      rowsHead: ["FEATURE", "HOW TO FIND IT"],
      rowsTop: 2.4, rowH: 0.66, rowsX: 6.6, rowsW: 6.3, rowsCw: [2.0, 4.3],
      rows: [
        ["Direction", "a > 0 opens up; a < 0 opens down"],
        ["y-intercept", "(0, c), because f(0) = c"],
        ["Axis of symmetry", { eq: "b_axis", k: 1.3 }],
        ["Vertex", { eq: "b_vtx", k: 1.0 }],
        ["Max or min value", "the y-coordinate of the vertex"],
      ],
      bar: ["WHY IT WORKS", "the axis sits halfway between a point and its mirror image — and the y-intercept (0, c) always has a mirror image across x = −b/(2a)."],
      barY: 6.32,
      notes: "Terms: leading term ax^2, leading coefficient a, linear term bx, linear coefficient b, constant term c. f(x)=x^2-6x+5: a=1,b=-6,c=5; axis x=-(-6)/(2*1)=3; vertex f(3)=9-18+5=-4 -> (3,-4). Misconceptions to say aloud: (1) the sign of b is part of b (b=-6, not 6); (2) the y-intercept is c, not b; (3) the axis formula gives only the x-coordinate -- substitute to get the y-coordinate. Walk the 'why' bar after the next slide.",
    },
    {
      title: "Graphing from Standard Form",
      sub: "Lesson 2-2, objective 5 — use key features and symmetry to place the parabola accurately",
      graph: "g_std", graphW: 5.0, graphX: 0.45, graphY: 2.5,
      graphAlt: "Parabola f of x equals x squared minus 6x plus 5 with vertex 3 comma minus 4, y-intercept 0 comma 5, its mirror point 6 comma 5, zeros at 1 and 5, and axis of symmetry x equals 3",
      rowsHead: ["STEP", "WORK"],
      rowsTop: 2.42, rowH: 0.7, rowsX: 5.7, rowsW: 7.2, rowsCw: [2.2, 5.0],
      rows: [
        ["1 Direction", "a = 1 > 0: opens up, minimum at the vertex"],
        ["2 Axis of symmetry", { eq: "b_s2", k: 1.3 }],
        ["3 Vertex", { eq: "b_s3", k: 1.3 }],
        ["4 Intercept and mirror", { eq: "b_s4", k: 1.3 }],
        ["5 Sketch", "plot all points, join with a smooth curve, label"],
      ],
      bar: ["TWO VIEWS, ONE PARABOLA", "f(x) = x^{2} − 6x + 5 = (x − 3)^{2} − 4. Vertex form shows (3, −4) at once; standard form shows the y-intercept at once."],
      barY: 6.32,
      notes: "Steps: a=1>0 up; axis x=3; vertex (3,-4); y-intercept (0,5) and its mirror (6,5); also the graph crosses the x-axis at 1 and 5 (factoring comes next lesson -- point it out, do not teach it). Check equivalence: (x-3)^2-4 = x^2-6x+9-4 = x^2-6x+5. This is the bridge between the two forms. Misconception: plotting the intercept but forgetting its mirror image.",
    },
  ],

  quickCheck: {
    lead: "State the vertex", leadW: 2.9,
    eq: "b_qc", k: 2.0,
    think: "Read h with the opposite sign: the bracket is (x + 4), so h = −4. Then read k.",
    rule: "80% correct → straight to guided practice.   Below 80% → one more modelled example, this time with a negative a.",
  },

  guided: {
    mins: 4,
    items: [
      { eq: "b_g1", t: "Write the function in vertex form, then say whether it opens up or down.", hint: "Put the vertex in the bracket; a is given." },
      { eq: "b_g2", t: "Name a, b and c, then find the y-intercept and the axis of symmetry.", hint: "Axis: −b over 2a. Intercept: the constant term." },
    ],
  },

  routes: {
    mins: 8,
    tiers: [
      { items: ["State the vertex, the axis and the direction of f(x) = 3(x − 5)^{2} − 2 and of g(x) = −2(x + 1)^{2} + 6.", "Write the vertex form with vertex (2, −3) and a = 1; then with vertex (−1, 4) through (0, 2).", "For f(x) = x^{2} − 4x + 3 name a, b, c, the y-intercept, the axis (x = 2) and the vertex.", "Sketch f(x) = 3(x − 5)^{2} − 2 using symmetry."],
        help: "You may use: the key-features table on the board, and a partner.",
        done: "each vertex is written as an ordered pair with the sign of h checked, and your sketch is symmetric about the axis.", eq: "b_ws1" },
      { items: ["Write the function with vertex (3, −1) that passes through (5, 7).", "Graph f(x) = −x^{2} + 4x + 1: find a, b, c, the axis, the vertex and the y-intercept with its mirror.", "Data: (0, 1), (2, 5), (4, 1). A fountain jet passes through these points. Fit a vertex-form function and check it with a fourth point of your own."],
        help: "You may use: the worked example, and the sentence frames.",
        done: "your function is checked by substituting a point, and every answer carries a sentence in context.", eq: "b_ws3" },
      { items: ["Expand f(x) = a(x − h)^{2} + k and show that b = −2ah, so h = −b over 2a.", "Explain why the y-intercept of vertex form is ah^{2} + k, and check it with f(x) = 2(x − 3)^{2} − 1.", "A student says the vertex of y = (x + 3)^{2} − 4 is (3, −4). Explain the error using the graph."],
        help: "You may use: nothing but your reasoning.",
        done: "you have an argument grounded in expanding or in the graph, not just a computed answer.", eq: null },
    ],
  },

  production: {
    title: "How High Does the Fountain Jet Reach?",
    sub: "A context you have not seen before — this tests transfer",
    situation: "A water jet in a Jeddah Corniche park leaves the nozzle 1 m above the ground. It reaches its highest point, 5 m, when it is 2 m away horizontally. This is an invented classroom model.",
    eq: "b_model_w", eqK: 2.2,
    tasks: [
      "(a)  Write the jet's height h(x) in vertex form using the vertex (2, 5) and the point (0, 1).",
      "(b)  Expand to standard form. Name a, b and c and say what c means for the fountain.",
      "(c)  Use −b over 2a to confirm the axis of symmetry.",
      "(d)  Using technology, find where the jet lands (height 0), to one decimal place.",
    ],
    note: "Exact expressions before any decimal; units named (metres); the vertex form checked against the nozzle point.",
    aiPrompt: "“Check whether my vertex form and my standard form describe the same parabola, and challenge any step I have not justified.”",
  },

  geogebra: {
    sub: "Slide a, h and k — watch the vertex and the shape move",
    preview: "g_vertex",
    previewAlt: "Parabola f of x equals 2 times x minus 3 squared minus 1 with its vertex and axis of symmetry",
    url: "https://www.geogebra.org/graphing",
    steps: [
      "Open the link (any browser, no sign-in needed).",
      "Type a = 1, h = 0 and k = 0 and click each slider button.",
      "Type f(x) = a(x − h)^(2) + k, then V = (h, k).",
      "Type g(x) = a x^(2) + b x + c with sliders b and c, and compare.",
    ],
    explore: "Which slider moves the vertex? Which changes the opening? Make f pass through (0, 1) with vertex (2, 5).",
  },

  gate: {
    eq: "b_gate_w",
    items: [
      { t: "Write the vertex form of the function described.", eq: "b_gate_w" },
      { t: "For f(x) = x^{2} + 6x + 5 state c, the axis and the vertex.", eq: null },
      { t: "In ONE sentence, say how you read the vertex in each of the two forms.", eq: null },
    ],
    footer: "Exact answers only. Question 3 is a sentence about the two forms, not an example.",
    routing: "PASS → Enrichment & Challenge (convert between the two forms and compare their features).      NOT YET → Targeted Learning Clinic on reading h with its sign, start of next lesson.",
  },

  smart: {
    steps: [
      { h: "Show the model", d: "Present the fountain function in both forms, the axis check, and the landing point." },
      { h: "Expose the trap", d: "Add one worked NON-example — reading the vertex of y = (x + 3)^{2} − 4 as (3, −4) — and say what point that wrong answer actually is." },
      { h: "Say why it matters", d: "One caption — “why a park designer wants the highest point of a jet” — for a non-maths reader." },
    ],
    published: "the class LMS portfolio; the strongest go on the Department wall as our Topic 2 modelling set.",
    reflection: "which is harder for you — reading a feature from vertex form, or from standard form?",
  },

  exams: [
    { code: "SAAT", full: "Tahsili — Achievement Test", skill: "Minimum value of a quadratic from standard form, no calculator.",
      question: "Minimum value of f(x) = x^{2} − 4x + 7?   (A) 3   (B) 7   (C) 2   (D) 11",
      steps: ["Axis: x = −(−4) over 2(1) = 2.", "f(2) = 4 − 8 + 7 = 3.", "Answer (A)."],
      trap: "(B) reads c; (C) gives the axis, not the value; (D) adds 4 and 7, using the size of b instead of the vertex." },
    { code: "SAT", full: "College Board — Advanced Math", skill: "Write a parabola's equation from its vertex and a point.",
      question: "Vertex (3, −2), through (5, 6). Which equation?   (A) y = 2(x − 3)^{2} − 2   (B) y = 2(x + 3)^{2} − 2   (C) y = 4(x − 3)^{2} − 2   (D) y = (x − 3)^{2} + 6",
      steps: ["y = a(x − 3)^{2} − 2.", "6 = a(2)^{2} − 2, so 4a = 8 and a = 2.", "Answer (A)."],
      trap: "(B) flips the sign of h; (C) forgets to square the 2; (D) mixes up the point." },
    { code: "GAT", full: "Qudurat — Quantitative Comparison", skill: "Find a minimum value by rewriting a quadratic as a square plus a constant.",
      question: "A = least value of x^{2} − 6x + 10 and B = 1.   (A) A greater   (B) B greater   (C) equal   (D) cannot tell",
      steps: ["x^{2} − 6x + 10 = (x − 3)^{2} + 1.", "A square is at least 0, so the least value is 1.", "A = B: answer (C)."],
      trap: "Reading c = 10 as the least value, or assuming the least value is 0." },
  ],
  examBar: ["THE SINGLE MOST EXAMINED IDEA HERE:", "the vertex gives the maximum or minimum value — find it by reading vertex form, or by x = −b over 2a and substituting."],

  summary: [
    "Graph a quadratic function from vertex form using the vertex and symmetry.",
    "Write a quadratic function in vertex form from its vertex and one more point.",
    "Name the leading term, linear term and constant term of standard form and say what each tells you.",
    "Find the axis, vertex and y-intercept from standard form, and use them to graph.",
    "Move between the two forms, knowing they describe the same parabola.",
  ],
  homework: [
    "Finish your product and upload it to the LMS portfolio — any of the three formats.",
    "Practice set on Pear Deck: 12 questions, choose your route.",
    "Watch the flipped video for our next lesson, Topic 2 · Lesson 2-3 — Factored Form (4 min, 2 embedded questions).",
    "Clinic group: bring your Time to Check paper — we start with 10 minutes on reading vertex form.",
  ],

  notes: {
    cover: "Week 6 lesson for 10A and 10C. Lessons 2-1 (Vertex Form) and 2-2 (Standard Form) are taught as ONE lesson at your request, so the deck has four instruction slides and two vocabulary slides (16 terms). If time runs short, cut Smart Production and carry it over, never the Mastery Gate. The map's Essential Question and Math Practices columns for these lessons were not in the project text; they are left off the objectives slide rather than invented. Standards from the map: HSF.IF.C.7.A, IF.B.4, BF.B.3, CED.A.2, REI.B.4, REI.B.4.A, IF.C.7, ID.B.6.A.",
    objectives: "The five objectives are quoted from the map: the first two are Lesson 2-1, the last three are Lesson 2-2.",
    vocabulary: "Sixteen terms across two slides: ten from Lesson 2-1 and six from Lesson 2-2. Definitions are written for this lesson; ask students to restate two in their own words.",
    prior: "If students cannot expand (x - 3)^2 or describe a horizontal shift, slow down on slide 8. Watch diagnostic questions 1 and 3.",
    diagnose: "Answers: (x-3)^2 = x^2-6x+9; f(0)=3, the y-intercept; y=(x+2)^2-5 is left 2 and down 5; axis x=0; x=3 is halfway (midpoint of 1 and 5) -- this anticipates the axis of symmetry.",
    quickCheck: "Answer: vertex (-4, 7); a=-3 so it opens down, maximum value 7. Watch for (4,7).",
    guided: "Answers: (1) f(x)=3(x-1)^2-2; opens up. (2) a=2, b=8, c=-3; y-intercept (0,-3); axis x=-8/(2*2)=-2. Do not release independent work until about 80% have both.",
    routes: "Answers. Practice: vertex (5,-2), axis x=5, up; vertex (-1,6), axis x=-1, down. f=(x-2)^2-3; f=-2(x+1)^2+4 (since a+4=2 gives a=-2). a=1,b=-4,c=3; y-int (0,3); axis x=2; vertex (2,-1). Apply: a(2)^2-1=7 gives a=2, f=2(x-3)^2-1. f=-x^2+4x+1: a=-1,b=4,c=1; axis 2; vertex (2,5); y-int (0,1), mirror (4,1). Data: vertex (2,5), a=-1: f=-(x-2)^2+5; check f(4)=1. Investigate: expanding gives ax^2-2ahx+(ah^2+k), so b=-2ah and h=-b/(2a); y-intercept f(0)=ah^2+k, with a=2,h=3,k=-1 gives 17; (x+3)^2-4 has h=-3, vertex (-3,-4); (3,-4) is a different point.",
    production: "Answers: (a) h(x)=a(x-2)^2+5 with h(0)=1: 4a+5=1, a=-1, so h(x)=-(x-2)^2+5. (b) Expand: -(x^2-4x+4)+5 = -x^2+4x+1, so a=-1, b=4, c=1; c=1 is the nozzle height in metres. (c) -4/(2(-1)) = 2 -- matches. (d) -(x-2)^2+5=0 gives x=2+sqrt(5), about 4.2 m from the nozzle.",
    geogebra: "h and k move the vertex; a changes the opening and width. g(x)=ax^2+bx+c with the same graph confirms the two forms agree: with a=-1, b=4, c=1 it coincides with f at h=2, k=5.",
    gate: "Answers: (1) a(2)^2+4=0 gives a=-1: f(x)=-(x+1)^2+4. (2) c=5; axis x=-3; vertex (-3,-4). (3) Vertex form: read (h,k) with the sign of h flipped; standard form: x=-b/(2a), then substitute. Score live and route privately.",
    smart: "The non-example is the highest-value part: (3,-4) uses the wrong sign of h -- the true vertex of y=(x+3)^2-4 is (-3,-4), and (3,-4) is not on its graph. The correction shows where the real vertex is.",
    exams: "Show before homework. Format reminders: SAAT four-option, no calculator; SAT two 35-minute adaptive modules with a calculator; GAT about 75 seconds per item with no calculator. Answers: SAAT (A); SAT (A); GAT (C).",
    summary: "Route the clinic group privately through the LMS -- never announce the list to the class.",
  },
};

(async () => { await build(CFG); })();
module.exports = { CFG };
