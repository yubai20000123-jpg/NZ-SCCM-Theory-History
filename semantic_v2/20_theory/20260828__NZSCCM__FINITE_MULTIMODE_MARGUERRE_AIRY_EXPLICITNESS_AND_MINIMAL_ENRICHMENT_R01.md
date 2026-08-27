# NZ-SCCM — 有限多模态 Marguerre–Airy 显式性与最小富集理论审计 R01

**日期：2026-08-28**  
**身份：THEORY AUDIT / NOT PRODUCTION**  
**基线：`20260821_1733__NZSCCM__MARGUERRE_AIRY_EXPLICIT_LIMIT_THEORY_V1.md`**  
**约束：本推导不使用 FEM/试验选择模态，不修改 production `P(q)`、Pu、qU 策略、terminal capacity 架构或材料参数。**

```text
FINITE_N_MARGUERRE_AIRY_EXPLICITNESS = PASS
FINITE_N_FORMAL_SPATIAL_QUADRATURE = 0
FINITE_N_IS_EXACT_FOR_CHOSEN_MODAL_ANSATZ = YES
FINITE_N_IS_EXACT_CLOSURE_OF_FULL_PDE = NO
SINGLE_MODE_EXACT_INVARIANT_SUBSPACE = NO
N2_UNIQUE_SECOND_MODE_FROM_NONLINEAR_SELECTION = NO
MINIMUM_FIRST_GENERATION_COMPLETE_ENRICHMENT = N3
FEM_USED_FOR_DERIVATION = NO
FEM_USED_FOR_MODE_SELECTION = NO
AIRY_FRAMEWORK_CHANGE = NO
CURRENT_PRODUCTION_THEORY_CHANGE = HOLD
```

---

## 1. 问题

当前 production 低阶理论采用单一物理面外模态

\[
w_d=bq\phi,
\qquad
w_i=bq_0\phi,
\]

并由 Marguerre compatibility + Airy stress function + Galerkin 面外平衡得到标量三次关系 `P(q)`。

本审计只回答两个理论问题：

1. 若改成有限多模态
   \[
   w_d=b\sum_{r=1}^{N}q_r\phi_r,
   \]
   是否仍能保持无空间数值积分、有限显式代数闭合？
2. 从当前主模态自身的非线性选择规则出发，最小 `N=2` 是否能唯一决定第二模态；若不能，最小 first-generation complete 富集是什么？

---

## 2. 一般有限 N 的位移展开

取有限 Navier 模态集合

\[
\boxed{\phi_r(x,y)=\sin(\alpha_r x)\sin(\beta_r y)},
\qquad r=1,\ldots,N,
\]

其中完整物理板上可写

\[
\alpha_r=\frac{m_r\pi}{b},\qquad
\beta_r=\frac{n_r\pi}{a_{phys}}.
\]

加载新增挠度和无应力初始缺陷统一写成

\[
\boxed{w_d=b\sum_{r=1}^{N}q_r\phi_r},
\qquad
\boxed{w_i=b\sum_{r=1}^{N}q_{0r}\phi_r}.
\]

定义当前总模态系数

\[
t_r=q_r+q_{0r}.
\]

这里 `q_r` 与当前标量 `q` 具有同一物理身份：均为以 `b` 无量纲化的加载新增面外模态幅值；仅自由度数由 1 扩展为有限 N。

---

## 3. Marguerre bracket 与有限谐波闭合

定义对称 Marguerre bracket

\[
\boxed{
[u,v]
=u_{,xx}v_{,yy}+u_{,yy}v_{,xx}-2u_{,xy}v_{,xy}.
}
\]

与当前单模态符号约定一致，兼容方程右端可写为

\[
\boxed{
\mathcal G
=-\frac12[w_d,w_d]-[w_d,w_i].
}
\]

代入有限展开，因为 bracket 双线性且对称：

\[
\boxed{
\mathcal G
=-\frac{b^2}{2}
\sum_{i=1}^{N}\sum_{j=1}^{N}
H_{ij}[\phi_i,\phi_j],
}
\]

其中

\[
\boxed{
H_{ij}=q_iq_j+q_iq_{0j}+q_{0i}q_j.
}
\]

特别地

\[
H_{ii}=q_i(q_i+2q_{0i}),
\]

严格退化回当前单模态的 `q(q+2q0)`。

### 3.1 任意两模态 bracket 的精确谐波式

定义

\[
d^-_{ij}=\alpha_i\beta_j-\alpha_j\beta_i,
\qquad
d^+_{ij}=\alpha_i\beta_j+\alpha_j\beta_i.
\]

则积化和差后得到

\[
\boxed{
[\phi_i,\phi_j]
=\frac14(d^-_{ij})^2
\left[
\cos((\alpha_i-\alpha_j)x)\cos((\beta_i-\beta_j)y)
+\cos((\alpha_i+\alpha_j)x)\cos((\beta_i+\beta_j)y)
\right]
}
\]

\[
\boxed{
\quad
-\frac14(d^+_{ij})^2
\left[
\cos((\alpha_i-\alpha_j)x)\cos((\beta_i+\beta_j)y)
+\cos((\alpha_i+\alpha_j)x)\cos((\beta_i-\beta_j)y)
\right].
}
\]

当 `i=j` 时，`d^-_{ii}=0`，上式立即变为

\[
\boxed{
[\phi_i,\phi_i]
=-\alpha_i^2\beta_i^2
[\cos(2\alpha_i x)+\cos(2\beta_i y)].
}
\]

这与当前单模态 compatibility forcing 完全一致。

因此：每一对 `(i,j)` 最多生成四个 cosine–cosine 谐波；有限 N 只生成有限个谐波，数量按 `O(N^2)` 增长，不产生空间离散需求。

---

## 4. Airy 方程对有限 N 仍逐谐波显式

当前正交板 Airy compatibility operator 为

\[
\mathcal L_A
=\bar A_{22}\partial_x^4
+(2\bar A_{12}+\bar A_{66})\partial_x^2\partial_y^2
+\bar A_{11}\partial_y^4.
\]

对于任一谐波

\[
\chi_{k_x,k_y}=\cos(k_xx)\cos(k_yy),
\]

都有

\[
\boxed{
\mathcal L_A\chi_{k_x,k_y}
=\Lambda(k_x,k_y)\chi_{k_x,k_y},
}
\]

其中

\[
\boxed{
\Lambda(k_x,k_y)
=\bar A_{22}k_x^4
+(2\bar A_{12}+\bar A_{66})k_x^2k_y^2
+\bar A_{11}k_y^4.
}
\]

于是 compatibility RHS 中每一个非零谐波系数 `G_{kx,ky}` 都直接给出

\[
\boxed{
\Theta_{k_x,k_y}=\frac{G_{k_x,k_y}}{\Lambda(k_x,k_y)}.
}
\]

故

\[
\boxed{
\theta_p
=\sum_{(k_x,k_y)\in\mathcal H_N}
\Theta_{k_x,k_y}(\mathbf q,\mathbf q_0)
\cos(k_xx)\cos(k_yy),
}
\]

其中 `\mathcal H_N` 是有限谐波集合；每个 `Theta` 至多二次依赖 `q_r,q0_r`。

结论：

\[
\boxed{
\text{有限 N 的 Airy compatibility 仍是有限、逐项、显式的。}
}
\]

不需要 Gauss、Simpson、adaptive quadrature、material points 或 spatial cells。

---

## 5. 面外平衡仍为有限三次代数系统

保留当前结构方程角色：

\[
\boxed{
\mathcal L_Dw_d-[\theta_h+\theta_p,w_d+w_i]=0,
}
\]

其中

\[
\mathcal L_D
=D_x\partial_x^4+2H\partial_x^2\partial_y^2+D_y\partial_y^4,
\]

\[
\theta_h=-\frac12Nx^2,
\qquad N=P/b.
\]

每一个 Navier mode 是 bending operator 的本征函数：

\[
\boxed{
K_r
=D_x\alpha_r^4+2H\alpha_r^2\beta_r^2+D_y\beta_r^4.
}
\]

将面外平衡精确投影到每个 `phi_r` 后：

\[
\boxed{
R_r(P,\mathbf q)
=bK_rq_r-Nb\beta_r^2(q_r+q_{0r})
+\mathcal C_r(\mathbf q,\mathbf q_0)=0,
\quad r=1,\ldots,N.
}
\]

因为：

- `theta_p` 的模态系数为 `q/q0` 的二次多项式；
- `w_d+w_i` 对 `q/q0` 为一次；
- bracket 线性作用于二者；

故

\[
\boxed{\deg_{\mathbf q}\mathcal C_r\le3.}
\]

因此任意固定有限 N 都得到有限个显式三次代数方程：

\[
\boxed{
R_1=\cdots=R_N=0.
}
\]

这里“显式”指：所有系数可由原始 A/D 刚度、板尺寸、整数模态指标直接写出；正式求解只需一次性有限代数求根。它并不要求每个根都能用初等根式单行表示。

### 5.1 零空间积分仍可严格保持

对于整数 Navier indices，所有投影积分均可由正交性/和差频选择规则写成 Kronecker delta。例如归一化的一维选择式

\[
\frac{2}{\pi}\int_0^\pi
\sin(rt)\sin(kt)\cos(pt)\,dt
=\frac12[\gamma_p\delta_{p,|r-k|}-\delta_{p,r+k}],
\]

其中 `gamma_0=2`，`gamma_{p>0}=1`。

故 cubic coupling tensor 也可预编译成有限整数选择规则，而不需要数值积分。

---

## 6. 重要限定：有限 N 显式 ≠ 全 PDE 的有限精确不变子空间

上面的 PASS 只说明：

> 对一个已经固定的有限 modal ansatz，Marguerre–Airy 方程可以精确投影成有限显式代数系统。

并不说明某个有限 modal set 在完整非线性 PDE 下自动闭合。

非线性和频/差频一般会生成更高谐波，因此有限 N 通常是一个有限 Galerkin 截断，而不是完整 PDE 的严格有限维不变子空间。

这一区分必须保留。

---

## 7. 从当前主模态自身出发：第一代非线性面外谐波是什么？

现在完全不看 FEM，只从 current primary mode 自身推导。

在代表完整半波坐标中定义

\[
\alpha=\pi/b,
\qquad
\beta=\pi/\ell,
\]

主模态为

\[
\boxed{
\phi_{1,1}=\sin\alpha x\sin\beta y.
}
\]

在完整物理板上它对应 `(1,m*)`。

主模态的自 bracket 只生成两个 Airy 二倍频：

\[
\cos2\alpha x,
\qquad
\cos2\beta y.
\]

但在面外平衡中，这两个 Airy 谐波还要与当前总形状 `sin(alpha x)sin(beta y)` 再发生 bracket。利用

\[
\sin\alpha x\cos2\alpha x
=\frac12[\sin3\alpha x-\sin\alpha x],
\]

\[
\sin\beta y\cos2\beta y
=\frac12[\sin3\beta y-\sin\beta y],
\]

可知主模态自非线性除了反馈到自身 `(1,1)` 外，还同时生成

\[
\boxed{(3,1)}
\qquad\text{和}\qquad
\boxed{(1,3)}.
\]

换回完整物理板索引：

\[
\boxed{(3,m_*)}
\qquad\text{和}\qquad
\boxed{(1,3m_*)}.
\]

这是理论上的精确选择规则，与 FEM 无关。

---

## 8. 直接证明：单模态子空间不是严格不变子空间

设初始缺陷只含主模态：

\[
q_{01}=q_0,
\qquad
q_{0,3m_*}=q_{03,m_*}=0.
\]

定义

\[
\boxed{
S(q)=q(q+q_0)(q+2q_0).
}
\]

若强行令两个第一代 secondary amplitudes 均为零，则它们的 residual 中仍分别存在非零强迫项。

对横向三次谐波 `(3,m*)`：

\[
\boxed{
F_x
=-\frac{b^3\beta^4}{16\bar A_{22}}S(q).
}
\]

对轴向三次谐波 `(1,3m*)`：

\[
\boxed{
F_y
=-\frac{b^3\alpha^4}{16\bar A_{11}}S(q).
}
\]

因此一般地只要 `q>0`：

\[
\boxed{F_x\ne0,\qquad F_y\ne0.}
\]

所以

\[
\boxed{
\text{current single-mode subspace is not an exact invariant subspace of the enlarged Marguerre–Airy system.}
}
\]

这不表示当前单模态公式代数错误；它表示单模态是一个截断近似，而不是完整非线性方程中的严格封闭模态族。

---

## 9. 为什么 N=2 不能由非线性选择规则唯一决定？

因为主模态自身在同一阶上同时产生两个 secondary modes：

\[
(3,m_*),\qquad(1,3m_*).
\]

仅根据“第一代由主模态非线性激活”的规则，二者地位相同，不能凭空只留一个。

因此：

\[
\boxed{
N=2\ \text{cannot be uniquely justified by nonlinear selection alone}.
}
\]

最小 first-generation symmetry-complete 富集应为

\[
\boxed{
N=3:\quad
(1,m_*),\ (3,m_*),\ (1,3m_*).
}
\]

注意：N=3 只是“第一代完整”，并非全 PDE 永久闭合；一旦两个 secondary amplitudes 非零，它们之间的交互还能生成更高谐波。

---

## 10. 如果坚持 N=2，唯一允许的理论选择方式：forcing / detuning 排序

可以不靠 FEM，而从 secondary equation 在主模态路径附近的线性响应比较两者的重要性。

在固定膜力 `N=P/b` 下，leading-order secondary amplitudes 为

\[
\boxed{
q_{3,m_*}^{(1)}
=\frac{b^2\beta^4}
{16\bar A_{22}[K_{3,m_*}-N\beta^2]}
S(q),
}
\]

\[
\boxed{
q_{1,3m_*}^{(1)}
=\frac{b^2\alpha^4}
{16\bar A_{11}[K_{1,3m_*}-9N\beta^2]}
S(q).
}
\]

在主模态弹性临界膜力

\[
N_{cr}=K_1/\beta^2
\]

处，可定义纯理论 ranking indices

\[
\boxed{
\Gamma_x
=\frac{\beta^4/\bar A_{22}}
{K_{3,m_*}-N_{cr}\beta^2},
}
\]

\[
\boxed{
\Gamma_y
=\frac{\alpha^4/\bar A_{11}}
{K_{1,3m_*}-9N_{cr}\beta^2}.
}
\]

若一个 `Gamma` 远大于另一个，才有理论依据将 N=3 进一步做 controlled N=2 asymptotic reduction。若二者同量级，则理论本身要求保留两者。

相应 detuning 可完全显式写成：

\[
\boxed{
K_{3,m_*}-K_1
=80D_x\alpha^4+16H\alpha^2\beta^2,
}
\]

\[
\boxed{
K_{1,3m_*}-9K_1
=8(9D_y\beta^4-D_x\alpha^4).
}
\]

后一项在当前 elastic front-end 真正由 `m*` 控制、且与 `3m*` 比较不退化时应为非负；若接近零，则表示与 `(1,3m*)` 近退化/近共振，更不能删除该模态。

---

## 11. 一个完整可写出的 N=2 示例：主模态 + 轴向三次谐波

本节仅证明 N=2 确实可以完全显式；不宣布它优于 N=3。

在代表半波上取

\[
\phi_1=\sin\alpha x\sin\beta y,
\qquad
\phi_2=\sin\alpha x\sin3\beta y,
\]

并取

\[
q_{02}=0,
\qquad
t_1=q_1+q_0,
\qquad
t_2=q_2.
\]

定义

\[
H_{11}=q_1(q_1+2q_0),
\qquad
H_{12}=q_2(q_1+q_0),
\qquad
H_{22}=q_2^2.
\]

用

\[
C_{pq}=\cos(p\alpha x)\cos(q\beta y)
\]

简记，有三个精确 bracket：

\[
\boxed{B_{11}=-\alpha^2\beta^2(C_{02}+C_{20})},
\]

\[
\boxed{B_{12}=\alpha^2\beta^2(C_{02}+C_{24}-4C_{04}-4C_{22})},
\]

\[
\boxed{B_{22}=-9\alpha^2\beta^2(C_{06}+C_{20})}.
\]

令

\[
\Lambda_{pq}=\Lambda(p\alpha,q\beta).
\]

Airy particular solution 中非零谐波系数逐项为

\[
\boxed{
T_{02}=\frac{b^2\alpha^2\beta^2}{\Lambda_{02}}
\left(\frac12H_{11}-H_{12}\right),
}
\]

\[
\boxed{
T_{20}=\frac{b^2\alpha^2\beta^2}{\Lambda_{20}}
\left(\frac12H_{11}+\frac92H_{22}\right),
}
\]

\[
\boxed{T_{24}=-\frac{b^2\alpha^2\beta^2}{\Lambda_{24}}H_{12}},
\]

\[
\boxed{T_{04}=\frac{4b^2\alpha^2\beta^2}{\Lambda_{04}}H_{12}},
\]

\[
\boxed{T_{22}=\frac{4b^2\alpha^2\beta^2}{\Lambda_{22}}H_{12}},
\]

\[
\boxed{T_{06}=\frac{9b^2\alpha^2\beta^2}{2\Lambda_{06}}H_{22}}.
\]

定义两个 bending eigenvalues

\[
K_1=D_x\alpha^4+2H\alpha^2\beta^2+D_y\beta^4,
\]

\[
K_2=D_x\alpha^4+18H\alpha^2\beta^2+81D_y\beta^4.
\]

则两个 exact finite-Galerkin residual 为

\[
\boxed{
R_1=
 bK_1q_1-Nb\beta^2t_1
+2b\alpha^2\beta^2t_1(T_{02}+T_{20})
-b\alpha^2\beta^2t_2(2T_{02}-8T_{04}-4T_{22}+T_{24})
=0,
}
\]

\[
\boxed{
R_2=
 bK_2q_2-9Nb\beta^2t_2
-b\alpha^2\beta^2t_1(2T_{02}-8T_{04}-4T_{22}+T_{24})
+18b\alpha^2\beta^2t_2(T_{06}+T_{20})
=0.
}
\]

所有 `T_pq` 都是 `q1,q2,q0` 的二次显式多项式除以常数 `Lambda_pq`，所以 `R1,R2` 是显式三次代数方程。

进一步令 `q2=0`，第二方程并不会自动消失，而是

\[
\boxed{
R_2\big|_{q_2=0}
=-\frac{b^3\alpha^4}{16\bar A_{11}}
q_1(q_1+q_0)(q_1+2q_0)\ne0.
}
\]

这给出单模态不严格闭合的一个直接代数证明。

---

## 12. 为什么当前单模态 `P(q)` 仍可能在近屈曲区是合理的？

上述结果不能被误读为“单模态理论无效”。

对于 perfect plate `q0=0`：

\[
F_x,F_y=O(q^3).
\]

因此 secondary amplitudes 首先是

\[
q_{secondary}=O(q^3),
\]

而 secondary 对 primary equation 的再反馈通常到更高阶才出现，典型为

\[
O(q^5).
\]

于是当前单模态 cubic `P(q)` 在 perfect plate 的近屈曲小幅值展开中仍有明确的渐近依据：

\[
\boxed{
\text{single-mode cubic is asymptotically consistent through cubic order near buckling for }q_0=0.
}
\]

对于 `q0>0`，严格幂次计数发生变化，但 secondary forcing 始终由

\[
S=q(q+q_0)(q+2q_0)
\]

控制。因此小初始缺陷、近起始区仍可理解为受控修正，而不能宣称 exact invariant closure。

---

## 13. 本轮理论裁决

### 13.1 已证明

1. **有限 N 完全可以显式化。** 不能再以“为了显式所以只能一个 q”作为单模态的理由。
2. 对固定 finite modal ansatz，compatibility、Airy solution、Galerkin residual 全部是有限解析/代数对象，formal spatial quadrature 仍为零。
3. current single mode 不是完整 Marguerre–Airy 非线性系统中的严格不变子空间。
4. 主模态第一代非线性同时生成 `(3,m*)` 与 `(1,3m*)`，故 nonlinear selection 本身不能唯一给出一个 N=2 secondary mode。
5. 最小 first-generation complete enrichment 是 N=3：`(1,m*)`, `(3,m*)`, `(1,3m*)`。
6. 若坚持 N=2，只能先用纯理论 forcing/detuning 指标 `Gamma_x,Gamma_y` 证明其中一个 secondary 渐近占优；不得用 FEM/试验选模态。
7. 单模态 cubic 在 perfect plate 近屈曲区仍有三次阶渐近合理性，因此本轮不撤销 production 单模态理论。

### 13.2 尚未证明

1. N=3 是否已经足以描述终端前全部结构响应；不能从 first-generation completeness 推成 full-PDE completeness。
2. terminal capacity 坐标应如何与 N=3 的多个 global modal coordinates 接口；本轮不修改 terminal 架构。
3. 对 BH032/BH050 等具体板，`Gamma_x/Gamma_y` 的数值排序尚未在本文件中执行。
4. 多模态富集是否改善任何 FEM/试验预测不是本轮理论门禁，也不得作为理论成立依据。

---

## 14. 当前治理状态

```text
MAIN_PRODUCTION_BRANCH = UNCHANGED
CURRENT_SINGLE_MODE_PRODUCTION = RETAIN_FOR_NOW
MULTIMODE_THEORY_STATUS = THEORY_AUDIT_PASS_EXPLICITNESS
MULTIMODE_PRODUCTION_STATUS = HOLD
NEXT_THEORY_ONLY_TASK = EVALUATE_GAMMA_X_GAMMA_Y_FROM_FROZEN_A_D_STIFFNESSES_AND_DERIVE_N3_EXPLICIT_RESIDUAL_FAMILY
NO_FEM_CALIBRATION = YES
NO_TEST_CALIBRATION = YES
NO_AIRY_ROLE_CHANGE = YES
NO_TERMINAL_CAPACITY_ROLE_CHANGE = YES
```
