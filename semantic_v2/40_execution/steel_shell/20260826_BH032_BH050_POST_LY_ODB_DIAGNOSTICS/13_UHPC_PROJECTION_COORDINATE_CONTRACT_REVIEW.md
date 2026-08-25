# BH032/BH050 UHPC projection — coordinate-contract review before accepting K4

**Status:** DIAGNOSIS CORRECTION / NO THEORY CHANGE  
**Date:** 2026-08-26  

## 1. What remains valid

The Codex ODB extraction of UHPC `LE33`, the reported frame histories, weighted residuals, steel/core strain comparisons, and all archived raw artifacts are retained as diagnostic evidence.

The latest pooled regression reported at FEM peak:

- BH032: `kappa_UHPC_fit = 1.93135e-5 /mm`, theory `4.78844e-5 /mm`;
- BH050: `kappa_UHPC_fit = 1.83974e-5 /mm`, theory `6.49782e-5 /mm`.

The report therefore proposed `K4 > K3 > K2 > K1`.

## 2. New coordinate-contract problem

Before that ranking can be accepted as a physical conclusion, the independent coordinate used in the UHPC regression must be audited.

The production theory uses nominal UHPC thickness

`tc = 42 mm`, hence the local through-thickness material coordinate is nominally `z in [-21,+21] mm` relative to the local section midsurface.

However the ODB pooled regression reported global-y node bounds:

- BH032: `y_lower=-20.9686`, `y_upper=+24.9921`, total span `45.9608 mm`;
- BH050: `y_lower=-21.0000`, `y_upper=+27.2377`, total span `48.2377 mm`.

These spans exceed the nominal 42 mm core thickness by about 9.4% and 14.9%, respectively. They therefore cannot be treated automatically as the physical local thickness coordinate of one section column. The pooled global-y span can contain transverse midsurface offset/imperfection/global or local out-of-plane deflection variation across the width, in addition to the actual through-thickness coordinate.

Consequently, a regression of all selected section integration points using

`LE33 = eps0 + kappa*(global_y - one_global_mid)`

can mix two different spatial effects:

1. true through-thickness strain gradient within a local material column;
2. variation of the local midsurface position across the plate width.

That mixing can reduce or otherwise distort the fitted generalized curvature and the weighted R2 even if each local through-thickness column is close to linear.

## 3. Second observable issue to verify

The current Marguerre–Airy terminal equations are evaluated at a specified spatial station (`s=1` for the current terminal roots). The ODB diagnostic to date has used a section band integrated/averaged across a broad transverse width. Before any generalized-variable comparison is certified, it must be demonstrated that this width-averaged FEM quantity is the same observable as the theory's local `s=1` terminal section state. If not, the FEM extraction must be restricted to the corresponding transverse antinode band or the theory must be spatially averaged by an explicitly derived operator; no ad-hoc averaging is allowed.

## 4. Required next diagnostic

Use the existing ODB only; do not rerun Abaqus and do not modify R06/theory.

For BH032 and BH050:

1. Recover **reference-configuration** coordinates for UHPC integration-point columns.
2. Group samples by in-plane material column `(x,z_station)` (or the exact equivalent mesh-column identity).
3. For each column define a **local thickness coordinate**
   `zeta = y_ref - y_mid_ref(column)`
   so that the local core boundaries recover approximately `zeta = +/-21 mm` for the nominal 42 mm core.
4. Do not use the deformed/global midsurface offset as part of `zeta`.
5. Identify the FEM transverse position corresponding to the theory terminal station `s=1`; perform the primary comparison there using a narrow, mesh-resolved band. A full-width average may be retained only as a secondary diagnostic.
6. Within each selected local column fit
   `LE33(zeta) = eps0_col + kappa_col*zeta`
   with the existing area-consistent weights.
7. Report the column-to-column distribution of `eps0_col` and `kappa_col`, the antinode-band weighted mean, residuals, and local face-band strains.
8. Apply the same procedure to BH032 and BH050 before comparing with theory.

## 5. Decision boundary

Until the local-coordinate / spatial-station audit is complete:

```text
K4_GENERALIZED_VARIABLE_TO_FEM_OBSERVABLE_CONTRACT_NOT_VALIDATED = PROVISIONAL
K3_PHASE_COMPATIBILITY = PROVISIONAL
K2_SECTION_WARPING_LOCALIZATION = PROVISIONAL
K1_MARGUERRE_AIRY_SECTION_NM_ERROR = NOT_PROVEN
R02_R06_PRIMARY_ERROR = NOT_PROVEN
THEORY_CHANGE = PROHIBITED
```

The immediate next task is therefore **not** to change linear section kinematics, phase compatibility, Marguerre–Airy, or R06. It is to establish the correct local material-coordinate and spatial-station mapping between the theoretical generalized terminal variables and the FEM observable.
