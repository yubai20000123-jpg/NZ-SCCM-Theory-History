# -*- coding: utf-8 -*-
from __future__ import print_function
import argparse,csv,json,math,os
from collections import defaultdict
from odbAccess import openOdb


def vsub(a,b): return (a[0]-b[0],a[1]-b[1],a[2]-b[2])
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def norm(a): return math.sqrt(sum(x*x for x in a))

def area_xz(pts):
    s=0.0
    for i in range(len(pts)):
        x1,z1=pts[i][0],pts[i][2]; x2,z2=pts[(i+1)%len(pts)][0],pts[(i+1)%len(pts)][2]
        s+=x1*z2-x2*z1
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

def fit(rows,vals,sgn,mode):
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
            'R2':1.0-s/sp if sp>1e-30 else (1.0 if s<=1e-30 else 0.0),
            'RMS_mm':rms,'NRMS':rms/max(abs(W),1e-30)}

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

def sum_rf3(frame,region):
    if 'RF' not in frame.fieldOutputs: raise RuntimeError('RF field missing')
    vals=frame.fieldOutputs['RF'].getSubset(region=region).values
    s=0.0; n=0
    for v in vals:
        if len(v.data)>=3: s+=float(v.data[2]); n+=1
    return s,n

def reaction_regions(odb):
    out=[]; ra=odb.rootAssembly
    for name,reg in ra.nodeSets.items(): out.append(('ASSEMBLY::'+name,reg))
    for iname,inst in ra.instances.items():
        for name,reg in inst.nodeSets.items(): out.append((iname+'::'+name,reg))
    return out

def choose_reaction_region(odb,peak_frame,expected_peak_mn,max_rel_error):
    target=abs(expected_peak_mn)*1e6; cand=[]
    for name,reg in reaction_regions(odb):
        try: s,n=sum_rf3(peak_frame,reg)
        except Exception: continue
        if n==0: continue
        mag=abs(s); rel=abs(mag-target)/max(target,1.0)
        cand.append({'name':name,'region':reg,'sum_RF3_N':s,'n_values':n,'rel_error':rel})
    cand.sort(key=lambda x:x['rel_error'])
    if not cand or cand[0]['rel_error']>max_rel_error:
        top=[dict((k,v) for k,v in x.items() if k!='region') for x in cand[:20]]
        raise RuntimeError('no reaction node set matches expected peak within tolerance; best=%s'%repr(top))
    best=cand[0]
    return best,[dict((k,v) for k,v in x.items() if k!='region') for x in cand[:20]]
def airy_P(q,pcr,C,q0):
    return pcr*q/(q+q0)+C*q*(q+2.0*q0) if q>=0.0 else None
def airy_q(P,pcr,C,q0):
    if P<=0.0: return 0.0
    lo=0.0; hi=max(q0,1e-6)
    while airy_P(hi,pcr,C,q0)<P:
        hi*=2.0
        if hi>10.0: raise RuntimeError('cannot bracket Airy q')
    for _ in range(100):
        mid=0.5*(lo+hi)
        if airy_P(mid,pcr,C,q0)<P: lo=mid
        else: hi=mid
    return 0.5*(lo+hi)
def first_sustained(rows,pred,n,start_p):
    run=0; start=None
    for r in rows:
        if r['P_FE_MN']<start_p: run=0; start=None; continue
        if pred(r):
            if run==0: start=r
            run+=1
            if run>=n: return start
        else: run=0; start=None
    return None
def slim(r):
    if r is None: return None
    return dict((k,r[k]) for k in ['frame','time_s','P_FE_MN','q_FE','q_Airy_same_load','P_Airy_at_qFE_MN','load_bias','q_bias','R2','NRMS'])

def main():
    ap=argparse.ArgumentParser(description='Read-only full-frame BH P-q-R2 audit against frozen Airy P(q).')
    ap.add_argument('odb'); ap.add_argument('outdir'); ap.add_argument('b',type=float); ap.add_argument('a',type=float); ap.add_argument('mstar',type=int); ap.add_argument('q0',type=float)
    ap.add_argument('pcr_mn',type=float); ap.add_argument('C_mn',type=float); ap.add_argument('peak_frame',type=int); ap.add_argument('peak_p_mn',type=float)
    ap.add_argument('--peak-time',type=float,default=None); ap.add_argument('--step',default='EXPLICIT_LOADING'); ap.add_argument('--instance',default='C-S-SHELL-1')
    ap.add_argument('--normal-cut',type=float,default=0.90); ap.add_argument('--pair-tol',type=float,default=None); ap.add_argument('--reaction-match-tol',type=float,default=0.01)
    args=ap.parse_args()
    if not os.path.isdir(args.outdir): os.makedirs(args.outdir)
    odb=openOdb(args.odb,readOnly=True)
    try:
        if args.step not in odb.steps: raise RuntimeError('step not found')
        if args.instance not in odb.rootAssembly.instances: raise RuntimeError('instance not found')
        step=odb.steps[args.step]; inst=odb.rootAssembly.instances[args.instance]
        if len(step.frames)!=501: print('WARNING frame count=%d, expected 501'%len(step.frames))
        if args.peak_frame<0 or args.peak_frame>=len(step.frames): raise RuntimeError('peak frame out of range')
        pf=step.frames[args.peak_frame]
        if args.peak_time is not None and abs(float(pf.frameValue)-args.peak_time)>1e-4: raise RuntimeError('peak frame/time mismatch')
        rows,tol,bounds=face_pairs(inst,args.normal_cut,args.pair_tol); xmin,xmax,zmin,zmax=bounds; lx=xmax-xmin; lz=zmax-zmin
        for r in rows:
            r['phi']=math.sin(math.pi*(r['x']-xmin)/lx)*math.sin(args.mstar*math.pi*(r['z']-zmin)/lz)
        y0=[r['ym0'] for r in rows]; init0=fit_mode(rows,y0,1.0); sgn=1.0 if init0['W_mm']>=0.0 else -1.0; init=fit_mode(rows,y0,sgn)
        best,cands=choose_reaction_region(odb,pf,args.peak_p_mn,args.reaction_match_tol); reaction_region=best['region']
        path=[]
        for iframe,frame in enumerate(step.frames):
            Uf=frame.fieldOutputs['U'].getSubset(region=inst); umap=dict((v.nodeLabel,float(v.data[1])) for v in Uf.values if len(v.data)>=2)
            valid=[]; vals=[]
            for r in rows:
                if r['up'] in umap and r['lo'] in umap:
                    valid.append(r); vals.append(0.5*(umap[r['up']]+umap[r['lo']]))
            if len(valid)<max(20,int(0.8*len(rows))): raise RuntimeError('insufficient U2 pairs frame %d'%iframe)
            fm=fit_mode(valid,vals,sgn); W=fm['W_mm']; q=W/args.b
            rf,nrf=sum_rf3(frame,reaction_region); P=abs(rf)/1e6
            qA=airy_q(P,args.pcr_mn,args.C_mn,args.q0); PA=airy_P(q,args.pcr_mn,args.C_mn,args.q0) if q>=0 else None
            load_bias=(PA/P-1.0) if (PA is not None and P>1e-9) else None
            q_bias=(q/qA-1.0) if qA>1e-12 else None
            path.append({'frame':iframe,'time_s':float(frame.frameValue),'P_FE_MN':P,'RF3_N':rf,'RF_values':nrf,
                         'Wd_FE_mm':W,'q_FE':q,'kappa_FE_geom_per_mm':W*(args.mstar*math.pi/lz)**2,
                         'R2':fm['R2'],'RMS_mm':fm['RMS_mm'],'NRMS':fm['NRMS'],'q_Airy_same_load':qA,
                         'P_Airy_at_qFE_MN':PA,'load_bias':load_bias,'q_bias':q_bias,'c0_mm':fm['c0'],'cx_mm':fm['cx'],'cz_mm':fm['cz']})
        pre=path[:args.peak_frame+1]; start_p=0.05*args.peak_p_mn
        events={'first_positive_load_bias_10frames':slim(first_sustained(pre,lambda r:r['load_bias'] is not None and r['load_bias']>0.0,10,start_p))}
        for th in [0.02,0.05,0.10,0.20,0.50]:
            events['load_bias_ge_%g_pct_5frames'%(100*th)]=slim(first_sustained(pre,lambda r,t=th:r['load_bias'] is not None and r['load_bias']>=t,5,start_p))
            events['q_bias_ge_%g_pct_5frames'%(100*th)]=slim(first_sustained(pre,lambda r,t=th:r['q_bias'] is not None and r['q_bias']>=t,5,start_p))
        for th in [0.95,0.90,0.80,0.70,0.60]: events['R2_le_%g_5frames'%th]=slim(first_sustained(pre,lambda r,t=th:r['R2']<=t,5,start_p))
        for th in [0.05,0.10,0.20,0.30]: events['NRMS_ge_%g_5frames'%th]=slim(first_sustained(pre,lambda r,t=th:r['NRMS']>=t,5,start_p))
        fields=['frame','time_s','P_FE_MN','RF3_N','RF_values','Wd_FE_mm','q_FE','kappa_FE_geom_per_mm','R2','RMS_mm','NRMS','q_Airy_same_load','P_Airy_at_qFE_MN','load_bias','q_bias','c0_mm','cx_mm','cz_mm']
        with open(os.path.join(args.outdir,'FEM_FULL_PATH_P_Q_R2.csv'),'wb') as f:
            w=csv.DictWriter(f,fieldnames=fields); w.writeheader()
            for r in path: w.writerow(r)
        summary={'status':'FULL_501_FRAME_P_Q_R2_AUDIT_EXECUTED','diagnostic_only':True,'theory_modified':False,'odb':os.path.abspath(args.odb),'step':args.step,'instance':args.instance,
                 'n_frames':len(path),'peak_contract':{'frame':args.peak_frame,'time_s':float(pf.frameValue),'P_expected_MN':args.peak_p_mn,'P_extracted_MN':path[args.peak_frame]['P_FE_MN']},
                 'reaction_region':dict((k,v) for k,v in best.items() if k!='region'),'reaction_candidates_top20':cands,
                 'initial':{'W0_FE_mm':init['W_mm'],'q0_FE':init['W_mm']/args.b,'q0_theory':args.q0,'R2':init['R2'],'NRMS':init['NRMS']},
                 'theory':{'Pcr_MN':args.pcr_mn,'C_MN':args.C_mn,'q0':args.q0,'P_of_q':'Pcr*q/(q+q0)+C*q*(q+2*q0)'},
                 'peak':path[args.peak_frame],'events_prepeak':events,
                 'interpretation_rule':'positive load_bias means frozen Airy requires more load than FEM to reach the same projected q; thresholds are diagnostic onset markers, not acceptance criteria.'}
        with open(os.path.join(args.outdir,'FEM_FULL_PATH_P_Q_R2_SUMMARY.json'),'w') as f: json.dump(summary,f,indent=2,sort_keys=True)
        print('PASS frames=%d reaction=%s peak P=%.9g MN q=%.9g R2=%.6f'%(len(path),best['name'],path[args.peak_frame]['P_FE_MN'],path[args.peak_frame]['q_FE'],path[args.peak_frame]['R2']))
    finally: odb.close()
if __name__=='__main__': main()
