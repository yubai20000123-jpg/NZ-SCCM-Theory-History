# NZ-SCCM — NC-M4 全局积分稀疏电路与支撑审计

时间：2026-08-20 17:30 +08:00

状态：`EXECUTION_AUDIT / GLOBAL_Rm_P_RA / EXACT_SUPPORT_COUNT`

## 1. 执行对象

只审计冻结 NC-M4 + 一般矩形 Nguyen 二阶运动学下三个完整目标：

\[
R_m=\iiint\sigma_x\,dV,
\qquad
P=-\frac1\ell\iiint\sigma_y\,dV,
\qquad
R_A=\iiint(\sigma_xG_x+\sigma_yG_y+\tau_{xy}G_\gamma)\,dV.
\]

TC/CT 不作为单独研究问题重新打开。

## 2. 代数恒等核验

使用精确符号代数检查以下 NC-M4 半角/谱有理式与原材料式恒等：

- `T_sigma(L/(2D))` 与 NC-M4 `f_t T4(t)`：difference = 0。
- `C_sigma(L/(2D))` 与 NC-M4 `-f_c C(c)`：difference = 0。
- `B(L/(2D))` 与 `beta(t)`：difference = 0。
- `eta(L+,L-)` 与 `1+0.16 C(c+) C(c-)`：difference = 0。
- 板坐标谱重构：
  - `2 W sigma_x = W Sigma + Ed Delta_sigma`
  - `2 W sigma_y = W Sigma - Ed Delta_sigma`
  - `2 W tau_xy = Eg Delta_sigma`

## 3. 稀疏多项式电路实际统计

变量数：32。

电路关系数：29。

关系 monomial-support 审计结果：

```text
total Cayley support columns = 84
maximum monomials in any relation = 5
Cayley row dimension = variables + relations = 61
A_star_M4 size = 61 x 84
```

旧 R12 finite-R10 pilot 是 `159 x 271`；当前 NC-M4 对应支撑显著更小。

## 4. 三个目标 numerator support

每个谱状态 branch（TT/M/CC）分别取：

\[
N_m=W(s_++s_-)+E_d(s_+-s_-),
\]

\[
N_P=W(s_++s_-)-E_d(s_+-s_-),
\]

\[
N_A=W(s_++s_-)(\mathcal G_x+\mathcal G_y)
+(s_+-s_-)[E_d(\mathcal G_x-\mathcal G_y)+E_\gamma\mathcal G_\gamma].
\]

实际合并同指数 monomial 后：

```text
N_m support = 4
N_P support = 4
N_A support = 16
```

因此三个全局量只改变 numerator insertion，不改变 master denominator/circuit support。

## 5. 全局 exact period

正根支 relation：

\[
G_W=W^2-E_d^2-E_\gamma^2.
\]

正支 residue lift：

\[
H(W_+)=\frac1{2\pi i}\oint_{\gamma_+}H(W)\frac{2W}{G_W}\,dW.
\]

于是完整半波三个目标均为同一个 finite rational relative-period family 的有限 numerator shifts。

结论：

```text
NC_M4_GLOBAL_Rm_RATIONAL_PERIOD = PASS
NC_M4_GLOBAL_P_RATIONAL_PERIOD  = PASS
NC_M4_GLOBAL_RA_RATIONAL_PERIOD = PASS
NC_M4_SHARED_MASTER_SUPPORT     = PASS
A_STAR_M4_SIZE                  = 61 x 84
FORMAL_SPATIAL_QUADRATURE       = 0
MATERIAL_POINT_GRID             = 0
TC_REOPENED_AS_THEORY_PROBLEM   = NO
```

## 6. 边界

本审计证明并构造的是完整参数化的 exact rational-period / relative-incomplete-GKZ 表示。它没有证明一般参数下可进一步化成单个 elementary/Appell/Lauricella 短公式；不得把“没有更短 named-function 降阶”误写成“积分未解析”。
