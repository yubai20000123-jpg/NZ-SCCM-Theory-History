# Case21 current result — Airy-scalar current-R10 membrane closure

**Updated:** 2026-08-17 02:10 +08:00

## Active mechanics

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order continuous kinematics
frozen R10 ordinary-concrete current operator
two-way reinforcement included before solve
current membrane redistribution r=lambda*M*a(nu)
Rq=0 and RA=a^T Rm=0
```

with

\[
M=\frac{\pi^2}{\varepsilon_0}\left(q_0q+\frac12q^2\right),
\]

\[
a(0.18)=[-0.295,-0.205,+0.25,-0.205,+0.25]^T.
\]

The previous five-free-current-amplitude nonlinear Case21 route is superseded because it develops large non-Airy relaxation states under frozen R10.

## Current direct-source mechanics result

```text
D_u = 0.78879248
q_u = 0.0018083573
lambda_u = 0.08623596
M_u = 0.02907033478
A_increment = 2.20620 mm
A_total = 5.25620 mm

r_u = [-0.00073954,
       -0.00051392,
       +0.00062673,
       -0.00051392,
       +0.00062673]

Pc = 337.923030 kN
Ps =  28.844798 kN
Pu = 366.767829 kN
```

Equilibrium at the same state:

```text
Rq ~= 6.3e-13 kN mm
RA ~= 3.6e-15
```

Steel remains elastic.

Experiment:

```text
P_exp = 368.312750 kN
Delta = -1.544921 kN
error = -0.41946 %
```

Direct frozen-R10 constrained `r=0` comparison:

```text
P_r0 ~= 368.731457 kN
membrane redistribution delta = -1.96363 kN = -0.53254 %
```

## Identity of this number

`366.767829 kN` is the current **direct-source mechanics target** obtained from a highly refined independent continuum audit of the frozen R10 equations. The Gauss-Legendre audit executor is not the formal zero-spatial-quadrature operator.

Formal counters remain

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```

Formal compact analytic numerical release remains separate from this mechanics result; no experimental calibration was used.

## Canonical detailed evidence

- `../../semantic_v2/40_execution/common/20260817_0210__NZSCCM__CASE21_AIRY_SCALAR_CURRENT_R10_CONTINUATION__EXECUTION_REPORT.md`
- `../../semantic_v2/40_execution/common/20260817_0210__NZSCCM__CASE21_AIRY_SCALAR_CURRENT_R10_CONTINUATION__PARAMS_AND_RESULTS.json`
- `../../semantic_v2/40_execution/common/20260817_0210__NZSCCM__CASE21_AIRY_SCALAR_CURRENT_R10_CONTINUATION__REPRO.py`
- `../../semantic_v2/10_governance/20260817_0210__NZSCCM__CASE21_AIRY_SCALAR_CURRENT_MEMBRANE_CLOSURE__LOCK.md`
