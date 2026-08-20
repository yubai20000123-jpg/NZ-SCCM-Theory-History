# NZ-SCCM — NC-M6 architecture candidate + constitutive gate audit

时间：2026-08-20 22:11 +08:00

状态：`NC_M6_ARCHITECTURE_CANDIDATE / STRESS_GATE_PASS / PHYSICAL_CONSISTENT_TANGENT_GATE_PASS / UNIAXIAL_DEGENERATION_GATE_PASS / VIRTUAL_WORK_CONJUGACY_GATE_PASS / FULL_DOMAIN_BOUNDEDNESS_GATE_PASS`

本节点不计算 Case21，不重新拟合 T5，不增加任何材料修复项。

## 0. 治理边界

唯一材料参考继续固定为 `NC-基准本构`。

NC-M6 参考 NC-M4 / NC-M4-R12 的外部形式：

`physical strain -> physical principal strains -> explicit principal stresses -> physical stress rotation -> consistent tangent -> virtual-work residual`。

冻结 NC 物理目标：

\[
CC:\quad c_i^*=c_i(1+a_{cc}c_1c_2),\qquad a_{cc}=0.1072329249362415,
\]

\[
TC/CT:\quad c^*=c(1-\tau),
\]

\[
TT:\quad \tau_i^*=\tau_i(1-a_t\tau_j^8),\qquad a_t=1-2^{-1/8}=0.08299595679532878.
\]

NC-M6 永久不含旧 NC-M4 `beta=1/(1+0.15t^2)`，也不含 NC-M4-R12 additive `Pi_i`。

## 1. 物理应变、主应变和 Poisson 显式代数消元

\[
\mathbf E=\begin{bmatrix}\varepsilon_x&\gamma_{xy}/2\\\gamma_{xy}/2&\varepsilon_y\end{bmatrix}.
\]

\[
\varepsilon_{1,2}=\frac{\varepsilon_x+\varepsilon_y}{2}
\pm\frac12\sqrt{(\varepsilon_x-\varepsilon_y)^2+\gamma_{xy}^2}.
\]

只保留这一套物理主方向。

定义显式代数材料驱动应变：

\[
\bar\varepsilon_1=\frac{\varepsilon_1+\nu\varepsilon_2}{1-\nu^2},\qquad
\bar\varepsilon_2=\frac{\varepsilon_2+\nu\varepsilon_1}{1-\nu^2}.
\]

它们不是新自由度、不是第二状态格、不需要 material Newton。

定义

\[
\lambda_i=\bar\varepsilon_i/\varepsilon_{c0},\qquad
\kappa=\frac{E_0\varepsilon_{c0}}{f_c},\qquad
\rho=\frac{f_t}{f_c},\qquad
x_{cr}=\frac{\rho}{\kappa}=\frac{f_t}{E_0\varepsilon_{c0}}.
\]

## 2. 冻结 primitive

压缩：

\[
C(c)=\frac{\kappa c}{1+(\kappa-2)c+c^2},\qquad c\ge0.
\]

拉伸理论定义保持为冻结的 C2-regularized NC target：

\[
\tau=T_{NC}(r),\qquad r=\lambda/x_{cr}.
\]

本节点不把 T5 重新定义为物理本构；T5 仅保留为未来可能使用的解析编译形式。

冻结 target 已知：`T_NC(0)=0`, `T_NC'(0)=1`, `0<=T_NC<=0.977862112142`, 远端 residual 为 0.3。

## 3. NC-M6 四区主应力

### CC

\[
\lambda_1<0,\quad\lambda_2<0,
\]

\[
c_i=-\lambda_i,\qquad h=1+a_{cc}c_1c_2,
\]

\[
s_1=-C(c_1h),\qquad s_2=-C(c_2h).
\]

### TC

\[
\lambda_1\ge0,\quad\lambda_2<0,
\]

\[
\tau_1=T_{NC}(\lambda_1/x_{cr}),\qquad c_2=-\lambda_2,
\]

\[
s_1=\rho\tau_1,\qquad s_2=-C[c_2(1-\tau_1)].
\]

### CT

严格交换 1、2：

\[
s_1=-C[c_1(1-\tau_2)],\qquad s_2=\rho\tau_2.
\]

### TT

\[
\tau_i=T_{NC}(\lambda_i/x_{cr}),
\]

\[
s_1=\rho\tau_1(1-a_t\tau_2^8),\qquad
s_2=\rho\tau_2(1-a_t\tau_1^8).
\]

物理主应力：

\[
\sigma_i=f_c s_i.
\]

随后用唯一物理主方向旋回得到 `sigma_x,sigma_y,tau_xy`。

## 4. stress gate

### 4.1 sector-front continuity

在 CC-TC 边界 `lambda1=0`：两侧均严格给出

\[
s_1=0,\qquad s_2=-C(c).
\]

TC-TT 边界 `lambda2=0`：两侧均严格给出

\[
s_1=\rho\tau_1,\qquad s_2=0.
\]

其余边界由交换对称性同理。

因此 `FINITE_FRONT_STRESS_CONTINUITY = PASS`。

### 4.2 repeated-eigenvalue orientation independence

当 `eps1=eps2` 时，由交换对称性有 `sigma1=sigma2`，所以应力张量与主方向选择无关；原点亦为零应力。

因此 global physical stress map 连续且定义良好。

## 5. exact principal normal tangent

令

\[
\mathbf H_\nu=\frac1{1-\nu^2}\begin{bmatrix}1&\nu\\\nu&1\end{bmatrix},
\qquad
\frac{\partial\boldsymbol\lambda}{\partial\boldsymbol\varepsilon_p}
=\frac1{\varepsilon_{c0}}\mathbf H_\nu.
\]

记

\[
\mathbf J_\lambda=\frac{\partial(s_1,s_2)}{\partial(\lambda_1,\lambda_2)}.
\]

则物理 principal-normal consistent tangent 为

\[
\boxed{
\mathbf A
=\frac{f_c}{\varepsilon_{c0}}\mathbf J_\lambda\mathbf H_\nu.
}
\]

其中 `C'=dC/dc`，`g_i=T_NC'(r_i)/xcr`。

### CC

令 `u1=c1h`, `u2=c2h`：

\[
\mathbf J_\lambda^{CC}=
\begin{bmatrix}
(1+2a_{cc}c_1c_2)C'(u_1)&a_{cc}c_1^2C'(u_1)\\
a_{cc}c_2^2C'(u_2)&(1+2a_{cc}c_1c_2)C'(u_2)
\end{bmatrix}.
\]

### TC

令 `u2=c2(1-tau1)`：

\[
\mathbf J_\lambda^{TC}=
\begin{bmatrix}
\rho g_1&0\\
c_2g_1C'(u_2)&(1-\tau_1)C'(u_2)
\end{bmatrix}.
\]

CT 为交换形式。

### TT

\[
\mathbf J_\lambda^{TT}=\rho
\begin{bmatrix}
g_1(1-a_t\tau_2^8)&-8a_t\tau_1\tau_2^7g_2\\
-8a_t\tau_2\tau_1^7g_1&g_2(1-a_t\tau_1^8)
\end{bmatrix}.
\]

这些是 exact branch Jacobians；没有新增材料物理项。

## 6. full physical engineering tangent: required spectral term

仅有 `A` 还不是完整的 global engineering tangent，因为任意虚应变还会改变 principal directions。

在当前 principal frame 中，完整 engineering tangent 必须写为

\[
\boxed{
\mathbf D_p^{eng}=
\begin{bmatrix}
A_{11}&A_{12}&0\\
A_{21}&A_{22}&0\\
0&0&G_{12}^{sp}
\end{bmatrix},
}
\]

其中，当 `eps1 != eps2`：

\[
\boxed{
G_{12}^{sp}=\frac{\sigma_1-\sigma_2}{2(\varepsilon_1-\varepsilon_2)}.
}
\]

当 `eps1=eps2` 时取连续极限；在交换对称状态

\[
G_{12}^{sp}=\frac{A_{11}-A_{12}}{2}.
\]

再用当前主方向的 stress/engineering-strain transformation 旋回：

\[
\boxed{
\mathbf D_{xy}=\mathbf T_\sigma^{-1}\mathbf D_p^{eng}\mathbf T_\varepsilon.
}
\]

这是后续虚功 Jacobian 应采用的物理一致 tangent。

该 spectral shear term 是对既定 stress map 的完整微分，不是新增 constitutive repair。

## 7. origin plane-stress gate

因为

\[
C(c)=\kappa c+O(c^2),\qquad
\rho T_{NC}(\lambda/x_{cr})=\kappa\lambda+O(\lambda^2),
\]

四区均有

\[
\mathbf J_\lambda(0)=\kappa\mathbf I.
\]

所以

\[
\mathbf A(0)=\frac{E_0}{1-\nu^2}\begin{bmatrix}1&\nu\\\nu&1\end{bmatrix},
\]

且 spectral limit

\[
G_{12}^{sp}(0)=\frac{E_0}{2(1+\nu)}.
\]

最终

\[
\boxed{
\mathbf D_0=\frac{E_0}{1-\nu^2}
\begin{bmatrix}
1&\nu&0\\
\nu&1&0\\
0&0&(1-\nu)/2
\end{bmatrix}.
}
\]

`COMMON_ORIGIN_PLANE_STRESS_TANGENT = PASS`。

## 8. exact uniaxial degeneration

### free uniaxial compression

取轴向压缩幅值 `e>0`：

\[
\varepsilon_1=\nu e,\qquad\varepsilon_2=-e.
\]

则严格有

\[
\lambda_1=0,\qquad\lambda_2=-e/\varepsilon_{c0}.
\]

因此

\[
\sigma_1=0,
\qquad
\sigma_2=-f_c C(e/\varepsilon_{c0}).
\]

Poisson expansion 不会被误当成真实 tensile damage。

### free uniaxial tension

\[
\varepsilon_1=e,\qquad\varepsilon_2=-\nu e
\]

严格给出

\[
\lambda_1=e/\varepsilon_{c0},\qquad\lambda_2=0,
\]

因此

\[
\sigma_1=f_tT_{NC}(e/\varepsilon_{cr}),\qquad\sigma_2=0.
\]

`UNIAXIAL_AXIS_DEGENERATION = PASS`。

该结论是在锁定 constant-nu plane-stress assumption 下的精确退化。

## 9. virtual-work conjugacy

定义 engineering strain/stress vectors：

\[
\boldsymbol e=[\varepsilon_x,\varepsilon_y,\gamma_{xy}]^T,
\qquad
\boldsymbol s=[\sigma_x,\sigma_y,\tau_{xy}]^T.
\]

物理虚功密度严格为

\[
\boxed{
\delta w_{int}=\boldsymbol s^T\delta\boldsymbol e
=\mathbf S:\delta\mathbf E.
}
\]

因为 stress tensor 与 physical strain tensor 共轴，任意虚应变下

\[
\mathbf S:\delta\mathbf E
=\sigma_1\delta\varepsilon_1+\sigma_2\delta\varepsilon_2.
\]

因此后续可以直接定义

\[
\delta W_{int}=\int_V\boldsymbol s^T\delta\boldsymbol e\,dV,
\]

以及 generalized residual

\[
R_a=\int_V \mathbf B_a^T\boldsymbol s\,dV-R_a^{ext}.
\]

`VIRTUAL_WORK_CONJUGACY = PASS`。

注意：NC-M6 的 branch tangent 一般不是 major-symmetric，因此不自动声明存在单一 hyperelastic potential。后续正式路线应使用 virtual-work residual + exact Jacobian，而不是未经证明地改写成 total potential minimization。这不是材料修复项，也不阻断虚功法。

## 10. full-domain stress boundedness

压缩 denominator

\[
q(c)=1+(\kappa-2)c+c^2
\]

对任意 `kappa>0`, `c>=0` 均严格正；且

\[
C'(c)=\frac{\kappa(1-c^2)}{q(c)^2}.
\]

所以

\[
0\le C(c)\le1,\qquad c\ge0.
\]

冻结 `T_NC` 有

\[
0\le\tau\le\tau_{max}=0.977862112142<1.
\]

因此 TC 中

\[
1-\tau\ge 0.022137887858>0.
\]

TT 中

\[
1-a_t\tau^8\ge 1-a_t\tau_{max}^8\approx0.930613>0.
\]

于是所有 sector 的 stress 在整个有限/无限 strain domain 内均有界：

- compression principal stress 始终位于 `[-fc,0]`；
- tensile principal stress 始终有限且不超过冻结 tensile target；
- interaction 不产生 pole 或无界应力。

`FULL_DOMAIN_STRESS_BOUNDEDNESS = PASS`。

## 11. full-domain tangent boundedness

- `C'` 无 pole 且趋于 0；
- `T_NC` 是冻结的 C2-regularized target，因此 `T_NC'` 全域有限；
- CC derivatives 是 `C'(u_i)` 乘有限阶多项式，所有无穷远方向均有有限极限；
- TC 因 `1-tau >= 0.022137887858`, 有 `u=c(1-tau)` 与 `c` 同阶，所以 `c C'(u)` 不会发散；
- TT 只含 bounded `tau`, `tau'` 和有限次幂；
- repeated-eigenvalue spectral shear tangent 取交换对称连续极限，因此不产生 `0/0` singularity。

sector front 上 normal tangent 可以有有限 jump，但两侧均有限。NC-M6 不把 finite-front C1 continuity 作为物理本构硬门槛。

因此

`WITHIN_SECTOR_TANGENT_BOUNDEDNESS = PASS`

`FULL_PHYSICAL_ONE_SIDED_TANGENT_BOUNDEDNESS = PASS`。

## 12. sector-front tangent governance

旧 NC-M5 审计已经证明冻结 sector physics 在有限 front 上存在 one-sided derivative mismatch，例如 CC-TC 和 TC-TT。

NC-M6 重新分类：

- stress continuity 是硬门槛；
- finite one-sided physical tangent boundedness 是硬门槛；
- finite-front `D-=D+` 不是虚功法的物理硬门槛。

因此不为此新增 C1/C2 material repair。以后若为 Newton 数值性能添加窄正则化，只能作为独立 solver regularization，不得改变 NC-M6 physical operator 身份。

## 13. ordered spectral chart note

因为

\[
\lambda_1-\lambda_2
=\frac{\varepsilon_1-\varepsilon_2}{(1+\nu)\varepsilon_{c0}},
\]

若实现中约定 `eps1>=eps2`，则必有 `lambda1>=lambda2`。因此 mixed-sign ordered chart 实际只访问 TC；CT 保留为 1<->2 交换完成式，以保证 permutation covariance，不删除其理论定义。

## 14. final gate table

- `NC_M6_ARCHITECTURE_CANDIDATE = LOCKED`
- `STRESS_CONTINUITY = PASS`
- `PHYSICAL_CONSISTENT_TANGENT = PASS`
- `COMMON_ORIGIN_PLANE_STRESS_TANGENT = PASS`
- `UNIAXIAL_AXIS_DEGENERATION = PASS`
- `VIRTUAL_WORK_CONJUGACY = PASS`
- `FULL_DOMAIN_STRESS_BOUNDEDNESS = PASS`
- `FULL_PHYSICAL_ONE_SIDED_TANGENT_BOUNDEDNESS = PASS`
- `HYPERELASTIC_POTENTIAL / MAJOR_SYMMETRY = NOT_ASSUMED / NOT_REQUIRED_FOR_VIRTUAL_WORK`
- `CASE21 = NOT_RUN`
- `T5 = NOT_REFIT`
- `NEW_MATERIAL_REPAIR_TERMS = NONE`

## 15. next allowed task

下一步只允许把 NC-M6 放入连续结构虚功架构，先建立材料层 generalized internal virtual work 与 exact Jacobian 的符号接口；不得先做 Case21，不得重开 T5，不得增加材料修复项。