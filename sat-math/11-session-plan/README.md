# SAT Math 11-session plan (private tutoring)

Weeks 1A, 1B, 2A, 2B and 3A are finished. The remaining content is reorganized into 11 sessions of 3 hours, built from the 919-item SAT bank (`../../sat-bank/verified-item-bank/`). The Algebra domain is excluded because Weeks 1 to 3A already covered it, leaving 618 questions.

| File | What it is |
|---|---|
| `session_plan_11.csv` | Every question ID with its session, part (In class or Self-assessment), domain, skill and difficulty |
| `SAT-M_Session-01_Quadratics-and-Nonlinear-Functions_Worksheet.pdf` | Session 1 worksheet: Part A in class (35 problems), Part B self-assessment (23) |
| `SAT-M_Session-01_Quadratics-and-Nonlinear-Functions_Answers.pdf` | Identical copy with every solution in green, as 3 to 4 Desmos steps per problem |
| `SAT-M_Session-02_Nonlinear-Functions_Worksheet.pdf` | Session 2 worksheet: Part A in class (48 problems), Part B self-assessment (25); 73 problems = 49 bank items + 24 new original items (IDs `S2N-01` to `S2N-24`, not in the bank CSV) |
| `SAT-M_Session-02_Nonlinear-Functions_Answers.pdf` | Identical copy with every solution in green, as 3 to 4 Desmos steps per problem |
| `session-02-builder/` | Scripts and data for Session 2 (new items in `new_items.py`, `steps_new.py`, `figs.py`), including `solve.py`, `verify.py` and `verify_steps.py` (independent answer check against the Answers PDF) |
| `session-01-builder/` | Scripts and data that build Session 1 (`build.py`, `steps.py`, `lib.py`, `figlib.py`, `s1_items.json`) |

Balancing: sessions are cut at equal solving time (about 195 minutes each, estimated at 4 minutes per Hard and 2.5 per Medium question). Each session has about 35 in-class questions (about 140 minutes) and the rest as self-assessment.

Session 1 has no Saudi context (private tutoring rule); the bank items were reworded to neutral contexts and dollars. Session 2 follows the same rules. Sessions 3 to 11 are not built yet.
