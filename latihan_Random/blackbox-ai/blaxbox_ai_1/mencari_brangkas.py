brankas = {
    "kunci1": "kunci1",
    "kunci2": "kunci2",
    "kunci3": "kunci3",
    "kunci4": "kunci4",
    "kunci5": "kunci5",
    "kunci6": "kunci6",
    "kunci7": "kunci7",
    "kunci8": "kunci8",
    "kunci9": "kunci9",
    "kunci10": "kunci10",
    "kunci11": "kunci11",
    "kunci12": "kunci12",
    "kunci13": "kunci13",
    "kunci14": "kunci14",
    "kunci15": "kunci15",
    "kunci16": "kunci16",
    "kunci17": "kunci17",
    "kunci18": "kunci18",
    "kunci19": "kunci19",
    "kunci20": "kunci20",
    "kunci21": "kunci21",
    "kunci22": "kunci22",
}

def cari_data(kunci):
    '''fungsi untuk mencari data berdasarkan kunci'''
    if kunci in brankas:
        return brankas[kunci]
    else:
        return "Data tidak ditemukan"

def main():
    print("Selamat datang di Black Box AI")
    while True:
        kunci = input("Masukkan kunci untuk mencari data (atau ketik 'keluar' untuk keluar): ")
        if kunci.lower() == 'keluar':
            print("Terima kasih telah menggunakan Black Box AI")
            break
        hasil = cari_data(kunci)
        print("Hasil pencarian:", hasil)
if __name__ == "__main__":
    main()
