# Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a
# default value of 50.
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return (f"The Seating Capacity of a {self.name} is {capacity} passenger, a maximum speed of {self.max_speed}km"
                f"/h, and a milieage of {self.mileage}km")

class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)
School_bus = Bus('school Volvo', 180, 12)
print(School_bus.seating_capacity())



