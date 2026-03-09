class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Menghitung luas persegi panjang."""
        return self.length * self.width

    def perimeter(self):
        """Menghitung keliling persegi panjang."""
        return 2 * (self.length + self.width)

# Contoh penggunaan
rectangle = Rectangle(5, 3)
print("Luas persegi panjang:", rectangle.area())
print("Keliling persegi panjang:", rectangle.perimeter())

rectangle1 = Rectangle(4, 6)
print("Luas persegi panjang:", rectangle1.area())
print("Keliling persegi panjang:", rectangle1.perimeter())

rectangle2 = Rectangle(7, 8)
print("Luas persegi panjang:", rectangle2.area())
print("Keliling persegi panjang:", rectangle2.perimeter())
