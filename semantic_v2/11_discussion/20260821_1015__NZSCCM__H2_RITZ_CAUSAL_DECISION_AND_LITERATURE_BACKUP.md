# NZ-SCCM H2 Ritz 因果裁决与文献备份

- Date: 2026-08-21 10:15 +08:00
- Status: DECISION BACKUP / NO M7
- Scope: NC-M6 冻结后的结构层修正；面内边界兼容 Ritz admissible subspace + virtual-work/Galerkin projection

## 0. 不可修改边界

1. `NC-M6 = FROZEN`；不得建立 M7，不得用试验荷载反标材料或结构系数。
2. `ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE`。
3. 正式理论保持：
   - `N_formal_spatial_sampling = 0`
   - `N_formal_spatial_quadrature = 0`
   - `N_formal_spatial_subdomains = 1`
   - `N_formal_thickness_quadrature = 0`
   - `N_formal_material_points = 0`
4. 高阶 direct-current continuum quadrature 只允许用于 causal/convergence audit 和小数定位，不获得正式理论身份。
5. NC-M6 tangent 保持 source-consistent；不强迫 major symmetry；因此正式结构投影写成虚功/Galerkin，而不是假定全局标量势存在的传统最小势能 Ritz。

## 1. 本轮因果结论

此前 `(D,q,alpha)` 运动学把混凝土 `nu_c D` 直接写入结构参考态，且单一 `alpha` 同时承担均匀横向膜应变与非均匀膜应力重分布。两类结构的真实边界不同：

- Z0–Z5 钢箱/钢壳类横向自由边：正确参考条件应由多相截面共同满足横向自然边界，而不是混凝土单相 Poisson 参考；全局横向 resultant 条件为 `N_x=0`。
- Swartz24 RC 板：Nguyen 数值模型的侧边 `u_x` 受约束，底边 `v_y` 受约束；横向 `N_x` 是反力而不是必须消失的 residual。

此前用 `beta + zero-mean alpha` 只修正了 `q=0` 参考态，却没有重新从 admissible displacement field 建立完整后屈曲面内子空间。STEP5 结果证明：参考态错误是真实机械问题，但不是 Z 与 Swartz 预测误差的共同主因。修正参考态后，所测试 Z 与 Swartz 多数承载力反而下降，因此“wrong reference alone”作为预测误差主因已被否证。

新的结构层问题锁定为：

> **在 NC-M6 不动的前提下，建立严格满足各结构族 essential in-plane boundary conditions 的有限面内 admissible subspace，并让多相 current stress 通过虚功自行决定各个膜重分布坐标。**

## 2. 为什么停止单一 alpha

单一 `(1,1)` 完整半波

`w = b(q0+q) sin X sin Y`, `X=pi x/b`, `Y=pi y/ell`

经 von Karman 二阶几何项生成有限谐波族：

- `1`
- `cos 2X`
- `cos 2Y`
- `cos 2X cos 2Y`
- `sin 2X sin 2Y`

其中 uniform `1` 应由轴向缩短 `D` 与横向均匀膜坐标 `eta` 承担；其余正常应变谐波不能再被一个 `alpha` 预先绑成固定比例。对非线性、多轴、状态相关的 NC-M6，多相应力重分布应通过独立的 compatible in-plane coordinates 由虚功方程确定。

因此第一闭合子空间 H2 使用：

- `eta`
- `a20, a22`
- `b02, b22`

而旧 `alpha` 退出结构运动学。

## 3. 文献检索结论：不需要发明“新 Ritz 理论”

本轮 web 检索用于确认方法学成熟度，不作为 NZ-SCCM 本构来源。

### 3.1 Smith, Bradford & Oehlers (2003)

**Inelastic buckling of rectangular steel plates using a Rayleigh-Ritz method**  
International Journal of Structural Stability and Dynamics, 3(4), 503–521.  
DOI: `10.1142/S0219455403001026`  
Adelaide repository: `https://digital.library.adelaide.edu.au/items/339e6ab6-4bb6-46ca-90ab-36ba45d3c270`

公开摘要明确给出：Rayleigh–Ritz 可作为 **non-discretization method** 处理矩形钢板非弹性局部屈曲；位移函数可按边界构造；作者进行了 convergence/accuracy demonstration，并指出该方法在非弹性分岔板稳定问题上具有可计算性。

**对 NZ-SCCM 的作用**：证明“有限 admissible displacement coordinates + 非弹性 constitutive response + 非拓扑离散稳定分析”并不是新概念。NZ-SCCM 的区别是 current operator 为 NC-M6、多相结构、并要求 formal zero spatial quadrature。

### 3.2 Shin (1999)

**Postbuckling behavior of rectangular plates simply supported along loaded sides and clamped along unloaded sides**  
KSCE Journal of Civil Engineering, 3(1), 15–26.  
DOI: `10.1007/BF02830732`  
ScienceDirect PII: `S1226798824027673`

公开摘要明确给出：采用 von Karman strain nonlinearity；面内和面外位移均用 truncated Fourier series 表示 admissible functions；并比较不同 buckled modes 的势能。

**对 NZ-SCCM 的作用**：说明矩形板后屈曲中同时展开 in-plane / out-of-plane displacement 是成熟路径；不能只丰富 `w` 而把面内重分布压成单坐标。

### 3.3 Validation of Rayleigh–Ritz postbuckling (2003)

**Validation of the Rayleigh–Ritz method for the postbuckling analysis of rectangular plates with application to delamination growth**  
DOI: `10.1016/S0093-6413(03)00060-0`  
ScienceDirect PII: `S0093641303000600`

公开摘要指出：用 von Karman nonlinear strain-displacement relations 与高阶 displacement expansions 建立 nonlinear algebraic equations；若要准确恢复 membrane forces、moments 和 pointwise response，通常需要更多 undetermined coefficients；高阶解显示显著的 non-uniform in-plane forces/strains 和 boundary effects。

**对 NZ-SCCM 的作用**：直接支持本轮“结构输出是否已收敛必须通过 H2→H4 内部收敛审计，而不能凭一个低阶 alpha 的承载力吻合度认定”的治理原则。

### 3.4 Chen, Nie & Wu (2020)

**Application of Rayleigh-Ritz formulation to thermomechanical buckling of variable angle tow composite plates with general in-plane boundary constraint**  
International Journal of Mechanical Sciences 187 (2020) 106094.  
DOI: `10.1016/j.ijmecsci.2020.106094`  
ScienceDirect PII: `S0020740320332227`

公开摘要/全文预览明确给出：general in-plane boundary constraint 会改变 prebuckling non-uniform in-plane force resultant；作者用 generalized Rayleigh–Ritz + Lagrange multipliers 处理 pure stress、pure displacement 与 mixed in-plane constraints。

**对 NZ-SCCM 的作用**：确认“预屈曲膜应力与面内边界条件必须共同求解”是成熟结构力学认识。NZ-SCCM 不照搬其 Airy/Lagrange/Chebyshev 数值实现，因为本项目正式理论禁止空间 collocation/quadrature；这里只吸收边界与预屈曲场不能分离的物理原则。

### 3.5 Chen & Nie (2020)

**Prebuckling and buckling analysis of moderately thick variable angle tow composite plates considering the extension-shear coupling**  
Composite Structures 242 (2020) 112093.  
DOI: `10.1016/j.compstruct.2020.112093`

公开摘要同样强调：先在 general in-plane boundary conditions 下求 non-uniform prebuckling stress field，再进入 buckling problem。

## 4. 方法学裁决

1. 不需要依赖某篇新近论文“发明”子空间；Ritz/Fourier/Galerkin、von Karman 几何非线性和边界 admissibility 已非常成熟。
2. NZ-SCCM 需要自己的 H2/H4，是因为其材料 current operator、单半波治理、formal zero integration 与多相组装是项目特有的。
3. 由于 NC-M6 tangent 不要求对称，不使用“全局最小势能必然存在”作为前提；采用：

`Ritz admissible subspace -> current constitutive map -> virtual-work/Galerkin residual -> source-consistent Jacobian`。

4. 不能再通过一个 `alpha` 把多个面内 harmonics 固定比例绑定。
5. 是否需要 H4 不由试验误差决定，只由 H2→H4 内部收敛决定。

## 5. 下一步锁定

- 建立 H2 完整显式 strain/residual/Jacobian ledger。
- 建立 nested H4，不改变 NC-M6 和 `w`。
- 在任何试验荷载不参与的条件下执行 H2→H4 convergence audit。
- H2 通过预先冻结的 convergence gate：冻结 H2。
- 任一门禁失败：H2 不冻结，只升至 H4；不得跳到 M7、经验系数或几十自由度无控制扩张。
