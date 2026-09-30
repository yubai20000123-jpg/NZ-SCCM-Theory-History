# UCFT M5 steel deformation theory active-set

更新时间：2026-09-30 16:36 +08:00

M5 已完成。结构级仍保持 q 为 continuation parameter，给定 q 后求 P、A+、A-；本阶段只建立 steel material/section operator。

## M5-1 首轮审计
直接把实际弹性 plane-stress 的 nu_s=0.30 与 Chen-Ji 塑性简化 nu_p=0.50 在 eps_i=fy/Es 处硬切换，会产生 finite stress discontinuity。Es=206000 MPa、fy=355 MPa 的方向扫描得到最大应力张量跳跃 40%，同一 eps_i 阈值处 elastic Mises/fy 为 0.714286~1.153846。因此 literal abrupt splice = FAIL；这是材料接口问题，不是 single-q 路线失败。

## M5-2 最小一致修正
定义 normalized elastic plane-stress operator C0(nu_s)，elastic matrix Ce=Es*C0；定义 plane-stress Mises metric W，并令 Hnu=C0^T W C0。

新的 equivalent secant strain：
ebar_i = sqrt(epsilon^T Hnu epsilon) = elastic-trial-Mises/Es.

plastic equivalent uniaxial law:
sigma_i = Ps(ebar_i),
Esec = Ps(ebar_i)/ebar_i,
Etan = dPs/debar_i.

finite current stress:
sigma = Esec*C0*epsilon.

该定义严格满足 current Mises stress = Ps(ebar_i)。当 nu_s=0.5 时，C0=Hnu 恰好退化为 Chen-Ji 简化矩阵，因此这是 Chen-Ji 特殊式与实际 elastic nu_s 之间的最小一致推广，而不是新结构理论。

consistent material tangent:
Ct = Esec*C0 + (Etan-Esec)/ebar_i^2 * (C0 epsilon) tensor (Hnu epsilon).

finite stress 只用于 current virtual work / internal force；Ct 只用于 Newton/Jacobian/stability。

## M5-3 analytic thickness active-set
对钢壳厚度仿射应变 epsilon(zeta)=a+zeta*b，
ebar_i^2 = C2*zeta^2 + C1*zeta + C0，
其中 C2=b^T Hnu b，C1=2 a^T Hnu b，C0=a^T Hnu a。

屈服边界：
C2*zeta^2 + C1*zeta + C0 - (fy/Es)^2 = 0.
每个厚度截面最多两个内部屈服根、三个 elastic/plastic 区间，全部解析求根、排序、分区。

任意有限阶 equivalent uniaxial polynomial Ps(e) 的 finite stress 可化为 (linear in zeta)*Q(zeta)^p 的有限和，其中 Q=ebar_i^2。complete-square 后用 elementary/asinh recurrence 闭式计算 Ns 与 Ms；production 不需要 thickness Gauss points。

## M5-4 consistency benchmark
测试只验证 kernel，不拟合试件。Es=206000 MPa, nu=0.30, fy=355 MPa, ts=4 mm；采用 ideal plateau 与 diagnostic cubic hardening law。

- analytic thickness resultants vs adaptive numerical diagnostic: max relative error 7.727093e-14
- yield quadratic root ebar error: 2.168404e-19
- consistent tangent vs central finite difference: 2.568376e-10
- finite stress Mises vs polynomial target: 1.601223e-16
- nu=0.5 reduction to Chen-Ji: exact
- corrected yield-interface stress jump: 0
- corrected yield-interface Mises/fy deviation: 3.330669e-16

M5 corrected operator = PASS.

## M5-5 applicability
后续必须监测 d ebar_i/dq 与 Mises-strain direction change。若主要塑性承载区出现大范围卸载或显著非比例/反转，只升级 steel material operator 到 plane-stress J2 flow + return mapping；结构级 q,A+,A- 不变。

正式 Q355 plastic polynomial Ps 的高阶系数尚未冻结；M5 diagnostic law 不是生产材性。M6 可保留 Ps 为材料输入接口，M8 前依据真实材性冻结，禁止按 Pu 拟合。

## NEXT_ACTION
M6：组装 M4 UHPC analytic operator + M5 steel consistent secant-Mises operator + M3 C/S/B frequency-generated inner enrichment；形成 inner membrane residual、outer Rq/RA+/RA- 与 exact Schur-condensed Jacobian。
