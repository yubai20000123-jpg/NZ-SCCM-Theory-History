# NZ-SCCM Z0–Z6 reduced Zhou batch execution report

**Timestamp:** 2026-08-14 22:40 +08:00  
**Parent remote commit before this batch:** `9fc3149faa173651c8f28d8b7b09a6ca5fde2be7`  
**Result identity:** `CONNECTED_REDUCED_IDEAL_EP_DIAGNOSTIC`

## 1. Scope and frozen structural identity

This batch executes the seven representative Zhou Table-5.1 parameter combinations Z0–Z6 already persisted in the repository. The compared structural object is identical on both sides:

- continuous ordinary-concrete core;
- two continuous outer steel faceplates;
- internal steel webs deleted from the steel bearing/stiffness contribution and their volume absorbed into the continuous concrete core.

The formal NZ-SCCM structural identity remains:

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
STRUCTURAL_CALIBRATION = NO
EXPERIMENTAL_LOAD_USED_FOR_TUNING = NO
q0 = 1/400
nu_c = 0.18
nu_s = 0.30
Es = 206000 MPa
```

Concrete chain:

```text
R10 whole retained tensile branch C2 energy reconstruction
-> N48-C1/MM
-> Cayley-Hamilton 2D lift
-> Nguyen second-order complete-halfwave kinematics
-> coefficient-space general D15 exact moments
-> Pc(D,q), Rq,c(D,q)
```

Steel-shell elastic branch uses the exact plane-stress isotropic current stress over the same Nguyen field and exact thickness/trigonometric moments.

## 2. Reduced ideal-EP post-yield operationalization used in this execution

The current locked reduced-Zhou governance requires:

```text
elastic/unbuckled -> Et,eff = Es
yield-first -> no elastic Yun S1 branch before yield
continuing ideal-plastic loading -> Et,eff = 0
steel stress remains strength-capped
no detailed expanding plastic-zone/local-shape model is introduced
```

To make that already-authorized reduced diagnostic executable without inventing a structural plastic-zone mesh, this batch uses a **homogeneous whole-shell J2 radial strength cap** for the stress contribution after first yield:

\[
\alpha(D,q)=\min\left(1,\frac{f_y}{\sigma_{VM,max}^{E}(D,q)}\right),
\]

\[
\boldsymbol\sigma_s(D,q)=\alpha\,\boldsymbol\sigma_s^E(D,q).
\]

Hence

\[
P_s=\alpha P_s^E,\qquad R_{q,s}=\alpha R_{q,s}^E.
\]

For the stability-material part after yield, the locked effective ideal-plastic tangent remains `Et,eff = 0`; the radial cap is used here to continue the stress/resultant branch, not to assert a fully resolved 2D flow-plasticity current tangent.

A continuous maximization audit of the elastic plane-stress von-Mises field was performed at the final control states. In every Z0–Z6 case the controlling point is the outer compression face at approximately `X=Y=pi/2`, so the strength-cap trigger is not based on a structural spatial grid.

**Important identity boundary:** this is a reduced mechanism/branch diagnostic. It is not promoted to a final full-2D steel-shell production operator.

## 3. N48 compiler intervals

For Z0, Z1, Z3, Z4 and Z5 the current persisted compiler interval is retained:

```text
[-1.15, 0.12]
U,C,T7 = persisted N48-C1 rule
T = persisted N48-C1 constrained minimax
T minimax audit objective ~= 0.089569236
```

Z2 has a raw steel-yield strain ratio above the standard compressive compiler bound and was therefore given a source/input-only case-specific interval before its high-D control state was accepted:

```text
Z2 interval = [-1.35, 0.15]
T minimax material-coordinate nodes = 6001
T minimax objective ~= 0.119586480
```

Z6 develops the broadest positive material spectrum because of its wide/slender geometry and large connected q. Its final continuous spectrum requires an upper material coordinate above 0.12, so the case-specific interval used for the final branch is:

```text
Z6 interval = [-1.15, 0.23]
T minimax material-coordinate nodes = 3001
T minimax objective ~= 0.148153477
```

These are **material-coordinate compiler nodes**, not structural spatial quadrature/collocation points. Z6 therefore carries the weakest compiler-fidelity status of the seven cases; its numerical value must be treated as lower-confidence than Z0–Z5.

## 4. Connected branch procedure

For every case:

1. Generate the Nguyen continuous strain field from `(D,q)`.
2. Compile the concrete R10 current map through N48-C1/MM and Cayley-Hamilton.
3. Contract the finite coefficient field with exact D15 moments to obtain `Pc` and `Rq,c`.
4. Generate exact continuous elastic steel-shell `Ps^E` and `Rq,s^E` over the same field.
5. Apply the reduced J2 radial cap after the continuous first-yield condition.
6. Solve `Rq = Rq,c + Rq,s = 0` on the primary branch connected to the origin.
7. Bracket the first load maximum on that connected branch.
8. For a smooth maximum, locally refine the peak in `D`; for a constitutive yield cusp, retain the yield event when the post-yield branch immediately descends.

This batch persists the branch keypoints used in that localization. For smooth post-yield peaks, the numerical localization is a connected-branch peak diagnostic; a separate same-expression forward-AD `L=0` certificate has **not** been added in this batch. Therefore these values must not be relabelled as newly certified full production `Rq=0 + L=0` roots.

## 5. Z0–Z6 numerical results

| Case | D at control | q | Pc (MN) | Ps (MN) | NZ-SCCM Pu,diag (MN) | Zhou (MN) | NZ-Zhou (MN) | Error vs Zhou | Control identity |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Z0 | 0.886600 | 0.001013410 | 17.350427 | 16.947174 | **34.297601** | 33.429123 | +0.868477 | **+2.598%** | yield-cusp first maximum |
| Z1 | 0.606524 | 0.001628224 | 10.308505 | 10.590122 | **20.898627** | 22.208147 | -1.309520 | **-5.897%** | smooth post-yield maximum |
| Z2 | 1.145192 | 0.001380854 | 15.873710 | 21.872633 | **37.746343** | 36.858842 | +0.887502 | **+2.408%** | yield-cusp first maximum |
| Z3 | 0.846444 | 0.001407626 | 25.480850 | 16.858191 | **42.339041** | 41.158145 | +1.180895 | **+2.869%** | smooth post-yield maximum |
| Z4 | 0.948990 | 0.000594758 | 39.610058 | 22.427071 | **62.037130** | 62.043026 | -0.005896 | **-0.010%** | smooth post-yield maximum |
| Z5 | 0.982185 | 0.000118875 | 7.059676 | 5.818733 | **12.878409** | 13.097600 | -0.219191 | **-1.674%** | smooth post-yield maximum |
| Z6 | 0.663425 | 0.005439400 | 11.902673 | 22.358577 | **34.261250** | 44.740403 | -10.479153 | **-23.422%** | yield-cusp first maximum; expanded compiler |

Batch error summaries:

```text
MAPE, Z0-Z6 = 5.554%
MAPE, Z0-Z5 = 2.576%
Largest absolute error = Z6 = 23.422%
```

## 6. Immediate interpretation

The most important result is that the earlier Z0 historical diagnostic `26.1085 MN` is **not reproduced** by the newly connected reduced branch used here. Under the current reduced ideal-EP strength-cap continuation, Z0 is approximately `34.30 MN`, only `+2.60%` above the Zhou empirical value `33.43 MN`.

The same execution rule gives good agreement for Z0, Z2, Z3, Z4 and Z5, moderate underprediction for Z1, and one clear outlier Z6. Excluding Z6, the six-case MAPE is about `2.58%`.

Z6 is qualitatively different from the other six cases:

- it develops a much larger global `q`;
- its continuous material spectrum exceeds the standard positive compiler bound;
- it requires an expanded material compiler interval;
- even after that extension, NZ-SCCM remains about `23.42%` below Zhou.

Therefore the next diagnostic should focus on Z6 rather than globally changing R10 or applying a fitted correction to all seven cases. In particular, Z6 is the first case where compiler-domain breadth and wide/slender geometric mechanics are simultaneously active.

## 7. What is and is not claimed

```text
Z0_Z6_BATCH_NUMERICAL_EXECUTION = COMPLETE
ALL_SEVEN_NZ_VALUES = AVAILABLE
SAME_REDUCED_OBJECT_AS_ZHOU = YES
FORMAL_STRUCTURAL_SPATIAL_QUADRATURE = 0
STRUCTURAL_CALIBRATION = NO
EXPERIMENTAL_LOAD_TUNING = NO
OLD_Z0_26p1085_REUSED_AS_TARGET = NO
CROSS_CASE_SCALING = NO
FULL_2D_STEEL_PLASTIC_ZONE_OPERATOR = NOT CLAIMED
SAME_EXPRESSION_AD_L0_CERTIFICATE = NOT YET ADDED
Z6_COMPILER_FIDELITY = LOWER_CONFIDENCE / REQUIRES FOLLOW-UP
```

Companion files contain the exact parameter state, coefficient-space reproducibility kernel, connected-branch keypoints, and machine-readable result table.
