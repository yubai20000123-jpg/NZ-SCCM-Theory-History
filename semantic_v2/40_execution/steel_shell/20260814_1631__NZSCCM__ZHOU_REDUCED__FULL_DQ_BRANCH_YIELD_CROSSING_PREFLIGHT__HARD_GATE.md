# NZ-SCCM Zhou reduced reference — full D-q primary-branch yield-crossing preflight / hard gate

Date: 2026-08-14 16:31 +08:00

## Requested execution

Regenerate the reduced Zhou reference complete connected `D-q` primary branch and persist, especially across first steel yield `Y_s`,

```text
D, q,
Pc, Ps, P,
Rq,
P_D, P_q, Rq_D, Rq_q, L,
max steel stress / Y_s,
KZ_c^mat, KZ_s^mat, KZ^geo, KZ
```

The target causal sequence to test is

```text
Ps remains high
+ KZ_s^mat drops strongly at/after Y_s
-> shortly followed by L = 0 or KZ -> 0.
```

No structural calibration, no experimental root selection, no spatial quadrature, and no synthetic post-yield rule are authorized.

## Audit result before solve

The current shell structural extension is closed, but its own contract still states:

```text
STEEL_SHELL_2D_CURRENT_OPERATOR = PENDING SOURCE-CONSISTENT FREEZE
```

and requires a production plane-stress map

\[
\sigma^s=M_s(\varepsilon^s),
\qquad
\mathbb C_t^s=\partial\sigma^s/\partial\varepsilon^s,
\]

with full 2D current stress and full directional consistent tangent.

The later locked ideal-EP governance correction freezes the event/tangent semantics:

```text
elastic/unbuckled -> Et,eff = Es
elastic Yun postbuckled -> Et,eff = d sigma_Yun / d epsilon_Yun
yield + continuing plastic loading -> Et,eff = 0
unloading/redistribution below fy -> elastic physical tangent again
```

but it does **not** supply the missing full 2D path-independent plane-stress current map or a finite analytic plastic-zone compiler.

The semantic branch index additionally states explicitly:

```text
Detailed expanding plastic-zone/local-shape evolution after first yield is not supplied by Yun Lu Chapter 2 and is not invented.
```

## Why a global Es -> 0 switch is prohibited

At first yield under the common Nguyen membrane+bending field, first yield is generally attained only on a subset of the continuous shell field. After that event the production quantities require fieldwise current stress and tangent:

\[
P_s=-\frac1\ell\int_{\Omega_s}\sigma_y^s\,dV,
\]

\[
K_{Z,s}^{mat}=\int_{\Omega_s}b_\varphi^T\mathbb C_t^s b_\varphi\,dV.
\]

A legitimate post-yield branch therefore has to distinguish, continuously and analytically, at least:

- steel still elastic;
- steel on the ideal-plastic surface under continuing loading;
- previously yielded steel unloading/redistributing below `fy`.

Setting the **entire** shell to `Et=0` at the instant the first point reaches yield would not implement the locked rule. It would replace heterogeneous first yield by a global binary switch.

More importantly, such a shortcut would make the requested causal test circular: it would force `KZ_s^mat` to collapse at `Y_s` by construction, then use that imposed collapse as evidence that the real branch is controlled by steel tangent loss.

Therefore:

```text
GLOBAL_SHELL_ET_ZERO_AT_FIRST_POINT_YIELD = PROHIBITED
INVENTED_VON_MISES_RETURN_MAP = PROHIBITED
INVENTED_PLASTIC_ZONE_PARTITION = PROHIBITED
```

## Historical 26.1085 MN point cannot repair the missing state

The historical

```text
P_NZ_diag ~= 26.1085 MN
```

remains only a diagnostic first-load-maximum neighbourhood. No persisted associated state was recovered containing the required

```text
D, q, Pc, Ps, KZ_s^mat, KZ_c^mat, KZ_geo, L
```

components. It is therefore not used as a restart state or as a hidden root selector.

## What can and cannot be released now

The elastic steel branch before first yield is structurally defined. The requested *yield-crossing complete branch*, however, is not mathematically closed after `Y_s` under the currently frozen production theory.

Consequently this execution stops at the operator gate rather than manufacturing a branch table.

```text
FULL_ZHOU_REDUCED_DQ_BRANCH = NOT RELEASED
PRE_YIELD_STEEL_OPERATOR = CLOSED_ELASTIC
FIRST_YIELD_EVENT_SEMANTICS = CLOSED
POST_YIELD_FULL_2D_CURRENT_STRESS = NOT CLOSED
POST_YIELD_FULL_DIRECTIONAL_TANGENT = NOT CLOSED
POST_YIELD_EXACT_D15_COMPILER = NOT CLOSED
CAUSAL_SEQUENCE_Ps_HIGH_KZs_DROP_THEN_L_OR_KZ = NOT YET TESTABLE_PRODUCTION
FAILURE_TYPE = THEORY_OPERATOR_CLOSURE, NOT NUMERICAL_SOLVER
```

## Smallest exact next action

Do **not** perform more parameter sweeps. Close exactly one missing material-layer object:

\[
\boxed{M_s^{EP}(\varepsilon)\;\text{and}\;\mathbb C_{t,s}^{EP}(\varepsilon)}
\]

for the approved ideal elastic-perfectly-plastic steel under plane stress, in a form compatible with the project's no-load-step current-map requirement and finite analytic / general-D15 compilation.

Then regenerate this same reduced Zhou reference from zero load and persist the requested complete state table. The causal test is accepted only if the resulting independently computed path itself shows

```text
Y_s
-> Ps remains high
-> KZ_s^mat drops due to the fieldwise consistent tangent
-> L=0 or KZ=0 follows on the same connected branch.
```

No numerical value from Zhou's comparator or the historical 26.1085 MN diagnostic is permitted to choose or tune that operator.
