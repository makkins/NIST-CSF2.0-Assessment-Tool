# -*- coding: utf-8 -*-
"""Headless smoke test for the built HTML tools (plan W0 rebuild check).
Usage: python check_html.py <file.html> [--sample-btn ID] [--xlsx-btn ID] [--save-xlsx out.xlsx]
Opens the file, loads the CMC sample, clicks every tab (every stage first when the tool has stage navigation), exports Excel, and fails on any page error."""
import sys, argparse
from playwright.sync_api import sync_playwright

ap = argparse.ArgumentParser()
ap.add_argument("html"); ap.add_argument("--sample-btn", default="b-sample"); ap.add_argument("--xlsx-btn", default="b-xlsx")
ap.add_argument("--save-xlsx"); ap.add_argument("--confirm", default="")
a = ap.parse_args()
errs = []
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/opt/pw-browsers/chromium" if __import__("os").path.exists("/opt/pw-browsers/chromium") else None)
    ctx = b.new_context(accept_downloads=True, viewport={"width": 1500, "height": 1000})
    ctx.route("**/fonts.googleapis.com/**", lambda r: r.abort())
    pg = ctx.new_page()
    pg.on("pageerror", lambda e: errs.append("pageerror: " + str(e)))
    pg.on("console", lambda m: m.type == "error" and "ERR_FAILED" not in m.text and errs.append("console: " + m.text))
    pg.goto("file://" + __import__("os").path.abspath(a.html))
    pg.wait_for_timeout(500)
    tabs = pg.eval_on_selector_all("[data-tab]", "e=>e.map(x=>x.dataset.tab)")
    # load sample (setup tab first when present)
    for t in tabs[:1]:
        pg.click(f'[data-tab="{t}"]')
    if pg.query_selector("#" + a.sample_btn):
        pg.click("#" + a.sample_btn); pg.wait_for_timeout(300)
        for sel in ("#cf-ok", ".modal .danger", "dialog button.danger", "#dlg-ok"):
            if pg.query_selector(sel):
                try: pg.click(sel, timeout=1000)
                except Exception: pass
        pg.wait_for_timeout(500)
    stages = pg.eval_on_selector_all("[data-stage]", "e=>e.map(x=>x.dataset.stage)")
    if stages:  # stage navigation (Information Gathering): each stage shows its own tab row
        tabs = []
        for sg in stages:
            pg.click(f'[data-stage="{sg}"]'); pg.wait_for_timeout(200)
            for t in pg.eval_on_selector_all("#tabs [data-tab]", "e=>e.map(x=>x.dataset.tab)"):
                tabs.append(t)
                try:
                    pg.click(f'#tabs [data-tab="{t}"]', timeout=3000); pg.wait_for_timeout(250)
                except Exception as e:
                    errs.append(f"tab {t}: {str(e)[:80]}")
    else:
        for t in tabs:
            try:
                pg.click(f'[data-tab="{t}"]', timeout=3000); pg.wait_for_timeout(250)
            except Exception as e:
                errs.append(f"tab {t}: {str(e)[:80]}")
    print("tabs:", tabs)
    if pg.query_selector("#" + a.xlsx_btn):
        try:
            with pg.expect_download(timeout=15000) as d:
                pg.click("#" + a.xlsx_btn)
            path = a.save_xlsx or "/tmp/out.xlsx"; d.value.save_as(path); print("xlsx saved", path)
        except Exception as e:
            errs.append("xlsx export: " + str(e)[:120])
    b.close()
print("ERRORS:", len(errs))
for e in errs[:15]: print(" -", e)
sys.exit(1 if errs else 0)
