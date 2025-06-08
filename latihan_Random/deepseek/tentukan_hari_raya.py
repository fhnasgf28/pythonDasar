from datetime import datetime, date

def tentukan_hari_raya(tanggal_input):
    try:
        tanggal = datetime.strptime(tanggal_input, "%d-%m-%Y").date()
    except ValueError:
        print("Format tanggal tidak valid. Gunakan format dd-mm-yyyy.")
        return None
    
    hari_raya = {
        "Idul Fitri": {"bulan": 4, "hari": 10},
        "Idul Adha": {"bulan": 6, "hari": 17},
        "Natal": {"bulan": 12, "hari": 25},
        "Tahun Baru": {"bulan": 1, "hari": 1},
        "Hari Kemerdekaan RI": {"bulan": 8, "hari": 17}
    }

    # cek hari raya
    for name, data in hari_raya.items():
        if (tanggal.month, tanggal.day) == (data["bulan"], data["hari"]):
            hari_ini = date.today()
            selisih_hari = (tanggal - hari_ini).days

            if selisih_hari == 0:
                return f"Selamat Hari Raya {name}!"
            elif selisih_hari > 0:
                return f"selisih {selisih_hari} hari lagi menuju Hari Raya {name} ({tanggal.strftime('%d-%m-%y')})."
            else:
                return f"selisih {-selisih_hari} hari sudah lewat Hari Raya {name} ({tanggal.strftime('%d-%m-%y')})."
    return f"Tanggal {tanggal_input} bukan Hari Raya yang ditentukan."
# Contoh penggunaan
tanggal_input = "10-04-2023"
print(tentukan_hari_raya(tanggal_input))
tanggal_input = "17-06-2023"
print(tentukan_hari_raya(tanggal_input))
tanggal_input = "25-12-2023"
print(tentukan_hari_raya(tanggal_input))
tanggal_input = "01-01-2023"
print(tentukan_hari_raya(tanggal_input))
tanggal_input = "17-08-2023"
print(tentukan_hari_raya(tanggal_input))
tanggal_input = "15-07-2023"
print(tentukan_hari_raya(tanggal_input))
tanggal_input = "10-04-2024"
print(tentukan_hari_raya(tanggal_input))
tanggal_input = "17-06-2024"
print(tentukan_hari_raya(tanggal_input))