# NZ-SCCM Case21 零空间解析极限—切线稳定统一计算合同

**时间基线：2026-08-12 17:34 +08:00**  
**文件身份：CURRENT GOVERNING CASE21 EXECUTION CONTRACT**  
**理论基线：`current/theory/NZ_SCCM_NC_REBAR_ZERO_SPATIAL_ANALYTIC_LIMIT_TANGENT_UNIFIED_THEORY_20260812_1734.md`**

---

# 0. 命名与版本纪律

本合同及其后续替代文件不再使用 V1/V2/R1/R2 等序号作为主命名。后续正式文件采用：

```text
<内容描述>_YYYYMMDD_HHMM.<ext>
```

若后续同一日再次修订，以新的小时分钟时间戳建立新的治理基线；旧文件保留为历史证据，不删除、不覆盖其历史身份。

---

# 1. 隔离纪律

Case21 正式计算只允许读取：

1. 当前时间戳理论基线；
2. Case21 原始材料、几何与配筋输入；
3. 从当前 R10 重新生成的材料 coefficient；
4. 当前计算过程中由同一解析表达新生成的中间量。

禁止：

```text
HISTORICAL_CASE21_D_Q_P_Pu_ROOT_PATH = FORBIDDEN
HISTORICAL_CASE21_ANALYTIC_RESULT = FORBIDDEN
HISTORICAL_FE_GAUSS_SIMPSON_RESULT = FORBIDDEN
HISTORICAL_MATERIAL_POINT_HISTORY = FORBIDDEN
EXPERIMENT_DURING_SOLVE = FORBIDDEN
EXPERIMENT_FOR_ROOT_SELECTION = FORBIDDEN
EXPERIMENT_FOR_PARAMETER_TUNING = FORBIDDEN
EXPERIMENT = FINAL COMPARISON ONLY AFTER THEORY RESULT FREEZE
```

正式空间身份固定为

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
ACTIVE_MODE = m=1
KINEMATICS = NGUYEN_SECOND_ORDER
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
```

49 个 N48 Chebyshev 根只是一维材料坐标，不是结构空间采样点。

---

# 2. 唯一正式计算链

Case21 只允许按下列顺序执行：

\[
\boxed{
\text{原始输入}
\rightarrow R10
\rightarrow N48\text{-}C1/MM
\rightarrow \mathrm{Cayley\!\!-Hamilton}
\rightarrow \mathrm{Nguyen\ 完整连续半波}
\rightarrow \mathrm{general\ D15}
\rightarrow P(D,q),R_q(D,q),L(D,q)
\rightarrow \Gamma_0
\rightarrow \text{first }+\to-\text{ limit candidate}
\rightarrow K_Z\text{ on same }\Gamma_0
\rightarrow \text{final control verdict}
\rightarrow \text{experiment-only comparison}
}
\tag{C1}
\]

式中，\(P\) 为总轴向荷载 observable；\(R_q\) 为 q-广义平衡残量；\(L\) 为荷载沿平衡支的切向驻值函数；\(\Gamma_0\) 为包含无载点 \((0,0)\) 的可接受主连通平衡支；\(K_Z\) 为同一个 current material operator 产生的 Zhou/Navier full-field current tangent。

任何历史 Case21 理论值不得用于初始化、括根、排序、选根或判断路径方向。

---

# 3. Case21 原始输入区

Case21 计算启动时必须显式列出并冻结：

\[
\boxed{b,\ \ell,\ t_p}
\tag{C2}
\]

式中，\(b\) 为完整代表半波宽度，mm；\(\ell\) 为轴向完整半波长度，mm；\(t_p\) 为板厚，mm。

\[
\boxed{f_c,\ E_0,\ \varepsilon_0,\ \nu}
\tag{C3}
\]

式中，\(f_c\) 为混凝土抗压强度，MPa；\(E_0\) 为初始弹性模量，MPa；\(\varepsilon_0\) 为 R10 参考压缩应变；\(\nu\) 为泊松比。

\[
\boxed{q_0=A_0/b}
\tag{C4}
\]

式中，\(A_0\) 为 stress-free initial imperfection 物理幅值，mm；\(q_0\) 为初始缺陷比。

\[
\boxed{E_s,\ f_y,\ \varepsilon_y,\ \rho_{s,\alpha}^{(r)},\ z_s^{(r)}}
\tag{C5}
\]

式中，\(E_s\) 为钢筋弹性模量；\(f_y\) 为屈服应力；\(\varepsilon_y\) 为屈服应变；\(\rho_{s,\alpha}^{(r)}\) 为第 \(r\) 层、方向 \(\alpha\) 的配筋率；\(z_s^{(r)}\) 为该层钢筋相对中面的物理位置。

材料 compiler 区间

\[
\boxed{\lambda\in[\lambda_a,\lambda_b]}
\tag{C6}
\]

式中，\(\lambda_a,\lambda_b\) 为求根前冻结的一维材料主等效应变范围；不得根据试验荷载或历史理论结果调整。

---

# 4. R10 与 N48-C1/MM 生成门

必须从原始材料参数重新计算

\[
\boxed{\kappa=E_0\varepsilon_0/f_c,\qquad x_{cr}=\rho/\kappa,\qquad \eta=x_{cr}/20}
\tag{C7}
\]

式中，\(\kappa\) 为 R10 无量纲初始斜率；\(x_{cr}\) 为拉伸特征材料坐标；\(\eta\) 为零主应变附近平滑尺度；\(\rho=0.1\) 为当前冻结拉伸强度尺度。

必须重新生成并输出完整

```text
49 × 4 coefficient table:
U_C1
C_C1
T_MM
T7_C1
```

禁止从历史 Case21 coefficient 文件读取 production coefficient。

必须报告：

\[
\boxed{F_{48}(0),\qquad F_{48}'(0)}
\tag{C8}
\]

式中，\(F\in\{U,C,T,T^{(7)}\}\)；这些量用于检查零点 C1 锚点。

必须报告全 compiler 区间的材料值与一阶切线误差：

\[
\boxed{E_F^{(0)}=\|F_{48}-F_{R10}\|_\infty}
\tag{C9}
\]

\[
\boxed{E_F^{(1)}=\lambda_h\|F_{48}'-F_{R10}'\|_\infty}
\tag{C10}
\]

式中，\(E_F^{(0)}\) 为材料值误差；\(E_F^{(1)}\) 为尺度化一阶切线误差；\(\lambda_h=(\lambda_b-\lambda_a)/2\)。

---

# 5. general-D15 强制合同

每一个最终结构标量 integrand 必须化为

\[
\boxed{Q(X,Y,\zeta)=\sum_{p,r,u,s,h}c_{prush}\sin^pX\cos^rX\sin^uY\cos^sY\zeta^h}
\tag{C11}
\]

式中，\(c_{prush}\) 为有限解析系数；\(p,r,u,s,h\) 为非负整数幂次。

精确面内矩为

\[
\boxed{J_{pr}=\int_0^\pi\sin^pX\cos^rX\,dX}
\tag{C12}
\]

式中，\(J_{pr}\) 为完整半波上的一般三角精确矩。

厚度矩为

\[
\boxed{Z_h=\int_{-1}^{1}\zeta^h d\zeta}
\tag{C13}
\]

式中，\(Z_h\) 为归一化厚度精确矩。

所有正式积分统一收缩为

\[
\boxed{\mathscr D[Q]=\sum c_{prush}J_{pr}J_{us}Z_h}
\tag{C14}
\]

式中，\(\mathscr D[Q]\) 为完整连续代表半波上的解析精确积分。

式（C11）—（C14）无例外应用于：

```text
Syy
Qq = S : e_,q
P_D, P_q, Rq,D, Rq,q 所依赖的同源 scalar integrands
current-tangent material integrands
current-stress geometric-stiffness integrands
reinforcement tangent/geometric terms
```

只含 `sin X, sin Y, zeta` 的 restricted basis 仅在对特定最终 scalar integrand 完成严格代数等价证明后才允许作为等价退化实现；不得静默替换 general-D15。

---

# 6. 连续 compiler-domain certificate

给定任一候选 \((D,q)\)，必须证明整个完整半波上两主值满足

\[
\boxed{\lambda_a\le\lambda_-(X,Y,\zeta)\le\lambda_+(X,Y,\zeta)\le\lambda_b}
\tag{C15}
\]

式中，\(\lambda_\pm\) 为 current \(\mathbf X\) 的两个主值；\(\lambda_a,\lambda_b\) 见式（C6）。

允许使用有限 polynomial/Bernstein coefficient enclosure 或等价解析证书；禁止用空间点扫描代替全域证书。

---

# 7. 混凝土荷载与平衡残量

混凝土轴向荷载为

\[
\boxed{P_c=-\frac{f_cbt_p}{2\pi^2}\mathscr D[S_{yy}]}
\tag{C16}
\]

式中，\(S_{yy}\) 为无量纲 current stress tensor 的轴向分量；\(\mathscr D\) 必须使用 general-D15。

定义

\[
\boxed{Q_q=\mathbf S:\frac{\partial\mathbf e}{\partial q}}
\tag{C17}
\]

式中，\(Q_q\) 为无量纲 q-广义功密度；\(\mathbf S\) 为无量纲 current stress tensor；\(\mathbf e=\mathbf E/\varepsilon_0\)；\(\partial\mathbf e/\partial q\) 由 Nguyen 连续运动学解析得到。

混凝土 q-广义残量为

\[
\boxed{R_{q,c}=f_c\varepsilon_0J_\Omega\mathscr D[Q_q]}
\tag{C18}
\]

式中，\(J_\Omega=b\ell t_p/(2\pi^2)\) 为坐标变换 Jacobian；\(\mathscr D[Q_q]\) 必须按式（C11）—（C14）重新生成。

---

# 8. 钢筋 branch 与解析贡献门

必须先证明完整连续钢筋场落在一个受支持材料支内。若当前案例全部弹性，则应满足

\[
\boxed{\max_{X,Y,r,\alpha}|\varepsilon_{s,\alpha}^{(r)}|<\varepsilon_y}
\tag{C19}
\]

式中，\(\varepsilon_{s,\alpha}^{(r)}\) 为第 \(r\) 层、方向 \(\alpha\) 钢筋连续应变；\(\varepsilon_y\) 为屈服应变。

若式（C19）不满足且尚无全域单支解析合同，则

```text
BLOCKED_AT_STEEL_BRANCH
```

不得通过钢筋空间材料点分区继续。

总荷载与总平衡残量为

\[
\boxed{P=P_c+P_s}
\tag{C20}
\]

\[
\boxed{R_q=R_{q,c}+R_{q,s}}
\tag{C21}
\]

式中，\(P_s\) 为钢筋轴向荷载；\(R_{q,s}\) 为钢筋 q-广义残量；两者均由连续钢筋解析关系和 exact moments 得到。

---

# 9. 正确主平衡支与 limit-point candidate

正式平衡条件为

\[
\boxed{R_q(D,q)=0}
\tag{C22}
\]

式中，\(D,q\) 是当前仅有的两个结构广义未知量。

同源偏导为

\[
\boxed{P_D,\ P_q,\ R_{q,D},\ R_{q,q}}
\tag{C23}
\]

式中，所有导数必须由同一个有限解析表达解析求导或 forward AD；禁止用空间有限差分替代。

极限函数为

\[
\boxed{L=P_DR_{q,q}-P_qR_{q,D}}
\tag{C24}
\]

式中，\(L\) 为荷载沿平衡 level set 的切向驻值条件。

主平衡支为

\[
\boxed{\Gamma_0=\operatorname{Conn}_{(0,0)}(\{R_q=0\}\cap\mathcal A)}
\tag{C25}
\]

式中，\(\mathcal A\) 为满足所有 compiler/material/rebar/source gates 的可接受域；\(\Gamma_0\) 为包含无载点的连通分量。

首个 limit-point candidate 必须满足

\[
\boxed{R_q=0,\qquad L=0}
\tag{C26}
\]

并且沿有向 \(\Gamma_0\) 的荷载导数发生

\[
\boxed{+\rightarrow-}
\tag{C27}
\]

式中，式（C27）表示该驻值点确为局部最大值而非最小值。

生产残量门为

\[
\boxed{R_{norm}\le10^{-5},\qquad |L_{norm}|\le10^{-5}}
\tag{C28}
\]

式中，\(R_{norm}\) 和 \(L_{norm}\) 按当前时间戳理论基线中的定义计算。

**重要：只有用同一个 governing general-D15 \(R_q\) 建立的 \(\Gamma_0\) 才具有生产身份。**

---

# 10. current-tangent 强制门

同一个 current material operator 必须产生

\[
\boxed{\mathbb C_t=\frac{\partial\boldsymbol\sigma}{\partial\mathbf E}}
\tag{C29}
\]

式中，\(\mathbb C_t\) 为完整连续 current tangent field。

由于

\[
\boxed{\mathbf X=\mathbf E_u/\varepsilon_0}
\tag{C30}
\]

式中，\(\mathbf X\) 为无量纲等效应变张量；\(\mathbf E_u\) 为等效单轴应变张量，因此方向导数必须满足

\[
\boxed{\delta\mathbf X=\delta\mathbf E_u/\varepsilon_0}
\tag{C31}
\]

式中，\(1/\varepsilon_0\) 为 mandatory tangent scaling；遗漏则 current tangent 尺度错误。

基本 Navier 模态为

\[
\boxed{\varphi=\sin X\sin Y}
\tag{C32}
\]

式中，\(\varphi\) 为与完整代表半波一致的基本稳定微扰形函数。

总模态 current tangent 为

\[
\boxed{K_Z=K_{Z,c}^{mat}+K_{Z,c}^{geo}+K_{Z,s}^{mat}+K_{Z,s}^{geo}}
\tag{C33}
\]

式中，\(K_{Z,c}^{mat}\) 为混凝土 material-tangent 模态刚度；\(K_{Z,c}^{geo}\) 为混凝土 current-stress 几何模态刚度；\(K_{Z,s}^{mat}\) 为钢筋 material-tangent 模态刚度；\(K_{Z,s}^{geo}\) 为钢筋几何模态刚度。四项全部使用 general-D15 exact moments。

Case21 在无载状态的 mandatory regression 为

\[
\boxed{K_Z(0,0)=\frac{E_0t_p^3\pi^4}{12(1-\nu^2)b^2}}
\tag{C34}
\]

式中，\(E_0,t_p,\nu,b\) 均为 Case21 原始输入；该式为方形完整半波、初始线弹性 isotropic degeneration 的解析回归值。

必须先有

```text
ZERO_STATE_TANGENT_REGRESSION = PASS
```

才能接受任何有限幅值 state 的 \(K_Z\)。

---

# 11. 极限点与 tangent-loss 的先后控制

在已经由 correct general-D15 建立的同一个 \(\Gamma_0\) 上，计算

\[
\boxed{K_Z[\Gamma_0(s)]}
\tag{C35}
\]

式中，\(s\) 为从无载点开始的有向主支参数。

若直到首个 \(+\to-\) limit-point candidate 之前始终有

\[
\boxed{K_Z>0}
\tag{C36}
\]

式中，正值表示基本 Navier 模态仍保持正 current tangent；则 limit-point candidate 通过 pre-limit tangent gate。

若先出现

\[
\boxed{K_Z=0}
\tag{C37}
\]

且此时尚未到达首个 \(+\to-\) limit point，则

```text
BLOCKED_AT_PRELIMIT_TANGENT_LOSS
```

后续极大值不得直接冻结为最终容量。本合同不静默把 Zhou tangent root 升级为第二套 Pu solver；若需赋予其最终承载力身份，必须另有明确治理决定。

若 first \(K_Z=0\) 与 first \(+\to-\) limit point 在冻结 root-repeatability tolerance 内重合，则

```text
COUPLED_LIMIT_TANGENT_CONTROL
```

并同时保存 \(R_q,L,K_Z\) 三类残量。

---

# 12. Case21 完整输出清单

只有以下 19 项全部显式输出后，Case21 才允许标记

```text
CALCULATION_CLOSURE = PASS
```

清单：

```text
01 raw Case21 inputs
02 R10 derived parameters
03 fresh 49×4 N48 coefficient table
04 C1/MM material fidelity records
05 continuous compiler-domain certificate
06 general-D15 Syy contraction
07 general-D15 Qq contraction
08 rebar supported-branch certificate
09 corrected Rq=0 primary branch Gamma0
10 first +->- limit candidate + R_norm/L_norm
11 zero-state K_Z regression
12 KZ,c^mat
13 KZ,c^geo
14 KZ,s^mat
15 KZ,s^geo
16 total K_Z along corrected Gamma0
17 proof whether a K_Z=0 state occurs before the first limit maximum
18 final theory result freeze
19 only then experimental comparison
```

第 06—17 项中的任何一项缺失，都不能把候选荷载称为当前理论最终承载力。

---

# 13. 当前 Case21 执行状态

截至本合同时间：

```text
ZERO_STATE_TANGENT_REGRESSION = PASS
GENERAL_D15_Syy_RECHECK = PASS
GENERAL_D15_Qq_RECHECK = FAIL_AGAINST PREVIOUS CASE21 EXECUTION
PREVIOUS_CASE21_GAMMA0 = NOT CURRENTLY ACCEPTED
PREVIOUS_CASE21_LIMIT_LOAD = AUDIT RECORD ONLY
PRODUCTION_TANGENT_GATE = NOT YET REACHED ON A CORRECTED BRANCH
CASE21_COMPLETE_CLOSURE = BLOCKED
```

下一步唯一允许的执行顺序：

```text
fresh general-D15 Qq
-> fresh Rq(D,q)
-> corrected Gamma0 from (0,0)
-> first +->- limit candidate
-> K_Z along the same corrected Gamma0
-> control classification
-> theory result freeze
-> experiment-only comparison
```

不得使用历史 Gauss/Simpson/FE/material-point 结果，也不得用此前 Case21 的任何理论根、荷载或路径作为目标。