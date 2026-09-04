# NZ-SCCM Multiwave Steel Shell 03 — fixed-m=2 distributed partial interaction with PBL k_ps

Status: DIAGNOSTIC / THEORY-DEVELOPMENT. Production R14 is not modified.

This R02 supersedes the 20260904 Multiwave-03 R01 **only on the global-mode selection and connector-stiffness instantiation**. R01 incorrectly allowed the newly introduced partial-interaction stiffness to re-rank the global longitudinal mode and changed the BH global halfwave count from m=2 to m=3. That crossed the frozen R14 / Multiwave-01/02 mode boundary. In R02, the established BH global mode is frozen at m*=2; only one representative complete global halfwave is computed:

\[
L_G=a/2.
\]

Hence, for the BH family with a=2b,

\[
L_G=b.
\]

For standard bays with s=0.225b,

\[
n_0=\lfloor L_G/s\rfloor=\lfloor 1/0.225\rfloor=4,
\]

and the standard local candidates remain

\[
n=3,4,5.
\]

The purpose of partial interaction in this version is to modify force transfer and the stiffness of this **fixed m=2 mode**, not to open a new global mode-selection problem.

---

## 1. PBL shear stiffness source used for the diagnostic instantiation

The user supplied a structural-design formula for the shear stiffness of a perforated-plate connector:

\[
\boxed{k_{ps}=23.4\sqrt{(d-d_s)d_sE_cf_{ck}}}\qquad (N/mm)
\]

where:

- d = perforated-plate hole diameter (mm),
- d_s = through-rebar diameter (mm),
- E_c = concrete elastic modulus (MPa),
- f_ck = concrete compressive-strength standard value (MPa).

For the first R02 diagnostic instantiation, choose a geometrically plausible small PBL detail that fits the current approximately 37 mm rib height:

\[
\boxed{d=20\ mm,\qquad d_s=8\ mm.}
\]

The current UHPC material inputs are provisionally inserted as

\[
E_c=43400\ MPa,
\qquad
f_{ck}^{trial}=141.1\ MPa.
\]

Therefore,

\[
\begin{aligned}
k_{ps}
&=23.4\sqrt{(20-8)\times 8\times 43400\times141.1}\\
&=5.67361478\times10^5\ N/mm.
\end{aligned}
\]

Thus

\[
\boxed{k_{ps}=567.361\ kN/mm\ per\ hole.}
\]

This value is **not calibrated to FEM**.

The current PBL design rule in Sun's thesis recommends the longitudinal hole center spacing to be approximately 2.5d to 3.5d. R02 takes the neutral mid-range value

\[
\boxed{s_c=3d=60\ mm.}
\]

Hence the line stiffness of one longitudinal PBL rib is

\[
\boxed{k_{\ell,r}=\frac{k_{ps}}{s_c}}
\]

and numerically

\[
\boxed{k_{\ell,r}=9.45602\ kN/mm^2.}
\]

For a face with N_r longitudinal PBL ribs,

\[
\boxed{k_\ell^{(f)}=N_r^{(f)}k_{\ell,r}.}
\]

For the BH TOP face (N_r^+=4):

\[
\boxed{k_+=37.82410\ kN/mm^2.}
\]

For the BH BOTTOM face (N_r^-=5):

\[
\boxed{k_-=47.28012\ kN/mm^2.}
\]

This replaces the R01 interpretation of 75.835 kN/mm as the total stiffness of an entire rib. The old 75.835 number is not used in R02.

---

## 2. Three-layer distributed partial-interaction system on the fixed m=2 global halfwave

Define the three longitudinal phases:

- TOP steel face: +,
- continuous UHPC+web core: c,
- BOTTOM steel face: -.

Steel plane-stress modulus:

\[
Q_s=\frac{E_s}{1-\nu_s^2}.
\]

One steel-face longitudinal membrane stiffness:

\[
\boxed{A_s=Q_sbt_s.}
\]

With

\[
\rho_w=\frac{A_w}{bt_c},
\qquad
Q_c=\frac{E_c}{1-\nu_c^2},
\]

the initial longitudinal core stiffness used only in the partial-interaction condensation is

\[
\boxed{A_c=Q_c(1-\rho_w)bt_c+E_sA_w.}
\]

The fixed global mode is

\[
\boxed{m=2,\qquad \beta=\frac{2\pi}{a}=\frac{\pi}{L_G}.}
\]

The global curvature amplitudes are \(\kappa_x,\kappa_y\). Because of steel plane-stress coupling, the longitudinal connector-driving curvature is

\[
\boxed{\chi=\kappa_y+\nu_s\kappa_x.}
\]

Introduce one longitudinal relative-displacement harmonic per phase:

\[
r_+(y)=R_+\cos\beta y,
\]

\[
r_c(y)=R_c\cos\beta y,
\]

\[
r_-(y)=R_-\cos\beta y.
\]

Interface slips are

\[
s_+(y)=r_+(y)-r_c(y),
\]

\[
s_-(y)=r_-(y)-r_c(y).
\]

The connector shear flows are

\[
q_+(y)=k_+s_+(y),
\]

\[
q_-(y)=k_-s_-(y).
\]

No spatial connector grid is introduced.

---

## 3. Exact one-harmonic energy and static condensation

Let

\[
z_f=\frac{t_c+t_s}{2}.
\]

The partial-interaction energy over one complete m=2 representative halfwave is

\[
\begin{aligned}
\Pi_{PI}={}&\frac12\int A_s[r_+'^2+2z_f\chi\sin(\beta y)r_+']dy\\
&+\frac12\int A_cr_c'^2dy\\
&+\frac12\int A_s[r_-'^2-2z_f\chi\sin(\beta y)r_-']dy\\
&+\frac12\int k_+(r_+-r_c)^2dy\\
&+\frac12\int k_-(r_--r_c)^2dy.
\end{aligned}
\]

Using the exact halfwave moments of sine/cosine, stationarity gives

\[
\boxed{\mathbf K_m\mathbf R=F\mathbf v}
\]

with

\[
\mathbf R=\begin{bmatrix}R_+\\R_c\\R_-\end{bmatrix},
\qquad
\mathbf v=\begin{bmatrix}1\\0\\-1\end{bmatrix},
\]

\[
F=A_s\beta z_f\chi,
\]

and

\[
\boxed{
\mathbf K_m=
\begin{bmatrix}
A_s\beta^2+k_+ & -k_+ & 0\\
-k_+ & A_c\beta^2+k_++k_- & -k_-\\
0 & -k_- & A_s\beta^2+k_-
\end{bmatrix}.}
\]

No empirical gamma is inserted.

For explicit evaluation define

\[
a_s=A_s\beta^2+k_+,
\]

\[
d_s=A_s\beta^2+k_-,
\]

\[
c_s=A_c\beta^2+k_++k_-.
\]

Then

\[
H_c=c_s-\frac{k_+^2}{a_s}-\frac{k_-^2}{d_s}.
\]

For unit forcing F=1:

\[
R_c^{(1)}=\frac{k_+/a_s-k_-/d_s}{H_c},
\]

\[
R_+^{(1)}=\frac{1+k_+R_c^{(1)}}{a_s},
\]

\[
R_-^{(1)}=\frac{-1+k_-R_c^{(1)}}{d_s}.
\]

The displacement-derived strain-transfer lengths are

\[
\boxed{h_+=-A_s\beta^2z_fR_+^{(1)}},
\]

\[
\boxed{h_c=-A_s\beta^2z_fR_c^{(1)}},
\]

\[
\boxed{h_-=-A_s\beta^2z_fR_-^{(1)}}.
\]

Therefore at the control section of the fixed complete halfwave:

\[
\boxed{\varepsilon_{y,s}^{+}=\varepsilon_y^0+z_f\kappa_y+h_+(\kappa_y+\nu_s\kappa_x)}
\]

\[
\boxed{\varepsilon_{y,s}^{-}=\varepsilon_y^0-z_f\kappa_y+h_-(\kappa_y+\nu_s\kappa_x)}
\]

and the core longitudinal strain is

\[
\boxed{\varepsilon_y^c(z)=\varepsilon_y^0+h_c(\kappa_y+\nu_s\kappa_x)+z\kappa_y.}
\]

Transverse strains are unchanged:

\[
\varepsilon_{x,s}^{\pm}=\varepsilon_x^0\pm z_f\kappa_x,
\qquad
\varepsilon_x^c(z)=\varepsilon_x^0+z\kappa_x.
\]

---

## 4. Consistent fixed-mode bending stiffness

Although m is frozen at 2 and is not re-ranked, the stiffness used by this prescribed mode must still be consistent with the same partial-interaction condensation.

Let

\[
\Psi=\mathbf v^T\mathbf K_m^{-1}\mathbf v=R_+^{(1)}-R_-^{(1)}.
\]

The released combination-bending stiffness is

\[
\boxed{\Delta D=\frac{(A_s\beta z_f)^2}{b}\Psi.}
\]

Starting from the full-composite bending constants \(D_x^{FC},D_y^{FC},D_\mu^{FC}\), the m=2 effective constants are

\[
\boxed{D_x^{PI}=D_x^{FC}-\nu_s^2\Delta D}
\]

\[
\boxed{D_\mu^{PI}=D_\mu^{FC}-\nu_s\Delta D}
\]

\[
\boxed{D_y^{PI}=D_y^{FC}-\Delta D.}
\]

R02 keeps

\[
D_{66}^{PI}=D_{66}^{FC}
\]

because the current slip field has y-dependence only and no x-dependent slip DOF.

The important governance rule is:

\[
\boxed{m=2\ \text{is fixed.}}
\]

Thus \(D^{PI}\) updates \(P_{cr}\), \(J_x\), \(J_y\), and the force balance **within the fixed m=2 subspace**, but does not trigger a new minimization over m.

---

## 5. Fixed standard and edge local-bay rules

For the BH family:

\[
L_G=a/2=b.
\]

Standard bay width:

\[
s=0.225b.
\]

Hence

\[
n_0=4,
\qquad
n=3,4,5.
\]

TOP uses the already frozen standard pattern 3/4/5. BOTTOM uses 3/4/5/4.

Non-standard edge bays are not forced into an E branch. Each edge bay uses its actual width and performs its own local-buckling gate.

TOP total remaining width is 0.325b, hence each TOP edge bay is

\[
b_{e,+}=0.1625b.
\]

Its own nominal wave count is

\[
n_{e,+}=\left\lfloor\frac{L_G}{b_{e,+}}\right\rfloor=6.
\]

BOTTOM each edge bay is

\[
b_{e,-}=0.05b,
\]

so

\[
n_{e,-}=20.
\]

Each standard or edge bay applies the same local elastic buckling gate

\[
\sigma_{cr}^E\gtreqless f_y.
\]

If local-first, the same R02 cubic amplitude and R06 first-local-yield capped reduced operator are used. If yield-first, the full-thickness ideal-EP branch is used.

---

## 6. Numerical instantiation for BH032 and BH050

Using d=20 mm, ds=8 mm, sc=60 mm:

\[
k_{ps}=567.361\ kN/mm/hole,
\]

\[
k_{\ell,r}=9.45602\ kN/mm^2/rib,
\]

\[
k_+=37.82410\ kN/mm^2,
\qquad
k_-=47.28012\ kN/mm^2.
\]

### BH032

For b=1600 mm, a=3200 mm, m=2:

\[
\boxed{h_+=-2.84441\ mm},
\]

\[
\boxed{h_c=+0.131993\ mm},
\]

\[
\boxed{h_-=+2.54812\ mm}.
\]

Equivalent pure-y-curvature retained lever fractions are

\[
\frac{z_f+h_+}{z_f}=0.87633,
\]

\[
\frac{z_f-h_-}{z_f}=0.88921.
\]

The condensed fixed-mode critical load is

\[
\boxed{P_{cr}^{PI,m=2}=29.43275\ MN.}
\]

### BH050

For b=2500 mm, a=5000 mm, m=2:

\[
\boxed{h_+=-1.90241\ mm},
\]

\[
\boxed{h_c=+0.091523\ mm},
\]

\[
\boxed{h_-=+1.70183\ mm}.
\]

Equivalent retained lever fractions are

\[
0.91729,
\qquad
0.92601.
\]

and

\[
\boxed{P_{cr}^{PI,m=2}=19.08107\ MN.}
\]

These values are physically much closer to the no-slip limit than the previous R01 trial based on the misinterpreted 75.835 kN/mm/rib total stiffness.

---

## 7. Theory identity

The corrected R02 chain is

\[
\boxed{
\text{fixed }m=2
\to
L_G=a/2
\to
k_{ps}(d,d_s,E_c,f_{ck})
\to
k_{\ell,r}=k_{ps}/s_c
\to
\mathbf K_m
\to
(h_+,h_c,h_-)
\to
D^{PI}_{m=2}
\to
\text{existing multiwave R02/R06 section operator}
\to
N/M
\to
R_4.
}
\]

No re-ranking of m is allowed in Multiwave-03 R02. Any future investigation of whether connector compliance changes the global integer mode is a separate diagnostic gate and does not belong inside the current fixed-R14 mode branch.
