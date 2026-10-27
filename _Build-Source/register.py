# -*- coding: utf-8 -*-
"""Loads the single Register source (00_Master/Gap-Analysis-Method/tools/register-ids.json, plan W1-2)."""
import json, pathlib
PATH = pathlib.Path(__file__).resolve().parent.parent / "00_Master" / "Gap-Analysis-Method" / "tools" / "register-ids.json"
def load():
    return json.load(open(PATH, encoding="utf-8"))
REG = load()
