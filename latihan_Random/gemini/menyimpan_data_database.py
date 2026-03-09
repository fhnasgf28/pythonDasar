import psycopg2
import json

# fungsi untuk membuat koneksi ke database PostgreSQL

def buat_koneksi(host="localhost", port=5432, user="postgres", password="", database=""):
    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        return conn
    except psycopg2.Error as error:
        print(f"Error: {error}")
        return None

# fungsi untuk menambahkan data buku ke database
def tambah_buku(conn, judul, penulis, genre, tahun):
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO books (judul, penulis, genre, tahun) VALUES (%s, %s, %s, %s)", (judul, penulis, genre, tahun))
        conn.commit()
        cur.close()
        print("Data buku berhasil ditambahkan ke database")
    except (Exception,psycopg2.Error) as error:
        print(f"Error: {error}")

# fungsi untuk menghapus data buku dari database
def cari_dan_simpan_ke_json(conn, judul):
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM books WHERE judul ILIKE %s", ('%' + judul + '%',))
        hasil = cur.fetchall()
        cur.close()

        with open("hasil_pencarian.json", "w") as file:
            json.dump(hasil, file, indent=4)
        print("Hasil pencarian disimpan dalam hasil_pencarian.json")
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data:", error)

# membuat koneksi ke database
conn = buat_koneksi()
if conn:
    while True:
        print("Masukkan data buku baru (atau ketik 'keluar' untuk berhenti):")
        judul = input("Judul: ")
        if judul.lower() == "keluar":
            break
        penulis = input("Penulis: ")
        tahun = input("Tahun: ")
        genre = input("Genre: ")

        # Tambahkan buku ke database
        tambah_buku(conn, judul, penulis, tahun, genre)

#     cari buku berdasarkan judul yang diinputkan user
    judul_cari = input("Masukkan judul buku yang ingin dicari: ")
    cari_dan_simpan_ke_json(conn, judul_cari)
    conn.close()
else:
    print("Gagal membuat koneksi ke database")
