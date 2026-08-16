# NZ-SCCM PROJECT CURRENT STATE — MEMBRANE HISTORY RECOVERED

**Updated:** 2026-08-17 00:02 +08:00

## Current status

The prior `Z6_FIVE_MEMBRANE_DOWNSHIFT_DIAGNOSTIC` state is superseded as a physical interpretation.

Recovered controlling evidence:

1. `20260815_2358` explicitly retracted the prior interpretation that free membrane coordinates reduce capacity.
2. `20260816_0007` exact FvK/Airy gate proved positive postbuckling membrane stiffness and edgeward axial stress redistribution.
3. `20260816_0016` Z6 boundary gate locked `ZHOU_BOUNDARY_CLASSICAL_MEMBRANE_STIFFENING_SIGN = POSITIVE / PASS`.
4. `20260816_1848` quantified the membrane driver scale: Case21 small perturbation, Z6 first-order effect, with `M_Z6/M_Case21=59.0684`.
5. `20260816_1912` five-term basis remains valid in its exact elastic Airy degeneration; the nonlinear unrestricted `Rm=0` amplitude promotion is reopened.

## Capacity status

```text
Case21 320.749185 kN = RETRACTED_AS_PHYSICAL_MEMBRANE_Pu / DIAGNOSTIC_ONLY
Z6 43.762840 MN      = RETRACTED_AS_PHYSICAL_MEMBRANE_Pu / DIAGNOSTIC_ONLY
Case21 historical/current-support closure 368.189 kN = retained support baseline pending corrected membrane closure
Z6 retained engineering baseline 51.30 MN = retained support baseline pending corrected membrane closure
NEW_CORRECTED_MEMBRANE_Pu = NOT RELEASED
```

## Physical membrane direction recovered

```text
CLASSICAL_MEMBRANE_POSTBUCKLING_STIFFNESS = POSITIVE
HIGH_b_over_t_EFFECT > LOW_b_over_t_EFFECT
CASE21_MEMBRANE_EFFECT_SCALE = SMALL
Z6_MEMBRANE_EFFECT_SCALE = LARGE / FIRST_ORDER
```

## Current unique next gate

`RECOVER_COMPATIBILITY_COUPLED_CURRENT_MEMBRANE_CLOSURE_FROM_1848_1912_TRANSITION`

Do not compute another Pu until the nonlinear membrane closure preserves compatibility/equilibrium/boundary work and the exact positive classical degeneration.

## Key new artifacts

- `../60_validation/common/20260817_0002__NZSCCM__MEMBRANE_HISTORY_RECOVERY_AND_DOWNSHIFT_RETRACTION__AUDIT.md`
- `../10_governance/20260817_0002__NZSCCM__POSITIVE_MEMBRANE_POSTBUCKLING_SIGN_AND_SCALE_RECOVERY__LOCK.md`
