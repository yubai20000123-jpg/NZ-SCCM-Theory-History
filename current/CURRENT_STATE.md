# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-17 13:37 +08:00  
**Status:** Z6 RECTANGULAR AIRY MECHANICS CALCULABLE / DIRECT-COPY FIXED-N48 COMPILER FAILED / COMPILER REORGANIZATION ACTIVE

## Current operational entry

`semantic_v2/00_index/20260817_1337__NZSCCM__PROJECT__Z6_RECTANGULAR_AIRY_COMPILER_REORGANIZATION__SEMANTIC_INDEX.md`

## Current active task

```text
Z6_CONVERGENT_SERIES_FINITE_MOMENT_MATERIAL_COMPILER
```

## Latest user correction

The successful Case21 N48/CH/D15 path is a **reasoning precedent**, not a command to copy the Case21 fixed-N48 material representation literally to every geometry.

The Case21 result already obtained is retained, but Z6 is now used as the cross-geometry compiler diagnostic. If the direct-copy compiler shows an obvious source-fidelity error, the compiler must be reorganized as a convergent analytic series whose individual structural terms have finite exact moments.

## Formal project counters

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```

Gauss/direct continuum remains audit-only.

## Case21 retained result

The 13:04 Case21 finite-compiler formal baseline remains:

```text
Airy scalar + N48-C1/MM + 2x2 CH + General-D15
Pu_formal = 365.257 kN
raw-R10 mechanics oracle = 366.767829 kN
formal-vs-raw difference = -0.4120%
Pf_exp = 368.312750 kN
formal-vs-Pf error = -0.82976%
```

This remains a valid Case21 result; it is no longer interpreted as proof that the same fixed-N48 compiler should be copied unchanged to Z6.

## Real Z6 identity

```text
a = 9000 mm
b = 12000 mm
ell = 9000 mm
m* = 1
k = b/ell = 4/3
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

The historical virtual AR2 object (`a=24000,b=12000,m=2,ell=12000,q0=.004`) is not the current Z6 and may not be substituted for it.

## Rectangular Airy scalar

For `k=b/ell`, the mechanically derived direction is

\[
a(k,\nu)=\left[
-\frac{1+\nu k^2}{4},
\frac{\nu k^2-1}{4},
\frac14,
\frac{\nu-k^2}{4},
\frac{k^2}{4}
\right]^T.
\]

For Z6 (`k=4/3, nu=.18`):

```text
[-0.33, -0.17, +0.25, -0.3994444444, +0.4444444444]
shear Airy coefficient = -2/3
```

At `lambda=1` the pure isotropic elastic field reduces to

```text
sigma_x/(E eps0) = -M/4 cos(2Y)
sigma_y/(E eps0) = k^2 M/4 [1-cos(2X)]
tau_xy = 0
```

so the square Case21 direction has been generalized rather than copied.

## Z6 direct-source mechanics audit

Using frozen raw R10 concrete + effective concrete factor `.98` + two face-shell local ideal-EP caps + homogenized longitudinal web phase `.02`, and solving the rectangular Airy scalar branch `Rq_base=0, RA=0`, the direct continuum audit gives a first peak near

```text
D ~= 1.30722
q ~= 0.0214430
lambda ~= 0.84614
Pu_direct_R10_audit ~= 43.46 MN
Pc_eff ~= 20.238 MN
Ps_face ~= 16.759 MN
Pw ~= 6.460 MN
```

The face-shell local plastic cap is active (`trial VM ratio max ~=1.78`).

The raw-R10 concrete principal normalized material coordinate spans approximately

```text
[-1.6225,+1.0732]
```

at the peak neighborhood.

This is **audit-only**, not formal Z6 Pu.

## External Zhou comparator

For the same real nominal Z6 parameter combination, Zhou's original full-MCFSTW formula chain gives

```text
Pyth_full = 88.089888 MN
Pcr = 42.831476 MN
Pu_Zhou_original_formula = 49.672436 MN
```

The raw-R10 mechanics audit is therefore about `-12.5%` below the Zhou fitted formula. Since this comparison bypasses N48, that residual difference cannot be assigned to material-compiler error.

## Fixed-N48 direct-copy gate

Historical narrow Z6 compiler:

```text
[-1.15,+.23]
```

cannot cover the current Airy branch.

Regenerating a fixed N48 compiler on the previously used broad interval

```text
[-2.35,+1.90]
```

produces large primitive value errors:

```text
U  ~= 0.02625
C  ~= 0.08247
T  ~= 0.71062
T7 ~= 0.79605
```

At the same raw-R10 peak state:

```text
Pc_full_N48 ~= 18.5008 MN
Pc_full_raw  ~= 20.6509 MN
same-state concrete difference ~= -10.4%
```

Therefore:

```text
DIRECT_COPY_FIXED_N48_TO_WIDE_Z6_DOMAIN = FAIL
FORMAL_Z6_Pu_FROM_THIS_COMPILER = NOT RELEASED
FAILURE_CLASS = MATERIAL_ANALYTIC_COMPILER_FIDELITY
SPATIAL_INTEGRATION_FAILURE = NO
```

The old CH/D15 structural integrator itself remains valid: at the historical `D=.705,q=.0058975999,lambda=0` Z6 state it reproduces the persisted H0 concrete load to engineering precision.

## Current compiler direction

The next compiler must preserve frozen R10 physics but reorganize its analytic representation:

```text
R10 scalar source
 -> source-regular convergent scalar series / factorized analytic expansion
 -> termwise 2x2 Cayley-Hamilton lift
 -> target-first General-D15 exact moments
 -> finite partial sum at source/target engineering convergence
```

Key principle:

```text
INFINITE_CONVERGENT_MATERIAL_SERIES = ALLOWED
EACH_STRUCTURAL_TERM_HAS_FINITE_EXACT_INTEGRAL = REQUIRED
FORMAL_SPATIAL_QUADRATURE = 0
BLIND_GLOBAL_N_ESCALATION = NOT THE GOVERNING STRATEGY
```

The new compiler must be validated by same-state source consistency against raw R10, not by fitting the final Z6 capacity to Zhou/experiment.

## Current artifacts

- `semantic_v2/10_governance/20260817_1337__NZSCCM__Z6_RECTANGULAR_AIRY_AND_COMPILER_REORGANIZATION__LOCK.md`
- `semantic_v2/20_theory/nc_steel_shell_panel/20260817_1337__NZSCCM__RECTANGULAR_AIRY_SCALAR_AND_CONVERGENT_SERIES_FINITE_MOMENT_COMPILER__THEORY.md`
- `semantic_v2/40_execution/steel_shell/20260817_1337__NZSCCM__Z6_RECTANGULAR_AIRY_DIRECT_R10_AND_N48_FIXED_STATE_GATE__EXECUTION_REPORT.md`
- `semantic_v2/40_execution/steel_shell/20260817_1337__NZSCCM__Z6_RECTANGULAR_AIRY_DIRECT_R10_AND_N48_FIXED_STATE_GATE__PARAMS_AND_INTERMEDIATES.json`
- `semantic_v2/40_execution/steel_shell/20260817_1337__NZSCCM__Z6_RECTANGULAR_AIRY_AND_COMPILER_GATE__REPRO.py`

## Next gate

```text
CURRENT_NEXT_TASK = Z6_CONVERGENT_SERIES_FINITE_MOMENT_MATERIAL_COMPILER
```

No formal Z6 ultimate-load value shall be released until that compiler passes same-state value/tangent target convergence and the coupled branch is rerun.
