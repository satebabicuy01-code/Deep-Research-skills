"""Simulasi arus kas tahunan (mencerminkan formula di kalkulator Excel)."""
from scenarios import ASSUMPTIONS as A, AGES, AGE_START, RETIRE_AGE, SCENARIOS


def simulate(s):
    i, ih, gp = A["inflasi"], A["inflasi_kesehatan"], A["kenaikan_properti"]
    bal, jht, prop, cum = 0.0, 0.0, 0.0, 1.0
    rows, cums, Z = [], [], []
    for a in AGES:
        t = a - AGE_START
        D, E, G = (1 + i) ** t, (1 + ih) ** t, (1 + gp) ** t
        working = a < RETIRE_AGE
        r = s["r_acc"] if working else s["r_ret"]
        jht_in = A["iuran_jht"] * s["gaji"][a] * 12 * D if working else 0.0
        jht_cash = jht if a == RETIRE_AGE else 0.0
        jht = jht * (1 + A["imbal_jht"]) + jht_in if working else 0.0
        flow = (12 * D * (s["gaji"][a] + s["tambahan"][a] + s["properti_income"][a] + s["jp"][a]
                          - s["biaya"][a] - s["tinggal"][a])
                - 12 * E * s["kesehatan"][a] - s["beli_aset"][a] * G + s["lain"][a] * D + jht_cash)
        bal = bal * (1 + r) + flow * (1 + r / 2)
        prop = prop * (1 + gp) + s["beli_aset"][a] * G
        cum *= (1 + r)
        cums.append(cum)
        Z.append(12 * D * (1 + r / 2) if working else 0.0)
        rows.append(dict(age=a, D=D, flow=flow, bal=bal, real=bal / D, jht=jht, prop=prop))
    # tambahan tabungan bulanan (nilai hari ini) agar saldo usia 75 >= 0
    cum75 = cums[-1]
    zsum = sum(z * cum75 / c for z, c in zip(Z, cums))
    need = max(0.0, -rows[-1]["bal"]) / zsum
    neg = [r["age"] for r in rows if r["bal"] < 0 and r["age"] >= RETIRE_AGE]
    at49 = next(r for r in rows if r["age"] == RETIRE_AGE - 1)
    at50 = next(r for r in rows if r["age"] == RETIRE_AGE)
    last = rows[-1]
    return dict(rows=rows, saldo50_real=at49["real"], saldo75_real=last["real"],
                prop75_real=last["prop"] / last["D"], habis=neg[0] if neg else None,
                tambahan_bulanan=need, jht50_real=at49["jht"] / at50["D"])


if __name__ == "__main__":
    for s in SCENARIOS:
        r = simulate(s)
        print(f"{s['code']}: saldo49={r['saldo50_real']:8.0f} jht={r['jht50_real']:5.0f} "
              f"saldo75={r['saldo75_real']:8.0f} prop75={r['prop75_real']:6.0f} "
              f"habis={r['habis']} need/bln={r['tambahan_bulanan']:.1f}")
