# NZ-SCCM N48-C1：R10 函数值—一阶切线锚点约束修复审计

**日期：2026-08-11**  
**身份：CANDIDATE DIAGNOSTIC — NOT PRODUCTION**  
**本轮边界：R10 不动；不增加材料机制；材料解析阶次仍为 \(N_M=48\)；不重新计算或反标 Swartz 24块 \(P_u\)。**

---

## 1. 问题只定位在编译层

P1 已经证明：当前直接 N48 在 R10 的关键材料坐标 \(\lambda=0\) 不能同时保持函数值和一阶切线。

R10 的精确锚点为

\[
U(0)=0,\qquad U'(0)=\kappa,
\]

\[
C(0)=T(0)=T^7(0)=0,
\]

\[
C'(0)=T'(0)=(T^7)'(0)=0.
\]

本轮不修改上述 R10 目标，而只修改 **R10 → N48 系数生成规则**。

---

## 2. 最简单的修复：同一49个材料点 + 两个硬约束

仍写

\[
F_{48}^{C1}(\lambda)
=
\sum_{n=0}^{48} a_n^{(F,C1)}\,\mathcal C_n(\xi),
\qquad
F\in\{U,C,T,T^7\},
\]

\[
\xi=\frac{\lambda-\lambda_c}{\lambda_h}.
\]

材料坐标点完全不变：

\[
\theta_j=\frac{(j+\tfrac12)\pi}{49},
\qquad
\lambda_j=\lambda_c+\lambda_h\cos\theta_j,
\qquad
j=0,\ldots,48.
\]

定义

\[
V_{jn}=\mathcal C_n(\xi_j)=\cos(n\theta_j).
\]

与旧直接插值不同，N48-C1 不要求 49 个点逐点完全插值，而是采用：

\[
\boxed{
\min_{\mathbf a}
\|V\mathbf a-\mathbf f\|_2^2
}
\]

同时强制

\[
\boxed{
C\mathbf a=\mathbf d_F
}
\]

其中

\[
C=
\begin{bmatrix}
\mathcal C_0(\xi_0)&\cdots&\mathcal C_{48}(\xi_0)\\
\lambda_h^{-1}\mathcal C_0'(\xi_0)&\cdots&
\lambda_h^{-1}\mathcal C_{48}'(\xi_0)
\end{bmatrix},
\]

\[
\xi_0=-\frac{\lambda_c}{\lambda_h}.
\]

四个目标向量为

\[
\mathbf d_U=
\begin{bmatrix}
0\\ \kappa
\end{bmatrix},
\]

\[
\boxed{
\mathbf d_C=\mathbf d_T=\mathbf d_{T^7}
=
\begin{bmatrix}
0\\0
\end{bmatrix}.
}
\]

因此函数值锚点和一阶切线锚点是**硬约束**，不是惩罚项，也没有经验权重。

---

## 3. 系数公式仍然非常简单

因为原49点正是 Chebyshev 根点，

\[
H=V^TV
=
\operatorname{diag}
\left(
49,\frac{49}{2},\ldots,\frac{49}{2}
\right).
\]

令旧直接 N48 系数为 \(\mathbf a^{(0)}\)。由于

\[
V\mathbf a^{(0)}=\mathbf f,
\]

N48-C1 可以直接写成最小扰动修正式：

\[
\boxed{
\mathbf a^{C1}
=
\mathbf a^{(0)}
+
H^{-1}C^T
\left(
CH^{-1}C^T
\right)^{-1}
\left(
\mathbf d_F-C\mathbf a^{(0)}
\right).
}
\]

其中

\[
\boxed{
H^{-1}
=
\frac1{49}
\operatorname{diag}(1,2,\ldots,2).
}
\]

所以每个 \(F\) 只需要解一个 **\(2\times2\)** 小矩阵。

这不是新的材料拟合路线；它是：

\[
\boxed{
\text{在原49个材料值受到最小二乘扰动的条件下，强制恢复R10的C1锚点。}
}
\]

没有新增材料参数，没有试验荷载，没有结构 \(P_u\) 进入系数求解。

---

## 4. 为什么本轮不采用其他“看起来更直接”的修复

已经逐项检查：

1. **只改最后两个系数**：可以强制锚点，但会造成明显高阶振荡；
2. **在原 N48 后加线性/低阶修正**：一阶锚点能恢复，但全域函数值被明显拖偏；
3. **\(\lambda^2\) 因子化残差**：锚点天然正确，但在当前宽材料域上值误差明显恶化；
4. **两段可达谱带单独最小二乘**：可达区函数值较好，但谱隙内出现巨大多项式振荡，系数可达到 \(10^5\) 量级，不符合“简单、稳健、可手算审计”的要求；
5. **提高到 N96/N112**：本轮明确不采用，因为当前首先应解决表示规则，而不是用阶次覆盖错误。

因此，本轮选取的 N48-C1 是目前**最小结构改动**方案。

---

## 5. 锚点门：PASS

24块板重新生成 N48-C1 后，四个材料函数的

\[
F_{48}^{C1}(0)-F_{R10}(0)
\]

以及

\[
\left(F_{48}^{C1}\right)'(0)-F_{R10}'(0)
\]

最大绝对残差约为

\[
\boxed{3.0\times10^{-14}}.
\]

因此

```text
R10_VALUE_ANCHOR_GATE     = PASS
R10_FIRST_TANGENT_GATE    = PASS
```

---

## 6. 系数简单性门：PASS

旧直接 N48 在24板中的最大系数绝对值上界约为

\[
0.62990,
\]

N48-C1 为

\[
\boxed{0.62976}.
\]

全部四函数系数绝对值总和的24板平均：

\[
\text{direct N48}\approx 6.272,
\]

\[
\boxed{
\text{N48-C1}\approx 6.360.
}
\]

所以不存在“两谱带无约束拟合”中 \(10^5\sim10^6\) 级系数爆炸。

```text
COEFFICIENT_ORDER = 48
COEFFICIENT_MAGNITUDE_GATE = PASS
```

---

## 7. 周思铭 \(D_x-D_y-H\) 稳定验收门

材料切线仍由同一 current-map 求导，穿厚度后按周思铭/Navier 的正交刚度语言审计：

\[
D_x=D_{11},
\qquad
D_y=D_{22},
\]

\[
D_{\mu,\mathrm{eff}}
=
\frac{D_{12}+D_{21}}2,
\]

\[
\boxed{
H_{\mathrm{eff}}
=
D_{\mu,\mathrm{eff}}+2D_{66}.
}
\]

单代表半波的稳定刚度组合为

\[
\boxed{
N_y^{cr}
=
\frac{
D_x\alpha^4
+
2H_{\mathrm{eff}}\alpha^2\beta^2
+
D_y\beta^4
}{\beta^2}.
}
\]

本轮不是另建周思铭求解器，而是把它作为“修复后的 current tangent 有没有恢复正确稳定刚度构成”的验收门。

### 24板结果

相对于闭式 R10 target：

\[
\max
\left|
\frac{E_{\parallel,t}^{C1}
-
E_{\parallel,t}^{R10}}
{E_0}
\right|
=
\boxed{0.00689}.
\]

即最坏约为

\[
\boxed{0.69\%E_0}.
\]

对 \(H\)：

\[
\boxed{
\max
\left|
\frac{H^{C1}}{H^{R10}}-1
\right|
=
0.1386\%.
}
\]

24板平均绝对偏差：

\[
\boxed{0.0459\%}.
\]

对周思铭式单半波稳定 margin：

\[
\boxed{
\max
\left|
\frac{M_Z^{C1}}{M_Z^{R10}}-1
\right|
=
0.3872\%.
}
\]

平均绝对偏差：

\[
\boxed{0.1394\%}.
\]

而旧直接 N48 在 P1 中曾把 \(H\) 放大到 R10 的约 \(4.7\sim6.8\) 倍。

因此：

```text
ZHOU_Dx_Dy_H_TANGENT_GATE = PASS
ZHOU_SINGLE_HALFWAVE_MARGIN_GATE = PASS
```

三个板组的加载方向切线比进一步说明了这一点：

| 板组 | R10 target \(E_{\parallel,t}/E_0\) | 旧 direct N48 | N48-C1 |
|---|---:|---:|---:|
| Case1–8 | -0.0195 | 0.9928 | -0.0188 |
| Case9–16 | -0.0360 | 0.9362 | -0.0337 |
| Case17–24 | +0.0599 | 0.9659 | +0.0591 |

即 N48-C1 恢复了 R10 本来具有的“峰值附近切线退化”，没有再把它重新拉回近弹性模量。

---

## 8. 但是：全域值函数门暂时不能宣告完全通过

N48-C1 是“最小扰动 + C1硬约束”，所以必然牺牲一部分旧 direct N48 的逐点插值精度。

在各板自己的完整 compiler hull 上，24板平均最大绝对误差为：

| primitive | direct N48 | N48-C1 |
|---|---:|---:|
| \(U\) | 0.00110 | 0.00124 |
| \(C\) | 0.00499 | 0.01252 |
| \(T\) | 0.04979 | 0.12215 |
| \(T^7\) | 0.11599 | 0.11706 |

最坏板的 N48-C1：

\[
|U-U_{R10}|_{\max}\approx0.00189,
\]

\[
|C-C_{R10}|_{\max}\approx0.01343,
\]

\[
|T-T_{R10}|_{\max}\approx0.13006,
\]

\[
|T^7-(T^7)_{R10}|_{\max}\approx0.14151.
\]

这里最明显的是 \(T\) 在 \(\lambda=0\) 附近的极窄 R10 拉伸边界层。

原因已经明确：

- R10 精确要求 \(T'(0)=0\)；
- 但 \(\eta\sim2.5\times10^{-3}\) 使 \(T\) 在很短的 \(\lambda\) 距离内迅速上升；
- 旧 direct N48 实际通过制造 \(T'_{48}(0)\approx9\sim11\) 的假斜率来换取较好的函数值；
- N48-C1 把假斜率取消以后，一个“单一全域48阶多项式”必须付出一定的局部值误差。

所以本轮不能把问题伪装成“已经全部解决”。

---

## 9. 当前正式裁决

\[
\boxed{
\text{N48-C1 是目前最简单、最透明的切线修复候选。}
}
\]

它已经做到：

- R10 不变；
- \(N_M=48\) 不变；
- 同一49个材料坐标不变；
- 最终仍是一组普通48阶 Chebyshev 系数；
- 函数值锚点严格满足；
- 一阶切线锚点严格满足；
- 系数仍为 \(O(1)\)；
- 周思铭 \(D_x-D_y-H\) 稳定刚度恢复到 R10 target 的千分量级。

但是：

\[
\boxed{
\text{GLOBAL VALUE FIDELITY = HOLD}
}
\]

原因不是稳定切线，而是 R10 拉伸零点附近存在非常窄的材料边界层，单一全域 N48 在“精确零斜率 + 原有值精度”之间存在明显竞争。

因此当前治理身份应为：

```text
R10_MATERIAL_TARGET                = FROZEN
N48_ORDER                          = 48
N48_DIRECT_INTERPOLATION           = TANGENT_FAIL
N48_C1_CONSTRAINED_PROJECTION      = PASS_TANGENT_DIAGNOSTIC
R10_VALUE_ANCHOR_GATE              = PASS
R10_FIRST_TANGENT_GATE             = PASS
COEFFICIENT_MAGNITUDE_GATE         = PASS
ZHOU_Dx_Dy_H_GATE                  = PASS
GLOBAL_PRIMITIVE_VALUE_GATE        = HOLD
PRODUCTION_REPLACEMENT             = NOT_YET
SWARTZ24_Pu_RECALCULATION          = NOT_AUTHORIZED_IN_THIS_STEP
```

---

## 10. 下一步边界

下一步不应提高 N，也不应改 R10。

唯一值得继续检查的是：

\[
\boxed{
\text{能否在仍保持单一 N48 / O(1) 系数 / D15 可编译的条件下，专门改善 }\lambda\approx0\text{ 的 R10 拉伸边界层值误差。}
}
\]

如果这一点不能在 N48 内完成，就应明确承认“单一全域 N48 的表示能力边界”，而不是继续靠阶次堆叠掩盖。
