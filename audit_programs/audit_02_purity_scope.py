#!/usr/bin/env python3
import json, pathlib, sys
root=pathlib.Path(__file__).resolve().parents[1]
m=json.loads((root/'MANIFEST.json').read_text(encoding='utf-8'))
allowed={'README.md','RECOVERY_SCOPE_LOCK.md','MANIFEST.json','.github','audit_programs','audit','archive','recovered','AUDIT_REPORT.md'}
err=[]
for p in root.iterdir():
    if p.name=='.git': continue
    if p.name not in allowed: err.append('unauthorized top-level '+p.name)
auth={x['destination'] for x in m['payload']}
actual={str(p.relative_to(root)).replace('\\','/') for p in (root/'recovered').rglob('*') if p.is_file()}
for p in sorted(actual-auth): err.append('unmanifested payload '+p)
for p in sorted(auth-actual): err.append('manifest payload absent '+p)
for p in actual:
    text=(root/p).read_text(encoding='utf-8',errors='ignore')
    for token in m['excluded_wrong_detour_tokens']:
        if token in text: err.append(f'forbidden token {token} in {p}')
if err:
    print('PURITY_FAIL'); print('\n'.join(err)); sys.exit(1)
print(f'PURITY_PASS authorized_payload={len(auth)}')