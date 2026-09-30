# UCFT 低维全过程半解析理论 当前状态

更新时间：2026-09-30 18:15 +08:00

## 1. 最高层级合同

当前最高优先级路线合同：用户上传《指示词(6).md》。

理论身份：

\[
\text{single-q 主导}
+\text{steel-local }A^+/A^-\text{ 从属}
+\text{nonlinear membrane condensation}
+\text{UHPC analytic active-set}
+\text{steel Mises deformation theory}.
\]

结构级保持：

\[
q=\text{continuation parameter},
\]

给定 q 后最终求：

\[
P,\quad A^+,\quad A^-,
\]

并满足：

\[
R_q=0,\qquad R_{A^+}=0,\qquad R_{A^-}=0.
\]

端缩仅为 equilibrium state 后的 derived response。

## 2. global geometry

\[
X=\pi x/b,\qquad Y=\pi y/a_h,
\]

\[
W_0=bq_0\sin X\sin Y,
\qquad
W_g=b(q_0+q)\sin X\sin Y,
\]

\[
Q(q)=q^2+2q_0q,
\qquad
C_q=\pi^2Q/8.
\]

初始缺陷是 stress-free geometry，绝不产生 \(q_0^2\) 初始应力。

## 3. C0/C1 baseline

C0：

\[
\varepsilon_x^0=E_x+B_x\cos2X-C_q\cos2Y,
\]

\[
\varepsilon_y^0=E_y-C_q(b^2/a_h^2)\cos2X+B_y\cos2Y,
\]

\[
\gamma_{xy}^0=0,\qquad N_{xy}=0.
\]

C1：

\[
\varepsilon_x^0\supset H_x\cos2X\cos2Y,
\]

\[
\varepsilon_y^0\supset H_y\cos2X\cos2Y,
\]

\[
\gamma_{xy}^0=
-\left[(b/a_h)H_x+(a_h/b)H_y\right]\sin2X\sin2Y.
\]

M0 compatibility：PASS。

## 4. Gate 状态

### M1 / Gate1
PASS。

线弹性、\(A^+=A^-=0\) 时严格退化到 Chen-Ji/Airy \(N_{xy}=0\) separation。

### M2 / Gate2
PASS at model-class / diagnostic level。

A=0、UHPC nonlinear active-set 下，BH050 代表半波 diagnostic：

- 中央 7 MPa tensile family：q=0~0.02，41 点；
- \(\max|P_{C1}/P_{C0}-1|=0.04821\%\)；
- \(\max\eta_H=0.4939\%\)；
- 三组 admissible 7 MPa tensile polynomial family 的最大 C0/C1 path difference \(\le0.10898\%\)。

M2 还修正了 q 外载虚功：

\[
R_q=
\int_\Omega
[N_x\varepsilon_{x,q}^0+N_y\varepsilon_{y,q}^0+N_{xy}\gamma_{xy,q}^0+
M_x\kappa_{x,q}+M_y\kappa_{y,q}+M_{xy}\kappa_{xy,q}]\,dA
-
P a_h(b^2/a_h^2)C_q'=0,
\]

\[
C_q'=\pi^2(q+q_0)/4.
\]

修正后线弹性极限恢复：

\[
P(q)=P_{cr}\frac{q}{q+q_0}+C_A(q^2+2q_0q).
\]

### M3 / Gate3 geometric spectrum audit
PASS，且发现 current C1 必须保留 finite enrichment interface。

whole-face local geometry：

\[
\psi_\ell=[1-\cos(2NX)][1-\cos(2mY)].
\]

qA exact channel：

- normal parity = sin-sin；
- shear parity = cos-cos；
- generic \(N,m\ge2\) 有八个 mixed pairs：

\[
(2N\pm1,1),\quad
(1,2m\pm1),\quad
(2N\pm1,2m\pm1).
\]

因此现有 C-family 不能表示 qA channel。新增严格 compatible S-family：

\[
\Delta\varepsilon_x=S_{x,kl}\sin(kX)\sin(lY),
\]

\[
\Delta\varepsilon_y=S_{y,kl}\sin(kX)\sin(lY),
\]

\[
\Delta\gamma_{xy}
=
-\left[
\frac{lb}{ka_h}S_{x,kl}
+
\frac{ka_h}{lb}S_{y,kl}
\right]\cos(kX)\cos(lY),
\]

并已逐项证明 compatibility contribution = 0。

A² exact channel：

mixed C-family：

\[
(2N,2m),\quad(2N,4m),\quad(4N,2m),\quad(4N,4m),
\]

同时严格产生 1-D companion harmonics：

\[
(0,2m),\quad(0,4m),\quad(2N,0),\quad(4N,0).
\]

这些 1-D 项不能漏掉。

线弹性 plane-stress steel tangent 下，对任一 mixed C/S harmonic 的 normalized residual：

\[
\widehat g_x
=
a+\nu_sb
-\frac{1-\nu_s}{2}\frac{l(b/a_h)}{k}c,
\]

\[
\widehat g_y
=
b+\nu_sa
-\frac{1-\nu_s}{2}\frac{k}{l(b/a_h)}c.
\]

M3 机制扫描：

\[
\nu_s=0.30,\quad N,m=2,\ldots,12,\quad 0.5\le b/a_h\le2.
\]

qA 六个通常主导 pair 的 squared-residual share：

\[
95.3120\%\sim99.8324\%,
\]

但两个 off-diagonal high-high pair 单项最大仍可达到 2.3440%，故不能永久从通用候选库删除。

A² 的 1-D \((0,4m)\)、\((4N,0)\) 项 squared-residual share 最大可达约 42.5647%，与 mixed terms 同量级，必须保留。

M3 裁决：

\[
\boxed{\mathrm{M3\ spectrum\ audit}=PASS}
\]

但：

\[
\boxed{\text{原单一 C1 }(2,2)\text{ pair 覆盖全部 steel-local}=FAIL}.
\]

这是 minimal compatible enrichment，不是路线级失败，也不增加结构级 \(q,A^+,A^-\)。

production 采用：

\[
\text{C0/C1 baseline}
+
\text{frequency-generated C/S/B inner active-set}.
\]

实际 statewise 激活由 omitted residual 决定，不预先堆叠巨大 Fourier basis。

## 5. TOP/BOTTOM local coupling rule

TOP：

\[
q_0A^+ + qA_0^+ + qA^+,
\qquad
(A^+)^2+2A_0^+A^+.
\]

BOTTOM global-local 项整体变号，local-local 项不变。

因此 qA top/bottom residual 异号组合；A² 同号相加。

完全对称 benchmark 可以使 qA membrane forcing 相消，但正式理论的 \(A^+,A^-\) 是独立从属响应，不能据此通用删项。

## 6. 当前材料状态

UHPC：
- tension/compression 分开 polynomial / piecewise polynomial；
- thickness active-set 已闭式；
- current contract 只锁定 tensile peak ~7 MPa 量级；
- production 面内 active-set 已由 M4 完成：解析 z + 解析 Y + 单一 X 确定积分。

Steel：
- M3 只用 linear plane-stress tangent 做 harmonic mechanism audit；
- final steel deformation-theory elastic/plastic active-set 尚待 M5；
- finite current stress 与 tangent 必须分离。


## 7. M4 / UHPC production analytic active-set

PASS。

在 C1 directional mapping 下，固定 X 后 UHPC 顶/底面材料输入严格化为

\[
e^\pm(X,s)=A(X)+B(X)+C^\pm(X)s-2B(X)s^2,\qquad s=\sin Y,
\]

故任一材料阈值 \(e_j\) 的面内 moving boundary 由二次方程

\[
-2Bs^2+C^\pm s+A+B-e_j=0
\]

显式给出。厚度方向继续使用 M2 的解析 active-set，并进一步构造全局累计原函数

\[
\mathcal F'(e)=\sigma(e),\qquad \mathcal H'(e)=e\sigma(e),
\]

使

\[
N^U=\frac{\mathcal F(e^+)-\mathcal F(e^-)}{\chi},
\]

\[
M^U=\frac{\mathcal H(e^+)-\mathcal H(e^-)-e_m[\mathcal F(e^+)-\mathcal F(e^-)]}{\chi^2}.
\]

固定 X 后，Y 向 active intervals 内的结果为有限 Laurent polynomial，利用 \(s=\sin Y\) 的闭式 primitives 完成 Y 解析积分；production 仅保留一个 X 向 deterministic integral。

独立一致性核验：
- cumulative primitive vs 显式 z_j 排序 active-set：最大相对差 \(1.722389\times10^{-8}\)；
- 解析 Y + 一维 X vs 80×120 二维 Gauss diagnostic：最大相对差 \(2.720307\times10^{-7}\)，平均绝对相对差 \(2.269048\times10^{-8}\)。

因此：

\[
\boxed{\mathrm{M4\ analytic\ active\mbox{-}set\ kernel}=\mathrm{PASS}}.
\]

正式 UHPC tensile polynomial 的具体 \(e_{tp},e_{tu}\) 与系数仍未冻结；M2 central family 仅用于算法等价性 benchmark，未升级为生产材料输入。该输入在 M8 前冻结，不阻塞 M5。

正式文件：
- semantic_v2/40_execution/ucft_low_dim_semianalytical/UCFT_M4_UHPC_active_set_analytic_partition.md
- Library /UCFT_backups/20260930_152314/output/UCFT_M4_UHPC_active_set_analytic_partition.md

## 8. M3 正式文件

GitHub：
- semantic_v2/40_execution/ucft_low_dim_semianalytical/UCFT_M3_steel_local_mixed_harmonic_audit.md
- commit: 33cdac0d9ef87c56ac1fc0c873baac91f07daaaa

Library：
- /UCFT_backups/20260930_145000/output/UCFT_M3_steel_local_mixed_harmonic_audit.md
- /UCFT_backups/20260930_145000/output/UCFT_M3_qA_A2_解析频谱.csv
- /UCFT_backups/20260930_145000/output/UCFT_M3_N4_m4_归一化残量谱.csv
- /UCFT_backups/20260930_145000/output/UCFT_M3_频谱鲁棒性扫描.csv
- /UCFT_backups/20260930_145000/output/UCFT_M3_频谱审计摘要.csv
- /UCFT_backups/20260930_145000/output/UCFT_M3_频谱审计结果.txt
- /UCFT_backups/20260930_145000/output/UCFT_M3_mixed_harmonic_解析谱计算器.py

## 9. 九试件进度

尚未进入 M8。M4 没有使用 FEM target 求根或调参；M2 central tensile family 仅用于积分算法 benchmark。

## 10. 已排除/禁止

继续禁止：
- 31/41/57DOF 主理论回归；
- 固定 q 盲扫 Pu；
- FEM 标定参数；
- q 与独立 curvature 并存；
- 大量 spatial Gauss 作为 production definition；
- 人为负刚度制造下降段；
- PBL 经验弹簧。

## 11. M5 / steel deformation-theory active-set

PASS after one internal constitutive-interface correction.

Literal splice audit:
- elastic plane-stress nu_s=0.30 -> Chen-Ji plastic simplification nu_p=0.50 at eps_i=fy/Es produced up to 40% finite stress-tensor jump;
- elastic Mises/fy on that literal strain threshold ranged 0.714286~1.153846;
- therefore literal abrupt splice was rejected as materially discontinuous.

Production M5 uses the minimum consistent generalization:
\[
\mathbf C_0=\frac1{1-\nu_s^2}
\begin{bmatrix}
1&\nu_s&0\\
\nu_s&1&0\\
0&0&(1-\nu_s)/2
\end{bmatrix},
\quad
\mathbf H_\nu=\mathbf C_0^T\mathbf W\mathbf C_0,
\]
\[
\bar\varepsilon_i=\sqrt{\boldsymbol\varepsilon^T\mathbf H_\nu\boldsymbol\varepsilon}
=\sigma_{VM}^{elastic}/E_s.
\]
Plastic equivalent law and dual modulus:
\[
\sigma_i=P_s(\bar\varepsilon_i),\quad
E_{sec}=P_s/\bar\varepsilon_i,\quad
E_{tan}=dP_s/d\bar\varepsilon_i.
\]
Finite stress:
\[
\boldsymbol\sigma=E_{sec}\mathbf C_0\boldsymbol\varepsilon.
\]
Tangent:
\[
\mathbf C_t=
E_{sec}\mathbf C_0+
\frac{E_{tan}-E_{sec}}{\bar\varepsilon_i^2}
(\mathbf C_0\boldsymbol\varepsilon)\otimes
(\mathbf H_\nu\boldsymbol\varepsilon).
\]
At nu_s=0.5 this reduces exactly to the Chen-Ji simplified Mises deformation-theory form.

For affine steel thickness strain:
\[
\bar\varepsilon_i^2=C_2\zeta^2+C_1\zeta+C_0,
\]
so yield boundaries remain quadratic and all elastic/plastic intervals are analytically sorted. Finite polynomial Ps gives elementary/asinh-recursive closed-form thickness resultants; no thickness Gauss points define production.

Validation:
- exact thickness resultants vs numerical diagnostic: 7.727093e-14 max relative error;
- yield root error: 2.168404e-19;
- tangent vs finite difference: 2.568376e-10;
- finite Mises vs Ps target: 1.601223e-16;
- nu=0.5 Chen-Ji reduction: exact;
- corrected yield-interface finite stress jump: 0.

Production file:
- semantic_v2/40_execution/ucft_low_dim_semianalytical/UCFT_M5_steel_deformation_theory_active_set.md
- Library /UCFT_backups/20260930_163600/output/UCFT_M5_steel_deformation_theory_active_set.md
- Library /UCFT_backups/20260930_163600/output/UCFT_M5_steel_Mises_deformation_active_set_kernel.py

Formal Q355 plastic polynomial coefficients are not yet frozen. Diagnostic plateau/cubic laws are algorithm tests only. Freeze from actual material data before M8; do not fit Pu.

## 12. 九试件进度

尚未进入 M8。M5 没有使用 FEM target 求根或调参。


## 13. M6 / residual + Schur condensation

PASS。

- complete inner residual: \(\mathbf G(\boldsymbol\xi,\mathbf z;q)=0\)；
- outer state: \(\mathbf z=[P,A^+,A^-]^T\)；
- outer residual: \(\mathbf R=[R_q,R_{A^+},R_{A^-}]^T=0\)；
- steel strain input includes full \(qA\) and \(A^2\) channels plus global eccentric curvature；
- direct TOP/BOTTOM cross derivative is zero, but condensed \(A^+-A^-\) coupling generally nonzero through \(\boldsymbol\xi\)；
- exact Schur:
\[
K_{\rm cond}=R_z-R_\xi G_\xi^{-1}G_z;
\]
- for nonzero inner residual, exact condensed Newton RHS is
\[
-R+R_\xi G_\xi^{-1}G;
\]
- q sensitivity:
\[
d\mathbf z/dq=-K_{\rm cond}^{-1}(R_q^\partial-R_\xi G_\xi^{-1}G_q).
\]

Validation:
- Schur/full Newton outer difference \(1.110223\times10^{-16}\)；
- Schur/full Newton inner difference \(1.110223\times10^{-16}\)；
- q sensitivity outer difference \(1.665335\times10^{-16}\)；
- q sensitivity inner difference \(4.163336\times10^{-17}\)；
- steel-local kinematic derivative maximum relative error \(1.390166\times10^{-10}\)。

PBL/web correction remains report-only:
\[
P_{\rm report}=\chi_wP_c+P_s^++P_s^-.
\]

Formal M6 files:
- semantic_v2/40_execution/ucft_low_dim_semianalytical/UCFT_M6_inner_outer_residual_Schur_condensation.md
- semantic_v2/40_execution/ucft_low_dim_semianalytical/UCFT_M6_residual_schur_assembler.py
- Library /UCFT_backups/20260930_170500/output/UCFT_M6_inner_outer_residual_Schur_condensation.md
- Library /UCFT_backups/20260930_170500/output/UCFT_M6_Schur凝聚等价性验证.csv
- Library /UCFT_backups/20260930_170500/output/UCFT_M6_steel_local运动学导数验证.csv

## 14. 九试件进度

尚未进入 M8。M6 没有使用 FEM target 求根或调参。


## 15. M7 / theory self-audit

PASS after two exact internal corrections.

### M7-1 zero-load / linear / q->0 / A->0 / symmetry

- zero-load loading-induced strain/curvature max = 0；
- linear C1 H-block positive, benchmark minimum eigenvalue \(1.748459\times10^7\)，故 \(H_x=H_y=0\) 唯一；
- \(q\to0\) imperfect branch regular，\(P/q\) analytic-limit benchmark relative error \(3.999787\times10^{-6}\)；
- \(A_0=0,A=0\) 时 local finite strain/curvature 严格消失；\(R_A\) 在 \(q>0\) 可被 global-local interaction 驱动，不要求恒零；
- TOP/BOTTOM global-local odd、local-local even、local curvature antisymmetry，max parity error \(5.421011\times10^{-20}\)。

### M7-2 raw S-family loading-edge work correction

raw odd-odd \(S_y\) compatible mode 的 loading-edge mean displacement coefficient：
\[
c_{kl}
=
\frac{[1-(-1)^k][1-(-1)^l]}{kl\pi^2}.
\]
qA S-family 均为 odd-odd，因此 \(c_{kl}=4/(kl\pi^2)\neq0\)。

production 采用 exact traction-orthogonal basis：
\[
\widetilde B_{S_y}
=
B_{S_y}^{raw}
-c_{kl}B_{E_y}.
\]
于是 mean edge displacement = 0，且
\[
G_{\widetilde S_y}
=
G_{S_y}^{raw}-c_{kl}G_{E_y},
\]
故 root set、M3 spectrum、structural variables 与 Schur system 不变。

对应 M6 assembler 已修正。

### M7-3 virtual work / Jacobian / Schur

- common external-potential derivative benchmark max relative error \(4.262074\times10^{-10}\)；
- full nonlinear surrogate residual/Jacobian finite-difference max scaled relative error \(3.862825\times10^{-6}\)；
- physics-shaped Schur/full Newton inner difference \(4.054916\times10^{-17}\)；
- outer difference \(2.273737\times10^{-13}\)。

### M7-4 dimensional scaling

\[
[G_\xi]=FL,\qquad [R_q]=FL,\qquad [R_A]=F.
\]
raw mixed-unit Jacobian condition number 不再作为 branch diagnostic。

正式使用：
\[
\widehat J=S_F^{-1}JS_x
\]
以及 scaled \(\widehat G_\xi,\widehat K_{cond}\) condition/singular values。

单位变换 benchmark dimensionless matrix difference \(4.440892\times10^{-16}\)。

### M7-5 branch continuity

M8 production material inputs 必须满足 finite-stress continuity：

UHPC：
\[
P_c(0)=P_{t1}(0)=0,
\]
\[
P_{t1}(e_{tp})=P_{t2}(e_{tp})=f_t,
\]
若 terminal 后设零应力：
\[
P_{t2}(e_{tu})=0,\qquad P_c(e_z)=0.
\]

Steel：
\[
P_s(f_y/E_s)=f_y.
\]

tangent continuity 不要求；event localization / semismooth Newton 处理 topology switch。

### M7-6 equilibrium load 与 report load

M6 equilibrium unknown 统一改记：
\[
P_{eq}.
\]

PBL/web 当前仍为 report-only reaction correction：
\[
P_{report}
=
\chi_wP_c+P_s^++P_s^-.
\]

从 M8 起项目最终输出定义：
\[
P(q)\equiv P_{report}(q).
\]

因此：
\[
P_u=\max_qP_{report}(q),
\]
regular q branch 上用：
\[
dP_{report}/dq=0.
\]

Schur 第一分量 \(dP_{eq}/dq\) 不再在 \(\chi_w\neq1\) 时直接定义最终 Pu。

正式 M7 文件：
- semantic_v2/40_execution/ucft_low_dim_semianalytical/UCFT_M7_theory_self_audit.md
- semantic_v2/40_execution/ucft_low_dim_semianalytical/UCFT_M7_理论自检摘要.csv
- Library /UCFT_backups/20260930_181500/output/

\[
\boxed{\mathrm{M7}=PASS}.
\]

## 16. 九试件进度

尚未正式进入 M8 路径求解；M7 未使用 FEM target 或 Pu 拟合。

## 17. NEXT_ACTION

严格进入 M8 准备/执行起点：

先从现有 Project/Library/仓库恢复并冻结九试件正式材料与几何输入，尤其：

- UHPC \(e_{tp},e_{tu},P_{t1},P_{t2}\)；
- Q355 production \(P_s(\bar\varepsilon_i)\) polynomial；
- 九试件 geometry、\(N^\pm,m^\pm,A_0^\pm\)、PBL reaction-correction inputs。

若现有资料已经包含这些输入，不再询问用户，直接恢复并运行 connected q-path。


## 16. M8 / production input freeze（2026-09-30 19:01 +08:00）

状态：

\[
\boxed{\mathrm{M8\_INPUT\_FREEZE}=\mathrm{PARTIAL}}
\]

已恢复并冻结：
- steel: Es=206000 MPa, nu_s=0.30, fy=355 MPa；
- steel equivalent uniaxial post-yield law 正式采用项目原生 ideal elastic-perfectly plastic，作为 M5 degree-0 polynomial branch：
  \[
  P_s(\bar\varepsilon_i)=f_y,\quad E_{sec}=f_y/\bar\varepsilon_i,\quad E_{tan}=0;
  \]
- UHPC compression: Ec=43400 MPa, nu_c=0.20, fc=141.1 MPa, eps_c0=0.0035；
- tc=42 mm, ts=4 mm, Aw=1332 mm2, q0=0.0025；
- 九件宽度 b=250,500,1000,1600,2500,3000,3500,4250,5000 mm，a_h=2b；
- 已逐件计算 chi_w；
- 历史 local strip imperfection scale A0_strip=0.225b/1600 已恢复，但未偷换成 current whole-face A0±。

尚未唯一冻结：
1. 当前约 7 MPa UHPC 的 production tension law：Pt1/Pt2、e_tp、e_tu；
2. current whole-face steel local mode 的 N±,m±,A0± 正式映射/选择规则。

外部/Library 检索只用于输入来源核验，没有用 FEM Pu 选参数。Hiew 2024 的 2% fibre tensile peak 约 11 MPa，不能直接作为当前约 7 MPa project material；胡文旭材料（fc,axial=136.9 MPa, ft=7.2 MPa, E=45.1 GPa, Vf=2%）是近邻证据，但尚不足以唯一恢复当前 production Pt1/Pt2。

因此九试件正式 connected q-path 尚未启动；阻塞原因是不可替代 production input 尚未唯一闭合，不是求解器失败。

正式文件：
- UCFT_M8_production_input_freeze.md
- UCFT_M8_九试件输入清单.csv
- UCFT_M8_材料输入冻结状态.csv
- UCFT_M8_material_geometry_contract.py

## 17. NEXT_ACTION

继续 M8 input freeze：恢复/构造有明确来源的约 7 MPa UHPC production tensile polynomial，并从 current whole-face steel-local 历史推导中恢复 N±,m±,A0± 的正式选择规则；闭合后立即启动九试件 connected q-path。
