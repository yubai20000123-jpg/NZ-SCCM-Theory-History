# NZ-SCCM Case21 零空间解析极限—切线稳定完整理论计算（试验值读取前冻结稿）

**时间基线：2026-08-12 18:02 +08:00**  
**身份：THEORY RESULT FREEZE BEFORE EXPERIMENT / CURRENT FRESH CASE21 CALCULATION**  
**理论基线：`current/theory/NZ_SCCM_NC_REBAR_ZERO_SPATIAL_ANALYTIC_LIMIT_TANGENT_UNIFIED_THEORY_20260812_1734.md`**  
**执行合同：`current/workflows/NZ_SCCM_CASE21_ZERO_SPATIAL_ANALYTIC_EXECUTION_CONTRACT_20260812_1734.md`**

---

# 0. 隔离声明

本次计算只使用当前时间戳理论、当前 Case21 原始输入冻结表及由这些输入新生成的材料系数和结构解析量。

```text
HISTORICAL_CASE21_D_Q_P_Pu_ROOT_PATH_USED = NO
HISTORICAL_CASE21_ANALYTIC_RESULT_USED = NO
HISTORICAL_FE_GAUSS_SIMPSON_RESULT_USED = NO
HISTORICAL_MATERIAL_POINT_HISTORY_USED = NO
EXPERIMENT_OPENED_DURING_SOLVE = NO
EXPERIMENT_USED_FOR_ROOT_SELECTION = NO
EXPERIMENT_USED_FOR_PARAMETER_TUNING = NO
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
```

本文件形成时尚未读取 Case21 试验极限荷载。理论结果在本文件中先行冻结；试验值只能在其后独立读取并比较。

---

# 1. 原始输入

几何输入：

\[
\boxed{b=\ell=1220\ \mathrm{mm},\qquad t_p=19.30\ \mathrm{mm}}
\tag{C1}
\]

式中，\(b\) 为完整代表半波宽度；\(\ell\) 为轴向完整半波长度；\(t_p\) 为板厚。

普通混凝土：

\[
\boxed{f_c=21.23\ \mathrm{MPa},\quad E_0=20321\ \mathrm{MPa},\quad \varepsilon_0=0.00209,\quad \nu=0.18}
\tag{C2}
\]

式中，\(f_c\) 为单轴抗压强度；\(E_0\) 为初始弹性模量；\(\varepsilon_0\) 为 R10 参考压缩应变；\(\nu\) 为泊松比。

初始缺陷：

\[
\boxed{q_0=A_0/b=1/400=0.0025}
\tag{C3}
\]

式中，\(A_0\) 为 stress-free initial imperfection 幅值；\(q_0\) 为初始缺陷比。

两个正交方向配筋率：

\[
\boxed{\rho_{s,x}=\rho_{s,y}=0.00375}
\tag{C4}
\]

且为中面单层钢筋：

\[
\boxed{z_s=0,\qquad \zeta_s=0}
\tag{C5}
\]

钢筋材料：

\[
\boxed{E_s=200000\ \mathrm{MPa},\qquad \varepsilon_y=0.00265,\qquad f_y=530\ \mathrm{MPa}}
\tag{C6}
\]

compiler 区间在求根前固定为

\[
\boxed{\lambda\in[-1.15,0.12]}
\tag{C7}
\]

---

# 2. R10 派生参数

由

\[
\kappa=\frac{E_0\varepsilon_0}{f_c}
\]

代入 Case21：

\[
\kappa=\frac{20321\times0.00209}{21.23}
=\boxed{2.0005129533678754}.
\tag{C8}
\]

因此

\[
x_{cr}=\frac{\rho}{\kappa}
=\frac{0.1}{2.0005129533678754}
=\boxed{0.04998717945397425}.
\tag{C9}
\]

\[
\eta=\frac{x_{cr}}{20}
=\boxed{0.0024993589726987125}.
\tag{C10}
\]

Foster-informed 一维材料源函数使用

\[
T_{src}(r)=r+(m_t-1)H(r,1)-m_tH(r,10),
\]

其中

\[
m_t=-7/90,\qquad \eta_r=0.05.
\]

对平滑铰闭式原函数直接评价得到

\[
\boxed{\int_0^{10}T_{src}(r)\,dr=6.34987521359851}.
\tag{C11}
\]

这是一维材料坐标运算，不是结构空间求积。

于是

\[
W_{src}=\rho x_{cr}\int_0^{10}T_{src}(r)dr
\]

\[
=0.1\times0.04998717945397425\times6.34987521359851
=\boxed{0.03174123518124918}.
\tag{C12}
\]

由

\[
h=\frac15\left(\frac{W_{src}}{x_{cr}}-\frac{\rho}{10}-\frac92u_r\right),\qquad u_r=0.03,
\]

得到

\[
\boxed{h=0.09799750427197022}.
\tag{C13}
\]

至此闭式 \(U,C,T,T^{(7)}\) 均由材料输入唯一确定。

---

# 3. fresh N48-C1/MM 材料系数

compiler 中心和半宽：

\[
\lambda_c=\frac{-1.15+0.12}{2}=\boxed{-0.515},
\qquad
\lambda_h=\frac{0.12-(-1.15)}2=\boxed{0.635}.
\tag{C14}
\]

零材料坐标：

\[
\xi_0=-\frac{\lambda_c}{\lambda_h}
=\boxed{0.811023622047244}.
\tag{C15}
\]

49 个材料 Chebyshev 根为

\[
\theta_j=\frac{(j+1/2)\pi}{49},\qquad
\lambda_j=-0.515+0.635\cos\theta_j,\quad j=0,\ldots,48.
\tag{C16}
\]

对 \(F\in\{U,C,T,T^{(7)}\}\)，direct coefficient 重新生成：

\[
a_n^{(F,0)}=\frac{2-\delta_{n0}}{49}\sum_{j=0}^{48}F(\lambda_j)\cos(n\theta_j).
\tag{C17}
\]

随后对零点值和真实材料切线施加 C1 修正；\(T\) 再执行 strict-C1 constrained-minimax。fresh minimax 主误差为

\[
\boxed{E_T^*=0.08957188141255312}.
\tag{C18}
\]

fresh 零点记录：

\[
\boxed{U_{48}(0)=1.1102230\times10^{-16},\qquad U'_{48}(0)=2.0005129533678745},
\tag{C19}
\]

\[
\boxed{C_{48}(0)=-1.1102230\times10^{-16},\qquad C'_{48}(0)=6.9935309\times10^{-16}},
\tag{C20}
\]

\[
\boxed{T_{48}(0)=6.6613381\times10^{-15},\qquad T'_{48}(0)=2.2379299\times10^{-14}},
\tag{C21}
\]

\[
\boxed{T^{(7)}_{48}(0)=0,\qquad [T^{(7)}_{48}]'(0)=-3.4967654\times10^{-16}}.
\tag{C22}
\]

完整 fresh 49×4 coefficient table 保存于：

`current/case21/NZ_SCCM_CASE21_FRESH_MATERIAL_COEFFICIENTS_20260812_1802.csv`

其最大 coefficient 仍为 O(1)。

按照当前合同 C9–C10，同步报告整个 compiler 区间上的材料值与一阶切线误差指标：

| primitive | \(E_F^{(0)}\) | \(E_F^{(1)}=\lambda_h\|F'_{48}-F'_{R10}\|_\infty\) |
|---|---:|---:|
| U | 0.00245360402031 | 0.906633445993 |
| C | 0.0140129840394 | 1.21310364652 |
| T | 0.0895720993894 | 199.312325124 |
| T7 | 0.112736914660 | 64.1319479976 |

当前 17:34 时间戳 Case21 合同要求报告 C9–C10，但未冻结新的全域 \(E_F^{(1)}\) 数值接受阈值；本次不擅自发明阈值、不提高 N48 阶数，也不修改 R10。这些值作为材料 compiler fidelity record 原样冻结。结构 current-tangent 另由后述零状态解析回归与沿主平衡支的 \(K_Z\) 门独立检查。

---

# 4. Cayley–Hamilton 二维提升

定义

\[
\mathbf Y=(\mathbf X-\lambda_c\mathbf I)/\lambda_h,
\qquad K_1=\operatorname{tr}\mathbf Y,
\qquad K_2=\det\mathbf Y.
\tag{C23}
\]

由二维 Cayley–Hamilton 恒等式

\[
\mathbf Y^2-K_1\mathbf Y+K_2\mathbf I=0,
\]

每个 Chebyshev 张量项均写成

\[
\mathcal C_n(\mathbf Y)=A_n\mathbf I+B_n\mathbf Y,
\tag{C24}
\]

其中

\[
A_0=1,B_0=0,\quad A_1=0,B_1=1,
\]

\[
A_{n+1}=-2K_2B_n-A_{n-1},
\qquad
B_{n+1}=2A_n+2K_1B_n-B_{n-1}.
\tag{C25}
\]

因此第 \(n\) 个 fresh material coefficient 的二维贡献为

\[
\boxed{\mathbf F_{48}^{(n)}=a_n^{(F,*)}(A_n\mathbf I+B_n\mathbf Y)}.
\tag{C26}
\]

所有 \(\mathbf{CC},\mathbf{TC},\mathbf{TT}\) 均在有限 coefficient 空间内卷积，没有建立物理空间材料点。

---

# 5. fresh limit candidate 的 Nguyen 连续场

由当前 general-D15 平衡支新得到的首个荷载极大值候选为

\[
\boxed{D_L=0.7822850963110681},
\qquad
\boxed{q_L=0.0017707520964949533}.
\tag{C27}
\]

物理附加挠曲幅值：

\[
A_L=bq_L=1220\times0.0017707520964949533
=\boxed{2.160317557723843\ \mathrm{mm}}.
\tag{C28}
\]

因为 Case21 为方形半波 \(b=\ell\)，二阶膜系数为

\[
C_m=\frac{\pi^2}{\varepsilon_0}\left(q_0q_L+\frac12q_L^2\right)
=\boxed{0.02830858365617066}.
\tag{C29}
\]

弯曲系数为

\[
C_b=\frac{\pi^2t_p}{2\varepsilon_0b}q_L
=\boxed{0.06614221072569076}.
\tag{C30}
\]

因此完整连续归一化应变场为

\[
e_x=0.18(0.7822850963110681)
+0.02830858365617066\cos^2X\sin^2Y
+0.06614221072569076\sin X\sin Y\,\zeta,
\tag{C31}
\]

\[
e_y=-0.7822850963110681
+0.02830858365617066\sin^2X\cos^2Y
+0.06614221072569076\sin X\sin Y\,\zeta,
\tag{C32}
\]

\[
g_{xy}=2(0.02830858365617066)\sin X\cos X\sin Y\cos Y
-2(0.06614221072569076)\cos X\cos Y\,\zeta.
\tag{C33}
\]

这些是整个完整半波的连续解析场，不是材料点数组。

---

# 6. 连续 compiler-domain certificate

对整个连续完整半波的低阶 kinematic polynomial 进行 Bernstein coefficient enclosure，得到：

\[
\boxed{0.12-X_{11}\ge0.03933876740769418>0},
\tag{C34}
\]

\[
\boxed{\det(0.12\mathbf I-\mathbf X)\ge0.03232167007144341>0},
\tag{C35}
\]

\[
\boxed{X_{11}+1.15\ge1.0693387674076942>0},
\tag{C36}
\]

\[
\boxed{\det(\mathbf X+1.15\mathbf I)\ge0.3069576188303195>0}.
\tag{C37}
\]

故整个连续完整半波满足

\[
\boxed{-1.15<\lambda_-\le\lambda_+<0.12}.
\tag{C38}
\]

该证书是有限 coefficient enclosure，不是空间点扫描。

---

# 7. general-D15 精确矩与混凝土作用

坐标 Jacobian：

\[
J_\Omega=\frac{b\ell t_p}{2\pi^2}
=\frac{1220\times1220\times19.30}{2\pi^2}
=\boxed{1455282.239925916\ \mathrm{mm^3}}.
\tag{C39}
\]

所有最终 scalar integrand 先展开为

\[
Q=\sum c_{prush}\sin^pX\cos^rX\sin^uY\cos^sY\zeta^h,
\]

然后使用

\[
J_{pr}=\int_0^\pi\sin^pX\cos^rX\,dX,
\quad
Z_h=\int_{-1}^{1}\zeta^h d\zeta,
\]

\[
\mathscr D[Q]=\sum c_{prush}J_{pr}J_{us}Z_h.
\tag{C40}
\]

对最终标量中严格成对出现的余弦因子使用 \(\cos^2=1-\sin^2\) 作精确代数消元只是 general-D15 的等价退化，不是空间 collocation。

fresh 精确收缩为

\[
\boxed{\mathscr D[S_{yy}]=-13.306145538701315},
\tag{C41}
\]

\[
\boxed{\mathscr D[Q_q]=4.479715227945151}.
\tag{C42}
\]

混凝土轴力 prefactor：

\[
\frac{f_cbt_p}{2\pi^2}
=\frac{21.23\times1220\times19.30}{2\pi^2}
=\boxed{25324.296683300985\ \mathrm N}.
\tag{C43}
\]

故

\[
P_c=-\frac{f_cbt_p}{2\pi^2}\mathscr D[S_{yy}]
\]

\[
=-25324.296683300985\times(-13.306145538701315)
=\boxed{336968.77733325394\ \mathrm N}
=\boxed{336.968777333\ \mathrm{kN}}.
\tag{C44}
\]

广义残量 prefactor：

\[
f_c\varepsilon_0J_\Omega
=21.23\times0.00209\times1455282.239925916
=\boxed{64571.891683080845\ \mathrm{N\,mm}}.
\tag{C45}
\]

所以

\[
R_{q,c}=64571.891683080845\times4.479715227945151
=\boxed{289263.68646992213\ \mathrm{N\,mm}}.
\tag{C46}
\]

---

# 8. 钢筋 supported-branch certificate 与解析贡献

因为 \(z_s=0\)，钢筋弯曲应变项消失。fresh limit candidate 上：

\[
\varepsilon_{s,x}\in
[\varepsilon_0\nu D_L,\ \varepsilon_0(\nu D_L+C_m)]
\]

\[
=\boxed{[0.0002942956532322238,\ 0.0003534605930736205]}.
\tag{C47}
\]

轴向钢筋：

\[
\varepsilon_{s,y}\in
[-\varepsilon_0D_L,\ \varepsilon_0(-D_L+C_m)]
\]

\[
=\boxed{[-0.0016349758512901322,\ -0.0015758109114487357]}.
\tag{C48}
\]

因此

\[
\max|\varepsilon_s|=\boxed{0.0016349758512901322},
\]

\[
\frac{\max|\varepsilon_s|}{\varepsilon_y}
=\frac{0.0016349758512901322}{0.00265}
=\boxed{0.6169720193547669<1}.
\tag{C49}
\]

完整连续钢筋场保持弹性支，故 \(E_{s,t}=E_s\)。

Case21 中面纵向钢筋轴力闭式为

\[
P_s=\rho_{s,y}bt_pE_s\varepsilon_0\left(D_L-\frac{C_m}{4}\right).
\tag{C50}
\]

常数乘数：

\[
\rho_{s,y}bt_pE_s\varepsilon_0
=0.00375\times1220\times19.30\times200000\times0.00209
=\boxed{36908.355\ \mathrm N}.
\tag{C51}
\]

故

\[
\boxed{P_s=28611.65023207581\ \mathrm N=28.611650232\ \mathrm{kN}}.
\tag{C52}
\]

同一连续钢筋解析关系给出

\[
\boxed{R_{q,s}=-289262.7835307681\ \mathrm{N\,mm}}.
\tag{C53}
\]

---

# 9. 总平衡与 limit-point candidate

总轴力：

\[
P=P_c+P_s
=336968.77733325394+28611.65023207581
\]

\[
\boxed{P_L=365580.42756532977\ \mathrm N=365.580427565\ \mathrm{kN}}.
\tag{C54}
\]

总平衡残量：

\[
R_q=R_{q,c}+R_{q,s}
=289263.68646992213-289262.7835307681
\]

\[
\boxed{R_q=0.9029391540098004\ \mathrm{N\,mm}}.
\tag{C55}
\]

归一化后

\[
\boxed{R_{norm}=1.5607568552718478\times10^{-6}<10^{-5}}.
\tag{C56}
\]

由同一 finite analytic expression 直接求导得到

\[
\boxed{P_D=144654.26712212552},
\tag{C57}
\]

\[
\boxed{P_q=-79481761.88183713},
\tag{C58}
\]

\[
\boxed{R_{q,D}=-1863131.2151967557},
\tag{C59}
\]

\[
\boxed{R_{q,q}=1023724655.8203216}.
\tag{C60}
\]

所以

\[
L=P_DR_{q,q}-P_qR_{q,D}
=\boxed{1.1882216524375\times10^9},
\tag{C61}
\]

而

\[
\boxed{L_{norm}=4.011943389636033\times10^{-6}<10^{-5}}.
\tag{C62}
\]

平衡支上的荷载切线为

\[
\frac{dP}{dD}\bigg|_{\Gamma_0}
=P_D-P_q\frac{R_{q,D}}{R_{q,q}}
=\boxed{1.1606848049268592\ \mathrm N},
\tag{C63}
\]

在当前尺度上已经接近 0。

fresh 主支在候选点以前的平衡状态给出

\[
L_{norm}=+0.0350822260,\qquad
\frac{dP}{dD}\bigg|_{\Gamma_0}=+9892.2588\ \mathrm N>0,
\]

候选点以后的平衡状态给出

\[
L_{norm}=-0.00306929937,\qquad
\frac{dP}{dD}\bigg|_{\Gamma_0}=-889.9528\ \mathrm N<0.
\]

因此 fresh 主平衡支上确实发生

\[
\boxed{+\rightarrow-},
\tag{C64}
\]

故 (C27) 是从无载点沿当前 general-D15 主支遇到的首个荷载极大值候选。

---

# 10. Zhou/Navier current-tangent gate

同一个 current material operator 生成

\[
\mathbb C_t=\partial\boldsymbol\sigma/\partial\mathbf E.
\]

因为

\[
\mathbf X=\mathbf E_u/\varepsilon_0,
\]

方向导数严格使用

\[
\delta\mathbf X=\delta\mathbf E_u/\varepsilon_0.
\tag{C65}
\]

Case21 无载方形半波解析回归：

\[
K_Z(0,0)=\frac{E_0t_p^3\pi^4}{12(1-\nu^2)b^2}
\]

\[
=\frac{20321\times19.30^3\times\pi^4}{12(1-0.18^2)\times1220^2}
=\boxed{823.416805664979\ \mathrm{N/mm}}.
\tag{C66}
\]

coefficient-space full-field tangent 复现同一值，因此

```text
ZERO_STATE_TANGENT_REGRESSION = PASS
```

沿同一个 fresh corrected \(\Gamma_0\)，general-D15 exact-moment tangent 记录为：

| \(D\) | 对应 fresh equilibrium \(q\)（约） | \(K_Z\) (N/mm) |
|---:|---:|---:|
| 0.500 | 0.001369 | +440.923502 |
| 0.600 | 0.0015126 | +310.077631 |
| 0.700 | 0.0016478 | +163.391903 |
| 0.750 | 0.001722 | +83.391102 |
| 0.770 | 0.001752 | +34.060495 |
| 0.780 | 0.0017667 | +6.705588 |
| 0.782 | 0.0017704 | +0.979509 |

在首个荷载极大值候选 (C27) 上：

\[
\boxed{K_{Z,c}^{mat}=765.4620815266977\ \mathrm{N/mm}},
\tag{C67}
\]

\[
\boxed{K_{Z,c}^{geo}=-719.5765678312335\ \mathrm{N/mm}},
\tag{C68}
\]

由于中面钢筋 \(z_s=0\)，

\[
\boxed{K_{Z,s}^{mat}=0},
\tag{C69}
\]

钢筋几何项为

\[
\boxed{K_{Z,s}^{geo}=-45.50598684467001\ \mathrm{N/mm}}.
\tag{C70}
\]

故

\[
K_Z=765.4620815266977-719.5765678312335-45.50598684467001
\]

\[
\boxed{K_Z(D_L,q_L)=+0.37952685079415716\ \mathrm{N/mm}>0}.
\tag{C71}
\]

因此首个荷载极大值到达时基本 Navier 模态尚保持微小正切线。

继续只在同一个 corrected \(\Gamma_0\) 上定位首个 tangent zero，得到

\[
\boxed{D_T=0.7824254327857517},
\qquad
\boxed{q_T=0.0017710077550576295}.
\tag{C72}
\]

该状态荷载约为

\[
\boxed{P_T=365580.40007630707\ \mathrm N}.
\tag{C73}
\]

其 tangent 分解为

\[
K_{Z,c}^{mat}=765.0871372932144,
\]

\[
K_{Z,c}^{geo}=-719.5753920238684,
\]

\[
K_{Z,s}^{mat}=0,
\]

\[
K_{Z,s}^{geo}=-45.51414376245792\ \mathrm{N/mm},
\]

总和

\[
\boxed{K_Z=-0.0023984931119542807\ \mathrm{N/mm}\approx0}.
\tag{C74}
\]

两位置的 \(D\) 差为

\[
D_T-D_L=\boxed{0.0001403364746835889}>10^{-4}.
\tag{C75}
\]

因此按照当前合同的冻结 root-repeatability 尺度，二者不归为 coincident：

```text
PRELIMIT_TANGENT_STABILITY = PASS
LIMIT_POINT_CONTROL = YES
COUPLED_LIMIT_TANGENT_CONTROL = NO
```

也就是说，fresh Case21 当前理论控制状态是 **荷载极大值先于 Zhou/Navier 基本模态 tangent loss**。

---

# 11. 试验读取前的最终理论冻结

按照当前统一理论和 Case21 时间戳合同，本次 fresh Case21 理论结果在读取任何试验极限荷载之前冻结为

\[
\boxed{D_u=0.7822850963110681},
\tag{C76}
\]

\[
\boxed{q_u=0.0017707520964949533},
\tag{C77}
\]

\[
\boxed{A_u=2.160317557723843\ \mathrm{mm}},
\tag{C78}
\]

\[
\boxed{P_u^{theory}=365.580427565\ \mathrm{kN}}.
\tag{C79}
\]

控制机制：

```text
CONTROL = FIRST +->- LIMIT POINT
PRELIMIT_TANGENT_STABILITY = PASS
FIRST_TANGENT_ZERO = AFTER LIMIT POINT
```

生产残量：

\[
\boxed{R_{norm}=1.5607568553\times10^{-6}<10^{-5}},
\]

\[
\boxed{|L_{norm}|=4.0119433896\times10^{-6}<10^{-5}},
\]

\[
\boxed{K_Z(D_u,q_u)=+0.3795268508\ \mathrm{N/mm}>0}.
\]

至本文件结束时：

```text
ITEMS_01_TO_18_OF_CASE21_CONTRACT = COMPLETE
THEORY_RESULT_FROZEN = YES
EXPERIMENTAL_LIMIT_LOAD_READ = NO
```

下一步只允许读取原始试验来源中的 Case21 实验极限荷载列，并与式（C79）比较；不得读取、引用或比较任何历史解析、FE、Gauss、Simpson 或其他计算结果。