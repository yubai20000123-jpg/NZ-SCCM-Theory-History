# NZ-SCCM Case21 SageMath/FriCAS zero-spatial-sampling analytic execution result

**Date:** 2026-08-09  
**Task:** frozen ordinary-concrete current operator → exact tangent-half-angle algebraic integrands → Sage/FriCAS direct integration → concrete-only Case21 → reinforced Case21  
**Priority:** theory MD > helper Python > previous multi-backend report.

## Executive status

The frozen theory contract was read and reproduced exactly, the tangent-half-angle transformation was carried out symbolically, and the two **actual continuous structural integrands** were generated as exact algebraic expressions with **zero spatial sampling**.

However, this container does not contain SageMath or FriCAS and cannot acquire them: outbound DNS/network access is blocked, package indexes cannot be refreshed, and archive acquisition through the available download bridge is not usable for the release binary. Symbolica/Rubi and python-flint/Arb are blocked by the same environment constraints. The installed SymPy 1.14.0 was actually tried on the first exact algebraic integration stage and returned no primitive before the enforced timeouts.

Therefore the current-run status is:

```text
CONTRACT_CHECK                                  = PASS
EXACT_TANGENT_HALF_ANGLE_TRANSFORMATION         = PASS
EXACT_fP_alg_AND_fR_alg_BUILT                   = PASS
N_formal_spatial_sampling                       = 0
N_formal_spatial_quadrature                     = 0
SAGE_EXECUTED                                   = NO (runtime unavailable)
FRICAS_EXECUTED                                 = NO (runtime unavailable)
SYMPY_EXACT_FIRST_STAGE_ATTEMPTED               = YES, timeout
ZERO_SPATIAL_Pc(D,q)                            = NOT YET OBTAINED
ZERO_SPATIAL_Rq,c(D,q)                          = NOT YET OBTAINED
CONCRETE_ONLY_ROOT_RECOMPUTED_THIS_RUN          = NO
RC_ROOT_RECOMPUTED_THIS_RUN                     = NO
FINAL_STATUS                                    = DIRECT_CAS_EXECUTION_BLOCKED_BY_RUNTIME_TOOL_INSTALLATION
```

The previous `338.3184 kN` concrete-only and `342.3339 kN` RC values are retained **only as later verification targets**. They are not promoted to new formal results in this report.

---

# A. Theory contract

The frozen MD requires the complete ordinary-concrete current map and explicitly excludes the later exploratory `tanh` tension smoothing. The helper Python agrees with the MD for the material operator and reinforcement law.

The formal tension smoothing retained here is

\[
H(r,r_0)=
\frac12\left[(r-r_0)+\sqrt{(r-r_0)^2+0.05^2}\right]
-
\frac12\left[-r_0+\sqrt{r_0^2+0.05^2}\right].
\]

The implementation chain retained without substitution by a surrogate is

\[
(\varepsilon_x,\varepsilon_y,\gamma_{xy})
\to (X_{11},X_{22},X_{12})
\to (\lambda_+,\lambda_-)
\to (c_\pm,t_\pm)
\to (C_\pm,T_\pm,U_\pm)
\to (s_+,s_-)
\to (\sigma_x,\sigma_y,\tau_{xy}).
\]

Automated contract checks are stored in `contract_check.json`; all frozen-law checks passed.

Input SHA-256 values:

```text
MD      98483fa75e828f57916b06fc708fc35fc7960fabbdebf4edb3e04aba10061bc6
Python  740e8862b1f428e66c779ea17c2ffefdec1f53ae7da5b98f9d85669ea24811c2
Prior   e19b8dbc2c4c1835ed2ce36d8e9d027c3d6fd7e6aed2b4d9eaabcfa83cf5c55f
```

---

# B. Exact Case21 kinematics used

Case21 constants used in the generated CAS task are

\[
f_c=21.23\ \mathrm{MPa},\quad E_0=20321\ \mathrm{MPa},\quad
\varepsilon_0=0.00209,\quad \nu=0.18,
\]

\[
b=\ell=1220\ \mathrm{mm},\qquad t=19.30\ \mathrm{mm},\qquad
q_0=\frac1{400}.
\]

With

\[
C_m=\frac{\pi^2}{\varepsilon_0}\left(q_0q+\frac12q^2\right),\qquad
C_b=\frac{\pi^2}{2\varepsilon_0}\frac tb q,
\]

the frozen continuous strain field is

\[
e_x=\nu D+C_m\cos^2X\sin^2Y+C_b\sin X\sin Y\,\zeta,
\]

\[
e_y=-D+C_m\sin^2X\cos^2Y+C_b\sin X\sin Y\,\zeta,
\]

\[
g_{xy}=2C_m\sin X\cos X\sin Y\cos Y-2C_b\cos X\cos Y\,\zeta,
\]

\[
\varepsilon_x=\varepsilon_0e_x,\quad
\varepsilon_y=\varepsilon_0e_y,\quad
\gamma_{xy}=\varepsilon_0g_{xy}.
\]

The amplitude derivatives are also retained exactly in the supplied source.

---

# C. Tangent-half-angle transformation

Define

\[
u=\tan\frac X2,\qquad v=\tan\frac Y2,
\]

so for the physical interval \(X,Y\in[0,\pi]\),

\[
u,v\in[0,+\infty).
\]

Exactly,

\[
\sin X=\frac{2u}{1+u^2},\qquad
\cos X=\frac{1-u^2}{1+u^2},
\]

\[
\sin Y=\frac{2v}{1+v^2},\qquad
\cos Y=\frac{1-v^2}{1+v^2},
\]

and

\[
dX\,dY=\frac{4\,du\,dv}{(1+u^2)(1+v^2)}.
\]

The Jacobian is denoted

\[
J_{uv}=\frac{4}{(1+u^2)(1+v^2)}.
\]

After this substitution the exact formal integrands are

\[
f_{P,\mathrm{alg}}(u,v,\zeta;D,q)=\sigma_y\,J_{uv},
\]

\[
f_{R,\mathrm{alg}}(u,v,\zeta;D,q)
=\left(\sigma_x e_{x,q}+\sigma_y e_{y,q}+\tau_{xy}g_{xy,q}\right)J_{uv}.
\]

No trigonometric, exponential, logarithmic, or Piecewise object remains in either expression. The only non-integer powers are \(\pm1/2\) from algebraic radicals and the fixed algebraic constant \(2^{7/8}\). This was checked symbolically in `algebraic_identity_check.json`.

Expression statistics:

| expression | constructed `count_ops` | textual length | sqrt occurrences | unique sqrt subexpressions |
|---|---:|---:|---:|---:|
| \(f_{P,alg}\) | 58,452 | 238,859 | 559 | 11 |
| \(f_{R,alg}\) | 146,231 | 597,296 | 1,397 | 11 |

The full exact expressions are stored verbatim in:

- `fP_alg_sympy.txt`
- `fR_alg_sympy.txt`
- `stress_sigma_x_alg_sympy.txt`
- `stress_sigma_y_alg_sympy.txt`
- `stress_tau_xy_alg_sympy.txt`

Their hashes are listed in `generated_file_hashes.sha256`.

---

# D. Why the first integration variable is zeta

The order

```text
zeta -> u -> v
```

was selected by exact symbolic degree inspection, not by spatial sampling.

Before composition with the outer material radicals:

- \(\mu\) is affine in \(\zeta\);
- \(\delta\) is independent of \(\zeta\) for this Case21 field;
- \(X_{12}\) is affine in \(\zeta\);
- therefore \(r_X^2=\delta^2+X_{12}^2\) is exactly quadratic in \(\zeta\).

The exact check is stored in `algebraic_structure.json`. In contrast, \(u\) and \(v\) already enter through the tangent-half-angle rational denominators. Hence \(\zeta\) is the natural first variable for FriCAS's algebraic integrator.

No trial nodes, collocation, or sampled degree estimate was used.

---

# E. Formal integrals after transformation

The required zero-spatial-sampling concrete functions are

\[
P_c(D,q)=
-\frac{bt}{2\pi^2}
\int_0^\infty\int_0^\infty\int_{-1}^{1}
 f_{P,alg}(u,v,\zeta;D,q)
\,d\zeta\,dv\,du,
\]

\[
R_{q,c}(D,q)=
\frac{\varepsilon_0b\ell t}{2\pi^2}
\int_0^\infty\int_0^\infty\int_{-1}^{1}
 f_{R,alg}(u,v,\zeta;D,q)
\,d\zeta\,dv\,du.
\]

The first concrete CAS targets are therefore, specifically,

\[
\boxed{
I_{P,z}(D,q,u,v)=\int_{-1}^{1}f_{P,alg}(u,v,\zeta;D,q)\,d\zeta
}
\]

and

\[
\boxed{
I_{R,z}(D,q,u,v)=\int_{-1}^{1}f_{R,alg}(u,v,\zeta;D,q)\,d\zeta.
}
\]

These are the precise unresolved mathematical objects in the current runtime. The failure statement is **not** “the material law is too complex.”

---

# F. CAS installation and backend audit

See `TOOL_INSTALLATION_RECORD.md`, `tool_environment_probe.log`, and `backend_audit_current_runtime.json` for full records.

## F.1 SageMath

Not present. The official conda-forge bootstrap route was attempted, but the runtime cannot resolve `github.com`. No conda/mamba executable is preinstalled. The present apt cache has no SageMath candidate and `apt-get update` cannot reach Debian mirrors.

**Outcome:** not executable in this container.

## F.2 FriCAS

Not present. FriCAS 1.3.13's official amd64 binary route was attempted directly and through SourceForge. Direct container networking cannot resolve GitHub; the alternate download bridge could reach the SourceForge landing page but could not transfer the binary archive into the container. Source compilation is not possible here because no supported Common Lisp implementation is installed and external acquisition is blocked.

**Outcome:** the primary requested algebraic backend was not mathematically tried because it could not be installed/started. This is an environment block, not a FriCAS integration failure.

A complete direct FriCAS input has nevertheless been generated as `case21_fricas.input`.

## F.3 Giac / Maxima

Neither executable is present. Package installation is blocked by the unavailable package indexes/network.

**Outcome:** not executable in this container.

## F.4 SymPy 1.14.0 — actually executed

SymPy is installed and was applied directly to the exact transformed algebraic functions with \(D,q,u,v\) symbolic.

For \(I_{P,z}\):

1. `integrate(fP_alg, z, risch=True)` — no return within 90 s;
2. `integrate(fP_alg, z)` — no return within 60 s.

For \(I_{R,z}\):

1. `integrate(fR_alg, z)` — no return within 60 s.

No primitive file was produced, so derivative verification was impossible.

Logs:

- `sympy_z_attempt_risch.log`
- `sympy_z_attempt_normal.log`
- `sympy_z_attempt_fR.log`

This is a backend timeout only; it is not promoted to an impossibility proof for the algebraic integral.

## F.5 Symbolica-integrate / Rubi

The official repository was located and its `integrate_with_steps` capability was checked. This runtime has neither Rust nor Cargo. A clone attempt failed because the runtime cannot resolve GitHub.

**Outcome:** no Symbolica integration or Rubi step trace was generated, and none is fabricated. `symbolica_execution_NOT_AVAILABLE.log` records this explicitly.

## F.6 python-flint / Arb

Installation was attempted using both the configured Python index and the public route. `python-flint` remains unavailable.

**Outcome:** no Arb certificate can be generated in this container; `arb_certificate_NOT_AVAILABLE.log` records this.

---

# G. Prepared SageMath/FriCAS execution sources

Because the requested tools cannot be installed here, a full external direct-CAS task package has been generated rather than reverting to spatial collocation.

## G.1 `case21_zero_spatial_analytic.sage`

This source:

1. reconstructs the frozen material operator and Case21 kinematics directly;
2. performs the tangent-half-angle substitution exactly;
3. tries each primitive in the required order:
   - FriCAS;
   - Giac;
   - Maxima;
   - SymPy;
4. records the input, primitive, return type, elapsed time, and derivative check;
5. **accepts a primitive only if**
   \[
   \mathrm{simplify}(dF/dx-f)=0;
   \]
6. substitutes finite endpoints or evaluates exact limits at \(+\infty\);
7. continues \(\zeta\to u\to v\) only after the preceding primitive is verified;
8. constructs \(P_c(D,q)\) and \(R_{q,c}(D,q)\);
9. only then forms the stationary equations and searches a broad family of parameter-space roots.

The broad root multistart is in \((D,q)\)-parameter space and is not a spatial integration discretization. The old `338.3184/342.3339 kN` values do not appear as equations or calibration targets.

## G.2 `case21_fricas.input`

This is a standalone FriCAS input of the same exact operator. It requests:

```text
FPz := integrate(fPalg,zz)
verifyPz := simplify(D(FPz,zz)-fPalg)
IPz := eval(FPz,zz=1)-eval(FPz,zz=-1)
```

followed by the analogous \(u\), \(v\), and residual chain. The direct transcript can therefore preserve FriCAS's returned algebraic/elliptic/special-function objects without manually decomposing them.

## G.3 `run_external_sage_fricas.sh`

Runs both the Sage-driven and standalone FriCAS paths and saves full console transcripts.

---

# H. Branch treatment required in the direct CAS run

Physical domain:

\[
D>0,\qquad q>0,\qquad u,v\in[0,+\infty),\qquad \zeta\in[-1,1].
\]

All square roots in the frozen current law are principal nonnegative real roots on real arguments of the form \(a^2+b^2\) or \(w^2+\eta^2\). The spectral map uses the generic \(r_X>0\) formula; the MD prescribes its continuous limit at \(r_X=0\). Thus isolated \(r_X=0\) locations do not create a stress jump.

If FriCAS returns logarithms, inverse trigonometric functions, elliptic functions, `RootOf`, or another standard object, the expression should be retained at that level. The audit condition is the derivative identity plus real endpoint/limit treatment; the term is not to be manually decomposed further.

---

# I. Strict error certificate

There is no sampled polynomial or truncated spatial representation in the new formal task package. Therefore, **if** FriCAS/Sage returns derivative-verified exact primitives and exact endpoint expressions, there is no spatial interpolation/truncation remainder to certify.

A ball-arithmetic certificate would then be used only for numerical evaluation of the final algebraic/special-function expression and root residuals. Arb could not be installed in the current container, so no such certificate is claimed here.

---

# J. Reinforcement — exact closed form already ready

The frozen Case21 reinforcement mapping is

\[
\rho_{s,x}=\rho_{s,y}=0.00375,\qquad z_s=0,
\]

with

\[
E_s=200000\ \mathrm{MPa},\qquad \varepsilon_y=0.00265,
\qquad f_y=530\ \mathrm{MPa}.
\]

On the previously observed reachable RC limit branch, all steel strains were below yield. That earlier observation remains a **verification item** to be rechecked after the new concrete root is obtained. Under the elastic-range condition, the exact steel functions embedded in the supplied Sage/FriCAS source are

\[
\boxed{
P_s(D,q)=
\rho_{s,y}tbE_s\varepsilon_0
\left(D-\frac{C_m}{4}\right)
}
\]

(in N before reporting conversion to kN), and, with

\[
S=q_0q+\frac12q^2,
\]

\[
\boxed{
R_{q,s}(D,q)=
\rho_s tE_s\pi^2(q_0+q)b\ell
\left[
\frac{\varepsilon_0D(\nu-1)}4
+\frac{9\pi^2S}{32}
\right].
}
\]

No steel quadrature or steel expansion is used.

---

# K. Concrete-only root status

The required equations are

\[
R_{q,c}(D,q)=0,
\]

\[
L_c=P_{c,D}R_{q,c,q}-P_{c,q}R_{q,c,D}=0.
\]

Because the current runtime did **not** obtain zero-spatial-sampling \(P_c(D,q)\) and \(R_{q,c}(D,q)\), it would be methodologically invalid to quote the previous collocation-based `338.318379 kN` as a newly solved direct-CAS result.

Hence:

```text
D_u,c     = NOT RECOMPUTED IN THIS RUNTIME
q_u,c     = NOT RECOMPUTED IN THIS RUNTIME
A_u,c     = NOT RECOMPUTED IN THIS RUNTIME
P_u,c     = NOT RECOMPUTED IN THIS RUNTIME
```

Verification targets reserved for a successful external CAS run:

```text
previous direct-candidate target: ~338.3184 kN
historical formal-D15 target:     ~339.1 kN
```

Neither target is used to choose a root or tune the law.

---

# L. RC root status

After a true direct-CAS concrete evaluator exists, the total system is

\[
P=P_c+P_s,
\qquad
R_q=R_{q,c}+R_{q,s},
\]

and

\[
R_q=0,
\qquad
P_{,D}R_{q,q}-P_{,q}R_{q,D}=0.
\]

The RC root is therefore also not recomputed in this container.

Verification target reserved for the external CAS run:

```text
previous reference target: ~342.3339 kN
experiment:                368.312750 kN
```

The previous reference corresponds to about `-7.05%` relative to the experiment, but this number is not relabeled as a new Sage/FriCAS result.

---

# M. Formal-vs-reference distinction

## FORMAL_ZERO_SPATIAL_CAS in this package

```text
frozen explicit kinematics
-> frozen explicit algebraic M_NC
-> exact tangent-half-angle substitution
-> exact algebraic fP_alg/fR_alg
-> CAS primitive + derivative verification
-> exact endpoints/limits
-> Pc(D,q), Rq,c(D,q)
-> stationary root equations
```

Formal spatial counts in the sources generated this run:

```text
Gauss points                    = 0
Simpson points                  = 0
adaptive quadrature points      = 0
Chebyshev-Lobatto spatial nodes = 0
DCT spatial samples             = 0
collocation points              = 0
material-point grid             = 0
N_formal_spatial_sampling       = 0
```

## REFERENCE_ONLY

The prior report's collocation-derived values remain audit targets only. No values from that report were used to construct `fP_alg`, `fR_alg`, integration coefficients, or CAS expressions.

---

# N. Exact unresolved item

The unresolved item is not an undefined constitutive law and not a compiler problem. It is the inability of the **current runtime** to execute the CAS best suited to the following actual algebraic primitives:

\[
\boxed{
\int f_{P,alg}(D,q,u,v,\zeta)\,d\zeta
}
\]

and

\[
\boxed{
\int f_{R,alg}(D,q,u,v,\zeta)\,d\zeta.
}
\]

Current concrete evidence:

- exact algebraic expressions were built;
- \(f_P\) has about 58k symbolic operations and 11 distinct square-root subexpressions;
- \(f_R\) has about 146k symbolic operations and the same 11 distinct square-root subexpressions;
- SymPy 1.14.0 did not return the first \(\zeta\) primitive within 60–90 s;
- FriCAS, Sage, Giac, Maxima, Symbolica, and Arb could not be installed/start due the runtime environment.

Therefore the correct present label is

\[
\boxed{\texttt{DIRECT\_CAS\_EXECUTION\_BLOCKED\_BY\_RUNTIME\_TOOL\_INSTALLATION}}
\]

—not `M_NC_TOO_COMPLEX`, and not a claim that FriCAS cannot integrate the function.

---

# Files produced

Core:

- `NZ_SCCM_CASE21_SAGE_FRICAS_ZERO_SPATIAL_ANALYTIC_RESULT.md`
- `case21_zero_spatial_analytic.sage`
- `case21_fricas.input`
- `run_external_sage_fricas.sh`
- `README_EXTERNAL_EXECUTION.md`

Exact expressions:

- `fP_alg_sympy.txt`
- `fR_alg_sympy.txt`
- `stress_sigma_x_alg_sympy.txt`
- `stress_sigma_y_alg_sympy.txt`
- `stress_tau_xy_alg_sympy.txt`
- `exact_integrand_manifest.json`
- `algebraic_identity_check.json`
- `algebraic_structure.json`

Audit/install logs:

- `TOOL_INSTALLATION_RECORD.md`
- `backend_audit_current_runtime.json`
- `tool_environment_probe.log`
- `sage_miniforge_install_attempt.log`
- `fricas_binary_install_attempt.log`
- `symbolica_install_attempt.log`
- `python_flint_install.log`
- `python_flint_public_install.log`
- `sympy_z_attempt_risch.log`
- `sympy_z_attempt_normal.log`
- `sympy_z_attempt_fR.log`
- `fricas_execution_NOT_AVAILABLE.log`
- `symbolica_execution_NOT_AVAILABLE.log`
- `arb_certificate_NOT_AVAILABLE.log`
