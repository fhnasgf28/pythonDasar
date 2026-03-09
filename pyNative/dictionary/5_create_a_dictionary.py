sample_dict = {
    'name': 'kelly',
    'age': 23,
    'salary': 9000,
    'city': 'new york'
}

# keys to extrack
keys = ['name', 'salary']

newDict = {k: sample_dict[k] for k in keys}
print(newDict)


# menggunakan method update
res = dict()
for k in keys:
    res.update({k: sample_dict[k]})
print(res)