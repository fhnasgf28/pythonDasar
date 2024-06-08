# Iterate the mentioned keys using a loop
# Next, check if the current key is present in the dictionary, if it is present, remove it from the dictionary
# To achieve the above result, we can use the dictionary comprehension or the pop() method of a dictionary.

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
# Keys to remove
keys = ["name", "salary"]

for k in keys:
    sample_dict.pop(k)
print(sample_dict)