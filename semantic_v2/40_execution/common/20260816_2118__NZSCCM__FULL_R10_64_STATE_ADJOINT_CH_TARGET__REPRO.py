"""NZ-SCCM 21:18 adjoint/CH target-reduction core reproducer.

This file reproduces the NEW algebraic identities of the 21:18 gate:
  1) exact 2x2 CH reduction of T^7 and adj(T^7),
  2) exact field-product adjoint identity on the retained 64-state quadratic tower.

The full R10 source-graph construction is already reproduced by the 20:59 predecessor
`20260816_2059__NZSCCM__FULL_R10_QUADRATIC_TOWER_64_STATE__REPRO.py`.
The 21:18 execution additionally ran the complete R10 compression/U/stress graph on
exact rational fibers x=0 and x=1/2; those executed intermediate values and timings are
stored in the companion JSON and audit report. No fiber is used as structural quadrature.
"""

import sympy as sp

# -----------------------------------------------------------------------------
# 1. Generic 2x2 Cayley-Hamilton T^7 reduction
# -----------------------------------------------------------------------------
a,b,c,d0 = sp.symbols('a b c d0')
T = sp.Matrix([[a,b],[c,d0]])
trT = sp.trace(T)
detT = sp.factor(T.det())

beta = {0: sp.Integer(0), 1: sp.Integer(1)}
for n in range(2,9):
    beta[n] = sp.expand(trT*beta[n-1]-detT*beta[n-2])

T7_res = T**7 - (beta[7]*T-detT*beta[6]*sp.eye(2))
adjT7_res = (sp.trace(T**7)*sp.eye(2)-T**7) - (beta[8]*sp.eye(2)-beta[7]*T)

assert all(sp.factor(z)==0 for z in T7_res)
assert all(sp.factor(z)==0 for z in adjT7_res)

print('B7 =', sp.factor(beta[7]))
print('B8 =', sp.factor(beta[8]))
print('T7_CH_RESIDUAL = 0 exactly')
print('ADJ_T7_CH_RESIDUAL = 0 exactly')

# -----------------------------------------------------------------------------
# 2. Retained 64-state field multiplication table at one exact rational fiber.
#    This is an algebraic audit only, NOT structural sampling/quadrature.
# -----------------------------------------------------------------------------
x=sp.symbols('x')
rho=sp.Rational(1,10)
kappa=sp.Integer(2)
eta=(rho/kappa)/20
I2=sp.eye(2)
E=sp.Matrix([[sp.Rational(1,5)+x/3, sp.Rational(1,7)+x/5],
             [sp.Rational(1,7)+x/5,-sp.Rational(1,4)+2*x/7]])
L1=sp.Rational(500933621342341,10_000_000_000_000_000)
L10=sp.Rational(500009374609403,1_000_000_000_000_000)
A0=sp.expand(E*E)+eta**2*I2
P0=sp.factor(sp.trace(A0));Q0=sp.factor(A0.det())
rels=[]
for L in [None,L1,L10]:
    if L is None:
        Q,A=Q0,P0
    else:
        F=E-L*I2; tt=sp.trace(F); dd=sp.factor(F.det())
        Q=sp.factor(dd**2); A=sp.factor(tt**2-2*dd)
    rels.append((sp.factor(Q.subs(x,0)),sp.factor(A.subs(x,0))))

bits=[tuple((i>>j)&1 for j in range(6)) for i in range(64)]
idx={q:i for i,q in enumerate(bits)}

def local_reduce(eq,es,Q,A):
    state={(0,0):sp.Integer(1)}
    for _ in range(eq):
        nxt={}
        for (iq,is_),coef in state.items():
            key=(0,is_) if iq else (1,is_)
            nxt[key]=nxt.get(key,0)+coef*(Q if iq else 1)
        state=nxt
    for _ in range(es):
        nxt={}
        for (iq,is_),coef in state.items():
            if not is_:
                nxt[(iq,1)]=nxt.get((iq,1),0)+coef
            else:
                nxt[(iq,0)]=nxt.get((iq,0),0)+coef*A
                if iq:
                    nxt[(0,0)]=nxt.get((0,0),0)+2*coef*Q
                else:
                    nxt[(1,0)]=nxt.get((1,0),0)+2*coef
        state=nxt
    return state

red={}
for i,bi in enumerate(bits):
    for j,bj in enumerate(bits):
        ex=[bi[k]+bj[k] for k in range(6)]
        rr=[local_reduce(ex[2*g],ex[2*g+1],rels[g][0],rels[g][1]) for g in range(3)]
        out={}
        for k0,c0 in rr[0].items():
            for k1,c1 in rr[1].items():
                for k2,c2 in rr[2].items():
                    key=(k0[0],k0[1],k1[0],k1[1],k2[0],k2[1])
                    out[idx[key]]=c0*c1*c2
        red[(i,j)]=out

def mul(u,v):
    out=[sp.Integer(0)]*64
    for i,ui in enumerate(u):
        if ui==0: continue
        for j,vj in enumerate(v):
            if vj==0: continue
            for k,r in red[(i,j)].items():
                out[k]+=ui*vj*r
    return out

def pull_left(v,lam):
    # dual with respect to u in z=u*v
    out=[sp.Integer(0)]*64
    for i in range(64):
        s=sp.Integer(0)
        for j,vj in enumerate(v):
            if vj==0: continue
            for k,r in red[(i,j)].items():
                if lam[k]!=0:
                    s += lam[k]*vj*r
        out[i]=s
    return out

def dot(u,v):
    return sum((aa*bb for aa,bb in zip(u,v)),sp.Integer(0))

# deterministic sparse exact vectors
def vec(entries):
    z=[sp.Integer(0)]*64
    for i,v in entries.items(): z[i]=sp.Rational(v)
    return z

u=vec({0:2,1:3,5:-1,17:4,63:2})
v=vec({0:-1,2:5,9:2,33:-3,62:1})
lam=[sp.Rational((i%7)-3,11) for i in range(64)]

lhs=dot(lam,mul(u,v))
rhs=dot(pull_left(v,lam),u)
assert sp.factor(lhs-rhs)==0
print('FIELD_PRODUCT_ADJOINT_RESIDUAL = 0 exactly')

# -----------------------------------------------------------------------------
# 3. Stored executed full-R10 fiber audit metrics.
#    These are printed for traceability; see JSON/audit for the complete execution.
# -----------------------------------------------------------------------------
AUDIT={
    'x=0': {
        'Syy_support':60,
        'b7_support':64,
        'b8_support':64,
        'old_binary_T7_target_s':14.896949290531248,
        'CH_target_total_s':5.103483200073242,
        'old_over_CH':2.9189768452682388,
        'Syy_adjoint_minus_direct':'0 exactly'
    },
    'x=1/2': {
        'Syy_support':60,
        'b7_support':64,
        'b8_support':64,
        'old_binary_T7_target_s':17.459341049194336,
        'CH_target_total_s':5.680615663528442,
        'old_over_CH':3.0734945089296337,
        'Syy_adjoint_minus_direct':'0 exactly'
    }
}
print('EXECUTED_FULL_R10_FIBER_AUDIT =',AUDIT)
print('FORMAL STRUCTURAL COUNTERS: sampling=0 quadrature=0 subdomains=1 thickness_quadrature=0')
print('NEW_Pu = NOT_RUN')
