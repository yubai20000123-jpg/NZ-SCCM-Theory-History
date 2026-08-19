# NZ-SCCM CURRENT STATE — R15 single-file full from-zero calculation ledger

**Date:** 2026-08-19  
**Status:** `R15_FULL_FROM_ZERO_CALCULATION_LEDGER = ACTIVE`

## Canonical execution ledger

`../20_theory/20260819__NZSCCM__R15_FULL_FROM_ZERO_CALCULATION_LEDGER_CASE21_Z6.md`

## Scope

R15 consolidates the active theory into one file that is sufficient as the sole theory/input source for an independent zero-discretization Case21 or Z6 re-execution:

```text
raw specimen parameters
-> Dx,Dy,H
-> physical controlling halfwave
-> continuous Nguyen/von-Karman kinematics
-> finite global current material constructors
-> continuous P,Rq,Ralpha
-> same-source Jlim
-> direct solve Rq=0, Ralpha=0, det(Jlim)=0
-> Pu
```

## Key corrections incorporated

```text
Case21 physical a = 2440 mm, b = 1220 mm, m_phys = 2, ell = 1220 mm
historical a=b=ell=1220 notation = representative-halfwave coordinates only

material true-infinite series layer = removed
R10 three-branch law = exact finite global spline
Z6 face radial cap = exact finite global algebraic cap
Z6 web ideal EP = exact finite global clip
uniform q=alpha=0 stationary load = explicitly rejected as Pu
```

## Zero-discretization governance

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
N_formal_material_points = 0
DISCRETE_AUDIT_ORACLE = PROHIBITED
FINITE_PREFIX_CONVERGENCE_AS_EVIDENCE = PROHIBITED
```

## Evidence identity

R15 is a **complete from-zero calculation specification / single-file ledger**.

It does not claim that this chat has independently re-solved the full nonuniform Case21/Z6 roots using a new CAS backend. The released roots are placed only in the sealed regression-target section and must not be used during blind execution.

## Next execution

Give an independent executor only R15 Sections 0–10, hide the sealed target section, and require direct zero-discretization solution of the full `(D,q,alpha)` limit system. Unseal the regression targets only after the independent result is frozen.
