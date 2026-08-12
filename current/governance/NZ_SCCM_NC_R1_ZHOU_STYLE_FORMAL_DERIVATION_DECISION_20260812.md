# GOVERNANCE DECISION — NC-R1 周思铭式正式逐式理论推导

**日期：2026-08-12**  
**身份：CURRENT GOVERNING THEORY-WRITING DECISION**

## 1. 决定

新增并冻结以下文件作为当前 NC + Rebar 理论的正式“逐式、逐参数、逐来源”写作基线：

- `current/theory/NZ_SCCM_NC_R1_ZHOU_STYLE_FORMAL_EQUATION_DERIVATION_20260812.md`

该文件在不改变任何上游理论的前提下，把以下链条统一展开：

```text
material/geometric parameters
-> frozen closed R10
-> primitives {U,C,T,T^7}
-> direct N48 general coefficient formula
-> N48-C1 for U/C/T7
-> strict-C1 constrained minimax for T
-> Cayley-Hamilton 2D lift
-> Nguyen second-order one continuous complete halfwave
-> finite analytic coefficient convolution
-> D15 exact moments
-> Pc / Rq,c
-> Rebar contribution
-> total P / Rq
-> level-set tangent and L
-> NC-R1 admissible domain / primary connected branch
-> first +->- maximum
-> unique production Pu
-> R_norm / L_norm
-> Zhou Dx-Dy-H current-tangent stability gate
```

## 2. 写作风格冻结

正式理论正文采用周思铭博士论文式理论写法：

1. 先给出研究对象、边界和理论假定；
2. 每个公式单独编号；
3. 每个公式后必须给出“式中，xxx 表示……”；
4. 同时给出参数/公式的来源身份；
5. 不把程序实现细节冒充理论；
6. 不以结构试验值解释材料参数来源；
7. 明确区分来源材料、解析编译、数学恒等式、结构运动学、精确矩和根生产合同。

## 3. 当前正式身份

```text
R10_MATERIAL_TARGET = FROZEN
MATERIAL_COMPILER_ORDER = 48
U_COMPILER = N48-C1
C_COMPILER = N48-C1
T7_COMPILER = N48-C1
T_COMPILER = N48-C1-CONSTRAINED-MINIMAX
CAYLEY_HAMILTON = GOVERNING
KINEMATICS = NGUYEN_SECOND_ORDER
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
D15 = GOVERNING
NC_R1_LIMIT_ROOT_PRODUCTION_CONTRACT = GOVERNING
ZHOU_Dx_Dy_H = TANGENT-STABILITY ACCEPTANCE / INTERPRETATION
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_SPATIAL_SAMPLING = 0
FORMAL_SPATIAL_SUBDOMAINS = 1
STRUCTURAL_CALIBRATION = NO
```

## 4. 不得误读为新理论版本

本文件不创建新的材料模型或求解器，也不改变 NC-R1 的物理定义。

“NC-R1 周思铭式正式逐式推导”只是把当前 governing chain 和 NC-R1 root-production contract 写成统一论文式理论章节。它不是：

- R11；
- N49/N96；
- D16；
- 新 Pu solver；
- 新 Zhou solver；
- 新 UHPC operator；
- 新 Steel Shell operator。

## 5. 来源边界

周思铭原论文提供并支持的是正交各向异性板稳定、方向刚度和 Navier 稳定语言。当前文件只继承其“理论章节写法”和 `Dx-Dy-H` 稳定骨架；不得把周思铭组合墙的截面常数直接搬入 Swartz RC 板。

Nguyen 提供的是来源物理、初始缺陷和二阶运动学；其历史 FE/Gauss 数值路线不恢复为正式生产方法。

D15 只保留 exact-moment 数学引擎；旧 UHPC Layer-0 材料身份继续禁止。

## 6. 执行边界

本次只完成理论写作和 GitHub 同步：

```text
NEW_CASE21_CALCULATION = NO
SWARTZ24_RECALCULATION = NO
R10_REOPEN = NO
N48_ORDER_ESCALATION = NO
T_MINIMAX_CHANGE = NO
D15_CHANGE = NO
NC_R1_CHANGE = NO
UHPC_OPERATOR_CREATION = NO
STEEL_SHELL_OPERATOR_CREATION = NO
```

下一步仍由用户单独授权，不因本文件创建而自动进入任何数值计算阶段。
