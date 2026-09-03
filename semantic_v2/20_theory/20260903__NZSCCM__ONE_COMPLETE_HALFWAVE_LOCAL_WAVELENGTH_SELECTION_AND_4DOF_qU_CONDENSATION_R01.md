# NZ-SCCM — one complete global halfwave local-wavelength selection and fixed-4DOF qU condensation R01

Date: 2026-09-03
Branch: `diagnostic/bh032-bh050-mode-projection-20260827`
Status: **DIAGNOSTIC THEORY CANDIDATE / NOT PRODUCTION R14**

This file records a deliberate reduction of the preceding BH050 99-cell registration diagnostic. It does **not** modify production R14, does **not** introduce effective width/area, does **not** use FE to fit a theoretical root, and does **not** make `8` or `9` a universal local-wave count.

The governing correction is:

> The formal structural domain is one complete global buckling halfwave. Repeated global halfwaves of the physical member are not separate formal computational domains. The local wavelength is selected from local stability/current qU mechanics; the number of visibly active local cells/lobes is an output of the solved amplitude field, not a prescribed constant.

---

## 1. Source-locked objects retained

The qU kinematics and energy are retained from

`semantic_v2/20_theory/20260827_1240__NZSCCM__EXPLICIT_AIRY_Q_U_COMMON_CURVATURE_REPAIR_WITH_UNCHANGED_NM_R02.md`.

For a local C1 bay/patch,

\[
\phi=(1-\cos k_x\xi)(1-\cos k_y\eta),
\qquad
k_x=2\pi/L_x,
\qquad
k_y=2\pi/L_y.
\]

It retains C1 compatibility at the local boundary:

\[
\phi=0,\qquad \phi_{,n}=0,
\]

without imposing curvature lock.

The local current/initial amplitudes are `U,A0`; the global current/initial amplitudes are

\[
W=B(q_0+q),\qquad W_0=Bq_0.
\]

The exact qU invariants are

\[
d=U^2-A_0^2,
\]

\[
\Delta=WU-W_0A_0
=B[(q_0+q)U-q_0A_0].
\]

The augmented mean coordinates remain

\[
m_x=e_x-c_xd-h_x\Delta,
\]

\[
m_y=e_y-c_yd-h_y\Delta,
\]

\[
m_\gamma=\gamma-h_\gamma\Delta.
\]

The retained local augmented energy is

\[
\begin{aligned}
\Pi_b^{qU}={}&
\frac12K_b(U-A_0)^2\\
&+\frac12t_sQ_s(m_x^2+m_y^2+2\nu_sm_xm_y)\\
&+\frac12t_sG_sm_\gamma^2\\
&+t_sE_s\left[K_A d^2+2K_{d\Delta}d\Delta+K_{\Delta\Delta}\Delta^2\right].
\end{aligned}
\]

The exact source derivation already proves

\[
R_U=\frac{\partial\Pi_b^{qU}}{\partial U}
=B_3U^3+B_2U^2+B_1U+B_0=0.
\]

Therefore the local qU object is already finite algebraic; the present reduction only changes how the collection of local amplitudes is parameterized.

---

## 2. Formal domain = one complete global halfwave

For a global longitudinal mode

\[
\psi\propto\sin\left(\frac{m_G^*\pi y}{L}\right),
\]

the length of one complete global halfwave is

\[
\boxed{\ell_G=\frac{L}{m_G^*}}.
\]

The current BH family contract has

\[
L=2B,\qquad m_G^*=2,
\]

hence

\[
\boxed{\ell_G=B}.
\]

This is the formal computational length. A physical member with two repeated global halfwaves is **not** represented by solving two independent copies of the same local system.

If a total integrated energy over the whole member is ever needed on a perfectly repeated branch, it is a multiplicity of the representative-halfwave energy. Such a common multiplicative factor does not change the stationary equations. Section resultants and the current steel-shell operator are evaluated from the representative halfwave directly.

This reduction does not assert that a real imperfect member must display identical amplitudes in every physical halfwave. Whole-member localization remains a morphology/validation question; it is not a reason to duplicate formal degrees of freedom.

---

## 3. Hard-coded `Ly=L/9`, `n=8`, `n=9` are retired as universal theory inputs

The preceding BH050 registration diagnostic used

\[
L_y=5000/9=555.5556\ \mathrm{mm}
\]

and 9 axial registration cells. Combined with five top transverse bays and six bottom transverse bays, this produced

\[
5\times9+6\times9=99
\]

independent local amplitudes.

That execution remains valid only as a **registration diagnostic**. It is not a universal shell architecture.

The correct hierarchy is now

\[
\boxed{
\text{global stability}\to\ell_G,
\qquad
\text{local current stability}\to\ell_L^*,
\qquad
\text{solved amplitude localization}\to N_{active}^{eff}.
}
\]

Neither 8 nor 9 appears as a material/structural constant.

---

## 4. Continuous local-wavelength pre-screen from the retained C1 shape

Before evaluating the full qU energy for every candidate wavelength, the retained C1 shape gives a closed-form linear wavelength screen.

For

\[
\phi=(1-\cos k_xx)(1-\cos k_yy),
\]

exact area averages over one local rectangle are

\[
\langle\phi_x^2\rangle=\frac34k_x^2,
\qquad
\langle\phi_y^2\rangle=\frac34k_y^2,
\qquad
\langle\phi_x\phi_y\rangle=0,
\]

\[
\langle\phi_{xx}^2\rangle=\frac34k_x^4,
\qquad
\langle\phi_{yy}^2\rangle=\frac34k_y^4,
\]

\[
\langle\phi_{xx}\phi_{yy}\rangle=\frac14k_x^2k_y^2,
\qquad
\langle\phi_{xy}^2\rangle=\frac14k_x^2k_y^2.
\]

These identities were re-derived symbolically for this node; no spatial quadrature was used.

For an isotropic elastic steel plate with compression-positive proportional membrane resultants

\[
N_y^c=\Lambda,
\qquad
N_x^c=\rho\Lambda,
\qquad
N_{xy}=0,
\]

define

\[
r=\frac{k_y}{k_x}.
\]

The one-term Rayleigh predictor is

\[
\boxed{
\Lambda_{cr}(r)
=D_sk_x^2
\frac{3(1+r^4)+2r^2}{3(\rho+r^2)}.
}
\]

Let `z=r^2`. The continuous stationary condition is

\[
3z^2+6\rho z+2\rho-3=0.
\]

The positive interior root is

\[
\boxed{
z^*=-\rho+\sqrt{\rho^2-\frac23\rho+1},
\qquad
r^*=\sqrt{z^*}.
}
\]

Therefore the continuous local axial scale is

\[
\boxed{
\ell_{L,cont}^*=\frac{L_x}{r^*}
}
\]

because

\[
r=\frac{k_y}{k_x}=\frac{L_x}{L_y}.
\]

The corresponding continuous number of local wavelengths contained in one global halfwave is

\[
\boxed{
n_{cont}=\frac{\ell_G}{\ell_{L,cont}^*}
=\frac{\ell_G}{L_x}r^*.
}
\]

This is a **pre-screen**, not the final nonlinear selector. In the current qU theory, current biaxial membrane state, tangent, PBL registration and GL coupling can shift the selected scale.

---

## 5. Immediate BH-family consequence

For the current BH similarity geometry,

\[
L_x=0.225B,
\qquad
\ell_G=B.
\]

Under the axial-dominant benchmark `rho=0`,

\[
r^*=1,
\qquad
\ell_{L,cont}^*=L_x,
\]

so

\[
\boxed{
n_{cont}=\frac{1}{0.225}=4.444444\ldots}
\]

per complete global halfwave.

Thus the old whole-member `about 9` local waves is naturally explained as approximately

\[
2\times4.444=8.888
\]

when two global halfwaves of the physical BH member are both represented. It is not a universal `n=9` law.

If the existing C1-cell implementation is required to tile the representative halfwave by complete local cells, the nearest discrete realizations are `n=4` and `n=5`. They are candidate implementations only.

For all three similarity cases:

| Case | `ell_G` mm | `Lx` mm | `Ly(n=4)` mm | `Ly(n=5)` mm |
|---|---:|---:|---:|---:|
| BH020 | 1000 | 225 | 250 | 200 |
| BH032 | 1600 | 360 | 400 | 320 |
| BH050 | 2500 | 562.5 | 625 | 500 |

For `rho=0`, the normalized Rayleigh costs relative to the continuous optimum are identical for this similarity family:

\[
\frac{\Lambda_{cr}(n=4)}{\Lambda_{cr,cont}}-1
\approx1.6713\%,
\]

\[
\frac{\Lambda_{cr}(n=5)}{\Lambda_{cr,cont}}-1
\approx2.0906\%.
\]

Hence the simple linear screen slightly favors `n=4`; **this does not lock `n*=4`**. The full qU/current-state selection remains to be evaluated.

Also, the continuous result is primary. If future shell kinematics no longer require full C1 local-cell tiling in the global-y direction, `ell_L^*` need not be commensurate with `ell_G` at all.

---

## 6. Why the one-halfwave domain materially reduces the old BH050 assembly

Retaining the previous deterministic BH050 transverse registration only as a counting example:

Top face: 5 transverse bays.

Bottom face: 6 transverse bays.

Then one global halfwave gives:

### Candidate `n=4`

\[
N_{patch}^{top}=5\times4=20,
\]

\[
N_{patch}^{bottom}=6\times4=24,
\]

\[
\boxed{N_{patch}^{total}=44}.
\]

### Candidate `n=5`

\[
N_{patch}^{top}=5\times5=25,
\]

\[
N_{patch}^{bottom}=6\times5=30,
\]

\[
\boxed{N_{patch}^{total}=55}.
\]

The old full-length registration diagnostic used 99 patches. Therefore the representative-halfwave domain cuts the analytic patch count to 44 or 55 for these two nearby realizations.

**Important:** 44/55 are analytic integration/assembly objects, not 44/55 nonlinear unknowns.

---

## 7. Fixed 4 generalized local amplitudes per steel face

The unloaded state must remain exact. Therefore project the **amplitude increment**, not the raw amplitude.

For patch `b`, define

\[
u_b=U_b-A_{0b}.
\]

For one steel face introduce

\[
\mathbf a_f=
[a_1,a_2,a_3,a_4]^T.
\]

Let `Psi_f` be a fixed four-column analytic projection matrix for the current geometry/wavelength candidate. Then

\[
\boxed{
\mathbf u_f=\mathbf\Psi_f\mathbf a_f,
}
\]

or cellwise

\[
\boxed{
U_b=A_{0b}+\sum_{\alpha=1}^4\Psi_{b\alpha}a_\alpha.
}
\]

Consequently

\[
\boxed{
\mathbf a_f=0\Rightarrow U_b=A_{0b}
}
\]

for every patch, so the stress-free local imperfection is preserved exactly.

Substitution into the qU invariants gives

\[
d_b
=U_b^2-A_{0b}^2
=2A_{0b}(\Psi_b^T\mathbf a)+(\Psi_b^T\mathbf a)^2,
\]

and

\[
\Delta_b
=BqA_{0b}+B(q_0+q)(\Psi_b^T\mathbf a).
\]

No qU term is dropped.

---

## 8. Exact connection to the existing qU energy

For one face and one wavelength candidate,

\[
\boxed{
\Pi_f^{(4)}(\mathbf a_f;\mathbf z,\ell_L)
=
\sum_{b\in\mathcal H_f}
\Pi_b^{qU}
\left(A_{0b}+\Psi_b^T\mathbf a_f;\mathbf z,\ell_L\right),
}
\]

where `z` denotes the existing macro/section variables. If a local `Pi_b` is already area-integrated, it is included once; no extra cell-area weight is introduced.

Since

\[
\frac{\partial U_b}{\partial a_\alpha}=\Psi_{b\alpha},
\]

the reduced residual follows exactly by the chain rule:

\[
\boxed{
\mathbf R_a
=\frac{\partial\Pi_f^{(4)}}{\partial\mathbf a_f}
=\mathbf\Psi_f^T\mathbf R_U
=0.
}
\]

The exact local tangent is

\[
\boxed{
\mathbf K_{aa}
=\mathbf\Psi_f^T\mathbf K_{UU}\mathbf\Psi_f
}
\]

for fixed `Psi`.

Cross tangents to macro variables are

\[
\boxed{
K_{az}=\Psi^TK_{Uz},
\qquad
K_{za}=K_{zU}\Psi.
}
\]

Thus exact Schur condensation into the macro operator is

\[
\boxed{
K_{zz}^{eff}
=K_{zz}-K_{za}K_{aa}^{-1}K_{az}.
}
\]

For top and bottom faces kept distinct,

\[
\mathbf a=
[\mathbf a_+;\mathbf a_-]\in\mathbb R^8.
\]

Therefore the preceding BH050 diagnostic architecture changes from

\[
\boxed{99\ \text{independent local amplitudes}}
\]

to

\[
\boxed{4\ \text{per face}=8\ \text{local generalized amplitudes total}}.
\]

The nominal nonlinear-coordinate reduction is

\[
1-\frac8{99}=91.92\%.
\]

This is a dimension reduction only; no CPU speedup factor is claimed without a benchmark.

---

## 9. The reduced local equations remain finite cubic algebra

The source qU theory has, patchwise,

\[
R_{U_b}=B_{3b}U_b^3+B_{2b}U_b^2+B_{1b}U_b+B_{0b}.
\]

After

\[
U_b=A_{0b}+\Psi_b^T\mathbf a,
\]

each reduced equation is

\[
\boxed{
R_{a_\alpha}
=
\sum_b\Psi_{b\alpha}
\left[
B_{3b}U_b^3+B_{2b}U_b^2+B_{1b}U_b+B_{0b}
\right]=0.
}
\]

Because `U_b` is linear in the four generalized amplitudes, every `R_a_alpha` is a polynomial of total degree at most three in `(a1,a2,a3,a4)`.

A polynomial in four variables of total degree <=3 has at most

\[
\binom{4+3}{3}=35
\]

monomials including the constant term. Therefore each face remains a compact four-equation finite algebraic stationarity problem, regardless of whether the representative halfwave is assembled from 20, 25, 24, 30 or another finite number of analytic patches.

The patch number affects coefficient summation, not nonlinear state dimension.

---

## 10. Do not use the previously proposed degenerate cell-center carrier basis

A previous exploratory suggestion used columns of the form

\[
\cos(k_Ly_j),\qquad\sin(k_Ly_j)
\]

at cell centers.

For complete local cells with

\[
y_j=(j-1/2)\ell_L,
\qquad
k_L=2\pi/\ell_L,
\]

this degenerates because

\[
\cos(k_Ly_j)=-1,
\qquad
\sin(k_Ly_j)=0.
\]

Therefore that cell-center basis is **retracted** and must not be used.

The exact qU condensation in Sections 7-9 is independent of this basis choice: it only requires a full-rank four-column analytic `Psi`.

A production `Psi` is deliberately **not yet locked**. It must pass the physical N/M and morphology sufficiency gate. Candidate construction should retain at minimum:

- a mean/local-amplitude component;
- an alternating local-cell component if alternating inward/outward lobes are mechanically relevant;
- an analytically generated global-local envelope component derived from the existing global field/`h_x,h_y,h_gamma`, not from FE fitting;
- an envelope × alternating component.

For example, a provisional structural form may be

\[
\Psi_1=1,
\qquad
\Psi_2=s_b,
\qquad
\Psi_3=G_b,
\qquad
\Psi_4=s_bG_b,
\]

where `s_b` is a deterministic local phase/parity convention and `G_b` is an exact analytic global-local driving/envelope coefficient. This is only a basis family; exact definitions and rank tests remain a separate gate.

---

## 11. Effective number of buckling cells is an output, not a discrete state variable

The user-observed number of strong lobes/cells is physically relevant, but introducing a separate integer state such as `N_active=4/8/9` would reintroduce a large state machine and make the theory sample-specific.

Instead, after solving the four generalized amplitudes, every analytic patch has a reconstructed increment

\[
u_b=\Psi_b^T\mathbf a.
\]

For axial local-cell strip `j`, aggregate its local amplitude energy-like participation across transverse bays:

\[
E_j^{loc}=\sum_{i\in j}A_{ij}u_{ij}^2.
\]

Define normalized participation

\[
p_j=\frac{E_j^{loc}}{\sum_kE_k^{loc}}.
\]

Then define the inverse-participation effective cell count

\[
\boxed{
N_{active}^{eff}=\frac1{\sum_jp_j^2}.
}
\]

Properties:

- one dominant axial cell -> `N_active_eff = 1`;
- `n` equally active cells -> `N_active_eff = n`;
- partial/localized participation -> a continuous value between 1 and `n`.

This quantity introduces **no additional unknown** and no arbitrary amplitude threshold. It is a morphology diagnostic/output. It may later be related to an effective active local length

\[
L_{active}^{eff}=N_{active}^{eff}\ell_L^*,
\]

but it is not promoted to a production constitutive variable at this stage.

Thus the three user-identified physical scales become explicit:

\[
\boxed{
\ell_G,
\qquad
\ell_L^*,
\qquad
N_{active}^{eff}.
}
\]

---

## 12. Exact nonlinear local-wavelength selector on one global halfwave

The linear Rayleigh relation in Section 4 is only a pre-screen. The final qU selector must use the same reduced current energy that later feeds the steel-shell operator.

For a candidate local wavelength `ell_L` (or a discrete realization `n` when complete-cell tiling is required):

1. Set

\[
k_y=2\pi/\ell_L.
\]

2. Recompile the exact geometry coefficients

\[
c_y,\ h_x,\ h_y,\ h_\gamma,\ K_A,\ K_{d\Delta},\ K_{\Delta\Delta}
\]

for that local scale and registration.

3. Assemble only one complete global halfwave.

4. Solve the unloaded-connected reduced qU stationarity equations

\[
R_a=0.
\]

5. Condense consistently against the existing macro variables. If local stability is evaluated after macro equilibrium has been enforced, use the corresponding reduced local Hessian

\[
\boxed{
K_{aa}^{cond}
=K_{aa}-K_{az}K_{zz}^{-1}K_{za}
}
\]

with the exact variable ordering used by the implementation.

6. Define local-mode onset for that wavelength by

\[
\boxed{
q_{L,cr}(\ell_L)
=
\inf\left\{
q>0:\lambda_{min}[K_{aa}^{cond}(q;\ell_L)]=0
\right\}.
}
\]

7. Select

\[
\boxed{
\ell_L^*
=\arg\min_{\ell_L\in\mathcal A_L}
q_{L,cr}(\ell_L),
}
\]

where `A_L` is the admissible local-wavelength set implied by the C1 geometry/boundary contract.

If the current implementation requires complete local-cell tiling of one global halfwave, this reduces to

\[
\boxed{
n^*=\arg\min_{n\in\mathbb N}q_{L,cr}(n),
\qquad
\ell_L^*=\ell_G/n^*.
}
\]

No hard-coded 8/9 appears.

A material-domain boundary encountered before the local tangent singularity remains a material-domain event; it must not be relabeled as a local wavelength optimum.

---

## 13. Relation to the existing FE morphology evidence

Existing read-only FE extraction reports whole-member strong-lobe counts/spacings approximately:

- BH020 TOP/BOTTOM: 4 strong lobes, spacing ~226.7 mm;
- BH032 TOP: 4, ~405.3 mm;
- BH032 BOTTOM: 8, ~365.7 mm;
- BH050 TOP: 8, ~557.1 mm;
- BH050 BOTTOM: 9, ~525.0 mm.

The same reports state that localization suppresses some lobes, so these are not exact modal identities.

The current theory reduction therefore does **not** attempt to reproduce whole-member 4/8/9 counts as prescribed inputs. Instead:

- the representative global halfwave fixes the formal domain;
- the local stability problem selects `ell_L*`;
- the solved reduced amplitude field gives `N_active_eff` within the representative halfwave;
- whole-member repeated-halfwave localization remains a validation observable.

This preserves the useful FE information without fitting the theoretical wave number to FE.

---

## 14. Complexity ledger after this reduction

Old BH050 diagnostic:

```text
physical longitudinal length represented: 5000 mm
axial registration cells: 9
TOP analytic patches: 5 x 9 = 45
BOTTOM analytic patches: 6 x 9 = 54
total analytic patches: 99
independent local amplitudes: 99
```

One-complete-global-halfwave candidate `n=4`:

```text
formal length: 2500 mm
TOP analytic patches: 20
BOTTOM analytic patches: 24
total analytic patches: 44
local generalized amplitudes: 4 + 4 = 8
```

One-complete-global-halfwave candidate `n=5`:

```text
formal length: 2500 mm
TOP analytic patches: 25
BOTTOM analytic patches: 30
total analytic patches: 55
local generalized amplitudes: 4 + 4 = 8
```

Thus two different reductions occur simultaneously:

1. **domain reduction:** full physical member -> one complete global halfwave;
2. **state reduction:** one amplitude per patch -> four generalized amplitudes per face.

The first reduces analytic summation work; the second prevents nonlinear dimension from growing with geometry or selected local wave count.

---

## 15. Gate result

```text
ONE_COMPLETE_GLOBAL_HALFWAVE_DOMAIN = PASS
    Reason: already consistent with the BH family global m* formulation and the project's representative-halfwave architecture.

HARDCODED_LOCAL_8_OR_9 = RETIRED / FAIL
    Reason: those numbers are whole-member/case-specific morphology or registration values, not universal inputs.

CONTINUOUS_LOCAL_WAVELENGTH_PRE-SCREEN = PASS
    Reason: exact C1 derivative integrals and closed Rayleigh stationary condition derived.

BH_SIMILARITY_SCREEN = PASS
    Result: rho=0 benchmark gives ell_L,cont*=Lx and n_cont=4.444 per global halfwave; n=4/5 are neighboring complete-cell realizations.

FIXED_4DOF_qU_ENERGY_CONNECTION = PASS
    Reason: exact chain-rule projection of the existing qU energy; each face remains four coupled cubic residual equations.

UNLOADED_IMPERFECTION_IDENTITY = PASS
    Reason: projection is applied to u=U-A0, so a=0 exactly restores U=A0.

EXACT_NONLINEAR_ell_L_STAR = HOLD
    Reason: KdDelta/KDeltaDelta/h coefficients must be recompiled as functions of the candidate local scale and the reduced branch must be executed; the present node has only completed the analytic selector and linear pre-screen.

FOUR_COLUMN_PSI_PRODUCTION_BASIS = HOLD
    Reason: exact basis definitions must still pass rank, N/M sufficiency and morphology tests. The earlier degenerate cell-center cos/sin proposal is explicitly withdrawn.

UNIFIED_THICKNESS-INTEGRATED_STEEL_SHELL_NM_OPERATOR = HOLD
    Reason: after the local reduction passes, the current stress field must still be integrated through the physical steel thickness and audited against macro N/M; cell-mean stress is not the final section operator.

PRODUCTION_R14 = UNCHANGED
```

---

## 16. Immediate next execution target

Do **not** return to 99 independent local amplitudes and do **not** add C_P transfer yet.

Next execution should be:

1. implement the one-halfwave qU coefficient compiler with `ell_L`/`n` as an input;
2. explicitly evaluate BH050 neighboring local-scale candidates beginning with `n=4` and `n=5` because the analytic screen brackets the current similarity optimum;
3. solve the fixed-4DOF local stationarity system for each face along the connected branch;
4. compare `q_L,cr`, reconstructed `N_active_eff`, and coarse steel-face N/M sensitivity;
5. only then decide whether the four-column analytic basis is sufficient or must be enlarged/reorganized;
6. if sufficient, proceed to the unified steel stress field -> through-thickness N/M operator -> existing R4.

No Pu generated from this node is production-authorized.
