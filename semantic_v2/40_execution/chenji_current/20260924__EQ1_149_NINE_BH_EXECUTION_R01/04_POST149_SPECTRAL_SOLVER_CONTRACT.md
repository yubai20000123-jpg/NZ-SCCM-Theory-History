# Post-Eq.(149) solver contract

No reduction is introduced before Eq.(149).

After Eq.(149), the continuous fields may be represented spectrally to close the nonlinear BVP without x/y/z physical-point discretization.

Chosen execution backend once the C1 tensile gate is complete:

1. Expand only after Eq.(149): Phi with uniform axial-load term plus Fourier field; eps_x^0/eps_y^0 with cosine fields; gamma_xy^0 with sine fields.
2. Retain all harmonics required by the global mode and locked steel-local N=m=4 mode; increase order for convergence.
3. UHPC thickness integration uses the signed-C1 analytic primitives C0,C1,T0,T1,H0; no z Gauss points.
4. Steel thickness integration uses affine-in-zeta strain/stress, quadratic Mises^2, exact quadratic yield crossings, and analytic interval primitives; no zeta points.
5. Spatial nonlinear scalar maps are compiled only in material-coordinate Chebyshev polynomials and lifted into finite Fourier algebra. Compiler nodes are not x/y material points.
6. All area integrals and Galerkin moments are exact trigonometric moments/convolutions. No x/y Gauss grid.
7. Solve Eq.(28),(89)–(91),(109),(114),(119),(123), Eq.(128)–(143), and Eq.(147) simultaneously; Eq.(149) checks d2P/dDelta2<0.
8. Multi-start enumerates stationary roots; connected-branch status is audited separately.
