// ---------------------------------------------------------------------------
// SIMULATED GAT BANK — part N: level-1/2 top-up for thin syllabus skills (22 items)
//
// Written against the Coverage Audit's third priority item: syllabus skills
// with only 1-2 items in the bank that also appear on the GAT itself.
// Six skills topped up here — percentage of a quantity, weighted averages,
// permutations and combinations, line graphs, histograms — plus the two
// genuine syllabus gaps, mixed numbers and decimal equations. Deliberately
// level 1/2, not level 3: these give each thin skill enough repetition to
// teach from, not another pass at the star pool (part m did that). The two
// new chart figures are each reused across three items, which is intentional
// — every item still carries its own `fig` reference independently, so each
// stands alone if shuffled into a different worksheet. Every answer was
// re-derived independently in Python (verify_sim.py) before this part was
// wired into the build. ORIGINAL throughout: no wording, number set or
// figure reproduced from any source.
// ---------------------------------------------------------------------------
module.exports = [

// ==================================================== PERCENTAGE OF A QUANTITY
{ sig: "percent-of-simple-quantity", code: "GAT-Q-ARI.3", lvl: 1,
  stem: "Find 35% of 240.",
  opts: ["35", "72", "84", "96"], ans: 2,
  trick: "convert the percentage to a decimal and multiply — 35% is 0.35, not the answer itself",
  why: "0.35 × 240 = 84.",
  traps: ["A: the percentage itself given as the answer, never applied to 240.",
          "B: 30% used instead of 35%.",
          "D: 40% used instead of 35%."] },

{ sig: "percent-find-part-from-total", code: "GAT-Q-ARI.3", lvl: 1,
  stem: "A class has 40 students. 60% of them are girls. How many boys are in the class?",
  opts: ["16", "20", "24", "28"], ans: 0,
  trick: "find the girls first, then subtract from the total — the question asks for the boys, the part that is NOT given directly",
  why: "60% of 40 = 24 girls, so the boys are 40 − 24 = 16.",
  traps: ["B: the class assumed split evenly, 40 ÷ 2.",
          "C: the number of GIRLS given, not boys — the trap this item exists for.",
          "D: 70% used for the girls by misreading the percentage."] },

{ sig: "percent-increase-simple", code: "GAT-Q-ARI.3", lvl: 2,
  stem: "A phone priced at 250 SAR is increased by 12%. Find the new price, in SAR.",
  opts: ["262", "270", "280", "300"], ans: 2,
  trick: "add the percentage increase to 100% first, 112%, then multiply once — adding 12 SAR flat treats a percentage like a fixed amount",
  why: "250 × 1.12 = 280 SAR.",
  traps: ["A: 12 SAR added directly, the percentage treated as a flat amount.",
          "B: 8% used instead of 12%.",
          "D: 20% used instead of 12%."] },

{ sig: "percent-of-percent-simple", code: "GAT-Q-ARI.3", lvl: 2,
  stem: "Find 10% of 30% of 900.",
  opts: ["27", "90", "270", "360"], ans: 0,
  trick: "work through BOTH percentages in order — the first percentage taken of 900 is not the final answer, it is the number the second percentage is taken of",
  why: "30% of 900 = 270, and 10% of 270 = 27.",
  traps: ["B: only the first step done, 10% of 900.",
          "C: only the second step done, 30% of 900.",
          "D: the two percentages added, 10% + 30% = 40%, and taken of 900."] },

// ============================================================ WEIGHTED AVERAGES
{ sig: "weighted-avg-equal-group-sizes", code: "GAT-Q-DAT.5", lvl: 1,
  stem: "Group A has 10 students with an average score of 80. Group B has 10 students with an average score of 90. Since the groups are the SAME size, what is the average score of all 20 students combined?",
  opts: ["80", "85", "90", "170"], ans: 1,
  trick: "equal-sized groups are the ONE case where a plain average of the two means is correct — that shortcut breaks the moment the group sizes differ, so check the sizes before using it",
  why: "Because both groups have 10 students, the combined average is simply (80 + 90) ÷ 2 = 85.",
  traps: ["A: only Group A's average given.",
          "C: only Group B's average given.",
          "D: the two averages added instead of averaged."] },

{ sig: "weighted-avg-unequal-small-groups", code: "GAT-Q-DAT.5", lvl: 2,
  stem: "Group A has 8 students with an average score of 70. Group B has 12 students with an average score of 85. Find the average score of all 20 students combined.",
  opts: ["76", "77.5", "79", "85"], ans: 2,
  trick: "multiply EACH group's average by its OWN size and add the totals — the group sizes are different here, so the plain average of 70 and 85 is not allowed",
  why: "Total = (8 × 70) + (12 × 85) = 560 + 1020 = 1580, and 1580 ÷ 20 = 79.",
  traps: ["A: the group sizes swapped, 12 applied to Group A and 8 to Group B.",
          "B: the two averages simply averaged, the different group sizes ignored.",
          "D: only Group B's average given, the larger group."] },

{ sig: "weighted-avg-price-per-kg", code: "GAT-Q-DAT.5", lvl: 2,
  stem: "A shop buys 5 kg of rice at 20 SAR per kilogram, and 15 kg of rice at 24 SAR per kilogram. Find the average price per kilogram for the whole purchase.",
  opts: ["20", "22", "23", "24"], ans: 2,
  trick: "weight each price by how many kilograms were bought at it — 15 kg cost far more of the total than 5 kg, so the average sits closer to 24 than to 20",
  why: "Total cost = (5 × 20) + (15 × 24) = 100 + 360 = 460 SAR, for 20 kg total. 460 ÷ 20 = 23 SAR per kilogram.",
  traps: ["A: only the cheaper price given.",
          "B: the two prices simply averaged, the different quantities ignored.",
          "D: only the pricier price given."] },

// ================================================ PERMUTATIONS AND COMBINATIONS
{ sig: "permutation-simple-books", code: "GAT-Q-DAT.4", lvl: 1,
  stem: "A shelf holds 5 different books, but only 3 of them will be displayed in a row. In how many different orders can 3 of the 5 books be displayed?",
  opts: ["10", "15", "60", "120"], ans: 2,
  trick: "ORDER matters here — build the count position by position: 5 choices for the first spot, 4 for the second, 3 for the third",
  why: "5 × 4 × 3 = 60.",
  traps: ["A: the COMBINATION count given instead, order ignored.",
          "B: 5 × 3 multiplied directly instead of 5 × 4 × 3.",
          "D: 5! used, as if all 5 books were being arranged, not just 3 positions."] },

{ sig: "combination-simple-committee", code: "GAT-Q-DAT.4", lvl: 1,
  stem: "A 3-person committee is chosen from 7 people, and the order in which they are chosen does not matter. How many different committees are possible?",
  opts: ["21", "35", "105", "210"], ans: 1,
  trick: "since order does NOT matter here, count the arrangements first (7 × 6 × 5) and then divide by the 3! ways those same three people could have been ordered",
  why: "(7 × 6 × 5) ÷ 3! = 210 ÷ 6 = 35.",
  traps: ["A: 7 × 3 multiplied directly.",
          "C: the PERMUTATION count given instead, order counted when it should not be — the trap this item exists for.",
          "D: 7! computed, far more than the question needs."] },

{ sig: "word-arrangement-simple-factorial", code: "GAT-Q-DAT.4", lvl: 2,
  stem: "The word DOHA has four different letters. In how many ways can all four letters be arranged?",
  opts: ["4", "16", "24", "256"], ans: 2,
  trick: "with n different letters and no repeats, the count is n! — build it position by position, 4 choices then 3 then 2 then 1",
  why: "4 × 3 × 2 × 1 = 24.",
  traps: ["A: just the number of letters given, not the number of arrangements.",
          "B: 4 × 4 computed instead of 4 × 3 × 2 × 1.",
          "D: 4⁴ used, as if each position could repeat a letter."] },

// =================================================================== LINE GRAPHS
{ sig: "line-graph-read-value", code: "GAT-Q-DAT.1", lvl: 1,
  stem: "The graph below shows the distance a cyclist has travelled, in km, over a 4-hour ride. According to the graph, how far had the cyclist travelled after 2 hours?",
  fig: "sim_line_cyclist_distance", figW: 2.6,
  opts: ["7", "14", "17", "22"], ans: 1,
  trick: "find the mark at hour 2 on the horizontal axis and read straight up to the line — not the mark before it or after it",
  why: "At hour 2 the graph reads 14 km.",
  traps: ["A: the reading at hour 1 given instead of hour 2.",
          "C: the reading at hour 3 given instead of hour 2.",
          "D: the final reading at hour 4 given instead of hour 2."] },

{ sig: "line-graph-total-increase", code: "GAT-Q-DAT.1", lvl: 1,
  stem: "Using the same graph, by how many kilometres did the cyclist's distance increase from hour 0 to hour 4?",
  fig: "sim_line_cyclist_distance", figW: 2.6,
  opts: ["15", "20", "22", "40"], ans: 1,
  trick: "the ride did NOT start at 0 km — subtract the hour-0 reading from the hour-4 reading, rather than just reading the final value off the graph",
  why: "The distance at hour 4 is 22 km and at hour 0 is 2 km, so the increase is 22 − 2 = 20 km.",
  traps: ["A: the increase from hour 1 to hour 4 used instead of hour 0 to hour 4, 22 − 7.",
          "C: the final reading given directly, the starting value of 2 km never subtracted.",
          "D: the correct increase doubled by mistake."] },

{ sig: "line-graph-average-rate", code: "GAT-Q-DAT.1", lvl: 2,
  stem: "Using the same graph, find the cyclist's average speed over the whole 4-hour ride, in km per hour.",
  fig: "sim_line_cyclist_distance", figW: 2.6,
  opts: ["4", "5", "5.5", "10"], ans: 1,
  trick: "average speed is the TOTAL increase in distance divided by the TOTAL time — find the increase first (subtracting the starting point), then divide by the number of hours",
  why: "The distance increased by 22 − 2 = 20 km over 4 hours, so the average speed is 20 ÷ 4 = 5 km/h.",
  traps: ["A: the total increase divided by 5 hours instead of 4, an off-by-one.",
          "C: the final reading, 22, divided by 4 directly — the starting value of 2 never subtracted.",
          "D: the total increase divided by 2 hours instead of 4."] },

// ==================================================================== HISTOGRAMS
{ sig: "histogram-modal-class", code: "GAT-Q-DAT.2", lvl: 1,
  stem: "The histogram below shows the scores of 40 students on a test. Which interval contains the most students?",
  fig: "sim_hist_test_scores", figW: 2.81,
  opts: ["60–70", "70–80", "80–90", "90–100"], ans: 1,
  trick: "compare the HEIGHT of every bar before answering — the tallest bar is not always the one next to the highest-numbered interval",
  why: "The tallest bar, with 15 students, is the 70–80 interval.",
  traps: ["A: the second-tallest bar picked instead of the tallest.",
          "C: the bar to the right of the tallest one picked.",
          "D: the smallest bar picked, at the high end of the scores."] },

{ sig: "histogram-total-count", code: "GAT-Q-DAT.2", lvl: 1,
  stem: "Using the same histogram, how many students took the test in total?",
  fig: "sim_hist_test_scores", figW: 2.81,
  opts: ["15", "28", "38", "40"], ans: 3,
  trick: "add the heights of EVERY bar, not just the tallest one or the first few — the total is the sum of all five classes",
  why: "4 + 9 + 15 + 10 + 2 = 40 students.",
  traps: ["A: the modal class's frequency given, not the total.",
          "B: only the first three classes summed, the last two overlooked.",
          "C: one bar under-read by 2 during the count."] },

{ sig: "histogram-count-above-threshold", code: "GAT-Q-DAT.2", lvl: 2,
  stem: "Using the same histogram, how many students scored 80 or above?",
  fig: "sim_hist_test_scores", figW: 2.81,
  opts: ["2", "10", "12", "27"], ans: 2,
  trick: "'80 or above' means the 80–90 class AND the 90–100 class together — read where the classes begin carefully before deciding which bars to add",
  why: "80–90 has 10 students and 90–100 has 2, so 10 + 2 = 12 students scored 80 or above.",
  traps: ["A: only the top class, 90–100, counted.",
          "B: only the 80–90 class counted, 90–100 left out.",
          "D: the 70–80 class wrongly included as well, three classes summed instead of two."] },

// ================================================================= MIXED NUMBERS
{ sig: "improper-fraction-to-mixed-number", code: "GAT-Q-ARI.2", lvl: 1,
  stem: "Write 17/5 as a mixed number.",
  opts: ["2 2/5", "3 2/5", "3 3/5", "4 2/5"], ans: 1,
  trick: "divide the numerator by the denominator — the whole-number part is the quotient, and the remainder sits over the SAME denominator",
  why: "17 ÷ 5 = 3 remainder 2, so 17/5 = 3 2/5.",
  traps: ["A: the quotient taken one too small.",
          "C: the remainder found as 5 − 2 instead of 17 − 15.",
          "D: the quotient taken one too large."] },

{ sig: "add-two-mixed-numbers", code: "GAT-Q-ARI.2", lvl: 1,
  stem: "Find 2¾ + 1⅚, giving your answer as a mixed number.",
  opts: ["3 4/5", "3 19/12", "4 5/12", "4 7/12"], ans: 3,
  trick: "convert both fractions to a COMMON denominator before adding — ¾ and ⅚ do not share a denominator, so they cannot be added as they stand",
  why: "¾ = 9/12 and ⅚ = 10/12, so 9/12 + 10/12 = 19/12 = 1 7/12. Adding the whole numbers: 2 + 1 + 1 7/12 = 4 7/12.",
  traps: ["A: the numerators and denominators added straight across, (3+5)/(4+6), instead of using a common denominator.",
          "B: the improper fraction 19/12 left uncarried into the whole number.",
          "C: 9/12 + 10/12 misadded to 17/12 instead of 19/12, one twelfth short after the carry."] },

{ sig: "mixed-number-recipe-scaling", code: "GAT-Q-ARI.2", lvl: 2,
  stem: "A recipe needs 2½ cups of flour per batch. How many cups of flour are needed for 3 batches?",
  opts: ["5.5", "6", "7.5", "8"], ans: 2,
  trick: "multiply the WHOLE mixed number by 3, not just its whole-number part — 2½ cups per batch means the half-cup scales up too",
  why: "2½ × 3 = 7½ cups.",
  traps: ["A: 2½ added to 3 instead of multiplied.",
          "B: the halves dropped, 2 × 3 used instead of 2½ × 3.",
          "D: 2½ rounded up to 3, then 3 × 3 used."] },

// =============================================================== DECIMAL EQUATIONS
{ sig: "solve-decimal-equation-simple", code: "GAT-Q-ALG.1", lvl: 1,
  stem: "Solve for x: 0.5x + 3 = 8.",
  opts: ["1", "2.5", "10", "16"], ans: 2,
  trick: "isolate the term with x FIRST — subtract 3 from both sides before doing anything with the 0.5",
  why: "0.5x = 8 − 3 = 5, so x = 5 ÷ 0.5 = 10.",
  traps: ["A: 0.5 misread as 5, so (8 − 3) ÷ 5 was used.",
          "B: the correct 5 multiplied by 0.5 instead of divided.",
          "D: 8 divided by 0.5 directly, the +3 never subtracted first."] },

{ sig: "solve-decimal-equation-both-sides", code: "GAT-Q-ALG.1", lvl: 2,
  stem: "Solve for x: 1.2x − 4 = 0.4x + 4.8.",
  opts: ["1", "1.1", "5.5", "11"], ans: 3,
  trick: "gather the x-terms on ONE side and the numbers on the other, watching the sign on each term as it crosses the equals sign",
  why: "1.2x − 0.4x = 4.8 + 4, so 0.8x = 8.8, and x = 8.8 ÷ 0.8 = 11.",
  traps: ["A: the −4 moved to the other side with the wrong sign, giving 0.8x = 0.8.",
          "B: the coefficient 0.8 misread as 8, so 8.8 ÷ 8 was used.",
          "C: the two x-coefficients added, 1.2 + 0.4, instead of subtracted."] },

{ sig: "decimal-equation-taxi-fare", code: "GAT-Q-ALG.1", lvl: 2,
  stem: "A taxi charges a flat fare of 5 SAR plus 1.75 SAR per kilometre. A ride costs 26 SAR in total. How many kilometres was the ride?",
  opts: ["10.5", "12", "14", "21"], ans: 1,
  trick: "subtract the FLAT fare first to find what was actually spent on distance, then divide THAT by the per-kilometre rate",
  why: "26 − 5 = 21 SAR spent on distance, and 21 ÷ 1.75 = 12 km.",
  traps: ["A: the rate misread as 2 SAR per km instead of 1.75.",
          "C: the rate misread as 1.5 SAR per km instead of 1.75.",
          "D: 26 − 5 = 21 given directly as the distance, the final division by the rate skipped."] },

];
