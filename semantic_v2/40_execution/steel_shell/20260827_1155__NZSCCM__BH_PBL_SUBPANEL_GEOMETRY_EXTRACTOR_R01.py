# Abaqus/CAE 2019 Python 2 compatible. Read-only geometry extraction.
from __future__ import print_function
import os, sys, json, csv, math
from collections import defaultdict, deque
from odbAccess import openOdb


def vsub(a,b): return (a[0]-b[0],a[1]-b[1],a[2]-b[2])
def cross(a,b): return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def norm(a): return math.sqrt(a[0]*a[0]+a[1]*a[1]+a[2]*a[2])
def unit(a):
    n=norm(a)
    if n <= 1e-15: return (0.0,0.0,0.0)
    return (a[0]/n,a[1]/n,a[2]/n)

def edge_key(a,b): return (a,b) if a < b else (b,a)


def main():
    if len(sys.argv) < 4:
        raise SystemExit('usage: abaqus python script.py ODB_PATH INSTANCE_NAME OUTDIR')
    odb_path=sys.argv[1]; inst_name=sys.argv[2]; outdir=sys.argv[3]
    if not os.path.isdir(outdir): os.makedirs(outdir)
    odb=openOdb(odb_path,readOnly=True)
    try:
        inst=odb.rootAssembly.instances[inst_name]
        nodes={n.label:tuple(float(x) for x in n.coordinates) for n in inst.nodes}
        elements={e.label:tuple(int(x) for x in e.connectivity) for e in inst.elements}

        elem_normal={}
        is_face={}
        for lab,conn in elements.items():
            if len(conn) < 3: continue
            p0,p1,p2=nodes[conn[0]],nodes[conn[1]],nodes[conn[2]]
            nn=unit(cross(vsub(p1,p0),vsub(p2,p0)))
            elem_normal[lab]=nn
            # face plate normal approximately global +/-Y. Web/PBL is mainly x-z normal.
            is_face[lab]=(abs(nn[1]) >= 0.90)

        edge_elems=defaultdict(list)
        elem_edges={}
        for lab,conn in elements.items():
            # shell polygon edges only; works for S3/S4/S4R etc.
            ee=[]
            for i in range(len(conn)):
                k=edge_key(conn[i],conn[(i+1)%len(conn)])
                ee.append(k); edge_elems[k].append(lab)
            elem_edges[lab]=ee

        # A face-face edge is traversable only if it is not simultaneously attached to a non-face shell.
        adj=defaultdict(set)
        boundary_edges=set()
        for ed,labs in edge_elems.items():
            fl=[e for e in labs if is_face.get(e,False)]
            nfl=[e for e in labs if not is_face.get(e,False)]
            if len(fl)==2 and not nfl:
                adj[fl[0]].add(fl[1]); adj[fl[1]].add(fl[0])
            if fl and (nfl or len(fl)==1):
                boundary_edges.add(ed)

        comps=[]; seen=set()
        for seed in sorted(e for e in elements if is_face.get(e,False)):
            if seed in seen: continue
            q=deque([seed]); seen.add(seed); c=[]
            while q:
                e=q.popleft(); c.append(e)
                for nb in adj[e]:
                    if nb not in seen: seen.add(nb); q.append(nb)
            comps.append(sorted(c))

        records=[]
        for cid,comp in enumerate(comps,1):
            nset=set(); bedges=[]
            for e in comp:
                nset.update(elements[e])
                for ed in elem_edges[e]:
                    labs=edge_elems[ed]
                    # boundary of this connected face component or attachment to non-face
                    if ed in boundary_edges or not all((x in comp) for x in labs if is_face.get(x,False)):
                        bedges.append(ed)
            xyz=[nodes[n] for n in nset]
            xs=[p[0] for p in xyz]; ys=[p[1] for p in xyz]; zs=[p[2] for p in xyz]
            ymean=sum(ys)/len(ys)
            side='TOP' if ymean >= 0 else 'BOTTOM'
            rec={
                'subpanel_id':cid,'side':side,'element_count':len(comp),'node_count':len(nset),
                'x_min':min(xs),'x_max':max(xs),'y_mean':ymean,'z_min':min(zs),'z_max':max(zs),
                'Lx_bbox':max(xs)-min(xs),'Lz_bbox':max(zs)-min(zs),
                'element_labels':comp,'node_labels':sorted(nset),
                'boundary_edges':[list(x) for x in sorted(set(bedges))]
            }
            records.append(rec)

        # This file deliberately extracts geometry only. It does NOT select local sign from FEM response.
        # A later mapper may use the stress-free initial geometry/imperfection definition to determine s_f.
        with open(os.path.join(outdir,'PBL_SUBPANEL_GEOMETRY.json'),'w') as f:
            json.dump({'odb':odb_path,'instance':inst_name,'subpanels':records},f,indent=2,sort_keys=True)
        fields=['subpanel_id','side','element_count','node_count','x_min','x_max','y_mean','z_min','z_max','Lx_bbox','Lz_bbox']
        with open(os.path.join(outdir,'PBL_SUBPANEL_BOUNDS.csv'),'wb') as f:
            w=csv.DictWriter(f,fieldnames=fields); w.writeheader()
            for r in records: w.writerow({k:r[k] for k in fields})
        with open(os.path.join(outdir,'PBL_SUBPANEL_NODES.csv'),'wb') as f:
            w=csv.writer(f); w.writerow(['subpanel_id','side','node_label','x','y','z'])
            for r in records:
                for nl in r['node_labels']:
                    p=nodes[nl]; w.writerow([r['subpanel_id'],r['side'],nl,p[0],p[1],p[2]])
        print('PASS subpanels=%d top=%d bottom=%d' % (len(records),sum(r['side']=='TOP' for r in records),sum(r['side']=='BOTTOM' for r in records)))
    finally:
        odb.close()

if __name__=='__main__': main()
