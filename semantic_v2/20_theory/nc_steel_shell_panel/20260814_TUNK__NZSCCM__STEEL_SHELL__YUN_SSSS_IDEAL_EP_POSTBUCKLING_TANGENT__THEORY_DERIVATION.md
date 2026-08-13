# NZ-SCCM — four-edge SSSS steel-shell Yun/Karman postbuckling tangent

Date: 2026-08-14
Status: PROJECT-DERIVED SSSS DEGENERATION / THEORY SUPPORT / NO STRUCTURAL CALIBRATION

This file does not claim that Yun Lu printed the following SSSS formulas verbatim. It applies the same Karman large-deflection + Airy stress-function + Galerkin machinery to one four-edge simply-supported complete local halfwave so that the current steel-shell extension can be checked against a four-edge SSSS benchmark.

## 1. One complete local halfwave

Let

\[
w_0=A_0\sin\alpha x\sin\beta y,
\qquad
w=(A_0+A)\sin\alpha x\sin\beta y,
\]

\[
\alpha=\pi/b_s,\qquad \beta=\pi/\ell_s,\qquad r=\ell_s/b_s.
\]

The local halfwave is selected from the theoretical energy minimum; observed experimental bulge shape is not an input.

## 2. Elastic local-buckling gate

For a SSSS plate under axial compression,

\[
\boxed{k_{cr}^{SSSS}(r)=\frac{(r^2+1)^2}{r^2}=r^2+2+r^{-2}}
\]

and

\[
\boxed{
\sigma_{cr,s}^{E}
=k_{cr}^{SSSS}(r)
\frac{\pi^2E_s}{12(1-\nu_s^2)}
\left(\frac{t_s}{b_s}\right)^2
}.
\]

The theoretical minimum is at `r=1`, giving `k_cr=4`.

## 3. Karman compatibility and membrane field

For the sine halfwave,

\[
w_{,xx}w_{,yy}-w_{,xy}^2
=-\frac{W^2\alpha^2\beta^2}{2}
(\cos2\alpha x+\cos2\beta y).
\]

Using the incremental amplitude combination

\[
\Delta W^2=2A_0A+A^2,
\]

a compatible Airy perturbation can be written as

\[
F_1=
\frac{E_st_s\Delta W^2}{32}
\left[
\frac{\beta^2}{\alpha^2}\cos2\alpha x
+
\frac{\alpha^2}{\beta^2}\cos2\beta y
\right].
\]

Galerkin projection then gives the one-wave average axial-stress relation

\[
\boxed{
\bar\sigma_y(A)=
\sigma_{cr,s}^{E}(r)\frac{A}{A+A_0}
+
\frac{E_s\pi^2}{16b_s^2}(r^2+r^{-2})(2A_0A+A^2)
}.
\]

In Yun-type coefficient notation the SSSS membrane coefficient is

\[
\boxed{k_p^{SSSS}(r)=\frac34(r^2+r^{-2})}.
\]

At `r=1`, `k_p=1.5`.

## 4. Average axial strain and postbuckling tangent

The average axial strain associated with the same one-wave field is

\[
\boxed{
\bar\varepsilon_y(A)=
\frac{\bar\sigma_y(A)}{E_s}
+
\frac{\beta^2}{8}(2A_0A+A^2)
}.
\]

Therefore the elastic postbuckling effective tangent is obtained from the same branch:

\[
\boxed{
E_{post}^{Yun}(A)
=
\frac{d\bar\sigma_y/dA}{d\bar\varepsilon_y/dA}
}.
\]

It is not an empirical reduction factor.

For a perfect-plate bifurcation limit `A0 -> 0+`, the relation becomes especially transparent. At `r=1`,

\[
\bar\sigma_y
=
\sigma_{cr,s}^{E}
+
\frac{E_s\pi^2A^2}{8b_s^2},
\]

\[
\bar\varepsilon_y
=
\frac{\bar\sigma_y}{E_s}
+
\frac{\pi^2A^2}{8b_s^2},
\]

hence

\[
\boxed{
\bar\sigma_y
=
\frac{E_s\bar\varepsilon_y+\sigma_{cr,s}^{E}}{2}
},
\qquad
\boxed{E_{post}^{Yun}=E_s/2}.
\]

For a general perfect one-wave aspect ratio,

\[
\boxed{
\frac{E_{post}^{Yun}}{E_s}
=
\frac{r^4+1}{r^4+3}
}.
\]

## 5. Ideal-EP event rule

The governing effective tangent is

```text
elastic + unbuckled:        Es
elastic + Yun postbuckled:  d sigma_Yun / d epsilon_Yun
yield surface + plastic loading: 0
unloading below fy:
    local mode inactive -> Es
    local mode active   -> current elastic Yun postbuckling tangent
```

No strain hardening is allowed.

For an elastic-buckling-first plate the event chain is

\[
\boxed{B_s\rightarrow S1_{Yun}\rightarrow Y_s}.
\]

`B_s` is defined by `sigma = sigma_cr,E`; `Y_s` is defined by `|sigma|=fy` on the S1 branch.

## 6. Coupling to the parent D,q system

The local amplitude is an internal finite coordinate, not a prescribed empirical function:

\[
R_A(D,q,A)=0.
\]

Together with the global residual,

\[
R_q(D,q,A)=0.
\]

When `R_A,A != 0`, exact implicit condensation gives

\[
A_D=-R_{A,D}/R_{A,A},\qquad
A_q=-R_{A,q}/R_{A,A}.
\]

All load and residual derivatives entering the limit condition use these condensed derivatives. The same-branch current tangent after local-mode activation uses

\[
\boxed{K_{gg}^{cond}=K_{gg}-K_{gA}K_{AA}^{-1}K_{Ag}}.
\]

No spatial Gauss/Simpson/adaptive quadrature or material-point grid is introduced.
