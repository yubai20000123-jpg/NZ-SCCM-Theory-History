# NZ-SCCM — 2026-08-17 批量计算书再次撤回：膜效应隔离与零驱动力退化审计

**Timestamp:** 2026-08-17 19:50 +08:00  
**Identity:** IMPLEMENTATION CORRECTION / CALCULATION-BOOK RETRACTION  
**Parent theory:** `20260817_1824__NZSCCM__ZERO_SPATIAL_DISCRETIZATION_FINITE_CURRENT_TRUE_INFINITE_D15__CANONICAL_LOCK.md`

## 1. 结论

当前 canonical 的“有限 current operator -> 真无限解析表示 -> 2x2 Cayley-Hamilton -> General-D15 exact moments -> 零正式空间离散/数值积分”理论不撤回。

撤回的是 2026-08-17 19:14 生成的 Case01–24 / Z0–Z5 统一计算书及其批量数值解释。该计算书把下列三个效应混在了一起：

1. halfwave / mode identity 改变；
2. Z0–Z5 人为统一 `a/b=2` 的几何改变；
3. membrane-stress redistribution delta。

因此不能从“新 Pu 与旧 Pu 的差”直接解释膜应力重分布影响。

正确的膜效应诊断必须保持：

```text
same geometry
same halfwave
same material operators
same initial imperfection
same steel/web phases
same ultimate-point definition
```

只改变：

```text
MEMBRANE_REDISTRIBUTION = OFF / ON
```

即

\[
\Delta P_{mem}=P_u^{ON}-P_u^{OFF}.
\]

## 2. Swartz24：上一版“大变化”主要是 halfwave 改变，不是膜效应

来源/历史模式映射保持：

```text
Cases1–16: ell=2440 mm, one full-length halfwave
Cases17–24: ell=1220 mm, one representative square halfwave
```

用 direct-current continuum evaluator 作为 AUDIT-ONLY 十进制差分 oracle，在**完全相同的 source-mode geometry** 上分别关闭/打开 Airy 膜应力重分布，得到近似 Pu 差分：

|Case|Pu OFF kN|Pu ON kN|Delta_mem %|
|---:|---:|---:|---:|
|1|645.870|656.218|+1.60|
|2|631.341|641.118|+1.55|
|3|550.953|562.287|+2.06|
|4|587.345|598.845|+1.96|
|5|581.321|594.124|+2.20|
|6|659.638|673.780|+2.14|
|7|654.709|669.788|+2.30|
|8|560.559|573.905|+2.38|
|9|554.201|560.344|+1.11|
|10|572.123|578.072|+1.04|
|11|548.062|556.005|+1.45|
|12|588.216|597.696|+1.61|
|13|596.578|606.308|+1.63|
|14|672.758|683.143|+1.54|
|15|703.550|714.644|+1.58|
|16|623.293|633.489|+1.64|
|17|333.988|330.273|-1.11|
|18|357.699|350.508|-2.01|
|19|357.734|356.747|-0.28|
|20|350.831|351.206|+0.11|
|21|368.705|366.920|-0.48|
|22|370.628|370.323|-0.08|
|23|376.694|376.449|-0.07|
|24|442.752|442.494|-0.06|

Group audit:

```text
Cases1–8:  mean membrane delta ~= +2.02%
Cases9–16: mean membrane delta ~= +1.45%
Cases17–24: mean membrane delta ~= -0.50%
max |delta| ~= 2.38%
```

因此：

```text
SWARTZ24_MEMBRANE_EFFECT = SMALL
```

上一版计算书中 Cases1–16 相对旧表的较大变化，主要来自把旧 `ell=1220` square-halfwave baseline 改成来源一致的 `ell=2440` full-length mode，而不是膜应力重分布。

例如 Case1：旧 square-halfwave current baseline 约 608.9 kN；source-mode full-length、膜关闭约 645.9 kN；再打开膜重分布约 656.2 kN。因此大部分增量属于 mode/halfwave correction，膜增量本身约 +1.6%。

Case21 同参数审计尤其清楚：OFF 约 368.7 kN，ON 约 366.9 kN，变化不足 0.5%，与“Case21 膜重分布只是小扰动”的历史尺度判断一致。

## 3. Z0–Z5：发现比“根连续性”更深的实现错误

Z0–Z5 本轮均人为改为：

```text
a=2b
m*=2
ell=b
q0=A0/b=0.004
SSSS
```

在当前 total-RA Airy-scalar 实现中，膜增量写成

\[
\alpha=\lambda_A M,
\qquad
M={\pi^2\over\varepsilon_0}\left(q_0q+{q^2\over2}\right),
\]

并使用 total generalized residual

\[
R_A(D,q,\alpha)=0.
\]

但对钢-混凝土组合板，这个 total `R_A` 在

\[
q=0,\quad M=0,\quad \alpha=0
\]

时一般并不为零。原因是历史 backbone 的均匀预压状态使用混凝土泊松响应，而连续钢面板采用不同的 `nu_s`; Airy 方向含有非零平均横向应变分量，因此钢面板的预屈曲横向应力会对 `R_A` 做功。

于是求解 `total R_A=0` 会让 Airy 坐标在**没有屈曲几何驱动力**时也去释放钢面板的预屈曲 Poisson mismatch。该自由度已经不再是纯粹的 postbuckling membrane-redistribution delta。

这违反历史已锁定的基本退化：

\[
q\to0 \Rightarrow M\to0 \Rightarrow \Delta\varepsilon_{mem}\to0.
\]

### 3.1 Z5 是决定性反例

在错误 total-RA 解附近：

```text
q ~= 1.3e-4
lambda_A ~= -13
```

即几何膜驱动力极小，而 `lambda_A` 发散以维持一个非零的 `alpha=lambda_A*M`，导致膜变量主要在修正预屈曲钢/混凝土 Poisson mismatch，而不是响应大挠度膜效应。

所以 Z5 的 12.64 MN 一类结果必须撤回；它不是物理膜效应。

## 4. Z0–Z5 同参数 OFF/ON 差分能说明什么

即使暂时用当前 total-RA 实现作错误定位 oracle，在同一 AR2 几何上比较 membrane OFF/ON，也得到以下数量级：

|Case|Pu OFF MN|Pu ON MN|apparent delta|
|---|---:|---:|---:|
|Z0|~32.53|~31.99|~-1.7%|
|Z1|~19.32|~20.02|~+3.6%|
|Z2|~35.69|~36.59|~+2.5%|
|Z3|~38.70|~38.19|~-1.3%|
|Z4|~63.18|~59.42|~-5.9%|
|Z5|~14.32|~12.63|~-11.8% **INVALID: lambda_A~-13 zero-driver degeneration failure**|

这些数值只用于错误定位，不是正式新 Pu。它们表明：

1. Z0–Z3 的同参数膜差分只有约 1–4% 量级；
2. Z4 首次出现约 6% 的清晰一阶变化；
3. Z5 的“大变化”与其低几何 slenderness 不相称，并同时伴随 `lambda_A` 发散，因此是实现异常；
4. 已释放 Z6 的膜驱动尺度远大于 Case21，历史诊断亦一直把 Z6 视为一阶膜效应对象。

这与用户的物理判断一致：**当前样本中真正需要把膜重分布视为明显结构效应的主要是 Z4 和 Z6；其余 Z 系列不应因该模块发生大幅 Pu 改写。**

作为几何参考，外钢面板厚度 `ts=4 mm` 时：

```text
Z0–Z3: b/ts=1500
Z4:    b/ts=2000
Z5:    b/ts=500
Z6:    b/ts=3000
```

Z4/Z6 正好是该族中整体板宽/面板厚度显著较大的对象。

## 5. 正确的下一版计算身份

新的计算书必须明确分成三列/三层，禁止再次混淆：

```text
BASELINE Pu:
  correct geometry + correct halfwave + current material + membrane redistribution OFF

MEMBRANE DELTA:
  same exact object, membrane redistribution ON - OFF

FINAL Pu:
  BASELINE + physically admissible membrane delta
```

膜增量的正式 closure 必须满足：

```text
ZERO_DRIVER_DEGENERATION:
q -> 0 / M -> 0  => membrane correction -> 0
```

且不得允许 Airy internal coordinate 用来重新平衡/释放历史 backbone 的 pre-buckling phase Poisson mismatch。

在该 zero-driver identity 重新闭合前，不再发布 Z0–Z5 membrane-ON production Pu，也不再把 19:14 计算书作为 CURRENT。

## 6. 当前身份

```text
20260817_1914_UNIFIED_CALCULATION_BOOK = RETRACTED
20260817_1946_BATCH = RETRACTED
CASE21/Z6 TRUE-INFINITE D15 THEORY ANCHORS = RETAINED AS PRIOR INDIVIDUAL RELEASES
CANONICAL ZERO-SPATIAL-DISCRETIZATION / TRUE-INFINITE-D15 THEORY = RETAINED
SWARTZ24 MEMBRANE EFFECT = AUDIT-CONFIRMED SMALL
Z0-Z5 TOTAL-RA MEMBRANE CLOSURE = REOPENED DUE ZERO-DRIVER FAILURE
Z4/Z6 = PRIMARY SIGNIFICANT MEMBRANE-EFFECT REGIME
```

Direct-current/Gauss values in this audit are AUDIT-ONLY and do not change the formal counters:

```text
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
N_formal_thickness_quadrature=0
```
