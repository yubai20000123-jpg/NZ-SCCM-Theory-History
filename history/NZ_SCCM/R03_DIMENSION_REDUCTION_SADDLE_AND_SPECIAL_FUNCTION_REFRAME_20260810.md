# NZ-SCCM R03 — 降维、马鞍曲面判断与特殊函数重定位

**Date:** 2026-08-10

## 1. 用户触发的问题
用户在 R02 后提出两个关键问题：

1. 继续执行 spectral/reachable-domain reduction；
2. 观察此前 `(epsilon1,epsilon2,sigma1,sigma2)` 可视化后，怀疑应力曲面具有类似马鞍面的几何，并要求检索是否存在高度相似的已知构造函数、特殊函数或稳定积分方法。

这不是 route switch，而是在既有 G18/G20/G27 current-map + G26 D15 主线上寻找更合适的坐标与解析核。

## 2. R03 执行结果
采用明确约定 `r=ell/b`：Swartz cases 1-16 为 r=2，cases 17-24 为 r=1。

对 common diagnostic contract

```text
D in [0.60,0.78]
q in [0.0001,0.006]
```

推导得到全空间 sufficient spectral-order condition

```text
D > D_sep(q)
  = Cm/[r^2(1+nu)] + |Cb|(1-r^-2)/(1+nu).
```

24 块板在该 diagnostic box 全部通过。最不利为 Case 11：

```text
D_sep(q=0.006)=0.3214976720
certified lower gap at D=0.60 = 0.2785023280
```

这证明 Case21 的两条 ordered principal spectrum 并非偶然现象，但 final Swartz24 production D-q box 仍未冻结，不能把当前 diagnostic box 冒充最终定理。

## 3. 马鞍判断
对 reference `s1(lambda1,lambda2)` 做 Hessian sign diagnostic：

```text
det(H)<0 saddle-like ~30.62%
convex-like          ~68.54%
concave-like         ~0.84%
```

因此“看起来像马鞍”在局部是对的，但整个 current surface 不是单一 hyperbolic paraboloid。不能从视觉马鞍形状直接推导出一个统一积分公式。

## 4. 更重要的降维发现：exact separated rank <= 4
重新写 source-shaped principal law 后发现：

```text
s+ = U(lp)
   - a_cc C(lp)^2 C(lm)
   + C(lp) T(lm)
   - rho a_t T(lp) T(lm)^8
```

`s-` 为对称表达。

因此每个 principal stress surface 本来就是最多四个一维函数乘积之和。二维 SVD 只是在数值上再次确认这一点。

R03 reachable rectangle 中 numerical rank 2 已能达到 <1e-4 Frobenius residual，rank 3 到机器精度；原因不是新的拟合技巧，而是负谱分支的 tensile primitive 极小：

```text
max |T(lambda-)| ~= 1.238e-4
```

这使若干耦合项天然接近消失。

## 5. 对此前 compiler detour 的新解释
此前 M1R/PF1 把每个一维 primitive rationalize 后，再把所有 resolvent denominator 带进结构积分，最终导致 27 poles / 106 pair blocks / 15x15 PF system。

R03 表明正确优先级应是：

```text
ordered spectral coordinates
-> exact rank-4 separability
-> reachable branch intervals
-> only then compile a few 1D primitives
-> exact small contraction
```

而不是重新构造一个大 2D material surface compiler。

## 6. 特殊函数研究的正确身份
R03 检索并确认：

- Appell F1 对 `a+b sin^2X+c sin^2Y+d sin^2X sin^2Y` 型 whole-domain kernel 有直接 exact master；R03 数值 audit relative difference `1.88e-15`；
- Carlson symmetric elliptic integrals RF/RD/RJ 提供 elliptic-class kernel 的对称、稳定 duplication backend；
- 2x2 matrix-function divided-difference/Cayley-Hamilton form可在 principal eigenvalues 接近时保持连续，不需要材料状态机；
- Zolotarev/rational approximation 对 separated spectra 有理论优势，但只有当其 poles 可直接约化到 Appell/Carlson 等小型 named kernel 时才可能获得 production 身份；不得重演 PF1 大系统；
- Chebfun2/low-rank literature只作为“低秩分离是成熟数学思想”的外部佐证，不允许其 adaptive collocation 成为正式 NZ-SCCM operator。

## 7. 当前纠偏后的唯一方向

```text
2D SURFACE FIT = NO LONGER DEFAULT
EXACT RANK4 PRINCIPAL FACTORIZATION = PROMOTED
NEGATIVE BRANCH = ANALYTICALLY CHEAP
POSITIVE BRANCH T/T8 = REMAINING HARD SCALAR OBJECT
```

下一步不是再画一个马鞍拟合函数，而是逐项检查 rank-4 中真正活跃的一维 branch primitive 经 Case21/Swartz kinematics 复合后，哪些 structural moment 可直接进入 Beta/Appell/Carlson 或其它小型 named special-function kernel。

如果 named-kernel classification 失败，再讨论 positive branch 的紧凑 sigmoid-aware scalar representation；不允许直接回到大 rational/PF family search。