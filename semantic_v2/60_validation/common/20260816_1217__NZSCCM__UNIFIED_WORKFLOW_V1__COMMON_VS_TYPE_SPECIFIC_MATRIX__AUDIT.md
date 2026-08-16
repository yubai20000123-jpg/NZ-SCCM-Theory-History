# NZ-SCCM unified workflow V1 — common-vs-type-specific audit

**Timestamp:** 2026-08-16 12:17 +08:00  
**Identity:** PROJECT-WIDE ARCHITECTURE AUDIT

## 1. Audit question

Can NC+rebar, NC+steel-shell, UHPC+rebar and UHPC+steel-shell use one production workflow without pretending that physically different modules are identical?

**Verdict: YES**, provided the project distinguishes **common invariants** from **physical type adapters**.

## 2. Common invariants that are already supported by current branches

### 2.1 Continuous halfwave + Nguyen second order

The current NC+rebar production contract and NC+steel-shell extension both preserve one continuous complete halfwave and Nguyen second-order kinematics. The shell extension explicitly states that the bonded shell shares the same membrane/curvature field.

### 2.2 Membrane redistribution

The second-order membrane terms are present in the same continuous strain field for concrete, reinforcement projection and bonded shell. Therefore membrane stress redistribution is a **common mandatory mechanism**, not a switch controlled by specimen stockiness.

### 2.3 Zero spatial numerical integration

Both the NC+rebar and steel-shell branches close structural integrals through General-D15 exact moments. The shell branch additionally closes the thickness coordinate analytically. Therefore:

```text
formal spatial sampling = 0
formal spatial quadrature = 0
formal thickness quadrature = 0
```

is a common invariant.

### 2.4 Current tangent and stability

The shell contract explicitly requires a full directional consistent tangent and current-stress geometric stiffness. The NC+rebar branch likewise uses same-branch tangent/stability auditing. Therefore the common project rule must be:

```text
same current stress state
+ consistent current material tangent
+ material stiffness contribution
+ current-stress geometric stiffness contribution
-> same-state KZ audit
```

A specimen may not use a frozen elastic tangent merely because its structural phase differs.

### 2.5 Common primary limit root

Both current NC+rebar and NC+shell contracts assemble phase contributions into total `P,Rq` and use the same derivative determinant

\[
L=P_D R_{q,q}-P_qR_{q,D}.
\]

Hence the primary connected-branch root topology is common.

## 3. Type-specific differences that are legitimate

### 3.1 NC versus UHPC source material law

A universal workflow does not imply one universal constitutive equation. NC R10 and the future frozen UHPC multidimensional current operator are different physical source maps. They may need different analytic basis details or converged algebraic order, but both must pass the same source-operator interface and source-fidelity governance before entering the same structural backend.

### 3.2 Rebar versus shell phase geometry

Rebar uses directional line/layer projection; shell uses bonded finite-thickness plane-stress kinematics. These are legitimate phase adapters. They are not reasons to change the concrete/UHPC compiler, D15 engine or root logic.

### 3.3 Shell local buckling

A shell specimen may possess a source-grounded local plate-buckling coordinate absent from a rebar specimen. The correct common treatment is not to forbid that coordinate and not to create a separate solver. It is to treat the local amplitude as a finite internal coordinate and exactly condense it into the same global `D,q` derivative/tangent system.

### 3.4 Boundary conditions / halfwave selector

Different experimental or structural families may genuinely have different physical boundary conditions. The allowed variation is the boundary operator and its theoretical energy/design halfwave selector. The prohibited variation is choosing a boundary/halfwave because it makes Pu match a target.

## 4. Conflicts corrected by V1

### 4.1 Fixed N48 as a project identity

**Rejected.** N48 is not the theory. The 11:34 audit remains evidence that one global N48 representation can be insufficient for the NC source transition. The response is a deterministic material-family compiler convergence process, not a case-specific workaround.

### 4.2 Literal identical compiler internals for NC and UHPC

**Relaxed.** The previous 11:52 wording could be read too literally. V1 requires the same compiler **interface, source-only fidelity governance, family freeze rule and D15 compatibility**, while permitting material-family-specific analytic basis details where physically/mathematically necessary.

### 4.3 Z6 exemption

**Rejected.** Z6 is computationally solvable and remains a user-accepted engineering baseline, but its old N48 result does not prove compiler fidelity. It must be rerun with Z0-Z5 after the NC family compiler is frozen.

## 5. Production gate matrix

| Gate | NC+rebar | NC+shell | UHPC+rebar | UHPC+shell |
|---|---|---|---|---|
| source current operator frozen | PASS (R10) | PASS (R10) | PENDING | PENDING |
| family compiler frozen under V1 | PENDING | PENDING, same NC compiler | WAITING UHPC source | WAITING UHPC source |
| Nguyen second order | PASS | PASS | REQUIRED | REQUIRED |
| membrane redistribution | REQUIRED | REQUIRED | REQUIRED | REQUIRED |
| zero spatial integration | REQUIRED | REQUIRED | REQUIRED | REQUIRED |
| rebar adapter | CURRENT SUPPORT | N/A | CURRENT SUPPORT architecture | N/A |
| shell structural adapter | N/A | CURRENT SUPPORT | N/A | CURRENT SUPPORT architecture |
| shell 2D current material operator | N/A | production status must be source-frozen/checked | N/A | production status must be source-frozen/checked |
| local amplitude exact condensation | N/A | when physically active | N/A | when physically active |
| common P,Rq,L root | REQUIRED | REQUIRED | REQUIRED | REQUIRED |
| same-state consistent KZ | REQUIRED | REQUIRED | REQUIRED | REQUIRED |

## 6. Required intermediate-state record

Every production result must persist at least:

1. specimen/source input hash or canonical parameter record;
2. boundary/halfwave selector result;
3. material-family compiler identity, domain and source-fidelity metrics;
4. generalized coordinates `D,q` and all active finite internal coordinates;
5. material principal/invariant envelope;
6. phase `P` contributions;
7. phase `Rq` contributions;
8. `P_D,P_q,Rq_D,Rq_q,L` or exact condensed equivalents;
9. current tangent/geometric `KZ` phase contributions;
10. equilibrium/condensation residuals;
11. branch peak bracket;
12. formal spatial/thickness integration counters.

This record is mandatory regardless of specimen type.

## 7. Audit verdict

```text
UNIFIED_WORKFLOW_V1_COMMON_MECHANICS = PASS
TYPE_ADAPTER_CONCEPT = PASS
MEMBRANE_REDISTRIBUTION_COMMON = PASS
CONSISTENT_TANGENT_COMMON = PASS
ZERO_SPATIAL_INTEGRATION_COMMON = PASS
COMMON_P_Rq_L_ROOT = PASS
MATERIAL_FAMILY_SPECIFIC_COMPILER_INTERNALS = ALLOWED_UNDER_COMMON_FIDELITY_GOVERNANCE
CASE_SPECIFIC_BESPOKE_METHOD = PROHIBITED
```

Immediate next numerical task:

`UNIFIED_PRODUCTION_WORKFLOW_V1_IMPLEMENTATION_AND_NC_FAMILY_COMPILER_FREEZE`.