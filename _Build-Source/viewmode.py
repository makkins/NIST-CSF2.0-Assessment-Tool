# -*- coding: utf-8 -*-
"""View-mode patch (Presentation view / Editor view) applied after the template is built.
Source: extracted on 17 October 2026 from the delivered HTML files, where it was applied by an unsaved script (plan W0-1).
Usage: from viewmode import apply_viewmode; html = apply_viewmode(html, ["land", "tier", "str", "gap", "reg"])
Presentation view shows only the tabs listed in pres. The setting is stored per browser under csf-view-mode."""
import json

OLD_CSS = '<style>[hidden]{display:none!important}</style>'
NEW_CSS = '<style>[hidden]{display:none!important}\n/* View mode: Presentation / Editor */\n#b-vm{white-space:nowrap}\nbody.vm-pres #b-open,body.vm-pres #b-save,body.vm-pres #b-xlsx,body.vm-pres #savebar{display:none!important}\n#audseg{display:none!important}\n</style>'
BUTTON = '      <button class="btn" id="b-vm" type="button" aria-pressed="false">Presentation view</button>\n'
SCRIPT = '<script>\n/* View mode: Presentation / Editor. Presentation shows only the tabs listed in CFG.pres. */\n(function(){\nvar CFG=__CFG__, KEY="csf-view-mode";\nvar T={EN:{pres:"Presentation view",edit:"Editor view",tp:"Switch to presentation view (presentation tabs only)",te:"Switch to editor view (all tabs and tools)"},\nTH:{pres:"มุมมองนำเสนอ",edit:"มุมมองแก้ไข",tp:"สลับเป็นมุมมองนำเสนอ (แสดงเฉพาะแท็บนำเสนอ)",te:"สลับเป็นมุมมองแก้ไข (แสดงทุกแท็บและเครื่องมือ)"}};\nvar ws=CFG.kind==="ws", stored=null, mode="edit";\ntry{stored=localStorage.getItem(KEY)}catch(e){}\nif(stored==="pres")mode="pres";\nfunction isTH(){try{return ws?S.lang==="th":lang==="TH"}catch(e){return false}}\nfunction cur(){return ws?(S.aud==="exec"?"pres":"edit"):mode}\nfunction paint(){\n  var b=document.getElementById("b-vm");if(!b)return;\n  var m=cur(),L=T[isTH()?"TH":"EN"];\n  b.textContent=m==="pres"?L.edit:L.pres;\n  b.title=m==="pres"?L.te:L.tp;\n  b.setAttribute("aria-pressed",m==="pres"?"true":"false");\n  b.classList.toggle("pri",m==="pres");\n  document.body.classList.toggle("vm-pres",m==="pres");\n}\nif(ws){\n  if(stored==="pres"||stored==="edit")S.aud=stored==="pres"?"exec":"cons";\n  var r0=render;render=function(){r0.apply(this,arguments);paint();};\n}else{\n  var ok=function(v){return mode!=="pres"||CFG.pres.indexOf(v)>-1};\n  var ensure=function(){if(!ok(view))view=CFG.pres[0];};\n  var rs=renderStatic;\n  renderStatic=function(){ensure();rs.apply(this,arguments);\n    if(mode==="pres"){var tb=document.getElementById("tabs");\n      if(tb)tb.querySelectorAll("[data-tab]").forEach(function(b){if(CFG.pres.indexOf(b.dataset.tab)<0)b.remove();});}\n    paint();};\n  var rv=renderView;renderView=function(){ensure();return rv.apply(this,arguments);};\n  var sv=setView;setView=function(v){if(!ok(v))return;return sv.apply(this,arguments);};\n  if(typeof goDoc==="function"){var gd=goDoc;goDoc=function(){if(!ok("assess"))return;return gd.apply(this,arguments);};}\n  if(typeof goSub==="function"){var gs=goSub;goSub=function(){if(!ok("iv"))return;return gs.apply(this,arguments);};}\n}\ndocument.addEventListener("click",function(e){\n  var b=e.target.closest&&e.target.closest("#b-vm");if(!b)return;\n  var next=cur()==="pres"?"edit":"pres";\n  try{localStorage.setItem(KEY,next)}catch(x){}\n  if(ws){S.aud=next==="pres"?"exec":"cons";save();render();}\n  else{mode=next;renderAll();}\n  window.scrollTo(0,0);\n});\nif(ws)render();else renderAll();\n})();\n</script>'

def apply_viewmode(html, pres, anchor='id="b-xlsx"></button>\n'):
    """anchor: the header line after which the View button goes (the Document Map has no Excel button, so it uses the Help button)."""
    assert OLD_CSS in html, "skeleton style line not found"
    assert anchor in html, "header button anchor not found"
    assert "\n</body>" in html
    html = html.replace(OLD_CSS, NEW_CSS, 1)
    html = html.replace(anchor, anchor + BUTTON, 1)
    cfg = json.dumps({"kind": "std", "pres": pres})
    i = html.rindex("\n</body>")
    return html[:i] + "\n\n" + SCRIPT.replace("__CFG__", cfg) + "\n" + html[i:]
