# NZ-SCCM — 单半波 FvK 最小膜力重分布补全门禁

**Timestamp:** 2026-08-15 21:34 +08:00  
**Identity:** THEORY-SPACE AUDIT + MINIMAL SYSTEM CONSTRUCTION ONLY  
**Pu status:** NO NEW Pu / NO NEW ROOT / NO D>0.60 CONTINUATION

## 1. Frozen parent identity

Unchanged:

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order kinematics
R10 / N48-C1-MM / Cayley-Hamilton
General D15 exact structural moments
A0=a/500
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
no Zhou/Winter calibration
no out-of-plane multimode expansion
```

This gate does not change any material law, current-map coefficient, shell law, initial imperfection or formal integration rule.

## 2. Decision from the 21:18 Nguyen/FvK audit

The existing `D+q+c` formulation already contains Nguyen Eq.(6.3) second-order geometric terms and the `c` boundary-admissible in-plane warp. However, exact harmonic-span audit shows that its retained in-plane virtual space cannot exactly span the two independent second-harmonic membrane-redistribution directions forced by the single `(1,1)` out-of-plane halfwave.

Therefore:

```text
DQC_EXACT_SINGLE_HALFWAVE_POSTBUCKLING_MEMBRANE_COMPLETENESS = FAIL
CAUSE = FUNCTION-SPACE RANK DEFICIENCY, NOT MATERIAL OR D15
```

This conclusion is independent of any new Pu calculation.

## 3. Minimal authorized completion

Retain the existing boundary coordinate `c` and add exactly two dimensionless in-plane generalized coordinates:

```text
p20 = admissible in-plane direction carrying the missing X-second-harmonic content
p02 = admissible in-plane direction carrying the missing Y-second-harmonic content
```

No new out-of-plane coordinate is authorized in this gate.

The minimal membrane unknown vector at fixed `(D,q)` is

```text
m = [c, p20, p02]^T
```

with residuals

```text
Rm = [Rc, R20, R02]^T = 0.
```

The out-of-plane equilibrium remains

```text
Rq = 0.
```

## 4. Matrix-size governance

The implementation shall use a flat `3x3` membrane Jacobian

```text
Jmm = d(Rc,R20,R02)/d(c,p20,p02)
```

and statically/directionally condense the membrane variables into the scalar out-of-plane equation. A monolithic nested block-matrix theory is not authorized.

At the tangent level:

```text
dm/dq = -Jmm^{-1} Jmq
Lcond = Rq,q - Rq,m Jmm^{-1} Jm,q
```

This preserves the project's low-dimensional flat-matrix discipline.

## 5. Formal integration identity

Every new virtual-strain field is a finite polynomial in `sin X`, `sin Y` (and no new thickness dependence). Therefore the existing D15 exact-moment contraction remains the governing structural integral engine.

```text
NEW_STRUCTURAL_SPATIAL_POINTS = 0
NEW_GAUSS_SIMPSON_CELLS = 0
D15_FORM = UNCHANGED
```

## 6. What is not yet claimed

This gate establishes the **minimum FvK-source-complete Ritz membrane space**, not proof that two added coordinates are the globally exact solution of the full nonlinear in-plane PDE for all states.

Before any new Pu is released, the next execution must first evaluate `R20` and `R02` on already accepted Z6 states using the unchanged current stress operator and D15 moments, then solve the membrane subsystem only if those projections are materially nonzero.

```text
CURRENT_NEXT_EXECUTION = EXISTING_STATE_R20_R02_D15_PROJECTION_GATE
NEW_Pu_BEFORE_GATE = PROHIBITED
```