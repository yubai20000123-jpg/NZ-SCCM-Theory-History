# PF1 执行边界锁 — 2026-08-10

**身份：CURRENT GOVERNANCE LOCK / USER-RECONFIRMED BOUNDARY**

用户在进入 `PF1 = Gauss-Manin / Picard-Fuchs closure` 前再次明确：无论后续数学表示如何变化，基础限制不得变化，研究路径不得偏离。

PF1 以及其后同一主线必须继承以下不可修改身份：

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
FORMAL_INTEGRATION = ANALYTIC_EXACT
ELEMENT_INTEGRATION = PROHIBITED
MATERIAL_POINT_GRID = PROHIBITED
SPATIAL_CELLS = PROHIBITED
GAUSS_SIMPSON_ADAPTIVE = PROHIBITED_IN_FORMAL_OPERATOR
```

结构目标保持：

```text
P(D,q)
Rq(D,q)=0
L(D,q)=P_,D Rq_,q - P_,q Rq_,D=0
```

材料主线保持：

```text
strong multiaxial material physics
-> source-shaped finite analytic compiler
-> invariant/tensor reduction
-> exact whole-halfwave contraction
-> analytic tangent
-> P / Rq / L
```

PF1 的唯一职责是把 R02 已识别的 `HYPERELLIPTIC_RELATIVE / PICARD_FUCHS` outer period 进一步闭合为有限解析对象。PF1 不得借数学困难重新定义结构问题、降低材料非线性、改变 Case21 运动学、引入空间离散，或把 numerical quadrature 改名为 special-function evaluation。

Fail-fast：

```text
PF1 cannot close under the locked identity
-> STOP + report exact blocker
-> do not silently switch to spatial quadrature/cells/material points
-> do not calibrate against Case21/Swartz Pu
```

允许的数学变化仅限于：等价坐标变换、有限代数基、resolvent decomposition、de-Rham/Gauss-Manin/Picard-Fuchs/GKZ 等有限解析表示，以及可解析消元的辅助变量。所有新增对象必须最终保持有限、可审计、可解析求导，并服务于同一 `P,Rq,L`。
