# UCFT M8 execution log — 2026-09-30 23:29 +08:00

task:
1. add only the requested human-reproducibility lock section to the instruction;
2. execute the first real BH005 fixed-q C1 base point without default M3 enrichment;
3. audit the next perfect-local mode-identification step before using its tangent criterion.

files read:
- 指示词(20260930-155305).md
- latest M8 current state 20260930_2235
- UCFT_M8_input_closure_and_solver_interface_audit.md
- UCFT_M6_inner_outer_residual_Schur_condensation.md
- UCFT_M5_steel_deformation_theory_active_set.md
- UCFT_M4_UHPC_active_set_analytic_partition.md
- UCFT_M7_theory_selfcheck.py
- UCFT_M8_production_input_freeze.md
- UCFT_M3_mixed_harmonic_解析谱计算器.py
- previous execution log / backup manifest / state from backups/20260930_223500/output

instruction change:
Inserted one section only:
29.1 人工可复现的严格定义（新增锁定）

The section locks:
- no program-only black-box step;
- hand-reproducible strain -> active roots -> intervals -> analytic integration -> residual/Jacobian -> linear solve -> Newton update;
- repeated explicit iterations can in principle reconstruct q->P(q);
- default formal C1 unknowns only:
  Ex,Ey,Bx,By,Hx,Hy,P,A+,A-;
- no default instantiation of M3 candidate harmonics;
- synthetic high-frequency integration tests are not formal shape functions/unknowns.

fixed-q calculation:
case BH005
q=1.0e-5
A0+=A0-=0
constrained perfect-local global base state A+=A-=0

all final-INP UHPC and M5 steel states are analytically proven elastic at this point.
No 2D/3D spatial Gauss quadrature defines the residual.

Newton iteration 0 residual:
[0,0,-1.105037361e3,-4.420149442e3,0,0,9.550714400e5]^T

One affine elastic Newton solve gives:
Ex=4.26540289e-4
Ey=-1.421800965e-3
Bx=4.63562982e-9
By=1.85425193e-8
Hx=Hy=0
P=1233.696696957 kN

post-update max residual:
1.16e-10.

force shares:
Pc=647.914699554 kN
Ps+=Ps-=292.890998701 kN
P=Pc+Ps++Ps-=1233.696696957 kN

BH005 chi_w=1.475275839368
P_report=1541.634899626 kN.

derived Delta:
0.710908208334 mm.

active-set proof:
UHPC |e_x| <= 9.855492765e-6 < first tensile nonlinear total strain 1.283711751e-4.
UHPC e_y in [-1.426827139e-3,-1.416774790e-3], below first compression inelastic magnitude 2.753225806e-3.
Steel ebar_i <= 1.436171823e-3 < yield strain 1.723300971e-3.

mode-identification audit:
Exact analytic X,Y integration of the locked M6 RA residual at the same equilibrium point gives:

N=m=1:
RA+=-2561.158110982 N
RA-=+2644.857566627 N

N=m=2:
RA+=-1666.066308563 N
RA-=+1666.066308563 N

Therefore A=0 is not generally an unconstrained local equilibrium at q>0.
The old auxiliary rule that evaluated K_l,cond on A=0 and interpreted lambda_min=0 as a strict bifurcation must be corrected.

classification:
NEEDS CORRECTION, NOT ROUTE-FATAL.
It directly affects local mode identity/branch definition, so it is allowed to block the old tangent scan under the instruction's execution discipline.

minimal correction:
For each candidate (N,m), keep A0+=A0-=0 but solve the original M6 equilibrium RA+=RA-=0 from q=0 onward, obtaining candidate-wise forced local response A+(q),A-(q).
Evaluate K_l,cond only on those actual equilibrium points.
No structure equation, material law, shape function, or empirical coefficient is changed.

gate/status:
M0-M7 = PASS
M8_HUMAN_REPRO_FIXED_Q_BASE = PASS
M8_PERFECT_LOCAL_MODE_ID = NEEDS_IMPLEMENTATION_CORRECTION
M8_PATH_SOLVER = PARTIAL
M9 = NOT STARTED

NEXT_ACTION:
Build the BH005 candidate-wise perfect-geometry forced-response evaluator for the initial (N,m)=1..12 window.
For every q-state save the complete human-reproducible Newton ledger and evaluate K_l,cond only after RA+=RA-=0.
Do not instantiate M3 candidate harmonics unless real-path omitted residual is significant.
