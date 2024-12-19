class Film:
    def __init__(self, judul, genre, tahun,rating):
        self.judul = judul
        self.genre = genre
        self.tahun = tahun
        self.rating = rating

class Pengguna:
    def __init__(self, id_pengguna):
        self.id_pengguna = id_pengguna
        self.film_ditonton = {}

    def tambah_penilaian(self, film, rating):
        self.film_ditonton[film.judul] = rating

    def rekomendasi(self, daftar_film):
        pass

