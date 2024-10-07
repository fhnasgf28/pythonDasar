def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        return True

# list comprehension
prime_list = [x for x in range(2, 100) if is_prime(x)]
print('list of primes:', prime_list)

# menggunakan generator

def primes_generator(limit):
    for num in range(2, limit):
        if is_prime(num):
            yield num

primes_gen = primes_generator(100)
print('primes from generator', list(primes_gen))