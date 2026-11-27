# NEKA unit economics & projections (all Rp miliar unless noted)
# Revenue per store: BRIDS visit 150-200 trx/day x Rp80-100k
lo = 150*80_000*30/1e9; hi=200*100_000*30/1e9; base=170*88_000*30/1e9
print("rev/store/month M: lo %.2f base %.2f hi %.2f"%(lo,base,hi))
# MDIY benchmark
mdiy_rev=7190; st_end25=1416-202; avg=(st_end25+1416)/2
print("MDIY avg stores",avg,"rev/store/month M %.3f"%(mdiy_rev/9/avg/1))
print("MDIY GM 9M26 %.1f%%  9M25 %.1f%%  NM %.1f%%"%(3690/7190*100, 3200/5770*100, 894.3/7190*100))
# per-store P&L monthly, Rp juta
def pnl(rev, gm, staff, rent, util, other_pct):
    gp=rev*gm; other=rev*other_pct; c=gp-staff-rent-util-other
    return gp,c
scen={'pesimis':(360,0.43,48,60,22,0.09,2100),'dasar':(450,0.45,48,50,20,0.08,1800),'optimis':(600,0.46,50,45,20,0.07,1500)}
for k,(rev,gm,s,r,u,o,capex) in scen.items():
    gp,c=pnl(rev,gm,s,r,u,o)
    print(k,"rev",rev,"GP %.0f"%gp,"contrib %.0f (%.1f%%)"%(c,c/rev*100),"capex",capex,"payback bln %.0f"%(capex/c))
# store projections
stores_oct26=35
def proj(rate26, rate):
    e26=stores_oct26+rate26*2
    e27=e26+rate*12; e28=e27+rate*12
    return e26,e27,e28
for name,(r26,r,rev,ramp27,ramp28) in {'konservatif':(2,2,0.36,0.85,0.9),'dasar':(3.5,3.5,0.45,0.85,0.9),'agresif':(5,6,0.55,0.85,0.9)}.items():
    e26,e27,e28=proj(r26,r)
    om27=(e26+e27)/2*rev*12*ramp27; om28=(e27+e28)/2*rev*12*ramp28
    capex=(e28-e26)*1.8
    print(name,"end26 %.0f end27 %.0f end28 %.0f"%(e26,e27,e28),"omzet27 Rp%.0fM omzet28 Rp%.0fM capex26-28 Rp%.0fM"%(om27*1000/1000*1, om28, capex))
# 2026 NEKA revenue estimate: store-months
sm=[10,11,12,13,14,17,22,25,29,33,36,39]
print("store-months",sum(sm),"rev26 base Rp%.0fM"%(sum(sm)*0.45*0.8), "range %.0f-%.0f"%(sum(sm)*0.36*0.8,sum(sm)*0.6*0.8))
print("ACES annualised 9M26", 6857/9*12)
