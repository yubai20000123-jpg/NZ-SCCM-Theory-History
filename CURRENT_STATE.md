# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-10  
**Repository role:** authoritative current-state pointer; original literature/dialogue/artifacts remain higher evidence according to `SOURCE_OF_TRUTH_POLICY.md`.

## 1. Current project priority

The immediate production question is no longer “prove a theorem-level remainder bound as tightly as possible.” The current priority is to close Case21 with an engineering-analytic single-domain evaluator if it satisfies the final hard gates, then move to Swartz24 without per-panel calibration.

If the final single-domain route still has a blocker that materially changes the identity of `Pu`, stop patching the current operator and move to literature-driven **new material / new target function / new solution operator** design.

See:
- `governance/NZ_SCCM_PRIORITY_RESET_MATERIAL_OPERATOR_ARCHITECTURE_REVIEW_20260810.md`
- `snapshots/2026-08-10_R2/05_R2_FINAL_ATTEMPT_OR_NEW_OPERATOR.md`

## 2. Formal spatial identity

Locked for the current Case21/NZ-SCCM analytic branch:

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
```

`subdomains=1` means the entire continuous representative half-wave itself. Spatial cells, Gauss/Simpson/adaptive quadrature, Chebyshev collocation and material-point grids may be used only as independent numerical audits, never as the formal theory/evaluator.

## 3. Current ordinary-concrete + reinforcement benchmark

Authoritative benchmark contract:

`theory/current/NZ_SCCM_CURRENT_OPERATOR_EXPLICIT_NC_REBAR_V1_20260809.md`

Original MD SHA-256:
`98483fa75e828f57916b06fc708fc35fc7960fabbdebf4edb3e04aba10061bc6`

Executable helper:
`theory/current/nz_sccm_current_operator_explicit_v1.py`

Original PY SHA-256:
`740e8862b1f428e66c779ea17c2ffefdec1f53ae7da5b98f9d85669ea24811c2`

Material chain:

```text
engineering strain E
→ equivalent-uniaxial tensor Eu
→ normalized tensor X
→ principal lambda+/lambda-
→ smooth positive/negative coordinates Pi_eta
→ Saenz compression C
→ algebraic Foster tension H/T
→ uniaxial master U
→ biaxial interactions
→ spectral return
→ sigma = M_NC(epsilon)
```

The formal benchmark tension law is **algebraic Foster**, not the later exploratory tanh/sigmoid variant.

This operator is a **benchmark/reference current operator**, not a permanently final ordinary-concrete constitutive theory.

## 4. Case21 structural variables and ultimate-condition identity

Geometry/material benchmark:

```text
b = l = 1220 mm
t = 19.30 mm
A0 = 3.05 mm
q0 = A0/b = 0.0025
fc = 21.23 MPa
E0 = 20321 MPa
eps0 = 0.00209
nu = 0.18
```

Global unknowns:

```text
D
q = A/b
```

Nguyen second-order continuous half-wave kinematics is used. Concrete produces `Pc(D,q)` and `Rq,c(D,q)` over the same complete continuous half-wave.

Reinforcement benchmark:

```text
Es = 200000 MPa
eps_y = 0.00265
fy = 530 MPa
Ew = 0
eps_f = 0.04
rho_s,x = rho_s,y = 0.00375
z_s = 0
```

Reinforcement must enter both total load and amplitude residual before the RC root is solved:

```text
P = Pc + Ps
Rq = Rq,c + Rq,s
```

Formal ultimate/stability conditions:

```text
Rq(D,q) = 0
L(D,q) = P_,D Rq_,q - P_,q Rq_,D = 0
```

Never use `Pu = Pu,concrete + As fy` as the formal RC ultimate load.

## 5. Numerical reference values — verification only

Historical independent high-accuracy numerical references exist approximately at:

```text
concrete-only Pu ≈ 338.3184 kN
RC Pu ≈ 342.3339 kN
experiment Pf ≈ 368.3128 kN
```

These numbers are **audit/reference only**. They must not be used to choose analytic degree, select a root, tune material coefficients or calibrate the model.

The current model-to-experiment difference is on the order of several percent, which is one reason theorem-level integration error far below the model uncertainty is no longer a production hard gate.

## 6. Current single-domain final-attempt gates

Current route passes production only if all of the following remain true:

1. sampling=0, quadrature=0, spatial subdomains=1;
2. global analytic order is selected by internal convergence, not historical 338/342 or an audit target;
3. independent numerical audit is performed only after the formal result exists;
4. analytic/solver error is clearly smaller than material/structural model error; a theorem-tight outward-rounded remainder certificate is optional rather than an independent production gate;
5. the same evaluator handles concrete + reinforcement P/R/root and re-checks steel state;
6. no unresolved blocker materially changes `Pu` identity, including large Rq/root degree drift, audit-selected degree, required spatial splitting, provenance failure or structure-Pu calibration.

Pass identity:
`CURRENT_OPERATOR_SINGLE_DOMAIN_ROUTE = PASS`

Fail identity:
`CURRENT_OPERATOR_SINGLE_DOMAIN_ROUTE = TERMINATED_FOR_PRODUCTION`

## 7. Current known single-domain mathematical status

Scalar frozen material functions themselves show strong high-order global convergence. The difficult part has been nonlinear coefficient-tail validation after composition with the 3D continuous kinematics and especially the cancellation-sensitive `Rq` functional.

A single scalar Chebyshev l1 Banach tail bound was safe but far too pessimistic for `Rq`. Padding nonlinear products without restoring true missing high modes was rejected. Direct radical iteration on unvalidated truncated fields was also rejected because positivity can be lost.

The apparent spectral `1/R` singularity has been removed by symmetric divided-difference / matrix-function reformulation. Principal spectra are separated in the relevant Case21 parameter box, so spectral degeneracy is not currently the main blocker.

See:
- `cases/Case21/NZ_SCCM_CASE21_GLOBAL_AUDIT_HANDOFF_20260809.md`
- `cases/Case21/NEXTSTEP_EXECUTION_REPORT.md`

## 8. UHPC current evidence status

UHPC must not be represented by simply changing `fc` in the ordinary-concrete benchmark.

Current evidence registry includes at least:
- Hiew 2024 direct tension / unified tensile law;
- Liu biaxial / TC evidence;
- Lee 2017 biaxial tension-compression panel evidence;
- Leutbecher TC/path evidence;
- Zhou Jun triaxial/octrahedral/DP evidence;
- Wang Shunan triaxial / Willam-Warnke five-parameter failure evidence;
- Hu Wenxu historical UHPC uniaxial/interface source;
- FHWA UHPC engineering boundary source.

G16R historical parameter re-audit locked only `fc=141.1 MPa` as user-immutable at that stage; old `ft=7.3 MPa` was retired. However G16R did **not** identify a complete path-independent production 2D interaction surface. See:
- `materials/UHPC/audits/NZ_SCCM_G16R_signed_excess坐标_材料参数重审_U候选_D可识别性门禁.md`
- `materials/UHPC/audits/UHPC_STATE_EQUATION_LEDGER.csv`
- `materials/UHPC/audits/D19_LIU_TC_CLOSURE_MATRIX.csv`

Historical `UHPC-C0` is a calculable baseline, not the final multiaxial/path-dependent UHPC operator.

## 9. Steel shell / Y status

The current strict NC Case21 benchmark does not contain a final frozen steel-shell current law:

```text
M_shell = UNSPECIFIED BY CURRENT LOCKED SOURCE
```

This does **not** mean shell sources are absent. Historical source families include Yunlu local postbuckling/thin-membrane work, Zhang Ning PBL local stability and Sun Lipeng R-O/Bleich/PBL thin-wall theory. Those sources must be recovered before a next-generation shell operator is frozen.

PBL long-term Layer-0 role remains: strong local boundary / subpanel divider, not an independent axial-bearing term and not an explicit spring-energy term.

## 10. Long-term material/operator direction

Current promising material architecture is:

```text
C+ thermodynamic/internal-variable framework
+ E invariant/tensor-basis representation
```

with a compact symbolic/rational analytic law as an important analytic-friendly bridge/competitor. Concrete may require a thermodynamically admissible non-associated plasticity extension; classical associated GSM is not assumed sufficient.

Physics-constrained symbolic regression may help discover compact material potentials from **material-level** data. Neural constitutive/operator models are not the first analytic core and must not be trained to reproduce structural `Pu` as a substitute for material physics.

## 11. Material operator vs structural solution operator

Do not conflate:

```text
material operator:
(epsilon_{n+1}, z_n, material parameters)
→ (sigma_{n+1}, z_{n+1}, C_alg)
```

with:

```text
structural solution operator:
(geometry, material, BC, load fields, imperfections, history)
→ (fields, equilibrium path, stability, Pu)
```

Arbitrary boundary conditions and arbitrary loading cannot be obtained merely by replacing the material law. Long-term structure should use a physics/analytic core with global Ritz/spectral modes, and only later a separate approximate general solution-operator surrogate if needed.

## 12. Historical truth lock

For the recovered NZ-SCCM-U v0.2 shared dialogue:

```text
TURN 0001–0148 = continuous shared-text baseline
TURN 0147 = user: “那就执行吧”
TURN 0148 = task start/thinking + connection interruption
D20 formal assistant final text = NOT DELIVERED in the shared page
```

Later D20/D19R/D19C/v0.6.1/v0.6.3 artifacts may prove backend/branch work, but must not be used to fabricate a shared user-visible turn or user acceptance.

Use `history/RAW_HISTORY_REGISTRY.md` and the original chat-export locator before making claims about this history.

## 13. Retrieval entry points

Before substantial new work, read:

1. `START_HERE.md`
2. `SOURCE_OF_TRUTH_POLICY.md`
3. `evidence/MASTER_SOURCE_INVENTORY.csv`
4. `RECOVERY_PROTOCOL.md`
5. this file

For history reconstruction, also read `snapshots/2026-08-10_R2/` and `history/RAW_HISTORY_REGISTRY.md`.
