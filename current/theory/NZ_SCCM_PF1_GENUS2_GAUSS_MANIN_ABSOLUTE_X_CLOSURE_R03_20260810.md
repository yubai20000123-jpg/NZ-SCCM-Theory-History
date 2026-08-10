# NZ-SCCM PF1 genus-2 Gauss–Manin absolute-x closure R03

**日期：2026-08-10**  
**身份：CURRENT PF1 ANALYTIC PROGRESS — ABSOLUTE x-COHOMOLOGY PASS / RELATIVE PHYSICAL PERIOD HOLD**

## 0. 前置治理门禁

本轮在以下文件已经先行提交后执行：

`governance/PF1_PATH_INVARIANTS_LOCK_20260810.md`

因此本轮没有权力改变：

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
FORMAL_INTEGRATION = ANALYTIC_EXACT
NO element integration
NO material-point grid
NO spatial cells
Nguyen second-order current Case21 finite kinematics
P(D,q), Rq(D,q), L(D,q)
M1R source-shaped rational -> resolvent -> s=I1 route
```

任何有限矩阵仅作用于解析系数/period basis，不代表空间离散。

---

## 1. R02 输入：generic genus-2 single-resolvent algebraic kernel

R02 已得到固定 generic interior `y` 时：

\[
w^2=P_5(x;\theta),
\qquad
P_5=x(1-x)\Gamma_r(x,y;D,M,\nu,r),
\]

其中 `Gamma_r` generically cubic in x，所以 `P5` generically degree 5；存在 exact square-free genus-2 witness。

本轮先处理 PF1 的第一子任务：**single-resolvent algebraic kernel 的 finite Gauss–Manin closure**。

这里参数集合可取

\[
\theta\in\{D,M,y,\nu,r\},
\]

而结构的 q 导数之后通过 `M=M(q)` 以及 relative endpoint 中的 `B=B(q)` 链式进入。R03 不改变任何结构变量定义。

---

## 2. genus-2 absolute de-Rham basis

对 square-free degree-5 hyperelliptic curve

\[
w^2=P_5(x),
\]

采用 4 维 odd de-Rham basis：

\[
\boxed{
\omega_k=\frac{x^k\,dx}{w},\qquad k=0,1,2,3.
}
\]

记

\[
\boldsymbol\omega=(\omega_0,\omega_1,\omega_2,\omega_3)^T.
\]

对 genus 2，absolute `H^1_dR` 的维数为 4；这一 basis 作为当前 algebraic-kernel connection 的固定有限 basis。它不是 Ritz 模态、不是空间节点、不是材料点。

数学来源参考：Griffiths 1969 的 rational-period reduction；Köck–Tait 2018 对 hyperelliptic de-Rham cohomology 给出 explicit basis。它们只提供数学工具，不改变 NZ-SCCM 物理。

---

## 3. 参数导数只产生 `w^-3`

因为

\[
\omega_k=x^kP^{-1/2}dx,
\]

所以对任意参数 `theta`：

\[
\boxed{
\partial_\theta\omega_k
=-\frac12\frac{x^kP_{,\theta}}{w^3}dx.
}
\]

定义

\[
N_{k\theta}(x)=-\frac12x^kP_{,\theta}(x).
\]

由于 `deg P=5`、`deg P_theta<=5` 且 `k<=3`：

\[
\deg N_{k\theta}\le 8.
\]

这正好允许一个固定大小的 polynomial Bezout reduction。

---

## 4. 固定 9×9 Griffiths/Hermite reduction

寻找：

\[
A(x)=\sum_{i=0}^3a_ix^i,
\qquad
B(x)=\sum_{j=0}^4b_jx^j,
\]

使

\[
\boxed{
N=A P+B P'.
}
\]

未知数总数：

```text
4 coefficients of A
+ 5 coefficients of B
= 9
```

等式最高次数 8，也提供 9 个 coefficient equations。

因此构造固定 9×9 coefficient matrix：

\[
\boxed{
\mathsf S(P)\,
(a_0,a_1,a_2,a_3,b_0,b_1,b_2,b_3,b_4)^T
=\operatorname{coeff}_{0:8}(N).
}
\]

`S(P)` 本质上就是 `P,P'` 的 Sylvester map，所以：

\[
\boxed{
\det\mathsf S(P)=\operatorname{Res}(P,P').
}
\]

对 square-free `P`：

\[
\operatorname{Res}(P,P')\ne0,
\]

因此 reduction 唯一存在。

这给出一个重要结论：**PF1 的 x-direction Gauss–Manin reduction 不需要任何空间采样，只需固定 9×9 的解析系数线性代数。**

---

## 5. reduction identity

利用

\[
d\left(\frac{B}{w}\right)
=\frac{B'}{w}dx-\frac{BP'}{2w^3}dx,
\]

得到：

\[
\frac{BP'}{w^3}dx
=
\frac{2B'}{w}dx
-2d\left(\frac{B}{w}\right).
\]

所以：

\[
\boxed{
\frac{N}{w^3}dx
=
\frac{A+2B'}{w}dx
-2d\left(\frac{B}{w}\right).
}
\]

由于：

```text
deg A <= 3
deg B' <= 3
```

故

\[
Q=A+2B'
\]

自动满足

\[
\deg Q\le3.
\]

也就是说，每个参数导数一次 reduction 后**直接回到同一个 4 维 basis**，不需要第二轮 degree reduction。

---

## 6. finite Gauss–Manin connection

若只考虑 closed absolute periods：

\[
\Pi_k=\oint_\gamma\omega_k,
\]

exact differential 的积分为零，于是：

\[
\boxed{
\partial_\theta\boldsymbol\Pi
=\mathsf C_\theta\boldsymbol\Pi,
}
\]

其中 `C_theta` 是 4×4 matrix；每一列由上述固定 9×9 reduction 产生。

由于：

\[
\mathsf S^{-1}=\frac{\operatorname{adj}\mathsf S}{\det\mathsf S},
\]

所以 `C_theta` 的元素是 `P` coefficients 及其 parameter derivatives 的有限 rational functions；唯一 generic singular locus 是 discriminant/resultant locus，即 hyperelliptic curve 退化位置。

当前正式身份：

```text
PF1_R03_GENUS2_ABSOLUTE_DERHAM_BASIS = PASS_EXACT
PF1_R03_FIXED_9X9_GRIFFITHS_HERMITE_REDUCTION = PASS_EXACT
PF1_R03_ABSOLUTE_X_GAUSS_MANIN = PASS_EXACT
```

---

## 7. exact R02 witness 验证

继续使用 R02 完全有理 witness：

```text
D=1
M=1
nu=1/5
r=2
y=1/3
```

\[
P_5(x)
=-\frac{x(x-1)(225x^3+1950x^2-10031x+7920)}{675}.
\]

R03 程序 exact audit 得到：

```text
rank S = 9
```

并且：

\[
\boxed{
\det S
=\operatorname{Res}(P,P')
=-\frac{7162455748218191872}{10509453369140625}
\ne0.
}
\]

对：

```text
theta = D
       M
       y
```

分别对四个 basis forms `k=0..3` 逐一求解：

\[
N_{k\theta}=A_{k\theta}P+B_{k\theta}P'
\]

全部 exact identity check 为 TRUE，并生成对应 4×4 rational connection matrices。

因此这一 PASS 不是只靠维数论，而有 actual M1R/R02 curve 的 exact executable witness。

配套：

- `nz_sccm_pf1_genus2_gauss_manin_r03.py`
- `NZ_SCCM_PF1_GENUS2_GAUSS_MANIN_R03_results.json`

---

## 8. 为什么现在还不能把 physical x integral 标成 PASS

NZ-SCCM 的真实 outer integral 不是任意 closed cycle，而是由：

```text
x in [0,1]
Beta endpoint branch points x=0,1
s-endpoint algebra
log/atanh relative terms
```

共同形成的 **relative period**。

R03 reduction 中保留了：

\[
-2d(B/w).
\]

对于 closed cycle 它消失；但对 physical relative chain 不能直接删除。尤其 `x=0,1` 是 branch endpoints，`B/w` 单项可出现 local-coordinate singular representation；必须在：

\[
t_0=\sqrt{x},
\qquad
t_1=\sqrt{1-x}
\]

局部坐标下建立 regularized relative/tangential endpoint functional，或等价地扩展 relative de-Rham basis，使 exact-term boundary contribution 与 algebraic/log terms 一致闭合。

因此当前必须保持：

```text
PF1_R03_PHYSICAL_RELATIVE_X_ENDPOINT = HOLD
PF1_R03_LOG_RELATIVE_EXTENSION = NOT_YET_CLOSED
```

绝不允许因为 absolute cohomology 已闭合，就把 physical endpoint term 丢掉。

---

## 9. 与 q 导数的关系

R02 的 `Gamma_r`/genus-2 algebraic radical family显式依赖 `D,M,nu,r,y`；其中 `M=C_m(q)`。

因此 algebraic absolute connection 的结构导数满足：

\[
\partial_q\boldsymbol\Pi
=M_q\,\mathsf C_M\boldsymbol\Pi
\]

对这一 algebraic radical部分成立。

但完整 M1R endpoint expressions 还显式依赖：

\[
B=C_b(q),
\]

以及 `E_r,O_r`、log arguments，所以完整 q derivative 必须等 relative/log extension 完成后再统一构造；R03 不提前删掉 B-dependence。

---

## 10. 基础限制 audit

本轮 formal counts：

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_material_point_grid = 0
absolute de-Rham basis dimension = 4
coefficient reduction matrix dimension = 9
```

4 和 9 都是有限解析 function-space/coefficient-space 维数，不是空间离散数量。

没有执行：

```text
NO Case21 Pu
NO Swartz24
NO UHPC production fit
NO shell/Y production solve
NO structural calibration
NO coarea route switch
```

---

## 11. 当前正式判定

```text
PF1_PATH_INVARIANTS = LOCKED
PF1_R03_GENUS2_ABSOLUTE_DERHAM_BASIS = PASS_EXACT
PF1_R03_FIXED_9X9_GRIFFITHS_HERMITE_REDUCTION = PASS_EXACT
PF1_R03_ABSOLUTE_X_GAUSS_MANIN = PASS_EXACT
PF1_R03_PHYSICAL_RELATIVE_X_ENDPOINT = HOLD
PF1_R03_LOG_RELATIVE_EXTENSION = NOT_YET_CLOSED
PF1_R03_PAIR_BLOCK_EXTENSION = NOT_YET_CLOSED
PF1_R03_Y_WHOLE_HALFWAVE_CLOSURE = NOT_YET_CLOSED
FORMAL_WHOLE_HALFWAVE_GATE_A = HOLD
```

这一步把 PF1 从“需要 genus-2 Picard–Fuchs”推进成：

> **single-resolvent algebraic kernel 的 absolute x-direction 已有一个固定 4-dimensional de-Rham basis 和固定 9×9 exact coefficient reduction；真正剩下的第一硬问题是 physical branch-endpoint / algebraic-log relative extension。**

---

## 12. 下一唯一执行任务：PF1-R04

```text
physical x-relative chain
-> local branch coordinates at x=0,1
-> retain exact differential boundary functional
-> add algebraic-log / third-kind relative generators
-> derive finite extended connection
-> verify no hidden quadrature
```

R04 PASS 后才进入 pair-resolvent relative extension；随后才闭合 y 方向。

如果 R04 发现 relative extension 无法形成 finite analytic system，则按治理文件停止并报告 PF1 FAIL/HOLD；不得通过 numerical x-integration、endpoint cells 或 route substitution 绕过。

---

## 13. 数学工具来源

- P. A. Griffiths, *On the periods of certain rational integrals, I, II*, Annals of Mathematics 90 (1969), 460–495, 496–541. DOI: `10.2307/1970746`, `10.2307/1970747`. Role: period/rational-integral reduction methodology.
- B. Köck, J. Tait, *On the de-Rham cohomology of hyperelliptic curves*, Research in Number Theory 4, 19 (2018). DOI: `10.1007/s40993-018-0111-4`. Role: explicit hyperelliptic de-Rham cohomology basis context.

这些来源只提供数学闭合工具，不改变本项目材料、运动学、结构目标或 formal integration identity。
