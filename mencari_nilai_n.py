def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n - 1)

n = int(input("Masukkan nilai n: "))
hasil = faktorial(n)
print(f"Faktorial dari {n} adalah {hasil}")