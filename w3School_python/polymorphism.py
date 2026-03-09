# class polymorphism
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive")


class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail")


class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print('fly')


car1 = Car('ford', 'Mustang')
boat1 = Boat('Ibiza', 'Toring 20')
plane1 = Plane('Boing', '747')

for x in (car1, boat1, plane1):
    x.move()

# Belum paham bos