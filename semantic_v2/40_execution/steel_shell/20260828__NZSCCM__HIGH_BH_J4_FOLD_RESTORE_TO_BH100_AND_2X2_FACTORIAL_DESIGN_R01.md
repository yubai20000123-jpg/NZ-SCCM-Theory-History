# NZ-SCCM — 高 B/H 四平衡 J4-fold 路线恢复至 BH100 + 2×2 正交参数设计 R01

Date: 2026-08-28

Status: DIAGNOSTIC EXECUTION / PARAMETRIC DESIGN ONLY / PRODUCTION UNCHANGED

## 1. Restored calculation route

按用户 2026-08-28 指令，停止继续讨论统一 UHPC -0.0035 terminal contact 的机制问题，计算恢复到此前能够连续处理高整板宽厚比的版本：

\[
\mathbf R_4(\mathbf x;q)=\mathbf S(\mathbf x)-\mathbf D(q)=\mathbf 0,
\qquad
\mathbf x=(\varepsilon_T^0,\kappa_T,\varepsilon_L^0,\kappa_L)^T.
\]

不再预设第五个 UHPC compression-contact 方程。沿 q=0 连通的主平衡支进行 continuation；R06 upper/lower local-yield 作为内部事件更新截面 resultant。高 B/H 区域的终点恢复为第一 admissible four-equation tangent fold：

\[
\det J_4=0,
\qquad
J_4=\partial\mathbf R_4/\partial\mathbf x.
\]

continuation 只用于 branch identity，不是材料历史积分。current constituent/resultant operators 保持 frozen/path-free。

## 2. Recovered/continued high-BH results

已恢复并冻结的高 B/H 连续族：

| Case | B/H | P_fold (MN) |
|---|---:|---:|
| BH071 | 71 | 14.702190 |
| BH072 | 72 | 14.663695 |
| BH073 | 73 | 14.629788 |
| BH074 | 74 | 14.600303 |
| BH074.5 | 74.5 | 14.587172 |
| BH075 | 75 | 14.575092 |
| BH080 | 80 | 14.508580 |
| BH085 | 85 | 14.530920 |
| BH090 | 90 | 14.630020 |
| BH095 | 95 | 14.795680 |
| BH100 | 100 | 15.019180 |

BH075–BH100 detailed fold states:

| Case | Lx/ts | sigma_cr/fy | q_fold | B q (mm) | P_fold (MN) | g_L- |
|---|---:|---:|---:|---:|---:|---:|
| BH075 | 210.9375 | 0.12576 | 0.01274045 | 47.78 | 14.57509 | 3.092e-4 |
| BH080 | 225.0000 | 0.11053 | 0.01330267 | 53.21 | 14.50858 | 6.146e-4 |
| BH085 | 239.0625 | 0.09791 | 0.01382610 | 58.76 | 14.53092 | 8.796e-4 |
| BH090 | 253.1250 | 0.08733 | 0.01431296 | 64.41 | 14.63002 | 1.115e-3 |
| BH095 | 267.1875 | 0.07838 | 0.01476560 | 70.14 | 14.79568 | 1.326e-3 |
| BH100 | 281.2500 | 0.07074 | 0.01518627 | 75.93 | 15.01918 | 1.516e-3 |

BH100 fold terminal coordinates:

\[
\varepsilon_T^0=9.01567\times10^{-4},\quad
\kappa_T=7.80659\times10^{-5}/\mathrm{mm},
\]
\[
\varepsilon_L^0=-8.50154\times10^{-4},\quad
\kappa_L=5.39829\times10^{-5}/\mathrm{mm}.
\]

BH100 local-Mises certificate at fold:

\[
\eta_+=0.640452,\quad \eta_-=0.629439,
\qquad \sigma_{VM,max,+}=\sigma_{VM,max,-}=355.0000\ \mathrm{MPa}.
\]

Internal event sequence in the high-B/H family remains:

\[
\text{lower R06}\rightarrow\text{upper R06}\rightarrow J_4\text{-fold}.
\]

## 3. 2×2 factorial design objective

目标是把两个因素独立开：

- Factor G: 整板宽厚比 B/H；
- Factor L: 单个钢壳局部子板宽厚比 Bs/ts。

为避免第三个因素“局部子板长宽比”随组合变化，四个新试件统一令局部子板纵横比约为 1.0，并采用整除的 PBL 间距。

固定合同：

- total H = 50 mm;
- UHPC core tc = 42 mm;
- upper/lower steel face ts = 4 mm;
- global aspect a/B = 2;
- global imperfection q0 = 1/400;
- UHPC/steel material constants, boundary conditions, R02/R06 definitions, web/PBL plate thickness and hole/detail rules unchanged;
- local steel imperfection rule A0s = Bs/1600 retained;
- no FEM/test quantity enters theory root selection.

Factor levels:

\[
(B/H)_S=50,\qquad (B/H)_L=100,
\]
\[
(B_s/t_s)_S=156.25\;(B_s=625\ \mathrm{mm}),
\qquad
(B_s/t_s)_L=312.50\;(B_s=1250\ \mathrm{mm}).
\]

These levels are chosen because they are close to the existing BH050/BH100 local-ratio range (140.625 to 281.25), differ by an exact factor of two, and tile both global geometries without edge remainder strips.

## 4. Frozen 2×2 design matrix

| ID | Combination | B/H | B mm | a mm | H mm | tc mm | ts mm | Bs mm | Bs/ts | local Ly mm | local aspect Ly/Bs | global imperfection B/400 mm | local imperfection Bs/1600 mm | transverse local-cell count B/Bs | longitudinal local-cell count a/Ly |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| F-LL | large global + large local | 100 | 5000 | 10000 | 50 | 42 | 4 | 1250 | 312.50 | 1250 | 1.000 | 12.50 | 0.78125 | 4 | 8 |
| F-LS | large global + small local | 100 | 5000 | 10000 | 50 | 42 | 4 | 625 | 156.25 | 625 | 1.000 | 12.50 | 0.390625 | 8 | 16 |
| F-SL | small global + large local | 50 | 2500 | 5000 | 50 | 42 | 4 | 1250 | 312.50 | 1250 | 1.000 | 6.25 | 0.78125 | 2 | 4 |
| F-SS | small global + small local | 50 | 2500 | 5000 | 50 | 42 | 4 | 625 | 156.25 | 625 | 1.000 | 6.25 | 0.390625 | 4 | 8 |

This is a true orthogonal 2×2 geometry design: changing G does not change Bs/ts; changing L does not change B/H; local aspect ratio is fixed.

## 5. Execution order for the factorial set

For each of F-SS, F-SL, F-LS, F-LL use exactly the restored high-B/H calculation route:

1. rebuild initial Airy demand coefficients from the case geometry;
2. rebuild R02/R06 local steel parameters from Bs, Ly, ts and A0s;
3. solve R4=0 on the branch connected continuously to q=0;
4. record lower-R06 and upper-R06 internal events;
5. locate the first admissible det(J4)=0 fold;
6. certify four residuals, UHPC margins, R06 active sets and finite-algebraic local-Mises maxima;
7. report q_fold, Bq, P_fold and constituent resultants.

No production file or qU setting is changed by this checkpoint.
