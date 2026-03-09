pelanggan = {
    "12345": {
        "nama": "Budi Santoso",
        "tanggal_lahit": "28-08-2000",
        "tagihan": 600000,
    },
    "678960": {
        "nama": "Any Lestari",
        "tanggal_lahir": "1990-08-14",
        "tagihan": 300000
    }
}

# mengakses data pelanggan
print(pelanggan["12345"]["nama"])
print(pelanggan["678960"]["tagihan"])

# mengubah data pelanggan
pelanggan["12345"]["tagihan"] = 800000
print(pelanggan)