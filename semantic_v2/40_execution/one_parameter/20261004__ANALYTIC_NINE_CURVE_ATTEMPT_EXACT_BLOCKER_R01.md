# 2026-10-04 analytic one-parameter nine-curve execution attempt — exact blocker R01

## Scope

Target theory is the two current chat handoff texts of 2026-10-04:

1. UHPC: elastic Airy trial field -> peak-rebased DAMAGE/plastic -> energy-weighted rho_A, rho_D, w_P -> P_U(w).
2. Steel: global base state first; then one continuous whole-face high-order mode per face; combined global+local Mises; no cell discretization.
3. Total: P(w)=P_U(w)+P_s^+(w)+P_s^-(w), Pu=max_w P(w).
4. Current nine-specimen geometry uses a_h=2b, t_c=42 mm, t_s=4 mm, q0=0.0025, N_+=N_-=m_+=m_-=4, A0=0.225b/1600.

This execution deliberately does NOT fall back to 41DOF/57DOF, 99-cell steel, 2D Gaussian integration, or differential_evolution.

## Nine specimens

| Case | b mm | a_h mm | t_c mm | t_s mm | A0 mm |
|---|---:|---:|---:|---:|---:|
| BH005 | 250 | 500 | 42 | 4 | 0.03515625 |
| BH010 | 500 | 1000 | 42 | 4 | 0.07031250 |
| BH020 | 1000 | 2000 | 42 | 4 | 0.14062500 |
| BH032 | 1600 | 3200 | 42 | 4 | 0.22500000 |
| BH050 | 2500 | 5000 | 42 | 4 | 0.35156250 |
| BH060 | 3000 | 6000 | 42 | 4 | 0.42187500 |
| BH070 | 3500 | 7000 | 42 | 4 | 0.49218750 |
| BH085 | 4250 | 8500 | 42 | 4 | 0.59765625 |
| BH100 | 5000 | 10000 | 42 | 4 | 0.70312500 |

Materials: E_c=43400 MPa, nu_c=0.30, f_c=141.1 MPa, f_t=7.3 MPa; E_s=206000 MPa, nu_s=0.30, f_y=355 MPa.

## UHPC analytic identity retained

Q_E=w^2+2 w0 w, w0=b q0.

N_y^E =
D0 ((alpha^2+beta^2)^2/beta^2) w/(w0+w)
+ E_c t_c/16 ((alpha^4+beta^4)/beta^2) Q_E.

The current symbolic reduction remains:
- threshold boundaries: finite quartic roots after u=sin(alpha x), v=sin(beta y);
- rho_A, rho_D, w_P: finite algebraic/hyperelliptic one-dimensional definite-integral layer after exact level-set partition;
- no 2D production grid.

## Steel constants for current N=m=4, a_h=2b

beta_* = N a_h/b = 8.

k_cr = 4 beta_*^2/m^2 + 8/3 + 4 m^2/beta_*^2 = 59/3 = 19.6666666666667.

k_p(8,4)=77.9807266435986.

C_GL =
64 N^2 m^2 / [a_h^2(4N^2-1)(4m^2-1)] > 0.

C_LL = 3 pi^2 m^2/(2 a_h^2) > 0.

## Exact contradiction found before any curve sweep

The latest chat reply replaced the old total compatibility by the local-only elastic residual

R_A,E^±(A;w)
= Delta sigma_l,E(A)/E_s
- s_± C_GL [w0 A + w A0 + w A] = 0,

with s_+=+1, s_-=-1, A0>0, A>=0, w>0.

The same reply defines the Yun local elastic mean increment as

Delta sigma_l,E(A)
= K_s [
k_cr A/(A0+A)
+ k_p(1-nu_s^2)(2A0 A + A^2)/t_s^2
],

where K_s>0. Therefore for every physical A>0,

Delta sigma_l,E(A) > 0.

For BOTTOM (s_-=-1),

R_A,E^-(A;w)
=
Delta sigma_l,E(A)/E_s
+ C_GL [w0 A + w A0 + w A].

Every term is nonnegative and, for any w>0, the second term contains C_GL w A0>0. Hence

R_A,E^-(A;w) > 0
for all A>=0 and every w>0.

At A=0:

R_A,E^-(0;w)=C_GL w A0>0.

Therefore the latest two chat replies, taken literally, have NO BOTTOM physical root for any nonzero global deflection. This is not a numerical convergence issue. It is an exact parity/sign closure contradiction.

BH050 numerical example at w=56.05 mm:
- b=2500 mm, a_h=5000 mm, A0=0.3515625 mm
- C_GL=1.65119677500630e-7 mm^-2
- R_A,E^-(0;w)=C_GL*w*A0=3.25369614512472e-6 > 0

Thus the requested total curve cannot be truthfully produced from these two replies without first repairing the steel compatibility/operator identity.

## Consequence

Do NOT fabricate nine P(w) curves from the current pair of replies.
Do NOT fix this with a numerical solver: no root exists.
Do NOT reintroduce e_U or a signed local operator silently.

The UHPC branch can still be evaluated independently, but P_s^- is undefined in the literal latest formulation for every w>0, so P_total(w) is undefined.

## Minimal repair candidates to audit next

Candidate A — retain total axial compatibility from the former locked whole-face model, but update only the Mises check to use sigma_global + Delta sigma_local. This is executable but needs a double-counting audit.

Candidate B — derive a genuinely signed incremental Yun operator from total global+local virtual work, so Delta sigma_l can have the TOP/BOTTOM parity required by the GL term. This is mechanically cleaner, but must be derived rather than imposed.

No candidate is accepted in this file. The purpose of this commit is to preserve the exact point where the attempted nine-curve computation stops.

## Reproducibility contract for later detailed curve-point output

Once the steel closure is repaired, each saved curve point must include at least:
case, w, w0, Q_E, N_y^E, rho_A, rho_D, w_P, P_U,
TOP/BOTTOM A, e, A_P, global steel base stress state, local stress increment,
max Mises and controlling algebraic candidate,
P_s^+, P_s^-, P_total,
plus all branch/status flags and numerical tolerances for the allowed 1D UHPC definite integrals.

This is the minimum state needed to reconstruct an arbitrary future point by hand.
