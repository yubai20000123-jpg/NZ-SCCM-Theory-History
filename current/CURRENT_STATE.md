# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-10 22:25 +08:00  
**Purpose:** 唯一当前工作入口。详细推导、历史偏离/恢复、失败 compiler 与执行证据留在 canonical governance/theory/history/evidence 文件中。

## 0. 最高优先级：EXPLICIT END-TO-END CAPACITY

Canonical current files:

- `governance/EXPLICIT_END_TO_END_CAPACITY_DOCTRINE_20260810.md`
- `governance/USER_SKETCH_SHAPE_PRESERVING_SMOOTHING_RULE_20260810.md`
- `governance/R09A_TENSION_SENSITIVITY_DECISION_20260810.md`
- `current/theory/NZ_SCCM_USER_SKETCH_SMOOTH_AND_RC_CASE21_R08_20260810.md`
- `current/theory/NZ_SCCM_R09A_TENSION_SATURATION_SENSITIVITY_20260810.md`
- `current/theory/NZ_SCCM_R09A_TENSION_SATURATION_SENSITIVITY_results.json`

User highest requirement:

```text
最终极限承载力必须由显式公式及同一公式的显式导数得到。
```

允许使用 4D stress-strain manifold、invariant/spectral current map、whole-structure global target、低秩面、polynomial/rational/algebraic formula、named special functions、局部 analytic patch、显式 piecewise smooth function 等。

材料 pointwise regression error 不是首要目标。允许 deliberate under-use / smoothing / trimming 局部尖峰；必须透明说明削弱/增强的力学后果。

---

## 1. 最终容量方程

\[
P(D,q),\qquad R_q(D,q)=0,
\]

\[
L(D,q)=P_{,D}R_{q,q}-P_{,q}R_{q,D}=0,
\]

\[
P_u=P(D^*,q^*).
\]

`P,Rq,P_,D,P_,q,Rq_,D,Rq_,q` 必须来自同一显式数学表示。

结构层继续保留：

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
ACTIVE_MODE = m=1
KINEMATICS = NGUYEN_SECOND_ORDER
```

数值求根可用于求已经显式得到的有限方程。

---

## 2. MATERIAL-NATIVE DOMAIN GOVERNANCE

```text
PRIMARY_DOMAIN   = MATERIAL_ADMISSIBLE_SPECTRAL_DOMAIN Lambda_M
SECONDARY_DOMAIN = STRUCTURAL_REACHABLE_SUBDOMAIN Lambda_R
MANDATORY        = Lambda_R subset of Lambda_M
```

Case21/Swartz24 cannot define the production material domain.

NC source-active landmark interval remains recorded as

\[
\Lambda_{M,NC}^{active}=[-10,0.49987179453974245].
\]

UHPC must derive its own `Lambda_M`; NC numerical bounds must not be copied into UHPC.

---

## 3. Compression-side NC target — retained from R08

```text
lambda < -10         : residual -0.10 fc
-10 <= lambda < -1   : R06 C2 source-faithful postpeak target
-1 <= lambda < 0     : Saenz compression
```

The R06 C2 postpeak closure remains PASS.

The compression branch is currently treated as the primary direct-load carrier and is NOT modified by R09A.

---

## 4. R08 tensile prototype — retained as baseline only

R07R rational tensile regression is rejected because it created artificial `overshoot -> dip -> rebound`.

R08 replaced it by a shape-preserving rounded peak:

```text
one monotone rise -> one rounded peak -> monotone decay -> residual
```

with

\[
\lambda_p=x_{cr}=0.049987179454,
\quad u(\lambda_p)=0.09,
\]

\[
\lambda_r=10x_{cr}=0.49987179454,
\quad u(\lambda_r)=0.03.
\]

R08 remains a valid smooth baseline but is no longer the only preferred tensile shape after R09A.

---

## 5. R09A simple monotone tensile-saturation family

The user proposed an even more aggressive simplification: because axial-compression response is expected to be compression dominated, remove the distinct tensile peak/softening history and use a simple monotone saturation law.

R09A tested

\[
u_t(\lambda)=u_\infty\frac{r}{1+r},
\qquad r=\frac{\kappa\lambda}{u_\infty},
\qquad \lambda\ge0,
\]

with explicit derivative

\[
u_t'(\lambda)=\frac{\kappa}{(1+\kappa\lambda/u_\infty)^2}.
\]

Properties:

- `u_t(0)=0`;
- `u_t'(0)=kappa`;
- monotone;
- no sharp peak;
- no dip/rebound;
- one retained tensile-capacity parameter `u_inf`.

Predeclared sensitivity brackets:

```text
SAT03: u_inf = 0.03 fc
SAT05: u_inf = 0.05 fc
SAT07: u_inf = 0.07 fc
```

None was selected from Case21 experimental Pu.

---

## 6. Case21 reinforcement — analytic same-equation coupling

Source mapping:

```text
rho_x = rho_y = 0.00375
Es = 200000 MPa
fy = 530 MPa
eps_y = 0.00265
```

Let

\[
S=q_0q+\frac12q^2,
\qquad
C_m=\frac{\pi^2S}{\varepsilon_0}.
\]

Exact loading-direction steel load:

\[
P_s=
\frac{\rho_y t b E_s\varepsilon_0}{1000}
\left(D-\frac{C_m}{4}\right).
\]

Exact steel amplitude residual:

\[
R_s=
\frac{\rho_y tE_s\pi^2(q_0+q)b\ell}{1000}
\left[
\frac{\varepsilon_0D(\nu-1)}4
+\frac{9\pi^2S}{32}
\right].
\]

The total equations are always solved as

\[
P=P_c+P_s,
\qquad
R=R_c+R_s=0,
\]

then

\[
L=P_D R_q-P_qR_D=0.
\]

No post-addition `As fy` is permitted.

---

## 7. R09A executed Case21 RC sensitivity

All candidates use the same compression branch, geometry, reinforcement and explicit limit equations.

Results:

| candidate | tensile identity | D_u | q_u | Pc (kN) | Ps (kN) | Pu (kN) |
|---|---|---:|---:|---:|---:|---:|
| R08 | rounded 0.09 peak -> 0.03 residual | 0.706185 | 0.0165438 | 317.3033 | 18.2991 | 335.6024 |
| SAT03 | `u_inf=0.03` | 0.674303 | 0.0166825 | 305.3951 | 17.0068 | 322.4019 |
| SAT05 | `u_inf=0.05` | 0.732368 | 0.0175027 | 316.3733 | 18.4497 | 334.8230 |
| SAT07 | `u_inf=0.07` | 0.789742 | 0.0182769 | 325.9317 | 19.8795 | 345.8111 |

SAT03–SAT07 spread:

\[
\Delta P_u=23.409173\ \mathrm{kN},
\]

\[
\frac{\Delta P_u}{\overline P_u}=7.001495\%.
\]

All explicit stationary roots pass same-root audit residual checks and all reinforcement remains elastic.

---

## 8. R09A physical conclusion

The user's compression-dominance intuition is **partly correct**:

```text
COMPRESSION_DOMINATES_DIRECT_LOAD = PASS
```

At every stationary root, concrete compression carries roughly 305–326 kN, versus steel 17–20 kN.

However:

```text
TENSILE_CAPACITY_LEVEL_IS_NEGLIGIBLE = FAIL
```

Changing only `u_inf` from `0.03` to `0.07` changes Pu by about 7%.

Reason: the tensile law changes `D_u,q_u`, which changes the compression-side `Pc` itself. Therefore “tension carries little direct axial load” does NOT imply “the tensile constitutive branch has little influence on the coupled limit state”.

The important positive result is:

```text
TENSILE_SHAPE_CAN_BE_STRONGLY_SIMPLIFIED = PASS
```

The project does not need to restore the sharp source tensile peak, Foster transition details, or any oscillatory regression. A one-parameter monotone explicit law is sufficient as a shape family.

But its retained capacity level must be defined independently from structural experiment.

---

## 9. Formal-status boundary

R09A runtime `P,R,L` evaluation is finite and explicit.

Concrete local `Pc(D,q),Rc(D,q)` coefficients were identified offline using high-accuracy full-halfwave numerical integration, as in R08/R07R proof-of-concept.

Therefore:

```text
R09A_TENSION_SATURATION_SENSITIVITY = PASS_DIAGNOSTIC
ANALYTIC_REINFORCEMENT_COUPLING = PASS
EXPLICIT_P_R_L = PASS_DIAGNOSTIC
FORMAL_ZERO_SPATIAL_QUADRATURE_PRODUCTION = HOLD
```

This is not silently relabeled as the older pure-D15 production identity.

---

## 10. Multiaxial correction status

R08 had recommended jumping directly to a minimum source-grounded multiaxial correction.

R09A changes the order:

**do not add multiaxial correction yet.**

First freeze the single retained tensile-capacity level from material evidence or an explicit conservative material rule.

Only after that tensile scalar level is fixed independently of Case21/Swartz Pu should the project ask whether a small CC/TC multiaxial correction is still required.

---

## 11. UHPC implication

The R09A simplification philosophy is transferable to UHPC, but not the NC numerical plateau.

UHPC may also use a simple monotone explicit tension law if material evidence permits, but `u_inf,UHPC` must come from UHPC sources / a declared conservative UHPC rule and its own material-native domain.

NC `0.03/0.05/0.07` values are sensitivity brackets only and must not be copied into UHPC.

---

## 12. Current recommended next task

```text
CURRENT_RECOMMENDED_NEXT_TASK
= R09B_SOURCE_GROUNDED_TENSION_CAPACITY_LEVEL
```

R09B must:

1. keep the current compression branch fixed;
2. keep the simple monotone saturation tensile family;
3. derive/freeze one NC tensile-capacity level from material-source evidence or an explicitly declared conservative material convention;
4. not use Case21/Swartz Pu to select that level;
5. rerun the same explicit `P,R,L` chain only after the material-level decision;
6. then decide whether the minimum multiaxial correction remains necessary.

---

## 13. Recovery read order

1. `current/CURRENT_STATE.md`
2. `governance/EXPLICIT_END_TO_END_CAPACITY_DOCTRINE_20260810.md`
3. `governance/USER_SKETCH_SHAPE_PRESERVING_SMOOTHING_RULE_20260810.md`
4. `governance/R09A_TENSION_SENSITIVITY_DECISION_20260810.md`
5. `current/theory/NZ_SCCM_R09A_TENSION_SATURATION_SENSITIVITY_20260810.md`
6. `current/theory/NZ_SCCM_R09A_TENSION_SATURATION_SENSITIVITY_results.json`
7. R08 user-sketch + reinforcement files
8. R07R, then R06/R05/R04/R03/R02/R01 history/evidence
9. Case21 invariant exact-moment foundation
