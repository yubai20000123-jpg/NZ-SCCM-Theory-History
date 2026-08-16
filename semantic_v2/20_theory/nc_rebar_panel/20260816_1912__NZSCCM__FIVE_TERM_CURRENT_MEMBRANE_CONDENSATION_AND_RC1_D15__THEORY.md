# NZ-SCCM — 五项 current-material 膜内凝聚与 RC1/General-D15 目标泛函接口

**时间：2026-08-16 19:12 +08:00**  
**门禁：`UNIFIED_V1_CURRENT_MATERIAL_FIVE_TERM_MEMBRANE_CONDENSATION_PLUS_RC1_D15_GATE`**

## 0. 结论先行

本轮把 18:48 已经识别的五个相容膜内位移分量正式写成有限内部坐标，并完成三件事：

1. **精确闭合线弹性五坐标凝聚**，严格恢复上一门禁得到的 Airy/FvK 膜应力重分布；
2. **证明五个膜内残量与既有 `P,Rq,L,KZ` 都属于同一 General-D15 目标泛函接口**，不需要任何空间积分点；
3. **给出 R10+钢筋 current-material 的一致残量、切线和 Schur 凝聚公式**。

但是，`R10-MSAC-RC1` 的高阶 nested beta-lens/Chebyshev 图尚未真正接入一个可运行的 adjoint-Clenshaw/Qnm General-D15 target-functional backend。因此本门禁只能判为：

```text
FIVE_TERM_ELASTIC_CONDENSATION = PASS_EXACT
FIVE_TERM_AIRY_FVK_RECOVERY = PASS_EXACT
FIVE_TERM_GENERAL_D15_TARGET_CLOSURE = PASS
CURRENT_MATERIAL_RESIDUAL_AND_CONDENSATION_FORM = PASS_FORMAL
LEGACY_N48_CURRENT_MATERIAL_DIAGNOSTIC = EXECUTED_FAIL_FAST_ONLY
RC1_NESTED_TARGET_FUNCTIONAL_RUNTIME = OPEN
NEW_MEMBRANE_REDISTRIBUTED_Pu = NOT_RUN
OVERALL_GATE = PARTIAL_PASS_TO_IMPLEMENTATION_BOUNDARY
```

这里没有用试验值、Zhou、Winter 或历史 Pu 选择任何系数或根。

---

# 1. 全局未知量与五个内部膜坐标

全局结构坐标继续保持

\[
\boxed{g=(D,q)},\qquad A=bq.
\]

对当前 square complete halfwave `ell=b`，定义

\[
X=\pi x/b,\qquad Y=\pi y/b,
\]

以及五个**内部响应坐标**

\[
\boxed{r=(r_0,r_{20},r_{22},s_{02},s_{22})^T}.
\]

采用如下相容位移定义：

\[
u_0=\varepsilon_0r_0x,
\]

\[
u_{20}=\varepsilon_0\frac{b}{2\pi}r_{20}\sin2X,
\]

\[
u_{22}=\varepsilon_0\frac{b}{2\pi}r_{22}\sin2X\cos2Y,
\]

\[
v_{02}=\varepsilon_0\frac{b}{2\pi}s_{02}\sin2Y,
\]

\[
v_{22}=\varepsilon_0\frac{b}{2\pi}s_{22}\cos2X\sin2Y.
\]

对应归一化工程应变基为

\[
B_0=(1,0,0),
\]

\[
B_{20}=(\cos2X,0,0),
\]

\[
B_{u22}=(\cos2X\cos2Y,0,-\sin2X\sin2Y),
\]

\[
B_{02}=(0,\cos2Y,0),
\]

\[
B_{v22}=(0,\cos2X\cos2Y,-\sin2X\sin2Y).
\]

因此

\[
\boxed{e(D,q,r,\zeta)=e^{old}_{Nguyen}(D,q,\zeta)+\sum_{j=1}^{5}r_jB_j}.
\]

这五个坐标不是新的全局 Pu 求解维数。它们必须先由面内平衡求解并一致凝聚，随后外层仍回到 `(D,q)`。

---

# 2. 精确线弹性凝聚

令

\[
M=\frac{\pi^2}{\varepsilon_0}\left(q_0q+\frac12q^2\right).
\]

square halfwave 的旧 Nguyen 中面几何膜场对单位 `M` 可写为

\[
e_M=
\left(
\frac{1+c_X-c_Y-c_Xc_Y}{4},
\frac{1-c_X+c_Y-c_Xc_Y}{4},
\frac12s_Xs_Y
\right),
\]

其中

\[
c_X=\cos2X,\quad c_Y=\cos2Y,
\quad s_X=\sin2X,\quad s_Y=\sin2Y.
\]

轴压基为

\[
e_D=(\nu,-1,0).
\]

采用各向同性平面应力无量纲双线性型

\[
\langle e,f\rangle_\nu=
\int_0^\pi\int_0^\pi
\left[e_xf_x+e_yf_y+\nu(e_xf_y+e_yf_x)
+\frac{1-\nu}{2}g_eg_f\right]dX\,dY.
\]

定义

\[
K_{ij}=\langle B_i,B_j\rangle_\nu,
\qquad
(f_M)_i=\langle B_i,e_M\rangle_\nu,
\qquad
(f_D)_i=\langle B_i,e_D\rangle_\nu.
\]

全部积分解析化后得到

\[
\boxed{
\frac{K}{\pi^2}=
\begin{bmatrix}
1&0&0&0&0\\
0&1/2&0&0&0\\
0&0&(3-\nu)/8&0&(1+\nu)/8\\
0&0&0&1/2&0\\
0&0&(1+\nu)/8&0&(3-\nu)/8
\end{bmatrix}}
\]

以及

\[
\boxed{
\frac{f_M}{\pi^2}=
\begin{bmatrix}
(1+\nu)/4\\
(1-\nu)/8\\
-1/8\\
(1-\nu)/8\\
-1/8
\end{bmatrix}},
\qquad
\boxed{f_D=0}.
\]

矩阵行列式为

\[
\boxed{\det K=\frac{\pi^{10}}{32}(1-\nu)}.
\]

对物理范围 `nu<1`，五坐标系统非奇异。其无量纲特征值为

\[
\boxed{1,\;1/2,\;1/2,\;1/2,\;(1-\nu)/4}.
\]

对当前普通混凝土 `nu=.18`：

```text
K/pi^2 =
[[1,     0,      0,     0,      0],
 [0,   .5,      0,     0,      0],
 [0,     0,  .3525,     0,  .1475],
 [0,     0,      0,    .5,      0],
 [0,     0,  .1475,     0,  .3525]]

eigenvalues = [.205,.5,.5,.5,1]
cond_2(K)=4.87804878049
```

故线弹性内部平衡

\[
Kr+Mf_M+Df_D=0
\]

精确给出

\[
\boxed{
\frac rM=
\begin{bmatrix}
-(1+\nu)/4\\
-(1-\nu)/4\\
1/4\\
-(1-\nu)/4\\
1/4
\end{bmatrix}}
\]

即

\[
r_0=-\frac{1+\nu}{4}M,
\quad
r_{20}=s_{02}=-\frac{1-\nu}{4}M,
\quad
r_{22}=s_{22}=\frac14M.
\]

这与 18:48 从 Airy/FvK 直接反推的五个位移分量逐项一致。

---

# 3. Airy/FvK 应力恢复检查

把上述精确 `r` 代回旧 Nguyen 膜场，得到

\[
e_x^{red}=\nu D-\frac{\nu M}{4}
+\frac M4(\nu\cos2X-\cos2Y),
\]

\[
e_y^{red}=-D+\frac M4
+\frac M4(-\cos2X+\nu\cos2Y),
\]

\[
g^{red}=0.
\]

平面应力关系给出

\[
\boxed{\frac{\sigma_x}{E\varepsilon_0}=-\frac M4\cos2Y},
\]

\[
\boxed{\frac{\sigma_y}{E\varepsilon_0}=-D+\frac M2\sin^2X}
=
-D+\frac M4(1-\cos2X),
\]

\[
\boxed{\tau_{xy}=0}.
\]

这正是一个 complete halfwave 上由兼容方程得到的经典 Airy/FvK 重分布结构。因此：

```text
FIVE_TERM_ELASTIC_LIMIT_TO_AIRY = EXACT
D_FORCING_OF_INTERNAL_MODES = ZERO
q->0 => M->0 => r->0
```

---

# 4. R10 + reinforcement 的 current-material 方程

线弹性 Airy 系数只用于 limit benchmark，不能在 R10 非线性材料中直接固定。

对 concrete：

\[
\sigma_c=\mathcal M_{R10}(\varepsilon),
\]

对每一钢筋层/方向：

\[
\sigma_s=\mathcal M_s(\varepsilon_s),
\qquad
\varepsilon_s=n^TEn.
\]

五个 current membrane residual 统一写成

\[
\boxed{
R_{m,j}(D,q,r)=
\sum_p\int_{V_p}\sigma_p:B_j\,dV=0,
\qquad j=1,\ldots,5.}
\]

这里 `p` 同时包含 concrete 与 reinforcement phases；钢筋不是求完 concrete 后再附加。

一致 current tangent：

\[
\boxed{K_{rr}=\frac{\partial R_m}{\partial r}}
\]

必须由同一 current state 的材料切线生成。

令 `g=(D,q)`，内部坐标导数为

\[
\boxed{r_{,g}=-K_{rr}^{-1}R_{m,g}}.
\]

因此凝聚后的外层导数为

\[
\boxed{\bar P_g=P_g+P_r r_{,g}},
\]

\[
\boxed{\bar R_{q,g}=R_{q,g}+R_{q,r}r_{,g}},
\]

以及

\[
\boxed{
\bar L=
\bar P_D\bar R_{q,q}
-\bar P_q\bar R_{q,D}.}
\]

外层极限点拓扑仍为

\[
\boxed{\bar R_q(D,q)=0,\qquad \bar L(D,q)=0}
\]

沿 origin-connected primary branch 的第一个 `+->-` maximum。

对于同一状态的稳定切线，内部膜坐标的静力凝聚采用

\[
\boxed{K_{gg}^{cond}=K_{gg}-K_{gr}K_{rr}^{-1}K_{rg}}.
\]

因此五项膜重分布没有引入第二套 Pu solver，也没有改变当前 Zhou/Navier tangent 的身份。

---

# 5. 五个残量全部属于 General-D15

令

\[
u=\sin X,\qquad v=\sin Y.
\]

则

\[
\cos2X=1-2u^2,
\qquad
\cos2Y=1-2v^2,
\]

\[
\cos2X\cos2Y=(1-2u^2)(1-2v^2).
\]

两个 `22` 基的 shear kernel 为

\[
-\sin2X\sin2Y=-4uv\cos X\cos Y.
\]

R10 的二维 isotropic spectral map 经 Cayley-Hamilton 总可写成

\[
S=A(I_1,I_2)I+B(I_1,I_2)Y.
\]

其中 shear stress 满足

\[
S_{xy}=B\,Y_{xy}\propto B\,g_{xy}.
\]

因此在 `22` 膜残量中，shear scalar work 包含

\[
S_{xy}[-\sin2X\sin2Y]
\propto
g_{xy}\sin2X\sin2Y.
\]

当前 Nguyen + 五项修正的 `g_xy` 都含有 `cosX cosY` 因子，所以相乘后只剩 `cos^2X cos^2Y`，再利用

\[
\cos^2X=1-\sin^2X,
\qquad
\cos^2Y=1-\sin^2Y
\]

即可回到有限整数三角/厚度多项式。

故五个 concrete target kernels 可写为

\[
\mathcal T_0[S]=\mathscr D[S_{xx}],
\]

\[
\mathcal T_{20}[S]=\mathscr D[S_{xx}\cos2X],
\]

\[
\mathcal T_{u22}[S]=\mathscr D[S_{xx}\cos2X\cos2Y-S_{xy}\sin2X\sin2Y],
\]

\[
\mathcal T_{02}[S]=\mathscr D[S_{yy}\cos2Y],
\]

\[
\mathcal T_{v22}[S]=\mathscr D[S_{yy}\cos2X\cos2Y-S_{xy}\sin2X\sin2Y].
\]

它们与现有

```text
P target
Rq target
same-expression derivative targets
KZ material target
KZ geometric target
```

属于同一个 `target kernel -> General-D15 exact moment` 接口。

因此：

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
FIVE_TERM_SPATIAL_CELLS = 0
```

---

# 6. RC1 nested compiler 应如何接入

`R10-MSAC-RC1` 当前是 nested factor graph，不能先展开成几万阶普通多项式再交给 D15。

正确接口不是

```text
RC1 -> giant full stress polynomial -> D15
```

而是

```text
state (D,q,r)
 -> low-order Nguyen/in-plane invariant fields
 -> RC1 nested spectral primitives
 -> Cayley-Hamilton matrix lift
 -> target-functional contraction
 -> General-D15 exact moments
 -> [P,Rq,Rm1...Rm5,KZ]
```

定义目标泛函

\[
\boxed{\mathcal L_K[F]=\mathscr D[K:F]}.
\]

每一个五项膜残量只是换了一个有限低阶 `K`；材料 operator 本身不变。

对于一个 Chebyshev matrix stage

\[
T_n(Y)=A_nI+B_nY,
\]

二维 CH recurrence 仍是

\[
A_{n+1}=-2I_2(Y)B_n-A_{n-1},
\]

\[
B_{n+1}=2[A_n+I_1(Y)B_n]-B_{n-1}.
\]

生产实现应把 recurrence **直接作用在所需 target functional 上**，或用等价的 `Q_nm`/adjoint-Clenshaw moment table，使每一层 nested map 都保持因子化；不得 materialize 全空间 stress polynomial。

这一接口在数学上已经闭合，但本轮没有把 `R10-MSAC-RC1` 的 `Ng=512...1152 / Nc=14...16 / Nt=256...576` nested 图真正执行到五个结构 target 上。因此不能声称 `RC1_NESTED_TARGET_FUNCTIONAL_RUNTIME=PASS`。

---

# 7. Case21 / Z6 五项弹性 benchmark 幅值

仅用已经冻结的状态计算 benchmark，不是新 Pu。

对 `nu=.18`：

\[
\frac rM=(-.295,-.205,.25,-.205,.25).
\]

Case21 historical/current-support state `M=.02869338081034484`：

```text
r0   = -.00846454733905
r20  = -.00588214306612
r22  = +.00717334520259
s02  = -.00588214306612
s22  = +.00717334520259
```

对应位移尺度：

```text
u0 across full width = -0.0215829 mm
u20 amplitude         = -0.00238705 mm
u22 amplitude         = +0.00291104 mm
v02 amplitude         = -0.00238705 mm
v22 amplitude         = +0.00291104 mm
```

Z6 retained engineering-baseline state `M=1.6948726156196714`：

```text
r0   = -.499987421608
r20  = -.347448886202
r22  = +.423718153905
s02  = -.347448886202
s22  = +.423718153905
```

对应位移尺度：

```text
u0 across full width = -11.2272 mm
u20 amplitude         = -1.24172 mm
u22 amplitude         = +1.51429 mm
v02 amplitude         = -1.24172 mm
v22 amplitude         = +1.51429 mm
```

这些值再次显示：Case21 的经典重分布尺度很小，而 Z6 可能进入明显的 current-material coupling 区域；但这仍不是 Z6 误差因果证明。

---

# 8. 旧 N48 current-material fail-fast 诊断

为了验证“弹性 benchmark 系数不能直接当非线性 R10 解”，本轮在**历史 Case21 状态**上用旧 N48-C1 coefficient-space CH/D15 kernel 做了一次隔离诊断。此诊断不属于 RC1 production。

在 classical `r` 处，定义缩放后的五残量

\[
\widehat R_m=\frac{\pi^2}{\varepsilon_0b\ell t}R_m.
\]

得到

```text
Rhat = [
 +2.69233687,
 +0.13819441,
 -0.31339370,
 -15.52815375,
 +3.00791537
]
```

其中 concrete / rebar 分量分别为

```text
concrete = [+.38452432,+.12820657,-.31339370,-15.53814159,+3.00791537]
rebar    = [+2.30781255,+.00998784,~0,+.00998784,~0]
```

所以 nonlinear RC current state 下，classical elastic `r` 显然**不是** current membrane-equilibrium root，这正是需要重新求 `R_m=0` 的原因。

随后只做了一次 generalized-coordinate finite-difference Newton diagnostic。局部 5x5 Jacobian condition number 约 `8.53e2`，第一步给出非常大的 `r22/s22` 改变量，明显不适合作为当前生产推进依据；而该 kernel 又不是当前 RC1。因此按 fail-fast 纪律立即停止，没有继续用旧 N48 求一个伪“新 Pu”。

```text
OLD_N48_FIVE_R_CURRENT_DIAGNOSTIC = STOPPED
USE_IT_AS_CURRENT_RC1_PRODUCTION = NO
```

---

# 9. 本门禁与下一门禁

本轮已经把理论结构压缩到一个非常清楚的实现问题：

```text
global solve remains (D,q)
five current membrane coordinates are finite internal variables
elastic limit is exactly verified
all five residuals are General-D15 target functionals
current residual/tangent/Schur formulas are fixed
```

唯一没有完成的是：**让 nested RC1 真正接受任意 target kernel 并返回 exact General-D15 contraction。**

因此当前唯一下一门禁为

```text
UNIFIED_V1_RC1_ADJOINT_CLENSHAW_GENERAL_D15_TARGET_FUNCTIONAL_EXECUTION_GATE
```

通过条件：

1. 同一个 RC1 nested graph 对 `P,Rq,Rm1...Rm5` target 全部工作；
2. 不展开 full stress field；
3. 不使用空间 Gauss/Simpson/adaptive/collocation/material-point grid；
4. 在低阶可直接展开的测试上与 direct General-D15 严格一致；
5. 在 Z0-Z6 RC1 第一通过层上给出时间、内存、moment-state count；
6. 只有该 backend 通过后，才允许真正解 `r(D,q)`、再解凝聚后的 `Rq=0,L=0` 并发布新的 Pu。
