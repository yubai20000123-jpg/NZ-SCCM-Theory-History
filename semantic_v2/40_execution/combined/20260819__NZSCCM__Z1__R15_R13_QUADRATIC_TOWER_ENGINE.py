#!/usr/bin/env python3
"""Exact recursive quadratic-tower executor for the full R13 112-equation circuit.

Purpose: execute the complete finite R13 current-material circuit as an algebraic
field element, not by spatial sampling/quadrature and not by material prefixes.
The base field remains symbolic in (r,s,u,D,M,B,al, material constants).

Representation:
  K0 = Q(r,s,u,D,M,B,al,eta,xcr,kappa,rho,HR,UR,acc,at)
  Ki = K_{i-1}[yi]/(yi^2-Ri), i=1..7.
An element of Ki is represented recursively as a + b*yi.
"""
from __future__ import annotations
import csv, json, re
from dataclasses import dataclass
from pathlib import Path
from collections import defaultdict
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, rationalize

ROOT=Path(__file__).resolve().parents[3]
MANIFEST=ROOT/"semantic_v2"/"40_execution"/"combined"/"20260819__NZSCCM__CASE21__R13__FULL_THREE_BRANCH_SPLINE_GKZ_COLUMN_MANIFEST.csv"
TRANS=standard_transformations+(rationalize,)
FACTOR=re.compile(r"^([A-Za-z_][A-Za-z0-9_]*)(?:\^([0-9]+))?$")
PHYSICAL=["r","s","u"]
PARAMS=["D","M","B","al","eta","xcr","kappa","rho","HR","UR","acc","at"]
RADICALS=["w","Del","Sig","absdetX1","sigAbsX1","absdetX10","sigAbsX10"]
SYMS={n:sp.Symbol(n) for n in PHYSICAL+PARAMS}


def parse_mon(text):
    text=text.strip()
    if text=="1": return {}
    out={}
    for f in text.split("*"):
        m=FACTOR.match(f.strip())
        if not m: raise ValueError((text,f))
        out[m.group(1)]=out.get(m.group(1),0)+(int(m.group(2)) if m.group(2) else 1)
    return out

@dataclass(frozen=True)
class Elt:
    level:int
    data:object

class Tower:
    def __init__(self):
        self.rad_names=[]
        self.rad_R=[]  # R_i stored as Elt at level i-1
        self.max_base_ops=0

    def zero(self, level=0): return Elt(level, sp.Integer(0) if level==0 else (self.zero(level-1),self.zero(level-1)))
    def one(self, level=0): return Elt(level, sp.Integer(1) if level==0 else (self.one(level-1),self.zero(level-1)))
    def base(self,x): return Elt(0,sp.sympify(x))

    def lift(self,a:Elt,to:int)->Elt:
        if a.level>to: raise ValueError((a.level,to))
        while a.level<to:
            a=Elt(a.level+1,(a,self.zero(a.level)))
        return a

    def neg(self,a:Elt)->Elt:
        if a.level==0:return Elt(0,-a.data)
        return Elt(a.level,(self.neg(a.data[0]),self.neg(a.data[1])))

    def add_same(self,a:Elt,b:Elt)->Elt:
        if a.level==0:return Elt(0,a.data+b.data)
        return Elt(a.level,(self.add_same(a.data[0],b.data[0]),self.add_same(a.data[1],b.data[1])))

    def add(self,a:Elt,b:Elt)->Elt:
        n=max(a.level,b.level);return self.add_same(self.lift(a,n),self.lift(b,n))

    def sub(self,a:Elt,b:Elt)->Elt:return self.add(a,self.neg(b))

    def mul_same(self,a:Elt,b:Elt)->Elt:
        n=a.level
        if n==0:
            z=a.data*b.data
            try:self.max_base_ops=max(self.max_base_ops,int(sp.count_ops(z)))
            except Exception:pass
            return Elt(0,z)
        aa,ab=a.data; ba,bb=b.data
        R=self.rad_R[n-1]
        ac=self.mul_same(aa,ba)
        bd=self.mul_same(ab,bb)
        bdR=self.mul_same(bd,R)
        adbc=self.add_same(self.mul_same(aa,bb),self.mul_same(ab,ba))
        return Elt(n,(self.add_same(ac,bdR),adbc))

    def mul(self,a:Elt,b:Elt)->Elt:
        n=max(a.level,b.level);return self.mul_same(self.lift(a,n),self.lift(b,n))

    def inv_same(self,a:Elt)->Elt:
        n=a.level
        if n==0:
            if a.data==0:raise ZeroDivisionError
            return Elt(0,1/a.data)
        aa,bb=a.data; R=self.rad_R[n-1]
        den=self.sub(self.mul_same(aa,aa),self.mul(self.mul_same(bb,bb),R))
        deni=self.inv_same(den)
        return Elt(n,(self.mul_same(aa,deni),self.neg(self.mul_same(bb,deni))))

    def inv(self,a:Elt)->Elt:return self.inv_same(a)
    def div(self,a:Elt,b:Elt)->Elt:return self.mul(a,self.inv(b))

    def pow(self,a:Elt,n:int)->Elt:
        if n<0:return self.pow(self.inv(a),-n)
        out=self.one(a.level);base=a
        while n:
            if n&1:out=self.mul_same(out,base)
            n//=2
            if n:base=self.mul_same(base,base)
        return out

    def extend(self,name:str,R:Elt)->Elt:
        expected=len(self.rad_names)
        if R.level!=expected: R=self.lift(R,expected)
        self.rad_names.append(name);self.rad_R.append(R)
        return Elt(expected+1,(self.zero(expected),self.one(expected)))

    def flatten(self,a:Elt):
        """Return basis coefficients ordered by bitmask 0..2^level-1."""
        if a.level==0:return [a.data]
        lo=self.flatten(a.data[0]);hi=self.flatten(a.data[1]);return lo+hi


def main():
    with MANIFEST.open(newline="",encoding="utf-8") as f: rows=list(csv.DictReader(f))
    byeq=defaultdict(list)
    for row in rows:
        x=dict(row);x["exp"]=parse_mon(x["monomial"]);byeq[int(x["equation_index"])].append(x)

    known=set(PHYSICAL);producer={};outvar={}
    for i in range(112):
        vars_i=set().union(*(set(t["exp"]) for t in byeq[i]))
        new=sorted(vars_i-known)
        if len(new)!=1:raise RuntimeError(("topology",i,new))
        outvar[i]=new[0];producer[new[0]]=i;known.add(new[0])

    local={**SYMS}
    def cparse(s):
        z=parse_expr(s,local_dict=local,transformations=TRANS,evaluate=True)
        if z.has(sp.Float):raise RuntimeError(("float coefficient",s,z))
        return z

    T=Tower(); env={n:Elt(0,SYMS[n]) for n in PHYSICAL+PARAMS}
    rad_data=[]

    def monomial(term,skip=None):
        z=Elt(0,cparse(term["coefficient"]))
        for name,p in term["exp"].items():
            if name==skip:continue
            z=T.mul(z,T.pow(env[name],p))
        return z

    for i in range(112):
        y=outvar[i]; terms=byeq[i]
        out_terms=[];rest=[]
        for term in terms:
            p=term["exp"].get(y,0)
            (out_terms if p else rest).append((term,p))
        if not out_terms:raise RuntimeError(("no output term",i,y))
        b=T.zero(len(T.rad_names))
        for term,_ in rest:b=T.add(b,monomial(term))

        if y in RADICALS:
            # Exact R13 radical relations are y^2 coefficient + b = 0.
            if len(out_terms)!=1 or out_terms[0][1]!=2:raise RuntimeError(("radical form",i,y,out_terms))
            term,_=out_terms[0]
            a=monomial(term,skip=y)
            R=T.neg(T.div(b,a))
            yy=T.extend(y,R);env[y]=yy
            coeffs=T.flatten(R)
            rad_data.append({
                "name":y,"equation":i,"prior_level":R.level,
                "R_basis_support":sum(1 for z in coeffs if z!=0),
                "R_basis_dimension":len(coeffs),
                "R_base_ops_total":sum(int(sp.count_ops(z)) for z in coeffs),
            })
        else:
            # Linear output; if multiple output-containing terms, sum their coefficient.
            a=T.zero(len(T.rad_names))
            for term,p in out_terms:
                if p!=1:raise RuntimeError(("nonlinear nonradical",i,y,p))
                a=T.add(a,monomial(term,skip=y))
            env[y]=T.neg(T.div(b,a))

    syy=env["Syy"]
    flat=T.flatten(syy)
    nz=[(i,z) for i,z in enumerate(flat) if z!=0]
    report={
        "identity":"NZSCCM_Z1_R15_R13_RECURSIVE_QUADRATIC_TOWER_ENGINE",
        "governance":{"spatial_sampling":0,"spatial_quadrature":0,"material_points":0,"finite_prefix":0},
        "base_field":"Q(r,s,u,D,M,B,al,eta,xcr,kappa,rho,HR,UR,acc,at)",
        "radicals":T.rad_names,
        "radical_count":len(T.rad_names),
        "basis_dimension_upper_bound":len(flat),
        "Syy_nonzero_basis_coefficients":len(nz),
        "Syy_basis_masks":[i for i,_ in nz],
        "Syy_base_ops_total":sum(int(sp.count_ops(z)) for _,z in nz),
        "max_intermediate_base_ops":T.max_base_ops,
        "radicand_structure":rad_data,
        "status":{"FULL_112_EQUATION_CIRCUIT_EXECUTED_IN_TOWER":"PASS","Syy_EXACT_TOWER_ELEMENT":"PASS"}
    }
    print(json.dumps(report,indent=2,ensure_ascii=False))

if __name__=="__main__":main()
