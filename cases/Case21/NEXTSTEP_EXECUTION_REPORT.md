# NZ-SCCM Case21：单完整半波全域解析表示——严格尾项下一步执行报告

日期：2026-08-09

## 1. 本轮执行边界

正式身份继续锁定为：`ONE_CONTINUOUS_COMPLETE_HALFWAVE`。正式空间 sampling=0，quadrature=0，subdomains=1。上一阶段所有 analytic cell / seed partition / NeedSplit / adaptive analytic subdivision 均继续保持撤销状态。本轮没有恢复任何空间分片。

冻结材料仍是 algebraic Foster ordinary-concrete current operator；没有改动材料物理，也没有使用上一轮 338.3175 kN / 342.3332 kN 来构造级数、选阶数或选根。

## 2. 本轮首先实际执行：严格系数尾项是否能直接用单一 l1 范数关闭？

建立了一个三维 Chebyshev coefficient + tail diagnostic。有限系数执行完整 Chebyshev convolution，截掉的全部高阶系数绝对值进入 tail；已存在的输入 tail 再按 Banach algebra 乘法界传播。因此它明确覆盖“高阶×高阶重新回流低阶”的可能性。

在独立状态 D=0.75, q=0.002、Nsp=20 的已有单域字段上，得到：

- Savg finite l1 norm = 2.2363，tail <= 0.005493；
- Dcal finite l1 norm = 5.1468，tail <= 0.013409；
- sigma_y tail <= 0.23138；
- fR tail <= 45.05。

收缩到结构积分后，保守区间约为：

- Pc = 335.141710 ± 5.448 kN；
- Rq = 39678.3 ± 2.7047e6。

这个证书虽然数学方向正确，但极端过松，因此**拒绝作为正式 certificate**。这一负结果非常重要：问题不是“是否可以写一个 Banach 尾项”，而是“不能把所有方向、所有模态和所有非线性依赖压缩成一个标量 l1 半径”。必须保留更多结构信息。

## 3. Scalar material series 本身是否真的不收敛？

不是。对 frozen scalar material functions C,T,U，在覆盖当前测试状态 principal-strain 范围的同一个全局标量区间上，提高 degree 得到最后20项系数绝对和：

| degree | C | T | U |
|---:|---:|---:|---:|
| 1024 | 4.359e-4 | 1.965e-4 | 4.556e-4 |
| 1536 | 9.25e-6 | 5.33e-6 | 9.78e-6 |
| 2048 | 1.85e-7 | 1.38e-7 | 1.99e-7 |

所以 scalar Foster material map 的全域解析逼近并不是根本障碍。真正困难发生在把它复合到三维连续运动学以后，再经过 C/T/U 的乘积、determinant、T^7/T^8 interaction 以及 Rq 中的抵消组合时，如何严格追踪被截断的高阶信息。

## 4. 单完整域 anisotropic p-refinement

为了判断 Rq 的误差是否主要来自厚度方向解析阶数不足，建立了单域各向异性 degree (Na,Nb,Nz)。整个域始终没有切分，也没有空间采样。结果：

| (Na,Nb,Nz) | Pc / kN | Rq |
|---|---:|---:|
| (16,16,24) | 335.162825 | 38597.504 |
| (18,18,28) | 335.144074 | 38951.033 |
| (20,20,28) | 335.143957 | 38971.238 |
| (22,22,30) | 335.144506 | 38628.621 |
| (18,18,32) | 335.131144 | 39505.127 |

独立 numerical audit 仅用于事后判断：Pc≈335.13308 kN，Rq≈38988.58。

结论：各向异性提高阶数确实能使某些 Rq 很接近 audit，但序列非单调，所以**不能按“哪个最接近 audit”选择 degree**。这不能成为正式收敛判据。

## 5. 两条看似自然但本轮已排除的办法

### 5.1 只给 nonlinear interaction 增加 padding

把同一 N=20 的 C/T/U 有限字段嵌入更大的工作 degree，再保留更多 nonlinear products。结果工作 degree 增大后反而出现爆炸。这说明缺失的是真实输入高阶模式；仅给乘法留更多空间，不会自动恢复它们，反而会放大伪高阶反馈。因此该办法废止。

### 5.2 在 truncated spatial algebra 中直接做 radical Newton/Zolotarev-like iteration

尝试直接对正 radicand 求 square root / reciprocal。低阶全域截断会令原本严格正的 radicand 近似场局部失去 positivity，迭代因此发散或产生 NaN。该结果说明：必须先有 validated tail / positivity，或者使用具有独立统一误差定理的 rational functional calculus，不能先在未认证的 truncated field 上强行迭代。

## 6. 新发现：principal spectrum 实际全域分离

在 D=0.75,q=0.002，解析无采样界可得：

- lambda+ roughly in [-0.1051, 0.13584]；
- lambda- roughly in [-0.86569, -0.62473]。

更重要的是，在相当宽的参数盒 D∈[0.5,0.9], q∈[0,0.003] 内，解析下界仍有 delta_min≈0.22599>0。这意味着当前 Case21 root 邻域的两个 principal spectra 并不是挤在一起，而是两个分离的实区间。

这是下一步的重要突破口：此前 scalar material Chebyshev series 被迫覆盖两个谱区间中间一大段实际永远不会访问的空白区，从而浪费了大量 degree。后续应优先研究**对两个分离谱区间有统一严格误差定理的 rational / polynomial functional calculus**，而不是增加空间 cell。

## 7. 当前正式结论

本轮没有发布新的 concrete-only 或 RC root。原因已经明确缩小为：

> 需要一个保留谱分支/方向/阶次结构的全域 coefficient-tail certificate；单一 l1 tail 太松，单纯提高 degree 又缺少可接受的正式选择准则。

当前仍满足：one complete halfwave；formal sampling=0；formal quadrature=0；formal subdomains=1。
