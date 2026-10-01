// Week 6 · Gr11 · T6 L6-3 Logarithms — plan, Lesson plan 2026/27, differentiation, PBL.
// Derived from lessons_w6l3.js (the deck): same objectives, same worked numbers, same production context.
const { ASSESS, T, AI_CRITIC, PILLAR_ADAPTIVE, WEEK_NOTE, PHASE_STD, STUB } = require("./wk6_common");

const GR11_L63 = {
  slug: "Wk6_Gr11_T6_L6-3_Logarithms",
  mathDocIndex: "math_wk6_doc/_index.json", graphIndex: "graphs_wk6/_index.json", timings: T,
  lessonTitle: "Logarithms",
  unit: "Topic 6 — Exponential and Logarithmic Functions · Lesson 6-3",
  gradeFull: "Grade 11 — Algebra II",
  week: "Week 6 · Semester 1, 2026–27", weekNum: "6",
  lessonLine: "Grade 11 · Algebra II · Topic 6: Exponential and Logarithmic Functions · Lesson 6-3 — Logarithms",
  codes: ["HSF.BF.B.4.A", "HSF.BF.B.5", "HSF.LE.A.4"], mps: ["MP.2", "MP.5"],
  assessments: ASSESS,
  objectives: [
    "Understand and evaluate logarithms.",
    "Analyze common logarithms and natural logarithms.",
    "Convert between exponential and logarithmic forms.",
    "Use logarithms to solve problems involving exponential models.",
    "Evaluate logarithms using technology.",
  ],
  essentialQuestion: "How can we use logarithms and relate them to exponents?",
  vocabList: "logarithm ; common logarithm ; natural logarithm ; logarithmic function ; order of magnitude",

  plan: {
    outcome: [
      "Students will explain a logarithm as the exponent that produces a number, and convert between exponential and logarithmic form (objectives 1 and 3).",
      "Students will tell a common logarithm (base 10) from a natural logarithm (base e), evaluate both with technology, and use log N to state an order of magnitude (objectives 2 and 5).",
      "Students will solve an exponential model for an unknown time by isolating the power and taking a logarithm (objective 4).",
      "Note: Lesson 6-2 is not taught in the department’s Curriculum Distribution, so this lesson follows Lesson 6-1 directly and does not use 6-2 as a prerequisite.",
      WEEK_NOTE,
    ],
    preclass: [
      "Flipped video (4 min): “The question exponentials couldn’t answer” — reading 2ˣ = 8 backwards, and why 2ˣ = 20 needs a new tool. Posted on the LMS 48 hours ahead.",
      "Two embedded EdPuzzle questions: one evaluation of bˣ, one solve-by-inspection.",
      "Evidence of readiness: EdPuzzle completion report plus both embedded answers submitted before the bell.",
    ],
    diagTool: [
      "5-question Quizizz (≤ 4 minutes) — the slide-5 warm-up: 2⁵ ; 10³ ; f(x) = 2(3)ˣ, find f(0) ; solve 2ˣ = 16 ; between which two integers is log₂ 20.",
      "Cross-referenced against overnight EdPuzzle watch analytics — who watched, who skipped, who missed the embedded items.",
      "Answers: 32 ; 1000 ; f(0) = 2 ; x = 4 ; between 4 and 5, since 2⁴ = 16 and 2⁵ = 32.",
    ],
    diagGap: [
      "Expected gap 1 — evaluating bˣ directly (questions 1–3). A student who cannot do this cannot check any logarithm they compute.",
      "Expected gap 2 — Q5: students want an exact integer and have no language for “between two values”. This is the motivation for the whole lesson, not a failure.",
      "Routing: 0–2 correct → re-teach exponent basics with the teacher.  3–4 → straight to the definition.  5 → begin the Investigate prompt immediately.",
    ],
    instruction: [
      "Slide 6 — Understanding and evaluating logarithms (objectives 1 and 3). log_b x = y is always asking “b to what power gives x?”. Conversion rule: b^y = x ⟺ log_b x = y. Worked: log₂ 8 = 3 because 2³ = 8; log_b 1 = 0 for every valid base; log_b x is undefined for x ≤ 0.",
      "Slide 7 — Common and natural logarithms (objectives 2 and 5). log x with no base means base 10; ln x means base e ≈ 2.71828. On a calculator log 50 ≈ 1.699 and ln 50 ≈ 3.912. Order of magnitude: log(6.3 × 10⁸) ≈ 8.8, so about 10⁹.",
      "Slide 8 — Logarithms and exponential models (objective 4). A culture starts at 5 and doubles each hour: 5·2ᵗ = 40 → 2ᵗ = 8 → t = log₂ 8 = 3 hours. General pattern: A = A₀·bᵗ gives t = log_b(A/A₀).",
      "Narration focus — convert and check the exponential form BEFORE naming the rule. Say aloud the misconception that a student can “cancel” the base and the log like factors.",
      "This is a NEW example — it does not repeat the flipped video.",
    ],
    quickCheck: [
      "On whiteboards, 60 seconds: evaluate log₃ 27.",
      "Expected: 3, since 3³ = 27. Watch for 9 (computing 3 × 3) and 24 (subtracting).",
      "80% correct → release guided practice. Below 80% → one more modelled example, this time a common logarithm.",
    ],
    guided: [
      "Two “Give it a go” problems, identical for every student, worked together with the teacher:",
      "(1) log₂ 32, then check by rewriting in exponential form.  (2) log₁₀ 10 000 — a common logarithm.",
      "Answers: (1) 5, since 2⁵ = 32.  (2) 4, since 10⁴ = 10 000 (count the zeros).",
      "Feedback: worked live on the board step by step; students self-mark and circle their OWN first error.",
    ],
    independent: [
      "Delivered through the “Choose Your Route” sheet with live feedback in Pear Deck. Routes are named for the task, not for the student.",
      "PRACTICE — Secure the method. Four logarithms evaluated by converting to exponential form, each labelled common, natural or neither, then log 50 and ln 50 on a calculator. Done when: every logarithm you evaluated checks out in exponential form.",
      "APPLY — Use it in context. 6ˣ = 216 and log₄ x = 3 solved by converting, then a Vision 2030 desalination tank growing 18% a year: equation set up BEFORE the calculator. Done when: your equation is set up before you touch a calculator, and your final answer carries units (years).",
      "INVESTIGATE — Find out why. Why a logarithm is undefined for x ≤ 0, why log 50 and ln 50 differ, and a proof that log_b(bᵏ) = k. Done when: you have an argument grounded in the definition, not just a computed answer.",
      "Every student sits the same Mastery Gate. The gate is not differentiated, because it is the evidence.",
    ],
    production: [
      "Non-routine transfer task — this context has not appeared in practice (slide 14).",
      "A Jeddah desalination reservoir holds 500 000 m³ and usage is draining it by 4% a week (decay factor 0.96).",
      "(a) Write V(t). (b) Set up the equation for the weeks until the volume reaches 300 000 m³ — do not solve yet. (c) Solve for t using logarithms, to one decimal place, with units. (d) A colleague says “just divide 500 000 by 300 000.” Explain in one sentence why this skips the step that answers the question.",
      "Answers: (a) V(t) = 500 000(0.96)ᵗ. (b) 500 000(0.96)ᵗ = 300 000. (c) 0.96ᵗ = 0.6, so t = log 0.6 ÷ log 0.96 ≈ 12.5 weeks. (d) the division only finds the ratio (≈ 1.67); the logarithm is what counts how many 4% shrinkages produce that ratio.",
      "Students then hand their reasoning to the AI critic and ask it to challenge any step they have not justified.",
    ],
    criteria: [
      "Minimum acceptable standard: the exact equation written before any decimal, the unit named (m³, weeks), and the equation set up before it is solved.",
      AI_CRITIC,
      "Completed independently by the student: the written justification for parts (a)–(d). AI may challenge it; it may not write it.",
    ],
    evidence: [
      "“Time to Check” — one individual task. No notes, no partner, no AI.",
      "1. Evaluate the logarithm shown (log₅ 125). 2. Rewrite it in exponential form. 3. In ONE sentence, explain what a logarithm is, in terms of exponents.",
      "Answers: 1. 3. 2. 5³ = 125. 3. a logarithm is the exponent you need on a given base to produce a given number.",
      "Done when: answers are exact, question 2 is a full equation, and question 3 is a definition, not an example.",
      "Scored live in Pear Deck as submissions arrive; result logged in the Impact Dashboard Mastery Rate.",
    ],
    refinement: [
      "Students revise their reservoir reasoning using the AI critique and the teacher’s micro-conference note.",
      "Final product, three equally acceptable formats: a Canva one-pager, a photographed hand-written solution, or a 45-second voice note.",
      "Required content: V(t), the equation set up for the target volume, and the solved number of weeks; ONE worked non-example — dividing the two volumes and stopping — with a sentence saying what that shortcut actually computes; and a caption on why a water utility needs to know WHEN, not just by how much.",
      "Graded on originality and clarity of reasoning, not correctness alone.",
    ],
    publication: [
      "Published to the class LMS portfolio; the strongest go on the Mathematics Department wall as the Topic 6 modelling set.",
      "Reflection question: “Which direction is still harder for you — evaluating a logarithm you’re given, or setting one up from a word problem yourself?”",
    ],
    differentiation: [
      "PRACTICE — Secure the method. Four logarithms converted to exponential form and labelled common, natural or neither; log 50 and ln 50 by calculator. Done when: every logarithm checks out in exponential form.",
      "APPLY — Use it in context. 6ˣ = 216 and log₄ x = 3, then the desalination tank. Done when: the equation is set up before the calculator and the answer carries years.",
      "INVESTIGATE — Find out why. Why log is undefined for x ≤ 0, why log 50 ≠ ln 50, and a proof of log_b(bᵏ) = k. Done when: there is an argument grounded in the definition.",
      "No student is labelled. The routes describe tasks; every student sits the same Mastery Gate.",
    ],
    adaptive: PILLAR_ADAPTIVE,
    saudi: [
      "Production and project context: a Jeddah desalination reservoir draining 4% a week, with a warning line to plan for — Kingdom water-security planning.",
      "Apply-route item: a Vision 2030 desalination storage tank growing 18% a year — years to reach 50 000 litres.",
      "Discussion prompt: why a water utility needs to know WHEN a level will be reached, not just by how much it has fallen.",
    ],
    exams: [
      "SAAT (Tahsili) — if log₄ x = 3, find log₂ x (answer 6: find x = 64 first). No calculator.",
      "SAT — Advanced Math: V = 500(1.06)ᵗ, which expression gives the years to reach 1000? (answer log base 1.06 of 2: divide by 500 before converting).",
      "GAT (Qudurat) — compare log₂ 64 and log₃ 243 (6 against 5): the base decides the exponent, not the size of the number. About 75 seconds, no calculator.",
    ],
  },

  plan2026: {
    day: "Week 6 · day per timetable", section: "Grade 11 — 11B",
    tools: "Quizizz (diagnostic) · Pear Deck (live practice feedback) · GeoGebra Graphing Calculator · Calculator (LOG, LN keys) · Canva (final product) · Whiteboards",
    resources: "Lesson presentation (18 slides) · “Choose Your Route” differentiation sheet · “When Does the Reservoir Run Low?” project task (A3) · squared paper",
    competencies: ["Reading a logarithm as an exponent and converting between the two forms.", "Choosing between a common and a natural logarithm and evaluating each with technology."],
    technology: ["Quizizz live diagnostic with instant gap analysis.", "GeoGebra: slide the base b and watch y = bˣ fold into its logarithm across y = x."],
    reallife: ["A desalination reservoir draining by a fixed percentage each week.", "A storage tank growing 18% a year — when does it reach its target?"],
    values: ["Precision — setting the equation up before reaching for a calculator.", "Stewardship — planning for a scarce resource such as water."],
    soft: ["Collaboration in assigned group roles.", "Explaining a method in words so a non-mathematician follows it."],
    hard: ["Evaluating and converting logarithms; using LOG and LN.", "Solving an exponential model for time."],
    phases: [
      "FIKR Phase 1 — Diagnose. 5-question Quizizz: powers, f(0), 2ˣ = 16, bracketing log₂ 20. Gap map; routed to re-teach, the definition, or Investigate.",
      "FIKR Phase 2 — Targeted Instruction. Re-teach exponents (flagged). Whole class: logarithm as exponent; common and natural logs; growth model solved for time. Whiteboard check.",
      "FIKR Phase 3 — Practice. Two identical “Give it a go” problems worked together. Students then choose a route and may switch at any time. Live feedback via Pear Deck; 2-minute micro-conferences.",
      "FIKR Phase 4 — Production. The desalination reservoir: V(t), the equation set up, the solved week, and why dividing the volumes is not the answer. AI used as critic only. Extended in the A3 project task.",
      "FIKR Phase 5 — Proof of Learning. “Time to Check” — evaluate, rewrite in exponential form, define in one sentence. No notes, no partner, no AI.",
      "FIKR Phase 6 — Smart Production. Students refine their reasoning into a final product including one worked non-example, and publish to the LMS portfolio.",
    ],
    assessment: PHASE_STD.assessment,
    closure: "Two minutes of peer show-and-tell on the final products, then the reflection question: “Which direction is still harder for you — evaluating a logarithm you’re given, or setting one up from a word problem yourself?”",
    homework: "Finish the final product and upload to the LMS portfolio (any of the three formats). Practice set on Pear Deck — 12 questions, choose your route. Watch the flipped video for the next lesson, Topic 6 · Lesson 6-4 — Logarithmic Functions. Clinic group: bring your Time to Check paper.",
  },

  classwork: STUB("k_l3a"),

  diffSheet: {
    routes: [
      { note: "Convert it, check it", done: "every logarithm you evaluated checks out in exponential form.",
        intro: "Evaluate items 1–4 by writing the exponential form first. Items 5–6: use a calculator, three decimal places.",
        grid: [["1.", "l_ws1"], ["2.", "l_ws2"], ["3.", "k_l3a"], ["4.", "k_l3b"], ["5.", "k_l3c"], ["6.", "k_l3d"]],
        tasks: ["7.  State whether each of items 1–6 is a common logarithm, a natural logarithm, or neither.",
                "8.  Check every answer against its exponential form before moving on."],
        lines: 3 },
      { note: "Solve it, then one real context", done: "your equation is set up BEFORE you touch a calculator, and your final answer carries units (years).",
        tasks: [
          ["1.  Solve ", { eq: "l_ws3", k: 1.0 }, " by converting to a logarithm."],
          ["2.  Solve ", { eq: "l_ws4", k: 1.0 }, " by converting to exponential form."],
          "3.  A Vision 2030 desalination plant’s storage tank holds 6 000 litres and grows 18% a year. Set up the equation for the years to reach 50 000 litres — do NOT solve yet.",
          "4.  Now solve it with a calculator, to one decimal place, and state the units.",
        ], lines: 4 },
      { note: "Arguments, not answers", done: "you have an argument grounded in the definition, not just a computed answer.",
        tasks: [
          ["1.  Explain why ", { eq: "k_logb", k: 1.0 }, " is undefined for x ≤ 0 — argue from what a logarithm MEANS, not “the calculator gives an error”."],
          "2.  A classmate says log 50 and ln 50 must be equal because they are “both logarithms of 50”. Say what is wrong, using the two different bases.",
          ["3.  Show that ", { eq: "k_logbk", k: 1.0 }, " for any valid base b and any k, and explain why it must always be true."],
        ], lines: 5 },
    ],
  },

  pbl: {
    title: "When Does the Reservoir Run Low?", minutes: 20,
    subtitle: "A 20-minute group project. Work in fours. Every member signs the sheet.",
    driving: "A reservoir loses 4% of its water every week. How long can the water authority wait before the level reaches a warning line — and why is dividing the two volumes not the answer?",
    situation: [
      "A Jeddah desalination reservoir holds 500 000 m³. Usage drains it by 4% a week, so each week keeps 0.96 of the week before.",
      "The authority must plan restrictions before the volume reaches certain warning lines.",
      "A colleague suggests: “just divide 500 000 by the warning volume.”",
    ],
    eq: "k_l3p",
    data: [["t (weeks)", "0", "5", "10", "15", "20"], ["V(t)  (m³)", "500 000", "", "", "", ""]],
    steps: [
      ["1", "WRITE THE MODEL  (3 min)", "Write V(t) (given above), and say in words what 500 000 and 0.96 mean."],
      ["2", "BUILD THE TABLE  (4 min)", "Fill in V(t) for t = 5, 10, 15 and 20 in the table. Round to the nearest m³."],
      ["3", "SET UP, THEN SOLVE  (6 min)", "Find the weeks until the reservoir reaches 400 000, 300 000 and 250 000 m³, to one decimal place. Write each equation BEFORE you use a calculator."],
      ["4", "TEST THE SHORTCUT  (4 min)", "Work out 500 000 ÷ 300 000. What does that number measure, and why is it not the number of weeks? Use your table to show your answer for 300 000 m³ sits between t = 10 and t = 15."],
      ["5", "PRESENT  (3 min)", "One sentence for the authority: by which week must restrictions start if the warning line is 300 000 m³, and why do they need a logarithm to know?"],
    ],
    working: [["Step 1 — the model in words:", 2], ["Step 2 — the table (show one calculation):", 3],
              ["Step 3 — three equations, then three answers:", 5], ["Step 4 — why the ratio is not the weeks:", 3],
              ["Step 5 — our sentence:", 2]],
    roles: ["Reader — states the plan and the warning lines", "Calculator — builds the table", "Checker — substitutes each answer back into V(t)", "Presenter — says the sentence"],
    doneWhen: ["Every equation is written before it is solved.", "Each answer is checked by substituting it back into V(t).", "Units (m³, weeks) appear in every answer.", "Your sentence makes sense to someone who does not study maths."],
    materials: ["This sheet", "Squared paper", "A pencil and ruler", "A calculator with LOG and LN keys"],
  },
};
module.exports = { GR11_L63 };
