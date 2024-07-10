def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


number = int(input("Masukan Bilangan\t:"))
if is_prime(number):
    print(f"{number} adalah bilangan prima")
else:
    print(f"{number} bukan bilangan prima")
