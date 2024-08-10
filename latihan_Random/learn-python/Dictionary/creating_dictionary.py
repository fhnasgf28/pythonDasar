products = {'Jeans': 49.99, 'T-Shirt': 14.99, 'Suit': 89.99}

countries = {'France': 'Paris', 'Japan': 'Tokyo', 'Chile': 'Santiago'}

print(countries['France'])
print(countries['Japan'])

# getting all keys and Values

print(countries.keys())
print(countries.values())

# add key and values
keys_view = countries.keys()

countries['Canada'] = 'Ottawa'

print(keys_view)