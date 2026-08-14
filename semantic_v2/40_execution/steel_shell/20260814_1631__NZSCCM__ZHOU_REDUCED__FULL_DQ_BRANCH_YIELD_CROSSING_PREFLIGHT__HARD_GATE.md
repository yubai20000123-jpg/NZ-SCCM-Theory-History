# RETRACTED — NZ-SCCM Zhou reduced reference D-q yield-crossing hard gate

Date originally created: 2026-08-14 16:31 +08:00
Retraction: 2026-08-14
Status: **RETRACTED / DO NOT USE AS A GOVERNING GATE**

## Retraction reason

This file was created by incorrectly promoting an older steel-shell extension-draft requirement (`STEEL_SHELL_2D_CURRENT_OPERATOR = PENDING SOURCE-CONSISTENT FREEZE`) above the later locked governance and semantic branch rules for the present **reduced Zhou diagnostic**.

That promotion was wrong.

The later locked rule already defines the reduced-reference steel event/tangent closure to be used for this diagnostic:

```text
elastic and unbuckled -> Et,eff = Es
elastic Yun postbuckled (only when elastic buckling precedes yield) -> Et,eff = d sigma_Yun/d epsilon_Yun
first yield and continuing ideal-plastic loading -> Et,eff = 0
steel stress remains strength-capped; Et=0 does NOT mean Ps=0
```

For the current Zhou Table-5.1 reduced reference the ordering is `YIELD_FIRST`, because the Yun elastic local-buckling stress exceeds `fy`. Therefore no elastic Yun S1 branch is inserted ahead of yield.

The semantic branch explicitly permits the global path to continue after first yield with the approved ideal-EP strength cap while refusing to invent a detailed expanding plastic-zone/local-shape model. The absence of such a detailed plastic-zone model is **not** a reason to stop the present reduced-reference branch diagnostic.

## Correct execution scope

The requested calculation remains authorized:

```text
regenerate the complete connected reduced-Zhou D-q primary branch
capture Y_s^- / Y_s / Y_s^+
record Pc, Ps, P, Rq, L,
KZ_c^mat, KZ_s^mat, KZ^geo, KZ,
and test whether Ps stays high while KZ_s^mat drops and is followed by L=0 or KZ=0.
```

This calculation is a **mechanism diagnostic under the already locked reduced-reference ideal-EP closure**, not a claim that a fully resolved 2D plastic-zone theory has been derived.

## Governance consequence

```text
OLD_HARD_GATE = RETRACTED
FULL_2D_PLASTIC_ZONE_OPERATOR_AS_PRECONDITION_FOR_THIS_DIAGNOSTIC = NO
REDUCED_ZHOU_DQ_BRANCH_DIAGNOSTIC = AUTHORIZED
R10 = UNCHANGED
N48-C1/MM = UNCHANGED
NGUYEN_SECOND_ORDER = UNCHANGED
GENERAL_D15 = UNCHANGED
FORMAL_SPATIAL_QUADRATURE = 0
STRUCTURAL_CALIBRATION = NO
```

The next execution must proceed from the existing locked reduced-reference rules rather than reopening the steel material theory.
