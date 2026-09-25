// ---------------------------------------------------------------------------
// SIMULATED GAT BANK — part O: word-logic supply top-up (10 items)
//
// Word logic (LOG) had run down to 6 unused items bank-wide, and ZERO of
// them level-3 — the tightest supply of any strand, and the new binding
// constraint on a weekly worksheet (see the Standing Resource, flagged after
// part n). Work-rate (LOG.2) was the thinnest sub-skill overall at only 5
// items total. This part adds 10 items — 4 work-rate, 2 speed/distance,
// 2 age, 2 money/value — weighted toward level-3 (5 of the 10) specifically
// to refill the empty star pool for this strand, the same reason part m
// existed for arithmetic and data. ORIGINAL throughout: no wording, number
// set or figure reproduced from any source. Every answer was re-derived
// independently in Python (verify_sim.py) before this part was wired into
// the build.
// ---------------------------------------------------------------------------
module.exports = [

// =================================================================== LOGIC
{ sig: "rate-scale-workers-inverse", code: "GAT-Q-LOG.2", lvl: 1,
  stem: "5 workers can paint a fence in 6 days. Working at the same rate, how many days would 3 workers need to paint the same fence?",
  opts: ["4", "6", "8", "10"], ans: 3,
  trick: "FEWER workers means MORE days, and the total amount of work stays fixed — multiply the workers by the days first, then divide by the new number of workers",
  why: "5 workers × 6 days = 30 worker-days of work. With 3 workers, 30 ÷ 3 = 10 days.",
  traps: ["A: each fewer worker assumed to subtract a day, 6 − 2.",
          "B: the number of days left unchanged, no scaling applied at all.",
          "C: each fewer worker assumed to add a day, 6 + 2."] },

{ sig: "pipe-two-rates-together", code: "GAT-Q-LOG.2", lvl: 2,
  stem: "Pipe A alone fills a tank in 8 hours, and Pipe B alone fills the same tank in 12 hours. If both pipes are opened together, how many hours does it take to fill the tank?",
  opts: ["4.8", "8", "10", "20"], ans: 0,
  trick: "add the two pipes' RATES (fraction of the tank per hour), not their times — then take the reciprocal of the sum",
  why: "Pipe A's rate is 1/8 and Pipe B's rate is 1/12. Together: 1/8 + 1/12 = 5/24 of the tank per hour, so the tank fills in 24/5 = 4.8 hours.",
  traps: ["B: only Pipe A's time given, the faster pipe.",
          "C: the two times simply averaged, (8 + 12) ÷ 2.",
          "D: the two times added, as if the pipes worked against each other."] },

{ sig: "combined-then-one-leaves", code: "GAT-Q-LOG.2", lvl: 3,
  stem: "Worker A can complete a job in 10 days and Worker B can complete it in 15 days. They work together for 3 days, and then Worker A leaves. How many MORE days does Worker B need, working alone, to finish the job?",
  opts: ["5", "7.5", "12", "15"], ans: 1,
  trick: "find how much of the job is done during the 3 days TOGETHER first, then give only what remains to Worker B's own rate",
  why: "Together they complete 3 × (1/10 + 1/15) = 3 × 1/6 = 1/2 of the job in 3 days. The remaining 1/2 divided by Worker B's rate, 1/15, is 1/2 ÷ 1/15 = 7.5 days.",
  traps: ["A: the remaining half divided by Worker A's rate instead of Worker B's.",
          "C: three days simply subtracted from Worker B's total time, 15 − 3.",
          "D: Worker B's full time given, the 3 days of joint work never accounted for."] },

{ sig: "inlet-outlet-net-rate", code: "GAT-Q-LOG.2", lvl: 3,
  stem: "An inlet pipe can fill an empty tank in 6 hours. A separate outlet pipe, left open by mistake, can drain a full tank in 10 hours. If both pipes are open at the same time on an empty tank, how many hours does it take to fill it?",
  opts: ["3.75", "4", "6", "15"], ans: 3,
  trick: "the outlet pipe works AGAINST the inlet pipe — subtract its rate from the inlet's rate instead of adding it",
  why: "The net rate is 1/6 − 1/10 = 1/15 of the tank per hour, so the tank fills in 15 hours.",
  traps: ["A: the two rates added, as if both pipes were filling.",
          "B: the two times subtracted directly, 10 − 6, instead of the rates.",
          "C: only the inlet pipe's time given, the outlet ignored."] },

{ sig: "avg-speed-weighted-distances", code: "GAT-Q-LOG.1", lvl: 2,
  stem: "A car travels 30 km at a steady 30 km/h, then a further 120 km at a steady 60 km/h. Find the car's average speed for the whole trip, in km/h.",
  opts: ["45", "50", "60", "150"], ans: 1,
  trick: "average speed is TOTAL distance divided by TOTAL time — find the time for each leg separately, add them, and divide the full distance by that sum",
  why: "The first leg takes 30 ÷ 30 = 1 hour and the second takes 120 ÷ 60 = 2 hours, for 3 hours total. The average speed is (30 + 120) ÷ 3 = 50 km/h.",
  traps: ["A: the two speeds simply averaged, the different times ignored.",
          "C: only the faster speed given.",
          "D: the total distance divided by only the first hour, the second leg's time left out."] },

{ sig: "two-trains-toward-each-other", code: "GAT-Q-LOG.1", lvl: 3,
  stem: "Two train stations, one in Riyadh and one in Dammam, are 315 km apart. A train leaves the Riyadh station at 60 km/h, and at the same moment another train leaves the Dammam station at 45 km/h, travelling toward each other on the same line. After how many hours do the two trains meet?",
  opts: ["1.5", "3", "7", "21"], ans: 1,
  trick: "when two objects move toward each other, ADD their speeds to get the closing speed, then divide the FULL distance between them by that combined speed",
  why: "The combined speed is 60 + 45 = 105 km/h, so the trains meet after 315 ÷ 105 = 3 hours.",
  traps: ["A: the distance halved first, as if only half the gap needed covering.",
          "C: the slower train's speed used alone, 315 ÷ 45.",
          "D: the speeds subtracted instead of added, as if the trains moved in the same direction."] },

{ sig: "future-age-given-current", code: "GAT-Q-LOG.3", lvl: 1,
  stem: "In 6 years, Amal will be twice as old as her brother Faisal is right now. Faisal is currently 8 years old. How old is Amal now?",
  opts: ["2", "10", "16", "28"], ans: 1,
  trick: "find Amal's age IN 6 YEARS first (twice Faisal's current age), then subtract 6 to bring it back to today",
  why: "In 6 years Amal will be 2 × 8 = 16. Today, Amal is 16 − 6 = 10 years old.",
  traps: ["A: 6 subtracted from Faisal's age instead of from Amal's future age.",
          "C: Amal's age in 6 years given, the 'now' never adjusted for.",
          "D: Faisal's age in 6 years doubled instead of his current age."] },

{ sig: "three-ages-ratio-sum", code: "GAT-Q-LOG.3", lvl: 3,
  stem: "The sum of the ages of three cousins is 54 years, and their ages are in the ratio 4 : 5 : 9. Find the age of the youngest cousin.",
  opts: ["3", "12", "18", "27"], ans: 1,
  trick: "share the total into 4 + 5 + 9 = 18 parts first — the youngest cousin's age is 4 of those parts, not one part and not a third of the total",
  why: "54 ÷ 18 = 3 per part, and the youngest has 4 parts: 4 × 3 = 12 years.",
  traps: ["A: the value of ONE part given, not four parts worth.",
          "C: the total split evenly among the three cousins, the ratio ignored.",
          "D: the oldest cousin's age given instead of the youngest's."] },

{ sig: "two-item-purchase-system", code: "GAT-Q-LOG.4", lvl: 2,
  stem: "A stationery shop in Jeddah sells notebooks for 6 SAR each and pens for 2 SAR each. Sara buys 8 items in total, a mix of notebooks and pens, and pays 36 SAR. How many notebooks did she buy?",
  opts: ["3", "4", "5", "6"], ans: 2,
  trick: "set up both facts as equations — the number of items and the total cost — and solve them together, rather than guessing a split",
  why: "If n notebooks and (8 − n) pens cost 36 SAR: 6n + 2(8 − n) = 36, so 4n = 20 and n = 5 notebooks (and 3 pens).",
  traps: ["A: the number of PENS given instead of notebooks.",
          "B: the 8 items assumed split evenly, 4 and 4.",
          "D: all 8 items assumed to be notebooks, 36 ÷ 6, the pens ignored entirely."] },

{ sig: "simple-interest-rate", code: "GAT-Q-LOG.4", lvl: 3,
  stem: "Khalid invests 10 000 SAR at a simple annual interest rate. After 4 years, the total amount — principal plus interest — is 13 200 SAR. Find the annual interest rate.",
  opts: ["8", "32", "33", "80"], ans: 0,
  trick: "find the interest EARNED first (the total minus the principal), then divide by both the principal AND the number of years before converting to a percentage",
  why: "The interest earned is 13 200 − 10 000 = 3 200 SAR over 4 years. The rate is (3 200 ÷ (10 000 × 4)) × 100 = 8% per year.",
  traps: ["B: the interest divided by the principal alone, the 4 years never factored in.",
          "C: the total amount, 13 200, used in place of the interest, 3 200, in the rate formula.",
          "D: the decimal-to-percent conversion done wrong, ×1000 instead of ×100."] },

];
