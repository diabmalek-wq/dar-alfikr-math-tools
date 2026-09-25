"""Class analysis workbook for the three GAT quantitative mocks.

The point of this file is NOT the total score. A GAT total tells Mr Thiab that a
student is weak; it does not tell him what to teach on Sunday. So every sheet
computes three things the total hides:

  1. a per-student strand profile, because 24/40 built on weak arithmetic and
     24/40 built on weak geometry need opposite lessons;
  2. per-question facility across the class; and
  3. the most common WRONG option on each question, with a TEACH flag when half
     the class or more chose the same one. A shared wrong answer is a shared
     misconception, and the item map names the trick behind it.

Everything is live formulas — type the letters in and the whole sheet moves.
"""
import json
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

META = json.load(open("mock_meta.json"))
LET = "ABCD"
N_Q = 40
N_STUDENTS = 30

TEAL = "0E6E68"; PALE = "E8EFEF"; YELL = "FFF7D6"; RED = "C62828"
ARIAL = "Arial"
thin = Side(style="thin", color="9AA6A5")
BOX = Border(left=thin, right=thin, top=thin, bottom=thin)

HDR = Font(name=ARIAL, size=9, bold=True, color="FFFFFF")
BOLD = Font(name=ARIAL, size=9, bold=True)
BODY = Font(name=ARIAL, size=9)
BLUE = Font(name=ARIAL, size=9, bold=True, color="0000FF")   # given, do not edit
NOTE = Font(name=ARIAL, size=8, italic=True, color="555555")

FILL_H = PatternFill("solid", fgColor=TEAL)
FILL_P = PatternFill("solid", fgColor=PALE)
FILL_Y = PatternFill("solid", fgColor=YELL)

wb = Workbook()

# ------------------------------------------------------------------ how to use
ws = wb.active
ws.title = "How to use"
ws.column_dimensions["A"].width = 4
ws.column_dimensions["B"].width = 104
rows = [
    ("Dar Alfikr Schools · Mathematics Department · Mr Malek Thiab", BOLD),
    ("GAT (Qudurat) Quantitative Mocks 1–3 · Grade 12 · Semester 1, 2026–27", BOLD),
    ("", BODY),
    ("WHAT TO TYPE", BOLD),
    ("On each mock sheet, type student names in column A and their chosen letter "
     "(A, B, C or D) in the shaded cells under Q1 to Q40. Leave a cell blank if the "
     "student did not answer. Those shaded cells are the only ones to edit.", BODY),
    ("Everything else is a formula and will fill itself in.", BODY),
    ("", BODY),
    ("WHAT THE SHEET GIVES BACK", BOLD),
    ("Score and %  — the total, out of 40.", BODY),
    ("ARI / ALG / GEO / DAT / LOG  — the same student split by strand, as a percentage. "
     "This is the column to teach from. Two students on 24/40 can need opposite lessons.", BODY),
    ("% correct  — the share of the class that got each question right.", BODY),
    ("Common wrong  — the wrong option most of the class chose on that question.", BODY),
    ("TEACH  — appears when half the class or more picked the SAME wrong option. That is a "
     "shared misconception, not bad luck. Look the question up on the Item map sheet: it "
     "names the trick the question was built on and what that wrong option means.", BODY),
    ("", BODY),
    ("HOW TO READ THE THREE MOCKS TOGETHER", BOLD),
    ("The three papers are sampled to the same ETEC blueprint (14 arithmetic, 7 algebra, "
     "7 geometry, 7 data, 5 word logic) and each carries ten level-3 items, so they are of "
     "equal difficulty by construction. A change in a strand percentage between mocks is a "
     "change in the student, not in the paper. The Progress sheet plots that.", BODY),
    ("", BODY),
    ("BLUE text is given — the answer key, strands and levels. Do not overwrite it.", BLUE),
    ("SHADED cells are yours to fill in.", BODY),
]
for i, (txt, f) in enumerate(rows, start=1):
    c = ws.cell(row=i, column=2, value=txt)
    c.font = f
    c.alignment = Alignment(wrap_text=True, vertical="top")
    if len(txt) > 90:
        ws.row_dimensions[i].height = 30

# --------------------------------------------------------------- a mock sheet
FIRST_Q_COL = 2                         # B
LAST_Q_COL = FIRST_Q_COL + N_Q - 1      # AO
KEY_R, STR_R, LVL_R = 4, 5, 6
FIRST_S, LAST_S = 8, 8 + N_STUDENTS - 1

def qc(i):
    return get_column_letter(FIRST_Q_COL + i)

def mock_sheet(n, items):
    ws = wb.create_sheet(f"Mock {n}")
    ws.freeze_panes = "B8"
    ws.column_dimensions["A"].width = 22
    for i in range(N_Q):
        ws.column_dimensions[qc(i)].width = 4.2

    ws["A1"] = f"GAT Quantitative Mock {n} — class analysis"
    ws["A1"].font = Font(name=ARIAL, size=12, bold=True, color=TEAL)
    ws["A2"] = ("Type letters in the shaded cells only. Blue rows are the key and are given. "
                "40 items · blueprint 14 ARI / 7 ALG / 7 GEO / 7 DAT / 5 LOG.")
    ws["A2"].font = NOTE

    ws.cell(row=3, column=1, value="Student").font = HDR
    ws.cell(row=3, column=1).fill = FILL_H
    for i in range(N_Q):
        c = ws.cell(row=3, column=FIRST_Q_COL + i, value=f"Q{i+1}")
        c.font = HDR; c.fill = FILL_H; c.alignment = Alignment(horizontal="center")
        c.border = BOX

    for r, lab in ((KEY_R, "Answer key"), (STR_R, "Strand"), (LVL_R, "Level")):
        c = ws.cell(row=r, column=1, value=lab)
        c.font = BLUE; c.fill = FILL_P; c.border = BOX
    for i, it in enumerate(items):
        for r, v in ((KEY_R, LET[it["ans"]]),
                     (STR_R, it["code"].split(".")[0].replace("GAT-Q-", "")),
                     (LVL_R, it["lvl"])):
            c = ws.cell(row=r, column=FIRST_Q_COL + i, value=v)
            c.font = BLUE; c.fill = FILL_P; c.border = BOX
            c.alignment = Alignment(horizontal="center")

    # ---- summary column headers
    cols = [("Score", 7), ("%", 7), ("ARI", 6), ("ALG", 6), ("GEO", 6),
            ("DAT", 6), ("LOG", 6)]
    base = LAST_Q_COL + 2
    for j, (lab, w) in enumerate(cols):
        L = get_column_letter(base + j)
        ws.column_dimensions[L].width = w
        c = ws.cell(row=3, column=base + j, value=lab)
        c.font = HDR; c.fill = FILL_H; c.border = BOX
        c.alignment = Alignment(horizontal="center")

    Q0, Q1 = qc(0), qc(N_Q - 1)
    dv = DataValidation(type="list", formula1='"A,B,C,D"', allow_blank=True)
    ws.add_data_validation(dv)

    for r in range(FIRST_S, LAST_S + 1):
        nm = ws.cell(row=r, column=1)
        nm.font = BODY; nm.fill = FILL_Y; nm.border = BOX
        for i in range(N_Q):
            c = ws.cell(row=r, column=FIRST_Q_COL + i)
            c.font = BODY; c.fill = FILL_Y; c.border = BOX
            c.alignment = Alignment(horizontal="center")
        dv.add(f"{Q0}{r}:{Q1}{r}")

        rng = f"{Q0}{r}:{Q1}{r}"
        key = f"$={Q0}$4"  # placeholder, replaced below
        ws.cell(row=r, column=base,
                value=f"=SUMPRODUCT(--({rng}=${Q0}${KEY_R}:${Q1}${KEY_R}))").font = BODY
        ws.cell(row=r, column=base + 1,
                value=f"={get_column_letter(base)}{r}/{N_Q}").font = BODY
        ws.cell(row=r, column=base + 1).number_format = "0%"
        for j, s in enumerate(["ARI", "ALG", "GEO", "DAT", "LOG"]):
            f = (f'=IFERROR(SUMPRODUCT(--(${Q0}${STR_R}:${Q1}${STR_R}="{s}"),'
                 f'--({rng}=${Q0}${KEY_R}:${Q1}${KEY_R}))'
                 f'/COUNTIF(${Q0}${STR_R}:${Q1}${STR_R},"{s}"),"")')
            c = ws.cell(row=r, column=base + 2 + j, value=f)
            c.font = BODY; c.number_format = "0%"
        for j in range(len(cols)):
            ws.cell(row=r, column=base + j).border = BOX

    # ---- an example row, clearly marked, so the format is unambiguous
    ws.cell(row=FIRST_S, column=1, value="EXAMPLE — delete this row")
    ws.cell(row=FIRST_S, column=1).font = Font(name=ARIAL, size=9, italic=True,
                                               color=RED)
    demo = "ACBDBACDBADCABCDBADCACBDBADCABDCBACDBADC"
    for i in range(N_Q):
        ws.cell(row=FIRST_S, column=FIRST_Q_COL + i, value=demo[i])

    # ---- per-question analysis
    r0 = LAST_S + 2
    labels = ["% correct", "Common wrong", "TEACH?"]
    counts0 = r0 + 4
    for k, lab in enumerate(labels):
        c = ws.cell(row=r0 + k, column=1, value=lab)
        c.font = BOLD; c.fill = FILL_P; c.border = BOX
    for k, L in enumerate(LET):
        c = ws.cell(row=counts0 + k, column=1, value=f"chose {L}")
        c.font = NOTE
    ws.cell(row=counts0 + 4, column=1, value="answered").font = NOTE

    for i in range(N_Q):
        L = qc(i)
        col = FIRST_Q_COL + i
        ans = f"{L}{counts0+4}"
        ws.cell(row=counts0 + 4, column=col,
                value=f"=COUNTA({L}{FIRST_S}:{L}{LAST_S})").font = NOTE
        for k, opt in enumerate(LET):
            # the correct option is scored -1 so it can never win "most common wrong"
            f = (f'=IF(${L}${KEY_R}="{opt}",-1,'
                 f'COUNTIF({L}${FIRST_S}:{L}${LAST_S},"{opt}"))')
            ws.cell(row=counts0 + k, column=col, value=f).font = NOTE
        pc = (f'=IF({ans}=0,"",COUNTIF({L}{FIRST_S}:{L}{LAST_S},${L}${KEY_R})/{ans})')
        c = ws.cell(row=r0, column=col, value=pc)
        c.font = BODY; c.number_format = "0%"; c.border = BOX
        c.alignment = Alignment(horizontal="center")
        cw = (f'=IF({ans}=0,"",INDEX({{"A","B","C","D"}},'
              f'MATCH(MAX({L}{counts0}:{L}{counts0+3}),{L}{counts0}:{L}{counts0+3},0)))')
        c = ws.cell(row=r0 + 1, column=col, value=cw)
        c.font = BODY; c.border = BOX; c.alignment = Alignment(horizontal="center")
        fl = (f'=IF({ans}=0,"",IF(MAX({L}{counts0}:{L}{counts0+3})/{ans}>=0.5,"TEACH",""))')
        c = ws.cell(row=r0 + 2, column=col, value=fl)
        c.font = Font(name=ARIAL, size=8, bold=True, color=RED)
        c.border = BOX; c.alignment = Alignment(horizontal="center")

    ws.cell(row=r0 + 3, column=1,
            value="TEACH means half the class or more chose the SAME wrong option — "
                  "look the question up on the Item map sheet.").font = NOTE
    return ws

for n, items in enumerate(META, start=1):
    mock_sheet(n, items)

# ------------------------------------------------------------------ item map
ws = wb.create_sheet("Item map")
heads = ["Mock", "Q", "Strand", "Sub-skill code", "Level", "Correct", "The trick it tests"]
widths = [7, 5, 8, 17, 7, 9, 96]
for j, (h, w) in enumerate(zip(heads, widths), start=1):
    c = ws.cell(row=1, column=j, value=h)
    c.font = HDR; c.fill = FILL_H; c.border = BOX
    ws.column_dimensions[get_column_letter(j)].width = w
r = 2
for n, items in enumerate(META, start=1):
    for i, it in enumerate(items, start=1):
        vals = [n, i, it["code"].split(".")[0].replace("GAT-Q-", ""),
                it["code"] + " · " + it["sig"], it["lvl"], LET[it["ans"]], it["trick"]]
        for j, v in enumerate(vals, start=1):
            c = ws.cell(row=r, column=j, value=v)
            c.font = BODY if j != 7 else Font(name=ARIAL, size=8)
            c.border = BOX
            c.alignment = Alignment(wrap_text=(j == 7), vertical="top")
        r += 1
ws.freeze_panes = "A2"

# ------------------------------------------------------------------ progress
ws = wb.create_sheet("Progress")
ws.column_dimensions["A"].width = 26
for j in range(2, 5):
    ws.column_dimensions[get_column_letter(j)].width = 12
ws["A1"] = "Class averages across the three mocks"
ws["A1"].font = Font(name=ARIAL, size=12, bold=True, color=TEAL)
ws["A2"] = ("The three papers carry the same blueprint and the same number of level-3 items, "
            "so a move in a row below is a move in the class, not in the paper.")
ws["A2"].font = NOTE
for j in range(3):
    c = ws.cell(row=4, column=2 + j, value=f"Mock {j+1}")
    c.font = HDR; c.fill = FILL_H; c.border = BOX
    c.alignment = Alignment(horizontal="center")
c = ws.cell(row=4, column=1, value="Measure"); c.font = HDR; c.fill = FILL_H; c.border = BOX

base = LAST_Q_COL + 2
SUMCOL = {"Overall %": base + 1, "Arithmetic": base + 2, "Algebra": base + 3,
          "Geometry": base + 4, "Data": base + 5, "Word logic": base + 6}
for i, (lab, col) in enumerate(SUMCOL.items()):
    L = get_column_letter(col)
    c = ws.cell(row=5 + i, column=1, value=lab)
    c.font = BOLD if lab == "Overall %" else BODY
    c.border = BOX
    for j in range(3):
        f = (f"=IFERROR(AVERAGEIF('Mock {j+1}'!$A${FIRST_S}:$A${LAST_S},\"<>\","
             f"'Mock {j+1}'!{L}${FIRST_S}:{L}${LAST_S}),\"\")")
        cc = ws.cell(row=5 + i, column=2 + j, value=f)
        cc.font = BODY; cc.number_format = "0%"; cc.border = BOX
        cc.alignment = Alignment(horizontal="center")
ws.cell(row=12, column=1,
        value="The example row must be deleted from each mock sheet before these "
              "averages mean anything.").font = NOTE
ws.cell(row=13, column=1,
        value="Blueprint for every mock: 14 arithmetic · 7 algebra · 7 geometry · "
              "7 data · 5 word logic · 10 level-3 items.").font = NOTE

wb.save("GAT_Mock_Analysis_Gr12_2026-27.xlsx")
print("wrote GAT_Mock_Analysis_Gr12_2026-27.xlsx")
