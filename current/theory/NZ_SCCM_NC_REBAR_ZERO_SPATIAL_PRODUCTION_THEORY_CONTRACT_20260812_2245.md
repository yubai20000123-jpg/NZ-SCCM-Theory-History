# NZ-SCCM 普通混凝土 + 钢筋板零空间解析极限承载力—切线稳定生产理论合同

**时间基线：2026-08-12 22:45 +08:00**  
**身份：CURRENT PRODUCTION THEORY + EXECUTION CONTRACT**  
**形成原则：以 2026-08-11 Swartz24 fresh production 的已成功计算链为 operational baseline，只并入 2026-08-12 formal closure 已明确接受的公式修复与 compiler 报告要求；不新增任何未经证明的约束、材料机制、搜索边界或莫须有 gate。**

---

# 0. 本合同的唯一目的

本合同把已经成功用于 Swartz 24 块板的 fresh production 流程，与 2026-08-12 更晚的 formal closure 合并成一套可直接用于：

1. Swartz24 fresh blind recomputation；
2. Case21 逐式演算；
3. 任意额外、且满足同一结构/材料适用范围的 RC 板试件；
4. 最终 theory-freeze 后与试验 failure/ultimate load 比较。

本合同**不是新理论**，不重新建立 compiler coverage，不新增 `Lambda_M/Lambda_R` 运行时方程，不新增 `D_max/q_max`，不重新打开 R10，不提高 N48 阶数，不增加空间积分点。

```text
NO_NEW_THEORY = YES
NO_NEW_MATERIAL_MECHANISM = YES
NO_NEW_RUNTIME_DOMAIN_EQUATION = YES
NO_ARTIFICIAL_DMAX_QMAX = YES
NO_PANEL_CALIBRATION = YES
NO_EXPERIMENT_IN_SOLVE = YES
```

---

# 1. 现有公式一致性检查结论

对 2026-08-11 fresh Swartz24 production、2026-08-12 N48-C1/MM closure、formal D15 closure、limit-root contract 与 Zhou/Navier tangent closure 逐项核对后：

```text
CORE_MECHANICS_CONFLICT = NO
R10_CONFLICT = NO
NGUYEN_KINEMATICS_CONFLICT = NO
CH_CONFLICT = NO
P/Rq/L_DEFINITION_CONFLICT = NO
REBAR_ANALYTIC_MAPPING_CONFLICT = NO
LIMIT_ROOT_TOPOLOGY_CONFLICT = NO
TANGENT_AS_SECOND_Pu_SOLVER = NO
```

需要并入的只有已经明确批准的两类更新：

1. **compiler representation update**：`U/C/T7 = N48-C1`，`T = N48-C1-CONSTRAINED-MINIMAX`；
2. **formal algebra update**：所有最终 scalar integrand 采用 `D15_GENERAL_TRIG_MOMENTS`，并对每个新的 compiler interval 报告 full-hull value/first-tangent error。

2026-08-11 的 24 板数值表是成功 operational baseline / historical fresh result；若按本合同重新生产，必须用当前 C1/MM + general-D15 重新生成 coefficient 与结构结果，不能把旧数值直接冒充新计算输出。

---

# 2. 固定理论身份

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
ACTIVE_MODE = m=1
KINEMATICS = NGUYEN_SECOND_ORDER
R10_MATERIAL_TARGET = FROZEN
N48_ORDER = 48
U_COMPILER = N48-C1
C_COMPILER = N48-C1
T7_COMPILER = N48-C1
T_COMPILER = N48-C1-CONSTRAINED-MINIMAX
CAYLEY_HAMILTON = GOVERNING
EXACT_MOMENT_ENGINE = D15_GENERAL_TRIG_MOMENTS
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
STRUCTURAL_CALIBRATION = NO
PANEL_LEVEL_SURROGATE = NO
```

49 个 N48 Chebyshev 根只是一维材料坐标，用于生成有限解析 coefficient；不是结构空间积分点。

数学 root backend 可内部 Newton / elimination / resultant / root isolation；这不改变理论的非加载步、零空间离散身份。

---

# 3. 对一个任意新增板件所需的原始输入

只要一个新试件属于当前理论适用的 RC 板类，并能给出以下原始参数，就可以直接进入同一计算链：

## 3.1 几何与缺陷

\[
\boxed{b,\ \ell,\ t_p,\ A_0}
\]

或

\[
\boxed{b,\ \ell,\ t_p,\ q_0=A_0/b}.
\]

式中，\(b\) 为代表完整半波横向宽度；\(\ell\) 为轴向完整半波长度；\(t_p\) 为板厚；\(A_0\) 为 stress-free initial imperfection amplitude。

## 3.2 普通混凝土

\[
\boxed{f_c,\ E_0,\ \varepsilon_0,\ \nu}.
\]

这些量来自试件/材料本身的测量或已批准材料来源关系；不得由该板的 ultimate load 反标。

## 3.3 钢筋

\[
\boxed{E_s,\ f_y,\ \varepsilon_y,\ \rho_{s,\alpha}^{(r)},\ z_s^{(r)},\ \theta_\alpha}.
\]

式中 \(r\) 为层号，\(\alpha\) 为方向；\(z_s^{(r)}\) 为钢筋层相对中面位置。

## 3.4 compiler interval

每块板沿用 2026-08-11 fresh production 的既有 operational policy：在求结构根以前声明本板的一维材料 compiler interval

\[
\boxed{\lambda\in[\lambda_a,\lambda_b]}.
\]

不得依据该板试验 ultimate load、历史 theory root 或历史 predicted Pu 调整该区间。

本合同**不重新发明 interval 生成规则**；沿用已成功生产流程。求解后必须给出完整连续谱域 certificate，证明 current reachable principal values 落在已声明区间内。

---

# 4. R10 ordinary-concrete current target

定义

\[
\boxed{\kappa=\frac{E_0\varepsilon_0}{f_c}},\qquad
\boxed{\rho=0.1},\qquad
\boxed{x_{cr}=\frac{\rho}{\kappa}},\qquad
\boxed{\eta=\frac{x_{cr}}{20}}.
\]

物理面内应变

\[
\boxed{\mathbf E=\begin{bmatrix}
\varepsilon_x&\gamma_{xy}/2\\
\gamma_{xy}/2&\varepsilon_y
\end{bmatrix}}.
\]

R10 equivalent-uniaxial tensor

\[
\boxed{\mathbf E_u=\frac{(1-\nu)\mathbf E+\nu\operatorname{tr}(\mathbf E)\mathbf I}{1-\nu^2}},
\qquad
\boxed{\mathbf X=\frac{\mathbf E_u}{\varepsilon_0}}.
\]

\[
X_{11}=\frac{\varepsilon_x+\nu\varepsilon_y}{(1-\nu^2)\varepsilon_0},\qquad
X_{22}=\frac{\nu\varepsilon_x+\varepsilon_y}{(1-\nu^2)\varepsilon_0},
\]

\[
X_{12}=X_{21}=\frac{\gamma_{xy}}{2(1+\nu)\varepsilon_0}.
\]

\[
\mu=\frac{X_{11}+X_{22}}2,\qquad
\delta=\frac{X_{11}-X_{22}}2,\qquad
r_X=\sqrt{\delta^2+X_{12}^2},
\]

\[
\boxed{\lambda_\pm=\mu\pm r_X}.
\]

R10 one-sided coordinate：

\[
\boxed{\Pi_\eta(z)=\frac{z^2(\sqrt{z^2+\eta^2}+z)}{2(z^2+\eta^2)}}.
\]

\[
\boxed{c(\lambda)=\Pi_\eta(-\lambda)},\qquad
\boxed{t(\lambda)=\Pi_\eta(\lambda)}.
\]

Compression primitive：

\[
\boxed{C(\lambda)=\frac{\kappa c(\lambda)}{1+(\kappa-2)c(\lambda)+c(\lambda)^2}}.
\]

Foster-informed tensile source：

\[
\boxed{m_t=-\frac7{90}},\qquad \boxed{\eta_r=0.05},
\]

\[
H(r,r_0)=\frac12[(r-r_0)+\sqrt{(r-r_0)^2+\eta_r^2}]
-\frac12[-r_0+\sqrt{r_0^2+\eta_r^2}],
\]

\[
T_{src}(r)=r+(m_t-1)H(r,1)-m_tH(r,10),
\]

\[
\boxed{W_{src}=\rho x_{cr}\int_0^{10}T_{src}(r)\,dr}.
\]

该积分是材料坐标解析积分，不是结构空间 quadrature。

定义

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
\boxed{h=\frac15\left(\frac{W_{src}}{x_{cr}}-\frac{\rho}{10}-\frac92u_r\right)}.
\]

\[
u_{sm}(t)=
\begin{cases}
u_1(t/x_{cr}),&0\le t\le x_{cr},\\
u_2[(t-x_{cr})/(9x_{cr})],&x_{cr}<t\le10x_{cr},\\u_r,&t>10x_{cr}.
\end{cases}
\]

\[
\boxed{T(\lambda)=\frac{u_{sm}[\Pi_\eta(\lambda)]}{\rho}},\qquad
\boxed{T^{(7)}(\lambda)=T(\lambda)^7}.
\]

\[
\boxed{U(\lambda)=\kappa\lambda-C(\lambda)+\kappa c(\lambda)+\rho T(\lambda)-\kappa t(\lambda)}.
\]

\[
\boxed{a_{cc}=0.1072329249362415},\qquad
\boxed{a_t=1-2^{-1/8}}.
\]

主方向 current response：

\[
s_+=U_+-a_{cc}C_+^2C_-+C_+T_- -\rho a_tT_+T_-^8,
\]

\[
s_-=U_--a_{cc}C_-^2C_++C_-T_+ -\rho a_tT_-T_+^8.
\]

R10 anchors：

\[
U(0)=0,\quad U'(0)=\kappa,
\]

\[
C(0)=T(0)=T^{(7)}(0)=0,
\]

\[
C'(0)=T'(0)=[T^{(7)}]'(0)=0.
\]

---

# 5. N48-C1/MM finite analytic compiler

\[
\lambda_c=\frac{\lambda_a+\lambda_b}{2},\qquad
\lambda_h=\frac{\lambda_b-\lambda_a}{2},\qquad
\xi(\lambda)=\frac{\lambda-\lambda_c}{\lambda_h}.
\]

49 个材料根：

\[
\boxed{\theta_j=\frac{(j+1/2)\pi}{49}},\qquad
\boxed{\lambda_j=\lambda_c+\lambda_h\cos\theta_j},\quad j=0,\ldots,48.
\]

Direct coefficients：

\[
\boxed{a_n^{(F,0)}=\frac{2-\delta_{n0}}{49}\sum_{j=0}^{48}F(\lambda_j)\cos(n\theta_j)},
\]

\[
F\in\{U,C,T,T^{(7)}\}.
\]

定义

\[
V_{jn}=\cos(n\theta_j),\qquad
H=V^TV=\operatorname{diag}(49,49/2,\ldots,49/2),
\]

\[
H^{-1}=\frac1{49}\operatorname{diag}(1,2,\ldots,2),
\qquad
\xi_0=-\frac{\lambda_c}{\lambda_h}.
\]

C1 constraint matrix：

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
\boxed{a^{(F,C1)}=a^{(F,0)}+H^{-1}G^T(GH^{-1}G^T)^{-1}(d_F-Ga^{(F,0)})}.
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
E_T^*=\min_{a\in\mathcal F_T}\|p_a-T_{R10}\|_{L^\infty([\lambda_a,\lambda_b])},
\]

\[
\mathcal S_T^*=\{a\in\mathcal F_T:\|p_a-T_{R10}\|_\infty=E_T^*\},
\]

\[
\boxed{a^{(T,MM)}=\arg\min_{a\in\mathcal S_T^*}\frac12(a-a^{(T,C1)})^TH(a-a^{(T,C1)})}.
\]

## 5.1 每个新的 compiler interval 必须输出的材料报告

对每个

\[
F\in\{U,C,T,T^{(7)}\}
\]

报告：

\[
\boxed{F_{48}(0),\quad F'_{48}(0)},
\]

\[
\boxed{E_F^{(0)}=\|F_{48}-F_{R10}\|_{L^\infty([\lambda_a,\lambda_b])}},
\]

\[
\boxed{E_F^{(1)}=\lambda_h\|F'_{48}-F'_{R10}\|_{L^\infty([\lambda_a,\lambda_b])}}.
\]

并报告：

- near-zero tensile boundary-layer T error；
- `max |a_n|` / coefficient simplicity；
- CH compatibility；
- D15 compatibility。

**重要：上述 full-hull `E_F^(0), E_F^(1)` 在当前 closure 中是必须报告的 fidelity information；本合同不新增一个新的 universal reject threshold。**

继续保持已有工程接受证据：

```text
C1_ORIGIN_ANCHORS = REQUIRED
NEAR_ZERO_T_VALUE_GATE = EXISTING
O1_COEFFICIENT_SIMPLICITY = EXISTING
CAYLEY_HAMILTON_COMPATIBILITY = REQUIRED
D15_COMPATIBILITY = REQUIRED
NO_NEW_THEOREM_LEVEL_REMAINDER_GATE = YES
```

---

# 6. Cayley-Hamilton 2D lift

\[
\boxed{Y=\frac{X-\lambda_cI}{\lambda_h}},\qquad
K_1=\operatorname{tr}Y,\qquad K_2=\det Y.
\]

\[
Y^2-K_1Y+K_2I=0.
\]

\[
\mathcal C_n(Y)=A_nI+B_nY,
\]

\[
A_0=1,\ B_0=0,\qquad A_1=0,\ B_1=1,
\]

\[
A_{n+1}=-2K_2B_n-A_{n-1},
\]

\[
B_{n+1}=2A_n+2K_1B_n-B_{n-1}.
\]

每个 finite primitive：

\[
F_{48}(X)=\sum_{n=0}^{48}a_n^{(F,*)}\mathcal C_n(Y)=A_FI+B_FY.
\]

Interaction tensors：

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
\boxed{S=U-a_{cc}CC+TC-\rho a_tTT},
\qquad
\boxed{\sigma=f_cS}.
\]

---

# 7. Nguyen second-order complete-halfwave kinematics

\[
X=\frac{\pi x}{b},\qquad Y=\frac{\pi y}{\ell},\qquad \zeta=\frac{2z}{t_p}.
\]

\[
w_0=A_0\sin X\sin Y,\qquad w_1=A\sin X\sin Y,
\]

\[
q_0=\frac{A_0}{b},\qquad q=\frac{A}{b}.
\]

No-load state：

\[
\boxed{(D,q)=(0,0)}.
\]

\[
\chi_q=q_0q+\frac12q^2.
\]

General rectangular coefficients：

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

\[
\boxed{e_x=\nu D+C_{mx}\cos^2X\sin^2Y+C_{bx}\sin X\sin Y\,\zeta},
\]

\[
\boxed{e_y=-D+C_{my}\sin^2X\cos^2Y+C_{by}\sin X\sin Y\,\zeta},
\]

\[
\boxed{g_{xy}=C_{mxy}\sin X\cos X\sin Y\cos Y+C_{bxy}\cos X\cos Y\,\zeta}.
\]

\[
\varepsilon_x=\varepsilon_0e_x,\qquad
\varepsilon_y=\varepsilon_0e_y,\qquad
\gamma_{xy}=\varepsilon_0g_{xy}.
\]

给定 \((D,q)\)，整个连续完整半波应变场唯一确定。

---

# 8. general-D15 exact moments

所有最终 scalar integrand 统一写为

\[
\boxed{Q(X,Y,\zeta)=\sum_{p,r,u,s,h}c_{prush}\sin^pX\cos^rX\sin^uY\cos^sY\zeta^h}.
\]

\[
J_{pr}=\int_0^\pi\sin^pX\cos^rX\,dX
=\begin{cases}
0,&r\text{ odd},\\
B((p+1)/2,(r+1)/2),&r\text{ even},
\end{cases}
\]

\[
Z_h=\int_{-1}^{1}\zeta^h\,d\zeta
=\begin{cases}
0,&h\text{ odd},\\
2/(h+1),&h\text{ even}.
\end{cases}
\]

\[
\boxed{\mathscr D[Q]=\sum c_{prush}J_{pr}J_{us}Z_h}.
\]

\[
\boxed{J_\Omega=\frac{b\ell t_p}{2\pi^2}}.
\]

该 general-D15 无例外应用于：

```text
Syy
Qq = S : e_,q
all same-expression derivative integrands used by P_D,P_q,Rq,D,Rq,q
current-tangent material integrands
current-stress geometric integrands
rebar tangent/geometric integrands when needed
```

restricted sine-only form只有在对具体 scalar integrand 证明代数等价时才是允许的退化实现。

---

# 9. Concrete axial load and q-equilibrium

\[
\boxed{P_c=-\frac{f_cbt_p}{2\pi^2}\mathscr D[S_{yy}]}.
\]

定义

\[
\boxed{Q_q=S:e_{,q}}.
\]

\[
\boxed{R_{q,c}=f_c\varepsilon_0J_\Omega\mathscr D[Q_q]}.
\]

这里 \(P_c\) 的身份是 representative complete-halfwave average axial load observable。

---

# 10. Rebar analytic contribution

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
\boxed{\varepsilon_{s,\alpha}^{(r)}=n_\alpha^TE(X,Y,\zeta_r)n_\alpha}.
\]

\[
t_{s,\alpha}^{(r)}=\rho_{s,\alpha}^{(r)}t_p.
\]

\[
\boxed{P_s=-\sum_{r\parallel y}\frac{t_{s,y}^{(r)}}{\ell}\int_A\sigma_{s,y}^{(r)}\,dA},
\]

\[
\boxed{R_{q,s}=\sum_{r,\alpha}t_{s,\alpha}^{(r)}\int_A\sigma_{s,\alpha}^{(r)}\frac{\partial\varepsilon_{s,\alpha}^{(r)}}{\partial q}\,dA}.
\]

在一个新板件上，钢筋只需按 frozen source law 与实际层位/方向代入；不引入板级经验参数。

若实际连续钢筋场在求得的相关主支状态内保持同一个已支持材料支，则直接闭式计算。若真的跨入尚无 analytic closure 的支路，则报告事实；不得用试验值或空间材料点修补。

---

# 11. Total P, Rq and same-expression derivatives

\[
\boxed{P(D,q)=P_c(D,q)+P_s(D,q)},
\]

\[
\boxed{R_q(D,q)=R_{q,c}(D,q)+R_{q,s}(D,q)}.
\]

同一个有限解析表达直接求：

\[
\boxed{P_D,\ P_q,\ R_{q,D},\ R_{q,q}}.
\]

允许 analytic differentiation / forward AD；不允许用空间 finite differences 替代。

定义 limit function：

\[
\boxed{L(D,q)=P_DR_{q,q}-P_qR_{q,D}}.
\]

---

# 12. Primary equilibrium branch and production limit root

Equilibrium set：

\[
\mathcal E=\{(D,q):R_q(D,q)=0\}.
\]

No-load origin：

\[
\boxed{(D,q)=(0,0)}.
\]

Primary branch：

\[
\boxed{\Gamma_0=\operatorname{Conn}_{(0,0)}(\mathcal E\cap\mathcal A)}.
\]

在 regular point：

\[
\nabla R_q=(R_{q,D},R_{q,q})\ne0,
\]

\[
t_0=(R_{q,q},-R_{q,D}),
\]

\[
\nabla P\cdot t_0=L.
\]

沿从 origin 指向加载方向的有向主支：

\[
g(s)=\frac{dP}{ds}.
\]

Production limit candidate 必须是从 origin 遇到的第一个

\[
\boxed{R_q=0,\qquad L=0,\qquad g:+\rightarrow-}.
\]

不得：

```text
select maximum mathematical root
select disconnected high-amplitude branch
select negative-q branch
select closest experimental root
select closest historical root
skip first +->- maximum
```

数值残量沿用现有合同：

\[
R_{mat}=f_c\varepsilon_0J_\Omega,
\]

\[
R_{scale}=\max(R_{mat},|R_{q,c}|+|R_{q,s}|),
\]

\[
\boxed{R_{norm}=\frac{|R_q|}{R_{scale}}\le10^{-5}},
\]

\[
\boxed{L_{norm}=\frac{P_DR_{q,q}-P_qR_{q,D}}{|P_DR_{q,q}|+|P_qR_{q,D}|}},
\qquad
\boxed{|L_{norm}|\le10^{-5}}.
\]

本合同不新增其他 root gate。

---

# 13. Continuous compiler-domain certificate

对求得的相关主支状态，证明完整连续半波上

\[
\boxed{\lambda_a\le\lambda_-(X,Y,\zeta)\le\lambda_+(X,Y,\zeta)\le\lambda_b}.
\]

允许 analytic/Bernstein/interval coefficient enclosure；不允许有限空间点扫描冒充全域证书。

这只是验证已声明 compiler interval 覆盖 current structural spectrum；不是新的材料理论。

---

# 14. Zhou/Navier full-field current-tangent closure

\[
\boxed{\mathbb C_t(X,Y,\zeta;D,q)=\frac{\partial\sigma}{\partial E}}.
\]

由于

\[
X=E_u/\varepsilon_0,
\]

必须保留

\[
\boxed{\delta X=\delta E_u/\varepsilon_0}.
\]

Navier mode：

\[
\varphi=\sin X\sin Y,
\qquad
\alpha=\pi/b,
\qquad
\beta=\pi/\ell.
\]

\[
\varphi_{,x}=\alpha\cos X\sin Y,
\qquad
\varphi_{,y}=\beta\sin X\cos Y,
\]

\[
\varphi_{,xx}=-\alpha^2\varphi,
\qquad
\varphi_{,yy}=-\beta^2\varphi,
\qquad
\varphi_{,xy}=\alpha\beta\cos X\cos Y.
\]

\[
b_\varphi=-z\begin{bmatrix}
\varphi_{,xx}\\
\varphi_{,yy}\\
2\varphi_{,xy}
\end{bmatrix}.
\]

Concrete：

\[
\boxed{K_{Z,c}^{mat}=\int_{\Omega_h}b_\varphi^TC_t^{eng}b_\varphi\,dV},
\]

\[
\boxed{K_{Z,c}^{geo}=\int_{\Omega_h}(\sigma_x\varphi_{,x}^2+2\tau_{xy}\varphi_{,x}\varphi_{,y}+\sigma_y\varphi_{,y}^2)\,dV}.
\]

Steel：

\[
E_{s,t}^{(r,\alpha)}=d\sigma_s/d\varepsilon_s,
\]

\[
\kappa_\varphi=-\begin{bmatrix}
\varphi_{,xx}&\varphi_{,xy}\\
\varphi_{,xy}&\varphi_{,yy}
\end{bmatrix},
\]

\[
\boxed{K_{Z,s}^{mat}=\sum_{r,\alpha}t_{s,\alpha}^{(r)}\int_AE_{s,t}^{(r,\alpha)}[z_s^{(r)}n_\alpha^T\kappa_\varphi n_\alpha]^2dA},
\]

\[
\boxed{K_{Z,s}^{geo}=\sum_{r,\alpha}t_{s,\alpha}^{(r)}\int_A\sigma_{s,\alpha}^{(r)}(n_\alpha\cdot\nabla\varphi)^2dA}.
\]

Total：

\[
\boxed{K_Z=K_{Z,c}^{mat}+K_{Z,c}^{geo}+K_{Z,s}^{mat}+K_{Z,s}^{geo}}.
\]

Interpretation：

```text
K_Z > 0 : positive modal tangent
K_Z = 0 : modal critical
K_Z < 0 : negative modal tangent
```

Zhou/Navier tangent 是同一 equilibrium branch 上的 current-tangent stability acceptance / control interpretation；**不是第二套 Pu solver**。

如果 first `+->-` limit candidate 以前未出现 `K_Z=0`，则 limit candidate 保持当前生产极限候选身份；若确实更早出现 tangent loss，则只报告真实的 control ordering，不凭空创造经验折减。

---

# 15. 对一个额外试验板的直接可计算性检查

对一个未参与任何现有 Swartz24 历史计算的新试件，只要：

1. 它属于当前 one-complete-halfwave / Nguyen second-order / m=1 的结构类；
2. §3 的材料、几何、缺陷与钢筋原始输入齐全；
3. 在求解前按现有 production policy 声明 compiler interval；

则从公式层面可直接执行：

```text
raw specimen data
-> R10
-> fresh N48-C1/MM coefficients for this specimen interval
-> material fidelity report
-> Nguyen continuous strain field
-> CH current stress
-> general-D15 exact moments
-> Pc,Rq,c
-> Ps,Rq,s
-> P,Rq,L
-> Gamma0
-> first +->- limit candidate
-> current K_Z
-> theory freeze
-> only then read experimental failure/ultimate load
```

所有公式只依赖原始 specimen/material inputs 和 frozen project constants；没有 Case number、Swartz experimental load 或 historical predicted Pu 进入任何结构方程。

因此：

```text
EXTRA_CONFORMING_SPECIMEN_CALCULABILITY = YES
CASE_ID_DEPENDENCE = NO
EXPERIMENTAL_LOAD_DEPENDENCE = NO
HISTORICAL_ROOT_DEPENDENCE = NO
```

若某篇文献缺少 §3 的必要原始输入，应记为 `INPUT_INCOMPLETE`，而不是由试验 ultimate load 反推材料参数。

---

# 16. Fresh blind validation contract

对 Swartz24 或其他学者试验板，求解阶段禁止读取：

```text
historical D,q,Pu
historical FE/Gauss results
historical root path
experimental buckling/ultimate/failure load
```

先冻结全部理论结果，再读取原论文的对应实验量。

极限承载力理论必须与 experimental failure/ultimate load 对比；experimental buckling load 只有在明确做 Pcr validation 时才可作为比较对象。

---

# 17. 每块板的标准输出

每一个 production specimen 至少输出：

1. raw input table；
2. R10 derived parameters；
3. declared compiler interval；
4. fresh 49×4 coefficient table；
5. C1 origin anchors；
6. `E_F^(0), E_F^(1)` for U/C/T/T7；
7. near-zero T / coefficient simplicity / CH-D15 compatibility report；
8. continuous compiler-domain certificate；
9. steel strain/branch report；
10. `D_u,q_u,A_u`；
11. `Pc,Ps,Pu`；
12. `Rq,c,Rq,s,R_norm`；
13. `P_D,P_q,Rq,D,Rq,q,L_norm`；
14. proof of first `+->-` maximum；
15. `K_Z,c^mat,K_Z,c^geo,K_Z,s^mat,K_Z,s^geo,K_Z`；
16. control ordering；
17. theory freeze marker；
18. experimental failure/ultimate load read afterwards；
19. theory/experiment ratio and error；
20. source-based physical discussion, with no calibration.

---

# 18. Explicit non-constraints

以下对象不得因为恢复历史或看到旧治理文件而擅自升级成新 blocker：

```text
new Lambda_M/Lambda_R runtime equations
new universal compiler interval
new Dmax/qmax
new strict remainder certificate
new N96/N112 escalation
new material point state machine
new spatial cells
new Gauss/Simpson/adaptive integration
new panel correction factor
new root-selection heuristic
new experiment-driven material parameter
new second Pu solver
```

只有当前正式方程本身出现确定代数冲突，或某个新 specimen 实际触发 frozen source-law incompatibility 时，才报告对应真实问题；不得预先制造问题。

---

# 19. Final production chain

\[
\boxed{
\begin{aligned}
&\text{raw specimen/material inputs}
\\&\to R10
\\&\to \text{declared compiler interval}
\\&\to N48\text{-}C1/MM + full-hull fidelity report
\\&\to Nguyen\ \text{continuous complete halfwave}
\\&\to Cayley\!\!\text{-}Hamilton\ \text{current map}
\\&\to general\text{-}D15\ \text{exact moments}
\\&\to P_c,R_{q,c},P_s,R_{q,s}
\\&\to P,R_q,P_D,P_q,R_{q,D},R_{q,q},L
\\&\to \Gamma_0
\\&\to \text{first }+\to-\text{ limit candidate}
\\&\to \text{continuous domain/steel/residual checks}
\\&\to K_Z\ \text{on the same branch}
\\&\to \text{theory result freeze}
\\&\to \text{experimental failure/ultimate comparison}.
\end{aligned}}
\]

```text
THEORY_CONTRACT_FORMULA_CONSISTENCY = PASS
EXTRA_CONFORMING_SPECIMEN_CALCULABILITY = PASS
NEW_CONSTRAINT_ADDED = NO
SWARTZ24_OPERATIONAL_BASELINE = RETAINED
20260812_FORMAL_CLOSURE_UPDATES = INCORPORATED
```
