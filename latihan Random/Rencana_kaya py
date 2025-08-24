from dataclasses import dataclass
from math import ceil
from random import gauss
from statistics import median
from typing import List, Tuple

@dataclass
class Inputs:
    monthly_income: float           # gaji bersih per bulan (IDR)
    monthly_expense: float          # biaya hidup per bulan (IDR)
    current_savings: float          # total tabungan/investasi saat ini (IDR)
    emergency_months: int = 6       # target dana darurat (x bulan biaya)
    invest_return_mean: float = 0.10   # ekspektasi return tahunan (10% = 0.10)
    invest_return_vol: float = 0.15    # volatilitas tahunan (15% = 0.15)
    zakat_rate: float = 0.0            # 0.025 jika ingin zakat tahunan otomatis
    halal_mode: bool = True            # True: prioritaskan dana darurat, hindari leverage
    target_multiple_expense: float = 25.0  # target “kaya” = 25x biaya tahunan (FIRE-style)
    invest_all_surplus: bool = True        # True: seluruh surplus (di luar darurat) diinvest

@dataclass
class PlanResult:
    monthly_invest: float
    months_to_emergency: int
    annual_savings_rate: float
    annual_surplus: float
    target_networth: float

def plan(inputs: Inputs) -> PlanResult:
    # Hitung zakat bulanan (opsional). Umumnya zakat harta tahunan; di sini kita sederhanakan bulanan.
    zakat_monthly = 0.0
    if inputs.zakat_rate > 0:
        # zakat dari surplus+aset: perkiraan kasar → diambil dari surplus bulanan untuk konservatif
        pass

    surplus = max(0.0, inputs.monthly_income - inputs.monthly_expense - zakat_monthly)
    if surplus <= 0:
        raise ValueError("Surplus <= 0. Kurangi pengeluaran atau tambah penghasilan dulu.")

    # Target dana darurat
    emergency_target = inputs.emergency_months * inputs.monthly_expense
    already_safe = inputs.current_savings >= emergency_target
    monthly_invest = surplus if (already_safe or not inputs.halal_mode) else 0.0
    monthly_to_emergency = 0.0 if already_safe else surplus

    months_to_emergency = 0
    if not already_safe:
        needed = emergency_target - inputs.current_savings
        months_to_emergency = ceil(needed / monthly_to_emergency)

    annual_surplus = surplus * 12
    annual_savings_rate = annual_surplus / max(1.0, inputs.monthly_income * 12)  # proporsi dari income
    target_networth = inputs.target_multiple_expense * (inputs.monthly_expense * 12)

    return PlanResult(
        monthly_invest=monthly_invest,
        months_to_emergency=months_to_emergency,
        annual_savings_rate=annual_savings_rate,
        annual_surplus=annual_surplus,
        target_networth=target_networth
    )

def year_steps_from_monthly(months: int) -> Tuple[int, int]:
    return months // 12, months % 12

def deterministic_years_to_target(inputs: Inputs, planres: PlanResult, max_years: int = 60) -> int:
    """Perkiraan sederhana tanpa volatilitas: compounding dengan return rata-rata."""
    nw = inputs.current_savings
    monthly_r = (1 + inputs.invest_return_mean) ** (1/12) - 1
    monthly_invest = planres.monthly_invest

    # Fase 1: bangun dana darurat dulu (halal_mode)
    months = 0
    if inputs.halal_mode and planres.months_to_emergency > 0:
        nw += planres.months_to_emergency * (inputs.monthly_income - inputs.monthly_expense)
        months += planres.months_to_emergency

    # Setelah dana darurat aman, invest bulanan
    while nw < planres.target_networth and months < max_years * 12:
        nw = nw * (1 + monthly_r) + monthly_invest
        months += 1

    return months if nw >= planres.target_networth else -1

def monte_carlo_probability(inputs: Inputs, planres: PlanResult, years: int = 30, trials: int = 2000) -> Tuple[float, List[int]]:
    """Simulasi volatilitas return tahunan (lognormal approx via normal di aritmatik)."""
    successes = 0
    months_to_hit: List[int] = []
    for _ in range(trials):
        nw = inputs.current_savings
        months = 0

        # Fase darurat
        if inputs.halal_mode and planres.months_to_emergency > 0:
            nw += planres.months_to_emergency * (inputs.monthly_income - inputs.monthly_expense)
            months += planres.months_to_emergency

        while months < years * 12 and nw < planres.target_networth:
            # hasilkan return tahunan acak, lalu ubah jadi bulanan
            annual_r = gauss(inputs.invest_return_mean, inputs.invest_return_vol)
            monthly_r = (1 + annual_r) ** (1/12) - 1
            # 12 langkah bulan dalam satu tahun
            for _m in range(12):
                if months >= years * 12 or nw >= planres.target_networth:
                    break
                nw = nw * (1 + monthly_r) + planres.monthly_invest
                months += 1

        if nw >= planres.target_networth:
            successes += 1
            months_to_hit.append(months)

    prob = successes / trials if trials > 0 else 0.0
    return prob, months_to_hit

def pretty_currency(x: float) -> str:
    # Format sederhana IDR
    return f"Rp {x:,.0f}".replace(",", ".")

def summarize(inputs: Inputs) -> None:
    pr = plan(inputs)
    months_det = deterministic_years_to_target(inputs, pr, max_years=60)
    if months_det >= 0:
        y, m = year_steps_from_monthly(months_det)
    else:
        y, m = (-1, -1)

    # Monte Carlo untuk 30 tahun
    prob30, hits = monte_carlo_probability(inputs, pr, years=30, trials=1000)
    med_hit = None
    if hits:
        mh_y, mh_m = year_steps_from_monthly(int(median(hits)))
        med_hit = f"{mh_y} tahun {mh_m} bulan"

    print("=== Rencana Kekayaan (Versi Keluarga Menengah) ===")
    print(f"Income bulanan      : {pretty_currency(inputs.monthly_income)}")
    print(f"Biaya bulanan       : {pretty_currency(inputs.monthly_expense)}")
    print(f"Aset awal           : {pretty_currency(inputs.current_savings)}")
    print(f"Dana darurat target : {inputs.emergency_months} bulan x biaya = {pretty_currency(inputs.emergency_months * inputs.monthly_expense)}")
    print(f"Surplus / bulan     : {pretty_currency(max(0, inputs.monthly_income - inputs.monthly_expense))}")
    print(f"Invest / bulan      : {pretty_currency(pr.monthly_invest)} (setelah dana darurat aman)")
    print(f"Butuh dana darurat  : {pr.months_to_emergency} bulan (estimasi)")
    print(f"Target net worth    : {inputs.target_multiple_expense:.0f}x biaya tahunan = {pretty_currency(pr.target_networth)}")
    print(f"Return tahunan (μ/σ): {inputs.invest_return_mean*100:.1f}% / {inputs.invest_return_vol*100:.1f}%")
    print(f"Saving rate tahunan : {pr.annual_savings_rate*100:.1f}% dari income")
    if months_det >= 0:
        print(f"Estimasi (deterministik): tercapai dalam ~ {y} tahun {m} bulan.")
    else:
        print("Estimasi (deterministik): > 60 tahun (perlu naikkan investasi atau turunkan biaya).")
    print(f"Probabilitas tercapai ≤30 th (Monte Carlo): {prob30*100:.1f}%")
    if med_hit:
        print(f"Median waktu tercapai (simulasi): {med_hit}")
    print("==================================================")

# ----------------------------
# CONTOH PEMAKAIAN:
# Angka di bawah hanyalah contoh tipikal keluarga menengah. UBAH sesuai kondisimu.
if __name__ == "__main__":
    contoh = Inputs(
        monthly_income=12_000_000,     # gaji bersih bulanan
        monthly_expense=7_500_000,     # biaya hidup bulanan
        current_savings=25_000_000,    # tabungan awal
        emergency_months=6,
        invest_return_mean=0.10,       # ekspektasi return tahunan 10%
        invest_return_vol=0.15,        # volatilitas 15%
        zakat_rate=0.0,                # set 0.025 jika ingin potong zakat tahunan secara kasar
        halal_mode=True,
        target_multiple_expense=25.0,  # target “financial independence”
        invest_all_surplus=True
    )
    summarize(contoh)
