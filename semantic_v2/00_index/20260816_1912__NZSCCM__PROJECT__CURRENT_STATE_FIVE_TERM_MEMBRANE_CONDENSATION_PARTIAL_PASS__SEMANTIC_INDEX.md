# NZ-SCCM current state — five-term membrane condensation partial pass

**Timestamp:** 2026-08-16 19:12 +08:00

## Current status

The 18:48 historical-RC-backbone / membrane-delta gate remains valid. The exact five-component compatible membrane subspace has now been promoted from a classical-delta interpretation into a finite internal-coordinate condensation formulation.

```text
FIVE_TERM_ELASTIC_CONDENSATION = PASS_EXACT
FIVE_TERM_AIRY_FVK_RECOVERY = PASS_EXACT
FIVE_TERM_GENERAL_D15_TARGET_CLOSURE = PASS
CURRENT_MATERIAL_RESIDUAL_AND_CONDENSATION_FORM = PASS_FORMAL
RC1_NESTED_TARGET_FUNCTIONAL_RUNTIME = OPEN
NEW_Pu = NOT_RUN
OVERALL_GATE = PARTIAL_PASS_TO_IMPLEMENTATION_BOUNDARY
```

## Five internal membrane coordinates

```text
r = [r0,r20,r22,s02,s22]
```

They are finite internal response coordinates. After current-material equilibrium and consistent Schur condensation, the global production root remains `(D,q)`.

Exact elastic square-halfwave result:

```text
r/M = [-(1+nu)/4,-(1-nu)/4,1/4,-(1-nu)/4,1/4]
fD=0
```

At `nu=.18` the exact 5x5 elastic matrix has condition number `4.87805`.

The reconstructed elastic stresses are exactly

```text
sigma_x/(E eps0) = -M cos(2Y)/4
sigma_y/(E eps0) = -D + M sin(X)^2/2
tau_xy             = 0
```

which recovers the classical Airy/FvK redistribution.

## Current-material equations

```text
Rm_j=sum_p integral sigma_p:B_j dV=0
Krr=dRm/dr
r_g=-Krr^-1 Rm_g
Pbar_g=P_g+P_r r_g
Rqbar_g=Rq_g+Rq_r r_g
Lbar=Pbar_D Rqbar_q-Pbar_q Rqbar_D
Kgg_cond=Kgg-Kgr Krr^-1 Krg
```

Concrete and reinforcement enter the same internal equilibrium before condensation.

## General-D15 target closure

The five membrane residuals are finite target kernels of the same current stress field:

```text
D15[Sxx]
D15[Sxx cos2X]
D15[Sxx cos2X cos2Y-Sxy sin2X sin2Y]
D15[Syy cos2Y]
D15[Syy cos2X cos2Y-Sxy sin2X sin2Y]
```

All reduce exactly to the existing General-D15 integer-trigonometric/thickness moment family; no structural spatial or thickness quadrature is introduced.

## Fail-fast diagnostic

A historical Case21 N48-C1 CH/D15 kernel was used only as a non-production current-material diagnostic. At the classical elastic `r`, the five nonlinear R10+rebar residuals were clearly nonzero, confirming that elastic Airy coefficients cannot be imposed in nonlinear current material. A first local Newton diagnostic was badly conditioned relative to the desired current route, so the legacy N48 path was stopped and no new root/Pu was produced.

```text
LEGACY_N48_AS_RC1_PRODUCTION = NO
```

## Material compiler state

`R10-MSAC-RC1` remains source-fidelity PASS for Z0-Z6 and must remain nested. Full monomial expansion is prohibited.

The missing implementation is now narrowly identified:

```text
nested RC1 factor graph
 -> arbitrary finite target kernel
 -> adjoint-Clenshaw / Qnm target recurrence
 -> General-D15 exact contraction
```

## Capacity boundary

```text
Case21 368.189 kN = historical/current-support closure only
Z6 51.30 MN = retained engineering baseline only
Z0-Z5 old Pu = retracted/diagnostic as previously governed
NEW membrane-redistributed Pu = NOT RELEASED
```

## Formal counters

```text
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
N_formal_thickness_quadrature=0
```

## Current unique next gate

```text
UNIFIED_V1_RC1_ADJOINT_CLENSHAW_GENERAL_D15_TARGET_FUNCTIONAL_EXECUTION_GATE
```

Pass requirements:

1. implement the RC1 nested target-functional backend without full stress expansion;
2. validate against direct General-D15 expansion at controlled low order;
3. run the same backend for `P,Rq,Rm1...Rm5` and later KZ targets;
4. record memory/time/moment-state complexity at the Z0-Z6 RC1 first-pass levels;
5. keep all formal spatial/thickness numerical integration counters at zero;
6. only after backend PASS solve current `r(D,q)`, Schur-condense, trace the connected `(D,q)` branch and release new Pu.

## Key artifacts

1. `../20_theory/nc_rebar_panel/20260816_1912__NZSCCM__FIVE_TERM_CURRENT_MEMBRANE_CONDENSATION_AND_RC1_D15__THEORY.md`
2. `../40_execution/common/20260816_1912__NZSCCM__FIVE_TERM_MEMBRANE_CONDENSATION_RC1_D15__EXECUTION_REPORT.md`
3. `../40_execution/common/20260816_1912__NZSCCM__FIVE_TERM_MEMBRANE_CONDENSATION_RC1_D15__PARAMS_AND_INTERMEDIATES.json`
4. `../40_execution/common/20260816_1912__NZSCCM__FIVE_TERM_MEMBRANE_CONDENSATION_RC1_D15__REPRO.py`
5. `../60_validation/common/20260816_1912__NZSCCM__FIVE_TERM_MEMBRANE_CONDENSATION_RC1_D15__AUDIT.md`
6. `20260816_1848__NZSCCM__PROJECT__CURRENT_STATE_RC_BACKBONE_MEMBRANE_DELTA_PASS__SEMANTIC_INDEX.md` — predecessor
