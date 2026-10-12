from extract_geometry import OUT, extract
from pathlib import Path
import json
inventory=json.loads((OUT/'VERSION_INVENTORY.json').read_text(encoding='utf-8'))
results=[];hashes={}
for row in inventory:
    if row.get('AR') not in [1.,3.]:continue
    r=extract(Path(row['source']),row['case'],'HISTORICAL_LB3_RP_R01')
    key=(r['case'],r['sha256'])
    if key in hashes:hashes[key]['duplicate_source_paths'].append(r['source']);continue
    r['duplicate_source_paths']=[];hashes[key]=r;results.append(r)
(OUT/'AR1_AR3_VARIANTS.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
print([(r['case'],r['AR'],r['initial_global_halfwaves'],r['half_wave_length_mm'],len(r['duplicate_source_paths'])) for r in results])
