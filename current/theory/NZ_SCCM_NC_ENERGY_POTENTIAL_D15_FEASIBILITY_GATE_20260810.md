# NC ENERGY POTENTIAL + D15 FEASIBILITY GATE

Date: 2026-08-10

## Scope

This execution implements ONLY the approved gate:

1. material energy contract;
2. one unified low-parameter potential concept;
3. zero-spatial-quadrature / D15 closure test.

NO Case21 ultimate-capacity solution is executed.
NO Swartz24 calculation is executed.
NO structural experimental capacity is used to select a material parameter.

## Source boundary

Nguyen Chapter 3 uses the equivalent-uniaxial-strain concept for undamaged biaxial concrete and explicitly distinguishes TT, TC, CC and crushed states. In TC, the compression capacity is reduced by the coexisting tensile strain. Therefore the original source is NOT silently relabelled as an exact scalar potential. The present energy potential is a controlled current-work replacement candidate for the project.

## Material energy contract

fc = 21.23 MPa
E0 = 20321.0 MPa
eps0 = 0.00209
nu = 0.18
kappa = 2.00051295336788

Material spectral interval used by the gate:
lambda in [-10.0, 0.499871794539742]

Compression reference:
- -10 <= lambda < -1: retained R06/R08 C2 postpeak;
- -1 <= lambda < 0: retained Saenz branch.

Tension:
R08 tensile work is used as the neutral material-energy reference:

Et_R08 = 0.0297423717751347

The simple monotone saturation potential

phi_t(lambda)
= u_inf*lambda
- u_inf^2/kappa * ln(1+kappa*lambda/u_inf)

is required to preserve that material tensile work at lambda=0.499871794539742.

This gives

u_inf = 0.0742211076392931

This number is obtained only from MATERIAL WORK. It is not fitted to Case21.

## Candidate 1 — minimum anchor-exact global polynomial

Stress grammar:

u_A(lambda)
= kappa lambda + sum_(n=2)^7 a_n lambda^n

The six algebraic constants are uniquely determined by:
- compression peak stress and zero tangent at lambda=-1;
- compression residual and zero tangent at lambda=-10;
- tension endpoint stress from the energy-equivalent saturation target;
- total tensile work Et_R08.

They are derived constants, NOT free material fitting parameters.

a2..a7 =
[-6.17386072034511 -5.24326704803289 13.07305520434379 13.28327445555494
  2.24669642792592  0.10537055102603]

Result:

minimum stress inside material domain
= -12965.289024 fc

at lambda
= -7.236296

Therefore:

ANCHOR_EXACT_LOW_PARAMETER_GLOBAL_POLYNOMIAL = FAIL

The polynomial satisfies the anchors but oscillates catastrophically between them.

## Candidate 2 — energy-first single global potential

A single Chebyshev potential is used only as a diagnostic D15-compatible grammar:

phi_N(lambda) = sum a_n T_n(xi(lambda))

The fit objective uses MATERIAL potential values only.
The following quantities are imposed exactly:
- phi(0)=0;
- u(0)=0;
- u'(0)=kappa;
- u(-1)=-1;
- u'(-1)=0;
- u(-10)=-0.10;
- u'(-10)=0;
- retained tensile work phi(lambda_hi)=Et_R08.

Only N=8,10,12 are executed. Degree escalation stops at N=12.

Metrics:

 potential_max_abs  potential_p95_abs  stress_max_abs_fc  stress_p95_abs_fc  tangent_max_abs_normalized  tangent_p95_abs_normalized  max_spurious_tension_in_compression_fc  max_spurious_compression_in_tension_fc  compression_overshoot_beyond_fc  potential_degree_N  max_invariant_monomials_before_D15
        135.055197         126.124869         105.476529          93.058239                   86.766694                   71.986324                              105.185120                                0.682103                        53.236538                   8                                  25
          4.144058           3.491604           5.723855           4.761838                    9.910178                    8.354566                                5.533162                                0.748071                         4.331491                  10                                  36
          0.231823           0.166272           0.879333           0.405728                    9.918593                    5.441321                                0.328363                                0.810240                         0.083387                  12                                  49

At N=12 the potential itself is much closer to the reference, but differentiating that same potential still produces unacceptable stress/tangent errors and sign violations.

Therefore:

ENERGY_FIRST_LOW_ORDER_GLOBAL_POTENTIAL_N_LE_12 = FAIL

## D15 closure

For any finite polynomial potential p_N(Eu),

Psi_N = fc eps0 tr[p_N(Eu)].

For a 2x2 equivalent-uniaxial strain tensor Eu, Cayley-Hamilton gives

Eu^2 - J1 Eu + J2 I = 0.

Define s_n = tr(Eu^n). Then

s_0=2,
s_1=J1,
s_n = J1 s_(n-1) - J2 s_(n-2).

Therefore every tr(Eu^n) is a finite polynomial in J1,J2.

After inserting the already-derived Case21 kinematics,

J1 = I1(D,q,x,y,z),
J2 = I2(D,q,x,y,z),

each invariant monomial is a finite trigonometric-thickness polynomial and is exactly evaluable by D15 moments.

Hence:

D15_POLYNOMIAL_EXACT_CLOSURE = PASS
FORMAL_SPATIAL_GAUSS = 0
FORMAL_SPATIAL_SIMPSON = 0
FORMAL_SPATIAL_ADAPTIVE_QUADRATURE = 0
FORMAL_MATERIAL_POINT_GRID = 0

Complexity:

                candidate  potential_polynomial_degree  invariant_monomial_upper_count  formal_spatial_quadrature  D15_exact_closure
       anchor_stress_deg7                            8                              25                          0               True
 energy_potential_cheb_N8                            8                              25                          0               True
energy_potential_cheb_N10                           10                              36                          0               True
energy_potential_cheb_N12                           12                              49                          0               True

## Gate decision

The mathematical D15 closure works.

The current low-parameter global-polynomial material potential does NOT.

This is an important distinction:

D15 feasibility = PASS
material-potential adequacy = FAIL

Overall:

NC_ENERGY_POTENTIAL_AND_D15_FEASIBILITY_GATE = FAIL__STOP_AT_GATE

No attempt is made to raise the global degree beyond N=12.
No Case21 structural calculation follows.

A future route, if explicitly approved by the user, must use a DIFFERENT low-parameter potential grammar and must prove zero-spatial-quadrature closure before any structural calculation.
