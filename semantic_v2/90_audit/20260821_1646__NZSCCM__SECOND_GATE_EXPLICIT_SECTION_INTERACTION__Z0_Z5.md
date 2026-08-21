# NZ-SCCM — 第二生死门：显式截面 N–M 容量与 Z0–Z5 无拟合核验

时间：2026-08-21 16:46 +08:00  
状态：`Z_STEEL_SHELL_SECOND_GATE_STRONG_PASS / RC_NOT_YET_TESTED`

## 0. 本轮唯一问题

第一层几何后屈曲已经冻结为 Marguerre–Airy 单物理模态三次式：

\[
F_{pb}(P,q)=Cq^3+3Cq_0q^2+(2Cq_0^2+P_{cr}-P)q-Pq_0=0,
\]

或

\[
P_{pb}(q)=\frac{q}{q+q_0}\left[P_{cr}+C(q+q_0)(q+2q_0)\right].
\]

本轮不修改该式，不增加 Airy/Ritz 阶数，不重新把 NC-M6/R10/C73 塞入整板后屈曲 PDE。只回答：

> 对 steel-shell concrete Z 系列，能否建立一个同样低阶、来源明确、无经验拟合、无需荷载路径追踪的 \(F_{cap}(P,q)=0\)？

结论：**可以。**

---

## 1. 来源身份与本轮派生边界

1. 周思铭只提供 steel-shell 正交各向异性截面刚度来源：\(D_x,D_y,D_{xy},D_\mu,H=D_{xy}+D_\mu\)。
2. Attard 类方法提供“先求稳定/放大后的 \(N,M\)，再与截面 interaction capacity 比较”的架构启发。
3. 本文件下面的 Z 系列显式 \(N-M\) 相互作用式为 **NZ-SCCM project-derived analytical idealization**，不是周思铭或 Attard 原式。
4. 全部材料强度只取原始输入：混凝土 \(f_c\)、钢材 \(f_y\)、几何 \(t_c,t_s\)、web 体积分数 \(\rho_w\)。不使用 Zhou/FE/试验荷载反标任何系数。

---

## 2. 截面强度理想化

按单位板宽考虑厚度方向截面。定义

\[
h_c=\frac{t_c}{2},\qquad z_f=h_c+\frac{t_s}{2}.
\]

冻结材料强度块：

- 有效混凝土矩阵 \((1-\rho_w)\)：只受压，压应力上限 \(f_c\)，拉区不计；
- 纵向 web 等效钢相 \(\rho_w\)：理想弹塑性，极限应力 \(\pm f_y\)；
- 上、下钢面板：理想弹塑性，极限应力 \(\pm f_y\)；
- 平截面假定。

定义

\[
a_c=(1-\rho_w)f_c.
\]

核心全部受压、两钢面一压一拉时的轴压力为

\[
\boxed{N_0=a_ct_c+\rho_w f_yt_c}.
\]

截面全部受压的 squash load 为

\[
\boxed{N_p=N_0+2f_yt_s}.
\]

---

## 3. 两个精确塑性截面区间

### 3.1 Regime A：中性轴位于 concrete/web core 内，\(n\le N_0\)

定义

\[
K=\frac{a_c+2\rho_wf_y}{2}.
\]

由轴力平衡得

\[
\boxed{
z_n=\frac{a_ch_c-n}{a_c+2\rho_wf_y}
}.
\]

截面塑性抗弯矩为

\[
\boxed{
m_u^{(A)}(n)=K(h_c^2-z_n^2)+2f_yt_sz_f
}.
\]

该式对 \(n\) 是二次式。

### 3.2 Regime B：高压区，中性轴进入低压侧钢面板，\(N_0\le n\le N_p\)

定义低压侧钢面板中的拉应力穿透厚度

\[
\boxed{
\delta=\frac{N_p-n}{2f_y}
}.
\]

于是

\[
\boxed{
m_u^{(B)}(n)=f_y\delta\,[2(h_c+t_s)-\delta]
}.
\]

该式同样对 \(n\) 是二次式。

若 \(n>N_p\)，则触发 squash failure。

因此本容量层不存在高阶材料编译：两个有效区间都只是 \(n\) 的二次函数。

---

## 4. Airy 后屈曲场映射到截面 \(N,M\)

在当前完整两半波的某一纵向半波中心 \(|\sin\beta y|=1\)，取横向坐标

\[
s=\sin(\alpha x),\qquad 0\le s\le1.
\]

其中 \(s=0\) 为侧边，\(s=1\) 为半波横向中线。

第一层 Airy 解给出的加载方向压缩膜力为

\[
\boxed{
n(s;P,q)=\frac{P}{b}+gq(q+2q_0)(1-2s^2)
}
\]

其中

\[
\boxed{
g=\frac{\pi^2}{8\bar A_{22}}}.
\]

加载方向弯矩需求为

\[
\boxed{
m(s;q)=Jqs
}
\]

其中

\[
\boxed{
J=\frac{\pi^2}{b}(D_y+D_\mu)
}.
\]

这里 \(D_\mu\) 采用 Zhou-source 的泊松耦合弯曲刚度；半波中心的 twist 项为零，因此 \(D_{xy}\) 不直接进入该点的 \(M_y\)。

---

## 5. 完整容量条件与“无需空间扫描”证明

定义容量裕度

\[
\boxed{
\Phi(s;P,q)=m_u[n(s;P,q)]-Jqs
}.
\]

材料/截面极限条件为

\[
\boxed{
\min_{0\le s\le1}\Phi(s;P,q)=0
}.
\]

因为

\[
n(s)=a-bs^2
\]

且两个 regime 中 \(m_u(n)\) 均为 \(n\) 的二次式，所以每个光滑 regime 内

\[
\boxed{
\Phi(s)=A_4s^4+A_2s^2+A_1s+A_0
}.
\]

内部驻点严格满足

\[
\boxed{
4A_4s^3+2A_2s+A_1=0
},
\]

即一个 depressed cubic。

因此正式控制位置不需要空间采样。有限候选集合仅包括：

1. \(s=0\)；
2. \(s=1\)；
3. 每个光滑材料区间内上述三次方程的实根 \(0<s<1\)；
4. 若存在，\(n(s)=N_0\) 与 \(n(s)=N_p\) 的材料区间边界点。

在该有限候选集上比较 \(\Phi\) 即得到全横向域的精确控制点。

---

## 6. Z0：控制点进一步降为显式低阶式

Z0 最终控制位置为 \(s_*=1\)，且局部压缩力处于 Regime B：

\[
N_0<n_c<N_p.
\]

于是

\[
\boxed{
n_c(P,q)=\frac{P}{b}-gq(q+2q_0)
},
\]

\[
\boxed{
m_c(q)=Jq
}.
\]

定义

\[
\delta(P,q)=\frac{N_p-n_c(P,q)}{2f_y}.
\]

则第二个联立方程为

\[
\boxed{
F_{cap}(P,q)=f_y\delta(P,q)[2(h_c+t_s)-\delta(P,q)]-Jq=0
}.
\]

该式对 \(P\) 只为二次，对 \(q\) 最高为四次；不存在 R10→N48→C73 高阶爆炸。

还可直接解出

\[
\delta=(h_c+t_s)-\sqrt{(h_c+t_s)^2-\frac{Jq}{f_y}},
\]

进而得到

\[
\boxed{
P_{cap}(q)=b\left[
N_p-2f_y(h_c+t_s)
+2f_y\sqrt{(h_c+t_s)^2-\frac{Jq}{f_y}}
+gq(q+2q_0)
\right]
}.
\]

所以 Z0 的直接极限求解只需：

\[
\boxed{
P_{pb}(q)=P_{cap}(q)
}.
\]

不需要加载步、路径追踪、Newton continuation 或 Ritz 阶数收敛。若要求纯多项式形式，只需平方一次即可消去单个平方根，并对所得有限低阶候选根做原式回代验根。

---

## 7. Z0 原始量与结果

Z0：

\[
b=6000\;\mathrm{mm},\quad t_c=122\;\mathrm{mm},\quad t_s=4\;\mathrm{mm},
\]
\[
f_c=30.4\;\mathrm{MPa},\quad f_y=355\;\mathrm{MPa},\quad \rho_w=0.02,
\]
\[
q_0=0.004.
\]

由 Zhou-source stiffness 与同一截面 extensional stiffness 得：

\[
P_{cr}=78.306708780\;\mathrm{MN},
\]

\[
C=43035.798729\;\mathrm{MN},
\]

\[
N_0=4500.824\;\mathrm{N/mm},\qquad N_p=7340.824\;\mathrm{N/mm},
\]

\[
g=7.469209326\times10^6\;\mathrm{N/mm},
\]

\[
J=2.483849043\times10^7\;\mathrm{N}.
\]

直接联立 \(F_{pb}=0,F_{cap}=0\) 得

\[
\boxed{q_u=0.0034282307},
\]

\[
\boxed{P_u=37.8257068\;\mathrm{MN}}.
\]

控制位置：

\[
\boxed{s_*=1.000000}.
\]

该点

\[
n_*=6011.651\;\mathrm{N/mm},
\]

\[
m_*=85152.076\;\mathrm{N},
\]

\[
\delta=1.872074\;\mathrm{mm},
\]

中性轴位于低压侧 4 mm 钢面板内部，故 Regime B 身份自洽。

Zhou 的 36.94554 MN 未参与任何上式推导或求根；仅在结果释放后做 cross-anchor，对应差异约 +2.38%。

---

## 8. 同一公式、零调参 Z0–Z5 批量核验

每块板均使用自己的原始 \(b,t_c,f_c,E_c,f_y\) 与共同的 \(t_s=4\) mm、\(\rho_w=0.02\)、\(q_0=0.004\)。Zhou 荷载只在最后一列后验比较。

| Case | Pcr (MN) | C (MN) | qu | s* | Pu direct (MN) | Zhou cross-anchor (MN) | posterior diff |
|---|---:|---:|---:|---:|---:|---:|---:|
| Z0 | 78.3067 | 43035.80 | 0.00342823 | 1.000000 | 37.8257 | 36.9455 | +2.382% |
| Z1 | 40.3502 | 35478.24 | 0.00499668 | 0.840295 | 24.7141 | 23.7214 | +4.185% |
| Z2 | 78.3067 | 43035.80 | 0.00432177 | 1.000000 | 42.9590 | 41.2134 | +4.236% |
| Z3 | 81.7974 | 46129.62 | 0.00461341 | 1.000000 | 46.4957 | 44.3203 | +4.908% |
| Z4 | 179.7548 | 80875.43 | 0.00244543 | 1.000000 | 70.2657 | 69.3399 | +1.335% |
| Z5 | 231.7884 | 14345.27 | 0.000258842 | 1.000000 | 14.1182 | 14.6816 | -3.838% |

后验相对 Zhou 统计：

\[
\boxed{\text{mean signed}=+2.201\%},
\]

\[
\boxed{\text{MAE}=3.481\%},
\]

\[
\boxed{\text{RMSE}=3.691\%}.
\]

Z1 的 \(s_*=0.840295\) 是重要审计结果：正式理论不能把控制位置硬编码为板中线；必须保留第 5 节的有限三次驻点检查。该检查仍然是有限代数问题，不引入空间离散或阶数层级。

---

## 9. 第二生死门裁决

### 9.1 可计算性

\[
\boxed{
F_{pb}(P,q)=0+F_{cap}(P,q)=0
}
\]

对 Z steel-shell concrete 可以保持为低阶直接代数系统：

- 几何后屈曲：三次；
- 截面容量：分区二次 \(m_u(n)\)；
- 横向控制位置：每区一个三次驻点方程 + 有限边界候选；
- Z0 控制分支甚至可显式写成 \(P_{cap}(q)\)；
- 无加载步；
- 无路径追踪；
- 无 H6/H60；
- 无正式空间 quadrature；
- 无经验折减参数。

因此：

\[
\boxed{
\mathrm{Z\ SECOND\ GATE}=\mathrm{STRONG\ PASS}
}
\]

### 9.2 尚未被证明的范围

本结果 **不等于整套理论已对 RC/Swartz24 通过**。RC 必须单独建立与钢筋层相容的 reinforced-concrete \(N-M\) 低阶容量式并接受同一“不得路径追踪、不得高阶爆炸”的门禁。

此外，本 Z 容量式使用的是 rigid-perfectly-plastic/no-tension section capacity，而不是 NC-M6 全场 current operator。其物理身份是：

`ELASTIC/ORTHOTROPIC GEOMETRIC POSTBUCKLING + EXPLICIT ULTIMATE SECTION INTERACTION`。

这是有意的理论分层，而不是把 NC-M6 隐藏进经验系数。

### 9.3 验证身份

当前 Z0–Z5 只与 Zhou 结果作 cross-anchor；Zhou 本身不是 FE/试验 ultimate truth。因此 +2.2% mean / 3.48% MAE 只能说明公式量级和参数趋势良好，不能替代对真正 deterministic FE benchmark 的最终验证。

---

## 10. 唯一下一生死门

若继续，只做 RC：

> 能否用相同原则，从 concrete no-tension/compression block + discrete reinforcement layers 解析得到低阶 reinforced-concrete \(N-M\) interaction，并与已冻结的 cubic \(F_{pb}\) 联立，直接求 Swartz24 的 \(P_u,q_u\)？

若 RC 容量层再次出现高阶材料编译或必须荷载路径追踪，则该统一路线在 RC 处立即停止。
