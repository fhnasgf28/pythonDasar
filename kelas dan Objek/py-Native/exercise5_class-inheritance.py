# Given:
#
# Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating
# capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So
# total fare for bus instance will become the final amount = total fare + 10% of the total fare.
#
# Note: The bus seating capacity is 50. so the final fare amount should be 5500. You need to override the fare()
# method of a Vehicle class in Bus class.

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 10 / 100
        return amount


School_bus = Bus('School Volvo', 10, 50)
print('Total bus fare is:', School_bus.fare())

'''Overall effect: The entire expression amount += amount * 10 / 100 essentially increases the value stored in amount 
by 10% of itself. It's a concise way to write amount = amount + (amount * 10 / 100).'''