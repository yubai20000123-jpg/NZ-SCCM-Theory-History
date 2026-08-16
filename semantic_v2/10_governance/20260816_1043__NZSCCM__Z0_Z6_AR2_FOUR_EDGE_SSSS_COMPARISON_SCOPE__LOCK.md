# NZ-SCCM — Z0–Z6 AR2 four-edge simply-supported comparison scope lock

**Timestamp:** 2026-08-16 10:43 +08:00  
**Status:** CURRENT GOVERNANCE LOCK

## User decision carried forward

1. The previously obtained Z6 four-edge simply-supported result `Pu = 51.30 MN` is accepted and retained.
2. Z0–Z5 are to be recalculated by the same production process, with each physical panel geometry changed only so that `a/b = 2`.
3. Zhou's analytical/empirical capacity formula and Winter formula are to be evaluated for those same modified parameters, strictly as post-solve comparators.
4. Calculation process and intermediate parameters are to be preserved in GitHub.

## Governing boundary and computation

```text
PRODUCTION_BOUNDARY = THEORETICAL_FOUR_EDGE_SIMPLY_SUPPORTED
ZHOU_FE_UX_UY_REVERSE_ENGINEERING = OUT_OF_SCOPE
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
Nguyen second-order kinematics = ACTIVE
R10/N48-C1-MM/Cayley-Hamilton = ACTIVE
General D15 exact moments = ACTIVE
A0 = a/500
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
```

No PF/end-warp/axial-trace FE correction and no free `p20,p02` membrane coordinate enters the production field.

## Modified AR2 geometry

Only `a` is changed to enforce `a=2b`; all other specimen parameters retain their source values.

```text
case  b(mm)  a_new(mm)  a/b  m*  ell=a/m*(mm)  A0=a/500(mm)  q0=A0/b
Z0    6000   12000      2    2   6000           24            .004
Z1    6000   12000      2    2   6000           24            .004
Z2    6000   12000      2    2   6000           24            .004
Z3    6000   12000      2    2   6000           24            .004
Z4    8000   16000      2    2   8000           32            .004
Z5    2000    4000      2    2   2000            8            .004
Z6   12000   24000      2    2  12000           48            .004
```

For Z0–Z5 and Z6, the selected representative complete halfwave is therefore square: `ell=b`.

## Comparator isolation

Zhou/Winter values must not enter:
- R10 parameters;
- N48-C1/MM coefficients;
- q-equilibrium;
- branch selection;
- peak location;
- steel/web cap coefficients.

They are read/evaluated only after the NZ-SCCM capacity is frozen.

## Interpretation boundary

Z0–Z5 with modified `a/b=2` are hypothetical geometry-adjusted comparison objects. They are not to be presented as direct reproductions of the original physical tests at their historical aspect ratios.
