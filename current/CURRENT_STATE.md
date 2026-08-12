# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-12 10:35 +08:00  
**Purpose:** 唯一当前工作入口；只保留当前有效状态、canonical evidence 和下一门禁。

## 0. Highest-priority contract

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
ACTIVE_MODE = m=1
KINEMATICS = NGUYEN_SECOND_ORDER
STABILITY_BACKBONE = ZHOU_NAVIER_TANGENT_STABILITY
EXACT_MOMENT_ENGINE = D15
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
STRUCTURAL_CALIBRATION = NO
```

Formal production prohibits spatial Gauss/Simpson/adaptive quadrature, spatial Chebyshev collocation, material-point grids/cells, whole-structure P/R fitting and experiment-driven material tuning.

---

## 1. Governing material target — R10 FROZEN

```text
source Foster current relation
-> R10 1D energy-smoothed tensile scalar
-> SAME U/C/T + CC/TC/TT multidimensional current map
```

Core identities remain

\[
\kappa=\frac{E_0\varepsilon_0}{f_c},\qquad
x_{cr}=\frac{\rho}{\kappa},\qquad \rho=0.1,
\]

\[
h=\frac15\left(\frac{W_{src}}{x_{cr}}-\frac{\rho}{10}-\frac92u_r\right).
\]

Exact zero-state anchors:

\[
U(0)=0,\quad U'(0)=\kappa,
\]

\[
C(0)=T(0)=T^7(0)=0,
\]

\[
C'(0)=T'(0)=(T^7)'(0)=0.
\]

```text
R10_MATERIAL_TARGET = GOVERNING_AND_UNCHANGED
NEW_MATERIAL_MECHANISM = NOT_AUTHORIZED
```

---

## 2. Current N48 compiler identity

\[
\boxed{N_M=48}.
\]

```text
U_COMPILER  = N48-C1
C_COMPILER  = N48-C1
T7_COMPILER = N48-C1
T_COMPILER  = N48-C1-CONSTRAINED-MINIMAX
```

For \(F\in\{U,C,T^7\}\), first generate the direct Chebyshev-root coefficients

\[
a_n^{(F,0)}=
\frac{2-\delta_{n0}}{49}
\sum_{j=0}^{48}F(\lambda_j)\cos(n\theta_j),
\]

then enforce the strict-C1 anchors by

\[
\boxed{
\mathbf a^{(F,C1)}
=
\mathbf a^{(F,0)}
+
\mathbf H^{-1}\mathbf G^T
(\mathbf G\mathbf H^{-1}\mathbf G^T)^{-1}
(\mathbf d_F-\mathbf G\mathbf a^{(F,0)}).
}
\]

For \(T\), use the degree-48 strict-C1 constrained minimax solution over the full compiler interval.

Current compiler gates:

```text
R10_VALUE_ANCHOR_GATE = PASS
R10_FIRST_TANGENT_GATE = PASS
N48_NEAR_ZERO_T_VALUE_GATE = PASS
O1_COEFFICIENT_GATE = PASS
CAYLEY_HAMILTON_COMPATIBILITY = PASS
D15_COMPATIBILITY = PASS
ZHOU_Dx_Dy_H_GATE = PASS
N48_STRICT_C1_FULL_HULL_DIRECT_VALUE_LEVEL = NOT_FULLY_RECOVERED
```

The last item is a degree-48 representation-capacity boundary, not authorization to reopen R10 or raise polynomial order.

Canonical compiler audits:

- `current/audits/NZ_SCCM_N48_C1_VALUE_TANGENT_REPAIR_AUDIT_20260811.md`
- `current/audits/NZ_SCCM_N48_C1_TENSILE_MINIMAX_BOUNDARY_LAYER_AUDIT_20260812.md`
- `governance/N48_C1_VALUE_TANGENT_REPAIR_DECISION_20260811.md`
- `governance/N48_C1_TENSILE_MINIMAX_BOUNDARY_LAYER_DECISION_20260812.md`

---

## 3. Canonical updated paper-style derivations — COMPLETE

Current theory files:

- `current/theory/NZ_SCCM_R10_N48C1MM_D15_PAPER_STYLE_DERIVATION_20260812.md`
- `current/theory/NZ_SCCM_R10_N48C1MM_D15_EQUATION_BY_EQUATION_DERIVATION_20260812.md`
- `governance/R10_N48C1MM_D15_PAPER_STYLE_DERIVATION_DECISION_20260812.md`

The equation-by-equation file contains the full material-parameter -> R10 -> N48-C1/MM -> Cayley-Hamilton -> Nguyen -> D15 -> P/Rq/L -> Zhou Dx-Dy-H chain with paper-style symbol definitions.

```text
UPDATED_PAPER_STYLE_DERIVATION = COMPLETE
EQUATION_BY_EQUATION_DERIVATION = COMPLETE
SYMBOL_DEFINITIONS = COMPLETE
```

---

## 4. Updated Case21 fresh numerical record — PRESERVED, but independent reproduction BLOCKED

A fresh N48-C1/MM + D15 Case21 numerical record was produced without historical Case21 calculated values or experimental load entering the solve. That record is preserved as an execution artifact, but it has **not** passed the later blank-chat self-contained reproduction gate.

The independent blank-chat audit used the fresh full-calculation document as its only allowed input and found the first blocking omission at R10:

```text
OVERALL = BLOCKED
FIRST_SUBSTANTIVE_DIVERGENCE = R10
FIRST_BLOCK = R10 / FOSTER_SOURCE_H_NOT_DEFINED
```

The same audit also found that the fresh full-calculation document was not self-contained for:

- \(\Pi_\eta(z)\);
- the complete \(u_{sm}(t)\) branch definition and \(\tau(t),s(t)\);
- N48-C1 \(\mathbf H,\mathbf G,\mathbf d_F\);
- a unique reproducible numerical production contract for the T constrained-minimax coefficients.

Therefore the previously reported fresh values, including the numerical \(D,q,P_u\), remain **reported execution results only** until a second independent reproduction passes. They must not be labeled an independently verified closure.

Canonical audit evidence:

- `current/audits/NZ_SCCM_CASE21_N48C1MM_INDEPENDENT_REPRO_BLOCKED_R10_20260812.md`

Governance status:

```text
CASE21_N48C1MM_D15_FRESH_NUMERICAL_RECORD = PRESERVED
CASE21_N48C1MM_D15_INDEPENDENT_REPRO = BLOCKED_AT_R10
CASE21_N48C1MM_D15_FRESH_CLOSURE_ACCEPTED = NO
HISTORICAL_CASE21_COMPUTED_VALUES_USED_IN_FRESH_RECORD = NO
EXPERIMENT_USED_DURING_FRESH_SOLVE = NO
```

No inference about agreement with experiment can override this reproducibility block.

---

## 5. Self-contained Case21 blind contract V2 — READY FOR SECOND AUDIT

A new blind contract has been prepared specifically to remove the omissions identified by the independent audit. It includes explicit definitions for:

- \(H(r,r_0)\);
- \(\Pi_\eta(z)\);
- complete \(u_{sm}(t)\), \(\tau(t)\), \(s(t)\) and branch intervals;
- \(\mathbf H,\mathbf G,\mathbf d_F\) for N48-C1;
- a deterministic material-coordinate exchange/LP contract for T strict-C1 constrained-minimax;
- Cayley-Hamilton, Nguyen kinematics, D15, Case21 steel, same-expression derivatives and the continuous compiler-domain gate.

Files:

- `current/workflows/NZ_SCCM_CASE21_N48C1MM_D15_SELF_CONTAINED_BLIND_CONTRACT_V2_20260812.md`
- `current/workflows/NZ_SCCM_CASE21_N48C1MM_D15_SELF_CONTAINED_BLIND_PROMPT_V2_20260812.txt`

The V2 contract contains **no Case21 theoretical answer and no experimental failure load**.

```text
SELF_CONTAINED_BLIND_CONTRACT_V2 = READY
SECOND_BLANK_CHAT_REPRODUCTION = NOT_YET_EXECUTED
```

V2 itself is not declared validated until the new blank-chat audit reaches PASS. If the second audit finds another first missing closure, that new first block controls the next revision.

---

## 6. Earlier structural records remain preserved

```text
EARLIER_CASE21_DIRECT_N48_VALUE_CLOSURE = PRESERVED_HISTORICAL_RECORD
SWARTZ24_FRESH_BLIND_VALUE_CLOSURE = 24/24 PRESERVED_RECORD
SWARTZ24_PRIMARY_MECHANISM_AUDIT = COMPLETE
```

They are not inputs to the new Case21 V2 blind reproduction.

---

## 7. Current execution boundary

Do not automatically:

- reopen R10;
- add a new material mechanism;
- raise to N96/N112;
- use old Case21 values as targets for the V2 audit;
- use experiment during the V2 solve;
- recalculate Swartz24 before Case21 V2 reproducibility passes.

```text
R10 = FROZEN
N48_ORDER = 48
UPDATED_N48_C1_MM_D15_DERIVATION = CANONICAL
CASE21_N48C1MM_D15_FRESH_CLOSURE_ACCEPTED = NO
CURRENT_NEXT_TASK = SECOND_BLANK_CHAT_CASE21_V2_REPRODUCTION
```
