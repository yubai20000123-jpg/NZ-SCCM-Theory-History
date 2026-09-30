# UCFT 低维全过程半解析理论 执行日志

## 2026-09-30 13:31 +08:00

### task
严格按《指示词.md》恢复项目并执行 M0，随后执行允许的 M1 Gate 1 解析退化证明。

### files read / restored
- 指示词.md（本轮上传，路线合同）
- Project/Library 中既有 UCFT 层0、陈骥、解析化与极值迭代、V3 工程状态等文件
- GitHub: yubai20000123-jpg/NZ-SCCM-Theory-History；确认 private、main、push permission=true
- 未找到此前已创建的四个稳定文件：当前状态 / 当前推导 / 执行日志 / 备份清单，因此本轮首次创建。

### files created
- semantic_v2/40_execution/ucft_low_dim_semianalytical/UCFT_nonlinear_membrane_condensation_当前推导.md
- semantic_v2/40_execution/ucft_low_dim_semianalytical/UCFT_低维全过程半解析理论_当前状态.md
- semantic_v2/40_execution/ucft_low_dim_semianalytical/UCFT_低维全过程半解析理论_执行日志.md
- semantic_v2/40_execution/ucft_low_dim_semianalytical/UCFT_低维全过程半解析理论_备份清单.md

### backups
input:
- backups/20260930_133100/input/指示词.md

output:
- backups/20260930_133100/output/UCFT_nonlinear_membrane_condensation_当前推导.md
- 同时间戳下同步备份当前状态、执行日志、备份清单。

### formulas changed / added
正式锁定 C0/C1 compatible membrane basis。
C1 由显式 u,v 生成，包含 Hx/Hy mixed/shear-compatible pair。
建立六个 inner generalized residual。
完成线弹性 Gate 1 解析证明。

### independent algebra check
用符号代数核验：
- 从 u,v + Kármán geometry 恢复目标 epsilon_x/epsilon_y/gamma_xy；
- compatibility 左端严格化为 pi^4 Q/(2 a_h^2)(cos2X+cos2Y)。

### gate status
- M0 compatible basis: PASS
- M0 compatibility identity: PASS
- M0 residual system: PASS
- M1 Gate 1: PASS
- M2: NOT STARTED

### numerical result
本轮为解析门槛，无试件数值路径结果。

### theory issue
无致命问题。
记录 Gate 1 对称 benchmark 适用边界。

### NEXT_ACTION
M2：A+=A−=0，打开 UHPC tension/compression polynomial active-set，构造 C0/C1 current composite membrane kernel，并准备 q-path 比较。


### backup correction / exact original preservation
- 原上传《指示词.md》已额外以原始文件快照保存到个人 Library：
  /UCFT_backups/20260930_133100/input/指示词.md
- library_file_id: libfile_7cfb901ec6b08191aeefe77588079d3b
- GitHub backups/20260930_133100/input/指示词.md 为便于仓库检索的文本镜像；原始上传快照以 Library 版本为准。


## 2026-09-30 14:17 +08:00 — M2

### task
A+=A−=0；打开 UHPC nonlinear tension/compression polynomial active-set；建立 C0/C1 current membrane kernel，并计算 C0/C1 P(q)、Hx/Hy、omitted shear residual。

### recovery / pre-backup
本轮执行前已读取：
- 当前状态；
- 当前推导；
- 执行日志；
- 备份清单；
- 本轮上传《指示词(1).md》。

pre-backup：
- backups/20260930_141737/input/UCFT_低维全过程半解析理论_当前状态.md
- backups/20260930_141737/input/UCFT_nonlinear_membrane_condensation_当前推导.md
- backups/20260930_141737/input/UCFT_低维全过程半解析理论_执行日志.md
- backups/20260930_141737/input/UCFT_低维全过程半解析理论_备份清单.md
- backups/20260930_141737/input/指示词(1).md（GitHub text mirror）
- Library exact upload: /UCFT_backups/20260930_141737/input/指示词(1).md

### formulas added
1. UHPC e_x/e_y thickness-linear active-set；
2. threshold z_j=(e_j-e_m)/chi；
3. polynomial primitives for exact N/M thickness integration；
4. M2 7 MPa non-fitted tensile polynomial diagnostic family；
5. corrected q external virtual-work term。

### critical correction
当前 compatible v(x,ah)=ah[Ey-Cq(b^2/ah^2)]，所以 q virtual displacement 对加载边有非零位移。
正式：
Rq = internal q virtual work - P*ah*(b^2/ah^2)*Cq' = 0.

若删除该外力项，线弹性 C0 中均匀 P 项因 cos2X 正交而从 q 内虚功消失，不能正确建立 P-q 稳定关系。

修正后严格恢复：
P(q)=Pcr*q/(q+q0)+CA*(q^2+2q0*q).

分类：NEEDS_CORRECTION，非致命，不改变 M0 compatible basis / Gate1 membrane result。

### diagnostic numerical setup
Representative BH050 half-wave:
b=ah=2500 mm, q0=0.0025, tc=42 mm, ts=4 mm.
steel-local off；symmetric steel skins linear elastic.
UHPC thickness exact analytic active-set.
X-Y Gauss-Legendre only diagnostic evaluator, not production theory definition.

Central tensile family:
ft=7.0 MPa, rt=2, eps_tu/eps_tp=5.

### results
q=0..0.02, 41 points:
max abs(P_C1/P_C0-1)=0.04821%.
max eta_omitted=0.004939=0.4939%.

Three deliberately separated 7 MPa tensile polynomial families:
- rt=1.5, lambda=2: max dP=0.10898%, max eta=0.004807
- rt=2.0, lambda=5: max dP=0.04785%, max eta=0.004938
- rt=3.0, lambda=10: max dP=0.03063%, max eta=0.004103

Therefore UHPC material nonlinearity alone activates nonzero C1 Hx/Hy, but P(q) sensitivity is <=~0.11% in this M2 diagnostic family.

At q=0.005 central case:
P_C0=13.14013 MN
P_C1=13.13558 MN
eta_omitted=0.002280
Hx=1.3601e-5
Hy=-5.8668e-6
UHPC x-direction active fractions:
T1=70.13%, C=20.48%, T2=9.39%
UHPC y-direction: C=100%.

### numerical consistency
8x8 vs 12x12 diagnostic X-Y evaluator:
P differences at q=0.005,0.010,0.020 remain below ~0.003%.

One 16x16 full-path convergence run exceeded the current single execution 60 s limit and was interrupted. No incomplete 16x16 result was retained or used.

### runtime
Unoptimized 12x12 Python:
C0 mean ~0.39 s/q point
C1 mean ~0.54 s/q point
continuation nfev typically 3, max 4.

### files generated / backed
Library:
- UCFT_M2_BH050_C0_C1_诊断路径.csv
  libfile_05df8419b6348191861c1b18031ac9c6
- UCFT_M2_UHPC拉伸多项式敏感性.csv
  libfile_d6c8988fc93881919ccdf6f74ec2af72
- UCFT_M2_面积求积独立核验.csv
  libfile_80a734c2379c81918bee5f16e0efdc02
- UCFT_M2_nonlinear_membrane_诊断计算器.py
  libfile_e054c0bb3c2081919ccf749e976e99a6

GitHub derivation commit:
67e4d7fb852dc432233fc6c644cb1bedbf549b74

GitHub state commit:
247ff99cf34959f16f717a9a00fab49ccf8d994d

### gate status
M0 PASS
M1 / Gate1 PASS
M2 / Gate2 PASS at model-class/diagnostic level
Nxy production deletion decision: DEFER TO M3
M3 NOT STARTED

### NEXT_ACTION
M3：打开 A+/A−，不预增 membrane modes；完整展开 qA/A² steel-local mixed-harmonic frequency set，计算 omitted generalized residual spectrum，仅激活显著 compatible pairs。


## 2026-09-30 14:50 +08:00 — M3 steel-local mixed-harmonic audit

### recovered
读取当前 CURRENT_STATE / nonlinear membrane derivation / execution log / backup manifest，并完整读取新上传《指示词(2).md》。M0/M1/M2 均已完成，因此按合同直接进入 M3。

### pre-backup
GitHub：
- backups/20260930_145000/input/UCFT_低维全过程半解析理论_当前状态.md
  commit 1dc7f249425b08490cb29bbee75574c31ff5231b
- backups/20260930_145000/input/UCFT_nonlinear_membrane_condensation_当前推导.md
  commit 38b92ce8061e5f60c52e6ed665a1e6ab608fc0d3
- backups/20260930_145000/input/UCFT_低维全过程半解析理论_执行日志.md
  commit 5d4ad2b633ac6c203c643fd0ea66f1eb3922518b
- backups/20260930_145000/input/UCFT_低维全过程半解析理论_备份清单.md
  commit 2299e70eb2f633818c821741dd50cc4e1fe791ed

原始《指示词(2).md》已原名保存至：
Library /UCFT_backups/20260930_145000/input/指示词(2).md
libfile_cbb9afffcb3481919e6df40ddfe46893。

GitHub 大文本镜像尝试被工具安全检查阻止，未伪称成功；Library exact copy 为本轮原件备份。

### formulas / findings
从 whole-face local geometry 精确展开 qA 与 A²。

qA：
- normal = sin-sin odd-odd；
- shear = cos-cos odd-odd；
- generic \(N,m\ge2\) exact mixed pairs：
  \((2N\pm1,1)\)、\((1,2m\pm1)\)、\((2N\pm1,2m\pm1)\)。
- 现有 C-family 对此 parity 不适用。
- 新增严格 compatible S-family：
\[
\Delta\varepsilon_x=S_x\sin kX\sin lY,\quad
\Delta\varepsilon_y=S_y\sin kX\sin lY,
\]
\[
\Delta\gamma
=
-\left[
\frac{lb}{ka_h}S_x+\frac{ka_h}{lb}S_y
\right]\cos kX\cos lY.
\]
已符号验证 compatibility contribution = 0。

A²：
- mixed C-family：
  \((2N,2m),(2N,4m),(4N,2m),(4N,4m)\)；
- 同时产生 1-D companion：
  \((0,2m),(0,4m),(2N,0),(4N,0)\)。
- 1-D 项不是格式细节；必须进入 candidate ledger。

线弹性 steel plane-stress normalized mixed residual：
\[
\widehat g_x
=
a+\nu b-\frac{1-\nu}{2}\frac{l(b/a_h)}{k}c,
\]
\[
\widehat g_y
=
b+\nu a-\frac{1-\nu}{2}\frac{k}{l(b/a_h)}c.
\]

### dimensionless spectrum audit
扫描：
\[
\nu_s=0.30,\ N,m=2..12,\ b/a_h=0.5..2.
\]
无 FEM target。

qA：
- four edge share: 74.8746%–98.7147%
- six dominant share: 95.3120%–99.8324%, mean 99.1172%
- two off-diagonal high-high modes each max 2.3440%

A²：
- mixed (2N,4m)/(4N,2m) max 38.1537%
- mixed (2N,2m) ~9.24%
- mixed (4N,4m) max 4.7142%
- 1-D (0,4m)/(4N,0) max 42.5647%
- 1-D (0,2m)/(2N,0) max 6.8198%

### gate
M3 geometric spectrum audit = PASS.

但：
原单一 C1 (2,2) pair 覆盖全部 steel-local = FAIL。

分类：NEEDS_MINIMAL_COMPATIBLE_ENRICHMENT；非路线级失败。结构级仍只有 q,A+,A−。采用 finite frequency-generated C/S/B inner active-set；实际 statewise 激活由 omitted residual 决定。

### files
GitHub full M3 report：
semantic_v2/40_execution/ucft_low_dim_semianalytical/UCFT_M3_steel_local_mixed_harmonic_audit.md
commit 33cdac0d9ef87c56ac1fc0c873baac91f07daaaa

Current state updated:
commit 032028166e95d2e47f2a795302bd437708195983

Library output：
- UCFT_M3_steel_local_mixed_harmonic_audit.md
- UCFT_M3_qA_A2_解析频谱.csv
- UCFT_M3_N4_m4_归一化残量谱.csv
- UCFT_M3_频谱鲁棒性扫描.csv
- UCFT_M3_频谱审计摘要.csv
- UCFT_M3_频谱审计结果.txt
- UCFT_M3_mixed_harmonic_解析谱计算器.py

### NEXT_ACTION
M4：完成 UHPC tension/compression polynomial active-set 的 production 面内解析分区；保留 M2 thickness closed form，二维/三维 Gauss 不得定义 production residual。


## 2026-09-30 15:23 +08:00 — M4 UHPC analytic active-set partition

### task
严格执行 M4：保持 M2 thickness closed form，完成 UHPC tension/compression piecewise-polynomial active-set 的 production 面内解析分区；二维/三维 Gauss 仅作独立验证。

### recovery / pre-backup
已恢复最新 CURRENT_STATE / nonlinear membrane derivation / execution log / backup manifest / M3 report，并读取本轮上传《指示词(3).md》。M3 已完成，故直接进入 M4。

pre-backup GitHub：
- backups/20260930_152314/input/UCFT_低维全过程半解析理论_当前状态.md — 55541ff5dd081bd9e192ae85cdd048a52d4bb07a
- backups/20260930_152314/input/UCFT_nonlinear_membrane_condensation_当前推导.md — 7d561ffb6f1dcb19eb42e1974badf86fa11e0eeb
- backups/20260930_152314/input/UCFT_低维全过程半解析理论_执行日志.md — 2c76fc21e85db184949a75aebf08fa10f79b3845
- backups/20260930_152314/input/UCFT_低维全过程半解析理论_备份清单.md — f088ae47fd75b13dc47210f358257d5339cd2e4a

原上传《指示词(3).md》 exact copy：
Library /UCFT_backups/20260930_152314/input/指示词(3).md；library id libfile_6fff8727f600819186371e8094c7725f。

### formulas added
固定 X 后，令 s=sinY，UHPC 顶/底面 directional strain 严格成为：
\[
e^\pm=A+B+C^\pm s-2Bs^2.
\]
任一材料阈值由：
\[
-2Bs^2+C^\pm s+A+B-e_j=0
\]
显式求 moving boundary。

建立连续累计原函数：
\[
\mathcal F'(e)=\sigma(e),\qquad \mathcal H'(e)=e\sigma(e),
\]
并得到 thickness-exact：
\[
N^U=[\mathcal F(e^+)-\mathcal F(e^-)]/\chi,
\]
\[
M^U=[\mathcal H(e^+)-\mathcal H(e^-)-e_m(\mathcal F(e^+)-\mathcal F(e^-))]/\chi^2.
\]

Y-active intervals 内形成有限 Laurent polynomial；用 J_{-2},J_{-1},J_0,J_1 及递推 J_n 完成 Y 初等闭式。production 只剩一个 X 向 deterministic integral。

UHPC shear channel 保持线性：
\[
G_c=E_c/[2(1+\nu_c)],
\]
故 Nxy、Mxy 与 H/shear residual、q twisting virtual-work 均闭式，不需要 material active-set。

### material lock discipline
当前项目只锁定 UHPC tensile peak ~7 MPa，未找到唯一冻结的 production e_tp/e_tu 与 tensile polynomial coefficients。本轮 kernel 保持材料参数化；M2 central tensile family 只用于算法一致性 benchmark，不冒充最终生产材料。

### independent validation
M2 central diagnostic C1 states：q=0.005,0.010,0.015,0.020。

1. 全局累计 primitive vs 显式 z_j 排序 active-set：
- 4 q × 2 directions × 9 X × 11 Y；
- max relative error = 1.722389e-08。

2. analytic Y + one X deterministic integral vs independent 80×120 2D Gauss diagnostic：
- 比较 8 个 N/M area moments；
- max relative difference = 2.720307e-07；
- mean abs relative difference = 2.269048e-08。

### gate
\[
\boxed{\mathrm{M4\ analytic\ active\mbox{-}set\ kernel}=\mathrm{PASS}}.
\]

### theory issue
无致命问题。未冻结 production tensile e_tp/e_tu/coefficients 属于材料输入未定，不是 M4 数学缺口；记录为 M8 前必须冻结，不阻塞 M5。

### generated / persisted
GitHub stable report：
- semantic_v2/40_execution/ucft_low_dim_semianalytical/UCFT_M4_UHPC_active_set_analytic_partition.md
- commit af80c6e12161ae111a735c40a81a6b1706337ac8

Current state post-M4：
- commit 20b695d701b6c321e8fc0c92e7918d70fb762147

Library output folder /UCFT_backups/20260930_152314/output/：
- UCFT_M4_UHPC_active_set_analytic_partition.md — libfile_a9a8eb64c6dc819195b2823b07e86186
- UCFT_M4_UHPC_analytic_partition_kernel.py — libfile_a09d5b18be4c8191a54299cb95e0c52c
- UCFT_M4_一致性验证摘要.csv — libfile_fa92abdba54c8191ad9cc97122cd88ea
- UCFT_M4_厚度全局原函数_vs_显式active_set验证.csv — libfile_2a5ebb5eee1481919cb365d81219485d
- UCFT_M4_解析材料边界示例.csv — libfile_43c274ff9c008191a9d2d1decf8ed529
- UCFT_M4_面内解析分区_vs_二维Gauss验证.csv — libfile_204daabb48c881918c6c80fb21a170e2

### artifact SHA256
- report: 7ba100f0c35e5d76d2457b657a3bdf557fccdaa03a93401bfcfc1b1bd3117077
- kernel: 5586f5f5af2d3491349f2c37525ce22cff09580fe0ea7d12e1978341f90288a5
- consistency summary: 6e23ee0d368fe7fd8a2d3db9613d536379f4e6b2e95dd579753e410e68d6a299
- thickness validation: 43d85617ab2e32152b08f11d51b3003b3e92f9c01c827572d16ba5ad05cb72e3
- boundary example: dc0d40206c11c5b86efb248ee56ed9dff1731130b58d080dbfd11cc50f9acf8f
- 2D Gauss validation: 0907dcb94a7f8fbd24753046d361495bb7abded6f88f1c1cbc607a1bcfd55f8b

### NEXT_ACTION
M5：steel Mises deformation theory + equivalent uniaxial polynomial + E_sec/E_tan + analytic elastic/plastic thickness active-set；保持 \(\varepsilon_i^2=C_2\zeta^2+C_1\zeta+C_0\)，屈服边界解析求根、排序、分区积分，并严格区分 finite current stress 与 tangent。


## 2026-09-30 16:36 +08:00 — M5 steel deformation-theory active-set

### recovered
读取最新 CURRENT_STATE / nonlinear membrane derivation / execution log / backup manifest，并读取新上传《指示词(4).md》。确认 M0-M4 已完成，NEXT_ACTION=M5。

### pre-backup
- 原始《指示词(4).md》按原名保存至 Library /UCFT_backups/20260930_163600/input/指示词(4).md
- GitHub pre-backup commits:
  - CURRENT_STATE: bea1c50bc0311d57082e96c6fbab249ff201c3df
  - nonlinear membrane derivation: 6d01f817ae64fc55ff05a24d3656cc477f7fbcd3
  - execution log: bd61bb40932321535670e482b632e99d4a8a298d
  - backup manifest: 1f14d62da098c8b9ea9a6fd195f3f2be9a2b015d

### source audit
读取项目 ChenJi Chapter8 archive，确认 Chen-Ji 8.9 deformation theory：
- secant/tangent moduli separated;
- plastic simplification uses nu_p=0.5;
- equivalent strain = 2/sqrt(3)*sqrt(ex^2+ey^2+ex*ey+gamma^2/4).

### first implementation / failure
Literal UCFT splice used actual elastic plane-stress nu_s=0.30 then switched to Chen-Ji nu_p=0.50 at eps_i=fy/Es. Direction scan:
- max finite stress tensor jump = 0.400000;
- elastic Mises/fy at the same literal strain threshold = 0.714286~1.153846.
Classification: NEEDS_CORRECTION; not route-fatal.

### minimal correction
Define normalized elastic plane-stress operator C0, Mises metric W, Hnu=C0^T W C0, and:
ebar_i=sqrt(epsilon^T Hnu epsilon)=elastic_trial_Mises/Es.
Use:
sigma_i=Ps(ebar_i);
Esec=Ps/ebar_i;
Etan=dPs/debar_i;
finite sigma=Esec*C0*epsilon.
Consistent tangent:
Ct=Esec*C0+(Etan-Esec)/ebar_i^2*(C0 epsilon) tensor (Hnu epsilon).
At nu_s=0.5, C0=Hnu exactly equals the Chen-Ji simplified Mises deformation matrix.

### analytic thickness active-set
For affine steel thickness strain:
ebar_i^2=C2*zeta^2+C1*zeta+C0.
Yield boundaries remain quadratic. Finite polynomial Ps gives exact thickness resultants through elementary/asinh quadratic-power primitives. No thickness Gauss defines production.

### numerical consistency
Es=206000 MPa, nu_s=0.30, fy=355 MPa, ts=4 mm; ideal plateau and diagnostic cubic only as algorithm benchmarks:
- exact thickness resultants vs adaptive numerical diagnostic: 7.727093e-14
- yield root absolute ebar error: 2.168404e-19
- consistent tangent vs FD: 2.568376e-10
- finite Mises vs polynomial target: 1.601223e-16
- nu=0.5 Chen-Ji reduction: exact
- yield-interface stress jump after correction: 0
- yield-interface Mises/fy deviation: 3.330669e-16

### gate
Literal abrupt splice = FAIL.
Corrected consistent secant-Mises deformation-theory operator = PASS.

### files
Stable GitHub report:
- semantic_v2/40_execution/ucft_low_dim_semianalytical/UCFT_M5_steel_deformation_theory_active_set.md
- commit aee49e8a6aecd7d12368302ed0bf3410f071042e

Library exact artifacts under:
- /UCFT_backups/20260930_163600/output/

Key files:
- UCFT_M5_steel_deformation_theory_active_set.md
- UCFT_M5_steel_Mises_deformation_active_set_kernel.py
- UCFT_M5_最终一致性验证摘要.csv
- first-failure audit and corrected validation CSVs.

CURRENT_STATE updated:
- commit 7601a49002e558785f90831b95ab9a3939d40c21

### unresolved
Formal production Q355 plastic polynomial coefficients Ps are not frozen. Diagnostic plateau/cubic are not material calibration. Freeze actual material input before M8, not from Pu fitting.

### NEXT_ACTION
M6: assemble M4 UHPC analytic operator + M5 steel consistent secant-Mises operator + M3 C/S/B frequency-generated inner enrichment into inner membrane residual, outer Rq/RA+/RA-, and exact Schur-condensed Jacobian. No nine-specimen run yet.


## 2026-09-30 17:05 +08:00 — M6

task: unified M3/M4/M5 residual and Jacobian assembly; exact Schur condensation.

created:
- UCFT_M6_inner_outer_residual_Schur_condensation.md
- UCFT_M6_residual_schur_assembler.py
- UCFT_M6_Schur凝聚等价性验证.csv
- UCFT_M6_steel_local运动学导数验证.csv

closed:
- full steel-local qA and A2 kinematics connected to M5 affine thickness strain;
- inner G and outer Rq / RA+ / RA-;
- full block Jacobian Gxi/Gz/Rxi/Rz;
- exact condensed Newton RHS when inner residual is nonzero;
- q-continuation condensed sensitivity;
- moving active-boundary tangent rule under continuous finite stress.

checks:
- Schur/full Newton outer max diff: 1.110223e-16
- Schur/full Newton inner max diff: 1.110223e-16
- q-sensitivity outer max diff: 1.665335e-16
- q-sensitivity inner max diff: 4.163336e-17
- steel-local kinematic derivative max relative error: 1.390166e-10

status: M6 PASS.

open before M8:
- freeze production UHPC tensile polynomial;
- freeze production Q355 equivalent uniaxial polynomial;
- keep equilibrium generalized P distinct from P_report under chi_w report correction.

NEXT_ACTION: M7 theory self-audit only.


## 2026-09-30 18:15 +08:00 — M7

task:
- M0–M6 unified self-audit.

files read:
- 指示词(6).md
- CURRENT_STATE / current derivation / execution log / backup manifest
- M6 theory and assembler.

files created:
- UCFT_M7_theory_self_audit.md
- UCFT_M7_理论自检摘要.csv
- UCFT_M7_branch_continuity条件.csv
- UCFT_M7_theory_selfcheck.py
- zero-load / q->0 / TOP-BOTTOM / S-family work / dimensional / Jacobian diagnostics.

files modified:
- UCFT_M6_inner_outer_residual_Schur_condensation.md
- UCFT_M6_residual_schur_assembler.py
- current state / current derivation.

formulas changed:
1. raw odd-odd S_y loading-edge work identified:
   \(c_{kl}=[1-(-1)^k][1-(-1)^l]/(kl\pi^2)\).
2. production S_y basis replaced by exact traction-orthogonal transform
   \(\widetilde B_{S_y}=B_{S_y}^{raw}-c_{kl}B_{E_y}\).
3. equilibrium load renamed \(P_{eq}\); final load is \(P_{report}=\chi_wP_c+P_s^++P_s^-\).
4. final peak criterion changed to \(dP_{report}/dq=0\).
5. raw dimensional Jacobian condition number replaced by scaled diagnostics.

numerical result:
- zero-load max loading strain = 0;
- TOP/BOTTOM parity error = 5.421011e-20;
- external-work derivative error = 4.262074e-10;
- full Jacobian FD max scaled relative error = 3.862825e-06;
- physics-shaped Schur outer difference = 2.273737e-13.

gate status:
- M7 PASS after exact local corrections.

unresolved issue:
- production UHPC tensile polynomial values and Q355 polynomial coefficients must be recovered/frozen before M8; do not fit Pu.

NEXT_ACTION:
- recover formal M8 material/geometric input from Project/Library/repository and run connected q-path.
