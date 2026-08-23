# NZ-SCCM — Resultant-only RC terminal active-set elimination + uniaxial ablation R02

**Time:** 2026-08-24 01:05 +08:00  
**Status:** `ACTIVE_SET_ELIMINATION = PASS / GENERIC_OPTIMIZER = REMOVED / R01_NUMERIC_TABLE = SUPERSEDED / AIRY_UNCHANGED / SWARTZ8_ONLY / NX_TERMINAL_STATUS = REOPENED`

## 0. Scope

Only the fixed common set

\[
\{4,5,6,8,9,14,21,23\}
\]

is considered. The Marguerre–Airy structural front end, representative halfwaves, corrected reinforcement mapping, and projected work-conjugate bending direction are unchanged.

R01 used a generic SLSQP feasibility maximization over all concrete-block and steel resultants. R02 eliminates those internal-force unknowns analytically and then solves only finite scalar active-set roots. No test load enters any active-set selection or root calculation.

---

## 1. Bounded-resultant allocation theorem

For one direction `j in {x,y}`, let each admissible internal force contribution be `r_k` acting at ordinate `z_k`, with a finite interval

\[
\ell_k\le r_k\le u_k,
\qquad
\sum_k r_k=N_j.
\]

Concrete compression blocks use

\[
[-f_c c_t,0],\qquad[-f_c c_b,0],
\]

at

\[
z_t=h-c_t/2,\qquad z_b=-h+c_b/2,
\]

and each reinforcement layer uses `[0,A_{s,i}f_y]` in the source-faithful R01 tension-only limit model.

Define

\[
L=\sum_k\ell_k,\qquad
\Delta=N_j-L,\qquad
w_k=u_k-\ell_k.
\]

Sort the contributors by descending `z_k` for the maximum positive bending moment. If

\[
W_{m-1}\le\Delta\le W_m,
\qquad
W_m=\sum_{k\le m}w_k,
\]

then the exact force-constrained maximum moment is

\[
\boxed{
M_j^+(N_j)=
\sum_k z_k\ell_k
+\sum_{k<m}z_kw_k
+z_m\bigl(\Delta-W_{m-1}\bigr)
}.
\]

No linear-programming optimizer is required. The minimum moment is obtained by sorting the same finite contributors in ascending `z_k`.

For the single Airy bending DOF,

\[
\boxed{
M_\parallel^+
=d_xM_x^+(N_x)+d_yM_y^+(N_y)
}
\]

and terminal contact is

\[
\boxed{M_\parallel^+(q)=M_\parallel^d(q)}.
\]

Inside each finite allocation cell this expression is at most quadratic in the compression-block depths, because `f_c c` is linear in block depth and the centroid is affine in block depth.

---

## 2. Controlling active families for the eight panels

### 2.1 Cases 4, 5, 6, 8: two reinforcement layers

The exhausting maximum-moment family is

\[
C_x^t=C_y^t=0,
\]

\[
S_x^+=S_y^+=F_s=A_{s,\text{layer}}f_y,
\qquad
S_x^-=S_y^-=0,
\]

\[
C_y^b=-f_cc_b,
\qquad
C_x^b=N_x-F_s.
\]

Longitudinal force equilibrium gives

\[
\boxed{c_b(q)=\frac{F_s-N_y(q)}{f_c}}.
\]

With `z_+=+h_r` and `z_b=-h+c_b/2`,

\[
M_x^u=z_b[N_x(q)-F_s]+z_+F_s,
\]

\[
M_y^u=z_b[-f_cc_b]+z_+F_s.
\]

The ultimate state is therefore the smallest positive admissible root of the single explicit equation

\[
\boxed{
d_xM_x^u(q)+d_yM_y^u(q)
-d_xM_x^d(q)-d_yM_y^d(q)=0.
}
\]

### 2.2 Cases 9 and 23: mid-plane reinforcement

Here `z_s=0`. The exhausting family is

\[
S_x=F_s,\qquad S_y=0,
\]

\[
C_x^t=C_y^t=0,
\qquad
C_y^b=-f_cc_b,
\qquad
C_x^b=N_x-F_s,
\]

and

\[
\boxed{c_b(q)=-\frac{N_y(q)}{f_c}}.
\]

Because the steel is at the middle plane it contributes no bending moment. The same scalar projected-moment equation gives `q_u`.

### 2.3 Case 21: mid-plane reinforcement + interior block-depth optimum

The active family is

\[
S_x=F_s,
\qquad
S_y=N_y+f_cc_b\in(0,F_s),
\]

\[
C_x^t=C_y^t=0,
\qquad
C_x^b=N_x-F_s,
\qquad
C_y^b=-f_cc_b.
\]

The projected resisting moment is

\[
M_\parallel^u
=z_b\left[d_x(N_x-F_s)-d_yf_cc_b\right],
\qquad
z_b=-h+c_b/2.
\]

Because `c_b` is an interior maximizer,

\[
\frac{\partial M_\parallel^u}{\partial c_b}=0,
\]

hence the block depth is explicit:

\[
\boxed{
c_b(q)=h+\frac{d_x[N_x(q)-F_s]}{2d_yf_c}.
}
\]

Substitution into `M_parallel^u=M_parallel^d` again leaves one scalar root in `q`.

### 2.4 Case 14: longitudinal resultant force floor

The governing bound is not a moment contact. With tensile concrete neglected and compression reinforcement not credited, the largest longitudinal compression resultant is

\[
\boxed{N_y^{\min}=-f_ct}.
\]

The exact ultimate amplitude is therefore the root

\[
\boxed{N_y(q_u)+f_ct=0.}
\]

At that root a finite projected-moment feasible witness exists. For example, the symmetric split

\[
c_t=c_b=t/2
\]

makes the longitudinal concrete stress block uniform through the thickness and gives `M_y^u=0`; the exact x-direction bounded-resultant moment interval contains the required projected x-moment. Hence the longitudinal force floor is attainable and is the true active limit for this R01/R02 capacity model.

---

## 3. Corrected active-set-exhausted Swartz8 results

The R01 architecture is retained, but its SLSQP numerical table was not root-exhaustive for Cases 4, 5, 8 and 14. The finite active-set roots supersede that table.

|Case|controlling active family|q_u|P_u / kN|P_f / kN|error|
|---:|---|---:|---:|---:|---:|
|4|2-layer bottom-compression + upper-tension|0.00188032724|568.7986|534.2314|+6.47%|
|5|2-layer bottom-compression + upper-tension|0.00207049300|547.4729|623.6407|-12.21%|
|6|2-layer bottom-compression + upper-tension|0.00266300085|595.0867|691.6985|-13.97%|
|8|2-layer bottom-compression + upper-tension|0.00139148726|516.4777|455.0531|+13.50%|
|9|mid-plane steel / bottom compression|0.00131853739|567.9543|625.8648|-9.25%|
|14|`N_y=-f_ct` force floor|0.00098162126|780.2071|716.1637|+8.94%|
|21|mid-plane steel / interior `c_b` stationary|0.00509993552|304.5437|368.3127|-17.31%|
|23|mid-plane steel / bottom compression|0.00315121327|341.0334|346.9613|-1.71%|

Statistics:

```text
mean signed error = -3.1931 %
MAE               = 10.4209 %
RMSE              = 11.3831 %
```

Therefore:

```text
GENERIC_OPTIMIZER_REQUIRED = NO
FINITE_ACTIVE_SET_ROOTS = YES
R01_SLSQP_NUMERIC_TABLE = SUPERSEDED
RESULTANT_ONLY_ARCHITECTURE = RETAIN_DIAGNOSTIC
```

---

## 4. Controlled uniaxial ablation using the SAME resultant-capacity assumptions

To isolate the user's observation, no material assumption is changed. Concrete tension remains zero; compression reinforcement remains uncredited; the same `f_c`, `f_y`, steel positions, halfwaves and Airy `P(q)` are retained.

The only change is terminal kinematics/equilibrium:

```text
FULL RESULTANT TERMINAL:
    enforce Nx + Ny + M_parallel

UNIAXIAL ABLATION:
    enforce Ny + My only
```

For the uniaxial case the exact positive-moment envelope is obtained by one bottom compression block plus the highest positive-ordinate steel layer. Let `z_+=h_r` for the two-layer panels and `z_+=0` for mid-plane reinforcement. Then

\[
T_y=N_y+f_cc_b,
\]

\[
M_y^+=f_cc_b(h-c_b/2)+z_+T_y,
\]

and the unconstrained optimum is

\[
\boxed{c_b^*=h+z_+.}
\]

The actual `c_b` is this value clipped only by `0<=T_y<=F_s` and `0<=c_b<=t`. The uniaxial ultimate root is `M_y^+(N_y(q))=M_y^d(q)`.

|Case|full resultant P_u / kN|uniaxial-resultant P_u / kN|full minus uniaxial / kN|
|---:|---:|---:|---:|
|4|568.799|595.536|-26.737|
|5|547.473|568.598|-21.125|
|6|595.087|621.074|-25.987|
|8|516.478|521.237|-4.760|
|9|567.954|592.150|-24.196|
|14|780.207|766.430|+13.777|
|21|304.544|408.081|**-103.537**|
|23|341.033|367.811|-26.777|

Uniaxial-resultant statistics:

```text
mean signed error = +3.1777 %
MAE               =  9.2835 %
RMSE              =  9.7233 %
```

Thus the user's observation is confirmed inside one and the same capacity model: hard biaxial resultant enforcement is slightly worse overall than the direct loading-direction resultant constraint, and Case 21 supplies by far the largest penalty.

---

## 5. Why the nominally more complete biaxial model is less accurate

### 5.1 The difference is not caused by a concrete constitutive law

This ablation contains no pointwise concrete stress-strain law at all. Therefore the accuracy loss cannot be blamed on Cedolin–Mulas, CC/TC logic, peak strain, post-peak continuation or thickness integration.

### 5.2 Hard local `N_x` equilibrium consumes a finite transverse force-couple capacity

The Airy solution generates a positive transverse membrane resultant `N_x(q)` together with positive `M_x(q)`. In the current R01/R02 terminal these are treated as hard local capacity demands.

This is particularly restrictive for the mid-plane reinforcement panels. For Case 21,

\[
S_x=F_s,
\qquad
C_x^b=N_x-F_s<0,
\]

and, because `z_s=0`,

\[
\boxed{M_x^u=z_b[N_x-F_s].}
\]

As `q` increases, `N_x(q)` increases. Hence the magnitude `F_s-N_x` of the bottom concrete compression needed to form the transverse couple **decreases**, while the Airy demand

\[
M_x^d=J_xq
\]

increases linearly. The transverse force and transverse moment therefore compete against each other in exactly the same finite force-couple. This creates the early Case-21 root and lowers `P_u` by about 103.5 kN relative to the otherwise identical uniaxial terminal.

For two-layer panels the upper reinforcement has a positive lever arm and can supply part of `M_x` directly, so the penalty is much smaller. Case 14 is the exception: its outer reinforcement and Airy curvature weighting make the x-direction channel helpful, while the actual active limit is the longitudinal force floor `N_y=-f_ct`.

### 5.3 The deeper structural issue: `N_x` is not an externally prescribed load resultant

The experiment is uniaxially loaded. The Airy `N_x` field is a secondary, self-equilibrated compatibility resultant produced by postbuckling geometry; it is not an externally controlled transverse membrane load applied to the panel boundary.

Therefore there is a genuine reduced-order mechanics question:

> Should the terminal section be forced to reproduce the **local Airy value of `N_x` exactly**, or should the transverse membrane channel be treated as an internally redistributable/reaction channel, analogously to the already-corrected `M_perp` reaction of the frozen single bending mode?

The current numerical evidence does not by itself prove that `N_x` must be released. It proves that the hard-equality choice is the source of most of the loss relative to the direct uniaxial constraint, especially for mid-plane reinforcement.

---

## 6. Current decision and next gate

Do **not** revert to a uniaxial material theory merely because its error is smaller. The present finding is instead a generalized-force/work-conjugacy problem.

The next theoretical gate is therefore:

```text
MEMBRANE_TERMINAL_GATE:
    determine the independent membrane generalized deformation(s)
    of the frozen Marguerre-Air y reduced model;
    identify their work-conjugate resultant combination(s);
    classify the orthogonal transverse membrane resultant as
    either HARD_CAPACITY_COORDINATE or INTERNAL_REACTION/REDISTRIBUTABLE_RESULTANT.
```

Only after that variational/work-conjugacy audit should the 8 panels be rerun. No pointwise concrete material model needs to be reopened.
