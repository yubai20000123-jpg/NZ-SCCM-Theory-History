# UCFT 低维全过程半解析理论 当前状态

更新时间：2026-09-30 15:23 +08:00

## 1. 最高层级合同

当前最高优先级路线合同：用户上传《指示词(3).md》。

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

## 11. NEXT_ACTION

严格进入 M5：

\[
\boxed{
\text{steel Mises deformation theory}
+\text{equivalent uniaxial polynomial}
+E_{sec}/E_{tan}
+\text{analytic elastic/plastic thickness active-set}
}
\]

保持 \(\varepsilon_i^2=C_2\zeta^2+C_1\zeta+C_0\)，屈服边界由二次方程解析求根、排序、分区积分；finite current stress 与 tangent 严格分离。