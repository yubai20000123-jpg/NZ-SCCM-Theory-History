# NZ-SCCM R03 — Saddle-like geometry, matrix functions, special functions, and stable exact kernels

## Scope
This note records external mathematical research used only to interpret and extend the existing G18/G20/G27 current-map + D15 mainline. It does not authorize a route switch.

## 1. Is the current stress surface a saddle surface?
R03 directly computed the Hessian determinant of the current reference principal surface `s1(lambda1,lambda2)` on a material-coordinate rectangle. About 30.6% of the inspected interior points had `det(H)<0`, so there are substantial locally saddle-like regions. However, the same surface also contains mostly convex-like regions and small concave-like regions. It is therefore not a single global hyperbolic paraboloid.

Conclusion: the visual resemblance to a saddle is geometrically meaningful locally, but it is not by itself an integration theorem.

## 2. Stronger result than “saddle-like”: exact separability
The source-shaped reference map already has an exact separated form:

```text
s_plus = U(lambda_plus)
         - a_cc C(lambda_plus)^2 C(lambda_minus)
         + C(lambda_plus) T(lambda_minus)
         - rho a_t T(lambda_plus) T(lambda_minus)^8
```

with the symmetric expression for `s_minus`.

Hence each principal stress surface has separated rank <=4 exactly. The numerical SVD is only a confirmation; generic 2D surface fitting is unnecessary for this reference architecture.

This is the most important dimensional-reduction result of R03.

## 3. 2x2 matrix-function representation
For a symmetric 2x2 equivalent-uniaxial tensor

```text
X = mu I + Y,     Y^2 = r_s^2 I
```

any scalar matrix function can be written

```text
f(X) = f_e(mu,r_s) I + f_o(mu,r_s) Y
```

where

```text
f_e = [f(mu+r_s)+f(mu-r_s)]/2
f_o = [f(mu+r_s)-f(mu-r_s)]/(2 r_s)
f_o -> f'(mu) as r_s -> 0
```

This is the natural coalescence-safe divided-difference/Cayley-Hamilton representation. It removes any need to introduce a material state switch when two principal values approach each other.

Primary references:
- N. J. Higham, “Functions of Matrices,” Handbook of Linear Algebra, 2014.
- N. J. Higham and A. H. Al-Mohy, “Computing Matrix Functions,” Acta Numerica 19 (2010), 159–208.

## 4. Appell F1 exact master integral already matches an NZ-SCCM kernel class
For

```text
D(X,Y)=a+b sin^2 X+c sin^2 Y+d sin^2 X sin^2 Y
```

the whole-domain integral is

```text
M(a,b,c,d)
= pi^2 / sqrt[a(a+b)]
  F1(1/2;1/2,1/2;1; -c/a, -(c+d)/(a+b)).
```

R03 evaluated a representative case by the named Appell F1 expression and compared it with an audit-only high-order quadrature:

```text
relative difference = 1.88e-15
formal spatial quadrature count = 0
```

NIST DLMF §16.15 gives the Euler integral representation of Appell F1.

## 5. Carlson symmetric elliptic integrals
After one trigonometric integration, many kernels with products of two quadratic factors under a square root are complete elliptic integrals. NIST DLMF Chapter 19 gives their reduction to Carlson symmetric integrals `RF`, `RD`, `RJ` and describes the duplication algorithm. In the duplication method, variable differences are repeatedly reduced by factors of four, followed by evaluation of a fixed polynomial expansion.

This makes Carlson functions attractive as a stable numerical backend for a named exact kernel, provided the NZ-SCCM reduced denominator actually falls into the elliptic class.

Primary source:
- NIST DLMF §§19.15, 19.23, 19.29, 19.36.

## 6. Low-rank bivariate representation
Townsend and Trefethen, “An Extension of Chebfun to Two Dimensions,” SIAM J. Sci. Comput. 35 (2013), C495–C518, DOI `10.1137/130908002`, demonstrate efficient low-rank separated representation of smooth bivariate functions.

NZ-SCCM does **not** import Chebfun2 adaptive sampling/collocation as a production operator. Its relevance is conceptual: separated low-rank structure is a standard route for compressing smooth bivariate functions. In the current source-shaped map we have a stronger result: separated rank <=4 is exact by algebra.

## 7. Zolotarev / rational approximation
Zolotarev rational functions are designed for approximation on separated sets. This is relevant after R03 proves separated principal spectra in a certified D-q envelope.

However, NZ-SCCM has already learned that a good rational material approximation can create difficult resolvent denominators and Picard-Fuchs complexity after structural composition. Therefore Zolotarev/AAA-type rational approximation is not promoted as production by itself. It may be reconsidered only if its poles reduce to direct Appell/Carlson or comparably small named kernels.

Primary references:
- L. N. Trefethen and H. D. Wilber, “Computation of Zolotarev rational functions,” SIAM J. Sci. Comput. 47 (2025), A2205–A2220.
- D. Huybrechs and L. N. Trefethen, “Sigmoid Functions, Multiscale Resolution of Singularities, and hp-Mesh Refinement,” SIAM Review 66 (2024), 683–693, DOI `10.1137/23M1556629`.

The latter paper is directly relevant to the R01/R02 observation that very narrow smooth sigmoid-like transitions can create multiscale approximation pressure.

## 8. R03 mathematical priority
The order of attack is now:

1. exploit exact rank-4 principal-coordinate separability;
2. certify reachable `lambda+` / `lambda-` intervals from the structural D-q envelope;
3. compile only the required one-dimensional primitives on those intervals;
4. use the coalescence-safe 2x2 matrix-function form when needed;
5. identify whether the resulting structural moments fall into Beta/Appell/Carlson named-kernel families;
6. only if these fail, consider another representation.

Do not infer an integration method solely from the visual saddle shape.