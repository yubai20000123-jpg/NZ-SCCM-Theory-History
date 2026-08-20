# NZ-SCCM — NC-M4 的 R_m / P 解析闭合审计

时间：2026-08-20 15:41 +08:00

状态：`ACTIVE_MATERIAL_CANDIDATE / ANALYTIC_CLOSURE_AUDIT`

## 1. 本轮目标

承接 `20260820_1533__NZSCCM__NC_M4_FORMAL_MATERIAL_AND_CONTINUOUS_INTERNAL_WORK_FIELD.md`，本轮不做 Case21，不做空间数值积分，直接检查

\[
R_m=\iiint_V \sigma_x\,dV,
\qquad
P=-\frac1\ell\iiint_V\sigma_y\,dV
\]

在 NC-M4 下能否进一步解析闭合。

固定：

- `ONE_CONTINUOUS_COMPLETE_HALFWAVE`
- `b` 与 `ell` 独立；
- `N_formal_spatial_sampling = 0`
- `N_formal_spatial_quadrature = 0`
- 不使用 Gauss / Simpson / Chebyshev collocation / material-point grid。

## 2. 板面应变张量与两个不变量

采用工程剪应变 `gamma_xy` 时，二维小应变张量写为

\[
\mathbf E=
\begin{bmatrix}
\varepsilon_x & \gamma_{xy}/2\\
\gamma_{xy}/2 & \varepsilon_y
\end{bmatrix}.
\]

定义

\[
J_1=\operatorname{tr}\mathbf E=\varepsilon_x+\varepsilon_y,
\]

\[
J_2=\det\mathbf E
=\varepsilon_x\varepsilon_y-\frac{\gamma_{xy}^2}{4}.
\]

主应变为

\[
\lambda_{\pm}
=\frac{J_1\pm r}{2},
\qquad
r=\sqrt{J_1^2-4J_2}
=\sqrt{(\varepsilon_x-\varepsilon_y)^2+\gamma_{xy}^2}.
\]

材料状态可用不变量直接识别：

- `TT`: `J2>0` 且 `J1>0`；
- `CC`: `J2>0` 且 `J1<0`；
- `TC/CT mixed`: `J2<0`；
- `J2=0` 为单轴/零主应变边界。

这不是新的材料模型，只是九宫格状态在积分层的等价不变量判别。TC 与 CT 在九宫格中仍保留两个标签；在无序谱表示里它们是同一个“一正一负”物理状态的 1↔2 交换。

## 3. 通过厚度后 J1 为一次式、J2 为二次式

记

\[
\alpha=\frac{\pi x}{b},\qquad
\beta=\frac{\pi y}{\ell},
\qquad
k_x=\frac{\pi}{b},\qquad
k_y=\frac{\pi}{\ell},
\]

\[
\phi=\sin\alpha\sin\beta,
\qquad
S=A_0A+\frac12A^2.
\]

将应变写为

\[
\varepsilon_x=X_0+zX_1,
\qquad
\varepsilon_y=Y_0+zY_1,
\qquad
\gamma_{xy}=G_0+zG_1,
\]

其中

\[
X_0=\varepsilon_m
+S k_x^2\cos^2\alpha\sin^2\beta,
\]

\[
X_1=A k_x^2\phi,
\]

\[
Y_0=-\frac{\Delta}{\ell}
+S k_y^2\sin^2\alpha\cos^2\beta,
\]

\[
Y_1=A k_y^2\phi,
\]

\[
G_0=2S k_xk_y
\cos\alpha\sin\alpha\sin\beta\cos\beta,
\]

\[
G_1=-2A k_xk_y\cos\alpha\cos\beta.
\]

于是

\[
J_1=p_0+p_1z,
\]

\[
J_2=q_0+q_1z+q_2z^2,
\]

其中

\[
p_0=X_0+Y_0,\qquad p_1=X_1+Y_1,
\]

\[
q_0=X_0Y_0-\frac{G_0^2}{4},
\]

\[
q_1=X_0Y_1+X_1Y_0-\frac{G_0G_1}{2},
\]

\[
q_2=X_1Y_1-\frac{G_1^2}{4}.
\]

特别地

\[
q_2
=A^2k_x^2k_y^2
\left(\sin^2\alpha+\sin^2\beta-1\right).
\]

因此状态前沿 `J2=0` 对固定 `(x,y)` 最多给出两个精确厚度根：

\[
z_{\pm}
=\frac{-q_1\pm\sqrt{q_1^2-4q_2q_0}}{2q_2}
\]

（`q2=0` 时退化为一次根）。这些是物理材料状态前沿，不是数值空间 cell。

同时

\[
r^2=J_1^2-4J_2
=r_0+r_1z+r_2z^2,
\]

仍然只是 `z` 的二次式。

## 4. CC：无需显式求主方向，得到纯有理矩阵算子

在 CC 中定义压缩归一化张量

\[
\mathbf C_\varepsilon=-\frac{\mathbf E}{\varepsilon_{c0}},
\]

其两个特征值为 `c1,c2>0`。定义

\[
s_c=c_1+c_2=-\frac{J_1}{\varepsilon_{c0}},
\qquad
p_c=c_1c_2=\frac{J_2}{\varepsilon_{c0}^2},
\]

\[
D_c=(1+c_1^2)(1+c_2^2)
=1+s_c^2-2p_c+p_c^2.
\]

对

\[
C(c)=\frac{2c}{1+c^2}
\]

作二维谱函数约化，可严格写为

\[
C(\mathbf C_\varepsilon)
=A_c\mathbf I+B_c\mathbf C_\varepsilon,
\]

其中

\[
A_c=\frac{2p_cs_c}{D_c},
\qquad
B_c=\frac{2(1-p_c)}{D_c}.
\]

CC 双压增强为

\[
\eta
=1+0.16C(c_1)C(c_2)
=1+\frac{0.64p_c}{D_c}.
\]

所以

\[
\boxed{
\boldsymbol\sigma^{CC}
=-f_c\eta
\left(A_c\mathbf I+B_c\mathbf C_\varepsilon\right)
}
\]

是 `J1,J2,E` 的纯有理函数，不需要 `sqrt(J1^2-4J2)`。

故

\[
\sigma_x^{CC}
=-f_c\eta\left(A_c-B_c\frac{\varepsilon_x}{\varepsilon_{c0}}\right),
\]

\[
\sigma_y^{CC}
=-f_c\eta\left(A_c-B_c\frac{\varepsilon_y}{\varepsilon_{c0}}\right).
\]

由于 `J1` 对 `z` 一次、`J2` 对 `z` 二次，固定 `(x,y)` 后两者都是 `z` 的有理函数。实际代数度审计得到：

\[
\sigma_x^{CC},\sigma_y^{CC}
=\frac{P_7(z)}{Q_8(z)}
\]

（约分后最高次数为分子 7、分母 8；具体某点可进一步降阶）。

## 5. TT：同样得到纯有理矩阵算子

定义拉伸归一化张量

\[
\mathbf T_\varepsilon=\frac{\mathbf E}{\varepsilon_{t0}},
\]

其特征值为 `t1,t2>0`，并定义

\[
s_t=t_1+t_2=\frac{J_1}{\varepsilon_{t0}},
\qquad
p_t=t_1t_2=\frac{J_2}{\varepsilon_{t0}^2}.
\]

NC-M4 拉伸标量函数

\[
T_4(t)
=K\frac{t(t+a)}{d(t)},
\]

其中

\[
K=1.07515,\qquad a=0.09,
\]

\[
d(t)=1-0.83t+1.04t^2+0.14t^3.
\]

二维谱函数同样可以写为

\[
T_4(\mathbf T_\varepsilon)
=A_t\mathbf I+B_t\mathbf T_\varepsilon,
\]

其中 `A_t,B_t` 都是 `(s_t,p_t)` 的有理函数。令

\[
D_t=d(t_1)d(t_2),
\]

则一组紧凑的完全对称形式为

\[
B_t=
\frac{K\left[
 a+s_t+(-0.83-1.04a)p_t
-0.14a s_tp_t
-0.14p_t^2
\right]}{D_t},
\]

\[
A_t=
\frac{Kp_t\left[
-0.83a+1.04a s_t
+0.14a(s_t^2-p_t)
-1+1.04p_t+0.14s_tp_t
\right]}{D_t}.
\]

而

\[
D_t
=1-0.83s_t+1.04(s_t^2-2p_t)
+0.14(s_t^3-3s_tp_t)
+0.83^2p_t
-0.83\cdot1.04\,s_tp_t
-0.83\cdot0.14\,p_t(s_t^2-2p_t)
+1.04^2p_t^2
+1.04\cdot0.14\,s_tp_t^2
+0.14^2p_t^3.
\]

所以

\[
\boxed{
\boldsymbol\sigma^{TT}
=f_t\left(A_t\mathbf I+B_t\mathbf T_\varepsilon\right)
}
\]

从而

\[
\sigma_x^{TT}=f_t\left(A_t+B_t\frac{\varepsilon_x}{\varepsilon_{t0}}\right),
\]

\[
\sigma_y^{TT}=f_t\left(A_t+B_t\frac{\varepsilon_y}{\varepsilon_{t0}}\right).
\]

固定 `(x,y)` 后仍为 `z` 的纯有理函数；代数度审计得到

\[
\sigma_x^{TT},\sigma_y^{TT}
=\frac{P_5(z)}{Q_6(z)}.
\]

## 6. TC/CT：只剩一个二次根式，不再需要显式旋转角

在 `J2<0` 的混合状态，定义

\[
r=\sqrt{J_1^2-4J_2},
\]

\[
\lambda_t=\frac{J_1+r}{2}>0,
\qquad
\lambda_c=\frac{J_1-r}{2}<0.
\]

定义

\[
t=\frac{\lambda_t}{\varepsilon_{t0}},
\qquad
c=-\frac{\lambda_c}{\varepsilon_{c0}},
\]

\[
\sigma_t=f_tT_4(t),
\qquad
\sigma_c=-f_c\beta(t)C(c).
\]

拉向谱投影算子可写为

\[
\mathbf P_t
=\frac{\mathbf E-\lambda_c\mathbf I}{r}.
\]

因此混合状态应力无需显式 `theta`：

\[
\boxed{
\boldsymbol\sigma^{M}
=\sigma_c\mathbf I
+(\sigma_t-\sigma_c)\mathbf P_t
}
\]

即

\[
\sigma_x^M
=\sigma_c
+(\sigma_t-\sigma_c)
\frac{\varepsilon_x-\lambda_c}{r},
\]

\[
\sigma_y^M
=\sigma_c
+(\sigma_t-\sigma_c)
\frac{\varepsilon_y-\lambda_c}{r}.
\]

由于固定 `(x,y)` 后

\[
r=\sqrt{r_0+r_1z+r_2z^2},
\]

所以 `sigma_x^M, sigma_y^M` 属于

\[
\mathbb R(z,\sqrt{Q_2(z)})
\]

这一二次代数函数域。通过 Euler 代换可精确化为有理积分，因此厚度原函数属于代数项 + `log/atan/atanh/asin` 等初等函数组合；不需要厚度 Gauss 积分。

## 7. 厚度凝聚后的二维广义内力场

定义

\[
N_x(x,y)=\int_{-h/2}^{h/2}\sigma_x(x,y,z)\,dz,
\]

\[
N_y(x,y)=\int_{-h/2}^{h/2}\sigma_y(x,y,z)\,dz.
\]

材料状态变化时，积分按 `J2=0` 的精确物理状态根评价各实体区原函数；这不是人为网格或数值 subcell。

于是

\[
\boxed{
R_m=\int_0^b\int_0^{\ell}N_x(x,y)\,dy\,dx
}
\]

\[
\boxed{
P=-\frac1\ell
\int_0^b\int_0^{\ell}N_y(x,y)\,dy\,dx
}
\]

本轮已经把三重积分的厚度方向解析地降为二维连续积分。

## 8. 一般矩形板的切半角变换

令

\[
u=\tan\frac{\alpha}{2},
\qquad
v=\tan\frac{\beta}{2},
\]

则

\[
\sin\alpha=\frac{2u}{1+u^2},
\qquad
\cos\alpha=\frac{1-u^2}{1+u^2},
\]

\[
\sin\beta=\frac{2v}{1+v^2},
\qquad
\cos\beta=\frac{1-v^2}{1+v^2},
\]

\[
dx\,dy
=\frac{4b\ell}{\pi^2}
\frac{du\,dv}{(1+u^2)(1+v^2)},
\]

且 `u,v∈[0,∞)`。

因此：

- TT / CC 的未凝聚三维被积式在 `(u,v,z)` 中是纯有理函数；
- TC / CT 的被积式只含 `sqrt(Q2(z))` 这一二次根式；
- 所有一般矩形参数 `b,ell` 均显式保留。

## 9. 实际 CAS 审计结果

本轮不是只做形式判断，实际进行了三类后端试算。

### 9.1 符号等价验证

用直接特征分解与上述不变量算子分别评价 TT 与 CC，应力张量的随机测试最大绝对差约为 `1e-15`，即达到浮点舍入误差量级，说明不变量约化正确。

### 9.2 TT / CC 代表性厚度积分

Wolfram 对一个非退化的精确有理代表状态进行了符号积分：

- TT: `P5(z)/Q6(z)`，返回精确 `RootSum + Log` 原函数，`LeafCount ≈ 149`；
- CC: `P7(z)/Q8(z)`，返回精确有理项 + `RootSum + Log` 原函数，`LeafCount ≈ 145`。

这验证了同号状态的厚度方向可以直接解析闭合。

### 9.3 混合状态代表性厚度积分

对一个 `J2<0` 的代表状态，Wolfram 返回了精确原函数，包含 `ArcSin/ArcTan/Log/RootSum` 与二次根式；但是完全展开后 `LeafCount ≈ 115489`。

因此结论不是“混合状态不能解析积分”，而是：

\[
\boxed{
\text{混合状态厚度积分数学上可闭合，但直接展开表达式极不适合作为正式理论表示。}
}
\]

另外，SymPy 对全符号 TT `P5/Q6` 原函数直接 `ratint` 在 60 s 内未完成，说明 `naive expand-then-integrate` 后端策略仍不适用。

## 10. 当前 PASS / FAIL

### PASS

1. `R_m` 与 `P` 的局部应力不再需要显式主方向角 `theta`；
2. TT / CC 可降为不变量纯有理算子；
3. TC / CT 仅保留一个二次根式；
4. 厚度积分可以零数值积分地精确闭合；
5. `b` 与 `ell` 全程独立。

### 尚未 PASS

外层

\[
\int_0^b\int_0^{\ell}(\cdot)\,dy\,dx
\]

的**一般矩形、全状态、短表达式直接闭合**尚未完成。困难主要来自：

- `J2=0` 状态前沿随 `(x,y)` 变化；
- 混合状态厚度原函数虽精确，但展开后极长；
- 厚度原函数代入精确状态根后会产生代数根、对数和反三角函数的二维组合。

因此下一步不应回退空间数值积分，也不应恢复板级多项式拟合；应继续做“厚度先凝聚 + 外层二维不变量/切半角解析编译”，优先保持原函数为 `RootSum / AlgebraicNumber / compact special-function object`，禁止把它完全展开成十万项表达式。
