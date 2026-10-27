# -*- coding: utf-8 -*-
"""Generates the project doc claude/csf-document-framework-register.md from the Register (plan W1-2).
Usage: python gen_register_md.py [output path]"""
import pathlib, sys
from enrich import ENRICH, ORDER, CAPS
from build import pkg_of
from meta import DOC
def table():
    out = ["| # | ID | Title | Category | Tier | Level | Trigger | Package | Wave | Track | Capability | ISO theme |", "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for i, did in enumerate(ORDER, 1):
        d, e = DOC[did], ENRICH[did]
        out.append(f"| {i} | {did} | {d['en']} | {d['cat']} | {d['tier']} | {d['level']} | {', '.join(d['trigger'])} | {pkg_of(d)} | {e['wave']} | {e['track']} | {CAPS[e['cap']][0]} | {e['theme']} |")
    return "\n".join(out) + "\n"
def render():
    return open(pathlib.Path(__file__).with_name("register_md_header.md"), encoding="utf-8").read() + table()
if __name__ == "__main__":
    p = sys.argv[1] if len(sys.argv) > 1 else "register.md"
    open(p, "w", encoding="utf-8").write(render()); print(p)
