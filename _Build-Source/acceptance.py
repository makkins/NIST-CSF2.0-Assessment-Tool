# -*- coding: utf-8 -*-
"""CMC sample acceptance checks for the Gap Analysis HTML (Design Summary 15.1 and Landscape spec 8).
Usage: python acceptance.py <Gap-Analysis.html> <interview.xlsx> [more interview.xlsx ...]
Each Interview export is imported on a clean page together with the Workshop risk criteria from the CMC sample.
Then the CMC sample state is loaded and its Function outputs, Landscape lock, and flags are checked.
Exit code 1 when any check fails."""
import sys, os, json, pathlib
import openpyxl
from playwright.sync_api import sync_playwright

html = os.path.abspath(sys.argv[1]); xlsxs = sys.argv[2:]
HERE = pathlib.Path(__file__).resolve().parent
sample = json.load(open(HERE / "gap_sample" / "sample.json", encoding="utf-8"))
ws_path = "/tmp/_ws.json"; json.dump(sample["ws"], open(ws_path, "w", encoding="utf-8"))
res = []
def check(name, ok, info=""):
    res.append(ok); print(("PASS " if ok else "FAIL ") + name + (f"  [{info}]" if info else ""))

def fresh(b):
    ctx = b.new_context(viewport={"width": 1500, "height": 1000}); pg = ctx.new_page(); pg.errs = []
    pg.on("pageerror", lambda e: pg.errs.append(str(e))); ctx.route("**/fonts.googleapis.com/**", lambda r: r.abort())
    pg.goto("file://" + html); pg.wait_for_timeout(400); return pg

with sync_playwright() as p:
    b = p.chromium.launch()
    for xf in xlsxs:
        tag = os.path.basename(xf)[:40]
        pg = fresh(b)
        pg.click('[data-tab="setup"]')
        pg.set_input_files("#f-xlsx", xf); pg.wait_for_timeout(1500)
        pg.set_input_files("#f-ws", ws_path); pg.wait_for_timeout(800)
        wb = openpyxl.load_workbook(xf, read_only=True, data_only=True)
        nsys = sum(1 for r in wb["Systems (Quick BIA)"].iter_rows(min_row=2, values_only=True) if r[0])
        got = pg.evaluate("S.iv?{sys:S.iv.sys.length,schema:S.iv.meta.schema,ws:!!S.ws}:null")
        check(f"1 import without manual edits [{tag}]", bool(got) and got["ws"] and not pg.errs, f"{got} errors={pg.errs[:2]}")
        check(f"2a Landscape system count matches Systems sheet [{tag}]", bool(got) and got["sys"] == nsys, f"html {got and got['sys']} sheet {nsys}")
        st = pg.evaluate("SUBS.map(s=>subInfo(s).st)")
        check(f"2 every Subcategory has exactly one status [{tag}]", len(st) == 106 and all(x in ("Strength", "Meets with Observation", "Gap", "Not Assessed", "Meets", "Not assessed") for x in st), f"{len(st)} {sorted(set(st))}")
        pg.click('[data-tab="land"]'); pg.wait_for_timeout(300)
        nb = pg.evaluate("LSB.length"); txt = pg.inner_text("#v-land") if pg.query_selector("#v-land") else ""
        check(f"3 Landscape renders 14 blocks without edits [{tag}]", nb == 14 and all(f"B{i}" in txt for i in range(1, 15)) and not pg.errs, f"blocks {nb}")
        pg.click('[data-tab="ai"]'); pg.wait_for_timeout(300)
        gate = pg.evaluate("t().ls.gate"); ai = pg.inner_text("#v-ai")
        check(f"4 Stage 1 refuses to start while Landscape unlocked [{tag}]", gate[:30] in ai and pg.query_selector("#v-ai textarea") is None)
        pg.context.close()
    # CMC sample state
    pg = fresh(b); pg.click('[data-tab="setup"]'); pg.click("#b-sample"); pg.wait_for_timeout(500)
    for sel in ("#cf-ok", ".modal .danger", "dialog button.danger"):
        if pg.query_selector(sel):
            try: pg.click(sel, timeout=800)
            except Exception: pass
    pg.wait_for_timeout(400)
    r = pg.evaluate("""()=>FN.map(f=>{const o=curOut(f);const v=validateReply('an',f,JSON.stringify(o));
        const imps=o.improvementActions;return {f,ok:v.ok,err:v.err.slice(0,3),schema:o.schema,n:imps.length,
        cif:imps.filter(i=>i.changeInFlight).length,dep:imps.filter(i=>i.existingTool&&/^Deploy/.test(i.action)).length}})""")
    check("5 sample Function outputs pass the HTML validator", all(x["ok"] for x in r), "; ".join(f"{x['f']}:{x['schema'][-1]}:{x['n']}imps" for x in r) + "".join(f" ERR {x['f']} {x['err']}" for x in r if not x["ok"]))
    check("6a sample has a change-in-flight IMP", sum(x["cif"] for x in r) >= 1, f"{sum(x['cif'] for x in r)} IMPs")
    check("6b sample has a deploy-existing IMP (Landscape spec 8.4)", sum(x["dep"] for x in r) >= 1, f"{sum(x['dep'] for x in r)} IMPs. Known gap: no sample IMP uses the bought-not-deployed tool TOOL-07")
    locked = pg.evaluate("!!S.ls.locked"); l2 = pg.evaluate("l2Open()")
    check("7 sample Landscape locked and L2 reports zero open blocks", locked and not l2, f"locked {locked} open {l2}")
    stg = pg.evaluate("""()=>{let bad=[];FN.forEach(f=>{const o=curOut(f);o.categories.forEach(c=>c.gapFindings.forEach(g=>{const r=g.responses;
        (r.stageStatus?STG:STG.slice(0,4)).forEach(a=>{ if(r.stageStatus){ if(r.stageStatus[a]==='Required'&&!r[a].length)bad.push(g.id+':'+a);} else if(!r[a]||(!r[a].length&&!(r.notApplicable||{})[a]))bad.push(g.id+':'+a); });}));});return bad}""")
    check("8 every Gap Finding has IMPs per stage or a stated reason", not stg, str(stg[:4]))
    check("no page errors in sample run", not pg.errs, str(pg.errs[:2]))
    b.close()
print("RESULT", "PASS" if all(res) else "FAIL", f"{sum(res)}/{len(res)}")
sys.exit(0 if all(res) else 1)
