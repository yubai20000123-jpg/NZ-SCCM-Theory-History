# NZ-SCCM — Z6 D=.55 增广 FvK connected continuation 执行报告

**Timestamp:** 2026-08-15 23:06 +08:00  
**Identity:** continuation attempt / no Pu / fail-fast representation gate

## 1. 任务

从 22:35 已认证的 D=.50 directional moment-first 状态出发，执行下一步 D=.55 connected checkpoint：

```text
Rq=0
Rc=0
R20=0
R02=0
unknowns q,c,p20,p02
```

保持 one complete halfwave、Nguyen second order、R10/N48/Cayley-Hamilton、General D15 和 local steel current operator 不变。

## 2. 起点

D=.50 certificate：

```text
q=.008003063422252722
c=-.07766034129851779
p20=-.06065823792663306
p02=.16525678113314005
P=37.6899290259 MN
```

## 3. 直接把 D 提到 .55、坐标先不变

在 concrete pruning tol=5e-4 下，同一 directional evaluator 能完成一次求值：

```text
P=42.98592845 MN
Pc=25.14107040 MN
Ps=17.84485801 MN
Rq=-2299.87338768 MN mm
Rc=-35.63554892 MN mm
R20=+2.83556533 MN mm
R02=-6.46484800 MN mm
runtime≈32.11 s
```

残量分解：

```text
Rqc=-4386.37308    Rqs=+2086.49969
Rcc=-44.76119      Rcs=+9.12564
R20c=-1.15705      R20s=+3.99262
R02c=-19.02892     R02s=+12.56408  MN mm
```

normalized residual / internal cancellation：

```text
Rq 35.53%
Rc 66.13%
R20 55.06%
R02 20.46%
```

所以 D=.50 坐标不能直接作为 D=.55 平衡点，必须更新 q,c,p20,p02。

## 4. 用已保存 D=.50 4x4 Jacobian 作 predictor

这里只把 21:53 保存的 Jacobian 当 continuation preconditioner，不把它当新理论 Jacobian。由 D=.55 起始残量得到预测修正：

```text
dq   = +.001373733217
dc   = -.034825120945
dp20 = -.034121403685
dp02 = +.080270687466
```

预测坐标：

```text
q=.009376796639
c=-.112485462244
p20=-.094779641612
p02=.245527468599
```

独立非积分材料域审计给出 principal normalized lambda 约：

```text
[-.90064,+.22428]
```

仍在 inherited N48 interval `[-1.75,+.45]` 内。

但是把该 predictor 带回同一 dense-buildS directional evaluator 后，单次求值在 180 s 执行窗口内未完成。因而没有为该 predictor 声称任何 P 或残量。

## 5. 排除“只是 D=.55 步子太大”

内部增加一个 D=.51 bridge 诊断，不作为正式新路径结果。

直接使用 D=.50 certificate 坐标，在 D=.51、tol=5e-4 下：

```text
P=38.7451335 MN
Rq=-449.371183 MN mm
Rc=-5.93723357 MN mm
R20=+.329748708 MN mm
R02=-1.07098535 MN mm
runtime≈22.11 s
```

用同一存储 Jacobian 得到很小的 predictor：

```text
dq=+.000282665117
dc=-.007462944185
dp20=-.007036942324
dp02=+.016852248138
```

预测状态：

```text
q=.008285728539
c=-.085123285484
p20=-.067695180251
p02=.182109029271
```

非积分材料域仍合法：

```text
lambda≈[-.83626,+.19300]
```

但该小修正状态在同一 dense `buildS` evaluator 中仍超过 180 s 未完成。

因此当前问题不是单纯 D=.50→.55 步长过大。

## 6. 新诊断

22:35 directional moment-first 已经避免 materializing 完整 `Sxx/Syy` 和每一个 stress×virtual-strain product，但其内部仍然调用 inherited：

```text
A,B = buildS(K1,K2,tol)
```

也就是说高阶 R10/N48/Cayley-Hamilton material pair 本身仍以 dense 3D coefficient boxes 生成。

本轮证明：

```text
D=.50 certificate                         PASS
D=.55 at old coordinates                  evaluable
D=.55 connected predictor                 dense-buildS runtime failure
D=.51 small connected predictor           dense-buildS runtime failure
material-domain illegality                NO
formal General-D15 failure                NO
```

因此 22:20/22:35 的 representation diagnosis 进一步收窄为：

```text
remaining bottleneck = dense Cayley-Hamilton A/B pair construction itself
```

而不是 residual contraction。

## 7. Fail-fast 状态

```text
D055_CONNECTED_CHECKPOINT = NOT_REACHED
CORRECTED_Pu = NOT SOLVED
D_CONTINUATION = BLOCKED
FAILURE_IDENTITY = DENSE_CH_PAIR_REPRESENTATION_RUNTIME_GATE
```

没有尝试空间 Gauss/Simpson、material-point grid、cells、out-of-plane multimode 或材料理论替换。

## 8. 唯一下一步

```text
CAYLEY_HAMILTON_MOMENT_RECURSIVE_PAIR_WITHOUT_DENSE_BUILDS_AT_D055
```

下一实现只允许修改高阶材料 pair 的表示/收缩顺序：不先形成完整 dense A/B boxes，而针对 P,Rq,Rc,R20,R02 和 flat Jacobian 所需方向直接递推/收缩 moment information。

该实现必须先复现 D=.50 certificate，再重新建立 D=.51→.55 connected checkpoints。