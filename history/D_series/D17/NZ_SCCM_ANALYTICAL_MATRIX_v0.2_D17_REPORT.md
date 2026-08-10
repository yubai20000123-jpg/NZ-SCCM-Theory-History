# D17：精确厚度状态前沿与解析矩透明化报告

> Archive identity: complete text recovered from File Library `file_000000007d1081fd84f4ce14c9de8db8`. Historical D17 artifact. Deliverable ZIP hash source: `file_00000000da9881f8ae446cc5d6f9c53d`, ZIP SHA-256 `0e0226f8b7cadc0117dc8ea13b023d001c60bcaf533981f0a568fe38abbc2e71`.

## 1. 阶段目标

本阶段先解决两个基础问题：

1. 用完全展开的例子证明矩阵系数来自理论积分，而不是拟合；
2. 消除厚度方向材料点离散，用解析方程直接求开裂或压碎前沿。

## 2. 透明系数例子

本阶段对

\[
U_y=\frac12E\int_\Omega\varepsilon_y^2dV
\]

完成符号积分。完整展开系数见：

`results/D17_ELASTIC_EPSY2_EXACT_COEFFICIENTS.csv`

精确积分恒等式见：

`results/D17_TRANSPARENT_MOMENT_TABLE.csv`

## 3. 厚度状态前沿

固定 \(X,Y\) 后：

\[
\mathbf E(z)=
\begin{bmatrix}
a_x+b_xz & (a_\gamma+b_\gamma z)/2\\
(a_\gamma+b_\gamma z)/2 & a_y+b_yz
\end{bmatrix}.
\]

任意主应变阈值 \(\lambda_*\) 满足：

\[
\det[\mathbf E(z)-\lambda_*\mathbf I]=0.
\]

展开得到：

\[
c_2=b_xb_y-\frac14b_\gamma^2,
\]

\[
c_1=(a_x-\lambda_*)b_y+(a_y-\lambda_*)b_x
-\frac12a_\gamma b_\gamma,
\]

\[
c_0=(a_x-\lambda_*)(a_y-\lambda_*)
-\frac14a_\gamma^2.
\]

所以厚度边界由：

\[
c_2z^2+c_1z+c_0=0
\]

直接确定。

## 4. 实现与测试

建立：

`src/exact_thickness_state_front.py`

测试结果：

```text
D17 exact thickness-front tests: PASS (755 random roots + fixtures)
```

## 5. Case 21形式演示

使用D13 Case 21极限点的 \((\delta,A)\) 作为纯运动学演示，在板中心、四分点和靠边位置对以下阈值分区：

- 单轴压缩峰值应变；
- 零应变；
- \(f_t/E_c\)拉裂应变。

结果见：

`results/D17_CASE21_THICKNESS_PARTITION_DEMO.csv`

该演示不是新的Case 21承载力结果，只证明厚度方向不需要材料积分点。

## 6. 本阶段门禁

```text
D17_TRANSPARENT_MATRIX_COEFFICIENT_DERIVATION = PASS
D17_EXACT_TRIGONOMETRIC_MOMENTS              = PASS
D17_EXACT_THICKNESS_MOMENTS                  = PASS
D17_EXACT_THICKNESS_STATE_FRONT              = PASS
D17_RANDOM_ROOT_TESTS                        = PASS

D17_IN_PLANE_MOVING_STATE_DOMAIN             = OPEN
D17_UHPC_TC_COMPLETE_FORMULA                  = OPEN
D17_UHPC_TT_COMPLETE_FORMULA                  = OPEN
D17_UHPC_TCX_CLOSURE                          = OPEN
D17_FULL_PANEL_PRODUCTION                     = NOT AUTHORIZED
```

## 7. 下一阶段

下一阶段同时推进：

1. 将面内阈值方程变换为 \(u=\sin^2X,v=\sin^2Y\) 下的代数曲线；
2. 研究不完全Beta函数或有限代数矩能否积分移动状态区；
3. 继续获取Liu 2023完整TC公式和Looney多轴拉伸系数。

如果来源全文仍无法取得，不得虚构公式。
