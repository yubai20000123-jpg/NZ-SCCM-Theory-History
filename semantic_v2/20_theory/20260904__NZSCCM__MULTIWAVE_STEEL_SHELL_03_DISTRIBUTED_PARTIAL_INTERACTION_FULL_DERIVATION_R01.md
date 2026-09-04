# NZ-SCCM 多波钢壳03——考虑剪切滑移的单半波分布式部分组合凝聚版本 R01

**Date:** 2026-09-04  
**Branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Status:** `DIAGNOSTIC THEORY / SINGLE-HARMONIC DISTRIBUTED PARTIAL INTERACTION / STATIC CONDENSATION / NOT PRODUCTION R14`  
**Parent-1:** `20260903__NZSCCM__MULTIWAVE_STEEL_SHELL_01_NO_SHEAR_SLIP_FULL_DERIVATION_R01.md`  
**Parent-2:** `20260903__NZSCCM__MULTIWAVE_STEEL_SHELL_02_FIXED_RIB_SLIP_STIFFNESS_R01.md`

---

## 0. 为什么建立03

02证明“有限钢-UHPC纵向剪切传递”是一个值得保留的机制，但02把所有纵向PBL/肋合并为一个集中弹簧，并用

\[
\gamma=\frac{K_P}{K_P+K_{eq}}
\]

直接缩放钢面曲率应变。复检发现这一做法存在四个内部不一致：

1. PBL剪切传递本质沿纵向分布，02的集中式 `gamma` 丢失波长效应；
2. 02用“半个UHPC”定义轴向刚度，却仍以整个UHPC中面距离 `z_f` 做杠杆臂；
3. 02只修改钢面当前纵向应变，UHPC没有同源滑移场；
4. 02外层 `D_y,D_mu,Pcr,J_y` 仍采用完全组合刚度，而截面内层已经采用部分组合。

03只修正上述partial-interaction层，不重新打开01的R02/R06材料和多波逻辑。

同时修正01/02遗留的边缘格室问题：任何真实格室（包括非标准边缘格室）都必须经过相同的 `sigma_cr^E` vs `f_y` 门，禁止默认把全部边缘宽度归入E分支。

---

## 1. 03保留与不保留的内容

### 1.1 保留

- 一个完整整体半波作为正式代表域；
- `n0=floor(L_G/s)`；
- 等宽相邻标准格室采用 `n0-1,n0,n0+1` 的低阶多波分类；
- R02局部幅值三次方程；
- R06有限七谐波首次局部屈服门；
- 完整钢厚度，不使用有效宽度/有效面积；
- UHPC与web原有解析厚度积分；
- 原四个截面平衡 `R4=0`；
- FEM不参与参数反标、选根或终点选取。

### 1.2 修改

- 02的集中式 `gamma` 被删除；
- 以TOP钢面 / 连续UHPC+web核心 / BOTTOM钢面三层体系建立纵向分布式滑移；
- 每个整体候选半波数 `m` 都重新凝聚出其自己的 `Dx(m),Dy(m),Dmu(m)`；
- 选模、Pcr、Jx/Jy和当前截面使用同一套partial-interaction operator；
- TOP/BOTTOM边缘格室按实际宽度重新检查局部屈曲门。

### 1.3 当前仍不升级的参数

按用户要求，03暂时保持02的数值：

\[
\boxed{K_r^{\Sigma}=75.835\ \mathrm{kN/mm/rib}}
\]

但重新明确其身份：它只是“每条完整纵向肋的总等效连接刚度尺度”的诊断参数，不是已经来源锁定的PBL实测抗剪刚度。03的目的首先是消除02中“刚度怎样嵌入”的理论错误，而不是用FEM重新调这个数值。

---

# 2. 坐标与基本截面量

UHPC中面为 `z=0`，上、下钢面中面：

\[
z_+=+z_f,\qquad z_-=-z_f,
\]

\[
\boxed{z_f=\frac{t_c+t_s}{2}}.
\]

钢材平面应力模量：

\[
\boxed{Q_s=\frac{E_s}{1-\nu_s^2}}.
\]

UHPC初始平面应力模量：

\[
\boxed{Q_c=\frac{E_c}{1-\nu_c^2}}.
\]

纵向PBL/web占core面积率：

\[
\boxed{\rho_w=\frac{A_w}{bt_c}}.
\]

一个钢面的纵向膜刚度（全宽）：

\[
\boxed{A_s=Q_sbt_s}.
\]

把UHPC连续核心和已有纵向web作为同一个中心轴向phase，其初始纵向膜刚度为

\[
\boxed{A_c=Q_c(1-\rho_w)bt_c+E_sA_w}.
\]

这里 `A_c` 只用于partial-interaction凝聚；web在最终截面合力中仍按原R14/01公式单独积分，避免重复计力。

---

# 3. 把固定单肋总刚度变成纵向分布刚度

03不再把 `N_r K_r` 作为作用在一个点上的集中弹簧。

若物理构件纵向长度为 `a`，定义每条完整纵向肋的均布等效线刚度

\[
\boxed{k_r=\frac{K_r^{\Sigma}}{a}}
\]

其单位为 `N/mm^2`（因为单位长度剪流 `q=k_r s` 的单位为N/mm）。

TOP、BOTTOM分别有 `N_r^+`,`N_r^-` 条纵向肋，因此

\[
\boxed{k_+=\frac{N_r^+K_r^{\Sigma}}{a}},
\qquad
\boxed{k_-=\frac{N_r^-K_r^{\Sigma}}{a}}.
\]

注意：这是“保持02数值不变而修正其分布拓扑”的诊断解释。后续source-lock若证明 `K_r` 应按单孔及孔距构造，则只需替换 `k_+,k_-` 的来源，下面的凝聚方程无需改变。

---

# 4. 一个整体候选半波的三层滑移场

对任意整体候选纵向半波数 `m`：

\[
\boxed{\beta_m=\frac{m\pi}{a}}.
\]

整体曲率按同一谐波：

\[
\kappa_y(y)=\kappa_y^a\sin(\beta_my),
\qquad
\kappa_x(y)=\kappa_x^a\sin(\beta_my).
\]

TOP钢面、核心、BOTTOM钢面各增加一个纵向附加位移谐波：

\[
r_+(y)=R_+\cos(\beta_my),
\]
\[
r_c(y)=R_c\cos(\beta_my),
\]
\[
r_-(y)=R_-\cos(\beta_my).
\]

所以

\[
r_i'(y)=-\beta_mR_i\sin(\beta_my).
\]

界面相对滑移为

\[
\boxed{s_+(y)=r_+(y)-r_c(y)},
\]
\[
\boxed{s_-(y)=r_-(y)-r_c(y)}.
\]

这样TOP和BOTTOM共享同一个核心位移 `r_c`，不再把核心人为劈成两个彼此独立的“半UHPC”。

---

# 5. 为什么钢面滑移受 `kappa_y + nu_s kappa_x` 驱动

钢面plane-stress能量密度包含

\[
\frac12Q_s(\varepsilon_x^2+\varepsilon_y^2+2\nu_s\varepsilon_x\varepsilon_y).
\]

对钢面的纵向附加应变 `r_i'` 变分时，出现

\[
\varepsilon_y+\nu_s\varepsilon_x.
\]

因此定义

\[
\boxed{\chi=\kappa_y^a+\nu_s\kappa_x^a}.
\]

TOP基准曲率项为 `+z_f chi`，BOTTOM为 `-z_f chi`。

---

# 6. 三层partial-interaction势能

去掉与 `R_+,R_c,R_-` 无关的常数项后，一个完整物理长度上的附加势能为

\[
\begin{aligned}
\Pi_{PI}={}&\frac12\int_0^a A_s\left[r_+'(y)^2+2z_f\chi\sin(\beta y)r_+'(y)\right]dy\\
&+\frac12\int_0^a A_c r_c'(y)^2dy\\
&+\frac12\int_0^a A_s\left[r_-'(y)^2-2z_f\chi\sin(\beta y)r_-'(y)\right]dy\\
&+\frac12\int_0^a k_+[r_+(y)-r_c(y)]^2dy\\
&+\frac12\int_0^a k_-[r_-(y)-r_c(y)]^2dy.
\end{aligned}
\]

利用

\[
\int_0^a\sin^2(\beta y)dy=\int_0^a\cos^2(\beta y)dy=\frac a2,
\]

可精确写成

\[
\boxed{
\Pi_{PI}=\frac a4\left(\mathbf R^T\mathbf K_m\mathbf R-2F\mathbf v^T\mathbf R\right)
}
\]

其中

\[
\mathbf R=\begin{bmatrix}R_+\\R_c\\R_-\end{bmatrix},
\qquad
\mathbf v=\begin{bmatrix}1\\0\\-1\end{bmatrix},
\]

\[
\boxed{F=A_s\beta z_f\chi},
\]

且

\[
\boxed{
\mathbf K_m=
\begin{bmatrix}
A_s\beta^2+k_+&-k_+&0\\
-k_+&A_c\beta^2+k_++k_-&-k_-\\
0&-k_-&A_s\beta^2+k_-
\end{bmatrix}.
}
\]

驻值给出

\[
\boxed{\mathbf K_m\mathbf R=F\mathbf v}.
\]

这就是03取代02集中式 `gamma` 的核心方程。

---

# 7. 不隐藏3×3逆矩阵：逐式显式求解

定义

\[
a_s=A_s\beta^2+k_+,
\]
\[
d_s=A_s\beta^2+k_-,
\]
\[
c_s=A_c\beta^2+k_++k_-.
\]

再定义

\[
\boxed{H_c=c_s-\frac{k_+^2}{a_s}-\frac{k_-^2}{d_s}}.
\]

由第一、三式

\[
R_+=\frac{F+k_+R_c}{a_s},
\]
\[
R_-=\frac{-F+k_-R_c}{d_s}.
\]

代入核心方程可得

\[
\boxed{
R_c=F\frac{k_+/a_s-k_-/d_s}{H_c}
}.
\]

最终

\[
\boxed{R_+=\frac{F+k_+R_c}{a_s}},
\qquad
\boxed{R_-=\frac{-F+k_-R_c}{d_s}}.
\]

如果 `k_+=k_-`，自动有 `R_c=0`，满足上下对称性。

---

# 8. 控制截面的03当前应变

令 `R_i=F R_i^(1)`，其中 `R_i^(1)` 是单位F解。定义三个长度量

\[
\boxed{h_i=-\beta A_s\beta z_f R_i^{(1)}}.
\]

即

\[
h_+=-A_s\beta^2z_fR_+^{(1)},
\]
\[
h_c=-A_s\beta^2z_fR_c^{(1)},
\]
\[
h_-=-A_s\beta^2z_fR_-^{(1)}.
\]

在整体半波控制截面 `sin(beta y)=1`：

TOP钢面：

\[
\boxed{
\varepsilon_{y,s}^{+}
=\varepsilon_y^0+z_f\kappa_y+h_+(\kappa_y+\nu_s\kappa_x)
}
\]

BOTTOM钢面：

\[
\boxed{
\varepsilon_{y,s}^{-}
=\varepsilon_y^0-z_f\kappa_y+h_-(\kappa_y+\nu_s\kappa_x)
}
\]

核心：

\[
\boxed{
\varepsilon_y^U(z)
=\varepsilon_y^0+h_c(\kappa_y+\nu_s\kappa_x)+z\kappa_y
}
\]

web使用同一个core offset `h_c(κ_y+ν_sκ_x)`。

横向应变保持01：

\[
\boxed{\varepsilon_{x,s}^{\pm}=\varepsilon_x^0\pm z_f\kappa_x},
\]
\[
\boxed{\varepsilon_x^U(z)=\varepsilon_x^0+z\kappa_x}.
\]

因此03同时修改钢面和core的纵向相容，不再出现02“只改钢、不改UHPC”的不一致。

---

# 9. 三层静力凝聚产生同源整体弯曲刚度

令单位F解为

\[
R_c^{(1)}=\frac{k_+/a_s-k_-/d_s}{H_c},
\]
\[
R_+^{(1)}=\frac{1+k_+R_c^{(1)}}{a_s},
\]
\[
R_-^{(1)}=\frac{-1+k_-R_c^{(1)}}{d_s}.
\]

则

\[
\boxed{\Psi_m=\mathbf v^T\mathbf K_m^{-1}\mathbf v
=R_+^{(1)}-R_-^{(1)}}.
\]

静力凝聚后相对于完全组合弯曲能量的释放量为

\[
\boxed{
\Delta D_m=\frac{(A_s\beta_m z_f)^2}{b}\Psi_m
}.
\]

因为释放项乘的是

\[
(\kappa_y+\nu_s\kappa_x)^2,
\]

所以若01完全组合初始弯曲参数为 `Dx^FC,Dy^FC,Dmu^FC`，03每一个m分别使用

\[
\boxed{D_x^{(m)}=D_x^{FC}-\nu_s^2\Delta D_m},
\]
\[
\boxed{D_\mu^{(m)}=D_\mu^{FC}-\nu_s\Delta D_m},
\]
\[
\boxed{D_y^{(m)}=D_y^{FC}-\Delta D_m}.
\]

03-R01保留 `D66` 不变。原因是本版本只允许沿y且横向均匀的滑移谐波；若要释放扭转刚度，需要引入x相关滑移场，超出03-R01边界。

---

# 10. 整体选模必须对每个m重新凝聚

横向整体波数

\[
\alpha=\frac\pi b.
\]

（程序实际使用 `alpha=pi/b`。）

对每个正整数m：

\[
\beta_m=\frac{m\pi}{a},
\]

先由第6~9节算出 `Dx(m),Dy(m),Dmu(m)`，再定义

\[
H_m=D_\mu^{(m)}+2D_{66}.
\]

临界膜力

\[
\boxed{
N_{cr,m}=\frac{D_x^{(m)}\alpha^4+2H_m\alpha^2\beta_m^2+D_y^{(m)}\beta_m^4}{\beta_m^2}
}
\]

\[
\boxed{P_{cr,m}=bN_{cr,m}}.
\]

取

\[
\boxed{m^*=\arg\min_m P_{cr,m}}.
\]

然后

\[
\boxed{L_G=\frac a{m^*}}.
\]

这一步消除了02“内层部分组合、外层完全组合”的矛盾。

---

# 11. A矩阵为什么不改

03只释放由整体曲率引起的反对称/弯曲型纵向相对变形。均匀预压的平均端位移仍共同给定，且滑移谐波的导数在完整半波上平均为零。

因此R01保留01的

\[
A_{11},A_{22},A_{12}.
\]

已有全长partial-interaction解析核也表明：在共同端位移下，相位平均的钢/UHPC轴力分配本身不由连接刚度直接改变；连接刚度主要改变滑移、界面剪流、局部轴力振荡和凝聚切线。因此03不再对gross mean steel stress额外乘任何 `gamma`。

---

# 12. 外层Airy参数

选定 `m*` 后，使用同一 `beta=beta_m*` 和同一凝聚后的 `Dx*,Dy*,Dmu*`：

\[
\Delta_A=A_{11}A_{22}-A_{12}^2,
\]

\[
K_x=\frac{b^2\alpha^2\Delta_A}{8A_{22}},
\]

\[
G=\frac{b^2\beta^2\Delta_A}{8A_{11}},
\]

\[
C=\frac{b^3\Delta_A}{16\beta^2}
\left(\frac{\alpha^4}{A_{22}}+\frac{\beta^4}{A_{11}}\right),
\]

\[
\boxed{J_x=b(D_x^*\alpha^2+D_\mu^*\beta^2)},
\]

\[
\boxed{J_y=b(D_\mu^*\alpha^2+D_y^*\beta^2)}.
\]

`Pcr`必须使用第10节的03值。

然后

\[
Q=q(q+2q_0),
\]

\[
P(q)=P_{cr}\frac{q}{q+q_0}+CQ,
\]

\[
N_x^A=K_xQ,
\quad M_x^A=J_xq,
\]

\[
N_y^A=-\left[\frac{P(q)}b-GQ\right],
\quad M_y^A=J_yq.
\]

---

# 13. 标准格室与边缘格室全部进入同一局部门

每张钢面有 `N_r^f` 条纵向PBL线，则标准内部格室数

\[
\boxed{J_f=N_r^f-1}.
\]

标准格室宽度为 `s`，剩余总边缘宽度

\[
\boxed{b_{res}=b-J_fs}.
\]

左右对称边缘格室各取

\[
\boxed{b_e=\frac{b_{res}}2}.
\]

标准等宽格室：

\[
n_0=\left\lfloor\frac{L_G}{s}\right\rfloor
\]

并使用 `n0-1,n0,n0+1` 的相邻分类。对多于4个标准格室，采用平衡循环 `n0-1,n0,n0+1,n0,...`，只影响同类数量，不赋予额外局部未知量。

非标准边缘格室不满足“与标准格室等宽”的前提，因此不强加标准格室的±1关系；每个边缘格室按自己的

\[
\boxed{n_{0,e}=\left\lfloor\frac{L_G}{b_e}\right\rfloor}
\]

作为参考局部波数。

所有格室无一例外计算

\[
\sigma_{cr}^E
=
\frac{\pi^2E_st_s^2}{12(1-\nu_s^2)L_x^2}k_{cr}.
\]

若 `sigma_cr^E >= fy`，进入完整厚度ideal-EP/yield-first；否则进入R02/R06 local-first。

这样从03开始不再存在“TOP边缘32.5%宽度自动被保护成E”的规则。

---

# 14. 局部R02/R06本体保持01

对任一实际格室 `Lx`、局部纵向波数n：

\[
L_y=\frac{L_G}{n},
\quad k_x=\frac{2\pi}{L_x},
\quad k_y=\frac{2\pi n}{L_G}.
\]

形函数仍为

\[
\phi=(1-\cos k_x\xi)(1-\cos k_yy).
\]

`c_x,c_y,K_b,K_A,B3,B1,B0`、三次方程、能量选根及R06七谐波完全沿用01。

03只把其输入钢面宏观应变换成第8节的 `eps_x,s^±`,`eps_y,s^±`。

术语从本版本起更正：R06后段称为

`FIRST-LOCAL-YIELD CAPPED REDUCED OPERATOR`

而不再声称它是完整J2理想弹塑性屈后演化。

---

# 15. 局部R02几何缩短与PBL滑移的次级解析核

R02局部大挠度产生的x平均纵向几何失配可写成

\[
\bar g_y(y)=c_yd[1-\cos(2k_yy)],
\quad d=U^2-A_0^2.
\]

其波动项与既有exact partial-interaction harmonic kernel完全相容。对

\[
s=S_n\sin(n\pi y/L),\quad g=g_n\cos(n\pi y/L),
\]

有

\[
\Lambda=\frac{k_PL^2}{K_{eq}},
\]

\[
S_n=-\frac{g_nn\pi L}{n^2\pi^2+\Lambda},
\]

\[
\eta_n=\frac{\Lambda}{n^2\pi^2+\Lambda}.
\]

但是共同端位移下，这个局部谐波连接刚度不直接改变相位平均轴力分配。因此03-R01不把gross R02 mean stress再乘一个滑移系数，避免重复折减。局部滑移导致的剪流/轴力振荡可作为后续R06局部应力修正模块；在真实每个格室应分配多少相邻PBL线刚度source-lock之前，不偷偷加入Pu主算子。

---

# 16. 钢壳、UHPC、web截面结果量

所有实际格室按真实宽度面积加权得到

\[
\bar\sigma_x^+,\bar\sigma_y^+,\bar\sigma_x^-,\bar\sigma_y^-.
\]

钢壳：

\[
N_x^s=t_s(\bar\sigma_x^++\bar\sigma_x^-),
\]
\[
M_x^s=t_sz_f(\bar\sigma_x^+-\bar\sigma_x^-),
\]
\[
N_y^s=t_s(\bar\sigma_y^++\bar\sigma_y^-),
\]
\[
M_y^s=t_sz_f(\bar\sigma_y^+-\bar\sigma_y^-).
\]

UHPC横向仍为

\[
\varepsilon_x^U(z)=\varepsilon_x^0+z\kappa_x.
\]

纵向使用

\[
\varepsilon_y^U(z)=\varepsilon_y^0+\delta_c+z\kappa_y,
\]

其中

\[
\boxed{\delta_c=h_c(\kappa_y+\nu_s\kappa_x)}.
\]

把 `eps_y0` 在原01的 `F0/F1` 厚度积分式中替换为 `eps_y0+delta_c` 即得 `Ny^U,My^U`。web同样使用这个core offset。

---

# 17. 最终R4不增加外层未知量

给定q，仍解

\[
R_{N_x}=N_x^U+N_x^s-N_x^A=0,
\]
\[
R_{M_x}=M_x^U+M_x^s-M_x^A=0,
\]
\[
R_{N_y}=N_y^U+N_y^s+N_y^w-N_y^A=0,
\]
\[
R_{M_y}=M_y^U+M_y^s+M_y^w-M_y^A=0.
\]

外层未知量仍只有

\[
\varepsilon_x^0,\kappa_x,\varepsilon_y^0,\kappa_y.
\]

`R_+,R_c,R_-` 已由3×3解析静力凝聚消去，不成为新的路径自由度。

---

# 18. 退化门

03必须满足：

1. `K_r^Sigma -> infinity`：`R_i -> 0`, `DeltaD -> 0`，恢复01完全组合；
2. `K_r^Sigma -> 0`：钢面纵向组合杠杆刚度被大幅释放，钢面在plane-stress意义下趋向独立轴向响应；
3. `k_+=k_-`：`R_c=0`；
4. 上下钢面交换且连接刚度交换，总轴力不变；
5. 每个m的外层D与同一个m的slip condensation同源；
6. 边缘格室若 `sigma_cr>=fy` 自动退化为E，否则自动local-first；
7. 不允许用FEM峰值反推 `K_r`。

---

# 19. 03-R01的明确边界

03修复了02集中式gamma、half-core、外内层刚度不一致和edge-E四个问题，但仍是降阶诊断理论：

- `K_r^Sigma=75.835 kN/mm/rib` 的物理来源仍未source-lock；
- 当前slip shape只取整体主谐波，不含x相关滑移，因此D66不释放；
- current nonlinear slip amplitudes没有另做材料切线随状态重解，而采用初始弹性partial-interaction凝聚生成的固定谐波传递算子；若升级production，需把同一3层残量提升为current tangent/Schur凝聚；
- R06仍是first-local-yield capped reduced operator，而非完整塑性区演化；
- 局部R02几何缩短引起的interface shear oscillation目前只保留exact analytic kernel，不直接修改gross mean N/M。

因此身份锁定：

`MULTIWAVE_STEEL_SHELL_03 = DISTRIBUTED_PARTIAL_INTERACTION_DIAGNOSTIC_R01`

`PRODUCTION_R14 = UNCHANGED`
