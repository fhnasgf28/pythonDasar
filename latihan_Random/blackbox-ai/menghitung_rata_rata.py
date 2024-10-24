
# menghitung rata rata
grades = []
while True:
    grade = float(input("Masukan Nilai: "))
    if grade < 0:
        break
    grades.append(grade)
    
    # mencetak semua nilai
    print("Nilai yang dimasukan:", grades)

    # menghitung rata-rata
    average = sum(grades) / len(grades)
    print("Rata-rata:", average)