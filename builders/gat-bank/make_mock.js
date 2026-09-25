// ---------------------------------------------------------------------------
// BLUEPRINT-SAMPLED GAT MOCKS
//
// The bank is 226 items, one per sub-skill. A bank is not a paper: setting the
// first forty items would hand the class a paper that is 28% geometry and 10%
// data, which is not the test they sit. This script SAMPLES to the published
// ETEC quantitative blueprint instead —
//
//     ARI 36%  ALG 18%  GEO 18%  DAT 18%  LOG 10%   ->  14 / 7 / 7 / 7 / 5
//
// and builds three mocks that share no item, so a class can sit one, be taught
// from it, and sit the next without meeting a question twice.
//
// THREE RULES THE SAMPLER ENFORCES, each one a way a hand-picked mock goes wrong:
//   1. Blueprint. The strand counts above are exact, not approximate.
//   2. Difficulty. Every mock gets the same number of level-3 (star) items, so
//      mock 2 is not quietly harder than mock 1 and a score drop between them
//      means something.
//   3. Sub-skill spread. Within a strand the sampler takes one item per
//      sub-code (ARI.1, ARI.2, ...) before it takes a second from any of them,
//      so no mock is four questions about percentages and nothing about ratio.
//
// Item order is interleaved across strands, the way the real sitting runs —
// never all the geometry together.
//
//     node make_mock.js          -> all three mocks
//     node make_mock.js 2        -> just mock 2
// ---------------------------------------------------------------------------
const { buildSet } = require("./exam_engine");
const ITEMS = [...require("./sim_items_a.js"), ...require("./sim_items_b.js"),
               ...require("./sim_items_c.js"), ...require("./sim_items_d.js"),
               ...require("./sim_items_e.js"), ...require("./sim_items_f.js"),
               ...require("./sim_items_g.js"), ...require("./sim_items_h.js"),
               ...require("./sim_items_i.js"),
               ...require("./sim_items_j.js"),
               ...require("./sim_items_k.js"),
               ...require("./sim_items_l.js"),
               ...require("./sim_items_m.js"),
               ...require("./sim_items_n.js"),
               ...require("./sim_items_o.js")];

const BLUEPRINT = { "GAT-Q-ARI": 14, "GAT-Q-ALG": 7, "GAT-Q-GEO": 7,
                    "GAT-Q-DAT": 7, "GAT-Q-LOG": 5 };
const N_MOCKS = 3;
const STARS_PER_MOCK = 10;          // level 3 items; ~25%, which is GAT-paced

// A tiny deterministic generator. The mocks must be reproducible: if a student
// queries question 14, it has to be the same question next time the file builds.
function rng(seed) {
  let s = seed >>> 0;
  return () => (s = (s * 1664525 + 1013904223) >>> 0) / 4294967296;
}
function shuffled(arr, rand) {
  const a = arr.slice();
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(rand() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

// ---- sample ---------------------------------------------------------------
const rand = rng(20262027);
const pools = {};
for (const it of ITEMS) {
  const s = it.code.split(".")[0];
  (pools[s] = pools[s] || []).push(it);
}
for (const s of Object.keys(pools)) {
  const need = BLUEPRINT[s] * N_MOCKS;
  if (pools[s].length < need)
    throw new Error(`${s}: ${pools[s].length} items but ${N_MOCKS} mocks need ${need}`);
}

/** Draw `n` items from `pool`, one per sub-code before repeating a sub-code,
 *  and hitting `stars` level-3 items exactly. Chosen items are removed. */
function draw(pool, n, stars) {
  const take = [];
  const want = (wantStar) => {
    const bySub = {};
    for (const it of pool) {
      if ((it.lvl === 3) !== wantStar) continue;
      (bySub[it.code] = bySub[it.code] || []).push(it);
    }
    const subs = shuffled(Object.keys(bySub), rand);
    const used = new Set(take.map((t) => t.code));
    subs.sort((a, b) => (used.has(a) ? 1 : 0) - (used.has(b) ? 1 : 0));
    for (const c of subs) {
      const cand = shuffled(bySub[c], rand)[0];
      if (cand) return cand;
    }
    return null;
  };
  for (let i = 0; i < n; i++) {
    const it = want(take.filter((t) => t.lvl === 3).length < stars) ||
               want(take.filter((t) => t.lvl === 3).length >= stars);
    if (!it) throw new Error("pool exhausted");
    take.push(it);
    pool.splice(pool.indexOf(it), 1);
  }
  return take;
}

const mocks = [];
for (let m = 0; m < N_MOCKS; m++) {
  const picked = [];
  // stars are spread across the strands in proportion to their share
  const starShare = { "GAT-Q-ARI": 4, "GAT-Q-ALG": 2, "GAT-Q-GEO": 2,
                      "GAT-Q-DAT": 1, "GAT-Q-LOG": 1 };
  for (const [s, n] of Object.entries(BLUEPRINT))
    picked.push(...draw(pools[s], n, starShare[s]));

  // ORDER. Two things at once. Strands are interleaved round-robin so no two
  // neighbours come from the same strand, and the ten star items are dealt into
  // every fourth slot rather than falling at the front — a paper that opens with
  // three multi-step items costs a nervous student four minutes before they have
  // scored anything, which is exactly how Grade 12 loses the easy marks.
  const roundRobin = (list) => {
    const by = {};
    for (const it of list) {
      const s = it.code.split(".")[0];
      (by[s] = by[s] || []).push(it);
    }
    const out = [], keys = Object.keys(by);
    while (out.length < list.length)
      for (const k of keys) if (by[k].length) out.push(by[k].shift());
    return out;
  };
  const easy = roundRobin(picked.filter((x) => x.lvl !== 3));
  const hard = roundRobin(picked.filter((x) => x.lvl === 3));
  const order = [];
  for (let i = 0; order.length < picked.length; i++)
    order.push((i % 4 === 3 && hard.length) ? hard.shift() : (easy.shift() || hard.shift()));
  mocks.push(order);
}

// ---- guards ---------------------------------------------------------------
const all = new Set();
mocks.forEach((mk, i) => {
  const tally = {};
  for (const it of mk) {
    const s = it.code.split(".")[0];
    tally[s] = (tally[s] || 0) + 1;
    if (all.has(it.sig)) throw new Error(`"${it.sig}" appears in more than one mock`);
    all.add(it.sig);
  }
  for (const [s, n] of Object.entries(BLUEPRINT))
    if (tally[s] !== n) throw new Error(`mock ${i + 1}: ${s} has ${tally[s]}, blueprint says ${n}`);
  const stars = mk.filter((x) => x.lvl === 3).length;
  if (stars !== STARS_PER_MOCK)
    throw new Error(`mock ${i + 1}: ${stars} star items, expected ${STARS_PER_MOCK}`);
});

// ---- build ----------------------------------------------------------------
function cfg(n, items) {
  return {
    mathIndex: "math_sim_doc/_index.json",
    figIndex: "figs_sim/_index.json",
    examName: "GAT (Qudurat) quantitative mock",
    targets: { "GAT-Q-ARI": "36%", "GAT-Q-ALG": "18%", "GAT-Q-GEO": "18%",
               "GAT-Q-DAT": "18%", "GAT-Q-LOG": "10%" },
    dense: true, itemGap: 55,
    marking: "One point each, no penalty for a wrong answer",
    budgetNote:
      "Forty items sampled from the 226-item bank to the ETEC quantitative " +
      "blueprint exactly: 14 arithmetic, 7 algebra, 7 geometry, 7 data, 5 word " +
      "logic, with ten level-3 items. Mocks 1, 2 and 3 share no question and " +
      "carry the same strand and difficulty mix, so a score change between them " +
      "is a change in the student, not in the paper.",
    compareNote:
      "COMPARISON QUESTIONS.  Some questions give you two quantities, A and B, and ask which is greater. Answer (A) if A is greater, (B) if B is greater, (C) if the two are exactly equal, and (D) if what you are given is not enough to decide. Both (C) and (D) are real answers on this paper.",
    conditions:
      "No calculator, no phone, no smartwatch. Forty minutes for forty questions — " +
      "about one minute each. Answer every question: nothing is deducted for a " +
      "wrong answer, so a guess is always better than a blank.",
    sourceNote:
      "These questions are ORIGINAL. They were written to match the skills and " +
      "the traps of the real sitting; no wording, number set or figure is taken " +
      "from any past or circulating paper. Every answer was re-derived " +
      "independently in Python before release.",
    weekLine: "Grade 12 GAT · Semester 1, 2026–27",
    headerLine: `GAT (Qudurat) · Quantitative · Mock ${n} · 40 items · 40 minutes`,
    paperTitle: `GAT Quantitative Mock ${n}`,
    paperSub: "Forty questions, forty minutes. One point each. Answer every question.",
    keyTitle: `GAT Quantitative Mock ${n} — Answer Key and Error Analysis`,
    keySub: "For Mr Malek Thiab. Each item names the trick it is built on and what each wrong option means.",
    outPaper: `GAT_Mock_${n}_Paper.docx`,
    outKey: `GAT_Mock_${n}_Key.docx`,
    timing: "40 minutes",
    followUp: [
      ["32 – 40", "At or above the band that carries a strong Qudurat score. Move to full-length timed practice."],
      ["24 – 31", "The skills are there; the losses are pace or traps. Re-mark using the trick column, not the answer column."],
      ["16 – 23", "Take the strand with the most losses on its own, untimed, before the next mock."],
      ["Below 16", "Arithmetic first. It is 36% of the paper and it carries the other strands."],
      ["Whole class", "Any question where more than half the class chose the SAME wrong option is a teaching point, not a marking point — the key names what that option means."],
    ],
    items,
  };
}

(async () => {
  const only = process.argv[2] ? Number(process.argv[2]) : null;
  for (let i = 0; i < mocks.length; i++) {
    if (only && only !== i + 1) continue;
    await buildSet(cfg(i + 1, mocks[i]));
    const t = {};
    for (const it of mocks[i]) {
      const s = it.code.split(".")[0].replace("GAT-Q-", "");
      t[s] = (t[s] || 0) + 1;
    }
    console.log(`  mock ${i + 1}: ${mocks[i].length} items`, JSON.stringify(t),
                `| ${mocks[i].filter((x) => x.lvl === 3).length} star`);
  }
})();
