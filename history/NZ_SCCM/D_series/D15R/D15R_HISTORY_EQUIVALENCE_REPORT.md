# D15R：历史等价性核验与精确矩恢复报告

## 1. 核验结论

用户记忆正确。当前提出的“有限项材料函数 + 不变量 + 精确空间矩”并不是一条全新路线，其直接历史对应物是 D15。

D15 已经完成：

1. 用 `I1、I2` 和主应变幂和递推消除显式主应变根式；
2. 用有限材料基生成精确三角矩和厚度矩；
3. 生成有限的材料基—全局单项式映射；
4. 运行时不使用空间积分或板级投影。

因此本阶段不再重造一个平行模型，而是恢复 D15 精确矩引擎，并把 D15 后来被否决的材料简化与仍可保留的数学引擎分开。

## 2. D15 中可直接继承与不可直接继承的部分

### 可直接继承

- `m=1` 连续完整半波运动学；
- 精确三角矩 `J_pq`；
- 精确厚度矩 `Z_h`；
- Newton 幂和递推；
- 有限材料基到全局单项式的自动展开；
- 零空间求积运行结构。

### 不可直接继承

- UHPC-L0 仅按两个主方向单轴曲线的材料身份；
- 所有多轴系数 `beta=0` 的永久设置；
- 取消 U/TC/TT/CC/TCX 状态信息的材料解释；
- 未经形状约束和认证域审计的 `a3...a6`；
- 单一标量势必然要求切线主对称的限制。

## 3. 本轮恢复结果

恢复的十二个历史 D15 材料基为：

- `p2/2 ... p6/6`；
- `I2`；
- 六个 `beta` 多轴项。

程序通过精确 Beta/Gamma 矩和厚度幂矩，生成 **155 条非零全局映射**。历史报告写为 156 条。本轮没有人为补一条零项来凑数；差异暂标记为计数口径开放项，可能来自历史零项、元数据项或其他计数对象。

这项差异不影响精确矩原理，但必须在找到历史原 CSV 后逐行核对，不能靠猜测消除。

## 4. 正确的后继材料接口

Nguyen 来源切线不一定对称，因此不能先验要求普通混凝土和 UHPC 全部来自一个标量势。二维各向同性、主方向共轴的有限解析向量接口可写为：

\[
\boldsymbol\sigma
=a(I_1,I_2)\mathbf I+b(I_1,I_2)\mathbf E.
\]

该形式仍然完全由有限多项式组成，并能保持零空间求积；当 `a,b` 不满足势函数可积条件时，一致切线可以非对称。

本轮只实现并验证了这一数学接口，没有识别普通混凝土或 UHPC 系数，也没有改变冻结的 D19R 来源材料。

## 5. 当前门禁

```text
D15_ROUTE_IDENTIFICATION                  = PASS
D15_EXACT_MOMENT_ENGINE_REACTIVATION      = PASS
RUNTIME_SPATIAL_QUADRATURE                = ZERO
OFFLINE_SPATIAL_QUADRATURE                = ZERO
PANEL_LEVEL_PROJECTION                    = ZERO
COMMON_VECTOR_OPERATOR_INTERFACE          = PASS_MATHEMATICAL_ONLY
NSC_SOURCE_CONSTRAINED_COEFFICIENTS        = OPEN
UHPC_SOURCE_CONSTRAINED_COEFFICIENTS       = OPEN
SWARTZ24                                   = NOT_AUTHORIZED
YUNLU_COUPLING                             = NOT_STARTED
```
