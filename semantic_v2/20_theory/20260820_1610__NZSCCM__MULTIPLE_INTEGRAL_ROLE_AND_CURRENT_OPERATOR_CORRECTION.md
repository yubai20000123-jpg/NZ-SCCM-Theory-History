# NZ-SCCM — 多重积分角色与 current operator 定位修正

时间：2026-08-20 16:10 +08:00

## 1. 核心修正

前一轮把 I1(z)、I2(z) 作为新的正式中间层，并继续据此展开状态根与厚度原函数，偏离了当前主线。I1/I2 只可作为可选代数压缩工具，不应成为正式理论新增层。

正式链条应回到：

\[
(\Delta,A,\varepsilon_m)
\to
(\varepsilon_x,\varepsilon_y,\gamma_{xy})(x,y,z)
\to
\mathcal M_{NC}(\varepsilon_x,\varepsilon_y,\gamma_{xy})
\to
(\sigma_x,\sigma_y,\tau_{xy})
\to
R_A,R_m,P.
\]

## 2. 多重积分真正解决的问题

引入连续多重积分，解决的是“同一块连续板内，不同空间位置可以处于不同材料状态”这一结构积分问题。

它禁止错误的：

\[
CC_{full}+TC_{full}+TT_{full}
\]

全域延拓响应叠加。

正确形式是：每个空间点只评价一次唯一材料响应：

\[
\boldsymbol\sigma(x,y,z)=\mathcal M_{NC}(\boldsymbol\varepsilon(x,y,z)).
\]

然后直接积分：

\[
R_p=\iiint_V \boldsymbol\sigma(\boldsymbol\varepsilon):\boldsymbol\varepsilon_{,p}\,dV.
\]

因此，多重积分负责“空间共存”，不负责“替材料理论决定局部关系”。

## 3. “唯一 current operator”不等于“一个全局无分支公式”

一个数学上唯一的 current operator 完全可以是 piecewise / 九宫格定义：

\[
\mathcal M_{NC}(\varepsilon)=
\begin{cases}
\mathcal M_{CC}, & \varepsilon_1<0,\varepsilon_2<0,\\
\mathcal M_{TC}, & \varepsilon_1>0,\varepsilon_2<0,\\
\mathcal M_{CT}, & \varepsilon_1<0,\varepsilon_2>0,\\
\mathcal M_{TT}, & \varepsilon_1>0,\varepsilon_2>0.
\end{cases}
\]

只要任意当前应变状态只返回一组唯一应力，它就是单值 current operator。

所以当前不需要再追求一个跨 CC/TC/CT/TT 的“全局大多项式”或“全局无分支单式”。

## 4. 当前真正剩余的材料问题

NC-M4 已经在形式上提供了一个单值九宫格 current operator 候选，因此“唯一 M 是否存在”不再是结构层阻塞项。

真正未冻结的是：

1. 各实体区公式是否物理合理；
2. 拉伸 T4 是否合理；
3. TC/CT 的 beta(t) 是否合理；
4. CC 的 eta(c1,c2) 是否合理；
5. 这些简式相对原始/文献趋势的误差是否可接受；
6. 在保持物理合理的同时，直接代入 Nguyen 二阶运动学后是否仍可完成零数值积分解析闭合。

因此当前“材料函数仍是核心”是正确的，但不是因为多重积分失效，而是因为多重积分只能正确汇总局部材料响应，不能替代局部材料关系本身。

## 5. 直接代入形式

正式下一步不新增 I1/I2 层，直接使用：

\[
\varepsilon_x=\varepsilon_m+S\phi_{,x}^2-zA\phi_{,xx},
\]

\[
\varepsilon_y=-\frac{\Delta}{\ell}+S\phi_{,y}^2-zA\phi_{,yy},
\]

\[
\gamma_{xy}=2S\phi_{,x}\phi_{,y}-2zA\phi_{,xy},
\]

并写：

\[
\boldsymbol\sigma=\mathcal M_{NC-M4}(\varepsilon_x,\varepsilon_y,\gamma_{xy}).
\]

随后：

\[
R_m=\iiint_V \sigma_x\,dV,
\qquad
P=-\frac1\ell\iiint_V\sigma_y\,dV,
\]

\[
R_A=\iiint_V
\left(
\sigma_x\varepsilon_{x,A}
+\sigma_y\varepsilon_{y,A}
+\tau_{xy}\gamma_{xy,A}
\right)dV.
\]

## 6. 当前治理结论

- `MULTIPLE_INTEGRAL_ROLE = SPATIAL_STATE_COEXISTENCE_AND_GLOBAL_ASSEMBLY`
- `MULTIPLE_INTEGRAL_DOES_NOT_DEFINE_LOCAL_CONSTITUTIVE_LAW = TRUE`
- `UNIQUE_CURRENT_OPERATOR_MAY_BE_PIECEWISE = TRUE`
- `GLOBAL_BRANCHLESS_POLYNOMIAL_REQUIRED = FALSE`
- `I1_I2_FORMAL_LAYER = WITHDRAWN_AS_REQUIRED_LAYER`
- `CURRENT_CORE_OPEN_ITEM = PHYSICAL_ACCEPTANCE_AND_ANALYTIC_MANAGEABILITY_OF_NC_M4_BRANCH_LAWS`
