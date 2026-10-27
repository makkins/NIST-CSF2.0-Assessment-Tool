# -*- coding: utf-8 -*-
"""Rebuild the HTML tools (Information Gathering, Gap Analysis, and the standalone Document Audit Tracker and Document Map) and run the CMC sample checks.
Information Gathering replaces the Interview Assessment (spec v2.0); the old Full Gap Analysis is retired (plan W1-3).
Usage (from _Build-Source): python run_checks.py [--no-build]
Steps: build Information Gathering, Gap Analysis, Audit Tracker and Document Map; check_enums; validate.py on method examples and CMC sample JSON;
headless smoke test of each HTML; export a fresh Interview Excel; Information Gathering acceptance (spec v2.0 Section 16, includes the P1 handoff validator); acceptance checks on Gap Compact.
Needs: Python packages jsonschema, openpyxl, playwright."""
import subprocess, sys, pathlib, glob, tempfile, os

R = pathlib.Path(__file__).resolve().parent
M = R.parent / "00_Master"; TOOLS = M / "Gap-Analysis-Method" / "tools"; EX = M / "Gap-Analysis-Method" / "examples"
SAMPLE = R.parent / "Sample_file" / "CMC_Gap_Analyst_JSON"
tmp = tempfile.mkdtemp()
fails = []

def run(name, cmd, cwd=R, allow=()):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip().splitlines()
    ok = r.returncode == 0
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        fails.append(name)
        for l in out[-12:]: print("    " + l)
    return r

py = sys.executable
tracker = str(M / "Document-Audit-Tracker.html")
if "--no-build" not in sys.argv:
    run("build Information Gathering", [py, "build_ig.py", tracker, str(M / "Information-Gathering.html")])
    run("build Audit Tracker and Document Map", [py, "build_html.py"])
    run("build Gap (compact)", [py, "build_gap.py", tracker, str(M / "Gap-Analysis-Compact.html"), "--mode", "compact"])
run("Data Dictionary export is current", [py, "-c", "import dictionary,json,sys;d=json.load(open(sys.argv[1],encoding='utf-8'));sys.exit(0 if d==json.loads(json.dumps(dictionary.as_dict(),ensure_ascii=False)) else 1)", str(TOOLS / "dictionary.json")])
run("enums frozen (stage status, stage names)", [py, "-I", str(TOOLS / "check_enums.py"), str(R)])
facts = str(EX / "cmc-landscape-facts.json")
files = sorted(glob.glob(str(EX / "*.json"))) + sorted(glob.glob(str(SAMPLE / "CMC-gap-analyst-??.json"))) + [str(SAMPLE / "CMC-gap-xreview.json")]
for f in files:
    if os.path.exists(f):
        run("validate.py " + os.path.basename(f), [py, "-I", str(TOOLS / "validate.py"), f, "--input", facts])
xlsx = os.path.join(tmp, "iv.xlsx")
for h in ("Information-Gathering.html", "Gap-Analysis-Compact.html"):
    cmd = [py, "check_html.py", str(M / h)] + (["--save-xlsx", xlsx] if h.startswith("Information") else [])
    run("smoke " + h, cmd)
r = run("acceptance Information-Gathering.html (spec v2.0 Section 16)", [py, "ig_acceptance.py", str(M / "Information-Gathering.html")])
for l in r.stdout.splitlines(): print("    " + l)
r = run("Landscape facts parity, Python vs JavaScript (W1-4)", [py, "parity_landscape.py", str(M / "Gap-Analysis-Compact.html"), xlsx])
for l in r.stdout.splitlines(): print("    " + l)
for h in ("Gap-Analysis-Compact.html",):
    r = run("acceptance " + h, [py, "acceptance.py", str(M / h), xlsx])
    for l in (r.stdout.splitlines()): print("    " + l)
print("\nFAILED:" if fails else "\nALL PASS", ", ".join(fails))
sys.exit(1 if fails else 0)
