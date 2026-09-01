# DEPRECATED — NZ-SCCM 钢壳–UHPC R09 finite-candidate implementation detour

**Date deprecated:** 2026-09-01  
**Branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Production main:** unchanged

This file is intentionally replaced by a tombstone. Its original 1162-line content remains recoverable from Git history at commit `9b8b59128d921eea751cfb2574d2322da67c282c`.

## Why deprecated

R09 introduced implementation devices that were not part of the previously accepted steel-shell–UHPC theory:

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

`20260901__NZSCCM__STEEL_SHELL_UHPC_CENTRAL_TECHNICAL_LEDGER_R10_SIMPLE_MATERIAL.md`

R10 restores the accepted structural calculation chain and simplifies only the UHPC scalar material law to a piecewise-polynomial design-oriented compression model with zero tensile contribution for the axial capacity terminal.

```text
R09_FORMAL_STATUS = DEPRECATED_IMPLEMENTATION_DETOUR
33_POINT_ETA = PROHIBITED_AS_FORMAL_THEORY
8_LEVEL_TERMINAL_REFINEMENT = PROHIBITED_AS_FORMAL_THEORY
CURRENT_TRANSFER_BASELINE = R10_SIMPLE_MATERIAL
```
