# NZ-SCCM governance — restore the proven N48 compiler → Cayley–Hamilton → D15 path for Case21 Airy-scalar

**Timestamp:** 2026-08-17 13:04 +08:00  
**Status:** CONTROLLING CORRECTION / SAME END-TO-END TASK

## 1. User correction accepted

The recent raw-R10 `64-state/16-state/semialgebraic-period` work silently strengthened the formal requirement from

```text
source-controlled finite analytic material compiler
 -> exact zero-spatial structural moment contraction
```

to

```text
raw R10 positive-part/square-root expression
 -> direct theorem-level whole-domain exact period evaluation.
```

That strengthening was not required by the user and is no longer the production route.

The current end-to-end task remains

```text
CASE21_AIRY_SCALAR_FORMAL_ZERO_SPATIAL_ULTIMATE_LOAD
```

No new project task is created.

## 2. Production chain restored

```text
frozen R10 source
 -> frozen Case21 N48-C1/MM U,C,T,T7 material compiler on [-1.15,+0.12]
 -> 2x2 Cayley-Hamilton matrix lift
 -> Nguyen + Airy-scalar finite trigonometric strain field
 -> General-D15 exact structural moments
 -> exact elastic reinforcement contribution
 -> connected (D,q,lambda) equilibrium branch
 -> first load maximum
 -> Case21 formal zero-spatial Pu
```

The material compiler nodes remain one-dimensional material-coordinate operations, not structural spatial points.

Formal counters remain

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```

## 3. Why Airy does not require a new integration theory

The Airy scalar only changes the finite continuous strain field by adding

```text
1, cos(2X), cos(2Y), cos(2X)cos(2Y), sin(2X)sin(2Y)
```

terms. After `cos^2=1-sin^2` and the common `cosX cosY` factor in shear are handled algebraically, every final scalar target remains a finite sum of

\[
\sin^pX\cos^rX\sin^uY\cos^sY\zeta^h,
\]

which is exactly the existing General-D15 moment class.

The Cayley-Hamilton recurrence is unchanged; only its finite polynomial invariants acquire additional Airy coefficients.

## 4. Compiler-domain compatibility

The old compiler interval is

```text
[-1.15,+0.12].
```

The already-certified current Airy peak envelope lies approximately inside

```text
lambda_plus  in [-0.094,+0.095]
lambda_minus in [-0.882,-0.693]
```

and is therefore strictly contained in the old compiler interval. No new material interval is required.

## 5. Status of the 11:55 semialgebraic-period branch

The 11:55 source identities and 16-state algebraic classification remain valid mathematical diagnostics, but they are demoted from production governance:

```text
RAW_R10_DIRECT_SEMIALGEBRAIC_PERIOD = RESEARCH_DIAGNOSTIC_ONLY
RAW_R10_DIRECT_PERIOD_RUNTIME = NOT_A_PRODUCTION_PREREQUISITE
N48_C1MM_CH_D15 = RESTORED_PRODUCTION_BASELINE
```

No files are deleted; provenance is preserved.

## 6. Formal release obtained in the companion execution

The restored path has been executed with the current Airy-scalar field. The formal N48-C1/MM + CH + D15 branch has a first local load maximum near

```text
D ≈ 0.77708
q ≈ 0.0018057
lambda ≈ 0.0434
Pu ≈ 365.257 kN
```

with the final equilibrium residuals at the refined peak neighborhood at the `10^-3 kN mm / 10^-5` level and no structural numerical quadrature.

The exact execution record and all intermediate values are stored in the 13:04 execution report and JSON.
