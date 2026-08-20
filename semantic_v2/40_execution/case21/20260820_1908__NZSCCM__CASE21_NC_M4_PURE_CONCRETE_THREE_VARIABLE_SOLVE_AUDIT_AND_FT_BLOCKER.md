# NZ-SCCM — Case21 NC-M4 纯混凝土三变量极限求解：原始输入门禁、完整方程组与独立数值审计

时间：2026-08-20 19:08 +08:00

状态：`FORMAL_SOURCE_UNIQUE_SOLVE = BLOCKED_BY_FT_INPUT`; `DIRECT_CONTINUOUS_AUDIT = COMPLETED_NONPRODUCTION`

## 1. 当前任务

钢筋/钢壳关闭。采用已冻结到当前节点的 Nguyen 连续二阶运动学 + NC-M4 current operator + 三变量 `(Delta,A,epsilon_m)`，求纯混凝土 Case21 极限承载力。

正式生产边界仍为：空间 Gauss/Simpson/adaptive quadrature/material-point grid = 0。下文数值积分仅作为独立审计，不取得生产理论身份。

## 2. Case21 原始输入

来自既有 Case21 blind input：

\[
b=\ell=1220\ \mathrm{mm},\qquad h=19.30\ \mathrm{mm},
\]
\[
f_c=21.23\ \mathrm{MPa},\qquad E_0=20321\ \mathrm{MPa},
\]
\[
\varepsilon_{c0}=0.00209,\qquad \nu=0.18,
\]
\[
q_0=1/400,\qquad A_0=b/400=3.05\ \mathrm{mm}.
\]

钢筋全部关闭。

### 唯一原始输入缺口

当前 NC-M4 还需要 `f_t` 与 `epsilon_t0`。Swartz/Nguyen Case21 原始表没有给 Case21 实测 `f_t`；历史 source-input audit 已明确把 `ft` 标记为 BLOCK。因此只凭“原始 Case21 参数”不能形成 source-unique NC-M4 数值根。

若要求 NC-M4 在原点的拉伸初始切线等于 Nguyen 的 `E0`，则

\[
T_4'(0)=1.07515\times0.09=0.0967635,
\]

故

\[
\boxed{\varepsilon_{t0}=\frac{0.0967635 f_t}{E_0}.}
\]

只需再锁定一个 `f_t`，`epsilon_t0` 即随之确定。

## 3. 当前 exact no-spatial-integral global functions

当前 shared-GKZ master 已给出

\[
R_m=C_m\Phi_m,\qquad P=C_P\Phi_P,\qquad R_A=C_A\Phi_A,
\]

其中

\[
C_m=C_A=\frac{2b\ell h}{\pi^2},\qquad C_P=-\frac{2bh}{\pi^2},
\]

\[
\Phi_j=\operatorname{RGKZ}_{A^*_{M4,global}}(\beta_j;\mathbf c(\Delta,A,\varepsilon_m)\mid\Gamma_{phys}),
\quad j\in\{m,P,A\},
\]

且同一个 master 为 `99 x 155`, 由 48 个 explicit polynomial relations + 51 variables 构成。

## 4. 同源导数与最终三元非线性系统

对 `g in {Delta,A,m}`：

\[
\Phi_{j,g}=\sum_{r=1}^{155}c_{r,g}\,\partial_{c_r}\Phi_j,
\]

因此

\[
R_{m,g}=C_m\Phi_{m,g},\qquad
R_{A,g}=C_A\Phi_{A,g},\qquad
P_{,g}=C_P\Phi_{P,g}.
\]

`partial_{c_r} Phi` 属于同一 GKZ master 的 coefficient derivative / contiguous family，不引入第二套积分。

最终未知量

\[
\mathbf q=(\Delta,A,\varepsilon_m)^T.
\]

完整三元系统：

\[
\boxed{F_1=R_A(\Delta,A,\varepsilon_m)=0,}
\]
\[
\boxed{F_2=R_m(\Delta,A,\varepsilon_m)=0,}
\]
\[
\boxed{
\begin{aligned}
F_3={}&P_{,\Delta}R_{A,A}R_{m,m}
-P_{,\Delta}R_{A,m}R_{m,A}\\
&-P_{,A}R_{A,\Delta}R_{m,m}
+P_{,A}R_{A,m}R_{m,\Delta}\\
&+P_{,m}R_{A,\Delta}R_{m,A}
-P_{,m}R_{A,A}R_{m,\Delta}=0.
\end{aligned}}
\]

Equivalently `F3=det(J_lim)=0` with

\[
J_{lim}=\begin{bmatrix}
P_{,\Delta}&P_{,A}&P_{,m}\\
R_{A,\Delta}&R_{A,A}&R_{A,m}\\
R_{m,\Delta}&R_{m,A}&R_{m,m}
\end{bmatrix}.
\]

## 5. Mathematical proof of limit condition

On `R_A=R_m=0`, define

\[
J_c=\begin{bmatrix}R_{A,A}&R_{A,m}\\R_{m,A}&R_{m,m}\end{bmatrix}.
\]

If `det J_c != 0`, implicit-function theorem gives local functions `A(Delta), epsilon_m(Delta)` and

\[
\begin{bmatrix}A'\\\varepsilon_m'\end{bmatrix}
=-J_c^{-1}\begin{bmatrix}R_{A,\Delta}\\R_{m,\Delta}\end{bmatrix}.
\]

Hence

\[
\frac{dP}{d\Delta}
=P_{,\Delta}-[P_{,A}\ P_{,m}]J_c^{-1}
\begin{bmatrix}R_{A,\Delta}\\R_{m,\Delta}\end{bmatrix}.
\]

Direct 3x3 determinant expansion gives

\[
\boxed{\det J_{lim}=\det J_c\,\frac{dP}{d\Delta}.}
\]

Therefore for an ordinary fold (`det J_c != 0`):

\[
\det J_{lim}=0\iff dP/d\Delta=0.
\]

A candidate root must additionally satisfy local maximum (`d^2P/dDelta^2<0`) and lie on the equilibrium branch continuously connected to the origin. Root selection by experimental proximity is prohibited.

## 6. Nonproduction direct-continuous audit closure

Because the original Case21 dataset does not contain `f_t`, the following is explicitly diagnostic only:

\[
f_t=0.1f_c=2.123\ \mathrm{MPa},
\]

where `0.1` is inherited only from the historical NC tensile-amplitude ratio and is NOT a Case21 measured tensile strength.

Then initial-tangent consistency gives

\[
\varepsilon_{t0}=\frac{0.0967635\times2.123}{20321}
=1.01091929777\times10^{-5}.
\]

Using the exact same continuous strain field and NC-M4 local stress equations, tensor-product Gauss was used only as an independent audit evaluator; derivatives for the fold audit were finite-difference derivatives of that direct-continuous evaluator. Neither is formal production.

### Audit convergence

| area x area x thickness | Pu (kN) |
|---|---:|
|20 x 20 x 14|288.8660|
|24 x 24 x 16|288.7589|
|28 x 28 x 18|288.6677|
|32 x 32 x 20|288.6624|
|36 x 36 x 24|288.7177|
|40 x 40 x 28|288.7208|
|44 x 44 x 30|288.7205|

Final audit root at 44 x 44 x 30:

\[
\boxed{\Delta_u^{audit}=1.17258497\ \mathrm{mm}},
\]
\[
\boxed{A_u^{audit}=2.84803957\ \mathrm{mm}},
\]
\[
\boxed{\varepsilon_{m,u}^{audit}=-3.28075016\times10^{-5}},
\]
\[
\boxed{P_u^{audit}=288.7205038\ \mathrm{kN}}.
\]

Residuals:

\[
R_m\approx-5.53\times10^{-3},\qquad R_A\approx-1.98\times10^{-6}
\]

in the direct evaluator's native force/generalized-force units; relative to their constitutive cancellation scales these are essentially zero.

Audit Jacobian (rows `P,R_A,R_m`; columns `Delta,A,epsilon_m`):

\[
J_{lim}^{audit}\approx
\begin{bmatrix}
1.67796009\times10^5&-4.48232029\times10^4&-1.73585950\times10^9\\
-1.63926787\times10^3&4.50105975\times10^2&2.53536574\times10^7\\
-8.11022857\times10^5&1.06029838\times10^6&5.88477433\times10^{11}
\end{bmatrix}.
\]

Because the raw determinant is severely ill-scaled, row-normalized determinant is used for the audit:

\[
\boxed{\det_{norm}\approx-2.12\times10^{-21}},
\]

confirming the determinant cancellation numerically.

Local branch check at `Delta_u +/- 0.005 mm` after re-solving `R_A=R_m=0`:

\[
P(\Delta_u-0.005)\approx288.7102742\ \mathrm{kN},
\]
\[
P(\Delta_u)\approx288.7205038\ \mathrm{kN},
\]
\[
P(\Delta_u+0.005)\approx288.7100375\ \mathrm{kN}.
\]

Central curvature estimate:

\[
\boxed{d^2P/d\Delta^2\approx-827.84\ \mathrm{kN/mm^2}<0},
\]

so this diagnostic root is a local load maximum on the audited equilibrium branch.

## 7. Status and next gate

- The **mathematical three-variable limit system is closed**.
- The exact no-spatial-integral `R_m,P,R_A` master is closed at standard-function representation level.
- A unique source-input Case21 NC-M4 `Pu` is NOT yet available because `f_t` is absent from the original specimen data.
- `288.7205 kN` is an independent diagnostic value under the explicit transferred assumption `f_t=0.1fc`, not a production prediction.
- To promote a numerical value to formal production, first lock/provide `f_t` (then `epsilon_t0` follows from initial-tangent consistency if that rule remains adopted), and evaluate the exact shared-GKZ derivatives rather than spatial quadrature/finite differences.
