// Grade 11 · Topic 6 · Lesson 6-5 — Properties of Logarithms
// FIKR lesson plan, Lesson plan 2026/27, differentiation activity, PBL task.
// Classwork is NOT requested this round (matching the pattern for L6-1/L6-3/L6-4)
// — a minimal stub is supplied only so docs_engine's buildAll() does not
// throw; the resulting file is deleted after build and never delivered.
//
// Objectives / EQ / vocabulary / assessments verbatim from the curriculum
// map. This suite shares the same objective thread as lessons_w6l5.js — see
// the standing alignment rule noted there (product/quotient/power properties,
// change of base, and the Vision 2030 solar-capacity production task).
const { buildAll } = require("./docs_engine");
const fs = require("fs");

const MATHDOC = "math_w6l5_doc/_index.json";
const GRAPH = "graphs_w6l5/_index.json";
const ASSESS = ["“Give it a go” questions", "“Time to Check”"];
const T = { t1: 6, t2: 18, t3: 12, t4: 12, t5: 6, t6: 6 };

const AI_CRITIC = "Role of AI: critic only. Briefed prompt — “Check whether I set up the equation $a_n=100$ correctly before I took a logarithm, and challenge any rounding step I have not justified.” Never “solve this”.";
const PILLAR_ADAPTIVE = [
  "Entry branch — the Quizizz result routes each student to the re-teach table, straight to the properties, or the Investigate prompt.",
  "Mid-lesson branch — Pear Deck flags error patterns during independent practice; flagged students get a 2-minute micro-conference while others continue.",
  "Exit branch — the Mastery Gate routes each student: PASS → Enrichment & Challenge; NOT YET → Targeted Learning Clinic at the start of the next lesson.",
  "Routing is communicated privately through the LMS, never read aloud.",
];
const WEEK_NOTE = "Three teaching days this week. If time runs short, cut Smart Production and carry it into the next session — never the Mastery Gate, which is the evidence.";

// =====================================================================
// GR11 · T6 L6-5 · Properties of Logarithms
// =====================================================================
const GR11_L65 = {
  slug: "Gr11_T6_L6-5_Properties_of_Logarithms",
  mathDocIndex: MATHDOC, graphIndex: GRAPH, timings: T,
  lessonTitle: "Properties of Logarithms",
  unit: "Topic 6 — Exponential and Logarithmic Functions · Lesson 6-5",
  gradeFull: "Grade 11 — Algebra II",
  week: "Week 7 · Semester 1, 2026–27",
  weekNum: "7",
  lessonLine: "Grade 11 · Algebra II · Topic 6: Exponential and Logarithmic Functions · Lesson 6-5 — Properties of Logarithms",
  codes: ["HSA.SSE.A.2", "HSF.BF.A.2", "HSF.LE.A.4"],
  mps: ["MP.2", "MP.7"],
  assessments: ASSESS,
  objectives: [
    "Apply properties of logarithms to rewrite logarithmic expressions and evaluate logarithms.",
    "Use the change of base formula to rewrite and evaluate logarithmic expressions.",
  ],
  essentialQuestion: "How can the properties of logarithms, including the change of base formula, be applied to simplify and evaluate logarithmic expressions?",
  vocabList: "logarithmic properties ; change of base formula",

  plan: {
    outcome: [
      "Students will apply the product, quotient and power properties to expand or condense a logarithmic expression, and to evaluate logarithms.",
      "Students will prove each property from the definition of a logarithm and the exponent rules from Topic 5.",
      "Students will use the change of base formula to evaluate any logarithm on a calculator, and to solve for an unknown exponent in a geometric or exponential model.",
      WEEK_NOTE,
    ],
    preclass: [
      "Flipped video (4 min): “Exponent rules in disguise” — why every property of logarithms is just an exponent rule, restated. Posted on the LMS 48 hours ahead.",
      "Two embedded EdPuzzle questions: one exponent-rule recall, one Lesson 6-4 inverse-property recall.",
      "Evidence of readiness: EdPuzzle completion report plus both embedded answers submitted before the bell.",
    ],
    diagTool: [
      "5-question Quizizz ($\\le 4$ minutes): evaluate $\\log_5 25$; apply the product-of-powers rule to $2^{3}\\cdot 2^{4}$; apply the quotient-of-powers rule to $3^{7}⁄3^{2}$; apply the Lesson 6-4 inverse property to $\\log_4(4^{6})$; apply the power-of-a-power rule to $(5^{2})^{3}$.",
      "Cross-referenced against overnight EdPuzzle watch analytics — who watched, who skipped, who missed the embedded items.",
      "Answers: $\\log_5 25=2$; $2^{7}=128$; $3^{5}=243$; $\\log_4(4^{6})=6$; $5^{6}=15625$.",
    ],
    diagGap: [
      "Expected gap 1 — forgetting the Lesson 6-4 inverse property and trying to compute $4^{6}$ first instead of cancelling directly (Q4).",
      "Expected gap 2 — mixing up which exponent rule matches which operation (product vs. quotient of powers).",
      "Expected gap 3 — general fluency with exponent rules from Topic 5, which every property today restates in logarithm language.",
      "Routing: 0–2 correct → re-teach exponent rules.  3–4 → straight to the properties.  5 → begin the Investigate prompt immediately.",
    ],
    instruction: [
      "Direct explanation (3–5 min, flagged students only): a logarithm property is not a new rule to memorise from scratch — it is one of Topic 5's exponent rules, translated into logarithm language, because a logarithm IS an exponent.",
      "Whole class, SSE.A.2: the product property $\\log_b(xy)=\\log_b x+\\log_b y$ and the quotient property $\\log_b(x⁄y)=\\log_b x-\\log_b y$, proved by writing $x=b^{\\log_b x}$ and $y=b^{\\log_b y}$ and applying the exponent-product/quotient rule.",
      "Whole class, SSE.A.2: the power property $\\log_b(x^{n})=n\\log_b x$, proved the same way; the two special values $\\log_b 1=0$ and $\\log_b b=1$; expanding $\\log_5((x^{3}y)⁄(z^{2}))$ fully and condensing $2\\log_4 x-½\\log_4 y$ into a single logarithm.",
      "Whole class, BF.A.2 / LE.A.4: the change of base formula $\\log_b x=(\\log_c x)⁄(\\log_c b)$; a solar plant's capacity modelled geometrically, $a_n=40(1.12)^{n-1}$ megawatts, with the recursive form $a_n=1.12\\,a_{n-1}$, $a_1=40$; solving $40(1.12)^{n-1}=100$ for $n$ by taking a logarithm of both sides and evaluating with change of base.",
      "Narration focus — an exponent on the unknown cannot be removed by division, only by taking a logarithm of both sides; this is the single most common error when solving for $n$.",
      "This is a NEW example — it does not repeat the flipped video.",
    ],
    quickCheck: [
      "On whiteboards, 60 seconds: simplify $\\log_2 20-\\log_2 5$ using the quotient property.",
      "Expected: $\\log_2(20÷5)=\\log_2 4=2$. Watch for students who add instead of subtract, or who subtract the numbers inside the logarithm instead of dividing.",
      "80% correct → release guided practice. Below 80% → one further modelled example, this time condensing three terms.",
    ],
    guided: [
      "Two “Give it a go” problems, identical for every student, worked together with the teacher:",
      "(1) Condense $\\log_6 4+\\log_6 9$ into a single logarithm.  (2) Expand $\\log_7((x^{4})⁄(y^{3}))$ fully.",
      "Answers: (1) $\\log_6(4\\cdot 9)=\\log_6 36$. (2) $4\\log_7 x-3\\log_7 y$.",
      "Feedback: worked live on the board step by step; students self-mark and circle their OWN first error.",
    ],
    independent: [
      "Delivered through the “Choose Your Route” sheet with live feedback in Pear Deck. Routes are named for the task, not for the student.",
      "PRACTICE — Secure the method. Condense and expand four logarithmic expressions, use change of base to evaluate two logarithms to three decimal places, and check each answer by substitution or reversing the step. Done when: every property applied matches its name, and both change-of-base answers agree with a calculator check.",
      "APPLY — Use it in context. A telecom signal-strength context combined with the product property, the recursive form of the solar-capacity sequence, and change of base used to find how many years until capacity first exceeds 150 MW. Done when: the change-of-base answer is shown as an exact logarithm BEFORE it is evaluated, and the final year is a sensible whole number.",
      "INVESTIGATE — Find out why. Proving the quotient property from the definition of a logarithm, explaining with a counterexample why $\\log_b(x+y)$ cannot be split into $\\log_b x+\\log_b y$, and explaining why change of base works with any valid base $c$, not just base 10. Done when: you have an argument grounded in the definition, not just a computed answer.",
      "Every student sits the same Mastery Gate. The gate is not differentiated, because it is the evidence.",
    ],
    production: [
      "Non-routine transfer task — this context has not appeared in practice.",
      "A solar power plant expanding under a Vision 2030 renewable-energy initiative models its capacity, in megawatts, with the geometric sequence $a_n=40(1.12)^{n-1}$, where $n$ is the year of operation. Planners need to know exactly when capacity first exceeds a 100 MW regulatory target.",
      "(a) Write the recursive form of the same sequence, and state what $1.12$ and $40$ each represent physically. (b) Set $a_n=100$ and solve for $n$, expressing the solution as a logarithm before evaluating it with a calculator. (c) Round appropriately and state the first WHOLE year in which capacity exceeds 100 MW. (d) A planner claims capacity will double to 80 MW before it reaches 100 MW. Is that claim consistent with the model? Justify using the growth equation, not just the graph.",
      "Answers: (a) recursive: $a_n=1.12\\,a_{n-1}$, $a_1=40$; $1.12$ is the growth factor (12% growth per year), $40$ is the starting capacity. (b) $40(1.12)^{n-1}=100 \\to (1.12)^{n-1}=2.5 \\to n-1=\\log_{1.12}2.5\\approx 8.09 \\to n\\approx 9.09$. (c) capacity first exceeds the target partway through year 9; accept either year 9 or year 10 with correct justification of the rounding direction. (d) $40(1.12)^{n-1}=80$ gives $n\\approx 7.12$ — yes, consistent, since $7.12<9.09$.",
      "Students then hand their reasoning to the AI critic and ask it to challenge any rounding step they have not justified.",
    ],
    criteria: [
      "Minimum acceptable standard: the recursive form stated correctly, the exponent solved for AS a logarithm before any decimal is computed, and the final year stated as a whole number with a one-sentence justification for the rounding direction.",
      AI_CRITIC,
      "Completed independently by the student: the written justification for parts (a)–(d). AI may challenge it; it may not write it.",
    ],
    evidence: [
      "“Time to Check” — one individual task. No notes, no partner, no AI.",
      "1. Condense $\\log_4 3+\\log_4 12$ into a single logarithm. 2. Expand $\\log_5((x^{2})⁄y)$ fully. 3. In ONE sentence, explain why $\\log_b(x+y)\\ne\\log_b x+\\log_b y$ in general.",
      "Answers: 1. $\\log_4 3+\\log_4 12=\\log_4 36$. 2. $2\\log_5 x-\\log_5 y$. 3. a clean counterexample: $\\log_2(1+1)=\\log_2 2=1$ while $\\log_2 1+\\log_2 1=0+0=0$, which are NOT equal.",
      "Done when: question 2 is fully expanded with every property applied, and question 3 gives a definition-based reason with a counterexample, not just a rule restated.",
      "Scored live in Pear Deck as submissions arrive; result logged in the Impact Dashboard Mastery Rate.",
    ],
    refinement: [
      "Students revise their solar-capacity reasoning using the AI critique and the teacher's micro-conference note.",
      "Final product, three equally acceptable formats: a Canva one-pager, a photographed hand-written solution, or a 45-second voice note.",
      "Required content: the recursive and explicit forms of the capacity sequence, the equation set equal to the target, and the exponent solved as a logarithm before it is evaluated; ONE worked non-example — dividing both sides by $1.12$ instead of taking a logarithm — with a sentence on what goes wrong (the exponent never comes down, so $n$ cannot be isolated that way); and a caption on why a planner needs the exact year, not just the shape of the growth curve.",
      "Graded on originality and clarity of reasoning, not correctness alone.",
    ],
    publication: [
      "Published to the class LMS portfolio; the strongest go on the Mathematics Department wall as the Topic 6 modelling set.",
      "Reflection question: “Which property do you still reach for a reminder card on — product, quotient, power, or change of base?”",
    ],
    differentiation: [
      "PRACTICE — Secure the method. Condense and expand four logarithmic expressions, use change of base to evaluate two logarithms; the property bar stays on the board and a partner is allowed. Done when: every property applied matches its name, and both change-of-base answers agree with a calculator check.",
      "APPLY — Use it in context. The telecom signal-strength item and the Vision 2030 solar-capacity sequence, with change of base used to find a target-crossing year. Done when: the change-of-base answer is shown as an exact logarithm before it is evaluated, and the final year is a sensible whole number.",
      "INVESTIGATE — Find out why. The quotient-property proof, the $\\log_b(x+y)$ counterexample, and the any-base argument for change of base. Done when: there is an argument grounded in the definition, not just a computed answer.",
      "No student is labelled. The routes describe tasks; every student sits the same Mastery Gate.",
    ],
    adaptive: PILLAR_ADAPTIVE,
    saudi: [
      "Production context: a Vision 2030 solar power plant's capacity, modelled geometrically and solved with change of base for the year capacity first exceeds a regulatory target.",
      "In-class Apply-route item: the same solar-capacity sequence, used to find how many years until capacity exceeds a higher target.",
      "Discussion prompt: why a planner needs the exact crossing year from the algebra, not just the shape of the growth curve on a graph.",
    ],
    exams: [
      "SAAT (Tahsili) — condensing a difference of two logarithms with the same base into one, usually a single quotient-property step. Practice tip: same base, subtraction inside the problem, division inside the logarithm.",
      "SAT — Advanced Math, evaluating a logarithm in an unfamiliar base with change of base is a recurring item type. Practice tip: use $\\log$ or $\\ln$ on both top and bottom — never mix the two.",
      "GAT (Qudurat) — combining two same-base logarithms fast, usually a one-step product or quotient property. Practice tip: match the operation between the two logarithms to the property it signals.",
    ],
  },

  plan2026: {
    day: "Tuesday, Week 7", section: "Grade 11-B",
    tools: "Quizizz (diagnostic) · Pear Deck (live practice feedback) · GeoGebra Graphing Calculator · Canva (final product) · Whiteboards",
    resources: "Lesson presentation (18 slides) · “Choose Your Route” differentiation sheet · “Powering Vision 2030” project task · squared paper",
    competencies: ["Applying the product, quotient and power properties to expand or condense a logarithmic expression.", "Using the change of base formula to evaluate a logarithm and to solve for an unknown exponent."],
    technology: ["Quizizz live diagnostic with instant gap analysis.", "GeoGebra sliders showing the geometric growth model crossing a target line."],
    reallife: ["A Vision 2030 solar power plant's capacity, modelled geometrically in megawatts.", "Finding exactly when that capacity first exceeds a regulatory target, using change of base."],
    values: ["Precision — expressing a solution as an exact logarithm before rounding.", "Justification — explaining why a rounding direction was chosen, not just stating an answer."],
    soft: ["Collaboration in assigned group roles.", "Explaining why a property works, not just applying it."],
    hard: ["Applying the product, quotient and power properties to logarithmic expressions.", "Using the change of base formula to evaluate logarithms and solve for an exponent."],
    phases: [
      "FIKR Phase 1 — Diagnose. 5-question Quizizz on exponent rules and the Lesson 6-4 inverse property. Results read as a gap map; students routed to the re-teach table, straight to the properties, or the Investigate prompt.",
      "FIKR Phase 2 — Targeted Instruction. Focused re-teach on exponent rules for flagged students. Whole class: the product, quotient and power properties, each proved from the definition of a logarithm; the change of base formula, applied to a Vision 2030 solar-capacity model. Quick check on whiteboards.",
      "FIKR Phase 3 — Practice. Two identical “Give it a go” problems worked together. Students then choose a route and may switch at any time. Live feedback via Pear Deck; 2-minute micro-conferences.",
      "FIKR Phase 4 — Production. The Vision 2030 solar-capacity sequence: the recursive form, the equation set equal to the target, and the exponent solved as a logarithm before it is evaluated. AI used as critic only.",
      "FIKR Phase 5 — Proof of Learning. “Time to Check” — a condensed logarithm, a fully expanded logarithm, and a one-sentence, counterexample-based justification. No notes, no partner, no AI.",
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
    closure: "Two minutes of peer show-and-tell on the final products, then the reflection question: “Which property do you still reach for a reminder card on — product, quotient, power, or change of base?”",
    homework: "Finish the final product and upload to the LMS portfolio (any of the three formats). Practice set on Pear Deck — 12 questions, choose your route. Watch the flipped video for the next lesson, Topic 6 · Lesson 6-6 — Exponential and Logarithmic Equations and Inequalities. Clinic group: bring your Time to Check paper.",
  },

  // Minimal stub — classwork is NOT requested this round; this file is
  // deleted immediately after build and never delivered.
  classwork: {
    subtitle: "Not delivered this round.",
    sections: [
      { h: "SECTION A", note: "placeholder — not delivered", lines: 2,
        q: [{ n: "Q1", eq: "m_ws1", t: "Evaluate." }] },
    ],
  },

  diffSheet: {
    routes: [
      { note: "Condense, expand, and change of base", done: "every property you applied matches its name, and both change-of-base answers agree with a calculator check.",
        intro: "Condense or expand each expression, then use change of base where shown.",
        grid: [["1.", "m_ws1"], ["2.", "m_ws2"], ["3.", "m_ws3"], ["4.", "m_ws4"], ["5.", "m_cob_ws1"], ["6.", "m_cob_ws2"]],
        tasks: ["7.  Check any two of your answers above by substituting a value or reversing the step."],
        lines: 2 },
      { note: "A Saudi context, and the solar-capacity model", done: "your change-of-base answer is shown as an exact logarithm BEFORE you evaluate it, and your final year is a sensible whole number.",
        graph: "gm_growth", graphW: 380,
        tasks: [
          "1.  A telecom tower's signal strength model uses $\\log_{10}$ ratios that combine additively when two signals overlap. Use the product property to combine $\\log_{10} 4$ and $\\log_{10} 25$ into a single logarithm, then evaluate it exactly.",
          "2.  A Vision 2030 solar plant's capacity follows $a_n=40(1.12)^{n-1}$ megawatts. Write the recursive form of the same sequence.",
          "3.  Use change of base to find how many years until capacity first exceeds 150 MW, to two decimal places.",
        ], lines: 4 },
      { note: "Arguments, not answers", done: "you have an argument grounded in the definition, not just a computed answer.",
        tasks: [
          ["1.  Prove the quotient property ", { eq: "m_quot_rule", k: 0.95 }, " from the definition of a logarithm — do not just quote the product property, derive it the same way."],
          "2.  Explain why $\\log_b(x+y)$ can NOT be split into $\\log_b x+\\log_b y$, using a specific numerical counterexample.",
          "3.  A classmate claims the change of base formula only works with base 10. Explain why any valid base $c$ gives the same answer, using the definition of a logarithm.",
        ], lines: 5 },
    ],
  },

  pbl: {
    title: "Powering Vision 2030", minutes: 20,
    subtitle: "A 20-minute group project. Work in fours. Every member signs the sheet.",
    driving: "A solar plant's capacity grows geometrically toward a regulatory target. If planners are only given the target, how do they work out exactly which year the plant will reach it?",
    situation: [
      "A solar power plant expanding under a Vision 2030 renewable-energy initiative models its capacity, in megawatts, with the geometric sequence $a_n=40(1.12)^{n-1}$, where $n$ is the year of operation.",
      "This monitoring supports Vision 2030 renewable-energy targets.",
      "A group of Grade 11 students is asked to build a quick-reference tool that finds exactly when capacity first crosses a regulatory target.",
    ],
    eq: "m_prod_eq",
    steps: [
      ["1", "WRITE THE MODEL  (3 min)", "Write the recursive form of the same sequence, and state what $1.12$ and $40$ each represent physically."],
      ["2", "SET THE TARGET  (4 min)", "Set $a_n=100$ and write the exponential equation that must be solved for $n$."],
      ["3", "SOLVE WITH A LOGARITHM  (5 min)", "Solve for $n$ — show every algebra step, expressing your solution as a logarithm before you evaluate it."],
      ["4", "EVALUATE WITH CHANGE OF BASE  (4 min)", "Use change of base to evaluate your logarithm, and state the first WHOLE year capacity exceeds 100 MW."],
      ["5", "PRESENT  (4 min)", "One sentence: why does a planner need the exact year from the algebra, not just the shape of the growth curve?"],
    ],
    working: [["Step 1 — the recursive form and what it means:", 2], ["Step 2 — the equation to solve:", 2],
              ["Step 3 — the logarithm, worked out:", 4], ["Step 4 — the evaluated year:", 3],
              ["Step 5 — our sentence:", 2]],
    roles: ["Reader — states the capacity model", "Calculator — evaluates the logarithm with change of base", "Checker — verifies the algebra step by step", "Presenter — says the sentence"],
    doneWhen: ["The recursive form is written correctly, with $1.12$ and $40$ explained physically.", "The exponent is solved for as a logarithm before any decimal is computed.", "Change of base is shown as a fraction of two logarithms before it is evaluated.", "Your sentence makes sense to someone who does not study maths."],
    materials: ["This sheet", "Squared paper", "A pencil and ruler", "A calculator"],
  },
};

(async () => {
  await buildAll(GR11_L65);
  const cwFile = `Classwork_${GR11_L65.slug}.docx`;
  if (fs.existsSync(cwFile)) fs.unlinkSync(cwFile);
})();

module.exports = { GR11_L65 };
