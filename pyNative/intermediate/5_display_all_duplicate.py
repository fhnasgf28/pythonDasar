import collections
# Use the counter() method of the collection module.
# Create a dictionary that will maintain the count
# of each item of a list. Next, Fetch all keys whose value is greater than 2

sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]

duplicate = []
for item, count in collections.Counter(sample_list).items():
    if count > 1:
        duplicate.append(item)
print(duplicate)

# solusi ke 2
exists = {}
duplicates = []

for x in sample_list:
    if x not in exists:
        exists[x] = 1
    else:
        if exists[x] == 1:
            duplicates.append(x)
        exists[x] += 1
print(duplicates)