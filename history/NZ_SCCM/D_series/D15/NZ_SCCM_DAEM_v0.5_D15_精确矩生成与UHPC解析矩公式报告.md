# D15：精确解析矩生成器与 UHPC 解析矩公式

## 1. 对 D14 的实质修正

D14 的 198 个数值系数来自板级离线投影。本轮不再拟合全局残量，而是从连续应变场和材料势逐项生成精确矩。

采用无量纲变量：

\[
X=\pi x/b,\qquad Y=\pi y/\ell,\qquad \zeta=z/b,
\]

\[
\alpha=\ell/b,\qquad \tau=t/b,\qquad a_0=A_0/b,
\qquad r=\delta/\varepsilon_0,\qquad q=A/b.
\]

连续应变为：

\[
\bar\varepsilon_x=\frac{\pi^2}{\varepsilon_0}
\left[
\left(a_0q+\frac{q^2}{2}\right)\cos^2X\sin^2Y
+q\zeta\sin X\sin Y
\right],
\]

\[
\bar\varepsilon_y=-r+\frac{\pi^2}{\alpha^2\varepsilon_0}
\left[
\left(a_0q+\frac{q^2}{2}\right)\sin^2X\cos^2Y
+q\zeta\sin X\sin Y
\right],
\]

\[
\bar\gamma=\frac{2\pi^2}{\alpha\varepsilon_0}
\left[
\left(a_0q+\frac{q^2}{2}\right)
\sin X\cos X\sin Y\cos Y
-q\zeta\cos X\cos Y
\right].
\]

每个空间单项式只调用两个精确矩：

\[
J_{pq}=\int_0^\pi \sin^pX\cos^qX\,dX,
\qquad
Z_m=\int_{-\tau/2}^{\tau/2}\zeta^m\,d\zeta.
\]

余弦奇次或厚度奇次自动为零；其余项由 Beta/Gamma 函数化为精确有理数与 \(\pi\) 的组合。这里不存在 Gauss 点、采样网格或板级回归系数。

## 2. UHPC 主应变势不需要显式求主应变

定义二维应变张量不变量：

\[
I_1=\bar\varepsilon_x+\bar\varepsilon_y,
\qquad
I_2=\bar\varepsilon_x\bar\varepsilon_y-\frac{\bar\gamma^2}{4}.
\]

两个主应变的幂和满足 Newton 递推：

\[
p_0=2,\qquad p_1=I_1,
\qquad p_j=I_1p_{j-1}-I_2p_{j-2}.
\]

因此：

\[
p_j=\bar\varepsilon_1^j+\bar\varepsilon_2^j
\]

始终是 \(\bar\varepsilon_x,\bar\varepsilon_y,\bar\gamma\) 的有限多项式，不需要显式特征值平方根，也没有主方向状态判断。

## 3. UHPC-L0 解析矩

定义无量纲材料势：

\[
\widehat\Psi_{L0}
=
\sum_{j=2}^6\frac{a_j}{j}p_j+b_2I_2.
\]

二次系数取：

\[
a_2=\frac{n_c}{1-\nu^2},
\qquad
b_2=\frac{n_c\nu}{1-\nu^2},
\qquad
n_c=\frac{E_c\varepsilon_{c0}}{f_c}.
\]

本轮已经符号验证，该二次部分严格恢复各向同性平面应力弹性能。\(a_3\sim a_6\) 只允许由 UHPC 材料曲线识别，不能用板承载力识别。

当前项目层 0 明确不采用围压增强或双轴经验修正，因此：

\[
\beta_{11}=\beta_{21}=\beta_{31}
=\beta_{02}=\beta_{12}=\beta_{03}=0.
\]

## 4. UHPC-L1 可选扩展

只有理论层级明确升级后，才允许：

\[
\begin{aligned}
\widehat\Psi_{L1}
={}&\widehat\Psi_{L0}
+\beta_{11}I_1I_2
+\beta_{21}I_1^2I_2
+\beta_{31}I_1^3I_2\\
&+\beta_{02}I_2^2
+\beta_{12}I_1I_2^2
+\beta_{03}I_2^3.
\end{aligned}
\]

这些系数只能由 UHPC 多轴材料数据约束，不得由 Swartz 板或 UCFT 板承载力反算。

## 5. 精确全局矩

本轮生成了 **156 条** 精确的“材料基—全局单项式”映射：

\[
\widehat U(r,q)
=\sum_k c_k\sum_{p,s}M_{kps}r^pq^s.
\]

每个 \(M_{kps}\) 都是 \(\alpha,\tau,a_0,\varepsilon_0\) 的显式符号函数，不是拟合数。

实际能量、平衡残量、轴力和极限条件为：

\[
U=\frac{f_c\varepsilon_0\alpha b^3}{\pi^2}\widehat U,
\]

\[
R_A=\frac{f_c\varepsilon_0\alpha b^2}{\pi^2}
\widehat U_{,q}=0,
\]

\[
P=\frac{f_cb^2}{\pi^2}\widehat U_{,r},
\]

\[
\widehat D
=\widehat U_{,rr}\widehat U_{,qq}
-\widehat U_{,rq}^2=0.
\]

运行时只需评价有限多项式并求两个代数方程，不存在空间积分循环。

## 6. D11 机器精度回归

使用同一精确矩引擎重新生成 D11 P4 能量，得到：

\[
\delta_u/\varepsilon_0=1.176946009764341,
\]

\[
A_u/b=0.012862137357895,
\qquad
A_u=15.691807576631\ \mathrm{mm},
\]

\[
P_u=514.268712063680\ \mathrm{kN}.
\]

与 D11 冻结值的差为：

\[
\Delta P=-2.274e-13\ \mathrm{kN}.
\]

因此精确矩引擎通过机器精度回归，且回归使用的空间积分点数和板级投影数均为 0。

## 7. UHPC 来源链与当前边界

项目来源锁定的 UHPC 受压曲线为胡文旭型峰前/峰后有理式；受拉曲线为纤维参数控制的指数型关系。UHPC 材料参数接口已经写入 JSON，但 \(a_3\sim a_6\) 尚未冻结为生产数值，原因是：

1. 原受压、受拉函数不是有限多项式；
2. 原点处项目定义的弹性极限切线与受拉指数函数的单侧导数并不天然相同；
3. 必须先完成材料层形状约束识别和认证域审计，不能再用板荷载决定材料系数。

周俊 Drucker–Prager 关系和王淑楠 Willam–Warnke 关系已登记为 UHPC-L1 材料约束，但不进入当前 L0。

## 8. 当前门禁

```text
D15_EXACT_GEOMETRY_MOMENT_ENGINE       = PASS
D15_RUNTIME_SPATIAL_QUADRATURE         = ZERO
D15_OFFLINE_PLATE_PROJECTION           = ZERO
D15_D11_MACHINE_PRECISION_REGRESSION   = PASS
D15_UHPC_L0_ANALYTICAL_MATRIX_FORMULA  = PASS
D15_UHPC_L1_OPTIONAL_MATRIX_FORMULA    = PASS
D15_UHPC_NUMERIC_A3_TO_A6              = PENDING
D15_UHPC_NUMERIC_BETA                  = LOCKED_ZERO_IN_L0 / PENDING_IN_L1
D15_UHPC_PANEL_CALCULATION             = NOT STARTED
D15_PRODUCTION_USE                     = NOT AUTHORIZED
```

下一门禁只剩材料层系数识别：在不使用板结果的前提下，对 \(a_3\sim a_6\) 进行形状受约束识别，并验证同一系数集能够同时恢复 UHPC 受压、受拉和初始泊松响应。
