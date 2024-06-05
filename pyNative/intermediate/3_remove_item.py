# Get the list's size
# Iterate list using while loop
# Check if the number is greater than 50
# If yes, delete the item using a del keyword
# Reduce the list size

number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

i = 0
# get list size list

n = len(number_list)

# iterate list till i is smaller than n
while i < n:
    if number_list[i] > 50:
        del number_list[i]
        n = n - 1
    else:
        i = i + 1

print(number_list)

# solusi ke2

# menggunakan for loop dan range()
for i in range(len(number_list) -1, -1, -1):
    if number_list[i] > 50:
        del number_list[i]
print(number_list)