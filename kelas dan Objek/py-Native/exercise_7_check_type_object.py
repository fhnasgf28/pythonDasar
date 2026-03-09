class Vehicle:
    def __init__(self, name, milleage, capacity):
        self.name = name
        self.milleage = milleage
        self.capacity = capacity


class Bus(Vehicle):
    pass


School_bus = Bus('School Volvo', 12, 50)

print(f'Type of School_bus Variable: {type(School_bus)}')
print(f'Type of School_bus School_bus.name: {type(School_bus.name)}')
print(f'Type of School_bus School_bus.milleage: {type(School_bus.milleage)}')
print(f'Type of School_bus School_bus.capacity: {type(School_bus.capacity)}')

# menggunakan isinstance()

print(isinstance(School_bus, Vehicle))