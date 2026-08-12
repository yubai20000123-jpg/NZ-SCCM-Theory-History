# NZ-SCCM 完整计算理论与执行合同恢复审计 — 2026-08-12 21:45 +08:00

**身份：FULL_STARTUP_RECOVERY AUDIT / NO NEW THEORY / NO NEW CALCULATION**  
**目的：联合历史原始治理、当前 GitHub、当前正式理论和用户最新可见修正，恢复完整计算理论与合同；不重新设计 compiler coverage，不新增材料机制，不重算 Case21/Swartz24。**

---

## 0. 恢复裁决

本轮递归核查 current / governance / evidence / history，并按项目 source-of-truth 与 recovery protocol 处理冲突。恢复出的当前完整主链为：

```text
材料/几何来源
-> material-native spectral domain Λ_M（材料原生资格域，PRIMARY）
-> R10 closed current target
-> N48-C1/MM finite analytic compiler
-> Cayley-Hamilton 2D lift
-> Nguyen second-order ONE_CONTINUOUS_COMPLETE_HALFWAVE, m=1
-> general-D15 exact trigonometric moments
-> concrete Pc, Rq,c
-> rebar Ps, Rq,s + branch certificate
-> total P(D,q), Rq(D,q)
-> same-expression derivatives P_D,P_q,Rq_D,Rq_q
-> primary equilibrium branch Γ0
-> first +->- limit-point candidate from L=0
-> full-field Zhou/Navier current-tangent K_Z on the same Γ0
-> control/acceptance verdict
-> theory freeze
-> experiment-only validation after freeze
```

结构 reachable spectral domain `Λ_R` 是 SECONDARY：只用于验证/conditioning/optional acceleration，必须满足 `Λ_R ⊆ Λ_M`；不得用结构 Pu、历史根、试验荷载反向决定材料原生资格域或生产系数。

```text
FULL_STARTUP_RECOVERY = COMPLETE
NEW_THEORY_CREATED = NO
NEW_CALCULATION = NO
DOMAIN_HIERARCHY_RESTORED = YES
CURRENT_17:34_THEORY_MECHANICS = GOVERNING
CURRENT_17:34_DOMAIN_LAYER = INCOMPLETE / OMITTED ACTIVE GOVERNANCE
REPOSITORY_STATE_LAG = YES
```

---

# 1. 固定理论边界

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
ACTIVE_MODE = m=1
KINEMATICS = NGUYEN_SECOND_ORDER
R10_MATERIAL_TARGET = FROZEN
MATERIAL_COMPILER_ORDER = 48
U_COMPILER = N48-C1
C_COMPILER = N48-C1
T7_COMPILER = N48-C1
T_COMPILER = N48-C1-CONSTRAINED-MINIMAX
CAYLEY_HAMILTON = GOVERNING
EXACT_MOMENT_ENGINE = D15_GENERAL_TRIG_MOMENTS
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_auxiliary_numerical_quadrature = 0
N_auxiliary_ODE_steps = 0
NO hidden initial-value integration
NO large connection system as production operator
STRUCTURAL_CALIBRATION = NO
PANEL_LEVEL_SURROGATE = NO
```

材料 N48 的 49 个根是 1D MATERIAL COORDINATES，不是结构空间积分点。

---

# 2. R10 普通混凝土 current target

基本输入：

\[
f_c,\quad E_0,\quad \varepsilon_0,\quad \nu.
\]

定义

\[
\kappa=\frac{E_0\varepsilon_0}{f_c},\qquad
\rho=0.1,\qquad
x_{cr}=\frac{\rho}{\kappa},\qquad
\eta=\frac{x_{cr}}{20}.
\]

物理面内应变

\[
\mathbf E=\begin{bmatrix}
\varepsilon_x&\gamma_{xy}/2\\
\gamma_{xy}/2&\varepsilon_y
\end{bmatrix}.
\]

等效单轴应变张量

\[
\mathbf E_u=
\frac{(1-\nu)\mathbf E+\nu\operatorname{tr}(\mathbf E)\mathbf I}{1-\nu^2},
\qquad
\mathbf X=\frac{\mathbf E_u}{\varepsilon_0}.
\]

\[
X_{11}=\frac{\varepsilon_x+\nu\varepsilon_y}{(1-\nu^2)\varepsilon_0},\quad
X_{22}=\frac{\nu\varepsilon_x+\varepsilon_y}{(1-\nu^2)\varepsilon_0},\quad
X_{12}=\frac{\gamma_{xy}}{2(1+\nu)\varepsilon_0}.
\]

主值：

\[
\mu=\frac{X_{11}+X_{22}}2,\quad
\delta=\frac{X_{11}-X_{22}}2,\quad
r_X=\sqrt{\delta^2+X_{12}^2},\quad
\lambda_\pm=\mu\pm r_X.
\]

R10 平滑 one-sided coordinate：

\[
\Pi_\eta(z)=
\frac{z^2\left(\sqrt{z^2+\eta^2}+z\right)}{2(z^2+\eta^2)}.
\]

正式解释：`Π_η` 是 smooth nonnegative one-sided material coordinate；不得重新称为严格 softplus，也不得声称 `Π_η(z)-Π_η(-z)=z`。

\[
c(\lambda)=\Pi_\eta(-\lambda),\qquad
t(\lambda)=\Pi_\eta(\lambda).
\]

压缩 primitive：

\[
C(\lambda)=\frac{\kappa c(\lambda)}{1+(\kappa-2)c(\lambda)+c(\lambda)^2}.
\]

Foster-informed tensile source：

\[
r=\frac{t}{x_{cr}},\qquad m_t=-\frac7{90},\qquad \eta_r=0.05,
\]

\[
H(r,r_0)=\frac12[(r-r_0)+\sqrt{(r-r_0)^2+\eta_r^2}]
-\frac12[-r_0+\sqrt{r_0^2+\eta_r^2}],
\]

\[
T_{src}(r)=r+(m_t-1)H(r,1)-m_tH(r,10),
\]

\[
W_{src}=\rho x_{cr}\int_0^{10}T_{src}(r)\,dr.
\]

这里是 MATERIAL-COORDINATE analytic integral，不是结构空间 quadrature。

C2 tensile reconstruction：

\[
\tau=\frac{t}{x_{cr}},
\]

\[
u_1(\tau)=\rho\tau+(10h-6\rho)\tau^3+(8\rho-15h)\tau^4+(6h-3\rho)\tau^5,
\]

\[
s=\frac{t-x_{cr}}{9x_{cr}},\qquad u_r=0.03,
\]

\[
u_2(s)=h+(u_r-h)(10s^3-15s^4+6s^5),
\]

\[
h=\frac15\left(\frac{W_{src}}{x_{cr}}-\frac{\rho}{10}-\frac92u_r\right),
\]

\[
u_{sm}(t)=
\begin{cases}
u_1(t/x_{cr}),&0\le t\le x_{cr},\\
u_2[(t-x_{cr})/(9x_{cr})],&x_{cr}<t\le10x_{cr},\\u_r,&t>10x_{cr}.
\end{cases}
\]

\[
T(\lambda)=\frac{u_{sm}[\Pi_\eta(\lambda)]}{\rho},\qquad T^{(7)}(\lambda)=T(\lambda)^7.
\]

Master primitive：

\[
U(\lambda)=\kappa\lambda-C(\lambda)+\kappa c(\lambda)+\rho T(\lambda)-\kappa t(\lambda).
\]

Interaction constants：

\[
a_{cc}=0.1072329249362415,\qquad a_t=1-2^{-1/8}.
\]

`a_cc` 的身份是 project-frozen biaxial-compression physical target coefficient；不是 Nguyen/Foster 原文直接常数，也不是通过 Case21/Swartz Pu 反标。

主方向 current stress：

\[
s_+=U_+-a_{cc}C_+^2C_-+C_+T_- -\rho a_tT_+T_-^8,
\]

\[
s_-=U_--a_{cc}C_-^2C_++C_-T_+ -\rho a_tT_-T_+^8.
\]

零点锚：

\[
U(0)=0,\quad U'(0)=\kappa,
\]

\[
C(0)=T(0)=T^{(7)}(0)=0,
\]

\[
C'(0)=T'(0)=[T^{(7)}]'(0)=0.
\]

R10 只改 1D tensile scalar 的历史决定不改变结构 mechanics / multidimensional architecture；不得依据 panel capacity 重新调 R10。

---

# 3. 被 17:34 当前理论遗漏的材料域层：Λ_M 与 Λ_R

## 3.1 ACTIVE hierarchy

恢复治理：

```text
PRIMARY_DOMAIN   = MATERIAL_ADMISSIBLE_SPECTRAL_DOMAIN = Λ_M
SECONDARY_DOMAIN = STRUCTURAL_REACHABLE_SUBDOMAIN      = Λ_R
Λ_R ⊆ Λ_M
```

生产材料 compiler 首先必须在 constitutive material-native spectral domain `Λ_M` 上具有资格。结构 Case21/Swartz 的 reachable spectrum `Λ_R` 只允许用于：

- verification;
- conditioning;
- optional acceleration.

禁止：

```text
Pu -> material spectral domain = PROHIBITED
experiment -> compiler domain = PROHIBITED
historical root -> compiler domain = PROHIBITED
Λ_R -> redefine material-native validity = PROHIBITED
```

## 3.2 Historical R05 scalar-domain instance

历史 R05 source-stage 给出过：

\[
\Lambda_{M,NC}^{active}=[-\gamma_2,\alpha_1\rho/\kappa],
\quad \gamma_2=10,\ \alpha_1=10.
\]

这条数值公式属于当时 active source closure。恢复本轮只保留 ACTIVE hierarchy；**不得未经当前 R10 reconciliation 就把该历史数值域直接冒充当前 R10 的最终 native domain。**

## 3.3 Structural reachable-domain certifier

历史 structure-first domain certifier 的正确当前身份是 SECONDARY / certificate：

Nguyen continuous kinematics -> interval enclosure of `e_x,e_y,g_xy` -> linear `E -> E_u -> X` propagation -> 2×2 Gershgorin/eigenvalue enclosure -> `Λ_R`.

它不使用结构空间点，但它不是 `Λ_M` 的物理来源。历史某些 Case21 regression search boxes 只具有历史/secondary identity，不能升级为当前 admissible-domain definition。

## 3.4 Current omission

17:34 当前 theory 仅写：

\[
\lambda\in[\lambda_a,\lambda_b]
\]

并要求 root 前冻结、不得由 experiment/history 修改；但没有说明它究竟是 `Λ_M`、`Λ_R` 还是 qualification subdomain。没有找到后续明确 revocation 撤销 2026-08-10 的 material-native hierarchy。

因此当前裁决：

```text
CURRENT_CONTRACT_OMISSION = MATERIAL_NATIVE_DOMAIN_LAYER_NOT_CARRIED_FORWARD
CURRENT_CASE21_INTERVAL_IDENTITY = UNRESOLVED UNTIL RECONCILED
MATERIAL_NATIVE_RULE_REVOKED = NO EVIDENCE
```

另需区分四个对象：

1. `Λ_M` = material-native spectral admissible domain;
2. `Λ_R` = structural reachable spectral subdomain;
3. compiler support topology/mask = retained analytic term topology;
4. 49 N48 nodes = material-coordinate coefficient-generation nodes.

四者不得混同。

---

# 4. N48-C1/MM finite analytic compiler

给定一个**合法身份已经明确**的 qualification interval `[λ_a,λ_b]` 后：

\[
\lambda_c=\frac{\lambda_a+\lambda_b}{2},\qquad
\lambda_h=\frac{\lambda_b-\lambda_a}{2},\qquad
\xi=\frac{\lambda-\lambda_c}{\lambda_h}.
\]

49 个材料根：

\[
\theta_j=\frac{(j+1/2)\pi}{49},\qquad
\lambda_j=\lambda_c+\lambda_h\cos\theta_j,
\quad j=0,\ldots,48.
\]

Direct coefficients：

\[
a_n^{(F,0)}=\frac{2-\delta_{n0}}{49}\sum_{j=0}^{48}F(\lambda_j)\cos(n\theta_j),
\quad F\in\{U,C,T,T^{(7)}\}.
\]

定义

\[
V_{jn}=\cos(n\theta_j),
\]

\[
H=V^TV=\operatorname{diag}(49,49/2,\ldots,49/2),
\qquad
H^{-1}=\frac1{49}\operatorname{diag}(1,2,\ldots,2),
\]

\[
\xi_0=-\frac{\lambda_c}{\lambda_h},
\]

\[
G=\begin{bmatrix}
\mathcal C_0(\xi_0)&\cdots&\mathcal C_{48}(\xi_0)\\
\lambda_h^{-1}\mathcal C_0'(\xi_0)&\cdots&\lambda_h^{-1}\mathcal C_{48}'(\xi_0)
\end{bmatrix}.
\]

Targets：

\[
d_U=(0,\kappa)^T,\qquad d_C=d_T=d_{T^{(7)}}=(0,0)^T.
\]

C1 correction：

\[
a^{(F,C1)}=a^{(F,0)}+H^{-1}G^T(GH^{-1}G^T)^{-1}(d_F-Ga^{(F,0)}).
\]

Production identity：

```text
U = N48-C1
C = N48-C1
T7 = N48-C1
T = N48-C1-CONSTRAINED-MINIMAX
```

T minimax：

\[
\mathcal F_T=\{a:Ga=d_T\},
\]

\[
p_a(\lambda)=\sum_{n=0}^{48}a_n\mathcal C_n[\xi(\lambda)],
\]

\[
E_T^*=\min_{a\in\mathcal F_T}\|p_a-T_{R10}\|_\infty,
\]

\[
\mathcal S_T^*=\{a\in\mathcal F_T:\|p_a-T_{R10}\|_\infty=E_T^*\},
\]

\[
a^{(T,MM)}=\arg\min_{a\in\mathcal S_T^*}\frac12(a-a^{(T,C1)})^TH(a-a^{(T,C1)}).
\]

Deterministic T material-only contract：4096 initial exchange material nodes; 131072 verify material nodes; material landmarks; max 50 rounds; if not converged `BLOCKED_AT_T_MINIMAX`. 这些均不是结构空间 discretization。

材料 fidelity 必须报告：

\[
E_F^{(0)}=\|F_{48}-F_{R10}\|_{L^\infty},
\]

\[
E_F^{(1)}=\lambda_h\|F'_{48}-F'_{R10}\|_{L^\infty}.
\]

当前不新增 theorem-level numerical cutoff；direct N48 tangent 已被历史审计否定，C1/MM 是当前 production compiler。

---

# 5. Cayley-Hamilton 2D lift 与 current stress

\[
Y=\frac{X-\lambda_cI}{\lambda_h},\qquad K_1=\operatorname{tr}Y,\qquad K_2=\det Y.
\]

二维 Cayley-Hamilton：

\[
Y^2-K_1Y+K_2I=0.
\]

\[
\mathcal C_n(Y)=A_nI+B_nY,
\]

\[
A_0=1,B_0=0,\qquad A_1=0,B_1=1,
\]

\[
A_{n+1}=-2K_2B_n-A_{n-1},
\]

\[
B_{n+1}=2A_n+2K_1B_n-B_{n-1}.
\]

每一 primitive：

\[
F_{48}(X)=\sum_{n=0}^{48}a_n^{(F,*)}\mathcal C_n(Y)=A_FI+B_FY.
\]

Tensor interactions：

\[
CC=\det(C)C,
\]

\[
TC=C[\operatorname{tr}(T)I-T],
\]

\[
TT=\det(T)[\operatorname{tr}(T^{(7)})I-T^{(7)}],
\]

\[
S=U-a_{cc}CC+TC-\rho a_tTT,
\qquad
\sigma=f_cS.
\]

---

# 6. Nguyen second-order ONE_CONTINUOUS_COMPLETE_HALFWAVE

\[
X=\frac{\pi x}{b},\qquad Y=\frac{\pi y}{\ell},\qquad \zeta=\frac{2z}{t_p}.
\]

\[
w_0=A_0\sin X\sin Y,\qquad w_1=A\sin X\sin Y,
\]

\[
q_0=A_0/b,\qquad q=A/b.
\]

No-load state：

\[
(D,q)=(0,0).
\]

\[
\chi_q=q_0q+\frac12q^2.
\]

General coefficients：

\[
C_{mx}=\frac{\pi^2}{\varepsilon_0}\chi_q,
\quad
C_{my}=\frac{\pi^2b^2}{\varepsilon_0\ell^2}\chi_q,
\quad
C_{mxy}=\frac{2\pi^2b}{\varepsilon_0\ell}\chi_q,
\]

\[
C_{bx}=\frac{\pi^2t_p}{2\varepsilon_0b}q,
\quad
C_{by}=\frac{\pi^2t_pb}{2\varepsilon_0\ell^2}q,
\quad
C_{bxy}=-\frac{\pi^2t_p}{\varepsilon_0\ell}q.
\]

Normalized continuous strain field：

\[
e_x=\nu D+C_{mx}\cos^2X\sin^2Y+C_{bx}\sin X\sin Y\,\zeta,
\]

\[
e_y=-D+C_{my}\sin^2X\cos^2Y+C_{by}\sin X\sin Y\,\zeta,
\]

\[
g_{xy}=C_{mxy}\sin X\cos X\sin Y\cos Y+C_{bxy}\cos X\cos Y\,\zeta.
\]

\[
\varepsilon_x=\varepsilon_0e_x,\quad
\varepsilon_y=\varepsilon_0e_y,\quad
\gamma_{xy}=\varepsilon_0g_{xy}.
\]

`m=1` 和一个完整代表半波固定。不得在无明确 failure evidence / AMEND 授权时重启 m-search。

---

# 7. general-D15 exact moments

正式 scalar basis：

\[
Q(X,Y,\zeta)=\sum c_{prush}\sin^pX\cos^rX\sin^uY\cos^sY\zeta^h.
\]

\[
J_{pr}=\int_0^\pi\sin^pX\cos^rX\,dX
=\begin{cases}
0,&r\ \text{odd},\\
B((p+1)/2,(r+1)/2),&r\ \text{even},
\end{cases}
\]

\[
Z_h=\int_{-1}^{1}\zeta^h\,d\zeta
=\begin{cases}
0,&h\ \text{odd},\\
2/(h+1),&h\ \text{even}.
\end{cases}
\]

\[
\boxed{\mathscr D[Q]=\sum c_{prush}J_{pr}J_{us}Z_h.}
\]

\[
J_\Omega=\frac{b\ell t_p}{2\pi^2}.
\]

旧 restricted sine/Chebyshev-in-sine basis 只有在对具体 scalar integrand 证明 algebraic equivalence 后才可作为退化实现。general-D15 是 governing mathematical statement。

---

# 8. Concrete / Rebar / total structural operators

Concrete axial observable：

\[
P_c=-\frac1\ell\int_{\Omega_h}\sigma_{yy}\,dV
=-\frac{f_cbt_p}{2\pi^2}\mathscr D[S_{yy}].
\]

它是 representative complete-halfwave average axial load observable，不自动等价于任意局部端截面反力。

定义

\[
e=E/\varepsilon_0,
\qquad
Q_q=S:e_{,q}.
\]

\[
R_{q,c}=f_c\varepsilon_0J_\Omega\mathscr D[Q_q].
\]

Rebar source inputs：

\[
E_s,f_y,\varepsilon_y,\varepsilon_f,\rho_{s,\alpha}^{(r)},z_s^{(r)}.
\]

\[
\sigma_s(\varepsilon_s)=
\begin{cases}
E_s\varepsilon_s,&|\varepsilon_s|\le\varepsilon_y,\\
f_y\operatorname{sgn}(\varepsilon_s),&\varepsilon_y<|\varepsilon_s|\le\varepsilon_f.
\end{cases}
\]

\[
n_\alpha=(\cos\theta_\alpha,\sin\theta_\alpha)^T,
\qquad
\zeta_r=\frac{2z_s^{(r)}}{t_p},
\]

\[
\varepsilon_{s,\alpha}^{(r)}=n_\alpha^TE(X,Y,\zeta_r)n_\alpha,
\]

\[
t_{s,\alpha}^{(r)}=\rho_{s,\alpha}^{(r)}t_p.
\]

\[
P_s=-\sum_{r\parallel y}\frac{t_{s,y}^{(r)}}{\ell}\int_A\sigma_{s,y}^{(r)}\,dA,
\]

\[
R_{q,s}=\sum_{r,\alpha}t_{s,\alpha}^{(r)}\int_A\sigma_{s,\alpha}^{(r)}\frac{\partial\varepsilon_{s,\alpha}^{(r)}}{\partial q}\,dA.
\]

若一个连续钢筋族跨越多个材料支且没有零空间 analytic branch closure：

```text
BLOCKED_AT_STEEL_BRANCH
```

不得使用 rebar spatial material-point partition/Gauss 继续。

Total：

\[
P=P_c+P_s,
\qquad
R_q=R_{q,c}+R_{q,s}.
\]

Same-expression derivatives：

\[
P_D,\ P_q,\ R_{q,D},\ R_{q,q}.
\]

生产导数必须来自同一有限解析表达的 analytic differentiation / forward AD；不得使用 spatial finite differences。

\[
L=P_DR_{q,q}-P_qR_{q,D}.
\]

---

# 9. Primary equilibrium branch 与 first +->- limit root

Admissible set：

\[
\mathcal A=\{(D,q):D\ge0,q\ge0,P\ge0,\text{material/compiler certificates pass},\text{steel branch pass},P,R_q,\text{required derivatives finite}\}.
\]

Current limit-root contract explicitly states：

```text
NO artificial D_max
NO artificial q_max
NO historical Case21 answer defining admissible upper boundary
```

Equilibrium set：

\[
\mathcal E=\{(D,q):R_q(D,q)=0\}.
\]

Primary branch：

\[
\boxed{\Gamma_0=\operatorname{Conn}_{(0,0)}(\mathcal E\cap\mathcal A).}
\]

Regular point：

\[
\nabla R_q=(R_{q,D},R_{q,q})\ne0.
\]

Tangent vector：

\[
t_0=(R_{q,q},-R_{q,D}),
\]

\[
\nabla P\cdot t_0=L.
\]

Oriented unit tangent：

\[
\hat t=\pm\frac{(R_{q,q},-R_{q,D})}{\sqrt{R_{q,q}^2+R_{q,D}^2}},
\]

initial orientation toward `D>0`, then maintain orientation continuity.

If `∇Rq=0` before first maximum：

```text
BLOCKED_AT_PRIMARY_BRANCH_SINGULARITY
```

Along branch：

\[
g(s)=\frac{dP}{ds}=\nabla P\cdot\hat t.
\]

At regular point：

\[
g=0\iff L=0.
\]

Production maximum requires：

\[
g(s_L^-)>0,\qquad g(s_L^+)<0.
\]

\[
\mathcal M=\{s_i>0:R_q=0,L=0,g:+\to-\}.
\]

\[
s_L=\min\mathcal M,
\quad
(D_L,q_L)=\Gamma_0(s_L),
\quad
P_L=P(D_L,q_L).
\]

Forbidden root selection：

```text
maximum mathematical root = FORBIDDEN
disconnected high-amplitude root = FORBIDDEN
negative-q branch = FORBIDDEN
closest historical root = FORBIDDEN
closest experiment = FORBIDDEN
skip first +->- maximum = FORBIDDEN
```

If no admissible first maximum before leaving `A`：

```text
NO_ADMISSIBLE_LIMIT_ROOT
```

Residual gates：

\[
R_{mat}=f_c\varepsilon_0J_\Omega,
\]

\[
R_{scale}=\max(R_{mat},|R_{q,c}|+|R_{q,s}|),
\]

\[
R_{norm}=\frac{|R_q|}{R_{scale}}\le10^{-5},
\]

\[
L_{norm}=\frac{P_DR_{q,q}-P_qR_{q,D}}{|P_DR_{q,q}|+|P_qR_{q,D}|},
\qquad |L_{norm}|\le10^{-5}.
\]

---

# 10. Full-field Zhou/Navier current-tangent stability gate

\[
\boxed{\mathbb C_t(X,Y,\zeta;D,q)=\frac{\partial\sigma}{\partial E}.}
\]

Mandatory dimension/scaling：

\[
\delta X=\frac{\delta E_u}{\varepsilon_0}.
\]

不得漏掉 `1/ε0`。

Navier mode：

\[
\varphi=\sin X\sin Y,
\qquad
\alpha=\frac\pi b,
\qquad
\beta=\frac\pi\ell.
\]

\[
\varphi_{,x}=\alpha\cos X\sin Y,\quad
\varphi_{,y}=\beta\sin X\cos Y,
\]

\[
\varphi_{,xx}=-\alpha^2\varphi,\quad
\varphi_{,yy}=-\beta^2\varphi,\quad
\varphi_{,xy}=\alpha\beta\cos X\cos Y.
\]

Unit perturbation engineering curvature strain：

\[
b_\varphi=-z\begin{bmatrix}
\varphi_{,xx}\\
\varphi_{,yy}\\
2\varphi_{,xy}
\end{bmatrix}.
\]

Concrete material tangent modal stiffness：

\[
K_{Z,c}^{mat}=\int_{\Omega_h}b_\varphi^TC_t^{eng}b_\varphi\,dV.
\]

Concrete geometric：

\[
K_{Z,c}^{geo}=\int_{\Omega_h}(\sigma_x\varphi_{,x}^2+2\tau_{xy}\varphi_{,x}\varphi_{,y}+\sigma_y\varphi_{,y}^2)\,dV.
\]

Steel tangent：

\[
E_{s,t}^{(r,\alpha)}=\frac{d\sigma_s}{d\varepsilon_s},
\]

elastic branch `=E_s`, ideal-plastic branch `=0`.

\[
\kappa_\varphi=-\begin{bmatrix}
\varphi_{,xx}&\varphi_{,xy}\\
\varphi_{,xy}&\varphi_{,yy}
\end{bmatrix}.
\]

\[
K_{Z,s}^{mat}=\sum t_{s,\alpha}^{(r)}\int_AE_{s,t}^{(r,\alpha)}[z_s^{(r)}n_\alpha^T\kappa_\varphi n_\alpha]^2dA,
\]

\[
K_{Z,s}^{geo}=\sum t_{s,\alpha}^{(r)}\int_A\sigma_{s,\alpha}^{(r)}(n_\alpha\cdot\nabla\varphi)^2dA.
\]

\[
\boxed{K_Z=K_{Z,c}^{mat}+K_{Z,c}^{geo}+K_{Z,s}^{mat}+K_{Z,s}^{geo}.}
\]

Interpretation：

```text
K_Z > 0 : positive modal tangent
K_Z = 0 : modal critical
K_Z < 0 : negative modal tangent
```

Directional Zhou projections：

\[
I_\varphi=I_\psi=b\ell/4,
\]

\[
D_x^*=\frac1{I_\varphi}\int z^2C_{xx,t}\varphi^2dV,
\quad
D_y^*=\frac1{I_\varphi}\int z^2C_{yy,t}\varphi^2dV,
\]

\[
D_\mu^*=\frac1{I_\varphi}\int z^2\frac{C_{xy,t}+C_{yx,t}}2\varphi^2dV,
\]

\[
D_{66}^*=\frac1{I_\psi}\int z^2G_t(\cos X\cos Y)^2dV,
\]

\[
H^*=D_\mu^*+2D_{66}^*,
\]

\[
K_{Z,c}^{mat}=I_\varphi[D_x^*\alpha^4+2H^*\alpha^2\beta^2+D_y^*\beta^4].
\]

`t_p^3 C_t/12` 仅是 uniform-tangent degeneration，不是一般 nonlinear current state 定义。

Zhou/Attard identity：Zhou 提供方向刚度/Navier 稳定语言；不得把 Zhou 组合墙截面材料常数移入 RC。Attard 只作解释/诊断，不得把 `0.4Ec` 植入 R10。

Tangent gate 与 limit root 的关系：

- 若 first `+->-` limit candidate 以前 `K_Z>0`，则 `PRELIMIT_TANGENT_STABILITY=PASS`，limit candidate 可接受；
- 若更早出现 `K_Z=0`，则 `BLOCKED_AT_PRELIMIT_TANGENT_LOSS`，后面的 limit point 不得直接冻结为最终 capacity；
- 不得悄悄把 `K_Z=0` 定义成第二套 Pu solver；
- 若二者在已冻结 repeatability tolerance 内 coincidence，可标记 `COUPLED_LIMIT_TANGENT_CONTROL`。

**当前恢复没有找到“1e-4 coincidence tolerance”作为 universal governing rule 的明确 provenance；该数值不得在未找到来源前上升为普适理论常数。**

---

# 11. Blind execution / experiment isolation contract

任何新的 Case/Swartz production calculation：

```text
HISTORICAL_CASE_D_Q_P_Pu_ROOT_PATH = FORBIDDEN
HISTORICAL_CASE_ANALYTIC_RESULT = FORBIDDEN
HISTORICAL_FE_GAUSS_SIMPSON_RESULT = FORBIDDEN
HISTORICAL_MATERIAL_POINT_HISTORY = FORBIDDEN
EXPERIMENT_DURING_SOLVE = FORBIDDEN
EXPERIMENT_FOR_ROOT_SELECTION = FORBIDDEN
EXPERIMENT_FOR_PARAMETER_TUNING = FORBIDDEN
EXPERIMENT = FINAL COMPARISON ONLY AFTER THEORY RESULT FREEZE
```

必须区分：experimental buckling load / experimental failure load / historical FE prediction / current Pcr / current Pu。不得混用。极限承载力验证应与 failure/ultimate load 比较，而不是把 experimental buckling load 当作 Pu。

---

# 12. 19-item calculation closure gate

只有下列 19 项全部完成才可写 `CALCULATION_CLOSURE=PASS`：

1. raw materials/geometric inputs；
2. R10 derived parameters；
3. fresh 49×4 N48 coefficients；
4. C1/MM material value+tangent fidelity records；
5. material/compiler-domain certificate，且 domain identity 符合 `Λ_M/Λ_R` hierarchy；
6. general-D15 `S_yy` contraction；
7. general-D15 `Q_q` contraction；
8. rebar continuous branch certificate；
9. corrected `Rq=0` primary branch `Γ0`；
10. first `+->-` limit candidate + `R_norm/L_norm`；
11. zero-state `K_Z` regression；
12. `K_Z,c^mat`；
13. `K_Z,c^geo`；
14. `K_Z,s^mat`；
15. `K_Z,s^geo`；
16. total `K_Z` along the same corrected `Γ0`；
17. whether `K_Z=0` occurs before limit candidate；
18. final theory result freeze；
19. experiment-only comparison after theory freeze。

---

# 13. Historical architecture retained / superseded / rejected

## 13.1 Retained architecture

```text
G18/G27 invariant-current-map architecture = RETAINED
G20/G21 smooth conservative source-regularization principles = RETAINED
G26 moment-first D15 = RETAINED
G28 M(epsilon)->analytic series->D15 exact moments = RETAINED
G30 same P,Rq,L kernel for Pu = RETAINED / OPERATIONALLY ACCEPTED
```

## 13.2 Historical evidence only

```text
G22 high-order global polynomial = CERTIFICATE EVIDENCE ONLY
G23-G25 surrogate experiments = HISTORICAL / NOT FORMAL
G29 historical Pcr batch = HISTORICAL
G31 uncracked Pu + UHPC-C0 = EXECUTED BASELINE / NOT CURRENT PRODUCTION MATERIAL
old Case21 roots/loads = AUDIT ONLY
old Swartz24 predicted roots/loads = AUDIT ONLY for future blind recomputation
old structure-first domain boxes = SECONDARY HISTORICAL reachability certificates
```

## 13.3 Rejected / prohibited

```text
U+xyD mandatory grammar = RETIRED
G18 q4/q6 specific coefficients = REJECTED, architecture retained
formal spatial Gauss/Simpson/adaptive quadrature = PROHIBITED
spatial Chebyshev collocation = PROHIBITED
material-point grid/cells = PROHIBITED
formal spatial subdomains > 1 = PROHIBITED
auxiliary numerical quadrature/ODE propagation = PROHIBITED
panel-level surrogate = PROHIBITED
panel-load calibration = PROHIBITED
experiment/history root selection = PROHIBITED
naive expand-then-integrate = REJECTED
new load-step/arclength Pu solver = PROHIBITED
PF1 large connection as production operator = REJECTED
P2A degree<=16 primitive compiler = REJECTED FAMILY
D15 UHPC Layer-0 material identity = PROHIBITED
UHPC=NC with changed fc = PROHIBITED
Attard 0.4Ec inserted into R10 = PROHIBITED
Zhou composite-wall material constants inserted into RC = PROHIBITED
steel-shell Gauss/cells = PROHIBITED
PBL automatic spring energy/additive axial load = PROHIBITED
```

---

# 14. UHPC / steel-shell / PBL current boundaries

```text
UHPC final multiaxial current operator = OPEN
UHPC only forced retained fc = 141.1 MPa
UHPC-C0 = historical executed calculable baseline, not production operator
steel-shell production material/operator = NOT YET FROZEN
PBL = strong local boundary / subpanel divider
PBL != automatic independent axial load term
PBL != automatic spring energy
```

The structural analytic architecture may be portable, but UHPC/steel-shell material maps, domains and tangents must be source-specific and separately frozen.

---

# 15. Repository lag / conflicting current records

Latest GitHub HEAD before this recovery was the 18:02 Case21 closure series. Current user-visible corrections after that outrank stale fields.

Recovered conflicts：

1. `current/CURRENT_STATE.md` records Case21 experimental 336 kN as comparison object; this is buckling-load identity and is wrong for ultimate/failure comparison. Earlier governance already records Case21 failure load `82.8 kip = 368.312750 kN` after blind theory freeze.
2. `current/CURRENT_STATE.md` still says Swartz24 recalculation not authorized; user has since explicitly authorized a fresh blind 24-panel calculation.
3. 17:34 unified theory/contract omitted the active material-native `Λ_M` vs structural-reachable `Λ_R` hierarchy.
4. Case21 narrow `[λ_a,λ_b]` identity has not yet been reconciled against the restored `Λ_M` hierarchy; do not guess or re-invent its provenance.

Therefore：

```text
CURRENT_STATE = REPOSITORY_STATE_LAG
CASE21_336kN_ULTIMATE_COMPARISON = INVALID IDENTITY
CASE21_FAILURE_LOAD_FOR_Pu_VALIDATION = ~368.313 kN
SWARTZ24_FRESH_BLIND_RECALC_AUTHORIZATION = YES BY CURRENT USER
```

No numerical Case21/Swartz result is recalculated in this recovery.

---

# 16. Unresolved interfaces after FULL recovery

The recovery itself is complete; the following are genuine interfaces that remain unresolved and must not be filled by invention：

1. **Current R10 exact numerical material-native spectral domain `Λ_M`**: hierarchy is recovered and active; historical R05 numerical domain cannot automatically be copied into current R10 without reconciliation.
2. **Current narrow compiler interval identity/provenance**: `[-1.15,0.12]` etc. cannot be assumed to be `Λ_M`; current 17:34 text omitted this distinction.
3. **Specific universal coincidence tolerance for `K_Z=0` vs first limit point**: later calculation used a local `~1e-4` classification scale, but universal governing provenance was not found in recovered files.
4. **Material/tangent fidelity acceptance numeric threshold**: current theory requires full-interval `E_F^(0),E_F^(1)` reporting and prior engineering gates, but no new theorem-level universal cutoff was frozen; do not invent one.

These are not invitations to create new rules. They are the exact places where the recovered governing layer must be reconciled from existing evidence before next production batch.

---

# 17. Source map used in this recovery

Primary current/governance sources include：

- `START_HERE.md`
- `current/CURRENT_STATE.md`
- `governance/SOURCE_OF_TRUTH_POLICY.md`
- `governance/RECOVERY_PROTOCOL.md`
- `governance/SYNC_PROTOCOL.md`
- `governance/FULL_STARTUP_RECOVERY_AND_ARCHITECTURE_CONTINUITY_20260810.md`
- `governance/PRIORITY_RESET_20260810.md`
- `governance/EXPLICIT_END_TO_END_CAPACITY_DOCTRINE_20260810.md`
- `governance/EXPLICIT_EXECUTION_EVIDENCE_RULE_20260810.md`
- `governance/MATERIAL_NATIVE_SPECTRAL_DOMAIN_RULE_20260810.md`
- `governance/MATERIAL_NATIVE_SCALAR_DOMAIN_CONTRACT_R05_20260810.md`
- `governance/R10_R10B_IDENTITY_AND_INTERPRETATION_CLARIFICATION_20260811.md`
- `governance/N48_C1_VALUE_TANGENT_REPAIR_DECISION_20260811.md`
- `governance/N48_C1_TENSILE_MINIMAX_BOUNDARY_LAYER_DECISION_20260812.md`
- `current/governance/NZ_SCCM_NC_R1_FORMAL_CLOSURE_DECISION_20260812.md`
- `current/governance/NZ_SCCM_NC_R1_LIMIT_ROOT_PRODUCTION_CONTRACT_V1_20260812.md`
- `current/governance/NZ_SCCM_NC_R1_ZHOU_STYLE_FORMAL_DERIVATION_DECISION_20260812.md`
- `current/theory/NZ_SCCM_NC_R1_ZHOU_STYLE_FORMAL_EQUATION_DERIVATION_20260812.md`
- `current/theory/NZ_SCCM_NC_REBAR_ZERO_SPATIAL_ANALYTIC_LIMIT_TANGENT_UNIFIED_THEORY_20260812_1734.md`
- `current/workflows/NZ_SCCM_CASE21_ZERO_SPATIAL_ANALYTIC_EXECUTION_CONTRACT_20260812_1734.md`
- `current/workflows/NZ_SCCM_CASE21_N48C1MM_D15_SELF_CONTAINED_BLIND_CONTRACT_V2_20260812.md`
- `evidence/materials/NC/Nguyen_source_map.md`
- `evidence/literature/NZ_SCCM_ZHOU_ATTARD_TANGENT_STABILITY_INTERPRETATION_20260811.md`
- `history/ledgers/HISTORICAL_COMPONENT_LEDGER.md`
- `history/NZ_SCCM/R04_MATERIAL_DOMAIN_AND_NAMED_KERNEL_REFRAME_20260810.md`
- `history/NZ_SCCM/R05_MATERIAL_NATIVE_DOMAIN_AND_COMPACTIFICATION_20260810.md`
- `history/Case21/material_compiler/R5_REPORT.md`
- `history/Case21/common_policy/REPORT_R2.md`

Latest user-visible corrections are also binding where they supersede stale repository summaries.

---

# 18. Recovery stop condition

```text
FULL THEORY RECOVERY = COMPLETE
FULL EXECUTION CONTRACT RECOVERY = COMPLETE
NEW CALCULATION = NO
NEW MATERIAL MODEL = NO
NEW COMPILER COVERAGE RULE = NO
R10 CHANGE = NO
N48 ORDER CHANGE = NO
D15 CHANGE = NO
ROOT CONTRACT CHANGE = NO
ZHOU SECOND Pu SOLVER = NO
```

Before any next production calculation, the recovered omitted `Λ_M/Λ_R` domain layer must be carried back into the governing timestamped theory/contract **as restoration of existing governance, not as a new theory invention**. No Case21/Swartz root or experiment is allowed to determine that restoration.