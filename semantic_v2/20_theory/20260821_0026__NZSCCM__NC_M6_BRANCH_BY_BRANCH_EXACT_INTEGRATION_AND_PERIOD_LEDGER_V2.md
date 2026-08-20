# NZ-SCCM — NC-M6 branch-by-branch 精确积分实例化与二维 exact-period 系数账本 V2

时间：2026-08-21 00:26 +08:00

状态：`ONE_CONTINUOUS_COMPLETE_HALFWAVE / NC_M6_FROZEN / 21_ANALYTIC_BRANCHES / 63_KERNELS_INSTANTIATED / THICKNESS_PRIMITIVE=HERMITE+ROOTSUM / 2D_PERIOD_LEDGER=FACTOR_DAG / CASE21_NOT_RUN`

## 0. 执行结果

本节点不做九个导数、不构造极限 Jacobian、不运行 Case21。只把上一节点仍以 `T_P,T_q,T_alpha` 表示的积分对象继续实例化。

执行后：
- 解析材料 branch 共 21 个：1 CC + 5 TC + 15 有序 TT；
- 每个 branch 生成 `P/Rq/Ralpha` 三个 kernel，共 63 个；
- 63 个 kernel 全部属于同一二次扩张 `K(zeta,R), R^2=q2*zeta^2+q1*zeta+q0`；
- Euler substitution 后 63 个 kernel 均为 `N(w)/D(w)` 有理函数；
- 厚度原函数用 exact Hermite reduction + RootSum 表示，因此不再保留厚度积分号；
- 板面 exact-period 的全部基础多项式系数与 branch DAG 已生成。

## 1. 五段 T_NC 的精确多项式

令 `r=lambda/xcr`：

\[
T_1=r.
\]

\[
T_2=-\frac{12125}{6144}r^5+\frac{438925}{36864}r^4-\frac{1012195}{36864}r^3+\frac{241045}{8192}r^2-\frac{20346463}{1474560}r+\frac{8351021}{2949120}.
\]

\[
T_3=\frac{97}{90}-\frac7{90}r.
\]

\[
T_4=-\frac7{1440}r^4+\frac7{36}r^3-\frac{231}{80}r^2+\frac{847}{45}r-\frac{64787}{1440}.
\]

\[
T_5=\frac3{10}.
\]

全部以有理数保存。

## 2. 21 个 branch

`CC`; `TC-T1`...`TC-T5`; `TT-T1T1`, `TT-T2T1`, `TT-T2T2`, `TT-T3T1`, `TT-T3T2`, `TT-T3T3`, `TT-T4T1`, `TT-T4T2`, `TT-T4T3`, `TT-T4T4`, `TT-T5T1`, `TT-T5T2`, `TT-T5T3`, `TT-T5T4`, `TT-T5T5`。

TC 的 compression denominator degree 上界依次为 4,12,4,10,2；TT 的有限代数次数上界依次为 9,41,45,9,41,9,33,44,33,36,8,40,8,32,0。高次数不产生新独立根式。

## 3. 三个 branch-local kernel

记
\[
\Delta_E=E_x-E_y,\qquad R=\sqrt{Q},\qquad s_\pm=s_1\pm s_2.
\]

对每个 branch \(b\)：

\[
K_P^{(b)}=\frac1{UV}\left(s_+^{(b)}-s_-^{(b)}\frac{\Delta_E}{R}\right).
\]

\[
K_\alpha^{(b)}=\frac1{UV\mathscr D}\left[s_+^{(b)}A_\Sigma^\#+\frac{s_-^{(b)}}R\left(\Delta_EA_\Delta^\#+GA_\gamma^\#\right)\right].
\]

\[
K_q^{(b)}=\frac1{UV\mathscr D}\left[s_+^{(b)}Q_\Sigma^\#+\frac{s_-^{(b)}}R\left(\Delta_EQ_\Delta^\#+GQ_\gamma^\#\right)\right].
\]

21 个 branch 的差别仅在 \(s_1,s_2\)。

CC:
\[
s_1=-C[(-\lambda_1)(1+a_{cc}\lambda_1\lambda_2)],\qquad s_2=-C[(-\lambda_2)(1+a_{cc}\lambda_1\lambda_2)].
\]

TC-Ti:
\[
t_1=T_i(\lambda_1/x_{cr}),\quad s_1=\rho t_1,\quad s_2=-C[(-\lambda_2)(1-t_1)].
\]

TT-TiTj:
\[
t_1=T_i(\lambda_1/x_{cr}),\qquad t_2=T_j(\lambda_2/x_{cr}),
\]
\[
s_1=\rho t_1(1-a_tt_2^8),\qquad s_2=\rho t_2(1-a_tt_1^8).
\]

## 4. Euler 有理化与 exact 厚度原函数

每个 branch 内：
\[
Q=q_2\zeta^2+q_1\zeta+q_0,\qquad R=\sqrt Q.
\]

每个 kernel 均可唯一约化为
\[
K_j^{(b)}=\frac{N_0^{(b,j)}(\zeta)+N_1^{(b,j)}(\zeta)R}{D^{(b,j)}(\zeta)}.
\]

取
\[
w=R+\sqrt{q_2}\zeta.
\]

则
\[
\zeta=\frac{w^2-q_0}{2\sqrt{q_2}w+q_1},
\]
\[
R=\frac{\sqrt{q_2}w^2+q_1w+\sqrt{q_2}q_0}{2\sqrt{q_2}w+q_1}.
\]

所以
\[
K_j^{(b)}d\zeta=\frac{\mathcal N_j^{(b)}(w)}{\mathcal D_j^{(b)}(w)}dw.
\]

对这个有理函数做 exact Hermite reduction：
\[
\frac{\mathcal N}{\mathcal D}=\frac{dH}{dw}+\frac{R_h}{S_h},\qquad S_h\ \text{squarefree}.
\]

定义厚度原函数：
\[
\boxed{\Phi(w)=H(w)+\operatorname{RootSum}_{S_h(t)=0}\left[\frac{R_h(t)}{S_h'(t)}\log(w-t)\right].}
\]

这是有理函数积分的 exact algebraic-logarithmic primitive；实数形式可组合为 rational + log + arctan。

因此任一 branch 的厚度贡献已经没有积分号：
\[
\boxed{\mathcal T_j^{(b)}=\Phi_j^{(b)}(w(\zeta_+))-\Phi_j^{(b)}(w(\zeta_-)).}
\]

## 5. 材料 front 的精确端点

全部阈值：
\[
\lambda_b\in\left\{0,\frac7{10}x_{cr},\frac32x_{cr},9x_{cr},11x_{cr}\right\}.
\]

front 方程：
\[
[(E_x+\nu E_y)-L_b][(\nu E_x+E_y)-L_b]-\frac{(1-\nu)^2}{4}G^2=0,
\]
\[
L_b=(1-\nu^2)\mathscr D\lambda_b.
\]

因为 \(E_x,E_y,G\) 对 \(\zeta\) 一次，故
\[
a_b\zeta^2+b_b\zeta+c_b=0,
\]
\[
\zeta_b^\pm=\frac{-b_b\pm\sqrt{b_b^2-4a_bc_b}}{2a_b}.
\]

所有厚度 branch 端点均由这些代数根和 \(-1,+1\) 组成，不用材料点扫描。

## 6. 三个 closed functions

对每一个 branch 的 relative cycle \(\mathcal C_b(D,q,\alpha)\)，二维板面 exact-period 记为 \(\mathfrak P_2[\cdot;\mathcal C_b]\)。则

\[
\boxed{P(D,q,\alpha)=-\frac{f_cb t_r}{\pi^2}\sum_{b=1}^{21}\mathfrak P_2[\mathcal T_P^{(b)};\mathcal C_b].}
\]

\[
\boxed{R_q(D,q,\alpha)=\frac{f_c\varepsilon_0b\ell t_r}{\pi^2}\sum_{b=1}^{21}\mathfrak P_2[\mathcal T_q^{(b)};\mathcal C_b].}
\]

\[
\boxed{R_\alpha(D,q,\alpha)=\frac{f_c\varepsilon_0b\ell t_r}{\pi^2}\sum_{b=1}^{21}\mathfrak P_2[\mathcal T_\alpha^{(b)};\mathcal C_b].}
\]

\(\mathfrak P_2\) 是由 coefficient DAG 指定的 relative/incomplete Aomoto-Gelfand / GKZ exact period，不是空间数值积分器。relative cycle 只编码真实材料 analytic branch 前沿，不是物理空间 cell。

## 7. 二维 exact-period coefficient DAG

基础多项式的 \((\xi,\eta)\) 幂次及系数已经生成：\(U\) 2项、\(V\) 2项、\(\mathscr D\) 9项、\(F_x^\#\) 3项、\(F_y^\#\) 3项、\(H^\#\) 4项、\(A_x^\#\) 9项、\(A_y^\#\) 9项、\(A_\gamma^\#\) 4项。

例如：
\[
F_x^\#=4\xi^4\eta^2-8\xi^2\eta^2+4\eta^2,
\]
\[
F_y^\#=4\xi^2\eta^4-8\xi^2\eta^2+4\xi^2,
\]
\[
H^\#=4(\xi^3\eta^3+\xi^3\eta+\xi\eta^3+\xi\eta).
\]

高层对象 \(E_x,E_y,G,\Delta_E,\Sigma_E,Q\)、front、compression denominator、Euler numerator/denominator 均作为 exact DAG 节点引用这些系数。日志项通过
\[
\log P=\left.\frac{\partial}{\partial\lambda}P^\lambda\right|_{\lambda=0}
\]
登记为 period parameter derivative。

## 8. 完成边界

当前已完成：`21 branches -> 63 kernels -> Euler rational form -> Hermite+RootSum exact thickness primitive -> 2D exact relative-period coefficient DAG`。

当前未做：不求 \(P,R_q,R_\alpha\) 的导数；不构造极限条件 \(\mathcal L\)；不运行 Case21。

下一步才允许在三个 closed functions 固定以后做同源解析微分与极限求解。