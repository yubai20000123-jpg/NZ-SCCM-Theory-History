# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-15 19:34 +08:00  
**Status:** LEGACY MUTABLE POINTER ONLY

## Z6 aspect-ratio comparator correction

For the fixed Z6 section/material parameters

```text
b=12000 mm, h=130 mm, ns=60, ls=200 mm, ts=4 mm
fy=355 MPa, fcu=40 MPa, f'c=30.4 MPa
Ac=1,434,720 mm2, As=125,280 mm2
Pyth=88.089888 MN
```

changing only a gives:

```text
a/b=0.75: Pcr=42.83147561 MN, lambda=1.43410685
a/b=1.00: Pcr=39.28801472 MN, lambda=1.49738331
a/b=1.25: Pcr=41.04137379 MN, lambda=1.46504878
```

This is the classical m=1 energy trend: 0.75 -> 1.00 reduces Pcr by 8.273%, then 1.00 -> 1.25 raises Pcr by 4.463%.

Using Zhou Eq.5-87/5-88 FE-fitted lower-envelope:

```text
Pu_Zhou_fit: 49.67243594 -> 49.48676675 -> 49.50839695 MN
```

Using Zhou Eq.5-86 Winter curve:

```text
Pu_Winter: 52.00198798 -> 50.18585413 -> 51.09851222 MN
```

Therefore:

```text
ZHOU_ELASTIC_Pcr_ASPECT_RESPONSE = ENERGY-CONSISTENT
WINTER_Pu_ASPECT_RESPONSE = CLEAR CLASSICAL-LIKE DOWN-THEN-UP TREND
ZHOU_EQ5_87_5_88_Pu_ASPECT_RESPONSE = LOCALLY FLAT DUE TO FITTED phi(lambda)
ZHOU_FIT_Pu_MUST_NOT_BE_USED_ALONE_AS_ENERGY_DIAGNOSTIC
```

The original Z6 `49.6724359 MN` remains a Zhou FE-fitted lower-envelope design value, not a recovered raw FE load and not a pure energy-method ultimate load.

Latest artifacts:

- `semantic_v2/50_results/steel_shell/20260815_1934__Z6__ASPECT_RATIO_ZHOU_VS_WINTER_FROM_BASIC_PARAMETERS__RESULT.csv`
- `semantic_v2/60_validation/steel_shell/20260815_1934__NZSCCM__Z6__ASPECT_RATIO_ZHOU_VS_WINTER_BASIC_PARAMETER_AUDIT.md`

## Boundary-compatible in-plane current path

Previous N=1 admissible warp remains valid. Full current checkpoints currently retained:

```text
D=.50: q=.007244279, c=-.01545635, P=37.34514 MN, certified coupled checkpoint
D=.55: q=.008198205, c=-.02004071, P=38.41062 MN, connected near-equilibrium
D=.60: q=.009177472, c=-.02655088, P=39.12698 MN, connected near-equilibrium
```

Corrected Z6 Pu is still NOT SOLVED. Current next implementation remains directional moment-first contraction of `P,Rq,Rc` and the local `(q,c)` Jacobian from the D=.60 connected state.

Frozen parent identity:

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order kinematics
R10 / N48-C1-MM / Cayley-Hamilton / General D15 unchanged
A0=a/500
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
no Zhou/Winter calibration
no out-of-plane multimode expansion
```
