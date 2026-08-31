# NZ-SCCM — 几何曲率锁定修正与 BH050 从零重算计划 R01

**Date:** 2026-08-31  
**Branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Status:** `CORRECTION BACKUP / RECOMPUTE INPUT / PRODUCTION MAIN UNCHANGED`

## 1. Correction

当前单半波 added displacement 已定义为

\[
w_m=bq\sin(\alpha x)\sin(\beta y).
\]

因此材料弯曲应变所用的增量曲率不是独立截面未知量，而由位移场唯一决定：

\[
\boxed{\kappa_T=-w_{m,xx}=bq\alpha^2\sin\alpha x\sin\beta y},
\]

\[
\boxed{\kappa_L=-w_{m,yy}=bq\beta^2\sin\alpha x\sin\beta y}.
\]

在完整代表半波控制截面 \(y=\ell/2\)，令 \(s=\sin\alpha x\)：

\[
\boxed{\kappa_T=bq\alpha^2s},\qquad
\boxed{\kappa_L=bq\beta^2s}.
\]

在双反节点 \(s=1\)：

\[
\kappa_T=bq\alpha^2,\qquad \kappa_L=bq\beta^2.
\]

BH050 historical family has \(b=1600\) mm, \(a=3200\) mm, \(m_*=2\), hence \(\ell=1600\) mm and \(\alpha=\beta=\pi/1600\). Therefore at the control antinode:

\[
\boxed{\kappa_T=\kappa_L=\pi^2q/1600}.
\]

Initial imperfection \(q_0\) is stress-free. The constitutive curvature increment uses the added displacement \(q\), not \(q+q_0\), under the current Nguyen-type stress-free-imperfection convention.

## 2. Superseded interpretation

The historical force-first R4/J4 bridge used

\[
\mathbf x=(\varepsilon_T^0,\kappa_T,\varepsilon_L^0,\kappa_L)^T
\]

and enforced four resultant matches

\[
N_T^{sec}=N_T^A,\quad M_T^{sec}=M_T^A,\quad N_L^{sec}=N_L^A,\quad M_L^{sec}=M_L^A.
\]

That formulation let \(\kappa_T,\kappa_L\) float as independent section unknowns. Once the displacement field \(w_m(q)\) is accepted as the kinematic ansatz, those two curvature DOFs are duplicated and must no longer be treated as independent.

This correction does **not** assert that Airy mathematics is wrong; it corrects the kinematic identity between global displacement and section curvature.

## 3. Invalidated numerical claims

The following historical/hybrid values are NOT accepted as predictions of the corrected theory and must not be reused as roots or terminal states:

- free-curvature BH050 \(q\approx0.004772819646\) and its old R4/J4 terminal;
- hybrid/common-curvature claim \(q=0.011215527128\), \(P=17.98426079\) MN.

Reason: the corrected theory must be recomputed from the original BH050 inputs and must close the same-state constituent force ledger. A total-load value without a complete same-state UHPC/steel/web resultant decomposition is not an accepted solution.

## 4. Frozen upstream formulas retained for recomputation

Initial A/D stiffness, halfwave selection, Marguerre–Airy membrane field and R02/R06/UHPC material operators are retained unless the recomputation itself proves an incompatibility.

Airy quantities:

\[
Q_q=q(q+2q_0),
\]

\[
P^A(q)=P_{cr}\frac{q}{q+q_0}+C Q_q,
\]

\[
N_T^A=K_xQ_q,
\]

\[
N_L^A=-\left[\frac{P^A(q)}b+GQ_q(1-2s^2)\right].
\]

The historical numerical coefficients may be used only after independent reproduction from the original BH050 input.

## 5. Required recomputation chain

The corrected BH050 calculation must be executed in this order:

1. Recover original BH050 geometry/material input.
2. Recompute initial \(\mathbf A\), \(\bar{\mathbf A}\), \(D_x,D_y,D_{xy},D_\mu,H\).
3. Recompute integer halfwave selection \(m_*\), \(\ell\), \(\alpha,\beta\).
4. Recompute \(P_{cr},C,K_x,G\) and the explicit Airy demand functions.
5. Replace independent section curvatures by
   \[
   \kappa_T(q,s)=bq\alpha^2s,\quad \kappa_L(q,s)=bq\beta^2s.
   \]
6. Using the unchanged current UHPC + R02/R06 steel + web/PBL operators, compute all section resultants from the same current state.
7. Re-derive the independent equation/unknown set after curvature elimination; do not mechanically retain four R4 equations with only two section membrane-strain unknowns.
8. Solve the corrected continuation from \(q=0\) without using FEM/test in root selection.
9. Determine the first mathematically and physically admissible terminal event of the corrected system.
10. At the accepted terminal, explicitly output the same-state force ledger:
    \[
    P_U,\ P_{s,+},\ P_{s,-},\ P_w,
    \]
    and verify
    \[
    P_U+P_{s,+}+P_{s,-}+P_w=P_u
    \]
    within numerical tolerance.
11. Only after the blind theoretical state is frozen, compare with FEM as a post-check.

## 6. Acceptance gate

A corrected BH050 `Pu` is not accepted unless all of the following are simultaneously available:

- root/generalized coordinates;
- curvature from the prescribed displacement field;
- section membrane strains;
- UHPC resultant;
- upper/lower steel resultants;
- web/PBL resultant;
- total-load closure;
- terminal-condition residual;
- constituent percentages summing to 100%.

No parameter fitting, FEM root selection, effective width, or hidden spatial quadrature is allowed.

## 7. Governance

This file is a continuity/correction backup only. It does not modify production `main` and does not yet declare a corrected production theory or a new BH050 prediction.
