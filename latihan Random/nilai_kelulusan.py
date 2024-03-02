# meningput nilai tugas, UTS, dan UAS
tugas = float(input("Masukan Nilai Tugas\t:"))
uts = float(input("Masukan Nilai UTS\t:"))
uas = float(input("Masukan Nilai UAS \t:"))

# menghitung nilai akhir sesuai dengan bobotnya
nilai = (0.15 * tugas) + (0.35 * uts) + (0.50 * uas)

# menentukan hasil grade =  berdasarkan nilai akhir

if nilai > 80:
    grade = "A"
elif nilai > 70:
    grade = "B"
elif nilai > 60:
    grade = "C"
elif nilai > 50:
    grade = "D"
else:
    grade = "E"

# Menentukan status kelulusan berdasarkan Nilai Akhir
if nilai > 60:
    status = "Lulus"
else:
    status = "Tidak Lulus"
# menampilkan nilai akhir, grade dan status kelulusan
print('Nilai Akhir: %0.2f' % nilai)
print('Grade: {}'.format(grade))
print('Status: {}'.format(status))