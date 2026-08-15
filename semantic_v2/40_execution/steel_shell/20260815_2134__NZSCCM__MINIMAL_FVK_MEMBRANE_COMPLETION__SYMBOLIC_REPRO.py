"""Symbolic audit only: no Pu, no material solve, no spatial quadrature.
Verifies loaded-edge admissibility, zero linear shear, polynomial forms, and rank
for the minimum single-halfwave FvK membrane-completion basis.
"""
import sympy as sp

X,Y,a,b=sp.symbols('X Y a b', positive=True)
k=b/a

# Per-unit dimensionless generalized-coordinate displacement shapes (length units).
U20=b/(2*sp.pi)*sp.sin(2*X)*sp.sin(Y)**2
V20=b**2/(4*sp.pi*a)*sp.cos(2*X)*sp.sin(2*Y)
U02=sp.Integer(0)
V02=a/(2*sp.pi)*sp.sin(2*Y)

# Chain rules: d/dx=(pi/b)d/dX, d/dy=(pi/a)d/dY.
def strains(U,V):
    ex=sp.simplify((sp.pi/b)*sp.diff(U,X))
    ey=sp.simplify((sp.pi/a)*sp.diff(V,Y))
    g=sp.simplify((sp.pi/a)*sp.diff(U,Y)+(sp.pi/b)*sp.diff(V,X))
    return ex,ey,g

ex20,ey20,g20=strains(U20,V20)
ex02,ey02,g02=strains(U02,V02)

print('p20 loaded-edge U:',sp.simplify(U20.subs(Y,0)),sp.simplify(U20.subs(Y,sp.pi)))
print('p20 loaded-edge V:',sp.simplify(V20.subs(Y,0)),sp.simplify(V20.subs(Y,sp.pi)))
print('p02 loaded-edge V:',sp.simplify(V02.subs(Y,0)),sp.simplify(V02.subs(Y,sp.pi)))
print('p20 strains:',ex20,ey20,g20)
print('p02 strains:',ex02,ey02,g02)

# Exact polynomial expressions in xs=sin X, ys=sin Y.
xs,ys=sp.symbols('xs ys')
poly_ex20=ys**2-2*xs**2*ys**2
poly_ey20=sp.expand(k**2/sp.Integer(2)*(1-2*xs**2)*(1-2*ys**2))
poly_ey02=1-2*ys**2
print('polynomial p20 ex=',poly_ex20)
print('polynomial p20 ey=',poly_ey20)
print('polynomial p02 ey=',poly_ey02)

# Rank audit in a finite polynomial coefficient basis.
# slots = ex00,ex10,ex02,ex12,ex22,ey00,ey10,ey02,ey12,ey20,ey22
D=sp.Matrix([0,0,0,0,0,-1,0,0,0,0,0])
c=sp.Matrix([0,0,0,4/sp.pi,0,0,8*k**2/sp.pi,0,-16*k**2/sp.pi,0,0])
p20=sp.Matrix([0,0,1,0,-2,k**2/2,0,-k**2,0,-k**2,2*k**2])
p02=sp.Matrix([0,0,0,0,0,1,0,-2,0,0,0])
M=sp.Matrix.hstack(D,c,p20,p02)
print('rank[D,c,p20,p02]=',M.rank())
assert sp.simplify(g20)==0
assert sp.simplify(g02)==0
assert M.rank()==4
