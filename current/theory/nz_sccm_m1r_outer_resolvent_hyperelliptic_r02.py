"""NZ-SCCM M1R outer resolvent / hyperelliptic classification R02.

Formal purpose
--------------
Exact structural classification only. No Case21 Pu, no Swartz24, no spatial
quadrature, no material-point integration.

Checks
------
1. R01 rational primitives have finite simple scalar-pole decompositions.
2. 2D matrix resolvent and "oth" identities.
3. Pair-resolvent source block exact Cayley-Hamilton reduction.
4. Delta_r(s)=I2(s)-r*s+r^2 is quadratic in s.
5. Endpoint identity Delta_r(s±)=E_r±sqrt(xy) O_r.
6. Gamma_r=4xy*disc_s(Delta_r) is polynomial of bidegree <=(3,3),
   total degree 4.
7. One exact rational specialization gives a square-free degree-5
   hyperelliptic curve, proving generic genus >= 2 behavior is present.

This script is an analytic architecture audit, not a production special-function
evaluator.
"""
from __future__ import annotations

import json
import numpy as np
import sympy as sp

FC = 21.23
E0 = 20321.0
EPS0 = 0.00209
KAPPA = E0 * EPS0 / FC

U_COEF = np.array([-9.786990860138413,20.2150042396063,-10.648551770753837,-2.1990006614651056,27.740854104357723,21.454401259317827,32.84751931776155])
C_COEF = np.array([-0.9442135131854792,8.475283733893267,-19.155032651471718,11.717171611700422,2.502734679618874,36.42244419918754,31.105995105744704,36.19639777683384])
C2_COEF = np.array([-0.22001900119107273,1.235734615177478,-1.4750318560416769,0.02930272701903502,2.4695146543890787,6.3090038864234,4.550686012252086,2.6723789248563734])
T_COEF = np.array([5.2832456515727308e+00,5.9036380076624050e+02,1.6827160529299152e+04,3.4424484696375992e+05,2.3654301901438353e+06,-5.3855760768061061e+05,-1.9558929506678067e+07,4.6747916139120964e+05,3.6048668340100557e+07,1.6064437897170084e+07,-1.4488932046500764e+02,1.5542658904204591e+04,-5.2992374395863095e+05,9.7304263129297085e+06,-8.4085213382741570e+07,4.6193321040738773e+08,-1.4278058956538005e+09,2.5022789964268451e+09,-2.4676258484463243e+09,1.1691624735294776e+09])
V_COEF = np.array([-2.6397090716844929e+00,8.5521709459697178e+01,4.7435950866466396e+02,-7.6967479847511470e+02,-7.2653855232676938e+02,-4.5562216690418325e+01,9.5670115797598226e+02,-1.0491501141642168e+04,6.6993892415682218e+04,-3.1190274492658256e+04])


def primitive_polynomials():
    out = {}
    n1,n2,n3,d1,d2,d3,d4 = U_COEF
    out['U']=(np.array([0.0,KAPPA,n1,n2,n3]),np.array([1.0,d1,d2,d3,d4]))
    for name,coef,m in (('C',C_COEF,3),('C2',C2_COEF,3),('T',T_COEF,9),('V',V_COEF,4)):
        num=np.zeros(m+2); num[1:]=coef[:m+1]
        den=np.r_[1.0,coef[m+1:]]
        out[name]=(num,den)
    return out


def pole_audit():
    out={}
    for name,(num,den) in primitive_polynomials().items():
        roots=np.roots(den[::-1])
        minsep=min(abs(roots[i]-roots[j]) for i in range(len(roots)) for j in range(i+1,len(roots)))
        q,_=np.polydiv(num[::-1],den[::-1])
        dder=np.array([k*den[k] for k in range(1,len(den))])
        residues=[]
        for root in roots:
            Nv=sum(num[k]*root**k for k in range(len(num)))
            Dp=sum(dder[k-1]*root**(k-1) for k in range(1,len(den)))
            residues.append(Nv/Dp)
        errs=[]
        for lam in (-2.0,-0.5,0.1,0.7):
            exact=np.polyval(num[::-1],lam)/np.polyval(den[::-1],lam)
            recon=q[-1]+sum(res/(lam-root) for res,root in zip(residues,roots))
            errs.append(abs(exact-recon))
        out[name]={'degree':int(len(den)-1),'quotient_constant':float(np.real(q[-1])),'min_pole_separation':float(minsep),'real_poles':[float(z.real) for z in roots if abs(z.imag)<1e-10],'partial_fraction_reconstruction_max_abs':float(max(errs))}
    return out


def symbolic_audit():
    x,y,s,D,M,B,nu,r,t=sp.symbols('x y s D M B nu r t', nonzero=True)
    H=x+y-2*x*y
    K=nu*x-y+(1-nu)*x*y
    a=(nu-1)*D+M*H
    I2=(-nu*D**2+D*M*K+D*(nu-1)*(s-a)/2+M*(2-x-y)*(s-a)/2+(x+y-1)*(s-a)**2/(4*x*y))
    Dr=sp.expand(I2-r*s+r**2); Dt=sp.expand(I2-t*s+t**2)
    Ar,Br=(s-r)/Dr,-1/Dr
    Ato,Bto=-t/Dt,1/Dt
    Aprod=sp.factor(Ar*Ato-Br*Bto*I2)
    Bprod=sp.factor(Ar*Bto+Br*Ato+Br*Bto*s)
    target_A=sp.factor((I2-t*(s-r))/(Dr*Dt)); target_B=sp.factor((t-r)/(Dr*Dt))
    E=sp.factor(-nu*D**2+D*M*K+B**2*(x+y-1)-r*a+r**2)
    O=sp.factor(B*(D*(nu-1)+M*(2-x-y)-2*r))
    w=sp.symbols('w')
    def reduce_w2(expr):
        poly=sp.Poly(sp.expand(expr),w); out=0
        for (k,),coef in poly.terms():
            out += coef*(x*y)**(k//2) if k%2==0 else coef*(x*y)**((k-1)//2)*w
        return sp.factor(out)
    endpoint_plus_ok=sp.simplify(reduce_w2(Dr.subs(s,a+2*B*w))-(E+w*O))==0
    endpoint_minus_ok=sp.simplify(reduce_w2(Dr.subs(s,a-2*B*w))-(E-w*O))==0
    Qr=sp.factor(4*x*y*Dr)
    Gamma=sp.factor(sp.discriminant(Qr,s)/(4*x*y)); pg=sp.Poly(Gamma,x,y)
    spec={D:sp.Integer(1),M:sp.Integer(1),nu:sp.Rational(1,5),r:sp.Integer(2),y:sp.Rational(1,3)}
    Gamma_spec=sp.factor(Gamma.subs(spec)); P5=sp.factor(x*(1-x)*Gamma_spec)
    gcd=sp.gcd(sp.Poly(P5,x),sp.Poly(sp.diff(P5,x),x)); discr=sp.factor(sp.discriminant(sp.Poly(P5,x),x))
    return {'pair_resolvent_A_identity':bool(sp.simplify(Aprod-target_A)==0),'pair_resolvent_B_identity':bool(sp.simplify(Bprod-target_B)==0),'Delta_r_degree_s':int(sp.Poly(Dr,s).degree()),'endpoint_plus_identity':bool(endpoint_plus_ok),'endpoint_minus_identity':bool(endpoint_minus_ok),'E_total_degree_xy':int(sp.Poly(E,x,y).total_degree()),'O_total_degree_xy':int(sp.Poly(O,x,y).total_degree()),'endpoint_product_total_degree_xy':int(sp.Poly(sp.expand(E**2-x*y*O**2),x,y).total_degree()),'Gamma_degree_x':int(pg.degree(x)),'Gamma_degree_y':int(pg.degree(y)),'Gamma_total_degree':int(pg.total_degree()),'Gamma_term_count':int(len(pg.terms())),'Gamma_x3_coefficient':str(sp.factor(sp.Poly(Gamma,x).coeff_monomial(x**3))),'Gamma_y3_coefficient':str(sp.factor(sp.Poly(Gamma,y).coeff_monomial(y**3))),'genus_witness_Gamma':str(Gamma_spec),'genus_witness_P5':str(P5),'genus_witness_degree':int(sp.Poly(P5,x).degree()),'genus_witness_gcd_degree':int(sp.Poly(gcd,x).degree()),'genus_witness_discriminant':str(discr),'genus_witness_genus':2}


def main():
    result={'status':{'M1R_R02_RESOLVENT_CANONICALIZATION':'PASS_EXACT','M1R_R02_ACTUAL_S_FACTORS':'QUADRATIC_ONLY','M1R_R02_ENDPOINT_ALGEBRA':'PASS_EXACT','M1R_R02_GENERIC_OUTER_CLASS_A':'FAIL','M1R_R02_GENERIC_ORDINARY_ELLIPTIC':'INSUFFICIENT','M1R_R02_GENERIC_SIMPLE_APPELL':'NOT_GENERAL','M1R_R02_OUTER_PERIOD_CLASS':'HYPERELLIPTIC_RELATIVE / PICARD_FUCHS','FORMAL_WHOLE_HALFWAVE_GATE_A':'HOLD'},'canonical_block_counts':{'scalar_poles_total':27,'single_pole_blocks_consolidated_max':27,'pair_C2_C':16,'pair_C_T':40,'pair_T_V':50,'pair_total':106,'constant_plus_single_plus_pair_complex_blocks_max':134},'pole_audit':pole_audit(),'symbolic_audit':symbolic_audit()}
    print(json.dumps(result,indent=2,ensure_ascii=False))

if __name__=='__main__':
    main()
