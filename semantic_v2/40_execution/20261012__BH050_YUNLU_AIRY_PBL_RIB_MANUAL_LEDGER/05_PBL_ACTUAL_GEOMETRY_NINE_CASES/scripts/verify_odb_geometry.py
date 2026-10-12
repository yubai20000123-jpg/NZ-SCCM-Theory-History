# Abaqus Python 2.7. Only stress-free mesh geometry; no fields, frames, stress or reaction.
from __future__ import print_function
import os,json,math,time
from odbAccess import openOdb
ROOT=r'C:\03SCI\abaqus-UCFT test\UCFT_GS_DIRECT_R01_11MODELS'
OUT=r'C:\03SCI\abaqus-UCFT test\outputs\PBL_ACTUAL_GEOMETRY_20261012'
results=[]
for case in ['BH005','BH010','BH020','BH032','BH050','BH060','BH070','BH085','BH100']:
    inp=os.path.join(ROOT,'JOB_'+case+'_GS_DIRECT_R01.inp'); nodes={};active=False;node_mode=False
    for s in open(inp,'rb'):
        s=s.strip();low=s.lower()
        if low.startswith('*part,'):active='name=c-s-shell' in low.replace(' ','');node_mode=False
        elif low.startswith('*end part'):active=False;node_mode=False
        elif active and low.startswith('*node'):node_mode=True
        elif low.startswith('*') and not low.startswith('**'):node_mode=False
        elif active and node_mode and s and not s.startswith('*'):
            v=s.split(',');nodes[int(v[0])]=map(float,v[1:4])
    path=os.path.join(ROOT,'JOB_'+case+'_GS_DIRECT_R01.odb');before=os.stat(path);odb=openOdb(path,readOnly=True)
    ins=odb.rootAssembly.instances['C-S-SHELL-1'];diffs=[]
    for n in ins.nodes:diffs.append(max(abs(float(a)-b) for a,b in zip(n.coordinates,nodes[n.label])))
    row={'case':case,'odb':path,'inp':inp,'instance':'C-S-SHELL-1','INP_nodes':len(nodes),'ODB_nodes':len(ins.nodes),'max_coordinate_difference_mm':max(diffs),'PBL_elements':len(ins.elementSets['UCFT_PBL_WEB_FACES'].elements),'sections':list(odb.sections.keys()),'readOnly':True,'field_or_history_read':False,'bytes':before.st_size,'mtime':before.st_mtime}
    row['status']='MATCH' if len(nodes)==len(ins.nodes) and max(diffs)<0.001 else 'MISMATCH'
    odb.close();after=os.stat(path);assert before.st_size==after.st_size and before.st_mtime==after.st_mtime
    results.append(row);print(case,row['status'],max(diffs))
with open(os.path.join(OUT,'ODB_GEOMETRY_VERIFICATION.json'),'w') as h:json.dump(results,h,indent=2)
