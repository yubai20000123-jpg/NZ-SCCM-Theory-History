# NZ-SCCM — Swartz24 逐板鼓包位置与有效波长证据审计

**Time:** 2026-08-22 17:25 +08:00  
**Status:** `EXECUTED / RAW_SWARTZ_TABLE2_RECOVERED / BINARY_WAVELENGTH_REJECTED / MATERIAL_FROZEN / 2D_RERUN_PAUSED`

## 0. 本轮问题

本轮不再把 Nguyen 的组级“approximate one half sinusoidal wave / two sinusoidal half waves”机械地翻译成 `ell=2440/1220 mm`。

只回答：

1. Swartz 原始 24 块板逐板报告的鼓包位置/区域是否组内一致；
2. 原始试验证据是否支持每组一个固定波长；
3. 当前显式计算 `ell=1220 mm for all 24` 与原始形态证据是否一致；
4. 哪些逐板数据足以形成波长约束，哪些仍只能给“位置/区域”而不能给精确半波长。

不计算新的 Pu，不修改材料本构，不使用试验荷载反标波长。

---

## 1. 必须区分三个量

### 1.1 Swartz 原始 `buckling location`

Swartz Table 2 给的是屈曲鼓包出现的**位置/区域**，例如：

- `Middle`；
- `Top 1/3`；
- `Top 1/2 and bottom 1/2`；
- `Top 2/3 and bottom 1/3 of plate`。

这是真实试验形态证据。

### 1.2 理想化正弦半波长度 `ell_mode`

对于严格全板 Navier 单项：

\[
w=A\sin\frac{m\pi y}{a}\sin\frac{\pi x}{b},
\qquad
\ell_{mode}=\frac{a}{m},\quad m\in\mathbb N^+.
\]

它只允许 `2440, 1220, 813.3, 610, ... mm` 这样的离散值。

### 1.3 项目后续可能采用的代表有效波长 `ell_eff`

如果原始鼓包并非严格全板单项正弦，则项目需要另行定义一个满足边界和显式可积要求的代表波形参数。它不能被 Swartz 的 `buckling location` 自动等同。

因此本轮使用：

```text
BUCKLING_LOCATION != EXACT_SINUSOIDAL_HALFWAVE_LENGTH
ZONE_LENGTH_SURROGATE != PRODUCTION_ELL_EFF
```

---

## 2. 原始 Swartz 证据的总说明

Swartz 原文说明：

- 一部分板的鼓包类似 Plate 21；
- 一般而言，板更倾向于像 Plate 6 那样“bulge in one panel”；
- 所有板均以双向曲率鼓包方式屈曲；
- Table 2 逐板给出 `locations of bulges`。

因此，原始试验从一开始就不是“24 块板只有两个严格统一波长”的资料体系。

Nguyen 第5章则把同一批板的 FE 结果总结为更平滑的组级类别：

```text
Panels 1-8   : approximate one half sinusoidal wave
Panels 9-16  : approximate one half sinusoidal wave
Panels 17-24 : two sinusoidal half waves
```

这两层证据不能互换：前者是逐板试验位置/区域，后者是 Nguyen FE 的组级理想化模态。

---

## 3. 24 块板逐板原始鼓包位置

板长统一为

\[
a=2440\ \mathrm{mm}.
\]

下表中的 `zone-length surrogate` 只是在原始文字包含明确分数时，把该区域占全长的分数乘以 2440 mm，用来显示形态尺度；**它不是已经确定的正弦半波长。** `Middle` 没有给长度，因此严格记为 `UNRESOLVED`。

|Case|Group|Swartz Table2 buckling location|raw morphology|zone fraction(s)|zone-length surrogate / mm|exact ell from source?|
|---:|---|---|---|---|---:|---|
|1|1–8|Top 2/3 and bottom 1/3 of plate|multiple unequal zones|2/3 + 1/3|1626.7 + 813.3|NO|
|2|1–8|Middle|central zone|unknown|UNRESOLVED|NO|
|3|1–8|Middle|central zone|unknown|UNRESOLVED|NO|
|4|1–8|Bottom 1/3|bottom-localized zone|1/3|813.3|NO|
|5|1–8|Top 2/3 and bottom 1/3|multiple unequal zones|2/3 + 1/3|1626.7 + 813.3|NO|
|6|1–8|Top 1/3|top-localized zone|1/3|813.3|NO|
|7|1–8|Middle|central zone|unknown|UNRESOLVED|NO|
|8|1–8|Top 1/4|top-localized zone|1/4|610.0|NO|
|9|9–16|Top 1/3|top-localized zone|1/3|813.3|NO|
|10|9–16|Middle|central zone|unknown|UNRESOLVED|NO|
|11|9–16|Middle|central zone|unknown|UNRESOLVED|NO|
|12|9–16|Middle|central zone|unknown|UNRESOLVED|NO|
|13|9–16|Middle|central zone|unknown|UNRESOLVED|NO|
|14|9–16|Middle|central zone|unknown|UNRESOLVED|NO|
|15|9–16|Middle|central zone|unknown|UNRESOLVED|NO|
|16|9–16|Middle|central zone|unknown|UNRESOLVED|NO|
|17|17–24|Middle 1/3 and bottom 1/3|multiple zones|1/3 + 1/3|813.3 + 813.3|NO|
|18|17–24|Top 2/3|large top zone|2/3|1626.7|NO|
|19|17–24|Top 1/2 and bottom 1/2|two equal gross zones|1/2 + 1/2|1220 + 1220|NO; strong gross support|
|20|17–24|Middle 1/3 and bottom 1/3|multiple zones|1/3 + 1/3|813.3 + 813.3|NO|
|21|17–24|Top 1/2 and bottom 1/2|two equal gross zones|1/2 + 1/2|1220 + 1220|NO; strongest two-wave support|
|22|17–24|Top 1/3|top-localized zone|1/3|813.3|NO|
|23|17–24|Top 1/3|top-localized zone|1/3|813.3|NO|
|24|17–24|Middle|central zone|unknown|UNRESOLVED|NO|

The explicit fractional values are therefore **region-scale evidence**, not a license to set `ell_eff` equal to those numbers without a waveform definition.

---

## 4. Group-internal consistency

### Group 1 — Cases 1–8

Observed location classes:

- multiple unequal zones: Cases 1, 5;
- middle: Cases 2, 3, 7;
- bottom 1/3: Case 4;
- top 1/3: Case 6;
- top 1/4: Case 8.

Decision:

```text
GROUP1_RAW_EXPERIMENTAL_MORPHOLOGY = HETEROGENEOUS
GROUP1_SINGLE_FIXED_EXPERIMENTAL_WAVELENGTH = NOT_SUPPORTED
```

This directly contradicts any per-panel statement `Cases1-8 ell=2440 mm`.

### Group 2 — Cases 9–16

Observed location classes:

- top 1/3: Case 9;
- middle: Cases 10–16.

Decision:

```text
GROUP2_RAW_LOCATION_PATTERN = RELATIVELY_CONSISTENT / MOSTLY_MIDDLE
GROUP2_EXACT_COMMON_WAVELENGTH = STILL_NOT_SOURCE_CLOSED
```

This is the most internally consistent group in terms of reported peak-zone location, but `Middle` does not specify a numerical half-wave length.

### Group 3 — Cases 17–24

Observed location classes:

- multiple 1/3 zones: Cases 17, 20;
- top 2/3: Case 18;
- two equal half-length zones: Cases 19, 21;
- top 1/3: Cases 22, 23;
- middle: Case 24.

Decision:

```text
GROUP3_RAW_EXPERIMENTAL_MORPHOLOGY = HETEROGENEOUS / OFTEN MULTI-ZONE
GROUP3_NGUYEN_TWO_HALFWAVE = GROUP_LEVEL_FE_IDEALIZATION
```

Panel 21 is special: Nguyen explicitly states its FE shape is similar to Swartz's experimental record. Therefore Panel21 has the strongest source chain for a gross two-halfwave interpretation.

---

## 5. The user's 1220–2440 observation is source-supported in scale, but must be named correctly

Cases 1 and 5 have a reported dominant `Top 2/3` region. Case18 also has `Top 2/3`.

As a region-length surrogate:

\[
L_{2/3}=\frac{2}{3}a=\frac{2}{3}(2440)=1626.7\ \mathrm{mm},
\]

which satisfies

\[
1220 < 1626.7 < 2440.
\]

So the raw test evidence does contain a characteristic spatial scale between the two binary endpoints.

But the correct statement is:

\[
\boxed{L_{zone}=1626.7\ \mathrm{mm}\ \text{(source-reported region-scale surrogate)}}
\]

not

\[
\boxed{\ell_{sin}=1626.7\ \mathrm{mm}\ \text{(not source proven)}}.
\]

This distinction prevents a new hidden backfit.

---

## 6. Comparison with current explicit waveform assumption

Current explicit frontend, when using initial symmetric stiffness, selects `m=2` for every Swartz plate, therefore

\[
\ell_{calc}=a/2=1220\ \mathrm{mm}\quad\text{for all 24}.
\]

Against raw experimental morphology:

- Cases 19 and 21 have the strongest gross compatibility with two half-length zones;
- Cases 1, 5 and 18 directly show a dominant 2/3-length region, incompatible with a universal 1220-mm interpretation;
- Cases 17 and 20 contain multiple shorter one-third regions;
- all `Middle` cases do **not** provide enough source information to assign a numerical `ell_exp`; they must remain unresolved rather than being silently called 2440 or 1220.

Therefore:

```text
CURRENT_M2_ALL24_EXACT_WAVELENGTH_MATCH_TO_RAW_EXPERIMENT = NOT_SUPPORTED
```

The earlier binary diagnostic `1-16 -> 2440 / 17-24 -> 1220` is also not supported as a per-panel experimental wavelength assignment.

---

## 7. Nguyen group mode versus Swartz raw experiment

The correct hierarchy is now:

```text
LEVEL A: Swartz Table2 = per-panel experimental bulge location/zone evidence
LEVEL B: Nguyen Ch5 = group-level FE idealized mode class
LEVEL C: Current explicit = initial-stiffness m=2 prediction for all 24
```

Thus:

- `Nguyen m≈1 for 1–16` may be used to say his FE develops a broad one-halfwave-like group mode;
- it may **not** be rewritten as `experimental ell=2440 mm for every panel 1–16`;
- `Nguyen m=2 for 17–24` is group FE evidence;
- Panel21 has explicit text linking Nguyen FE shape to experiment;
- exact per-panel experimental sinusoidal wavelength is not source-closed for most panels.

---

## 8. Consequence for the next explicit calculation

No new 2D Pu calculation is executed in this audit.

Reason: the structural waveform parameter must first be defined without confusing a reported bulge zone with an exact sine wavelength.

Two admissible next mathematical candidates remain:

### Candidate W1 — one continuous local representative halfwave with a continuous `ell_eff`

This keeps the current low-dimensional explicit solver closest to its present form, but must derive a boundary-compatible embedding of the local halfwave into the full simply-supported plate. A free `sin(pi y/ell_eff)` written over the whole 2440-mm domain is **not** boundary-compatible unless `a/ell_eff` is integer.

### Candidate W2 — finite global Navier mixture

For example,

\[
w(x,y)=A\sin\frac{\pi x}{b}
\left[c_1\sin\frac{\pi y}{a}+c_2\sin\frac{2\pi y}{a}\right],
\]

which automatically satisfies all four simple supports and can shift peak locations and produce unequal lobes without declaring a noninteger global Navier index.

The coefficient ratio must ultimately come from tangent stability / current structural equations, not from choosing the value that best matches `Pf`.

No candidate is frozen in this audit.

---

## 9. Decision

```text
RAW_SWARTZ_TABLE2_PER_PANEL_BULGE_LOCATION = RECOVERED
EXACT_PER_PANEL_EXPERIMENTAL_SINE_WAVELENGTH = NOT_SOURCE_CLOSED
BINARY_ELL_1220_2440_AS_EXPERIMENTAL_INPUT = REJECTED
GROUP1_RAW_MORPHOLOGY = HETEROGENEOUS
GROUP2_RAW_MORPHOLOGY = RELATIVELY_CONSISTENT_MOSTLY_MIDDLE
GROUP3_RAW_MORPHOLOGY = HETEROGENEOUS_MULTI_ZONE
NGUYEN_1_16_M1_17_24_M2 = FE_GROUP_IDEALIZATION_ONLY
PANEL21_TWO_HALFWAVE_EXPERIMENT_LINK = STRONGEST_SOURCE_CASE
CURRENT_M2_ALL24_EXPERIMENTAL_WAVEFORM_VALIDATION = FAIL
WAVEFORM_CONDITIONED_2D_RERUN = PAUSED
MATERIAL_MODEL_CHANGED = FALSE
STRUCTURAL_BACKBONE_CHANGED = FALSE
NEXT_RC_TASK = FINITE_BOUNDARY_COMPATIBLE_WAVEFORM_PARAMETERIZATION_FROM_RAW_LOCATION_EVIDENCE
```

This supersedes any wording that treats the earlier `ell=2440/1220` endpoint run as a real observed-wavelength calculation. It remains only an endpoint sensitivity calculation.
