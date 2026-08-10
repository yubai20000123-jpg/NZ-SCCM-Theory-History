# NZ-SCCM FULL STARTUP RECOVERY 与架构连续性纠偏 — 2026-08-10

**Status:** CURRENT RECOVERY CHECKPOINT / SUPERSEDES INCOMPLETE TASK-SCOPED UNDERSTANDING  
**Recovery baseline HEAD:** `22b3d39e74972ffcc66abede9691d65ba1732f22`

## 0. 本轮为什么执行 FULL_STARTUP_RECOVERY

近期工作只沿 `CURRENT_STATE -> M1R -> PF1 -> P2A` 局部恢复，导致把“平滑二维强度域 + invariant current map”误说成新路线。按照 `RECOVERY_PROTOCOL.md`，这种长期工程接管必须进入 FULL_STARTUP_RECOVERY，而不能用 TASK_SCOPED_RECOVERY 替代。

本轮实际执行：

1. 核验默认分支与 baseline HEAD；
2. 递归扫描当前 `main` 的 current / governance / evidence / history；
3. 读取 current state、source-of-truth、recovery、sync、priority reset；
4. 读取 NC、UHPC、steel-shell evidence maps；
5. 读取历史 component ledger、D/G 路线树、Case21 current/historical assets；
6. 按 `PRE_CLEAN_REPOSITORY_POINTER.md` 定位 pre-clean 历史资产；
7. 因项目历史证据优先级要求，再回 File Library 的原始 Conversation JSON/思想演化恢复工件，核验 G12-G31 active-main-branch 结论与中断身份。

本 checkpoint 的“FULL”指按仓库 recovery protocol 恢复到足以继续理论工作的完整项目状态，不等于把所有历史 PDF/ZIP/TXT 字节重新复制回 main。二进制原件仍按 catalog/File Library locator 按需读取。

---

## 1. 最关键纠偏：当前不是一条新 current-map 路线

真实材料语法演化为：

```text
G10  F=U+yC                  -> RETIRED
G11  F=U*B(y)                -> REJECTED
G12  F=U+xyD(x,y)            -> DIAGNOSTIC ONLY
G16  total-transverse TC     -> FAIL: Poisson false softening
G16R signed/excess coords    -> PARTIAL PASS, D not source-identifiable
G17  U+xyD mandatory grammar -> RETIRED
G18  invariant current map   -> ARCHITECTURE PASS
G19  G18 q4/q6 coefficients  -> FAIL, architecture retained
G20  C1 smooth conservative biaxial envelope + C1/C2 regularization
G21  NC mechanism inventory / stress+tangent+shape+domain gate
G22  high-order global polynomial implementation -> historical certificate PASS
G23-G25 compiler/performance experiments -> point/material surrogate not formal
G26  continuous moment-first D15 -> retained compiler architecture
G27  historical correction -> G18 invariant architecture restored explicitly
G28  M(epsilon)->analytic series->D15 exact moments -> PASS mechanism
G30  Pu uses same P,R_A,L direct analytic kernel -> operationally accepted
G31  uncracked Case21 Pu + UHPC-C0 artifact -> executed, not user-accepted
```

因此当前主干从来不是“重新发明一个二维 current map”。当前正式材料表示骨架早已是：

\[
\boxed{
\boldsymbol\sigma
=
U(\mathbf E_u)
+J_2\left[
A(J_1,J_2)\mathbf I+B(J_1,J_2)\mathbf E_u
\right]
}
\]

其中

\[
\mathbf E_u=
\frac{(1-\nu)\mathbf E+\nu\,\mathrm{tr}(\mathbf E)\mathbf I}{1-\nu^2},
\quad J_1=\mathrm{tr}\mathbf E_u,
\quad J_2=\det\mathbf E_u.
\]

G27 已明确：G19 否定的是 G18 的具体 q4/q6 anchor coefficients，不是上述 invariant architecture。

---

## 2. G20/G21 已经回答了“二维强度域是否可以平滑、保守”

G20 已建立：

- CC：平滑保守双压包络；
- TT：`p=8` 平滑超椭圆；
- TC：C1 Bernstein 曲线，与 TT/CC 两轴切线连续；
- NC 开裂轴：不再使用 `x>=0 -> sigma=0` 的人工尖角，而采用来源约束的 C1/C2 正则化；
- 强度包络只负责峰值/启动/转换几何，不能替代 current stress map，也不能用包络斜率生成 tangent。

G21 又锁定普通混凝土 project approximation：

```text
current/rotating principal surface instead of fixed-crack history
no independent Nguyen beta shear-retention state
C1/C2 regularization instead of source finite jumps
alpha2=0.3 conservative tension-stiffening
smooth conservative post-peak compression
no independent TCX history state
```

并要求材料必须同时通过：stress + tangent + shape + full-domain boundedness。

所以用户当前提出“允许一定拟合误差，并适度收缩 TC/TT 面域以获得平顺、偏保守 current surface”不是换路径，而是对既有 G18/G20/G27 路径中 **target surface 的允许保守化程度** 进一步明确。

---

## 3. G22 的正确身份

G22 曾得到单一全局有限多项式：

```text
sigma_i/fc = K180(e_i) * U70[(e_i+nu e_j)/(1-nu^2)] * M90(e_j) + H180(e_i)
```

历史 certificate：

```text
stress RMS  = 0.000655 fc
stress P95  = 0.001635 fc
tangent RMS = 0.021726
tangent P95 = 0.053346
D15 compatibility = PASS
```

它证明：统一连续 current target 在数学上可以被有限全局多项式实现，并且同一应力多项式可以解析产生一致切线。

但其 524 个编译系数、最高总代数次数约 340，以及后来 G27 的生产语法纠偏，使其当前身份为：

```text
G22_STRESS_TANGENT_CERTIFICATE = RETAINED_EVIDENCE
G22_KUMH_AS_CURRENT_PRODUCTION_GRAMMAR = DIAGNOSTIC_ONLY / NOT CURRENT FINAL
```

不能删除其证据，也不能把它重新冒充最终 material operator。

---

## 4. G23-G26 的真正贡献

G23-G25 显示：

- 把高阶连续材料直接 fully expand 再积分会 term explosion / catastrophic cancellation；
- point-cloud/material surrogate 可以快，但改变理论身份，不能进入正式 production。

G26 保留下来的正确方向是：

\[
\boxed{
\text{continuous material}
\rightarrow
\text{moment-first dual contraction}
\rightarrow
\text{D15 exact moments}
}
\]

并使用

\[
s=\sin^2X,\ t=\sin^2Y,\ \eta=\zeta^2,\ \chi=\sin X\sin Y\zeta
\]

的 parity-orthogonal algebra，避免 naive full expansion。

因此：

```text
NAIVE_EXPAND_THEN_INTEGRATE = REJECTED
MOMENT_FIRST_D15 = RETAINED
MATERIAL_POINT/PANEL_SURROGATE = REJECTED_FORMAL
```

---

## 5. G28-G31：积分/求解与材料闭合必须分开

G28 已证明：

\[
\mathbf E(X,Y,\zeta;D,A)
\to \boldsymbol\sigma=\mathcal M(\mathbf E)
\to \text{analytic series}
\to \text{D15 exact moments}
\to P(D,A),R_A(D,A)
\]

可以在零正式空间积分下成立。G28 自己把 remaining issue 写成：G18 `A(J1,J2),B(J1,J2)` production closure，而不是新的 integration problem。

G30 又进一步明确：

\[
\boxed{
R_A(D,A)=0,
\qquad
L=P_{,D}R_{A,A}-P_{,A}R_{A,D}=0
}
\]

可以使用同一 direct-series/D15 kernel 求 Pu，不需要第二套 load-step/arclength Pu solver。

高证据恢复身份：

```text
LATEST_FULLY_DELIVERED_STAGE       = G30
LATEST_OPERATIONALLY_ACCEPTED_STAGE = G30
LATEST_EXECUTED_ARTIFACT_STAGE     = G31
G31_FINAL_VISIBLE_DELIVERY         = ABSENT
G31_USER_ACCEPTANCE                = UNRESOLVED
```

G31 的 `Pu ~= 476.936 kN` 是故意忽略裂化的 mathematical-chain validation，不是 validated RC Pu；UHPC-C0 也是 calculable baseline，不是 production material operator。

---

## 6. 2026-08-09~10 后续工作如何接到同一主线上

后续 Case21 单域全局 Chebyshev、严格尾项、priority reset、invariant coordinate lift、M1/M1R、PF1、P2A 都发生在上述架构之后。

正确身份是：

- 它们是在尝试寻找 **更可控的 material compiler / exact analytic contraction**；
- 它们没有替代 G18/G27 的 invariant current-map architecture；
- PF1 R06 的 15x15/211-nonzero connection 只证明 rational compiler 的解析分类可研究，但 production complexity 失败；
- P2A 只否定 `degree<=16 single-global polynomial primitives U,C,C2,T,V` 这个 compiler family；
- P2A 失败不能推导出“统一 current map 失败”；
- 当前 source-shaped `U,C,C2,T,T^8` 也不能被误当成唯一必须永久忠实保存的物理材料面。

因此近期“不断换 compiler”的循环应停止，但停止的是 compiler 试撞，不是 invariant-current-map 主线。

---

## 7. FULL_STARTUP_RECOVERY 完成门禁 — 15项回答

### 7.1 当前项目最终目标

固定边界、单调轴压板的稳定临界与有限幅值极限承载；以连续完整代表半波、可信二维 current material map、一致切线和精确矩得到 `P,Rq,L`，不是通用 FE。

### 7.2 当前正式主线

```text
Nguyen second-order continuous kinematics
-> Eu / invariants J1,J2 (or equivalent I1,I2)
-> unified current map M(epsilon)
-> consistent tangent from same map
-> moment-first D15 / direct analytic contraction
-> P,Rq,L
-> all-real-root physical branch decision
```

### 7.3 当前推进阶段

结构/运动学/D15/根条件已形成；真正 production 2D material target/closure 仍是主要未闭合层。近期 PF1/P2A 是失败的 compiler experiments，不是新主线。

### 7.4 ordinary concrete operator 当前身份

- Nguyen/Foster current operator：benchmark/regression/source evidence；
- G18/G27 invariant architecture：ACTIVE ARCHITECTURE；
- G20/G21 smooth conservative material target principles：RETAINED CURRENT PHYSICS CONSTRAINTS；
- final compact `A_NC,B_NC` production closure：OPEN。

### 7.5 reinforcement 如何进入

必须在根方程之前：

\[
P=P_c+P_s,
\qquad
R_q=R_{q,c}+R_{q,s}.
\]

禁止事后 `Pu=Pu,c+As fy`。

### 7.6 UHPC 当前闭合程度

仅 `fc=141.1 MPa` 为用户强制保留值。Hiew/Liu/Leutbecher/周俊/王淑楠等材料证据已建立 source map；UHPC-C0 仅 executed calculable baseline；final multiaxial current operator OPEN。

### 7.7 steel-shell / Y / PBL

Yun Lu、Zhang Ning、Sun Lipeng source evidence 已保留；`M_shell` 尚未冻结。PBL 继续是强局部边界/子板分隔，不自动成为独立轴向承载项或 spring energy。production Y/shell 未开始。

### 7.8 Case21 当前正式身份

Case21 是 current structural/analytic benchmark。当前 `I1,I2` exact polynomial foundation 有效。历史 338/342 kN 只作 audit；G31 476.936 kN 只作 uncracked chain validation；当前没有新 production RC Pu 冻结。

### 7.9 Swartz24

当前 production 计算 PAUSED。G29 等历史 Pcr/旧全根表仅作历史/诊断；不得在 final material closure 前逐板调参或发布新的 Pu population。

### 7.10 当前锁定理论边界

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
m=1 representative halfwave lock
Nguyen second-order kinematics
zero formal spatial sampling/quadrature/cells
zero auxiliary quadrature/ODE propagation
no material-point production
moment-first D15
same-map analytic tangent
P,Rq,L low-dimensional structural unknowns
all-real-root physical branch discipline
no panel-load calibration
```

### 7.11 已淘汰路线

包括：旧 `U+xyD` mandatory grammar、G18 q4/q6具体系数、panel-level proxy、material-point production、naive full expansion、D15 UHPC Layer-0、为 Pu 另造 load-step/arclength solver、PF1 large connection production、P2A degree<=16 primitive compiler。

### 7.12 只能 audit/reference 的历史结果

G22 high-order KUMH、G23-G25 surrogates、G29 historical Pcr batch、G31 uncracked Pu/UHPC-C0、R02-R06 PF1 special-function systems、旧 338/342 kN Case21 roots。

### 7.13 当前关键 unresolved blocker

不是“还缺一种积分器”，而是：在既有 G18/G27 invariant architecture 与 G20/G21 smooth conservative material philosophy 下，如何冻结一个 **足够可信、允许合理保守误差、同时低复杂度直接可积** 的 2D current target/closure。

### 7.14 下一步最合理工作

不再执行 P2R basis search，也不再启动 D1-D3 式泛化审计循环。下一步只在现有路径内做：

```text
EXISTING_PATH_CONSERVATIVE_CURRENT_TARGET_REFORMULATION
```

目标：明确 CC/TC/TT/current postpeak 中哪些 material features 必须保留，哪些 TC/TT 区域可按用户允许的保守原则向内平滑收缩；然后再决定最小 `A(J1,J2),B(J1,J2)` closure。先定 target geometry/constraints，再谈 compiler；不换 architecture。

### 7.15 核查路径

优先：

- `current/CURRENT_STATE.md`
- `current/theory/NZ_SCCM_CASE21_INVARIANT_EXACT_MOMENTS_DERIVATION_V1_20260810.md`
- `current/theory/NZ_SCCM_CURRENT_OPERATOR_EXPLICIT_NC_REBAR_V1_20260809.md`
- `governance/PRIORITY_RESET_20260810.md`
- `history/ledgers/HISTORICAL_COMPONENT_LEDGER.md`
- `history/NZ_SCCM/G_series/G20/...`
- `history/NZ_SCCM/G_series/G21/...`
- `history/NZ_SCCM/G_series/G22/...`
- File Library `00_G27_历史纠偏与生产材料算子公式闭合.md`
- File Library `06_G28_gate.json` / G28 report
- File Library raw Conversation JSON / `NZ-SCCM思想演化恢复`
- File Library `00_G31_Case21_Pu全过程与UHPC_C0同步模型.md`
- `evidence/materials/NC/Nguyen_source_map.md`
- `evidence/materials/UHPC/`
- `evidence/steel_shell/`

因此：

```text
FULL_STARTUP_RECOVERY = PASS_FOR_PROJECT_CONTINUATION
BYTE_FOR_BYTE_BULK_HISTORY_REIMPORT = NOT_REQUIRED
```

---

## 8. 对 `ROOT_CAUSE_DIAGNOSTIC_PAUSE` 的纠偏

保留其中两个结论：

1. 禁止继续盲目换 compiler；
2. recent rational/PF/global-primitive difficulties 是复杂度搬运的真实证据。

但其“下一步 D1-D3 再审计材料来源”的要求被本 recovery checkpoint **部分 supersede**：G20/G21/G27 已经完成大量来源/机制/架构裁决，不能再次从零审计。

当前唯一合法的下一理论任务是现有路径内的 conservative target reformulation，不是另起炉灶，也不是再开一轮 source provenance loop。
