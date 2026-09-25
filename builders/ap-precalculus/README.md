# builders/ap-precalculus/

The AP Precalculus session-distribution schedule for the accelerated Grade 9
candidate track (see `docs/AP Precalculus — Grade 9 accelerated candidate.md`
in the Claude Project for the fuller narrative).

## What's in this folder

| File | What it is |
|---|---|
| `sched_full4b.json` | The data: a week-by-week schedule (start/end dates, teaching days, breaks) with per-session entries — each session typed `A` (a lesson, with unit/lesson/day/title), `B` (FRQ & Calculator Lab), `D` (a unit marker), or `null` (no session) — plus a `review_weeks` list |
| `build_ap_session_schedule_v4.py` | Reads `sched_full4b.json` and renders the 4-sessions/week version of the schedule as HTML/PDF, with each session type rendered as its own badge/cell |

## Conventions

- **The schedule is data-driven** — a change to pacing or session content is a
  change to `sched_full4b.json`, not to the build script, unless the change is
  to how a session type is rendered (a genuine script change, per the working
  agreement in the top-level `README.md`).
- **`v4` names the sessions-per-week variant**, not a version to overwrite — this
  script is specifically the 4-sessions/week build; a different weekly session
  count would be a new script, not an edit to this one.

## Running

```
python3 build_ap_session_schedule_v4.py
```

## Verification

No dedicated verifier — this is a schedule/pacing document, not an item bank or
graded deliverable, so there's nothing here for `verifiers/` to independently
re-derive.
