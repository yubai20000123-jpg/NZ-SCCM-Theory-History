# NZ-SCCM — Z6 rectangular Airy direct-R10 audit and fixed-N48 formal-representation gate

**Timestamp:** 2026-08-17 13:37 +08:00  
**Status:** EXECUTED AUDIT + COMPILER FAIL GATE / NO FORMAL Z6 Pu RELEASE

## 0. Objective

This calculation tests the user's proposed diagnostic sequence:

1. use the previously successful Case21 path as a clue, not as a literal copy;
2. generalize the Airy membrane direction correctly to rectangular Z6;
3. see whether the real Z6 mechanics branch can be calculated;
4. independently test whether a direct fixed-N48 reuse is accurate enough over the much wider Z6 material domain;
5. if not, stop before releasing a formal Pu and reorganize the material analytic compiler.

## 1. Real Z6 inputs

```text
a = 9000 mm
b = 12000 mm
ell = 9000 mm
k = b/ell = 1.3333333333333333
m* = 1
h = 130 mm
tc = 122 mm
ts = 4 mm
ns = 60
ls = 200 mm
rho_w = 0.02
fc = 30.4 MPa
eps0 = 0.0018712490394580678
nu_c = 0.18
Es = 206000 MPa
fy = 355 MPa
nu_s = 0.30
A0 = 18 mm
q0 = 0.0015
```

The virtual AR2 object is not used.

## 2. Rectangular Airy coefficients

For `k=4/3`, `nu=.18`:

```text
b0  = -(1+nu*k^2)/4 = -0.33
b20 = (nu*k^2-1)/4  = -0.17
b22 = 1/4            = +0.25
c02 = (nu-k^2)/4     = -0.3994444444444444
c22 = k^2/4          = +0.4444444444444444
d22 = -k/2           = -0.6666666666666666
```

At `lambda=1` the pure isotropic elastic check produces exactly

```text
sigma_x/(E eps0) = -M/4 cos(2Y)
sigma_y/(E eps0) =  k^2 M/4 [1-cos(2X)]
tau_xy            = 0
```

so the rectangular direction passes the mechanics benchmark and is not a copied square coefficient set.

## 3. Direct-R10 audit model

The audit uses:

- frozen raw R10 concrete current map;
- effective concrete fraction `1-rho_w=.98`;
- two outer face steel plates with the already-used local radial elastic-perfectly-plastic cap;
- longitudinal homogenized web/PBL steel phase with `rho_w=.02`;
- one complete Z6 halfwave;
- rectangular Airy scalar `lambda`;
- coupled solution `Rq_base=0, RA=0` on the origin-connected branch.

Gauss-Legendre evaluation is used only as an external continuum oracle. It is not promoted into the formal theory.

```text
N_formal_spatial_sampling   = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```

## 4. Direct-R10 Z6 branch and peak

The connected branch gives a smooth first capacity maximum around

```text
D ~= 1.30 to 1.31
q ~= 0.02144
lambda ~= 0.846
```

A local quadratic locator from the branch states gives

```text
D_peak ~= 1.30722165
```

Independent higher-grid evaluations at this D gave:

| audit order | Pu (MN) |
|---|---:|
| 32x32x14 + face 6 | 43.46840 |
| 40x40x16 + face 8 | 43.43295 |
| 48x48x20 + face 8 | 43.47339 |
| 56x56x22 + face 10 | 43.45191 |
| 64x64x24 + face 10 | 43.45118 |
| 72x72x28 + face 12 | 43.46148 |
| 80x80x30 + face 12 | 43.45654 |

The remaining oscillation is associated with the external audit treatment of local plastic interfaces. At engineering scale the direct-source mechanics oracle is therefore recorded as

\[
\boxed{P_u^{direct\ R10,\ audit}\approx43.46\ \mathrm{MN}.}
\]

This is not a formal zero-quadrature release.

## 5. Representative high-grid state

At the 80x80x30 + face-12 audit near the peak:

```text
D       ~= 1.30722165
q       ~= 0.02144304
lambda  ~= 0.84614161
P       ~= 43.45654 MN
Pc_eff  ~= 20.23789 MN
Ps_face ~= 16.75865 MN
Pw      ~=  6.45999 MN
```

The face-steel trial von-Mises ratio reaches approximately

```text
r_vm,max ~= 1.7833
```

so the local steel cap is active.

The raw-R10 concrete normalized principal material coordinate spans approximately

```text
lambda_material_min ~= -1.62252
lambda_material_max ~= +1.07324
```

on the audit state. This immediately proves that the historical narrow Z6 concrete compiler `[-1.15,+.23]` is not admissible for the current branch.

## 6. External Zhou comparison — audit interpretation only

The original full-MCFSTW Zhou formula chain gives for the same nominal Z6 parameter combination

```text
Pyth_full = 88.089888 MN
Pcr_Zhou  = 42.831476 MN
Pu_Zhou_original_formula = 49.672436 MN
```

The direct raw-R10 Airy audit is therefore approximately

```text
Delta = 43.45654 - 49.672436 = -6.21590 MN
relative = -12.51 %
```

This is a substantial model-side discrepancy, but Zhou's number is a fitted analytical/design formula, not an independent experimental truth. More importantly, raw R10 contains no N48 material compiler, so this 12.5% difference cannot be blamed on the compiler.

## 7. Restored CH/D15 fixed-state regression

Before testing the wide compiler, the old exact N48 -> 2x2 CH -> D15 concrete evaluator was restored and checked at the historical Z6 state

```text
D = .705
q = .0058975999
lambda = 0
compiler interval = [-1.15,+.23]
```

It returns

```text
Pc_full = 13.32145962 MN
Pc_eff  = .98*Pc_full ~= 13.05503043 MN
```

which reproduces the historical H0 record `Pc_eff=13.05503 MN`. This validates the recreated formal evaluator identity.

## 8. Fixed N48 on the wide Z6 domain

The previously used broad interval

```text
[-2.35,+1.90]
```

was then regenerated at the same fixed N48 order. Full-domain primitive value errors are approximately

```text
U  max error  = 0.0262457
C  max error  = 0.0824700
T  max error  = 0.710620
T7 max error  = 0.796049
T constrained minimax = 0.703936
```

These are source-representation errors, not structural quadrature errors.

## 9. Same-state compiler fidelity gate

At the direct-R10 peak state (`D~=1.30722, q~=0.021443, lambda~=0.84614`), the broad fixed-N48 + CH + exact-D15 concrete evaluator gives approximately

```text
Pc_full_N48 = 18.5008 MN
```

whereas the raw-R10 high-grid audit gives

```text
Pc_eff_raw ~= 20.23789 MN
Pc_full_raw = Pc_eff_raw/.98 ~= 20.6509 MN
```

Therefore at the **same physical state**:

```text
fixed-N48 concrete discrepancy ~= -2.150 MN
relative discrepancy ~= -10.4 %
```

This comparison does not involve Zhou or any capacity-root selection. It directly diagnoses material analytic representation fidelity.

The same broad-N48 state also gives large shifts in the formal concrete generalized residual components, approximately

```text
Rq_c_N48 ~= -8.2321e9 N mm
RA_c_N48 ~= +9.2049e6 N mm
```

so a formal branch solved with this representation would move materially away from the raw-R10 branch.

## 10. Gate decision

The user's proposed diagnostic criterion is met:

```text
REAL_Z6_MECHANICS_CALCULABLE = YES
DIRECT_R10_AUDIT_PEAK ~= 43.46 MN
LITERAL_FIXED_N48_WIDE_COMPILER_REUSE = FAIL
FAIL_REASON = SAME_STATE MATERIAL SOURCE FIDELITY (~10.4% concrete load discrepancy)
FORMAL_Z6_Pu_FROM_FIXED_N48 = NOT RELEASED
```

The correct next step is therefore not another spatial integration method and not blind global-order escalation. It is to reorganize the frozen R10 analytic compiler as a convergent source series whose individual composed terms are contracted by finite exact D15 moments.

## 11. Current scientific distinction

Two different gaps now exist and must not be conflated:

1. **Compiler gap:** broad fixed-N48 differs from raw R10 by about 10.4% in the concrete load at the same Z6 state. This is an implementation/representation problem and must be repaired.
2. **Model/comparator gap:** even raw R10 predicts about 43.46 MN versus Zhou-original-full formula 49.67 MN. Since raw R10 bypasses N48, this residual gap survives compiler removal and may belong to structural/material modeling or comparator identity. It must not be tuned away during compiler reconstruction.
