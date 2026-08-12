# NZ-SCCM Case21 试验值独立来源摘录

**时间：2026-08-12 18:02 +08:00**  
**身份：EXPERIMENT-ONLY SOURCE / OPENED AFTER THEORY RESULT FREEZE**

本文件建立于 `current/results/NZ_SCCM_CASE21_ZERO_SPATIAL_ANALYTIC_THEORY_FREEZE_20260812_1802.md` 已写入并冻结理论结果之后。

来源：用户已上传的 Nguyen 博士论文 `Nguyen-011325526.pdf`，第 5 章，Table 5.1 `Data for Concrete Elements` 与随后 `Experimental and FE Buckling Loads` 表。

只摘录与 Case21 原始输入核对和最终实验比较直接相关的**实验/试件数据**，不摘录、不使用 FE 计算列，也不读取任何其他历史理论结果。

Case21 的试件数据在 `Data for Concrete Elements` 中为：

```text
thickness t = 19.30 mm
f'c = 24.98 MPa
0.85 f'c = 21.23 MPa
hr = 0.00 mm
nominal total steel ratio p = 0.75 %
epsilon_0 = 2.09e-3
initial modulus Ec = 20321 MPa
number of steel layers = 1
```

这说明当前原始输入冻结表采用的混凝土强度 `fc = 21.23 MPa` 对应原表中的 `0.85 f'c`，并非误读 `f'c=24.98 MPa`。

在 `Experimental and FE Buckling Loads` 表中，Case21 的实验列为：

\[
\boxed{P_{exp}=336\ \mathrm{kN}}.
\]

本文件故意不记录该表的 FE 列数值。

```text
THEORY_RESULT_ALREADY_FROZEN_BEFORE_THIS_FILE = YES
EXPERIMENT_USED_DURING_THEORY_SOLVE = NO
FE_COLUMN_USED = NO
HISTORICAL_ANALYTIC_RESULT_USED = NO
```