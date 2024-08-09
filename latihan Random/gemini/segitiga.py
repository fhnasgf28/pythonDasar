N = int(input("Masukkan nilai N: "))

def is_prima(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

print("Bilangan prima dari 2 sampai", N, ":")
for num in range(2, N+1):
    if is_prima(num):
        print(num)
