// ---------------------------------------------------------------------------
// WEEKLY GAT WORKSHEETS, DRAWN FROM THE 226-ITEM BANK
//
// The bank is the standing resource now, not a one-off deliverable. This script
// is how a week's worksheet comes out of it, and the thing it protects is the
// one property a question bank loses first: a student must never meet the same
// question twice across a term of worksheets and mocks.
//
// THE LEDGER (gat_ledger.json) is what makes that true. Every item the bank has
// already issued — the three mocks, and every week built so far — is recorded
// against where it went. A new week draws only from what is left, and writes
// itself back. Delete the ledger and the guarantee is gone, so keep it beside
// the bank.
//
//     node make_gat_week.js 6          -> Week 6 worksheet + key
//     node make_gat_week.js 6 7 8      -> three weeks at once
//     node make_gat_week.js --status   -> what is used, what is left
//
// Each worksheet is twelve items in about fifteen minutes: a starter, not a
// mock. The strand mix follows the ETEC blueprint at worksheet scale
// (4 ARI / 2 ALG / 2 GEO / 2 DAT / 2 LOG) with four level-3 items, so a week is
// a small, honest slice of the real paper rather than a topic drill.
//
// WHY FOUR STARS AND NOT THREE. The bank is 34% level-3, and the three mocks
// took their stars at 25%, which left the unused pool star-heavy. Drawing three
// per week would empty the level-1 and level-2 items first and quietly make each
// week harder than the last — Week 9 would arrive at six stars out of twelve and
// a score drop would mean nothing. Four per week drains the pool evenly.
// ---------------------------------------------------------------------------
const fs = require("fs");
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
const BY = new Map(ITEMS.map((i) => [i.sig, i]));

const PER_WEEK = { "GAT-Q-ARI": 4, "GAT-Q-ALG": 2, "GAT-Q-GEO": 2,
                   "GAT-Q-DAT": 2, "GAT-Q-LOG": 2 };
const STARS = 4;   // 33%, the bank's own level-3 share, so the pool drains evenly
const LEDGER = "gat_ledger.json";

// ---- ledger ---------------------------------------------------------------
function loadLedger() {
  if (fs.existsSync(LEDGER)) return JSON.parse(fs.readFileSync(LEDGER, "utf8"));
  // First run: seed from the three mocks so a worksheet can never repeat a
  // question the class has already sat.
  const used = {};
  if (fs.existsSync("mock_meta.json")) {
    const mocks = JSON.parse(fs.readFileSync("mock_meta.json", "utf8"));
    mocks.forEach((m, i) => m.forEach((it) => { used[it.sig] = `Mock ${i + 1}`; }));
  }
  return { used };
}
function saveLedger(l) {
  fs.writeFileSync(LEDGER, JSON.stringify(l, null, 1));
}

// ---- deterministic draw ---------------------------------------------------
// The week number seeds the generator, so Week 7 is the same twelve questions
// whether it is built today or rebuilt in March.
function rng(seed) {
  let s = seed >>> 0;
  return () => (s = (s * 1664525 + 1013904223) >>> 0) / 4294967296;
}
function pick(pool, n, stars, rand) {
  const take = [];
  const want = (star) => {
    const bySub = {};
    for (const it of pool) {
      if ((it.lvl === 3) !== star) continue;
      (bySub[it.code] = bySub[it.code] || []).push(it);
    }
    const used = new Set(take.map((t) => t.code));
    const subs = Object.keys(bySub)
      .sort((a, b) => (used.has(a) ? 1 : 0) - (used.has(b) ? 1 : 0) || rand() - 0.5);
    return subs.length ? bySub[subs[0]][Math.floor(rand() * bySub[subs[0]].length)] : null;
  };
  for (let i = 0; i < n; i++) {
    const it = want(take.filter((t) => t.lvl === 3).length < stars) ||
               want(take.filter((t) => t.lvl === 3).length >= stars);
    if (!it) throw new Error("the bank has run out of unused items for this strand — " +
                            "run with --status to see what is left");
    take.push(it);
    pool.splice(pool.indexOf(it), 1);
  }
  return take;
}

function buildWeek(week, ledger) {
  const rand = rng(1000 + week);
  const free = {};
  for (const it of ITEMS) {
    if (ledger.used[it.sig]) continue;
    const s = it.code.split(".")[0];
    (free[s] = free[s] || []).push(it);
  }
  // WHICH STRAND SUPPLIES THE HARD ITEMS is worked out each week rather than
  // fixed. The bank is not evenly hard: data and word logic are mostly level-3,
  // arithmetic and geometry mostly level-1/2. A fixed share (say "one star from
  // each strand") empties the few easy data items in four weeks and then forces
  // BOTH data items to be level-3 for the rest of the term, so the worksheets
  // drift harder without anyone deciding they should. Instead each week takes
  // the stars it must (a strand with too few easy items left) and then fills the
  // rest from whichever strand is most star-heavy, which drains the pool level.
  const starShare = {};
  let owed = STARS;
  const supply = {};
  for (const [s, n] of Object.entries(PER_WEEK)) {
    const pool = free[s] || [];
    supply[s] = { star: pool.filter((x) => x.lvl === 3).length,
                  easy: pool.filter((x) => x.lvl !== 3).length, need: n };
    starShare[s] = Math.max(0, n - supply[s].easy);      // forced
    owed -= starShare[s];
  }
  const hungriest = Object.keys(PER_WEEK).sort((a, b) =>
    (supply[b].star / Math.max(1, supply[b].easy)) -
    (supply[a].star / Math.max(1, supply[a].easy)));
  while (owed > 0) {
    const s = hungriest.find((k) => starShare[k] < supply[k].need &&
                                    supply[k].star > starShare[k]);
    if (!s) break;
    starShare[s]++; owed--;
  }
  const picked = [];
  for (const [s, n] of Object.entries(PER_WEEK)) {
    if (!free[s] || free[s].length < n)
      throw new Error(`${s}: only ${(free[s] || []).length} unused items left, Week ${week} needs ${n}`);
    picked.push(...pick(free[s], n, starShare[s], rand));
  }
  // interleave strands, and keep the level-3 items off the front
  const rr = (list) => {
    const by = {};
    for (const it of list) (by[it.code.split(".")[0]] = by[it.code.split(".")[0]] || []).push(it);
    const out = [], keys = Object.keys(by);
    while (out.length < list.length)
      for (const k of keys) if (by[k].length) out.push(by[k].shift());
    return out;
  };
  const easy = rr(picked.filter((x) => x.lvl !== 3));
  const hard = rr(picked.filter((x) => x.lvl === 3));
  const order = [];
  for (let i = 0; order.length < picked.length; i++)
    order.push((i % 4 === 3 && hard.length) ? hard.shift() : (easy.shift() || hard.shift()));

  const gotStars = order.filter((x) => x.lvl === 3).length;
  if (gotStars !== STARS)
    console.log(`  note: Week ${week} has ${gotStars} level-3 items, not ${STARS} — ` +
                `the unused pool no longer holds enough of them`);
  for (const it of order) ledger.used[it.sig] = `Week ${week}`;
  return order;
}

function cfg(week, items) {
  const t = {};
  for (const it of items) {
    const s = it.code.split(".")[0].replace("GAT-Q-", "");
    t[s] = (t[s] || 0) + 1;
  }
  return {
    mathIndex: "math_sim_doc/_index.json",
    figIndex: "figs_sim/_index.json",
    examName: "GAT (Qudurat) weekly worksheet",
    targets: { "GAT-Q-ARI": "36%", "GAT-Q-ALG": "18%", "GAT-Q-GEO": "18%",
               "GAT-Q-DAT": "18%", "GAT-Q-LOG": "10%" },
    dense: true, itemGap: 60,
    marking: "One point each, no penalty for a wrong answer",
    budgetNote:
      `Twelve items drawn from the department's 226-item GAT bank: ` +
      `${t.ARI || 0} arithmetic, ${t.ALG || 0} algebra, ${t.GEO || 0} geometry, ` +
      `${t.DAT || 0} data, ${t.LOG || 0} word logic — the ETEC blueprint at ` +
      `worksheet scale. No question here appears in any other week or in Mocks 1 to 3.`,
    compareNote:
      "COMPARISON QUESTIONS.  Some questions give you two quantities, A and B, and ask which is greater. Answer (A) if A is greater, (B) if B is greater, (C) if the two are exactly equal, and (D) if what you are given is not enough to decide. Both (C) and (D) are real answers.",
    conditions:
      "No calculator. Fifteen minutes. Answer every question — nothing is deducted " +
      "for a wrong answer, so a guess always beats a blank.",
    sourceNote:
      "These questions are ORIGINAL to the department's own bank. Nothing is taken " +
      "from any past or circulating paper. Every answer was re-derived independently " +
      "in Python before release.",
    weekLine: `Grade 12 GAT · Week ${week} · Semester 1, 2026–27`,
    headerLine: `GAT (Qudurat) · Quantitative · Week ${week} worksheet · 12 items · 15 minutes`,
    paperTitle: `GAT Weekly Worksheet — Week ${week}`,
    paperSub: "Twelve questions, fifteen minutes. One point each. Answer every question.",
    keyTitle: `GAT Weekly Worksheet Week ${week} — Answer Key and Error Analysis`,
    keySub: "For Mr Malek Thiab. Each item names the trick it is built on and what each wrong option means.",
    outPaper: `GAT_Worksheet_W${week}_Paper.docx`,
    outKey: `GAT_Worksheet_W${week}_Key.docx`,
    timing: "15 minutes",
    followUp: [
      ["10 – 12", "Secure. Set the level-3 items from this week as the discussion points."],
      ["7 – 9", "Re-mark using the trick column. The gap is usually the trap, not the topic."],
      ["Below 7", "Take the strand with the most losses on its own before the next worksheet."],
      ["Whole class", "Any question where more than half the class chose the SAME wrong option is a teaching point, not a marking point."],
    ],
    items,
  };
}

// ---- status ---------------------------------------------------------------
function status(ledger) {
  const left = {}, used = {};
  for (const it of ITEMS) {
    const s = it.code.split(".")[0].replace("GAT-Q-", "");
    if (ledger.used[it.sig]) used[s] = (used[s] || 0) + 1;
    else left[s] = (left[s] || 0) + 1;
  }
  const where = {};
  for (const w of Object.values(ledger.used)) where[w] = (where[w] || 0) + 1;
  const total = Object.keys(ledger.used).length;
  console.log(`GAT bank: ${ITEMS.length} items · ${total} issued · ${ITEMS.length - total} left`);
  console.log("  issued to:", JSON.stringify(where));
  console.log("  unused by strand:", JSON.stringify(left));
  // How many more weeks are really possible is set by whichever runs out first:
  // a strand, or the supply of level-1/2 items. Reporting only the strand count
  // hides the difficulty drift until the worksheets are already lopsided.
  const byStrand = Object.entries(PER_WEEK)
    .map(([s, n]) => [s.replace("GAT-Q-", ""), Math.floor((left[s.replace("GAT-Q-", "")] || 0) / n)]);
  const unusedStars = ITEMS.filter((i) => !ledger.used[i.sig] && i.lvl === 3).length;
  const unusedEasy = ITEMS.length - total - unusedStars;
  const weeks = Math.min(...byStrand.map(([, w]) => w),
                         Math.floor(unusedEasy / (12 - STARS)));
  const binding = byStrand.filter(([, w]) => w === weeks).map(([s]) => s);
  console.log(`  unused level-3: ${unusedStars} · level-1/2: ${unusedEasy}`);
  console.log(`  that is ${weeks} more full weekly worksheet(s)` +
              (binding.length ? `, limited by ${binding.join(" and ")}` :
                                ", limited by the supply of level-1/2 items") + ".");
}

// ---- run ------------------------------------------------------------------
(async () => {
  const ledger = loadLedger();
  const args = process.argv.slice(2);
  if (!args.length || args.includes("--status")) {
    status(ledger);
    if (!fs.existsSync(LEDGER)) saveLedger(ledger);
    return;
  }
  // --rebuild reprints weeks ALREADY in the ledger, from the sigs it recorded.
  // Nothing is drawn and nothing is issued: this is how a week is re-made after
  // an item's wording or figure has been corrected.
  if (args.includes("--rebuild")) {
    const byS = Object.fromEntries(ITEMS.map((i) => [i.sig, i]));
    const only = args.filter((a) => /^\d+$/.test(a)).map(Number);
    const weeks = {};                       // the ledger maps sig -> set name
    for (const [sig, set] of Object.entries(ledger.used || {})) {
      const m = String(set).match(/^Week (\d+)$/);
      if (m) (weeks[Number(m[1])] = weeks[Number(m[1])] || []).push(sig);
    }
    for (const week of Object.keys(weeks).map(Number).sort((a, b) => a - b)) {
      if (only.length && !only.includes(week)) continue;
      const items = weeks[week].map((sig) => byS[sig]);
      if (items.some((i) => !i)) throw new Error(`Week ${week}: a recorded item is missing from the bank`);
      await buildSet(cfg(week, items));
      console.log(`  Week ${week}: ${items.length} items reprinted from the ledger`);
    }
    return;
  }
  for (const a of args) {
    const week = Number(a);
    if (!Number.isInteger(week)) throw new Error("week must be a number: " + a);
    const items = buildWeek(week, ledger);
    await buildSet(cfg(week, items));
    console.log(`  Week ${week}: ${items.length} items, ` +
                `${items.filter((x) => x.lvl === 3).length} level-3`);
  }
  saveLedger(ledger);
  status(ledger);
})();
