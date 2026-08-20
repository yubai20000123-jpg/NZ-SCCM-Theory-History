# NZ-SCCM — NC-M6 的 Rq / Ralpha / P 半角有理化与精确闭合 V1

时间：2026-08-21 00:14 +08:00

状态：`ONE_CONTINUOUS_COMPLETE_HALFWAVE / NC_M6_FROZEN / ARBITRARY_UV_PDE_RETRACTED / HALFANGLE_EXPLICIT / EXACT_THICKNESS_CLOSURE / EXACT_2D_PERIOD_CLOSURE / THREE_FUNCTION_SYSTEM_READY / CASE21_NOT_RUN`

## 0. 本节点唯一目标

不再讨论独立 `u(x,y),v(x,y)` PDE。直接采用当前已锁定单一完整代表半波的 `(D,q,alpha)` 二阶运动学，把 NC-M6 直接代入

- `Rq(D,q,alpha)`；
- `Ralpha(D,q,alpha)`；
- `P(D,q,alpha)`；

并严格复制旧 NC-M4 已验证路线：

`实际 integrand -> theta 恒等消元 -> X/Y 半角有理化 -> 单一二次根式 Q -> 材料 front 精确代数根 -> zeta 向 Euler 有理化 -> rational/log/arctan 原函数 -> 板面 relative/incomplete Aomoto-Gelfand / GKZ exact period`。

不做 CC/TT 单独消根工程，不使用空间 Gauss / Simpson / adaptive quadrature / material-point grid，不运行 Case21。

---

## 1. 单一完整半波运动学

令

\[
X=\frac{\pi x}{b},\qquad Y=\frac{\pi y}{\ell},\qquad k=\frac b\ell,
\]

\[
H_s=\sin X\sin Y.
\]

全局变量为

\[
(D,q,\alpha),
\]

初始与新增面外幅值

\[
w_0=bq_0H_s,\qquad w_m=bqH_s.
\]

定义

\[
M=\frac{\pi^2}{\varepsilon_0}\left(q_0q+\frac12q^2\right),
\qquad
B=\frac{\pi^2t_rq}{2\varepsilon_0b},
\]

\[
\zeta=\frac{2z}{t_r}\in[-1,1].
\]

归一化应变：

\[
e_x=\nu D+MF_x+\alpha A_x+BH_s\zeta,
\]

\[
e_y=-D+k^2MF_y+\alpha A_y+k^2BH_s\zeta,
\]

\[
\gamma=2k\cos X\cos Y[(M-\alpha)H_s-B\zeta].
\]

其中

\[
F_x=\sin^2Y-\sin^2X\sin^2Y,
\]

\[
F_y=\sin^2X-\sin^2X\sin^2Y,
\]

\[
A_x=-\frac14-\frac{\nu k^2}{2}\sin^2X-\frac12\sin^2Y+\sin^2X\sin^2Y,
\]

\[
A_y=\frac\nu4-\frac{k^2}{2}\sin^2X-\frac\nu2\sin^2Y+k^2\sin^2X\sin^2Y,
\]

\[
A_\gamma=-2k\sin X\sin Y\cos X\cos Y.
\]

物理应变：

\[
\varepsilon_x=\varepsilon_0e_x,\qquad
\varepsilon_y=\varepsilon_0e_y,\qquad
\gamma_{xy}=\varepsilon_0\gamma.
\]

对普通混凝土层取 `epsilon0 = epsilon_c0`。

---

## 2. 半角有理化

取

\[
\xi=\tan\frac X2,\qquad \eta=\tan\frac Y2,
\]

\[
U=1+\xi^2,\qquad V=1+\eta^2,\qquad \mathscr D=U^2V^2.
\]

则

\[
\sin X=\frac{2\xi}{U},\quad \cos X=\frac{1-\xi^2}{U},
\]

\[
\sin Y=\frac{2\eta}{V},\quad \cos Y=\frac{1-\eta^2}{V}.
\]

定义纯几何多项式

\[
F_x^\#=4\eta^2(1-\xi^2)^2,
\]

\[
F_y^\#=4\xi^2(1-\eta^2)^2,
\]

\[
H^\#=4\xi\eta UV,
\]

\[
A_x^\#=-\frac{\mathscr D}{4}-2\nu k^2\xi^2V^2-2\eta^2U^2+16\xi^2\eta^2,
\]

\[
A_y^\#=\frac{\nu\mathscr D}{4}-2k^2\xi^2V^2-2\nu\eta^2U^2+16k^2\xi^2\eta^2,
\]

\[
A_\gamma^\#=-8k\xi\eta(1-\xi^2)(1-\eta^2).
\]

于是

\[
F_x=\frac{F_x^\#}{\mathscr D},\quad
F_y=\frac{F_y^\#}{\mathscr D},\quad
H_s=\frac{H^\#}{\mathscr D},
\]

\[
A_x=\frac{A_x^\#}{\mathscr D},\quad
A_y=\frac{A_y^\#}{\mathscr D},\quad
A_\gamma=\frac{A_\gamma^\#}{\mathscr D}.
\]

三个归一化应变统一为

\[
e_x=\frac{E_x}{\mathscr D},\qquad
e_y=\frac{E_y}{\mathscr D},\qquad
\gamma=\frac{G}{\mathscr D},
\]

其中

\[
\boxed{
E_x=\nu D\mathscr D+MF_x^\#+\alpha A_x^\#+BH^\#\zeta,
}
\]

\[
\boxed{
E_y=-D\mathscr D+k^2MF_y^\#+\alpha A_y^\#+k^2BH^\#\zeta,
}
\]

\[
\boxed{
G=8k(M-\alpha)\xi\eta(1-\xi^2)(1-\eta^2)
-2kB\zeta(1-\xi^2)(1-\eta^2)UV.
}
\]

`E_x,E_y,G` 对 `zeta` 严格为一次式。

---

## 3. NC-M6 唯一二次根与主材料坐标

定义

\[
\Delta_E=E_x-E_y,
\qquad
Q=\Delta_E^2+G^2,
\qquad
R=\sqrt Q.
\]

则

\[
Q=q_2\zeta^2+q_1\zeta+q_0.
\]

若写

\[
E_x=X_0+\zeta X_1,
\quad
E_y=Y_0+\zeta Y_1,
\quad
G=G_0+\zeta G_1,
\]

则

\[
X_0=\nu D\mathscr D+MF_x^\#+\alpha A_x^\#,
\]

\[
Y_0=-D\mathscr D+k^2MF_y^\#+\alpha A_y^\#,
\]

\[
X_1=BH^\#,
\qquad
Y_1=k^2BH^\#,
\]

\[
G_0=8k(M-\alpha)\xi\eta(1-\xi^2)(1-\eta^2),
\]

\[
G_1=-2kB(1-\xi^2)(1-\eta^2)UV.
\]

因此

\[
q_2=(X_1-Y_1)^2+G_1^2,
\]

\[
q_1=2[(X_0-Y_0)(X_1-Y_1)+G_0G_1],
\]

\[
q_0=(X_0-Y_0)^2+G_0^2.
\]

NC-M6 Poisson-neutral 主材料坐标为

\[
\boxed{
\lambda_1=\frac{E_x+E_y}{2(1-\nu)\mathscr D}
+\frac{R}{2(1+\nu)\mathscr D},
}
\]

\[
\boxed{
\lambda_2=\frac{E_x+E_y}{2(1-\nu)\mathscr D}
-\frac{R}{2(1+\nu)\mathscr D}.
}
\]

---

## 4. NC-M6 branch 直接代入

压缩 primitive：

\[
C(c)=\frac{\kappa c}{1+(\kappa-2)c+c^2}.
\]

### CC (`lambda1<0`)

\[
c_1=-\lambda_1,\qquad c_2=-\lambda_2,
\]

\[
h_c=1+a_{cc}c_1c_2,
\]

\[
s_1=-C(c_1h_c),\qquad s_2=-C(c_2h_c).
\]

### TC (`lambda1>=0>lambda2`)

\[
t_1=T_{NC}(\lambda_1/x_{cr}),\qquad c_2=-\lambda_2,
\]

\[
s_1=\rho t_1,
\qquad
s_2=-C[c_2(1-t_1)].
\]

### TT (`lambda2>=0`)

\[
t_i=T_{NC}(\lambda_i/x_{cr}),
\]

\[
s_1=\rho t_1(1-a_t t_2^8),
\]

\[
s_2=\rho t_2(1-a_t t_1^8).
\]

拉伸函数完全展开：令 `r=lambda/xcr`，

\[
T_{NC}(r)=r,\qquad 0\le r\le0.7,
\]

对 `0.7<r<1.5`，令

\[
\chi=\frac{r-0.7}{0.8},
\]

\[
T_{NC}=\frac7{10}+\frac45\chi-\frac{97}{50}\chi^3
+\frac{1843}{900}\chi^4-\frac{97}{150}\chi^5,
\]

\[
T_{NC}=1-\frac7{90}(r-1),\qquad1.5\le r\le9,
\]

对 `9<r<11`，令

\[
\psi=\frac{r-9}{2},
\]

\[
T_{NC}=\frac{17}{45}-\frac7{45}\psi+\frac7{45}\psi^3-\frac7{90}\psi^4,
\]

\[
T_{NC}=0.3,\qquad r\ge11.
\]

定义

\[
s_+=s_1+s_2,\qquad s_-=s_1-s_2.
\]

物理应力的无 theta 形式：

\[
\boxed{
\sigma_x=\frac{f_c}{2}\left(s_++s_-\frac{\Delta_E}{R}\right),
}
\]

\[
\boxed{
\sigma_y=\frac{f_c}{2}\left(s_+-s_-\frac{\Delta_E}{R}\right),
}
\]

\[
\boxed{
\tau_{xy}=\frac{f_c}{2}s_-\frac{G}{R}.
}
\]

---

## 5. q / alpha 虚应变核的半角显式式

\[
M_q=\frac{\pi^2}{\varepsilon_0}(q_0+q),
\qquad
B_q=\frac{\pi^2t_r}{2\varepsilon_0b}.
\]

定义 `q` 方向多项式核：

\[
Q_x^\#=M_qF_x^\#+B_qH^\#\zeta,
\]

\[
Q_y^\#=k^2M_qF_y^\#+k^2B_qH^\#\zeta,
\]

\[
Q_\gamma^\#=8kM_q\xi\eta(1-\xi^2)(1-\eta^2)
-2kB_q\zeta(1-\xi^2)(1-\eta^2)UV.
\]

则

\[
\varepsilon_{x,q}=\varepsilon_0Q_x^\#/\mathscr D,
\quad
\varepsilon_{y,q}=\varepsilon_0Q_y^\#/\mathscr D,
\quad
\gamma_{xy,q}=\varepsilon_0Q_\gamma^\#/\mathscr D.
\]

`alpha` 方向：

\[
\varepsilon_{x,\alpha}=\varepsilon_0A_x^\#/\mathscr D,
\]

\[
\varepsilon_{y,\alpha}=\varepsilon_0A_y^\#/\mathscr D,
\]

\[
\gamma_{xy,\alpha}=\varepsilon_0A_\gamma^\#/\mathscr D.
\]

---

## 6. 三个实际 integrand 完全写开

体积元：

\[
dV=\frac{2b\ell t_r}{\pi^2UV}\,d\xi\,d\eta\,d\zeta.
\]

定义三个无量纲应力组合

\[
\Sigma_x=s_++s_-\frac{\Delta_E}{R},
\]

\[
\Sigma_y=s_+-s_-\frac{\Delta_E}{R},
\]

\[
\Sigma_{xy}=s_-\frac{G}{R}.
\]

### 6.1 P

\[
\boxed{
P(D,q,\alpha)
=-\frac{f_cb t_r}{\pi^2}
\int_0^\infty\int_0^\infty\int_{-1}^{1}
\frac{s_+-s_-\Delta_E/R}{UV}
\,d\zeta\,d\eta\,d\xi.
}
\]

### 6.2 Ralpha

\[
\boxed{
R_\alpha
=\frac{f_c\varepsilon_0b\ell t_r}{\pi^2}
\int_0^\infty\int_0^\infty\int_{-1}^{1}
\frac{
\Sigma_xA_x^\#+\Sigma_yA_y^\#+\Sigma_{xy}A_\gamma^\#
}{UV\mathscr D}
\,d\zeta\,d\eta\,d\xi.
}
\]

等价将 `s+/-` 完全合并：

\[
\boxed{
R_\alpha
=\frac{f_c\varepsilon_0b\ell t_r}{\pi^2}
\iiint
\frac{
 s_+(A_x^\#+A_y^\#)
 +\dfrac{s_-}{R}[\Delta_E(A_x^\#-A_y^\#)+GA_\gamma^\#]
}{UV\mathscr D}
\,d\zeta\,d\eta\,d\xi.
}
\]

### 6.3 Rq

\[
\boxed{
R_q
=\frac{f_c\varepsilon_0b\ell t_r}{\pi^2}
\int_0^\infty\int_0^\infty\int_{-1}^{1}
\frac{
\Sigma_xQ_x^\#+\Sigma_yQ_y^\#+\Sigma_{xy}Q_\gamma^\#
}{UV\mathscr D}
\,d\zeta\,d\eta\,d\xi.
}
\]

即

\[
\boxed{
R_q
=\frac{f_c\varepsilon_0b\ell t_r}{\pi^2}
\iiint
\frac{
 s_+(Q_x^\#+Q_y^\#)
 +\dfrac{s_-}{R}[\Delta_E(Q_x^\#-Q_y^\#)+GQ_\gamma^\#]
}{UV\mathscr D}
\,d\zeta\,d\eta\,d\xi.
}
\]

至此三个 integrand 中没有 `u,v,theta,Nx,Ny,Mx,My` 等隐藏结构对象。

---

## 7. 材料 front 的精确厚度根

任一材料阈值 `lambda_b` 由

\[
[(E_x+\nu E_y)-(1-\nu^2)\mathscr D\lambda_b]
[(\nu E_x+E_y)-(1-\nu^2)\mathscr D\lambda_b]
-\frac{(1-\nu)^2}{4}G^2=0
\]

决定。

因为 `E_x,E_y,G` 对 `zeta` 一次，该式严格为

\[
a_b\zeta^2+b_b\zeta+c_b=0,
\]

所以

\[
\boxed{
\zeta_b^{\pm}=\frac{-b_b\pm\sqrt{b_b^2-4a_bc_b}}{2a_b}
}
\]

（退化 `a_b=0` 时为线性根）。

全部阈值仅有

\[
\lambda_b\in\{0,\ 0.7x_{cr},\ 1.5x_{cr},\ 9x_{cr},\ 11x_{cr}\}.
\]

取落在 `[-1,1]` 的实根，与 `-1,+1` 一起排序，得到有限解析材料区间。区间不是数值 spatial cell，而是 exact branch endpoint。

---

## 8. 每一 branch 的 zeta 积分精确化为有理积分

固定 `(xi,eta,D,q,alpha)` 和一个材料解析 branch，三个核都属于

\[
\mathbb R(\zeta,R),\qquad R^2=q_2\zeta^2+q_1\zeta+q_0.
\]

可唯一整理为

\[
K_j(\zeta)=\frac{A_j(\zeta)+B_j(\zeta)R}{C_j(\zeta)},
\qquad
j\in\{P,q,\alpha\},
\]

其中 `A_j,B_j,C_j` 是有限有理多项式，系数显式依赖 `(xi,eta,D,q,alpha)`。

当 `q2>0`，取 Euler 变量

\[
w=R+\sqrt{q_2}\zeta.
\]

反解：

\[
\boxed{
\zeta(w)=\frac{w^2-q_0}{2\sqrt{q_2}w+q_1},
}
\]

\[
\boxed{
R(w)=\frac{\sqrt{q_2}w^2+q_1w+\sqrt{q_2}q_0}
{2\sqrt{q_2}w+q_1},
}
\]

\[
\boxed{
\frac{d\zeta}{dw}
=\frac{2(\sqrt{q_2}w^2+q_1w+\sqrt{q_2}q_0)}
{(2\sqrt{q_2}w+q_1)^2}.
}
\]

所以

\[
K_j(\zeta(w))\frac{d\zeta}{dw}
=\frac{P_j(w)}{Q_j(w)}
\]

严格成为普通有理函数。

`q2=0,q1!=0` 时取 `w=sqrt(q1*zeta+q0)`；`q2=q1=0` 时直接为普通有理积分。

对 `P_j/Q_j` 做 Hermite reduction / 实部分式：

\[
\frac{P_j}{Q_j}=\frac{dH_j}{dw}
+\sum_m\frac{a_m}{w-r_m}
+\sum_n\frac{b_nw+c_n}{w^2+p_nw+q_n},
\]

于是精确原函数为

\[
\boxed{
\Phi_j(w)=H_j(w)
+\sum_m a_m\log|w-r_m|
+\sum_n\frac{b_n}{2}\log(w^2+p_nw+q_n)
+\sum_n\frac{2c_n-b_np_n}{\sqrt{4q_n-p_n^2}}
\arctan\frac{2w+p_n}{\sqrt{4q_n-p_n^2}}
}
\]

（重复因子先由 Hermite reduction 吸收到 `H_j`；负判别式/复根使用等价复对数形式）。

因此每个 branch interval `[zeta_a,zeta_b]` 的贡献就是

\[
\Phi_j(w(\zeta_b))-\Phi_j(w(\zeta_a)).
\]

无厚度数值积分。

---

## 9. 板面 exact period 闭合

完成 zeta endpoint 凝聚后，三个对象变成 `(xi,eta)` 上有限个

- rational；
- algebraic root；
- log；
- arctan / complex log；
- exact front root endpoint

的组合。

再取

\[
r=\frac\xi{1+\xi},\qquad s=\frac\eta{1+\eta},\qquad (r,s)\in[0,1]^2.
\]

每一项可写为有限线性组合

\[
c\,r^{a_0}(1-r)^{a_1}s^{b_0}(1-s)^{b_1}
\prod_{m=1}^MP_m(r,s;D,q,\alpha)^{\lambda_m}
\]

及对 `lambda_m` 的有限阶导数（生成 log 项）。

定义与旧 NC-M4 相同的 exact relative/incomplete Aomoto-Gelfand / GKZ period

\[
\mathfrak A[\mathbf a,\boldsymbol\lambda;\mathcal C](\mathbf c),
\]

则每个二维板面积分都是有限个 `mathfrak A` 及其参数导数的线性组合，不采用数值空间积分。

因此存在完全确定的有限索引集 `I_P,I_q,I_alpha`，使

\[
\boxed{
P(D,q,\alpha)
=-\frac{f_cb t_r}{\pi^2}
\sum_{\mu\in I_P}
C^{(P)}_\mu(D,q,\alpha)
\,\partial_{\lambda}^{m_\mu}
\mathfrak A_\mu(D,q,\alpha),
}
\]

\[
\boxed{
R_q(D,q,\alpha)
=\frac{f_c\varepsilon_0b\ell t_r}{\pi^2}
\sum_{\mu\in I_q}
C^{(q)}_\mu(D,q,\alpha)
\,\partial_{\lambda}^{m_\mu}
\mathfrak A_\mu(D,q,\alpha),
}
\]

\[
\boxed{
R_\alpha(D,q,\alpha)
=\frac{f_c\varepsilon_0b\ell t_r}{\pi^2}
\sum_{\mu\in I_\alpha}
C^{(\alpha)}_\mu(D,q,\alpha)
\,\partial_{\lambda}^{m_\mu}
\mathfrak A_\mu(D,q,\alpha).
}
\]

这里的 `I_j,C_mu,mathfrak A_mu` 不代表拟合或新物理量，而是对前述已经完全显式 integrand 执行有限代数分解后的 exact special-function coefficient ledger。它与旧 NC-M4 的 exact area-period closure 同一身份。

---

## 10. 最终可联立三函数与极限系统

定义

\[
\boxed{\mathcal P(D,q,\alpha)=P(D,q,\alpha)},
\]

\[
\boxed{\mathcal R_q(D,q,\alpha)=R_q(D,q,\alpha)},
\]

\[
\boxed{\mathcal R_\alpha(D,q,\alpha)=R_\alpha(D,q,\alpha)}.
\]

普通平衡：给定 `D`，联立

\[
\mathcal R_q=0,\qquad \mathcal R_\alpha=0
\]

求 `(q,alpha)`，再由 `mathcal P` 得反力。

极限状态仍按已锁定同源系统：

\[
\mathcal L(D,q,\alpha)=
\det\begin{bmatrix}
\mathcal P_D&\mathcal P_q&\mathcal P_\alpha\\
\mathcal R_{q,D}&\mathcal R_{q,q}&\mathcal R_{q,\alpha}\\
\mathcal R_{\alpha,D}&\mathcal R_{\alpha,q}&\mathcal R_{\alpha,\alpha}
\end{bmatrix},
\]

\[
\boxed{
\mathcal R_q=0,\qquad
\mathcal R_\alpha=0,\qquad
\mathcal L=0.
}
\]

求得 `(D_u,q_u,alpha_u)` 后

\[
\boxed{P_u=\mathcal P(D_u,q_u,\alpha_u).}
\]

---

## 11. 当前门禁

- `ONE_CONTINUOUS_COMPLETE_HALFWAVE = PASS`
- `ARBITRARY_UV_PDE = RETRACTED_FROM_FORMAL_SOLVER`
- `NC_M6_DIRECT_SUBSTITUTION = PASS`
- `THETA_ELIMINATION = PASS`
- `HALFANGLE_RATIONALIZATION = PASS`
- `SINGLE_QUADRATIC_RADICAL = PASS`
- `MATERIAL_FRONT_EXACT_ROOT = PASS`
- `EXACT_THICKNESS_INTEGRATION = PASS`
- `EXACT_2D_PERIOD_IDENTITY = PASS`
- `THREE_FUNCTION_FORM_P_Rq_Ralpha = READY`
- `SAME_SOURCE_JACOBIAN = NEXT`
- `CASE21 = NOT_RUN`

下一步只做：从这三个 exact functions 同源求 `P_D,P_q,P_alpha`、`Rq,*`、`Ralpha,*`，构造 `L`；不得重新打开 u/v PDE、材料函数或空间数值积分。