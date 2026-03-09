months = {
    "januari": 31,
    "februari": 28,
    "maret": 31,
    "april": 30,
    "mei": 31,
    "juni": 30,
    "juli": 31,
    "agustus": 31,
    "september": 30,
    "oktober": 31,
    "november": 30,
    "desember": 31
}

def get_days(month):
    return months.get(month.lower(), "bulan tidak valid")

print("Jumlah hari dalam mei:", get_days("mei"))