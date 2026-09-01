# DEPRECATED — NZ-SCCM 钢壳–UHPC R09 finite-candidate implementation detour

**Date deprecated:** 2026-09-01  
**Branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Production main:** unchanged

This file is intentionally retained as a tombstone. Its original 1162-line content remains recoverable from Git history at commit `9b8b59128d921eea751cfb2574d2322da67c282c`.

## Why deprecated

R09 introduced implementation devices that were not part of the accepted steel-shell–UHPC mechanics:

```text
33 fixed eta nodes
six-point fitted quintic eta candidate
fixed terminal endpoint grids
3x3x3 affine stencils
8 predetermined refinement stages
```

These were added only to remove `root/brentq`; they were not derived from the R02/R04/R06/Airy/UHPC mechanics and therefore must not be treated as formal theory.

The original R06 theory remains the finite-algebraic local-yield definition in

`20260825_1530__NZSCCM__STEEL_SHELL_COMMON_R06_LOCAL_YIELD_RESULTANT_GATE_V1.md`.

## Current replacement

Use:

`20260901__NZSCCM__STEEL_SHELL_UHPC_CENTRAL_TECHNICAL_LEDGER_R11_POLYNOMIAL_UHPC.md`

R10 was an intermediate material simplification and has itself been deprecated because it made UHPC compression elastic-perfectly-plastic and set UHPC tension to zero.

R11 retains the accepted structural calculation chain and uses finite polynomial UHPC material pieces with exact thickness primitives.

```text
R09_FORMAL_STATUS = DEPRECATED_IMPLEMENTATION_DETOUR
33_POINT_ETA = PROHIBITED_AS_FORMAL_THEORY
8_LEVEL_TERMINAL_REFINEMENT = PROHIBITED_AS_FORMAL_THEORY
R10_SIMPLE_MATERIAL = DEPRECATED_OVERSIMPLIFIED_UHPC
CURRENT_TRANSFER_BASELINE = R11_POLYNOMIAL_UHPC
```
