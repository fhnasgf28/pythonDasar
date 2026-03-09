import requests
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
import json

# Url data surat Alquran
url = "https://cdn.jsdelivr.net/npm/quran-json@3.1.2/dist/quran_id.json"
local_file = "quran.json"

# fungsi untuk mengambil data dari URL
def fetch_data(url):
    try:
        print(f"Fetching data from {url}")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        print(f"Data fetched successfully from {url}")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        if os.path.exists(local_file):
            with open(local_file, "r") as file:
                return json.load(file)
        else:
            print(f"Local file {local_file} not found.")
            return []

# fungsi untuk mencari ayat berdasarkan nomor surat dan nomor ayat
def search_surat(data, query):
    result = []
    for surat in data:
        if str(query).lower() == surat["transliteration"].lower() or str(query) == str(surat["id"]):
            result.append(surat)
    return result

def save_to_pdf(surat, filename="surat_alquran.pdf"):
    try:
        pdf = canvas.Canvas(filename, pagesize=letter)
        pdf.setTitle("Surat Alquran")
        pdf.setFont("Times-Roman", 12)
        y_position = 750

        # Menulis informasi surat ke PDF
        pdf.drawString(50, y_position, "Hasil Pencarian Surat Al-Qur'an:")
        y_position -= 20
        pdf.drawString(50, y_position, f"Nomor Surat    : {surat['id']}")
        y_position -= 20
        pdf.drawString(50, y_position, f"Nama Arab      : {surat['name']}")
        y_position -= 20
        pdf.drawString(50, y_position, f"Transliterasi  : {surat['transliteration']}")
        y_position -= 20
        pdf.drawString(50, y_position, f"Terjemahan     : {surat['translation']}")
        y_position -= 20
        pdf.drawString(50, y_position, f"Jenis Surat    : {'Mekah' if surat['type'] == 'meccan' else 'Madinah'}")
        y_position -= 20
        pdf.drawString(50, y_position, f"Total Ayat     : {surat['total_verses']}")
        y_position -= 40

        # Menulis ayat-ayat surat ke PDF
        pdf.drawString(50, y_position, "Ayat Pertama:")
        y_position -= 20
        pdf.drawString(50, y_position, surat["verses"][0]["text"])
        y_position -= 20
        pdf.drawString(50, y_position, f"Terjemahan: {surat['verses'][0]['translation']}")

        pdf.save()
        print(f"Surat Alquran berhasil disimpan dalam {filename}")
    except Exception as e:
        print(f"Error saving PDF: {e}")

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

        #         menyimpan hasil pencarian ke PDF
            save_option = input("Apakah Anda ingin menyimpan hasil pencarian ke PDF? (y/n): ").strip().lower()
            if save_option == 'y':
                file_name = input("Masukkan nama file PDF: ").strip()
                file_name = file_name if file_name else "surat_alquran.pdf"
                save_to_pdf(results[0], file_name)
        else:
            print("Surat atau ayat tidak ditemukan.")

if __name__ == "__main__":
    main()
