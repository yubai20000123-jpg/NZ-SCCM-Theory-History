# NZ-SCCM 显式执行证据规则 — 2026-08-10

**Status:** CURRENT GOVERNANCE / MANDATORY FOR ALL NEXT STEPS

## 1. 核心要求

以后任何被称为“执行”“通过”“闭合”“验证”的步骤，都必须在聊天中真正展示其计算对象、公式、变换、实际中间结果和最终判定；不得只给出“已执行”“脚本可生成”“矩阵已得到”“误差已验证”等摘要性叙述。

## 2. 最低可见证据

每一步至少必须公开：

1. 本步唯一输入及其来源/版本；
2. 本步实际使用的公式，不只写算法名称；
3. 变量代换、代数化简或拟合方式；
4. 实际系数、实际中间表达或实际数值表；
5. 误差或恒等式的逐项检查结果；
6. 复杂度指标：阶数、项数、未知量、矩阵维数、非零项数；
7. 明确 PASS/HOLD/FAIL 门禁；
8. 若产生正式公式，必须在聊天中直接给出，不能仅说“完整公式在脚本中可生成”。

## 3. 脚本的身份

脚本只能作为复现器和独立核验器，不能替代公式本身。以下说法不得单独构成 PASS：

- “代码可重新生成”；
- “符号矩阵已存 JSON”；
- “数值交叉验证通过”；
- “存在有限 Picard–Fuchs/Gauss–Manin system”。

若正式理论需要一个大辅助系统、隐藏初值积分、ODE 步进、branch patch 或大规模符号对象才能得到 P/Rq/L，则必须触发 production complexity gate。

## 4. 当前 production complexity 边界

继续冻结：

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_auxiliary_numerical_quadrature = 0
N_auxiliary_ODE_steps = 0
NO hidden initial-value integration
NO large connection system as production operator
```

最终 production 输出应直接回到：

```text
P(D,q)
Rq(D,q)
P_,D, P_,q
Rq_,D, Rq_,q
L = P_,D Rq_,q - P_,q Rq_,D
```

并由有限、明确、可审计的解析项组成。

## 5. 下一任务的执行纪律

下一任务 `M1R_P2_INTEGRABILITY_FIRST_PRIMITIVE_COMPILER_SCREEN` 必须分门执行：

- P2-A：五个一维 primitive 的直接 polynomial/orthogonal-polynomial 编译筛选；
- P2-B：source-shaped 二维材料面重构误差；
- P2-C：二维 Cayley–Hamilton 精确降阶；
- P2-D：代入 Case21 I1/I2 后的 exact-moment term-count 审计；
- P2-E：仅当 A-D 全通过，才允许进入 P/Rq 公式生成。

任一门 FAIL 即停止，不得用新的特殊函数系统继续“救”该表示。
