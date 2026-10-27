# -*- coding: utf-8 -*-
"""Injects site_data.json into the HTML templates. Writes an artifact body (no skeleton) and a standalone file for the folder."""
import json, sys
from viewmode import apply_viewmode

SKEL = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<style>[hidden]{display:none!important}</style>\n</head>\n<body>\n{body}\n</body>\n</html>\n')

def load():
    return json.load(open("site_data.json", encoding="utf-8"))

def inject(tpl, data):
    s = open(tpl, encoding="utf-8").read()
    js = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    assert "__DATA__" in s
    return s.replace("__DATA__", js)

def write(body, art_path, standalone_path, pres=None, anchor=None):
    open(art_path, "w", encoding="utf-8").write(body)
    html = SKEL.replace("{body}", body)
    if pres:
        html = apply_viewmode(html, pres, anchor) if anchor else apply_viewmode(html, pres)
    open(standalone_path, "w", encoding="utf-8").write(html)

def map_page():
    data = load()
    for d in data["docs"]:
        d["chk"] = [c["t"] for c in d.get("content", []) if c["id"] not in ("c-purpose", "c-scope")]
        d.pop("ctrl", None); d.pop("content", None)
    body = inject("map_template.html", data)
    write(body, "artifact_map.html", "out/NIST-CSF2-Document-Framework/00_Master/Document-Hierarchy.html",
          ["map", "tree", "order", "flow", "owner", "split"], 'aria-haspopup="dialog">Help</button>\n')
    print("map", len(body))

def audit_page():
    data = load()
    body = inject("audit_template.html", data)
    write(body, "artifact_audit.html", "out/NIST-CSF2-Document-Framework/00_Master/Document-Audit-Tracker.html", ["dash", "gaps"])
    print("audit", len(body))

if __name__ == "__main__":
    which = sys.argv[1:] or ["map", "audit"]
    if "map" in which: map_page()
    if "audit" in which: audit_page()
