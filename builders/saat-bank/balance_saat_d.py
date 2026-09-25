"""Answer-position balancer for part D.

Same idea as balance_saat.js — ROTATE each option list so the correct answer
lands on the least-used letter, and renumber the trap notes to follow — but it
reads the multi-line layout part D is written in rather than the one-line-per-
item layout of the earlier parts.

Rotation, not a swap: the author's ordering of the options is deliberate (a
list that runs 2, 4, 6, 8 should still read 2, 4, 6, 8), so the list is turned,
never shuffled.

    python3 balance_saat_d.py            # edits saat_items_d.js in place
"""
import re
import subprocess
import sys

FILE = sys.argv[1] if len(sys.argv) > 1 else "saat_items_d.js"
LET = ["A", "B", "C", "D"]


def span(src, start):
    """Return (text, end) for the bracketed group that starts at src[start]."""
    depth, in_str, i = 0, False, start
    while i < len(src):
        c = src[i]
        if c == '"' and src[i - 1] != "\\":
            in_str = not in_str
        elif not in_str:
            if c in "[{(":
                depth += 1
            elif c in "]})":
                depth -= 1
                if depth == 0:
                    return src[start:i + 1], i + 1
        i += 1
    raise ValueError("unbalanced group")


def elements(group):
    """Split a bracketed group into its top-level element sources."""
    body, out, depth, in_str, start = group[1:-1], [], 0, False, 0
    for i, c in enumerate(body):
        if c == '"' and body[i - 1] != "\\":
            in_str = not in_str
            continue
        if in_str:
            continue
        if c in "[{(":
            depth += 1
        elif c in "]})":
            depth -= 1
        elif c == "," and depth == 0:
            out.append(body[start:i])
            start = i + 1
    tail = body[start:]
    if tail.strip():
        out.append(tail)
    return [e.strip() for e in out]


def main():
    src = open(FILE, encoding="utf8").read()
    # one block per item, cut at the "sig:" lines
    parts = re.split(r"(?=\n  \{\n    sig: )", src)
    tally = [0, 0, 0, 0]
    out = []
    for b in parts:
        m = re.search(r'sig: "([^"]+)"', b)
        oi = b.find("opts: [")
        ai = re.search(r"\n    ans: (\d),", b)
        ti = b.find("traps: [")
        if not m or oi < 0 or not ai or ti < 0:
            out.append(b)
            continue
        opts_src, _ = span(b, oi + len("opts: "))
        traps_src, traps_end = span(b, ti + len("traps: "))
        opts = elements(opts_src)
        traps = elements(traps_src)
        assert len(opts) == 4 and len(traps) == 3, m.group(1)
        ans = int(ai.group(1))

        target = min(range(4), key=lambda i: (tally[i], i))
        k = (target - ans) % 4
        new_opts = [opts[(i - k) % 4] for i in range(4)]
        # a trap that named old position j now names (j + k) mod 4
        new_traps = []
        for t in traps:
            tm = re.match(r'"([ABCD]): ', t)
            assert tm, t
            j = LET.index(tm.group(1))
            new_traps.append('"%s: %s' % (LET[(j + k) % 4], t[len(tm.group(0)):]))
        new_traps.sort(key=lambda t: t[1])
        tally[target] += 1

        pad = "\n      "
        b = (b[:oi] + "opts: [" + pad + ("," + pad).join(new_opts) + "\n    ]"
             + b[oi + len("opts: ") + len(opts_src):])
        # the traps block moved, so find it again in the rewritten text
        ti2 = b.find("traps: [")
        _, t_end = span(b, ti2 + len("traps: "))
        b = (b[:ti2] + "traps: [" + pad + ("," + pad).join(new_traps) + ",\n    ]"
             + b[t_end:])
        b = re.sub(r"\n    ans: \d,", "\n    ans: %d," % target, b, count=1)
        out.append(b)

    open(FILE, "w", encoding="utf8").write("".join(out))
    subprocess.run(["node", "-e", "require('./%s')" % FILE], check=True)
    print("answer positions now A/B/C/D = " + " / ".join(map(str, tally)))


if __name__ == "__main__":
    main()
