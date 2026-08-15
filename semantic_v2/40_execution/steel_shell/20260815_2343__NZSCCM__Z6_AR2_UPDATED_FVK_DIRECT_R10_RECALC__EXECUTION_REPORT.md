# NZ-SCCM — Z6 AR2 更新膜力重分布完整理论重算执行报告

**Timestamp:** 2026-08-15 23:43 +08:00  
**Identity:** `Z6_AR2_UPDATED_FVK_R10_DIRECT_CONTINUUM_AUDIT_RECALC`

## 1. 计算目标

按用户最新指令，不再围绕原 Z6 的固定 D checkpoint 做局部推进，而直接对长宽比大于 1 的 Z6 比较板重新建立完整更新后屈曲路径并寻找峰值。

计算对象沿用此前 AR2 定义：

```text
a=24000 mm
b=12000 mm
a/b=2
m=2
ell=a/m=12000 mm
h=130 mm
tc=122 mm
ts=4 mm
fc=30.4 MPa
Es=206000 MPa
fy=355 MPa
nu_c=0.18
nu_s=0.30
eps0=0.0018712490394580678
q0=a/(500b)=0.004
A0=q0*b=48 mm
```

`m=2` 只决定完整物理板上有两个最优重复半波；正式代表域仍为一个连续完整半波 `ell=12000 mm`。

## 2. 更新后的完整平衡系统

面外场仍为单一完整 `(1,1)` 半波：

\[
w_0=A_0\sin X\sin Y,\qquad
w_m=qb\sin X\sin Y.
\]

Nguyen 二阶几何不变。面内最小 FvK 重分布坐标为

\[
\mathbf m=[c,p_{20},p_{02}]^T.
\]

D15 变量中新增面内方向仍为有限解析函数：

\[
e_{x,20}=y_s^2-2x_s^2y_s^2,
\]

\[
e_{y,20}=\frac{k^2}{2}(1-2x_s^2)(1-2y_s^2),
\]

\[
e_{y,02}=1-2y_s^2.
\]

每个给定 D 解：

\[
R_q=R_c=R_{20}=R_{02}=0.
\]

## 3. current material operator

### 3.1 混凝土

本轮直接评价冻结 R10 物理 current operator，不通过 N48 系数代理。

对归一化 plane-stress effective strain matrix

\[
E_u=\begin{bmatrix}E_{xx}&G\\G&E_{yy}\end{bmatrix}
\]

逐点谱分解，直接评价冻结 scalar targets `U(lambda), C(lambda), T(lambda), T^7(lambda)`，然后重构：

\[
S=U-a_{cc}\det(C)C+\operatorname{tr}(T)C-CT
-\rho a_t\det(T)[\operatorname{tr}(T^7)I-T^7].
\]

因此材料物理函数与现有 R10 完全一致；变化仅是 audit backend 绕过 N48 编译表示。

### 3.2 钢壳

两块 faceplates 采用同一当前 local radial cap：

\[
\alpha=\min(1,f_y/\sigma_{vm}^{trial}).
\]

没有使用 whole-shell force-only cap。

## 4. 为什么本轮使用 direct-continuum audit backend

当前正式 N48/D15 增广实现仍存在 dense Cayley-Hamilton A/B pair representation/runtime gate。用户要求直接重算完整 AR2 路径，因此本轮采用 Gauss-Legendre 高阶连续积分作为 audit executor。

这一后端仅用于本轮物理路径审计：

```text
formal N48/D15 zero-spatial-quadrature production release = NO
formal project governance N_formal_spatial_quadrature = 0 remains unchanged
```

不能把本轮数值称为正式零积分 production certificate。

## 5. connected equilibrium path

48x48x18 求解/记录路径从 D=.10 连续推进至 D=1.40。所有记录点均解四个广义平衡，求解网格上的 `Rq,Rc,R20,R02` 接近机器零。

主要路径：

| D | q | c | p20 | p02 | P (MN) | Pc (MN) | Ps (MN) | steel rmax |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|0.10|0.0013078|+0.00146|-0.00508|-0.00384|11.4346|7.7995|3.6351|0.154|
|0.20|0.0029327|-0.01116|-0.02554|+0.02086|20.7747|13.7039|7.0708|0.321|
|0.30|0.0051298|-0.05225|-0.07696|+0.08531|27.6562|17.5457|10.1105|0.494|
|0.40|0.0076552|-0.12095|-0.16236|+0.18128|32.2538|19.5666|12.6873|0.660|
|0.50|0.0101124|-0.20341|-0.26861|+0.28845|35.4117|20.4568|14.9548|0.810|
|0.60|0.0123750|-0.29338|-0.38586|+0.40084|37.9172|20.8552|17.0620|0.943|
|0.70|0.0144640|-0.38919|-0.51048|+0.51647|40.0427|20.9992|19.0435|1.062|
|0.75|0.0154878|-0.44228|-0.57875|+0.58012|40.7053|20.9430|19.7623|1.145|
|0.80|0.0165131|-0.50121|-0.65322|+0.65184|40.9455|20.8116|20.1338|1.239|
|0.825|0.0170148|-0.53175|-0.69146|+0.68924|40.9763|20.7288|20.2475|1.287|
|0.8308|0.0171299|-0.53891|-0.70040|+0.69801|40.9769|20.7077|20.2692|1.298|
|0.85|0.0175074|-0.56276|-0.73012|+0.72717|40.9669|20.6346|20.3323|1.335|
|0.90|0.0184661|-0.62577|-0.80827|+0.80375|40.8608|20.4208|20.4400|1.431|
|1.00|0.0202914|-0.75397|-0.96751|+0.95400|40.3675|19.8664|20.5012|1.620|
|1.20|0.0236138|-1.01316|-1.29133|+1.24663|39.0567|18.7196|20.3371|1.986|
|1.40|0.0265321|-1.26259|-1.60518|+1.52873|38.2242|18.1270|20.0972|2.347|

完整记录见 companion PATH.csv。

## 6. 峰值细化

围绕 D≈.83 用 96x96x36 求解状态，再用更高阶独立网格评价：

```text
D=.8250: 128x128x48 audit P=40.9715363450 MN
D=.8300: 128x128x48 audit P=40.9724530492 MN
D=.8308: 128x128x48 audit P=40.9724721822 MN
D=.8325: 128x128x48 audit P=40.9723891086 MN
```

在 D=.8308 进一步做 160x160x60 audit：

```text
P=40.9733400613 MN
```

128-grid 三点局部二次拟合给出峰值位置约 `D=0.83079`。综合高阶审计：

\[
\boxed{P_u^{AR2,updated\ membrane}\approx40.97\ \mathrm{MN}}
\]

数值连续积分在峰值附近的网格差异约千分之几 MN 量级；该精度远小于当前结构/材料模型本身的工程误差。

## 7. 峰值状态中间参数

推荐代表峰值状态：

```text
D≈0.8308
q≈0.01712
c≈-0.538
p20≈-0.700
p02≈+0.697
P≈40.97 MN
Pc≈20.69 MN
Ps≈20.28 MN
```

几何幅值：

```text
Ainc=q*b≈205.42 mm
A0=48 mm
Atotal≈253.42 mm
Atotal/h≈1.949
pi*Atotal/b≈0.06635 rad≈3.80 deg
```

面内广义应变尺度：

```text
eps0*c≈-1.0066e-3
eps0*p20≈-1.3085e-3
eps0*p02≈+1.3051e-3
```

160-grid material audit：

```text
R10 principal normalized lambda≈[-1.13695,+0.47949]
steel trial rmax≈1.30146
```

所以局部钢材径向屈服 cap 在峰值附近已经活动。

## 8. 与旧 AR2 路径比较

此前未释放完整 FvK membrane equilibrium 的 AR2 R10 direct-continuum audit：

```text
Pu_old=44.5529191054 MN
```

本轮：

```text
Pu_updated≈40.97334 MN
Delta≈-3.57958 MN=-8.03%
```

Zhou comparator：`49.4867667519 MN`，本轮约低 17.20%。

Winter comparator：`50.1858541295 MN`，本轮约低 18.36%。

重要的是：加入膜力重分布并没有自动增加 Pu。它显著改变 connected equilibrium path，并在当前 reduced two-face steel object 中导致更强面内重分布和较早/较强局部钢屈服。

## 9. 当前对象限制

当前钢对象仍只有两块 faceplates。longitudinal PBL/web steel phase 尚未进入 `Rq,Rc,R20,R02` 的实际增广平衡，因此本轮约 40.97 MN 不能解释为包含完整 Zhou section topology 的最终 Z6 物理承载力。

此前 H0 证明 web phase 对 Z6 截面强度基线约有 10% 量级贡献，但它不能用 `P_web` 事后直接相加，因为它同时会改变所有广义残量和峰值路径。

## 10. 当前结论

```text
UPDATED_FVK_MEMBRANE_PATH = SOLVED_IN_DIRECT_R10_CONTINUUM_AUDIT
AR2_AUDIT_PEAK ≈ 40.97 MN
MEMBRANE_REDISTRIBUTION_EFFECT = LARGE_AND_CAPACITY_REDUCING_FOR_CURRENT_REDUCED_OBJECT
FORMAL_N48_D15_PRODUCTION_Pu = NOT YET RELEASED
FULL_PBL_WEB_SECTION_EQUILIBRIUM = NOT YET INCLUDED
```
