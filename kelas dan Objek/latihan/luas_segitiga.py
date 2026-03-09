class Segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def get_luas(self):
        return 0.5 * self.alas * self.tinggi


segitiga1 = Segitiga(5, 10)
segitiga2 = Segitiga(10, 10)

print('luas segitiga\t:', segitiga1.get_luas())
print('Luas segitiga2\t:', segitiga2.get_luas())
