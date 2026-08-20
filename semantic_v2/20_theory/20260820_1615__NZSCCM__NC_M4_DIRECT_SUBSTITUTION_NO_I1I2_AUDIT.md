# NZ-SCCM — NC-M4 直接代入 Nguyen 二阶运动学审计（不引入 I1/I2 中间理论层）

时间：2026-08-20 16:15 +08:00

状态：`ACTIVE_MATERIAL_CANDIDATE / DIRECT_SUBSTITUTION_AUDIT`

## 1. 本轮修正

正式主线不再先构造 `I1(z)`、`I2(z)` 再做厚度根分析。直接使用 Nguyen 二阶连续应变场：

\[
\varepsilon_x=\varepsilon_m+S\phi_{,x}^2-zA\phi_{,xx},
\]
\[
\varepsilon_y=-\frac{\Delta}{\ell}+S\phi_{,y}^2-zA\phi_{,yy},
\]
\[
\gamma_{xy}=2S\phi_{,x}\phi_{,y}-2zA\phi_{,xy},
\]
其中
\[
\phi=\sin\frac{\pi x}{b}\sin\frac{\pi y}{\ell},\qquad S=A_0A+\frac12A^2.
\]

直接接材料 current operator：
\[
\boldsymbol\sigma=\mathcal M_{NC-M4}(\varepsilon_x,\varepsilon_y,\gamma_{xy}).
\]

## 2. 一个关键代数事实

主应变根号并不是由 `I1/I2` 产生；如果材料函数仍按主应变状态定义，直接求主应变同样会出现
\[
d=\sqrt{(\varepsilon_x-\varepsilon_y)^2+\gamma_{xy}^2}.
\]

因此删除 `I1/I2` 只能删除多余中间层，不能自动消掉主应变谱分解本身的根号。

但是，对 CC 和 TT，因为两个主方向调用的是同一个标量函数，可以把谱函数直接写成 2×2 矩阵有理函数，从而完全避免显式主应变根号；真正保留根号问题的是 TC/CT 混合拉压区，因为正、负主方向调用的是不同函数。

## 3. CC 直接矩阵函数

令
\[
\mathbf E=\begin{bmatrix}\varepsilon_x&\gamma_{xy}/2\\\gamma_{xy}/2&\varepsilon_y\end{bmatrix},
\qquad \mathbf X=-\mathbf E/\varepsilon_{c0}.
\]

单轴压缩函数 `C(c)=2c/(1+c^2)` 直接提升为矩阵函数：
\[
\boxed{\mathbf C=2\mathbf X(\mathbf I+\mathbf X^2)^{-1}}.
\]

它的两个特征值正好是 `C(c1), C(c2)`，不需要显式求 `c1,c2`。

双压增强：
\[
\boxed{\eta=1+0.16\det\mathbf C}.
\]

于是 CC 直接 current operator：
\[
\boxed{\boldsymbol\sigma^{CC}=-f_c\eta\mathbf C}.
\]

这对 `εx,εy,γxy` 是纯有理 2×2 矩阵函数，没有主应变根号。

## 4. TT 直接矩阵函数

令
\[
\mathbf T=\mathbf E/\varepsilon_{t0}.
\]

NC-M4 拉伸函数
\[
T_4(t)=1.07515\frac{t(t+0.09)}{1-0.83t+1.04t^2+0.14t^3}
\]
直接提升为
\[
\boxed{
\boldsymbol\sigma^{TT}=f_t\,1.07515\,\mathbf T(\mathbf T+0.09\mathbf I)
\left(\mathbf I-0.83\mathbf T+1.04\mathbf T^2+0.14\mathbf T^3\right)^{-1}.
}
\]

同样是 `εx,εy,γxy` 的纯有理 2×2 矩阵函数，没有显式主应变根号。

## 5. TC/CT 是当前真正的代数阻塞项

混合拉压状态必须让一个主方向使用
\[
\sigma_t=f_tT_4(t),
\]
另一个主方向使用
\[
\sigma_c=-f_c\beta(t)C(c).
\]

这不是对两个特征值施加同一个标量函数，因此无法像 CC/TT 那样简单写成同一个矩阵有理函数 `f(E)`。

若直接做主应变分解，则
\[
\varepsilon_{\pm}=\frac{\varepsilon_x+\varepsilon_y\pm\sqrt{(\varepsilon_x-\varepsilon_y)^2+\gamma_{xy}^2}}{2}.
\]

所以根号来自 **TC/CT 材料定义对正、负主方向采用不同公式**，而不是来自 `I1/I2` 中间变量。

## 6. 直接代入结构广义内力

保持
\[
\varepsilon_{x,A}=(A_0+A)\phi_{,x}^2-z\phi_{,xx},
\]
\[
\varepsilon_{y,A}=(A_0+A)\phi_{,y}^2-z\phi_{,yy},
\]
\[
\gamma_{xy,A}=2(A_0+A)\phi_{,x}\phi_{,y}-2z\phi_{,xy}.
\]

材料算子返回唯一
\[
\boldsymbol\sigma=\begin{bmatrix}\sigma_x&\tau_{xy}\\\tau_{xy}&\sigma_y\end{bmatrix}.
\]

直接积分：
\[
R_m=\iiint_V\sigma_x\,dV,
\]
\[
P=-\frac1\ell\iiint_V\sigma_y\,dV,
\]
\[
R_A=\iiint_V\left(\sigma_x\varepsilon_{x,A}+\sigma_y\varepsilon_{y,A}+\tau_{xy}\gamma_{xy,A}\right)dV.
\]

## 7. 当前定位

- `I1/I2` 不再作为正式理论层；
- CC 可直接写成纯有理矩阵 current operator；
- TT 可直接写成纯有理矩阵 current operator；
- 当前唯一真正保留主应变根号的材料区是 TC/CT；
- 因此下一步材料重构重点应进一步收缩到：**能否为 TC/CT 构造一个直接作用于 2×2 当前应变张量的短显式单式，同时保持“拉应变削弱压缩”的物理趋势。**

这一步不是为了积分强行改坏材料，而是为了确认 NC-M4 当前复杂性的真实来源。
