# MATA37H3 Tutoring Series — 15-Week Map

Confirmed against the official UTSC calendar description (fetched this session): the course's
real topic scope is Riemann sums/definite integral, FTC, techniques of integration, improper
integrals, numerical integration, sequences and series, absolute/conditional convergence,
convergence tests, Taylor polynomials/series, power series and applications — nothing more.
Applications of Integration, Differential Equations, and Parametric/Polar Coordinates are
OUT of scope (they belong to other UofT courses) and must never be added.

Per Malek's decision: 15 CALENDAR weeks, same topic scope, denser topics split across two
weeks each and dedicated practice woven in. **No midterm review weeks. One final review week
(Week 15) is included.**

| Wk | Topic | Status | Source content |
|----|-------|--------|-----------------|
| 1 | Sigma Notation, Riemann Sums & the Definite Integral | ✅ built (unchanged) | `week-01/` |
| 2 | The Fundamental Theorem of Calculus | ✅ built (unchanged) | `week-02/` |
| 3 | Integration Techniques I — Substitution & Integration by Parts | ✅ built (new split) | split from old Week-03 + Dummit enrichment |
| 4 | Integration Techniques II — Trig Integrals, Partial Fractions & the Weierstrass Substitution | ✅ built (new split + enrichment) | split from old Week-03 + Dummit's Weierstrass sub |
| 5 | Improper Integrals | ✅ built (unchanged; enrichment pending) | `week-05/` — UPenn (Blair) extra examples not yet folded in |
| 6 | Numerical Integration (Midpoint, Trapezoidal & Simpson's Rule) | ✅ built (new week, from OpenStax §3.6) | `week-06/` — closes the one real gap vs. official calendar |
| 7 | Sequences | ✅ built (renumbered, unchanged) | `week-07/` (was old Week-04) |
| 8 | Series: Definitions, Geometric Series & the Divergence Test | ✅ built (renumbered, unchanged) | `week-08/` (was old Week-06) |
| 9 | Convergence Tests I — Integral Test & Comparison Tests | ✅ built (new split) | `week-09/` — split from `_staged/src-convergence-tests/` (old Week-07) |
| 10 | Convergence Tests II — Alternating Series, Ratio Test, Absolute vs. Conditional Convergence | ✅ built (new split) | `week-10/` — split from `_staged/src-convergence-tests/` (old Week-07) |
| 11 | Power Series — Convergence, Radius & Interval | ⏳ not yet built — split pending | staged: `_staged/src-power-series.md` (old Week-08) |
| 12 | Power Series — Representations, Term-by-Term Operations & Taylor Polynomials | ⏳ not yet built — split pending | staged: `_staged/src-power-series.md` (old Week-08) |
| 13 | Taylor & Maclaurin Series | ⏳ not yet built — split pending | staged: `_staged/src-taylor-series.md` (old Week-09) |
| 14 | Taylor Series Applications — Binomial Series, Error Bounds & Series Gymnastics | ⏳ not yet built — split pending | staged: `_staged/src-taylor-series.md` (old Week-09) + Binomial Series enrichment (Millersville/Paul's Notes) |
| 15 | Final Exam Review (comprehensive, all topics) | ⏳ not yet built — NEW week | SFU Ch. 7.3 Final Exam Practice (13 problems, full answers) + True/False supplement drawn from Montana State §10.5.4/10.8.6/10.9.1–3 and SFU 7.1/7.2 |

## Staged (not yet renumbered/split) source files
- `_staged/src-integration-methods.md` + `_staged/src-integration-methods.json` (hints) — old Week-03, fully split into Weeks 3–4 already; kept only as a reference, safe to delete once Weeks 3–4 are verified.
- `_staged/src-convergence-tests.md` + `.json` — old Week-07, to be split into Weeks 9–10.
- `_staged/src-power-series.md` + `.json` — old Week-08, to be split into Weeks 11–12.
- `_staged/src-taylor-series.md` + `.json` — old Week-09, to be split into Weeks 13–14.

## Known enrichment backlog (from the 10-PDF + SFU-notes library read)
- Week 4: Weierstrass substitution `t=tan(x/2)` — done (added).
- Week 5: fold in UPenn (Blair) improper-integral examples (interior-singularity split case) — not yet done.
- Week 6: built from OpenStax §3.6 (Midpoint, Trapezoidal, Simpson's Rule, all error bounds) — done; UConn (Stein)/SFU §3.6 cross-reference examples not yet folded in as extra enrichment.
- Week 10: MIT 18.100A rigorous proofs as an optional "why it works" box (not required for the worksheet).
- Week 11: Waterloo (Forrest) "ratio test limit doesn't exist" ninja-level example as a challenge problem.
- Week 14: Binomial Series content (from Millersville handout + user-uploaded Paul's Notes) — full derivation + 1/√(1-x) worked example ready to drop in.
- Week 15 / True-False supplement: raw material identified in Montana State Ch.10 homework sets and SFU Chapters 7.1/7.2/7.3 — real exam screenshots (2016/2017) confirm True/False is the heavily-weighted opening section on actual MATA37H3 exams.

## Build pipeline (unchanged)
`tools/build.sh <NN> <path/to/Week-NN-*.md> <tools/hints/week-NN.json> <out_dir>` — see `tools/render.py` for the markdown→LaTeX transform. Each `.md` must have exactly the four `##` sections (`Page 1 — ...`, `Pages 2–3 — Solved Examples`, `Pages 4–5 — Practice Problems`, `Answer Key & Misconception Notes`) with the `# Week N — Title` H1 matching the folder number exactly.
