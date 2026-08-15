# NZ-SCCM — Nguyen/FvK 屈曲后膜力相容性审计

**Timestamp:** 2026-08-15 21:18 +08:00  
**Identity:** THEORY/COMPATIBILITY AUDIT ONLY — NO NEW Pu / NO NEW ROOT / NO CALIBRATION  
**Scope:** 只审计“Nguyen 二阶运动学是否已足以自动形成正确的屈曲后膜力重分布，以及当前 NZ-SCCM 低维面内投影覆盖了什么、遗漏了什么”。

---

## 0. 本轮禁止事项

本轮未执行：

- 新的 Z6 `Pu` 求解；
- `D=0.60` 之后的 continuation；
- 新的空间数值积分、Gauss/Simpson/cells；
- R10、N48-C1/MM、Cayley-Hamilton、D15、Nguyen 二阶公式的修改；
- 新材料参数、Zhou/Winter 拟合、试验荷载反标；
- 新的面外多模态生产计算。

本轮只做解析/来源/空间完备性审计。

---

## 1. 来源事实：Nguyen 二阶运动学已经包含初始缺陷后的几何非线性

Nguyen Ch.6 取中面总挠度

`w = w0 + wm`

其中 `w0` 是初始缺陷，`wm` 是加载后新增挠度。其 Eq.(6.3) 的中面膜应变部分包含

`eps_x = u_,x + 1/2 (wm_,x^2 + 2 w0_,x wm_,x)`

`eps_y = v_,y + 1/2 (wm_,y^2 + 2 w0_,y wm_,y)`

以及相应的面内剪切二阶项；厚度方向还叠加 `-z wm_,xx`, `-z wm_,yy`, `-z wm_,xy` 曲率项。

因此：

`NGUYEN_SECOND_ORDER_CONTAINS_IMPERFECT_POSTBUCKLING_GEOMETRY = YES`

把 `wm` 与 `w0` 合并来看，二阶增量项等价于“总挠度平方项减去初始无应力几何的平方项”。所以“NZ-SCCM 没有考虑二阶几何”不是当前缺口。

---

## 2. 来源事实：Nguyen 完整理论不是只有面外平衡

Nguyen Eqs.(6.8) 与 (6.9) 来源于面内虚位移与面外虚位移相互独立；完整问题本质上要求独立满足：

- 面内虚功/平衡；
- 面外虚功/平衡。

Nguyen 明确说明，对线弹性墙两者可在特定假设下解耦；对非弹性墙则面内与面外行为耦合，问题同时包含材料非线性与几何非线性。

Nguyen Eq.(6.36) 又把完整离散未知量写成结构位移向量 `q_m`，其中包含完整面内/面外位移自由度；该完整非线性系统在论文中因时间限制没有真正实现，后续采用了 small-imperfection / tangent-modulus uncoupled approximation。

因此：

`USING_NGUYEN_EQ6_3 != SOLVING_FULL_NGUYEN_CH6_EQUILIBRIUM_SPACE`

这一区分是本轮核心。

---

## 3. FvK/经典屈曲后理论的共同结构

经典 Föppl-von Kármán (FvK) 板后屈曲理论同时需要：

1. 面外挠度场 `w(x,y)`；
2. 面内膜力场 `N_x, N_y, N_xy`（常用 Airy 应力函数 `Phi` 表示）。

Airy 表示

`N_x = Phi_,yy`

`N_y = Phi_,xx`

`N_xy = -Phi_,xy`

可使面内平衡 `div N = 0` 先验满足；随后通过 FvK 相容方程把 `Phi` 与 `w` 的二阶曲率源耦合，再由面外平衡求后屈曲路径。

Walker (1969) 对四边简支方板的后屈曲分析使用 von Karman 方程 + 三角级数 + Galerkin，并专门区分“非加载边可面内自由畸变”与“非加载边保持直线但可整体移动”两种面内边界条件；初始几何缺陷也进入其后屈曲解。现代 Galerkin/FvK 工作仍明确指出：面外挠度可能已由低阶基很好描述，但面内应力为了准确可能需要更高阶基函数。

所以：

`SECOND_ORDER_W_TERMS = POSTBUCKLING_GEOMETRIC_SOURCE`

但

`POSTBUCKLING_GEOMETRIC_SOURCE != POSTBUCKLING_MEMBRANE_EQUILIBRIUM_SOLUTION`

除非面内平衡/相容空间也被充分满足。

---

## 4. 对 NZ-SCCM 单一完整半波做解析谐波审计

保持当前面外主线，不增加新面外模态：

`X = pi x / b`

`Y = pi y / a`

`w0 = A0 sin X sin Y`

`wm = A sin X sin Y`

定义二阶增量幅值因子

`S = A^2 + 2 A0 A`.

Nguyen Eq.(6.3) 的中面二阶膜应变部分可精确展开为：

### 4.1 横向正应变二阶项

`eps_x^NL = (S pi^2 / 8 b^2) [1 + cos(2X) - cos(2Y) - cos(2X)cos(2Y)]`

### 4.2 加载向正应变二阶项

`eps_y^NL = (S pi^2 / 8 a^2) [1 - cos(2X) + cos(2Y) - cos(2X)cos(2Y)]`

### 4.3 工程剪切二阶项

`gamma_xy^NL = (S pi^2 / 4ab) sin(2X) sin(2Y)`

（若采用 tensor shear `eps_xy`，则为上述工程剪切的一半；Nguyen Eq.(6.3) 的张量/工程剪切约定必须保持一致。）

**第一关键结果：** 即使面外挠度只有 `(1,1)` 一个主谐波，二阶几何自动在膜应变中生成：

- uniform `(0,0)`；
- `(2,0)`；
- `(0,2)`；
- `(2,2)`；
- shear `(2,2)`。

所以“ONE_CONTINUOUS_COMPLETE_HALFWAVE”并不意味着“面内场也只需要一个空间形状”。

---

## 5. 相容算子会把这些应变谐波进一步收缩成两个基本 FvK 源方向

对同一 `(1,1)` 面外形，几何相容源

`wm_,xx wm_,yy - wm_,xy^2`

以及初始缺陷交叉项的增量组合，可写成与 `S` 成正比的：

`-(S alpha^2 beta^2 / 2) [cos(2X) + cos(2Y)]`

其中

`alpha = pi/b`, `beta = pi/a`.

因此在经典 Airy/FvK 表示中，最基本的 particular membrane-stress response 至少需要独立承载：

- `(2,0)` 方向；
- `(0,2)` 方向；

外加由平均轴力、边界位移/边界膜力所决定的 homogeneous membrane field。

注意：这里不是要求增加 `q31/q13` 面外模态。它是**同一个 `(1,1)` 面外半波自身产生的二阶面内再分布需求**。

---

## 6. displacement form 与 Airy form 的差别

两种路线都可与 NZ-SCCM 的零结构空间积分合同兼容，但它们满足约束的方式不同。

### 6.1 位移形式

令

`u = u_bar(D) + sum c_i U_i(X,Y)`

`v = v_bar(D) + sum d_j V_j(X,Y)`

由位移生成应变，几何相容先验满足；但必须对所有独立 admissible 面内虚位移方向满足

`R_{c_i}=0`, `R_{d_j}=0`.

若只保留很少的 `c_i,d_j`，则只是完整面内平衡 PDE 的 Ritz/Galerkin 投影。

### 6.2 Airy 应力函数形式

令

`Phi = Phi_h + Phi_p`

并用 `N_x=Phi_,yy`, `N_y=Phi_,xx`, `N_xy=-Phi_,xy`，则面内力平衡先验满足；随后用材料/应变相容确定 Airy 系数。

对于当前一般非线性 `sigma=M(epsilon)`，不能直接把线弹性 Airy 闭式式子当作 production 本构解；但 Airy/FvK 谐波结构可以作为**面内平衡空间完备性审计基准**。

---

## 7. 当前 NZ-SCCM 低维面内空间覆盖情况

### 7.1 旧 D-q 场

旧基场在 `q=0` 采用

`eps_x = +nu D`

`eps_y = -D`

对应全域 free-Poisson 预屈曲状态。此前来源边界审计已确认，这与 Zhou loaded edges 的 `u_x=0` 条件不相容。

同时，旧 `D,q` 模型只有平均加载变量 D，没有独立非均匀面内 redistribution coordinate；因此 Nguyen Eq.(6.3) 虽生成 `(2,0)/(0,2)/(2,2)` 二阶应变内容，却没有对应的一组独立面内虚功条件去验证完整膜力平衡。

结论：

`OLD_DQ_POSTBUCKLING_MEMBRANE_EQUILIBRIUM_COMPLETENESS = FAIL/NOT REPRESENTED`

### 7.2 当前 boundary-warp D-q-c 场

新增 `c` 场的首要目的，是满足 Zhou loaded-edge 的面内 essential boundary condition，并在 `R_c=0` 下做静力凝聚。此前已证明：

- kinematic admissibility = PASS；
- `R_q=0 + R_c=0` full-current checkpoint = 可计算；
- Z6 平衡路径因此发生真实改变。

但本轮审计发现：**一个 `c` 只能增加一个额外面内虚功条件**。它并没有被证明与经典 FvK 的完整 `(2,0)+(0,2)+homogeneous boundary field` 膜力解空间等价。

特别是当前 `c` 形状是为 loaded-edge `u=0` 构造的奇次 Fourier boundary warp；它不是从 FvK compatibility source 对 `(2,0)/(0,2)` 的 particular Airy 解推导出来的。

因此：

`BOUNDARY_ADMISSIBILITY_CORRECTION = REAL AND NECESSARY`

但

`ONE_C_COORDINATE_PROVES_FULL_POSTBUCKLING_MEMBRANE_EQUILIBRIUM = NO`

这不是说 `c` 错，而是说其**完备性尚未证明**。

---

## 8. 当前最重要的理论区分

现在应严格区分三个层次：

### Layer A — Nguyen second-order kinematics

`PASS / already present`

它正确生成 `w0-wm` 交叉项及 `wm^2` 二阶膜应变源。

### Layer B — in-plane boundary admissibility

`old D-q = FAIL`

`D-q-c = partial correction / demonstrated`

这解决 loaded-edge `u=0` 的明确边界不相容。

### Layer C — postbuckling membrane-equilibrium space completeness

`NOT YET CERTIFIED`

当前没有证据证明 `D+c` 已完整覆盖由单 `(1,1)` 面外半波二阶几何强制产生的全部独立膜力再分布方向。

所以本轮不能把 Z6 偏低简单归因于“Nguyen 二阶公式不足”，也不能把原因只压缩成“边界 c 修正”。更准确的状态是：

`POSTBUCKLING_KINEMATICS = PRESENT`

`POSTBUCKLING_MEMBRANE_EQUILIBRIUM_COMPLETENESS = OPEN`

---

## 9. 为什么这个缺口与“屈曲后强度”直接相关

经典板的屈曲后承载储备来自：

`w` 增长

`->` 二阶膜应变源增长

`->` `u,v` / membrane-stress field 重新分布

`->` 中部/局部区域卸载与边缘/其他区域继续传力

`->` 达到 `Pcr` 后仍存在稳定的后屈曲平衡支。

因此，只把 `1/2 w_,i^2` 放入应变并不自动保证正确 postbuckling reserve；必须同时允许并满足相应的膜力平衡/相容重分布。

这正是用户提出的核心疑问的回答：

`WHY_SECOND_ORDER_PRESENT_BUT_POSTBUCKLING_RESERVE_MAY_BE_WRONG`

`= SECOND_ORDER_GEOMETRIC_SOURCE_PRESENT + IN_PLANE_EQUILIBRIUM_PROJECTION_POSSIBLY_INCOMPLETE`.

---

## 10. 对此前 q31 诊断的关系

此前 q31 first-variation 曾发现非零广义功，但后续 governance 已正确撤回“q31 因此解释 Z6 偏低”的因果推断。

本轮进一步说明：在打开新的面外模态之前，应先审计**单 `(1,1)` 面外模态自身要求的面内膜力再分布空间**。否则增加 q31/q13 可能只是把一个未闭合的面内问题扩大到更多面外自由度。

因此：

`OUT_OF_PLANE_MULTIMODE_AS_NEXT_CAUSAL_STEP = NOT AUTHORIZED`

---

## 11. 后续唯一合理的验证门禁（本轮未执行）

下一步如获用户授权，应先做**residual-projection completeness gate**，仍不求 Pu：

1. 保持 `w=w0+q sinX sinY` 不变；
2. 构造与 FvK `(2,0)`、`(0,2)` 源及 Zhou in-plane edge conditions 相容的最小解析 `u,v` test/basis family；
3. 用 frozen current operator 在现有已接受状态上只计算对应的独立面内广义残量；
4. 检查当前 `D+c` 平衡点是否同时对这些额外方向 stationary/equilibrated；
5. 若额外残量均可忽略，则 `D+c` 面内空间通过；若显著非零，则确认 postbuckling membrane-space deficiency，再决定增加最少多少个解析面内系数。

这个 gate 仍可保持：

`ONE_CONTINUOUS_COMPLETE_HALFWAVE`

`N_formal_spatial_sampling = 0`

`N_formal_spatial_quadrature = 0`

`N_formal_spatial_subdomains = 1`.

---

## 12. 本轮结论

```text
NGUYEN_EQ6_3_SECOND_ORDER_GEOMETRY = SUFFICIENT AS GEOMETRIC SOURCE
NGUYEN_EQ6_3_ALONE = NOT SUFFICIENT TO GUARANTEE FULL POSTBUCKLING EQUILIBRIUM
CLASSICAL_FVK_POSTBUCKLING_REQUIRES_MEMBRANE_REEQUILIBRATION = CONFIRMED
ONE_OUT_OF_PLANE_HALFWAVE_CAN_GENERATE_MULTIPLE_IN_PLANE_HARMONICS = CONFIRMED
OLD_DQ_FREE_POISSON_IN_PLANE_FIELD = INCOMPATIBLE WITH ZHOU LOADED-EDGE BC
BOUNDARY_WARP_C = NECESSARY CORRECTION BUT FULL MEMBRANE COMPLETENESS NOT PROVEN
R10_AS_PRIMARY_CAUSE = NOT ESTABLISHED
D15_AS_PRIMARY_CAUSE = NOT SUPPORTED
WRONG_LINEAR_M_AS_PRIMARY_CAUSE = NOT SUPPORTED
OUT_OF_PLANE_Q31_AS_PRIMARY_CAUSE = NOT ESTABLISHED
NEW_Pu_THIS_ROUND = NONE
```

**Current causal frontier:**

`CURRENT_NEXT_THEORY_GATE = SINGLE_HALFWAVE_FVK_MEMBRANE_RESIDUAL_PROJECTION_COMPLETENESS`

本轮只建立审计边界和解析谐波台账，不执行该 gate 的数值残量评价。

---

## 13. 主要来源

1. Nguyen Dai Minh (1996), *Buckling of reinforced concrete walls by the finite element method*: Ch.2 nonlinear thin-plate theory; Ch.6 Eqs.(6.1)-(6.9), (6.27)-(6.36), approximate tangent-modulus limitation.
2. A. C. Walker (1969), *The Post-Buckling Behaviour of Simply-Supported Square Plates*, Aeronautical Quarterly 20(3), 203-222: von Karman equations, trigonometric series, Galerkin, explicit comparison of alternative in-plane edge constraints and initial imperfections.
3. M. Stein (1959), NASA TR R-40, *Loads and Deformations of Buckled Rectangular Plates*: nonlinear von Karman large-deflection equations and postbuckling response of simply supported rectangular plates under longitudinal compression.
4. Recent Galerkin/FvK work (International Journal of Non-Linear Mechanics, 2025, 105210): higher-order basis functions can be required for accurate in-plane stresses even when transverse deflection is captured by low-order bases. Used only as modern corroboration, not as a governing source.
