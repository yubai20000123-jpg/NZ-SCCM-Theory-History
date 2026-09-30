# UCFT M8 — generalized finite-trigonometric UHPC rational-Y production operator gate

执行时间：2026-09-30 21:15+08:00 起

## 1. 恢复状态

M0–M7 已通过。M8 输入冻结已通过；上一状态唯一求解器缺口为：M3 的 C/S/B compatible enrichment 使固定 X 下 UHPC directional strain 从 baseline 二次 active-set 扩展为有限三角多项式，因而 M4 原有 quadratic-in-sin(Y) analytic-Y kernel 不能直接用于 M8 production path。

本轮不改变 single-q、A+/A-、M3 compatible membrane、M5 steel、M6 residual/Schur，不使用 FEM/试验 Pu 标定。

## 2. 本轮实现

对固定 X，材料边界仍由

    e(Y) - e_j = 0

决定。采用

    t = tan(Y/2)

后，任一有限三角多项式严格化为普通多项式 P_j(t)=0，因此 active boundary 仍由代数求根取得，不是空间 Gauss 采样。

在每个已经分出的 active interval 内，厚度凝聚后的 UHPC resultants 含有有限 Fourier/Laurent 分子除以 sin(Y) 或 sin^2(Y)。本轮使用与半角有理原函数严格等价、但数值条件更好的有限谐波递推原函数：

p=1:

    Jc1(0)=ln tan(Y/2)
    Jc1(1)=ln sin Y
    Jc1(k)=Jc1(k-2)+2 cos((k-1)Y)/(k-1)

    Js1(0)=0
    Js1(1)=Y
    Js1(k)=Js1(k-2)+2 sin((k-1)Y)/(k-1)

p=2:

    Jc2(0)=-cot Y
    Jc2(1)=-csc Y
    Jc2(k)=Jc2(k-2)-2 Js1(k-1)

    Js2(0)=0
    Js2(1)=ln tan(Y/2)
    Js2(k)=Js2(k-2)+2 Jc1(k-1)

其中 Jc/Js 分别是 cos(kY)/sin^p(Y)、sin(kY)/sin^p(Y) 的原函数。由此，C/S/B enrichment 开启后仍保持：解析 thickness + algebraic active boundary + analytic/rational Y + 单一 deterministic X integral。

同一材料 polynomial branch 的上下表面采用精确 chi 因子消去，避免 q->0 或 active interval 端点附近的差分消去损失。

## 3. strict baseline regression

选取全压缩 baseline C1 状态，以旧 M4 J_n primitive 为严格基准：

- integral[ N ]：旧 = -8086.980331390181；新 = -8086.980331390180；相对差 = 1.125e-16
- integral[ N cos(2Y) ]：旧 = 357.1307991797434；新 = 357.13079917974244；相对差 = 2.706e-15

因此 generalized rational-Y -> baseline M4 analytic-Y 达到机器精度退化。

## 4. active-set independent diagnostic

独立诊断仅用于 benchmark，不进入 production definition。诊断采用直接材料函数 + 高阶厚度 Gauss + scipy adaptive Y integration，与解析 production operator 比较。

baseline active state，13 个区间：
- weight 1: N 3.008e-08, M 9.740e-08
- cos2Y: N 8.192e-09, M 1.039e-07
- sinY: N 1.085e-08, M 6.472e-08

enriched state (k=7,9,16)，17 个区间：
- weight 1: N 4.491e-08, M 6.585e-07
- cos2Y: N 1.016e-07, M 4.805e-07
- sinY: N 9.350e-08, M 3.815e-07

最大相对差 = 6.585e-07。诊断积分本身在个别项出现 roundoff warning，因此按 1e-6 gate 判定通过；production evaluator 本身不调用空间 Gauss。

## 5. high-harmonic boundary locator check

e(Y)=0.001 + 0.0008 cos7Y - 0.00045 sin9Y + 0.0003 cos16Y，对阈值 0.0012，代数 kernel 找到 9 个内部边界根，最大原三角方程残差 = 2.277e-18。

## 6. 裁决

M8_RATIONAL_Y_OPERATOR = PASS。

这关闭了上一状态唯一明确的 M4/M3 integration-interface gap。

但九试件 connected path 尚不能宣称完成：当前仓库中的 `UCFT_M6_residual_schur_assembler.py` 明确只是 residual/Jacobian/Schur 接口合同，并不包含完整 M3+M4+M5 物理积分 evaluator 和 q-continuation driver。因此不能伪造 BH005 的 N,m 或 P(q) 数值。

M8_PATH_SOLVER = PARTIAL。剩余点是实现集成，不是理论路线缺口。

## 7. 唯一 NEXT_ACTION

将本轮 production rational-Y operator 接入完整 M3/M4/M5/M6 evaluator，形成可实际计算 G,R,J 的固定-q 求解器；随后不增加新门，立即执行 BH005：

    perfect-local A0=0, N,m identification
    -> restore A0=0.225 b/1600
    -> imperfect connected q-path
    -> save P, Pc, Ps+, Ps-, A+, A-, active sets, residual/Jacobian diagnostics, derived Delta.
