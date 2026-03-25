import locale

def format_idr(amount):
    """
    Fungsi untuk memformat angka menjadi format mata uang Rupiah.
    Contoh: 5000000 -> Rp 5.000.000
    """
    try:
        locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')
    except locale.Error:
        try:
            locale.setlocale(locale.LC_ALL, 'Indonesian_Indonesia.1252')
        except locale.Error:
            pass # Lanjutkan dengan format manual jika locale tidak ditemukan

    return f"Rp {amount:,.0f}".replace(",", "#").replace(".", ",").replace("#", ".")

def hitung_biaya_bulanan(gaji_bulanan, custom_pengeluaran):
    """
    Menghitung dan menampilkan ringkasan biaya bulanan berdasarkan input.

    Args:
        gaji_bulanan (int): Jumlah gaji bulanan.
        custom_pengeluaran (dict): Kamus pengeluaran dari pengguna.
    Returns:
        tuple: (dict_pengeluaran, total_pengeluaran, sisa_uang)
    """
    total_pengeluaran = sum(custom_pengeluaran.values())
    sisa_uang = gaji_bulanan - total_pengeluaran

    print("\n--- RINGKASAN BIAYA BULANAN ANDA ---")
    print(f"Gaji Bulanan Anda      : {format_idr(gaji_bulanan)}")
    print("------------------------------------")
    print("DETAIL PENGELUARAN:")
    for kategori, jumlah in custom_pengeluaran.items():
        if jumlah > 0: # Hanya tampilkan pengeluaran yang ada isinya
            print(f"- {kategori:<35}: {format_idr(jumlah)}")
    print("------------------------------------")
    print(f"TOTAL PENGELUARAN      : {format_idr(total_pengeluaran)}")
    print("------------------------------------")
    print(f"SISA UANG ANDA         : {format_idr(sisa_uang)}")
    print("------------------------------------")

    if sisa_uang < 0:
        print("\n!!! PERHATIAN: Pengeluaran Anda melebihi gaji. Harap tinjau kembali anggaran Anda. !!!")
    elif sisa_uang > 0:
        print("\nSisa uang bisa ditabung lebih banyak atau digunakan untuk kebutuhan mendadak lainnya.")
    else:
        print("\nAnggaran Anda pas, namun pertimbangkan untuk menyisihkan sedikit untuk dana darurat jika belum ada.")

    return custom_pengeluaran, total_pengeluaran, sisa_uang

def minta_input_pengguna():
    """
    Fungsi untuk meminta input gaji dan detail pengeluaran dari pengguna.
    """
    # 1. Meminta input gaji dari pengguna
    while True:
        try:
            gaji_anda = int(input("Masukkan total gaji bulanan Anda (Rp): "))
            if gaji_anda < 0:
                print("Jumlah gaji tidak boleh negatif. Silakan masukkan angka positif.")
            else:
                break
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")

    # 2. Meminta input pengeluaran dari pengguna
    print("\n--- Silakan Masukkan Detail Pengeluaran Anda ---")
    print("(Kosongkan jika tidak ada pengeluaran untuk kategori tersebut)")
    
    pengeluaran_interaktif = {}
    kategori_input = [
        "Sewa/Cicilan Rumah",
        "Tagihan Utilitas (Listrik, Air, Gas)",
        "Internet",
        "Pulsa/Paket Data",
        "Transportasi",
        "Belanja Kebutuhan Pokok (Groceries)",
        "Makan di Luar/Hiburan",
        "Perawatan Diri/Kesehatan",
        "Hobi/Hiburan Lain",
        "Tabungan/Investasi",
        "Lain-lain/Darurat"
    ]

    for kategori in kategori_input:
        while True:
            try:
                prompt_text = f"- Masukkan biaya untuk '{kategori}' (Rp): "
                jumlah_str = input(prompt_text)
                
                jumlah = int(jumlah_str) if jumlah_str else 0

                if jumlah < 0:
                    print("  Jumlah tidak boleh negatif. Silakan masukkan angka positif.")
                else:
                    pengeluaran_interaktif[kategori] = jumlah
                    break
            except ValueError:
                print("  Input tidak valid. Harap masukkan hanya angka.")
    
    return gaji_anda, pengeluaran_interaktif

if __name__ == "__main__":
    gaji, pengeluaran = minta_input_pengguna()
    hitung_biaya_bulanan(gaji, pengeluaran)
