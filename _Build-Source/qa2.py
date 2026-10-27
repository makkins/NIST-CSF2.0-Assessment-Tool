import re, json, sys
from docx import Document
sys.path.insert(0,'.')
from qa import BANNED, BRIT, EMOJI, text_of
files={}
for f in ["enrich_activities.py","enrich.py","map_template.html","audit_template.html","master.py"]:
    files[f]=open(f,encoding="utf-8").read()
M="out/NIST-CSF2-Document-Framework/00_Master/"
for f in ["Framework-Summary_EN.docx","Framework-Summary_TH.docx","Tailoring-Guide_EN.docx","Tailoring-Guide_TH.docx"]:
    files[f]=text_of(M+f)
import openpyxl
wb=openpyxl.load_workbook(M+"Document-Register-and-CSF-Traceability.xlsx")
files["xlsx"]="\n".join(str(c.value) for ws in wb for row in ws.iter_rows() for c in row if c.value)
for name,s in files.items():
    for pat,lab in [("—","em dash"),("–","en dash"),(r"\be\.g\.",'e.g.'),(r"\betc\.",'etc.'),(r"\bi\.e\.",'i.e.')]:
        for m in re.finditer(pat,s): print(name,lab,repr(s[max(0,m.start()-40):m.end()+40]))
    for m in re.finditer(BANNED,s,re.I): print(name,"BANNED",repr(s[max(0,m.start()-40):m.end()+40]))
    for m in re.finditer(BRIT,s,re.I): print(name,"BRIT",repr(s[max(0,m.start()-40):m.end()+40]))
    for m in EMOJI.finditer(s): print(name,"EMOJI",repr(s[max(0,m.start()-20):m.end()+20]))
print("done")
