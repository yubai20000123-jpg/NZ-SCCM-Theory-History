# NZ-SCCM Swartz24 — limit-point vs tangent-loss control-ordering correction audit

**Timestamp:** 2026-08-13 16:47 +08:00  
**Identity:** CURRENT CONTROL-ORDERING AUDIT / SEMANTIC CORRECTION / NO THEORY OR NUMERICAL VALUE CHANGE

## 0. Trigger

The current Swartz24 comparison table contains 24 equilibrium-branch load maxima obtained from the `R_q=0, L=0, first +->- maximum` route. A mechanical objection was raised for Case1: after repairing the material tangent from direct N48 to R10-faithful N48-C1/MM, tangent stiffness is much lower, so a tangent-stability loss may occur before the later load maximum. If so, the later load maximum cannot be called the governing physical ultimate load.

This audit checks that objection against the governing contract and preserved execution evidence. It does not recalibrate any material parameter and does not modify any stored load value.

## 1. Governing production rule already requires event ordering

The current 2026-08-12 22:45 theory/execution contract defines the full-field Zhou/Navier modal tangent

\[
K_Z=K_{Z,c}^{mat}+K_{Z,c}^{geo}+K_{Z,s}^{mat}+K_{Z,s}^{geo}.
\]

On the same primary equilibrium branch, the contract requires checking whether `K_Z=0` occurs before the first `L=0, g:+->-` load maximum. The first load maximum retains governing limit identity only when no earlier tangent loss occurs. If tangent loss occurs first, the true control ordering must be reported.

Therefore `L=0` is not, by itself, sufficient to certify governing physical capacity when the full tangent-stability gate is active.

## 2. Current Swartz24 execution package has not completed that ordering for 23/24 panels

The 2026-08-13 10:35 bulk-gate audit records:

```text
CASE21_FULL_L_KZ_GATE = PASS
SWARTZ24_CURRENT_Pu = 24/24 AVAILABLE
SWARTZ24_CURRENT_ROOT_COORDINATES_RETAINED = 6/24
SWARTZ24_FULL_SAME_EXPRESSION_L_KZ_GATE = IN_PROGRESS / NOT YET SIGNABLE
FALSE_24_OF_24_PASS = PROHIBITED
```

Only Case21 has a completed same-branch load-maximum versus `K_Z=0` ordering. Cases19,20,22,23,24 retain current roots but not a completed full KZ ordering. Cases1–18 additionally lack the retained current corrected `(D_u,q_u)` checkpoints required to reproduce that ordering.

Hence the existing 24-row load table is a valid current **equilibrium limit-point candidate table**, but it is not yet a 24/24 governing-capacity table.

## 3. Case1: the apparent worsening is real at the load-maximum level

Using the same experimental failure load

\[
P_{f,exp}=490.194022001707\ \mathrm{kN},
\]

the preserved direct-N48 result is

\[
P_{L,\mathrm{directN48}}=599.515895352265\ \mathrm{kN},
\qquad error=+22.3018\%.
\]

The current C1/MM + general-D15 load-maximum candidate is

\[
P_{L,\mathrm{current}}=608.925000000000\ \mathrm{kN},
\qquad error=+24.2212\%.
\]

Thus

\[
\Delta P_L=+9.409104647735\ \mathrm{kN}
\]

and the prediction did move farther above the experiment. This cannot be explained away by the historical `Pcr`/`Pf` identity issue.

## 4. Case1: tangent repair moves the stability evidence in the opposite direction

At the **same old direct-N48 Case1 limit state**

\[
D=0.994049227092674,
\qquad q=0.000773995088472599,
\]

the preserved tangent-repair audit gives:

| quantity | direct N48 | R10-faithful N48-C1 |
|---|---:|---:|
| loaded tangent ratio `E_parallel,t/E0` | 1.0552906913 | 0.0044587769 |
| Zhou-form `H` / N mm | 101,515,988.44 | 15,417,664.10 |
| Zhou-form single-halfwave margin | 3.586092204 | 0.831706848 |

The exact R10 target at that same state has margin `0.831057231`, so the C1 repaired tangent reproduces the R10 stability proxy closely while direct N48 is artificially stiff.

This is a strong diagnostic confirmation of the mechanical objection:

```text
DIRECT_N48_TANGENT_AT_OLD_CASE1_LIMIT = ARTIFICIALLY_STIFF
C1_REPAIR_AT_SAME_STATE = LARGE_STIFFNESS_REDUCTION
C1_ZHOU_PROXY_MARGIN_AT_SAME_STATE = BELOW_1
```

However, this Zhou-form value is a diagnostic proxy evaluated at the **old direct-N48 state**. It is not the required full same-expression `K_Z` evaluated along the **current C1/MM equilibrium branch**. It therefore cannot be used to invent a corrected Case1 capacity.

## 5. What is and is not presently known for current Case1

```text
P_L_current_Case1 = 608.925 kN                  # preserved load-maximum candidate
D_L_current_Case1 = NOT_YET_LOCATED
q_L_current_Case1 = NOT_YET_LOCATED
first_same_expression_KZ_zero_state = NOT_COMPUTED / NOT_RETAINED
P_at_first_KZ_zero = NOT_COMPUTED / NOT_RETAINED
CONTROL_EVENT_CASE1 = UNRESOLVED
```

A fresh File Library search on 2026-08-13 for the exact `608.925`, `Case1`, `D_u`, `q_u`, `N48-C1/MM`, `general-D15`, and `K_Z` identities did not recover the missing final Case1 root or the final Aug12–13 transient production source. No historical direct-N48 root is substituted.

## 6. Correct physical interpretation

Reducing material tangent stiffness does **not mathematically require** the equilibrium-branch load maximum `P_L` itself to decrease, because the C1/MM change also alters the stress-value field and therefore changes `P(D,q)` and `R_q(D,q)`. A load maximum can therefore move upward even while tangent stiffness falls.

But the governing physical capacity is not allowed to ignore the tangent event. If, on the current connected equilibrium branch,

\[
K_Z=0
\]

is reached before

\[
L=0,\quad g:+\to-,
\]

then the structure cannot be assigned the later load maximum as its governing capacity under the current stability contract. In that precise control-ordering sense, the objection is correct.

## 7. Semantic correction

From this audit forward:

```text
CASE21_365p580428 = GOVERNING_CURRENT_CAPACITY
  because its same-branch audit found KZ>0 at the first load maximum
  and the tangent zero occurs slightly later.

SWARTZ_OTHER_23_STORED_LOADS = CURRENT_EQUILIBRIUM_LIMIT_POINT_CANDIDATES
SWARTZ_OTHER_23_GOVERNING_CAPACITY = KZ_ORDERING_PENDING

CASE1_608p925 = NOT_YET_CERTIFIED_AS_GOVERNING_Pu
CASE1_608p925_NUMERICAL_RECORD = PRESERVE
```

No row is deleted. No experimental value is used to choose a new root. No empirical stiffness reduction or load factor is introduced.

## 8. Required Case1 continuation

Only the following sequence can close Case1 legitimately:

```text
A. recover or regenerate current C1/MM + general-D15 Case1 Gamma0 from raw input
B. freeze current (D,q,P,Rq,L) branch checkpoints
C. identify the first +->- P maximum
D. evaluate the full same-expression KZ continuously on that same branch
E. locate the first KZ=0 event, if any
F. compare event order:
      KZ-zero first  -> stability controls, P_control=P(KZ-zero)
      P-maximum first -> limit point controls, P_control=P_L
G. only after F, compare the governing P_control with experiment
```

Until A–F are completed, the current Case1 value must remain a load-maximum candidate rather than a certified physical ultimate load.

## 9. Verdict

```text
USER_MECHANICAL_OBJECTION = SUBSTANTIVELY_SUPPORTED
Pcr_vs_Pf_MIXUP = NOT_THE_EXPLANATION_FOR_CASE1_WORSENING
CURRENT_CASE1_608p925_AS_GOVERNING_Pu = NOT_YET_CERTIFIED
CURRENT_CASE1_LIMIT_POINT_VALUE = PRESERVED
CASE1_FULL_KZ_ORDERING = REQUIRED
CURRENT_THEORY_CHANGED = NO
CURRENT_NUMERICAL_VALUES_CHANGED = NO
STRUCTURAL_CALIBRATION = NO
FORMAL_SPATIAL_QUADRATURE_ADDED = NO
```
