# NZ-SCCM — 钢壳–UHPC 显式极限承载力理论集中技术总账 R01

**Date:** 2026-08-31  
**Repository:** `yubai20000123-jpg/NZ-SCCM-Theory-History`  
**Working branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Production main:** unchanged.  
**Production calculation baseline:** `MARGUERRE_AIRY_EXPLICIT_Z_CAPACITY_V1`  
**Formal spatial quadrature:** `0`  
**Load-step/path tracking:** `0`  
**Newton/Solver structural iteration:** `0`  
**Comparator/test/FEM in coefficient identification or root selection:** `0`

---

# 0. Locked scope

本总账只保留钢壳–UHPC 显式 V1 极限承载力生产链：

```text
raw specimen parameters
-> A/D
-> integer m*
-> Pcr, C, G, J
-> Ppb(q)
-> explicit Z N-M capacity Regime A/B
-> finite algebraic control candidates
-> all polynomial roots
-> qu = minimum positive admissible q
-> Pu = Ppb(qu)
```

理论来源：
`semantic_v2/20_theory/20260821_1733__NZSCCM__MARGUERRE_AIRY_EXPLICIT_LIMIT_THEORY_V1.md`
(blob `968f3ba1b6990bfc7a52e21de6a0047ea0866042`).

后续 R02/R06、Zhang/Liu exact current-section 与 same-q diagnostic 属于独立研究/增强模块；除非未来另行冻结新的 terminal rule，它们不替代、不阻断本 V1 显式 Pu 生产算子。

BH050 的 `13.3563763545430 MN` 属于后来的 historical Airy N-M capacity-contact closure，不是 V1 Z-section Excel 的回归目标。

---

# 1. Raw inputs

正式输入：

\[
\{b,a_{phys},t_c,t_s,A_{0g},A_w,E_s,\nu_s,f_y,E_c,\nu_c,f_c\}.
\]

派生量：

\[
q_0=A_{0g}/b,
\qquad
\rho_w=A_w/(bt_c).
\]

统一使用 N–mm–MPa。

---

# 2. Initial A/D stiffness

定义：

\[
K_s=\frac{E_s}{1-\nu_s^2},\qquad
K_c=\frac{E_c}{1-\nu_c^2},
\]

\[
G_s=\frac{E_s}{2(1+\nu_s)},\qquad
G_c=\frac{E_c}{2(1+\nu_c)},
\]

\[
z_f=\frac{t_c}{2}+\frac{t_s}{2}.
\]

面内刚度：

\[
A_{11}=2t_sK_s+(1-\rho_w)t_cK_c,
\]

\[
A_{22}=A_{11}+\rho_wt_cE_s,
\]

\[
A_{12}=2t_s\nu_sK_s+(1-\rho_w)t_c\nu_cK_c,
\]

\[
A_{66}=2t_sG_s+(1-\rho_w)t_cG_c.
\]

弯曲分量：

\[
D_f=2K_s\left(\frac{t_s^3}{12}+t_sz_f^2\right),
\]

\[
D_c=(1-\rho_w)K_c\frac{t_c^3}{12},
\]

\[
D_{w,y}=\rho_wE_s\frac{t_c^3}{12}.
\]

因此：

\[
D_x=D_f+D_c,
\qquad
D_y=D_x+D_{w,y},
\]

\[
D_\mu=\nu_sD_f+\nu_cD_c,
\]

\[
D_{66}=2G_s\left(\frac{t_s^3}{12}+t_sz_f^2\right)
+(1-\rho_w)G_c\frac{t_c^3}{12},
\]

\[
\boxed{H=D_\mu+2D_{66}}.
\]

---

# 3. Integer mode and Airy coefficients

对正整数 \(m\)：

\[
\alpha=\frac{\pi}{b},
\qquad
\beta_m=\frac{m\pi}{a_{phys}},
\qquad
\ell_m=\frac{a_{phys}}{m}.
\]

\[
N_{cr,m}
=
\frac{D_x\alpha^4+2H\alpha^2\beta_m^2+D_y\beta_m^4}{\beta_m^2},
\]

\[
P_{cr,m}=bN_{cr,m}.
\]

\[
\boxed{m_*=\arg\min_{m\in\mathbb N^+}P_{cr,m}},
\]

随后固定 \(\beta=\beta_{m_*}\)、\(\ell=\ell_{m_*}\)、\(P_{cr}=P_{cr,m_*}\)。

定义：

\[
\Delta_A=A_{11}A_{22}-A_{12}^2,
\]

\[
\bar A_{11}=\frac{A_{22}}{\Delta_A},
\qquad
\bar A_{22}=\frac{A_{11}}{\Delta_A}.
\]

Airy 系数：

\[
K_x=\frac{b^2\alpha^2}{8\bar A_{11}},
\]

\[
G=\frac{b^2\beta^2}{8\bar A_{22}},
\]

\[
C=
\frac{b^3\Delta_A}{16\beta^2}
\left(
\frac{\alpha^4}{A_{22}}
+
\frac{\beta^4}{A_{11}}
\right),
\]

\[
J_x=b(D_x\alpha^2+D_\mu\beta^2),
\]

\[
\boxed{J=J_y=b(D_\mu\alpha^2+D_y\beta^2)}.
\]

---

# 4. Explicit postbuckling demand

\[
Q(q)=q(q+2q_0).
\]

\[
\boxed{
P_{pb}(q)
=P_{cr}\frac{q}{q+q_0}+Cq(q+2q_0)
}.
\]

加载方向局部膜力与弯矩需求：

\[
\boxed{
n(s;q)
=\frac{P_{pb}(q)}{b}
+Gq(q+2q_0)(1-2s^2)
},
\]

\[
\boxed{m(s;q)=Jqs},
\qquad 0\le s\le1.
\]

对 \(q\ge0,q_0>0,P_{cr}>0,C>0\)：

\[
\frac{dP_{pb}}{dq}
=
\frac{P_{cr}q_0}{(q+q_0)^2}+2C(q+q_0)>0.
\]

所以不需要加载路径追踪。

---

# 5. Explicit Z-section capacity

定义：

\[
h_c=\frac{t_c}{2},
\]

\[
N_0=[(1-\rho_w)f_c+\rho_wf_y]t_c,
\]

\[
N_p=N_0+2f_yt_s.
\]

## 5.1 Regime A: 0 <= n <= N0

定义：

\[
D_A=(1-\rho_w)f_c+2\rho_wf_y,
\]

\[
A_A=(1-\rho_w)f_ch_c.
\]

\[
\boxed{
m_u^A(n)
=
\frac{D_Ah_c^2}{2}
-
\frac{(A_A-n)^2}{2D_A}
+
2f_yt_s\left(h_c+\frac{t_s}{2}\right)
}.
\]

写成
\[
m_u^A(n)=u_2^An^2+u_1^An+u_0^A,
\]
其中

\[
u_2^A=-\frac1{2D_A},
\qquad
u_1^A=\frac{A_A}{D_A},
\]

\[
u_0^A
=
\frac{D_Ah_c^2}{2}
-
\frac{A_A^2}{2D_A}
+
2f_yt_s\left(h_c+\frac{t_s}{2}\right).
\]

## 5.2 Regime B: N0 <= n <= Np

\[
\delta=\frac{N_p-n}{2f_y},
\]

\[
\boxed{
m_u^B(n)=f_y\delta[2(h_c+t_s)-\delta]
}.
\]

写成
\[
m_u^B(n)=u_2^Bn^2+u_1^Bn+u_0^B,
\]
其中

\[
u_2^B=-\frac1{4f_y},
\]

\[
u_1^B=\frac{N_p}{2f_y}-(h_c+t_s),
\]

\[
u_0^B=(h_c+t_s)N_p-\frac{N_p^2}{4f_y}.
\]

若 \(n>N_p\)，则为 squash boundary/failure。

---

# 6. Fixed-s q polynomial

在任一固定 \(s\) 与固定 Regime 中，定义

\[
H_s=\frac{C}{b}+G(1-2s^2).
\]

清除 \(q+q_0\) 分母后，定义

\[
N(q)=n(s;q)(q+q_0)
=n_3q^3+n_2q^2+n_1q,
\]
其中

\[
n_3=H_s,
\qquad
n_2=3H_sq_0,
\]

\[
n_1=\frac{P_{cr}}{b}+2H_sq_0^2.
\]

容量接触方程为

\[
\boxed{
F(q)
=u_2N(q)^2
+u_1N(q)(q+q_0)
+u_0(q+q_0)^2
-Jsq(q+q_0)^2
=0
}.
\]

其次数不超过 6。显式系数：

\[
c_6=u_2n_3^2,
\]

\[
c_5=2u_2n_2n_3,
\]

\[
c_4=u_2(n_2^2+2n_1n_3)+u_1n_3,
\]

\[
c_3=2u_2n_1n_2+u_1(n_2+n_3q_0)-Js,
\]

\[
c_2=u_2n_1^2+u_1(n_1+n_2q_0)+u_0-2Jsq_0,
\]

\[
c_1=u_1n_1q_0+2u_0q_0-Jsq_0^2,
\]

\[
c_0=u_0q_0^2.
\]

因此

\[
\boxed{c_6q^6+c_5q^5+c_4q^4+c_3q^3+c_2q^2+c_1q+c_0=0}.
\]

---

# 7. Finite control candidates

在固定 Regime 中：

\[
\Phi_Z(s,q)=m_u[n(s;q)]-Jqs.
\]

它对 \(s\) 为

\[
\boxed{
\Phi_Z=A_4s^4+A_2s^2+A_1s+A_0
},
\]

其中

\[
A_4=u_2n_b^2,
\]

\[
A_2=-2u_2n_an_b-u_1n_b,
\]

\[
A_1=-Jq,
\]

\[
A_0=u_2n_a^2+u_1n_a+u_0,
\]

\[
n_a=\frac{P_{pb}(q)}b+GQ(q),
\qquad
n_b=2GQ(q).
\]

内部控制点满足

\[
\boxed{4A_4s^3+2A_2s+A_1=0}.
\]

正式有限候选集合只包含：

1. \(s=0\)；
2. \(s=1\)；
3. 上述三次式在 \(0<s<1\) 的全部实根；
4. \(n=N_0\) 的 Regime A/B 边界；
5. \(n=N_p\) 的 squash 边界。

内部候选通过 \(\Phi_Z=0\) 与 \(\partial\Phi_Z/\partial s=0\) 的 resultant/discriminant 一次性消元得到有限 \(q\) 多项式根集。

对每个候选根必须重新检查：

\[
q>0,
\qquad
0\le s\le1,
\]

以及对应 Regime 的

\[
0\le n\le N_0
\quad\text{或}\quad
N_0\le n\le N_p.
\]

---

# 8. Ultimate root rule

汇总全部合法有限代数候选：

\[
\mathcal Q
=
\{q_k>0:\ q_k\text{ satisfies contact and branch admissibility}\}.
\]

\[
\boxed{q_u=\min\mathcal Q}.
\]

\[
\boxed{P_u=P_{pb}(q_u)}.
\]

如果 \(\mathcal Q\) 为空，返回
`NO_ADMISSIBLE_CAPACITY_ROOT_IN_V1_DOMAIN`，不得改参数、不得使用试验/FEM 选择根。

---

# 9. Polynomial all-root backend

正式理论身份是：

```text
FINITE_ALGEBRAIC_ALL_ROOT
```

允许使用：

- polynomial Root/RootOf object；
- resultant/discriminant；
- companion-matrix all-root evaluation；
- 其他一次性全根代数后端。

不允许使用：

- Newton structural iteration；
- Excel Goal Seek / Solver；
- load stepping / path continuation；
- spatial discretization；
- comparator-proximity root selection。

Excel R04 中，所有结构方程和多项式系数都由普通 worksheet 公式显式生成；仅最后的一般高次多项式全根提取使用 Excel 365 `PY()`/NumPy `roots` 作为 companion all-root evaluator。它不改变理论方程，也不参与参数标定或路径迭代。

---

# 10. BH050 V1 audit point

输入：

```text
b=2500 mm
a_phys=5000 mm
tc=42 mm
ts=4 mm
A0g=6.25 mm
Aw=1332 mm2
Es=206000 MPa
nu_s=0.30
fy=355 MPa
Ec=43400 MPa
nu_c=0.20
fc=141.1 MPa
```

自动恢复：

```text
m*=2
ell=2500 mm
Pcr=19.5818772367311 MN
Kx=4.272925966136171e6 N/mm
G=4.400171479082513e6 N/mm
C=1.0841371806523354e10 N
Jx=6.234616244717026e6 N
J=6.298311709061200e6 N
```

V1 Z-section 全根计算的 governing candidate：

```text
q_u = 0.0097504617131234
s_u = 1
regime = B
n_u = 6225.14008391775 N/mm
P_u = 17.1449738007645 MN
```

`13.3563763545430 MN` 属于后来的 historical Airy N-M capacity-contact closure，不能作为 V1 Z-section Excel 的目标或根选择依据。

---

# 11. Standalone status

```text
RAW_INPUT_TO_A_D = EXPLICIT
A_D_TO_MODE = EXPLICIT
MODE_TO_AIRY = EXPLICIT
POSTBUCKLING_P_OF_q = EXPLICIT
Z_NM_CAPACITY = EXPLICIT
FIXED_s_q_POLYNOMIAL_DEGREE = <= 6
CONTROL_LOCATION = FINITE_ALGEBRAIC
ULTIMATE_ROOT_RULE = MINIMUM_POSITIVE_ADMISSIBLE_q
RAW_INPUT_TO_Pu = EXPLICIT_FINITE_ALGEBRAIC
PARAMETER_EDIT_RECOMPUTES_Pu = YES
GENERAL_POLYNOMIAL_ALL_ROOT_BACKEND_REQUIRED = YES
NEWTON_REQUIRED = NO
SOLVER_REQUIRED = NO
LOAD_PATH_REQUIRED = NO
FORMAL_SPATIAL_QUADRATURE = 0
EXPERIMENT_OR_FEM_IN_ROOT_SELECTION = 0
DEFAULT_OUTPUT = EXPLICIT_Z_V1_PREDICTION
```

**END OF CENTRAL TECHNICAL LEDGER R01**