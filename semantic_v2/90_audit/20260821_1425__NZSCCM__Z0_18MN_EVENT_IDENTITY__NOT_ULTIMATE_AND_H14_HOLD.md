# NZ-SCCM — Z0 ~18 MN 事件身份拆解：不是已证明的极限承载力，H14 暂停

时间：2026-08-21 14:25 +08:00
状态：`CURRENT_EVENT_IDENTITY_CORRECTION`
材料：`NC-M6 FROZEN`

## 1. 本文件修正什么

本文件显式 supersede 2026-08-21 13:54 的 `CURRENT_UNIFIED_BRANCH_CONVERGENCE_LEDGER` 中以下判定：

`Pu = first reachable local load maximum on the origin-connected representative branch`。

该规则对当前 Z0/H10 不成立。此前 H6/H8/H10/H12 的约 18–19 MN 数列只能保留为“某一局部平衡事件的有限-N谱位置”，不得再标记为 Z0 极限承载力收敛序列。

因此：

- `18.30~18.95 MN = NOT ACCEPTED AS Pu`；
- `H12->H14 = HOLD`；
- 不再增加 Ritz 阶次，直到该局部事件与真正 ultimate/control event 的关系被澄清。

本修正不修改 NC-M6，不使用 Zhou/FE 值选根或调参。Zhou Z0 = 36.9455 MN 只作为独立物理交叉检查，不能作为求根约束。

## 2. H10 局部事件的代表状态

采用此前同源 H10、40x40x20 AUDIT-ONLY direct-current evaluator，在局部载荷极值附近：

- D = 0.3530719042
- q = 0.0007279545
- eta = 0.0717732883
- P = 18.4255115 MN

其局部 pseudo-arclength 轨迹为：

- D=0.3527463, P=18.41899 MN
- D=0.3529969, P=18.42463 MN
- D=0.3530719, P=18.42551 MN
- D=0.3531159, P=18.42519 MN
- D=0.3531351, P=18.42388 MN
- D=0.3531296, P=18.42160 MN
- D=0.3530633, P=18.41476 MN

因此这里既有很浅的局部 P 极值，也出现 D 的局部回折；它是 equilibrium manifold 的局部 fold/S-shaped branch geometry event，而不能仅凭 `dP/ds=0` 自动称为 ultimate load。

## 3. 轴力分相：没有任何相在 18.4 MN 达到承载极限

同一状态逐相积分得到：

- concrete: Pc = 9.82619 MN
- upper+lower face steel: Pface = 6.63043 MN
- longitudinal web: Pw = 1.96888 MN
- total: P = 18.42551 MN

三相严格相加复现总轴力。

### 3.1 混凝土

NC-M6 状态覆盖：

- CC ≈ 16.83%
- TC ≈ 83.17%
- TT = 0

材料坐标：

- lambda1 ∈ [-0.01995, 0.07583]
- lambda2 ∈ [-0.44596, -0.27706]
- 最大等效压缩坐标约 0.44635
- `c_equiv > 1` 体积分数 = 0

因此压缩支距离 C(c) 的峰值坐标 c=1 尚很远；没有混凝土压缩峰/压碎控制。

物理主应变约：

- p1 ∈ [8.21e-5, 2.60e-4]
- p2 ∈ [-8.28e-4, -5.20e-4]

### 3.2 face steel

- trial von Mises ≈ 105.1~168.9 MPa
- fy = 355 MPa
- yielded fraction = 0

所以 face steel 完全没有屈服。

### 3.3 longitudinal web

- elastic trial sigma_y ≈ -170.6~-107.1 MPa
- fy = 355 MPa
- yielded fraction = 0

所以 web 也完全没有屈服。

结论：18.4 MN 没有对应任何常规材料承载极限事件。

## 4. TC 拉向过渡：存在局部材料切线变化，但规模不足以把它认作轴压极限

NC-M6 拉向 cracking coordinate `xcr ~= 0.0499872`。在 18.4255 MN 状态，TC 区的 r=lambda1/xcr：

- max r ≈ 1.5170
- 全混凝土体积中 TC 且 r>0.7 ≈ 8.71%
- TC 且 r>1.0 ≈ 2.98%
- TC 且 r>1.5 ≈ 0.0053%

即只有极少区域刚碰到 T_NC 的 r=1.5 breakpoint。它可以改变局部切线并参与形成小型膜内 fold，但没有证据表明这等价于整个构件的轴压 ultimate capacity。

## 5. fixed-D 内部 Jacobian：事件确实是膜内平衡近奇异，而不是 q 主导

令 x=[q,eta,all Ritz membrane amplitudes]，固定 D 后的平衡残量为 R(D,x)=0，数值构造 Jx=partial R/partial x。

沿同一 pseudo-arclength 小段：

- P=18.41899 MN: sigma_min(Jx) ≈ 1.69e-3
- P=18.42463 MN: sigma_min(Jx) ≈ 1.01e-3
- P=18.42551 MN: sigma_min(Jx) ≈ 6.95e-4
- 后续局部回折附近: sigma_min(Jx) 最小约 2.16e-4

同时 sigma_max(Jx) 约 2.80e2，条件数可升到约 1.3e6。

所以这里确实存在一个固定-D 内部平衡近奇异/fold。

但是对应最软右奇异向量中：

- q 分量约 1.47e-5
- eta 分量约 2.19e-5

几乎为零；主导项是 Ritz 面内 b_(m,n) 模态，例如 b(4,4)、b(3,3)、b(4,3)、b(2,2)、b(5,4) 等。

按 harmonic ring 的奇异向量能量：

- ring1 ≈ 7.23%
- ring2 ≈ 13.38%
- ring3 ≈ 22.19%
- ring4 ≈ 35.68%
- ring5 ≈ 21.52%

因此该事件的数学身份非常明确：

`HIGH-ORDER IN-PLANE MEMBRANE REDISTRIBUTION FOLD / INTERNAL RITZ EQUILIBRIUM NEAR-SINGULARITY`

而不是一个由 q 主导的面外屈曲幅值极限，也不是材料压碎/钢材屈服极限。

## 6. 最关键的否决证据：18.4 MN 之后仍有更高荷载平衡状态

从 H10 局部状态继续对同一 frozen equations 做 fixed-D continuation，在局部多根/回折区之后可以恢复到严格残量的更高荷载平衡状态。例如：

- D=0.359: P≈18.5735 MN, max|R|≈8.7e-13
- D=0.369: P≈18.9521 MN, max|R|≈4.5e-13
- D=0.379: P≈19.0946 MN, max|R|≈4.1e-14
- D=0.399: P≈19.3851 MN, max|R|≈3.7e-13
- D=0.401: P≈19.4224 MN, max|R|≈8.4e-15

所以 18.4255 MN 不是方程意义上的 terminal equilibrium capacity。

在 D=0.401、P≈19.4224 MN 时仍然：

- concrete c_equiv,max≈0.607 < 1；
- face steel 未屈服，VM max≈237 MPa<355 MPa；
- web 未屈服，trial |sigma_y|max≈237 MPa<355 MPa。

说明越过 18.4 MN 后体系仍能继续承担更高轴力，而没有触发材料容量终止。

注意：0.353~0.359 附近存在多根和 fixed-D branch switching，因此本文件不把每一个小波动的精确位置升级为物理事件；只使用两个稳健事实：

1. 18.4 MN 附近是高阶面内 Ritz 平衡 fold/近奇异；
2. 更高荷载的严格平衡状态存在。

## 7. 对“极限承载力”定义的修正

撤销：

`Pu = origin-connected path 上第一个局部 P 极值`。

新的最低要求是：一个候选 Pu 必须具有明确的控制身份，例如：

- 无法继续承载的 terminal/global load maximum；或
- 在实际控制条件下可证明不可通过的结构稳定性丧失；或
- 明确的材料容量控制；或
- 与完整同源 tangent/bordered stability criterion 一致的先行失稳事件。

仅有 reduced-coordinate/fixed-D fold 或局部 P wiggle 不够。

在 source-consistent non-major-symmetric tangent 下，不允许用人为对称化 Hessian/energy minimum 给该事件补一个虚假的稳定性身份。

## 8. 当前裁决

- `Z0_18MN_EVENT = IN_PLANE_RITZ_MEMBRANE_FOLD`
- `Z0_18MN_EVENT_IS_ULTIMATE = NO / NOT ESTABLISHED`
- `18MN_AS_Pu = SUPERSEDED`
- `H6/H8/H10/H12_18MN_SEQUENCE = LOCAL_EVENT_SPECTRAL_SEQUENCE_ONLY`
- `H14 = HOLD`
- `NC_M6 = FROZEN`
- `M7 = PROHIBITED`

## 9. 唯一下一物理任务

不增加 Ritz 阶次。继续在已存在的 H10/H12 空间内：

1. 用 pseudo-arclength 穿过所有局部 fold；
2. 对每个候选控制事件同步记录 P、D、q、phase loads、material state、representative tangent、J_perp；
3. 找到真正 terminal/global controlling event，并解释其力学身份；
4. 只有 physical Pu identity 恢复以后，才重新讨论 Ritz 截断误差。

下一数学任务不是 H14，而是把已经验证有效的 tail-residual relation / bordered correction 发展成 a-posteriori Ritz truncation error certificate，使 Ritz 阶次最终可以在当前 N 上直接停止，而不是靠无限 consecutive-order brute force。