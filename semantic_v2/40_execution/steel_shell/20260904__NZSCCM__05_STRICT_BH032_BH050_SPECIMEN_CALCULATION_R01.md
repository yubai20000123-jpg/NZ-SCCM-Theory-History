# NZ-SCCM Multiwave Steel Shell 05 — strict BH032/BH050 specimen calculation R01

> Date: 2026-09-04  
> Branch: `diagnostic/bh032-bh050-mode-projection-20260827`  
> Theory source: **ONLY** `20260904__NZSCCM__MULTIWAVE_STEEL_SHELL_05_PLATE_SPECIFIC_TWO_INTERFACE_GALERKIN_AVERAGED_SLIP_FULL_DERIVATION_R01.md`  
> Status: `EXECUTED THROUGH 05-INTRINSIC INPUT-CLOSURE GATE / NO Pu CLAIM`  
> Production R14: unchanged.

## 0. Strict calculation rule

This run deliberately does **not** import old 02/03/04 operators, old R14 numerical branch states, old Pu, FE response, stored roots, fitted gamma, effective area/width, or any outside interface parameter.

The purpose is to test whether version 05, **by itself**, is numerically closed for the current BH specimens.

Current 05 contains explicit numerical global-mode results for BH032 and BH050, and an explicit BH top-edge local-buckling check. Those are treated as 05-internal numerical data. Any quantity not numerically defined inside 05 remains undefined; it is not silently recovered from an older file.

---

# Part I — global plate eigenmode calculation already instantiated inside 05

05 uses

\[
N_{y,cr}^{(m)}=
\frac{D_x\alpha^4+2H\alpha^2\beta_m^2+D_y\beta_m^4}{\beta_m^2},
\qquad
P_{cr}^{(m)}=bN_{y,cr}^{(m)},
\]

\[
\alpha=\frac{\pi}{b},
\qquad
\beta_m=\frac{m\pi}{a},
\qquad
m^*=\arg\min_m P_{cr}^{(m)}.
\]

## 1. BH032

05-internal candidate results:

| m | Pcr (MN) |
|---:|---:|
| 1 | 47.61390 |
| 2 | 30.60352 |
| 3 | 36.08402 |
| 4 | 48.19705 |

and

\[
m_c=1.98991.
\]

Therefore

\[
\boxed{m^*_{BH032}=2},
\qquad
\boxed{P_{cr,BH032}=30.60352\ \text{MN}}.
\]

## 2. BH050

05-internal candidate results:

| m | Pcr (MN) |
|---:|---:|
| 1 | 30.51308 |
| 2 | 19.58188 |
| 3 | 23.05007 |
| 4 | 30.75194 |

and

\[
m_c=1.99353.
\]

Therefore

\[
\boxed{m^*_{BH050}=2},
\qquad
\boxed{P_{cr,BH050}=19.58188\ \text{MN}}.
\]

No old production Pcr value is used to select these modes; these are the values explicitly instantiated in 05.

---

# Part II — representative global half-wave and local candidates

05 states for the BH geometry that \(a/b=2\). With \(m^*=2\),

\[
L_G=\frac{a}{m^*}=b.
\]

The standard transverse rib spacing is

\[
s=0.225b.
\]

Hence

\[
n_0=\left\lfloor\frac{L_G}{s}\right\rfloor
=\left\lfloor\frac{1}{0.225}\right\rfloor=4,
\]

and the standard-bay longitudinal candidates are

\[
\boxed{n=3,4,5}.
\]

For each candidate

\[
L_x=0.225b,
\qquad
L_y=\frac{b}{n}.
\]

The TOP edge bays are

\[
L_{x,e}^+=0.1625b,
\qquad
n_e^+=6,
\qquad
L_{y,e}^+=\frac{b}{6}.
\]

The BOTTOM edge bays are

\[
L_{x,e}^-=0.05b,
\qquad
n_e^-=20,
\qquad
L_{y,e}^-=\frac{b}{20}.
\]

Transverse topology over one representative global half-wave:

- TOP: 3 standard bays + 2 edge bays = 5 transverse bays;
- BOTTOM: 4 standard bays + 2 edge bays = 6 transverse bays.

Thus 05 has 11 physical transverse bays in the representative global half-wave, but it does **not** introduce 11 independent random local amplitudes, and it certainly does not return to the old 99-cell external-unknown architecture. Geometrically identical bays share the same analytic local operator class.

---

# Part III — local elastic gate, evaluated strictly from 05 quantities

05 gives

\[
r=\frac{L_y}{L_x},
\]

\[
k_{cr}=\frac{4(3r^4+2r^2+3)}{3r^2},
\]

\[
\sigma_{cr}^{E}=
\frac{\pi^2E_st_s^2}{12(1-\nu_s^2)L_x^2}k_{cr}.
\]

Define the common specimen factor

\[
C_s=\frac{\pi^2E_st_s^2}{12(1-\nu_s^2)b^2}.
\]

Then every local class can be written as

\[
\sigma_{cr}^{E}=C_s\,F,
\qquad
F=\frac{k_{cr}}{(L_x/b)^2}.
\]

This permits all other local gates to be computed from the TOP-edge value that is already explicitly reported inside 05, without importing \(E_s,t_s,\nu_s,b\) from an older file.

## 3.1 Dimensionless local factors

### Standard n=3

\[
\frac{L_x}{b}=0.225,
\qquad
\frac{L_y}{b}=\frac13,
\qquad
r=1.48148148,
\]

\[
k_{cr}=13.26831619,
\qquad
F_{3}=262.0901963.
\]

### Standard n=4

\[
r=1.11111111,
\qquad
k_{cr}=10.84493827,
\qquad
F_4=214.2210029.
\]

### Standard n=5

\[
r=0.88888889,
\qquad
k_{cr}=10.88966049,
\qquad
F_5=215.1044048.
\]

### TOP edge

\[
\frac{L_x}{b}=0.1625,
\qquad
\frac{L_y}{b}=\frac16,
\qquad
r=1.02564103,
\]

\[
k_{cr}=10.67692472,
\qquad
F_{e+}=404.3332439.
\]

### BOTTOM edge

\[
\frac{L_x}{b}=0.05,
\qquad
\frac{L_y}{b}=\frac1{20},
\qquad
r=1,
\]

\[
k_{cr}=10.66666667,
\qquad
F_{e-}=4266.6666667.
\]

Therefore the ratios relative to the 05-internal TOP-edge result are

\[
\frac{F_3}{F_{e+}}=0.648203432,
\]

\[
\frac{F_4}{F_{e+}}=0.529812985,
\]

\[
\frac{F_5}{F_{e+}}=0.531997821,
\]

\[
\frac{F_{e-}}{F_{e+}}=10.55235188.
\]

## 3.2 BH032 local gates

05 explicitly reports

\[
\sigma_{cr,e+}^{E}\approx470.5\ \text{MPa}
\]

and compares it with \(f_y=355\) MPa.

Thus, using the exact 05 dimensionless ratios:

| class | sigma_cr^E (MPa) | 05 gate |
|---|---:|---|
| standard n=3 | 304.98 | LOCAL-FIRST |
| standard n=4 | 249.28 | LOCAL-FIRST |
| standard n=5 | 250.30 | LOCAL-FIRST |
| TOP edge n=6 | 470.50 | YIELD-FIRST |
| BOTTOM edge n=20 | 4964.88 | YIELD-FIRST |

Therefore in BH032:

- all 7 standard transverse bays (3 TOP + 4 BOTTOM) are LOCAL-FIRST for each of the three standard candidate wave-count checks;
- both TOP edge bays and both BOTTOM edge bays are YIELD-FIRST;
- among the three standard elastic local candidates, n=4 has the lowest \(\sigma_{cr}^{E}\), but 05 does **not** authorize replacing the subsequent nonlinear R02 energy/root calculation by this linear minimum alone.

## 3.3 BH050 local gates

05 explicitly reports

\[
\sigma_{cr,e+}^{E}\approx192.7\ \text{MPa}<355\ \text{MPa}.
\]

Thus:

| class | sigma_cr^E (MPa) | 05 gate |
|---|---:|---|
| standard n=3 | 124.91 | LOCAL-FIRST |
| standard n=4 | 102.09 | LOCAL-FIRST |
| standard n=5 | 102.52 | LOCAL-FIRST |
| TOP edge n=6 | 192.70 | LOCAL-FIRST |
| BOTTOM edge n=20 | 2033.44 | YIELD-FIRST |

Therefore in BH050:

- all 7 standard transverse bays are LOCAL-FIRST;
- both TOP edge bays are also LOCAL-FIRST;
- only the two BOTTOM edge bays are YIELD-FIRST;
- again n=4 is the lowest *elastic* standard-bay candidate, but final nonlinear mode selection still belongs to the 05 R02/root/energy branch.

---

# Part IV — unloaded local state is closed exactly

For every LOCAL-FIRST class, 05 defines

\[
A_{0\ell}=\frac{L_x}{1600},
\qquad
B_3U^3+B_1U+B_0=0.
\]

At the unloaded state

\[
e_x^c=e_y^c=0,
\]

so \(L_0=0\),

\[
B_1=K_b-B_3A_{0\ell}^2,
\qquad
B_0=-K_bA_{0\ell}.
\]

Substitute \(U=A_{0\ell}\):

\[
B_3A_0^3+(K_b-B_3A_0^2)A_0-K_bA_0=0.
\]

Therefore the connected unloaded local branch has the exact root

\[
\boxed{U(q=0)=A_{0\ell}}.
\]

No numerical root search and no stored Pu are needed to establish the initial state.

---

# Part V — strict 05-only calculation reaches a hard input-closure gate

The next 05 stage is the two-interface partial-interaction condensation.

For the current unperforated-rib construction,

\[
k_{\ell,r}=2h_rK_t,
\]

\[
k_+=N_r^+k_{\ell,r},
\qquad
k_-=N_r^-k_{\ell,r}.
\]

Then

\[
B_{11}=k_+\left(\frac1{\mathcal K_+}+\frac1{\mathcal K_c}\right),
\qquad
B_{12}=\frac{k_-}{\mathcal K_c},
\]

\[
B_{21}=\frac{k_+}{\mathcal K_c},
\qquad
B_{22}=k_-\left(\frac1{\mathcal K_-}+\frac1{\mathcal K_c}\right),
\]

followed by

\[
c_+=1-\beta^2\frac{A_{22}^{PI}+A_{12}^{PI}}{\Delta_\beta},
\]

\[
c_-=1-\beta^2\frac{A_{11}^{PI}+A_{21}^{PI}}{\Delta_\beta}.
\]

The 05 theory itself explicitly states that the current specimen's real unperforated-rib/UHPC interface stiffness \(K_t\) is **not source-locked**. The values 696 and 13 N/mm^3 appearing in 05 are only reference values from different interface treatments and are explicitly declared **not** to be the current specimen parameter.

Therefore, under the user's present instruction “based on and only on 05”, neither value may be inserted as the specimen's \(K_t\).

Consequently the following quantities are not numerically determined:

\[
c_+,\quad c_-,\quad z_c^{PI},\quad z_+^{PI},\quad z_-^{PI}.
\]

The dependency chain that becomes blocked is

\[
\boxed{
K_t
\to
k_\pm
\to
c_\pm,z_c^{PI},z_\pm^{PI}
\to
\varepsilon_{y,s}^{\pm},\varepsilon_y^U
\to
U^*
\to
\sigma_s,N_s,M_s,N_U,M_U,N_w,M_w
\to
R_4(q)
\to
P_u.
}
\]

This is an **input-identification block**, not a Newton/convergence block.

---

# Part VI — two additional self-containment defects of 05 exposed by the strict calculation

The strict specimen run reveals that 05 is not yet a numerically self-contained calculation contract even if \(K_t\) were somehow supplied.

## 6.1 Global initial imperfection q0 is not numerically defined in 05

05 writes

\[
Q=q(q+2q_0),
\]

\[
P(q)=P_{cr}\frac{q}{q+q_0}+C_AQ,
\]

but the 05 file does not provide a numerical \(q_0\) for BH032/BH050. Therefore a strict 05-only continuation cannot numerically instantiate the outer load curve.

## 6.2 UHPC tensile polynomial is referenced but its coefficients are not written into 05

05 states that tension “continues to use the existing frozen four-piece explicit cubic polynomial”,

\[
\sigma=a_j+b_js+c_js^2+d_js^3,
\qquad
s=\varepsilon-\varepsilon_j,
\]

but 05 does not reproduce the numerical values of \(\varepsilon_j,a_j,b_j,c_j,d_j\).

Therefore the requested rule “only version 05” forbids silently recovering those values from an older theory file.

This means the UHPC section integrations \(N^U,M^U\) cannot be completed numerically over arbitrary current tensile/compressive strain states from 05 alone.

---

# Part VII — exact stopping point and result identity

## Successfully executed with 05 only

1. BH032 global candidate modes m=1..4: 4 candidates.
2. BH050 global candidate modes m=1..4: 4 candidates.
3. Both specimens select m*=2 by the 05 eigenvalue comparison.
4. Representative global half-wave: \(L_G=b\).
5. Standard local candidates: n=3,4,5.
6. Edge local counts: TOP n=6, BOTTOM n=20.
7. Local elastic gate classes were evaluated for BH032 and BH050.
8. The exact unloaded connected local root \(U=A_{0\ell}\) was verified algebraically.

## Not executed / not claimed

The calculation **does not** claim:

- a numerical \(c_+\) or \(c_-\) for the specimen;
- a current local amplitude \(U(q>0)\);
- steel-shell N/M along the load path;
- UHPC/web N/M along the load path;
- a numerical four-equation R4 branch;
- J4 fold location;
- terminal q;
- Pu.

Doing any of these numerically while preserving the strict “05 only” rule would require inventing or importing data that 05 itself does not contain.

## Strict result

\[
\boxed{\text{05-ONLY FULL SPECIMEN Pu CALCULATION = NOT NUMERICALLY CLOSED}}
\]

with the **first causal block**

\[
\boxed{K_t\ \text{for the actual unperforated-rib/UHPC interface is undefined in 05}}.
\]

Even after resolving that first block, the 05 file must also become self-contained in \(q_0\) and the UHPC tensile polynomial coefficients before a truly strict 05-only Pu run is possible.

No alternative theory, empirical correction, FE fit, or old result was used to bypass these missing definitions.
