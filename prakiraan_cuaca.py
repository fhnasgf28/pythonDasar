class Angin:
  def __init__(self, kecepatan):
    self.kecepatan = kecepatan

  def deskripsi(self):
    if self.kecepatan < 5:
      return "Angin sanagat pelan"
    elif self.kecepatan < 12:
      return "Angin Pelan"
    elif self.kecepatan < 20:
      return "Angin Sedang"
    else:
      return "Angin Kencang"

class Cuaca:
  def __init__(self, suhu, kelembaban, angin):
    self.suhu = suhu 
    self.kelembaban = kelembaban
    self.angin = angin

  def prediksi_cuaca(self):
    if self.suhu < 15 and self.kelembaban > 80:
      return "Hujan"
    elif self.suhu > 30 and self.kelembaban < 40:
      return "Panas"
    else:
      return "Cerah"

# Membuat objek angin
angin_kencang = Angin(25)

# Membuat objek cuaca
cuaca_hari_ini = Cuaca(28, 50, angin_kencang)

# Menampilkan hasil
print("Kecepatan angin:", angin_kencang.deskripsi())
print("Prediksi cuaca:", cuaca_hari_ini.prediksi_cuaca())
