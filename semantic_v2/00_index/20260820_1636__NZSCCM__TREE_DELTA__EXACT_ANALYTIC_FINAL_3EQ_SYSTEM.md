# TREE DELTA — NC-M4 exact analytic final 3-equation system

时间：2026-08-20 16:36 +08:00

## 当前节点

`Nguyen second-order -> theta/principal strains -> NC-M4 unique current operator -> exact thickness elementary integration -> exact outer relative-GKZ period -> R_A, R_m, P -> same-source derivatives -> det J_lim = 0`.

## 锁定结果

- General rectangle: `b` and `ell` independent.
- Unknowns: `(Delta,A,epsilon_m)`.
- Formal spatial quadrature/material points: zero.
- After half-angle rationalization the complete NC-M4 local kernels lie in one quadratic algebraic field `Q(u,v,zeta,sqrt(Q2(zeta)))`; no second independent radical is introduced.
- Thickness exact integral: elementary after Euler rationalization because `Q2` is quadratic in `zeta`.
- Thickness state boundaries: exact roots of `epsilon1=0` or `epsilon2=0`, equivalently `4 E_x E_y-G^2=0`; at most two internal roots, used only as exact analytic endpoints, not spatial cells.
- Outer area exact representation: finite relative/incomplete Aomoto-Gelfand / GKZ A-hypergeometric periods; log terms are parameter derivatives.
- Final equations:
  `R_A=0`, `R_m=0`, `det J_lim=0`, where
  `J_lim=[[P_Delta,P_A,P_m],[R_A,Delta,R_A,A,R_A,m],[R_m,Delta,R_m,A,R_m,m]]`.
- Ultimate load: `P_u=P(Delta_u,A_u,epsilon_m,u)`.

## Next unique task

Substitute a concrete panel dataset (first preferred: Case21) into the exact integrated functions, evaluate the finite exact special-function objects, and solve the 3-variable system without using experiment values for solving or root selection.