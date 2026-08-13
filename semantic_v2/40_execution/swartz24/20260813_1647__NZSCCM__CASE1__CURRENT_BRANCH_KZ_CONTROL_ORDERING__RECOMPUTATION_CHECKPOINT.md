# NZ-SCCM Case1 — current branch / KZ control-ordering recomputation checkpoint

**Timestamp:** 2026-08-13 16:47 +08:00  
**Identity:** CURRENT EXECUTION CHECKPOINT / EXPLICIT BLANKS ALLOWED / NO RESULT FABRICATION

## 1. Fixed theory identity

```text
R10_MATERIAL_TARGET = FROZEN
U/C/T7 = N48-C1
T = N48-C1-CONSTRAINED-MINIMAX
CAYLEY_HAMILTON = GOVERNING
KINEMATICS = NGUYEN_SECOND_ORDER
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
D15 = GENERAL TRIGONOMETRIC EXACT MOMENTS
FORMAL_SPATIAL_SAMPLING = 0
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_SPATIAL_SUBDOMAINS = 1
STRUCTURAL_CALIBRATION = NO
```

## 2. Known Case1 records

Experimental failure load, used only for post-calculation comparison:

```text
Pf_exp = 490.194022001707 kN
```

Historical direct-N48 first load maximum:

```text
D_L_directN48 = 0.994049227092674
q_L_directN48 = 0.000773995088472599
P_L_directN48 = 599.515895352265 kN
error_vs_Pf = +22.3017557 %
```

Stored current C1/MM + general-D15 first-load-maximum value:

```text
P_L_current = 608.925000000000 kN
error_vs_Pf = +24.2212210 %
```

At the historical direct-N48 state, the tangent-repair diagnostic gives:

```text
eta_parallel_directN48 = 1.0552906913 E0
eta_parallel_C1        = 0.0044587769 E0
H_directN48            = 101515988.44 N mm
H_C1                   = 15417664.10 N mm
Zhou_margin_directN48  = 3.586092204
Zhou_margin_C1         = 0.831706848
```

These values establish a strong stiffness-reduction diagnostic, but they are not a substitute for current-branch full `K_Z`.

## 3. Current missing checkpoint fields

The following fields are intentionally left blank because the final Aug12–13 transient execution source/root was not recovered from GitHub or File Library in the 2026-08-13 search:

```text
D_L_current = <BLANK_NOT_YET_RECOVERED>
q_L_current = <BLANK_NOT_YET_RECOVERED>
A_L_current = <BLANK_NOT_YET_RECOVERED>
Pc_L_current = <BLANK_NOT_YET_RECOVERED>
Ps_L_current = <BLANK_NOT_YET_RECOVERED>
Rq_norm_L_current = <BLANK_NOT_YET_RECOVERED>
L_norm_L_current = <BLANK_NOT_YET_RECOVERED>

D_KZ0_current = <BLANK_NOT_YET_COMPUTED>
q_KZ0_current = <BLANK_NOT_YET_COMPUTED>
P_KZ0_current = <BLANK_NOT_YET_COMPUTED>
KZ_sign_before = <BLANK_NOT_YET_COMPUTED>
KZ_sign_after = <BLANK_NOT_YET_COMPUTED>

CONTROL_EVENT = <UNRESOLVED>
GOVERNING_P_CURRENT = <UNRESOLVED>
```

No old root is inserted into these fields.

## 4. Mandatory recomputation sequence

1. Rebuild Case1 current material coefficients from its raw material input and frozen compiler rules.
2. Rebuild the current `P(D,q), R_q(D,q)` general-D15 evaluator.
3. Pass an independent Case21 regression before Case1 production use.
4. Trace the Case1 primary connected equilibrium branch from `(0,0)` without experimental root selection.
5. Freeze the first `P` +→− load maximum and all residual/derivative fields.
6. Evaluate full same-expression `K_Z` on the same branch.
7. Locate the first `K_Z=0` event, if present.
8. Select the earlier physical control event.
9. Only then compare the governing current load with `Pf_exp`.

## 5. Fail-safe rule

If the current structural backend cannot pass the Case21 regression, stop with the missing fields above still blank. Recalculation may be retried later with a recovered or reconstructed coefficient-space backend, but no spatial Gauss/Simpson/collocation/material-point fallback obtains production identity.

## 6. Current checkpoint verdict

```text
CASE1_CURRENT_LIMIT_POINT_LOAD_RECORD = PRESENT
CASE1_CURRENT_LIMIT_POINT_STATE = NOT_YET_RECOVERED
CASE1_CURRENT_FULL_KZ_ORDERING = NOT_YET_COMPUTED
CASE1_608p925_AS_GOVERNING_Pu = HOLD
BLANK_FIELDS_AUTHORIZED = YES
RECALCULATION_IF_NEEDED = AUTHORIZED
```
