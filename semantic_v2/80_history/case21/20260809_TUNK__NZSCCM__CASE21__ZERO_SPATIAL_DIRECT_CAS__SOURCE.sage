# NZ-SCCM Case21: zero-spatial-sampling direct CAS integration task
# Intended runtime: SageMath with FriCAS installed (primary), Giac/Maxima/SymPy fallback.
# Frozen theory: NZ_SCCM_CURRENT_OPERATOR_EXPLICIT_NC_REBAR_V1_20260809.md
# No spatial quadrature, collocation, DCT, material grid, or sampled interpolation is used here.

import os, json, time, traceback
from pathlib import Path

OUT = Path(os.environ.get('NZ_CASE21_OUT', 'sage_fricas_execution'))
OUT.mkdir(parents=True, exist_ok=True)
TRACE = OUT/'integration_trace'
TRACE.mkdir(exist_ok=True)

# -----------------------------------------------------------------------------
# Logging utilities
# -----------------------------------------------------------------------------
RUNLOG = OUT/'sage_fricas_run.log'
def log(msg):
    s = str(msg)
    print(s)
    with open(RUNLOG,'a',encoding='utf-8') as fh:
        fh.write(s+'\n')

def save(name, obj):
    p = TRACE/name
    with open(p,'w',encoding='utf-8') as fh:
        fh.write(str(obj))
    return p

import sage.version
log('Sage version: %s' % sage.version.version)
try:
    from sage.interfaces.fricas import fricas
    log('FriCAS interface loaded. FriCAS version query: %s' % fricas.eval(')version'))
except Exception as e:
    fricas = None
    log('FriCAS interface unavailable: %r' % e)

# -----------------------------------------------------------------------------
# Exact symbols and Case21 constants
# -----------------------------------------------------------------------------
D,q,u,v,z = var('D q u v z', domain='real')
assume(D > 0)
assume(q > 0)
# u,v are tangent-half-angle variables for X,Y in [0,pi], hence [0,+infinity).
# We do not impose u/v assumptions globally because some external CAS interfaces
# handle endpoint limits more reliably without Sage assumptions.

fc   = QQ(2123)/100
E0   = ZZ(20321)
eps0 = QQ(209)/100000
nu   = QQ(9)/50
b    = ZZ(1220)
ell  = ZZ(1220)
t    = QQ(193)/10
q0   = QQ(1)/400
rho  = QQ(1)/10
kappa = E0*eps0/fc
xcr = rho/kappa
eta = xcr/20
eta_r = QQ(1)/20
mt = -QQ(7)/90
acc = QQ(214465849872483)/2000000000000000
at = 1 - 2^(-QQ(1)/8)

# -----------------------------------------------------------------------------
# Tangent-half-angle transformation (exact, no samples)
# X,Y in [0,pi]: u=tan(X/2), v=tan(Y/2), u,v in [0,+infinity)
# ----------------------------------------------------------------------------
sX = 2*u/(1+u^2); cX = (1-u^2)/(1+u^2)
sY = 2*v/(1+v^2); cY = (1-v^2)/(1+v^2)
Jxy = 4/((1+u^2)*(1+v^2))

Cm  = pi^2/eps0*(q0*q + q^2/2)
Cb  = pi^2/(2*eps0)*(t/b)*q
Cmq = pi^2/eps0*(q0+q)
Cbq = pi^2/(2*eps0)*(t/b)

ex  = nu*D + Cm*cX^2*sY^2 + Cb*sX*sY*z
ey  = -D   + Cm*sX^2*cY^2 + Cb*sX*sY*z
gxy = 2*Cm*sX*cX*sY*cY - 2*Cb*cX*cY*z

exq  = Cmq*cX^2*sY^2 + Cbq*sX*sY*z
eyq  = Cmq*sX^2*cY^2 + Cbq*sX*sY*z
gxyq = 2*Cmq*sX*cX*sY*cY - 2*Cbq*cX*cY*z

epsx = eps0*ex; epsy = eps0*ey; gam = eps0*gxy
X11=(epsx+nu*epsy)/((1-nu^2)*eps0)
X22=(nu*epsx+epsy)/((1-nu^2)*eps0)
X12=gam/(2*(1+nu)*eps0)
mu=(X11+X22)/2
delta=(X11-X22)/2
rad=sqrt(delta^2+X12^2)
lp=mu+rad
lm=mu-rad

def PiEta(w):
    return w^2*(sqrt(w^2+eta^2)+w)/(2*(w^2+eta^2))

def HH(r,r0):
    return ((r-r0)+sqrt((r-r0)^2+eta_r^2))/2 - ((-r0)+sqrt(r0^2+eta_r^2))/2

def principal(lam):
    cc=PiEta(-lam); tt=PiEta(lam)
    C=kappa*cc/(1+(kappa-2)*cc+cc^2)
    rr=tt/xcr
    T=rr+(mt-1)*HH(rr,1)-mt*HH(rr,10)
    U=kappa*lam-C+kappa*cc+rho*T-kappa*tt
    return U,C,T,cc,tt

Up,Cp,Tp,cp,tp = principal(lp)
Um,Cm_,Tm,cm,tm = principal(lm)
sp_ = Up - acc*Cp^2*Cm_ + Cp*Tm - rho*at*Tp*Tm^8
sm_ = Um - acc*Cm_^2*Cp + Cm_*Tp - rho*at*Tm*Tp^8
Savg=(sp_+sm_)/2
Sdiff=(sp_-sm_)/2
# Generic rad>0 branch. The frozen theory defines the continuous rad=0 limit.
Sxx=Savg+Sdiff*delta/rad
Syy=Savg-Sdiff*delta/rad
Sxy=Sdiff*X12/rad
sigx=fc*Sxx; sigy=fc*Syy; tauxy=fc*Sxy

fPalg = sigy*Jxy
fRalg = (sigx*exq + sigy*eyq + tauxy*gxyq)*Jxy

save('00_fP_alg.txt',fPalg)
save('00_fR_alg.txt',fRalg)
save('00_sigma_x_alg.txt',sigx)
save('00_sigma_y_alg.txt',sigy)
save('00_tau_xy_alg.txt',tauxy)
log('Exact transformed integrands constructed. No spatial sampling performed.')

# -----------------------------------------------------------------------------
# CAS primitive attempt: FriCAS primary, then Giac, Maxima, SymPy.
# An integration result is accepted only if it is not visibly unevaluated and
# diff(F,x)-f simplifies/is_zero exactly.
# -----------------------------------------------------------------------------
BACKENDS=['fricas','giac','maxima','sympy']

def visible_unevaluated(F):
    s=str(F).lower()
    return ('integrate(' in s or 'integral(' in s or "'integrate" in s)

def verify_primitive(F, f, x):
    try:
        r=(diff(F,x)-f).simplify_full()
        save('verify_tmp.txt',r)
        if r == 0:
            return True, 'simplify_full -> 0'
        try:
            rr=r.canonicalize_radical().simplify_full()
            if rr == 0:
                return True, 'canonicalize_radical+simplify_full -> 0'
        except Exception:
            pass
        return False, str(r)[:1000]
    except Exception as e:
        return False, 'verification exception: %r' % e

def primitive_with_backends(f,x,label):
    save(label+'_input.txt',f)
    records=[]
    for alg in BACKENDS:
        t0=time.time()
        log('[%s] attempt backend=%s variable=%s' % (label,alg,x))
        try:
            F=integral(f,x,algorithm=alg)
            elapsed=time.time()-t0
            save(label+'_'+alg+'_primitive.txt',F)
            uneval=visible_unevaluated(F)
            ok,msg=verify_primitive(F,f,x) if not uneval else (False,'unevaluated integral visible')
            rec={'label':label,'backend':alg,'elapsed_s':elapsed,'unevaluated':uneval,'derivative_verified':ok,'verification':msg,'return_type':str(type(F))}
            records.append(rec)
            with open(TRACE/(label+'_backend_records.json'),'w',encoding='utf-8') as fh: json.dump(records,fh,indent=2)
            log(rec)
            if ok and not uneval:
                return F,alg,records
        except Exception as e:
            elapsed=time()-t0
            rec={'label':label,'backend':alg,'elapsed_s':elapsed,'exception':repr(e),'traceback':traceback.format_exc()}
            records.append(rec)
            with open(TRACE/(label+'_backend_records.json'),'w',encoding='utf-8') as fh: json.dump(records,fh,indent=2)
            log(rec)
    raise RuntimeError('No backend returned a derivative-verified primitive for '+label)

def definite_from_primitive(F,x,a,bnd,label):
    # Finite endpoints use substitution. Infinite endpoint uses one-sided limit.
    if bnd == Infinity:
        Fb=limit(F,x=Infinity,dir='-')
    else:
        Fb=F.subs({x:bnd})
    if a == -Infinity:
        Fa=limit(F,x=-Infinity,dir='+')
    else:
        Fa=F.subs({x:a})
    out=(Fb-Fa).simplify_full()
    save(label+'_endpoint_upper.txt',Fb)
    save(label+'_endpoint_lower.txt',Fa)
    save(label+'_definite.txt',out)
    return out

# Stage P: z -> u -> v
try:
    FPz, bpz, _ = primitive_with_backends(fPalg,z,'P_01_z')
    IPz = definite_from_primitive(FPz,z,-1,1,'P_01_z')
    FPu, bpu, _ = primitive_with_backends(IPz,u,'P_02_u')
    IPu = definite_from_primitive(FPu,u,0,Infinity,'P_02_u')
    FPv, bpv, _ = primitive_with_backends(IPu,v,'P_03_v')
    IP = definite_from_primitive(FPv,v,0,Infinity,'P_03_v')
    Pc = (-b*t/(2*pi^2))*IP
    save('P_FINAL_Pc_N.txt',Pc)
    log('Pc(D,q) analytic construction complete.')
    P_OK=True
except Exception as e:
    log('P analytic chain unresolved: %r' % e)
    P_OK=False

# Stage R: z -> u -> v
try:
    FRz, brz, _ = primitive_with_backends(fRalg,z,'R_01_z')
    IRz = definite_from_primitive(FRz,z,-1,1,'R_01_z')
    FRu, bru, _ = primitive_with_backends(IRz,u,'R_02_u')
    IRu = definite_from_primitive(FRu,u,0,Infinity,'R_02_u')
    FRv, brv, _ = primitive_with_backends(IRu,v,'R_03_v')
    IR = definite_from_primitive(FRv,v,0,Infinity,'R_03_v')
    Rqc = (eps0*b*ell*t/(2*pi^2))*IR
    save('R_FINAL_Rqc.txt',Rqc)
    log('Rq,c(D,q) analytic construction complete.')
    R_OK=True
except Exception as e:
    log('R analytic chain unresolved: %r' % e)
    R_OK=False

# -----------------------------------------------------------------------------
# Exact steel contribution: Case21 reachable branch is checked after analytic
# concrete root. The formula below is valid while |eps_s| <= eps_y everywhere.
# It uses no steel integration points.
# -----------------------------------------------------------------------------
Es=ZZ(200000)
rhos=QQ(375)/100000 # 0.00375 per direction
S=q0*q+q^2/2
Ps_N = rhos*t*b*Es*eps0*(D-Cm/4)
Rqs  = rhos*t*Es*pi^2*(q0+q)*b*ell*(eps0*D*(nu-1)/4 + 9*pi^2*S/32)
save('STEEL_Ps_N_elastic.txt',Ps_N)
save('STEEL_Rqs_elastic.txt',Rqs)

# -----------------------------------------------------------------------------
# Root calculation is executed only after both analytic concrete expressions
# exist. Multiple broad seeds are used; reference 338.318/342.334 values are
# never used as equations or calibration targets.
# -----------------------------------------------------------------------------
def numerical_root_family(Pexpr,Rexpr,label):
    import mpmath as mp
    mp.mp.dps=60
    PD=diff(Pexpr,D); Pq=diff(Pexpr,q)
    RD=diff(Rexpr,D); Rq_=diff(Rexpr,q)
    Lexpr=(PD*Rq_ - Pq*RD).simplify_full()
    save(label+'_L.txt',Lexpr)
    R80=RealField(256)
    def ev(expr,dd,qq):
        return mp.mpf(str(expr.subs({D:R80(str(dd)),q:R80(str(qq))}).n(70)))
    def f1(dd,qq): return ev(Rexpr,dd,qq)
    def f2(dd,qq): return ev(Lexpr,dd,qq)
    roots=[]
    # Parameter-space multistart only; this is NOT spatial sampling.
    seedsD=[0.15,0.30,0.45,0.60,0.75,0.90,1.05]
    seedsq=[0.00025,0.00075,0.0015,0.0025,0.0040,0.0060]
    for d0 in seedsD:
        for q00 in seedsq:
            try:
                r=mp.findroot((f1,f2),(mp.mpf(d0),mp.mpf(q00)),tol=mp.mpf('1e-35'),maxsteps=80)
                dd,qq=r[0],r[1]
                if dd>0 and qq>0 and dd<2 and qq<0.05:
                    if all(abs(dd-a)>mp.mpf('1e-20') or abs(qq-bb)>mp.mpf('1e-20') for a,bb in roots):
                        roots.append((dd,qq))
            except Exception:
                pass
    rec=[]
    for dd,qq in roots:
        rec.append({'D':mp.nstr(dd,30),'q':mp.nstr(qq,30),'A_mm':mp.nstr(1220*qq,30),'P_kN':mp.nstr(ev(Pexpr,dd,qq)/1000,30),'R':mp.nstr(f1(dd,qq),8),'L':mp.nstr(f2(dd,qq),8)})
    with open(OUT/(label+'_root_family.json'),'w',encoding='utf-8') as fh: json.dump(rec,fh,indent=2)
    return rec

if P_OK and R_OK:
    try:
        concrete_roots=numerical_root_family(Pc,Rqc,'concrete')
        log('Concrete stationary root family: '+str(concrete_roots))
        # Total RC analytic equations under elastic reinforcement law.
        Ptot=(Pc+Ps_N).simplify_full()
        Rtot=(Rqc+Rqs).simplify_full()
        save('RC_P_total_N.txt',Ptot); save('RC_Rq_total.txt',Rtot)
        rc_roots=numerical_root_family(Ptot,Rtot,'RC')
        log('RC stationary root family: '+str(rc_roots))
    except Exception as e:
        log('Root phase exception: %r' % e)
else:
    log('Root phase skipped because zero-spatial-sampling Pc/Rqc was not completed.')

status={'P_OK':P_OK,'R_OK':R_OK,'formal_spatial_sampling':0,'formal_spatial_quadrature':0}
with open(OUT/'execution_status.json','w',encoding='utf-8') as fh: json.dump(status,fh,indent=2)
log(status)
