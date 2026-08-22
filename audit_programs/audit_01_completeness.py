#!/usr/bin/env python3
import json, pathlib, sys, zipfile

root = pathlib.Path(__file__).resolve().parents[1]
m = json.loads((root / 'MANIFEST.json').read_text(encoding='utf-8'))

expected = {
    '01_AIRY_DISCOVERY_RESEARCH',
    '02_FIRST_TRIAL',
    '03_RC_AND_STEEL_SHELL_COMBINED',
    '04_CORRECTED_GEOMETRY_STEEL_SHELL_UHPC',
    '05_NORMAL_CONCRETE_CONSTITUTIVE_RESEARCH',
    '06_UHPC_CONSTITUTIVE_RESEARCH',
}
err = []

payload = m['payload']
cats = {x['category'] for x in payload}
if cats != expected:
    err.append(f'category set mismatch: {cats ^ expected}')

for c in expected:
    if not any(x['category'] == c for x in payload):
        err.append(f'empty category {c}')

paths = [x['destination'] for x in payload]
if len(paths) != len(set(paths)):
    err.append('duplicate payload destination detected')

for x in payload:
    if not (root / x['destination']).is_file():
        err.append('missing ' + x['destination'])

payload_set = set(paths)
for x in m.get('cross_stage_references', []):
    p = x['canonical_destination']
    if p not in payload_set:
        err.append('cross-stage reference not canonical payload: ' + p)
    if not (root / p).is_file():
        err.append('cross-stage canonical file missing: ' + p)

need = ['1608', '1646', '1824', '0745', '1151', '1240', '1255', '1315', '1320']
joined = '\n'.join(paths)
for t in need:
    if t not in joined:
        err.append('milestone token missing ' + t)

governance = [
    'README.md',
    'RECOVERY_SCOPE_LOCK.md',
    'ARCHITECTURE_POSITIONING_LOCK.md',
    'RESEARCH_OVERLAP_AUDIT_CRITERIA.md',
    'KNOWN_GAPS_AND_INTENTIONAL_OMISSIONS.md',
    'audit/HISTORICAL_CONTINUITY_AUDIT_20260823.md',
]
for g in governance:
    if not (root / g).is_file():
        err.append('governance file missing ' + g)

zip_path = root / 'archive/NZ_SCCM_MA_ORIGIN_RECOVERY_20260823.zip'
if '--post-zip' in sys.argv:
    if not zip_path.is_file():
        err.append('zip missing')
    else:
        with zipfile.ZipFile(zip_path) as z:
            names = set(z.namelist())
        for p in paths:
            if p not in names:
                err.append('zip payload missing ' + p)
        for g in governance:
            if g not in names:
                err.append('zip governance missing ' + g)

if err:
    print('COMPLETENESS_FAIL')
    print('\n'.join(err))
    sys.exit(1)

print(f'COMPLETENESS_PASS unique_payload={len(payload)} categories=6 cross_refs={len(m.get("cross_stage_references", []))}')
