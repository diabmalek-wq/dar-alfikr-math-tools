// ---------------------------------------------------------------------------
// SAAT BANK — part M: Statistics/Probability (STA) and Trigonometry (TRI)
// supply top-up (20 items). Answer positions rotated A/B/C/D for balance.
// ---------------------------------------------------------------------------
module.exports = [
  {
    "sig": "recover-value-from-a-stated-mean",
    "code": "SAAT-M-STA.40",
    "unit": 5,
    "topic": "Data representation & measures of centre",
    "ses": 41,
    "lvl": 2,
    "stem": "A set of 6 numbers is 7, 10, x, 15, 8, 14. If the mean of the set is 11, find x.",
    "opts": [
      "12",
      "11",
      "9",
      "66"
    ],
    "ans": 0,
    "trick": "multiply the mean by the COUNT to get the total first, then subtract the sum of the known numbers — the missing value is not the mean itself",
    "why": "The total must be 11 × 6 = 66. The five known numbers sum to 7 + 10 + 15 + 8 + 14 = 54, so x = 66 − 54 = 12.",
    "traps": [
      "B: 11 — x mistaken for the mean itself, rather than solved from the total.",
      "C: 9 — an arithmetic slip while adding the five known numbers.",
      "D: 66 — the total sum given as the answer instead of solving for x."
    ]
  },
  {
    "sig": "identify-study-type",
    "code": "SAAT-M-STA.41",
    "unit": 5,
    "topic": "Data representation & measures of centre",
    "ses": 41,
    "lvl": 1,
    "stem": "A researcher records the exam scores every student in a school already earned, without changing anything about how they were taught. What type of study is this?",
    "opts": [
      "A survey",
      "An observational study",
      "An experiment",
      "A controlled trial"
    ],
    "ans": 1,
    "trick": "an observational study records existing behaviour without intervening, while an experiment deliberately changes a variable to see its effect — recording scores as they already stand is observation, not an experiment or a survey",
    "why": "No variable was manipulated and no one was asked a question directly; the existing scores were simply recorded, which is the definition of an observational study.",
    "traps": [
      "A: A survey — mistaking the recording of already-existing data for directly asking respondents questions.",
      "C: An experiment — assuming any organised data collection counts as one, when no variable was manipulated.",
      "D: A controlled trial — a term reserved for experiments with a control group, which requires manipulation not present here."
    ]
  },
  {
    "sig": "variance-and-sd-of-a-small-list",
    "code": "SAAT-M-STA.42",
    "unit": 5,
    "topic": "Measures of dispersion & standard deviation",
    "ses": 42,
    "lvl": 2,
    "stem": "Find the variance of the data set: 4, 8, 6, 10, 7.",
    "opts": [
      "2",
      "20",
      "4",
      "1.4"
    ],
    "ans": 2,
    "trick": "variance is the AVERAGE of the squared deviations from the mean — divide the sum of squares by n, and take the square root only afterward for the standard deviation, which is not what this question asks for",
    "why": "The mean is 35 ÷ 5 = 7. The squared deviations are 9, 1, 1, 9, 0, summing to 20, so the variance is 20 ÷ 5 = 4.",
    "traps": [
      "A: 2 — the square root taken too soon, giving the standard deviation instead of the variance.",
      "B: 20 — the sum of squared deviations left undivided by n.",
      "D: 1.4 — an unrelated ratio, such as the range divided by the count."
    ]
  },
  {
    "sig": "compare-two-groups-by-mean-and-sd",
    "code": "SAAT-M-STA.43",
    "unit": 5,
    "topic": "Measures of dispersion & standard deviation",
    "ses": 42,
    "lvl": 2,
    "stem": "Class A has a mean score of 78 with standard deviation 4. Class B has a mean score of 78 with standard deviation 9. Which statement is correct?",
    "opts": [
      "Class A's scores are more spread out than Class B's",
      "The two classes have identical score distributions",
      "Class B's average score is higher than Class A's",
      "Class B's scores are more spread out than Class A's"
    ],
    "ans": 3,
    "trick": "the mean alone says nothing about spread — a larger standard deviation means the scores are more spread out around that mean, even when the two means themselves are equal",
    "why": "Both classes share a mean of 78, but Class B's standard deviation of 9 is larger than Class A's 4, so Class B's scores are more spread out.",
    "traps": [
      "A: the direction of the comparison reversed, choosing the smaller standard deviation as the more spread out.",
      "B: equal means mistaken for identical distributions, ignoring the different standard deviations entirely.",
      "C: the means compared as if they differed, when both classes average 78."
    ]
  },
  {
    "sig": "recover-sd-from-empirical-rule-percentage",
    "code": "SAAT-M-STA.44",
    "unit": 5,
    "topic": "Measures of dispersion & standard deviation",
    "ses": 42,
    "lvl": 3,
    "stem": "Test scores are normally distributed with a mean of 60. 95% of scores fall between 50 and 70. What is the standard deviation?",
    "opts": [
      "5",
      "10",
      "2.5",
      "20"
    ],
    "ans": 0,
    "trick": "95% corresponds to TWO standard deviations either side of the mean, not one — divide the half-width by 2, not leave it as it is, to recover the standard deviation",
    "why": "The interval 50 to 70 is 2 standard deviations wide on each side, and its half-width is 70 − 60 = 10, so σ = 10 ÷ 2 = 5.",
    "traps": [
      "B: 10 — the half-width taken directly as σ, without dividing by 2.",
      "C: 2.5 — the half-width divided by 4, as if 95% corresponded to four standard deviations.",
      "D: 20 — the FULL width, 50 to 70, taken as σ."
    ]
  },
  {
    "sig": "factorial-equation-in-n-simple",
    "code": "SAAT-M-STA.45",
    "unit": 5,
    "topic": "Permutations, combinations & conditional probability",
    "ses": 44,
    "lvl": 2,
    "stem": "Solve the equation n! = 6 × (n − 1)! for n.",
    "opts": [
      "5",
      "6",
      "720",
      "120"
    ],
    "ans": 1,
    "trick": "n! ÷ (n − 1)! simplifies to n itself — cancel the shared factorial rather than expanding both sides into full factorial values",
    "why": "n! = n × (n − 1)!, so dividing both sides by (n − 1)! gives n = 6 directly.",
    "traps": [
      "A: 5 — one less than the correct value, from misreading (n − 1)! as n!.",
      "C: 720 — 6! evaluated in full, mistaking the request for a factorial VALUE rather than for n.",
      "D: 120 — 5! evaluated, compounding the same misreading."
    ]
  },
  {
    "sig": "conditional-probability-two-way-table",
    "code": "SAAT-M-STA.46",
    "unit": 5,
    "topic": "Permutations, combinations & conditional probability",
    "ses": 44,
    "lvl": 3,
    "stem": "Of 200 students, 120 study Arabic and 80 study French. Of the Arabic students, 45 also study French. A student is chosen at random from those who study French. What is the probability that the student also studies Arabic?",
    "opts": [
      "45/200",
      "45/120",
      "9/16",
      "35/80"
    ],
    "ans": 2,
    "trick": "conditional probability shrinks the sample space to the CONDITION given — divide by the French total, not by the whole class or by the Arabic total",
    "why": "45 of the 200 students study both subjects, and the French total is 80, so P(Arabic | French) = 45 ÷ 80 = 9/16.",
    "traps": [
      "A: 45/200 — divided by the whole class instead of by the French group.",
      "B: 45/120 — divided by the Arabic total, the wrong conditioning group.",
      "D: 35/80 — the complement (French only, not Arabic) used in the numerator instead of the overlap."
    ]
  },
  {
    "sig": "binomial-probability-exact-count",
    "code": "SAAT-M-STA.47",
    "unit": 5,
    "topic": "Permutations, combinations & conditional probability",
    "ses": 44,
    "lvl": 3,
    "stem": "A fair coin is tossed 5 times. What is the probability of getting exactly 3 heads?",
    "opts": [
      "1/32",
      "5/4",
      "3/5",
      "5/16"
    ],
    "ans": 3,
    "trick": "binomial probability needs BOTH the counting factor for which tosses are heads AND the probability of the whole outcome — one without the other misses either the arrangements or the likelihood",
    "why": "P(3 heads) = C(5, 3) × (1/2)^5 = 10 × 1/32 = 10/32 = 5/16.",
    "traps": [
      "A: 1/32 — the counting factor C(5, 3) left out entirely, as if there were only one way to get 3 heads.",
      "B: 5/4 — the probability factor for the two tails left out, so the result is not even a valid probability.",
      "C: 3/5 — the fraction of tosses that are heads used directly as if it were the probability."
    ]
  },
  {
    "sig": "circular-permutation-with-fixed-reference",
    "code": "SAAT-M-STA.48",
    "unit": 5,
    "topic": "Permutations, combinations & conditional probability",
    "ses": 44,
    "lvl": 4,
    "stem": "6 people are to be seated around a round table, and one particular person must sit facing the entrance (a fixed seat). In how many ways can the remaining 5 people be seated?",
    "opts": [
      "120",
      "720",
      "24",
      "60"
    ],
    "ans": 0,
    "trick": "once one seat is fixed by a real landmark, every other seat becomes distinguishable, so the usual divide-by-(n − 1) circular shortcut does not apply — it becomes an ordinary arrangement of the remaining people",
    "why": "With one seat already fixed, the remaining 5 people fill 5 distinguishable seats in 5! = 120 ways.",
    "traps": [
      "B: 720 — 6! used directly, treating the table as if all 6 seats were still unlabelled.",
      "C: 24 — 4! used, one too few of the remaining people arranged.",
      "D: 60 — 5! ÷ 2 used, applying a reflection-symmetry halving that does not apply when a seat is fixed."
    ]
  },
  {
    "sig": "missing-probability-in-a-distribution-table",
    "code": "SAAT-M-STA.49",
    "unit": 5,
    "topic": "Probability, sample spaces & counting principles",
    "ses": 43,
    "lvl": 2,
    "stem": "A discrete random variable X has the probability distribution P(X = 1) = 0.15, P(X = 2) = 0.35, P(X = 3) = k, P(X = 4) = 0.20. Find k.",
    "opts": [
      "0.70",
      "0.30",
      "1.00",
      "0.15"
    ],
    "ans": 1,
    "trick": "every probability distribution's values must sum to exactly 1 — add the three given probabilities and subtract the total from 1",
    "why": "0.15 + 0.35 + k + 0.20 = 1, so 0.70 + k = 1 and k = 0.30.",
    "traps": [
      "A: 0.70 — the sum of the three GIVEN probabilities reported directly, the subtraction from 1 never taken.",
      "C: 1.00 — the total probability itself given, instead of the single missing value.",
      "D: 0.15 — a nearby table entry copied by mistake instead of computing the missing value."
    ]
  },
  {
    "sig": "angle-of-elevation-basic",
    "code": "SAAT-M-TRI.66",
    "unit": 8,
    "topic": "Right-triangle trigonometry",
    "ses": 64,
    "lvl": 2,
    "stem": "From a point on the ground 40 m from the base of a tower, the angle of elevation to the top of the tower is 30°. Find the height of the tower, to the nearest metre. (tan 30° ≈ 0.577)",
    "opts": [
      "35 m",
      "69 m",
      "23 m",
      "20 m"
    ],
    "ans": 2,
    "trick": "the angle of elevation sits between the horizontal ground and the line of sight up to the top — the height is the side OPPOSITE that angle, found with tangent, not sine or cosine of the ground distance",
    "why": "height = 40 × tan 30° ≈ 40 × 0.577 ≈ 23 m.",
    "traps": [
      "A: 35 m — sine used in place of tangent, treating the 40 m as the hypotenuse rather than the adjacent side.",
      "B: 69 m — the 40 m divided by tan 30° instead of multiplied by it.",
      "D: 20 m — half of 40 taken directly, ignoring the angle altogether."
    ]
  },
  {
    "sig": "arc-length-from-radius-and-radians",
    "code": "SAAT-M-TRI.67",
    "unit": 8,
    "topic": "Degree & radian measure",
    "ses": 67,
    "lvl": 2,
    "stem": "A circle has radius 12 cm. Find the length of an arc that subtends a central angle of 2π/3 radians.",
    "opts": [
      "4π cm",
      "24π cm",
      "2π/3 cm",
      "8π cm"
    ],
    "ans": 3,
    "trick": "arc length is s = rθ with θ already in radians — multiply the radius by the angle directly, with no degree conversion needed",
    "why": "s = 12 × 2π/3 = 24π/3 = 8π cm.",
    "traps": [
      "A: 4π cm — the radius halved instead of used in full.",
      "B: 24π cm — the radius multiplied only by the angle's numerator, without dividing by its denominator, 3.",
      "C: 2π/3 cm — the angle itself reported as if it were already the arc length, the radius left out."
    ]
  },
  {
    "sig": "area-of-a-sector-from-degrees",
    "code": "SAAT-M-TRI.68",
    "unit": 8,
    "topic": "Degree & radian measure",
    "ses": 67,
    "lvl": 2,
    "stem": "A circle has radius 9 cm. Find the area of a sector with a central angle of 40°.",
    "opts": [
      "9π cm²",
      "81π cm²",
      "4π cm²",
      "20π cm²"
    ],
    "ans": 0,
    "trick": "a sector's area is the FRACTION of the full circle's area that the central angle represents — the angle over 360°, times πr² — not the angle used as a raw multiplier",
    "why": "Area = (40/360) × π × 9² = (1/9) × 81π = 9π cm².",
    "traps": [
      "B: 81π cm² — the full circle's area given, the 40° fraction never applied.",
      "C: 4π cm² — the angle fraction applied to the radius itself instead of to the full area πr².",
      "D: 20π cm² — the fraction inverted, using 360/40 in place of 40/360."
    ]
  },
  {
    "sig": "vertical-and-horizontal-shift-of-a-trig-graph",
    "code": "SAAT-M-TRI.69",
    "unit": 8,
    "topic": "Amplitude, period & phase shift",
    "ses": 71,
    "lvl": 3,
    "stem": "The graph of y = sin x is shifted 3 units up and π/2 units to the right. Which equation describes the new graph?",
    "opts": [
      "y = sin(x + π/2) + 3",
      "y = sin(x − π/2) + 3",
      "y = sin(x − π/2) − 3",
      "y = sin(x) + 3 − π/2"
    ],
    "ans": 1,
    "trick": "a shift RIGHT by h enters the function as (x − h), and a shift up by k is added OUTSIDE the function — the sign inside the bracket for a rightward shift is the one that gets flipped by reflex",
    "why": "A rightward shift of π/2 gives sin(x − π/2), and adding 3 outside raises the graph, giving y = sin(x − π/2) + 3.",
    "traps": [
      "A: the sign inside the bracket flipped, giving a leftward shift instead of rightward.",
      "C: the vertical shift's sign flipped, moving the graph down instead of up.",
      "D: the horizontal shift written as if it combined arithmetically with the vertical shift, instead of sitting inside the function."
    ]
  },
  {
    "sig": "sum-formula-direct-application",
    "code": "SAAT-M-TRI.70",
    "unit": 9,
    "topic": "Sum, difference & double-angle identities",
    "ses": 74,
    "lvl": 3,
    "stem": "If sin A = 3/5 and cos B = 12/13, with A and B both acute, find sin(A + B).",
    "opts": [
      "16/65",
      "33/65",
      "56/65",
      "63/65"
    ],
    "ans": 2,
    "trick": "sin(A + B) = sin A cos B + cos A sin B — every term keeps its own function, and the sign between the two terms is PLUS, unlike the cosine sum formula which reverses it",
    "why": "With cos A = 4/5 and sin B = 5/13: sin(A + B) = (3/5)(12/13) + (4/5)(5/13) = 36/65 + 20/65 = 56/65.",
    "traps": [
      "A: 16/65 — the sign between the terms taken as minus, as in a difference formula rather than a sum.",
      "B: 33/65 — the cosine sum formula used by mistake, cos A cos B − sin A sin B.",
      "D: 63/65 — the cosine difference formula used instead, cos A cos B + sin A sin B."
    ]
  },
  {
    "sig": "quadratic-in-cosine-solve",
    "code": "SAAT-M-TRI.71",
    "unit": 9,
    "topic": "Basic trigonometric equations",
    "ses": 76,
    "lvl": 4,
    "stem": "Solve 2cos²θ − cosθ − 1 = 0 for 0° ≤ θ ≤ 180°.",
    "opts": [
      "θ = 0° or 60°",
      "θ = 60° or 120°",
      "θ = 180° or 120°",
      "θ = 0° or 120°"
    ],
    "ans": 3,
    "trick": "treat cos θ as a single variable and factor the quadratic first — two roots for cos θ give two separate angle equations, and both must be checked against the given range",
    "why": "Factoring gives (2cos θ + 1)(cos θ − 1) = 0, so cos θ = 1 (θ = 0°) or cos θ = −1/2 (θ = 120° in this range).",
    "traps": [
      "A: 60° — the reference angle for cos θ = −1/2 used without the quadrant sign check, giving the acute angle instead of the obtuse one.",
      "B: the root cos θ = 1 dropped entirely, leaving only the second angle.",
      "C: 180° — cos θ = −1 solved instead of cos θ = −1/2, a sign misread in the factoring."
    ]
  },
  {
    "sig": "choose-which-law-applies",
    "code": "SAAT-M-TRI.72",
    "unit": 9,
    "topic": "Law of Sines & Cosines",
    "ses": 77,
    "lvl": 2,
    "stem": "A triangle has two known angles and one known side, which is opposite one of those angles. Which method should be used to find another side?",
    "opts": [
      "Law of Sines",
      "Law of Cosines",
      "Pythagorean theorem",
      "Basic right-triangle ratios"
    ],
    "ans": 0,
    "trick": "the Law of Sines needs an angle-side pair that already matches — an angle and the side opposite it — while the Law of Cosines is for two sides and the included angle, or three sides, where no matching pair exists yet",
    "why": "A known angle paired with its opposite side is exactly the ratio the Law of Sines is built from, so it applies directly.",
    "traps": [
      "B: the Law of Cosines chosen despite already having a complete angle-side pair, which the Law of Sines is built for.",
      "C: the Pythagorean theorem chosen, which only applies to a right triangle, not a general one.",
      "D: basic right-triangle ratios chosen, which likewise require a right angle that is not given here."
    ]
  },
  {
    "sig": "bearing-and-distance-worded",
    "code": "SAAT-M-TRI.73",
    "unit": 9,
    "topic": "Applications of trigonometry",
    "ses": 78,
    "lvl": 4,
    "stem": "A ship sails 40 km due east from a port, then 30 km due north. What is the ship's bearing from the port, to the nearest degree?",
    "opts": [
      "037°",
      "053°",
      "127°",
      "323°"
    ],
    "ans": 1,
    "trick": "a bearing is measured clockwise FROM NORTH — take the inverse tangent of the east distance over the north distance, not the reversed ratio, which swaps the angle with its complement",
    "why": "The bearing is arctan(40/30) ≈ 53° measured from north toward east, so the bearing is 053°.",
    "traps": [
      "A: 037° — the ratio inverted (north over east instead of east over north), giving the complementary angle.",
      "C: 127° — the angle measured from the east direction instead of from north.",
      "D: 323° — the bearing placed in the wrong hemisphere, as if the ship had travelled north-west instead of north-east."
    ]
  },
  {
    "sig": "resolve-vector-into-components",
    "code": "SAAT-M-TRI.74",
    "unit": 9,
    "topic": "Vectors & their basic applications",
    "ses": 79,
    "lvl": 3,
    "stem": "A force of 50 N acts at an angle of 37° above the horizontal. Find its horizontal and vertical components, to the nearest newton. (sin 37° ≈ 0.60, cos 37° ≈ 0.80)",
    "opts": [
      "30 N horizontal, 40 N vertical",
      "50 N horizontal, 0 N vertical",
      "40 N horizontal, 30 N vertical",
      "37 N horizontal, 50 N vertical"
    ],
    "ans": 2,
    "trick": "the component along the horizontal uses cosine and the component perpendicular to it uses sine — swapping sine and cosine here is the single most common slip in resolving a force",
    "why": "Horizontal = 50 × cos 37° ≈ 50 × 0.80 = 40 N. Vertical = 50 × sin 37° ≈ 50 × 0.60 = 30 N.",
    "traps": [
      "A: the sine and cosine components swapped, horizontal and vertical reversed.",
      "B: the force treated as entirely horizontal, the angle ignored altogether.",
      "D: the angle itself reported as if it were one of the components."
    ]
  },
  {
    "sig": "undefined-reciprocal-ratio-values",
    "code": "SAAT-M-TRI.75",
    "unit": 8,
    "topic": "Sine, cosine & tangent",
    "ses": 65,
    "lvl": 2,
    "stem": "At which of the following angles is sec θ undefined?",
    "opts": [
      "0°",
      "180°",
      "360°",
      "90°"
    ],
    "ans": 3,
    "trick": "a reciprocal ratio is undefined exactly where the ratio it inverts equals zero — secant inverts cosine, so it fails wherever cos θ = 0, not wherever some other special value occurs",
    "why": "sec θ = 1/cos θ, and cos 90° = 0, so sec θ is undefined at 90°. At 0°, 180° and 360° cosine is ±1 and secant is defined.",
    "traps": [
      "A: 0° chosen, where cos θ = 1 and secant is perfectly defined.",
      "B: 180° chosen, where cos θ = −1 and secant is defined, just negative.",
      "C: 360° chosen, coterminal with 0°, where cosine is again 1."
    ]
  }
];