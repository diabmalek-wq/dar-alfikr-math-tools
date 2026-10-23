#!/usr/bin/env python3
"""Build a self-contained Bluebook-style SAT Math mock exam (one HTML file) from an exam JSON.

Usage:
  python3 build.py exams/exam-01_sessions-1-3-4-10.json \
      --title "SAT Aceit" \
      --intro "44 questions from Sessions 1, 3, 4 and 10." \
      --sessions "01=Session 1 · Quadratics & Nonlinear Functions" "03=Session 3 · ..." \
      --out dist/SAT_Aceit_Exam-01.html

The Desmos API key is NOT stored in the repo. Pass --desmos-key or set DESMOS_API_KEY.
(The page also accepts ?desmosKey=... in the URL.)
"""
import argparse, base64, json, os, sys, html
from pathlib import Path

HERE = Path(__file__).parent
Q_PER_MODULE = 22          # the scoring table and timing assume the real 2 x 22 layout
REQUIRED = ("id", "sess", "lv", "mc", "q", "key", "steps", "domain", "skill")


def validate(ex):
    errs, warns, ids = [], [], set()
    for m in ("m1", "m2"):
        items = ex.get(m)
        if not isinstance(items, list) or len(items) != Q_PER_MODULE:
            errs.append(f"{m}: need exactly {Q_PER_MODULE} items, got {len(items) if isinstance(items, list) else 'none'}")
            continue
        for n, it in enumerate(items, 1):
            tag = f"{m} Q{n} ({it.get('id', '?')})"
            for f in REQUIRED:
                if f not in it:
                    errs.append(f"{tag}: missing '{f}'")
            if it.get("id") in ids:
                errs.append(f"{tag}: duplicate id")
            ids.add(it.get("id"))
            if it.get("lv") not in ("M", "H"):
                errs.append(f"{tag}: lv must be 'M' or 'H'")
            if it.get("mc"):
                o = it.get("opts") or []
                if len(o) != 4 or len(set(o)) != 4:
                    errs.append(f"{tag}: MC needs 4 distinct options")
                if not isinstance(it.get("key"), int) or not 0 <= it["key"] < len(o):
                    errs.append(f"{tag}: MC key must be an index 0-3")
            else:
                if not isinstance(it.get("key"), (int, float)):
                    errs.append(f"{tag}: SPR key must be a number")
                elif not float(it["key"]).is_integer() and "disp" not in it:
                    warns.append(f"{tag}: non-integer SPR key; add 'disp' (LaTeX) for the review screen")
            if not it.get("steps"):
                errs.append(f"{tag}: needs worked Desmos steps")
            if it.get("q", "").count("$") % 2:
                errs.append(f"{tag}: odd number of $ in question text")
            for s in (it.get("opts") or []) + it.get("steps", []):
                if s.count("$") % 2:
                    errs.append(f"{tag}: odd number of $ in an option/step: {s[:50]}")
    mc = [it["key"] for m in ("m1", "m2") for it in ex.get(m, []) if it.get("mc") and isinstance(it.get("key"), int)]
    if mc:
        dist = {k: mc.count(k) for k in range(4)}
        if max(dist.values()) > 0.4 * len(mc):
            warns.append(f"answer-position spread is lopsided: {dist}")
    return errs, warns


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("exam_json")
    ap.add_argument("--title", default="SAT Math Mock Exam")
    ap.add_argument("--intro", default="44 questions.")
    ap.add_argument("--sessions", nargs="*", default=[], help='"01=Session 1 · Name" ...')
    ap.add_argument("--figs", default=None, help="folder of SVG figures named <fig-id>.svg (items use the 'fig' field)")
    ap.add_argument("--desmos-key", default=os.environ.get("DESMOS_API_KEY", ""))
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    ex = json.loads(Path(a.exam_json).read_text(encoding="utf-8"))
    errs, warns = validate(ex)
    for w in warns:
        print("WARN ", w)
    if errs:
        print("\n".join("ERROR " + e for e in errs))
        sys.exit(1)

    sess = dict(s.split("=", 1) for s in a.sessions)
    for m in ("m1", "m2"):
        for it in ex[m]:
            sess.setdefault(it["sess"], f"Session {it['sess']}")
    figs = {}
    if a.figs:
        for it in ex["m1"] + ex["m2"]:
            if it.get("fig"):
                p = Path(a.figs) / f"{it['fig']}.svg"
                figs[it["fig"]] = base64.b64encode(p.read_bytes()).decode()
    if not a.desmos_key:
        print("WARN  no Desmos key: the embedded calculator will fall back to the link to Desmos test mode")

    t = (HERE / "template.html").read_text(encoding="utf-8")
    t = (t.replace("/*DATA*/null", json.dumps(ex)).replace("/*SESS*/null", json.dumps(sess))
          .replace("/*FIGS*/null", json.dumps(figs)).replace("{{TITLE}}", html.escape(a.title))
          .replace("{{INTRO}}", html.escape(a.intro)).replace("{{DESMOS_KEY}}", a.desmos_key))
    out = Path(a.out); out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(t, encoding="utf-8")
    print(f"OK  {out}  ({out.stat().st_size // 1024} KB, {len(ex['m1']) + len(ex['m2'])} questions)")


if __name__ == "__main__":
    main()
