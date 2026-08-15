# NZ-SCCM Z6 — 加载边面内约束可容许场 + 长宽比回退试算审计

**Timestamp:** 2026-08-15 18:13 +08:00  
**Status:** BOUNDARY-ADMISSIBLE FIELD CONSTRUCTION = PASS; ELASTIC STATIC CONDENSATION = PASS; ZERO-SPATIAL EXACT-MOMENT COMPATIBILITY = PASS; FULL NONLINEAR R10/N48 COUPLED CONDENSATION = REPRESENTATION/RUNTIME GATE; SQUARE-Z6 FALLBACK = PARTIAL BRANCH PROBE ONLY, NO Pu RELEASED

## 1. 本轮任务

按用户要求执行两级检查：

1. 优先尝试构造满足周思铭四边简支轴压模型真实面内加载边条件的连续 `u(x,y)`，并将新增面内幅值用能量最小/静力凝聚消去；
2. 若完整当前材料算子下无法立即闭合，则把 Z4/Z6 的加载方向高度 `a` 调整为 `a=b` 或 `a>b`，以原方法作长宽比诊断。

冻结：Nguyen 二阶几何、一个连续完整面外半波、R10/N48-C1-MM/Cayley-Hamilton/General-D15、A0=a/500、零正式结构空间采样/数值积分。不得用 Zhou/Winter 结果选根或调参。

## 2. 来源边界条件

周思铭博士论文表 1.3 的四边简支组合墙边界条件：

- 顶部加载边：`ux=0`, `uy=unset`, `uz=0`；
- 底部加载边：`ux=0`, `uy=0`, `uz=0`；
- 左右非加载边：`ux=unset`, `uy=unset`, `uz=0`。

取 `x in [0,b]` 为横向，`y in [0,a]` 为加载方向。于是本轮必须满足的面内本质条件是

`u(x,0)=u(x,a)=0`，而 `x=0,b` 两侧不得再施加 `u=0`。

## 3. 连续可容许场构造

定义

`X = pi x/b`, `Y = pi y/a`，

以及有限奇次 Fourier 截断 `N=1,3,5`：

`F_N(x)=-(4b/pi^2) sum_{n odd<=N} cos(nX)/n^2`

`H_N(x)=-(4b^2/pi^3) sum_{n odd<=N} sin(nX)/n^3`, 且 `dH_N/dx=F_N`。

取新增无量纲面内幅值 `c`：

`u = eps0 c F_N(x) sin^2(Y)`

`v = -eps0 D y - eps0 c H_N(x) (pi/a) sin(2Y)`。

该场满足：

1. `u(x,0)=u(x,a)=0` 精确成立；
2. `v` 的翘曲修正项在 `y=0,a` 精确为零，因此底边 `uy=0` 与顶部统一轴向缩短自由度可兼容；
3. `x=0,b` 的 `u` 不被设为零，左右边保持面内位移自由；
4. 由 `H_N,x=F_N`，新增线性剪切严格抵消：`u,y + v,x = 0`；
5. 奇次 `sin(nX)` 对 `N=1,3,5` 可写成 `sin X` 的有限多项式，`cos 2Y=1-2 sin^2Y`，所以新增应变仍属于有限三角-多项式场，可进入 D15 精确矩，不引入结构积分点。

对应新增归一化膜应变为

`ex,c = (4/pi) sum sin(nX)/n * sin^2(Y)`

`ey,c = (8/pi)(b/a)^2 sum sin(nX)/n^3 * cos(2Y)`

且新增线性 `gamma_xy,c=0`。

**结论：从运动学、边界和零空间积分三个层面，构造是可行的，不存在理论上的“做不到”。**

## 4. 线弹性静力凝聚闭式解

先在 `q=0` 的各向同性平面应力层面做严格预检。忽略与 `c,D` 无关的正因子后，面积积分可写成

`I_N(c,D)=A_N c^2 - 2 B_N D c + pi^2 D^2`。

故静力凝聚/能量驻值给出

`c*(D)=(B_N/A_N)D`。

其中 `k=b/a`：

### N=1

`A1 = 16 k^4 - 8 nu k^2 + 3`

`B1 = 4 nu`

### N=3

`A3 = 2(5840 k^4 - 2952 nu k^2 + 1215)/729`

`B3 = 40 nu/9`

### N=5

`A5 = (182511664 k^4 - 92395800 nu k^2 + 39335625)/11390625`

`B5 = 1036 nu/225`

凝聚后的轴向膜刚度相对原自由泊松单轴状态为

`Keff/Kfree = [pi^2 - B_N^2/A_N] / [pi^2(1-nu^2)]`。

对 Z4/Z6 共同的 `a/b=0.75`, `nu=0.18`：

|N|c/D|c/(nu D)|Keff/Kfree|
|---:|---:|---:|---:|
|1|0.01411546|0.07842|1.03242069|
|3|0.01557057|0.08650|1.03218055|
|5|0.01609379|0.08941|1.03208818|

`N=1 -> 3 -> 5` 后凝聚刚度已经收敛到约 `+3.21%`，表明这个可容许场族在纯线弹性层面数值稳定。

N=5 时，板中高 `y=a/2` 处侧边横向位移只约为自由泊松横向位移的 `8.34%`。这定量说明 `a/b=0.75` 时加载边 `ux=0` 对全板泊松展开的抑制确实很强。

但必须强调：线弹性刚度只提高约 3.2%，**单凭线弹性端部约束不可能直接宣称解释 Z6 约 24.5% 的 Pu 差值**。若该机制最终重要，只能通过它对二维 current stress、材料切线、钢材屈服面和几何刚度的非线性耦合放大。

## 5. 长宽比变化下的凝聚趋势

N=5, `nu=0.18`：

|a/b|c/D|c/(nu D)|Keff/Kfree|中高侧边 u / 自由泊松 u|
|---:|---:|---:|---:|---:|
|0.75|0.01609|0.0894|1.03209|0.0834|
|1.00|0.04600|0.2556|1.02949|0.2385|
|1.25|0.09126|0.5070|1.02556|0.4731|
|1.50|0.13884|0.7713|1.02144|0.7197|

随着 `a/b` 增大，板中部逐渐恢复自由泊松展开，这与加载端约束逐渐从“全板效应”转为“端部效应”的物理预期一致。

## 6. 完整 R10/N48 current operator 耦合尝试

已将上述场写成与当前 D15 兼容的有限 `sin X, sin Y, eta` 多项式，并尝试把

`ex = ex_Nguyen + c ex,c`

`ey = ey_Nguyen + c ey,c`

直接送入一般化 `Eu -> invariants -> R10/N48 -> Cayley-Hamilton -> stress`，再联立

`Rq(D,q,c)=0`

`Rc(D,q,c)=0`。

理论上 `Rc` 可由同一虚功形式精确写出，不需要标量势能；因此即便 current material operator 未全局证明存在单一势函数，静力凝聚仍可定义。

实际执行发现：将任意 `c` 场先完整展开成一般二维不变量，再做 48 阶 CH 复合，系数张量增长明显，单次一般化 concrete evaluation 已进入十秒级乃至更高，重复二维根求解不适合作为当前可验证生产路径。继续强行迭代会重演之前 finite-q31 的 naive expand-then-compose 条件恶化。

因此本轮在这里执行 fail-fast：

`BOUNDARY_WARP_KINEMATIC_FEASIBILITY = PASS`

`ELASTIC_STATIC_CONDENSATION = PASS`

`D15_FINITE_EXACT_MOMENT_COMPATIBILITY = PASS`

`NAIVE_FULL_R10_N48_GENERALIZED_COMPOSITION_FOR_COUPLED_Rq_Rc = REPRESENTATION/RUNTIME FAIL`

这不是理论做不到，而是当前通用系数实现需要改为“moment-first / sparse invariant derivative”而不是先把整个高阶 current map 展开。

## 7. 用户建议的长宽比回退：Z4/Z6 改成 a=b 或 a=1.25b

虽然第一条在理论上已经可行，但为了提供独立诊断，仍执行了参数回退的来源侧比较。

保持各自 `b,h,ns,ls,ts,fy,fcu` 不变，只修改加载方向高度 `a`：

### Z4

- base: `a/b=0.75`, a=6000, b=8000
- square: `a/b=1.0`, a=8000
- taller: `a/b=1.25`, a=10000

### Z6

- base: `a/b=0.75`, a=9000, b=12000
- square: `a/b=1.0`, a=12000
- taller: `a/b=1.25`, a=15000

上述三个长宽比均仍由 `m=1` 控制（未跨过经典 `sqrt(2)` 的换半波界附近到更高整数模态）。

周思铭原理论/拟合比较值：

|case|a/b|m|Pcr (MN)|lambda_n|Zhou lower Pu (MN)|
|---|---:|---:|---:|---:|---:|
|Z4 base|0.75|1|196.4112|0.63575|70.1873|
|Z4 square|1.00|1|179.7548|0.66456|69.3399|
|Z4 1.25b|1.25|1|187.5893|0.65053|69.7569|
|Z6 base|0.75|1|42.8315|1.43411|49.6724|
|Z6 square|1.00|1|39.2880|1.49738|49.4868|
|Z6 1.25b|1.25|1|41.0414|1.46505|49.5084|

非常重要：**对 Z6，仅把 a/b 从 0.75 改到 1.0 或 1.25，Zhou 下包络 Pu 仍约 49.5 MN，几乎不变。** 因此这组虚拟算例非常适合作为 NZ 自身长宽比敏感性鉴别器。

## 8. Z6-square 原 NZ 单-q/current-local-cap 部分支路试探

对 `a=b=12000`, `h=130`, `ns=60`, `q0=a/(500b)=0.002`，保持旧单-q 路径和 current local radial-cap，不用 Zhou 荷载选根。

已完成的点：

|D|q|P (MN)|Rq (MN mm)|
|---:|---:|---:|---:|
|0.60|0.0025|47.4096|-2414.65|
|0.60|0.0040|41.0537|-1754.87|
|0.60|0.0055|36.3539|-748.85|
|0.70|0.0030|50.3133|-3090.53|
|0.70|0.0045|44.4759|-2599.68|
|0.70|0.0060|40.0764|-1658.03|
|0.80|0.0035|52.9858|-3825.30|
|0.80|0.0050|47.6163|-3448.83|

这些点尚未出现 `Rq` 变号，因此**不能发布 square-Z6 的 connected root，更不能发布 Pu**。继续往更大 q 推进时，N48/CH 系数规模和计算时间迅速增大；本轮不允许根据 Zhou≈49.5 MN 反向挑 q。

因此：

`Z6_SQUARE_FULL_NZ_Pu = NOT SOLVED`

`Z6_SQUARE_PARTIAL_BRANCH = PERSISTED`

## 9. 当前结论

本轮最重要的不是得到一个新 Pu，而是完成了“是否做得到”的门禁：

1. **可以**构造满足 Zhou 加载边 `ux=0`、左右边面内自由的连续可容许场；
2. 新幅值可在线弹性层面完全闭式凝聚；
3. 该场保持有限三角多项式身份，因此与零结构积分/D15 理论兼容；
4. 对 Z6 的 `a/b=0.75`，横向泊松展开确实受到强烈抑制，但线弹性轴向刚度只增加约 3.2%，不能直接解释 24.5% Pu 差值；
5. 真正剩余任务是将 `Rc=0` 以 sparse/moment-first 方式并入 current R10/N48，而不是 naive 全展开；
6. square/taller Z6 的 Zhou 比较值几乎不变，因此一旦 NZ 的 square-Z6 connected Pu 能稳定求出，它将是非常强的机制鉴别测试。

## 10. 下一执行门禁

`CURRENT_NEXT_TASK = Z6_BOUNDARY_WARP_SPARSE_STATIC_CONDENSATION`

要求：

- 仅新增一个面内 `c`，先用 N=1；
- `u,v` 采用本报告可容许场；
- 不新增 out-of-plane mode；
- `Rc=0` 用 current stress 的虚功凝聚，不要求构造全局势函数；
- 不展开完整高阶 stress polynomial，改为 sparse invariant directional moment / moment-first contraction；
- 先在 q=0 退化回本报告闭式 c/D；
- 再计算 Z4 与 Z6；
- 若仍遇表示门禁，则转为完成 Z6-square / Z6-1.25b 原单-q 支路，但不得用 Zhou 值选根。
