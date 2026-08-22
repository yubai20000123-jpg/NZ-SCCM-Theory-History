#!/usr/bin/env python3
import json, pathlib, sys

root = pathlib.Path(__file__).resolve().parents[1]
m = json.loads((root / 'MANIFEST.json').read_text(encoding='utf-8'))

allowed = {
    'README.md',
    'RECOVERY_SCOPE_LOCK.md',
    'ARCHITECTURE_POSITIONING_LOCK.md',
    'RESEARCH_OVERLAP_AUDIT_CRITERIA.md',
    'KNOWN_GAPS_AND_INTENTIONAL_OMISSIONS.md',
    'MANIFEST.json',
    '.github',
    'audit_programs',
    'audit',
    'archive',
    'recovered',
    'AUDIT_REPORT.md',
}
err = []

for p in root.iterdir():
    if p.name == '.git':
        continue
    if p.name not in allowed:
        err.append('unauthorized top-level ' + p.name)

auth = {x['destination'] for x in m['payload']}
actual = {
    str(p.relative_to(root)).replace('\\', '/')
    for p in (root / 'recovered').rglob('*')
    if p.is_file()
}

for p in sorted(actual - auth):
    err.append('unmanifested payload ' + p)
for p in sorted(auth - actual):
    err.append('manifest payload absent ' + p)

# One physical historical file per canonical payload path.
if len(auth) != len(m['payload']):
    err.append('duplicate canonical payload destinations in manifest')

# Wrong-detour tokens are forbidden only inside historical payload. Governance
# files may name them explicitly in order to define exclusion boundaries.
for p in actual:
    text = (root / p).read_text(encoding='utf-8', errors='ignore')
    for token in m['excluded_wrong_detour_tokens']:
        if token in text:
            err.append(f'forbidden token {token} in historical payload {p}')

# Cross-stage references must not create duplicate physical historical files.
for x in m.get('cross_stage_references', []):
    if x['canonical_destination'] not in auth:
        err.append('cross-stage reference outside canonical payload: ' + x['canonical_destination'])

if err:
    print('PURITY_FAIL')
    print('\n'.join(err))
    sys.exit(1)

print(f'PURITY_PASS authorized_unique_payload={len(auth)}')
