# NZ-SCCM — NC-M1 九宫格材料函数审计与撤回

时间：2026-08-20 14:32 +08:00

## 1. 本轮来源

本轮从用户提出的 3×3 主应变符号九宫格出发：横向按 ε1<0 / =0 / >0，纵向按 ε2<0 / =0 / >0。目标不是继续拟合 Nguyen/Foster，而是寻找一个更低复杂度、能直接进入后续连续虚功/多重积分的普通混凝土 current material law。

## 2. 已生成但现正式撤回的 NC-M1

NC-M1 曾采用：

- compression backbone：三段式，峰前 2c-c^2，随后线性下降，再进入 0.5 平台；
- tension backbone：弹性上升 + 线性软化 + 零平台；
- TC/CT softening：1 平台 + 线性下降 + 0.4 平台；
- CC enhancement：η=1+0.15ρ，ρ=min(c1,c2)/max(c1,c2)。

并绘制了九宫格材料图以及 compression / tension / TC softening / CC enhancement 四张新旧对比曲线。

## 3. 用户指出的问题

用户观察到：NC-M1 的“简化”并没有降低真正的材料算子复杂度，反而出现更多人为分段、阈值和 min/max；部分曲线比原始参考曲线更不自然。

该判断成立。

## 4. 审计结论

NC-M1 不再作为 production / formal candidate，身份改为：

**REJECTED_DIAGNOSTIC_CANDIDATE**

原因不是它不能计算，而是其复杂度方向错误：

1. compression：M1 使用 3 个分支和 2 个新增阈值；原参考关系本身并没有因此被真正简化。
2. tension：M1 仍是多段式，还新增了 t=6 的人为归零点；没有减少 branch count，且改变后期耗能。
3. TC：M1 从原来的“常数上限 + 一个有理下降式”变成“平台 + 线性段 + 平台”，branch 数更多，并新增 t=2 人为阈值。
4. CC：η=1+0.15ρ 虽然图上是直线，但 ρ=min/max 本身引入 min、max、除法和排序逻辑；对解析 current operator 并不比原 Foster 形式更干净。

因此不能用“曲线画起来更直”来等价于“材料函数更简单”。正式复杂度指标应改为：

- 分支数量；
- 新阈值数量；
- min/max/positive-part 数量；
- 根号 / 主方向依赖；
- 有理分母数量与次数；
- 是否引入额外状态变量或历史变量；
- 代入连续应变场后积分核的代数复杂度。

## 5. 当前新的设计原则

后续材料简化不再追求“直线化”或“贴着 Nguyen 原式拟合”。优先顺序改为：

1. 每个九宫格实体象限尽量 1 个单表达式；
2. 边界 ε1=0、ε2=0 由实体象限自然退化，不额外建立材料分支；
3. 避免 min/max、abs、positive-part、状态机；
4. 如果一个经典原式已经很短，不为了“看起来新”而强行替换；
5. 新关系可以来自其他经典 concrete laws，也可以构造，但必须先比较 operator complexity，再比较曲线误差；
6. 不用 Case21 Pu 反标材料参数；先做纯材料面审计，再做结构验证。

## 6. 九宫格仍保留

九宫格思想本身保留。它的作用是将二维 principal-strain material law 组织为 CC / TC / CT / TT 以及自然单轴边界，而不是强迫每格再人为分成多个子段。

## 7. 与结构积分的关系

结构层继续采用：

ε(x,y,z; Δ,A,εm) -> principal strains -> 九宫格唯一局部 material response -> scalar virtual-work density -> one continuous volume integral -> RA,Rm,P -> three-variable equilibrium/limit system.

此前把 CC / TC / TT 分别延拓到全域后再相加得到的 603 kN diagnostic 已撤销，不代表理论预测。

## 8. GitHub 同步纪律更新

从本检查点开始，本项目中具有实质理论、计算、否决或当前状态意义的检查点，应在本轮完成后直接同步 GitHub；不再把“是否同步”作为需要用户额外确认的后续动作。
