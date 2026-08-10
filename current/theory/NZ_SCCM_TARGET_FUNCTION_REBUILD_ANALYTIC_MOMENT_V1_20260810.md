# NZ-SCCM 目标函数体系重建：解析矩驱动材料—结构接口 V1

**日期：2026-08-10**  
**身份：CURRENT DESIGN DECISION / USER-ACCEPTED DIRECTION**

## 0. 本文件锁定的新方向

用户已明确接受：下一阶段不再把主要研究资源用于“如何把当前复杂 integrand 用更强数学工具积分掉”，而是保留结构力学目标，重建中间的材料—结构目标函数体系。

同时新增不可退让边界：

```text
FORMAL_INTEGRATION = ANALYTIC_EXACT_MOMENTS
ELEMENT_INTEGRATION = PROHIBITED
SPATIAL_CELLS = PROHIBITED
GAUSS_SIMPSON_ADAPTIVE = PROHIBITED_IN_FORMAL_OPERATOR
MATERIAL_POINT_GRID = PROHIBITED_IN_FORMAL_OPERATOR
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
```

所谓“重建目标函数”绝不意味着把数值积分或单元积分换一个名字重新引入。正式结果必须由一个连续完整代表半波上的有限解析积分 / 精确矩得到。

## 1. 什么保留，什么重建

### 保留的结构力学目标

当前 Case21 结构层继续保留：

- 轴向承载力 `P(D,q)`；
- 幅值方向平衡残量 `Rq(D,q)=0`；
- 极限点/稳定条件

`L(D,q)=P_,D Rq_,q - P_,q Rq_,D = 0`。

钢筋仍必须在求根前进入 `P` 和 `Rq`，不得使用 `Pu=Pu,concrete+As fy` 的事后附加法。

### 重建的中间层

旧问题链：

```text
finite kinematics
-> complicated full stress field sigma(x,y,z)
-> difficult nonlinear composition
-> try to integrate/certify the resulting integrand
```

新链：

```text
finite analytic kinematics
-> finite strain invariants
-> compact invariant/tensor-basis material law
-> finite analytic material moments
-> P, Rq, derivatives/tangent, L
```

核心原则：零数值积分应从材料表示、有限运动学和结构所需功能量共同设计之初实现，而不是事后用越来越复杂的积分算法战胜任意 integrand。

## 2. 运动学层

对 Case21 保持 Nguyen 二阶单完整半波运动学。令广义坐标

`a=(D,q)`，其中 `q=A/b`。

物理应变张量写成有限解析场：

`E(X,Y,zeta;a)=sum_r e_r(a) Phi_r(X,Y,zeta)`，

其中 `Phi_r` 只由有限个 sin/cos 与厚度多项式组成。

这意味着任意有限次应变多项式仍属于有限三角—厚度多项式代数，可在整个半波域上解析积分。

## 3. 材料表示层：二维各向同性 invariant/tensor basis

对二维对称应变张量定义归一化张量

`X=E/eps_ref`。

采用两个基本不变量，例如

`I1=tr(X)`，
`I2=det(X)`

或等价的 `I1` 与 `J2=dev(X):dev(X)`。正式实现应选择最利于材料识别与解析矩闭合的一组。

二维 Cayley-Hamilton 关系使各向同性同轴应力映射可压缩为

`sigma_hat = A(I1,I2,z) I + B(I1,I2,z) X`

其中 `sigma_hat=sigma/f_ref`；`z` 为未来路径依赖扩展所需内部变量。对当前单调 current-state V1，可先令 `z` 为空。

这一表示避免必须显式求 principal eigenvalues、sqrt(delta^2+shear^2) 与 spectral return 才能构造应力。

## 4. 解析友好的 scalar material functions

V1 正式候选要求 `A`、`B` 属于有限解析基，优先采用有限 polynomial / orthogonal-polynomial expansion：

`A(I1,I2)=sum_(m,n in S_A) a_mn Phi_mn(I1,I2)`

`B(I1,I2)=sum_(m,n in S_B) b_mn Phi_mn(I1,I2)`。

最透明形式为 monomial basis `I1^m I2^n`；若为数值条件采用 Chebyshev/Jacobi material basis，则必须能有限代数展开并最终落到同一精确矩族。

系数只能由材料级单轴/双轴/三轴/拉伸数据与物理约束确定，禁止用 Case21、Swartz24、UCFT 结构 Pu 反标。

NC 与 UHPC 共享表示骨架，但 `A/B` 的形式、阶次与参数不要求相同。

## 5. 新的核心对象不是完整应力场，而是有限材料矩

若

`sigma_hat = A I + B X`

且 `A,B` 为有限 invariant polynomial，则结构只需要以下有限矩族。

对每个 material basis index `(m,n)` 定义：

### 5.1 轴力矩

`J^A_P(m,n)=int_Omega Phi_mn(I1,I2) dV`

`J^B_P(m,n)=int_Omega Phi_mn(I1,I2) X_yy dV`

于是

`P_c = -f_ref * sum_mn [ a_mn J^A_P(m,n) + b_mn J^B_P(m,n) ]`

乘上具体坐标归一化 Jacobian 后得到最终物理单位。

### 5.2 幅值平衡矩

定义 `X_q=partial X/partial q`：

`J^A_q(m,n)=int_Omega Phi_mn(I1,I2) tr(X_q) dV`

`J^B_q(m,n)=int_Omega Phi_mn(I1,I2) X:X_q dV`

于是

`Rq,c = f_ref*eps_ref * sum_mn [ a_mn J^A_q(m,n) + b_mn J^B_q(m,n) ]`

同样保留真实几何 Jacobian。

这四族矩是 V1 最基本材料—结构接口：材料只提供 `a_mn,b_mn`；结构运动学只提供精确矩 `J`；两者通过有限线性 contraction 得到 P 和 Rq。

## 6. 为什么这些矩可以解析精确积分

由于 Case21 应变分量是有限 sin/cos × zeta-polynomial，`I1`、`I2` 仍为有限三角—厚度多项式。有限次 `I1^m I2^n`、再乘 `X_yy`、`tr(X_q)` 或 `X:X_q` 后仍为有限和：

`sin^p(X) cos^r(X) sin^s(Y) cos^t(Y) zeta^k`。

因此整个连续半波积分可归结为有限个基础解析矩：

`M_X(p,r)=int_0^pi sin^p X cos^r X dX`

`M_Y(s,t)=int_0^pi sin^s Y cos^t Y dY`

`M_z(k)=int_-1^1 zeta^k dzeta`。

其中整数指数时：

- `M_X(p,r)=0` 若 `r` 为奇数；其余可用 Beta/Gamma 函数或双阶乘闭式；
- Y 同理；
- `M_z(k)=0` 若 k 为奇数，若 k 为偶数则 `2/(k+1)`。

因此最终 P、Rq 及其导数是有限解析和，不存在空间 quadrature、element integration 或 material-point sampling。

## 7. 导数、切线与极限条件

因为每个 `J(D,q)` 已是 D、q 的有限显式解析函数，可直接解析求导：

`P_,D`、`P_,q`、`Rq_,D`、`Rq_,q`。

不采用 finite difference，也不需要对空间点逐点形成 tangent 后再积分。

最终：

`Rq(D,q)=0`

`L(D,q)=P_,D Rq_,q - P_,q Rq_,D=0`

保持现有极限点身份。

如后续扩展多个广义坐标 `a_alpha`，则统一形成

`R_alpha=int_Omega sigma:E_,alpha dV - Q_alpha`

和解析 Jacobian `K_alpha_beta=partial R_alpha/partial a_beta`，仍由同一有限矩族组装。

## 8. 钢筋接口

钢筋保持现有解析封闭式 `Ps(D,q)` 与 `Rq,s(D,q)`；总量：

`P=P_c+P_s`

`Rq=Rq,c+Rq,s`。

如未来钢筋发生屈服，仍应采用解析分支/状态表达；不得为了钢筋单独引入空间积分点。

## 9. NC 与 UHPC 的关系

共享：

- finite kinematics；
- invariant coordinates；
- tensor basis；
- exact analytic moment engine；
- P/R/Jacobian/L contraction architecture。

不共享：

- `A_NC,B_NC` 与 `A_UHPC,B_UHPC` 的具体 scalar law；
- 材料参数；
- 必要内部变量；
- tension/compression/confinement/path-dependence 的材料级证据。

UHPC 不能通过把 NC 的 fc 换成 141.1 MPa 得到。

## 10. 路径依赖的后续扩展

V1 先服务当前单调轴压 current-state benchmark。若后续材料证据要求 history/internal variables，则扩展为

`sigma_hat=A(I,z)I+B(I,z)X+...`

但 `z(X,Y,zeta)` 不允许采用材料点网格。应使用有限全局解析 basis 表示其场，并使状态更新或增量势仍能投影到有限解析矩；若某一候选内部变量模型无法做到这一点，它可以作为高保真材料 benchmark，但不能直接成为本项目 formal zero-spatial analytic operator。

## 11. V1 第一阶段必须完成的数学任务

1. 从现有 Nguyen 二阶 Case21 应变严格展开 `I1(D,q)` 与 `I2(D,q)`；
2. 建立基础三角—厚度精确矩表；
3. 推导四族 target moments `J^A_P,J^B_P,J^A_q,J^B_q` 的通项；
4. 推导 P、Rq 与 D/q 导数；
5. 先用低阶 generic coefficients 做手算/程序逐项一致性验证；
6. 然后才进入 NC 材料级 `A/B` 识别；
7. NC 通过材料级门禁后再接 Case21；
8. UHPC 使用同一结构/积分骨架，但独立建立其材料 scalar law。

## 12. 禁止事项

- 不允许 element / Gauss / Simpson / adaptive integration 进入正式结果；
- 不允许 spatial cells / collocation / material-point grid 伪装成“解析”；
- 不允许为了积分方便修改 P、Rq、L 的力学定义；
- 不允许用结构 Pu 反标材料 coefficient；
- 不允许先生成巨大的完整 stress polynomial 再暴力 expand-and-integrate；正式实现应 moment-first contraction；
- 不允许把 current benchmark Nguyen/Foster 自动当成新 `A/B` 的最终材料真值。

## 13. 当前决策一句话

`KEEP structural targets P,Rq,L; REBUILD material-to-target interface as finite invariant/tensor-basis material moments; REQUIRE exact analytic integration over one continuous complete halfwave.`
