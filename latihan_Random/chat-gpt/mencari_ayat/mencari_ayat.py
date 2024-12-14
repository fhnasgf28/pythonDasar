import requests

# Url data surat Alquran
url = "https://cdn.jsdelivr.net/npm/quran-json@3.1.2/dist/quran_id.json"

# fungsi untuk mengambil data dari URL
def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

# fungsi untuk mencari ayat berdasarkan nomor surat dan nomor ayat
def search_surat(data, query):
    result = []
    for surat in data:
        if str(query).lower() == surat["transliteration"].lower() or str(query) == str(surat["id"]):
            result.append(surat)
    return result

#  Fungsi Utama
def main():
    data = fetch_data(url)

    if not data:
        print("Tidak ada data yang dimuat. Pastikan koneksi internet Anda baik.")
        return

    print("Selamat datang di pencarian surat Al-Quran")
    print("=================Anda Bisa Mencari Surat Al-Quran Berdasarkan Nomor Surat atau Nomor Ayat===========================================")

    while True:
        # input dari pengguna
        query = input("\nMasukkan nama transliterasi atau nomor surat (atau ketik 'exit' untuk keluar): ").strip()

        if query.lower() == 'exit':
            print("Terima kasih telah menggunakan aplikasi pencarian surat Al-Quran!")
            break

        # mencari ayat berdasarkan nomor surat dan nomor ayat
        results = search_surat(data, query)
        if results:
            print("Hasil pencarian:")
            for surat in results:
                print(f""" 
                    Nomor Surat: {surat['id']}
                Nama Arab: {surat['name']}
                Transliterasi: {surat['transliteration']}
                Terjemahan: {surat['translation']}
                Jenis Surat: {"Mekah" if surat['type'] == "meccan" else "Madinah"}
                Total Ayat: {surat['total_verses']}
                Ayat Pertama: {surat['verses'][0]['text']}
                Terjemahan Ayat Pertama: {surat['verses'][0]['translation']}
                """)
        else:
            print("Surat atau ayat tidak ditemukan.")

if __name__ == "__main__":
    main()
