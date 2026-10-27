from meta import DOCS, DOC
from build import pkg_of, load_content
from enrich import ENRICH, WAVES, FLOWS, ORDER
from enrich_activities import ACTIVITIES
W=list(WAVES); P={d['id']:pkg_of(d) for d in DOCS}; E=ENRICH
def wi(x): return W.index(E[x]['wave'])
print("== R1 Track A child earlier than parent (structural)")
for d in DOCS:
    e=E[d['id']]
    if e['track']=='A':
        for p in d['parents']:
            if wi(p)>wi(d['id']): print(' ',d['id'],e['wave'],'parent',p,E[p]['wave'])
print("== R2 Essential docs in W4/W5 (claim: first year)")
for d in DOCS:
    if P[d['id']]=='Essential' and E[d['id']]['wave'] in ('W4','W5'): print(' ',d['id'],E[d['id']]['wave'])
print("== R3 Extended docs in W0-W2")
for d in DOCS:
    if P[d['id']]=='Extended' and wi(d['id'])<=2: print(' ',d['id'],E[d['id']]['wave'],d['level'])
print("== R4 Required docs in Extended")
for d in DOCS:
    if d['level']=='Required' and P[d['id']]=='Extended': print(' ',d['id'],d['trigger'])
print("== R5 IT-ready docs whose activity needs SPEC")
for d in DOCS:
    e=E[d['id']]
    for a in e['acts']:
        if e['cap']=='IT' and ACTIVITIES[a]['cap']=='SPEC': print(' ',d['id'],a)
print("== R6 Flow step depends on a later step")
for f in FLOWS:
    ids=[s[0] for s in f[5]]
    for i,x in enumerate(ids):
        for y in ids[i+1:]:
            if y in E[x]['deps']: print(' ',f[0],x,'deps on later',y)
print("== R7 owner == approver")
for d in DOCS:
    if d['owner']==d['approver']: print(' ',d['id'],d['owner'])
print("== R8 Essential with Optional level / Optional not Extended")
for d in DOCS:
    if d['level']=='Optional' and P[d['id']]!='Extended': print(' ',d['id'],P[d['id']])
print("== R9 docs whose Package Essential but seq > first year waves",)
print("== R10 Track B docs not Essential")
for d in DOCS:
    if E[d['id']]['track']=='B' and P[d['id']]!='Essential': print(' ',d['id'],P[d['id']],d['level'])
print("== R11 Required(All/PDPA trigger) not Essential")
for d in DOCS:
    if d['level']=='Required' and set(d['trigger'])&{'All','PDPA'} and P[d['id']]!='Essential': print(' ',d['id'],d['trigger'],P[d['id']])
print("== R12 review cycles", sorted({d['review'] for d in DOCS}))
print("== R13 counts flows",len(FLOWS),"acts",len(ACTIVITIES))
