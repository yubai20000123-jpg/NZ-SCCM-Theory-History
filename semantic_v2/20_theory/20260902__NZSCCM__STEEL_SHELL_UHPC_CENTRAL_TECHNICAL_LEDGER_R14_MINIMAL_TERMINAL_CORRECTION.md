# NZ-SCCM — 钢壳–UHPC 显式极限承载力集中技术总账 R14 — MINIMAL TERMINAL CORRECTION / FINAL TRANSFER

**Date:** 2026-09-02  
**Supersedes:** `STEEL_SHELL_UHPC_R13_FINAL_TRANSFER_AUDITED` only where R13 made axial lower-core compression contact a mandatory universal terminal.  
**Production main:** unchanged unless separately authorized.  
**Runtime dependence on historical markdown:** NONE.  
**Formal spatial quadrature:** 0.  
**Material-point grid:** 0.  
**Reference-result lookup in solve/root selection:** 0.

---

# 0. R14 的唯一理论修正

R14 **不重开** R13 的 A/D、Airy、R04、R02、R06、UHPC、web 或 section-resultant 公式。

R14 只修正 R13 的一个回退：R13 错误地把

\[
\varepsilon_y^{U,-}=-\varepsilon_{c0}
\]

固定成所有试件都必须同时满足的第五个终点方程。

R14 恢复已经在 2026-08-28 验证过的结构：

\[
\boxed{\mathbf R_4(\mathbf x;q)=0}
\]

其中

\[
\boxed{\mathbf x=(\varepsilon_x^0,\kappa_x,\varepsilon_y^0,\kappa_y)^T}
\]

并沿与

\[
q=0,\qquad \mathbf x=\mathbf0
\]

连续连通的主平衡支求解。

UHPC 压缩峰值、拉伸材料域边界等仍被监测，但它们是 **competing material-domain events**，不是预设的第五个平衡方程。

同时定义

\[
\boxed{J_4=\frac{\partial\mathbf R_4}{\partial\mathbf x}}
\]

并监测第一个 admissible structural tangent fold：

\[
\boxed{\det J_4=0.}
\]

当前 \(P_u\) 是在 `q=0` 连通主平衡支上首先到达的、当前 R14 已闭合的 admissible terminal 所对应的

\[
\boxed{P_u=P(q_u)}.
\]

这可以是当前材料域边界先到，也可以是 J4 fold 先到。

---

# 1. 适用范围与硬边界

R14 是矩形钢壳–UHPC 组合板轴压 current-state reduced theory。

当前闭合范围：

```text
one rectangular gross panel
x = transverse
y = axial
one continuous global sinusoidal family
positive integer longitudinal mode selected mechanically
zero imposed uniform engineering shear at terminal
independent generalized section strains/curvatures
one registered local steel-face cell Lx,Ly,A0_local
automatic R04/R06 steel-face event theory
scalar nonlinear UHPC continuous-thickness operator
longitudinal web steel area Aw smeared through core thickness
R4 connected equilibrium branch
competing material-domain terminal / J4 tangent-fold terminal
```

禁止作为正式力学：

```text
spatial Gauss/Simpson/adaptive quadrature
material-point grids
effective width/effective area
stored Pu lookup
FEM/test-based root selection
FEM/test-based material calibration
artificial B/H cutoff
artificial q cutoff as a physical terminal
mandatory universal -eps_c0 contact equation
```

---

# 2. 单位、坐标、符号

```text
force  N
length mm
stress MPa=N/mm²
strain dimensionless
```

\[
0\le x\le b,\qquad 0\le y\le a.
\]

\(z>0\) 指向 upper steel face。拉应变、拉应力为正。

\[
[N_x]=[N_y]=N/mm,\qquad [M_x]=[M_y]=N,\qquad [P]=N.
\]

---

# 3. 独立物理输入

几何：

\[
b,a,t_c,t_s,A_{0g},A_w,L_x,L_y,A_{0\ell}.
\]

钢：

\[
E_s,\nu_s,f_y.
\]

UHPC：

\[
E_c,\nu_c,f_c,\varepsilon_{c0}
\]

以及五个拉伸锚点

\[
(0,0),(\varepsilon_{t,cr},f_{t,cr}),(\varepsilon_{t,p},f_{t,p}),(\varepsilon_{t,l},f_{t,l}),(\varepsilon_{t,lim},0).
\]

必须：

\[
b,a,t_c,t_s,L_x,L_y,E_s,E_c,f_y,f_c,\varepsilon_{c0}>0,
\]

\[
A_{0g},A_{0\ell},A_w\ge0,\qquad -1<\nu_s,\nu_c<0.5.
\]

\[
\boxed{\rho_w=\frac{A_w}{bt_c}<1},\qquad \boxed{z_f=\frac{t_c+t_s}{2}}.
\]

当前代表性 UHPC 拉伸锚点保持 R13：

```text
0          0
0.000420   9.767718 MPa
0.003800  10.734818 MPa
0.006900  10.347978 MPa
0.007590   0
```

---

# 4. 初始 full-composite A/D —— R13 不变

\[
K_s=\frac{E_s}{1-\nu_s^2},\qquad K_c=\frac{E_c}{1-\nu_c^2},
\]

\[
G_s=\frac{E_s}{2(1+\nu_s)},\qquad G_c=\frac{E_c}{2(1+\nu_c)}.
\]

\[
A_{11}=2t_sK_s+(1-\rho_w)t_cK_c,
\]

\[
A_{22}=A_{11}+\rho_wt_cE_s,
\]

\[
A_{12}=2t_s\nu_sK_s+(1-\rho_w)t_c\nu_cK_c.
\]

\[
D_f=2K_s\left(\frac{t_s^3}{12}+t_sz_f^2\right),
\]

\[
D_c=(1-\rho_w)K_c\frac{t_c^3}{12},\qquad D_w=\rho_wE_s\frac{t_c^3}{12},
\]

\[
D_x=D_f+D_c,\qquad D_y=D_x+D_w,
\]

\[
D_\mu=\nu_sD_f+\nu_cD_c,
\]

\[
D_{66}=2G_s\left(\frac{t_s^3}{12}+t_sz_f^2\right)+(1-\rho_w)G_c\frac{t_c^3}{12},
\]

\[
\boxed{H=D_\mu+2D_{66}}.
\]

---

# 5. 全局整数模态与 Pcr —— R13 不变

\[
\alpha=\frac{\pi}{b},\qquad \beta_m=\frac{m\pi}{a}.
\]

\[
\boxed{m_c=\frac{a}{b}\left(\frac{D_x}{D_y}\right)^{1/4}}.
\]

只比较相邻正整数。

\[
N_{cr,m}=\frac{D_x\alpha^4+2H\alpha^2\beta_m^2+D_y\beta_m^4}{\beta_m^2},
\]

\[
\boxed{P_{cr,m}=bN_{cr,m}}.
\]

取严格最小者为 \(m^*\)。

---

# 6. Marguerre–Airy demand —— R13 不变

令

\[
\beta=\frac{m^*\pi}{a},\qquad \Delta_A=A_{11}A_{22}-A_{12}^2.
\]

\[
K_x=\frac{b^2\alpha^2}{8(A_{22}/\Delta_A)},
\]

\[
G=\frac{b^2\beta^2}{8(A_{11}/\Delta_A)},
\]

\[
C=\frac{b^3\Delta_A}{16\beta^2}\left(\frac{\alpha^4}{A_{22}}+\frac{\beta^4}{A_{11}}\right).
\]

\[
J_x=b(D_x\alpha^2+D_\mu\beta^2),\qquad J_y=b(D_\mu\alpha^2+D_y\beta^2).
\]

\[
q_0=\frac{A_{0g}}{b},\qquad Q=q(q+2q_0).
\]

\[
\boxed{P(q)=P_{cr}\frac{q}{q+q_0}+CQ}.
\]

\[
N_x^A=K_xQ,\qquad M_x^A=J_xq,
\]

\[
N_y^A=-\left[\frac{P(q)}b-GQ\right],\qquad M_y^A=J_yq.
\]

---

# 7. 截面广义变量 —— 只撤销 R13 的强制 contact 消元

R14 使用：

\[
\boxed{\varepsilon_x(z)=\varepsilon_x^0+\kappa_xz},\qquad
\boxed{\varepsilon_y(z)=\varepsilon_y^0+\kappa_yz}.
\]

upper/lower UHPC endpoints：

\[
\varepsilon_i^{U,\pm}=\varepsilon_i^0\pm\kappa_i\frac{t_c}{2}.
\]

upper/lower steel-face centroid strains：

\[
e_i^{s,\pm}=\varepsilon_i^0\pm\kappa_i z_f.
\]

**R14 不再设置**

\[
\varepsilon_y^{U,-}\equiv-\varepsilon_{c0}
\]

作为恒等约束。

\(\kappa_x,\kappa_y\) 仍是当前 R13/R12 截面平衡中的独立 generalized section curvatures；本次不重开另外的 `q -> kappa^g` 研究分支。

---

# 8. 钢面 R04 —— R13 不变

\[
Q_s=\frac{E_s}{1-\nu_s^2}.
\]

\[
\sigma_x^{tr}=Q_s(e_x+\nu_se_y),\qquad \sigma_y^{tr}=Q_s(e_y+\nu_se_x).
\]

当前 terminal shear 为零时：

\[
\sigma_{VM}^{tr}=\sqrt{(\sigma_x^{tr})^2-\sigma_x^{tr}\sigma_y^{tr}+(\sigma_y^{tr})^2}.
\]

\[
\boxed{\lambda_p=\min\left(1,\frac{f_y}{\sigma_{VM}^{tr}}\right)}.
\]

\[
\boldsymbol\sigma_s=\lambda_p\boldsymbol\sigma_s^{tr}.
\]

---

# 9. R04/R06 自动事件门 —— R13 不变

\[
r_c=\frac{L_y}{L_x},
\]

\[
k_{cr}=\frac{4(3r_c^4+2r_c^2+3)}{3r_c^2},
\]

\[
\boxed{\sigma_{cr,s}^E=\frac{\pi^2E_st_s^2}{12(1-\nu_s^2)L_x^2}k_{cr}}.
\]

若 \(\sigma_{cr,s}^E\ge f_y\) 则 `R04_YIELD_FIRST`，否则 `R06_LOCAL_FIRST`。不得按 specimen_id 人工选分支。

---

# 10. R02 local condensed amplitude —— R13 不变

\[
k_x=\frac{2\pi}{L_x},\qquad k_y=\frac{2\pi}{L_y},
\]

\[
c_x=\frac{3k_x^2}{8},\qquad c_y=\frac{3k_y^2}{8}.
\]

\[
d=U^2-A_{0\ell}^2,\qquad m_x=e_x+c_xd,\qquad m_y=e_y+c_yd.
\]

\[
K_b=D_s\left[\frac34(k_x^4+k_y^4)+\frac12k_x^2k_y^2\right].
\]

\[
B_3=4t_sE_sK_A+2t_sQ_s(c_x^2+2\nu_sc_xc_y+c_y^2),
\]

\[
B_1=K_b-A_{0\ell}^2B_3+2t_sQ_s(c_xe_x+\nu_sc_xe_y+\nu_sc_ye_x+c_ye_y),
\]

\[
B_0=-A_{0\ell}K_b.
\]

枚举

\[
B_3U^3+B_1U+B_0=0
\]

的全部非负实根，并加入 \(U=0\)。

\[
\Pi(U)=\frac{B_3}{4}U^4+\frac{B_1}{2}U^2+B_0U,
\]

\[
\boxed{U^*=\arg\min_{U\ge0}\Pi(U)}.
\]

---

# 11. R06 local field / first radial yield —— R13 不变

用 R13 冻结的 finite LL harmonics 构造

\[
\sigma_x(u,v),\quad\sigma_y(u,v),\quad\tau_{xy}(u,v),\qquad (u,v)\in[-1,1]^2.
\]

\[
\boxed{\Phi(u,v)=\sigma_x^2-\sigma_x\sigma_y+\sigma_y^2+3\tau_{xy}^2}.
\]

\(\Phi_{\max}\) 必须来自完整 finite candidate set：

```text
interior stationary roots
four edge stationary-root sets
four corners
```

不是空间网格。

对 radial factor：

\[
\mathbf e_f(\lambda)=\lambda\mathbf e_f.
\]

每个 \(\lambda\) 重新求 R02 \(U^*\)，再求 \(\Phi_{\max}\)。

\[
\Psi(\lambda)=\Phi_{\max}(\lambda)-f_y^2.
\]

若 \(\Psi(1)\le0\)，则 \(\lambda_y=1\)。否则

\[
\boxed{\lambda_y=\min\{\lambda\in(0,1]:\Psi(\lambda)=0\}}.
\]

R06 mean face stress：

\[
\boxed{\bar{\boldsymbol\sigma}^{R06}=\bar{\boldsymbol\sigma}^{R02}(\lambda_y\mathbf e_f)}.
\]

无 effective width。

---

# 12. UHPC scalar law / primitives —— R13 不变

\[
A_c=\frac{E_c\varepsilon_{c0}}{f_c},\qquad B_c=6-5A_c,\qquad C_c=4A_c-5.
\]

\[
\xi=-\frac{\varepsilon}{\varepsilon_{c0}}.
\]

当前已冻结压缩域：

\[
-\varepsilon_{c0}\le\varepsilon\le0.
\]

\[
\boxed{\sigma_c=-f_c(A_c\xi+B_c\xi^5+C_c\xi^6)}.
\]

拉伸使用五锚点 PCHIP/Hermite slopes 和四段 cubic-Hermite。

定义原函数：

\[
F_0'(\varepsilon)=\sigma(\varepsilon),\qquad F_1'(\varepsilon)=\varepsilon\sigma(\varepsilon).
\]

对任一方向 \(i\)：

\[
N_i^U=(1-\rho_w)\frac{F_0(\varepsilon_i^+)-F_0(\varepsilon_i^-)}{\kappa_i},
\]

\[
M_i^U=(1-\rho_w)\frac{F_1(\varepsilon_i^+)-F_1(\varepsilon_i^-)-\varepsilon_i^0[F_0(\varepsilon_i^+)-F_0(\varepsilon_i^-)]}{\kappa_i^2},
\]

并采用 \(\kappa_i\to0\) 的解析极限。

---

# 13. longitudinal web —— R13 不变

\[
\varepsilon_y^w(z)=\varepsilon_y^0+\kappa_yz.
\]

\[
\sigma_y^w=\operatorname{clip}(E_s\varepsilon_y^w,-f_y,+f_y).
\]

若 \(\varepsilon_y^w=\pm f_y/E_s\) 在厚度内出现，严格在这些解析 crossing 处分段积分，得到 \(N_y^w,M_y^w\)。

---

# 14. 总截面 resultants —— R13 不变

\[
N_x=N_x^U+t_s(\sigma_x^++\sigma_x^-),
\]

\[
M_x=M_x^U+t_sz_f(\sigma_x^+-\sigma_x^-),
\]

\[
N_y=N_y^U+t_s(\sigma_y^++\sigma_y^-)+N_y^w,
\]

\[
M_y=M_y^U+t_sz_f(\sigma_y^+-\sigma_y^-)+M_y^w.
\]

---

# 15. 正式四平衡 —— R14 修正后的核心闭合

对给定 \(q\)：

\[
\boxed{R_1=N_x-N_x^A(q)=0},
\]

\[
\boxed{R_2=M_x-M_x^A(q)=0},
\]

\[
\boxed{R_3=N_y-N_y^A(q)=0},
\]

\[
\boxed{R_4=M_y-M_y^A(q)=0}.
\]

写成

\[
\boxed{\mathbf R_4(\mathbf x;q)=\mathbf0}.
\]

这四个方程是理论闭合。数值 Newton/root 只是这些非线性代数方程的 evaluator；不是材料历史积分，也不是结构加载步理论。

---

# 16. 主平衡支身份

正式物理支由

\[
q=0,\qquad\mathbf x=\mathbf0
\]

出发。对增加的 \(q\)，每个当前状态都重新求

\[
\mathbf R_4(\mathbf x;q)=0.
\]

continuation 的唯一理论身份：

\[
\boxed{\text{识别与 unloaded state 连续连通的代数根支}}
\]

而不是 material history / load-step constitutive update / spatial marching。不得用“哪个根更接近 FEM/试验”决定 branch identity。

---

# 17. Competing material-domain events

当前 R13/R14 UHPC 压缩函数只冻结到 \(\varepsilon=-\varepsilon_{c0}\)。因此定义四个压缩裕量：

\[
g_{c,i}^{\pm}=\varepsilon_i^{U,\pm}+\varepsilon_{c0}.
\]

当前允许：

\[
\boxed{g_{c,i}^{\pm}\ge0}.
\]

拉伸端定义：

\[
g_{t,i}^{\pm}=\varepsilon_{t,lim}-\varepsilon_i^{U,\pm}\ge0.
\]

当某个材料域边界首先到达零时，它是当前已冻结 material operator 的 domain terminal。

**关键：**

\[
g_{c,y}^{-}=0
\]

只是这些事件之一；R14 不再把它预设成 universal terminal。

---

# 18. J4 structural tangent fold

在平衡支上：

\[
\boxed{J_4=\frac{\partial\mathbf R_4}{\partial(\varepsilon_x^0,\kappa_x,\varepsilon_y^0,\kappa_y)}}.
\]

structural fold：

\[
\boxed{\det J_4=0}.
\]

更稳健的正式 augmented form：

\[
\boxed{\mathbf R_4=0},\qquad
\boxed{J_4\mathbf v=\mathbf0},\qquad
\boxed{\mathbf v^T\mathbf v=1}.
\]

这给出 \(4+4+1=9\) 个方程，对 \((q,\mathbf x,\mathbf v)\) 九个未知量。必须同时检查该 fold 的全部材料域、R04/R06 和 R02/R06 active-set admissibility。

---

# 19. 最终 Pu 规则

沿 `q=0` 连通主平衡支，按 q 增加的物理次序监测：

1. R04/R06 内部事件；
2. UHPC/current-material domain boundary；
3. J4 fold；
4. 其他当前明确冻结的 admissibility 边界。

R04/R06 内部 steel events 通常只更新 current face operator，并不自动结束整体支。

最终：

\[
\boxed{q_u=\text{first positive q of the first admissible closed terminal}}
\]

\[
\boxed{P_u=P(q_u)}.
\]

不存在 universal \(q_u=\min\{\text{compression-contact roots}\}\)，也不存在人为 \(B/H\) 上限。

---

# 20. 人工 / Excel 求解身份

对一个给定 q：

1. 猜 \(\mathbf x\)；
2. 计算四个 R4 残量；
3. 对四个 generalized section variables 分别做小扰动；
4. 形成 4×4 数值 Jacobian；
5. 解 \(J_4\Delta\mathbf x=-\mathbf R_4\)；
6. 全步若变差，用 \(1/2,1/4,1/8\) 阻尼；
7. 收敛到该 q 的平衡点。

随后略增 q，以前一平衡点作首猜。

这叫

\[
\boxed{\text{finite-dimensional nonlinear equilibrium inversion / branch continuation}}
\]

不是被禁止的空间离散或材料历史 stepping。

fold 附近通过 `det(J4)`、smallest singular value，或正式 `R4 + J4 v + normalization` 精化。

---

# 21. R06 内部人工求根身份

R06 的 \(\lambda,u,v\) 仍是某一当前 steel-face operator 内部数学变量。它们不升级成外层结构状态。边界 \(u,v=\pm1\) 是完整 \(\Phi\) 极值问题的定义域边界，不是人工 topology 分类。

---

# 22. Standalone implementation sequence

新 AI / 人类计算者只拿本文件时按以下顺序：

```text
01  read units/signs
02  read raw geometry/material inputs
03  run input gates
04  compute rho_w,zf
05  construct initial A/D
06  compute continuous m_c
07  compare adjacent positive integers -> m*
08  compute Pcr,Kx,G,C,Jx,Jy
09  establish q=0, x=0 branch origin
10  choose a positive q trial
11  solve four equations R4(x;q)=0
12  for every steel face evaluate automatic R04/R06
13  if R06: solve R02 all nonnegative roots + minimum energy U*
14  construct full finite local field
15  obtain Phi_max from interior/edge/corner candidate set
16  solve first radial local-yield lambda if required
17  evaluate UHPC exact primitives
18  evaluate web exact yield-crossing integrals
19  assemble Nx,Mx,Ny,My
20  verify four R4 residuals
21  verify all material-domain margins
22  compute/estimate J4
23  continue the same connected branch to next q
24  record internal R06 events but do not make them automatic global terminals
25  if a material-domain margin reaches zero first, refine R4+g=0
26  if J4 becomes singular first, refine R4+J4 v=0+vTv=1
27  choose the first admissible closed terminal on the connected branch
28  report q_u and Pu=P(q_u)
29  output full audit state
```

---

# 23. 必须输出的 audit state

至少：

```text
raw inputs
rho_w,zf
A11,A22,A12
Dx,Dy,Dmu,D66,H
mc,m1,m2,m*
Pcr,Kx,G,C,Jx,Jy
q and branch-connection record
epsx0,kappax,epsy0,kappay
four UHPC endpoint strains
upper/lower steel centroid strains
R04/R06 branch
R02 B3,B1,B0 and selected U*
R06 lambda,u,v and Phi_max
UHPC Nx,Mx,Ny,My
web Ny,My
total Nx,Mx,Ny,My
Airy NxA,MxA,NyA,MyA
four raw/scaled residuals
J4 determinant / smallest singular value or null vector
all compression/tension domain margins
terminal type
q_u
Pu
```

---

# 24. R13 → R14 逐项变更门禁

| 层 | R14 相对 R13 |
|---|---|
| raw inputs | unchanged |
| A/D | unchanged |
| integer mode | unchanged |
| Airy P(q) | unchanged |
| R04 | unchanged |
| R02 | unchanged |
| R06 | unchanged |
| UHPC compression/tension | unchanged |
| UHPC F0/F1 | unchanged |
| web | unchanged |
| section N/M | unchanged |
| generalized section variables | restored to full four-variable R4 state |
| mandatory `eps_y^-=-eps_c0` | **removed** |
| `-eps_c0` identity | retained only as material-domain event |
| terminal selection | **first admissible terminal on connected R4 branch** |
| J4 fold | **restored as formal structural terminal candidate** |
| artificial B/H cutoff | prohibited |

因此：

\[
\boxed{\text{R14 是 terminal/closure 的最小修正，不是新材料或新局部屈曲理论。}}
\]
