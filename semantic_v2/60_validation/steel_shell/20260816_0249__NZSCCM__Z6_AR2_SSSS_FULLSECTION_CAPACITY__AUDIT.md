# NZ-SCCM — audit: Z6 AR2 theoretical SSSS full-section capacity

**Timestamp:** 2026-08-16 02:49 +08:00

## Scope

Audit the Z6 ultimate-capacity computation after the user explicitly fixed the analytical boundary scope to **theoretical four-edge simply supported**, rather than Zhou FE-specific translational restraints.

## Boundary identity

```text
THEORETICAL_FOUR_EDGE_SSSS = GOVERNING
NAVIER_ONE_COMPLETE_HALFWAVE = GOVERNING
ZHOU_FE_UX_UY_IMPLEMENTATION = OUT_OF_SCOPE
FE_BOUNDARY_DETOUR_0016_TO_0121 = SUPERSEDED_FOR_Z6_PRODUCTION
```

No `c` end-warp, PF end layer, axial-trace condensation, or free `p20,p02` coordinate appears in the production strain field.

## Spatial-integration audit

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
Gauss = 0
Simpson = 0
adaptive spatial integration = 0
spatial collocation = 0
material-point grid = 0
```

N48 compiler nodes and steel-cap coefficient nodes are one-dimensional material-coordinate coefficient-generation objects, not structural spatial integration points.

## Full-section identity

The current result contains:

1. effective concrete core `(1-rho_w) Pc`;
2. both face steel plates `Ps`;
3. equivalent longitudinal web/PBL steel phase `Pw` with `rho_w=.02`.

At the degree-48 final state:

```text
Pc_eff = 20.72760903 MN
Ps     = 21.59547236 MN
Pw     =  8.97221193 MN
Pu     = 51.29529333 MN
```

The component sum closes to the reported load.

## Equilibrium audit

Final local state:

```text
D  = 1.5853259043
q  = 0.02166488056895
Rq = -311.161 N mm
```

Component generalized works are of order several `10^9 N mm`; using their absolute sum gives

`Rnorm ~= 1.36e-8`,

well inside the existing `1e-5` production residual scale.

## Branch topology audit

The connected positive-q branch in the fixed compiler interval gives

```text
D=1.56  P=51.23273135 MN
D=1.58  P=51.31276663 MN
D=1.60  P=51.28835746 MN
```

at the degree-40 locator level. Therefore the load increases before the local maximum and decreases after it. The first local `+ -> -` maximum in the capacity neighborhood is around `D=1.585`.

Degree-48 steel/web coefficient refinement at this peak changes the load by only about `-0.0202 MN`, yielding `51.2953 MN`; the engineering-rounded capacity remains `51.30 MN`.

This audit does not use Zhou/Winter values in root selection.

## Compiler-domain audit

Declared interval:

`lambda in [-2.35,+1.90]`.

Final reachable envelope:

```text
lambda_min = -2.2936943231
lambda_max = +1.8232424497
```

Coverage margins are positive on both sides, so the final state is inside the declared hull.

The full-hull N48-C1/MM fidelity diagnostics are not small on this wide interval; in particular the T value error is about `0.7046`. The frozen production contract explicitly treats full-hull errors as fidelity information and does not define a universal reject threshold. This audit therefore records the wide-hull compiler fidelity as the dominant representation uncertainty instead of creating a new blocker.

## Comparator audit

Comparators were read only after the theoretical state was determined:

```text
Pcr_AR2               = 39.2880147150 MN
Pyth_full              = 88.089888 MN
Zhou Eq.(5-87)/(5-88) = 49.4867667519 MN
Winter                 = 50.1858541295 MN
```

Current result:

```text
Pu/Pcr      = 1.30562
Pu/Pyth     = 0.58231
vs Zhou     = +3.65%
vs Winter   = +2.21%
```

No calibration is present.

## Historical-value identity

```text
40.97334 MN Gauss/free-p20-p02 result = RETRACTED / INVALID
44.552919 MN old reduced q-only result = HISTORICAL AUDIT ONLY
51.30 MN = CURRENT FOUR-EDGE-SSSS FULL-SECTION Z6 CAPACITY
```

## Verdict

```text
Z6_THEORETICAL_FOUR_EDGE_SSSS_SCOPE = PASS
ZERO_SPATIAL_INTEGRATION = PASS
FULL_SECTION_WEB_PHASE_INCLUDED = PASS
POSITIVE_CONNECTED_BRANCH = PASS
FIRST_LOCAL_PLUS_TO_MINUS_MAXIMUM = LOCATED
FINAL_GENERALIZED_EQUILIBRIUM = PASS
COMPILER_INTERVAL_COVERAGE = PASS
COMPILER_WIDE_HULL_FIDELITY = RECORDED_UNCERTAINTY
STRUCTURAL_CALIBRATION = NONE
CURRENT_Z6_Pu = 51.30 MN
```

The Z6 capacity task is no longer blocked by FE-boundary reverse engineering.