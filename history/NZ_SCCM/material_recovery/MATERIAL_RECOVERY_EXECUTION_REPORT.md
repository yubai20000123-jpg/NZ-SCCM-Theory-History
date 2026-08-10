# NZ-SCCM 历史材料组件恢复执行报告（组合基线 v1.1）

## 1. 本轮任务

本轮不建立新材料函数、不计算板承载力，只执行：

1. 在账户文件库、当前会话文件和本地历史交付物中检索 D15 之后是否曾冻结普通混凝土或 UHPC 的正式有限解析材料系数；
2. 将已经真正实现并通过审计的材料组件从原求解框架中拆出，登记为可继承的“材料来源组件”；
3. 修正 v1.0 组合基线中“正式普通混凝土材料仍完全 OPEN”的过度概括。

硬边界保持不变：`m=1`、完全零空间数值积分、禁止板荷载反标定、禁止离散特值拟合、正式计算必须给出手算过程。

## 2. 检索范围与方法

执行了三类检索：

- File Library 与当前会话文件的近期导航和精确语义检索；
- 针对 `D15_UHPC_NUMERIC_A3_TO_A6`、`a3..a6`、`FROZEN/PASS/PRODUCTION`、`equation_to_code_registry_R20`、`n_branch_c.materials` 等对象的交叉检索；
- `/mnt/data` 已有交付物、报告、源码展开目录和清单的递归文本扫描。

未使用网页资料，也未根据记忆补写缺失文件。

## 3. 关键恢复结论

### 3.1 D15 精确矩引擎成功，但 UHPC 数值材料系数未冻结

原 D15 已完成：连续半波运动学、`I1/I2`、Newton 幂和、精确三角矩、精确厚度矩、有限材料基到全局多项式的零求积映射，以及 D11 机器精度回归。

原 D15 门禁同时明确：

```text
D15_UHPC_NUMERIC_A3_TO_A6 = PENDING
D15_UHPC_PANEL_CALCULATION = NOT STARTED
D15_PRODUCTION_USE = NOT AUTHORIZED
```

本轮没有检索到任何将 `a3...a6` 改为 `PASS/FROZEN/PRODUCTION` 的后继文件。因此不得继续假设历史上曾存在一套已经成功冻结但暂时遗失的 D15 UHPC 数值系数。

### 3.2 D15 来源注册表不是最终系数表

恢复的 `D15_UHPC_SOURCE_CONSTRAINT_REGISTRY.csv` 只锁定：

- 胡文旭型 UHPC 峰前/峰后受压关系；
- 纤维参数控制的受拉指数关系；
- 系数只能由材料曲线确定，禁止板荷载反算；
- 当时 L0 边界下多轴 beta 项取零；
- 周俊 DP 与王淑楠 W-W 作为可选多轴约束。

它提供的是来源和约束，不包含最终 `a3...a6` 数值。

### 3.3 后继理论已经废止 UHPC-L0 的正式材料身份

同日后继记录明确：D15 精确矩生成器可以保留，但“UHPC 仅调用两个主方向单轴曲线、永久关闭多轴项”的 L0 材料身份应废止；正式 UHPC 应恢复 U、TC、TT、CC、TCX、C3 等完整状态族。

所以即使以后找到一组旧 L0 系数，也只能作为历史回归对象，不能直接成为当前正式 UHPC 材料。

### 3.4 普通混凝土完整来源实现的历史审计证据已经恢复

R20 方程—代码注册表证明，Nguyen 普通混凝土来源实现已经完成并通过历史审计：

- U 状态内 TT、TC、CC 三条 Appendix-B 来源子路线；
- TC 含 1 个独立割线未知量、CC 含 2 个独立割线未知量；
- U/TC/TT/CC/TCX 五状态原始分支；
- U→TC、U→TT、U→CC、TC→TCX 的事件定位和历史变量传递；
- U→开裂状态的有限来源跳变保持，不做人为平滑；
- TC→TCX 连续连接；
- 24 组 Swartz 材料参数下 1056 个二维主应变点零失败；
- 96 条自然材料路径，粗细子步最大应力差约 `5.24e-7`；
- R16–R20 统一门禁记载 75/75 测试和 `compileall PASS`。

本轮恢复的是**来源实现及测试的注册证据**。对应 R20 源代码发布包的本地字节没有在当前容器中恢复，因此本轮没有重新执行那 75 项测试，也不声称完成了源码级复跑。

当前身份应写为：

```text
NSC_SOURCE_IMPLEMENTATION_EVIDENCE = RECOVERED_HISTORICAL_PASS
NSC_SOURCE_ORACLE = ACTIVE_REFERENCE_CORE
NSC_SOURCE_PACKAGE_LOCAL_BYTES = NOT_RECOVERED
NSC_ZERO_QUADRATURE_FINITE_OPERATOR = OPEN
```

这一区分修正了 v1.0 的过度概括：普通混凝土不是“来源材料理论尚未建立”，而是“来源模型已建立且有历史测试证据，但尚未转换成满足完全零空间积分的有限解析算子”。

### 3.5 UHPC 历史中仅恢复到部分来源组件

已恢复：

- Hu 型单轴受压和受拉来源关系；
- Liu 2023 TC 压缩标量子支路：压缩峰值软化、峰值应变、上升/下降段及相应导数；
- 周俊 DP、王淑楠 W-W 多轴破坏面约束；
- D19 精确状态前沿和事件系统，作为状态边界审计核心。

仍未闭合：

- 完整二维 TC 的拉向应力和裂缝剪切；
- TT 完整多轴拉伸算子；
- CC/C3 全过程应力—应变与一致切线；
- TCX 完整历史和残余关系；
- 满足完全零空间数值积分的正式有限材料算子。

因此：

```text
UHPC_SOURCE_FRAGMENTS = RECOVERED
UHPC_FULL_STATE_ZERO_QUADRATURE_OPERATOR = OPEN
```

## 4. 对 v1.0 组合基线的修正

旧表述：

```text
FORMAL_NSC_MATERIAL = OPEN
```

修正为：

```text
NSC_SOURCE_MATERIAL_IMPLEMENTATION = HISTORICAL_PASS_EVIDENCE_RECOVERED
NSC_ZERO_QUADRATURE_FINITE_REPRESENTATION = OPEN
```

UHPC 修正为：

```text
UHPC_SOURCE_COMPONENTS = PARTIAL_RECOVERED
UHPC_ZERO_QUADRATURE_FINITE_REPRESENTATION = OPEN
```

## 5. 本轮没有执行的内容

- 没有新造 P6、十项式或高阶正交材料函数；
- 没有从板荷载反算任何材料参数；
- 没有把 R20 材料点离散实现接入当前生产矩阵；
- 没有恢复 UHPC-L0 为正式材料；
- 没有计算 Swartz 24 板；
- 没有加入云露模块；
- 没有宣称重新运行 R20 历史测试。

## 6. 下一步唯一允许的工作

以 R20 Nguyen 来源实现的审计注册表和 Nguyen 原文为普通混凝土真值依据，按 U、TC、TT、CC、TCX 逐状态提取：

1. 来源方程与 Appendix-B 子程序；
2. 独立局部未知量；
3. 状态进入、保持、退出条件；
4. 应力和一致切线；
5. 能否由 D15 有限不变量基严格表示；
6. 阻止完全有限闭式的具体项。

UHPC 建立同格式表，但只登记已恢复来源；缺失项保持 OPEN。整个过程不得生成新的拟合系数。

## 7. 当前裁决

```text
D15_EXACT_MOMENT_ENGINE                    = PASS_RETAIN
D15_UHPC_A3_TO_A6_FROZEN_HISTORY           = NOT_FOUND_AND_ORIGINAL_STATUS_PENDING
D15_UHPC_L0_FORMAL_IDENTITY                = REJECTED_BY_LATER_LOCK

NGUYEN_R20_NSC_SOURCE_EVIDENCE              = RECOVERED_HISTORICAL_PASS
NGUYEN_R20_NSC_SOURCE_PACKAGE_LOCAL_BYTES   = NOT_RECOVERED
NGUYEN_R20_NSC_STATE_SET                    = U_TC_TT_CC_TCX_PASS_BY_REGISTRY
NGUYEN_R20_MATERIAL_DOMAIN_AUDIT            = PASS_1056_POINTS_BY_REGISTRY
NGUYEN_R20_NATURAL_PATH_AUDIT               = PASS_96_PATHS_BY_REGISTRY
NGUYEN_R20_COMPLETE_TEST_GATE               = PASS_75_OF_75_BY_REGISTRY
NSC_ZERO_QUADRATURE_FINITE_OPERATOR         = OPEN

UHPC_HU_UNIAXIAL_SOURCES                    = RECOVERED_SOURCE_LOCKED
UHPC_LIU_TC_COMPRESSION_SCALAR              = RECOVERED_PARTIAL_PASS
UHPC_DP_WW_MULTIAXIAL_CONSTRAINTS            = RECOVERED_REFERENCE
UHPC_FULL_STATE_ZERO_QUADRATURE_OPERATOR     = OPEN

SWARTZ24                                    = PAUSED
YUNLU_MODULE                                = NOT_STARTED
```
