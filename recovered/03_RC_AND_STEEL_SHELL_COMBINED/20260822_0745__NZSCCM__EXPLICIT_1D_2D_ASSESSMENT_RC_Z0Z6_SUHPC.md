# NZ-SCCM — 当前显式路径 1D → 2D 材料判断统一验收包

**Time:** 2026-08-22 07:45 +08:00  
**Status:** `EXECUTED / USER_ACCEPTANCE_PENDING`  
**Scope:** selected Swartz RC + Z0–Z6 + steel-shell UHPC  

## 0. 本轮边界

本轮严格回到当前 Marguerre–Airy 显式路径，不继续 2026-08-22 00:15 / 01:05 的 hard-envelope/history/material-point 诊断岔路。

正式结构层只使用：

\[
P_{pb}(q)=P_{cr}\frac{q}{q+q_0}+Cq(q+2q_0),
\]

\[
n(s;q)=\frac{P_{pb}(q)}b+Gq(q+2q_0)(1-2s^2),
\qquad
m(s;q)=Jqs,
\]

以及 Airy 横向膜力：

\[
N_x
=-\frac{\alpha^2b^2\Delta_A}{8A_{22}}
q(q+2q_0)\cos(2\beta y),
\qquad N_{xy}=0.
\]

本轮“1D → 2D”只表示：

\[
\boxed{
\text{同一个显式结构候选根}
\to
\text{加入 Airy 二维膜力}
\to
\text{用二维材料容量判断检查/必要时重切显式容量根}
}
\]

材料本构/强度关系只作为容量判断依据，不建立第二套结构求解器。

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_material_points = 0
LOAD_PATH_TRACKING = 0
RITZ_ORDER = NONE
HISTORY_STATE_MACHINE = OFF_MAINLINE
HARD_ENVELOPE_HISTORY_OVERLAY = OFF_MAINLINE_DIAGNOSTIC
EXPERIMENT_IN_ROOT_SELECTION = 0
FEM_IN_ROOT_SELECTION = 0
```

## 1. 1D 与 2D 的统一定义

### 1.1 1D 显式容量

1D 列表示当前显式结构需求 \(P_{pb},n,m\) 与单轴材料容量截面联立得到的最小正根。

- RC：显式 Nguyen 型抛物线压缩上升支 + 钢筋当前应力，截面容量 \(n_u(c),m_u(c)\) 完全闭式；
- Z：显式两段塑性 \(N-M\) 容量；
- SUHPC：当前显式 UHPC 单轴 backbone + 钢面局部分支 + 纵向 web 轴压贡献。

### 1.2 2D 显式材料判断

2D 列不重新做空间积分，只在同一有限控制候选上加入 Airy \(N_x\) 后判断材料二维状态。

- 若二维判断不触发新的容量限制，\(P_u^{2D}=P_u^{1D}\)；
- 若二维判断触发且已有有限显式重切公式，则重解得到 \(P_u^{2D}\)；
- 若二维判断触发但对应材料尚没有唯一有限显式重切公式，则只判为 `TRIGGERED / Pu open`，不造数。

这正是本轮要交给用户验收的理论层级。

---

# 2. 筛选后的 Swartz RC

采用可信重复/准重复组：Case 1/2、9/10、19/20、21/22。

Swartz 配筋率采用已修正来源解释：

\[
\rho_x=\rho_y=p_{table},
\]

不是 \(p_{table}/2\)。

本轮 RC 二维判断采用已建立的有限 TC 容量判断。共同普通混凝土材料输入保留项目基线

\[
f_t=0.10f_c.
\]

Swartz 没有逐板实测 \(f_t\)，因此 Case1/2 的 2D 数值是“统一材料输入下的显式二维工作值”，不是 specimen-specific source-closed tensile calibration。

| Case | 1D explicit Pu / kN | 2D explicit Pu / kN | Pf / kN | 1D error | 2D error | error change | 2D judgment |
|---:|---:|---:|---:|---:|---:|---:|---|
|1|567.712|495.989|490.194|+15.814%|+1.182%|−14.632 pp|TC active / finite re-cut|
|2|561.638|501.025|506.652|+10.853%|−1.111%|−11.963 pp|TC active / finite re-cut|
|9|515.424|515.424|625.865|−17.646%|−17.646%|0|2D criterion inactive at 1D root|
|10|534.711|534.711|696.147|−23.190%|−23.190%|0|2D criterion inactive at 1D root|
|19|339.177|339.177|377.654|−10.188%|−10.188%|0|no finite 2D re-cut activated|
|20|335.013|335.013|372.761|−10.127%|−10.127%|0|no finite 2D re-cut activated|
|21|350.460|350.460|368.313|−4.847%|−4.847%|0|no finite 2D re-cut activated|
|22|351.679|351.679|355.858|−1.174%|−1.174%|0|no finite 2D re-cut activated|

### RC reading

The 2D judgment is selective rather than a global multiplier:

- Case1/2: strong TC re-cut; the previous +10–16% high bias reduces to about ±1%;
- Case9/10: current 2D TC criterion does not activate, so the large low bias remains visible;
- Case19/20 and 21/22: this finite 2D judgment does not change the current 1D candidate.

No attempt is made to remove the remaining biases.

---

# 3. Z0–Z6：当前 Marguerre–Airy 显式路线从头重算

Important: the following `1D explicit` values are **not** the older AR2 values `31.99/20.02/...`. They are fresh calculations using the current 2026-08-21 Marguerre–Airy explicit formulation.

Common rules:

- all physical walls have \(a_{phys}=2b\);
- current integer search gives \(m_*=2\), hence \(\ell=b\);
- \(t_s=4\) mm/face, \(\rho_w=0.02\), \(E_s=206\) GPa;
- structural coefficients are regenerated from each case's raw parameters;
- no Zhou/Winter value enters mode or root solution.

Fresh current 1D coefficients/root summary:

|Case|Pcr / MN|C / MN|q_u(1D)|s_u(1D)|Pu(1D) / MN|
|---|---:|---:|---:|---:|---:|
|Z0|78.30671|43035.79873|0.00342823|1.0000|37.82571|
|Z1|40.35021|35478.23714|0.00499668|0.8403|24.71413|
|Z2|78.30671|43035.79873|0.00432177|1.0000|42.95901|
|Z3|81.78821|46121.44731|0.00461430|1.0000|46.49489|
|Z4|179.75477|80875.42965|0.00244543|1.0000|70.26572|
|Z5|231.78841|14345.26624|0.000258842|1.0000|14.11819|
|Z6|39.28801|86071.59746|0.01380741|0.2984|56.37942|

At these 1D roots the Airy transverse demand increases strongly toward Z6. Approximate \(|N_x|\) working magnitudes are:

\[
269.4,\ 369.5,\ 366.2,\ 430.1,\ 246.3,\ 14.7,\ 2070.4\ \mathrm{N/mm}
\]

for Z0 through Z6 respectively.

The explicit 2D material judgment does not re-cut Z0–Z5. Z6 strongly activates the steel-face/concrete biaxial capacity interaction and is re-cut by the already-derived finite phase-rebalanced 2D section equations. The governing Z6 2D state is the finite endpoint \(s=0\), where the phase stresses are uniform through thickness and no thickness quadrature is required.

| Case | 1D Pu / MN | 2D Pu / MN | Zhou / MN | Winter / MN | 2D vs Zhou | 2D vs Winter | ordering |
|---|---:|---:|---:|---:|---:|---:|---|
|Z0|37.8257|37.8257|36.9455|41.5008|+2.382%|−8.855%|Zhou < 2D < Winter|
|Z1|24.7141|24.7141|23.7214|26.1001|+4.185%|−5.310%|Zhou < 2D < Winter|
|Z2|42.9590|42.9590|41.2134|45.7333|+4.236%|−6.066%|Zhou < 2D < Winter|
|Z3|46.4949|46.4949|44.3203|49.0469|+4.907%|−5.203%|Zhou < 2D < Winter|
|Z4|70.2657|70.2657|69.3399|79.3861|+1.335%|−11.489%|Zhou < 2D < Winter|
|Z5|14.1182|14.1182|14.6816|14.6816|−3.838%|−3.838%|2D < Zhou = Winter|
|Z6|56.3794|51.3450|49.4868|50.1859|+3.755%|+2.310%|Zhou < Winter < 2D|

### Z reading

- Z0–Z4: current explicit result naturally lies between Zhou and Winter without using either comparator in calculation;
- Z5: current explicit result is about 3.84% lower than both comparator formulas;
- Z6: 2D interaction changes the prediction materially,
  \[
  56.3794\to51.3450\ \mathrm{MN},
  \]
  a reduction of
  \[
  \boxed{8.9295\%},
  \]
  but remains 2.31% above Winter. This residual is shown as-is and is not tuned away.

---

# 4. Steel-shell UHPC：37 mm web geometry rebased explicit assessment

## 4.1 Geometry rebase

For the BH family, the old `32 mm` net web height is not used as the current comparator geometry. The geometry audit indicates a net added web height close to

\[
\boxed{h_w=37\ \mathrm{mm}}
\]

inside the 42-mm UHPC core.

With 9 longitudinal webs:

\[
A_{w,total}=9\times4\times37=1332\ \mathrm{mm^2},
\]

\[
\rho_w=\frac{1332}{42B}.
\]

Thus:

|Case|rho_w, 37 mm|
|---|---:|
|BH005|12.6857%|
|BH010|6.34286%|
|BH020|3.17143%|
|BH032|1.98214%|
|BH050|1.26857%|

The regenerated explicit coefficients are:

|Case|Pcr / MN|C / MN|G / N/mm|J / N|
|---|---:|---:|---:|---:|
|BH005|197.5373|1179.2700|5.3614e6|6.7473e7|
|BH010|98.3195|2253.6479|4.8274e6|3.2496e7|
|BH020|49.0475|4400.9325|4.5604e6|1.5938e7|
|BH032|30.6284|6977.1939|4.4603e6|9.8889e6|
|BH050|19.5920|10841.3718|4.4002e6|6.3010e6|

The resulting corrected-geometry 1D explicit roots are:

|Case|q_u|c_u / mm|Pu(1D) / MN|
|---|---:|---:|---:|
|BH005|3.10044e-5|275.08|2.41999|
|BH010|1.18557e-4|182.15|4.45287|
|BH020|4.99119e-4|110.30|8.17466|
|BH032|1.41701e-3|72.86|11.14350|
|BH050|5.01438e-3|51.50|13.61827|

T120/T360 retain their already web-corrected current geometry/result for this table.

## 4.2 Finite 2D UHPC judgment

The current explicit UHPC 2D precheck uses the Airy transverse membrane demand and the UHPC tensile cracking anchor

\[
f_{t,cr}=9.7677\ \mathrm{MPa}.
\]

For the current compressed core profile, the finite transverse closure is

\[
\varepsilon_x^0
=
\frac{
N_x+\nu_cN_c+\nu_sN_f
}{
(1-\rho_w)t_cE_c+2t_sE_s
},
\]

and

\[
\sigma_x^c(y)=E_c\varepsilon_x^0-\nu_c\sigma_y(y).
\]

Only the analytic extrema required by the explicit section profile are checked; no material-point field is introduced.

For the corrected BH roots, Airy \(N_x\) increases from about `0.64 N/mm` at BH005 to about `214.6 N/mm` at BH050. The resulting maximum transverse tensile UHPC stress is approximately:

- BH005: −0.52 MPa;
- BH010: +1.26 MPa;
- BH020: +4.62 MPa;
- BH032: +7.34 MPa;
- BH050: +11.69 MPa.

Hence BH005–BH032 pass the current finite 2D tensile check and remain unchanged. BH050 exceeds the current UHPC tensile anchor and is therefore rejected as a final 2D value, but this stripped explicit path does not yet possess a unique finite UHPC TC re-cut formula; no corrected BH050 number is invented.

| Case | geometry | 1D Pu / MN | 2D Pu / MN | Abaqus peak / MN | theory/FEM error after 2D | max transverse UHPC tension | 2D judgment |
|---|---|---:|---:|---:|---:|---:|---|
|T120|current web-corrected|12.3480|12.3480|12.6378|−2.293%|+8.06 MPa|PASS, unchanged|
|T360|current web-corrected|11.2978|11.2978|10.9688|+3.000%|+7.27 MPa|PASS, unchanged|
|BH005|37-mm web|2.41999|2.41999|2.3558|+2.725%|−0.52 MPa|PASS, unchanged|
|BH010|37-mm web|4.45287|4.45287|4.3043|+3.452%|+1.26 MPa|PASS, unchanged|
|BH020|37-mm web|8.17466|8.17466|8.0076|+2.086%|+4.62 MPa|PASS, unchanged|
|BH032|37-mm web|11.14350|11.14350|10.9905|+1.392%|+7.34 MPa|PASS, unchanged|
|BH050|37-mm web|13.61827|**TRIGGERED / unique Pu OPEN**|12.2198*|OPEN (1D is +11.444%)|+11.69 MPa|2D tensile gate active|

`*` BH050 Abaqus comparator is from a different diagnostic model family and has lower validation confidence than BH005–BH032.

### SUHPC reading

- T120/T360 and corrected BH005–BH032: current finite 2D material judgment does not alter the 1D root;
- BH050: the corrected geometry plus larger Airy transverse membrane force pushes the UHPC transverse tension above the current cracking anchor, so the 1D value cannot be accepted as the final 2D value;
- the present stripped explicit theory can say `Pu_2D < 13.6183 MN` for BH050, but cannot yet give a unique corrected Pu without adding a new finite UHPC TC capacity formula. This boundary is left explicit for user judgment.

---

# 5. Cross-family summary for user acceptance

|Family|What 2D changes|Current observation|
|---|---|---|
|Selected RC|TC capacity judgment selectively re-cuts Case1/2|Case1/2 move from +10–16% high to about ±1%; other selected biases remain|
|Z0–Z6|Airy transverse membrane + biaxial material/steel judgment|Z0–Z4 stay between Zhou/Winter; Z5 low; Z6 falls 8.93% but remains 2.31% above Winter|
|SUHPC|Airy transverse membrane checked against finite UHPC 2D material criteria|T120/T360/BH005–032 pass unchanged; BH050 triggers and remains numerically open|

This report intentionally stops here. No new material history model, no material-point discretization, no hidden multiplier, and no comparator-based correction is introduced.

```text
CURRENT_ASSESSMENT = EXPLICIT_1D_TO_2D_MATERIAL_JUDGMENT
USER_ACCEPTANCE = PENDING
```
