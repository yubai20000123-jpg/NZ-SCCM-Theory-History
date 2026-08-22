#!/usr/bin/env python3
import hashlib,json,pathlib,sys
root=pathlib.Path(__file__).resolve().parents[1]
m=json.loads((root/'MANIFEST.json').read_text(encoding='utf-8'))
report=[]; err=[]
for x in m['payload']:
    p=root/x['destination']; data=p.read_bytes()
    gitsha=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    sha256=hashlib.sha256(data).hexdigest()
    report.append({'path':x['destination'],'expected_git_blob':x['blob_sha'],'actual_git_blob':gitsha,'sha256':sha256})
    if gitsha!=x['blob_sha']: err.append(x['destination'])
(root/'audit').mkdir(exist_ok=True)
(root/'audit/PROVENANCE_SHA256.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
if err:
    print('PROVENANCE_FAIL'); print('\n'.join(err)); sys.exit(1)
print(f'PROVENANCE_PASS files={len(report)}')