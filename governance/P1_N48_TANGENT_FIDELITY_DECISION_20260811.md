# GOVERNANCE DECISION — P1 N48 tangent fidelity audit

**Date:** 2026-08-11

## Decision

The Swartz24 P1 current-tangent audit is accepted as a diagnostic result.

```text
R10_MATERIAL_TARGET = FROZEN / NOT CHANGED
SWARTZ24_FROZEN_Pu_VALUES = PRESERVED AS VALUE-CLOSURE RECORD
N48_ORDER = 48
N48_TANGENT_FIDELITY = FAIL_DIAGNOSTIC
FIRST_CLEAR_DEVIATION = R10_TARGET -> N48_FIRST_DERIVATIVE
STRUCTURAL_CALIBRATION = PROHIBITED
AUTOMATIC_MATERIAL_ROUTE_CHANGE = PROHIBITED
AUTOMATIC_ORDER_ESCALATION = PROHIBITED
```

## Basis

At the exact R10 zero tensile coordinate,

\[
C(0)=T(0)=T^7(0)=0,
\]

and

\[
C'(0)=T'(0)=(T^7)'(0)=0.
\]

The current global N48 Chebyshev representation does not preserve the first-derivative anchors. Across the 24 current panel compiler intervals, the audit finds

```text
T48'(0) = approximately 8.69 ... 11.36
R10 target T'(0) = 0
```

and large downstream changes in the equivalent current tangent matrix.

Using a Zhou-form directional-stiffness decomposition, the equivalent mixed/torsional quantity H from N48 is approximately 4.72–6.79 times the R10-target tangent value, and the corresponding center-state stability proxy is inflated approximately 3.28–4.42 times.

## Interpretation boundary

This diagnostic does NOT prove that the frozen blind Pu values must be discarded. Those remain valid records of the executed R10→N48→D15 value-closure chain.

It DOES mean that the physical interpretation of the same-expression derivative limit condition L=0 cannot be treated as fully source-faithful until R10-to-N48 tangent representation fidelity is resolved.

Attard and Zhou are used only for independent interpretation:

- Attard: orthotropic tangent-stability benchmark;
- Zhou Siming: directional stiffness decomposition and Navier stability logic.

Neither source replaces the R10 material operator.

## Next gate

The next permitted task is narrowly defined:

```text
PRESERVE R10
PRESERVE ONE_CONTINUOUS_COMPLETE_HALFWAVE
PRESERVE ZERO FORMAL SPATIAL QUADRATURE
PRESERVE SIMPLE N48-SCALE ANALYTIC REPRESENTATION IF POSSIBLE
-> repair/redefine only the analytic representation so that required material values AND first derivatives/anchor identities are faithfully represented
-> re-audit tangent before any material or structural retuning
```
