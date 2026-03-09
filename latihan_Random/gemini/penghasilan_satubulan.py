import locale

def hitung_konversi_penghasilan(penghasilan_tahunan):
    penghasilan_bulanan = penghasilan_tahunan / 12
    penghasilan_mingguan = penghasilan_tahunan / 52
    penghasilan_harian = penghasilan_tahunan / 365
    return penghasilan_bulanan, penghasilan_mingguan, penghasilan_harian

# Menggunakan locale
try:
    locale.setlocale(locale.LC_ALL, 'id_ID')
except locale.Error:
    locale.setlocale(locale.LC_ALL, '')

# Contoh penggunaan
penghasilan_tahunan = 10000000
penghasilan_bulanan, penghasilan_mingguan, penghasilan_harian = hitung_konversi_penghasilan(penghasilan_tahunan)

def format_currency(amount):
    return f"Rp.: {amount:,.0f}".replace(",", ".")

print(f"Penghasilan tahunan Rp.: {format_currency(penghasilan_tahunan)} {locale.format_string('%d', penghasilan_tahunan, grouping=True)}")
print(f"Penghasilan bulanan Rp.: {locale.format_string('%d', penghasilan_bulanan, grouping=True)}")
print(f"Penghasilan mingguan Rp.: {locale.format_string('%d', penghasilan_mingguan, grouping=True)}")
print(f"Penghasilan harian: Rp.{format_currency(penghasilan_harian)}")