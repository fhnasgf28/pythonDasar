from weather import get_weather
from travel_notes import TravelNotes

def main():
    print("Selamat datang di aplikasi Travel Notes")

    # mendapatkan cuaca
    location = input("Masukkan lokasi tujuan anda saat ini: ")
    weather_info = get_weather(location)
    print(f"Cuaca saat ini di {location}: {weather_info}")

    # menyimpan catatan perjalanan
    travel_notes = TravelNotes()
    while True:
        action = input("Apakah Anda ingin menambahkan catatan perjalanan? (ya/tidak): ").lower()
        if action == "ya":
            date = input("Masukkan tanggal perjalanan: (YYYY-MM-DD): ")
            place = input("Tempat yang dikunjungi: ")
            note = input("Catatan perjalanan: ")
            travel_notes.add_entry(date, place, note)

        elif action == "tidak":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()