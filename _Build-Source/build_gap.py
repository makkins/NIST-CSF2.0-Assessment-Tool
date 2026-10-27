# -*- coding: utf-8 -*-
"""Builds the CSF Gap Analysis HTML (Phase 2).
Inputs: gap_template.html (UI and logic), interview_template.html (shared style), rubric.py (Tier Rubric),
sysprofile.py (profile fields), the method pack in ../00_Master/Gap-Analysis-Method (prompts, anchors, schemas),
document data from the Document Audit Tracker, and optional sample files in gap_sample/.
Usage: python build_gap.py [Document-Audit-Tracker.html] [output.html] [--mode compact]
One template (gap_template.html, plan W1-3). Build flag mode=compact is the only mode; the old Full template is archived as gap_template_full_legacy.html and is not built."""
import json, os, re, sys
from rubric import RUBRIC, RUBRIC_VERSION, COVERAGE
from sysprofile import PROFILE, VENDOR
from deptprofile import DEPT_FIELDS
from build_html import SKEL
from build_interview import load_data
from viewmode import apply_viewmode

METHOD = "../00_Master/Gap-Analysis-Method"
APP_VERSION = "1.4"
MODES = ("compact",)

def prompt_body(path):
    s = open(path, encoding="utf-8").read()
    i, j = s.index("## PROMPT START"), s.index("## PROMPT END")
    return s[i + len("## PROMPT START"):j].strip()

def followups(path):
    s = open(path, encoding="utf-8").read()
    blocks = re.findall(r"```\n(.*?)\n```", s[s.index("## PROMPT END"):], re.S)
    assert len(blocks) == 2, "analyst prompt must hold two follow-up messages"
    return blocks

def function_blocks(path):
    s = open(path, encoding="utf-8").read()
    out = {}
    for m in re.finditer(r"^## (GV|ID|PR|DE|RS|RC) [^\n]*\n(.*?)(?=^## |\Z)", s, re.S | re.M):
        out[m.group(1)] = m.group(2).strip()
    assert set(out) == {"GV", "ID", "PR", "DE", "RS", "RC"}, "need six Function blocks"
    return out

def anchors(path):
    s = open(path, encoding="utf-8").read()
    return s[s.index("## 1."):s.index("## 3.")].strip()

def main():
    args = sys.argv[1:]
    mode = "compact"
    if "--mode" in args:
        i = args.index("--mode"); mode = args[i + 1]; del args[i:i + 2]
    assert mode in MODES, f"mode {mode!r} is not supported; use one of {MODES}"
    tracker = args[0] if len(args) > 0 else "../00_Master/Document-Audit-Tracker.html"
    out = args[1] if len(args) > 1 else "../00_Master/Gap-Analysis-Compact.html"
    d = load_data(tracker)
    m = d["meta"]
    readme = open(os.path.join(METHOD, "README.md"), encoding="utf-8").read()
    method_version = re.search(r"Version ([0-9.]+)", readme).group(1)
    schemas = {}
    for f in sorted(os.listdir(os.path.join(METHOD, "schemas"))):
        j = json.load(open(os.path.join(METHOD, "schemas", f), encoding="utf-8"))
        schemas[j["$id"]] = j
    fu = followups(os.path.join(METHOD, "prompts/01-analyst-prompt.md"))
    lsp = os.path.join(METHOD, "prompts/05-landscape-prompt.md")
    ls_tail = open(lsp, encoding="utf-8").read().split("## PROMPT END")[1]
    ls_follow = re.findall(r"```\n(.*?)\n```", ls_tail, re.S)
    assert len(ls_follow) == 1, "landscape prompt must hold one follow-up message"
    data = dict(
        appVersion=APP_VERSION, buildMode=mode, methodVersion=method_version, rubricVersion=RUBRIC_VERSION,
        meta=dict(functions=m["functions"], categories=m["categories"], subcats=m["subcats"]),
        rubric=RUBRIC, coverage=COVERAGE,
        profile=[dict(id=f["id"], sec=f["sec"], n=f["n"], s=f["s"]) for f in PROFILE + VENDOR],
        docs={x["id"]: dict(en=x["en"], level=x["level"], tier=x["tier"], type=x["type"]) for x in d["docs"]},
        prompts=dict(analyst=prompt_body(os.path.join(METHOD, "prompts/01-analyst-prompt.md")),
                     follow1=fu[0], follow2=fu[1],
                     reviewer=prompt_body(os.path.join(METHOD, "prompts/03-reviewer-prompt.md")),
                     xreview=prompt_body(os.path.join(METHOD, "prompts/04-cross-function-reviewer-prompt.md")),
                     fnContext=function_blocks(os.path.join(METHOD, "prompts/02-function-context.md")),
                     anchors=anchors(os.path.join(METHOD, "calibration-anchors.md")),
                     landscape=prompt_body(lsp), lsFollow=ls_follow[0]),
        deptFields=[dict(id=f["id"], type=f["type"], n=f["n"], s=f["s"]) for f in DEPT_FIELDS],
        schemas=schemas,
        sample=json.load(open("gap_sample/sample.json", encoding="utf-8")) if os.path.exists("gap_sample/sample.json") else None)
    assert set(RUBRIC) == set(m["categories"])
    js = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    itpl = open("interview_template.html", encoding="utf-8").read()
    css = itpl[itpl.index("<style>"):itpl.index("</style>") + len("</style>")]
    tpl_path = "gap_template.html"
    tpl = open(tpl_path, encoding="utf-8").read()
    assert "__DATA__" in tpl and "__CSS__" in tpl
    named = re.search(r"`(csf-gap-analyst/\d+)`", data["prompts"]["analyst"]).group(1)
    assert named in tpl, f"method pack {method_version} asks the Analyst for {named}, but {tpl_path} does not read it. Update the template first (Gap Analysis HTML v1.2)"
    body = tpl.replace("__CSS__", css).replace("__DATA__", js)
    page = apply_viewmode(SKEL.replace("{body}", body), ["land", "tier", "str", "gap", "reg"])
    open(out, "w", encoding="utf-8").write(page)
    print("gap", len(body), "->", out)

if __name__ == "__main__":
    main()
