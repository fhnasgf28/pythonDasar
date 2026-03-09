# Program untuk menghitung jarak antara Bulan dan Bumi berdasarkan waktu tertentu
# Menggunakan modul Astropy untuk kalkulasi astronomi

from astropy.coordinates import EarthLocation, get_moon
from astropy.time import Time
from astropy import units as u

def calculate_moon_earth_distance(date_time):
    """
    Menghitung jarak antara Bulan dan Bumi pada waktu tertentu.

    Parameters:
        date_time (str): Waktu dalam format ISO 8601 (contoh: "2024-12-14T00:00:00").

    Returns:
        float: Jarak antara Bulan dan Bumi dalam kilometer.
    """
    try:
        # Waktu yang ditentukan
        time = Time(date_time)

        # Posisi Bulan relatif terhadap Bumi
        moon = get_moon(time)

        # Lokasi Bumi di pusat (geosentrik)
        earth_center = EarthLocation(lat=0, lon=0, height=0)

        # Menghitung jarak antara Bulan dan Bumi
        distance = moon.separation_3d(earth_center)  # Dalam satuan AU (Astronomical Unit)
        distance_km = distance.to(u.km).value

        return distance_km

    except Exception as e:
        return f"Error dalam menghitung jarak: {e}"

# Contoh penggunaan
if __name__ == "__main__":
    date_time = input("Masukkan waktu dalam format ISO 8601 (contoh: 2024-12-14T00:00:00): ")
    distance = calculate_moon_earth_distance(date_time)

    if isinstance(distance, float):
        print(f"Jarak antara Bulan dan Bumi pada {date_time}: {distance:.2f} km")
    else:
        print(distance)
