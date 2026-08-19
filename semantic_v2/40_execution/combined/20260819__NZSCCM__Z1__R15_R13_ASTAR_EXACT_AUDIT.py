#!/usr/bin/env python3
"""NZ-SCCM Z1 — R15/R13 exact A* audit; exact algebra only, zero discretization."""
from __future__ import annotations
import csv, hashlib, json, re
from pathlib import Path
import sympy as sp
from sympy.polys.domains import ZZ
from sympy.polys.matrices import DomainMatrix

REPO = Path(__file__).resolve().parents[3]
MANIFEST = REPO / "semantic_v2" / "40_execution" / "combined" / "20260819__NZSCCM__CASE21__R13__FULL_THREE_BRANCH_SPLINE_GKZ_COLUMN_MANIFEST.csv"
EXPECTED = {"equations":112,"variables":115,"rows":227,"columns":403}
FACTOR = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*)(?:\^([0-9]+))?$")

def parse_monomial(text):
    text=text.strip()
    if text=="1": return {}
    out={}
    for factor in text.split("*"):
        m=FACTOR.match(factor.strip())
        if not m: raise ValueError(f"unsupported monomial factor {factor!r} in {text!r}")
        name,power=m.group(1),m.group(2)
        out[name]=out.get(name,0)+(int(power) if power else 1)
    return out

def z1_locals():
    D,q,al=sp.symbols("D q al", real=True)
    eps0=sp.Rational("0.0018712490394580678")
    rho=sp.Rational(1,10)
    kappa=sp.Rational("2.0005129533678754")
    HR=sp.Rational("0.09799750427197301")
    UR=sp.Rational(3,100)
    xcr=rho/kappa
    eta=xcr/20
    M=sp.pi**2/eps0*(sp.Rational(1,250)*q+q**2/2)
    B=sp.pi**2*sp.Integer(92)*q/(2*eps0*sp.Integer(6000))
    return {
        "D":D,"q":q,"al":al,"M":M,"B":B,"rho":rho,"kappa":kappa,
        "HR":HR,"UR":UR,"xcr":xcr,"eta":eta,
        "acc":sp.Rational("0.1072329249362415"),
        "at":1-2**sp.Rational(-1,8),"Rational":sp.Rational,"pi":sp.pi,
    }

def main():
    with MANIFEST.open(newline="",encoding="utf-8") as f:
        records=list(csv.DictReader(f))
    assert len(records)==EXPECTED["columns"], (len(records),EXPECTED["columns"])
    eqids=sorted({int(r["equation_index"]) for r in records})
    assert eqids==list(range(EXPECTED["equations"]))
    parsed=[parse_monomial(r["monomial"]) for r in records]

    variables=[]; seen=set()
    for mon in parsed:
        for v in mon:
            if v not in seen: seen.add(v); variables.append(v)
    assert len(variables)==EXPECTED["variables"], (len(variables),variables)
    vind={v:i for i,v in enumerate(variables)}

    rowdicts=[{} for _ in range(EXPECTED["rows"])]
    for j,(rec,mon) in enumerate(zip(records,parsed)):
        rowdicts[int(rec["equation_index"])][j]=1
        for v,p in mon.items(): rowdicts[EXPECTED["equations"]+vind[v]][j]=int(p)
    A=DomainMatrix({i:d for i,d in enumerate(rowdicts) if d},(EXPECTED["rows"],EXPECTED["columns"]),ZZ)
    rank=int(A.to_field().rank())
    nullity=EXPECTED["columns"]-rank

    canon="\n".join(f"{int(rec['equation_index'])};"+",".join(f"{v}^{mon[v]}" for v in sorted(mon)) for rec,mon in zip(records,parsed))+"\n"
    support_sha=hashlib.sha256(canon.encode()).hexdigest()

    loc=z1_locals(); zero_cols=[]; parse_fail=[]
    decimal=re.compile(r"(?<![A-Za-z0-9_])(\d+\.\d+)(?![A-Za-z0-9_])")
    for rec in records:
        raw=rec["coefficient"].strip()
        raw_exact=decimal.sub(lambda m:f"Rational('{m.group(1)}')",raw)
        try:
            expr=sp.simplify(sp.sympify(raw_exact,locals=loc))
            if expr==0: zero_cols.append(rec["column"])
        except Exception as exc:
            parse_fail.append({"column":rec["column"],"coefficient":raw,"error":str(exc)})

    r13=[r for r in records if r["source"]=="R13"]
    r13eq=sorted({int(r["equation_index"]) for r in r13})
    report={
      "identity":"NZSCCM_Z1_R15_R13_EXACT_ASTAR_AUDIT",
      "governance":{"spatial_sampling":0,"spatial_quadrature":0,"material_points":0,"finite_prefix":0,"numerical_ode_stepping":0,"arithmetic":"exact integer/rational/symbolic only"},
      "manifest":str(MANIFEST.relative_to(REPO)),
      "counts":{"equations":len(eqids),"variables":len(variables),"cayley_rows":A.shape[0],"cayley_columns":A.shape[1],"r13_added_columns":len(r13),"r13_equation_range":[min(r13eq),max(r13eq)]},
      "exact_linear_algebra":{"rank_Q":rank,"nullity_Q":nullity,"full_row_rank":rank==A.shape[0],"canonical_support_sha256":support_sha},
      "z1_concrete_specialization":{"a_phys_mm":12000,"b_mm":6000,"tc_mm":92,"k":1,"nu_R10":"9/50","q0":"1/250","M_of_q":str(loc["M"]),"B_of_q":str(loc["B"]),"generic_identically_zero_manifest_columns":zero_cols,"generic_support_preserved":len(zero_cols)==0,"coefficient_parse_failures":parse_fail},
      "status":{"R13_ASTAR_RECONSTRUCTION":"PASS","Z1_CONCRETE_SHARED_SUPPORT":"PASS" if not zero_cols and not parse_fail else "FAIL","FULL_PHYSICAL_RELATIVE_GKZ_EVALUATOR":"NOT_YET_INSTANTIATED"}
    }
    print(json.dumps(report,indent=2,ensure_ascii=False))

if __name__=="__main__": main()
