# NZ-SCCM Case21 零空间解析极限—切线稳定完整计算闭合

**时间：2026-08-12 18:02 +08:00**  
**身份：CURRENT CASE21 FULL CLOSURE RESULT**

本文件是以下两份先后隔离证据的最终闭合记录：

1. 理论先冻结：`current/results/NZ_SCCM_CASE21_ZERO_SPATIAL_ANALYTIC_THEORY_FREEZE_20260812_1802.md`
2. 理论冻结后才读取试验：`current/case21/NZ_SCCM_CASE21_EXPERIMENT_ONLY_SOURCE_20260812_1802.md`

完整 fresh 49×4 材料 coefficient：

`current/case21/NZ_SCCM_CASE21_FRESH_MATERIAL_COEFFICIENTS_20260812_1802.csv`

---

## 1. 隔离状态

```text
HISTORICAL_CASE21_D_Q_P_Pu_ROOT_PATH_USED = NO
HISTORICAL_CASE21_ANALYTIC_RESULT_USED = NO
HISTORICAL_FE_GAUSS_SIMPSON_RESULT_USED = NO
HISTORICAL_MATERIAL_POINT_HISTORY_USED = NO
EXPERIMENT_USED_DURING_SOLVE = NO
EXPERIMENT_USED_FOR_ROOT_SELECTION = NO
EXPERIMENT_USED_FOR_PARAMETER_TUNING = NO
FORMAL_SPATIAL_SAMPLING = 0
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_SPATIAL_SUBDOMAINS = 1
```

---

## 2. 理论冻结结果

当前 general-D15 主平衡支的首个 `+ -> -` 荷载极大值为

\[
\boxed{D_u=0.7822850963110681},
\]

\[
\boxed{q_u=0.0017707520964949533},
\]

\[
\boxed{A_u=2.160317557723843\ \mathrm{mm}},
\]

\[
\boxed{P_u^{theory}=365.580427565\ \mathrm{kN}}.
\]

荷载分解：

\[
\boxed{P_c=336.968777333\ \mathrm{kN}},
\qquad
\boxed{P_s=28.611650232\ \mathrm{kN}}.
\]

平衡与极限残量：

\[
\boxed{R_{norm}=1.5607568553\times10^{-6}<10^{-5}},
\]

\[
\boxed{|L_{norm}|=4.0119433896\times10^{-6}<10^{-5}}.
\]

continuous compiler-domain certificate：PASS。

完整连续钢筋场保持弹性：

\[
\max|\varepsilon_s|=0.0016349758512901322<0.00265.
\]

---

## 3. Zhou/Navier current-tangent 控制检查

无载状态解析回归：

\[
\boxed{K_Z(0,0)=823.416805664979\ \mathrm{N/mm}},
\]

与 isotropic square-halfwave 解析退化一致，因此 `ZERO_STATE_TANGENT_REGRESSION = PASS`。

在理论荷载极大值处：

\[
K_{Z,c}^{mat}=765.4620815266977\ \mathrm{N/mm},
\]

\[
K_{Z,c}^{geo}=-719.5765678312335\ \mathrm{N/mm},
\]

\[
K_{Z,s}^{mat}=0,
\]

\[
K_{Z,s}^{geo}=-45.50598684467001\ \mathrm{N/mm},
\]

所以

\[
\boxed{K_Z(D_u,q_u)=+0.37952685079415716\ \mathrm{N/mm}>0}.
\]

首个 tangent-zero 状态在同一 corrected primary branch 上稍后出现：

\[
D_T=0.7824254327857517,
\qquad
q_T=0.0017710077550576295,
\]

且

\[
K_Z\approx-0.0023984931\ \mathrm{N/mm}\approx0.
\]

位置差：

\[
\boxed{D_T-D_u=0.0001403364746835889>10^{-4}}.
\]

因此当前控制分类为

```text
PRELIMIT_TANGENT_STABILITY = PASS
LIMIT_POINT_CONTROL = YES
COUPLED_LIMIT_TANGENT_CONTROL = NO
```

---

## 4. 材料 compiler fidelity record

当前时间戳合同要求报告全 compiler 区间的材料值/一阶切线误差，但没有冻结新的数值 acceptance threshold。本次原样报告：

| primitive | E0 value metric | E1 tangent metric |
|---|---:|---:|
| U | 0.00245360402031 | 0.906633445993 |
| C | 0.0140129840394 | 1.21310364652 |
| T | 0.0895720993894 | 199.312325124 |
| T7 | 0.112736914660 | 64.1319479976 |

本轮不擅自提高 N48 阶数、不修改 R10、不新增阈值。该记录属于 compiler fidelity diagnostic；本次正式结构 tangent gate 由零状态精确回归及同一主支上的 full-field KZ 检查执行。

---

## 5. 理论冻结后读取的实验值

Nguyen 原论文第 5 章 `Experimental and FE Buckling Loads` 表中，Case21 的实验列为

\[
\boxed{P_{exp}=336\ \mathrm{kN}}.
\]

原论文表头将该实验值记为 `Exp. Pcr`。本次只读取实验列；FE 列没有进入求解、选根、定参或最终比较。

同时，原论文 `Data for Concrete Elements` 表确认 Case21：

```text
t = 19.30 mm
f'c = 24.98 MPa
0.85 f'c = 21.23 MPa
p = 0.75 %
epsilon_0 = 2.09e-3
Ec = 20321 MPa
one steel layer
```

故本次理论输入 `fc=21.23 MPa` 与原论文 `0.85 f'c` 列一致。

---

## 6. 唯一允许的最终比较

理论—试验差值：

\[
\Delta P=P_u^{theory}-P_{exp}
=365.580427565-336
=\boxed{+29.580427565\ \mathrm{kN}}.
\]

相对试验误差：

\[
\delta_P=
\frac{P_u^{theory}-P_{exp}}{P_{exp}}\times100\%
\]

\[
=\frac{365.580427565-336}{336}\times100\%
=\boxed{+8.803698680\%}.
\]

理论/试验比：

\[
\boxed{P_u^{theory}/P_{exp}=1.0880369868}.
\]

---

## 7. 19 项合同闭合状态

```text
01 raw Case21 inputs = COMPLETE
02 R10 derived parameters = COMPLETE
03 fresh 49x4 N48 coefficient table = COMPLETE
04 C1/MM material fidelity records = COMPLETE
05 continuous compiler-domain certificate = PASS
06 general-D15 Syy contraction = COMPLETE
07 general-D15 Qq contraction = COMPLETE
08 rebar supported-branch certificate = PASS
09 corrected Rq=0 primary branch Gamma0 = COMPLETE
10 first +->- limit candidate + R_norm/L_norm = PASS
11 zero-state K_Z regression = PASS
12 KZ,c^mat = COMPLETE
13 KZ,c^geo = COMPLETE
14 KZ,s^mat = COMPLETE
15 KZ,s^geo = COMPLETE
16 total K_Z along corrected Gamma0 = COMPLETE
17 pre-limit K_Z=0 ordering proof = PASS / tangent zero occurs after limit
18 final theory result freeze = COMPLETE BEFORE EXPERIMENT
19 experiment-only comparison = COMPLETE AFTER FREEZE
```

因此，按 `NZ_SCCM_CASE21_ZERO_SPATIAL_ANALYTIC_EXECUTION_CONTRACT_20260812_1734.md`：

```text
CASE21_ZERO_SPATIAL_ANALYTIC_CALCULATION = COMPLETE
CALCULATION_CLOSURE = PASS
CONTROL = FIRST +->- LIMIT POINT
THEORY_RESULT = 365.580427565 kN
EXPERIMENT = 336 kN
ERROR = +8.803698680 %
```
