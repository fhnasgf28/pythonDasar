# Exercise 9: Get all
# values from the
# dictionary and add them to a list but don’t add duplicates

speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

print("Dictionary values - ", speed.values())

speed_list = list()

# iterate dict values
for val in speed.values():
    #check if values not present in a list
    if val not in speed_list:
        speed_list.append(val)
print('UNique List', speed_list)