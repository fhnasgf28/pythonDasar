x = lambda a: a + 10
print(x(5))

x = lambda a, b, c: a + b + c
print(x(5, 6, 2))


# why Use lambda Function

def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
print(mydoubler(11))

def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

# contoh lain
greeting = lambda name: print(f"Hello, {name}")
sapa = greeting
greeting("andi")
greeting("Neli")