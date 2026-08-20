# NZ-SCCM — tensile default rule and double-layer steel extension order

Time: 2026-08-20 19:12 +08:00

## 1. New locked tensile-input rule

If a specimen/source does not report concrete tensile strength, use

\[
\boxed{f_t=0.1 f_c}
\]

where `f_c` is the cylindrical compressive strength used by the current concrete operator.

If NC-M4 initial tensile tangent is required to match `E0`, retain

\[
T_4'(0)=1.07515\times0.09=0.0967635,
\]

therefore

\[
\boxed{\varepsilon_{t0}=0.0967635\,f_t/E_0.}
\]

This rule supersedes the previous `ft source blocker` for cases with no reported tensile strength.

## 2. Next extension order

The next executable extension is **reinforcement first**, then steel shell.

Reason:

- reinforcement source law and Case21 steel properties are already source-defined: `Es=200000 MPa`, `eps_y=0.00265`, `fy=530 MPa`, `eps_f=0.04`, with zero post-yield modulus up to failure strain;
- the current locked source does not yet define a steel-shell current law, so shell integration cannot be completed without first freezing that law.

## 3. User-mandated double-layer treatment

Both reinforcement and steel-shell extensions are to be formulated as two through-thickness layers.

For reinforcement, use symmetric levels

\[
\boxed{z_r^{(+)}=+h_r,\qquad z_r^{(-)}=-h_r.}
\]

For a total nominal two-way reinforcement ratio `p`, distribute equally over the two directions and two layers:

\[
\boxed{\rho_{s,x,+}=\rho_{s,x,-}=\rho_{s,y,+}=\rho_{s,y,-}=p/4.}
\]

Equivalently, each direction has total ratio `p/2` and each layer of a given direction has `p/4`.

For Case21 `p=0.75%`, this gives

\[
\boxed{\rho_{s,x,+}=\rho_{s,x,-}=\rho_{s,y,+}=\rho_{s,y,-}=0.001875.}
\]

The original Case21 source has `h_r=0`, i.e. one mid-plane layer. Because the user now mandates a two-layer formulation, numerical double-layer Case21 reinforcement requires an explicit nonzero `h_r` rule/input; until supplied, keep `h_r` symbolic rather than inventing cover.

## 4. Double-layer reinforcement strain fields

With

\[
S=A_0A+\tfrac12A^2,\qquad H=A_0+A,
\]

and `kx=pi/b`, `ky=pi/ell`, for layer sign `s=+1,-1`:

\[
\boxed{
\varepsilon_{sx}^{(s)}=
\varepsilon_m+S k_x^2\cos^2(k_xx)\sin^2(k_yy)
+s h_r A k_x^2\sin(k_xx)\sin(k_yy)
}
\]

\[
\boxed{
\varepsilon_{sy}^{(s)}=
-\Delta/\ell+S k_y^2\sin^2(k_xx)\cos^2(k_yy)
+s h_r A k_y^2\sin(k_xx)\sin(k_yy)
}
\]

and their A-derivatives are

\[
\boxed{
G_{sx}^{(s)}=
H k_x^2\cos^2(k_xx)\sin^2(k_yy)
+s h_r k_x^2\sin(k_xx)\sin(k_yy)
}
\]

\[
\boxed{
G_{sy}^{(s)}=
H k_y^2\sin^2(k_xx)\cos^2(k_yy)
+s h_r k_y^2\sin(k_xx)\sin(k_yy).
}
\]

The double-layer steel current law is

\[
\sigma_s(\varepsilon_s)=
\begin{cases}
E_s\varepsilon_s,& |\varepsilon_s|\le\varepsilon_y,\\
f_y\operatorname{sgn}(\varepsilon_s),&\varepsilon_y<|\varepsilon_s|\le\varepsilon_f.
\end{cases}
\]

No post-failure branch is added.

## 5. Equivalent continuous-area contribution for ratio-only inputs

For a regular isotropic mesh specified only by nominal ratio, represent each direction/layer by an equivalent steel sheet thickness

\[
\boxed{t_{s,d,s}=\rho_{s,d,s}\,h.}
\]

Then

\[
\boxed{
P_s=-\frac1\ell\sum_{s=\pm1}t_{s,y,s}\int_0^b\int_0^\ell\sigma_{sy}^{(s)}\,dy\,dx
}
\]

\[
\boxed{
R_{m,s}=\sum_{s=\pm1}t_{s,x,s}\int_0^b\int_0^\ell\sigma_{sx}^{(s)}\,dy\,dx
}
\]

\[
\boxed{
R_{A,s}=\sum_{s=\pm1}\int_0^b\int_0^\ell
\left[t_{s,x,s}\sigma_{sx}^{(s)}G_{sx}^{(s)}+t_{s,y,s}\sigma_{sy}^{(s)}G_{sy}^{(s)}\right]dy\,dx.
}
\]

Total system becomes

\[
P=P_c+P_s,\qquad R_m=R_{m,c}+R_{m,s},\qquad R_A=R_{A,c}+R_{A,s},
\]

followed by the same same-source three-variable limit determinant.

## 6. Steel shell

Steel shell will use the same two-surface architecture, normally at two prescribed shell centroids `z_sh^+` and `z_sh^-` (for zero-offset thin skins these may be near `+/-h/2`, but no numerical position or constitutive law is assumed here). A shell current law must be source-frozen before formal integration.

Current unique next task: analytically compile the above double-layer reinforcement contribution into `P_s, R_m,s, R_A,s`, add the same-source derivatives, and re-solve Case21 once `h_r` is specified.