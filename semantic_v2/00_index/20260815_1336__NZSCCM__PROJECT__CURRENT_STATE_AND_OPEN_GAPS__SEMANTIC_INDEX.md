# CURRENT STATE AND OPEN GAPS — NZ-SCCM

**Timestamp:** 2026-08-15 13:36 +08:00  
**Identity:** CURRENT_PRIMARY / HOMOGENIZED WEB-STEEL H0 GATE COMPLETE  
**Supersedes as operational entry:** `20260815_1308__NZSCCM__PROJECT__CURRENT_STATE_AND_OPEN_GAPS__SEMANTIC_INDEX.md`

---

## 0. Parent theory remains locked

```text
FORMAL_DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
GENERALIZED_COORDINATES = D,q
KINEMATICS = NGUYEN_SECOND_ORDER
R10 = FROZEN
N48-C1/MM = FROZEN
CAYLEY_HAMILTON = GOVERNING
GENERAL_D15 = GOVERNING
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
STRUCTURAL_CALIBRATION = NO
```

Zhou comparison remains original full MCFSTW/original formulas.

---

## 1. New user-directed NZ web representation

The internal web material is now under an H0 extension test as a continuous homogenized longitudinal web-steel phase:

```text
rho_w = ts/ls
Ac_eq = (1-rho_w)*b*tc
Aw_eq = rho_w*b*tc = ns*ts*tc
outer faceplates = retained continuous shell
physical web strips/nodes/material points = 0
```

For Z0-Z6, `rho_w=0.02`.

The exact section baseline

```text
(1-rho_w)*fc'*b*tc + fy*rho_w*b*tc + fy*2*b*ts
```

reproduces Zhou's original full-section `Pyth` exactly for all seven cases.

Theory contract:

- `semantic_v2/20_theory/nc_steel_shell_panel/20260815_1336__NZSCCM__HOMOGENIZED_WEB_STEEL_PHASE__THEORY_AND_ZERO_DISCRETIZATION_CONTRACT.md`

---

## 2. H0 execution status

Primary fixed-state activation uses a degree-24 material-coordinate compiler for the uniaxial ideal-EP web current map, composed with the continuous Nguyen field and integrated by exact D15 moments.

No structural x/y/z sampling or quadrature is used.

At the previously persisted current peak states, the web phase changes the force and produces large nonzero `Rq`; therefore those fixed-state loads are not new capacities.

A degree-10 same-D branch-location diagnostic re-equilibrated q for Z0-Z5:

```text
Z0 q shift +20.38%, P(same-D eq) 40.9523 MN
Z1 q shift +19.55%, P(same-D eq) 24.8777 MN
Z2 q shift +42.15%, P(same-D eq) 44.9368 MN
Z3 q shift +12.66%, P(same-D eq) 49.4964 MN
Z4 q shift +9.27%,  P(same-D eq) 77.2971 MN
Z5 q shift +2.17%,  P(same-D eq) 14.9633 MN
```

These are branch-locator diagnostics, not Pu.

Degree-16 spot checks at Z0 and Z4 preserve the same conclusion and remain roughly 10% above Zhou at those fixed D values.

Artifacts:

- `semantic_v2/40_execution/steel_shell/20260815_1336__NZSCCM__Z0_Z6__HOMOGENIZED_WEB_STEEL_PHASE__H0_EXECUTION_REPORT.md`
- `semantic_v2/40_execution/steel_shell/20260815_1336__NZSCCM__Z0_Z6__HOMOGENIZED_WEB_STEEL_PHASE__PARAMS_AND_INTERMEDIATES.json`
- `semantic_v2/50_results/steel_shell/20260815_1336__NZSCCM__Z0_Z6__HOMOGENIZED_WEB_STEEL_PHASE__H0_RESULT.csv`

---

## 3. Z6 blocking gate

At `D=0.705`, activating the web phase keeps `Rq` strongly negative through the last evaluated admissible neighborhood:

```text
q=0.005 -> Rq approx -2.5164e9 N mm
q=0.006 -> Rq approx -1.5459e9 N mm
```

Continuation toward q=0.008 drives the current Z6 concrete N48 polynomial outside its validated compiler interval `[-1.15,0.23]`; catastrophic extrapolation is rejected.

```text
Z6_WEB_PHASE_RQ_ROOT_INSIDE_CURRENT_COMPILER_DOMAIN = NOT FOUND
N48_EXTRAPOLATION = REJECTED
SILENT_COMPILER_WIDENING = NOT PERFORMED
FULL_WEB_PHASE_Z0_Z6_Pu_RECALCULATION = NOT COMPLETE
```

---

## 4. Current decisions

```text
HOMOGENIZED_WEB_STEEL_CONCEPT = MECHANICALLY FEASIBLE / ANALYTICALLY COMPATIBLE
ZERO_STRUCTURAL_DISCRETIZATION = PASS
SECTION_MATERIAL_CONSERVATION = PASS
DIRECT_PRODUCTION_PROMOTION = NO
Z0_Z5_BRANCH_RELOCATION = CONFIRMED
Z6_CURRENT_N48_DOMAIN = BLOCKING GATE
```

The H0 result shows that adding the full web-steel material phase is not merely an axial strength correction. It changes the q-equilibrium materially and tends to raise Z0-Z4 strongly at the old D scale, while Z6's branch is pushed toward a larger-amplitude region.

---

## 5. Current next task

```text
CURRENT_NEXT_TASK = WEB_PHASE_Z6_MATERIAL_DOMAIN_PREFLIGHT
```

Required next execution:

1. derive analytic coefficient/invariant bounds for the Z6 web-phase connected branch without spatial sampling;
2. determine the material-coordinate interval required before any polynomial evaluation outside the current `[-1.15,0.23]` domain;
3. test whether the frozen N48-C1/MM order can represent the same physical R10 operator over that interval with acceptable material-function error;
4. only on PASS continue full connected-branch `Rq=0 -> L=0 -> KZ` recalculation;
5. on FAIL, do not widen/fudge parameters and do not accept the web phase as production.

Swartz24 full same-expression L/KZ remains open/deferred.
