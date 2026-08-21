# NZ-SCCM — Ritz 的原始目的与有限停止原则

时间：2026-08-21 14:25 +08:00
状态：`THEORY_PURPOSE_RESTATEMENT_AND_EXECUTION_CORRECTION`

## 1. 为什么本项目引入 Ritz

Ritz 不是为了修改 NC-M6，也不是为了把面外屈曲形状不断变复杂，更不是为了靠 H2→H4→... 无休止升阶来“寻找一个看起来收敛的 Pu”。

Ritz 被引入的直接原因是：旧的单一 `alpha` / Airy 膜重分布假设已经不足以同时满足真实面内位移边界、多相预屈曲参考平衡和屈曲后的非均匀膜应力重分布。

旧 alpha 实际承担了两个本应分开的职责：

1. 修正 concrete-only Poisson reference 与 multiphase transverse equilibrium 的差异；
2. 表示 postbuckling nonuniform membrane redistribution。

对 Z 钢壳混凝土，nu_c=0.18 与 nu_s=0.30 使 concrete-only Poisson reference 下钢面在 q=0 已有非零 transverse stress/generalized force；对 RC，横向钢筋也会在混凝土 Poisson 横向应变下产生拉力。因此单个预设 alpha 形状不是一个可靠的完整膜内运动学空间。

Ritz 的目的就是把“猜一个膜应变形状”改成“先给出满足必要位移边界的面内位移函数空间，再由多相材料平衡自己决定各模态幅值”。

## 2. Ritz 在本理论中只负责面内膜场

固定的面外理想半波仍由 q 描述，NC-M6 仍是 frozen current material operator。

Ritz 只展开 u(x,y)、v(x,y)：

- essential displacement BC 由基函数逐项满足；
- kinematics 中不再放材料 Poisson ratio；
- concrete/steel/rebar/web 的不同 Poisson/constitutive response 全部留在 material operator 和广义平衡里；
- 模态系数由 virtual work/Bubnov-Galerkin residual 求解，而不是经验指定。

所以它的物理角色是：

`boundary-compatible in-plane membrane redistribution solver`。

而不是：

`higher-order out-of-plane buckling-mode generator`。

## 3. H2/H4/H6/... 的身份

H2、H4、H6、H8、H10、H12 不是不同理论，而是同一个完整 admissible in-plane Ritz space 的有限截断。

增加 N 只是在问：

“当前保留的面内 Fourier/Ritz 模态，是否已经足够表达真实膜内重分布？”

因此 consecutive-order comparison 原本只是空间充分性审计，不应该变成无限升阶的生产求解器。

## 4. 前一阶段执行偏离了 Ritz 原始目的

当 H6/H8/H10/H12 的局部约 18 MN fold 被错误当作 Pu 后，项目开始用：

`H_N -> 完整求 H_{N+1} -> 不过门槛 -> 再升一级`

作为唯一停止规则。

这是执行方法的偏移。对于 nonlinear material map，有限 Fourier strain 经过 M6 后可以产生更高谐波，单靠“下一阶差值”不存在事先保证的有限停止 N。

所以不能把“继续到 H14/H16 直到差值小”为最终 production doctrine。

## 5. 正确的有限停止机制：后验 Ritz 截断误差证书

生产理论需要在当前 H_N 解上直接估计未打开高阶空间还能造成多大修正。

定义当前解 y_N，在更高阶/互补 Ritz 模态上投影得到 tail residual：

`R_tail,N`。

当前同源 tangent / limit bordered operator 记作 `A_N`。一阶关系为：

`Delta y ~= - A_N^{-1} R_tail,N`。

此前项目在 Swartz H4→H6 和 H6→H8 audit 中已经验证：condition-aware / bordered tail correction 对膜场和荷载修正具有很高预测能力。这一关系以后应从 predictor 升级为 certified a-posteriori truncation bound。

最终目标不是永远求 N+1，而是在当前 N 得到：

- E_P,N >= |P_infty-P_N|；
- E_D,N >= |D_infty-D_N|；
- E_w,N >= |w_infty-w_N|；
- E_eps,N >= ||eps_infty-eps_N||。

一旦：

- E_P,N <= 0.5%；
- E_D,N <= 0.5%；
- E_w,N <= 1.0%；
- E_eps,N <= 2.0%；

就直接停止在 H_N，不需要完整求 H_{N+1}。

如果证书不通过，只升一个必要等级，再重新评价。

## 6. Ritz 的理论尽头是什么

数学尽头是完整 admissible space：

`F_infty = closure(union_N F_N)`。

工程/生产尽头不是 N→∞，而是第一个满足 certified truncation-error gate 的有限 N*。

因此正确流程为：

`physical problem + fixed w family + frozen M6`

→ `boundary-compatible u,v Ritz space`

→ `solve H_N equilibrium/control state`

→ `project unopened modes -> R_tail`

→ `source-consistent tangent/bordered operator filters R_tail`

→ `certified effect on P,D,w,eps`

→ if bound passes: STOP at N

→ else: enrich once and repeat.

## 7. 与当前 18 MN 审计的关系

在定义任何 Ritz truncation error 以前，必须先确认被比较的对象是同一个正确物理事件。

当前 Z0 的约 18.4 MN 已被识别为 high-order in-plane membrane fold，而不是已证明的 ultimate capacity；因此 H6/H8/H10/H12 对该局部 fold 的收敛不能拿来决定 production order。

当前顺序必须是：

1. 不升 H14；
2. 在已有空间中恢复真正的 Z0 controlling/ultimate event；
3. 固定 Pu/control identity；
4. 再对这个同一物理事件建立 a-posteriori Ritz truncation certificate。

## 8. 一句话定义

本项目中的 Ritz：

> 用满足结构面内边界条件的一组有限位移基，替代单一经验 Airy/alpha 膜形，让 concrete + steel/rebar/web 的真实多相 current equilibrium 自己决定轴压前后膜应力如何重新分布；阶次 N 只是这张膜内位移“画布”的分辨率，不是新的材料或新的屈曲理论。

## 9. 固定执行规则

- `RITZ_PURPOSE = IN_PLANE_BOUNDARY_COMPATIBLE_MEMBRANE_REDISRIBUTION`
- `RITZ_DOES_NOT_CHANGE_M6 = YES`
- `RITZ_DOES_NOT_CHANGE_FIXED_W_HALFWAVE_FAMILY = YES`
- `CONSECUTIVE_ORDER_ONLY_STOPPING = REJECTED`
- `APOSTERIORI_TRUNCATION_CERTIFICATE = REQUIRED_FOR_FINAL_PRODUCTION_STOP`
- `H14 = HOLD UNTIL PHYSICAL Pu IDENTITY IS RESTORED`
