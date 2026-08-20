# NZ-SCCM — Nguyen 二阶运动学的显式 u,v 恢复与 NC-M6 广义虚功系统

时间：2026-08-20 23:58 +08:00

状态：`SOURCE_AUDIT_CORRECTION / EXPLICIT_DISPLACEMENT_FIELD_RECOVERED / NC_M6_MATERIAL_FROZEN / NO_CASE21`

## 0. 先纠正一个来源身份

Nguyen Chapter 6 并没有给出一个唯一的解析 `u(x,y),v(x,y)`。其式 (6.1) 只写中面总位移 `u=u, v=v, w=w0+wm`；式 (6.2)-(6.3) 给出厚度点位移与二阶应变；式 (6.8) 是面内虚功平衡；Chapter 6 后续明确说 in-plane analysis 通过求解 (6.8) 完成，并在其有限元实现中用 RECAP 求解。

所以：
- 二阶运动学给的是 `u,v,w -> strain` 的关系；
- `u,v` 的具体解析形状不是 Nguyen 直接规定；
- 在当前零空间离散理论中，若要得到有限广义坐标系统，只能使用项目中已经冻结的兼容单半波面内场，而不能声称它是 Nguyen 原文唯一解。

当前共享理论总账已经冻结全局变量 `(D,q,alpha)` 及对应兼容面内重分布应变场。本节点不新造参数，而是把这个已存在的应变场反积分成显式的中面位移函数 `u(x,y),v(x,y)`，再把 NC-M6 虚功系统全部展开。

---

## 1. 坐标与面外位移

\[
X=\frac{\pi x}{b},\qquad Y=\frac{\pi y}{\ell},\qquad k=\frac b\ell.
\]

令

\[
s_X=\sin X,\ c_X=\cos X,\ s_Y=\sin Y,\ c_Y=\cos Y,\ H_s=s_Xs_Y.
\]

初始缺陷与加载新增挠度：

\[
w_0=bq_0H_s,
\]

\[
w_m=bqH_s,
\]

\[
w=w_0+w_m=b(q_0+q)H_s.
\]

其导数：

\[
w_{m,x}=\pi q c_Xs_Y,
\]

\[
w_{m,y}=\pi kq s_Xc_Y,
\]

\[
w_{0,x}=\pi q_0 c_Xs_Y,
\]

\[
w_{0,y}=\pi kq_0 s_Xc_Y,
\]

\[
w_{m,xx}=-\frac{\pi^2q}{b}H_s,
\]

\[
w_{m,yy}=-\frac{\pi^2k^2q}{b}H_s,
\]

\[
w_{m,xy}=\frac{\pi^2kq}{b}c_Xc_Y.
\]

---

## 2. 已冻结兼容面内应变场

当前总账中的面内重分布基为

\[
A_x=b_0+b_{20}\cos2X+b_{22}\cos2X\cos2Y,
\]

\[
A_y=c_{02}\cos2Y+c_{22}\cos2X\cos2Y,
\]

\[
A_\gamma=d_{22}\sin2X\sin2Y,
\]

其中

\[
b_0=-\frac{1+\nu k^2}{4},\qquad
b_{20}=\frac{\nu k^2-1}{4},\qquad
b_{22}=\frac14,
\]

\[
c_{02}=\frac{\nu-k^2}{4},\qquad
c_{22}=\frac{k^2}{4},\qquad
d_{22}=-\frac k2.
\]

等价：

\[
A_x=-\frac14-\frac{\nu k^2}{2}s_X^2-\frac12s_Y^2+s_X^2s_Y^2,
\]

\[
A_y=\frac\nu4-\frac{k^2}{2}s_X^2-\frac\nu2s_Y^2+k^2s_X^2s_Y^2,
\]

\[
A_\gamma=-2kH_sc_Xc_Y.
\]

---

## 3. 显式恢复中面位移 u(x,y),v(x,y)

取刚体平移常数为零。均匀轴压部分：

\[
u_D=\varepsilon_0\nu D\,x,
\]

\[
v_D=-\varepsilon_0D\,y.
\]

将 `A_x,A_y,A_gamma` 反积分，可取唯一到刚体平移的兼容 primitive：

\[
\boxed{
\begin{aligned}
u_A(x,y)=\varepsilon_0\alpha\frac b\pi\Bigg[&
-\frac{1+\nu k^2}{4}X
+\frac{\nu k^2-1}{8}\sin2X
+\frac18\sin2X\cos2Y
\Bigg],
\end{aligned}}
\]

\[
\boxed{
\begin{aligned}
v_A(x,y)=\varepsilon_0\alpha\frac\ell\pi\Bigg[&
\frac{\nu-k^2}{8}\sin2Y
+\frac{k^2}{8}\cos2X\sin2Y
\Bigg].
\end{aligned}}
\]

因此中面总面内位移为

\[
\boxed{
\begin{aligned}
u(x,y)=&\ \varepsilon_0\nu D\,x
+\varepsilon_0\alpha\frac b\pi\left[
-\frac{1+\nu k^2}{4}X
+\frac{\nu k^2-1}{8}\sin2X
+\frac18\sin2X\cos2Y
\right],
\end{aligned}}
\]

\[
\boxed{
\begin{aligned}
v(x,y)=&-\varepsilon_0D\,y
+\varepsilon_0\alpha\frac\ell\pi\left[
\frac{\nu-k^2}{8}\sin2Y
+\frac{k^2}{8}\cos2X\sin2Y
\right].
\end{aligned}}
\]

直接微分：

\[
u_{,x}=\varepsilon_0(\nu D+\alpha A_x),
\]

\[
v_{,y}=\varepsilon_0(-D+\alpha A_y),
\]

\[
u_{,y}+v_{,x}=\varepsilon_0\alpha A_\gamma=-2\varepsilon_0\alpha kH_sc_Xc_Y.
\]

所以该位移 primitive 与当前冻结的面内应变场严格兼容，不是通过应力反算出来的。

---

## 4. Nguyen/von Karman 二阶应变全部展开

定义

\[
S_q=q_0q+\frac12q^2.
\]

按当前项目采用的工程剪应变约定：

\[
\varepsilon_x=u_{,x}-zw_{m,xx}+\frac12w_{m,x}^2+w_{0,x}w_{m,x},
\]

\[
\varepsilon_y=v_{,y}-zw_{m,yy}+\frac12w_{m,y}^2+w_{0,y}w_{m,y},
\]

\[
\gamma_{xy}=u_{,y}+v_{,x}-2zw_{m,xy}+w_{m,x}w_{m,y}+w_{0,x}w_{m,y}+w_{0,y}w_{m,x}.
\]

于是

\[
\boxed{
\begin{aligned}
\varepsilon_x={}&\varepsilon_0\nu D
+\varepsilon_0\alpha\left[-\frac14-\frac{\nu k^2}{2}s_X^2-\frac12s_Y^2+s_X^2s_Y^2\right]\\
&+\pi^2S_q\left(s_Y^2-s_X^2s_Y^2\right)
+\frac{\pi^2q}{b}zH_s.
\end{aligned}}
\]

\[
\boxed{
\begin{aligned}
\varepsilon_y={}&-\varepsilon_0D
+\varepsilon_0\alpha\left[\frac\nu4-\frac{k^2}{2}s_X^2-\frac\nu2s_Y^2+k^2s_X^2s_Y^2\right]\\
&+\pi^2k^2S_q\left(s_X^2-s_X^2s_Y^2\right)
+\frac{\pi^2k^2q}{b}zH_s.
\end{aligned}}
\]

\[
\boxed{
\begin{aligned}
\gamma_{xy}={}&-2\varepsilon_0\alpha kH_sc_Xc_Y
+2\pi^2kS_qH_sc_Xc_Y
-\frac{2\pi^2kq}{b}zc_Xc_Y.
\end{aligned}}
\]

若使用厚度标准坐标 `zeta=2z/t_r`，弯曲项等价为

\[
\frac{\pi^2t_rq}{2b}H_s\zeta,
\qquad
\frac{\pi^2t_rk^2q}{2b}H_s\zeta,
\qquad
-\frac{\pi^2t_rkq}{b}c_Xc_Y\zeta.
\]

---

## 5. 三个广义坐标的虚应变全部展开

### D 方向

\[
\varepsilon_{x,D}=\varepsilon_0\nu,
\qquad
\varepsilon_{y,D}=-\varepsilon_0,
\qquad
\gamma_{xy,D}=0.
\]

### alpha 方向

\[
\boxed{
\varepsilon_{x,\alpha}=\varepsilon_0\left[-\frac14-\frac{\nu k^2}{2}s_X^2-\frac12s_Y^2+s_X^2s_Y^2\right],
}
\]

\[
\boxed{
\varepsilon_{y,\alpha}=\varepsilon_0\left[\frac\nu4-\frac{k^2}{2}s_X^2-\frac\nu2s_Y^2+k^2s_X^2s_Y^2\right],
}
\]

\[
\boxed{
\gamma_{xy,\alpha}=-2\varepsilon_0kH_sc_Xc_Y.
}
\]

### q 方向

\[
\boxed{
\varepsilon_{x,q}=\pi^2(q_0+q)(s_Y^2-s_X^2s_Y^2)+\frac{\pi^2}{b}zH_s,
}
\]

\[
\boxed{
\varepsilon_{y,q}=\pi^2k^2(q_0+q)(s_X^2-s_X^2s_Y^2)+\frac{\pi^2k^2}{b}zH_s,
}
\]

\[
\boxed{
\gamma_{xy,q}=2\pi^2k(q_0+q)H_sc_Xc_Y-\frac{2\pi^2k}{b}zc_Xc_Y.
}
\]

二阶仅 q-q 非零：

\[
\varepsilon_{x,qq}=\pi^2(s_Y^2-s_X^2s_Y^2),
\]

\[
\varepsilon_{y,qq}=\pi^2k^2(s_X^2-s_X^2s_Y^2),
\]

\[
\gamma_{xy,qq}=2\pi^2kH_sc_Xc_Y.
\]

---

## 6. NC-M6 直接代入

定义物理应变张量

\[
\mathbf E=\begin{bmatrix}\varepsilon_x&\gamma_{xy}/2\\\gamma_{xy}/2&\varepsilon_y\end{bmatrix}.
\]

唯一主应变根

\[
d_\varepsilon=\sqrt{(\varepsilon_x-\varepsilon_y)^2+\gamma_{xy}^2}.
\]

NC-M6 Poisson-neutral 主材料坐标

\[
\lambda_1=\frac{\varepsilon_x+\varepsilon_y}{2(1-\nu)\varepsilon_{c0}}
+\frac{d_\varepsilon}{2(1+\nu)\varepsilon_{c0}},
\]

\[
\lambda_2=\frac{\varepsilon_x+\varepsilon_y}{2(1-\nu)\varepsilon_{c0}}
-\frac{d_\varepsilon}{2(1+\nu)\varepsilon_{c0}}.
\]

在 CC/TC/TT 对应 branch 中按已冻结 NC-M6 得到 `s1,s2`，再

\[
\sigma_x=\frac{f_c}{2}\left[s_1+s_2+(s_1-s_2)\frac{\varepsilon_x-\varepsilon_y}{d_\varepsilon}\right],
\]

\[
\sigma_y=\frac{f_c}{2}\left[s_1+s_2-(s_1-s_2)\frac{\varepsilon_x-\varepsilon_y}{d_\varepsilon}\right],
\]

\[
\tau_{xy}=\frac{f_c}{2}(s_1-s_2)\frac{\gamma_{xy}}{d_\varepsilon}.
\]

---

## 7. 虚功系统：Ru/Rv 在显式位移场下不再是两个任意函数 PDE

当 `u,v` 已写成 `(D,alpha)` 的显式 compatible field，而 `w_m` 写成 `q` 的显式单半波时，任意虚位移只剩

\[
\delta D,\qquad\delta\alpha,\qquad\delta q.
\]

因此原先连续 `R_u[delta u], R_v[delta v]` 投影为有限广义虚功系数，而不是再去反求一个任意 `u(x,y),v(x,y)`。

### alpha 平衡残量

\[
\boxed{
\begin{aligned}
R_\alpha={}&\iiint_V\Bigg\{
\sigma_x\varepsilon_0\left[-\frac14-\frac{\nu k^2}{2}s_X^2-\frac12s_Y^2+s_X^2s_Y^2\right]\\
&+\sigma_y\varepsilon_0\left[\frac\nu4-\frac{k^2}{2}s_X^2-\frac\nu2s_Y^2+k^2s_X^2s_Y^2\right]\\
&-2\tau_{xy}\varepsilon_0kH_sc_Xc_Y
\Bigg\}\,dV=0.
\end{aligned}}
\]

### q / 面外幅值平衡残量

\[
\boxed{
\begin{aligned}
R_q={}&\iiint_V\Bigg\{
\sigma_x\left[\pi^2(q_0+q)(s_Y^2-s_X^2s_Y^2)+\frac{\pi^2}{b}zH_s\right]\\
&+\sigma_y\left[\pi^2k^2(q_0+q)(s_X^2-s_X^2s_Y^2)+\frac{\pi^2k^2}{b}zH_s\right]\\
&+\tau_{xy}\left[2\pi^2k(q_0+q)H_sc_Xc_Y-\frac{2\pi^2k}{b}zc_Xc_Y\right]
\Bigg\}\,dV=0.
\end{aligned}}
\]

### 轴向力函数

沿当前总账定义

\[
\boxed{
P(D,q,\alpha)=-\frac1\ell\iiint_V\sigma_y(D,q,\alpha;x,y,z)\,dV.
}
\]

所以当前平衡构形在给定 `D` 时由

\[
R_q(D,q,\alpha)=0,
\qquad
R_\alpha(D,q,\alpha)=0
\]

求 `q(D),alpha(D)`，随后得到 `P(D)`。

---

## 8. 极限承载力的直接联立系统

不需要逐加载步作为正式理论。定义

\[
\mathcal L(D,q,\alpha)=
\det\begin{bmatrix}
P_D&P_q&P_\alpha\\
R_{q,D}&R_{q,q}&R_{q,\alpha}\\
R_{\alpha,D}&R_{\alpha,q}&R_{\alpha,\alpha}
\end{bmatrix}.
\]

极限状态直接满足

\[
\boxed{
R_q=0,\qquad R_\alpha=0,\qquad\mathcal L=0.
}
\]

求得

\[
(D_u,q_u,\alpha_u),
\]

之后

\[
P_u=P(D_u,q_u,\alpha_u).
\]

对应位移场直接为

\[
u_u(x,y)=u(x,y;D_u,\alpha_u),
\]

\[
v_u(x,y)=v(x,y;D_u,\alpha_u),
\]

\[
w_u(x,y)=b(q_0+q_u)\sin X\sin Y.
\]

这正是“通过联立虚功平衡求极限承载力及对应位移状态”，而不是“由力反算未知位移函数形状”。

---

## 9. 尚未消失的来源边界问题

Nguyen 对 Swartz 24 板的有限元 in-plane boundary conditions 还明确采用：bottom edge 的 y 位移约束，以及 side edges 的 x 位移约束。当前 `(D,q,alpha)` 显式解析场是 NZ-SCCM 既有兼容单半波场，并不是 Nguyen 原 FE `u,v` 插值的逐字替代。

因此下一步若进入 Case21 之前，应单独做一次 `IN_PLANE_BOUNDARY_CONDITION_GATE`：检查当前显式 `u,v` 场是否满足本项目最终希望采用的真实试验面内边界条件；若不满足，必须在结构层修正，不得回头调 NC-M6 材料函数。

本节点不运行 Case21。