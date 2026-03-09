"""" args """
# memasukan data/argument

def fungsi(nama,tinggi,berat):
    print(f'{nama} punya tinggi {tinggi} dan berat {berat}')

fungsi('ucup',170,56)

def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f'{nama} punya tinggi {tinggi} dan berat badan {berat}')

fungsi(['otong', 170, 56])

# kenalan dengan args

def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f'{nama} punya tinggi {tinggi} dan berat badan {berat}')

fungsi("dudung", 160, 70)