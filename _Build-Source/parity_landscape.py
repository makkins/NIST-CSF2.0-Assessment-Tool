# -*- coding: utf-8 -*-
"""Parity test (plan W1-4): Landscape facts from Python (landscape_facts.py) and from the Gap Analysis HTML (JavaScript)
must match on the CMC sample. Compares the two JSON objects after import of the same Interview Excel export.
Usage: python parity_landscape.py <Gap-Analysis-Compact.html> <interview.xlsx>
Ignored fields: asOf (the date of the run). Exit code 1 on any difference."""
import sys, os, json, pathlib
from playwright.sync_api import sync_playwright
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "00_Master" / "Gap-Analysis-Method" / "tools"))
import landscape_facts
html, xlsx = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2])
py = json.loads(json.dumps(landscape_facts.build(xlsx), ensure_ascii=False))
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_context(viewport={"width": 1400, "height": 900}).new_page(); errs = []
    pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.goto("file://" + html); pg.wait_for_timeout(400)
    pg.click('[data-tab="setup"]'); pg.set_input_files("#f-xlsx", xlsx); pg.wait_for_timeout(1500)
    js = pg.evaluate("JSON.parse(JSON.stringify(landscapeFacts()))")
    b.close()
def diff(a, c, path=""):
    out = []
    if isinstance(a, dict) and isinstance(c, dict):
        for k in sorted(set(a) | set(c)):
            if k == "asOf" and path == "":
                continue
            if k not in a: out.append(f"{path}/{k}: only in HTML")
            elif k not in c: out.append(f"{path}/{k}: only in Python")
            else: out += diff(a[k], c[k], f"{path}/{k}")
    elif isinstance(a, list) and isinstance(c, list):
        if len(a) != len(c): out.append(f"{path}: length Python {len(a)} vs HTML {len(c)}")
        for i, (x, y) in enumerate(zip(a, c)): out += diff(x, y, f"{path}[{i}]")
    elif a != c:
        out.append(f"{path}: Python {str(a)[:80]!r} vs HTML {str(c)[:80]!r}")
    return out
d = diff(py, js)
print(("PASS" if not d and not errs else "FAIL"), "Landscape facts parity (Python vs JavaScript):", sum(len(x["facts"]) for x in py["blocks"].values()), "facts")
for x in d[:25]: print(" -", x)
for e in errs[:3]: print(" - page error:", e)
sys.exit(1 if d or errs else 0)
