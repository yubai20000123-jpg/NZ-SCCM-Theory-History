# NZ-SCCM — Cedolin–Mulas 1984 peak-envelope semantics correction R01

**Time:** 2026-08-23 23:57 +08:00  
**Status:** `SOURCE_AUDIT_PASS / PREVIOUS_CHAT_ONLY_CM_PU_VALUES_INVALID / AIRY_UNCHANGED / SWARTZ8_ONLY`

## 0. Scope

This audit corrects the interpretation used in the immediately preceding Cedolin–Mulas diagnostic for the fixed Swartz common set

\[
\{4,5,6,8,9,14,21,23\}.
\]

No structural equation, representative halfwave ledger, reinforcement mapping, Airy demand equation or experimental comparator is modified here.

The only question is the meaning of Cedolin–Mulas (1984) Fig. 7 and Eqs. (17)–(19), especially the line

\[
\sigma_1=-\alpha\sigma_2,\qquad \alpha\simeq0.3.
\]

## 1. Primary-source reading of Cedolin–Mulas

Cedolin–Mulas explicitly states that the fitted secant moduli `Ks` and `Gs` are valid in the **nonlinear range**. The paper then identifies the approximate line

\[
\sigma_1=-0.3\sigma_2
\]

as the **limit between linear and nonlinear behavior** in the tension–compression quadrant. On the linear side, the corresponding strain relation is obtained with Hooke's law; the nonlinear relation is reported to approach this boundary smoothly.

Therefore:

```text
SIGMA1_OVER_SIGMA2 = -0.3
= LINEAR/NONLINEAR BRANCH BOUNDARY
!= PEAK-STRESS ENVELOPE
!= MATERIAL FAILURE BY ITSELF
!= RC PANEL Pu
```

The same source separately explains that the Kupfer data used for fitting failed just before peak stress, so the fitted `Ks,Gs` expressions are valid only for the ascending part of the stress–strain relation. Because a total stress–strain relation does not by itself provide a failure criterion, Cedolin–Mulas introduces Eqs. (17)–(19) as an **ascending-branch peak/limit check** parameterized by principal-stress ratio.

Its conclusion again defines the proposed law as a total explicit plane-stress relation for **monotonic biaxial loading until peak stress**.

Hence Eqs. (17)–(19) have the following correct identity:

```text
CM_EQ17_19 = LOCAL_MATERIAL_ASCENDING_BRANCH_PEAK_LIMIT
CM_EQ17_19 = RANGE_OF_APPLICABILITY / PEAK_PROXIMITY CHECK
CM_EQ17_19 != GLOBAL_RC_PANEL_ULTIMATE_CRITERION
```

## 2. Independent consistency check from Nguyen

Nguyen's RC-wall material chapter gives the same physical hierarchy in a different constitutive framework. When the biaxial strength envelope is breached in the tension–compression quadrant, the concrete element **changes state** to cracked tension–compression; the breach is not treated as immediate failure of the whole RC wall. The cracked state then continues carrying compression with reduced compressive strength and a separate post-cracking tensile response.

Therefore the structural/material hierarchy is consistent:

\[
\text{first local biaxial envelope event}
\rightarrow
\text{material-state transition / continuation}
\neq
\text{global wall ultimate load}.
\]

## 3. Independent consistency check from Attard wall methodology

Attard's RC-wall procedure uses the buckling analysis to obtain amplified axial force and bending moments. The design actions are then checked against the **ultimate capacity of the wall section through an interaction diagram**. Thus the wall ultimate check is a section-level demand–capacity contact, not the first local concrete point reaching an ascending-branch boundary.

This supports the present Marguerre–Airy architecture:

\[
\text{Airy structural demand}
\rightarrow
(N_x,N_y,M_x,M_y)
\rightarrow
\text{section/material capacity}
\rightarrow
P_u.
\]

## 4. Consequence for the immediately preceding Swartz8 Cedolin–Mulas numbers

The immediately preceding chat-only calculation stopped seven of the eight specimens when a local stress state reached approximately

\[
\sigma_1/\sigma_2=-0.3.
\]

That stop condition is source-incorrect. It mistakes the linear/nonlinear constitutive branch boundary for a peak/failure condition.

Accordingly the previously reported chat-only values

```text
Case4  179.79 kN
Case5  159.35 kN
Case6  149.58 kN
Case8  169.99 kN
Case9  111.57 kN
Case14 363.96 kN
Case21 106.30 kN
Case23 140.65 kN
```

are **invalid as Cedolin–Mulas Pu predictions** and must not be used for theory selection, calibration, error statistics or GitHub current-state evidence.

```text
PREVIOUS_CHAT_CM_SWARTZ8_PU = WITHDRAWN
PREVIOUS_CHAT_CM_MAE = WITHDRAWN
PREVIOUS_CHAT_CM_RMSE = WITHDRAWN
```

## 5. Correct Cedolin–Mulas evaluator semantics for the rerun

For every current plane-stress material state, the evaluator must first classify only the **constitutive range**, not a damage/history state.

### 5.1 Linear range

When the current principal-stress ratio lies on the linear side of the Fig. 7(a) boundary, use the plane-stress Hooke relation corresponding to the source's linear-range prescription.

Crossing

\[
\sigma_1/\sigma_2=-0.3
\]

is a smooth branch transition and must not terminate the panel calculation.

### 5.2 Nonlinear ascending range

Inside the source-defined nonlinear range, use the explicit Cedolin–Mulas map

\[
(\varepsilon_1,\varepsilon_2)
\rightarrow
\varepsilon_3
\rightarrow
(\varepsilon,\gamma)
\rightarrow
(K_s,G_s)
\rightarrow
(\sigma_1,\sigma_2).
\]

### 5.3 Peak-envelope event

Eqs. (17)–(19) are evaluated only with their stated stress-ratio domains. Reaching that envelope is recorded as

```text
LOCAL_CM_PEAK_EVENT
```

not automatically as `P_u`.

### 5.4 No unsupported extrapolation

Cedolin–Mulas does not supply a complete post-peak RC continuation. Therefore, if a local CM peak event occurs before the Airy section-level ultimate contact can be established, the calculation must report

```text
POSTPEAK_CONTINUATION_REQUIRED
```

rather than silently extrapolating `Ks,Gs`, inventing a descending law, or declaring the first local peak to be the wall ultimate load.

## 6. Fixed next execution

Only the eight specimens

\[
\boxed{4,5,6,8,9,14,21,23}
\]

are to be rerun.

Keep fixed:

- existing per-panel representative-halfwave ledger;
- corrected reinforcement mapping;
- frozen Marguerre–Airy demand side;
- projected work-conjugate bending moment architecture;
- no use of `Pf` in root/event selection.

The rerun shall output, for each panel:

1. first entry into/out of the CM nonlinear range;
2. first true CM Eq. (17)–(19) peak event, if any;
3. whether a valid section-level terminal root occurs before that event;
4. otherwise `POSTPEAK_CONTINUATION_REQUIRED`;
5. `Pf` only as a post-check after the theoretical event/root identity is frozen.

## 7. Governance decision

```text
AIRY = UNCHANGED
SWARTZ_SET = ONLY_4_5_6_8_9_14_21_23
CEDOLIN_MULAS_PREPEAK_EXPLICIT_MAP = RETAIN
CM_MINUS_0P3_LINE = BRANCH_BOUNDARY_NOT_FAILURE
CM_EQ17_19 = LOCAL_ASCENDING_PEAK_LIMIT
FIRST_LOCAL_CM_PEAK_AS_GLOBAL_Pu = PROHIBITED
UNSUPPORTED_POSTPEAK_EXTRAPOLATION = PROHIBITED
NEXT_TASK = CORRECTED_CM_BRANCH_LOGIC_SWARTZ8_RERUN
```
