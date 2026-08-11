# NZ-SCCM R10 MATERIAL-TARGET INTENT AUDIT

**Date:** 2026-08-11 15:30 +08:00  
**Identity:** CURRENT MATERIAL-LEVEL AUDIT. This audit does not change the already executed R10/R10B numerical records by itself. It checks whether the frozen R10 scalar actually matches the previously stated material-modification intent.

## 0. Evidence hierarchy used

This audit uses, in order:

1. `current/theory/NZ_SCCM_CURRENT_OPERATOR_EXPLICIT_NC_REBAR_V1_20260809.md` for the source Foster current operator;
2. `current/theory/NZ_SCCM_R10_1D_ENERGY_SMOOTHING_REINSERTION_CASE21_20260810.md` for the executed R10 formula;
3. `governance/R10_1D_ENERGY_SMOOTHING_DECISION_20260810.md` for the frozen R10 decision;
4. original-conversation excerpt supplied again on 2026-08-11 (`file_000000009470821198589fc2be909fa7`, filename `粘贴的 markdown (1)。md(7)`) for the stated intent that the source 1D law should be altered only where the sharp feature requires regularization, with the rest retained.

No structural experiment is used to choose or modify any material quantity in this audit.

---

# 1. Source Foster tensile scalar

The source ordinary-concrete current operator uses

\[
t=\Pi_\eta(\lambda),
\qquad
r=\frac{t}{x_{cr}},
\]

\[
H(r,r_0)=
\frac12\left[(r-r_0)+\sqrt{(r-r_0)^2+\eta_r^2}\right]
-\frac12\left[-r_0+\sqrt{r_0^2+\eta_r^2}\right],
\]

with

\[
\eta_r=0.05,
\qquad
m_t=-\frac7{90}.
\]

The source tensile utilization is

\[
T_{src}(r)
=r+(m_t-1)H(r,1)-m_tH(r,10),
\]

and the normalized tensile stress scalar entering the current map is

\[
\boxed{u_{src}(t)=\rho T_{src}(t/x_{cr})}.
\]

For Case21,

\[
\rho=0.1,
\qquad
\kappa=\frac{E_0\varepsilon_0}{f_c}=2.0005129533678754,
\]

\[
\boxed{x_{cr}=\frac{\rho}{\kappa}=0.04998717945397425}.
\]

The R10 source-work record is

\[
\boxed{W_{src}=0.031741235181249904}.
\]

---

# 2. Executed R10 target

The executed R10 does not leave the source law untouched outside a tiny local window. It replaces the whole retained tensile interval

\[
\boxed{0\le t\le10x_{cr}}
\]

by two C2 quintic branches.

For

\[
0\le t\le x_{cr},
\qquad
r=\frac{t}{x_{cr}},
\]

\[
\boxed{
 u_{rise}(r)=
\rho r+(10h-6\rho)r^3+(8\rho-15h)r^4+(6h-3\rho)r^5.
}
\]

For

\[
x_{cr}\le t\le10x_{cr},
\qquad
s=\frac{r-1}{9},
\]

\[
\boxed{
 u_{fall}(s)=
h+(u_r-h)(10s^3-15s^4+6s^5),
}
\]

with

\[
u_r=0.03,
\qquad
\boxed{h=0.09799750427197301}.
\]

The energy condition is

\[
\boxed{
\int_0^{10x_{cr}}u_{R10}(t)\,dt
=
\int_0^{10x_{cr}}u_{src}(t)\,dt.
}
\]

Thus R10 is a genuine material-target change, not an analytic-compiler approximation.

---

# 3. Intent-versus-execution finding

The earlier stated intent was effectively

```text
source 1D scalar
-> locate sharp peak/kink/boundary layer
-> regularize only the necessary scalar feature
-> keep the unaffected source scalar unchanged
-> reinsert into the same multidimensional interaction
```

The actually executed R10 is

```text
source 1D scalar on 0 <= t <= 10 x_cr
-> replace the entire retained tensile interval
   by a two-piece C2 quintic target
-> preserve selected physical anchors and total scalar work
-> reinsert into the same multidimensional interaction
```

These are related, but they are not mathematically identical.

Therefore the phrase `R10 energy smoothing only of the sharp 1D tensile feature` is acceptable as a statement of *motivation*, but is insufficient as an exact description of the executed target. The executed formula is a **whole-retained-branch C2 reconstruction motivated by the sharp Foster transition**.

---

# 4. Material-coordinate forensic audit

The following audit evaluates only the 1D material coordinate `r=t/x_cr`. It is not spatial sampling, structural quadrature, or a production structural calculation.

Using the frozen source Foster formula and the frozen R10 formula gives approximately:

| quantity | source Foster | executed R10 | audit implication |
|---|---:|---:|---|
| normalized stress at `r=0` | 0 | 0 | same origin value |
| `du/dr` at `r=0` | 0.0999328 | 0.1000000 | R10 enforces the idealized elastic anchor exactly; it is not byte-for-byte the source smoothed-Foster tangent |
| source peak location | `r ≈ 1.083` | `r = 1` | peak location is shifted |
| peak value | `≈0.098673` | `0.0979975` | peak reduction only about 0.685% |
| value at `r=10` | `≈0.0302538` | `0.0300000` | R10 enforces the intended residual level exactly; the algebraically smoothed source does not hit 0.03 exactly at finite `r=10` |
| total work over `0<=r<=10` | `≈0.63498752` | `≈0.63498752` | equal by construction after multiplication by `x_cr` |

Pointwise differences are not confined to the immediate peak neighborhood. Representative values are:

| `r=t/x_cr` | Foster `u_src` | R10 `u_R10` | `R10-source` |
|---:|---:|---:|---:|
| 0.25 | 0.02498 | 0.02860 | +0.00362 |
| 0.50 | 0.04993 | 0.06462 | +0.01469 |
| 0.66 | 0.06587 | 0.08418 | +0.01831 |
| 1.00 | 0.09737 | 0.09800 | +0.00062 |
| 2.00 | 0.09222 | 0.09721 | +0.00499 |
| 3.00 | 0.08448 | 0.09280 | +0.00832 |
| 5.00 | 0.06894 | 0.07102 | +0.00208 |
| 7.50 | 0.04950 | 0.03918 | -0.01033 |
| 10.00 | 0.03025 | 0.03000 | -0.00025 |

The maximum absolute normalized-stress difference is approximately

\[
\boxed{
\max_{0\le r\le10}|u_{R10}-u_{src}|
\approx0.01831
}
\]

and occurs near

\[
r\approx0.660.
\]

This is about `0.01831 f_c` in normalized stress, not a negligible numerical perturbation.

The signed work difference is zero by construction, but the positive and negative redistributed work are each approximately

\[
0.03140
\]

in the `r` coordinate. The total absolute redistributed work is about

\[
\boxed{9.89\%}
\]

of the source tensile work, while the positive relocated portion is about

\[
\boxed{4.95\%}
\]

of the source work.

The first moment of the normalized tensile work shifts from approximately

\[
\bar r_{src}=4.3791
\]

to

\[
\bar r_{R10}=4.1208,
\]

a shift of about

\[
\boxed{-5.90\%}.
\]

Thus equal total work does **not** mean that the material work distribution along the tensile scalar is unchanged.

---

# 5. Relation to the large Case21 change

The same-execution R10 structural audit recorded

\[
P_u^{source}=342.334029463\ \mathrm{kN},
\]

\[
P_u^{R10}=368.723464127\ \mathrm{kN},
\]

so

\[
\Delta P_u=+26.389434664\ \mathrm{kN}.
\]

This audit does **not** use that structural difference to reject, fit, or alter R10. However, the 1D material audit shows that the R10 target redistributes the tensile scalar over a broad part of the retained interval despite almost preserving the peak value. Therefore the large structural response change cannot be described as the consequence of only an infinitesimal smoothing of one mathematical cusp.

The R09A sensitivity result already established that tensile-branch shape/capacity changes can move the coupled `(D,q)` equilibrium and thereby change the compression-dominated capacity indirectly.

---

# 6. Multiaxial architecture remains unchanged

This audit does not challenge the R10 reinsertion architecture.

R10 uses

\[
T_i^{R10}=\frac{u_{R10}(t_i)}{\rho},
\]

then keeps the same

\[
U_i,
\quad
CC,
\quad
TC,
\quad
TT,
\]

and the same spectral return. No multidimensional interaction coefficient is refitted.

Therefore the issue identified here is specifically the **identity of the 1D R10 material target**, not the validity of the multidimensional reinsertion mechanism.

---

# 7. Audit decision

```text
R10_EXECUTED_FORMULA_RECOVERY                 = PASS
R10_SOURCE_WORK_EQUALITY                       = PASS
R10_C2_TARGET_INTERNAL_CONSISTENCY              = PASS
R10_SAME_MULTIAXIAL_REINSERTION_ARCHITECTURE    = PASS
R10_AS_TINY_LOCAL_SOURCE_PATCH                  = FAIL_DESCRIPTION
R10_AS_WHOLE_RETAINED_TENSILE_BRANCH_REBUILD    = PASS_DESCRIPTION
R10_ORIGINAL_INTENT_VS_EXECUTED_TARGET           = HOLD_RECONCILIATION
STRUCTURAL_Pu_CALIBRATION                       = NO
```

The existing R10 and R10B numerical results remain valid as records of the **executed R10 target**. This audit does not yet decide whether that executed target should remain the final physical material target for publication/generalization.

---

# 8. Required next step before coefficient reconstruction

The next task is now strictly:

```text
R10A_MATERIAL_TARGET_INTENT_RECONCILIATION
```

It must answer one question only:

> Is the intended formal material model the already executed whole-retained-branch C2 energy reconstruction, or should the original design intent of a genuinely local source-preserving regularization be restored?

No R10B coefficient generator should be frozen or published before this identity is resolved, because the coefficient table must represent the final material target rather than an accidentally intermediate target.

This reconciliation must be decided from material/source/analytic considerations only. Case21 agreement must not be used to choose between the alternatives.
