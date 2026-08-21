# NZ-SCCM — Ritz 理论终点：full-panel admissible space、sector decomposition 与 production rule

时间：2026-08-21 13:35 +08:00
状态：`RITZ_THEORY_ENDPOINT_LOCKED`
材料：`NC-M6 FROZEN`

## 1. 目的

本文件一次性给出当前 NZ-SCCM Ritz 路线的理论终点。后续只允许在该固定框架内做阶次收敛、branch continuation 和材料/结构误差验证；不得再因为某个算例结果改变函数空间身份。

## 2. fixed ideal out-of-plane sector

对 a/b=2 的理想四边简支轴压板，面外基准固定为两个完整半波：

w = b(q0+q) sin(pi x/b) sin(2 pi y/a).

该 halfwave count 不由试验偶然形态、FE后验结果或理论误差改变。

## 3. full-panel boundary-compatible in-plane space

设 A=a=2b，X=pi x/b，Ybar=pi y/A。

定义一个 nested full-panel Ritz family F_N：

u = eps0 [ eta x + sum_{m=1..N} sum_{r=0..4N} b/(2m pi) a_{m r} sin(2mX) cos(rYbar) ],

v = eps0 [ -D y + sum_{m=0..N} sum_{r=1..4N} A/(r pi) b_{m r} cos(2mX) sin(rYbar) ].

这就是当前 Ritz 路线的完整生产母空间；N 只控制有限截断，不改变理论。

F_N 维数有限，N->infinity 给出当前 fixed-w ideal-mode 下的 full boundary-compatible in-plane spectral limit。

## 4. representative halfwave is one exact sector, not the whole space

旧 H_{2N} representative family 对应 full-panel longitudinal indices

r = 4n, n=0..N.

因此

V_rep,N subset F_N.

它不是经验近似；在理想重复两半波基态下它是 exact invariant Fourier sector。

其余 modes 按 r mod 4 组成 complementary sectors。正式 current stress/tangent coefficients具有 halfwave repeat periodicity，所以 full source-consistent residual/Jacobian 按 Fourier residue class 分块。

## 5. final production algorithm

对每一候选 N，唯一生产流程：

A. 在 representative sector 求 origin-connected nonlinear equilibrium branch；
B. 同源组装所有 complementary tangent blocks J_perp,N；
C. 定义 full-panel first control point 为：

min_along_path { first representative limit/rank condition, first complementary block rank loss }；

D. 只有在所有 complementary blocks 在 representative first control point 前均 nonsingular 时，才允许用单 representative halfwave 的 Pu 代表 full-panel Pu；
E. 在相同 F_N 定义下比较 N 与 N+1，使用预冻结 delta_P/delta_D/delta_w/delta_epsilon gate；
F. 一旦 N 收敛，停止升阶；不得根据 FE/试验误差继续增加 N。

## 6. final mathematical endpoint

理论极限不是 H2、H4、H6、H8 或 H10 本身，而是：

F_infinity = closure of union_N F_N

在 fixed ideal two-halfwave w-sector、frozen material current operators、frozen boundary conditions 下求连续平衡与第一控制点。

有限 production order N* 只是一种可验证截断：

Error(F_N*, F_N*+1) <= frozen tolerance

并且 complementary-sector ordering 已通过。

## 7. no further conceptual layers

自本文件起，以下问题全部已在母框架中预先包含，不再作为后续“新理论问题”出现：

- 一个半波 vs 两个半波：由 fixed ideal w-sector + full-panel coordinates 解决；
- 两半波膜内是否完全重复：由 full-panel complementary sectors 自动覆盖；
- 高阶 Ritz 是否遗漏：由 N->N+1 nested convergence 解决；
- 对称解是否漏掉更早非对称控制：由 J_perp ordering 解决；
- branch fold：统一用 origin-connected continuation / pseudo-arclength / KKT limit definition；
- M6 tangent 非 major-symmetric：始终使用 source-consistent unsymmetrized Jacobian/rank condition；
- direct-current quadrature：只作为 audit decimal localizer，正式理论仍由零空间数值积分的解析矩编译完成。

后续若出现数值异常，只允许归入：

1. branch tracking/implementation error；
2. finite-N truncation error；
3. formal analytic compiler error；
4. frozen physical model error。

不得再通过扩张函数空间定义、改变 halfwave count 或增加未经预定义的新自由度来解释。

## 8. cost identity

Production 不需要每次解完整 F_N nonlinear system。利用 sector decomposition：

- nonlinear solve 只在 representative block；
- complementary blocks只做 tangent/rank audit；
- 若 complementary block先失稳，才激活对应 sector进入后续 branch。

因此完整性与低成本并不冲突。

H10 当前：representative amplitudes=60，full in-plane amplitudes=225，complementary amplitudes=165；但 full 225 nonlinear unknowns不是默认生产成本。

## 9. governance

NC-M6 remains frozen.
M7 prohibited.
No trial/FE load in N selection, root selection or convergence threshold.
ONE_CONTINUOUS_COMPLETE_HALFWAVE may continue as computational representative sector only after the corresponding full-panel complementary gate passes for the candidate N.
