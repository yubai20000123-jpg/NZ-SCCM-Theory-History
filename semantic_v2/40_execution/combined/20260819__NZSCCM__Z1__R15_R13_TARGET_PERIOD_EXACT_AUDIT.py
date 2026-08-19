#!/usr/bin/env python3
"""
NZ-SCCM Z1 — exact target-period reconstruction from the R13 sparse circuit.
No quadrature, no sampling, no numerical ODE, no finite truncation.

Goal: go beyond A* support and reconstruct the exact triangular multi-residue
integral data for the concrete P target: auxiliary outputs, residue Jacobian
monomial, denominator exponents, and physical relative cycle.
"""
from __future__ import annotations
import csv, json, re
from collections import defaultdict
from pathlib import Path

REPO=Path(__file__).resolve().parents[3]
MANIFEST=REPO/"semantic_v2"/"40_execution"/"combined"/"20260819__NZSCCM__CASE21__R13__FULL_THREE_BRANCH_SPLINE_GKZ_COLUMN_MANIFEST.csv"
FACTOR=re.compile(r"^([A-Za-z_][A-Za-z0-9_]*)(?:\^([0-9]+))?$")

def mon(text):
    text=text.strip()
    if text=="1": return {}
    out={}
    for f in text.split("*"):
        m=FACTOR.match(f.strip())
        if not m: raise ValueError((text,f))
        v,p=m.group(1),m.group(2)
        out[v]=out.get(v,0)+(int(p) if p else 1)
    return out

def fmt_monomial(exp):
    items=[]
    for v in sorted(exp):
        p=exp[v]
        if p: items.append(v if p==1 else f"{v}^{p}")
    return "1" if not items else "*".join(items)

def main():
    with MANIFEST.open(newline="",encoding="utf-8") as f:
        rows=list(csv.DictReader(f))
    byeq=defaultdict(list)
    for r in rows:
        r=dict(r); r["exp"]=mon(r["monomial"]); byeq[int(r["equation_index"])].append(r)

    physical=["r","s","u"]
    known=set(physical)
    outputs=[]
    triangular_fail=[]
    diagonal=[]
    jac_exp=defaultdict(int)
    square_root_outputs=[]

    for i in range(112):
        vars_i=set()
        for term in byeq[i]: vars_i.update(term["exp"])
        new=sorted(vars_i-known)
        if len(new)!=1:
            triangular_fail.append({"equation":i,"new_variables":new,"known_count":len(known)})
            continue
        out=new[0]
        outputs.append(out)
        terms_with=[t for t in byeq[i] if t["exp"].get(out,0)>0]
        degree=max(t["exp"].get(out,0) for t in terms_with)
        if degree==2: square_root_outputs.append(out)
        # diagonal derivative dG_i/d(out): exact term-level derivative
        deriv=[]
        for t in terms_with:
            p=t["exp"][out]
            e=dict(t["exp"]); e[out]-=1
            if e[out]==0: e.pop(out)
            deriv.append({"coefficient":t["coefficient"],"integer_factor":p,"exp":e})
        if len(deriv)!=1:
            diagonal.append({"equation":i,"output":out,"monomial_diagonal":False,"terms":len(deriv)})
        else:
            d=deriv[0]
            for v,p in d["exp"].items(): jac_exp[v]+=p
            diagonal.append({"equation":i,"output":out,"degree":degree,"monomial_diagonal":True,"coefficient":d["coefficient"],"integer_factor":d["integer_factor"],"diagonal_monomial":fmt_monomial(d["exp"])})
        known.add(out)

    # P_c after zeta=2u-1 has integrand Syy/w dr ds du.  The Grothendieck
    # residue lift multiplies by det(dG/dy), y = 112 auxiliary outputs.
    numerator_exp=dict(jac_exp)
    numerator_exp["Syy"]=numerator_exp.get("Syy",0)+1
    numerator_exp["w"]=numerator_exp.get("w",0)-1
    numerator_exp={k:v for k,v in numerator_exp.items() if v}

    # Every circuit constraint occurs with denominator power one in the iterated
    # residue lift. This is the raw generalized-Euler exponent data before any
    # sign convention is imposed for a particular GKZ software package.
    gamma=[1]*112

    # Positive-real branch selectors for all quadratic output relations.  These
    # are not spatial cells: they select the intended algebraic sheet.
    positive_branch_names={
        "w","Del","Sig",
        "absdetX1","sigAbsX1","absdetX10","sigAbsX10"
    }
    unclassified_quadratic=[v for v in square_root_outputs if v not in positive_branch_names]

    report={
      "identity":"NZSCCM_Z1_R15_R13_TARGET_PERIOD_EXACT_AUDIT",
      "governance":{"spatial_sampling":0,"spatial_quadrature":0,"material_points":0,"finite_prefix":0,"numerical_ode_stepping":0},
      "triangular_residue_lift":{
        "physical_variables":physical,
        "auxiliary_equations":112,
        "auxiliary_outputs":len(outputs),
        "all_115_variables_accounted_for":len(known)==115,
        "triangular_failures":triangular_fail,
        "all_diagonal_derivatives_monomial":all(d.get("monomial_diagonal",False) for d in diagonal),
        "square_root_outputs":square_root_outputs,
        "unclassified_quadratic_outputs":unclassified_quadratic
      },
      "raw_generalized_euler_residue_data_for_Pc":{
        "denominator_powers_gamma_length":len(gamma),
        "denominator_powers_gamma_unique":sorted(set(gamma)),
        "residue_jacobian_monomial":fmt_monomial(dict(jac_exp)),
        "Pc_residue_numerator_monomial":fmt_monomial(numerator_exp),
        "Pc_residue_numerator_exponents":dict(sorted(numerator_exp.items())),
        "physical_factor_after_zeta_to_u":"Pc = -(fc*b*tc/pi^2) * relative-residue-period",
        "physical_relative_chain":"[0,1]_r x [0,1]_s x [0,1]_u x product(small positive-sheet residue loops for 112 auxiliary outputs)"
      },
      "branch_sheet":{
        "positive_quadratic_generators":sorted(positive_branch_names),
        "rule":"select positive real algebraic sheet continuously from the physical interior; no spatial subdivision"
      },
      "status":{
        "TRIANGULAR_MULTIRESIDUE_DATA":"PASS" if not triangular_fail else "FAIL",
        "MONOMIAL_RESIDUE_JACOBIAN":"PASS" if all(d.get("monomial_diagonal",False) for d in diagonal) else "FAIL",
        "RAW_A_GAMMA_MU_RELATIVE_CYCLE":"CONSTRUCTED" if not triangular_fail and not unclassified_quadratic else "PARTIAL",
        "SOFTWARE_CONVENTION_GKZ_BETA":"NOT_YET_FIXED",
        "TAU_PULLBACK_HOLONOMIC_OPERATOR":"NOT_YET_GENERATED"
      },
      "diagonal_derivatives":diagonal
    }
    print(json.dumps(report,indent=2,ensure_ascii=False))

if __name__=="__main__": main()
