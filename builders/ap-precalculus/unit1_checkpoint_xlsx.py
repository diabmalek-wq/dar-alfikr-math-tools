from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter as L
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule, FormulaRule

NAVY = "1F3A5F"
parts = [  # (question, part label, lesson, cluster)
 ("Q1","A(i)","1.3"),("Q1","A(ii)","1.3"),("Q1","B(i)","1.2"),("Q1","B(ii)","1.2"),("Q1","B(iii)","1.4"),("Q1","C","1.3"),
 ("Q2","B(i)","1.2"),("Q2","B(ii)","1.2"),("Q2","B(iii)","1.4"),
 ("Q3","B(i)","1.2"),("Q3","B(ii)","1.2"),("Q3","B(iii)","1.4"),
 ("Q4","B(i)","1.5"),("Q4","B(ii)","1.6"),
 ("Q5","A","1.1"),("Q5","B","1.2"),("Q5","C","1.4"),
 ("Q6","A","1.5"),("Q6","B","1.5"),("Q6","C","1.6"),("Q6","D","1.5"),
 ("Q7","A(i)","1.10"),("Q7","A(ii)","1.10"),("Q7","B(i)","1.8"),("Q7","B(ii)","1.8"),
 ("Q7","C(i)","1.9"),("Q7","C(ii)","1.9"),("Q7","D(i)","1.7"),("Q7","D(ii)","1.7"),
]
assert len(parts) == 29
def cluster(les):
    return "C1" if les in ("1.1","1.2","1.3","1.4") else ("C2" if les in ("1.5","1.6") else "C3")
partA = {"Q1","Q2","Q3","Q4"}

wb = Workbook()
# ------------------------------------------------------------- Settings
st = wb.active; st.title = "Settings"
hfont = Font(bold=True, color="FFFFFF"); hfill = PatternFill("solid", fgColor=NAVY)
st["A1"] = "AP Precalculus Unit 1 Checkpoint (Lessons 1.1 to 1.10): thresholds"; st["A1"].font = Font(bold=True, size=14, color=NAVY)
rows = [("Ready band: total at or above", 0.75), ("Developing band: total at or above", 0.60),
        ("Cluster flag: student cluster score below", 0.60), ("Cluster review: class cluster average below", 0.70),
        ("Group share in Intervention band that triggers a group plan", 0.30), ("Students flagged on the same cluster that trigger a group plan", 2)]
for i, (a, b) in enumerate(rows, start=3):
    st.cell(i, 1, a); c = st.cell(i, 2, b); c.fill = PatternFill("solid", fgColor="FFF2CC")
    if b < 1: c.number_format = "0%"
st["A10"] = "Change a yellow cell and every sheet updates. Defaults follow the answer key (section 5)."
st["A10"].font = Font(italic=True, color="6B7280")
st.column_dimensions["A"].width = 62; st.column_dimensions["B"].width = 12

# ------------------------------------------------------------- Marks
ws = wb.create_sheet("Marks")
ws["A1"] = "Marks entry: type 1 for a mark earned and 0 for a mark not earned in each part (yellow cells only)."
ws["A1"].font = Font(bold=True, size=12, color=NAVY)
first_col = 3; last_col = first_col + len(parts) - 1       # C .. AE
for k, (q, p, les) in enumerate(parts):
    c = first_col + k
    ws.cell(3, c, les); ws.cell(4, c, cluster(les)); ws.cell(5, c, 1); ws.cell(6, c, f"{q} {p}")
ws.cell(3, 1, "Lesson"); ws.cell(4, 1, "Cluster"); ws.cell(5, 1, "Max marks"); ws.cell(6, 2, "Student"); ws.cell(6, 1, "#")
S0, S1 = 7, 18                                              # 12 student rows
tot_c = last_col + 1
heads = ["Total /29", "Total %", "Part A /14", "Part B /15", "C1 /15", "C2 /6", "C3 /8", "C1 %", "C2 %", "C3 %", "Band", "Flagged clusters"]
for j, h in enumerate(heads): ws.cell(6, tot_c + j, h)
rng = lambda r: f"{L(first_col)}{r}:{L(last_col)}{r}"
hdr = f"${L(first_col)}$4:${L(last_col)}$4"; mx = f"${L(first_col)}$5:${L(last_col)}$5"
ptA = [k for k, (q, p, l) in enumerate(parts) if q in partA]
for r in range(S0, S1 + 1):
    ws.cell(r, 1, r - S0 + 1)
    for c in range(first_col, last_col + 1): ws.cell(r, c).fill = PatternFill("solid", fgColor="FFF2CC")
    T = L(tot_c)
    ws.cell(r, tot_c, f'=IF(COUNT({rng(r)})=0,"",SUM({rng(r)}))')
    ws.cell(r, tot_c + 1, f'=IF({T}{r}="","",{T}{r}/SUM({mx}))'); ws.cell(r, tot_c + 1).number_format = "0%"
    ws.cell(r, tot_c + 2, f'=IF({T}{r}="","",SUM({L(first_col)}{r}:{L(first_col + 13)}{r}))')
    ws.cell(r, tot_c + 3, f'=IF({T}{r}="","",SUM({L(first_col + 14)}{r}:{L(last_col)}{r}))')
    for j, cl in enumerate(("C1", "C2", "C3")):
        ws.cell(r, tot_c + 4 + j, f'=IF({T}{r}="","",SUMIF({hdr},"{cl}",{rng(r)}))')
        ws.cell(r, tot_c + 7 + j, f'=IF({T}{r}="","",{L(tot_c + 4 + j)}{r}/SUMIF({hdr},"{cl}",{mx}))')
        ws.cell(r, tot_c + 7 + j).number_format = "0%"
    P = L(tot_c + 1)
    ws.cell(r, tot_c + 10, f'=IF({T}{r}="","",IF({P}{r}>=Settings!$B$3,"Ready",IF({P}{r}>=Settings!$B$4,"Developing","Intervention")))')
    c1, c2, c3 = L(tot_c + 7), L(tot_c + 8), L(tot_c + 9)
    ws.cell(r, tot_c + 11, f'=IF({T}{r}="","",TRIM(IF({c1}{r}<Settings!$B$5,"C1 ","")&IF({c2}{r}<Settings!$B$5,"C2 ","")&IF({c3}{r}<Settings!$B$5,"C3","")))')
# class row
CR = S1 + 2
ws.cell(CR, 2, "Class % correct per part")
for c in range(first_col, last_col + 1):
    cl = L(c); ws.cell(CR, c, f'=IF(COUNT({cl}{S0}:{cl}{S1})=0,"",AVERAGE({cl}{S0}:{cl}{S1}))'); ws.cell(CR, c).number_format = "0%"
dv = DataValidation(type="list", formula1='"0,1"', allow_blank=True, showErrorMessage=True, errorTitle="Marks", error="Enter 1 or 0.")
ws.add_data_validation(dv); dv.add(f"{L(first_col)}{S0}:{L(last_col)}{S1}")
for c in range(1, tot_c + 12):
    for r in (3, 4, 5, 6):
        cell = ws.cell(r, c); cell.font = Font(bold=True, color="FFFFFF" if r == 6 else NAVY, size=9)
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        if r == 6: cell.fill = hfill
ws.row_dimensions[6].height = 42
ws.column_dimensions["A"].width = 9; ws.column_dimensions["B"].width = 26
for c in range(first_col, last_col + 1): ws.column_dimensions[L(c)].width = 6.5
for j in range(12): ws.column_dimensions[L(tot_c + j)].width = 11
ws.column_dimensions[L(tot_c + 11)].width = 16
red = PatternFill("solid", bgColor="F8CBAD", fgColor="F8CBAD"); amb = PatternFill("solid", bgColor="FFE699", fgColor="FFE699"); grn = PatternFill("solid", bgColor="C6E0B4", fgColor="C6E0B4")
bc = f"{L(tot_c + 10)}{S0}:{L(tot_c + 10)}{S1}"
ws.conditional_formatting.add(bc, CellIsRule(operator="equal", formula=['"Intervention"'], fill=red))
ws.conditional_formatting.add(bc, CellIsRule(operator="equal", formula=['"Developing"'], fill=amb))
ws.conditional_formatting.add(bc, CellIsRule(operator="equal", formula=['"Ready"'], fill=grn))
ws.freeze_panes = ws.cell(7, 3)

# ------------------------------------------------------------- Group decision
gd = wb.create_sheet("Group decision")
gd["A1"] = "Group readiness and intervention decision"; gd["A1"].font = Font(bold=True, size=14, color=NAVY)
M = "Marks!"
col = lambda off: f"{M}${L(tot_c + off)}${S0}:${L(tot_c + off)}${S1}"
gd["A3"] = "Students with marks entered"; gd["B3"] = f"=COUNT({col(0)})"
gd["A4"] = "Class average total"; gd["B4"] = f'=IF(B3=0,"",AVERAGE({col(1)}))'; gd["B4"].number_format = "0.0%"
gd["A5"] = "Students in Ready band"; gd["B5"] = f'=COUNTIF({col(10)},"Ready")'
gd["A6"] = "Students in Developing band"; gd["B6"] = f'=COUNTIF({col(10)},"Developing")'
gd["A7"] = "Students in Intervention band"; gd["B7"] = f'=COUNTIF({col(10)},"Intervention")'
gd["A8"] = "Share of group in Intervention band"; gd["B8"] = '=IF(B3=0,"",B7/B3)'; gd["B8"].number_format = "0%"
hdrs = ["Cluster", "Lessons", "Class average", "Below class threshold?", "Students flagged"]
for j, h in enumerate(hdrs, start=1):
    c = gd.cell(10, j, h); c.font = hfont; c.fill = hfill; c.alignment = Alignment(wrap_text=True)
cl_info = [("C1 Rates of change and concavity", "1.1 to 1.4", 7), ("C2 Polynomial zeros and end behavior", "1.5 to 1.6", 8), ("C3 Rational functions", "1.7 to 1.10", 9)]
for i, (n, ls, off) in enumerate(cl_info, start=11):
    gd.cell(i, 1, n); gd.cell(i, 2, ls)
    gd.cell(i, 3, f'=IF($B$3=0,"",AVERAGE({col(off)}))'); gd.cell(i, 3).number_format = "0%"
    gd.cell(i, 4, f'=IF($B$3=0,"",IF(C{i}<Settings!$B$6,"Yes","No"))')
    gd.cell(i, 5, f'=COUNTIF({col(11)},"*C{i - 10}*")')
gd["A15"] = "Triggers met"; gd["A15"].font = Font(bold=True)
gd["A16"] = "Intervention share at or above threshold"; gd["B16"] = '=IF(B3=0,"",IF(B8>=Settings!$B$7,"Yes","No"))'
gd["A17"] = "A cluster average below threshold"; gd["B17"] = '=IF(B3=0,"",IF(COUNTIF(D11:D13,"Yes")>0,"Yes","No"))'
gd["A18"] = "Same cluster flagged for enough students"; gd["B18"] = '=IF(B3=0,"",IF(MAX(E11:E13)>=Settings!$B$8,"Yes","No"))'
gd["A20"] = "DECISION"; gd["A20"].font = Font(bold=True, size=13, color=NAVY)
gd["B20"] = '=IF(B3=0,"Enter marks first",IF(COUNTIF(B16:B18,"Yes")>0,"INTERVENTION PLAN REQUIRED","No group intervention: individual clinics only"))'
gd["B20"].font = Font(bold=True, size=13)
gd.conditional_formatting.add("B20", FormulaRule(formula=['LEFT($B$20,12)="INTERVENTION"'], fill=red))
gd.conditional_formatting.add("B20", FormulaRule(formula=['LEFT($B$20,2)="No"'], fill=grn))
gd["A21"] = "Weakest cluster to reteach first"
gd["B21"] = '=IF(B3=0,"",INDEX(A11:A13,MATCH(MIN(C11:C13),C11:C13,0)))'
# lesson table
gd["A23"] = "Mastery by lesson"; gd["A23"].font = Font(bold=True)
for j, h in enumerate(["Lesson", "Marks available", "Class % earned"], start=1):
    c = gd.cell(24, j, h); c.font = hfont; c.fill = hfill
lessons = ["1.1", "1.2", "1.3", "1.4", "1.5", "1.6", "1.7", "1.8", "1.9", "1.10"]
lrow = f"Marks!${L(first_col)}$3:${L(last_col)}$3"
for i, les in enumerate(lessons, start=25):
    gd.cell(i, 1, les)
    gd.cell(i, 2, f'=SUMIF({lrow},A{i},Marks!${L(first_col)}$5:${L(last_col)}$5)')
    rngd = f"Marks!${L(first_col)}${S0}:${L(last_col)}${S1}"
    gd.cell(i, 3, f'=IF($B$3=0,"",SUMPRODUCT(({lrow}=A{i})*{rngd})/(B{i}*$B$3))'); gd.cell(i, 3).number_format = "0%"
gd.conditional_formatting.add("C25:C34", CellIsRule(operator="lessThan", formula=["Settings!$B$6"], fill=red))
gd.column_dimensions["A"].width = 46
for c in "BCDE": gd.column_dimensions[c].width = 24
gd["A36"] = "Mark map: C1 = lessons 1.1 to 1.4 (15 marks), C2 = 1.5 to 1.6 (6 marks), C3 = 1.7 to 1.10 (8 marks)."
gd["A36"].font = Font(italic=True, color="6B7280")
wb.move_sheet("Group decision", offset=-1)
wb.save("AP-Precalc_Unit1_Checkpoint_Class-Analysis.xlsx")
print("saved")
