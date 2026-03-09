import datetime
import json


def hitung_suara(data_suara):
    """
    Fungsi untuk menghitung jumlah suara dari setiap daerah

    """

    pemenang = ""
    jumlah_suara_terbanyak = 0
    total_suara = sum(data_suara.values())
    for kandidat, suara in data_suara.items():
        if suara > jumlah_suara_terbanyak:
            pemenang = kandidat
            jumlah_suara_terbanyak = suara
    persentase_pemenang = (jumlah_suara_terbanyak / total_suara) * 100
    return pemenang, total_suara, persentase_pemenang

def simpan_json(pemenang, total_suara, persentase_pemenang):
    data = {"pemenang": pemenang}
    with open("pemenang.json", "w") as file:
        json.dump(data, file)

    waktu_pemilihan = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {
        "pemenang": pemenang,
        "waktu_pemilihan": waktu_pemilihan,
        "total_suara": total_suara,
        "persentase_pemenang": persentase_pemenang

    }


# contoh penggunaan 
tata_suara = {
    "Kota A": 100,
    "Kota B": 200,
    "Kota C": 150,
    "Kota D": 250,
    "Kota E": 300,
    "Kota F": 180,
    "Kota G": 220,
    "Kota H": 90,
    "Kota I": 400,
    "Kota J": 140,
    "Kota K": 170,
    "Kota L": 350,
    "Kota M": 50,
    "Kota N": 275
}

pemenang, total_suara, persentase_pemenang = hitung_suara(tata_suara)
print("Pemenang adalah:", pemenang)
print("Total suara:", total_suara)
print("Persentase suara pemenang:", persentase_pemenang)

simpan_json(pemenang, total_suara, persentase_pemenang)
print("Hasil pemilihan telah disimpan ke file hasil_pemilihan.json")
