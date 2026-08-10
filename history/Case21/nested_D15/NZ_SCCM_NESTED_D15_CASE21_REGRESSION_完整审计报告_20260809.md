# NZ-SCCM NESTED-D15 Case21 Regression 完整审计报告

**审计对象**：`NZ_SCCM_NESTED_D15_CASE21_REGRESSION_20260809(1).zip`  
**审计日期**：2026-08-09  
**ZIP SHA-256**：`f4ad23cfd00f2ea545dcc81fdb507dbadbc3c0be1cc0923e2130986afb4a3eb6`

## 0. 总结判定

本压缩包**不是坏包，也不是方向错误的包**。其核心实现与当前 NZ-SCCM 的 moment-first D15 主线总体一致：一个连续完整代表半波、Nguyen 二阶运动学、连续 `sigma=M(epsilon)` 材料接口、零正式空间数值积分、基项闭式矩收缩，以及 Case21 中钢筋必须与混凝土共同进入承载力和平衡残量的思想。

但是，按“可独立复现的正式生产回归包”标准，本包当前**不通过**。更准确的身份应为：

```text
PACKAGE_IDENTITY = CASE21_LOCAL_VALIDATION_SNAPSHOT
REPRODUCIBILITY  = PARTIAL
FORMAL_D15_CORE  = PASS_WITH_GUARDS_MISSING
CASE21_RESULT    = NUMERICALLY_PLAUSIBLE_BUT_PROVENANCE_NOT_CLOSED
SWARTZ24_READY   = NO
PRODUCTION_FREEZE= NO
```

最关键的原因不是 `342.10774 kN` 这个数值本身，而是：**包内现有源码、系数、冻结 mask 与 README 指定的 D,q 组合，不能重新生成包内冻结的 `final_case21_out.txt`；并且包中缺少从 D,q → 混凝土/钢筋总残量 → 平衡根 → 极限点的完整驱动器。**

---

## 1. 压缩包完整性与安全性

压缩包共 12 个条目：1 个目录 + 11 个文件，未压缩总大小 16,175,569 bytes。主要文件为：

- `README.md`
- `build_material_coeffs.py`
- `gen_state.py`
- `eval_stepmask.cpp`
- `ug.txt / Cg.txt / Tg.txt`
- `Case21_local_step_masks.bin`
- `Case21_fixed_mask_peak_scan.csv`
- `final_case21_out.txt`
- `MANIFEST_SHA256.json`

检查结果：

1. ZIP 可正常解压；
2. 无路径穿越条目；
3. 无符号链接；
4. 无加密文件；
5. `MANIFEST_SHA256.json` 中列出的 10 个实体文件，SHA-256 与字节数全部严格匹配；
6. manifest 唯一未自列的是 `MANIFEST_SHA256.json` 自身，没有其他漏列文件；
7. 两个 Python 文件语法编译通过；
8. `eval_stepmask.cpp` 使用 `g++ -Wall -Wextra -Wpedantic` 编译无警告。

因此，**文件完整性门禁通过**。

---

## 2. README 声明的理论身份

README 明确声明：

- 正式空间 quadrature 点数 = 0；
- 空间执行基为 `(sin X, sin Y, zeta)` 的张量 Chebyshev；
- 所有保留基项最终通过闭式解析矩收缩，而不是空间配点积分；
- NC 材料编译区间为 `x∈[-1.25,0.15]`；
- 结构计算使用 N=60；
- 稀疏中间量使用在 `D=0.71, q=0.00220821` 冻结的 per-operation fixed support mask；
- 该 mask 只用于 Case21 验证，不得直接作为 Swartz24 生产 mask；
- 引入 fixed mask 的原因是避免状态依赖幅值剪枝使 `P(D,q), Rq(D,q)` 非光滑；
- 当前 Case21 正式结果声明为：
  - `D_u≈0.7062869`
  - `q_u≈0.0021970710`
  - `A_u≈2.68043 mm`
  - `P_u≈342.10774 kN`
- 独立高阶空间 quadrature 仅用于 audit，声明得到 `P_u≈342.32988 kN`；
- C++ 当前省略显式 TT 高阶项，但 README 对 Case21 给出局部误差上界，并明确要求 Swartz24 前恢复 TT 或在共同域上重新证明上界。

这些声明与当前项目的“大方向”相容；尤其 fixed mask 的动机是正确的：**极限点计算不能让内部稀疏支撑随状态跳变。**

---

## 3. 三个核心源码的数学审计

### 3.1 `build_material_coeffs.py`

材料参数：

```text
fc   = 21.23 MPa
E0   = 20321 MPa
eps0 = 0.00209
rho  = 0.1
```

代码生成三个一维标量原函数 `U,C,T`，保留：

- Saenz 压缩骨架；
- 平滑的正/负应变分离；
- Foster 风格 post-cracking tension-stiffening 目标；
- material interval `[-1.25,0.15]`；
- degree-10 多尺度坐标映射 `chi(x)`。

随后用 200001 点建立 `chi` 的单调逆 PCHIP，再在 8192 个 Chebyshev 节点上评价材料函数，使用 DCT 生成 0—500 阶系数。

审计结论：

- **这不是空间数值积分，也不是板级 surrogate。**
- 但它是**材料坐标上的数值投影/采样式系数生成器**，并非纯符号闭式系数生成器。
- 如果项目允许“材料公式 → 有限解析级数”的离线数值编译，此项可以接受；若要求每个材料系数也必须解析闭式生成，则当前脚本还不满足更强门禁。
- 包内没有 Python/Numpy/SciPy 版本锁定。当前环境（Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0）重建系数后，与冻结文件在 N≤60 范围内仅有极小浮点差异，但不能 byte-for-byte 重现。

### 3.2 `gen_state.py`

该脚本负责由 `D,q` 生成连续 Case21 应变与等效应变张量的不变量，并转成 `(sin X,sin Y,zeta)` 张量 Chebyshev 系数。

关键运动学与当前锁定式一致：

```text
Cm = pi^2/eps0*(q0*q + q^2/2)
Cb = pi^2/(2 eps0)*(t/b)*q

ex = nu D + Cm cos^2X sin^2Y + Cb sinX sinY zeta
ey = -D   + Cm sin^2X cos^2Y + Cb sinX sinY zeta
```

并采用 plane-stress 等效变换构造 `X11,X22,I1,I2`。2×2 矩阵函数使用 Cayley-Hamilton 形式的 pair algebra；乘法实现与

```text
X^2 = I1 X - I2 I
```

一致。

审计结论：**Case21 局部运动学和 2×2 谱代数实现没有发现结构性公式错误。**

但脚本路径硬编码为：

```text
/mnt/data/nested_backend_test
```

因此压缩包解压后不能直接原地运行，属于可移植性缺陷。

### 3.3 `eval_stepmask.cpp`

核心优点：

1. 用 Clenshaw 递推编译 `U,C,T`；
2. 用 Cayley-Hamilton pair 代数组合二维 current operator；
3. 当前 NC interaction 为：
   - `CC = C*C*CY`
   - `TC = C*TY`
   - `S = U - a_cc*CC + TC`
   - `a_cc = 0.1072329249362415`
4. 空间积分采用解析 Chebyshev 矩：

```text
mx(0)=pi
mx(n)=2 sin(pi n/2)/n
mz(odd)=0
mz(even)=2/(1-n^2)
```

这分别是 `∫_0^pi T_n(sin X)dX` 与 `∫_-1^1 T_n(zeta)dzeta` 的闭式结果。

因此，本 C++ 核心的**正式空间积分确实不是 Gauss/Simpson/配点求积**。

---

## 4. fixed mask 二进制审计

`Case21_local_step_masks.bin` 可完整解析：

```text
operation masks       = 2021
total retained keys   = 1,342,030
mask size min         = 0
mask size median      = 348
mask size mean        ≈ 664.043
mask size max         = 6367
zero masks            = 15
masks > 1000 keys     = 401
masks > 5000 keys     = 4
max Chebyshev indices = [60,54,52]
```

文件无尾部冗余字节，二进制结构本身完整。

但是存在一个**重要的程序防护缺陷**：mask 文件不携带以下元数据：

- N=60；
- TOL=1e-6；
- reference D,q；
- `ug/Cg/Tg` 的 hash；
- `gen_state.py` / compiler 版本；
- mask 构建调用总数的强制身份。

更严重的是，C++ 在 fixed mode 只检查“调用超过 mask 数量”时退出，并不检查**结束时是否恰好使用全部 mask**。

实测误用：

```text
N=40, fixed mode
fixed_calls=1351/2021
intP=-12.426941446389979
intR=-32.962365472522286
Snnz=54
```

程序正常退出，没有拒绝该错误组合。

而 N>60 会因为调用更多 mask 最终触发 `MASK_CALL_OVERFLOW`。这说明当前 mask 与 N=60 的身份是隐含的、单向防护的，**N<60 可以静默地产生无效结果**。

这是当前包中最明确的软件合同漏洞之一。

---

## 5. 默认执行入口与 README 正式模式不一致

`eval_stepmask.cpp` 的默认参数为：

```text
TOL = 1e-6
N   = 120
mode= value
```

而 README 正式 Case21 验证要求：

```text
N=60
mode=fixed
```

`value` 模式会执行状态依赖的 magnitude pruning；README 自己明确指出这种方式会使 `P(D,q),Rq(D,q)` 非光滑，不允许用于 fold/limit calculation。

因此：

> **如果用户只编译并直接运行 executable，默认走的恰恰不是 README 所定义的正式验证路径。**

包内也没有 wrapper / Makefile / shell script / Python driver 强制调用：

```text
./eval_stepmask 1e-6 60 fixed
```

这属于正式复现门禁 FAIL。

---

## 6. mask 文件名与运行时路径不闭合

README/压缩包提供：

```text
Case21_local_step_masks.bin
```

C++ fixed mode 却硬编码读取：

```text
/mnt/data/nested_backend_test/step_masks.bin
```

同时 `gen_state.py` 也硬编码同一临时目录。

也就是说，包内没有一个命令可以“解压后原地运行”。审计复现时必须人工：

1. 建 `/mnt/data/nested_backend_test`；
2. 复制三个材料系数；
3. 把 `Case21_local_step_masks.bin` 重命名为 `step_masks.bin`；
4. 运行 `gen_state.py D q`；
5. 编译 C++；
6. 手工指定 `1e-6 60 fixed`。

这不改变数学结果，但不符合“reproducibility package”的工程要求。

---

## 7. 关键复现实验：包内冻结输出不能由包内源码在 README 指定状态重现

README 明确给出附近显式平衡状态：

```text
D = 0.7063550281
q = 0.0021972899281
```

并声明：

```text
Pc ≈ 316.38186 kN
Ps ≈ 25.72586 kN
P  ≈ 342.10772 kN
normalized total Rq ≈ -2.27e-6
```

包内 `final_case21_out.txt` 为：

```text
intP=-12.493214014622462
intR= 4.3417659299685987
Snnz=4345
```

审计使用包内：

- `gen_state.py`
- `eval_stepmask.cpp`
- `ug.txt/Cg.txt/Tg.txt`
- `Case21_local_step_masks.bin`

在同一 README D,q 下重新运行，得到：

```text
intP=-12.491659029482660
intR= 4.391462603953352
Snnz=4345
fixed_calls=2021/2021
```

轴力缩放系数为：

```text
fc*b*t/(2*pi^2)/1000 = 25.324296683300986 kN
```

因此：

```text
审计 Pc = 316.3424793 kN
冻结 Pc = 316.3818582 kN
差值     = -0.0393789 kN
相对 Pc  ≈ -0.01245%
```

raw `intR` 差值为：

```text
+0.04969667
```

约为冻结 raw `intR` 的 1.14%。

这个差异数值不大，但**性质非常关键**：

> `final_case21_out.txt` 确实与 README 的 `Pc≈316.38186 kN` 完全对应，但包内现有源码/系数/mask 在 README 给定 D,q 下不能生成这个冻结输出。

又检查了 README 的 mask reference state `D=0.71,q=0.00220821` 与峰值行 `D=0.7062868783,q=0.0021970710247`，也均不等于 `final_case21_out.txt`。

因此只能判定：**冻结 output 的精确生成状态或生成版本没有随包持久化。**

这不是“数值算法一定错了”，而是明确的 provenance closure 失败。

---

## 8. 为什么包内还不能独立重算 `342.10774 kN`

当前 C++ evaluator 只输出：

```text
intP
intR
Snnz
time
```

它没有实现：

1. concrete raw integral → `Pc` 物理单位转换的正式输出；
2. 钢筋 `Ps(D,q)`；
3. 钢筋 `Rq_s(D,q)`；
4. concrete + reinforcement 总 `Rq=0` 的求根；
5. `L=P_D Rq_q-P_q Rq_D`；
6. 光滑极限点求解；
7. 或 README/CSV 所用 quadratic local limit 的自动化生成；
8. 峰前/峰后可达支路证明；
9. 输出结果与源码/材料/mask 的 hash 绑定。

`Case21_fixed_mask_peak_scan.csv` 已冻结若干 `D,q_equilibrium_est,P_total` 行，但包内没有生成这个 CSV 的 driver。

因此，`342.10774 kN` 当前是一个**结果快照**，而不是“从 ZIP 解压后可一键独立重建的结果”。

---

## 9. 独立 quadrature audit 未随包交付

README 声明同一物理 operator 的高阶空间 quadrature audit 得到：

```text
D ≈ 0.70522
Pu≈342.32988 kN
```

并声称 formal nested-D15 与 audit 相差约 `-0.0649%`。

数值关系本身成立：

```text
342.10774 - 342.32988 = -0.22214 kN
relative difference ≈ -0.0648906%
```

但包内没有独立 quadrature audit 脚本、输入或输出明细，因此本次审计**无法仅凭该 ZIP 独立重建 342.32988 kN**。

所以这一项只能标为：

```text
AUDIT_RESULT_CLAIM = INTERNALLY_NUMERICALLY_CONSISTENT
AUDIT_REPRODUCIBLE_FROM_PACKAGE = NO
```

---

## 10. N=60 材料级数：应力值较好，但切线门禁不足

用包内冻结 `ug/Cg/Tg` 对 `build_material_coeffs.py` 的目标函数在整个 `[-1.25,0.15]` 区间做独立稠密检查：

### N=60 标量函数值误差

近似最大绝对误差：

```text
U              ≈ 4.65e-4  (normalized)
C              ≈ 1.59e-3
rho*T physical ≈ 1.57e-3
```

按 `fc=21.23 MPa` 换算，最大应力量级约 0.01—0.034 MPa，作为 Case21 局部值逼近是较小的。

### 但标量导数的 N=60 收敛明显更慢

在开裂/零应变附近，独立导数审计观察到：

```text
U' max abs error       ≈ 0.236
C' max abs error       ≈ 0.946
(rho*T)' max abs error ≈ 0.926
```

高阶 N=500 时 C/T 导数误差可明显下降到约 0.01 量级。

必须谨慎解释：这些是 `U,C,T` **标量原函数的局部导数误差**，二维 operator 中不同项可能相互抵消，因此不能直接宣布总材料切线误差就是 0.9。

但它足以形成一个正式风险标记：

> 当前包只证明了 P 值局部稳定性，没有交付总 `d sigma/d epsilon`、`Rq` 导数、`L` 或稳定切线的 N=60 收敛证书。

而 NZ-SCCM 极限点/稳定理论对一致切线是正式要求，所以该门禁目前属于 **OPEN / NOT QUALIFIED**。

---

## 11. Case21 材料编译区间覆盖检查

独立稠密评价当前 Case21 等效应变张量主值：

### 正式峰值附近

```text
D=0.7062868783
q=0.0021970710247
principal equivalent strain range ≈ [-0.80637, +0.10008]
```

### mask reference state

```text
D=0.71
q=0.00220821
range ≈ [-0.81059, +0.10059]
```

都明显位于：

```text
[-1.25, +0.15]
```

之内。

因此**Case21 局部 compiler material interval 门禁通过，且有明显余量**。

---

## 12. TT 省略项的局部上界检查

README 给出的 Case21 TT 上界经过独立数量级复核是可信的。

当至少一个主应变 `<=-0.2303` 时，当前标量 tension operator 约：

```text
T(-0.2303) ≈ 1.355e-4
```

结合 `Tmax<0.987`、`rho=0.1` 和当前 TT 系数，可得到 normalized TT stress term 约 `1.0e-6`，对应 direct axial-load upper bound 约 `5.1e-4 kN`，与 README 的 `<0.00051 kN` 一致。

因此：

- **对 Case21 当前局部峰值，TT 从轴力 P 的直接影响确实极小；**
- 但 package 没有提供自动化 TT bound 脚本，也没有把 residual → q-shift → Pu-shift 的推导封装成可复现证据；
- 更不能把 Case21 的局部上界直接推广到 Swartz24。

所以 TT 的当前身份只能是：

```text
CASE21_LOCAL_BOUND = CREDIBLE
FORMAL_EXPLICIT_TT = OMITTED
SWARTZ24_COMMON_DOMAIN = OPEN
```

---

## 13. 与当前 NZ-SCCM 锁定主线的关系

### 一致之处

本包符合以下已锁定原则：

- 一个连续完整代表半波；
- m=1；
- Nguyen 二阶运动学；
- `sigma=M(epsilon)`；
- formal spatial material points = 0；
- formal Gauss points = 0；
- D15 exact analytic moments；
- 不使用 panel-level surrogate；
- fixed support 避免状态依赖剪枝破坏极限点光滑性；
- 钢筋必须进入总 P 和总 RA 后重新求极限状态，不能只在 concrete-only Pu 上事后加一个钢筋承载项。

### 尚不能自动取代旧锁定基线之处

当前治理文件明确规定：新 ZIP、新报告或更接近试验的结果不能自行修改执行宪章；只有用户显式 `AMEND_CHARTER` 才能改变宪章身份。

因此本包虽然看起来是在执行“Case21 加钢筋”的 Stage A，但**本次只读审计不能把 342.10774 kN 自动升级为新的永久 production baseline**。

---

## 14. 数值结果的工程含义

当前包声明：

```text
Pu formal nested-D15 = 342.10774 kN
Pu independent audit = 342.32988 kN
Pf experimental      = 368.31275 kN
```

对应：

```text
formal vs experiment ≈ -7.1149%
audit  vs experiment ≈ -7.0546%
formal vs audit      ≈ -0.06489%
```

与历史 `343.882 kN` 比：

```text
342.10774 - 343.882 = -1.77426 kN
≈ -0.516%
```

峰值运动学量：

```text
mean axial strain = D*eps0 ≈ 0.00147614
A = q*b ≈ 2.68043 mm
```

这些数值在数量级和局部收敛关系上没有表现出明显异常。因此审计不是“否定 342.1 kN”，而是：

> **342.1 kN 是可信候选结果，但当前 ZIP 尚未达到足以证明该结果由包内所有冻结对象唯一、完整、可重复生成的证据标准。**

---

## 15. 门禁总表

| 门禁 | 结论 | 说明 |
|---|---|---|
| ZIP/manifest 完整性 | PASS | hash、size、解压、安全性均通过 |
| Python/C++ 静态可执行性 | PASS | Python compile、C++ warning audit 通过 |
| Case21 m=1 单完整半波 | PASS | 与当前主线一致 |
| Nguyen 二阶连续应变场 | PASS | 公式结构一致 |
| formal zero spatial quadrature | PASS | C++ 使用闭式 Chebyshev moments |
| panel-level surrogate 禁止 | PASS | 未发现板级拟合器 |
| NC CC/TC 低参数 target | PASS | `a_cc` 等与当前冻结目标一致 |
| fixed mask 思路 | PASS_CONCEPT | 避免 state-dependent pruning 非光滑是正确的 |
| fixed mask 文件完整性 | PASS | 2021 masks 可完整解析 |
| fixed mask 身份防护 | FAIL | N<60 可静默误用，缺 metadata/hash guard |
| 默认运行入口 | FAIL | 默认 N120/value，不是 README N60/fixed |
| 解压后直接运行 | FAIL | hard-coded path + mask filename mismatch |
| final output 精确来源闭合 | FAIL | README D,q 下不能重现 frozen final output |
| Case21 全流程 driver | FAIL | 缺 reinforcement、总 Rq root、Pu/limit driver |
| independent quadrature audit 可复现 | FAIL | audit 代码/数据未交付 |
| N60 应力值局部精度 | PASS/GOOD | primitive value error 较小 |
| N60 一致切线/limit 收敛 | OPEN/RISK | 缺 total tangent/L certificate |
| Case21 material interval coverage | PASS | 主值远离 [-1.25,0.15] 边界 |
| TT Case21 局部 load bound | PASS_LOCAL | 数量级可信 |
| TT formal explicit compile | OPEN | C++ 仍省略 |
| TT / mask Swartz24 common domain | FAIL_NOT_READY | README 自己也明确未完成 |
| Swartz24 production readiness | NO | 共同 mask/TT/完整 driver 均未闭合 |
| 自动修改执行宪章 | NOT_AUTHORIZED | 本次用户未发 AMEND_CHARTER |

---

## 16. 当前应如何修复，且不改变理论路线

不需要换理论。建议只修复“可复现性和正式门禁”这一条工程链：

1. **建立唯一入口 `run_case21_regression.py`（或等价 executable）**：从 ZIP 根目录运行，不使用 `/mnt/data/nested_backend_test` 硬编码。
2. **mask 增加 manifest header**：至少绑定 `N=60,TOL,reference D,q,coeff hashes,compiler hash,expected mask_calls=2021`。
3. fixed mode 结束时强制：
   ```text
   PRUNE_CALL == SMASK.size()
   ```
   否则非零退出；同时强制 N/TOL 与 mask metadata 一致。
4. 把 `Case21_local_step_masks.bin` 的正式文件名直接写入配置，不再靠人工重命名。
5. driver 必须完整实现：
   ```text
   D,q
   -> state fields
   -> concrete Pc,Rq_c
   -> reinforcement Ps,Rq_s
   -> total Rq=0
   -> P(D,q)
   -> L=0 或声明的局部极值算法
   -> D_u,q_u,A_u,Pc,Ps,Pu,Rq,L
   ```
6. **解释并修复 `final_case21_out.txt` provenance mismatch**：记录其确切 D,q、全部 field hashes 和生成 executable hash；若不能恢复，应重新生成并废止旧 frozen output。
7. 把 independent high-order quadrature audit 作为 `audit_only/` 子目录交付，使 `342.32988 kN` 可独立复算。
8. 对 N=40、N=50、N=60、N=70（或合适序列）做**总材料应力 + 总一致切线 + Rq/L** 收敛门禁，而不仅是 Pu 标量收敛。
9. TT：Case21 可以继续使用自动化上界证书；进入 Swartz24 前，要么显式编译 TT，要么在共同材料/应变域证明统一上界。
10. 建立**一个 Swartz24 共用、state-independent support policy**，随后先用同一 policy 回归 Case21，再允许 24 板批算；不得逐板 mask tuning。

---

## 17. 最终审计身份

建议本压缩包当前登记为：

```text
ARTIFACT_STAGE
    = NESTED_D15_CASE21_LOCAL_VALIDATION

THEORY_ROUTE
    = RETAINED

FORMAL_SPATIAL_QUADRATURE
    = ZERO_CONFIRMED

CASE21_REPORTED_PU_KN
    = 342.10774

CASE21_NUMERICAL_PLAUSIBILITY
    = PASS

CASE21_BITWISE/PROVENANCE_REPRODUCIBILITY
    = FAIL

FULL_CASE21_END_TO_END_REPRODUCIBILITY
    = FAIL

COMMON_SWARTZ24_COMPILER_DOMAIN
    = OPEN

PRODUCTION_ADOPTION
    = NOT_AUTHORIZED

CURRENT_RECOMMENDED_NEXT_TASK
    = REPRODUCIBILITY_CLOSURE_WITHOUT_CHANGING_THEORY
```

**核心结论**：保留 nested moment-first D15 路线；不要因为当前包的复现缺口推翻理论。下一步应先把 Case21 的“同一源码—同一材料系数—同一 mask—同一总残量—同一极限点”证据链闭合，再建立 Swartz24 共用 support policy。
