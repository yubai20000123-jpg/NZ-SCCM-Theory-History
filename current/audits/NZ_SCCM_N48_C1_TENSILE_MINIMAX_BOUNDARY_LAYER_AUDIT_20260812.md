# NZ-SCCM N48-C1 拉伸边界层最小极大修复审计

**日期：2026-08-12**  
**身份：COMPILER-LAYER DIAGNOSTIC / NEAR-ZERO VALUE GATE**  
**边界：R10 不动；不增加材料机制；不提高阶次；不重新计算 Swartz24 Pu；不使用试验值生成系数。**

## 1. 本轮只解决什么

上一轮 N48-C1 已守住 R10 的函数值/一阶切线锚点，并通过 Zhou/Navier 切线稳定门；剩余问题集中在 R10 的极窄拉伸边界层。

用 R10 自己的平滑尺度定义边界层：

\[
\boxed{\mathcal B_\eta=\{\lambda\ge0:\ 0\le t(\lambda)=\Pi_\eta(\lambda)\le\eta\}}
\]

令 \(\lambda_\eta>0\) 满足 \(\Pi_\eta(\lambda_\eta)=\eta\)。

24块板中，\(\lambda_\eta\in[0.0034231,0.0034258]\)，约为 \(3.42\times10^{-3}\)。

## 2. 哪个 primitive 真正需要继续改

在上述极窄边界层内，N48-C1 对 U、C、T^7 已经显著优于旧 direct N48；剩余控制项是 T。因此只改 T 的 coefficient-generation objective：

```text
U   = N48-C1
C   = N48-C1
T^7 = N48-C1
T   = N48-C1 + constrained minimax
```

## 3. T 分支的最小修改

\[
T_{48}^{C1-MM}(\lambda)=\sum_{n=0}^{48}a_n^{(T,MM)}\mathcal C_n(\xi),
\qquad \xi=\frac{\lambda-\lambda_c}{\lambda_h}.
\]

系数只由材料函数本身确定：

\[
\boxed{\min_{\mathbf a}\|V(\lambda)\mathbf a-T_{R10}(\lambda)\|_{L^\infty([\lambda_a,\lambda_b])}}
\]

并严格满足

\[
\boxed{T_{48}^{C1-MM}(0)=0,\qquad (T_{48}^{C1-MM})'(0)=0.}
\]

这是标准 C1 约束最小极大问题；可由 Remez/exchange 或等价线性规划求系数。用于求系数和审计的材料坐标不属于空间离散，最终仍只有一个 48 阶 Chebyshev 多项式。

## 4. 为什么不把四个 primitive 全部改成 minimax

如果 U、C、T、T^7 全部改为 minimax，冻结24个状态上的 Zhou 切线门会比 N48-C1 明显退化。只改 T 时，Zhou 门基本保持 N48-C1 的水平。因此这是最小改动。

## 5. 值函数结果

### 5.1 完整 compiler hull

- direct N48：24板 T 最大绝对误差平均 = **0.04981**；
- N48-C1：平均 = **0.12216**；
- N48-C1 + T-minimax：平均 = **0.08195**；最坏 = **0.08812**。

相对 N48-C1，完整 hull 的 T 最大误差平均降低 **32.9%**。

### 5.2 极窄边界层 B_eta

- direct N48：平均 = **0.04460**；
- N48-C1：平均 = **0.04089**；
- N48-C1 + T-minimax：平均 = **0.03728**；最坏 = **0.03795**。

相对 N48-C1，边界层 T 最大误差平均再降低 **8.8%**。

|组|direct N48 B_eta|N48-C1 B_eta|T-minimax B_eta|N48-C1 全域|T-minimax 全域|
|---|---:|---:|---:|---:|---:|
|Case1-8|0.05965|0.04128|0.03749|0.12759|0.08365|
|Case9-16|0.05572|0.04122|0.03758|0.12678|0.08459|
|Case17-24|0.01842|0.04017|0.03677|0.11211|0.07760|

Case17-24 的旧 direct N48 在极窄正拉伸区存在偶然较低值误差，但它不满足 R10 零斜率；本轮验收对象是“严格 C1 后能否继续压低值误差”。

```text
N48_NEAR_ZERO_T_VALUE_GATE = PASS
```

## 6. C1 与系数简单性

- 最大 |T(0)| 残差：**1.42e-14**；
- 最大 |T'(0)| 残差：**5.31e-14**；
- 24板最大 |a_n^(T,MM)|：**0.329**；
- T 系数绝对值和平均：**1.898**。

因此系数仍为 O(1)，没有分谱带拟合出现的巨大系数。

## 7. Cayley-Hamilton / D15 兼容性

最终 T 仍是普通 48 阶 Chebyshev 多项式，因此矩阵提升仍为

\[
\mathcal C_n(\mathbf Y)=A_n\mathbf I+B_n\mathbf Y,
\]

并继续由同一个 D15

\[
\sum c_{ijk}M_iM_jZ_k
\]

闭合。没有 piecewise branch、空间 cell、材料状态点或新矩阵自由度。

```text
CAYLEY_HAMILTON_COMPATIBILITY = PASS
D15_COMPATIBILITY = PASS
FORMAL_SPATIAL_QUADRATURE = 0
```

## 8. Zhou Dx-Dy-H 稳定门

本轮不重新计算24板 Pu，只在冻结状态上做 compiler replacement 的切线审计。

- max |H_candidate/H_R10 - 1| = **0.1386%**；平均 **0.0459%**；
- max |ZhouMargin_candidate/ZhouMargin_R10 - 1| = **0.3872%**；平均 **0.1394%**；
- 加载方向 tangent ratio 最大差 = **0.00689 E0**。

这些数值与上一版 N48-C1 的 PASS 门基本一致。

```text
ZHOU_Dx_Dy_H_GATE = PASS
ZHOU_SINGLE_HALFWAVE_MARGIN_GATE = PASS
```

## 9. 表示能力边界

对 T 做“degree 48 + strict C1”的全域 constrained minimax，实际上就是当前 48 阶空间中的最佳一致逼近审计。最佳找到的全域最大误差平均约为

**0.08195**，

而旧 direct N48 平均约为 **0.04981**。

因此不能再要求“严格守住 R10 零斜率，同时完全恢复旧 direct N48 的全域值误差”。这应记录为表示能力边界，而不是 R10 材料物理失败。

```text
N48_STRICT_C1_FULL_HULL_DIRECT_VALUE_LEVEL = NOT_RECOVERED
N48_STRICT_C1_NEAR_ZERO_VALUE_GATE = PASS
```

## 10. 本轮裁决

```text
R10_MATERIAL_TARGET = FROZEN / UNCHANGED
MATERIAL_COMPILER_ORDER = 48
NEW_MATERIAL_MECHANISM = NO

U_COMPILER = N48-C1
C_COMPILER = N48-C1
T7_COMPILER = N48-C1
T_COMPILER = N48-C1-CONSTRAINED-MINIMAX

STRICT_R10_C1_ANCHORS = PASS
NEAR_ZERO_T_VALUE_GATE = PASS
O1_COEFFICIENT_GATE = PASS
CAYLEY_HAMILTON_GATE = PASS
D15_GATE = PASS
ZHOU_Dx_Dy_H_GATE = PASS

GLOBAL_DIRECT_N48_VALUE_LEVEL = NOT_FULLY_RECOVERED
SWARTZ24_Pu_RECALCULATION = NOT_PERFORMED
STRUCTURAL_CALIBRATION = NO
```

结论：在单一 N48、O(1) 系数、严格 C1、Cayley-Hamilton/D15 兼容以及 Zhou 稳定门不退化的条件下，lambda≈0 的 R10 拉伸边界层值误差可以继续压低；无需动 R10，也无需提高阶次。