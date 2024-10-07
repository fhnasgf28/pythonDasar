print("Hari ini adalah hari yang baik untuk jiwa yang sedang sepi")

# Assign String to a Variable

a = "Hello"
print(a)

# Multiline Srings

a = """
nama saya adalah farhanassegaf yang sedang berusaha untuk memahami sesuatu dan ingin belajar lebih banyak lagi
"""
print(a)

# Strings are Arrays
a = "Hallo, dunia"

print(a[1])

# looping Through a string
for x in "banana":
    print(x)

# string length
print(len(a))

# check string
txt = "The Best things in life are free"
if "free" in txt:
    print("free" in txt)

    # slicing
    b = "Hello, World"
    print(b[2:5])

    # Slice From the Start
    print(b[2:])

    # upper case
    a = 'Hello, World'
    print(a.upper())

    # lower case
    a = 'Hello, World '
    print(a.lower())

    # remove whitespace
    print(a.strip())

    # replace string
    print(a.replace("H", "W"))

    # split string
    print(a.split(","))