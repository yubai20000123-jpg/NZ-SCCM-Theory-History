# NZ-SCCM Case1 — compiler value shift and full-field KZ reconstruction audit

**Date:** 2026-08-13  
**Time:** TUNK  
**Identity:** RECONSTRUCTION AUDIT / AUDIT-ONLY SPATIAL CROSSCHECK / NO PRODUCTION PROMOTION

## 0. Why this audit was run

The Case1 prediction changed from the historical direct-N48 first load maximum

\[
P_{L,old}=599.515895352\ \mathrm{kN}
\]

(error +22.3018% versus the same experimental failure load) to the stored current C1/MM + general-D15 first-load-maximum value

\[
P_{L,current}=608.925\ \mathrm{kN}
\]

(error +24.2212%).

The mechanical objection is important: if the tangent stiffness was repaired downward, a stability loss might be reached before the later high-load state, so a later load maximum must not be accepted blindly.

The previous 16:47 control-ordering audit correctly reopened this gate. The present audit goes one step further and reconstructs the missing Case1 state and the full-field modal tangent as an independent numerical crosscheck.

## 1. Formal / audit boundary

The governing production theory remains unchanged:

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
R10 -> N48-C1/MM -> Cayley-Hamilton -> Nguyen second-order -> general-D15
FORMAL_SPATIAL_SAMPLING = 0
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_SPATIAL_SUBDOMAINS = 1
```

The reconstruction in this file deliberately uses a high-order physical-space Gauss rule only as an **AUDIT-ONLY independent evaluator**. It does not obtain theory identity, does not replace D15, and is not used to calibrate any parameter.

The audit evaluator was benchmarked against the frozen Case21 current state using the frozen material-coefficient identity; it reproduced the Case21 load and full-field KZ to the small numerical discrepancy expected of an independent audit evaluator. Therefore it is used here only to recover the missing Case1 branch state and diagnose the direction of the discrepancy.

## 2. Current Case1 input used

```text
b = ell = 1220 mm
t = 25.4 mm
fc = 22.81 MPa
E0 = 21730 MPa
eps0 = 0.00210
nu = 0.18
q0 = 1/400
rho_s,x = rho_s,y = 0.001
one mid-plane reinforcement layer
Es = 200000 MPa
eps_y = 0.00265
fy = 530 MPa
compiler interval = [-1.12, 0.105]
```

No experimental load was used to generate coefficients, trace the branch, locate the load maximum, or evaluate KZ.

## 3. Material compiler was regenerated from the frozen rules

The audit regenerated:

```text
U   = N48-C1
C   = N48-C1
T7  = N48-C1
T   = N48-C1 constrained minimax
```

from the R10 source functions and the Case1 compiler interval.

This is important because the diagnosis cannot be made by inserting the old direct-N48 coefficients into the current structural equations.

## 4. Reconstructed current Case1 first load maximum

Tracing the positive connected `Rq=0` branch with the regenerated current compiler gives the independent audit reconstruction

\[
\boxed{D_L^{audit}\approx0.98833818},
\]

\[
\boxed{q_L^{audit}\approx8.3313173\times10^{-4}},
\]

\[
\boxed{P_L^{audit}\approx608.92642\ \mathrm{kN}}.
\]

The stored current result is 608.925 kN, so the independently reconstructed load agrees to about 0.0014 kN. The small difference is consistent with an independently regenerated constrained-minimax coefficient set and audit-only numerical integration.

The old direct-N48 limit state was

\[
D_{L,old}=0.9940492271,
\qquad
q_{L,old}=0.0007739951.
\]

Thus the current reconstructed maximum is actually reached at

\[
\boxed{\Delta D\approx-0.00571104=-0.5745\%},
\]

while

\[
\boxed{\Delta q\approx+7.6404\%}.
\]

So the later compiler did **not** push Case1 to a larger mean compression coordinate before the load maximum. In the generalized compression coordinate D, the maximum occurs slightly earlier.

## 5. Direct decomposition of why P nevertheless increased

This is the key reconstruction.

At the **same old direct-N48 state**

\[
(D,q)=(0.9940492271,0.0007739951),
\]

the audit exactly reproduces the old direct-N48 load:

\[
\boxed{P_{directN48}=599.51589536\ \mathrm{kN}}.
\]

Now replace only the material compiler by the current C1/MM compiler while keeping the same D and q fixed. The axial load becomes

\[
\boxed{P_{C1/MM\ at\ old\ state}=618.67743205\ \mathrm{kN}}.
\]

Therefore the compiler value change by itself raises the axial resultant by

\[
\boxed{+19.16153669\ \mathrm{kN}=+3.19617\%}.
\]

But that frozen old state is no longer a current equilibrium state. Its reconstructed current residual is approximately

\[
\boxed{R_q\approx-453.13\ \mathrm{kN\,mm}},
\]

so the branch must re-equilibrate.

Moving from that frozen old state to the reconstructed current equilibrium load maximum reduces the load by

\[
\boxed{-9.75100795\ \mathrm{kN}\approx-1.57611\%}.
\]

The net change is therefore

\[
\boxed{+9.41052874\ \mathrm{kN}\approx+1.56969\%},
\]

which is the observed old-to-current Case1 increase to numerical audit accuracy.

### Interpretation

The apparent paradox is resolved:

```text
current limit state occurs earlier in D
BUT
C1/MM changes the stress-value field, not only the tangent
AND
that value-field increase is larger than the load reduction caused by re-equilibration
THEREFORE
P_L rises even though D_L falls.
```

So `N48-C1/MM` cannot be interpreted as a pure stiffness correction.

## 6. Full-field KZ audit

The earlier Zhou-form center-state diagnostic gave, at the old direct-N48 state:

```text
Zhou margin direct N48 = 3.58609
Zhou margin C1         = 0.83171
```

This correctly shows that the **center / lambda≈0 tangent proxy** falls sharply when C1 is imposed.

However, the governing theory uses the complete-halfwave integral

\[
K_Z=K_{Z,c}^{mat}+K_{Z,c}^{geo}+K_{Z,s}^{mat}+K_{Z,s}^{geo},
\]

not the center proxy alone.

The independent full-field audit gives at the old direct-N48 state:

```text
direct-N48 full-field KZ ≈ +3142.70 N/mm
current C1/MM evaluated at the same old state ≈ +3567.59 N/mm
```

At the reconstructed current Case1 load maximum:

```text
KZ,c^mat  ≈ +4322.43 N/mm
KZ,c^geo  ≈ -1234.75 N/mm
KZ,s^mat  = 0                # mid-plane reinforcement
KZ,s^geo  ≈   -20.99 N/mm
--------------------------------
KZ,total  ≈ +3066.68 N/mm
```

Therefore the reconstructed current load maximum is **not** close to a full-field modal tangent zero.

A 15-state audit trace on the connected current branch from D=0.05 to the reconstructed maximum kept KZ positive at every checked state; the tabulated audit values are stored in the companion CSV. The sampled KZ values are roughly +1.96e3 to +3.84e3 N/mm and remain +3.07e3 N/mm at the load maximum.

This does not constitute the formal D15 proof of absence of a zero between audit states, but it provides strong evidence against the hypothesis that the current Case1 branch has already crossed KZ=0 before 608.9 kN.

## 7. Why the center stiffness can fall while full-field KZ does not

The C1 constraint is exact at the material coordinate lambda=0:

```text
value and first derivative at lambda=0 = repaired
```

It is **not** a global first-derivative fidelity constraint over the full compiler interval.

The current production contract itself records, for Case21, very large full-hull scaled derivative errors for some primitives while retaining the exact zero-point C1 anchors. The present Case1 audit likewise finds large off-origin derivative discrepancies in the finite compiler representation.

Audit-only scaled full-interval derivative metrics for Case1 are approximately:

| primitive | lambda_h * max |F48' - FR10'| |
|---|---:|
| U | 1.48 |
| C | 3.81 |
| T | 187.44 |
| T7 | 14.33 |

These numbers are diagnostic, not new acceptance thresholds. Their significance is narrower:

> exact C1 fidelity at lambda=0 does not imply that the current tangent field is R10-faithful over all material states occupied by the plate.

Hence a center-state Zhou proxy can decrease dramatically while the integrated complete-halfwave KZ remains strongly positive.

## 8. Revised root-cause diagnosis for the Case1 worsening

The evidence now supports the following ordering:

1. **direct N48 had a real tangent-fidelity defect at lambda=0**; repairing it was justified;
2. **C1/MM was not a tangent-only repair** — it also changed primitive values over the interval;
3. in Case1, that value change raises the axial stress resultant strongly at fixed state;
4. the current equilibrium/load maximum shifts to slightly lower D, but the re-equilibration reduction is smaller than the value-field increase;
5. the full-field current KZ audit remains strongly positive at the reconstructed current maximum;
6. therefore the Case1 increase from 599.516 to 608.925 kN is presently best attributed to the **finite analytic compiler value/tangent trade-off away from the C1 anchor**, not to an earlier full-field tangent loss being ignored.

This is a materially different conclusion from saying merely "stiffness decreased, so Pu should decrease". That statement would be correct only if the relevant complete-halfwave governing tangent had actually fallen through zero first.

## 9. Formal-production status

The audit has reconstructed the missing Case1 state very closely, but the final production promotion is deliberately withheld:

```text
CASE1_CURRENT_LIMIT_POINT_STATE_RECONSTRUCTED = YES / AUDIT_ONLY
CASE1_CURRENT_LIMIT_POINT_LOAD_REPRODUCED = YES / AUDIT_ONLY
CASE1_FULL_FIELD_KZ_PRELIMIT_ZERO_EVIDENCE = NOT_SEEN_IN_AUDIT
CASE1_KZ_AT_LOAD_MAX = STRONGLY_POSITIVE_IN_AUDIT
FORMAL_ZERO_SPATIAL_GENERAL_D15_CASE1_KZ = STILL_PENDING
CASE1_608p925_GOVERNING_Pu_PRODUCTION_PROMOTION = HOLD UNTIL FORMAL_D15_KZ
```

A direct coefficient-space re-expansion was started, but the current runtime does not yet contain the recovered transient Aug12–13 production backend. A naive sparse prototype grows to tens of thousands of analytic monomials even before the complete interaction+tangent contraction, so this file does not pretend that the formal D15 KZ has been regenerated.

Per project fail-safe policy, the formal KZ field remains blank rather than being replaced by the Gauss audit.

## 10. No calibration

```text
R10_CHANGED = NO
N48_ORDER_CHANGED = NO
STRUCTURAL_Pu_BACKFIT = NO
EXPERIMENT_USED_FOR_ROOT_SELECTION = NO
EXPERIMENT_USED_FOR_COEFFICIENT_GENERATION = NO
FORMAL_SPATIAL_QUADRATURE_CHANGED = NO
```

The immediate technical target is now sharply defined: regenerate **the same current Case1 state and full-field KZ with the zero-spatial general-D15 coefficient engine**, then decide production control ordering without changing the material model to chase the experiment.
