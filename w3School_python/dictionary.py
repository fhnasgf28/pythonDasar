# Dictionary

thisdict = {
    "brand": "ford",
    "model": "Mustang",
    "year": 1964,
}

print(thisdict["brand"])

# Changeable

# Duplicates Not Allowed
# dictionary Length

print(len(thisdict))

# Dictionary Items - Data Types
thisdict1 = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

# Accessing Items
x = thisdict.get("brand")
print(x)

# get keys
x = thisdict.keys()
print(x)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()
print(x) #before the change

car["color"] = "White"
print(x)

# get Values