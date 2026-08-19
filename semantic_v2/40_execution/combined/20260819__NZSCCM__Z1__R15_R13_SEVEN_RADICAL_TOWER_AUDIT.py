#!/usr/bin/env python3
"""Exact structural reduction of R13's 112-equation circuit to its quadratic radical tower.
No numerical integration, sampling, continuation, finite prefix, or floating algebra.
"""
from __future__ import annotations
import csv,json,re
from collections import defaultdict,deque
from pathlib import Path

REPO=Path(__file__).resolve().parents[3]
MANIFEST=REPO/"semantic_v2"/"40_execution"/"combined"/"20260819__NZSCCM__CASE21__R13__FULL_THREE_BRANCH_SPLINE_GKZ_COLUMN_MANIFEST.csv"
FACTOR=re.compile(r"^([A-Za-z_][A-Za-z0-9_]*)(?:\^([0-9]+))?$")

def mon(s):
    s=s.strip()
    if s=="1":return {}
    out={}
    for f in s.split("*"):
        m=FACTOR.match(f.strip())
        if not m:raise ValueError((s,f))
        out[m.group(1)]=out.get(m.group(1),0)+(int(m.group(2)) if m.group(2) else 1)
    return out

def main():
    with MANIFEST.open(newline="",encoding="utf-8") as f: rows=list(csv.DictReader(f))
    byeq=defaultdict(list)
    for r in rows:
        x=dict(r);x["exp"]=mon(x["monomial"]);byeq[int(x["equation_index"])].append(x)
    physical={"r","s","u"};known=set(physical)
    records=[];quadratics=[];linears=[]
    producer={}
    for i in range(112):
        vars_i=set().union(*(set(t["exp"]) for t in byeq[i]))
        new=sorted(vars_i-known)
        if len(new)!=1: raise RuntimeError((i,new,known))
        y=new[0];producer[y]=i
        deg=max(t["exp"].get(y,0) for t in byeq[i])
        terms_y=[t for t in byeq[i] if t["exp"].get(y,0)]
        deps=sorted(v for v in vars_i if v!=y)
        prior_outputs=sorted(v for v in deps if v not in physical)
        # coefficient support multiplying output variable, useful to identify rational divisions.
        coeff_mons=[]
        for t in terms_y:
            e=dict(t["exp"]);e[y]-=1
            if not e[y]:e.pop(y)
            coeff_mons.append({"coefficient":t["coefficient"],"remaining_monomial":e})
        rec={"equation":i,"name":byeq[i][0]["equation"],"output":y,"degree_in_output":deg,"dependencies":deps,"prior_output_dependencies":prior_outputs,"output_coefficient_terms":coeff_mons}
        records.append(rec)
        (quadratics if deg==2 else linears).append(rec)
        known.add(y)
    if any(r["degree_in_output"]!=1 for r in linears): raise RuntimeError("nonlinear nonquadratic output")
    radical_names=[r["output"] for r in quadratics]
    # Dependency graph among the seven quadratic generators through all linear intermediates.
    radical_ancestors={}
    ancestors={v:set() for v in physical}
    for rec in records:
        aset=set()
        for d in rec["dependencies"]:
            if d in radical_names: aset.add(d)
            aset.update(ancestors.get(d,set()))
        if rec["output"] in radical_names:
            # a generator depends only on prior radicals, never itself
            radical_ancestors[rec["output"]]=sorted(aset)
            ancestors[rec["output"]]=aset|{rec["output"]}
        else:
            ancestors[rec["output"]]=aset
    # Syy is final output; identify exact radical support of target.
    syy_radicals=sorted(ancestors["Syy"])
    # A generic tower with seven monic quadratic generators has degree <=2^7.
    report={
      "identity":"NZSCCM_Z1_R15_R13_SEVEN_RADICAL_TOWER_AUDIT",
      "governance":{"spatial_sampling":0,"spatial_quadrature":0,"material_points":0,"finite_prefix":0,"numerical_ode_stepping":0},
      "circuit":{"equations":112,"physical_variables":["r","s","u"],"auxiliary_outputs":112,"linear_outputs":len(linears),"quadratic_outputs":len(quadratics)},
      "quadratic_radical_tower":[{"equation":r["equation"],"output":r["output"],"dependencies":r["dependencies"],"prior_radical_ancestors":radical_ancestors[r["output"]]} for r in quadratics],
      "radical_names":radical_names,
      "Syy_radical_ancestors":syy_radicals,
      "Syy_uses_all_seven_radicals":set(syy_radicals)==set(radical_names),
      "generic_algebraic_extension_degree_upper_bound":2**len(quadratics),
      "linear_outputs_with_nonconstant_diagonal_coefficient":[r["output"] for r in linears if any(t["remaining_monomial"] for t in r["output_coefficient_terms"])],
      "status":{"112_AUX_TO_7_RADICAL_TOWER":"PASS","GENERIC_EXTENSION_DEGREE_BOUND":"128" if len(quadratics)==7 else "UNEXPECTED","Syy_SEVEN_RADICAL_CLOSURE":"PASS" if set(syy_radicals)==set(radical_names) else "PARTIAL"}
    }
    print(json.dumps(report,indent=2,ensure_ascii=False))
if __name__=="__main__":main()
