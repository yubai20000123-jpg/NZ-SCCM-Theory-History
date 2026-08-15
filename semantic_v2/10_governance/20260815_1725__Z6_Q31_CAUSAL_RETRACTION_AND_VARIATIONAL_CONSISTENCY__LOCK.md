# Z6 q31 causal retraction and variational-consistency lock

**Timestamp:** 2026-08-15 17:25 +08:00

## Correction

The 16:47 higher-harmonic execution established only that a manually constructed virtual `q31` direction produced a nonzero generalized work when evaluated on the old single-q current stress field. It did **not** establish that releasing q31 increases ultimate capacity or explains the Z6 underprediction.

The previous wording `MISSING_Q31_FINITE_AMPLITUDE_DIRECTION = CONFIRMED MODEL-SPACE DEFICIENCY` is therefore retracted as a causal statement.

## Variational/Ritz boundary

For a conservative elastic system, restricting the admissible displacement space in a Rayleigh-Ritz formulation generally produces an upper-bound tendency for the critical eigenvalue / an artificially stiff kinematic response. Therefore modal restriction cannot be invoked, without a complete coupled calculation, as an explanation for a **lower** predicted capacity.

For the present nonlinear current-material problem there is no proven monotonic upper/lower bound for peak Pu, but the sign of the capacity correction must be demonstrated, not assumed.

## Additional flaw in the 16:47 q31 gate

The q31 first-variation test modified the out-of-plane field direction while retaining the old reduced in-plane/generalized field structure. A variationally consistent multimode extension would require the full admissible displacement field (including any associated in-plane harmonics / condensed membrane variables) to be redefined and re-equilibrated before interpreting the generalized work as a true derivative of the reduced potential or residual manifold.

Moreover, the current `sigma=M(epsilon)` operator has not been formally proven to derive from a scalar hyperelastic potential over the full nonlinear range, so energy-stationarity language must not be used beyond what the virtual-work residual actually proves.

## Current decisions

```text
FE_FIRST_MODE_IMPERFECTION_LOCKS_POSTBUCKLING_SHAPE = FALSE
FE_CAN_DEVELOP_SHAPE_CHANGES = TRUE
Q31_NONZERO_GENERALIZED_WORK_AT_OLD_STATE = DIAGNOSTIC FACT ONLY
Q31_AS_CAUSE_OF_Z6_LOW_PU = NOT ESTABLISHED
SINGLE_Q_CAUSES_CONSERVATIVE_BIAS = RETRACTED
NGUYEN_SECOND_ORDER_AS_PRIMARY_CAUSE = NOT SUPPORTED
ORIGINAL_ONE_COMPLETE_HALFWAVE_BASELINE = RESTORED AS CURRENT PRODUCTION BASELINE
```

## Next causal priority

Before any multimode promotion, return to causes capable of explaining why Z6 is uniquely low while Z0-Z4 remain accurate:

1. exact source identity / applicability of the constructed Z6 extreme-corner combination;
2. discrete internal-web topology versus the homogenized/reduced NZ object in deep high-b/h postbuckling;
3. full incremental ideal-elastoplastic redistribution versus the present path-independent radial-cap current map;
4. concrete current-tangent / geometric-stiffness balance on the valid Z6 branch;
5. only then, if required, a fully variationally consistent multimode Ritz extension with all associated in-plane fields.

No empirical correction or material retuning is authorized.
