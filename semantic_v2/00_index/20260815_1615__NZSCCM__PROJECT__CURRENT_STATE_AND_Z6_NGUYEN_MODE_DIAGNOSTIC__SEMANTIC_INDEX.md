# NZ-SCCM project current state — Z6 Nguyen-vs-mode-space diagnostic

**Timestamp:** 2026-08-15 16:15 +08:00  
**Identity:** CURRENT OPERATIONAL SEMANTIC INDEX

## 1. Frozen parent theory

```text
FORMAL_DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
GENERALIZED_COORDINATES = D,q
KINEMATICS = NGUYEN_SECOND_ORDER
R10 = FROZEN
N48-C1/MM = FROZEN
CAYLEY-HAMILTON = GOVERNING
GENERAL_D15 = GOVERNING
A0 = a/500 for current Z-family comparator diagnostics
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
STRUCTURAL_CALIBRATION = NO
```

## 2. Comparator identity

```text
ZHOU LOWER = Eqs.5-87/5-88 FE-informed Perry-Robertson lower-envelope design curve
WINTER = engineering upper-envelope reference
Z0-Z6 = representative parameter combinations, not recovered literal FE specimen IDs
```

Zhou Chapter 5 Table 5.1 confirms Group 4 spans `ns=10–60, h=100–130 mm, a=3000–9000 mm, b=2000–12000 mm` with `ls=200 mm, ts=4 mm, fy=355 MPa, fcu=40 MPa`. Z6 is inside this nominal range but lies at its extreme high-slenderness corner.

## 3. New 16:15 causal results

### 3.1 Nguyen second-order truncation

At the current Z6 reduced peak (`q0=.0015`, `q=.0058976`) the maximum slope is only about `0.03099 rad = 1.775 deg`; the leading small-angle omitted-term indicator `theta^2/6` is about `1.60e-4 = 0.016%`. Even the deeper H0 locator (`q≈.007356`) gives only about `2.13 deg`.

Decision:

```text
NGUYEN_SECOND_ORDER_AS_PRIMARY_Z6_ERROR_CAUSE = NOT SUPPORTED
```

This does not prove all higher-order Green-Lagrange terms are identically zero; it rejects the simple claim that large `b/h` alone makes Nguyen's second-order relation responsible for a 20–25% capacity gap.

### 3.2 Linear mode separation

For Z6, Zhou full-topology elastic mode candidates give:

```text
Pcr(1,1) = 42.8315 MN
Pcr(2,1) / Pcr(1,1) = 2.1347
Pcr(3,1) / Pcr(1,1) = 4.1634
Pcr(1,2) / Pcr(1,1) = 4.2580
```

S1–S4 neighbors have the nearest second mode at least `1.774–2.367` times the fundamental. Thus Z6 is not a linearly near-degenerate wrong-halfwave case.

Decision:

```text
WRONG_LINEAR_HALFWAVE_COUNT_AS_PRIMARY_CAUSE = NOT SUPPORTED
```

### 3.3 Unchanged-method S0–S4 nonlinear neighborhood sweep

All material/kinematic equations are unchanged. Engineering peak trend:

|case|a/h|b/h|lambda_Zhou|NZ peak MN|Zhou lower MN|NZ-Zhou|
|---|---:|---:|---:|---:|---:|---:|
|S0 Z6|69.23|92.31|1.4341|37.5094|49.6724|-24.49%|
|S1 a=8000|61.54|92.31|1.3782|40.7732|50.2501|-18.86%|
|S2 b=10000|69.23|76.92|1.2400|37.0002|44.1305|-16.16%|
|S3 a=8000,b=10000|61.54|76.92|1.2154|39.6080|44.6847|-11.36%|
|S4 a,b -5%|65.77|87.69|1.3625|38.1674|47.9466|-20.40%|

The 5% perturbation S4 does not jump back to the ±5% band; the discrepancy decreases smoothly as overall slenderness is reduced. Therefore Z6 is not behaving as an isolated numerical singularity.

Decision:

```text
Z6_ISOLATED_NUMERICAL_BUG = NOT SUPPORTED
HIGH_SLENDERNESS_SYSTEMATIC_CONSERVATIVE_BIAS = SUPPORTED
```

The stronger response to reducing `b/h` is directionally consistent with Zhou Chapter 5, which identifies width/thickness as especially important to four-edge stability.

## 4. Current causal ranking

```text
1. SINGLE-q FINITE-AMPLITUDE MODE SPACE / POSTBUCKLING REDISTRIBUTION = PRIMARY OPEN SUSPECT
2. DISCRETE INTERNAL-WEB TOPOLOGY AT LARGE AMPLITUDE = OPEN SECONDARY SUSPECT
3. FULL INCREMENTAL J2 PLASTIC REDISTRIBUTION = OPEN SECONDARY SUSPECT
4. NGUYEN SECOND-ORDER KINEMATICS ITSELF = CURRENTLY NOT SUPPORTED AS PRIMARY CAUSE
5. WRONG LINEAR m=1 HALFWAVE = CURRENTLY NOT SUPPORTED
```

The distinction is mandatory: a limitation of the current low-dimensional projection must not be relabelled as a failure of Nguyen's continuous second-order strain-displacement relation.

## 5. Current next task

```text
CURRENT_NEXT_TASK = Z6_ZERO_SPATIAL_HIGHER_HARMONIC_RELEASE_DIAGNOSTIC
```

Authorized diagnostic only:

1. retain Nguyen second-order, R10, N48, CH and D15;
2. retain current `w11` mode;
3. add one symmetric higher out-of-plane harmonic amplitude, first `w31`;
4. require exact degeneration `q31=0 -> current single-q model`;
5. keep one continuous domain and zero structural quadrature/sampling;
6. compare Z6, S4 and S3 without Zhou/Winter in root selection;
7. if the released harmonic produces a load gain that grows strongly with normalized slenderness, diagnose single-q finite-amplitude mode-space insufficiency;
8. if the gain is small, move next to discrete-web topology or full incremental J2 redistribution.

This is a diagnostic gate only and does not create or promote a new production multimode theory.

## 6. Latest artifacts

- `semantic_v2/10_governance/20260815_1615__Z6_NGUYEN_SECOND_ORDER_VS_LOW_DIMENSIONAL_MODE_SPACE__LOCK.md`
- `semantic_v2/60_validation/steel_shell/20260815_1615__NZSCCM__Z6__NGUYEN_VS_MODE_TRUNCATION_AND_NEIGHBOR_SWEEP__AUDIT.md`
- `semantic_v2/40_execution/steel_shell/20260815_1615__NZSCCM__Z6__KINEMATICS_MODE_NEIGHBOR_AUDIT_INTERMEDIATES.json`
- `semantic_v2/40_execution/steel_shell/20260815_1615__NZSCCM__Z6__NGUYEN_MODE_AND_NEIGHBOR_SWEEP__REPRO.py`
- `semantic_v2/50_results/steel_shell/20260815_1615__NZSCCM__Z6_S0_S4__UNCHANGED_METHOD_PEAK_TREND__RESULT.csv`
- `semantic_v2/50_results/steel_shell/20260815_1615__NZSCCM__Z6_S1_S4__UNCHANGED_LOCALCAP_BRANCH_LOCATORS__RESULT.csv`
- `semantic_v2/50_results/steel_shell/20260815_1615__Z6_S0_S4__LINEAR_MODE_SEPARATION__RESULT.csv`
- `semantic_v2/50_results/steel_shell/20260815_1615__Z6__NGUYEN_SMALL_SLOPE_INDICATORS__RESULT.csv`
- `semantic_v2/50_results/steel_shell/20260815_1615__NZSCCM__Z6_S1_S4__LOCALCAP_DEG20_DEG32_CHECKPOINTS__RESULT.csv`

Historical H0 compiler/domain diagnostics remain evidence but do not control the present causal ordering.
