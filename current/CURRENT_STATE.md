# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-19  
**Status:** `R15_FULL_FROM_ZERO_CALCULATION_LEDGER = ACTIVE`

## Canonical current-state artifact

`semantic_v2/00_index/20260819__NZSCCM__CURRENT_STATE_R15_FULL_FROM_ZERO_CALCULATION_LEDGER__INDEX.md`

## Canonical single-file ledger

`semantic_v2/20_theory/20260819__NZSCCM__R15_FULL_FROM_ZERO_CALCULATION_LEDGER_CASE21_Z6.md`

R15 consolidates the active Case21/Z6 theory into one zero-discretization from-zero execution specification:

```text
raw specimen parameters
-> Dx,Dy,H
-> physical controlling halfwave
-> continuous Nguyen/von-Karman kinematics
-> finite global material constructors
-> continuous P,Rq,Ralpha + same-source derivatives
-> direct solve Rq=0, Ralpha=0, det(Jlim)=0
-> Pu
```

## Mandatory governance

```text
ZERO_DISCRETIZATION_DEFAULT = LOCKED
DISCRETE_AUDIT_ORACLE = PROHIBITED
FINITE_PREFIX_CONVERGENCE_AS_EVIDENCE = PROHIBITED
TASK_LOCAL_DISCRETIZATION_EXCEPTION_ONLY = TRUE
AUTO_GITHUB_CHECKPOINT_AFTER_MATERIAL_CHANGE = REQUIRED
PROACTIVE_CHAT_LENGTH_CHECKPOINT = REQUIRED
```

## Key R15 corrections

```text
Case21 raw physical geometry: a_phys=2440 mm, b=1220 mm
physical controlling mode: m_phys=2 -> ell=1220 mm
historical a=b=ell=1220 notation = already-reduced representative-halfwave coordinates

material true-infinite series layer = removed
R10 three-branch law = finite global matrix spline
Z6 face radial cap = finite global algebraic cap
Z6 web ideal EP = finite global algebraic clip
uniform q=alpha=0 stationary load = rejected as Pu
```

## Evidence identity

R15 is the current **complete from-zero calculation specification / single-file ledger**. It is intended to be sufficient as the only theory/input document for an independent execution.

The released Case21/Z6 roots and Pu values are included only in a `SEALED REGRESSION TARGETS` section. They must not be used as solve inputs, seed tuning, parameter calibration, or root-selection criteria during a blind re-execution.

R15 does **not** claim that this chat has independently re-solved the full nonuniform roots using a new CAS backend. That independent blind re-execution is the next verification step.

## Formal discretization counters

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
N_formal_material_points = 0
```

No new theory gate is introduced by R15.
