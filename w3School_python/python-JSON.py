# JSON IN PYTHON

import json

# some JSON

x = '{ "name": "John", "age":"30", "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a python dictionary:

print(y['age'])

# convert from python to JSON

# python object
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# convert into JSON:
y = json.dumps(x)
print(y)

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))