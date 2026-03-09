# Daftar nama-nama Asmaul Husna
asmaul_husna = [
    "Ar-Rahman", "Ar-Rahim", "Al-Malik", "Al-Quddus", "As-Salam",
    "Al-Mu'min", "Al-Muhaymin", "Al-Aziz", "Al-Jabbar", "Al-Mutakabbir",
    "Al-Khaliq", "Al-Bari'", "Al-Musawwir", "Al-Ghaffar", "Al-Qahhar",
    "Al-Wahhab", "Ar-Razzaq", "Al-Fattah", "Al-Alim", "Al-Qabid",
    "Al-Basit", "Al-Khafid", "Ar-Rafi'", "Al-Mu'izz", "Al-Mudhill",
    "As-Sami'", "Al-Basir", "Al-Hakam", "Al-Adl", "Al-Latif",
    "Al-Khabir", "Al-Halim", "Al-Azim", "Al-Ghafur", "Ash-Shakur",
    "Al-Kabir", "Al-Hafiz", "Al-Muqit", "Al-Hasib", "Al-Jalil",
    "Al-Karim", "Ar-Raqib", "Al-Mujib", "Al-Wasi'", "Al-Hakim",
    "Al-Wadud", "Al-Majid", "Al-Ba'ith", "Ash-Shahid", "Al-Haqq",
    "Al-Wakil", "Al-Qawi", "Al-Matin", "Al-Wali", "Al-Hamid",
    "Al-Muhsi", "Al-Mubdi'", "Al-Mu'id", "Al-Muhyi", "Al-Mumit",
    "Al-Hayy", "Al-Qayyum", "Al-Wajid", "Al-Majid", "Al-Wahid",
    "Al-Ahad", "As-Samad", "Al-Qadir", "Al-Muqtadir", "Al-Muqaddim",
    "Al-Mu'akhkhir", "Al-Awwal", "Al-Akhir", "Az-Zahir", "Al-Batin",
    "Al-Wali", "Al-Muta'ali", "Al-Barr", "At-Tawwab", "Al-Muntaqim",
    "Al-'Afuww", "Ar-Ra'uf", "Malik-ul-Mulk", "Al-Dhu al-Jalali wal-Ikram",
    "Al-Muqsit", "Al-Jami'", "Al-Ghani", "Al-Mughni", "Al-Mani'",
    "Ad-Darr", "An-Nafi'", "An-Nur", "Al-Hadi", "Al-Badi'",
    "Al-Baqi", "Al-Warith", "Ar-Rashid", "As-Sabur"
]

# fungsi untuk mencari nama asmaul husna berdasarkan input angka
def get_asmaul_husna_by_number(number):
    if 1 <= number <= 99:
        return asmaul_husna[number - 1]
    else:
        return None
#     mendapatkan input dari pengguna
try:
    user_input = int(input("Masukkan angka dari 1 sampai 99 untuk mencari nama Asmaul Husna :"))
    found_name = get_asmaul_husna_by_number(user_input)

    if found_name:
        print(f"Nama Asmaul Husna yang ditemukan: {found_name}")
    else:
        print("Angka tidak valid. Silakan masukkan angka antara 1 sampai 99")
except ValueError:
    print("Input tidak valid. Harap masukkan angka yang benar")
# fungsi untuk mencari nama asmaul husna


def search_asmaul_husna(query):
    results = [name for name in asmaul_husna if query.lower() in name.lower()]
    return results

# mendapatkan input dari pengguna
user_input = input("Masukkan nama atau bagian dari nama Asmaul Husna yang ingin dicari")
# mencari dan menampilkan hasil
found_names = search_asmaul_husna(user_input)
if found_names:
    print('Nama-nama asmaul husna yang ditemukan:')
    for name in found_names:
        print(name)

else:
    print('Tidak ada nama yang ditemukan')