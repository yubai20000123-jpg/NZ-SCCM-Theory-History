# NZ-SCCM 根因诊断暂停 — 2026-08-10

**Status:** CURRENT PAUSE / NO NEW COMPILER ROUTE AUTHORIZED

## 1. 本轮裁决

暂停 P2R 及任何新的 compiler/basis 试探。当前不允许继续“换函数族—拟合—再救积分”的试错链。

## 2. 当前证据指向的主根因

困难不是一般意义上的“矩阵理论太复杂”，也不是 Nguyen 二阶运动学本身。Case21 的 I1/I2 已经是有限多项式场，且 polynomial material 下 D15/Beta exact moments 可直接闭合。

真正困难集中在四个要求同时成立：

1. 强多轴混凝土非线性，尤其拉伸/开裂附近的窄尺度激活；
2. 不允许按 TT/TC/CC 等材料状态或空间区域分区；
3. 要求一个统一连续 current material map；
4. 同时要求 whole-halfwave 零空间积分、零辅助积分、零 ODE 步进，并最终得到低复杂度直接公式。

这形成“复杂度搬运”问题：

- 若保留材料状态分支，复杂度在 state/domain partition；
- 禁止分支后，用 Pi_eta/H 等光滑激活把复杂度搬进全局材料函数；
- rational compiler 又把复杂度搬进 poles/resolvents/algebraic periods；
- Picard-Fuchs 再把复杂度搬进 15x15 auxiliary state system；
- global polynomial 则把同一复杂度表现为高阶振荡和巨大系数。

因此不是复杂度消失，而是在不同表示之间迁移。

## 3. 当前最直接的材料证据

P2-A degree<=16 global polynomial screen：

- U max normalized error ≈ 2.43%
- C ≈ 2.44%
- C2 ≈ 0.51%
- T ≈ 32.58%
- V=T^8 ≈ 43.28%

所以“一般材料非线性”不是准确描述；主要困难明显集中在 tensile activation / cracking-like narrow transition 及其高次放大 V=T^8。

当前 lambda 全域约从 -2.439 到 0.732，跨度约 3.17；而 T 在 lambda≈0~0.05 内由 0 快速升至接近 1，存在约 60 倍量级的多尺度分离。single global low-degree polynomial 因此天然困难。

## 4. 一个更重要的疑点

当前 frozen NC / source-shaped U,C,C2,T,V 只是 regression/material oracle，不是 final NC source truth。特别是 V=T^8 与相关 interaction 必须重新审计其身份：

- 是 Nguyen/Foster 原始材料关系必需的物理结构；
- 还是我们为了把旧二维 frozen operator 写成统一 source-shaped map 而引入的 compiler/surrogate 结构。

如果属于后者，则当前大量解析困难可能是在忠实保留一个中间 surrogate，而不是在忠实保留最终物理材料本构。

## 5. 结构侧不是主根因，但会放大材料难度

Case21：I1 对厚度变量线性，I2 对 s=I1 二次。对 polynomial primitive，这一结构仍直接可积；一旦 primitive 含 denominator / square-root / sharp activation，经过矩阵函数复合与 whole-domain contraction 后就会形成 algebraic-period complexity。因此 second-order kinematics 是复杂度放大器，不是原始病灶。

## 6. 在继续任何新路线前必须完成的三个诊断

### D1 — source provenance audit
逐式追溯 U,C,T、Pi_eta、H、C2、T^8 以及 source-shaped interaction 到 Nguyen/Foster/我方 compiler，明确哪些是 SOURCE_PHYSICS，哪些是 SMOOTHING，哪些是 SURROGATE/COMPILER。

### D2 — necessity/domain audit
解析地确定 Case21/Swartz family 实际需要覆盖的主应变/等效 lambda 范围和拉伸激活范围，区分“物理必需域”与此前为了全局保险设置的宽泛 oracle square。不得用试验 Pu 反标或缩域。

### D3 — incompatibility audit
在不拟合任何新函数的前提下，判断以下四项是否可同时满足：

STRONG_MULTAXIAL_PHYSICS + ONE_UNIFIED_MAP + NO_DOMAIN_PARTITION + DIRECT_ZERO_QUADRATURE_LOW_COMPLEXITY_FORMULA。

若数学上只有通过高阶、多分支、大 special-function system 才能同时满足，则应重新讨论哪一条是可合理调整的建模约束，而不是继续换 compiler。

## 7. 当前禁止事项

在 D1-D3 完成前：

- NO P2R basis search
- NO new polynomial/rational/spline/special-function compiler fit
- NO Case21 Pu rerun
- NO Swartz24
- NO UHPC production fit
- NO PF/GKZ/ODE rescue
- NO spatial/material numerical integration

当前唯一允许的下一阶段是 ROOT_CAUSE_DIAGNOSTIC，不是新的计算路线。
