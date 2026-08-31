# NZ-SCCM — 曲率/容量坐标身份纠正与 BH050 重算 R02

**Date:** 2026-08-31  
**Branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Status:** `CORRECTION OF R01 INTERPRETATION / SOURCE-AUDITED RECALCULATION / MAIN UNCHANGED`

## 0. Why this R02 exists

The immediately preceding R01 backup incorrectly treated the historical terminal affine variables `(Bx,By)` as actual independent physical curvatures and therefore described `kappa_geo(q)` as a replacement for those variables.

A direct source audit of:

- `current/SSUHPC_CURRENT_STATE_ADDENDUM_20260827_2052_KINEMATIC_CURVATURE_RESET.md`
- `semantic_v2/40_execution/steel_shell/20260827_2052__NZSCCM__BH050_BH032_CLASSICAL_W_KAPPA_EPS_KINEMATIC_RECONSTRUCTION_R01.md`

shows that this interpretation had already been formally corrected on 2026-08-27.

The correct identity is:

```text
q = sole global structural postbuckling amplitude
kappa_geo(q) = actual structural curvature from w_d
Bx_cap, By_cap = terminal N-M capacity-surface affine coordinates
Bx_cap, By_cap != actual physical global curvature observables
```

Therefore imposing `By_cap = pi^2*q/b` is NOT a missing kinematic correction to the existing Airy-capacity-contact theory. It creates a new deformation-compatible theory variant and requires a new equilibrium derivation; it cannot be obtained by simple variable substitution.

This R02 supersedes the R01 interpretation on that point. R01 remains historical evidence of the dialogue correction sequence.

---

# 1. Actual structural curvature is already in the Airy front

Frozen added displacement:

\[
w_d=bq\sin(\alpha x)\sin(\beta y).
\]

Stress-free imperfection:

\[
w_i=bq_0\sin(\alpha x)\sin(\beta y).
\]

Incremental Kirchhoff-Love curvatures:

\[
\Delta\kappa_x=-w_{d,xx}=bq\alpha^2\sin\alpha x\sin\beta y,
\]

\[
\Delta\kappa_y=-w_{d,yy}=bq\beta^2\sin\alpha x\sin\beta y.
\]

At the BH control antinode, with `ell=b`,

\[
\boxed{\Delta\kappa_x=\Delta\kappa_y=\pi^2q/b}.
\]

The frozen Airy bending demand is

\[
M_y^d=J_yqs,
\qquad
J_y=b(D_\mu\alpha^2+D_y\beta^2),
\]

hence

\[
\boxed{M_y^d=D_\mu\Delta\kappa_x+D_y\Delta\kappa_y}.
\]

Thus the physical `w -> kappa` relation was already present in the structural demand and was not missing from the original Airy derivation.

---

# 2. BH050 original input re-audit

Frozen BH050 input from the blind R06 execution:

```text
b = 2500 mm
a_phys = 5000 mm
tc = 42 mm
ts = 4 mm
zf = 23 mm
9 longitudinal webs
net web height = 37 mm
Aw = 1332 mm2
rho_w = 0.0126857142857143
q0 = 0.0025
s = 1

steel: Es = 206000 MPa, nu_s = 0.30, fy = 355 MPa
UHPC: Ec = 43400 MPa, nu_c = 0.20, fc = 141.1 MPa, eps_c0 = 0.0035
UHPC tension: fct = 4.513133983249735 MPa, eps_t0 = 0.001, mt = 0.4418

local R02 cell:
Lx = 562.5 mm
Ly = 555.555555555556 mm
A0 = 0.3515625 mm
```

This corrects an intermediate chat misstatement that had temporarily used `b=1600 mm` for BH050. `b=1600 mm` belongs to BH032; BH050 uses `b=2500 mm`.

---

# 3. Initial stiffness and Airy recomputation

Frozen source-reproduced initial stiffness:

\[
A_{11}=3.685652010989011\times10^6\;N/mm,
\]
\[
A_{22}=3.795408810989011\times10^6\;N/mm,
\]
\[
A_{12}=9.182293032967034\times10^5\;N/mm,
\]
\[
A_{66}=1.383711353846154\times10^6\;N/mm,
\]

\[
D_x=1.236003299827839\times10^9\;Nmm,
\]
\[
D_y=1.252137549427839\times10^9\;Nmm,
\]
\[
D_\mu=3.432434438483517\times10^8\;Nmm,
\]
\[
D_{66}=4.463799279897436\times10^8\;Nmm,
\]
\[
H=1.236003299827839\times10^9\;Nmm.
\]

Integer mode scan:

```text
m=1  Pcr=30.5130828854 MN
m=2  Pcr=19.5818772367 MN  <- minimum
m=3  Pcr=23.0500697915 MN
m=4  Pcr=30.7519408767 MN
m=5  Pcr=41.4350738286 MN
m=6  Pcr=54.7904307691 MN
```

Thus

\[
\boxed{m_*=2},\qquad \boxed{\ell=2500\;mm},
\]

\[
\alpha=\beta=\pi/2500.
\]

Airy coefficients:

\[
P_{cr}=19.5818772367311\;MN,
\]
\[
K_x=4.272925966136171\times10^6\;N/mm,
\]
\[
G=4.400171479082513\times10^6\;N/mm,
\]
\[
C=10841.3718065234\;MN,
\]
\[
J_x=6.234616244717026\times10^6\;N,
\qquad
J_y=6.298311709061200\times10^6\;N.
\]

The physical curvature at the historical q value is

\[
\kappa_{geo}=\pi^2q/b.
\]

At

\[
q=0.004772819645833164,
\]

\[
\boxed{\kappa_{geo}=1.88423367128\times10^{-5}\;mm^{-1}}.
\]

---

# 4. Airy load and demand at the source-audited terminal capacity contact

\[
Q_q=q(q+2q_0)=4.664390560081682\times10^{-5}.
\]

\[
P_{cr}\frac q{q+q_0}=12.8506924314162\;MN,
\]

\[
CQ_q=0.505683923126832\;MN.
\]

Therefore

\[
\boxed{P_u=13.3563763545430\;MN}.
\]

Demand resultants at `s=1`:

\[
N_x^d=+199.305955403735\;N/mm,
\]

\[
N_y^d=-5137.30935871948\;N/mm,
\]

\[
M_x^d=29756.6988970160\;N,
\qquad
M_y^d=30060.7058605883\;N.
\]

The local antinode axial resultant is not equal to `-P/b` because the Airy redistribution term is active:

\[
P/b=5342.55054181721\;N/mm,
\qquad
GQ_q=205.241183097731\;N/mm,
\]

\[
N_y^d=-P/b+GQ_q.
\]

---

# 5. Terminal capacity-contact constituent ledger

The zero-thickness-quadrature UHPC primitives give

\[
N_y^U=-3775.20864050157\;N/mm,
\qquad
M_y^U=16306.0755102416\;N.
\]

Longitudinal web:

\[
N_y^w=-170.904638861559\;N/mm,
\qquad
M_y^w=293.915178045378\;N.
\]

Upper steel face:

\[
N_{y,+}^s=-302.97379680\;N/mm.
\]

Lower R06 steel face:

\[
N_{y,-}^s=-888.22228255\;N/mm.
\]

Thus

\[
N_y^{faces}=-1191.19607935637\;N/mm,
\]

and exact section closure is

\[
-3775.20864050157
-1191.19607935637
-170.904638861559
=-5137.30935871949\;N/mm.
\]

The terminal capacity-contact section shares are therefore

\[
\boxed{UHPC=73.4861\%},
\]

\[
\boxed{two\ steel\ faces=23.1872\%},
\]

\[
\boxed{web/PBL=3.3267\%}.
\]

Within the two steel faces:

\[
\boxed{upper=5.8975\%\ of\ section\ total},
\qquad
\boxed{lower=17.2896\%\ of\ section\ total}.
\]

These percentages describe the **terminal N-M capacity-contact section ledger at the control antinode**. They are NOT certified as the actual deformation-path load shares of the physical section, because `Bx_cap,By_cap` are capacity-surface coordinates rather than global kinematic curvatures.

Multiplying the local antinode resultants by `b` yields a local section-force decomposition:

\[
P_U^{local}=9.43802\;MN,
\]
\[
P_{faces}^{local}=2.97799\;MN,
\]
\[
P_w^{local}=0.427262\;MN,
\]

which sums to

\[
12.84327\;MN.
\]

The difference to global Airy load

\[
13.356376-12.843273\approx0.513103\;MN
\]

is exactly the antinode Airy redistribution correction

\[
bGQ_q\approx0.513103\;MN.
\]

Therefore the global `Pu` cannot be uniquely decomposed into constituent axial-force pieces simply by multiplying one antinode section resultant by width; the physically meaningful constituent comparison currently available is the local section share above.

---

# 6. Consequence for the proposed `Bcap = kappa_geo` substitution

The source audit shows:

\[
\boxed{\kappa_{geo}(q)=\pi^2q/b}
\]

was already present in the structural Airy bending demand.

The historical terminal variables satisfy

\[
\varepsilon_i^{cap}(z)=A_i^{cap}+B_i^{cap}z
\]

only as a parameterization of the terminal N-M capacity surface. They are not actual deformation-path curvatures.

Hence the proposed operation

\[
B_x^{cap}=\kappa_x^{geo}(q),\qquad B_y^{cap}=\kappa_y^{geo}(q)
\]

is not a correction of a wrong curvature formula. It is a new **deformation-compatible current-section theory**.

Such a theory cannot consistently retain all four old capacity-contact equations plus the old Airy `P(q)` unchanged. Once the current section is forced to use the actual q-curvature, a new generalized out-of-plane equilibrium/current-moment work relation is required; otherwise the system is either overdetermined or double-counts the old Airy Galerkin bending equilibrium.

Accordingly, no new `Pu` is invented from simple substitution in this R02 backup.

---

# 7. Next correct derivation if actual deformation-path shares are required

The required new route is:

```text
q -> w_d(q) -> kappa_geo(q)
                 |
                 v
     current UHPC + R02/R06 + web section response
                 |
                 v
        N(q), M(q), current tangent
                 |
                 v
      generalized q virtual-work equilibrium
                 |
                 v
              P(q)
                 |
                 v
        admissible branch / peak Pu
```

This is distinct from the existing terminal demand-capacity-contact method. It is the proper route if the research objective is not only `Pu` but also actual constituent load-sharing and deformation compatibility.

No FEM/test value is used to define this new route.

---

# 8. Governance

```text
R01_DUPLICATED_CURVATURE_INTERPRETATION = SUPERSEDED_BY_THIS_R02
PHYSICAL_KAPPA_GEO_FROM_q = RETAIN
AIRY_My_ALREADY_Dkappa = CONFIRMED
Bcap_AS_PHYSICAL_CURVATURE = PROHIBITED
OLD_17.984_MN_HYBRID = INVALID
BH050_SOURCE_AUDITED_CAPACITY_CONTACT_Pu = 13.3563763545430 MN
CAPACITY_CONTACT_SECTION_SHARE_UHPC = 73.4861%
CAPACITY_CONTACT_SECTION_SHARE_STEEL_FACES = 23.1872%
CAPACITY_CONTACT_SECTION_SHARE_WEB = 3.3267%
NEW_DEFORMATION_COMPATIBLE_Pu = NOT_YET_DERIVED
PRODUCTION_MAIN_CHANGED = NO
```
