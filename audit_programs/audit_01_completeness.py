#!/usr/bin/env python3
import json, pathlib, sys, zipfile
root=pathlib.Path(__file__).resolve().parents[1]
m=json.loads((root/'MANIFEST.json').read_text(encoding='utf-8'))
expected={f'{i:02d}_'+n for i,n in [(1,'AIRY_DISCOVERY_RESEARCH'),(2,'FIRST_TRIAL'),(3,'RC_AND_STEEL_SHELL_COMBINED'),(4,'CORRECTED_GEOMETRY_STEEL_SHELL_UHPC'),(5,'NORMAL_CONCRETE_CONSTITUTIVE_RESEARCH'),(6,'UHPC_CONSTITUTIVE_RESEARCH')]}
cats={x['category'] for x in m['payload']}
err=[]
if cats!=expected: err.append(f'category set mismatch: {cats ^ expected}')
for c in expected:
    if not any(x['category']==c for x in m['payload']): err.append(f'empty category {c}')
for x in m['payload']:
    if not (root/x['destination']).is_file(): err.append('missing '+x['destination'])
need=['1608','1646','1824','0745','1240','1255','1315','1320']
joined='\n'.join(x['destination'] for x in m['payload'])
for t in need:
    if t not in joined: err.append('milestone token missing '+t)
zip_path=root/'archive/NZ_SCCM_MA_ORIGIN_RECOVERY_20260823.zip'
if '--post-zip' in sys.argv:
    if not zip_path.is_file(): err.append('zip missing')
    else:
        with zipfile.ZipFile(zip_path) as z: names=set(z.namelist())
        for x in m['payload']:
            if x['destination'] not in names: err.append('zip payload missing '+x['destination'])
if err:
    print('COMPLETENESS_FAIL'); print('\n'.join(err)); sys.exit(1)
print(f'COMPLETENESS_PASS payload={len(m["payload"])} categories=6')