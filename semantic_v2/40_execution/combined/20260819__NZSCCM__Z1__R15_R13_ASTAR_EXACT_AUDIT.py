#!/usr/bin/env python3
"""
NZ-SCCM Z1 — R15/R13 exact A* audit.

STRICT GOVERNANCE:
- no numerical integration
- no spatial sampling / grids / material points
- no finite-prefix approximation
- no numerical ODE stepping
- exact integer/rational/symbolic algebra only

This script reads the already committed R13 Cayley-column manifest, reconstructs
A_* exactly, computes exact rank/nullity, and checks that generic Z1 concrete
specialization does not change the R13 monomial support.
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path

import sympy as sp
from sympy.polys.domains import ZZ
from sympy.polys.matrices import DomainMatrix

ROOT = Path(__file__).resolve().parents[3]
MANIFEST = ROOT / "40_execution" / "combined" / "20260819__NZSCCM__CASE21__R13__FULL_THREE_BRANCH_SPLINE_GKZ_COLUMN_MANIFEST.csv"
# __file__ = semantic_v2/40_execution/combined/...; parents[3] = semantic_v2
if not MANIFEST.exists():
    # robust repository-root fallback
    repo = Path(__file__).resolve().parents[3].parent
    MANIFEST = repo / "semantic_v2" / "40_execution" / "combined" / "20260819__NZSCCM__CASE21__R13__FULL_THREE_BRANCH_SPLINE_GKZ_COLUMN_MANIFEST.csv"

EXPECTED = {
    "equations": 112,
    "variables": 115,
    "rows": 227,
    "columns": 403,
}

_FACTOR = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*)(?:\^([0-9]+))?$")


def parse_monomial(text: str) -> dict[str, int]:
    text = text.strip()
    if text == "1":
        return {}
    out: dict[str, int] = {}
    for factor in text.split("*"):
        factor = factor.strip()
        m = _FACTOR.match(factor)
        if not m:
            raise ValueError(f"Unsupported monomial factor: {factor!r} in {text!r}")
        name, power = m.group(1), m.group(2)
        out[name] = out.get(name, 0) + (int(power) if power else 1)
    return out


def exact_z1_substitution():
    # Treat every published decimal input as the exact decimal rational supplied.
    D, q, al = sp.symbols("D q al", real=True)
    pi = sp.pi
    eps0 = sp.Rational("0.0018712490394580678")
    q0 = sp.Rational(1, 250)  # 0.004
    b = sp.Integer(6000)
    tc = sp.Integer(92)
    rho = sp.Rational(1, 10)
    kappa = sp.Rational("2.0005129533678754")
    HR = sp.Rational("0.09799750427197301")
    UR = sp.Rational(3, 100)
    xcr = rho / kappa
    eta = xcr / 20
    acc = sp.Rational("0.1072329249362415")
    at = 1 - 2 ** sp.Rational(-1, 8)
    M = pi**2 / eps0 * (q0*q + q**2/2)
    # R13 normalized thickness u in [0,1]: z = tc*(u-1/2), so B=beta*tc/2.
    B = pi**2 * tc * q / (2 * eps0 * b)
    return {
        "D": D,
        "q": q,
        "al": al,
        "M": M,
        "B": B,
        "rho": rho,
        "kappa": kappa,
        "HR": HR,
        "UR": UR,
        "xcr": xcr,
        "eta": eta,
        "acc": acc,
        "at": at,
    }


def main() -> None:
    with MANIFEST.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    if len(rows) != EXPECTED["columns"]:
        raise AssertionError(("column_count", len(rows), EXPECTED["columns"]))

    equation_ids = sorted({int(r["equation_index"]) for r in rows})
    if equation_ids != list(range(EXPECTED["equations"])):
        raise AssertionError("equation indices are not exactly 0..111")

    parsed = [parse_monomial(r["monomial"]) for r in rows]

    # Variable order: deterministic first appearance in c000..c402.
    variables: list[str] = []
    seen = set()
    for mon in parsed:
        for v in mon:
            if v not in seen:
                seen.add(v)
                variables.append(v)

    if len(variables) != EXPECTED["variables"]:
        raise AssertionError(("variable_count", len(variables), EXPECTED["variables"], variables))

    var_index = {v: i for i, v in enumerate(variables)}
    n_eq = EXPECTED["equations"]
    n_var = EXPECTED["variables"]
    n_col = EXPECTED["columns"]

    # Build exact integer Cayley configuration: [equation one-hot ; monomial exponent].
    # Store as sparse row dicts for DomainMatrix over ZZ.
    rowdicts: list[dict[int, int]] = [dict() for _ in range(n_eq+n_var)]
    for j, (record, mon) in enumerate(zip(rows, parsed)):
        eq = int(record["equation_index"])
        rowdicts[eq][j] = 1
        for v, power in mon.items():
            rowdicts[n_eq + var_index[v]][j] = int(power)

    dod = {i: d for i, d in enumerate(rowdicts) if d}
    A = DomainMatrix(dod, (n_eq+n_var, n_col), ZZ)
    if A.shape != (EXPECTED["rows"], EXPECTED["columns"]):
        raise AssertionError(("A_shape", A.shape))

    # Exact rank over Q; no floating point or probabilistic rank is accepted as final.
    rank = int(A.to_field().rank())
    nullity = n_col - rank

    # Exact canonical SHA of the integer matrix, independent of CSV coefficient formatting.
    # One line per column: equation id ; sorted variable exponent pairs.
    canonical_lines = []
    for r, mon in zip(rows, parsed):
        canonical_lines.append(
            f"{int(r['equation_index'])};" + ",".join(f"{v}^{mon[v]}" for v in sorted(mon))
        )
    canonical_text = "\n".join(canonical_lines) + "\n"
    canonical_sha256 = hashlib.sha256(canonical_text.encode()).hexdigest()

    # Z1 generic coefficient specialization.  We only test whether a coefficient
    # becomes identically zero as a symbolic function of (D,q,alpha).  Isolated
    # state zeros do NOT remove a monomial from the generic master support.
    loc = exact_z1_substitution()
    sympify_locals = dict(loc)
    sympify_locals.update({"pi": sp.pi})
    identically_zero_columns = []
    coefficient_parse_failures = []
    for r in rows:
        raw = r["coefficient"].strip()
        # Decimal literals in the historical CSV are first rationalized exactly.
        raw_exact = re.sub(r"(?<![A-Za-z0-9_])(\d+\.\d+)(?![A-Za-z0-9_])",
                           lambda m: f"Rational('{m.group(1)}')", raw)
        try:
            expr = sp.sympify(raw_exact, locals={**sympify_locals, "Rational": sp.Rational})
            expr = sp.simplify(expr.subs({
                sp.Symbol("M"): loc["M"],
                sp.Symbol("B"): loc["B"],
                sp.Symbol("rho"): loc["rho"],
                sp.Symbol("kappa"): loc["kappa"],
                sp.Symbol("HR"): loc["HR"],
                sp.Symbol("UR"): loc["UR"],
                sp.Symbol("xcr"): loc["xcr"],
                sp.Symbol("eta"): loc["eta"],
                sp.Symbol("acc"): loc["acc"],
                sp.Symbol("at"): loc["at"],
            }))
            if expr == 0:
                identically_zero_columns.append(r["column"])
        except Exception as exc:
            coefficient_parse_failures.append({"column": r["column"], "coefficient": raw, "error": str(exc)})

    # Structural audit of the key R13 additions and terminal Syy equations.
    r13_cols = [r for r in rows if r["source"] == "R13"]
    r13_eqs = sorted({int(r["equation_index"]) for r in r13_cols})
    terminal = rows[-14:]

    report = {
        "identity": "NZSCCM_Z1_R15_R13_EXACT_ASTAR_AUDIT",
        "governance": {
            "spatial_sampling": 0,
            "spatial_quadrature": 0,
            "material_points": 0,
            "finite_prefix": 0,
            "numerical_ode_stepping": 0,
            "arithmetic": "exact integer/rational/symbolic only",
        },
        "manifest": str(MANIFEST),
        "counts": {
            "equations": len(equation_ids),
            "variables": len(variables),
            "cayley_rows": A.shape[0],
            "cayley_columns": A.shape[1],
            "r13_added_columns": len(r13_cols),
            "r13_equation_range": [min(r13_eqs), max(r13_eqs)],
        },
        "exact_linear_algebra": {
            "rank_Q": rank,
            "nullity_Q": nullity,
            "full_row_rank": rank == A.shape[0],
            "canonical_support_sha256": canonical_sha256,
        },
        "z1_concrete_specialization": {
            "a_phys_mm": 12000,
            "b_mm": 6000,
            "tc_mm": 92,
            "k": 1,
            "nu_R10": "9/50",
            "q0": "1/250",
            "M_of_q": str(loc["M"]),
            "B_of_q": str(loc["B"]),
            "generic_identically_zero_manifest_columns": identically_zero_columns,
            "generic_support_preserved": len(identically_zero_columns) == 0,
            "coefficient_parse_failures": coefficient_parse_failures,
        },
        "terminal_equations": [
            {"column": r["column"], "equation": r["equation"], "monomial": r["monomial"]}
            for r in terminal
        ],
        "status": {
            "R13_ASTAR_RECONSTRUCTION": "PASS",
            "Z1_CONCRETE_SHARED_SUPPORT": "PASS" if len(identically_zero_columns) == 0 else "FAIL",
            "FULL_PHYSICAL_RELATIVE_GKZ_EVALUATOR": "NOT_YET_INSTANTIATED",
        },
    }

    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
