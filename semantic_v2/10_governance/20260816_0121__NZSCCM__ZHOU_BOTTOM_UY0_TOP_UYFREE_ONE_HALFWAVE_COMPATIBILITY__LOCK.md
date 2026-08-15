# NZ-SCCM — Zhou bottom-uy0 / top-uyfree one-halfwave compatibility gate

**Timestamp:** 2026-08-16 01:21 +08:00  
**Parent:** `20260816_0102__NZSCCM__PROJECT__CURRENT_STATE_AR2_PF_TO_D15_CURRENT_MATERIAL_MAPPING_GATE__SEMANTIC_INDEX.md`

## Frozen project boundary

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order kinematics
R10 / N48-C1-MM / Cayley-Hamilton unchanged
General D15 unchanged
A0=a/500
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
Gauss/Simpson/adaptive/collocation/cells/material-point-grid=PROHIBITED
out-of-plane multimode production expansion=PROHIBITED
Zhou/Winter calibration=PROHIBITED
```

The historical Gauss-based AR2 `Pu=40.97334 MN` remains retracted and is not admissible evidence.

## Gate question

Zhou Table 1.3 source boundary retained from the previous source audit is

```text
loaded top:    ux=0, uy=unset, uz=0
loaded bottom: ux=0, uy=0,     uz=0
lateral sides: ux=unset, uy=unset, uz=0
```

The present gate asks only:

> Is `uy=0` on the complete bottom loaded edge merely a removable rigid-body axial datum, so that the 01:02 symmetric one-halfwave axial-correction space remains exactly equivalent to Zhou's full in-plane boundary class?

## Pass criterion

The gate may pass as a pure datum only if fixing the complete bottom trace removes no x-dependent admissible axial-displacement variation beyond one global rigid translation, or if every excluded x-dependent top/bottom trace direction is rigorously inactive for the m=2 FvK membrane source.

## Fail criterion

The gate fails current exact one-halfwave equivalence if there exists a conforming, zero-mean-in-x axial trace mode which:

1. satisfies `v(x,0)=0` exactly;
2. is admissible because the top `v` trace is not an essential condition;
3. cannot be represented by a global rigid translation or the mean shortening coordinate `D`;
4. has nonzero exact generalized forcing from the m=2 FvK geometric membrane source; and
5. is excluded by the current 01:02 symmetric `v_rs ~ sin(sY)` one-halfwave family.

If this fail condition is met, stop before generic multi-coordinate R10/N48 implementation and before any new Pu calculation.

## Execution discipline

No new material theory, no spatial numerical integration, no spatial subdivision, no Pu fitting and no alternative out-of-plane mode are authorized in this gate. Exact finite coefficient/closed-form moments only.