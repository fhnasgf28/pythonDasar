import geocoder

def get_current_location():
    current_location = geocoder.ip('me')
    if current_location.latlng:
        return current_location.address
    else:
        return "Gagal mendapatkan lokasi." or None

if __name__ == "__main__":
    current_location = get_current_location()
    if current_location:
        print(f"Lokasi saat ini: {current_location}")
    else:
        print("Gagal mendapatkan lokasi.")