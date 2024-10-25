def hitung_pajak(penghasilan):
    if penghasilan <= 50000000:
        pajak = 0
    elif penghasilan <= 250000000:
        pajak = (penghasilan - 50000000) * 0.10
    elif penghasilan <= 500000000:
        pajak = (200000000 * 0.10) + (250000000 * 0.15) + (penghasilan - 500000000) * 0.25
    return pajak

def main():
    try:
        penghasilan = float(input("Masukkan penghasilan tahunan Anda: Rp "))
        pajak = hitung_pajak(penghasilan)
        print(f"Pajak yang harus dibayar: {pajak:,.2f}")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang benar.")

if __name__ == "__main__":
    main()