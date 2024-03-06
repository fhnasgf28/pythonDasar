''' kwargs'''

def fungsi(nama, tinggi,berat):
    '''Fungsi biasa'''
    print(f'{nama} punya tinggi {tinggi} dan berat {berat}')
fungsi("Ucup", 169, 156)

def fungsi(**kwargs):
    '''fungsi kwargs'''

    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]

    print(f'{nama} punya tinggi {tinggi} dan berat {berat}')
fungsi(nama="farhan", tinggi=183,berat=78)

# study kasus

def math(*args, **kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output +=angka
    elif kwargs["option"] == "Kali":
        output = 1
        for angka in args:
            output *= angka
    else:
        print("tidak ada operasi")
    return output

hasil =math(1,2,3,4,5,option="tambah")

print(f"hasil jumlah {hasil}")
hasil = math(1,2,3,4,option="kali")
print(f"hasil kali {hasil}")