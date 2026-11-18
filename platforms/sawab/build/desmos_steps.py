"""Per-question 'Solve it with Desmos' walkthroughs for SAT items.
Every number shown as 'Desmos shows ...' is computed here with sympy from the exact lines the student is told to type."""
import re, html, math
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor

TR = standard_transformations + (implicit_multiplication_application, convert_xor)
X, Y = sp.symbols('x y')

def esc(s): return html.escape(str(s), quote=False)

# ---------------- LaTeX -> what the student types ----------------
def _grab(s, i):
    """s[i]=='{' -> (content, index after closing brace)"""
    d = 0
    for j in range(i, len(s)):
        if s[j] == '{': d += 1
        elif s[j] == '}':
            d -= 1
            if d == 0: return s[i+1:j], j+1
    raise ValueError('brace')

def _simple(a): return re.fullmatch(r'-?[0-9.]+|[a-zA-Z]|[a-zA-Z]_\d', a) is not None

def tex2type(s):
    s = s.strip().strip('$').strip()
    s = re.sub(r'\\(left|right|big|Big|bigl|bigr)(?![a-zA-Z])', '', s)
    s = s.replace('\\dfrac', '\\frac').replace('\\tfrac', '\\frac').replace('{,}', '')
    s = re.sub(r'\\(,|!|;|:| |quad|qquad)', '', s)
    s = re.sub(r'\\text\{[^{}]*\}|\\mathrm\{[^{}]*\}', '', s)
    s = s.replace('\\%', '%')
    # \frac and \sqrt (recursive, innermost first via loop)
    for _ in range(40):
        m = re.search(r'\\frac\s*\{', s)
        n = re.search(r'\\sqrt\s*(\[[^\]]*\])?\s*\{', s)
        if not m and not n: break
        if m and (not n or m.start() < n.start()):
            a, k = _grab(s, s.index('{', m.start()))
            if k >= len(s) or s[k] != '{': raise ValueError('frac')
            b, k2 = _grab(s, k)
            A, B = tex2type_inner(a), tex2type_inner(b)
            rep = (A if _simple(A) else '(' + A + ')') + '/' + (B if _simple(B) else '(' + B + ')')
            s = s[:m.start()] + rep + s[k2:]
        else:
            idx = n.group(1)
            a, k = _grab(s, s.index('{', n.start() + (len(idx) if idx else 0) + 5))
            A = tex2type_inner(a)
            rep = ('(' + A + ')^(1/' + idx[1:-1] + ')') if idx else 'sqrt(' + A + ')'
            s = s[:n.start()] + rep + s[k:]
    s = re.sub(r'\^\{([^{}]*)\}', lambda m: '^' + (m.group(1) if _simple(m.group(1)) else '(' + m.group(1) + ')'), s)
    s = re.sub(r'_\{([^{}]*)\}', lambda m: '_' + m.group(1), s)
    rep = {'\\cdot': '*', '\\times': '*', '\\div': '/', '\\leq': '<=', '\\geq': '>=', '\\le': '<=', '\\ge': '>=',
           '\\lt': '<', '\\gt': '>', '\\pi': 'pi', '\\sin': 'sin', '\\cos': 'cos', '\\tan': 'tan', '\\ln': 'ln', '\\log': 'log',
           '^\\circ': '', '\\circ': '', '\\degree': ''}
    for k in sorted(rep, key=len, reverse=True): s = s.replace(k, rep[k])
    s = s.replace('{', '(').replace('}', ')')
    if '\\' in s: raise ValueError('cmd')
    s = re.sub(r'\s+', '', s)
    return s

def tex2type_inner(a): return tex2type(a)

def type2sym(t, extra_funcs=()):
    u = t.replace('^', '**')
    loc = {'pi': sp.pi, 'sqrt': sp.sqrt, 'ln': sp.log, 'log': lambda z: sp.log(z, 10), 'sin': sp.sin, 'cos': sp.cos, 'tan': sp.tan,
           'e': sp.E, 'mean': None}
    loc = {k: v for k, v in loc.items() if v is not None}
    for f in extra_funcs: loc[f] = sp.Function(f)
    for c in 'abcdghjkmnpqrstuvwxyzABCDEFGHJKLMNOPQRSTUVWXYZ':
        loc.setdefault(c, sp.Symbol(c))
    return parse_expr(u, local_dict=loc, transformations=TR, evaluate=True)

def fmt(v):
    """number as Desmos would show it (up to 4 decimals, trimmed)"""
    try:
        v = sp.nsimplify(v) if not isinstance(v, (int, float)) else v
        f = float(sp.N(v))
    except Exception:
        return None
    if not math.isfinite(f): return None
    if abs(f - round(f)) < 1e-9: return str(int(round(f)))
    s = ('%.4f' % f).rstrip('0').rstrip('.')
    return s.replace('-', '−')

def math_segs(text):
    out = []
    text = text.replace('\\$', '')  # currency \$ inside math is not an equation delimiter
    for m in re.finditer(r'\$\$(.+?)\$\$|\$(.+?)\$', text, re.S):
        out.append((m.group(1) or m.group(2)).strip())
    return out

def tex_load(t):  # LaTeX handed to Desmos.setExpression
    t = t.replace('\\dfrac', '\\frac').replace('\\tfrac', '\\frac').replace('{,}', '')
    t = re.sub(r'\\(,|!|;| |quad)', '', t)
    t = re.sub(r'\\text\{[^{}]*\}', '', t)
    return t.strip()

def rename_var(tex, v):
    return re.sub(r'(?<![\\a-zA-Z])%s(?![a-zA-Z])' % re.escape(v), 'x', tex)

# ---------------- classification ----------------
REL = re.compile(r'<=|>=|<|>')
def classify(seg):
    try: t = tex2type(seg)
    except Exception: return None
    if not t or not re.search(r'[a-zA-Z]', t.replace('pi', '')) and '=' not in t: return {'kind': 'num', 'type': t, 'tex': seg}
    if REL.search(t): return {'kind': 'ineq', 'type': t, 'tex': seg}
    fm = re.fullmatch(r'([a-zA-Z])\(([a-z])\)=(.+)', t)
    if fm: return {'kind': 'func', 'type': t, 'tex': seg, 'f': fm.group(1), 'v': fm.group(2), 'rhs': fm.group(3)}
    if t.count('=') == 1:
        l, r = t.split('=')
        if not l or not r: return None
        return {'kind': 'eq', 'type': t, 'tex': seg, 'l': l, 'r': r}
    if t.count('=') == 0: return {'kind': 'expr', 'type': t, 'tex': seg}
    return None

def free_vars(t):
    try:
        e = type2sym(t.replace('=', '-(') + (')' if '=' in t else ''))
        return sorted(str(s) for s in e.free_symbols)
    except Exception:
        return None

def eq_sym(t):
    l, r = t.split('=')
    return type2sym(l) - type2sym(r)

def real_solutions(expr, v):
    try:
        sol = sp.solve(sp.Eq(expr, 0), v)
    except Exception:
        return None
    out = []
    for s in sol:
        try:
            c = complex(sp.N(s))
            if abs(c.imag) < 1e-9: out.append(sp.nsimplify(s) if s.is_number else s)
        except Exception:
            return None
    return out

TRIG_SUBS = {'Sine, cosine, tangent ratios', 'Other trigonometry', 'Special right triangles', 'Pythagorean theorem applications'}
REASON_SUBS = {'Study design and causation', 'Generalizing from samples', 'Scatterplot and model choice', 'Data displays and distributions'}
SYS_SUBS = {'Finding a value from the solution', 'Solving by substitution or elimination', 'Word problems with systems', 'Linear-nonlinear and nonlinear systems'}
NSOL_SUBS = {'Number of solutions (none or infinite)', 'No solution or infinitely many solutions'}
INEQ_SKILL = 'Linear inequalities'
CIRC_SUBS = {'Equation of a circle', 'Tangent lines'}
DATA_SUBS = {'Mean, median and mode', 'Spread: range and standard deviation'}

def chip(t, tex=None):
    return {'s': t, 'x': tex}

def opt_text(o): return o

# ---------------- main ----------------
def build(x):
    q = x['q']; sub = x['sub']; skill = x['skill']; opts = x.get('opts')
    steps = []; nums = []          # nums: values Desmos will display (for the answer check)
    segs = [c for c in (classify(s) for s in math_segs(q)) if c]
    codes = []
    for st in x['steps']:
        for m in re.finditer(r'<code>(.*?)</code>', st):
            c = html.unescape(m.group(1)).strip()
            if re.match(r'(?i)^solve\b', c) or not c: continue
            c = re.sub(r'\ba(cos|sin|tan)\(', r'arc\1(', c)
            if c not in codes: codes.append(c)
    used_codes = set()
    qtxt = re.sub(r'\$[^$]*\$', ' ', q).lower()
    deg = sub in TRIG_SUBS or '^\\circ' in q or 'degree' in qtxt
    if deg and re.search(r'\\(sin|cos|tan)|sin|cos|tan', q):
        steps.append({'t': 'Set Desmos to degrees: click the wrench (graph settings) and choose <b>Degrees</b>.'})

    eqs = [c for c in segs if c['kind'] == 'eq']
    funcs = [c for c in segs if c['kind'] == 'func']
    ineqs = [c for c in segs if c['kind'] == 'ineq']
    exprs = [c for c in segs if c['kind'] == 'expr']
    done = False

    # --- systems: two equations in two unknowns ---
    if not done and len(eqs) >= 2:
        pair = eqs[:2]; vs = sorted(set((free_vars(pair[0]['type']) or []) + (free_vars(pair[1]['type']) or [])))
        each = [set(free_vars(p['type']) or []) for p in pair]
        okpair = len(vs) == 2 and (sub in SYS_SUBS or all(len(e_) == 2 for e_ in each)) and not ('x' in vs and 'y' not in vs and 'x' not in (vs[0],))
        if 'x' in vs and 'y' not in vs: okpair = False
        if okpair:
            a, b = vs if vs != ['x', 'y'] else ['x', 'y']
            if 'x' in vs and 'y' in vs: a, b = 'x', 'y'
            try:
                E1 = eq_sym(pair[0]['type']); E2 = eq_sym(pair[1]['type'])
                A, B = sp.Symbol(a), sp.Symbol(b)
                E1 = E1.subs({A: X, B: Y}, simultaneous=True); E2 = E2.subs({A: X, B: Y}, simultaneous=True)
                sol = sp.solve([E1, E2], [X, Y], dict=True)
                sol = [s for s in sol if all(abs(complex(sp.N(v)).imag) < 1e-9 for v in s.values()) and len(s) == 2]
            except Exception:
                sol = None
            ren = '' if (a, b) == ('x', 'y') else f' Desmos graphs in <i>x</i> and <i>y</i>, so write <i>{esc(a)}</i> as <i>x</i> and <i>{esc(b)}</i> as <i>y</i>.'
            def rn(tex):
                if (a, b) == ('x', 'y'): return tex
                t2 = re.sub(r'(?<![\\a-zA-Z])%s(?![a-zA-Z])' % a, 'XX', tex)
                t2 = re.sub(r'(?<![\\a-zA-Z])%s(?![a-zA-Z])' % b, 'y', t2)
                return t2.replace('XX', 'x')
            lines = [chip(tex2type(rn(e['tex'])), tex_load(rn(e['tex']))) for e in pair]
            steps.append({'t': 'Type each equation on its own line.' + ren, 'c': lines})
            if sol is not None and len(sol) == 0:
                steps.append({'t': 'Look at the two graphs.', 'r': 'They never meet (parallel lines), so the system has <b>no solution</b>.'})
            elif sol:
                pts = ['(' + fmt(s[X]) + ', ' + fmt(s[Y]) + ')' for s in sol if fmt(s[X]) and fmt(s[Y])]
                if pts:
                    steps.append({'t': 'Click the point where the graphs cross. Desmos shows its coordinates in grey.', 'r': 'Desmos shows ' + ' and '.join(f'<b>{p}</b>' for p in pts) + '.'})
                    for s in sol: nums += [s[X], s[Y], s[X] + s[Y], s[X] - s[Y], s[X] * s[Y]]
            done = True

    # --- one equation (or one equation + parameter) ---
    if not done and eqs:
        e = eqs[0]; vs = free_vars(e['type']) or []
        if sub in NSOL_SUBS and len(vs) >= 1:
            l, r = e['type'].split('=')
            v = 'x' if 'x' in vs else vs[0]
            others = [w for w in vs if w != v]
            L = rename_var(tex_load(e['tex'].split('=')[0]), v); Rr = rename_var(tex_load(e['tex'].split('=', 1)[1]), v)
            steps.append({'t': 'Graph each side of the equation as its own line.' + (f' Write <i>{esc(v)}</i> as <i>x</i>.' if v != 'x' else ''),
                          'c': [chip('y=' + tex2type(L), 'y=' + L), chip('y=' + tex2type(Rr), 'y=' + Rr)]})
            if others:
                steps.append({'t': f'Desmos offers a slider for <i>{esc(others[0])}</i>: click <b>add slider</b> and drag it.', 'r': 'When the two lines are <b>parallel</b> (same slope, different intercept) the equation has no solution; when they <b>lie on top of each other</b> it has infinitely many.'})
            else:
                steps.append({'t': 'Look at the two lines.', 'r': 'Parallel lines that never meet mean <b>no solution</b>; one line exactly on top of the other means <b>infinitely many solutions</b>; one crossing point means exactly one solution.'})
            done = True
        elif len(vs) == 1:
            v = vs[0]
            try:
                Ex = eq_sym(e['type']).subs(sp.Symbol(v), X)
                sols = real_solutions(Ex, X)
            except Exception:
                sols = None
            L = rename_var(tex_load(e['tex'].split('=')[0]), v); Rr = rename_var(tex_load(e['tex'].split('=', 1)[1]), v)
            try:
                c1, c2 = chip('y=' + tex2type(L), 'y=' + L), chip('y=' + tex2type(Rr), 'y=' + Rr)
            except Exception:
                c1 = None
            if c1:
                steps.append({'t': 'Type the left side and the right side of the equation as two graphs.' + (f' Write <i>{esc(v)}</i> as <i>x</i>.' if v != 'x' else ''), 'c': [c1, c2]})
                if sols:
                    xs = [fmt(s) for s in sols if fmt(s) is not None]
                    if xs:
                        steps.append({'t': 'Click where the two graphs cross. The <i>x</i>-coordinate of that point is the solution.' if len(xs) == 1 else 'Click each point where the graphs cross. Their <i>x</i>-coordinates are the solutions.',
                                      'r': 'Desmos shows ' + ', '.join(f'<b>x = {s}</b>' for s in xs) + (f' (that is, {esc(v)} = {xs[0]})' if v != 'x' and len(xs) == 1 else '') + '.'})
                        nums += sols
                        # "what is the value of <expr>?"
                        m = re.search(r'value of \$([^$]+)\$', q)
                        if m and len(sols) == 1:
                            try:
                                tgt = tex2type(m.group(1))
                                if tgt != v:
                                    val = type2sym(tgt).subs(sp.Symbol(v), sols[0])
                                    tt = tgt.replace(v, '(' + tex2type(fmt(sols[0]).replace('−', '-')) + ')') if re.fullmatch(r'[0-9a-z+\-*/().^]+', tgt) else None
                                    if fmt(val) and tt:
                                        steps.append({'t': 'The question asks for ' + f'<i>{esc(tgt)}</i>' + ', so type it with that value put in.', 'c': [chip(tt, None)], 'r': f'Desmos shows <b>{fmt(val)}</b>.'})
                                        nums.append(val)
                            except Exception:
                                pass
                    elif sols == []:
                        steps.append({'t': 'Look at the two graphs.', 'r': 'They never cross, so the equation has no real solution.'})
                done = True
        elif len(vs) == 2 and 'x' in vs and 'y' in vs:
            steps.append({'t': 'Type the equation exactly as given.', 'c': [chip(e['type'], tex_load(e['tex']))]})
            done = 'graph'

    # --- functions ---
    if not done and funcs:
        f = funcs[0]
        try:
            fx = type2sym(f['rhs']).subs(sp.Symbol(f['v']), X)
        except Exception:
            fx = None
        lines = [chip(c['type'], tex_load(c['tex'])) for c in funcs[:2]]
        steps.append({'t': 'Type the function exactly as written. Desmos understands function notation.', 'c': lines})
        done = 'graph'
        # evaluations like f(3) in the stem text
        if fx is not None:
            ev = []
            for m in re.finditer(r'%s\((-?\d+(?:\.\d+)?)\)' % f['f'], q.replace('$', '')):
                a = m.group(1)
                if (f['f'], a) in [(z[0], z[1]) for z in ev]: continue
                try:
                    val = fx.subs(X, sp.nsimplify(a))
                    if fmt(val): ev.append((f['f'], a, val))
                except Exception: pass
            for g, a, val in ev[:2]:
                steps.append({'t': f'On a new line type the value you need.', 'c': [chip(f'{g}({a})', f'{g}\\left({a}\\right)')], 'r': f'Desmos shows <b>{fmt(val)}</b>.'})
                nums.append(val)
            fxx = fx
            if fxx.free_symbols <= {X}:
                try:
                    poly = sp.Poly(sp.expand(fxx), X)
                    if poly.degree() == 2 and re.search(r'vertex|maximum|minimum|greatest|least|highest|lowest', qtxt):
                        a2, b2, _ = poly.all_coeffs(); h = -b2 / (2 * a2); k = fxx.subs(X, h)
                        steps.append({'t': 'Click the turning point of the parabola.', 'r': f'Desmos shows the vertex <b>({fmt(h)}, {fmt(k)})</b>.'}); nums += [h, k]
                    elif re.search(r'zero|x-intercept|roots?|solutions?', qtxt) and poly.degree() <= 4:
                        rs = [r for r in real_solutions(fxx, X) or []]
                        if rs and all(fmt(r) for r in rs):
                            steps.append({'t': 'Click the points where the graph crosses the <i>x</i>-axis.', 'r': 'Desmos shows the <i>x</i>-intercepts at ' + ', '.join(f'<b>x = {fmt(r)}</b>' for r in rs) + '.'}); nums += rs
                    elif re.search(r'y-intercept', qtxt):
                        steps.append({'t': 'Click where the graph crosses the <i>y</i>-axis.', 'r': f'Desmos shows <b>(0, {fmt(fxx.subs(X, 0))})</b>.'}); nums.append(fxx.subs(X, 0))
                except Exception:
                    pass

    # --- equivalent expressions: compare graphs with the answer choices ---
    if not done and opts and exprs and re.search(r'equivalent', qtxt):
        try:
            E0 = exprs[-1]; e0 = type2sym(E0['type']); vs = {str(s) for s in e0.free_symbols}
            if len(vs) == 1:
                v = vs.pop(); same = []
                for i, o in enumerate(opts):
                    oo = classify(o.strip('$'))
                    if not oo or oo['kind'] != 'expr': raise ValueError
                    eo = type2sym(oo['type'])
                    if sp.simplify(e0 - eo) == 0: same.append(i)
                if same == [x['key']]:
                    steps.append({'t': 'Type the expression from the question as a graph.' + (f' Write <i>{esc(v)}</i> as <i>x</i>.' if v != 'x' else ''), 'c': [chip('y=' + tex2type(rename_var(tex_load(E0['tex']), v)), 'y=' + rename_var(tex_load(E0['tex']), v))]})
                    steps.append({'t': 'Type each answer choice as its own <i>y=</i> line (change the colour or hide lines to compare them one at a time).',
                                  'c': [chip('y=' + tex2type(rename_var(tex_load(o.strip('$')), v)), 'y=' + rename_var(tex_load(o.strip('$')), v)) for o in opts]})
                    steps.append({'t': 'Find the choice whose graph lies exactly on top of the original: Desmos draws the two as one curve.', 'r': f'Only choice <b>{"ABCD"[x["key"]]}</b> overlaps the original everywhere.'})
                    done = True
        except Exception:
            pass

    # --- inequalities ---
    if not done and ineqs:
        steps.append({'t': 'Type each inequality on its own line. Desmos shades the points that make it true.' + (' Where the shadings overlap is the solution region.' if len(ineqs) > 1 else ''), 'c': [chip(c['type'], tex_load(c['tex'])) for c in ineqs[:3]]})
        if opts and all(re.fullmatch(r'\$?\(\s*-?[\d.]+\s*,\s*-?[\d.]+\s*\)\$?', o.replace('\\left', '').replace('\\right', '')) for o in opts):
            try:
                good = []
                for i, o in enumerate(opts):
                    a, b = [sp.nsimplify(z) for z in re.findall(r'-?[\d.]+', o)]
                    ok = all(bool(type2sym(c['type'].replace('<=', '<=').replace('>=', '>=')).subs({X: a, Y: b})) for c in ineqs)
                    if ok: good.append(i)
                if good == [x['key']]:
                    steps.append({'t': 'Type each answer choice as a point, e.g. <code>(2,3)</code>.', 'r': f'Only choice <b>{"ABCD"[x["key"]]}</b> lands inside the shaded region.'})
            except Exception:
                pass
        done = True

    # --- circles ---
    if not done and sub in CIRC_SUBS:
        circ = [c for c in segs if c['kind'] == 'eq' and 'x' in c['type'] and 'y' in c['type'] and '^2' in c['type']]
        if circ:
            c = circ[0]
            steps.append({'t': 'Type the circle equation exactly as given. Desmos draws the circle.', 'c': [chip(c['type'], tex_load(c['tex']))]})
            try:
                E = sp.expand(eq_sym(c['type'])); P = sp.Poly(E, X, Y)
                A = P.coeff_monomial(X**2)
                if A != 0 and A == P.coeff_monomial(Y**2) and P.coeff_monomial(X*Y) == 0:
                    D, Ey, F = P.coeff_monomial(X) / A, P.coeff_monomial(Y) / A, P.coeff_monomial(1) / A
                    h, k = -D / 2, -Ey / 2; r2 = h**2 + k**2 - F
                    if r2 > 0:
                        r = sp.sqrt(r2)
                        steps.append({'t': f'Check the centre: type the point <code>({fmt(h).replace("−","-")},{fmt(k).replace("−","-")})</code>. It sits exactly in the middle of the circle. Click the top of the circle to read the radius as the vertical distance from the centre.',
                                      'c': [chip(f'({fmt(h).replace("−","-")},{fmt(k).replace("−","-")})', f'\\left({fmt(h).replace("−","-")},{fmt(k).replace("−","-")}\\right)')],
                                      'r': f'Centre <b>({fmt(h)}, {fmt(k)})</b>, radius <b>{fmt(r)}</b>{" (about " + fmt(sp.N(r)) + ")" if not r.is_integer else ""}, so the diameter is <b>{fmt(2*r)}</b>.'})
                        nums += [h, k, r, 2 * r, r2]
            except Exception:
                pass
            done = 'graph'

    # --- one-variable data: lists ---
    if not done and sub in DATA_SUBS:
        lists = []
        for m in re.finditer(r'((?:-?\d+(?:\.\d+)?\s*,\s*(?:\\[ ,]|\\ )?\s*){3,}-?\d+(?:\.\d+)?)', q.replace('$', '').replace('\\ ', ' ').replace('{,}', '')):
            vals = [sp.nsimplify(v) for v in re.findall(r'-?\d+(?:\.\d+)?', m.group(1))]
            if len(vals) >= 4: lists.append(vals)
        if lists:
            Lv = lists[0]; s = ','.join(str(v) for v in Lv)
            steps.append({'t': 'Type the data as a list.', 'c': [chip(f'L=[{s}]', f'L=\\left[{s}\\right]')]})
            fun = []
            if 'mean' in qtxt or 'average' in qtxt: fun.append(('mean(L)', sum(Lv) / len(Lv)))
            if 'median' in qtxt: fun.append(('median(L)', sp.Rational(sorted(Lv)[(len(Lv) - 1) // 2] + sorted(Lv)[len(Lv) // 2], 2)))
            if 'range' in qtxt: fun.append(('max(L)-min(L)', max(Lv) - min(Lv)))
            if 'standard deviation' in qtxt or 'sd' in qtxt.split():
                m_ = sum(Lv) / len(Lv); fun.append(('stdev(L)', sp.sqrt(sum((v - m_)**2 for v in Lv) / (len(Lv) - 1))))
            for t, v in fun:
                steps.append({'t': 'On a new line type', 'c': [chip(t, '\\operatorname{' + t.split('(')[0] + '}\\left(L\\right)' if '-' not in t else '\\max\\left(L\\right)-\\min\\left(L\\right)')], 'r': f'Desmos shows <b>{fmt(v)}</b>.'}); nums.append(v)
            done = True

    # --- graph only: help read it ---
    if done == 'graph' and len(steps) <= 2:
        steps.append({'t': 'Click the graph to see its key points (intercepts, turning points, crossings) in grey, then compare them with what the question asks.'})

    # --- computations from the solution (the author's own Desmos lines) ---
    comp = []
    for c in codes:
        try:
            if re.search(r'[a-zA-Z]', re.sub(r'sqrt|pi|floor|ceil|round|abs|mean|median|stdev|min|max|nCr|nPr|mod|sin|cos|tan|ln|log', '', c)) :
                comp.append((c, None)); continue
            cc = c.split('=')[0] if c.count('=') == 1 and not REL.search(c) else c
            v = type2sym(cc.replace('nCr', 'binomial'))
            comp.append((c, v if v.is_number else None))
        except Exception:
            comp.append((c, None))
    norm = lambda z: re.sub(r'\s|^y=', '', z)
    have = {norm(c['s']) for st_ in steps for c in st_.get('c', [])}
    have |= {norm(c['s'].split('=', 1)[1]) for st_ in steps for c in st_.get('c', []) if c['s'].startswith('y=')}
    comp = [(c, v) for c, v in comp if norm(c) not in have and norm(c.split('=')[0]) not in have]
    if comp:
        lead = 'Use Desmos for the arithmetic: type each line.' if not steps else 'Then type these lines.'
        for i, (c, v) in enumerate(comp[:5]):
            st = {'t': lead if i == 0 else 'Next line:', 'c': [chip(c, None)]}
            if v is not None and fmt(v): st['r'] = f'Desmos shows <b>{fmt(v)}</b>.'; nums.append(v)
            steps.append(st)
    # --- arithmetic hidden in the written steps (when nothing else) ---
    if not comp and len(steps) <= (1 if deg else 0):
        k = 0
        for stx in x['steps']:
            for seg in math_segs(stx):
                if '=' not in seg: continue
                try:
                    parts = [tex2type(p) for p in seg.split('=')]
                except Exception:
                    continue
                left = parts[0] if len(parts) == 2 else parts[-2]
                if not re.fullmatch(r'[0-9+\-*/().^sqrtpi]+', left) or not re.search(r'[+\-*/^]|sqrt', left.lstrip('-')): continue
                try:
                    v = type2sym(left); w = type2sym(parts[-1])
                    if not (v.is_number and w.is_number) or abs(float(v) - float(w)) > 1e-6 * max(1, abs(float(w))): continue
                except Exception:
                    continue
                steps.append({'t': 'Type the calculation.' if k == 0 else 'Next line:', 'c': [chip(left, None)], 'r': f'Desmos shows <b>{fmt(v)}</b>.'}); nums.append(v); k += 1
                if k >= 3: break
            if k >= 3: break

    reason = sub in REASON_SUBS and not comp and len(steps) == 0
    if not steps:
        if reason:
            steps.append({'t': 'Desmos is not the tool here: this question tests how to read a study, sample or display, not a calculation. Use the reasoning in the solution above.'})
        else:
            steps.append({'t': 'This one is faster by reasoning than by graphing (see the solution above). Use Desmos to check: type the numbers or expressions from the question and compare them with the answer choices.'})
    # --- bridge when Desmos gives an intermediate value ---
    keyv0 = None
    try:
        keyv0 = float(x['key']) if not x['mc'] else float(sp.N(type2sym(tex2type(opts[x['key']]))))
    except Exception:
        pass
    reached = keyv0 is not None and any(abs(float(sp.N(v)) - keyv0) < max(0.0006, 1e-6 * abs(keyv0)) for v in nums if getattr(sp.N(v), 'is_real', False) or isinstance(v, (int, float)))
    if any(s_.get('r') for s_ in steps) and not reached:
        steps.append({'t': 'Use what Desmos showed in the last step of the written solution above to finish.'})
    # --- answer ---
    if opts:
        ans = f'That matches choice <b>{"ABCD"[x["key"]]}</b>: {esc(opts[x["key"]])}.'
    else:
        ans = f'Enter <b>${esc(x.get("disp", ""))}$</b> in the answer box.'
    steps.append({'t': ans, 'fin': True})
    # answer check
    keyv = None
    try:
        keyv = float(x['key']) if not x['mc'] else float(sp.N(type2sym(tex2type(opts[x['key']]))))
    except Exception:
        keyv = None
    hit = False
    if keyv is not None:
        for v in nums:
            try:
                if abs(float(sp.N(v)) - keyv) <= 1e-6 * max(1, abs(keyv)) or abs(float(sp.N(v)) - keyv) < 0.0006: hit = True; break
            except Exception: pass
    return steps, {'nsteps': len(steps), 'specific': any(s.get('c') for s in steps), 'hit': hit, 'keynum': keyv is not None, 'readouts': sum(1 for s in steps if s.get('r'))}
