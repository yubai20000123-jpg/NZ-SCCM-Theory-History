# NZ-SCCM — R_m 无积分符号统一 NC-M4 exact-GKZ 编译

时间：2026-08-20 18:10 +08:00

状态：`ACTIVE_DERIVATION / RM_INTEGRAL_SYMBOL_REMOVED / P_RA_NOT_YET_COMPILED`

## 0. 本节点完成标准

本节点只执行当前唯一任务的第一项：把全局

`R_m = ∭ sigma_x dV`

继续编译到**不再含空间积分符号**的标准函数形式。

不重新打开 TC/CT，不修改 NC-M4，不采用数值空间积分。

上一节点的 `61 x 84` 是按 CC/Mixed/TT 分链的 state-split pilot support；本节点进一步使用与九宫格 NC-M4 **逐状态完全等价**的全局正/负应变张量恒等表示，消除内部材料状态分区后，得到最终 R_m 单链统一 circuit。其 support 尺寸因此不同，不能混称。

---

## 1. 九宫格 NC-M4 的全局等价写法（不是新材料）

令当前面内应变张量

\[
E=\begin{bmatrix}\varepsilon_x&\gamma_{xy}/2\\\gamma_{xy}/2&\varepsilon_y\end{bmatrix}.
\]

定义主平方根

\[
R=(E^2)^{1/2},
\]

并定义正、负应变幅值张量

\[
E_+=\frac{R+E}{2},\qquad E_c=\frac{R-E}{2}.
\]

它们的特征值分别为 `max(epsilon_i,0)` 与 `max(-epsilon_i,0)`。

归一化：

\[
T=E_+/\varepsilon_{t0},\qquad C=E_c/\varepsilon_{c0}.
\]

NC-M4 拉伸矩阵函数：

\[
\mathcal T(T)=1.07515\,T(T+0.09I)
[I-0.83T+1.04T^2+0.14T^3]^{-1}.
\]

NC-M4 压缩矩阵函数：

\[
\mathcal C(C)=2C(I+C^2)^{-1}.
\]

定义

\[
t_\Sigma=\operatorname{tr}T,
\qquad
\beta_\Sigma=\frac1{1+0.15t_\Sigma^2},
\]

\[
d_C=\det\mathcal C(C),
\qquad
\alpha=\beta_\Sigma+0.16d_C.
\]

则唯一全局 current operator 为

\[
\boxed{\Sigma=f_t\mathcal T(T)-f_c\alpha\mathcal C(C).}
\]

逐状态核验：

- TT：`C=0`，所以只剩 `f_t T4`；
- Mixed(TC/CT)：`det C=0`，故 `alpha=beta(t)`；
- CC：`T=0 -> beta_Sigma=1`，故 `alpha=1+0.16 C(c1)C(c2)=eta`。

因此该式与此前九宫格四实体区**完全相同**，只是后端写成一个全局代数算子，不新增材料机制。

---

## 2. 半角空间变量

令

\[
u=\tan(X/2),\qquad v=\tan(Y/2),\qquad \zeta=2z/h,
\]

\[
U=1+u^2,\qquad V=1+v^2,
\qquad C_x=1-u^2,\qquad C_y=1-v^2,
\]

\[
D=U^2V^2.
\]

定义

\[
a_x=\pi^2S/b^2,\quad a_y=\pi^2S/\ell^2,\quad a_g=2\pi^2S/(b\ell),
\]

\[
b_x=hA\pi^2/(2b^2),\quad b_y=hA\pi^2/(2\ell^2),\quad b_g=hA\pi^2/(b\ell),
\]

其中

\[
S=A_0A+\frac12A^2.
\]

则

\[
E_x=\varepsilon_mD+4a_xv^2C_x^2+4b_x\zeta uvUV,
\]

\[
E_y=-\frac\Delta\ell D+4a_yu^2C_y^2+4b_y\zeta uvUV,
\]

\[
E_g=4a_guvC_xC_y-b_g\zeta C_xC_yUV,
\]

且

\[
\varepsilon_x=E_x/D,\quad \varepsilon_y=E_y/D,\quad \gamma_{xy}=E_g/D.
\]

面积 Jacobian：

\[
dX\,dY=4\,du\,dv/(UV).
\]

因此原来的 R_m 公共外因子是

\[
4K_0=\frac{2b\ell h}{\pi^2}.
\]

---

## 3. 稀疏 CH/current-operator circuit

变量顺序固定为 45 个：

`u,v,z,U,V,Cx,Cy,D,Ex,Ey,Eg,tau,delta,r0,r1,t0,t1,c0,c1,t20,t21,t30,t31,dt0,dt1,nt0,nt1,kc0,kc1,trt,T0,T1,C0,C1,beta,detC,alpha,S0,S1,sx,Rdet,JT,JC,JB,Jaux`.

前三个 `u,v,z` 为物理积分坐标；其余 42 个为 exact auxiliary circuit variables。

42 条多项式关系如下：

1. `U-u^2-1=0`
2. `V-v^2-1=0`
3. `Cx+u^2-1=0`
4. `Cy+v^2-1=0`
5. `D-U^2 V^2=0`
6. `Ex-eps_m D-4 ax v^2 Cx^2-4 bx z u v U V=0`
7. `Ey+(Delta/ell)D-4 ay u^2 Cy^2-4 by z u v U V=0`
8. `Eg-4 ag u v Cx Cy+bg z Cx Cy U V=0`
9. `tau D-Ex-Ey=0`
10. `4 delta D^2+Eg^2-4 Ex Ey=0`
11. `r0^2-delta r1^2+delta=0`
12. `2 r0 r1+tau r1^2-tau=0`
13. `2 eps_t0 t0-r0=0`
14. `2 eps_t0 t1-r1-1=0`
15. `2 eps_c0 c0-r0=0`
16. `2 eps_c0 c1-r1+1=0`
17. `t20-t0^2+delta t1^2=0`
18. `t21-2 t0 t1-tau t1^2=0`
19. `t30-t20 t0+delta t21 t1=0`
20. `t31-t20 t1-t21 t0-tau t21 t1=0`
21. `dt0-1+0.83 t0-1.04 t20-0.14 t30=0`
22. `dt1+0.83 t1-1.04 t21-0.14 t31=0`
23. `nt0-1.07515[t0(t0+0.09)-delta t1^2]=0`
24. `nt1-1.07515[(2t0+0.09)t1+tau t1^2]=0`
25. `kc0-1-c0^2+delta c1^2=0`
26. `kc1-2c0c1-tau c1^2=0`
27. `trt-2t0-tau t1=0`
28. `T0 dt0-delta T1 dt1-nt0=0`
29. `T0 dt1+T1 dt0+tau T1 dt1-nt1=0`
30. `C0 kc0-delta C1 kc1-2c0=0`
31. `C0 kc1+C1 kc0+tau C1 kc1-2c1=0`
32. `beta(1+0.15 trt^2)-1=0`
33. `detC-C0^2-tau C0 C1-delta C1^2=0`
34. `alpha-beta-0.16 detC=0`
35. `S0-ft T0+fc alpha C0=0`
36. `S1-ft T1+fc alpha C1=0`
37. `sx D-S0 D-S1 Ex=0`
38. `Rdet-r0^2-tau r0 r1-delta r1^2=0`
39. `JT-dt0^2-tau dt0 dt1-delta dt1^2=0`
40. `JC-kc0^2-tau kc0 kc1-delta kc1^2=0`
41. `JB-1-0.15 trt^2=0`
42. `Jaux-256 eps_t0^2 eps_c0^2 D^4 Rdet JT JC JB=0`.

关系 11–12 正是 `R^2=E^2` 的 2x2 Cayley-Hamilton pair 形式；关系 28–31 是两个矩阵有理函数的 exact pair 解。

该 circuit 的辅助变量 Jacobian 行列式严格为

\[
J_{aux}=256\varepsilon_{t0}^2\varepsilon_{c0}^2D^4Rdet\,JT\,JC\,JB,
\]

故第42式把它变成一个 auxiliary variable。以 `Jaux*sx` 作为 residue numerator 时，42 维辅助留数精确返回 `sigma_x`。

---

## 4. Cayley configuration A*_m4,Rm

每条关系 `F_j=sum_k c_{jk} x^{m_jk}`。

对每一个 monomial 建一列

\[
a_{jk}=\begin{bmatrix}e_j\\m_{jk}\end{bmatrix},
\]

其中 `e_j` 是 42 维第 j 个单位向量，`m_jk` 是按上述45变量顺序的 monomial exponent vector。

本次实际符号编译得到：

- circuit variables = 45
- polynomial relations = 42
- total Cayley rows = 87
- total Cayley columns = 137
- maximum monomials in any single relation = 5

因此

\[
\boxed{A^*_{M4,Rm}\in\mathbb Z^{87\times137}.}
\]

该矩阵不是匿名对象：它由上面的42条关系逐 monomial 按 `[e_j;m_jk]` 唯一生成。对应137个 coefficient entries 也就是42条明文关系中逐 monomial 的系数。

---

## 5. R_m 的 GKZ 参数向量

所有42个 circuit relations 在 residue period 中均为一次分母，所以

\[
\alpha_1=\cdots=\alpha_{42}=1.
\]

物理半角 Jacobian提供 `U^{-1}V^{-1}`，residue numerator 为单个 monomial `Jaux*sx`。

因此45维 Euler exponent `nu_m` 按固定变量顺序为

\[
\boxed{
\nu_m=(
1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,2
)^T.}
\]

采用 Cayley-Euler 方程约定

\[
\sum_{q=1}^{137}A^*_{iq}c_q\partial_{c_q}\Phi=\beta_i\Phi,
\]

则

\[
\boxed{\beta_m=(-\mathbf1_{42},-\nu_m)^T\in\mathbb Z^{87}.}
\]

Box 方程为对任意 `l in ker_Z(A*)`

\[
\left(\partial_c^{l_+}-\partial_c^{l_-}\right)\Phi=0.
\]

物理 branch 固定为：

- `u,v in [0,+infinity)`；
- `z in [-1,1]`；
- CH square-root auxiliary variables取 `R=(E^2)^{1/2}` 的 principal real branch；
- 其他 auxiliary variables取由42条关系连续决定的 physical branch。

这唯一确定当前所需的 relative/incomplete GKZ branch，记为

\[
\operatorname{RGKZ}_{A^*_{M4,Rm}}(\beta_m;\mathbf c\mid\Gamma_{phys}).
\]

这里 `A*、beta_m、c、Gamma_phys` 均已在本文件逐项定义，不是匿名 placeholder。

---

## 6. R_m：积分符号已经消失

原式

\[
R_m=K_0\int_0^\pi\int_0^\pi\int_{-1}^{1}\sigma_x\,d\zeta\,dY\,dX
\]

经过半角变换、42维 exact residue lift 和 Cayley/GKZ 编译后，得到

\[
\boxed{
R_m(\Delta,A,\varepsilon_m)
=\frac{2b\ell h}{\pi^2}
\operatorname{RGKZ}_{A^*_{M4,Rm}}
\left(\beta_m;\mathbf c(\Delta,A,\varepsilon_m,b,\ell,h,A_0,f_c,f_t,\varepsilon_{c0},\varepsilon_{t0})\mid\Gamma_{phys}\right).
}
\]

右端不再包含 `x,y,z,X,Y,zeta,u,v` 的未求值积分符号。

`c` 的参数依赖完全来自上述42条关系；特别是

\[
a_x=\frac{\pi^2(A_0A+A^2/2)}{b^2},\quad
a_y=\frac{\pi^2(A_0A+A^2/2)}{\ell^2},\quad
a_g=\frac{2\pi^2(A_0A+A^2/2)}{b\ell},
\]

\[
b_x=\frac{hA\pi^2}{2b^2},\quad b_y=\frac{hA\pi^2}{2\ell^2},\quad b_g=\frac{hA\pi^2}{b\ell}.
\]

因此该式已经是一般矩形板 `b != ell` 下的三变量 exact standard-function form。

---

## 7. 状态修正

本节点完成的是：

`RM_EXPLICIT_INTEGRAND = PASS`

`RM_GLOBAL_UNIFIED_OPERATOR = PASS`

`RM_INTEGRAL_SYMBOL_REMOVED_TO_EXPLICIT_RELATIVE_GKZ = PASS`

但不能把它误标成“初等函数闭式”。一般三变量参数下，该 period 不保证退化为 Appell/Lauricella 或 elementary/log/arctan；如果某一具体参数集发生退化，可以进一步约化。

下一步必须沿同一个统一 circuit 扩展 `sy` 与 `tau_xy/G_A` targets，得到 P 与 R_A 的无积分符号标准函数，然后形成同源 Jacobian。