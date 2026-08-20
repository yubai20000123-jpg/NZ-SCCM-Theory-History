# NZ-SCCM — NC-M4 参数化全局结果与数字出处

时间：2026-08-20 18:48 +08:00

状态：`ACTIVE_DERIVATION / PARAMETERIZED_OUTPUT / NUMERIC_PROVENANCE_AUDIT`

## 1. 参数化材料形状常数

为避免把项目候选系数误写成“文献常数”，将 NC-M4 写成

\[
C(c)=k_c\frac{c}{1+c^2},
\]

\[
T(t)=k_T\frac{t(t+a_T)}{1+b_Tt+c_Tt^2+d_Tt^3},
\]

\[
\beta(t)=\frac1{1+k_\beta t^2},
\]

\[
\eta(c_1,c_2)=1+k_\eta C(c_1)C(c_2).
\]

当前 NC-M4 文件采用

\[
k_c=2,\quad k_T=1.07515,\quad a_T=0.09,\quad b_T=-0.83,\quad c_T=1.04,\quad d_T=0.14,\quad k_\beta=0.15,\quad k_\eta=0.16.
\]

这些数字的身份必须区分：

- `k_c=2`：由所选单式 `k_c c/(1+c^2)` 的归一化 `C(1)=1` 得到，是解析归一化常数；该形状随后与当前 Saenz 峰前参考曲线作材料级审计。
- `a_T=0.09, b_T=-0.83, c_T=1.04, d_T=0.14`：2026-08-20 broad-peak single-form tension diagnostic 中为满足“峰值后移、宽峰、缓慢软化”而提出的项目候选形状系数，不是直接抄录自某篇文献的材料常数。
- `k_T=1.07515`：对上述 broad-peak 诊断式做峰值归一化后写入 NC-M4 的项目系数。由当前四个诊断系数精确数值求极值可得 `t_p≈1.5716247753`、未归一化峰值 `≈0.9300618037`，其倒数 `≈1.0751973644`；因此仓库中的 `1.07515` 是当前使用的舍入值，不应称为精确文献常数。
- `k_beta=0.15`：NC-M2 中为一个单一光滑 TC/CT 压缩削弱候选而引入；材料级审计给出与旧 Nguyen 型参考曲线在 `0<=t<=3` 的面积比约 `0.94525`。它是项目候选参数，不是 Nguyen 原文常数。
- `k_eta=0.16`：NC-M2 中为对称 CC 双压增强候选而引入，使 `eta(1,1)=1.16`；沿 `c1=1,c2=rho` 的材料级审计与 Foster/Kupfer 参考增强曲线面积比约 `0.92192`。它是项目候选参数，不是 Foster/Kupfer 原文常数。

## 2. 参数化统一后端算子

形式材料关系仍按九宫格解释；以下只作为精确积分后端等价表示。

\[
E=\begin{bmatrix}\varepsilon_x&\gamma_{xy}/2\\\gamma_{xy}/2&\varepsilon_y\end{bmatrix},
\quad R=(E^2)^{1/2},
\]

\[
E_+=(R+E)/2,\qquad E_c=(R-E)/2,
\]

\[
T=E_+/\varepsilon_{t0},\qquad C=E_c/\varepsilon_{c0}.
\]

\[
\mathcal T(T)=k_T T(T+a_T I)[I+b_TT+c_TT^2+d_TT^3]^{-1},
\]

\[
\mathcal C(C)=k_c C(I+C^2)^{-1},
\]

\[
\alpha=\frac1{1+k_\beta(\operatorname{tr}T)^2}+k_\eta\det\mathcal C(C),
\]

\[
\Sigma=f_t\mathcal T(T)-f_c\alpha\mathcal C(C).
\]

## 3. 全局无空间积分符号结果

令 `A*_{M4,global}` 为当前 48 条稀疏 circuit relations 按 Cayley construction 唯一生成的 `99 x 155` 配置；物理 branch 为完整单半波。则

\[
R_m=\frac{2b\ell h}{\pi^2}\,\mathrm{RGKZ}_{A^*_{M4,global}}(\beta_m;\mathbf c\mid\Gamma_{phys}),
\]

\[
P=-\frac{2bh}{\pi^2}\,\mathrm{RGKZ}_{A^*_{M4,global}}(\beta_P;\mathbf c\mid\Gamma_{phys}),
\]

\[
R_A=\frac{2b\ell h}{\pi^2}\,\mathrm{RGKZ}_{A^*_{M4,global}}(\beta_A;\mathbf c\mid\Gamma_{phys}).
\]

`c` 中的所有数值材料形状常数应优先按本文件第一节的参数符号保留，只有在采用当前 NC-M4 候选时才代入上述数值。

## 4. 数字类别

- `pi`, `1/2`, `2`, `4`, `256`, `512` 等：坐标变换、CH pair、residue Jacobian 的解析常数，不是材料试验参数。
- `99 x 155`, `48`, `51`, `5`：当前 symbolic compiler/circuit audit 的机器输出，不是物理参数。
- `fc, ft, eps_c0, eps_t0, b, ell, h, A0`：必须保持为问题输入参数，除非具体算例明确给值。
- `Delta, A, eps_m`：结构未知量，绝不预先数值化。

## 5. 治理说明

NC-M4 仍是 `ACTIVE_MATERIAL_CANDIDATE / NOT_YET_PRODUCTION_LOCK`。因此任何项目候选材料形状数字不得包装成“文献给定常数”。