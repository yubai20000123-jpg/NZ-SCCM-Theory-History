# -*- coding: utf-8 -*-
from __future__ import print_function

import argparse
import csv
import json
import math
import os
from collections import defaultdict
from odbAccess import openOdb


def vsub(a,b): return (a[0]-b[0],a[1]-b[1],a[2]-b[2])
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def norm(a): return math.sqrt(a[0]*a[0]+a[1]*a[1]+a[2]*a[2])


def area_xz(pts):
    s=0.0
    for i in range(len(pts)):
        x1,z1=pts[i][0],pts[i][2]; x2,z2=pts[(i+1)%len(pts)][0],pts[(i+1)%len(pts)][2]
        s += x1*z2-x2*z1
    return 0.5*abs(s)


def solve(A,b):
    n=len(b); M=[list(A[i])+[float(b[i])] for i in range(n)]
    for k in range(n):
        p=max(range(k,n),key=lambda i:abs(M[i][k]))
        if abs(M[p][k])<1e-20: raise RuntimeError('singular normal equation')
        if p!=k: M[k],M[p]=M[p],M[k]
        d=M[k][k]
        for j in range(k,n+1): M[k][j]/=d
        for i in range(n):
            if i==k: continue
            f=M[i][k]
            for j in range(k,n+1): M[i][j]-=f*M[k][j]
    return [M[i][n] for i in range(n)]


def fit(rows,vals,sgn,mode=True):
    n=4 if mode else 3; A=[[0.0]*n for _ in range(n)]; b=[0.0]*n
    for r,y in zip(rows,vals):
        c=[1.0,r['xn'],r['zn']]
        if mode: c.append(sgn*r['phi'])
        w=r['w']
        for i in range(n):
            b[i]+=w*c[i]*y
            for j in range(n): A[i][j]+=w*c[i]*c[j]
    q=solve(A,b); sse=0.0; sw=0.0
    for r,y in zip(rows,vals):
        c=[1.0,r['xn'],r['zn']]
        if mode: c.append(sgn*r['phi'])
        yp=sum(q[i]*c[i] for i in range(n)); w=r['w']; sse+=w*(y-yp)**2; sw+=w
    return q,sse,sw


def fit_mode(rows,vals,sgn):
    qp,sp,sw=fit(rows,vals,sgn,False); q,s,sw=fit(rows,vals,sgn,True)
    W=q[3]; rms=math.sqrt(max(s,0.0)/max(sw,1e-30))
    return {'c0':q[0],'cx':q[1],'cz':q[2],'W_mm':W,
            'modal_R2_after_plane':1.0-s/sp if sp>1e-30 else (1.0 if s<=1e-30 else 0.0),
            'rms_residual_mm':rms,'nrms_residual_over_absW':rms/max(abs(W),1e-30)}


def face_pairs(inst,normal_cut,pair_tol):
    nodes=dict((n.label,tuple(float(x) for x in n.coordinates)) for n in inst.nodes)
    wt=defaultdict(float); labs=set(); xs=[]; zs=[]
    for e in inst.elements:
        if not str(getattr(e,'type','')).upper().startswith('S') or len(e.connectivity)<3: continue
        pts=[nodes[x] for x in e.connectivity]; nn=cross(vsub(pts[1],pts[0]),vsub(pts[2],pts[0])); nnorm=norm(nn)
        if nnorm<=1e-20 or abs(nn[1]/nnorm)<normal_cut: continue
        a=area_xz(pts)
        if a<=0.0: continue
        sh=a/len(e.connectivity)
        for lab in e.connectivity:
            labs.add(lab); wt[lab]+=sh; xs.append(nodes[lab][0]); zs.append(nodes[lab][2])
    if not labs: raise RuntimeError('no horizontal shell face nodes')
    if pair_tol is None: pair_tol=max(1e-5,1e-6*max(max(xs)-min(xs),max(zs)-min(zs)))
    buck=defaultdict(list)
    for lab in labs:
        x,y,z=nodes[lab]; buck[(int(round(x/pair_tol)),int(round(z/pair_tol)))].append(lab)
    raw=[]
    for ll in buck.values():
        if len(ll)<2: continue
        ll=sorted(ll,key=lambda lab:nodes[lab][1]); lo,up=ll[0],ll[-1]
        xl,yl,zl=nodes[lo]; xu,yu,zu=nodes[up]
        if yu-yl<1.0: continue
        w=0.5*(wt[lo]+wt[up])
        if w>0: raw.append((0.5*(xl+xu),0.5*(zl+zu),up,lo,0.5*(yl+yu),w))
    if len(raw)<20: raise RuntimeError('too few top-bottom pairs: %d'%len(raw))
    xmin=min(r[0] for r in raw); xmax=max(r[0] for r in raw); zmin=min(r[1] for r in raw); zmax=max(r[1] for r in raw)
    lx=xmax-xmin; lz=zmax-zmin; rows=[]
    for x,z,up,lo,ym,w in raw:
        rows.append({'x':x,'z':z,'up':up,'lo':lo,'ym0':ym,'w':w,
                     'xn':(x-0.5*(xmin+xmax))/lx,'zn':(z-0.5*(zmin+zmax))/lz})
    return rows,pair_tol,(xmin,xmax,zmin,zmax)


def main():
    ap=argparse.ArgumentParser(description='Canonical BH peak-frame U2 -> global q projection; read-only ODB.')
    ap.add_argument('odb'); ap.add_argument('outdir'); ap.add_argument('b',type=float); ap.add_argument('a',type=float)
    ap.add_argument('mstar',type=int); ap.add_argument('q0',type=float); ap.add_argument('peak_frame',type=int)
    ap.add_argument('--peak-time',type=float,default=None); ap.add_argument('--step',default='EXPLICIT_LOADING')
    ap.add_argument('--instance',default='C-S-SHELL-1'); ap.add_argument('--normal-cut',type=float,default=0.90)
    ap.add_argument('--pair-tol',type=float,default=None); args=ap.parse_args()
    if not os.path.isdir(args.outdir): os.makedirs(args.outdir)
    odb=openOdb(args.odb,readOnly=True)
    try:
        if args.step not in odb.steps: raise RuntimeError('step not found')
        if args.instance not in odb.rootAssembly.instances: raise RuntimeError('instance not found: '+args.instance)
        step=odb.steps[args.step]; inst=odb.rootAssembly.instances[args.instance]
        if args.peak_frame<0 or args.peak_frame>=len(step.frames): raise RuntimeError('peak frame index out of range')
        frame=step.frames[args.peak_frame]
        if args.peak_time is not None and abs(float(frame.frameValue)-args.peak_time)>1e-4:
            raise RuntimeError('peak frame/time mismatch: frame time %.12g expected %.12g'%(frame.frameValue,args.peak_time))
        rows,tol,bounds=face_pairs(inst,args.normal_cut,args.pair_tol)
        xmin,xmax,zmin,zmax=bounds; lx=xmax-xmin; lz=zmax-zmin
        for r in rows:
            xi=(r['x']-xmin)/lx; eta=(r['z']-zmin)/lz
            r['phi']=math.sin(math.pi*xi)*math.sin(args.mstar*math.pi*eta)
        y0=[r['ym0'] for r in rows]; p0=fit_mode(rows,y0,1.0); sgn=1.0 if p0['W_mm']>=0 else -1.0; init=fit_mode(rows,y0,sgn)
        Uf=frame.fieldOutputs['U'].getSubset(region=inst)
        umap=dict((v.nodeLabel,float(v.data[1])) for v in Uf.values if len(v.data)>=2)
        valid=[]; u=[]
        for r in rows:
            if r['up'] in umap and r['lo'] in umap:
                valid.append(r); u.append(0.5*(umap[r['up']]+umap[r['lo']]))
        if len(valid)<max(20,int(0.8*len(rows))): raise RuntimeError('insufficient U2 pairs: %d/%d'%(len(valid),len(rows)))
        peak=fit_mode(valid,u,sgn); W=peak['W_mm']
        init.update({'q0_FE':init['W_mm']/args.b,'q0_theory':args.q0,'q0_ratio_FE_over_theory':(init['W_mm']/args.b)/args.q0,
                     'kappa_x_FE_geom_per_mm':init['W_mm']*(math.pi/lx)**2,
                     'kappa_y_FE_geom_per_mm':init['W_mm']*(args.mstar*math.pi/lz)**2})
        peak.update({'frame_index':args.peak_frame,'time_s':float(frame.frameValue),'n_pairs':len(valid),'q_FE':W/args.b,
                     'kappa_x_FE_geom_per_mm':W*(math.pi/lx)**2,'kappa_y_FE_geom_per_mm':W*(args.mstar*math.pi/lz)**2})
        summary={'status':'PEAK_FEM_GLOBAL_MODE_PROJECTION_EXECUTED','diagnostic_only':True,'theory_modified':False,
                 'formal_structural_spatial_quadrature':0,'material_points':0,'odb':os.path.abspath(args.odb),'step':args.step,'instance':args.instance,
                 'contract':{'FE_X':'theory_x','FE_Z':'theory_y_loading','FE_Y':'out_of_plane','incremental_w':'U2','mode_sign':'from_initial_imperfection','rigid_terms_removed':['1','X','Z'],'field_subset':'U.getSubset(region=C-S-SHELL-1)'},
                 'theory':{'b_mm':args.b,'a_mm':args.a,'mstar':args.mstar,'q0':args.q0},
                 'mesh':{'pair_tol_mm':tol,'n_pairs':len(rows),'xmin':xmin,'xmax':xmax,'Lx_FE_mm':lx,'zmin':zmin,'zmax':zmax,'Lz_FE_mm':lz,'Lx_FE_over_b':lx/args.b,'Lz_FE_over_a':lz/args.a},
                 'initial':init,'peak':peak}
        with open(os.path.join(args.outdir,'FEM_GLOBAL_OUT_OF_PLANE_MODE_SUMMARY.json'),'w') as f: json.dump(summary,f,indent=2,sort_keys=True)
        with open(os.path.join(args.outdir,'FEM_GLOBAL_MODE_PAIRED_NODES.csv'),'wb') as f:
            w=csv.writer(f); w.writerow(['x','z','top_node','bottom_node','ymid0','area_weight','phi_aligned'])
            for r in rows: w.writerow([r['x'],r['z'],r['up'],r['lo'],r['ym0'],r['w'],sgn*r['phi']])
        print('PASS case ODB=%s frame=%d time=%.12g'%(os.path.basename(args.odb),args.peak_frame,frame.frameValue))
        print('initial W0=%.12g q0_FE=%.12g R2=%.6f'%(init['W_mm'],init['q0_FE'],init['modal_R2_after_plane']))
        print('peak Wd=%.12g q_FE=%.12g kappa_y=%.12g R2=%.6f'%(W,peak['q_FE'],peak['kappa_y_FE_geom_per_mm'],peak['modal_R2_after_plane']))
    finally:
        odb.close()

if __name__=='__main__': main()
