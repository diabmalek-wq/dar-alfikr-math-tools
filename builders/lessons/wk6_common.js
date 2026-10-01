const ASSESS = ["“Give it a go” questions", "“Time to Check”"];
const T = { t1: 6, t2: 18, t3: 12, t4: 12, t5: 6, t6: 6 };
const AI_CRITIC = "Role of AI: critic only. Briefed prompt — “Challenge my reasoning and point out any step I have not justified.” Never “solve this”.";
const PILLAR_ADAPTIVE = [
  "Entry branch — the Quizizz result routes each student to the re-teach table, straight to the new content, or the Investigate prompt.",
  "Mid-lesson branch — Pear Deck flags error patterns during independent practice; flagged students get a 2-minute micro-conference while others continue.",
  "Exit branch — the Mastery Gate routes each student: PASS → Enrichment & Challenge; NOT YET → Targeted Learning Clinic at the start of the next lesson.",
  "Routing is communicated privately through the LMS, never read aloud.",
];
const WEEK_NOTE = "Three teaching days this week. If time runs short, cut Smart Production and carry it into the next session — never the Mastery Gate, which is the evidence.";
const PHASE_STD = {
  assessment: [
    "Diagnostic quiz — gap map, not a grade.",
    "Quick check for understanding on whiteboards (80% threshold).",
    "“Give it a go” questions — self-marked, teacher circulates.",
    "Project task sheet against its “Done when…” criteria.",
    "“Time to Check” — Mastery Gate, scored live. PASS → Enrichment & Challenge. NOT YET → Targeted Learning Clinic next lesson.",
    "Final product graded on reasoning and clarity, not correctness alone.",
  ],
};
const STUB = (key) => ({ subtitle: "Not delivered this round.", sections: [{ h: "SECTION A", note: "placeholder — not delivered", lines: 2, q: [{ n: "Q1", eq: key, t: "Placeholder." }] }] });
module.exports = { ASSESS, T, AI_CRITIC, PILLAR_ADAPTIVE, WEEK_NOTE, PHASE_STD, STUB };
