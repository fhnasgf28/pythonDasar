def buat_resume(nama, alamat, pendidikan, pengalaman_kerja, keterampilan):
    resume = f"""
        =========================
        Resume Pribadi
        =========================

        Nama : {nama}
        Alamat : {alamat}
        Pendidikan : {pendidikan}
        Pengalaman Kerja : {pengalaman_kerja}
        Keterampilan : {keterampilan}
        =========================
    """

    return resume

def main():
    print("Selamat datang di pembuatan Resume")

    # input pengguna
    nama  = input("Masukan Nama Anda :")
    alamat = input("Masukan Alamat Anda :")
    pendidikan = input("Masukan Pendidikan Anda :")
    pengalaman_kerja = input("Masukan pengalaman Kerja Anda (pisahkan dengan koma jika lebih dari satu :): ").split(", ")
    keterampilan = input("Masukan Keterampilan Anda (pisahkan dengan koma jika lebih dari satu :): ").split(", ")

    # membuat resume
    resume = buat_resume(nama, alamat, pendidikan, ".\n".join(pengalaman_kerja), ",".join(keterampilan))

    # Menampilkan resume
    print("\nIni adalah resume Anda:")
    print(resume)

    # menyimpan resume
    simpan = input("Apakah anda ingin menyimpan resume dalam file? ya/tidak").lower()
    if simpan == "ya":
        with open("resume.txt", "w") as file:
            file.write(resume)
        print("resume anda telah disimpan dalam file resume.txt")

if __name__ == "__main__":
    main()