# R16–R20 Nguyen N-module Recovery Boundary

**Purpose:** preserve the actual progression of the historical Branch-C numerical route without allowing its later `PASS_READY_FOR_UNIFIED_24_PANEL_BATCH` label to overwrite the subsequent NZ-SCCM zero-spatial/current-operator governance.

## Evidence files in this repository

- `R16/equation_to_code_registry_R16.csv`
- `R17/equation_to_code_registry_R17.csv`
- `R18/equation_to_code_registry_R18.csv`
- `R18/status_R18.json`
- `R18/N模块分支C_来源Newton全局化与首个自然路径审计_R18.md`
- `R19/equation_to_code_registry_R19.csv`
- `R20/equation_to_code_registry_R20.csv`
- `R20/pytest_R20_summary.txt`

Original File Library IDs are registered in `evidence/MASTER_SOURCE_INVENTORY.csv` and recovery registries.

## R16

R16 closed the local-source and material-domain audit much more strongly than earlier stages:

- TT uncracked: 0 independent local unknowns;
- TC uncracked: 1 independent local secant unknown;
- CC uncracked: 2 independent local secant unknowns;
- 24 Swartz material parameter sets scanned over 1056 principal-strain points with zero failures and deterministic repeat;
- 96 natural source paths over `U->TC`, `U->TT`, `U->CC`, `TC->TCX` passed, with max fine/coarse stress difference `5.240386842854213e-7`;
- source transition surfaces were **not smoothed**: finite jumps remained at `U->TC/TT/CC`; `TC->TCX` was continuous.

But the full structural production gate was explicitly:

```text
NOT_EXECUTED_R16
OPEN
```

Therefore:

```text
R16_LOCAL_MATERIAL_SOURCE_AUDIT = PASS
R16_FULL_STRUCTURAL_PRODUCTION  = OPEN
```

## R17

R17 improved source handoff provenance:

- Appendix-B CC pre-crushing event rule passed;
- post-crushing CC peak-secant remap matched independent Appendix-B transcription to <= `1.17e-16`;
- `U->cracked` source handoff was accepted as **source-exact with a finite full-vector jump**, and artificial smoothing was explicitly prohibited;
- `TC->TCX` handoff was continuous to max normalized stress jump `3.68e-16`.

However, the full production gate ended as:

```text
OPEN_ONE_CC_GLOBALIZATION_FAILURE
68 passed, 1 failed
```

The failure was the pre-seeded CC fixed-load Newton line search. Thus R17 was not a production-complete solver.

## R18

R18 did **not** change Nguyen Ch.3 material equations. `materials.py` SHA stayed:

```text
3a8dffd6eeff11f25945af7674fe36fc1432a43cc491d4c6a5ff6fe6f713f97f
```

It added numerical globalization of the **source Newton mapping** without replacing the source tangent by finite differences or another Jacobian.

R18 achieved:

- CC source-Newton globalization: PASS;
- natural global `U->TT`: PASS;
- 71/71 tests + compileall PASS.

But `status_R18.json` explicitly kept open:

- natural global `U->TC`;
- natural global `U->CC`;
- natural global `TC->TCX`;
- real-material nonlinear arc-length;
- full nested gate.

Therefore:

```text
R18_GLOBAL_NESTED_GATE = PARTIAL_PASS
R18_READY_FOR_SWARTZ_24_PANEL = false
```

## R19

R19 closed the remaining zero-state natural global paths and demonstrated a real-material source-event/peak/postpeak arc path under an **exact linear constraint/Galerkin transformation**. It also verified transaction rollback.

But the mandatory unconstrained multi-DOF real-material source-active arc gate remained:

```text
OPEN
```

The exact linearly constrained audit was explicitly not sufficient to promote to production.

## R20

R20 finally demonstrated the unconstrained multi-DOF historical Branch-C audit:

```text
24 global DOFs
16 free DOFs
5 layers
45 material points
15 accepted points
U -> TC event
one discrete peak
two accepted postpeak points
PASS_AUDIT_ONLY
```

The unified R16–R20 regression contract then reported:

```text
75/75 tests
compileall PASS
PASS_READY_FOR_UNIFIED_24_PANEL_BATCH
```

Critically, the same registry also says:

```text
Swartz calculations have not started
```

and identifies the 15-point path as an **audit fixture, not a Swartz specimen**.

## Why R20 is retained but not current production theory

R20 is highly valuable as a **Nguyen-source numerical oracle / historical verification route** because it preserved:

- Ch.3 source-state relations and source tangents;
- Ch.4 Q4/Hermite16 discretization;
- Ch.6 full residual/path structure;
- material-state transaction and rollback;
- natural state transitions;
- peak/postpeak path behavior.

But R20's actual implementation also uses:

```text
5 layers
45 material points
```

and the broader R16–R20 route is a finite-element/material-point/history path. It therefore cannot be silently described as the later formal NZ-SCCM operator satisfying:

```text
N_formal_spatial_sampling   = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
```

Historical identity:

```text
R16_R20_NGUYEN_BRANCH_C = RETAINED_AS_SOURCE_ORACLE_AND_NUMERICAL_AUDIT
R16_R20_NGUYEN_BRANCH_C = NOT_CURRENT_FORMAL_ZERO_SPATIAL_OPERATOR
```

## Non-revival rule

A future conversation may use R16–R20 to answer questions such as:

- What did Nguyen-source TC/TT/CC/TCX transitions do?
- Were source jumps artificially smoothed? (No.)
- Did the historical full residual reach peak and postpeak? (Yes, in R20 audit.)
- How did rollback and source-active arc handling work?
- What source equations were mapped to which code objects?

But it may **not** infer from the R20 `PASS_READY_FOR_UNIFIED_24_PANEL_BATCH` label that:

1. Swartz24 had already been calculated at R20;
2. R20 is the current NZ-SCCM production path;
3. 45 material points satisfy the zero-spatial formal theory;
4. the later current-state operator / moment-first D15 / single-domain governance is obsolete.

Any such promotion requires an explicit later user decision and provenance review.
