# NZ-SCCM — Airy 分区积分闭合与避开 CC/TC/TT 的替代材料路线审计 R01

**Time:** 2026-08-23 20:48 +08:00  
**Status:** `AIRY_REGION_D15_CLOSURE = FAIL_GENERIC / SPECIAL_FUNCTION_CLOSURE = POSSIBLE_BUT_REOPENS_ELLIPTIC_ABELIAN_COMPLEXITY / CC_TC_TT_IS_NOT_PHYSICALLY_MANDATORY / MATERIAL_ALTERNATIVE_SEARCH = OPEN_WITH_PRIORITY_CANDIDATES`

## 0. 目的

承接 `PURE_AIRY_PARTITION_COMPLEXITY_AUDIT_R01`，只回答两个问题：

1. Airy 已显式给出的 conic / quartic 区域边界，能否继续保持当前所需的有限初等/D15 型零空间积分；
2. 若不能，是否存在文献中的混凝土材料框架能够绕开 Nguyen/Foster 的 CC/TC/TT/TCX 状态机，而仍保留多轴非线性。

本轮不计算 Pu，不修改 Airy/Marguerre，不用试验荷载选模型。

---

## 1. 最简单 conic 子问题已经足以否定 generic D15 closure

上一轮上下表面分量应变零线在

\[
u=\sin X,\qquad v=\sin Y
\]

中具有

\[
C+A u^2+B v^2+Luv=0.
\]

为了判断“区域知道以后是否仍能简单解析积分”，不需要处理最一般的 `L != 0`。只取更简单的合法子类

\[
L=0,
\qquad
v_b^2=a+b u^2,
\qquad 0<a,\quad 0<a+b<1.
\]

考虑最简单的区域面积贡献（若连常数 integrand 都不属于有限三角矩族，则更复杂材料 integrand 更不可能自动属于该族）：

\[
I(a,b)=\int_0^{\pi/2}\arcsin\!\sqrt{a+b\sin^2X}\,dX.
\]

对参数 `a` 求导：

\[
\frac{\partial I}{\partial a}
=\frac12\int_0^{\pi/2}
\frac{dX}
{\sqrt{a+b\sin^2X}\sqrt{1-a-b\sin^2X}}.
\]

令

\[
t=\tan X,
\]

则

\[
\frac{\partial I}{\partial a}
=\frac12\int_0^\infty
\frac{dt}
{\sqrt{a+(a+b)t^2}\sqrt{(1-a)+(1-a-b)t^2}}.
\]

再令

\[
t=\sqrt{\frac{a}{a+b}}\tan\theta,
\]

可严格化成

\[
\boxed{
\frac{\partial I}{\partial a}
=
\frac{1}{2\sqrt{(a+b)(1-a)}}
K\!\left(
\frac{b}{(a+b)(1-a)}
\right)
}
\]

其中 `K(m)` 为第一类完全椭圆积分。

因此，即便 Airy 区域边界只是最简单的无 `uv` conic，区域面积本身的参数导数已经 generic 地进入 elliptic class。除 `b=0`、退化直线、特殊完全平方等非一般情形外，它不再属于有限初等三角矩/D15 closure。

结论：

```text
AIRY_CONIC_FRONT_KNOWN_EXPLICITLY = YES
CONIC_REGION_ELEMENTARY_D15_INTEGRAL = NO, GENERICALLY
```

这不是 CAS 能力不足，而是积分函数类已经改变。

---

## 2. `L != 0` conic 不会变简单

一般边界

\[
C+A u^2+B v^2+Luv=0
\]

给

\[
v(u)=\frac{-Lu\pm\sqrt{(L^2-4AB)u^2-4BC}}{2B}.
\]

在原坐标面积元

\[
dxdy=\frac{dudv}{\alpha\beta\sqrt{1-u^2}\sqrt{1-v^2}}
\]

下，先对 `v` 积分产生 `arcsin v(u)`，外层再对 `u` 积分。其最简单 `L=0` 子类已经是椭圆积分，故一般 `L != 0` 不可能获得统一的有限 D15 closure。

---

## 3. 真正 CC/TC/TT 主应变前沿更复杂

若保留表面剪切，真实主应变变号满足

\[
\varepsilon_x^\zeta\varepsilon_y^\zeta
-\left(\frac{\gamma_{xy}^\zeta}{2}\right)^2=0.
\]

在 `(u,v)` 中它 generic 为四次代数曲线

\[
F_4(u,v;q)=0.
\]

固定 `u` 后，`v` 一般由四次代数根给出；区域积分继续包含 `arcsin(v_k(u))` 与代数根。它可以在“更广义的特殊函数意义”下做解析研究，但已经重新进入 elliptic / Abelian / algebraic-period 类型问题。

因此本轮裁决不是“数学上绝对不能积分”，而是：

\[
\boxed{
\text{Airy 分区没有把正式结构积分重新带回有限 D15/初等解析域。}
}
\]

若坚持完整 CC/TC/TT 空间前沿并要求零数值积分，就会重新打开此前已经付出很高成本的特殊函数后端路线，而不是获得一次简化。

---

## 4. 因此 Airy 分区猜想的最终身份

保留：

- Airy 可显式给出 `Nx,Ny,Mx,My` 受力区域；
- resultant 分区最多是规则矩形，适合审计与物理解释；
- 表面应变前沿也是有限显式代数曲线。

否决作为 production integration cure：

- 用真正 CC/TC/TT 前沿切全板，再逐区 exact-integrate，generic 不回到 D15；
- 每区独立平衡继续否决；
- 逐区贡献汇总一个 global residual 在力学上成立，但解析复杂度没有被根治。

```text
AIRY_FORCE_PARTITION = RETAIN_FOR_MECHANICS/AUDIT
AIRY_MATERIAL_PARTITION_AS_D15_CURE = FAIL_GENERIC
```

---

## 5. Nguyen 的 CC/TC/TT/CC/TCX 不是混凝土力学的唯一必然表达

Nguyen Chapter 3 明确把混凝土组织成 undamaged、cracked TC、cracked TT、crushed CC、crushed TCX 等状态；未损伤部分继承 Darwin–Pecknold equivalent-uniaxial strain，裂后 TC 又引入 Vecchio–Collins compression softening 等。该状态体系对解释二阶稳定过程中“裂化—压碎—切线变化”很有帮助，但它是一个 constitutive architecture choice，不是平面混凝土必须使用的唯一数学形式。

项目既有 state-equation ledger 也已指出：Nguyen U-TC/U-CC 含局部 secant unknowns，裂后分支又携带 crack/peak history fields，因此它对 strict zero-spatial-quadrature full-domain production 不友好。

---

## 6. 文献检索：可绕开显式 CC/TC/TT 状态机的候选

### 6.1 Cedolin–Mulas 1984 — 当前最匹配“显式 current strain”目标的候选

`Biaxial Stress-Strain Relation for Concrete`, J. Eng. Mech. 110(2), 187–206.

来源摘要明确：

- monotonic biaxial loading；
- total, explicit stress–strain relation；
- nonlinear bulk/shear moduli written as functions of the first two strain invariants；
- plane-stress transverse strain is eliminated by an explicit empirical approximation；
- final relation depends on only three concrete parameters；
- accurate up to/close to peak stress, including inelastic dilatancy.

优点：

```text
NO CC/TC/TT DISPATCH
NO CRACK-HISTORY STATE MACHINE
CURRENT TOTAL STRAIN -> STRESS EXPLICITLY
INVARIANT/TENSOR FORM
PLANE-STRESS SPECIFIC EXPLICIT ELIMINATION
```

硬缺点：

```text
MONOTONIC
UP TO PEAK STRESS
NO COMPLETE POSTPEAK / TENSION-SOFTENING LAW IN ORIGINAL PAPER
```

因此它不能直接被称为最终 Pu 材料，但非常适合作为新材料骨架候选。

### 6.2 Bažant–Tsubaki 1980 — 比 Cedolin–Mulas 更值得重新审计的“总应变大应变/峰后”候选

`Total Strain Theory and Path-Dependence of Concrete`, J. Eng. Mech. Div. 106(6), 1151–1173.

来源摘要明确：

- algebraic relation between total strains and stresses，类似 deformation theory；
- unloading is not modeled；
- gives peak stress points、failure envelopes、strain softening、inelastic dilatancy；
- applies to substantially larger strains than earlier total-strain models；
- optional corrective path-dependent terms vanish under proportional loading。

这意味着，如果本项目正式接受“忽略历史/卸载，只处理单调轴压首次极限”，该模型在概念上比 Nguyen 状态机更接近目标，而且比 Cedolin–Mulas 原始 1984 模型覆盖更深的峰后域。

关键待审计问题：

1. 去掉 path-dependent correction 后，Airy 局部加载是否可接受地视为 total-strain current law；
2. plane-stress specialization 是否可显式消元；
3. 其 algebraic stress–strain relation 的解析复杂度是否低于当前 Nguyen state machine；
4. 文中“free of continuous cracks”的适用边界对 RC wall ultimate 是否可接受。

### 6.3 Ottosen 1979 — 单一 nonlinear-elastic all-stress-state 模型

`Constitutive Model for Short-Time Loading of Concrete`, J. Eng. Mech. Div. 105(1), 127–141.

来源摘要明确：

- nonlinear elasticity；
- secant Young modulus and Poisson ratio vary through a nonlinearity index；
- nonlinearity index relates current stress state to a smooth failure surface；
- uses all three stress invariants；
- handles all stress states including tensile stresses；
- simulates hardening, failure and post-failure softening；
- calibration needs essentially uniaxial compression/tension data.

优点：没有 Nguyen 式 `U/TC/TT/CC/TCX` 状态机，且覆盖峰后。

硬缺点：材料参数依赖 current **stress** state/failure surface，故从给定 strain 到 stress 通常是隐式 local solve，而不是 Cedolin–Mulas 式直接显式 strain map。对本项目“Airy strain explicit -> material explicit”目标，这一点可能成为新的局部非线性瓶颈。

### 6.4 Kupfer–Gerstle 1973 — 统一 isotropic invariant deformation relation

`Behavior of Concrete under Biaxial Stresses`, J. Eng. Mech. Div. 99(4), 853–866.

来源摘要：把 stress/strain 分为 hydrostatic 与 deviatoric 部分，用 bulk/shear moduli 描述；这些 moduli 可写成 octahedral shear stress 的函数，并给出 tangent/secant matrix。

优点：统一 invariant/isotropic 描述，不依赖 Nguyen 的裂化状态名称。

不足：主要描述到 failure stage，且 moduli 是 stress-based；对 `strain -> stress` 的显式性不如 Cedolin–Mulas。

---

## 7. 明确不适合当前目标的替代路线

### Romstad–Taylor–Herrmann 1974

虽然转到 strain space，但本身用四个 damage regions、incremental law、cumulative damage 思想；只是换了一套分区，不解决根问题。

### Microplane / CDP / Menétrey–Willam damage-plasticity / endochronic

这些模型能够避免 CC/TC/TT 名称，但通常需要：

- internal variables/history；
- return mapping / incremental update；
- orientation quadrature 或其他材料积分。

与当前“current-state、低维显式、零材料点历史”的目标不匹配，暂不作为首选。

### Darwin–Pecknold 1977

其 monotonic biaxial equivalent-uniaxial concept仍有价值，也是 Nguyen undamaged branch 的来源，但如果继续外接 cracking/crushing state machine，就会重新回到当前困难；因此只保留为 baseline/benchmark，不作为“避开 CC/TC/TT”的最终答案。

---

## 8. 当前推荐顺序

不继续投入 Airy quartic-region exact integration。

材料替代审计按以下顺序执行：

1. **Cedolin–Mulas 1984**：先恢复完整 plane-stress explicit total-strain formula，检查 `eps -> sigma`、consistent tangent、原点 Poisson tangent、单轴/双轴峰值与解析复杂度。
2. **Bažant–Tsubaki 1980**：重点检查其 algebraic total-strain law 能否在忽略 path correction 后覆盖峰后，并比较解析复杂度。
3. **Ottosen 1979**：若前两者不足，再判断 stress-based implicit nonlinear elasticity 是否能被有限显式/代数消元。
4. Kupfer–Gerstle 1973 作为 invariant deformation benchmark。

判据不是哪个模型对 Swartz 误差更小，而是：

```text
A. 不依赖 CC/TC/TT/TCX history dispatcher
B. 当前 strain 能唯一确定 current stress
C. plane-stress 可显式或有限代数闭合
D. consistent tangent 可由同一表达求导
E. 单调首次极限范围覆盖足够
F. 与 Airy finite-trigonometric strain field 复合后，不重新制造更重的空间状态前沿
```

---

## 9. 最终裁决

```text
AIRY_PARTITION_KNOWS_REGIONS = TRUE
AIRY_CONIC_REGION_D15_CLOSURE = FAIL_GENERIC
TRUE_QUARTIC_CC_TC_TT_REGION_D15_CLOSURE = FAIL_GENERIC
ELLIPTIC/ABELIAN_SPECIAL_FUNCTION_ROUTE = MATHEMATICALLY POSSIBLE, STRATEGICALLY NOT A SIMPLIFICATION
NGUYEN_CC_TC_TT_ARCHITECTURE = RETAIN_AS_PHYSICAL/REGRESSION_REFERENCE, NOT SACROSANCT
PRIMARY_ESCAPE_CANDIDATE_1 = CEDOLIN_MULAS_1984
PRIMARY_ESCAPE_CANDIDATE_2 = BAZANT_TSUBAKI_1980
SECONDARY_ESCAPE_CANDIDATE = OTTOSEN_1979
```

下一步不应再算 Pu；应先完成 Cedolin–Mulas 1984 与 Bažant–Tsubaki 1980 的公式级恢复和“是否真的可作为 current explicit plane-stress operator”的门禁。