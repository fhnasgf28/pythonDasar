# OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

school_bus = Bus('shool Volvo', 100, 23)
print('Vehicle name:', school_bus.name, 'speed', school_bus.max_speed, 'mileage', school_bus.mileage)


