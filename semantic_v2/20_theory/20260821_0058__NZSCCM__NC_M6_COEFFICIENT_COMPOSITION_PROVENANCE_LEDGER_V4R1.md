# NZ-SCCM — NC-M6 系数组成与来源总账 V4R1

时间：2026-08-21 00:58 +08:00

状态：`ONE_CONTINUOUS_COMPLETE_HALFWAVE / NC_M6_FROZEN / D-q-alpha / NO_UV_PDE / NO_G18_REOPEN / COEFFICIENT_PROVENANCE_LOCK / NO_CASE21 / NO_LIMIT_DERIVATIVES`

## 0. 治理纠正

本节点只做当前 NC-M6 三函数解析积分的系数组成/来源说明，不增加任何新理论。此前 V3 为解释 `a_cc` 而重新引入 G18 的做法撤回；当前活动推导不重新打开 G18。

当前 NC-M6 直接冻结：

\[
a_{cc}=0.1072329249362415,
\qquad
a_t=1-2^{-1/8}.
\]

`a_cc` 在当前正式 architecture 节点中是冻结材料常数；本节点不臆造其更早来源。

## 1. 主链

唯一结构全局变量：

\[
(D,q,\alpha).
\]

一个完整代表半波：

\[
X=\pi x/b,\quad Y=\pi y/\ell,\quad k=b/\ell,\quad \zeta=2z/t_r.
\]

\[
w=b(q_0+q)\sin X\sin Y.
\]

正式链：

`(D,q,alpha) -> second-order strain -> NC-M6 stress -> P,Rq,Ralpha -> half-angle rationalization -> exact thickness integration -> exact 2D period`。

不再引入任意 `u(x,y),v(x,y)` PDE。

## 2. 一级派生参数

\[
\kappa=E_0\varepsilon_{c0}/f_c,\qquad
\rho=f_t/f_c,\qquad
x_{cr}=\rho/\kappa=f_t/(E_0\varepsilon_{c0}).
\]

\[
M(q)=\frac{\pi^2}{\varepsilon_0}\left(q_0q+\frac12q^2\right),
\qquad
B(q)=\frac{\pi^2t_r}{2\varepsilon_0b}q.
\]

对 NC：`epsilon0 = epsilon_c0`。

## 3. 半角基础多项式

取

\[
\xi=\tan(X/2),\quad \eta=\tan(Y/2),\quad
U=1+\xi^2,\quad V=1+\eta^2,\quad \mathscr D=U^2V^2.
\]

\[
F_x^\#=4\eta^2(1-\xi^2)^2,
\quad
F_y^\#=4\xi^2(1-\eta^2)^2,
\quad
H^\#=4\xi\eta UV.
\]

\[
A_x^\#=-\mathscr D/4-2\nu k^2\xi^2V^2-2\eta^2U^2+16\xi^2\eta^2,
\]

\[
A_y^\#=\nu\mathscr D/4-2k^2\xi^2V^2-2\nu\eta^2U^2+16k^2\xi^2\eta^2,
\]

\[
A_\gamma^\#=-8k\xi\eta(1-\xi^2)(1-\eta^2).
\]

数字 `4,8,16` 只来自半角恒等式和代数展开，不是材料参数。

## 4. 六个一级应变系数

\[
E_x=X_0+X_1\zeta,
\quad
E_y=Y_0+Y_1\zeta,
\quad
G=G_0+G_1\zeta,
\]

其中

\[
X_0=\nu D\mathscr D+MF_x^\#+\alpha A_x^\#,
\quad X_1=BH^\#,
\]

\[
Y_0=-D\mathscr D+k^2MF_y^\#+\alpha A_y^\#,
\quad Y_1=k^2BH^\#,
\]

\[
G_0=8k(M-\alpha)\xi\eta(1-\xi^2)(1-\eta^2),
\]

\[
G_1=-2kB(1-\xi^2)(1-\eta^2)UV.
\]

所有后续结构大系数均由这六项通过加减乘平方生成。

## 5. 唯一二次根的系数组成

\[
\Delta_E=E_x-E_y=\Delta_0+\Delta_1\zeta,
\quad
\Delta_0=X_0-Y_0,
\quad
\Delta_1=X_1-Y_1,
\]

\[
\Sigma_E=E_x+E_y=\Sigma_0+\Sigma_1\zeta,
\quad
\Sigma_0=X_0+Y_0,
\quad
\Sigma_1=X_1+Y_1.
\]

\[
Q=\Delta_E^2+G^2
=\mathcal Q_2\zeta^2+\mathcal Q_1\zeta+\mathcal Q_0,
\]

\[
\mathcal Q_0=\Delta_0^2+G_0^2,
\quad
\mathcal Q_1=2(\Delta_0\Delta_1+G_0G_1),
\quad
\mathcal Q_2=\Delta_1^2+G_1^2.
\]

任意平铺单项式系数均由普通多项式卷积产生，不具有独立物理身份。

\[
R=\sqrt Q.
\]

主材料坐标：

\[
L=\Sigma_E/[2(1-\nu)\mathscr D],
\quad
\beta=1/[2(1+\nu)\mathscr D],
\]

\[
\lambda_1=L+\beta R,
\quad
\lambda_2=L-\beta R.
\]

## 6. 二次代数 pair 规则

任意对象写为 `Z=Z0+Z1 R`。

加法：

\[
(A,B)+(C,D)=(A+C,B+D).
\]

乘法：

\[
(A,B)\odot(C,D)=(AC+BDQ,AD+BC).
\]

若 `Z^n=P_n+S_n R`：

\[
P_{n+1}=AP_n+BS_nQ,
\qquad
S_{n+1}=AS_n+BP_n.
\]

因此所有 `T_NC` 多项式、TT 八次 interaction、compression rational 都保持 `A+B R`，不会产生第二个独立根式。

## 7. 材料 branch 组合规律

物理 sector 只有 CC/TC/TT。五段 `T_NC` 导致解析记账数：

\[
1\ (CC)+5\ (TC)+15\ (ordered\ TT)=21.
\]

乘 `P,Rq,Ralpha` 三类结构核得到 63 个 CAS kernel；它们不是新增物理方程。

TC 的五个子式只差当前 `T_i` 的固定多项式系数；TT 的十五个子式只差有序 `(T_i,T_j)` 组合。

## 8. 冻结 T_NC 数字规则

当前冻结源式中的小数保持原值，不擅自改成“更漂亮”的近似循环分数。

例如 T2：

\[
\chi=(r-0.7)/0.8,
\]

\[
T_2=0.7+0.8\chi-1.94\chi^3+2.04777777778\chi^4-0.646666666667\chi^5.
\]

只有 `0.7=7/10`, `0.8=4/5`, `1.94=97/50` 可无歧义精确改写；其余有限小数以冻结显示值为权威，除非原始来源另有精确分数定义。

T4 同理保持冻结显示值：

\[
T_4=0.377777777778-0.155555555556\psi+0.155555555556\psi^3-0.0777777777778\psi^4,
\quad \psi=(r-9)/2.
\]

## 9. 三个结构 kernel 的统一终端形式

对任一 branch，最终可写

\[
\Sigma_x=X_0^\sigma+X_1^\sigma R,
\quad
\Sigma_y=Y_0^\sigma+Y_1^\sigma R,
\quad
\Sigma_{xy}=T_0^\sigma+T_1^\sigma R.
\]

轴力核：

\[
K_P=\Sigma_y/(UV).
\]

\[
R_\alpha=\frac{f_c\varepsilon_0b\ell t_r}{\pi^2}\iiint
\frac{\Sigma_xA_x^\#+\Sigma_yA_y^\#+\Sigma_{xy}A_\gamma^\#}{UV\mathscr D}
\,d\zeta d\eta d\xi.
\]

\[
R_q=\frac{f_c\varepsilon_0b\ell t_r}{\pi^2}\iiint
\frac{\Sigma_xQ_x^\#+\Sigma_yQ_y^\#+\Sigma_{xy}Q_\gamma^\#}{UV\mathscr D}
\,d\zeta d\eta d\xi.
\]

所以所有 branch 的三个实际 integrand 都统一为

\[
K_j=K_{j0}+K_{j1}R,
\qquad j=P,q,\alpha.
\]

## 10. 厚度 front 和解析积分

所有 sector/T_NC front 对 `zeta` 都是至多二次的精确代数方程，端点由二次公式给出；不是空间 cell。

固定 `(xi,eta)` 和 branch 后，采用 Euler substitution

\[
\omega=R+\sqrt{\mathcal Q_2}\zeta
\]

把

\[
K_jd\zeta
\]

变成普通有理函数 `N_j(omega)/D_j(omega) d omega`。一次/二次因子继续化为 rational+log+arctan；一般高次不可约因子可用 exact RootSum 保存。RootSum 不是数值积分。

## 11. 板面 exact-period 系数规律

对任一 `P(xi,eta)=sum c_ij xi^i eta^j`，紧化

\[
\xi=r/(1-r),\qquad \eta=s/(1-s)
\]

后，清分母多项式系数由 `c_ij` 和二项式系数卷积唯一生成。因此最终 Aomoto-Gelfand/GKZ period 系数不是拟合参数，而是前述有限代数账本的结果。

## 12. 当前最终目标

\[
P=P(D,q,\alpha),
\qquad
R_q=R_q(D,q,\alpha),
\qquad
R_\alpha=R_\alpha(D,q,\alpha).
\]

当前不求极限导数、不运行 Case21。后续所有 coefficient 必须能回溯为：

1. 运动学系数 `(D,M,alpha,B)`；
2. 几何/半角系数 `(k,2,4,8,16,...)`；
3. NC-M6 材料系数 `(kappa,rho,xcr,a_cc,a_t,T_NC knots/coefficients)`；
4. 纯代数生成系数（pair、卷积、共轭、通分、部分分式、坐标紧化）。

任何不能回溯到这四类的系数都不得进入正式理论。
