// ---------------------------------------------------------------------------
// SIMULATED GAT (QUDURAT) QUESTION BANK — 100 items
//
// WHAT THIS IS. Five of Mr Tamer Elsawy's departmental practice sets (parts 6, 8
// and 10, Set C and Set D) were transcribed from Mr Thiab's screen recordings.
// Across those six sets there are 156 items but only 142 distinct SKILLS: the
// rest repeat a skill and a trick that another item already covers. This bank
// keeps one item per skill and REWRITES every one of them from scratch —
// new numbers, new names, new Saudi contexts, new distractor values, and new
// figures. No question here reproduces the wording of a source item.
//
// WHY THAT MATTERS BEYOND DEDUPLICATION. Because nothing is transcribed, this
// bank is Mr Thiab's own material. It can be set, printed and shared without
// the department-internal restriction that governs the four transcription
// banks, which stay credited to Mr Elsawy.
//
// TWO GUARDS RUN AT BUILD TIME.
//   1. No two items may share a `sig` (its skill-and-trick signature). That is
//      the "no repeated questions" rule, enforced rather than promised.
//   2. Every figure places its labels through figlabel.py, which measures each
//      label's rendered box and refuses to ship one that sits on the drawing.
//
// All answers were re-derived independently in Python before release
// (verify_sim.py, 0 failures).
// ---------------------------------------------------------------------------
const { buildSet } = require("./exam_engine");
const ITEMS = [...require("./sim_items_a.js"), ...require("./sim_items_b.js"),
               ...require("./sim_items_c.js"), ...require("./sim_items_d.js"),
               ...require("./sim_items_e.js"), ...require("./sim_items_f.js"), ...require("./sim_items_g.js"), ...require("./sim_items_h.js"),
               ...require("./sim_items_i.js"),
               ...require("./sim_items_j.js"),
               ...require("./sim_items_k.js"),
               ...require("./sim_items_l.js"),
               ...require("./sim_items_m.js"),
               ...require("./sim_items_n.js"),
               ...require("./sim_items_o.js")];

const seen = new Map();
for (const it of ITEMS) {
  if (!it.sig) throw new Error("item carries no skill signature: " + it.stem.slice(0, 50));
  if (seen.has(it.sig))
    throw new Error(`two items share the skill "${it.sig}" — one of them is a repeat:\n` +
                    `  1) ${seen.get(it.sig).slice(0, 70)}\n  2) ${it.stem.slice(0, 70)}`);
  seen.set(it.sig, it.stem);
  if (!it.trick) throw new Error("no trick recorded for " + it.sig);
  if (!it.traps || it.traps.length !== 3)
    throw new Error("an item needs exactly three distractor notes: " + it.sig);
}

const tally = {};
for (const it of ITEMS) {
  const s = it.code.split(".")[0];
  tally[s] = (tally[s] || 0) + 1;
}
const pct = (k) => Math.round((tally[k] / ITEMS.length) * 100);

const CFG = {
  mathIndex: "math_sim_doc/_index.json",
  figIndex: "figs_sim/_index.json",
  examName: "GAT (Qudurat) question bank",
  targets: { "GAT-Q-ARI": "~36%", "GAT-Q-ALG": "~18%", "GAT-Q-GEO": "~18%",
             "GAT-Q-DAT": "~18%", "GAT-Q-LOG": "~10%" },
  dense: true, itemGap: 55,
  marking: "Two points each",
  budgetNote:
    `${ITEMS.length} items, one per distinct GAT sub-skill, each written fresh for this bank. ` +
    `The mix is ARI ${pct("GAT-Q-ARI")}%, ALG ${pct("GAT-Q-ALG")}%, ` +
    `GEO ${pct("GAT-Q-GEO")}%, DAT ${pct("GAT-Q-DAT")}%, LOG ${pct("GAT-Q-LOG")}% — ` +
    `close to the ETEC blueprint on algebra and geometry, light on data and heavy ` +
    `on word logic, because that is the shape of the department sets these skills ` +
    `were drawn from. Build a mock by sampling to the blueprint, not by taking the ` +
    `first forty items.`,
  compareNote:
    "COMPARISON QUESTIONS.  Some questions give you two quantities, A and B, and ask which is greater. Answer (A) if A is greater, (B) if B is greater, (C) if the two are exactly equal, and (D) if what you are given is not enough to decide. Both (C) and (D) are real answers on this bank: (C) is correct wherever a comparison turns out to be a disguised identity, and (D) wherever no sign is fixed for a letter. Neither is a way out.",
  conditions: "No calculator, no phone, no smartwatch. Two points per item. If an item is taking more than about 70 seconds, mark it and move on.",
  sourceNote:
    "These questions are ORIGINAL to this bank. They were written to match, skill for skill and trick for trick, the department's own GAT practice sets, but no wording, number set or figure is reproduced from them. That means this bank may be set, printed and shared freely; the four transcription banks (parts 8 and 10, Set C, Set D) remain department-internal and credited to Mr Tamer Elsawy. Every answer below was re-derived independently in Python before release, and every figure's labels were placed by a routine that refuses to let a variable or an angle sit on the drawing.",
  weekLine: "Question bank · Semester 1, 2026–27",
  headerLine: `GAT (Qudurat) · Quantitative Reasoning · simulated question bank · ${ITEMS.length} items, one per sub-skill`,
  paperTitle: "GAT Question Bank — Simulated Set",
  paperSub: `${ITEMS.length} original questions, one for every distinct sub-skill in the department sets. Two points each.`,
  keyTitle: "GAT Simulated Bank — Answer Key and Error Analysis",
  keySub: "For Mr Malek Thiab. Every answer re-derived from scratch; each item names the trick it is built on.",
  outPaper: "GAT_Bank_Simulated_Paper.docx",
  outKey: "GAT_Bank_Simulated_Key.docx",
  timing: "Two hours for the whole bank, or 25 minutes for any block of twenty",
  followUp: [
    ["100 or more", "Working at the target band across the whole blueprint. Move to timed forty-item mocks."],
    ["70 to 99", "Check WHICH strand the losses sit in — the strand column in this key names it for every item."],
    ["Below 70", "Take the arithmetic block alone, untimed. ARI is over a third of the real test."],
    ["Whole class", "Any item where more than half the class chose the SAME wrong option is a teaching point, not a marking point."],
  ],
  items: ITEMS,
};

module.exports = { SIM: CFG };

if (require.main === module) {
  (async () => {
    await buildSet(CFG);
    console.log("  skills:", ITEMS.length, "| strands:", JSON.stringify(tally));
  })();
}
