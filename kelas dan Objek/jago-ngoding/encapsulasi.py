
# encapsulasi
class Segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
        self.luas = 0.5 * alas * tinggi

segitiga_besar = Segitiga(100, 90)

# akses variabel alas, tinggi dan luas dari luar kelas
print(f'alas\t: {segitiga_besar.alas}')
print(f'tinggi\t: {segitiga_besar.tinggi}')
print(f'luas\t: {segitiga_besar.luas}')


class Mobil:
    def __init__(self, merk):
        self._merk = merk

class MobilBalap(Mobil):
    def __init__(self, merk, total_gear):
        super().__init__(merk)
        self._total_gear = total_gear

    def pamer(self):
#         akses _merk dari subclass
        print(f'ini mobil  {self._merk} dengan total gear {self._total_gear}')

ferari = MobilBalap('ferari', 8)
ferari.pamer()

class Mobil:
    def __init__(self, merk):
        self.__merk = merk

    def tampilkan_merk(self):
        print(f'Merk\t: {self.__merk}')
jip = Mobil('Jeep')
jip.tampilkan_merk()