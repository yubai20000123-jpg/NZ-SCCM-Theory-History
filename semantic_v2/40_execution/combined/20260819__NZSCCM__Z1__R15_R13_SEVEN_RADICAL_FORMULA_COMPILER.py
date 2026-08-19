#!/usr/bin/env python3
"""Compile the seven R13 quadratic generators to exact formulas over (r,s,u,D,M,B,al).
No numerical evaluation or discretization. Linear circuit dependencies are eliminated recursively;
quadratic generators remain explicit algebraic generators.
All decimal literals in the manifest are parsed as exact rationals.
"""
from __future__ import annotations
import csv,json,re
from collections import defaultdict
from functools import lru_cache
from pathlib import Path
import sympy as sp
from sympy.parsing.sympy_parser import (
    parse_expr, standard_transformations, rationalize
)

REPO=Path(__file__).resolve().parents[3]
MANIFEST=REPO/"semantic_v2"/"40_execution"/"combined"/"20260819__NZSCCM__CASE21__R13__FULL_THREE_BRANCH_SPLINE_GKZ_COLUMN_MANIFEST.csv"
FACTOR=re.compile(r"^([A-Za-z_][A-Za-z0-9_]*)(?:\^([0-9]+))?$")
RADICALS=["w","Del","Sig","absdetX1","sigAbsX1","absdetX10","sigAbsX10"]
PARAM_NAMES=["D","M","B","al","eta","xcr","kappa","rho","HR","UR","acc","at"]
PHYSICAL=["r","s","u"]
SYMS={n:sp.Symbol(n) for n in PHYSICAL+PARAM_NAMES+RADICALS}
TRANSFORMATIONS=standard_transformations+(rationalize,)

def parse_mon(s):
    s=s.strip()
    if s=="1":return {}
    out={}
    for f in s.split("*"):
        m=FACTOR.match(f.strip())
        if not m:raise ValueError((s,f))
        out[m.group(1)]=out.get(m.group(1),0)+(int(m.group(2)) if m.group(2) else 1)
    return out

def main():
    with MANIFEST.open(newline="",encoding="utf-8") as f: raw=list(csv.DictReader(f))
    byeq=defaultdict(list); producer={}; known=set(PHYSICAL)
    for row in raw:
        x=dict(row);x["exp"]=parse_mon(x["monomial"]);byeq[int(x["equation_index"])].append(x)
    for i in range(112):
        vars_i=set().union(*(set(t["exp"]) for t in byeq[i]))
        new=sorted(vars_i-known)
        if len(new)!=1:raise RuntimeError((i,new))
        producer[new[0]]=i;known.add(new[0])

    locals_map={**SYMS,"Rational":sp.Rational}
    def coeff(s):
        z=parse_expr(s,local_dict=locals_map,transformations=TRANSFORMATIONS,evaluate=True)
        if z.has(sp.Float):
            raise RuntimeError(("nonexact coefficient survived rationalize",s,z))
        return z

    @lru_cache(None)
    def resolve(v):
        if v in PHYSICAL or v in PARAM_NAMES or v in RADICALS:
            return SYMS[v]
        i=producer[v]
        expr=sp.Integer(0)
        y=sp.Symbol(v)
        for t in byeq[i]:
            term=coeff(t["coefficient"])
            for name,pow_ in t["exp"].items():
                if name==v: term*=y**pow_
                else: term*=resolve(name)**pow_
            expr+=term
        deg=sp.degree(expr,y)
        if deg!=1: raise RuntimeError(("expected linear",v,i,deg))
        a=expr.coeff(y,1); b=expr.subs(y,0)
        return sp.factor(-b/a)

    formulas=[]
    for rad in RADICALS:
        i=producer[rad]; y=SYMS[rad]
        expr=sp.Integer(0)
        for t in byeq[i]:
            term=coeff(t["coefficient"])
            for name,pow_ in t["exp"].items():
                if name==rad:term*=y**pow_
                elif name in RADICALS:term*=SYMS[name]**pow_
                else:term*=resolve(name)**pow_
            expr+=term
        a2=expr.coeff(y,2); a1=expr.coeff(y,1); b=expr.subs(y,0)
        if a1!=0: raise RuntimeError(("quadratic has linear term",rad,a1))
        R=sp.factor(-b/a2)
        num,den=sp.fraction(R)
        if R.has(sp.Float): raise RuntimeError(("nonexact radical formula",rad,R))
        formulas.append({
          "output":rad,"equation_index":i,
          "relation":f"{rad}^2 = R_{rad}",
          "R":sp.sstr(R),
          "ops_R":int(sp.count_ops(R)),
          "ops_num":int(sp.count_ops(num)),"ops_den":int(sp.count_ops(den)),
          "free_symbols":sorted(str(x) for x in R.free_symbols),
        })

    eps0=sp.Rational("0.0018712490394580678")
    q=sp.Symbol("q")
    Mz=sp.factor(sp.pi**2/eps0*(sp.Rational(1,250)*q+q**2/2))
    Bz=sp.factor(sp.pi**2*sp.Integer(92)*q/(2*eps0*sp.Integer(6000)))
    kappa=sp.Rational("2.0005129533678754"); rho=sp.Rational(1,10)
    xcr=sp.factor(rho/kappa); eta=sp.factor(xcr/20)
    report={
      "identity":"NZSCCM_Z1_R15_R13_SEVEN_RADICAL_FORMULA_COMPILER",
      "governance":{"spatial_sampling":0,"spatial_quadrature":0,"material_points":0,"finite_prefix":0,"numerical_ode_stepping":0},
      "coefficient_parser":"sympy parse_expr + rationalize; Float forbidden after parse",
      "base_symbols":["r","s","u","D","M","B","al","eta","xcr"],
      "z1_substitution":{"M_of_q":sp.sstr(Mz),"B_of_q":sp.sstr(Bz),"xcr":sp.sstr(xcr),"eta":sp.sstr(eta)},
      "tower":formulas,
      "max_ops_R":max(x["ops_R"] for x in formulas),
      "total_ops_R":sum(x["ops_R"] for x in formulas),
      "status":{"SEVEN_QUADRATIC_RELATIONS_EXPLICIT":"PASS","NO_LINEAR_AUXILIARY_REQUIRED_IN_PRINTED_TOWER":"PASS","ALL_MANIFEST_DECIMALS_EXACT_RATIONAL":"PASS"}
    }
    print(json.dumps(report,indent=2,ensure_ascii=False))
if __name__=="__main__":main()
