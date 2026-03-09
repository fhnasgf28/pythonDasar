class Film:
    def __init__(self, judul, genre, tahun, rating):
        self.judul = judul
        self.genre = genre
        self.tahun = tahun
        self.rating = rating

    def __repr__(self):
        return f"Film(judul='{self.judul}', genre={self.genre}, tahun={self.tahun}, rating={self.rating})"


class Pengguna:
    def __init__(self, id_pengguna):
        self.id_pengguna = id_pengguna
        self.film_ditonton = {}

    def tambah_penilaian(self, film, rating):
        self.film_ditonton[film.judul] = rating

    def rekomendasi(self, daftar_film):
        pass

def rekomendasi_berdasarkan_genre(pengguna, daftar_film):
    genre_favorit = set(genre for film, rating in pengguna.film_ditonton.items() if rating >= 4)


def rekomendasi_berdasarkan_genre(pengguna, daftar_film):
    # Create a mapping of film titles to Film objects
    film_mapping = {film.judul: film for film in daftar_film}

    # Find genres of films rated 4 or higher
    genre_favorit = set(
        genre
        for film_title, rating in pengguna.film_ditonton.items()
        if rating >= 4 and film_title in film_mapping
        for genre in film_mapping[film_title].genre
    )

    # Generate recommendations based on favorite genres
    rekomendasi = [
        film for film in daftar_film if any(genre in genre_favorit for genre in film.genre)
    ]
    return rekomendasi


# Contoh penggunaan
# buat beberapa objek film
film1 = Film("The Shawshank Redemption", ["Drama", "Drama"], 1994, 9.2)
film2 = Film("The Godfather", ["Crime", "Drama"], 1972, 9.2)
film3 = Film("The Dark Knight", ["Action", "Crime"], 2008, 9.0)
film4 = Film("Pulp Fiction", ["Crime", "Drama"], 1994, 8.9)
film5 = Film("Schindler's List", ["Biography", "Drama", "History"], 1993, 8.9)

# buat objek pengguna
user1 = Pengguna("user1")
user1.tambah_penilaian(film1, 9)
user1.tambah_penilaian(film2, 9)
user1.tambah_penilaian(film3, 9)
user1.tambah_penilaian(film4, 9)
user1.tambah_penilaian(film5, 9)

# buat daftar film
daftar_film = [film1, film2, film3, film4, film5]

# rekomendasi berdasarkan genre favorit
rekomendasi_user1 = rekomendasi_berdasarkan_genre(user1, daftar_film)
print(f"Rekomendasi film untuk user1: {rekomendasi_user1}")
for film in rekomendasi_user1:
    print(f"Judul: {film.judul}, Genre: {film.genre}, Tahun: {film.tahun}, Rating: {film.rating}")