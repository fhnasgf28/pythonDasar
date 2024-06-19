# Exercise 10: Remove duplicates from a list and create a tuple
# and find the minimum and maximum number

sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

print('Original list', sample_list)

sample_list = list(set(sample_list))
print("Unique list", sample_list)

t = tuple(sample_list)
print('tuple', t)

print("minimum number is ", min(t))
print("Maximum number is :", max(t))