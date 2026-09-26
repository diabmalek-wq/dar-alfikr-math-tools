// Grade 11 · Topic 6 · Lesson 6-6 — Exponential and Logarithmic Equations
// and Inequalities
// FIKR lesson plan, Lesson plan 2026/27, differentiation activity, PBL task.
// Classwork is NOT requested this round (matching the pattern for
// L6-1/L6-3/L6-4/L6-5) — a minimal stub is supplied only so docs_engine's
// buildAll() does not throw; the resulting file is deleted after build and
// never delivered.
//
// Objectives / EQ / vocabulary / assessments verbatim from the curriculum
// map. This suite shares the same objective thread as lessons_w6l6.js — see
// the standing alignment rule noted there (common base, logarithmic
// equations/inequalities with domain checks, and the Saudi Green Initiative
// emissions production task).
const { buildAll } = require("../../engines/docs_engine");
const fs = require("fs");

const MATHDOC = "math_w6l6_doc/_index.json";
const GRAPH = "graphs_w6l6/_index.json";
const ASSESS = ["“Give it a go” questions", "“Time to Check”"];
const T = { t1: 6, t2: 18, t3: 12, t4: 12, t5: 6, t6: 6 };

const AI_CRITIC = "Role of AI: critic only. Briefed prompt — “Check whether I set up the equation before I took a logarithm, and challenge any rounding step I have not justified.” Never “solve this”.";
const PILLAR_ADAPTIVE = [
  "Entry branch — the Quizizz result routes each student to the re-teach table, straight to solving equations, or the Investigate prompt.",
  "Mid-lesson branch — Pear Deck flags error patterns during independent practice; flagged students get a 2-minute micro-conference while others continue.",
  "Exit branch — the Mastery Gate routes each student: PASS → Enrichment & Challenge; NOT YET → Targeted Learning Clinic at the start of the next lesson.",
  "Routing is communicated privately through the LMS, never read aloud.",
];
const WEEK_NOTE = "This lesson closes Topic 6. If time runs short, cut Smart Production and carry it into the next session — never the Mastery Gate, which is the evidence.";

// =====================================================================
// GR11 · T6 L6-6 · Exponential and Logarithmic Equations and Inequalities
// =====================================================================
const GR11_L66 = {
  slug: "Gr11_T6_L6-6_Exponential_and_Logarithmic_Equations_and_Inequalities",
  mathDocIndex: MATHDOC, graphIndex: GRAPH, timings: T,
  lessonTitle: "Exponential and Logarithmic Equations and Inequalities",
  unit: "Topic 6 — Exponential and Logarithmic Functions · Lesson 6-6",
  gradeFull: "Grade 11 — Algebra II",
  week: "Week 8 · Semester 1, 2026–27",
  weekNum: "8",
  lessonLine: "Grade 11 · Algebra II · Topic 6: Exponential and Logarithmic Functions · Lesson 6-6 — Exponential and Logarithmic Equations and Inequalities",
  codes: ["HSA.SSE.A.2", "HSA.CED.A.1", "HSA.REI.A.1", "HSF.LE.A.4"],
  mps: ["MP.2", "MP.3"],
  assessments: ASSESS,
  objectives: [
    "Solve exponential equations and inequalities by applying the concept of a common base.",
    "Solve logarithmic equations and inequalities by using the rules of logarithms.",
    "Use logarithms to solve exponential equations and models.",
  ],
  essentialQuestion: "How can we solve exponential and logarithmic equations and inequalities?",
  vocabList: "exponential equation ; exponential inequality ; logarithmic equation ; logarithmic inequality",

  plan: {
    outcome: [
      "Students will solve an exponential equation or inequality by rewriting both sides with a common base and comparing exponents, including recognizing when a base between 0 and 1 flips the inequality.",
      "Students will solve a logarithmic equation or inequality by condensing with the properties of logarithms, exponentiating both sides, and checking the domain.",
      "Students will use a logarithm to solve an exponential equation or model when no common base exists.",
      WEEK_NOTE,
    ],
    preclass: [
      "Flipped video (4 min): “Two ways to undo an exponent” — matching bases versus taking a logarithm, framed as the same idea from two directions. Posted on the LMS 48 hours ahead.",
      "Two embedded EdPuzzle questions: one common-base recall, one inverse-property recall from Lesson 6-4.",
      "Evidence of readiness: EdPuzzle completion report plus both embedded answers submitted before the bell.",
    ],
    diagTool: [
      "5-question Quizizz ($\\le 4$ minutes): solve $2^{x}=8$ by common base; apply the inverse property to $\\log_3(3^{5})$; condense and evaluate $\\log_2 20-\\log_2 5$; evaluate $\\log_7 30$ by change of base to 3 decimal places; solve the linear inequality $2x-1>5$.",
      "Cross-referenced against overnight EdPuzzle watch analytics — who watched, who skipped, who missed the embedded items.",
      "Answers: $x=3$; $\\log_3(3^{5})=5$; $\\log_2 20-\\log_2 5=2$; $\\log_7 30\\approx 1.748$; $x>3$.",
    ],
    diagGap: [
      "Expected gap 1 — a student who cannot recall the inverse property from Lesson 6-4; the logarithmic-equation method stalls immediately without it.",
      "Expected gap 2 — a student who cannot condense two logarithms from Lesson 6-5; the two-logarithm equation method stalls without it.",
      "Expected gap 3 — Q4, which decides whether a student reaches for change of base at all when no common base is available.",
      "Routing: 0–2 correct → re-teach exponent and logarithm rules.  3–4 → straight to solving equations.  5 → begin the Investigate prompt immediately.",
    ],
    instruction: [
      "Direct explanation (3–5 min, flagged students only): every equation of the form $b^{x}=y$ says the same thing as $x=\\log_b y$ — two ways of writing one fact. Match the bases when possible; take a logarithm when not.",
      "Whole class, SSE.A.2/CED.A.1 (Objective 1): solve $3^{2x-1}=27$ and $2^{x+1}\\le 32$ by rewriting as powers of the same base and comparing exponents; then solve $\\left(1⁄2\\right)^{x}<8$ and show the inequality direction FLIPS because the base is between 0 and 1.",
      "Whole class, REI.A.1 (Objective 2): solve $\\log_2(x+3)=4$ by exponentiating; then $\\log_3 x+\\log_3(x-2)=1$ by condensing first, factoring, and REJECTING the extraneous root $x=-1$ that fails the domain; then the inequality $\\log_5(x-1)\\le 2$, keeping the domain restriction $x>1$ in the final answer.",
      "Whole class, LE.A.4 (Objective 3): $5^{x}=40$ has no common base — take a logarithm of both sides. Then a refinery's emissions model $E(t)=500\\,000(0.9)^{t}$: solve $E(t)=250\\,000$ for $t$ as a logarithm before evaluating it.",
      "Narration focus — after ANY logarithmic equation, go back and check every candidate solution against the ORIGINAL logarithm's domain before accepting it.",
      "This is a NEW example — it does not repeat the flipped video.",
    ],
    quickCheck: [
      "On whiteboards, 90 seconds: solve $3^{x}=50$ for $x$ using a logarithm, to three decimal places.",
      "Expected: $x=(\\log 50)/(\\log 3)\\approx 3.561$. Watch for students who waste time hunting for a common base that does not exist.",
      "80% correct → release guided practice. Below 80% → one further modelled example, this time a logarithmic equation.",
    ],
    guided: [
      "Two “Give it a go” problems, identical for every student, worked together with the teacher:",
      "(1) $\\log_2(x-1)=5$ — solve for $x$.  (2) $6^{x}=200$ — solve for $x$ using a logarithm, to three decimal places.",
      "Answers: (1) $x-1=32 \\to x=33$. (2) $x=(\\log 200)/(\\log 6)\\approx 2.957$.",
      "Feedback: worked live on the board step by step; students self-mark and circle their OWN first error.",
    ],
    independent: [
      "Delivered through the “Choose Your Route” sheet with live feedback in Pear Deck. Routes are named for the task, not for the student.",
      "PRACTICE — Secure the method. Four common-base equations/inequalities solved, one logarithmic equation solved, one exponential equation solved with a logarithm. Done when: every solution checks back in the ORIGINAL equation.",
      "APPLY — Use it in context. A user-growth doubling-time problem, a logarithmic inequality with a domain restriction, and a savings-balance target solved for time. Done when: units and rounding are sensible, and the logarithmic inequality states its domain.",
      "INVESTIGATE — Find out why. Arguing from the range of an exponential function why $2^{x}=-8$ has no solution, checking an unchecked classmate's logarithmic solution against the domain, and proving that $b^{m}=b^{n}\\Rightarrow m=n$. Done when: you have an argument, not just an answer.",
      "Every student sits the same Mastery Gate. The gate is not differentiated, because it is the evidence.",
    ],
    production: [
      "Non-routine transfer task — this context has not appeared in practice.",
      "A refinery participating in the Saudi Green Initiative is cutting its annual carbon emissions by 10% every year. This year's emissions are 500,000 metric tons of CO2, modeled by $E(t)=500\\,000(0.9)^{t}$, where $t$ is years from now.",
      "(a) Set up the equation for when emissions first fall to HALF their current level, and solve for $t$ as a logarithm before evaluating it. (b) State the first WHOLE year the target is met, with a justification for the rounding. (c) The board wants emissions below 150,000 tons (30% of current) within 12 years — solve the inequality to check. (d) A board member says “just divide 500,000 by 10 — it hits zero in 10 years.” Explain in one sentence why this is wrong for a percentage-based model.",
      "Answers: (a) $(0.9)^{t}=0.5 \\to t=(\\log 0.5)/(\\log 0.9)\\approx 6.579$. (b) year 7 (at $t=6$, $E\\approx 265\\,720$; at $t=7$, $E\\approx 239\\,150$, the first whole year below half). (c) $(0.9)^{t}<0.30 \\to t>(\\log 0.30)/(\\log 0.9)\\approx 11.43$, so YES, the 12-year goal is met (at $t=12$, $E\\approx 141\\,000$ tons). (d) a percentage reduction is not a fixed amount — 10% of a shrinking total shrinks too, so the model approaches but never exactly reaches zero, unlike a fixed 50,000-ton yearly cut.",
      "Students then hand their reasoning to the AI critic and ask it to challenge any step they have not justified.",
    ],
    criteria: [
      "Minimum acceptable standard: the logarithmic expression for $t$ shown exactly before any decimal is computed, part (c) solved as an inequality (not just a yes/no guess), and a written reason for part (d).",
      AI_CRITIC,
      "Completed independently by the student: the written justification for parts (b) and (d). AI may challenge it; it may not write it.",
    ],
    evidence: [
      "“Time to Check” — one individual task. No notes, no partner, no AI.",
      "1. Solve $5^{2x-1}=125$. 2. Solve $\\log_4(x+5)=3$, checking the domain. 3. In ONE sentence, explain why $7^{x}=15$ needs a logarithm to solve, while $2^{x}=8$ does not.",
      "Answers: 1. $125=5^{3} \\to 2x-1=3 \\to x=2$. 2. $x+5=64 \\to x=59$; domain check $64>0$, valid. 3. because $15$ is not a whole-number power of $7$, so the exponent must be found with a logarithm, while $8=2^{3}$ already is a whole-number power of $2$.",
      "Done when: question 2 shows the domain check explicitly, and question 3 gives a definition-based reason, not an example alone.",
      "Scored live in Pear Deck as submissions arrive; result logged in the Impact Dashboard Mastery Rate.",
    ],
    refinement: [
      "Students revise their emissions-model reasoning using the AI critique and the teacher's micro-conference note.",
      "Final product, three equally acceptable formats: a Canva one-pager, a photographed hand-written solution, or a 45-second voice note.",
      "Required content: the halving equation solved as a logarithm before evaluating, the year stated with justification, the 12-year inequality check, and ONE worked non-example — treating the 10% cut as a fixed 50,000-ton drop — with a sentence on how a reader would spot it.",
      "Graded on originality and clarity of reasoning, not correctness alone.",
    ],
    publication: [
      "Published to the class LMS portfolio; the strongest go on the Mathematics Department wall as the Topic 6 modelling set.",
      "Reflection question: “Which is still harder for you — knowing WHEN to use a logarithm instead of matching bases, or checking a logarithmic equation's domain?”",
    ],
    differentiation: [
      "PRACTICE — Secure the method. Four common-base equations/inequalities, one logarithmic equation, one exponential equation solved with a logarithm; a partner is allowed. Done when: every solution checks back in the original equation.",
      "APPLY — Use it in context. The user-growth doubling time, a logarithmic inequality with domain, and the savings-balance target. Done when: units and rounding are sensible and the domain is stated.",
      "INVESTIGATE — Find out why. The no-real-solution argument, the unchecked-domain scenario, and the $b^{m}=b^{n}\\Rightarrow m=n$ proof. Done when: there is an argument, not just an answer.",
      "No student is labelled. The routes describe tasks; every student sits the same Mastery Gate.",
    ],
    adaptive: PILLAR_ADAPTIVE,
    saudi: [
      "Production context: a Saudi Green Initiative refinery's 10%-per-year emissions reduction, modeled exponentially and solved with logarithms for a regulatory target.",
      "In-class Apply-route item: a Jeddah startup's monthly user growth, solved for its doubling time using a logarithm.",
      "Discussion prompt: why a percentage-based reduction never behaves like a fixed yearly amount, using the emissions model as evidence.",
    ],
    exams: [
      "GAT (Qudurat) — a quick common-base exponential equation, solved mentally without a calculator. Practice tip: rewrite the number on the right as a power of the same base first.",
      "SAAT (Tahsili) — a one-logarithm equation, exponentiated directly. Practice tip: exponentiate both sides using the logarithm's own base.",
      "SAT — Advanced Math, an exponential equation with no common base, solved with logarithms — a recurring item type. Practice tip: take $\\log$ or $\\ln$ of both sides and divide, never guess a decimal base by trial and error.",
    ],
  },

  plan2026: {
    day: "Thursday, Week 8", section: "Grade 11-B",
    tools: "Quizizz (diagnostic) · Pear Deck (live practice feedback) · GeoGebra Graphing Calculator · Canva (final product) · Whiteboards",
    resources: "Lesson presentation (18 slides) · “Choose Your Route” differentiation sheet · “Meeting a Green Initiative Target” project task · squared paper",
    competencies: ["Solving an exponential equation or inequality by common base, including when the direction flips.", "Solving a logarithmic equation or inequality by condensing, exponentiating, and checking the domain."],
    technology: ["Quizizz live diagnostic with instant gap analysis.", "GeoGebra slider showing an exponential curve tip from rising to falling as its base crosses 1."],
    reallife: ["A Saudi Green Initiative refinery's annual emissions-reduction target, solved with logarithms.", "A Jeddah startup's monthly active-user growth and its doubling time."],
    values: ["Rigor — checking every logarithmic solution against its domain before accepting it.", "Precision — distinguishing a percentage-based change from a fixed amount."],
    soft: ["Collaboration in assigned group roles.", "Explaining why a logarithmic solution can be extraneous."],
    hard: ["Solving exponential and logarithmic equations and inequalities by common base and by logarithm properties.", "Using a logarithm to solve an exponential model with no common base."],
    phases: [
      "FIKR Phase 1 — Diagnose. 5-question Quizizz on common base, the inverse property, condensing logarithms, change of base, and a linear inequality. Results read as a gap map; students routed to the re-teach table, straight to solving equations, or the Investigate prompt.",
      "FIKR Phase 2 — Targeted Instruction. Focused re-teach on the inverse property and condensing for flagged students. Whole class: common-base equations and inequalities (including the direction flip); logarithmic equations and inequalities with domain checks; using a logarithm when no common base exists. Quick check on whiteboards.",
      "FIKR Phase 3 — Practice. Two identical “Give it a go” problems worked together. Students then choose a route and may switch at any time. Live feedback via Pear Deck; 2-minute micro-conferences.",
      "FIKR Phase 4 — Production. The Green Initiative emissions model: the halving equation solved as a logarithm, the year justified, and the 12-year inequality checked. AI used as critic only.",
      "FIKR Phase 5 — Proof of Learning. “Time to Check” — a common-base equation, a logarithmic equation with a domain check, and a one-sentence justification. No notes, no partner, no AI.",
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
    closure: "Two minutes of peer show-and-tell on the final products, then the reflection question: “Which is still harder for you — knowing WHEN to use a logarithm instead of matching bases, or checking a logarithmic equation's domain?”",
    homework: "Finish the final product and upload to the LMS portfolio (any of the three formats). Practice set on Pear Deck — 12 questions, choose your route. This closes Topic 6 — the Topic Recap and Unit Assessment follow next session, not a new flipped video.",
  },

  // Minimal stub — classwork is NOT requested this round; this file is
  // deleted immediately after build and never delivered.
  classwork: {
    subtitle: "Not delivered this round.",
    sections: [
      { h: "SECTION 1", note: "placeholder — not delivered", lines: 2,
        q: [{ n: "Q1", eq: "e_ws1", t: "Solve." }] },
    ],
  },

  diffSheet: {
    routes: [
      { note: "Common base, and one logarithm", done: "every equation solution checks back in the ORIGINAL equation, and your logarithm answer is rounded only at the very last step.",
        intro: "Solve each equation or inequality by common base, unless a logarithm is asked for.",
        grid: [["1.", "e_ws1"], ["2.", "e_ws2"], ["3.", "e_ws3"], ["4.", "e_ws4"], ["5.", "e_ws5"], ["6.", "e_g2"]],
        tasks: ["7.  Solve $7^{x}=90$ using a logarithm, to three decimal places, and check your answer with a calculator power."],
        lines: 2 },
      { note: "Contexts, and a logarithmic inequality", done: "your month/year answer is rounded to a sensible whole unit, and your logarithmic inequality states BOTH the domain restriction and the solved inequality.",
        graph: "g_emissions", graphW: 380,
        tasks: [
          "1.  A Jeddah startup's active users grow 8% a month: $U(t)=U_{0}(1.08)^{t}$. Find, to two decimal places, how many months until the user base DOUBLES.",
          "2.  Solve the inequality $\\log_3(x-4)<2$, stating the domain restriction as part of your final answer.",
          "3.  A savings account follows $B(t)=2000(1.05)^{t}$ SAR. Find how many years until the balance exceeds 3000 SAR.",
          "4.  Using the graph shown, confirm the emissions model's halving time to the nearest tenth of a year.",
        ], lines: 4 },
      { note: "Arguments, not answers", done: "you have an argument, not just an answer.",
        tasks: [
          "1.  Explain why $2^{x}=-8$ has no real solution, using the RANGE of an exponential function.",
          "2.  A classmate solves $\\log_5(x-3)=2$ and gets $x=28$ without checking the domain. Confirm whether $x=28$ is valid, and explain why checking mattered here.",
          ["3.  Prove that if ", { eq: "e_prior_base", k: 0.95 }, " for $b>0,\\ b\\ne 1$, using the fact that $y=b^{x}$ is one-to-one."],
        ], lines: 5 },
    ],
  },

  pbl: {
    title: "Meeting a Green Initiative Target", minutes: 20,
    subtitle: "A 20-minute group project. Work in fours. Every member signs the sheet.",
    driving: "A refinery is cutting emissions by a PERCENTAGE every year, not a fixed amount. When will it actually hit its target — and can a board member's quick mental estimate be trusted?",
    situation: [
      "A refinery participating in the Saudi Green Initiative is cutting its annual carbon emissions by 10% every year. This year's emissions are 500,000 metric tons of CO2.",
      "The model is $E(t)=500\\,000(0.9)^{t}$, where $t$ is years from now.",
      "A group of Grade 11 students is asked to find exactly when two regulatory targets are met.",
    ],
    eq: "e_model",
    steps: [
      ["1", "SET UP THE HALVING EQUATION  (4 min)", "Set $E(t)=250\\,000$ and solve for $t$, expressing your answer as a logarithm before evaluating it."],
      ["2", "STATE THE YEAR  (3 min)", "Round appropriately and state the first WHOLE year emissions fall below half, with a one-sentence justification."],
      ["3", "CHECK THE 12-YEAR GOAL  (5 min)", "Solve the inequality $(0.9)^{t}<0.30$ algebraically to check whether the 150,000-ton goal is met within 12 years."],
      ["4", "FIND THE TRAP  (4 min)", "A board member says “just divide 500,000 by 10 — it hits zero in 10 years.” Explain in one sentence why this is wrong."],
      ["5", "PRESENT  (4 min)", "Prepare one sentence your presenter will say: why an exact logarithm beats a quick mental guess here."],
    ],
    working: [["Step 1 — the halving equation, solved:", 3], ["Step 2 — the year, justified:", 2],
              ["Step 3 — the 12-year check:", 3], ["Step 4 — the board member's error:", 3],
              ["Step 5 — our sentence:", 2]],
    roles: ["Reader — states the emissions model", "Calculator — runs both logarithm calculations", "Checker — verifies the 12-year inequality", "Presenter — says the sentence"],
    doneWhen: ["The halving time is expressed as a logarithm before it is evaluated.", "The stated year carries a reason for the rounding direction.", "The 12-year check is a solved inequality, not a guess.", "Your sentence makes sense to someone who does not study maths."],
    materials: ["This sheet", "Squared paper", "A pencil and ruler", "A calculator"],
  },
};

(async () => {
  await buildAll(GR11_L66);
  // The docx engine writes output next to itself (engines/), not the CWD
  // this script was invoked from.
  const cwFile = require("path").join(__dirname, "../../engines", `Classwork_${GR11_L66.slug}.docx`);
  if (fs.existsSync(cwFile)) fs.unlinkSync(cwFile);
})();

module.exports = { GR11_L66 };
