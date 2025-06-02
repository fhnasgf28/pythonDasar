def hitung_probabilitas_hujan(jumlah_mendung_hujan, jumlah_mendung_total):
  """Menghitung probabilitas hujan berdasarkan data mendung.

  Args:
    jumlah_mendung_hujan: Jumlah hari mendung yang diikuti hujan.
    jumlah_mendung_total: Jumlah total hari mendung yang diobservasi.

  Returns:
    Probabilitas hujan ketika mendung (angka antara 0 dan 1).
    Mengembalikan None jika jumlah_mendung_total adalah 0 untuk menghindari division by zero.
  """
  if jumlah_mendung_total == 0:
    return None
  probabilitas = jumlah_mendung_hujan / jumlah_mendung_total
  return probabilitas

# Contoh penggunaan data
mendung_hujan = 30  # Misalnya, dari 50 hari mendung, 30 di antaranya hujan
total_mendung = 50

probabilitas = hitung_probabilitas_hujan(mendung_hujan, total_mendung)

if probabilitas is not None:
  print(f"Jumlah hari mendung yang diikuti hujan: {mendung_hujan}")
  print(f"Jumlah total hari mendung yang diobservasi: {total_mendung}")
  print(f"Probabilitas hujan ketika mendung adalah: {probabilitas:.2f}")
else:
  print("Tidak ada data mendung yang diobservasi.")
