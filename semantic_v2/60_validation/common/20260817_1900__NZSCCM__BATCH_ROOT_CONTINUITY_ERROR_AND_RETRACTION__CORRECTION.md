# NZ-SCCM — 2026-08-17 批量结果最终复算修正

**Timestamp:** 2026-08-17 19:14 +08:00  
**Identity:** FINAL IMPLEMENTATION CORRECTION / CONNECTED-BRANCH RECALCULATION  
**Parent theory:** `20260817_1824__NZSCCM__ZERO_SPATIAL_DISCRETIZATION_FINITE_CURRENT_TRUE_INFINITE_D15__CANONICAL_LOCK.md`

## 1. 最终修正

当前 canonical theory 保持不变：有限 current operator、真无限解析表示、exact 2x2 Cayley–Hamilton、General-D15 精确连续域矩、零正式空间离散与零正式空间数值积分。

19:00 版本中“只要 `lambda_A<0` 就判为 disconnected/nonphysical root”的快速诊断过强，现由显式低荷载连续支路复算正式 supersede。

正确的膜内根身份不是由 `lambda_A` 的正负单独判断，而是由

```text
(q, alpha=lambda_A*M) 的连续性
+ total Rq=0, RA=0 的残量闭合
+ 从低荷载兼容 Airy/FvK 状态连续延伸
+ 同一支路的 first reachable limit point
```

共同确定。`lambda_A` 可以在合法连续支路上经过零或变为负值；当 `M -> 0` 时只要 `alpha=lambda_A*M -> 0` 且完整膜内场保持连续，就不能仅凭 `lambda_A` 的数值或符号宣告根非法。

## 2. Swartz24 真正的批量实现错误

重新核对 Nguyen / Swartz 的物理半波后，上一轮 19:46 批量表的首要错误是错误地把 Case1–Case24 全部设成

```text
ell = 1220 mm
```

而来源与历史正式映射应为：

```text
Case1–Case16:
physical a = 2440 mm
one complete halfwave over full length
ell = 2440 mm
k = b/ell = 0.5

Case17–Case24:
physical a = 2440 mm
m*=2 repeated halfwaves
one representative complete halfwave
ell = 1220 mm
k = 1
```

因此 19:46 的 Case1–Case16 数值因错误 halfwave identity 被撤回；Case17–Case24 的 halfwave identity 本来正确，其中 Case21 继续采用已独立释放的 formal exact-D15 anchor。

## 3. Z0–Z5 的最终复核

本次按用户指定统一修改为

```text
a = 2b
boundary = theoretical four-edge simply supported
m*=2
ell=b
A0=a/500
q0=0.004
```

并从低荷载状态显式连续追踪 `(q,alpha)`，而不是在每个状态独立挑选 `RA=0` 的任意代数根。

复算后 Z0–Z5 的 first connected limit 仍落在与 19:46 数值非常接近的位置。因此本轮 Z0–Z5 的低值 **不是** 由离散的 Airy-scalar 根跳转造成。

这与旧历史“Z0–Z5 多数高于 Zhou、低于 Winter”的记忆并不矛盾，因为旧比较对应原始不同长宽比几何；本轮对象已经全部人为改成 `a/b=2`，同时 `A0=a/500`、控制半波以及 Zhou/Winter 同参数 replay 均随之改变。二者必须作为不同几何对象比较。

## 4. 当前控制结果身份

```text
20260817_1946_CASE01_CASE24_Z0_Z5_BATCH = SUPERSEDED
20260817_1914_UNIFIED_CALCULATION_BOOK = CURRENT BATCH RESULT
CASE21_RELEASED_FORMAL_ANCHOR_366.767828685_kN = RETAINED
Z6_RELEASED_FORMAL_ANCHOR_48.4061215_MN = RETAINED
CANONICAL_ZERO_SPATIAL_DISCRETIZATION_TRUE_INFINITE_D15_THEORY = RETAINED
```

Swartz24 的新结果必须采用 Case1–16 `ell=2440`、Case17–24 `ell=1220`；Z0–Z5 采用统一 AR2/SSSS 的 connected-branch 结果。

## 5. 正式根规则

每一块板统一执行：

```text
1. 从低荷载、小附加挠度状态开始；
2. 用 alpha=lambda_A*M 作为连续膜内物理幅值检查量；
3. 所有材料相在求解前共同进入 P,Rq,RA；
4. 沿同一 (q,alpha) equilibrium branch 连续推进；
5. 不允许按 comparator 或实验值换根；
6. 取该支路 first reachable limit point；
7. Pu 冻结后才读取 Pf / Zhou / Winter 比较。
```

本修正不改变 R10、钢材 current map、D15、解析级数、正式空间计数器或比较公式，只修复 halfwave identity 与根连续性实现判断。