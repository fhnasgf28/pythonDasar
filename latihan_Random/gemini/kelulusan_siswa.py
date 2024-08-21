nilai_siswa = 80
nilai_kelulusan = 78

lulus = nilai_siswa >= nilai_kelulusan

if lulus:
    print("Selamat, Kamu lulus")
else:
    print("Semangat untuk ujian berikutnya")


hari_ini = "Minggu"
hari_libur = hari_ini == "Minggu"

if hari_libur:
    print("Hari ini hari libur")
else:
    print("Hari ini hari kerja")

umur = 10
umur_anak = 12

menu_anak_anak = umur < umur_anak

if menu_anak_anak:
    print("Anda boleh memesan menu anak anak")

else:
    print("Anda boleh memilih menu dewasa")