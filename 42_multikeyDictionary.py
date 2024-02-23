import datetime

mahasiswa1 = {
    'nama': 'ucup',
    'nim': '19106311',
    'sks_lulus':130,
    'beasiswa': False,
    'lahir': datetime.datetime(2001, 4, 10)
}

mahasiswa2 = {
    'nama': 'otong1',
    'nim': '19106312',
    'sks_lulus': 120,
    'beasiswa': True,
    'lahir': datetime.datetime(2001, 5, 11)
}

mahasiswa3 = {
    'nama': 'otong2',
    'nim': '18106312',
    'sks_lulus': 140,
    'beasiswa': False,
    'lahir': datetime.datetime(2000, 8, 11)
}

data_mahasiswa = {
    'MAH001': mahasiswa1,
    'MAH002': mahasiswa2,
    'MAH003': mahasiswa3
}

print(f"{'KEY':<6} {'Nama':<16} {"SKS Lulus":<3} {"Beasiswa":<9} {"Lahir":<10}")
print("_"*50)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa

    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY] ['nim']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

    print(f"{KEY:<6} {NAMA:<16} {SKS:<3} {BEASISWA:<9} {LAHIR:<10}")

