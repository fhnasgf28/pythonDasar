def hitung_pajak(penghasilan):
    if penghasilan < 50000000:
        pajak = 0.5 * penghasilan
    elif 50000000 <= penghasilan < 250000000:
        pajak = 0.10 * penghasilan
    else:
        pajak = 0.15 * penghasilan

    return pajak

def alokasi_penghasilan(penghasilan):
    pajak = hitung_pajak(penghasilan)
    kebutuhan_pokok = 0.50 * penghasilan
    tabungan_investasi = 0.20 * penghasilan
    hiburan_lainnya = 0.30 * penghasilan
    sisa_penghasilan = penghasilan - (kebutuhan_pokok + tabungan_investasi + hiburan_lainnya )
    return {
        "penghasilan": penghasilan,
        "pajak": pajak,
        "kebutuhan_pokok": kebutuhan_pokok,
        "tabungan_investasi": tabungan_investasi,
        "hiburan_lainnya": hiburan_lainnya,
        "sisa_penghasilan": sisa_penghasilan
    }

def main():
    try:
        penghasilan = float(input("Masukkan penghasilan tahunan Anda: Rp "))
        hasil = alokasi_penghasilan(penghasilan)
        print("\nHasil alokasi penghasilan:")
        print(f"Penghasilan: Rp {penghasilan:.2f}")
        print(f"Pajak: Rp {hasil['pajak']:.2f}")
        print(f"Kebutuhan Pokok: Rp {hasil['kebutuhan_pokok']:.2f}")
        print(f"Tabungan Investasi: Rp {hasil['tabungan_investasi']:.2f}")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang benar.")

if __name__ == "__main__":
    main()