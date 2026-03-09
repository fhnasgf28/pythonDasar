# Use the fromkeys() method of dict.

employees = ['kelly', 'Emma']
default = {'designation': 'developer', 'salary': 8000}

res = dict.fromkeys(employees, default)
print(res)
print(res['kelly'])