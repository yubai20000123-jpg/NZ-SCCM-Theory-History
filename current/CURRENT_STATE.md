# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-15 19:55 +08:00  
**Status:** LEGACY MUTABLE POINTER ONLY

## Z6 aspect-ratio comparator correction

For the fixed Z6 section/material parameters

```text
b=12000 mm, h=130 mm, ns=60, ls=200 mm, ts=4 mm
fy=355 MPa, fcu=40 MPa, f'c=30.4 MPa
Ac=1,434,720 mm2, As=125,280 mm2
Pyth=88.089888 MN
```

changing only a gives the established energy check:

```text
a/b=0.75, m=1: Pcr=42.83147561 MN, lambda=1.43410685
a/b=1.00, m=1: Pcr=39.28801472 MN, lambda=1.49738331
a/b=1.25, m=1: Pcr=41.04137379 MN, lambda=1.46504878
```

The Zhou elastic Pcr response is energy-consistent. Zhou Eq.5-87/5-88 is an FE-fitted lower-envelope and must not be used alone as an energy diagnostic; Winter preserves clearer Pcr sensitivity.

## New a/b=1 versus a/b=2 gate

For a/b=2 the controlling integer halfwave count is m=2. Hence:

```text
a/b=1: a=12000, m=1, ell=a/m=12000 mm
a/b=2: a=24000, m=2, ell=a/m=12000 mm
```

The two cases therefore have the same complete representative halfwave geometry and identical Zhou elastic stability input:

```text
Pcr = 39.288014715 MN
lambda_n = 1.49738330617
```

Three-way comparison:

```text
                    a/b=1             a/b=2
NZ-SCCM R10 continuum audit  44.58066266 MN    44.55291911 MN
Zhou Eq.5-87/5-88            49.48676675 MN    49.48676675 MN
Winter Eq.5-86               50.18585413 MN    50.18585413 MN
```

The NZ-SCCM audit difference is only about 0.062%, supporting the user's expectation that a/b=1 and a/b=2 should be energetically equivalent/nearly equivalent when the correct integer mode m=2 is used for a/b=2.

Important identity of the NZ-SCCM numbers:

```text
R10_DIRECT_CONTINUUM_AUDIT_ONLY
```

The formal single-interval N48 compiler exits its frozen valid material range on these high-amplitude modified branches. Broadening one N48 interval produces unacceptable scalar T approximation error, so those broad-N48 values were rejected. The reported 44.58/44.55 MN values come from direct evaluation of the frozen R10 current map with high-order continuum quadrature solely as an audit backend; they are not a release of a formal spatial-quadrature production operator. Formal project identity remains N_formal_spatial_quadrature=0.

Latest aspect artifacts:

- `semantic_v2/50_results/steel_shell/20260815_1955__Z6_AR1_AR2__NZSCCM_ZHOU_WINTER_COMPARISON__RESULT.csv`
- `semantic_v2/40_execution/steel_shell/20260815_1955__Z6_AR1_AR2__R10_CONTINUUM_AUDIT_CONVERGENCE.csv`
- `semantic_v2/60_validation/steel_shell/20260815_1955__NZSCCM__Z6__AR1_AR2_THREE_WAY_CAPACITY_AUDIT.md`

## Boundary-compatible in-plane current path

Previous N=1 admissible warp remains valid. Full current checkpoints currently retained:

```text
D=.50: q=.007244279, c=-.01545635, P=37.34514 MN, certified coupled checkpoint
D=.55: q=.008198205, c=-.02004071, P=38.41062 MN, connected near-equilibrium
D=.60: q=.009177472, c=-.02655088, P=39.12698 MN, connected near-equilibrium
```

Corrected original-Z6 Pu is still NOT SOLVED. Current next formal implementation remains directional moment-first contraction of `P,Rq,Rc` and the local `(q,c)` Jacobian from the D=.60 connected state.

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
