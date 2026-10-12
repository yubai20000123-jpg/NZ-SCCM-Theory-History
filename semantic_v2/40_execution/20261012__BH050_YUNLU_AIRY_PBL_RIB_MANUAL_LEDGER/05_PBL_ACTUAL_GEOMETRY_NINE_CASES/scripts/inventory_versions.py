from extract_geometry import ROOT, OUT, parse, extract, CASES
import re,json
import numpy as np
rows=[];variants=[]
for path in ROOT.rglob('*.inp'):
    matches=re.findall(r'BH\d{3}',str(path))
    if not matches or not any(c in CASES for c in matches):continue
    if '.git' in path.parts:continue
    case=next((c for c in re.findall(r'BH\d{3}',path.name) if c in CASES),None)
    if not case:continue
    try:
        parts,instances,bs=parse(path)
        ckey=next(n for n in instances if n.upper()=='C-C-1');ci=instances[ckey]
        c=np.array(list(parts[ci['part']]['nodes'].values()))
        gskey=next(n for n in instances if n.upper()=='GS_LOAD-1');gs=np.array(list(parts[instances[gskey]['part']]['nodes'].values()))
        b=float(np.ptp(gs[:,0]));l=float(np.ptp(c[:,2]));ar=l/b
        row=dict(case=case,source=str(path),B_mm=b,L_mm=l,AR=ar,status='GEOMETRY_INVENTORIED',model_role='FORMAL_DIRECT' if path.parent.name=='UCFT_GS_DIRECT_R01_11MODELS' and path.name==f'JOB_{case}_GS_DIRECT_R01.inp' else 'HISTORICAL_OR_DIAGNOSTIC_NOT_MIXED')
        if abs(ar-1)<1e-6 or abs(ar-3)<1e-6:
            try:variants.append(extract(path,case,'HISTORICAL_AR'+str(round(ar))));row['rib_status']='EXTRACTED_SEPARATELY'
            except Exception as e:row['rib_status']='NOT_FOUND: '+str(e)
    except Exception as e:row=dict(case=case,source=str(path),status='NOT_FOUND: '+str(e))
    rows.append(row)
(OUT/'VERSION_INVENTORY.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'AR1_AR3_VARIANTS.json').write_text(json.dumps(variants,ensure_ascii=False,indent=2),encoding='utf-8')
print('INP inventory',len(rows),'AR1/3 extracted',len(variants))
print(json.dumps([r for r in rows if r.get('AR') in (1.,3.)],ensure_ascii=False,indent=2))
