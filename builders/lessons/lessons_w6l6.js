// Grade 11 · Topic 6 · Lesson 6-6 — Exponential and Logarithmic Equations
// and Inequalities
//
// Follows L6-5 (Properties of Logarithms) directly, and closes Topic 6
// (Exponential and Logarithmic Functions) — L6-7 (Geometric Sequences and
// Series) opens the next topic. Objectives, essential question, vocabulary,
// standards and MPs are quoted VERBATIM from "Curriculum map A2 OBLAS.docx",
// Unit 6, Lesson 6.
//
// Alignment (standing rule, 24 Sep 2026): this deck, its FIKR lesson plan,
// its differentiation activity, and its PBL/product task must all share the
// same objective thread — see w6l6_docs.js for the matching plan/activity/PBL.
// The Saudi Green Initiative emissions context here is the SAME context,
// same numbers, as the PBL task and the docs' production/evidence sections.
//
// HOUSE RULE, confirmed by Mr Thiab 26 Sep 2026: every FIKR deck ships
// ANIMATED — run engines/animate_deck.py on the built .pptx before delivery.
// (Retro-fitted onto Gr10_T1_L6_Linear_Systems.pptx the same day; do not
// ship a new deck without this step again.)
//
// Every piece of mathematics inside a sentence (titles, panels, bars, notes)
// is written as $...$ per the inline-maths house rule — see engines/inline_math.js.
// Only self-contained display equations use a LaTeX image key (eq:).
const { build } = require("../../engines/lesson_engine");

const MATH = "math_w6l6/_index.json";
const GRAPH = "graphs_w6l6/_index.json";
const ASSESS = ["“Give it a go” questions", "“Time to Check”"];

// =====================================================================
// GRADE 11 · TOPIC 6 · LESSON 6-6 — Exponential and Logarithmic Equations
// and Inequalities
// =====================================================================
const GR11_L66 = {
  out: "Gr11_T6_L6-6_Exponential_and_Logarithmic_Equations_and_Inequalities.pptx",
  deckTitle: "Exponential and Logarithmic Equations and Inequalities — Grade 11 Algebra II",
  mathIndex: MATH, graphIndex: GRAPH,
  weekNum: "8",
  topicLine: "TOPIC 6 · EXPONENTIAL AND LOGARITHMIC FUNCTIONS · LESSON 6-6",
  lessonTitle: "Exponential and Logarithmic Equations and Inequalities",
  titleSize: 28,
  subtitle: "Every equation with an exponent has two ways in — match the base, or take a logarithm",
  titleEq: "e_title_w", titleEqK: 2.0,
  titleEqAlt: "b to the x equals y if and only if x equals log base b of y",
  grade: "Grade 11", week: "Week 8 · Semester 1, 2026–27",
  footerLeft: "Grade 11 · Algebra II · Topic 6 · Lesson 6-6",
  lessonRef: "Lesson 6-6 — Exponential and Logarithmic Equations and Inequalities",
  nextLesson: "Topic 6 Recap & Unit Assessment — then Topic 7 · Lesson 7-1, Geometric Sequences and Series",

  codes: ["HSA.SSE.A.2", "HSA.CED.A.1", "HSA.REI.A.1", "HSF.LE.A.4"],
  mps: ["MP.2", "MP.3"],
  assessments: ASSESS,

  objectives: [
    "Solve exponential equations and inequalities by applying the concept of a common base.",
    "Solve logarithmic equations and inequalities by using the rules of logarithms.",
    "Use logarithms to solve exponential equations and models.",
  ],
  essentialQuestion: "How can we solve exponential and logarithmic equations and inequalities?",

  vocabulary: [
    { term: "Exponential equation", def: "An equation in which the variable appears in an EXPONENT, such as $3^{x}=27$ — solved by matching bases or by taking a logarithm." },
    { term: "Exponential inequality", def: "An inequality with the variable in an exponent. Solved the same way as an exponential equation, EXCEPT the direction can flip if the base is between $0$ and $1$." },
    { term: "Logarithmic equation", def: "An equation containing a logarithm of the variable, such as $\\log_2(x+3)=4$ — solved by condensing to one logarithm, then exponentiating both sides." },
    { term: "Logarithmic inequality", def: "An inequality containing a logarithm of the variable. Its solution must always be checked against the logarithm's DOMAIN, not just the inequality itself." },
  ],
  vocabSub: "All four terms the curriculum map lists for this lesson",

  prior: [
    { h: "Same base means same exponent (Topic 5)", eq: "e_prior_base", d: "If $b^{m}=b^{n}$ for the same base $b$, then $m=n$ — an exponential function is one-to-one, so matching exponents is always valid." },
    { h: "Lesson 6-4: the inverse property", eq: "e_prior_inv", d: "$\\log_b(b^{x})=x$ undoes an exponent instantly — today it turns an exponentiated logarithm back into the variable it isolates." },
    { h: "Lesson 6-5: properties of logarithms", eq: "e_prior_props", d: "A sum of logarithms condenses to the logarithm of a product — today that condensing step turns a two-logarithm equation into a one-logarithm equation you already know how to solve." },
  ],
  priorSub: "Three things you already know — today they solve for the unknown",
  carryOver: "Every equation of the form $b^{x}=y$ says the same thing as $x=\\log_b y$ — these are just two ways of writing ONE fact. Match the bases when you can; take a logarithm when you can't.",
  carryOverEq: "e_def",

  diagnose: {
    title: "Warm-Up: The Tools You Already Have",
    sub: "Answer on Quizizz — 5 questions, 4 minutes. This builds a gap map, not a grade.",
    questions: [
      { eq: "e_d1", t: "Solve by common base." },
      { eq: "e_d2", t: "Apply the inverse property." },
      { eq: "e_d3", t: "Condense, then evaluate." },
      { eq: "e_d4", t: "Evaluate by change of base, to 3 decimal places." },
      { eq: "e_d5", t: "Solve the linear inequality." },
    ],
    routing: "0–2 correct → re-teach exponent and logarithm rules with me.      3–4 correct → straight to solving equations.      5 correct → start the Investigate prompt now.",
  },

  instruction: [
    {
      title: "Common Base: Equations and Inequalities",
      sub: "Objective 1 — rewrite both sides with the same base, then compare exponents",
      rowsHead: ["MATCH THE BASE", "RESULT"],
      rowsTop: 2.42, rowH: 1.0,
      rows: [
        [{ eq: "e_eq1", k: 1.6 }, { eq: "e_eq1_sol", k: 1.3 }],
        [{ eq: "e_ineq1", k: 1.6 }, { eq: "e_ineq1_sol", k: 1.3 }],
        [{ eq: "e_ineq2", k: 1.5 }, { eq: "e_ineq2_sol", k: 1.05 }],
      ],
      bar: ["A BASE BETWEEN 0 AND 1 FLIPS THE INEQUALITY", "$2^{x+1}\\le 32$ keeps its direction because base $2>1$ is increasing; $\\left(1⁄2\\right)^{x}<8$ flips because base $1⁄2<1$ is DEcreasing — the bigger exponent gives the SMALLER value."],
      barY: 6.32,
      notes: "Row 1: $3^{2x-1}=3^{3} \\to 2x-1=3 \\to x=2$; check $3^{3}=27$. Row 2: $2^{x+1}\\le 2^{5} \\to x+1\\le 5 \\to x\\le 4$, direction preserved since base $2>1$. Row 3: $\\left(1⁄2\\right)^{x}<\\left(1⁄2\\right)^{-3} \\to x>-3$, direction FLIPS since base $1⁄2$ is between 0 and 1 — see the graph on the geogebra slide for why. Misconception to address aloud: students apply the same-direction rule to EVERY exponential inequality; press them to check whether the base is bigger or smaller than 1 before deciding direction.",
    },
    {
      title: "Logarithmic Equations and Inequalities",
      sub: "Objective 2 — condense with Lesson 6-5's properties, then exponentiate",
      panel: {
        h: "CONDENSE, EXPONENTIATE, CHECK THE DOMAIN",
        items: [
          "One logarithm: $\\log_2(x+3)=4 \\ \\Rightarrow\\ x+3=2^{4}=16 \\ \\Rightarrow\\ x=13$.",
          "Two logarithms — condense FIRST: $\\log_3 x+\\log_3(x-2)=1 \\ \\Rightarrow\\ \\log_3(x(x-2))=1 \\ \\Rightarrow\\ x(x-2)=3$.",
          "That gives $x^{2}-2x-3=0 \\ \\Rightarrow\\ x=3$ or $x=-1$ — but $x=-1$ fails the domain $x>2$, so it is REJECTED.",
          "Inequality, same method: $\\log_5(x-1)\\le 2 \\ \\Rightarrow\\ 0<x-1\\le 5^{2} \\ \\Rightarrow\\ 1<x\\le 26$ — the domain restriction $x>1$ stays part of the final answer.",
        ],
      },
      panelX: 0.55, panelY: 2.42, panelW: 11.9, panelH: 4.0,
      bar: ["A LOGARITHMIC EQUATION'S SOLUTION IS NEVER FINISHED UNTIL THE DOMAIN IS CHECKED", "every candidate solution must make the ORIGINAL logarithm's argument positive — an algebraically correct root can still be an extraneous solution."],
      barY: 6.32,
      notes: "$\\log_2(x+3)=4$: exponentiate both sides as powers of 2, $x+3=16$, $x=13$; domain check $13+3=16>0$, valid. $\\log_3 x+\\log_3(x-2)=1$: product property condenses to $\\log_3(x^{2}-2x)=1$, exponentiate: $x^{2}-2x=3$, factor $(x-3)(x+1)=0$; domain requires BOTH $x>0$ and $x>2$, so only $x=3$ survives — $x=-1$ is extraneous. $\\log_5(x-1)\\le 2$: domain $x>1$ FIRST, then exponentiate the inequality (a logarithm is an increasing function, so direction is preserved) to get $x-1\\le 25$, so $x\\le 26$; combined answer $1<x\\le 26$. Misconception to address aloud: students solve the algebra correctly and stop — they never go back to check each root in the ORIGINAL logarithm's domain, which is exactly where an extraneous solution hides.",
    },
    {
      title: "When There's No Common Base — Take a Logarithm",
      sub: "Objective 3 — use a logarithm to solve an exponential equation or model",
      graph: "g_emissions", graphW: 6.4, graphY: 2.5,
      graphAlt: "The decaying curve E of t equals 500,000 times 0.9 to the t, crossing the half-target line of 250,000 metric tons at t approximately 6.58 years",
      panel: {
        h: "TAKE THE LOGARITHM OF BOTH SIDES",
        items: [
          "$5^{x}=40$ has no nice common base — take $\\log$ of both sides: $x=(\\log 40)⁄(\\log 5)\\approx 2.292$.",
          "A refinery's annual CO$_2$ emissions fall 10% a year: $E(t)=500{,}000(0.9)^{t}$ metric tons.",
          "Find when emissions first drop to HALF: set $E(t)=250{,}000$, giving $(0.9)^{t}=0.5$.",
          "$t=(\\log 0.5)⁄(\\log 0.9)\\approx 6.58$ years — matches the crossing point on the graph.",
        ],
      },
      panelX: 7.2, panelW: 5.7, panelH: 4.0,
      bar: ["AN UNKNOWN IN THE EXPONENT NEEDS A LOGARITHM, NOT DIVISION", "dividing both sides by the base does not isolate an exponent — only taking a logarithm of both sides brings the exponent down where you can solve for it."],
      barY: 6.32,
      notes: "$5^{x}=40 \\to x=(\\log 40)/(\\log 5)\\approx 2.292$ — check: $5^{2.292}\\approx 40$. Emissions model: $500{,}000(0.9)^{t}=250{,}000 \\to (0.9)^{t}=0.5 \\to t=(\\log 0.5)/(\\log 0.9)\\approx 6.579$, so the halving point falls partway through year 7. Misconception to address aloud: students try to divide both sides by $0.9$ repeatedly instead of taking a logarithm — technically possible for a whole number of steps, but it cannot produce a decimal answer like $6.58$, and it does not generalize to a model with a non-nice base.",
    },
  ],

  quickCheck: {
    lead: "Solve for $x$, using a logarithm, to three decimal places:", leadW: 7.0,
    eq: "e_qc", k: 2.0,
    think: "Ask: can I rewrite 50 as a power of 3? No — so take a logarithm of both sides instead of hunting for a common base.",
    rule: "80% correct → straight to guided practice.   Below 80% → one more modelled example, this time a logarithmic equation.",
  },

  guided: {
    mins: 4,
    items: [
      { eq: "e_g1", t: "Solve the logarithmic equation for $x$.", hint: "Exponentiate both sides as powers of the base first, then isolate $x$." },
      { eq: "e_g2", t: "Solve for $x$ using a logarithm, to three decimal places.", hint: "No common base exists here — take $\\log$ of both sides." },
    ],
  },

  routes: {
    mins: 8,
    tiers: [
      { items: ["Solve by common base: (a) $2^{x}=16$   (b) $3^{x+2}=81$   (c) $5^{2x}=125$.", "Solve the inequality $2^{x-1}\\ge 8$.", "Solve: $\\log_2(x+1)=5$.", "Solve $7^{x}=90$ using a logarithm, to three decimal places."],
        help: "You may use: the property bar on the board, a calculator, and a partner.",
        done: "every equation solution checks back in the ORIGINAL equation, and your logarithm answer is rounded only at the very last step.", eq: "e_ws1" },
      { items: ["A Jeddah startup's active users grow 8% a month: $U(t)=U_{0}(1.08)^{t}$. Find, to two decimal places, how many months until the user base DOUBLES.", "Solve the inequality $\\log_3(x-4)<2$, stating the domain restriction as part of your final answer.", "A savings account follows $B(t)=2000(1.05)^{t}$ SAR. Find how many years until the balance exceeds 3000 SAR."],
        help: "You may use: the worked example, and a calculator.",
        done: "your month/year answer is rounded to a sensible whole unit, and your logarithmic inequality states BOTH the domain restriction and the solved inequality.", eq: "e_ws7" },
      { items: ["Explain why $2^{x}=-8$ has no real solution, using the RANGE of an exponential function.", "A classmate solves $\\log_5(x-3)=2$ and gets $x=28$ without checking the domain. Confirm whether $x=28$ is actually valid, and explain why checking mattered here.", "Prove that if $b^{m}=b^{n}$ for $b>0,\\ b\\ne 1$, then $m=n$, using the fact that $y=b^{x}$ is one-to-one."],
        help: "You may use: nothing but your reasoning.",
        done: "you have an argument, not just an answer.", eq: null },
    ],
  },

  production: {
    title: "Vision 2030: Meeting a Green Initiative Target",
    sub: "A context you have not seen before — this tests transfer",
    situation: "A refinery participating in the Saudi Green Initiative is cutting its annual carbon emissions by 10% every year. This year's emissions are 500,000 metric tons of CO2, modeled by $E(t)=500{,}000(0.9)^{t}$, where $t$ is years from now.",
    eq: "e_ctx_w", eqK: 1.6,
    tasks: [
      "(a)  Set up the equation for when emissions first fall to HALF their current level, and solve for $t$ as a logarithm before evaluating it.",
      "(b)  State the first WHOLE year in which the target is met, with a one-sentence justification for your rounding.",
      "(c)  The board wants emissions below 150,000 tons (30% of the current level) within 12 years. Does the model meet this goal? Solve the inequality algebraically to justify.",
      "(d)  A board member says “just divide 500,000 by 10 — it hits zero in 10 years.” Explain in one sentence why this reasoning is wrong for a percentage-based model.",
    ],
    note: "The logarithmic expression for $t$ shown exactly before any decimal is computed, and part (c) answered with a solved inequality, not just yes or no.",
    aiPrompt: "“Check whether I set up the equation before I took a logarithm, and challenge any rounding step I have not justified.”",
  },

  geogebra: {
    sub: "Drag the base below 1 and watch an inequality's direction flip",
    graph: "g_flip",
    graphAlt: "The decreasing curve one half to the x, crossing the horizontal line y equals 8 at x equals negative 3, with the region x greater than negative 3 shaded where the curve sits below the line",
    explore: "Graph $f(x)=\\left(1⁄2\\right)^{x}$ at geogebra.org/graphing alongside $y=8$, and find where they cross. Then add a slider for the base $b$ in $f(x)=b^{x}$: with $b>1$ the curve rises and the inequality direction matches; drag $b$ below 1 and watch the curve flip to falling — and the inequality direction flip with it.",
  },

  gate: {
    items: [
      { t: "Solve by common base.", eq: "e_gate1" },
      { t: "Solve the logarithmic equation, checking the domain.", eq: "e_gate2" },
      { t: "In ONE sentence, explain why $7^{x}=15$ needs a logarithm to solve, while $2^{x}=8$ does not.", eq: null },
    ],
    footer: "Exact answers for Q1 and Q2, with Q2's domain check shown, and Q3 a reason rather than a restatement.",
    routing: "PASS → Enrichment & Challenge (a logarithmic inequality with two logarithm terms to condense first).      NOT YET → Targeted Learning Clinic on domain-checking a logarithmic equation, start of next lesson.",
  },

  smart: {
    steps: [
      { h: "Show the model", d: "Present the emissions equation set to the half-target, the exponent solved as a logarithm before evaluating, and the year stated with justification." },
      { h: "Expose the trap", d: "Add one worked NON-example — treating a 10%-per-year reduction as a fixed 50,000-ton yearly drop — and a sentence on how a reader would spot the error." },
      { h: "Say why it matters", d: "One caption — why a regulator needs the EXACT year a target is met, not just the shape of the decline — for a non-maths reader." },
    ],
    published: "the class LMS portfolio; the strongest go on the Department wall as our Topic 6 modelling set.",
    reflection: "which is still harder for you — knowing WHEN to use a logarithm instead of matching bases, or checking a logarithmic equation's domain?",
  },

  exams: [
    { code: "GAT", full: "Qudurat — General Aptitude", skill: "A quick common-base exponential equation, meant to be solved mentally without a calculator.", fmt: "Multiple choice, about 75 seconds per item, no calculator.", tip: "Rewrite the number on the right as a power of the same base FIRST — the whole problem collapses to comparing exponents.",
      question: "Solve $4^{x}=64$. What is $x$?",
      steps: ["Rewrite $64$ as a power of $4$: $64=4^{3}$.", "Match exponents: $4^{x}=4^{3}\\ \\Rightarrow\\ x=3$."] },
    { code: "SAAT", full: "Tahsili — Achievement Test", skill: "A one-logarithm equation, exponentiated directly — sits in the Grade 11 band.", fmt: "Four-option multiple choice, no calculator.", tip: "Exponentiate both sides using the logarithm's OWN base — it undoes the logarithm in one step.",
      question: "Solve $\\log_2(x-1)=4$.",
      steps: ["Exponentiate base 2: $x-1=2^{4}=16$.", "Solve: $x=17$."] },
    { code: "SAT", full: "College Board", skill: "Advanced Math — solving an exponential equation with no common base using logarithms, a recurring item type.", fmt: "Two 35-minute adaptive modules; calculator allowed throughout.", tip: "Take $\\log$ or $\\ln$ of both sides and divide — never try to guess a decimal base by trial and error.",
      question: "If $3^{x}=20$, what is the value of $x$ to the nearest hundredth?",
      steps: ["Take $\\log$ of both sides: $x\\log 3=\\log 20$.", "Divide: $x=(\\log 20)/(\\log 3)$.", "Evaluate: $x\\approx 2.73$."] },
  ],
  examBar: ["THE SINGLE MOST EXAMINED IDEA HERE:", "match the bases and set the exponents equal when you can; when you can't, take a logarithm of both sides — and always check a logarithmic equation's solution against its domain."],

  summary: [
    "Solve an exponential equation by rewriting both sides with a common base and setting the exponents equal.",
    "Solve an exponential inequality by common base, remembering that a base between 0 and 1 flips the inequality's direction.",
    "Solve a logarithmic equation by condensing with Lesson 6-5's properties, exponentiating both sides, and checking the domain.",
    "Solve a logarithmic inequality the same way, keeping the domain restriction as part of the final answer.",
    "Use a logarithm to solve an exponential equation or model when no common base exists.",
  ],
  homework: [
    "Finish your product and upload it to the LMS portfolio — any of the three formats.",
    "Practice set on Pear Deck: 12 questions, choose your route.",
    "This closes Topic 6 — the next session is the Topic Recap and Unit Assessment, not a new flipped video.",
    "Clinic group: bring your Time to Check paper — we start with 10 minutes on checking a logarithmic equation's domain.",
  ],

  notes: {
    cover: "Week 8 lesson for Grade 11-B, closing Topic 6 (Exponential and Logarithmic Functions) directly from Lesson 6-5. The Topic Recap and Unit Assessment follow next session, not a new lesson.",
    objectives: "All three objectives are verbatim from the curriculum map. The map lists HSA.SSE.A.2, HSA.CED.A.1, HSA.REI.A.1 and HSF.LE.A.4 for this lesson, and only MP.2 and MP.3 — do not add others. HSF.LE.A.4 is the standard's own \"solve $a\\cdot b^{ct}=d$ as a logarithm\" language — the emissions model is written in exactly that shape.",
    vocabulary: "All four terms are the map's list. Pair them as you introduce them: exponential equation/inequality first, then logarithmic equation/inequality — the same solving logic, applied to the inverse function.",
    prior: "If a student cannot recall the inverse property from Lesson 6-4 or condense two logarithms from Lesson 6-5, both new methods stall immediately. Watch for it in the diagnostic, questions 2 and 3.",
    diagnose: "Answers: $x=3$ ($8=2^{3}$); $\\log_3(3^{5})=5$; $\\log_2 20-\\log_2 5=\\log_2 4=2$; $\\log_7 30\\approx 1.748$; $x>3$. Expected gap: Q4, where students forget change of base entirely and try to guess a decimal power of 7.",
    quickCheck: "Answer: $x=(\\log 50)/(\\log 3)\\approx 3.561$. Watch for students who try common base first on a number that doesn't have one, wasting time before switching methods.",
    guided: "Answers — 1: $\\log_2(x-1)=5 \\to x-1=32 \\to x=33$. 2: $6^{x}=200 \\to x=(\\log 200)/(\\log 6)\\approx 2.957$. Do not release independent work until roughly 80% have both.",
    routes: "Students choose their own route and may switch mid-task. Pear Deck flags error patterns live; use it to decide who gets a two-minute conference. Apply-route answers: doubling time $\\approx 9.01$ months; $\\log_3(x-4)<2 \\to 4<x<13$; savings balance exceeds 3000 SAR after $\\approx 8.31$ years, so year 9.",
    production: "Answers — (a) $(0.9)^{t}=0.5 \\to t=(\\log 0.5)/(\\log 0.9)\\approx 6.579$. (b) year 7 is the first WHOLE year emissions fall below half (at $t=6$, $E\\approx 265{,}720$; at $t=7$, $E\\approx 239{,}150$). (c) $(0.9)^{12}\\approx 0.282<0.30$, so emissions at year 12 are about $141{,}000$ tons — YES, the model meets the 150,000-ton goal within 12 years (solved exactly: $(0.9)^{t}<0.30 \\to t>(\\log 0.30)/(\\log 0.9)\\approx 11.43$, so by year 12 the target is already met). (d) the board member has mistaken a PERCENTAGE reduction for a fixed yearly amount — 10% of a shrinking total is itself shrinking, so the actual yearly drop gets smaller every year and emissions approach, but never exactly reach, zero.",
    geogebra: "The slider is the whole point — watching the curve tip from rising to falling as $b$ crosses 1 is the same moment an inequality's direction would flip, made visible rather than just stated as a rule.",
    gate: "Answers: $5^{2x-1}=125=5^{3} \\to 2x-1=3 \\to x=2$. $\\log_4(x+5)=3 \\to x+5=64 \\to x=59$; domain check $59+5=64>0$, valid. Q3: because $15$ is not a whole-number power of $7$ (no integer exponent gives $15$), so the exponent must be found with a logarithm, while $8=2^{3}$ already IS a whole-number power of $2$. Score live and route privately.",
    smart: "The non-example in step 2 is the highest-value part — mistaking a percentage decrease for a fixed amount is exactly the error a real sustainability report could make, and the correction (the yearly drop itself shrinks) is worth showing as a short table.",
    exams: "Show this before homework so the practice set has an obvious purpose. Walk through at least one worked card aloud before moving on.",
    summary: "Route the clinic group privately through the LMS — never announce the list to the class.",
  },
};

(async () => {
  await build(GR11_L66);
})();

module.exports = { GR11_L66 };
