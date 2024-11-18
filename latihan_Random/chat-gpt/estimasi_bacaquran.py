import datetime
import json

def calculate_quran_reading(pages_per_day):
    total_pages = 604  # Jumlah total halaman Al-Qur'an
    days_needed = total_pages // pages_per_day
    if total_pages % pages_per_day != 0:
        days_needed += 1  # Tambahkan 1 hari jika ada sisa halaman

    # Hitung tanggal selesai
    start_date = datetime.date.today()
    end_date = start_date + datetime.timedelta(days=days_needed)

    # Hasil
    result = {
        "pages_per_day": pages_per_day,
        "total_pages": total_pages,
        "days_needed": days_needed,
        "start_date": start_date.strftime("%Y-%m-%d"),
        "end_date": end_date.strftime("%Y-%m-%d"),
    }

    # Simpan hasil ke file JSON
    with open("quran_reading_plan.json", "w") as json_file:
        json.dump(result, json_file, indent=4)

    return result

# Input jumlah halaman per hari
try:
    pages_per_day = int(input("Berapa halaman yang akan Anda baca setiap hari? "))
    if pages_per_day <= 0:
        print("Jumlah halaman per hari harus lebih dari 0.")
    else:
        result = calculate_quran_reading(pages_per_day)
        print("\nRencana membaca Al-Qur'an:")
        print(f"Halaman per hari: {result['pages_per_day']}")
        print(f"Total halaman: {result['total_pages']}")
        print(f"Diperlukan waktu: {result['days_needed']} hari")
        print(f"Tanggal mulai: {result['start_date']}")
        print(f"Tanggal selesai: {result['end_date']}")
        print("\nHasil telah disimpan ke file 'quran_reading_plan.json'.")
except ValueError:
    print("Masukkan angka yang valid.")
