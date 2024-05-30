import platform
import datetime
import mymodule as mx

mx.greeting('Farhan')

# Variables in module

a = mx.person1['age']
print(a)

# Naming a module

# Built-in Modules
x = platform.system()
print(x)

# using the dir() function

# x = dir(platform)
# print(x)

# Import From Module
# Date output
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime('%A'))

# creating date objects

x = datetime.datetime(2020, 5, 17)
print(x)
print(x.strftime('%B'))
# The strftime() method

