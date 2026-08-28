# NZ-SCCM — Nguyen + current terminal 零空间积分显式闭合门禁：UHPC/core normal R01

**日期：2026-08-28**  
**身份：THEORY AUDIT / DIAGNOSTIC ONLY / NOT PRODUCTION**  
**分支：** `diagnostic/bh032-bh050-mode-projection-20260827`  
**执行纪律：** `THEORY FIRST / NO FEM / NO TEST / ZERO FORMAL SPATIAL QUADRATURE / FAIL FAST / FIRST FAILED TERM STOPS EXECUTION`

---

## 0. 本轮唯一任务与停止规则

只检查：

\[
\text{Nguyen-compatible finite kinematics}
\to
(\varepsilon^0,\kappa)
\to
\text{frozen UHPC current directional N-M}
\to
(P_c,R_{\alpha,c},R_{q,c})
\]

能否在一个连续完整半波内实现**零空间数值积分的有限解析/正式 exact-period 闭合**。

本轮只从最简单的 UHPC/core normal 项开始。禁止：

```text
Chebyshev = NO
Gauss/Simpson/adaptive quadrature = NO
spatial/material grid = NO
fitted polynomial = NO
material replacement = NO
new local mode = NO
new special-function family invented as workaround = NO
FEM/test = NO
Pu calculation = NO
```

一旦遇到第一项不能落入当前已经锁定的有限解析 / exact-period 闭合类，立即停止。

---

# G0 — compatible Nguyen/project finite kinematics

采用已经恢复并验证兼容的项目单半波 `(D,alpha,q)` 场。令

\[
X=\pi x/b,\qquad Y=\pi y/\ell,\qquad k=b/\ell,
\]

\[
H=\sin X\sin Y,\qquad S_q=q_0q+\frac12q^2.
\]

normal strains are

\[
\varepsilon_x=\varepsilon_x^0(D,\alpha,q;X,Y)+z\kappa_x(q;X,Y),
\]

\[
\varepsilon_y=\varepsilon_y^0(D,\alpha,q;X,Y)+z\kappa_y(q;X,Y),
\]

with

\[
\kappa_x=\frac{\pi^2q}{b}H,
\qquad
\kappa_y=\frac{\pi^2k^2q}{b}H.
\]

The midplane normal strains are finite combinations of

\[
1,\quad \sin^2X,\quad \sin^2Y,\quad \sin^2X\sin^2Y.
\]

The associated generalized kernels `epsilon^0_,D`, `epsilon^0_,alpha`, `epsilon^0_,q`, `kappa_,q` are finite trigonometric polynomials.

This is a displacement/kinematic closure; no stress is used to reconstruct strain.

```text
G0_NGUYEN_COMPATIBLE_FINITE_KINEMATICS = PASS
```

---

# G1 — frozen UHPC directional current N-M at each (X,Y)

For direction `i in {x,y}` write

\[
A_i=\varepsilon_i^0(X,Y),\qquad B_i=\kappa_i(X,Y),
\]

\[
\varepsilon_i(z)=A_i+B_i z,
\qquad
\varepsilon_{i\pm}=A_i\pm B_i t_c/2.
\]

The frozen terminal/current UHPC operator already defines exact through-thickness primitives

\[
S_0'(\varepsilon)=\sigma_U(\varepsilon),
\qquad
S_1'(\varepsilon)=\varepsilon\sigma_U(\varepsilon),
\]

and hence, for `B_i != 0`,

\[
N_i^U=(1-\rho_w)
\frac{S_0(\varepsilon_{i+})-S_0(\varepsilon_{i-})}{B_i},
\]

\[
M_i^U=(1-\rho_w)
\frac{S_1(\varepsilon_{i+})-S_1(\varepsilon_{i-})
-A_i[S_0(\varepsilon_{i+})-S_0(\varepsilon_{i-})]}{B_i^2}.
\]

At `B_i=0` the apparent divisions are removable limits:

\[
N_i^U\to(1-\rho_w)t_c\sigma_U(A_i),
\qquad
M_i^U\to0.
\]

Thus halfwave boundary lines where `H=0` do not create a spatial cell or numerical singularity.

```text
G1_UHPC_DIRECTIONAL_THICKNESS_NM = PASS
THICKNESS_QUADRATURE = 0
```

---

# G2 — simplest core normal spatial term: ascending compression

Take the Hu ascending compression branch only:

\[
\xi_c=-\varepsilon/\varepsilon_{c0},
\qquad 0\le\xi_c\le1,
\]

\[
\sigma_c=-f_c\frac{n_h\xi_c-\xi_c^2}
{1+(n_h-2)\xi_c}.
\]

Put

\[
a=n_h-2.
\]

The stress is rational in `xi_c`, and an exact primitive is

\[
S_{0,a}=f_c\varepsilon_{c0}
\left[
-\frac{\xi_c^2}{2a}
+\frac{(a+1)^2}{a^2}\xi_c
-\frac{(a+1)^2}{a^3}\log(1+a\xi_c)
\right]
\]
(up to an irrelevant additive constant; the `a=0` degeneration is obtained directly before division).

Likewise `S_{1,a}` is a finite polynomial in `xi_c` plus one `log(1+a xi_c)` term. Therefore the exact `N_i^U,M_i^U` are finite rational/log functions of the two face strains `epsilon_i+/-`.

Now apply the half-angle variables

\[
u=\tan(X/2),\qquad v=\tan(Y/2).
\]

Because the Nguyen normal midplane strain is a finite polynomial in `sin^2 X, sin^2 Y`, and `B_i` is proportional to `sin X sin Y`, both face strains have the form

\[
\boxed{
\varepsilon_{i\pm}
=\frac{P_{i\pm}(u,v;D,\alpha,q)}{(1+u^2)^2(1+v^2)^2}
}
\]

for finite polynomials `P_i+/-` after clearing constant dimensional factors.

Consequently every ascending-compression contribution to

\[
P_c=-\frac1\ell\iint N_y^U\,dA,
\]

\[
R_{\alpha,c}^{(n)}
=\iint\left(
N_x^U\varepsilon^0_{x,\alpha}
+N_y^U\varepsilon^0_{y,\alpha}
\right)dA,
\]

and the normal part of

\[
R_{q,c}^{(n)}
=\iint\left(
N_x^U\varepsilon^0_{x,q}
+N_y^U\varepsilon^0_{y,q}
+M_x^U\kappa_{x,q}
+M_y^U\kappa_{y,q}
\right)dA
\]

is a finite sum of rational/algebraic factors and logarithms of finite polynomials/rational functions.

The branch fronts `epsilon=0` and `epsilon=-eps_c0` become polynomial equations after denominator clearing, so they define finite relative algebraic cycles, not spatial cells.

Under the already-locked NC-M4/NC-M6 integration grammar, rational/algebraic terms and finite log parameter derivatives over such relative algebraic cycles are finite relative/incomplete Aomoto-Gelfand / GKZ exact-period objects.

No NC material law is imported here; only the previously frozen **mathematical integration grammar** is reused.

```text
G2_UHPC_ASCENDING_COMPRESSION_NORMAL_SPATIAL_CLOSURE = PASS
FORMAL_SPATIAL_QUADRATURE = 0
```

---

# G3 — descending compression normal branch

For

\[
\xi_c>1,
\]

the frozen Hu descending compression branch is

\[
\sigma_c=-f_c\frac{\xi_c}{2(\xi_c-1)^2+\xi_c}
=-f_c\frac{\xi_c}{2\xi_c^2-3\xi_c+2}.
\]

The denominator has discriminant

\[
(-3)^2-4(2)(2)=-7<0,
\]

and the exact primitives contain only finite rational terms, logarithms, and arctangents. For example,

\[
\int\frac{x}{2x^2-3x+2}\,dx
=
\frac14\log\left(x^2-\frac32x+1\right)
+\frac{3\sqrt7}{14}\arctan\frac{4x-3}{\sqrt7},
\]

and `int x^2/(2x^2-3x+2) dx` is again a finite rational/log/arctan expression.

Using `arctan z=(2i)^{-1}[log(1+iz)-log(1-iz)]`, these terms remain inside the same finite algebraic/log exact-period family after half-angle substitution. The compression peak front `xi_c=1` is algebraic.

```text
G3_UHPC_DESCENDING_COMPRESSION_NORMAL_SPATIAL_CLOSURE = PASS
FORMAL_SPATIAL_QUADRATURE = 0
```

---

# G4 — first failed item: frozen Hu tensile normal branch

The frozen UHPC source architecture also requires the Hu tensile branch when a directional core strain becomes tensile:

\[
\sigma_t
=f_{ct}e^{1/m}\,\xi_t
\exp\left(-\frac{\xi_t^m}{m}\right),
\]

with

\[
m=0.85-0.47K+0.12K^2
\]

and source-instance tensile parameters.

At fixed `(X,Y)`, the thickness variable enters `xi_t` affinely through

\[
\varepsilon=A_i+B_i z.
\]

Therefore thickness integration itself is exact in incomplete-gamma functions. If `epsilon_t0` denotes the frozen tensile strain scale and

\[
C_t=f_{ct}e^{1/m},
\]

then, up to additive constants,

\[
\boxed{
S_{0,t}
=C_t\varepsilon_{t0}\,
 m^{2/m-1}
\gamma\left(\frac2m,\frac{\xi_t^m}{m}\right)
}
\]

and

\[
\boxed{
S_{1,t}
=C_t\varepsilon_{t0}^2\,
 m^{3/m-1}
\gamma\left(\frac3m,\frac{\xi_t^m}{m}\right).
}
\]

Thus **the thickness gate still passes**.

However, after inserting the Nguyen face strains, the halfwave area kernels contain objects of the form

\[
\gamma\left(\frac2m,
\frac{[R(u,v)]^m}{m}
\right),
\qquad
\gamma\left(\frac3m,
\frac{[R(u,v)]^m}{m}
\right),
\]

multiplied by finite rational/trigonometric kernels, where `R(u,v)` is rational/algebraic after half-angle substitution.

Equivalently, before thickness condensation the spatial/material integrand contains

\[
\boxed{
R(u,v,z)\exp\left[-\frac{R(u,v,z)^m}{m}\right].
}
\]

This is **not** of the currently locked exact-period integrand class

\[
r^{a_0}(1-r)^{a_1}s^{a_2}(1-s)^{a_3}
\prod_h P_h(r,s)^{\lambda_h}
\]

plus finite parameter derivatives that generate logarithms. The exponential factor cannot be produced by a finite number of algebraic powers and log-parameter derivatives.

To continue exactly would require opening a **new** special-function class, e.g. an exponential/confluent period or irregular/confluent GKZ-type backend, and proving its finite coefficient/cycle compilation for the actual Hu tension term. That is a different analytic route and is not already part of the frozen NC-M4 exact-period closure.

Alternatively replacing/expanding the tensile law would change/approximate the material model. Both actions are prohibited by this execution's fail-fast instruction.

No exceptional restriction on `m` is present in the frozen UHPC contract that would force the incomplete-gamma functions to collapse to the existing algebraic/log period class.

Therefore the first non-closable item **under the currently authorized exact-period closure** is the UHPC tensile normal contribution.

```text
G4_UHPC_TENSION_NORMAL_SPATIAL_CLOSURE = FAIL
FAIL_TYPE = ANALYTIC_FUNCTION_CLASS / NOT NUMERICAL
THICKNESS_INTEGRATION = EXACT_PASS
HALFWAVE_SPATIAL_CLOSURE_IN_EXISTING_PERIOD_CLASS = FAIL
NEW_CONFLUENT_OR_EXPONENTIAL_PERIOD_ROUTE = NOT_OPENED
MATERIAL_APPROXIMATION = NOT_USED
```

---

# STOP — fail-fast

Execution stops immediately at G4.

The following are **NOT EXECUTED**:

```text
UHPC shear contribution
steel faces / qU / R02 / R06
web contribution
full Ralpha/Rq assembly
same-source Jacobian
det(Kt) or material-envelope root
Pu
BH032/BH050
FEM/test comparison
```

---

# What this gate proves — and what it does not

It proves:

1. Nguyen/project compatible kinematics + current directional terminal N-M has no old-Airy/current-N compatibility conflict.
2. UHPC normal **compression** (ascending and descending) can be compiled with zero formal spatial quadrature into the already-accepted finite algebraic/log relative exact-period class.
3. The currently frozen **Hu tensile exponential branch** is the first term that leaves that exact-period class.
4. Therefore the **full** UHPC/core normal operator cannot yet be certified as zero-spatial-integral explicit using only the currently frozen integration grammar.

It does **not** prove that no broader exact mathematics can represent the Hu tension term. An exponential/confluent-period construction may exist. It is simply a new route and was deliberately not opened after the first gate failure.

It also does not authorize dropping tension by assuming the core remains in compression. Such a domain restriction would have to be proved from the eventual admissible structural solution; it cannot be assumed to pass this general operator gate.

---

# Final status

```text
THEORY_ONLY = YES
FEM_USED = NO
TEST_USED = NO
PRODUCTION_CHANGED = NO
NGUYEN_COMPATIBLE_KINEMATICS = PASS
UHPC_DIRECTIONAL_NM_THICKNESS_EXACT = PASS
UHPC_ASCENDING_COMPRESSION_SPATIAL_EXACT_PERIOD = PASS
UHPC_DESCENDING_COMPRESSION_SPATIAL_EXACT_PERIOD = PASS
UHPC_TENSION_THICKNESS_PRIMITIVE = PASS_INCOMPLETE_GAMMA
UHPC_TENSION_SPATIAL_EXISTING_EXACT_PERIOD = FAIL
FIRST_FAILED_GATE = G4
EXECUTION_STOPPED_AT_FIRST_FAILED_GATE = YES
PU_COMPUTED = NO
```
