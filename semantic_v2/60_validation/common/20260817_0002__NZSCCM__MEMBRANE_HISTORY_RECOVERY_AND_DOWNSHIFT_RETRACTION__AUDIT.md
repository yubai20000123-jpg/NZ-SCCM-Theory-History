# NZ-SCCM — 膜力重分布历史恢复与近期下降解释撤回审计

**时间：2026-08-17 00:02 +08:00**  
**身份：HISTORY RECOVERY / CORRECTION AUDIT**

## 1. 审计触发

近期 Case21 五项膜内自由凝聚得到 `Pu=320.749185 kN`，并进一步用 direct-R10 数值审计得到 Z6 `Pu~=43.762840 MN`，随后曾把二者共同解释为“膜力重分布系统性降低承载力”。

该解释与仓库中更早、优先级更高且已经明确锁定的经典 FvK/Airy 退化极限相冲突。本审计恢复旧证据并撤回该物理解释。

## 2. 关键历史证据

### 2.1 2026-08-15 23:58：相同错误已经被撤回过

`20260815_2358__NZSCCM__AR2_MEMBRANE_THEORY_CLASSICAL_LIMIT_REOPEN__AUDIT.md` 明确撤回了 `Pu≈40.97 MN` 被解释为“释放 p20,p02 后膜力重分布导致峰值下降约 8%”的说法。

原因：

1. 该值来自空间 Gauss-Legendre 路径，不满足零空间积分正式边界；
2. 更根本地，`p20,p02` 只是函数空间 rank completion，并没有由 `FvK compatibility + in-plane equilibrium + boundary conditions` 导出唯一/受约束膜应力场。

锁定结论：

```text
AR2_40.97334_MN = RETRACTED
P20_P02_AS_FINAL_CLASSICAL_MEMBRANE_CLOSURE = UNPROVEN / REOPENED
CLASSICAL_POSTBUCKLING_LIMIT = MANDATORY BEFORE NEXT Pu
```

### 2.2 2026-08-16 00:07：经典膜力重分布是正后屈曲刚度

经典 one-halfwave FvK/Airy 精确推导给出

\[
S=A^2+2A_0A,
\]

\[
N=N_{cr}\frac{A}{A+A_0}+
\frac{EtS}{16}\left(\beta^2+\frac{\alpha^4}{\beta^2}\right).
\]

第二项为严格非负的膜效应后屈曲承载贡献。square halfwave、perfect plate 下

\[
\frac{\sigma}{\sigma_{cr}}
=1+\frac{3(1-\nu^2)}8\left(\frac At\right)^2.
\]

因此 `dN/dA>0`。仓库锁定：

```text
POSITIVE_MEMBRANE_POSTBUCKLING_BRANCH = RECOVERED
EDGEWARD_AXIAL_STRESS_REDISTRIBUTION = RECOVERED
p20,p02 AS TWO INDEPENDENT FREE MEMBRANE COORDINATES = RETIRED
```

### 2.3 2026-08-16 00:16：Z6 实际边界下膜效应符号仍锁定为正

Zhou/Z6 mixed in-plane boundary gate 明确锁定：

```text
ZHOU_BOUNDARY_CLASSICAL_MEMBRANE_STIFFENING_SIGN = POSITIVE / PASS
compatibility-generated membrane response gives positive postbuckling stiffness
```

所以任何声称 Z6 的“正确膜应力重分布本身导致约 15% 承载力下降”的新实现，都必须先被视为违反经典退化极限的实现异常，而不是新物理结论。

### 2.4 2026-08-16 18:48：Case21 应是小扰动，Z6 应是一阶效应

历史 accepted RC backbone + membrane redistribution delta gate 给出共同几何驱动

\[
M=\frac{\pi^2}{\varepsilon_0}\left(q_0q+\frac12q^2\right).
\]

已冻结参考状态：

```text
Case21: M = 0.02869338081
        (M/4)/D = 0.00858140 = 0.85814%

Z6:     M = 1.69487261562
        (M/4)/D = 0.26727511 = 26.7275%

M_Z6 / M_Case21 = 59.0684
```

因此仓库已有清楚的尺度结论：

- Case21 的膜应力重分布相对旧 Nguyen backbone 应当是小修正；
- Z6 的膜应力重分布应当成为一阶效应，明显改变屈后承载储备；
- 这与“低宽厚比/较厚板影响小，高宽厚比/薄板影响明显”的经典趋势一致。

## 3. 五项基底本身与近期错误的区别

2026-08-16 19:12 的五项基底

```text
u0, u20, u22, v02, v22
```

在线弹性极限下精确凝聚得到

\[
\frac rM=
\left[-\frac{1+\nu}{4},-\frac{1-\nu}{4},\frac14,-\frac{1-\nu}{4},\frac14\right],
\]

并逐项恢复经典 Airy/FvK 应力重分布。因此：

```text
FIVE_TERM_BASIS = NOT RETRACTED
FIVE_TERM_ELASTIC_AIRY_LIMIT = PASS
```

问题出现在后续把五个幅值推广为 current-material 下完全自由的 `Rm=0` 内部坐标后，非线性解可以远离由 compatibility/equilibrium/boundary constraints 规定的经典耦合方向。

Case21 近期错误极限状态就是明显证据：其 `M` 仍仅约 0.03，但求出的 `r22,s02,s22` 已相对线弹性 Airy leading direction 出现大倍数放大甚至符号翻转，从而产生与 18:48 尺度预判完全不相称的 `-12.26%` Pu 变化。

因此当前最合理的错误定位是：

```text
FIVE_TERM_SHAPE_SPACE = RETAIN
UNCONSTRAINED_NONLINEAR_FIVE_COORDINATE_CONDENSATION = REOPEN / NOT ACCEPTED
```

需要恢复的是“compatibility-coupled membrane response”，而不是把五个 harmonic 当作五个可以任意卸载结构的独立 relaxation directions。

## 4. 对近期结果的正式身份修正

```text
Case21 320.749185 kN
= RETRACTED_AS_PHYSICAL_MEMBRANE_Pu
= OVERRELAXED_FIVE_COORDINATE_DIAGNOSTIC_ONLY

Z6 43.762840 MN
= RETRACTED_AS_PHYSICAL_MEMBRANE_Pu
= GAUSS/direct-R10 OVERRELAXED_DIAGNOSTIC_ONLY
```

它们可以保留为实现错误证据，但不得继续用于论证“膜力重分布降低承载力”。

## 5. 恢复后的物理主线

```text
HISTORICAL_ACCEPTED_NGUYEN_BACKBONE
+ COMPATIBILITY / EQUILIBRIUM / BOUNDARY-ADMISSIBLE MEMBRANE REDISTRIBUTION
-> positive classical postbuckling stiffness in elastic degeneration
-> edgeward axial stress redistribution
-> small effect for Case21-scale M
-> first-order / much larger effect for Z6-scale M / high b/t
-> current-material amplitudes only after preserving the above constraints
```

不得通过 R10 调参或试验 Pu 拟合恢复这一趋势。

## 6. 唯一下一门禁

`RECOVER_COMPATIBILITY_COUPLED_CURRENT_MEMBRANE_CLOSURE_FROM_1848_1912_TRANSITION`

只审计 18:48 -> 19:12 -> 22:xx 的理论/实现转换，回答：

1. 五项 elastic Airy coupling 如何在 nonlinear `Rm=0` 实现中被丢失；
2. 哪些关系必须由 compatibility/equilibrium/boundary/external-work 继续约束；
3. 如何在 current material 下保留内部凝聚但禁止非物理 over-relaxation；
4. elastic degeneration 必须严格恢复正后屈曲刚度；
5. Case21 correction 必须与其小 `M` 尺度相称；
6. Z6 correction 应随 large `M` / high b/t 明显增强。

在该门禁通过之前，不再发布新的 membrane-redistributed Pu。
