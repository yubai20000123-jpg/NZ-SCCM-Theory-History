# NZ-SCCM semantic_v2 tree delta — 2026-08-20 14:41

## GitHub startup verification

Actual main HEAD before this audit:

`0dc3a634807d3c1eaa15b833fdef8bcb86977538`

The previously unconfirmed NC-M2 chain is now verified:

- `8103eefa581e19893773cda65936a6b1cc41bfff`
- `adc92b96785da15d06cb17b009c0e7e6d84aed74`
- `0dc3a634807d3c1eaa15b833fdef8bcb86977538`

## New theory checkpoint

`semantic_v2/20_theory/20260820_1441__NZSCCM__NC_M2_TENSION_BACKBONE_AUDIT__FINITE_ENERGY_GATE.md`

Main decision:

`T(t)=t/(1-t+t^2)` has a valid smooth single peak but `T(t)~1/t`, therefore its tensile work integral diverges. It is not accepted for production lock.

## New execution checkpoint

`semantic_v2/40_execution/combined/20260820_1441__NZSCCM__NC_M2_TENSION_CURVE_AUDIT.md`

## Current identities

- NC-M1: `REJECTED_DIAGNOSTIC_CANDIDATE`
- NC-M2: `ACTIVE_MATERIAL_CANDIDATE / NOT_YET_PRODUCTION_LOCK`
- NC-M2 tension backbone: `UNDER_REVIEW / FAILS_FINITE_ENERGY_GATE`

No NC-M3 has been created. The finite-energy rational family recorded in the theory audit is diagnostic only; no parameter has been selected and no Case21 load calibration was used.

## Next material question

Before formal replacement of T(t), decide whether the NC tensile current law remains a length-free total-strain law or is regularized by fracture energy / crack-band length. Only after that decision should a new formal material candidate be issued with the required five-figure curve package. CC eta remains the next interaction term to audit after the tensile backbone is resolved.
