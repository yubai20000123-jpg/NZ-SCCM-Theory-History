# NZ-SCCM — canonical Marguerre–Airy UV to always-on Yun bridge source closure R19

**Timestamp:** 2026-08-24 16:12 +08:00  
**Identity:** SOURCE-CLOSED CANONICAL MA-UV → YUN BRIDGE / DIRECT RESIDUAL-JACOBIAN PRE-D15 GATE  
**Calibration to Zhou/FE/test:** NO  
**Comparator used in solve:** NO

## 0. Why R19 exists

R18 correctly fixed the architecture to

\[
\text{Marguerre--Airy deformation}\rightarrow
\varepsilon_s\rightarrow
\text{Yun/Karman}\rightarrow
(\sigma_s,E_{t,s})\rightarrow
(\mathbf R,\mathbf J),
\]

but its executable used a manufactured `B_A^y` and a diagnostic coordinate/scaling form. That derivative test proved the calculus of the bridge scaffold, not the exact project Marguerre--Airy strain adapter.

R19 closes that source gap from the already-frozen project files. It does not change the current material model, activate/deactivate Yun, introduce a new mode, or use any comparator.

## 1. Canonical source recovery

The authoritative explicit UV source is

`semantic_v2/20_theory/20260820_2358__NZSCCM__NGUYEN_KINEMATICS_EXPLICIT_UV_AND_NC_M6_VIRTUAL_WORK_SYSTEM.md`.

It uses

\[
X=\pi x/b,\qquad Y=\pi y/\ell,\qquad k=b/\ell,
\]

\[
w=bq\sin X\sin Y,\qquad w_0=bq_0\sin X\sin Y.
\]

For the loading-direction y-normal strain,

\[
\boxed{
\varepsilon_y
=
-\varepsilon_0D
+\varepsilon_0\alpha A_y
+\pi^2k^2S_qF_y
+\pi^2k^2\frac{q}{b}zH_s
}
\]

with

\[
S_q=q_0q+\frac12q^2,
\]

\[
\boxed{F_y=\sin^2X(1-\sin^2Y)},
\qquad
\boxed{H_s=\sin X\sin Y},
\]

and the previously missing production Airy/in-plane basis

\[
\boxed{
A_y=
\frac{\nu}{4}
-\frac{k^2}{2}\sin^2X
-\frac{\nu}{2}\sin^2Y
+k^2\sin^2X\sin^2Y.
}
\]

With \(\zeta=2z/t_r\),

\[
\boxed{
e_y=\frac{\varepsilon_y}{\varepsilon_0}
=
-D+\alpha A_y
+\frac{\pi^2k^2}{\varepsilon_0}S_qF_y
+\frac{\pi^2t_rk^2}{2\varepsilon_0b}qH_s\zeta.
}
\]

This exactly reduces to the square-panel formula recorded in

`semantic_v2/40_execution/steel_shell/20260818_1421__NZSCCM__Z1_Z4__UNIFIED_YUN_IDEAL_EP_LOCAL_AMPLITUDE_FULL_RECALC.md`

when \(k=1\).

## 2. Exact generalized derivatives

For fixed geometry and material reference strain,

\[
\boxed{\varepsilon_{y,D}=-\varepsilon_0},
\]

\[
\boxed{
\varepsilon_{y,q}
=
\pi^2k^2(q_0+q)F_y
+\frac{\pi^2t_rk^2}{2b}H_s\zeta,
}
\]

\[
\boxed{\varepsilon_{y,\alpha}=\varepsilon_0A_y},
\]

and

\[
\boxed{\varepsilon_{y,qq}=\pi^2k^2F_y}.
\]

All mixed second derivatives among \(D,q,\alpha\) are zero.

These expressions replace the manufactured R18 production placeholder.

## 3. Nested global/local coordinate map

The historical unified Yun file states that the representative face is partitioned into \(b/B_s\) transverse 200-mm strips and that every strip uses a local coordinate \(x_i\) in

\[
\phi_i=
\left(1-\cos\frac{2\pi x_i}{B_s}\right)
\left(1-\cos\frac{2m_i\pi y}{\ell}\right).
\]

The global Marguerre--Airy field must not be reset to \(x=0\) for every strip. R19 therefore makes the two coordinates explicit:

\[
\boxed{x_g=x_{0,i}+x_i,\qquad x_{0,i}=iB_s,\qquad 0\le x_i\le B_s.}
\]

Thus:
- global \(A_y,F_y,H_s,w_{,y}\) are evaluated at \(x_g\);
- local Yun \(\phi_i,\phi_{i,y}\) are evaluated at \(x_i\);
- \(y\) remains the representative-halfwave global coordinate.

For Z1, 30 strips give exact coverage \(0\le x_g\le6000\) mm.  
For Z4, 40 strips give exact coverage \(0\le x_g\le8000\) mm.

This is a geometry-coordinate adapter implied by the contiguous strip partition; it is not a new material or activation rule.

## 4. Current Yun steel strain retained

R19 keeps the 2026-08-18 unified strain exactly:

\[
\boxed{
\varepsilon_s
=
\varepsilon_y^g
+A_i(w_{0,y}^g+\Delta w_{,y}^g)\phi_{i,y}
+A_{0i}\Delta w_{,y}^g\phi_{i,y}
+\left(A_{0i}A_i+\frac12A_i^2\right)\phi_{i,y}^2.
}
\]

For \(\theta=(D,q,\alpha,A_i)\), R19 implements all first and second derivatives analytically, including

\[
\frac{\partial\varepsilon_s}{\partial A_i}
=
(w_{0,y}^g+\Delta w_{,y}^g)\phi_{i,y}
+(A_{0i}+A_i)\phi_{i,y}^2,
\]

\[
\frac{\partial^2\varepsilon_s}{\partial q\,\partial A_i}
=
\frac{\partial\Delta w_{,y}^g}{\partial q}\phi_{i,y},
\qquad
\frac{\partial^2\varepsilon_s}{\partial A_i^2}
=
\phi_{i,y}^2.
\]

The minimal current steel law remains

\[
\sigma_s=\operatorname{clip}(E_s\varepsilon_s,-f_y,+f_y).
\]

No `sigma_cr/f_y` activation switch exists.

## 5. Executed derivative audit

Executable:

`semantic_v2/40_execution/steel_shell/20260824_1612__NZSCCM__CANONICAL_MA_UV_TO_YUN_RESIDUAL_JACOBIAN_R19.py`

Diagnostic result:

```text
R19_CANONICAL_MA_UV_SOURCE = PASS
NESTED_LOCAL_GLOBAL_COORDINATE_MAP = PASS
STRIP_COVERAGE_X0_TO_B = PASS
POINTWISE_FIRST_DERIV_MAX_ABS_ERR = 2.659429e-12
POINTWISE_SECOND_DERIV_MAX_ABS_ERR = 2.140954e-12
DIAGNOSTIC_RA_JAC_MAX_ABS_ERR = 1.653234e-08
DIAGNOSTIC_RA_JAC_MAX_REL_ERR = 8.276635e-10
R19_CANONICAL_MA_TO_YUN_JACOBIAN_AUDIT = PASS
```

The `R_A` Jacobian check uses high-order Gauss-Legendre only as a finite-difference/oracle evaluator after equations are frozen. It is not a formal production integration rule.

Formal counters remain:

```text
FORMAL_SPATIAL_QUADRATURE = 0
THICKNESS_QUADRATURE = 0
MATERIAL_POINTS = 0
```

## 6. Explicit R18 supersession boundary

Retained from R18:
- direct `sigma_s -> residual`;
- direct `Et,s -> consistent Jacobian`;
- current-stress geometric term;
- always-on Yun local amplitude;
- no A/B/D stiffness prerequisite;
- no parameter activation gate.

Superseded in R18:
- manufactured `B_A^y`;
- diagnostic `u=x/b`, `v=y/ell` executable mapping;
- cosine-based report shorthand;
- omitted \(\varepsilon_0\), \(k^2\), and physical bending scaling.

The derivative success in R18 remains a scaffold calculus check; R19 is the first source-closed canonical MA-UV/Yun adapter.

## 7. D15 gate now opened

The upstream geometric blocker is closed. The next production gate is no longer “find \(B_A^y\)”; it is:

```text
NEXT_TASK =
D15_COMPILE_CANONICAL_DIRECT_YUN_STEEL_RESIDUAL_JACOBIAN
+ Z1_Z4_HISTORICAL_REGRESSION
+ Z0_Z6_RERUN
+ UHPC_ADAPTER_RERUN
```

The exact Yun Ch.2 finite-harmonic audit already proves that its elastic Airy/Galerkin side is D15-compatible. The remaining work is to compile the composed current ideal-EP steel terms without giving numerical quadrature formal theoretical identity.

No new \(P_u\) is claimed in R19.
