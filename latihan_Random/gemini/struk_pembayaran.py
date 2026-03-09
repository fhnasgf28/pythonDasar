import locale
from prettytable import PrettyTable

def buat_struk(nama_toko, alamat_toko, barang_list, diskon=0, pajak=0):
    """Membuat struk penjualan.

        Args:
            nama_toko (str): Nama toko.
            alamat_toko (str): Alamat toko.
            barang_list (list): List of dictionaries berisi nama barang dan harga.
            diskon (float, optional): Persentase diskon. Defaults to 0.
            pajak (float, optional): Persentase pajak. Defaults to 0.

        Returns:
            str: String berisi struk penjualan.
        """
    locale.setlocale(locale.LC_ALL, "")

    table = PrettyTable(["Nama Barang", "Harga Satuan", "Jumlah", "Subtotal"])
    total_harga = 0
    for barang in barang_list:
        harga_satuan = barang['harga']
        jumlah = barang.get('jumlah', 1)
        subtotal = harga_satuan * jumlah
        total_harga += subtotal
        table.add_row([barang['nama'], locale.currency(harga_satuan), jumlah, locale.currency(subtotal)])

    # hitung diskon dan pajak
    diskon_nominal = total_harga * diskon / 100
    pajak_nominal = (total_harga - diskon_nominal) * pajak /100
    total_bayar = total_harga - diskon_nominal + pajak_nominal

    # Tambahkan baris total, diskon, pajak, dan total bayar
    table.add_row(["", "", "Diskon", locale.currency(-diskon_nominal)])
    table.add_row(["", "", "Pajak", locale.currency(pajak_nominal)])
    table.add_row(["", "", "Total Bayar", locale.currency(total_bayar)])

    # Buat header struk
    struk = f"{'=' * 30}\n{nama_toko.center(30)}\n{alamat_toko.center(30)}\n{'=' * 30}\n"
    struk += str(table)
    struk += f"{'=' * 30}\n"

    return struk


# Contoh penggunaan
barang_list = [
    {'nama': 'Buku', 'harga': 15000, 'jumlah': 2},
    {'nama': 'Pensil', 'harga': 5000},
    {'nama': 'Penghapus', 'harga': 3000}
]
print(buat_struk("Toko Buku Cerdas", "Jl. Pemuda No. 123", barang_list, diskon=5, pajak=10))