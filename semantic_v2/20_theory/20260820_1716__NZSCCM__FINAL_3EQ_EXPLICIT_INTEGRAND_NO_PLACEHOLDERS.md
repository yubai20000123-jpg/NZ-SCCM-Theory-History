# NZ-SCCM — NC-M4 最终三元方程组显式积分版（无抽象 period 占位符）

时间：2026-08-20 17:16 +08:00

状态：`ACTIVE_DERIVATION / EXPLICIT_INTEGRAND / NO_PERIOD_PLACEHOLDERS`

本节点补交上一轮尚未单独同步的“每个参数都明明白白”的显式积分形式。撤去 `a_ν,m_ν,p_ν,𝔄_ν` 等抽象压缩记号，直接保留 Nguyen 二阶运动学、θ、NC-M4 四实体区、膜力/弯矩虚功核以及最终三元极限方程。

## 1. 坐标与公共量

\[
X=\frac{\pi x}{b},\qquad Y=\frac{\pi y}{\ell},\qquad \zeta=\frac{2z}{h},
\]

\[
dx\,dy\,dz=\frac{b\ell h}{2\pi^2}\,dX\,dY\,d\zeta,
\qquad K_0=\frac{b\ell h}{2\pi^2}.
\]

\[
S=A_0A+\frac12A^2,\qquad H=A_0+A.
\]

## 2. Nguyen 二阶当前应变场

\[
\varepsilon_x=\varepsilon_m+\frac{\pi^2S}{b^2}\cos^2X\sin^2Y+\frac{hA\pi^2}{2b^2}\zeta\sin X\sin Y,
\]

\[
\varepsilon_y=-\frac{\Delta}{\ell}+\frac{\pi^2S}{\ell^2}\sin^2X\cos^2Y+\frac{hA\pi^2}{2\ell^2}\zeta\sin X\sin Y,
\]

\[
\gamma_{xy}=\frac{2\pi^2S}{b\ell}\cos X\sin X\sin Y\cos Y-\frac{hA\pi^2}{b\ell}\zeta\cos X\cos Y.
\]

## 3. 当前主方向与主应变

\[
\tan 2\theta=\frac{\gamma_{xy}}{\varepsilon_x-\varepsilon_y},
\qquad p=\cos\theta,
\qquad q=\sin\theta.
\]

\[
\varepsilon_1=p^2\varepsilon_x+q^2\varepsilon_y+pq\gamma_{xy},
\]

\[
\varepsilon_2=q^2\varepsilon_x+p^2\varepsilon_y-pq\gamma_{xy}.
\]

方向 1/2 按连续方向标签保留，不强制按大小排序，因此 TC 与 CT 都保留。

## 4. NC-M4 基础函数

\[
C(c)=\frac{2c}{1+c^2},
\]

\[
T_4(t)=1.07515\frac{t(t+0.09)}{1-0.83t+1.04t^2+0.14t^3},
\]

\[
\beta(t)=\frac{1}{1+0.15t^2},
\]

\[
\eta(c_1,c_2)=1+0.16C(c_1)C(c_2).
\]

CC：
\[
c_i=-\frac{\varepsilon_i}{\varepsilon_{c0}},\qquad
\sigma_i=-f_c\eta(c_1,c_2)C(c_i).
\]

TC：
\[
t_1=\frac{\varepsilon_1}{\varepsilon_{t0}},\qquad c_2=-\frac{\varepsilon_2}{\varepsilon_{c0}},
\]
\[
\sigma_1=f_tT_4(t_1),\qquad \sigma_2=-f_c\beta(t_1)C(c_2).
\]

CT：
\[
c_1=-\frac{\varepsilon_1}{\varepsilon_{c0}},\qquad t_2=\frac{\varepsilon_2}{\varepsilon_{t0}},
\]
\[
\sigma_1=-f_c\beta(t_2)C(c_1),\qquad \sigma_2=f_tT_4(t_2).
\]

TT：
\[
t_i=\frac{\varepsilon_i}{\varepsilon_{t0}},\qquad \sigma_i=f_tT_4(t_i).
\]

## 5. 旋回板坐标

\[
\sigma_x=p^2\sigma_1+q^2\sigma_2,
\qquad
\sigma_y=q^2\sigma_1+p^2\sigma_2,
\qquad
\tau_{xy}=pq(\sigma_1-\sigma_2).
\]

例如 TC：
\[
\sigma_x^{TC}=f_tT_4(t_1)p^2-f_c\beta(t_1)C(c_2)q^2,
\]
\[
\sigma_y^{TC}=f_tT_4(t_1)q^2-f_c\beta(t_1)C(c_2)p^2,
\]
\[
\tau_{xy}^{TC}=pq\left[f_tT_4(t_1)+f_c\beta(t_1)C(c_2)\right].
\]

## 6. A 方向虚应变核

\[
G_x=\frac{\pi^2H}{b^2}\cos^2X\sin^2Y+\frac{h\pi^2}{2b^2}\zeta\sin X\sin Y,
\]

\[
G_y=\frac{\pi^2H}{\ell^2}\sin^2X\cos^2Y+\frac{h\pi^2}{2\ell^2}\zeta\sin X\sin Y,
\]

\[
G_\gamma=\frac{2\pi^2H}{b\ell}\cos X\sin X\sin Y\cos Y-\frac{h\pi^2}{b\ell}\zeta\cos X\cos Y.
\]

## 7. 三个实际积分对象

横向膜力平衡：
\[
R_m=K_0\int_0^\pi\int_0^\pi\int_{-1}^{1}\sigma_x\,d\zeta\,dY\,dX=0.
\]

轴力：
\[
P=-\frac{K_0}{\ell}\int_0^\pi\int_0^\pi\int_{-1}^{1}\sigma_y\,d\zeta\,dY\,dX.
\]

面外幅值平衡：
\[
R_A=K_0\int_0^\pi\int_0^\pi\int_{-1}^{1}\left(\sigma_xG_x+\sigma_yG_y+\tau_{xy}G_\gamma\right)d\zeta\,dY\,dX=0.
\]

TC 的完整局部核：
\[
\begin{aligned}
r_A^{TC}={}&\left[f_tT_4(t_1)p^2-f_c\beta(t_1)C(c_2)q^2\right]
\left(\frac{\pi^2H}{b^2}\cos^2X\sin^2Y+\frac{h\pi^2}{2b^2}\zeta\sin X\sin Y\right)\\
&+\left[f_tT_4(t_1)q^2-f_c\beta(t_1)C(c_2)p^2\right]
\left(\frac{\pi^2H}{\ell^2}\sin^2X\cos^2Y+\frac{h\pi^2}{2\ell^2}\zeta\sin X\sin Y\right)\\
&+pq\left[f_tT_4(t_1)+f_c\beta(t_1)C(c_2)\right]
\left(\frac{2\pi^2H}{b\ell}\cos X\sin X\sin Y\cos Y-\frac{h\pi^2}{b\ell}\zeta\cos X\cos Y\right).
\end{aligned}
\]

其余 CC/CT/TT 由对应已明写的 \(\sigma_x,\sigma_y,\tau_{xy}\) 直接代入同一核，不做全域叠加。

## 8. 导数入口

\[
\varepsilon_{x,\Delta}=0,\qquad \varepsilon_{y,\Delta}=-\frac1\ell,\qquad \gamma_{xy,\Delta}=0,
\]

\[
\varepsilon_{x,m}=1,\qquad \varepsilon_{y,m}=0,\qquad \gamma_{xy,m}=0,
\]

\[
\varepsilon_{x,A}=G_x,\qquad \varepsilon_{y,A}=G_y,\qquad \gamma_{xy,A}=G_\gamma.
\]

对 \(s\in\{\sigma_x,\sigma_y,\tau_{xy}\}\)：
\[
s_{,g}=s_{,\varepsilon_x}\varepsilon_{x,g}+s_{,\varepsilon_y}\varepsilon_{y,g}+s_{,\gamma_{xy}}\gamma_{xy,g},
\qquad g\in\{\Delta,A,m\}.
\]

## 9. Jacobian 显式积分项

\[
R_{m,\Delta}=K_0\iiint\sigma_{x,\Delta},\quad
R_{m,A}=K_0\iiint\sigma_{x,A},\quad
R_{m,m}=K_0\iiint\sigma_{x,m},
\]

\[
P_{,\Delta}=-\frac{K_0}{\ell}\iiint\sigma_{y,\Delta},\quad
P_{,A}=-\frac{K_0}{\ell}\iiint\sigma_{y,A},\quad
P_{,m}=-\frac{K_0}{\ell}\iiint\sigma_{y,m},
\]

其中积分域均为 \(X,Y,\zeta\in[0,\pi]\times[0,\pi]\times[-1,1]\)。

\[
R_{A,\Delta}=K_0\iiint(\sigma_{x,\Delta}G_x+\sigma_{y,\Delta}G_y+\tau_{xy,\Delta}G_\gamma),
\]

\[
R_{A,m}=K_0\iiint(\sigma_{x,m}G_x+\sigma_{y,m}G_y+\tau_{xy,m}G_\gamma).
\]

又有
\[
G_{x,A}=\frac{\pi^2}{b^2}\cos^2X\sin^2Y,
\]
\[
G_{y,A}=\frac{\pi^2}{\ell^2}\sin^2X\cos^2Y,
\]
\[
G_{\gamma,A}=\frac{2\pi^2}{b\ell}\cos X\sin X\sin Y\cos Y,
\]

故
\[
R_{A,A}=K_0\iiint\left(\sigma_{x,A}G_x+\sigma_{y,A}G_y+\tau_{xy,A}G_\gamma+\sigma_xG_{x,A}+\sigma_yG_{y,A}+\tau_{xy}G_{\gamma,A}\right).
\]

## 10. 最终三元极限系统

\[
J_{\lim}=\begin{bmatrix}
P_{,\Delta}&P_{,A}&P_{,m}\\
R_{A,\Delta}&R_{A,A}&R_{A,m}\\
R_{m,\Delta}&R_{m,A}&R_{m,m}
\end{bmatrix}.
\]

\[
\begin{aligned}
0={}&P_{,\Delta}R_{A,A}R_{m,m}-P_{,\Delta}R_{A,m}R_{m,A}
-P_{,A}R_{A,\Delta}R_{m,m}+P_{,A}R_{A,m}R_{m,\Delta}\\
&+P_{,m}R_{A,\Delta}R_{m,A}-P_{,m}R_{A,A}R_{m,\Delta}.
\end{aligned}
\]

最终未知量严格只有
\[
(\Delta,A,\varepsilon_m).
\]

本节点不宣称空间积分已经被具体原函数完全替代；下一节点从 TC 厚度积分开始逐项解析执行。