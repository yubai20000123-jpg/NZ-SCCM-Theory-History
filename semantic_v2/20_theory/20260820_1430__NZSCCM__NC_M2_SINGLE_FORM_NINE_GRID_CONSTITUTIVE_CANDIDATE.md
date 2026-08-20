# NZ-SCCM — NC-M2 单公式九宫格混凝土候选

时间：2026-08-20 14:30 +08:00

状态：`ACTIVE_MATERIAL_CANDIDATE / NOT_YET_PRODUCTION_LOCK`

本文件正式撤回此前 NC-M1 的“多阈值、多分段、min/max”极简化思路。NC-M1 仅保留为诊断性失败候选，不再进入后续积分与结构求解。

## 1. 新目标

按照用户九宫格主应变分类，只在物理象限层面保留 CC / TC / CT / TT。每一个实体象限内部只允许一个连续显式公式，不再继续分裂材料子段。

原则：

- 九宫格可以分区；
- 每个实体格内部不再增加阈值；
- 不使用 `min/max`；
- 不使用 positive-part；
- 不使用额外状态变量；
- 优先允许一个短的低阶有理函数，而不是三个以上分段直线；
- 边界格 ε1=0、ε2=0 应由相邻实体格自然退化得到，不另建材料分支。

## 2. 单轴压缩骨架

定义

\[
c=-\varepsilon_c/\varepsilon_{c0}\ge0.
\]

采用单一有理式

\[
\boxed{C(c)=\frac{2c}{1+c^2}}.
\]

性质：

\[
C(0)=0,\quad C'(0)=2,\quad C(1)=1,\quad C'(1)=0,\quad C(c)\to0\;(c\to\infty).
\]

无峰前/峰后切换点。

对于当前普通混凝土基准 κ=E0 ε0/fc≈2.0005，该式在峰前与原 Saenz 参考关系几乎重合；0≤c≤1 的面积比约为 0.999955。该对比只用于曲线审计，不代表 NC-M2 依附 Nguyen/Foster 理论。

## 3. 单轴拉伸骨架

定义

\[
t=\varepsilon_t/\varepsilon_{cr}\ge0.
\]

采用单一有理式

\[
\boxed{T(t)=\frac{t}{1-t+t^2}}.
\]

性质：

\[
T(0)=0,\quad T'(0)=1,\quad T(1)=1,\quad T'(1)=0,\quad T(t)\to0.
\]

无“开裂后第二段/残余第三段”。

## 4. TC / CT 压缩削弱

采用单一光滑式

\[
\boxed{\beta(t)=\frac{1}{1+0.15t^2}}.
\]

性质：

\[
\beta(0)=1,\quad \beta'(0)=0,
\]

且随横向主拉应变单调减小。

与旧 Nguyen 型参考曲线在 0≤t≤3 的面积比约为 0.94525，即当前 M2 整体约低 5.5%。该数字仅用于材料级诊断，不参与板级反标。

## 5. CC 双压增强

不再使用应变比 `min/max`。直接利用两个单轴压缩骨架的乘积形成对称增强：

\[
\boxed{\eta(c_1,c_2)=1+0.16\,C(c_1)C(c_2)}.
\]

因此

\[
\eta=1\quad\text{若任一压缩方向退化为零},
\]

而等双压峰值点 c1=c2=1 时

\[
\eta(1,1)=1.16.
\]

沿 c1=1、c2=ρ 的对比路径，M2 与 Foster/Kupfer 参考增强曲线的面积比约为 0.92192；M2 为明显更保守、更平滑的单式关系。

## 6. 九宫格主应力关系

### CC: ε1<0, ε2<0

\[
c_i=-\varepsilon_i/\varepsilon_{c0},
\]

\[
\boxed{\sigma_i=-f_c\,\eta(c_1,c_2)\,C(c_i)},\qquad i=1,2.
\]

### TC: ε1>0, ε2<0

\[
t_1=\varepsilon_1/\varepsilon_{cr},\qquad c_2=-\varepsilon_2/\varepsilon_{c0},
\]

\[
\boxed{\sigma_1=f_tT(t_1)},
\]

\[
\boxed{\sigma_2=-f_c\beta(t_1)C(c_2)}.
\]

### CT: ε1<0, ε2>0

与 TC 完全对称：

\[
\boxed{\sigma_1=-f_c\beta(t_2)C(c_1)},\qquad
\boxed{\sigma_2=f_tT(t_2)}.
\]

### TT: ε1>0, ε2>0

\[
\boxed{\sigma_i=f_tT(t_i)},\qquad i=1,2.
\]

### 边界格

ε1=0 或 ε2=0 时直接取相邻实体式的自然极限，不新增材料公式。

## 7. 当前复杂度判定

NC-M2 与已撤回的 M1 相比：

- CC：1 个公式；
- TC：1 个公式；
- CT：TC 的对称式；
- TT：1 个公式；
- 内部分段数：0；
- 人为材料阈值：0；
- min/max：0；
- positive-part：0；
- 局部材料 Newton：0。

因此 NC-M2 当前作为下一轮积分/联立审计的材料候选，但尚未 production lock。下一步必须先检查其九宫格曲线、能量趋势和代入主应变虚功后的解析复杂度，不得直接用 Case21 Pu 反标参数。
