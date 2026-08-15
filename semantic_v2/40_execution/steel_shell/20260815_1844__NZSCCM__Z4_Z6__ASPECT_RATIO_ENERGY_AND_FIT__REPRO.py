import math
ES=206000.; EC=32500.; FY=355.; FCP=30.4; NUS=.30; NUC=.20; LS=200.; TS=4.
def phi_fit(lam):
    if lam<=.55:return 1.
    Phi=.454+.192*lam+.416*lam*lam if lam<=1 else -.140+1.387*lam-.186*lam*lam
    return 1/(Phi+math.sqrt(Phi*Phi-lam*lam))
def zhou(a,b,h,ns):
    tc=h-2*TS;Ac=ns*(LS-TS)*tc;As=b*h-Ac;Pyth=FY*As+FCP*Ac
    Dx=ES*(h**3-tc**3)/12+EC*tc**3/12
    Dys=ES/b*(b*h**3/12-ns*(LS-TS)*tc**3/12)
    Dyc=EC/b*(ns*(LS-TS)*tc**3/12);Dy=Dys+Dyc
    Gs=ES/(2*(1+NUS));Gc=EC/(2*(1+NUC));A0=(b-TS)*(h-TS);ids=2*((b-TS)+(h-TS))/TS
    beta=(1/3)*(1-.63*(h-2*TS)/(b-2*TS)+.052*((h-2*TS)/(b-2*TS))**5)
    Dt=(1/b)*(4*Gs*A0*A0/ids+Gc*beta*(b-2*TS)*(h-2*TS)**3);H=Dt/2+NUS*Dys+NUC*Dyc
    cand=[(m,b*math.pi**2*(Dx*a*a/(m*m*b**4)+2*H/b**2+Dy*m*m/a**2)) for m in range(1,6)]
    m,Pcr=min(cand,key=lambda z:z[1]);lam=math.sqrt(Pyth/Pcr);phi=phi_fit(lam)
    return m,Pyth/1e6,Pcr/1e6,lam,phi,phi*Pyth/1e6
for name,b,h,ns in [('Z4',8000.,200.,40),('Z6',12000.,130.,60)]:
    for r in [.75,1.,1.25]:
        print(name,r,'kiso_m1',(r+1/r)**2,'zhou',zhou(r*b,b,h,ns))
lo,hi=1.45,1.52
for _ in range(60):
    x=(lo+hi)/2;h=1e-6;d=(phi_fit(x+h)-phi_fit(x-h))/(2*h)
    if d<0:lo=x
    else:hi=x
print('fit_phi_local_min_lambda',(lo+hi)/2,'phi',phi_fit((lo+hi)/2))
