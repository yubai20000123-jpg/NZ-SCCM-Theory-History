# NZ-SCCM M1 structured matrix polynomial 首轮强非线性筛选 R01

**日期：2026-08-10**  
**身份：CURRENT MATERIAL SCREEN / NEGATIVE RESULT**

## 0. 目的

本轮执行 `CONCRETE_NONLINEARITY_GATE` 下的 Candidate M1 首轮筛选。目标不是用结构 Pu 拟合材料，而是检验：

> `强一维 matrix-polynomial 主骨架 + 低阶 invariant interaction correction`

是否能在较宽的普通混凝土强非线性材料域内，以明显低于自由二维 A/B surface 的复杂度捕捉 frozen NC benchmark 的多轴 current response。

本轮只把 frozen Nguyen/Foster NC operator 当作**材料级非线性 oracle / regression benchmark**；它不是最终材料真理。

严格排除：

- Case21 / Swartz24 / UCFT Pu；
- 空间坐标 X,Y,zeta；
- 空间积分；
- 结构状态反标；
- 材料点历史。

---

## 1. 诊断域

归一化原始主应变

\[
e_i=\varepsilon_i/\varepsilon_0
\]

取

\[
(e_1,e_2)\in[-2.0,0.6]^2.
\]

这是 stress-test domain，不是正式材料有效域冻结。

oracle 输出归一化主应力

\[
s_i=\sigma_i/f_c.
\]

---

## 2. M1-R01 表示

采用

\[
\boxed{
s_i\approx p(e_i)+A_c(\mu,r^2)+B_c(\mu,r^2)e_i
}
\]

其中

\[
\mu=(e_1+e_2)/2,
\qquad
r^2=((e_1-e_2)/2)^2.
\]

`p(e)` 是单变量 Chebyshev polynomial，负责吸收强 tension/compression 主形状；`A_c,B_c` 是总阶有限的二维 Chebyshev interaction correction。

本轮固定 `degree(p)=12`，逐步增加 correction total degree `d=4,8,10,12`。所有表示都是材料空间 finite polynomial；若被采用，最终均可通过 Cayley-Hamilton 回到 `A(I1,I2) I + B(I1,I2) X` 并进入 exact moments。

为了避免显式线性相关导致的虚假条件数，先用 pivoted QR 删除 rank-dependent columns，再做最小二乘。训练网格 45×45；独立检验网格 101×101。

---

## 3. 全域结果

误差均为 `sigma/fc` 的绝对误差。

| p degree | correction degree | independent coefficients | condition number | mean abs. error | 95% abs. error | max abs. error |
|---:|---:|---:|---:|---:|---:|---:|
| 12 | 4 | 38 | 1.17e3 | 0.06399 | 0.24467 | 0.58983 |
| 12 | 8 | 94 | 4.28e5 | 0.03808 | 0.15480 | 0.46499 |
| 12 | 10 | 134 | 7.38e6 | 0.03199 | 0.11632 | 0.44044 |
| 12 | 12 | 182 | 1.76e8 | 0.02916 | 0.10869 | 0.41314 |

与此前自由 A/B surface 的诊断相比，M1-R01 **没有出现“一维主骨架使二维 interaction 阶次大幅下降”的预期效果**。

---

## 4. 路径诊断

对 `p=12, d=12`，代表路径误差如下（仍为 `sigma/fc` 绝对误差）：

| material path | mean | 95% | max |
|---|---:|---:|---:|
| `e2=0`, e1∈[-2,0.6] | 0.02879 | 0.09487 | 0.10807 |
| equal biaxial compression `e1=e2∈[-2,0]` | 0.00797 | 0.01999 | 0.05324 |
| equal biaxial tension `e1=e2∈[0,0.6]` | 0.01216 | 0.04217 | 0.05578 |
| TC ratio `e1=-t, e2=0.25t, t∈[0,2]` | 0.09724 | 0.37460 | 0.40472 |

最明显的失败仍在 tension-compression interaction。提高单变量 `p(e)` 阶次对该问题帮助很有限；主要改善仍依赖更高阶二维 interaction。

---

## 5. 正式判定

\[
\boxed{
M1\_R01\_SIMPLE\_ADDITIVE\_STRUCTURED\_POLYNOMIAL = FAIL\_SCREEN
}
\]

这里失败的是**具体 M1-R01 结构**，不是所有 structured analytic material law。

允许结论：

1. 混凝土多轴强非线性不能简单降格为“一条很强的一维曲线 + 很弱的低阶二维修正”；
2. 若继续把所有多轴 interaction 都塞入高阶二维 polynomial，复杂度会重新接近自由 A/B surface，且条件数快速恶化；
3. 因此下一候选不应只是继续提高 M1 correction degree。

---

## 6. 下一候选：M1R rational / algebraic source-shaped material primitives

本轮同时启动的 invariant-coordinate/lifting 分析发现：Case21 `I1` 对厚度坐标 z 是严格 affine，`I2` 对 z 是严格 quadratic。若材料 `A(I1,I2),B(I1,I2)` 采用**低参数有理型**而不是高阶自由 polynomial，则换元 `s=I1` 后，固定 `(u,v)` 的材料 integrand 对 `s` 成为 rational function；这一方向允许先把强非线性材料方向精确解析积分掉。

因此新的优先候选改为：

```text
M1R = source-shaped rational/algebraic scalar material primitives
      + invariant/tensor basis
      + exact invariant-coordinate reduction
```

而不是继续堆高 M1-R01 polynomial degree。

详细数学推导见：

`current/theory/NZ_SCCM_INVARIANT_COORDINATE_LIFT_EXACT_REDUCTION_R01_20260810.md`
