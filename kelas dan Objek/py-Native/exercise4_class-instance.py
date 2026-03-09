# OOP Exercise 5: Define a property that must have the same value for every class instance (object)
# Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.
class Vehicle:
    color = 'White'

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass


School_bus = Bus('School Volvo', 180, 13)
print('Color :',School_bus.color, School_bus.name, 'Speed:', School_bus.max_speed, 'Mileage:', School_bus.mileage)

car = Car('Audi Q5', 240, 19)
print('Color :',car.color, car.name, 'speed:', car.max_speed, 'Mileage:', car.mileage)
