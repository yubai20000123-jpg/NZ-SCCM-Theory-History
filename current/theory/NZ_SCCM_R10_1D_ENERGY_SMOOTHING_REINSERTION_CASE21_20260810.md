# NZ-SCCM R10 — 1D ENERGY SMOOTHING → SAME MULTIAXIAL REINSERTION → CASE21

**Date:** 2026-08-10 23:52 +08:00  
**Identity:** corrected current-mainline execution. This is not a global material-potential refit.

## 1. Scope

R10 executes exactly the corrected chain:

```text
existing multidimensional/current NC operator
→ internal 1D Foster tensile scalar
→ material-energy smoothing of that 1D scalar only
→ reinsert into the SAME U/C/T + CC/TC/TT + spectral map
→ Case21 continuous-halfwave same-equation audit
```

No multidimensional interaction coefficient is re-fitted. No Case21/Swartz experimental load is used to choose the smoothing.

The formal zero-spatial D15 production recompile is intentionally deferred to R10B; the Case21 structural calculation in R10 uses high-order full-halfwave Gauss integration only as an audit/reinsertion check and is not relabelled as production.

---

## 2. Frozen NC scalar source

Case21 NC material constants:

\[
f_c=21.23\ \mathrm{MPa},\quad
E_0=20321\ \mathrm{MPa},\quad
\varepsilon_0=0.00209,\quad
\nu=0.18,
\]

\[
\kappa=\frac{E_0\varepsilon_0}{f_c}=2.0005129533678754,
\quad \rho=0.1,
\]

\[
x_{cr}=\frac{\rho}{\kappa}=0.04998717945397425.
\]

The current operator's positive scalar coordinate is

\[
t=\Pi_\eta(\lambda),
\]

and its Foster tensile utilization is

\[
T_{src}(t)=r+(m_t-1)H(r,1)-m_tH(r,10),
\qquad r=t/x_{cr},
\]

with

\[
m_t=-\frac7{90}.
\]

The tensile stress scalar entering the current operator is

\[
u_{t,src}(t)=\rho T_{src}(t).
\]

The source scalar work over the retained tensile interval is

\[
\boxed{
W_{src}=\int_0^{10x_{cr}}u_{t,src}(t)\,dt
=0.031741235181249904.
}
\]

The source peak is

\[
\boxed{
\max u_{t,src}=0.09867291206823792.
}
\]

The retained residual level at \(10x_{cr}\) is \(0.03\).

---

## 3. Fixed C2 energy-smoothing template

No arbitrary plateau value is selected. The smoothing has one retained scalar height \(h\), and \(h\) is fixed uniquely by material work.

### 3.1 Rise branch

For

\[
0\le t\le x_{cr},\qquad \tau=t/x_{cr},
\]

use a quintic satisfying

\[
u(0)=0,\qquad u'(0)=\kappa,\qquad u''(0)=0,
\]

\[
u(x_{cr})=h,\qquad u'(x_{cr})=0,\qquad u''(x_{cr})=0.
\]

After applying these constraints:

\[
\boxed{
u_{rise}(\tau)=
0.1\tau
+0.3799750427197293\tau^3
-0.6699625640795939\tau^4
+0.28798502563183753\tau^5.
}
\]

### 3.2 Decay branch

For

\[
x_{cr}\le t\le10x_{cr},\qquad
\tau=\frac{t-x_{cr}}{9x_{cr}},
\]

use the unique quintic satisfying

\[
u(x_{cr})=h,\quad u'(x_{cr})=u''(x_{cr})=0,
\]

\[
u(10x_{cr})=0.03,\quad u'(10x_{cr})=u''(10x_{cr})=0.
\]

The adopted branch is

\[
\boxed{
u_{fall}(\tau)=
0.09799750427197301
-0.6799750427197289\tau^3
+1.0199625640795933\tau^4
-0.40798502563183736\tau^5.
}
\]

### 3.3 Energy condition

The defining condition is

\[
\boxed{
\int_0^{10x_{cr}}u_{sm}(t)\,dt
=
\int_0^{10x_{cr}}u_{t,src}(t)\,dt.
}
\]

This gives

\[
\boxed{h=0.09799750427197301.}
\]

Therefore

\[
W_{sm}=W_{src}=0.031741235181249904
\]

exactly at the adopted numerical precision.

The peak is reduced only by

\[
\boxed{0.6844916017\%},
\]

while the narrow Foster transition is replaced by a broad C2 rounded scalar branch. The residual, origin tangent, total retained scalar work, monotone rise/fall identity and endpoint derivative regularity are retained.

All polynomial constants above are algebraically derived from physical/energy anchors; they are not free material regression coefficients.

---

## 4. Reinsertion into the SAME multidimensional current operator

Only the tensile scalar is changed:

\[
T_i^{new}=u_{sm}(t_i)/\rho.
\]

The current master remains

\[
U_i=\kappa\lambda_i-C_i+\kappa c_i+\rho T_i-\kappa t_i.
\]

The same multiaxial interaction remains

\[
s_+=U_+-a_{cc}C_+^2C_-+C_+T_--\rho a_tT_+T_-^8,
\]

\[
s_-=U_--a_{cc}C_-^2C_++C_-T_+-\rho a_tT_-T_+^8.
\]

The same spectral return then generates \(\sigma_x,\sigma_y,\tau_{xy}\).

Thus R10 is genuinely

\[
\boxed{
\text{current multidimensional law}
\to\text{1D scalar smoothing}
\to\text{same multidimensional law}.
}
\]

It does not introduce a replacement global material potential.

---

## 5. Case21 same-execution audit

The source Foster operator and the energy-smoothed operator are recomputed in the **same execution**, using the same geometry, Nguyen kinematics, current-map code, reinforcement model and structural evaluator.

Final audit values reclose both \(D\) and \(q\) with the same 48×48×28 full-halfwave Gauss evaluator.

### 5.1 Same-execution source baseline

\[
D_u=0.705727\ \text{(approximately)},
\qquad
q_u=0.002194\ \text{(approximately)},
\]

\[
A_u=2.676738\ \mathrm{mm},
\]

\[
P_c=316.630682\ \mathrm{kN},
\qquad
P_s=25.703347\ \mathrm{kN},
\]

\[
\boxed{P_u=342.334029\ \mathrm{kN}}.
\]

The reclosed equilibrium residual is approximately

\[
1.42\times10^{-12}\ \mathrm{kN\,mm}.
\]

### 5.2 Energy-smoothed 1D result

\[
\boxed{D_u=0.843270\ \text{(approximately)}},
\]

\[
\boxed{q_u=0.001783\ \text{(approximately)}},
\]

\[
\boxed{A_u=2.175523\ \mathrm{mm}},
\]

\[
P_c=337.863269\ \mathrm{kN},
\qquad
P_s=30.860195\ \mathrm{kN},
\]

\[
\boxed{P_u=368.723464\ \mathrm{kN}}.
\]

The reclosed equilibrium residual is approximately

\[
-1.92\times10^{-8}\ \mathrm{kN\,mm}.
\]

Compared with the Case21 experiment

\[
P_f=368.312750\ \mathrm{kN},
\]

the audit difference is

\[
\boxed{+0.111512\%}.
\]

The same-execution change caused solely by the frozen 1D material-energy smoothing is approximately

\[
\boxed{\Delta P_u=26.389435\ \mathrm{kN}}.
\]

This near agreement is explicitly classified as a **post-freeze consequence**, not a calibration target.

At the energy-smoothed audit root the principal equivalent-strain ranges are approximately

\[
\lambda_+\in[-0.080641,\ 0.080821],
\]

\[
\lambda_-\in[-0.923911,\ -0.762450].
\]

---

## 6. Status boundary

```text
R10_1D_ENERGY_SMOOTHING          = PASS
MULTIAXIAL_REINSERTION           = PASS
CASE21_SAME_EXECUTION_AUDIT      = PASS
STRUCTURAL_CALIBRATION_TO_Pf     = NO
SWARTZ24                          = NOT_STARTED
```

However the R10 structural evaluator uses spatial Gauss integration **only as an audit**. Therefore:

```text
FORMAL_ZERO_SPATIAL_QUADRATURE_PRODUCTION
= HOLD_UNTIL_EXISTING_D15_COMPILER_IS_REBUILT_WITH_FROZEN_SMOOTH_SCALAR
```

The next formal task must make **no further material change**. It must feed the frozen R10 scalar law into the already-existing zero-spatial nested-D15 compiler, recover explicit \(P(D,q),R_q(D,q)\) and same-expression derivatives, and solve

\[
R_q=0,
\]

\[
L=P_{,D}R_{q,q}-P_{,q}R_{q,D}=0.
\]

Only after that passes can the R10 capacity be promoted from audit consequence to formal zero-spatial production result.

```text
CURRENT_RECOMMENDED_NEXT_TASK
= R10B_RECOMPILE_FROZEN_ENERGY_SMOOTH_SCALAR_IN_EXISTING_ZERO_SPATIAL_D15_BACKEND
```
