# NZ-SCCM — 正膜效应屈后刚度与尺度层级恢复锁

**时间：2026-08-17 00:02 +08:00**

## 恢复的高优先级规则

```text
CLASSICAL_FVK_MEMBRANE_POSTBUCKLING_SIGN = POSITIVE
EDGEWARD_AXIAL_STRESS_REDISTRIBUTION = REQUIRED
MEMBRANE_REDISRIBUTION_MUST_NOT_BE_MODELED_AS_ARBITRARY_FREE_RELAXATION = REQUIRED
P20_P02_INDEPENDENT_FREE_RELAXATION = RETIRED
FIVE_TERM_ELASTIC_AIRY_LIMIT = RETAINED / EXACT
UNCONSTRAINED_NONLINEAR_FIVE_COORDINATE_CONDENSATION = REOPENED
```

## 尺度趋势

同一 one-complete-halfwave 几何驱动

`M=pi^2/eps0*(q0*q+q^2/2)`

历史冻结尺度：

```text
Case21 M=.02869338081, (M/4)/D=.85814%
Z6     M=1.69487261562, (M/4)/D=26.7275%
ratio  =59.0684
```

因此当前理论必须恢复：

```text
CASE21_MEMBRANE_REDISTRIBUTION = SMALL_PERTURBATION_EXPECTATION
Z6_MEMBRANE_REDISTRIBUTION = FIRST_ORDER / STRONG_EFFECT_EXPECTATION
HIGH_b_over_t_MEMBRANE_EFFECT = STRONGER_THAN_LOW_b_over_t
```

这里的“effect”是对正确 compatibility/equilibrium/boundary-admissible postbuckling reserve 的作用，不允许以结构试验荷载反标幅值。

## 近期结果身份

```text
Case21 320.749185 kN = RETRACTED_AS_PHYSICAL_MEMBRANE_Pu / DIAGNOSTIC_ONLY
Z6 43.762840 MN      = RETRACTED_AS_PHYSICAL_MEMBRANE_Pu / DIAGNOSTIC_ONLY
```

理由：两者来自当前 nonlinear five-coordinate free-condensation implementation，其向下软化与已锁定的经典正屈后刚度及尺度层级冲突。

## 禁止事项

```text
DO_NOT_TUNE_R10_TO_FIX_THIS = YES
DO_NOT_FIT_MEMBRANE_AMPLITUDES_TO_Pu = YES
DO_NOT_REINTERPRET_DOWNSHIFT_AS_NEW_PHYSICS = YES
DO_NOT_REOPEN_ENDLESS_BACKEND_DEVELOPMENT = YES
DO_NOT_COMPUTE_NEW_MEMBRANE_Pu_BEFORE_CLOSURE_RECOVERY = YES
```

## 唯一下一门禁

`RECOVER_COMPATIBILITY_COUPLED_CURRENT_MEMBRANE_CLOSURE_FROM_1848_1912_TRANSITION`

比较并逐式追踪：

1. 2026-08-16 18:48 historical backbone + exact membrane delta；
2. 2026-08-16 19:12 five-term elastic condensation；
3. 后续 current-material `Rm=0` runtime；

找出 classic Airy coupling / boundary work / compatibility constraint 在 nonlinear promotion 中丢失的位置。修复必须先通过 elastic positive-postbuckling degeneration，再进入 Case21/Z6 Pu。
