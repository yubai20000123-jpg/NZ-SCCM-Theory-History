# NZ-SCCM — NC-M4 的 R_m / P 符号闭合执行报告

时间：2026-08-20 15:41 +08:00

## 1. 执行对象

本轮执行的是：

\[
R_m=\iiint_V\sigma_x\,dV,
\qquad
P=-\frac1\ell\iiint_V\sigma_y\,dV
\]

的解析闭合审计，不执行 Case21。

## 2. 实际完成项

### A. 不变量状态判别

建立：

\[
J_1=\varepsilon_x+\varepsilon_y,
\qquad
J_2=\varepsilon_x\varepsilon_y-\gamma_{xy}^2/4.
\]

得到：

- TT: `J2>0,J1>0`
- CC: `J2>0,J1<0`
- TC/CT: `J2<0`

状态边界为 `J2=0`。

### B. 厚度代数结构

将

\[
\varepsilon_x=X_0+zX_1,
\quad
\varepsilon_y=Y_0+zY_1,
\quad
\gamma=G_0+zG_1
\]

代入后得到：

\[
J_1=p_0+p_1z,
\qquad
J_2=q_0+q_1z+q_2z^2.
\]

因此材料状态前沿沿厚度最多有两个精确代数根。

### C. TT / CC 不变量矩阵算子

已将 TT 和 CC 从“求主应变 + 求角度 + 旋转回去”改写为：

\[
\boldsymbol\sigma=A(J_1,J_2)\mathbf I+B(J_1,J_2)\mathbf E.
\]

直接数值对照特征分解：随机测试最大绝对误差为约 `1e-15`。

### D. 被积式次数

固定 `(x,y)` 后：

- TT: `sigma_x,y = P5(z)/Q6(z)`；
- CC: `sigma_x,y = P7(z)/Q8(z)`；
- TC/CT: `sigma_x,y ∈ R(z,sqrt(Q2(z)))`。

### E. Wolfram 精确积分试验

用非退化精确有理代表参数进行实际符号积分：

- TT：精确返回 `RootSum + Log` 原函数；`LeafCount≈149`；
- CC：精确返回有理项 + `RootSum + Log` 原函数；`LeafCount≈145`；
- TC/CT：精确返回包含 `ArcSin / ArcTan / Log / RootSum / sqrt(quadratic)` 的原函数；`LeafCount≈115489`。

故厚度方向不是“积分不出来”，而是混合状态完全展开后表达式爆炸。

### F. SymPy 负面诊断

对全符号 TT `P5/Q6` 直接使用 `ratint`，60 s 内未完成。

这进一步确认：

`naive expand-then-integrate = NOT SUITABLE`。

## 3. 本轮形成的厚度凝聚场

定义：

\[
N_x(x,y)=\int_{-h/2}^{h/2}\sigma_x dz,
\]

\[
N_y(x,y)=\int_{-h/2}^{h/2}\sigma_y dz.
\]

于是：

\[
R_m=\int_0^b\int_0^\ell N_x\,dy\,dx,
\]

\[
P=-\frac1\ell\int_0^b\int_0^\ell N_y\,dy\,dx.
\]

三重积分已经解析地压缩为二维连续积分，仍保持正式空间数值积分为零。

## 4. 当前结论

`THICKNESS_ANALYTIC_CLOSURE = PASS`

`GENERAL_RECTANGLE_OUTER_2D_SHORT_CLOSED_FORM = NOT_YET_PASS`

真正剩余难点已定位为：

1. `(x,y)` 相关的 `J2=0` 材料状态前沿；
2. 混合状态厚度原函数的表达式管理；
3. 外层二维积分中代数根 + log / atan 类对象的解析处理。

下一步必须继续外层二维解析编译，不回退 Gauss / Simpson / material-point grid，也不把 NC-M4 再为了积分方便强行改成多项式。
