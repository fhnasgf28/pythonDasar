# membuat list uuntuk menyimpan nilai
grades = []
while True:
    grade = float(input("Masukan Nilai: "))
    if grade < 0:
        break
    grades.append(grade)
    
    # mencetak semua nilai
    print("Nilai yang dimasukan:", grades)