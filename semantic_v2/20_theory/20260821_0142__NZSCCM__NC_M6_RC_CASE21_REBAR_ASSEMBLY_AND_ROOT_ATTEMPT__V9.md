# NZ-SCCM — NC-M6 + 钢筋 Case21 RC 总体系装配与首次求解执行 V9

时间：2026-08-21 01:42 +08:00

状态：`NC_M6_FROZEN / REBAR_ADDED_EXACTLY / TOTAL_RC_3EQ_ASSEMBLED / STEEL_ZERO_QUADRATURE / NUMERICAL_ROOT_ATTEMPT_STOPPED_AT_CONCRETE_PERIOD_INSTANTIATION`

## 0. 裁决

本节点按 NC-M4/当前锁定 RC 路线，在求极限根之前先将双向钢筋加入 NC-M6 的 `P,Rq,Ralpha` 与全部同源导数。钢筋贡献重新由一个完整方形代表半波的有限三角积分闭式推导，不读取历史 Case21 极限根。

V7/V8 的混凝土部分目前保存的是 finite exact-period 的通用索引/生成规则，但没有实例化 Case21 的实际 period descriptor list 为可数值调用对象。因此本轮不能伪造 `Du,qu,alphau,Pu`；数值三元求根在 concrete exact-period instantiation 处 fail-fast 停止。禁止以历史 NC-M4/R10 根替代，也禁止偷偷使用空间 Gauss/adaptive quadrature。

## 1. Case21 输入

代表完整半波：
\[
b=\ell=1220\ {\rm mm},\qquad t=19.30\ {\rm mm},\qquad k=1,\qquad q_0=1/400.
\]

混凝土：
\[
f_c=21.23\ {\rm MPa},\quad E_0=20321\ {\rm MPa},\quad \varepsilon_0=0.00209,\quad\nu=0.18.
\]

当前项目普通混凝土基准继续采用
\[
f_t=0.10f_c=2.123\ {\rm MPa},
\]
故
\[
\kappa=2.000512953367875,\qquad \rho=f_t/f_c=0.1,\qquad x_{cr}=0.049987179453974.
\]

钢筋：
\[
\rho_{s,x}=\rho_{s,y}=0.00375,\qquad z_s=0,
\]
\[
E_s=200000\ {\rm MPa},\qquad f_y=530\ {\rm MPa},\qquad\varepsilon_y=0.00265.
\]

## 2. 钢筋闭式重新推导

中面钢筋归一化应变：
\[
e_{s,x}=\nu D+MF_x+\alpha A_x,
\]
\[
e_{s,y}=-D+MF_y+\alpha A_y.
\]

对一个完整方形半波精确积分：
\[
\left\langle e_{s,x}F_x+e_{s,y}F_y\right\rangle
=\frac{8D(\nu-1)+9M-5\alpha}{32},
\]
\[
\left\langle e_{s,x}A_x+e_{s,y}A_y\right\rangle
=-\frac{8D\nu(\nu+1)+5M-(4\nu^2+5)\alpha}{32},
\]
\[
\langle e_{s,y}\rangle=-D+\frac M4.
\]

定义（N-mm）
\[
C_R=\frac{\rho_sE_s\varepsilon_0^2b\ell t}{32}=2940.90386184375\ {\rm N\,mm},
\]
以及
\[
K_s=\rho_stbE_s\varepsilon_0=36908.355\ {\rm N}.
\]

弹性钢筋支内：
\[
\boxed{P_s=K_s\left(D-\frac M4\right)},
\]
\[
\boxed{R_q^s=C_RM_q[8D(\nu-1)+9M-5\alpha]},
\]
\[
\boxed{R_\alpha^s=-C_R[8D\nu(\nu+1)+5M-(4\nu^2+5)\alpha]}.
\]

无钢筋空间 Gauss 点、无钢筋数值积分。

## 3. 钢筋同源导数

\[
M_q=\frac{\pi^2}{\varepsilon_0}(q_0+q),\qquad M_{qq}=\frac{\pi^2}{\varepsilon_0}.
\]

\[
P_{s,D}=K_s,\qquad P_{s,q}=-\frac14K_sM_q,\qquad P_{s,\alpha}=0.
\]

令
\[
G_q=8D(\nu-1)+9M-5\alpha.
\]

\[
R_{q,D}^s=8C_RM_q(\nu-1),
\]
\[
R_{q,q}^s=C_R[M_{qq}G_q+9M_q^2],
\]
\[
R_{q,\alpha}^s=-5C_RM_q.
\]

\[
R_{\alpha,D}^s=-8C_R\nu(\nu+1),
\]
\[
R_{\alpha,q}^s=-5C_RM_q,
\]
\[
R_{\alpha,\alpha}^s=C_R(4\nu^2+5).
\]

弹性钢筋相自身满足 `Rq,alpha^s=Ralpha,q^s`，但总体系不据此强迫 NC-M6 concrete cross derivatives 对称。

## 4. RC 总体系

混凝土沿用 NC-M6 V7/V8：
\[
P_c(D,q,\alpha),\quad R_q^c(D,q,\alpha),\quad R_\alpha^c(D,q,\alpha).
\]

求根前总装：
\[
\boxed{P=P_c+P_s},\qquad
\boxed{R_q=R_q^c+R_q^s},\qquad
\boxed{R_\alpha=R_\alpha^c+R_\alpha^s}.
\]

全部一阶导数逐相相加。极限 Jacobian：
\[
J_{lim}=\begin{bmatrix}
P_D&P_q&P_\alpha\\
R_{q,D}&R_{q,q}&R_{q,\alpha}\\
R_{\alpha,D}&R_{\alpha,q}&R_{\alpha,\alpha}
\end{bmatrix},\qquad \mathcal L=\det J_{lim}.
\]

最终 RC 三元极限系统：
\[
\boxed{R_q=0,\qquad R_\alpha=0,\qquad\mathcal L=0}.
\]

候选根得到后，必须连续全域检查
\[
\max|\varepsilon_{s,x}|<\varepsilon_y,\qquad \max|\varepsilon_{s,y}|<\varepsilon_y.
\]
若失败，则退回 source-defined bilinear steel current law，不能继续用弹性闭式。

## 5. 数值求根的真实阻断点

V7 已定义
\[
P_c=\sum_\nu C_{P\nu}\mathfrak A_{P\nu},\quad
R_q^c=\sum_\nu C_{q\nu}\mathfrak A_{q\nu},\quad
R_\alpha^c=\sum_\nu C_{\alpha\nu}\mathfrak A_{\alpha\nu},
\]
但当前实现尚未把 Case21 的实际有限索引集 `I_P,I_q,I_alpha` 的每一个 period parameter object 实例化成可调用 special-function list。因此目前不能诚实执行 `(D,q,alpha)->Pc,Rqc,Ralphac` 及其九导数的数值调用。

当前门禁：

`REBAR_ASSEMBLY = PASS`

`RC_FINAL_3EQ = ASSEMBLED`

`STEEL_FORMAL_SPATIAL_QUADRATURE = 0`

`CASE21_NC_M6_NUMERICAL_ROOT = NOT_YET_EXECUTABLE`

唯一剩余实现项：把 V7 的通用 exact-period descriptor 生成规则实际实例化为 Case21 的 finite special-function object list。这是实现闭环，不是新理论。