from pengolahan_teks import *

teks = "Ini adalah contoh teks untuk modul pengolahan teks"

# hitung_jumlah kata

jumlah_kata = hitung_kata(teks)
print(f"Jumlah kata dalam teks: {jumlah_kata}")

# hitung jumlah huruf
jumlah_huruf = hitung_huruf(teks)
print(f"jumlah huruf dalam teks: {jumlah_huruf}")

# ubah ke huruf besar
teks_besar = change_teks_toUpper(teks)
print(f"Teks dengan huruf besar: {teks_besar}")

# kemunculan_kata
kemunculan_kata = hitung_kemunculan_kata(teks)
print(f"Jumlah Kemunculan kata 'Contoh' {kemunculan_kata}")

gabungkan_teks1 = gabungkan_teks("farhan ", "assegaf")
print(f"kata yang akan digabungkan adalah nama ini {gabungkan_teks1}")