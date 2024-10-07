class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def bersuara(self):
        print("Hewan Ini bersuara")


class Anjing(Hewan):
    def bersuara(self):
        print('woof')


class Kucing(Hewan):
    def bersuara(self):
        print("Meow!")

# Membuat Objek
anjing = Anjing("Rex")
kucing = Kucing("Whiskers")

# memanggil method bersuara()
anjing.bersuara()
kucing.bersuara()
