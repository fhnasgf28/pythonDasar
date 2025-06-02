def is_hp_worth_it(harga_hp, penghasilan_bulanan, pengeluaran_bulanan, masa_pakai_tahun, penggunaan_untuk_kerja=True):
    sisa_bulanan = penghasilan_bulanan - pengeluaran_bulanan
    aman_secara_keuangan = sisa_bulanan > penghasilan_bulanan * 0.3
    biaya_per_bulan = harga_hp / (masa_pakai_tahun * 12)
    if penggunaan_untuk_kerja:
        manfaat = biaya_per_bulan * 1.5
    else:
        manfaat = biaya_per_bulan * 0.8
    
    worth_it = aman_secara_keuangan and (manfaat >= biaya_per_bulan)
    return {
        "sisa_bulanan": sisa_bulanan,
        "aman_secara_keuangan": aman_secara_keuangan,
        "biaya_per_bulan": biaya_per_bulan,
        "manfaat": manfaat,
        "worth_it": worth_it,
        "cataan": "layak beli" if worth_it else "tidak layak beli"
    }

# Contoh penggunaan fungsi
hasil = is_hp_worth_it(
    harga_hp=5000000,
    penghasilan_bulanan=4500000,
    pengeluaran_bulanan=2000000,
    masa_pakai_tahun=8,
    penggunaan_untuk_kerja=True
)
print(hasil)
print(f"Sisa bulanan: {hasil['sisa_bulanan']}")
print(f"Aman secara keuangan: {hasil['aman_secara_keuangan']}")
print(f"Biaya per bulan: {hasil['biaya_per_bulan']}")