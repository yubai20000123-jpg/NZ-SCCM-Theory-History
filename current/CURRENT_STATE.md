# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-15 16:47 +08:00  
**Status:** LEGACY MUTABLE POINTER ONLY

The operational project entry is now:

`semantic_v2/00_index/20260815_1647__NZSCCM__PROJECT__CURRENT_STATE_AND_Q31_STATIONARITY__SEMANTIC_INDEX.md`

Current Z6 decisions:

```text
Nguyen second-order kinematics as primary Z6 cause = NOT SUPPORTED
wrong linear m=1 halfwave as primary cause = NOT SUPPORTED
high-slenderness unchanged-method bias = SUPPORTED
single-q11 state stationary in q31 direction = FAIL
missing finite-amplitude longitudinal q31 direction = CONFIRMED MODEL-SPACE DEFICIENCY
q13 third-transverse direction = SECONDARY in current first-variation gate
full q11+q31 Pu recovery = NOT YET QUANTIFIED
```

Key zero-spatial first-variation results:

```text
S3 lambda=1.2154: eta31=0.01014
S4 lambda=1.3625: eta31=0.01998
Z6 lambda=1.4341: eta31=0.02527
Z6 eta13=0.00332
```

At Z6, the q11 equilibrium self-check gives `|Rq11|/(Pb) ~= 3.4e-7`, while `|Rq31|/(Pb) ~= 2.53e-2`. Thus the current state is an equilibrium in the one-q subspace but not in the enlarged Nguyen modal space.

`q31=+-1e-5` gives a local tangent predictor `q31~=-3.30e-4` (~-5.6% of q11), but naive finite-q31 polynomial composition becomes ill-conditioned before a trustworthy coupled root is obtained. No two-mode Pu is released.

Current next task:

```text
Z6_Q11_Q31_SPARSE_HARMONIC_EXACT_MOMENT_COUPLED_EQUILIBRIUM
```

Parent material laws remain unchanged; formal structural spatial sampling/quadrature remain zero.
