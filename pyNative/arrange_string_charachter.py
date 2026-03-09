str1 = "PYnaTiVE"
print("Original String", str1)
lower = []
upper = []
for char in str1:
    if char.islower():
        # add lowercase charachter to lower list
        lower.append(char)
    else:
        upper.append(char)

sorted_str = ''.join(lower + upper)
print('Result:', sorted_str)