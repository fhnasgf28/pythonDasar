# Use the zip() function. This function takes two or more iterables (like list, dict, string), aggregates them in a tuple, and returns it.
#
# Or, Iterate the list using a for loop and range() function. In each iteration, add a new key-value pair to a dict using the update() method

keys = ['Ten', 'Twenty', 'Thirty']
values = [10,20,40]

res_dict = dict(zip(keys, values))
print(res_dict)

# cara ke dua
res_dict1 = dict()
for i in range(len(keys)):
    res_dict1.update({keys[i]: values[i]})
print(res_dict1)