def sapa(nama):
    return f"halo {nama}"
def main():
    nama = input("masukkan nama anda : ")
    hasil = sapa(nama)
    print(hasil)

if __name__ == "__main__":
    main()