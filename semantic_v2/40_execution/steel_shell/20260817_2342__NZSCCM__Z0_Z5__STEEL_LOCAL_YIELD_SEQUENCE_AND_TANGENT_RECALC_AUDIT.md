# NZ-SCCM Z0–Z5 钢壳局部屈服先后顺序、鼓波中心—侧部切线差异与重新计算审计

**Date:** 2026-08-17 23:42 +08:00  
**Object:** Z0–Z5 modified AR2/SSSS, one continuous representative halfwave  
**Trigger:** 审计“鼓波中间先进入屈服/低切线区，而鼓波两侧仍保持较高弹性切线”的空间先后顺序，以及这一点是否被当前钢壳求解正确体现。  
**Status:** `LOCAL_YIELD_FRONT + LOCAL_TANGENT + CURRENT-PATH RECALCULATION AUDIT`  
**Calibration:** NO  
**Comparator used in solve:** NO

---

## 0. 先给结论

本轮确认了用户指出的力学现象，而且比此前的“最大 VM/fy > 1”检查更具体：

1. 对 Z0–Z4，压缩侧钢面板的鼓波中心/中心附近首先达到屈服，随后屈服前沿由中心向两侧扩展；在当前极限点，边缘通常仍为弹性。Z5 最接近整体压缩主导，边缘在极限点前刚刚进入屈服。
2. 因此不允许把整张钢面板在某一个 `max VM/fy > 1` 事件后整体设为 `E_t=0`，也不允许整张钢板继续统一使用 `E_s`。正确对象是连续位置相关的 `C_t^s(X,Y,z)`。
3. 此前的 direct-current audit 虽然没有把这张空间切线图输出出来，但其有限差分 residual Jacobian 实际上已经隐式包含了当前 **radial-cap current map** 的局部切线差异。把 radial-cap 的解析局部导数重新积分后，与此前 finite-difference face Jacobian 的最大相对差在六块板中不超过约 `2.2e-3`。
4. 但是更关键的问题是：当前 radial cap 的一致导数本身并不是一个合格的理想 J2 流动切线。在 Z0/Z1/Z2/Z3 的鼓波中心，它甚至给出负的 `C_yyyy/C_yyyy^e`（例如 Z1 约 `-1.10%`）。这说明当前钢壳 stress-cap current map 可以用于 stress redistribution 诊断，但其 full directional tangent 仍没有 production freeze。
5. 用正半定的 associative ideal-J2 continued-plastic tangent 做独立审计后，鼓波中心的切线确实远小于两侧：Z1 极限点中心 `C_yyyy/C_yyyy^e≈0.01355`，而边缘仍为 `1.0`；按实际连接支路的局部 strain increment 计算，中心轴向 stress-increment retention 约 `6.66%`，边缘仍为 `100%`。
6. 把这一物理可接受 J2 tangent 仅替换进当前极限点的 tangent/Jacobian 做**切线敏感性审计**时，六块板在旧 radial-cap 极限点的 `dP/dD` 全部转为正值；例如 Z1 从约 `0` 变为 `+0.704 MN/D`，Z4 从约 `0` 变为 `+2.169 MN/D`。所以旧 Pu **不能再被称为已经通过钢壳 full-consistent-tangent 认证的 production Pu**。
7. 但本轮没有把这个 tangent-only sensitivity 擅自改名为“新 Pu”。原因是 associative flow tangent 不是当前 radial-cap state function 的导数；要得到新的 production Pu，必须先冻结一个同源、同应力、同切线的 plane-stress steel current operator，再用同一 operator 重跑 `P,Rq,RA,KZ,L`。在此之前给一个“修正 Pu”会把不一致的 stress law 和 tangent law 拼在一起。

---

## 1. 为什么上一轮审计还不够

上一轮已经证明：concrete、face steel、web/PBL steel 同时进入

```text
P
Rq
RA_delta
Jacobian
```

而不是先求 concrete-only 平衡再后加钢材。

但那一轮只输出了：

```text
max trial VM/fy
face steel total force
face residual/Jacobian
```

没有把钢面板内部的屈服前沿和局部切线展开。因此它无法直接回答：

```text
鼓波中心是不是先屈服？
中心的当前切线是不是比侧边低？
侧边还弹性时，中心的切线到底剩多少？
当前 Jacobian 是不是误把整张钢板统一降模？
```

本轮专门补这一层。

---

## 2. 运动学和检查位置

仍采用同一连续完整代表半波：

\[
X=\pi x/b,\qquad Y=\pi y/\ell,\qquad \ell=b.
\]

初始缺陷和附加鼓波为

\[
w_0=A_0\sin X\sin Y,
\qquad
w=A\sin X\sin Y,
\qquad A=qb.
\]

膜驱动参数

\[
M=\frac{\pi^2}{\varepsilon_0}
\left(q_0q+\frac12q^2\right),
\qquad \alpha=\lambda_A M.
\]

本轮重点检查压缩侧外表面

\[
z=-(t_c/2+t_s)
\]

在半波中线 `Y=pi/2` 上的五个位置：

```text
edge:     x/b=0
1/8:      x/b=0.125
1/4:      x/b=0.25
3/8:      x/b=0.375
center:   x/b=0.5
```

因为当前六板的 trial von-Mises 最大值均位于或极接近 `X=Y=pi/2`、压缩侧外表面，所以这一条线可以直接显示“中心先软化、前沿向两侧推进”的顺序。

---

## 3. 当前 steel radial-cap stress map

当前 Z0–Z5 direct evaluator 使用的 face stress map 是

\[
\boldsymbol\sigma^{tr}=\mathbf C_e\boldsymbol\varepsilon,
\]

\[
\bar\sigma^{tr}
=\sqrt{\sigma_x^2-\sigma_x\sigma_y+\sigma_y^2+3\tau_{xy}^2},
\]

\[
a=\min\left(1,\frac{f_y}{\bar\sigma^{tr}}\right),
\qquad
\boldsymbol\sigma=a\boldsymbol\sigma^{tr}.
\]

这一步已经是**局部的**，不是整板统一 cap：只有当前位置 `VM_trial>fy` 才会被投影回 yield surface。

因此在 current stress 层面，鼓波中心先 cap、侧边后 cap 的现象实际上已经存在。

---

## 4. radial-cap 的局部一致导数

在 `VM_trial>fy` 区内，radial current map 的解析导数为

\[
\boxed{
\mathbf C_t^{rad}
=a\mathbf C_e
-\frac{a}{\bar\sigma^{tr}}
\boldsymbol\sigma^{tr}
\otimes
\left(\mathbf n^T\mathbf C_e\right)
}
\]

其中

\[
\mathbf n=
\frac{\partial\bar\sigma}{\partial\boldsymbol\sigma}
=
\begin{bmatrix}
(2\sigma_x-\sigma_y)/(2\bar\sigma)\\
(2\sigma_y-\sigma_x)/(2\bar\sigma)\\
3\tau/\bar\sigma
\end{bmatrix}.
\]

本轮把这个局部 `C_t^rad(X,Y,z)` 重新积分回 face Jacobian，并与上一轮 finite-difference Jacobian 对照。

最大相对差：

|Case|max relative difference, analytic local radial tangent vs prior FD face Jacobian|
|---|---:|
|Z0|1.74e-10|
|Z1|3.57e-4|
|Z2|2.20e-3|
|Z3|1.22e-3|
|Z4|1.03e-10|
|Z5|2.11e-4|

所以：

```text
PREVIOUS FD JACOBIAN USED ONE GLOBAL STEEL Et = NO
PREVIOUS FD JACOBIAN IMPLICITLY SAW LOCAL RADIAL-CAP TANGENT = YES
```

这纠正了上一轮报告没有说清楚的地方。

---

## 5. 但 radial-cap tangent 本身暴露出新的问题

虽然 spatial locality 是存在的，但 radial cap 的导数并不自动等于物理可接受的 ideal-J2 flow tangent。

在 Z1 当前 ON 极限点，压缩侧外表面中线：

|x/b|VM_trial/fy|radial `Cyyyy/Cyyyy_e`|
|---:|---:|---:|
|0|0.963513|1.000000|
|0.125|1.057843|0.042092|
|0.25|1.133270|-0.000777|
|0.375|1.182131|-0.010599|
|0.5|1.199165|-0.010954|

也就是说，current radial cap 会把中心的 partial axial tangent 推到负值。

对于理想 J2 perfect plastic continued loading，一个物理可接受的 material tangent 应保持耗散一致和非负的增量稳定性；不能因为采用了一个方便的径向 current stress cap，就把这个 cap 的负局部导数自动提升为 production constitutive tangent。

这正是当前 steel-shell `FULL LOCAL CONSISTENT DIRECTIONAL TANGENT` 仍未通过 freeze 的具体数值证据。

---

## 6. 本轮独立 ideal-J2 flow tangent audit

本轮不修改 frozen equilibrium stress result，只额外使用 associative ideal-J2 plastic-loading tangent 作为审计 oracle：

\[
\boxed{
\mathbf C_{ep}
=\mathbf C_e
-\frac{(\mathbf C_e\mathbf n)(\mathbf C_e\mathbf n)^T}
{\mathbf n^T\mathbf C_e\mathbf n}
}
\]

在当前位置仍弹性时：

\[
\mathbf C_t=\mathbf C_e.
\]

对已经在 yield surface 的点，用当前连接支路的 strain increment

\[
\dot{\boldsymbol\varepsilon}
=\boldsymbol\varepsilon_{,D}
+q_{,D}\boldsymbol\varepsilon_{,q}
+\alpha_{,D}\boldsymbol\varepsilon_{,\alpha}
\]

判断

\[
\mathbf n^T\mathbf C_e\dot{\boldsymbol\varepsilon}>0
\]

时为 continued plastic loading；否则采用 elastic unloading tangent。

六块板在各自当前极限点的已屈服 face 区域，本轮检查均处于 continued plastic loading，没有发现需要在该极限点把已屈服区重置为整体弹性 unloading 的证据。

注意：这个 J2 flow tangent 在本轮只具有 `AUDIT / TANGENT SENSITIVITY` 身份；它不是未经 source-freeze 就替换 production steel current operator。

---

## 7. Z1：把屈服前沿全过程展开

Z1 是当前最明显的例子。

### 7.1 D=0.400：仍全弹性

```text
D       = 0.400000
q       = 0.00217778
alpha   = 0.0418927
M       = 0.0584529
P       = 16.962121 MN
center VM/fy = 0.76606
edge   VM/fy = 0.65233
```

压缩侧外表面中心与侧部均未屈服，`C_t=C_e`。

### 7.2 中心外表面首次屈服

```text
D_y,c   = 0.508850274
q       = 0.003320445
alpha   = 0.076845612
M       = 0.099128347
P       = 19.871434 MN
center VM/fy ~= 1.00000
quarter VM/fy = 0.95396
edge    VM/fy = 0.83355
```

因此中心首先进入 plastic-loading tangent，而 1/4 和边缘仍为弹性。

在这个刚进入 yield 的 multiaxial state，J2 partial axial tangent retention 已降到约

\[
C_{yyyy}^{ep}/C_{yyyy}^e\approx0.02843.
\]

### 7.3 屈服前沿到达 x/b=0.25

```text
D       = 0.529928234
q       = 0.003630667
alpha   = 0.087125669
M       = 0.111359989
P       = 20.321044 MN
center  VM/fy = 1.04986
quarter VM/fy ~= 1.00000
edge    VM/fy = 0.86942
```

此时 center 已明显塑化，quarter 刚刚到达 yield front，edge 仍弹性。

### 7.4 屈服前沿到达 x/b=0.125

```text
D       = 0.557246634
q       = 0.004180674
alpha   = 0.105355906
M       = 0.134293734
P       = 20.686732 MN
center  VM/fy = 1.12287
quarter VM/fy = 1.06569
1/8     VM/fy ~= 1.00000
edge    VM/fy = 0.91738
```

屈服区已经由鼓波中心向两侧大幅扩展，但边界区仍保持完整弹性切线。

### 7.5 当前 ON 极限点

```text
D_u     = 0.582466694
q_u     = 0.004879405
M_u     = 0.165729871
alpha_u = 0.131555694
P_u     = 20.812048 MN   [current radial-stress equilibrium path]
```

压缩侧外表面中线切线分布：

|x/b|VM/fy|J2 `Cyyyy/Cyyyy_e`|actual-path axial increment retention|
|---:|---:|---:|---:|
|0|0.963513|1.000000|1.000000|
|0.25|1.133270|0.053373|0.104698|
|0.50|1.199165|0.013547|0.066618|

所以用户指出的“鼓波中间模量应比两侧小”不仅成立，而且差异很大：

```text
center:  only ~1.35% of plane-stress partial Cyyyy_e
center:  ~6.66% of the elastic axial stress increment along the actual branch direction
edge:    100% elastic
```

当前极限点 face-volume audit：

```text
both faces current yielded fraction ~= 38.14%
negative/compression-side skin yielded fraction ~= 72.32%
positive skin yielded fraction ~= 3.97%
J2 z^2-weighted face Cyyyy retention ~= 0.6719
radial-cap z^2-weighted face Cyyyy retention ~= 0.6462
```

因此绝对不能把 Z1 钢面板描述成“已经整体屈服，所以钢材 Et=0”，也不能描述成“钢板仍按 Es 整体弹性”。真实状态是一个非常明显的 elastic/plastic tangent mosaic。

---

## 8. 六块板的屈服前沿先后顺序

下表中的事件均沿各板自己的 origin-connected ON equilibrium branch 定位，不使用 Zhou/Winter/试验值选点。

|Case|center first yield D / P(MN)|quarter yield D / P|1/8 yield D / P|edge yield D / P|current peak D / P|
|---|---|---|---|---|---|
|Z0|0.820511 / 33.4963|0.846385 / 33.9524|0.877378 / 34.2215|peak 前未到|0.895406 / 34.2648|
|Z1|0.508850 / 19.8714|0.529928 / 20.3210|0.557247 / 20.6867|peak 前未到|0.582467 / 20.8120|
|Z2|1.009475 / 37.1886|1.041258 / 37.6619|1.081326 / 37.8061|peak 前未到|1.077007 / 37.8097|
|Z3|0.605026 / 39.3431|0.625207 / 39.9319|0.648873 / 40.2937|peak 前未到|0.664451 / 40.3617|
|Z4|0.865887 / 62.9614|0.885424 / 63.4474|0.906966 / 63.6988|0.934978 / 63.6452，已在 current peak 之后|0.918014 / 63.7293|
|Z5|0.912752 / 13.9901|0.920900 / 14.0406|0.929316 / 14.0664|0.938698 / 14.0783|0.939442 / 14.0786|

因此 Z0–Z4 都具有很清楚的

```text
center yield -> yield front expands sideways -> current limit
```

顺序；Z5 则由于 q 很小、整体压缩成分占主导，压缩侧皮肤在极限附近接近全面进入 yield，空间差异相对弱。

---

## 9. 当前极限点的空间软化程度

|Case|center VM/fy|edge VM/fy|center J2 Cyyyy retention|edge retention|both-face yielded|compression-skin yielded|J2 z2-weighted face retention|
|---|---:|---:|---:|---:|---:|---:|---:|
|Z0|1.12650|0.96413|0.04599|1.000|27.69%|55.38%|0.7509|
|Z1|1.19916|0.96351|0.01355|1.000|38.14%|72.32%|0.6719|
|Z2|1.12987|0.90512|0.01623|1.000|17.30%|34.60%|0.8366|
|Z3|1.12812|0.96888|0.04814|1.000|28.72%|57.45%|0.7427|
|Z4|1.06701|0.98161|0.09170|1.000|26.72%|53.44%|0.7657|
|Z5|1.03029|1.00079|0.13394|0.16390|49.11%|91.71%|0.5832|

其中 `z2-weighted face retention` 是

\[
\eta_{s,I}^{audit}
=
\frac{\int C_{yyyy}^t z^2\,dV_s}
{\int C_{yyyy}^{e} z^2\,dV_s},
\]

用于衡量外层钢板对 bending-material tangent 的保留程度。它不是完整 KZ；完整稳定矩阵仍必须保留全部方向分量和 current-stress geometric terms。

---

## 10. 压缩侧中线当前极限点的 yielded-band 宽度

把 `Y=pi/2`、压缩侧外表面上 `VM/fy=1` 的位置记为从侧边量起的 `x_f/b`。由于关于中心对称，中心 yielded band 的宽度为

\[
1-2x_f/b.
\]

|Case|x_f/b from edge|center yielded band / b|
|---|---:|---:|
|Z0|0.07046|0.8591|
|Z1|0.04633|0.9073|
|Z2|0.13591|0.7282|
|Z3|0.06284|0.8743|
|Z4|0.07185|0.8563|
|Z5|0|1.0000|

这进一步说明：即使 whole-face volume yielded fraction 只有 17–38%，压缩侧鼓波中线可能已经形成很宽的低切线区，而另一张皮肤和靠边区域仍保持高切线。

---

## 11. 这对当前 Pu 有什么直接影响？

### 11.1 保持 current radial stress map 不变

如果仅重新显式计算其**自身解析导数**，结果和上一轮 finite-difference residual Jacobian 基本一致，因此此前的 radial-stress equilibrium peak 数值不会因为“把局部 radial tangent 显式写出来”而突然改变。

换言之：

```text
“上一轮把整张钢板统一 Et=0” = FALSE
“上一轮 finite-difference Jacobian 已隐式看到局部 radial cap” = TRUE
```

### 11.2 但把 physically admissible J2 flow tangent 代入 tangent audit

在 current radial-stress equilibrium peak 上，旧路径斜率与 tangent-only J2 sensitivity 为：

|Case|current radial-map dP/dD at peak, MN/D|J2 tangent-only sensitivity dP/dD, MN/D|
|---|---:|---:|
|Z0|~0|+1.5158|
|Z1|+0.00076|+0.7042|
|Z2|+0.00979|+2.2250|
|Z3|+0.02823|+2.6364|
|Z4|-0.00427|+2.1688|
|Z5|-0.31747|+0.2640|

所以旧 peak 在一个物理可接受的 J2 positive-semidefinite tangent 下不再是 tangent-neutral point；它还在“继续增载”方向。

这说明 current radial cap 的过软/局部负 tangent 很可能提前触发了当前路径极限，至少在 tangent scale 上不能忽略。

但这里必须守住数学边界：

```text
J2 tangent-only sensitivity != new production Pu
```

因为 current equilibrium stress 仍来自 radial state map，而 J2 flow tangent 是另一种 incremental constitutive law。把两者混合后直接向前积分会失去 same-source stress/tangent consistency。

---

## 12. 本轮真正修改的项目判断

更新后的状态应写成：

```text
STEEL FACE NONUNIFORM YIELD ORDER = CONFIRMED
CENTER-FIRST YIELD FRONT = CONFIRMED FOR Z0-Z5
EDGE REMAINS ELASTIC AT CURRENT PEAK = Z0,Z1,Z2,Z3,Z4 YES; Z5 NO
WHOLE-STEEL GLOBAL Et=0 MODEL = REJECTED
WHOLE-STEEL GLOBAL Es MODEL AFTER CENTER YIELD = REJECTED
CURRENT RADIAL-CAP LOCALITY = CONFIRMED
CURRENT RADIAL-CAP ANALYTIC TANGENT vs PRIOR FD JACOBIAN = MATCH
CURRENT RADIAL-CAP TANGENT PHYSICAL ACCEPTANCE = FAIL / NOT PRODUCTION-FROZEN
ASSOCIATIVE J2 LOCAL TANGENT AUDIT = POSITIVE-SEMIDEFINITE AND PHYSICALLY CONSISTENT AS AUDIT
OLD Z0-Z5 Pu FULL-STEEL-TANGENT PRODUCTION CERTIFICATE = NOT PASSED
```

因此当前下一步不是再检查“钢材是不是最后加上”，而是：

```text
freeze one source-consistent plane-stress steel current operator
that returns BOTH sigma_s(epsilon) and Ct_s(epsilon)
with the same constitutive identity;
then compile the spatially varying Ct_s(X,Y,z) analytically,
assemble KZ_s^mat + KZ_s^geo,
and rerun Z1/Z4 first before Z0-Z5 batch.
```

这个步骤必须保持 formal zero-spatial-discretization。此次使用的面内/厚度检查点只属于 direct-continuum audit oracle，不获得正式理论身份。

---

## 13. Formal/audit boundary

```text
FORMAL:
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0

AUDIT ONLY:
dense direct-continuum evaluation of VM/fy and local tangent profile
yield-front localization
finite-resolution face-volume yielded-fraction estimate
associative-J2 tangent sensitivity at frozen current states
```

没有用这些 audit points 去拟合、选根、修正材料参数或校准 comparator。

---

## 14. 同批数据文件

- `semantic_v2/60_validation/steel_shell/20260817_2342__NZSCCM__Z0_Z5__STEEL_YIELD_FRONT_SEQUENCE.csv`
- `semantic_v2/60_validation/steel_shell/20260817_2342__NZSCCM__Z0_Z5__STEEL_LOCAL_TANGENT_PEAK_PROFILE.csv`
- `semantic_v2/60_validation/steel_shell/20260817_2342__NZSCCM__Z0_Z5__STEEL_TANGENT_SEQUENCE_SUMMARY.csv`

Source/theory anchors used by this audit:

- `20260814_TUNK__NZSCCM__STEEL_SHELL__YUN_SSSS_IDEAL_EP_POSTBUCKLING_TANGENT__THEORY_DERIVATION.md`
- `20260813_1834__NZSCCM__STEEL_SHELL__J2_DEFORMATION_THEORY_SOURCE_CURVE_PLANE_STRESS__MATERIAL_OPERATOR_DERIVATION.md`
- `20260816_1217__NZSCCM__NC_STEEL_SHELL_PANEL__UNIFIED_WORKFLOW_V1_ADAPTER_BRIDGE__GOVERNANCE.md`
- `20260817_1407__NZSCCM__Z6_N48_FAMILY_SOURCE_COMPILER_AND_AIRY_MEMBRANE_REDIStribution__THEORY.md`
