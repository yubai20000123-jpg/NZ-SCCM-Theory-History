# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-15 after Z6 squat-panel boundary audit  
**Status:** LEGACY MUTABLE POINTER ONLY

Current Z6 correction:

```text
Nguyen second-order kinematics as primary Z6 cause = NOT SUPPORTED
wrong m=1 halfwave as primary cause = NOT SUPPORTED
q31 as the cause of low Z6 Pu = NOT ESTABLISHED
single-q finite-amplitude restriction as explanation for conservative Pu = RETRACTED
original one-complete-halfwave production baseline = RETAINED
```

Geometry/source identity:

```text
Z6: a=9000 mm, b=12000 mm, h=130 mm, a/b=0.75
compression acts along the shorter in-plane dimension
classical m=1 at a/b=0.75 = CONSISTENT
Zhou Group-4 exact input combination (9000,12000,130,60) = STRONGLY SOURCE-SUPPORTED
unique raw FE model ID / raw FE Pu = NOT RECOVERED
49.6724359 MN = Zhou fitted lower-envelope value, not raw FE Pu
```

New confirmed kinematic mismatch:

```text
CURRENT NZ base membrane field at q=0:
ex = nu D
ey = -D
=> sigma_x = 0 in elastic plane stress
=> globally free transverse Poisson state

ZHOU four-edge FE loaded edges:
u_x = 0 on y=0 and y=a
non-loaded side edges: u_x free

Therefore current affine/free-Poisson in-plane field is NOT admissible under Zhou's actual loaded-edge in-plane boundary condition.
BOUNDARY_KINEMATICS_MISMATCH = CONFIRMED
```

Why Z6 exposes it:

```text
a/b=0.75 => squat finite panel; loaded-edge restraint zones can occupy a large part of the panel
Z4 also has a/b=0.75 but is much stockier / less stability-controlled
therefore a/b<1 alone is not the cause
primary diagnostic interaction = squat geometry x high global slenderness x wrong in-plane admissibility
```

Current next causal test — before changing material theory, steel law, D15, or adding out-of-plane modes:

```text
1. construct the lowest-order continuous in-plane field satisfying u(x,0)=u(x,a)=0 and the Zhou side-edge conditions
2. analytically/variationally condense its amplitude(s); formal structural sampling/quadrature remain zero
3. keep the same m=1 complete out-of-plane halfwave, R10/N48-C1-MM/Cayley-Hamilton/General-D15, steel current map and imperfection contract
4. recompute Z6
5. recompute Z4 as same-a/b control
6. accept the mechanism only if Z6 changes substantially in the required direction while Z4 remains comparatively stable
```

Frozen parent identity remains:

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order
R10 / N48-C1-MM / Cayley-Hamilton / General D15 unchanged
formal structural spatial sampling = 0
formal structural quadrature = 0
no Zhou/Winter calibration
```

Current audit artifacts:

- `semantic_v2/10_governance/20260815_1725__Z6_Q31_CAUSAL_RETRACTION_AND_VARIATIONAL_CONSISTENCY__LOCK.md`
- `semantic_v2/60_validation/steel_shell/20260815_1731__NZSCCM__Z6__ASPECT_RATIO_AND_HALFWAVE_IDENTITY__AUDIT.md`

The boundary mismatch is a proven formulation inconsistency. Its quantitative responsibility for the approximately -24.5% Z6 Pu gap is still open until the boundary-admissible same-theory rerun is completed.
