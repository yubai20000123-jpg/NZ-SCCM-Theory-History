#!/usr/bin/env python3
"""Constructor B: full R13 circuit -> Sage nested algebraic field -> exact annihilator.

No spatial discretization, quadrature, material points, finite-prefix evidence, or
numerical ODE stepping. This script asks a mature algebraic-function backend to
construct a scalar differential operator for the exact Syy algebraic function.

The active differential variable is r. All other physical/global/material symbols
are coefficient-field parameters. If the backend cannot support the nested tower
at this scale, this constructor is to be crossed out rather than repaired into a
new project gate.
"""
from __future__ import annotations
import csv,re,json,time
from collections import defaultdict
from pathlib import Path
from sage.all import QQ, PolynomialRing, sage_eval
from ore_algebra import OreAlgebra

ROOT=Path(__file__).resolve().parents[3]
MANIFEST=ROOT/"semantic_v2"/"40_execution"/"combined"/"20260819__NZSCCM__CASE21__R13__FULL_THREE_BRANCH_SPLINE_GKZ_COLUMN_MANIFEST.csv"
FACTOR=re.compile(r"^([A-Za-z_][A-Za-z0-9_]*)(?:\^([0-9]+))?$")
DECIMAL=re.compile(r"(?<![A-Za-z0-9_.])(\d+)\.(\d+)(?![A-Za-z0-9_.])")
PHYSICAL=["r","s","u"]
PARAMS=["D","M","B","al","eta","xcr","kappa","rho","HR","UR","acc","at"]
RADICALS=["w","Del","Sig","absdetX1","sigAbsX1","absdetX10","sigAbsX10"]

def exact_decimal_text(s):
    def repl(m):
        a,b=m.group(1),m.group(2)
        if set(b)=={"0"}: return a
        n=int(a+b); d=10**len(b)
        from math import gcd
        g=gcd(n,d);return f"({n//g}/{d//g})"
    return DECIMAL.sub(repl,s)

def parse_mon(text):
    text=text.strip()
    if text=="1":return {}
    out={}
    for f in text.split("*"):
        m=FACTOR.match(f.strip())
        if not m:raise ValueError((text,f))
        out[m.group(1)]=out.get(m.group(1),0)+(int(m.group(2)) if m.group(2) else 1)
    return out

def main():
    t0=time.time()
    with MANIFEST.open(newline="",encoding="utf-8") as f:rows=list(csv.DictReader(f))
    byeq=defaultdict(list)
    for row in rows:
        x=dict(row);x["exp"]=parse_mon(x["monomial"]);byeq[int(x["equation_index"])].append(x)
    known=set(PHYSICAL);outvar={}
    for i in range(112):
        vv=set().union(*(set(t["exp"]) for t in byeq[i]));new=sorted(vv-known)
        if len(new)!=1:raise RuntimeError(("topology",i,new))
        outvar[i]=new[0];known.add(new[0])

    # C = Q(s,u,D,M,B,al,...); F0=C(r).
    other=[x for x in PHYSICAL+PARAMS if x!="r"]
    CP=PolynomialRing(QQ,names=other); cgens=CP.gens_dict(); C=CP.fraction_field()
    R=PolynomialRing(C,'r'); r=R.gen(); F=R.fraction_field()
    env={"r":F(r)}
    for n in other: env[n]=F(C(cgens[n]))
    K=F

    def coeff(text):
        loc={k:env[k] for k in PARAMS if k in env}
        return K(sage_eval(exact_decimal_text(text),locals=loc))
    def mono(term,skip=None):
        z=K(coeff(term["coefficient"]))
        for n,p in term["exp"].items():
            if n==skip:continue
            z*=env[n]**p
        return z

    stage=[]
    for i in range(112):
        y=outvar[i]; terms=byeq[i]
        b=K(0);outs=[]
        for term in terms:
            p=term["exp"].get(y,0)
            if p:outs.append((term,p))
            else:b+=mono(term)
        if y in RADICALS:
            if len(outs)!=1 or outs[0][1]!=2:raise RuntimeError(("radical",i,y,outs))
            a=mono(outs[0][0],skip=y); rad=-b/a
            P=PolynomialRing(K,'_Y'); Y=P.gen(); poly=Y**2-rad
            Knew=K.extension(poly,names=(y,))
            # exact coercion of all previous straight-line circuit values
            env={n:Knew(v) for n,v in env.items()};K=Knew;env[y]=K.gen()
            stage.append({"radical":y,"equation":i,"elapsed_s":time.time()-t0})
        else:
            a=K(0)
            for term,p in outs:
                if p!=1:raise RuntimeError(("nonlinear",i,y,p))
                a+=mono(term,skip=y)
            env[y]=-b/a
        if i in (38,48,84,111):
            stage.append({"equation":i,"output":y,"elapsed_s":time.time()-t0})

    syy=env["Syy"]
    build_elapsed=time.time()-t0
    A=OreAlgebra(R,'Dr');Dr=A.gen()
    # Identity function f(x)=x is annihilated by x D_x -1; composition f(Syy(r))=Syy(r).
    L=(r*Dr-1).annihilator_of_composition(syy)
    elapsed=time.time()-t0
    report={
      "identity":"NZSCCM_Z1_R15_R13_SAGE_NESTED_TOWER_ANNIHILATOR_R",
      "governance":{"spatial_sampling":0,"spatial_quadrature":0,"material_points":0,"finite_prefix":0},
      "radical_count":7,
      "active_variable":"r",
      "coefficient_parameters":other,
      "circuit_build_seconds":build_elapsed,
      "total_seconds":elapsed,
      "annihilator_order":int(L.order()),
      "annihilator_degree":int(L.degree()),
      "annihilator":str(L),
      "stages":stage,
      "status":"PASS"
    }
    print(json.dumps(report,indent=2,ensure_ascii=False))

if __name__=="__main__":main()
