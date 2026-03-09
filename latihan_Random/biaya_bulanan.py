import locale

def format_idr(amount):
    """
    Fungsi untuk memformat angka menjadi format mata uang Rupiah.
    Contoh: 5000000 -> Rp 5.000.000
    """
    # Mengatur locale ke Indonesia untuk format mata uang
    # Ini mungkin tidak bekerja di semua sistem operasi tanpa instalasi locale yang tepat.
    # Sebagai alternatif, kita bisa melakukan format manual.
    try:
        locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')
    except locale.Error:
        try:
            locale.setlocale(locale.LC_ALL, 'Indonesian_Indonesia.1252')
        except locale.Error:
            pass # Lanjutkan dengan format manual jika locale tidak ditemukan

    # Format manual jika locale tidak berhasil diatur atau untuk konsistensi
    return f"Rp {amount:,.0f}".replace(",", "#").replace(".", ",").replace("#", ".")

def hitung_biaya_bulanan(gaji_bulanan, custom_pengeluaran=None):
    """
    Menghitung dan menampilkan ringkasan biaya bulanan.

    Args:
        gaji_bulanan (int): Jumlah gaji bulanan.
        custom_pengeluaran (dict, optional): Kamus pengeluaran kustom.
                                             Jika None, akan menggunakan pengeluaran contoh.
    Returns:
        tuple: (dict_pengeluaran, total_pengeluaran, sisa_uang)
    """

    # Contoh pengeluaran bulanan untuk gaji 5.000.000 IDR
    # HARAP SESUAIKAN DENGAN PENGELUARAN ANDA SENDIRI!
    pengeluaran_contoh = {
        "Sewa/Cicilan Rumah": 1_200_000,  # Contoh: Studio/kosan atau cicilan ringan
        "Tagihan Utilitas (Listrik, Air, Gas)": 350_000,
        "Internet": 200_000,
        "Pulsa/Paket Data": 100_000,
        "Transportasi": 400_000,       # Contoh: Bensin/transportasi umum
        "Belanja Kebutuhan Pokok (Groceries)": 800_000, # Makan di rumah lebih hemat
        "Makan di Luar/Hiburan": 200_000, # Harus ketat untuk gaji segini
        "Perawatan Diri/Kesehatan (Obat, Sabun, Dll)": 150_000,
        "Hobi/Hiburan Lain": 150_000,
        "Tabungan/Investasi": 250_000,    # Penting untuk menyisihkan, meskipun kecil
        "Lain-lain/Darurat": 200_000,     # Dana tak terduga
    }

    # Gunakan pengeluaran kustom jika disediakan, jika tidak gunakan contoh
    pengeluaran = custom_pengeluaran if custom_pengeluaran is not None else pengeluaran_contoh

    total_pengeluaran = sum(pengeluaran.values())
    sisa_uang = gaji_bulanan - total_pengeluaran

    print("\n--- RINGKASAN BIAYA BULANAN ---")
    print(f"Gaji Bulanan Anda      : {format_idr(gaji_bulanan)}")
    print("-------------------------------")
    print("DETAIL PENGELUARAN:")
    for kategori, jumlah in pengeluaran.items():
        print(f"- {kategori:<35}: {format_idr(jumlah)}")
    print("-------------------------------")
    print(f"TOTAL PENGELUARAN      : {format_idr(total_pengeluaran)}")
    print("-------------------------------")
    print(f"SISA UANG ANDA         : {format_idr(sisa_uang)}")
    print("-------------------------------")

    if sisa_uang < 0:
        print("\n!!! PERHATIAN: Pengeluaran Anda melebihi gaji. Harap tinjau kembali anggaran Anda. !!!")
    elif sisa_uang > 0:
        print("\nSisa uang bisa ditabung lebih banyak atau digunakan untuk kebutuhan mendadak lainnya.")
    else:
        print("\nAnggaran Anda pas, namun pertimbangkan untuk menyisihkan sedikit untuk dana darurat jika belum ada.")

    return pengeluaran, total_pengeluaran, sisa_uang

if __name__ == "__main__":
    # Gaji bulanan yang akan dihitung (5 juta Rupiah)
    gaji_anda = 5_000_000

    # Pilihan 1: Gunakan pengeluaran contoh
    print("--- Menggunakan Pengeluaran Contoh ---")
    hitung_biaya_bulanan(gaji_anda)

    # Pilihan 2: Jika Anda ingin memasukkan pengeluaran kustom sendiri
    # Anda bisa membuat dictionary baru dengan pengeluaran Anda
    # Hapus atau komentari bagian Pilihan 1 jika Anda ingin menjalankan ini.
    
    print("\n--- Menggunakan Pengeluaran Kustom ---")
    pengeluaran_saya = {
        "Sewa/Cicilan Rumah": 1_000_000,
        "Tagihan Utilitas (Listrik, Air, Gas)": 300_000,
        "Internet": 250_000,
        "Pulsa/Paket Data": 120_000,
        "Transportasi": 500_000,
        "Belanja Kebutuhan Pokok (Groceries)": 900_000,
        "Makan di Luar/Hiburan": 300_000,
        "Perawatan Diri/Kesehatan": 100_000,
        "Hobi/Hiburan Lain": 200_000,
        "Tabungan/Investasi": 500_000,
        "Lain-lain/Darurat": 150_000,
    }
    hitung_biaya_bulanan(gaji_anda, pengeluaran_saya)
    """

    # Pilihan 3: Menggunakan input dari pengguna (lebih interaktif)
    # Ini sedikit lebih kompleks karena memerlukan validasi input angka.
    """
    print("\n--- Memasukkan Pengeluaran Secara Interaktif ---")
    pengeluaran_interaktif = {}
    kategori_input = [
        "Sewa/Cicilan Rumah", "Tagihan Utilitas (Listrik, Air, Gas)", "Internet",
        "Pulsa/Paket Data", "Transportasi", "Belanja Kebutuhan Pokok (Groceries)",
        "Makan di Luar/Hiburan", "Perawatan Diri/Kesehatan", "Hobi/Hiburan Lain",
        "Tabungan/Investasi", "Lain-lain/Darurat"
    ]

    for kategori in kategori_input:
        while True:
            try:
                jumlah = int(input(f"Masukkan biaya {kategori} (Rp): "))
                if jumlah < 0:
                    print("Jumlah tidak boleh negatif. Silakan masukkan angka positif.")
                else:
                    pengeluaran_interaktif[kategori] = jumlah
                    break
            except ValueError:
                print("Input tidak valid. Harap masukkan angka.")
    
    hitung_biaya_bulanan(gaji_anda, pengeluaran_interaktif)

