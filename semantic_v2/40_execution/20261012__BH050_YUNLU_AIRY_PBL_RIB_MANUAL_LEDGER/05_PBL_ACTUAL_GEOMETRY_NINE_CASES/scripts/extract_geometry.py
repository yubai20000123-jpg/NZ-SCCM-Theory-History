"""Read-only INP rib topology extraction. No Abaqus analysis or model edits."""
from pathlib import Path
from collections import defaultdict, Counter
import json, hashlib, math
import numpy as np

ROOT=Path(r'C:\03SCI\abaqus-UCFT test')
OUT=Path(__file__).parent
CASES=['BH005','BH010','BH020','BH032','BH050','BH060','BH070','BH085','BH100']

def blocks(path):
    lines=path.read_text(encoding='utf-8-sig',errors='replace').splitlines()
    result=[]
    for i,s in enumerate(lines,1):
        s=s.strip()
        if not s or s.startswith('**'): continue
        if s.startswith('*'):
            p=[x.strip() for x in s.split(',')]
            attrs={x.split('=',1)[0].lower():x.split('=',1)[1] for x in p[1:] if '=' in x}
            result.append(dict(key=p[0].lower(),attrs=attrs,flags=[x.lower() for x in p[1:] if '=' not in x],line=i,header=s,data=[]))
        else: result[-1]['data'].append((i,s))
    return result

def parse(path):
    bs=blocks(path); parts={};part=None;instances={};inst=None
    for b in bs:
        k=b['key'];a=b['attrs']
        if k=='*part':
            part=a['name'];parts[part]=dict(nodes={},elements={},sets={},sections=[],node_lines={},element_lines={})
        elif k=='*end part':part=None
        elif part:
            p=parts[part]
            if k=='*node':
                for ln,s in b['data']:
                    v=[x.strip() for x in s.split(',')];n=int(v[0]);p['nodes'][n]=list(map(float,v[1:4]));p['node_lines'][n]=ln
            elif k=='*element':
                for ln,s in b['data']:
                    v=[int(x) for x in s.split(',') if x.strip()];p['elements'][v[0]]=v[1:];p['element_lines'][v[0]]=ln
            elif k=='*elset':
                ids=[]
                for ln,s in b['data']:
                    v=[int(x) for x in s.split(',') if x.strip()]
                    ids.extend(range(v[0],v[1]+1,v[2]) if 'generate' in b['flags'] else v)
                p['sets'].setdefault(a['elset'].upper(),set()).update(ids)
            elif k=='*shell section': p['sections'].append(dict(elset=a['elset'].upper(),thickness=float(b['data'][0][1].split(',')[0]),offset=a.get('offset','0'),line=b['line'],material=a['material']))
        elif k=='*instance':
            inst=a['name'];instances[inst]=dict(part=a['part'],line=b['line'],transform=[list(map(float,s.split(','))) for _,s in b['data']])
        elif k=='*end instance':inst=None
    return parts,instances,bs

def components(elements):
    node_to_elements=defaultdict(list)
    for e,conn in elements.items():
        for n in conn:node_to_elements[n].append(e)
    seen=set();comps=[]
    for seed in sorted(elements):
        if seed in seen:continue
        stack=[seed];seen.add(seed);c=[]
        while stack:
            e=stack.pop();c.append(e)
            for n in elements[e]:
                for other in node_to_elements[n]:
                    if other not in seen: seen.add(other);stack.append(other)
        comps.append(sorted(c))
    return comps

def extract(path,case,version):
    before=path.stat();parts,instances,bs=parse(path)
    si=next(n for n,i in instances.items() if any('PBL' in s for s in parts[i['part']]['sets']))
    ins=instances[si];p=parts[ins['part']]
    assert not ins['transform'], ('Need explicit assembly transform',path,ins)
    web=p['sets']['UCFT_PBL_WEB_FACES'];outer=p['sets']['UCFT_OUTER_SHELL_FACES']
    assert not web.intersection(outer)
    elems={e:p['elements'][e] for e in web}
    outer_nodes=set(n for e in outer for n in p['elements'][e])
    embedded=p['sets'].get('UCFT_PBL_EMBEDDED_INTERIOR_ELEMENTS',set())
    section=next(s for s in p['sections'] if s['elset']=='UCFT_PBL_WEB_FACES')
    endsets={}
    for b in bs:
        if b['key']=='*nset' and b['attrs'].get('instance')==si:
            vals=[]
            for _,s in b['data']:
                v=[int(x) for x in s.split(',') if x.strip()]
                vals.extend(range(v[0],v[1]+1,v[2]) if 'generate' in b['flags'] else v)
            endsets[b['attrs']['nset'].upper()]=set(vals)
    cn=parts[instances['C-C-1']['part']]['nodes'];coords=np.array(list(cn.values()))
    core_xmin,core_xmax=coords[:,0].min(),coords[:,0].max();zmin,zmax=coords[:,2].min(),coords[:,2].max()
    gs=np.array(list(parts[instances['GS_LOAD-1']['part']]['nodes'].values()))
    xmin,xmax=gs[:,0].min(),gs[:,0].max()
    core_mid=defaultdict(list)
    for xx,yy,zz in coords:
        if abs(xx-(core_xmin+core_xmax)/2)<1e-5:core_mid[zz].append(yy)
    mode_tests=[]
    for nmode in range(1,9):
        err=max(abs((min(v)+max(v))/2-(xmax-xmin)/400*math.sin(nmode*math.pi*(zz-zmin)/(zmax-zmin))) for zz,v in core_mid.items())
        mode_tests.append((err,nmode))
    bow_error,bow_mode=min(mode_tests)
    recognized_mode=bow_mode if bow_error<0.001 else None
    zeros=sorted(float(zz) for zz,v in core_mid.items() if abs((min(v)+max(v))/2)<1e-5)
    zero_spans=np.diff(zeros)
    observed_halfwave_length=float(zero_spans[0]) if len(zero_spans)>0 and np.max(np.abs(zero_spans-zero_spans[0]))<0.001 else 'NOT_FOUND'
    ribs=[]
    for index,c in enumerate(components(elems),1):
        ns=sorted(set(n for e in c for n in elems[e]));xyz=np.array([p['nodes'][n] for n in ns]);spans=np.ptp(xyz,axis=0)
        normal_axis=int(np.argmin(spans));direction='LONGITUDINAL' if normal_axis==0 else 'TRANSVERSE' if normal_axis==2 else 'UNCLASSIFIED'
        # Identify attachment by shared node labels, never by names alone.
        roots=sorted(set(ns).intersection(outer_nodes));rootxyz=np.array([p['nodes'][n] for n in roots])
        ymean=float(rootxyz[:,1].mean()) if roots else None
        # Stress-free endpoints have zero global sine imperfection; use endpoint root elevation as side identity.
        endroots=[n for n in roots if abs(p['nodes'][n][2]-zmin)<1e-4 or abs(p['nodes'][n][2]-zmax)<1e-4]
        endy=np.mean([p['nodes'][n][1] for n in endroots]) if endroots else ymean
        side='TOP' if endy is not None and endy>0 else 'BOTTOM' if endy is not None and endy<0 else 'NOT_FOUND'
        ec=Counter(tuple(sorted((a,b))) for e in c for a,b in zip(elems[e],elems[e][1:]+elems[e][:1]))
        boundary=[edge for edge,count in ec.items() if count==1]
        boundary_comp=components({i:list(ed) for i,ed in enumerate(boundary)})
        holes=max(0,len(boundary_comp)-1)
        xref=float((xyz[:,0].min()+xyz[:,0].max())/2)
        root_by_z=defaultdict(list);all_by_z=defaultdict(list)
        for n in roots:root_by_z[p['nodes'][n][2]].append(p['nodes'][n][1])
        for n in ns:all_by_z[p['nodes'][n][2]].append(p['nodes'][n][1])
        heights=[max(v)-min(v) for v in all_by_z.values()]
        root0=[p['nodes'][n] for n in endroots if abs(p['nodes'][n][2]-zmin)<1e-4]
        rootL=[p['nodes'][n] for n in endroots if abs(p['nodes'][n][2]-zmax)<1e-4]
        envmin=xyz.min(axis=0).copy();envmax=xyz.max(axis=0).copy();envmin[normal_axis]-=section['thickness']/2;envmax[normal_axis]+=section['thickness']/2
        initial_profile=[]
        for zz,ys in sorted(all_by_z.items()):
            rr=root_by_z.get(zz,[])
            initial_profile.append(dict(original_Z_mm=zz,midplane_Y_min_mm=min(ys),midplane_Y_max_mm=max(ys),root_Y_mm=float(np.mean(rr)) if rr else None))
        endpointYs=[p['nodes'][n][1] for n in ns if abs(p['nodes'][n][2]-zmin)<1e-4]
        flatmin,flatmax=min(endpointYs),max(endpointYs)
        bow_errors=[abs(q['midplane_Y_min_mm']-flatmin-(xmax-xmin)/400*math.sin(math.pi*(xref-xmin)/(xmax-xmin))*math.sin(bow_mode*math.pi*(q['original_Z_mm']-zmin)/(zmax-zmin))) for q in initial_profile]
        r=dict(case=case,version=version,AR=float((zmax-zmin)/(xmax-xmin)),rib_id=f'{side}_{index:02d}',part=ins['part'],instance=si,rib_type=direction,side=side,reference_x_mm=xref-xmin,core_origin_x_mm=xref-core_xmin,original_X_mm=xref,reference_y_start_mm=float(xyz[:,2].min()-zmin),reference_y_end_mm=float(xyz[:,2].max()-zmin),axial_length_mm=float(spans[2]),thickness_mm=section['thickness'],height_min_mm=float(min(heights)),height_max_mm=float(max(heights)),flat_reference_z_min_mm=flatmin,flat_reference_z_max_mm=flatmax,reference_centerline_z_mm=(flatmin+flatmax)/2,initial_bow_formula_max_error_mm=max(bow_errors),initial_profile=initial_profile,normal_axis=normal_axis,reference_flat_plane_span_mm=float(spans[normal_axis]),shell_mid_bbox_original=[xyz.min(axis=0).tolist(),xyz.max(axis=0).tolist()],finite_thickness_bbox_original=[envmin.tolist(),envmax.tolist()],root_start_original=root0[0] if root0 else 'NOT_FOUND',root_end_original=rootL[0] if rootL else 'NOT_FOUND',element_count=len(c),node_count=len(ns),shared_root_node_count=len(roots),embedded_element_count=len(set(c)&embedded),hole_boundary_loop_count=holes,element_ids=c,node_ids=ns,node_line_range=[min(p['node_lines'][n] for n in ns),max(p['node_lines'][n] for n in ns)],element_line_range=[min(p['element_lines'][e] for e in c),max(p['element_lines'][e] for e in c)],section_line=section['line'],assembly_line=ins['line'],connection='Shared shell-root node labels; partial embedded interior PBL in UHPC; end-node Tie to GS' if roots else 'NOT_FOUND',source=str(path))
        ribs.append(r)
        for loc,zz in [('LOAD',zmin),('FIX',zmax)]:
            ends=set(n for n in ns if abs(p['nodes'][n][2]-zz)<1e-4)
            setname=next((s for s in ['STEEL_END_ALL_NODES_TIED_'+loc,'STEEL_'+loc+'_END_ALL_NODES_TIED'] if s in endsets),None)
            target=endsets.get(setname,set())
            r['end_'+loc.lower()+'_tie_set']=setname or 'NOT_FOUND'
            r['end_'+loc.lower()+'_node_count']=len(ends)
            r['end_'+loc.lower()+'_tied_node_count']=len(ends&target)
        r['direct_named_end_set_coverage']='COMPLETE' if r['end_load_node_count']==r['end_load_tied_node_count'] and r['end_fix_node_count']==r['end_fix_tied_node_count'] else 'INCOMPLETE_REQUIRES_SURFACE_TIE_REVIEW'
    ties=[dict(line=b['line'],header=b['header'],data=b['data']) for b in bs if b['key'] in ['*tie','*embedded element','*boundary','*contact inclusions','*friction','*surface behavior','*contact property assignment','*coupling']]
    geometry_headers=[dict(line=b['line'],header=b['header'],data=b['data'] if b['key']=='*shell section' else []) for b in bs if b['key'] in ['*shell section','*elset','*element'] and ('PBL' in b['header'].upper() or 'OUTER_SHELL' in b['header'].upper() or (b['key']=='*element' and 'S4R' in b['header'].upper()))]
    sha=hashlib.sha256(path.read_bytes()).hexdigest()
    prior=ROOT/'outputs'/'DIRECT_END_CREST_FORCE_AUDIT_20261010'/f'{case}_EXTRACTION_PROVENANCE.json'
    priorhash=None
    if version=='FORMAL_GS_DIRECT_R02_CONTACT_RESTORED' and prior.exists():
        pr=json.loads(prior.read_text());priorhash=pr['source_before']['inp']['sha256'];assert sha==priorhash,(case,'Provenance source mismatch')
    assert path.stat().st_mtime_ns==before.st_mtime_ns and path.stat().st_size==before.st_size
    return dict(case=case,version=version,source=str(path),sha256=sha,prior_audit_sha256=priorhash,mtime=before.st_mtime,bytes=before.st_size,width_mm=float(xmax-xmin),core_width_mm=float(core_xmax-core_xmin),core_xmin_mm=float(core_xmin),length_mm=float(zmax-zmin),xmin_mm=float(xmin),Z_start_mm=float(zmin),AR=float((zmax-zmin)/(xmax-xmin)),initial_global_halfwaves=recognized_mode,initial_global_bow_max_error_mm=bow_error,centerline_initial_bow_zero_Z_mm=zeros,half_wave_length_mm=observed_halfwave_length,initial_geometry_halfwave_count=len(zero_spans),ribs=ribs,PBL_element_count=len(web),PBL_component_count=len(ribs),classified_element_count=sum(r['element_count'] for r in ribs),instances=instances,connections=ties,geometry_keyword_evidence=geometry_headers)

if __name__=='__main__':
    results=[]
    for case in CASES:
        r=extract(ROOT/'UCFT_GS_DIRECT_R01_11MODELS'/f'JOB_{case}_GS_DIRECT_R01.inp',case,'FORMAL_GS_DIRECT_R02_CONTACT_RESTORED');results.append(r)
        print(case,'B,L',r['width_mm'],r['length_mm'],'ribs',[(x['side'],x['original_X_mm'],x['height_min_mm'],x['height_max_mm'],x['hole_boundary_loop_count']) for x in r['ribs']])
    (OUT/'geometry_raw.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
