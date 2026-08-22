# NZ-SCCM — Panel21 geometry / wavelength / reinforcement mapping audit + continuous TC–TT postcrack-tension execution R02

**Time:** 2026-08-22 22:56 +08:00  
**Status:** `EXECUTED / PANEL21_GEOMETRY_PASS / HALFWAVE_PASS / REBAR_MAPPING_CORRECTED / PRIOR_2130_2205_VALUES_SUPERSEDED / EXPLICIT_STRUCTURAL_PATH_UNCHANGED / ZERO_FORMAL_QUADRATURE`

## 0. Hard boundary

This audit was requested before any further material change because the Panel21 prediction was anomalously low. The structural path is **not** reopened.

The following remain unchanged:

- prescribed Nguyen/Swartz source waveform as exogenous geometry input;
- full plate domain `a=2440 mm`, `b=1220 mm`;
- source-wave finite trigonometric representation;
- explicit structural relation
  \[
  P_\Phi(q)=P_{cr,\Phi}\frac{q}{q+q_0}+C_\Phi q(q+2q_0),
  \qquad q_0=1/400;
  \]
- full two-independent-affine-slope section variables
  \[
  \lambda_x=a_x+b_xz,\qquad \lambda_y=a_y+b_yz;
  \]
- section demand/equilibrium in `Nx,Ny,Mx,My`;
- NC-M6 two-dimensional TC crack front;
- NC CC branch and Vecchio–Collins gamma law;
- no `Pf` in root selection or parameter identification;
- formal spatial quadrature = 0 and formal material points = 0.

The only input correction is the reinforcement-ratio interpretation required by Nguyen Table 5.1 and the already-audited R23 mapping.

---

## 1. Panel21 source geometry and wavelength audit

Nguyen Chapter 5 defines the Swartz wall as

\[
a=2.44\ \mathrm m,\qquad b=1.22\ \mathrm m,
\]

with four-edge out-of-plane simple support and uniform in-plane compression. Panel21 has

\[
t=19.30\ \mathrm{mm},\quad f'_{cyl}=24.98\ \mathrm{MPa},\quad 0.85f'_{cyl}=21.23\ \mathrm{MPa},
\]

\[
E_0=20321\ \mathrm{MPa},\quad \varepsilon_0=0.00209,
\quad p=0.75\%,\quad h_r=0,\quad n_{layer}=1.
\]

Direct geometry gives

\[
\frac bt=\frac{1220}{19.30}=63.2124\approx63.2,
\]

matching Nguyen's table entry for Panel21.

### 1.1 Figure 5.6 caption typo

Figure 5.6a is captioned `Panel No.21 (b/t=64.3)`, but the adjacent source tables give `64.3` for Panel20 and `63.2` for Panel21. The direct geometry also gives `63.21`. Therefore `64.3` in the Figure 5.6a caption is treated as a source caption typo; the model geometry is **not** altered to force that value.

### 1.2 Longitudinal halfwaves

Nguyen explicitly reports that Panels 17–24 buckle in **two sinusoidal halfwaves**, and specifically states that Panel21's computed shape is similar to the experimentally recorded shape.

Hence the nominal representative longitudinal halfwave length is

\[
\boxed{\ell=a/2=1220\ \mathrm{mm}}.
\]

The current explicit source-wave implementation is consistent with this. It keeps the physical full length `A=2440 mm`, but Panel21 uses

\[
\Phi_{21}(u)=
-0.12203066\sin\pi u
-0.76471804\sin2\pi u
+0.18158893\sin3\pi u
+0.25675995\sin4\pi u,
\qquad u=y/a.
\]

The dominant `n=2` harmonic therefore represents the two-halfwave source mode. Keeping `A=2440 mm` in the finite-series representation does **not** mean that a 2440-mm single halfwave is being used.

A direct finite-series check gives:

- internal zero at `u≈0.537068`, i.e. `y≈1310.45 mm`;
- unequal observed source lobes approximately `1310.45 mm` and `1129.55 mm`;
- first negative extremum `u≈0.35056`;
- second positive extremum `u≈0.71322`;
- nine-station normalized waveform RMSE ≈ `0.0218`.

The current Panel21 controlling source-wave coordinate `u≈0.356` therefore lies essentially at the first observed lobe extremum. There is no evidence here of a halfwave/wavelength error capable of explaining the low Panel21 event.

```text
PANEL21_FULL_LENGTH_A = 2440 mm
PANEL21_WIDTH_B = 1220 mm
PANEL21_REFERENCE_HALFWAVES = 2
PANEL21_NOMINAL_HALFWAVE_LENGTH = 1220 mm
PANEL21_WAVELENGTH_AUDIT = PASS
PANEL21_SOURCE_WAVEFORM_AXIS_MAPPING = PASS
```

---

## 2. Reinforcement-ratio audit — a real implementation error was found

Nguyen Table 5.1 explicitly defines `p` as the **nominal total steel ratio (percent)**. For an isotropic two-way mesh, the project source-consistent mapping already audited in R23 is

\[
\boxed{
\rho_{s,dir,layer}=\frac{p}{2n_{layer}}.
}
\]

Thus Panel21 requires

\[
\boxed{ho_{sx}=\rho_{sy}=0.00375,\qquad z_s=0.}
\]

However, the frozen source-wave front end used by the 19:27, 21:30 and 22:05 diagnostics contained

```python
ax = [p*t/L] * L
ay = [p*t/L] * L
```

so `p=0.0075` was assigned independently to both x and y reinforcement families. This doubles the total steel content.

This is the same mapping error previously identified historically in the R23 Branch-C audit. It is an **input mapping bug**, not a change to the explicit structural equations.

### 2.1 Reproduction gate

Before applying the correction, the current exact Panel21 implementation was reconstructed and run with the old doubled mapping. At the 21:30 M6/F03 source-wave location it reproduces

\[
\boxed{P_{event}=180.159347\ \mathrm{kN}}
\]

and the published M6 state to machine precision. Therefore the correction is being applied to the same current explicit calculation, rather than to a replacement solver.

### 2.2 Corrected M6/F03 result

With only

\[
0.0075\ \text{per direction}\rightarrow0.00375\ \text{per direction},
\]

the connected stationary section fold becomes

\[
\boxed{u=0.3559087784},
\]

\[
\boxed{q=0.00134759},
\]

\[
\boxed{P_{event}=173.209915\ \mathrm{kN}}.
\]

Thus correcting the source input does **not** explain the low prediction by raising Panel21; it makes the baseline M6/F03 fold slightly lower.

```text
OLD_PANEL21_RHO_PER_DIRECTION = 0.0075   # WRONG: doubles nominal total p
CORRECT_PANEL21_RHO_PER_DIRECTION = 0.00375
OLD_M6_F03_PANEL21 = 180.159347 kN
CORRECTED_M6_F03_PANEL21 = 173.209915 kN
PRIOR_2130_PANEL21_NUMBER = SUPERSEDED_QUANTITATIVELY
PRIOR_2205_BOND_TARGETS_AND_PANEL21_NUMBERS = SUPERSEDED_QUANTITATIVELY
```

Because Panels 1 and 14 in the same source-wave front end use the same `rc_stiffness` construction, their previous 19:27/21:30/22:05 numerical values are also not retained as production evidence until they are rerun with the source-correct directional split.

---

## 3. Corrected bond parameter for Panel21

The previous 22:05 bond diagnostic also used `p=0.0075` as a directional reinforcement ratio. With the corrected directional ratio

\[
\rho_{dir}=0.00375
\]

and source wire diameter `d_b=2.7 mm`, the directional Bentz spacing parameter is

\[
\boxed{m=\frac{d_b}{4\rho_{dir}}=180.0\ \mathrm{mm}},
\]

not `90 mm`.

Using the same previously declared diagnostic endpoint projection:

### Bentz `3.6m`

\[
c_t=648.0\ \mathrm{mm},
\qquad
\boxed{\alpha_{2,B}=0.5486090032}.
\]

### Modified Bentz `3.6(0.6)m`

\[
c_t=388.8\ \mathrm{mm},
\qquad
\boxed{\alpha_{2,B}=0.6107497582}.
\]

These replace the earlier Panel21 `0.632/0.689` targets, which were based on doubled reinforcement.

---

## 4. Authorized next step executed — one continuous bond-dependent postcrack tensile layer across TC and TT

The previous TC-only blend was deliberately made to vanish at the TC→TT boundary in order to keep the old TT branch unchanged. That construction was useful diagnostically but prevented the bond/reinforcement dependence from surviving in weak-compression TC states.

The present execution performs the proposed next diagnostic while preserving the structural path:

- use the same source-derived bond target `alpha2,B` in the postcrack tension law on both the TC and TT sides;
- retain the NC-M6 two-dimensional TC crack front;
- retain CC and the literal VC gamma law;
- use the same finite Foster grammar so every through-thickness branch still has an exact finite primitive;
- use the derivative of the same law for the section Jacobian;
- introduce no formal numerical spatial/thickness quadrature;
- do not use `Pf` to choose `alpha2` or a root.

This removes an artificial TC→TT postcrack-stress mismatch without changing the source-wave structure.

### 4.1 Corrected B99 result

For

\[
\alpha_2=0.5486090032,
\]

the connected stationary fold is

\[
\boxed{u=0.3558050551},
\quad
\boxed{q=0.0014349058},
\quad
\boxed{P_{event}=180.549929\ \mathrm{kN}}.
\]

The section state is approximately

\[
(a_x,a_y,b_x,b_y)
=(0.0860995,-0.1746163,-0.0228311,-0.0119752).
\]

The singular section mode, normalized by its largest component, is approximately

\[
(1,\ 0.00715,\ -0.16725,\ 0.000089),
\]

so the fold remains overwhelmingly transverse-tension controlled. The mid-plane steel stresses are only about `+49.1 MPa` and `-79.5 MPa`; steel yield is not the control.

The two concrete faces are approximately

\[
(\lambda_x,\lambda_y)_{z=-h}
=(+0.30642,-0.05906),
\]

\[
(\lambda_x,\lambda_y)_{z=+h}
=(-0.13422,-0.29018),
\]

so the section remains `TC -> CC`, with no controlling TT zone.

### 4.2 Corrected Modified-Bentz result

For

\[
\alpha_2=0.6107497582,
\]

the connected stationary fold is

\[
\boxed{u=0.3557652290},
\quad
\boxed{q=0.0014687882},
\quad
\boxed{P_{event}=183.318982\ \mathrm{kN}}.
\]

The section state is approximately

\[
(a_x,a_y,b_x,b_y)
=(0.1088101,-0.1773154,-0.0267139,-0.0122953),
\]

and the normalized singular mode is approximately

\[
(1,\ 0.00718,\ -0.16197,\ 0.000093).
\]

Again the fold is transverse-tension controlled. Mid-plane steel stresses are only about `+58.8 MPa` and `-82.3 MPa`.

The faces are approximately

\[
(\lambda_x,\lambda_y)_{z=-h}
=(+0.36660,-0.05867),
\]

\[
(\lambda_x,\lambda_y)_{z=+h}
=(-0.14898,-0.29596).
\]

---

## 5. Main verdict

The audit separates the geometry/input issue from the material-shape issue.

### A. Panel21 wavelength and source waveform are not the cause

The source geometry, two-halfwave count, nominal `ell=1220 mm`, coordinate orientation and current source-wave control location all pass.

### B. A real steel-ratio double-counting bug existed

The old source-wave front end used the nominal total `p` in each direction. The correct Panel21 directional ratio is `0.00375`. All dependent old 19:27/21:30/22:05 numerical values must therefore be regarded as quantitatively superseded until rerun.

### C. Correcting the steel input does not cure Panel21

The exact M6/F03 fold moves from `180.16` to `173.21 kN`.

### D. Extending reinforcement/bond dependence continuously across TC and TT also does not cure Panel21

The two corrected source-anchored targets give only

\[
180.55\ \mathrm{kN}
\quad\text{and}\quad
183.32\ \mathrm{kN}.
\]

Both remain near half of the measured failure comparator. More importantly, the singular mode remains almost entirely the transverse tensile material coordinate.

### E. The remaining deficiency is now localized to the **postcrack tensile tangent shape**, not primarily the residual alpha2 level

At these folds the tensile face lies on the **linear Foster softening segment**. Its tangent is constant,

\[
\frac{d\sigma_t}{d\lambda_t}
=-\frac{1-\alpha_2}{9}\,E_0\varepsilon_0.
\]

For the modified-Bentz target this is only a constant negative slope over the whole softening interval. Increasing the retained-stress endpoint shifts the fold somewhat, but it does not remove the premature tension-tangent singularity.

This is consistent with the earlier diagnostic observation that a nonlinear postcrack shape such as Belarbi–Hsu changes Panel21 much more strongly than merely changing Foster `alpha2`.

---

## 6. Next unique material task

Keep the corrected steel mapping and the explicit structural path frozen.

The next task is **not** another `alpha2` sweep and not a waveform change. It is:

\[
\boxed{\text{derive a source-based nonlinear postcrack tensile response across TC/TT}}
\]

with all of the following gates:

1. no `Pf` parameter identification;
2. TC uses the NC-M6 current two-dimensional crack front;
3. the tensile response is continuous across TC↔TT;
4. stress and tangent come from the same law;
5. the through-thickness section resultants retain a finite exact/analytic zero-quadrature representation;
6. CC and the VC gamma law remain unchanged;
7. the source-wave structural operator remains unchanged.

The first candidate family to audit is the already-source-motivated **Belarbi–Hsu 0.4 nonlinear postcrack shape**, but only after deriving an exact/analytic primitive compatible with the moving NC-M6 crack front. A numerical thickness quadrature implementation is not admissible.

```text
PANEL21_GEOMETRY_WAVELENGTH_GATE = PASS
PANEL21_REBAR_MAPPING_GATE = CORRECTED
PANEL21_OLD_M6_F03 = SUPERSEDED
PANEL21_CORRECTED_M6_F03 = 173.209915 kN
PANEL21_CONTINUOUS_TC_TT_B99 = 180.549929 kN
PANEL21_CONTINUOUS_TC_TT_B03 = 183.318982 kN
PANEL21_PRIMARY_REMAINING_GAP = NONLINEAR_POSTCRACK_TENSION_TANGENT_SHAPE
NEXT_RC_TASK = DERIVE_EXACT_NONLINEAR_POSTCRACK_TENSION_SHAPE_ACROSS_TC_TT
EXPLICIT_STRUCTURAL_PATH_CHANGED = FALSE
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_MATERIAL_POINTS = 0
Pf_IN_ROOT_SELECTION = 0
```
