# NZ-SCCM Case21 多数学后端 direct-analytic 执行结果

**日期：2026-08-09**  
**执行对象：Case21 concrete-only → RC Case21**  
**理论合同：`NZ_SCCM_CURRENT_OPERATOR_EXPLICIT_NC_REBAR_V1_20260809.md`**  
**机器辅助参考：`nz_sccm_current_operator_explicit_v1.py`**

> 最终状态先行说明：本轮已经把冻结的显式 NC current operator、Case21 连续运动学、`Pc/Rq,c` 和钢筋耦合真正跑到了 concrete-only 与 RC 的极限方程解；正式空间 Gauss/Simpson/adaptive quadrature 数为 **0**。但是，当前运行环境未能关闭“临时实际 integrand Chebyshev 表达的有用严格截断余项证书”。因此数值解已经得到，且与独立高阶数值 audit 高度闭合，但按本轮用户定义的最高成功标准，整体状态记为：
>
> `FORMAL_ANALYTIC_CANDIDATE_CERTIFICATE_UNRESOLVED`。
>
> 不能把它伪报为“完全 certified production SUCCESS”。

---

## A. Theory contract check

### A.1 冻结文件身份

上传文件 SHA-256：

- MD：`98483fa75e828f57916b06fc708fc35fc7960fabbdebf4edb3e04aba10061bc6`
- Python：`740e8862b1f428e66c779ea17c2ffefdec1f53ae7da5b98f9d85669ea24811c2`

### A.2 MD > Python 检查

逐项核查结论：

1. Python 中 `nc_parameters`、`Pi_eta`、`foster_H`、`nc_principal_response`、`M_NC` 与 MD 第1节 ordinary-concrete current operator 一致；
2. Python 中正式 tension smoothing 明确是代数 Foster：

\[
H(r,r_0)=\frac12[(r-r_0)+\sqrt{(r-r_0)^2+0.05^2}]
-\frac12[-r_0+\sqrt{r_0^2+0.05^2}],
\]

没有 `tanh` 双 sigmoid；
3. Python 中钢筋 `Es=200000 MPa`、`eps_y=0.00265`、`fy=530 MPa`、`Ew=0`、`eps_f=0.04` 与 MD 一致；
4. Python 文件只提供材料函数和 Case21 材料参数，不含 MD 第2--6节的 Case21 结构运动学、`Pc`、`Rq,c` 与钢筋结构积分。这属于**机器文件范围更窄**，不是理论冲突；本轮结构部分严格取 MD。

**CONTRACT_CHECK = PASS。**

---

# B. Exact \(M_{NC}\) expression identity

本轮没有把 ordinary concrete 再缩写为隐藏的 `M(eps)`。计算链实际使用：

\[
(\varepsilon_x,\varepsilon_y,\gamma_{xy})
\rightarrow
(X_{11},X_{22},X_{12})
\rightarrow
(\lambda_+,\lambda_-)
\rightarrow
(c_\pm,t_\pm)
\rightarrow
(C_\pm,T_\pm,U_\pm)
\rightarrow
(s_+,s_-)
\rightarrow
(\sigma_x,\sigma_y,\tau_{xy}).
\]

## B.1 Equivalent-uniaxial tensor

\[
X_{11}=\frac{\varepsilon_x+\nu\varepsilon_y}{(1-\nu^2)\varepsilon_0},
\qquad
X_{22}=\frac{\nu\varepsilon_x+\varepsilon_y}{(1-\nu^2)\varepsilon_0},
\]

\[
X_{12}=\frac{\gamma_{xy}}{2(1+\nu)\varepsilon_0}.
\]

\[
\mu=\frac{X_{11}+X_{22}}2,
\quad
\delta=\frac{X_{11}-X_{22}}2,
\quad
r_X=\sqrt{\delta^2+X_{12}^2},
\]

\[
\lambda_\pm=\mu\pm r_X.
\]

## B.2 Smooth positive/negative coordinates

\[
\Pi_\eta(z)=
\frac{z^2(\sqrt{z^2+\eta^2}+z)}{2(z^2+\eta^2)},
\]

\[
c_i=\Pi_\eta(-\lambda_i),\qquad t_i=\Pi_\eta(\lambda_i).
\]

## B.3 Saenz compression

\[
C_i=\frac{\kappa c_i}{1+(\kappa-2)c_i+c_i^2}.
\]

## B.4 Algebraic Foster tension

\[
\eta_r=0.05,\qquad m_t=-\frac7{90},
\]

\[
H(r,r_0)=
\frac12[(r-r_0)+\sqrt{(r-r_0)^2+\eta_r^2}]
-\frac12[-r_0+\sqrt{r_0^2+\eta_r^2}],
\]

\[
r_i=\frac{t_i}{x_{cr}},
\]

\[
T_i=r_i+(m_t-1)H(r_i,1)-m_tH(r_i,10).
\]

## B.5 Uniaxial current master

\[
U_i=\kappa\lambda_i-C_i+\kappa c_i+\rho T_i-\kappa t_i.
\]

## B.6 CC/TC/TT interaction encoded in the frozen algebraic interaction

\[
s_+=U_+-a_{cc}C_+^2C_-+C_+T_--\rho a_tT_+T_-^8,
\]

\[
s_-=U_--a_{cc}C_-^2C_++C_-T_+-\rho a_tT_-T_+^8.
\]

## B.7 Spectral return

\[
S_{xx}=\frac{s_++s_-}{2}+\frac{s_+-s_-}{2}\frac{\delta}{r_X},
\]

\[
S_{yy}=\frac{s_++s_-}{2}-\frac{s_+-s_-}{2}\frac{\delta}{r_X},
\]

\[
S_{xy}=\frac{s_+-s_-}{2}\frac{X_{12}}{r_X},
\]

\[
\sigma_x=f_cS_{xx},\quad
\sigma_y=f_cS_{yy},\quad
\tau_{xy}=f_cS_{xy}.
\]

在本轮两个极限状态邻域，直接计算得到的最小谱半径约为 0.3 量级，因此没有触发 `r_X=0` 的连续延拓分支。

机器实现与上传 SymPy `M_NC` 在三组随机连续应变状态逐点对照，最大绝对应力差为约 `2.2e-14 MPa`，说明本轮 NumPy 直接表达没有改写材料物理。

---

# C. Exact reinforcement law

\[
E_s=200000\ \mathrm{MPa},\quad
\varepsilon_y=0.00265,
\quad f_y=530\ \mathrm{MPa},
\]

\[
E_w=0,\qquad \varepsilon_f=0.04.
\]

在来源定义区间：

\[
\sigma_s(\varepsilon_s)=
\begin{cases}
E_s\varepsilon_s,& |\varepsilon_s|\le\varepsilon_y,\\
f_y\operatorname{sgn}(\varepsilon_s),&
\varepsilon_y<|\varepsilon_s|\le\varepsilon_f.
\end{cases}
\]

不添加 \(|\varepsilon_s|>0.04\) 的 post-failure branch。

Case21：

\[
\rho_{s,x}=\rho_{s,y}=0.00375,
\qquad z_s=0.
\]

---

# D. Case21 \(P_c/R_{q,c}\)

## D.1 specimen data

本轮结构输入：

\[
b=\ell=1220\ \mathrm{mm},
\qquad t=19.30\ \mathrm{mm},
\]

\[
A_0=b/400=3.05\ \mathrm{mm},
\qquad q_0=1/400.
\]

材料：

\[
f_c=21.23\ \mathrm{MPa},
\quad E_0=20321\ \mathrm{MPa},
\quad \varepsilon_0=0.00209,
\quad \nu=0.18.
\]

## D.2 continuous Nguyen strain field

\[
C_m=\frac{\pi^2}{\varepsilon_0}\left(q_0q+\frac12q^2\right),
\]

\[
C_b=\frac{\pi^2}{2\varepsilon_0}\frac tbq.
\]

\[
e_x=\nu D+C_m\cos^2X\sin^2Y+C_b\sin X\sin Y\,\zeta,
\]

\[
e_y=-D+C_m\sin^2X\cos^2Y+C_b\sin X\sin Y\,\zeta,
\]

\[
g_{xy}=2C_m\sin X\cos X\sin Y\cos Y-2C_b\cos X\cos Y\,\zeta.
\]

\[
\varepsilon_x=\varepsilon_0e_x,
\quad
\varepsilon_y=\varepsilon_0e_y,
\quad
\gamma_{xy}=\varepsilon_0g_{xy}.
\]

## D.3 formal targets

\[
P_c(D,q)=
-\frac{bt}{2\pi^2}
\int_0^\pi\int_0^\pi\int_{-1}^{1}\sigma_y\,d\zeta\,dY\,dX,
\]

\[
R_{q,c}(D,q)=
\frac{\varepsilon_0b\ell t}{2\pi^2}
\int_0^\pi\int_0^\pi\int_{-1}^{1}
[\sigma_xe_{x,q}+\sigma_ye_{y,q}+\tau_{xy}g_{xy,q}]
\,d\zeta\,dY\,dX.
\]

`N_formal_spatial_quadrature = 0`。

---

# E. Actual tools / repositories used or checked

| backend | local status | actual action | outcome |
|---|---|---|---|
| SymPy 1.14.0 | installed | built full frozen near-peak `sigma_y` and called direct definite `zeta` integration | expression had 43,641 operations; no return within 25 s |
| SciPy 1.17.0 + NumPy 2.3.5 | installed | DCT-I construction of a transient Chebyshev expression for the **actual structural integrands**, exact Chebyshev moments, complex-step scalar derivatives, nonlinear root solve | returned stable concrete and RC candidates |
| mpmath 1.3.0 | installed | 80-digit direct current-operator evaluation | returned and agreed with double implementation |
| mpmath.iv | installed | attempted rigorous interval derivative/range certificate | natural interval dependency became too wide; rejected as useful certificate |
| Symbolica-integrate / Rubi | repository/API checked | install/run attempted conceptually; local Rust/cargo absent and no package in local Python mirror | not executable here |
| SageMath | docs checked | executable discovery | not installed |
| GIAC/Xcas | repository checked | executable discovery | not installed |
| Maxima | docs checked | executable discovery | not installed |
| python-flint / Arb | upstream package checked | pip installation attempted from local mirror and public PyPI | local mirror absent; public DNS/network blocked; not executable |

因此本轮没有把“SymPy 卡住”误判为解析路线失败；实际继续使用了独立的 SciPy/NumPy polynomial mathematics 和 mpmath 高精度/interval 后端。

---

# F. Integration transformation trace

## F.1 Direct CAS attempt

原始目标先直接送入 SymPy。完整 `sigma_y` 在固定 near-peak 状态构造后约 43,641 个 SymPy operations。直接：

\[
\int_{-1}^{1}\sigma_y\,d\zeta
\]

在 25 s 限时内没有返回，因此该后端被记录为 `EXECUTED_TIMEOUT`，而不是理论失败。

## F.2 Rejected global \(q=0\) Taylor route

曾对实际 integrand 尝试从 \(q=0\) 展开。由于 frozen smooth coordinate 中存在

\[
\sqrt{\lambda^2+\eta^2},
\]

其复平面邻近奇点尺度由很小的 \(\eta\) 控制，实际 \(q\approx2\times10^{-3}\) 已超出该简单中心展开的有效实用范围；有限阶系数迅速放大。该路线被废弃，不进入正式结果。

## F.3 Temporary actual-integrand Chebyshev expression

只对当前两个**结构 integrand**：

\[
f_P=\sigma_y,
\]

\[
f_R=\sigma_xe_{x,q}+\sigma_ye_{y,q}+\tau_{xy}g_{xy,q}
\]

作一次性有限解析表示。

线性映射：

\[
u=\frac{2X}{\pi}-1,
\qquad
v=\frac{2Y}{\pi}-1,
\qquad
w=\zeta,
\]

令：

\[
f_N(u,v,w)
=
\sum_{i=0}^{N_x}\sum_{j=0}^{N_y}\sum_{k=0}^{N_z}
 c_{ijk}T_i(u)T_j(v)T_k(w).
\]

本轮最终采用：

\[
N_x=N_y=112,\qquad N_z=56.
\]

这些系数只属于“当前 `(D,q)` 下当前实际结构 integrand 的瞬时多项式表达”；每次函数评价后即可丢弃：

- 不是 material coefficient；
- 不是 material common domain；
- 不是 support mask；
- 不是 PTDC；
- 不持久化；
- 不用于其他板或其他材料身份。

Chebyshev 基的精确矩：

\[
I_n=\int_{-1}^{1}T_n(s)\,ds
=
\begin{cases}
2,&n=0,\\
0,&n\ \text{odd},\\
\dfrac{2}{1-n^2},&n\ge2\ \text{even}.
\end{cases}
\]

因此：

\[
\int_0^\pi\int_0^\pi\int_{-1}^{1}f_N\,d\zeta dYdX
=
\frac{\pi^2}{4}
\sum_{ijk}c_{ijk}I_iI_jI_k.
\]

**正式积分阶段只有有限项闭式矩求和；没有任何 Gauss/Simpson/adaptive 权重。**

---

# G. Formal analytic evaluator

本轮得到两个可直接、快速评价的有限表达 evaluator：

\[
P_{c,N}(D,q),\qquad R_{q,c,N}(D,q).
\]

参数偏导不是通过空间差分得到；对已经完成空间解析收缩的 evaluator 使用 complex-step：

\[
P_{,D},\ P_{,q},\ R_{q,D},\ R_{q,q}.
\]

极限函数：

\[
L=P_{,D}R_{q,q}-P_{,q}R_{q,D}.
\]

正式求解器只调用上述 Chebyshev-moment evaluator，不调用下面的 numerical audit。

---

# H. Error / remainder certificate

## H.1 Independent numerical audit: PASS as audit only

采用原始显式 current operator 直接高阶 3D Gauss-Legendre，**仅在 formal root 已经得到后**独立核对。

Concrete-only 最终点：

- formal candidate: `338.318378991 kN`
- Gauss-96 audit: `338.317391831 kN`
- formal − audit: `+0.0002918%`

RC 最终点：

- formal candidate: `342.333946949 kN`
- Gauss-96 audit: `342.332787283 kN`
- formal − audit: `+0.0003388%`

这说明瞬时 finite Chebyshev expression 与冻结原函数的直接空间评价数值上已经闭合到约 \(3\times10^{-4}\%\)。

## H.2 Strict truncation certificate: NOT CLOSED

这里必须严格区分“数值高度一致”和“严格余项证书”。

已实际尝试：

1. `mpmath.iv` natural interval extension；
2. 为 Chebyshev 误差构造 interval derivative/range 上界；
3. 尝试安装 `python-flint/Arb` 作为 ball-arithmetic certificate backend。

结果：

- `mpmath.iv` 对嵌套谱分解、Foster 平滑和重复变量的 natural interval dependency 产生了过宽包络，无法给出有用的高阶导数/余项上界；
- `python-flint/Arb` 在本运行环境无法安装；
- 可以写出一个非常松的全局绝对包络，但其上界达到远大于结构荷载的量级，不能作为有效验收证书，因此本报告拒绝把它包装成“PASS”。

故：

`STRICT_TRUNCATION_REMAINDER_CERTIFICATE = UNRESOLVED`。

这也是本轮唯一阻止“fully certified production”身份的数学项。

---

# I. Concrete-only Case21 solution

正式方程：

\[
R_{q,c}(D,q)=0,
\]

\[
L_c(D,q)
=P_{c,D}R_{q,c,q}-P_{c,q}R_{q,c,D}=0.
\]

在与 \(q\to0^+\) 初始缺陷路径连续连接的正幅值平衡支上得到：

\[
\boxed{D_{u,c}=0.7927267495},
\]

\[
\boxed{q_{u,c}=0.002027009958},
\]

\[
\boxed{A_{u,c}=bq=2.472952149\ \mathrm{mm}},
\]

\[
\boxed{P_{c,u}=338.318378991\ \mathrm{kN}}.
\]

formal residual：

\[
R_{q,c}\approx-3.1\times10^{-11},
\]

\[
L_c\approx-4.6\times10^{-5}
\]

（相对于内部导数量级已接近数值零）。

### 与历史 D15 比较

历史：

\[
P_{u,c}^{D15}\approx339.1\ \mathrm{kN}.
\]

新 direct candidate：

\[
338.318379\ \mathrm{kN},
\]

差：

\[
-0.23050\%.
\]

因此新 direct-analytic current-operator 求解与历史 D15 在约 0.23% 内一致，但**不是完全相同数值**。

历史资料还曾给出约 `339.6 kN` 的独立 quadrature audit；本轮严格按当前上传 MD 的完整显式 operator 重新做 Gauss-96 audit 得到 `338.3174 kN`，与旧 `339.6 kN` 相差约 `1.283 kN`（约 `-0.378%`）。因此旧 audit 的具体执行身份/材料近似版本需要单独追溯；本轮没有用旧 339.6 去调任何参数。

---

# J. Reinforcement integration

## J.1 Reachable RC branch is entirely elastic

由于 Case21 钢筋位于 \(z_s=0\)，两方向连续应变为：

\[
\varepsilon_{s,x}
=\varepsilon_0[\nu D+C_m\cos^2X\sin^2Y],
\]

\[
\varepsilon_{s,y}
=\varepsilon_0[-D+C_m\sin^2X\cos^2Y].
\]

RC 极限点的精确范围：

\[
\varepsilon_{s,x}\in
[0.0002653711,\ 0.0003432177],
\]

\[
\varepsilon_{s,y}\in
[-0.0014742840,\ -0.0013964374].
\]

而：

\[
\varepsilon_y=0.00265.
\]

所以：

\[
\boxed{\max|\varepsilon_s|=0.001474284<0.00265}.
\]

整块 RC 极限状态的 x/y 钢筋均处于 Nguyen bilinear law 的第一段，不存在 \(\varepsilon_s=\pm\varepsilon_y\) 事件。因此本轮真实可达 RC 极限无需做分段事件切割；钢筋积分可以**直接闭式**完成。

## J.2 Exact steel contributions

令：

\[
S=q_0q+\frac12q^2,
\qquad
C_m=\frac{\pi^2S}{\varepsilon_0}.
\]

加载方向钢筋轴力：

\[
\boxed{
P_s
=\rho_{s,y}tbE_s\varepsilon_0
\left(D-\frac{C_m}{4}\right)/1000
}
\]

单位 kN。

两方向钢筋共同进入幅值残量：

\[
\boxed{
R_{q,s}
=
\rho_stE_s\pi^2(q_0+q)b\ell
\left[
\frac{\varepsilon_0D(\nu-1)}4
+\frac{9\pi^2S}{32}
\right].
}
\]

该式没有钢筋 Gauss points，也不是 \(A_sf_y\) 峰后追加。

---

# K. RC Case21 solution

总体系：

\[
P=P_c+P_s,
\qquad
R_q=R_{q,c}+R_{q,s}.
\]

极限方程：

\[
R_q=0,
\]

\[
L=P_{,D}R_{q,q}-P_{,q}R_{q,D}=0.
\]

同一可达正幅值平衡支重新求解得到：

\[
\boxed{D_u=0.7053990246},
\]

\[
\boxed{q_u=0.002193082030},
\]

\[
\boxed{A_u=2.675560077\ \mathrm{mm}}.
\]

分项：

\[
\boxed{P_c=316.642512331\ \mathrm{kN}},
\]

\[
\boxed{P_s=25.691434617\ \mathrm{kN}},
\]

\[
\boxed{P_u=342.333946949\ \mathrm{kN}}.
\]

formal residual：

\[
R_q\approx-4.37\times10^{-9},
\]

\[
L\approx-5.34\times10^{-3}.
\]

关键点：

Concrete-only 的峰值混凝土轴力为 `338.3184 kN`；加入钢筋并**重新平衡**后，RC 峰值时混凝土项降为 `316.6425 kN`，减少 `21.6759 kN`；钢筋项为 `25.6914 kN`，所以总极限只净增加：

\[
342.33395-338.31838
=4.01557\ \mathrm{kN}.
\]

这直接证明正式 RC 结果绝不是：

\[
P_{u,c}+A_sf_y.
\]

---

# L. Experiment comparison

试验：

\[
P_{f,exp}=368.312750\ \mathrm{kN}.
\]

新 RC candidate：

\[
P_u=342.333946949\ \mathrm{kN}.
\]

误差：

\[
\boxed{
\frac{342.333946949}{368.312750}-1
=-7.05346\%.
}
\]

因此在当前冻结 NC + Nguyen reinforcement current law 下，RC Case21 仍低估试验约 7.05%。本轮未针对该误差进行任何材料调参、荷载标定或 root 选择。

---

# M. Formal-vs-audit distinction

## M.1 FORMAL_ANALYTIC_CANDIDATE

只允许：

`explicit kinematics -> exact frozen current operator -> transient finite actual-integrand Chebyshev expression -> exact Chebyshev moments -> Pc/Rq -> R=0,L=0`。

正式求根中：

- Gauss points = 0；
- Simpson = 0；
- adaptive quadrature = 0；
- material point grid = 0；
- material-point Newton = 0；
- load-step constitutive history = 0。

## M.2 AUDIT_ONLY_NUMERICAL

只在 formal root 已经得到之后，用原始冻结函数进行独立 Gauss-96 评价：

| case | formal / kN | audit / kN | formal-audit |
|---|---:|---:|---:|
| concrete-only | 338.318379 | 338.317392 | +0.0002918% |
| RC | 342.333947 | 342.332787 | +0.0003388% |

Audit 没有：

- 参与 formal root；
- 生成 Chebyshev 系数；
- 修改材料函数；
- 反标参数。

---

# N. Unresolved items

## N.1 Strict finite-expansion remainder certificate

**唯一正式阻断项。** 当前临时 actual-integrand Chebyshev expression 已数值闭合，但严格、有效、可接受的 truncation remainder bound 尚未由 Arb/python-flint 或其他 validated backend 关闭。

精确失败对象不是笼统的“\(M(\varepsilon)\) 太复杂”，而是：

\[
f_P(X,Y,\zeta;D,q)=\sigma_y
\]

和

\[
f_R(X,Y,\zeta;D,q)
=\sigma_xe_{x,q}+\sigma_ye_{y,q}+\tau_{xy}g_{xy,q}
\]

在当前 transient Chebyshev representation 下的**严格三维截断余项证书**。

## N.2 Historical 339.6 audit identity

当前上传 MD 的原始显式 operator，经本轮独立 Gauss audit 给出约 `338.317 kN`；旧资料中的约 `339.6 kN` 与之差约 0.378%。旧 audit 是否用了不同级数截断、旧材料近似或其他执行细节，需要另行做 evidence-chain audit。本轮没有据此修改当前结果。

## N.3 Disconnected mathematical roots

低阶 formal topology scan 在较高 D 下发现了额外的正/负 q 平衡根。例如 concrete-only 在 D≈0.8 以后出现高幅值根族，另有负 q 根族。这些根不与 `D->0, q->0+` 的 Case21 初始缺陷连续平衡支相连，因此不用于极限承载力选择。当前报告没有把“最大数学根”当作 \(P_u\)。

RC 的高幅值断开根还可能进入钢筋屈服区；因为它们不属于可达主支，本轮没有为这些断开根额外建立钢筋事件分段。

---

# Final execution status

| item | status |
|---|---|
| Frozen explicit NC contract read correctly | PASS |
| Algebraic Foster H, not tanh | PASS |
| Multiple math backends actually exercised | PASS (SymPy + SciPy/NumPy + mpmath; interval attempt also executed) |
| Symbolica/Sage/Giac/Maxima checked | PASS as availability audit; not executable locally |
| Pc direct evaluator | PASS as finite analytic candidate |
| Rq,c direct evaluator | PASS as finite analytic candidate |
| formal spatial quadrature | 0 |
| concrete-only Case21 limit solved | PASS numerically/analytically |
| historical 339.1 comparison | PASS, −0.2305% |
| reinforcement coupled into P and Rq | PASS |
| RC Case21 limit solved | PASS numerically/analytically |
| experiment comparison | PASS, −7.0535% |
| strict truncation remainder certificate | **UNRESOLVED** |
| full user SUCCESS gate | **NOT FULLY PASSED** |

因此最精确的最终标签为：

\[
\boxed{
\texttt{DIRECT\_ANALYTIC\_EVALUATION\_UNRESOLVED}
\ \text{only in the strict-certification sense}
}
\]

数值/平衡解本身已经得到；未解决的是当前实际 integrand finite expansion 的严格、有效余项认证，而不是材料定义、Case21 运动学、concrete equilibrium 或 RC coupling。
