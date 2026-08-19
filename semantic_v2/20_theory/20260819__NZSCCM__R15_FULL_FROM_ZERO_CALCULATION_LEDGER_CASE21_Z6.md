# NZ-SCCM R15 — Case21 + Z6 单文件完整从零计算账本

**Date:** 2026-08-19  
**Identity:** FULL FROM-ZERO CALCULATION LEDGER / SINGLE-FILE EXECUTION SPECIFICATION  
**Formal discretization:** NONE  
**Active material layer:** finite global current-material constructors only

> 本文件把 2026-08-18 锁定总账、R13、R14 与 Case21/Z6 已冻结的输入和极限定义重新编译成一个单文件执行账本。目标是：另一个 AI/CAS 只拿本文件即可从原始试件参数开始建立控制半波、连续 Nguyen 二阶运动学、有限 current material map、连续广义力/残量/一致 Jacobian，并直接求解 `(D,q,alpha)` 三元极限系统。
>
> **严格区分：**本文件是完整的“从零计算规范/账本”。文末给出的 Case21/Z6 已释放数值只作为 `SEALED REGRESSION TARGETS`；盲算时不得作为输入、选根、调参或停止条件。R15 本身不宣称在本聊天中重新用独立后端把全部非均匀三重连续积分再次数值求出。

---

# 0. 不可违反的执行规则

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
N_formal_material_points = 0
FINITE_PREFIX_CONVERGENCE_AS_EVIDENCE = PROHIBITED
DISCRETE_AUDIT_ORACLE = PROHIBITED
```

禁止：

- Gauss / Simpson / adaptive quadrature；
- 空间网格、材料点、积分点、spatial cells；
- Chebyshev spatial collocation；
- 用有限 `N` 前缀逼近作为正式或辅助验证；
- 用试验值、周思铭值、Winter 值参与求解、选根、标定；
- 用 `q=alpha=0` 的均匀材料峰值代替板极限；
- 用逐 `D` 离散加载步作为正式生产算法。

允许：

- 有限维 Newton / trust-region 等全局未知量求根；
- 符号积分、代数消元、标准特殊函数、relative period / GKZ / Mellin–Barnes / differential-system 等连续精确表示；
- 任何与原 current operator **恒等**的有限代数构造。

正式极限系统唯一为：

\[
\boxed{R_q(D,q,\alpha)=0,\qquad R_\alpha(D,q,\alpha)=0,\qquad \det J_{\lim}(D,q,\alpha)=0.}
\]

\[
\boxed{
J_{\lim}=\begin{bmatrix}
P_D&P_q&P_\alpha\\
R_{q,D}&R_{q,q}&R_{q,\alpha}\\
R_{\alpha,D}&R_{\alpha,q}&R_{\alpha,\alpha}
\end{bmatrix}.}
\]

求根后：

\[
\boxed{P_u=P(D_u,q_u,\alpha_u).}
\]

---

# 1. 坐标和统一连续运动学

物理半波域：

\[
0\le x\le b,\qquad 0\le y\le \ell.
\]

\[
X=\pi x/b,\qquad Y=\pi y/\ell,\qquad k=b/\ell.
\]

\[
s_X=\sin X,\ c_X=\cos X,\ s_Y=\sin Y,\ c_Y=\cos Y,\ H_s=s_Xs_Y.
\]

初始缺陷与新增挠曲：

\[
w_0=bq_0H_s,\qquad \Delta w=bqH_s,\qquad w=b(q_0+q)H_s.
\]

定义：

\[
\boxed{M(q)=\frac{\pi^2}{\varepsilon_0}\left(q_0q+\frac12q^2\right)},
\]

\[
\boxed{M_q=\frac{\pi^2}{\varepsilon_0}(q_0+q),\qquad M_{qq}=\frac{\pi^2}{\varepsilon_0}.}
\]

\[
F_x=s_Y^2-s_X^2s_Y^2,\qquad F_y=s_X^2-s_X^2s_Y^2.
\]

Airy 场：

\[
\boxed{A_x=-\frac14-\frac{\nu k^2}{2}s_X^2-\frac12s_Y^2+s_X^2s_Y^2,}
\]

\[
\boxed{A_y=\frac\nu4-\frac{k^2}{2}s_X^2-\frac\nu2s_Y^2+k^2s_X^2s_Y^2,}
\]

\[
\boxed{A_\gamma=-2kH_sc_Xc_Y.}
\]

为统一核心、钢面和钢筋层，直接使用物理厚度坐标 `z`：

\[
\boxed{\beta(q)=\frac{\pi^2q}{\varepsilon_0b},\qquad \beta_q=\frac{\pi^2}{\varepsilon_0b}.}
\]

任意相在厚度位置 `z` 的归一化物理应变：

\[
\boxed{e_x=\nu D+MF_x+\alpha A_x+\beta zH_s,}
\]

\[
\boxed{e_y=-D+k^2MF_y+\alpha A_y+k^2\beta zH_s,}
\]

\[
\boxed{\gamma=2kc_Xc_Y[(M-\alpha)H_s-\beta z].}
\]

实际应变：

\[
\varepsilon_x=\varepsilon_0e_x,\quad
\varepsilon_y=\varepsilon_0e_y,\quad
\gamma_{xy}=\varepsilon_0\gamma.
\]

一阶导数：

\[
\varepsilon_{x,D}=\varepsilon_0\nu,\quad
\varepsilon_{y,D}=-\varepsilon_0,\quad
\gamma_{D}=0,
\]

\[
\varepsilon_{x,q}=\varepsilon_0(M_qF_x+\beta_qzH_s),
\]

\[
\varepsilon_{y,q}=\varepsilon_0k^2(M_qF_y+\beta_qzH_s),
\]

\[
\gamma_q=2\varepsilon_0kc_Xc_Y(M_qH_s-\beta_qz),
\]

\[
\varepsilon_{x,\alpha}=\varepsilon_0A_x,\quad
\varepsilon_{y,\alpha}=\varepsilon_0A_y,\quad
\gamma_\alpha=-2\varepsilon_0kH_sc_Xc_Y.
\]

唯一非零二阶运动学项：

\[
\varepsilon_{x,qq}=\varepsilon_0M_{qq}F_x,
\]

\[
\varepsilon_{y,qq}=\varepsilon_0k^2M_{qq}F_y,
\]

\[
\gamma_{qq}=2\varepsilon_0kM_{qq}H_sc_Xc_Y.
\]

---

# 2. 从原始试件参数到控制代表半波

候选正交各向异性 SSSS 模态：

\[
w_j=W_j\sin(\pi x/b)\sin(j\pi y/a_{phys}).
\]

候选屈曲膜力：

\[
\boxed{N_{cr,j}=\pi^2\left[\frac{D_xa_{phys}^2}{j^2b^4}+\frac{2H}{b^2}+\frac{D_yj^2}{a_{phys}^2}\right].}
\]

\[
P_{cr,j}=bN_{cr,j}.
\]

连续最优：

\[
\boxed{j_0=\frac{a_{phys}}b\left(\frac{D_x}{D_y}\right)^{1/4}.}
\]

\[
\boxed{m_*=\arg\min_{j\in\mathbb N^+}P_{cr,j},\qquad \ell=a_{phys}/m_*,\qquad k=b/\ell.}
\]

整个非线性求解只在**一个连续完整代表半波**上进行；不得将重复半波复制为独立空间材料域。

## 2.1 Case21 前端从零

原始试件：

```text
a_phys = 2440 mm
b      = 1220 mm
t      = 19.30 mm
E0     = 20321 MPa
nu     = 0.18
A0     = b/400 = 3.05 mm
q0     = 0.0025
```

各向同性初始板刚度：

\[
\boxed{D_0=\frac{E_0t^3}{12(1-\nu^2)}=12\,581\,716.55789238\ \mathrm{Nmm}.}
\]

因此：

\[
\boxed{D_x=D_y=H=D_0.}
\]

候选：

```text
j=1: Pcr = 636.150436030 kN
j=2: Pcr = 407.136279059 kN
j=3: Pcr = 477.819660840 kN
j=4: Pcr = 636.150436030 kN
```

故：

\[
\boxed{m_*=2,\qquad \ell=1220\ \mathrm{mm},\qquad k=1.}
\]

注意：历史部分文件直接把 Case21 写成 `a=b=ell=1220 mm, m*=1`，那已经是代表半波坐标；本账本从真实 `a_phys=2440 mm` 起算，因此物理半波数为 2。

## 2.2 Z6 前端从零

原始试件：

```text
a_phys = 24000 mm
b      = 12000 mm
tc     = 122 mm
ts     = 4 mm each face
h      = tc + 2 ts = 130 mm
rho_w  = 0.02
fc     = 30.4 MPa
eps0   = 0.0018712490394580678
kappa  = 2.0005129533678754
Es     = 206000 MPa
mu_s^Z = 0.30
mu_c^Z = 0.20
A0     = a_phys/500 = 48 mm
q0     = 0.004
```

混凝土初始弹模：

\[
\boxed{E_c^0=\kappa f_c/\varepsilon_0=32500\ \mathrm{MPa}.}
\]

钢面中心距：

\[
z_f=t_c/2+t_s/2=63\ \mathrm{mm}.
\]

总钢面惯性矩和核心惯性矩：

\[
I_f=2b\left(\frac{t_s^3}{12}+t_sz_f^2\right)=381\,152\,000\ \mathrm{mm^4},
\]

\[
I_c=bt_c^3/12=1\,815\,848\,000\ \mathrm{mm^4}.
\]

按板宽归一的弯曲刚度：

\[
\boxed{D_x=\frac{E_sI_f+E_c^0I_c}{b}=11\,461\,031\,000\ \mathrm{Nmm}.}
\]

\[
D_{y,s}=\frac{E_sI_f+\rho_wE_sI_c}{b}=7\,166\,550\,480\ \mathrm{Nmm},
\]

\[
D_{y,c}=\frac{(1-\rho_w)E_c^0I_c}{b}=4\,819\,563\,233.333333\ \mathrm{Nmm},
\]

\[
\boxed{D_y=D_{y,s}+D_{y,c}=11\,986\,113\,713.333333\ \mathrm{Nmm}.}
\]

剪切模量：

\[
G_s^Z=\frac{E_s}{2(1+\mu_s^Z)}=79\,230.76923077\ \mathrm{MPa},
\]

\[
G_c^Z=\frac{E_c^0}{2(1+\mu_c^Z)}=13\,541.66666667\ \mathrm{MPa}.
\]

薄壁闭口钢箱：

\[
A_\Box=(b-t_s)(h-t_s)=1\,511\,496\ \mathrm{mm^2},
\]

\[
\oint ds/t_s=\frac{2[(b-t_s)+(h-t_s)]}{t_s}=6061.
\]

\[
D_t^{(s)}=\frac{4G_s^ZA_\Box^2}{b\oint ds/t_s}=9\,955\,024\,611.98533\ \mathrm{Nmm}.
\]

内核心矩形尺寸：

\[
b_i=b-2t_s=11992\ \mathrm{mm},\qquad h_i=h-2t_s=122\ \mathrm{mm}.
\]

本账本显式采用与冻结目标一致的经典矩形 Saint-Venant 形状因子：

\[
\boxed{\beta_{shape}=\frac13\left[1-0.63\frac{h_i}{b_i}+0.052\left(\frac{h_i}{b_i}\right)^5\right]=0.331196909052367.}
\]

于是：

\[
D_t^{(c)}=\frac{G_c^Z}{b}\beta_{shape}b_ih_i^3
=8\,138\,572\,939.95845\ \mathrm{Nmm},
\]

\[
\boxed{D_t=D_t^{(s)}+D_t^{(c)}=18\,093\,597\,551.94378\ \mathrm{Nmm}.}
\]

\[
D_{xy}=D_t/2=9\,046\,798\,775.97189\ \mathrm{Nmm}.
\]

\[
D_\mu=\mu_s^ZD_{y,s}+\mu_c^ZD_{y,c}=3\,113\,877\,790.66667\ \mathrm{Nmm},
\]

\[
\boxed{H=D_{xy}+D_\mu=12\,160\,676\,566.63856\ \mathrm{Nmm}.}
\]

候选：

```text
j=1: 60.173337674 MN
j=2: 39.288014715 MN
j=3: 46.373899413 MN
j=4: 61.792824754 MN
```

故：

\[
\boxed{m_*=2,\qquad \ell=12000\ \mathrm{mm},\qquad k=1.}
\]

---

# 3. 普通混凝土有限全局 R10 current operator

对任意连续点 `(X,Y,z)`，先构造：

\[
E_{11}=\frac{e_x+\nu e_y}{1-\nu^2},\qquad
E_{22}=\frac{\nu e_x+e_y}{1-\nu^2},\qquad
E_{12}=\frac{\gamma}{2(1+\nu)}.
\]

\[
\mathbf E=\begin{bmatrix}E_{11}&E_{12}\\E_{12}&E_{22}\end{bmatrix}.
\]

\[
\mu_E=(E_{11}+E_{22})/2,\quad d_E=(E_{11}-E_{22})/2,
\]

\[
r_E=\sqrt{d_E^2+E_{12}^2},\qquad \lambda_{1,2}=\mu_E\pm r_E.
\]

冻结材料常数：

\[
\kappa=2.0005129533678754,\quad \rho=0.1,
\]

\[
x_{cr}=\rho/\kappa=0.0499871794539743,
\]

\[
\eta=x_{cr}/20=0.0024993589726987125,
\]

\[
H_R=0.09799750427197301,\quad U_R=0.03,
\]

\[
a_{cc}=0.1072329249362415,\qquad a_t=1-2^{-1/8}.
\]

平滑 projector：

\[
\boxed{\Pi_\eta(z)=\frac{z^2(\sqrt{z^2+\eta^2}+z)}{2(z^2+\eta^2)}.}
\]

\[
c_i=\Pi_\eta(-\lambda_i),\qquad t_i=\Pi_\eta(\lambda_i).
\]

压缩：

\[
\boxed{C_i=\frac{\kappa c_i}{1+(\kappa-2)c_i+c_i^2}.}
\]

## 3.1 三段拉伸的单一全局有限 spline

令：

\[
r=t/x_{cr}.
\]

第一段基础多项式：

\[
p_1(r)=\rho r+(10H_R-6\rho)r^3+(8\rho-15H_R)r^4+(6H_R-3\rho)r^5.
\]

系数：

\[
A_3=4\rho-\frac{7300}{729}H_R+\frac{10}{729}U_R,
\]

\[
A_4=7\rho-\frac{32800}{2187}H_R-\frac{5}{2187}U_R,
\]

\[
A_5=3\rho-\frac{118100}{19683}H_R+\frac{2}{19683}U_R,
\]

\[
B_3=\frac{10(H_R-U_R)}{729},\quad
B_4=\frac{5(H_R-U_R)}{2187},\quad
B_5=\frac{2(H_R-U_R)}{19683}.
\]

\[
x_+=\frac12(x+\sqrt{x^2}).
\]

完整三段 R10 拉伸函数严格恒等为：

\[
\boxed{
\begin{aligned}
u_R(t)=\;&p_1(r)
+A_3(r-1)_+^3+A_4(r-1)_+^4+A_5(r-1)_+^5\\
&+B_3(r-10)_+^3+B_4(r-10)_+^4+B_5(r-10)_+^5.
\end{aligned}}
\]

定义：

\[
T_i=u_R(t_i)/\rho,
\]

\[
U_i=\kappa\lambda_i-C_i+\kappa c_i+u_R(t_i)-\kappa t_i.
\]

主应力：

\[
\boxed{s_1=U_1-a_{cc}C_1^2C_2+C_1T_2-\rho a_tT_1T_2^8,}
\]

\[
\boxed{s_2=U_2-a_{cc}C_2^2C_1+C_2T_1-\rho a_tT_2T_1^8.}
\]

谱返回：若 \(\lambda_1\ne\lambda_2\)，

\[
P_1=\frac{\mathbf E-\lambda_2\mathbf I}{\lambda_1-\lambda_2},\qquad P_2=\mathbf I-P_1,
\]

\[
\boxed{\mathbf S=s_1P_1+s_2P_2.}
\]

重复主值用连续极限。物理应力：

\[
\boxed{\boldsymbol\sigma_c=f_c[S_{xx},S_{yy},S_{xy}]^T.}
\]

## 3.2 同源 concrete tangent

禁止另拟合切线。对任意全局未知量 `g`：

\[
\boxed{d\mathbf S=L_{\mathcal M_{R10}}(\mathbf E)[d\mathbf E],}
\]

其中 Fréchet 导数由同一标量 functions 的导数和 divided differences 构造；在重复特征值处取连续极限。

工程实现可以等价地逐项用：

\[
\Pi_\eta'(z),\quad C'(c),\quad u_R'(t),\quad s_{i,j}
\]

构造同源 material tangent \(\mathbf D_t=\partial\boldsymbol\sigma/\partial\boldsymbol\varepsilon\)。

---

# 4. 结构广义函数的连续定义

对任一三维材料相 `p`，定义其真实连续体积域 \(V_p\)。

轴力：

\[
\boxed{P_p=-\frac1\ell\int_{V_p}\sigma_y^{(p)}\,dV.}
\]

总轴力：

\[
\boxed{P=\sum_pP_p.}
\]

对于 `g in {q,alpha}`，广义残量：

\[
\boxed{
R_g^{(p)}=\int_{V_p}
\left(
\sigma_x\varepsilon_{x,g}+\sigma_y\varepsilon_{y,g}+\tau_{xy}\gamma_{xy,g}
\right)dV.
}
\]

\[
\boxed{R_g=\sum_pR_g^{(p)}.}
\]

同源一阶导数，对 `g in {q,alpha}`, `h in {D,q,alpha}`：

\[
\boxed{
R_{g,h}^{(p)}=\int_{V_p}
\left[
\boldsymbol\varepsilon_{,g}^{T}\mathbf D_t^{(p)}\boldsymbol\varepsilon_{,h}
+\boldsymbol\sigma^{(p)T}\boldsymbol\varepsilon_{,gh}
\right]dV.
}
\]

除 `g=h=q` 外，第二项的运动学二阶导数均为零。

轴力导数：

\[
\boxed{P_{p,h}=-\frac1\ell\int_{V_p}\left(\mathbf e_y^T\mathbf D_t^{(p)}\boldsymbol\varepsilon_{,h}\right)dV,}
\]

其中 \(\mathbf e_y=[0,1,0]^T\)。

这些积分必须通过连续解析/标准函数后端处理；不得用空间离散近似。

---

# 5. Case21 材料相

## 5.1 混凝土

\[
V_c:\ 0\le x\le b,\ 0\le y\le\ell,\ -t/2\le z\le t/2.
\]

使用第 3 节有限全局 R10。

## 5.2 两方向钢筋

```text
rho_sx = rho_sy = 0.00375
zsx = zsy = 0
Es = 200000 MPa
fy = 530 MPa
```

已释放状态钢筋保持弹性，因此：

\[
\sigma_{s,x}=E_s\varepsilon_{s,x},\qquad
\sigma_{s,y}=E_s\varepsilon_{s,y}.
\]

Case21 `k=1, z_s=0` 的闭式结果：

\[
\boxed{P_s=\rho_{s,y}tbE_s\varepsilon_0\left(D-\frac M4\right).}
\]

令：

\[
C_R=\frac{\rho_sE_s\varepsilon_0^2b\ell t}{32\times1000}=2.94090386184375.
\]

则：

\[
\boxed{R_q^s=C_RM_q[8D(\nu-1)+9M-5\alpha],}
\]

\[
\boxed{R_\alpha^s=-C_R[8D\nu(\nu+1)+5M-(4\nu^2+5)\alpha].}
\]

其 Jacobian 由这些闭式直接解析求导。

---

# 6. Z6 材料相

Z6 采用四相：

```text
0.98 R10 concrete core
upper face steel
lower face steel
rho_w-equivalent longitudinal web/PBL steel
```

不得双计：web 占据的 2% 核心体积必须从混凝土扣除。

## 6.1 有效核心

\[
V_c:\ 0\le x\le b,\ 0\le y\le\ell,\ -61\le z\le61\ \mathrm{mm}.
\]

混凝土贡献整体乘 \((1-\rho_w)=0.98\)。

## 6.2 上下钢面有限 radial-cap

上下钢面厚度域：

\[
V_+:61\le z\le65\ \mathrm{mm},\qquad
V_-:-65\le z\le-61\ \mathrm{mm}.
\]

钢面试应力：

\[
\sigma_x^{tr}=\frac{E_s}{1-\nu_s^2}(\varepsilon_x+\nu_s\varepsilon_y),
\]

\[
\sigma_y^{tr}=\frac{E_s}{1-\nu_s^2}(\nu_s\varepsilon_x+\varepsilon_y),
\]

\[
\tau^{tr}=\frac{E_s}{2(1+\nu_s)}\gamma_{xy}.
\]

\[
\sigma_{VM}^{tr}=\sqrt{(\sigma_x^{tr})^2-\sigma_x^{tr}\sigma_y^{tr}+(\sigma_y^{tr})^2+3(\tau^{tr})^2}.
\]

\[
r=(\sigma_{VM}^{tr}/f_y)^2.
\]

R14 的单一有限全局 radial-cap：

\[
\boxed{g_f(r)=\frac{2}{1+\sqrt r+\sqrt{(\sqrt r-1)^2}}.}
\]

\[
\boxed{\boldsymbol\sigma_f=g_f(r)\boldsymbol\sigma^{tr}.}
\]

这与原 `r<=1 -> 1; r>1 -> r^{-1/2}` 严格恒等，无需空间弹塑区划分。

同源 tangent 由该同一有限函数链式求导；在 `r=1` 使用 source-consistent one-sided / semismooth derivative，stress 本身连续。

## 6.3 web/PBL 等效纵向钢相

web 仍占核心同一连续域，但体积权重为 \(\rho_w\)。只读取纵向应变：

\[
x=E_s\varepsilon_y^w.
\]

R14 全局有限 clip：

\[
\boxed{\sigma_y^w=\frac{\sqrt{(x+f_y)^2}-\sqrt{(x-f_y)^2}}{2}.}
\]

其同源 tangent：

\[
E_t^w=E_s\quad(|x|<f_y),\qquad E_t^w=0\quad(|x|>f_y),
\]

kink 处取 source-consistent semismooth 值。

轴力与残量：

\[
P_w=-\frac{\rho_w}{\ell}\int_{V_c}\sigma_y^w\,dV,
\]

\[
R_q^w=\rho_w\int_{V_c}\sigma_y^w\varepsilon_{y,q}\,dV,
\]

\[
R_\alpha^w=\rho_w\int_{V_c}\sigma_y^w\varepsilon_{y,\alpha}\,dV.
\]

Z6 总量：

\[
\boxed{P=0.98P_c^{full}+P_++P_-+P_w,}
\]

\[
\boxed{R_q=0.98R_q^c+R_q^++R_q^-+R_q^w,}
\]

\[
\boxed{R_\alpha=0.98R_\alpha^c+R_\alpha^++R_\alpha^-+R_\alpha^w.}
\]

---

# 7. 零离散连续积分后端合同

本账本不规定唯一特殊函数名称；只规定**积分对象和禁止事项**。

正式后端必须把第 4–6 节的连续积分精确地表示/评价为有限数学对象。允许的典型构造：

```text
elementary / Beta / Gamma
Carlson elliptic
Gauss / Appell / Lauricella
algebraic Abelian periods
GKZ / relative-incomplete A-hypergeometric
Mellin-Barnes
differential-system / holonomic representation
```

如果某一种表示不方便：

```text
CROSS OUT THAT REPRESENTATION
-> SWITCH TO ANOTHER EXACT MATURE REPRESENTATION
```

不得把表示困难升级成新的理论门禁，也不得回退到空间离散。

R13 的 sparse CH / master A* 可作为一种具体 exact-period 编译器，但不是唯一允许的 evaluator。

---

# 8. 从零直接极限求解算法

对每一试件：

1. 只用第 2 节原始输入计算 `Dx,Dy,H,m*,ell,k,q0`；
2. 建立第 1 节连续运动学；
3. 建立第 3/5/6 节有限 current material operators；
4. 用第 4/7 节生成连续精确 `P,Rq,Ralpha`；
5. 从同一 material operators 生成 `P_D,P_q,P_alpha` 和残量 Jacobian；
6. 直接求解

\[
\boxed{
F_{lim}(D,q,\alpha)=
\begin{bmatrix}
R_q\\R_\alpha\\\det J_{\lim}
\end{bmatrix}=0.
}
\]

求根器迭代是三变量有限维数学求根，不是空间离散。

禁止把下面的均匀分支条件作为 `Pu`：

\[
\boxed{\frac{dP(D,0,0)}{dD}=0\quad\text{NOT A PLATE LIMIT}.}
\]

多实根时，禁止按“最大 P”“最接近试验”“根序号”选择。物理根应满足：

```text
q >= 0
材料状态有限且 current operator 有定义
属于初始稳定状态所连接的物理平衡支
为该物理支第一个可达普通荷载极大事件
```

如必须确认连通性，只允许连续数学 homotopy/解析分支身份；不得用空间/材料离散。

---

# 9. Case21 BLIND INPUT BLOCK

```text
a_phys = 2440 mm
b = 1220 mm
t = 19.30 mm
A0 = 3.05 mm
fc = 21.23 MPa
E0 = 20321 MPa
eps0 = 0.00209
nu_c_R10 = 0.18
rho_sx = 0.00375
rho_sy = 0.00375
zsx = 0
zsy = 0
Es = 200000 MPa
fy = 530 MPa
kappa = 2.0005129533678754
rho_R = 0.1
HR = 0.09799750427197301
UR = 0.03
acc = 0.1072329249362415
at = 1 - 2^(-1/8)
```

盲算时到此为止，不读取第 11 节目标。

---

# 10. Z6 BLIND INPUT BLOCK

```text
a_phys = 24000 mm
b = 12000 mm
tc = 122 mm
ts_top = 4 mm
ts_bottom = 4 mm
rho_w = 0.02
A0 = 48 mm
fc = 30.4 MPa
eps0 = 0.0018712490394580678
nu_c_R10 = 0.18
kappa = 2.0005129533678754
rho_R = 0.1
HR = 0.09799750427197301
UR = 0.03
acc = 0.1072329249362415
at = 1 - 2^(-1/8)
Es = 206000 MPa
fy = 355 MPa
nu_s_face = 0.30
mu_s_Z_shell = 0.30
mu_c_Z_shell = 0.20
```

注意 namespace：

```text
nu_c_R10 = 0.18  -> nonlinear concrete current operator only
mu_c_Z_shell = 0.20 -> Zhou shell initial stiffness only
nu_s_face = 0.30 -> face steel plane-stress law
```

盲算时到此为止，不读取第 11 节目标。

---

# 11. SEALED REGRESSION TARGETS — 仅复算后对照

> 本节不得参与 blind solve、seed tuning、root selection 或参数调整。

## 11.1 Case21

```text
m_phys = 2
ell = 1220 mm
k = 1
q0 = 0.0025

Du = 0.7887924801
qu = 0.0018083572562965242
alphau = 0.002506908330448254
lambda_A,u = 0.08623596353826937

Mu = 0.02907033478365149
Bu = 0.06754686155676540

Pc = 337.92303037 kN
Ps = 28.844798318 kN
Pu = 366.7678286852115 kN

experiment = 368.3127497435694 kN
post-solve error = -0.419459 %
```

历史极限处钢筋残量对照：

```text
Rq_s = -294.703813363 kN mm
Ralpha_s = -4.331387968 kN mm
```

## 11.2 Z6

```text
m_phys = 2
ell = 12000 mm
k = 1
q0 = 0.004

Du = 1.36180798
qu = 0.0264854039
alphau = 1.8954326279510263
lambda_A,u = 0.786915819

Mu = 2.4086853792820073
Bu = 0.7101062648720707

Pc_full = 23.2827595918 MN
Pc_eff = 22.8171044 MN
Pface = 18.5564373 MN
Pw = 7.0325797 MN
Pu = 48.4061215 MN

Zhou = 49.4867667519 MN
post-solve error vs Zhou = -2.183706 %
Winter = 50.1858541295 MN
post-solve error vs Winter = -3.546283 %
```

---

# 12. 已明确废止的两组错误结果

以下只是错误诊断证据，不是任何 `Pu` 候选：

```text
Case21 q=alpha=0 uniform stationary = 538.273498279 kN
Z6     q=alpha=0 uniform stationary = 90.150438116 MN
```

原因：它们解的是材料/截面均匀分支峰值，关闭了 `q` 和 `alpha` 对应的结构稳定与膜内重分布机制。

---

# 13. R15 完整性声明

```text
SINGLE_FILE_RAW_INPUTS_CASE21 = COMPLETE
SINGLE_FILE_RAW_INPUTS_Z6 = COMPLETE
RAW_TO_HALFWAVE_CASE21 = COMPLETE
RAW_TO_HALFWAVE_Z6 = COMPLETE
NGUYEN_CONTINUOUS_KINEMATICS = COMPLETE
FINITE_GLOBAL_R10_CONCRETE = COMPLETE
FINITE_CASE21_REBAR = COMPLETE
FINITE_Z6_FACE_RADIAL_CAP = COMPLETE
FINITE_Z6_WEB_CLIP = COMPLETE
CONTINUOUS_P_RQ_RALPHA_DEFINITIONS = COMPLETE
SAME_SOURCE_JLIM_DEFINITION = COMPLETE
DIRECT_THREE_VARIABLE_LIMIT_SYSTEM = COMPLETE
ZERO_DISCRETIZATION_GOVERNANCE = COMPLETE
SEALED_REGRESSION_TARGETS = INCLUDED_BUT_NOT_SOLVE_INPUTS
```

本文件因此可作为下一轮独立 AI/CAS 的唯一理论输入账本。

但必须保持以下证据身份：

```text
R15 = COMPLETE FROM-ZERO CALCULATION SPECIFICATION
R15 != CLAIM THAT THIS CHAT HAS INDEPENDENTLY RECOMPUTED THE FULL NONUNIFORM ROOTS USING A NEW CAS BACKEND
```

真正的下一项执行验证是：给独立执行器只提供第 0–10 节，禁止读取第 11 节，在零离散条件下直接求得 Case21 或 Z6 的完整三元极限根；复算完成后再解封第 11 节做对照。
