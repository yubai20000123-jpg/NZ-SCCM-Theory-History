# NZ-SCCM — BH050 qU-R06 有限 Fourier 全驻值认证 + 原五方程 contact 复算 R01

**Time:** 2026-08-27 17:30 +08:00  
**Parent current identity:** `20260827_1648` restored Airy-demand -> terminal N-M capacity contact  
**Certificate backend:** `20260827_1730__NZSCCM__Q_U_R06_FINITE_FOURIER_STATIONARY_CERTIFICATE_R01.py`  
**Status:** `BH050 qU-ON FORMAL LOCAL-MISES CERTIFICATE PASS / FIVE-EQUATION CONTACT RECLOSED / NO SPATIAL OPTIMIZER / NO QUADRATURE`

---

# 0. 本节点只做什么

本节点不再修改任何结构理论、材料本构、terminal 变量身份或 Airy 方程。

保持：

```text
Airy P(q), Nx^d, Ny^d, Mx^d, My^d = unchanged
terminal (Ax,Bx,Ay,By) = N-M capacity-surface parameters
UHPC S0/S1 exact N-M = unchanged
web exact affine ideal-EP resultant = unchanged
qU = only inside steel-face R02/R06
R06 = first local-Mises yield -> whole-width R02 mean resultant
```

本次唯一任务：

> 把 20260827 16:48 qU-on BH050 中用于 R06 的临时 L-BFGS 连续空间极值搜索，替换为对完整 GL+LL 有限 Fourier 应力场的全驻值根认证，然后重新闭合原始 5×5 terminal contact。

明确：

```text
NUMERICAL_SPATIAL_QUADRATURE = 0
NUMERICAL_THICKNESS_QUADRATURE = 0
MATERIAL_POINTS = 0
L_BFGS / MINIMIZE = 0
SPATIAL_GRID = 0
COMPARATOR_IN_ROOT = 0
```

本证书使用 Taylor/Krawczyk root isolation 来证明有限驻值方程的全部根已被枚举。root-isolation enclosure 只用于证明 `dPhi/dx=dPhi/dy=0` 是否存在根，不用于任何应力/合力积分，也不建立材料点或结构空间子域。改变 enclosure 宽度只改变证明精度，不改变 operator 值。

---

# 1. 为什么 qU-on 以后不能继续硬套旧 degree-6 `Phi(u,v)`

旧 R06（LL-only）在局部坐标

\[
u=\cos(k_xx),\qquad v=\cos(k_yy)
\]

下，Mises 平方

\[
\Phi=\sigma_x^2-\sigma_x\sigma_y+\sigma_y^2+3\tau^2
\]

可化成总次数不超过 6 的有限多项式。

打开 exact qU GL 后，局部场同时包含：

- local frequency `kx = (80/9) pi/B`, `ky = 9 pi/B`；
- global frequency `pi/B`。

二者是有理可公度的，但 GL 产生 `local +/- global` 频率。因此若强制仍只用旧 `(u,v)` degree-6 polynomial，会丢掉 qU GL 的真实局部应力波动，这是不允许的。

本次改为完整有限 Fourier/Laurent 表示。采用归一化坐标

\[
\bar x=x/B,\qquad \bar y=y/B,
\]

取 x 基频 `pi/(9B)`、y 基频 `pi/B`，则所有 qU+LL 频率都是整数：

\[
\exp\{i[m\pi\bar x/9+n\pi\bar y]\}.
\]

对 BH 注册单元，单个 stress component 的有限频率范围为：

```text
x integer index max = 160
y integer index max = 18
```

Mises 平方 `Phi` 因二次乘积扩大为：

```text
x integer index max = 320
y integer index max = 36
Laurent nonzero terms = 441
conjugate-paired real trig terms = 220
```

所以 qU-on R06 仍然是严格**有限解析场**；只是不能再假装成旧 degree-6 `(u,v)` polynomial。

---

# 2. 正式有限候选集

固定一个 R02/R06 face state 后，`Phi(xbar,ybar)` 已经是有限 Fourier polynomial。

内部候选满足

\[
\boxed{\Phi_{,\bar x}=0,\qquad \Phi_{,\bar y}=0.}
\]

四条边分别满足相应的一维驻值方程：

\[
\bar x=\bar x_{min/max}:\quad \Phi_{,\bar y}=0,
\]

\[
\bar y=\bar y_{min/max}:\quad \Phi_{,\bar x}=0.
\]

再加入四角点。

本次 backend 不做 objective optimization。它直接使用有限 Fourier 的解析 gradient、Hessian 和三阶导数全局界：

1. Taylor bound 排除不可能含驻值根的 enclosure；
2. surviving finite root neighborhoods 用 Newton 解 `grad Phi=0`；
3. Krawczyk enclosure 验证每个 interior root 唯一；
4. 再从整域重新排除，要求 `UNRESOLVED_ROOT_ENCLOSURES=0`；
5. 四边独立做一维 derivative root isolation；
6. 对全部候选直接比较 `Phi`。

这与 L-BFGS 的本质区别是：

```text
L-BFGS: 从若干起点找一个局部最大值；可能漏根。
本证书: 先证明所有驻值根都已 accounted，再比较有限候选集。
```

---

# 3. 计算参数首次引入时间

本次 qU-R06 formalization 的参数流水线固定如下，供 BH032/T360/其他同拓扑试件复用：

| Stage | 首次引入参数 | 求法 | 是否依赖后验 comparator |
|---|---|---|---|
| C00 | `(q,Ax,Bx,Ay,By)` terminal contact trial | 原 5×5 system 当前状态 | NO |
| C10 | upper/lower face strain | `eps_i^±=Ai±zf Bi` | NO |
| C20 | qU R02 `d,Delta,U` | augmented cubic, admissible positive minimum-energy root | NO |
| C30 | LL+GL local Fourier coefficients | exact registered harmonic algebra | NO |
| C40 | `Phi` | finite Laurent convolution | NO |
| C50 | interior/edge/corner stationary candidates | analytic derivative all-root certificate | NO |
| C60 | R06 radial `eta_y` | first scalar root on certified active stationary branch | NO |
| C70 | face whole-width mean resultant | R02 mean at `eta_y` | NO |
| C80 | terminal section resultants | UHPC + web + two steel faces | NO |
| C90 | final 5×5 contact | four resultant contacts + UHPC first compression peak | NO |
| C100 | Abaqus comparator | root frozen以后才读取 | YES, post-check only |

没有任何参数因为 BH050 comparator 而提前进入 C00-C90。

---

# 4. BH050 restored contact raw state

冻结 BH050 结构输入不变：

```text
B = 2500 mm
a_phys = 5000 mm
ts = 4 mm
tc = 42 mm
zf = 23 mm
Aw = 1332 mm2
q0 = 0.0025
Es = 206000 MPa
nu_s = 0.30
fy = 355 MPa
UHPC fc = 141.1 MPa
Ec = 43400 MPa
epsc0 = 0.0035
```

Airy coefficients不变：

```text
Pcr = 19.5818772367311 MN
C   = 10841.3718065234 MN
Kx  = 4.272925966136171e6 N/mm
G   = 4.400171479082513e6 N/mm
Jx  = 6.234616244717026e6 N
Jy  = 6.298311709061200e6 N
s   = 1
```

qU exact geometry coefficients仍使用已冻结 TOP/BOTTOM registration；本次没有重新拟合或改相位。

---

# 5. formal R06 — TOP face

最终 terminal root 附近的 upper face physical strain：

\[
(\varepsilon_x,\varepsilon_y)_+
=(+0.00103693754448,-0.000634960880244).
\]

upper face 不需要 radial projection，故

\[
\eta_+=1.
\]

qU augmented R02：

\[
\boxed{U_+=0.01727562617360\;\mathrm{mm}}.
\]

whole-width mean physical stress：

\[
\boxed{\bar{\sigma}_+=(+189.05703345,-75.89756007,0)\;\mathrm{MPa}.}
\]

完整有限 Fourier 驻值认证：

```text
interior roots = 5
edge stationary roots = 4 (1 on each edge)
corners = 4
unresolved interior root enclosures = 0
Taylor/Krawczyk processed proof enclosures = 711 + 903
```

global maximum：

\[
\boxed{\sigma_{VM,max,+}=239.9171871913\;\mathrm{MPa}<355\;\mathrm{MPa}}
\]

at

\[
\boxed{\bar x=0.5000000000000,\qquad \bar y=0.4552701224925.}
\]

因此 upper face 正式保持 uncapped qU-R02。

12-significant-digit decimal-rationalization 相对原 coefficient field 的 uniform Mises 扰动上界仅

\[
\boxed{7.90\times10^{-11}\;\mathrm{MPa}}.
\]

---

# 6. formal R06 — BOTTOM face

最终 full lower face strain：

\[
(\varepsilon_x,\varepsilon_y)_-
=(-0.000997209222390,-0.003630229050898).
\]

R06 first radial local-yield root 被重新精化为

\[
\boxed{\eta_-=0.383807225635240.}
\]

注意：这个 eta 仍是一个一维直接 root，不是空间搜索。每个 eta 的 active local candidate 由驻值方程决定；final face state 再做完整 all-candidate certificate，与 20260825 R06 的执行纪律一致。

在该 eta：

\[
\boxed{U_-=2.84115552117342\;\mathrm{mm}}.
\]

whole-width mean physical stress：

\[
\boxed{
\bar{\sigma}_-
=(-59.17656787,-217.83083339,-0.42049547)\;\mathrm{MPa}.
}
\]

完整 qU GL+LL Fourier candidate enumeration：

```text
interior stationary roots = 8
edge stationary roots = 9
    ylo = 4
    yhi = 3
    xlo = 1
    xhi = 1
corners = 4
unresolved interior root enclosures = 0
Taylor/Krawczyk processed proof enclosures = 2057 + 2273
```

所有 8 个 interior roots 均通过 Krawczyk local uniqueness gate。

全局最大是 interior root：

\[
\boxed{\bar x=0.47862062308910,}
\]

\[
\boxed{\bar y=0.55555994769262,}
\]

并给出

\[
\boxed{\sigma_{VM,max,-}=355.00000000003\;\mathrm{MPa}.}
\]

第二大候选为 `xhi` edge：

\[
\sigma_{VM,2}=352.6864433722\;\mathrm{MPa},
\]

故 final global-max margin 为

\[
\boxed{355-352.6864433722=2.3135566278\;\mathrm{MPa}.}
\]

12-significant-digit rationalization 对完整 field 的 uniform Mises perturbation bound：

\[
\boxed{8.36\times10^{-10}\;\mathrm{MPa}},
\]

远小于该候选间隔。

因此：

```text
BOTTOM_qU_R06_FINAL_GLOBAL_MAX = CERTIFIED
TEMPORARY_L_BFGS_MAX = SUPERSEDED
```

---

# 7. 用 formal R06 重新闭合原始 5×5 terminal contact

未知量仍然只有

\[
(q,A_x,B_x,A_y,B_y).
\]

方程仍然只有：

\[
N_x^{sec}=N_x^d,
\quad
M_x^{sec}=M_x^d,
\]

\[
N_y^{sec}=N_y^d,
\quad
M_y^{sec}=M_y^d,
\]

和既有 active UHPC endpoint

\[
A_y-21B_y=-0.0035.
\]

formal-R06 root：

\[
\boxed{q_u=0.00471512049258623}
\]

\[
\boxed{A_x=1.98641610451232\times10^{-5}}
\]

\[
\boxed{B_x=4.42205818884856\times10^{-5}\;\mathrm{mm^{-1}}}
\]

\[
\boxed{A_y=-0.00213259496557082}
\]

\[
\boxed{B_y=6.51145254490087\times10^{-5}\;\mathrm{mm^{-1}}}
\]

Airy explicit load：

\[
\boxed{P_u=13.2934844671869\;\mathrm{MN}.}
\]

resultant closure：

```text
Nx_sec = Nx_d = +195.734037645855 N/mm
Ny_sec = Ny_d = -5115.830891388012 N/mm
Mx_sec = Mx_d = +29396.9668188762 N
My_sec = My_d = +29697.2986080903 N
```

stored residual：

```text
Rx = +2.84e-13 N/mm
Ry =  0.00e+00 N/mm
RMx = -1.09e-11 N
RMy = +4.37e-11 N
active endpoint residual = 0
```

纵向 phase resultants：

```text
Ny_UHPC  = -3770.1940103190 N/mm
Ny_faces = -1174.9135738419 N/mm
Ny_web   =  -170.7233072271 N/mm
```

---

# 8. 与 16:48 pre-certified 数值的关系

16:48 临时 continuous stationary optimizer 给出：

\[
P_u=13.29348446718\;\mathrm{MN}.
\]

本次移除空间 optimizer 后：

\[
\boxed{P_u=13.2934844671869\;\mathrm{MN}.}
\]

所以：

```text
LOCAL_OPTIMIZER_REMOVAL_CHANGED_Pu = NO at displayed engineering precision
qU_EFFECT_RELATIVE_TO_FORMAL_qU_OFF_R06 = -0.4708754%
```

这说明此前 13.29348 MN 的数值本身并没有被 L-BFGS 偶然选错；缺的是正式全候选 certificate，现在该缺口已经补上。

---

# 9. comparator post-check

根和完整 finite-Fourier certificate 冻结后，才使用 equal-contract BH050 Abaqus：

\[
P_{FE}=12.591227\;\mathrm{MN}.
\]

因此：

\[
\boxed{\text{error}=+5.57736\%.}
\]

本节点不据此修改任何系数。

与 qU-off frozen R06：

\[
13.356376354543\;\mathrm{MN}
\]

相比，qU 修正为

\[
13.293484467187\;\mathrm{MN},
\]

即只降低约

\[
\boxed{0.47088\%}.
\]

所以 qU 是正式需要保留的缺项，但不是 BH050 剩余约 5.6% 偏差的主因。

---

# 10. 当前裁决

```text
RESTORED_AIRY_TO_TERMINAL_CONTACT = PASS
qU_AUGMENTED_R02 = PASS
qU_GL_PLUS_LL_FINITE_FOURIER_FIELD = PASS
R06_L_BFGS_SPATIAL_OPTIMIZER = REMOVED
TOP_COMPLETE_STATIONARY_CERTIFICATE = PASS
BOTTOM_COMPLETE_STATIONARY_CERTIFICATE = PASS
UNRESOLVED_STATIONARY_ROOTS = 0
BH050_FORMAL_qU_ON_Pu = 13.2934844671869 MN
BH050_EQUAL_CONTRACT_ERROR = +5.57736%
```

当前不再允许把以下近期分支带回生产：

```text
terminal Bx=By=pi^2 q/B
remove Mx/My contact
current-moment feedback into Airy
full-halfwave current-material integral
U=0 active-set as BH050 necessity
L-BFGS local Mises gate
```

---

# 11. 下一块试件

如果继续当前单一路径，下一步只做 BH032：

1. 同一 restored 5×5 demand-capacity contact；
2. 同一 exact qU coefficients；
3. 同一 finite-Fourier stationary certificate；
4. root/comparator 严格分离；
5. 检查 qU 是否保持原 BH032 已较好的 R06 预测，而不是重新改理论。
