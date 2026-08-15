# NZ-SCCM — Z6 固定 D=.50 的增广 FvK 膜力耦合平衡执行报告

**Timestamp:** 2026-08-15 21:53 +08:00  
**Identity:** FIXED-D COUPLED EXECUTION / NO Pu / GENERAL D15 RETAINED  

## 1. 目的

承接 21:44 gate。当前已经确认旧 `D+q+c` 状态在新的 admissible membrane virtual directions 上存在显著

```text
R20 != 0
R02 != 0
```

因此本轮不再只做投影，而是在固定 `D=.50` 下第一次实际求解最小单半波 FvK 膜力补全系统：

```text
Rq(q,c,p20,p02)=0
Rc(q,c,p20,p02)=0
R20(q,c,p20,p02)=0
R02(q,c,p20,p02)=0
```

全程不求 Pu、不推进 D。

## 2. 理论与积分保持不变

冻结：

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order kinematics
R10 current concrete operator
N48-C1/MM analytic material compilation
Cayley-Hamilton 2D current map
General D15 exact structural moments
local steel radial-cap current operator
A0=a/500
```

新增的 `p20,p02` 仍只是 finite analytic in-plane strain polynomials：

```text
e20x = y^2 - 2*x^2*y^2
e20y = (k^2/2)*(1-2*x^2)*(1-2*y^2)
e02x = 0
e02y = 1-2*y^2
```

因此正式结构积分仍是 D15 coefficient moments：

```text
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
```

## 3. 父状态复现

固定

```text
D=.50
q=.007244278905
c=-.0154563484942
p20=0
p02=0
```

用同一 current-map + D15 evaluator 复现：

```text
P   = 37.3451400961 MN
Pc  = 21.0700464554 MN
Ps  = 16.2750936407 MN
Rq  = +0.0013712476 MN mm
Rc  = +0.0000989812 MN mm
R20 = -19.4868582197 MN mm
R02 = -23.4734840601 MN mm
```

这与 21:44 projection gate 一致，说明本轮从同一父状态出发。

## 4. 第一级预条件：只用线性复合面内切线估计 p20/p02/c 方向

为了避免直接在 4D current map 上盲目 Newton，先只把钢+混凝土线弹性平面应力刚度当作 **Newton preconditioner**，不是替代材料模型。

该预条件器对 `[c,p20,p02]` 给出的第一修正约为：

```text
dc   = -0.03021656
dp20 = -0.01566154
dp02 = +0.10544004
```

于是候选 A：

```text
q=.007244278905
c=-.04567291
p20=-.01566154
p02=.10544004
```

带回完整 R10/N48/CH/D15 current evaluator：

```text
P   = 38.70382734 MN
Rq  = -576.44691572 MN mm
Rc  = +21.53268311 MN mm
R20 = -3.48191355 MN mm
R02 = +0.53893945 MN mm
```

结论：预条件器正确抓到了 `R20/R02` 消减方向，但由于 q-c-membrane 强耦合，不能把线弹性切线当作最终 Newton Jacobian。

## 5. 第二级：在完整 current D15 evaluator 上建立实际 4x4 数值 Jacobian

选 base candidate B：

```text
q=.00754262
c=-.06578089
p20=-.03749721
p02=.15577310
```

以 coefficient pruning tolerance `2e-5` 做 current D15 方向差分，步长：

```text
dq=1e-4
dc=1e-3
dp20=1e-3
dp02=1e-3
```

得到实际残量 Jacobian（单位 MN mm / generalized-coordinate）：

```text
             q               c             p20           p02
Rq   +2787333.552306   +96636.847993   -7730.455557  +19480.240744
Rc     +67271.966759    +7906.237458    -914.530413   +2343.313840
R20    -20821.855030     -785.947042    +155.898351     +46.725646
R02     -4168.426027    +2094.413911    -426.456221    +882.897056
```

`cond(J) ~= 1.7401e4`。

因此这个固定-D 耦合问题并不是奇异的，但明显病态；这也解释了为什么用单纯 secant / naive 4D root 很容易跳动或变慢。

对 B 状态做一次 Newton 修正：

```text
dq   = +0.000467
dc   = -0.011271
dp20 = -0.022543
dp02 = +0.007563
```

得到候选 C：

```text
q=.008009
c=-.077052
p20=-.060040
p02=.163336
```

在 coefficient pruning tolerance `1e-4` 下：

```text
P   = 37.60669527 MN
Rq  = +34.10861812 MN mm
Rc  = +0.18353536 MN mm
R20 = -0.57623038 MN mm
R02 = -0.68469288 MN mm
```

四残量已经从父状态中几十 MN mm 的漏项收缩到近零邻域。

## 6. 当前最佳 fixed-D=.50 增广 near-equilibrium checkpoint

进一步用同一 Jacobian 作小修正后，得到：

```text
D=.50
q=.008002
c=-.077622
p20=-.060657
p02=.165133
```

在 coefficient pruning tolerance `2e-4` 下：

```text
P   = 37.6959155513 MN
Pc  = 21.8832880065 MN
Ps  = 15.8126275449 MN

Rq  = -3.0633091506 MN mm
Rc  = +0.0100538389 MN mm
R20 = -0.0530074366 MN mm
R02 = -0.0237314047 MN mm
```

残量分解：

```text
Rqc  = -2979.7322758342
Rqs  = +2976.6689666836

Rcc  = -13.2483108482
Rcs  = +13.2583646871

R20c = -4.0298962207
R20s = +3.9768887841

R02c = -12.5706052016
R02s = +12.5468737970   MN mm
```

以 `|R|/(|Rc-part|+|Rs-part|)` 衡量内部 cancellation closure：

```text
Rq  : 0.05143 %
Rc  : 0.03793 %
R20 : 0.66203 %
R02 : 0.09448 %
```

因此四个独立广义平衡方向都已经进入同一小残量邻域；尤其 21:44 时的

```text
R20=-19.49
R02=-23.47 MN mm
```

已被实际的 `p20,p02` 重分布自由度消除到约 `10^-2 ~ 10^-1 MN mm`。

## 7. 同一 D 下荷载只作状态量，不是 Pu

父 `D+q+c` 状态：

```text
P_parent=37.34513713 MN
```

增广 near-equilibrium：

```text
P_aug≈37.69592 MN
```

同一 D 下约增加 `0.35078 MN = +0.9393%`。

这只说明释放 FvK membrane redistribution 后固定缩短状态的轴力发生真实重分配；**不能外推成 Pu 改善幅度**。

## 8. 材料域审计

为确认 near-root 不是跑出冻结材料域，做了独立的非积分 dense audit sampling（仅审计范围，不参与正式积分）：

```text
normalized principal lambda approx range = [-0.8212, +0.1852]
N48 inherited interval                    = [-1.75, +0.45]
```

所以候选仍在 inherited N48 区间内部。

钢壳 elastic-trial radial invariant：

```text
r approx range = [0.0142, 0.7864]
```

`rmax<1`，说明当前 fixed-D=.50 增广 near-root 并不是被局部钢屈服 cap 控制；这里的主要变化确实来自面内膜力重分布。

## 9. coefficient-pruning sensitivity 与 runtime gate

同一候选用较松 pruning `5e-4`：

```text
P   =37.70233744 MN
Rq  =-5.01977530 MN mm
Rc  =+0.26468013 MN mm
R20 =-0.07248958 MN mm
R02 =+0.04931505 MN mm
```

相对 `2e-4`：

```text
Delta P = 0.0064219 MN
relative Delta P ≈ 0.017%
```

所以荷载状态量很稳定，但四残量对 coefficient pruning 有可见敏感性。

尝试在增广 near-root 上把 dense N48 coefficient composition 收紧到 `1e-4` 甚至父实现级 `~7e-7` 时，单次 current-map evaluation 因新增 `p20/p02` 后高阶 dense coefficient support 显著膨胀，在当前执行窗口内超过 90 s，无法完成严格同表达式 fixed-D certificate。

因此 fail-fast：

```text
FIXED_D050_AUGMENTED_NEAR_EQUILIBRIUM = FOUND
STRICT_FIXED_D050_CERTIFICATE          = NOT_REACHED
FAILURE_IDENTITY                       = REPRESENTATION/RUNTIME GATE
PHYSICAL/DOMAIN ILLEGALITY             = NO EVIDENCE
Pu                                      = NOT SOLVED
D CONTINUATION                          = BLOCKED
```

这与此前 `c` 扩展时暴露的 naive expand-then-compose 问题同类：不是理论积分必须改成数值积分，而是当前 dense coefficient implementation 不适合继续强行扩维。

## 10. 直接理论结论

本轮已经比 21:44 更进一步证明：

1. `p20,p02` 不是形式上的“多余自由度”；它们一旦释放，就真实把 `R20/R02` 从几十 MN mm 消到接近零；
2. 同时 q 与 c 大幅重新调整，说明屈曲后膜力重分布和面外幅值/加载边 warp 是强耦合的；
3. 当前 Z6 的 postbuckling 问题确实不能由旧 `D+q+c` 路径代表；
4. **积分形式不需要改变。** General D15 仍然成立；下一障碍只是要把增广系统的 residual/Jacobian 做成 directional moment-first contraction，而不是每次完整展开高阶应力 tensor。

## 11. 唯一下一执行

在继续 D 或 Pu 前，只允许：

```text
DIRECTIONAL_MOMENT_FIRST_AUGMENTED_MEMBRANE_EVALUATOR_AT_D050
```

要求在同一 `[q,c,p20,p02]` 系统、同一 R10/N48/CH/D15 下，直接构造 `P,Rq,Rc,R20,R02` 与 flat Jacobian 的 directional contractions，复核当前 near-root 并把 coefficient-pruning/runtime gate 降下来。

在这个 fixed-D certificate 通过前，不继续 Z6 Pu。
