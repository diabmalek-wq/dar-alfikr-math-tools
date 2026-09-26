#!/usr/bin/env python3
"""Transform a Week-0N worksheet .md into two pandoc-ready markdown+rawtex
files (worksheet, answer key), using the boxed design system in preamble.tex.
Usage: render.py <week_md_path> <week_num> <hints_json_path> <out_dir>
"""
import sys, os, re, json, subprocess

def md2tex(s):
    """Convert a markdown fragment to LaTeX via pandoc, since content that
    ends up inside a custom \\begin{...}\\end{...} box is treated by pandoc's
    raw_tex extension as ONE opaque raw block and never reprocessed — so we
    must pre-convert **bold**/lists/etc. to real LaTeX ourselves first."""
    s = s.strip()
    if not s:
        return ''
    r = subprocess.run(['pandoc', '-f', 'markdown+raw_tex', '-t', 'latex'],
                        input=s, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"pandoc failed converting fragment:\n{s}\n\n{r.stderr}")
    return shrink_wide_math(r.stdout.strip())

def shrink_wide_math(tex):
    """Auto-shrink any display-math block (pandoc's \\[...\\]) to fit the
    box's available width, so a long row-reduction/derivation chain that
    used to fit the full page width doesn't clip against a box's padding."""
    def repl(m):
        return ("\\par\\begin{adjustbox}{max width=\\boxmathwidth,center}$"
                + m.group(1) + "$\\end{adjustbox}\\par\\noindent ")
    return re.sub(r'\\\[(.*?)\\\]', repl, tex, flags=re.DOTALL)

_ESCAPE_MAP = {'&': r'\&', '%': r'\%', '#': r'\#', '_': r'\_',
               '{': r'\{', '}': r'\}', '~': r'\textasciitilde{}',
               '^': r'\textasciicircum{}'}

def escape_latex(s):
    return re.sub(r'[&%#_{}~^]', lambda m: _ESCAPE_MAP[m.group()], s)

def md_lite_to_tex(s):
    """Convert a plain-text-ish string that may contain $...$ math spans and
    *italic* spans into safe raw LaTeX: math passes through verbatim,
    *italic* becomes \\textit{...}, everything else gets LaTeX-escaped."""
    pieces = re.split(r'(\$[^$]+\$|\*[^*]+\*)', s)
    out = []
    for p in pieces:
        if p.startswith('$') and p.endswith('$'):
            out.append(p)
        elif p.startswith('*') and p.endswith('*') and len(p) > 1:
            out.append('\\textit{' + escape_latex(p[1:-1]) + '}')
        else:
            out.append(escape_latex(p))
    return ''.join(out)

def strip_hr(text):
    return re.sub(r'(?m)^-{3,}\s*$\n?', '', text)

def split_h2(text):
    """Split on '## Heading' lines, return dict heading->body (raw, no heading line)."""
    parts = re.split(r'(?m)^## (.+)$', text)
    # parts[0] is preamble before first H2 (title/session/source block)
    sections = {'__pre__': parts[0]}
    for i in range(1, len(parts), 2):
        sections[parts[i].strip()] = parts[i+1]
    return sections

def split_h3(text):
    parts = re.split(r'(?m)^### (.+)$', text)
    pre = parts[0]
    blocks = []
    for i in range(1, len(parts), 2):
        blocks.append((parts[i].strip(), parts[i+1]))
    return pre, blocks

BOXABLE = {
    'Definition': 'definitionbox',
    'Key Fact': 'factbox',
    'Fact': 'factbox',
    'Theorem': 'factbox',
}

def classify(heading):
    for prefix, env in BOXABLE.items():
        if heading.startswith(prefix + ':'):
            return env, heading[len(prefix)+1:].strip(), prefix.upper()
    if re.search(r'\b(Strategy|Algorithm|Operations)\b', heading):
        return 'methodbox', heading, 'METHOD'
    if heading.lower().startswith('why this matters') or heading.lower().startswith('recap'):
        return None, heading, None
    # generic fallback -> factbox so nothing is left unstyled
    return 'factbox', heading, 'FACT'

def extract_citation(body):
    """If body's first non-blank line is an italic parenthetical citation,
    pull it out and return (citation_or_None, remaining_body)."""
    lines = body.split('\n')
    idx = 0
    while idx < len(lines) and lines[idx].strip() == '':
        idx += 1
    if idx < len(lines) and re.match(r'^\*\(.*\)\*$', lines[idx].strip()):
        cite = lines[idx].strip()[1:-1]  # strip the * *
        rest = '\n'.join(lines[:idx] + lines[idx+1:])
        return cite, rest
    return None, body

TABLE_LINE_RE = re.compile(r'(?m)^\|.*\|\s*$\n^\|[\s:|-]+\|\s*$')

def has_table(text):
    return bool(TABLE_LINE_RE.search(text))

def render_page1(body):
    pre, blocks = split_h3(strip_hr(body))
    out = []
    if pre.strip():
        out.append(pre.strip())
    for heading, block_body in blocks:
        # heading may carry a trailing parenthetical, e.g. 'Vector Form of a Line (Module 2, "Lines")'
        env, title, label = classify(heading)
        cite, block_body = extract_citation(block_body)
        # longtable (pandoc's table output) cannot nest inside a breakable
        # tcolorbox — render any block containing a markdown table unboxed,
        # as plain markdown, so the OUTER pandoc pass handles it normally.
        if env is None or has_table(block_body):
            out.append(f"**{heading}**\n\n{block_body.strip()}\n")
            continue
        out.append(f"\\begin{{{env}}}{{{md_lite_to_tex(title)}}}")
        if cite:
            out.append(f"\\textit{{{escape_latex(cite)}}}\\par\\smallskip")
        out.append(md2tex(block_body))
        out.append(f"\\end{{{env}}}\n")
    return '\n\n'.join(out)

EXAMPLE_RE = re.compile(r'(?m)^\*\*Example\s+(\d+)\s*\((.*)\)\.\*\*\s*(.*)$')

def render_examples(body):
    body = strip_hr(body)
    matches = list(EXAMPLE_RE.finditer(body))
    out = ["\\sectionbanner{Worked Examples}\n"]
    for i, m in enumerate(matches):
        num, desc, rest_of_line = m.group(1), m.group(2), m.group(3)
        start = m.end()
        end = matches[i+1].start() if i+1 < len(matches) else len(body)
        block = (rest_of_line + '\n' + body[start:end]).strip()
        out.append(f"\\begin{{examplebox}}{{{num}}}")
        out.append(f"\\textit{{{md2tex(desc)}}}\\par\\smallskip")
        out.append(md2tex(block))
        out.append("\\end{examplebox}\n")
    return '\n\n'.join(out)

ITEM_RE = re.compile(r'(?m)^(\d+)\.\s+(.*)$')
SUBHEAD_RE = re.compile(r'(?m)^\*\*([^*]+)\*\*\s*$')

def word_count(s):
    return len(re.findall(r'\S+', s))

def render_problems(body, hints):
    body = strip_hr(body)
    # tokenize into a stream of (kind, content) : ('sub', title) or ('item', (num, text))
    lines = body.split('\n')
    tokens = []
    i = 0
    cur_item = None
    while i < len(lines):
        line = lines[i]
        m_item = ITEM_RE.match(line)
        m_sub = SUBHEAD_RE.match(line)
        if m_item:
            if cur_item:
                tokens.append(('item', cur_item))
            cur_item = (m_item.group(1), m_item.group(2))
        elif m_sub and not cur_item_continuation(line):
            if cur_item:
                tokens.append(('item', cur_item))
                cur_item = None
            tokens.append(('sub', m_sub.group(1)))
        else:
            if cur_item is not None and line.strip() != '':
                cur_item = (cur_item[0], cur_item[1] + '\n' + line)
            elif cur_item is not None:
                cur_item = (cur_item[0], cur_item[1] + '\n')
        i += 1
    if cur_item:
        tokens.append(('item', cur_item))

    out = ["\\sectionbanner{Practice Problems}\n",
           "*Read the hint and the caution before you start each problem — not after.*\n"]
    for kind, val in tokens:
        if kind == 'sub':
            out.append(f"\\vspace{{6pt}}\\noindent{{\\bfseries\\large {md_lite_to_tex(val)}}}\\par\\vspace{{2pt}}\n")
        else:
            num, text = val
            text = text.strip()
            out.append(f"**{num}.** {text}\n")
            h = hints.get(num, {})
            hint = h.get('hint', '').strip()
            caution = h.get('caution', '').strip()
            if hint:
                out.append(f"\\begin{{hintbox}}\\hintlabel {md2tex(hint)}\\end{{hintbox}}")
            if caution:
                out.append(f"\\begin{{cautionbox}}\\cautionlabel {md2tex(caution)}\\end{{cautionbox}}")
            n_lines = 6 if ('(a)' in text and '(b)' in text) else (5 if word_count(text) > 35 else 4)
            out.append(f"\\worklines{{{n_lines}}}\n\\vspace{{6pt}}\n")
    return '\n\n'.join(out)

def cur_item_continuation(line):
    return False

def split_row_respecting_math(line):
    """Split a markdown table row on '|', but never inside a $...$ span
    (some answers contain a literal | inside math, e.g. $|z|=13$)."""
    spans = []
    def protect(m):
        spans.append(m.group(0))
        return f"\x00{len(spans)-1}\x00"
    protected = re.sub(r'\$[^$]*\$', protect, line)
    def restore(s):
        return re.sub(r'\x00(\d+)\x00', lambda m: spans[int(m.group(1))], s)
    return [restore(c.strip()) for c in protected.strip().strip('|').split('|')]

def parse_answer_table(body):
    rows = []
    for line in body.split('\n'):
        line = line.strip()
        if not line.startswith('|'):
            continue
        cells = split_row_respecting_math(line)
        if len(cells) != 3:
            continue
        a, b, c = cells
        if a in ('#', '---') or set(a) <= {'-', ':'}:
            continue
        rows.append((a, b, c))
    return rows

def render_answerkey(body, weeknum, topic):
    rows = parse_answer_table(body)
    out = [f"\\worksheettitle{{{weeknum}}}{{Answer Key \\& Misconception Notes}}"
           f"{{For tutor use only --- do not show the student until after their attempt. ({topic})}}\n"]
    for num, answer, misconception in rows:
        out.append(f"\\begin{{examplebox}}{{{num} --- Answer}}")
        out.append(md2tex(answer))
        out.append(f"\\textbf{{\\textcolor{{cautionInk}}{{Common misconception:}}}} {md2tex(misconception)}")
        out.append("\\end{examplebox}\n")
    return '\n\n'.join(out)

def main():
    md_path, weeknum, hints_path, out_dir = sys.argv[1:5]
    text = open(md_path, encoding='utf-8').read()
    text = text.replace('✓', r'$\checkmark$')  # ✓ has no glyph in DejaVu Serif
    with open(hints_path) as f:
        hints = json.load(f)

    title_m = re.search(r'(?m)^# Week \d+ [—-]\s*(.+)$', text)
    topic = md_lite_to_tex(title_m.group(1).strip()) if title_m else ''
    session_m = re.search(r'\*\*Session length:\*\*\s*(.+)', text)
    source_m = re.search(r'\*\*Source:\*\*\s*(.+)', text)
    session_txt = md_lite_to_tex(session_m.group(1).strip()) if session_m else ''
    source_txt = md_lite_to_tex(source_m.group(1).strip()) if source_m else ''
    subtitle_line = f"{session_txt} \\textbullet\\ {source_txt}"

    sections = split_h2(text)
    page1_key = next(k for k in sections if k.startswith('Page 1'))
    ex_key = next(k for k in sections if k.startswith('Pages 2'))
    prob_key = next(k for k in sections if k.startswith('Pages 4'))
    ans_key = next(k for k in sections if k.startswith('Answer Key'))

    worksheet_parts = [
        f"\\worksheettitle{{{weeknum}}}{{{topic}}}{{{subtitle_line}}}\n",
        render_page1(sections[page1_key]),
        render_examples(sections[ex_key]),
        render_problems(sections[prob_key], hints),
    ]
    worksheet_md = '\n\n'.join(worksheet_parts)
    answerkey_md = render_answerkey(sections[ans_key], weeknum, topic)

    os.makedirs(out_dir, exist_ok=True)
    open(os.path.join(out_dir, f"Week-{weeknum}-worksheet.md"), 'w', encoding='utf-8').write(worksheet_md)
    open(os.path.join(out_dir, f"Week-{weeknum}-answerkey.md"), 'w', encoding='utf-8').write(answerkey_md)
    print("wrote", out_dir)

if __name__ == '__main__':
    main()
