# NZ-SCCM — NC-M4-R123 完整材料本构合同与隐藏矛盾审计

时间：2026-08-20 19:58 +08:00

状态：`ACTIVE_MATERIAL_CANDIDATE_R123 / NOT_YET_PRODUCTION_LOCK`

本文件只处理此前定位的前三项材料问题：

1. R1：不得再用 `epsilon_t0` 作为 TC 压缩削弱的横坐标尺度；
2. R2：删除旧 `beta=1/(1+0.15 t^2)`，恢复 Nguyen Eq.(3.43) 型 cracked-TC compression softening；
3. R3：恢复 equivalent-uniaxial / Poisson-dilation coupling，同时保持显式解析闭合。

本文件不修改第四个结构问题：`epsilon_m` 仍然是当前唯一横向膜变量，不恢复 Airy 面内场。

## A. 基本材料输入与缺失参数规则

输入：

\[
E_0,\ \nu,\ f_c,\ \varepsilon_{c0},\ f_t,\ \varepsilon_{t0}.
\]

若来源未给 `f_t`，项目规则：

\[
\boxed{f_t=0.1f_c}.
\]

参考开裂应变：

\[
\boxed{\varepsilon_{cr}=f_t/E_0}.
\]

NC-M4 张拉骨架：

\[
T_4(t)=1.07515\frac{t(t+0.09)}{1-0.83t+1.04t^2+0.14t^3}.
\]

其原点斜率：

\[
T_4'(0)=1.07515\times0.09=0.0967635.
\]

若要求张拉原点切线严格等于 `E0`：

\[
\boxed{\varepsilon_{t0}=0.0967635\,f_t/E_0=0.0967635\,\varepsilon_{cr}}.
\]

注意 `epsilon_t0 != epsilon_cr`，R123 禁止二者混用。

## B. 物理应变张量、主方向与等效单轴主应变

板坐标工程应变：

\[
\mathbf E=\begin{bmatrix}\varepsilon_x&\gamma_{xy}/2\\\gamma_{xy}/2&\varepsilon_y\end{bmatrix}.
\]

定义

\[
d_\varepsilon=\sqrt{(\varepsilon_x-\varepsilon_y)^2+\gamma_{xy}^2}.
\]

用连续方向标签 `varsigma=+/-1` 保持 1/2 方向身份，不按大小排序：

\[
\varepsilon_1=\frac{\varepsilon_x+\varepsilon_y+\varsigma d_\varepsilon}{2},
\qquad
\varepsilon_2=\frac{\varepsilon_x+\varepsilon_y-\varsigma d_\varepsilon}{2}.
\]

令 `p=cos theta`, `q=sin theta`：

\[
p^2=\frac12\left(1+\varsigma\frac{\varepsilon_x-\varepsilon_y}{d_\varepsilon}\right),
\]
\[
q^2=\frac12\left(1-\varsigma\frac{\varepsilon_x-\varepsilon_y}{d_\varepsilon}\right),
\]
\[
pq=\varsigma\frac{\gamma_{xy}}{2d_\varepsilon}.
\]

R3 采用 Nguyen Eq.(3.21) 的 constant-dilation explicit specialization `v1=v2=nu`：

\[
\varepsilon_1=\widehat\varepsilon_1-\nu\widehat\varepsilon_2,
\qquad
\varepsilon_2=\widehat\varepsilon_2-\nu\widehat\varepsilon_1.
\]

反解：

\[
\boxed{\widehat\varepsilon_1=\frac{\varepsilon_1+\nu\varepsilon_2}{1-\nu^2}},
\qquad
\boxed{\widehat\varepsilon_2=\frac{\varepsilon_2+\nu\varepsilon_1}{1-\nu^2}}.
\]

张量形式：

\[
\boxed{\widehat{\mathbf E}=\frac{(1-\nu)\mathbf E+\nu\operatorname{tr}(\mathbf E)\mathbf I}{1-\nu^2}}.
\]

因此 `Ehat` 与 `E` 共轴，不产生第二个主方向根式。

## C. 必须显式修正的 state-grid 规则

R3 后 raw physical principal strains `(epsilon1,epsilon2)` 与 material-driving equivalent strains `(epshat1,epshat2)` 的符号不保证一致。若仍强制用 raw signs 定义 CC/TC/CT/TT，则 raw-TC 内可能出现 `epshat1<=0`，此时 `T4(t>=0)` 在整格内不再有合法定义，必须增加隐藏的 `epshat1=0` 内部状态前沿。

因此，要维持真正只有四个显式 material cells，R123 的 material-cell membership 必须以 equivalent-uniaxial signs 为准：

- CC: `epshat1<0, epshat2<0`;
- TC: `epshat1>0, epshat2<0`;
- CT: `epshat1<0, epshat2>0`;
- TT: `epshat1>0, epshat2>0`.

raw `(epsilon1,epsilon2)` 仍保留为物理主应变与方向变量。

如果项目治理坚持 raw-sign grid 不可修改，则 R123 不能同时保持“四格内无隐藏分区”；两者必须二选一。本文件为保持显式四区，自洽地采用 equivalent-sign material grid。

## D. scalar skeletons

Compression:

\[
\boxed{C(c)=\frac{2c}{1+c^2}},\qquad c\ge0.
\]

Derivative:

\[
\boxed{C'(c)=\frac{2(1-c^2)}{(1+c^2)^2}}.
\]

Tension:

\[
\boxed{T_4(t)=1.07515\frac{t^2+0.09t}{1-0.83t+1.04t^2+0.14t^3}},\qquad t\ge0.
\]

Let

\[
D_T(t)=1-0.83t+1.04t^2+0.14t^3.
\]

Then

\[
\boxed{T_4'(t)=1.07515\frac{-0.14t^4-0.0252t^3-0.9236t^2+2t+0.09}{D_T(t)^2}}.
\]

CC enhancement:

\[
\boxed{\eta(c_1,c_2)=1+0.16C(c_1)C(c_2)}.
\]

\[
\frac{\partial\eta}{\partial c_1}=0.16C'(c_1)C(c_2),
\qquad
\frac{\partial\eta}{\partial c_2}=0.16C(c_1)C'(c_2).
\]

## E. R2 cracked-TC compression softening

Old `beta=1/(1+0.15 t^2)` is deleted from R123.

Define the equivalent tensile ratio

\[
r=\widehat\varepsilon_t/\varepsilon_{c0}.
\]

The source Eq.(3.43) with positive compression strain scale becomes

\[
\boxed{\gamma_c(r)=\begin{cases}
1,&0\le r\le10/17,\\
\dfrac1{0.8+0.34r},&r>10/17.
\end{cases}}
\]

It is continuous because `0.8+0.34*(10/17)=1`, but not C1 at `r=10/17`.

Derivative wrt r:

\[
\boxed{\gamma_c'(r)=\begin{cases}
0,&0<r<10/17,\\
-\dfrac{0.34}{(0.8+0.34r)^2},&r>10/17.
\end{cases}}
\]

At the front `r=10/17`, one-sided derivatives differ; tangent is branch-sided.

R123 deliberately drives `gamma_c` with the dilation-removed equivalent tensile strain `epshat_t`, not the raw Poisson transverse strain. This is a project translation of Nguyen Eq.(3.43), required to avoid spurious compression softening under exact uniaxial compression.

## F. Four explicit principal-stress cells

### F1 CC

Conditions:

\[
\widehat\varepsilon_1<0,\qquad\widehat\varepsilon_2<0.
\]

\[
c_1=-\widehat\varepsilon_1/\varepsilon_{c0},\qquad c_2=-\widehat\varepsilon_2/\varepsilon_{c0}.
\]

\[
C_1=\frac{2c_1}{1+c_1^2},\qquad C_2=\frac{2c_2}{1+c_2^2}.
\]

\[
\eta=1+0.16C_1C_2.
\]

\[
\boxed{\sigma_1^{CC}=-f_c\left(1+0.16C_1C_2\right)C_1},
\]
\[
\boxed{\sigma_2^{CC}=-f_c\left(1+0.16C_1C_2\right)C_2}.
\]

### F2 TC

Conditions:

\[
\widehat\varepsilon_1>0,\qquad\widehat\varepsilon_2<0.
\]

\[
t_1=\widehat\varepsilon_1/\varepsilon_{t0},\qquad r_1=\widehat\varepsilon_1/\varepsilon_{c0},\qquad c_2=-\widehat\varepsilon_2/\varepsilon_{c0}.
\]

\[
\boxed{\sigma_1^{TC}=f_t\,1.07515\frac{t_1(t_1+0.09)}{1-0.83t_1+1.04t_1^2+0.14t_1^3}},
\]

\[
\boxed{\sigma_2^{TC}=-f_c\,\gamma_c(r_1)\frac{2c_2}{1+c_2^2}}.
\]

Thus explicitly:

for `0<r1<=10/17`,

\[
\boxed{\sigma_2^{TC}=-f_c\frac{2c_2}{1+c_2^2}},
\]

for `r1>10/17`,

\[
\boxed{\sigma_2^{TC}=-f_c\frac{1}{0.8+0.34r_1}\frac{2c_2}{1+c_2^2}}.
\]

### F3 CT

Conditions:

\[
\widehat\varepsilon_1<0,\qquad\widehat\varepsilon_2>0.
\]

\[
c_1=-\widehat\varepsilon_1/\varepsilon_{c0},\qquad t_2=\widehat\varepsilon_2/\varepsilon_{t0},\qquad r_2=\widehat\varepsilon_2/\varepsilon_{c0}.
\]

\[
\boxed{\sigma_1^{CT}=-f_c\,\gamma_c(r_2)\frac{2c_1}{1+c_1^2}},
\]

\[
\boxed{\sigma_2^{CT}=f_t\,1.07515\frac{t_2(t_2+0.09)}{1-0.83t_2+1.04t_2^2+0.14t_2^3}}.
\]

### F4 TT

Conditions:

\[
\widehat\varepsilon_1>0,\qquad\widehat\varepsilon_2>0.
\]

\[
t_i=\widehat\varepsilon_i/\varepsilon_{t0}.
\]

\[
\boxed{\sigma_1^{TT}=f_t\,1.07515\frac{t_1(t_1+0.09)}{1-0.83t_1+1.04t_1^2+0.14t_1^3}},
\]

\[
\boxed{\sigma_2^{TT}=f_t\,1.07515\frac{t_2(t_2+0.09)}{1-0.83t_2+1.04t_2^2+0.14t_2^3}}.
\]

### Zero boundaries

At `epshat1=0` or `epshat2=0`, `C(0)=T4(0)=0`, `gamma_c(0)=1`, `eta` reduces to 1 if the associated C is zero. Hence neighboring cell stresses coincide continuously on the zero boundaries.

## G. Principal tangent wrt equivalent-uniaxial strains

Define

\[
\mathbf K^u=\begin{bmatrix}\partial\sigma_1/\partial\widehat\varepsilon_1&\partial\sigma_1/\partial\widehat\varepsilon_2\\\partial\sigma_2/\partial\widehat\varepsilon_1&\partial\sigma_2/\partial\widehat\varepsilon_2\end{bmatrix}.
\]

TT:

\[
K^u_{11}=\frac{f_t}{\varepsilon_{t0}}T_4'(t_1),\quad K^u_{12}=0,\quad K^u_{21}=0,\quad K^u_{22}=\frac{f_t}{\varepsilon_{t0}}T_4'(t_2).
\]

TC:

\[
K^u_{11}=\frac{f_t}{\varepsilon_{t0}}T_4'(t_1),\qquad K^u_{12}=0,
\]
\[
K^u_{21}=-\frac{f_c}{\varepsilon_{c0}}\gamma_c'(r_1)C(c_2),
\]
\[
K^u_{22}=\frac{f_c}{\varepsilon_{c0}}\gamma_c(r_1)C'(c_2).
\]

CT:

\[
K^u_{11}=\frac{f_c}{\varepsilon_{c0}}\gamma_c(r_2)C'(c_1),
\]
\[
K^u_{12}=-\frac{f_c}{\varepsilon_{c0}}\gamma_c'(r_2)C(c_1),
\]
\[
K^u_{21}=0,
\qquad
K^u_{22}=\frac{f_t}{\varepsilon_{t0}}T_4'(t_2).
\]

CC: let `Di=C'(ci)` and `k_eta=0.16`.

\[
K^u_{11}=\frac{f_c}{\varepsilon_{c0}}D_1\left[\eta+k_\eta C_1C_2\right]
=\frac{f_c}{\varepsilon_{c0}}D_1\left[1+2k_\eta C_1C_2\right],
\]

\[
K^u_{12}=\frac{f_c k_\eta}{\varepsilon_{c0}}C_1^2D_2,
\]

\[
K^u_{21}=\frac{f_c k_\eta}{\varepsilon_{c0}}C_2^2D_1,
\]

\[
K^u_{22}=\frac{f_c}{\varepsilon_{c0}}D_2\left[1+2k_\eta C_1C_2\right].
\]

In general `K12 != K21`; R123 remains a current stress operator, not a proven hyperelastic potential.

## H. Tangent from physical principal strains

Equivalent-strain Jacobian:

\[
\mathbf A_\nu=\frac1{1-\nu^2}\begin{bmatrix}1&\nu\\\nu&1\end{bmatrix}.
\]

Hence with principal axes held fixed:

\[
\boxed{\mathbf K^p=\mathbf K^u\mathbf A_\nu}.
\]

Explicitly:

\[
K^p_{11}=\frac{K^u_{11}+\nu K^u_{12}}{1-\nu^2},\qquad
K^p_{12}=\frac{\nu K^u_{11}+K^u_{12}}{1-\nu^2},
\]

\[
K^p_{21}=\frac{K^u_{21}+\nu K^u_{22}}{1-\nu^2},\qquad
K^p_{22}=\frac{\nu K^u_{21}+K^u_{22}}{1-\nu^2}.
\]

## I. Rotation back to x-y and full engineering tangent ingredients

\[
\sigma_x=p^2\sigma_1+q^2\sigma_2,
\]
\[
\sigma_y=q^2\sigma_1+p^2\sigma_2,
\]
\[
\tau_{xy}=pq(\sigma_1-\sigma_2).
\]

Principal-strain derivatives:

\[
\varepsilon_{1,\varepsilon_x}=p^2,\quad\varepsilon_{2,\varepsilon_x}=q^2,
\]
\[
\varepsilon_{1,\varepsilon_y}=q^2,\quad\varepsilon_{2,\varepsilon_y}=p^2,
\]
\[
\varepsilon_{1,\gamma}=pq,\quad\varepsilon_{2,\gamma}=-pq.
\]

Direction derivatives for `d_epsilon != 0`:

\[
\theta_{,\varepsilon_x}=-\frac{\gamma_{xy}}{2d_\varepsilon^2},\qquad
\theta_{,\varepsilon_y}=+\frac{\gamma_{xy}}{2d_\varepsilon^2},
\]
\[
\theta_{,\gamma}=\frac{\varepsilon_x-\varepsilon_y}{2d_\varepsilon^2}.
\]

For `g in {epsilon_x,epsilon_y,gamma}`:

\[
\sigma_{1,g}=K^p_{11}\varepsilon_{1,g}+K^p_{12}\varepsilon_{2,g},
\]
\[
\sigma_{2,g}=K^p_{21}\varepsilon_{1,g}+K^p_{22}\varepsilon_{2,g}.
\]

Then

\[
\boxed{\sigma_{x,g}=p^2\sigma_{1,g}+q^2\sigma_{2,g}+2pq(\sigma_2-\sigma_1)\theta_{,g}},
\]

\[
\boxed{\sigma_{y,g}=q^2\sigma_{1,g}+p^2\sigma_{2,g}+2pq(\sigma_1-\sigma_2)\theta_{,g}},
\]

\[
\boxed{\tau_{xy,g}=pq(\sigma_{1,g}-\sigma_{2,g})+(p^2-q^2)(\sigma_1-\sigma_2)\theta_{,g}}.
\]

These nine derivatives constitute the full current engineering tangent away from repeated principal strains and material fronts.

## J. Small-strain proof

For `epshat_i` near zero, tension initial tangent is `E0` by construction. Compression initial tangent of the fixed `C(c)=2c/(1+c^2)` law is

\[
E_{c,0}^{model}=2f_c/\varepsilon_{c0}.
\]

If `E0=2fc/epsc0` exactly, then

\[
\sigma_1=\frac{E_0}{1-\nu^2}(\varepsilon_1+\nu\varepsilon_2),
\qquad
\sigma_2=\frac{E_0}{1-\nu^2}(\varepsilon_2+\nu\varepsilon_1),
\]

and exact plane-stress Poisson response is recovered. For Case21 `E0 epsc0/fc=2.000512953...`, so this consistency is satisfied to about 0.026%. For general panels it is an explicit parameter-compatibility condition; current R123 does not yet retune the fixed coefficient 2.

## K. Analytic-integration compatibility

`epshat_i` are linear combinations of the original principal strains. Since the old principal strains lie in `Q(u,v,zeta,W)` with one algebraic radical `W`, R3 adds no second radical.

`T4`, `C`, `eta`, and each branch of `gamma_c` are rational functions of `epshat_i`; therefore every CC/TC/CT/TT local stress remains rational in the same algebraic field.

The only new R2 front is

\[
\widehat\varepsilon_t=(10/17)\varepsilon_{c0},
\]

which is algebraic. Thus the existing half-angle -> algebraic lift -> residue/relative-GKZ integration architecture survives. A new circuit/master compilation is required; the old exact size `99x155` is not assumed unchanged.

## L. Hidden-contradiction audit

1. **State-grid conflict exposed and resolved in this draft:** after R3, raw-sign and equivalent-sign grids differ. Four-cell closure requires equivalent-sign material membership. If raw-sign governance is retained, additional internal zero-fronts are unavoidable.
2. **R2 gamma is C0 but not C1 at `r=10/17`:** stress is continuous, tangent has a finite jump. This is source-derived, not an artificial threshold; same-source Jacobian is branch-sided at the front.
3. **No scalar strain-energy potential is guaranteed:** TC has `K12=0` but generally `K21!=0`; CC also generally `K12!=K21`. Formal structure must continue to use current virtual-work resultants and direct Jacobian derivatives, not Hessians of a scalar energy.
4. **Full Nguyen dilation is not restored:** Nguyen allows state-dependent `v1,v2` depending on secant moduli; R123 uses the explicit constant specialization `v1=v2=nu` to preserve zero-local-Newton analytic closure. This is a deliberate simplification.
5. **Full Nguyen cracked shear-retention is not restored:** current NC-M4-R123 remains coaxial in the principal normal response and obtains global `tau_xy` by spectral rotation. Nguyen's separate postcracking shear-retention modulus is outside R1-R3 and remains an open omitted mechanism.
6. **T4 peak-strain consistency remains open:** with `eps_t0=0.0967635 ft/E0`, the current T4 peak is at `tp≈1.5716248`, so `eps_t,peak≈0.152076 ft/E0=0.152076 eps_cr`, while normalized peak stress is approximately `0.999956 ft`. This means the current T4 reaches tensile strength at only ~15.2% of the elastic cracking strain `ft/E0`; this is a pre-existing NC-M4 issue, not repaired by R1-R3.
7. **Compression initial-slope compatibility is conditional:** exact `E0` recovery requires `E0 epsc0/fc=2`; Case21 satisfies this nearly exactly, but arbitrary future datasets may not.

Therefore NC-M4-R123 is mathematically explicit and analytically integrable, but is not yet contradiction-free enough for production lock until the user decides the state-grid governance and whether the pre-existing T4/shear-retention issues should be reopened.
