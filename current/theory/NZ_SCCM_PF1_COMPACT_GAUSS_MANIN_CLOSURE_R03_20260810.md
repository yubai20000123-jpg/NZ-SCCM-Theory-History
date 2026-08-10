# NZ-SCCM PF1：genus-2 compact Gauss–Manin / Picard–Fuchs 闭合 R03

**日期：2026-08-10**  
**身份：CURRENT ANALYTIC DERIVATION — PF1A PASS / WHOLE GATE A STILL HOLD**

## 0. 执行边界先于数学推进

本轮在任何 PF1 计算前已新增：

`current/theory/NZ_SCCM_PF1_EXECUTION_CONTRACT_LOCK_20260810.md`

用户重新确认的基础限制没有改变，且本轮未触碰：

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
FORMAL_INTEGRATION = ANALYTIC_EXACT
ELEMENT_INTEGRATION = PROHIBITED
MATERIAL_POINT_GRID = PROHIBITED
SPATIAL_CELLS = PROHIBITED
GAUSS_SIMPSON_ADAPTIVE = PROHIBITED_IN_FORMAL_OPERATOR
```

PF1 只解决 R02 已识别的 outer hyperelliptic-relative period；不修改 Nguyen 二阶单半波运动学，不修改 `P,Rq,L`，不回到 FE/material-point 路线，不用 Case21/Swartz24 结构结果反标材料。

---

## 1. R02 留下的 canonical single-resolvent curve

R02 对 pole `r` 定义：

\[
\Delta_r(s)=I_2(s)-rs+r^2,
\]

\[
\Gamma_r(x,y;D,M,\nu,r)=4xy\,\operatorname{disc}_s\Delta_r(s).
\]

outer Beta weight 与 single-resolvent radical 合并后，自然得到：

\[
\boxed{
w^2=P_r(x)=x(1-x)\Gamma_r(x,y;D,M,\nu,r).
}
\]

R02 已 exact check：

\[
\deg_x\Gamma_r=3,
\qquad
\deg_y\Gamma_r=3,
\qquad
\deg_{x,y}^{\rm total}\Gamma_r=4.
\]

因此 generic `P_r` 对 `x` 为 square-free degree 5，对应 genus 2。

本轮不再尝试把该对象强行压回 elementary/Beta/ordinary elliptic；直接进入 finite de-Rham / Gauss–Manin reduction。

---

## 2. compact genus-2 de-Rham basis

对 regular state：

\[
\boxed{\operatorname{Disc}_x P_r\ne0}
\]

定义：

\[
\omega_k=\frac{x^k\,dx}{w},
\qquad k=0,1,2,3.
\]

采用四维 compact basis：

\[
\boxed{
\Omega=(\omega_0,\omega_1,\omega_2,\omega_3)^T.
}
\]

其中 `omega_0,omega_1` 为 holomorphic part，`omega_2,omega_3` 补足 genus-2 compact de-Rham cohomology 所需的第二类微分方向。这里 basis 数量 `4=2g`，不是空间离散自由度。

数学工具来源可与 hyperelliptic cohomology / Picard–Fuchs reduction 文献对应；本项目只把它作为解析求解工具，不赋予其材料或结构物理身份。

---

## 3. 对任意结构参数 theta 的 exact derivative reduction

令：

\[
\theta\in\{y,D,M\}.
\]

因为

\[
w^2=P(x;\theta),
\]

所以：

\[
\partial_\theta\omega_k
=-\frac12
\frac{x^kP_{,\theta}}{P^{3/2}}dx.
\]

定义：

\[
\boxed{
A_k=-\frac12x^kP_{,\theta}.
}
\]

关键是 regular state 下：

\[
\gcd(P,P')=1,
\]

因此 `P'` 在 quotient ring `Q[x]/(P)` 中可逆。

定义唯一次数 `<5` 的：

\[
\boxed{
S_k\equiv -2A_k(P')^{-1}\pmod P.
}
\]

于是：

\[
A_k+\frac12S_kP'\equiv0\pmod P.
\]

再定义：

\[
\boxed{
R_k=
\frac{A_k-S_k'P+\frac12S_kP'}{P}.
}
\]

因为 numerator 被 `P` 整除，所以 `R_k` 是普通 polynomial。

同时：

\[
\deg A_k\le 8,
\qquad
\deg S_k<5,
\qquad
\deg P=5,
\]

严格得到：

\[
\boxed{\deg R_k\le3.}
\]

而

\[
d\left(\frac{S_k}{w}\right)
=
\frac{S_k'P-\frac12S_kP'}{P^{3/2}}dx.
\]

因此：

\[
\boxed{
\partial_\theta\omega_k
=
R_k(x)\frac{dx}{w}
+d\left(\frac{S_k}{w}\right).
}
\]

由于 `deg R_k<=3`，第一项严格回到同一四维 basis，第二项为 exact differential。

这就是当前 canonical single-resolvent compact subsystem 的 finite Griffiths/Hermite reduction。

---

## 4. Gauss–Manin connection 已形成有限 4x4 system

把：

\[
R_k(x)=\sum_{j=0}^3 c_{kj}^{(\theta)}x^j
\]

写入 matrix：

\[
G_\theta=[c_{kj}^{(\theta)}].
\]

对随参数平坦延拓、且不穿过 discriminant locus 的 cycle `gamma`，定义 period vector：

\[
\Pi=
\begin{bmatrix}
\int_\gamma\omega_0\\
\int_\gamma\omega_1\\
\int_\gamma\omega_2\\
\int_\gamma\omega_3
\end{bmatrix}.
\]

exact differential 在闭 cycle 上不贡献，故：

\[
\boxed{
\partial_\theta\Pi=G_\theta\Pi.
}
\]

因此当前 compact single-resolvent family 已不再是“未求值的二维积分对象”，而是一个**有限四维解析 differential system**。

其 singular locus 明确由：

\[
\boxed{\operatorname{Disc}_xP_r=0}
\]

控制；在该集合之外 `P'^{-1} mod P` 存在，reduction 合法。

正式身份：

```text
PF1A_COMPACT_GENUS2_DERHAM_BASIS_DIMENSION = 4
PF1A_GRIFFITHS_HERMITE_REDUCTION = PASS_EXACT
PF1A_GAUSS_MANIN_CLOSURE_Y = PASS_EXACT
PF1A_GAUSS_MANIN_CLOSURE_D = PASS_EXACT
PF1A_GAUSS_MANIN_CLOSURE_M = PASS_EXACT
PF1A_SINGLE_RESOLVENT_COMPACT_SUBSYSTEM = PASS_CLASS_B_FINITE_DSYSTEM
```

---

## 5. exact rational state audit

配套脚本：

`current/theory/nz_sccm_pf1_compact_gauss_manin_r03.py`

只使用 SymPy exact rational arithmetic；没有 numerical quadrature。

选择三个完全不同的 rational regular states：

### State A

```text
D=1
M=1
nu=1/5
r=2
y=1/3
```

\[
P=-\frac{x(x-1)}{675}
(225x^3+1950x^2-10031x+7920),
\]

\[
\operatorname{Disc}_xP
=
\frac{7162455748218191872}{3503151123046875}\ne0.
\]

### State B

```text
D=4/5
M=3/2
nu=1/4
r=-1/2
y=2/5
```

\[
\operatorname{Disc}_xP
=
\frac{9316904745213}{1525878906250000}\ne0.
\]

### State C

```text
D=6/5
M=2/3
nu=1/6
r=3/2
y=3/5
```

\[
\operatorname{Disc}_xP
=
\frac{22925993681752704}{95367431640625}\ne0.
\]

对三个状态、三个 derivative directions：

```text
theta = y, D, M
```

共 `3 x 3 x 4 = 36` 个 basis derivative reductions，均得到：

```text
polynomial-division remainder = 0 exactly
deg(R_k) <= 3
```

不是浮点近似成立，而是 exact rational identity。

State A 的完整 `G_y,G_D,G_M` 已保存到：

`current/theory/NZ_SCCM_PF1_COMPACT_GAUSS_MANIN_R03_results.json`

作为可复现的非零 4x4 connection witness。

---

## 6. 对 D/q analytic tangent 的直接意义

Case21 compact curve `P_r` 依赖：

```text
D, M(q), nu, r, y
```

而 R02 已显示 `B(q)` 不进入 `Gamma_r` 本身；`B` 主要进入 endpoint/relative part。

因此 compact period 的结构导数已经可以写为：

\[
\boxed{
\partial_D\Pi=G_D\Pi,
}
\]

以及固定 `D,nu,r` 时：

\[
\boxed{
\partial_q\Pi
=M_qG_M\Pi.
}
\]

实际结构 block 还带显式 `D,M,B` prefactors 时，只需按 product rule 加入显式系数导数。

这表明 **compact hyperelliptic part 已具备 analytic tangent architecture**，不需要 finite difference，也不需要空间材料点切线积分。

但因为 `B(q)` 出现在 moving endpoint/log relative terms，完整 `q` tangent 仍需 PF1B 才能闭合。

---

## 7. outer y 方向现在如何理解

`y` 不再只是“必须数值积分掉的第二个空间坐标”。对 compact period vector：

\[
\boxed{
\frac{d\Pi}{dy}=G_y(y;D,M,\nu,r)\Pi.
}
\]

因此对任何已经 reduction 成：

\[
f(y)^T\Pi(y)
\]

的 compact algebraic subblock，可把目标累积量 `J` 加入有限 system：

\[
J'(y)=\frac{f(y)^T\Pi(y)}{\sqrt{y(1-y)}}.
\]

即：

\[
\frac d{dy}
\begin{bmatrix}\Pi\\J\end{bmatrix}
=
\begin{bmatrix}
G_y & 0\\
\dfrac{f^T}{\sqrt{y(1-y)}} & 0
\end{bmatrix}
\begin{bmatrix}\Pi\\J\end{bmatrix}.
\]

这是一个有限 analytic differential-system representation，而不是在 y 上定义正式 Gauss/Simpson quadrature。

但本轮**不把这一形式直接升级为 whole-halfwave PASS**，原因是：

1. 尚未给出 production branch/initial-value transport；
2. 尚未给出不依赖 numerical quadrature 的稳定 evaluator；
3. 更重要的是，actual M1R `s` antiderivative 包含 log/atanh endpoint terms，它们不属于当前 compact four-period subsystem。

---

## 8. 为什么整个 Gate A 仍然 HOLD

R02 已知实际 M1R single/pair resolvent antiderivative 不只有 `1/sqrt(discriminant)` 这种 compact algebraic factor，还会产生：

- log；
- atanh / atan 的 branch-equivalent forms；
- endpoint algebraic arguments；
- pair-resolvent coefficient singular divisors。

因此完整对象属于：

```text
relative / logarithmic / twisted period extension
```

而不是纯 compact `H^1(C)`。

本轮只把最重要的 genus-2 compact backbone 完整闭合，因此：

```text
PF1A = PASS_EXACT
PF1B_RELATIVE_LOG_PERIODS = HOLD
PF1C_PAIR_RESOLVENT_RELATIVE_CLOSURE = HOLD
FORMAL_WHOLE_HALFWAVE_GATE_A = HOLD
```

这不是路线后退，而是把原来的“generic hyperelliptic-relative”问题拆成了：

```text
compact genus-2 backbone        -> CLOSED
relative/log extension          -> NEXT
pair-resolvent relative layer   -> AFTER PF1B
```

---

## 9. 下一唯一任务：PF1B

继续保持全部基础限制，下一步只做：

```text
PF1B = actual M1R log/atanh endpoint terms
       -> algebraic divisor identification
       -> finite relative/twisted de-Rham basis
       -> parameter derivative reduction
       -> finite extended Gauss-Manin/Picard-Fuchs system
```

优先从 single-resolvent 的 log endpoint block 开始，不并行跳到 Case21 Pu、Swartz24、UHPC、shell/Y 或 coarea。

具体必须回答：

1. log argument 的 zeros/poles 在 genus-2 curve 上形成哪些有限 divisor；
2. `D,y,M,B` derivative 后出现哪些 meromorphic differential；
3. 是否能用 compact 4 basis + 有限 third-kind/relative generators 闭合；
4. branch jump 是否能以有限 monodromy/initial-data 规则管理；
5. 若成功，再处理 pair-resolvent 所引入的额外 divisor。

PF1B 失败时才允许回报真正数学 blocker；不得用 numerical quadrature 替代。

---

## 10. 数学方法来源身份

本轮使用的 Griffiths/Hermite reduction 与 Picard–Fuchs / Gauss–Manin 思路属于外部数学求解工具。与当前方法特别相关的公开算法文献包括：

- Pierre Lairez, *Computing periods of rational integrals* (2014), extended Griffiths–Dwork reduction for Picard–Fuchs equations；
- Hossein Movasati, *Calculation of mixed Hodge structures, Gauss-Manin connections and Picard-Fuchs equations* (2004), differential-form based Gauss–Manin/Picard–Fuchs computation；
- hyperelliptic cohomology literature中采用有限 differential basis/reduction 的相关算法。

这些来源只支持数学工具身份；不改变 NZ-SCCM 的材料物理、结构运动学和零正式空间积分治理。

---

## 11. 本轮明确没有执行

```text
NO Case21 Pu solve
NO Swartz24 solve
NO UHPC production fit
NO shell/Y production solve
NO structural-load calibration
NO spatial numerical quadrature
NO auxiliary numerical quadrature
NO material-point grid
NO route substitution
```
