import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Penambahan dua vektor
    def __add__(self, other):
        pass

    # Pengurangan dua vektor
    def __sub__(self, other):
        pass

    # Perkalian vektor dengan skalar
    def __mul__(self, scalar):
        pass

    # Kesamaan dua vektor
    def __eq__(self, other):
        pass

    # Perbandingan panjang vektor
    def __lt__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __le__(self, other):
        pass

    def __ge__(self, other):
        pass

    # Representasi string yang ramah pengguna
    def __str__(self):
        pass

    # Representasi string untuk debugging
    def __repr__(self):
        pass

    # Panjang (magnitude) vektor
    def __abs__(self):
        pass

# contoh penggunaan
vector1 = Vector(1, 2)
vector2 = Vector(3, 4)
vector3 = vector1 + vector2

print(vector3)

vector4 = vector1 - vector2

print(vector4)

vector5 = vector1 * 2

v1 = Vector(3, 4)
v2 = Vector(1, 2)

# Operasi aritmatika
v3 = v1 + v2  # Penambahan
v4 = v1 - v2  # Pengurangan
v5 = v1 * 2   # Perkalian skalar

# Perbandingan
print(v1 == v2)  # False
print(v1 > v2)   # True
print(v1 <= v2)  # False

# Panjang vektor
print(abs(v1))  # Output: 5.0 (karena sqrt(3^2 + 4^2) = 5)