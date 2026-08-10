# NZ-SCCM PF1-R05：physical hypergeometric pullback → common rational driver

**日期：2026-08-10**  
**身份：CURRENT PF1 ANALYTIC PROGRESS — HYPERGEOMETRIC DRIVER PASS / x EXACT ELIMINATION PASS / WHOLE CONNECTION HOLD**

## 0. 本轮先执行“目标相关性门禁”

本轮首先同步：

`governance/PF1_R05_GOAL_RELEVANCE_CHECKPOINT_20260810.md`

因此 R05 只允许处理 R04 已经得到的 **actual physical symmetric endpoint kernel**，不得为了数学完备性脱离当前 `P/Rq/L` 目标去建立无关的 generic period theory。

冻结不变：

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
KINEMATICS = NGUYEN_SECOND_ORDER
STRUCTURAL_TARGETS = P(D,q), Rq(D,q), L(D,q)
MATERIAL_ROUTE = M1R source-shaped rational primitives
INNER_ROUTE = resolvent -> s=I1 exact elimination
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
NO spatial cells
NO material-point grid
NO structure-based material refit
NO route switch
```

R05 的问题只剩：R04 的

\[
\mathrm{Beta}(x)\mathrm{Beta}(y)\times R(x,y)\Phi(\chi(x,y))
\]

怎样继续消去真实 whole-halfwave `x,y` 积分。

---

## 1. R04 的 canonical special function 比二阶 ODE 还可以再降一层

R04 定义：

\[
\boxed{
\Phi(z)=\frac{\operatorname{atanh}\sqrt z}{\sqrt z}
={}_2F_1\!\left(\frac12,1;\frac32;z\right),
\qquad \Phi(0)=1.
}
\]

除了 R04 已记录的二阶 Gauss ODE，`Phi` 还严格满足更直接的一阶非齐次恒等式：

\[
\boxed{
2z\Phi'(z)+\Phi(z)=\frac1{1-z}.
}
\]

证明只需令 `t=sqrt(z)`：

\[
t\Phi=\operatorname{atanh}t,
\]

对 `t` 求导即得。

配套 SymPy exact audit：

```text
2*z*dPhi/dz + Phi - 1/(1-z) = 0 exactly
```

正式状态：

```text
PF1_R05_PHI_FIRST_ORDER_IDENTITY = PASS_EXACT
```

这一步的意义不是换一个特殊函数，而是把 **Phi pullback 的参数导数直接降成“Phi 本身 + rational driver”**，避免继续扩大 log/hyperelliptic basis。

---

## 2. 只引入一个解析系数参数 tau，不改变物理问题

R04 actual single-resolvent quantities中，令：

\[
h=x+y-1,
\]

把物理 `B^2` 暂时记成一个**解析系数参数**：

\[
\boxed{\tau}.
\]

注意：`tau` **不是新的结构自由度、加载变量或材料内部变量**。它只用于构造同一个 finite special-function evaluator；物理值最后严格取：

\[
\boxed{\tau=B(q)^2.}
\]

`D,M,q,r,nu` 的物理定义全部不变。

定义去掉 `B^2` 项后的：

\[
E_{0r}
=-\nu D^2+DMK-r a+r^2,
\]

其中仍采用当前：

\[
a=(\nu-1)D+M(x+y-2xy).
\]

再定义：

\[
\boxed{E_r(\tau)=E_{0r}+\tau h,}
\]

\[
\boxed{K_r(\tau)=E_{0r}-\tau h,}
\]

以及：

\[
\boxed{\ell_r=D(\nu-1)+M(2-x-y)-2r.}
\]

R02 的 `Gamma_r` 与 `B` 无关，因此保持原式。

---

## 3. 新 exact identity：两个 R04 Phi kernel 实际共享同一个 rational driver denominator

R04 的两个核心 argument 分别对应：

### 3.1 log divided-difference kernel

\[
\boxed{
\mathcal F_{L,r}(\tau)
=\frac{\ell_r}{2E_r(\tau)}
\Phi\left(
\frac{\tau xy\ell_r^2}{E_r(\tau)^2}
\right).
}
\]

### 3.2 reciprocal quadratic kernel

\[
\boxed{
\mathcal F_{J,r}(\tau)
=\frac1{K_r(\tau)}
\Phi\left(
\frac{\tau\Gamma_r}{K_r(\tau)^2}
\right).
}
\]

本轮发现并 exact check：

\[
\boxed{
\mathscr D_r(\tau)
=E_r(\tau)^2-\tau xy\ell_r^2
=K_r(\tau)^2-\tau\Gamma_r.
}
\]

也就是说，R04 看起来不同的 `log` 和 `reciprocal` 两个 Phi pullback，在真正进入 outer contraction 时，共享**同一个 rational period denominator**。

配套 symbolic remainder：

```text
K_tau^2 - tau*Gamma
-
(E_tau^2 - tau*x*y*ell^2)
= 0 exactly
```

正式状态：

```text
PF1_R05_COMMON_TAU_DRIVER_IDENTITY = PASS_EXACT
```

这是当前 R05 最关键的物理相关简化：后续不需要分别建立两套 outer special-function engines。

---

## 4. 两个 Phi kernel 都满足同一个一阶 tau operator

利用：

\[
2z\Phi'(z)+\Phi(z)=\frac1{1-z},
\]

对 `tau` 做 chain rule。

### 4.1 log kernel

对：

\[
z_L=\frac{\tau xy\ell_r^2}{E_r^2},
\qquad
R_L=\frac{\ell_r}{2E_r},
\]

exact simplification 得：

\[
\frac{R_{L,\tau}}{R_L}
-\frac{z_{L,\tau}}{2z_L}
=-\frac1{2\tau}.
\]

最后：

\[
\boxed{
\left(2\tau\frac{\partial}{\partial\tau}+1\right)
\mathcal F_{L,r}
=
\frac{\ell_r K_r(\tau)}{2\mathscr D_r(\tau)}.
}
\]

### 4.2 reciprocal kernel

同理：

\[
z_J=\frac{\tau\Gamma_r}{K_r^2},
\qquad
R_J=\frac1{K_r},
\]

exact 得：

\[
\frac{R_{J,\tau}}{R_J}
-\frac{z_{J,\tau}}{2z_J}
=-\frac1{2\tau},
\]

以及：

\[
\boxed{
\left(2\tau\frac{\partial}{\partial\tau}+1\right)
\mathcal F_{J,r}
=
\frac{E_r(\tau)}{\mathscr D_r(\tau)}.
}
\]

配套脚本对以上两个 RHS 都得到 exact zero remainder。

正式升级：

```text
PF1_R05_LOG_KERNEL_TAU_ODE = PASS_EXACT
PF1_R05_RECIPROCAL_KERNEL_TAU_ODE = PASS_EXACT
```

这意味着 R04 的所有 physical `Phi` dependence 被压到同一个一阶 operator；其 inhomogeneous driver 全部变成**普通 rational Beta-weighted periods**。

---

## 5. pair-resolvent 没有产生新的 transcendental family

R04 已证明 pair block 在 `s` 方向通过 exact partial fraction / confluent limit 最终只需：

```text
polynomial endpoint moments
+ J0_r / J1_r
+ J0_t / J1_t
```

而 `J1` 又由 `log kernel + J0` 的有限 rational combination 得到。

因此 R05 的 common rational driver 同时覆盖：

```text
single resolvent
pair resolvent
P structural weights
Rq structural weights
```

不需要为 pair block 建新的一套 hyperelliptic/log machinery。

---

## 6. actual rational driver 的几何规模已精确锁定

\[
\boxed{
\mathscr D_r(\tau)
=E_r(\tau)^2-\tau xy\ell_r^2.
}
\]

对 generic current symbols exact 展开：

```text
degree_x = 3
degree_y = 3
total_degree = 4
number of monomials = 11
```

monomial support：

```text
(3,1)
(2,2) (2,1) (2,0)
(1,3) (1,2) (1,1) (1,0)
(0,2) (0,1) (0,0)
```

这很重要：R05 后续只需要处理一个固定低阶 11-term rational driver，不是任意二维函数。

---

## 7. physical x integral 可以直接 Class-A 精确消掉

outer weight：

\[
\frac{dx}{\sqrt{x(1-x)}}.
\]

对任意 pole `rho`，Euler-Beta identity 给出：

\[
\boxed{
\int_0^1
\frac{dx}{\sqrt{x(1-x)}(x-\rho)}
=-\frac{\pi}{\sqrt{\rho(\rho-1)}}
}
\]

其中 square root 按同一 analytic-continuation branch 定义；不是空间 cell。

该式也可由：

\[
{}_2F_1\left(\frac12,1;1;\frac1\rho\right)
=\frac1{\sqrt{1-1/\rho}}
\]

直接得到。

因为固定 `y,tau` 时：

\[
\deg_x\mathscr D_r\le3,
\]

若其 simple roots 为：

\[
\rho_1,\rho_2,\rho_3,
\]

则对任意 proper numerator `N(x,y)`：

\[
\frac{N(x,y)}{\mathscr D_r(x,y;\tau)}
=
\sum_j
\frac{N(\rho_j,y)}{\partial_x\mathscr D_r(\rho_j,y;\tau)}
\frac1{x-\rho_j}.
\]

于是：

\[
\boxed{
\int_0^1
\frac{N(x,y)\,dx}
{\sqrt{x(1-x)}\mathscr D_r}
= -\pi
\sum_j
\frac{N(\rho_j,y)}
{\partial_x\mathscr D_r(\rho_j,y;\tau)
\sqrt{\rho_j(\rho_j-1)}}.
}
\]

重根只使用同一表达的 confluent analytic limit；不得据此建立空间子域。

因此：

```text
PF1_R05_X_ARCSINE_RESOLVENT_ELIMINATION = PASS_CLASS_A
N_x_quadrature = 0
```

这一点比“存在某个 creative telescoper”更直接：actual physical x 积分本身已经被有限代数 root-trace 精确消去。

---

## 8. x 消元后的 y family 仍是 finite algebraic，但暂不冒充 whole closure PASS

为了不显式列出三个 cubic roots，定义：

\[
Z=\rho(\rho-1).
\]

通过：

\[
\boxed{
\mathcal R_r(Z,y;\tau)
=
\operatorname{Res}_{\rho}
\left(
\mathscr D_r(\rho,y;\tau),
Z-\rho(\rho-1)
\right).
}
\]

则所有 x-root-trace radical：

\[
\sqrt{\rho_j(\rho_j-1)}
\]

都属于这个**有限 algebraic cover**。

### 8.1 exact rational witness

用：

```text
D=1
M=1
nu=1/5
r=2
tau = symbolic
```

得到：

```text
degree_Z R = 3
degree_y R = 6
total degree in (Z,y) = 7
term count = 19
```

其 `Z`-discriminant：

```text
degree_y   = 20
degree_tau = 15
```

factor degree pattern：

```text
(y-degree, tau-degree, multiplicity)
(0,1,1)
(1,0,1)
(2,1,2)
(5,4,1)
(5,4,2)
```

所以 x 消元后没有变成无限 branch front；它变成固定有限代数函数族。

正式状态：

```text
PF1_R05_Y_ALGEBRAIC_TRACE_RESULTANT = PASS_FINITE_ALGEBRAIC
```

但**有限 algebraic cover 仍不是完整 y integral evaluator**，所以 Gate A 不能提前 PASS。

---

## 9. 为 y / whole-domain Picard-Fuchs 做了一个严格的规模筛选：19 个 twisted critical monomials

为了判断下一步是不是已经偏离工程目标，本轮没有直接去构造一个巨大 generic GKZ 系统，而是先对**actual common driver**检查 endpoint-compatible twisted critical quotient 的规模。

令：

\[
h_x=x(1-x),
\qquad
h_y=y(1-y).
\]

对应 arcsine weight 和 denominator `D_r` 的 critical polynomials：

\[
\boxed{
G_x=2h_x\,\mathscr D_{r,x}+h_x'\mathscr D_r,
}
\]

\[
\boxed{
G_y=2h_y\,\mathscr D_{r,y}+h_y'\mathscr D_r.
}
\]

它们正对应 endpoint-compatible integration-by-parts / twisted derivative 的有限 polynomial ideal；边界 multiplier `h_x,h_y` 保证 certificate 不需要 endpoint cells。

在上面的 exact rational witness、但保留 `tau` symbolic，并在 field：

\[
\mathbb Q(\tau)
\]

上做 exact Groebner reduction，得到 leading monomials：

```text
x^6
x^2 y^4
x y^5
y^6
x^4 y
x^3 y^2
```

因此 standard monomial quotient 恰有 **19 项**：

```text
1,y,y^2,y^3,y^4,y^5,
x,xy,xy^2,xy^3,xy^4,
x^2,x^2y,x^2y^2,x^2y^3,
x^3,x^3y,x^4,x^5
```

正式身份只写：

```text
PF1_R05_TWISTED_CRITICAL_QUOTIENT = PASS_WITNESS_DIMENSION_19
```

而**不能**偷换成：

```text
FINAL_GENERIC_CONNECTION_DIMENSION = 19
```

因为最终还必须实际构造 parameter-derivative reduction / connection matrix 并检查其 determinant、singular loci、branch continuation 和 `D,q` chain rule。

---

## 10. 为什么本轮在这里停，而不是继续扩大抽象数学

到现在为止，每一步都直接作用于 actual M1R physical kernel：

```text
R04 Phi kernel
-> first-order Phi identity
-> common rational driver D_r
-> exact x elimination
-> finite y algebraic trace
-> 19-dimensional exact witness scale screen
```

这仍然在用户预设目的内。

如果现在不经过 connection-matrix gate，就直接继续研究 generic GKZ / high-genus cohomology，会存在“数学上有限、但工程上越来越远”的风险。因此依照新的 `PF1_R05_GOAL_RELEVANCE_CHECKPOINT`，本轮不把理论向无关方向扩张。

当前必须保持：

```text
PF1_R05_FULL_GENERIC_CONNECTION_MATRIX = HOLD
FORMAL_WHOLE_HALFWAVE_GATE_A = HOLD
```

这不是 PF1 失败，而是一个明确的 practical/theory gate。

---

## 11. 当前下一唯一任务：PF1-R06

R06 仍只服务同一个 common rational driver：

```text
D_r(tau)=E_tau^2-tau*x*y*ell^2
```

下一步必须：

1. 以 actual endpoint-compatible twisted derivative relations 为基础；
2. 构造有限 master numerator basis；
3. **实际输出** `tau` Gauss-Manin / Picard-Fuchs connection matrix；
4. exact audit matrix identity，而不是只说“twisted cohomology 有限维”；
5. 检查 connection singular loci 与 physical `tau=B(q)^2` path；
6. 给出 same-system `D,M,B(q),q` chain derivatives；
7. 给出不使用 x/y quadrature 的 evaluator route。

如果最终 matrix dimension/branch management 已经大到失去当前“有限、透明、可审计、可用于 P/Rq/L”的目的，R06 必须停止并把 PF1 标成 practical FAIL/HOLD；不得为了证明抽象存在性继续无限扩张。

只有 R06 真正闭合，才讨论：

```text
FORMAL_WHOLE_HALFWAVE_GATE_A = PASS_CLASS_B
```

---

## 12. 本轮 formal counts

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_material_point_grid = 0
N_x_quadrature = 0
```

`19` 是一个 exact twisted polynomial quotient 的 witness dimension，不是空间点数、积分点数、材料点数或 structural DOF。

---

## 13. 本轮明确未执行

```text
NO Case21 Pu solve
NO Swartz24 solve
NO material refit
NO UHPC production fit
NO shell/Y production solve
NO spatial numerical quadrature
NO auxiliary numerical quadrature
NO material-point integration
NO spatial cells
NO coarea route switch
```
