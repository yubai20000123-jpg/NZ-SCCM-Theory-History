# NZ-SCCM — Z6(a=24000) / Case21 human-calculability full-chain audit

**Timestamp:** 2026-08-17 15:51 +08:00  
**Status:** DOCUMENTATION/AUDIT ONLY — no new Pu released

## Audit standard requested by the user

The calculation chain must expose every governing equation/operator actually used. It is acceptable to omit repetitive arithmetic or the step-by-step solution of a displayed high-degree algebraic/nonlinear equation, but it is not acceptable to omit the equation itself and jump directly to its root/result.

Accordingly this audit distinguishes:

- `EXPLICIT/HAND-AUDITABLE`: governing formula and required intermediate objects are exposed;
- `FORMALLY DEFINED BUT NOT YET FULLY EXPANDED`: the object is mathematically defined, but the current artifacts still omit a seed polynomial/coefficient stream, yield-front equation, or standalone limit evaluator needed for an independent hand reproduction;
- `NUMERICAL LOCALIZATION ONLY`: a raw-R10 continuum oracle was used only to locate/check the same exact limit function after formal equality had been established.

Formal structural counters remain zero-spatial-quadrature.

---

## Common finite kinematics

With `X=pi x/b`, `Y=pi y/ell`, `u=sin X`, `v=sin Y`, `zeta=2z/t`, and square representative halfwave `b=ell`, define

`M = pi^2/eps0 (q0 q + q^2/2)`,

`B = pi^2 t/(2 eps0 b) q`,

`alpha = lambda_A M`.

For `nu=0.18`, the constrained square-halfwave Airy functions are

`Aex = -1/4 -(nu/2)u^2 -(1/2)v^2 + u^2 v^2`,

`Aey = nu/4 -(nu/2)v^2 -(1/2)u^2 + u^2 v^2`,

and the normalized physical strain field is

`ex = nu D + M(v^2-u^2 v^2) + alpha Aex + B u v zeta`,

`ey = -D + M(u^2-u^2 v^2) + alpha Aey + B u v zeta`,

`gamma = 2 cosX cosY [ (M-alpha)u v - B zeta ]`.

Equivalent-strain matrix:

`E11=(ex+nu ey)/(1-nu^2)`,

`E22=(nu ex+ey)/(1-nu^2)`,

`E12=gamma/[2(1+nu)]`.

The material principal coordinates are the eigenvalues of this symmetric 2x2 matrix.

---

## Frozen R10 material source

Constants:

`kappa=2.0005129533678754`, `rho=0.1`, `eta=0.0024993589726987125`, `H=0.09799750427197301`, `UR=0.03`, `ACC=0.1072329249362415`, `AT=1-2^(-1/8)`.

`Pi_eta(z)=z^2(sqrt(z^2+eta^2)+z)/[2(z^2+eta^2)]`.

For principal coordinate `lambda_i`:

`c_i=Pi_eta(-lambda_i)`, `t_i=Pi_eta(lambda_i)`,

`C_i=kappa c_i/[1+(kappa-2)c_i+c_i^2]`,

`T_i=uR(t_i)/rho`,

`U_i=kappa lambda_i-C_i+kappa c_i+uR(t_i)-kappa t_i`.

The tensile polynomial is explicitly

- `r=t/(rho/kappa)`;
- for `r<=1`, `uR=rho r +(10H-6rho)r^3 +(8rho-15H)r^4 +(6H-3rho)r^5`;
- for `1<r<=10`, `s=(r-1)/9`, `uR=H+(UR-H)(10s^3-15s^4+6s^5)`;
- for `r>10`, `uR=UR`.

Principal normalized stresses:

`s1=U1-ACC C1^2 C2 + C1 T2 - rho AT T1 T2^8`,

`s2=U2-ACC C2^2 C1 + C2 T1 - rho AT T2 T1^8`.

This is equivalent to the matrix identity

`S = U - ACC det(C) C + C adj(T) - rho AT det(T) adj(T7)`.

---

## Infinite material stream and CH/D15 connection

On `lambda=c0+h x`, every scalar source is represented by its true infinite Chebyshev sequence. The universal square-root kernel `f=(lambda^2+eta^2)^(-1/2)` obeys

`(h^2/4)(n-1)a[n-2] + h c0(n-1/2)a[n-1] + A0 n a[n] + h c0(n+1/2)a[n+1] + (h^2/4)(n+1)a[n+2] = 0`,

`A0=c0^2+eta^2+h^2/2`.

The rational kernel `1/(lambda^2+eta^2)` has the corresponding constant-band recurrence. The compression source also has the exact global series

`C=kappa sum_{m>=1}(4-kappa)^(m-1) s^m`, `s=c/(1+c)^2`, with uniform ratio `<0.5`.

The tensile branch polynomials have exact cubic contact at the two physical knots; therefore the global `T,U,T7` coefficient tails are `O(n^-4)` and their first same-source directional derivative series is absolutely convergent.

For the matrix argument `Y=(E-c0 I)/h`, set `tau=tr Y`, `delta=det Y`. Then

`T_n(Y)=p_n I+q_n Y`,

`p_0=1,q_0=0,p_1=0,q_1=1`,

`p_{n+1}=-2 delta q_n-p_{n-1}`,

`q_{n+1}=2p_n+2 tau q_n-q_{n-1}`.

Examples:

`T_2(Y)=(-1-2delta)I+2tau Y`,

`T_3(Y)=(-4tau delta)I+(4tau^2-4delta-3)Y`.

For any structural target weight `W`,

`A_rs^(W)=D15[(W:I) tau^r delta^s]`,

`B_rs^(W)=D15[(W:Y) tau^r delta^s]`,

`J_n^(W)=sum P_n[r,s] A_rs^(W)+sum Q_n[r,s] B_rs^(W)`.

Every D15 monomial is exact. For `u=sinX`,

`int_0^pi sin^m X dX = sqrt(pi) Gamma((m+1)/2)/Gamma((m+2)/2)`

and recursively `I_m=(m-1)I_{m-2}/m`; thickness `int_{-1}^1 zeta^k dzeta=0` for odd `k` and `2/(k+1)` for even `k`.

The physical targets are

`Pc=-fc b t/(2 pi^2) D15[Syy]`,

`Q_z=(1+nu)S:E_,z - nu tr(S) I1_,z`,

`R_z^c=fc eps0 b ell t/(2 pi^2) D15[Q_z]`.

The same-source tangent is obtained by differentiating the same infinite streams, with

`d(det F)=adj(F):dF`, `d(adj F)=tr(dF)I-dF`.

The mathematical limit is

`lim_N D15[S_N]=D15[S_R10]`,

`lim_N D15[dS_N]=D15[dS_R10]`.

---

## Case21 released limit state

Input:

`b=ell=1220 mm`, `t=19.30 mm`, `q0=0.0025`, `fc=21.23 MPa`, `eps0=0.00209`, `nu=0.18`, `rho_sx=rho_sy=0.00375`, `Es=200000 MPa`.

Limit state:

`D=0.7887924801`, `q=0.0018083572562965242`, `lambda_A=0.08623596353826937`.

At this state:

`M=0.02907033478`, `B=0.06754686156`, `alpha=0.00250690833`.

The normalized strain coefficients are

`ex = 0.1413559193 -0.00022562175 u^2 +0.02781688062 v^2 -0.02656342645 u^2v^2 +0.06754686156 uv zeta`,

`ey = -0.7886796692 +0.02781688062 u^2 -0.00022562175 v^2 -0.02656342645 u^2v^2 +0.06754686156 uv zeta`,

`gamma=2 cosX cosY [0.02656342645 uv-0.06754686156 zeta]`.

Concrete limit target:

`Pc=337.923030 kN`, corresponding to `D15[Syy] ~= -13.34382686`.

Exact reinforcement closed form used at the same state:

`Ps=rho_sy t b Es eps0 (D-M/4)`.

With `rho_sy t b Es eps0=36908.355 N`, this gives `Ps=28.8447983 kN`.

The stored exact closed generalized-force formulas are

`RA_s=-CR[8D nu(nu+1)+M{5-(4nu^2+5)lambda_A}]`,

`Rq_s=CR Mq[8D(nu-1)+M(9-5lambda_A)]`,

with `CR=2.94090386184375`, `Mq=pi^2(q0+q)/eps0=20.34535011`.

They give

`Rq_s=-294.703813 kN mm`, `RA_s=-4.331388 kN mm`.

Therefore the concrete limit equilibrium target is the opposite contribution (up to the root tolerance), and

`Pu=Pc+Ps=366.767829 kN`.

Post-solve only: `Pf_exp=368.312750 kN`, error `-0.419459%`.

---

## Z6(a=24000) released limit state

Input:

`a=24000 mm`, `b=ell=12000 mm`, `m*=2`, `q0=0.004`, `tc=122 mm`, `ts=4 mm`, `rho_w=0.02`, `fc=30.4 MPa`, `eps0=0.0018712490394580678`, `nu_c=0.18`, `Es=206000 MPa`, `fy=355 MPa`, `nu_s=0.30`.

Limit state:

`D=1.36180798`, `q=0.0264854039`, `lambda_A=0.786915819`.

At this state:

`M=2.408685379`, `B=0.710106265`, `alpha=1.895432628`.

The normalized strain coefficients are

`ex = -0.2287327206 -0.1705889365 u^2 +1.4609690653 v^2 -0.5132527513 u^2v^2 +0.7101062649 uv zeta`,

`ey = -1.2765135117 +1.4609690653 u^2 -0.1705889365 v^2 -0.5132527513 u^2v^2 +0.7101062649 uv zeta`,

`gamma=2 cosX cosY [0.5132527513 uv-0.7101062649 zeta]`.

Released concrete limit:

`Pc,eff=22.8171044 MN`, hence before the `.98` web-volume replacement factor `Pc,full=23.2827596 MN`, corresponding to `D15[Syy] ~= -10.32641405`.

Frozen steel constitutive law is explicitly plane-stress elastic trial followed by a local radial ideal-plastic cap:

`sx_tr=Es/(1-nus^2)(ex+nus ey)`,

`sy_tr=Es/(1-nus^2)(nus ex+ey)`,

`tau_tr=Es/[2(1+nus)] gamma`,

`sigma_vm=sqrt(sx_tr^2-sx_tr sy_tr+sy_tr^2+3tau_tr^2)`,

`a_p=min(1,fy/sigma_vm)`,

`(sx,sy,tau)=a_p(sx_tr,sy_tr,tau_tr)`.

At the released state the faceplate trial `VM/fy ~=1.9474`, and the reported contributions are

`Ps_face=18.5564373 MN`, `Pw=7.0325797 MN`.

Thus

`Pu=.98 Pc,full+Ps_face+Pw=48.4061215 MN`.

Post-solve only: Zhou `49.48676675 MN` (`-2.18371%`), Winter `50.18585413 MN` (`-3.54628%`).

---

## Current human-calculability verdict — important gaps

### PASS / directly hand-auditable

1. finite Nguyen/Airy strain field for both Case21 and Z6;
2. equivalent-strain matrix and 2x2 principal-value reduction;
3. complete frozen R10 scalar law including both tensile branch polynomials;
4. exact nonlinear matrix stress identity;
5. true-infinite source recurrence structure and knot-tail law;
6. general-n CH recurrence;
7. exact D15 monomial moments;
8. physical definitions of `P,Rq,RA` and same-source tangent;
9. Case21 reinforcement closed-form contribution;
10. final finite equilibrium/limit equations and released roots.

### NOT YET SATISFACTORY under the user's strict hand-calculation criterion

1. **Infinite-series seed/limit evaluator:** Stage I gives the true recurrence and asymptotic/tail structure, but the current artifacts do not print a complete standalone set of low-order source seeds plus an explicit finite-special-function tail evaluator that lets a person reproduce the final `n->infinity` numerical target without consulting the raw-R10 oracle. The mathematical equality to R10 is proved, but the numerical infinite-sum implementation is not yet fully exposed as a hand ledger.

2. **Z6 faceplate plastic-zone exact integration:** the local radial cap law is explicit, but the current released Z6 value still uses the independent continuum oracle to localize/check the faceplate/web contribution. The exact yield-front equation and a closed piecewise D15 contraction of the yielded/non-yielded faceplate domains are not printed. Therefore `Ps_face=18.5564373 MN` is currently a released calculated result, not yet a complete hand-derived number under this stricter documentation standard.

3. **Case21 reinforcement constant `CR`:** the exact closed residual formulas and the numerical constant `CR=2.94090386184375` are stored, but the present Stage-III artifact does not re-derive `CR` from its underlying D15 monomial ledger. This is a documentation gap, smaller than the two items above.

4. **Root solving:** the finite nonlinear system itself is explicit, but the full iteration ledger is not printed. This is acceptable under the user's stated standard because the equations are exposed and only their repetitive numerical solution is omitted.

Accordingly, the present theory is mathematically closed at the true-infinite target level, but the current documentation is **not yet fully hand-reproducible end to end** for Z6 under the new stricter audit standard. The next documentation/theory task should fill the three specific gaps above rather than introducing a new physical model or new spatial integration method.
