# NZ-SCCM — Z6 length=24000 complete-halfwave and N48-family rebuild correction lock

**Timestamp:** 2026-08-17 14:07 +08:00  
**Status:** USER CORRECTION / SUPERSEDES 13:37 Z6=9000 INTERPRETATION

## 1. Controlling correction

The 13:37 interpretation `a=9000 mm, b=12000 mm, ell=9000 mm` is **wrong and superseded**.

The backup execution record already freezes the intended Z6 analytical object as

```text
a = 24000 mm
b = 12000 mm
a/b = 2
m* = 2
ell = a/m* = 12000 mm = b
A0 = a/500 = 48 mm
q0 = A0/b = 0.004
```

Therefore the production representative domain is still exactly **one continuous complete halfwave**, but the physical full plate contains two repeated halfwaves. The 9000-mm branch came from an earlier representative-parameter table and must not override the later user-confirmed AR2/Z6 backup state.

```text
Z6_FULL_LENGTH = 24000 mm
Z6_WIDTH = 12000 mm
Z6_HALFWAVE_COUNT = 2
ONE_FORMAL_HALFWAVE_LENGTH = 12000 mm
k=b/ell = 1
```

## 2. Membrane redistribution correction

The current Z6 calculation shall not use either of these as the physical production membrane closure:

- `r=0` / q-only membrane restraint;
- five fully independent membrane amplitudes solved by five free `Rm=0` equations.

The first omits the physically required postbuckling membrane-stress redistribution. The second was shown to over-release the membrane field and produced the historical direct-R10 value near `43.76284 MN`; it remains diagnostic history only.

The retained production-direction closure is the mechanically qualified Airy scalar subspace

\[
r=\lambda M a(\nu),
\qquad
M=\frac{\pi^2}{\varepsilon_0}\left(q_0q+\frac12q^2\right),
\]

and because `ell=b` for the correct Z6 representative halfwave,

\[
a(0.18)=[-0.295,-0.205,+0.25,-0.205,+0.25]^T.
\]

The coupled branch equations are

```text
Rq_base = 0
RA      = a^T Rm = 0
```

with reinforcement/steel/web phases present before the solve.

## 3. N48-family material rebuild

The old single fixed N48 compiled over the very wide `[-2.35,+1.90]` interval is not copied as-is. N48 is retained as the **prototype block size and source-constraint architecture**.

The rebuilt family is

```text
R10 scalar sources U,C,T,T7
 -> global C1-constrained Chebyshev source compiler
 -> cumulative family N=48,96,144,192,240,288
 -> 2x2 Cayley-Hamilton source lift
 -> finite analytic structural-moment target
```

The material compiler interval used for the corrected Z6 Airy peak neighborhood is

```text
lambda_material in [-1.75,+1.45]
```

which contains the connected first-peak branch with explicit margin.

The order is selected by **source/structural-target convergence only**, never by matching Zhou/Winter capacity.

## 4. Formal integration boundary

Project formal counters remain

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```

Direct continuum Gauss calculations are permitted only as an external mechanics/compiler oracle. They do not acquire formal-theory identity.

Each finite member of the N48-family is a finite polynomial/CH material representation and therefore remains termwise compatible with General-D15 exact moments. The present 14:07 execution uses the direct source/compiler oracle to establish the corrected Z6 branch and the required material order before promoting a high-block exact-moment runtime.

## 5. Current numerical engineering target

With the correct 24000-mm plate, `ell=12000 mm`, Airy scalar redistribution, full effective concrete + two faceplates + homogenized longitudinal web phase, the raw-R10 branch peaks near

```text
D ~= 1.362
q ~= 0.02648
lambda_Airy ~= 0.787
Pu_raw_R10_audit ~= 48.41 MN
```

The rebuilt N48-family converges toward the same result; N192-N288 give approximately `48.43 -> 48.42 MN` at the common audit resolution.

Therefore the old 43-MN result is not retained as current Z6 mechanics.

## 6. Comparator identity

For this corrected 24000-mm Z6 object, post-solve comparators remain

```text
Pcr_AR2 = 39.2880147150 MN
Zhou Eq.(5-87)/(5-88) = 49.4867667519 MN
Winter = 50.1858541295 MN
```

They do not enter material coefficients, branch choice, or root selection.
