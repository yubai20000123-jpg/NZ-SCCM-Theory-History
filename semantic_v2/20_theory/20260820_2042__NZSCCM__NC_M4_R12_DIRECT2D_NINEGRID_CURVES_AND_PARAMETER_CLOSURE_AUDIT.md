# NZ-SCCM — NC-M4-R12-direct2D 九宫格曲线与参数闭合审计

时间：2026-08-20 20:42 +08:00

状态：`VISUAL_CURVE_AUDIT_COMPLETED / DIRECT2D_ADDITIVE_POISSON_FORM_FAILS_FINITE_STRAIN / PARAMETER_CLOSURE_PARTIAL`

## 1. 审计基线

Case21 仅用于给曲线提供一组实际材料尺度，不用于反标任何参数：

- fc = 21.23 MPa
- E0 = 20321 MPa
- eps_c0 = 0.00209
- nu = 0.18
- ft = 0.1 fc = 2.123 MPa（按当前缺失 ft 时的统一规则）

内部派生：

\[
\varepsilon_{cr}=f_t/E_0,
\qquad
\varepsilon_{t0}=0.0967635 f_t/E_0,
\qquad
m_c=E_0\varepsilon_{c0}/f_c.
\]

Case21 有

\[
m_c=2.00051295337.
\]

## 2. 压缩 primitive：与 Nguyen/Saenz Eq. (3.39) 完全同式

当前

\[
C_m(c)=\frac{m_cc}{1+(m_c-2)c+c^2},
\qquad m_c=E_0\varepsilon_{c0}/f_c.
\]

Nguyen 采用的 Saenz 关系 Eq. (3.39) 在单轴峰值 \((f_c,\varepsilon_{c0})\) 下归一化以后恰好就是上式。因此这不是“近似 Foster/Saenz”，而是当前参数约定下的代数同式。

结论：`COMPRESSION_PRIMITIVE_SOURCE_FIDELITY = PASS`。

## 3. 拉伸 T4：与 Nguyen/Foster 参考差异大

当前

\[
T_4(t)=1.07515\frac{t(t+0.09)}{1-0.83t+1.04t^2+0.14t^3},
\qquad
\varepsilon_{t0}=0.0967635 f_t/E_0.
\]

因此 current T4 峰值约出现在

\[
\varepsilon_{t,p}\approx0.152\,\varepsilon_{cr},
\qquad \varepsilon_{cr}=f_t/E_0.
\]

而 Nguyen/Foster reference 在未裂阶段为线性 \(E_0\)，到 \(\varepsilon_{cr}\) 才达到 cracking stress；裂后 tension-stiffening 使用 \(\alpha_1=10\)、\(\alpha_2\in[0.3,0.7]\) 的下降/残余关系。

在 \(\varepsilon=\varepsilon_{cr}\) 处：

\[
T_4\approx0.44891,
\]

而 reference 是 1.0。

结论：`T4_SOURCE_FIDELITY = FAIL / REOPEN REQUIRED`。

## 4. TC compression reduction 参数 k_tc

Nguyen Eq. (3.43)，转为当前正压缩峰值应变幅值约定后：

\[
\gamma_{ref}(r)=
\begin{cases}
1, & 0\le r\le10/17,\\
1/(0.8+0.34r), & r>10/17,
\end{cases}
\qquad r=\varepsilon_t/\varepsilon_{c0}.
\]

当前希望使用无阈值平滑单式

\[
\Gamma_k(r)=\frac1{1+kr^2}.
\]

### Material-area closure（推荐）

在自然材料区间 \(0\le r\le1\) 保持平均 reduction：

\[
\int_0^1\Gamma_k(r)dr
=
\int_0^1\gamma_{ref}(r)dr.
\]

右侧严格为

\[
I_{ref}=\frac{10}{17}+\frac1{0.34}\ln(1.14)=0.973612536489\ldots
\]

左侧为

\[
\frac{\arctan\sqrt{k}}{\sqrt{k}}.
\]

因此 \(k_{tc}\) 定义为唯一正根

\[
\boxed{\frac{\arctan\sqrt{k_{tc}}}{\sqrt{k_{tc}}}=0.973612536489\ldots}
\]

得到

\[
\boxed{k_{tc}=0.0830721554223\ldots}
\]

这是纯材料 source-to-smooth closure，不使用 Case21 Pu 或任何结构试验荷载。

对照：

- L2 material-only closure: \(k=0.104524810106\ldots\)
- r=1 point anchor: \(k=0.14\)

推荐 material-area closure，因为与项目既有“材料功/面积保持”的简化思想一致且不依赖结构样本。

## 5. CC enhancement 参数 k_eta：可以直接由 Foster Eq. (3.17) 闭合

Foster/Nguyen CC strength envelope：

\[
|\sigma_{2p}|/f_c=\frac{1+3.65\alpha}{(1+\alpha)^2},
\qquad \alpha=\sigma_1/\sigma_2.
\]

等双压 \(\alpha=1\)：

\[
|\sigma_p|/f_c=\frac{1+3.65}{4}=1.1625.
\]

当前 CC interaction 在 \(c_1=c_2=1\) 有

\[
\eta(1,1)=1+k_\eta.
\]

因此严格 source-anchor closure：

\[
\boxed{k_\eta=0.1625.}
\]

原候选 0.16 应被 0.1625 supersede；不是结构反标。

## 6. 更严重的新发现：additive Poisson correction 只能通过原点 tangent，不能作为全域 finite-strain coupling

当前 direct2D 提议：

\[
\Pi_1=\frac{\nu E_0}{1-\nu^2}(\varepsilon_2+\nu\varepsilon_1),
\qquad
\Pi_2=\frac{\nu E_0}{1-\nu^2}(\varepsilon_1+\nu\varepsilon_2).
\]

它确实保证四象限在原点拥有标准 plane-stress tangent；但 \(\Pi_i\) 随应变线性无界增长，而压缩/拉伸 primitive 在峰后软化。因此 finite strain 时 \(\Pi_i\) 必然反过来支配应力。

Case21 material scale, equal biaxial physical compression \(\varepsilon_1=\varepsilon_2=-\varepsilon_{c0}\)：

- Foster Eq. (3.17) equal-biaxial peak factor = 1.1625
- 当前 additive-Pi direct2D 在 c=1 已给出 \(|\sigma|/f_c\approx1.60164\)
- c 继续增大时应力再次线性增大，不再存在合理的峰后软化极限。

因此：

\[
\boxed{\texttt{ADDITIVE_POISSON_FINITE_STRAIN_GATE = FAIL}}
\]

这不是 k_tc / k_eta 参数问题，而是 direct2D coupling 的函数形式问题。不能在它修正前把九宫格模型 production-lock。

## 7. Zero-transverse-stress 路径也显示该问题

当前 TC direct2D 从原点出发确实渐近满足 \(\varepsilon_t/|\varepsilon_c|\to\nu\)，但压缩增大后该比值迅速偏离 \(\nu\)，并在当前连续主分支约 \(|\varepsilon_c|/\varepsilon_{c0}\approx0.27\) 后无法继续保持同一近原点 \(\sigma_t=0\) 根支。

这再次说明：原点 tangent PASS 不等于全域二维 current-map PASS。

## 8. 当前参数身份

### 原始材料输入

\[
E_0,\ \nu,\ f_c,\ \varepsilon_{c0},\ f_t
\]

若 \(f_t\) 缺失：

\[
f_t=0.1f_c.
\]

### 内部派生（已闭合）

\[
\varepsilon_{cr}=f_t/E_0,
\qquad
m_c=E_0\varepsilon_{c0}/f_c,
\qquad
K_\nu=\nu E_0/(1-\nu^2),
\qquad
G_0=E_0/[2(1+\nu)].
\]

当前 \(\varepsilon_{t0}=0.0967635f_t/E_0\) 虽有公式，但因 T4 shape 本身 source-fidelity FAIL，不能视作最终 production closure。

### source-material closure 可立即锁定

\[
\boxed{k_\eta=0.1625}
\]

和（若继续采用 \(1/(1+k r^2)\) 这一 smooth family）

\[
\boxed{k_{tc}=0.0830721554223\ldots}
\]

采用 material-area closure。

### 仍未闭合 / 必须重开

1. T4 整个拉伸 shape，而不只是某一个参数；
2. finite-strain Poisson coupling form（additive Pi 被否决）。

## 9. 当前决策

- Compression primitive: LOCKABLE / source-identical Saenz.
- k_eta: LOCKABLE at 0.1625 from Foster CC equal-biaxial anchor.
- k_tc: material-only closure available at 0.0830721554223 if smooth quadratic-reduction family retained.
- T4: REOPEN.
- additive Pi direct2D: REJECT for finite-strain use; only its zero-strain tangent target remains valid.

下一步不应先跑 Case21，而应先以“不引入新自由参数、保持原点 plane-stress tangent、finite strain bounded/softening-compatible”为硬门禁重新构造二维 Poisson coupling；同时把 T4 改为与 Nguyen/Foster 的 linear-to-cracking + postcracking retained-tension 趋势一致的单式/有限解析式。
