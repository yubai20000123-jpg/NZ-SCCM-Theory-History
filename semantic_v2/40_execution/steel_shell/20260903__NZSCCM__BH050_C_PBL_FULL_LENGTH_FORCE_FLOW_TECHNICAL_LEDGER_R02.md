# NZ-SCCM / BH050 — C1-PBL 全长度纵向部分组合与 `C_P` 力流技术总账 R02

- 日期：2026-09-03
- 身份：**diagnostic / theory-development ledger**
- GitHub 目标分支：`diagnostic/bh032-bh050-mode-projection-20260827`
- production/main：**不修改**
- 理论文件优先级：**本文件 > 同名实现代码 > CSV 数值输出**
- 本文件不使用 FE 反标 `C_P`，不把任何历史/FE `P_u` 用作求根目标。
- 本轮执行目标：把 R01 的局部谐波 `C_P` 核提升为 BH050 5000 mm 全长度力流问题，明确 `A_weld`、`A_emb`、孔洞/混凝土榫、`C_w,C_e,C_P` 的身份，给出 `K_s,K_c,K_eq`、`s(y),t_P(y),ΔN_s,ΔN_c`、精确积分矩阵与最终 Schur 凝聚；同时执行参数化 `C_P` 的**力流/切线前置诊断**。

> **R02 最重要的新结论**：在钢壳与 UHPC 两条纵向受力路径的端部位移相同、局部几何缩短场 `g(y)` 已给定时，`C_P` 本身不能改变两相的**全长度平均轴力分担**；它改变的是 slip、PBL 传力剪应力、局部轴力起伏与局部/凝聚切线。要让 UHPC 平均分担随 `C_P` 发生变化，`C_P` 必须通过 C1 局部幅值、当前钢壳切线、非线性 UHPC 或端部力流条件反向改变 `g(y)`/current operator。因而不能再把 `C_P` 当作一个直接把 UHPC 比例从 54%“旋钮式调到”60–65% 的参数。

---

## 1. 本轮来源与冻结边界

### 1.1 BH050 raw input

采用当前 R13/R14 同源 BH050 输入：

- `B = 2500 mm`
- `L = 5000 mm`
- `t_c = 42 mm`
- `t_s = 4 mm`
- `A_w = 1332 mm²`
- `E_s = 206000 MPa`
- `ν_s = 0.30`
- `f_y = 355 MPa`
- `E_c = 43400 MPa`
- `ν_c = 0.20`
- `f_c = 141.1 MPa`
- `ε_c0 = 0.0035`
- `L_x = 562.5 mm`
- `L_y = 5000/9 = 555.555555556 mm`
- `A_{0,l} = 0.3515625 mm`.

来源锚点：

- `NZSCCM_R13_UCFT_BH005_BH100_严格输入映射_R01_20260902.md`
- `NZSCCM_钢壳UHPC_AI预测技术文本_R01_20260831.txt`
- `20260902__NZSCCM__STEEL_SHELL_UHPC_CENTRAL_TECHNICAL_LEDGER_R14_MINIMAL_TERMINAL_CORRECTION.md`

其中当前 `A_w=1332 mm²` 仍是 R14 的 longitudinal web/PBL steel area 输入，不改写成经验有效面积。

### 1.2 保持冻结的 R14 外层

本轮不重开：

\[
Q=q(q+2q_0),
\]

\[
P(q)=P_{cr}\frac{q}{q+q_0}+C_AQ,
\]

以及四个 outer generalized N–M balance：

\[
R_1=N_x-N_x^A,
\quad
R_2=M_x-M_x^A,
\quad
R_3=N_y-N_y^A,
\quad
R_4=M_y-M_y^A.
\]

但当纵向部分组合内部变量正式并入时，终点的 tangent 必须使用凝聚后的 `J4_cond`，不能继续使用未凝聚的旧 `J4`。

### 1.3 C1 local layer

继续采用当前优先假设：

\[
w_s(x_i,y)=W_c(x_i,y),
\qquad
w_{s,n}(x_i,y)=W_{c,n}(x_i,y),
\]

不要求：

\[
w_{s,nn}=W_{c,nn}.
\]

每个 bay 保留独立局部幅值 `A_b`。本轮**不**用旧 R02 单一幅值替代正式 C1 多 bay 幅值；旧 R02 `U_±` 只在第 8 节用于建立一个可复算的 BH050 forcing-scale audit。

---

## 2. PBL 纵向传力的几何变量账本

本轮必须把“真实几何来源”和“暂未锁定的几何”分开。

| 符号 | 物理身份 | BH050 当前状态 | 不允许的替代 |
|---|---|---|---|
| `A_w` | 当前 R14 longitudinal web/PBL steel area | **LOCKED = 1332 mm²** | 不得改成 `A_eff` |
| `A_weld` | 一个 PBL 传力路径内焊缝的有效剪切/传力面积 | **SOURCE_UNLOCKED_FOR_BH050** | 不从 FE 反标 |
| `A_emb` | PBL 埋置/钢板或构造件对 UHPC 的实际传力面积 | **SOURCE_UNLOCKED_FOR_BH050** | 不凭经验给“有效面积” |
| `d_h` | PBL 孔径 | **SOURCE_UNLOCKED_FOR_BH050** | 不拿其他试件孔径代入 |
| `s_h` | 孔洞/混凝土榫轴向间距 | **SOURCE_UNLOCKED_FOR_BH050** | 不用 `L_y` 自动冒充孔距 |
| `n_h` | 一个 reference cell 内参与传力的孔/榫数 | **SOURCE_UNLOCKED_FOR_BH050** | 不由网格数推定 |
| `t_p` | PBL rib/web 实际厚度 | 需从 source geometry 锁定；当前 `A_w` 已知但不足以唯一反推全部构造 | 不从 `A_w` 唯一反演连接细节 |

当前资料能证明 PBL 既是加劲构造也是 steel–UHPC 连接通道，并存在有限 load–slip 刚度的物理可能性；但当前 BH050 的 `A_weld,A_emb,d_h,s_h,n_h` 尚未形成 source-locked 数值合同。因此 R02 **不虚构这些数值**。

---

## 3. `C_w`、`C_e`、`C_P` 的严格身份

### 3.1 连续线刚度与 cell-lumped 刚度

定义纵向相对滑移：

\[
s(y)=u_s(y)-u_c(y).
\]

定义 distributed line coupling：

\[
t_P(y)=k_P s(y),
\]

其中

\[
[k_P]=\mathrm{N/mm^2},
\qquad
[t_P]=\mathrm{N/mm}.
\]

对 reference axial length `L_r` 定义：

\[
\boxed{C_P=k_P L_r},
\qquad [C_P]=\mathrm{N/mm}.
\]

本轮扫参取 `L_r=L_y=5000/9`。

### 3.2 焊缝路径 `C_w`

若焊缝可由弹性剪切能直接闭合，则一个 cell 的 weld tangent 可写为：

\[
C_w=\frac{\partial T_w}{\partial s_w}.
\]

在已明确焊缝类型、有效喉厚、传力长度与剪切路径长度后，才可进一步由类似

\[
C_w\sim \frac{G_w A_{weld}}{\ell_w}
\]

的几何—材料能量式获得。R02 只固定**能量/切线定义**，不在 BH050 几何未锁定时把右式中的几何量猜成数值。

### 3.3 埋置/孔洞/混凝土榫路径 `C_e`

对单个孔洞/混凝土榫或埋置传力单元：

\[
K_h^t=\frac{dT_h}{ds_h}.
\]

若 reference cell 内有若干相互并联的离散传力点：

\[
\boxed{C_e=\sum_{h=1}^{n_h}K_h^t}.
\]

其等效 distributed stiffness 为：

\[
k_e=\frac{C_e}{L_r}.
\]

`K_h^t` 应由真实构造几何/材料能量或 source-grade load–slip law 得到；不能由 BH050 FE 峰值反标。

### 3.4 sequential path 不是简单相加

若纵向力必须依次通过：

`steel shell → weld → PBL rib → embedded/dowel transfer → UHPC`，

则 weld 与 embedded/dowel 是**串联柔度**。对一个 sequential path：

\[
\boxed{
\frac1{C_{P,path}}=
\frac1{C_w}+\frac1{C_e}
}
\]

（若还需显式 rib shear/axial compliance，则继续把对应 `1/C_r` 加入）。

若存在多条独立路径并联：

\[
\boxed{C_P=\sum_p C_{P,path}^{(p)}}.
\]

因此 R01 中的 `C_P` 是**最终等效纵向连接切线**，不是 `C_w+C_e` 的无条件定义。

---

## 4. 全长度两相部分组合作用：从能量到平衡

先写最小 steel-faces ↔ UHPC 两相主核。web/PBL 的独立纵向轴力仍保留在 R14 constituent ledger 中，不在本节吞并为 UHPC 面积。

令：

\[
N_s=K_s(u_s'+g),
\qquad
N_c=K_cu_c',
\]

其中：

- `K_s`：两张 steel faces 的当前纵向 resultant tangent；
- `K_c`：UHPC 当前纵向 resultant tangent；
- `g(y)`：由 C1/R02 局部面外变形产生的 steel geometric axial-shortening mismatch；
- `s=u_s-u_c`。

最小相对能量：

\[
\boxed{
\Pi_{ax}
=
\frac12\int_0^L K_s(u_s'+g)^2dy
+
\frac12\int_0^L K_cu_c'^2dy
+
\frac12\int_0^L k_P(u_s-u_c)^2dy
}.
\]

变分得到：

\[
\boxed{N_s'=t_P=k_Ps},
\]

\[
\boxed{N_c'=-t_P=-k_Ps}.
\]

因此：

\[
\boxed{(N_s+N_c)'=0}.
\]

总纵向合力沿 `y` 自动守恒。

两式相减得到 slip governing equation：

\[
\boxed{
s''-\beta^2s=-g'
}
\]

其中：

\[
\boxed{
\beta^2=k_P\left(\frac1{K_s}+\frac1{K_c}\right)
=\frac{k_P}{K_{eq}}
}
\]

以及：

\[
\boxed{
K_{eq}=\frac{K_sK_c}{K_s+K_c}
},
\qquad
\boxed{
\ell_t=\frac1\beta=\sqrt{\frac{K_{eq}}{k_P}}
}.
\]

`ell_t` 是纵向力重新分配/滑移衰减的物理长度尺度。

---

## 5. R02 harmonic forcing 的全长度精确解

历史 R02-compatible local mode：

\[
\phi=(1-\cos k_xx)(1-\cos k_yy),
\qquad
k_y=\frac{2\pi}{L_y}.
\]

对一个 face，横向平均后的 geometric mismatch：

\[
\bar g_y(y)
=\frac34 d k_y^2\sin^2(k_yy)
=c_y d[1-\cos(2k_yy)],
\]

其中：

\[
d=U^2-A_{0,l}^2,
\qquad
c_y=\frac{3k_y^2}{8}.
\]

因为 `k_y=2π/L_y`，波动项在一个 local cell 内为 `n=4`：

\[
g_f(y)=g_n\cos\frac{4\pi y}{L_y}.
\]

取：

\[
s(y)=S_n\sin\frac{n\pi y}{L_r},
\qquad
n=4,
\]

则精确积分：

\[
\int_0^{L_r}s^2dy=\frac{S_n^2L_r}{2},
\]

\[
\int_0^{L_r}(s')^2dy=\frac{S_n^2n^2\pi^2}{2L_r},
\]

\[
\int_0^{L_r}s'g\,dy=\frac{S_ng_nn\pi}{2},
\]

\[
\int_0^{L_r}g^2dy=\frac{g_n^2L_r}{2}.
\]

令：

\[
\Lambda=\frac{k_PL_r^2}{K_{eq}}
=\frac{C_PL_r}{K_{eq}},
\]

stationarity 给出：

\[
\boxed{
S_n=-\frac{g_nn\pi L_r}{n^2\pi^2+\Lambda}
}.
\]

因此连接动员率：

\[
\boxed{
\eta_n=\frac{\Lambda}{n^2\pi^2+\Lambda}
},
\]

slip relief：

\[
\boxed{
r_n=\frac{n^2\pi^2}{n^2\pi^2+\Lambda}
}.
\]

### 5.1 5000 mm 全长度等价性

BH050 有 `9` 个轴向 local cells。若相同 R02 forcing 连续重复，则：

\[
L=9L_y=5000\ \mathrm{mm},
\qquad n_{full}=9\times4=36.
\]

同一物理 `k_P` 下：

\[
\Lambda_{full}
=\frac{k_PL^2}{K_{eq}}
=81\Lambda_{cell}.
\]

所以：

\[
\eta_{36}^{full}
=
\frac{81\Lambda}{36^2\pi^2+81\Lambda}
=
\frac{\Lambda}{16\pi^2+\Lambda}
=
\eta_4^{cell}.
\]

这说明本轮 sweep 虽使用 `L_y` 作为 normalization length，但它是 **5000 mm 全长度连续谐波解的严格等价表达**，不是把 9 个 cell 独立算完再平均。

---

## 6. 关键理论更正：`C_P` 不直接改变平均力分担

这是 R02 相对 R01 最重要的修正。

若钢壳与 UHPC 在两端具有共同纵向位移：

\[
u_s(0)=u_c(0),
\qquad
u_s(L)=u_c(L),
\]

则：

\[
s(0)=s(L)=0.
\]

令共同平均轴向位移梯度：

\[
\bar e=\frac{u_s(L)-u_s(0)}{L}
=\frac{u_c(L)-u_c(0)}{L}.
\]

对 constitutive resultants 全长度积分：

\[
\boxed{
\bar N_s=K_s(\bar e+\bar g)
}
\]

以及：

\[
\boxed{
\bar N_c=K_c\bar e
}.
\]

这两个式子里**没有 `k_P` 或 `C_P`**。

若总平均合力 `\bar N=\bar N_s+\bar N_c` 给定，则：

\[
\boxed{
\bar e=\frac{\bar N-K_s\bar g}{K_s+K_c}
}
\]

进而：

\[
\boxed{
\bar N_s
=K_s\left(\frac{\bar N-K_s\bar g}{K_s+K_c}+\bar g\right)
}
\]

\[
\boxed{
\bar N_c
=K_c\frac{\bar N-K_s\bar g}{K_s+K_c}
}.
\]

所以，在 `g(y)` 和端部共同位移条件固定时：

\[
\boxed{
\frac{\partial \bar N_s}{\partial C_P}=0,
\qquad
\frac{\partial \bar N_c}{\partial C_P}=0.
}
\]

这并不意味着 PBL 刚度“不重要”。因为：

\[
C_P\rightarrow s(y),t_P(y),N_s(y)-\bar N_s,N_c(y)-\bar N_c
\]

仍然显著变化；这些局部场进入 C1 amplitude stationarity、R06 current steel tangent、UHPC material event 和最终 condensed `J4` 后，**才可能间接改变** `q_*` 与最终承载力。

因此正确因果链是：

\[
\boxed{
C_P
\rightarrow
\text{local slip/transfer field}
\rightarrow
A_b\text{ 与 current tangents}
\rightarrow
\bar g\text{ / section resultants}
\rightarrow
J_{4,cond}
\rightarrow
q_*\rightarrow P_u
}
\]

而不是：

\[
C_P\rightarrow\text{直接指定 UHPC 60--65\%}\rightarrow P_u.
\]

---

## 7. BH050 截面设计基准：先把“原始分担比例”算清楚

对纯轴压、弹性、共同应变的截面设计基准，按当前 R14 constituent identities：

UHPC reduced-core stiffness per unit width：

\[
K_c^{sec}
=E_c(1-\rho_w)t_c
=1,799,676.48\ \mathrm{N/mm}.
\]

两张 steel faces：

\[
K_s^{sec}=2E_st_s
=1,648,000.00\ \mathrm{N/mm}.
\]

web/PBL longitudinal path：

\[
K_w^{sec}=E_s\frac{A_w}{B}
=109,756.80\ \mathrm{N/mm}.
\]

总刚度：

\[
K_T^{sec}=3,557,433.28\ \mathrm{N/mm}.
\]

因此弹性共同应变设计分担为：

\[
\boxed{\eta_c^{sec}=50.5892\%}
\]

\[
\boxed{\eta_{s,faces}^{sec}=46.3255\%}
\]

\[
\boxed{\eta_w^{sec}=3.0853\%}.
\]

这回答了此前“分担比例是否能从截面设计得到”的问题：**可以得到屈曲前的 `EA` 基准，但不是后屈曲全过程比例。**

当前 C1 diagnostic 的 UHPC 约 `54.23%` 已比这个弹性截面基准高约 `3.64` 个百分点。因此当前理论并非“完全没有发生 steel→UHPC 重分配”。

---

## 8. BH050 forcing-scale audit：旧 R02 幅值能解释多少当前 54%？

这一节只做 cross-ledger diagnostic，不把旧 R02 幅值冒充当前 C1 幅值。

冻结 R02/R06 regression 可复算幅值：

\[
U_+=0.1692668858\ \mathrm{mm},
\qquad
U_-=2.9398459145\ \mathrm{mm}.
\]

得到：

\[
\bar g_+=-4.5541540\times10^{-6},
\]

\[
\bar g_-=4.0862941\times10^{-4},
\]

两面 aggregate mean：

\[
\boxed{
G_0=\frac{\bar g_++\bar g_-}{2}
=2.0203763\times10^{-4}
}.
\]

用当前 C1 diagnostic 总纵向合力 `-5194.45 N/mm`，并暂保留其 web resultant `-162.60 N/mm`，将剩余合力交给 steel faces ↔ UHPC 两相公共端位移平衡，可得：

\[
\bar e=-1.5560648\times10^{-3},
\]

\[
\bar N_{s,faces}=-2231.437\ \mathrm{N/mm},
\]

\[
\bar N_c=-2800.413\ \mathrm{N/mm},
\]

对应总荷载分担：

\[
\eta_c=53.9116\%,
\quad
\eta_{s,faces}=42.9581\%,
\quad
\eta_w=3.1303\%.
\]

当前 C1 diagnostic 是约：

`UHPC 54.23% / steel faces 42.64% / web 3.13%`。

两者在 UHPC 分担上只差约 `0.32` 个百分点。**这不是正式验证**，因为混用了旧 R02 amplitudes 与当前 C1 resultant level；但它给出一个很强的方向性证据：当前 54% 左右的平均分担，主要量级已经可以由“局部几何缩短 `\bar g` + 共同端部相容”解释，并不需要把 `C_P` 直接当平均分担旋钮。

### 8.1 60–65% 真正意味着什么

在上述同一 force level / elastic audit closure 下，如果只问“要达到某个 UHPC 平均分担，所需 aggregate mean geometric mismatch `\bar g` 多大”，则：

| UHPC share | required `bar g` | 相对当前 forcing-scale `G0` | equivalent two-face RMS `U`* |
|---:|---:|---:|---:|
| 54.23% | 2.2146e-4 | 1.096 | 2.177 mm |
| 56% | 3.2814e-4 | 1.624 | 2.639 mm |
| 58% | 4.4890e-4 | 2.222 | 3.079 mm |
| 60% | 5.6967e-4 | 2.820 | 3.464 mm |
| 62% | 6.9044e-4 | 3.417 | 3.810 mm |
| 65% | 8.7159e-4 | 4.314 | 4.277 mm |

`*` 仅定义为满足 `bar g = c_y(U_rms²-A0²)` 的等效两面 RMS amplitude；不是实际 C1 bay amplitude。

所以 60–65% 并非通过“选一个 `C_P` 数值”直接得到；它要求局部幅值/几何缩短或 current constitutive state 出现足够大的变化。`C_P` 若能推动这种变化，只能通过 C1 coupling 间接实现。

---

## 9. 执行的 BH050 全长度 `C_P` 参数化 sweep

### 9.1 本轮 normalization

本节只取 **两张 steel faces ↔ UHPC** 的 full-width transfer kernel；web/PBL 自身轴力路径保持独立，不并入 UHPC。

\[
K_s=2E_st_sB=4.120000000\times10^9\ \mathrm N,
\]

\[
K_c=E_c(1-\rho_w)t_cB
=4.499191200\times10^9\ \mathrm N,
\]

\[
\boxed{
K_{eq}=2.150627282\times10^9\ \mathrm N
}.
\]

因此以 `L_r=L_y`：

\[
\boxed{
C_0=\frac{K_{eq}}{L_y}
=3.871129108\ \mathrm{MN/mm}
}.
\]

注意：该 `C_P` 是 full-width aggregate normalization。它与 R01 的 “per-face, one-interior-bay” `C_P` 数值不能直接横比；应比较 dimensionless `\Lambda=C_P/C_0`。

### 9.2 sweep 结果

以下全部由闭式公式计算，无空间数值积分：

| `Lambda` | `C_P` (MN/mm) | `eta_4` | transfer length `ell_t` (mm) | `s_max` (mm) | `t_P,max` (kN/mm) | `Delta Ns amp/B` (N/mm) |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0.000 | 0.000000 | inf | 0.008932 | 0.000000 | 0.000 |
| 0.1 | 0.387 | 0.000633 | 1756.821 | 0.008926 | 0.006220 | 0.110 |
| 1 | 3.871 | 0.006293 | 555.556 | 0.008876 | 0.061847 | 1.094 |
| 5 | 19.356 | 0.030691 | 248.452 | 0.008658 | 0.301642 | 5.334 |
| 10 | 38.711 | 0.059554 | 175.682 | 0.008400 | 0.585320 | 10.351 |
| 20 | 77.423 | 0.112414 | 124.226 | 0.007928 | 1.104843 | 19.538 |
| 40 | 154.845 | 0.202108 | 87.841 | 0.007127 | 1.986388 | 35.127 |
| 80 | 309.690 | 0.336256 | 62.113 | 0.005929 | 3.304839 | 58.442 |
| `16pi²=157.914` | 611.304 | 0.500000 | 44.210 | 0.004466 | 4.914166 | 86.902 |
| 200 | 774.226 | 0.558794 | 39.284 | 0.003941 | 5.492012 | 97.120 |
| 500 | 1935.565 | 0.759978 | 24.845 | 0.002144 | 7.469317 | 132.087 |
| 1000 | 3871.129 | 0.863622 | 17.568 | 0.001218 | 8.487965 | 150.100 |

解释：

- `C_P ↑`：slip amplitude `s_max ↓`；
- `C_P ↑`：PBL transfer shear `t_P,max ↑`；
- `C_P ↑`：局部 steel/core axial-force oscillation amplitude `ΔN ↑`；
- 但在本节固定 `g(y)` 与共同端部位移条件下，**全长度平均 `bar N_s/bar N_c` 不变**。

这就是 `C_P` 的正确第一层物理身份：**局部力流传递长度与局部 current state 控制参数，而不是直接的平均分配参数。**

---

## 10. 精确 line-element 积分矩阵：作为实现审计，不作为正式空间离散

对长度 `L_e` 的一维线段：

\[
\mathbf d_e=
[u_{s1},u_{s2},u_{c1},u_{c2}]^T.
\]

线性 shape functions 的两个 exact integrals：

\[
\boxed{
\int_0^{L_e}\mathbf B^T\mathbf B\,dy
=
\frac1{L_e}
\begin{bmatrix}
1&-1\\-1&1
\end{bmatrix}
}
\]

和：

\[
\boxed{
\int_0^{L_e}\mathbf N^T\mathbf N\,dy
=
\frac{L_e}{6}
\begin{bmatrix}
2&1\\1&2
\end{bmatrix}
}.
\]

因此：

\[
\mathbf K_s^e=
\frac{K_s}{L_e}
\begin{bmatrix}
1&-1&0&0\\
-1&1&0&0\\
0&0&0&0\\
0&0&0&0
\end{bmatrix},
\]

\[
\mathbf K_c^e=
\frac{K_c}{L_e}
\begin{bmatrix}
0&0&0&0\\
0&0&0&0\\
0&0&1&-1\\
0&0&-1&1
\end{bmatrix},
\]

\[
\boxed{
\mathbf K_P^e=
\frac{k_PL_e}{6}
\begin{bmatrix}
2&1&-2&-1\\
1&2&-1&-2\\
-2&-1&2&1\\
-1&-2&1&2
\end{bmatrix}
}.
\]

对 element-constant geometric mismatch `g`：

\[
\boxed{
\mathbf f_g^e
=K_sg[-1,1,0,0]^T
}.
\]

这些式子是**精确积分恒等式**，可用于代码核对；本轮正式 sweep 采用第 5 节连续谐波闭式解，不把 9 个 line elements 当成 formal spatial discretization。

### 10.1 横向 bay interpolation 的 exact matrix identity

若一个分布式 interfacial field 在两条 PBL line 之间线性插值：

\[
s_b(x,y)=(1-r)s_i(y)+rs_{i+1}(y),
\qquad
r=\frac{x-x_i}{b_i},
\]

则：

\[
\boxed{
\int_{x_i}^{x_{i+1}}
\begin{bmatrix}1-r\\r\end{bmatrix}
\begin{bmatrix}1-r&r\end{bmatrix}dx
=\frac{b_i}{6}
\begin{bmatrix}2&1\\1&2\end{bmatrix}
}.
\]

但必须区分：**离散 PBL line connector 应在真实 PBL lines 上组装；只有真实分布式 interfacial field 才使用上述横向分布矩阵。**

---

## 11. 从两相最小核升级到真实 upper/lower/core 多路径

真正 C1-PBL 需要至少允许：

\[
s_+=u_+-u_c,
\qquad
s_-=u_--u_c.
\]

对上下钢面刚度相同、connector tangent 相同的解释性分解：

\[
u_a=\frac{u_++u_-}{2},
\qquad
\delta=\frac{u_+-u_-}{2},
\]

\[
g_a=\frac{g_++g_-}{2},
\qquad
g_d=\frac{g_+-g_-}{2}.
\]

其中：

- `symmetric mode` 控制 steel aggregate ↔ UHPC 的纵向重分配；
- `antisymmetric mode` 控制 upper/lower steel face 的轴向不对称。

在最简线弹性解释中可得到两个 slip-length operators；但正式 R02 后续不能把 `K_s,K_c` 固定为初始 `EA`，必须使用 current consistent tangent resultants，而且 web/PBL 自身的 longitudinal operator 不能被重复计入 connector stiffness。

---

## 12. C1 amplitude 与 `C_P` 真正耦合的位置

对每个 bay：

\[
g_b=g_b(A_b,q,\mathbf x),
\]

因此：

\[
\Pi_{ax}
=\Pi_{ax}(\mathbf x,\mathbf A,\mathbf s;C_P).
\]

局部 stationarity：

\[
\boxed{
R_{A_b}=\frac{\partial\Pi}{\partial A_b}=0
}
\]

和 slip stationarity：

\[
\boxed{
R_s=\frac{\partial\Pi}{\partial\mathbf s}=0
}.
\]

于是 `C_P` 才能通过：

\[
\frac{\partial R_A}{\partial s},
\quad
\frac{\partial R_s}{\partial A},
\quad
\frac{\partial R_s}{\partial\mathbf x}
\]

真正反馈到 local amplitude 与 outer section state。

这一步是后续得到真实 `P_u(C_P)` 的必要条件。

---

## 13. 最终 Jacobian 与 exact Schur condensation

定义：

\[
\mathbf x=
[\varepsilon_x^0,\kappa_x,\varepsilon_y^0,\kappa_y]^T,
\]

`A` 为所有 C1 bay local amplitudes，`s` 为所有 longitudinal partial-interaction internal coordinates。

完整 current Jacobian：

\[
\boxed{
\mathbf J=
\begin{bmatrix}
\mathbf J_{xx}&\mathbf J_{xA}&\mathbf J_{xs}\\
\mathbf J_{Ax}&\mathbf J_{AA}&\mathbf J_{As}\\
\mathbf J_{sx}&\mathbf J_{sA}&\mathbf J_{ss}
\end{bmatrix}
}.
\]

内部变量块：

\[
\mathbf J_{ll}=
\begin{bmatrix}
\mathbf J_{AA}&\mathbf J_{As}\\
\mathbf J_{sA}&\mathbf J_{ss}
\end{bmatrix}.
\]

精确凝聚：

\[
\boxed{
\mathbf J_{4,cond}
=
\mathbf J_{xx}
-
\begin{bmatrix}\mathbf J_{xA}&\mathbf J_{xs}\end{bmatrix}
\mathbf J_{ll}^{-1}
\begin{bmatrix}\mathbf J_{Ax}\\\mathbf J_{sx}\end{bmatrix}
}.
\]

terminal 仍按当前 R14 rule：

- connected equilibrium branch 上第一个 material-domain event；或
- 凝聚后的 `J4_cond` first admissible fold；

谁先发生谁控制。

因此正式 structural fold 应检查：

\[
R_4=0,
\qquad
J_{4,cond}v=0,
\qquad
v^Tv=1.
\]

---

## 14. 本轮执行状态与硬边界

### 已完成

1. `A_weld/A_emb/孔洞/混凝土榫` 的物理身份与 source-lock status 已写清；未锁定项没有猜数值。
2. `C_w,C_e,C_P` 的串/并联关系与单位已闭合。
3. `K_s,K_c,K_eq`、`s(y)`、`t_P(y)`、`ΔN_s/ΔN_c` 的全长度连续控制方程已闭合。
4. 证明了共同端位移 + 固定 `g(y)` 下平均 force share 对 `C_P` 严格不敏感。
5. 得到 BH050 当前截面弹性设计 baseline：UHPC `50.589%` / steel faces `46.326%` / web `3.085%`。
6. 用冻结 R02 amplitudes 做了 cross-ledger forcing-scale audit，得到 UHPC `53.912%`，与当前 C1 diagnostic `54.23%` 在量级上接近。
7. 执行了 5000 mm 全长度等价 harmonic `C_P` sweep，得到 slip / transfer shear / local force oscillation 的闭式参数曲线。
8. 给出了 exact line-element integration matrices 与最终 global Schur condensation。

### 仍未完成，因此不得宣称 `P_u(C_P)`

1. BH050 current C1 的全部 `A_b(q,x,C_P)` 尚未 source-locked/synchronized 成可执行 residual family；
2. `A_weld,A_emb,d_h,s_h,n_h` 的 BH050 source-grade 几何尚未锁定，因此 `C_P` 仍是**物理可解释的 continuation parameter**，不是已确定设计值；
3. R06 steel current tangent 必须与 C1 amplitude + slip stationarity 同源；不能把旧 first-yield frozen mean resultant直接当新 tangent；
4. full multi-bay / upper-lower asymmetric internal block 的 exact condensation 尚待编译；
5. 只有上述闭合后，才能沿同一 connected branch 对每个 `C_P` 找 first admissible terminal 并称为：

\[
\boxed{P_u(C_P)}.
\]

---

## 15. R02 对下一步的唯一指向

下一步不再继续做“`C_P` → 平均 UHPC 比例”的代数比例扫参，因为 R02 已证明该关系在固定 `g` 下不存在。

唯一有物理意义的下一步是：

\[
\boxed{
C_P
\rightarrow
\text{C1 bay amplitude stationarity}
\rightarrow
\bar g(A_b)
\rightarrow
\text{steel/core current resultants}
\rightarrow
J_{4,cond}
\rightarrow
q_* / P_*
}
\]

也就是说：**把纵向 partial interaction 插入 C1 current operator 本身，而不是插入最终 force-share 百分比。**

---

## 16. 同步实现文件

- `NZSCCM_BH050_C_PBL_full_length_force_flow_kernel_R02.py`
- `NZSCCM_BH050_C_PBL_full_length_CP_sweep_R02.csv`

代码只实现本文件已经写明的闭式核和数值审计，不拥有独立理论身份。
