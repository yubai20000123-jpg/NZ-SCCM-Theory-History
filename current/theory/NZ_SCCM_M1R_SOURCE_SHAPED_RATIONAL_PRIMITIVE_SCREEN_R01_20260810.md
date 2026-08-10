# NZ-SCCM M1R source-shaped rational primitive 筛选 R01

**日期：2026-08-10**  
**身份：CURRENT MATERIAL/ANALYTIC ARCHITECTURE SCREEN — POSITIVE RESULT WITH OUTER-INTEGRAL HOLD**

## 0. 目的与边界

本轮承接：

- `NZ_SCCM_CONCRETE_NONLINEARITY_GATE_V1_20260810.md`；
- `NZ_SCCM_M1_STRUCTURED_MATRIX_POLYNOMIAL_SCREEN_R01_20260810.md` 的 FAIL-screen；
- `NZ_SCCM_INVARIANT_COORDINATE_LIFT_EXACT_REDUCTION_R01_20260810.md` 的 `s=I1` 精确坐标变换。

目标不是计算 Case21 Pu，也不是用结构结果反标材料，而是回答两个更前置的问题：

1. 能否用明显少于 M1-R01 自由二维 polynomial surface 的参数，保留 frozen-NC benchmark 的强 compression/tension/TC/CC 非线性；
2. 这种材料表示能否与 Case21 `s=I1` 变换组成真正的 exact analytic inner integration，而不是重新引入空间 quadrature。

本轮严格排除：

```text
Case21 / Swartz24 / UCFT Pu calibration
spatial X/Y/zeta fitting
spatial Gauss / Simpson / adaptive quadrature
material-point grid
TT/TC/CC spatial partition
```

frozen Nguyen/Foster NC operator 的身份仍是：

```text
MATERIAL-LEVEL NONLINEAR ORACLE / REGRESSION BENCHMARK
NOT FINAL MATERIAL TRUTH
```

因此本轮可以形成 `PASS_SCREEN`，但不能把最终来源冻结的 Gate B 标成 PASS。

---

## 1. 为什么不继续拟合自由二维 A/B surface

M1-R01 已表明：

```text
strong 1D curve + weak low-order 2D polynomial correction
```

并不能有效吸收 TC interaction；继续增加二维 degree 会把问题重新推回高系数、高条件数的自由二维曲面。

本轮改变材料编译对象：**不直接拟合二维应力面，而是保持原 benchmark 的 source algebra，只编译其中的一维 scalar primitives。**

frozen-NC 主方向结构为

\[
s_i
=U_i-a_{cc}C_i^2C_j+C_iT_j-\rho a_tT_iT_j^8,
\qquad i\ne j.
\]

因此定义五个一维 scalar objects：

\[
U(\lambda),\quad C(\lambda),\quad C_2(\lambda)=C(\lambda)^2,
\quad T(\lambda),\quad V(\lambda)=T(\lambda)^8.
\]

然后只把这五个对象编译为有限 rational functions，并按原 source-shaped interaction algebra 重构：

\[
\boxed{
\widetilde s_i
=\widetilde U_i
-a_{cc}\widetilde C_{2,i}\widetilde C_j
+\widetilde C_i\widetilde T_j
-\rho a_t\widetilde T_i\widetilde V_j
}
\]

其中没有任何拟合的二维 interaction surface coefficient。

### 1.1 为什么直接编译 C2 与 V

若先编译 C、T，再在结构计算中形成 `C^2` 与尤其 `T^8`，将人为提高 rational denominator 的幂次。直接把源函数导出的 `C2=C^2` 与 `V=T^8` 作为一维 material primitives 编译，可以：

- 保持原 source algebra；
- 避免额外二维自由参数；
- 显著降低后续 exact rational reduction 的 denominator multiplicity；
- 不引入结构状态反标。

这只是材料表示/编译优化，不改变 frozen benchmark 的材料目标函数。

---

## 2. 材料诊断域

与现有 `CONCRETE_NONLINEARITY_GATE` 完全一致，使用物理主应变归一化坐标

\[
e_i=\varepsilon_i/\varepsilon_0,
\qquad (e_1,e_2)\in[-2.0,0.6]^2.
\]

frozen operator 先映射到 equivalent-uniaxial 主坐标：

\[
\lambda_1=\frac{e_1+\nu e_2}{1-\nu^2},
\qquad
\lambda_2=\frac{\nu e_1+e_2}{1-\nu^2}.
\]

因此在上述完整材料方域上需要覆盖的一维编译区间为

\[
\boxed{
\lambda\in
\left[-\frac{2}{1-\nu},\frac{0.6}{1-\nu}\right]
=[-2.4390243902439024,\ 0.7317073170731706]
}
\]

其中 `nu=0.18`。

该域仍是 broad stress-test domain，不等于最终来源冻结后的材料有效域。

---

## 3. 有限 rational primitive family

通用 zero-preserving rational primitive 写为

\[
\boxed{
R(\lambda)=
\frac{\lambda\sum_{k=0}^{m}n_k\lambda^k}
{1+\sum_{k=1}^{d}d_k\lambda^k}
}
\]

对 `U` 进一步强制 benchmark 原点初始斜率 `kappa`：

\[
\boxed{
\widetilde U(\lambda)=
\frac{\lambda[\kappa+n_1\lambda+n_2\lambda^2+n_3\lambda^3]}
{1+d_1\lambda+d_2\lambda^2+d_3\lambda^3+d_4\lambda^4}
}
\]

R01 采用：

| primitive | numerator setting | denominator degree | free coefficients |
|---|---:|---:|---:|
| U | fixed `kappa` + 3 | 4 | 7 |
| C | m=3 | 4 | 8 |
| C2 | m=3 | 4 | 8 |
| T | m=9 | 10 | 20 |
| V=T^8 | m=4 | 5 | 10 |
| **total** |  |  | **53** |

所有 53 个系数均来自一维 material-oracle compilation；二维 interaction 的系数固定为 frozen source algebra 中的 `a_cc,rho,a_t`。

为数值评价可使用仿射尺度坐标

\[
\xi=\frac{\lambda-\lambda_c}{\lambda_s},
\quad
\lambda_c=-0.853658536585366,
\quad
\lambda_s=1.585365853658536,
\]

但正式材料函数仍是同一个有限 rational function；尺度变化不改变解析身份。

---

## 4. R01 固定系数

以下系数完全写入配套脚本，以保证本 screening result 可复现。

### 4.1 U

按 `[n1,n2,n3,d1,d2,d3,d4]`：

```text
[-9.786990860138413,
 20.2150042396063,
 -10.648551770753837,
 -2.1990006614651056,
 27.740854104357723,
 21.454401259317827,
 32.84751931776155]
```

### 4.2 C

按 `[n0,n1,n2,n3,d1,d2,d3,d4]`：

```text
[-0.9442135131854792,
 8.475283733893267,
 -19.155032651471718,
 11.717171611700422,
 2.502734679618874,
 36.42244419918754,
 31.105995105744704,
 36.19639777683384]
```

### 4.3 C2

```text
[-0.22001900119107273,
 1.235734615177478,
 -1.4750318560416769,
 0.02930272701903502,
 2.4695146543890787,
 6.3090038864234,
 4.550686012252086,
 2.6723789248563734]
```

### 4.4 T

```text
[5.2832456515727308e+00,
 5.9036380076624050e+02,
 1.6827160529299152e+04,
 3.4424484696375992e+05,
 2.3654301901438353e+06,
 -5.3855760768061061e+05,
 -1.9558929506678067e+07,
 4.6747916139120964e+05,
 3.6048668340100557e+07,
 1.6064437897170084e+07,
 -1.4488932046500764e+02,
 1.5542658904204591e+04,
 -5.2992374395863095e+05,
 9.7304263129297085e+06,
 -8.4085213382741570e+07,
 4.6193321040738773e+08,
 -1.4278058956538005e+09,
 2.5022789964268451e+09,
 -2.4676258484463243e+09,
 1.1691624735294776e+09]
```

### 4.5 V

```text
[-2.6397090716844929e+00,
 8.5521709459697178e+01,
 4.7435950866466396e+02,
 -7.6967479847511470e+02,
 -7.2653855232676938e+02,
 -4.5562216690418325e+01,
 9.5670115797598226e+02,
 -1.0491501141642168e+04,
 6.6993892415682218e+04,
 -3.1190274492658256e+04]
```

---

## 5. frozen-NC 材料级 screen

验证网格：物理 `(e1,e2)` 材料域 101×101。误差为

\[
|\Delta(\sigma/f_c)|.
\]

### 5.1 全域

| architecture | independent material coefficients | mean abs. error | P95 abs. error | max abs. error |
|---|---:|---:|---:|---:|
| old M1-R01 p=12,d=12 | 182 | 0.02916 | 0.10869 | 0.41314 |
| **M1R-R01** | **53** | **0.006786** | **0.018261** | **0.036742** |

### 5.2 代表材料路径

| path | mean | P95 | max |
|---|---:|---:|---:|
| `e2=0` | 0.008940 | 0.019825 | 0.031700 |
| equal biaxial compression | 0.006861 | 0.015074 | 0.020078 |
| equal biaxial tension | 0.007038 | 0.020418 | 0.037079 |
| `e1=-t,e2=0.25t` TC ratio | 0.009665 | 0.023137 | 0.026984 |

旧 M1-R01 的 TC P95 约为 `0.37460`；新 M1R-R01 为 `0.02314`。

### 5.3 当前允许判定

```text
M1R_R01_FROZEN_NC_ORACLE_REGRESSION = PASS_SCREEN
FINAL_NC_SOURCE_CALIBRATION = NOT_YET_DONE
FINAL_GATE_B = NOT_YET_FROZEN
```

这是重要正结果：source-shaped 1D rational compilation 可以在明显更低二维自由度的条件下保留 frozen benchmark 的强多轴响应。

但不得把 `0.01826` 直接解释为最终材料误差目标；最终 Gate B 必须回材料来源和试验散布定义。

---

## 6. rational pole audit

对五个固定 rational denominator 求根：

- `U`：诊断区间内无实极点；
- `C`：无实极点；
- `C2`：无实极点；
- `T`：无实极点；
- `V`：存在一个实根约 `1.9861419915`，位于诊断区间上界 `0.731707...` 之外。

因此：

```text
R01_REAL_POLES_ON_DIAGNOSTIC_DOMAIN = 0
```

五个 primitive 及其解析导数在当前 screen domain 内均保持 regular。

---

## 7. 从主值 primitive 到 invariant/tensor operator

对任意 scalar rational function `r(lambda)`，定义矩阵函数

\[
R=r(\mathbf X).
\]

二维 Cayley-Hamilton 保证

\[
\boxed{
R=A_r(I_1,I_2)\mathbf I+B_r(I_1,I_2)\mathbf X
}
\]

无需在结构域逐点执行 eigenvalue branch。

若

\[
R=\operatorname{diag}(r_1,r_2)
\]

位于主方向基底，则定义

\[
\boxed{
R^{\rm oth}=\operatorname{tr}(R)\mathbf I-R
}
\]

其主值为 `diag(r2,r1)`，即精确交换两个主方向 scalar primitive。

因此 frozen source-shaped biaxial algebra 可以整体写成矩阵式：

\[
\boxed{
\widehat{\boldsymbol\sigma}
=
U(\mathbf X)
-a_{cc}C_2(\mathbf X)C^{\rm oth}(\mathbf X)
+C(\mathbf X)T^{\rm oth}(\mathbf X)
-\rho a_tT(\mathbf X)V^{\rm oth}(\mathbf X)
}
\]

最终仍严格化为

\[
\boxed{
\widehat{\boldsymbol\sigma}
=A(I_1,I_2)\mathbf I+B(I_1,I_2)\mathbf X.
}
\]

这一步的重要性在于：强 NC interaction 不需要通过 `TT/TC/CC` 空间分区才能进入结构积分。

---

## 8. `s=I1` 后的 denominator degree

考虑一个 scalar quadratic denominator factor

\[
d(\lambda)=1+p\lambda+q\lambda^2.
\]

利用 Cayley-Hamilton：

\[
d(\mathbf X)=d_0\mathbf I+d_1\mathbf X,
\]

\[
d_0=1-qI_2,
\qquad d_1=p+qI_1.
\]

其矩阵行列式严格为

\[
\boxed{
\Delta=
1+pI_1+qI_1^2
+(p^2-2q)I_2
+pqI_1I_2
+q^2I_2^2
}
\]

对 linear scalar factor `1+p lambda`：

\[
\boxed{
\Delta_{\rm lin}=1+pI_1+p^2I_2.
}
\]

而 Case21 的 exact coordinate transform 已证明

\[
I_1=s,
\qquad I_2(s;u,v)=\alpha_0+\alpha_1s+\alpha_2s^2.
\]

所以：

```text
quadratic scalar denominator factor -> denominator degree in s <= 4
linear scalar denominator factor    -> denominator degree in s <= 2
```

配套 SymPy exact audit 对这一次数上界进行了符号核验。

---

## 9. P 与 Rq 的结构权重在 s 中仍为低阶

令

\[
a=(\nu-1)D+MH,
\qquad s=I_1=a+2Buvz.
\]

则

\[
uvz=\frac{s-a}{2B}.
\]

因此

\[
\boxed{
X_{yy}(s)
=-D+Mu^2(1-v^2)+\frac{s-a}{2}
}
\]

对 `s` 为一次。

同理 `I1,q` 对 `s` 为一次；而

\[
G_q=I_1I_{1,q}-I_{2,q}
\]

对 `s` 至多为二次。

所以每一个实际 M1R material block 乘上 P/Rq structural weight 后，固定 `(u,v,D,q)` 时仍是**有限 rational function of s**。

正确实现不应把全部 denominator 先乘成一个巨型 polynomial；应采用 factor-aware Hermite reduction / partial fractions，保留 primitive denominator 的低次数因子结构。

因此当前正式判定：

```text
M1R_R01_S_INNER_INTEGRATION = PASS_CLASS_A
N_s_quadrature = 0
```

Class A 允许结果包括 finite algebraic terms、log、atan/atanh 和显式 real-branch radicals。

---

## 10. endpoint symmetric divided-difference 消除表观 1/(uv)

原 `s=I1` 变换后，若 `F(s;u,v)` 的一个精确原函数为 `calF`，端点为

\[
s_\pm=a\pm c,
\qquad c=2Buv,
\]

定义 symmetric divided difference

\[
\boxed{
\mathcal D_{\mathcal F}(a,c)
=
\frac{\mathcal F(a+c)-\mathcal F(a-c)}{2c}.
}
\]

原变换中的 `1/(uv)` 与端点差中的 `2c=4Buv` 精确抵消，得到

\[
\boxed{
\mathscr M
=8\int_0^1\int_0^1
\frac{\mathcal D_{\mathcal F}(a,2Buv)}
{\sqrt{1-u^2}\sqrt{1-v^2}}
\,du\,dv.
}
\]

所以 `u->0` 或 `v->0` 不需要特殊空间 cell；连续极限直接由 divided difference 给出。

又因为 symmetric divided difference 对 `c` 为偶函数，其依赖自然进入

\[
c^2=4B^2u^2v^2.
\]

进一步令

\[
x=u^2,\qquad y=v^2,
\]

则

\[
\boxed{
\mathscr M
=2\int_0^1\int_0^1
\frac{
\mathcal D_{\mathcal F}(a(x,y),2B\sqrt{xy})
}{
\sqrt{x(1-x)y(1-y)}
}
\,dx\,dy.
}
\]

这把剩余问题规范化为一个 **Beta-weighted two-variable algebraic/logarithmic period**。

---

## 11. 当前 Gate A 到底走到哪里

现在已经不是“rational material 也许可以积分”的设想，而是：

```text
source-shaped rational primitive compilation = CONSTRUCTED
frozen-NC nonlinear oracle regression        = PASS_SCREEN
real-pole domain audit                        = PASS
matrix/invariant reduction                    = EXACT
s=I1 material/thickness inner integration     = PASS_CLASS_A
s spatial/material quadrature                 = 0
```

但完整三重域的 Gate A **尚未 PASS**，因为剩余 `(x,y)` Beta-weighted period 尚未逐 factor family 完成有限 special-function 闭合。

当前身份必须写成：

```text
M1R_R01_OUTER_XY = CLASS_B_CANDIDATE / NOT_YET_CLOSED
FORMAL_WHOLE_HALFWAVE_GATE_A = HOLD
```

不能因为内层已经闭式就提前进入 Case21 Pu。

---

## 12. 下一唯一执行任务

下一步不再重新拟合材料，也不回到 M1 polynomial。按实际 M1R denominator factor family：

```text
actual M1R factor blocks
-> exact s antiderivatives
-> symmetric endpoint divided differences
-> x=u^2, y=v^2
-> classify each outer family
```

分类顺序：

1. Beta / elementary / algebraic-log Class A；
2. Appell / Horn two-variable hypergeometric；
3. elliptic / generalized hypergeometric；
4. GKZ / Picard-Fuchs period representation。

PASS 条件：最终只保留有限 named special functions/finite analytic objects，且可对 `D,q` 解析求导，形成同一 operator 的 tangent 与 `L`。

若 outer family 不能形成可接受的有限解析闭合，再进入 joint pushforward/coarea 路线；仍禁止用 numerical spatial quadrature 作为 production fallback。

---

## 13. 本轮没有做什么

明确未执行：

```text
NO Case21 Pu solve
NO Swartz24 solve
NO UHPC production fit
NO shell/Y production operator
NO structural-load calibration
```

本轮只推进了材料架构与 exact analytic contraction 的关键中间层。

---

## 14. 当前一句话结论

\[
\boxed{
\text{M1R source-shaped 1D rational compiler}
+\text{ invariant matrix algebra}
+\text{ exact }s=I_1\text{ elimination}
}
\]

已经同时表现出显著优于 M1-R01 的 frozen-NC 强非线性保真度，并严格通过一维材料/厚度方向的 Class-A exact integration；当前唯一剩余主门禁是把真实 M1R endpoint functions 的 `(x,y)` Beta-weighted period 归类并闭合为有限解析 special-function family。