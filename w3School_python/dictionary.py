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
y = thisdict.values()

print(y)

thisdict['brand'] = "Toyota"
print(y)

# get items
y = thisdict.items()
print(y)

if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict")

# python - change dictionary items
# change Values
thisdict["year"] = 2020
print(thisdict)

# update dictionary
thisdict.update({"year": 2024})
print(thisdict)

# python - Remove Dictionary items

# Removing Items
thisdict.pop("model")
print(thisdict)

# menghapus semua dict clear()

thisdict.clear()
print(thisdict)

